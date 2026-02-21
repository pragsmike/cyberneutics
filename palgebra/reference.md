# Palgebra Reference

A reference for writing and reasoning about LLM pipelines as compositions
of decorated texts. For the full theoretical development, see
[decorated-texts.md](decorated-texts.md). For worked examples, see
[committee-as-palgebra.md](committee-as-palgebra.md) (the funnel half),
[duality-and-composition.md](duality-and-composition.md) (the fan half,
the composition, and the decision monad), and the equation files in
`.claude/skills/string-diagram/`.

The formalism derives from Fong and Spivak's resource-theoretic treatment
of monoidal categories in *Seven Sketches in Compositionality* (2019),
Chapter 2 (resource theories). We adapt their string diagram / resource
equation framework to LLM pipelines, where the resources are text
artifacts carrying structured metadata.

---

## Core model

Every pipeline artifact is a **decorated text**:

```
artifact = (text, metadata)
```

- **Text** is the payload: narrative, analysis, code, whatever the human
  reader cares about.
- **Metadata** is a structured record (YAML front matter) carrying
  scores, provenance, type information, and gate results, accumulated as
  the artifact moves through the pipeline.

The `---` delimiter in a markdown file is the product projector.
Everything above it is metadata; everything below is text. The file
format *is* the functor.

## Types

A type is a **soft type** — a `(template, rubric)` pair:

- **Template**: structural constraints (required sections, heading
  hierarchy, required metadata fields). Almost a grammar; a parser could
  check it.
- **Rubric**: quality criteria evaluated by LLM scoring ("claims are
  evidence-backed," "trade-offs are specific"). Semantic judgments that
  return graded scores, not booleans.

Artifacts **inhabit types to a degree**. A rubric scores each criterion
0-3, rolling up to a confidence band (High / Medium / Low). The template
defines the *support* (what could be a member). The rubric defines the
*membership function* (how well a particular artifact inhabits the type).

Type names are **lowercase hyphenated identifiers**: `evidence`,
`candidates-long-list`, `transcript`, `findings-rollup`.

## Resource equations

Pipelines are specified as resource equations. Each line is one
operation (a box in the string diagram):

```
inputs → outputs  [OperationName]  {annotations}
```

### Operators

| Symbol | ASCII | Meaning |
|--------|-------|---------|
| `×`    | `*`   | Cross product — all these inputs together |
| `→`    | `->` | Morphism arrow — operation produces output |
| `+`    |       | Coproduct — multiple distinct outputs (branching) |
| `( )`  |       | Grouping (associativity only, no semantic effect) |

### Annotations

Annotations are curly-braced, semicolon-separated:

```
{catalytic: B; discard: D; enriches: scores; feedback: X→Y}
```

| Annotation | Meaning |
|------------|---------|
| `catalytic: X` | Input X participates but is not consumed. Dashed wire in diagram. X can feed into multiple operations without being altered. Catalytic inputs are comonoid objects (equipped with copy). |
| `discard: X` | Output X is waste / rejected. Red sink in diagram. |
| `enriches: namespace` | Operation is an enrichment (see below) — payload unchanged, metadata updated in the declared namespace. |
| `feedback: X→Y` | Output X feeds back to input Y, closing a loop. Traced monoidal structure. |

### Comments

Lines starting with `#` are comments. Blank lines are ignored.

### Complete example

```
# Transformation: consume input, produce new artifact
experience-reports → preference-signals  [ExtractPreferences]

# Catalytic inputs: guides participate but aren't consumed
candidates × evidence-template × guides → evidence  [GatherEvidence]  {catalytic: evidence-template, guides}

# Enrichment: payload unchanged, metadata updated
evidence × evidence-rubric → evidence  [ScoreEvidence]  {catalytic: evidence-rubric; enriches: scores}

# Coproduct with discard: sort into accepted + rejected
evidence × security-criteria → accepted + rejected  [SecurityGate]  {catalytic: security-criteria; discard: rejected}

# Feedback loop: output feeds back to earlier input
rollup → experience-reports  [UpdatePreferences]  {feedback: experience-reports→experience-reports}
```

## Two kinds of morphism

Every pipeline operation is one of two kinds:

### Transformation morphisms

Produce **new content**. Inputs are consumed; outputs are different
artifacts.

```
f : (text, meta) → (text', meta')
```

Examples: GatherEvidence reads candidate descriptions, produces evidence
narratives. DraftFindings reads evidence, produces findings. Deliberate
reads a charter, produces a transcript.

### Enrichment morphisms

Leave the **payload unchanged**; only update metadata.

```
e : (text, meta) → (text, meta ⊔ Δmeta)
```

The `⊔` (join) operator merges metadata maps. Enrichment writes to a
declared namespace (e.g., `scores.*`, `gate.*`).

Examples: ScoreEvidence reads evidence body, writes quality scores to
front matter. SecurityGate reads evidence, writes gate result to front
matter. Evaluate reads a transcript, produces evaluation scores.

Mark enrichments with `{enriches: namespace}` in the equation.

### Why the distinction matters

- **Enrichment is safe to re-run** (close to idempotent when inputs are
  frozen).
- **Enrichments that write to disjoint namespaces can be parallelized**
  (order doesn't matter when writing to `scores.*` vs. `gate.*`).
- **Transformations generally can't be re-run** without discarding their
  previous output.
- Enrichment is analogous to email MTA headers: each stage stamps the
  artifact's metadata without touching the body.

## Three propagation rules

Three kinds of decoration flow through the pipeline, each with different
algebraic behavior:

| Decoration | Rule | Behavior | Analogy |
|------------|------|----------|---------|
| **Confidence** | Monotone decrease | Can only degrade through pipeline stages. A Medium-confidence evidence file cannot produce a High-confidence finding, no matter how good the analysis operation. | Measurement error accumulation |
| **Provenance** | Monotone increase | Only appends. Each operation adds to the chain without erasing prior links. | Chain of custody |
| **Content** | Transformation | May change entirely when passing through a transformation morphism. | Signal through a filter |

**The confidence rule is the most consequential.** It means quality can
only degrade through composition. If you want higher-confidence output,
you must improve the *inputs*, not the downstream operations. This
determines where to invest effort in a pipeline.

## Score combination structures

Confidence propagation uses min-lattice structure (weakest link
determines quality), but other scoring strategies are possible:

| Structure | How scores combine | When to use |
|-----------|--------------------|-------------|
| **Lattice (min/max)** | Greatest lower bound | Quality bounded by weakest link. Default for confidence. |
| **Semiring (weighted sums)** | Additive with weights | Cumulative contributions: multiple weak signals can add up. Cost accounting, evidence aggregation. |
| **Pareto (multi-objective)** | Preserve Pareto frontier | Incommensurable criteria: can't trade security for usability on one scale, so track both. |

Different pipeline stages may use different combination rules. The key
property is that they are monoidal — they compose predictably.

## Composition laws

Three operational principles for safe pipeline composition:

### 1. Monotone enrichment

An enrichment step writes **only** to its declared namespace.
ScoreEvidence writes to `scores.*` and nothing else. SecurityGate writes
to `gate.*` and nothing else. When enrichment steps respect namespace
boundaries, they can be reordered or parallelized without conflict.

### 2. Idempotence where possible

If an enrichment step is deterministic given frozen inputs (same rubric,
same model, same artifact), re-running it should not change the
metadata. When this isn't true (stochastic LLM, changed rubric), store
variance explicitly as structured data (e.g., `scores.helpfulness.samples:
[0.81, 0.83, 0.82]`). Idempotence makes enrichment safe to re-run
during debugging or pipeline repair.

### 3. First-class step specifications

Store each step's specification text (prompt, rubric version, template
version) in the provenance metadata. When you change a rubric, that
change is a diff in the spec text. This makes the pipeline reproducible
and auditable: you can see which rubric version produced a given score,
and diff pipeline versions to understand behavioral changes.

## Human gates

At certain points, a human reviews accumulated metadata and makes a
binary decision: proceed or stop. Human gates **collapse** graded
uncertainty into a crisp commitment.

```
gate : (text, meta) → proceed | halt
```

Before the gate: the artifact carries potential (quality scores,
confidence bands, conditions, caveats). After the gate: a decision.

Gates terminate the pipeline's recursive self-assessment. Rubrics check
artifacts. Rubric-of-rubrics check rubric calibration. But this tower
must terminate. Human gates are where it terminates — axioms that ground
recursive observation and let the pipeline proceed on settled foundation.

In the equations, a human gate is a coproduct:

```
evaluation × resolution → accepted + rejected  [HumanGate]  {discard: rejected}
```

## Three isomorphic representations

The same pipeline can be expressed in three forms. Given any one, you can
derive the other two mechanically:

| Representation | What it shows | Format |
|----------------|---------------|--------|
| **Resource equations** | Composition and typing | `.txt` file, one equation per line |
| **String diagrams** | Topology and dataflow | Mermaid flowchart (generated from equations via `resource_equations_to_mermaid.py`) |
| **Decorated artifact files** | Actual content and metadata | Markdown with YAML front matter |

The equations are the canonical specification. The diagram makes topology
visible. The files are the implementation. They are charts on the same
manifold.

## Metadata format

Decorations are carried as YAML front matter:

```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  source-coverage: 2
  security-completeness: 3
  overall-confidence: Medium
gate:
  security: Blue
  conditions: []
provenance:
  created-by: GatherEvidence
  scored-by: ScoreEvidence
  sources:
    - vendor-trust-center
    - community-reports
  cycle: 5
---

## Payload content starts here

The actual text artifact...
```

Each namespace (`type.*`, `scores.*`, `gate.*`, `provenance.*`)
corresponds to the enrichment steps that write to it. Namespace
discipline makes metadata merges predictable and compositional.

## How to specify a new pipeline

1. **Identify the types.** What artifacts flow through the pipeline?
   Name them as lowercase hyphenated identifiers.

2. **Identify the operations.** What transforms or enriches each
   artifact? Name them in PascalCase.

3. **Classify each operation.** Is it a transformation (new content) or
   enrichment (scoring / gating existing content)?

4. **Mark catalytic inputs.** Which inputs are consulted but not
   consumed? Templates, rubrics, guides, reference documents.

5. **Mark coproducts.** Where does the pipeline branch? What gets
   discarded?

6. **Mark feedback loops.** Where does output feed back to input?
   Specify the loop bound (max iterations).

7. **Write the resource equations.** One line per operation.

8. **Check the propagation rules.** Where does confidence degrade?
   Where must provenance accumulate? Where are the human gates?

9. **Generate the string diagram.** Run `resource_equations_to_mermaid.py`
   on your equations file. The visual topology should match your
   mental model. If it doesn't, the equations are wrong.

## Generating diagrams

The `/string-diagram` skill (or the Python tool directly) converts
equations to Mermaid:

```bash
python .claude/skills/string-diagram/resource_equations_to_mermaid.py \
  equations.txt -o flow.mermaid
```

Options: `--direction LR` (default), `TD`, `RL`, `BT`.

Always deliver **both** equations and diagram — they are isomorphic.

## Spider patterns: fan and funnel

Two dual patterns recur in pipeline design. They are formalized in
[duality-and-composition.md](duality-and-composition.md).

### Fan (one-to-many / coproduct spider)

A single input is injected into multiple distinct outputs:

```
situation × params → scenario-1 + scenario-2 + scenario-3  [Fan]  {catalytic: params}
```

Or more compactly, when the output is a typed collection:

```
situation × params → scenario-set  [Fan]  {catalytic: params}
```

The fan is **divergent**: it explores a possibility space by producing
multiple narratives from different assumptions. Each output is an
injection of the input into a different narrative context.

### Funnel (many-to-one / product spider)

Multiple inputs converge into a single output:

```
charter × scenario-set × roster → transcript  [Deliberate]  {catalytic: roster}
```

The funnel is **convergent**: it commits by combining multiple
perspectives into a single resolution. Each input contributes a
projection to the output.

### Composed pattern: the decision monad

Fan → funnel yields a single-input, single-output operation:

```
situation → resolution  [DeliberatedChoice]
```

This composition has monad structure (unit, associativity), meaning it
can be iterated and chained. See
[duality-and-composition.md](duality-and-composition.md) for the full
treatment, including monad laws as quality criteria and iteration for
mapping decision landscapes.

## Quick reference: annotation cheat sheet

```
A × B → C          [Op]                          # basic transformation
A × B → C          [Op]  {catalytic: B}          # B not consumed
A → B + C           [Op]  {discard: C}            # C is waste
A × R → A           [Op]  {catalytic: R; enriches: scores}  # enrichment
A → B               [Op]  {feedback: B→A}         # feedback loop
A × B → C + D       [Op]  {catalytic: B; discard: D}        # combined
A × P → B₁ + B₂ + B₃  [Op]  {catalytic: P}      # fan (one-to-many)
A₁ × A₂ × A₃ → B  [Op]                          # funnel (many-to-one)
```

## References

- Fong, B. and Spivak, D.I. (2019). *Seven Sketches in
  Compositionality: An Invitation to Applied Category Theory.*
  Cambridge University Press. Chapter 2: Resource Theories.
- Fong, B. (2016). *The Algebra of Open and Interconnected Systems.*
  PhD thesis, University of Oxford. (Decorated cospans.)
- De Wynter et al. (2023). "On Meta-Prompting." arXiv:2312.06562.
  (Category-theoretic framework for LLM interactions.)
- Liang et al. (2024). "Prompts Are Programs Too!" arXiv:2409.12447.
  (Prompt development as programming phenomenon.)
- Kelly, G.M. (1982). *Basic Concepts of Enriched Category Theory.*
  (Enriched categories over confidence lattices.)
- Baez, J. and Stay, M. (2011). "Physics, Topology, Logic and
  Computation: A Rosetta Stone." (String diagrams across domains.)
