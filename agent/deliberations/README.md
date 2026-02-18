# Deliberation Records

This directory holds **directory-structured deliberation records** produced by the cyber-sense committee and review skills. Each subdirectory is one deliberation, named by a topic slug (e.g. `microservices-migration`, `is-author-crackpot`). The **example/** subdirectory contains minimal template files showing the 00–04 structure; real runs create a new directory per topic (e.g. `agent/deliberations/my-topic/`).

## Structure (per deliberation)

| File | Phase | Purpose |
|------|--------|---------|
| `00-charter.yml` | Charter | Goal, context, success criteria, exit conditions, deliverable format |
| `01-roster.yml` | Convening | Fixed 5-member committee (Maya, Frankie, Joe, Vic, Tammy); roles and propensities |
| `01-convening.md` | Convening | Selection rationale, composition notes, outcome |
| `02-deliberation.md` | Deliberation | Full transcript: opening statements, rounds, analyses, consensus, decision space map |
| `03-resolution.yml` | Resolution | Decision, summary, votes, implementation plan, signatures |
| `04-evaluation.yml` | Evaluation | Resolution-only evaluation and/or transcript review (rubric scores, verdict) |

**04-evaluation.yml** can contain two sections (both optional):

- **resolution_evaluation** — Charter vs resolution only (no transcript). Reviewer reads `00-charter.yml` and `03-resolution.yml`, scores alignment_with_goal, completeness, feasibility, risk_mitigation; writes outcome (RATIFIED | REVISE | REJECT), critique, recommendation. Request via the review skill: e.g. "evaluate the resolution" or "run resolution-only evaluation" for this directory.
- **transcript_review** — Full transcript evaluation. Reviewer reads `02-deliberation.md` (and optionally `00-charter.yml`), scores the five rubrics (reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness), writes verdict (High/Medium/Low), biggest_gaps, recommendations. Produced when you run `/review agent/deliberations/<topic-slug>`; the review skill can write this section into 04-evaluation.yml so one file holds both evaluations.

All paths and references stay **under the cyber-sense repository**. Roster and character details come from `.claude/skills/committee/SKILL.md` and `artifacts/character-propensity-reference.md`; evaluation rubrics from `.claude/skills/review/SKILL.md` and `artifacts/evaluation-rubrics-reference.md`.

See **agent/augmentation-plan.md** for full schemas and implementation details; **agent/investigation-report.md** for how this structure was derived.
