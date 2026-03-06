# Agent Independence: Does Architectural Separation Improve Deliberation?

**Status**: Active (not started)
**Runs**: (none yet)
**Results**: (no results folder yet; create `agent-independence/results/` when first run begins)

> **Contributing to this program**
> - **Skills needed**: Access to a coding agent that supports independent subagents (e.g., Claude Code Agent Teams). Ability to run `/committee` deliberations and score on existing rubrics.
> - **Estimated scope**: Phase 1 is an afternoon (~4 hours). Phase 2 is 1–2 weeks.
> - **Contributor type**: Solo.
> - **Entry point**: Read the taxonomy in [committee-implementation-taxonomy.md](committee-implementation-taxonomy.md), then jump to Phase 1 below. Phase 1 is self-contained and produces a usable result regardless of whether Phase 2 runs.

---

## Objective

Test whether running committee characters as genuinely independent agent processes (separate context windows, peer-to-peer communication) produces better deliberation than the current approach of one model simulating all characters in a single context window.

**Core claim**: The current roleplay simulation forces one model to both generate and suppress its own tendencies — playing devil's advocate against itself. Independent agents with separate context windows can develop genuine positional commitments because each agent's reasoning accumulates in isolation before encountering the others' arguments. Disagreement emerges from architectural independence rather than being performed within a single reasoning thread.

**What this does NOT test**: Model diversity. All agents use the same underlying model. The model-diversity hypothesis is tested separately in [multi-model-committee.md](multi-model-committee.md). See [committee-implementation-taxonomy.md](committee-implementation-taxonomy.md) for how the two programs relate.

---

## Background

### The independence problem in current deliberations

The Condorcet comparison study ([condorcet-comparison.md](condorcet-comparison.md)) noted a limitation: "In a single model session, true independence of CJT-style votes is hard to guarantee." This applies equally to the committee pipeline — when one model plays all five characters in sequence, each character's response is conditioned on the full context of prior characters' responses *and* on the model's own tendency toward coherence. The model is not genuinely surprised by what "Maya" says when it was the same model that generated Maya's response moments earlier.

Independent agent processes address this directly. Each agent builds its own reasoning in its own context window. When agents communicate, the receiving agent encounters the other's argument as genuinely new information rather than as something it already generated.

### Prior attempts

A Cowork plugin attempt (2026-02-24) instantiated committee characters as separate agent definitions (`.md` system prompts). The attempt failed because the agents had no mechanism to communicate with each other — they were isolated oracles that only spoke when addressed by a central orchestrator. This produced simulated hub-and-spoke, not genuine peer debate. The lesson: agent independence requires both separate context *and* a communication mechanism.

Claude Code's Agent Teams feature (experimental, launched Feb 5 2026 with Opus 4.6) addresses both requirements. Agents are spawned into separate processes and communicate peer-to-peer via a `SendMessage` tool backed by a file-based mailbox system. Each agent runs in its own process with an independent context window.

**Confirmed feasibility (March 2026 landscape survey)**: A 5-agent committee deliberation is feasible within Agent Teams. Anthropic's own documentation lists "debate and consensus" as a use case. Teams of 5+ agents have been demonstrated in practice. Estimated cost per deliberation: ~$30–50 with Opus-class models; estimated wall-clock time: 10–20 minutes. Each teammate can be assigned a different Claude model (Opus, Sonnet, Haiku), enabling Tier 1+ experiments within the same platform.

**Practical limits to watch for**: Agent context windows are consumed by the accumulation of peer messages — in long deliberations this may degrade late-round reasoning quality. Reliability issues have been reported in early adopter usage. The feature is experimental and the API surface may change. See `references/coding-agent-subagent-capabilities-2026-03.md` for the full assessment.

Whether this is sufficient for multi-round committee deliberation following Robert's Rules is the open empirical question this program tests.

---

## Experimental Protocol

### Phase 1: Paired Comparison (one topic, both methods)

**Goal**: Determine whether there is an observable qualitative difference between roleplay and independent-agent deliberation on the same topic.

**Duration**: An afternoon.

**Procedure**:

1. **Choose one topic** — preferably a topic with known deliberation history (e.g., one used in the condorcet comparison or a prior `/committee` run) so there is a baseline to compare against.

2. **Condition A (Roleplay baseline)**: Run a standard `/committee` deliberation using the current single-context pipeline. Record the full transcript.

3. **Condition B (Independent agents)**: Run the same topic using Claude Code Agent Teams. Each of the five committee characters is spawned as a separate teammate with a spawn prompt containing:
   - Its character brief from `agent/roster.md`
   - Instructions to follow Robert's Rules of Order for debate
   - The topic under deliberation (identical to Condition A)

   Teammates communicate peer-to-peer via the `SendMessage` tool. The Chair (Joe) manages turn-taking and progression. All agents see messages addressed to them or broadcast to the group. Record all messages. Note: Agent Teams supports specifying different Claude models per teammate (Opus, Sonnet, Haiku) — for the Tier 1 experiment, hold model constant; a follow-up Tier 1+ experiment can vary models.

4. **Evaluate both transcripts** using the existing 5-rubric system (comprehensiveness, adversarial rigor, assumption coverage, reasoning depth, decision readiness). Use the `/review` skill or manual scoring.

5. **Qualitative comparison**: Beyond rubric scores, assess:
   - Do the independent agents develop genuinely different arguments, or do they converge to the same positions as the roleplay?
   - Is there evidence of authentic surprise — an agent visibly changing its position in response to another's argument?
   - Does the debate feel qualitatively different? (More combative? More exploratory? More repetitive?)

**Output**: A comparison write-up in `agent-independence/results/` following the format of the condorcet comparison results.

**Decision gate**: Is there an observable difference? If the transcripts are qualitatively indistinguishable, the agent-independence hypothesis may not hold for this platform and model combination. If they differ, proceed to Phase 2.

---

### Phase 2: Controlled Comparison (multiple topics, scored)

**Goal**: Quantify the difference across topics and rubrics.

**Duration**: 1–2 weeks.

**Procedure**:

1. **Select 5 topics** covering different domains and difficulty levels (ethics, technical, governance, resource allocation, strategy — matching the multi-model-committee's topic selection for comparability).

2. **Run both conditions** (A: roleplay, B: independent agents) on all 5 topics.

3. **Score all 10 transcripts** on the 5 rubrics. Ideally blind (evaluator does not know which condition produced which transcript).

4. **Compute**: Mean scores per rubric per condition. Effect sizes (Cohen's d) for the difference. Note which rubrics show the largest differences.

5. **Cost analysis**: Compare token usage, wall-clock time, and API cost between conditions. Independent agents will likely use more tokens (separate context windows, message overhead). Is the quality improvement (if any) worth the cost?

**Output**: Results table, effect sizes, cost comparison, and a recommendation on whether independent-agent deliberation should become the default or remain a special-case option.

---

## Evaluation Framework

Uses the existing 5-rubric system shared with other research programs:

| Rubric | What it measures |
|--------|-----------------|
| Comprehensiveness | Were all relevant aspects of the topic covered? |
| Adversarial rigor | Were arguments genuinely challenged, not just acknowledged? |
| Assumption coverage | Were hidden assumptions surfaced and examined? |
| Reasoning depth | Was the analysis deep or superficial? |
| Decision readiness | Could a decision-maker act on this output? |

Extended with two independence-specific observations (not scored, qualitative):

- **Positional commitment**: Did individual characters develop and maintain distinct positions, or did they drift toward agreement prematurely?
- **Authentic surprise**: Were there moments where an agent visibly updated its position in response to information it could not have anticipated from its own context?

---

## Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Agent Teams feature is too unstable or limited for 5-agent multi-round debate | Medium | High | Run a dry run with 2 agents first to test feasibility. If the feature can't handle it, document the limitation and defer until the platform matures. |
| Token cost is prohibitive (5 separate context windows) | Medium | Medium | Landscape survey estimates ~$30–50 per 5-agent deliberation with Opus-class models. Run Phase 1 first (one topic) to measure actual cost before committing to Phase 2. Using Sonnet for teammates (Tier 1+ configuration) would reduce cost significantly. |
| No observable difference (roleplay is already good enough) | Medium | Low | This is a valid finding. Document it — it means the current approach is more robust than expected and the multi-model program becomes the higher-priority path. |
| The Chair agent can't effectively manage turn-taking via sendMessage | Medium | Medium | Provide explicit procedural instructions. If peer coordination fails, fall back to a lightweight orchestrator that manages turn order but not content — less pure than full peer-to-peer but still better than single-context roleplay. |

---

## Connection to Other Programs

This program tests one cell of the implementation taxonomy (single-model, independent agents). Its results inform:

- **multi-model-committee**: If agent independence alone produces measurable improvement, then the multi-model program should control for implementation mechanism (not just model identity). If no improvement, model diversity is the more promising axis.
- **evaluating-deliberative-architectures**: The Black Swan framework's C2 condition ("peer-agent committee") can be implemented via either roleplay or independent agents. Results from this program indicate whether C2's implementation mechanism materially affects the framework's results.
- **The convergence question**: If both this program (independence helps) and the multi-model program (diversity helps) produce positive results, the case for Tier 2 (built-in multi-model subagents) becomes compelling.

See [committee-implementation-taxonomy.md](committee-implementation-taxonomy.md) for the full taxonomy and how all programs relate.
