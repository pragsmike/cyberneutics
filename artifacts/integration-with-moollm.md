# Integration with MOOLLM: Cyber-Sense as Application

## Conceptual Framing

### MOOLLM as Operating System

[MOOLLM](https://github.com/SimHacker/moollm) provides infrastructure for LLM-based applications the way an operating system provides infrastructure for traditional software. The core primitives:

- **Rooms** as cognitive contexts (process isolation, bounded conversation scope)
- **Cards** as actors (addressable entities with persistent identity and behavior)
- **Files-as-state** (persistence layer that survives session boundaries)
- **Protocols** as system calls (standardized interaction patterns, enforceable contracts)

An operating system doesn't know what applications will run on it. It provides memory management, process scheduling, and inter-process communication. Applications provide domain logic, user interaction models, and workflows.

### Cyber-Sense as Application

Cyber-Sense is a methodology that can run "bare metal" (manual state management, ad-hoc context injection) or on MOOLLM infrastructure. The relationship is analogous to version control concepts versus Git: you can practice version control with manual file copies and naming conventions, but Git provides infrastructure that makes it reliable, auditable, and scalable.

What MOOLLM provides that ad-hoc approaches lack:

| Ad-Hoc Approach | MOOLLM Equivalent |
|-----------------|-------------------|
| Copilot directories with markdown files | First-class file objects with query capability |
| "Use a fresh instance" (honor system) | Room isolation (OS-enforced) |
| Copy-paste handoff documents into context | Automatic state persistence across sessions |
| Hoping the model follows Robert's Rules | Protocol enforcement at system level |
| Manual lesson injection | Queryable institutional memory |

Cyber-Sense provides what MOOLLM doesn't: the methodology itself. Which characters to use, how to calibrate them, what makes a good rubric, when to iterate, how to extract lessons. MOOLLM is the platform; Cyber-Sense is the practice.

## Mapping Cyber-Sense Primitives to MOOLLM Primitives

### Characters → Cards

The five-character roster (Maya, Frankie, Joe, Vic, Tammy) maps naturally to MOOLLM cards:

```
Card: Maya
├── Propensity: paranoid-realism
├── Configuration: assumes political complexity, hidden agendas, bad-faith actors
├── Signature moves: [defined phrases and patterns]
├── Calibration state: [adjustments from past deliberations]
└── Activation context: [when to invoke this character]
```

Characters as cards enables:
- Persistent identity across deliberations
- Calibration that accumulates (Maya gets "tuned" over time)
- Swappable rosters for different domains
- Version control on character definitions

### Committee Sessions → Rooms

A deliberation is a bounded cognitive context—exactly what rooms provide:

```
Room: hiring-decision-2026-02-01
├── Participants: [Maya, Frankie, Joe, Vic, Tammy cards]
├── Protocol: roberts-rules-v1
├── Input: [problem statement, context documents]
├── State: [current motion, speaking queue, vote tally]
├── Output: [minutes, recommendation, dissents]
└── Lifecycle: setup → deliberation → minutes → archival
```

Room isolation guarantees that what happens in the deliberation room stays in the deliberation room—critical for independent evaluation.

### Lessons and Rubrics → Files

Cross-scenario learning requires persistent, queryable storage:

```
File: lessons/hiring/2026-01-15-senior-engineer.md
├── Domain: hiring
├── Decision type: senior technical hire
├── Key lessons: [structured extraction]
├── Applicable when: [trigger conditions]
└── Confidence: [how well-validated]

File: rubrics/deliberation-quality-v2.md
├── Dimensions: [evidence quality, assumption surfacing, ...]
├── Scoring: [1-5 scale definitions]
├── Failure indicators: [what triggers re-deliberation]
└── Version history: [how rubric evolved]
```

MOOLLM provides storage and retrieval. Cyber-Sense defines the schema—what lessons look like, how to query them, when to inject them into deliberations.

### Robert's Rules → Protocol

Currently, Robert's Rules enforcement depends on the model following instructions. With MOOLLM, it becomes a protocol specification:

```
Protocol: roberts-rules-v1
├── States: [idle, motion-pending, debate, voting, ...]
├── Transitions: [valid state changes]
├── Turn-taking: [who can speak when]
├── Violations: [what happens on invalid action]
└── Outputs: [required artifacts per state]
```

Protocol violations become system-level errors rather than model discretion. The infrastructure enforces procedure; the model provides content within that structure.

## Architecture Patterns

Cyber-Sense can run at different capability levels. The methodology remains constant; the infrastructure determines what guarantees you get.

### Pattern A: Single-Instance Simulated Committee

**Configuration**: One room, one model instance, characters simulated via prompt.

```
┌─────────────────────────────────────┐
│ Room: Deliberation                  │
│ ┌─────────────────────────────────┐ │
│ │ Single Model Instance           │ │
│ │ - Simulates all 5 characters    │ │
│ │ - Self-enforces Robert's Rules  │ │
│ │ - Generates + evaluates         │ │
│ └─────────────────────────────────┘ │
│ State: persisted via MOOLLM files   │
└─────────────────────────────────────┘
```

**What MOOLLM provides**: State persistence, eliminating manual handoffs. Session continuity without context injection.

**What you lose**: True isolation between generation and evaluation. Diversity is simulated, not actual.

**Appropriate for**: Low-stakes decisions, rapid iteration, resource-constrained environments.

This is essentially current Cyber-Sense practice with better state management.

### Pattern B: Isolated Evaluation Rooms

**Configuration**: Separate rooms for deliberation and evaluation, possibly same model instance but with enforced context isolation.

```
┌─────────────────────────┐     ┌─────────────────────────┐
│ Room: Deliberation      │     │ Room: Evaluation        │
│ ┌─────────────────────┐ │     │ ┌─────────────────────┐ │
│ │ Committee Instance  │ │     │ │ Evaluator Instance  │ │
│ │ - 5 characters      │ │     │ │ - Fresh context     │ │
│ │ - Produces minutes  │ │────▶│ │ - Rubric scoring    │ │
│ └─────────────────────┘ │     │ │ - No deliberation   │ │
│                         │     │ │   history visible   │ │
└─────────────────────────┘     └─────────────────────────┘
                                           │
                                           ▼
                                    Score + Feedback
                                           │
                          ┌────────────────┴────────────────┐
                          │                                 │
                          ▼                                 ▼
                    Score ≥ threshold              Score < threshold
                          │                                 │
                          ▼                                 ▼
                       Accept                    Return to Deliberation
                                                 with feedback
```

**What MOOLLM provides**: Enforced isolation. The evaluator literally cannot see the deliberation history—it only receives the output artifacts. Audit trail proves what each room could access.

**What you gain over Pattern A**: Independent evaluation is actually independent. The hermeneutic circle is broken by architecture, not honor system.

**Appropriate for**: High-stakes decisions, audit requirements, when you need to demonstrate rigor.

### Pattern C: Editorial Review Committee

**Configuration**: Evaluation performed by a second committee with different composition—editors and fact-checkers rather than the original deliberators.

```
┌─────────────────────────┐     ┌─────────────────────────┐
│ Room: Deliberation      │     │ Room: Editorial Review  │
│ ┌─────────────────────┐ │     │ ┌─────────────────────┐ │
│ │ Primary Committee   │ │     │ │ Review Committee    │ │
│ │ - Maya, Frankie,    │ │     │ │ - Editor-in-Chief   │ │
│ │   Joe, Vic, Tammy   │ │────▶│ │ - Fact-Checker      │ │
│ │ - Domain experts    │ │     │ │ - Devil's Advocate  │ │
│ └─────────────────────┘ │     │ │ - Domain Skeptic    │ │
│                         │     │ └─────────────────────┘ │
└─────────────────────────┘     └─────────────────────────┘
```

**What this adds**: Different propensities for evaluation than deliberation. The editorial committee isn't trying to solve the problem—they're trying to find holes in the solution. Different characters optimize for different failure modes.

**Potential editorial roster**:
- **Editor-in-Chief**: Evaluates clarity, coherence, whether the recommendation is actionable
- **Fact-Checker**: Demands sources for claims, flags unsupported assertions
- **Devil's Advocate**: Argues the opposite position, stress-tests the conclusion
- **Domain Skeptic**: Questions whether the committee understood the problem correctly

**Appropriate for**: Complex decisions where you want adversarial review, not just quality scoring.

### Pattern D: Parallel Multi-Instance (Aspirational)

**Configuration**: Each character as a separate model instance, running in parallel, with MOOLLM coordinating communication.

```
┌─────────────────────────────────────────────────────────┐
│ Room: Deliberation                                      │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│ │ Maya    │ │ Frankie │ │  Joe    │ │  Vic    │ │ Tammy   │
│ │Instance │ │Instance │ │Instance │ │Instance │ │Instance │
│ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
│      │          │          │          │          │      │
│      └──────────┴──────────┴──────────┴──────────┘      │
│                           │                              │
│                    Protocol Enforcer                     │
│                    (turn-taking, motions)                │
└─────────────────────────────────────────────────────────┘
```

**What this enables**: Genuine diversity from different instances, not simulated. Each character has truly independent reasoning. Parallel execution where instances deliberate simultaneously then synchronize.

**Current status**: Aspirational. Requires MOOLLM multi-instance coordination that may not yet exist. The architecture shouldn't preclude this, but implementations should degrade gracefully to Pattern A/B/C.

**Research questions this enables**: When does simulated diversity suffice? When do you need actual independent instances? What's the quality/cost tradeoff?

### Choosing a Pattern

| Factor | Pattern A | Pattern B | Pattern C | Pattern D |
|--------|-----------|-----------|-----------|-----------|
| Resource cost | Low | Medium | Medium-High | High |
| Setup complexity | Minimal | Moderate | Moderate | Complex |
| Isolation guarantee | None (simulated) | Enforced | Enforced | Maximum |
| Diversity source | Prompt simulation | Prompt simulation | Different rosters | Different instances |
| Audit trail | Weak | Strong | Strong | Strongest |
| Current feasibility | Now | Now | Now | Aspirational |

**Decision heuristic**:
- Exploring options, low stakes → Pattern A
- Need defensible process, audit trail → Pattern B
- Complex decision, want stress-testing → Pattern C
- Research context, studying methodology itself → Pattern D (when available)

## Migration Path

For practitioners currently using Cyber-Sense without MOOLLM, migration can be incremental.

### Stage 1: State Externalization

**Goal**: Eliminate manual handoff documents without changing workflow.

**Changes**:
- Copilot directory contents become MOOLLM file objects
- Handoff documents auto-generated from room state
- Lesson library queryable rather than manually injected
- Character calibrations persist automatically

**What stays the same**: Single-instance deliberation, simulated characters, manual evaluation. This is Pattern A with better plumbing.

### Stage 2: Evaluation Isolation

**Goal**: Make independent evaluation actually independent.

**Changes**:
- Split deliberation and evaluation into separate rooms
- MOOLLM enforces context boundaries
- Audit trail shows exactly what evaluator could see
- Iteration loop can be automated (re-deliberate if score below threshold)

**What you gain**: Pattern B—enforced isolation, reproducible evaluation, audit compliance.

### Stage 3: Protocol Formalization

**Goal**: Make Robert's Rules violations impossible rather than discouraged.

**Changes**:
- Robert's Rules as executable protocol specification
- Invalid moves rejected by system
- Turn-taking enforced, not suggested
- Meeting state machine explicit

**What you gain**: Reproducible procedure. Different instances running the same protocol produce structurally comparable outputs.

### Stage 4: Editorial Committees

**Goal**: Specialized review beyond quality scoring.

**Changes**:
- Define editorial roster (Editor-in-Chief, Fact-Checker, etc.)
- Review room receives deliberation output
- Editorial committee applies different propensities than primary committee
- Output includes both recommendation and editorial assessment

**What you gain**: Pattern C—adversarial review from characters optimized for finding problems rather than solving them.

### Stage 5: Multi-Instance (When Available)

**Goal**: Genuine parallel deliberation with independent instances.

**Changes**:
- Each character as separate model instance
- MOOLLM coordinates turn-taking across instances
- Parallel execution where appropriate
- True diversity, not simulated

**Prerequisites**: MOOLLM multi-instance coordination, cost-effective parallel inference.

**Design principle**: Patterns A-C should be implemented such that Pattern D is a configuration change, not an architecture change. The room structure, protocol definitions, and file schemas should work regardless of whether characters are simulated or instantiated.

## What Cyber-Sense Provides That MOOLLM Doesn't

MOOLLM provides infrastructure. Cyber-Sense provides methodology. The distinction matters.

### Character Design and Calibration

MOOLLM can store character definitions as cards. It doesn't know:
- What propensities produce useful tension
- How to balance risk-seeking vs. risk-averse characters
- When to add domain-specific characters vs. use the standard roster
- How to calibrate based on past performance

This is Cyber-Sense domain knowledge.

### Rubric Development

MOOLLM can store and retrieve rubrics. It doesn't know:
- What dimensions matter for deliberation quality
- How to score "evidence quality" vs. "assumption surfacing"
- What failure indicators should trigger re-deliberation
- How to evolve rubrics based on experience

This is Cyber-Sense methodology.

### Lesson Extraction and Injection

MOOLLM provides queryable storage. It doesn't know:
- What makes a lesson generalizable vs. context-specific
- When to inject past lessons vs. let the committee discover fresh
- How to weight recency vs. relevance
- What "similar enough" means for cross-scenario learning

This is Cyber-Sense practice.

### The Judgment Calls

When do you need Pattern B vs. Pattern A? When is a decision "high-stakes enough" for editorial review? When has a committee reached diminishing returns on iteration?

MOOLLM provides the machinery. Cyber-Sense provides the judgment.

## Open Design Questions

### Character Identity Across Sessions

Should Maya in today's hiring decision be "the same" Maya as in last month's strategic pivot discussion?

**Arguments for shared identity**:
- Calibration accumulates—Maya gets better over time
- Institutional memory—Maya "remembers" past decisions
- Consistency—stakeholders know what to expect from Maya

**Arguments for fresh instances**:
- Prevents contamination—past biases don't infect new decisions
- Cleaner evaluation—easier to reproduce
- Domain-specific calibration—hiring-Maya vs. strategy-Maya

**Current recommendation**: Shared identity within a domain, fresh instances across domains. Hiring-Maya persists across hiring decisions. Strategy-Maya is a different card.

### Protocol Rigidity

How strictly should MOOLLM enforce Robert's Rules?

Too rigid: Model can't request procedure suspension when genuinely stuck.
Too flexible: Model games the system, skips inconvenient procedures.

**Current recommendation**: Strict enforcement with explicit "point of order" escape hatch. The model can request procedure suspension, but must do so explicitly, and the request is logged. Default is enforcement; exceptions require justification.

### Evaluation Recursion

Can the evaluator's output be evaluated? Should it be?

**Risk**: Infinite regress. Evaluator evaluates deliberation, meta-evaluator evaluates evaluator, meta-meta-evaluator...

**Practical limit**: Two levels usually suffice. Deliberation → Evaluation → Meta-check on whether evaluator applied rubric correctly. Beyond that, diminishing returns.

**Termination conditions**:
- Score above threshold at each level
- Maximum iteration count
- Diminishing score improvement (delta below threshold)

### Interoperability

Can Cyber-Sense rooms interact with non-Cyber-Sense MOOLLM applications?

**Example**: A research synthesis application produces a summary. Can that summary be input to a Cyber-Sense deliberation room?

**Current recommendation**: Define clean interfaces. A Cyber-Sense room accepts:
- Problem statement (text)
- Context documents (files)
- Relevant lessons (query results)

Any MOOLLM application that can produce those artifacts can feed a Cyber-Sense deliberation. The methodology doesn't require the input to come from Cyber-Sense.

## Example: Hiring Decision on MOOLLM

Walking through the existing [hiring-decision-example](./examples/hiring-decision-example.md) reimplemented on MOOLLM infrastructure (Pattern B: Isolated Evaluation).

### Setup

```
1. Create Room: hiring-senior-engineer-2026-02
   - Protocol: roberts-rules-v1
   - Participants: [Maya, Frankie, Joe, Vic, Tammy]
   
2. Load Context:
   - File: problem-statement.md (job req, candidates, constraints)
   - Query: lessons/hiring/* where seniority=senior
   - Result: 3 relevant past lessons injected
   
3. Create Evaluation Room: hiring-eval-2026-02
   - Protocol: rubric-evaluation-v1
   - Input: [output of deliberation room]
   - Rubric: rubrics/deliberation-quality-v2.md
```

### Deliberation

```
4. Deliberation proceeds per Robert's Rules
   - Model cannot skip procedure (protocol-enforced)
   - Each character responds per their propensity
   - Motions, seconds, debate, votes all logged
   
5. Room produces artifacts:
   - minutes.md (full transcript)
   - recommendation.md (structured output)
   - dissents.md (minority positions)
```

### Evaluation

```
6. Evaluation room receives ONLY:
   - recommendation.md
   - dissents.md
   - (NOT the full transcript—evaluator judges output, not process)
   
7. Evaluator scores against rubric:
   - Evidence quality: 4/5
   - Assumption surfacing: 3/5
   - Trade-off articulation: 5/5
   - Dissent quality: 4/5
   - Overall: 4.0/5.0 (threshold: 3.5)
   
8. Score ≥ threshold → Accept
   - Final artifacts archived
   - Lessons extracted and stored
   - Room closed
```

### If Score Below Threshold

```
8a. Score < threshold → Return to deliberation
    - Evaluator feedback injected into deliberation room
    - Specific dimensions flagged (e.g., "assumption surfacing weak")
    - Committee re-deliberates with attention to feedback
    - New output sent to evaluation room
    - Repeat until threshold or max iterations
```

### Archival

```
9. Final state:
   - All artifacts in MOOLLM file store
   - Queryable for future hiring decisions
   - Audit trail shows: inputs, deliberation, evaluation, iterations
   - Lessons extracted per lesson-extraction-template
```

## Summary

MOOLLM provides the operating system: rooms, cards, files, protocols. Cyber-Sense provides the application: character rosters, deliberation patterns, evaluation rubrics, lesson extraction.

The integration allows Cyber-Sense to run at multiple capability levels:
- **Pattern A**: Single instance, simulated committee, MOOLLM provides state persistence
- **Pattern B**: Isolated evaluation rooms, MOOLLM enforces context boundaries
- **Pattern C**: Editorial review by second committee with different propensities
- **Pattern D** (aspirational): True multi-instance parallel deliberation

Migration is incremental. Each stage adds guarantees without requiring practitioners to change their methodology—just their infrastructure.

The goal is not to make Cyber-Sense dependent on MOOLLM, but to make MOOLLM the optimal environment for rigorous Cyber-Sense practice. The methodology remains portable; the infrastructure makes it reliable.

---

*For MOOLLM specifications and implementation status, see the [MOOLLM repository](https://github.com/SimHacker/moollm).*

*For Cyber-Sense methodology independent of MOOLLM, see the [artifacts](./README.md) and [essays](../essays/README.md) in this repository.*
