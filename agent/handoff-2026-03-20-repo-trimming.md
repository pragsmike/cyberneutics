# Handoff: Repository Trimming

**Date**: 2026-03-20
**Session**: Two-pass repo trimming to reduce size and organizational clutter.

---

## What was done

### Pass 1: Examples and wild archive

- Removed two black-swan deliberation directories from `examples/` (already canonical under `research-programs/evaluating-deliberative-architectures/results/deliberations/`). Fixed four files that referenced the old `examples/` location.
- Trimmed examples from 14 deliberation + 3 scenario directories to 5 + 1. Kept representative set: `is-author-crackpot`, `is-author-crackpot-revisited`, `methodology-adoption-strategy`, `eval-delib-architectures`, `soft-type-extension`.
- Created `wild/archive/` and moved 4 dormant topics there: residuality-theory, harness-engineering, neo-cybernetics, software-factories.
- Updated `agent/onboarding-core.md` step 4 to exclude both `agent/archive/` and `wild/archive/`.

### Pass 2: Larger structural trimming

- **Deleted `bradley_thesis.pdf`** (8 MB) from `wild/pask-mesh-fitting/research/`. The thesis is publicly available; the research survey retains the citation.
- **Archived `wild/subagent-personas-for-debate/`** to `wild/archive/` — was marked SUPERSEDED, content absorbed into research-programs.
- **Removed `cowork-plugin/`** — superseded by native `.claude/skills/` and `.cursor/` command structure. Removed the Cowork Plugin section from `README.md`. Open decision about MIT licensing is now moot.
- **Digested 39 archived handoff files** (Jan 29 – Mar 17) into `agent/archive/handoff-digest-2026-01-to-03.md`. Individual files deleted. Active handoffs (03-07c through 03-20) retained in `agent/`.
- **Consolidated pask-mesh-fitting research stubs**: 7 short research notes (7–22 lines each) merged into `research/research-survey.md`. The tractability analysis (`tractability-and-risks.md`, 79 lines) kept separate as the core analytical document. Updated `research/README.md`.

---

## Deferred work

- **Essay 07 redundancy**: The editorial review (`agent/archive/editorial-review-report-2026-03.md`) identified `essays/07-bolands-narrative-engineering.md` as ~30% redundant with essays 01, 05, and 06 (three eras, repetition-produces-difference, charts on a manifold). This is an editorial trim, not a deletion — the essay has unique value but restates material covered elsewhere. Deferred to a future session.

---

## Files modified or created

| File | Change |
|------|--------|
| `agent/onboarding-core.md` | Archive exclusion covers both `agent/archive/` and `wild/archive/` |
| `agent/archive/handoff-digest-2026-01-to-03.md` | New: digest replacing 39 individual handoffs |
| `wild/README.md` | Removed dormant and superseded entries from active sections; added to archive section |
| `wild/pask-mesh-fitting/research/research-survey.md` | New: consolidated 7 research notes |
| `wild/pask-mesh-fitting/research/README.md` | Updated to reference consolidated survey |
| `meta/project-state.md` | Updated architecture truths, recent changes, open decisions |
| `README.md` | Removed cowork-plugin section |
| `agent/handoff-2026-03-20-repo-trimming.md` | This file |
