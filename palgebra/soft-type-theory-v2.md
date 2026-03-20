# Soft Type Theory (v2 — extended treatment, pending independent mathematical review)

*A formal treatment of the soft type system, developing graded type
inhabitation as quantale-valued presheaves and extending to distributional
type membership, with full treatments of the product quantale, the coend
construction for untagged mixed-type texts, and the sheaf condition.*

*Status: §§1–5 share content with the canonical `soft-type-theory.md`.
§§6–7 are new formal developments that have not yet received independent
mathematical review. See the deliberation record at
`../situations/soft-type-extension/deliberations/` for the committee's
conditional adoption decision and the specific claims flagged for review.*

---

## 1. Motivation

The palgebra's soft type system, introduced informally in
[reference.md](reference.md) and used throughout the pipeline formalism,
assigns types to artifacts *to a degree*. A `(template, rubric)` pair defines
a type: the template specifies structural requirements, the rubric evaluates
semantic quality, and the resulting scores determine how well an artifact
inhabits the type. This section develops the mathematical structure behind
that intuition.

Six questions motivate the formalisation:

1. **What kind of mathematical object is a soft type?** The answer in §2 is:
   a quantale-valued presheaf. The template defines the presheaf's support,
   and the rubric defines the membership grades.

2. **How does graded type inhabitation compose through the pipeline?** The
   answer in §3 connects the presheaf structure to the enriched category
   **Text** over V (§2b of [categorical-structures.md](categorical-structures.md)):
   morphisms respect the grading, and the min-lattice propagation rule
   follows from the enrichment axioms.

3. **What happens when a text genuinely inhabits multiple types?** The
   answer in §4 extends from graded single-type membership to distributional
   membership across type-space — the "furry logic" extension sketched in
   [the diary entry](../wild/diary/2026-03-13-furry-logic.md). This is the
   novel contribution: type membership becomes a measure on type-space,
   connecting directly to Fritz's Markov category framework.

4. **What structure do the rubric scores themselves carry?** The answer in
   §5 develops the product quantale V_5 for vector-valued rubric scores,
   with a collapse functor mediating between rich internal tracking and
   coarse pipeline-boundary decisions.

5. **How does the pipeline compute when type decomposition is unknown?**
   The answer in §6 introduces the coend construction for integrating over
   latent type decompositions, connecting distributional type membership to
   soft routing as an alternative to hard MAP estimation.

6. **Are the type grades globally consistent?** The answer in §7 analyses
   the sheaf condition on the type lattice, conjecturing that the
   measurement framing generically prevents sheaf structure and identifying
   restricted settings where consistency holds.

---

## 2. Soft types as quantale-valued presheaves

### The type lattice

Let **T** be the category of soft types. Objects are `(template, rubric)`
pairs. A morphism `τ : A → B` in **T** exists when type B *refines* type A —
every artifact that inhabits B also inhabits A (possibly at a lower grade).
Refinement is transitive and reflexive, making **T** a preorder.

Examples: `evidence` refines `text` (every evidence artifact is a text).
`scored-evidence` refines `evidence` (scored evidence has additional
metadata structure). The refinement order tracks the template inclusion
hierarchy.

### The enrichment base as quantale

The enrichment base V = ({Low, Medium, High}, min, High) from §2b of
[categorical-structures.md](categorical-structures.md) is a commutative
quantale: a complete lattice in which the monoidal product (min) distributes
over arbitrary joins (max). Being a commutative quantale, V is also a
*monoidal closed* category — it has an internal hom given by the residuation:

```
(a → b) = max { c ∈ V | min(a, c) ≤ b }
```

For our three-element lattice, this is the implication of Heyting algebra:
`(Low → x) = High` for all x, `(Medium → Low) = Low`,
`(Medium → Medium) = High`, etc. The quantale structure is what makes V
a valid base for both enrichment (Kelly, Ch. 1.2) and for the presheaf
construction below.

### The presheaf

A **V-valued presheaf** on **T** is a functor:

```
F : T^op → V
```

It assigns to each soft type A a confidence grade `F(A) ∈ V`, subject to the
functoriality condition: if `τ : A → B` is a refinement (B is more
specialised than A), then `F(A) ≥ F(B)`. Inhabiting a more specialised type
at the same grade as a more general type is possible but not guaranteed.

**Interpretation.** A V-valued presheaf on **T** is exactly a *graded type
assignment* for a single artifact. The functor F says: "this artifact
inhabits type A at grade F(A), type B at grade F(B), and these grades are
compatible with the refinement order."

The collection of all V-valued presheaves on **T** is a category, written
**[T^op, V]**. This is the *soft type space* — each point in it is a
possible graded type profile for an artifact.

### Connecting to the pipeline

An artifact `a = (text, metadata)` in the pipeline determines a presheaf
`F_a : T^op → V` by evaluation: for each soft type A = (template, rubric),

```
F_a(A) = rubric_A(a)
```

where `rubric_A(a)` is the confidence band that the rubric assigns to the
artifact. This is the *measurement* interpretation from
[the diary entry](../wild/diary/2026-03-13-furry-logic.md): the type is
not an intrinsic property of the artifact but the result of applying the
rubric instrument.

Functoriality of F_a follows from the design of rubrics: if type B refines
type A, then the rubric for B is at least as demanding as the rubric for A,
so `F_a(A) ≥ F_a(B)`.

### What this gives us

The presheaf formulation makes three informal properties precise:

**Graded inhabitation is compositional.** The V-valued presheaves form a
category enriched over V — the hom-objects are confidence grades, and
composition uses the min-lattice. This is the same enrichment structure as
§2b of [categorical-structures.md](categorical-structures.md), now applied
to the type assignments themselves rather than to the pipeline morphisms.

**Template and rubric have distinct roles.** The template determines which
presheaves have non-trivial support (which types the artifact could
potentially inhabit). The rubric determines the grades within that support.
In the presheaf picture: the template is the *support* of the functor, and
the rubric is the *weighting* on that support.

**Refinement is functorial.** The refinement order on types is not an
afterthought — it is the categorical structure that the presheaf must
respect. Adding a new type to the hierarchy (say, `security-evidence`
refining `evidence`) automatically constrains how existing artifacts'
grades relate to the new type.

---

## 3. Morphisms and confidence propagation

### Pipeline operations on type profiles

A pipeline morphism `f : A → B` in **Text** transforms artifacts, changing
their type profiles. In the presheaf picture, f induces a map on type
profiles:

```
f* : [T^op, V] → [T^op, V]
```

If artifact a has type profile F_a, then the output `f(a)` has type profile
F_{f(a)}, and the relationship between them is constrained by the enriched
composition law (§2b):

```
F_{f(a)}(B) ≤ min(confidence(f), F_a(A))
```

The output cannot inhabit its target type at a grade higher than the minimum
of: the morphism's own confidence, and the input's inhabitation grade. This
is the monotone confidence degradation rule, now derived from the presheaf
structure rather than stated as an axiom.

### Enrichments preserve type profiles

Enrichment morphisms (deterministic morphisms in Layer 1 of §2c) operate at
confidence High. Their effect on type profiles is:

```
F_{e(a)}(B) = min(High, F_a(A)) = F_a(A)
```

Enrichments cannot change an artifact's type profile — they only update
metadata. This is precisely the statement that enrichments are deterministic
morphisms (Fritz, Definition 10.1): they respect the copy structure, and in
the presheaf picture this means they preserve the type assignment.

### Transformations may shift type profiles

Transformation morphisms (genuinely stochastic, Layer 2) can produce outputs
whose type profiles differ from the inputs'. The Deliberate morphism takes
a charter-typed input and produces a transcript-typed output. In the
presheaf picture, the output presheaf has support concentrated on
`transcript` and its refinements, not on `charter`.

The stochastic nature of transformations means the output type profile is
itself a random variable. Running Deliberate twice on the same charter
produces two transcripts with potentially different rubric scores —
different type profiles. The distribution over type profiles is determined
by the Markov kernel of the transformation.

---

## 4. The distributional extension: furry logic

### The problem with graded single-type membership

The presheaf picture of §2 assigns a grade to each type independently. A
text has grade High for `evidence` and grade Medium for `argument`. But
these grades are not the full story. Two texts might both score
Medium for `evidence`, but one is uniformly mediocre evidence while the
other is excellent evidence in some respects and poor in others. The scalar
grade collapses this distinction.

More fundamentally: a text can genuinely span multiple types in ways that
are not captured by independent scores. A committee transcript that
contains both deliberation and the resulting resolution is not 0.5
transcript and 0.5 resolution — it is both, fully, along different axes.
The scores along these axes are not independent; they are coupled by the
text's internal structure.

### Type membership as measure

The distributional extension replaces the scalar-valued presheaf with a
*measure-valued* assignment. Instead of:

```
F_a : T^op → V                    (graded: one grade per type)
```

we write:

```
μ_a : T^op → Prob(V)              (distributional: a distribution over grades per type)
```

But the more consequential move is to treat the *type itself* as a random
variable. Instead of asking "at what grade does this text inhabit type A?",
we ask "what is the distribution of this text's type across type-space?"

```
μ_a ∈ Prob(T)                     (distributional type membership)
```

Single-type texts are delta functions: `μ_a = δ_evidence`. Fuzzy membership
is a smeared delta. Texts that genuinely span two types are bimodal
distributions.

This is the "furry logic" of the
[diary entry](../wild/diary/2026-03-13-furry-logic.md): to fuzzy logic as a
probability distribution is to a point estimate.

### Connection to the Markov category framework

The distributional extension connects directly to Fritz's framework. The
assignment `a ↦ μ_a` is a *Markov kernel* from the space of artifacts to
the space of types:

```
τ : Artifacts → Prob(T)
```

This is a morphism in the category of Markov kernels (Fritz, Example 2.5).
Composition of pipeline operations then acts on type assignments via the
Chapman–Kolmogorov equation: if `f : A → B` is a pipeline morphism with
Markov kernel `k_f`, then the type assignment of the output is:

```
μ_{f(a)}(B) = ∫ k_f(a, db) · τ(b, B)
```

The integral is the convolution of the pipeline's stochastic map with the
type assignment map — the distributional type of the output is determined
by the distribution over outputs and the type profile of each possible
output.

When the pipeline morphism is deterministic (an enrichment), the kernel
`k_f` is a delta function and the integral collapses:
`μ_{f(a)} = τ(f(a))`. The type profile is simply evaluated at the
deterministic output. This recovers the enrichment-preserves-type-profiles
result from §3.

### The Giry monad perspective

The Giry monad `G` sends a measurable space X to the space of probability
measures `G(X) = Prob(X)`. Fritz (Corollary 3.2) shows that the Kleisli
category of the Giry monad is a Markov category. The distributional type
assignment `τ : Artifacts → G(T)` is a Kleisli arrow of G.

This makes the connection to the three-layer architecture (§2c of
[categorical-structures.md](categorical-structures.md)) precise:

- **Layer 1 (Text_det)**: Type assignments are deterministic —
  `τ(a) = δ_{type(a)}`. Each artifact has a definite type. The presheaf
  picture of §2 lives here (with grades refining the delta to a weighted
  delta).
- **Layer 2 (Text)**: Type assignments are Markov kernels. The
  distributional type membership is a morphism in the Markov category.
  Pipeline operations compose with type assignments via Chapman–Kolmogorov.
- **Layer 3 (Text enriched over V)**: The confidence enrichment interacts
  with distributional types through the expected grade:
  `confidence(μ_a, A) = E_{μ_a}[grade(A)]`, collapsing the distribution
  to a scalar for the min-lattice propagation.

### Routing as decision under distributional type uncertainty

The operational consequence of distributional type membership is for
pipeline routing. When an artifact's type is a distribution rather than a
point, routing becomes a decision under uncertainty:

```
route : Prob(T) → T
```

This is a MAP (maximum a posteriori) estimator: commit to the type with
highest probability mass. The distribution `μ_a` is the thing you are
betting with; the route is the bet.

The furry logic framing makes explicit what is implicit in every
classification pipeline: routing always involves a bet, and the quality of
the bet depends on the shape of the type distribution. A unimodal
distribution (one dominant type) is a safe bet. A bimodal distribution (two
competing types) is a risky bet that might warrant splitting the artifact
or flagging for human review.

This connects to the Probe (§9 of
[categorical-structures.md](categorical-structures.md)): multimodality in
the Probe's output is evidence that the pipeline's routing decisions are
operating in a high-uncertainty regime.

---

## 5. Vector scores and the product quantale

### The problem with scalar confidence

Sections 2–4 work with the scalar enrichment base
V = ({Low, Medium, High}, min, High). This captures pipeline-level
confidence but discards the structure that rubric evaluation actually
produces. An evaluation rubric scores five criteria — reasoning
completeness, adversarial rigor, assumption surfacing, evidence standards,
trade-off explicitness — each on a 0–3 scale. The scalar confidence band
is derived from these (typically as a threshold on the aggregate), but the
derivation is lossy: two transcripts both scoring Medium overall may have
very different score profiles — one uniformly mediocre, the other excellent
on evidence but poor on adversarial rigor.

The presheaf picture of §2 needs a richer base to track this structure.

### The product quantale

Let W = [0,3] with the usual order, min as monoidal product, and 3 as
unit. W is a commutative quantale (a complete lattice with min distributing
over arbitrary joins). The **product quantale** is:

```
V_5 = (W^5, componentwise min, (3,3,3,3,3))
```

where the order on W^5 is componentwise: `(a₁,...,a₅) ≤ (b₁,...,b₅)` iff
`aᵢ ≤ bᵢ` for all i. The monoidal product is componentwise min:
`(a₁,...,a₅) ⊗ (b₁,...,b₅) = (min(a₁,b₁),...,min(a₅,b₅))`. The unit is
`(3,3,3,3,3)`.

V_5 is again a commutative quantale. The argument is component-by-component:
W is a commutative quantale, and the product of commutative quantales
(with componentwise operations) is a commutative quantale. Monoidal
closure carries over: the internal hom in V_5 is componentwise residuation,
`(a → b)ᵢ = max { c ∈ W | min(aᵢ, c) ≤ bᵢ }`. (This follows from the
general fact that finite products of quantales are quantales — see e.g.
Rosenthal, *Quantales and their Applications*, Proposition 1.2.2, applied
componentwise.)

### Vector-valued presheaves

A **V_5-valued presheaf** on the type lattice **T** is a functor:

```
F : T^op → V_5
```

It assigns to each soft type A a vector of criterion scores
`F(A) = (s₁,...,s₅) ∈ V_5`, subject to the same functoriality condition
as §2: if `τ : A → B` is a refinement (B more specialised than A), then
`F(A) ≥ F(B)` componentwise.

**Interpretation.** Where the scalar presheaf of §2 says "this artifact
inhabits type A at confidence Medium," the vector presheaf says "this
artifact inhabits type A with reasoning-completeness 2, adversarial-rigor
1, assumption-surfacing 3, evidence-standards 2, trade-off-explicitness 2."
The full rubric profile is preserved, not collapsed.

The collection of V_5-valued presheaves on **T** is the enriched presheaf
category **[T^op, V_5]** — a richer soft type space in which each point is
a full rubric-profile assignment across types.

### Confidence propagation with vector scores

The confidence degradation rule of §3 generalises componentwise. If
`f : A → B` is a pipeline morphism with confidence vector
`conf(f) ∈ V_5`, then:

```
F_{f(a)}(B) ≤ componentwise-min(conf(f), F_a(A))
```

Each criterion degrades independently. A morphism with high evidence-
standards confidence but low adversarial-rigor confidence degrades
those criteria at different rates. This is more informative than the
scalar rule: it tells you *where* in the quality profile the degradation
is worst.

### The collapse functor

At pipeline boundaries — human gates, final deliverables, routing
decisions — the vector score must collapse to a scalar decision. This
collapse is a functor:

```
collapse : V_5 → V
```

where V is the three-element scalar confidence lattice {Low, Medium, High}
from §2. The standard collapse is a threshold on the aggregate:

```
collapse(s₁,...,s₅) = High   if sum(sᵢ) ≥ 13
                       Medium if sum(sᵢ) ≥ 8
                       Low    otherwise
```

This is an oplax monoidal functor from (V_5, componentwise-min) to (V, min).
It is *oplax* rather than strict because collapsing respects the order
(if `v ≤ w` componentwise then `collapse(v) ≤ collapse(w)`) but does not
strictly preserve the monoidal product — the collapse of a componentwise
min may fall strictly below the min of the collapses. Concretely: two
vectors might each collapse to Medium, but their componentwise min might
collapse to Low (if each vector's weak criterion is different and the
mins accumulate).

The oplaxness is a genuine feature, not a defect. It records the fact that
pipeline-boundary decisions are necessarily coarser than the internal
quality tracking. The category **Text** is enriched over V_5 internally,
and enriched over V at its boundaries. The collapse functor mediates
between the two enrichment bases.

**Connection to decorated texts.** The collapse functor is the formal
counterpart of the "score combination structures" in
[decorated-texts.md](decorated-texts.md) (§ Score combination structures),
which describes lattice, semiring, and Pareto combination strategies. The
min-lattice collapse is the lattice case. A semiring collapse (weighted
sum) or a Pareto collapse (preserve the frontier) would be alternative
functors from V_5 to different scalar bases, each oplax monoidal with
different oplaxness properties. The choice of collapse functor is a design
decision with operational consequences — it determines what information
survives at pipeline boundaries.

### The distributional extension with vector scores

The distributional extension of §4 generalises to the vector setting.
The distributional type membership becomes:

```
μ_a ∈ Prob(T)    with grades in V_5 rather than V
```

More precisely, the combined distributional-vector type assignment is a
Markov kernel:

```
τ : Artifacts → Prob(T × V_5)
```

assigning to each artifact a joint distribution over types and score
profiles. The Chapman–Kolmogorov composition from §4 carries through with
V_5 replacing V: the output's joint type-score distribution is the
convolution of the pipeline morphism's kernel with the input's joint
distribution.

The collapse functor then acts on the V_5 component, marginalising the
score profile to a scalar confidence for routing decisions. The full
joint distribution is preserved in the artifact's metadata (the YAML
front-matter scores); the collapsed scalar is what the pipeline's routing
logic uses. This two-level structure — rich internal tracking, coarse
boundary decisions — mirrors the architecture of the human gates described
in [decorated-texts.md](decorated-texts.md): the human reviewer sees the
full score vector but produces a binary proceed/halt decision.

### What this buys

The product quantale treatment makes three things precise:

**Independent criterion degradation.** The scalar rule says confidence
degrades through the pipeline. The vector rule says *which criteria*
degrade and by how much. This is actionable: if evidence-standards
consistently degrades but adversarial-rigor holds, the pipeline designer
knows where to invest effort.

**Collapse is a design choice, not a mathematical necessity.** The scalar
V of §2 is not the "real" enrichment base — it is the image of a chosen
collapse functor. Different collapse functors (different aggregation
strategies) yield different pipeline behaviors at the boundaries. Making
this explicit opens the door to principled comparison of scoring
strategies, which the open games work
([committee-as-open-game.md](../wild/committee-games/committee-as-open-game.md),
§4) frames as mechanism design: the collapse functor is part of the
continuation function k that determines equilibrium behavior.

**The vector presheaf is the natural home for rubric data.** The YAML
front-matter scores (five criteria, each 0–3) are literally elements of
V_5. The metadata format in
[reference.md](reference.md) is already storing V_5-valued type
assignments; the product quantale treatment gives that storage a formal
semantics.

---

## 6. The coend construction: computing with unknown type decompositions

### The problem

Section 4 introduces distributional type membership: a text's type is a
measure μ_a ∈ Prob(T) rather than a point. But it leaves open how the
pipeline should *compute* with this distribution when the type decomposition
is not observed. A committee transcript that spans both `deliberation` and
`resolution` types has a bimodal type distribution — but the pipeline
cannot directly observe the decomposition. It sees the text as a whole;
the internal structure that makes part of it deliberative and part of it
resolutional is latent.

The categorical tool for this situation is the **coend**: it integrates
over all possible decompositions, producing a result that is independent
of which decomposition is the "right" one.

### Coends in the enriched setting

In a V-enriched category **C**, the **coend** of a functor
`H : C^op × C → V` is a V-object written:

```
∫^X H(X, X)
```

defined by the universal property (Kelly, Ch. 3.10, Definition 3.69):
it is the universal V-object receiving a *dinatural transformation* from H.
Concretely, the coend is the coequaliser of:

```
∐_{f : X → Y} H(Y, X) ⇉ ∐_X H(X, X)
```

where the two maps are induced by H's covariant and contravariant
actions on f. The coend "quotients out" the dependency on the
intermediate variable — it identifies all the ways of decomposing through
different intermediate types.

**Intuition.** If H(A, B) measures "how well does this text look as an
A-component when viewed from the B-perspective," then the coend ∫^C H(C, C)
aggregates over all possible decomposition types C, producing a single
grade that does not depend on which C was chosen. It is the categorical
analogue of marginalisation in probability: sum over the latent variable.

### Application to mixed-type texts

For a text a that spans types A and B, define the bifunctor:

```
H_a : T^op × T → V_5
```

```
H_a(X, Y) = F_a(X) ⊗ Hom_T(Y, X)
```

where F_a is the V_5-valued presheaf of a (§5), ⊗ is the monoidal
product in V_5 (componentwise min), and Hom_T(Y, X) is the V_5-enriched
hom in the type lattice (the degree to which Y refines X).

The coend:

```
∫^C F_a(C) ⊗ Hom_T(C, C) = ∫^C F_a(C)
```

simplifies because Hom_T(C, C) = (3,3,3,3,3) (the identity refinement
is maximal). So the coend reduces to the colimit of F_a over T.

In V_5 (a complete lattice), the colimit is the join — the componentwise
supremum of all F_a(C) values. For a presheaf satisfying the
functoriality condition (grades decrease along refinement), the supremum
is achieved at the least refined (most general) type. The coend therefore
returns F_a evaluated at the top of the type lattice. This is
mathematically correct but computationally trivial: the coend does not
aggregate information from multiple types in a non-trivial way.

The coend's value lies not in the *number* it computes but in the
*universal property* it satisfies. By Kelly (Ch. 3.10, Definition 3.69),
the coend is characterised by the property that any family of V_5-morphisms
`H(C, C) → X` that is dinatural in C factors uniquely through the coend.
In the type-theoretic setting, this means: any construction that processes
an artifact in a way that does not depend on which type decomposition is
chosen is canonically determined by the coend. The coend is a *coherence
guarantee* — it identifies the type-decomposition-independent part of the
pipeline's computations.

### Two formalisations of marginalisation

The coend and the distributional type assignment of §4 both formalise the
intuition of "marginalising over the latent type variable," but they are
different constructions that give different answers in general.

**The categorical construction (coend).** The coend ∫^C F_a(C) in V_5
computes a join — a supremum over the monoidal structure (V_5, min). For
a presheaf on a bounded preorder, this is the value at the most general
type. Its contribution is the universal property (structural guarantee),
not the computed value.

**The probabilistic construction (expectation).** The distributional type
assignment `τ : Artifacts → Prob(T)` from §4 gives a probability measure
μ_a over types. The expected score profile is:

```
E_{μ_a}[F_a] = ∫_T μ_a(dC) · F_a(C)
```

This is a weighted average over the score profiles, using addition and
multiplication in ℝ^5. It is a different operation from the coend's join:
the coend operates in (V_5, min), the expectation operates in (ℝ^5, +, ·).
For a delta measure μ_a = δ_t (single-type text), the expectation
returns F_a(t); this equals the coend — which is always F_a at the most
general type — only when t is itself the most general type.

**Why both matter.** The coend provides structural guarantees (any
type-decomposition-independent construction factors through it). The
expectation provides a computational tool (a single aggregate score
profile for routing). A future treatment might unify them by working in
a semiring-enriched setting where the coend computes a weighted sum
rather than a supremum, but this would require reworking the enrichment
base throughout the document and is left as an open question.

**Connection to routing.** The routing decision of §4 (route : Prob(T) → T)
commits to a single type via MAP estimation. The expectation provides
a "soft routing" alternative: instead of committing, compute the expected
quality profile across all types and use that for downstream processing.
This is analogous to the difference between hard and soft attention in
neural architectures. Whether soft routing improves pipeline quality is
an empirical question. The coend's universal property provides a separate
guarantee: any soft router satisfying the dinaturality condition factors
canonically through the coend (see §8, open questions).

**Connection to the Probe.** The Probe (§9 of
[categorical-structures.md](categorical-structures.md)) runs the pipeline
N times to characterise the distribution over outputs. The expectation-based
type inference can be applied to each Probe run, producing N
expected-score profiles. The variance of these profiles across runs
measures how sensitive the type inference is to the pipeline's
stochasticity — a second-order uncertainty measure that the scalar
routing decision of §4 obscures.

### What the coend does not resolve

The coend construction assumes the presheaf F_a is already known — that
is, the artifact has been scored against all types in T. In practice,
scoring is expensive (each type requires a rubric evaluation), and T
may be large. The coend computes the right answer given complete data;
it does not address the data acquisition problem. An efficient
approximation would score against a small subset of T and estimate the
coend from the partial presheaf. Whether this approximation is reliable
depends on the structure of T (specifically, on how much information the
refinement order provides about unscored types). This is an open
question with operational consequences for pipeline design.

The coend also requires the enrichment base V_5 to support the
coequaliser construction. For the product quantale V_5, coequalisers
exist because V_5 is cocomplete as a lattice (arbitrary joins exist).
The coend is then well-defined as a specific join in V_5. This would
not hold for all enrichment bases — it is a consequence of the quantale
structure.

---

## 7. The sheaf condition: local-to-global consistency of type grades

### Motivation

The presheaf F_a : T^op → V_5 of §§2 and 5 assigns grades to types
subject only to the functoriality constraint (grades decrease along
refinement). This is a weak condition: it says nothing about whether
the grades are *consistent* across different refinement chains. Two
independent paths through the type lattice might assign the same
artifact conflicting grades at a common sub-type — the presheaf permits
this as long as each path individually respects the order.

A **sheaf condition** would strengthen the presheaf to require
local-to-global consistency: if an artifact's grades are compatible on
every overlap of refinement chains, they extend to a unique globally
consistent assignment. This is the "gluing" property that turns a
presheaf into a sheaf.

### The sheaf condition on T

The type lattice T, as a preorder, has a natural Grothendieck topology:
the *canonical topology* generated by covering families. For a preorder,
the relevant covers are the *jointly surjective refinement families*:
a type A is covered by types {B₁, ..., Bₙ} if every artifact that
inhabits A also inhabits some Bᵢ. (This semantic characterisation is
equivalent to the categorical one — the sieve generated by the Bᵢ is a
covering sieve for the canonical topology — because the refinement order
on T is defined in terms of inhabitation containment: B refines A
precisely when every B-artifact is an A-artifact, per §2.)

The sheaf condition for F_a on this topology says: if F_a is defined on
each Bᵢ and the values agree on overlaps (types that refine two or more
Bᵢ simultaneously), then F_a extends uniquely to A.

```
Sheaf condition: For every cover {B₁,...,Bₙ} of A in T,
if F_a(Bᵢ) and F_a(Bⱼ) agree on Bᵢ ∩ Bⱼ (the infimum in T)
for all i,j, then there exists a unique F_a(A) compatible with all Bᵢ.
```

In the vector setting (V_5-valued presheaves), "agree on overlaps"
means componentwise agreement at the overlap types. The condition is
checkable criterion by criterion.

### Does the rubric system satisfy the sheaf condition?

This is an empirical question with a likely negative answer. Here is the
argument for skepticism:

Consider three types: `text` (general), `evidence` (refines text), and
`argument` (refines text). The overlap `evidence ∩ argument` in the
type lattice is the infimum — the most refined type that both evidence
and argument refine. For many type lattices this infimum is `text`
itself (evidence and argument may have no common specialisation).

The sheaf condition would require: if an artifact scores (2,3,1,2,2)
as evidence and (3,1,2,1,3) as argument, and these are compatible at
`text` (which they must be, since both are ≤ the text grade), then
the text grade is uniquely determined. But the text grade is determined
by its own rubric, which may produce (2,2,2,2,2) — consistent with
both but not determined by them.

The problem is that rubric scores are *measurements*, not *deductions*.
The evidence rubric and the argument rubric measure different quality
dimensions. Their overlap at `text` does not constrain the text rubric's
output — the text rubric has its own criteria. The sheaf condition
requires that local measurements determine global assignments; the
measurement framing (§2, §4) says each rubric is an independent
instrument.

**Conjecture.** The presheaf F_a is generically *not* a sheaf on the
type lattice with the canonical topology. The failure is not a defect
of the rubric system but a consequence of the measurement framing:
independent instruments do not in general satisfy gluing conditions.

### When the sheaf condition does hold

There are restricted settings where the condition holds:

**Within a single refinement chain.** If types form a linear chain
(A₁ refines A₂ refines ... refines Aₙ), the sheaf condition is
trivially satisfied because there are no independent overlaps — every
cover is linearly ordered, and the presheaf values are already
determined by functoriality.

**When rubrics share criteria.** If two rubrics at the same level of
the type lattice share criteria (e.g., both `evidence` and `argument`
include "evidence-standards"), the shared criterion grades must agree
on any artifact. This gives a partial sheaf condition on the sub-quantale
corresponding to the shared criteria.

**When enforced by rubric design.** A rubric designer could choose to
make rubrics compositional: the text rubric's criteria are exactly the
union of the evidence and argument rubrics' criteria, with the text
grade on each criterion defined as the max of the sub-type grades.
This would force the sheaf condition by construction. Whether this
improves pipeline reliability or merely constrains rubric design
unnecessarily is a design question, not a mathematical one.

### Connection to mechanism design

The open games formalization
([committee-as-open-game.md](../wild/committee-games/committee-as-open-game.md),
§4) identifies the evaluation rubric as the continuation function k
that determines committee equilibrium. The sheaf condition is a
coherence constraint on k: it requires that the rubric system's
evaluations are globally consistent, not just locally consistent along
each refinement chain.

**Conjecture (sheaf-equilibrium connection).** If the sheaf condition
fails — if different rubrics can give inconsistent signals — then the
continuation function k becomes ambiguous at the overlaps, facing a
multi-objective optimisation problem rather than a scalar one.
Characters best-responding to inconsistent signals may produce
strategies that are locally rational but globally incoherent: a
non-sheaf rubric system permits committee equilibria that optimise
against different rubric perspectives without coordinating across them.
Deriving this rigorously would require showing that the composed open
game with inconsistent payoffs fails to have a Nash equilibrium or that
its equilibria are Pareto-dominated, which we have not attempted.

Whether this theoretical risk materialises in practice depends on
how much the rubric system's criteria overlap at different type
levels. The vector setting of §5 makes this checkable: compare
criterion-by-criterion grades across types and look for
inconsistencies at overlap points. This is a concrete diagnostic
that rubric designers can apply.

---

## 8. Open questions

Several questions remain for future development:

**Lawvere metric space interpretation.** Rubric scores can be read as
distances from perfect type inhabitation: `d(a, A) = 3 - rubric_A(a)`. The
triangle inequality `d(a, C) ≤ d(a, B) + d(B, C)` would express a
transitivity constraint on type refinement. Whether this holds for the
actual rubric scores is an empirical question — and whether a Lawvere
metric space gives a tighter characterisation than the quantale-valued
presheaf is an open comparison. With the vector treatment of §5, this
extends to a V_5-valued Lawvere metric, where the distance is a vector
and the triangle inequality holds componentwise.

**Probabilistic coherence spaces.** The template/rubric duality (structural
constraints vs. semantic evaluation) mirrors the web/coherence split in
Girard's coherence spaces. The presheaf of §2 is a "coherence" structure
(compatible assignment of grades), and the template is the "web"
(underlying set). Whether this analogy extends to a full probabilistic
coherence space (Danos & Ehrhard 2011) — with the pipeline's stochastic
maps as morphisms — is speculative but suggestive.

**Curry-Howard for soft types.** Is there a proof theory for the soft type
system? In classical type theory, types are propositions and programs are
proofs. In the soft type system, types are graded — so proofs would be
graded too. This connects to the quantitative type theories of Atkey (2018)
and the graded monads of Gaboardi et al. (2016). Whether a useful
correspondence exists for pipeline operations is unexplored.

**Sheaf condition: empirical validation.** Section 7 conjectures that the
presheaf is generically not a sheaf and identifies restricted settings
where the condition holds (linear chains, shared criteria, enforced by
rubric design). The next step is empirical: run a suite of rubric
evaluations across a type lattice, extract the overlap grades, and test
whether the sheaf condition holds or fails. The vector setting of §5 makes
this checkable criterion by criterion.

**Coend approximation for large type lattices.** Section 6's coend
construction assumes scoring against all types in T. For large T, this
is impractical. Whether the coend can be reliably approximated from a
sparse sub-lattice of T — and what the approximation error bounds are —
is an open question with direct operational implications for pipeline
routing efficiency.

**Soft routing vs. hard routing.** Section 6 introduces the coend-based
"soft routing" alternative to the MAP estimator of §4. Whether soft
routing improves pipeline quality (fewer misrouted artifacts, better
downstream scores) is an empirical question that could be tested in the
Probe framework (§9 of
[categorical-structures.md](categorical-structures.md)): compare hard-
and soft-routed versions of the same pipeline across N Probe runs.

**Connection to Gärdenfors' conceptual spaces.** The distributional type
membership of §4 has a geometric interpretation: convex regions in a
conceptual space (Gärdenfors 2000) correspond to natural types, and the
type distribution μ_a describes an artifact's position relative to these
regions. This would provide an alternative intuition for readers who think
geometrically rather than categorically. The V_5 score vector of §5 is
already a point in a 5-dimensional space; the connection to Gärdenfors
would ask whether the natural types (the soft types of §2) correspond to
convex regions in this space — and whether the presheaf functoriality
condition (grades decrease along refinement) has a geometric counterpart
in the containment of convex regions.

**Interaction between coend and sheaf condition.** The coend (§6) and the
sheaf condition (§7) are related but distinct. The coend marginalises over
type decompositions; the sheaf condition constrains whether local type
grades extend globally. If the presheaf is a sheaf, the coend computation
simplifies (local data determines global data, so the coend can be computed
from any sufficiently fine cover). If it is not a sheaf, the coend must
account for the inconsistencies — the "soft routing" of §6 may
systematically disagree with hard routing at the inconsistency points.
The interaction between these constructions is unexplored.

**Soft routing and dinaturality.** The "soft routing" alternative to MAP
estimation (§6) assigns processing weights to pipeline branches without
committing to a single type. A natural question is whether soft routers
satisfy the dinaturality condition required to factor through the coend.
For a linear router (weights are the presheaf values), dinaturality
follows from presheaf functoriality. For nonlinear routers, it is an
additional constraint. If the dinaturality condition holds, the coend's
universal property (Kelly 3.10, Definition 3.69) guarantees that the
router has a canonical factorisation — providing a formal basis for
comparing different soft routing strategies.

**Empirical test of the sheaf-equilibrium conjecture.** The conjecture
in §7 connecting sheaf failure to committee equilibrium incoherence has a
testable prediction: if rubric inconsistencies at type overlaps
(checkable via §5's vector scores) correlate with lower evaluation scores
in committee deliberations (checkable via the evaluation rubrics), the
conjecture gains empirical support. A systematic study would measure
rubric overlap grades across a type lattice and correlate the degree of
sheaf-condition failure with deliberation quality outcomes.

---

## References

**Fritz, Tobias.** "A synthetic approach to Markov kernels, conditional
independence and theorems on sufficient statistics." *Advances in
Mathematics* 370, 107239, 2020. arXiv:1908.07021. — Markov categories,
deterministic morphisms (Definition 10.1), Giry monad connection
(Corollary 3.2).

**Kelly, G. Maxwell.** *Basic Concepts of Enriched Category Theory.*
Cambridge University Press, 1982. — Enrichment axioms (Ch. 1.2),
V-valued presheaves (Ch. 2.1), quantale enrichment, coend definition and
universal property (Ch. 3.10, Definition 3.69).

**Lawvere, F. William.** "Metric spaces, generalized logic, and closed
categories." *Rendiconti del Seminario Matematico e Fisico di Milano* 43,
135–166, 1973. — Lawvere metric spaces as enriched categories.

**Atkey, Robert.** "Syntax and Semantics of Quantitative Type Theory."
*Proceedings of LICS 2018.* — Graded types and resource tracking.

**Cho, Kenta, and Bart Jacobs.** "Disintegration and Bayesian inversion
via string diagrams." *Mathematical Structures in Computer Science*
29(7), 938–971, 2019. — Bayesian inversion in Markov categories.
The type assignment kernel `τ : Artifacts → Prob(T)` is a conditional
arising from disintegration of the joint distribution over (text, type)
pairs.

**Perrone, Paolo.** "Markov categories and entropy." *IEEE Transactions
on Information Theory* 70(3), 1666–1693, 2024. — Functorial entropy
on Markov categories. The confidence degradation rule is a coarse
instance of Perrone's monotonicity result.

**Kock, Anders.** "Monads on symmetric monoidal closed categories."
*Archiv der Mathematik* 21, 1–10, 1970. — Commutative monads,
prerequisite for the Giry monad connection (§4).

**Rosenthal, Kimmo I.** *Quantales and their Applications.* Pitman
Research Notes in Mathematics 234, Longman, 1990. — Proposition 1.2.2:
finite products of quantales are quantales with componentwise operations.
Used in §5 for the product quantale V_5.

**Danos, Vincent, and Thomas Ehrhard.** "Probabilistic coherence spaces
as a model of higher-order probabilistic computation." *Information and
Computation* 209(6), 966–991, 2011. — Probabilistic coherence spaces.
