# Glossary of Key Terms

Quick reference for the 20 terms that recur across the essay collection. Each entry gives a one-sentence definition and points to the essay where the concept is introduced or most fully developed.

---

**Confidence propagation** — The rule that confidence can only degrade through pipeline stages; a Medium-confidence input cannot produce a High-confidence output. ([Essay 08](./08-from-methodology-to-formalism.md), §5; [Palgebra Reference](../palgebra/reference.md))

**Decorated text** — An artifact represented as a (text, metadata) pair, where metadata is YAML front matter carrying scores, provenance, and type information. ([Palgebra Reference](../palgebra/reference.md); [Decorated Texts](../palgebra/decorated-texts.md))

**Eigenform** — A fixed point of a transformation: a pattern that, when the process is applied to it, reproduces itself — a temporary stabilization in a field of becoming. ([Essay 04](./04-cybernetics-and-observation.md); [Essay 06](./06-deleuze-difference-repetition.md), §Eigenforms)

**Enrichment morphism** — A pipeline operation that leaves content unchanged and updates only metadata (scoring, gating); ideally idempotent and safe to re-run. ([Essay 08](./08-from-methodology-to-formalism.md), §3; [Palgebra Reference](../palgebra/reference.md))

**Entailment mesh** — Pask's term for a non-hierarchical network of mutually-entailing concepts; structurally isomorphic to Deleuze's rhizome. ([Essay 11](./11-conversation-theory.md), §Entailment Meshes)

**Fan/Funnel duality** — Scenario generation (fan, divergent: explore possible futures) and committee deliberation (funnel, convergent: compress exploration into commitment); the two operations compose into a decision pipeline. ([Essay 10](./10-decisions-under-uncertainty.md))

**Game within the game** — The general principle of constructing local order against entropic tendency; using process to impose structure where entropy would otherwise dissolve it. The adversarial committee is one instantiation; others include cell membranes, legal systems, engineering redundancy. ([Essay 02](./02-from-practice-to-theory.md), §The Outer Game is Rigged)

**Human gate** — A collapse operator in the pipeline where human editorial judgment terminates the recursive evaluation loop, projecting from graded uncertainty into crisp commitment. ([Essay 08](./08-from-methodology-to-formalism.md), §2; [Palgebra Reference](../palgebra/reference.md))

**Locally coherent** — Internally consistent and plausible within its own framing — each sentence follows from the previous, genre conventions are respected — but without guarantee that the narrative as a whole is true, complete, or consistent with external reality. ([Essay 01](./01-why-narrative-engines-change-everything.md), §The Dangerous Part)

**Narrative computing** — What the machine does: an LLM takes a prompt and generates a narrative. The primitive operation of narrative engineering, analogous to the transistor. ([Essay 01](./01-why-narrative-engines-change-everything.md); [README](./README.md))

**Narrative engine** — What an LLM *is*: a machine that generates narratives by traversing latent space. A technical characterization of the tool, distinct from "stochastic imps" (entropy personified) and "statistical ghost" (the phenomenological encounter). ([Essay 01](./01-why-narrative-engines-change-everything.md), §Why "Narrative Engine")

**Narrative engineering** — The discipline of composing primitive narrative computers into reliable systems through redundancy, feedback, iteration, and staged composition. Analogous to how software engineering grew from symbolic computing. ([Essay 07](./07-bolands-narrative-engineering.md); [README](./README.md))

**Organ/Bloodstream regime** — Two trust regimes from the immune-system analogy. *Organ*: a controlled channel with defined inputs, outputs, and inspectable transformations — you trust it because you built it and can verify the chain of custody. *Bloodstream*: an ambient medium carrying unprovenanced material — the receiving tissue must judge what to absorb and what to reject, because nobody owns the chain of custody and type membership is a social construct emerging from patterns of judgment. (Older material may use "pipeline/bath" as deprecated synonyms for organ/bloodstream.) ([Essay 09](./09-narrative-immune-systems.md))

**Rhizome** — A non-hierarchical knowledge topology with multiple entry points and no single root; Deleuze and Guattari's term for networks that grow by lateral connection rather than tree-structured hierarchy. Pask's entailment mesh is structurally isomorphic. ([Essay 06](./06-deleuze-difference-repetition.md); [Essay 11](./11-conversation-theory.md))

**Second-order cybernetics** — The cybernetics of observing systems (von Foerster, Bateson): the observer is part of the observed system, and observation changes state. First-order cybernetics studies systems from outside; second-order recognizes there is no outside. ([Essay 04](./04-cybernetics-and-observation.md))

**Situation-Gap-Bridge** — Dervin's Sense-Making model: people in *situations* encounter *gaps* (where understanding fails) and construct *bridges* (cognitive or communicative moves that allow continued navigation). The bridge changes the situation, producing new gaps. ([Essay 03](./03-sensemaking-101.md))

**Soft types** — Types with graded membership rather than boolean (is this an evidence file? not yes/no, but *how well* does it inhabit its type, measured along multiple dimensions). The type system appropriate to problems where quality is a membership function. ([Essay 08](./08-from-methodology-to-formalism.md), §1; [Palgebra Reference](../palgebra/reference.md))

**Stochastic imps of happenstance** — Entropy personified: the forces of chance that make things go wrong. Not the LLM (that's the narrative engine), but the adversary the methodology is designed to counter. Murphy betting with the house. ([Essay 02](./02-from-practice-to-theory.md); [The Stochastic Imps of Happenstance](./the-stochastic-imps-of-happenstance.md))

**Teachback** — Pask's central method: demonstrate understanding not by repeating what was said but by teaching it back in your own terms, applying it to new cases, and defending it against challenge. The operational test for whether a Dervin bridge holds weight. ([Essay 11](./11-conversation-theory.md), §The Teachback Mechanism)

**Transformation morphism** — A pipeline operation that produces new content: `f : (text, meta) → (text', meta')`. Stochastic, non-idempotent. The committee's Deliberate operation is the paradigmatic example. ([Essay 08](./08-from-methodology-to-formalism.md), §3; [Palgebra Reference](../palgebra/reference.md))
