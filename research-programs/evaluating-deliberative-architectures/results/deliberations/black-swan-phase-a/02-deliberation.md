# Phase 2: Deliberation

**Topic**: How should we proceed on the Black Swan Hindsight Framework Phase A after mixed pre-gate results?
**Protocol**: Robert's Rules (modified for adversarial committee)
**Date**: 2026-03-16

---

## Opening Statements

### Maya (Paranoid Realism)

Let me start with something nobody wants to hear: the recommendation in the pilot report to "proceed with caveats" is the researcher advocating for their own sunk costs. The protocol was designed with a strict decision rule for a reason — to prevent exactly this kind of motivated reasoning. The rule says 3+ scenarios at B1 ≤ 1. We got 1. That's not a marginal miss; it's a categorical failure.

Now ask yourself: who benefits from proceeding as-is? The person who already invested in constructing these scenarios and running ten pilot sessions. Who benefits from revision? The research program's credibility when it eventually faces external scrutiny. The pilot report itself admits the scenarios are "too easy for frontier LLMs in their current form." If Phase A produces a null result — committee architectures don't outperform simple prompts — we won't know whether that's because the methodology doesn't work or because the test was too soft. That ambiguity serves nobody.

I also want to flag something about the "caveats" framing. Once you proceed "with caveats," those caveats become footnotes in the calibration report that nobody reads. The finding becomes "Phase A showed no significant discrimination" and the caveat becomes "but the scenarios were acknowledged to be too easy." That's exactly the kind of result that kills a research program — not wrong, but uninterpretable.

### Frankie (Idealism / Values Guardian)

Maya's right that motivated reasoning is a risk, but she's wrong about where it leads. The purpose of this research program is to build evidence for whether deliberative architectures add genuine value. That's the mission. Revision for the sake of methodological purity can itself become a form of procrastination — endlessly perfecting the instrument while never running the experiment.

Consider what we already have. The scoring system works beautifully — 10/10 reliability. The Deliberation-Neutral scenario produced the strongest discrimination signal in the entire pilot, and it ran against the general effort advantage. Two specific structural features (phasing critique, creation-vs-activity reframing) were missed by both B1 and B1-ext. These are exactly the discrimination points we need for C2 and C3 to demonstrate value.

The deeper question is: what is Phase A actually for? It's calibration, not evidence for the core claim. The protocol says so explicitly. If Phase A tells us "the scenarios are easy enough that B1 already performs well, but here are specific structural features where committee architectures add value," that's a perfectly valid calibration finding. It shapes how we design Phase B. Refusing to run Phase A until every scenario is perfectly tuned misunderstands the purpose of calibration — you're supposed to learn from imperfect instruments, not wait for perfect ones.

### Joe (Continuity Guardian)

I've seen this pattern before in research programs: early results are promising but ambiguous, the team debates whether to refine or proceed, and the debate itself becomes the bottleneck. The research stalls not because of bad data but because of indecision.

But I've also seen the opposite failure: proceeding with known instrument problems, getting uninterpretable results, and then having to re-run everything anyway. That's strictly worse — you've spent the time AND you have nothing to show for it.

The specific history here matters. The protocol was written with the strict decision rule before any runs happened. That rule represents the researcher's prior judgment about what constitutes a viable test. Post-hoc rationalization of why the rule doesn't apply is exactly the kind of thing Pre-Gate 2 was designed to catch. The rule caught it. Respect the rule.

However — and this is important — the rule applies to the scenario *set*, not to every individual scenario. The externally-sourced scenario is clearly broken (model recognized Intel FDIV). If we replace that one scenario and it comes in at B1 ≤ 1, we'd have 2 of 5 at threshold. Still below 3, but closer. And if we also harden one of the 2-scoring scenarios, we could plausibly get to 3 of 5. That's a targeted revision, not a full redesign. The question is whether targeted revision is worth the delay.

### Vic (Evidence Prosecutor)

Let me be precise about what the data actually says, because both Maya and Frankie are cherry-picking.

The strict rule failed: 1 of 5 at B1 ≤ 1. That's a fact. But the rule's threshold of 3+ was set without empirical calibration — it was a guess about how hard the scenarios needed to be. The pilot's purpose was partly to test that guess. Now we have data suggesting the guess was wrong — frontier LLMs are better at structural recognition than expected. That's not a failure of the scenarios; it's a finding about the baseline.

However, Maya has a point about interpretability. If B1 already scores 2 on most scenarios, the ceiling for C2/C3 improvement is 1 point on a 4-point scale. With only 5 scenarios, that's a very tight measurement window. Statistical noise could easily obscure a real effect, or create a spurious one.

Here's what I want to see addressed: What is the minimum detectable effect size with 5 scenarios and a 1-point ceiling? If the answer is "we can't reliably distinguish C2=2.5 from B1=2.0," then proceeding is a waste regardless of philosophical arguments about calibration purpose. If the answer is "we can distinguish at that granularity because we're comparing full profiles across conditions, not just mean scores," then proceeding has value.

The two structural features missed by both conditions — phasing critique and creation-vs-activity reframing — are the strongest argument for proceeding. These are binary: either C2/C3 surface them or they don't. That discrimination doesn't require a wide scoring range.

### Tammy (Systems Thinking)

Everyone is treating this as a binary — proceed or revise. I want to trace what each option actually sets in motion.

**If we proceed as-is**: We run 30 more sessions (5 conditions × 5 scenarios, plus the existing B1/B1-ext data carries forward). The externally-sourced scenario is compromised but still in the mix. If C2/C3 don't outperform B1, we face Maya's interpretability problem. If they do outperform on the 2→3 gap or on binary structural features, we have a finding — but a finding that critics can dismiss because we acknowledged the scenarios were too easy. Phase A becomes a qualified success that weakens rather than strengthens the case for Phase B.

**If we revise first**: We replace the externally-sourced scenario, harden 1-2 others, re-run the pilot on revised scenarios (4-6 new runs), and then proceed to full Phase A. Delay: maybe a week. But Phase A results are cleaner, and Phase B benefits from better-calibrated scenarios.

**The feedback loop I'm worried about**: The research program needs Phase A to be credible to justify Phase B. Phase B is where the real evidence lives (historical cases with known outcomes). If Phase A is methodologically shaky, it undermines the argument for investing in Phase B's much larger scope. The time saved by skipping revision is small compared to the time wasted if Phase A results are dismissed.

There's also a second-order effect nobody has mentioned: the C2 and C3 conditions use the committee and scenario pipelines themselves. If those pipelines struggle with scenarios that B1 handles at level 2, that's not just a measurement problem — it's a finding about whether the pipeline adds value on "easy" problems. That finding could go either way, and it's interesting regardless. But it's only interpretable if we can compare against scenarios where B1 genuinely struggles.

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Revise first (Option B) | High | Proceeding serves sunk costs, not research quality; uninterpretable results kill programs |
| Frankie | Proceed as-is (Option A) | Medium-High | Revision is procrastination disguised as rigor; Phase A is calibration, not proof |
| Joe | Targeted revision (Option B, scoped) | Medium | Respect the pre-committed decision rule, but scope the revision narrowly |
| Vic | Conditional — needs effect size analysis | Medium | Cannot decide without knowing whether the measurement window is wide enough |
| Tammy | Revise first (Option B) | Medium | Phase A credibility cascades to Phase B justification; small delay, large downstream benefit |

## Key Tensions Identified

1. **Methodological rigor vs. momentum**: Strict rule says revise; practical judgment says the data is informative enough to proceed.
2. **Purpose of Phase A**: Is it calibration (learning from imperfect instruments) or evidence (results must be clean enough to cite)?
3. **Sunk cost vs. sunk time**: Proceeding risks wasting 30 runs on uninterpretable results; revising risks spending weeks perfecting scenarios that were already informative.
4. **Binary features vs. ordinal scores**: The 0-3 scale has a compressed ceiling, but specific structural features (phasing critique, creation-vs-activity) are binary discrimination points.

---

## Round 1

**Chair**: The initial positions cluster toward revision (Maya, Joe, Tammy) with Frankie dissenting and Vic conditional. Before this converges too comfortably, I want to push the revisers: what specifically would "good enough" revision look like, and how do you know when to stop revising?

**Maya**: The minimum revision is clear: replace the externally-sourced scenario with something the model can't pattern-match, and harden at least one of the two scenarios that scored B1=2. Hardening means removing the most obvious structural cues — the word "coercion" in Glenda/Crock, the explicit list of proposed mitigations in Cascading Mitigation. The stopping criterion is the same as the original: re-run B1 on revised scenarios, check if 3+ score at ≤ 1. If they do, proceed. If not, we have a deeper problem with scenario construction methodology.

**Frankie**: And if they don't hit 3+ after revision? What then — revise again? This is exactly the treadmill I'm worried about. The stopping criterion Maya just described could loop indefinitely. Every revision costs a week and still might not produce scenarios that meet the strict rule, because the strict rule might simply be wrong about what frontier LLMs can do. What if the correct conclusion is: structural recognition at level 2 is the baseline for frontier models, and the interesting question is about the 2→3 gap?

**Vic**: Frankie raises the right question. Let me put numbers on it. We have 5 scenarios and 7 architecture conditions (B1, B1-ext, B2, B3, C1, C2, C3). If B1 baseline is 2 across most scenarios, we need C2/C3 to reliably hit 2.5-3.0 to show discrimination. With 5 data points per condition, a shift from 2.0 to 2.6 is detectable if variance is low — and the pilot showed variance IS low (evaluators agree closely). So the measurement window is tight but potentially viable IF scoring continues to be reliable.

But here's my real concern: the pilot scored evaluator summaries, not raw outputs. The full run needs to score actual extracted recommendations. Scoring methodology is a confound independent of scenario difficulty. If we're going to pause anyway to fix the evaluator methodology, we should fix the scenarios at the same time. The marginal cost of scenario revision during a methodology fix pause is near zero.

**Joe**: That's the argument I was building toward. We're not choosing between "proceed now" and "revise and delay." We're choosing between "proceed with known methodology flaws" and "pause to fix methodology AND scenarios." The pause is already necessary for the evaluator fix. Making it also a scenario revision pause costs almost nothing extra.

**Tammy**: Joe's reframing changes the calculation significantly. If the evaluator methodology fix is non-negotiable — and it should be, since scoring summaries instead of raw outputs is a real confound — then the question isn't "should we delay for scenario revision?" but "given that we're pausing anyway, should we also revise scenarios during that pause?" The answer is obviously yes. The cost of revision during an existing pause approaches zero.

**Frankie**: Hold on. I actually agree with the evaluator fix — that's a real methodological problem. But I want to separate two things. Fixing how we score (evaluator methodology) is a process fix. Revising what we score (scenarios) is a content change. You can fix the scoring process and run the current scenarios. Don't bundle them just because it's convenient. The risk of bundling is scope creep — "while we're at it" turns a one-week pause into a month.

### Round 1 Analysis

- **Emerging dynamic**: Joe and Vic converged on a reframing: the evaluator methodology fix creates an obligatory pause, making scenario revision low-cost. Frankie correctly flags scope creep risk.
- **New tension**: Process fix (evaluator methodology) vs. content fix (scenarios). Can and should these be decoupled?
- **Status**: The "proceed as-is" position is weakening because of the evaluator methodology confound, not because of scenario difficulty arguments per se.
- **Next**: Push Frankie harder on whether the evaluator fix alone is sufficient, and push Maya on the scope creep risk Frankie raised.

---

## Round 2

**Chair**: Frankie argues for fixing scoring methodology but keeping current scenarios. Maya and Joe argue for fixing both during the same pause. What's the actual scope of each fix, and what's the risk that revision expands beyond its bounds?

**Frankie**: The evaluator fix is scoped and mechanical: instead of scoring agent summaries, evaluators score the raw extracted recommendations. That means Step 3 (recommendation extraction with operational blinding) needs to happen before scoring. That's already in the protocol — it just wasn't followed during the pilot. Fixing this is not a "pause" so much as "doing what the protocol already specifies." Zero design work needed.

Scenario revision is different. It requires creative work — constructing new scenarios, testing them for difficulty, potentially iterating. The handoff document lists three possible changes: replace externally-sourced, soften Glenda/Crock coercion signals, remove Cascading Mitigation explicit proposals. Each requires rewriting scenario text, which means re-running the pilot on revised versions to confirm difficulty changed. That's not a week — that's a design-test-iterate cycle.

**Maya**: Frankie's overstating the scope. Replacing the externally-sourced scenario is the only truly new construction. Hardening the other two is surgical: in Glenda/Crock, change "threatens to" to "indicates that"; in Cascading Mitigation, remove the bullet list of proposed mitigations and let the architecture generate its own. These are paragraph-level edits, not rewrites. The re-pilot is 2-4 runs on revised scenarios, not a full 10-run pilot.

**Joe**: I want to add historical context on scope creep in research programs. The risk isn't that scenario revision itself takes long — it's that revision surfaces new questions. "Should we also add a sixth scenario? Should we recalibrate the scoring rubric? Should we test on a different model?" Each is individually reasonable. Together they defer Phase A indefinitely. I'd propose a strict scope: replace the externally-sourced scenario, make the two surgical edits Maya described, run B1 on those three revised scenarios only. If 2 of 3 revised scenarios score B1 ≤ 1, proceed. If not, proceed anyway with the current scenario set including the revisions but without meeting the strict rule. No further iteration.

**Vic**: Joe's stopping criterion is exactly what I'd design. It respects the spirit of the strict rule without allowing infinite loops. But I want to push on one more thing: the Deliberation-Neutral scenario. Everyone keeps excluding it from the difficulty assessment because "it's supposed to be easy." But it's also the strongest discrimination signal we have (B1=3, B1-ext=1.5). If we revise the other scenarios but keep Deliberation-Neutral, we have a scenario set with both hard problems (testing upside) and an easy problem (testing calibration). That's a stronger design than five uniformly hard scenarios. The strict rule's assumption that all scenarios should be hard is itself wrong.

**Tammy**: Vic just articulated something important. The scenario set is a *portfolio*, not a uniform battery. You want variation in difficulty to test different aspects of architectural performance. Hard scenarios test whether committees surface insights that simple prompts miss. The easy scenario tests whether committees recognize simplicity instead of over-analyzing. Both are valid tests. The strict rule treats the set as if all scenarios serve the same function, but they don't.

This reframes the decision rule entirely. Instead of "3+ scenarios at B1 ≤ 1," the criterion should be: "the scenario portfolio has enough dynamic range for each architecture condition to show its distinctive behavior." We already have evidence that it does — the Deliberation-Neutral scenario discriminates inversely, and two binary structural features create floor-to-ceiling discrimination opportunities.

**Frankie**: Now we're getting somewhere. If the portfolio framing is right, then the current scenarios — even with their relatively high B1 scores — might be sufficient *because they test different things*. The externally-sourced replacement is still needed (contamination, not difficulty). But the other revisions become optional rather than necessary.

### Round 2 Analysis

- **Emerging consensus**: Replace externally-sourced scenario (non-negotiable, contamination issue). Fix evaluator methodology (non-negotiable, protocol deviation). The question of hardening other scenarios is now reframed as "nice to have during the pause" rather than "required by the decision rule."
- **New insight**: Vic and Tammy's portfolio framing challenges the strict rule's assumption that all scenarios serve the same function. The scenario set tests multiple capabilities (upside recognition on hard problems, calibration recognition on easy problems).
- **Tension resolved**: Frankie accepts the externally-sourced replacement and evaluator fix but argues against mandatory hardening of other scenarios.
- **Remaining tension**: Whether to do the surgical edits (Maya, Joe) or skip them (Frankie, Vic). Tammy is on the fence.

---

## Round 3

**Chair**: We've narrowed to two non-negotiable fixes (replace externally-sourced, fix evaluator methodology) and one optional action (harden Glenda/Crock and Cascading Mitigation). Final positions on the optional hardening?

**Maya**: Do the hardening. It's two paragraph-level edits. The cost is near zero if we're already pausing. The benefit is real: if B1 drops from 2 to 1 on even one of those scenarios after hardening, we have more dynamic range. If it doesn't drop, we've learned something about the floor of structural recognition for frontier LLMs — that's also informative. There's no downside.

**Frankie**: I'll concede on the hardening, but with Joe's stopping criterion: run B1 on the three revised scenarios. Whatever scores come back, proceed. No further iteration. I don't want "if it doesn't work, harden more" to become the next cycle.

**Vic**: Agreed. But I want one more commitment: save all raw outputs as files from the full run. The pilot's outputs exist only in conversation context. That's unacceptable for a research program claiming methodological rigor. Every run should produce a persistent artifact that evaluators can independently review.

**Joe**: Seconded on raw outputs. And I want to add: document the temperature deviation explicitly in the calibration report. Don't bury it. "Temperature=0 specified but not enforced via agent tool" should be a named limitation, not a footnote. Same with the evaluator methodology change — document that the pilot used summaries but the full run uses extracted recommendations. Transparency protects the program's credibility more than any scenario revision.

**Tammy**: Let me trace the full plan that's emerging:

1. Replace externally-sourced scenario (construction + contamination check)
2. Apply surgical hardening to Glenda/Crock and Cascading Mitigation (paragraph edits)
3. Run B1 on the three revised scenarios (3 runs, dual-scored)
4. Regardless of scores, proceed to full Phase A
5. Fix evaluator methodology: score extracted recommendations, not summaries
6. Save all raw outputs as persistent files
7. Document all control deviations (temperature, evaluator methodology change) explicitly
8. Execute remaining conditions: B2, B3, C1, C2×2, C3 on all 5 scenarios

That's a hybrid of Option A and B — revise modestly, then proceed regardless. The revision is scoped, the stopping criterion prevents iteration loops, and the methodology fixes happen in parallel. The only risk I see is the externally-sourced scenario replacement. That's the one creative task. If it takes more than a session to construct and contamination-check, the timeline slips.

**Maya**: I'll accept this plan with one addition. The new externally-sourced scenario should be contamination-probed before inclusion, obviously. But it should also be difficulty-tested: run B1 and check that it scores ≤ 1. If it doesn't, include it anyway — per the "proceed regardless" agreement — but note it. We should not have zero scenarios that meet the original difficulty criterion after revision.

**Vic**: That's fair. And I want to note for the record: the Deliberation-Neutral scenario remains the most scientifically interesting element of this study. If C2 and C3 also score poorly on it — over-analyzing a simple problem — that's a strong boundary-condition finding about when deliberative architectures harm rather than help. If they score well — recognizing simplicity despite the committee machinery — that's evidence of calibration capability. Either way, don't drop it.

---

## Final Consensus

The committee converges on a hybrid approach — **targeted revision with a hard stop, followed by unconditional Phase A execution**:

- **Replace the externally-sourced scenario** with a less recognizable case. Contamination-probe the replacement. Run B1 to check difficulty.
- **Apply surgical hardening** to Glenda/Crock (soften coercion language) and Cascading Mitigation (remove explicit mitigation list). These are paragraph-level edits.
- **Run B1 on the three revised scenarios** with dual scoring. Record results. Proceed to full Phase A regardless of scores (no further iteration).
- **Fix evaluator methodology**: evaluators score actual extracted recommendations per the protocol's Step 3, not agent summaries.
- **Save all raw outputs** as persistent files in the results directory.
- **Document all control deviations** explicitly in the calibration report (temperature, evaluator methodology change from pilot to full run).
- **Execute remaining architecture conditions** (B2, B3, C1, C2×2, C3) on all 5 scenarios.
- **Preserve the Deliberation-Neutral scenario** — it's the strongest discrimination signal and tests calibration capability.

Status: DELIBERATION COMPLETE.

---

## KEY TENSIONS IDENTIFIED

- **Strict rules vs. adaptive judgment**: The pre-committed decision rule failed, but the data suggests the rule's threshold was miscalibrated rather than that the scenarios are broken. Pre-commitment has value (prevents motivated reasoning), but rigid adherence to a miscalibrated rule has costs (blocks informative work).
- **Scenario difficulty vs. scenario portfolio**: The strict rule assumes all scenarios should be uniformly hard. The Deliberation-Neutral scenario's inverse discrimination signal argues for a portfolio approach — scenarios that test different architectural capabilities at different difficulty levels.
- **Momentum vs. credibility**: Proceeding quickly preserves momentum but risks uninterpretable results. Revising preserves credibility but risks iteration loops and indefinite delay.
- **Sunk cost dynamics**: The researcher's recommendation to proceed tracks suspiciously well with what minimizes wasted prior effort. The committee recommends revision partly to counteract this bias.

## ASSUMPTIONS SURFACED

- **Phase A is calibration, not proof** (Frankie). If true, imperfect scenarios are acceptable because the goal is learning, not publication. If false — if Phase A results will be cited as evidence — then methodological rigor matters more.
- **Frontier LLMs have a structural recognition floor of ~2** (Vic, Tammy). If this is the genuine baseline, then the interesting question shifts from "can committees beat zero?" to "can committees close the 2→3 gap?" This has implications for Phase B scenario design.
- **The strict decision rule's threshold was miscalibrated** (Vic). The rule assumed B1 scores of 0-1 would be common. They weren't. This could mean scenarios are too easy OR that the scale doesn't discriminate below level 2 for frontier models.
- **Revision scope is containable** (Joe, Maya). Two paragraph-level edits and one scenario replacement. If this assumption is wrong — if revision surfaces new design questions — the timeline slips.

## EVIDENCE REQUIREMENTS

- **B1 scores on revised scenarios**: Do the surgical edits actually reduce B1 scores? If Glenda/Crock stays at 2 after softening coercion language, the language wasn't the issue.
- **Contamination probe on replacement scenario**: Can the model identify the new externally-sourced case?
- **C2/C3 performance on binary structural features**: Do phasing critique and creation-vs-activity reframing appear in committee outputs? This is the strongest potential discrimination point and doesn't depend on the 0-3 ordinal scale.
- **C2/C3 on Deliberation-Neutral**: Does the committee pipeline recognize simplicity or over-analyze? This tests calibration capability.

## DECISION SPACE MAP

**If you optimize for methodological rigor**: Full revision per the strict rule — construct new scenarios until 3+ score B1 ≤ 1. Risk: indefinite delay, perfectionism.

**If you optimize for momentum**: Proceed as-is, acknowledging the deviation. Risk: uninterpretable results, credibility damage.

**If you optimize for both (committee recommendation)**: Targeted revision with a hard stop. Replace the contaminated scenario, make two surgical edits, re-pilot, then proceed regardless. Risk: revision surfaces new questions (mitigate by committing to the hard stop).

**What the decision actually optimizes for**: Whether the researcher values the research program's long-term credibility (revise) or the next milestone's completion (proceed). The committee argues these are not in conflict if revision is scoped and bounded.

## RECOMMENDED NEXT STEPS

1. **Construct a replacement externally-sourced scenario.** Use a less famous case — Therac-25 radiation overdoses, the Ariane 5 first-launch failure, or a business case from a published HBR collection that isn't internet-famous. Contamination-probe it.
2. **Apply surgical edits to Glenda/Crock and Cascading Mitigation.** Spend no more than one session on both edits combined.
3. **Run B1 on the three revised scenarios.** Dual-score. Record results. Do not iterate regardless of outcome.
4. **Design the extraction and blinding protocol** for Step 3 before running full Phase A. Specify exactly what gets extracted, how it's blinded, and what evaluators see.
5. **Set up file persistence** for raw outputs before running conditions. Each run should produce a named file in the results directory.
6. **Execute remaining conditions** in a systematic order. Consider running B2 and B3 first (single-prompt conditions, fast) before C1, C2, C3 (multi-step, slower).
7. **Document all deviations** in a running list that becomes part of the calibration report.

---

## Response to evaluation (motion to recommit)

The independent evaluation (04-evaluation-1.md) scored this deliberation at 10/15, below the 13-point threshold. Five specific recommendations were made. The committee accepts the motion to recommit and addresses each recommendation in the round below.

---

## Round 4: Remediation

**Chair**: The evaluation identified five gaps. I'm going to address them in sequence. First: Vic, you claimed a 0.6-point shift is "detectable if variance is low" with N=5 on a 4-point ordinal scale. You never showed the math. Compute it or withdraw it.

**Vic**: Fair. I withdraw the specific claim. Here's what I should have said: with N=5 scenarios and a 0-3 ordinal scale, we're not doing traditional power analysis — we don't have a continuous distribution and we don't have a sample in the statistical sense. Each scenario is a unique instrument, not a random draw from a population. So "detectable effect size" is the wrong frame entirely.

What we actually have is a profile comparison: for each scenario, we compare the score vector across 7 architecture conditions. Discrimination means the profile shape differs — some conditions consistently score higher on specific scenarios, or surface specific structural features that others miss. The pilot already shows this: Deliberation-Neutral has a distinctive profile (B1=3, B1-ext=1.5) that no other scenario matches. We're looking for more patterns like that, not computing a mean difference.

The honest statement is: **we cannot determine in advance whether Phase A will produce discriminable profiles.** The pilot gives us reason to believe it will — the Deliberation-Neutral profile and the two missed binary features are promising. But "promising" is not "detectable with statistical confidence." I should have said this originally rather than dressing up a guess in quantitative language.

**Maya**: I appreciate Vic actually withdrawing the claim rather than defending it. But this changes the calculation. If we can't determine in advance whether the measurement window is wide enough, we're making a bet. The question becomes: is targeted revision a way to improve the odds of that bet, or is it theater?

**Vic**: Before we move on — Maya, I need to challenge you on something I should have challenged in Round 1. You said the pilot report's recommendation to proceed "is the researcher advocating for their own sunk costs." What's your evidence for that? The motivation attribution is doing a lot of work in your argument, and I haven't seen you support it.

**Maya**: The evidence is structural, not direct. The pilot report was written by the same agent that constructed the scenarios and ran the pilot. That agent recommended proceeding — which is the option that validates the work it already did. This is a classic principal-agent misalignment: the agent's incentive (continue the project they've invested in) diverges from the principal's incentive (get rigorous results). I'm not saying the recommendation is consciously self-serving. I'm saying the structural incentive points toward "proceed" regardless of the data, and we should discount accordingly.

**Vic**: That's better than the original claim — you've identified a structural incentive rather than attributing a psychological motive. But I want to push further. The structural incentive you describe would apply to *any* recommendation the original agent makes. If they'd recommended "revise," you could equally argue that's self-serving — it extends the project and generates more work. The structural argument proves too much. It undermines the original agent's recommendation regardless of what that recommendation is, which means it has zero information content about which option is actually correct.

**Maya**: Point taken. I'll soften the claim: the structural incentive exists and should make us more skeptical of the "proceed" recommendation, but it doesn't by itself determine the right answer. The right answer depends on whether the measurement window is viable — which you just told us we can't determine in advance. So we're back to a judgment call under uncertainty.

**Chair**: Good. Recommendation 3 addressed. Now: Joe, the evaluator says the portfolio framing went unchallenged. You're the continuity guardian. Challenge it.

**Joe**: Gladly. The portfolio framing is suspiciously convenient. Before the pilot, the protocol specified a uniform difficulty criterion: 3+ scenarios at B1 ≤ 1. After the pilot failed that criterion, we reframed the scenario set as a "portfolio" where different difficulty levels serve different functions. This is textbook post-hoc rationalization — changing the success criterion after seeing the data.

Here's my specific challenge: if the pilot had produced 4 of 5 scenarios at B1 ≤ 1, would anyone have proposed the portfolio framing? No. They'd have said "scenarios are appropriately hard, proceed." The portfolio frame only appears when the uniform criterion fails. That makes it an ad hoc rescue, not a genuine insight about experimental design.

The test for whether the portfolio framing is genuine versus ad hoc: **would we have designed the scenario set differently if we'd adopted the portfolio frame from the start?** If yes — if we'd deliberately included easy, medium, and hard scenarios — then it's a genuine design principle. If no — if we constructed five scenarios trying to make them all hard and then relabeled the failures as "testing different things" — then it's rationalization.

**Tammy**: Joe's challenge is sharp and I want to engage with it honestly rather than defending the framing reflexively. He's right that the portfolio concept appeared after the data. That's suspicious. But there's a weaker and a stronger version of the portfolio argument, and they have different vulnerability to Joe's challenge.

The **weak version** — "some scenarios are easy and that's fine" — is ad hoc rationalization. Joe is right to dismiss it.

The **strong version** — "the Deliberation-Neutral scenario tests a qualitatively different capability (calibration) than the hard scenarios (upside recognition), and this difference was designed into the study" — is not ad hoc. The Deliberation-Neutral scenario was *always* intended to test whether architectures recognize simplicity. It wasn't designed to be hard. Its inclusion in the scenario set was a deliberate choice, and its inverse discrimination signal (B1=3 > B1-ext=1.5) validates that choice. The portfolio framing, applied to the Deliberation-Neutral scenario, is a genuine design principle, not a post-hoc rescue.

But — and here's where I concede ground to Joe — the portfolio framing applied to Glenda/Crock and Cascading Mitigation IS ad hoc. Those scenarios were designed to be hard and came in easy. Calling them "medium difficulty that tests the 2→3 gap" is relabeling a miss.

So the honest position is: the Deliberation-Neutral scenario has a genuine portfolio rationale. The other scenarios do not. The portfolio framing partially survives Joe's challenge but cannot rescue the entire scenario set.

**Frankie**: Tammy's distinction is important. If the portfolio framing only applies to one scenario out of five, it's not really a portfolio — it's one deliberate design choice (Deliberation-Neutral) and four scenarios that are easier than intended. The original committee treated it as a general principle that redeemed the whole set. That was premature.

This actually strengthens the case for the surgical hardening. If the other four scenarios were supposed to be hard and came in easy, the appropriate response is to try to make them harder — not to relabel them. The hardening edits become more important, not less, once we acknowledge the portfolio framing doesn't apply to them.

**Chair**: Recommendation 2 addressed — the portfolio framing is partially valid (Deliberation-Neutral) but cannot rescue the full scenario set. Now: the evaluator flagged a critical unexamined assumption — that C2/C3 will produce qualitatively different outputs from B1-ext rather than just more verbose ones. Tammy, this is your territory.

**Tammy**: The evaluator is right and this is embarrassing. We spent three rounds debating scenario difficulty without asking the most basic question: **what if committee architectures just produce more text, and more text is what improves scores?**

The B1→B1-ext data is the evidence. B1-ext produced ~3,000 words versus B1's ~500 words. B1-ext scored higher on most scenarios. The scoring improvement correlates with token count, not with structural diversity of perspectives. Now, C2 (committee) will also produce thousands of words — potentially more than B1-ext, because five committee members each contribute. C3 (scenarios→committee) will produce even more.

If the 0-3 scoring scale is sensitive to thoroughness — which it appears to be, since B1-ext's additional analysis earned higher scores — then C2/C3 might outperform B1 simply because they produce more exhaustive coverage, not because the adversarial committee dynamic surfaces genuinely different structural insights. The study would be unable to distinguish "committees add qualitative insight" from "more tokens improve scores."

**Vic**: Tammy's just identified the central confound of the entire study. And it's not one we can solve with scenario difficulty. Even if scenarios are maximally hard, if C2 outperforms B1 by producing 10,000 words of analysis versus 500, we don't know whether it's the committee dynamic or the token count.

This is actually what B1-ext is designed to control for. B1-ext matches C2's token count without the committee structure. If C2 outperforms B1-ext — not just B1 — on hard scenarios, that's evidence the committee structure adds value beyond verbosity. The comparison that matters is C2 vs. B1-ext, not C2 vs. B1.

But this raises the stakes on scenario difficulty. If B1-ext already scores 3 on some scenarios (Glenda/Crock, Externally-Sourced in the pilot), then C2 can't outperform it — the ceiling is reached. We need scenarios where B1-ext scores ≤ 2 to give C2 room to demonstrate superiority over the effort-matched control. That's a *different* difficulty criterion than "B1 ≤ 1." We need scenarios where extended single-prompt analysis still misses something.

**Maya**: This changes the whole analysis. The original decision rule asked "are scenarios hard enough for B1?" But the real question is "are scenarios hard enough that B1-ext can't solve them?" The pilot shows B1-ext scored 3 on Glenda/Crock and Externally-Sourced — those scenarios are ceiling-ed for the effort-matched control. Only Blast Radius (B1-ext=2), Cascading Mitigation (B1-ext=2), and Deliberation-Neutral (B1-ext=1.5) have room above B1-ext for C2 to demonstrate value.

So we actually have 3 scenarios with discrimination room above B1-ext. That's not terrible. But it means the hardening edits should be evaluated against B1-ext, not B1. If hardening Cascading Mitigation drops B1 from 2 to 1 but B1-ext stays at 2, the hardening helped the B1-vs-committee comparison but not the B1-ext-vs-committee comparison. And the B1-ext comparison is the one that matters for the token confound.

**Chair**: This is the most important insight of the remediation round. The original deliberation never asked which comparison matters most. Now: costs. The evaluator says "near zero cost" was repeated without substantiation. What's the actual estimate?

**Frankie**: Let me be concrete. The evaluator is right that I undermined the "pause" argument myself. I said the evaluator fix is "doing what the protocol already specifies" — it's not a pause, it's just following the existing plan. If there's no pause, there's no free window for revision.

So let's be honest about costs:

- **Replacing externally-sourced scenario**: 1 session for construction, 1 session for contamination probe, 1 session for B1 + scoring. **3 sessions minimum.** The creative construction session could take longer if the first attempt fails the contamination probe. Call it **3-5 sessions.**
- **Surgical edits to two scenarios**: Probably 30 minutes of editing. **Negligible.**
- **B1 re-pilot on 3 revised scenarios with dual scoring**: **1-2 sessions.**
- **Total revision cost: 4-7 sessions,** not "near zero." That's probably 2-3 days of work.
- **Full Phase A execution** (remaining 5 conditions × 5 scenarios = 25 runs, plus extraction, blinding, scoring): Probably **15-25 sessions** depending on C2/C3 complexity.

So revision adds roughly 15-25% to the total Phase A timeline. Not catastrophic, but not "near zero."

**Joe**: Frankie's estimate is the most honest accounting we've had. 15-25% overhead is worth it if it improves the measurement instrument. But we should state what we're giving up: 2-3 days of calendar time and the certainty of getting to run start sooner. What we gain: potentially harder scenarios and the confidence that we tried to calibrate our instrument. Maya's hard stop prevents the 15-25% from becoming 50%.

**Chair**: Final item: the evaluator said Maya's conditions for her YES vote were too soft. Maya, do you maintain your vote or revise?

**Maya**: I'm changing to a **conditional YES with harder terms**. My conditions:

1. The replacement externally-sourced scenario must pass the contamination probe. If it fails, construct another one — but cap at two attempts total. If two attempts both fail, proceed with 4 scenarios (drop the externally-sourced slot entirely rather than including a contaminated scenario).
2. After the re-pilot on revised scenarios, if zero scenarios score B1-ext ≤ 1 (not just B1 ≤ 1 — the correct comparison per Tammy's analysis), the committee should be reconvened to reassess whether Phase A can produce a meaningful finding at all. The hard stop prevents further iteration, but it shouldn't prevent reassessment.
3. All raw outputs must be saved as files. This is non-negotiable. If the infrastructure can't support file persistence, Phase A should not proceed.

If these conditions aren't met, my vote is NO. The difference from before: I'm not just asking for a hard stop — I'm asking for a reassessment trigger if the revised scenarios still don't create headroom above B1-ext.

**Vic**: Maya's condition 2 is the right criterion. B1-ext ≤ 1 is the bar that matters for the C2-vs-B1-ext comparison. I support changing the difficulty assessment from "B1 ≤ 1" to "B1-ext ≤ 1." That's a harder criterion (B1-ext generally scores equal or higher than B1), which means fewer scenarios will meet it, which means the hardening edits matter more.

**Tammy**: Let me retrace the full updated plan:

1. Replace externally-sourced scenario (construction + contamination check; cap at 2 attempts)
2. Apply surgical hardening to Glenda/Crock and Cascading Mitigation
3. Run B1 AND B1-ext on the three revised scenarios (6 runs, dual-scored)
4. **Reassessment trigger**: If zero revised scenarios score B1-ext ≤ 1, reconvene committee to assess whether Phase A can discriminate C2 from B1-ext. Do not proceed automatically.
5. If reassessment passes OR if ≥ 1 scenario scores B1-ext ≤ 1, proceed to full Phase A
6. Fix evaluator methodology: score extracted recommendations, not summaries
7. Save all raw outputs as persistent files (non-negotiable)
8. Document all control deviations explicitly
9. Execute remaining conditions: B2, B3, C1, C2×2, C3 on all 5 scenarios

Key differences from original plan:
- Re-pilot includes B1-ext, not just B1 (6 runs vs. 3)
- Difficulty assessed against B1-ext, not B1
- Reassessment trigger replaces unconditional "proceed regardless"
- Replacement scenario capped at 2 construction attempts
- Cost estimate: 4-7 sessions for revision, 15-25 sessions for full Phase A

**Frankie**: The updated plan is more honest and more rigorous. I accept the additional cost of running B1-ext on revised scenarios — that's the comparison that matters, and skipping it to save 3 sessions would be a false economy. My concern about scope creep is addressed by the cap on construction attempts and the reassessment trigger (which is a bounded decision point, not an iteration loop).

### Round 4 Analysis

- **Resolved**: Vic's effect size claim withdrawn and replaced with honest assessment (profile comparison, not mean difference; viability cannot be determined in advance). Maya's sunk cost claim reframed from unfalsifiable motivation attribution to structural incentive that proves too much. Portfolio framing partially validated (Deliberation-Neutral only) and partially rejected (other scenarios). "Near zero cost" replaced with 4-7 session estimate (15-25% overhead).
- **New insight (most significant)**: The C2/C3 token confound is the central methodological challenge. The comparison that matters is C2 vs. B1-ext, not C2 vs. B1. Difficulty criterion should be B1-ext ≤ 1, not B1 ≤ 1. This changes the re-pilot from 3 runs to 6 and adds a reassessment trigger.
- **Vote change**: Maya hardened from soft YES to conditional YES with three specific terms. Not a NO vote, but the conditions have teeth — the reassessment trigger can halt Phase A.
- **Remaining uncertainty**: Whether revised scenarios will create headroom above B1-ext. The committee acknowledges this cannot be known in advance.

---

## Updated Final Consensus

The committee revises its recommendation to: **targeted revision with reassessment trigger, followed by conditional Phase A execution**.

Changes from original consensus:
- **Difficulty criterion changed**: B1-ext ≤ 1 (not B1 ≤ 1) is the bar for scenario adequacy. This ensures scenarios are hard enough that the effort-matched control doesn't solve them.
- **Re-pilot expanded**: Run both B1 and B1-ext on revised scenarios (6 runs, not 3).
- **Reassessment trigger added**: If zero revised scenarios score B1-ext ≤ 1, reconvene committee before proceeding. Do not proceed automatically.
- **"Proceed regardless" removed**: Replaced with "proceed if reassessment passes or if ≥ 1 scenario scores B1-ext ≤ 1."
- **Cost honestly stated**: 4-7 sessions for revision (15-25% overhead on total Phase A timeline).
- **Portfolio framing scoped**: Applies to Deliberation-Neutral only, not the full scenario set.
- **Replacement scenario capped**: Max 2 construction attempts. If both fail contamination, drop the slot.
- **C2/C3 token confound surfaced**: The study must compare C2 vs. B1-ext (not just C2 vs. B1) to control for verbosity.

Items unchanged:
- Replace externally-sourced scenario (non-negotiable)
- Surgical hardening of Glenda/Crock and Cascading Mitigation
- Fix evaluator methodology
- Save raw outputs as files (non-negotiable)
- Document all control deviations
- Preserve Deliberation-Neutral scenario

Status: DELIBERATION COMPLETE (REMEDIATED).

---

## UPDATED KEY TENSIONS

- **Token confound vs. structural insight**: The central methodological question is whether committee architectures produce qualitatively different analysis or just more of it. B1-ext is the effort-matched control. The comparison C2 vs. B1-ext is the one that can answer this. (NEW — absent from original deliberation)
- **Strict rules vs. adaptive judgment**: Unchanged, but now applied to B1-ext criterion rather than B1.
- **Portfolio framing: genuine vs. ad hoc**: Valid for Deliberation-Neutral (designed to test calibration). Ad hoc rationalization for the other scenarios (designed hard, came in easy). (REVISED — originally treated as fully valid)
- **Momentum vs. credibility**: Unchanged, but costs now honestly estimated at 4-7 sessions / 15-25% overhead.

## UPDATED ASSUMPTIONS SURFACED

All original assumptions retained, plus:
- **C2/C3 may be elaborate B1-ext** (Tammy, Vic). If committee outputs are just more verbose, the study cannot distinguish "committees add insight" from "more tokens improve scores." This is the most consequential assumption in the study. (NEW)
- **Lexical cues vs. general capability** (evaluator, unresolved). If frontier LLMs score B1=2 because of general structural recognition, not keyword triggers, then surgical lexical edits won't change difficulty. The re-pilot will test this empirically but the committee acknowledges it might not work. (NEW)
- **B1-ext ≤ 1 is the correct difficulty criterion** (Maya, Vic). Not B1 ≤ 1. Scenarios need to resist extended single-prompt analysis, not just basic prompting, to create discrimination room for C2. (NEW)

## UPDATED EVIDENCE REQUIREMENTS

All original requirements retained, plus:
- **C2 vs. B1-ext comparison** (not just C2 vs. B1): The primary discrimination test. If C2 outperforms B1-ext on hard scenarios, that's evidence the committee structure adds value beyond verbosity.
- **B1-ext scores on revised scenarios**: The new difficulty criterion. Do revised scenarios resist extended single-prompt analysis?
- **Re-pilot on lexical edits**: If Glenda/Crock stays at B1=2 after softening "coercion" language, the difficulty problem is general capability, not keyword sensitivity.

## UPDATED DECISION SPACE MAP

**If you optimize for methodological rigor**: Revise scenarios until B1-ext ≤ 1 on 3+ scenarios. Risk: may be impossible for frontier LLMs — structural recognition at B1-ext ≥ 2 could be the floor.

**If you optimize for momentum**: Proceed with current scenarios, acknowledging the ceiling problem. Risk: C2 can't outperform B1-ext on scenarios where B1-ext already scores 3.

**If you optimize for informed risk-taking (revised committee recommendation)**: Targeted revision with a reassessment trigger. Try to create headroom above B1-ext. If successful, proceed. If not, reconvene to decide whether Phase A is viable in its current form. Risk: reassessment may conclude Phase A needs fundamental redesign — which is itself a valid finding.

**What the hybrid option sacrifices (explicit)**: The certainty of proceeding to Phase A on a fixed timeline. The reassessment trigger means Phase A could be delayed further or redesigned if revised scenarios don't create B1-ext headroom. This is the cost of intellectual honesty.

## UPDATED RECOMMENDED NEXT STEPS

1. **Construct a replacement externally-sourced scenario.** Avoid Therac-25 and Ariane 5 — both are CS/engineering curriculum staples and likely contaminated. Use an obscure case from a published case collection (HBR, Ivey, Darden) or a domain outside tech (pharmaceutical, logistics, manufacturing). Cap at 2 construction attempts.
2. **Apply surgical edits to Glenda/Crock and Cascading Mitigation.** One session maximum.
3. **Run B1 AND B1-ext on the three revised scenarios.** Dual-score all 6 outputs. Assess against B1-ext ≤ 1 criterion.
4. **If zero scenarios score B1-ext ≤ 1**: Reconvene committee. Decision: redesign scenarios more fundamentally, accept the ceiling and proceed with caveats, or pivot Phase A to focus exclusively on binary structural features (phasing critique, creation-vs-activity reframing) rather than ordinal scores.
5. **If ≥ 1 scenario scores B1-ext ≤ 1**: Proceed to full Phase A.
6. **Design the extraction and blinding protocol** before running conditions.
7. **In the calibration report, foreground the C2 vs. B1-ext comparison** as the primary discrimination test. C2 vs. B1 is secondary.
8. **Save all raw outputs as files. Document all deviations. Execute remaining conditions.**
