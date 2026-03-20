**Research brief: LLM-based deliberation workflows — prior art, packaged implementations, and metacognition handling**

You are researching the landscape of multi-agent LLM deliberation systems — frameworks where multiple LLM personas, agents, or model instances argue, debate, or deliberate to reach a decision or recommendation. The goal is to find prior art, especially implementations that have been packaged as reusable tools (skills, plugins, prompt libraries, MCP servers, agent frameworks), and to understand how (if at all) they handle metacognition (agents tracking or reporting confidence in their own outputs, and that confidence being validated or used downstream).

**Context on why this matters:** A project called Cyberneutics uses structured adversarial committee deliberation — five named personas with distinct cognitive propensities debate under Robert's Rules, produce a resolution with votes, then undergo independent evaluation and remediation. It has recently added a metacognition layer: each persona reports numeric confidence (1–4) at resolution; a register accumulates calibration data across runs (was high confidence correlated with being on the winning side?); and a "with-register" mode feeds that calibration history back into subsequent deliberations so the synthesis can weight claims by track record. The research question is: who else is doing anything like this, how far have they gotten, and what have they learned — especially about metacognition?

**What to find:**

1. **Multi-agent debate and deliberation frameworks.** Systems where multiple LLM agents (whether same-model personas or different models) argue toward a decision. Include:
   - Academic papers (e.g., "Debate" from Irving et al.; "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate"; "LLM-Deliberation"; Society of Mind / Society of Models papers; Constitutional AI's self-critique as a degenerate case)
   - Open-source implementations (GitHub repos, agent frameworks like AutoGen, CrewAI, MetaGPT, Camel, ChatDev that support multi-agent debate patterns)
   - Commercial products or features (e.g., ChatGPT's "thinking" or extended thinking as internal deliberation; any product that exposes multi-persona debate to end users)

2. **Packaged implementations specifically.** Things someone can install and use, not just papers:
   - Claude Code skills, MCP servers, or plugins that implement deliberation
   - GPT custom instructions, system prompts, or "GPTs" in the OpenAI store that run multi-persona debates
   - LangChain/LangGraph templates for debate or deliberation
   - AutoGen, CrewAI, or other agent framework recipes specifically for adversarial deliberation (not just task decomposition)
   - Prompt libraries (e.g., on GitHub, PromptBase, or similar) that package multi-persona debate prompts
   - Any Cowork plugins, Claude Code skills, or similar that do structured deliberation

3. **Metacognition in LLM systems.** How do any of the above handle the question "how much should we trust this output?" Specifically:
   - Do agents report confidence? Numeric? Calibrated? Per-claim or per-decision?
   - Is confidence ever validated against outcomes (calibration tracking)?
   - Is calibration history ever fed back into subsequent runs?
   - Are there systems that track which agent/persona has been reliable over time?
   - Is there any equivalent of meta-d'/d' (signal detection theory metacognitive efficiency) applied to LLM outputs?
   - Related: LLM calibration literature (e.g., Kadavath et al. "Language Models (Mostly) Know What They Know"; Tian et al. on verbalized confidence; any work on whether LLMs can self-assess accuracy)

4. **Adjacent patterns that aren't labeled "deliberation" but function similarly:**
   - Mixture of Experts at the prompt level (not architecture level)
   - "Ensemble" prompting where multiple LLM calls are aggregated
   - Self-consistency / majority voting (Wang et al.) — the simplest version of multi-agent aggregation
   - Reflection/self-critique loops (Reflexion, Self-Refine) — single-agent metacognition
   - Constitutional AI's critique-revision loop as a two-agent system
   - Anthropic's "extended thinking" or OpenAI's "reasoning tokens" as internalized deliberation

5. **Evaluation and comparison.** For any system found:
   - How is deliberation quality measured? (Rubrics? Human preference? Task accuracy?)
   - Is there evidence that multi-agent deliberation outperforms single-agent prompting? Under what conditions?
   - What are the failure modes? (Groupthink? Sycophancy between agents? Cost?)

**What to prioritize:**
- Packaged, reusable implementations over one-off research prototypes
- Systems that include any form of metacognition or confidence tracking over those that don't
- Systems that have been empirically compared to simpler baselines
- Anything published or updated in 2024–2026

**Output format:** Organize findings by category (frameworks, packaged tools, metacognition handling, adjacent patterns). For each item, provide: name, source (URL/paper), what it does, whether it's packaged/reusable, how it handles metacognition (if at all), and any empirical evidence of effectiveness. Flag anything that closely parallels the Cyberneutics approach (structured adversarial personas with role differentiation, evaluation/remediation cycles, cross-run calibration tracking).
