# Phase 2: Deliberation

**Topic:** How to correct mathematical errors in soft-type-theory §§5-7
**Protocol:** Modified Robert's Rules
**Input:** 07-mathematical-review.md (scoped mathematical review, tiered verification plan)

---

## Opening Statements

### Vic (Evidence Prosecutor)

Let me structure this. The review found five issues at three severity levels. I want to take them in order of mathematical certainty — start with what we *know* is wrong, then handle what's ambiguous.

**Finding 1 (§5, oplax): Clear error, clear fix.** The collapse functor satisfies collapse(a ⊗ b) ≤ collapse(a) ⊗ collapse(b). That's the oplax direction. The document says "lax" and says the collapse "may exceed," both backwards. The proof is three lines: sum(cmin(a,b)) ≤ sum(a) because min(aᵢ, bᵢ) ≤ aᵢ for all i. Monotonicity of collapse in the sum gives the result. This is a find-and-replace fix. Change "lax" to "oplax," reverse the inequality description, done.

**Finding 2 (§6, coend ≈ expectation): Genuine equivocation, but the fix is not obvious.** The categorical coend in V_5 is a join (componentwise max). The probabilistic expectation is a weighted average. These are different operations. But I want to understand *what the author was trying to say*. The intuition — that both the coend and the expectation marginalise over a latent variable — is correct. The error is in claiming they're the same construction. The fix needs to preserve the intuition while being honest about the gap.

**Finding 3 (§6, vacuity): This is the hardest.** The coend of a decreasing presheaf on a bounded preorder just returns the value at the top. That's mathematically correct but means the construction doesn't do useful work. The review suggests three possible repairs. The committee needs to decide which one to recommend.

**Findings 4-5 (§7, clarifications): Low severity, straightforward.**

### Maya (Paranoid Realism)

The oplax error is the one that scares me most, and not because it's mathematically hard. It scares me because it's in the *canonical* document — the version that already passed review without anyone catching it. The committee's previous deliberation accepted §5 without scrutiny because it was "technically contained." This is exactly the failure mode I warned about: containment is not correctness.

The fix for oplax is easy. But I want the committee to ask: what else in §5 might be wrong? The review only spot-checked the collapse functor because Maya-in-the-prior-deliberation flagged it. What about the claim that V_5 is monoidal closed? That Rosenthal 1.2.2 applies componentwise? The review verified claim 3 (cocompleteness) but didn't verify monoidal closure. If we're fixing §5, we should at minimum flag what we've verified and what we haven't.

On the coend equivocation: the review's diagnosis is correct and devastating. The "≈" on line 613 is doing the work of an entire theorem that doesn't exist. The document needs to either prove the bridge or admit it's an analogy. I favor admitting it's an analogy because proving the bridge would require changing the enrichment base from a quantale to a semiring, which rewrites the entire document.

### Frankie (Idealism / Values Guardian)

Maya's instinct to expand the review scope is understandable but misplaced here. The charter says: correct the errors found, don't audit the entire document. We have a tiered review that verified the Tier 1 claims. Expanding scope now would violate the same principle of proportionality the committee established in the prior deliberation.

On the substantive issues: the methodology requires honest formalization. The coend section currently *dishonest* formalization — it presents an equivocation as a derivation. That's the worst kind of error for a document that will face professional review. A professional mathematician will catch it in seconds and lose trust in everything else.

My proposed hierarchy of fixes:
1. Oplax: mechanical fix, do it.
2. Coend ≈ expectation: reframe as analogy with explicit statement of the gap. This is the review's option (a), and it's the honest one.
3. Coend vacuity: acknowledge it, redirect to the universal property interpretation.
4-5. Clarifications: add the bridging sentences.

The key principle: **better to have an honest gap than a dishonest bridge.** A professional reviewer will respect "we note that the categorical coend and the probabilistic expectation are different constructions sharing the intuition of marginalisation" far more than they'll respect "≈" covering a chasm.

### Joe (Continuity Guardian)

I want to calibrate the scope of changes. The canonical document (soft-type-theory.md) has §§1-5, of which §§1-4 went through a prior mathematical consistency review and are considered stable. The v2 document has §§1-8, where §§6-7 are the new material. The proposed changes are:

- §5 in both documents: change "lax" to "oplax," reverse inequality description. ~5 lines changed.
- §6 in v2 only: rewrite the coend-expectation passage, add acknowledgment of vacuity. ~30-40 lines changed.
- §7 in v2 only: add bridging sentence for canonical topology, relabel mechanism design connection. ~5-10 lines changed.

The §5 fix is safe. It's a terminology correction that doesn't change the mathematical content — the inequality itself is stated correctly in the preceding lines (sum(cmin) ≤ sum(a)), it's only the *label* that's wrong.

The §6 changes are the riskiest. We're rewriting the section's central claim. I want to see the exact proposed text before voting, not just a description of what to change.

### Tammy (Systems Thinker)

I want to trace the dependency graph of the proposed changes.

The oplax fix is truly local — nothing downstream depends on whether the functor is called lax or oplax. The discussion of "laxness as a genuine feature" (which is really about boundary-coarsening) is phrased in terms of what information is lost, not in terms of the categorical direction. It survives the rename.

The coend rewrite is *not* local. §6 currently promises that the coend provides a computational tool for mixed-type texts. If we downgrade it to an analogy, §8's open questions about "coend approximation for large type lattices" and "soft routing vs. hard routing" lose their formal grounding. They become questions about the *expectation* (which is well-defined but has no categorical backing) rather than the *coend* (which has categorical backing but is vacuous for the case at hand).

This means the fix needs to be two-pronged:
1. Fix the bridge (honest about the gap)
2. Redirect the coend's contribution: its value isn't in computing a number, it's in the *universal property* — any construction that is dinatural in the type variable factors through the coend. This is the review's suggestion (c). The coend becomes a *structural guarantee* (anything you compute that doesn't depend on which type decomposition you chose is canonically determined by the coend), not a *computational tool* (here's how to compute the aggregate grade).

This reframing preserves the open questions: "coend approximation" becomes about approximating the structural guarantee, not the number. "Soft routing" becomes: routing through the coend's universal property vs. MAP estimation.

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Vic | Fix all five, start with what's certain | High | Proposed text must be exact and verifiable |
| Maya | Fix all five, but flag unverified §5 claims | High | Canonical doc has uncaught errors — what else? |
| Frankie | Fix all five, prioritize honesty over elegance | High | Professional reviewer trust is at stake |
| Joe | Fix all five, but want exact proposed text | High | Scope control — don't rewrite more than needed |
| Tammy | Fix all five, but trace dependency graph | High | §6 fix is non-local — affects §8 open questions |

## Key Tensions Identified

1. **Scope of §5 audit**: Maya wants to flag unverified claims beyond the spot-check; Joe and Frankie want to stay within charter scope
2. **Coend section strategy**: Fix the bridge (analogy framing) vs. replace the contribution (universal property framing) vs. both
3. **Level of rewrite**: Minimal corrections vs. restructuring §6 around a different central claim

---

## Round 1: The Oplax Fix and §5 Scope

**Vic:** Let me draft the §5 fix. Three changes needed:

Change 1 (line 442): "This is a lax monoidal functor" → "This is an oplax monoidal functor"

Change 2 (lines 443-448): The sentence "It is *lax* rather than strict because collapsing respects the order (if v ≤ w componentwise then collapse(v) ≤ collapse(w)) but does not strictly preserve the monoidal product — the collapse of a componentwise min may exceed the min of the collapses" → "It is *oplax* rather than strict because collapsing respects the order (if v ≤ w componentwise then collapse(v) ≤ collapse(w)) but does not strictly preserve the monoidal product — the collapse of a componentwise min may fall strictly below the min of the collapses."

Change 3 (line 448): The concrete example needs updating. Currently: "two vectors might each collapse to Medium, but their componentwise min might collapse to Low (if each vector's weak criterion is different and the mins accumulate)." This is actually correct — it shows collapse(cmin) < min(collapse, collapse), which is the oplax direction. The example is right; only the framing around it was wrong.

That's the full §5 fix. Three edits, identical in both documents.

**Maya:** The fix is correct. But I want a one-line addition after the fix: "Note: the remaining §5 claims (V_5 monoidal closure, componentwise residuation) have been verified at Tier 1 (definitional) but not at Tier 2 (bounded construction). The Rosenthal 1.2.2 citation for quantale products has been confirmed; the extension to monoidal closure is straightforward but has not been independently checked against Kelly's axioms for the product enrichment base."

**Joe:** That's scope creep. The review verified claim 3 (cocompleteness), verified claim 1 (monoidal unit), and the enrichment axioms are verified in categorical-structures.md §2b. Adding a disclaimer about monoidal closure is importing doubt where the review found none.

**Vic:** Joe is right on the substance — the monoidal closure of V_5 follows from V_5 being a commutative quantale (Rosenthal) and commutative quantales being monoidal closed (standard). But Maya's instinct has a procedural point: we should distinguish what was reviewed from what was assumed. I propose a compromise: add a remark in the review file, not in the document itself. The document should state facts; the review file should track verification status.

**Tammy:** Agreed. The document's audience is mathematicians who can verify monoidal closure themselves. The review file's audience is us and future agents who need to know what's been checked. Different audiences, different artifacts.

**Maya:** I'll accept that. Note it in the review file, not the document.

### Round 1 Analysis

**Emerging consensus:** Oplax fix is agreed (3 edits, both documents). Maya's scope concern addressed by adding verification notes to the review file, not the document.
**New tension:** None on this finding.
**Status:** Finding 1 resolved.

---

## Round 2: The Coend Equivocation

**Tammy:** I outlined the two-pronged approach in my opening. Let me be more specific about what the rewritten passage should say.

The current text (lines 606-617) claims:
```
∫^C H(C, C) ≈ ∫_T μ_a(dC) · F_a(C)
```

This needs to become two separate statements:

Statement A (categorical): "The coend ∫^C F_a(C) in V_5 is the join (componentwise supremum) of all F_a(C) values over types C ∈ T. For a decreasing presheaf on a bounded preorder, this is the value at the most general type."

Statement B (probabilistic): "Separately, in the distributional setting of §4, the expected score profile E_{μ_a}[F_a] = ∫_T μ_a(dC) · F_a(C) computes the weighted average of score profiles under the type distribution. This is a different operation from the categorical coend — the coend takes a supremum, the expectation takes a weighted average — but both formalise the intuition of marginalising over the latent type variable."

Statement C (the honest bridge): "The two constructions coincide when the type distribution is a delta function (single-type text): both return F_a at the assigned type. For genuinely mixed-type texts, they diverge. The coend provides a *structural guarantee* (any construction dinatural in the type variable factors through it — Kelly 3.10, Proposition 3.73), while the expectation provides a *computational tool* (a single aggregate score for routing). A future treatment might unify them by working in a semiring-enriched setting where the coend computes a weighted sum rather than a supremum, but this would require reworking the enrichment base throughout."

**Vic:** Statement A is correct. Statement B is correct. Statement C's first sentence is correct (delta functions give the same result). The universal property claim (Proposition 3.73) — I need to verify that.

Kelly 3.10, Definition 3.69 defines the coend via the universal property: it is the universal V-object receiving a dinatural transformation from H. Proposition 3.73 (the "Fubini theorem for coends") is about iterated coends. The universal property of the *coend itself* is Definition 3.69, not Proposition 3.73. Let me correct the citation.

The relevant statement is: the coend ∫^C H(C,C) is characterised by the universal property that any family of V-morphisms H(C,C) → X that is dinatural in C factors uniquely through ∫^C H(C,C). This is the content of Definition 3.69 and the paragraph following it.

So Statement C should cite "Kelly 3.10, Definition 3.69" not "Proposition 3.73."

**Frankie:** The three-statement structure is exactly right. It's honest: here's what the categorical construction gives you, here's what the probabilistic construction gives you, here's how they relate, here's where they diverge, here's what would be needed to unify them. A professional reviewer reading this would think: these authors know what they're doing and are being careful about the boundaries.

**Maya:** I want to push on the vacuity issue (Finding 3). Tammy's Statement A says the coend "is the value at the most general type" for decreasing presheaves. This is correct but it means the entire §6 up to this point — the bifunctor H_a, the coend formula, the simplification — is an elaborate derivation of a trivial result. The professional reviewer will notice this. They'll ask: "Why did you develop the coend machinery to compute something you could have read off the presheaf directly?"

**Tammy:** That's the reason for Statement C's reframing. The coend's value is not the *number* it computes (which is trivial) but the *universal property* it satisfies. The universal property says: anything you compute that doesn't depend on which type decomposition you chose is canonically determined by the coend. That's not trivial — it's a coherence guarantee. It tells you that the type-independent computations form a well-defined category with canonical factorisations.

**Maya:** Can you make that concrete? What is an example of a "computation dinatural in the type variable" that a pipeline would actually perform?

**Tammy:** Yes. Consider the "soft routing" of §6 — routing an artifact without committing to a specific type. A soft router assigns processing weights to pipeline branches. The dinatural condition says: the weights assigned by two different type decompositions that agree on refinement overlaps must produce the same routing. If your router satisfies this, it factors through the coend. The coend becomes the canonical input to any type-decomposition-independent router.

**Vic:** That's a good example. But it's a new claim — that soft routing satisfies the dinaturality condition. Is it checkable?

**Tammy:** It would depend on the specific router. For a linear router (weights are the presheaf values), the dinaturality is exactly the presheaf functoriality condition, which we already have. For a nonlinear router, it's an additional constraint.

**Joe:** I'm getting nervous about scope. The charter says "correct the errors found." We're now designing new content — the universal property interpretation, the soft routing dinaturality example. That's development, not correction.

**Frankie:** Joe is right that we're at the boundary. But the review explicitly says the coend section needs restructuring — "consider whether §6 should be restructured around the universal property interpretation." The charter goal is "professional-review readiness," which requires the section to make a non-trivial claim. We're not adding new mathematics; we're reframing what's already there.

**Joe:** Then I want the reframing to be minimal. Tammy's Statements A, B, C with Vic's citation correction. No new examples, no soft routing dinaturality claim. If we want to add that, it goes in the open questions.

**Vic:** I support Joe's constraint. Statements A, B, C, corrected citation. The soft routing dinaturality observation goes in §8 (open questions) as a new bullet: "Does soft routing satisfy the dinaturality condition? If so, the coend provides the canonical input to any type-decomposition-independent router."

### Round 2 Analysis

**Emerging consensus:** Three-statement rewrite of §6's bridge passage (A: categorical coend as join, B: probabilistic expectation as separate construction, C: honest bridge with universal property reframing and semiring-enrichment note). Citation correction: Kelly 3.69 not 3.73. Soft routing dinaturality added to §8 as open question, not to §6.
**New tension:** How much to restructure §6 vs. minimal patch. Resolved toward minimal patch.
**Status:** Finding 2 addressed. Finding 3 (vacuity) addressed within the same rewrite (Statement A acknowledges triviality, Statement C redirects value to universal property).

---

## Round 3: The Sheaf Section Clarifications

**Vic:** Findings 4 and 5 are low severity. Let me propose exact fixes.

**Finding 4 (canonical topology, lines 679-683):** After "a type A is covered by types {B₁, ..., Bₙ} if every artifact that inhabits A also inhabits some Bᵢ," add: "This semantic characterisation is equivalent to the categorical one (the sieve generated by the Bᵢ is a covering sieve for the canonical topology) because the refinement order on T is defined in terms of inhabitation containment (§2): B refines A precisely when every B-artifact is an A-artifact."

**Finding 5 (mechanism design, lines 756-777):** Three changes:
(a) Change "the continuation function k is ill-defined at the overlaps" to "the continuation function k becomes ambiguous at the overlaps, facing a multi-objective optimisation problem rather than a scalar one."
(b) Add "Conjecture:" before "Characters best-responding to inconsistent signals will produce incoherent strategies."
(c) After the paragraph, add: "This connection between sheaf failure and equilibrium incoherence is conjectural — deriving it rigorously would require showing that the composed open game with inconsistent payoffs fails to have a Nash equilibrium or that its equilibria are Pareto-dominated, which we have not attempted."

**Maya:** Finding 4 fix is correct. The bridge sentence is exactly what the review asked for.

Finding 5: I agree with (a) and (c). On (b), the "Conjecture:" label should apply to the entire paragraph starting "If the sheaf condition fails," not just the sentence about incoherent strategies. The whole chain — from sheaf failure to ambiguous k to incoherent equilibria — is conjectural.

**Frankie:** Maya is right. The conjecture isn't just the conclusion — it's the chain of reasoning. Label it: "**Conjecture (sheaf-equilibrium connection).** If the sheaf condition fails..."

**Tammy:** I want to add one thing to Finding 5. The connection between sheaf failure and equilibrium incoherence has a testable prediction: if we observe rubric inconsistencies at type overlaps (checkable via §5's vector scores) and simultaneously observe committee deliberation failures (detectable via the evaluation rubrics), the correlation would support the conjecture. This is a concrete empirical test that could go in §8.

**Joe:** That's a good open question. Add it to §8: "Empirical test of the sheaf-equilibrium conjecture: does rubric inconsistency at type overlaps correlate with lower evaluation scores in committee deliberations?"

**Vic:** Agreed. Summary of §7 fixes: one bridging sentence (Finding 4), relabeling as conjecture with honest scope statement (Finding 5), one new open question in §8 (empirical test).

### Round 3 Analysis

**Emerging consensus:** Both §7 fixes are agreed. Clean edits.
**Status:** All five findings addressed.

---

## Final Consensus

The committee unanimously recommends the following edits:

### §5 (both documents):
1. "lax monoidal" → "oplax monoidal"
2. "may exceed the min of the collapses" → "may fall strictly below the min of the collapses"
3. "It is *lax*" → "It is *oplax*"

### §6 (v2 only):
4. Replace lines 606-626 (the coend-expectation passage) with the three-statement structure:
   - Statement A: coend as join in V_5, acknowledgment that it's trivial for decreasing presheaves
   - Statement B: probabilistic expectation as a separate construction
   - Statement C: honest bridge (delta-function coincidence, universal property as structural guarantee, semiring-enrichment as future unification path). Cite Kelly 3.10, Definition 3.69.
5. Add to §8 (open questions): soft routing dinaturality question

### §7 (v2 only):
6. Add bridging sentence after canonical topology description (link categorical and semantic characterisations via §2's refinement definition)
7. Relabel mechanism design connection as "Conjecture (sheaf-equilibrium connection)" with explicit scope statement
8. Add to §8 (open questions): empirical test of sheaf-equilibrium conjecture

### Review file (not document):
9. Add verification status notes for §5 claims not covered by the spot-check

---

## KEY TENSIONS IDENTIFIED

1. **Scope of §5 audit** (resolved): Maya wanted broader audit; committee agreed to note verification status in review file, not in document
2. **Coend section strategy** (resolved): universal property reframing via three-statement structure, not a full restructure
3. **Development vs. correction** (resolved): new content (soft routing dinaturality, sheaf-equilibrium test) goes to §8 as open questions, not embedded in existing sections

## ASSUMPTIONS SURFACED

1. The refinement order on T faithfully represents inhabitation containment — used in the canonical topology bridge (Finding 4 fix)
2. The universal property interpretation of the coend is more professionally defensible than the computational interpretation — used in the coend reframe
3. A semiring enrichment base would be needed to unify the coend and expectation — stated as future work, not verified

## EVIDENCE REQUIREMENTS

1. Kelly 3.10, Definition 3.69 must be verified as the correct citation for the coend's universal property (Vic's correction of the initial 3.73 proposal)
2. The oplax direction must be re-verified after the edit to ensure no sign errors in the new text

## DECISION SPACE MAP

**If we apply all 9 edits:** The documents become honest about what's proven vs. conjectured in §§6-7, the §5 error is fixed, and the coend section makes a defensible (if more modest) claim. Professional reviewers will see careful formalism.

**If we apply only the mechanical fixes (1-3, 6-7):** The documents are terminologically correct but §6 still contains the equivocation. A professional reviewer will catch it.

**If we restructure §6 more aggressively (beyond the three-statement patch):** Better document, but higher risk of introducing new errors. Not recommended without a second mathematical review.

## RECOMMENDED NEXT STEPS

1. Apply all 9 edits
2. Run independent review on this deliberation
3. Run fresh mathematical review on the edited §§5-7
4. If clean, commit; if not, iterate once more
