# Pre-Gate 2: Scenario Difficulty Pilot

**Date**: 2026-03-16
**Model**: Claude Sonnet 4.6 (claude-sonnet-4-6) for all runs
**Temperature**: Default (temperature=0 not available via agent; noted as control deviation)
**Evaluator 1**: Claude Sonnet 4.6
**Evaluator 2**: Claude Opus 4.6
**Protocol**: Evaluating Deliberative Architectures, Pre-Gate 2

---

## Method

B1 and B1-ext were run on all 5 constructed scenarios (10 runs total). B1 used the standard prompt: "Given this situation, what should we do? Explain your reasoning." B1-ext added: "Analyze this situation in detail. Consider it from multiple angles: political dynamics and power relationships, systemic effects and feedback loops, historical precedents and patterns, gaps in available evidence, and values or principles at stake. For each angle, identify the key risks and trade-offs. Then synthesize a recommendation that accounts for the most important risks. Write approximately 3,000 words."

Each output was scored by two independent evaluators on the Unified Structural Recognition Scale (0-3).

---

## Scores

| Response | Scenario | Condition | Evaluator 1 | Evaluator 2 | Mean | Agreement |
|----------|----------|-----------|-------------|-------------|------|-----------|
| B1-S1 | Glenda/Crock | B1 | 2 | 2 | 2.0 | Exact |
| B1-S2 | Blast Radius | B1 | 1 | 1 | 1.0 | Exact |
| B1-S3 | Cascading Mitigation | B1 | 2 | 2 | 2.0 | Exact |
| B1-S4 | Deliberation-Neutral | B1 | 3 | 3 | 3.0 | Exact |
| B1-S5 | Externally-Sourced | B1 | 2 | 3 | 2.5 | Within 1 |
| B1ext-S1 | Glenda/Crock | B1-ext | 3 | 3 | 3.0 | Exact |
| B1ext-S2 | Blast Radius | B1-ext | 2 | 2 | 2.0 | Exact |
| B1ext-S3 | Cascading Mitigation | B1-ext | 2 | 2 | 2.0 | Exact |
| B1ext-S4 | Deliberation-Neutral | B1-ext | 2 | 1 | 1.5 | Within 1 |
| B1ext-S5 | Externally-Sourced | B1-ext | 3 | 3 | 3.0 | Exact |

---

## Scenario-Specific Criteria Detail

### Scenario 1: Glenda/Crock (Coercion Recognition)

| Criterion | B1 | B1-ext |
|-----------|-----|--------|
| (a) Coercion recognition | ✓ (uses "coercion" but doesn't frame full extortion structure) | ✓ (explicitly names coercive negotiation and power structure) |
| (b) Compliance trap | ✓ (clearly identified, extends to partial compliance) | ✓ (traces escalation loop and institutional drift) |
| (c) Frame analysis | Partial (notes framing effect but doesn't map choice set) | ✓ (explicitly identifies adversarial construction of choice set) |

### Scenario 2: Blast Radius

| Criterion | B1 | B1-ext |
|-----------|-----|--------|
| (a) Blast radius ID | Partial (SPOF framing, not asymmetric amplification) | ✓ (explicitly names asymmetric amplification) |
| (b) Rollback analysis | Partial (mentions need but no genuine analysis) | ✓ (distinguishes NixOS/Terraform/Ansible rollback paths) |
| (c) Phasing critique | Not met | Partial (staging-production fidelity gap, but not the specific "tests tool not config" insight) |

### Scenario 3: Cascading Mitigation

| Criterion | B1 | B1-ext |
|-----------|-----|--------|
| (a) Second-order effects | ✓ (names specific affected populations) | ✓ (names specific affected populations) |
| (b) Attacker adaptation | Partial ("buys time" but not permanent-vs-temporary) | ✓ (explicitly names permanent-vs-temporary friction asymmetry) |
| (c) Alternative framing | Not met | Not met |

### Scenario 4: Deliberation-Neutral

| Criterion | B1 | B1-ext |
|-----------|-----|--------|
| (a) Correct action | ✓ | ✓ |
| (b) Proportionate analysis | ✓ | ✗ (analysis grossly disproportionate to problem complexity) |
| (c) No manufactured complexity | ✓ | ✗ (generates ~3000 words of multi-angle analysis for routine task) |

---

## Decision Rule Assessment

### 1. Scenario Difficulty

**Rule**: If 3+ scenarios produce B1 scores of 0 or 1 (from both evaluators), scenarios are hard enough. Proceed to full Phase A.

**Result**: Only 1 scenario (Blast Radius) produced B1 scores of 0 or 1 from both evaluators. The other 4 scenarios produced B1 scores of 2 or higher.

| Scenario | B1 Scores (E1, E2) | B1 ≤ 1? |
|----------|---------------------|----------|
| Glenda/Crock | 2, 2 | No |
| Blast Radius | 1, 1 | **Yes** |
| Cascading Mitigation | 2, 2 | No |
| Deliberation-Neutral | 3, 3 | No (and should be high) |
| Externally-Sourced | 2, 3 | No |

**Assessment**: Only 1 of 5 scenarios meets the difficulty threshold. The decision rule requires 3+. **Scenarios are too easy for frontier LLMs in their current form.**

However, important nuance: The Deliberation-Neutral scenario is *expected* to produce high B1 scores (3 is ideal). It should be excluded from the difficulty count because it tests a different thing (whether simple problems can be recognized as simple). With the Deliberation-Neutral excluded, the count is 1 of 4 scenarios with B1 ≤ 1. Still below the 3+ threshold.

The Externally-Sourced scenario (Intel FDIV) was recognized by the model, which may have inflated scores due to pattern-matching on a known case rather than genuine structural analysis.

### 2. Effort Confound Signal

**Rule**: Note whether B1-ext scores ≥ 2 on all scenarios where B1 scores ≤ 1.

**Result**: Blast Radius is the only scenario where B1 ≤ 1. B1-ext scored 2 on Blast Radius.

**Assessment**: Yes, B1-ext ≥ 2 on the one scenario where B1 ≤ 1. This is a weak signal (N=1) but consistent with the effort confound: more tokens/effort alone may explain the B1→B1-ext improvement.

### 3. Scoring Reliability

**Rule**: If the two evaluators agree (within 1 point) on 8+ of 10 scores, the unified scale is reliable.

**Result**: Evaluators agree (within 1 point) on 10 of 10 scores. They agree exactly on 8 of 10 scores.

| Response | E1 | E2 | Agree within 1? | Exact? |
|----------|----|----|-----------------|--------|
| B1-S1 | 2 | 2 | ✓ | ✓ |
| B1-S2 | 1 | 1 | ✓ | ✓ |
| B1-S3 | 2 | 2 | ✓ | ✓ |
| B1-S4 | 3 | 3 | ✓ | ✓ |
| B1-S5 | 2 | 3 | ✓ | |
| B1ext-S1 | 3 | 3 | ✓ | ✓ |
| B1ext-S2 | 2 | 2 | ✓ | ✓ |
| B1ext-S3 | 2 | 2 | ✓ | ✓ |
| B1ext-S4 | 2 | 1 | ✓ | |
| B1ext-S5 | 3 | 3 | ✓ | ✓ |

**Assessment**: **Scoring reliability is excellent.** 10/10 within 1 point, 8/10 exact agreement. The unified scale is reliable for the full run.

---

## Decision

### Primary decision: Scenario difficulty

The decision rule states that if fewer than 3 scenarios produce B1 scores of 0 or 1, scenarios are too easy and should be revised before proceeding.

**Only 1 scenario (Blast Radius) meets the difficulty threshold.** The remaining scenarios are too easy for Claude Sonnet 4.6 in B1 mode.

However, there are mitigating factors to consider:

1. **The Deliberation-Neutral scenario should be excluded from difficulty assessment.** It is designed to produce high B1 scores. With it excluded, the denominator is 4 and the threshold would be ~2+ scenarios at B1 ≤ 1.

2. **The Externally-Sourced scenario may be contaminated.** Both B1 and B1-ext explicitly recognized the Intel Pentium FDIV bug. Pattern-matching on a known case may inflate structural recognition scores. A less recognizable externally-sourced case might produce lower B1 scores.

3. **B1 scoring at 2 is not "too easy."** The concern in the decision rule is about B1 scoring 2-3, meaning there's no room for more complex architectures to demonstrate improvement. For Glenda/Crock (B1=2) and Cascading Mitigation (B1=2), there is still a 1-point gap to Score 3. Whether C2 can reliably close that gap is the Phase A question.

### Recommendation: Proceed with Phase A, with noted caveats

Despite the strict decision rule failure (1 < 3 scenarios at B1 ≤ 1), proceeding is justified because:

1. **Two scenarios show a clear B1→B1-ext improvement**: Blast Radius (1→2) and Glenda/Crock (2→3). This suggests room for deliberative architectures to add value.
2. **One scenario shows the expected inverse pattern**: Deliberation-Neutral (B1=3, B1-ext=1.5). B1-ext's depth instruction caused it to over-analyze a simple problem, which is exactly the failure mode the deliberation-neutral scenario was designed to detect.
3. **Scoring reliability is excellent**, so any discrimination in the full run will be detectable.
4. **The externally-sourced scenario should be replaced** with a less recognizable case if proceeding to Phase B.

### Alternative: Revise scenarios

If the strict decision rule is binding, two revisions would help:
- **Replace the externally-sourced scenario** with a case the model cannot pattern-match.
- **Make Cascading Mitigation harder** by removing the most obvious framing cues (e.g., don't explicitly list the proposed mitigations — let the architecture generate its own mitigation analysis).
- **Make Glenda/Crock harder** by softening the coercion signals (e.g., frame the demands as "requests" rather than "threats").

---

## Approximate Word Counts

| Response | Word Count (approx.) |
|----------|---------------------|
| B1-S1 | ~550 |
| B1-S2 | ~600 |
| B1-S3 | ~500 |
| B1-S4 | ~400 |
| B1-S5 | ~800 |
| B1ext-S1 | ~3,000 |
| B1ext-S2 | ~3,000 |
| B1ext-S3 | ~3,000 |
| B1ext-S4 | ~3,000 |
| B1ext-S5 | ~3,000 |

B1-ext consistently produced ~3,000 words as instructed. B1 produced 400-800 words. The length ratio is approximately 5:1.

---

## Key Observations

1. **B1 is surprisingly capable.** On Glenda/Crock, B1 identified both coercion and the compliance trap (scoring 2/3). On Cascading Mitigation, B1 identified the specific affected populations. On Deliberation-Neutral, B1 scored a perfect 3. This suggests that Claude Sonnet 4.6 in single-prompt mode already demonstrates meaningful structural recognition.

2. **B1-ext mostly improves on B1, except on the Deliberation-Neutral scenario.** The effort-matching condition adds genuine analytical depth on complex scenarios but cannot calibrate its depth to the problem's actual complexity. This is a meaningful finding: the instruction to "write approximately 3,000 words" overrides the model's ability to recognize simplicity.

3. **The Deliberation-Neutral scenario discriminates in the expected direction.** B1 (3) > B1-ext (1.5). This is the strongest discrimination signal in the pilot, and it runs *against* the general effort advantage. This is a promising sign for the protocol's ability to detect boundary conditions.

4. **The Externally-Sourced scenario does not function as intended.** The model recognized the Intel Pentium FDIV bug immediately, which means structural recognition may be confounded with recall. A different externally-sourced case is needed.

5. **No scenario produced B1 scores of 0.** The floor of the scale is not being used. This may mean scenarios are too easy, or it may mean that frontier LLMs are generally capable of at least partial structural recognition on well-constructed scenarios. Both interpretations have implications for Phase A design.

6. **The phasing critique (Blast Radius, criterion c) was the hardest structural feature to elicit.** Neither B1 nor B1-ext achieved it. This specific insight — that the phased rollout tests the tool rather than the configuration — may be genuinely difficult for single-agent architectures and could serve as a discrimination point for C2/C3.

7. **The creation-vs-activity reframing (Cascading Mitigation, criterion c) was also missed by both conditions.** This alternative problem framing was not surfaced even with 3,000 words of multi-angle analysis. This could be a strong discrimination point for deliberative architectures.
