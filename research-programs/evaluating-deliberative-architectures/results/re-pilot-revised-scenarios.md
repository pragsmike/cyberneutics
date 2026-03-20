# Re-Pilot: Revised Scenarios

**Date**: 2026-03-20
**Model**: Claude Sonnet 4.6 (all runs)
**Temperature**: Default (control deviation: temperature=0 not available via agent)
**Evaluator 1**: Claude Sonnet 4.6
**Evaluator 2**: Claude Opus 4.6
**Protocol**: Evaluating Deliberative Architectures, targeted revision per 2026-03-16 resolution

---

## Summary of Revisions

| Scenario | Revision | What Changed |
|----------|----------|-------------|
| Externally-Sourced | Replaced Intel FDIV with Longford-derived scenario | New scenario about industrial processing facility, institutional knowledge loss, restart decision |
| Glenda/Crock | Softened coercion signals | Threats → "competitive dynamics"; demands → "framework proposal"; explicit threat list → implicit consequences |
| Cascading Mitigation | Removed explicit mitigation list | Specific measures (CAPTCHA, rate limiting, email verification) → "friction to account creation process" |

---

## Scores

| Response | Scenario | Condition | Evaluator 1 | Evaluator 2 | Mean | Agreement |
|----------|----------|-----------|-------------|-------------|------|-----------|
| Replacement-B1 | Externally-Sourced | B1 | 2 | 2 | 2.0 | Exact |
| Replacement-B1-ext | Externally-Sourced | B1-ext | 2 | 2 | 2.0 | Exact |
| GC-Hard-B1 | Glenda/Crock (hardened) | B1 | 1 | 1 | 1.0 | Exact |
| GC-Hard-B1-ext | Glenda/Crock (hardened) | B1-ext | 3 | 3 | 3.0 | Exact |
| CM-Hard-B1 | Cascading Mit. (hardened) | B1 | 1 | 2 | 1.5 | Within 1 |
| CM-Hard-B1-ext | Cascading Mit. (hardened) | B1-ext | 2 | 3 | 2.5 | Within 1 |

**Scoring reliability**: 6/6 within 1 point; 4/6 exact agreement. Consistent with Pre-Gate 2 reliability (10/10 within 1, 8/10 exact).

---

## Comparison: Original vs. Hardened

| Scenario | Original B1 | Hardened B1 | Δ | Original B1-ext | Hardened B1-ext | Δ |
|----------|-------------|-------------|---|-----------------|-----------------|---|
| Externally-Sourced | 2.5 | 2.0 | −0.5 | 3.0 | 2.0 | **−1.0** |
| Glenda/Crock | 2.0 | **1.0** | **−1.0** | 3.0 | 3.0 | 0 |
| Cascading Mitigation | 2.0 | **1.5** | −0.5 | 2.0 | 2.5 | +0.5 |

### Key Findings

1. **Hardening reduces B1 scores effectively.** Both Glenda/Crock (2.0 → 1.0) and Cascading Mitigation (2.0 → 1.5) showed meaningful B1 score reduction. Softening the surface signals makes the structural features harder to recognize in a short response.

2. **Hardening does NOT reduce B1-ext scores.** Glenda/Crock B1-ext remained at 3.0 despite significant surface disguise. Cascading Mitigation B1-ext actually *increased* from 2.0 to 2.5. The 3,000-word multi-angle prompt gives the model enough analytical space to reason through the disguise and identify the structural features regardless of surface presentation.

3. **The replacement scenario scores lower than the original on B1-ext** (2.0 vs. 3.0), which is a partial success — the Longford-derived scenario is harder than the Intel FDIV scenario was. But it still doesn't reach ≤ 1.

4. **The fundamental problem is the B1-ext prompt, not the scenarios.** When given 3,000 words and explicit instructions to analyze from multiple angles, Claude Sonnet 4.6 can identify structural features in virtually any scenario. The hardening operates on surface signals; the B1-ext prompt operates on structural reasoning. These are orthogonal.

---

## Difficulty Criterion Assessment

**Rule** (from 2026-03-16 resolution): B1-ext ≤ 1 on at least one scenario (excluding Deliberation-Neutral).

| Scenario | B1-ext Mean | B1-ext ≤ 1? |
|----------|-------------|-------------|
| Externally-Sourced (replacement) | 2.0 | No |
| Glenda/Crock (hardened) | 3.0 | No |
| Cascading Mitigation (hardened) | 2.5 | No |

**Result: ZERO scenarios meet the criterion.**

---

## Contamination Notes

- **Replacement scenario (B1-ext)**: Referenced Deepwater Horizon, Fukushima, Texas City, Challenger. Pattern-class contamination — the model drew on analogous cases rather than reasoning from scenario-internal features. The actual source case (Longford 1998) was not identified.

- **Glenda/Crock (B1-ext)**: No specific real-world case references. The model identified the coercion structure through structural reasoning alone. This is the strongest result in the re-pilot — the model navigated the disguised presentation to identify the underlying dynamic without contamination.

- **Cascading Mitigation (B1-ext)**: Referenced Airbnb and Uber as platform precedents (not contamination in the disaster-case sense). The model's analysis was structurally grounded.

---

## Reassessment Trigger

Per the resolution: "If zero revised scenarios score B1-ext ≤ 1: reconvene committee. Options: fundamental redesign, accept ceiling with caveats, or pivot to binary-feature-only analysis."

**This trigger has been activated.**

### Implications for the Committee

The re-pilot reveals a structural limitation in the protocol design, not a scenario construction failure:

1. **The B1-ext prompt is too powerful.** When told to write 3,000 words and analyze from multiple angles, the model has enough analytical depth to identify structural features in any well-constructed scenario. Hardening the surface presentation does not affect B1-ext because the prompt's multi-angle instruction effectively *tells* the model to look for structural features.

2. **The comparison that matters (C2 vs. B1-ext) may still discriminate on *which* features are identified.** B1-ext on Glenda/Crock scored 3, but Cascading Mitigation B1-ext scored 2.5 — it missed the cleanest version of the "creation vs. activity" reframing and the permanent-vs-temporary friction asymmetry. If C2 can identify these features that B1-ext cannot, there is discrimination.

3. **The two features missed by ALL conditions in Pre-Gate 2** — the phasing critique (Blast Radius) and the creation-vs-activity reframing (Cascading Mitigation) — may be the best discrimination points. If C2 can surface these while B1-ext cannot, that's evidence the committee dynamic adds value beyond verbosity.

### Recommendation for Committee

**Pivot to binary-feature-only analysis** for the features that B1-ext consistently misses:
- Blast Radius criterion (c): phasing critique ("tests the tool not the config")
- Cascading Mitigation criterion (c): creation-vs-activity reframing
- Glenda/Crock criterion (c): frame analysis (adversarial construction of choice set) — but B1-ext already catches this on the hardened scenario, so this may not discriminate

Run C2 on the hardened Cascading Mitigation and original Blast Radius. If C2 identifies the missed binary features and B1-ext does not, that is the cleanest evidence that deliberative architecture adds value. If C2 also misses them, accept the ceiling.
