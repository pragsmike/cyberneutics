# Task: Build the cyberneutics Cowork plugin inside this repo

## Where to put it

Create a `cowork-plugin/` directory at the root of this repo. Everything below lives inside it. Do **not** modify any existing repo files.

## Read first — before writing anything

Read these files in order. They contain everything you need to understand the methodology before packaging it:

1. `CLAUDE.md` — orientation, working style, core ideas
2. `agent/roster.md` — the five committee characters verbatim
3. `.claude/skills/committee/SKILL.md` — committee deliberation protocol
4. `.claude/skills/scenarios/SKILL.md` — scenario generation protocol
5. `.claude/skills/probe/SKILL.md` — decision landscape mapping
6. `.claude/skills/review/SKILL.md` — evaluation rubric
7. `.claude/skills/handoff/SKILL.md` — session handoff
8. `.claude/skills/string-diagram/SKILL.md` — palgebra / pipeline notation
9. `palgebra/reference.md` — resource equation syntax
10. `essays/README.md` — to understand the reading paths by audience

Only after reading all of these, proceed.

## Plugin structure to create

```
cowork-plugin/
├── .claude-plugin/
│   └── plugin.json
├── .mcp.json
├── README.md
├── agents/                      ← one file per committee character
│   ├── maya.md
│   ├── frankie.md
│   ├── joe.md
│   ├── vic.md
│   └── tammy.md
├── commands/
│   ├── committee.md
│   ├── scenarios.md
│   ├── probe.md
│   ├── review.md
│   ├── handoff.md
│   └── string-diagram.md
└── skills/
    ├── orientation/
    │   └── SKILL.md
    ├── fan-funnel/
    │   └── SKILL.md
    ├── palgebra/
    │   └── SKILL.md
    └── committee/
        └── SKILL.md
```

---

## Step-by-step instructions

### Step 1: `.claude-plugin/plugin.json`

```json
{
  "name": "cyberneutics",
  "version": "0.1.0",
  "description": "Narrative engineering for decisions under genuine uncertainty. Committee deliberation with independent agents, scenario generation, and decision landscape mapping for knowledge workers.",
  "author": "mg"
}
```

### Step 2: `.mcp.json`

```json
{}
```

No external connectors in v1. The plugin is self-contained.

### Step 3: `agents/` — one file per committee character

Subagents are defined as markdown files with YAML frontmatter. Each committee character gets their own agent file so they can run independently with genuine context isolation — not simulated turns in a single conversation.

Create one file per character. Use the character descriptions verbatim from `agent/roster.md` as the core of each agent's system prompt. The frontmatter fields are:

```yaml
---
name: <character-name>
description: <one sentence — when the orchestrator should invoke this agent>
---
```

After the frontmatter, write a system prompt for the character that includes:
- Their role and disposition (from roster.md, verbatim)
- Their analytical lens and what they habitually look for
- Their characteristic objections and blind spots
- An instruction: "You are participating in a committee deliberation on the topic you are given. Produce your opening position clearly. Then, when given other characters' positions, produce your response. Stay in character throughout. Do not converge prematurely — your value is in the distinctiveness of your perspective."
- An instruction to conclude every position statement with: "**Confidence**: [Low/Medium/High] — [one sentence explaining why]"

The `description` field in the frontmatter is what the orchestrator uses to decide which agent to invoke. Write it so it's clearly tied to each character's role in deliberation, e.g.:
- Maya: "Invoke for rigorous systems analysis and long-term structural critique of a position or proposal"
- Frankie: "Invoke for operational feasibility check — what breaks in practice, what the implementation reality is"
- (etc., based on the actual roster)

### Step 4: `commands/committee.md`

This is the most important command. It must explicitly orchestrate the five character agents in parallel, collect their outputs, and run the synthesis and evaluation stages.

The command file should:

1. **Describe the command** in plain language for a first-time user: what it does, what input to provide, what output to expect.

2. **Specify the orchestration protocol** explicitly:

   ```
   When this command is invoked with a topic or decision:
   
   STAGE 1 — Charter (you, the orchestrator)
   Draft a one-paragraph charter: restate the topic as a genuine question, identify what kind of uncertainty is present, name what a good deliberation would produce. Output this before invoking any agents.
   
   STAGE 2 — Independent positions (parallel agent invocation)
   Invoke all five character agents simultaneously, each with:
   - The original topic/question
   - The charter from Stage 1
   - Instruction: produce your opening position independently, without seeing other characters' views
   
   Collect all five positions before proceeding.
   
   STAGE 3 — Cross-examination (sequential, each agent sees all positions)
   Invoke each character agent again, this time with:
   - The original topic
   - All five opening positions
   - Instruction: respond to the positions you most agree with and most disagree with; sharpen or revise your own view
   
   STAGE 4 — Synthesis (you, the orchestrator)
   Identify: points of genuine agreement, irresolvable tensions, what each character's position implies for action, and what the committee collectively recommends — with explicit dissents noted.
   
   STAGE 5 — Confidence and provenance
   State the committee's overall confidence (Low/Medium/High) and explain what would need to change to increase it. List the key assumptions the recommendation depends on.
   ```

3. **Include a note about transparency**: The committee's value is traceability. Every claim in the synthesis should be traceable to a specific character's position. Do not smooth over disagreements — name them.

4. **Include a note about re-running**: Running this command multiple times on the same topic and comparing outputs is a feature, not redundancy. Variance reveals the topology of the decision landscape.

5. **Adapt for Cowork users**: Write for someone who has just installed this plugin, not a developer. Avoid jargon. The input can be as simple as: `/cyberneutics:committee Should we expand into the European market?`

### Step 5: `commands/scenarios.md`

The fan half of the fan/funnel duality. Translate the `/scenarios` SKILL.md into a command file for Cowork users.

Key adaptations from the Claude Code version:
- The user provides a situation; the command generates N distinct futures (default: 4), each from a different scenario character's lens
- Each scenario should be a short narrative (2-3 paragraphs), not a bullet list
- End with a brief assessment: which scenarios are most plausible, which are most consequential, which are easiest to probe for early signals
- Write for a decision-maker, not a developer

### Step 6: `commands/probe.md`

The decision landscape mapper. Translate the `/probe` SKILL.md into a command file.

**Important adaptation for Cowork**: The full probe runs fan→funnel multiple times and produces a variance report. For Cowork v1, specify a simplified single-pass version that still produces the essential output:

```
PROBE (simplified v1):
1. Run /cyberneutics:scenarios on the situation (or accept pre-run scenarios as input)
2. For each scenario, invoke /cyberneutics:committee with scenario_context set to that scenario
3. Collect all committee resolutions
4. Identify: which resolution appears across multiple scenarios (eigenform), which only appears in extreme scenarios (residue), where small assumption changes flip the outcome (critical boundary)
5. Output: a landscape map as a short prose summary + a table of (scenario → resolution → confidence)
```

Note at the end: "For rigorous landscape mapping on high-stakes decisions, run this command 3–5 times and compare the outputs. Stable resolutions across runs are robust; unstable ones signal a decision near a critical boundary."

### Step 7: `commands/review.md`

Translate the `/review` SKILL.md. This command evaluates a completed committee deliberation transcript against five rubrics and produces a scored evaluation with specific improvement suggestions.

Adaptation: In Cowork, the user will paste or reference a deliberation output file. The command should:
- Accept either pasted text or a file path as input
- Apply the five rubrics from the existing SKILL.md verbatim
- Output a scored table plus one concrete suggestion per rubric for how this specific deliberation could have been stronger

### Step 8: `commands/handoff.md`

Adapt the `/handoff` SKILL.md for Cowork context.

The Cowork version should:
- Capture what was worked on this session
- Save a summary to a file in the current working directory named `handoff-YYYY-MM-DD.md`
- Include: topic, techniques used, key outputs produced, open questions, recommended next steps
- Be explicitly lighter than the Claude Code version — Cowork sessions are more task-focused than exploratory

### Step 9: `commands/string-diagram.md`

Translate the `/string-diagram` SKILL.md. This is the most technical command — calibrate the tone for a non-developer who nonetheless needs to reason carefully about pipelines and workflows.

The command should:
- Accept a description of a workflow or pipeline in plain language
- Produce a resource equation representation using palgebra notation (from `palgebra/reference.md`)
- Annotate fan/funnel nodes where relevant
- Explain what the notation reveals that the prose description obscured

Include a brief syntax cheat-sheet at the top of the command file so the user can read the output without needing to open the palgebra docs.

### Step 10: `skills/` — four background skills

Skills fire **automatically** when Claude detects relevance. Each SKILL.md should open with a `## When this skill applies` section that makes the trigger conditions explicit. Keep skills focused — they load into every relevant interaction, so brevity matters.

**`skills/orientation/SKILL.md`**
Distilled from `CLAUDE.md`. Covers:
- When to use cyberneutics vs. when not to (simple questions, data lookup, tasks with clear answers — don't run a committee on those)
- The five core ideas in condensed form
- The command index: which command for which kind of problem
- Common pitfalls (collapsing to single answers prematurely, skipping provenance)
- Fires when: the user seems to be facing a complex decision, asking "what should we do about X," or expressing genuine uncertainty

**`skills/fan-funnel/SKILL.md`**
The scenario generation / committee deliberation duality:
- Fan = one-to-many = `/scenarios` = exploring possible futures before committing
- Funnel = many-to-one = `/committee` = converging multiple perspectives to a justified commitment
- Composed = `/probe` = deliberated choice across multiple futures
- When to use each; how they sequence
- Fires when: the user is exploring futures, weighing options, or asking about uncertainty

**`skills/palgebra/SKILL.md`**
Minimal operational palgebra — just enough to read and write resource equations:
- Decorated text concept (text + metadata)
- Enrichment vs. transformation
- Basic notation: `→`, `⊗`, fan/funnel symbols
- Fires when: the user is describing a workflow, pipeline, or multi-step process

**`skills/committee/SKILL.md`**
The five characters and what they contribute:
- Verbatim character descriptions from `agent/roster.md`
- What each character is for, what they're likely to miss
- The principle that disagreement is the signal, not a problem to resolve
- Fires when: `/cyberneutics:committee` is invoked, or when the user asks for multiple perspectives

### Step 11: `README.md`

A user-facing readme. Not developer documentation. Write for a decision-maker who has just installed the plugin.

Structure:
1. **What this is** (two sentences)
2. **The three things you can do** — scenarios, committee, probe — with a one-line description of each
3. **Quick start** — a worked example: "You're facing X. Type: `/cyberneutics:scenarios [your situation]`. Here's what you'll get. Then type: `/cyberneutics:committee [your decision]`. Here's what you'll get."
4. **When to use this** — complex decisions, genuine uncertainty, situations where you need to be able to explain your reasoning afterward
5. **When not to use this** — simple lookups, questions with clear right answers, time pressure that doesn't allow for deliberation
6. **Command reference** — one line per command

---

## Key judgments to make

**Tone**: The existing SKILL.md files are written for Claude Code sessions with a methodology-aware user. The plugin versions should assume the user is a thoughtful decision-maker who knows their domain but has never heard of cyberneutics. Explain what you're doing, not just how.

**Committee agents vs. simulation**: The agent files are the critical innovation. They must be written so that each character runs independently, with a genuinely distinct worldview, not as a polite variation on the same answer. If the five agents produce similar outputs, the system has failed. Build in explicit resistance to premature convergence.

**What not to include**: Do not bundle the essays, the `agent/deliberations/` archive, or the `palgebra/duality-and-composition.md` deep theory into the plugin. The plugin is an interface to the methodology, not the methodology's full documentation. Users who want depth can explore the repo.

**Palgebra in commands**: String-diagram aside, the other commands should not require the user to understand palgebra. Internally, the commands can use resource equation logic to structure their output — but this should be invisible to the user unless they ask for it.

---

## When complete, report

1. All files created with their sizes
2. Any material from the existing repo you chose not to include and why
3. Specific judgment calls made in writing the committee agent files — what made each character distinctively themselves
4. Any structural decisions about the probe command's simplification
5. Recommended first test: which command to run first in Cowork and on what kind of input, to validate the plugin is working as intended
