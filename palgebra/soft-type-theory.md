# Soft Type Theory

*A formal treatment of the soft type system, developing graded type
inhabitation as quantale-valued presheaves and extending to distributional
type membership.*

---

## 1. Motivation

The palgebra's soft type system, introduced informally in
[reference.md](reference.md) and used throughout the pipeline formalism,
assigns types to artifacts *to a degree*. A `(template, rubric)` pair defines
a type: the template specifies structural requirements, the rubric evaluates
semantic quality, and the resulting scores determine how well an artifact
inhabits the type. This section develops the mathematical structure behind
that intuition.

Three questions motivate the formalisation:

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

## 6. Open questions

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

**Sheaf condition.** The presheaf of §2 (and its V_5-valued generalisation
in §5) is not yet a *sheaf*. A sheaf condition would say: if an artifact's
type grades are locally consistent (compatible on every overlap of
refinement chains), then they extend to a globally consistent type profile.
Whether the rubric system satisfies this gluing condition — and whether
enforcing it would improve pipeline reliability — is an open question with
practical consequences for rubric design. In the vector setting, the sheaf
condition is componentwise: consistency must hold for each criterion
independently. This may be easier to verify (or falsify) than the scalar
case, since individual criteria are more constrained.
*Proposed treatment:* [soft-type-theory-v2.md, §7](soft-type-theory-v2.md)
(pending independent review).

**Curry-Howard for soft types.** Is there a proof theory for the soft type
system? In classical type theory, types are propositions and programs are
proofs. In the soft type system, types are graded — so proofs would be
graded too. This connects to the quantitative type theories of Atkey (2018)
and the graded monads of Gaboardi et al. (2016). Whether a useful
correspondence exists for pipeline operations is unexplored.

**Coend construction for untagged mixed-type texts.** The diary entry
identifies the coend as the canonical tool for eliminating a "dummy
variable" of type decomposition: when a text's decomposition into component
types must be *inferred* rather than declared, the coend integrates over
all possible decompositions. Formally, for types A and B with a common
sub-structure, the coend `∫^C Hom(C,A) × Hom(C,B)` characterises the
space of texts that could be decomposed as either A or B. This would
formalise how the pipeline handles texts whose type membership is
distributional (§4) but whose decomposition is unknown — connecting the
distributional type assignment μ_a ∈ Prob(T) to the categorical
machinery for weighted colimits in enriched categories (Kelly, Ch. 3.10).
*Proposed treatment:* [soft-type-theory-v2.md, §6](soft-type-theory-v2.md)
(pending independent review).

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

---

## References

**Fritz, Tobias.** "A synthetic approach to Markov kernels, conditional
independence and theorems on sufficient statistics." *Advances in
Mathematics* 370, 107239, 2020. arXiv:1908.07021. — Markov categories,
deterministic morphisms (Definition 10.1), Giry monad connection
(Corollary 3.2).

**Kelly, G. Maxwell.** *Basic Concepts of Enriched Category Theory.*
Cambridge University Press, 1982. — Enrichment axioms (Ch. 1.2),
V-valued presheaves (Ch. 2.1), quantale enrichment.

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
