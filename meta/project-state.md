# Project State

Last updated: 2026-03-16

This document is the canonical current-state reference for repo structure, compatibility truths, and live open questions. It replaces the old stale backlog-file role with a narrower, actively maintained state doc.

## Current architecture truths

- `agent/onboarding-core.md` is the canonical onboarding source.
- `AGENTS.md` and `CLAUDE.md` are thin tool-specific entry points.
- Canonical skill bodies live only in `.claude/skills/`.
- Claude and Cursor command discovery is handled by thin wrappers in `.claude/commands/` and `.cursor/commands/`.
- Live outputs belong in external situation directories resolved via `--situation`, `.claude/cyberneutics-config.yaml`, or `~/situations/<topic-slug>/`.
- Checked-in run records in this repo are examples or historical records. They are not live runtime outputs.
- `agent/archive/` is historical only and excluded from onboarding unless provenance is explicitly requested.
- When adding cross-references in README files, use markdown links, not backtick paths (convention established 2026-03-07).

## Compatibility migration status

Complete as of 2026-03-07. All items resolved:

- Canonical onboarding doc established.
- Root wrappers aligned to the canonical onboarding doc.
- Canonical skill-source rule established: `.claude/skills/` only.
- Repo-local command wrappers added for Claude and Cursor.
- Runtime-path language converted to situation-directory language.
- Checked-in scenario and deliberation records labeled and housed as examples.
- Structural linting in place to keep these invariants from drifting.

## Recent changes (2026-03-08 through 2026-03-16)

### New content added (2026-03-08)

- `wild/committee-games/committee-as-open-game.md` — Translation of adversarial committee into open games (compositional game theory). Bridge to ACT/Cybercat community.
- `wild/diary/2026-03-13-furry-logic.md` — Diary entry exploring distributional type membership ("furry logic"), extending soft types from graded single-type to multi-type measurement.
- `wild/potential-to-sense/from_semantic_potential_to_situated_sense.md` — Essay on meaning as co-produced in conversation; theoretical grounding for human gates.
- `palgebra/categorical-structures.md` — Pedagogical treatment of category-theoretic constructions in the pipeline (products, coproducts, equalizers, pullbacks, pushouts, fan/funnel as spiders, Probe as universal property test).
- `wild/issues/` — Five GitHub issues from contributors (subagent capabilities, legal domain test case, narrative/archetypes, multimodal deliberation, emotional modeling).

### Documentation updates (2026-03-13)

- Created README.md for `wild/committee-games/` and `wild/potential-to-sense/`.
- Reorganized `wild/README.md` from flat list to categorized sections covering all fourteen topic directories.
- Added `categorical-structures.md` entry to `palgebra/README.md`.
- Completed `cyber-sense` → `cyberneutics` rename sweep in live content (diary entries, example deliberations). Archive files left as historical.
- Refactoring sprint plan created: `agent/prompts/refactoring-sprint-2026-03.md`.

### New content added (2026-03-15)

- `wild/communicating-absent-parties/README.md` — Seven-section synthesis from a 40-page Perplexity deep research report on absent-party communication across eight domains (nuclear semiotics, Pask CT, decipherment, Berea, SETI, information cascades, hermeneutics, biosemiotics). Bridges to pipeline/bath distinction, calibration register at zero-feedback limit, and furry logic.
- `wild/potential-to-sense/pask-machine-machine.md` — Pask's Colloquy of Mobiles (1968) as machine-machine conversation; chameleon-mirror problem, bisimulation as propensity constraint, Pask's machine trajectory from Musicolour to THOUGHTSTICKER.
- `wild/potential-to-sense/README.md` — Updated with pask-machine-machine.md entry and cross-references.
- `wild/diary/2026-03-15-absent-parties-and-chameleons.md` — Absent-party communication as unifying thread; pipeline/bath mapping at calibration register limit; Pask's chameleon-mirror problem; Berea bridge.
- `wild/diary/2026-03-15-emotional-attention-steering.md` — Addresses GitHub issue #13; emotional state as continuous PID-controlled variables per character; bricking/exclusion mechanisms.
- `wild/diary/2026-03-15-mystic-narrative.md` — Jean Houston's Four Levels model as pre-narrative conditioners; maps across shamanic and Diana's Grove lineages; connects to Bruner-Kahneman synthesis.

### Prompt and agent maintenance (2026-03-16)

- `agent/prompts/improve-repo-next-step.md` — Updated bias areas to reflect post-sprint state.
- `agent/prompts/editorial-review.md` — Added `essays/glossary.md` to scope.

## Open decisions

- Whether to record rubric scores as persistent metadata beyond the current review artifacts.
- Whether the cowork plugin should ship under MIT, and whether its runtime behavior needs additional validation before stronger claims are made.
- Whether `wild/potential-to-sense/` should be promoted to `essays/` (polished draft, strong connections to existing theory).
- Whether to add OpenCode to the multi-model committee research program as a Tier 2 platform candidate (per contributor issue #6).
- Whether multimodal inputs (images, diagrams) should be explored as a new research direction (per contributor issue #11).

## Active sprint

A refactoring sprint plan is at `agent/prompts/refactoring-sprint-2026-03.md`. It defines seven workstreams across two passes (core content first, then wild).

Pass 1 audit phase complete (2026-03-13). Reports:
- WS-1 editorial review: `agent/archive/editorial-review-report-2026-03.md` — all 7 dimensions score 2/3; 10-item remediation plan.
- WS-2 cross-reference audit: `agent/archive/cross-reference-audit-2026-03.md` — zero broken links; Bruner edit plan fully executed (9/9, verified 2026-03-16).
- WS-3 research program triage: `agent/archive/research-program-triage-2026-03.md` — all 8 programs relevant; ablation study and agent-independence ready to start.
- WS-7 rubric extensions: `agent/rubrics/repo-consistency.md` — draft of 5 new dimensions (internal consistency, currency, pipeline velocity, formal consistency, practical validation).

Pass 2 complete (2026-03-13). mg reviewed Pass 1 findings and approved remediation (directive: "don't reorder the essays"). Completed:
- WS-4 editorial remediation:
  - Character roster introduction added to `essays/README.md` (Note on the Committee Characters section).
  - Principles vs. Instantiations section added to `essays/05-the-synthesis.md`.
  - Pask forward reference resolved in `essays/05-the-synthesis.md` (Essay 11 callout).
  - Reading difficulty note added to theorist path in `essays/README.md`.
  - Concepts and Definitions index table (19 entries) added to `essays/README.md`.
  - Status and Evolution section rewritten with validated/theoretical/gaps distinction.
  - Societies of Thought arXiv DOI added to README entry.
- WS-5 wild triage: `agent/archive/wild-triage-2026-03.md` — 2 directories ready to promote (potential-to-sense, committee-games); 7 graduation-ready within 4 weeks; 4 remain active research; 1 superseded.
- WS-6 wild cleanup: Status notes added to all 12 wild subdirectory READMEs. Status indicators added to `wild/README.md` with triage report link.

Sprint status: **Complete**. Bruner edits 2/5/8 verified applied (2026-03-16). Remaining longer-term items (worked example, essay promotions from wild/) belong in future sprints.

### Post-sprint: categorical-structures.md focused review (2026-03-13)

`palgebra/categorical-structures.md` received a focused mathematical consistency review against the older palgebra documents. Review report: `agent/archive/categorical-structures-review-2026-03.md`. Key changes: lax/approximate coherence framing added (Mac Lane coherence doesn't hold strictly in stochastic pipelines); overclaimed universal properties weakened to design targets; category **Text** precisely defined; Kleisli and enriched category structures acknowledged; cross-references to committee-games open-game formalization and furry logic distributional types added. Also fixed monad composition direction bug in `palgebra/duality-and-composition.md` (was "Fan ∘ Funnel", should be "Funnel ∘ Fan").

## Scheduled reviews

- **2026-06-08 — Contributor gatekeeping changes**: Has anyone contributed to `wild/` or `wild/diary/`? Has the diary-to-wild-to-formalization pipeline worked for external contributors? Has the maintainer labor model held? Source: `meta/deliberations/contributor-gatekeeping/03-resolution.md`.

## Blocked or prerequisite-dependent items

- A full empirical failure case for `essays/when-methodology-fails.md` still depends on real practice data.
- Some evidence-building tasks in `research-programs/` still depend on running fresh situation-directory workflows rather than repo-local examples.
- ~~The Bruner-Kahneman diary entry 9-edit plan~~ — All 9 edits verified applied as of 2026-03-16. Item closed.

## Docs still needing sweep

- `project-state.md` itself should be updated after each sprint workstream completes. Last sweep: 2026-03-16.
- If this becomes stale, update this section rather than reintroducing a catch-all backlog file.
