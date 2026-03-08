# Implementation Plan: Contributor Gatekeeping Remediation

**Source**: `meta/deliberations/contributor-gatekeeping/03-resolution.md`
**Date**: 2026-03-08

---

## 1. CONTRIBUTING.md — add exploratory path and fix tone

**File**: `CONTRIBUTING.md`

**Change A — Opening paragraph** (line 5): Replace the "compact contribution contract" sentence with language that welcomes contributions at any level of polish.

Current:
> This file is the compact contribution contract: what kinds of work fit here, where they go, and what to verify before opening a PR.

Replace with something like:
> We welcome contributions at every level of polish — from fully-formed artifacts to half-formed ideas. This file explains what kinds of work fit here, where they go, and what to check before opening a PR.

**Change B — Sixth contribution type** (after line 15): Add a bullet to the Contribution Types list:

> - **Exploratory ideas and lateral connections** in `wild/` and `wild/diary/`

**Change C — Placement rule for wild/** (after line 22): Add a rule:

> - Exploratory ideas, field notes, and early-stage connections belong in `wild/`. Raw sketches with no structure go in `wild/diary/`; ideas with enough shape to warrant a topic directory go directly in `wild/`.

**Change D — Expectation-setting** (new section before "Update the Relevant Index"): Add a short section:

> ## Exploratory Contributions
>
> Contributions to `wild/` and `wild/diary/` have a different lifecycle. They are reviewed periodically by the maintainer, not in real time. Acceptance means the idea is being held — not that it will necessarily be developed into a formal artifact. Ideas that connect to existing threads may be promoted to `wild/` topic directories, folded into research programs, or remain as seeds for future work.
>
> The only convention for `wild/diary/` is a date-prefixed filename (`YYYY-MM-DD-short-title.md`). No structural requirements beyond that.

---

## 2. meta/contributor-guide.md — add exploratory routing

**File**: `meta/contributor-guide.md`

**Change A — New contribution path section** (after "Improve repo structure or navigation", line 56): Add:

> ### Explore an idea or connection
>
> Work in `wild/` when you have an idea that isn't ready for the structure of `artifacts/`, `essays/`, or `research-programs/`.
>
> Typical contributions:
> - a half-formed theoretical connection
> - field notes from applying the methodology
> - a lateral analogy worth exploring
> - raw material that might feed into a formal program later
>
> For raw sketches, use `wild/diary/` with a date-prefixed filename (`YYYY-MM-DD-short-title.md`). For ideas with enough shape to warrant their own topic, create a directory under `wild/`.

**Change B — First contributions list** (after line 66): Add item 6:

> 6. Drop an exploratory note in `wild/diary/` connecting the methodology to something from your own domain.

**Change C — Where Things Go** (after line 73): Add:

> - Exploratory ideas and raw field notes belong in `wild/` or `wild/diary/`.

**Change D — Audience table** (line 15): Add a row for exploratory contributors:

> | **Explorers** | Try an idea before committing to structure | `wild/diary/README.md` |

---

## 3. research-programs/README.md — scope the checklist

**File**: `research-programs/README.md`

**Change** (before line 22, "Before you pick a program"): Insert a scope note:

> *This checklist applies to formal research programs with defined protocols and results locations. If you have an exploratory idea that isn't ready for this level of structure, start at [`wild/`](../wild/) instead.*

---

## 4. wild/diary/README.md — confirm on-ramp language

**File**: `wild/diary/README.md`

**Status**: Already updated during the diary move (this session). The current text includes the contributor on-ramp paragraph. Verify it reads well alongside the new `CONTRIBUTING.md` and `contributor-guide.md` language.

**If needed**: Add the naming convention note explicitly:

> Name your file `YYYY-MM-DD-short-title.md`. No other structural requirements.

---

## 5. Three-month review checkpoint

**Action**: Add a follow-up item to `meta/project-state.md` under open decisions or follow-ups:

> - **2026-06-08**: Review contributor gatekeeping changes. Has anyone contributed to `wild/` or `wild/diary/`? Has the diary→wild→formalization pipeline worked for external contributors? Has the maintainer labor model held? Source: `meta/deliberations/contributor-gatekeeping/03-resolution.md`.

---

## 6. Optional: reach out to original contributor

Not a code change. The committee recommended asking the original contributor whether the revised docs would have changed their decision. This is mg's call.

---

## What we are not doing

Per the committee resolution:

- Not rewriting the structural conventions that agents depend on
- Not creating a contributor-experience rubric
- Not removing the validation checklist from research-programs
- Not promising real-time engagement with exploratory contributors

---

## Validation

After implementing:

1. Run `py -3 scripts/lint_repo_docs.py` — confirm pass.
2. Grep for any remaining stale references to the old contribution model that contradict the new exploratory path.
3. Read `CONTRIBUTING.md` and `meta/contributor-guide.md` end-to-end to check that the exploratory path feels like a natural addition, not an afterthought bolted on.
