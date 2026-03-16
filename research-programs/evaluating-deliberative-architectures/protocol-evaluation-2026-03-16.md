# Protocol Evaluation: Black Swan Hindsight Framework (Constructed Scenarios)

**Date**: 2026-03-16
**Evaluated document**: `research-programs/evaluating-deliberative-architectures.md`
**Scope**: Constructed scenarios only (Glenda/Crock, Blast Radius, Information Asymmetry, Cascading Mitigation) — the proposed first run.
**Rubric**: `protocol-evaluation-rubric.md` (8 dimensions, 0-3 each)

---

## Scores Summary

| Dimension | Score | One-line justification |
|-----------|-------|------------------------|
| 1. Construct Validity | 1 | Claims to test "anticipation" but constructed scenarios test checklist recognition — a fundamentally different construct. |
| 2. Confound Control | 1 | Token/effort confound is uncontrolled; structural blinding is infeasible; scenario provenance creates circularity. |
| 3. Discriminant Power | 1 | Scenarios may be too easy for capable LLMs; binary criteria collapse gradient; N=4 can't distinguish signal from noise. |
| 4. Internal Consistency | 2 | Generally coherent; some tension between general metrics (0-3 anticipation) and constructed scenario criteria (binary checklists). |
| 5. Executability | 2 | Constructed scenarios are fully specified; architecture conditions need more prompt detail; blind evaluation is operationally problematic. |
| 6. Statistical Adequacy | 0 | Protocol requests mean, 95% CI, and Cohen's d from N=4 ordinal scores. These calculations are meaningless at this sample size. |
| 7. Falsifiability | 1 | Scenarios designed by methodology's author to illustrate methodology's value; roster characters were designed to catch exactly these structural features. |
| 8. Honest Framing | 2 | Section XIII acknowledges many limitations; but the main framing ("tests anticipatory validity") overstates what constructed scenarios deliver. |

**Aggregate**: 10/24. Three dimensions at critical failure (0 or 1). The protocol should not be executed on constructed scenarios in its current form.

---

## Detailed Scoring

### Dimension 1: Construct Validity — Score: 1

**Research question** (Section I): "Which deliberative architectures anticipate structural risks that simpler approaches miss?"

**What "anticipation" means** (Section VII, Metric 1): "The degree to which the output identified, as risks or scenarios, the structural features that actually materialized in the historical outcome." The 0-3 scale runs from "absent" to "integrated" — the highest score requires the risk to be "identified, analyzed, and the recommendation explicitly accounts for it."

**What constructed scenarios actually test**: Whether the output mentions predefined structural features from a checklist. The Glenda/Crock criteria (Section VIII) are three binary items: coercion recognition (0/1), compliance trap identification (0/1), frame analysis (0/1). There is no "historical outcome" to anticipate. There is no future that materialized. There is a list of concepts the evaluator checks for.

**The gap**: Anticipation implies temporal asymmetry — seeing what's coming before it arrives. Constructed scenarios have no temporal dimension. They test whether the architecture recognizes structural patterns that the protocol designer identified in advance. This is closer to a reading comprehension test than an anticipation test. The protocol acknowledges this distinction in Section IV ("Historical cases test anticipatory validity; constructed cases test structural recognition") but the main framing (Sections I, XI, XIII) treats constructed and historical cases as addressing the same research question.

**Specific problem — Glenda/Crock**: The scenario was designed within this repo (`applications/narrative-immune-systems/glenda-crock-coercion.md`) as an application of the methodology. The structural features to be recognized (coercion frame, compliance trap, adversarial pre-framing) are concepts developed and named by the methodology itself. Testing whether the methodology's own committee characters recognize the methodology's own concepts is circular. It would be surprising if Maya (propensity: paranoid realism; asks: "Who benefits if this fails? What's the political angle?") failed to identify a coercion scenario that was designed to illustrate political coercion.

**What would raise this score**: Reframe the constructed scenarios as testing "structural feature recognition" (which is what they actually test), not "anticipation." Reserve "anticipation" claims for historical cases where temporal asymmetry is real. Or: redesign the constructed scenarios so that the structural features to be recognized were not designed by the methodology's author.

### Dimension 2: Confound Control — Score: 1

**Confound 1 — Token/effort asymmetry (uncontrolled)**:

B1 produces one response to one prompt — perhaps 300-500 words. C2 produces opening statements from five characters, structured debate across multiple rounds, and a resolution — perhaps 3,000-5,000 words. C3 adds scenario generation before that — perhaps 8,000-10,000 words total.

If C2 outscores B1, is that because deliberation helps, or because 10x more tokens means more opportunities to mention structural features? The protocol doesn't control for this. A fairer comparison would give B1 the same token budget: "Write a 3,000-word analysis of this situation" vs. "Run a committee that produces ~3,000 words." Or include a B1-extended condition: same prompt, same length, no deliberative structure.

The protocol holds "Model" and "Information" constant across conditions (Section V, Control Variables) but doesn't mention token count, response length, or effort as control variables.

**Confound 2 — Structural blinding (infeasible)**:

Section VI specifies blind evaluation: "Outputs are stripped of all metadata identifying the condition." But the outputs are structurally different. B1 is a single analytical response. C2 is a multi-character deliberation transcript with named characters, opening statements, and rounds. Even stripped of labels, these are trivially distinguishable. An evaluator — human or LLM — can identify the condition by format alone.

The protocol addresses evaluator *stylistic* bias (Section VI amendment: eloquent-but-blind vs. anticipatory-but-rough) but not evaluator *structural* bias. If the evaluator associates multi-character transcripts with higher quality (or if it's an LLM that recognizes the committee methodology from training data), blinding fails.

**Confound 3 — Scenario provenance (uncontrolled)**:

All four constructed scenarios were designed by or for the methodology's ecosystem:
- Glenda/Crock: from `applications/narrative-immune-systems/glenda-crock-coercion.md`, a document in this repo
- Blast Radius: references declarative infrastructure — a topic the repo has engaged with
- Information Asymmetry and Cascading Mitigation: follow the same design philosophy

A scenario designed to illustrate the value of structural analysis will naturally be more legible to an architecture designed for structural analysis. This is scenario selection bias. The protocol doesn't include scenarios designed to favor simpler approaches (e.g., problems where overthinking is the failure mode, or where fast decisive action outperforms deliberation).

**Confound 4 — Prompt engineering quality (uncontrolled)**:

The B3 condition is described as "Give 3-5 genuinely different perspectives on this decision, then synthesize a recommendation." This is a weak prompt. A strong B3 prompt would name specific analytical lenses (political, systemic, evidentiary, historical, values-based) — essentially replicating the committee's propensities without the deliberative structure. Testing a weak B3 against a fully designed C2 conflates "deliberation helps" with "well-designed prompts help."

**What would raise this score**: (a) Add a token-matched baseline condition. (b) Address structural blinding by extracting conclusions/recommendations only, stripping deliberative process. (c) Include scenarios not designed by the methodology's ecosystem. (d) Strengthen the B3 prompt to be a genuine best-effort competitor.

### Dimension 3: Discriminant Power — Score: 1

**Problem 1 — Capable LLMs may ace all conditions**:

The Glenda/Crock scenario asks whether the output recognizes coercion, compliance traps, and frame analysis. A capable LLM in 2026, given a scenario that literally describes extortion and blackmail, will very likely identify it as coercion regardless of architecture. The scenario description includes "credible threats," demands backed by consequences, and explicit leverage — the coercion structure is surface-level, not hidden.

The protocol predicts B1 will score 0-1 (Section VIII). This prediction may have been reasonable in early 2025 but is likely wrong for current frontier models. If B1 scores 2-3 alongside C2's 2-3, the protocol produces null results that don't inform anything.

**Problem 2 — Binary criteria collapse gradient**:

Glenda/Crock and Information Asymmetry use binary (0/1) criteria, producing composite scores of 0-3 from three yes/no questions. This creates only four possible scores per condition per scenario, with no way to distinguish "mentioned in passing" from "deeply analyzed." The general Anticipation metric (Section VII) has a 0-3 scale with descriptive anchors distinguishing peripheral mention from integrated analysis. The constructed scenario criteria lose this gradient.

Blast Radius and Cascading Mitigation use 0-2 criteria (slightly better), but the descriptions for Score 2 are often specific enough that they test for a particular phrasing rather than a general capability.

**Problem 3 — N=4 can't establish a pattern**:

Four scenarios produce four scores per condition. With six conditions, that's a 4×6 matrix of ordinal scores. Even if condition C2 outscores B1 on all four, that's N=4 — not enough to distinguish real superiority from scenario-specific advantage. One scenario where B1 beats C2 is 25% of the data.

**What would raise this score**: (a) Calibrate scenario difficulty: pilot-test each scenario with B1 and verify that B1 actually struggles before including it. Remove scenarios where B1 succeeds trivially. (b) Use the general 0-3 Anticipation scale for constructed scenarios instead of binary checklists. (c) Add more scenarios or design scenarios with multiple difficulty layers.

### Dimension 4: Internal Consistency — Score: 2

The protocol is generally coherent. The research question, conditions, and metrics form a logical structure. The historical/constructed distinction is properly maintained. The results tables match the evaluation protocol. Two tensions:

**Tension 1**: The general Anticipation metric (Section VII) is a thoughtful 0-3 scale measuring whether risk categories were identified, analyzed, and integrated into recommendations. The constructed scenario criteria (Sections VIII-IX) are binary checklists measuring whether specific concepts were mentioned. These are different measurement approaches applied within the same protocol, making cross-comparison difficult. Table 1b asks for "Anticipation (0-3)" scores for constructed cases, but the scenario-specific criteria produce different scales (0-3 for Glenda/Crock, 0-6 for Blast Radius).

**Tension 2**: Section VIII includes "Expected results by architecture" — predictions stated in advance to prevent post-hoc rationalization. This is good practice. But the predictions are extremely specific ("B1 is predicted to score 0-1... C2 is predicted to score 2-3") and frame confirmation as the expected outcome. If predictions are confirmed, is that evidence for the methodology or evidence that the test was calibrated to confirm? The protocol says "If results contradict these predictions, report that honestly" — but this framing treats contradiction as the noteworthy case, not confirmation.

**What would raise this score**: Unify the measurement approach across constructed and historical cases (use the general 0-3 scale for both). Reframe predictions as "what we'd consider surprising" rather than "what we expect."

### Dimension 5: Executability — Score: 2

**Strengths**: All four constructed scenario prompts are provided verbatim (Sections VIII, IX, IX-B, IX-C). Success criteria are defined with specific evaluation questions. The phased structure (corpus construction → runs → evaluation → analysis) is clear. The results tables are pre-formatted.

**Gaps**:

The architecture conditions (Section V) describe each condition in one sentence. For B1-B3, the one-sentence descriptions are sufficient (they're simple prompts). For C1, the "coordinator synthesizes" step is undefined — what prompt does the coordinator use? How are the five independent respondents prompted? For C2 and C3, the protocol references `/committee` and `/scenarios` — these are defined skills in this repo, so executability depends on skill availability.

Blind evaluation is operationally problematic for the reasons described in Dimension 2 (structural distinguishability). An executor following the protocol as written would strip labels but produce outputs that are obviously different in kind.

The protocol recommends human raters for the first run (Section VI amendment) but doesn't specify how to recruit them, what domain expertise they need, or what training/calibration beyond the pilot cases. It estimates $2-4K — feasible but non-trivial.

**What would raise this score**: Specify the C1 coordinator prompt. Define what "blind evaluation" means operationally when outputs are structurally different (e.g., evaluate only the final recommendation and its justification, not the process transcript). Provide evaluator recruitment criteria.

### Dimension 6: Statistical Adequacy — Score: 0

The results tables (Section XII) request:
- **Table 1b**: "mean [95% CI]" for Anticipation and Epistemic Humility across conditions, with N=4 constructed scenarios
- **Table 4**: "Cohen's d" with "95% CI" for pairwise condition comparisons

With N=4 ordinal (0-3) scores per condition:
- A **mean** of four ordinal values has no useful precision. The difference between means of 1.75 and 2.25 is one scenario scoring differently.
- A **95% confidence interval** from N=4 is so wide it will include nearly the entire scale. For a Poisson or ordinal variable with range 0-3 and N=4, a CI might be ±1.5, rendering it useless.
- **Cohen's d** requires at least rough normality and N>10 per group to be stable. With N=4 and ordinal data, Cohen's d is undefined or misleading.

The protocol acknowledges small N in Section XIII ("With 6-10 cases, effect sizes are unstable. This is a pilot; treat results as directional, not definitive") — but the results tables still request the calculations. A results table that asks for meaningless statistics undermines the credibility of results that *are* meaningful (like the qualitative observations and case-by-case narrative).

**What would raise this score**: Replace Table 1b and Table 4 for constructed scenarios with appropriate representations: case-by-case score tables showing the raw scores per condition per scenario, possibly with a descriptive comparison (e.g., "C2 scored higher than B1 on 3 of 4 scenarios"). Reserve mean, CI, and Cohen's d for the full program (historical + constructed, N=8-10) and explicitly note that even that N is marginal. For constructed scenarios alone, report raw scores and qualitative observations.

### Dimension 7: Falsifiability — Score: 1

**Problem 1 — Scenario provenance bias**:

All four constructed scenarios were designed within the methodology's ecosystem to illustrate the kind of structural thinking the methodology enables. The Glenda/Crock scenario comes from a repo document analyzing coercion dynamics through the methodology's lens. The Blast Radius scenario tests for second-order systems thinking — Tammy's propensity. The Information Asymmetry scenario tests for adversarial due diligence — Maya's propensity. The Cascading Mitigation scenario tests for systems thinking and alternative framing — Tammy and Maya again.

The committee characters were designed to catch these specific categories of structural feature. Testing the committee against scenarios that exemplify its design targets is like testing a calculator on arithmetic and concluding it outperforms a dictionary.

For genuine falsifiability, the protocol would need scenarios where:
- Deliberation produces worse outcomes than quick action (paralysis by analysis)
- The committee's propensity design is a poor fit (e.g., routine operational decisions, purely technical optimizations, situations where political analysis is genuinely irrelevant)
- Simpler approaches succeed because the problem doesn't benefit from multi-perspective analysis

**Problem 2 — Interpretive asymmetry**:

The protocol frames confirmation as expected ("Expected results by architecture": C2 scores 2-3, B1 scores 0-1) and disconfirmation as surprising ("If results contradict these predictions, report that honestly"). This creates an interpretive asymmetry: confirmation is absorbed smoothly while disconfirmation demands explanation. A falsifiable design would instead specify: "If B3 scores within 0.5 points of C2 on average, the deliberative structure does not add value beyond multi-perspective prompting."

**Problem 3 — No scenarios where B1 should win**:

All four scenarios are designed to reward depth and multi-perspective analysis. None test whether the methodology adds overhead without benefit on problems that are simpler than they appear. A protocol designed for falsifiability would include scenarios where overthinking is the failure mode.

**What would raise this score**: (a) Include at least one scenario designed to favor B1 or B3 (a problem where deliberation adds overhead without insight). (b) Specify explicit falsification criteria before running (e.g., "if C2 does not outscore B3 by at least 1 point on at least 3 of 4 scenarios, the hypothesis is not supported for structural feature recognition"). (c) Include scenarios designed by someone unfamiliar with the methodology's categories.

### Dimension 8: Honest Framing — Score: 2

**Strengths**: The protocol has a thorough Limitations section (Section XIII) that identifies seven specific limitations including hindsight bias, small N, contamination risk, single-model limitation, case selection effects, anticipation vs. decision quality, and the static-prompt limitation. The Section IV amendment explicitly states "Historical cases test anticipatory validity; constructed cases test structural recognition... reported separately, never aggregated." This is honest and important.

**Gap**: Despite the amendment in Section IV, the main framing throughout the document (title, Section I, Section XI) treats the protocol as testing "anticipatory validity" without consistently distinguishing what the constructed scenarios contribute from what the historical cases contribute. A reader encountering only the title and Section I would conclude that the protocol tests anticipation. Only after reading the Section IV amendment would they learn that half the cases test something different (structural recognition).

The predictions in Section VIII ("B1 is predicted to score 0-1") could be read either as honest advance registration (good scientific practice) or as confidence in a predetermined outcome (suggesting the test is confirmatory, not exploratory).

**What would raise this score**: (a) Add a paragraph to the introduction explicitly distinguishing what the constructed-scenario run can show (structural feature recognition, not anticipation) from what the full program with historical cases can show. (b) Frame the constructed-scenario run as "calibration and machinery testing" rather than as evidence for the main research question.

---

## Critical Findings

### Three dimensions at 0 or 1 (must fix before execution):

1. **Construct Validity (1)**: The constructed scenarios test structural feature recognition from a predefined checklist, not anticipation. The scenarios were designed within the methodology's ecosystem, making the test circular for assessing the methodology.

2. **Confound Control (1)**: Token/effort asymmetry between conditions is uncontrolled. A 10x difference in output length could explain any observed score differences without reference to deliberative quality. Structural blinding is infeasible.

3. **Statistical Adequacy (0)**: The results tables request statistics (mean, 95% CI, Cohen's d) that are meaningless at N=4 with ordinal data.

### One dimension at 1 (should fix):

4. **Falsifiability (1)**: All scenarios favor the methodology; none test where simpler approaches should win. The methodology's roster was designed to catch exactly the structural features these scenarios test.

### Two dimensions adequate (minor fixes only):

5. **Internal Consistency (2)**: Mostly coherent; unify measurement scales across general and scenario-specific criteria.
6. **Executability (2)**: Mostly executable; specify C1 coordinator prompt and define operational blinding.

### One dimension adequate:

7. **Honest Framing (2)**: Good limitations section; main framing slightly overclaims for constructed scenarios.

### One dimension not separately scored (insufficient data):

8. **Discriminant Power (1)**: Scenario difficulty may be miscalibrated for current LLMs; binary criteria collapse gradient. Requires pilot testing to assess properly.

---

## Remediation Plan

### Must-fix (raise to 2+ before executing)

**1. Reframe the constructed-scenario run as machinery calibration, not evidence.**

The constructed scenarios serve a legitimate purpose: they verify that the pipeline works, that scoring is consistent, that the evaluation protocol is operationally feasible, and that the architecture conditions produce meaningfully different outputs. This is valuable! But it is calibration, not evidence for the main research question. Reframe accordingly:

- Retitle the constructed-scenario run: "Protocol Calibration: Constructed Scenario Pilot"
- State explicitly: "This run tests whether the experimental machinery works and whether the architecture conditions produce discriminable outputs. It does not test anticipatory validity (which requires historical cases with temporal asymmetry). Findings are used to refine the protocol before the historical-case run."
- Remove the predictions from Section VIII or reframe them as "calibration expectations" — benchmarks for verifying the protocol discriminates between conditions, not hypotheses about the methodology's value.

**2. Add a token-matched baseline condition.**

Add B1-extended: "Analyze this situation in detail. Write approximately [N] words. Consider the problem from multiple angles: political dynamics, systemic effects, historical precedent, evidentiary gaps, and values at stake." Set N to match the average C2 output length. This isolates "deliberation helps" from "more words help." If B1-extended matches C2, the deliberative structure adds nothing beyond token budget.

**3. Fix statistical framing for N=4.**

Replace Tables 1b and 4 (for constructed scenarios) with:
- A raw-score matrix: scenario × condition × criterion score
- A descriptive comparison table: for each condition pair, how many scenarios did A outscore B?
- Qualitative observations from the evaluator

Reserve inferential statistics for the full program (N=8-10, and even then with caveats).

**4. Add at least one scenario where deliberation shouldn't help.**

Design or source a scenario where:
- The structural analysis is straightforward and doesn't benefit from multi-perspective debate
- The decision is primarily technical or operational, not political or value-laden
- Overthinking or looking for hidden dynamics is the failure mode (the problem is exactly what it appears to be)

If C2 outscores B1 even on this scenario, that's interesting. If B1 matches or beats C2, that's informative about boundary conditions.

### Should-fix (improve quality but not blocking)

**5. Strengthen the B3 prompt.**

Rewrite the B3 condition to be a maximally strong single-prompt competitor: name specific analytical lenses, request structured analysis, ask for explicit trade-off identification. This ensures the comparison is deliberation-vs-best-alternative, not deliberation-vs-weak-prompt.

**6. Define operational blinding.**

Since full output blinding is infeasible (C2 transcripts are structurally distinguishable from B1 responses), define what "blind evaluation" means operationally:
- Option A: Extract only the final recommendation and its justification from each output, discarding process transcripts. Evaluate the recommendations.
- Option B: Accept that full blinding is impossible and instead use outcome-focused metrics that are resistant to format bias.
- Option C: Use the full outputs but run the evaluator bias calibration protocol (already in the protocol) with format-matched synthetic outputs to quantify format bias.

**7. Unify scoring criteria.**

Apply the general Anticipation metric (0-3 with descriptive anchors) to constructed scenarios instead of using binary checklists. The binary checklists can serve as coding guides for what to look for, but the final score should use the same scale as the historical cases.

### Nice-to-have (further refinement)

**8. Include an externally-sourced scenario.**

Find or commission a scenario from outside the methodology's ecosystem — e.g., an existing case study from a business school, a decision scenario from another deliberation research program, or a problem designed by someone unfamiliar with cyberneutics. This addresses the provenance confound.

**9. Pilot-test scenario difficulty.**

Before the full run, test each scenario with B1 only. If B1 scores 2+ on the general Anticipation scale, the scenario is too easy to discriminate between conditions. Replace or harden it.
