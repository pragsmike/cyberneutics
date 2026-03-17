# The Story So Far: Black Swan Hindsight Framework, Phase A Calibration

**Date**: 2026-03-17
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

### Decision: How to proceed (committee deliberation, 2026-03-17)

We ran our own methodology on the question. A five-member adversarial AI committee debated whether to proceed with the current scenarios or revise them first. The debate went through a full quality-control cycle: an independent review scored it, found gaps, sent it back for a second round of argument, and re-scored it.

The committee's most important finding had nothing to do with the original question. They realized we'd been asking the wrong thing. The question isn't "are these problems hard enough for a basic AI?" — it's "are they hard enough that a *thorough* single AI can't already solve them?"

Here's why that matters. In Test 2, we ran both a short version (basic prompt) and a long version (detailed 3,000-word analysis). The committee format will also produce long, detailed output — potentially thousands of words from five debating characters. If the committee scores better than the basic prompt, we won't know whether that's because committee debate genuinely surfaces better insights, or just because *writing more words* produces better analysis regardless of format. The long single-AI version is the real comparison — it matches the committee's word count without the debate structure.

So the new rule is: scenarios need to be hard enough that the long single-AI version still misses things. That's a harder bar than the original plan set, and it changes what "good enough" looks like.

**The decision:** Revise three scenarios (replace one that was recognized from real history, make two others harder), then re-test them against *both* the short and long single-AI versions. If at least one revised scenario is still hard enough after the long version takes its best shot, proceed to the full experiment. If none are hard enough, reconvene the committee to decide whether the experiment needs a more fundamental redesign.

The revision adds roughly 4–7 work sessions (about 15–25% overhead on the total experiment timeline). The committee judged this worth it: running the full experiment on scenarios that are too easy would produce results that look like "committee debate doesn't help" when the real answer might be "the test wasn't hard enough to tell."

### What happens next

1. **Build a replacement scenario** for the one the AI recognized (the Intel chip bug — too famous). We'll use an obscure case from a published business case collection, something a general-purpose AI is unlikely to have memorized. Two attempts maximum.
2. **Make two scenarios harder** with targeted edits — remove the clues that make the hidden structure too easy to spot.
3. **Re-test all three revised scenarios** with both the short and long single-AI versions. Grade them.
4. **Check the bar**: Does at least one scenario resist the long version? If yes, run the full experiment. If no, reassess.
5. **Run the full experiment**: Five different AI configurations on all five scenarios. The headline comparison is committee-debate vs. thorough-single-AI — controlling for effort, isolating whether the debate structure itself adds value.

---

## Technical details

- **Pre-Gate 1 results**: [pre-gate-1-contamination-probes.md](pre-gate-1-contamination-probes.md)
- **Pre-Gate 2 results**: [pre-gate-2-scenario-difficulty-pilot.md](pre-gate-2-scenario-difficulty-pilot.md)
- **Committee deliberation record**: [../../../situations/black-swan-phase-a/deliberations/](../../../situations/black-swan-phase-a/deliberations/) (charter, transcript, resolution, two evaluations, one remediation round)
- **Protocol**: [../evaluating-deliberative-architectures.md](../evaluating-deliberative-architectures.md)
- **First-run prompt**: [../../agent/prompts/black-swan-first-run.md](../../agent/prompts/black-swan-first-run.md)
