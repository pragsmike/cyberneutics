# Bradley's Magnitude Paper, the Tropical Thread, and the Closure Insight

What started as a question about how Bradley's thesis work connects to the
categorifications in cyberneutics turned into something more specific once the
IPAM/UCLA talk (November 2024) was identified as presenting the
Bradley-Vigneaux paper "The Magnitude of Categories of Texts Enriched by
Language Models" (TAC 44, 2025). Then the conversation took an unexpected turn
into the internal structure of Text itself.

## The enrichment coincidence

Bradley-Vigneaux and cyberneutics both build enriched categories over text, but
with different bases for different purposes. Bradley enriches over [0,1] with
multiplication — objects are strings, hom-objects are conditional probabilities
P(y|x) from LLM next-token predictions. This is syntactic: what goes with what.
Cyberneutics enriches over V = ({Low, Medium, High}, min, High) — objects are
pipeline artifacts, hom-objects are confidence levels. This is operational: how
reliably one stage transforms one type into another.

The gap between them is where the work is. But Bradley's geometric move —
applying −ln to pass from [0,1] to [0,∞], turning probabilities into distances
in a generalized metric space — has a direct parallel. The Leinster magnitude
paper was already in the recommended reading. Bradley-Vigneaux now gives a
*computed example* of that machinery applied to LLM text.

Multiple enrichments over the same base category is standard — Kelly's framework
doesn't require a single enrichment. Text as a bare category has objects and
morphisms. You can enrich over [0,1] for transition probabilities, over V for
confidence, over V₅ for vector rubric scores, over [0,∞] for the metric
picture. These don't compete; they coexist, connected by change-of-base
functors (−ln is exactly such a functor).

## The tropical observation

Bradley passes through −ln to get from probabilities to distances and land in
[0,∞]-enriched territory, where tropical geometry applies (Vlassopoulos and
Gaubert, 2024, found the connection).

But cyberneutics' min-lattice enrichment is *already tropical*. The confidence
propagation rule — confidence(g ∘ f) = min(confidence(f), confidence(g)) — is
tropical multiplication. The product quantale V₅ with componentwise min is a
tropical semiring. This isn't an analogy. It's a literal instance. Cyberneutics
lives in the tropical world without needing the logarithmic passage that
Bradley uses to get there from the probability world.

Whether this means cyberneutics is "further along" or "missing a step" (the
probabilistic layer pre-logarithm may contain information the tropical layer
loses) is an open question. If the calibration register accumulates enough run
data, you could in principle estimate the conditional probabilities and build
the [0,1]-enriched category empirically, then the min-lattice becomes a
coarsening of a richer structure rather than the ground truth.

## Magnitude as pipeline diagnostic

The talk's headline result: the magnitude function of the text category recovers
Shannon entropies of the LLM's conditional distributions. Magnitude as
partition function.

If you modeled the committee pipeline as a Bradley-Vigneaux enriched category —
objects are pipeline states, morphisms weighted by conditional probabilities of
one stage producing outputs feeding the next — then magnitude would be an
aggregate entropy measure of the pipeline. High magnitude = large effective
output space. Low magnitude = collapsing to a small region. A stabilised
pipeline (eigenform found) should have lower magnitude than an unstabilised one.
The calibration register could track magnitude across runs as a single scalar
summary.

## Yoneda and soft types

Bradley makes the Firth/Yoneda connection explicit: the meaning of a string is
the totality of its relationships to all other strings, packaged as a
representable functor. The enriched Yoneda embedding sends each string to its
semantic profile.

The soft type system does something structurally analogous at the document level.
The type membership of an artifact is determined by how it scores against all
rubric criteria — by how it relates to templates. The presheaf F_a : T^op → V is
already a presheaf, so Yoneda machinery applies. But the enrichment base differs
(V vs [0,1]), which means the semantic structure in the copresheaf category
differs. Both copresheaf categories are complete and cocomplete (V is a
commutative quantale), but the operations are min-based rather than
multiplication-based. Whether this difference matters operationally is open.

## The terminological collision

There's a collision between "enrichment" in the SWE/enterprise-architecture
sense and "enrichment" in Kelly's sense. The architecture documents use
"enrichment morphism" to mean a pipeline stage that adds metadata without
changing the payload (ScoreEvidence, Evaluate, SecurityGate). Kelly uses
"enrichment" to mean replacing hom-sets with hom-objects valued in a monoidal
category — attaching data to arrows, not to objects.

These operate on different parts of the categorical structure. The SWE
enrichments are morphisms in Text that update the presheaf layer (the metadata
decoration on objects). The Kelly enrichment attaches data to hom-objects
(the spaces between objects). You need both, and they interact: the enrichment
tells you how confidence propagates through composition, the presheaf tells you
what type profile each artifact carries, and the compatibility condition is that
composition in the enriched category acts correctly on the presheaf values.

The architecture docs present these as parallel stories. They aren't. They're
two kinds of decoration on the same base category.

## The closure insight

If Text is closed — and it is, because hom-objects are themselves texts — then
the Kelly enrichment and the presheaf layer unify.

A confidence assessment of a pipeline stage is itself a text artifact. A
calibration report, a rubric evaluation, a track record summary. It's not an
abstract value floating outside the category. It's a document. It lives in Text.
It has a type profile. It can be scored by rubrics.

The presheaf machinery applies to hom-objects. You can evaluate how well a
calibration report inhabits its own type. You can score the scoring.

This means the Kelly enrichment (confidence on morphisms) is *derived from*
presheaf evaluation applied to the hom-object. The three-element lattice V is a
coarsening — a summary statistic extracted from the richer presheaf data on the
calibration record that lives at Hom(A, B).

The self-referential loop: calibration records are artifacts, subject to the same
type discipline as everything else. System 3* (the audit channel) works because
audit records are objects of Text evaluated by the same presheaf machinery.

The recursion bottoms out empirically, not formally. Formally you get an infinite
tower of meta-assessments. Practically, you stop when the presheaf values
stabilise — when scoring the scoring produces the same confidence as scoring
alone. That's the eigenform. Von Foerster's fixed point, realised as a fixed
point of the presheaf applied to its own hom-objects.

The SDT metacognition framing connects here too. The meta-d'/d' ratio — how well
a committee character knows what it knows — measures the quality of the
hom-object. A character with high metacognitive accuracy produces calibration
records whose presheaf values are high. The noise figure for self-knowledge *is*
the presheaf evaluation of the internal hom.

## Morphisms as texts

The implementation payoff: every morphism in Text is specified by a text. That
text is either a prompt (stochastic — the LLM interprets it) or a script
(deterministic — a runtime executes it). Both are artifacts. Both live in Text.
Both have type profiles. Both can be versioned, diffed, reviewed, scored.

The specification of a transformation and the transformation itself are both
objects of the same category. No separate metalanguage needed. The pipeline
description *is* pipeline data.

For verification: comparing a specification (prompt or script) against its output
is a morphism in Text. The evaluation of that comparison is a presheaf value.
Everything stays inside the category. The verification framework is a subsystem
of the thing being verified.

The deterministic/stochastic distinction maps onto Fritz's partition. Scripts are
deterministic morphisms (Text_det, genuine products, copy-respecting). Prompts
are genuinely stochastic (correlated but distinct outputs on repeated runs).
Both are specified by files. Both are versioned in git. Both are evaluated by
rubrics. Both are tracked by the calibration register. The only difference is
execution semantics — LLM endpoint vs runtime. The categorical formalism says
this is the right abstraction boundary.

## The Vickers-Faith-Rossiter semiotic paper

While tracing papers from the old ACT study group list, identified Vickers,
Faith, and Rossiter, "Understanding Visualization: A Formal Approach using
Category Theory and Semiotics" (IEEE TVCG 19(6), 2013, arXiv:1311.4376). It
renders the Peircean semiotic triad (object → representamen → interpretant) as a
commutative diagram and uses morphism properties to formally define visualization
concepts.

The resonance: the organ regime pipeline is a semiotic chain (situation →
charter → deliberation). The bloodstream's unprovenanced-text problem is a
broken triad. Type-spoofing is a semiotic pathology: the sign's form is intact
but its reference has been rewired.

## Papers to add

Compiled a reference list of 28 papers, 11 new to the corpus. Full list with
annotations in `references/bradley-cyberneutics-references.md`.

## What this means for the architecture documents

The closure insight — that the presheaf layer and the Kelly enrichment layer are
one story, not two, because hom-objects are objects — is not stated anywhere in
the current palgebra documents. `categorical-structures.md` develops them in
separate sections (§2b for enrichment, soft-type-theory.md for presheaves)
without a crisp statement of their unification. The terminological collision
("enrichment" meaning two different things) actively obscures the relationship.

The morphisms-as-texts observation — that prompt files and scripts are themselves
objects of Text, making the pipeline self-applicable — is implicit in the
implementation but never stated as a design principle. It's the engineering
answer to "why should I care about the formalism?"

Both insights require revisions to the architecture documents, but light ones.
The formal machinery is already in place. What's missing is a paragraph or
section that states the unification and draws the engineering consequences.
