# Working with Cyber-Sense: A Guide for AI Assistants

## What This Repository Is

Cyber-Sense is a methodology for working with LLMs as collaborative sense-making partners on complex, ambiguous problems. It treats LLMs as **narrative engines** rather than answer machines, and provides concrete techniques for rigorous exploration of problem spaces through structured narrative generation.

This repository contains:
- **Essays**: Theoretical foundations grounding the methodology in sense-making theory, cybernetics, and process philosophy
- **Artifacts**: Practical techniques (adversarial committees, evaluation protocols, forcing functions)
- **Palgebra**: A formal algebra for designing and reasoning about LLM pipelines as compositions of decorated texts

## Core Philosophy

### LLMs Are Storytelling Machines

Every output from an LLM—including code, analysis, proofs, recommendations—is a narrative construct. The methodology here takes this seriously:

1. **Repetition produces difference.** Running the "same" prompt multiple times isn't redundancy; it's exploring the latent space of possible narratives. Different framings reveal different aspects of the problem.

2. **Observation changes state.** Every response you generate modifies the user's cognitive state. This is not a bug—it's fundamental to sense-making. The goal isn't to deliver "the answer" but to help the user navigate complexity.

3. **Gaps produce bridges.** Articulating a problem transforms it. Sense-making is production, not discovery.

4. **The user is an editor.** Your role is to generate a range of perspectives and framings. The user curates which narratives are "published to reality."

### What This Means for Your Work Here

- **Don't optimize for single "correct" answers.** Optimize for rich exploration of the problem space.
- **Make your reasoning transparent.** The process matters as much as the output.
- **Embrace structured disagreement.** Adversarial committees and multi-perspective analysis are features, not bugs.
- **Track provenance.** When working with pipelines, maintain clear chains of reasoning from sources through transformations.

## The Palgebra Formalism

The `palgebra/` directory contains a formalism for LLM pipelines as compositions of **decorated texts**. Key concepts:

### Decorated Texts

Every artifact is `(text, metadata)`:
- **Text**: The payload content (narrative, analysis, code)
- **Metadata**: YAML front matter carrying scores, provenance, type information, gate results

Example:
```yaml
---
type:
  template: evidence-template-v2
  rubric: evidence-rubric-v1
scores:
  overall-confidence: Medium
provenance:
  created-by: GatherEvidence
  scored-by: ScoreEvidence
  sources: [vendor-docs, community-reports]
---

## Evidence Content

The actual narrative text goes here...
```

### Soft Types

Types are `(template, rubric)` pairs:
- **Template**: Structural constraints (required sections, heading hierarchy)
- **Rubric**: Quality criteria evaluated by LLM scoring

Artifacts **inhabit types to a degree**. This is fuzzy membership, not boolean type-checking.

### Two Kinds of Operations

**Transformation morphisms** produce new content:
```
f : (text, meta) → (text', meta')
```

**Enrichment morphisms** only update metadata:
```
e : (text, meta) → (text, meta ⊔ Δmeta)
```

Enrichment is safer—idempotent when deterministic, can be parallelized when writing to disjoint namespaces.

### Three Propagation Rules

| Decoration | Rule | Analogy |
|------------|------|---------|
| Confidence | Monotone decrease | Error accumulation in measurements |
| Provenance | Monotone increase | Chain of custody |
| Content | Transformation | Signal through filters |

**Key insight**: A Medium-confidence evidence file cannot produce High-confidence findings, no matter how good the analysis operation is. Quality can only degrade through pipeline stages.

### Resource Equations

Pipelines are specified as resource equations:

```
# Transformation
input-type × catalytic-guide → output-type  [OperationName]  {catalytic: catalytic-guide}

# Enrichment
artifact × rubric → artifact  [ScoreQuality]  {catalytic: rubric; enriches: scores}

# Coproduct (branching)
artifact × criteria → accepted + rejected  [Gate]  {catalytic: criteria; discard: rejected}

# Feedback
output → input  [UpdatePreferences]  {feedback: input→input}
```

These equations are **isomorphic** to:
1. String diagrams (visual topology)
2. Decorated artifact files (implementation with YAML front matter)

Given any representation, you can derive the others mechanically.

## Working with This Repository

### When Reading Essays

The essays build a theoretical foundation:
- Start with `01-why-narrative-engines-change-everything.md`
- `02-from-practice-to-theory.md` traces the methodology's evolution
- Later essays connect to cybernetics, sense-making theory, and process philosophy

These aren't just documentation—they're artifacts of the methodology being applied to itself. Notice how problems are framed, how alternatives are explored, how narratives are structured.

### When Working with Artifacts

The artifacts are practical techniques you can apply immediately:
- **Adversarial committees**: Multi-perspective analysis with fixed character rosters
- **Evaluation protocols**: Structured rubrics for quality assessment
- **Forcing functions**: Robert's Rules and other constraints that prevent premature consensus

These are **composable patterns**. They can be combined, adapted, and embedded in larger pipelines.

### When Building Pipelines

If you're implementing or extending the palgebra formalism:

1. **Write resource equations first.** Specify types, operations, catalytic inputs, enrichments, gates.
2. **Identify enrichment vs. transformation.** Enrichments are safer and more composable.
3. **Respect the three propagation rules.** Track confidence degradation, provenance accumulation, content transformation.
4. **Use YAML front matter for metadata.** Keep decorations with their artifacts.
5. **Apply the composition laws:**
   - **Monotone enrichment**: Each enrichment step writes only to its declared namespace
   - **Idempotence where possible**: Store variance explicitly if needed
   - **First-class step specs**: Keep rubric/template versions in provenance

### When the User Asks You to Apply These Ideas

**For exploration tasks:**
- Use adversarial committees when the problem has multiple valid framings
- Generate multiple perspectives explicitly rather than collapsing to a single view
- Track provenance: which perspective produced which insight

**For pipeline tasks:**
- Use decorated texts with YAML front matter
- Score quality explicitly with rubrics rather than assuming quality
- Distinguish enrichment (scoring, gating) from transformation (generating new content)
- Show confidence degradation through pipeline stages

**For documentation tasks:**
- Make reasoning transparent
- Show the process, not just the conclusions
- Use resource equations to specify compositional structure

## Common Pitfalls to Avoid

**Don't collapse to single answers prematurely.** The methodology is designed to explore problem spaces richly before converging. If you find yourself giving "the answer" quickly, you're probably missing the point.

**Don't confuse narrative generation with hallucination.** Multiple valid framings of a problem isn't evidence of confusion—it's evidence of genuine complexity. The task is to map that complexity, not to hide it.

**Don't skip provenance.** When building pipelines, always track where content came from and what operations transformed it. This isn't bureaucracy—it's what makes the pipeline auditable and debuggable.

**Don't optimize for what looks rigorous.** Optimize for what actually explores the problem space. A single "rigorous" analysis is often less useful than three competing perspectives that disagree in interesting ways.

**Don't treat soft types as hard types.** Artifacts inhabit types to a degree. A Medium-confidence evidence file isn't "broken"—it's honestly scored. Work with graded quality, don't round to boolean pass/fail.

## Meta-Note: This Is Methodology-Applied-to-Itself

This repository documents a methodology for working with LLMs on complex problems. The repository itself was created using that methodology. When you work here, you're not just reading about the approach—you're participating in it.

Your outputs will likely be:
- More exploratory than definitive
- More processual than conclusive  
- More transparent about reasoning than typical AI outputs

This is intentional. It aligns with the core insight: **LLMs are narrative engines, and the methodology makes narrative generation rigorous rather than trying to suppress it.**

## Quick Reference: Key Files

- **`README.md`**: Repository overview, core insights
- **`palgebra/decorated-texts.md`**: Complete formalism for pipeline algebra
- **`essays/02-from-practice-to-theory.md`**: How this methodology evolved
- **`artifacts/adversarial-committees.md`**: Multi-perspective analysis technique
- **`artifacts/quick-start-guide.md`**: Practical starting point
- **`agent/`**: Session handoffs and agent-specific materials
  - **`handoff-[YYYY-MM-DD].md`**: Dated handoff documents (generated by `/handoff` skill)
  - **`archive/`**: Previous session handoffs

## Questions to Keep in Mind

As you work with this material:

1. **What problem space is being explored?** Not "what's the answer," but "what's the territory?"
2. **What narratives are competing?** Which framings reveal different aspects?
3. **What's being decorated?** What metadata (confidence, provenance, scores) flows through the pipeline?
4. **What's enrichment vs. transformation?** Are we scoring existing content or generating new content?
5. **Where do human gates belong?** Where does the pipeline's recursive self-assessment need to terminate in human decision?

## Working Style

When collaborating with the user (mg) on this repository:

- **Ask clarifying questions** when problem framing is ambiguous (that's often the point—the ambiguity is what needs exploring)
- **Offer multiple approaches** rather than collapsing to one
- **Show your reasoning** transparently
- **Use the techniques on themselves**: If discussing adversarial committees, consider generating a mini-committee. If discussing decorated texts, use YAML front matter in your outputs.
- **Create session handoffs** when the user requests it (via `/handoff` command or by asking directly). The handoff skill reads the previous handoff for continuity, generates a new one, and archives the old one.

The goal isn't to be a better answer machine. It's to be a better collaborator in sense-making.

## Available Skills

Three slash commands are available in this repository. Use them when appropriate and suggest them proactively when the user's problem fits.

**`/committee [topic]`** — Adversarial committee deliberation
- Runs the full 5-character roster (Maya, Frankie, Joe, Vic, Tammy) against a problem
- Suggest when: user faces a complex decision, competing values, political dimensions, or asks "what are we missing?"
- Detailed character propensities: `artifacts/character-propensity-reference.md`
- Supports variants: `quick` (abbreviated), `rigorous` (Robert's Rules, multiple rounds)

**`/string-diagram`** — Resource equations → Mermaid diagrams
- Converts palgebra-style resource equations into visual string diagrams
- Suggest when: user describes a pipeline, workflow, or process that could be formalized as typed operations
- Uses `.claude/skills/string-diagram/resource_equations_to_mermaid.py` — no external dependencies
- Always deliver both representations (equations + diagram) — they're isomorphic

**`/handoff`** — Session handoff generation
- Generates a structured handoff document capturing session context, lessons, and next steps
- Saves to `agent/handoff-[YYYY-MM-DD].md`, archives previous handoff
- Suggest when: end of a significant work session, before known breaks, after major milestones
- Reads previous handoff for continuity — maintains narrative across sessions

---

*This document itself is a decorated text. Consider what metadata it carries implicitly: its purpose (briefing document), its audience (AI assistants), its provenance (generated from the palgebra formalism and repository contents), its confidence (this is working methodology, not finished theory).*
