# Phase 2: Deliberation

**Topic**: Is "When This Methodology Fails" good enough to publish? Will it help drive adoption?
**Protocol**: Robert's Rules (modified for adversarial committee)

---

## Opening Statements

### Maya (Paranoid Realism)

I recommended this essay. I said it would be "the single most credibility-building thing the project could produce." So let me be clear about what I expected and whether this delivers.

What I wanted was an essay that would make a competent practitioner think: "These people are engineers, not evangelists." An essay that *costs* something — that makes the methodology look genuinely weaker in places, not just performatively self-critical. The failure mode I feared most was what I'll call "credibility theater" — an essay that *performs* honesty about limitations while actually strengthening the reader's confidence by making the author look nobly self-aware. "We're so honest about our flaws!" as a marketing strategy.

Here's my assessment: the essay *mostly* avoids this trap, but not entirely. The self-application section at the end — "This essay could fail by making the methodology look robustly self-aware rather than genuinely limited" — explicitly names the credibility paradox. That's good. But naming the paradox doesn't escape it. The essay is well-written, well-structured, and ends with "Results, not resolutions." A reader who finishes it will almost certainly trust the methodology *more*, not less. That might be the correct response (the failure modes are real but manageable) or it might be exactly the trap the essay warns about.

The failure mode I think is insufficiently explored: **the problem of shared training distribution**. Failure Mode 3 raises it (independent evaluation by the same model family), but it applies much more broadly. All six failure modes are failure modes *that an LLM could identify about itself*. They're the kinds of limitations you'd expect from a system trained on methodology-critical literature. What about failure modes that are invisible from within the training distribution? The essay can't identify those by definition — and it acknowledges this in the self-application section — but the acknowledgment is too brief. Two sentences for the deepest problem in the essay.

### Frankie (Idealism / Values Guardian)

The essay fulfills a core value of the methodology: transparency about what the tool can and can't do. "A methodology that only tells you about its successes is marketing. This essay is engineering." That opening line is exactly right. It sets the contract with the reader.

Where the essay shines: the scope map. That section — "when to use the full pipeline, the committee alone, a quick propensity check, or nothing" — is the most practically valuable thing in the document. A practitioner can read just that section and make a better decision about whether to invest time. This is what Vic called "evidence-proportional" in the adoption strategy deliberation: cheap, one-time, measurably useful.

Where I'm uncomfortable: the essay treats all failure modes as engineering problems with engineering solutions. Pre-screening, calibration audits, domain-expert review, forced editorial engagement, frame-challenge protocols, external validation programs. These are all good recommendations. But some failure modes — particularly the meta-circularity trap and the user's abdication of editorial judgment — are not engineering problems. They're *human* problems. The meta-circularity trap doesn't have a technical fix. It requires the user to maintain genuine uncertainty about whether the methodology works, even while using it. That's a psychological posture, not a protocol. The essay gestures at this ("if reading this essay makes you trust the methodology more, check whether the trust comes from content or from gesture") but doesn't fully sit with the discomfort.

The essay's mission alignment is strong. It doesn't apologize for the methodology or hedge about whether it's useful. It says: here's where it works, here's where it doesn't, here's how to tell the difference. That's the voice of the project at its best.

### Joe (Continuity Guardian / Institutional Memory)

I want to check the failure modes against historical precedent. Do these match what happened to other methodologies that published limitations documents?

**Pattern 1: Agile.** The Agile Manifesto (2001) didn't include a "when Agile fails" document. The limitations were documented later by critics (Jez Humble, Martin Fowler), not by the creators. By then, the methodology was already being misapplied at scale. If the Agile founders had published a "when Agile fails" document up front — "don't use this when requirements are fixed and known, don't use this when the team is distributed with no trust, don't use this when management won't commit to changed processes" — it might have prevented some of the worst SAFe-ification. Or it might have been ignored. But having it *from the creators* would have given internal advocates something to cite.

**Pattern 2: Design Thinking.** IDEO published extensively about design thinking's applicability and process. They didn't publish failure modes prominently. When Natasha Jen's "Design Thinking is Bullshit" talk went viral in 2017, it hit hard precisely because IDEO hadn't preempted the critique. A methodology that owns its limitations inoculates against external critics — they can't reveal what you've already disclosed.

**Pattern 3: Lean Startup.** Eric Ries included some scope limitations in *The Lean Startup* but positioned them as edge cases, not fundamental boundaries. When practitioners discovered the hard way that lean startup doesn't work well for hardware, regulated industries, or B2B enterprise sales, the methodology's credibility took a hit.

The historical pattern says: **publishing failure modes from the creator's position is strategically advantageous.** It builds trust with sophisticated practitioners (the ones you want as early adopters), inoculates against external critique, and provides a reference point for "you're using this wrong." The essay does all three. The question is whether it does them *well enough*.

My specific concern: the essay's failure modes are *conceptual*, not *empirical*. Every scenario is hypothetical — "A developer asks the committee whether to use PostgreSQL or MySQL," "A CEO frames the problem as enterprise-or-consumer." None are drawn from actual committee runs. The methodology-evolution document notes that there are no documented failure cases. This means the essay is a *prediction* of what failure looks like, not a *report* of what failure looked like. That's appropriate for a young methodology (you write the safety manual before the crash, not after). But it should be made more explicit — these are predicted failure modes, and empirical validation is pending.

### Vic (Evidence Prosecutor)

Joe's right to flag the empirical gap, but I want to push harder on it. Let me evaluate the essay's claims against evidentiary standards.

**Claim 1: "The methodology fails most dangerously when it produces confident, well-scored, traceable answers to the wrong question."** This is the essay's central thesis. Is it supported? The staffing scenario in the opening is hypothetical. I want to know: has this actually happened? Has a committee run in this repository ever produced an answer to the wrong question? The three committee runs in the repository (testing-deliberated-choice-workflow, methodology-adoption-strategy, and now this one) are all self-referential — the methodology evaluating itself. That's too small a sample and too self-referential to confirm or refute this failure mode.

**Claim 2: "A transcript can score 15/15 and still be wrong about the situation."** True by construction — the rubrics measure process quality, not outcome quality. But how often does this happen? The claim implies it's a significant risk. Without frequency data, we can't distinguish "theoretically possible but rare" from "common and dangerous."

**Claim 3: The scope map — "Don't use this methodology at all when the problem has a factual answer that can be looked up."** This is actionable and I believe it's correct. But the boundary is fuzzier than the essay acknowledges. Many complex problems *look* like they have factual answers until you dig deeper. "Should we use PostgreSQL or MySQL?" might actually be complex if the decision interacts with team dynamics, vendor relationships, and long-term architecture. The essay's opening scenario dismisses this as a "complicated but not complex" problem — but the diagnosis "this doesn't need a committee" is itself a judgment call that might be wrong.

**Where the essay is strongest: detection heuristics.** The surprise heuristic ("if nothing surprised you, the methodology didn't earn its cost"), the override rate ("10-30% is healthy"), the "resolution closely mirrors initial framing" test — these are specific, testable, actionable. They're not evidence yet, but they're *falsifiable predictions*, which is better than most methodology documents provide.

**My verdict**: The essay is good enough to publish. It's stronger on specificity and actionability than I expected. The empirical gap (no actual failure cases) should be acknowledged more prominently. The scope map is the highest-value section and should be surfaced earlier.

### Tammy (Systems Thinker)

I want to trace how publishing this essay changes the system's feedback loops.

**Loop 1: Trust-building loop (positive).** Essay describes limitations honestly → practitioners read it → practitioners trust the methodology more → practitioners engage more deeply → methodology gets feedback → methodology improves → limitations document becomes more empirically grounded. This is the virtuous cycle the adoption-strategy committee was hoping for. The essay is the entry point.

**Loop 2: Self-selection loop (positive).** Essay describes scope boundaries → practitioners read scope map → practitioners with appropriate problems adopt the methodology → those practitioners get good results → good results generate positive signal → more appropriate practitioners adopt. The scope map is a *filter* — it reduces total adoption but increases successful adoption. This is higher-value than undifferentiated growth (see: Agile's dilution problem that Joe mentioned).

**Loop 3: Deterrence loop (potentially negative).** Essay describes failure modes → practitioners read failure modes → some practitioners conclude the methodology is too risky → they don't try it → the methodology loses potential adopters who would have succeeded. The question is the size of this group. Maya wants the essay to be maximally honest; this loop is the cost of that honesty.

**Loop 4: Self-fulfilling prophecy loop (concerning).** Essay describes "user abdicates editorial role" as a failure mode → practitioners become hypervigilant about over-trusting the process → practitioners second-guess every committee output → practitioners lose confidence in the methodology → practitioners abandon it — not because the methodology failed but because the warnings made them too cautious to use it effectively. This is the essay's own failure mode: *over-correction in response to the limitations document*.

The key question: **which loops dominate?** I believe Loops 1 and 2 dominate for sophisticated practitioners (the target audience). Loop 3 is real but small — most people who'd be deterred by honest limitations weren't committed enough to succeed anyway. Loop 4 is worth monitoring but unlikely to be large — the essay's tone is practical ("here's how to detect and fix this"), not alarming ("beware, everything could go wrong").

**System-level recommendation**: The essay should be published. It strengthens the positive feedback loops (trust, self-selection) more than it strengthens the negative ones (deterrence, over-correction). But the monitoring plan from the adoption-strategy deliberation should track whether practitioners who read the limitations essay first have different adoption patterns than those who don't.

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Mostly delivers on the credibility promise; shared training distribution underexplored | Medium-High | "Credibility theater" risk — naming the paradox doesn't escape it |
| Frankie | Strong mission alignment; some failure modes are human problems, not engineering problems | High | Meta-circularity and editorial abdication lack technical fixes |
| Joe | Historically, creator-published limitations are strategically advantageous; failure modes are conceptual, not empirical | High | No actual failure cases documented |
| Vic | Specific and actionable; empirical gap should be acknowledged more prominently | High | Claims about failure frequency are untested |
| Tammy | Positive feedback loops dominate; publish will improve the system | High | Loop 4 (over-correction) worth monitoring |

## Key Tensions Identified

1. **Honesty vs. encouragement**: Maya wants the essay to cost more (be harder to read as confidence-building); Frankie wants it to serve the mission (be honest but not demoralizing). The tension is where to set the dial between "unflinching" and "practical."
2. **Conceptual vs. empirical**: Joe and Vic note all failure modes are predicted, not observed. The essay reads as a safety manual written before any accidents. This is appropriate for the project's stage but should be acknowledged.
3. **Engineering fixes vs. human postures**: Frankie identifies that some failure modes (meta-circularity, editorial abdication) don't have protocol-level fixes — they require the user to maintain a psychological posture that no document can guarantee.

---

## Round 1

**Chair**: Two concrete questions for the committee. First: is the essay ready to publish, or does it need revision? Second: would the essay be better positioned at the *beginning* of the essays collection (as a first read for skeptics) or where it currently sits (among the later essays)?

**Vic**: On readiness — I say publish with two specific revisions. One: the opening section should state explicitly that these are *predicted* failure modes from a methodology with limited empirical data, not *documented* failures from extensive use. The essay currently implies empirical grounding it doesn't have. Two: the scope map should be promoted — either moved earlier in the essay or given a more prominent heading. It's the most actionable section and it's buried two-thirds of the way through.

**Maya**: I agree with Vic's first point but want to push it further. The essay should include a section — even a short one — that says: "These are the failure modes we can see from inside the methodology. The failure modes we can't see are, by definition, absent from this document. The most important failure mode may be one we haven't identified." The self-application section gestures at this, but it's too buried. This isn't modesty — it's the honest completion of the meta-circularity analysis.

**Frankie**: I disagree with moving the scope map earlier. The essay's current structure — open with a failure story, then explain failure modes, then provide the scope map — follows a narrative arc: *this is what failure looks like → here's why → here's how to avoid it*. Moving the scope map to the top turns it into a decision tree instead of a narrative. The practitioner reading path in essays/README already points skeptics to this essay. Let the narrative work.

**Joe**: On positioning — this essay belongs on the Skeptics path, which it's already been added to. But I'd also suggest it as a *recommended prerequisite* before running `/committee` for the first time. The quickstart guide should reference it: "Before running your first committee, read the limitations document so you know what to watch for." That's how safety manuals work in practice — you read them before operating the equipment, not after.

**Tammy**: On the question of whether it helps uptake — I think we're overthinking this. The essay exists. It's well-written. It's honest without being self-destructive. The four robust actions from the adoption-strategy committee were: Start Here guide, worked example, limitations doc, monitoring. This delivers the limitations doc. The strategic question is whether the other three actions get done, not whether this one is perfect.

### Round 1 Analysis

- **Emerging consensus**: Publish with minor revisions. The essay delivers on its promise but needs two additions: explicit acknowledgment that failure modes are predicted (not empirically documented) and a more prominent note about unknown unknowns.
- **Disagreement**: Scope map positioning (Vic wants it earlier; Frankie defends current narrative structure).
- **New development**: Joe's suggestion to reference the essay in the quickstart guide as a prerequisite for first committee use.
- **Status**: Near resolution.
- **Next**: Final challenge — any failure modes the essay missed?

---

## Round 2

**Chair**: Before we resolve — does the essay miss any failure modes?

**Maya**: One. **The asymmetric power problem.** When someone in authority uses the committee's output to justify a decision, the committee's formal apparatus creates an asymmetry. The subordinate who disagrees now has to challenge not just the boss's judgment but a five-person committee, independent evaluation, and rubric scores. The methodology can be weaponized — not because it's designed that way, but because formal processes always advantage the person who controls them. "I ran the committee and it agreed with me" is a more powerful rhetorical weapon than "I think we should do X." The essay's Failure Mode 4 (user abdicates editorial role) touches this, but from the user's perspective, not from the perspective of people affected by the user's decision.

**Vic**: That's a real failure mode, but I'd argue it's out of scope. Every decision tool — from spreadsheets to consultant reports to board votes — can be weaponized to justify predetermined conclusions. This isn't unique to cyberneutics. Including it risks making the essay about organizational power dynamics rather than methodology limitations. I'd note it in a line rather than a full section.

**Joe**: Another gap, smaller: the essay doesn't address **model capability degradation over time**. LLM capabilities change — models get updated, retrained, fine-tuned, or replaced. A committee that worked well with Model A might fail with Model B. The character calibration examples in the roster were developed with specific model behavior. If the model changes, the calibration might be wrong. This is a practical operational concern, not a theoretical one, and it belongs in the troubleshooting guide more than in this essay. But it's worth mentioning.

**Frankie**: I want to defend the essay against a critique I expect from external readers: "This is all very meta — an LLM writing about how LLMs fail. How can I trust the failure analysis?" The essay's self-application section addresses this, but I think the essay needs a stronger closing that says something like: "The ultimate validation of this analysis is whether practitioners who read it make better decisions about when and how to use the methodology. Track that. If they do, the essay earned its place. If they don't, it was credibility theater." The current closing — "Results, not resolutions" — gestures at this but could be more direct.

**Tammy**: I want to note something the essay does well that we haven't praised: it applies the methodology's own concepts to itself. The scope map uses Dervin's situation-gap-bridge model implicitly (is the difficulty about complexity or complication?). The detection heuristics are the methodology's evidence standards turned inward. The self-application section is the methodology's self-referential loop made explicit. This is how you demonstrate that a methodology is coherent — you show it can analyze itself without breaking. The essay does this well, and it should be noted as a strength, not just as a potential trap.

### Round 2 Analysis

- **New failure mode identified**: Asymmetric power problem (Maya). Consensus: real but out of scope for a full section; worth a brief mention.
- **Operational concern identified**: Model capability degradation (Joe). Consensus: belongs in troubleshooting guide, not this essay; worth a brief mention.
- **Closing could be stronger**: Frankie suggests tying the closing to practitioner outcomes more directly.
- **Status**: DELIBERATION COMPLETE.

---

## Final Consensus

- **Verdict**: **Publish with minor revisions.** The essay delivers on its stated purpose — honest engineering assessment of the methodology's limitations. It will strengthen the project's credibility with serious practitioners.
- **Specific revisions recommended**:
  1. Add a brief explicit statement that these are predicted failure modes, not empirically documented ones. (Vic, Joe)
  2. Expand the self-application section's note about unknown unknowns — the failure modes invisible from within the training distribution deserve more than two sentences. (Maya)
  3. Consider adding a one-line mention of the asymmetric power problem (methodology outputs used to justify predetermined conclusions) in Failure Mode 4. (Maya)
  4. Consider adding a one-line mention of model capability degradation as an operational concern. (Joe)
- **Structural decision**: Keep the scope map where it is (Frankie's narrative arc argument prevailed over Vic's accessibility argument). The essays README already points skeptics to this essay.
- **Integration recommendation**: The quickstart guide should reference this essay as recommended reading before first committee use. (Joe)
- **Uptake assessment**: The essay will help, not hurt, adoption. The positive feedback loops (trust-building, self-selection) dominate the negative ones (deterrence, over-correction). (Tammy)

Status: DELIBERATION COMPLETE.

---

## KEY TENSIONS IDENTIFIED

1. **Honesty dial**: How much should the essay cost the methodology's credibility? Maya wants it to cost more (naming the paradox isn't enough to escape it). Frankie wants it to serve the mission (honest but not demoralizing). Resolved: the essay strikes a reasonable balance; Maya's revision request (expand unknown unknowns) tightens it.
2. **Empirical vs. conceptual**: All failure modes are predicted, not observed. This is appropriate for the methodology's stage but should be explicit. Resolved: add a brief statement.
3. **Scope of failure analysis**: Should the essay cover organizational dynamics (weaponization), operational concerns (model degradation), and psychological postures (maintaining genuine uncertainty)? Resolved: keep focus on methodology failures; mention adjacent concerns briefly.

## ASSUMPTIONS SURFACED

- **The target audience is sophisticated practitioners** (Maya, Tammy). The essay's tone and specificity are calibrated for readers who already have some methodology experience or technical sophistication. Less technical readers might find it dense.
- **Honest limitations build trust** (all). This is an empirical assumption, not a certainty. Joe's historical examples (Agile, Design Thinking, Lean Startup) support it but are suggestive, not proof.
- **The positive feedback loops will dominate** (Tammy). Whether trust-building and self-selection outweigh deterrence and over-correction depends on the audience composition. If most potential adopters are risk-averse, deterrence might dominate.

## EVIDENCE REQUIREMENTS

- **For the essay's impact on adoption**: Track whether practitioners who read the limitations essay before engaging have different retention/success rates than those who don't.
- **For the failure modes themselves**: As the methodology gets more use, document actual failure cases and compare to the predicted modes. Update the essay with empirical data as it becomes available.
- **For the credibility hypothesis**: Ask early adopters directly: "Did the limitations document affect your trust in the methodology? How?"

## DECISION SPACE MAP

- **Publish as-is**: Fast, low cost. Risk: misses the improvements that would make it stronger.
- **Publish with minor revisions**: Small time investment. Addresses the committee's specific concerns. **This is where the consensus sits.**
- **Major revision**: Restructure, add new failure modes, expand scope. Not warranted — the essay is strong enough that major revision would be over-engineering.
- **Don't publish**: Loses the credibility and self-selection benefits. Not recommended by any committee member.

## RECOMMENDED NEXT STEPS

1. Apply the four specific revisions identified by the committee.
2. Add the essay to the quickstart guide's recommended reading.
3. Set up tracking for whether the essay affects practitioner engagement patterns.
4. Revisit the essay after 3-6 months of methodology use to add empirical failure cases.
