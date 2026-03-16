# Protocol Re-Evaluation: Black Swan Hindsight Framework (Post-Remediation)

**Date**: 2026-03-16
**Evaluated document**: `research-programs/evaluating-deliberative-architectures.md` (post-remediation version)
**Rubric**: `protocol-evaluation-rubric.md`
**Previous evaluation**: `protocol-evaluation-2026-03-16.md` (score: 10/24)

---

## Scores Summary

| Dimension | Before | After | Change | Justification |
|-----------|--------|-------|--------|---------------|
| 1. Construct Validity | 1 | 2 | +1 | Phase A/B distinction explicitly separates "structural recognition calibration" from "anticipatory validity." Constructed scenarios no longer claim to test anticipation. Circularity warning on Glenda/Crock. Residual: scenarios still designed within the methodology's ecosystem. |
| 2. Confound Control | 1 | 2 | +1 | B1-ext controls token/effort confound. Operational blinding protocol extracts recommendations only. Strengthened B3 eliminates weak-prompt confound. C1 coordinator prompt specified. Residual: scenario provenance bias (all scenarios from methodology ecosystem); recommendation length may still correlate with architecture. |
| 3. Discriminant Power | 1 | 2 | +1 | Deliberation-neutral scenario adds expected-to-discriminate-differently case. Unified 0-3 scale provides gradient. Phase A decision gate requires demonstrated discrimination before Phase B investment. Residual: scenario difficulty for current LLMs is untested (needs pilot); N=5 is still small. |
| 4. Internal Consistency | 2 | 3 | +1 | Unified scoring scale (VII-A) aligns constructed and historical case scoring. Phase A/B framing resolves the tension between "anticipation" claims and checklist criteria. Results tables match what evaluation protocol produces. Calibration expectations replace predictions. |
| 5. Executability | 2 | 2 | 0 | Improved: C1 coordinator prompt specified, B3 prompt fully specified, operational blinding protocol defined. Remaining gap: B1-ext token target depends on first-run C2 output length (minor bootstrapping issue; estimate ~3,000 words). |
| 6. Statistical Adequacy | 0 | 2 | +2 | Phase A uses raw scores and descriptive comparisons (appropriate for N=5). Phase B uses means with ranges (acknowledged as directional). Effect sizes reserved for combined program with explicit caveats. No more meaningless CI/Cohen's d at N=4. |
| 7. Falsifiability | 1 | 2 | +1 | Deliberation-neutral scenario explicitly tests where B1 should beat C2. Calibration expectations frame both confirmation and disconfirmation as informative. Circularity warning on Glenda/Crock. Phase A decision gate allows protocol failure. Residual: no externally-sourced scenario yet (nice-to-have 8 in remediation plan). |
| 8. Honest Framing | 2 | 3 | +1 | Introduction now explicitly distinguishes Phase A (calibration) from Phase B (evidence). Constructed scenarios framed as machinery testing, not methodology validation. Circularity warning on Glenda/Crock. Strengths section updated to reflect actual design features. |
| 9. Adaptive Design and Responsible Use | — | 3 | new | Phase A/B decision gates with specified responses to each outcome pattern. Three explicit outcome paths (discriminates → Phase B; doesn't discriminate → diagnose; B1-ext matches C2 → report). Pre-gates test feasibility assumptions before full investment. Circularity warnings bound what can be claimed. Framing explicitly names Phase A as calibration, not evidence. |

**Aggregate**: 21/27 (up from 18/24 on original 8 dimensions; now scored on 9 dimensions per updated rubric). No dimensions at 0 or 1. The protocol is a solid preliminary design with pre-gate structure that prevents wasted investment.

> **Note (2026-03-16)**: The rubric was expanded from 8 to 9 dimensions per committee recommendation ([deliberations/protocol-eval/03-resolution.md](../../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)). The new Dimension 9 (Adaptive Design and Responsible Use) evaluates decision gates, revision triggers, and overinterpretation protections. The protocol scores well on this dimension because it already had Phase A/B gates, outcome-dependent next steps, and explicit framing constraints. The pre-gate structure added in this revision further strengthens it.

---

## Residual Issues (not blocking, future improvement)

1. **Scenario provenance** (affects Construct Validity and Falsifiability): ~~All five constructed scenarios were designed within the methodology's ecosystem. Adding one externally-sourced scenario would further strengthen falsifiability.~~ **Addressed (2026-03-16)**: One externally-sourced scenario (Section IX-E) now replaces the information asymmetry scenario. Circularity warning extended to all remaining internal scenarios. Residual: four of five scenarios are still internal.

2. **Scenario difficulty calibration** (affects Discriminant Power): ~~Untested whether current frontier LLMs will struggle with any of these scenarios.~~ **Addressed (2026-03-16)**: Pre-Gate 2 (B1/B1-ext pilot) now tests scenario difficulty before the full run. Decision rule: if 3+ scenarios produce B1 scores of 0-1, proceed; otherwise revise.

3. **B1-ext bootstrap** (affects Executability): The token target for B1-ext depends on knowing the average C2 output length, which depends on running C2 first. Estimate ~3,000 words as starting point; adjust after first calibration run.

4. **Recommendation extraction subjectivity** (affects Confound Control): The operational blinding protocol says to extract "the final recommendation and its supporting justification." For C2, this means the resolution section. But how much of the resolution to include is a judgment call that could introduce bias. A clearer extraction protocol (e.g., "maximum 500 words from the resolution") would reduce this.

---

## Assessment

The protocol is now internally consistent, honestly framed, and executable. The critical confounds (token/effort, structural blinding) are controlled. The falsifiability gap is partially addressed (deliberation-neutral scenario, circularity warning). Statistical claims are calibrated to sample size.

**Phase A (constructed scenarios) is ready to run.** It will produce calibration data showing whether the protocol's architecture conditions generate discriminable outputs. This is valuable regardless of outcome:
- If conditions discriminate: proceed to Phase B with validated machinery.
- If conditions don't discriminate: diagnose why before investing in historical case construction.
- If B1-ext matches C2: deliberative structure may not add value beyond structured prompting — an important finding that changes the research program's direction.
- If B1 outscores C2 on the deliberation-neutral scenario: establishes a boundary condition for when deliberation helps.

**Phase B (historical cases) should wait for Phase A results.** Phase A may reveal that the protocol needs further refinement (scenario difficulty, scoring scale, extraction protocol) before the larger investment.
