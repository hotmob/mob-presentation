# Mob Presentation

Make presentations communicate clearly, preserve what must stay editable, and inspect what was actually rendered.

**Series:** Mob Skills · **Project:** Mob Presentation · **Call:** `$mob-presentation` · **License:** MIT

Mob Presentation is a small, host-independent skill for narrative, template inheritance, tool choice, visual revision and delivery review. It contains no slide generator, company facts, brand assets or required paid service. It uses an available authoring tool through that tool's actual instructions.

```text
Request + authorized source + constraints
  ├─ Review / local correction → preserve scope and existing source
  ├─ New narrative / rebuild   → audience, evidence, page plan
  └─ Template / visual work    → inspect reference, test needed choice
                       ↓
             One available authoring owner
                       ↓
       Render → compare → revise → inspect again
                       ↓
     Separate content, visual and engineering checks
                       ↓
             Requested artifact and limits
```

## Use it

> Use $mob-presentation to change only the title on slide 3 of this PPTX. Keep its template, other slides and notes. Return a local editable PPTX.

> Use $mob-presentation to review this deck for a partner meeting. Identify claims without evidence and confusing visual relationships. Do not rewrite the deck yet.

> Use $mob-presentation to build six editable slides from these confirmed facts and this template. Keep the data chart editable. The deployment is planned, not completed.

The current request takes precedence over optional method defaults. A local edit does not start a whole-deck redesign. An image concept is not product or deployment evidence. A successful export is not proof of visual quality.

## Install v0.1.1

Use the fixed release and record its commit. Python 3.9+ is needed only for the standard-library package helper.

```sh
git clone --branch v0.1.1 --depth 1 https://github.com/hotmob/mob-presentation.git mob-presentation-source
cd mob-presentation-source
git rev-parse HEAD
python3 scripts/package.py install --skills-dir /path/to/test-project/.agents/skills
```

The helper writes a fresh `mob-presentation/` directory and a hash receipt. It has no global default, makes no network requests and refuses an existing target or symlinked destination. Use an empty test location your host actually discovers. In a fresh session, verify that the host lists the skill and reads the intended entry. Merely cloning or successfully installing files does not prove discovery.

For an upgrade, install in a separate empty location, check the new release with representative requests, then change the caller's fixed reference. Keep the prior version for rollback. Active sessions and runs keep their prior version. This first release intentionally has no in-place updater or automatic installation of other skills.

```sh
python3 scripts/package.py check
python3 -m unittest discover -s tests -v
python3 scripts/package.py build --output /path/to/new-build
```

The build creates a skill ZIP, a skills-only Codex plugin ZIP and a file-hash manifest. Plugin import depends on the host; a built package does not establish installation or directory publication. The public allowlist excludes work inputs and logs, but cannot detect private prose accidentally added to an allowed file. Review every public file before publishing.

## Files and boundaries

| File | Purpose |
| --- | --- |
| [SKILL.md](SKILL.md) | Short decision entry |
| [Contract](references/contract.md) | Caller-owned facts, design, scope, output and authority |
| [Content](references/content.md) | Narrative and source preservation |
| [Tools](references/tools.md) | Conditions, inputs, outputs and fallbacks |
| [Quality](references/quality.md) | Render inspection, comparison, engineering and learning |
| [Sources](references/sources.md) | Dated public research, revisions and licensing |
| [Validation](docs/validation.md) | Small routing exercise and packaging evidence, with limits |

Projects can integrate the skill with a pinned version, commit and content digest. They retain their own permissions, source records, acceptance and delivery. The skill has no reverse dependency on any organization's directories or runtime.

Tool availability is checked at use time. PPT Master, host presentation APIs, native OOXML tooling, HTML/SVG workflows and image generation have different jobs. None is universally better, and reading their documentation does not make their capabilities available.

## Contribute

Describe a concrete request, observed output, desired behavior and applicability. Use synthetic or authorized public material. Do not include private decks, brand assets, customer data, credentials or private review history. New third-party material needs its own license review.

Original content is [MIT licensed](LICENSE). No third-party implementation, template or skill text is bundled; see [notices](THIRD_PARTY_NOTICES.md).
