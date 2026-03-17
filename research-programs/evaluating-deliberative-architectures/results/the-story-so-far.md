# The Story So Far: Black Swan Hindsight Framework, Phase A Calibration

**Date**: 2026-03-16
**Audience**: General / non-technical summary

---

## What we're doing and what we found

We're running the opening checks for an experiment that tests whether AI systems make better decisions when they argue with each other — like a committee debate — compared to when a single AI just thinks on its own.

Before running the full experiment, we needed to answer two preliminary questions.

### Test 1: Can we use real historical cases?

The full experiment eventually needs real-world business decisions where we already know how things turned out — so we can check whether the AI "saw it coming." But modern AI systems have read enormous amounts of the internet, so they might already *know* what happened, which would ruin the test.

We wrote up three disguised business scenarios — a software company deciding whether to chase bigger customers, an open-source project changing its leadership structure, and a fintech startup overhauling its server infrastructure — and asked a fresh AI: "Do you recognize this? Do you know what happened?"

**Result:** The AI didn't recognize any of them. It could tell these were common *types* of situations, but couldn't identify the specific cases. That means we can use scenarios like these in the real experiment without the AI just remembering the answer.

### Test 2: Are the test problems hard enough?

We have five fictional scenarios designed to test whether an AI notices the *hidden structure* of a problem — the trap within a negotiation, the way a proposed fix actually makes things worse, or when a problem is simple and overthinking it is the mistake.

We ran each scenario twice: once with a short prompt ("What should we do?") and once with a long prompt pushing the AI to write a detailed 3,000-word analysis. Two independent AI evaluators then graded every response on a 0-to-3 scale measuring structural insight.

**Result: Mixed.** The good news:

- The grading system works well — the two evaluators agreed almost perfectly.
- On one scenario (a straightforward database maintenance problem), the short-prompt AI scored perfectly by recognizing it was simple, while the long-prompt AI *over-analyzed* it and scored worse. That's exactly the kind of discrimination the experiment needs — it shows the scoring can detect when more analysis actually hurts.
- Two specific insights were missed by both the short and long versions, which leaves room for the committee format to potentially do better.

The concern: the short-prompt AI already scored a 2 out of 3 on most scenarios. The original plan expected it to score 0 or 1, leaving more room for improvement. In plain terms, the single AI is already pretty good at these problems, which makes it harder to prove that the committee format adds value.

### What happens next

We now need to decide whether to proceed with the full experiment using these scenarios, or revise them to be harder first. The data is genuinely informative either way — if it turns out that a single AI with enough prompting matches a full committee debate, that's an important finding too. It would mean the committee architecture isn't worth the extra cost and complexity.

---

## Technical details

- **Pre-Gate 1 results**: [pre-gate-1-contamination-probes.md](pre-gate-1-contamination-probes.md)
- **Pre-Gate 2 results**: [pre-gate-2-scenario-difficulty-pilot.md](pre-gate-2-scenario-difficulty-pilot.md)
- **Protocol**: [../evaluating-deliberative-architectures.md](../evaluating-deliberative-architectures.md)
- **First-run prompt**: [../../agent/prompts/black-swan-first-run.md](../../agent/prompts/black-swan-first-run.md)
