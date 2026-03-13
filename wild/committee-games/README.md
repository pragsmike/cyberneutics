# Committee Games

> **Status**: ACTIVE — Game-theoretic formalization of the adversarial committee; ready for publication as bridge paper for ACT community. See [wild triage report](../../agent/archive/wild-triage-2026-03.md).

A translation of the cyberneutics adversarial committee into the language of compositional game theory (open games), building a bridge to the ACT / Cybercat research community.

## Contents

- **[committee-as-open-game.md](committee-as-open-game.md)** — The committee formalized as an open game with five player sub-games composed in parallel (Stage 2, tensor product) and sequentially (Stage 3, categorical composition). Covers: typing the committee ports, propensity as strategy-set constraint rather than utility function, the evaluation rubric as continuation function, fan/funnel as composed open games, the distinction between equilibrium (fixed point of deliberation) and resolution (product of the Resolve morphism), and the connection to dependent optics.

## Connection to the Repo

This document operationalizes the open-thread from the [2026-03-08 diary entry](../diary/2026-03-08-cospans-open-games.md), which asked whether the committee/open-games analogy is genuinely functorial or merely suggestive. It is the game-theoretic companion to the resource-theoretic treatment in [palgebra/committee-as-palgebra.md](../../palgebra/committee-as-palgebra.md): both formalize the same workflow, but the open games treatment recovers the strategic dimension — backward-flowing evaluation signals, best-response structure, and the claim that rubric design is mechanism design — that the resource equations leave implicit.

Key cross-references:

- `palgebra/committee-as-palgebra.md` — resource-theoretic treatment of the same structure
- `palgebra/duality-and-composition.md` — fan/funnel duality and the decision monad
- `palgebra/categorical-structures.md` — categorical constructions (products, coproducts, pushouts) that appear in both treatments
- `artifacts/adversarial-committees.md` — practitioner-facing description
- `agent/roster.md` — character definitions and propensities

## Key Claims

1. **Propensities are selection functions, not utility functions.** Characters are not utility-maximizers; their "utility" is fidelity to their epistemic lens. This connects to Hedges's observation that open games require only a selection function, not expected utility.

2. **Rubric design is mechanism design.** The evaluation rubric is literally the continuation function k in the open games sense. Changing the rubric changes the equilibrium behavior of the committee.

3. **The fan and funnel are strategically coupled.** The backward-flowing evaluation signal means scenario narrators are best-responding to the committee: good scenarios are ones that, when deliberated, surface genuine fault lines.

4. **The composed pipeline may be a dependent lens.** The scenario-set (fan output) is indexed by the assumption space; the committee deliberates across scenarios. This suggests dependent optics as the right formalism, connecting to current Cybercat work.

## Status

**Early-stage bridge document.** The translation is laid out but several open questions remain:

- What selection function type formally captures propensity-driven play?
- What equilibrium notion characterizes coverage of the problem manifold rather than utility maximization?
- Is the fan/funnel composition a lens, a dependent lens, or something else?
- Does the calibration register provide empirical access to the continuation function?

These are research questions for the ACT community, not items that need resolution before the document is useful. The document is ready to serve as a point of contact for formal collaboration.
