# The Cyberneutics Director: Deliberative Routing Architecture

*Extracted from the 2026-02-26 field notes.*

## Concept
The Cyberneutics Director provides the deliberative layer missing from current agentic coding platforms. It is not an orchestrator in the hub-and-spoke sense; it is a router that recognizes which situations require deliberation versus which can go straight to execution. It maintains a state store tracking the compositional structure of the ongoing work.

### The Problem It Solves
Current agent tools conflate *task coordination* with *decision deliberation*. Task coordination is well-served by standard tracking tools (issue trackers, kanban boards). Decision deliberation requires a specialized computational architecture:
1. **The Fan:** Generating multiple framings of a wicked situation.
2. **The Committee:** Differentiated roles arguing through those framings.
3. **The Funnel:** Converging on a justified commitment with a traceable reasoning chain.
4. **The Audit Trail:** Making the reasoning inspectable after the fact.

## Architecture Guidelines
The director presents three interfaces serving three principals with different needs and trust levels:

- **MCP Interface (Agents' World):** Agents see tools, not APIs. They can query state, claim tasks, submit outputs, and escalate to deliberation. Crucially, keeping this boundary at the MCP protocol level makes the director composable with any future agent runtime.
- **Web API (Integration Surface):** Other tooling (issue trackers, monitoring systems, CI pipelines) can integrate with the director without understanding MCP. This exposes the "palgebra graph state" as queryable data.
- **Web UI (Human Observability):** Visualizations of the palgebra graph, deliberation transcripts, and decision audit trails. Read-mostly for humans; agents do not interact here.

## Next Steps for Taming
- Define an MVP schema for the "deliberation state store."
- Build a prototype MCP server demonstrating how an agent escalates a problem from "task" to "wicked decision."
- Interface with the `palgebra-graph-ui` project to visualize the output.

### The GitHub MCP Prototype
One immediate path to prototyping the Director is to leverage the official **GitHub MCP server**. Instead of building a custom database and state store, we can use GitHub Issues as the coordination layer:
*   **Reading Intents:** A local agent reads open GitHub issues and their labels to determine if an issue is a standard "task" fix or a "wicked problem" requiring deliberation.
*   **Posting Transcripts:** If local agents run a `/committee` debate on an issue, the Director script extracts the consensus and reasoning chain, and uses the GitHub MCP to post it directly as a comment on the Github Issue or Pull Request, satisfying the "Audit Trail" requirement.
*   **Managing Scope:** The Director agent can autonomously split wicked problems into discrete architectural tasks by generating new, linked GitHub Issues based on the committee's findings.
