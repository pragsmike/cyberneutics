# Fuzzy Type Theory and Furry Logic

**Status:** Active research — sibling-relationship established, adoption items identified, expert review needed.

## Research question

Cyberneutics' soft type system and "furry logic" extension share categorical machinery (enriched categories over ordered monoids, presheaf constructions) with Paige North's fuzzy type theory program and the Mulder-North-Péroux "Measuring Data Types" paper. Are these the same construction applied differently, or genuinely distinct formalisms? What should cyberneutics adopt?

## Current answer

Furry logic and North's fuzzy type theory are **sibling constructions**, not specializations of each other. They share a common ancestor (Kelly-style enriched categories) but diverge at the application layer. North builds a structural type theory (judgement forms, dependent types, Curry-Howard-Lambek correspondence). Cyberneutics builds a pipeline composition framework with distributional type membership and self-referential closure. Neither subsumes the other.

The "Measuring Data Types" paper introduces a third angle: Sweedler measuring coalgebras as enrichment data, which provides a formal model for rubric scoring (degree of conformance as enrichment). This is the most actionable connection for cyberneutics.

## Files in this directory

- **[norths-fuzzy-type-theory.md](norths-fuzzy-type-theory.md)** — Reference summary of the North et al. program: M-enriched categories for opinions, Set^M enrichment for proof relevance, fuzzy display map categories for dependent types. Technical detail sufficient for cross-referencing. Source links included. Credits the full collaboration (Arya, Coraglia, O'Connor, Riess, Tenório, North).

- **[north-cyberneutics-comparison.md](north-cyberneutics-comparison.md)** — Comparative analysis and action plan. Shared ancestor, divergences in both directions, measuring coalgebra–rubric parallel, magnitude connections, adoption triage (adopt now / investigate / defer).

## Related files elsewhere

- [wild/diary/2026-03-13-furry-logic.md](../diary/2026-03-13-furry-logic.md) — Genesis diary entry. Motivates furry logic from the problem of multi-type texts, DL historical arc, measurement framing, categorical constructions (coproduct, coend, pushout, pullback, tensor), routing consequences. Contains a tentative essay outline.
- [palgebra/soft-type-theory.md](../../palgebra/soft-type-theory.md) — The formalism that furry logic extends. Graded type profiles via presheaf evaluation.
- [palgebra/categorical-structures.md](../../palgebra/categorical-structures.md) — §2d (closure/self-reference) and §2e (morphisms as texts) are the cyberneutics-side constructions that North's system lacks.
- [wild/diary/2026-03-22-bradley-magnitude-tropical.md](../diary/2026-03-22-bradley-magnitude-tropical.md) — Bradley magnitude session that prompted the investigation.

## Adoption triage (from comparison report §6)

**Adopt now:** Acknowledge North et al. as prior art in soft-type-theory.md. Record measuring-coalgebra–rubric parallel as research note. Produce a Set^M enrichment design exploration — a worked example comparing Set^M-enriched hom-objects to scalar enrichment for one concrete pipeline morphism.

**Investigate:** Whether a natural endofunctor F exists for (template, rubric) pairs, or whether soft types require a different categorical framework (sketches, essentially algebraic theories, Lawvere theories). Magnitude of measuring-enriched categories.

**Defer:** North's dependent type theory (revisit trigger: branching pipelines where output type depends on input value). Formal proof that enrichment ≅ presheaf in closed categories (requires expert verification).

## Notation

| Symbol | Meaning | Used in |
|--------|---------|---------|
| V | Three-element lattice {Low, Medium, High} with min as tensor | soft-type-theory.md, categorical-structures.md |
| V₅ | Product quantale [0,3]⁵ with componentwise min | soft-type-theory.md §5, worked example (§5d) |
| M | Arbitrary ordered commutative monoid (North's general enrichment base) | norths-fuzzy-type-theory.md |
| [0,1] | Unit interval with multiplication (North's primary example) | norths-fuzzy-type-theory.md, comparison §1 |
| Set^M | Category of fuzzy sets over M (proof-relevant enrichment) | norths-fuzzy-type-theory.md §3, comparison §§1–2 |
| T | Category of soft types (objects = (template, rubric) pairs) | soft-type-theory.md §2, worked example (§5d) |

## Epistemic status

All analysis here is LLM-generated and provisionally useful but untrusted. The shared-ancestor observation is secure. The measuring-coalgebra–rubric parallel is structurally plausible but needs expert review. The magnitude speculation is the most tentative part.
