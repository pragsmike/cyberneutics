# Project State

Last updated: 2026-03-13

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

## Recent changes (2026-03-08 through 2026-03-13)

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

## Open decisions

- Whether to record rubric scores as persistent metadata beyond the current review artifacts.
- Whether the cowork plugin should ship under MIT, and whether its runtime behavior needs additional validation before stronger claims are made.
- Whether `wild/potential-to-sense/` should be promoted to `essays/` (polished draft, strong connections to existing theory).
- Whether to add OpenCode to the multi-model committee research program as a Tier 2 platform candidate (per contributor issue #6).
- Whether multimodal inputs (images, diagrams) should be explored as a new research direction (per contributor issue #11).

## Active sprint

A refactoring sprint plan is at `agent/prompts/refactoring-sprint-2026-03.md`. It defines seven workstreams across two passes (core content first, then wild). Workstreams 1–3 can run in parallel. See that document for details.

## Scheduled reviews

- **2026-06-08 — Contributor gatekeeping changes**: Has anyone contributed to `wild/` or `wild/diary/`? Has the diary-to-wild-to-formalization pipeline worked for external contributors? Has the maintainer labor model held? Source: `meta/deliberations/contributor-gatekeeping/03-resolution.md`.

## Blocked or prerequisite-dependent items

- A full empirical failure case for `essays/when-methodology-fails.md` still depends on real practice data.
- Some evidence-building tasks in `research-programs/` still depend on running fresh situation-directory workflows rather than repo-local examples.
- The Bruner-Kahneman diary entry (`wild/diary/2026-02-17-bruner-kahneman-synthesis.md`) contains an unexecuted 9-edit plan for essay cross-references. Decision needed: execute, revise, or archive.

## Docs still needing sweep

- `project-state.md` itself should be updated after each sprint workstream completes.
- If this becomes stale, update this section rather than reintroducing a catch-all backlog file.
