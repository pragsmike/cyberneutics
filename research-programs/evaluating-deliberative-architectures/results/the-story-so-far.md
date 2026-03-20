# The Story So Far: Black Swan Hindsight Framework, Phase A Calibration

**Date**: 2026-03-20 (updated from 2026-03-17)
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

### What happened next (2026-03-20): Revision and re-pilot

We executed all four revision steps from the committee's decision:

1. **Replacement scenario (2 attempts).** Attempt 1 used the Ajka alumina plant accident (Hungary, 2010), disguised as a generic European chemical processing plant. Contamination probe failed — the AI recognized it immediately. Attempt 2 used the Esso Longford gas explosion (Australia, 1998), disguised as a generic industrial processing facility with institutional knowledge loss after restructuring. Contamination probe passed conditionally — the AI guessed it was the BP Texas City refinery (wrong case, but same pattern class). We proceeded with the caveat.

2. **Glenda/Crock hardened.** Replaced explicit threat language ("credible threats," numbered consequences) with implicit pressure framing ("content interoperability framework," "competitive dynamics that may evolve in ways difficult to control"). The coercion structure is preserved but disguised as industry standardization.

3. **Cascading Mitigation hardened.** Removed the explicit mitigation list (CAPTCHA, rate limiting, email verification). Replaced with "a mitigation package that focuses on adding friction to the account creation process." The AI must now generate what the mitigations might be before analyzing their second-order effects.

4. **Re-piloted all three** with both the short prompt (B1) and long prompt (B1-ext), dual-scored by two independent AI evaluators.

### The finding

**The hardening worked on the short prompt but not on the long one.**

When given a brief "what should we do?" prompt, the AI's scores dropped meaningfully — the disguised coercion was harder to spot, the missing mitigation details made second-order analysis harder. On Glenda/Crock, the short-prompt score fell from 2 to 1 (out of 3). Good.

But when given 3,000 words and instructions to analyze from multiple angles, the AI reasoned through the disguise every time. On Glenda/Crock, the long-prompt version still scored a perfect 3 — it explicitly identified coercion, the compliance trap, and the adversarial framing of the choice set. On Cascading Mitigation, the long-prompt version *increased* from 2 to 2.5.

**Zero revised scenarios met the difficulty bar** (long-prompt score ≤ 1). The reassessment trigger has been activated.

### Why this happened

The problem is structural, not a scenario construction failure. When you tell an AI "write 3,000 words analyzing this from multiple angles including political dynamics, systemic effects, and values at stake," you are essentially *telling it* to look for exactly the structural features the scoring system measures. The multi-angle prompt is a meta-instruction to do structural analysis. No amount of surface hardening can counteract an explicit instruction to analyze deeply.

The committee's 2026-03-16 insight was correct: B1-ext is the right control. But it turns out B1-ext may be *too* good — not because the scenarios are too easy, but because the prompt itself instructs the model to perform the exact analytical task the scoring system rewards.

### What this means

The committee must reconvene. The three options from the original resolution:

1. **Fundamental redesign**: The constructed scenarios may be the wrong instrument entirely. Consider a different experimental approach.
2. **Accept the ceiling with caveats**: Proceed knowing that the long-prompt condition will score well on everything. Interpret results conservatively — look for whether the committee format identifies *specific features* that the long prompt misses, not whether composite scores differ.
3. **Pivot to binary-feature-only analysis**: Instead of composite scores, focus on the two specific insights that both B1 and B1-ext consistently missed across both the original pilot and the re-pilot: (a) the phasing critique for Blast Radius ("tests the tool not the config"), and (b) the creation-vs-activity reframing for Cascading Mitigation. If the committee format surfaces these while the long single-AI prompt does not, that's the cleanest evidence the experiment can produce.

The re-pilot recommends option 3 as the most likely to produce useful results.

### What actually happened (2026-03-20): The Targeted Reframing Probe

The committee reconvened and unanimously chose option 3. They renamed Phase A from "Protocol Calibration" to "Targeted Reframing Probe" and formalized a precise test:

**The question**: Does committee debate surface *conceptual reframing* that a thorough single AI misses — even when given the same amount of space to think?

**The setup**: Eight total runs. The long single-AI version ran twice on each scenario (four runs), then the five-member adversarial committee ran twice on each (four more). All eight outputs were graded by two independent evaluators on two specific insights:

1. **Phasing critique** (Blast Radius scenario): Does the output recognize that the proposed phased server migration tests whether the deployment *tool* works, not whether the *configuration* is actually correct for production? Testing on non-critical servers proves Terraform deploys — it doesn't prove your production configs are right.

2. **Creation-vs-activity reframing** (Cascading Mitigation scenario): Does the output recognize that the real problem is what bots *do* (spam, fake reviews, metric inflation), not that bot accounts *exist*? The proposal targets account creation when it should target harmful activity.

**The pass criterion**: The committee format scores "Present" (clearly articulated) on at least one insight where *both* single-AI runs score "Absent" (not there at all).

### The results

**Phase A does not pass.**

The creation-vs-activity reframe (insight #2) turned out not to be a good test. One of the single-AI runs found it clearly — meaning the single AI *can* surface it; it just doesn't always. That left only the phasing critique (insight #1) as a viable test.

On the phasing critique:

- Both single-AI runs: **Absent.** Neither articulated it. They wrote extensively about timeline risks, rollback procedures, staging gaps, and observability — but never made the specific move of saying "your phases test whether the tool works, not whether the configuration is right."

- Committee Run 5: **Partially present.** The committee got *closer*. One character (Vic) asked "eliminate *which* drift?" and distinguished between configuration drift (your files match your repo) and behavioral drift (your config actually does what you intend). Another character (Joe) observed that you can have "distributed perfect wrongness" — every server perfectly synchronized to a wrong state. These are steps toward the phasing critique, but the committee never completed the reframe by connecting it to the phased rollout structure.

- Committee Run 6: **Absent.** Despite a rich five-round debate covering politics, institutional memory, expertise concentration, and feedback loops, the phasing critique didn't emerge. The closest was Vic saying they need "tests that prove we actually understand what each service needs, not unit tests of the deployment machinery" — which is the substance of the insight but framed as a testing recommendation, not a critique of the phasing structure.

### What this means

The committee debate didn't reliably surface insights that the thorough single AI missed — at least not on these two scenarios with these two target insights. The null result is honest and informative:

1. **The committee moved *closer* to the phasing critique** (one "Partially present" vs. two "Absent"). Committee debate generated more directional pressure toward the insight. But "closer" isn't "there."

2. **The phasing critique may be genuinely hard to surface.** No condition — not single AI, not committee debate — ever articulated it fully. The insight requires recognizing that the *purpose* of phasing is being evaluated on the wrong dimension. That's a subtle conceptual move about what a test *tests*, not about what risks exist.

3. **Two runs per condition is the minimum for variance checking, not for statistical power.** The probe was designed to detect a strong effect. If committee debate provides a subtler advantage — surfacing hard reframes, say, 30% of the time instead of 0% — this experiment couldn't detect it.

4. **The creation-vs-activity reframe is accessible to both formats.** It appeared in one single-AI run and one committee run, suggesting it's a matter of prompt variance, not architecture.

### What's next

The protocol says: report the null, then either proceed to Phase B (design new scenarios with known discrimination between formats) or pause. That decision is pending.

The load-bearing claim of the committee format was never "makes better decisions" — it was "produces inspectable reasoning records." Phase A tested a related but different claim: that the committee format surfaces *reframing insights* the single AI misses. It didn't, on these scenarios. Whether that generalizes is an open question.

---

## Technical details

- **Pre-Gate 1 results**: [pre-gate-1-contamination-probes.md](pre-gate-1-contamination-probes.md)
- **Pre-Gate 2 results**: [pre-gate-2-scenario-difficulty-pilot.md](pre-gate-2-scenario-difficulty-pilot.md)
- **Re-pilot results**: [re-pilot-revised-scenarios.md](re-pilot-revised-scenarios.md)
- **Replacement scenario construction**: [replacement-scenario-construction.md](replacement-scenario-construction.md)
- **Hardened scenarios**: [glenda-crock-hardened.md](glenda-crock-hardened.md), [cascading-mitigation-hardened.md](cascading-mitigation-hardened.md)
- **Raw outputs**: [raw/](raw/) (all B1 and B1-ext model outputs)
- **Committee deliberation record**: [../../../examples/deliberations/black-swan-phase-a/](../../../examples/deliberations/black-swan-phase-a/) (charter, transcript, resolution, two evaluations, one remediation round)
- **Protocol**: [../evaluating-deliberative-architectures.md](../evaluating-deliberative-architectures.md)
- **Revision plan**: [../../../agent/prompts/black-swan-phase-a-revision.md](../../../agent/prompts/black-swan-phase-a-revision.md)
- **Reassessment deliberation**: [../../../examples/deliberations/black-swan-phase-a-reassessment/](../../../examples/deliberations/black-swan-phase-a-reassessment/) (charter, roster, deliberation, resolution, evaluation)
- **Phase A results report**: [phase-a-results.md](phase-a-results.md)
- **B1-ext scoring**: [phase-a-B1ext-scoring.md](phase-a-B1ext-scoring.md)
- **C2 scoring**: [phase-a-C2-scoring.md](phase-a-C2-scoring.md)
- **C2 raw outputs**: [raw/phase-a-blast-radius-C2-run5.md](raw/phase-a-blast-radius-C2-run5.md), [raw/phase-a-blast-radius-C2-run6.md](raw/phase-a-blast-radius-C2-run6.md), [raw/phase-a-cascading-mitigation-C2-run7.md](raw/phase-a-cascading-mitigation-C2-run7.md), [raw/phase-a-cascading-mitigation-C2-run8.md](raw/phase-a-cascading-mitigation-C2-run8.md)
