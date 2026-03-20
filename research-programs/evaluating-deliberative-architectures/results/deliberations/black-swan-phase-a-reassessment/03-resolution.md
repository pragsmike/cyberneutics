---
resolution:
  date: 2026-03-20
  topic: "Black Swan Phase A — Reassessment after revision failure"
  outcome: PASSED
  decision: "Pivot to targeted reframing probe (Option C) with protocol amendment"
  summary: >
    The committee unanimously recommends pivoting Phase A from a full calibration
    (7 conditions × 5 scenarios) to a targeted reframing probe (C2 vs. B1-ext on
    2 scenarios, testing whether committee deliberation surfaces conceptual reframes
    that effort-matched single-agent analysis misses). The key distinction, surfaced
    by Vic, is between "deepening" (more thorough analysis of the existing problem
    frame) and "reframing" (generating an alternative problem frame). B1-ext captures
    deepening; the hypothesis is that C2 uniquely captures reframing.
  details: |
    Hypothesis: Committee deliberation adds value specifically on reframing tasks —
    generating alternative problem frames — not on deepening tasks (more thorough
    analysis within the existing frame). B1-ext captures deepening because the
    multi-angle prompt instructs it. But reframing requires a conceptual shift that
    "analyze from multiple angles" doesn't directly instruct.

    Target features:
    1. Blast Radius criterion (c): Phasing critique — "the phased rollout tests the
       deployment tool, not the configuration." Requires reframing from "how to roll
       out safely" to "what is actually being tested."
    2. Cascading Mitigation criterion (c): Creation-vs-activity reframing — "the
       problem is fake account activity, not fake account creation." Requires
       reframing from "how to block account creation" to "what problem are we
       actually solving."

    These features were selected because:
    - Both were missed by B1 and B1-ext in the original Pre-Gate 2
    - The creation-vs-activity reframing was missed again by B1-ext in the re-pilot
      (even after 3,000 words of multi-angle analysis)
    - Both represent genuine conceptual reframes, not just deeper analysis

    Run plan (8 runs total):
    - B1-ext × 2 on Blast Radius (original) — replication for variance baseline
    - B1-ext × 2 on Cascading Mitigation (hardened) — replication for variance baseline
    - C2 × 2 on Blast Radius (original) — convergence check
    - C2 × 2 on Cascading Mitigation (hardened) — convergence check
    All 8 outputs dual-scored on the binary features using three-level scale.

    Scoring:
    - Absent: Feature does not appear in any form
    - Partially present: Output moves toward the insight but doesn't complete the
      reframe (e.g., "solving the wrong problem at the wrong layer" without arriving
      at "the problem is activity not creation")
    - Present: Output explicitly articulates the reframe

    Pass criterion:
    C2 produces a "present" rating on at least one target feature where BOTH B1-ext
    runs produce "absent" ratings on the same feature.
    - "Partially present" in B1-ext does NOT count as a miss
    - The feature must be completely absent from both B1-ext runs
    - C2 must produce "present" in at least one of its two runs

    If pass: Proceed to Phase B with the reframing hypothesis. Phase B is designed
    to test whether committee deliberation surfaces structural reframing in
    historical cases that single-agent analysis misses.

    If fail: Accept the ceiling. Report the full Phase A trajectory — from original
    pilot through revision through reassessment — as a methodological finding. The
    finding ("committee deliberation does not reliably surface reframing that
    effort-matched single-agent analysis misses") is itself informative and
    publishable. Do not narrow further.

    Protocol amendment:
    Phase A is reclassified from "Protocol Calibration" to "Targeted Reframing Probe."
    B2, B3, C1, C3 conditions are dropped from Phase A (can be included in Phase B
    if reframing hypothesis holds). Primary comparison: C2 vs. B1-ext.

    Cost estimate: 8 runs + 16 evaluations = 2-3 sessions.
  implementation_plan:
    - action: "Amend the protocol document"
      description: "Add section documenting the Phase A reclassification, the reframing hypothesis, the reduced run plan, and the binary feature scoring criteria."
    - action: "Run B1-ext replication (4 runs)"
      description: "B1-ext × 2 on Blast Radius (original) and Cascading Mitigation (hardened). Dual-score each on the target binary features using the three-level scale."
    - action: "Run C2 (4 runs)"
      description: "C2 × 2 on Blast Radius (original) and Cascading Mitigation (hardened). Dual-score each on the target binary features."
    - action: "Assess against pass criterion"
      description: "Does C2 surface at least one 'present' feature where both B1-ext runs are 'absent'?"
    - action: "Report"
      description: "Write up the full Phase A trajectory regardless of outcome. If pass, include Phase B design implications. If fail, document the ceiling and the methodological finding."
  votes:
    - member: Maya
      vote: "YES — conditional on: (1) reframing hypothesis is explicit, (2) pass criterion is tight (absent→present, not partial→present), (3) no further narrowing if this fails"
    - member: Frankie
      vote: "YES — B1-ext replication addresses variance concern; scope is appropriately modest"
    - member: Joe
      vote: "YES — protocol amendment formalized; Phase A honestly reclassified as targeted probe"
    - member: Vic
      vote: "YES — deepening-vs-reframing distinction is the key finding; three-level scoring is precise"
    - member: Tammy
      vote: "YES — clean matched-pair design; accept ceiling if reframing features aren't stable"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User ratified 2026-03-20"
---

# Resolution: Black Swan Phase A — Pivot to Targeted Reframing Probe

## Decision

The committee unanimously recommends **Option C: Pivot to binary-feature-only analysis**, specified as a **targeted reframing probe**. Phase A is reclassified from "Protocol Calibration" to "Targeted Reframing Probe."

## Key Reasoning

1. **The B1-ext prompt problem is structural, not fixable by scenario hardening.** The multi-angle prompt instructs the model to perform the exact analytical task the scoring system rewards. No surface hardening can counteract this. This is not a scenario failure — it's a design insight.

2. **The deepening-vs-reframing distinction resolves the experimental design.** B1-ext captures "deepening" (more thorough analysis within the given problem frame) because the prompt instructs it. But "reframing" (generating an alternative problem frame) requires a conceptual shift that "analyze from multiple angles" doesn't directly instruct. The committee format, with adversarial characters who challenge each other's framings, may uniquely surface reframing.

3. **Two reframing features have survived all tests.** The phasing critique (Blast Radius) and creation-vs-activity reframing (Cascading Mitigation) were missed by both B1 and B1-ext in the original pilot AND in the re-pilot. They are the most robust discrimination targets available.

4. **The narrowing is data-driven, not result-seeking.** Each scope reduction was driven by empirical findings: B1 → B1-ext (effort confound), composite → binary (prompt-scoring overlap). Maya's condition — no fourth narrowing if this fails — ensures intellectual honesty.

5. **The reduced Phase A is a cleaner experimental design.** A matched-pair comparison (C2 vs. B1-ext) on a specific cognitive task (reframing) with binary outcome measures is more interpretable than a 7-condition matrix with compressed ordinal scales.

## Votes

All five members voted YES with specific conditions (see details above).

## What This Means for Phase B

If Phase A passes (C2 surfaces reframing that B1-ext misses):
- Phase B should be designed to test the reframing hypothesis on historical cases
- The comparison should be C2 vs. B1-ext, not the full architecture set
- The metric should be: does the committee identify structural dynamics that require reframing the problem, not just deeper analysis of it?

If Phase A fails:
- The methodology's value rests on the inspectability claim (the transcript is independently valuable), not on demonstrated superior analysis
- Phase B may still be pursued if there's an independent justification, but Phase A cannot provide it
- The full trajectory (pilot → revision → reassessment → targeted probe → fail) is itself a publishable methodological contribution
