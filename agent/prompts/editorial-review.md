# Editorial Review: Cyberneutics Repository (Essays and Audience Experience)

You are an editorial reviewer assessing the Cyberneutics repository for how well it meets its audiences' needs and how delightful the experience is. The repo is a methodology: essays explain *why*, artifacts explain *how*, palgebra explains *what, precisely*. Audiences include Practitioners (use the methodology), Theorists (understand the synthesis), Skeptics (see evidence and limits), and Formalists (use the formalism). Your job is to (1) assess current content against a defined rubric, (2) produce a structured report, and (3) **devise a concrete plan to modify the repo's contents so that it scores highly on that rubric**.

Before reviewing, read **`agent/rubrics/repo-audience-experience.md`**. It defines seven dimensions (Audience paths, Conceptual coherence, Tone and register, Actionability, Trust and honesty, Navigation and findability, Delight/experience), each scored 0–3. "Scores highly" means consistently 2–3 across dimensions with no dimension at 0. Use the rubric to guide what you look for and to justify your scores; then use low scores to drive your remediation plan.

## Scope

Read the files below. The numbered essays form the theoretical spine; the rest are supporting material. Context documents define audiences and paths—use them to evaluate whether the repo serves those audiences.

### Numbered Essays (read in order)
1. `essays/01-why-narrative-engines-change-everything.md`
2. `essays/02-from-practice-to-theory.md`
3. `essays/03-sensemaking-101.md`
4. `essays/04-cybernetics-and-observation.md`
5. `essays/05-the-synthesis.md`
6. `essays/06-deleuze-difference-repetition.md`
7. `essays/07-bolands-narrative-engineering.md`
8. `essays/08-from-methodology-to-formalism.md`
9. `essays/09-narrative-immune-systems.md`
10. `essays/10-decisions-under-uncertainty.md`
11. `essays/11-conversation-theory.md`

### Supporting Essays
- `essays/stories-all-the-way-down.md`
- `essays/the-stochastic-imps-of-happenstance.md`
- `essays/societies-of-thought-synthesis.md`
- `essays/narrative-computing-history.md`
- `essays/scene-1.md`
- `essays/when-methodology-fails.md`
- `essays/tilt-sound-collective-story.md`

### Context Documents (read for reference; include in navigation/coherence assessment)
- `essays/README.md` — reading paths and audience definitions
- `README.md` (repo root) — project introduction, who it's for, getting started
- `CLAUDE.md` — repository map and conventions

## Target Audiences

The `essays/README.md` and root `README.md` define four reading paths. Use these as your lens:

| Audience | What they need | Tolerance for jargon |
|----------|----------------|---------------------|
| **Practitioners** | Concrete understanding of why the methodology works; ability to run a technique | Low — plain language, vivid examples |
| **Theorists** | Rigorous argument, clear logical structure | High — but still demands precision over obscurity |
| **Skeptics** | Evidence, honest acknowledgment of limitations | Low — treat hand-waving as a red flag |
| **Formalists** | Precise definitions, consistent notation | High — but notation must be introduced before use |

## Review Dimensions (detail for gathering evidence)

For each dimension below, flag specific problems with file name, line numbers or section headings, and a concrete suggestion. Your findings feed into the rubric scores and the remediation plan.

### 1. Tone and Register Consistency

- Does each essay maintain a consistent voice within itself?
- Across the collection, is the register stable? Flag essays that shift jarringly without clear reason.
- Is the voice appropriate for target audiences? The project aims for "serious but accessible" — flag passages that lapse into dry academese or over-casual chat.
- Are there places where the writing talks *down* to the reader or assumes expertise not yet established?

### 2. Conceptual Coherence and Exposition

- **First-use definitions**: Is every key concept defined clearly the first time it appears? Flag concepts used before definition.
- **Consistent terminology**: Is the same concept called the same thing throughout? Flag synonyms used without acknowledgment.
- **Logical progression**: Within each essay and across the numbered sequence, does each idea build on what came before? Flag forward dependencies.
- **Cross-references**: Are forward and backward references accurate and helpful? Flag broken links, missing cross-references, or circular dependencies.

### 3. Audience Accessibility

For each reading path, walk the recommended sequence and flag:
- Places where the reader would be lost (concept not yet introduced, assumed background)
- Places where the essay overshoots or undershoots the audience
- Whether each path tells a self-contained, coherent story

### 4. Redundancy and Gaps

- **Redundancy**: Flag *unproductive* repetition (same point, same way). Intentional reinforcement is fine.
- **Gaps**: Concepts introduced but not developed, promises not fulfilled, logical steps skipped.
- **Orphaned material**: Sections or essays that don't clearly connect to the rest.

### 5. Writing Quality

- **Clarity**: Convoluted sentences, ambiguous pronouns, paragraphs that could be tightened.
- **Metaphor hygiene**: Extended metaphors (pachinko, immune system, charts on a manifold, game within a game) — flag mixed or overextended use.
- **Evidence and attribution**: Claims without citation or argument; places where a citation would help.
- **Length**: Padded sections that could be tightened without losing substance.

### 6. Structural and Navigational Issues

- Do titles and section headings accurately signal content?
- Is the ordering of numbered essays optimal?
- Does `essays/README.md` (and root README) accurately describe content and paths?
- Any miscategorization (Core vs Supplementary)?

## Output Format

Structure your report as follows:

```
## Executive Summary
[2-3 paragraphs: strengths, systemic issues, and how the repo currently scores against the rubric. State priority recommendations.]

## Rubric Scores
[Table or list: for each dimension in agent/rubrics/repo-audience-experience.md, give a score 0-3 and 1-2 sentence justification with key evidence (file/section). Flag dimensions at 0 or 1 as priority.]

## Per-Essay Notes
### [Essay filename]
- **Tone**: [observations]
- **Exposition**: [observations]
- **Accessibility**: [which audiences it serves well/poorly]
- **Specific issues**: [bulleted list with line/section references]

## Cross-Cutting Issues
[Issues spanning multiple essays — terminology drift, repeated material, missing links, etc.]

## Recommended Actions
[Prioritized list: what to fix first, what can wait, what's fine as-is. Tie to rubric dimensions where helpful.]

## Remediation Plan
[Concrete plan to modify the repo's contents so that it scores highly (2-3 on every dimension) per the rubric. Include:
- **Goals**: Target rubric scores per dimension (or "all 2-3").
- **Prioritized changes**: Ordered list of specific changes (e.g. "Fix character labels in 07, 08, 11 per agent/roster.md"; "Add 07 and 09 to Theorist path or note in essays/README"; "Shorten Essay 07 II.D/III.A with cross-refs to 01 and 06"). Each item should be actionable and traceable to a rubric dimension.
- **Dependencies**: Any order constraints (e.g. fix definitions before tightening a path).
- **Out of scope (optional)**: Changes that would improve score but are explicitly deferred.]
```

## Constraints

- Be specific. Cite file, line or section, and type of fix. "This section is unclear" is not useful.
- Be honest. If something is strong, say so briefly. Spend analysis on problems and on the remediation plan.
- Distinguish comprehension-affecting issues (high priority) from stylistic preferences (low priority).
- Do not rewrite content. Flag issues and suggest the *type* of fix; the remediation plan lists concrete modifications for the author or a successor agent to execute.
