# Emotional Attention Steering

**Status:** Exploratory — architectural design target. No experiment protocol or implementation yet. Prerequisites not met (metacog instrumentation, independent agents).

## Research question

How should emotional dynamics be modeled in the adversarial committee to steer attention and argument intensity during deliberation? What vocabulary and measurement apparatus is needed to score emotional tone in transcripts?

## Current answer

Emotional state is modeled as a small set of continuous PID-controlled variables per character (urgency, frustration, confidence, engagement), updated by an external orchestrator between rounds — not simulated by the LLM. The modulation mechanism belongs in the orchestrator, not the LLM, and requires independent agents running on separate model instances with fresh contexts.

Negative decisions: don't attempt a rich emotional ontology for the state variables; don't ask a single LLM to simulate emotional dynamics; keep the calibration register mechanism-agnostic.

The PID state variables are engineering control variables, not emotion labels. But the orchestrator's scoring function — which evaluates the previous round's transcript to compute PID inputs — needs a finer diagnostic vocabulary than the four state dimensions provide.

Plutchik's wheel of emotions (8 generators, Z₂ opposition, graded dyads by cyclic distance, intensity rays, opposite annihilation) and the 6sec emotion blend chart (5 generators, 25 blends) provide candidate vocabularies for this scoring layer. The blend vocabularies also serve as calibration instruments: if a committee member's target emotional operating point is "protective skepticism" but their output reads as "dread," that's a detectable drift.

This is a long-term design target, not a near-term implementation. Prerequisites: metacognition measurement instrumentation (calibration register) and independent fresh agents.

## Files in this directory

- **README.md** — this file
- **[references.md](references.md)** — collected references on emotion blend taxonomies and formal models
- **6sec-emotion-blend-chart.png** — the chart that prompted this investigation (source: 6seconds.org)

## Related files elsewhere

- [wild/diary/2026-03-15-emotional-attention-steering.md](../diary/2026-03-15-emotional-attention-steering.md) — the originating diary entry; PID architecture, state variables, bricking detection, calibration separation
- [wild/diary/2026-03-15-mystic-narrative.md](../diary/2026-03-15-mystic-narrative.md) — Houston's Four Levels model; emotional and mythic layers as pre-narrative conditioners of sense-making (the theoretical upstream)
- [wild/diary/2026-03-08-cospans-open-games.md](../diary/2026-03-08-cospans-open-games.md) — open games framing; selection functions as the mechanism through which emotional state would modulate strategy choice
- [wild/diary/2026-03-06-metacog-sdt-beer.md](../diary/2026-03-06-metacog-sdt-beer.md) — calibration register design; meta-d'/d' as noise figure
- [wild/committee-games/committee-as-open-game.md](../committee-games/committee-as-open-game.md) — propensity as constraint on strategy set; emotional state as dynamic modulation of selection function

## Epistemic status

The PID architecture is a sound engineering design but untested. The emotion blend vocabularies are borrowed from psychology (Plutchik) and EQ practice (6sec) and have not been validated as useful for LLM transcript scoring. The algebraic observations about Plutchik's wheel (Z₂ × Z₈ skeleton, graded dyads) are original to this project and informal.
