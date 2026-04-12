# Diary: Stories, Scenarios, and the Serialization Problem

**Date:** 2026-04-09

**Context:** A conversation during a break from active cyberneutics development. Recent reading — Deleuze's *Difference and Repetition*, Thomas Rid's *Rise of the Machines*, and Robert Coles's *The Call of Stories* — converged on the role of narrative as cognitive technology, the scenario fan as the most distinctively productive use of LLMs, and the categorical duality between generation and diagnosis.

---

## The reading stack

Three books in progress, each feeding the project from a different angle.

**Deleuze, *Difference and Repetition*.** Slow going — a couple of pages at a time, multiple reads per paragraph. He uses words differently than expected. Commentary helps. The persistent instinct is to put his claims in category-theoretic terms: repetition as orbits of endofunctors, which connects to Rosen's chronicles. The attempt to formalize may be premature, but the exercise of trying forces genuine engagement with both Deleuze and the mathematics.

**Rid, *Rise of the Machines*.** Hundred pages to go. Currently in the cypherpunk section — relevant personal connections to some of the people involved. The historical parallels to current LLM discourse remain striking throughout.

**Coles, *The Call of Stories*.** The most directly relevant to cyberneutics. Coles's argument: literature trains moral imagination in ways that clinical training alone cannot. Narrative identification — inhabiting a character's situation — does genuine ethical and psychological work. This is not supplementary; it is a primary mode of understanding.

## Coles, the children, and the proxy channel

The most powerful illustration in Coles: black children in desegregated schools who were silent when asked directly how they felt — unwilling to engage, the situation too close, too dangerous to articulate to an adult with power over their world. But given readings, they engaged. They talked about how the stories made them feel, used characters as proxies, described their own inner situations indirectly through narrative identification.

This is not avoidance. It is a different and sometimes more honest channel. The proxy gives enough distance to be truthful about things that are too close to examine head-on. Coles understood that the indirection was not a limitation of the method — it *was* the method.

The structural parallel to scenario generation is exact. A decision-maker facing a wicked problem is in an analogous position — not because of power asymmetry but because of cognitive overwhelm. The problem space is too high-dimensional to apprehend directly. The fan gives multiple proxy worlds to inhabit, each one tractable, each one revealing structure that direct confrontation with the raw uncertainty cannot. The narrative frame makes it safe to think about futures you'd rather not face, because each scenario is explicitly a possibility, not a prediction. You can inhabit a worst case without committing to it as belief.

Telling stories is often a way to introduce assertions without admitting facts or making accusations. "I have a friend who..." lets you surface a problem without owning it. "A mad king once said..." puts a dangerous idea into circulation while maintaining distance. Nathan telling David the parable of the stolen lamb. Diplomacy, plea negotiations, family conflict — "hypothetically, if someone were to..." is the most productive sentence frame in human communication precisely because it opens possibility space without forcing commitment. The fan does exactly this: "here's a world where your assumptions hold" and "here's a world where they don't" — without accusing anyone of being wrong.

## The scenario fan as the primary contribution

The committee (the funnel) gets disproportionate attention because it has characters, drama, inspectable disagreement — it is the most legible part. But the scenario fan is the genuinely novel capability. Before LLMs, exploring possibility space required either formal modeling (which demands you already know the structure well enough to parameterize it) or human brainstorming (slow, expensive, bottlenecked by participants' collective imagination). LLMs can generate plausible, internally coherent alternative futures cheaply, quickly, and with a diversity of framing no small group could match.

Each scenario is a chart — a local coordinate system that makes one region of the problem space tractable. No single chart covers the whole manifold, but the collection, with its overlaps and contradictions, reveals the topology. Where scenarios converge: stable ground. Where small assumption changes flip outcomes: critical boundaries. Where coherent scenarios cannot be generated at all: the model of the problem is inadequate.

The committee then becomes a tool for *reading* those charts — important but secondary. The primary creative act is the generation, the fan that takes an ambiguous, high-dimensional situation and produces navigable slices.

## Assumptions revealed by absence

Confucius wanted all things called by their true names — the rectification of names as foundation of good governance. The ideal assumes you already know what things are. But with wicked problems, the important assumptions are invisible precisely because they are assumptions — the water the fish doesn't see.

Scenarios make the invisible visible by showing what happens when an assumption you didn't know you held turns out to be wrong. Generate five futures; in four things go roughly as expected; in the fifth everything breaks — and when you ask why, you discover you'd been silently assuming a supply chain would hold, or a regulation wouldn't change, or a key person would stay. The assumption reveals itself by its absence in the scenario where it fails.

You can't enumerate assumptions forward — there are too many, and the important ones are the ones you'd never list. But you can discover them backward, by generating diverse trajectories and asking what had to be true for each to play out as it did. The preconditions that differ between scenarios are the load-bearing assumptions.

Confucius had the right goal and the wrong sequence. You can't start with true names. You have to start with stories, and the true names emerge from the differences between them.

## Categorical duality: fan as pushout, funnel as pullback

The scenarios fan out from a common source — the starting situation — and diverge toward different outcomes. Two morphisms sharing a source: a span. The universal construction on a span is the pushout. The pushout captures what the scenarios collectively cover — the total explored territory, identifying overlapping outcomes while preserving distinctions.

The funnel goes the other direction. Multiple perspectives share a target — the situation under deliberation. Two morphisms sharing a target: a cospan. The universal construction is the pullback — the most general object simultaneously compatible with all perspectives. The pullback captures what the perspectives must agree on.

Fan as pushout, funnel as pullback. Colimit then limit. The deliberated choice monad, and the duality is exact.

The Deleuzian connection: generality as the target of morphisms from particulars (the thing they all map to by forgetting differences), but evolution goes the other way — the starting situation as source, scenarios as different morphisms out of it, each carrying initial conditions forward differently. Deleuze's example of annual Bastille Day celebrations: each instance caused by the original event, but also by the generality of the tradition. Arrow from general to particular is instantiation; arrow from particular to general is abstraction. Category theory is liberating here — it's easy to swap direction and work in the opposite category, studying both simultaneously.

And the evolutionary substitution of future states for past states is the endofunctor orbit again — Rosen's chronicles, where the temporal unfolding *is* the system rather than something the system does.

## Agee, Faulkner, and the serialization problem

James Agee's *Let Us Now Praise Famous Men* came up through Coles. Agee was sent to Alabama by Fortune magazine to document sharecroppers; he refused to produce a clean journalistic account. He was tortured by the question of whether documenting poverty for a magazine was itself exploitation — whether turning lives into subjects violated their dignity. The book mixes factual description with moral anguish about the act of representation. Evans's photographs sit at the front with no captions — different modes of witness given their own integrity.

Agee embraces the understanding that real lives can't be facilely serialized into a single narrative. Faulkner does the same in *As I Lay Dying* — fifteen narrators because no single voice can hold the Bundren family's reality without flattening it. These are both responses to the same fundamental constraint: a rich relational web must pass through a serial channel (pages, speech, a context window), and naive serialization destroys exactly what matters.

Faulkner's multiple-narrator technique and the fan/funnel architecture are structurally the same move: multiply perspectives, keep them in tension, let the reader reconstruct the higher-dimensional object from convergences and contradictions.

Agee goes further in one respect: he includes his own anguish about the serialization itself as part of the text. That's a metacognitive move — System 3*, the audit channel that monitors whether the sensing apparatus is itself introducing noise.

## Thamus, McLuhan, and the LLM blade

Found a passage in a 40-year-old notebook: Plato's *Phaedrus*, Thamus and Theuth. The god presents writing to the king as a gift that will improve memory; the king replies it will do the opposite — give people the appearance of knowledge without the reality.

The original cue-card critique. And the irony: the notebook entry did exactly what Thamus said writing couldn't — triggered genuine recall and connection rather than substituting for thought. Thamus was right that externalized memory changes cognition. Wrong that the change is purely degradation. Writing restructured memory rather than destroying it.

Reports of kids outsourcing thinking to LLMs are exactly Thamus. And the critique is real at every transition — writing, printing, calculators, Google, now LLMs. Each time the concern is real and the panic overblown, simultaneously.

But the LLM version is sharper because of the problem cyberneutics was built to address: LLM output has the *form* of reasoning without necessarily its substance. A calculator doesn't pretend to understand arithmetic. A book doesn't pretend to have had the thought for you. But an LLM produces fluent, confident prose that looks like deep thinking whether it is or not. The blade without a handle. A student can't tell the difference between having thought something through and having received something that looks thought-through.

McLuhan would have looked past the content to what the medium does to the sensorium. LLMs have the linearity of text but the participatory quality of conversation — neither hot nor cool in his framework, or both simultaneously. His tetrad: they extend the ability to articulate; obsolesce the solitary struggle to compose; retrieve the Socratic dialectic; and pushed to saturation, reverse into cognitive learned helplessness. He'd say we're in the numb phase — the narcosis that accompanies every new extension of the nervous system.

## Coles and Williams

Coles worked with William Carlos Williams, who was a practicing physician and a poet and insisted the two weren't separate activities. The attention you bring to a patient's story and the attention you bring to a line of poetry are the same faculty. Bringing literature into medical training wasn't enrichment — it was training a core clinical skill: the ability to attend to what someone is actually telling you.

The best physicians are widely read and culturally aware. Wide reading cultivates pattern recognition across human experience — not diagnostic pattern matching, but the kind that lets you hear what a patient means rather than just what they say.

## Freud, narrative, and organisms

Freud was crazy by modern clinical standards, but he got stuff done. His models weren't so far off as to be crackpot. Above all, his theories were his attempt to make sense of what he observed directly — hearing stories from patients. The structural insight about emergent behavior from interacting sub-agents (id/ego/superego) keeps being rediscovered: Minsky's society of mind, the cyberneutics committee.

An adjacent question: even one-celled organisms swim away from threats and toward food. Not because they run a logical evaluator on symbolic representations of "threat" and "food," but because their bodily structure *is* the accumulated narrative of ancestral encounters — billions of years of what worked, compressed into membrane receptors and flagellar responses. The bacterium doing chemotaxis has the Peircean triadic structure: chemical gradient (object), receptor state (sign), flagellar response (interpretant). A narrative in the minimal sense — a temporal sequence where earlier states condition later ones through a mediating structure.

Simon's point applies: the interesting behaviors of an organism arise in complex environments. The bacterium in uniform medium does nothing interesting. Put it in a gradient and suddenly it has behavior — because the environment provides the other half of the story. Pask's conversation, von Foerster's eigenform, Maturana's structural coupling — all the way back to a single cell.

## Aphorisms

Two compressed observations emerged during the conversation that are worth recording:

*The universe is a machine for converting the future — probabilities — into the past — statistics.*

Each tick of the clock collapses a probability distribution into a single realized outcome, which becomes the initial condition for the next distribution. The Giry monad in one sentence. The functor from future to past has no inverse — statistics don't convert back into the probabilities that generated them. Scenario generation is a partial reversal: starting from the realized present and fanning it back out into possible futures, an approximate section of an irreversible functor.

*The Big Crunch is the ultimate forgetful functor.*

Terminal object. Everything maps to it, nothing maps back. Every distinction, every structure, every morphism — forgotten into a single point. Forgetful in both the categorical sense (stripping structure) and the ordinary sense (final forgetting).

Pask's teachback technique is working. Explaining ideas back — to Claude, to the meetup group, to peers — is how they get metabolized. The planning, not the plan.

---

## Actions

### Reading

1. Continue Deleuze — the attempt to formalize in categorical terms is productive even if premature. The repetition/endofunctor connection and Bastille Day/instantiation example are worth developing.
2. Finish Rid. The cypherpunk section has personal resonance.
3. Continue Coles. The proxy-channel mechanism deserves a more thorough treatment connecting to scenario generation.
4. Pick up Agee's *Let Us Now Praise Famous Men* and the Nelly Bly book from the used bookstore.

### Theoretical

5. Develop the fan-as-pushout / funnel-as-pullback duality more carefully. The claim that the deliberated choice is colimit-then-limit needs scrutiny — is the composition well-defined? What are the coherence conditions?
6. The "assumptions revealed by absence" mechanism needs formalization. The difference between scenario preconditions is doing the diagnostic work — this may connect to the coalgebra/algebra duality flagged in the 2026-03-25 diary entry.
7. The "approximate section of an irreversible functor" observation about scenario generation deserves a note in `wild/` — it connects the fan to the arrow of time in a way that might be more than metaphorical.

---

*Cross-references: wild/diary/2026-03-25-language-epistemology-sensemaking.md (sensemaking game, rubber duck framing), wild/diary/2026-03-27-resistance-to-ai-sensemaking.md (Thamus, cue-card pattern, Dr. Reva), wild/diary/2026-03-26-echo-chamber-immune-organs.md (serialization, System 3*), palgebra/categorical-structures.md (pushout/pullback), research-programs/metacognition/ (Beer System 3*, calibration register), wild/diary/2026-03-15-emotional-attention-steering.md (PID dynamics, orchestrator), essays/01-why-narrative-engines-change-everything.md (narrative computing)*
