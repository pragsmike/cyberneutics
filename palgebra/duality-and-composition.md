# Duality and Composition: The Fan, the Funnel, and the Decision Monad

## Motivation

The adversarial committee pipeline formalized in [committee-as-palgebra.md](committee-as-palgebra.md) is a **convergent** operation: multiple perspectives collapse into a single resolution. This document formalizes its categorical dual — **scenario generation** — as a divergent operation, then shows what happens when you compose them.

The payoff: the composed operation converts ambiguity into justified commitment. The composition has the structure of a **monad**, which gives us formal quality criteria (the monad laws) and a theory of iteration (running the monad repeatedly to map decision landscapes). The iteration connects to [residuality theory](../wild/residuality-theory/README.md) and to the Deleuzian "repetition produces difference" insight from [Essay 06](../essays/06-deleuze-difference-repetition.md), grounding both in operational pipeline algebra.

This document parallels [committee-as-palgebra.md](committee-as-palgebra.md) in structure. That document formalizes one half of the duality (the funnel). This document formalizes the other half (the fan), the composition, and what the composition reveals.

---

## The duality

Two operations. Same formalism, dual topology.

### The funnel: committee deliberation (product / many-to-one)

The adversarial committee takes a charter, a roster of characters with divergent propensities, and a set of inputs — and produces a single resolution. This is **convergent**: multiple independent perspectives are combined into one commitment.

- **Projections**: any aspect of the resolution traces back to which character's perspective drove it.
- **Universal property**: the resolution is the most specific commitment all members could endorse. Any weaker consensus that satisfies all members factors through it.
- In string diagram language: a **many-to-one spider** (comultiplication).

The full formalization is in [committee-as-palgebra.md](committee-as-palgebra.md). The key signature:

```
charter × scenario-set × roster × character-propensities × roberts-rules → transcript  [Deliberate]
  {catalytic: character-propensities, roberts-rules}
```

### The fan: scenario generation (coproduct / one-to-many)

Scenario generation takes a single ambiguous situation and produces multiple distinct narratives, each exploring different assumptions, character weightings, or external shocks. This is **divergent**: one input is injected into multiple narrative contexts.

- **Injections**: each assumption-set is embedded into narrative form as a distinct scenario.
- **Universal property**: any downstream process that needs to handle all possible futures can be defined by specifying how it handles each scenario independently.
- In string diagram language: a **one-to-many spider** (multiplication).

The key signature:

```
situation × scenario-roster × scenario-parameters → scenario-set  [Fan]
  {catalytic: scenario-roster, scenario-parameters}
```

### The symmetry

| Property | Funnel (Committee) | Fan (Scenarios) |
|----------|-------------------|-----------------|
| Direction | Many → One | One → Many |
| Purpose | Convergence: commit | Divergence: explore |
| Categorical role | Product (with projections) | Coproduct (with injections) |
| Spider topology | Comultiplication | Multiplication |
| Guards against | Indefinite deferral | Premature convergence |
| Failure mode | Anchoring on first framing | Storytelling without selection |
| Roster function | Adversarial stress-test | Narrative exploration |
| Bruner mode | Paradigmatic (System 2, rule-governed) | Narrative (System 1, associative) |

Neither operation alone is sufficient. Scenarios without selection is storytelling — creative but uncommitted. Committee without scenario exploration risks anchoring on the first framing. The composed operation is where decision-making happens.

---

## New types

The fan operation introduces types not present in the committee pipeline. Together with the existing types, these form the complete vocabulary for composed pipelines.

| Type | Description | Palgebra status |
|------|-------------|-----------------|
| `situation` | Description of a wicked problem or ambiguous decision context. Input to the fan. | **New.** Needs (template, rubric) pair. |
| `scenario` | A narrative arc exploring one possible future under stated assumptions. | **New.** Needs (template, rubric) pair. |
| `scenario-set` | An indexed collection of scenarios with explicitly divergent assumptions. The index set is the assumption-space. | **New.** Coproduct structure. |
| `scenario-roster` | Named characters with roles and propensities designed for divergent exploration. Distinct from the committee roster. | **New.** To design. |
| `scenario-parameters` | Assumption axes, external shocks, time horizons. Parameterizes the fan's divergence. | **New.** Catalytic. |
| `variance-report` | Comparison across multiple runs of a composed pipeline; identifies stable decisions, fault lines, sensitivity. | **New.** Output of Probe. |
| `decision-landscape-map` | Topological summary: basins of attraction, ridges, load-bearing assumptions. Synthesized from variance report. | **New.** Output of Map. |

Existing types (`charter`, `roster`, `transcript`, `resolution`, `evaluation`, `remediation`) are defined in [committee-as-palgebra.md](committee-as-palgebra.md) and remain unchanged.

### Type relationships

The `situation` type sits upstream of both fan and funnel. A situation can be chartered directly (as in the existing committee pipeline: `problem-statement → charter`) or fanned first into scenarios that then feed a committee. The choice of which path to take depends on whether the problem's ambiguity is primarily about *what might happen* (fan first) or *what to do given what we know* (committee directly).

The `scenario-set` is a coproduct type: it holds N distinct scenarios indexed by their assumption-sets. When the committee receives a scenario-set as input, it deliberates across all scenarios simultaneously — weighing which futures are most critical, which actions are robust across scenarios, and where the fault lines lie.

---

## Resource equations: the fan operation

```
# ── Phase 0: Situation Framing ──────────────────────────────────
# The user's raw problem description is structured into a situation
# with explicit ambiguity markers: what is uncertain, what
# assumptions could diverge, what external factors might intervene.

raw-problem → situation  [FrameSituation]


# ── Phase 1: Scenario Generation (the fan) ──────────────────────
# The core divergent operation. The situation, combined with the
# scenario roster and parameters, produces a set of distinct
# scenarios. Each scenario is a narrative exploring one possible
# future under stated assumptions.
#
# The scenario roster and parameters are catalytic — they shape
# the fan's divergence without being consumed. The scenario roster
# provides narrative lenses (characters whose worldviews generate
# distinct futures). The parameters specify axes of divergence
# (what assumptions to vary, what shocks to consider).

situation × scenario-roster × scenario-parameters → scenario-set  [Fan]
  {catalytic: scenario-roster, scenario-parameters}


# ── Phase 2: Scenario Assessment ────────────────────────────────
# Each scenario in the set is enriched with metadata: internal
# consistency, assumption clarity, narrative completeness, coverage
# of the divergence axes. This is an enrichment morphism —
# scenarios are scored but not altered.

scenario-set × scenario-rubric → scenario-set  [AssessScenarios]
  {catalytic: scenario-rubric; enriches: scenario-scores}


# ── Phase 3: Coverage Gate ──────────────────────────────────────
# The scored scenario set is checked for coverage: do the scenarios
# collectively span the divergence axes? Are there assumption
# combinations not represented? This gate may route back to
# regeneration (add a scenario) or forward to the funnel.

scenario-set × coverage-criteria → adequate-set + gaps-identified  [CoverageGate]
  {catalytic: coverage-criteria}
```

### Catalytic inputs

| Catalytic input | What it is | Role |
|-----------------|------------|------|
| `scenario-roster` | Characters designed for divergent exploration | Each tells a coherent story from their own worldview — not arguing with each other but generating distinct futures |
| `scenario-parameters` | Axes of divergence, external shocks, time horizons | Constrains the fan's output space — ensures scenarios diverge along specified dimensions rather than drifting randomly |
| `scenario-rubric` | Quality criteria for individual scenarios | Internal consistency, assumption clarity, narrative completeness |
| `coverage-criteria` | Quality criteria for the set as a whole | Collective coverage of the assumption space, presence of worst-case and best-case anchors |

### Two distinct rosters

The committee roster (defined in `agent/roster.md`) is designed for **convergent stress-testing**: devil's advocate, evidence checker, historian, opportunity scout, systems analyst. Each character's propensity creates productive friction in debate.

The scenario roster is designed for **divergent exploration**: each character generates a distinct, internally consistent future. They don't argue with each other — they generate independently. The divergence comes from their different worldviews, not from adversarial interaction.

| Roster | Operation | Character function | Interaction mode |
|--------|-----------|-------------------|-----------------|
| Committee roster | Funnel (convergent) | Stress-test through adversarial debate | Characters argue, challenge, cross-examine |
| Scenario roster | Fan (divergent) | Explore through independent narrative generation | Characters narrate independently, each from their own worldview |

The scenario roster's composition is an **open design question** (see Open Questions below). The committee roster's composition is documented in `agent/roster.md` and `artifacts/character-propensity-reference.md`.

---

## The composed operation: the deliberated choice

Composing fan → funnel yields a **single-input, single-output** operation:

```
situation → resolution  [DeliberatedChoice]
```

The input is an ambiguous situation. The output is a decision with a rationale. What the composition does: **converts ambiguity into commitment**.

### Full resource equations for the composed pipeline

```
# ── Fan half ────────────────────────────────────────────────────
raw-problem → situation  [FrameSituation]
situation × scenario-roster × scenario-parameters → scenario-set  [Fan]
  {catalytic: scenario-roster, scenario-parameters}
scenario-set × scenario-rubric → scenario-set  [AssessScenarios]
  {catalytic: scenario-rubric; enriches: scenario-scores}
scenario-set × coverage-criteria → adequate-set + gaps-identified  [CoverageGate]
  {catalytic: coverage-criteria}

# ── Bridge: charter the committee using the scenario set ────────
adequate-set → charter  [DraftCharter]

# ── Funnel half (abbreviated; full equations in committee-as-palgebra.md) ──
charter × character-propensities → roster + convening  [Convene]
  {catalytic: character-propensities}
charter × roster × convening × adequate-set × character-propensities × roberts-rules → transcript  [Deliberate]
  {catalytic: character-propensities, roberts-rules}
transcript × charter → resolution  [Resolve]  {catalytic: charter}

# ── Evaluation (same as committee pipeline) ─────────────────────
transcript × evaluation-rubrics × charter → evaluation  [Evaluate]
  {catalytic: evaluation-rubrics, charter}
evaluation × remediation-threshold → passed-evaluation + needs-remediation  [QualityGate]
  {catalytic: remediation-threshold}
needs-remediation × transcript × character-propensities → remediation + transcript  [Remediate]
  {catalytic: character-propensities}

# ── Human gate ──────────────────────────────────────────────────
passed-evaluation × resolution → accepted-resolution + rejected-resolution  [HumanGate]
  {discard: rejected-resolution}
```

Note a key structural difference from the standalone committee pipeline: the Deliberate operation now receives `adequate-set` (the scenario collection) as input alongside the charter. The committee doesn't just debate a problem statement — it debates *across scenarios*, weighing which futures matter most and which actions are robust across them. The scenarios are consumed by the deliberation (their content is folded into the transcript) but the scenario roster and parameters that generated them are not.

### What the composition guarantees

The **fan** ensures the possibility space has been genuinely explored. It guards against premature convergence — the committee can't anchor on the first framing because multiple framings have been generated before deliberation begins.

The **funnel** ensures a commitment has actually been made. It guards against indefinite deferral — the scenarios don't just sit as interesting stories; they are evaluated, debated, and resolved.

The **evaluation loop** ensures quality. The same feedback mechanism from the committee pipeline (evaluate → quality gate → remediate) applies to the composed output.

---

## The monad structure

If the fan (free exploration) is left adjoint to the funnel (constrained selection), their composition yields a **monad** — the algebraic structure of "wrap in computational context, do work, extract result."

### The monad in brief

The decision monad M is the composition Fan ∘ Funnel:

```
M(situation) = Funnel(Fan(situation))
```

A single application of M: take a situation, fan it into scenarios, funnel the scenarios into a resolution. The resolution is a committed decision with traced rationale.

### The monad laws as quality criteria

The monad laws (unit, associativity) are not abstract requirements — they are **operational quality tests** for the pipeline.

**Unit law**: `Fan → immediate Funnel without real deliberation ≈ identity`

If you fan a situation into scenarios and then immediately collapse without genuine deliberation — without adversarial challenge, without evidence demands, without the committee's characteristic friction — you should get back approximately the same situation you started with. The pipeline added nothing.

*Operational test*: Run the composed pipeline with a trivially short deliberation (one round, no challenges). If the resolution is substantively different from the original situation framing, something in the pipeline is injecting content that didn't come from genuine deliberation. This tests whether the scaffold is load-bearing or just decorative.

**Associativity**: `M(M(situation)) ≈ M(situation)` — nested fan-collapse-fan-collapse should be equivalent to a single well-designed fan-collapse.

If you fan, funnel, then fan *the resolution* and funnel again, you should get a result equivalent to fanning more broadly in the first pass and funneling once. Nested application should not produce qualitatively different decisions than single application — it should just explore more thoroughly.

*Operational test*: Run M twice (fan → funnel → fan the resolution → funnel again). Compare the final resolution with a single-pass M where the initial fan was broader (more scenarios, more divergence axes). If the nested version produces qualitatively different conclusions, the single-pass fan wasn't broad enough — it missed scenario regions that the second fan found by exploring from the resolution's vantage point.

*When the law fails informatively*: Associativity failure isn't always a defect. If M(M(x)) ≠ M(x), the second application found something the first missed. The *pattern* of failure is diagnostic: it reveals which regions of the decision space were invisible from the original situation framing but became visible after the first resolution shifted the observer's position. This is the cybernetic loop in action — observation changes state, and the new state reveals new territory.

### Kleisli interpretation

In the Kleisli category of the decision monad, each pipeline operation is a Kleisli arrow:

```
f : Situation → M(Resolution)
```

where M captures the nondeterminism of LLM generation. Each invocation actualizes one trajectory through the distribution of possible deliberations. The monad's bind operation (>>=) is: "take a resolution, use it to frame a new situation, and deliberate again."

This connects to the Kleisli category discussion in [decorated-texts.md](decorated-texts.md) (Related Work section): the decision monad is a *specific* monad layered on top of the general nondeterminism monad that all LLM pipeline operations inhabit. It adds the expand-evaluate-commit structure to the underlying stochasticity.

---

## Iteration: the Deleuzian walk

Running the composed pipeline multiple times from the same premises is a **stability test**. Each run is an architectural walk (in [residuality theory](../wild/residuality-theory/README.md) terms) through the decision space. The walks are never identical — each actualizes a different trajectory through the stochastic pipeline — and the differences between walks reveal structure.

### The Probe operation

```
(situation → resolution)^N → variance-report  [Probe]
```

Run the composed fan → funnel pipeline N times on the same situation. Collect the N resolutions. Compare them.

### Sources of instability

When repeated runs produce different resolutions, the instability has three possible sources, each with different implications:

| Source | What it means | Intervention |
|--------|---------------|-------------|
| **Situation framing** | The premises underdetermine the possibility space; different runs interpret the input differently | Tighten the situation description — it doesn't inhabit its type tightly enough |
| **Parameters** | Small perturbations in assumptions or character propensities flip outcomes; identifies load-bearing assumptions | Sensitivity analysis — which assumptions are the ridge the decision sits on? |
| **Operational noise** | LLM stochasticity not washing out; temperature effects, presentation order, anchoring | Engineering fix: lower temperature, randomize order, increase N |

The variance report should distinguish these sources. The first two are *findings* — they tell you something about the decision space. The third is *noise* — it tells you something about the pipeline's engineering.

### Residues and eigenforms

The distinction from [residuality theory](../wild/residuality-theory/README.md) is precise and useful here:

- A **residue** is what a single run leaves behind — the resolution, the key tensions, the surfaced assumptions. It is the output of one architectural walk through the problem space.
- An **eigenform** is what persists across all runs — the decision (or tension, or assumption) that every walk discovers. It is a fixed point of the pipeline: `M(x) = x` — running the pipeline on this input reproduces it.

The remediation feedback loop within a single run (`Evaluate → QualityGate → Remediate → Evaluate`) hunts for eigenforms *within* a run — framings that stabilize under recursive self-assessment. The Probe operation hunts for eigenforms *across* runs — decisions that stabilize under repeated independent execution.

Stable outputs (eigenforms) indicate a well-determined decision landscape — the basin of attraction is broad and the decision is robust. Unstable outputs (multiple distinct residues) indicate you're near a **ridge** — a boundary between basins where small changes flip outcomes. The ridge is the most important thing to understand before committing.

### The Map operation

```
variance-report → decision-landscape-map  [Map]
```

Synthesize the N-run comparison into a topological summary:

- **Basins of attraction**: which decisions recur? With what frequency?
- **Ridges**: where do decisions diverge? Which assumptions correlate with which outcomes?
- **Load-bearing assumptions**: which parameter changes flip the basin? These are the assumptions that deserve the most scrutiny.
- **Robust actions**: which actions appear in resolutions across multiple basins? These are safe commitments even under decision-landscape uncertainty.

The decision landscape map is the operational deliverable of the Probe — the thing the human editor uses to make a final commitment.

---

## Composable pipeline patterns

The fan, funnel, and their compositions generate a family of reusable pipeline patterns:

| Pattern | Composition | Purpose |
|---------|-------------|---------|
| **Deliberated Choice** | Fan → Funnel | Convert ambiguity into justified commitment (the decision monad) |
| **Evaluated Choice** | Fan → Funnel → Evaluate | Deliberated choice with independent quality check |
| **Stress-Tested Choice** | (Fan → Funnel)^N → Probe → Map | Repeated deliberated choice with variance analysis |
| **Cascaded Exploration** | Fan → Funnel → Fan | "We chose A; now what might go wrong with A?" — the monad's bind |
| **Remediation Loop** | Funnel → Evaluate → Remediate → Evaluate → ... | Convergent refinement within a single run (bounded trace) |
| **Nested Fan** | Fan → (Fan per scenario) | Sub-branching within each scenario; decision tree exploration |

The first three are the primary use cases. Deliberated Choice is the default. Evaluated Choice adds a quality check. Stress-Tested Choice is for high-stakes decisions where understanding the decision landscape matters more than any single resolution.

Cascaded Exploration is the monad's bind operation made explicit: take a resolution, use it as the situation for a new fan, and explore what might go wrong with the chosen course. This is iterable — each cascade reveals second-order consequences.

### Confidence propagation through composition

The [three propagation rules](reference.md) apply to the composed pipeline:

**Confidence can only degrade.** A Medium-confidence scenario set cannot produce a High-confidence resolution, regardless of committee quality. The fan sets the ceiling. This means scenario quality — coverage, internal consistency, assumption clarity — is the binding constraint on the composed pipeline's output quality.

**Provenance can only accumulate.** The resolution from a Deliberated Choice carries provenance from both the fan (which scenarios were generated, from what assumptions) and the funnel (which characters debated, what evidence was demanded). The full chain of custody is richer than either operation alone.

**Content transforms.** The situation becomes scenarios becomes a transcript becomes a resolution. Each stage produces genuinely new content. The pipeline's topology determines the path content takes through the system.

---

## What the composition reveals

Formalizing the duality and composition makes several things visible that the procedural descriptions obscure:

1. **The fan is the committee's missing input.** The standalone committee pipeline starts from a `problem-statement` that goes directly to chartering. The fan provides the exploration that the problem statement assumes has already happened. When the committee receives a scenario set rather than a bare problem statement, it deliberates across *genuinely explored* possibilities rather than whatever framing the user happened to start with.

2. **The two rosters serve dual functions.** The committee roster creates convergent friction (characters argue). The scenario roster creates divergent exploration (characters narrate independently). This is not the same function applied twice — it is two genuinely different operations on the problem space. Conflating them (using the committee roster for scenario generation, or vice versa) collapses the duality and loses the composition's power.

3. **The monad laws are testable quality criteria.** Unit: does the pipeline add value beyond its scaffold? Associativity: does a single broad pass match nested narrow passes? These are not philosophical musings — they are operational tests you can run and learn from.

4. **Iteration maps topology, not just quality.** The existing remediation loop improves a single run. Probe/Map reveals the *structure* of the decision space across runs. These serve different purposes and should not be conflated. Remediation asks "is this specific deliberation good enough?" Probe asks "is the decision landscape well-understood?"

5. **Residues and eigenforms are distinct observables.** A single run produces a residue (what this walk left behind). Multiple runs reveal eigenforms (what every walk finds). The remediation loop within a run hunts for local eigenforms. Probe hunts for global eigenforms. The distinction between local and global fixed points is the distinction between "locally coherent" and "robustly correct" — exactly the gap that the adversarial committee was designed to address.

---

## Open questions

These are documented here for intellectual honesty and to guide future work. None blocks the implementation of the fan operation or the basic composition.

### 1. Scenario roster composition

What archetypes serve divergent exploration? The committee roster's design is grounded in adversarial epistemology (devil's advocate, evidence checker, etc.). The scenario roster needs a different design principle — characters whose worldviews generate maximally diverse futures.

Candidates from scenario planning literature (Schwartz, van der Heijden): optimist/pessimist/wildcardist is too generic. Domain-specific lenses (technologist, regulator, incumbent, disruptor) are more promising but less portable. Worldview-based lenses (individualist, egalitarian, hierarchist, fatalist — from Cultural Theory) have theoretical backing but may be too abstract.

The answer may be that the scenario roster is **problem-dependent** (unlike the committee roster, which is fixed). If so, the FrameSituation operation needs to include roster selection as part of its output.

### 2. Variance report structure

What format captures "three runs gave A, two gave B, and here's what differed"? The report needs to surface:
- The decisions themselves (what was resolved in each run)
- The assumptions/framings that correlated with each outcome
- Which instability sources (situation, parameters, noise) drove the divergence
- A compact summary suitable for human editorial review

### 3. Decision landscape map representation

How to represent basins of attraction and ridges in a way that's actionable? Options: string diagrams showing branching points, tables comparing assumptions to outcomes, narrative summaries of "if X then Y, if not-X then Z." Likely a combination.

### 4. Monad laws as operational tests

Can we operationalize the unit and associativity laws as executable checks? The unit test (trivial deliberation ≈ identity) seems straightforward. The associativity test (nested M ≈ single broad M) is harder — "equivalent" is not "identical" for stochastic pipelines. We may need a similarity metric for resolutions.

### 5. Remediation cap and eigenform depth

Is 2 rounds of remediation sufficient to distinguish local fixed points from robust eigenforms? Residuality theory suggests you need enough walks to see the topology. The current cap (2 rounds) may be appropriate for *within-run* quality (where you're refining a specific deliberation), while *across-run* exploration (Probe) handles the broader topology question. If so, the cap isn't a limitation — it's a separation of concerns: remediation fixes this run; Probe maps the landscape.

### 6. Interaction between rosters

Can scenario characters feed into committee characters? ("Scenario character X's future is the one Maya finds most threatening.") This cross-pollination between the dual operations might be a mechanism for richer composition — the fan's output shapes not just what the committee debates but *how* the committee members engage. This would make the scenario set not just an input to Deliberate but a modifier of the catalytic character-propensities input. Formally, this would mean character-propensities are no longer purely catalytic — they become partially shaped by the fan's output. The implications for pipeline stability need careful analysis.

---

## Connections

This document extends the following:

- **[Committee as Palgebra](committee-as-palgebra.md)** — formalizes the funnel half; this document formalizes the fan half and the composition
- **[Palgebra Reference](reference.md)** — provides the notation; spider (fan/funnel) patterns should be added to the reference
- **[Decorated Texts](decorated-texts.md)** — develops the underlying formalism; the Kleisli category discussion connects to the decision monad

This document connects to the following essays:

- **[Essay 06: Deleuzian Foundations](../essays/06-deleuze-difference-repetition.md)** — "Repetition produces difference" is the philosophical ground for the Probe operation
- **[Essay 04: Cybernetics and the Observer](../essays/04-cybernetics-and-observation.md)** — eigenforms are what the Probe hunts for; the human gate is where observation collapses the eigenform
- **[Essay 07: Narrative Engineering](../essays/07-bolands-narrative-engineering.md)** — Bruner's narrative/paradigmatic modes map to fan/funnel
- **[Essay 08: Methodology to Formalism](../essays/08-from-methodology-to-formalism.md)** — the bridge essay; the decision monad extends its Section 2 (traced monoidal structure) and Section 3 (transformation morphisms and Deleuzian difference)
- **[Essay 09: Narrative Immune Systems](../essays/09-narrative-immune-systems.md)** — the fan is antigen presentation; the funnel is immune response; Probe is affinity maturation

This document draws on:

- **[Residuality Theory](../wild/residuality-theory/README.md)** — architectural walks, residues vs. eigenforms, process over substance
- **Diary entry 2026-02-21** — the improvisational conversation that generated the initial inventory of types, operations, and patterns formalized here
