# From Semantic Potential to Situated Sense

> **Status**: ACTIVE — Polished essay ready for immediate promotion to essays/. See [wild triage report](../../agent/archive/wild-triage-2026-03.md).

An essay arguing that meaning in LLM interactions is co-produced in conversation rather than stored in model weights or extracted by prompting. The essay develops the claim through distributional semantics, Pask's conversation theory, von Foerster's eigenforms, and a cybernetic model of the human-LLM control loop.

## Contents

- **[from_semantic_potential_to_situated_sense.md](from_semantic_potential_to_situated_sense.md)** — The full essay. Eleven sections tracing a path from LLMs-as-semantic-potential-fields through pragmatic collapse (human participation converting potential into situated sense) to implications for AI theory, interface design, epistemology, and multi-agent systems.

- **[pask-machine-machine.md](pask-machine-machine.md)** — Working document on Pask's Colloquy of Mobiles (1968) as the earliest machine-machine conversation, the chameleon-mirror problem and its implications for LLM pipeline design, bisimulation as the right frame for evaluating committee character propensities, and the connection to absent-party communication (decipherment as bisimulation reconstruction from trace). Connects to `wild/communicating-absent-parties/`, `wild/committee-games/committee-as-open-game.md`, and the calibration register's zero-feedback limit.

## Central Argument

LLMs maintain structured fields of semantic potential rather than storing determinate meanings. LLM-only discourse explores a statistical landscape with its own attractors and degeneracies but lacks external grounding. Human participation introduces pragmatic, embodied, and social constraints — relevance, correction, consequences — that convert potential into situated sense. Meaning is a temporary eigenform of a coupled human-machine conversation: stable enough to be used, but dependent on the ongoing dynamics of the exchange.

## Connection to the Repo

This essay provides theoretical grounding for several commitments that the cyberneutics methodology makes in practice but has not previously argued from first principles:

- **Why multi-agent deliberation needs human gates.** The essay's account of LLM-only discourse drifting toward attractors and degeneracies is the theoretical basis for the human gate in the palgebra — the collapse operator that prevents pipeline outputs from floating free of pragmatic constraint.

- **The cybernetic control loop.** Section 9's formulation of prompt-proposal-feedback as a control loop parallels the remediation loop in the committee workflow. The essay provides the epistemological argument for why that loop matters: meaning is not retrieved but negotiated.

- **Eigenforms and the Probe.** The essay's use of von Foerster's eigenforms — stable distinctions produced by recursive interaction — connects directly to the palgebra treatment of eigenforms as resolution-content invariant across Probe runs (see `palgebra/categorical-structures.md` §9 and `wild/residuality-theory/`).

- **Pask and conversation theory.** The essay draws on the same Paskian roots as the [cybernetics](../cybernetics/) directory, developing the conversation-theoretic account in the specific context of LLM interaction.

Key cross-references:

- `essays/04-cybernetics-and-observation.md` — von Foerster, eigenforms, second-order cybernetics
- `wild/cybernetics/conversation-theory.md` — Pask's conversation theory
- `palgebra/categorical-structures.md` — eigenforms in the pipeline context
- `wild/residuality-theory/` — residues vs. eigenforms distinction
- `palgebra/decorated-texts.md` — soft types and the measurement framing
- `wild/communicating-absent-parties/` — absent-party communication, frozen entailment meshes
- `wild/committee-games/committee-as-open-game.md` — propensity as strategy-set constraint

## Status

**Complete draft, not yet integrated.** The essay is self-contained and polished. Integration questions:

- Does it belong in `essays/` as a standalone piece, or does its theoretical scope make it better suited as a reference from multiple essays?
- The "pragmatic collapse" concept could inform the palgebra's treatment of human gates. Currently the gate is described operationally; this essay provides the epistemological argument for why it exists.
- The measurement framing for meaning (§5) resonates with the furry logic diary entry's measurement framing for type membership (see `wild/diary/2026-03-13-furry-logic.md` §4). Both argue that the interesting property is relational (between text and instrument/rubric) rather than intrinsic. A future essay on soft types could draw on both.
