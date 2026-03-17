# Cyberneutics Onboarding Core

## What this repo is

Cyberneutics is a methodology for working with LLMs as collaborative sense-making partners. It treats LLMs as narrative engines rather than answer machines and focuses on rigorous, traceable decisions under genuine uncertainty. The repository is organized as:

- essays: why the methodology works
- artifacts: how to apply it
- palgebra: what the pipelines mean formally
- examples: checked-in example and historical run records
- agent: operational repo metadata for successor agents

For general orientation, read `README.md`.

## Session start

1. Read the most recent `agent/handoff-[YYYY-MM-DD]*.md`.
2. Read `meta/project-state.md` for current architecture truths and open decisions.
3. If `/committee`, `/scenarios`, or `/probe` is relevant, check the resolved situations root for prior runs on related topics before starting a new one.
4. Do not search `agent/archive/` during onboarding. It is historical only. Use it only when the task explicitly calls for provenance or historical reconstruction.

## Repository map

| Directory | Contains | Read when you need to... |
|-----------|----------|--------------------------|
| `essays/` | Theoretical foundations | Understand why the methodology works. |
| `artifacts/` | Techniques, templates, guides | Apply the methodology in practice. |
| `palgebra/` | Formal pipeline algebra | Write or inspect resource equations and composition rules. |
| `applications/` | Domain analyses | See the methodology applied to a real subject area. |
| `meta/` | Methodology evolution and project state | Understand current truths, open decisions, and validation status. |
| `examples/` | Checked-in scenario and deliberation records | Reference example runs and historical records that stay in the repo. |
| `research-programs/` | Evidence-building plans and study designs | Plan or execute empirical validation of the methodology. |
| `wild/` | Incoming ideas, external material, diary | Explore adjacent territory that is not yet integrated. |
| `references/` | Background reading | Find cited theoretical sources. |
| `agent/` | Handoffs, rosters, prompts, rubrics | Continue ongoing work inside this repo. |
| `.claude/skills/` | Canonical skill definitions | Follow cyberneutics workflows. |
| `.claude/commands/` | Thin Claude command wrappers | Discover slash commands in Claude without duplicating skill bodies. |
| `.cursor/commands/` | Thin Cursor command wrappers | Discover slash commands in Cursor without duplicating skill bodies. |

### `agent/` in more detail

- `handoff-[YYYY-MM-DD]*.md`: most recent session handoff; read this first
- `roster.md`: committee character roster
- `scenario-roster.md`: scenario-generation roster
- `prompts/`: reusable prompts for repo maintenance and research
- `rubrics/`: repo-review rubrics and evaluation criteria
- `archive/`: historical only; excluded from onboarding unless explicitly needed

### `wild/` in more detail

- `diary/`: field notes and idea-connection sketches; the most exploratory material in the repo
- Topic directories (e.g. `residuality-theory/`, `pask-mesh-fitting/`): incoming ideas being tamed

### `examples/` in more detail

- `examples/scenarios/`: checked-in scenario-generation runs kept as examples or historical records
- `examples/deliberations/`: checked-in committee runs kept as examples or historical records

These are not live runtime output locations. New runs belong in external situation directories.

## Situations and live outputs

Skill outputs are written outside the repo into situation directories. Cyberneutics is the methodology; the situation directory is the work product.

Location resolution:

1. `--situation <path>` on invocation
2. `situations_root` in `.claude/cyberneutics-config.yaml`, plus `<topic-slug>/`
3. default: `~/situations/<topic-slug>/`

Situation layout:

```text
<situation-dir>/
  situation.md
  scenarios/
  deliberations/
  probes/
```

Rosters always come from this repo (`agent/roster.md`, `agent/scenario-roster.md`). Live outputs do not.

## Skills and commands

Canonical skill bodies live only in `.claude/skills/`. Do not create a duplicate repo-local skill tree for other tools.

Compatibility model:

- Claude: discover workflows via `.claude/commands/`, then follow `.claude/skills/<name>/SKILL.md`
- Cursor: discover workflows via `.cursor/commands/`, then follow `.claude/skills/<name>/SKILL.md`
- Codex and other agents without repo-local skill discovery: open `.claude/skills/<name>/SKILL.md` manually and follow it

Available workflows:

| Command | Canonical skill doc | Use when... |
|---------|----------------------|-------------|
| `/committee [topic]` | `.claude/skills/committee/SKILL.md` | The user faces a complex decision, competing values, or asks what is being missed. |
| `/scenarios [situation]` | `.claude/skills/scenarios/SKILL.md` | The main uncertainty is what might happen. |
| `/probe [situation]` | `.claude/skills/probe/SKILL.md` | The user needs repeated fan->funnel runs to map the decision landscape. |
| `/review` | `.claude/skills/review/SKILL.md` | A committee run needs independent evaluation. |
| `/handoff` | `.claude/skills/handoff/SKILL.md` | The session is ending or continuity matters. |
| `/string-diagram` | `.claude/skills/string-diagram/SKILL.md` | A workflow should be formalized as resource equations or Mermaid. |

Read the relevant `SKILL.md` before using any of these workflows.

## Key vocabulary

The methodology distinguishes two trust regimes:

- **Organ**: a controlled channel with defined inputs, outputs, and inspectable transformations. You trust it because you built it and can verify the chain of custody. Internal trust, controlled transformations.
- **Bloodstream**: an ambient medium carrying unprovenanced material. The receiving tissue must judge what to absorb and what to reject. External judgment required, mixed provenance.

Older material may use "pipeline" and "bath" as synonyms for organ and bloodstream. The current terms are organ/bloodstream. "Pipeline" also appears in non-metaphorical senses (committee pipeline, fan/funnel pipeline, pipeline algebra) — those are unrelated to this distinction.

For the full glossary, see `essays/glossary.md`.

## Working style

- Ask clarifying questions when the ambiguity is itself the problem.
- Offer multiple approaches when tradeoffs are real.
- Show your reasoning transparently.
- Use the methodology on itself when it helps.
- Treat provenance as part of the deliverable, not decoration.
- Avoid collapsing prematurely to one answer when the situation is genuinely uncertain.