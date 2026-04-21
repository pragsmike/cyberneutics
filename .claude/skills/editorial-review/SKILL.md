---
name: editorial-review
description: >
  Run an editorial review of the Cyberneutics repository (essays and supporting
  material) against the seven-dimension audience-experience rubric. Produces
  rubric scores with evidence, per-essay notes, cross-cutting issues, and a
  prioritized remediation plan. Does not rewrite content. Use when the user
  types '/editorial-review' or asks for an editorial review of the repo.
---

# Editorial Review Skill

Assess the Cyberneutics repository for how well it meets its audiences' needs
and how delightful the reader experience is. The repo is a methodology:
essays explain *why*, artifacts explain *how*, palgebra explains *what,
precisely*. Audiences are Practitioners, Theorists, Skeptics, Formalists.

Your job is to (1) assess current content against the audience-experience
rubric, (2) produce a structured report, and (3) devise a concrete plan to
modify the repo's contents so that it scores highly on that rubric.

## Why this exists

Editorial drift is slow and hard to notice from inside the writing. A
standing, rubric-driven review gives the repo a way to measure itself against
its own stated audience commitments: when new essays are added, when
terminology drifts, when paths get stale. The review names specific problems
with file/line citations and proposes a remediation plan a successor agent
(or the author) can execute. The review itself does not rewrite — it maps.

## When to use

- User types `/editorial-review`
- User asks to "review the essays," "audit the repo against the rubric," or
  similar
- After a batch of essay additions, promotions, or restructurings
- Periodically (the project has run editorial reviews roughly every 4–6
  weeks; prior reports live in `agent/archive/editorial-review-*.md`)

## Before reviewing: read the rubric

Read `agent/rubrics/repo-audience-experience.md` first. It defines seven
dimensions (Audience paths, Conceptual coherence, Tone and register,
Actionability, Trust and honesty, Navigation and findability,
Delight/experience), each scored 0–3. "Scores highly" means consistently 2–3
across dimensions with no dimension at 0. Use the rubric to guide what you
look for and to justify your scores; then use low scores to drive the
remediation plan.

Also scan the most recent prior review in `agent/archive/editorial-review-*.md`
to see what was flagged last time and whether it was addressed — progress
or drift is part of the current reading.

## Scope

Read the files below. The numbered essays form the theoretical spine; the
rest are supporting material. Context documents define audiences and paths —
use them to evaluate whether the repo serves those audiences. The current
numbered sequence is essays 01 through 12; confirm the live count against
`essays/README.md` before listing.

### Numbered essays (read in order)

Enumerate by globbing `essays/[0-9][0-9]-*.md` and sorting. Do not hardcode
a count — the sequence grows.

### Supporting essays

All other files under `essays/` (supplementary, transcripts, glossary).

### Context documents (read for reference; include in navigation/coherence assessment)

- `essays/README.md` — reading paths and audience definitions
- `README.md` (repo root) — project introduction, who it's for, getting
  started
- `CLAUDE.md` and `AGENTS.md` — repository map and conventions
- `meta/project-state.md` — current state, recent changes

## Target audiences

The `essays/README.md` and root `README.md` define reading paths. Use these
as your lens:

| Audience | What they need | Tolerance for jargon |
|----------|----------------|---------------------|
| **Practitioners** | Concrete understanding of why the methodology works; ability to run a technique | Low — plain language, vivid examples |
| **Theorists** | Rigorous argument, clear logical structure | High — but still demands precision over obscurity |
| **Skeptics** | Evidence, honest acknowledgment of limitations | Low — treat hand-waving as a red flag |
| **Formalists** | Precise definitions, consistent notation | High — but notation must be introduced before use |

## Review dimensions (detail for gathering evidence)

For each dimension below, flag specific problems with file name, line
numbers or section headings, and a concrete suggestion. Findings feed into
the rubric scores and the remediation plan.

### 1. Tone and register consistency

- Does each essay maintain a consistent voice within itself?
- Across the collection, is the register stable? Flag essays that shift
  jarringly without clear reason.
- Is the voice appropriate for target audiences? The project aims for
  "serious but accessible" — flag passages that lapse into dry academese or
  over-casual chat.
- Are there places where the writing talks *down* to the reader or assumes
  expertise not yet established?

### 2. Conceptual coherence and exposition

- **First-use definitions**: Is every key concept defined clearly the first
  time it appears? Flag concepts used before definition.
- **Consistent terminology**: Is the same concept called the same thing
  throughout? Flag synonyms used without acknowledgment.
- **Conceptual hierarchy**: Distinguish abstract principles from their
  concrete instantiations. A general framework and a specific technique that
  implements it are *not* synonyms — they are different levels of
  abstraction. Flag places where the text conflates them, and flag places
  where they are correctly distinguished. (Example: "game within a game" is
  a general principle of self-organization against entropy; the adversarial
  committee is one instantiation of it.)
- **Logical progression**: Within each essay and across the numbered
  sequence, does each idea build on what came before? Flag forward
  dependencies.
- **Cross-references**: Are forward and backward references accurate and
  helpful? Flag broken links, missing cross-references, or circular
  dependencies.

### 3. Audience accessibility

For each reading path, walk the recommended sequence and flag:

- Places where the reader would be lost (concept not yet introduced,
  assumed background)
- Places where the essay overshoots or undershoots the audience
- Whether each path tells a self-contained, coherent story

### 4. Redundancy and gaps

- **Redundancy**: Flag *unproductive* repetition (same point, same way).
  Intentional reinforcement is fine.
- **Gaps**: Concepts introduced but not developed, promises not fulfilled,
  logical steps skipped.
- **Orphaned material**: Sections or essays that don't clearly connect to
  the rest.

### 5. Writing quality

- **Clarity**: Convoluted sentences, ambiguous pronouns, paragraphs that
  could be tightened.
- **Metaphor hygiene**: Extended metaphors (pachinko, immune system, charts
  on a manifold) — flag mixed or overextended use. Note: "game within a
  game" is not a metaphor but a theoretical framework (self-organization
  against entropy); assess whether it is clearly distinguished from its
  primary instantiation (the adversarial committee).
- **Evidence and attribution**: Claims without citation or argument; places
  where a citation would help.
- **Length**: Padded sections that could be tightened without losing
  substance.

### 6. Structural and navigational issues

- Do titles and section headings accurately signal content?
- Is the ordering of numbered essays optimal?
- Does `essays/README.md` (and root README) accurately describe content
  and paths?
- Any miscategorization (Core vs Supplementary)?
- Are cross-directory references (wild/, references/, palgebra/,
  artifacts/, applications/) live, or do they point at moved/archived
  material?

## Output format

Structure the report as follows:

```
## Executive Summary
[2-3 paragraphs: strengths, systemic issues, and how the repo currently
scores against the rubric. State priority recommendations.]

## Rubric Scores
[Table or list: for each dimension in agent/rubrics/repo-audience-experience.md,
give a score 0-3 and 1-2 sentence justification with key evidence
(file/section). Flag dimensions at 0 or 1 as priority.]

## Per-Essay Notes
### [Essay filename]
- **Tone**: [observations]
- **Exposition**: [observations]
- **Accessibility**: [which audiences it serves well/poorly]
- **Specific issues**: [bulleted list with line/section references]

## Cross-Cutting Issues
[Issues spanning multiple essays — terminology drift, repeated material,
missing links, broken cross-references, etc.]

## Recommended Actions
[Prioritized list: what to fix first, what can wait, what's fine as-is.
Tie to rubric dimensions where helpful.]

## Remediation Plan
[Concrete plan to modify the repo's contents so that it scores highly
(2-3 on every dimension) per the rubric. Include:
- **Goals**: Target rubric scores per dimension (or "all 2-3").
- **Prioritized changes**: Ordered list of specific changes. Each item
  should be actionable and traceable to a rubric dimension.
- **Dependencies**: Any order constraints (e.g. fix definitions before
  tightening a path).
- **Out of scope (optional)**: Changes that would improve score but are
  explicitly deferred.]
```

## Where to write the report

By default, write the report to a new file under `agent/` named
`editorial-review-[YYYY-MM-DD].md` (today's date). If a file for today
already exists, append a `-b`/`-c` suffix. When the next editorial review
runs, move the prior report to `agent/archive/` — not this run's job, but
something to flag in the report's "Recommended Actions" if old reports are
cluttering `agent/`.

If the user provides a specific path via argument or chat, write there
instead.

## Constraints

- **Be specific.** Cite file, line or section, and type of fix. "This section
  is unclear" is not useful.
- **Be honest.** If something is strong, say so briefly. Spend analysis on
  problems and on the remediation plan.
- **Distinguish comprehension-affecting issues (high priority) from
  stylistic preferences (low priority).**
- **Do not rewrite content.** Flag issues and suggest the *type* of fix;
  the remediation plan lists concrete modifications for the author or a
  successor agent to execute.
- **Do not grade on a curve.** A 3 means 3 per the rubric definition,
  regardless of how the repo has scored in prior reviews. Progress should
  appear as score changes against a stable standard.
- **Verify links before flagging or citing them.** Cross-reference claims
  rot. A memory of "X lives at Y" is not a claim about current state.

## What success looks like

After running the review, the user should be able to:

- See exactly where the repo is strong and weak by rubric dimension
- Understand what specific changes would raise each low score
- Decide what to fix this sprint vs. defer
- Compare this report to the prior one to see progress or drift
- Hand the remediation plan to a successor agent without further context

## Files reference

- **Rubric**: `agent/rubrics/repo-audience-experience.md`
- **Prior reviews**: `agent/archive/editorial-review-*.md`,
  `agent/archive/editorial-review-report-*.md`
- **Cross-reference audit (related, narrower scope)**:
  `agent/archive/cross-reference-audit-2026-03.md`
- **Repository map**: `CLAUDE.md`, `meta/project-state.md`
