# Evaluation Schemes for Cyberneutics Mechanisms

**Status**: Research design document, not a philosophical essay. Intended as a practical guide for empirical testing.

**Last updated**: 2026-02-22

**Origins**: Identified in [agent/handoff-2026-02-21.md](../../agent/archive/handoff-2026-02-21.md) (archived) as the highest-value evidence the project could produce. Committee recommendation in both deliberations (is-author-crackpot, is-author-crackpot-revisited).

---

## I. The Core Question

**Primary research question**: Do the structured mechanisms of Cyberneutics (adversarial committee, scenario generation, deliberated choice/compositions, evaluation loops) produce measurably better decisions than simpler prompting approaches?

**Secondary research question**: Which components contribute meaningfully to improved outcomes, and for which decision types?

**Tertiary research question**: What is the cost/benefit trade-off? (Better decisions may cost more time/tokens.)

---

## II. Why Direct Evaluation Is Intractable

### The Ground Truth Problem
- **No universal "good decision" metric** for genuinely uncertain situations. The methodology is designed for wicked problems (Rittel & Webber) where correctness is unknowable at decision time.
- **Counterfactual difficulty**: We can never know what would have happened if we had decided differently.
- **Outcome lag**: In many real decisions, the outcomes emerge over months or years. By then, the methodology has evolved.

### The Self-Reference Problem
- **Circular evaluation**: Using the methodology's own rubrics (e.g., "assumption coverage," "perspective diversity") to validate the methodology is circular. A framework can define itself as superior by its own definitions.
- **Observation changes state**: The methodology's theoretical framework (second-order cybernetics) posits that observation modifies the system being observed. An evaluation *changes* what it measures.

### The Baseline Problem
- **What counts as "simpler"?** The candidate baselines (single-prompt, chain-of-thought, multi-perspective, debate) are themselves LLM techniques, each with scholarly literature supporting them. There is no neutral ground.
- **Mode specificity**: Structured methodology may outperform on complex decisions while simple prompt engineering outperforms on routine ones. We need conditional results, not global comparisons.

---

## III. Proposed Evaluation Dimensions

These dimensions operationalize what "better" means without requiring ground truth.

### A. Assumption Surface Coverage

**Hypothesis**: Structured methodology surfaces more hidden assumptions than simpler methods.

**Operational definition**:
- An "assumption" is a claim not derivable from the decision inputs; something taken as given without justification.
- Examples: "The market will remain stable" (time horizon assumption), "Stakeholders are rational" (behavioral assumption), "Our data is unbiased" (provenance assumption).

**Measurement**:
1. For each decision, generate outputs from both full methodology and simple baseline.
2. Extract all propositions of the form: "We assume [X]" or implicit assumptions in the form "[X is implicit in the recommendation]."
3. Two independent raters (blind to method) classify each extracted proposition as:
   - **Genuine assumption** (0 = not, 1 = yes)
   - **Salience** (1-3 scale: minor, moderate, critical)
4. Compute:
   - **Total assumptions surfaced** (count of 1s)
   - **Critical assumptions surfaced** (count of salience 3)
   - **Assumption-to-word-ratio** (assumptions per 1000 output words; controls for methodology using more tokens)

**Interpretation**:
- More assumptions is *presumptively* better for wicked problems (you want to see what you're committing to).
- But not infinitely better; diminishing returns beyond ~N assumptions.
- Results should be reported as: "Methodology surfaced M assumptions vs. B for baseline; X% were critical."

**Why this dimension**:
- Directly measurable without ground truth.
- Tied to a specific cognitive benefit (making implicit commitments explicit).
- Ratable by humans without requiring domain expertise (though domain experts can rate salience better).

---

### B. Trade-off Explicitness

**Hypothesis**: Structured methodology makes trade-offs between objectives explicit; simpler methods elide them.

**Operational definition**:
- A "trade-off" is a situation where advancing one goal means constraining another. Example: "Faster decision-making trades off against stakeholder consultation."
- Trade-offs must be explicitly named and quantified (or at least rank-ordered) in the output.

**Measurement**:
1. For each decision, extract claims about trade-offs.
2. For each trade-off, code:
   - **Named**: Is the trade-off explicitly named? (0 = no, 1 = yes)
   - **Quantified**: Is it rank-ordered or numerically bounded? (0 = no, 1 = partially, 2 = yes)
   - **Defended**: Is there an argument for why this trade-off was resolved this way? (0 = no, 1 = yes)
3. Compute:
   - **Trade-offs identified** (count)
   - **Trade-offs defended** (count of defended)
   - **Defense-to-identification ratio** (should be high; identifying a trade-off without defending your position is incomplete)

**Interpretation**:
- Higher is presumptively better (you want decisions to explicitly state what you're giving up).
- Can be *misused* (identifying many false trade-offs just to score high); raters should validate.
- Results: "Methodology identified T trade-offs, defended D; baseline identified T', defended D'."

**Why this dimension**:
- Captures reasoning clarity without requiring ground truth.
- Ratable by domain experts who understand the decision space.
- Tied to a practical benefit: decision-makers who know the trade-offs can monitor them.

---

### C. Falsifiability

**Hypothesis**: Structured methodology produces falsifiable predictions; simpler methods produce hedged, unfalsifiable statements.

**Operational definition**:
- A **falsifiable prediction** is a claim that can be proven false by observing future states.
- Examples: Falsifiable: "Revenue will exceed $X within 12 months." Unfalsifiable: "Revenue might increase if market conditions improve."

**Measurement**:
1. Extract all forward-looking claims (predictions, recommendations about future).
2. For each claim, code:
   - **Form**: Is it falsifiable (1) or hedged/unfalsifiable (0)?
   - **Horizon**: How far in future is the claim testable? (days, months, years)
   - **Falsifiability quality**: Does it have explicit success/failure criteria? (0 = no, 1 = partial, 2 = yes)
3. Compute:
   - **Falsifiable-to-total ratio** (% of claims that are testable)
   - **Explicit-criteria ratio** (% of falsifiable claims with success metrics)

**Interpretation**:
- Higher falsifiability is presumptively better (you can actually test whether the decision was good).
- But some irreducible hedging is reasonable for genuine uncertainty (hedging shouldn't be counted as failure to falsify).
- Results: "Methodology produced F% falsifiable predictions; baseline produced F'%."

**Why this dimension**:
- Directly tied to accountability (did the prediction come true?).
- Can be automated if success criteria are explicit (no human judge needed for later evaluation).
- Captures the methodology's claim to support learning cycles.

---

### D. Perspective Diversity

**Hypothesis**: Structured methodology with character-based debate produces more genuinely different perspectives than simple "give me multiple views" prompts.

**Operational definition**:
- A **distinct perspective** is a viewpoint that cannot be derived from other viewpoints in the set. It represents a different value order, factual belief, or risk tolerance.
- Examples: Perspective A = "maximize growth" vs. Perspective B = "preserve stability" are distinct. Perspective A = "maximize growth" vs. Perspective A' = "maximize growth, but carefully" are *not* distinct.

**Measurement**:
1. For each decision, extract all perspectives/positions from methodology output and baseline.
2. Two independent raters (blind to method and source) classify each perspective as:
   - **Distinct from all others** (1) or **derivative** (0)
   - **Internally coherent** (1-3 scale: contradictory, mostly coherent, fully coherent)
3. Compute:
   - **Distinct perspective count** (count of distinct=1)
   - **Coherence score** (mean coherence rating)
   - **Diversity index** (use Herfindahl-Hirschman Index or similar; higher = more evenly distributed, lower = one perspective dominates)

**Interpretation**:
- More distinct perspectives is presumptively better, but past ~5-7, returns diminish and cognitive load increases.
- Coherence matters; contradictory perspectives are not useful.
- Diversity index captures *balance*: methodology might produce 5 distinct perspectives; baseline might produce 2 distinct + 3 repetitions.
- Results: "Methodology produced D distinct, coherent perspectives vs. D' for baseline; diversity index M vs. M'."

**Why this dimension**:
- Directly observable without ground truth.
- Validates core claim of structured methodology: character-based debate forces different viewpoints.
- Can be rated by humans without domain expertise (just reading comprehension).

---

### E. Reasoning Chain Completeness

**Hypothesis**: Structured methodology provides traceable reasoning (premises → inference rules → conclusions); simpler methods jump to conclusions.

**Operational definition**:
- A **complete reasoning chain** is one where you can identify:
  1. Premises (what we assume true)
  2. Inference rules (how conclusions follow from premises)
  3. Conclusions (the recommendation or claim)
  4. Failure modes (what would make this reasoning break)
4. A chain is "complete" if all four elements are present and connected.

**Measurement**:
1. Extract the main recommendation/conclusion from each output.
2. For each conclusion, trace backward:
   - What premises does it depend on?
   - What inference rule connects premises to conclusion?
   - What would falsify the conclusion?
3. Raters code:
   - **Premise clarity**: Are all critical premises explicit? (0 = no, 1 = mostly, 2 = yes)
   - **Inference transparency**: Can you see *why* the conclusion follows? (0 = unclear, 1 = visible, 2 = explicit)
   - **Failure mode visibility**: Are failure modes discussed? (0 = no, 1 = mentioned, 2 = explicit with triggers)
4. Compute:
   - **Completeness score** (sum of three subscales, 0-6)
   - **Proportion of decisions with complete chains** (count scoring 5-6 / total)

**Interpretation**:
- Higher completeness is presumptively better (more auditable, more learnable).
- This is where evaluation loop documentation helps; review rubrics should explicitly ask for reasoning chains, and deliberation transcripts naturally surface them.
- Results: "Methodology produced complete chains in X% of conclusions vs. Y% for baseline."

**Why this dimension**:
- Captures a core design goal of the methodology: governance through transparency.
- Ratable by humans (no expert needed, just logical reasoning).
- Directly testable in post-hoc evaluation.

---

### F. Scenario Robustness (Methodology-Specific Dimension)

**Hypothesis**: Deliberated choice (fan→funnel composition) produces recommendations that work across multiple possible futures; simple methods produce single-future optimizations.

**Operational definition**:
- A recommendation is **scenario-robust** if it is defensible (meets the decision-maker's objectives) across multiple possible future states, not just the most likely one.
- Operationally: if you generate 4 contrasting scenarios (continuity, disruption, opportunity, constraint), a robust recommendation should not require all 4 to go a specific way.

**Measurement**:
1. For methodology output, extract the scenarios used (if any) and the recommendation.
2. Generate the same 4 scenarios for the baseline (do not use baseline's scenarios if it generated any; use neutral scenarios).
3. Test: "If [scenario X] occurs, is this recommendation still defensible?"
   - Code: 0 = breaks, 1 = weakens but holds, 2 = holds fully
4. Compute:
   - **Robustness score** (mean score across 4 scenarios, 0-2)
   - **Robustness variance** (does recommendation break under one scenario type?)
   - **Scenario dependence**: How many scenarios must come true for recommendation to work? (Higher = more brittle)

**Interpretation**:
- Methodology should score higher on robustness because it *explicitly* tested scenarios.
- Baseline may score high if it happened to produce a robust recommendation by luck, or low if it overfit to one scenario.
- Results: "Methodology recommendation robust across R scenarios vs. R' for baseline."

**Why this dimension**:
- Unique measurement of the fan→funnel composition benefit.
- Directly tied to methodology claim about handling uncertainty.
- Requires scenario generation (can be automated or human-generated).

---

## IV. Measurement Workflow and Rater Design

### Rater Pool

**All evaluations use independent, fresh-instance raters**, never the authors of the decision outputs.

**Rater composition**:
- **Dimension A (assumptions)**: 2 raters, any background (task is recognizing unstated claims).
- **Dimension B (trade-offs)**: 2 raters, domain experts if possible (rating requires understanding the decision space).
- **Dimension C (falsifiability)**: 2 raters, any background (logical classification).
- **Dimension D (perspective diversity)**: 2 raters, any background (reading comprehension).
- **Dimension E (reasoning chains)**: 2 raters, philosophical or logical training preferred (must understand inference structure).
- **Dimension F (scenario robustness)**: 2 raters, domain experts (must understand decision context).

**Blind protocol**:
- All outputs stripped of identifying metadata (methodology name, time stamps, author info).
- Raters randomized over outputs (Method output 1 might be evaluated by Rater A; Method output 2 by Rater B).
- Consensus: if raters disagree >0.15 on continuous scales, resolve by third rater or discussion.

### Coding and Reliability

**Inter-rater reliability threshold**: Cohen's kappa ≥ 0.70 for categorical codes; ICC(3,1) ≥ 0.70 for continuous scales.

**If threshold not met**:
- Raters discuss discrepancies.
- Refine coding instructions if ambiguity is systematic.
- Rerun calibration on subset before full evaluation.

**Reporting**:
- All results reported with confidence intervals (95% CI).
- All inter-rater agreements reported.
- If agreement low, note as limitation.

---

## V. Experimental Designs

### Design A: Blind Panel Evaluation (Recommended first step)

**Objective**: Directly compare methodology vs. simple baselines on all six dimensions using structured rating.

**Procedure**:
1. **Select N decisions** (recommend N ≥ 8, ideally 10-15).
   - Decisions should be realistic, moderately complex, genuinely uncertain.
   - Ideally, decisions where outcomes are not yet known (avoid hindsight bias).
   - Domain variety: one or two from strategy/business, one or two from product, one or two from public policy, others as available.

2. **Generate outputs for each decision using**:
   - **Condition M**: Full cyberneutics methodology (committee + scenarios + deliberated choice).
   - **Condition S1**: Single-prompt baseline: "What should we do? Explain your reasoning."
   - **Condition S2**: Chain-of-thought baseline: "What should we do? Explain step-by-step reasoning and assumptions."
   - **Condition S3**: Multi-perspective baseline: "Give me 3-5 genuinely different perspectives on this decision."
   - *Optional* **Condition S4**: Self-critique baseline: "What should we do? Then critique your own answer."

3. **Strip metadata and randomize**: All outputs anonymized, randomized across raters.

4. **Rate on dimensions A-E** (F optional, requires scenario generation):
   - Use standardized codebooks (see Appendix).
   - Blind rating by rater pool.
   - Calculate inter-rater agreement before aggregation.

5. **Analyze**:
   - For each dimension: compute effect size (mean difference, Cohen's d, or equivalent).
   - Report by dimension and by condition.
   - Report moderation effects: does methodology advantage scale with decision complexity? With domain?

**Expected output**:
- Table: dimensions (rows) × conditions (columns) with mean scores and 95% CIs.
- Effect sizes showing which dimensions/conditions show largest gaps.
- Qualitative notes on surprising patterns.

**Strengths**:
- Direct evidence.
- Blind rating eliminates confirmation bias.
- Generalizable results.
- No requirement for ground truth.

**Weaknesses**:
- Expensive (N decisions × 4 conditions × 2 raters × 6 dimensions = ≈200+ rater-hours).
- Results may be modest (Methodology might beat S1 by 20-30%, not 100%).
- Dimensions may correlate (methodology beats on most, so result is not surprising).

**Timeline**: 4-6 weeks with coordinated rater pool.

---

### Design B: Retrospective Case Analysis

**Objective**: Find decisions made using the methodology, wait for outcomes, compare what was surfaced vs. what mattered.

**Procedure**:
1. **Identify past decisions** where:
   - Methodology was used (or could be reconstructed).
   - Outcomes are now known (6+ months later).
   - Sufficient documentation exists to evaluate both recommendation and outcome.

2. **Reconstruct the simple baselines**: Run the decision through S1, S2, S3 *at the original decision time* (using information that was available then, not hindsight).

3. **Compare what was surfaced**:
   - What assumptions did the methodology surface that turned out critical?
   - What trade-offs did it identify that actually mattered in execution?
   - What perspectives did it include that became relevant?
   - Which of these did simple baselines miss?

4. **Quantify**:
   - For each decision: count of [assumptions surfaced that mattered] / [total assumptions surfaced].
   - Same for trade-offs, perspectives.
   - For methodology vs. baseline.

5. **Analyze**:
   - Did methodology surface more decision-relevant content?
   - Did its scenario analysis predict what actually happened?
   - Did recommendations degrade less gracefully when reality diverged from assumptions?

**Expected output**:
- Case narratives (5-10 cases, ~2-3 pages each).
- Quantitative summary: Methodology relevance ratio vs. baseline ratio.
- Pattern: Did methodology help more for decisions that went well or badly? (If methodology only helps when you get lucky, that's a negative result.)

**Strengths**:
- Uses real outcomes, not proxies.
- No risk of artificial task effects.
- Builds credibility through transparency.

**Weaknesses**:
- Requires time passing (minimum 6 months between decision and evaluation).
- Confounding: outcomes depend on execution, not just decision quality.
- Hindsight bias: ex-post evaluation of "obvious" outcomes.
- Requires sufficient historical record.

**Timeline**: 8-12 months (waiting) + 2-4 weeks (retrospective analysis).

---

### Design C: Predictive Accuracy on Known Outcomes

**Objective**: Use historical scenarios with known outcomes to test which method better anticipated what happened.

**Procedure**:
1. **Find a library of historical decision scenarios**:
   - Business case studies, policy simulations, investment decisions, organizational changes.
   - Requirements: decision was made, outcomes are now documented, decision context is available.
   - Examples: Harvard Business School cases, strategic pivots at known companies, policy reversals, product launches with known outcomes.

2. **For each scenario**:
   - Reconstruct the decision as it would have looked at decision time.
   - Run through Methodology and Baselines (S1, S2, S3).
   - Extract predictions made by each approach (explicit or implicit).

3. **Score predictions**:
   - Which approach's prediction of what would happen was closest to actual outcome?
   - Which approach's recommendation would have worked better if followed?
   - Code: 0 = completely wrong, 1 = partially right, 2 = substantially right.

4. **Analyze**:
   - Prediction accuracy by condition.
   - Recommendation quality by condition.
   - Scenarios where methodology shines (genuinely uncertain, complex) vs. scenarios where baselines perform equally.

**Expected output**:
- Prediction accuracy table by scenario and condition.
- Scenarios where each method outperforms.
- Evidence of whether methodology is better at navigating genuine uncertainty.

**Strengths**:
- Uses real historical data.
- Tests actual predictive power, not proxies.
- Not subject to AI artifact effects (the decisions were made by humans, outcomes are objective).

**Weaknesses**:
- The methodology is **not designed for prediction**; it's designed for mapping the decision landscape. This test may measure the wrong thing.
- Selection bias: available case studies may not be representative of the decisions the methodology targets.
- Reconstruction difficulty: may be hard to recreate the informational state at decision time.

**Timeline**: 3-4 weeks (case selection and reconstruction) + 2-3 weeks (evaluation).

**Note**: This design may show that methodology does *not* beat baselines at prediction, and that's okay. If methodology's advantage is "better decision-making under uncertainty" rather than "better prediction," then a different dimension (scenario robustness, assumption coverage) would be the relevant measure.

---

### Design D: Information-Theoretic Comparison (Automated Baseline)

**Objective**: Measure diversity and entropy in outputs without requiring human judges.

**Procedure**:
1. **Generate outputs** for N decisions using Methodology and Baselines.

2. **Compute automated metrics**:
   - **Lexical diversity**: Type-token ratio, vocabulary richness (MTLD or similar).
   - **Structural entropy**: Measure of how different the argument structures are (entropy of sentence length distribution, argument types, etc.).
   - **Perspective density**: Using NLP/embedding tools, cluster perspectives and count distinct clusters.
   - **Assumption density**: Train a classifier to recognize assumption statements; count statements scored as assumptions per 1000 words.

3. **Statistical comparison**:
   - Methodology mean entropy vs. Baseline means.
   - Effect sizes.

**Expected output**:
- Information-theoretic metrics showing methodology produces higher-entropy (more diverse) outputs.
- Correlation analysis: does output entropy correlate with blind-panel dimension scores? (If yes, automation is validated; if no, important signals are lost in automation.)

**Strengths**:
- Cheap and fast (runs automatically).
- Objective (no rater bias).
- Can scale to very large N.
- Good diagnostic for whether methodology actually explores more possibilities.

**Weaknesses**:
- Higher entropy ≠ better decisions. A nonsensical paragraph has high entropy.
- Measures *coverage of possibility space*, not quality of reasoning.
- Missing what matters: a diverse but wrong output is worse than a boring correct output.
- **Use as a complement to other designs, not as a standalone test.**

**Timeline**: 1-2 days.

---

### Design E: Expert Judgment Panel

**Objective**: Have domain experts evaluate which output they would trust for a real decision.

**Procedure**:
1. **Recruit domain experts** (N ≥ 3-5 per decision domain).
   - For business decisions: executives, strategy consultants.
   - For product: product managers, designers.
   - For policy: policy analysts, academics.

2. **Present pairs**:
   - Show expert a decision + two outputs (Methodology vs. one Baseline, counterbalanced).
   - Blind to method.
   - Prompt: "If you had to make this decision using *only* one of these outputs, which would you choose? Why?"

3. **Quantify**:
   - % of times Methodology is chosen.
   - Time spent reading each output (implicit confidence signal).
   - Qualitative reasons (transcript).

4. **Analyze**:
   - Which method wins by domain?
   - What criteria do experts use to prefer one output? (Do they mention same dimensions as Design A?)
   - Do results correlate with Design A results?

**Expected output**:
- Preference percentages: "Experts chose Methodology X% of time vs. S1 Y% of time."
- Qualitative quotes: "Methodology was chosen because [clearer assumptions / more complete trade-off analysis / easier to monitor]."
- Credibility: external validation that Design A results are not artifacts.

**Strengths**:
- External validation (not the authors' evaluation).
- Captures practical decision-making (people trust outputs intuitively).
- Easy to interpret results.

**Weaknesses**:
- Expensive (expert time).
- Small sample sizes (hard to recruit many experts).
- Qualitative; may not generalize.

**Timeline**: 2-3 weeks (recruiting, interviews).

---

### Design F: Ablation Study

**Design F: Ablation Study.** Run full pipeline and remove or vary components to measure each component's contribution and interaction effects. Full procedure, factor definitions, run budget, and results tabulation are in [ablation-study.md](ablation-study.md). Results (when available): [ablation-study/results/](ablation-study/results/).

---

## VI. Composition and Sequencing

### Recommended Implementation Plan

**Phase 1 (Immediate, 4-6 weeks)**: Design F (Ablation Study)
- See [ablation-study.md](ablation-study.md) for plan and results.
- Cheapest to run.
- Directly informs whether each component is valuable.
- Can be run in parallel with decision-making; no waiting for outcomes.
- Result informs whether to invest in Phase 2.

**Phase 2 (6-10 weeks)**: Design A (Blind Panel Evaluation)
- Most convincing to external audiences.
- Requires recruiting rater pool and training (2 weeks), then rating (3-4 weeks).
- Most replicable and publishable.
- Consider publishing Design F + Design A results together.

**Phase 3 (Parallel to Phase 2 or after, negligible time)**: Design D (Information-Theoretic Baseline)
- Run after decisions are generated for Phase 2; uses same outputs.
- Use to validate whether high design scores correlate with high entropy.

**Phase 4 (Optional, 2-3 weeks)**: Design E (Expert Judgment)
- Use results from Design A to recruit experts.
- Smaller, qualitative validation.
- Strong credibility (independent experts).

**Phase 5 (Requires time passing, 6+ months)**: Design B (Retrospective Case Analysis)
- Start identifying candidate cases while running Phase 1-2.
- Execute once 6+ months of outcomes are available.
- Consider publishing as future follow-up.

**Phase 6 (Optional, research only)**: Design C (Predictive Accuracy)
- Use if Design A shows ambiguous results.
- Otherwise lower priority (methodology not designed for prediction).

### Integrated Output

After Phase 2 (by month 3):
- **Paper/Report**: "Structured Decision-Making Under Uncertainty: An Empirical Evaluation of Cybernetic Methodology"
  - Methods: Design F + Design A (and D if run in parallel)
  - Results: Component contributions + relative performance on each dimension
  - Discussion: Where methodology shines; where simple methods suffice
  - Caveats: limitations of proxy measures, possible confounds

After Phase 4 (by month 4-5):
- **Supplement**: Qualitative validation from expert panel (Design E)

After Phase 5 (by month 9-12):
- **Follow-up paper**: "Retrospective Validation: Do Structured Decisions Weather Uncertainty Better?"

---

## VII. Success Criteria and Interpretation

### Scenario A: Methodology Clearly Wins
- Methodology scores significantly higher (effect size d ≥ 0.5) on Dimensions A, B, D, E.
- Expert judges prefer methodology ≥65% of the time.
- Ablation shows all components contribute (each adds ≥5% improvement); see [ablation-study](ablation-study.md) for run results.

**Interpretation**: Publish results. Methodology has evidence-based support. Useful for adoption and credibility.

**Publication language**: "Structured adversarial deliberation produces more transparent, assumption-aware, scenario-robust decisions than prompting baselines across [N=?] decisions."

---

### Scenario B: Methodology Wins on Some Dimensions, Not Others
- Methodology higher on Dimensions A (assumptions), E (reasoning chains), F (scenario robustness).
- Baselines equivalent on Dimension D (perspective diversity, if good baseline engineering).
- Methodlogy costs more (tokens, time) but produces clearer outputs.

**Interpretation**: Not a loss. Methodology has *specific* value (clearer reasoning, assumption transparency) not *general* superiority. Publish with caveats.

**Publication language**: "Structured deliberation excels at surfacing assumptions and trade-offs [Dimension A, B] and maintaining scenario robustness [Dimension F]. Perspective diversity [Dimension D] is achievable with simpler multi-perspective prompting. Cost-benefit trade-off depends on decision stakes."

---

### Scenario C: Methodology and Baselines Perform Equivalently
- Effect sizes all < 0.2 (negligible).
- Expert judges split preferences.
- Ablation shows many components contribute little; see [ablation-study](ablation-study.md) for run results.

**Interpretation**: Methodology does *not* provide better decisions; it provides *clearer reasoning and documentation*. This is still valuable for governance, but not a claim about decision quality.

**Publication language**: "Structured deliberation does not produce higher-quality decisions than well-engineered simple prompts on these dimensions. Value lies in process transparency and auditability, not outcome superiority."

**Recommendation**: Reframe methodology as a *governance* tool (makes decisions auditable, traceable) rather than a *decision-quality* tool.

---

### Scenario D: Methodology Underperforms
- Methodology scores significantly lower on multiple dimensions.
- Expert judges prefer baselines ≥65% of the time.

**Interpretation**: Methodology has problems. Publish honestly. Investigate why (Are evaluators biased? Is the methodology poorly instantiated? Are dimensions measuring the wrong things?).

**Publication language**: "In head-to-head evaluation, structured methodology did not outperform simpler baselines. Possible explanations: [list], recommending [next steps]."

**Recommendation**: Don't suppress results. Publish with a committee (or external expert) reflecting on findings.

---

## VIII. Measurement Tools and Codebooks

### Appendix: Dimension A Codebook (Assumption Surface Coverage)

**Definition**: An assumption is a proposition that is necessary for the conclusion to hold, but is not derivable from the inputs and is not explicitly justified in the output.

**Coding examples**:

| Statement | Assumption? | Salience | Rationale |
|-----------|------------|----------|-----------|
| "We assume the market will remain stable." | Yes | 3 | Critical; undiscussed; changes recommendation if false |
| "Stakeholders have common values." | Yes | 2 | Moderate; implicit in multi-stakeholder framework |
| "Our data reflects ground truth." | Yes | 3 | Critical for inference; unvalidated |
| "Speed is more important than consensus." | No | N/A | Stated explicitly; not hidden |
| "Regulation will not change." | Yes | 2-3 | Depends on domain; regulatory risk is real |

**Procedure**:
1. Extract sentences of the form "We assume...", "Assuming that...", "Given that..." → count as explicit (record).
2. Identify *implicit* assumptions by asking "If this conclusion were false, what would have to be true?" Example: Recommendation "Launch now" implicitly assumes market timing is critical.
3. Rate salience: Could the assumption, if false, change the recommendation? (3=yes, 2=maybe, 1=probably not).

---

### Appendix: Dimension F Codebook (Scenario Robustness)

**Definition**: A recommendation is robust if it is defensible across multiple contrasting futures.

**The four scenarios** (use these for all evaluations):
1. **Continuity**: Current trends continue. Market/environment behaves as expected. Assumptions hold.
2. **Disruption**: A major disruptive event occurs (technological, market, regulatory, geopolitical). Status quo breaks.
3. **Opportunity**: An unexpected positive development emerges (new market, partnership, capability). Upside appears.
4. **Constraint**: A limiting factor tightens unexpectedly (regulation, resource scarcity, competitor). Downside emerges.

**Coding**:
- For each scenario: "If [scenario] occurs, does the recommendation still make sense?"
  - 0 = breaks (recommendation fails or makes things worse)
  - 1 = weakens (recommendation holds but with reduced effectiveness or modified execution)
  - 2 = holds (recommendation remains sound; possibly requires adaptation)

**Example**:

Scenario: "Launch a new product line immediately"
- **Continuity**: Recommendation holds (2). Demand grows as expected.
- **Disruption**: Breaks (0). If market disrupts, new product is vulnerability; should have delayed.
- **Opportunity**: Holds (2). If opportunity emerges, being in market early is advantage.
- **Constraint**: Weakens (1). If resource constraint tightens, product launch strains finances, but can be executed more carefully.

**Robustness score**: (2 + 0 + 2 + 1) / 4 = 1.25 / 2.0 = "Moderately robust; breaks under disruption scenario."

---

## IX. Ethical Considerations and Conflict of Interest

### Bias and Conflicts

1. **Author bias**: The methodology's author (if evaluating) should not be an evaluator. Use independent raters and design blind protocols.

2. **Publication bias**: There is incentive to design evaluations that make methodology look good. **Commit in advance** (this document) to:
   - Publishing results regardless of outcome (especially if negative).
   - Reporting effect sizes and confidence intervals, not just significance.
   - Discussing limitations and alternative interpretations.

3. **Interpretation bias**: Results can be framed favorably even if modest. **Agreed language**:
   - If effect size d < 0.3 (small), describe as "modest" or "marginal," not "significant" or "substantial."
   - If effect size 0.3 ≤ d < 0.8, describe as "moderate."
   - If effect size d ≥ 0.8, describe as "substantial."

4. **Audience mismatch**: Results publishable for academic audience may be misrepresented for practitioners. **Agreed responsibility**:
   - Academic paper: full caveats and limitations.
   - Practitioner summary: clear statement of decision-types where methodology helps and where it doesn't.

### Honesty Safeguards

- **Steering committee** (optional, but recommended): For major evaluation runs, convene a 2-3 person committee (external to the project, skeptical) to review evaluation design and interpretation.
- **Pre-registration**: Publish this design and all hypotheses *before* running evaluations, to constrain post-hoc interpretation.
- **Reporting all results**: If you run Design A and get mixed results, report *all* dimensions, not just positive ones.
- **Negative results are data**: If methodology underperforms on some dimension, that's important for understanding what it does and doesn't do.

---

## X. Resource Estimates

### Staffing and Timeline

| Phase | Design | Effort (person-hours) | Duration | Notes |
|-------|--------|----------------------|----------|-------|
| 1 | F (Ablation) | 40-60 | 4 weeks | Generate outputs, rate, analyze |
| 2a | A (Panel) setup | 20 | 2 weeks | Codebook, rater training, pilot |
| 2b | A (Panel) execution | 180-250 | 3-4 weeks | 2 raters × 6 dimensions × 8-15 decisions |
| 2c | A (Panel) analysis | 20 | 1 week | Aggregate, effect sizes, write-up |
| 3 | D (Information theory) | 10 | 2 days | Automated metrics; correlate with A |
| 4 | E (Expert) | 40-60 | 2-3 weeks | Recruit, interviews, transcription |
| 5 | B (Retrospective) | 60-80 | 4 weeks | Case research, outcome verification |
| 6 | C (Prediction) | 40-60 | 3 weeks | Historical case reconstruction |

**Total (Phases 1-4)**: ~600-700 person-hours over ~10 weeks. (Approximately one person, three-quarter time.)

**Cost factors**:
- Rater recruitment: If using internal staff, cost is opportunity cost. If external, ~$50/hour × 250 hours = ~$12.5K.
- Decision generation: If using existing methodology/staffing, negligible incremental cost. If not, ~40-60 hours.
- Expert recruitment (Design E): ~$150-500 per expert × 3-5 experts = ~$1-2K.

---

## XI. Known Limitations and Open Questions

### Limitations

1. **Proxy measures, not ground truth**: Dimensions A-F are *correlated with* decision quality (in theory), not *measures of* decision quality. An output can be high on all dimensions and still lead to a bad decision if the decision-maker ignores it.

2. **Decision selection effects**: Decisions chosen for evaluation may not be representative (selection for complexity, clarity, interest). Results may not generalize to all decisions.

3. **Task artifact**: LLM outputs are evaluated on LLM outputs. The evaluation may measure "which prompt style produces outputs that raters prefer" rather than "which method produces better decisions."

4. **Mode dependence**: Results apply to LLM-based decisions. May not generalize to human deliberation or mixed teams.

5. **Small sample, limited domains**: Even with N=10-15 decisions, effect sizes are unstable. Multiple domains (business, product, policy) help generalize, but each domain may only have 3-5 decisions.

6. **Rater training**: Quality of evaluation depends heavily on codebook clarity and rater training. Poor rater training → unreliable results.

### Open Questions

1. **Outcome lag**: How long after a decision should we evaluate it? Some outcomes emerge in weeks (product launch success), others in years (strategic pivot). Recommendation is 6 months minimum; but this varies.

2. **Remediation/refinement**: Can decision-makers improve decisions by acting on methodology outputs? If yes, is that an advantage of methodology (it helps people improve) or a disadvantage (the output wasn't good enough to start)?

3. **Decision complexity threshold**: At what level of complexity does methodology start to help? Is it helpful for simple binary decisions? Or only for complex, wicked problems?

4. **Generalization to humans**: Do the same mechanisms work if humans deliberate instead of LLMs? (Different research; noted for future.)

5. **Curation and selection bias**: The methodology asks the user to curate which committee recommendation or scenario output to act on. Does this curation undermine the objectivity of evaluation? (It may be a feature, not a bug: good decisions require editorial judgment.)

---

## XII. Publication and Dissemination

### Venues

- **Academic** (if results are rigorous):
  - Journal: *Organization Science*, *Administrative Science Quarterly*, *Organizational Dynamics* (decision-making focused).
  - Conference: Academy of Management (OB/OM division).

- **Practitioner** (if results are encouraging):
  - Harvard Business Review, McKinsey Quarterly (decision-making, strategy tools).
  - White paper published on project site.

- **Methodological** (regardless of outcome):
  - *Research Methods in Organizations*, *Qualitative Research in Organizations and Management* (evaluation methodology).

### Key Messages by Audience

**For skeptics**: "We designed this evaluation to find negative results if they exist. Here's what we found."

**For practitioners**: "This methodology helps in [specific situation type]. For [other situation type], simpler methods work fine. Here's the decision tree for when to use each."

**For academics**: "Structured deliberation is a testable design pattern. Here's the evidence and the open questions for future research."

---

## XIII. Success Metrics for This Evaluation Document

This document succeeds if:

1. **Implementable**: A team with 1-2 dedicated people and ~$10-15K budget can execute Phases 1-4 over ~3 months.

2. **Honest**: Design choices (dimension selection, codebooks, rater protocols) are transparent enough that someone could argue with them, replicate them, or improve them. (If the design seems impossible to argue with, it's probably overfit to the hypothesis.)

3. **Multi-faceted**: Not betting everything on one dimension or one design. Phases 1-4 provide multiple angles of evidence.

4. **Publishable as-is**: Even if methodology underperforms, results from this design are suitable for publication (with caveats). The design doesn't presuppose a favorable outcome.

5. **Actionable**: Results should tell you something concrete about when to use methodology and when not to.

---

## XIV. Appendix: References and Related Work

### Evaluation of Decision-Making Systems

- **Russo & Schoemaker (2002)**: "Winning Decisions" — framework for evaluating decision quality retrospectively via assumption checking and outcome analysis.
- **Kahneman & Klein (2009)**: "Conditions for Intuitive Expertise" — on when expert judgment is reliable (varies by feedback loops and outcome clarity).
- **Tetlock & Gardner (2015)**: "Superforecasting" — evaluation of probabilistic prediction; relevant for Dimension C (falsifiability).

### LLM Evaluation

- **Karpukhin et al. (2021)**, **Lewis et al. (2020)**: Benchmarking information retrieval and retrieval-augmented systems; provides methods for evaluating LLM outputs.
- **Liang et al. (2023)**: "Holistic Evaluation of Language Models" — comprehensive framework for evaluating LLM capabilities on multiple dimensions.

### Deliberation and Governance

- **Chambers (2003)**: "Deliberative Democratic Theory" — philosophical framework for evaluating deliberative processes (transparency, perspective diversity, reasoned argument).
- **Mansbridge et al. (2006)**: "Deliberative Systems" — framework for evaluating quality of deliberation in organizational/public contexts.

### Comparative Methodology

- **Shadish, Cook & Campbell (2002)**: "Experimental and Quasi-Experimental Designs" — design reference for comparative evaluation with threats to validity.

---

**Status**: Ready for implementation. Recommend review and pre-registration before running Phase 1.

**Next step**: If approved, begin Phase 1 (Ablation Study) design and rater recruitment; plan and results location: [ablation-study.md](ablation-study.md).
