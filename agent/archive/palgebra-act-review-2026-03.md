# Committee Review: Palgebra for Applied Category Theorists

**Date**: 2026-03-13
**Status**: All findings addressed by remediation plan (Phases 1–6, complete 2026-03-13). Archived.
**Prompt**: `agent/prompts/act-review-palgebra.md`
**Scope**: All files in `palgebra/`, plus wild documents `potential-to-sense`, `committee-games`, `furry-logic`
**Panel**: Maya, Frankie, Joe, Vic, Tammy — propensities applied to mathematical review

---

## Charter

Assess how well the palgebra directory will land with applied category theorists.
Classify every categorical claim by warrant level. Identify what is new, what is
borrowed, and what is overclaimed. Recommend how to fill the mathematical gaps
and where to extend.

---

## Opening Statements

**Vic** (Evidence Prosecutor): I read six documents totalling ~2,500 lines that
invoke products, coproducts, equalizers, pullbacks, pushouts, Kleisli categories,
enriched categories, monads, Frobenius structures, traced monoidal categories,
and decorated cospans. The word "precisely" appears alongside constructions whose
definitions have not been given. My job today is simple: for each claim, either
show me the definition, show me the proof sketch, or admit it is a conjecture.

**Maya** (Paranoid Realism): My concern is reputational. If this work is
presented to ACT people and the categorical vocabulary is decorative — if calling
the charter a "product" doesn't actually constrain anything that calling it a
"combined document" would not — then the formalism becomes a liability. The
audience will see through it. I want to know where the categorical language is
doing real work and where it is cargo-culting.

**Joe** (Historian): The bibliography cites Fong, Spivak, Kelly, Baez & Stay,
and De Wynter et al. These are real sources. But I need to check: does the work
engage with them substantively, or just cite them as authority? Fong's decorated
cospans thesis is 200 pages of careful construction. Saying "the fit appears
natural" (decorated-texts.md, line 704) is not engagement with Fong.

**Frankie** (Opportunity Scout): I see something genuinely interesting here that
the other panelists might miss while hunting for gaps. The soft type system —
types as (template, rubric) pairs with graded inhabitation — is not a standard
categorical construction. It has no obvious precedent in the ACT literature that
I can identify. If it can be formalized properly, it could be a real
contribution. I want to figure out what categorical structure it corresponds to
and whether the "furry logic" extension has legs.

**Tammy** (Systems Thinker): I count at least four distinct categorical stories
running in parallel: (1) the base SMC of pipeline operations, (2) the Kleisli
layer for stochasticity, (3) the enrichment layer for confidence propagation,
(4) the lax/approximate coherence story. My question is whether these compose
into a coherent mathematical framework or whether the formalism is trying to be
four things at once without settling on any of them.

---

## Round 1: The Warrant Audit

### 1.1 The category Text as a symmetric monoidal category

**Vic**: categorical-structures.md §2 defines Text with objects (soft types),
morphisms (pipeline operations), composition (sequential wiring), identity
(pass-through), and monoidal product (×). This is the most important claim in
the corpus. Is it warranted?

The objects are well-defined: (template, rubric) pairs. The morphisms are
specified by prompt texts and typed by their input/output signatures. Composition
is sequential application. So far this is fine — you can certainly define a
category with this data. But three things are missing.

First, associativity and identity laws for composition. The text says "run f
then g," but in a stochastic system, does `(h ∘ g) ∘ f` produce the same
distribution as `h ∘ (g ∘ f)`? The answer depends on whether the intermediate
artifacts carry all relevant state or whether there are hidden side effects
(context window, conversation history). The text does not address this.

Second, the monoidal structure. The text says × is the monoidal product and the
"trivial empty artifact" is the unit. What is the associator? What is the
symmetry natural isomorphism? In a deterministic setting these would be trivial
(just re-bracketing tuples), but in the Kleisli setting they need to be
specified.

Third, the claim that the category is symmetric. The text says "input order does
not affect the operation." But the Deliberate morphism takes `charter ×
scenario-set × roster` — does the LLM actually produce the same distribution
regardless of the order in which these inputs are presented in the prompt? This
is an empirical claim about LLM behaviour, not a structural guarantee.

**Classification**: **Plausible but unproven.** The data for a category is
present. The axioms have not been verified, and in the stochastic setting the
verification is nontrivial.

**Maya**: And notice what "plausible but unproven" buys an ACT audience:
nothing. They will ask exactly these questions in the first five minutes of a
talk. If you cannot answer them, the rest of the formalism rests on sand.

### 1.2 The Kleisli category claim

**Vic**: categorical-structures.md §2 says morphisms are Kleisli arrows
`(Text, Meta) → M(Text, Meta)` where M is "a nondeterminism monad." The
decorated-texts.md Related Work section (line 720) elaborates: M combines
"probability distributions (stochasticity), error handling (failure modes), and
possibly other effects." But M is never specified. What monad? What is its unit?
What is its multiplication?

This matters enormously. Products in a Kleisli category require the monad to be
commutative (Kock, 1970). If M is a probability distribution monad (the Giry
monad), it is commutative, and Kleisli products exist. If M includes failure
effects combined via a monad transformer, commutativity may fail, and then the
Kleisli category may not have the products the formalism relies on.

The text also says the constructions in categorical-structures.md are
"constructions in the Kleisli category, not the base category." But equalizers,
pullbacks, and pushouts in Kleisli categories require much stronger conditions
on the monad than mere commutativity. The text makes no attempt to verify these
conditions.

**Classification**: **Overclaimed.** Saying the morphisms are Kleisli arrows
without specifying M is like saying "our functions live in a monad" without
saying which one. The claim is suggestive but does no mathematical work until M
is pinned down.

**Tammy**: Worse, the duality-and-composition.md introduces a *second* monad —
the "decision monad" `M(situation) = Funnel(Fan(situation))`. The relationship
between this monad and the ambient Kleisli monad is never discussed. Are we in a
Kleisli category of one monad, with a second monad layered on top? That is a
distributive law situation (Beck, 1969) and the conditions are stringent. The
text treats the two monads as if they live in separate universes.

### 1.3 The enriched category claim

**Vic**: categorical-structures.md §2 says hom-sets carry "graded confidence
information" and this makes Text "an enriched category over a confidence
lattice," citing Kelly. What lattice? The text describes three confidence bands:
High, Medium, Low. That is a total order `Low ≤ Medium ≤ High`, which is a
lattice. But enrichment requires a monoidal closed category as enrichment base
(Kelly, Ch. 1.2). A three-element lattice with min as tensor is a quantale,
hence monoidal closed. So the claim is at least structurally sensible.

But what are the enriched composition maps? If `Hom(A,B)` is a confidence level
and `Hom(B,C)` is a confidence level, what is `Hom(A,C)`? The text says
"confidence degrades monotonically through composition," which suggests
`Hom(A,C) = min(Hom(A,B), Hom(B,C))`. This is consistent with enrichment over
`({L,M,H}, min, H)` as a monoidal category. So far, fine.

But the reference.md also describes semiring-style and Pareto-style score
combination (lines 175-186). If different pipeline stages use different
combination rules, what is the enrichment base? You cannot enrich over different
monoidal structures at different stages without a mechanism to relate them. The
text does not address this.

**Classification**: **Plausible but unproven** for the basic min-lattice
enrichment. **Unclear** for the multi-structure score combination story — it
could be enrichment over a product of enrichment bases, but this is not stated.

### 1.4 Products and coproducts: the "approximate" qualifier

**Vic**: categorical-structures.md §4 calls the charter an "approximate product"
and §5 calls the scenario-set an "approximate coproduct." The text is honest
about this: "the charter is a product *target* — a design criterion … rather
than a product *fact*." The Probe (§9) is offered as the empirical test of how
close the approximation is.

But "approximate" needs a metric. In what sense approximate? The text says "up
to distributional equivalence" (§1), but distributional equivalence is not
defined. Options include: (a) the two distributions have the same support, (b)
they have the same mean, (c) they are within ε in total variation distance, (d)
they are within ε in Wasserstein distance. Each gives a different notion of
"approximate product." None is specified.

**Maya**: And this is where the cargo-cult risk is highest. If "approximate
product" just means "a thing that packages two inputs together," then every
function that takes two arguments is an "approximate product" and the
categorical language adds nothing. The universal property — the *uniqueness* of
the factoring map — is doing all the work, and it is exactly what the
approximation dissolves.

**Frankie**: I disagree that it adds nothing. Even as an approximate universal
property, the product framing tells you what to test: can you recover the
original inputs from the charter? The Probe operation checks this empirically.
That is not nothing — it is a design criterion derived from the categorical
structure. An engineer who has never heard of products would not think to test
recoverability. The categorical language is earning its keep as a *generator of
quality criteria*, even if the products are not strict.

**Classification**: **Plausible but unproven** for the coproduct (the
scenario-set genuinely has injections with provenance, and componentwise
extension is a real operational principle). **Overclaimed** for the product
(the charter compresses its inputs; calling this a "product" even with the
"approximate" qualifier is misleading unless recoverability is actually tested
and quantified).

### 1.5 The decision monad

**Vic**: duality-and-composition.md defines `M(situation) = Funnel(Fan
(situation))` and claims monad structure. The monad laws are given operational
interpretations (unit law: trivial deliberation ≈ identity; associativity:
nested application ≈ single broad pass). This is creative. But:

The unit is not defined. There is no η : situation → M(situation). The text
describes the unit law as a *test* (run with trivial deliberation and check the
output), not as a *morphism*.

The multiplication is not defined. There is no μ : M(M(situation)) →
M(situation). The text describes associativity as a *test* (compare nested runs
with single broad run), not as a natural transformation.

Without η and μ, there is no monad. The text is using "monad" in the informal
sense of "an idempotent-ish operation you can iterate." This is a legitimate
informal usage, but an ACT audience will expect the formal one.

**Joe**: The text cites no source for the adjunction claim ("if the fan is left
adjoint to the funnel"). Left adjoint to the funnel in what sense? Fan goes
`Situation → ScenarioSet`, Funnel goes `ScenarioSet × ... → Resolution`.
These don't even have matching source/target types for an adjunction.

**Classification**: **Overclaimed.** The operational quality-test interpretation
of the monad laws is genuinely useful. But calling this a monad without defining
unit and multiplication is a category error (pun intended).

### 1.6 Equalizers, pullbacks, pushouts

**Vic**: categorical-structures.md §6-7 describes equalizers (cross-scenario
triangulation), pullbacks (load-bearing claims), and pushouts (resolution as
amalgamation). The text itself acknowledges that the maps involved —
"claim-extraction maps" and "interpretation maps" — are "not yet formalized as
named operations." If the morphisms in the equalizer/pullback/pushout diagrams
don't exist as operations in the palgebra, these are not constructions in the
category. They are aspirational descriptions of constructions that could exist
if the relevant operations were defined.

**Maya**: This is the most honest part of the document, ironically. The text
says "they are *potential* operations that the equalizer construction motivates
defining." That is a perfectly reasonable thing to say in a design document. But
it means §6-7 are not mathematics — they are design specifications inspired by
mathematics. An ACT reviewer should be told this clearly.

**Classification**: **Unclear**, tending toward **well-warranted as design
patterns** but **vacuous as categorical constructions** until the maps are
defined.

### 1.7 The Frobenius structure

**Vic**: duality-and-composition.md implies fan and funnel form a Frobenius pair
(the symmetry table on line 48 calls them "multiplication" and
"comultiplication"). categorical-structures.md §8 notes this terminology
explicitly and says the fan is a "coproduct spider" / "multiplication" and the
funnel is a "product spider" / "comultiplication." For a Frobenius structure,
you need four maps (multiplication, comultiplication, unit, counit) satisfying
the Frobenius equation: `(μ ⊗ id) ∘ (id ⊗ δ) = δ ∘ μ = (id ⊗ μ) ∘ (δ ⊗ id)`.
None of these equations are stated, let alone verified.

**Classification**: **Overclaimed.** The spider terminology is suggestive but
the Frobenius equations are never stated. An ACT reader who sees
"multiplication" and "comultiplication" will expect a Frobenius algebra, and
finding none will lose trust.

### 1.8 Traced monoidal structure (the feedback loop)

**Vic**: committee-as-palgebra.md describes the remediation loop as "traced
monoidal structure" — a finite unrolling of a trace. Trace in a monoidal
category (Joyal, Street, Verity, 1996) requires specific axioms (naturality,
superposing, yanking). The text uses the term correctly at the intuitive level —
there is a feedback wire from Remediate's output back to Evaluate's input — and
the finite unrolling is an honest concession. The bounded trace (max 2 rounds)
sidesteps the convergence questions that an unbounded trace would raise.

**Classification**: **Plausible but unproven.** The intuitive description maps
well onto traced monoidal structure. The axioms have not been checked, but
checking them is a well-defined exercise.

---

## Round 2: Foundational Coherence

**Tammy**: Do the documents describe the same category?

The base category in decorated-texts.md has objects as "named kinds of text
artifacts" and morphisms as "named transformations, each specified by a prompt
text." The category in categorical-structures.md has objects as "soft types:
(template, rubric) pairs" and morphisms as "pipeline operations." These are
compatible — the soft type is a refinement of the "named kind" — but the
transition is implicit. An ACT reader encountering both documents would need to
verify that the categorical-structures version is a sub-category or enrichment
of the decorated-texts version, not a different category.

The monoidal structure in reference.md (× operator) is consistent with
categorical-structures.md. The enrichment story (confidence propagation in
reference.md) aligns with the enriched category claim in
categorical-structures.md for the min-lattice case.

The resource equations in committee-as-palgebra.md and duality-and-composition.md
are well-typed according to reference.md. I checked: every morphism's input and
output types are declared, catalytic inputs are marked, enrichments are
namespaced. The formalism is internally consistent at the level of its own
notation.

**Assessment**: The documents are coherent with each other. The drift is
upward — each successive document claims stronger categorical properties than
the previous one, without always back-porting the qualifications. The
"approximate" caveat from categorical-structures.md §1 should propagate to
every document that claims categorical properties.

---

## Round 3: What's Actually New Here

**Joe**: Let me sort the contributions.

**Straightforward instantiation of existing frameworks:**

The resource equation notation, the string diagram rendering, and the basic
composition story are a direct application of Fong & Spivak's Chapter 2 to a
new domain (LLM pipelines instead of manufacturing). The string-diagram tool
that converts equations to Mermaid is a nice engineering artifact but not a
mathematical contribution. The two-morphism-kind distinction (transformation vs.
enrichment) is the process algebra distinction between state-changing and
state-observing operations, which has many precedents.

**Domain-specific adaptation with genuine conceptual content:**

The soft type system — (template, rubric) pairs with graded inhabitation — is
the most original element. I cannot find a direct precedent in the ACT
literature. It resembles fuzzy-set-valued presheaves (Stout, 1982) or
quantale-valued sheaves (Mulvey, 1986), but the dual template/rubric structure
(structural support vs. semantic membership function) is specific to this
domain and may warrant novel categorical treatment.

The "furry logic" extension (distributional type membership) is even more
interesting. If types are measures on type-space rather than points, you get a
category enriched over the space of probability measures. This connects to
categorical probability (Fritz, Rischel, 2020) and potentially to the Giry
monad. Nobody has done this for a type system, as far as I can tell.

The Probe as an empirical universal-property test is a genuinely novel idea. I
know of no precedent for operationalizing universal properties as repeated-trial
variance analyses. This could be publishable as a short note even without the
rest of the formalism.

**Maya**: The fact that the most original ideas are the least formalized is not
a coincidence. Formalization is hard. Everything that is easy to formalize has
already been done by Fong or Spivak. Everything that is hard to formalize is
where the palgebra might actually contribute — but it has not done the work yet.

**Regarding the cited references**: De Wynter et al. ("On Meta-Prompting") is
cited appropriately — the text correctly distinguishes its level of analysis
(single LLM calls) from palgebra's level (multi-step pipelines). The Fong
citation is appropriate but under-engaged. Kelly is cited by name only; there is
no evidence of deep engagement with enriched category theory. A notable omission
is Fritz's "A synthetic approach to Markov kernels" (2020), which provides the
categorical framework for stochastic maps that the Kleisli story needs.

---

## Round 4: Soft Types and Distributional Membership

**Frankie**: This is where the formalism could make its mark. Let me lay out the
structure.

A soft type τ = (template, rubric) defines: (a) a *support* — the set of
artifacts that match the template structurally, and (b) a *membership function*
— the rubric scores each artifact in the support on a graded scale. This is not
a fuzzy set in the Zadeh sense (where membership is a single value in [0,1]).
It is a *multi-dimensional* graded membership: five criteria, each 0-3, rolling
up to a band. The membership datum is a point in [0,3]^5, not a scalar.

Categorically, what is this? Here are candidates:

1. **Quantale-valued sheaves.** If the confidence lattice were a quantale Q,
   soft types could be Q-valued sheaves on the pipeline category. The template
   is the underlying set; the rubric is the Q-valued membership. Composition
   (confidence degradation via min) is the quantale multiplication. This works
   for the scalar case (Q = {L,M,H}). For the vector case ([0,3]^5), you need
   a product quantale.

2. **Lawvere metric spaces.** If you interpret the rubric scores as distances
   (distance from perfect type inhabitation), you get a generalized metric
   space. The confidence propagation rule (min composition) becomes the triangle
   inequality. This aligns with the enrichment over a quantale story.

3. **Probabilistic coherence spaces.** These model linear logic with
   probabilistic semantics. The dual template/rubric structure — structural
   support plus semantic weighting — mirrors the web/coherence split in
   coherence spaces. The connection is speculative but worth investigating.

The furry logic extension goes further: type membership is not a grade but a
*distribution* over type-space. This is exactly a Giry-monad-valued type
assignment: artifacts don't inhabit types at a grade, they inhabit the space of
distributions over types. Composition of pipeline operations would then be
composition of Markov kernels on type-space. This connects directly to Fritz's
categorical probability framework.

**Vic**: How much of this is actually *in* the documents versus your
extrapolation?

**Frankie**: Almost none of it is in the documents. The soft type system is
described operationally. The categorical interpretations I just gave are
reconstructions. The furry-logic diary entry gestures toward the distributional
framing but does not give any of these formal connections. This is a gap, but
it is a gap that could be filled with existing ACT tools. The novelty is in the
domain structure (template + rubric + graded vector-valued membership), not in
the categorical machinery needed to formalize it.

---

## Round 5: The Lax/Approximate Coherence Question

**Tammy**: categorical-structures.md §1 states that coherence holds "up to
distributional equivalence" and that the constructions are "lax." This is the
most important qualifying statement in the corpus. Let me assess it.

The text uses "lax" informally — not in the 2-categorical sense (lax functors,
lax natural transformations) but in the colloquial sense of "not strict." For
an ACT audience, this ambiguity is a problem. "Lax monoidal functor" means
something precise; "lax product" is not standard terminology.

There are several formal frameworks that could capture the intended meaning:

1. **Bicategories / 2-categories.** If "distributional equivalence" is a 2-cell,
   then the pipeline forms a bicategory where 1-cells are pipeline operations
   and 2-cells are distributional equivalences between operations. Products and
   coproducts would be bilimits. This is standard but requires specifying what
   the 2-cells are.

2. **Markov categories** (Fritz, 2020). A Markov category is a semicartesian
   symmetric monoidal category with a "copy" natural transformation. It is the
   native categorical framework for stochastic maps. If Text is a Markov
   category, then: (a) the "copy" map gives the comonoid structure for catalytic
   inputs, (b) the monoidal product handles parallel composition, (c)
   deterministic morphisms form a subcategory. This would resolve or at least
   clarify most of the coherence issues without requiring lax or approximate
   language.

3. **Quasi-Borel spaces** (Heunen, Kammar, Staton, Yang, 2017). These provide a
   convenient category for probability that is cartesian closed. If the
   artifacts live in a quasi-Borel space, the stochastic pipeline operations are
   morphisms in this category, and the coherence conditions are exact (not
   approximate).

The palgebra documents cite none of these frameworks. The "lax coherence" story
is an honest acknowledgment of the problem but not a solution. The solution
exists in the literature; it just has not been imported.

**Maya**: I want to press on the eigenform connection. categorical-structures.md
§9 connects eigenforms to the potential-to-sense essay and claims that
categorical structures are "structural eigenforms" — patterns that stabilise
across runs even when content varies. This is a beautiful idea. But does
"eigenform" correspond to anything in categorical probability? An eigenform of a
Markov kernel is a stationary distribution. If the pipeline is a Markov kernel,
its eigenforms are the distributions that are fixed points of repeated
application. This is exactly what the Probe tests. The connection is there, and
it is precise — but the documents do not make it.

---

## Round 6: Strengths

**Frankie** [leading]:

1. **Operational grounding.** The formalism is not abstract — it has a running
   pipeline with actual input/output files, YAML metadata, and a tool that
   converts equations to diagrams. This is unusually concrete for an ACT paper.
   Most ACT work starts from mathematics and gestures at applications; this
   starts from an application and reaches toward mathematics. The direction
   matters: it means the categorical claims are *tested* (informally) by whether
   the pipeline works, not just by whether the diagrams commute.

2. **The triple representation.** Resource equations, string diagrams, and
   decorated artifact files as three isomorphic views. This is the right way to
   organize an applied categorical project. It makes the formalism usable by
   practitioners who cannot read commutative diagrams.

3. **Honesty about approximation.** The "design target, not theorem" framing in
   categorical-structures.md §1 and §4 is exactly the right tone. It does not
   pretend the products are strict. It does not apologize for the approximation.
   It frames the categorical structures as *generators of quality criteria* —
   you use the universal property to derive what to test, then test it
   empirically. This is a pragmatic philosophy of applied mathematics that ACT
   people will recognise and respect.

4. **The Probe.** Running the pipeline N times and comparing variance is a novel
   operationalization of universal properties. No one in ACT has proposed this
   (to my knowledge). It connects to statistical testing of categorical
   hypotheses — a direction that has no precedent and could generate real
   research.

5. **Clear writing.** For a practitioner audience, the exposition is excellent.
   The lemon-meringue-pie opening in decorated-texts.md is effective pedagogy.
   The careful separation of operationally honest from type-theoretic readings
   of the initial object (§3) shows mathematical sophistication.

---

## Round 7: Weaknesses and Gaps

**Maya** [leading]:

1. **No definitions precise enough to be theorems.** Not a single claim in the
   corpus is stated with enough precision to be proved or disproved. The
   category Text is not defined to the level where you could check its axioms.
   The monad M is not specified. The enrichment base is gestured at. An ACT
   reviewer's first question will be: "state your main theorem." There is no
   main theorem.

2. **The enrichment, Kleisli, and distributional stories are not integrated.**
   Tammy's concern is justified. The text presents three different categorical
   perspectives (enriched category, Kleisli category, distributional/lax
   category) without explaining how they relate. In principle they could be
   layers of a single framework: base category → Kleisli category of M →
   enriched over confidence lattice → lax/approximate coherence as 2-categorical
   structure. But this layering is never stated, and the compatibility
   conditions between layers are never checked.

3. **Unmaterialized morphisms.** The equalizer/pullback/pushout sections depend
   on "claim-extraction maps" and "interpretation maps" that do not exist as
   pipeline operations. These sections are speculative mathematics about a
   system that does not yet have the operations they require.

4. **Spider/Frobenius terminology without substance.** Calling fan and funnel
   "multiplication" and "comultiplication" invites the Frobenius question, which
   the text cannot answer. This is worse than not using the terminology at all,
   because it creates a false expectation.

5. **Missing engagement with Markov categories.** The entire "approximate
   coherence" problem likely dissolves if you situate Text as a Markov category.
   Fritz (2020) handles stochastic maps, copying (catalytic inputs), and
   deterministic sub-operations all within one framework. Not citing this work
   is a significant gap.

6. **The "decision monad" is not a monad.** The unit and multiplication are
   missing. The monad laws are reinterpreted as operational tests — which is
   valuable — but calling the construction a monad is an overclaim that will
   erode credibility with the target audience.

7. **Risk of "ACT theater."** Some of the categorical vocabulary (particularly
   in §6-7) adds complexity without adding insight. Calling the resolution a
   "coequalizer" when the maps are undefined is not illuminating — it is
   name-dropping. An ACT audience will penalize this more than a general
   audience would.

---

## Round 8: Filling In the Mathematics

**Tammy** [leading, with interventions]:

### Minimum viable formalization

The smallest set of precise work that would make the central claims rigorous:

**Priority 1: Define the category Text precisely.** Objects: soft types (this is
done). Morphisms: specify what data constitutes a morphism (prompt text, input
type, output type, metadata schema). Composition: specify how sequential
application preserves typing. Identity: specify the pass-through. Monoidal
product: specify how × works (tupling of artifacts and metadata). Unit: the
empty artifact. Verify: associativity, identity, interchange. This is a
*definitions* task, not a theorems task — you are documenting what you already
have, not proving something new.

**Priority 2: Situate Text as a Markov category.** Import Fritz (2020). Define
the "copy" morphism (this is what catalytic inputs already are — the comonoid
structure). Show that deterministic enrichments form a subcategory.
Show that the monoidal product satisfies the semicartesian condition. This
resolves the approximate coherence problem: stochastic maps compose associatively
in a Markov category without requiring diagrams to commute on the nose.

**Vic**: What existing result does this import?

**Tammy**: Fritz's Theorem 3.1 shows that the category of Markov kernels is a
Markov category. If your objects are measurable spaces (or a suitable synthetic
substitute) and morphisms are Markov kernels, you get a SMC with copy. The task
is to show that soft types and pipeline operations fit this pattern.

**Priority 3: Specify the enrichment base.** Define the confidence lattice as
`({Low, Medium, High}, min, High)`. Show that this is a monoidal category (it
is a commutative quantale). State the enriched composition law:
`confidence(g ∘ f) = min(confidence(f), confidence(g))`. Show that this
satisfies the enrichment axioms. This is straightforward.

**Priority 4: Define the decision monad properly, or stop calling it a monad.**
Either: (a) define η and μ explicitly and verify the monad laws up to
distributional equivalence, or (b) rename the construction to "decision
pipeline" and keep the operational quality tests without the monad claim. Option
(b) is honest and loses nothing of practical value.

**Priority 5: Formalize one limit construction end-to-end.** Pick the coproduct
(scenario-set). Define the injections precisely. State the universal property.
Show that componentwise extension works. If this can be done rigorously, it
validates the approach and provides a template for the other constructions. If it
cannot, that is useful information.

### What would require new theorems

The soft type system as a quantale-valued presheaf, and the furry logic
extension as a Giry-monad-valued type assignment, would require new
constructions. The question of whether the Probe detects failure of universal
properties in a statistically valid way is also original and would need a new
result (connecting categorical universal properties to hypothesis testing).

### Rabbit holes to avoid

**Joe**: Don't try to formalize the equalizers/pullbacks until the
claim-extraction maps exist as pipeline operations. Those sections are currently
aspirational. Formalizing aspirations is a waste.

**Maya**: Don't try to make the Frobenius structure work unless the fan and
funnel actually satisfy the Frobenius equations. Just drop the
multiplication/comultiplication terminology.

---

## Round 9: Extension Directions

**Frankie** [leading]:

### Direction 1: Markov categories for the stochastic structure

**What**: Reformulate Text as a Markov category (Fritz, 2020).
**Cites**: Fritz, "A synthetic approach to Markov kernels, conditional products,
and information loss," 2020.
**Difficulty**: Straightforward application of known results.
**What it buys**: Dissolves the approximate coherence problem. Provides a
principled account of copying (catalytic inputs), determinism (enrichments), and
stochasticity (transformations) within one framework. The copy map is exactly
the comonoid structure the text already uses for catalytic inputs.

### Direction 2: Categorical probability for distributional types

**What**: Formalize furry logic (distributional type membership) using the
synthetic probability framework.
**Cites**: Fritz and Rischel, "Infinite products and zero-one laws in
categorical probability," 2020; Cho and Jacobs, "Disintegration and Bayesian
inversion via string diagrams," 2019.
**Difficulty**: Nontrivial adaptation. The domain structure (template + rubric +
multi-dimensional scores) is specific and needs custom treatment.
**What it buys**: A formal account of how type information composes through
stochastic pipelines. Routing as Bayesian decision (from the furry-logic diary)
becomes a categorical construction. This is the direction with the most
potential for a novel mathematical contribution.

### Direction 3: Open games for the committee structure

**What**: Complete the formalization in committee-as-open-game.md using the
Hedges/Bolt/Zahn framework.
**Cites**: Bolt, Hedges, Zahn, "Bayesian open games," 2019; Ghani, Hedges,
Winschel, Zahn, "Compositional game theory," 2018.
**Difficulty**: Nontrivial — the non-standard equilibrium concept
(coverage-maximizing rather than utility-maximizing) needs careful definition.
**What it buys**: A strategic dimension that the resource-theoretic treatment
lacks. Makes rubric design explicitly a mechanism design problem. Could yield
concrete results about when the committee reaches equilibrium and what that
equilibrium looks like.

### Direction 4: Decorated cospans for pipeline composition

**What**: Map pipeline operations onto Fong's decorated cospans.
**Cites**: Fong, "The Algebra of Open and Interconnected Systems," 2016.
**Difficulty**: Straightforward for the basic composition story. The decorations
(metadata, confidence, provenance) add domain-specific complexity.
**What it buys**: Formal compositionality guarantees. The ability to reason about
pipeline composition using Fong's functoriality results.

### Direction 5: Operads for multi-input operations

**What**: Model pipeline operations with multiple inputs as algebras over
operads or multicategories.
**Cites**: Leinster, "Higher Operads, Higher Categories," 2004; Spivak,
"The operad of wiring diagrams," 2013.
**Difficulty**: Moderate — the basic setup is standard but the interaction with
stochasticity and enrichment would need work.
**What it buys**: A cleaner treatment of operations like Deliberate (which takes
five inputs) without forcing them through the monoidal product. Multi-input
operations are first-class citizens in an operad, not encoded as binary products.

---

## Deliverables

### Warrant Table

| # | Claim | Location | Classification | Justification |
|---|-------|----------|---------------|---------------|
| 1 | Text is a symmetric monoidal category | cat-struct §2 | Plausible but unproven | Data present; axioms unchecked, especially symmetry under stochasticity |
| 2 | Morphisms are Kleisli arrows of M | cat-struct §2, dec-texts Related Work | Overclaimed | M never specified; required monad properties (commutativity) unverified |
| 3 | Text is enriched over a confidence lattice | cat-struct §2 | Plausible but unproven | Min-lattice enrichment is structurally sound; multi-structure scoring unaddressed |
| 4 | Charter is an approximate product | cat-struct §4 | Overclaimed | Compression is not a product; recoverability not tested; "approximate" has no metric |
| 5 | Scenario-set is a coproduct | cat-struct §5 | Plausible but unproven | Injections with provenance exist; componentwise extension is operational; universal property not formally stated |
| 6 | Variance report is a coproduct of Probe runs | cat-struct §5 | Well-warranted | N resolutions tagged by run index; componentwise analysis (Map) is the defining operation |
| 7 | Cross-scenario triangulation is an equalizer | cat-struct §6 | Unclear | Maps undefined; sensible as a design pattern; vacuous as a construction |
| 8 | Resolution is a coequalizer/pushout | cat-struct §6-7 | Unclear | Maps undefined; good intuition for what the funnel does; not formalizable yet |
| 9 | Fan/funnel are multiplication/comultiplication | cat-struct §8, dual-comp | Overclaimed | Frobenius equations never stated or verified; terminology misleading |
| 10 | Fan ∘ Funnel is a monad | dual-comp §Monad | Overclaimed | Unit and multiplication undefined; operational tests are valuable but not a monad |
| 11 | Remediation loop is traced monoidal structure | comm-palg | Plausible but unproven | Intuitive match is good; trace axioms unchecked; bounded unrolling is honest |
| 12 | Catalytic inputs are comonoid objects | comm-palg, reference | Well-warranted | Copy + delete structure is exactly comonoid; consistent with Markov category copy |
| 13 | Enrichments are idempotent endomorphisms | dec-texts, reference | Plausible but unproven | True when model and inputs frozen; stochasticity breaks strict idempotence |
| 14 | Three representations are isomorphic | dec-texts, reference | Plausible but unproven | Equations ↔ diagrams is mechanical; equations ↔ files is a convention, not an isomorphism |
| 15 | Confidence degrades monotonically through composition | dec-texts, reference | Well-warranted | Follows from min-lattice enrichment; this is the enrichment axiom |
| 16 | Human gates are collapse operators | dec-texts, comm-palg | Plausible but unproven | Good analogy to measurement; "collapse" is informal; could be made precise as a monad algebra |
| 17 | Eigenforms are fixed points of Probe iteration | cat-struct §9 | Plausible but unproven | Matches stationary distribution of a Markov kernel; connection not formalized |
| 18 | Soft types are (template, rubric) pairs with graded inhabitation | all documents | Well-warranted | Consistently defined and operationally implemented across all documents |

### Prioritised Gap List

1. **Specify the category Text precisely** — definitions only; no new theorems needed; maximum impact on credibility
2. **Import Markov categories** — resolves the approximate coherence problem with existing machinery
3. **Specify the enrichment base and verify enrichment axioms** — straightforward; cements the confidence propagation story
4. **Define or disown the decision monad** — either give η and μ or rename; currently an active credibility risk
5. **Formalize the scenario-set coproduct end-to-end** — one fully worked example validates the approach
6. **Drop Frobenius/spider terminology** — or state the Frobenius equations; current usage invites questions that cannot be answered
7. **Engage with Fritz (2020) on Markov categories** — the most consequential missing citation
8. **Formalize the eigenform/Probe connection** — novel and potentially publishable; needs stationary-distribution framing
9. **Give "approximate" a metric** — total variation, Wasserstein, or something domain-specific; without this, "approximate product" is vacuous
10. **Integrate the enrichment, Kleisli, and distributional layers** — show they are compatible, not just parallel stories

### Recommended Reading List

1. **Fritz, T.** "A synthetic approach to Markov kernels, conditional products, and information loss." *Advances in Mathematics* 370, 2020. — The categorical framework for stochastic maps. Resolves the approximate coherence problem and provides the comonoid (copy) structure palgebra already uses informally.

2. **Cho, K. and Jacobs, B.** "Disintegration and Bayesian inversion via string diagrams." *Mathematical Structures in Computer Science* 29(7), 2019. — String diagram calculus for probabilistic reasoning. Directly applicable to the distributional type membership question.

3. **Fong, B.** *The Algebra of Open and Interconnected Systems.* PhD thesis, Oxford, 2016, Chapters 2-4. — Not just the citation but the actual technical development of decorated cospans. The palgebra corpus cites this but has not engaged with the pushout construction that makes decorated cospans work.

4. **Ghani, N., Hedges, J., Winschel, V., and Zahn, P.** "Compositional game theory." *LICS 2018.* — Foundation for the open-games treatment in committee-as-open-game.md. Required reading for the game-theoretic extension direction.

5. **Heunen, C., Kammar, O., Staton, S., and Yang, H.** "A convenient category for higher-order probability theory." *LICS 2017.* — Quasi-Borel spaces. A cartesian closed category of probability spaces that could serve as the ambient category for Text if the distributional type story is pursued.

6. **Kock, A.** "Monads on symmetric monoidal closed categories." *Archiv der Mathematik* 21, 1970. — Commutative monads. Required for understanding when the Kleisli category has the products the palgebra assumes.

7. **Perrone, P.** "Markov categories and entropy." *IEEE Trans. Information Theory* 70(3), 2024. — Extends Fritz's framework to information loss, which connects directly to the confidence degradation story.

8. **Spivak, D.I.** "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits." *arXiv:1305.0297,* 2013. — Operads for systems with multiple inputs and outputs. Cleaner treatment of multi-input pipeline operations than forcing them through monoidal product.

9. **Leinster, T.** "The magnitude of metric spaces." *Documenta Mathematica* 18, 2013. — Enriched category theory applied to metric spaces. Relevant to the confidence-lattice enrichment and the Lawvere metric interpretation of rubric scores.

10. **Jacobs, B.** "Probabilities, distribution monads, and convex categories." *Theoretical Computer Science* 412(28), 2011. — Distribution monads and convex algebras. Connects the Giry monad, convex combination of strategies, and probability-valued type membership.

### Verdict

**Mathematical maturity**: Early-stage. The formalism has genuine
conceptual content — particularly the soft type system, the Probe as empirical
universal-property test, and the operational interpretation of monad laws as
quality criteria — but no claim is stated precisely enough to be a theorem. The
categorical vocabulary ranges from well-warranted (comonoids, confidence
degradation) through plausible (enrichment, traced structure) to overclaimed
(Kleisli monad, decision monad, Frobenius structure, approximate products).

**Potential as ACT contribution**: Moderate to high, *conditional on filling the
gaps.* The three most promising directions are: (1) soft types / furry logic as
a novel enrichment or presheaf structure, (2) the Probe as a statistical test
of categorical universal properties, and (3) the Markov category reformulation
that would resolve the coherence question. Direction (1) is potentially
publishable. Direction (2) is novel and could attract interest from the
categorical probability community. Direction (3) is necessary groundwork that
would establish credibility.

**Risk**: If presented in its current state to an ACT audience, the formalism
will be received as interesting applied work with suggestive but imprecise
categorical language. This is not fatal — many applied category theory projects
start this way — but the overclaims (monad, Frobenius, Kleisli without
specifying M) will draw friendly fire that could be avoided by either
formalizing or honestly downgrading. The recommended strategy: formalize what
you can (Priorities 1-3 above), downgrade what you cannot yet (Priorities 4,
6), and present the novel elements (soft types, Probe, operational monad laws)
as the main contribution, with the categorical precision as a work in progress.

**Trustworthiness as mathematical document**: Medium. Internally consistent and
conceptually rich, but not yet rigorous enough for peer review. Suitable as a
working document, technical report, or blog post. Not suitable as a submission
to a mathematics venue without substantial formalization work. Could be suitable
for an applied venue (e.g., ACT conference applied track) with Priorities 1-5
addressed.
