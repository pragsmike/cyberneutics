# Categorical Structures in Cyberneutics

*A treatment of the basic category-theoretic constructions as they appear in
narrative computing pipelines, in pedagogical order.*

> **Epistemic status**: Provisionally useful but untrusted. These constructions organize thinking about pipeline composition but have not been reviewed by category theory experts. Lax/approximate coherence framing was added after a focused review (2026-03-13); overclaimed universal properties were weakened to design targets in that same review. Treat as working hypotheses. See the [LLM-mathematical-inquiry outline](../wild/llm-mathematical-inquiry-outline.md).

---

## 1. Preliminaries: Why Category Theory Here

Category theory is concerned with *structure-preserving maps* rather than with
the intrinsic nature of objects. This priority — arrows over objects, relations
over essences — is not merely a formal preference; it matches the situation of
narrative computing precisely. What matters about a scenario text is not what it
"is" but what transformations it admits: what it can be summarised into, what
committee positions it supports, what resolutions it licenses. The objects
(texts, transcripts, resolutions) are just the sources and targets of those
transformations.

Three foundational commitments follow from this:

**Isomorphism replaces equality.** We rarely ask whether two pipeline outputs
are the same document. We ask whether they are *equivalent for the purposes at
hand* — whether they support the same downstream reasoning. This is the
categorical notion of isomorphism: not identity, but structure-preserving
invertible map. Two committee resolutions can be isomorphic in their
recommendation structure while differing in wording. The palgebra works with
this weaker, more useful relation.

**Compositionality is primary.** The value of the categorical framework lies in
composition: pipeline stages can be assembled, decomposed, and re-assembled in
ways that preserve type-correctness. A morphism `f: A → B` and a morphism
`g: B → C` compose to `g ∘ f: A → C`. The output type of `f` must match the
input type of `g`. This is not a trivial constraint — it is what prevents
pipelines from drifting into type-confusion, passing a `transcript` where a
`charter` was expected.

**Stochastic does not mean incoherent.** Running the same pipeline twice on
the same inputs will not produce identical outputs. This looks like it should
break the categorical framework — if diagrams don't commute on the nose, what
good are they? The answer is that the morphisms in **Text** are not functions
but *Markov kernels*: stochastic maps that assign to each input a probability
distribution over outputs. Composition of Markov kernels is strictly
associative — the Chapman–Kolmogorov equation holds exactly, not approximately.
The stochasticity is *inside* each morphism; the composition is exact. Two
different sample runs give different texts, but the *distribution* over texts
is the same regardless of how you parenthesise the composition. Section 2a
makes this precise using Fritz's Markov category framework (Fritz 2020).

Two distinct concerns should not be conflated:

*Compositional coherence* — do the categorical axioms hold? Yes, by the Markov
category structure. Associativity, identity laws, and the comonoid equations
hold as equalities between Markov kernels. This is not approximate.

*Universal properties* — does the charter satisfy the universal property of a
product? Does the scenario-set satisfy the universal property of a coproduct?
Here the answer is genuinely approximate. The charter compresses its inputs;
the projections are lossy. The universal properties described in §§4–7 below
are *design targets* that a well-constructed pipeline approximates, not
theorems that the pipeline satisfies exactly. The Probe operation (§9) is the
empirical test of how close the approximation is. Section 4.1 below gives
"approximate" a precise metric: the *reconstruction error* measures how much
information the approximate projections lose, grounded in the rubric-based
similarity scores the pipeline already uses for quality assessment.

Section 2c below integrates these two concerns — exact compositional coherence
and approximate universal properties — into a three-layer architecture that
shows how the deterministic base, the Markov category, and the confidence
enrichment fit together as compatible layers of a single framework.

This situation is not a deficiency to be apologised for. It reflects a genuine
feature of the domain. Meaning in LLM-mediated text processing is a temporary
stabilisation in a coupled system, not a fixed object
([From Semantic Potential to Situated Sense](../wild/potential-to-sense/from_semantic_potential_to_situated_sense.md)).
Concepts are eigenforms of conversational processes — stable enough to function,
dependent on the ongoing dynamics that produce them. The categorical framework
captures the *structural* relationships between pipeline stages even when the
*content* those stages produce is stochastic. The structure is the part that
composes reliably; the content is the part that varies. Keeping both in view is
what the formalism is for.

### A note on universal properties

The constructions in this document — products, coproducts, equalizers,
pullbacks, pushouts — are all defined by *universal properties*. A universal
property says: this construction is the *best* object for a given purpose,
where "best" means most economical. Specifically, any other object that serves
the same purpose maps to (or from) this one in exactly one way. The product
A × B is the best way to package A and B together — anyone who needs both can
get them from A × B, and there's only one way to do so that respects both
projections. The coproduct A + B is the best way to combine A and B as
alternatives — anyone who can handle both cases can handle A + B, and there's
only one consistent way to do so.

Uniqueness is the key word. It is what distinguishes a genuine categorical
construction from an arbitrary aggregation. And it is precisely where the
stochastic pipeline softens the classical picture: the "unique" map becomes
"the map that the pipeline will produce with high probability across runs." The
Probe operation tests whether uniqueness holds empirically.

---

## 2. Objects and Morphisms

The category **Text** has the following structure:

- **Objects** are *soft types*: `(template, rubric)` pairs that define what a
  well-formed artifact of a given kind looks like. The template is structural
  (required sections, metadata fields); the rubric is semantic (quality criteria
  evaluated by scoring). Objects include types such as `situation`, `charter`,
  `scenario-set`, `transcript`, and `resolution`.
- **Morphisms** are *pipeline operations*: typed transformations that consume
  input artifacts and produce output artifacts.
- **Composition** is sequential wiring: if `f: A → B` and `g: B → C`, then
  `g ∘ f: A → C` is the pipeline that runs f then g.
- **Identity** on a type A is the pass-through operation that leaves an artifact
  unchanged.
- **Monoidal structure**: `×` (cross product) is the monoidal product, with the
  trivial empty artifact as unit. The category is symmetric monoidal — input
  order does not affect the operation.

The morphism

```
Deliberate : charter × scenario-set × roster → transcript
```

takes three inputs and produces one output. The annotation `{catalytic: roster}`
marks the roster as non-consumed — it participates in the transformation without
being altered (a dashed wire in the string diagram). Catalytic inputs are
comonoid objects — equipped with a copy map that lets them feed into multiple
operations without depletion.

**Two important refinements apply to all morphisms in this category.** First,
every morphism is a *stochastic map*: a pipeline operation does not produce a
single determinate output but a probability distribution over possible outputs.
The same inputs run twice will generally yield different texts. This means the
category **Text** is not an ordinary category of functions but a category of
*Markov kernels* — stochastic maps that compose via the Chapman–Kolmogorov
equation. Section 2a below makes this precise using Fritz's Markov category
framework (Fritz 2020), which provides the comonoid structure (copy and
discard) that the palgebra already uses informally for catalytic inputs and
waste streams.

Second, the hom-sets carry graded information: not just "does this morphism
exist?" but "at what confidence level does the output inhabit its target type?"
This makes **Text** an *enriched category* over a confidence lattice — see §2b
for the precise specification, or Kelly (*Basic Concepts of Enriched Category
Theory*) for the general framework, and the confidence propagation rules in
[reference.md](reference.md). The enrichment is what makes the soft type system
compositional — confidence degrades monotonically through composition, and this
degradation is tracked by the enriched hom-structure.

Two morphism kinds are distinguished:

- **Transformations** produce genuinely new content. The transcript is not a
  rearrangement of the charter; it is new material generated through
  deliberation.
- **Enrichments** update only the metadata of an existing artifact. Scoring a
  transcript against an evaluation rubric adds a confidence score to its front
  matter without changing its text. Enrichments are idempotent and
  re-runnable; transformations are not.

In the Markov category framework (§2a), this distinction acquires a precise
characterisation: enrichments are the *deterministic morphisms* in the sense of
Fritz (2020, Definition 10.1) — those that respect the copy structure.
Transformations are the genuinely stochastic morphisms that do not.

---

## 2a. Text as a Markov category

Section 2 described the category **Text** informally. This section gives the
precise treatment. Readers comfortable with the informal picture can skip ahead
to §3; those who need to see the axioms — or who want to understand why the
"approximate coherence" caveat in §1 is less dire than it sounds — should read
on.

### The framework

A **Markov category** (Fritz 2020, Definition 2.1) is a symmetric monoidal
category **C** in which every object X is equipped with a commutative comonoid
structure:

- A *comultiplication* (copy map): `copy_X : X → X ⊗ X`
- A *counit* (delete map): `del_X : X → I`

satisfying the commutative comonoid equations:

1. **Coassociativity**: `(copy_X ⊗ id) ∘ copy_X = (id ⊗ copy_X) ∘ copy_X`
   — copying twice in either order gives the same three copies.
2. **Counitality**: `(del_X ⊗ id) ∘ copy_X = id = (id ⊗ del_X) ∘ copy_X`
   — copying then discarding one copy gives back the original.
3. **Commutativity**: `swap ∘ copy_X = copy_X` — the two copies are
   interchangeable.

plus compatibility with the monoidal product (Fritz, equation 2.4):

4. **Monoidal compatibility**: `copy_{X⊗Y}` decomposes as copy on each factor
   then regroup — copying a pair is the same as copying each component.

and naturality of del (Fritz, equation 2.5):

5. **Naturality of delete**: `del_Y ∘ f = del_X` for every morphism
   `f : X → Y` — discarding the output of any operation is the same as
   discarding the input. Every morphism preserves the counit.

The intuition: morphisms in a Markov category are "noisy maps." Each morphism
assigns to every input value a probability distribution over output values.
Composition is the Chapman–Kolmogorov equation — the output distribution of
`g ∘ f` is obtained by running f, then running g on each possible output of f,
then aggregating (Fritz, Example 2.5, equation 2.8). The copy map represents
deterministic duplication: take an input and produce two identical copies with
no added noise. The delete map discards an input entirely.

A consequence of the del axioms is that the monoidal unit I is **terminal**:
there is exactly one morphism from any object to I (Fritz, p. 13). This is the
*semicartesian* condition — the category has projections (you can always discard
a factor) but not necessarily products in the strict categorical sense (because
a joint distribution is not determined by its marginals).

### Text is a Markov category

We claim that **Text**, as described informally in §2, carries Markov category
structure. The identification is:

| Fritz's framework | Palgebra | Notation |
|---|---|---|
| Object X | Soft type (template, rubric) | `situation`, `charter`, `transcript`, ... |
| Morphism f : X → Y | Pipeline operation: stochastic map from X-artifacts to Y-artifacts | `Deliberate`, `Fan`, `Score`, ... |
| Monoidal product X ⊗ Y | Cross product of artifact types | `charter × scenario-set` |
| Monoidal unit I | Trivial empty artifact | `Unit` |
| `copy_X` | Feed artifact X into two downstream consumers unchanged | `{catalytic: X}` — the annotation that X is reused without alteration |
| `del_X` | Discard artifact X | `{discard: X}` — the waste-stream annotation |
| Composition g ∘ f | Sequential wiring: run f, feed its output to g | `→` chaining in resource equations |

**Verifying the axioms:**

*Coassociativity and counitality of copy.* Catalytic inputs are copied by
reference — the same artifact is passed unchanged to multiple downstream
operations. Copying an artifact twice (to feed three consumers) is the same
regardless of grouping, because the artifact is not modified by the copy. This
holds by the design of the catalytic annotation: the artifact is read, not
written. Counitality says copying then discarding one copy returns the
original — trivially true when copy is pass-by-reference.

*Commutativity of copy.* The two copies of a catalytic input are
interchangeable — the artifact doesn't know which consumer it was copied for.
True by construction.

*Monoidal compatibility (equation 2.4).* Copying a compound input `charter ×
scenario-set` decomposes into copying each component separately, then
regrouping. This holds because the monoidal product is tupling of independent
artifacts — there is no entanglement between components that would make
joint copying differ from componentwise copying.

*Naturality of del (equation 2.5).* Discarding the output of a pipeline
operation is the same as discarding the input without running the operation.
This is the statement that pipeline operations have no *side effects* beyond
their declared output — no hidden state changes, no context-window pollution,
no external writes. This is a **design discipline**, enforced by the pipeline
architecture (each operation reads its inputs and writes its declared outputs,
nothing else). It is the most substantive axiom to verify: violations (such as
context-window leakage between operations) would break the Markov category
structure. The template system and the operation isolation conventions exist
precisely to maintain this property.

### What this buys

**Associativity is no longer approximate.** In a Markov category, composition
of stochastic maps is strictly associative — `(h ∘ g) ∘ f = h ∘ (g ∘ f)` as
an equality of Markov kernels. The stochasticity is *inside* each morphism
(the output is a distribution), not *around* the composition. Running the same
pipeline twice gives different sample outputs, but the *distribution* over
outputs is the same regardless of how you parenthesise the composition. The
"approximate coherence" language in §1 was responding to a real phenomenon
(sample-level variation) but misdiagnosed it as a failure of associativity.
It is not. It is the ordinary behaviour of stochastic maps composing exactly.

**The monoidal structure is semicartesian, not cartesian.** The monoidal
product X ⊗ Y has projections (discard one factor) but is not a categorical
product, because a joint output distribution is not determined by its
marginals. This is exactly right for Text: knowing the distribution over
charters and the distribution over transcripts separately does not tell you
the joint distribution over (charter, transcript) pairs, because the
transcript depends on the charter. Fritz (p. 14) makes this point explicitly
for FinStoch; it applies equally here.

**Catalytic inputs are comonoid maps.** The `{catalytic: X}` annotation is not
an informal convention but the *copy map of the Markov category*. Catalytic
inputs are precisely the objects being copied: they feed into an operation
without being consumed because copy_X produces two references to the same
artifact. The comonoid equations guarantee this is well-behaved.

**The Kleisli perspective is compatible but not required.** The earlier
formulation (§2, pre-revision) described morphisms as Kleisli arrows of an
unspecified monad M. Fritz's Corollary 3.2 shows that if one does pin down a
specific monad (such as the Giry monad for measure-theoretic probability), the
resulting Kleisli category is automatically a Markov category — provided the
monad is *commutative* in the sense of Kock (1970). Kock's result shows that
a commutative monad on a symmetric monoidal closed category induces a
symmetric monoidal structure on the Kleisli category, which is the prerequisite
for Fritz's corollary. The Giry monad is commutative (the Fubini theorem for
product measures is precisely the commutativity condition), so the Kleisli
category of Giry is symmetric monoidal and hence a Markov category.

The synthetic approach taken here is more general: we work with the Markov
category axioms directly, without committing to a specific monad. The advantage
is that the formalism does not depend on identifying the "right" monad — a
question that would require specifying a measure space on artifacts. Heunen,
Kammar, Staton, and Yang (2017) show that *quasi-Borel spaces* provide a
convenient ambient category for higher-order probability that avoids the
measure-theoretic pathologies of standard Borel spaces. If one wanted to pin
down the ambient category for **Text** — to make the Kleisli perspective
concrete — quasi-Borel spaces would be the natural candidate: they support a
probability monad, the resulting Kleisli category is a Markov category, and
they handle the higher-order structure needed for prompt-parametrised
operations. We do not need this commitment for the current development, but
it clarifies what "specifying a measure space on artifacts" would involve.

The Markov category axioms capture exactly the structure we need without
this commitment.

### Deterministic morphisms

Fritz (2020, Definition 10.1) defines a morphism `f : X → Y` in a Markov
category as **deterministic** if it respects the comultiplication:

```
copy_Y ∘ f = (f ⊗ f) ∘ copy_X
```

In words: copying the output of f is the same as copying the input and
applying f to each copy independently. For stochastic maps, this fails in
general — applying a noisy operation to two copies of the same input produces
*correlated but distinct* outputs, while copying the output of one application
produces two *identical* copies.

The deterministic morphisms form a symmetric monoidal subcategory
**Text**_det ⊆ **Text** (Fritz, Lemma 10.12). This subcategory is in fact
*cartesian* monoidal (Fritz, Remark 10.13) — it has genuine products and the
full universal property.

In the palgebra, the deterministic morphisms are exactly the **enrichments**:
operations that read an artifact and update its metadata without changing the
payload text. ScoreEvidence, Evaluate, SecurityGate — these produce the same
output given the same input (modulo negligible model-temperature variation that
can be driven to zero). They respect the copy structure: scoring two copies of
the same evidence produces two copies of the same scores.

**Transformations** — Deliberate, Fan, DraftCharter — are the genuinely
stochastic morphisms. They do not respect copy: deliberating on two copies of
the same charter will produce two different transcripts. This is not a defect;
it is the whole point. The stochasticity of transformations is what the Probe
(§9) measures.

---

## 2b. The enrichment base

The Markov category structure (§2a) handles the stochastic composition story.
The *enrichment* handles the confidence-tracking story. These are compatible
layers: **Text** is a Markov category enriched over a confidence lattice.

### The lattice

The enrichment base is:

```
V = ({Low, Medium, High}, min, High)
```

This is a three-element totally ordered set with min as the monoidal product
and High as the unit. It is a *commutative quantale* — a complete lattice in
which the monoidal product distributes over arbitrary joins. (For a
three-element total order, this is easy to verify: min distributes over max.)
Being a commutative quantale, V is a monoidal closed category and therefore
a valid enrichment base in the sense of Kelly (1982, Ch. 1.2).

### The enriched structure

For any two soft types A and B, the enriched hom-object `Hom(A, B)` is a
confidence level — the minimum confidence at which any morphism A → B has
been observed to produce outputs inhabiting type B.

The enriched composition law is:

```
confidence(g ∘ f) = min(confidence(f), confidence(g))
```

This says: the confidence of a composed pipeline is bounded by its weakest
link. A Medium-confidence evidence-gathering step followed by a
High-confidence scoring step yields a Medium-confidence result.

### Verification of the enrichment axioms

The enrichment axioms (Kelly, Ch. 1.2, specifically equations 1.1–1.4) require:

1. **Composition is a V-morphism** (Kelly, eq. 1.1): the composition map
   `M : Hom(B,C) ⊗ Hom(A,B) → Hom(A,C)` sends `(c₂, c₁) ↦ min(c₂, c₁)`.
   This must be associative: `min(c₃, min(c₂, c₁)) = min(min(c₃, c₂), c₁)`.
   True because min is associative. Kelly requires this as a morphism in V
   (a monotone map between hom-objects); it is, because min is monotone in
   each argument.

2. **Identity is maximal** (Kelly, eq. 1.2): `j_A : I → Hom(A, A)` picks out
   the identity element High ∈ V. The unit axiom requires
   `M ∘ (id ⊗ j_A) = id = M ∘ (j_A ⊗ id)` — composing with the identity
   morphism at confidence High does not degrade confidence. True because
   `min(c, High) = c`.

3. **Associativity** (Kelly, eq. 1.3): the two ways of composing three
   enriched hom-objects agree. This holds because min is associative.

4. **Unit coherence** (Kelly, eq. 1.4): the left and right unit maps compose
   correctly. This follows from min being commutative and High being its unit.

These four conditions are exactly Kelly's definition of a V-category (Kelly
1982, Definition 1.2). Our verification is simple because V is a total order
— the conditions become equations about min on a three-element chain. In a
richer enrichment base (such as the product quantale V^5 for vector scores),
verification would require checking the conditions componentwise.

### Multi-dimensional scores

The three-element lattice captures the *pipeline-level* confidence
propagation. Within individual rubrics, scoring is richer: five criteria, each
0–3, with semiring (weighted sum) or Pareto (multi-objective frontier)
combination. These internal scoring structures are not part of the enrichment
— they operate *inside* the scoring morphisms, producing the metadata that the
enrichment then tracks through composition. The relationship is:

- **Within a rubric**: criteria combine via domain-specific rules (semiring,
  Pareto, etc.) to produce a confidence band.
- **Across pipeline stages**: confidence bands combine via min-lattice — the
  enrichment.

The enrichment base is the min-lattice. The other structures are internal to
the enrichment morphisms.

---

## 2c. The layered structure of Text

Sections 2, 2a, and 2b developed three categorical perspectives on the
pipeline. This section makes explicit that they are compatible layers of a
single framework, not parallel stories told about the same objects.

### The three layers

**Layer 1: The deterministic base — Text_det.** The subcategory of
deterministic morphisms (Fritz, Definition 10.1, Lemma 10.12). Objects are
soft types. Morphisms are operations that respect the copy structure:
enrichments, structural transformations (tagging, projection, template-fill),
and the coproduct injections of §5. This subcategory is *cartesian* monoidal
(Fritz, Remark 10.13) — it has genuine products, and universal properties hold
strictly. The template system, the metadata join operator `⊔`, and the
provenance accumulation rules all live here. Layer 1 is where the pipeline's
bookkeeping is exact.

**Layer 2: The Markov category — Text.** The full category of stochastic
pipeline operations, with the Markov category structure of §2a. Objects are
the same soft types. Morphisms are Markov kernels — stochastic maps that
compose via Chapman–Kolmogorov. The comonoid structure (copy and delete)
provides catalytic inputs and waste streams. Layer 2 contains Layer 1 as a
subcategory: every deterministic morphism is a Markov kernel that happens to
be non-stochastic. The distinction between transformations (genuinely
stochastic) and enrichments (deterministic) is precisely the distinction
between morphisms that live only in Layer 2 and those that also live in
Layer 1.

**Layer 3: The enriched category — Text over V.** The Markov category
enriched over the confidence lattice V = ({Low, Medium, High}, min, High)
as specified in §2b. The enrichment tracks quality degradation through
composition: `confidence(g ∘ f) = min(confidence(f), confidence(g))`. This
layer does not replace Layers 1–2; it *decorates* them with quality
information. Every morphism in Layer 2 carries a confidence grade from
Layer 3. Every deterministic morphism in Layer 1 operates at confidence
High (the unit of V), because deterministic operations introduce no quality
degradation.

### How the layers interact

The layers are not independent choices. They form a single coherent structure:

```
Text_det  ⊆  Text  →  enriched over V
  (L1)        (L2)         (L3)

L1 ⊂ L2:  deterministic ⊂ stochastic (Fritz, Lemma 10.12)
L3 on L2:  every L2 morphism carries a V-grade
L3 on L1:  all L1 morphisms have grade High (no quality loss)
```

**Layer 1 inside Layer 2** is the subcategory inclusion. The enrichments
(Score, Evaluate, SecurityGate) and the structural operations (tagging
injections, template-fill, projection) belong to Layer 1. The
transformations (Fan, Deliberate, DraftCharter, Resolve) belong to Layer 2
but not Layer 1. This inclusion is not a design choice — it is a consequence
of the Markov category axioms: deterministic morphisms are closed under
composition and contain the identities (Fritz, Lemma 10.12).

**Layer 3 on top of Layer 2** is enrichment in the sense of Kelly (1982,
Ch. 1.2). The enrichment does not change the morphisms — it adds a quality
grade to each one. The min-composition law means that Layer 3 automatically
tracks quality through the Layer 2 composition. No additional structure is
needed: the enrichment axioms (§2b) are compatible with the Markov category
axioms (§2a) because the enrichment operates on the hom-objects, not on the
composition rule.

**The three propagation rules** from
[reference.md](reference.md) and
[decorated-texts.md](decorated-texts.md) correspond to the layers:

| Propagation rule | Layer | Mechanism |
|---|---|---|
| Confidence can only degrade | Layer 3 | min-lattice enrichment |
| Provenance can only accumulate | Layer 1 | Monotone metadata join in **Text**_det |
| Content transforms | Layer 2 | Stochastic morphisms in **Text** |

Confidence degradation is a Layer 3 phenomenon. Provenance accumulation is a
Layer 1 phenomenon (metadata operations are deterministic). Content
transformation is a Layer 2 phenomenon (stochastic generation of new text).
The three rules are not ad hoc — they are consequences of the layered
structure.

### What this integration clarifies

**The "approximate" qualifier has a precise scope.** Compositional coherence
(associativity, identity laws, comonoid equations) holds exactly in Layer 2 —
it is a property of the Markov category structure. Universal properties
(products, coproducts, equalizers) are design targets that the pipeline
approximates — they hold exactly in Layer 1 (where the subcategory is
cartesian) but only approximately for the stochastic operations of Layer 2.
The Probe (§9) tests the Layer 2 approximation. The approximation metric
(§4.1) quantifies it. Conflating "compositional coherence is approximate"
with "universal properties are approximate" was the error that the Markov
category framework (Layer 2) corrected: the first is false, the second is
true and measurable.

**Quality tracking is not bolted on.** The enrichment (Layer 3) is not a
separate system that happens to run alongside the pipeline. It is a
categorical structure on the same category — the confidence grades are part
of the hom-objects, and the min-composition law is a consequence of the
enrichment axioms. This means quality tracking composes the same way the
pipeline composes. There is no gap between "the pipeline works" and "the
pipeline tracks its own quality."

**Deterministic operations are special, not second-class.** Layer 1 is not
a degenerate case of Layer 2. It is a structurally richer subcategory —
cartesian where Layer 2 is only semicartesian, with genuine products where
Layer 2 has only semicartesian projections. The operations that live in
Layer 1 (enrichments, structural transformations, injections) are the ones
where the full universal properties hold. The pipeline's bookkeeping —
scoring, gating, tagging, provenance — is exact. The stochasticity lives
in the content-generating operations, which is exactly where it belongs.

---

## 3. Terminal and Initial Objects

A **terminal object** 1 has exactly one morphism into it from every object X.
It is the universal sink — everything maps to it, nothing informative maps *out*.

In the category of committee outputs, the *vacuous resolution* — "a situation
was considered and a response was formulated" — is terminal. Every deliberation
maps to it via the information-discarding projection that strips all specific
content. Its presence is diagnostic: if the committee produces something
isomorphic to the terminal object, the funnel has collapsed without doing work.

In a typed pipeline, `Unit` is the terminal type. Every pipeline stage has a
unique morphism into Unit (discard all output). The `{discard: C}` annotation in
palgebra resource equations marks the *site* where this morphism is applied —
the point where an output is dropped from the pipeline.

An **initial object** 0 has exactly one morphism from it to every object X.
It is the universal source — anything can be generated from it, which means
nothing is constrained.

Two complementary perspectives illuminate how this works in the pipeline:

*Operationally*, the maximally ambiguous situation description is close to
initial: when the input constrains nothing, the narrators have no surface to
push against, and the scenarios they generate are unconstrained artifacts rather
than genuine explorations of a determinate possibility space. This is "close to"
rather than "exactly" initial because the uniqueness condition does not hold
strictly — there is no single canonical way to generate a transcript from an
empty prompt, only an unconstrained distribution over possible transcripts.

*Type-theoretically*, `False` (⊥) is the initial type: from an incoherent
premise, any conclusion follows. The practical analog is a charter that contains
a contradiction: a committee chartered on inconsistent premises can justify any
resolution, which is precisely no justification at all. This is a different
pathology from the operational one — not "too little constraint" but "incoherent
constraint" — but both move the pipeline toward initial-object behaviour, where
the output carries no information traceable to the input.

The quality of the fan's input situation can be understood as its distance from
the initial object: a well-framed situation is far from initial (it constrains
the pipeline's output space meaningfully), and a poorly framed one is close.

---

## 4. Products

The **product** A × B of two objects comes with *projection morphisms*
π₁: A × B → A and π₂: A × B → B. Its universal property states: any object X
equipped with maps f: X → A and g: X → B factors uniquely through A × B via the
pairing ⟨f, g⟩: X → A × B. The product is the *minimal object* from which both
A and B are recoverable.

**The charter as approximate product of situation and scenario-set.** In the
composed pipeline, the charter carries both the framed problem and the scenario
context into the deliberation. A well-constructed charter should support two
approximate projections: recover the original situation framing (strip the
scenarios) and recover the scenario-set context (strip the problem framing). Any
pipeline operation needing both — the Deliberate operation most prominently —
routes through the charter.

In practice, the charter is produced by a `DraftCharter` transformation that
*compresses* its inputs, not a genuine categorical product that preserves them
faithfully. The projections are lossy: the charter summarises and reframes
rather than merely packaging. This means the charter is a product *target* — a
design criterion that says "both the situation and the scenario-set should be
recoverable from the charter" — rather than a product *fact*. The charter rubric
can enforce this: a charter that garbles either projection scores lower on
completeness, and the quality gate catches it. The product structure is
maintained by design discipline, not by categorical necessity. (This is an
approximate universal property in the sense distinguished in §1 — the
compositional structure is exact, but the product structure is a design target
quantified by the reconstruction error of §4.1.)

**The transcript as approximate product of character positions.** The
deliberation transcript carries all five character position-streams. Each
character's contribution defines an approximate projection: π_Maya:
transcript → Maya's position record, and so on for Frankie, Joe, Vic, and
Tammy. The product interpretation says that any operation reasoning about what
a character said must route through the transcript.

The transcript is closer to a genuine product than the charter, because it is a
*full record* rather than a summary: the template requires that all speech acts
are preserved verbatim. A transcript that summarises rather than records is a
*lossy* product: the projections are no longer faithful, and auditability is
lost. This is why the palgebra insists transcripts are full records — the
product structure is worth maintaining, and it is maintained by the structural
constraint (the template), not by any abstract guarantee.

### 4.1 The approximation metric

The preceding discussion calls the charter an "approximate product" and the
transcript a "closer" one. Without a metric, "approximate" is vacuous — every
function of two arguments could be called an "approximate product." This
subsection gives the qualifier a precise meaning.

**Reconstruction error.** For a candidate product P of types A and B, with
approximate projections π̃₁ : P → A and π̃₂ : P → B and construction morphism
c : A × B → P, define the *reconstruction error*:

```
ε(P) = E[ d_A(a, π̃₁(c(a, b))) ] + E[ d_B(b, π̃₂(c(a, b))) ]
```

where the expectations are over pipeline runs (since c, π̃₁, and π̃₂ are Markov
kernels — stochastic maps — the expectation averages over their output
distributions), and d_A, d_B are rubric-based similarity scores on the
respective artifact types. If P were a genuine categorical product with faithful
projections, the reconstruction error would be zero: constructing the product
and projecting back would recover the original inputs exactly (up to equality of
Markov kernels).

The similarity scores d_A and d_B are not arbitrary — they are derived from the
rubric's completeness criterion for the relevant type. The situation rubric
defines what it means for a situation description to be complete; comparing an
original situation with one reconstructed from the charter via π̃₁ measures how
much the charter's compression lost. This grounds the metric in the same
quality infrastructure the pipeline already uses for scoring.

**What "approximate product to within ε" means.** The charter is an
*approximate product of situation and scenario-set to within ε* when the
reconstruction error ε(charter) is below the threshold ε. The threshold is a
design target: the charter rubric's completeness criterion sets the acceptable
loss. A charter that scores High on completeness has low reconstruction error; a
charter that scores Low has high reconstruction error and should be caught by
the quality gate.

**Connection to the Probe.** The Probe operation (§9) provides empirical
samples of the reconstruction error. Each Probe run produces a charter from the
same inputs; comparing the N charters' projections against the original inputs
gives N samples of ε(charter). The variance report quantifies:

- The *mean* reconstruction error — how lossy is the charter on average?
- The *variance* of reconstruction error — how stable is the compression?
- Whether the error is *systematic* (the charter consistently loses the same
  information) or *stochastic* (different runs lose different things).

High mean error with low variance indicates a design problem: the charter
template or DraftCharter prompt systematically discards important input
structure. Low mean error with high variance indicates an engineering problem:
the compression is adequate on average but unreliable. The Probe distinguishes
these failure modes, which the categorical structure alone cannot.

**The transcript's tighter bound.** The transcript has lower reconstruction
error than the charter because its template requires verbatim preservation of
all speech acts. The projections πₖ : transcript → positionₖ are extraction
operations (filtering by speaker tag), not summarisation. For a well-formed
transcript, the reconstruction error approaches zero — the projections are
faithful, and the transcript approaches a genuine product. The template
constraint is what enforces this: it is a structural guarantee rather than a
statistical tendency, placing the transcript in the deterministic subcategory
**Text**_det (§2a) for the purpose of projection.

---

## 5. Coproducts

The **coproduct** A + B comes with *injection morphisms* ι₁: A → A + B and
ι₂: B → A + B. Its universal property states: for any object X and any family
of morphisms fₖ: Aₖ → X, there exists a unique morphism [f₁,...,fₙ]: A₁ + ⋯ + Aₙ → X
such that [f₁,...,fₙ] ∘ ιₖ = fₖ for each k. The coproduct is a *disjoint
union that retains provenance* — each element remembers which component it came
from.

### 5.1 The scenario-set as coproduct of scenarios

The fan produces four scenarios (Continuity, Disruption, Opportunity,
Constraint). Their coproduct is the `scenario-set`:

```
scenario-set = scenario_C + scenario_D + scenario_O + scenario_K
```

**The injections, precisely.** Each injection ιₖ : scenarioₖ → scenario-set is
the operation that:

1. Tags the scenario with its index k ∈ {C, D, O, K}.
2. Attaches the source narrator's identity and assumption-set as provenance
   metadata.
3. Includes the tagged scenario in the collected set.

In the Markov category setting (§2a), each ιₖ is a *deterministic morphism* in
the sense of Fritz (Definition 10.1): it respects the copy structure, because
tagging and including a scenario is a structural operation that adds no
stochastic content. Copying a scenario then injecting it gives the same result
as injecting it then copying the result — the injection commutes with the
comonoid structure. This places the injections in the cartesian subcategory
**Text**_det (Fritz, Remark 10.13), which is exactly where structural
bookkeeping operations belong.

The injections are not bare inclusions — they carry the provenance annotations
(narrator, assumption-set, divergence axis) that make scenarios distinguishable
in committee deliberation. This is the *decorated coproduct*: the operative
site of Fong's decorated cospan construction (Fong 2016, Ch. 2). In Fong's
framework, a decorated cospan is a cospan `A → N ← B` equipped with a
decoration on the apex N drawn from a symmetric monoidal functor
`F : Cospan → Set`. The pushout of the cospan legs determines how the
decorations compose. Here the apex is the scenario-set, the legs are the
injection morphisms ιₖ, and the decorations are the assumption-annotations.
The pushout composition of decorated cospans is what makes the committee
pipeline compositional: wiring two decorated operations together produces a
decorated operation whose decorations combine via the pushout of their shared
interface. This is not an analogy — it is the specific mechanism from Fong's
thesis that the palgebra's pipeline wiring instantiates.

**The universal property, precisely.** For any soft type X and any family of
morphisms fₖ : scenarioₖ → X (one per scenario), there exists a morphism
[f_C, f_D, f_O, f_K] : scenario-set → X such that:

```
[f_C, f_D, f_O, f_K] ∘ ιₖ = fₖ    for each k ∈ {C, D, O, K}
```

In the Markov category setting, "exists uniquely" means *equality as Markov
kernels*: the induced morphism [f_C, f_D, f_O, f_K] is the unique stochastic
map (up to equality of the corresponding probability distributions over
X-artifacts) that extends the componentwise family. The factoring morphism
operates by dispatching on the tag: given a tagged scenario in the coproduct,
it reads the tag, selects the corresponding fₖ, and applies it. Since the tag
is deterministic metadata, the dispatch is deterministic; the stochasticity
lives entirely inside the individual fₖ.

**What the universal property buys.** Any pipeline operation that handles the
full scenario-set — coverage assessment, charter drafting, committee
deliberation — can be defined *componentwise* (by specifying what it does with
each scenario) and uniquely extended to the full set. This is what licenses the
committee's scenario-by-scenario reasoning as a valid method for producing a
resolution about the whole set. The categorical structure is not decorative
here: it constrains the space of valid operations on scenario-sets to those
that decompose into per-scenario operations composed with the injections. An
operation that treats the scenario-set as an opaque blob, ignoring provenance
tags, is *not* a valid morphism out of the coproduct.

### 5.2 The variance report as coproduct of Probe runs

Across N runs of the composed fan → funnel pipeline, each resolution is an
injection into the variance report:

```
variance-report = resolution₁ + resolution₂ + ⋯ + resolution_N
```

Each injection ιⱼ : resolutionⱼ → variance-report tags the resolution with its
run index j, the random seed or ordering parameters used, and any metadata
distinguishing this run from the others. As with the scenario-set injections,
these are deterministic morphisms in **Text**_det.

**The Map operation as instance of the universal property.** The Map operation
(see [duality-and-composition.md](duality-and-composition.md)) produces a
decision-landscape-map from the variance report:

```
variance-report → decision-landscape-map  [Map]
```

Map is an instance of the coproduct's universal property. The construction is:

1. For each resolution j, define a morphism fⱼ : resolutionⱼ → decision-landscape-map
   that extracts the structural features of that resolution — its recommendation,
   key claims, vote pattern, identified tensions — and records them as a data
   point in the landscape.

2. The family {f₁, ..., f_N} uniquely determines the factoring morphism
   [f₁, ..., f_N] : variance-report → decision-landscape-map, which operates
   componentwise: it processes each resolution according to its corresponding fⱼ,
   then assembles the results into the landscape summary (basins, ridges,
   load-bearing assumptions, robust actions).

3. The universal property guarantees that this is the *unique* way to produce a
   decision-landscape-map from the variance report that is consistent with the
   per-resolution extractions. Any other morphism variance-report → decision-landscape-map
   that agrees with each fⱼ on the corresponding component must equal Map (as
   Markov kernels).

In practice, the fⱼ are identical operations (the same structural-feature
extraction applied to each resolution), so the factoring morphism is a uniform
componentwise extension. This is the simplest case of the universal property —
and the most common one in the palgebra, since the Probe deliberately runs the
same pipeline under the same conditions, varying only the stochastic seed.

**Interpreting the landscape through the coproduct.** If the coproduct has one
non-trivial component class (all resolutions produce isomorphic structural
features), the decision landscape has one basin — the decision is robust. If it
has multiple non-isomorphic component classes, there are multiple basins and the
ridge structure requires examination before commitment. The number of distinct
component classes in the coproduct is a measure of decision-landscape
complexity, directly derivable from the coproduct structure.

---

## 6. Equalizers and Coequalizers

*The constructions in §§6–7 are **categorical design specifications**, not
claims about existing pipeline operations. The morphisms they require —
"claim-extraction maps," "interpretation maps" — do not yet exist as named
operations in the palgebra resource equations. The value of stating these
constructions is prescriptive: the categorical structure tells us what
operations would be worth building and what properties they should have. If
and when these operations are implemented, the constructions become testable
claims. Until then, they are a requirements spec derived from category theory.*

Given two morphisms f, g: A → B, their **equalizer** is an object E with a map
e: E → A such that f ∘ e = g ∘ e, universal among all such objects. The
equalizer picks out the *subobject of A where f and g agree*.

**Cross-scenario triangulation.** Let A be a collection of situation
descriptions, B the space of factual claims, and let f and g be claim-extraction
maps of two different narrators. (These maps are potential operations that the
equalizer construction motivates defining.) The equalizer E is the
sub-collection of situation descriptions on which both narrators produce the
same claim — the *zone of uncontested framing*. Claims in the equalizer are
load-bearing: they survive independent lenses and deserve the most scrutiny in
deliberation.

Diagnostically: if E ≅ A (the equalizer is the whole domain), the two narrators
are not genuinely divergent — the fan has failed to produce variety. If E is
empty, the narrators share no common ground, which may indicate the situation
framing is pathologically underspecified.

The **coequalizer** of f, g: A → B is an object Q with a map q: B → Q such that
q ∘ f = q ∘ g, universal among all such. The coequalizer *quotients B by the
identification* generated by the two maps: it is the coarsest object into which
both f and g inject consistently.

**The resolution as quotient of competing positions.** Let A be the space of
situations, B the space of position-texts, and let f and g be two characters'
interpretation maps from shared evidence. (As with the claim-extraction maps
above, these interpretation maps are a categorical reading of what the
characters do, not named operations in the current resource equations.) The
coequalizer Q is the resolution that identifies f(a) and g(a) for every
situation a — the text in which the distinction between the two characters'
framings has been absorbed into a justified commitment.

The funnel constructs this coequalizer. The adversarial deliberation is the
process of finding the right quotient: coarse enough to subsume both positions,
fine enough not to collapse to the terminal object (the vacuous resolution that
says nothing). Each character resists premature identification of their position
with an opposing one — that resistance is what keeps the coequalizer
non-degenerate.

---

## 7. Pullbacks and Pushouts

The **pullback** of f: A → C and g: B → C is an object P with maps p₁: P → A
and p₂: P → B such that f ∘ p₁ = g ∘ p₂, universal among all such. It is the
*fibered product*: the part of A × B that is consistent over C.

**Load-bearing claims.** Let A be the Disruption scenario text, B the Constraint
scenario text, and C the space of claims about the operating environment. Let f
and g be the claim-extraction maps for each scenario. The pullback P is the set
of (disruption-fragment, constraint-fragment) pairs that extract to the same
claim in C: the shared assertions that survive *independent* narrative lenses.

This is the formal structure of the CoverageGate operation. Claims in the
pullback are independently corroborated across scenarios; claims unique to one
scenario are possible narrative artifacts. The pullback makes visible which
assumptions are doing real work in the scenario set versus which are
narrator-specific embellishments.

The **pushout** of f: C → A and g: C → B is an object Q with maps q₁: A → Q and
q₂: B → Q such that q₁ ∘ f = q₂ ∘ g, universal among all such. It is the
*fibered coproduct*: the amalgamation of A and B along their shared sub-object C.

**The resolution as amalgamation over shared evidence.** Let C be the shared
evidentiary record (charter plus scenario-set — everything the committee has
read), A Maya's position text, and B Frankie's position text. The interpretation
maps f and g send shared evidence into each character's position.

The pushout Q is the resolution that amalgamates both positions by identifying
their shared evidentiary ground. It is not Maya's position, not Frankie's, and
not an average: it is the minimal object into which both positions inject
consistently. If C is thin (the committee lacks common ground — poor charter,
inadequate scenario framing), the pushout degenerates toward a bare coproduct
(A + B: a list of positions rather than a synthesis). The quality of the charter
is therefore the quality of the common base C in the pushout diagram.

This pushout is exactly the composition operation for Fong's decorated cospans
(Fong 2016, Ch. 2): the resolution is the apex of the composed cospan, obtained
by pushout over the shared evidentiary base. The decorated cospan framework
ensures that composition is associative and that decorations (provenance,
confidence grades) propagate correctly through the pushout. The palgebra's
pipeline wiring inherits this compositional guarantee.

---

## 8. Fan and Funnel as Divergent and Convergent Spiders

The two core pipeline operations are *spiders* in the string diagram calculus:
nodes of higher arity that generalise the basic binary product and coproduct.
The fan is a coproduct spider (one-to-many, divergent) and the funnel is a
product spider (many-to-one, convergent). Their visual topology — one wire in
and many out, or many in and one out — is the defining feature.

(A note on what this section does *not* claim: earlier versions of this
document described fan and funnel using the algebraic terminology
"multiplication" and "comultiplication," suggesting a Frobenius algebra
structure. A Frobenius algebra requires four maps satisfying the Frobenius
equation `(μ ⊗ id) ∘ (id ⊗ δ) = δ ∘ μ = (id ⊗ μ) ∘ (δ ⊗ id)`. We have
not verified this equation — and it likely does not hold in general, since
it would require that partially funnelling then fanning equals fanning then
partially funnelling. We retain the spider *visual* but do not claim the
Frobenius algebraic structure.)

**The fan (divergent spider / one-to-many)** injects a single situation into
multiple distinct narrative contexts:

```
situation × params → scenario_1 + scenario_2 + scenario_3 + scenario_4  [Fan]
  {catalytic: params}
```

Each injection carries the source narrator's lens as a decoration. The fan is
the divergent half of the pipeline: it releases the ambiguity of the situation
into an explicitly structured space of possibilities. The universal property of
the resulting coproduct licenses componentwise reasoning downstream.

**The funnel (convergent spider / many-to-one)** combines multiple inputs into
a single committed output:

```
charter × scenario-set × roster × character-propensities × roberts-rules → transcript  [Deliberate]
  {catalytic: character-propensities, roberts-rules}
```

The resolution is the product of all the perspectives that contributed to it;
each character's position is recoverable via projection. The funnel is the
convergent half: it collapses the coproduct of perspectives into a committed
product with recoverable provenance.

**Composition: the deliberated choice.** Fan → funnel is the *decision
pipeline* — an endofunctor with monad-like structure:

```
M(situation) = Funnel(Fan(situation))
```

The monad laws generate operational quality criteria. The unit law: fanning and
immediately collapsing without deliberation should return approximately the
original situation — the pipeline added nothing. The associativity law: nested
fan-funnel-fan-funnel should be equivalent to a single well-designed fan-funnel.
Both are testable by running the pipeline with degraded deliberation and
comparing output to input. See
[duality-and-composition.md](duality-and-composition.md) for the full
treatment, including the precise status of the monad claim.

---

## 9. The Probe as Statistical Test of Categorical Properties

The constructions in §§4–7 claim that pipeline objects satisfy categorical
universal properties — that the charter is an approximate product, that the
scenario-set is a coproduct, that the resolution is an approximate pushout.
Section 4.1 gave "approximate" a metric (reconstruction error). This section
develops the Probe operation as a *statistical test* of those claims, grounding
the eigenform concept in the Markov category framework and connecting it to
well-defined hypothesis testing.

### The pipeline as Markov kernel

The composed pipeline `M = Funnel ∘ Fan` is a morphism
`M : situation → resolution` in **Text**. By the Markov category structure
(§2a), M is a Markov kernel: it assigns to each input situation s a probability
distribution M(s) over resolution-artifacts. Two runs of M on the same input
produce different resolution texts, but both are samples from the same
distribution M(s). The distribution is well-defined even though we cannot write
it in closed form — it is determined by the pipeline's architecture, the model's
stochastic generation process, and the template constraints.

The key observation is that M(s) encodes everything the pipeline "knows" about
situation s. The categorical properties of the pipeline — whether the charter
is a product, whether the factoring morphisms are unique — are properties of
M(s) as a distribution. They can therefore be *tested empirically* by sampling
from M(s).

### The Probe as Monte Carlo sampling

The **Probe** operation runs M on the same input s a total of N times, producing
resolutions r₁, r₂, ..., r_N. In the Markov category framework, this is a
precise construction: the copy map `copy_situation` (§2a) produces N identical
copies of s, and each copy is fed independently to M. The independence of Probe
runs follows from the comonoid structure: copying then applying M to each copy
independently is exactly what the Markov category axioms license. In Fritz's
conditional independence framework (Fritz 2020, Section 12), the N outputs
display the independence `r_i ⊥ r_j | s` for all i ≠ j — each resolution is
conditionally independent of every other given the shared input.

The N resolutions are therefore i.i.d. samples from M(s). The variance report
is their coproduct (§5.2), and the Map operation synthesises it into a
decision-landscape-map. The landscape's structure — basins, ridges,
load-bearing assumptions — is an empirical estimate of the structure of M(s).

### Eigenforms as support structure

**Eigenforms** are the resolution-content present in every Probe run: the
invariant sub-structure that the pipeline reliably produces regardless of the
particular stochastic trajectory. In the Markov category framing, eigenforms
are the *support structure* of the distribution M(s) — specifically, the
features shared by all (or nearly all) elements in the support. If a
recommendation appears in every one of N independent samples, it is almost
certainly in the support of M(s); its presence is a structural feature of the
distribution, not a stochastic accident.

**Residues** are run-specific content: features that appear in some samples but
not others. These are the trajectory-dependent parts that reflect particular
deliberation dynamics — which character spoke first, which analogy happened to
land, which rhetorical move shifted the vote — rather than the structure of the
situation itself. The Probe separates eigenforms from residues empirically,
which is what Deleuzian repetition does philosophically: difference produced by
repetition reveals the topology of the space.

The eigenform/residue distinction has a precise probabilistic interpretation.
Let φ be a structural feature extractor (e.g., "extract the primary
recommendation" or "extract the list of identified risks"). Then:

- φ is an **eigenform** of M at s if `P[φ(r) = v | r ~ M(s)] ≈ 1` for some
  value v — the feature is deterministic even though the full resolution is
  stochastic. In the Markov category, this means φ ∘ M is a *deterministic
  morphism* in the sense of Fritz (Definition 10.1): it respects the copy
  structure, because applying it to two independent samples gives the same
  result.

- φ is a **residue** if the distribution of φ(r) under M(s) has high entropy
  — the feature varies substantially across runs. The morphism φ ∘ M is
  genuinely stochastic.

The entropy of the feature distribution φ(M(s)) quantifies how much
information the pipeline loses about the input situation at the level of
feature φ. Perrone (2024) extends Fritz's Markov category framework with a
categorical treatment of entropy, defining functorial entropy measures on
Markov categories that compose correctly through morphism composition. The
confidence degradation rule (§2b) — that confidence can only degrade through
composition — is an instance of Perrone's monotonicity result: the entropy of
a composed pipeline is at least the entropy of its components. The min-lattice
enrichment tracks a coarse summary (three confidence bands) of what Perrone's
framework tracks precisely (functorial entropy on Markov categories).

This gives the eigenform concept a categorical home: eigenforms are the features
for which the composed morphism φ ∘ M lands in the deterministic subcategory
**Text**_det (Fritz, Lemma 10.12, Remark 10.13). The Probe empirically
identifies which features are deterministic and which are stochastic.

### Universal properties as distributional hypotheses

The connection between eigenforms and universal properties is where the Probe
becomes a genuine statistical test. Recall that the universal property of a
product requires a *unique* factoring morphism: for any morphism h into the
product's components, there is exactly one morphism through the product that
recovers h. In the Markov category, "exactly one" means equality as Markov
kernels — a single well-defined distribution.

This uniqueness corresponds to a distributional property of M(s):

**Unimodality hypothesis.** If the pipeline's construction satisfies the
relevant universal property, then the distribution M(s) should have a single
mode — one basin in the decision landscape. Multiple distinct modes (multiple
basins) indicate that the factoring morphism is not unique: the pipeline
produces categorically distinct resolution-types depending on the stochastic
trajectory. This is a failure of the universal property.

The Probe converts this into a testable statistical question:

```
H₀: M(s) is unimodal (universal property holds — one basin)
H₁: M(s) is multimodal (universal property fails — multiple basins)
```

The test procedure is:

1. Run the Probe N times, producing resolutions r₁, ..., r_N.
2. Extract structural features: recommendations, key claims, vote patterns,
   identified tensions.
3. Cluster the resolutions by structural similarity.
4. Test whether the clustering reveals one dominant cluster (unimodal) or
   multiple distinct clusters (multimodal).

The number of distinct component classes in the variance report's coproduct
(§5.2) is the empirical estimate of the number of modes. One class means the
decision is robust — the universal property holds approximately. Multiple
classes means the decision landscape has structure that requires examination
before commitment.

### What the Probe measures, precisely

The Probe provides three distinct measurements, each corresponding to a
different categorical property:

**Mean reconstruction error** (§4.1) tests how close the pipeline's
construction is to satisfying the universal property. High mean error means
the construction systematically fails — the charter loses too much information,
the projections are too lossy. This is a property of the pipeline's *design*
(templates, prompts, model choice).

**Variance of reconstruction error** tests the *stability* of the construction.
Low mean with high variance means the pipeline approximates the universal
property on average but unreliably — some runs produce faithful products, others
don't. This is an *engineering* problem (temperature settings, prompt
sensitivity) rather than a design problem.

**Number of modes** tests the *uniqueness* of the factoring morphism. Multiple
modes with low intra-mode variance means the pipeline has multiple stable
operating points — it reliably produces one of several categorically distinct
outputs, and which one depends on the stochastic trajectory. This is the most
consequential finding: it means the decision landscape has genuine structure
(ridges, basins) that the single-run pipeline obscures.

These three measurements decompose the gap between the pipeline's actual
behaviour and the ideal categorical construction into independently actionable
components. The categorical structure tells us *what to measure*; the Probe
provides the *samples*; standard statistical methods provide the *test*.

### Connection to broader eigenform theory

The eigenform concept connects the categorical treatment to a broader picture of
meaning in LLM-mediated systems. Concepts in a human-LLM exchange are themselves
eigenforms of the conversational process — temporary stabilisations produced by
recursive interaction, not fixed objects stored in either participant
([From Semantic Potential to Situated Sense](../wild/potential-to-sense/from_semantic_potential_to_situated_sense.md)).
The pipeline's categorical structures are the *structural* eigenforms: the
patterns of composition, projection, and injection that stabilise across runs
even when the *content* varies.

This is why the distinction drawn in §1 — between compositional coherence
(which holds exactly in the Markov category) and universal properties (which
hold approximately) — matters. The structure composes reliably; the content
varies. The eigenforms are where these meet: structural invariants that
persist across stochastic variation. The Probe, by sampling from the pipeline's
Markov kernel and decomposing the results into eigenforms and residues, makes
this meeting point empirically visible.

---

## 10. Connections

The categorical treatment of the committee pipeline has a complementary
game-theoretic formalization in
[The Adversarial Committee as an Open Game](../wild/committee-games/committee-as-open-game.md).
Where this document asks "what categorical constructions does the pipeline
instantiate?", the open-game treatment asks "what does equilibrium mean for a
committee whose goal is coverage rather than utility maximization?" The pushout
treatment of resolutions in §7 — amalgamation of competing positions over shared
evidence — is closely related to the game-theoretic equilibrium structure: both
describe the resolution as the minimal object that honestly integrates all
perspectives. The backward-flowing evaluation signal in the open-game framework
(rubric scores as continuation functions) provides the strategic dimension that
the categorical treatment leaves implicit.

The soft type system is formalised in
[soft-type-theory.md](soft-type-theory.md), which develops graded type
inhabitation as quantale-valued presheaves on the type lattice (§§2–3 of that
document) and extends to distributional type membership — the "furry logic" of
[the diary entry](../wild/diary/2026-03-13-furry-logic.md) — in §4. The
distributional extension connects directly to the Markov category framework:
the type assignment `a ↦ μ_a ∈ Prob(T)` is a Markov kernel, and pipeline
operations compose with type assignments via Chapman–Kolmogorov. The
three-layer architecture (§2c) maps cleanly onto the soft type theory:
deterministic type assignments (Layer 1), stochastic type assignments
(Layer 2), and confidence-graded type assignments (Layer 3).

The distributional type extension has a natural connection to the
*disintegration* framework of Cho and Jacobs (2019). Disintegration is the
categorical operation that decomposes a joint distribution into a marginal
and a conditional — the Bayesian inversion that recovers `P(type | text)`
from the joint `P(type, text)`. In the soft type context, the type
assignment kernel `τ : Artifacts → Prob(T)` is precisely such a conditional:
given a text, what is the distribution over types? Cho and Jacobs develop
this via string diagrams in Markov categories, which means the disintegration
composes correctly with the pipeline's other string-diagrammatic structure.
The Bayesian inversion — going from `P(text | type)` (generative: what texts
does this type produce?) to `P(type | text)` (discriminative: what type does
this text have?) — is the formal version of the measurement framing in
[soft-type-theory.md](soft-type-theory.md): rubric evaluation is
discriminative classification, and the distributional type assignment is
the result of Bayesian inversion on the generative pipeline.

---

## References

**Lawvere, F. William, and Stephen Schanuel.** *Conceptual Mathematics: A First
Introduction to Categories.* Cambridge University Press, 1997. — Accessible
entry point; emphasises conceptual over technical.

**Spivak, David I.** *Category Theory for the Sciences.* MIT Press, 2014. —
Applications-focused; bridges formal machinery and scientific domains.

**Fong, Brendan, and David I. Spivak.** *Seven Sketches in Compositionality: An
Invitation to Applied Category Theory.* Cambridge University Press, 2019. —
Resource theories (Chapter 2) and string diagrams for symmetric monoidal
categories; direct foundation for the palgebra formalism.

**Fong, Brendan.** *The Algebra of Open and Interconnected Systems.* PhD thesis,
University of Oxford, 2016. — Decorated cospans (Ch. 2): a cospan
`A → N ← B` with a decoration on the apex N drawn from a symmetric monoidal
functor `F : Cospan → Set`. Composition is by pushout of the cospan legs,
which determines how decorations compose. The palgebra's pipeline wiring —
connecting operations by matching output types to input types — instantiates
this construction, with provenance and confidence annotations as the
decorations. §5 (coproduct injections) and §7 (resolution as pushout) are the
specific sites where Fong's pushout composition appears.

**Fritz, Tobias.** "A synthetic approach to Markov kernels, conditional
independence and theorems on sufficient statistics." *Advances in Mathematics*
370, 107239, 2020. arXiv:1908.07021. — Markov categories: the categorical
framework for stochastic maps. Definition 2.1 (Markov category), Corollary 3.2
(Kleisli categories of affine monads are Markov categories), Definition 10.1
(deterministic morphisms), Lemma 10.12 and Remark 10.13 (deterministic
subcategory is cartesian monoidal). The foundation for §2a of this document.

**Kelly, G. Maxwell.** *Basic Concepts of Enriched Category Theory.* Cambridge
University Press, 1982. — The foundation for enriched category theory.
Definition 1.2 (V-category): a collection of objects with V-valued
hom-objects, composition maps `M : Hom(B,C) ⊗ Hom(A,B) → Hom(A,C)`, and
identity elements `j_A : I → Hom(A,A)` satisfying associativity (eq. 1.3)
and unit coherence (eq. 1.4). §2b of this document verifies these four
conditions for V = ({Low, Medium, High}, min, High). Ch. 2.1 (V-valued
presheaves) provides the framework used in
[soft-type-theory.md](soft-type-theory.md) for graded type inhabitation.

**Baez, John, and Mike Stay.** "Physics, Topology, Logic and Computation: A
Rosetta Stone." In *New Structures for Physics*, ed. B. Coecke. Springer, 2011.
— String diagrams as a unified language across physics, logic, and computation.

**Cho, Kenta, and Bart Jacobs.** "Disintegration and Bayesian inversion via
string diagrams." *Mathematical Structures in Computer Science* 29(7),
938–971, 2019. — Develops disintegration (decomposition of a joint
distribution into marginal and conditional) and Bayesian inversion within the
string diagram calculus for Markov categories. Directly applicable to the
distributional type membership question (§10, [soft-type-theory.md](soft-type-theory.md)):
the type assignment kernel is a conditional arising from Bayesian inversion of
the generative pipeline.

**Perrone, Paolo.** "Markov categories and entropy." *IEEE Transactions on
Information Theory* 70(3), 1666–1693, 2024. — Extends Fritz's Markov
category framework with functorial entropy measures that compose correctly
through morphism composition. The monotonicity result — entropy cannot
decrease through composition — is the information-theoretic counterpart of
the palgebra's confidence degradation rule (§2b). The min-lattice enrichment
tracks a coarse summary of what Perrone's framework tracks precisely.
See §9 for the connection to eigenform/residue entropy.

**Kock, Anders.** "Monads on symmetric monoidal closed categories." *Archiv
der Mathematik* 21, 1–10, 1970. — Commutative monads on symmetric monoidal
closed categories: the commutativity condition ensures the Kleisli category
inherits a symmetric monoidal structure. This is the prerequisite for Fritz's
Corollary 3.2 (Kleisli categories of commutative affine monads are Markov
categories). The Giry monad's commutativity — the Fubini theorem — is the
concrete instance. See §2a (Kleisli perspective).

**Heunen, Chris, Ohad Kammar, Sam Staton, and Hongseok Yang.** "A convenient
category for higher-order probability theory." *Proceedings of LICS 2017.* —
Quasi-Borel spaces: a cartesian closed category that supports a probability
monad without the pathologies of standard Borel spaces. A candidate ambient
category for making the Kleisli perspective on **Text** concrete (§2a):
quasi-Borel spaces handle the higher-order structure needed for
prompt-parametrised operations and yield a Markov category via the Kleisli
construction.

**De Wynter, Adrian, et al.** "On Meta-Prompting." arXiv:2312.06562, 2023. —
Category-theoretic framework for LLM interactions; models prompt-response pairs
as morphisms and proves equivalence results for meta-prompting strategies.
