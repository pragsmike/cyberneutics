---
plan:
  created: 2026-04-20
  source: "Committee deliberation on essays coherence audit"
  situation_dir: "../situations/essays-coherence-audit/"
  final_score: 13/15
  deliberation_status: "PASSED (post-remediation); verdict caveated to Claude-trained evaluative standards"
  owner: mg
---

# Essays Coherence Remediation Plan

This plan is the actionable residue of the **Essays Coherence Audit** committee deliberation run on 2026-04-20. Full record lives in `../situations/essays-coherence-audit/deliberations/` (00-charter → 06-evaluation-2). This file is the durable, repo-local plan so the work survives the situation-directory workflow and gets committed with the repository.

## The verdict in one paragraph

The essay collection contains **coherent intellectual work by Claude-trained evaluative standards**. The four-pillar synthesis (Dervin + von Foerster + Deleuze + Pask + distributional semantics) composes as an architecture. The palgebra isomorphically formalizes pipeline structure. Five Claude subagents running with different propensities converged on "substance, needs refinement" rather than "mishmash" — but the committee itself acknowledged a structural limit on that verdict: **shared training installs shared priors about what counts as intellectual substance, so the committee cannot distinguish "genuine substance" from "coherence within Claude's evaluative frame" without external (non-Claude, non-author) review.**

The plan below addresses three gap types the committee named: **scope overreach** (essays imply the formalism captures more than it does), **empirical under-support** (the central "methodology produces better decisions" claim has a null result and zero outcome-tracked real-world decisions), and **self-application opacity** (the essays argue human gates are load-bearing while showing no visible artifact of gates operating in their own production). A fourth track — **external-tradition review** — tests whether the verdict survives outside the Claude-trained frame.

## Load-bearing caveats recorded

Two residual tensions from the deliberation that should be preserved for future readers of this plan:

1. **Vic vs. Tammy.** Structural soundness vs. empirical validation. Committee consensus: operational claims ("committee produces better decisions") require operational evidence; structural claims can earn limited confidence on their own terms. Both characters' positions retained in the resolution.
2. **Maya vs. Frankie.** Interpretive stance on the safety essay. Maya reads strategic positioning; Frankie reads principled substance surviving strategic pressure. Both accept the essay is real work; they differ on whether strategic function contaminates principled content. Not resolved.

## P0 — First-pass edits (~2–3 hours of focused work)

Each item names file, section, and intended change. These are scope-narrowing + prior-art engagement + falsifiability patches.

1. **`essays/societies-of-thought-synthesis.md` opening paragraph.** Lead with the disanalogy (trained reasoning models ≠ prompting-based committees), not the apparent convergence. Change the "provides empirical validation" framing to "provides empirical support for the hypothesis that multi-perspective reasoning matters, but does not validate external committee prompting as an implementation strategy without transfer-learning evidence." *(Maya, Vic)*

2. **`essays/when-methodology-fails.md` §Failure Mode 2.** The essay's top-of-file preamble (line 25) already mentions the Phase A null honestly; the specific Failure Mode 2 subsection does not lead with it. Add a lead-in to Failure Mode 2 that restates the Phase A result verbatim and treats it as primary evidence for the failure mode rather than a trailing reference. *(Maya)*

3. **`essays/when-methodology-fails.md` §Failure Mode 6.** Add a concrete falsification criterion. Currently the "methodology fails when it answers the wrong question" framing is an immunity capsule — any bad outcome can be attributed downstream to the user. Specify: "If three external practitioners report they used this methodology and made decisions worse than their prior judgment, that counts as genuine failure, not misapplication." Or a similar concrete threshold. *(Vic)*

4. **`essays/05-the-synthesis.md` — new subsection "What Winograd & Flores Got Right".** After the Grand Unification section, before Why This Matters for AI. Quote their core objection (formal equivalence ≠ capability equivalence; formal systems cannot capture situated action). Explain what the synthesis *accepts* from their critique (irreducibility of situated judgment) and what it *diverges* on (human-gate preservation rather than full formalization). *(Joe)*

5. **`essays/08-from-methodology-to-formalism.md` — new subsection "What Formalization Cannot Do".** State explicitly: the palgebra formalizes pipeline structure and quality propagation; it does *not* formalize situated judgment. The human gate preserves Winograd's insight rather than eliminating it. This narrows the scope of the formalism's claim and addresses Joe's prior-art objection at the structural level. *(Tammy, Joe)*

6. **`essays/12-potential-to-sense.md` §4 — engage Dreyfus directly.** Add a paragraph: "Dreyfus argued tacit understanding cannot be formalized. He was right about models in isolation. But when understanding is distributed across a human-AI feedback loop, the AI doesn't need to formalize situation; it formalizes *alternatives*. The human provides situation. This reduces the problem's scope — not a solution to Dreyfus, a bypass." *(Joe)*

7. **`essays/05-the-synthesis.md` and `essays/11-conversation-theory.md` — distinguish structural from empirical claims.** Name which of "bridge = feedback = differentiation = teachback" moves are structural (four frameworks converging on the same shape) vs. empirical (this architecture produces better decisions). State which are tested and which are hypotheses. *(Tammy)*

## P1 — Second-pass additions (self-application + case material + bounded-claim appendix)

8. **Create `agent/theoretical-revision-log.md`.** For each numbered essay, document instances where an LLM draft contradicted prior work and was revised. If no such instances exist — as the remediation-round investigation suggests — the document should say so explicitly. This is the honest resolution of Frankie's retrofit challenge. *(Frankie, Tammy)*

9. **Expand `wild/diary/2026-04-13-convergences.md` with a Categorical Pun Registry.** For claims like "fan is coalgebraic, funnel is algebraic," state "Status: metaphorically suggestive, not yet validated by domain experts. Awaiting review by ACT practitioners." Moves implicit honesty to explicit. *(Frankie)*

10. **Create `essays/design-decisions.md`.** Document three-essay sequences where new essays *did* constrain earlier ones (if any). If no such instances exist, the document should say so — "essays are consistent and cross-referenced; we have no evidence of new essays forcing rewrites of old ones due to discovered contradiction." Honest. *(Frankie)*

11. **Add case material to `essays/02-from-practice-to-theory.md`.** Section title: "One Example: Where the Methodology Changed the Output." Real abbreviated deliberation transcript showing initial question, naive AI response, committee reframing, decision made differently, outcome. Without at least one of these, the practitioner path ends in artifacts with no worked example. *(Joe, prior editorial-review finding)*

12. **Create appendix `essays/formalism-as-bounded-claim.md`.** ~2000 words. Position the palgebra as scaffolding for disciplined reasoning, not complete capture of situated understanding. Explain what formal composition breaks down on and why that's acceptable. Give Winograd & Flores the last word. *(Joe)*

13. **Create `essays/open-questions-empirical.md` appendix.** Testable predictions with falsification criteria: monotone confidence propagation prevents premature collapse; committee deliberation explores the decision space more thoroughly than single-agent generation; repeated runs reveal stable eigenforms that unseen tests respect. Each prediction names what would validate or falsify. *(Tammy)*

14. **Add to `essays/12-potential-to-sense.md` §"The Self-Application Test".** If human gates are load-bearing and the essays were LLM-assisted, what evidence would show the gates doing work in the essays' own production? State the test; name whether the evidence has been gathered. *(Tammy, Frankie)*

## P2 — Research commitments (ongoing)

15. **External human review (added in remediation).** Commission three scholars from non-Claude-trained evaluative traditions — proposed: historian of ideas, continental philosopher, pragmatist engineer — each independently assessing whether the essay collection constitutes intellectual substance *by their own field's criteria*. This is the test the committee named as the one that would genuinely update the "intellectual substance" verdict. Without it, the verdict remains caveated. *(Maya, added in remediation)*

16. **Create `research-programs/outcome-tracking-protocol.md`.** Lightweight system: (decision, pre/post confidence, 6-12 month outcome, match assessment). Populate with 3-5 real decisions from the Cyberneutics team's own work as initial calibration data. *(Vic)*

17. **Add to `palgebra/reference.md` §"Confidence Monotonicity in Practice".** Specify operationalized test (confidence on 0-100 at pipeline input/output). Provide 3-5 worked examples from existing deliberations. Current state: unfalsifiable. Target: empirically checkable. *(Vic)*

18. **Run the Committee Advantage study.** N=12 real organizational decisions. Treatment: `/committee` with standard roster on Claude Sonnet. Control: single Claude Sonnet with same token budget, instructed to "analyze from multiple perspectives." Outcome measure at 6 months: outcome match, insight novelty, decision-maker regret, avoided failure modes. Pre-registered prediction: committee ≥15% higher on outcome match. Failure threshold: no significant difference → central claim not supported. **Outstanding work needed:** power analysis, operationalization of "outcome match," blinding protocol, inter-rater reliability plan. *(Vic, with post-remediation review caveats)*

## What this plan does NOT do

- **Does not declare the methodology validated.** The Phase A null is still there. The P0 edits make the gap visible; they do not close it.
- **Does not settle the self-application question by itself.** P1 #8 and #10 either produce evidence of genuine mutual-constraint or honestly record that the evidence is not there. Either outcome is acceptable; the plan demands honesty, not a specific finding.
- **Does not assume P1 #15 (external human review) will validate the verdict.** If the three external reviewers conclude the essays are hollow by their field's criteria, the methodology's status becomes genuinely open. The plan accepts that risk.
- **Does not specify a checkpoint schedule.** A follow-up review is recommended at 3 months (P0 complete check) and at 12 months (P2 study first results).

## Not part of the plan (recorded for future reference)

- **Maya's substitution test** — replacing Pask's teachback in Essay 11 with an incompatible framework (Bayesian updating, strict correspondence theories) to check if Essay 12 still works. Proposed as a falsifiability probe for Tammy's architectural-dependency claim. The committee declined to run it because it is genuinely destructive of the corpus as currently written. If future questions about architectural rigidity reopen, this test is available.
- **Multi-model committee run.** The underlying epistemological fix for the five-Claude-subagent problem is to run the same deliberation with different base models. This is the subject of the existing `research-programs/multi-model-committee.md` program and is already in-scope there. Not duplicated here.

## Execution sequencing

**Week 1–2.** P0 items. Small, mechanical, no dependencies. Probably 2-3 hours of focused editing.

**Sprint 1 (weeks 3–6).** P1 items. Items 8 and 10 likely produce honest "no-evidence" findings; items 11 and 12 require more original writing. Item 14 depends on item 8.

**Sprint 2+ (months 2+).** P2 items. Item 15 (external review) should begin commissioning as soon as P1 #8 produces a result — the external reviewers should see both the essays and the theoretical-revision-log so they can evaluate the coherence claim honestly. Items 16-18 are research-program work that may take 6-12 months.

**Checkpoints.**
- At P0 complete: re-run `/editorial-review` to confirm scope narrowing landed.
- At P1 complete: revisit the resolution in `../situations/essays-coherence-audit/`; amend if findings from #8, #10 require it.
- At 12 months: assess P2 progress; if committee-advantage study (#18) is not yet designed in detail, the central empirical claim remains unvalidated and the verdict should be re-examined.

## Provenance

Full deliberation record: `../situations/essays-coherence-audit/deliberations/` (checked out of this repo; lives in the external situations directory per the repo's situation-dir convention).

- `00-charter.md` — Problem statement and success criteria
- `01-roster.md`, `01-convening.md` — Committee composition and experimental setup notes
- `02-deliberation.md` — Full transcript (Round 1 + Round 2 + remediation summary)
- `03-resolution.md` — Committee verdict (updated post-remediation)
- `04-evaluation-1.md` — Independent review, Round 1 (10/15, below threshold)
- `05-remediation-1.md` — Motion to recommit, committee response
- `06-evaluation-2.md` — Independent review, Round 2 (13/15, at threshold)

**Deliberation score evolution:** 10/15 (initial) → 13/15 (post-remediation). The key improvement was in Adversarial Rigor and Assumption Surfacing — the committee turned on its own epistemology in remediation rather than preserving its authority.
