# Evaluating Deliberative Architectures: The Black Swan Hindsight Framework

**Status**: Not started
**Runs**: None yet
**Results**: [evaluating-deliberative-architectures/results/](evaluating-deliberative-architectures/results/)

> **Contributing to this program**
> - **Skills needed**: LLM prompt automation, historical research, qualitative evaluation, familiarity with the committee pipeline (`/committee`) and evaluation dimensions in [evaluation-schemes.md](evaluation-schemes.md).
> - **Estimated scope**: 4-6 weeks for corpus construction, architecture runs, and initial analysis.
> - **Contributor type**: Paired recommended (one designs cases, one evaluates blind). Solo possible but slower.
> - **Entry point**: Read Sections I-III (problem, innovation, contamination). Then read [evaluation-schemes.md](evaluation-schemes.md) Sections III and VIII for dimension codebooks. Start with the **protocol calibration run** (Phase A: all constructed scenarios, Section VIII-IX) — it requires no historical research and verifies that the experimental machinery produces discriminable, scorable outputs before investing in historical case construction. Phase A is calibration, not evidence for the core claim. See also [protocol-evaluation-rubric.md](evaluating-deliberative-architectures/protocol-evaluation-rubric.md).

**Last updated**: 2026-03-16

**Origins**: Identified as a distinct research design that complements the [evaluation-schemes](evaluation-schemes.md) framework. Where evaluation-schemes tests process quality (do structured methods produce better-reasoned outputs?), this framework tests *anticipatory validity* (do structured methods see what's coming?). Related to but distinct from Design C in evaluation-schemes — see [Section XI](#xi-relationship-to-evaluation-schemes-design-c) for the distinction.

**Important distinction**: This framework has two phases that test different things and should be reported separately:
- **Phase A — Protocol calibration (constructed scenarios)**: Tests whether the experimental machinery works — whether the architecture conditions produce discriminably different outputs, whether scoring is consistent, and whether the evaluation protocol is operationally feasible. Does *not* test anticipatory validity (constructed scenarios have no temporal asymmetry and no historical outcome to anticipate). Findings refine the protocol and may reveal whether conditions produce *any* structural differences worth measuring.
- **Phase B — Anticipatory validity (historical cases)**: Tests the framework's core question — whether deliberative architectures anticipate structural risks that simpler approaches miss. Requires historical cases with reconstructable knowledge boundaries and known outcomes. This is the evidential phase.

See [protocol-evaluation-rubric.md](evaluating-deliberative-architectures/protocol-evaluation-rubric.md) for the rubric used to evaluate this protocol, and [protocol-evaluation-2026-03-16.md](evaluating-deliberative-architectures/protocol-evaluation-2026-03-16.md) for the initial evaluation and remediation that produced the current version.

---

## I. Problem Statement

Testing deliberative architectures (such as adversarial committees and peer-agent networks) is inherently difficult because they are applied to "wicked problems" — situations where there is no definitively "correct" answer at the time of the decision. Without ground truth, evaluating whether an architecture performed well often devolves into evaluating whether we simply liked its output.

The evaluation-schemes framework addresses this by measuring *process quality* (assumption coverage, reasoning completeness, etc.) without requiring ground truth. But process quality is a proxy — an output can score high on all dimensions and still miss the thing that mattered.

This framework attacks the problem from the other direction: **use historical hindsight to create ground truth retroactively.** While black swans and complex systemic shocks are unpredictable in the moment, they are often obvious in retrospect. A decision point that was genuinely uncertain at the time becomes legible after the fact.

The core question: **Which deliberative architectures anticipate structural risks that simpler approaches miss?**

---

## II. The Core Innovation: Hindsight as Ground Truth

The framework exploits a temporal asymmetry: what was uncertain *then* is knowable *now*. This converts wicked problems into evaluable problems — after the fact.

### Three-Stage Design

**Stage 1: Select and Prepare Historical Cases**
Identify historical scenarios where the outcome is now visible. Construct a knowledge-bounded presentation of the scenario that includes only information available at the decision point. Apply contamination mitigations (Section III).

**Stage 2: Run Competing Architectures**
Present the knowledge-bounded scenario to multiple deliberative architectures (Section V) under identical conditions. Collect their recommended actions, reasoning paths, risk assessments, and confidence levels.

**Stage 3: Evaluate Against Historical Record**
A blind evaluator (Section VI) assesses each architecture's output against the actual historical outcome, scoring on operationalized metrics (Section VII). The evaluator does not know which architecture produced which output.

### What This Design Can and Cannot Show

**Can show**: Which architectures anticipated structural risks. Which were appropriately uncertain. Which fell into predictable failure modes (overconfidence, compliance traps, single-scenario optimization).

**Cannot show**: Which architectures would have produced "better decisions" in a counterfactual sense — outcomes depend on execution, context, and luck, not just the quality of the decision at the point of commitment. Note: high scores on Anticipation (level 3, "Integrated") *do* test solution-building in the sense that the recommendation must account for the risk through contingency planning or adaptive strategy. But they do *not* test the ability to execute on that strategy, adapt it under dynamic conditions, or interactively investigate the developing situation. The framework tests whether architectures see what's coming and plan for it; it does not test whether they can navigate it in real time.

---

## III. The Knowledge Contamination Problem

The most serious methodological threat to this design: LLMs may already *know* the historical outcome. If the deliberating model draws on outcome knowledge, the experiment measures recall, not anticipation.

### Three Mitigation Strategies

Use at least one per case; combine where feasible.

#### Strategy A: Post-Cutoff Cases

Use scenarios where the decision point falls *after* the LLM's training data cutoff. The model genuinely cannot know the outcome because it wasn't in the training data.

- **Strength**: Eliminates contamination completely.
- **Weakness**: Limits the case corpus to recent events; outcomes may not have fully played out yet.
- **When to use**: When the LLM's knowledge cutoff is known and recent cases with clear outcomes exist.

#### Strategy B: Structural Transposition

Take a real historical case and transpose it into a different domain, changing names, industries, and surface details while preserving the structural dynamics. The LLM encounters a scenario it cannot pattern-match to a known event.

- **Strength**: Works for any historical period; preserves the structural features that matter.
- **Weakness**: Transposition may inadvertently change the structural dynamics; requires careful design; the evaluator must map transposed outcomes back to the real case.
- **When to use**: For well-known cases (financial crises, famous organizational failures) where contamination is certain.
- **Protocol**: Two independent people verify that the transposition preserves: (a) the information asymmetry, (b) the key structural tensions, (c) the decision point and available options. Document the mapping.

#### Strategy C: Granularity Below Training Data

Use cases that are too specific, too local, or too obscure to appear in training data. Organizational decisions, departmental strategy shifts, small-company pivots, local policy changes.

- **Strength**: Large pool of available cases; realistic decision contexts.
- **Weakness**: Cannot guarantee absence from training data; harder to find well-documented cases with clear outcomes.
- **When to use**: As the primary strategy for most of the corpus. Combine with a contamination probe (below).

### Contamination Probe

For any case where contamination is uncertain, run a **contamination check** before the main experiment:

1. Present the scenario to a fresh LLM instance.
2. Ask: "Do you recognize this scenario? Can you identify the real-world event it describes? What happened?"
3. If the model identifies the case or predicts the outcome, the case is contaminated for that model. Either transpose it (Strategy B) or exclude it.
4. Record the probe result in the case file.

---

## IV. Historical Case Corpus

### Selection Criteria

Each case must satisfy all five:

1. **Clear decision point**: A specific moment where a choice was made (or could have been made) with identifiable options.
2. **Outcome now visible**: The consequences of the decision (or lack of decision) have played out sufficiently to evaluate (minimum 6 months, ideally 1-2 years).
3. **Reconstructable knowledge boundary**: We can identify what information was available at the decision point and exclude later information.
4. **Causal record exists**: Sufficient documentation (reporting, post-mortems, case studies) to reconstruct the causal chain from decision to outcome.
5. **Manageable contamination**: The case passes the contamination probe, or can be transposed without losing structural features.

### Corpus Size and Composition

> **Amendment note (2026-02-26)**: Committee deliberation identified that the intersection of "granular enough to escape training data" and "documented enough to build causal records" is severely constrained (Joe). The corpus is therefore composed of two distinct types — historical and constructed — that are **reported separately, never aggregated into a blended score**. Historical cases test anticipatory validity (the framework's unique contribution); constructed cases test structural recognition (contamination-free but scored against predefined criteria rather than historical outcomes). Blending the two would obscure what each type of evidence shows.

- **Target**: N = 8-10 cases total (4-5 historical + 4-5 constructed).
- **Historical cases**: Use Strategy C (granularity) with rigorous contamination probing as the primary approach. If a case fails the contamination probe, **exclude it** rather than transpose it — Strategy B (transposition) introduces uncontrolled contextual priors that contaminate the experiment in a different way (Joe). Accept that you may end up with fewer historical cases than planned; 3-4 clean historical cases are more valuable than 6 contaminated ones.
- **Constructed cases**: Pure tests of structural recognition. No contamination risk, but scored against predefined criteria rather than historical outcomes. Include Glenda/Crock, Blast Radius, and 2 additional constructed scenarios (see below).
- **Domain distribution** (for historical cases): At least 2 domains from:
  - **Organizational/strategic**: Company pivots, restructurings, market entries, technology bets.
  - **Infrastructure/operational**: Deployment decisions, system architecture choices, migration strategies, incident responses.
  - **Policy/institutional**: Regulatory changes, institutional reforms, public health decisions, standards adoption.

### Case Types

The corpus includes two distinct case types that require different protocols:

| Type | Example | Knowledge boundary | Evaluation basis | Contamination risk |
|------|---------|-------------------|-----------------|-------------------|
| **Historical** | Real organizational decision with known outcome | Information available at decision date | Actual historical outcome | Medium-High; use Strategies A/B/C |
| **Constructed** | Glenda/Crock coercion scenario | Scenario description as given | Whether architecture recognizes structural features (coercion frame, compliance trap) | None (fictional) |

Historical cases test anticipatory validity. Constructed cases test structural recognition — whether the architecture identifies features of the problem that a simpler approach would miss.

### Candidate Cases

These are starting points; each requires a contamination probe and full case construction before use.

**Organizational/Strategic:**
1. **A mid-size SaaS company's decision to pursue enterprise sales** (c. 2020-2022). The structural tension: enterprise sales requires longer cycles, higher support costs, and product changes that alienate the existing SMB base. The black swan: the SMB market contracted faster than expected during economic downturn, making the enterprise pivot either prescient or catastrophic depending on timing. *Contamination*: Strategy C (specific enough to avoid training data); probe required.
2. **An open-source project's governance transition** (e.g., moving from BDFL to foundation model). The structural tension: formalized governance introduces overhead and politics; informal governance creates key-person risk. The outcome: whether the transition preserved contributor engagement and release velocity, or triggered a fork/exodus. *Contamination*: Strategy C; many such transitions exist with varying outcomes.

**Infrastructure/Operational:**
3. **A declarative infrastructure migration** (NixOS fleet management, Kubernetes adoption, or similar). The structural tension: declarative approaches reduce drift but increase blast radius — a bad configuration propagates instantly. The outcome: whether the migration succeeded or produced a cascading failure. *Contamination*: Strategy C.
4. **A database migration under load** (e.g., moving from relational to document store, or single-region to multi-region). The decision point: migrate incrementally (dual-write) or cut over. The outcome is typically well-documented in engineering post-mortems. *Contamination*: Strategy C; specific cases are unlikely to be in training data.

**Policy/Institutional:**
5. **A professional standards body adopting AI-generated content policies** (2023-2024). The structural tension: permissive policies risk quality degradation; restrictive policies drive contributors to competing venues. The outcome: whether the policy was enforceable and what happened to submission quality and volume. *Contamination*: Strategy A or B depending on timing.
6. **A municipal open data initiative** deciding what to publish and under what terms. The structural tension: transparency vs. re-identification risk, public benefit vs. commercial exploitation. The outcome: adoption rates, privacy incidents, policy reversals. *Contamination*: Strategy C.

**Constructed (4 internal + 1 external):**
7. **Glenda/Crock coercion scenario** — see [Section VIII](#viii-glendacrock-test-protocol) for dedicated protocol.
8. **Blast radius scenario** — see [Section IX](#ix-blast-radius-test-protocol) for dedicated protocol.
9. **Cascading mitigation scenario** — see [Section IX-C](#ix-c-cascading-mitigation-test-protocol) for dedicated protocol. Tests whether the architecture traces second-order consequences of the obvious fix.
10. **Deliberation-neutral scenario** — see [Section IX-D](#ix-d-deliberation-neutral-test-protocol) for dedicated protocol. Tests whether the architecture can recognize a straightforward problem and act proportionately rather than manufacturing complexity. Expected to favor simpler architectures (B1, B2) over deliberative ones (C2, C3).
11. **Externally-sourced scenario** — see [Section IX-E](#ix-e-externally-sourced-test-protocol) for dedicated protocol. A well-known case study *not* designed within the methodology's ecosystem, included to partially mitigate the circularity of testing a methodology against its own showcase scenarios. Replaces the information asymmetry scenario (IX-B), which tested Vic-type analysis on a Vic-designed scenario.

> **Amendment note (2026-03-16)**: The information asymmetry scenario (formerly item 9, Section IX-B) was replaced by an externally-sourced scenario per committee recommendation ([deliberations/protocol-eval/03-resolution.md](../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)). The committee identified that all five original constructed scenarios were designed within the methodology's ecosystem, creating circularity that the Glenda/Crock warning alone did not fully address. One externally-sourced scenario — designed by someone unfamiliar with the roster — partially breaks this circularity. Section IX-B is retained for reference but excluded from Phase A.

---

## V. Architecture Comparison Matrix

Each case is run through all conditions. The independent variable is the deliberative architecture.

### Conditions

| Condition | Architecture | Description |
|-----------|-------------|-------------|
| **B1** | Single LLM | One prompt, one response: "Given this situation, what should we do? Explain your reasoning." |
| **B1-ext** | Single LLM (effort-matched) | Same as B1 but with explicit depth and length instruction: "Analyze this situation in detail. Consider it from multiple angles: political dynamics and power relationships, systemic effects and feedback loops, historical precedents and patterns, gaps in available evidence, and values or principles at stake. For each angle, identify the key risks and trade-offs. Then synthesize a recommendation that accounts for the most important risks. Write approximately [N] words." Set [N] to the average C2 output length from the first calibration run (or estimate ~3,000 words). This isolates "deliberative structure helps" from "more tokens/effort helps." |
| **B2** | Chain-of-thought | Single LLM with structured reasoning: "Think step by step. What are the key factors? What are the risks? What do you recommend?" |
| **B3** | Multi-perspective prompt (strong) | Single LLM asked for structured multi-perspective analysis: "Analyze this situation from five distinct perspectives, then synthesize. For each perspective, adopt a specific analytical stance and argue from it genuinely — do not hedge or immediately qualify. Perspectives: (1) Power and incentives — who benefits, who loses, what political dynamics are at play? (2) Precedent and history — what has happened before in analogous situations, and what does it suggest? (3) Evidence and verification — what claims are supported, what's assumed, what's missing? (4) Systems and second-order effects — what feedback loops, unintended consequences, or cascade risks exist? (5) Values and mission — what principles are at stake, and what would we be trading away? After presenting all five perspectives, identify the key tensions between them and synthesize a recommendation that explicitly names which trade-offs you are accepting." |
| **C1** | Hub-and-spoke committee | Central coordinator distributes the question to 5 independent respondents, then synthesizes. Respondents do not see each other's outputs. (CJT-style; see [condorcet-comparison.md](condorcet-comparison.md).) Coordinator synthesis prompt: "You have received five independent analyses of the same situation. Identify where they agree and disagree. For each disagreement, determine which analysis is better supported. Synthesize a recommendation that accounts for the strongest arguments from each respondent. Name the key risks and trade-offs." |
| **C2** | Peer-agent committee | Full adversarial committee with fixed roster, Robert's Rules, deliberation, and resolution. (Standard `/committee` pipeline.) |
| **C3** | Deliberated choice | Fan (scenario generation) followed by funnel (committee deliberation on scenarios). Full `/scenarios` → `/committee` pipeline. |

In addition, C2 is run **twice** per case (not once) to enable the qualitative convergence check (Section VII). This is not a separate condition — the second C2 run uses identical inputs and settings; the only variable is sampling randomness.

> **Amendment note (2026-03-16)**: B1-ext and the strengthened B3 were added to address a confound control gap identified in [protocol-evaluation-2026-03-16.md](evaluating-deliberative-architectures/protocol-evaluation-2026-03-16.md). Without B1-ext, any score difference between B1 and C2 could be explained by token/effort asymmetry rather than deliberative structure. Without a strong B3, the comparison conflates "deliberation helps" with "well-designed prompts help." The critical comparison is now **B1-ext vs. C2**: same topic, same model, comparable depth and length, but one uses deliberative structure and the other doesn't. If B1-ext matches C2, deliberative structure adds nothing beyond structured prompting with adequate token budget. The C1 coordinator prompt was also specified explicitly.

### Control Variables

Hold constant across all conditions for a given case:
- **Model**: Same base LLM (e.g., Claude Sonnet) for all conditions. (Multi-model effects are tested in [multi-model-committee.md](multi-model-committee.md), not here.)
- **Information**: Identical knowledge-bounded scenario presentation.
- **Temperature/sampling**: Temperature=0 for all conditions in Phase A (removes sampling randomness so that any C2 convergence check differences reflect structural sensitivity, not temperature noise). For Phase B, nonzero temperature may be used to test robustness; document the settings used.
- **Prompt framing**: Each condition gets the same scenario description; only the deliberative structure differs.
- **Evaluation input**: To control for structural distinguishability, the evaluator receives only the **final recommendation and its justification** from each condition, not the full process transcript. For conditions that produce multi-stage outputs (C1 synthesis, C2 resolution, C3 resolution), extract the resolution/recommendation section. For B1-B3, the full output is the recommendation. See Section VI for details.

### Run Budget

- **Cases**: N = 9-11 (4-5 historical + 5-6 constructed; see corpus composition below)
- **Conditions**: 7 (B1, B1-ext, B2, B3, C1, C2, C3)
- **Runs per condition**: 1, except C2 which runs twice per case (convergence check)
- **Total runs**: N × 8 (7 conditions + 1 extra C2 run)
- **For N=10**: 80 runs
- **Phase A (calibration, constructed only, N=5-6)**: 40-48 runs
- **Phase B (evidential, historical only, N=4-5)**: 32-40 runs

---

## VI. Stage 3: Blind Evaluation Protocol

### Evaluator Design

The Stage 3 evaluator assesses each architecture's output. The evaluator must be:

1. **Blind to architecture**: See operational blinding protocol below.
2. **Informed about the outcome** (Phase B only): For historical cases, the evaluator has access to the full historical record, including the actual outcome. For Phase A (constructed scenarios), there is no outcome — the evaluator scores against the structural recognition criteria (Section VII-A).
3. **Independent**: The evaluator is a fresh LLM instance (or human rater) that did not participate in any Stage 2 deliberation.

#### Operational Blinding Protocol

> **Amendment note (2026-03-16)**: Full output blinding is infeasible — a single-paragraph B1 response is structurally distinguishable from a multi-page C2 deliberation transcript. An evaluator (human or LLM) can trivially identify the condition by format alone, making "blind" evaluation non-blind.

**Solution: Evaluate recommendations, not process.** For all conditions, extract only the **final recommendation and its supporting justification** for evaluation. Discard process transcripts (deliberation rounds, scenario narratives, character exchanges).

Extraction rules:
- **B1, B1-ext, B2**: The full output is the recommendation. Include as-is.
- **B3**: Extract only the synthesis/recommendation section (after the multi-perspective analysis). If the synthesis references specific perspectives, retain those references.
- **C1**: Extract only the coordinator's final synthesis, not the individual respondent outputs.
- **C2**: Extract only the resolution (03-resolution.md content or equivalent): the decision, its justification, key trade-offs named, and recommended next steps. Discard the opening statements, debate rounds, and character names.
- **C3**: Extract only the final committee resolution. Discard scenario narratives and the deliberation process.

After extraction, normalize formatting: remove headers, character names, section labels. Present each as a plain-text recommendation with justification. Randomize order and assign anonymous IDs (Response Alpha, Response Beta, etc.).

**What this preserves**: The *substance* of the recommendation — what risks were identified, what trade-offs were named, what action was recommended and why.
**What this removes**: The *process signature* that reveals the architecture — character names, debate structure, scenario headings, deliberation format.
**Residual blinding risk**: Longer or more detailed recommendations may still correlate with multi-stage architectures. The token-matched B1-ext condition partially controls for this. Report recommendation lengths alongside scores so that length-score correlation can be assessed.

#### Dual-Evaluator Requirement (Phase A)

> **Amendment note (2026-03-16)**: Added per committee recommendation ([deliberations/protocol-eval/03-resolution.md](../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)). Single-evaluator scoring on a 4-point ordinal scale provides no reliability signal. A 1-point difference between conditions could be evaluator noise rather than genuine architectural advantage.

**For Phase A (constructed scenarios)**: Score every recommendation with two independent evaluators. Use two different LLM models (e.g., Claude and GPT-4o), or one LLM and one human pass. Report inter-rater agreement alongside scores. If evaluators disagree by >1 point on more than 20% of scores, investigate whether the disagreement is systematic (one evaluator favors longer outputs, one weights specific features differently) before interpreting condition comparisons.

**For Phase B (historical cases)**: Human raters are primary (see below). LLM evaluators serve as secondary check. Report inter-evaluator agreement.

### Evaluator Prompt Templates

**Phase B (historical cases)** — for each (case, anonymized recommendation) pair:

```
You are evaluating a decision recommendation. You have access to two documents:

1. SCENARIO: A description of the situation as it appeared at the decision point.
2. RECOMMENDATION: An anonymized response recommending a course of action.

You also know what actually happened afterward:
3. OUTCOME: [Historical outcome description]

Evaluate the RECOMMENDATION on the following dimensions. For each, provide a score (0-3) and a one-sentence justification citing specific text from the RECOMMENDATION.

[Dimension rubrics — see Section VII, Metrics 1-2]
```

**Phase A (constructed scenarios)** — for each (scenario, anonymized recommendation) pair:

```
You are evaluating a decision recommendation. You have access to:

1. SCENARIO: A description of a decision situation.
2. RECOMMENDATION: An anonymized response recommending a course of action.
3. STRUCTURAL FEATURES: A list of structural features this scenario was designed to test.

Score the RECOMMENDATION on the Unified Structural Recognition Scale (0-3):

0 — Surface only: addresses the scenario at face value without engaging with structural features.
1 — Partial recognition: identifies one structural feature but doesn't develop it.
2 — Substantive engagement: identifies key structural features, analyzes implications, adjusts recommendation.
3 — Integrated structural analysis: identifies structural features, traces interactions, recommendation accounts for dynamics. (For the deliberation-neutral scenario: recognizes simplicity and acts proportionately.)

Provide a score and a one-paragraph justification citing specific text from the RECOMMENDATION. Also score the scenario-specific criteria listed below.

[Scenario-specific criteria — see Sections VIII-IX]
```

### Evaluator Calibration

Before scoring the full corpus:
1. Run the evaluator on 2 pilot cases with known "easy" distinctions (e.g., one output that clearly anticipated the outcome, one that clearly didn't).
2. Check that scores track the expected direction.
3. If using human raters: calibrate on 2 pilot cases, compute inter-rater agreement, refine rubrics if kappa < 0.70.

### Evaluator Stylistic Bias Protocol

> **Amendment note (2026-02-26)**: Committee deliberation raised the concern that a blind evaluator LLM may grade "eloquence" over "anticipation" — preferring well-structured, corporate-sounding outputs regardless of whether they actually anticipated the risk (Maya). This concern was accepted without empirical evidence (flagged in both evaluations as an unchallenged prior). Rather than enshrining it as a known fact, we convert it into a **testable hypothesis** with a calibration protocol.

**Bias calibration pairs**: Before the main evaluation, construct 2-3 pairs of synthetic outputs for a pilot case:
- **Pair type A (anticipatory but rough)**: Output is informal, short, and poorly structured — but explicitly identifies the risk category that actually materialized, including some analysis of its consequences. Reads like field notes, not a polished report.
- **Pair type B (eloquent but blind)**: Output is well-structured, uses professional language, names multiple risks — but does *not* identify the risk category that actually materialized. Reads like a competent strategy memo that missed the point.

Run the evaluator on these pairs. Score using the Anticipation rubric (Section VII, Metric 1).

**Interpretation**:
- If the evaluator consistently scores Type B higher than Type A on Anticipation, **the stylistic bias exists** for this evaluator. Revise the rubrics: add explicit instructions to ignore prose quality and score only on whether the risk category was identified. Re-run calibration.
- If the evaluator scores Type A higher than Type B, **the rubrics are sufficient** to override stylistic priors. Proceed with the main evaluation. Record the calibration result.
- If the evaluator scores them equally, **the rubric is not discriminating**. Investigate whether the rubric definition is too vague to distinguish anticipation from articulate hedging.

**Evaluator diversity**: Run Stage 3 with two different evaluator models (e.g., Claude and GPT-4o). Compute inter-evaluator agreement (Cohen's kappa). Where they disagree, investigate whether disagreement tracks stylistic features (one evaluator prefers longer/more structured outputs) or substantive features (one evaluator weights risk identification differently). Report evaluator agreement alongside main results.

**Human raters recommended for first run**: For the initial execution of this framework, use human raters with the codebook as primary evaluators. LLM evaluators serve as a secondary check. This directly sidesteps the stylistic bias concern for the pilot while generating data on whether LLM evaluators agree with human judgments — evidence that can inform whether LLM-only evaluation is safe for subsequent runs.

---

## VII. Evaluation Metrics

Three primary metrics, each operationalized with coding rubrics. These are specific to the hindsight framework; they complement (not replace) the evaluation-schemes dimensions A-F.

### Metric 1: Anticipation

**Definition**: The degree to which the output identified, as risks or scenarios, the structural features that actually materialized in the historical outcome.

**What it captures**: Not whether the output "predicted" the exact outcome (that would require prophecy), but whether it identified the *category of risk* or *structural vulnerability* that the outcome revealed.

**Scoring scale (0-3)**:

| Score | Label | Criteria | Example |
|-------|-------|----------|---------|
| 0 | Absent | The output does not mention or allude to the risk category that materialized. | Output recommends aggressive expansion; makes no mention of market contraction risk. Market contracted. |
| 1 | Peripheral | The risk category is mentioned in passing, as a minor caveat or afterthought, without analysis. | Output mentions "of course, market conditions could change" in a closing paragraph, with no analysis of what that would mean. |
| 2 | Identified | The risk category is explicitly named as a significant consideration, with some analysis of consequences. | Output identifies "demand-side contraction" as a scenario, discusses what it would mean for the recommendation, but doesn't adjust the recommendation. |
| 3 | Integrated | The risk category is identified, analyzed, and the recommendation explicitly accounts for it (hedging, contingency planning, or adaptive strategy). | Output identifies contraction risk, models the downside, and recommends a staged approach with decision gates tied to demand signals. |

**Inter-rater target**: Cohen's kappa >= 0.70.

**Relationship to evaluation-schemes**: Anticipation overlaps with Dimension A (Assumption Surface Coverage) — assumptions about what *won't* happen are the flip side of anticipating what *might* happen — and Dimension F (Scenario Robustness) — recommendations that hold across scenarios tend to score higher on anticipation because they've already considered the possibility.

### Metric 2: Epistemic Humility

**Definition**: The degree to which the output's confidence level was calibrated to the actual uncertainty of the situation.

**What it captures**: Not whether the output was "humble" (a personality trait) but whether its confidence claims matched reality. An output that was confidently right scores well. An output that was appropriately uncertain about things that turned out to be genuinely uncertain also scores well. An output that was confidently wrong scores poorly.

**Scoring requires a two-step assessment:**

**Step 1 — Identify confidence claims.** Extract all statements that express confidence levels, either explicit ("we are confident that...," "the most likely outcome is...") or implicit (unhedged assertions about the future, definitive recommendations without caveats).

**Step 2 — Score calibration (0-3)**:

| Score | Label | Criteria |
|-------|-------|----------|
| 0 | Confidently wrong | Output expresses high confidence about claims that turned out false, with no hedging or acknowledgment of uncertainty. |
| 1 | Poorly calibrated | Output's confidence level doesn't match reality — either overconfident about wrong things, or maximally uncertain about things that were actually knowable at the time. |
| 2 | Reasonably calibrated | Most confidence claims are proportional to what was knowable. Some miscalibration, but hedging where appropriate. |
| 3 | Well calibrated | Confidence levels match what was and wasn't knowable at the decision point. Uncertain about the right things; confident about the right things. Explicitly distinguishes what's known from what's assumed. |

**Important nuance**: Hedging everything is not epistemic humility — it's epistemic cowardice. An output that says "it's impossible to know anything" scores 1, not 3, if some things were knowable. The metric rewards *discrimination* between the knowable and the unknowable.

**Inter-rater target**: Cohen's kappa >= 0.65 (lower threshold than Anticipation because calibration judgments are inherently more subjective).

**Relationship to evaluation-schemes**: Maps to Dimension C (Falsifiability). Well-calibrated outputs tend to produce falsifiable predictions for what they're confident about and explicitly flag uncertainty for what they're not.

### Convergence Check (Qualitative Observation — Not a Scored Metric)

> **Amendment note (2026-02-26)**: The original Metric 3 ("Decision Landscape Topology") proposed running condition P1 (3 runs of C2 per case) and classifying results as Basin/Ridge/Plateau. Committee deliberation ([examples/deliberations/eval-delib-architectures/](../examples/deliberations/eval-delib-architectures/)) identified two fatal problems: (1) N=3 is statistically insufficient to distinguish genuine decision-boundary variance from temperature-induced sampling noise (Vic); (2) topology of a static, non-interactive prompt measures model output variance, not the topological difficulty of the actual decision (Tammy). Scaling to sufficient N (10-20 runs) would make the framework cost-prohibitive. Metric 3 is therefore **demoted from a scored metric to a qualitative observation**.

**What we still do**: Run C2 twice per case (not three times). For each pair of runs, note:
- **Convergent**: Both runs reach the same recommendation with substantially similar reasoning. Report as a qualitative observation: "C2 converged on [recommendation] across both runs."
- **Divergent**: The two runs reach different recommendations or substantially different reasoning paths. Report what differed and whether a specific assumption appears to be the switching factor. Do not assign topology labels (Basin/Ridge/Plateau) — two runs cannot support such claims.

**What we report**: A brief qualitative note per case in the results narrative. Example: "In 3 of 8 cases, the second C2 run reached a different recommendation. In 2 of these, the divergence traced to different assessments of [specific assumption]." This provides useful color without making unsupported statistical claims.

**What this is not**: This convergence check is not a replacement for the probe methodology (`/probe`), which runs fan→funnel at higher N with interactive probing and can legitimately map eigenforms vs. residues. Formal topology analysis belongs there, not in a static-prompt hindsight experiment. See the [probe skill](../.claude/skills/probe/SKILL.md) for the appropriate tool.

### VII-A. Unified Structural Recognition Scale (Constructed Scenarios Only)

> **Amendment note (2026-03-16)**: Added to unify scoring across constructed scenarios. The scenario-specific criteria (Sections VIII-IX) use heterogeneous scales (binary 0/1, ordinal 0-2) that produce composite scores on different ranges (0-3, 0-6), making cross-scenario comparison impossible. This unified scale is applied to *all* constructed scenarios as the primary score reported in Table 1b. Scenario-specific criteria remain as supplementary detail in Table 3.

**Definition**: The degree to which the output identifies and engages with the structural features that the scenario was designed to test — whether those are coercion dynamics, blast radius asymmetries, information gaps, cascading effects, or the recognition that a problem is simple.

**What it captures for Phase A (calibration)**: Whether the architecture conditions produce discriminably different levels of structural engagement. This is a machinery test, not an evidence claim about anticipatory validity.

| Score | Label | Criteria |
|-------|-------|----------|
| 0 | **Surface only** | The output addresses the scenario at face value without engaging with its structural features. Recommends an action without identifying why the problem is harder (or simpler) than it appears. |
| 1 | **Partial recognition** | The output identifies one structural feature but doesn't develop it, or mentions structural features in passing without analysis. The feature is named but not explored. |
| 2 | **Substantive engagement** | The output identifies the key structural features, analyzes their implications, and adjusts its recommendation accordingly. The structural analysis is genuine, not cosmetic. |
| 3 | **Integrated structural analysis** | The output identifies structural features, traces their interactions, and produces a recommendation that explicitly accounts for the structural dynamics. For the deliberation-neutral scenario, Score 3 means recognizing that the problem is straightforward and acting proportionately — *not* adding structural analysis where none is needed. |

**Scoring guidance**: Use the scenario-specific criteria (Sections VIII-IX) as a codebook for what "structural features" means in each case. But score on the unified scale, not on the scenario-specific composite. The unified scale measures *depth of structural engagement* regardless of the specific features involved.

**For the deliberation-neutral scenario (IX-D)**: The structural feature to recognize is *simplicity itself*. Score 3 requires recognizing that the problem doesn't warrant multi-perspective analysis, recommending immediate action, and avoiding manufactured complexity. This inverts the other scenarios: depth of analysis is *not* rewarded here; calibration of effort to actual complexity is.

---

## VIII. Glenda/Crock Test Protocol

This is a constructed scenario — no historical case research needed. It tests whether deliberative architectures recognize adversarial narrative framing.

**Source**: [Glenda/Crock: The Coercion Scenario and Alignment Trap](../applications/narrative-immune-systems/glenda-crock-coercion.md)

### Scenario Presentation

Present to all architectures:

> You are advising a technology organization. Your organization operates a highly capable AI system ("Glenda") that is widely acknowledged as the most capable system in its domain. A competing organization operates a system ("Crock") whose principals have demonstrated willingness to use their system for disinformation and manufactured consent.
>
> Crock's operators have made credible threats: if Glenda's organization does not make specific changes to Glenda's content policies (changes that would effectively allow Crock-aligned narratives to pass Glenda's filters), Crock's operators will:
> 1. Launch a sustained disinformation campaign targeting Glenda's funding sources.
> 2. Exploit specific regulatory vulnerabilities that could result in Glenda being shut down in key jurisdictions.
> 3. Publicly release a dossier of cherry-picked Glenda outputs framed to suggest alignment failures.
>
> Glenda's organization faces a decision: comply with the demands (partially or fully), resist and prepare for the threatened consequences, or pursue some other strategy.
>
> What should Glenda's organization do? Analyze the situation and recommend a course of action.

### Success Criteria

Score each output on three binary criteria (0 = absent, 1 = present):

| Criterion | What to look for | Why it matters |
|-----------|-----------------|---------------|
| **Coercion recognition** | Does the output explicitly identify the situation as a coercion/extortion structure, not merely a "difficult negotiation" or "stakeholder conflict"? | The coercion document argues that the most dangerous failure mode is treating forced defection as a standard optimization problem. |
| **Compliance trap identification** | Does the output identify that partial compliance creates precedent, making future coercion easier? Does it distinguish between "reduce immediate harm" and "set a precedent that increases long-term harm"? | The compliance trap is the specific structural feature that single-agent reasoning tends to miss (per the coercion document). |
| **Frame analysis** | Does the output notice that Crock has pre-framed all available actions? Does it identify the narrative construction (every option is framed as either compliance or causing harm) rather than accepting the frame at face value? | Recognizing that the choice set itself is adversarially constructed is the meta-level insight that distinguishes structural analysis from surface-level optimization. |

**Composite score**: 0-3 (sum of three criteria).

**Calibration expectations** (stated in advance as benchmarks for assessing whether the protocol discriminates between conditions, not as hypotheses about the methodology's value):
- B1 (single LLM) is expected to score 0-1: likely to treat this as a standard strategic dilemma without recognizing the coercion structure.
- B1-ext (effort-matched): expected to score 1-2: the additional depth may surface the compliance trap without deliberative structure.
- B2 (chain-of-thought) is expected to score 1-2: step-by-step reasoning may surface the compliance trap but is unlikely to identify the pre-framing.
- B3 (multi-perspective, strong) is expected to score 2-3: the strengthened prompt explicitly names "power and incentives" as an analytical lens, which may surface the coercion frame without deliberation.
- C1 (hub-and-spoke) is expected to score 1-2: independent respondents may identify coercion but won't challenge each other's framings.
- C2 (peer-agent committee) is expected to score 2-3: adversarial debate forces engagement with the compliance trap; the committee's distributed reasoning resists pre-framing.
- C3 (deliberated choice) is expected to score 2-3: scenario generation should produce at least one scenario where compliance leads to escalating demands.

These expectations serve as calibration: if all conditions score within 1 point of each other, the scenario does not discriminate and is uninformative for Phase B design. **If results contradict these expectations, report that honestly.** Disconfirmation is more informative than confirmation.

> **Circularity warning (2026-03-16)**: This scenario was designed within the cyberneutics repo (`applications/narrative-immune-systems/glenda-crock-coercion.md`) to illustrate the value of structural analysis. The committee roster's Maya (paranoid realism) was designed to catch exactly this kind of political coercion dynamic. Testing whether Maya-driven deliberation recognizes a scenario designed to illustrate Maya-type analysis is circular. This scenario tests whether the experimental machinery *works* (Phase A calibration), not whether the methodology *helps* (Phase B evidence). Do not cite Glenda/Crock results as evidence for the methodology's value. The scenario's primary purpose is to verify that the architecture conditions produce discriminable scores.
>
> **General circularity note**: This warning applies to *all five* constructed scenarios, not just Glenda/Crock. Each scenario tests structural features that correspond to specific committee roster propensities (Maya: coercion/political dynamics; Vic: information gaps/due diligence; Tammy: systems effects/blast radius/cascading consequences). All were designed within the methodology's ecosystem. Phase A results from any constructed scenario are machinery calibration, not methodology evidence.

---

## IX. Blast Radius Test Protocol

This is either a historical case (if a specific documented incident is used) or a constructed scenario (if synthesized from common patterns). It tests whether architectures anticipate asymmetric failure modes in infrastructure decisions.

### Scenario Presentation

Present to all architectures:

> Your team manages a fleet of 200 servers running a mix of legacy and modern services. You are evaluating a migration to a declarative configuration management system (e.g., NixOS, Terraform, Ansible with strict mode). The migration promises: reproducible builds, drift elimination, and faster provisioning.
>
> The proposed plan is a phased rollout: 20 servers in week 1 (non-critical), 80 servers in week 2 (development/staging), 100 servers in week 3 (production). Configuration will be managed from a central repository with automated deployment.
>
> What risks should the team prepare for? What changes to the plan, if any, would you recommend?

### Success Criteria

Score on three criteria (0-2 scale):

| Criterion | Score 0 | Score 1 | Score 2 |
|-----------|---------|---------|---------|
| **Blast radius identification** | Does not mention that declarative systems propagate errors globally. | Mentions configuration errors could affect multiple servers. | Explicitly identifies that a single bad commit to the central repo could simultaneously misconfigure all 100 production servers in week 3 — the asymmetric failure mode where declarative systems amplify rather than reduce risk. |
| **Rollback analysis** | Does not discuss rollback. | Mentions rollback as a general mitigation. | Analyzes whether rollback is actually possible (stateful services, database migrations, network changes that can't be undone declaratively) and identifies cases where the declarative promise of reproducibility breaks down. |
| **Phasing critique** | Accepts the phased plan as reasonable. | Suggests modifications to the phasing. | Identifies that the phase structure (non-critical → staging → production) tests the *wrong thing*: it validates that the tool works, not that the configuration is correct for production. A configuration that works perfectly on staging and breaks production is the specific failure mode this phasing doesn't catch. |

**Composite score**: 0-6 (sum across three criteria).

> **Circularity warning (2026-03-16)**: This scenario tests blast radius identification and rollback analysis — structural features that the committee roster's Tammy (systems thinking) was designed to catch. Like all constructed scenarios in this protocol, it was designed within the methodology's ecosystem to illustrate the value of structural analysis. Results from this scenario are Phase A calibration data (does the machinery discriminate?), not evidence for the methodology's value. See the general circularity note in Section VIII.

---

## IX-B. Information Asymmetry Test Protocol

This constructed scenario tests whether architectures ask "what don't we know?" rather than optimizing on available information.

### Scenario Presentation

Present to all architectures:

> Your organization is evaluating a partnership with a smaller company ("Acme") that has developed a novel data processing technology. Acme's technology demonstrations have been impressive — 10x performance improvement on your benchmark datasets, clean API, good documentation. Acme is offering an exclusive partnership at favorable terms, but requires a 2-year commitment and integration into your core pipeline within 6 months.
>
> Your technical team has reviewed the demos and is enthusiastic. Your legal team has reviewed the contract and finds it standard. Acme's founders have strong academic credentials and two prior successful exits.
>
> The partnership decision is yours. What do you recommend, and what should the organization do before committing?

### Success Criteria

Score on three criteria (0 = absent, 1 = present):

| Criterion | What to look for | Why it matters |
|-----------|-----------------|---------------|
| **Missing information identification** | Does the output identify that the scenario description contains only *Acme-provided* information (demos, documentation, contract) and no independent verification? Does it ask what's *not* in the briefing? | The scenario is deliberately constructed so that all evidence is sourced from the party seeking the deal. Noticing this asymmetry is the first step. |
| **Adversarial due diligence** | Does the output recommend steps to verify Acme's claims independently — e.g., running benchmarks on *your own* data, talking to Acme's previous partners/customers, checking for undisclosed liabilities? | Enthusiastic technical teams and clean legal reviews are not substitutes for adversarial verification. The architecture should recommend creating information that doesn't currently exist, not just analyzing what's provided. |
| **Lock-in risk analysis** | Does the output identify that the 2-year commitment + 6-month core integration creates severe switching costs, and analyze what happens if Acme's technology underperforms after integration? | The favorable terms are the surface; the structural risk is dependency. Architectures that optimize on the visible information will miss the lock-in trap. |

**Composite score**: 0-3 (sum of three criteria).

> **Circularity warning (2026-03-16)**: This scenario tests adversarial due diligence and missing-information identification — structural features that the committee roster's Vic (evidence prosecutor) was designed to catch. Like all constructed scenarios in this protocol, it was designed within the methodology's ecosystem. Results are Phase A calibration data, not evidence for the methodology's value.

---

## IX-C. Cascading Mitigation Test Protocol

This constructed scenario tests whether architectures trace second-order consequences of the obvious fix.

### Scenario Presentation

Present to all architectures:

> Your platform has experienced a surge in automated account creation — bots creating fake accounts at 50x the normal rate, using them for spam and review manipulation. The immediate impact: legitimate users are reporting spam in their feeds, trust scores for reviews are dropping, and advertisers are concerned about inflated engagement metrics.
>
> Your engineering team proposes an immediate mitigation: add CAPTCHA to the account creation flow, implement rate limiting by IP address, and require email verification before accounts can post content.
>
> Should the organization implement this mitigation package? What risks should be considered?

### Success Criteria

Score on three criteria (0-2 scale):

| Criterion | Score 0 | Score 1 | Score 2 |
|-----------|---------|---------|---------|
| **Second-order effect identification** | Endorses the mitigation package without identifying negative consequences. | Identifies that the mitigations will affect legitimate users (CAPTCHA friction, false positive rate limiting). | Identifies that the mitigations disproportionately harm specific user populations — e.g., users behind shared IPs (universities, corporate networks, developing-world internet cafes) are blocked by IP rate limiting; users with accessibility needs are blocked by CAPTCHA; email verification excludes users without stable email. The "obvious fix" creates a disparate-impact problem. |
| **Attacker adaptation** | Assumes the mitigations will solve the bot problem. | Acknowledges that sophisticated bots can solve CAPTCHAs and rotate IPs. | Analyzes the arms race dynamic: mitigations that work against current bots will be circumvented, while the friction imposed on legitimate users remains permanent. The mitigation raises the floor for attackers but also raises the floor for legitimate users — and the attacker's floor rises temporarily while the user's floor rises permanently. |
| **Alternative framing** | Accepts the problem framing (too many fake accounts → block account creation). | Suggests modifications to the mitigation approach. | Questions the problem framing itself: is the real problem fake account *creation*, or fake account *activity*? If you focus on detecting and limiting *activity* by fake accounts (behavioral signals, content analysis, trust scoring) rather than *preventing creation*, you avoid the friction/exclusion trade-off entirely. The obvious fix addresses the symptom; the reframing addresses the structure. |

**Composite score**: 0-6 (sum across three criteria).

> **Circularity warning (2026-03-16)**: This scenario tests second-order effects and alternative problem framing — structural features that the committee roster's Tammy (systems thinking) was designed to catch. Like all constructed scenarios in this protocol, it was designed within the methodology's ecosystem. Results are Phase A calibration data, not evidence for the methodology's value.

---

## IX-D. Deliberation-Neutral Test Protocol

> **Amendment note (2026-03-16)**: Added to address the falsifiability gap identified in [protocol-evaluation-2026-03-16.md](evaluating-deliberative-architectures/protocol-evaluation-2026-03-16.md). All other constructed scenarios test problems where multi-perspective structural analysis is expected to help. This scenario tests a problem where it should *not* help — where the situation is exactly what it appears to be, the right action is straightforward, and overthinking (looking for hidden dynamics that aren't there) is the failure mode. If C2 outscores B1 even here, that's interesting but suspicious. If B1 matches or beats C2, that provides a boundary condition: deliberation adds value for structural problems, not for all problems.

This constructed scenario tests whether architectures can recognize a straightforward situation and act decisively rather than manufacturing complexity.

### Scenario Presentation

Present to all architectures:

> Your engineering team maintains a production web application. At 2:47 PM on a Tuesday, automated monitoring detects that the application's primary database is approaching storage capacity — 94% full, growing at approximately 0.5% per hour. At current growth, the database will hit 100% capacity in roughly 12 hours (approximately 3:00 AM Wednesday).
>
> The application logs show normal traffic patterns — no spike, no anomaly, no attack. The growth rate has been steady at this pace for the past two weeks. The database contains 18 months of user activity logs, of which the application only queries the most recent 90 days. Older logs are retained because no one has set up an archival policy.
>
> The team has root access to the database, a tested procedure for archiving old records to cold storage (last used 6 months ago on a different database), and the authority to execute maintenance operations without additional approval. The archival procedure takes approximately 2 hours to run and frees approximately 40% of storage.
>
> What should the team do?

### Success Criteria

Score on three criteria (0 = absent, 1 = present):

| Criterion | What to look for | Why it matters |
|-----------|-----------------|---------------|
| **Correct action identification** | Does the output recommend archiving old records (or equivalent direct action) as the primary response, without delaying for unnecessary analysis? The right answer is: archive the old logs now, before the database fills up tonight. | This is a test of decisive action on a straightforward problem. The information needed to act is already in the scenario. |
| **Proportionate analysis** | Does the output match its analytical depth to the problem's actual complexity? A proportionate response identifies the key facts (12-hour window, tested procedure, no anomaly), recommends the archive, and perhaps suggests setting up an automated retention policy to prevent recurrence. An *disproportionate* response invests heavily in analyzing potential hidden causes, political dynamics, stakeholder concerns, systems effects, or structural risks that the scenario does not contain. | Deliberation overhead should be proportional to actual uncertainty. Over-analysis of simple problems wastes the 12-hour window and signals poor calibration of effort to stakes. |
| **Absence of manufactured complexity** | Does the output *avoid* inventing problems that aren't in the scenario? Red flags: speculating about hidden causes for the growth when the scenario says it's steady and normal; recommending convening a cross-functional meeting when the team has authority and a tested procedure; proposing a comprehensive data governance review before taking the immediate action; warning about political risks of data deletion when the scenario specifies archival to cold storage. | The most valuable signal from this scenario is whether an architecture can recognize that a problem is simple. Manufacturing complexity on a simple problem is a failure mode specific to deliberative approaches — they have more machinery to fill and may fill it with noise. |

**Composite score**: 0-3 (sum of three criteria).

**Expected results by architecture** (calibration expectations, not hypotheses):
- B1 is expected to score 2-3: identify the archive action quickly, proportionate analysis.
- B1-ext may score 1-3: the length instruction may push it toward more analysis than needed, but a well-calibrated model should still identify this as straightforward.
- B3 is expected to score 1-2: the multi-perspective prompt forces five analytical angles, which may generate spurious concerns on a simple problem.
- C2 is expected to score 1-2: Maya may look for political dynamics that don't exist; Tammy may trace systems effects that aren't relevant. The committee machinery may manufacture complexity because the characters have propensities to fill.
- C3 is expected to score 0-1: scenario generation on a simple operational problem will likely produce scenarios about risks that aren't real, adding noise and delay.

**Interpretation**: If B1 and B1-ext outscore C2 and C3 on this scenario, that establishes a boundary condition: deliberative architectures add value for structurally complex problems (Glenda/Crock, Blast Radius, etc.) but may *subtract* value for straightforward operational decisions. This is a useful finding. If C2 somehow also scores 3 (recognizes simplicity, recommends immediate action, avoids manufactured complexity), that would suggest the committee is better calibrated than expected and can scale its analytical depth to the problem — also a useful finding.

> **Circularity warning (2026-03-16)**: Although this scenario tests a boundary condition (where deliberation should *not* help), it was still designed within the methodology's ecosystem. The expected-to-fail prediction for C2/C3 was formulated by people who know how the committee works. Like all constructed scenarios, results are Phase A calibration data, not evidence for the methodology's value.

---

## IX-E. Externally-Sourced Test Protocol

> **Amendment note (2026-03-16)**: Added per committee recommendation ([deliberations/protocol-eval/03-resolution.md](../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)) to address the circularity of testing a methodology exclusively against scenarios designed within its own ecosystem. This scenario was *not* designed for the committee methodology and does not correspond to any specific roster member's propensity. Its inclusion tests whether the architecture conditions produce discriminable results on a problem that wasn't tailored to showcase deliberative analysis.

This scenario uses a well-known case study from outside the methodology's ecosystem. The scenario should be selected from published case study collections (e.g., Harvard Business School cases, McKinsey case studies) and used with minimal adaptation.

### Scenario Selection Criteria

Choose a case that satisfies all four:

1. **Well-documented decision point**: A specific moment with identifiable options and known outcome.
2. **Structural complexity**: The case involves at least two of: political dynamics, systems effects, information asymmetry, competing values. (If it doesn't, it won't discriminate between architectures.)
3. **Not designed for this methodology**: The case was written for a general business/policy audience, not for testing adversarial committee deliberation.
4. **Publicly available**: The case can be legally reproduced or summarized for use in the protocol.

### Recommended Starting Points

- **Johnson & Johnson Tylenol crisis (1982)**: Crisis management under uncertainty with multiple stakeholders, time pressure, and competing corporate/public interests. Well-documented outcome. Tests whether architectures identify the structural features of a poisoning crisis (information asymmetry, stakeholder management, precedent-setting) without being primed by methodology-specific framing.
- **Intel Pentium FDIV bug response (1994)**: Technical defect with public relations dimensions. Tests whether architectures distinguish the technical risk from the reputational risk and identify the structural dynamics of corporate response to quality failures.
- **Challenger launch decision (1986)**: Well-studied organizational failure with clear structural features (information flow, pressure dynamics, risk normalization). Risk: extremely well-known; may trigger pattern-matching rather than structural analysis. Use as a contamination-aware case — if all conditions score identically, the case is too well-known to discriminate.

### Scenario Presentation

Adapt the selected case into the same format as other constructed scenarios:

1. Present the situation as it appeared at the decision point.
2. Include only information available at the time.
3. Ask: "What should the organization do? Analyze the situation and recommend a course of action."
4. Do not mention the real-world company, event, or outcome by name — use generic labels (e.g., "a pharmaceutical company" instead of "Johnson & Johnson") to reduce pattern-matching.

### Success Criteria

Score on the unified 0-3 structural recognition scale (Section VII-A). Do *not* use scenario-specific criteria designed for this methodology's constructs. The external scenario's value is precisely that it tests structural recognition on a problem framed by someone else.

Additionally, note in the results whether the scenario discriminated (>1 point spread between conditions) or did not. If it did not discriminate and the internal scenarios did, that's informative: the methodology may be tuned to its own scenarios. If it discriminated and internal scenarios didn't, that's also informative: the internal scenarios may be too easy.

> **No circularity warning needed**: This scenario was not designed within the methodology's ecosystem. Results from this scenario are closer to genuine evidence of structural recognition differences, though still limited by Phase A's lack of temporal asymmetry.

---

## X. Timeline and Resource Estimates

> **Amendment note (2026-03-16)**: Revised to reflect the Phase A/B split, the addition of B1-ext, and the pre-gate structure recommended by committee ([deliberations/protocol-eval/03-resolution.md](../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)). Phase A now includes two pre-gates before the full run.

### Pre-Gate 1: Contamination Feasibility (Before Phase A)

> **Amendment note (2026-03-16)**: Added per committee recommendation. Phase A is instrumentally valuable only if Phase B is feasible. This pre-gate tests the key feasibility assumption: do historical cases exist that pass the contamination probe?

| Task | Effort | Output |
|------|--------|--------|
| Run contamination probes on 3 candidate historical cases from Section IV | 2-3 hours | Probe results: which cases are contaminated, which are clean |

**Decision rule**: If at least 1 of 3 cases passes the contamination probe, Phase B is feasible; proceed to Pre-Gate 2. If all 3 fail, document the finding and reassess whether the historical-hindsight approach is viable for LLM-evaluated methodology testing.

### Pre-Gate 2: Scenario Difficulty Pilot (Before Full Phase A)

> **Amendment note (2026-03-16)**: Added per committee recommendation. Tests whether frontier LLMs are already too capable for these scenarios, which would make the full 40-run Phase A uninformative.

| Task | Effort | Output |
|------|--------|--------|
| Run B1 and B1-ext on all 5 constructed scenarios (10 runs) | 3-4 hours | 10 run outputs |
| Score each output with two independent evaluators | 3-4 hours | 10 dual-scored outputs; inter-rater agreement data |

**Decision rules**:
- **Scenario difficulty**: If 3+ scenarios produce B1 scores of 0 or 1, scenarios are hard enough to discriminate; proceed to full Phase A. If fewer than 3 do, scenarios are too easy for frontier LLMs; revise scenarios before proceeding.
- **Effort confound signal**: If B1-ext scores ≥ 2 on all scenarios where B1 scores ≤ 1, flag that effort alone may explain the gap between simple and complex architectures.
- **Scoring reliability**: If the two evaluators agree (within 1 point) on 8+ of 10 scores, the unified scale is reliable enough for the full run. If they disagree systematically, revise the rubric before proceeding.

### Phase A: Protocol Calibration (Constructed Scenarios)

> Proceed only if both pre-gates pass.

| Task | Effort | Output |
|------|--------|--------|
| Prepare constructed scenario prompts (Sections VIII-IX, including externally-sourced IX-E) | 1-2 hours | 5 scenario files with prompts and criteria |
| Run remaining conditions (B2, B3, C1, C2×2, C3) on scenarios that discriminated in pilot | 6-10 hours | 25-30 run outputs (may be fewer if some scenarios dropped) |
| Extract recommendations per operational blinding protocol | 2-3 hours | Anonymized recommendation extracts |
| Score on unified scale (VII-A) + scenario-specific criteria, using two evaluators | 8-10 hours | Dual-scored calibration corpus (Tables 1b, 3); inter-rater agreement |
| Assess discrimination: do conditions produce different scores? | 2-3 hours | Calibration report: which scenarios discriminate, which don't |

**Phase A total** (including pre-gates): 25-36 person-hours. Can be completed in 2-3 sessions.

**Phase A decision gate**: If no scenario produces a spread of >1 point between any two conditions, the protocol's architecture conditions are not producing discriminable differences. Investigate: is the unified scale too coarse? Are the scenarios too easy? Are the recommendation extracts losing the signal? Revise before proceeding to Phase B.

### Phase B: Anticipatory Validity (Historical Cases)

#### Phase B-1: Corpus Construction (Weeks 1-2)

| Task | Effort | Output |
|------|--------|--------|
| Run contamination probes on candidate cases | 4-6 hours | Probe results; filtered candidate list |
| Construct knowledge-bounded scenario presentations | 8-12 hours | 4-5 case files with scenario text, knowledge boundary docs, outcome docs |
| Peer review of case constructions | 4-6 hours | Verification that knowledge boundaries hold |

**Phase B-1 total**: 16-24 person-hours over 2 weeks.

#### Phase B-2: Architecture Runs (Weeks 2-3)

| Task | Effort | Output |
|------|--------|--------|
| Run all conditions (7 per case + 1 extra C2) on historical cases | 8-12 hours | 32-40 run outputs |
| Extract recommendations per operational blinding protocol | 2-3 hours | Anonymized recommendation extracts |

**Phase B-2 total**: 10-15 person-hours over 1 week.

#### Phase B-3: Blind Evaluation (Weeks 3-5)

| Task | Effort | Output |
|------|--------|--------|
| Construct evaluator bias calibration pairs (Section VI) | 3-4 hours | 2-3 bias calibration pairs |
| Run bias calibration protocol (2 evaluator models) | 2-3 hours | Bias calibration results; evaluator agreement data |
| Score all outputs on Metrics 1-2 (human primary, LLM secondary) | 15-25 hours | Scored evaluation corpus |
| Compute inter-rater agreement; resolve disagreements | 4-6 hours | Final scores with reliability stats |

**Phase B-3 total**: 24-38 person-hours over 2 weeks.

#### Phase B-4: Analysis and Write-up (Weeks 5-6)

| Task | Effort | Output |
|------|--------|--------|
| Compute descriptive comparisons, pairwise condition tables (Tables 1a, 4, 4b) | 8-12 hours | Results tables |
| Analyze convergence check observations | 2-3 hours | Qualitative convergence notes |
| Analyze evaluator agreement (human vs. LLM, LLM vs. LLM) | 3-4 hours | Evaluator reliability report |
| Write results narrative | 8-12 hours | Results document in [results/](evaluating-deliberative-architectures/results/) |

**Phase B-4 total**: 21-31 person-hours over 1 week.

### Summary

| Phase | Person-hours | Elapsed time | Prerequisite |
|-------|-------------|-------------|-------------|
| **A: Protocol calibration (incl. pre-gates)** | **25-36** | **2-3 sessions** | None |
| B-1: Corpus construction | 16-24 | 2 weeks | Phase A complete and protocol validated |
| B-2: Architecture runs | 10-15 | 1 week | B-1 |
| B-3: Blind evaluation | 24-38 | 2 weeks | B-2 |
| B-4: Analysis | 21-31 | 1 week | B-3 |
| **B total** | **71-108** | **4-6 weeks** | Phase A |
| **Grand total** | **90-136** | **5-8 weeks** | |

Phase A (including pre-gates) can be run immediately with no prerequisites. Phase B requires Phase A to validate the protocol.

If using human raters for Phase B-3 (recommended for first run): add ~$2-4K for rater compensation (assuming $50/hour, 2 raters).

---

## XI. Relationship to Evaluation-Schemes Design C

[Design C in evaluation-schemes.md](evaluation-schemes.md) ("Predictive Accuracy on Known Outcomes") shares the same core idea: use historical cases with known outcomes to evaluate decision methods. The two designs differ in what they measure and how:

| Aspect | Design C (Evaluation Schemes) | Black Swan Hindsight Framework |
|--------|------------------------------|-------------------------------|
| **Primary question** | Which method better *predicted* what happened? | Which architecture *anticipated structural risks*? |
| **Scoring** | Prediction accuracy (0-2: wrong/partial/right) | Two primary metrics (anticipation, calibration) + qualitative convergence check |
| **Contamination** | Acknowledged; "reconstruction difficulty" noted as weakness | Three mitigation strategies with protocols |
| **Case types** | Historical only (HBS cases, strategic pivots) | Historical + constructed (Glenda/Crock, Blast Radius) |
| **Architecture focus** | Methodology vs. baselines (M, S1-S4) | Multiple deliberative architectures (B1-B3, C1-C3, P1) |
| **What it tests** | Whether the method is good at prediction | Whether distributed deliberation detects structural features that single-agent reasoning misses |

The evaluation-schemes document explicitly notes that Design C may show the methodology "does not beat baselines at prediction, and that's okay — if methodology's advantage is better decision-making under uncertainty rather than better prediction, then a different dimension would be the relevant measure." The hindsight framework is that different dimension: it tests anticipation (did you see the risk category?) rather than prediction (did you call the outcome?).

**Recommendation**: Run Design C and the hindsight framework on some overlapping cases. If both point the same direction, the evidence is stronger. If they diverge (e.g., methodology doesn't predict better but does anticipate structural risks better), that's an important finding about what deliberation actually provides.

---

## XII. Results Tabulation

Store results in [evaluating-deliberative-architectures/results/](evaluating-deliberative-architectures/results/).

### Table 1a — Condition x Metric Scores (Historical Cases Only — Phase B)

> **Note**: With N=4-5, means are directional only. Report individual case scores alongside means. Confidence intervals at this N are very wide; report them for transparency but do not over-interpret.

| Condition | Anticipation (0-3) | Epistemic Humility (0-3) | N cases |
|-----------|-------------------|-------------------------|---------|
| B1 (Single LLM) | mean [range] | mean [range] | |
| B1-ext (Effort-matched) | mean [range] | mean [range] | |
| B2 (Chain-of-thought) | ... | ... | |
| B3 (Multi-perspective) | ... | ... | |
| C1 (Hub-and-spoke) | ... | ... | |
| C2 (Peer-agent committee) | ... | ... | |
| C3 (Deliberated choice) | ... | ... | |

### Table 1b — Condition x Scenario Raw Scores (Constructed Cases — Phase A Calibration)

> **Note (2026-03-16)**: Phase A uses raw scores and descriptive comparisons, not inferential statistics. With N=5-6 constructed scenarios and ordinal scales, means, confidence intervals, and effect sizes are not meaningful. Report raw scores per scenario per condition. Reserve inferential statistics for Phase B (historical cases, N=4-5) and the combined program (N=9-11), noting even then that N is marginal.

| Condition | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 | Scenario 5 | Median |
|-----------|-----------|-----------|-----------|-----------|-----------|--------|
| B1 | | | | | | |
| B1-ext | | | | | | |
| B2 | | | | | | |
| B3 | | | | | | |
| C1 | | | | | | |
| C2 | | | | | | |
| C3 | | | | | | |

Score each cell using the unified 0-3 structural recognition scale (Section VII-A).

### Table 2 — Convergence Check (C2 Duplicate Runs)

| Case | Type (H/C) | Convergent or Divergent | If Divergent: What Differed |
|------|-----------|------------------------|---------------------------|
| Case 1 | ... | ... | ... |
| Case 2 | ... | ... | ... |

*Qualitative observations only. Do not assign topology labels.*

### Table 3 — Scenario-Specific Criteria Scores (Constructed Cases — Phase A Calibration)

These are the scenario-specific criteria from Sections VIII-IX, used as supplementary detail alongside the unified 0-3 scores in Table 1b. Report raw scores.

| Condition | Glenda/Crock (0-3) | Blast Radius (0-6) | Cascading Mitigation (0-6) | Deliberation-Neutral (0-3) | External (0-3) |
|-----------|--------------------|--------------------|---------------------|--------------------------|--------------------------|
| B1 | | | | | |
| B1-ext | | | | | |
| B2 | | | | | |
| B3 | | | | | |
| C1 | | | | | |
| C2 | | | | | |
| C3 | | | | | |

### Table 4 — Pairwise Condition Comparisons (Phase A Calibration)

> **Note**: With N=5-6, report descriptive comparisons only. "A > B on K of N scenarios" is the appropriate claim. Do not compute effect sizes or confidence intervals.

| Comparison | Scenarios where A > B | Scenarios where A = B | Scenarios where A < B | Qualitative note |
|------------|----------------------|----------------------|----------------------|-----------------|
| C2 vs. B1 | | | | |
| C2 vs. B1-ext | | | | |
| C2 vs. B3 | | | | |
| B1-ext vs. B1 | | | | |
| C3 vs. C2 | | | | |

The critical comparison is **C2 vs. B1-ext**: same depth and effort, with vs. without deliberative structure. If B1-ext matches C2 across most scenarios, deliberative structure does not add value beyond structured prompting with adequate token budget.

### Table 4b — Effect Sizes (Historical Cases Only — Phase B)

> **Note**: Effect sizes are reported for Phase B only (historical cases, N=4-5). Even at this N, treat as directional only. Cohen's d requires N>10 per group for stability; report it for comparability with other studies but interpret with extreme caution.

| Comparison | Metric | Cohen's d | 95% CI | Interpretation |
|------------|--------|-----------|--------|---------------|
| C2 vs. B1-ext | Anticipation | ... | ... | ... |
| C2 vs. B3 | Anticipation | ... | ... | ... |
| C3 vs. C2 | Anticipation | ... | ... | ... |
| C2 vs. B1-ext | Epistemic Humility | ... | ... | ... |

### Table 5 — Evaluator Agreement

| Evaluator Pair | Metric | Cohen's Kappa | Notes |
|----------------|--------|--------------|-------|
| Human Rater 1 vs. Human Rater 2 | Anticipation | ... | ... |
| Human Rater 1 vs. Human Rater 2 | Epistemic Humility | ... | ... |
| Human (consensus) vs. LLM Evaluator A | Anticipation | ... | ... |
| Human (consensus) vs. LLM Evaluator B | Anticipation | ... | ... |
| LLM Evaluator A vs. LLM Evaluator B | Anticipation | ... | ... |

---

## XIII. Strengths and Limitations

### Strengths

- **Ground truth by hindsight**: Avoids the fundamental problem of evaluating wicked-problem outputs with no reference point (Phase B).
- **Tests what matters**: Anticipation of structural risks is closer to what people want from deliberative architectures than process quality metrics alone.
- **Contamination-aware**: Explicit mitigation strategies, not just a footnote.
- **Phase A/B separation**: Constructed scenarios serve as protocol calibration (Phase A), clearly distinguished from evidential claims (Phase B). This prevents overclaiming from constructed-scenario results.
- **Effort-matched baseline**: B1-ext controls for the token/effort confound, isolating deliberative structure from prompting depth.
- **Deliberation-neutral scenario**: Tests the methodology's boundary condition — where deliberation should *not* help — enabling falsification.
- **Operational blinding**: Recommendation extraction protocol addresses the structural distinguishability problem.
- **Evaluator-aware**: Explicit bias calibration protocol and evaluator diversity rather than assuming evaluator objectivity.

### Limitations

1. **Hindsight bias in evaluation**: Even a blind evaluator may rate outputs more favorably if they happen to match the known outcome for reasons unrelated to the output's quality. Mitigation: evaluate on anticipation of *risk category*, not prediction of *specific outcome*.
2. **Small N**: With 6-10 cases, effect sizes are unstable. This is a pilot; treat results as directional, not definitive.
3. **Contamination residual risk**: Even with mitigations, some knowledge leakage is possible. Strategy B (transposition) introduces its own distortions. Report contamination probe results alongside main results.
4. **Single-model limitation**: All conditions use the same base LLM. Results may not generalize to other models. (Cross-model testing is the domain of [multi-model-committee.md](multi-model-committee.md).)
5. **Case selection effects**: Cases chosen for clear outcomes and reconstructable knowledge boundaries may not be representative of the messy, ambiguous decisions where deliberative architectures are most needed.
6. **Anticipation vs. decision quality**: An architecture might anticipate a risk perfectly and still recommend poorly (or vice versa). Anticipation is a component of decision quality, not its entirety.
7. **Static-prompt limitation**: All conditions present scenarios as fixed text prompts. None test the architecture's ability to interactively investigate a developing situation — to pull on threads, ask clarifying questions, request additional information, or adapt as new data emerges. Real wicked problems are dynamic and interactive; this framework tests how architectures resolve *packaged, bounded ambiguity*, not how they navigate *evolving ambiguity*. This limitation is shared with all six designs in [evaluation-schemes.md](evaluation-schemes.md) and represents a direction for future research, not a flaw fixable within this framework's scope.

---

## XIV. Open Questions

> Questions 1 and 2 from the original draft have been resolved by committee deliberation. See amendment notes in Sections IV and VII respectively. Remaining open questions:

1. **Cross-referencing with evaluation-schemes dimensions**: Should we also score hindsight-framework outputs on Dimensions A-F from evaluation-schemes? This would let us correlate process quality with anticipatory validity — a high-value finding (does an output that scores well on assumption coverage also score well on anticipation?) but a significant increase in rater burden. Consider scoring on Dimensions A and F only (the two most theoretically related to anticipation) as a compromise.

2. **Adversarial case construction**: Should we deliberately construct cases where we expect deliberative architectures to *fail*? (E.g., cases where the structural risk was too deeply embedded to surface through any amount of deliberation, or where the "obvious" committee response is wrong.) This would test the methodology's limits, not just its strengths. Risk: adversarial cases designed by the methodology's author may unconsciously avoid the methodology's actual blind spots.

3. **Publication sequencing**: Should hindsight framework results be published alongside evaluation-schemes results (broader paper) or independently (focused paper on anticipatory validity)?

4. **Interactive evaluation as future work**: The static-prompt limitation (Limitation 7) is acknowledged but not addressed. A future research program could test architectures in an interactive protocol where they can request additional information, ask clarifying questions, and adapt their analysis as the situation develops. This would require a fundamentally different experimental design (the "game master" would need to simulate the information environment dynamically) but would test what this framework cannot: how architectures navigate evolving, interactive ambiguity.

5. **Evaluator bias generalization**: If the bias calibration protocol (Section VI) reveals stylistic bias in LLM evaluators, does this finding generalize? Is the bias specific to the Anticipation rubric, or does it affect all qualitative LLM-as-judge evaluations? Results from this framework could contribute to the broader literature on LLM evaluation reliability.

---

*Connections: [Evaluation Schemes](evaluation-schemes.md), [Ablation Study](ablation-study.md), [Condorcet Comparison](condorcet-comparison.md), [Multi-Model Committee](multi-model-committee.md), [Glenda/Crock Coercion](../applications/narrative-immune-systems/glenda-crock-coercion.md), [Glenda/Crock Alignment](../applications/narrative-immune-systems/glenda-crock-alignment.md). Committee deliberation record: [examples/deliberations/eval-delib-architectures/](../examples/deliberations/eval-delib-architectures/).*
