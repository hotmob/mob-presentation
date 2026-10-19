# Public source review

Retrieved **2026-10-19 UTC**, approximately 11:12–11:13. Repository metadata and default-branch commits came from the GitHub REST API. Counts are a dated snapshot, not a ranking or evidence of quality, installs or active users. `pushed_at` measures repository activity; a component may be older. No external repository code was executed and no dependencies were installed for this review.

Discovery used GitHub queries `presentation skill in:name,description` sorted by stars, plus the three specifically named sources. The query is incomplete by construction. Four complementary approaches were selected; no full-slide multi-tool benchmark was run. The search also surfaced AGPL projects such as `op7418/guizang-ppt-skill`; popularity alone did not justify adding another execution path or copying its code.

| Project | Stars | Latest repository push (UTC) | Reviewed commit | License at relevant scope |
| --- | ---: | --- | --- | --- |
| [PPT Master](https://github.com/hugohe3/ppt-master) | 63,722 | 2026-10-19 03:30 | [`c350bc31e6d43b7bcf5234183d650ba8f9f4c9d7`](https://github.com/hugohe3/ppt-master/tree/c350bc31e6d43b7bcf5234183d650ba8f9f4c9d7) | MIT |
| [Anthropic skills](https://github.com/anthropics/skills) | 182,118 | 2026-10-09 18:45 | [`dbd4588f9e1033efb41dad4bef2f7947c8993d44`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) | **pptx is proprietary/source-available** |
| [presentation-skill](https://github.com/siril9/presentation-skill) | 80 | 2026-10-08 08:21 | [`efd899c5ddf866af2ce0001c4c9340af775d4d55`](https://github.com/siril9/presentation-skill/tree/efd899c5ddf866af2ce0001c4c9340af775d4d55) | MIT |
| [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) | 8,742 | 2026-09-14 07:36 | [`fd1629067909ff55b36b905476de4e5f26062a1f`](https://github.com/lewislulu/html-ppt-skill/tree/fd1629067909ff55b36b905476de4e5f26062a1f) | MIT |

## What the sources establish

**PPT Master:** Maintained presentation workflow with separate generation, design/reference and native-editing routes. Latest release observed was [v6.7.2](https://github.com/hugohe3/ppt-master/releases/tag/v6.7.2), published 2026-10-17. An existing local installation declared v5.0.0; its entry and Huawei preset exactly matched tag commit [`e469064b0ca85eea179a9af60c9182f7fa8baf1a`](https://github.com/hugohe3/ppt-master/tree/e469064b0ca85eea179a9af60c9182f7fa8baf1a). This is a two-file provenance check, not full installation validation. The native routes changed across these versions. Useful when the selected workflow and prerequisites fit; high stars do not prove a better slide.

The [reviewed Huawei preset](https://github.com/hugohe3/ppt-master/blob/e469064b0ca85eea179a9af60c9182f7fa8baf1a/skills/ppt-master/templates/brands/huawei/templates/design_spec.md) explicitly describes approximate style values and no official manual provenance. It is an identity preset, not an official Huawei PowerPoint master. It is not bundled here.

**Anthropic pptx:** Relevant to native PowerPoint creation/editing and output inspection, but the repository's star count covers all skills. The last `skills/pptx` change observed was [`fa0fa64bdc967915dc8399e803be67759e1e62b8`](https://github.com/anthropics/skills/commit/fa0fa64bdc967915dc8399e803be67759e1e62b8), 2026-07-17, earlier than the repository push. Read its [specific license](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/pptx/LICENSE.txt); do not treat it as a reusable MIT/Apache dependency. Referenced only, with no copied or adapted implementation or instructions.

**siril9/presentation-skill:** Latest release [v0.14.0](https://github.com/siril9/presentation-skill/releases/tag/v0.14.0), 2026-10-08. A smaller, recently maintained specialist: structured source planning, repeatable native editable output and rendered QA. Its declared runtime and supported layout vocabulary matter. It is a possible approved backend when those constraints fit, not a generic precision editor for every arbitrary deck. No local installation or execution was established in this study.

**html-ppt-skill:** Static HTML/CSS/JS presentation authoring with theme/layout separation and browser navigation. A useful reference for browser delivery or visual exploration; dependencies such as webfonts affect portability. The reviewed browser workflow does not by itself prove native PPTX editability. No local installation, conversion or rendering was tested here.

## Distribution precedent and limits

[Mob Write](https://github.com/hotmob/mob-write), reviewed at [`bb5aa08918ccc14e8c5402f35431488f86454eaa`](https://github.com/hotmob/mob-write/tree/bb5aa08918ccc14e8c5402f35431488f86454eaa), MIT, latest observed release v0.4.0, supplies the naming/distribution precedent: one canonical skill, on-demand references, explicit local installation, fixed releases and separate private context. Its installer was not copied; this package uses a much smaller original helper and has no in-place upgrade support.

Host presentation and image tools are runtime-dependent, not GitHub dependencies. Their current instructions and available APIs must be checked in the target session. Native OOXML and HTML/SVG are formats/techniques, not proof of an installed tool. No benchmark result or guaranteed cross-host compatibility is claimed.
