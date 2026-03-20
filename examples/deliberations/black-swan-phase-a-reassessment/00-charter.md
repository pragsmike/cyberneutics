---
charter:
  goal: "Decide how to proceed after the targeted revision failed to produce scenarios that meet the B1-ext ≤ 1 difficulty criterion. The reassessment trigger from the 2026-03-16 resolution has been activated."
  context: >
    The committee's 2026-03-16 resolution specified a targeted revision with reassessment
    trigger: replace the contaminated externally-sourced scenario, harden Glenda/Crock and
    Cascading Mitigation, re-pilot with B1 and B1-ext, and assess against the B1-ext ≤ 1
    criterion. The revision was executed on 2026-03-20. Results: hardening effectively
    reduced B1 scores (Glenda/Crock: 2→1, Cascading Mitigation: 2→1.5) but did NOT
    reduce B1-ext scores (Glenda/Crock: 3→3, Cascading Mitigation: 2→2.5). Zero scenarios
    meet B1-ext ≤ 1.

    The re-pilot identified a structural explanation: the B1-ext multi-angle prompt
    instructs the model to analyze from multiple angles (political dynamics, systemic
    effects, historical precedents, values), which is effectively a meta-instruction to
    perform structural analysis — exactly what the scoring system measures. No amount of
    surface hardening can counteract an explicit analytical instruction.

    The resolution specified three options if zero scenarios pass:
    (A) Fundamental redesign of Phase A
    (B) Accept ceiling with caveats — proceed knowing B1-ext is strong
    (C) Pivot to binary-feature-only analysis targeting specific insights B1-ext misses

    Additional data: Two specific structural features have been consistently missed by
    both B1 and B1-ext across the original pilot AND the re-pilot — the phasing critique
    for Blast Radius ("tests the tool not the config") and the creation-vs-activity
    reframing for Cascading Mitigation. These binary features survived hardening.
  success_criteria:
    - "Clear decision among the three options with explicit reasoning"
    - "Assessment of whether the B1-ext prompt problem invalidates the experimental design or just narrows the measurable effect"
    - "Concrete specification of what 'proceed' means operationally under the chosen option"
    - "Honest assessment of what evidence Phase A can and cannot produce"
  exit_conditions:
    - "Committee has chosen an option"
    - "The scope of what Phase A will measure has been explicitly narrowed or maintained"
    - "Next concrete action is specified"
  deliverable_format: "Resolution Artifact"
---

# Charter: Black Swan Phase A — Reassessment After Revision Failure

The committee is reconvened per the reassessment trigger in the 2026-03-16 resolution. The targeted revision has been executed and the results are in. Zero revised scenarios meet the B1-ext ≤ 1 difficulty criterion.

## Data Package

- Re-pilot results: `research-programs/evaluating-deliberative-architectures/results/re-pilot-revised-scenarios.md`
- Replacement scenario construction: `results/replacement-scenario-construction.md`
- Hardened scenarios: `results/glenda-crock-hardened.md`, `results/cascading-mitigation-hardened.md`
- Original Pre-Gate 2: `results/pre-gate-2-scenario-difficulty-pilot.md`
- Original resolution: `examples/deliberations/black-swan-phase-a/03-resolution.md`
