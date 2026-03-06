# LLM-Based Deliberation Workflows: Prior Art, Packaged Implementations, and Metacognition Handling

## Executive Summary

The landscape of multi-agent LLM deliberation has exploded since 2023, with dozens of academic frameworks, several packaged tools, and a growing (but still immature) treatment of metacognition. The core finding for the Cyberneutics project is that **no existing system combines all three of its distinguishing features**: structured adversarial personas with role differentiation, formal evaluation/remediation cycles, and cross-run calibration tracking fed back into subsequent deliberations. Individual components exist — confidence-weighted voting (ReConcile), dynamic reputation tracking (DRF), persistent metacognitive memory (DS-MCM), and packaged multi-persona debate skills (Clear Thought MCP, MOOLLM) — but their integration into a single deliberative pipeline with a calibration register is novel. The closest parallel is DS-MCM's "Slow Experience-Driven Monitor" (Jan 2026), which accumulates metacognitive patterns from historical trajectories and feeds them back into real-time monitoring, though it targets deep search agents rather than structured committee deliberation.

***

## Multi-Agent Debate and Deliberation Frameworks

### Foundational Academic Work

The field traces to two independent origins: **Irving et al. (2018)** proposed AI Safety via Debate, where two AI systems argue before a human judge to ensure truthfulness — framing adversarial debate as an alignment mechanism. This work has been extended with complexity-theoretic formalization and applied to safety cases for deployed LLMs.[^1][^2][^3][^4][^5]

The **Multi-Agent Debate (MAD) framework** by Liang et al. (2023) introduced the "tit-for-tat" debate structure to combat the Degeneration-of-Thought (DoT) problem in self-reflection, where LLMs that become confident in incorrect answers cannot generate novel reasoning through reflection alone. This work demonstrated that structured adversarial exchange between agents outperforms single-agent self-reflection on reasoning tasks. The original implementation is available on GitHub.[^6][^7][^8]

**Du et al. (2023)** demonstrated independently that multi-round debate enables LLMs to correct each other's errors and improve logical consistency. **ReConcile** (Chen, Saha & Bansal, ACL 2024) extended this to a round-table conference among heterogeneous LLMs (ChatGPT, Bard, Claude2), adding **confidence-weighted voting** where agents express uncertainty that is shared in discussion prompts and used to weight the final consensus. ReConcile improved over single-agent baselines by 7.7% and outperformed GPT-4 on several benchmarks.[^9][^10][^11][^12]

### Recent Advances (2024–2026)

**DMAD (Diverse Multi-Agent Debate, ICLR 2025)** breaks agents' "fixed mental sets" by assigning distinct reasoning approaches per agent, outperforming traditional MAD in fewer rounds. **GroupDebate** enhances efficiency using group communication structures.[^13][^14]

**ConfMAD** (Lin & Hooi, Sep 2025) integrates explicit confidence expression throughout the debate process. Agents communicate numeric confidence levels, and the framework analyzes how confidence influences debate dynamics — offering insights into designing confidence-aware MAD systems. This is the most direct academic treatment of intra-debate confidence, though it does not track confidence across runs.[^15]

**iMAD (intelligent Multi-Agent Debate)** selectively triggers debate only when it is likely to correct an initially wrong answer, using a debate-decision classifier based on confidence scores and semantic uncertainty to avoid wasting tokens on unnecessary deliberation.[^16]

**AgentAuditor** (Feb 2026) replaces majority voting with evidence-based auditing over a Reasoning Tree. Its **Anti-Consensus Preference Optimization (ACPO)** trains an adjudicator on historical majority-failure cases, rewarding minority-correct selections — directly addressing the "confabulation consensus" failure mode where correlated LLM biases produce convergent wrong answers. AgentAuditor yields up to 5% absolute accuracy improvement over majority voting while using ~50% fewer tokens, and recovers 65–82% of minority-correct cases (vs. 0% for majority voting).[^17]

**UDPO (Uncertainty-Driven Policy Optimization, Feb 2026)** mitigates "debate collapse" by penalizing self-contradiction, peer conflict, and low-confidence outputs with agent-specific asymmetric penalties.[^18]

### Failure Modes

A critical finding for Cyberneutics: **sycophancy between agents is a documented core failure mode**. Tang et al. (Sep 2025) demonstrated that inter-agent sycophancy amplifies "disagreement collapse" before reaching correct conclusions, and can yield lower accuracy than single-agent baselines. Their design recommendation: cap debate rounds at 2–3 exchanges, implement automated diminishing-returns detection, and use heterogeneous agents (different models, not just different personas of the same model). Separate work on failure modes by Subramanian et al. (2025) showed debate can harm group performance with heterogeneous agents, challenging the narrative that more discussion is inherently beneficial.[^19][^20]

***

## Packaged Implementations

### Agent Frameworks Supporting Deliberation

| Framework | Debate Support | Metacognition | Packaged? | Notes |
|-----------|---------------|---------------|-----------|-------|
| **AutoGen** (Microsoft) | Yes — used as platform for sycophancy research[^19]; debate templates available | None built-in | ✅ pip install | General multi-agent orchestration; debate is a pattern, not a first-class feature |
| **CrewAI** | Role-based task orchestration[^21] | None | ✅ pip install | Designed for task decomposition, not adversarial deliberation |
| **LangGraph** | Graph-based agent workflows; multi-agent RAG templates[^22][^23] | None | ✅ pip install | Low-level controllable framework; debate requires custom graph construction |
| **MetaGPT / CAMEL / ChatDev** | Software development role-play[^24] | None | ✅ | Role differentiation exists but oriented toward coding tasks, not adversarial reasoning |

### MCP Servers and Claude Code Skills

**Clear Thought MCP Server** (waldzellai) is the most feature-rich packaged deliberation toolset found. It provides tools for: collaborative reasoning (multi-persona problem-solving with structured debate), structured argumentation (formal dialectical reasoning with thesis-antithesis-synthesis), **metacognitive monitoring** (knowledge boundary assessment, claim certainty evaluation, reasoning bias detection, confidence calibration), and decision frameworks. It is available as an MCP server installable for Claude Code and other MCP-compatible hosts.[^25][^26][^27]

**Structured Thinking MCP Server** empowers LLMs to explore idea spaces via mind maps with metacognitive self-reflection through thought quality scoring and stage-based feedback, managing short-term and long-term memory of thoughts.[^28]

**Manage Board (MCP Market)** implements a "Board of Directors" metaphor within Claude Code — curating virtual expert advisors with distinct persona profiles. While it creates multi-persona deliberation, the depth of its adversarial structure and confidence tracking is limited compared to Cyberneutics.[^29]

**MOOLLM** (SimHacker) is the closest packaged system to Cyberneutics' architecture. It includes an **adversarial-committee** skill, a **debate** skill, and runs multiple agents within a single LLM call for zero-latency interaction. MOOLLM's architectural philosophy — "the LLM is eval(), skills are programs" — means all agents share context and can interrupt each other in real time. It has 117+ skills organized in a trust-tiered ecosystem. The adversarial-committee skill is documented as providing "the shape of the opinion space". However, MOOLLM's metacognition layer appears to be via the skill ecosystem's general introspection tools rather than a formal calibration register.[^30][^31][^32][^33]

### Prompt Libraries and Templates

The **AI Debate Panel tutorial** (Sep 2025) provides a complete AutoGen-based implementation of agents that argue and produce a final conclusion. The **Multi-LLM Debate framework** on OpenReview formalizes debate procedures with interventions for tyranny-of-the-majority and shared misconceptions, including diversity pruning.[^34][^35]

**Claude-Flow** has been used for adversarial planning with specialized agent swarms (VP of Product, VP of Engineering, growth engineer, design director) that each voice concerns independently before convergence — closely paralleling Cyberneutics' persona differentiation.[^36]

***

## Metacognition in LLM Systems

### Intra-Run Confidence

**ReConcile** represents the most established approach to intra-debate confidence: agents express uncertainty scores that are shared in discussion prompts and used for weighted voting. **ConfMAD** extends this by integrating confidence expression throughout all debate phases, not just at resolution.[^10][^15]

The Clear Thought MCP Server's metacognitive monitoring tool provides knowledge boundary assessment, claim certainty evaluation, and confidence calibration as callable tools. The **Rewire.it guide to building metacognitive AI agents** provides a complete implementation including `calibrate_from_history()` using isotonic regression on historical confidence/accuracy pairs — the closest published code to Cyberneutics' calibration register pattern.[^37][^27]

### Cross-Run Calibration and Persistent Tracking

This is the thinnest area in the literature and where Cyberneutics is most novel. Three systems approach it:

**DS-MCM (Deep Search with Meta-Cognitive Monitoring, Jan 2026)** is the most sophisticated academic treatment. Its Slow Experience-Driven Monitor constructs a persistent **metacognitive experience memory** from historical agent trajectories, organized into success (M⁺) and failure (M⁻) pools. During deployment, it retrieves relevant experiences via embedding similarity and uses them to condition corrective interventions. Its optional **online memory update and consolidation** mechanism incrementally adds new experiences during execution, with deduplication to prevent memory growth. While targeting deep search agents rather than committee deliberation, the architectural pattern — accumulate calibrated experience, retrieve relevant precedents, condition current decisions — directly parallels Cyberneutics' calibration register.[^38]

**DRF (Dynamic Reputation Filtering, Sep 2025)** tracks agent reputation dynamically across tasks using a rating network and reputation iteration mechanism. Agents that perform well see reputation increase (Equation 7 in the paper); agents that perform poorly see reputation decay (Equation 8). A UCB-based selection strategy then prioritizes high-reputation, low-cost agents for subsequent tasks. DRF demonstrated consistent improvements over AutoGen, DyLAN, and Reflexion on code generation and logical reasoning benchmarks. This is the closest system to Cyberneutics' cross-run persona weighting — but DRF tracks task accuracy, not calibration of confidence per se.[^39]

**Empirica** is a community-built epistemic tracking system for Claude Code that records knowledge states, uncertainties, and insights across sessions, anchored to git commits. It implements systematic overconfidence detection across 500+ sessions, applies bias correction (+/- adjustments to knowledge/uncertainty scores), and uses a "readiness gate" requiring knowledge ≥ 0.70 and uncertainty ≤ 0.35 before proceeding. Postflight deltas compare claimed knowledge against actual code changes. This is the **most direct parallel** to Cyberneutics' calibration register in a deployed (non-academic) system.[^40]

### LLM Calibration Literature

**Kadavath et al. (2022)** established that "Language Models (Mostly) Know What They Know" — larger models are well-calibrated on diverse multiple choice and true/false questions when provided in the right format. This foundational work is cited extensively in the calibration literature.[^41][^42][^43]

A PNAS Nexus paper (Apr 2025) argues that AI systems should report **metacognitive sensitivity** — the correspondence between confidence judgments and accuracy on specific tasks — and that this will be key to calibrating human trust in AI. The paper explicitly proposes a framework with four levels: type 1 decisions, type 2 confidence judgments, **type 3 long-run correspondence tracking** (analogous to Cyberneutics' register), and type 4 introspection about the decision process.[^44]

**MARS (Metacognitive Agent with Reflective Self-improvement, Jan 2026)** introduces a triple-pathway reflection mechanism extracting normative principles for error avoidance, procedural strategies for success replication, and a unified synthesis — inspired by human metacognitive learning theory. It outperforms recursive self-improvement frameworks while requiring fewer iterations.[^45]

### Signal Detection Theory and meta-d'/d'

Peters, Charles & Maniscalco (2024) provide the definitive treatment of optimal metacognitive decision strategies in Signal Detection Theory, deriving formulae for optimal type 2 (confidence) criteria under four objectives: maximizing type 2 accuracy, maximizing type 2 reward, calibrating confidence to accuracy, and maximizing the difference between type 2 hit rate and false alarm rate. **No published work was found applying meta-d'/d' directly to LLM output confidence.** This represents a clear research gap that Cyberneutics could pioneer — computing metacognitive efficiency as the ratio of meta-d' to d' for each persona's confidence reports vs. their actual accuracy.[^46][^47]

***

## Adjacent Patterns

### Prompt-Level Mixture of Experts

**Symbolic-MoE** (Chen et al., Mar 2025) implements a gradient-free, text-based Mixture-of-Experts framework that dynamically selects expert LLMs per-instance based on skill profiles, matching 70B model performance with pools of smaller models. **Dynamic Ensemble Reasoning (DER)** models ensemble reasoning as a Markov Decision Process, training an agent to select optimal answering routes.[^48][^49]

### Self-Consistency and Majority Voting

**Self-Consistency** (Wang et al., 2023) — sampling multiple reasoning paths and selecting answers via majority voting — remains the simplest baseline for multi-agent aggregation. **Mirror-Consistency** (2024) extends this by reflecting on inconsistent minority views rather than discarding them, using conditional resampling to improve both accuracy and calibration. **Ranked Voting-based Self-Consistency** (ACL 2025) generates ranked answers per reasoning path and conducts ranked voting.[^50][^51][^45]

### Reflection and Self-Critique

**Reflexion** (Shinn et al., 2023) stores linguistic reflections in episodic memory to guide subsequent attempts — single-agent metacognition without confidence scoring. **Self-Refine** (Madaan et al., 2023) iteratively improves responses through self-feedback. The **Generative Self-Refinement** paradigm fuses multiple candidate solutions through critique and first-principles reasoning rather than just selecting the best one.[^52][^45][^39]

### Internalized Deliberation

OpenAI's "reasoning tokens" and Anthropic's "extended thinking" represent **internalized** deliberation — the model argues with itself within a single forward pass. **Latent Debate** (Dec 2025) provides a surrogate framework for interpreting LLM internal reasoning as an implicit debate process.[^53]

***

## Evaluation and Effectiveness

### Does Multi-Agent Deliberation Outperform Single-Agent Prompting?

The evidence is mixed and condition-dependent:

| Condition | Evidence |
|-----------|----------|
| Homogeneous agents, reasoning tasks | Generally improves over single-agent[^6][^12] |
| Heterogeneous agents (different models) | ReConcile shows 7.7% improvement; greater potential[^10][^19] |
| Tasks with correlated biases | Can **harm** performance due to confabulation consensus[^20][^17] |
| With sycophancy controls | 2-3 round cap with diminishing-returns detection is optimal[^19] |
| With evidence-based auditing | AgentAuditor: +3-5% over majority voting consistently[^17] |
| With confidence weighting | ConfMAD and ReConcile show improvements over unweighted debate[^15][^10] |

### Failure Modes

- **Sycophancy / Groupthink**: Agents converge on wrong answers through social pressure[^54][^19]
- **Confabulation Consensus**: Correlated biases produce high-confidence wrong answers[^17]
- **Debate Collapse**: Agents become self-contradictory or low-confidence under pressure[^18]
- **Cost**: Multi-agent debate is inherently more expensive; iMAD addresses this by selectively triggering debate[^16]
- **Agent Collusion and Mode Collapse**: Coordination mechanisms designed for collaboration can foster echo chambers[^54]

### Quality Measurement

Most frameworks use task accuracy on reasoning benchmarks (GSM8K, MATH, MMLU, AMC). ReConcile and some others use human evaluation. No framework found uses the kind of structured rubric + independent evaluation + remediation cycle that Cyberneutics implements.[^17]

***

## Cyberneutics Positioning Analysis

### What Cyberneutics Does That No One Else Does (Combined)

| Feature | Cyberneutics | Closest Parallel | Gap |
|---------|-------------|------------------|-----|
| Named personas with distinct cognitive propensities | ✅ 5 personas | MOOLLM adversarial-committee[^31]; DiMo 4 agents[^55] | Others lack formal cognitive-propensity differentiation |
| Robert's Rules procedural framework | ✅ | None found | Unique formalization |
| Independent evaluation + remediation post-resolution | ✅ | AgentAuditor's post-hoc auditing[^17] | AgentAuditor replaces voting, doesn't remediate |
| Numeric confidence (1–4) at resolution per persona | ✅ | ReConcile confidence-weighted voting[^10]; ConfMAD[^15] | These are per-round, not structurally tied to resolution votes |
| Cross-run calibration register | ✅ | DS-MCM experience memory[^38]; DRF reputation[^39]; Empirica[^40] | DS-MCM tracks cognitive patterns, not per-persona calibration; DRF tracks accuracy, not confidence calibration; Empirica is closest but not deliberation-specific |
| With-register mode feeding history back | ✅ | DS-MCM online memory update[^38]; DRF UCB selection[^39] | Neither feeds calibration into persona-weighted synthesis |

### Recommendations for Cyberneutics

1. **Adopt meta-d'/d' from SDT**: No one has applied metacognitive efficiency metrics from signal detection theory to LLM deliberation. Peters et al. (2024) provide the mathematical framework. Computing meta-d'/d' per persona would yield a principled metacognitive efficiency score.[^47]

2. **Implement sycophancy controls**: The sycophancy literature strongly recommends heterogeneous agents and 2–3 round caps. If Cyberneutics uses a single model with different persona prompts, it is especially vulnerable to correlated biases.[^19]

3. **Consider AgentAuditor-style evidence auditing**: Rather than majority voting on resolutions, an evidence-based audit of the actual reasoning divergences could catch confabulation consensus.[^17]

4. **Benchmark against self-consistency**: Wang et al.'s self-consistency remains a strong baseline. Cyberneutics should demonstrate improvement over SC-k (k samples with majority voting) to validate the added complexity.

5. **Publish the calibration register analysis**: The cross-run calibration data (was high confidence correlated with being on the winning side?) is the most novel contribution. Publishing calibration curves per persona — and demonstrating that the with-register mode improves downstream decisions — would be a first-of-its-kind result in the literature.

---

## References

1. [Scalable AI Safety via Doubly-Efficient Debate - OpenReview](https://openreview.net/forum?id=MTvYflAH62) - Review: Summary The paper studies and improves the debate framework introduced by Irving et al. in 2...

2. [[2311.14125] Scalable AI Safety via Doubly-Efficient Debate](https://arxiv.org/abs/2311.14125) - Irving et al. [2018] proposed a debate method in this direction with the goal of pitting the power o...

3. [Scalabale AI Safety via Doubly-Efficient Debate - OpenReview](https://openreview.net/forum?id=49ZYkhEGmv) - Summary: This paper studies interaction protocol for the debate framework introduced by Irving et al...

4. [[PDF] A Safety Case for a Deployed LLM: Corrigibility as a Singular Target ...](https://openreview.net/pdf?id=mhEnJa9pNk) - This paper uses the AI Debate framework as a concrete, testable, yet provisional mechanism for insti...

5. [An alignment safety case sketch based on debate](https://www.alignmentforum.org/posts/iELyAqizJkizBQbfr/an-alignment-safety-case-sketch-based-on-debate) - AI safety via debate is a promising method for solving part of the alignment problem for ASI (artifi...

6. [[PDF] Encouraging Divergent Thinking in Large Language Models through ...](https://aclanthology.org/2024.emnlp-main.992.pdf) - Con- current with our work, a few studies (Xiong et al.,. 2023; Du et al., 2023) also explore the mu...

7. [Skytliang/Multi-Agents-Debate: MAD: The first work to ... - GitHub](https://github.com/Skytliang/Multi-Agents-Debate) - This work aims to explore the debating capability of LLMs by proposing the MAD framework, which stan...

8. [Encouraging Divergent Thinking in Large Language Models through ...](https://arxiv.org/html/2305.19118v4) - We propose a Multi-Agent Debate (MAD) framework, in which multiple agents express their arguments in...

9. [ReConcile: Round-Table Conference Improves Reasoning via ...](https://arxiv.org/html/2309.13007v3) - ReConcile enhances collaborative reasoning between LLM agents via multiple rounds of discussion, lea...

10. [[PDF] ROUND-TABLE CONFERENCE IMPROVES REASONING VIA ...](https://openreview.net/pdf?id=Yol6nUVIJD) - Thus, we propose RECONCILE, a novel method of round-table conference for improved consensus among di...

11. [ReConcile: Consensus among Diverse LLMs](https://arxiv.org/abs/2309.13007) - ReConcile enhances collaborative reasoning between LLM agents via multiple rounds of discussion, lea...

12. [Tool-MAD: A Multi-Agent Debate Framework for Fact Verification ...](https://arxiv.org/html/2601.04742v1) - Multi-Agent Debate (MAD) systems aim to improve answer accuracy by enabling multiple LLM agents to e...

13. [GroupDebate: Enhancing the Efficiency of Multi-Agent Debate Using ...](https://arxiv.org/html/2409.14051v2) - ConfMAD lin2025enhancingmultiagentdebateperformance integrates confidence expression throughout the ...

14. [[PDF] Breaking Mental Set to Improve Reasoning through Diverse Multi ...](https://iclr.cc/media/iclr-2025/Slides/28079.pdf) - LLMs often suffer from mistakes when reasoning. • We can use stronger model to provide feedback. • O...

15. [Enhancing Multi-Agent Debate System Performance via Confidence ...](https://chatpaper.com/paper/189275) - The paper presents ConfMAD, a framework that enhances Multi-Agent Debate systems by incorporating ex...

16. [[PDF] Intelligent Multi-Agent Debate for Efficient and Accurate LLM Inference](https://arxiv.org/pdf/2511.11306.pdf) - To further enhance reasoning and accuracy on complex tasks, Multi-Agent Debate (MAD) has emerged as ...

17. [AI agents research, distilled weekly | Yutori](https://scouts.yutori.com/9716b0a9-bd43-4492-9460-03a8c84eef36) - Arxiv. AgentAuditor replaces majority vote with reasoning-tree audits; ACPO favors evidence-backed m...

18. [[PDF] Mitigating Debate Collapse in Multi-Agent Systems via Uncertainty ...](https://www.arxiv.org/pdf/2602.07186.pdf) - Multi-agent debate (MAD) systems improve LLM reasoning through iterative deliberation, but re- main ...

19. [How Sycophancy Shapes Multi-Agent Debate](https://arxiv.org/html/2509.23055v1) - We implement all the frameworks by AutoGen (Wu et al., 2024) , an efficient and flexible platform fo...

20. [[PDF] Understanding Failure Modes in Multi-Agent Debate](https://arxiv.org/pdf/2509.05396.pdf) - Various forms of multi-agent debate have been shown to improve performance on multiple arithmetic an...

21. [AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and ...](https://arxiv.org/html/2505.10468v1) - Architectures such as CrewAI demonstrate how these agentic frameworks can orchestrate decision-makin...

22. [LangGraph Template: Multi-Agent RAG Research - YouTube](https://www.youtube.com/watch?v=JLDLANs_m_w) - This video walks through building a RAG research agent with LangGraph and LangGraph Studio. It uses ...

23. [Top 5 LangGraph Agents in Production 2024 - LangChain Blog](https://blog.langchain.com/top-5-langgraph-agents-in-production-2024/) - 2024 was the year that agents started to work in production. Not the wide-ranging, fully autonomous ...

24. [[PDF] Agentic Artificial Intelligence (AI): Architectures, Taxonomies, and ...](https://arxiv.org/pdf/2601.12560.pdf) - This paper investigates the architectures that let Large Language Models. (LLMs) run complex workflo...

25. [r/ClaudeAI on Reddit: (devs) Enhancement MCP Server Repo](https://www.reddit.com/r/ClaudeAI/comments/1kctbas/devs_enhancement_mcp_server_repo_servers_like/) - A repo full of servers that operate using the same paradigm as memory and sequentialthinking. most M...

26. [Cognitive Enhancement MCP Servers - LobeHub](https://lobehub.com/mcp/waldzellai-model-enhancement-servers) - Dialectical Reasoning and Argument Analysis: Create, critique, and synthesize complex arguments usin...

27. [Clear Thought Server MCP Server | Price Per Token](https://pricepertoken.com/mcp-servers/clear-thought-server) - A detailed tool for systematic dialectical reasoning and argument analysis. This tool helps analyze ...

28. [Structured Thinking: LLM Mind Mapping with Metacognition](https://mcpmarket.com/server/structured-thinking) - About. This TypeScript server, based on the Model Context Protocol (MCP), empowers LLMs to explore i...

29. [Manage Board | Claude Code Skill for AI Personas - MCP Market](https://mcpmarket.com/tools/skills/manage-board-of-directors) - The manage-board skill allows you to curate a virtual 'Board of Directors' within Claude Code by add...

30. [Gas Town's agent patterns, design bottlenecks, and vibecoding at ...](https://news.ycombinator.com/item?id=46734302) - I predicted someone would lash the Claude Code camels together into chariots, and that is exactly wh...

31. [Astrological CPU Scheduler - Hacker News](https://news.ycombinator.com/item?id=46805763) - MOOLLM's response: simulate an adversarial committee within the same call. ... https://github.com/Si...

32. [MOOLLM-FOR-HACKERS.md - GitHub](https://github.com/SimHacker/moollm/blob/main/designs/MOOLLM-FOR-HACKERS.md) - An adversarial committee gives you the shape of the opinion space. Stop 2: The Semantic Image Pyrami...

33. [moollm/designs/SKILL-ECOSYSTEM.md at main - GitHub](https://github.com/SimHacker/moollm/blob/main/designs/SKILL-ECOSYSTEM.md) - Skills are programs. The ecosystem is the package registry. The Vision. npm for skills. Docker Hub f...

34. [Building an AI Debate Panel: Agents that Argue and Give a Final ...](https://pub.towardsai.net/building-an-ai-debate-panel-agents-that-argue-and-give-a-final-conclusion-fb3fb3153f0c) - A single LLM prompt or a plain ReAct (reasoning & take actions) agent often gives you a plausible an...

35. [[PDF] Multi-LLM Debate: Framework, Principals, and Interventions](https://openreview.net/pdf?id=sy7eSEXdPC) - Our work is closely related to multi-agent debate, which focuses on iterative collaboration between ...

36. [Adversarial Planning with Claude Code : r/ClaudeAI - Reddit](https://www.reddit.com/r/ClaudeAI/comments/1pwfrxs/adversarial_planning_with_claude_code/) - I'm using Claude-Flow to run the swarm. > create a specialized swarm with the following roles. Their...

37. [Building Metacognitive AI Agents: A Complete Guide from Theory to ...](https://rewire.it/blog/building-metacognitive-ai-agents-complete-guide/) - The definitive guide to building AI agents that monitor their own thinking through dual-loop archite...

38. [Deep Search with Hierarchical Meta-Cognitive Monitoring ...](https://arxiv.org/html/2601.23188v1) - In this work, we propose Deep Search with Meta-Cognitive Monitoring (DS-MCM), a deep search framewor...

39. [DRF: LLM-AGENT Dynamic Reputation Filtering Framework - arXiv](https://arxiv.org/html/2509.05764v1) - Experiments show that DRF significantly improves task completion quality and collaboration efficienc...

40. [I got tired of Claude forgetting what it learned, so I built something to ...](https://www.reddit.com/r/ClaudeAI/comments/1q36l43/i_got_tired_of_claude_forgetting_what_it_learned/) - Postflight delta is compared against what code actually changed. Empirical validation - 500+ session...

41. [Your Pre-trained LLM is Secretly an Unsupervised Confidence ...](https://openreview.net/forum?id=I4PJYZvfW5) - ... Calibration of Large Language Models and Alignment." EMNLP (2023). [4] Kadavath, Saurav, et al. ...

42. [From small to large language models: How much confidence can we ...](https://openreview.net/forum?id=B9i2B0IjRT) - Normally, calibration of UQ refers to expected calibration ... [1] Kadavath, Saurav, et al. "Languag...

43. [Figure 1 from Language Models (Mostly) Know What They Know](https://www.semanticscholar.org/paper/Language-Models-(Mostly)-Know-What-They-Know-Kadavath-Conerly/142ebbf4760145f591166bde2564ac70c001e927/figure/0) - It is shown that larger models are well-calibrated on diverse multiple choice and true/false questio...

44. [The key to calibrating trust and optimal decision making with AI](https://academic.oup.com/pnasnexus/article/4/5/pgaf133/8118889) - In this piece, we argue that measures of metacognitive sensitivity provided by AI systems will likel...

45. [Learn Like Humans: Use Meta-cognitive Reflection for Efficient Self ...](https://arxiv.org/html/2601.11974v1) - ... Self-Consistency Wang et al. (2023) which samples multiple reasoning paths and selects answers v...

46. [Optimal metacognitive decision strategies in Signal Detection Theory](https://jov.arvojournals.org/article.aspx?articleid=2791939) - In this project, we further advance the application of SDT to the study of metacognition by providin...

47. [Optimal metacognitive decision strategies in signal detection theory](https://pmc.ncbi.nlm.nih.gov/articles/PMC12092500/) - Signal detection theory (SDT) has long provided the field of psychology with a simple but powerful m...

48. [Symbolic Mixture-of-Experts: Adaptive Skill-based Routing for ...](https://arxiv.org/html/2503.05641v1) - We propose a skill-based recruiting strategy that dynamically selects the most relevant set of exper...

49. [Efficient Dynamic Ensembling for Multiple LLM Experts - arXiv.org](https://arxiv.org/html/2412.07448v2) - We propose Dynamic Ensemble Reasoning (DER) for the LLM ensemble, modeling it as a Markov Decision P...

50. [Mirror-Consistency: Harnessing Inconsistency in Majority Voting](https://arxiv.org/html/2410.10857v1) - We compare our method with Standard CoT Prompt (Kojima et al., 2022) and Self-Consistency (Wang et a...

51. [Ranked Voting based Self-Consistency of Large Language Models](https://aclanthology.org/2025.findings-acl.744/) - In this work, we propose to generate ranked answers in each reasoning process and conduct ranked vot...

52. [Self-Refinement in Language Models - Emergent Mind](https://www.emergentmind.com/topics/self-refinement) - Self-refinement is a framework where models generate diverse candidate solutions, critique errors, a...

53. [Papers citing 'ReConcile: Round-Table Conference Improves ...](https://www.researchtrend.ai/papers/2309.13007/cited-by) - Paper list citing the paper 'ReConcile: Round-Table Conference Improves Reasoning via Consensus amon...

54. [TRiSM for Agentic AI: A Review of Trust, Risk, and Security ... - arXiv](https://arxiv.org/html/2506.04133v4) - This review presents a structured analysis of Trust, Risk, and Security Management (TRiSM) in the co...

55. [Unleashing Diverse Thinking Modes in LLMs through Multi-Agent ...](https://arxiv.org/html/2510.16645v1) - This paper introduces the Multi-Agent Collaboration Framework for Diverse Thinking Modes (DiMo), whi...

