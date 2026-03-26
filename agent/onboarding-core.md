# Cyberneutics Onboarding Core

## What this repo is

Cyberneutics is a methodology for harnessing LLMs as structured sense-making tools. It treats LLMs as narrative engines rather than answer machines and focuses on rigorous, traceable decisions under genuine uncertainty. The repository is organized as:

- essays: why the methodology works
- artifacts: how to apply it
- palgebra: what the pipelines mean formally
- examples: checked-in example and historical run records
- agent: operational repo metadata for successor agents

For general orientation, read `README.md`.

## Session start

0. **Confirm repo root.** All paths in this document are relative to the repository root. List the contents of `agent/` and confirm you can see files including `onboarding-core.md`, `roster.md`, and one or more `handoff-*.md` files. If you see nothing or get errors, your working directory is not the repo root — resolve the correct path before proceeding. (Common in Cowork, sandboxed environments, and IDE configurations where the working directory differs from the project root.)
1. List the files in `agent/` and read the most recent `handoff-[YYYY-MM-DD]*.md` (by date in the filename). You should see at least one handoff file. If you see none, recheck your path resolution per step 0 — do not assume they have been archived.
2. Read `meta/project-state.md` for current architecture truths and open decisions.
3. If `/committee`, `/scenarios`, or `/probe` is relevant, check the resolved situations root for prior runs on related topics before starting a new one.
4. Do not search archive directories during onboarding — they are historical only. This includes `agent/archive/` and `wild/archive/`. Use them only when the task explicitly calls for provenance or historical reconstruction.

## Repository map

| Directory | Contains | Read when you need to... |
|-----------|----------|--------------------------|
| `essays/` | Theoretical foundations | Understand why the methodology works. |
| `artifacts/` | Techniques, templates, guides | Apply the methodology in practice. |
| `palgebra/` | Formal pipeline algebra | Write or inspect resource equations and composition rules. **Epistemic status: provisionally useful but untrusted** — see "Epistemic positions" below. |
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
- `archive/`: historical only; excluded from onboarding unless explicitly needed (see step 4 above)

### `wild/` in more detail

- `diary/`: field notes and idea-connection sketches; the most exploratory material in the repo
- Topic directories (e.g. `committee-games/`, `pask-mesh-fitting/`): incoming ideas being tamed
- `archive/`: dormant topics (historical only; excluded from onboarding unless explicitly needed)

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

- Claude: auto-loads `CLAUDE.md`; discover workflows via `.claude/commands/`, then follow `.claude/skills/<name>/SKILL.md`
- Cursor: auto-loads `.cursor/rules`; discover workflows via `.cursor/commands/`, then follow `.claude/skills/<name>/SKILL.md`
- Codex and other agents without repo-local skill discovery (including Antigravity): open `.claude/skills/<name>/SKILL.md` manually and follow it
- Cowork: `CLAUDE.md` is injected as system context but the working directory is not the repo root. Follow step 0 above to anchor paths before proceeding.

Available workflows:

| Command | Canonical skill doc | Use when... |
|---------|----------------------|-------------|
| `/committee [topic]` | `.claude/skills/committee/SKILL.md` | The user faces a complex decision, competing values, or asks what is being missed. |
| `/scenarios [situation]` | `.claude/skills/scenarios/SKILL.md` | The main uncertainty is what might happen. |
| `/probe [situation]` | `.claude/skills/probe/SKILL.md` | The user needs repeated fan->funnel runs to map the decision landscape. |
| `/review` | `.claude/skills/review/SKILL.md` | A committee run needs independent evaluation. |
| `/handoff` | `.claude/skills/handoff/SKILL.md` | The session is ending or continuity matters. |
| `/string-diagram` | `.claude/skills/string-diagram/SKILL.md` | A workflow should be formalized as resource equations or Mermaid. |
| `/diary` | `.claude/skills/diary/SKILL.md` | Writing or drafting diary entries for `wild/diary/`; or a conversation produces exploratory ideas that should be recorded. |

Read the relevant `SKILL.md` before using any of these workflows.

## Key vocabulary

The methodology distinguishes two trust regimes:

- **Organ**: a controlled channel with defined inputs, outputs, and inspectable transformations. You trust it because you built it and can verify the chain of custody. Internal trust, controlled transformations.
- **Bloodstream**: an ambient medium carrying unprovenanced material. The receiving tissue must judge what to absorb and what to reject. External judgment required, mixed provenance.

Older material may use "pipeline" and "bath" as synonyms for organ and bloodstream. The current terms are organ/bloodstream. "Pipeline" also appears in non-metaphorical senses (committee pipeline, fan/funnel pipeline, pipeline algebra) — those are unrelated to this distinction.

For the full glossary, see `essays/glossary.md`.

## Epistemic positions the agent must know

### Committee value: inspectability, not (just) decision quality

The committee's core value proposition is **inspectable reasoning records**, not superior decision outcomes. Solo evaluation can reach good decisions but does not reliably produce an audit trail. The deliberation transcript *is* the product, not a byproduct. This is a separate axis from whether the committee outperforms simpler approaches on decision quality (which is what the ablation study tests). Both claims matter, but they are independent — and the inspectability claim holds regardless of ablation results.

### Formal work is provisionally useful but untrusted

The deep mathematical analyses — palgebra, furry logic, open games translation — are **provisionally useful but untrusted** until a human expert evaluates them. LLM-generated mathematics should not be treated as established results. This connects directly to the ACT outreach: one reason to engage the Cybercat community is to get qualified eyes on whether the categorical constructions actually work. The formal outputs are working hypotheses, not theorems. Do not cite them as proven; do cite them as structurally useful for organizing thinking.

### LLM-steered mathematical inquiry as a research program

The formal work is simultaneously **subject matter and test case** for the methodology. We are using the cyberneutics framework to push LLMs into doing real mathematics, which means the palgebra and furry logic analyses are not just categorical theory — they are empirical data about how well LLM pipelines can do mathematics when harnessed through structured deliberation. The interesting questions are: How do we steer LLM pipelines to do reliable mathematics? How do we know when they have? What does the calibration register need to track to support this? What is the role of human expert verification in the loop? This is distinct from both the metacognition research program (SDT calibration) and the ablation study (does the committee help?). It sits at the meta-level: the epistemics of LLM-assisted formal reasoning. See `wild/` for a rough outline of this program.

## Working style

- Ask clarifying questions when the ambiguity is itself the problem.
- Offer multiple approaches when tradeoffs are real.
- Show your reasoning transparently.
- Use the methodology on itself when it helps.
- Treat provenance as part of the deliverable, not decoration.
- Avoid collapsing prematurely to one answer when the situation is genuinely uncertain.