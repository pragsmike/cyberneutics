# Summary: "No Vibes Allowed: Solving Hard Problems in Complex Codebases"

**Presenter:** Dex Horthy, Founder & CEO of [HumanLayer](https://www.humanlayer.dev/)
**Event:** AI Engineer Code Summit, November 2025
**Video:** https://www.youtube.com/watch?v=rmvDxxNubIg

---

## Overview

Horthy opens by citing a Stanford study showing that AI coding tools — despite their hype — often
*decrease* net productivity when applied to real-world, complex ("brownfield") codebases. The culprit
is not the models themselves but the way engineers use them: intuitively, improvisationally, on
"vibes." The talk lays out a disciplined, engineering-first methodology to fix that.

The core thesis: **AI-assisted coding in complex codebases is a hard engineering problem, not a
magic trick.** It requires rigorous management of context, explicit workflows, and human oversight
at the right chokepoints.

---

## Main Points

### 1. The Problem: Brownfield AI Struggle

- AI tools work well for greenfield tasks (new projects, isolated files).
- In large, existing codebases they generate "slop" — plausible-looking but incorrect or
  architecturally incoherent code.
- The Stanford study found AI coding assistance can *reduce* developer throughput in complex settings.
- Root cause: the model doesn't have enough coherent context about the system to make good decisions.

---

### 2. The Dumb Zone

One of Horthy's key diagnostic concepts: LLMs have a **"Dumb Zone"** — a performance cliff that
occurs when the context window starts filling up, typically around **40% capacity**.

- As context fills, models begin to forget constraints, make more errors, and produce lower quality output.
- The model is stateless; its behavior is entirely determined by what is currently in the context window.
- A stuffed or poorly organized context window degrades model performance dramatically.
- Engineers often don't realize this is happening — they just see increasingly bad output.

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
- **Trajectory** — setting up the context so the next compaction is clean

The discipline is a progression from prompt engineering: instead of crafting a single prompt, you
design systems that dynamically build the right context over a session.

---

### 4. Frequent Intentional Compaction

The practical technique for staying out of the Dumb Zone is **intentional compaction** — regularly
and deliberately summarizing/distilling the current context before it grows too large.

- Rather than letting the context accumulate indefinitely, the engineer (or agent) periodically
  writes a compact summary of what has been decided, what is known, and what the plan is.
- This compact summary becomes the new starting context, shedding noise while preserving intent.
- This is analogous to writing good commit messages or design documents: capturing conclusions,
  not the full stream of reasoning.

---

### 5. The RPI Framework: Research → Plan → Implement

The operational workflow Horthy advocates is **RPI** — a structured three-phase approach:

```
Research → Plan → Implement
```

#### Research Phase
- The agent (or engineer + agent) explores the codebase to build objective understanding.
- Goal: produce a factual, accurate model of what exists — no code changes.
- Human reviews the research output before proceeding.

#### Plan Phase
- Based on the research, the agent produces a detailed **plan file** — a design document.
- The plan file is itself a form of intentional compaction: it crystallizes understanding into a
  structured artifact that becomes the context for implementation.
- **Human review is mandatory here.** This is the critical chokepoint for team mental alignment.
- The plan must be reviewed and agreed upon before any code is written.

#### Implement Phase
- The agent implements against the plan, using it as the primary context anchor.
- Continuous intentional compaction is applied during implementation.
- If complexity grows, a new research/plan cycle may be triggered for a sub-problem.

**Why this works:** Each phase produces a durable artifact that can be reviewed by humans, used to
re-anchor context, and shared across team members. It prevents "semantic diffusion" — the gradual
drift of shared understanding about what the code does and why.

---

### 6. Mental Alignment and the "Outsourcing Thinking" Problem

A second-order danger Horthy flags: when AI does too much of the work invisibly, teams lose
**mental alignment** — shared understanding of what the code does and why.

- When engineers accept AI-generated code without understanding it, they accumulate invisible technical debt.
- This is "outsourcing thinking," not just outsourcing labor.
- The plan review step in RPI is specifically designed to force explicit alignment before implementation.
- The plan file becomes a shared artifact that the whole team can reason about.

---

### 7. Human Oversight at the Right Points

Horthy is not anti-autonomy: he wants agents to be highly autonomous *within* phases.
But he argues humans must stay in the loop at specific decision points:

- After Research: "Is this understanding correct?"
- After Planning: "Is this plan the right approach?"
- Selectively during Implementation: on high-risk or high-leverage actions.

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

### 9. The "No Vibes" Principle

The overarching message of the talk is captured in its title:

> **No Vibes Allowed.**

"Vibes coding" — improvising with AI based on intuition and seeing what sticks — does not scale
to complex, production codebases. The antidote is treating AI-assisted development as a rigorous
engineering discipline:

- Explicit context management
- Structured research-plan-implement workflows
- Mandatory human review at key decision points
- Documentation of intent (plan files, compaction summaries) as first-class artifacts

---

## Key Concepts Glossary

| Term | Definition |
|---|---|
| **Brownfield codebase** | An existing, complex, production codebase (vs. greenfield/new) |
| **Dumb Zone** | Performance degradation when LLM context window exceeds ~40% capacity |
| **Context Engineering** | The discipline of deliberately curating and managing LLM context |
| **Intentional Compaction** | Proactively summarizing/distilling context to prevent Dumb Zone |
| **RPI** | Research → Plan → Implement workflow for agentic coding |
| **Semantic Diffusion** | Team drift in shared understanding of code intent |
| **Mental Alignment** | Shared, explicit understanding of what code does and why |
| **12-Factor Agents** | Design principles for reliable production LLM applications |
| **Slop** | AI-generated code that looks plausible but is incorrect or incoherent |

---

## Resources

- 🌐 [HumanLayer](https://www.humanlayer.dev/) — Horthy's company; builds CodeLayer agentic IDE
- 📖 [Advanced Context Engineering (GitHub)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) — Open-source prompts from the talk
- 📖 [12-Factor Agents (GitHub)](https://github.com/humanlayer/12-factor-agents) — Full framework with explanation
- 🎬 [Talk Video](https://www.youtube.com/watch?v=rmvDxxNubIg) — Original presentation
- 🏗️ [AI Engineer Code Summit](https://www.ai.engineer/) — Conference where this was presented
