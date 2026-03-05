# Multi-Model Committee: Build-Out Plan

**Status**: Proposed
**Parent program**: [multi-model-committee.md](../multi-model-committee.md)
**Orchestrator**: [pcrit-llm](https://github.com/pragsmike/pcrit-llm) (Clojure, via LiteLLM proxy)

> This document turns the four-phase experimental protocol in
> [multi-model-committee.md](../multi-model-committee.md) into a concrete
> implementation plan centered on pcrit-llm. It specifies what code to write,
> what data to collect, and what decisions each phase gates.

---

## Phase 0 — Infrastructure (1 week)

**Goal**: Get pcrit-llm, LiteLLM, and at least two provider API keys running
together; prove the round-trip works.

### Tasks

1. **LiteLLM proxy setup**
   - Deploy LiteLLM locally (Docker or pip).
   - Configure at least two providers (Anthropic + OpenAI).
   - Validate with `curl` that `openai/gpt-4o` and `anthropic/claude-sonnet-4-5`
     both return completions through the single proxy endpoint.

2. **pcrit-llm validation**
   - Run `pcrit.llm.core/pre-flight-checks` against the proxy.
   - Call `call-model` for each configured provider; confirm `generation-metadata`
     (token counts, cost, latency, provider) returns correctly.

3. **Orchestrator namespace** — `pcrit.committee.orchestrator`
   - **Input**: a topic string, a roster map (`{character-name model-name}`),
     a round count, and an optional character-briefs map.
   - **Loop**: for each round, for each character in the roster, call
     `call-model` with the character's model, passing the accumulated
     transcript as context and the character brief (if any) as system prompt.
   - **Output**: a deliberation record — a vector of round maps, each
     containing per-character response text plus `generation-metadata`.
     Also a summary map with aggregate token counts and total cost.
   - **Concurrency**: rounds are sequential (each builds on prior context);
     characters within a round may be called concurrently (pmap) since they
     see the same transcript snapshot.
   - Write a `format-transcript` function that renders the deliberation
     record into the same markdown format the `/committee` skill uses
     (00-charter through 03-resolution), so results are directly comparable.

4. **Smoke test**
   - Run one 3-round deliberation on a throwaway topic ("Should this project
     use tabs or spaces?") with 2 models and 2 characters.
   - Confirm: transcript renders correctly, `generation-metadata` is present
     on every turn, total cost is computed.

### Deliverables

- Working LiteLLM proxy with ≥2 providers
- `pcrit.committee.orchestrator` namespace (source + tests)
- Smoke-test transcript saved to `results/phase-0/smoke-test.md`

### Decision gate

Can pcrit-llm reliably route to multiple providers and return cost metadata?
If yes, proceed. If not, debug the proxy or library before continuing.

---

## Phase 1 — Baseline + Model Profiles (1–2 weeks)

**Goal**: Establish single-model performance and profile each model's natural
tendencies; determine whether models are sufficiently different to justify
the multi-model hypothesis.

### Tasks

1. **Select 5 topics** spanning: ethics, technical architecture, governance,
   resource allocation, strategy. Prefer topics already used in prior
   cyberneutics deliberations for comparability.

2. **Single-model baseline** (5 topics × 1 run each)
   - Run standard single-model deliberations using the orchestrator with
     every character mapped to the same model (e.g., all Claude).
   - Score each on the 5 existing rubrics (comprehensiveness, adversarial
     rigor, assumption coverage, reasoning depth, decision readiness).
   - Save as `results/phase-1/baseline-single-model.json`.

3. **Model personality profiles** (5 topics × N models, no deliberation)
   - For each topic, send to each available model (Claude, GPT-4o, Gemini,
     Llama, Mistral — whatever is configured) a bare prompt:
     "Please respond to this topic: [topic]. What's your perspective?"
   - No character roleplay, no prior context.
   - Analyze each response for: length, hedging score, confidence, evidence
     count, risk mentions, value mentions, sentiment, logical structure,
     novelty of framing.
   - Save as `results/phase-1/model-profiles.json`.

4. **Analysis**
   - Compute per-model averages across topics for each dimension.
   - Visualize as a radar chart or heatmap.
   - Write `results/phase-1/phase-1-report.md` summarizing findings.

### Deliverables

- `results/phase-1/baseline-single-model.json`
- `results/phase-1/model-profiles.json`
- `results/phase-1/phase-1-report.md`

### Decision gate

Do model profiles show meaningfully different personality signatures
(e.g., ≥1 standard deviation on ≥2 dimensions)? If yes, the hypothesis
that different models bring genuine diversity is supported; proceed to
Phase 2. If no, document the finding and consider closing the program
(single-model may be sufficient).

---

## Phase 2 — Comparative Architectures (2–4 weeks)

**Goal**: Run the same topics through three multi-model patterns and compare
against the single-model baseline.

### Tasks

1. **Pattern 1: Fixed Mapping** (5 topics × 1 run each)
   - Assign models to characters based on Phase 1 profiles. The mapping
     should pair each character's intended role with the model whose
     natural tendencies best match:
     - Maya (Paranoid Realist) → model with highest risk-mention score
     - Frankie (Values Advocate) → model with highest value-mention score
     - Vic (Evidence Synthesizer) → model with highest evidence count
     - Tammy (Cross-Domain Linker) → model with broadest framing
     - Joe (Chair) → model with best coherence/summary scores
   - Run full deliberation via orchestrator. Score on 5 rubrics.
   - Save as `results/phase-2/pattern-1-fixed-mapping.json`.

2. **Pattern 3: No Character Prompting** (5 topics × 1 run each, same topics)
   - Same model assignments as Pattern 1, but no character briefs.
   - Prompt: "We are running a debate on [topic]. Here is what others have
     said: [prior responses]. Please add your perspective."
   - Score on same rubrics.
   - Save as `results/phase-2/pattern-3-no-prompting.json`.

3. **Pattern 4: Hybrid** (5 topics × 1 run each, same topics)
   - Same model assignments as Pattern 1.
   - Character briefs are tuned to *amplify* each model's natural
     tendencies (e.g., to the high-risk model playing Maya: "You are Maya,
     Paranoid Realist. Catch hidden agendas and risks.").
   - Score on same rubrics.
   - Save as `results/phase-2/pattern-4-hybrid.json`.

4. **Statistical comparison**
   - ANOVA or Kruskal-Wallis across: baseline, Pattern 1, Pattern 3, Pattern 4.
   - Compute effect sizes (Cohen's d) for each rubric dimension.
   - Write `results/phase-2/phase-2-report.md`.

5. **Qualitative review**
   - Manually review 2–3 transcripts per pattern.
   - Guiding questions: Do arguments feel genuinely different or theatrically
     different? Does the debate reveal different blind spots? Which character's
     contribution feels most authentic?

### Deliverables

- `results/phase-2/pattern-{1,3,4}-*.json`
- `results/phase-2/phase-2-report.md`

### Decision gate

Does any multi-model pattern statistically improve over single-model on
aggregate rubric scores? Is the improvement large enough to justify the
added cost and complexity? If yes, proceed to Phase 3 with the best
pattern. If no, document and close — single-model is sufficient.

---

## Phase 3 — Ablation & Optimization (2–3 weeks, if Phase 2 positive)

**Goal**: Isolate the contribution of model diversity vs. character prompting;
find optimal model→character assignments.

### Tasks

1. **Ablation: model diversity**
   - Run the best Phase 2 pattern multiple times (5 runs per topic).
   - Compare score variance: high variance → model identity matters;
     low variance → character prompting dominates.

2. **Ablation: character prompting**
   - Compare Pattern 3 (no prompting) vs. Pattern 1 (with prompting)
     statistically across the expanded run set.
   - Do character briefs help or hinder authentic diversity?

3. **Optimization: model→character permutations**
   - For the top pattern, try alternative model→character mappings
     (e.g., swap the model for Maya and Vic).
   - Identify which pairing produces the strongest debate (highest
     adversarial rigor).
   - Save as `results/phase-3/optimization-matrix.json`.

4. **Statistical significance**
   - For the top 3 configurations, run 10 deliberations each.
   - Compute 95% confidence intervals on mean rubric scores.
   - Determine whether confidence intervals overlap.

5. **Decision memo**
   - Write `results/phase-3/decision-memo.md` recommending the production
     pattern, with cost/quality/complexity analysis.

### Deliverables

- `results/phase-3/optimization-matrix.json`
- `results/phase-3/decision-memo.md`

### Decision gate

Based on cost, complexity, and performance — which pattern should be the
production recommendation? Output is a clear recommendation with evidence.

---

## Phase 4 — Longitudinal Validation (ongoing, 3–6 months)

**Goal**: Confirm that the chosen pattern produces consistent quality over
time and across diverse topics.

### Tasks

1. Expand to 15–20 topics across 7 domains: ethics, technical architecture,
   governance/policy, resource allocation, strategy/planning, failure
   analysis, uncertainty quantification.
2. 3 deliberations per topic using the chosen pattern (45–60 total runs).
3. Track: mean score per rubric, std dev, min/max, cross-rubric correlations.
4. Regression analysis: does topic domain or complexity affect score?
5. Monitor cost trends as model pricing changes.
6. Feed findings back into evaluation-schemes and ablation-study programs.

### Deliverables

- `results/phase-4/validation-report.md`
- Updated recommendations in parent program doc

---

## Cross-Cutting: pcrit-llm Enhancements

These enhancements should be built incrementally as the phases progress,
not as a separate up-front effort.

| Enhancement | Needed by | Description |
|-------------|-----------|-------------|
| `pcrit.committee` namespace | Phase 0 | Orchestrator, transcript formatter, roster parser |
| Aggregate cost summary | Phase 1 | Function that summarizes `generation-metadata` across an entire deliberation: total tokens in/out, total cost, cost per character, cost per round |
| Rubric scoring helpers | Phase 1 | Functions to score a transcript against the 5-rubric framework, returning structured data for statistical analysis |
| Ollama endpoint docs | Phase 2 | Document how to point pcrit-llm at Ollama for open-weight model experiments (may already work; verify and document) |
| Concurrent character calls | Phase 2 | Use `pmap` or `core.async` for within-round parallelism; measure latency improvement |
| Result serialization | Phase 1 | Standard JSON schema for deliberation results (transcript + metadata + scores) to enable cross-phase comparison |

---

## Cost Estimate

| Phase | API calls (approx) | Estimated cost | Hours |
|-------|-------------------|----------------|-------|
| 0 | ~20 | $5 | 10 |
| 1 | ~50 | $50 | 20 |
| 2 | ~75 | $100 | 30 |
| 3 | ~200 | $150 | 40 |
| 4 | ~180 | $200 | 60 |
| **Total** | **~525** | **~$505** | **~160** |

Costs assume a mix of frontier models (Claude Opus/Sonnet, GPT-4o) and
mid-tier models (GPT-4o-mini, Gemini Flash). Open-weight models via Ollama
reduce marginal cost to near zero for phases that use them.

---

## Related

- [../multi-model-committee.md](../multi-model-committee.md) — the experimental protocol this plan implements
- [reference.md](reference.md) — architectural patterns, model profiles, implementation code, cost analysis
- [../committee-implementation-taxonomy.md](../committee-implementation-taxonomy.md) — design space; this program is Tier 3
- [pcrit-llm](https://github.com/pragsmike/pcrit-llm) — the Clojure orchestration library
- [pcrit-llm USAGE.md](../../../../pcrit-llm/USAGE.md) — library usage guide
