# Metacognition register

Tracks confidence and accuracy **across committee runs** to support the end user (who to weight when interpreting advice). Does not change the committee's decision. Updated by `scripts/update_metacog_register.py`.

**Last updated:** 2026-02-24

## Deliberations included

- default-roster-5-vs-3
- example
- quickstart-one-page
- readme-glossary
- readme-glossary-with-register
- readme-when-not-to-use

---

## Per-character summary (across runs)

| Character | Trials | Correct | High conf (3–4) acc % | Low conf (1–2) acc % |
|-----------|--------|---------|------------------------|------------------------|
| Frankie | 6 | 6 (100%) | 100.0% (n=5) | 100.0% (n=1) |
| Joe | 6 | 5 (83%) | 83.3% (n=6) | 0.0% (n=0) |
| Maya | 6 | 5 (83%) | 75.0% (n=4) | 100.0% (n=2) |
| Tammy | 6 | 6 (100%) | 100.0% (n=5) | 100.0% (n=1) |
| Vic | 6 | 6 (100%) | 100.0% (n=5) | 100.0% (n=1) |

---

## Committee-wide (pooled)

- **Total trials:** 30
- **Overall correct:** 28 (93.3%)
- **High confidence (3–4):** 25 votes, **92.0%** correct.
- **Low confidence (1–2):** 5 votes, **100.0%** correct.

### HMeta-d inputs (pooled)

For `fit_meta_d_mcmc` in [HMeta-d](https://github.com/metacoglab/HMeta-d):

```
nR_S1 = [7, 16, 5, 0, 0, 0, 0, 0]
nR_S2 = [0, 0, 0, 0, 0, 0, 1, 1]
```

For per-character efficiency use `python scripts/build_metacog_counts.py agent/deliberations --per-character` and `fit_meta_d_mcmc_group` in HMeta-d.
