# Deliberation Records

This directory holds **directory-structured deliberation records** produced by the cyberneutics committee skill. Every `/committee [topic]` run creates a new subdirectory here (e.g. `agent/deliberations/microservices-adoption/`) and writes the standard set of files; there is no single-file or inline-only output. The review skill reads from these directories and can write the evaluation file. The **example/** subdirectory contains minimal template files showing the structure.

## Naming convention

Filenames are **`<chronology>-<type>[-<suffix>].md`**:

- **Numeric prefix (00, 01, 02, …)** = **chronology index** — order in the process. They are not file-type IDs; they ensure files sort in chronological order.
- **The rest of the name** = **type** — charter, roster, convening, deliberation, resolution, evaluation, remediation, etc.
- **Optional suffix** — When there is more than one instance of the same type, use **incrementing suffixes** (-1, -2, …) to keep filenames unique: e.g. `04-evaluation-1.md`, `04-evaluation-2.md` (multiple reviews); `05-remediation-1.md`, `05-remediation-2.md` (multiple remediation rounds).

So the "real" type is the type name (charter, deliberation, …); the number is when it occurs in the sequence. When the feedback loop runs (evaluate → remediate → re-evaluate → …), both evaluations and remediations can have multiple instances; the **chronology index** (04, 05, 06, 07, …) increments for each new file so lexical sort stays chronological (e.g. 04-evaluation-1 → 05-remediation-1 → 06-evaluation-2 → 07-remediation-2).

## Structure (per deliberation)

| File | Type | Purpose |
|------|------|---------|
| `00-charter.md` | charter | Goal, context, success criteria, exit conditions, deliverable format |
| `01-roster.md` | roster | Committee roster (copied from `agent/roster.md`); roles and propensities |
| `01-convening.md` | convening | Selection rationale, composition notes, outcome. Optional **Remediation parameters** (for the evaluation feedback loop): **remediation_threshold** (default 13; pass if sum of five rubric scores ≥ this), **max_remediation_rounds** (default 2). Add a short "Remediation parameters" section when this deliberation uses non-default values. |
| `02-deliberation.md` | deliberation | Full transcript: opening statements, rounds, analyses, consensus, decision space map |
| `03-resolution.md` | resolution | Decision, summary, votes, optional **confidence** (per-member integer 1–4 for metacognition; see `artifacts/metacognition-and-committee-veracity.md`), implementation plan, signatures |
| `04-evaluation-1.md` | evaluation | First review: resolution-only evaluation and/or transcript review (rubric scores, verdict). **Always use a number** for the first evaluation file (04-evaluation-1.md). |
| `04-evaluation-2.md`, … | evaluation | Subsequent reviews after remediation rounds (suffix -2, -3, …). |
| `05-remediation-1.md`, … | remediation | Committee's response to evaluation (point-by-point, new round in 02). Present when the deliberation "went overtime." Suffix for each remediation round. |

Optional (when evaluation feedback loop runs): `05-remediation-1.md`, then `06-evaluation-2.md`, then `07-remediation-2.md`, then `08-evaluation-3.md`, etc. (chronology index increments so order is preserved).

**Evaluation files** (04-evaluation-1.md, 04-evaluation-2.md, …) can contain (both optional):

- **resolution_evaluation** — Charter vs resolution only (no transcript). Reviewer reads `00-charter.md` and `03-resolution.md`, scores alignment_with_goal, completeness, feasibility, risk_mitigation; writes outcome (RATIFIED | REVISE | REJECT), critique, recommendation. Request via the review skill: e.g. "evaluate the resolution" or "run resolution-only evaluation" for this directory.
- **transcript_review** — Full transcript evaluation. Reviewer reads `02-deliberation.md` (and optionally `00-charter.md`), scores the five rubrics (reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness), writes verdict (High/Medium/Low), biggest_gaps, recommendations. Produced when you run `/review agent/deliberations/<topic-slug>`; the review skill writes to the appropriate evaluation file (04-evaluation-1.md for first review, 04-evaluation-2.md after first remediation, etc.).

All paths and references stay **under the cyberneutics repository**. Roster and character details come from `agent/roster.md` (operational definitions) and `artifacts/character-propensity-reference.md` (extended commentary); evaluation rubrics from `.claude/skills/review/SKILL.md` and `artifacts/evaluation-rubrics-reference.md`.

See **agent/archive/augmentation-plan.md** for full schemas and implementation details; **agent/investigation-report.md** for how this structure was derived.

**Resolution and metacognition:** When the committee records confidence (1–4 per member at resolution), it is stored in `03-resolution.md` under `confidence:` (same keys as `votes`). **Purpose:** Metacognition helps the end user interpret the committee — whose confidence to trust — not change the committee's decision. To track confidence and accuracy **across runs**, run `python scripts/update_metacog_register.py`; the result is `agent/metacog_register.md`. See `artifacts/metacognition-and-committee-veracity.md` for the full picture and optional HMeta-d/build_metacog_counts.

## File format: all files are Markdown

All deliberation record files use **Markdown** (`.md`). Files that carry structured data (charter, roster, resolution, evaluation) store it in **YAML front matter** (delimited by `---`). Files that are primarily narrative (convening, deliberation, remediation) use standard Markdown with optional front matter.

This uniform format means every artifact in the pipeline is a **decorated text** in the palgebra sense: `(text, metadata)` where metadata lives in YAML front matter and text lives in the body. Structured-data files simply have an empty (or minimal) body — the front matter carries the payload. This eliminates special-casing: all files can be read, enriched, and gated with the same operations regardless of whether their content is primarily structured or narrative.
