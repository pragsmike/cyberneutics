# Repository Review and Run/Test Guide

**Purpose:** Practical guide to what is runnable in this repository, where live outputs belong, and how to validate the repo structurally.

---

## 1. What this repository is

Cyberneutics is primarily methodology documentation plus a small executable surface.

- **Essays** explain why narrative engineering is needed.
- **Artifacts** explain how to run the techniques.
- **Palgebra** formalizes the pipelines.
- **Canonical skills** live in `.claude/skills/`.
- **Command discovery wrappers** live in `.claude/commands/` and `.cursor/commands/`.
- **One script** lives at `.claude/skills/string-diagram/resource_equations_to_mermaid.py`.

So "running" the repo has two meanings:

1. Run the methodology inside an AI session.
2. Run the string-diagram script directly.

---

## 2. Live outputs vs. checked-in examples

### Live outputs

Live committee, scenario, review, and probe runs belong in an external **situation directory**.

Resolution order:

1. `--situation <path>`
2. `situations_root` from `.claude/cyberneutics-config.yaml`, plus `<topic-slug>/`
3. `~/situations/<topic-slug>/`

Expected layout:

```text
<situation-dir>/
  situation.md
  scenarios/
  deliberations/
  probes/
```

### Checked-in examples

Repo-kept example and historical records live under:

- `examples/scenarios/`
- `examples/deliberations/`

These are reference material, not runtime targets.

---

## 3. How to run the methodology

### Prerequisites

- Read `agent/onboarding-core.md`, the latest `agent/handoff-*.md`, and `meta/project-state.md`.
- `agent/roster.md` exists for committee runs.
- `agent/scenario-roster.md` exists for scenario runs.
- You have a concrete topic or situation.

### Command surface

| Workflow | Canonical doc | Output location |
|----------|---------------|-----------------|
| `/committee [topic]` | `.claude/skills/committee/SKILL.md` | `<situation-dir>/deliberations/` |
| `/scenarios [situation]` | `.claude/skills/scenarios/SKILL.md` | `<situation-dir>/scenarios/` |
| `/review --situation <path>` | `.claude/skills/review/SKILL.md` | `<situation-dir>/deliberations/` |
| `/probe [situation]` | `.claude/skills/probe/SKILL.md` | `<situation-dir>/probes/` |
| `/handoff` | `.claude/skills/handoff/SKILL.md` | `agent/handoff-*.md` |
| `/string-diagram` | `.claude/skills/string-diagram/SKILL.md` | User-chosen file or inline Mermaid |

### Tool compatibility

- **Claude** discovers workflows through `.claude/commands/`.
- **Cursor** discovers workflows through `.cursor/commands/`.
- **Codex** reads `.claude/skills/<name>/SKILL.md` manually.

### Recommended first run

1. Use [artifacts/quick-start-guide.md](../artifacts/quick-start-guide.md).
2. Try `/committee Should we hire two juniors or one senior?`
3. If the output matters enough to inspect formally, run `/review --situation <path-to-situation-dir>`.

### Deliberated choice

1. Run `/scenarios [situation]`.
2. Review the scenario set in `<situation-dir>/scenarios/`.
3. Run `/committee [decision question] --situation <path-to-situation-dir>`.
4. The committee auto-detects the scenarios already present in that situation directory.

---

## 4. How to run the code

The only direct code artifact in the repo is the string-diagram converter.

```bash
python .claude/skills/string-diagram/resource_equations_to_mermaid.py <equations.txt> [-o output.mermaid]
```

Example inputs:

- `.claude/skills/string-diagram/decision-monad-equations.txt`
- `.claude/skills/string-diagram/ai-study-equations.txt`
- `.claude/skills/string-diagram/lemon-pie-equations.txt`

Smoke test:

```bash
python scripts/test_string_diagram.py
```

---

## 5. How to test the repository

### Automated checks

- `python scripts/test_string_diagram.py`
- `python scripts/lint_repo_docs.py`

### What the structural lint should enforce

- No live references to the removed gap-analysis backlog file
- Onboarding docs explicitly exclude `agent/archive/` during onboarding
- No live docs describe repo-local `agent/` run-record directories as runtime output locations
- No live docs point to a duplicate repo-local Codex skill surface
- Indexed docs exist where the indexes claim they do

### Manual checks

- Confirm a live situation directory receives `situation.md` plus `scenarios/`, `deliberations/`, or `probes/` as appropriate.
- Confirm `/review --situation <path>` writes the next evaluation file in `<situation-dir>/deliberations/`.
- Spot-check checked-in examples under `examples/` for schema and naming consistency.

---

## 6. Related docs

- `agent/onboarding-core.md`: canonical onboarding instructions
- `meta/project-state.md`: current architecture truths and open decisions
- `examples/deliberations/README.md`: naming and structure for checked-in example deliberation records
- `artifacts/quick-start-guide.md`: fastest path to a first run
- `artifacts/deliberated-choice-workflow.md`: fan->funnel workflow guide