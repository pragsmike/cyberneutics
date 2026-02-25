# Subagent Personas for Debate: Coordination & Architecture

## The Holy Grail: Native Inter-Agent Communication
Before diving into the history of our experiments, it is crucial to note that **Claude Code does offer an experimental, native inter-agent communication protocol called "Agent Teams."** 

Unlike earlier constraints where subagents could only talk back to a hub, Agent Teams allow instances of Claude Code to communicate directly peer-to-peer (or broadcast to all teammates) using a built-in `sendMessage` tool. The underlying file reads and writes are abstracted away from the LLM, giving the illusion of direct network messaging without forcing the agents to coordinate manual filesystem writes. **If you are building within the Claude Code terminal ecosystem, this is the most attractive and resilient path forward for orchestrating the 5-character committee.**

---

## 1. Existing Research Program: API-Based Multi-Model Committees
The foundation of the current research on multi-agent debate exists in `meta/research-programs/multi-model-committee.md` and `multi-model-committee-reference.md`. 

**The Premise:**
The research correctly identifies the "Single-Model Monoculture Problem." Asking one model (like Claude) to simulate 5 hostile characters (Maya, Frankie, Joe, Vic, Tammy) forces the model to overcome its own training biases (like safety filters or a tendency to hedge). 

**The Approach Found in the Repo:**
To date, the documented approach to solving this has been almost **exclusively API-based**. The `multi-model-committee-reference.md` explicitly specs out writing custom Python scripts that hit multiple vendor endpoints (Anthropic, OpenAI, Meta, Google). 
*   **The Orchestrator:** Described as a Python `SimpleChair` or `SmartChair` class that iterates through characters in a loop, hitting `API.complete()` and building a single, expanding string of context.
*   **The Problem:** This is fully programmatic and decoupled from AI coding agents (like Cowork, Antigravity, or Cline). It relies on fixed API keys and deterministic `for` loops, rather than autonomous agents deciding when to speak.

## 2. The Cowork Plugin Attempt: Forced Hub-and-Spoke
The recent attempt to move this out of Python scripts and into an agent ecosystem lives in the `cowork-plugin/` directory built on 2026-02-24.

**The Strategy:**
The plugin attempted to instantiate Maya, Frankie, Joe, Vic, and Tammy as distinct Claude Code "subagents" (`agents/maya.md`, etc.).

**The Flaw / Finding:**
As documented in the review, this attempt hit an architectural wall: **The agents didn't know how to talk to each other without a human or a hub standing between them.** 
*   Because the subagents were just defined as `.md` system prompts with no orchestration protocol, they acted as isolated oracles.
*   To fix this, the design relied on `agents/committee-orchestrator.md`—a single orchestrator agent that runs Stages 1-5 manually. The orchestrator collects independent viewpoints in Phase 1, summarizes them, and hands them back in Phase 2.
*   **Conclusion:** This is a simulated Hub-and-Spoke model, not a true P2P debate. The agent personas were isolated and could not spontaneously cross-examine each other; they only spoke when spoken to by the Orchestrator.

---

## 3. Alternative Coordination Schemes & Future Directions

If we step away from the Python API orchestration loop, we have three paths to achieve a true, autonomous committee debate depending on the ecosystem you choose:

### Option A: Native Agent Team Protocols (Recommended for Claude Code)
As mentioned above, if operating within Claude Code, enable the experimental **Agent Teams**.
*   **How it works:** Agents are spawned into a shared context. They use the `sendMessage` tool to invoke specific personas (e.g., "Ask Vic to evaluate the evidence Frankie just provided"). 
*   **Why it's good:** No custom backend, no filesystem hacking. The agent platform handles the routing, token limits, and context injection invisibly.

### Option B: The File-System "Blackboard" Utility
If you are using agents that do not have native P2P protocols (like raw open-source instances, or agents relying strictly on CLI tools), you can use the **Blackboard Pattern**. 
This is widely used in systems like `taskmd` and `tick-md`, where the filesystem *is* the messaging bus.

**How it works:**
1. You create a shared directory structure: `/blackboard/deliberations/topic_01/`.
2. Inside, you create distinct phase folders: `/01_opening_statements/`, `/02_cross_examination/`.
3. You give all 5 agents a polling script or file-watch capability.
4. **Coordination via Atomic Writes:** When Maya wants to speak, she writes a Markdown file `maya.md`. She can use an atomic write command or script (or a Git lock) to ensure she isn't stepping on Joe.
5. **Progression Triggers:** Vic is instructed: *"Do not write your cross-examination until you see 5 markdown files in output directory 01."* 

**The Verdict:** This works reliably for any agent that can read and write files, but is slow and consumes heavy context tokens as agents re-read the directory state.

### Option C: The MCP Server (Model Context Protocol) 
Cursor, Aider, and many open-source ecosystems utilize **A2A (Agent2Agent)** and **MCP**. Rather than hacking the filesystem to pass messages, we build a local MCP server that acts as the debate room.

**How it works:**
1. A local Python/Node server hosts the state of the debate in memory.
2. The server exposes tools: `get_transcript()`, `submit_argument(persona="Maya")`.
3. The agents connect to this MCP server. They never write to `.md` files to speak; they execute tool calls against the server.
4. The MCP server can use real-time resource updates to alert the agents when someone new has spoken.

**The Verdict:** Much faster and cleaner than the File-System Blackboard, but requires standing up the MCP server application as an intermediate step.
