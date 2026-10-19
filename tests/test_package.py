import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('package', Path(__file__).resolve().parents[1] / 'scripts/package.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class PackagingBoundary(unittest.TestCase):
    def test_runtime_links_and_entry(self):
        self.assertEqual(len(p.payload()), 9)

    def test_fresh_install_verify_and_tamper(self):
        with tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve()) as d:
            result = p.install(Path(d))
            target = Path(result['installed'])
            p.verify(target, result['content_sha256'])
            with self.assertRaises(ValueError): p.install(Path(d))
            (target / 'SKILL.md').write_text((target / 'SKILL.md').read_text() + '\nchanged\n')
            with self.assertRaises(ValueError): p.verify(target, result['content_sha256'])

    def test_wrong_pin(self):
        with tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve()) as d:
            target = Path(p.install(Path(d))['installed'])
            with self.assertRaises(ValueError): p.verify(target, '0' * 64)

    def test_symlink_destination(self):
        with tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve()) as d:
            root = Path(d); (root / 'real').mkdir(); (root / 'link').symlink_to(root / 'real', target_is_directory=True)
            with self.assertRaises(ValueError): p.install(root / 'link')

    def test_archive_allowlist_and_plugin(self):
        with tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve()) as d:
            out = Path(d) / 'build'; record = p.build(out)
            for archive in out.glob('*.zip'):
                with zipfile.ZipFile(archive) as z:
                    names = z.namelist()
                    self.assertFalse(any('research/' in n or 'docs/' in n or 'tests/' in n or 'private/' in n for n in names))
                    if 'codex-plugin' in archive.name:
                        entry = json.loads(z.read(p.NAME + '/.codex-plugin/plugin.json'))
                        self.assertEqual(entry['skills'], './skills/')
                        for rel, value in p.payload().items(): self.assertEqual(z.read(p.NAME + '/skills/' + p.NAME + '/' + rel), value)
            self.assertEqual(len(record['archives']), 2)
            with self.assertRaises(ValueError): p.build(out)

    def test_unknown_installed_file(self):
        with tempfile.TemporaryDirectory(dir=Path(tempfile.gettempdir()).resolve()) as d:
            target = Path(p.install(Path(d))['installed']); (target / 'extra.txt').write_text('unexpected')
            with self.assertRaises(ValueError): p.verify(target)


if __name__ == '__main__': unittest.main()
