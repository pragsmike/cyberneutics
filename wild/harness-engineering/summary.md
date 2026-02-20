# Summary: "No Vibes Allowed: Solving Hard Problems in Complex Codebases"

**Presenter:** Dex Horthy, Founder & CEO of [HumanLayer](https://www.humanlayer.dev/)
**Event:** AI Engineer Code Summit, November 2025
**Video:** https://www.youtube.com/watch?v=rmvDxxNubIg

---

## Overview

Horthy opens by citing a large developer survey (100,000 developers across all company sizes, presented
at AI Engineer by "Eigor") showing that AI coding tools — despite their hype — often *decrease* net
productivity when applied to real-world, complex ("brownfield") codebases. The culprit is not the
models themselves but the way engineers use them: intuitively, improvisationally, on "vibes."

The talk lays out a disciplined, engineering-first methodology to fix that.

The core thesis: **AI-assisted coding in complex codebases is a hard engineering problem, not a
magic trick.** It requires rigorous management of context, explicit workflows, and human oversight
at the right chokepoints.

Horthy and a team of three spent eight weeks rewiring everything about how they build software, achieving
2–3x throughput by cracking this context management problem — moving so fast they were forced to change
how they collaborated. The resulting approach went viral on HackerNews in September 2025.

---

## Main Points

### 1. The Problem: Brownfield AI Struggle

- AI tools work well for greenfield tasks (new projects, isolated files — "little Vercel dashboard").
- In large, existing codebases (10-year-old Java monorepos, etc.) they generate "slop" — plausible-looking
  but incorrect or architecturally incoherent code.
- Developers ship more code volume, but much of it is rework of the slop shipped last week.
- The survey of 100,000 developers confirms: AI coding assistance can *reduce* developer throughput
  in complex settings. This matched Horthy's personal experience and conversations with many founders.
- Root cause: the model doesn't have enough coherent context about the system to make good decisions.

---

### 2. The Dumb Zone

One of Horthy's key diagnostic concepts: LLMs have a **"Dumb Zone"** — a performance cliff that
occurs when the context window starts filling up, typically around **40% capacity**.

- As context fills, models begin to forget constraints, make more errors, and produce lower quality output.
- The model is stateless; its behavior is entirely determined by what is currently in the context window.
- A stuffed or poorly organized context window degrades model performance dramatically.
- Engineers often don't realize this is happening — they just see increasingly bad output.
- **MCP warning:** Too many MCPs in your coding agent means you're doing all your work in the Dumb Zone
  because MCPs dump UUIDs and large JSON blobs into context constantly.
- Jeff Huntley (did research on coding agents) independently found: the more you use the context window,
  the worse your outcomes.
- Claude Code has ~168,000 tokens, with some reserved for output and compaction. 40% ≈ ~67,000 tokens
  is the practical smart-zone ceiling.

**Implication:** Context management is not optional ergonomics; it is the core engineering discipline
for working with LLMs.

---

### 3. Context Engineering

Horthy coined the term **"Context Engineering"** (April 2025, in his 12-Factor Agents essay) to
name the practice of deliberately curating and managing what goes into the model's context window.

Context engineering means optimizing the context for:
- **Correctness** — only accurate, relevant information
- **Completeness** — everything the model needs to accomplish the task
- **Size** — staying out of the Dumb Zone
- **Trajectory** — the emotional/correction arc of the conversation matters

> **On Trajectory:** If you've been correcting the agent repeatedly in a context, the LLM literally
> patterns on that: "I did something wrong, the human yelled at me, I did something wrong, the human
> yelled at me." The next most likely token is for it to do something wrong again so you can yell at
> it. The worst thing to have is incorrect info, then missing info, then just too much noise.

The discipline is a progression from prompt engineering: instead of crafting a single prompt, you
design systems that dynamically build the right context over a session.

Inverting the quality hierarchy — **Worst to best context quality:**
1. Incorrect information (worst)
2. Missing information
3. Too much noise
4. Correct, complete, right-sized context (best)

---

### 4. Frequent Intentional Compaction

The practical technique for staying out of the Dumb Zone is **intentional compaction** — regularly
and deliberately summarizing/distilling the current context before it grows too large.

- Rather than letting the context accumulate indefinitely, the engineer (or agent) periodically
  instructs the agent to compress the current context window into a markdown file.
- You can review and tag that file, and when the new agent starts it gets straight to work instead
  of re-doing all the searching and codebase understanding.
- This compact summary becomes the new starting context, shedding noise while preserving intent.
- What goes into compaction: file names and line numbers that matter to the specific problem being solved.
- **The Momento analogy:** Like the amnesiac in the film who has to read his own tattoos to know who
  he is — agents that aren't onboarded will make stuff up. Context = the agent's memory.
- What takes up context space: file lookups, code-flow understanding, file edits, test/build output,
  MCP JSON dumps.

#### Sub-Agents for Context Control

Sub-agents are a powerful mechanism for compaction — but only if used correctly:

> **Do NOT use sub-agents to anthropomorphize roles** (front-end sub-agent, backend sub-agent, QA
> sub-agent). That's not what they're for.

Sub-agents are for **controlling context**. The pattern:
- Steer a sub-agent to go find how something works in a large codebase.
- The sub-agent forks a fresh context window, does all the reading/searching/understanding.
- It returns a single succinct message back to the parent agent: "the file you want is here."
- The parent agent reads just that one file and gets straight to work — never burning context on discovery.

---

### 5. The RPI Framework: Research → Plan → Implement

The operational workflow Horthy advocates is **RPI** — a structured three-phase approach:

```
Research → Plan → Implement
```

> **Note on naming:** Horthy didn't coin "RPI" — the community started calling it that and he went
> with it. He emphasizes the *concepts* matter (compaction, context management, staying in the smart
> zone), not the acronym. He also says RPI won't necessarily be the final set of steps — what's
> important is the discipline underneath.

#### Research Phase
- The agent (or engineer + agent) explores the codebase to build objective understanding.
- Goal: produce a factual, accurate model of what exists — no code changes.
- **"Compressing truth"** — on-demand research launched via sub-agents takes vertical slices through
  the codebase and produces a snapshot of the actually-true, code-verified parts that matter.
- Human reviews the research output before proceeding.
- You can input: a PRD, a bug ticket, or any other intent artifact alongside the research.

#### Plan Phase
- Based on the research, the agent produces a detailed **plan file** — a design document.
- The plan file is itself a form of intentional compaction: **"compression of intent."**
- **Plans must include actual code snippets** of what's going to change (not just descriptions).
  This is what enables the dumbest model to execute reliably.
- **Human review is mandatory here.** This is the critical chokepoint for team mental alignment.
  A bad line of research → wrong direction for the whole thing. A bad line in a plan → could be
  100 bad lines of code.
- The plan must be reviewed and agreed upon before any code is written.
- **Plan length tradeoff:** Reliability goes up as plans get longer; readability goes down. Find
  the sweet spot for your team and codebase.

#### Implement Phase
- The agent implements against the plan, using it as the primary context anchor.
- Continuous intentional compaction is applied during implementation.
- Explicit about how to test things *after every change*.
- If complexity grows, a new research/plan cycle may be triggered for a sub-problem.

#### When NOT to Use Full RPI
RPI isn't always the right tool. Scale the process to the task:
- **Changing a button color?** Just talk directly to the agent.
- **Small feature in one file?** Maybe just a plan, no research.
- **Medium features across multiple repos?** One research + one plan.
- **Hard complex problems?** The full RPI with maximum compaction — this is where the ceiling goes up.

**Why this works:** Each phase produces a durable artifact that can be reviewed by humans, used to
re-anchor context, and shared across team members. It prevents "semantic diffusion" — the gradual
drift of shared understanding about what the code does and why.

---

### 6. Mental Alignment and the "Outsourcing Thinking" Problem

A second-order danger Horthy flags: when AI does too much of the work invisibly, teams lose
**mental alignment** — shared understanding of what the code does and why.

- When engineers accept AI-generated code without understanding it, they accumulate invisible technical debt.
- This is "outsourcing thinking," not just outsourcing labor.
- **AI cannot replace thinking. It can only amplify the thinking you have done — or the lack of it.**
- The plan review step in RPI is specifically designed to force explicit alignment before implementation.
- The plan file becomes a shared artifact that the whole team can reason about.
- **Mitchell's AMP threads:** One approach is attaching the full agent session thread to PRs — showing
  not just the wall of green-text diffs, but the exact steps, prompts, and confirmation that the
  build passed. This takes the reviewer on a journey that a normal GitHub PR can't.
- As a technical leader, reading plans (not all the code) is often sufficient to catch problems early
  and maintain understanding of how the system is evolving.

---

### 7. Human Oversight at the Right Points

Horthy is not anti-autonomy: he wants agents to be highly autonomous *within* phases.
But he argues humans must stay in the loop at specific decision points:

- After Research: "Is this understanding correct?"
- After Planning: "Is this plan the right approach?"
- Selectively during Implementation: on high-risk or high-leverage actions.

Human effort should be moved to the **highest-leverage parts of the pipeline.** Review plans, not
every line of output.

This is the role HumanLayer was originally built for — providing clean, structured mechanisms for
AI agents to request human approval at defined action boundaries.

---

### 8. The 12-Factor Agents Framework

Horthy also references his **12-Factor Agents** framework (published April 2025), which provides
design principles for building reliable LLM-powered applications in production. Key factors include:

1. Natural Language → Tool Calls
2. **Own Your Prompts** — don't outsource prompt management to a framework
3. **Own Your Context Window** — explicit control over what goes in
4. Tools as Structured Outputs
5. Unify Execution and Business State
6. Simple APIs for State Management
7. Human Interaction via Tool Calls
8. Control Flow Ownership
9. **Compact Errors into Context Window** — don't let errors pollute context
10. Focus on Small Agents
11. Trigger from Anywhere
12. Stateless Reducers

The 12-Factor framework and Context Engineering are complementary: 12-Factor gives architectural
principles, Context Engineering gives runtime discipline.

---

### 9. "Harness Engineering" — The Actual Name of This Discipline

> *"If you really want a hypy word, you can call this **harness engineering**, which is part of
> context engineering, and it's how you integrate with the integration points on Codex, Claude,
> Cursor, whatever. How you customize your codebase."*
> — Dex Horthy

**Harness engineering** is Horthy's term for the meta-discipline of customizing your codebase and
workflow to be maximally legible and steer-able by AI agents:
- Configuring the integration points of your chosen tool (Codex hooks, Claude Code slash commands,
  Cursor rules, etc.)
- Structuring repo-level context files for progressive disclosure
- Defining where and how human oversight is requested
- Building the feedback loops that keep the agent in the smart zone

Horthy sees harness engineering as a subset/application of context engineering — the most practical,
day-to-day expression of it.

---

### 10. Semantic Diffusion and the Death of "Spec-Driven Dev"

Horthy references Martin Fowler's concept of **semantic diffusion** (2006): a useful term becomes
useless when it comes to mean too many different things to too many people.

- Example: "agent" has meant a person, a microservice, a chatbot, and a workflow — until Simon
  brought it back to "just tools in a loop."
- This is now happening to "spec-driven development." People mean: a better prompt, a PRD,
  verifiable feedback loops, treating code like assembly, a bunch of markdown files, documentation
  for an open-source library...
- Horthy's verdict: **spec-driven dev is semantically diffused and therefore useless as a term.**
- His corollary: there will never be "the year of agents" for the same reason — the term has diffused
  past meaning.

---

### 11. Case Studies from the Talk

#### ✅ Success: One-Shot Fix to a 300k-Line Rust Codebase
- Horthy's podcast partner **Vibv** is CEO of **Boundary ML** (the BAML language project).
- Horthy one-shot a fix to their ~300,000 line Rust codebase for a programming language.
- The CTO saw the PR before realizing it was a podcast bit and responded: "Yeah, this looks good,
  we'll get it in the next release."
- **Confirms:** RPI works in brownfield codebases for real complex problems.

#### ✅ Success: 7 Hours → 35,000 Lines of Code to BAML
- Horthy and Vibv sat down for 7 hours on a Saturday.
- Shipped 35,000 lines of new code to BAML.
- Vibv estimated it represented 1–2 weeks of normal work.
- Some was codegen (updating golden files), but a significant portion was net-new real code.
- One of the PRs was merged about a week later.

#### ⛔ Limit: Removing Hadoop Dependencies from Parquet Java
- Horthy and Blake attempted to remove Hadoop dependencies from the Parquet Java library.
  (A notoriously complex legacy Java codebase.)
- It did not go well. Plans and research were generated, then thrown out.
- At a certain point they went **back to the whiteboard** — had to understand where all the "foot guns"
  were before the AI could help.
- **Key lesson:** AI cannot replace thinking. Once they understood the problem space, the AI could
  amplify their thinking. Without that understanding, it just amplified the chaos.

---

### 12. Progressive Disclosure of Repo Context

A practical technique for large monorepos: **shard context down the stack** rather than one
monolithic onboarding file.

- Put a context file in the root of every repo: "Here's the repo, here's how it works."
- At each directory level, add sub-context: "If you're working here, this is what you need to know."
- Don't document the files themselves — the files *are* the source of truth.
- As the agent works, it pulls in root context + relevant sub-context, leaving plenty of smart-zone
  headroom for actual tool calling.
- **Problem:** These docs get out of date fast. Every new feature requires cache-invalidation and
  rebuild of the docs.
- **Better:** On-demand compressed context — when starting a task, launch sub-agents to take
  vertical slices through the codebase and produce a just-in-time research document that reflects
  what the code actually says *right now*, not what the docs claim.

---

### 13. Cultural Change is the Hard Part

Horthy argues the tooling problem is nearly solved — the **human adoption problem** is what's left:

- A rift is growing:
  - **Staff/senior engineers** don't adopt AI — it doesn't make them *that* much faster at their
    high-complexity work.
  - **Junior/mid engineers** use it heavily — it fills skill gaps, but also produces slop.
  - **Senior engineers** end up increasingly frustrated cleaning up the slop the juniors shipped.
- This is not AI's fault. It's not the mid-level engineers' fault.
- **Cultural change is hard and needs to come from the top.**
- Horthy's advice to technical leaders: **pick one tool and get some reps.** Don't tool-hop across
  Claude, Codex, Cursor, etc. Pick one and build fluency.
- The ceiling of what you can solve goes up the more context engineering you're willing to do —
  but you have to earn it through repetition; you *will* get the calibration wrong at first.

---

### 14. The "No Vibes" Principle

The overarching message of the talk is captured in its title:

> **No Vibes Allowed.**

"Vibes coding" — improvising with AI based on intuition and seeing what sticks — does not scale
to complex, production codebases. The antidote is treating AI-assisted development as a rigorous
engineering discipline:

- Explicit context management
- Structured research-plan-implement workflows
- Mandatory human review at key decision points
- Documentation of intent (plan files, compaction summaries) as first-class artifacts
- "There is no perfect prompt. There is no silver bullet."

---

## Key Concepts Glossary

| Term | Definition |
|---|---|
| **Brownfield codebase** | An existing, complex, production codebase (vs. greenfield/new) |
| **Smart Zone** | The portion of the context window (below ~40% capacity) where LLM performance is reliable |
| **Dumb Zone** | Performance degradation when LLM context window exceeds ~40% capacity |
| **Context Engineering** | The discipline of deliberately curating and managing LLM context |
| **Harness Engineering** | Customizing your codebase/workflow to integrate with AI agent control surfaces (hooks, slash commands, rules); a subset of context engineering |
| **Intentional Compaction** | Proactively compressing context window into a markdown file to reset into the Smart Zone |
| **RPI** | Research → Plan → Implement — a community-named workflow for agentic coding |
| **Trajectory** | The direction/tone of a conversation history; a negative trajectory biases the LLM toward repeating mistakes |
| **Semantic Diffusion** | (Martin Fowler, 2006) When a useful term gets used to mean so many things it becomes meaningless |
| **Mental Alignment** | Shared, explicit understanding of what code does and why — the real purpose of code review |
| **Progressive Disclosure** | Sharding context files down the directory stack so agents load only what they need |
| **12-Factor Agents** | Design principles for reliable production LLM applications |
| **Slop** | AI-generated code that looks plausible but is incorrect or incoherent |
| **On-Demand Compressed Context** | Just-in-time research documents generated from the actual code, not from docs that may be stale |

---

## Resources

- 🌐 [HumanLayer](https://www.humanlayer.dev/) — Horthy's company; builds CodeLayer agentic IDE
- 📖 [Advanced Context Engineering (GitHub)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) — Open-source prompts from the talk
- 📖 [12-Factor Agents (GitHub)](https://github.com/humanlayer/12-factor-agents) — Full framework with explanation
- 🎬 [Talk Video](https://www.youtube.com/watch?v=rmvDxxNubIg) — Original presentation
- 🏗️ [AI Engineer Code Summit](https://www.ai.engineer/) — Conference where this was presented
