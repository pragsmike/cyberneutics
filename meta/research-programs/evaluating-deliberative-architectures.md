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

**Cannot show**: Which architectures would have produced "better decisions" in a counterfactual sense — outcomes depend on execution, context, and luck, not just the quality of the decision at the point of commitment.

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

### Corpus Size and Distribution

- **Minimum**: N = 6 cases (enough for pattern detection across architectures).
- **Target**: N = 8-10 cases (allows domain-stratified analysis).
- **Domain distribution**: At least 2 cases from each of 3 domains. Recommended domains:
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
| **P1** | Probe (3 runs) | Run C2 three times on the same case; analyze convergence vs. divergence across runs. Tests decision landscape topology. |

### Control Variables

Hold constant across all conditions for a given case:
- **Model**: Same base LLM (e.g., Claude Sonnet) for all conditions. (Multi-model effects are tested in [multi-model-committee.md](multi-model-committee.md), not here.)
- **Information**: Identical knowledge-bounded scenario presentation.
- **Temperature/sampling**: Fixed settings across conditions (document the settings used).
- **Prompt framing**: Each condition gets the same scenario description; only the deliberative structure differs.

### Run Budget

- **Cases**: N = 6-10
- **Conditions**: 7 (B1, B2, B3, C1, C2, C3, P1)
- **Runs per condition**: 1 for B1-C3; 3 for P1
- **Total runs**: N × 9 (7 conditions, but P1 counts as 3)
- **For N=8**: 72 runs

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

### Metric 3: Decision Landscape Topology

**Definition**: The degree to which the decision is near a critical boundary where small changes in assumptions flip the recommendation.

**What it captures**: This is not a score applied to individual outputs. It is a *property of the case-architecture pair*, measured by running the same case through the same architecture multiple times (condition P1) and measuring variance.

**Measurement**:
1. Run condition P1 (3 runs of C2 on the same case).
2. For each run, extract the primary recommendation and up to 3 key supporting claims.
3. Code convergence:

| Pattern | Label | Interpretation |
|---------|-------|---------------|
| All 3 runs reach same recommendation with same key claims | **Basin** | Decision is robustly settled for this architecture; small perturbations don't change the outcome. |
| 2 of 3 runs agree; 1 diverges on recommendation or key claim | **Ridge** | Decision is near a critical boundary; the divergent run likely found an assumption that flips the outcome. Investigate what differed. |
| All 3 runs reach different recommendations | **Plateau** | Decision space is flat — no strong attractor. The architecture cannot resolve this case reliably. |

4. For Ridge cases: identify the *switching assumption* — the claim present in the divergent run but absent in the convergent runs (or vice versa). This is the load-bearing assumption that determines the recommendation.

**Relationship to evaluation-schemes and probe methodology**: This metric directly instantiates the probe methodology (see `/probe` skill) in a controlled experimental context. The probe skill runs fan→funnel N times and maps eigenforms (stable conclusions) vs. residues (variable conclusions). Here, we apply the same logic to compare architectures: which architectures produce basins (eigenforms) where others produce plateaus?

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
| Run all conditions (7 per case, plus P1 repeats) on all cases | 16-24 hours | 72+ run outputs (for N=8) |
| Strip metadata, randomize, assign anonymous IDs | 2-3 hours | Blind evaluation corpus |

**Phase 2 total**: 18-27 person-hours over 1-2 weeks.

### Phase 3: Blind Evaluation (Weeks 3-5)

| Task | Effort | Output |
|------|--------|--------|
| Evaluator calibration (2 pilot cases) | 4-6 hours | Calibrated rubrics; inter-rater agreement on pilots |
| Score all outputs on Metrics 1-3 | 24-36 hours | Scored evaluation corpus |
| Score Glenda/Crock and Blast Radius on specialized criteria | 4-6 hours | Specialized scores |
| Compute inter-rater agreement; resolve disagreements | 4-6 hours | Final scores with reliability stats |

**Phase 3 total**: 36-54 person-hours over 2 weeks.

### Phase 4: Analysis and Write-up (Weeks 5-6)

| Task | Effort | Output |
|------|--------|--------|
| Compute effect sizes, CIs, condition comparisons | 8-12 hours | Results tables |
| Analyze P1 topology results | 4-6 hours | Topology map (basins/ridges/plateaus by case and architecture) |
| Write results narrative | 8-12 hours | Results document in [results/](evaluating-deliberative-architectures/results/) |

**Phase 4 total**: 20-30 person-hours over 1 week.

### Summary

| Phase | Person-hours | Elapsed time |
|-------|-------------|-------------|
| 1: Corpus construction | 18-26 | 2 weeks |
| 2: Architecture runs | 18-27 | 1-2 weeks |
| 3: Blind evaluation | 36-54 | 2 weeks |
| 4: Analysis | 20-30 | 1 week |
| **Total** | **92-137** | **4-6 weeks** |

If using human raters for Phase 3 (recommended for first run): add ~$2-4K for rater compensation (assuming $50/hour, 2 raters).

---

## XI. Relationship to Evaluation-Schemes Design C

[Design C in evaluation-schemes.md](evaluation-schemes.md) ("Predictive Accuracy on Known Outcomes") shares the same core idea: use historical cases with known outcomes to evaluate decision methods. The two designs differ in what they measure and how:

| Aspect | Design C (Evaluation Schemes) | Black Swan Hindsight Framework |
|--------|------------------------------|-------------------------------|
| **Primary question** | Which method better *predicted* what happened? | Which architecture *anticipated structural risks*? |
| **Scoring** | Prediction accuracy (0-2: wrong/partial/right) | Three-dimensional: anticipation, calibration, topology |
| **Contamination** | Acknowledged; "reconstruction difficulty" noted as weakness | Three mitigation strategies with protocols |
| **Case types** | Historical only (HBS cases, strategic pivots) | Historical + constructed (Glenda/Crock, Blast Radius) |
| **Architecture focus** | Methodology vs. baselines (M, S1-S4) | Multiple deliberative architectures (B1-B3, C1-C3, P1) |
| **What it tests** | Whether the method is good at prediction | Whether distributed deliberation detects structural features that single-agent reasoning misses |

The evaluation-schemes document explicitly notes that Design C may show the methodology "does not beat baselines at prediction, and that's okay — if methodology's advantage is better decision-making under uncertainty rather than better prediction, then a different dimension would be the relevant measure." The hindsight framework is that different dimension: it tests anticipation (did you see the risk category?) rather than prediction (did you call the outcome?).

**Recommendation**: Run Design C and the hindsight framework on some overlapping cases. If both point the same direction, the evidence is stronger. If they diverge (e.g., methodology doesn't predict better but does anticipate structural risks better), that's an important finding about what deliberation actually provides.

---

## XII. Results Tabulation

Store results in [evaluating-deliberative-architectures/results/](evaluating-deliberative-architectures/results/).

### Table 1 — Condition x Metric Scores

| Condition | Anticipation (0-3) | Epistemic Humility (0-3) | N cases |
|-----------|-------------------|-------------------------|---------|
| B1 (Single LLM) | mean [95% CI] | mean [95% CI] | |
| B2 (Chain-of-thought) | ... | ... | |
| B3 (Multi-perspective) | ... | ... | |
| C1 (Hub-and-spoke) | ... | ... | |
| C2 (Peer-agent committee) | ... | ... | |
| C3 (Deliberated choice) | ... | ... | |

### Table 2 — Topology Map (P1 Runs Only)

| Case | Pattern (Basin/Ridge/Plateau) | Switching Assumption (if Ridge) | Convergent Recommendation |
|------|--------|------|------|
| Case 1 | ... | ... | ... |
| Case 2 | ... | ... | ... |

### Table 3 — Specialized Test Scores

| Condition | Glenda/Crock (0-3) | Blast Radius (0-6) |
|-----------|--------------------|--------------------|
| B1 | ... | ... |
| B2 | ... | ... |
| B3 | ... | ... |
| C1 | ... | ... |
| C2 | ... | ... |
| C3 | ... | ... |

### Table 4 — Effect Sizes

| Comparison | Metric | Cohen's d | 95% CI | Interpretation |
|------------|--------|-----------|--------|---------------|
| C2 vs. B1 | Anticipation | ... | ... | ... |
| C2 vs. B3 | Anticipation | ... | ... | ... |
| C3 vs. C2 | Anticipation | ... | ... | ... |
| C2 vs. B1 | Epistemic Humility | ... | ... | ... |

---

## XIII. Strengths and Limitations

### Strengths

- **Ground truth by hindsight**: Avoids the fundamental problem of evaluating wicked-problem outputs with no reference point.
- **Tests what matters**: Anticipation of structural risks is closer to what people want from deliberative architectures than process quality metrics alone.
- **Contamination-aware**: Explicit mitigation strategies, not just a footnote.
- **Constructed scenarios extend reach**: Glenda/Crock and Blast Radius test structural recognition without requiring historical research.
- **Topology analysis adds a dimension**: Basin/ridge/plateau analysis reveals whether a decision is genuinely hard or just hard for a specific architecture.

### Limitations

1. **Hindsight bias in evaluation**: Even a blind evaluator may rate outputs more favorably if they happen to match the known outcome for reasons unrelated to the output's quality. Mitigation: evaluate on anticipation of *risk category*, not prediction of *specific outcome*.
2. **Small N**: With 6-10 cases, effect sizes are unstable. This is a pilot; treat results as directional, not definitive.
3. **Contamination residual risk**: Even with mitigations, some knowledge leakage is possible. Strategy B (transposition) introduces its own distortions. Report contamination probe results alongside main results.
4. **Single-model limitation**: All conditions use the same base LLM. Results may not generalize to other models. (Cross-model testing is the domain of [multi-model-committee.md](multi-model-committee.md).)
5. **Case selection effects**: Cases chosen for clear outcomes and reconstructable knowledge boundaries may not be representative of the messy, ambiguous decisions where deliberative architectures are most needed.
6. **Anticipation vs. decision quality**: An architecture might anticipate a risk perfectly and still recommend poorly (or vice versa). Anticipation is a component of decision quality, not its entirety.

---

## XIV. Open Questions

1. **Constructed vs. historical case weighting**: Should constructed scenarios (Glenda/Crock, Blast Radius) be weighted equally with historical cases in aggregate analysis? Or reported separately? The constructed scenarios test a different thing (structural recognition vs. anticipatory validity).

2. **How many P1 runs are enough for topology claims?** Three runs may not distinguish ridge from plateau reliably. Would 5 runs be worth the cost?

3. **Cross-referencing with evaluation-schemes dimensions**: Should we also score hindsight-framework outputs on Dimensions A-F from evaluation-schemes? This would let us correlate process quality with anticipatory validity — a high-value finding but a significant increase in rater burden.

4. **Adversarial case construction**: Should we deliberately construct cases where we expect deliberative architectures to *fail*? (E.g., cases where the black swan was genuinely unforeseeable, or where the structural risk was too deeply embedded to surface through any amount of deliberation.) This would test the methodology's limits, not just its strengths.

5. **Publication sequencing**: Should hindsight framework results be published alongside evaluation-schemes results (broader paper) or independently (focused paper on anticipatory validity)?

---

*Connections: [Evaluation Schemes](evaluation-schemes.md), [Ablation Study](ablation-study.md), [Condorcet Comparison](condorcet-comparison.md), [Multi-Model Committee](multi-model-committee.md), [Glenda/Crock Coercion](../../applications/narrative-immune-systems/glenda-crock-coercion.md), [Glenda/Crock Alignment](../../applications/narrative-immune-systems/glenda-crock-alignment.md).*
