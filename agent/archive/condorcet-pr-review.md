# PR Review: Condorcet Experiment (PR #3)

**Date**: 2026-02-22
**Reviewer**: mg (maintainer), assisted by Claude
**PR**: condorcet-constraints branch, merged

**Note (2026-02-24):** The comparison and deliberation records referenced below were moved from `agent/comparisons/` and `agent/deliberations/` to `meta/research-programs/condorcet-comparison/results/`. See [meta/research-programs/condorcet-comparison.md](../../meta/research-programs/condorcet-comparison.md).
**Scope**: 45 files changed, +1713 / -119

---

## Summary

The PR investigates Condorcet's jury theorem as a formal foundation for the adversarial committee process. Its central finding is that the committee deliberately violates CJT's conditions (independence, binary outcome, literal competence probability) and that this is correct by design. The PR documents this relationship, builds a comparison protocol for testing deliberation against independent aggregation, and runs two comparison experiments that produce the methodology's first empirical evidence for the value of structured deliberation.

---

## What the PR contains

### Core conceptual work

1. **Condorcet artifact** (`artifacts/condorcet-jury-theorem-and-committee.md`): Design goals first, CJT as motivating analogy, three explicit deviations (no independence, no binary outcome, no literal *p*), and the fork — a CJT-compliant variant would be a different pipeline, not a correction. Well-structured, intellectually honest, appropriately scoped. Cross-linked from `artifacts/adversarial-committees.md`.

2. **Condorcet deliberation** (`agent/deliberations/condorcet-jury-theorem-process/`): Committee asked "should we correct for CJT?" Unanimous recommendation: document, don't change process. Review scored 13/15 (High). The deliberation itself is a good example of the methodology working — Maya's "who benefits" challenge was engaged, her condition (lead with design, not theorem) was adopted, and the resolution language was explicitly corrected away from "correct for."

### Comparison infrastructure

3. **Comparison protocol** (`artifacts/comparison-protocol-deliberative-vs-cjt.md`): Reusable protocol for running deliberative vs. CJT-style (independent vote then aggregate) on the same question. Clean structure: same question, same roster, same charter context; record each pipeline's output; compare. Limitations honestly flagged (independence hard to guarantee in a single model session, binary vs. rich output not apples-to-apples, single runs are datapoints).

4. **Two comparison runs** (`agent/comparisons/`):
   - *second-ci-job*: Both pipelines said Nay. CJT 4-1, Deliberative 5-0. Same verdict; deliberation changed one vote (Frankie) and added a revisit condition. Demonstrates that on straightforward questions, the pipelines agree but deliberation adds nuance.
   - *code-of-conduct*: **Opposite verdicts.** CJT Aye 3-2, Deliberative Nay 5-0. Three characters (Frankie, Vic, Tammy) voted Aye in isolation but flipped to Nay after debate. The enforcement/weaponization objection — present in independent rationales from Maya and Joe — was never answered by Aye voters in the CJT run. In deliberation, the Chair forced engagement, and three votes changed. This is the headline finding.

### Operational additions

5. **Smoke test** (`scripts/test_string_diagram.py`): Runs the equation-to-Mermaid converter on all three equation files, checks exit code 0, non-empty output, and "flowchart" in output. Clean, no dependencies, correct.

6. **Run guide** (`meta/repository-review-and-run-guide.md`): Comprehensive guide covering what the repo is, how to run skills, how to run the script, how to test (automated and manual), and a runbook. `meta/README.md` updated with link.

7. **CI deliberation** (`agent/deliberations/ci-string-diagram-test/`): Committee recommended adding a CI job for the smoke test. Review scored 9/15; remediation added Round 2. Resolution: add CI with documented scope. **Not implemented** — left for maintainer decision.

### Housekeeping

8. Handoff rotation (`agent/archive/handoff-2026-02-21.md`, `agent/handoff-2026-02-22.md`)
9. `artifacts/adversarial-committees.md`: one-line cross-reference to Condorcet doc added
10. `agent/ready-for-maintainer-review.md`: checklist for maintainer pickup

---

## Which phase of the committee process does it affect?

**None.** The PR does not change any phase of the committee pipeline. The Condorcet deliberation explicitly asked this question and answered: document the relationship, don't change the process. The comparison protocol creates a *separate* pipeline (CJT-style independent vote) for experimental comparison purposes — it does not modify or replace the existing committee.

This is the right call. The committee's value comes from Phases 2-3 (Deliberation and Resolution), where characters read and respond to each other. CJT requires independence, which would destroy the adversarial back-and-forth. The comparison runs empirically confirm this: the deliberative pipeline's strength is precisely in the cross-examination that CJT's independence condition prohibits.

---

## Fit with documented assumptions

**Strong fit across all five core ideas:**

1. **LLMs are narrative engines / repetition produces difference**: The comparison protocol operationalizes "repetition produces difference" by running the same question through two different pipelines and comparing. The CoC comparison is a demonstration: same inputs, different process, different narrative output.

2. **Narrative engineering composes unreliable primitives into reliable systems**: The CJT-style pipeline is a single-shot primitive per character — no composition, no feedback, no adversarial pressure. The deliberative pipeline composes those primitives through Robert's Rules, cross-examination, and structured debate. The comparison shows the composition matters.

3. **Observation changes state**: In the CJT run, Vic and Tammy never observed Maya and Joe's enforcement objection directed at them. In deliberation, that observation changed their state (their votes). The cybernetic loop was present in deliberation and absent in aggregation.

4. **The user is an editor**: The Condorcet artifact respects this — "The user is the editor; the committee informs, it does not decide." CJT is about getting the correct binary answer via majority vote. The methodology is about producing a map the editor can use.

5. **Adversarial committees artifact**: The core claim — "We are not aggregating independent judgments; we are generating a map through structured conflict" — is directly supported by the comparison evidence. The CJT-style pipeline aggregates independent judgments. The deliberative pipeline generates structured conflict. Same question, different output.

---

## Fit with Roberts Rules as forcing function

**The comparison runs provide the strongest evidence yet for why Roberts Rules matters.** The Roberts Rules artifact identifies four statistical shortcuts it prevents. The CoC comparison empirically confirms Shortcut #1 (premature consensus):

- Without Roberts Rules (CJT-style): Vic and Tammy gave surface-level Aye rationales ("low cost," "sets expectations") that never confronted the enforcement problem. Premature consensus with the Aye majority.
- With Roberts Rules (deliberative): The Chair directed Vic and Tammy to respond to Maya and Joe's enforcement challenge. Both changed their votes after engaging the objection.

The second-CI-job comparison confirms Shortcut #2 (vague synthesis) prevention: Frankie's Aye became a conditional Nay with a specific revisit clause — an amendment-like formulation forced by the structured debate.

---

## Concerns

1. **The handoff was a merge artifact.** Two sessions' content was concatenated into one file. This has been resolved — the condorcet content was split to `agent/archive/handoff-2026-02-22-condorcet.md` and the remaining handoff cleaned up.

2. **Independence caveat.** The comparison protocol honestly flags that true independence is hard to guarantee in a single model session. The CJT-style results should be read as "best-effort independence," not as a rigorous implementation of Condorcet's conditions. This is acknowledged in the protocol and does not undermine the finding — the point is that even imperfect independence produced a different outcome than deliberation.

3. **Two datapoints, not a study.** The PR produced two comparison runs. One agreed (second-CI-job), one disagreed (CoC). This is initial evidence, not proof. The comparison protocol is reusable and more runs would strengthen or weaken the pattern. The question types that produce divergence appear to be value-laden ones with hidden enforcement or second-order concerns.

4. **No ground truth.** We cannot say the deliberative verdict on the CoC question was *better* — only that it was *different* and arrived at through a more rigorous process. Whether "Nay on CoC" is the right answer depends on values and context, not on which pipeline produced it.

---

## Checklist verification (from `agent/ready-for-maintainer-review.md`)

| Item | Status |
|------|--------|
| Read handoff | Done (handoff has been split and cleaned) |
| Run smoke test | Not runnable in this environment (Python not on PATH); script verified present and correct by inspection |
| Skim Condorcet artifact | Done — thorough review above |
| Skim CoC comparison summary | Done — thorough review above |
| Decide on CI workflow | **Outstanding** — committee recommended it; maintainer has not yet decided |
| Commit | PR already merged |

**Outstanding items from optional follow-ups:**
- Add `when-methodology-fails.md` to quick-start recommended reading (carried forward, low effort)
- Full comparative evaluation (one decision, three methods, same rubric) — partially addressed by two deliberative-vs-CJT comparisons but the three-method version remains undone
- CI workflow — committee recommended, not yet implemented

---

## Disposition

The PR fits cleanly with the methodology's documented assumptions, strengthens the case for Robert's Rules as a forcing function, and does not change any phase of the committee process. The Condorcet artifact is well-written and appropriately scoped. The comparison runs are the methodology's first empirical evidence and the comparison protocol is a reusable tool. The handoff merge artifact has been resolved. The `ready-for-maintainer-review.md` checklist has been addressed except for the CI workflow decision (which is a maintainer choice, not a blocker).

**Recommendation**: Archive `ready-for-maintainer-review.md` — its purpose is served.
