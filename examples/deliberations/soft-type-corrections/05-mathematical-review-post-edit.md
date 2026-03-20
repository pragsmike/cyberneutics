# Fresh Mathematical Review: soft-type-theory-v2.md §§5-7 (post-correction)

**Date:** 2026-03-19
**Scope:** Verify all edits from the corrections committee deliberation. Check for new errors introduced by the edits. Re-evaluate original claims in light of the rewritten text.

---

## §5 Collapse Functor: Oplax Fix

### Verification of the edit

The text now reads: "This is an oplax monoidal functor... the collapse of a componentwise min may fall strictly below the min of the collapses."

**Check:** collapse(a ⊗ b) = collapse(cmin(a,b)). Since sum(cmin(a,b)) = sum(min(a₁,b₁),...,min(a₅,b₅)) ≤ sum(a₁,...,a₅) = sum(a), and collapse is monotone in the sum, we get collapse(cmin(a,b)) ≤ collapse(a). Similarly ≤ collapse(b). Therefore collapse(a ⊗ b) ≤ collapse(a) ⊗ collapse(b). This is the **oplax** direction. ✓

The concrete example (two Medium vectors whose cmin is Low) demonstrates the strict inequality. ✓

The phrase "oplaxness is a genuine feature" — the surrounding discussion about boundary-coarsening is phrased in terms of information loss, which is compatible with both lax and oplax. The switch to "oplaxness" doesn't affect the argument. ✓

The "each oplax monoidal with different oplaxness properties" in the decorated texts connection — this is correct in principle (different collapse functors will have different oplaxness characteristics). ✓

**Verdict: §5 fix is clean. No new errors.**

---

## §6 Coend Section: Three-Statement Rewrite

### Statement A (coend as join, lines 596-614)

**Claim:** "the coend reduces to the colimit of F_a over T... In V_5 (a complete lattice), the colimit is the join — the componentwise supremum of all F_a(C) values."

**Check:** In a complete lattice viewed as a thin category, colimits are joins. The coend of the representable-tensored bifunctor, after simplification, is the colimit of the presheaf. The colimit of a functor into a complete lattice is the join of the images. ✓

**Claim:** "For a presheaf satisfying the functoriality condition (grades decrease along refinement), the supremum is achieved at the least refined (most general) type."

**Check:** Functoriality says F(A) ≥ F(B) when B refines A (B is lower in the preorder, A is higher/more general). So F(A) ≥ F(B) for all B below A. The supremum over all C of F(C) is achieved at the most general type (highest in the preorder). ✓

**Claim:** "This is mathematically correct but computationally trivial."

**Assessment:** Honest and accurate. ✓

**Claim (universal property):** "By Kelly (Ch. 3.10, Definition 3.69), the coend is characterised by the property that any family of V_5-morphisms H(C, C) → X that is dinatural in C factors uniquely through the coend."

**Check:** Kelly 3.10 treats ends and coends. Definition 3.69 defines the coend as the colimit of the functor H when restricted to the diagonal, characterised by the universal property of receiving all dinatural transformations from H. The statement in the text is a correct paraphrase of this definition. ✓

**Minor issue:** The text says "any family of V_5-morphisms H(C, C) → X that is dinatural in C." More precisely, the coend's universal property is: for any V-object X equipped with a dinatural transformation from H to the constant X, there exists a unique V-morphism from the coend to X. The text's phrasing conflates "family of morphisms" with "dinatural transformation" — these are the same thing (a dinatural transformation *is* a family satisfying the dinaturality hexagon), but a reader unfamiliar with enriched category theory might not parse it correctly. This is an expository issue, not a mathematical error.

### Statement B (expectation as separate construction, lines 628-640)

**Claim:** "The expected score profile is E_{μ_a}[F_a] = ∫_T μ_a(dC) · F_a(C)."

**Check:** Standard definition of expectation of a V_5-valued function under a probability measure. ✓

**Claim:** "This is a weighted average over the score profiles, using addition and multiplication in ℝ^5."

**Check:** Correct. The expectation operates in (ℝ^5, +, ·), not in (V_5, min). ✓

**Claim:** "They coincide only when the type distribution is a delta function."

**Check:** For μ_a = δ_t, E[F_a] = F_a(t) and the coend = ∨_C F(C). These coincide only if t is the most general type (where F_a achieves its supremum). For a delta at a more refined type, E[F_a] = F_a(t) ≤ F_a(top) = coend.

**Issue found.** The claim "they coincide only when the type distribution is a delta function" is **not quite right**. They coincide when μ_a = δ_top (delta at the most general type). For μ_a = δ_t where t is not the top, E[F_a] = F_a(t) which may be strictly less than the coend = F_a(top). The text says "both return F_a at the assigned type" — for the coend, this is only true if the assigned type is the top. For the expectation, it returns F_a(t) regardless.

**Severity: Low.** The broader point (coend and expectation are different operations) is correct. The specific claim about delta-function coincidence needs a parenthetical: "in which case the expectation returns F_a(t) at the assigned type; this equals the coend when t is the most general type."

### Statement C (honest bridge, lines 642-648)

**Claim:** "A future treatment might unify them by working in a semiring-enriched setting."

**Assessment:** This is honest about the gap and correctly identifies what would be needed. The suggestion is plausible: if V is a semiring (with addition instead of join), the coend computes a weighted colimit that looks like a sum. However, the text doesn't claim this is straightforward or that it would preserve other properties. ✓

### Connection to routing (lines 650-658)

**Claim:** "any soft router satisfying the dinaturality condition factors canonically through the coend (see §8, open questions)."

**Check:** This is a correct application of the coend's universal property: if the router's assignment to each type forms a dinatural transformation from H to the routing space, it factors through the coend. The §8 open question correctly notes this holds for linear routers (by presheaf functoriality) and is an additional constraint for nonlinear ones. ✓

### "What the coend does not resolve" subsection (lines 669-687)

No changes were made to this subsection. The claims about cocompleteness and coequaliser existence remain correct per the original review. ✓

---

## §7 Sheaf Section

### Canonical topology bridge (lines 715-719)

**Added text:** "This semantic characterisation is equivalent to the categorical one... because the refinement order on T is defined in terms of inhabitation containment: B refines A precisely when every B-artifact is an A-artifact, per §2."

**Check:** §2 defines refinement: "A morphism τ : A → B in T exists when type B refines type A — every artifact that inhabits B also inhabits A." So B refines A means inhabitation(B) ⊆ inhabitation(A). The covering condition "every A-artifact inhabits some Bᵢ" means inhabitation(A) ⊆ ∪ inhabitation(Bᵢ), which combined with the refinement containment means the Bᵢ jointly cover A in the inhabitation-containment sense. This is the semantic content of the categorical covering sieve condition. ✓

**Minor precision issue:** The canonical topology on a preorder is technically the topology where a sieve S on A is covering iff S is "jointly epimorphic" — in a preorder, this means the upward closure of S contains A (or equivalently, A is in the sieve). For the specific claim that {B₁,...,Bₙ} covers A, we need A ≤ ∨Bᵢ in the lattice order. The bridge sentence's argument works if T is a lattice (not just a preorder), which it is described as being ("type lattice"). ✓

### Mechanism design conjecture (lines 800-810)

**Label:** "Conjecture (sheaf-equilibrium connection)."

**Content:** Changed "ill-defined" to "ambiguous" and "facing a multi-objective optimisation problem." Added: "Deriving this rigorously would require showing that the composed open game with inconsistent payoffs fails to have a Nash equilibrium or that its equilibria are Pareto-dominated, which we have not attempted."

**Assessment:** The relabeling as conjecture is appropriate. The characterisation of what a rigorous derivation would require is correct — these are standard criteria for mechanism design failure. The word "ambiguous" is more accurate than "ill-defined." ✓

### New open questions in §8 (lines 895-913)

**Soft routing and dinaturality:** The claim that "for a linear router (weights are the presheaf values), dinaturality follows from presheaf functoriality" — this needs checking. A linear router assigns weight F_a(C) to the branch for type C. The dinaturality condition requires: for any morphism f : C → D in T, the routing through C composed with f equals the routing through D. For a linear router, this means F_a(C) composed with the refinement C → D gives the same result as F_a(D). By presheaf functoriality, F_a(C) ≥ F_a(D), and the refinement acts by the enriched hom. The exact dinaturality hexagon would need to be checked against the specific bifunctor, but the directional claim is plausible. **No error, but the claim is marked as an open question, which is appropriate.**

**Sheaf-equilibrium empirical test:** Well-formulated. The prediction is testable and specific. ✓

---

## Summary of fresh review findings

### Original errors — all corrected:
1. ✓ §5 oplax: correctly fixed, no new errors
2. ✓ §6 coend ≈ expectation: equivocation removed, replaced with honest three-statement structure
3. ✓ §6 vacuity: acknowledged explicitly, value redirected to universal property
4. ✓ §7 canonical topology: bridge sentence added, mathematically sound
5. ✓ §7 mechanism design: relabeled as conjecture with explicit scope

### New issues found:

**Issue A (Low severity):** §6 Statement B claims coend and expectation "coincide only when the type distribution is a delta function." More precisely, they coincide when the delta is at the most general type. For a delta at a refined type, E[F_a] = F_a(t) ≤ F_a(top) = coend. The claim should be: "For a delta measure μ_a = δ_t, the expectation returns F_a(t); this equals the coend (which is always F_a at the most general type) only when t is the most general type."

**Issue B (Expository, not mathematical):** The universal property description conflates "family of V_5-morphisms" with "dinatural transformation." These are technically the same thing but may confuse readers unfamiliar with enriched category theory.

### Overall assessment

The edits are well-executed. The three original errors are corrected, the two clarifications are added, and no significant new mathematical errors are introduced. Issue A is a minor imprecision in the delta-function coincidence claim (low severity, easy fix). Issue B is expository, not mathematical.

**The document is substantially improved for professional review.** The boundary between proven and conjectured claims is now explicit. The coend section is honest about its limitations while preserving its structural contribution (universal property). The sheaf section is properly labeled.

**Recommendation:** Fix Issue A (one sentence edit) and optionally improve Issue B. Then the edited sections are ready for professional review.
