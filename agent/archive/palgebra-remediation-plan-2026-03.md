# Remediation Plan: Palgebra for Applied Category Theorists

**Date**: 2026-03-13
**Status**: All phases complete (2026-03-13). Archived.
**Source**: `palgebra/act-review-2026-03.md`
**Goal**: Address the review's findings systematically, converting the
palgebra corpus from "early-stage formalism with genuine conceptual
content" into work suitable for the ACT applied track.

---

## Guiding principles

The review's verdict is clear: the conceptual content is real, but no
claim is stated precisely enough to be a theorem. The overclaims erode
credibility with exactly the audience we want to reach. The strategy
is therefore:

1. **Formalize what we can** — definitions first, theorems where
   possible.
2. **Honestly downgrade what we cannot yet** — rename or qualify
   rather than overclaim.
3. **Present the novel elements as the main contribution** — soft
   types, the Probe, operational monad-law tests.
4. **Import existing frameworks rather than reinventing** — Fritz's
   Markov categories dissolve most of the "approximate coherence"
   problem.

Each task below is tagged with the review gap it addresses, the
file(s) it touches, and a rough difficulty estimate.

---

## Phase 1: Foundations (do first — everything else depends on these)

### 1.1 Define the category Text precisely

**Review gap**: #1 (specify the category), Warrant Table rows 1–2
**Files**: `categorical-structures.md` §2, new section or appendix
**Difficulty**: Definitions only; no new theorems needed

The review notes that the data for a category is present but the
axioms have not been verified. Three things are missing:

**A. Associativity and identity laws for composition.** In a
stochastic system, does `(h ∘ g) ∘ f` produce the same distribution
as `h ∘ (g ∘ f)`? The answer depends on whether intermediate
artifacts carry all relevant state. We need to either:

- State a **self-containment condition** on artifacts (all downstream-
  relevant state is in the (text, metadata) pair; no hidden context-
  window effects), and show that under this condition composition is
  associative up to distributional equivalence; or
- Acknowledge that the condition is a design discipline (enforced by
  the template system) rather than a structural guarantee, and frame
  associativity as a quality target tested by the Probe.

The honest path is probably both: state the condition, explain how the
template system enforces it, note that violations (context-window
leakage, ordering effects) are empirically detectable via the Probe.

**B. Monoidal structure.** Specify the associator, left/right
unitors, and symmetry isomorphism. In the deterministic case these
are trivial (re-bracketing tuples of artifacts). In the Kleisli
setting, state that they are inherited from the base category (since
the monad acts on the content, not the packaging). This needs to be
said explicitly.

**C. Symmetry.** The review flags that "input order does not affect
the operation" is an empirical claim about LLM behaviour. We should:

- Acknowledge this candidly.
- Define symmetry as holding when the pipeline's output distribution
  is invariant under input permutation.
- Note that prompt-engineering best practice (consistent input
  ordering, structured templates) is exactly the discipline that
  enforces approximate symmetry.
- Frame the Probe as the empirical test of symmetry violations.

**Deliverable**: Rewrite §2 of `categorical-structures.md` with
explicit axiom statements, conditions under which they hold, and
pointers to the Probe as the empirical verification mechanism.

---

### 1.2 Situate Text as a Markov category

**Review gap**: #2 (import Markov categories), #5 (missing engagement
with Fritz), #7 (Fritz citation)
**Files**: New section in `categorical-structures.md` (insert after
§2), update `reference.md` ✓ (done — Fritz already added)
**Difficulty**: Straightforward application of known results

This is the single highest-leverage change. Fritz (2020) provides a
framework where:

- **Stochastic maps compose associatively** without requiring diagrams
  to commute on the nose — this dissolves the "approximate coherence"
  problem that currently requires the awkward "lax" qualifier.
- **The copy morphism** (comonoid structure) is exactly what catalytic
  inputs already are — the formalism already uses this informally.
- **Deterministic morphisms** form a subcategory — this is the
  enrichment/transformation distinction already in the palgebra.
- **Semicartesian structure** handles the monoidal product without
  requiring strict products.

The work:

**A.** State the definition of a Markov category (Fritz, Definition
2.1): a semicartesian symmetric monoidal category with a commutative
comonoid structure on every object (the "copy" map) satisfying
naturality conditions.

**B.** Show that Text fits this pattern:
- Objects: soft types (as before).
- Morphisms: stochastic pipeline operations (Markov kernels on the
  space of artifacts).
- Monoidal product: × (tupling).
- Copy map: the operation that feeds an artifact into two downstream
  consumers without alteration — this is exactly what `{catalytic: X}`
  already denotes.
- Delete map: the discard operation `{discard: X}`.
- Deterministic sub-morphisms: enrichments (payload unchanged).

**C.** State which results from Fritz we import:
- Corollary 3.2: the Kleisli category of a symmetric monoidal affine
  monad on a Markov category is again a Markov category. (Note: Fritz's
  3.1 is a Proposition establishing that the Kleisli category is
  symmetric monoidal; the Markov category result is Corollary 3.2.)
- The treatment of conditional independence (relevant for scenario
  independence assumptions).
- The copy/delete structure (relevant for catalytic inputs).

**D.** Explain what this buys: the "approximate" qualifier in §1
can be replaced with the precise statement that Text is a Markov
category, and coherence holds in the standard sense for stochastic
maps. The Probe remains valuable — not as a test of whether coherence
holds (it does, by construction), but as a test of whether the
*implementation* (specific prompts, specific models) faithfully
instantiates the Markov category structure.

**Deliverable**: New §2a in `categorical-structures.md`: "Text as a
Markov category." Update §1 to replace the informal "lax" discussion
with a forward reference to the Markov category treatment.

---

### 1.3 Specify the enrichment base

**Review gap**: #3 (specify enrichment base and verify axioms)
**Files**: `categorical-structures.md` §2, `reference.md` (score
combination section)
**Difficulty**: Straightforward

**A.** Define the enrichment base explicitly:
`V = ({Low, Medium, High}, min, High)` — a commutative quantale
(complete lattice with min as tensor, High as unit).

**B.** State the enriched composition law:
`confidence(g ∘ f) = min(confidence(f), confidence(g))`

**C.** Verify the enrichment axioms (Kelly, Ch. 1.2):
- Composition: the enriched composition map
  `Hom(B,C) ⊗ Hom(A,B) → Hom(A,C)` sends `(c₂, c₁) ↦ min(c₂, c₁)`.
  This is associative because min is associative.
- Identity: `High ≤ Hom(A,A)` for all A — the identity morphism has
  maximum confidence. True by definition.

**D.** Address the multi-structure scoring question from the review:
`reference.md` describes semiring and Pareto combination alongside
lattice. Explain that these apply at different levels:
- **Within a rubric**: individual criteria may combine via weighted
  sums (semiring) or Pareto frontiers.
- **Across pipeline stages**: confidence propagation uses the
  min-lattice — this is the enrichment.
- The enrichment base is the min-lattice. The other structures are
  internal to the scoring operations, not part of the enriched
  category structure.

**Deliverable**: Expanded enrichment subsection in §2 of
`categorical-structures.md` with explicit definitions and axiom
verification.

---

## Phase 2: Honest downgrades (credibility repairs)

### 2.1 Decision monad: define or disown

**Review gap**: #4 (define or stop calling it a monad)
**Files**: `duality-and-composition.md`, `categorical-structures.md`
§8, `reference.md` (spider patterns / decision monad section)
**Difficulty**: Conceptual — need to make a choice

The review is right: without η and μ, there is no monad. Two options:

**Option A: Define η and μ explicitly.**
- η (unit): `situation ↦ Fan(situation)` followed by trivial
  deliberation (single-round, no adversarial pressure) — a "rubber-
  stamp" committee. The unit law says: rubber-stamping should return
  approximately the original situation framing.
- μ (multiplication): `M(M(situation)) → M(situation)`. Operationally:
  take the resolution of a first fan-funnel pass, re-fan it, re-
  funnel it — versus doing a single broader fan-funnel. The
  associativity law says these should produce equivalent distributions.
- Verify monad laws "up to distributional equivalence" — which, in the
  Markov category framing, means up to equality of Markov kernels (a
  well-defined notion).

**Option B: Rename to "decision pipeline" and keep the operational
quality tests.** The quality tests (unit law ≈ "trivial deliberation
is identity," associativity ≈ "nested application ≈ single broad
pass") are valuable regardless of whether the construction is
technically a monad. Call them "monad-inspired quality criteria" and
drop the formal monad claim.

**Recommendation**: Option A if we can define η and μ cleanly in the
Markov category setting. Option B if the definitions become forced.
Start with A; fall back to B if it doesn't work. Either way, the
current text that describes monad laws as "tests" rather than
"morphisms" needs to be revised.

**Deliverable**: Rewrite the monad section of
`duality-and-composition.md`. Update `categorical-structures.md` §8
and `reference.md` to match.

---

### 2.2 Drop or substantiate Frobenius/spider terminology

**Review gap**: #6 (drop Frobenius terminology or state the equations)
**Files**: `categorical-structures.md` §8,
`duality-and-composition.md` (symmetry table)
**Difficulty**: Low — editorial

The review says calling fan and funnel "multiplication" and
"comultiplication" invites the Frobenius question, which we cannot
answer. Two options:

**Option A: State the Frobenius equation and check it.**
The equation is `(μ ⊗ id) ∘ (id ⊗ δ) = δ ∘ μ = (id ⊗ μ) ∘ (δ ⊗ id)`.
Operationally: fanning then partially funnelling should equal
funnelling then partially fanning. This is a strong condition that
may not hold — it would mean that running two committees on
overlapping scenario-sets and then merging results is equivalent to
first merging then running one committee. This seems unlikely to
hold in general.

**Option B: Drop the Frobenius/spider terminology.** Call them
"divergent" and "convergent" operations, or simply "fan" and "funnel."
Remove "multiplication" and "comultiplication" from the symmetry
table. Keep the string-diagram spider *visual* (it's descriptive)
but stop claiming algebraic structure we haven't verified.

**Recommendation**: Option B. The Frobenius structure is not doing
work for us, and claiming it creates expectations we cannot meet.
If we later discover it does hold, we can add it back with proof.

**Deliverable**: Edit `categorical-structures.md` §8 and
`duality-and-composition.md` symmetry table. Replace algebraic
terminology with operational terminology. Add a brief note
acknowledging that the spider structure is suggestive of Frobenius
algebra but that the equations have not been verified.

---

### 2.3 Downgrade equalizer/pullback/pushout sections

**Review gap**: #3 (unmaterialized morphisms), Warrant Table rows 7–8
**Files**: `categorical-structures.md` §6–7
**Difficulty**: Low — editorial

The review correctly notes that the "claim-extraction maps" and
"interpretation maps" in §6–7 do not exist as pipeline operations.
The text already half-acknowledges this ("they are *potential*
operations that the equalizer construction motivates defining"). We
need to make this fully explicit.

**A.** Retitle §6–7 or add a framing paragraph: "The following
sections describe categorical constructions that could be implemented
if the relevant morphisms were defined as pipeline operations. They
are design specifications — the categorical structure tells us what
operations *would be worth building* and what properties they should
have. They are not claims about what the current pipeline does."

**B.** For each construction, clearly state which morphisms would need
to exist and what defining them would involve. This turns §6–7 from
"aspirational mathematics" into "a categorical requirements spec" —
which is actually more useful to the target audience.

**Deliverable**: Revised §6–7 with explicit "design specification"
framing.

---

## Phase 3: Formalize the strongest claims

### 3.1 Formalize the scenario-set coproduct end-to-end

**Review gap**: #5 (formalize one limit construction), Warrant Table
row 5
**Files**: `categorical-structures.md` §5
**Difficulty**: Moderate — our best candidate for a fully rigorous
construction

The scenario-set coproduct is the review's recommended candidate for
a fully worked example because:

- The injections exist as concrete operations (each scenario is tagged
  with its source narrator and assumption-set).
- The universal property has a clear operational meaning (componentwise
  extension).
- The provenance metadata makes the injections *decorated*, connecting
  to Fong's framework.

The work:

**A.** Define the injections precisely: `ι_k : scenario_k → scenario-set`
is the operation that tags a scenario with its index, narrator, and
assumption-set, then includes it in the collected set.

**B.** State the universal property precisely: for any type X and
family of morphisms `f_k : scenario_k → X`, there exists a unique
(up to distributional equivalence) morphism `[f₁,...,f₄] : scenario-set → X`
such that `[f₁,...,f₄] ∘ ι_k = f_k` for each k. In the Markov
category setting, "unique up to distributional equivalence" means
equality of Markov kernels.

**C.** Show that the Map operation (which produces the decision-
landscape-map from the variance report) is an instance of the
universal property: it is defined componentwise on each resolution
in the coproduct, then uniquely extended.

**D.** If this works, note that it provides a template for
formalizing other constructions. If it doesn't (if the universal
property fails empirically), document what fails and why — that is
equally valuable information.

**Deliverable**: Rewritten §5 of `categorical-structures.md` with
full definitions, stated universal property, and explicit connection
to the Map operation.

---

### 3.2 Give "approximate" a metric

**Review gap**: #9 (give "approximate" a metric)
**Files**: `categorical-structures.md` §1 and §4
**Difficulty**: Moderate — requires choosing a distance

The review says "approximate product" is vacuous without a metric.
Options from the review:

- (a) Same support (too weak).
- (b) Same mean (inapplicable — artifacts aren't numeric).
- (c) Within ε in total variation distance (well-defined for
  distributions over artifacts, but requires a σ-algebra on artifact
  space).
- (d) Within ε in Wasserstein distance (requires a metric on artifact
  space).

**Recommendation**: Use a **domain-specific operational metric**
rather than importing a general-purpose distance. The Probe already
provides one: run the pipeline N times, extract the structural
features (recommendations, key claims, vote patterns), and measure
variance. The "distance from a true product" is the reconstruction
error: how much information is lost when you try to recover the
original inputs from the charter via the approximate projections.

Concretely:

**A.** Define reconstruction error for the charter-as-product:
`d(charter, product) = E[‖situation − π₁(DraftCharter(situation, scenarios))‖]`
where the norm is a rubric-based similarity score and the expectation
is over pipeline runs. If the charter were a true product, this would
be zero.

**B.** The Probe provides empirical samples of this error. The
variance report quantifies how far from zero it is.

**C.** State that "approximate product to within ε" means the
reconstruction error is below ε, and that ε is a design target
enforced by the charter rubric's completeness criterion.

**Deliverable**: New subsection in §1 or §4 of
`categorical-structures.md` defining the approximation metric.

---

## Phase 4: Develop the novel contributions

### 4.1 The Probe as statistical test of universal properties

**Review gap**: #8 (formalize the eigenform/Probe connection)
**Files**: `categorical-structures.md` §9
**Difficulty**: Nontrivial — potentially publishable

The review calls this "novel and potentially publishable as a short
note even without the rest of the formalism." The connection to make:

**A.** In the Markov category setting, an eigenform of a Markov
kernel is a stationary distribution — a distribution that is a fixed
point of the kernel.

**B.** The Probe runs the pipeline N times. The eigenforms are the
structural features present in every run. In the Markov category
framing, these are the components of the stationary distribution's
support.

**C.** The Probe is therefore a *Monte Carlo estimator of the
stationary distribution* of the pipeline-as-Markov-kernel. Running
it more times gives a better estimate. The variance report is an
empirical approximation of the stationary distribution's structure.

**D.** The categorical universal property (uniqueness of the
factoring map) corresponds to *unimodality* of the stationary
distribution: if the pipeline is a true product, there is one basin
in the decision landscape. Multiple basins indicate failure of the
universal property.

**E.** This connects to hypothesis testing: "is the pipeline a
product?" becomes "is the stationary distribution unimodal?", which
is a well-defined statistical question.

**Deliverable**: Expanded §9 of `categorical-structures.md` making
the Markov-kernel / stationary-distribution / Probe connection
explicit. Could later be extracted as a standalone short note.

---

### 4.2 Soft types as enriched presheaves (longer-term)

**Review gap**: Round 4 of the review (Frankie's analysis)
**Files**: New document or new section of `categorical-structures.md`
**Difficulty**: Nontrivial — requires new constructions

The review identifies three candidate formalizations of the soft type
system:

1. **Quantale-valued sheaves** — template is the underlying set,
   rubric is Q-valued membership, min-composition is the quantale
   multiplication. Works for scalar confidence; needs a product
   quantale for the vector case ([0,3]^5).

2. **Lawvere metric spaces** — rubric scores as distances from
   perfect type inhabitation, confidence propagation as triangle
   inequality.

3. **Probabilistic coherence spaces** — the template/rubric duality
   mirrors the web/coherence split. Speculative.

The furry-logic extension (distributional type membership) goes
further: type membership is a distribution over type-space, making
this a Giry-monad-valued type assignment. Composition of pipeline
operations is then composition of Markov kernels on type-space,
connecting directly to Fritz's framework.

**This is the most promising direction for a novel mathematical
contribution**, but it is also the most work. Defer to Phase 4 — do
the foundations first.

**Deliverable** (eventual): New document `soft-type-theory.md`
developing the formal structure. Start with the quantale-valued
sheaf interpretation (simplest), then extend to the distributional
case.

---

## Phase 5: Integration and consistency

### 5.1 Integrate the three categorical layers

**Review gap**: #10 (integrate enrichment, Kleisli, and
distributional layers)
**Files**: All palgebra documents; may warrant a new "architecture"
section in `categorical-structures.md`
**Difficulty**: Moderate — organizational, not technically hard once
Phases 1–3 are done

The review notes that the corpus presents three categorical
perspectives without explaining how they relate. The layering should
be made explicit:

1. **Base category**: Text with deterministic operations (templates,
   structural transformations).
2. **Markov category**: Text with stochastic operations (the main
   working category after Phase 1.2).
3. **Enriched over confidence lattice**: the Markov category enriched
   over V = ({L,M,H}, min, H) to track quality propagation.

State explicitly that these are compatible layers of a single
framework, not parallel stories. The Markov category structure
(Phase 1.2) handles stochasticity. The enrichment (Phase 1.3)
handles quality tracking. Together they give a Markov category
enriched over a quantale — a well-defined mathematical object.

**Deliverable**: New §2b in `categorical-structures.md`: "The layered
structure of Text." Update cross-references in all documents to point
to this section.

---

### 5.2 Propagate the "approximate" caveat consistently

**Review gap**: Tammy's Round 2 assessment (upward drift of claims)
**Files**: All palgebra documents
**Difficulty**: Low — editorial pass

The review notes that each successive document claims stronger
categorical properties without back-porting the qualifications. After
Phases 1–3, some qualifications become unnecessary (the Markov
category framing makes "approximate" precise). But where claims
remain approximate, the qualifier must be present.

**Deliverable**: Editorial pass across all documents. Ensure that
every categorical claim is either (a) made precise by the Markov
category framing, or (b) explicitly qualified with the approximation
metric from Phase 3.2.

---

## Phase 6: Bibliography and engagement

### 6.1 Add missing citations and deepen engagement

**Review gap**: #7 (missing citations), Recommended Reading List
**Files**: References sections of all documents
**Difficulty**: Low per citation, but there are several

Citations to add (beyond Fritz, already done ✓):

- [x] **Cho, K. and Jacobs, B.** "Disintegration and Bayesian
  inversion via string diagrams." *MSCS* 29(7), 2019. — For the
  distributional type membership question.
- [x] **Perrone, P.** "Markov categories and entropy." *IEEE Trans.
  Information Theory* 70(3), 2024. — Extends Fritz to information
  loss; connects to confidence degradation.
- [x] **Kock, A.** "Monads on symmetric monoidal closed categories."
  *Archiv der Mathematik* 21, 1970. — Commutative monads; required
  for Kleisli products.
- [x] **Heunen, C., Kammar, O., Staton, S., and Yang, H.** "A
  convenient category for higher-order probability theory." *LICS
  2017.* — Quasi-Borel spaces; potential ambient category for Text.

Citations where deeper engagement is needed (already cited but
under-engaged):

- [x] **Fong (2016)** — Engage with the pushout construction that
  makes decorated cospans work, not just cite the thesis.
- [x] **Kelly (1982)** — Engage with the enrichment axioms
  specifically, not just cite the book.

**Deliverable**: Updated references sections. For Fong and Kelly,
add specific section/theorem references and explain what we import.

---

## Execution order

```
Phase 1 (Foundations) — do first, in order:
  1.1  Define Text precisely         ✓ Complete (§2)
  1.2  Markov category treatment     ✓ Complete (§2a), verified against Fritz
  1.3  Enrichment base               ✓ Complete (§2b)

Phase 2 (Honest downgrades) — can mostly parallelize:
  2.1  Decision monad                ✓ Complete (duality-and-composition.md)
  2.2  Frobenius terminology         ✓ Complete (§8)
  2.3  Equalizer/pullback framing    ✓ Complete (§6–7)

Phase 3 (Formalize strongest claims):
  3.1  Coproduct end-to-end          ✓ Complete (§5), verified against Fritz
  3.2  Approximation metric          ✓ Complete (§4.1), verified against Fritz

Phase 4 (Novel contributions):
  4.1  Probe as statistical test     ✓ Complete (§9), verified against Fritz
  4.2  Soft type theory              ✓ Complete (soft-type-theory.md)

Phase 5 (Integration):
  5.1  Layer integration             ✓ Complete (§2c — three-layer architecture)
  5.2  Editorial consistency pass    ✓ Complete (2026-03-13)

Phase 6 (Bibliography):
  6.1  Citations and engagement      ✓ Complete (all citations added,
                                     Fong and Kelly engagement deepened)
```

---

## What not to do (from the review)

The review explicitly warns against two rabbit holes:

1. **Don't formalize equalizers/pullbacks until the claim-extraction
   maps exist as pipeline operations.** §6–7 are currently
   aspirational. Formalizing aspirations is waste. (Phase 2.3 handles
   this by reframing them as design specifications.)

2. **Don't try to make the Frobenius structure work unless the fan and
   funnel actually satisfy the Frobenius equations.** Just drop the
   terminology. (Phase 2.2 handles this.)

Additionally: don't try to resolve everything at once. The review
recommends presenting the novel elements (soft types, Probe,
operational monad-law tests) as the main contribution, with
categorical precision as a work in progress. The formalization in
Phases 1–3 is the minimum viable precision for credibility. Phases
4–5 are where the real contributions emerge.
