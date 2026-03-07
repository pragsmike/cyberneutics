# Working with Cyberneutics in Codex

Read `agent/onboarding-core.md` first. It is the canonical onboarding source for this repository.

Codex-specific notes:

- Read the most recent `agent/handoff-[YYYY-MM-DD]*.md` and `meta/project-state.md` before substantial work.
- Do not search `agent/archive/` during onboarding. It is historical only.
- Codex does not auto-discover repo-local skills in this environment. When a task matches `/committee`, `/scenarios`, `/probe`, `/review`, `/handoff`, or `/string-diagram`, open the corresponding `.claude/skills/<name>/SKILL.md` manually and follow it.
- Canonical skill bodies live only in `.claude/skills/`. Do not create a duplicate Codex skill tree.
- Treat external situation directories as the only live output location. Checked-in records under `examples/` are examples or historical records only.