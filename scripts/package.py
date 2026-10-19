#!/usr/bin/env python3
"""Build or install a fresh, explicit, public-only skill. No network or dependencies."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

VERSION = '0.1.2'
NAME = 'mob-presentation'
SOURCE = 'https://github.com/hotmob/mob-presentation'
ROOT = Path(__file__).resolve().parents[1]
PUBLIC = (
    'SKILL.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'agents/openai.yaml',
    'references/contract.md', 'references/content.md', 'references/tools.md',
    'references/quality.md', 'references/sources.md',
)


def reject_symlinks(path):
    path = Path(path).absolute()
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError(f'Symlink is not supported: {part}')
    return path


def payload(root=ROOT):
    root = reject_symlinks(root)
    result = {}
    for rel in PUBLIC:
        p = reject_symlinks(root / rel)
        result[rel] = p.read_bytes()
    text = result['SKILL.md'].decode()
    if not text.startswith('---\nname: mob-presentation\ndescription: '):
        raise ValueError('Unexpected skill entry')
    if len(text.splitlines()) > 90:
        raise ValueError('Keep the skill entry short')
    for rel, data in result.items():
        if not rel.endswith('.md'):
            continue
        for target in re.findall(r'\]\(([^)]+)\)', data.decode()):
            if re.match(r'^[a-z][a-z0-9+.-]*:', target) or target.startswith('#'):
                continue
            p = (root / rel).parent / target.split('#')[0]
            resolved = p.resolve()
            if not resolved.is_relative_to(root.resolve()) or resolved.relative_to(root.resolve()).as_posix() not in PUBLIC:
                raise ValueError(f'Runtime reference escapes package: {rel} -> {target}')
    return result


def manifest(data):
    files = {p: hashlib.sha256(b).hexdigest() for p, b in sorted(data.items())}
    digest = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    try:
        revision = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        revision = None
    return {'schema': 1, 'name': NAME, 'version': VERSION, 'source': SOURCE,
            'source_commit': revision, 'content_sha256': digest, 'files': files}


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def install(skills_dir):
    base = reject_symlinks(skills_dir)
    target = base / NAME
    if target.exists() or target.is_symlink():
        raise ValueError(f'Refusing existing target: {target}')
    data = payload()
    base.mkdir(parents=True, exist_ok=True)
    staged = Path(tempfile.mkdtemp(prefix='.mob-presentation-', dir=base))
    try:
        for rel, content in data.items():
            p = staged / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(content)
        write_json(staged / '.mob-presentation-install.json', manifest(data))
        if target.exists() or target.is_symlink():
            raise ValueError('Target appeared during installation')
        staged.rename(target)
    finally:
        if staged.exists():
            shutil.rmtree(staged)
    return {'installed': str(target), **manifest(data)}


def verify(directory, expected_digest=None):
    directory = reject_symlinks(directory)
    receipt_path = reject_symlinks(directory / '.mob-presentation-install.json')
    receipt = json.loads(receipt_path.read_text())
    actual = manifest(payload(directory))
    if receipt.get('name') != NAME or receipt.get('source') != SOURCE or receipt.get('version') != VERSION:
        raise ValueError('Receipt identity/version mismatch')
    if receipt.get('files') != actual['files'] or receipt.get('content_sha256') != actual['content_sha256']:
        raise ValueError('Installed public files differ from receipt')
    if expected_digest is not None and actual['content_sha256'] != expected_digest:
        raise ValueError('Installed content differs from pinned digest')
    allowed = set(PUBLIC) | {'.mob-presentation-install.json'}
    for p in directory.rglob('*'):
        if p.is_symlink():
            raise ValueError('Symlink in installed skill')
        if p.is_file() and p.relative_to(directory).as_posix() not in allowed:
            raise ValueError('Unexpected installed file')
    return {'verified': str(directory), 'version': VERSION, 'content_sha256': actual['content_sha256'], 'source_commit': receipt.get('source_commit')}


def build(output):
    output = reject_symlinks(output)
    if output.exists():
        raise ValueError('Build output must be a new directory')
    data = payload()
    output.mkdir(parents=True)
    plugin = {'name': NAME, 'version': VERSION, 'description': 'Plan, route and inspect presentations.',
              'author': {'name': 'Mob', 'url': 'https://github.com/hotmob'},
              'homepage': SOURCE, 'repository': SOURCE, 'license': 'MIT', 'skills': './skills/'}
    for kind, prefix in [('skill', NAME + '/'), ('codex-plugin', NAME + '/skills/' + NAME + '/')]:
        with zipfile.ZipFile(output / f'{NAME}-{kind}-{VERSION}.zip', 'w', zipfile.ZIP_DEFLATED) as z:
            for rel, content in data.items():
                z.writestr(prefix + rel, content)
            if kind == 'codex-plugin':
                z.writestr(NAME + '/.codex-plugin/plugin.json', json.dumps(plugin, indent=2) + '\n')
    record = manifest(data)
    record['archives'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(output.glob('*.zip'))}
    write_json(output / 'package-manifest.json', record)
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('check')
    p = sub.add_parser('build'); p.add_argument('--output', type=Path, required=True)
    p = sub.add_parser('install'); p.add_argument('--skills-dir', type=Path, required=True)
    p = sub.add_parser('verify'); p.add_argument('directory', type=Path); p.add_argument('--expected-digest')
    args = parser.parse_args()
    try:
        if args.action == 'check': result = manifest(payload())
        elif args.action == 'build': result = build(args.output)
        elif args.action == 'install': result = install(args.skills_dir)
        else: result = verify(args.directory, args.expected_digest)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as e:
        parser.exit(1, str(e) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
