# Smoke test: Does cumulative confidence improve decision making?

This artifact defines a **comparison smoke test** to test whether using the metacognition register (cumulative confidence and accuracy across past runs) improves committee decision quality. The test compares two committee runs on the **same** topic: one without the register (baseline) and one with the register (committee instructed to weight or hedge by past calibration).

**Hypothesis:** When the committee (or synthesis) has access to past calibration data, the resulting resolution or deliberation quality will be at least as good and may be better (e.g. more nuanced weighting, explicit hedging where a character has been overconfident when wrong).

**Tiered recommendation and assumptions (per committee resolution, agent/deliberations/metacog-process-useful):** We recommend confidence at resolution; we recommend the register when running multiple committees; we *support* with-register and this comparison test as the way to test whether the register helps, but do not recommend with-register as default until we have at least three comparison runs showing benefit. We use **review sum** and **calibration-mentioned** as *proxies* for user benefit (unvalidated). **Register usage** by end users is unknown; primary consumers are the with-register run and maintainers; the sunset review will consider evidence of use. **Sunset trigger:** Deprecate with-register if fewer than 3 of the first 5 comparison runs show with-register ≥ baseline AND calibration mentioned in the resolution or transcript. Revisit at 12 months or 5 comparison runs, whichever comes first.

---

## Single prompt: run the full smoke test

You can run the entire smoke test (both committee runs, both reviews, and the comparison) with **one paste**. Replace the topic and slug if you want a different question.

**Prompt (copy and paste):**

```
Run the cumulative-confidence smoke test in one go.

Topic: Should we add a short glossary of key terms (e.g. 'fan', 'funnel', 'meta-d'') to the README or a dedicated doc?

1. (Optional) Run: python scripts/update_metacog_register.py
2. Run committee on this topic (no register). Use slug: readme-glossary. Record vote and confidence (1–4) per member in the resolution.
3. Run committee on the same topic with metacog register. Use slug: readme-glossary-with-register. Record vote and confidence.
4. Run /review on agent/deliberations/readme-glossary then /review on agent/deliberations/readme-glossary-with-register
5. Run: python scripts/compare_cumulative_confidence_runs.py agent/deliberations/readme-glossary agent/deliberations/readme-glossary-with-register -o agent/cumulative_confidence_comparison.md
6. Show me the comparison report (or the path to it) and a one-line interpretation: did using the register improve or match the baseline?
```

For a **different topic**, change the topic text and both slugs (e.g. topic "Should we X?" → slugs `should-we-x` and `should-we-x-with-register`).

---

## 1. Protocol summary

| Step | Action |
|------|--------|
| 1 | Ensure the metacog register has data: run `python scripts/update_metacog_register.py`. |
| 2 | Pick a **new** topic (not yet deliberated). Use a topic slug you will reuse with a suffix for the second run (e.g. `readme-glossary`). |
| 3 | Run committee on the topic **without** the register. Use slug `<topic-slug>` (e.g. `readme-glossary`). Record confidence (1–4) in the resolution. |
| 4 | Run committee on the **same** topic **with** the metacog register. Use slug `<topic-slug>-with-register` (e.g. `readme-glossary-with-register`). Invoke with "with metacog register" or "with cumulative confidence" so the skill injects the register summary and instructs the committee to take past calibration into account. Record confidence. |
| 5 | Run `/review` on both deliberation directories. |
| 6 | Run the comparison script: `python scripts/compare_cumulative_confidence_runs.py agent/deliberations/<topic-slug> agent/deliberations/<topic-slug>-with-register` |
| 7 | Interpret: compare review scores, and whether the with-register run mentions calibration or weights arguments by past validity. |

---

## 2. Committee "with register" mode

When you want the committee to use cumulative confidence in its synthesis:

- **Invoke with:** e.g. `/committee [same topic as baseline] with metacog register` or `... with cumulative confidence`. Use a slug that distinguishes the run: **`<topic-slug>-with-register`** (e.g. `readme-glossary-with-register`).
- **What the skill does:** Reads `agent/metacog_register.md` (if present). Adds to the charter **context** (or to a short "Metacog context" note in the charter) a summary of the register: e.g. "Past calibration (across prior runs): [per-character summary — who had high/low confidence accuracy]. Use this when synthesizing: weight or hedge recommendations by past calibration where relevant."
- **Deliverable:** The committee is instructed to take past calibration into account when forming the resolution (e.g. explicitly discount or hedge high-confidence claims from characters who have been overconfident when wrong in past runs, or weight well-calibrated characters more). The resolution and transcript may mention calibration, weighting, or veracity.

See `.claude/skills/committee/SKILL.md` for the exact "With cumulative confidence" subsection.

---

## 3. Comparison criteria

After both runs and both reviews:

| Criterion | How to check | What "improvement" could look like |
|-----------|----------------|-----------------------------------|
| **Review score (sum)** | Compare `transcript_review.sum` in 04-evaluation-1.md for baseline vs with-register. | With-register run has sum ≥ baseline (or both above threshold). |
| **Calibration-aware content** | In the with-register run, does 02-deliberation.md or 03-resolution.md mention calibration, past runs, veracity, weighting by validity, or the register? | At least one of: resolution summary, implementation plan, or transcript refers to past calibration or weighting. |
| **Verdict** | Compare `transcript_review.verdict` (High/Medium/Low). | With-register verdict is at least as high as baseline. |

The comparison script (`scripts/compare_cumulative_confidence_runs.py`) automates: reading both evaluation files, comparing sum and verdict, and scanning the with-register deliberation and resolution for calibration-related language. It writes a short report.

---

## 4. Interpreting the test

- **Positive signal:** With-register run has (a) review sum ≥ baseline, and (b) calibration or weighting mentioned in resolution/transcript. Suggests that feeding cumulative confidence into the process can improve or at least not harm decision quality, and that the committee uses the signal.
- **Null:** With-register sum ≈ baseline, little or no calibration language. Either the register didn’t change behavior or the topic didn’t give room for calibration to matter.
- **Negative:** With-register sum &lt; baseline. Possible confound: same topic twice can make the second run feel repetitive; review might penalize that. Run on a different topic or document the limitation.

This smoke test is **one comparison**; repeating on several topics would strengthen evidence.

---

## 5. Suggested test topic

Use a topic that is **new** (not in the register yet) and where character weighting could plausibly matter (e.g. values vs evidence tension):

**Topic:** "Should we add a short glossary of key terms (e.g. 'fan', 'funnel', 'meta-d'') to the README or a dedicated doc?"

**Slugs:** `readme-glossary` (baseline), `readme-glossary-with-register` (with register).

---

## 6. Files and scripts

- **Register:** `agent/metacog_register.md` (updated by `scripts/update_metacog_register.py`).
- **Comparison script:** `scripts/compare_cumulative_confidence_runs.py` — takes baseline and with-register deliberation dirs, compares review scores and checks for calibration language; writes a short report (stdout or file).
- **Smoke-test log:** `agent/cumulative_confidence_smoke_log.md` — append one row per run (date, topic slug, baseline sum, with-register sum, calibration Y/N) for aggregate evidence.
- **Committee skill:** `.claude/skills/committee/SKILL.md` — "With cumulative confidence" mode.

---

## 7. Quick reference: commands

```bash
# 1. Update register (optional but recommended)
python scripts/update_metacog_register.py

# 2. Run committee baseline (no register) — in chat: /committee [topic]
#    Use slug e.g. readme-glossary.

# 3. Run committee with register — in chat: /committee [same topic] with metacog register
#    Use slug readme-glossary-with-register (skill uses <slug>-with-register).

# 4. Review both — in chat: /review agent/deliberations/readme-glossary
#    then /review agent/deliberations/readme-glossary-with-register

# 5. Compare
python scripts/compare_cumulative_confidence_runs.py agent/deliberations/readme-glossary agent/deliberations/readme-glossary-with-register -o agent/cumulative_confidence_comparison.md
```

---

## 8. Optional extensions

- **Replication:** Run the same test on 2–3 more topics (different slugs) to see if with-register consistently matches or beats baseline.
- **Log:** Optionally append one row per run to `agent/cumulative_confidence_smoke_log.md` (topic, baseline sum, with-register sum, calibration Y/N) for aggregate evidence.

See also [Metacognition and committee veracity](metacognition-and-committee-veracity.md).
