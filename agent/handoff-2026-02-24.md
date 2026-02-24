# Session Handoff: 2026-02-24 (Cowork plugin build)

---

## Session Summary

**Duration**: Single session. Focus: build the cyberneutics Cowork plugin from the prompt in `agent/prompts/create-cowork-plugin.md`.

**Original intent**: mg provided a detailed build prompt specifying a complete Cowork plugin — directory structure, 18 files, step-by-step instructions for each. The task was to read all 10 source files (CLAUDE.md, roster.md, 6 SKILL.md files, palgebra/reference.md, essays/README.md), then create the plugin package.

**Actual outcome**: All 18 files created in `cowork-plugin/` as specified. No existing repo files modified. Completion report delivered covering files created, material excluded with rationale, agent writing judgment calls, probe simplification decisions, and recommended first test.

**Key deliverables**:
- `cowork-plugin/` directory with full plugin structure
- 5 independent agent files (Maya, Frankie, Joe, Vic, Tammy) with distinct system prompts
- 6 command files (committee, scenarios, probe, review, handoff, string-diagram)
- 4 background skill files (orientation, fan-funnel, palgebra, committee)
- README.md for end-users (decision-makers, not developers)
- plugin.json and .mcp.json

---

## Mistakes and Lessons

- **No mistakes encountered** — the build prompt was extraordinarily detailed and well-structured. Each step had clear inputs, outputs, and judgment criteria. The 10-file reading list ensured deep understanding before writing.
- **Lesson for successor**: The build prompt (`agent/prompts/create-cowork-plugin.md`) is itself a model for how to specify a complex multi-file creation task. If mg creates similar prompts for future plugin builds, following the same structure (read list → directory structure → step-by-step with judgment notes) will work well.

---

## Dead Ends Explored

None — the prompt was prescriptive enough that no exploratory paths were needed.

---

## Current State

### Completed this session

| Item | Location |
|------|----------|
| Plugin manifest | `cowork-plugin/.claude-plugin/plugin.json` |
| MCP config | `cowork-plugin/.mcp.json` |
| Maya agent | `cowork-plugin/agents/maya.md` (3.1 KB) |
| Frankie agent | `cowork-plugin/agents/frankie.md` (3.5 KB) |
| Joe agent | `cowork-plugin/agents/joe.md` (3.5 KB) |
| Vic agent | `cowork-plugin/agents/vic.md` (3.6 KB) |
| Tammy agent | `cowork-plugin/agents/tammy.md` (3.7 KB) |
| Committee command | `cowork-plugin/commands/committee.md` (5.3 KB) |
| Scenarios command | `cowork-plugin/commands/scenarios.md` (4.2 KB) |
| Probe command | `cowork-plugin/commands/probe.md` (4.1 KB) |
| Review command | `cowork-plugin/commands/review.md` (4.7 KB) |
| Handoff command | `cowork-plugin/commands/handoff.md` (1.7 KB) |
| String-diagram command | `cowork-plugin/commands/string-diagram.md` (4.2 KB) |
| Orientation skill | `cowork-plugin/skills/orientation/SKILL.md` (3.4 KB) |
| Fan-funnel skill | `cowork-plugin/skills/fan-funnel/SKILL.md` (2.9 KB) |
| Palgebra skill | `cowork-plugin/skills/palgebra/SKILL.md` (2.4 KB) |
| Committee skill | `cowork-plugin/skills/committee/SKILL.md` (3.6 KB) |
| README | `cowork-plugin/README.md` (3.5 KB) |

### Not included (by design)

- Essays, palgebra deep theory, deliberation archives, artifact templates — per the prompt's "What not to include" section
- Scenario roster as separate agent files — scenario characters (Continuity/Disruption/Adaptation/Constraint) are narrative lenses described in the scenarios command, not independent agents needing context isolation
- Remediation workflow (evaluate→remediate→re-evaluate file chain) — simplified to "rerun with feedback" for Cowork users
- Robert's Rules framing — same mechanics as the Claude Code version but with "stages" language instead of parliamentary jargon

### From prior handoff (unchanged)

- Pask mesh fitting rename still pending
- Ablation-study, comparative evaluation, CI string-diagram job still pending mg's decisions
- Rubric score persistence question still open

---

## Immediate Next Steps

1. **Commit the cowork-plugin** — all 18 new files plus the build prompt, handoff archive
2. **Test the plugin in Cowork** — mg should install and run `/cyberneutics:committee` on a real decision to validate agent distinctiveness
3. **Iterate on agent prompts if needed** — if the five agents converge too easily or are excessively polite, their system prompts need sharpening (especially the cross-agent challenge instructions)
4. **Consider adding scenario-roster agent files** — v1 describes scenario characters inline in the scenarios command; v2 could give them independent agent files if Cowork supports it

---

## Working with mg: Session-Specific Insights

- **Detailed build prompts work**: mg provided an extremely structured build specification with reading requirements, directory structure, step-by-step instructions, judgment guidance, and a reporting template. This eliminated ambiguity and produced clean execution. mg thinks in terms of complete specifications, not iterative refinement.
- **"Read first" discipline**: mg's prompt required reading 10 source files before writing anything. This isn't ceremony — the character calibration examples, interaction dynamics, and voice notes in roster.md directly shaped the agent files. Skipping the reading would have produced generic agents.
- **mg asked for handoff + commit message together**: mg chains related deliverables into single requests rather than sequential asks. Same pattern as the previous session.

---

## Open Questions and Decisions Needed

- **Cowork plugin testing**: Has mg tested this in an actual Cowork environment? The plugin structure follows the spec in the build prompt, but runtime behavior depends on how Cowork processes agent files, command files, and skill files.
- **Scenario character independence**: Should the four scenario lenses (Continuity, Disruption, Adaptation, Constraint) get their own agent files in a future version? Currently they're described inline in `commands/scenarios.md`.
- **Prior handoff questions still open**: pask-mesh-fitting rename, rubric score persistence, CI workflow, comparative evaluation, multi-model-committee-reference.

---

## Watch-Outs for Successor

- **Agent distinctiveness is the quality criterion**: If the five committee agents produce similar outputs in testing, the plugin has failed. The agent files include explicit cross-agent challenge instructions to prevent convergence — but this needs validation in Cowork's actual execution model.
- **Probe simplification**: The Cowork probe is a single-pass version (scenarios → committee per scenario → compare), not the N-independent-runs version from the Claude Code skill. The prompt specified this simplification for v1. If users want the full probe, the command file already includes the "run 3-5 times" guidance.
- **Build prompt still in agent/prompts/**: `agent/prompts/create-cowork-plugin.md` is the spec that generated the plugin. It's not part of the plugin itself — it's build documentation.

---

## Session Metadata

**Agent**: Single session (Cowork plugin build)
**Date**: 2026-02-24
**Goal**: Build complete Cowork plugin from detailed build prompt
**Status**: All 18 files created. Commit pending.
**Previous handoff**: agent/archive/handoff-2026-02-24-editorial.md (editorial remediation session, same day)
**Continuation priority**: Commit → test in Cowork → iterate on agent prompts if needed
