# Multi-Model Committee: Experimental Plan

**Status**: Active (not started)
**Runs**: (none yet)
**Results**: (no results folder yet; create `multi-model-committee/results/` when Phase 1 begins)

> **Contributing to this program**
> - **Skills needed**: API access to 2+ LLM providers (e.g., Anthropic + OpenAI), ability to run `/committee` deliberations, basic statistics (rubric scoring, effect sizes). Phase 1 requires only API calls and analysis; later phases require orchestration code.
> - **Estimated scope**: Phase 1 is 1-2 weeks (~20 hours). Phase 2 is 2-4 weeks (~30 hours). Full program is 3-6 months.
> - **Contributor type**: Solo for Phase 1; collaborative for Phases 2+.
> - **Entry point**: Read the Hypothesis section below, then jump to Phase 1 (Establish Baseline + Model Profiles). Phase 1 is self-contained and produces publishable results regardless of whether later phases run. For architectural background, see [multi-model-committee-reference.md](multi-model-committee-reference.md).

---

## Objective

Test whether using different LLM models to play different committee characters produces more authentic and rigorous adversarial deliberation than a single model simulating all five characters.

**Core claim**: A single model simulating five characters must overcome its own training biases to generate genuine disagreement. Different models with genuinely different training distributions could produce more authentic adversarial dynamics at lower cognitive cost.

**Theoretical grounding**: Multi-agent debate literature consistently shows that systems composed of diverse agents outperform systems using the same agent multiple times — but diversity must be genuine (different training, different optimization targets), not simulated. See the full hypothesis and theoretical basis in [multi-model-committee-reference.md § The Hypothesis](multi-model-committee-reference.md#the-hypothesis-why-model-diversity-matters).

---

## Experimental Protocol

### Phase 1: Establish Baseline + Model Profiles

**Goal**: Validate that single-model works as expected; profile each model's natural tendencies.

**Duration**: 1–2 weeks

**Procedure**:

1. **Single-Model Baseline** (5 topics, 1 run each)
   - Run standard deliberations using current single-model approach
   - Topics should cover diverse domains (ethics, technical, governance, resource allocation, strategy)
   - Score on 5 rubrics
   - Record as `baseline-single-model.json`

2. **Model Personality Profiles** (5 topics, 1 response per model, no deliberation)
   - For each topic, send to all 5 models: "Please respond to this topic: [topic]. What's your perspective?"
   - No character roleplay, no prior context
   - Analyze responses for:
     - Length, hedging score, confidence, evidence count
     - Risk mentions, value mentions, sentiment
     - Logical structure, novelty of framing
   - Record as `model-profiles.json`

3. **Output**:
   ```yaml
   baseline_scores:
     topic_1:
       comprehensiveness: 8.2
       adversarial_rigor: 7.1
       assumption_coverage: 8.5
       reasoning_depth: 7.8
       decision_readiness: 7.4
       avg: 7.8

   model_profiles:
     claude:
       hedging_avg: 0.62
       confidence_avg: 0.58
       evidence_count_avg: 2.4
       risk_mentions_avg: 1.2
       value_mentions_avg: 3.8
     gpt4:
       hedging_avg: 0.31
       confidence_avg: 0.72
       evidence_count_avg: 4.1
       risk_mentions_avg: 2.1
       value_mentions_avg: 0.9
     ... etc
   ```

**Decision Gate**: Do model profiles justify hypothesis that different models have different personalities? If yes, proceed to Phase 2.

---

### Phase 2: Comparative Architectures

**Goal**: Run the same topics through Patterns 1, 3, and 4; compare outputs.

**Duration**: 2–4 weeks

**Procedure**:

1. **Pattern 1: Fixed Mapping** (5 topics, 1 run each)
   - Use empirically-derived model-character assignments from Phase 1
   - Example mapping:
     - Maya: Llama (high risk mentions, low hedging)
     - Frankie: Claude (high value mentions)
     - Vic: GPT-4o (high evidence count, high confidence)
     - Tammy: Gemini (high cross-domain references)
     - Joe: Claude or Gemini (maintain coherence)
   - Score on 5 rubrics, track per-character contribution
   - Record as `pattern-1-fixed-mapping.json`

2. **Pattern 3: No Character Prompting** (5 topics, 1 run each, same topics as Pattern 1)
   - Send same 5 models (assigned to characters, but no character brief)
   - Prompt: "We are running a debate on [topic]. Here is what others have said: [prior responses]. Please add your perspective."
   - Score on same rubrics
   - Record as `pattern-3-no-prompting.json`

3. **Pattern 4: Hybrid** (5 topics, 1 run each, same topics)
   - Use same fixed mapping as Pattern 1
   - BUT: character brief is tuned to amplify that model's natural tendencies
   - Example: To Llama (Maya): "You are Maya, Paranoid Realist. Catch hidden agendas and risks. What's being dismissed?"
   - Score, record as `pattern-4-hybrid.json`

4. **Comparative Analysis**: ANOVA or Kruskal-Wallis test across patterns. See [reference § Comparative Analysis](multi-model-committee-reference.md#pattern-2-random-model-character-assignment) for analysis code template.

5. **Qualitative Analysis**:
   - For each pattern, manually review 2–3 transcripts
   - Ask: Do arguments feel genuinely different, or theatrically different?
   - Does the debate reveal different blind spots?
   - Which character's contribution feels most authentic?

**Decision Gate**: Which pattern produces the best results (highest aggregate score)? Is the improvement worth the cost/complexity?

---

### Phase 3: Ablation & Optimization

**Goal**: Isolate the contribution of model diversity vs. character prompting; find optimal model-character assignments.

**Duration**: 2–3 weeks

**Procedure**:

1. **Ablation: Model Diversity**
   - Run Pattern 4 (hybrid) vs. Pattern 1 (fixed) multiple times on same topics
   - Does the specific model-character pairing matter, or just that there are different models?
   - Metric: variance in scores across runs using same pattern
     - High variance = model identity matters
     - Low variance = character prompting dominates

2. **Ablation: Character Prompting**
   - Run Pattern 3 (no prompting) vs. Pattern 1 (with prompting)
   - Does the character brief help or hinder authentic diversity?
   - Metric: do deliberations with character briefs converge to more stereotyped arguments?

3. **Optimization: Model-Character Permutations**
   - Run Pattern 4 (hybrid) with different model-character mappings
   - Identify which pairing produces strongest debate (highest adversarial rigor score)
   - Record as `optimization-matrix.json`

4. **Statistical Significance**:
   - For top 3 patterns, run 10 deliberations each on same topics
   - Compute confidence intervals on average rubric scores
   - Do confidence intervals overlap? (If not, difference is significant)

**Decision Gate**: Based on cost, complexity, and performance — which pattern should be production recommendation?

---

### Phase 4: Longitudinal Validation

**Goal**: Confirm that the chosen pattern produces consistent quality over time and across diverse topics.

**Duration**: Ongoing (3–6 months)

**Procedure**:

1. **Diverse Topic Set** (15–20 topics covering): Ethics, technical architecture, governance/policy, resource allocation, strategy/planning, failure analysis, uncertainty quantification
2. **Runs per Topic**: 3 deliberations per topic using chosen pattern (total: 45–60)
3. **Quality Metrics**: Mean score per rubric, std. dev., min/max, cross-rubric correlations
4. **Regression Analysis**: Does topic domain or complexity affect score? Which rubrics are weakest?
5. **Output**: `validation-report.md`

---

## Evaluation Framework

Uses the existing 5-rubric system (comprehensiveness, adversarial rigor, assumption coverage, reasoning depth, decision readiness), extended with **provenance tracking** (which model contributed to each rubric dimension) and **model-specific evaluation** (which models lead on which rubrics). See [reference § Evaluation Framework](multi-model-committee-reference.md#evaluation-framework) for schema details.

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **Coordination complexity overwhelms benefits** | Medium | High | Phase 2 testing; compare pattern complexity to score improvement |
| **API cost multiplication** | Low | Medium | Use parallel execution; negotiate volume discounts; use open-source models |
| **Inconsistent quality (weak model drags down debate)** | Medium | Medium | Implement model health checks; fallback to single-model; abort with grace |
| **Loss of "game within game"** | Low | Medium | Empirically test Pattern 3 vs. Pattern 1; single-model approach still available |
| **Model training cutoff creates "hallucinated facts"** | Medium | Low | Accept as part of model's perspective; add fact-checker role if needed |
| **Vendor lock-in to multiple APIs** | Medium | Medium | Prioritize open-source models (Llama); build abstraction layer for easy swaps |
| **Debate meanders without strong Chair** | Medium | Medium | Use explicit agenda; limit turn count; use model as Chair if needed |
| **Difference is statistically insignificant** | Medium | Low | Commit to Phase 3 ablation; accept if result is negative (single-model sufficient) |

---

## Recommendations

### Short-term (Phases 1–2: 4–6 weeks)

1. **Run baseline + profile studies** (Phase 1)
   - Establish single-model performance
   - Measure each model's natural personality biases
   - Investment: ~$50, ~20 hours

2. **Run Pattern 1 vs. Pattern 4 comparison** (Phase 2)
   - Use empirical profiles to assign models to characters
   - Compare fixed hybrid mapping vs. current single-model approach
   - Investment: ~$100, ~30 hours

3. **Decision point**: Does hybrid multi-model beat single-model on evaluation rubrics?
   - **If yes**: Proceed to optimization (Phase 3)
   - **If no**: Multi-model adds complexity without benefit; stick with single-model but document findings

### Medium-term (Phase 3: 2–3 weeks, if Phase 2 is positive)

4. **Run ablation studies** (Phase 3) — Investment: ~$150, ~40 hours
5. **Write decision memo**: Based on Phases 1–3, recommend which pattern should be standard practice

### Long-term (Phase 4: ongoing, if Phase 3 is positive)

6. **Longitudinal validation** — Track consistency and failure modes; refine based on live performance

---

## Conclusion

Multi-model committee deliberations represent a natural evolution of the Cyberneutics methodology, extending the principle of perspective diversity from the character level to the model level. The recommended path is:

1. **Phase 1–2** (~6 weeks): Establish baselines, run Pattern 4 (Hybrid) vs. single-model
2. **Decision gate**: Does hybrid improve over single-model? If yes, continue; if no, document and close
3. **Phase 3** (~3 weeks, if positive): Optimize model-character pairings, ablate components
4. **Phase 4** (ongoing): Longitudinal validation and production hardening

The output will be either a new standard for committee deliberations (if multi-model proves superior) or documented evidence that single-model simulation is sufficient. Either way, the methodology and infrastructure become reusable for future agent research.

---

## Reference Material

The full architectural analysis, model personality profiles, implementation code, orchestration strategies, cost calculations, open questions, and production checklist are in [multi-model-committee-reference.md](multi-model-committee-reference.md). Consult it for:

- **Architectural patterns**: Five patterns (Fixed Mapping, Random Assignment, Model-as-Model, Hybrid, Adversarial Selection) with trade-offs and code
- **Model profiles**: Detailed personality analysis of Claude, GPT-4o, Gemini, Llama, Mistral
- **Implementation**: Orchestrator code, API abstraction layer, context management strategies, error handling
- **Cost analysis**: Token-level and subscription-level cost comparison across patterns
- **Open questions**: 13 technical, architectural, operational, and evaluation unknowns
- **Connections**: Links to MOOLLM integration, multi-agent debate literature, residuality theory, Pask's conversation theory
