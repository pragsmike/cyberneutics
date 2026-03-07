---
resolution:
  date: 2026-03-01
  topic: "Making the Glenda/Crock application essays more accessible"
  outcome: PASSED
  decision: >
    Adopt a four-layer progressive-disclosure strategy: narrative-first
    restructuring, inline conceptual primers, directory-level reading guide,
    and TL;DR scaffolds.
  summary: >
    The committee identified context dependency (not vocabulary per se) as the
    primary accessibility barrier in the Glenda/Crock essays, confirmed by
    comparative analysis with the successful social-disruption essay. The
    recommended strategy preserves full technical precision while restructuring
    the reader's path so that vocabulary arrives when needed rather than as a
    prerequisite. Key interventions: lead with narrative (the heist/hostage
    frames already implicit in Glenda/Crock), provide inline conceptual primers
    covering mesh/rewiring/seam, add audience-aware reading paths at the
    directory level, and scaffold each essay with a TL;DR. The committee
    explicitly rejected rewriting from scratch, removing framework vocabulary,
    and targeting casual readers as the primary audience.
  implementation_plan:
    - action: "Draft inline conceptual primer for alignment essay"
      description: >
        3–5 paragraphs covering mesh (as entailment web), rewiring (as
        selective modification), and seam (as detectable boundary artifact).
        Must include Maya's point about structural inevitability.
        Defer bath, type-spoof, residuality to footnotes.
    - action: "Restructure alignment essay opening"
      description: >
        Replace the Pask-dependency epigraph with a narrative hook using the
        heist frame. Move the 'Builds on' reference to a footnote or
        'Further Reading' section.
    - action: "Add scenario recap to coercion essay"
      description: >
        Brief 1-paragraph setup so the coercion essay doesn't require having
        read the alignment essay to begin.
    - action: "Write TL;DR scaffolds"
      description: >
        3–5 sentence plain-language summaries at the top of both Glenda/Crock
        essays, framed as reading scaffolds.
    - action: "Restructure directory README as reading guide"
      description: >
        Transform narrative-immune-systems/README.md into an audience-aware
        entry point with reading paths (journalist / researcher / deep dive),
        a concept map, and a brief overview of the argument arc.
    - action: "Document accessibility conventions"
      description: >
        Add a section to applications/README.md or a new conventions doc
        establishing the pattern (narrative-first + primer + TL;DR + reading
        guide) for future application essays.
    - action: "Reader test"
      description: >
        Test revised alignment essay with a reader unfamiliar with Pask.
        Success criterion: can they explain the seam concept back, even
        imprecisely?
  votes:
    - member: Maya
      vote: "YES — with the constraint that we do not create a separate 'popular' version"
    - member: Frankie
      vote: "YES"
    - member: Joe
      vote: "YES — the layered entry-point approach addresses historical failure modes"
    - member: Vic
      vote: "YES — contingent on reader testing after revision"
    - member: Tammy
      vote: "YES — contingent on documenting the pattern for future use"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: Making the Glenda/Crock Essays Accessible

## Decision

Adopt a four-layer progressive-disclosure strategy for the Glenda/Crock application essays:

1. **Narrative-first restructuring** — lead with story, earn vocabulary progressively
2. **Inline conceptual primers** — self-contained scaffolding for the Pask framework concepts
3. **Directory-level reading guide** — audience-aware navigation with explicit paths
4. **TL;DR scaffolds** — plain-language argument summaries at the top of each essay

## Rationale

The social-disruption essay succeeds because it opens with a bold claim in plain language, builds from familiar territory (journalism, trust, propaganda), earns its specialized vocabulary through narrative, and depends on no external documents. The Glenda/Crock essays fail on all four counts: they open with framework references, build from unfamiliar territory (Pask mesh fitting), spend vocabulary before earning it, and depend on multiple external documents.

The fix is structural, not cosmetic. The intellectual substance stays intact. What changes is the *ordering* — readers enter through narrative and arrive at precision, rather than being required to start with precision.

## Key Constraint

The committee explicitly rejects creating a separate "simplified" or "popular" version. There is one version of each essay; it serves multiple audience tiers through progressive disclosure and signposting, not through dumbing down.

## Unanimous with Conditions

All five members voted YES. Conditions: no separate popular versions (Maya), reader testing after revision (Vic), and pattern documentation for future use (Tammy).
