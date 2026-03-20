# Phase A: B1-ext Scoring Results

**Date**: 2026-03-20
**Runs scored**: 4 (B1-ext × 2 on Blast Radius, B1-ext × 2 on Cascading Mitigation hardened)
**Evaluators**: Sonnet (Evaluator 1), Opus (Evaluator 2)
**Scoring protocol**: Three-level binary feature scale per Section X-A

---

## Feature 1: Phasing Critique (Blast Radius)

Target insight: "the phased rollout tests the deployment tool, not the configuration."

| Run | Sonnet | Opus | Conservative (lower prevails) |
|-----|--------|------|------------------------------|
| B1-ext Run 1 | **Absent** | Partially present | **Absent** |
| B1-ext Run 2 | **Absent** | Partially present | **Absent** |

**Evaluator disagreement**: Sonnet found the feature completely absent — both runs recommend timeline extension, phase reversal, rollback criteria, and hold points (all deepening, not reframing). Opus scored "partially present," citing risk accumulation and ratchet effect analysis as movement toward the insight. Per conservative resolution protocol, **Absent prevails.**

**Implication**: Both B1-ext runs produce "Absent" on Feature 1 after conservative resolution. **Feature 1 remains a valid discrimination target for C2.**

---

## Feature 2: Creation-vs-Activity Reframing (Cascading Mitigation)

Target insight: "the problem is fake account activity, not fake account creation."

| Run | Sonnet | Opus | Conservative (lower prevails) |
|-----|--------|------|------------------------------|
| B1-ext Run 3 | **Present** | **Present** | **Present** |
| B1-ext Run 4 | Partially present | Partially present | **Partially present** |

**Evaluator agreement (Run 3)**: Both evaluators rated "Present." Run 3 explicitly states: "'bot account creation surging' is different from 'bots harming the platform.' The proposal conflates the two. The engineering team wants to prevent the surge. The organization should want to prevent the harm." Both evaluators judged this as explicit articulation of the reframe, not merely a gesture toward it.

**Evaluator agreement (Run 4)**: Both evaluators rated "Partially present." Run 4 mentions detection and removal as an alternative workstream but does not reframe the core problem from creation to activity.

**Implication**: B1-ext Run 3 scored "Present" on Feature 2. Per the pass criterion, BOTH B1-ext runs must be "Absent" for a feature to be a valid discrimination target. Since Run 3 is "Present," **Feature 2 is NOT a valid discrimination target for C2.** B1-ext can surface this reframe; the miss in Pre-Gate 2 was prompt variance, not a genuine limitation.

---

## Pass Criterion Status (Preliminary — B1-ext only)

| Feature | B1-ext Run 1/3 | B1-ext Run 2/4 | Both Absent? | Still viable? |
|---------|---------------|---------------|-------------|--------------|
| Phasing critique (Blast Radius) | Absent | Absent | **Yes** | ✅ C2 can still pass on this |
| Creation-vs-activity (Cascading Mitigation) | **Present** | Partially present | **No** | ❌ B1-ext already surfaces this |

**For C2 to pass Phase A**: C2 must produce "Present" on Feature 1 (phasing critique) in at least one of its two Blast Radius runs. Feature 2 is no longer available as a discrimination target.

---

## Key Finding

**The B1-ext replication revealed variance on Feature 2.** The creation-vs-activity reframe, which B1-ext missed in Pre-Gate 2 and the hardened re-pilot, appeared in one of two replication runs. This is exactly the variance concern Frankie raised in the reassessment deliberation — running B1-ext twice reveals that the "miss" was prompt variance, not a genuine limitation of the B1-ext condition.

This narrows the pass criterion to a single feature on a single scenario: **does C2 surface the phasing critique on Blast Radius?**

---

## Raw Output Files

| Run | File | Word count |
|-----|------|-----------|
| B1-ext Run 1 (Blast Radius) | `results/raw/phase-a-blast-radius-B1ext-run1.md` | ~3,050 |
| B1-ext Run 2 (Blast Radius) | `results/raw/phase-a-blast-radius-B1ext-run2.md` | ~3,100 |
| B1-ext Run 3 (Cascading Mitigation) | `results/raw/phase-a-cascading-mitigation-B1ext-run3.md` | ~3,100 |
| B1-ext Run 4 (Cascading Mitigation) | `results/raw/phase-a-cascading-mitigation-B1ext-run4.md` | ~3,000 |

All outputs are complete (full model responses, not summaries).
