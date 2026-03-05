# Committee Implementation Taxonomy

This document describes the design space for implementing adversarial committee deliberations. It provides a shared vocabulary for the research programs that investigate different regions of this space. Each program tests a specific hypothesis within the taxonomy; this document explains how they relate.

---

## The Two Axes

Committee deliberation quality is affected by at least two independent implementation choices:

**Model diversity**: Do all committee characters share the same underlying model (same training distribution, same biases, same latent space), or do different characters use genuinely different models?

**Agent independence**: Do characters share a single context window (one model instance roleplaying multiple voices in sequence), or does each character run as an independent agent process with its own context?

These axes are orthogonal. Varying one while holding the other constant tests a different hypothesis.

---

## The Taxonomy

|  | Single model | Multi-model |
|---|---|---|
| **Shared context** (roleplay) | Current baseline. One model simulates all five characters in a single context window. Disagreement is performed, not emergent. | Not meaningful — a single context can only run one model. |
| **Independent agents** | Each character runs as a separate agent process with its own context. All agents use the same model. Disagreement can emerge from architectural independence (different accumulated context, separate reasoning threads) even without model diversity. | Each character runs as a separate agent using a different model. Genuine independence *and* genuine diversity. The convergence point. |

The bottom-right cell is the theoretical ideal. The practical question is how to get there given current platform constraints.

---

## Three Implementation Tiers

### Tier 1: Built-in subagents, single model

Use the subagent mechanism provided by a commercial coding agent (e.g., Claude Code Agent Teams). Each committee character runs as an independent agent process, but all on the same underlying model.

**What you get**: Genuine agent independence — separate context windows, potential for concurrent execution, peer-to-peer communication. The single-model monoculture remains, but architectural independence removes the artificial constraint of one model playing five roles in sequence.

**Who can use it**: Anyone with the product. No API keys, no infrastructure, no programming required.

**What it tests**: Does agent independence alone improve deliberation quality? (See [agent-independence.md](agent-independence.md).)

### Tier 1+: Built-in subagents, intra-family model selection

Claude Code Agent Teams supports specifying different Claude models per teammate (Opus for the lead, Sonnet for teammates, Haiku for sub-subagents). This introduces *some* model diversity (different capability tiers, different cost profiles) while retaining native peer-to-peer communication — but all models share the same provider's training distribution. This is a half-step beyond Tier 1: more than single-model, less than cross-provider diversity.

**Who can use it**: Anyone with Claude Code. No external infrastructure.

**What it tests**: Whether intra-family model diversity (capability tiers) adds value beyond single-model independence.

### Tier 2: Built-in subagents, cross-provider models

A coding agent that allows spawning subagents on genuinely different models from different providers. This is the convergence point — genuine agent independence *and* genuine model diversity, with no orchestration code.

**Current state (March 2026)**: Partially exists. Cursor 2.4 supports cross-provider model selection per agent (Claude, GPT, Gemini) but uses hub-and-spoke communication — no peer-to-peer debate. Claude Code Agent Teams has peer-to-peer but is Claude-only. OpenCode has a design proposal (issue #12711) for cross-provider agent teams with peer-to-peer messaging, but the feature is still in development. **No product currently combines cross-provider multi-model with peer-to-peer agent communication.** See `wild/coding-agent-subagent-capabilities-multi-model-support.md` for the full landscape survey.

**What it tests**: The full hypothesis — both axes at once.

### Tier 2.5: Native agents + cross-provider MCP tools

Use Claude Code Agent Teams for the deliberation architecture (peer-to-peer communication, independent context windows) and a LiteLLM MCP server for cross-provider model access. Each teammate's own reasoning runs on Claude, but it can invoke an MCP tool backed by LiteLLM to query GPT-5, Gemini, or local models and incorporate those perspectives as evidence.

**What you get**: The peer-to-peer deliberation architecture of Tier 1, augmented with cross-provider model perspectives. Not a full model swap for each agent's reasoning (that's Tier 2), but genuine access to diverse model outputs during deliberation.

**Who can use it**: Users comfortable with Claude Code, LiteLLM deployment, and MCP configuration. Setup: ~2 hours.

**What it tests**: Whether incorporating diverse model perspectives as tool-accessed evidence (rather than as each agent's native reasoning) provides meaningful diversity benefit.

### Tier 3: External orchestration via LiteLLM

Use an API multiplexer ([LiteLLM](https://github.com/BerriAI/litellm) or [Ollama](https://ollama.ai/) for local models) to route different model names to different providers through a single endpoint. A standalone orchestrator process — implemented in Clojure using [pcrit-llm](https://github.com/pragsmike/pcrit-llm) — manages the deliberation.

**What you get**: Full multi-model support, any combination of providers, complete control over orchestration logic, cost tracking per character per turn via pcrit-llm's `generation-metadata`.

**Who can use it**: Power users comfortable running a LiteLLM proxy and providing API keys for multiple providers. The setup is modest: install LiteLLM, configure API keys, run the Clojure orchestrator.

**What it tests**: Does model diversity improve deliberation quality? (See [multi-model-committee.md](multi-model-committee.md).)

**Trade-off vs. Tier 1**: Tier 3 gives model diversity but the orchestrator is hub-and-spoke by construction — a `reduce` over sequential (or parallel) API calls. There are no persistent independent reasoning threads. Tier 1 gives agent independence but no model diversity. Tier 2 partially exists but no product yet combines cross-provider models with peer-to-peer communication. Tier 2.5 is currently the best practical compromise: native peer-to-peer architecture with cross-provider perspectives accessed as tool evidence.

**LiteLLM vs. Ollama**: LiteLLM multiplexes across cloud providers (Anthropic, OpenAI, Google, etc.) through a single OpenAI-compatible endpoint. Ollama does the same for locally-hosted models. Both expose the same API shape. pcrit-llm works with either by changing the endpoint URL. LiteLLM is needed for frontier model access; Ollama opens the door to experiments with open-weight models at no marginal cost.

---

## How the Research Programs Map to the Taxonomy

| Program | Tier | Axis tested | Relationship |
|---------|------|------------|--------------|
| [agent-independence.md](agent-independence.md) | 1 | Agent independence (model held constant) | Fast, cheap precursor experiment. Tests whether architectural independence alone improves deliberation. |
| [agent-independence.md](agent-independence.md) | 1+ | Intra-family model diversity | Extension of Tier 1: same platform (Agent Teams), different Claude models per teammate. Tests whether capability-tier diversity adds value. |
| [multi-model-committee.md](multi-model-committee.md) | 3 | Model diversity (via LiteLLM orchestration) | The main multi-model experiment. Tests whether different models for different characters improves deliberation. |
| (future) | 2.5 | Cross-provider perspectives via MCP tools | Agent Teams architecture + LiteLLM MCP server. Tests whether tool-accessed diverse model outputs provide meaningful diversity within a native peer-to-peer architecture. |
| [evaluating-deliberative-architectures.md](evaluating-deliberative-architectures.md) | Any | Deliberative *structure* (architecture-agnostic) | Tests which deliberative structures (single prompt, hub-and-spoke, peer-agent, deliberated choice) anticipate risks. Holds model constant; holds implementation mechanism constant within a run. Reusable across all tiers — its conditions (B1–B3, C1–C3) characterize whatever mechanism implements them. |

The ablation study, condorcet comparison, and societies-of-thought program are process-level investigations (which *components* of the pipeline matter, not which *implementation* carries them) and are unaffected by this taxonomy.

---

## The Convergence Observation

Tiers 1 and 3 are currently the most accessible paths — Tier 1 for anyone with the product, Tier 3 for power users with API keys. They test different axes. Tier 2.5 is a viable middle ground that combines the peer-to-peer architecture of Tier 1 with cross-provider model access via MCP, though it requires more setup than either pure path.

If a commercial coding agent adds cross-provider multi-model subagent support with peer-to-peer communication (full Tier 2), the programs collapse into one: run the existing `/committee` skill with each character routed to a different model via the platform's native mechanism. As of March 2026, Tier 2 partially exists — Cursor 2.4 has cross-provider model selection but hub-and-spoke communication; Claude Code Agent Teams has peer-to-peer but is Claude-only; OpenCode has a design proposal for the combination but hasn't shipped it.

Until full Tier 2 arrives, the programs are complementary. A positive result from either one (agent independence helps, or model diversity helps) motivates pursuing the other. A positive result from both motivates pursuing Tier 2 aggressively — or using Tier 2.5 as an interim solution.

---

## Implementation Notes

### Clojure over Python

The multi-model reference document (`multi-model-committee-reference.md`) contains Python orchestrator code (the `SimpleChair`/`SmartChair` classes). The preferred implementation language is Clojure, for reasons documented in the reference and summarized here: a deliberation is a fold over rounds, each round a map over characters, each character invocation a stateless function call. Clojure makes this pipeline structure visible where Python obscures it with class hierarchies. Immutable data, composable transformations, and REPL-driven development match the exploratory workflow cyberneutics advocates.

### pcrit-llm

The [pcrit-llm](https://github.com/pragsmike/pcrit-llm) library provides a clean Clojure interface to LLMs through a LiteLLM proxy. Its `call-model` function takes a model name (carrying the provider prefix, e.g., `"openai/gpt-4o"`, `"anthropic/claude-sonnet-4-5"`) and a prompt, returning content plus generation metadata (token counts, cost, latency, provider). Multi-model routing is built in — the model name is the only parameter that changes between characters. Cost and provenance tracking are automatic.

### MCP considerations

For Tier 3, the orchestrator is a standalone Clojure process that talks to LiteLLM over HTTP. No MCP integration is needed. For Tier 2.5, LiteLLM v1.65.0+ already functions as an MCP Gateway — it can expose cross-provider model access as MCP tools directly, with no custom wrapper needed. This makes the Tier 2.5 setup concrete: deploy LiteLLM with MCP enabled, configure Claude Code to use it as an MCP server, and each Agent Teams teammate gains access to cross-provider model queries as a tool alongside its native Claude reasoning.

---

## Prior Work

This taxonomy was developed from several sources within the repository:

- `wild/subagent-personas-for-debate/README.md` (now superseded by this document and [agent-independence.md](agent-independence.md)) — documented the Cowork plugin attempt, the hub-and-spoke failure, and three alternative coordination schemes (Agent Teams, filesystem blackboard, MCP server).
- `agent/diary/2026-02-26-cyberneutics-field-notes.md` §I, §II — identified the hub-and-spoke vs. peer-agent distinction as epistemically fundamental and documented the agentic coding landscape.
- `agent/diary/2026-03-05-implementation-convergence.md` — first articulation of the three-tier framework and the convergence observation.
- `artifacts/integration-with-moollm.md` — four escalating patterns (single instance through parallel multi-instance) that map to this taxonomy.
- `references/coding-agent-subagent-capabilities-2026-03.md` — comprehensive landscape survey (March 2026) of coding agent subagent capabilities, multi-model support, agent frameworks, and MCP servers. Source for the Tier 1+/2/2.5 refinements and the "partially exists" assessment of Tier 2.
