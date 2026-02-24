# Condorcet Comparison: Deliberative Committee vs. CJT-Style Independent Vote

**Status**: Completed (initial two-run study)
**Runs**: 2 (2026-02-22)
**Results**: [condorcet-comparison/results/](condorcet-comparison/results/)

> **Contributing to this program**
> - **Skills needed**: Ability to run `/committee` deliberations and generate independent CJT-style votes per the [comparison protocol](../../artifacts/comparison-protocol-deliberative-vs-cjt.md). Analytical writing for comparison summaries.
> - **Estimated scope**: Afternoon per additional run (one question, both pipelines, comparison write-up).
> - **Contributor type**: Solo.
> - **Entry point**: Read the [comparison protocol](../../artifacts/comparison-protocol-deliberative-vs-cjt.md), then review one completed run (e.g., [code-of-conduct results](condorcet-comparison/results/code-of-conduct/)) as a template. Pick a new binary question and run both pipelines.

---

## Objective

Compare the deliberative committee pipeline (adversarial debate via `/committee`) against a CJT-style (Condorcet jury theorem) independent-vote-then-aggregate pipeline on the **same** questions, to test whether structured deliberation produces different — and better-mapped — outcomes than independent aggregation.

**Conceptual foundation**: [Condorcet's Jury Theorem and the Committee](../../artifacts/condorcet-jury-theorem-and-committee.md) — establishes that the committee deliberately violates CJT's conditions (independence, binary outcome, literal competence probability), and that a CJT-compliant variant would be a different pipeline.

**Reusable protocol**: [Comparison Protocol: Deliberative vs. CJT-Style](../../artifacts/comparison-protocol-deliberative-vs-cjt.md) — defines how to run both pipelines on the same question with the same roster and charter.

---

## Procedure

Per the [comparison protocol](../../artifacts/comparison-protocol-deliberative-vs-cjt.md):

1. **Choose a binary or categorical question** and write a shared charter (goal, context, success criteria).
2. **Pipeline A (Deliberative)**: Run `/committee [question]` with the standard roster. Characters see each other's arguments and debate. Record deliberation transcript and resolution with per-character votes.
3. **Pipeline B (CJT-style)**: For each roster member, generate exactly one independent response (vote + rationale) without access to the others' responses. Aggregate by majority.
4. **Compare**: Do the outcomes agree? How do rationales differ? What changed between isolation and debate?

**Same roster** (`agent/roster.md`) and **same charter context** for both pipelines on each question.

---

## Runs

### Conceptual deliberation (pre-experiment)

A committee deliberation asked: "Should we correct for Condorcet's jury theorem?" Unanimous recommendation: **document the relationship, don't change the process**. Review scored 13/15 (High). This deliberation informed the design of the comparison protocol and the Condorcet artifact.

- Records: [condorcet-comparison/results/condorcet-jury-theorem-process/](condorcet-comparison/results/condorcet-jury-theorem-process/)

### Run 1: second-ci-job (2026-02-22)

**Question**: Should we add a second CI job (e.g. link-check) in addition to the existing string-diagram test?

| Pipeline | Verdict | Votes (Aye–Nay–Abstain) |
|----------|---------|--------------------------|
| CJT-style | Nay (majority) | 1–4–0 (Frankie Aye) |
| Deliberative | Nay (unanimous) | 0–5–0 |

**Same verdict.** Deliberation changed one vote (Frankie Aye → Nay) and added a revisit condition. CJT-style produced five separate rationales with no refinement; deliberative produced a resolution with implementation steps.

- Comparison records: [condorcet-comparison/results/second-ci-job/](condorcet-comparison/results/second-ci-job/)
- Deliberation transcript: [condorcet-comparison/results/second-ci-job-deliberation/](condorcet-comparison/results/second-ci-job-deliberation/)

### Run 2: code-of-conduct (2026-02-22)

**Question**: Should we add a Code of Conduct (CoC) to the repository?

| Pipeline | Verdict | Votes (Aye–Nay–Abstain) |
|----------|---------|--------------------------|
| CJT-style | Aye (majority) | 3–2–0 (Frankie, Vic, Tammy Aye) |
| Deliberative | Nay (unanimous) | 0–5–0 |

**Opposite verdicts.** Three characters (Frankie, Vic, Tammy) voted Aye in isolation but flipped to Nay after debate. The enforcement/weaponization objection — present in Maya and Joe's CJT-style rationales — was never answered by Aye voters in the independent run. In deliberation, the Chair forced engagement with that objection, and three votes changed.

- Comparison records: [condorcet-comparison/results/code-of-conduct/](condorcet-comparison/results/code-of-conduct/)
- Deliberation transcript: [condorcet-comparison/results/code-of-conduct-deliberation/](condorcet-comparison/results/code-of-conduct-deliberation/)

---

## Key Findings

1. **Deliberation can change outcomes.** On the code-of-conduct question, CJT-style said Aye and deliberative said Nay — same question, same roster, different process, opposite verdict.

2. **The divergence mechanism is cross-examination.** In isolation, Vic and Tammy gave surface-level Aye rationales ("low cost," "sets expectations") that never confronted the enforcement problem. In debate, they had to face it and changed their views.

3. **Question type matters.** The straightforward question (second-ci-job) produced agreement between pipelines. The value-laden question with hidden second-order concerns (code-of-conduct) produced divergence. This suggests deliberation's value is greatest for questions where important objections exist but aren't obvious.

4. **Deliberation produces richer output.** Both runs produced more actionable deliberative output (decision-space maps, revisit conditions, implementation steps) compared to CJT-style output (a vote tally and five rationales).

5. **This is the methodology's first empirical evidence** for the value of structured deliberation over independent aggregation.

---

## Limitations

- **Two datapoints, not a study.** One run agreed, one disagreed. More runs needed to establish when and how often the pipelines diverge.
- **Independence caveat.** In a single model session, true independence of CJT-style votes is hard to guarantee. Results should be read as "best-effort independence."
- **No ground truth.** We cannot say the deliberative verdict was *better* — only that it was different and arrived at through a more rigorous process.
- **Binary comparison.** This compares two pipelines (deliberative vs. CJT-style). The full evaluation-schemes design ([evaluation-schemes.md](evaluation-schemes.md)) calls for comparison against additional baselines (single-prompt, chain-of-thought, multi-perspective).

---

## Connection to Other Programs

This study provides partial evidence toward the [evaluation-schemes](evaluation-schemes.md) "highest priority" question: does committee-based deliberation beat simpler approaches? The comparison protocol is a lightweight precursor to the full blind panel evaluation (Design A in evaluation-schemes). The ablation study ([ablation-study.md](ablation-study.md)) addresses a complementary question: which components of the deliberative pipeline contribute most?

---

## Origin

Produced in a single session on 2026-02-22. Session handoff: `agent/archive/handoff-2026-02-22-condorcet.md`. PR review: `agent/archive/condorcet-pr-review.md`. These records were originally stored in `agent/comparisons/` and `agent/deliberations/` and consolidated here on 2026-02-24.
