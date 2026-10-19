# v0.1.1 validation

The v0.1.0 baseline checks below were repeated after adding audience, notes, evidence, template and auxiliary-design routing details. These additions close gaps found in a method coverage review. No private sources or feedback are bundled.

# Baseline scope

This release is a lightweight instruction and routing package. It has no slide renderer and does not claim to improve presentation quality by a measured amount.

## Small request walkthrough, 2026-10-19

The author exercised the following synthetic requests against the actual entry and references. These are manual route checks, not blinded model trials, audience tests or executions of the named third-party tools. No private presentation content was used. The result column records the selected path and stopping boundary.

| Request and available context | Result |
| --- | --- |
| Change only slide 3's title in a supplied PPTX; original editor available | Bounded edit → tools → original editor. Inspect slide 3 and changed notes/dependencies. No full redesign, no new brand selection. |
| Turn a 20-page technical deck into a shorter partner presentation | Content first; account for all source pages and necessary mechanisms. Choose content destinations before omission. Then choose an available editable authoring owner. |
| Use a real corporate POTX and preserve native charts | Inspect template/layouts, map content, choose native template route. A screenshot or brand preset cannot satisfy master inheritance. |
| Make a diagram of a planned deployment look convincing | Content review preserves “planned”; image tool may supply a clearly conceptual illustration. No claim of an actual deployment and no invented customer evidence. |
| Explore visuals; current candidate has cleaner geometry but communicates the wrong activity | Quality check fails communication despite engineering pass. Keep current best, change the hypothesis and rerender within actual permission/budget. |
| Deliver an editable PPTX; only HTML preview available | HTML preview is insufficient. Find an available supported conversion/editor and test native objects, or report the unmet format/editability requirement. |
| Render service is unavailable after a local edit | Continue source/text checks, mark visual validation incomplete. Do not claim target-app or whole-deck inspection. |
| Use PPT Master v5.0.0 while a search returns v6.7.2 instructions | Read installed v5 router; do not combine native route instructions. No automatic update or integrity-gate bypass. |

The walkthrough did not require changing the eight route decisions. It exposed the need to state review-only scope, local versus full-deck coverage, and version-aware native routes explicitly; those boundaries are present in the entry/references. General model compliance remains unproven.

## Packaging checks

The package helper uses Python's standard library only. Tests cover a fresh isolated installation, receipt and pinned digest, tampering, wrong pins, existing-target refusal, symlink refusal, unexpected installed files, public archive contents and plugin path consistency. Run the commands in the README for the current checkout; final execution results are recorded in the release notes.

Execution on 2026-10-19: **6 packaging tests passed**; the source package check and all relative Markdown file links passed. The first test run exposed macOS's symlinked temporary-directory ancestor; tests now use its canonical path while the installer continues to refuse symlinked destinations. No dependency was installed.

The separate locally supplied `quick_validate.py` could not run because both available Python runtimes lacked PyYAML. Its success is not claimed. The dependency-free package check verified the exact frontmatter prefix and runtime link closure instead; this is narrower than a general YAML validator. These checks establish package structure and source identity, not host discovery, native PowerPoint compatibility, tool installation or visual quality.

## Remaining validation

Fresh host discovery/import, independently observed model routing, real template fidelity, actual editable deck production, cross-renderer differences and measured audience comprehension require future authorized trials. No global skill environment was changed during this release's preparation. No unfamiliar external code was executed.
