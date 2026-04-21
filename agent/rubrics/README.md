# Agent Rubrics

Rubrics used by agent prompts and skills to score or evaluate repo artifacts. Distinct from the committee deliberation rubrics in [artifacts/evaluation-rubrics-reference.md](../../artifacts/evaluation-rubrics-reference.md) (those evaluate deliberation transcripts).

| Rubric | Purpose | Used by |
|--------|---------|--------|
| [repo-audience-experience.md](repo-audience-experience.md) | Score repository contents for how well they meet audience needs and how delightful the reader experience is (0–3 per dimension). | [`/editorial-review`](../../.claude/skills/editorial-review/SKILL.md) — editorial review produces scores and a remediation plan to raise them. |

**Scoring**: Each dimension is 0–3. "High" = consistently 2–3 with no dimension at 0. The `/editorial-review` skill instructs the reviewer to devise a plan so the repo scores highly per this rubric.
