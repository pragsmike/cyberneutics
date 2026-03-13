# Refactoring Sprint Plan: March 2026

**Created**: 2026-03-13
**Source**: Session analysis of new material, contributor issues, rubric gaps, and staleness audit.
**Scope**: Two passes — core content first (essays, artifacts, palgebra, meta, research-programs), then wild content.

## Context

The repo has grown significantly since the last editorial review and compatibility sweep (2026-03-07). New palgebra theory, three wild topic directories, five contributor issues, and a diary entry with furry logic type theory extensions have been added. The `project-state.md` open decision "when to rerun the editorial review" is now answerable: now.

Two existing rubrics measure distinct things:

- **Repo audience experience** (`agent/rubrics/repo-audience-experience.md`): 7 dimensions measuring presentation quality for practitioners, theorists, skeptics, formalists.
- **Deliberation evaluation** (`artifacts/evaluation-rubrics-reference.md`): 5 dimensions measuring committee transcript quality.

Neither covers internal consistency, formal consistency, staleness, pipeline health, or research program viability. This sprint addresses all of these.

## Workstreams

### Pass 1: Core Content (essays, artifacts, palgebra, meta, research-programs)

#### WS-1: Editorial Review Rerun

**What**: Run the editorial review prompt (`agent/prompts/editorial-review.md`) against the current essay collection and supporting material. Score all 7 audience-experience dimensions. Produce remediation plan.

**Why**: Last review predates the compatibility sweep, the new palgebra theory, and the conversation-theory essay. The "when to rerun" open decision is now resolved.

**Inputs**: `agent/prompts/editorial-review.md`, `agent/rubrics/repo-audience-experience.md`, all essays, READMEs.

**Output**: `agent/archive/editorial-review-report-2026-03.md` (report + remediation plan).

**Parallelizable**: Yes — independent of WS-2 and WS-3.

**Agent instructions**: Follow the editorial-review prompt exactly. Read the rubric first. Score every dimension. Be specific with file/section citations. The remediation plan should produce concrete, ordered changes traceable to rubric dimensions.

#### WS-2: Cross-Reference and Link Audit

**What**: Systematically verify all internal cross-references, markdown links, and cross-document claims across core content.

**Why**: Growth has introduced potential drift. The palgebra now has four documents; do they agree on notation? Do essay cross-references still land? Are README descriptions accurate?

**Checks**:
1. Run `scripts/lint_repo_docs.py` and record results.
2. For each palgebra document, verify type names and operator syntax match `palgebra/reference.md`.
3. For each essay cross-reference (forward and backward), verify target section exists.
4. For each README description of a document, verify it matches the document's actual content.
5. Check whether the Bruner-Kahneman edit plan (9 edits in `wild/diary/2026-02-17-bruner-kahneman-synthesis.md`) is still wanted. Flag for mg's decision.

**Output**: `agent/archive/cross-reference-audit-2026-03.md` listing all findings, categorized as (a) broken/wrong, (b) stale/drifted, (c) fine.

**Parallelizable**: Yes — independent of WS-1 and WS-3.

**Agent instructions**: Be mechanical. Check every link. Check every type name. Don't fix anything yet — produce the audit. Fixes happen in a follow-up session after mg reviews.

#### WS-3: Research Program Triage

**What**: Assess each of the five research programs for current relevance, feasibility, blockers, and whether they should be updated, archived, or run.

**Why**: Five programs defined, none run. The landscape has changed (Agent Teams exist, OpenCode is a platform candidate per contributor issue #6, furry logic extends soft types). Some may be blocked; some may be stale.

**Programs to assess**:
1. `ablation-study.md` — still feasible? still the right ablation targets?
2. `agent-independence.md` — Agent Teams status? cost model still valid?
3. `committee-implementation-taxonomy.md` — update for OpenCode (per issue #6), current platform landscape.
4. `multi-model-committee.md` — merge with implementation taxonomy? OpenCode as candidate?
5. `evaluating-deliberative-architectures.md` — legal domain test case (per issue #7) as pilot?
6. `societies-of-thought-research-plan.md` — still relevant after the societies-of-thought essay was written?

**Output**: `agent/archive/research-program-triage-2026-03.md` with per-program assessment: status, relevance, blockers, recommended action (run/update/archive/merge).

**Parallelizable**: Yes — independent of WS-1 and WS-2.

**Agent instructions**: Read each program document. For each, assess: (a) is the question still interesting? (b) are the prerequisites met? (c) has anything changed that invalidates or supersedes the design? (d) what's the recommended next action? Note specifically where contributor issues #6 (OpenCode/subagent capabilities) and #7 (legal domain test case) connect.

---

### Pass 1 Gate

After WS-1, WS-2, and WS-3 complete, mg reviews the three reports. Findings feed into:

#### WS-4: Remediation Execution

**What**: Execute the prioritized changes from WS-1 (editorial remediation), WS-2 (link/reference fixes), and WS-3 (program updates/archives).

**Why**: The audits produce findings; this workstream acts on them.

**Inputs**: The three audit/report documents from WS-1, WS-2, WS-3, plus mg's review and prioritization.

**Output**: Modified repo files. Updated `project-state.md`. New handoff.

**Parallelizable**: No — depends on Pass 1 Gate review. But individual remediation items within WS-4 can be parallelized if they touch non-overlapping files.

**Agent instructions**: Work through the prioritized remediation list. Commit in logical batches (e.g., all essay cross-reference fixes together, all palgebra notation fixes together). Run lint after each batch. Update `project-state.md` as items complete.

---

### Pass 2: Wild Content

#### WS-5: Wild Content Triage and Pipeline Assessment

**What**: For each of the fourteen wild topic directories plus `wild/diary/`, assess: status (active/dormant/promoted/archived), graduation readiness, and what would be needed to promote or explicitly shelve.

**Why**: Wild has grown large. Some topics are polished (committee-games, potential-to-sense). Others are assessed as intractable (pask-mesh-fitting). The June 2026 review will ask whether the diary-to-wild-to-formalization pipeline works; this assessment provides the content-side evidence.

**Directories to assess** (in addition to diary):
1. `blast-radius-problem/`
2. `committee-games/`
3. `cybernetics/`
4. `cyberneutics-director/`
5. `harness-engineering/`
6. `issues/`
7. `neo-cybernetics/`
8. `palgebra-graph-ui/`
9. `pask-mesh-fitting/`
10. `potential-to-sense/`
11. `residuality-theory/`
12. `software-factories/`
13. `subagent-personas-for-debate/`

**Output**: `agent/archive/wild-triage-2026-03.md` with per-directory assessment: status, graduation readiness (and to where: essays, artifacts, palgebra, applications, research-programs), blockers, recommended action.

**Parallelizable**: Can run concurrently with WS-4 if WS-4 doesn't touch wild content.

**Agent instructions**: For each directory, read its README (if present) and main document(s). Assess against these questions: (a) Is it active or dormant? (b) Is it polished enough to promote? If so, where? (c) What work would graduation require? (d) Should it be explicitly archived/shelved? (e) Does it connect to any current sprint findings (editorial review, research program triage)?

#### WS-6: Wild README and Cross-Reference Cleanup

**What**: Ensure every wild directory has an accurate README. Fix cross-references between wild content and core content. Update wild/README.md if triage changes any statuses.

**Inputs**: WS-5 triage results.

**Output**: Updated wild READMEs and cross-references.

**Parallelizable**: No — depends on WS-5.

---

### Cross-Cutting

#### WS-7: Rubric Extensions (Design Only)

**What**: Draft additional rubric dimensions that the existing rubrics don't cover. These are design documents, not implementations.

**Candidate dimensions**:
1. **Internal consistency**: Do cross-document claims agree? Do type names, terminology stacks, and definitions match across documents?
2. **Currency/staleness**: Is each document accurate as of today? When was it last verified?
3. **Pipeline velocity**: For wild content, what's the status (active/dormant/promoted/archived) and what would graduation require?
4. **Formal consistency**: For palgebra, do the four theory documents agree on notation, type names, composition laws?
5. **Practical validation**: How much of the methodology has been tested outside the repo itself?

**Output**: `agent/rubrics/repo-consistency.md` (draft, for review).

**Parallelizable**: Can run anytime. No dependencies.

**Agent instructions**: Model on `agent/rubrics/repo-audience-experience.md`. Same 0–3 scale. Each dimension gets: what it measures, scoring criteria with examples, evaluation questions. This is a design document — it will be reviewed before use.

## Dependency Graph

```
WS-1 (editorial review) ──┐
WS-2 (cross-ref audit)  ──┼── Pass 1 Gate (mg review) ── WS-4 (remediation)
WS-3 (research triage)  ──┘                                      │
                                                                  │
WS-7 (rubric extensions) ── independent, anytime                  │
                                                                  │
                              WS-5 (wild triage) ── WS-6 (wild cleanup)
                              (can overlap with WS-4 if non-conflicting)
```

## Subagent Strategy

WS-1, WS-2, and WS-3 are independent read-heavy audits with well-defined outputs. Each can be assigned to a separate subagent (or run in parallel worktrees if the tooling supports it). Key requirements:

- Each subagent must onboard via `agent/onboarding-core.md` before starting.
- Each subagent writes its output to `agent/archive/` with the naming convention `<topic>-2026-03.md`.
- No subagent modifies repo content — Pass 1 is audit-only. Content changes happen in WS-4 after mg reviews.
- WS-7 is also independent and can run as a subagent concurrently with anything.

For agents without native subagent support: run WS-1, WS-2, WS-3 sequentially in that order. The editorial review (WS-1) provides the most context for later work.

## Success Criteria

- `project-state.md` accurately reflects repo state after each workstream.
- All audit outputs exist in `agent/archive/` with clear findings.
- No dimension in the audience-experience rubric scores 0 after WS-4 remediation.
- Every wild directory has a README with status and cross-references.
- Research programs have explicit status (run/update/archive/merge).
- Handoff document exists recording what was done and what remains.

## How to Start

1. Read `agent/onboarding-core.md`.
2. Read `meta/project-state.md` (which points here).
3. Read the latest `agent/handoff-*.md`.
4. Pick a workstream from Pass 1 (WS-1, WS-2, WS-3, or WS-7) and execute it.
5. Write output to `agent/archive/`. Update `project-state.md`.
6. Write a handoff if the session ends before the sprint completes.
