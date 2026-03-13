# Categorical Structures in Cyberneutics

*A treatment of the basic category-theoretic constructions as they appear in
narrative computing pipelines, in pedagogical order.*

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

Two foundational commitments follow from this:

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

---

## 2. Objects and Morphisms

In the category **Text**, objects are *soft types*: `(template, rubric)` pairs
that define what a well-formed artifact of a given kind looks like. The template
is structural (required sections, metadata fields); the rubric is semantic
(quality criteria evaluated by scoring). Objects include types such as
`situation`, `charter`, `scenario-set`, `transcript`, and `resolution`.

Morphisms are *pipeline operations*: typed transformations that consume input
artifacts and produce output artifacts. The morphism

```
Deliberate : charter × scenario-set × roster → transcript
```

takes three inputs and produces one output. The annotation `{catalytic: roster}`
marks the roster as non-consumed — it participates in the transformation without
being altered, a dashed wire in the string diagram.

Two morphism kinds are distinguished:

- **Transformations** produce genuinely new content. The transcript is not a
  rearrangement of the charter; it is new material generated through
  deliberation.
- **Enrichments** update only the metadata of an existing artifact. Scoring a
  transcript against an evaluation rubric adds a confidence score to its front
  matter without changing its text. Enrichments are idempotent and
  re-runnable; transformations are not.

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
palgebra resource equations is the morphism from C to Unit.

An **initial object** 0 has exactly one morphism from it to every object X.
It is the universal source — anything can be generated from it, which means
nothing is constrained.

The *empty prompt* (or maximally ambiguous situation description) is initial:
every text is reachable from it because no consistency constraint rules anything
out. This is why the quality of the fan's input situation matters so much. A
poorly framed situation is close to initial — the narrators have no surface to
push against, and the scenarios they generate are unconstrained artifacts rather
than genuine explorations of a determinate possibility space.

In type-theoretic terms, `False` (⊥) is the initial type: from an incoherent
premise, any conclusion follows. The practical analog is a charter that contains
a contradiction: a committee chartered on inconsistent premises can justify any
resolution, which is precisely no justification at all.

---

## 4. Products

The **product** A × B of two objects comes with *projection morphisms*
π₁: A × B → A and π₂: A × B → B. Its universal property states: any object X
equipped with maps f: X → A and g: X → B factors uniquely through A × B via the
pairing ⟨f, g⟩: X → A × B. The product is the *minimal object* from which both
A and B are recoverable.

**The charter as product of situation and scenario-set.** The charter carries
both the framed problem and the scenario context into the deliberation. Its two
projections recover the original situation (strip the scenarios) and the
scenario-set (strip the problem framing). Any pipeline operation needing both —
the Deliberate operation most prominently — routes through the charter. This is
not merely organisational: if the charter garbles one of its projections, the
downstream operation is working in a degraded product, and provenance breaks.

**The transcript as product of character positions.** The deliberation transcript
is the product of all five character position-streams. Each character's
contribution is a projection: π_Maya: transcript → Maya's position record, and
so on for Frankie, Joe, Vic, and Tammy. The universal property of the product
says that any operation reasoning about what a character said must route through
the transcript. A transcript that summarises rather than records is a *lossy*
product: the projections are no longer faithful, and auditability is lost. This
is why the palgebra insists transcripts are full records.

---

## 5. Coproducts

The **coproduct** A + B comes with *injection morphisms* i₁: A → A + B and
i₂: B → A + B. Its universal property states: any object X equipped with maps
f: A → X and g: B → X factors uniquely through A + B via [f, g]: A + B → X.
The coproduct is a *disjoint union that retains provenance* — each element
remembers which component it came from.

**The scenario-set as coproduct of scenarios.** The fan produces four scenarios
(Continuity, Disruption, Opportunity, Constraint). Their coproduct is the
`scenario-set`:

```
scenario-set = scenario_C + scenario_D + scenario_O + scenario_K
```

Each injection carries metadata: the source narrator, the assumption-set, the
divergence axis. This is the *decorated coproduct* — the injections are not bare
inclusions but carry the provenance annotations that make scenarios
distinguishable in committee deliberation. When Fong's decorated cospans appear
in the palgebra formalism, this is the operative site: the decorations on the
injection morphisms are exactly the assumption-annotations.

The universal property has direct operational significance: any pipeline
operation that handles the full scenario-set — coverage assessment, charter
drafting, committee deliberation — can be defined *componentwise* (by specifying
what it does with each scenario) and uniquely extended to the full set. This is
what licenses the committee's scenario-by-scenario reasoning as a valid method
for producing a resolution about the whole set.

**The variance report as coproduct of Probe runs.** Across N runs of the
composed fan → funnel pipeline, each resolution is an injection into the
variance report:

```
variance-report = resolution_1 + resolution_2 + ... + resolution_N
```

The Map operation is the unique morphism out of this coproduct into the
decision-landscape-map type. If the coproduct has one non-trivial component
class (all resolutions isomorphic), the decision landscape has one basin. If it
has multiple non-isomorphic component classes, there are multiple basins and the
ridge structure requires examination before commitment.

---

## 6. Equalizers and Coequalizers

Given two morphisms f, g: A → B, their **equalizer** is an object E with a map
e: E → A such that f ∘ e = g ∘ e, universal among all such objects. The
equalizer picks out the *subobject of A where f and g agree*.

**Cross-scenario triangulation.** Let A be a collection of situation
descriptions, B the space of factual claims, and let f and g be the
claim-extraction maps of two different narrators. The equalizer E is the
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
interpretation maps from shared evidence. The coequalizer Q is the resolution
that identifies f(a) and g(a) for every situation a — the text in which the
distinction between the two characters' framings has been absorbed into a
justified commitment.

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

---

## 8. Fan and Funnel as Coproduct and Product Spiders

The two core pipeline operations are *spiders* in the string diagram calculus:
nodes of higher arity that generalise the basic binary product and coproduct.

**The fan (coproduct spider / one-to-many)** injects a single situation into
multiple distinct narrative contexts:

```
situation × params → scenario_1 + scenario_2 + scenario_3 + scenario_4  [Fan]
  {catalytic: params}
```

Each injection carries the source narrator's lens as a decoration. The fan is
the divergent half of the pipeline: it releases the ambiguity of the situation
into an explicitly structured space of possibilities. The universal property of
the resulting coproduct licenses componentwise reasoning downstream.

**The funnel (product spider / many-to-one)** combines multiple inputs into a
single committed output:

```
charter × scenario-set × roster × character-propensities × roberts-rules → transcript  [Deliberate]
  {catalytic: character-propensities, roberts-rules}
```

The resolution is the product of all the perspectives that contributed to it;
each character's position is recoverable via projection. The funnel is the
convergent half: it collapses the coproduct of perspectives into a committed
product with recoverable provenance.

**Composition: the deliberated choice.** Fan → funnel is the *decision monad*:

```
M(situation) = Funnel(Fan(situation))
```

The monad laws are operational quality criteria. The unit law: fanning and
immediately collapsing without deliberation should return approximately the
original situation — the pipeline added nothing. The associativity law: nested
fan-funnel-fan-funnel should be equivalent to a single well-designed fan-funnel.
Both are testable by running the pipeline with degraded deliberation and
comparing output to input.

---

## 9. The Probe as Empirical Universal Property Test

The strict categorical product and coproduct satisfy their universal properties
*uniquely up to isomorphism*. In practice the pipeline only approximately
satisfies them: different model temperatures, ordering effects, and prompt
variations mean there is not a unique "correct" transcript or a single
determinate coproduct of scenarios. The pipeline constructs *a* product, not
*the* product.

The **Probe** operation — running the composed pipeline N times from the same
inputs — is the empirical test of how close the funnel comes to a genuine
categorical product. Its output is a variance report: the coproduct of N
resolutions. The Map operation synthesises this into a decision-landscape-map
with basins (resolution-types that recur), ridges (boundaries where small input
variations flip outcomes), and load-bearing assumptions (parameters whose
variation produces basin-crossings).

**Eigenforms** are the resolution-content present in every Probe run: the
invariant sub-structure that the funnel reliably produces, regardless of
trajectory. Eigenforms correspond to the "truly universal" part of the product —
the content no morphism out of the product can fail to factor through.
**Residues** are run-specific content: the trajectory-dependent part that
reflects particular deliberation dynamics rather than the structure of the
situation. The Probe separates these empirically, which is what Deleuzian
repetition does philosophically: difference produced by repetition reveals the
topology of the space.

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
University of Oxford, 2016. — Decorated cospans for composing open systems;
grounds the treatment of pipeline operations as open systems with input/output
interfaces.

**Kelly, G. Maxwell.** *Basic Concepts of Enriched Category Theory.* Cambridge
University Press, 1982. — Foundation for enrichment over confidence lattices;
the theoretical basis for quality-score propagation through composition.

**Baez, John, and Mike Stay.** "Physics, Topology, Logic and Computation: A
Rosetta Stone." In *New Structures for Physics*, ed. B. Coecke. Springer, 2011.
— String diagrams as a unified language across physics, logic, and computation.

**De Wynter, Adrian, et al.** "On Meta-Prompting." arXiv:2312.06562, 2023. —
Category-theoretic framework for LLM interactions; models prompt-response pairs
as morphisms and proves equivalence results for meta-prompting strategies.
