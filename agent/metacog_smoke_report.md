# Metacognition smoke test report

Compares three committee deliberations chosen to elicit variation in confidence, and summarizes how **confidence relates to accuracy** (metacognition impact on committee decision making).

**What this is for:** Metacognition helps the *end user* interpret and weight the committee's advice when making their own decision (e.g. whose confidence to trust). It does not change or improve the committee's decision itself.

## Topics (run /committee on each with confidence recorded)

- **quickstart-one-page**: Should we add a one-page Quickstart that gets someone to their first committee run in under 10 minutes, even if it skips some nuance?
- **default-roster-5-vs-3**: Should the default committee run use the full 5-member roster, with a documented 'quick' 3-member variant as optional (rather than 5 as the only default)?
- **readme-when-not-to-use**: Should we add a short 'When not to use this methodology' section to the README (e.g. don't use for X, Y, Z) even if it might make the project look narrow or defensive?

---

## Per-topic summary

| Topic | Resolution | Aye | Nay | Confidence (mean ± sd) | Accuracy |
|-------|------------|-----|-----|------------------------|----------|
| quickstart-one-page | Aye | 4 | 1 | 3.4 ± 0.49 (range 3-4) | 80.0% |
| default-roster-5-vs-3 | Aye | 4 | 1 | 3.4 ± 0.49 (range 3-4) | 80.0% |
| readme-when-not-to-use | Aye | 5 | 0 | 3.0 ± 0.63 (range 2-4) | 100.0% |

---

## Metacognition impact (confidence vs accuracy)

- **High confidence (3–4):** 14 votes, **85.7%** correct.
- **Low confidence (1–2):** 1 votes, **100.0%** correct.

When members were less confident, they were more often aligned with the resolution (overconfidence when wrong).

---

## HMeta-d inputs (pooled across all three topics)

For hierarchical meta-d' (e.g. `fit_meta_d_mcmc` in [HMeta-d](https://github.com/metacoglab/HMeta-d)):

```
nR_S1 = [4, 8, 1, 0, 0, 0, 0, 0]
nR_S2 = [0, 0, 0, 0, 0, 0, 1, 1]
```

See `artifacts/metacognition-and-committee-veracity.md` and `scripts/build_metacog_counts.py --per-character` for per-character efficiency across runs.
