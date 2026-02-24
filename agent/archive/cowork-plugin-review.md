# Cowork Plugin Review — 2026-02-24

## Summary

The `cowork-plugin/` directory packages cyberneutics as a Claude Code/Cowork plugin. The content quality is excellent — the commands, skills, and agent definitions are well-written, well-scoped, and genuinely useful. The structural issues below are mostly about conformance to the official plugin specification, which affects whether the plugin will actually work as intended when loaded.

**Sources**: [Anthropic plugin creation guide](https://docs.anthropic.com/en/docs/claude-code/plugins), [Anthropic plugins reference](https://docs.anthropic.com/en/docs/claude-code/plugins-reference)

---

## Issues

### HIGH — Agents are character definitions, not Claude sub-agents

**What's wrong**: The five files in `agents/` (maya.md, frankie.md, joe.md, vic.md, tammy.md) are character personality definitions for the cyberneutics committee. In the Claude plugin system, `agents/` files define **sub-agents** — autonomous Claude instances that Claude can invoke (via `/agents` or automatically) to perform tasks. Each agent file's frontmatter `description` field tells Claude *when to invoke* that sub-agent.

The current descriptions (e.g. "Invoke for rigorous systems analysis and long-term structural critique") will cause Claude to invoke these as separate sub-agents in inappropriate contexts. A user asking about incentive structures might trigger Maya as a standalone sub-agent, outside any committee context. This is not the intended use.

**Why it matters**: The committee pattern requires all five characters to deliberate *together* within a structured pipeline (charter → independent positions → cross-examination → synthesis). Exposing them as individual sub-agents breaks this structure. Users would get single-character responses instead of the adversarial deliberation that produces the value.

**Options**:

1. **Move character definitions to skills** — Put the five character files under a skill like `skills/committee/characters/` as reference material. The committee SKILL.md already describes the characters; the full definitions would be supporting material Claude reads when executing the committee command. This is the cleanest structural fix.

2. **Rename and reframe as a single orchestrator agent** — Create one agent (`agents/committee-orchestrator.md`) that runs the full pipeline, with the five characters embedded or referenced as supporting material. Description: "Use for adversarial committee deliberation on complex decisions." This prevents individual character invocation while still using the agents directory.

3. **Keep as agents but fix the descriptions** — Adjust descriptions to constrain invocation: "Only invoke as part of a cyberneutics:committee deliberation, never independently." This is the smallest change but fights the grain of the plugin system (agents are *meant* to be independently invocable).

> [!IMPORTANT]
> Recommendation: Option 1. The characters are reference material for the committee skill/command, not independent agents. Moving them to `skills/committee/` makes the plugin's architecture match its intent.

---

### MEDIUM — plugin.json author field should be an object

**Current**:
```json
"author": "mg"
```

**Expected** (per the plugin manifest schema):
```json
"author": {
  "name": "mg"
}
```

The spec defines `author` as an object with `name`, optional `email`, and optional `url` fields. A bare string may fail schema validation.

---

### MEDIUM — Commands don't reference skills or agents

The command files (e.g. `committee.md`) describe the deliberation process in detail but don't tell Claude *how* to actually execute it — specifically, they don't reference the agent characters or skill files. The `/cyberneutics:committee` command describes a five-stage multi-agent deliberation but doesn't say "use the Maya, Frankie, Joe, Vic, and Tammy agents" or "refer to the committee skill for character details."

Without these references, Claude has to hope the skills fire contextually. Making the references explicit (e.g. "Invoke the five committee agents defined in `agents/` for Stage 2") would make execution more reliable.

> [!NOTE]
> This is less critical if the characters are moved to `skills/committee/` (see issue above), since the committee skill would automatically be read alongside its supporting files. But the commands should still reference the skills they depend on.

---

### LOW — Empty .mcp.json is unnecessary

The `.mcp.json` file contains `{}`. Since there are no MCP servers to configure, this file can be removed entirely. The plugin system only looks for it if present; absence is fine and cleaner.

---

### LOW — Missing recommended files

The plugin reference recommends (but doesn't require):

- **`settings.json`** — Could set `"agent": "committee-orchestrator"` as the default agent, so the plugin has a clear entry point.
- **`LICENSE`** — The main repo specifies CC BY-SA 4.0 for essays and MIT for code. The plugin should include a LICENSE file stating its terms.
- **`CHANGELOG.md`** — Not needed yet at v0.1.0, but worth adding before distribution.

---

### LOW — No hooks for session integration

The plugin has no `hooks/hooks.json`. The cyberneutics methodology would benefit from hooks, for example:

- **`SessionStart`** — Auto-suggest cyberneutics commands when a session begins, or remind the user of the `/cyberneutics:handoff` command.
- **`Stop`** — Prompt to run `/cyberneutics:handoff` before ending a session, ensuring continuity.

These are nice-to-haves, not structural problems.

---

## Content Quality Notes

### Strengths

- **Commands are excellent**: Each command file is well-structured with clear "what you'll get", "how to use it", and output format sections. The `review.md` rubrics are particularly strong — specific, graduated, with red flags.
- **Skills provide genuine background knowledge**: The fan/funnel skill and orientation skill give Claude the conceptual framework to reason about which command to suggest. The palgebra skill is appropriately scoped — "just enough" for string diagrams.
- **Character definitions are well-calibrated**: Each agent has propensity, characteristic objections, blind spots, calibration examples (bad vs. good), and inter-agent dynamics. This is high-quality prompt engineering.
- **README is user-focused**: The plugin README leads with "the three things you can do" — a good choice for a tool that knowledge workers would evaluate quickly.

### Minor Observations

- The `probe.md` command describes running `/cyberneutics:committee` for each of 4 scenarios — that's 4 full five-agent deliberations plus scenario generation. This is a very large context window operation. The command file should note this cost explicitly, and possibly suggest a lighter-weight version.
- The `string-diagram.md` command is noticeably different from the others: it's a formalization tool, not a decision-making tool. Consider whether it belongs in the plugin or whether it's better as a standalone skill in the main repo (it doesn't use the committee or scenarios).
- Terminology inconsistency: the README calls the characters "agents" (cyberneutics terminology), while in Claude plugin architecture "agents" means something different (sub-agents). The README should clarify this distinction or use "committee characters" / "committee members" consistently.

---

## Assessment

| Aspect | Rating | Notes |
|--------|--------|-------|
| Content quality | **Strong** | Commands, skills, and characters are well-written and well-scoped |
| Plugin structure | **Needs work** | Agents directory semantic mismatch is a real functional issue |
| Completeness | **Adequate** | Missing some recommended files but nothing blocking |
| Usability | **Good** | README is clear; command usage examples are practical |
| Testability | **Untested** | No indication of having been loaded via `--plugin-dir` |

**Overall**: The conceptual work is strong and the content is ready. The main structural issue (agents as characters vs. sub-agents) needs resolution before the plugin will behave as intended when loaded. The fix is straightforward.
