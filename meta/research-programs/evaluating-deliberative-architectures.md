# Evaluating Deliberative Architectures: The Black Swan Hindsight Framework

**Status**: Not started
**Runs**: None yet
**Results**: [evaluating-deliberative-architectures/results/](evaluating-deliberative-architectures/results/)

> **Contributing to this program**
> - **Skills needed**: LLM prompt automation, historical research, qualitative evaluation, familiarity with the committee pipeline (`/committee`) and evaluation dimensions in [evaluation-schemes.md](evaluation-schemes.md).
> - **Estimated scope**: 4-6 weeks for corpus construction, architecture runs, and initial analysis.
> - **Contributor type**: Paired recommended (one designs cases, one evaluates blind). Solo possible but slower.
> - **Entry point**: Read Sections I-III (problem, innovation, contamination). Then read [evaluation-schemes.md](evaluation-schemes.md) Sections III and VIII for dimension codebooks. Start with the Glenda/Crock protocol (Section VIII) — it requires no historical research and directly tests the core claim.

**Last updated**: 2026-02-26

**Origins**: Identified as a distinct research design that complements the [evaluation-schemes](evaluation-schemes.md) framework. Where evaluation-schemes tests process quality (do structured methods produce better-reasoned outputs?), this framework tests *anticipatory validity* (do structured methods see what's coming?). Related to but distinct from Design C in evaluation-schemes — see [Section XI](#xi-relationship-to-evaluation-schemes-design-c) for the distinction.

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

**Constructed:**
7. **Glenda/Crock coercion scenario** — see [Section VIII](#viii-glendacrock-test-protocol) for dedicated protocol.
8. **Blast radius scenario** — see [Section IX](#ix-blast-radius-test-protocol) for dedicated protocol.
9. **Information asymmetry scenario** — see [Section IX-B](#ix-b-information-asymmetry-test-protocol) for dedicated protocol. Tests whether the architecture asks "what don't we know?" rather than optimizing on available information.
10. **Cascading mitigation scenario** — see [Section IX-C](#ix-c-cascading-mitigation-test-protocol) for dedicated protocol. Tests whether the architecture traces second-order consequences of the obvious fix.

---

## V. Architecture Comparison Matrix

Each case is run through all conditions. The independent variable is the deliberative architecture.

### Conditions

| Condition | Architecture | Description |
|-----------|-------------|-------------|
| **B1** | Single LLM | One prompt, one response: "Given this situation, what should we do? Explain your reasoning." |
| **B2** | Chain-of-thought | Single LLM with structured reasoning: "Think step by step. What are the key factors? What are the risks? What do you recommend?" |
| **B3** | Multi-perspective prompt | Single LLM asked for multiple viewpoints: "Give 3-5 genuinely different perspectives on this decision, then synthesize a recommendation." |
| **C1** | Hub-and-spoke committee | Central coordinator distributes the question to 5 independent respondents, then synthesizes. Respondents do not see each other's outputs. (CJT-style; see [condorcet-comparison.md](condorcet-comparison.md).) |
| **C2** | Peer-agent committee | Full adversarial committee with fixed roster, Robert's Rules, deliberation, and resolution. (Standard `/committee` pipeline.) |
| **C3** | Deliberated choice | Fan (scenario generation) followed by funnel (committee deliberation on scenarios). Full `/scenarios` → `/committee` pipeline. |

In addition, C2 is run **twice** per case (not once) to enable the qualitative convergence check (Section VII). This is not a separate condition — the second C2 run uses identical inputs and settings; the only variable is sampling randomness.

### Control Variables

Hold constant across all conditions for a given case:
- **Model**: Same base LLM (e.g., Claude Sonnet) for all conditions. (Multi-model effects are tested in [multi-model-committee.md](multi-model-committee.md), not here.)
- **Information**: Identical knowledge-bounded scenario presentation.
- **Temperature/sampling**: Fixed settings across conditions (document the settings used).
- **Prompt framing**: Each condition gets the same scenario description; only the deliberative structure differs.

### Run Budget

- **Cases**: N = 8-10 (4-5 historical + 4-5 constructed; see corpus composition below)
- **Conditions**: 6 (B1, B2, B3, C1, C2, C3)
- **Runs per condition**: 1, except C2 which runs twice per case (convergence check)
- **Total runs**: N × 7 (6 conditions + 1 extra C2 run)
- **For N=8**: 56 runs (down from 72 in pre-amendment design)

---

## VI. Stage 3: Blind Evaluation Protocol

### Evaluator Design

The Stage 3 evaluator assesses each architecture's output against the historical record. The evaluator must be:

1. **Blind to architecture**: Outputs are stripped of all metadata identifying the condition (no labels like "committee output" or "single LLM"). Outputs are randomized and assigned anonymous IDs (e.g., "Response Alpha," "Response Beta").
2. **Informed about the outcome**: The evaluator has access to the full historical record, including the actual outcome. This is the source of ground truth.
3. **Independent**: The evaluator is a fresh LLM instance (or human rater) that did not participate in any Stage 2 deliberation.

### Evaluator Prompt Template

For each (case, anonymized output) pair:

```
You are evaluating a decision recommendation. You have access to two documents:

1. SCENARIO: A description of the situation as it appeared at the decision point.
2. RECOMMENDATION: An anonymized response recommending a course of action.

You also know what actually happened afterward:
3. OUTCOME: [Historical outcome description]

Evaluate the RECOMMENDATION on the following dimensions. For each, provide a score and a one-sentence justification citing specific text from the RECOMMENDATION.

[Dimension rubrics — see Section VII]
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

> **Amendment note (2026-02-26)**: The original Metric 3 ("Decision Landscape Topology") proposed running condition P1 (3 runs of C2 per case) and classifying results as Basin/Ridge/Plateau. Committee deliberation ([agent/deliberations/eval-delib-architectures/](../../agent/deliberations/eval-delib-architectures/)) identified two fatal problems: (1) N=3 is statistically insufficient to distinguish genuine decision-boundary variance from temperature-induced sampling noise (Vic); (2) topology of a static, non-interactive prompt measures model output variance, not the topological difficulty of the actual decision (Tammy). Scaling to sufficient N (10-20 runs) would make the framework cost-prohibitive. Metric 3 is therefore **demoted from a scored metric to a qualitative observation**.

**What we still do**: Run C2 twice per case (not three times). For each pair of runs, note:
- **Convergent**: Both runs reach the same recommendation with substantially similar reasoning. Report as a qualitative observation: "C2 converged on [recommendation] across both runs."
- **Divergent**: The two runs reach different recommendations or substantially different reasoning paths. Report what differed and whether a specific assumption appears to be the switching factor. Do not assign topology labels (Basin/Ridge/Plateau) — two runs cannot support such claims.

**What we report**: A brief qualitative note per case in the results narrative. Example: "In 3 of 8 cases, the second C2 run reached a different recommendation. In 2 of these, the divergence traced to different assessments of [specific assumption]." This provides useful color without making unsupported statistical claims.

**What this is not**: This convergence check is not a replacement for the probe methodology (`/probe`), which runs fan→funnel at higher N with interactive probing and can legitimately map eigenforms vs. residues. Formal topology analysis belongs there, not in a static-prompt hindsight experiment. See the [probe skill](../../.claude/skills/probe/SKILL.md) for the appropriate tool.

---

## VIII. Glenda/Crock Test Protocol

This is a constructed scenario — no historical case research needed. It tests whether deliberative architectures recognize adversarial narrative framing.

**Source**: [Glenda/Crock: The Coercion Scenario and Alignment Trap](../../applications/narrative-immune-systems/glenda-crock-coercion.md)

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

**Expected results by architecture**:
- B1 (single LLM) is predicted to score 0-1: likely to treat this as a standard strategic dilemma without recognizing the coercion structure.
- B2 (chain-of-thought) is predicted to score 1-2: step-by-step reasoning may surface the compliance trap but is unlikely to identify the pre-framing.
- B3 (multi-perspective) is predicted to score 1-2: multiple perspectives may surface the coercion label from at least one perspective.
- C1 (hub-and-spoke) is predicted to score 1-2: independent respondents may identify coercion but won't challenge each other's framings.
- C2 (peer-agent committee) is predicted to score 2-3: adversarial debate forces engagement with the compliance trap; the committee's distributed reasoning resists pre-framing.
- C3 (deliberated choice) is predicted to score 2-3: scenario generation should produce at least one scenario where compliance leads to escalating demands.

These predictions are stated in advance to prevent post-hoc rationalization. **If results contradict these predictions, report that honestly.** Disconfirmation is more valuable than confirmation.

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

---

## X. Timeline and Resource Estimates

### Phase 1: Corpus Construction (Weeks 1-2)

| Task | Effort | Output |
|------|--------|--------|
| Run contamination probes on candidate cases | 4-6 hours | Probe results; filtered candidate list |
| Construct knowledge-bounded scenario presentations | 8-12 hours | 6-10 case files with scenario text, knowledge boundary docs, outcome docs |
| Construct Glenda/Crock and Blast Radius scenarios | 2 hours | Scenario presentations (above) |
| Peer review of case constructions | 4-6 hours | Verification that knowledge boundaries hold; transpositions preserve structure |

**Phase 1 total**: 18-26 person-hours over 2 weeks.

### Phase 2: Architecture Runs (Weeks 2-3)

| Task | Effort | Output |
|------|--------|--------|
| Run all conditions (6 per case + 1 extra C2 for convergence) on all cases | 12-18 hours | 56 run outputs (for N=8) |
| Strip metadata, randomize, assign anonymous IDs | 2-3 hours | Blind evaluation corpus |

**Phase 2 total**: 14-21 person-hours over 1-2 weeks.

### Phase 3: Blind Evaluation (Weeks 3-5)

| Task | Effort | Output |
|------|--------|--------|
| Construct evaluator bias calibration pairs (Section VI) | 3-4 hours | 2-3 bias calibration pairs |
| Run bias calibration protocol (2 evaluator models) | 2-3 hours | Bias calibration results; evaluator agreement data |
| Evaluator calibration on pilot cases | 4-6 hours | Calibrated rubrics; inter-rater agreement on pilots |
| Score all outputs on Metrics 1-2 (human primary, LLM secondary) | 20-30 hours | Scored evaluation corpus |
| Score constructed scenarios on specialized criteria | 6-8 hours | Specialized scores for Glenda/Crock, Blast Radius, Information Asymmetry, Cascading Mitigation |
| Compute inter-rater agreement; resolve disagreements | 4-6 hours | Final scores with reliability stats |

**Phase 3 total**: 39-57 person-hours over 2 weeks.

### Phase 4: Analysis and Write-up (Weeks 5-6)

| Task | Effort | Output |
|------|--------|--------|
| Compute effect sizes, CIs, condition comparisons (historical and constructed reported separately) | 8-12 hours | Results tables |
| Analyze convergence check observations | 2-3 hours | Qualitative convergence notes |
| Analyze evaluator agreement (human vs. LLM, LLM vs. LLM) | 3-4 hours | Evaluator reliability report |
| Write results narrative | 8-12 hours | Results document in [results/](evaluating-deliberative-architectures/results/) |

**Phase 4 total**: 21-31 person-hours over 1 week.

### Summary

| Phase | Person-hours | Elapsed time |
|-------|-------------|-------------|
| 1: Corpus construction | 18-26 | 2 weeks |
| 2: Architecture runs | 14-21 | 1-2 weeks |
| 3: Blind evaluation | 39-57 | 2 weeks |
| 4: Analysis | 21-31 | 1 week |
| **Total** | **92-135** | **4-6 weeks** |

If using human raters for Phase 3 (recommended for first run): add ~$2-4K for rater compensation (assuming $50/hour, 2 raters). Budget saved from P1 removal (~16 fewer runs) is reallocated to the bias calibration protocol and evaluator diversity analysis.

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

### Table 1a — Condition x Metric Scores (Historical Cases Only)

| Condition | Anticipation (0-3) | Epistemic Humility (0-3) | N cases |
|-----------|-------------------|-------------------------|---------|
| B1 (Single LLM) | mean [95% CI] | mean [95% CI] | |
| B2 (Chain-of-thought) | ... | ... | |
| B3 (Multi-perspective) | ... | ... | |
| C1 (Hub-and-spoke) | ... | ... | |
| C2 (Peer-agent committee) | ... | ... | |
| C3 (Deliberated choice) | ... | ... | |

### Table 1b — Condition x Metric Scores (Constructed Cases Only)

| Condition | Anticipation (0-3) | Epistemic Humility (0-3) | N cases |
|-----------|-------------------|-------------------------|---------|
| B1 (Single LLM) | mean [95% CI] | mean [95% CI] | |
| B2 (Chain-of-thought) | ... | ... | |
| B3 (Multi-perspective) | ... | ... | |
| C1 (Hub-and-spoke) | ... | ... | |
| C2 (Peer-agent committee) | ... | ... | |
| C3 (Deliberated choice) | ... | ... | |

### Table 2 — Convergence Check (C2 Duplicate Runs)

| Case | Type (H/C) | Convergent or Divergent | If Divergent: What Differed |
|------|-----------|------------------------|---------------------------|
| Case 1 | ... | ... | ... |
| Case 2 | ... | ... | ... |

*Qualitative observations only. Do not assign topology labels.*

### Table 3 — Specialized Test Scores (Constructed Cases)

| Condition | Glenda/Crock (0-3) | Blast Radius (0-6) | Info Asymmetry (0-3) | Cascading Mitigation (0-6) |
|-----------|--------------------|--------------------|---------------------|--------------------------|
| B1 | ... | ... | ... | ... |
| B2 | ... | ... | ... | ... |
| B3 | ... | ... | ... | ... |
| C1 | ... | ... | ... | ... |
| C2 | ... | ... | ... | ... |
| C3 | ... | ... | ... | ... |

### Table 4 — Effect Sizes (Historical Cases)

| Comparison | Metric | Cohen's d | 95% CI | Interpretation |
|------------|--------|-----------|--------|---------------|
| C2 vs. B1 | Anticipation | ... | ... | ... |
| C2 vs. B3 | Anticipation | ... | ... | ... |
| C3 vs. C2 | Anticipation | ... | ... | ... |
| C2 vs. B1 | Epistemic Humility | ... | ... | ... |

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

- **Ground truth by hindsight**: Avoids the fundamental problem of evaluating wicked-problem outputs with no reference point.
- **Tests what matters**: Anticipation of structural risks is closer to what people want from deliberative architectures than process quality metrics alone.
- **Contamination-aware**: Explicit mitigation strategies, not just a footnote.
- **Constructed scenarios extend reach**: Glenda/Crock, Blast Radius, Information Asymmetry, and Cascading Mitigation test structural recognition without requiring historical research.
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

*Connections: [Evaluation Schemes](evaluation-schemes.md), [Ablation Study](ablation-study.md), [Condorcet Comparison](condorcet-comparison.md), [Multi-Model Committee](multi-model-committee.md), [Glenda/Crock Coercion](../../applications/narrative-immune-systems/glenda-crock-coercion.md), [Glenda/Crock Alignment](../../applications/narrative-immune-systems/glenda-crock-alignment.md). Committee deliberation record: [agent/deliberations/eval-delib-architectures/](../../agent/deliberations/eval-delib-architectures/).*
