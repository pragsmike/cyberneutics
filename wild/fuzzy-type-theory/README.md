# Fuzzy Type Theory and Furry Logic

**Status:** Active research — sibling-relationship established, adoption items identified, expert review needed.

## Research question

Cyberneutics' soft type system and "furry logic" extension share categorical machinery (enriched categories over ordered monoids, presheaf constructions) with Paige North's fuzzy type theory program and the Mulder-North-Péroux "Measuring Data Types" paper. Are these the same construction applied differently, or genuinely distinct formalisms? What should cyberneutics adopt?

## Current answer

Furry logic and North's fuzzy type theory are **sibling constructions**, not specializations of each other. They share a common ancestor (Kelly-style enriched categories) but diverge at the application layer. North builds a structural type theory (judgement forms, dependent types, Curry-Howard-Lambek correspondence). Cyberneutics builds a pipeline composition framework with distributional type membership and self-referential closure. Neither subsumes the other.

The "Measuring Data Types" paper introduces a third angle: Sweedler measuring coalgebras as enrichment data, which provides a formal model for rubric scoring (degree of conformance as enrichment). This is the most actionable connection for cyberneutics.

## Files in this directory

- **[norths-fuzzy-type-theory.md](norths-fuzzy-type-theory.md)** — Reference summary of North's program: M-enriched categories for opinions, Set^M enrichment for proof relevance, fuzzy display map categories for dependent types. Technical detail sufficient for cross-referencing. Source links included.

- **[north-cyberneutics-comparison.md](north-cyberneutics-comparison.md)** — Comparative analysis and action plan. Shared ancestor, divergences in both directions, measuring coalgebra–rubric parallel, magnitude connections, adoption triage (adopt now / investigate / defer).

## Related files elsewhere

- [wild/diary/2026-03-13-furry-logic.md](../diary/2026-03-13-furry-logic.md) — Genesis diary entry. Motivates furry logic from the problem of multi-type texts, DL historical arc, measurement framing, categorical constructions (coproduct, coend, pushout, pullback, tensor), routing consequences. Contains a tentative essay outline.
- [palgebra/soft-type-theory.md](../../palgebra/soft-type-theory.md) — The formalism that furry logic extends. Graded type profiles via presheaf evaluation.
- [palgebra/categorical-structures.md](../../palgebra/categorical-structures.md) — §2d (closure/self-reference) and §2e (morphisms as texts) are the cyberneutics-side constructions that North's system lacks.
- [wild/diary/2026-03-22-bradley-magnitude-tropical.md](../diary/2026-03-22-bradley-magnitude-tropical.md) — Bradley magnitude session that prompted the investigation.

## Adoption triage (from comparison report §6)

**Adopt now:** Acknowledge North as prior art in soft-type-theory.md. Record measuring-coalgebra–rubric parallel as research note.

**Investigate:** Set^M enrichment for proof-relevant type profiles (multiple evaluations as structured hom-object data). C-inductive data types as rubric-relative types ((template, rubric) as C-algebra). Magnitude of measuring-enriched categories.

**Defer:** North's dependent type theory (not needed for current pipeline). Formal proof that enrichment ≅ presheaf in closed categories (requires expert verification).

## Epistemic status

All analysis here is LLM-generated and provisionally useful but untrusted. The shared-ancestor observation is secure. The measuring-coalgebra–rubric parallel is structurally plausible but needs expert review. The magnitude speculation is the most tentative part.
