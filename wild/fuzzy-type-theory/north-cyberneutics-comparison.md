# North's Fuzzy Type Theory, Measuring Data Types, and Cyberneutics

**Date:** 2026-03-22
**Context:** Comparison of three related programs — North et al.'s fuzzy type
theory, the Mulder-North-Péroux "Measuring Data Types" paper
(arXiv:2405.14678), and the cyberneutics soft type / furry logic system.
Prompted by the question: is furry logic a variant of North's work, and does
the measuring framework connect to Bradley's magnitude and rubric scoring?

**Prerequisite:** For North's technical machinery (M-enrichment, Set^M
enrichment, fuzzy display maps, dependent types), see
[norths-fuzzy-type-theory.md](norths-fuzzy-type-theory.md). For the
motivation behind furry logic (multi-type texts, DL historical arc,
measurement framing, categorical constructions), see
[wild/diary/2026-03-13-furry-logic.md](../diary/2026-03-13-furry-logic.md).

---

## 1. The shared ancestor: enriched categories over ordered monoids

All three programs begin from the same categorical root: replace Boolean
type membership with enriched membership over an ordered monoid M.

North uses M = [0,1] with multiplication; hom-values are degrees of
entailment. Cyberneutics uses V = ({Low, Medium, High}, min, High);
hom-values are confidence levels. Both are commutative quantales, both are
valid enrichment bases in the sense of Kelly (1982, Ch. 1.2), and both
produce presheaf constructions as the natural object for graded type
assignment. The formal machinery is the same; the application domains
diverge.

---

## 2. Where North's program goes that cyberneutics doesn't

North builds a structural type theory: judgement forms with degree
annotations (Γ ⊢ s : A [≥ α]), structural rules tracking degree
propagation, proof relevance via Set^M enrichment (multiple arrows per hom,
each with its own degree), and dependent types via fuzzy display map
categories. See [norths-fuzzy-type-theory.md §§2–3](norths-fuzzy-type-theory.md)
for full exposition.

Cyberneutics has none of this. The soft type system assigns graded type
profiles via presheaf evaluation but has no judgement forms, structural
rules, or dependent types. It does not need them for pipeline composition —
the three-layer architecture (categorical-structures.md §2a–§2c) handles
composition without a proof theory. But the structural rules would be
useful for reasoning about type-level guarantees across pipeline stages
(e.g., "if all inputs have confidence ≥ Medium, the output has confidence
≥ Medium" as a formally derivable statement rather than an empirical
observation).

---

## 3. Where cyberneutics goes that North doesn't

### 3a. Distributional type membership (furry logic)

North's system grades membership in individual types: artifact a inhabits
type A to degree α. Cyberneutics' furry logic extension (soft-type-theory.md
§4, diary 2026-03-13) replaces this with a *measure on type-space*:

    μ_a ∈ Prob(T)

where T is the type category. Single-type artifacts are delta functions.
Fuzzy membership is a smeared delta. Texts that genuinely span two types
are bimodal distributions.

This distributional move connects to Fritz's Markov category framework:
the type assignment τ : Artifacts → Prob(T) is a Markov kernel, and
pipeline composition acts on type assignments via Chapman-Kolmogorov.
North's system stays at graded inhabitation of individual types and does
not make this distributional step.

The furry logic insight — that type membership is a *measure* rather than
a *grade* — is the key divergence. It means cyberneutics treats multi-type
texts as first-class objects rather than artifacts that happen to score
nonzero on multiple rubrics independently.

### 3b. Closure and self-reference

Because Text is a closed category — its hom-objects are themselves texts
(prompts, scripts, calibration records) — the presheaf construction applies
reflexively to hom-objects. The Kelly enrichment value Hom(A, B) = Medium
is a summary statistic derived from the presheaf evaluation of the
calibration record living at Hom(A, B). The enrichment layer and the
presheaf layer are one story at different resolutions.

North works with general enriched type theories, not with a specific closed
category where specifications are objects. Her system does not have this
self-referential property. It is both a structural limitation (less self-
applicable) and a feature (more general, applies to any ordered monoid).

### 3c. Pipeline composition and operational semantics

Cyberneutics has a worked-out pipeline composition framework: resource
equations, string diagrams, fan/funnel duality, the decision monad,
bounded feedback traces, human gates as collapse operators. North's system
has no pipeline story — it is a type theory, not a workflow formalism.

---

## 4. Furry logic is not a specialization of North

Furry logic and North's fuzzy type theory are *sibling constructions*
sharing the same categorical parent (enriched categories over ordered
monoids) but diverging at the application layer:

| Dimension | North | Cyberneutics |
|-----------|-------|--------------|
| Goal | Type theory (Curry-Howard-Lambek) | Pipeline composition and audit |
| Enrichment base | [0,1] with multiplication | V = {Low, Medium, High} with min |
| Type membership | Graded single-type (presheaf) | Distributional multi-type (measure on T) |
| Proof relevance | Set^M enrichment (multiple arrows per hom) | Not present (single scalar per hom) |
| Dependent types | Fuzzy display maps | Not needed |
| Self-reference | Not present | Closed category; presheaf on hom-objects |
| Pipeline operations | Not present | Full resource algebra |

Both could benefit from each other. North's structural rules could
discipline the furry logic (formal guarantees about degree propagation
through pipeline stages). Cyberneutics' distributional extension and
closure insight could enrich North's system.

---

## 5. Measuring Data Types: the deeper connection

Mulder, North, and Péroux (arXiv:2405.14678, 2024) combine Sweedler's
measuring coalgebras with W-types to show that *algebras of an endofunctor
are enriched in coalgebras of the same endofunctor*. The key ideas:

**Measuring as partial homomorphism.** For two k-algebras A and B, the
universal measuring coalgebra P(A, B) encodes all *partial* homomorphisms
A → B, each annotated with a degree of "how close" it is to being a
genuine homomorphism. The hom-coalgebras give higher-precision tools for
studying algebras than the ordinary category of total homomorphisms.

**Enrichment captures closeness.** The enrichment of algebras in coalgebras
is the formal structure: the hom-objects are coalgebras (not sets), and
they carry information about degree of conformance. This is not Boolean
(is/isn't a homomorphism) but graded (how close to being one).

**Generalized W-types.** Initial algebras (W-types, the semantics of
inductive data types) are generalized by parameterizing them with a
coalgebra C. A C-inductive data type is "the smallest algebra satisfying
the recursion *as measured by C*." Different measuring instruments give
different notions of initiality.

### 5a. Connection to rubric scoring

The structural parallel to cyberneutics is immediate:

| Measuring Data Types | Cyberneutics |
|---------------------|--------------|
| How close is this map to a genuine homomorphism? | How well does this artifact inhabit this type? |
| Measuring coalgebra P(A, B) as hom-object | Presheaf evaluation F_a(A) = rubric_A(a) |
| Enrichment of algebras in coalgebras | Enrichment of pipeline artifacts in type profiles |
| Multiple partial homomorphisms with degrees | Multiple rubric evaluations with scores |
| Coalgebra tracks degree of conformance | Rubric tracks degree of inhabitation |

Both are "degree of conformance" measurements formalized as enrichment
data. The measuring coalgebra says "here are all the ways this map
*almost* respects the algebra structure, and here is how close each way
gets." The rubric evaluation says "here are all the criteria for this
type, and here is how well the artifact satisfies each."

North's Set^M enrichment is the bridge. In the fuzzy type theory, hom-
objects carry *sets of arrows each with a degree* — multiple distinct
proofs, each with a strength grade. In the measuring paper, hom-objects
carry *coalgebras of partial homomorphisms* — multiple partial maps, each
with a closeness grade. Both replace scalar hom-values with structured
hom-objects that track multiple measurements simultaneously.

Cyberneutics currently collapses this structure. Multiple rubric runs on
the same artifact are treated as variance data (repeated measurements
producing a distribution of scores). The North/Sweedler framework suggests
an alternative: treat them as multiple arrows in a structured hom-object,
each carrying its own grade. This would preserve more information than the
variance summary.

### 5b. Connection to Bradley's magnitude

Bradley-Vigneaux compute magnitude for the [0,1]-enriched category of
texts. Magnitude is a numerical invariant summarizing "effective size"
— how many independent objects, weighted by distinguishability.

The measuring enrichment of North-Mulder-Péroux is a different enrichment
of a different category (algebras of endofunctors, not texts over [0,1]),
but both share the structural pattern: enrichment that measures "how
different are these objects?" If magnitude could be computed for the
measuring-enriched category of data types, it would yield an invariant
measuring "how many effectively independent data types exist, weighted by
the distinguishability of their partial homomorphisms."

The pipeline application: if you modeled the committee pipeline as a
measuring-enriched category — objects are pipeline stages, hom-objects are
coalgebras of partial transformations weighted by conformance degree —
then magnitude would be an aggregate measure of pipeline complexity. The
calibration register could track this scalar across runs.

Whether this is a genuine mathematical connection or a superficial analogy
requires expert review. The enrichment bases differ (coalgebras vs.
ordered monoids vs. [0,1]), and it is not obvious that magnitude
generalizes cleanly across all these settings. Leinster's magnitude is
defined for enriched categories over [0,∞]; extending it to coalgebra-
enriched categories would require new mathematics.

### 5c. C-inductive data types as rubric-relative types

The generalized W-types in the measuring paper — C-inductive data types,
parameterized by a coalgebra C — have a structural echo in cyberneutics.
A soft type is a (template, rubric) pair: the rubric is the measuring
instrument, and changing the rubric changes the type. Different rubrics
give different type profiles for the same artifact.

In the measuring framework, different coalgebras C give different notions
of initiality for the same endofunctor. The coalgebra plays the same role
as the rubric: it defines what counts as a good instance.

This suggests that the cyberneutics soft type (template, rubric) could be
formalized as a C-algebra where C is a measuring coalgebra derived from
the rubric. The template defines the endofunctor (the recursive structure
of the type); the rubric defines the measuring coalgebra (the standard
against which conformance is assessed). This would give the soft type
system a foundation in the same categorical framework as North's type
theory.

---

## 6. What to adopt, what to defer

### Adopt now (light integration)

- **Terminology**: acknowledge North's fuzzy type theory as prior art in
  the soft-type-theory.md document. The enriched-category-over-ordered-
  monoid construction is the same; the divergence is in application.

- **Measuring coalgebra as rubric model**: record the structural parallel
  (§5a above) as a research note. This is a potential formalization of
  what rubric scoring does, worth developing if the ACT outreach produces
  collaborators interested in the formal foundations.

### Investigate (medium-term)

- **Set^M enrichment for proof-relevant type profiles**: could cyberneutics
  benefit from tracking multiple distinct evaluations as structured hom-
  object data rather than variance samples? Worth a worked example.

- **C-inductive data types as rubric-relative types** (§5c): formalize
  (template, rubric) as C-algebra where C is a measuring coalgebra. This
  would unify the soft type system with the measuring framework.

- **Magnitude of measuring-enriched categories**: determine whether
  Leinster magnitude extends to coalgebra-enriched categories, and if so
  whether it connects to Bradley-Vigneaux magnitude through change-of-base.

### Defer (requires expert review)

- **North's dependent type theory**: display maps, structural rules, Π/Σ
  formers. Cyberneutics does not currently need dependent types. If the
  methodology scales to nested pipelines (pipelines that generate
  pipelines), dependent types might become relevant — the type of the
  output depends on the value of the input. But this is speculative.

- **Formal proof that enrichment ≅ presheaf in closed categories**: the
  §2d closure insight (categorical-structures.md) states that Kelly
  enrichment values are derived from presheaf evaluation of hom-objects.
  Making this an isomorphism (rather than a derivation with coarsening)
  would require working in the full V₅-enriched setting rather than the
  three-element coarsening. This is a mathematical claim that needs
  verification.

---

## 7. Epistemic status

This analysis is LLM-generated and provisionally useful but untrusted. The
structural parallels described are real at the level of shared categorical
machinery (enriched categories, presheaves, quantales). Whether they
constitute genuine mathematical connections — isomorphisms, adjunctions,
or natural transformations between the three programs — or are superficial
analogies that break under scrutiny requires expert review. The measuring
coalgebra connection (§5) is the most speculative part; the shared-
ancestor observation (§1) is the most secure.

---

## References

- North, P.R. "(Towards a) Fuzzy type theory." Topos Institute colloquium,
  2023-02-02. Slides: https://topos.institute/events/topos-colloquium/slides/2023-02-02.pdf
- Coraglia, G. *Categorical structures for deduction.* PhD thesis, Genova,
  2023. Ch. 4 (fuzzy dependent types). PDF: https://etagreta.github.io/docs/coraglia_phdthesis-oneside2023.pdf
- Mulder, L., North, P.R., and Péroux, M. "Measuring data types."
  arXiv:2405.14678, 2024.
- Mulder, L., North, P.R., and Péroux, M. "Functoriality of Enriched Data
  Types." arXiv:2505.06059, 2025.
- Mulder, L., North, P.R., and Péroux, M. "Coinductive control of
  inductive data types." CALCO 2023. arXiv:2303.16793.
- Bradley, T.-D. and Vigneaux, J.P. "The Magnitude of Categories of Texts
  Enriched by Language Models." TAC 44(37), 2025. arXiv:2501.06662.
- Kelly, G.M. *Basic Concepts of Enriched Category Theory.* Cambridge, 1982.
- Fritz, T. "A synthetic approach to Markov kernels." *Advances in
  Mathematics* 370, 2020. arXiv:1908.07021.
- Leinster, T. "The magnitude of metric spaces." *Documenta Mathematica*
  18, 2013.
- Atkey, R. "Syntax and Semantics of Quantitative Type Theory." LICS 2018.
