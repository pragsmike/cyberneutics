---
name: string-diagram
description: "Visualize a workflow as a resource equation diagram — formalize pipelines and processes to reveal hidden structure"
---

# /cyberneutics:string-diagram

**Turn a workflow description into a precise visual diagram.**

Describe a pipeline or process in plain language, and this command produces a formal representation using resource equations — a notation that makes inputs, outputs, transformations, and waste explicit. The diagram reveals structure that prose descriptions obscure: where things branch, what gets consumed vs. reused, and where feedback loops exist.

## Quick syntax reference

```
A → B                [Transform]                  # A is consumed, B is produced
A × B → C            [Combine]                    # Two inputs combined
A → B + C            [Split]                      # One input, two outputs
A × B → C            [Op]  {catalytic: B}         # B is used but not consumed
A → B + C            [Op]  {discard: C}           # C is waste/byproduct
A × R → A            [Score]  {enriches: scores}  # Same thing out, with metadata added
A → B₁ + B₂ + B₃    [Explore]  {spider: fan}     # One-to-many (divergent)
A₁ × A₂ × A₃ → B   [Converge]  {spider: funnel} # Many-to-one (convergent)
```

**Key symbols**:
- `→` means "produces" (a transformation)
- `×` means "and" (multiple inputs combined)
- `+` means "or" (multiple distinct outputs / branches)
- `{catalytic: X}` means X is used but not used up (like a recipe — you consult it but don't eat it)
- `{discard: X}` means X is waste
- `{enriches: Y}` means the thing itself doesn't change, just gets annotated

## How to use it

Describe your workflow in plain language:

```
/cyberneutics:string-diagram We take customer interviews and market data, run them through a scoring process using our evaluation criteria, then split into qualified and unqualified leads. Qualified leads go to the sales team along with the original interview notes.
```

Or provide equations directly:

```
/cyberneutics:string-diagram
interviews × market-data × criteria → scored-leads  [Score]  {catalytic: criteria}
scored-leads → qualified + unqualified  [Gate]  {discard: unqualified}
qualified × interviews → sales-package  [Package]  {catalytic: interviews}
```

## What you'll get

1. **Resource equations**: The formal representation of your workflow
2. **A diagram**: A visual flow showing operations as boxes, types as wires, and annotations for catalytic inputs, waste, and feedback
3. **What the notation reveals**: A brief explanation of what the formal representation shows that wasn't obvious in the prose description

## What this reveals

The notation forces precision about things prose lets you hand-wave:

- **What actually gets consumed vs. reused?** A "template" you consult at every step is catalytic — it should be marked as such, not drawn as a regular input that gets used up.
- **Where does information branch?** Coproducts (`+`) make decision points explicit.
- **Where are the feedback loops?** If output from step 5 feeds back into step 2, that's a loop with implications for convergence and termination.
- **What's waste?** Making byproducts explicit helps you decide whether they're truly waste or potentially valuable output you're discarding.

## Examples

**Hiring pipeline**:
```
applications × job-spec → candidates-long-list  [InitialScreen]  {catalytic: job-spec}
candidates-long-list × interview-rubric → scored-candidates  [Interview]  {catalytic: interview-rubric}
scored-candidates → offers + rejections  [Decide]  {discard: rejections}
```

**Decision pipeline** (the cyberneutics probe):
```
situation × scenario-roster → scenario-set  [GenerateScenarios]
  {catalytic: scenario-roster; spider: fan}
scenario-set × committee-roster → resolution  [Deliberate]
  {catalytic: committee-roster; spider: funnel}
```

## When to use this

- When you're designing a multi-step process and want to catch gaps
- When you're explaining a workflow to someone and want to be precise
- When you suspect a process has hidden complexity (feedback loops, wasted outputs)
- When you want to compare two versions of a workflow structurally
