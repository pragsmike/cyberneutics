# Project State

Last updated: 2026-03-07

This document is the canonical current-state reference for repo structure, compatibility truths, and live open questions. It replaces the old stale backlog-file role with a narrower, actively maintained state doc.

## Current architecture truths

- `agent/onboarding-core.md` is the canonical onboarding source.
- `AGENTS.md` and `CLAUDE.md` are thin tool-specific entry points.
- Canonical skill bodies live only in `.claude/skills/`.
- Claude and Cursor command discovery is handled by thin wrappers in `.claude/commands/` and `.cursor/commands/`.
- Live outputs belong in external situation directories resolved via `--situation`, `.claude/cyberneutics-config.yaml`, or `~/situations/<topic-slug>/`.
- Checked-in run records in this repo are examples or historical records. They are not live runtime outputs.
- `agent/archive/` is historical only and excluded from onboarding unless provenance is explicitly requested.

## Compatibility migration status

- Canonical onboarding doc established.
- Root wrappers aligned to the canonical onboarding doc.
- Canonical skill-source rule established: `.claude/skills/` only.
- Repo-local command wrappers added for Claude and Cursor.
- Live-doc sweep is moving runtime-path language to situation-directory language.
- Checked-in scenario and deliberation records are being labeled and housed as examples, not runtime state.
- Structural linting exists to keep these invariants from drifting again.

## Open decisions

- Whether to record rubric scores as persistent metadata beyond the current review artifacts.
- Whether the cowork plugin should ship under MIT, and whether its runtime behavior needs additional validation before stronger claims are made.
- When to rerun the editorial review after the compatibility sweep settles.

## Scheduled reviews

- **2026-06-08 — Contributor gatekeeping changes**: Has anyone contributed to `wild/` or `wild/diary/`? Has the diary-to-wild-to-formalization pipeline worked for external contributors? Has the maintainer labor model held? Source: `meta/deliberations/contributor-gatekeeping/03-resolution.md`.

## Blocked or prerequisite-dependent items

- A full empirical failure case for `essays/when-methodology-fails.md` still depends on real practice data.
- Some evidence-building tasks in `research-programs/` still depend on running fresh situation-directory workflows rather than repo-local examples.

## Docs still needing sweep

- None currently expected after the 2026-03-07 compatibility remediation completes.
- If this becomes stale, update this section rather than reintroducing a catch-all backlog file.
