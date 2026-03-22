# Task: Revise Palgebra Architecture Documents

## Context

A conversation on 2026-03-22 identified two insights that are implicit in
the cyberneutics formalism but not stated anywhere in the architecture
documents. The diary entry `wild/diary/2026-03-22-bradley-magnitude-tropical.md`
documents the full reasoning. This task implements the documentation changes.

The two insights:

1. **The closure insight (presheaf-enrichment unification).** Text is a
   closed category — its hom-objects are themselves texts (prompts,
   scripts, calibration records). This means the Kelly enrichment layer
   (confidence values on morphisms) and the presheaf layer (type profiles
   on objects) are not parallel stories but one story: the enrichment
   values are derived from presheaf evaluation applied to hom-objects.
   The three-element confidence lattice V is a coarsening of the richer
   presheaf data on the calibration records that live at Hom(A, B).

2. **Morphisms as texts (self-applicability).** Every morphism in Text is
   specified by a text — either a prompt (stochastic) or a script
   (deterministic). Both are objects of Text. Both have type profiles.
   The pipeline description is pipeline data. Verification stays inside
   the category.

There is also a terminological collision to address: "enrichment" is used
in two incompatible senses (SWE: metadata-adding pipeline stage; Kelly:
replacing hom-sets with hom-objects in V).

## Guiding principles

- **Light touch.** The formal machinery is already in place. These are
  paragraphs and short sections, not rewrites. The existing audience
  calibration (engineers first, ACT readers second) must be preserved.
- **No new formalism.** State insights in prose with minimal notation.
  Point to existing formal infrastructure (Fritz, Kelly, presheaf
  construction in soft-type-theory.md) for readers who want precision.
- **Don't increase density.** The documents already push the limits of
  what non-specialist readers will tolerate. Each addition should be
  self-contained and skippable — a reader who doesn't care about closure
  should be able to skip the new section without losing the thread.
- **Flag the terminological collision.** Don't rename anything (the SWE
  sense is established in the codebase and the architecture docs). Just
  add a disambiguation note where both senses appear.

## Files to revise

### 1. `palgebra/categorical-structures.md`

This is the primary target. It has the three-layer architecture (§2c),
the enrichment base (§2b), the deterministic/stochastic partition (§2a),
and the Probe/eigenform section (§9).

**Add: §2d — Closure and self-reference** (new subsection after §2c)

Content to cover:
- Text is closed: hom-objects are texts. A calibration record for the
  Deliberate morphism is itself an artifact in Text.
- This means the presheaf machinery (from soft-type-theory.md) applies
  to hom-objects. The type profile of a calibration record — how well
  it inhabits the "calibration record" type — is a presheaf value.
- The Kelly enrichment value (Hom(A,B) = Medium) is a summary statistic
  derived from the presheaf evaluation of the hom-object. The
  three-element lattice V is a coarsening of the richer V₅-valued
  presheaf data.
- The self-referential loop: calibration records are auditable by the
  same machinery that audits pipeline outputs. This is what makes the
  calibration register a viable System 3* audit channel rather than an
  external oracle.
- The recursion stabilises at the eigenform: when scoring the scoring
  produces the same result as scoring alone.
- Keep it to ~15–20 lines of prose. No new notation. Point to
  soft-type-theory.md for the presheaf formalism and §9 for eigenforms.

**Add: §2e — Morphisms as texts** (new subsection after §2d)

Content to cover:
- Every morphism in the pipeline is specified by a text: a prompt file
  or a script. Both are objects of Text. Both have type profiles.
- Prompts are stochastic morphisms (Layer 2); scripts are deterministic
  morphisms (Layer 1 / Text_det). This maps exactly onto Fritz's
  partition.
- The engineering payoff: no separate metalanguage for pipeline
  specification. The pipeline description is pipeline data. Verification
  (comparing spec against output) is a morphism in Text. The evaluation
  of that comparison is a presheaf value.
- The pipeline is self-applicable in a controlled way: you can run the
  committee on a prompt to evaluate prompt quality. Every modification
  is an artifact with a type profile, subject to audit.
- Keep it to ~15–20 lines. Emphasise the engineering consequence
  ("why should I care") over the categorical observation.

**Add: Terminology note in §2b**

Where the enrichment base is introduced, add a short disambiguation:

  > **Terminology note.** "Enrichment" is used in two senses in this
  > repository. In the pipeline architecture (reference.md,
  > decorated-texts.md), an *enrichment morphism* is a pipeline stage
  > that updates metadata without changing the payload text — the
  > enterprise-architecture sense. In category theory (Kelly, 1982), an
  > *enriched category* replaces hom-sets with hom-objects valued in a
  > monoidal category — attaching quantitative data to the arrows
  > themselves. Both senses are active here. The SWE enrichment morphisms
  > are operations that update the presheaf layer (object decoration).
  > The Kelly enrichment is the confidence structure on hom-objects
  > (arrow decoration). Section 2d explains how they relate.

### 2. `palgebra/soft-type-theory.md`

This document develops the presheaf formalism but doesn't mention that
it applies to hom-objects.

**Add: Short remark at end of §3 (Morphisms and confidence propagation)**

After the subsection on enrichments preserving type profiles, add a
paragraph noting that because Text is closed, the presheaf construction
applies reflexively — hom-objects are objects, so they carry type
profiles. This connects the presheaf layer to the enrichment layer:
the confidence value on a morphism is the presheaf evaluation of the
corresponding hom-object, coarsened to V. Point to
categorical-structures.md §2d for the full discussion.

~5–8 lines. Don't develop the point here; just plant the cross-reference.

### 3. `palgebra/decorated-texts.md`

This is the essay developing the formalism from first principles. It
introduces the transformation/enrichment distinction and the decorated
text structure.

**Add: Short remark in the "Two kinds of morphism" section**

After the existing discussion of transformation vs enrichment morphisms,
add a paragraph noting that both kinds of morphism are *specified by
texts* — prompt files or scripts — which are themselves decorated texts
in the pipeline. This makes the specification of a transformation an
object of the same category as the transformation's input and output.
The consequence: pipeline specifications are auditable by the same
machinery that audits pipeline outputs. No separate verification
framework needed.

~5–8 lines. Frame as an engineering observation, not a categorical one.
This document's audience is practitioners, not ACT readers.

### 4. `palgebra/reference.md`

This is the reference card. It defines the two morphism kinds tersely.

**Add: One-line note under "Two kinds of morphism"**

Something like:

  > Both morphism kinds are specified by text artifacts (prompt files or
  > scripts) that are themselves objects of the pipeline — see
  > [categorical-structures.md §2e](categorical-structures.md) for
  > implications.

One line. Don't develop it here; the reference card should stay terse.

### 5. `palgebra/README.md`

**Add: Entry in "Key ideas in brief"**

After "Three representations" add:

  > **Self-applicable.** Morphisms are specified by texts (prompts,
  > scripts) that are themselves pipeline objects with type profiles.
  > The pipeline can audit its own specifications. See
  > [categorical-structures.md §2d–§2e](categorical-structures.md).

Two sentences. Consistent with the existing entry style.

## Files NOT to revise

- `committee-as-palgebra.md` — worked example; doesn't need the
  abstract insight
- `duality-and-composition.md` — fan/funnel duality; the closure
  observation doesn't change anything here
- `wild/` documents — the diary entry already covers this
- Essays — these are published prose; revising them for a formal
  insight would change their register

## Verification

After revising, confirm:
- §2d and §2e in categorical-structures.md are self-contained and
  skippable — a reader who skips them loses nothing needed for §3–§9
- The terminology note in §2b is visible early enough that readers
  encounter it before the collision causes confusion
- Cross-references between documents are bidirectional (categorical-
  structures points to soft-type-theory; soft-type-theory points back)
- No new notation is introduced
- The reference card (reference.md) stays under 10 pages
- The README key-ideas list stays under 10 entries
