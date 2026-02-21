# Palgebra

A pipeline algebra for LLM workflows, treating them as compositions of
**decorated texts** — text artifacts carrying structured metadata through
typed operations.

The formalism adapts the resource-theoretic framework from Fong and
Spivak's *Seven Sketches in Compositionality* (2019), Chapter 2, to
LLM pipelines. Where Fong and Spivak use string diagrams and resource
equations to model manufacturing processes (their lemon meringue pie),
we use the same structures to model pipelines of prompted text
transformations — with the addition of soft types, enrichment morphisms,
and confidence propagation to handle the inherent fuzziness of
LLM-generated artifacts.

## Contents

### Reference and specification

- **[reference.md](reference.md)** — The reference card. Syntax,
  operators, annotations, morphism types, propagation rules, composition
  laws, metadata format, and the step-by-step process for specifying a
  new pipeline. **Start here** if you want to write resource equations
  or understand an existing pipeline.

### Theory

- **[decorated-texts.md](decorated-texts.md)** — The full essay
  developing the formalism from first principles: why basic type systems
  fail for LLM pipelines, how soft types address graded inhabitation,
  the two morphism kinds and their algebraic properties, score
  combination structures, human gates as collapse operators, and
  connections to category theory (decorated cospans, enriched categories,
  Kleisli categories for nondeterminism). Read this to understand *why*
  the formalism has the shape it does, not just *how* to use it.

### Worked examples

- **[committee-as-palgebra.md](committee-as-palgebra.md)** — The
  adversarial committee workflow (`/committee` + `/review` + remediation
  loop) formalized as resource equations. Nine operations spanning all
  four structural kinds (transformation, enrichment, coproduct, collapse).
  Detailed commentary on catalytic inputs, the bounded feedback trace,
  confidence propagation, and comparison with the trade study pipeline.

- **[duality-and-composition.md](duality-and-composition.md)** — The
  committee as one half of a dual pair: scenario generation (fan,
  one-to-many) is the other. Composing fan → funnel yields a decision
  monad with quality laws; Probe/Map operations for N-run variance and
  decision-landscape mapping; new types (situation, scenario-set,
  variance-report, etc.); two rosters (committee vs scenario). Scenario
  skill and composed pipeline are specified but not yet implemented.

### Tool

- **[`../.claude/skills/string-diagram/`](../.claude/skills/string-diagram/)** —
  The `/string-diagram` skill and `resource_equations_to_mermaid.py`
  converter. Turns resource equations into Mermaid flowcharts.
  Equations and diagrams are isomorphic — the tool is one direction of
  the isomorphism. Includes example equation files (AI study pipeline,
  lemon meringue pie).

## Key ideas in brief

**Decorated texts.** Every artifact is `(text, metadata)`. Text is the
payload. Metadata is YAML front matter carrying scores, provenance, type
info, and gate results.

**Soft types.** Types are `(template, rubric)` pairs. Artifacts inhabit
types to a degree, not boolean pass/fail. The rubric is the membership
function.

**Two morphism kinds.** Transformations produce new content. Enrichments
only update metadata (scoring, gating). Enrichments are safer:
idempotent, parallelizable, re-runnable.

**Three propagation rules.** Confidence can only degrade. Provenance can
only accumulate. Content transforms.

**Three representations.** Resource equations (term language), string
diagrams (visual topology), decorated artifact files (implementation).
Given any one, you can derive the others.

## Theoretical roots

The formalism draws on:

- **Fong and Spivak**, *Seven Sketches in Compositionality* (2019) —
  resource theories, string diagrams for symmetric monoidal categories
- **Fong**, *The Algebra of Open and Interconnected Systems* (Oxford,
  2016) — decorated cospans for composing open systems
- **Kelly**, *Basic Concepts of Enriched Category Theory* (1982) —
  enrichment over confidence lattices
- **Baez and Stay**, "Physics, Topology, Logic and Computation: A
  Rosetta Stone" (2011) — string diagrams across domains
- **De Wynter et al.**, "On Meta-Prompting" (2023) — category-theoretic
  framework for LLM interactions
- **Liang et al.**, "Prompts Are Programs Too!" (2024) — prompt
  development as programming phenomenon
