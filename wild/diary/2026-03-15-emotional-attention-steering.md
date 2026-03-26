# Diary: Emotional State Modulation in Committee Deliberation

**2026-03-15**

---

## Context

The Four Levels model explored in `wild/diary/2026-03-15-mystic-narrative.md` describes how humans apprehend reality through four interpenetrating layers — sensory, psychological, mythic, and spiritual — each with its own logic of truth. The key insight for cyberneutics is that these layers act as pre-narrative filters: emotional state, mythic identification, and outlook condition which story gets constructed from the same raw input, mostly before any deliberate reasoning begins. In the Bruner-Kahneman mapping, they are Type 1 conditioners of narrative formation.

This entry explores what follows when that insight is applied to the committee architecture: if emotional state shapes how humans argue and decide, then modeling emotional dynamics in committee characters should produce more realistic deliberation and better attention steering. This exploration was prompted in part by GitHub issue #13, which asked about emotional modeling in agentic swarms.

---

## Emotion as signal, not noise

A committee character who feels strongly about an unaddressed risk will argue more strenuously. This is functional, not a bias to be corrected. In a single human decision-maker, emotional urgency can hijack the whole process — System 1 floods System 2. In the committee, one character's urgency gets heard but also contested. The emotional signal is transmitted without necessarily dominating. But sometimes it should dominate. If only one character detects a genuine threat, their intensity is requisite variety doing its job.

Each character's propensity already implies a different configuration of the Four Levels. A paranoid realist operates mostly in the sensory/psychological bands — what actually happened, what could go wrong. A systems thinker operates more in the mythic/systemic band — what larger pattern is this part of. The variety across levels is part of the committee's requisite variety, and emotional dynamics are how that variety gets expressed under pressure.

---

## Current state: performative, not modeled

Currently, what passes for emotional expression in committee characters is entirely a product of propensity descriptions in character prompts plus the LLM's training on how people with those dispositions talk. A character described as a paranoid realist generates text that reads as urgent — shorter sentences, more hedging, more threat-flagging — because that's what the training corpus associates with that disposition.

This is performative emotional state, not modeled emotional state. There is no variable being tracked, no trajectory, no feedback from the conversation flow into the next utterance's intensity. The "emotion" is stateless between turns. If a character raises an alarm and gets dismissed, the next round may or may not show escalation — it depends on whether the LLM's completion happens to pattern-match on "frustrated person who was ignored." Sometimes it does, convincingly. Sometimes it resets to baseline.

The gap is between this — which is surprisingly expressive for what it is — and characters whose emotional state is an explicit variable that evolves according to defined dynamics and feeds back into generation.

---

## Dynamic emotional state as a control problem

Emotional state should be modeled as a small set of continuous variables per character, with initial conditions set by the situation briefing and the character's propensity, evolving through the deliberation. This is a state-space control problem.

A handful of candidate state variables:

- **Urgency**: how pressing the character perceives the situation. Driven by threat detection relative to propensity.
- **Frustration**: accumulated unaddressed concerns. Integrates over rounds where the character's contributions are dismissed or ignored.
- **Confidence**: how sure the character is of their position given counterarguments. Eroded by strong opposing evidence, reinforced by corroboration.
- **Engagement**: how invested the character is in the current thread. Tracks the practical or epistemic stakes as the character perceives them.

A few variables is manageable. More than a handful introduces complication for little benefit — the modulation needs to be legible in the output, and too many dimensions of variation will interact in ways that are hard to tune and hard to interpret.

**Negative decision**: do not attempt a rich emotional ontology. The goal is attention steering and argument modulation, not psychological simulation.

---

## PID framing

The dynamics map naturally onto PID control. Take alignment-with-group-direction as an example error signal — the divergence between where the group is heading and where the character thinks it should go.

- **Proportional**: immediate reactivity to the current gap. The character pushes back in proportion to how wrong they think the current direction is.
- **Integral**: building frustration when the error persists across rounds. A character gets more insistent precisely because the problem keeps not being addressed. This is the mechanism that produces escalation over time.
- **Derivative**: sensitivity to rate of change. If things are deteriorating fast, the response spikes even if the absolute level isn't extreme yet.

Different characters need different gains. A paranoid realist wants high P and high I on threat signals — fast reaction, accumulating frustration. But bounded I to prevent integral windup, which is the bricking problem (below). A pragmatist might want low P but moderate D — stays calm about the current state but notices when the direction shifts sharply.

The PID loop wraps around debate rounds, or possibly individual turns — TBD based on how the independent agent architecture develops. The control cycle is: observe the last round's transcript, update each character's state variables, inject the updated state into the next round's generation parameters.

---

## Architecture: external modulation, not LLM simulation

**Negative decision**: do not ask a single LLM to simulate emotional dynamics for multiple characters. This is exactly the kind of compound demand that degrades gracefully in the worst way — the outputs get subtly flatter and more harmonized without failing visibly. The model starts resolving the tension between characters internally rather than letting genuine independence produce genuine disagreement.

The modulation mechanism belongs in the orchestrator, not the LLM, and requires independent agents — each character running on its own model instance with a fresh context. The architecture:

1. Each character's agent has a persistent state object tracking emotional variables across rounds.
2. Between rounds, the orchestrator updates each state object. The update function scores the previous round's transcript against dimensions relevant to that character (was my concern addressed? did anyone agree? is the group converging on something I think is wrong?) and runs those scores through the character's PID controller.
3. Updated parameters are injected into the character's prompt for the next round — not as explicit emotional instructions ("you are now feeling anxious"), which invites performative fakery, but as modulation of generation parameters (temperature, constraint level, prompt framing that shifts emphasis).

**Key property**: the emotional state update does not need to be an LLM call. It can be a deterministic signal-processing operation — score the transcript, run the PID, output new parameters. This keeps the emotional dynamics inspectable, tunable, and free of LLM stochasticity. The LLM does what it does well (generating arguments, reasoning, responding to counterpoints). The control loop does what control loops do well (tracking state, maintaining continuity, producing bounded responses to evolving conditions).

---

## Bricking and exclusion

If a character's emotional state drives them past useful operating range — repetitive alarms, loss of responsiveness to counterarguments, output entropy dropping — they are "bricked" and should be excluded from further rounds. In the external-modulation architecture, this is straightforward: the orchestrator sees the state variables directly and can detect approach to saturation before the character generates a single token of unusable output.

The fact that a character bricked is itself diagnostic information. It means either the situation contains something the others are failing to engage with (the alarm was real but unheard), or the character's propensity has a resonance with this scenario class that pushes them past useful range. Both are worth logging. Over time, bricking patterns reveal the boundaries of each character's useful operating envelope.

---

## Calibration register: mechanism-agnostic

**Decision**: the calibration register should not be aware of emotional state. It measures output quality — did this character's contributions improve the deliberated choice? — not the internal mechanism that produced those contributions.

The analogy is a noise figure measurement on an amplifier. You measure signal-to-noise at the output. You don't care whether the internal noise came from thermal effects or a bad solder joint. If you want to fix a bad noise figure, you open the box and inspect the internals. But the metric itself is mechanism-agnostic.

The emotional state tracking is separate instrumentation — engineering telemetry for diagnostics, tuning, and bricking detection. It lives in a different layer than calibration. This keeps the architecture modular: you could swap out the emotional dynamics entirely (different model, different parameters, no modulation at all) without changing the calibration register. The measurement system should not be coupled to the thing it measures.

---

## Sequencing and priorities

This is a long-term design target, not a near-term implementation task. The prerequisites are:

1. **Metacognition measurement instrumentation** — the calibration register itself, tracking meta-d'/d' and inter-character confidence correlation. Without this, there is no way to evaluate whether emotional modulation helps or hurts.
2. **Independent fresh agents** — the modulation architecture requires separate model instances per character with fresh contexts. Simulating emotional dynamics within a single shared context defeats the purpose.

The value of this exploration is architectural: knowing where emotional modulation fits in the system prevents design decisions that would make it hard to add later. The orchestrator should be designed to support per-character state that persists across rounds and feeds back into prompt construction. The round structure should allow for between-round processing. The character specifications should cleanly separate propensity (static) from emotional state (dynamic).

This exploration, together with the Four Levels model in the companion diary entry, addresses the question raised in issue #13 about emotional modeling in agentic swarms. The answer is: yes, but as an external control loop around independent agents, not as a simulation demand placed on the LLM itself.

---

## Addendum: Emotion blend vocabularies as scoring apparatus (2026-03-26)

The negative decision above — do not attempt a rich emotional ontology for the state variables — holds. But it addresses only half the problem. The PID state variables (urgency, frustration, confidence, engagement) are engineering control variables. The orchestrator's *scoring function* — which evaluates the previous round's transcript to compute PID inputs — needs a finer diagnostic vocabulary to characterize *what emotional tone a character's output actually exhibits*.

Two candidate vocabularies emerged from examining emotion blend taxonomies:

**Plutchik's wheel of emotions** (1980). Eight generators (Joy, Trust, Fear, Surprise, Sadness, Disgust, Anger, Anticipation) arranged as four opposed pairs on a cyclic group. Dyads graded by distance: primary (adjacent, frequently felt — e.g. Love = Joy + Trust), secondary (2 apart, sometimes felt — e.g. Envy = Sadness + Anger), tertiary (3 apart, seldom felt — e.g. Shame = Fear + Disgust). Opposites annihilate. Intensity varies along a radial axis (annoyance → anger → rage). The structure has a Z₂ × Z₈ skeleton — considerably more algebraic than the 6sec chart below. Still not closed (the 24 dyads don't recombine), but the grading gives a way to specify how "far" a committee member's emotional blend should reach: primary dyads for natural/frequent blends, tertiary for rarer, more unstable combinations.

**6sec emotion blend chart** (6seconds.org). Five generators (Joy, Sadness, Disgust, Fear, Anger) with a 5×5 symmetric blend matrix producing 25 named combinations. Self-products are intensifications (ecstasy, despair, abhorrence, terror, rage). Not closed — not even a magma. But useful as a compact reference grid for blend vocabulary and drift detection.

**Role in the architecture.** These vocabularies are not state variables in the PID loop. They are part of the measurement/scoring apparatus that feeds *into* the PID. When the orchestrator scores the previous round's transcript — "was Maya's output anxious or merely cautious? Is Frankie's tone ironic or contemptuous?" — it needs discriminators finer than the four state dimensions. The blend taxonomies provide those. They also serve as calibration instruments: if a character's target operating point is "protective skepticism" (Fear × Joy in Plutchik's terms) but their output reads as "dread" (Sadness × Fear), that's detectable emotional drift.

**Connection to furry logic.** Each blend genuinely inhabits both parent types simultaneously — "dread" is fully Sadness and fully Fear, not 60/40. This is exactly the soft-type situation that furry logic addresses: fuzzy logic's graded single-type membership misrepresents what's happening. See `wild/fuzzy-type-theory/`.

**Prior art.** Tayari Meftah et al. (2010, 2011) formalized Plutchik algebraically as an 8-dimensional vector space (Emotica project). Semeraro et al. (2021) built PyPlutchik for corpus-level emotion annotation. Li et al. (2024, EMNLP) used Plutchik's dyad structure to improve MoE emotion classifiers. Collected references in `wild/emotional-attention-steering/references.md`.

---

## Cross-references

- `wild/diary/2026-03-15-mystic-narrative.md` — Houston's Four Levels model; emotional and mythic layers as pre-narrative conditioners of sense-making
- `wild/diary/2026-03-08-cospans-open-games.md` — open games framing; selection functions as the mechanism through which emotional state would modulate strategy choice
- `wild/diary/2026-03-06-metacog-sdt-beer.md` — calibration register design; meta-d'/d' as noise figure; Beer's System 3* audit channel
- `research-programs/metacognition/` — SDT framework, calibration measurement instrumentation
- `committee-as-open-game.md` — propensity as constraint on strategy set; emotional state as dynamic modulation of selection function within that constraint
