# The Adversarial Committee as an Open Game

*A translation of the cyberneutics committee structure into the language
of compositional game theory (Ghani, Hedges, Winschel, Zahn 2018 and
subsequent work). Intended as a bridge document for the ACT /
Cybercat community. Cross-reference: `palgebra/committee-as-palgebra.md`
for the resource-theoretic treatment of the same structure.*

---

## Motivation

The cyberneutics adversarial committee is a multi-agent deliberative
architecture for decision-making under uncertainty. Five characters —
Maya, Frankie, Joe, Vic, Tammy — each with fixed propensities and
incompatible priors, deliberate over a chartered problem and produce a
justified resolution. The committee's value is not (primarily) that it
produces better answers than a single agent; it is that it produces
*inspectable reasoning* with a traceable justification chain.

Palgebra (the resource-theoretic formalism for this system) describes
the committee as a many-to-one funnel: five character-inputs converge
via a `Deliberate` transformation morphism to a single transcript,
then resolved by a `Resolve` enrichment morphism. This is structurally
correct but loses the strategic dimension — the characters are not just
inputs; they are *agents* with propensities that determine how they
respond to each other and to the problem context.

Open games recover that strategic dimension. They are the right language
for asking: what constitutes a well-played committee deliberation? What
does equilibrium mean here? What is the analogue of a Nash equilibrium
in a committee that aims at justified commitment rather than utility
maximization?

---

## 1. Open Games: Brief Recapitulation

An open game `G : (X, S) → (Y, R)` has four ports:

- **X** — covariant input: what the game *observes* (the "history",
  what happened before)
- **Y** — covariant output: what the game *produces* (the "play",
  actions taken)
- **R** — contravariant input: utility returned *from* the downstream
  environment (what the future says about the quality of the play)
- **S** — contravariant output: coutility returned *upstream* to the
  past environment (the game's contribution to prior utility)

A concrete open game consists of:
- A **strategy set** Σ
- A **play function** `P : Σ × X → Y`
- A **best-response function** `B : Σ × X × (Y → R) → 𝒫(Σ)` — given
  a context `(x : X, k : Y → R)`, returns the set of strategies that
  are best responses to that context

A **context** for G is a pair `(x, k) : X × (Y → R)`: a history x
and a continuation k that converts plays into outcomes. The best-response
function is always evaluated relative to a context.

A **selection equilibrium** is a strategy profile σ such that each
component's strategy is a best response to the context induced by
the others playing their equilibrium strategies.

Open games compose:
- **Sequentially** (categorical composition): G then H, where G's
  output becomes H's input
- **In parallel** (monoidal product ⊗): G and H played simultaneously,
  each observing only their own inputs

---

## 2. Typing the Committee

### 2.1 Types

Let the following types be fixed:

| Symbol | Type | Description |
|--------|------|-------------|
| X | `Charter` | The chartered problem: question, constraints, success criteria |
| Σᵢ | `Strategy(i)` | Character i's strategy set — all possible positions, arguments, votes |
| Y | `Transcript` | The full record of the deliberation |
| R | `EvaluationScore` | Downstream quality signal: rubric scores from the evaluator |
| S | `Coutility` | Upstream signal: how much the committee's deliberation contributed to justified commitment |

The committee as a whole is an open game:

```
Committee : (Charter, Coutility) → (Transcript, EvaluationScore)
```

In Hedges notation: `Committee : (X, S) → (Y, R)`.

### 2.2 The Five Player Games

Each character i ∈ {Maya, Frankie, Joe, Vic, Tammy} is itself an open
game:

```
Playerᵢ : (Charter × Transcript_<i, Coutilityᵢ) → (Positionᵢ, EvaluationScoreᵢ)
```

Where `Transcript_<i` is the transcript of all prior speech acts (in
sequential deliberation, this is the history visible to character i at
the point they speak).

The **strategy set** Σᵢ for character i is the set of all positions,
arguments, challenges, motions, and votes consistent with their
propensity. Crucially, this strategy set is not arbitrary — it is
constrained by the character's propensity:

- **Maya's** strategy set is concentrated on arguments that surface
  political risk, misaligned incentives, and hidden agendas. She cannot
  play Frankie's strategies (values-based appeals) without violating her
  propensity.
- **Frankie's** strategy set is concentrated on arguments that invoke
  mission, principle, and normative commitments.
- **Joe's** strategy set foregrounds historical precedent and
  institutional memory.
- **Vic's** strategy set demands falsifiable claims and quantified
  evidence.
- **Tammy's** strategy set surfaces feedback loops, second-order effects,
  and systemic complexity.

**The propensity is a constraint on the strategy set, not a utility
function.** This is the key departure from standard game theory: the
characters are not utility-maximizers in the economic sense. Their
"utility" is fidelity to their lens — successfully playing their
epistemic role in the deliberation.

### 2.3 The Play Function

For character i, the play function is:

```
Pᵢ : Σᵢ × (Charter × Transcript_<i) → Positionᵢ
```

It takes a strategy (a particular argumentative stance consistent with
the propensity) and the visible history (charter + prior speech acts),
and produces a position: a speech act in the deliberation.

The **chair** (the orchestrating process, not one of the five characters)
enforces Robert's Rules — the procedural structure that determines whose
turn it is, what motions are on the table, and when voting occurs. The
chair is not a player in the game-theoretic sense; it is the *category
structure* — the composition rule that sequences the individual player
games.

### 2.4 The Best-Response Function and Equilibrium

For character i, the best-response function is:

```
Bᵢ : Σᵢ × (Charter × Transcript_<i) × (Positionᵢ → EvaluationScoreᵢ) → 𝒫(Σᵢ)
```

Given a context `(charter, prior_transcript, k)` where `k : Positionᵢ
→ EvaluationScoreᵢ` is the continuation that will evaluate i's
contribution, `Bᵢ` returns the set of strategies that are best
responses — i.e., positions that best fulfill the character's propensity
given the context.

**What is "best" for a committee character?** Not utility maximization
in the Nash sense, but something closer to *epistemic integrity*: the
best strategy for Maya is the one that most faithfully exercises
paranoid realism given the charter and the prior arguments — the
strategy that surfaces the political risks that would most likely be
missed without her lens.

A **committee equilibrium** is a strategy profile `(σ_Maya, σ_Frankie,
σ_Joe, σ_Vic, σ_Tammy)` such that:

1. Each character's strategy is a best response to the context induced
   by the others playing their equilibrium strategies
2. No character can better fulfill their propensity by unilaterally
   switching strategies
3. The resulting transcript covers the problem manifold (all five
   epistemic perspectives have been genuinely brought to bear)

**Note**: A committee equilibrium is *not* consensus. It is a fixed
point of the mutual best-response correspondence where each character
is playing their lens faithfully. The transcript at equilibrium is
likely to contain unresolved disagreements — that is expected and
desirable. The resolution (justified commitment) is a separate operation
performed on the equilibrium transcript.

---

## 3. The Committee as a Tensor Product

The five player games run simultaneously in Stage 2 (independent
positions) and sequentially in Stage 3 (cross-examination). This maps
cleanly onto the two composition operations in open games:

### 3.1 Stage 2: Tensor (Parallel Play)

In Stage 2, each character produces their opening position
independently, without seeing the others:

```
Stage2 = Maya_game ⊗ Frankie_game ⊗ Joe_game ⊗ Vic_game ⊗ Tammy_game
```

This is monoidal product composition. Each character observes only the
charter (shared input), and their positions are generated independently.
The strategy profile for Stage 2 is a product: `Σ_Maya × Σ_Frankie ×
Σ_Joe × Σ_Vic × Σ_Tammy`.

The independence of Stage 2 is not incidental — it is the *design
intent*. Running characters as separate model instances (the preferred
execution mode in Pattern D of the implementation) is the operational
realization of genuine tensor product structure: no shared context
window, no cross-contamination.

### 3.2 Stage 3: Sequential Composition (Cross-Examination)

In Stage 3, each character sees the full set of opening positions and
responds. The structure is sequential: the cross-examination of
character i is an open game that receives the Stage 2 transcript as
input (covariant) and produces a refined position as output. Characters
are played sequentially, and each sees the responses of those who went
before.

This is categorical composition (sequential):

```
Stage3 = Cross_Maya ; Cross_Frankie ; Cross_Joe ; Cross_Vic ; Cross_Tammy
```

(with the semicolon denoting sequential composition). The order within
Stage 3 is a design parameter — in practice it may be run in parallel
with all five characters seeing the same Stage 2 transcript, which
returns to tensor product structure at the Stage 3 level.)

### 3.3 The Full Committee Game

The committee is the sequential composition of Stage 2 and Stage 3,
followed by the Resolve operation (which is not a player game but a
deterministic collapse):

```
Committee = Stage2 ; Stage3 ; Resolve
```

Where `Resolve : Transcript → Resolution` is the chair's operation of
distilling the equilibrium transcript into a justified commitment.
`Resolve` is not itself a game — it is the morphism that closes the
deliberation.

---

## 4. Context and the Evaluation Signal

The **context** for the committee game is the pair:

```
(charter : Charter, k : Transcript → EvaluationScore)
```

The continuation `k` is the downstream evaluator: a fresh model instance
(or human reviewer) that scores the transcript against explicit rubrics.
This is the *evaluation morphism* in palgebra terms, and the
*continuation function* in open games terms.

The evaluator's rubric scores flow backward through the game:

- The evaluator scores the transcript (R = EvaluationScore)
- This score is the contravariant input to the Committee game
- The committee's coutility (S) is the degree to which its deliberation
  contributed to a resolution that would survive the evaluator's scrutiny

**This is where the open games framework adds something the resource-
theoretic treatment does not directly capture**: the backward-flowing
evaluation signal is not an afterthought — it is constitutive of what
it means for each character to play well. Maya's best response depends
on what the evaluator will score highly; an evaluator that rewards
political insight will elicit more of Maya's best work. The evaluation
rubric is literally the continuation function k, and changing it changes
the equilibrium.

This has a practical implication: rubric design is mechanism design.
The rubrics determine the equilibrium behavior of the committee.

---

## 5. The Fan as a Prior Game

The fan operation (scenario generation) that precedes the committee in
the full deliberated-choice pipeline is itself an open game:

```
Fan : (Situation, FanCoutility) → (ScenarioSet, ScenarioScore)
```

With four narrators as players (a parallel tensor product), each
observing the situation and generating a scenario from their worldview.

The composed pipeline — Fan ; Committee — is then a sequential
composition of two open games:

```
DeliberatedChoice : (Situation, Coutility) → (Resolution, EvaluationScore)
```

The scenario set produced by the Fan becomes the covariant input to
the Committee (augmenting the charter). The evaluation signal flows
backward through both games: the resolution's quality score propagates
back through the committee's coutility into the fan's coutility, which
tells the scenario generators whether their scenarios adequately covered
the decision-relevant possibility space.

**The fan narrators are best-responding to the committee**: good
scenarios are ones that, when deliberated by the committee, surface
genuine fault lines and produce robust commitments. This backward signal
— which in palgebra is implicit in the pipeline structure — is explicit
in the open games treatment. The Fan and Committee games are
strategically coupled through their shared context.

---

## 6. Equilibrium vs. Resolution: A Key Distinction

A **committee equilibrium** (in the game-theoretic sense) is a state
where no character can better fulfill their propensity by unilaterally
changing their strategy. This is a property of the *deliberation
process*.

A **resolution** is the output of the `Resolve` operation applied to
the equilibrium transcript. This is a *product* of the deliberation —
the justified commitment.

These are distinct. The committee can reach equilibrium (no character
has a better move) while still producing a transcript that the Resolve
operation must interpret. In a contentious case, the resolution may be:
"The committee is split; the majority position is X, with a significant
minority dissent from Maya on political grounds." That is still a
resolution — an honest characterization of the deliberation's outcome.

The calibration register (from the VSM / System 3* framing) is the
empirical track record that, over time, tells us which resolutions were
justified — that is, which equilibria were genuinely informative. This
is the temporal extension of the best-response structure: over a corpus
of deliberations, the register identifies which characters' equilibrium
strategies were most epistemically reliable.

---

## 7. Departure from Standard Game Theory

The committee is not a standard game in several respects that are worth
making explicit for an ACT audience:

1. **Non-utility-maximizing agents**. Characters are propensity-driven,
   not utility-maximizing in the economic sense. Their "utility" is
   fidelity to their epistemic lens. This may connect to behavioral
   game theory (prospect theory, satisficing) or to the weaker condition
   noted by Hedges: "the only requirement is that the decision criterion
   can be described by a selection function." The propensity *is* a
   selection function — it selects the strategies consistent with the
   character's epistemic role.

2. **No adversarial outcome competition**. The characters are not
   competing to win. They are competing to *surface* — each character's
   "winning" condition is that their perspective is genuinely heard and
   responded to, not that their preferred resolution is adopted. The
   committee equilibrium is reached when all perspectives have been
   brought to bear, not when one wins.

3. **The resolution is not the payoff**. In standard game theory, the
   payoff is determined by the outcome. Here, the resolution is an
   artifact produced by the Resolve operation; it is the *evaluator*
   that determines the payoff (via the rubric scores that flow
   backward). The characters' payoffs are mediated by the evaluation,
   not directly by the resolution's content.

4. **Propensities as catalytic constraints**. In palgebra, the character
   propensities are catalytic inputs — they participate in every
   operation without being consumed. In open games terms, the propensity
   constrains the strategy set Σᵢ but does not change as the game
   unfolds. This is a comonoid structure: the propensity can be copied
   (used in multiple stages) without depletion.

---

## 8. Connection to Dependent Optics

The recent Cybercat work on dependent optics suggests a further
translation worth pursuing. An open game `G : (X, S) → (Y, R)` is a
lens: the play function is the "view" direction (forward), the
best-response function incorporates the "update" direction (backward,
using the continuation k). The fan/funnel duality in palgebra has a
natural optics reading:

- **Fan (scenario generation)**: The "get" / view direction — projecting
  from a situation into the scenario space
- **Funnel (committee deliberation)**: The "put" / update direction —
  integrating the scenario-indexed perspectives back into a justified
  commitment

The composed DeliberatedChoice pipeline is then a lens whose forward
pass explores the possibility space and whose backward pass contracts it
into a resolution. The evaluation signal flowing backward is the update
function. This framing — cyberneutics as a lens — connects directly to
the dependent optics work at Cybercat and may be the most productive
point of contact for a formal collaboration.

---

## Open Questions

1. **What selection function type captures propensity-driven play?**
   The standard selection function `ε : (X → R) → X` selects an action
   given a continuation. The propensity-constrained character needs a
   selection function that additionally respects the propensity
   constraint. Is this a selection function in a subcategory? A
   constrained selection function? This needs a proper formal treatment.

2. **What is the right notion of equilibrium for a committee whose goal
   is coverage rather than utility maximization?** The intuition is that
   a committee equilibrium should be characterized by *coverage* of the
   problem manifold — all five epistemic charts have been applied — rather
   than by mutual best-response in the Nash sense. Is there a
   game-theoretic notion that captures this?

3. **Does the calibration register give us empirical access to the
   continuation function k?** Over a corpus of historical deliberations,
   the register accumulates data on which committee strategies produced
   resolutions that survived later evaluation. This is empirical
   estimation of the best-response function — which is to say, empirical
   mechanism design. The connection to Bayesian open games (Bolt, Hedges,
   Zahn 2019) may be productive here.

4. **Is the fan/funnel composition a lens, a dependent lens, or
   something else?** The scenario-set produced by the fan is not a
   simple type — it is indexed by the assumption space (a coproduct
   type). The committee deliberates *across* scenarios, which means the
   funnel's input type depends on the fan's output. This suggests
   dependent lenses as the right formalism, which connects to the
   dependent optics work.

---

*Cross-references: `palgebra/committee-as-palgebra.md` (resource-
theoretic treatment), `palgebra/duality-and-composition.md` (fan/funnel
duality and decision monad), `artifacts/adversarial-committees.md`
(practitioner-facing description), `agent/roster.md` (character
definitions). Primary sources: Ghani, Hedges, Winschel, Zahn (2018)
arXiv:1603.04641; Bolt, Hedges, Zahn (2019) arXiv:1910.03656; Hedges
(2016) PhD thesis.*
