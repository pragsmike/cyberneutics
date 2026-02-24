# Ablation Study: Component Contribution and Interaction Effects

**Status**: Not started  
**Runs**: (none yet)  
**Results**: [ablation-study/results/](ablation-study/results/)

This plan was extracted from the evaluation-schemes design (Design F). Full procedure, factor definitions, run budget, and results tabulation are below. The umbrella evaluation design and phase ordering remain in [evaluation-schemes.md](evaluation-schemes.md).

---

## Objective

Run the full pipeline and remove or vary components one at a time (and in a factorial subset) to measure each component's contribution and to test interaction effects (e.g. does the evaluation loop help only when both committee and scenarios are present?).

---

## Procedure

1. **Run full methodology** on N decisions (Committee + Scenarios + Deliberated Choice + Evaluation).

2. **Run ablations** (one-at-a-time removal):
   - **A1**: Committee only (no scenarios, no deliberated choice).
   - **A2**: Scenarios only (no committee debate, just scenario generation).
   - **A3**: Scenarios + simple resolution (no adversarial committee, just funnel without debate).
   - **A4**: Scenarios + committee (no evaluation loop).
   - **A5**: Committee without Robert's Rules structure (just free-form debate).

3. **Evaluate all versions** using Dimensions A–F (see [evaluation-schemes.md](evaluation-schemes.md) for codebooks).

4. **Compute contribution**: marginal improvement from adding each component; optional factorial analysis for interactions.

5. **Analyze**: Which components contribute most? Which are optional? Interaction effects?

---

## Factor definitions (for information-maximizing design)

Binary factors for structured analysis:

| Factor | On (1) | Off (0) |
|--------|--------|--------|
| **S** Scenarios | Fan (scenario generation) | No scenarios |
| **C** Committee | Adversarial committee debate | No committee |
| **D** Deliberated choice | Fan→funnel composition | Simple resolution |
| **E** Evaluation loop | Review/evaluation step | No evaluation loop |
| **R** Robert's Rules | Structured procedure | Free-form debate |

Full methodology = S=1, C=1, D=1, E=1, R=1. Deliberated choice (D) is only meaningful when S=1.

**Recommended design for interactions**: Fix D=1 and run a 2³ factorial on (S, C, E) to estimate main effects and two-way interactions (S×C, S×E, C×E). Run R as a single ablation at full methodology (R=1 vs R=0). Baseline: S=0, C=0 for reference.

---

## Run budget

- **N decisions**: ≥ 8 (ideally 10–15); same set across all conditions.
- **Conditions**: Baseline + one-at-a-time ablations A1–A5; or (if factorial) baseline + 8 (S,C,E) cells + 2 for R.
- **Repeats**: 2 runs per (decision, condition) to estimate variance and CIs.
- **Raters**: Same Dimensions A–F, same rater pool, blind to condition; see evaluation-schemes for codebooks and inter-rater reliability.

---

## Results tabulation

After each run, populate the following and store in [ablation-study/results/](ablation-study/results/) (e.g. `results/YYYY-MM-run1.md` or `results/component-contribution-table.csv`).

### Table 1 — Condition × Dimension scores

| Condition | A (Assumptions) | B (Trade-offs) | C (Falsifiability) | D (Diversity) | E (Reasoning) | F (Robustness) | Cost (optional) |
|-----------|-----------------|----------------|-------------------|---------------|---------------|----------------|-----------------|
| Baseline  | mean [95% CI]   | …              | …                 | …             | …             | …              | time/tokens     |
| A1        | …               | …              | …                 | …             | …             | …              | …               |
| A2 … A5   | …               | …              | …                 | …             | …             | …              | …               |
| Full      | …               | …              | …                 | …             | …             | …              | …               |

- **Rows**: Conditions (baseline, A1–A5, full; or factorial labels).
- **Cells**: Mean score and 95% CI, e.g. `3.2 [2.8–3.6]`.
- **Cost**: Optional column for person-hours or tokens per condition.

### Table 2 — Component contribution

| Component            | Dimension (or composite) | Effect size (Δ or Cohen's d) | 95% CI | Conditional on (optional) |
|----------------------|--------------------------|------------------------------|--------|----------------------------|
| Scenarios            | A, B, … or composite    | e.g. +0.4                    | …      | —                          |
| Committee            | …                       | …                             | …      | —                          |
| Deliberated choice   | …                       | …                             | …      | S=1                        |
| Evaluation loop      | …                       | …                             | …      | e.g. S=1 & C=1             |
| Robert's Rules       | …                       | …                             | …      | Full pipeline              |

- **Conditional on**: Note when a component’s effect is only estimated in a subset (e.g. “E only when S=1 & C=1”).

### Table 3 — Interactions (if factorial run)

| Interaction | Dimension or composite | Estimate | 95% CI | Brief interpretation |
|-------------|------------------------|----------|--------|------------------------|
| E×C         | e.g. A, composite      | …        | …      | e.g. E helps more when C=1 |
| E×S         | …                      | …        | …      | …                        |
| S×C         | …                      | …        | …      | …                        |

### Cost–benefit summary

| Component            | Cost (person-hours or tokens) | Benefit (score Δ or effect size) | Note                |
|----------------------|--------------------------------|-----------------------------------|----------------------|
| Scenarios            | …                              | …                                 |                      |
| Committee            | …                              | …                                 |                      |
| Deliberated choice   | …                              | …                                 |                      |
| Evaluation loop      | …                              | …                                 | Flag if high-cost/low-benefit |
| Robert's Rules       | …                              | …                                 |                      |

- Flag components that are high-cost and low-benefit for discussion.

---

## Expected output

- Component contribution table (Table 2) with effect sizes.
- Insight statements, e.g. "Committee debate contributes +X% to perspective diversity; Robert's Rules contribute additional +Y%."
- Cost–benefit summary: is the evaluation loop worth it if it adds +10% but doubles runtime?
- If factorial: interaction report (Table 3).

---

## Strengths

- Answers the practical question: "Do we need all of this?"
- Cheaper than full comparison (variants of the methodology only, not external baselines).
- Diagnostic: tells you where to invest effort when improving the methodology.

---

## Weaknesses

- Only tests **within** methodology, not against baselines. All variants may beat a simple prompt equally.
- Some components may have non-linear effects (e.g. removing Robert's Rules may break the whole structure).

---

## Timeline

3–4 weeks (generate outputs, rate, analyze). See [evaluation-schemes.md](evaluation-schemes.md) resource table for person-hours.
