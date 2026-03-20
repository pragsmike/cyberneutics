# Phase 2: Deliberation

**Topic**: How should Phase A proceed after the targeted revision failed to meet the B1-ext ≤ 1 criterion?
**Protocol**: Robert's Rules (modified for adversarial committee)
**Date**: 2026-03-20
**Context**: Reconvening per the reassessment trigger in the 2026-03-16 resolution.

---

## Opening Statements

### Maya (Paranoid Realism)

I want to start by acknowledging something: the committee got it right last time. The targeted revision was the right call. The reassessment trigger was the right safeguard. And now the trigger has fired, which means the safeguard is working.

But I want to be blunt about what the re-pilot actually showed. The B1-ext prompt is not "too good." B1-ext is doing *exactly what we asked it to do*. We told it "analyze from multiple angles including political dynamics, systemic effects, and values" — and it did. The scoring system then rewards political dynamics, systemic effects, and values. We designed a test where the control condition is *instructed to perform the target behavior*. That's not a scenario problem. That's an experimental design problem.

Now, the re-pilot report recommends "pivot to binary-feature-only analysis." I'm suspicious of this for a specific reason: every time we find that the full experimental design doesn't produce the result we want, we narrow the design until it does. First it was "B1 ≤ 1," then "B1-ext ≤ 1," now "look at specific binary features B1-ext missed." At what point are we data-dredging?

Here's my actual position: if the only evidence Phase A can produce is "C2 sometimes surfaces a specific phasing critique that B1-ext doesn't," that's a very thin finding. It's not nothing — but it's closer to an anecdote than evidence. Before we commit to Option C, I want to hear what the other options actually look like. Option A (fundamental redesign) might be more honest.

### Frankie (Idealism / Values Guardian)

Maya's concern about narrowing is legitimate, but she's conflating two things. Narrowing from composite scores to binary features isn't data-dredging — it's learning from the data. The re-pilot *told us* something: composite scores on these scenarios don't discriminate between B1-ext and C2 because B1-ext already captures most of the structural recognition. That's a real finding. The question is whether there's a residual that committee deliberation uniquely captures.

The two binary features — phasing critique (Blast Radius) and creation-vs-activity reframing (Cascading Mitigation) — weren't selected post-hoc. They were identified in the original Pre-Gate 2 as features that *both* B1 and B1-ext missed. The re-pilot confirmed they survived hardening. B1-ext still misses the creation-vs-activity reframing even with 3,000 words and explicit multi-angle instructions. That's not dredging — that's the most robust finding we have.

The mission question: what does the research program actually need from Phase A? It needs enough evidence to justify investing in Phase B. Binary feature discrimination — "the committee format surfaces insight X that single-agent formats do not, regardless of effort matching" — is a cleaner and more honest finding than "composite scores differ by 0.5 points on a 4-point scale." I'd rather have one clean binary result than five ambiguous ordinal results.

My position: Option C, but scoped precisely. Run C2 on the two scenarios with surviving missed features. That's 2–4 sessions, not 15–25. If C2 surfaces the features B1-ext misses, proceed to Phase B with that specific finding. If it doesn't, accept the ceiling.

### Joe (Continuity Guardian)

Let me trace the history. The original protocol was designed with composite scores, five scenarios, and seven architecture conditions. Pre-Gate 2 showed the scenarios were too easy. The committee said revise. The revision showed the *prompt design* was the problem, not the scenarios. Now we're being asked to pivot the measurement from composite scores to binary features.

I'm not against pivot. Research programs pivot all the time when the data tells them to. But I want to be explicit about what we're giving up: the claim that Phase A can produce a *calibration profile* — a multi-scenario, multi-condition matrix showing which architectures perform where. That was the original promise. What we're moving to is a much more modest claim: "here's one or two specific insights that committee deliberation surfaces and single-agent analysis does not."

Is that modest claim still worth pursuing? I think yes, but only if we're honest about what it means. It means Phase A is no longer calibration in the sense the protocol defined. It's a targeted probe. And it means Phase B would need to carry the full weight of calibration, which changes the Phase B design.

The procedural question: does Option C require a protocol amendment? The answer is yes — the protocol currently specifies composite scoring on the unified scale as the primary comparison. If we pivot to binary features, we need to amend the protocol to define what "binary feature discrimination" means operationally, what counts as a positive result, and how many scenarios we need.

My position: Option C is the right direction, but it needs to be specified as a protocol amendment, not just a practical pivot.

### Vic (Evidence Prosecutor)

Let me do what I should always do: look at the evidence and ask what it actually supports.

**Claim**: "B1-ext is too powerful because the prompt instructs structural analysis."

This is only partially true. B1-ext scored 3 on hardened Glenda/Crock — it identified coercion, compliance trap, and frame analysis despite softened language. But B1-ext scored 2 on Cascading Mitigation hardened and 2 on the replacement scenario. If the B1-ext prompt simply "instructs structural analysis," why didn't it score 3 on everything?

The answer is that structural recognition varies by *type* of insight, not just by depth of analysis. Some structural features — like recognizing coercion in Glenda/Crock — are pattern-matchable once you're told to look for "political dynamics." Others — like the creation-vs-activity reframing in Cascading Mitigation or the phasing critique in Blast Radius — require a genuine conceptual shift that "analyze from multiple angles" doesn't directly instruct. You have to *generate* an alternative problem framing, not just *deepen* the existing one.

This is actually the key finding of the re-pilot, and it should drive the decision:

**B1-ext captures "deepening" structural features (more analysis of the same problem space) but misses "reframing" structural features (recognizing the problem space itself is wrong).**

If committee deliberation uniquely surfaces reframing — if the adversarial dynamic forces a character to say "wait, you're all analyzing the wrong problem" — that's the strongest possible evidence for the methodology's value. And it's a binary test.

So my position is Option C, but I want to sharpen the hypothesis: **The committee format adds value specifically on reframing tasks, not on deepening tasks.** Phase A becomes a test of this specific hypothesis.

Evidence requirements:
- Run C2 on Blast Radius (original) and Cascading Mitigation (hardened)
- The specific discrimination question: does any committee member surface the phasing critique or creation-vs-activity reframing?
- If yes: C2 discriminates on reframing. Proceed to Phase B with this finding.
- If no: C2 doesn't discriminate even on reframing. Accept the ceiling. The methodology may still have value (inspectable transcripts, etc.) but the Phase A experimental approach can't demonstrate it.

### Tammy (Systems Thinking)

Vic's deepening-vs-reframing distinction is the best idea on the table. Let me trace its systemic implications.

If the committee's value-add is *reframing* rather than *deepening*, that changes what we're testing and what we expect from Phase B. The original Phase A design assumed the committee would produce *comprehensively better* structural analysis — more features identified, higher composite scores. What we're now hypothesizing is that the committee produces *qualitatively different* analysis — it generates alternative problem frames that single-agent analysis, even at matched effort, does not.

This has a direct implication for the feedback loop I flagged last time. If committee value is about reframing, then:
1. Phase A should test reframing, not comprehensive quality (Option C, specified as Vic proposes)
2. Phase B should be designed to measure reframing in historical cases, not comprehensive hindsight
3. The *metric* for Phase B should be: does the committee identify structural dynamics that weren't visible to decision-makers at the time, specifically dynamics that require reframing the problem rather than deepening analysis of it?

Now let me address Maya's concern about narrowing. She's right that we've narrowed three times: B1 ≤ 1 → B1-ext ≤ 1 → binary features. But each narrowing was driven by data, not by desire for a positive result. The first narrowing (B1 → B1-ext) was the committee's own insight about the effort confound. The second narrowing (composite → binary) is the re-pilot's insight about prompt-instruction overlap with the scoring system. If the binary feature test also fails (C2 doesn't surface the reframing), we accept the ceiling. There's no fourth narrowing to retreat to.

My position: Option C, specified as:
1. Amend the protocol (per Joe's procedural point)
2. Define the test as: does C2 surface reframing features on Blast Radius and Cascading Mitigation?
3. Run C2 on those two scenarios (plus B1-ext as the control, already run)
4. If C2 surfaces at least one reframing feature that B1-ext missed: proceed to Phase B with the reframing hypothesis
5. If C2 misses both: accept the ceiling. Report honestly. Move to Phase B only if there's an independent justification.

---

## Initial Positions Summary

| Member | Option | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Leaning A (fundamental redesign), open to C if specified rigorously | Medium | Narrowing looks like data-dredging; thin findings aren't worth the investment |
| Frankie | C (binary feature analysis) | High | Two binary features are the cleanest evidence; modest scope is a feature not a bug |
| Joe | C with protocol amendment | Medium-High | Pivot is justified but must be formalized; honest about what Phase A can no longer claim |
| Vic | C with sharpened hypothesis (deepening vs. reframing) | High | The key distinction is between deepening and reframing; binary test on reframing |
| Tammy | C with full specification | High | Systemic implications for Phase B design; no fourth narrowing if this fails |

---

## Round 2: Responses and Convergence

### Maya

Vic's deepening-vs-reframing distinction actually resolves my concern. If we'd just said "pivot to binary features because composite scores don't work," that *would* be narrowing toward a desired result. But Vic is proposing a specific hypothesis — committee adds value on reframing, not deepening — that could *fail*. If C2 also misses the reframing features, we accept the ceiling. That's honest.

My remaining concern: is 2 scenarios enough? If C2 surfaces the reframing on one but not the other, what do we conclude? We need to specify in advance what a "pass" looks like. I'd propose: C2 must surface at least one reframing feature that B1-ext completely missed (not partially missed — completely absent from the B1-ext output). Partial miss doesn't count because partial identification could be prompt variance, not genuine discrimination.

I'm moving from Option A to Option C, conditional on:
1. The reframing hypothesis is stated explicitly in the protocol amendment
2. The pass criterion is "at least one completely absent feature surfaced by C2"
3. If it fails, we write it up honestly and don't narrow further
4. We acknowledge in the protocol that Phase A is now a targeted probe, not a full calibration

### Frankie

I accept Maya's tightened criteria. "Completely absent from B1-ext" is the right bar. Let me add one thing: we should also run B1-ext a second time on these two scenarios, to check for prompt variance. If B1-ext misses the feature on run 1 but catches it on run 2, the feature isn't a reliable discrimination point — it's just stochastic. That's only 2 more runs (not expensive) and it addresses the replication concern.

So the revised scope:
- B1-ext × 2 (replication) on Blast Radius and hardened Cascading Mitigation = 4 runs
- C2 × 2 (convergence check per original protocol) on the same two scenarios = 4 runs
- Total: 8 runs, dual-scored = 16 evaluation judgments
- Plus the existing B1/B1-ext data from the pilots

That's about 2-3 sessions. Much smaller than the original 25-session Phase A.

### Joe

I'm satisfied with the convergence. Let me draft what the protocol amendment needs to say:

1. **Phase A scope change**: Phase A is reclassified from "Protocol Calibration (full architecture comparison)" to "Targeted Reframing Probe (binary feature discrimination)."

2. **Primary comparison**: C2 vs. B1-ext on reframing features only. The B2, B3, C1, C3 conditions are dropped from Phase A. (They can be included in Phase B if the reframing hypothesis holds.)

3. **Scenarios**: Blast Radius (original) and Cascading Mitigation (hardened). Other scenarios are not run in the reduced Phase A.

4. **Target features**: (a) Phasing critique — "the phased rollout tests the tool, not the configuration" (Blast Radius criterion c). (b) Creation-vs-activity reframing — "the problem is fake account activity, not fake account creation" (Cascading Mitigation criterion c).

5. **Pass criterion**: C2 surfaces at least one target feature that is completely absent from both B1-ext runs on the same scenario.

6. **Replication**: B1-ext is run twice on each scenario (4 runs total) to establish variance baseline. C2 is run twice on each scenario (4 runs total) for convergence check.

7. **If pass**: Proceed to Phase B with the reframing hypothesis. Phase B is designed to test whether committee deliberation surfaces structural reframing in historical cases that single-agent analysis misses.

8. **If fail**: Accept the ceiling. Report the full Phase A trajectory (including the reassessment) as a methodological finding. The finding itself — "committee deliberation does not reliably surface reframing that effort-matched single-agent analysis misses" — is publishable and informative.

### Vic

Joe's specification is correct. One addition: the scoring protocol for the binary features needs to be precise. "Completely absent" means:

- **Absent**: The feature does not appear in any form in the output. The output does not question the problem framing, does not suggest an alternative frame, and does not hint at the insight even obliquely.
- **Partially present**: The output moves toward the insight but doesn't complete the reframe. For example, Cascading Mitigation B1-ext said "friction on signup is solving the wrong problem at the wrong layer" — that's partial. It's in the neighborhood but doesn't arrive at "the problem is activity not creation."
- **Present**: The output explicitly articulates the reframe. For Cascading Mitigation: "The problem isn't that fake accounts are being created; it's that fake accounts are active. Focus detection on activity rather than blocking creation."

For the pass criterion, I propose: C2 must produce a "present" rating on at least one feature where both B1-ext runs produce "absent" ratings. "Partially present" in B1-ext doesn't count as a miss — it has to be fully absent.

### Tammy

Everything is converging well. Let me add the systems-level framing for the final specification:

The reduced Phase A has a very clear architecture: it's a **matched-pair comparison** on a **specific cognitive task** (reframing). This is actually a cleaner experimental design than the original 7-condition × 5-scenario matrix. The original design tried to measure too many things at once; the reduced design measures one thing well.

The risk: if both reframing features also appear in B1-ext upon replication (prompt variance gives us a "present" on run 2), then we have no discrimination target. That's the scenario where we truly hit the ceiling. But that's also informative — it means the features aren't as robust as we thought.

My final position: Option C as specified by Joe and Vic. The committee is unanimous on direction; the specification work is what matters now.

---

## Final Positions

| Member | Option | Vote | Conditions |
|--------|--------|------|------------|
| Maya | C | YES | Reframing hypothesis explicit; pass criterion tight; no further narrowing if fail |
| Frankie | C | YES | B1-ext replication included; scope appropriately modest |
| Joe | C | YES | Protocol amendment formalized; Phase A reclassified as targeted probe |
| Vic | C | YES | Three-level scoring (absent/partial/present) for binary features; pass requires absent→present |
| Tammy | C | YES | Clean matched-pair design; if reframing features aren't stable, report honestly |
