# Deep Research Prompt: Coding Agent Subagent Capabilities

**Context**: The Cyberneutics project uses adversarial committee deliberation — multiple characters with different cognitive styles debating a topic — as a decision-support mechanism. Currently this runs as roleplay within a single LLM context window. We want to understand whether commercial coding agents can host genuinely independent subagents, and whether any support routing different subagents to different models.

**Date of research**: March 2026. Capabilities are changing rapidly; focus on what is available now or announced for near-term release, not speculative roadmaps.

---

## Primary Questions

### 1. Multi-model subagent support

Do any of the following coding agents or agent frameworks currently support spawning subagents that run on a *different* model than the parent?

- **Claude Code** (Anthropic) — particularly the "Agent Teams" feature
- **Codex** (OpenAI) — desktop app, CLI, and IDE extensions
- **Cursor** — native AI features and any agent/subagent capabilities
- **Windsurf / Codeium**
- **Aider**
- **Continue.dev**
- **Amazon Q Developer**
- **Google Jules / Gemini Code Assist**
- **Any other significant entrants since January 2026**

For each: can a parent agent spawn a child agent that uses a different LLM provider or model? If not natively, is there a documented workaround (e.g., MCP tool that calls a different model's API)?

### 2. Peer-to-peer vs. hub-and-spoke

For each agent that supports subagents or multi-agent workflows:

- Can subagents communicate directly with each other (peer-to-peer), or must all communication flow through a central orchestrator (hub-and-spoke)?
- If peer-to-peer: what is the communication mechanism? (Shared filesystem, message passing, tool calls, something else?)
- If hub-and-spoke: does the orchestrator pass full context or summaries between subagents?

### 3. Concurrent execution

For each agent supporting subagents:

- Can multiple subagents run concurrently (parallel execution), or must they run sequentially?
- If concurrent: are they in separate processes/threads with independent context windows, or do they share state?
- What are the practical limits? (Maximum number of concurrent subagents, token budget per subagent, timeout constraints?)

### 4. Claude Code Agent Teams specifics

This is the most immediately relevant platform. Research in detail:

- Current status of Agent Teams (still experimental? generally available?)
- Can Agent Teams members have different system prompts / personas?
- Can they use different models? (Even different Claude models — Haiku vs Sonnet vs Opus?)
- What is the communication mechanism? (The `sendMessage` tool — is it point-to-point or broadcast? Can agents selectively address each other?)
- What are the practical limits for a 5-agent deliberation with multiple rounds? (Context window consumption, cost, latency, reliability?)
- Is there documentation, blog posts, or community experience reports on using Agent Teams for deliberation or debate rather than coding tasks?

### 5. LiteLLM and Ollama as MCP servers

- Does LiteLLM currently offer an MCP server interface, or is there a community MCP wrapper?
- Does Ollama offer an MCP server interface?
- If not: how hard would it be to wrap either one? (Is there a template or pattern for wrapping an OpenAI-compatible API as an MCP tool?)
- Are there any existing MCP servers that provide multi-model LLM access as tools?

### 6. Agent frameworks with multi-model support

Beyond coding agents, are there agent frameworks or orchestration platforms that explicitly support multi-model agent ensembles?

- **CrewAI** — can different crew members use different models?
- **AutoGen** (Microsoft) — multi-model support?
- **LangGraph** — can nodes in the graph route to different models?
- **Semantic Kernel** — multi-model agent support?
- **Any Clojure-based agent frameworks** — particularly anything built on or compatible with LiteLLM or Ollama?

For each: what is the setup complexity? Could a non-developer power user configure and run a multi-model deliberation?

### 7. The accessibility question

For a power user (comfortable with API keys and configuration, but not a developer) who wants to run multi-model committee deliberations:

- What is the simplest current path? (Fewest dependencies, least code, most guided setup)
- What is the most capable current path? (Best control, best observability, best cost tracking)
- Is there anything that provides both simplicity and capability?

---

## Output Format

For each question, provide:

1. **Current state** (what exists today, with version numbers and dates where possible)
2. **Evidence quality** (official documentation, community reports, your direct testing, or inference from architecture)
3. **Trajectory** (is this capability being actively developed? any announcements or signals?)
4. **Gaps** (what doesn't exist that would need to for our use case?)

Organize findings as a structured report suitable for inclusion in a research repository. Distinguish clearly between confirmed facts, well-sourced reports, and your inferences or speculations.

---

## Why This Matters

We have a taxonomy of implementation tiers for committee deliberation:

| | Single model | Multi-model |
|---|---|---|
| **Roleplay** (one context) | Current state (baseline) | N/A |
| **Independent agents** | Tier 1: built-in subagents | Tier 2: built-in multi-model subagents / Tier 3: external orchestration via LiteLLM |

Tier 1 is accessible to anyone with the product. Tier 3 is available to power users with LiteLLM. Tier 2 would be the convergence point but may not exist yet. This research determines which tiers are currently viable and what the path to Tier 2 looks like.
