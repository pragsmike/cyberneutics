# Decorated Texts: A Resource-Theoretic View of LLM Pipelines

## From pie to pipeline

The diagram below is from Fong and Spivak's *Seven Sketches in
Compositionality*. It shows how to make a lemon meringue pie.

![Resource diagram for lemon meringue pie](assets/lemon-meringue-pie.png)

These resource equations are equivalent and isomorphic to that diagram:

```
egg → yolk + white + egg-shells  [SeparateEgg]  {discard: egg-shells}
lemon × butter × sugar × yolk → lemon-filling + lemon-peel + butter-wrapper  [MakeLemonFilling]  {discard: lemon-peel, butter-wrapper}
white × sugar → meringue  [MakeMeringue]
crust × lemon-filling → unbaked-lemon-pie  [FillCrust]
unbaked-lemon-pie × meringue → unbaked-pie  [AddMeringue]
```

Read this as a set of resource equations. Each line is an operation
(a box in the string diagram). The things flowing between boxes are
typed resources — ingredients, intermediate products, waste. The `×`
is "and" (you need all these inputs together). The `+` is "or"
(the operation produces these distinct outputs). Waste streams
(egg shells, lemon peel) flow to discard.

The string diagram and the equations carry the same information. Given
either representation, you can mechanically derive the other. They are
isomorphic descriptions of the same process.

We built an LLM-driven text-processing pipeline — a trade study
pipeline — using exactly this formalism, with resource equations
as the canonical specification and string diagrams as the visual
rendering. After several weeks of iterative development, we found
ourselves needing to say more than the basic equations could express.
This essay describes what we found and the formalism we developed to
capture it.

## The basic algebra

An LLM is a text transformer, parameterized by a prompt. An agent
pipeline is a composition of such transformers, wired together so that
the output of one becomes the input of the next. If we define data
types as certain kinds of texts, and operations as prompted
transformations between them, we get an algebra:

- **Types** (objects) are named kinds of text artifacts.
- **Operations** (morphisms) are named transformations, each specified
  by a prompt text.
- **×** (cross product) means "all of these inputs together."
- **→** means "this operation produces that output."
- **Composition** (sequential wiring) is: if `f : A → B` and
  `g : B → C`, then `g ∘ f : A → C`.

This is a symmetric monoidal category. The string diagram is its
standard visual representation. The resource equations are its
term language. They are the same thing in different notation, just as a
circuit schematic and its netlist are the same circuit.

## A simplified evaluation pipeline

Here is a simplified version of our trade study pipeline, reduced to
the essential operations while preserving every structural feature we
need to discuss:

```
# 1. Extract preference signals from experience reports
experience-reports → preference-signals  [ExtractPreferences]

# 2. Assemble candidate list from preferences, use cases, and guides
preference-signals × use-cases × guides → candidates  [AssembleCandidates]  {catalytic: use-cases, guides}

# 3. Gather evidence for each candidate
candidates × evidence-template × guides → evidence  [GatherEvidence]  {catalytic: evidence-template, guides}

# 4. Score evidence quality (enrichment — same artifact, new metadata)
evidence × evidence-rubric → evidence  [ScoreEvidence]  {catalytic: evidence-rubric; enriches: scores}

# 5. Security gate — sort into accepted and rejected
evidence × security-criteria → accepted-evidence + rejected-evidence  [SecurityGate]  {catalytic: security-criteria; discard: rejected-evidence}

# 6. Produce findings from accepted evidence
accepted-evidence × preference-signals × findings-template → findings  [DraftFindings]  {catalytic: findings-template}

# 7. Aggregate findings into a recommendation
findings × rollup-template → rollup  [SynthesizeRollup]  {catalytic: rollup-template}

# 8. Feed learnings back into experience reports
rollup → experience-reports  [UpdatePreferences]  {feedback: experience-reports→experience-reports}
```

Eight operations, demonstrating:

- **Simple transformation** (arrows 1, 3, 6, 7): inputs are consumed,
  outputs are new artifacts.
- **Catalytic inputs** (arrows 2, 3, 5, 6, 7): guides, templates,
  rubrics, and criteria participate without being consumed. In the
  string diagram they appear as dashed wires. Algebraically, they are
  comonoid objects — equipped with a copy map that lets them feed into
  multiple operations.
- **Enrichment** (arrow 4): the evidence artifact goes in and comes out
  structurally unchanged, but now carries quality scores in its
  metadata. The operation is an endomorphism that decorates rather than
  transforms.
- **Coproduct with discard** (arrow 5): the security gate sorts
  evidence into two streams. Accepted evidence flows forward; rejected
  evidence flows to a waste sink. This is the coproduct — dual to the
  cross product.
- **Feedback loop** (arrow 8): the rollup's learnings feed back into
  the experience reports, closing the cycle for the next refresh. This
  is traced monoidal structure.

## What the basic algebra doesn't capture

We arrived at this pipeline iteratively. The initial version had just
operations and types — inputs, outputs, composition. It worked, but we
observed problems:

**Drift.** Operations would produce outputs that gradually deviated from
what downstream operations expected. An evidence file might omit a
section that the findings operation needed. The structural contract
between operations was implicit and eroded over time.

**Invisible quality.** A findings document might look structurally
correct — all the right sections, all the right headers — but contain
unsupported claims. The *shape* was right but the *substance* was weak.
Nothing in the basic type system could express this.

**Lost provenance.** When the rollup made a recommendation, we couldn't
trace it back through the chain to the original evidence. The causal
history was in the analyst's head, not in the artifacts.

These problems led us to introduce templates (structural constraints on
types) and rubrics (quality evaluation of artifacts), and eventually to
recognize that both, along with provenance metadata, are *decorations*
on the artifacts — additional information that flows through the
pipeline alongside the primary content.

## Templates and rubrics: soft types

A type in our algebra is not a simple label. It is a pair:

```
type = (template, rubric)
```

The **template** defines the structural shape of a valid artifact:
required sections, heading hierarchy, required metadata fields, link
targets. It is almost a grammar — you could write a parser for the
structural part.

The **rubric** defines the quality criteria for a good artifact: "claims
are evidence-backed," "preference evidence is distinct from scoring
judgment," "evidence gaps are listed with impact." These are semantic
judgments. No parser can evaluate them. An LLM can, probabilistically.

An artifact *inhabits* the type if it passes both checks. But
inhabitation is not binary. The rubric returns a *score* — 0 through 3
per criterion, rolling up to a confidence band (High, Medium, Low). An
evidence file doesn't simply inhabit or fail to inhabit the type
`evidence`. It inhabits it *to a degree*.

This is a fuzzy type system. The template defines the support (what
could possibly be a member). The rubric defines the membership function
(how well any particular artifact actually inhabits the type). Confidence
bands are level sets of the membership function. The human review gates
are threshold checks: proceed only if the membership grade exceeds a
minimum on every criterion.

In algebraic terms, this type-checking operation is a morphism that
produces both a score and enriched metadata. If we write a soft type as
τ = (template, rubric), then type-checking is not a boolean predicate but
a score-producing map:

```
check_τ : (t, m) ↦ (t, m ⊔ {type := τ, fit := s, violations := ...})
```

The payload `t` passes through unchanged. The metadata `m` is enriched
(via the join operator `⊔`) with the type annotation, the fit score `s`,
and any violations the rubric detected. This is an enrichment morphism:
the artifact gains type information without transforming its content.

## The decorated text model

The insight that unifies all of this is that pipeline artifacts are
*decorated texts*. Every artifact has two parts:

```
artifact = (payload, metadata)
```

The **payload** is the primary text content — the evidence narrative,
the findings analysis, the rollup recommendation. This is what a human
reader cares about.

The **metadata** is a structured record of decorations accumulated as
the artifact moves through the pipeline: type information, quality
scores, provenance links, gate results, processing timestamps.

We encode this physically using YAML front matter:

```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  source-coverage: 2
  security-completeness: 3
  p0-probe-coverage: 2
  preference-integration: 1
  overall-confidence: Medium
gate:
  security: Blue
  conditions: []
provenance:
  gathered-by: DraftCandidateEvidence
  scored-by: ScoreEvidenceQuality
  sources:
    - vendor-trust-center
    - community-reports
  cycle: 5
---

## Vendor Facts

Cursor provides an AI-augmented code editor built on VS Code...
```

The `---` delimiter is the product projector. Everything above it is
`Meta`. Everything below it is `Text`. The artifact is literally
`Text × Meta` in the file format. The format is the functor.

## Three kinds of decoration

Three distinct kinds of information ride on the metadata, each with its
own propagation rules:

**Confidence** measures how well the artifact inhabits its type. It is
produced by rubric-scoring operations (enrichment morphisms) and
propagates forward monotonically — it can only degrade. You cannot
manufacture confidence you don't have. A Medium-confidence evidence file
cannot produce a High-confidence finding, no matter how good the
findings operation is. This is analogous to the propagation of
measurement uncertainty in physics: every operation introduces noise, and
the uncertainties accumulate through composition.

```yaml
scores:
  overall-confidence: Medium
  # Downstream findings will carry: evidence-confidence: Medium
  # The finding's own confidence cannot exceed this ceiling
```

**Provenance** records where the artifact came from and what processing
it has undergone. It accumulates — each operation adds to the chain
without erasing prior links. This is the traceability requirement: every
claim in findings must trace to evidence, which must trace to sources.

```yaml
provenance:
  gathered-by: GatherEvidence
  scored-by: ScoreEvidence
  sources:
    - vendor-trust-center
    - community-forum-reports
```

**Content** is the payload text itself. It transforms — operations
read it and produce new text. Unlike the other two decorations, content
doesn't propagate as metadata; it *is* the payload, and the metadata
rides alongside it.

These three decorations have different algebraic behavior:

| Decoration | Propagation rule | Analogy |
|------------|-----------------|---------|
| Confidence | Monotone decrease (can only degrade) | Measurement error accumulation |
| Provenance | Monotone increase (only appends) | Chain of custody |
| Content | Transformation (may change entirely) | Signal through a filter |

### Score combination structures

The monotone degradation of confidence is a specific algebraic choice.
More precisely, confidence scores form a lattice where composition takes
the minimum (greatest lower bound). This ensures quality can only degrade
through the pipeline: a Medium-confidence evidence file cannot produce a
High-confidence finding.

But other scoring strategies are possible, each with different monoidal
structure:

**Lattice-style (max/min):** Scores combine by taking the supremum or
infimum. This is appropriate when quality is bounded: the weakest link
determines overall quality, or the strongest signal dominates. Confidence
degradation uses min-lattice structure.

**Semiring-style (weighted sums):** Scores combine additively with
weights. This is appropriate when contributions are cumulative: multiple
weak signals can add up to a strong conclusion, or costs accumulate
across operations. Cost accounting and evidence aggregation often use
semiring structure.

**Pareto-style (multi-objective frontiers):** Scores are vectors, and
combination preserves the Pareto frontier. This is appropriate when
criteria are incommensurable: you cannot trade off security against
usability on a single scale, so you track both and let human reviewers
choose from non-dominated options.

Different pipeline stages may use different combination rules. The rubric
application at line 159 chose the lattice structure (overall confidence
is the minimum across criteria), but a different pipeline might sum
weighted criterion scores or maintain a Pareto frontier of candidates.
The key insight is that these are monoidal structures: they compose
predictably, and the pipeline algebra tells you how scores flow through
composition.

## Two kinds of morphism

The decorated-text model reveals that pipeline operations fall into two
distinct classes:

**Transformation morphisms** change the payload:

```
f : (text, meta) ↦ (text', meta')
```

GatherEvidence reads candidate descriptions and produces evidence
narratives. DraftFindings reads evidence and produces findings.
SynthesizeRollup reads findings and produces a recommendation. These
are the *work* of the pipeline — new text is created.

**Enrichment morphisms** leave the payload unchanged and only modify the
metadata:

```
e : (text, meta) ↦ (text, meta ⊔ Δmeta)
```

ScoreEvidence reads the evidence body, evaluates it against the rubric,
and writes scores to the front matter. SecurityGate reads the evidence
body, evaluates security criteria, and writes a gate result to the front
matter. The body is untouched.

The `⊔` (join) operator merges metadata maps. It is associative and has
an identity (the empty map). When two enrichment operations write to
disjoint namespaces (e.g., one writes `scores.*` and another writes
`gate.*`), they commute — order doesn't matter. When they write to
overlapping namespaces, order matters and must be specified.

This distinction has practical consequences:

- Enrichment morphisms are safe to re-run (they're close to
  idempotent if the model and inputs are frozen).
- Enrichment morphisms that write to disjoint namespaces can be
  parallelized.
- Transformation morphisms generally can't be re-run without
  discarding their previous output.

The RFC 822 analogy is useful here. An email message passes through a
sequence of mail transfer agents. Each MTA adds `Received:` headers to
the message without touching the body. The headers accumulate the full
routing history. Our YAML front matter works the same way: pipeline
stages stamp their observations onto the artifact's header block, and
the body only changes when the operation's specific job is to produce
new text.

Or think of a manufacturing assembly line. Each station either works on
the part (transformation) or inspects it and updates the traveler
clipboard (enrichment). The traveler accompanies the workpiece through
the shop floor. At the end of the line, the traveler is the proof that
the workpiece was built correctly.

## Pipeline composition laws

Having distinguished these two morphism types, we can now state the laws
that govern their safe composition. These are not mathematical theorems
but operational principles — discipline that makes pipelines predictable
and maintainable.

**Monotone enrichment.** An enrichment step should only add or overwrite
keys within its declared namespace. For example, a step that scores
evidence quality writes to `scores.*` and nothing else; a security gate
writes to `gate.*` and nothing else. This namespace discipline makes
metadata merges predictable and compositional. When enrichment steps
respect namespace boundaries, they can be reordered or parallelized
without conflict. The RFC 822 analogy (lines 362-368) embodies this law:
each mail transfer agent adds its own `Received:` header without touching
anyone else's headers or the message body.

**Idempotence where possible.** If a step is deterministic given frozen
inputs — same rubric text, same model settings, same artifact — then
re-running it should not change the metadata. When this isn't true
(because the LLM is stochastic or the rubric has changed), store the
variance explicitly as structured data (e.g., `scores.helpfulness.samples:
[0.81, 0.83, 0.82]` for an ensemble). Idempotence makes enrichment steps
safe to re-run during debugging or pipeline repair. You can re-score an
artifact after tuning a rubric without cascading changes to unrelated
metadata.

**First-class step specifications.** Since pipeline operations are
specified by prompt texts, store each step's specification text alongside
its outputs in the provenance metadata. When you change a rubric or
template, that change is a diff in the spec text. This makes the pipeline
reproducible and auditable: you can see exactly what version of what
rubric produced a given score, and you can diff pipeline versions to
understand behavioral changes. The `type.rubric: evidence-rubric-v1`
field (line 447) is an instance of this law — it records which rubric
version was applied.

Taken together, these three laws ensure that enrichment composes cleanly.
Namespace discipline prevents accidental clobbers. Idempotence makes
steps rerunnable. First-class specs make the pipeline's behavior explicit
and diffable. They transform an LLM pipeline from an opaque sequence of
prompt calls into a system with the compositional properties we expect
from well-engineered software.

## Human gates as collapse operators

At several points in the pipeline, a human reviews the accumulated
metadata and makes a binary decision: proceed or stop. These human
gates are not ordinary operations. They collapse the graded uncertainty
of the enrichment decorations into a crisp commitment.

Before the gate, the artifact carries potential — quality scores,
confidence bands, conditions, caveats. After the gate, it carries a
decision: *this is the accepted short list*, *these are the approved
findings*, *we will pilot these tools*.

In the algebra, a human gate is a morphism from the enriched category
to the boolean category:

```
gate : (text, meta) ↦ proceed | halt
```

If `proceed`, the artifact continues through the pipeline with its
metadata intact plus a new decoration: `gate.human-approved: true`.
If `halt`, the artifact returns to an earlier stage for rework.

The gates serve a role analogous to measurement in physics: they
collapse a superposition of possible interpretations (this evidence
*might* be sufficient, this gate *might* pass) into a definite state.
They are also fixed points in the sense of second-order cybernetics —
the recursive self-observation of the pipeline (rubric scoring,
committee review, quality checks) reaches a fixed point not by
converging mathematically but by an act of human decision.

The pipeline cannot check its own output to arbitrary depth. Rubrics
check artifacts. Rubric-of-rubrics check whether rubrics are well
calibrated. But this tower must terminate somewhere. The human gates
are where it terminates: axioms that ground the recursive observation
and let the pipeline proceed on a settled foundation.

## The enrichment pipeline in detail

To make this concrete, here is what happens to a single evidence
artifact as it passes through the enrichment and gating stages.

**After GatherEvidence (transformation):**

```yaml
---
type:
  template: evidence-template-v2
provenance:
  created-by: GatherEvidence
  cycle: 5
---

## Vendor Facts
Cursor provides an AI-augmented code editor built on VS Code...

## Security Gate Facts
SOC 2 Type II certified. Data encrypted at rest and in transit...

## P0 Probe Coverage
Community reports indicate strong performance on agentic coding tasks...
```

The artifact exists. It has a type annotation and provenance. No scores
yet.

**After ScoreEvidence (enrichment):**

```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  source-coverage: 2
  security-completeness: 3
  p0-probe-coverage: 2
  preference-integration: 1
  overall-confidence: Medium
provenance:
  created-by: GatherEvidence
  scored-by: ScoreEvidence
  cycle: 5
---

## Vendor Facts
(unchanged)

## Security Gate Facts
(unchanged)

## P0 Probe Coverage
(unchanged)
```

The body is untouched. The front matter now carries quality scores and
a confidence band. The provenance chain records who scored it.

**After SecurityGate (enrichment + coproduct):**

```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  source-coverage: 2
  security-completeness: 3
  p0-probe-coverage: 2
  preference-integration: 1
  overall-confidence: Medium
gate:
  security: Blue
  conditions: []
  disposition: Evaluate
provenance:
  created-by: GatherEvidence
  scored-by: ScoreEvidence
  gated-by: SecurityGate
  cycle: 5
---

## Vendor Facts
(unchanged)

## Security Gate Facts
(unchanged)

## P0 Probe Coverage
(unchanged)
```

Still the same body. The front matter now additionally carries the gate
result. If the gate were Black, the artifact would be routed to the
discard sink (rejected-evidence) instead of flowing forward.

**After human review (collapse):**

```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  source-coverage: 2
  security-completeness: 3
  p0-probe-coverage: 2
  preference-integration: 1
  overall-confidence: Medium
gate:
  security: Blue
  conditions: []
  disposition: Evaluate
  human-approved: true
  approved-by: mg
  approved-date: 2026-02-16
provenance:
  created-by: GatherEvidence
  scored-by: ScoreEvidence
  gated-by: SecurityGate
  reviewed-by: human
  cycle: 5
---
```

One more stamp on the traveler. The artifact is now committed. It
flows forward to DraftFindings, carrying its full decoration history.

## Equations, diagrams, pipelines

We now have three representations of the same pipeline:

**Resource equations** — the term language:

```
experience-reports → preference-signals  [ExtractPreferences]
preference-signals × use-cases × guides → candidates  [AssembleCandidates]
...
```

**String diagrams** — the visual language. Operations are boxes, types
are wires, catalytic inputs are dashed, waste is red. Mechanically
derivable from the equations.

**Decorated artifact files** — the implementation. YAML front matter
carries metadata; the body carries content. Pipeline operations read
input files and produce output files, stamping the front matter as they
go.

These three are isomorphic. Given any one, you can derive the other
two. The equations tell you the types and their relationships. The
diagram shows the same topology visually. The files instantiate the
types as concrete artifacts with the metadata structure implied by the
equations.

The `{enriches: ...}` annotation in the equation language marks an
operation as an enrichment morphism — the file format makes this
concrete as "only the front matter changes." The `{catalytic: ...}`
annotation marks an input as not consumed — in the file format, the
catalytic input file is read but not modified. The `{discard: ...}`
annotation marks a waste output — in the file format, the rejected
artifact is moved to an archive directory.

## What this buys us

The point of this formalism is not mathematical elegance. It is
predictability.

When we build a new pipeline — for a client engagement, for internal
process, for a different kind of evaluation — we want to:

1. **Write the resource equations** for the pipeline, specifying types,
   operations, catalytic inputs, enrichments, gates, and feedback loops.
2. **Generate the string diagram** mechanically from the equations (we
   have a tool for this).
3. **Implement each operation** as a prompt template that reads input
   files and produces output files with appropriate front matter.
4. **Know in advance** where quality will degrade (wherever confidence
   propagates through a transformation), where parallelism is safe
   (wherever enrichment operations write to disjoint namespaces), and
   where human review is needed (wherever the pipeline's self-assessment
   reaches its limits).

The lemon meringue pie doesn't need rubrics — butter either is or
isn't butter. Text artifacts are different. They inhabit their types to
a degree, and that degree matters for everything downstream. The
decorated-text model makes this explicit: every artifact carries its
quality record, its provenance chain, and its gate history in its front
matter, and the algebra tells you how those decorations propagate
through composition.

No single representation captures everything. The equations capture
composition and typing. The diagram captures topology and dataflow. The
files capture the actual content and metadata. These are charts on the
same manifold — different views, each making different aspects visible,
consistent because the transition maps (the isomorphisms between
representations) are maintained. The observer — the engineer designing
the pipeline, the analyst running it, the leadership reviewing the
output — sees through whichever chart best serves their purpose.

## Related work

The ideas here draw on several threads that are developing in parallel.

**Category theory for LLM behavior.** De Wynter et al., "On
Meta-Prompting" (arXiv:2312.06562, 2023), propose a category-theoretic
framework for in-context learning and meta-prompting. They model LLM
interactions as morphisms in a category and prove equivalence results
for different meta-prompting strategies. Our work shares the categorical
vocabulary but focuses on a different level: not the internal mechanics
of a single LLM call, but the compositional structure of multi-step
pipelines built from many such calls. Their morphisms are individual
prompt-response pairs; ours are entire pipeline stages that consume and
produce document artifacts.

**Prompts as programs.** Liang et al., "Prompts Are Programs Too!"
(arXiv:2409.12447, 2024; accepted FSE 2025), interview 20 developers
and argue that prompt development is a distinct programming phenomenon.
They observe that prompt programmers develop mental models of the
foundation model's behavior rather than of code. This matches our
experience exactly: the operation specs in our pipeline are programs
written in prose, and debugging them requires understanding what the
model will do with the text, not what a compiler will do with syntax.
Their 15 observations about prompt programming practices provide
empirical grounding for what we are trying to formalize algebraically.

**String diagrams and monoidal categories.** Our visual and algebraic
language comes directly from Fong and Spivak, *Seven Sketches in
Compositionality* (2019), which introduces string diagrams for
symmetric monoidal categories in an applied setting. The lemon meringue
pie example is from their Chapter 2 on resource theories. Baez and
Stay, "Physics, Topology, Logic and Computation: A Rosetta Stone"
(2011), provides the broader context for why string diagrams, type
theories, and physical systems share the same categorical structure.

**Decorated cospans and open systems.** Fong, "The Algebra of Open and
Interconnected Systems" (PhD thesis, Oxford, 2016), develops decorated
cospans as a framework for composing open systems with internal
structure. Each of our pipeline operations is an open system in this
sense: it has an input interface (types consumed), an output interface
(types produced), and internal structure (the prompt, the procedure).
Composition is by gluing interfaces. We have not yet mapped our
formalism onto decorated cospans, but the fit appears natural.

**Enriched categories.** The confidence-propagation structure (quality
scores that can only degrade through composition) is an enrichment.
Kelly, *Basic Concepts of Enriched Category Theory* (1982), is the
standard reference. Our hom-sets carry not just "does this morphism
exist" but "at what confidence level does the output inhabit its type,"
which is precisely the data of enrichment over a confidence lattice.

**YAML front matter as metadata carrier.** The practice of embedding
structured metadata in document headers has extensive precedent in
static site generators (Jekyll, Hugo), document processors (Pandoc),
and knowledge management tools (Obsidian). The RFC 822 message header
format and its descendants (MIME, HTTP) are the original version of
this pattern: metadata headers that accumulate as a message passes
through processing stages.

**Kleisli categories and LLM nondeterminism.** The morphisms in our
algebra are effectful: an LLM call is stochastic, may fail, and operates
through a prompt that is itself a text artifact subject to drift. The
natural framework for modeling this is the Kleisli category of a monad
that captures nondeterminism and failure. In this view, a pipeline
operation is not a pure function `(Text, Meta) → (Text, Meta)` but a
Kleisli arrow `(Text, Meta) → M(Text, Meta)` where `M` is a monad
combining probability distributions (stochasticity), error handling
(failure modes), and possibly other effects (API rate limits, model
unavailability). Human gates (lines 424-459) become collapse operators
that project from the monadic type back to a committed value — precisely
the role of measurement in quantum mechanics or observer decisions in
second-order cybernetics. We have not yet formalized this connection, but
the parallel is suggestive: the gate is where the pipeline's internal
uncertainty resolves into a definite state that subsequent operations can
depend on. This remains a direction for future work.

## Next steps

This essay describes a formalism we developed empirically and have now
partially codified. What remains:

- **Extend the equation-to-diagram tool** to handle the `{enriches: ...}`
  annotation, rendering enrichment morphisms as pass-through
  decorations on wires rather than as separate output nodes.

- **Formalize confidence propagation.** Define the rules by which
  confidence bands compose: what confidence can a finding achieve given
  Medium-confidence evidence? This is analogous to defining error
  propagation formulas in experimental physics.

- **Apply the formalism to new pipelines.** Choose agent pipelines that solve a
  problem. Writing their resource equations would be the first step toward
  making them as auditable and composable as the trade study pipeline.

- **Investigate the connection to existing categorical frameworks.**
  Decorated cospans (Fong), operads for manufacturing (Spivak), and
  enriched categories over confidence lattices are all potential
  formalizations. The goal is not to force the pipeline into an
  existing framework but to find where existing theory provides
  composition laws we can use and where our "soft type" phenomenon
  requires extension.
