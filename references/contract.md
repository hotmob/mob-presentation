# Input and output contract

Use ordinary language or the caller's existing records. Do not require a new database or duplicate ledger.

## Inputs, when relevant

| Input | Meaning |
| --- | --- |
| Purpose and audience | What the audience needs to understand, compare or decide; delivery language and presentation versus independent reading |
| Scope | Review, bounded edit, narrative rebuild, creation, template use or delivery; exact pages/objects and what is protected |
| Current artifact | Exact source, format, revision or hash when version ambiguity matters, page order, notes, and current best comparison |
| Evidence references | Authorized facts and sources; distinguish confirmed facts, assumptions, proposed work and unknowns |
| Design references | Actual template or reference assets, ownership and usage constraints; clarify whether a deck supplies content, design or both |
| Output requirements | Local PPTX, Google Slides, Spaces, HTML or PDF; objects that must stay editable, slide count, notes and required copies |
| Execution limits | Available tools and renderer, installation permissions, image/API budget, confidentiality and external-service boundaries |
| Existing decisions | Accepted content or design and the specific object it covers; permission for autonomous revision where given |

Missing optional inputs do not block useful work. Missing facts are not permission to invent them. If the current artifact cannot be located, inspect supplied material and report the exact missing source before dependent editing.

## Working specification

For creation or narrative rebuild, develop the caller's existing brief or spec progressively: start with the working framing and core claim, add page points and order, then refine template and visual decisions from the real sample. Carry known output, brand and content constraints throughout; do not freeze a layout merely to complete an early spec. A short working note is enough when no record exists; do not require a new schema, file or acceptance gate. A local correction reuses the current spec and updates only affected decisions.

That record is the source of truth for this deck's decisions. Refer to facts, brands, assets and prior decisions at their existing authorized owners instead of copying them into a competing source. Update the spec as visual choices or review findings change the intended artifact. It guides production; it is not an audience-facing slide or a reason to display internal evidence checklists.

## Outputs

For a review: page-specific findings, evidence and recommended changes, separated from factual gaps.

For production: editable source and requested deliverables, actual authoring route/version, inspected renders, content and visual findings, engineering checks and known compatibility gaps. Put these in the caller's existing handoff location; do not force a manifest for a trivial edit.

When versions can be confused, bind the checks to the output hash or native document revision. Tool logs belong to their actual output. A later edit requires rechecking the affected evidence.

## Integration boundary

A project adapter supplies authorized input references, fixes dependency versions, enforces its own acceptance process and owns delivery. Mob Presentation knows no private directory layout, task system, brand or business. It does not fetch company records on its own.

Keep confidential inputs and their review logs outside this repository and its packages. Passing a reference does not grant access; confirm the current tool can read it within the task. Public contributions use synthetic or explicitly cleared material.

Pin a release and full commit before adopting the skill. Check the distributed file hashes, then verify discovery in a fresh session. Preserve the old installation and pin for rollback. Upgrade only in a separate test location first; never replace the dependency beneath an active run. A release, local installation and host discovery are three separate observations.
