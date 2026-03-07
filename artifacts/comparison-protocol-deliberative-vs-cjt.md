# Comparison Protocol: Deliberative Committee vs. CJT-Style Independent Vote

This protocol defines how to run and compare two pipelines on the **same** question:

1. **Deliberative (current)** — Characters see the question, see each other's arguments, debate, then produce a resolution and votes. Implemented by the `/committee` skill.
2. **CJT-style (independent aggregation)** — Each character responds to the question **without** seeing the others' responses; responses are then **aggregated** (e.g. majority vote). This approximates Condorcet's jury theorem conditions (independent judgments, then aggregate).

See [Condorcet's Jury Theorem and the Committee](condorcet-jury-theorem-and-committee.md) for why these are different pipelines.

---

## When to use this protocol

- To test whether outcomes differ between deliberative and independent-aggregation on the same topic.
- To gather evidence for or against "CJT-style aggregation vs. deliberation" (as noted in the Condorcet artifact: if evidence emerges from comparison, we can revisit).

---

## Requirements

- **Same question** for both pipelines. For a clean comparison, use a **binary or categorical** question so the CJT-style pipeline can produce a clear aggregate (e.g. Aye/Nay majority).
- **Same roster** (e.g. the five characters from `agent/roster.md`).
- **Same charter context** (goal, context, success criteria) so both pipelines see the same framing.

---

## Pipeline A: Deliberative

1. Run `/committee [question]` (or `/committee quick [question]`) with the chosen topic and context.
2. Record the deliberative output in `<situation-dir>/deliberations/` (00-charter, 02-deliberation, 03-resolution).
3. From the resolution, extract: **outcome** (PASSED/DEFERRED/NO_CONSENSUS), **decision** (one line), and **votes** (per character: Aye/Nay/Abstain).
4. Optional: run `/review --situation <path-to-situation-dir>` and record the rubric sum.

---

## Pipeline B: CJT-style (independent vote)

1. **Isolation:** For each roster member, generate exactly one response: "You are [character]. Here is the question and context. Give your vote: **Aye** or **Nay** (or Abstain). Then give one short paragraph rationale. You have not seen and must not reference any other character's response."
2. **No cross-reading:** Each character's response must be produced without access to the others' responses. (In practice: separate prompts or one batch with strict instruction that each response is written in isolation.)
3. **Aggregation:** Collect the five votes. Compute majority (Aye vs Nay; treat Abstain as no vote). If tie, record as tie.
4. **Record:** Save the five independent rationales and the aggregate result in a dedicated study directory (for example `research-programs/<study>/results/<topic-slug>/` or another explicit workspace outside `agent/`).

---

## Comparison

| Dimension | Deliberative | CJT-style |
|-----------|--------------|-----------|
| **Output** | Resolution + decision-space map + per-character votes | Aggregate vote (e.g. majority) + five independent rationales |
| **Independence** | No (deliberation creates dependence) | Yes (by design) |
| **Stress-testing** | Yes (characters challenge each other) | No (no cross-reading) |
| **Interpretation** | Map of tensions, assumptions, trade-offs | Single collective verdict under CJT-like conditions |

**Compare:**

- Do the **outcomes** agree (e.g. both Aye, or both Nay)?
- How do the **rationales** differ? (Deliberative: refined by debate. CJT-style: raw, unrefined by others.)
- If you run both on several topics, do deliberative and CJT-style agree more often than not? Disagree on which kinds of questions?

---

## Limitations

- **Independence in practice:** In a single chat or API session, true independence is hard to guarantee (the same model generates all five; it may implicitly "remember" earlier outputs). Best effort: separate calls or strict isolation instructions.
- **Binary vs. rich:** Deliberative output is a map and a resolution; CJT-style output is a vote. Comparing them is not apples-to-apples on "quality" unless you define a common rubric (e.g. "usefulness for the user" or "reasoning completeness" applied to both).
- **One run each:** A single run per pipeline is only a datapoint. Multiple runs on the same question (or many questions) would strengthen evidence.

---

## Where to store comparison runs

Runs that are part of the **condorcet-comparison research program** live in [research-programs/condorcet-comparison/results/](../research-programs/condorcet-comparison/results/). The first two runs (second-ci-job and code-of-conduct, 2026-02-22) are stored there.

For **future runs** not yet assigned to a research program, keep the comparison in an explicit study workspace rather than under `agent/`. Two good options are:

- `research-programs/<study>/results/<topic-slug>/` when the run is part of a tracked study
- a dedicated situation or experiment workspace that stores the deliberative record, the CJT-style votes, and the comparison summary together

A minimal comparison record should include:

- `00-charter.md` - shared question and context
- `01-deliberative/` - copy or link to the relevant `<situation-dir>/deliberations/` record when applicable
- `02-cjt-style-votes.md` - five independent rationales and votes
- `03-cjt-style-result.md` - aggregate result
- `04-comparison-summary.md` - outcome agreement and notes on differences

The key rule is simple: do not use `agent/` as runtime storage for new comparison runs.