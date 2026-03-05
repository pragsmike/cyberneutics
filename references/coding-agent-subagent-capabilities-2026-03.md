# Coding Agent Subagent Capabilities: Multi-Model Support & Architecture Analysis

*Research date: March 2026 | For the Cyberneutics adversarial committee deliberation project*

## Executive Summary

The landscape of coding agent multi-model subagent support has shifted dramatically since January 2026. Claude Code Agent Teams (released February 5, 2026 with Opus 4.6) is the most mature native implementation, supporting per-teammate model selection within the Claude family, peer-to-peer communication, and concurrent execution — but not cross-provider routing. Cursor, OpenCode, and the agent frameworks (CrewAI, AutoGen, LangGraph) all support genuine multi-provider model assignment per agent. For Cyberneutics' adversarial committee deliberation, **Tier 2 (built-in multi-model subagents) partially exists**: Claude Code Agent Teams provides the deliberation architecture natively, while frameworks like CrewAI provide full cross-provider multi-model support with moderate setup complexity. **Tier 3 (external orchestration via LiteLLM) is fully viable today** — LiteLLM operates as an MCP Gateway and supports 100+ models behind a unified API.[^1][^2][^3][^4]

## 1. Multi-Model Subagent Support by Platform

### Claude Code Agent Teams

**Current state:** Experimental, released February 5, 2026 with Opus 4.6. Enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Agent Teams supports specifying different Claude models per teammate — the recommended configuration is Opus 4.6 for the team lead, Sonnet 4.5 for teammates, and Haiku 4.5 for sub-subagents, creating a three-tier cost hierarchy. This is explicitly documented in prompt templates that include directives like "Use Sonnet model" per teammate.[^3][^4]

**Cross-provider limitation:** All teammates must use Claude/Anthropic models. There is no mechanism to route a teammate to GPT-5, Gemini, or an open-source model. This is a fundamental architectural constraint — teammates are Claude Code instances, not generic LLM endpoints.[^4][^5]

**Workaround:** A teammate could invoke an MCP tool that calls a different model's API. Since teammates inherit MCP server configuration, any MCP tool available to the lead is available to teammates. A LiteLLM MCP server could theoretically provide cross-provider access as a tool call, though this would be a tool invocation, not a model swap for the agent's reasoning itself.[^3]

**Evidence quality:** Official documentation, detailed community guides, and multiple independent experience reports.[^6][^5][^4][^3]

### OpenAI Codex

**Current state:** Codex CLI supports multi-agent configurations with configurable roles in `config.toml`, where each role can have different model configurations. Sub-agents report to the parent in a hub-and-spoke pattern, with parallel execution in isolated contexts. The ARTEMIS security framework demonstrated forking Codex's open-source scaffold to spawn sub-agents with `spawn_codex`, `terminate_instance`, and `send_followup` tools.[^7][^8]

**Multi-model:** Different roles can override model settings, but this remains within the OpenAI ecosystem. Cross-provider routing is not natively supported.

**Evidence quality:** Academic papers using forked scaffolds; limited official documentation on multi-agent features.

### Cursor

**Current state:** Cursor 2.4 (January 2026) introduced subagents that run in parallel with their own context, custom prompts, tool access, and model specifications in agent spec frontmatter. Cursor supports model selection per agent from its full model roster, which includes Claude Sonnet 4.5, GPT-5, Gemini 2.5 Pro, and proprietary models. This makes Cursor one of the few coding IDEs with **genuine cross-provider multi-model agent support**.[^9]

**Caveats:** Community reports indicate the model configuration in agent specs is sometimes ignored, defaulting to the session's primary model. Cursor's multi-agent mode supports up to 8 agents with a best-of-N approach for comparing outputs across models.[^9]

**Evidence quality:** Product documentation and community reports; some bug reports about model spec adherence.

### Windsurf / Codeium

**Current state:** Windsurf's Cascade agentic feature is the core product capability. Wave 13 introduced parallel multi-agent sessions with up to five concurrent Cascade instances. Model selection between SWE-1.5, Claude, and GPT models is available at the session level. However, native sub-agent spawning or per-agent model routing is not documented. A workaround is running separate Cascade sessions with a shared file for inter-agent communication.[^10][^11][^12]

**Evidence quality:** Product reviews and community discussion; no official multi-agent API documentation.

### Aider

**Current state:** Aider's "architect mode" is the closest analogue to multi-model support — it uses two models in sequence: one for planning/reasoning and another for code editing. The canonical example pairs an o1-class reasoning model as the architect with GPT-4o or Sonnet as the editor. This is multi-model by design, but it is two-model sequential, not multi-agent parallel. Aider has no sub-agent spawning mechanism; a community request for multi-agent flow (issue #1839) was closed without implementation.[^13][^14]

**Evidence quality:** Official documentation for architect mode; community discussion confirms no multi-agent plans.

### Continue.dev

**Current state:** Continue supports multiple model providers and different models for different tasks (chat, autocomplete, embedding). The CLI supports parallel sessions via shell-level parallelism. Agent mode uses tool calling with MCP server integration. However, true in-process multi-agent orchestration is acknowledged as a future release item. Continue is model-agnostic and works with OpenAI, Anthropic, Ollama, and self-hosted providers.[^15][^16][^17][^18]

**Evidence quality:** Official documentation and blog posts; community reports of limited agentic capability with local models.[^19]

### Amazon Q Developer

**Current state:** Q Developer CLI supports custom agents with MCP tools, custom prompts, and context. Agents can be switched via `q chat --agent <name>` for different development contexts (e.g., front-end vs. back-end). However, there is no native multi-agent orchestration. A GitHub discussion (#1448) requesting A2A protocol support for collaborative multi-agent workflows remains open with no official response.[^20][^21]

**Evidence quality:** Official blog posts; community feature requests confirm the capability gap.

### Google Jules

**Current state:** Jules reached GA in August 2025, with CLI and API added October 2025. Powered exclusively by Gemini 2.5 Pro, Jules operates asynchronously in cloud VMs with parallel task execution. It is a single-agent, single-model tool with no sub-agent or multi-model capability. Jules' design philosophy emphasizes autonomous end-to-end task completion rather than multi-agent collaboration.[^22][^23][^24][^25]

**Evidence quality:** Official Google announcements and documentation.

### OpenCode

**Current state:** OpenCode is an open-source, provider-agnostic coding agent. A design proposal (GitHub issue #12711, February 8, 2026) explicitly targets Agent Teams with flat team structure, named messaging, and **multi-model support per teammate** — e.g., Gemini for research, Claude for implementation. Community members have already configured multi-provider setups with Claude Opus for coding, Perplexity for research, and GPT for debugging. The feature is behind an experimental flag.[^26][^27]

**Evidence quality:** Open design documents and community implementations; feature still in development.

### Platform Comparison

| Platform | Sub-agents | Multi-model (same provider) | Cross-provider multi-model | Peer-to-peer comms | Status |
|---|---|---|---|---|---|
| Claude Code Agent Teams | ✅ | ✅ (Opus/Sonnet/Haiku) | ❌ (Claude only) | ✅ (mailbox) | Experimental |
| OpenAI Codex | ✅ | ✅ (role config) | ❌ (OpenAI only) | ❌ (hub-spoke) | Experimental |
| Cursor | ✅ | ✅ | ✅ (Claude/GPT/Gemini) | ❌ (hub-spoke) | Released |
| Windsurf | ❌ (workaround) | Session-level | Session-level | ❌ | N/A |
| Aider | ❌ (architect mode) | ✅ (2-model sequential) | ✅ (any provider) | N/A | Stable |
| Continue.dev | ❌ (parallel sessions) | ✅ (per-task) | ✅ (any provider) | ❌ | CLI only |
| Amazon Q Developer | ❌ | ❌ | ❌ | ❌ | N/A |
| Google Jules | ❌ | ❌ | ❌ | ❌ | GA |
| OpenCode | ✅ (in design) | ✅ (planned) | ✅ (planned) | ✅ (planned) | Experimental |

## 2. Peer-to-Peer vs. Hub-and-Spoke

### Claude Code Agent Teams — Hybrid (Mesh)

Agent Teams implements a **hybrid architecture**. The team lead creates the team and spawns teammates (hub-and-spoke for initialization), but once spawned, **any teammate can message any other teammate directly** via the `SendMessage` tool, or broadcast to the entire team. Communication flows through a file-based mailbox system at `~/.claude/teams/{team-name}/inboxes/`. The shared task list at `~/.claude/tasks/{team-name}/` provides additional coordination with task statuses, ownership, and dependency relationships.[^4][^3]

The lead does not mediate ongoing communication — this is genuine peer-to-peer messaging. However, the lead remains the only session visible to the human operator and is responsible for final synthesis. This architecture directly supports adversarial deliberation patterns: teammates can challenge each other's findings, share intermediate results, and converge through direct debate.[^3][^4]

### OpenAI Codex — Hub-and-Spoke

Sub-agents report to the parent agent. There is no documented mechanism for sibling agents to communicate directly. The parent manages all coordination and relays information between sub-agents by spawning new sub-agents or updating its own context.[^8]

### Cursor — Hub-and-Spoke

Cursor's subagents run in parallel with independent context windows but report results back to the orchestrating session. No peer-to-peer communication is documented.[^9]

### Agent Frameworks

CrewAI supports both sequential and hierarchical processes, with agents able to delegate tasks to each other. AutoGen's `GroupChat` manager coordinates multi-agent conversations with customizable speaker selection, enabling round-robin or dynamic turn-taking. LangGraph uses graph-based state management where nodes pass state through edges, enabling complex routing patterns including conditional branching and cycles. Semantic Kernel supports concurrent, sequential, handoff, group chat, and Magentic orchestration patterns.[^28][^29][^30][^31][^32][^33]

## 3. Concurrent Execution

### Claude Code Agent Teams

Teammates run as **separate Claude Code processes** with independent context windows. They execute concurrently and can be monitored in split-pane mode (tmux/iTerm2). Practical limits: 2-16 teammates per team, with 2-3 focused teammates recommended for optimal results; beyond 4-5 agents, coordination overhead and file conflict risk grow faster than productivity gains. Token budget per teammate is independent (each has its own context window). Teams use approximately **3-7x the tokens** of a single session, with 7x being the upper bound for plan-mode usage. Anthropic demonstrated 16-agent teams across ~2,000 sessions for building a C compiler, but this was sequential sessions rather than 16 simultaneous agents.[^4][^3]

### Other Platforms

| Platform | Concurrent? | Isolation | Practical limits |
|---|---|---|---|
| Codex | Yes (parallel) | Separate processes | `max_threads` configurable[^7] |
| Cursor | Yes (up to 8) | Independent context | 8 agents max[^9] |
| CrewAI | Yes (async) | Per-agent context | Memory/API rate limits |
| AutoGen | Yes (async) | Per-agent context | Rate limits; semaphore-bounded[^34] |
| LangGraph | Node-level | Shared state graph | Graph complexity limits |

## 4. Claude Code Agent Teams — Detailed Analysis

### Status and Maturity

Agent Teams is **experimental** — it requires an explicit opt-in flag and is disabled by default. It shipped with the Opus 4.6 release on February 5, 2026. There is no timeline for GA. The feature is actively used by early adopters and has been validated at scale by Anthropic's engineering team (C compiler project).[^5][^35][^6][^3]

### System Prompts and Personas

Each teammate receives: (1) the project's `CLAUDE.md` context, (2) MCP server configurations, (3) skills, and (4) a **spawn prompt from the lead** that defines the teammate's role, scope, and instructions. The lead's conversation history does **not** carry over to teammates. This means each teammate can have a distinct persona, expertise area, and set of constraints defined in the spawn prompt — directly supporting the Cyberneutics character-based deliberation model.[^3][^4]

### Model Selection

Different Claude models can be specified per teammate in the spawn prompt (e.g., "Use Sonnet model"). The recommended three-tier hierarchy is: Opus 4.6 (lead, $5/$25 per MTok), Sonnet 4.5 (teammates, $3/$15 per MTok), Haiku 4.5 (sub-subagents, $1/$5 per MTok). **Cross-provider models are not supported** — all participants must be Claude models.[^3]

### Communication Mechanism

The `SendMessage` tool supports both **point-to-point** (direct message to a named teammate) and **broadcast** (message to all teammates). Messages are stored in the file-based mailbox system. Broadcasts are expensive because they inject the message into every teammate's context window. Teammates can selectively address each other by name. The `TaskCreate`, `TaskUpdate`, and `TaskList` tools provide structured coordination via the shared task list with dependency tracking.[^4][^3]

### 5-Agent Deliberation Feasibility

For a 5-agent deliberation with multiple rounds:

- **Context window consumption:** Each teammate has an independent context window. Multi-round debate messages accumulate in each participant's inbox. With 5 agents doing 3 rounds of debate, approximately 15 broadcast messages would be injected (5 agents × 3 rounds), each appearing in 4 other agents' contexts. At ~2,000 tokens per message, this is ~120K tokens of communication overhead alone.[^3]
- **Cost estimate:** Based on verified pricing — Opus lead + 4 Sonnet teammates, assuming ~500K total tokens per teammate including communication: approximately $30-50 per full deliberation session. This is expensive but feasible for high-value decisions.[^3]
- **Latency:** Teammates spawn in 20-30 seconds and begin producing results within the first minute. A multi-round deliberation with 3 rounds would likely take 10-20 minutes.[^4]
- **Reliability:** Current limitations include task status lag (teammates sometimes fail to mark tasks completed), limited session resumption (cannot resume interrupted teammates), and occasional file conflicts.[^5][^3]

### Deliberation Use Case Evidence

Agent Teams documentation explicitly lists **"Debugging with competing hypotheses"** and **"Debate and consensus"** as strong use cases. The competing hypothesis template instructs investigators to "Share findings via messages as you go. If you find strong evidence for your hypothesis, broadcast to the team immediately. If you can rule out your hypothesis, say so and help another investigator". This directly maps to the Cyberneutics adversarial deliberation pattern.[^4][^3]

**Trajectory:** Agent Teams is under active development. The experimental flag suggests GA is planned. OpenCode's design proposal (issue #12711) explicitly cites Claude Code Agent Teams as inspiration, suggesting the pattern is becoming an industry standard.[^26]

**Gaps for Cyberneutics:**
1. No cross-provider model support (all agents must be Claude)
2. No structured voting or consensus mechanism (must be implemented in prompts)
3. No persistent deliberation state across sessions (task list persists but teammate context does not)
4. No formal "character" or "cognitive style" abstraction (must be encoded in spawn prompts)

## 5. LiteLLM and Ollama as MCP Servers

### LiteLLM MCP Support

**Current state:** LiteLLM v1.65.0 introduced MCP support, positioning the proxy as an **MCP Gateway**. The gateway allows centrally adding MCP server endpoints that developers can list and call through LiteLLM. LiteLLM's MCP integration includes OAuth 2.1 + JWT security and supports forwarding custom headers to backend MCP servers.[^36][^2][^1]

LiteLLM already provides a unified API to 100+ LLM providers. As an MCP Gateway, it bridges MCP clients (Claude Code, Cursor, etc.) with MCP tool servers, handling authentication, rate limiting, and cost tracking centrally. The community has also built a minimal CLI tool ("Assistant LiteLLM + MCP CLI") that streams LLM responses via LiteLLM while executing MCP tools.[^2][^37][^1]

**For Cyberneutics:** LiteLLM as MCP Gateway is the clearest path to Tier 3 (external multi-model orchestration). A coding agent like Claude Code could invoke an MCP tool backed by LiteLLM that calls GPT-5, Gemini, or any local model. The agent's own reasoning stays on Claude, but it can query other models as tools and incorporate their responses into deliberation.

### Ollama MCP Support

**Current state:** Ollama does **not** natively implement MCP. However, multiple bridges exist:[^38]

1. **Ollama MCP Server** (community): A full MCP server wrapping Ollama's API, including model management, chat completion, and configurable parameters.[^39]
2. **MCPHost**: A CLI tool that connects Ollama models to MCP servers, allowing local models to use MCP tools.[^38]
3. **LlamaIndex MCP client**: Provides MCP client functionality for connecting Ollama-backed agents to MCP servers.[^40]

### Wrapping an OpenAI-Compatible API as MCP

The pattern is well-established and straightforward:

1. **openapi-to-mcp-converter**: Automatically converts any OpenAPI v3 spec into a deployable MCP server configuration.[^41]
2. **MCP-OpenAI Bridge**: An existing community tool that bridges MCP servers with OpenAI's function calling interface, compatible with any OpenAI-API-compatible endpoint (including Ollama, LM Studio, vLLM).[^42]
3. **ToolRegistry**: A protocol-agnostic library that unifies native Python functions, OpenAPI services, MCP servers, and LangChain tools under a single interface.[^43]

A minimal MCP server wrapping an LLM API requires approximately 50-100 lines of Python using the FastMCP or MCP SDK. The core pattern: declare a tool (e.g., `query_model`), accept parameters (model name, prompt, temperature), call the LLM API, return the response as a tool result.[^44][^45]

**Evidence quality:** Official LiteLLM documentation, community MCP servers with active maintenance, and multiple tutorials. The pattern is production-ready.

### Existing Multi-Model MCP Servers

- **LiteLLM Proxy** itself serves as a multi-model gateway accessible via MCP[^46][^1]
- **Ollama MCP Server** provides access to any Ollama-hosted model[^39]
- **ToolRegistry** can aggregate tools from multiple MCP servers, OpenAPI endpoints, and native functions simultaneously[^43]

## 6. Agent Frameworks with Multi-Model Support

### CrewAI

**Multi-model:** Yes — CrewAI is explicitly **LLM-agnostic** and supports assigning different models to different agents based on task complexity, latency requirements, or cost constraints. Different agents can use different providers through LiteLLM as an abstraction layer. Over 20,000 GitHub stars; production-ready.[^29][^47][^28]

**Setup complexity:** Moderate. Requires Python, `pip install crewai`, API keys for each provider, and agent/task definitions. A 3-agent crew with different models can be configured in ~50 lines of Python. A non-developer power user would need basic Python comfort but no deep programming knowledge.[^28]

**Communication:** Coordinator-worker pattern with task delegation between agents. Supports sequential, hierarchical, and consensus-based processes.[^29][^28]

### AutoGen (Microsoft)

**Multi-model:** Yes — each agent takes an `llm_config` with a `config_list` of models. Different agents can use different providers (OpenAI, Azure, Anthropic, local GGUF models). The framework supports automatic fallback to alternate models on failure.[^31][^48]

**Setup complexity:** Moderate to high. Configuration via JSON files (`oai_config_list.json`). GroupChat manager handles multi-agent orchestration with customizable speaker selection. Supports asynchronous message exchange and container-based deployment.[^34][^31]

**Communication:** Conversation-based — all decisions expressed in natural language chat logs, enabling transparent, replayable traces.[^31]

### LangGraph

**Multi-model:** Yes — each node in the graph can use a different model. The CASTER framework (2026) provides dynamic model selection per node based on real-time state analysis, routing between e.g., GPT-4o vs. cheaper models depending on task complexity. LangGraph's `StateGraph` with conditional edges naturally supports routing to different model-backed nodes.[^30][^49]

**Setup complexity:** High. LangGraph requires understanding graph-based state machines, typed state definitions, and edge routing logic. It is the most flexible but also the most code-intensive option.[^32]

### Semantic Kernel (Microsoft)

**Multi-model:** Yes — agents are registered with the kernel, which abstracts AI services. Multiple models can be registered and swapped without system redesign. Supports concurrent, sequential, handoff, group chat, and Magentic orchestration patterns. Currently **experimental**.[^33][^50]

**Setup complexity:** Moderate. C# or Python SDK. Enterprise-focused with production-grade observability. The Magentic pattern supports manager-coordinated teams analogous to Claude Code Agent Teams.[^51]

### Clojure-Based Options

**Agent-o-rama:** A Clojure/Java agent framework built on Rama, inspired by LangGraph. Agents are defined as graphs of Clojure or Java functions with LangChain4j for LLM integration. Supports parallel execution, tracing, and durable storage. Multi-model is possible via LangChain4j's model abstraction.[^52][^53]

**Nubank pattern:** Nubank (a major Clojure shop) uses LiteLLM as a proxy layer, importing Python LiteLLM directly into the Clojure runtime for multi-provider access. This pattern provides a unified interface, centralized observability, and cost control across providers.[^54]

No pure Clojure agent framework with native multi-model orchestration exists. The practical path is Agent-o-rama + LangChain4j, or Clojure + LiteLLM via Python interop.

### Framework Comparison

| Framework | Multi-model | Communication | Setup complexity | Non-developer accessible |
|---|---|---|---|---|
| CrewAI | ✅ Cross-provider | Coordinator-worker, delegation | Moderate (~50 LoC) | Possible with guidance |
| AutoGen | ✅ Cross-provider | GroupChat, conversation-based | Moderate-High | Challenging |
| LangGraph | ✅ Dynamic routing | Graph state, conditional edges | High | No |
| Semantic Kernel | ✅ Kernel-registered | 5 orchestration patterns | Moderate (C#/Python) | Possible with guidance |
| Agent-o-rama | ✅ Via LangChain4j | Graph-based, parallel | Moderate (Clojure/Java) | No |

## 7. The Accessibility Question

### Simplest Current Path

**CrewAI with LiteLLM** is the simplest path to multi-model committee deliberation. A power user comfortable with API keys and Python basics can:

1. Install CrewAI (`pip install crewai`)
2. Configure API keys for each provider (Anthropic, OpenAI, Google)
3. Define 3-5 agents with different models, roles, and backstories
4. Define a "deliberation" task with sequential or hierarchical process
5. Run the crew

Total setup: ~1 hour, ~100 lines of Python. CrewAI's role-based abstraction maps naturally to the Cyberneutics character model — each "character" becomes an agent with a role, goal, and backstory. The framework handles turn-taking, task delegation, and result aggregation.[^28][^29]

**Limitation:** CrewAI's communication patterns are coordinator-worker, not free-form debate. Achieving genuine adversarial deliberation requires creative task design — e.g., a "debate" task where agents sequentially critique each other's positions.

### Most Capable Current Path

**LangGraph with CASTER-style routing** provides the most control. Each node in the graph represents a deliberation participant, with dynamic model selection, custom state management, and arbitrary communication topologies. This enables:[^30][^32]

- True round-robin debate with state accumulation
- Dynamic model selection based on deliberation phase
- Full observability via LangSmith traces
- Cost tracking per participant per round
- Conditional routing (e.g., escalate to stronger model if consensus not reached)

**Cost:** Requires significant Python development. Not accessible to non-developers.

### The Convergence Point

**Claude Code Agent Teams + LiteLLM MCP** represents a potential convergence of simplicity and capability. The setup:

1. Enable Agent Teams in Claude Code (one environment variable)
2. Deploy a LiteLLM MCP server exposing `query_model` as a tool
3. Configure Agent Teams with different personas in spawn prompts
4. Each teammate uses Claude for reasoning but can invoke `query_model` to get GPT-5 or Gemini perspectives

This is a **Tier 2.5** approach — native multi-agent deliberation architecture (Claude Code Agent Teams) augmented with cross-provider model access (LiteLLM MCP). The teammates' own reasoning runs on Claude, but they can incorporate diverse model perspectives as evidence. Setup: ~2 hours, requires familiarity with Claude Code, LiteLLM, and MCP.

## Implementation Tier Assessment

| Tier | Description | Status (March 2026) | Viable for Cyberneutics? |
|---|---|---|---|
| **Roleplay** | Single model, multiple personas in one context | ✅ Current baseline | Yes (limited by single context window) |
| **Tier 1** | Independent agents, single model family | ✅ Claude Code Agent Teams | Yes — native peer-to-peer deliberation |
| **Tier 2** | Built-in multi-model subagents | ⚠️ Partial — Cursor supports cross-provider; Claude Code supports intra-family | Cursor: limited deliberation support; Claude: no cross-provider |
| **Tier 2.5** | Native agents + MCP cross-provider tools | ✅ Claude Code Agent Teams + LiteLLM MCP | Yes — best near-term path |
| **Tier 3** | External orchestration via frameworks | ✅ CrewAI, AutoGen, LangGraph | Yes — most flexible, highest setup cost |

### Recommended Path for Cyberneutics

**Immediate (March 2026):** Use Claude Code Agent Teams with different Claude model tiers (Opus lead as moderator, Sonnet teammates as committee characters). This provides the deliberation architecture natively with zero external dependencies. Encode character cognitive styles in spawn prompts. Cost: ~$30-50 per multi-round deliberation session.[^3]

**Near-term (Q2 2026):** Deploy LiteLLM as an MCP server alongside Agent Teams. This enables Tier 2.5 — teammates can query GPT-5, Gemini, or local models as evidence-gathering tools, incorporating diverse model perspectives into Claude-native deliberation. Setup: moderate (LiteLLM deployment + MCP configuration).

**Strategic (H2 2026):** Monitor OpenCode's agent teams implementation (issue #12711) for genuine cross-provider multi-model agent teams. Also monitor CrewAI for potential integration with MCP and coding-agent-style tool access. The convergence of native multi-model agent teams with full peer-to-peer communication is the true Tier 2 target — it does not yet exist in any single product but is clearly the trajectory.[^26]

## Key Gaps

1. **No product combines cross-provider multi-model with peer-to-peer agent communication.** Claude Code Agent Teams has the best communication model but is Claude-only. CrewAI has the best multi-model support but uses coordinator-worker communication.

2. **No structured deliberation primitives.** Voting, consensus detection, position tracking, and argument strength assessment must be implemented in prompts or external logic. No agent framework provides these natively.

3. **No persistent deliberation state.** Agent Teams task lists persist across sessions, but teammate context windows do not. A multi-session deliberation (e.g., revisiting yesterday's debate) requires re-prompting from scratch.[^3]

4. **Cost scaling for deliberation.** Multi-round debate with 5 agents is token-intensive. Each broadcast message is injected into every other agent's context, creating O(n²) token growth per round. Cost optimization requires careful message design and selective (rather than broadcast) communication.[^3]

5. **No Clojure-native solution.** The closest path is Agent-o-rama + LangChain4j or Clojure + LiteLLM via Python interop. A pure Nix/Clojure/functional approach to multi-model deliberation does not exist as a packaged solution.[^52][^54]

---

## References

1. [MCP Overview](https://docs.litellm.ai/docs/mcp) - LiteLLM Proxy provides an MCP Gateway that allows you to use a fixed endpoint for all MCP tools and ...

2. [Securing LiteLLM's MCP Integration: Write Once, ...](https://www.linkedin.com/pulse/securing-litellms-mcp-integration-write-once-secure-rick-hightower-njksc) - This guide shows how to implement OAuth 2.1, JWT validation, and TLS encryption for LiteLLM's MCP in...

3. [Claude Code Agent Teams: The Practical Guide to Multi-Agent ...](https://blog.laozhang.ai/en/posts/claude-code-agent-teams) - Agent Teams in Claude Code let you orchestrate multiple AI sessions that communicate, share tasks, a...

4. [Claude Code Agent Teams: The Complete Guide 2026](https://claudefa.st/blog/guide/agents/agent-teams) - Guide to Claude Code Agent Teams for parallel multi-agent development. What they are, when to use th...

5. [Claude Code Agent Teams: What I Learned from Testing - LinkedIn](https://www.linkedin.com/pulse/claude-code-agent-teams-what-i-learned-from-testing-eric-buess-5itbc) - Agent teams are experimental and disabled by default. There's no toggle in the Claude Code CLI menu ...

6. [Thoughts on Claude Code's experimental Agent Teams feature?](https://www.reddit.com/r/ClaudeAI/comments/1ree1fi/thoughts_on_claude_codes_experimental_agent_teams/) - It spins up a team of agents. They work in parallel, share a task list, and can message each other d...

7. [Understanding the multi-headed agentic daemon of the coding seas](https://arxiv.org/html/2602.08765v1) - The framework is model-agnostic, designed to work with any CLI tool; this paper demonstrates it with...

8. [Comparing AI Agents to Cybersecurity Professionals in Real-World ...](https://arxiv.org/html/2512.09882v2) - ARTEMIS is a multi-agent framework featuring dynamic prompt generation, arbitrary sub-agents, and au...

9. [SWE-Bench Mobile: Can Large Language Model Agents Develop ...](https://arxiv.org/html/2602.09540v1) - We evaluate 22 agent-model configurations across four coding agents—three commercial (Cursor, Codex,...

10. [Windsurf (Codeium) Review 2026: AI Coding Agent Worth Switching ...](https://pinklime.io/blog/windsurf-codeium-review-2026) - It's an AI agent that can plan multi-step changes, edit multiple files, run terminal commands, and i...

11. [Sub agents in Windsurf - Reddit](https://www.reddit.com/r/windsurf/comments/1qfgkgo/sub_agents_in_windsurf/) - They allow us to run specialized agents in their own isolated context. That means we can run code re...

12. [AI Coding Agent: 2026 Comparison of Every Major Tool - Morph](https://morphllm.com/ai-coding-agent) - Windsurf (formerly Codeium) ranked #1 on LogRocket's AI dev tool power rankings. Wave 13 introduced ...

13. [Chat modes](https://aider.chat/docs/usage/modes.html) - Aider has a few different chat modes. By default, aider starts in “code” mode. As you are talking, y...

14. [how to add a multi-agent flow ? · Issue #1839 · Aider-AI/aider](https://github.com/Aider-AI/aider/issues/1839) - Also interested in this concept of having multiple agents (possibly using different models) with the...

15. [How Agent Mode Works | Continue Docs](https://docs.continue.dev/ide-extensions/agent/how-it-works) - In Agent mode, available tools are sent along with user chat requests · The model can choose to incl...

16. [Building Cloud Agents with Continue CLI - Blog](https://blog.continue.dev/building-async-agents-with-continue-cli/) - Continue CLI brings continuous AI to your terminal. Generate smart commits, run parallel analysis, a...

17. [Customization Overview | Continue Docs](https://docs.continue.dev/customize/overview) - Continue allows you to choose your favorite or even add multiple model providers. This allows you to...

18. [AI Companies don't want you to know this | VS Code + Continue](https://www.youtube.com/watch?v=13ab5dyOasI) - Author has hidden an important detail - you would require a mid to high end gpu with large vram(12-1...

19. [continue.dev agent mode + ??agent : r/LocalLLaMA - Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1mqcuy1/continuedev_agent_mode_agent/) - I've tried a variety of current models (mostly local) together with continue's agent mode, but I'm s...

20. [Overcome development disarray with Amazon Q Developer CLI ...](https://aws.amazon.com/blogs/devops/overcome-development-disarray-with-amazon-q-developer-cli-custom-agents/) - In this post I will explain how to configure a custom agent for front-end and back-end development. ...

21. [A2A protocol support for enabling complex workflow involving ...](https://github.com/aws/amazon-q-developer-cli/discussions/1448) - They don't appear to be using Agent2Agent. Is anyone working on anything similar in Amazon Q Develop...

22. [Google makes Jules, its AI coding agent, available to everyone with ...](https://siliconangle.com/2025/08/06/google-makes-jules-ai-coding-agent-available-everyone-free-paid-plans/) - It has the ability to handle multiple tasks at once, in parallel ... 2026 data predictions: Scaling ...

23. [Google's Jules coding agent moves beyond chat with new command ...](https://venturebeat.com/ai/googles-jules-coding-agent-moves-beyond-chat-with-new-command-line-and-api) - That's why we built Jules Tools, a lightweight command line interface, so you can spin up tasks, ins...

24. [Practical Agentic Coding with Google Jules](https://machinelearningmastery.com/practical-agentic-coding-with-google-jules/) - This pipeline allows you to delegate complex coding and development tasks without having Jules inter...

25. [Meet Google Jules: The Asynchronous AI Coding Agent - Kartaca](https://kartaca.com/en/meet-google-jules-the-asynchronous-ai-coding-agent/) - With Gemini, Jules can: Handle complex, multi-file changes. Understand codebase-specific context via...

26. [flat teams with named messaging, multi-model support, and TUI ...](https://github.com/anomalyco/opencode/issues/12711) - Multi-model — each teammate can use a different provider/model (e.g., Gemini for research, Claude fo...

27. [OpenCode Multi-Agent Setup: 3 Specialized AI Agents That 10x ...](https://amirteymoori.com/opencode-multi-agent-setup-specialized-ai-coding-agents/) - Configure OpenCode with 3 specialized AI agents: Claude Opus for coding, Perplexity for research, GP...

28. [CrewAI Multi-Agent AI Teams: Complete Guide with Memory - Mem0](https://mem0.ai/blog/crewai-guide-multi-agent-ai-teams) - Learn how to build multi-agent AI teams with CrewAI and add persistent memory with Mem0. Step-by-ste...

29. [Top 7 Agentic AI Frameworks in 2026: LangChain, CrewAI, and ...](https://www.alphamatch.ai/blog/top-agentic-ai-frameworks-2026) - With over 20,000 GitHub stars, CrewAI introduces a unique role-based approach where multiple AI agen...

30. [CASTER: Breaking the Cost-Performance Barrier in Multi-Agent ...](https://arxiv.org/html/2601.19793v1) - We propose CASTER (Context-Aware Strategy for Task Efficient Routing), a lightweight router for dyna...

31. [How AutoGen Framework Helps You Build Multi-Agent Systems](https://galileo.ai/blog/autogen-framework-multi-agents) - AutoGen solves multi-agent coordination by treating everything as a conversation. Each agent acts in...

32. [LangGraph: Multi-Agent Workflows - LangChain Blog](https://blog.langchain.com/langgraph-multi-agent-workflows/) - Multi-agent designs allow you to divide complicated problems into tractable units of work that can b...

33. [Semantic Kernel Agent Orchestration | Microsoft Learn](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent/agent-orchestration/) - Semantic Kernel's Agent Orchestration framework enables developers to build, manage, and scale compl...

34. [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent ...](https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/) - AutoGen agents are customizable, conversable, and can operate in various modes that employ combinati...

35. [Claude Code's Agent Teams Are Insane (Build Your AI Workforce)](https://www.youtube.com/watch?v=oC3F2SFaF9w) - With the Claude Opus 4.6 release, Anthropic shipped Agent Teams as a new Claude Code feature, and it...

36. [v1.65.0-stable - Model Context Protocol](https://docs.litellm.ai/release_notes/v1.65.0-stable) - Model Context Protocol (MCP)​ ... This allows you to add MCP server endpoints and your developers ca...

37. [Assistant (LiteLLM + MCP CLI)](https://lobehub.com/mcp/subashc2023-tinyclient) - Minimal, fast CLI that streams responses from an LLM (via LiteLLM) and executes Model Context Protoc...

38. [Set Up ClickHouse MCP Server with Ollama](https://clickhouse.com/docs/use-cases/AI/MCP/ollama) - At the time of writing (July 2025) there is no native functionality for using Ollama with MCP Server...

39. [Ollama MCP Server](https://mcpservers.org/servers/NightTrek/Ollama-mcp) - A powerful bridge between Ollama and the Model Context Protocol (MCP), enabling seamless integration...

40. [MCP meets Ollama: Build a 100% local MCP client - YouTube](https://www.youtube.com/watch?v=C64rVY1eN8k) - I just built a 100% local MCP client. (that you can connect to any MCP server) We often use Cursor I...

41. [Should you wrap MCP around your existing API? - Scalekit](https://www.scalekit.com/blog/wrap-mcp-around-existing-api) - Only certain API capabilities are wrapped as MCP tools, while ... By thoughtfully configuring your M...

42. [Run MCP Tools with Any OpenAI-Compatible LLM - Reddit](https://www.reddit.com/r/LocalLLaMA/comments/1h5edl7/mcp_openai_bridge_run_mcp_tools_with_any/) - I created an MCP implementation that bridges the gap between MCP servers (and tools) and OpenAI's fu...

43. [Unified Tool Integration for LLMs: A Protocol-Agnostic Approach to ...](https://arxiv.org/html/2508.02979v1) - While major AI providers have announced MCP support—with Anthropic offering native integration, Open...

44. [Tools for Your LLM: a Deep Dive into MCP | Towards Data Science](https://towardsdatascience.com/tools-for-your-llm-a-deep-dive-into-mcp/) - When is a program an MCP server? · declaring tools · accepting a tool call request · executing the r...

45. [How to use Anthropic MCP Server with open LLMs, OpenAI or ...](https://www.philschmid.de/mcp-example-llama) - Convert tools into LLM-compatible function calling tools (JSON Schema) with callable to our MCP Serv...

46. [Using your MCP](https://docs.litellm.ai/docs/mcp_usage) - This document covers how to use LiteLLM as an MCP Gateway. You can see how to use it with Responses ...

47. [How to Build Multi-Agent Systems: Complete 2026 Guide - Dev.to](https://dev.to/eira-wexford/how-to-build-multi-agent-systems-complete-2026-guide-1io6) - Amazon used Amazon Q Developer to coordinate agents that modernized thousands of legacy Java applica...

48. [Getting Started with AutoGen - A Framework for Building Multi ...](https://newsletter.victordibia.com/p/getting-started-with-autogen-a-framework) - Each agent in AutoGen takes an llm_config parameter that includes a config_list of models. The first...

49. [Building AI Agents with LangGraph | Routing Logic - AI Advances](https://ai.gopubby.com/building-ai-agents-with-langgraph-routing-logic-2c252aa9240b) - A special node called ToolNode that knows how to use different tools when needed; A smart routing sy...

50. [Orchestrating Multi‑Agent AI With Semantic Kernel | Digital Bricks](https://www.digitalbricks.ai/blog-posts/orchestrating-multi-agent-ai-with-semantic-kernel) - Semantic Kernel (SK) is an open-source toolkit from Microsoft that serves as a central orchestration...

51. [Semantic Kernel: Multi-agent Orchestration - Microsoft Dev Blogs](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-multi-agent-orchestration/) - Semantic Kernel introduces a new multi-agent orchestration framework that enables developers to buil...

52. [Introducing Agent-o-rama: build, trace, evaluate, and monitor stateful ...](https://blog.redplanetlabs.com/2025/11/03/introducing-agent-o-rama-build-trace-evaluate-and-monitor-stateful-llm-agents-in-java-or-clojure/) - Agents are defined as simple graphs of Java or Clojure functions that execute in parallel. Agent-o-r...

53. [Scalable, Traceable, Stateful AI agents in Pure Clojure or Java](https://www.youtube.com/watch?v=mNLWtM3Iya4) - ... Agent-o-rama models agents as graphs of Clojure or Java functions that do LLM calls, interact wi...

54. [Building AI agentes in practice with Clojure - Building Nubank](https://building.nubank.com/building-ai-agentes-in-practice-with-clojure/) - LiteLLM is a proxy that standardizes access to multiple models and providers behind a single API, re...

