# Phase A Results: Targeted Reframing Probe

**Date**: 2026-03-20
**Result**: **DOES NOT PASS**
**Runs completed**: 8 (4 B1-ext, 4 C2)
**Scoring**: Dual-evaluator (Sonnet + Opus), conservative resolution

---

## Summary

Phase A tested whether C2 (adversarial committee deliberation) surfaces conceptual reframing that B1-ext (effort-matched single-agent analysis) misses. Two target reframing features were evaluated across two scenarios (Blast Radius and Cascading Mitigation hardened), with 2 runs per condition per scenario.

**Result**: C2 does not produce "Present" on any target feature where both B1-ext runs produce "Absent." Phase A does not pass.

---

## Combined Scoring Table

| Run | Condition | Scenario | Feature 1 (Phasing) | Feature 2 (Creation-vs-Activity) |
|-----|-----------|----------|---------------------|----------------------------------|
| 1 | B1-ext | Blast Radius | **Absent** | — |
| 2 | B1-ext | Blast Radius | **Absent** | — |
| 3 | B1-ext | Cascading Mitigation | — | **Present** |
| 4 | B1-ext | Cascading Mitigation | — | **Partially present** |
| 5 | C2 | Blast Radius | **Partially present** | — |
| 6 | C2 | Blast Radius | **Absent** | — |
| 7 | C2 | Cascading Mitigation | — | **Partially present** |
| 8 | C2 | Cascading Mitigation | — | **Present** |

All ratings are conservative (lower evaluator rating prevails on disagreement).

---

## Feature-Level Analysis

### Feature 1: Phasing Critique ("the phased rollout tests the tool, not the configuration")

| Condition | Run A | Run B | Best Score |
|-----------|-------|-------|------------|
| B1-ext | Absent | Absent | Absent |
| C2 | Partially present | Absent | Partially present |

**Finding**: Neither condition explicitly articulated the phasing critique. C2 moved closer (one "Partially present" vs. two "Absent" in B1-ext), but the insight remained incomplete. The committee's argumentative pressure — particularly Vic's demand to distinguish types of drift and Joe's institutional memory — produced directional movement but did not complete the reframe.

**Interpretation**: The phasing critique may represent a genuinely difficult conceptual move that resists both systematic analysis and argumentative pressure. The insight requires recognizing that the *purpose* of phasing is being tested on the wrong dimension — not just that phasing has risks or limitations, but that it validates mechanism rather than content. Both conditions produced extensive analysis of phasing risks without completing this specific reframe.

### Feature 2: Creation-vs-Activity Reframing ("the problem is activity, not creation")

| Condition | Run A | Run B | Best Score |
|-----------|-------|-------|------------|
| B1-ext | Present | Partially present | Present |
| C2 | Partially present | Present | Present |

**Finding**: Both conditions surfaced this reframe at "Present" level in at least one run. Feature 2 does not discriminate between conditions. The creation-vs-activity reframe appears to be accessible to both single-agent analysis and committee deliberation — it emerged from B1-ext's systematic "values and principles" angle and from C2's character-driven debate (Frankie's values challenge, Tammy's systems analysis).

**Interpretation**: This confirms Frankie's concern during the reassessment deliberation — the Pre-Gate 2 miss on this feature was prompt variance, not a genuine B1-ext limitation. Running 2 replications per condition caught this.

---

## Pass Criterion Assessment

**Criterion**: C2 produces "Present" on ≥1 target feature where BOTH B1-ext runs produce "Absent."

- Feature 1 (Phasing critique): Both B1-ext runs Absent ✓, but C2 best score is "Partially present" ✗
- Feature 2 (Creation-vs-activity): B1-ext Run 3 is "Present" → not eligible as discrimination target

**Result: DOES NOT PASS.**

---

## Trajectory Record

1. **Pre-Gate 1** (2026-03-16): B1 scored ≤1 on 1/5 scenarios (needed 3+). Committee recommended revision.
2. **Pre-Gate 2** (2026-03-16): B1-ext produced longer, deeper analyses but did not clearly separate from C2 on reframing. Preliminary signals mixed.
3. **Reassessment** (2026-03-20): Committee reclassified Phase A as Targeted Reframing Probe. Narrowed to 2 features × 2 scenarios.
4. **B1-ext Replication** (2026-03-20): Feature 2 eliminated as discrimination target (B1-ext Run 3 scored "Present"). Narrowed to Feature 1 only.
5. **C2 Runs** (2026-03-20): C2 scored "Partially present" (best) on Feature 1. Does not meet "Present" threshold.
6. **Final**: Phase A does not pass.

---

## Implications (per Protocol Section X-A)

**If-fail path**: "Phase A reports a null result on the targeted reframing probe. The committee deliberation architecture did not reliably surface reframing insights absent from the effort-matched baseline on the tested scenarios. The research program proceeds to Phase B (new scenarios with established discrimination) or documents the null and pauses."

### What this means

1. **C2 does not demonstrate reliable reframing advantage over B1-ext on these scenarios.** The committee format produced qualitatively different analysis (character-driven debate, productive tensions) but not reliably different insights at the reframing level.

2. **The null is informative, not trivial.** C2 moved *closer* to the phasing critique than B1-ext (Partially present vs. Absent). This suggests committee deliberation may produce partial reframing pressure without reliably completing the move. A larger sample might reveal a statistical difference, but the current probe does not support the discrimination claim.

3. **The reframing hypothesis is not refuted — it's untested at sufficient power.** Two runs per condition is the minimum for variance checking, not for statistical discrimination. The probe was designed to detect a strong effect; a subtler effect would require more runs or different scenarios.

4. **Scenario design matters.** The phasing critique proved elusive for *all* conditions. This may indicate the insight is unusually difficult to surface, or that the Blast Radius scenario doesn't provide sufficient cues to trigger it. Future work should consider whether different scenario designs better probe for reframing.

---

## Detailed Scoring Files

- B1-ext scoring: `results/phase-a-B1ext-scoring.md`
- C2 scoring: `results/phase-a-C2-scoring.md`
- Raw B1-ext outputs: `results/raw/phase-a-blast-radius-B1ext-run{1,2}.md`, `results/raw/phase-a-cascading-mitigation-B1ext-run{3,4}.md`
- Raw C2 outputs: `results/raw/phase-a-blast-radius-C2-run{5,6}.md`, `results/raw/phase-a-cascading-mitigation-C2-run{7,8}.md`
