---
name: palgebra
description: "Minimal pipeline algebra — just enough to read and write resource equations when working with string diagrams"
---

# Palgebra Skill

## When this skill applies

This skill fires when:
- The user is describing a workflow, pipeline, or multi-step process
- The user asks about resource equations or string diagrams
- The user invokes `/cyberneutics:string-diagram`
- The user wants to formalize a process or compare workflow versions

## Core concept: decorated texts

Every artifact in a pipeline is a **decorated text** — content plus metadata:

```
artifact = (text, metadata)
```

The text is what you read. The metadata tracks quality, provenance, and type information. Think of it like a document with a structured header that accumulates annotations as it moves through a process.

## Two kinds of operation

### Transformation
Produces **new content**. Inputs are consumed, outputs are different things.
```
interviews × criteria → scored-leads  [Score]
```

### Enrichment
Leaves the **content unchanged**, only updates metadata (scores, tags, status).
```
report × rubric → report  [Evaluate]  {catalytic: rubric; enriches: scores}
```

The distinction matters: enrichments are safe to re-run. Transformations generally aren't.

## Basic notation

| Symbol | Meaning | Example |
|--------|---------|---------|
| `→` | produces | `A → B` (A becomes B) |
| `×` | and (multiple inputs) | `A × B → C` (A and B together become C) |
| `+` | or (multiple outputs) | `A → B + C` (A splits into B and C) |
| `{catalytic: X}` | X is used but not consumed | Like consulting a recipe |
| `{discard: X}` | X is waste | Byproduct, not the goal |
| `{enriches: Y}` | Same thing out, metadata updated | Scoring, tagging, evaluating |
| `{spider: fan}` | One-to-many topology | Exploring, generating options |
| `{spider: funnel}` | Many-to-one topology | Converging, deciding |

## Three propagation rules

As artifacts move through a pipeline:

1. **Confidence can only degrade.** A medium-quality input cannot produce a high-quality output, no matter how good the operation. Improve inputs, not downstream processing.

2. **Provenance can only accumulate.** Each operation adds to the chain of custody without erasing prior links. You can always trace back.

3. **Content transforms.** The actual text may change completely through transformation operations. That's the point.
