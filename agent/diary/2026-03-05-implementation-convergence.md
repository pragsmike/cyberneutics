# Implementation Convergence: Subagents, Multi-Model, and the Platform Bottleneck

*Wednesday, 5 March 2026*

A session examining the implementation mechanics of committee deliberations — specifically how the repo's research programs relate to what commercial coding agents actually offer, and where an existing Clojure library (pcrit-llm) changes the picture.

---

## I. The Artificial Separation

The repo currently treats multi-model committees and subagent-based deliberation as separate research programs with separate implementation paths. The multi-model program (`meta/research-programs/multi-model-committee.md`) assumes Python API orchestration — a `SimpleChair` class iterating through vendor endpoints. The subagent exploration (`wild/subagent-personas-for-debate/`) assumes single-model but architecturally independent agents communicating peer-to-peer via Claude Code's Agent Teams.

This separation is an artifact of current platform limitations, not a conceptual necessity. The two programs are asking complementary questions: *does genuine model diversity improve deliberation?* and *does genuine agent independence improve deliberation?* These are orthogonal axes. A system could have both (different models running as independent peer agents), either one alone, or neither (the current single-model roleplay simulation).

The interesting finding is that the repo has documented the problem from both ends without connecting them. The field notes (2026-02-26) identify the hub-and-spoke vs. peer-agent distinction as "epistemically fundamental." The multi-model reference document identifies the single-model monoculture as a structural limitation. But neither program acknowledges that a single platform feature — "spawn subagent on model X" — would collapse both programs into one.

---

## II. Three Implementation Tiers

The conversation surfaced a clearer way to think about implementation paths, ordered by accessibility:

### Tier 1: Built-in subagents, single model

Use whatever subagent mechanism the coding agent provides (Claude Code Agent Teams, or future equivalents in Codex, Cursor, etc.). Each committee character runs as an independent agent process with its own context window, but all on the same underlying model.

**What you get**: Genuine agent independence — separate context, concurrent execution, peer-to-peer communication. No monoculture escape, but architectural independence that the current roleplay simulation lacks.

**Who can use it**: Anyone with the product. No API keys, no infrastructure, no programming required.

**What you lose**: All characters still share the same training distribution. Disagreement emerges from architectural independence (different accumulated context) rather than genuinely different cognitive styles.

### Tier 2: Built-in subagents, multiple models

If a coding agent offered "spawn subagent on model X" — routing different characters to different providers — you'd get both axes at once. Genuine architectural independence *and* genuine model diversity.

**What you get**: The full hypothesis tested by the multi-model program, delivered through the subagent mechanism, with no orchestration code.

**Who can use it**: Anyone with the product, if the product supports it. Currently no commercial coding agent offers this.

**What you lose**: Nothing, in principle. This is the convergence point. The limitation is that it doesn't exist yet.

### Tier 3: External orchestration via LiteLLM/Ollama

Use an API multiplexer (LiteLLM, Ollama, or similar) to route different model names to different providers through a single endpoint. Write the orchestration in Clojure (or Python, but see below) as a standalone process.

**What you get**: Full multi-model, any combination of providers, complete control over the orchestration logic, cost tracking per character per turn.

**Who can use it**: Power users comfortable running a LiteLLM proxy, managing API keys for multiple providers, and running Clojure (or Python) processes. Not casual users.

**What you lose**: Agent independence in the peer-to-peer sense. The orchestrator is hub-and-spoke by construction — it's a `reduce` over sequential API calls. You can parallelize with `pmap` or `core.async`, but each call is stateless; there are no persistent reasoning threads.

### The tradeoff

Tier 1 is accessible but limited. Tier 3 is powerful but requires infrastructure. Tier 2 would be the sweet spot but doesn't exist. The strategic question is: which tier do we build for first?

The argument for Tier 1: even single-model multi-subagent deliberation is better than the roleplay simulation we have now. If five independent Claude agents with separate context windows deliberate peer-to-peer, the disagreement that emerges is more authentic than one Claude playing five roles in sequence. The independence caveat noted in the Condorcet comparison ("true independence of CJT-style votes is hard to guarantee") is directly addressed — these would be genuinely independent processes.

The argument for Tier 3: it's available now, it answers the multi-model question, and the infrastructure requirement (LiteLLM) is modest for anyone already comfortable with API access. And the Clojure implementation already exists in embryonic form.

These are not mutually exclusive. Tier 1 for accessibility and validation, Tier 3 for the full multi-model experiment.

---

## III. pcrit-llm as Foundation

The PromptCritical project produced a Clojure library (`pragsmike/pcrit-llm`) that provides a clean LLM interface through a LiteLLM proxy. Two things about it matter for cyberneutics implementation:

**The API shape is almost exactly right.** `call-model` takes a model name string (carrying the provider prefix: `"openai/gpt-4o"`, `"anthropic/claude-sonnet-4-5"`) and a prompt, returning `{:content ... :generation-metadata {:model, :provider, :token-in, :token-out, :cost-usd-snapshot, :duration-ms}}`. A deliberation round reduces to:

```clojure
(defn deliberation-round [transcript assignments]
  (mapv (fn [{:keys [character model brief]}]
          (let [prompt (render-prompt brief character transcript)]
            (assoc (llm/call-model model prompt)
                   :character character)))
        assignments))
```

The whole deliberation is `(reduce deliberation-round [] (range num-rounds))` with transcript accumulation. The generation-metadata gives provenance tracking per character per turn for free — token counts, cost, latency, provider identity. This is exactly the decorated-text metadata that palgebra requires.

**LiteLLM as the abstraction layer** means multi-model is already built in. The model name is the only thing that changes between `"anthropic/claude-sonnet-4-5"` (Frankie) and `"openai/gpt-4o"` (Vic). No provider-specific client code. The `call-model` function doesn't know or care which provider it's hitting.

**What's missing is small.** Currently `call-model` takes a single prompt string and wraps it as one user message. Multi-turn deliberation wants a message sequence (system prompt for the character brief, conversation history as prior turns). That's a straightforward extension — accept either a string or a message vector.

Note on Ollama: Ollama now offers the same model-multiplexing functionality as LiteLLM for locally-hosted models, with an OpenAI-compatible API. For users who want to run multi-model committees entirely locally (e.g., different Llama variants for different characters), Ollama would serve the same role as LiteLLM without requiring cloud API keys. The pcrit-llm library would work with either by changing the endpoint URL.

---

## IV. Why Clojure Over Python

The multi-model reference document specs the orchestrator as Python classes (`SimpleChair`, `SmartChair`) with methods, inheritance, and mutable state. This obscures the actual computational structure, which is simple: a deliberation is a fold over rounds, each round is a map over characters, each character invocation is a stateless function call. The Python version makes it look like an object-oriented system when it's actually a pipeline.

Clojure makes the pipeline structure visible:

- **Immutable data**: The transcript accumulates; nothing mutates. Each round produces a new transcript by `conj`-ing new entries. This is naturally thread-safe for parallel execution.
- **Composable transformations**: The fan (scenarios) and funnel (committee) are just functions that compose. `(funnel (fan situation))` is the deliberated-choice monad. No framework needed.
- **Concurrency primitives**: `core.async` channels or `pmap` for parallel model calls. If we want Maya and Frankie to reason concurrently (not sequentially), that's a one-word change from `mapv` to `pmap`. The Python version would need threading, asyncio, or a concurrency framework.
- **REPL-driven development**: Deliberation runs can be developed interactively. Call one model, inspect the result, adjust the prompt, call the next. This is exactly the exploratory workflow that cyberneutics advocates.

The Python orchestrator code in the reference document is roughly 200 lines of class scaffolding. The equivalent Clojure would be roughly 40 lines of functions operating on maps. The computational content is the same; the ceremony is different.

---

## V. Implications for Research Programs

### Multi-model committee program

The experimental protocol (Phases 1-4) is sound regardless of implementation language. What changes:

- **Implementation language**: Clojure via pcrit-llm replaces the Python `SimpleChair`/`SmartChair` classes. The reference document's code examples should get Clojure equivalents.
- **Infrastructure assumption**: LiteLLM (or Ollama for local models) as the provider abstraction layer, rather than direct multi-vendor API clients.
- **Cost tracking**: Already built into pcrit-llm's `generation-metadata`. No separate cost calculation needed.

### Evaluating deliberative architectures program

The architecture comparison matrix (conditions B1-B3, C1-C3) currently holds model constant: "Same base LLM for all conditions." The multi-model dimension is explicitly deferred to the multi-model program. This is the right separation for a controlled experiment. But a future Phase 2 could cross the architecture conditions with the model-diversity conditions — testing whether peer-agent + multi-model (Tier 2) outperforms peer-agent + single-model (Tier 1) outperforms hub-and-spoke + multi-model (Tier 3).

### Ablation study

The ablation study's factor definitions (Scenarios, Committee, Deliberated Choice, Evaluation, Robert's Rules) are all process-level factors. Implementation architecture (single-model roleplay vs. single-model subagent vs. multi-model subagent) is a separate axis that could be crossed with the process factors. But that multiplies the run budget considerably. Better to resolve the process-level ablation first, then test architecture as a separate factor on the winning process configuration.

### Societies of thought, Item 8 (MOOLLM integration)

MOOLLM's Room/Card/File architecture is conceptually aligned with the subagent approach — each Card is essentially an agent with defined behaviors, Rooms provide the communication context. If MOOLLM materializes as a platform, it would be a fourth implementation tier alongside the three above. The mapping work specified in Item 8 remains relevant regardless of which tier we build first.

---

## VI. What to Watch For

The key external development that would change the picture: **any commercial coding agent offering model routing for subagents.** If Claude Code's Agent Teams added a `model` parameter to the agent spawn call, or if Codex offered similar, the Tier 2 path opens immediately and the need for external orchestration (Tier 3) diminishes for all but the most customized use cases.

Until then, the practical path is:

1. **Tier 1 now**: Experiment with Claude Code Agent Teams for single-model multi-subagent deliberation. Test whether genuine agent independence (separate context windows, peer-to-peer communication) improves deliberation quality over the current single-context roleplay. This requires no code beyond the skill files.

2. **Tier 3 in parallel**: Use pcrit-llm + LiteLLM for the multi-model experiments specified in the research program. This is the power-user path and produces the empirical evidence about whether model diversity matters.

3. **Tier 2 when available**: Monitor the coding agent landscape for multi-model subagent support. When it arrives, the two tiers converge and the orchestration code becomes unnecessary.

---

## VII. Open Questions

- Does Claude Code's Agent Teams feature currently support enough concurrent agents and message volume for a full 5-character deliberation with multiple rounds? The feature is experimental; practical limits are unknown.
- What is the actual quality difference between single-model subagent deliberation (Tier 1) and single-model roleplay simulation (current)? This is testable now and would be the most immediately valuable experiment.
- How much of pcrit-llm's `call-model` needs to change to support message sequences (system + conversation history) rather than single prompts? Likely a small extension but worth scoping.
- Should the multi-model research program's reference document be updated now with Clojure examples alongside the Python, or should we wait until Phase 1 runs are underway?
