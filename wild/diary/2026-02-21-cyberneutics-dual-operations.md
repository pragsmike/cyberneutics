# Diary: Cyberneutics, Dual Operations, and Decision-Making Under Uncertainty

**Date:** 2026-02-21
**Context:** Improvisational conversation exploring naming, category-theoretic structure of narrative computing operations, and their application to wicked problems. This entry captures ideas for future formalization in palgebra.

---

## 1. Naming Resolution

### The Stack

| Layer | Name | Role |
|-------|------|------|
| Discipline | **Narrative Computing** / **Narrative Engineering** | What the field is. "Narrative computing" names what the machine does; "narrative engineering" names how we compose machines into systems that do useful work. Public-facing, immediately legible. |
| Theoretical framework | **Cyberneutics** | Abbreviated form of **Cybernetic Hermeneutics**. Names the core insight: steering (cybernetics) and interpretation (hermeneutics) are inseparable when working with narrative engines. Echoes of *heuristics* and *neural* are felicitous. |
| Methodology | **Cyber-Sense** | The operational practice: adversarial committees, parliamentary procedures, RUBRIC evaluation, cross-scenario learning. |
| Formal substrate | **Palgebra** | The type system for texts: decorated texts, soft types as (template, rubric) pairs, pipeline composition. |

### Repository Rename

The repository was renamed from `cyber-sense` to `cyberneutics` on 2026-02-21. The previous name risked confusion with Dell/Quest's CyberSense data protection product. "Cyberneutics" is a neologism with zero existing competition in search results. Two known forks were notified.

---

## 2. Dual Operations: Fan and Funnel

A central structural insight emerged from considering two distinct skills — scenario generation and committee deliberation — as categorical duals.

### The Committee as Product (Funnel / Many-to-One)

The adversarial committee is a **convergent** operation. Multiple independent perspectives (Maya, Frankie, Joe, Vic, Tammy) are combined into a single resolution. This is product-like:

- **Projections**: Any aspect of the resolution can be traced back to which committee member's perspective drove it.
- **Universal property**: The resolution is the most specific commitment all members could endorse. Any alternative resolution that satisfies all members factors through this one.
- In string diagram language: a **many-to-one spider** (comultiplication).

### Scenario Generation as Coproduct (Fan / One-to-Many)

Scenario generation is a **divergent** operation. A single ambiguous situation is injected into multiple distinct narrative contexts, each exploring different assumptions, character weightings, or external shocks. This is coproduct-like:

- **Injections**: Each assumption-set is embedded into narrative form as a distinct scenario.
- **Universal property**: Any downstream process that needs to handle all possible futures can be defined by specifying how it handles each scenario independently.
- In string diagram language: a **one-to-many spider** (multiplication).

### Composition: The Deliberated Choice

Composing fan → funnel (scenarios → committee) yields a **single-input, single-output** operation: a **deliberated choice** (justified commitment). The input is an ambiguous situation. The output is a decision with a rationale.

What the composed operation does: **converts ambiguity into commitment**.

- The fan ensures the possibility space has been genuinely explored (guards against premature convergence).
- The funnel ensures a commitment has actually been made (guards against indefinite deferral).
- Neither alone is sufficient: scenarios without selection is storytelling; committee without scenario exploration risks anchoring on the first framing.

### Section and Stability

If the funnel is f: Many → One, a **section** s: One → Many satisfying f ∘ s = id would mean: for every decision, there's a canonical way to expand it back into the scenarios that justify it, and re-running the committee on those scenarios recovers the same decision. This is an **idempotence check** — a quality criterion for deliberated choices.

### Adjunction and Monad Structure

If the fan (free exploration) is left adjoint to the funnel (constrained selection), their composition yields a **monad** — the structure of "wrap in computational context, do work, extract result."

- **Unit law**: Fanning then immediately collapsing without real deliberation ≈ doing nothing.
- **Associativity**: Nested fan-collapse-fan-collapse ≈ single well-designed fan-collapse.

The composed operation is a **decision monad**: expand, evaluate, commit, with the property that commitment is stable under re-examination of the possibilities that generated it.

---

## 3. Repetition as Instrument: The Deleuzian Walk

Running the composed fan → funnel operation multiple times from the same premises is a **stability test**. Consistent outputs indicate a well-determined decision landscape. Inconsistent outputs are diagnostic — the *pattern* of variance reveals the topology of the decision space.

### Sources of Instability

| Source | What it means | Palgebra interpretation |
|--------|---------------|------------------------|
| **Formula** (situation description) | Premises underdetermine the possibility space; different runs interpret the same input differently | Input text doesn't inhabit its type tightly enough |
| **Parameters** (assumptions, character propensities, rubric weights) | Small perturbations in assumptions flip outcomes; identifies load-bearing assumptions | Sensitivity analysis on pipeline parameters |
| **Operations** (LLM temperature, presentation order, anchoring effects) | Stochastic noise not washing out; engineering problem | Operational noise in the pipeline; fix with lower temperature, randomization, multiple runs |

### Deleuze's Difference and Repetition

Repetition never produces the identical — it produces the *nearly* identical, and the gap between repetitions reveals structure. The differences aren't noise; they're the system showing its topology.

Running the operation five times and getting three A's and two B's means the decision landscape is **bistable**. The boundary between the basins of attraction — the ridge where small changes flip the outcome — is the most important thing to understand. The divergence *is* the finding.

### Operational Consequence

This suggests a third skill beyond `/scenarios` and `/committee`: a **`/probe`** or **`/stress-test`** operation that runs the composed pipeline N times and reports on variance structure. Which decisions recur? Where do they diverge? Which assumptions correlate with which outcomes? A Deleuzian repetition engine — not converging on the One True Answer, but mapping the topology of the decision space.

---

## 4. Application: Decision-Making Under Uncertainty

### The Shift in Success Criteria

Wicked problems don't have correct solutions. They have interventions with consequences that interact unpredictably with the environment. Traditional decision tools (expected utility, decision trees, cost-benefit analysis) assume you can enumerate outcomes and assign probabilities. For wicked problems, you can't — and the act of intervening changes both the outcome space and the probability distribution.

The appropriate optimization target shifts from **maximizing expected value** to **satisficing subject to a survival constraint**: find an answer that doesn't kill us outright.

### How the Machinery Helps

**The fan** populates the space of futures you're capable of imagining. Scenarios aren't forecasts with confidence intervals; they're narratives that make different failure modes viscerally concrete. Value lies in *coverage*, not probability. Did any story surface a failure mode that kills you? If not, generate a fourth.

**The funnel** asks: given these possible futures, what can we commit to that doesn't produce catastrophic failure in *any* of them? This is **minimax reasoning**, not expected value reasoning. Pick the action whose worst case across scenarios is survivable.

**The repetition** tells you how robust the decision is. Stable outcomes mean smooth terrain. Unstable outcomes mean you're near a ridge — and the ridge is where you should direct attention before committing.

### What the Mathematics Provides

**Composability.** Chain operations: fan → funnel → fan again ("we chose A, now what might go wrong with A?"). Each stage is typed with known inputs and outputs. Pipelines of arbitrary depth without losing track.

**Diagnosability.** When results are surprising or inconsistent, the structure tells you *where* to look. Instability in the fan = ambiguous framing. Instability in the funnel = sensitive criteria. Instability in the composition = genuine decision boundary. Different problems, different interventions.

**Repeatability without rigidity.** Different people, different LLMs, different times — the *structure* of the output is comparable even when the content differs. "Did team A's scenario exploration cover the same failure modes as team B's?" is answerable because both used the same typed pipeline.

### The Sagan Analogy

Sagan's baloney detection kit gave people heuristics that *embody* formal logic in usable form. "What's the control experiment?" is really about conditional independence. "Could an alternative explanation account for the same observations?" is really about model identifiability. People use the heuristics; the mathematics guarantees they work.

Cyberneutics is building toward a **baloney detection kit for decisions under uncertainty**: enough formal structure that you can trust the process, packaged as practices people can actually follow. The fan, the funnel, the repetition, the variance analysis — these are the heuristics. Category theory, palgebra, and pipeline composition — that's the guarantee the heuristics aren't just vibes.

---

## 5. Inventory: Data Types, Operations, and Patterns

The following emerged from this conversation and prior work. This is an initial inventory for more careful formalization.

### Data Types (Texts Inhabiting Soft Types)

| Type | Description | Palgebra Status |
|------|-------------|-----------------|
| **Situation** | A description of a wicked problem or ambiguous decision context. Input to the fan. | Needs formal type definition (template + rubric) |
| **Scenario** | A narrative arc exploring one possible future under stated assumptions. Output of the fan. | Needs formal type definition |
| **Scenario Set** | A collection of scenarios with explicitly divergent assumptions. Coproduct structure. | Indexed family; the index set is the assumption-space |
| **Charter** | Goal, context, success criteria, exit conditions. Frames a deliberation. | Defined (00-charter.yml schema exists) |
| **Roster** | Named characters with roles and propensities. Parameterizes both fan and funnel. | Defined (01-roster.yml schema exists) |
| **Deliberation Transcript** | Multi-round adversarial debate with opening statements, rounds, analyses. | Defined (02-deliberation.md structure exists) |
| **Resolution** | Decision, votes, rationale, implementation plan. Output of the funnel. | Defined (03-resolution.yml schema exists) |
| **Evaluation** | Rubric-scored assessment of a resolution against a charter. | Defined (04-evaluation.yml schema exists) |
| **Remediation** | Response to evaluation critique; committee addresses identified weaknesses. | Defined (05-remediation.md structure exists) |
| **Variance Report** | Comparison across multiple runs of the same composed operation; identifies stable decisions, fault lines, and sensitivity. Output of `/probe`. | **New.** Needs design. |
| **Decision Landscape Map** | Topological summary: basins of attraction, ridges, load-bearing assumptions. Synthesized from variance report. | **New.** Needs design. |

### Operations (Typed Pipeline Stages)

| Operation | Signature | Category-Theoretic Role |
|-----------|-----------|------------------------|
| **Charter** | Situation → Charter | Framing; constrains downstream types |
| **Convene** | Charter × Roster → Committee | Selection and parameterization |
| **Fan (Scenario Generation)** | Situation → Scenario Set | Coproduct injection (one-to-many spider) |
| **Funnel (Committee Deliberation)** | Charter × Scenario Set × Committee → Resolution | Product projection (many-to-one spider) |
| **Evaluate** | Charter × Resolution → Evaluation | Independent discriminator; enrichment |
| **Remediate** | Evaluation × Deliberation → Remediation | Feedback loop; error correction |
| **Probe (Repetition)** | (Situation → Resolution)^N → Variance Report | Deleuzian repetition; stability test |
| **Map** | Variance Report → Decision Landscape Map | Synthesis; topology extraction |

### Patterns (Composable Pipeline Templates)

| Pattern | Composition | Purpose |
|---------|-------------|---------|
| **Deliberated Choice** | Fan → Funnel | Convert ambiguity into justified commitment (decision monad) |
| **Evaluated Choice** | Fan → Funnel → Evaluate | Deliberated choice with independent quality check |
| **Stress-Tested Choice** | (Fan → Funnel)^N → Probe → Map | Repeated deliberated choice with variance analysis |
| **Cascaded Exploration** | Fan → Funnel → Fan | "We chose A; now what might go wrong with A?" |
| **Remediation Loop** | Funnel → Evaluate → Remediate → Evaluate → ... | Convergent refinement until threshold met |
| **Nested Fan** | Fan → (Fan per scenario) | Sub-branching within each scenario; decision tree exploration |

### Characters and Rosters

Two distinct roster types serve the two dual operations:

| Roster | Operation | Character Function |
|--------|-----------|-------------------|
| **Committee Roster** (existing) | Funnel (convergent) | Adversarial roles designed to stress-test: devil's advocate, evidence checker, historian, opportunity scout, systems analyst |
| **Scenario Roster** (new, to design) | Fan (divergent) | Narrative lenses designed to explore: each tells a coherent story from their own worldview. Not arguing with each other but generating distinct, internally consistent futures |

### Open Design Questions

1. **Scenario roster composition.** What archetypes serve divergent exploration? Optimist/pessimist/wildcard is too generic. Domain-specific? Drawn from the situation? Fixed cast or dynamically composed?

2. **Variance report structure.** What format captures "three runs gave A, two gave B, and here's what differed"? Needs to surface both the decisions and the assumptions/framings that correlated with each.

3. **Decision landscape map.** How to represent basins of attraction and ridges in a way that's actionable? String diagrams? Tables? Narrative summary?

4. **Interaction between rosters.** Can scenario characters feed into committee characters? (e.g., "Scenario character X's future is the one Maya finds most threatening.") Cross-pollination between the dual operations.

5. **Monad laws as quality criteria.** Can we operationalize the unit and associativity laws as tests? "If fanning then immediately collapsing gives the same answer as not running the pipeline, the pipeline added nothing" — is that checkable?

6. **Step-at-a-time mode.** Implementation of `--step` flag for committee skill: stop after each phase, allow human editing of intermediate artifacts, resume with edited artifacts as input. Human edits become first-class pipeline interventions, not hacks.

---

## 6. Next Steps

1. **Rename complete.** Repository is now `cyberneutics`. Update internal references as encountered.

2. **Formalize the fan operation.** Design the `/scenarios` skill: input format, output format, roster, and how it connects to the existing committee pipeline. Define the Scenario and Scenario Set types in palgebra.

3. **Design the scenario roster.** What characters serve divergent exploration well? Look at scenario planning literature (Schwartz, van der Heijden) for precedent.

4. **Implement step-at-a-time mode** for the committee skill. Add `--step` flag; human edits to intermediate artifacts are first-class.

5. **Design the `/probe` skill.** Repeated pipeline execution with variance analysis. Define Variance Report and Decision Landscape Map types.

6. **Write the palgebra treatment.** Resource equations for fan, funnel, and their compositions, following the pattern established in `palgebra/committee-as-palgebra.md`. String diagrams showing the dual spider topologies.

7. **Essay integration.** The Bruner lens applies directly: the fan is narrative-mode exploration (System 1, fast, associative); the funnel is paradigmatic-mode evaluation (System 2, slow, rule-governed). The composed operation is the full binocular view.
