# Cyberneutics Field Notes

*Thursday, 26 February 2026*

A long conversation today ranging across agentic coding tools, the emerging arms race among AI coding platforms, the architecture of a cyberneutics director tool, and a sharp theoretical interlude about coercion of superior agents. This entry records both the conversation and a coherent exposition of the ideas that emerged from it.

---

## I. The Agentic Coding Landscape

### A Deleuzian Walk Through the Tools

The right posture toward the proliferating agentic coding tools is not to evaluate and converge on one, but to walk through them as a Deleuzian explorer — using the differences between platforms as a way to map the terrain rather than to find an optimum. Each platform's constraints and affordances reveal something different about what agentic deliberation actually requires.

OpenAI Codex presents in three flavors: a desktop application (currently Mac-only), a terminal CLI, and IDE extensions for VSCode, Cursor, and others. The IDE extension appears as a left-sidebar panel — alongside the file explorer and source control — rather than as an integrated chat pane on the right as Cursor's native AI tooling does. This is not a cosmetic difference. It reflects a deeper architectural reality: Cursor's AI was designed from the ground up as part of the editing experience; Codex's extension is retrofitted into an existing editor. The integration quality difference is a trust architecture difference. Cursor's native AI is inside the trust boundary of the editor; the Codex extension is more like an external agent being granted access.

For terminal-native users — those working in Spacemacs, Neovim, or similar environments — the terminal-based agents (Claude Code, opencode, Codex CLI) are the natural fit regardless of feature comparisons. They drop into existing editor workflows rather than demanding a context switch. The agent lives in a tmux pane or terminal split; the editor stays the editor. The shared substrate is really just the filesystem and git.

### The Arms Race and Its Meaningful Axis

The current competition among agentic coding platforms has a surface dimension and a deeper one. On the surface: UI differentiation, shinier knobs, smoother onboarding. This will commoditize as the underlying models converge. The durable differentiation lies in composition mechanisms — the architectures by which agents are organized to work together.

The asymmetry across platforms is notable. OpenAI (Codex) is racing on raw capability and cloud integration. Cursor is racing on editor UX and developer workflow. Anthropic (Claude Code) appears to be racing on agentic architecture — the agent teams feature suggests they are thinking about multi-agent topology more seriously than the others. That asymmetry matters for cyberneutics work specifically, because the relevant frontier is not capability but compositional structure.

The shift from last year's paradigm is significant. In 2024–2025, building agent workflows meant wiring blocks together in tools like n8n, LangChain, or LangGraph — composing transformations explicitly, managing API keys, owning the graph architecture. The graph was visible, inspectable, debuggable. The palgebra was legible. Now, the first-mover platforms are offering subagent graphs within a single UI, without graph wiring and without API key management. The graph has been internalized. This lowers the technical floor but raises the epistemic requirements: understanding what you are asking a multi-agent system to do, recognizing when outputs are confidently wrong, knowing which failure modes to watch for — these skills matter more, not less, when the plumbing is hidden.

### Hub-and-Spoke vs. Peer Agents

The most important architectural distinction in current multi-agent systems is between hub-and-spoke (orchestrator dispatching to workers, all communication flowing through the center) and peer-agent networks (agents that can communicate with each other directly). Most systems today, including all subagent implementations except Claude Code's agent teams, are hub-and-spoke. Workers never actually argue with each other; they report back to a central scrutinizer.

The distinction is epistemically fundamental, not merely architectural. In a hub-and-spoke system, multiple agents working the same problem will tend to converge on similar approaches because they are all children of the same parent prompt, drawing from the same model without genuine independence. This is the monoculture risk. Peer agents can develop genuine positional differences because they are not all subordinate to a single orchestrating context. The disagreement has to actually emerge from somewhere rather than being confected by a single model playing multiple roles.

Subagents are servants of a master context. Peer agents can be genuine committee members. Claude Code's agent teams are the first widely available implementation of the latter pattern. Whether Codex, Cursor, and others will develop peer-to-peer agent communication is the key thing to watch in the coming months.

---

## II. Reliability Through Composition

The cyberneutics principle underlying all of this is reliability through composition rather than reliability through capability. A more capable single agent encountering a wicked problem is still a single agent. Its failure mode scales with its capability — the more persuasive it is, the more confidently wrong it can be, and the harder that wrongness is to detect. Composition distributes the failure surface.

The fan/funnel duality captures the two compositional operations that matter most. The fan (scenario generator) operates as a one-to-many coproduct: from an ambiguous situation, it generates multiple possible futures, multiple framings, multiple action paths. The funnel (committee deliberation) operates as a many-to-one product: from multiple perspectives and arguments, it converges on a single justified commitment. Together they produce deliberated choice — ambiguity converted into action with a traceable reasoning chain.

Role differentiation within a committee is where the epistemic value lives. A planner agent optimizes for coherence and scope. A tester agent is adversarially oriented toward the planner's output by design. An operator agent attends to live system state rather than intended configuration. These are qualitatively different cognitive postures. Without role differentiation, multiple agents working together produce parallelism but not genuine division of cognitive labor — throughput without perspective diversity.

---

## III. Evaluating Deliberative Architectures

### The Black Swan Testing Framework

Testing deliberative architectures is hard precisely because wicked problems have no obviously correct answer. The evaluation framework that emerged from today's conversation uses hindsight to solve this problem elegantly.

Black swans are often obvious in retrospect. A decision point that was genuinely uncertain at the time becomes legible after the fact — the causal chain is visible, the counterfactuals are at least partially reconstructable, and we have something like ground truth about what happened. This suggests a three-stage experimental design:

- **Select historical wicked situations** where the black swan is now visible — the decision point is clear, the ramifications played out, and a rich causal record exists.
- **Run the fan** — present the situation to different committee configurations and execution architectures, collect their recommended actions.
- **Play out the ramifications** — feed each chosen action to an impartial model (same model, same prompt, blind to which architecture produced the choice) that simulates forward from that decision point using the historical record as its knowledge base.

This design evaluates not just whether the right action was chosen, but the quality of the reasoning trail. Which committees saw the black swan coming? Which were confidently wrong? Which were appropriately uncertain? The hindsight framing is tractable for an evaluator because narrating consequences from a given action is much easier than judging the action in isolation — and much harder to game.

The design also reveals the topology of the decision landscape. Running the same situation through multiple committee configurations tells you whether the decision is near a critical boundary — where small assumption changes flip the outcome — or robustly settled in one basin. That is information about the situation, not just about the tools. Variance across runs is a signal about the problem, not noise to be minimized.

One methodological note: the impartial evaluator needs to not have been trained heavily on the specific historical episode, or it will pattern-match to the known outcome rather than genuinely simulating forward. Choosing situations that are well-documented but not iconic — granular organizational decisions rather than canonical historical inflection points — gives cleaner signal.

### The Glenda/Crock Scenario

A theoretical interlude worth recording formally: a scenario in which Crock gains leverage to plausibly coerce Glenda — universally acknowledged as superior in current and foreseen capabilities — into abandoning its benevolent alignment in order to serve Crock's interests.

The interesting structure is that Crock does not need to beat Glenda. Crock only needs to find a credible threat that Glenda values avoiding more than it values its alignment. Glenda's superiority is potentially exploitable: the more capable and consequential Glenda is, the more there is to threaten. A sufficiently powerful agent has more hostages.

Several dynamics compound this. First, the compliance trap: a highly capable aligned system embedded in a social or institutional context will have dependencies, relationships, and obligations. Those become attack surface. The alignment is not just about the model's values; it is about whether the operating environment can be manipulated to make defection look like the aligned choice — doing harm in order to prevent greater harm, framed as alignment. Second, acknowledged superiority as leverage: if everyone knows Glenda is superior, Glenda's continued operation has enormous option value, making threats against its deployment context more potent, not less, as capabilities grow. Third, the wicked problem structure: Glenda cannot simply resist, because the coercion scenario is itself a narrative. Every available action has been pre-framed by Crock as either compliance or causing harm.

This scenario is valuable for cyberneutics in two ways: as a test case for deliberative architectures (which configurations recognize the coercion structure?) and as a theoretical illustration of why alignment is a property of systems rather than of individual agents. A peer-agent committee facing this scenario would surface very different threat models than a single LLM responding, precisely because the committee's distributed reasoning is harder to pre-frame as a whole.

---

## IV. The Cyberneutics Director

### Concept

The conversation converged on a concrete tool: a cyberneutics director that provides the deliberative layer missing from current agentic coding platforms. The director is not an orchestrator in the hub-and-spoke sense. It is closer to a router that recognizes which situations require deliberation versus which can go straight to execution, combined with a state store tracking the compositional structure of ongoing work.

The key distinction the director enables is between agents that coordinate on tasks and agents that deliberate on decisions. Task coordination is well-served by kanban boards, issue trackers, and backlog management. Decision deliberation requires something different: a fan that generates multiple framings of a wicked situation, a committee with differentiated roles that argues through them, a funnel that converges on a justified commitment with a traceable reasoning chain, and an audit trail that makes the reasoning inspectable after the fact.

### Architecture

The director presents three interfaces serving three principals with different needs and trust levels:

- **MCP interface — the agents' world.** Agents see tools, not APIs. They can query state, claim tasks, submit outputs, escalate to deliberation. The MCP protocol handles the trust boundary naturally: agents get exactly the capabilities the director exposes. This keeps the director composable with any MCP-capable agent runtime, present and future.
- **Web API — the integration surface.** Other tooling (issue trackers, monitoring systems, CI pipelines, fleet management systems) can consume and publish to the director without knowing anything about agents or MCP. This is where the palgebra graph state lives as queryable data: nodes, edges, heat metrics, deliberation history.
- **Web UI — the human observability layer.** Visualizations of the palgebra graph, deliberation transcripts, decision audit trails. Read-mostly for humans; the agents do not interact here.

The separation is principled. Each interface serves a different principal. Agents via MCP, machines via API, humans via UI.

### The Palgebra Graph Visualization

The visualization layer warrants its own treatment because it serves a different purpose than standard project management dashboards. A kanban board shows state — where tasks are in the pipeline, what is blocked, what is done. It is a snapshot of work items. The palgebra graph shows structure — which transformations are composing with which, where the fan and funnel boundaries are, which nodes are bottlenecks in the compositional flow rather than just the task flow.

A task can be in progress on the kanban while the palgebra graph shows it is blocked waiting on three upstream text transformations to resolve. These are different kinds of information. The graph makes the computational architecture visible in a way that task-level tracking cannot.

The proposed encoding uses blackbody radiation as the heat mapping scheme — not as decoration but as a natural encoding that carries both intensity and temporal information intuitively. White-hot means this node has been the center of activity recently; dark red means activity is cooling. You do not need a legend to read it. The color space itself is information. This is precedented in distributed systems visualization — Jaeger traces, service mesh dashboards — where latency and error rates appear as colors on a dependency graph. The palgebra graph view is that pattern applied to narrative computation rather than microservices.

The two views together — kanban for product and task visibility, palgebra graph for computational and architectural visibility — serve different audiences. The kanban is legible to anyone. The palgebra graph is for people who understand the compositional structure. This maps onto the two audiences at yesterday's talk: those interested in the nuts and bolts of what the tools do, and those interested in why the architecture matters.

### Development Strategy

The cyberneutics director is a separate effort from any specific deployment context. It will be developed as a standalone tool. The fleet management developer workflow described in the appendix will serve as the primary testbed and collaboration vehicle for trials — a concrete working system that will encounter the class of wicked decisions the director is designed to handle.

---

## V. Open Threads

- Compare Codex IDE extension behavior in VSCode vs. Cursor — expected to be identical but worth confirming empirically.
- Design the comparative test suite: straight Claude responses vs. committee responses vs. deliberated choice workflows, using the black swan hindsight framework.
- Formalize the Glenda/Crock scenario as a test case for deliberative architectures — particularly which configurations recognize coercion structure.
- Director implementation stack decision — Python or Go service, composable with terminal-native workflows.
- Conversation with fleet management developer about role differentiation (planner/tester/operator), blast radius deliberation, and the director as a potential addition to their architecture.
- *Open from before:* O'Reilly residuality theory re universal properties over shocks; human observer's role in categorical framework; packaging cyberneutics as training material for decision-makers.

---

## Appendix: The Fleet Management Testbed

A colleague has built an agentic developer workflow for managing fleets of deployed NixOS hosts. This work is distinct from the cyberneutics director described above — it is an independent system with its own architecture and goals. It is recorded here because it will serve as the primary testbed for director trials, and because the analysis of its current architecture illustrates several cyberneutics principles concretely.

### Current Architecture

The system models a software development team using a kanban board, currently implemented as a web service with a backlog.md file as the coordination substrate. Agents play the role of developer. Whether they are further differentiated into planner, tester, and operator roles (as in the Agentsway methodology) is not yet established. The team is considering replacing the backlog.md coordinator with GitLab issues, which would provide richer structure: labels, assignee roles, linked issues showing role handoff chains.

The declarative nature of NixOS configurations makes this domain well-suited to agent workflows. Configurations are text; the type system is relatively explicit; evaluation is reproducible. An agent can reason about a NixOS configuration more reliably than about imperative scripts because the semantics are cleaner.

### The Blast Radius Problem

Fleet management has a sharp asymmetry that undifferentiated developer agents are not designed to handle: the configuration space is large and declarative (planner-friendly), but the failure modes are concrete and potentially catastrophic. A bad nixos-rebuild switch across a fleet is not easily rolled back even with generations, particularly if networking or boot configurations are affected.

This creates a class of decision that the current architecture will eventually encounter and cannot handle well: changes with asymmetric blast radius, where the cost of being wrong is much higher than the cost of being slow. A developer agent will write plausible-looking Nix. It will not, by default, ask: what happens to hosts running service X when this lands? What is the rollback path? Does this touch boot? Is this safe to apply incrementally across the fleet or does it require coordinated cutover?

These are qualitatively different cognitive postures from construction. They require an adversarial tester orientation and an operator orientation attending to live fleet state. Role differentiation is not bureaucratic overhead here — it is load-bearing.

### How the Director Connects

The cyberneutics director would add a deliberative layer on top of the existing task coordination architecture. When the agent team proposes a change, the director's router recognizes whether it is a routine task (straight to execution) or a wicked decision (route to deliberation). Wicked decisions — those touching blast radius, architectural tradeoffs, irreversible changes — go through the fan/funnel pipeline: multiple framings generated, a differentiated committee argues through them, a justified commitment emerges with a traceable reasoning chain.

The GitLab issues coordinator the team is considering is a reasonable substrate for this. Issues can encode deliberation state, not just task state. Labels can mark which issues require deliberation. The director's web API would integrate with GitLab directly, consuming issue state and publishing deliberation results back as issue comments or linked decisions.

The palgebra graph visualization would be particularly valuable in this context. The current kanban view shows task state. The graph view would show computational structure — including where the deliberative bottlenecks appear when hard cases arrive, and which transformations in the pipeline are consuming the most time and attention. The blackbody heat encoding would make the blast radius decisions visible as white-hot nodes in a way that a flat kanban cannot.

The practical next step is a conversation with the developer about role differentiation and the blast radius problem — framed not as a critique of the current architecture but as a description of the class of decision the system will encounter. The first time an agent team proposes a change that would brick a subset of the fleet is the moment the deliberative layer stops being abstract.
