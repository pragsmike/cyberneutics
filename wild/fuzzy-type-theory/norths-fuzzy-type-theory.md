# Fuzzy Type Theory (North et al.): Reference Summary

**Purpose:** Standalone summary of the enriched-type-theory program developed by North and collaborators, for cross-reference from cyberneutics documents. Not a cyberneutics document itself — see [north-cyberneutics-comparison.md](north-cyberneutics-comparison.md) for the comparative analysis.

**Primary source:** North, "(Towards a) Fuzzy type theory," Topos Institute colloquium, 2023-02-02. Slides: https://topos.institute/events/topos-colloquium/slides/2023-02-02.pdf

---

## 1. Motivation and setting

North's project builds a type theory for **opinions** — propositions that hold to intermediate degrees and may have multiple distinct reasons or pieces of evidence. The program is collaborative: key contributions come from Arya, Coraglia, O'Connor, Riess, and Tenório alongside North, particularly in the ACT 2022 Adjoint School project and Coraglia's thesis (Ch. 4). This summary follows North's 2023 colloquium presentation as the most accessible single source but the underlying work is collective. The categorical program:

- Replace posets (Boolean-enriched categories) with fuzzy posets: categories enriched in an ordered monoid such as [0,1] with multiplication.
- Keep proof relevance: hom-objects should carry many arrows (reasons), not just a truth value.
- Extend the Curry–Howard–Lambek correspondence from ordinary to enriched categories: from cartesian closed categories to their enriched analogues.

The construction works over a fixed ordered commutative monoid M (typically [0,1] with multiplication, but any fuzzy t-norm structure), building logical connectives and type-theoretic structure in terms of M-enriched and Set^M-enriched categories.

## 2. Fuzzy propositional logic via enrichment

### 2.1 Boolean and fuzzy enrichment

Ordinary propositional logic is modelled by a complete lattice, equivalently a category enriched in the Boolean poset **2** = {0 ≤ 1}. A hom-value hom(p, q) = 1 reads as "p entails q."

For opinions, replace **2** by an ordered monoid M. With M = [0,1]:

- An M-enriched category has objects (propositions) and for each pair x, y a hom-value hom(x, y) ∈ M giving the degree to which x entails y.
- Identities have value 1 (full self-entailment).
- Composition satisfies hom(x, y) ⊗ hom(y, z) ≤ hom(x, z) — fuzzy transitivity.

A fuzzy poset is exactly an M-enriched category with at most one underlying arrow per hom, but with a graded entailment value in M.

### 2.2 Weighted limits: conjunction and disjunction

Ordinary conjunction and disjunction are (co)limits. In the enriched setting, **weighted limits and colimits** are the right generalization.

A weighted product of objects A, B with weights α, β ∈ M behaves like a fuzzy conjunction of "A to degree α" and "B to degree β." (More precisely, a weighted limit is defined for a weight functor W : J^op → V — see Kelly, Ch. 3.1. The scalar-weight description here is the special case where J is discrete and W assigns a single value from M to each object, a pedagogical simplification of the general construction.) One can prove fuzzy modus ponens: from a fuzzy implication and a fuzzy premise weighted by α, derive a conclusion whose degree is bounded below by α.

Presheaf constructions appear naturally: functors from a discrete set of basic statements into M yield a completion under weighted colimits, whose elements are large fuzzy conjunctions ⋀_s μ(s) · s.

## 3. From fuzzy logic to fuzzy types

### 3.1 Proof relevance and Set^M enrichment

To capture multiple distinct reasons supporting an opinion, move from M-enriched to **Set^M-enriched** categories.

The category of fuzzy sets Set^M has:

- Objects: pairs (X, μ) where X is a set and μ : X → M assigns a degree to each element.
- Morphisms: functions f : X → Y with μ_X(x) ≤ μ_Y(f(x)) (non-decreasing in certainty).
- Monoidal structure: (X, μ) ⊗ (Y, ν) on X × Y with valuation (x, y) ↦ μ(x) ⊗ ν(y).

A category C enriched in Set^M then has:

- For each X, Y, a fuzzy set of morphisms hom(X, Y): a set of arrows, each with a degree in M.
- Distinguished identity arrows of degree 1.
- Composition that is set-theoretic on underlying arrows, with degrees satisfying |g ∘ f| ≥ |f| ⊗ |g|.

This is the semantic home for a fuzzy simply-typed lambda calculus: types are objects of a cartesian closed Set^M-enriched category, terms are arrows with degrees, products and exponentials correspond to fuzzy conjunction and implication.

### 3.2 From simply-typed to dependent types

Dependent type theory requires modelling families of types depending on terms, typically via display map categories or comprehension categories.

A crisp display map category consists of a category C with terminal object and a chosen class D of morphisms (display maps) closed under pullback, including all maps into the terminal object. Objects interpret contexts, arrows interpret substitutions, display maps interpret dependent types.

North's **fuzzy display map category** in the Set^M-enriched setting:

- Underlying category: a Set^M-enriched category whose hom-objects are fuzzy sets of terms.
- Distinguished class D of arrows (display maps) with degree exactly 1 — "pure" type dependencies with no fuzziness.
- Stability of D under weighted pullbacks, reflecting substitution in the presence of degrees.

This yields a fuzzy dependent type theory with judgements of the form:

    Γ ⊢ s : A [≥ α]

meaning "s is a term of type A in context Γ with degree at least α ∈ M." Structural rules (weakening, substitution) track degrees through the semantics. The central meta-theorem: every derivable judgement corresponds to a morphism in the enriched model whose degree meets the annotated bound.

At the time of the talk, the system included structural rules but not the full suite of type formers (Π, Σ, identity types). Extending to these formers and to fuzzy judgemental equality is ongoing work.

## 4. Enrichment by further metadata

The architecture generalizes to richer enrichment bases:

1. Replace the scalar monoid M by a commutative monoidal category of "evidence objects" — e.g., finite-dimensional ordered vector spaces with a suitable tensor.
2. Form an analogue of Set^M where each hom carries structured data (a vector of scores for different evidence kinds, or a tuple of confidence/recency/source).
3. Require composition to combine these data monoidally, generalizing |g ∘ f| ≥ |f| ⊗ |g| to a suitable order on the metadata space.

This is formally "changing the enriching base" the same way the move from **2** to [0,1] to arbitrary ordered monoids works. The constraints: the base must support weighted limits and pullbacks, and must interact with the comprehension structure so substitution composes metadata in a controlled way.

## 5. Written sources

- Coraglia, G. *Categorical structures for deduction.* PhD thesis, Genova, 2023. Ch. 4: fuzzy dependent types (with Arya, O'Connor, Riess, Tenório, North). https://etagreta.github.io/docs/coraglia_phdthesis-oneside2023.pdf
- "A theory of fuzzy types," Logic Group talk slides, 2022. https://www.logicgroup.altervista.org/Slides/20221125Coraglia.pdf
- "Fuzzy Type Theory for Opinion Dynamics," ACT 2022 Adjoint School slides. https://msp.cis.strath.ac.uk/act2022/slides/adjointschool_group2.pdf
- North, "(Towards a) Fuzzy type theory," Topos colloquium slides, 2023. https://topos.institute/events/topos-colloquium/slides/2023-02-02.pdf
- North's research page: https://paigenorth.github.io
- Mulder, North, Péroux. "Measuring data types." arXiv:2405.14678, 2024.
