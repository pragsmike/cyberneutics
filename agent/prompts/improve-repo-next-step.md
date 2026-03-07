# Improve This Repo: Next Highest-Value Change

Onboard to this repository by reading `agent/onboarding-core.md`, the latest `agent/handoff-*.md`, and `meta/project-state.md`. Then audit the repo for the next highest-value improvement now that the 2026-03-07 compatibility remediation is complete.

## Constraints

- Treat `agent/onboarding-core.md` and `meta/project-state.md` as canonical.
- Do not search `agent/archive/` during onboarding.
- Treat `examples/` as historical/example material, not live runtime output.
- If the task matches a repo skill workflow, open the relevant `.claude/skills/<name>/SKILL.md` manually and follow it.
- Prefer concrete repo changes over abstract advice.

## Deliverables

1. Identify the single best next improvement, with a short rationale tied to current repo state.
2. Implement it end to end in the repo.
3. Add or update validation where appropriate.
4. Run the relevant checks.
5. Report:
   - what changed
   - why this was the right next improvement
   - any risks or follow-up work

## Bias

Bias toward improvements that strengthen one of these areas:

- documentation consistency after the compatibility sweep
- structural linting or guardrails
- onboarding clarity
- unresolved stale or redirect surfaces
- evidence-building or methodology validation support where the repo is currently thin
