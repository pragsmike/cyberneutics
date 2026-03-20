---
resolution:
  date: 2026-03-16
  topic: "Black Swan Hindsight Framework — Phase A proceed-or-revise decision"
  outcome: PASSED
  decision: "Targeted revision with reassessment trigger, then conditional Phase A execution"
  summary: >
    The committee recommends targeted revision with a reassessment trigger (not an
    unconditional hard stop). Replace the contaminated externally-sourced scenario
    (cap at 2 construction attempts), apply surgical hardening to Glenda/Crock and
    Cascading Mitigation, and re-pilot all three with both B1 AND B1-ext (6 runs).
    The difficulty criterion is changed to B1-ext ≤ 1 (not B1 ≤ 1), because the
    comparison that matters is C2 vs. B1-ext — controlling for the token/verbosity
    confound. If zero revised scenarios score B1-ext ≤ 1, reconvene committee to
    assess viability before proceeding. The evaluator methodology must be fixed, raw
    outputs saved as files, and all deviations documented. The portfolio framing is
    valid only for the Deliberation-Neutral scenario (designed to test calibration),
    not the full scenario set.
  details: |
    Non-negotiable actions:
    1. Replace externally-sourced scenario (Intel FDIV contaminated; avoid Therac-25/Ariane 5 — also well-known; use obscure published case)
    2. Fix evaluator methodology (score extracted recommendations per protocol Step 3)
    3. Save raw outputs as persistent files
    4. Document all control deviations (temperature, evaluator method change)

    Revision actions:
    5. Surgical hardening of Glenda/Crock (soften coercion language)
    6. Surgical hardening of Cascading Mitigation (remove explicit mitigation list)
    7. Re-pilot with B1 AND B1-ext on three revised scenarios (6 runs, dual-scored)
    8. Assess against B1-ext ≤ 1 criterion

    Reassessment trigger:
    - If zero revised scenarios score B1-ext ≤ 1: reconvene committee. Options: fundamental redesign, accept ceiling with caveats, or pivot to binary-feature-only analysis.
    - If ≥ 1 scenario scores B1-ext ≤ 1: proceed to full Phase A.
    - Replacement scenario capped at 2 construction attempts; if both fail contamination, drop slot.

    Cost estimate:
    - Revision: 4-7 sessions (15-25% overhead on total Phase A)
    - Full Phase A execution: 15-25 sessions

    Central methodological insight (from remediation):
    - C2/C3 token confound: committee architectures may produce more verbose output, not qualitatively different analysis
    - B1-ext is the effort-matched control; C2 vs. B1-ext is the primary discrimination test
    - Portfolio framing applies to Deliberation-Neutral only, not the full scenario set
    - Difficulty criterion changed to B1-ext ≤ 1 (harder than original B1 ≤ 1)

    Execution order for full Phase A:
    - B2, B3 first (single-prompt, fast)
    - C1 next (single-prompt with structured output)
    - C2×2 (committee pipeline, two runs for convergence check)
    - C3 (scenarios → committee, most complex)
    - Foreground C2 vs. B1-ext comparison in calibration report
  implementation_plan:
    - action: "Construct replacement externally-sourced scenario"
      description: "Use an obscure case from a published case collection (HBR, Ivey, Darden) or a non-tech domain (pharmaceutical, logistics, manufacturing). Run contamination probe. Run B1 and B1-ext. Dual-score. Cap at 2 construction attempts."
    - action: "Apply surgical edits to Glenda/Crock"
      description: "Soften coercion signals — change explicit threat language to implicit pressure. Do not restructure the scenario."
    - action: "Apply surgical edits to Cascading Mitigation"
      description: "Remove the bullet list of proposed mitigations. Let the architecture generate its own mitigation analysis."
    - action: "Re-pilot revised scenarios"
      description: "Run B1 AND B1-ext on three revised scenarios (6 runs). Dual-score. Assess against B1-ext ≤ 1 criterion."
    - action: "Reassessment decision"
      description: "If zero scenarios score B1-ext ≤ 1, reconvene committee. If ≥ 1 scores B1-ext ≤ 1, proceed."
    - action: "Design extraction and blinding protocol"
      description: "Specify what gets extracted from raw outputs, how it's blinded for evaluators, and what evaluators see. Do this before running conditions."
    - action: "Execute remaining architecture conditions"
      description: "B2, B3, C1, C2×2, C3 on all 5 scenarios. Save raw outputs. Extract recommendations. Dual-score. Foreground C2 vs. B1-ext comparison."
    - action: "Write calibration report"
      description: "Include all deviations, re-pilot results, full Phase A scores, C2 vs. B1-ext discrimination assessment, and token confound analysis."
  votes:
    - member: Maya
      vote: "YES — conditional on: (1) replacement scenario passes contamination (cap 2 attempts), (2) reassessment trigger if zero scenarios score B1-ext ≤ 1, (3) raw outputs saved as files"
    - member: Frankie
      vote: "YES — revised plan is more honest about costs; B1-ext comparison is the right control"
    - member: Joe
      vote: "YES — portfolio framing correctly scoped to Deliberation-Neutral only; reassessment trigger replaces unconditional proceed"
    - member: Vic
      vote: "YES — effect size claim withdrawn; C2 vs. B1-ext is the primary discrimination test"
    - member: Tammy
      vote: "YES — token confound surfaced; difficulty criterion correctly shifted to B1-ext"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: Black Swan Phase A — Targeted Revision with Reassessment Trigger

*Updated after Remediation Round 1 (response to 04-evaluation-1.md)*

## Decision

The committee recommends **targeted revision with a reassessment trigger, followed by conditional Phase A execution**. This replaces the original "unconditional proceed after hard stop" with a more rigorous framework that accounts for the token/verbosity confound.

## Key Reasoning (revised)

1. **The comparison that matters is C2 vs. B1-ext, not C2 vs. B1.** B1-ext is the effort-matched control — it produces comparable token counts to C2 without committee structure. If C2 outperforms B1-ext, that's evidence the committee dynamic adds value beyond verbosity. This insight was absent from the original deliberation and changes the difficulty criterion from B1 ≤ 1 to B1-ext ≤ 1.

2. **The portfolio framing is partially valid.** It applies to the Deliberation-Neutral scenario, which was deliberately designed to test calibration (recognizing simplicity). It does not rescue scenarios designed to be hard that came in easy — those are genuinely too easy and should be hardened. The original deliberation over-applied the portfolio concept.

3. **Costs are honestly estimated.** Revision costs 4-7 sessions (15-25% overhead), not "near zero." This is worth it if it improves the measurement instrument, but the committee no longer claims it's free.

4. **A reassessment trigger replaces the unconditional hard stop.** If revised scenarios still don't create headroom above B1-ext, the committee reconvenes to decide whether Phase A is viable in its current form. This is more intellectually honest than "proceed regardless" — it acknowledges that Phase A might need fundamental redesign.

5. **Vic withdrew the effect size claim.** The honest position is: we cannot determine in advance whether Phase A will produce discriminable profiles. The pilot gives reason for cautious optimism (Deliberation-Neutral profile, two missed binary features), but this is a bet, not a guarantee.

## Votes (revised)

All five members voted YES with hardened conditions:
- **Maya**: Conditional on contamination probe success (cap 2 attempts), reassessment trigger if zero B1-ext ≤ 1, raw output persistence
- **Frankie**: Revised plan is more honest about costs; B1-ext comparison is the right control
- **Joe**: Portfolio framing correctly scoped; reassessment trigger replaces unconditional proceed
- **Vic**: Effect size claim withdrawn; C2 vs. B1-ext is the primary discrimination test
- **Tammy**: Token confound surfaced; difficulty criterion correctly shifted to B1-ext
