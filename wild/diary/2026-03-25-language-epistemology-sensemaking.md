# Diary: Language, Epistemology, and the Sensemaking Game

**2026-03-25**

---

## The epistemological turn

A new batch of books arrived: Quine's *From Stimulus to Science*, *Introducing Semiotics* (Cobley and Jansz), *Saussure for Beginners* (Gordon), and Leonard Reich's *The Making of American Industrial Research*. Several Deleuze volumes and Lynn Segal's *The Dream of Reality* (on von Foerster's constructivism) followed shortly after.

I'm drawn to epistemology now, and to questions about language and reasoning that I can't quite phrase cleanly. The best approximation: how much reasoning simply arises from the imperative flow of words? Not "intelligence in language" exactly, but whether the sequential, syntactic structure of discourse does cognitive work that we attribute to a reasoning agent. Whether, in some meaningful sense, the discourse itself thinks.  Carnap seems relevant here.

This is directly relevant to the committee pipeline. The fan/funnel architecture produces reasoning outputs that no single prompt generates — not because the components are smarter, but because structured discourse through multiple perspectives forces exploration of the scenario space. The composition is where the thinking happens. The characters are lenses; the pipeline is the cognition.

## Saussure, Peirce, and the observer

The key structural difference between Saussure and Peirce turns out to matter. Saussure's model is dyadic — signifier and signified. The interpreter is presupposed but has no formal position. Signs get their value from differential relations within the system (langue), and the system is self-contained and synchronic. Nobody is explicitly doing the interpreting.

Peirce's triad — sign, object, interpretant — gives the observer a structural role, but subtly. The interpretant isn't the observer; it's the sign that interpretation generates. The observer enters as the locus where a new sign is produced, and that new sign enters further triadic relations, generating an indefinite chain of semiosis. The observer isn't outside the system — they're the site where the sign chain propagates.

This matters because in Saussure's framework the cognitive work is structural but static. In Peirce's, semiosis is a process, and the observer is what makes it a process rather than a structure. Each interpretant is a little act of construction — which is von Foerster's point about the observer being operationally inside the system.

For the committee, each character occupying the interpretant position generates a new sign (their assessment) from the prior sign-object relation (the scenario and evidence). The funnel is a chain of semiosis — successive interpretation, each stage producing a new interpretant that becomes the sign for the next.

## Meaning as process, perception as communication

I've come to believe that all meaning is a process, and that all apprehension of sensory input follows a structure similar to linguistic understanding — a kind of communication.

This position has more support than I expected, and from different directions. Peirce's semiotics is explicitly not limited to language: any process where something stands for something else to some interpretant is semiosis, including perception, animal behavior, and biochemical signaling. Von Foerster would frame it as computation — the nervous system cannot distinguish between perception and hallucination; only the cause differs, not the process. Maturana and Varela built this into autopoiesis: cognition is the process of living, every organism is a semiotic system maintaining itself through structural coupling. Pask's conversation theory treats all cognition as conversation formally, not metaphorically — understanding as the achievement of agreement between interacting processes, whether between people, brain subsystems, or organism and environment. Bateson's "a difference that makes a difference" is deliberately substrate-independent. Merleau-Ponty, from phenomenology, argued that perception is active bodily engagement — a dialogue with the world. The biosemiotics tradition (Hoffmeyer, Kull, the Tartu school) takes Peirce literally and argues semiosis is a defining feature of life itself.

"If all apprehension is interpretive process, then the committee pipeline doesn't simulate reasoning — it instantiates it."  An LLM just told me that.  How would you tell the difference?

## Carnap, coalgebra, and transforming problems

Carnap's use of "functor" predates the categorical sense (Eilenberg and Mac Lane, 1945). He means a function-expression in a formal language — a syntactic concept. The terminological overlap with category theory is mostly coincidental, though both involve structure-preserving mappings.

Rediscovered Bart Jacobs on coalgebra. The motto — "coalgebras take things apart, algebras put things together" — captures the duality: algebra is synthesis, coalgebra is analysis. An algebraic specification says how to build a thing; a coalgebraic specification says what you can observe about it from outside. Which is Yoneda-adjacent: the coalgebraic view says a system is its observations, its relationships to probes.

Found the paper I'd half-remembered: Trancón y Widemann and collaborators, "Scientific Modelling with Coalgebra–Algebra Homomorphisms" (arXiv:1506.07290, 2015), with an earlier companion paper (2010) using the logistic map. The framing is that algebraic models are "queries of causality" and coalgebraic models are "representations of behavior," and composing them via coalgebra-algebra homomorphisms lets you transform problems into domains where they're more tractable and back. The connection to fan (decomposing situations into observable behaviors — coalgebraic) and funnel (constructing resolutions — algebraic) is suggestive, but may be a superficial pattern match rather than a genuine structural correspondence.

Also encountered a paper on the Galois connection between syntax and semantics — the pair of order-reversing maps between theories and classes of models, where each determines the other up to closure. If something like this connects the pipeline algebra's syntactic face to its semantic face, it would formalize how tightening structural constraints narrows the space of possible interpretations.

## Vickers on visualization and semiotics

Identified one of two papers on semiotics and category theory I'd read previously: Vickers, Faith, and Rossiter, "Understanding Visualization: A Formal Approach using Category Theory and Semiotics" (IEEE TVCG, 2013). It renders the Peircean triad as a commutative diagram and uses morphism properties (mono, epi, iso) to define visualization concepts like literalness, sensitivity, and redundancy. An earlier diary entry (2026-03-22) already noted the connection: the organ regime pipeline is a semiotic chain; the bloodstream's unprovenanced-text problem is a broken triad; type-spoofing is semiotic pathology. The second paper remains unidentified — possibly Tohmé, Gangle, and Caterina on category theory and ML semiotics (2024), but uncertain.

## Yoneda in cybernetics

The Yoneda lemma — an object is completely determined by its relationships to all other objects — keeps appearing in early cybernetics, expressed without the name. Ashby is the strongest candidate: systems defined entirely by input-output behavior, internal structure irrelevant to the cybernetic description. Beer inherits this — the viable system model defines subsystems by their relationships to other subsystems. Von Foerster comes at it through eigenvalues of cognitive operations: objects as tokens for eigenbehaviors, constituted by recursive interaction. Meadows emphasizes that system behavior arises from relationship structure, not component nature.  Herbert Simon says something similar: that the interesting behaviors of an organism show up in a complex environment.  Not quite the same thing, but it rhymes.
The specific author I was trying to recall remains elusive, but the idea pervades the first-generation cybernetics literature.

## Rise of the Machines — the 1960s cybernetics fever

Continued reading Rid's *Rise of the Machines*. The early 1960s were a period of extraordinary polarization around cybernetics and automation. Unemployment fears and utopian optimism coexisted, often in the same publication. Some scientists expected very fast progress toward goals that now look dubious — space-adapted cyborgs, for instance. Clynes and Kline coined "cyborg" in 1960, proposing pharmacological and mechanical adaptations for space travel. Mosher at GE built hydraulic exoskeletons with haptic feedback — Waldos, essentially — funded by the military, which didn't succeed. Diebold wrote effusive articles about automation for mass audiences. By the mid-1960s the focus shifted to hydraulic-powered teleoperated systems. By the early 1970s, "cybernetics" had fallen out of use as a term.

Much of the talk from that era is heard again now, prompted by LLMs. The same mix of unemployment anxiety, transformation rhetoric, utopian and dystopian framing, with engineering lagging behind the promises. The historical pattern is useful as inoculation against both hype and despair.

## Barwise, Burgess, and frameworks that don't land

Barwise and Seligman's *Information Flow* (1997) has been sitting on my shelf since a clearance table. I never understood it and never saw it cited much. The term "infomorphism" never caught on. But Barwise was a serious logician (situation semantics, non-well-founded sets), and my inability to understand the material isn't a reliable indicator that it's empty. The book tried to build a general mathematical theory of information flow using channel theory — Galois connections between distributed systems. It landed awkwardly: too abstract for practitioners, undercooked for the logic community, overtaken by Lawvere-style and sheaf-theoretic approaches. With more category theory background now, it might reward a reread — as a test of whether the framework gives anything that Fong, Spivak, or Lawvere don't already provide.

A similar case: Burgess and Bergstra's promise theory. Burgess came from real engineering (CFEngine), and the core insight — that you can only reason about what autonomous agents volunteer to do, not what they're commanded to do — is a genuine architectural point for distributed systems. But they admitted they couldn't formulate a logic of promises. The idea remains interesting as a coordination model for agents operated by and accountable to different people. The committee characters make something like promises — each commits to an assessment from its perspective — and the funnel is a reconciliation protocol. The bloodstream regime, where commitments are implicit and potentially dishonest, is where a promise-theoretic framing gets interesting.

## The sensemaking game, and LLMs as rubber ducks

I've been reflecting on how to explain what LLMs are good for to people who are either uncritically enthusiastic or categorically opposed.

A common resistance pattern: someone who has legitimate concerns about AI — psychosis from parasocial attachment, profit-driven deployment indifferent to user wellbeing, environmental costs borne by disadvantaged communities, the use of engagement metrics that reward addictive interaction — treats those concerns as reasons never to engage with the technology at all. The concerns are real. But treating them as a settled position rather than an ongoing inquiry prevents developing the discrimination needed to use the tools critically. Refusing to enter the room is safe but static.

LLMs are storytelling machines, not oracles. The Eisenhower maxim applies: "Plans are useless, but planning is essential." If you treat the machine as an oracle, it gives you the plan, but you don't get the benefit of the planning process — the exploration, the what-if detours, the learning how puzzle pieces fit. The value is in the human's cognitive process, not the machine's output.

The best analogy I've found: rubber ducks that talk back. The classic rubber-duck debugging technique works because explaining a problem forces you to put it into words, and that often leads to the solution. The duck does nothing. These ducks talk back — they bring in threads of inquiry and connections you hadn't considered. Often useful, sometimes misleading, occasionally leading down fruitless rabbitholes. In every case, it's finally up to the human to draw conclusions and make decisions.

This frames the committee pipeline correctly. Its value isn't the final output — it's that running it forces exploration of the scenario space from multiple angles. The characters are structured provocation. The deliberation is where the human learning happens.

Some introductory material in the repo uses phrases like "sensemaking partner" which could be misconstrued. The intent is affectionate, like saying "my books are my friends" — not a claim that machines are people. But in a repo whose core claim is that LLM outputs need inspectable reasoning chains *because* they're unreliable narrators, language implying partnership or agency works against the message. The rubber-duck framing is cleaner: it keeps the locus of judgment with the human.

## The Bogdanov problem

Working with an LLM on mathematics you're learning is a peculiar pedagogical situation. The machine produces text with the surface texture of mathematical reasoning, uses vocabulary correctly most of the time, and makes structural claims that range from genuinely insightful to subtly wrong to occasionally vacuous. It's like being given a pile of plausible theory by a prolific but unreliable research assistant and having to learn the concepts well enough to distinguish real content from something that merely passes peer review — the Bogdanov problem.

The risk is real. Confident fluency substitutes for rigor. Plausible-sounding structural correspondences — "fan is coalgebraic, funnel is algebraic, Galois connections everywhere" — may be genuine or may be categorical puns. After fifty years in software I have reliable judgment about when something works versus when it sounds good. That's a different kind of pattern recognition than formal fluency, and it's arguably more reliable for detecting when an analogy is load-bearing versus decorative. But it has limits.

The formal work in the repo — palgebra, furry logic, the open games translation — is provisionally useful but untrusted until validated by domain experts. The committee's core value is inspectable reasoning records, which stands independently of whether the category theory is correct. The repo needs to say this prominently. Someone from the ACT community landing on the repo and finding categorical formalism without clear epistemic status markers will either dismiss it or — worse — politely walk away. The math must be clearly labeled as exploratory, LLM-assisted, and awaiting expert review.

This connects to Bradley's work, which is the real thing — a working mathematician using category theory to formalize properties of language models. Following up on the enriched-category language modeling trajectory (thesis through magnitude paper) is a priority, both as subject matter worth understanding and as a calibration point for how far the repo's formal work is from rigorous practice.

---

## Actions

### Research

1. Follow up on Bradley's trajectory: read the enriched category theory of language paper (2022, arXiv:2106.07890) and the AMS Notices expository piece (2024). The earlier diary entry (2026-03-22) identified these as high priority. The Yoneda-as-semantic-representation construction is directly relevant to the soft type system.
2. Identify the second semiotics/category theory paper read alongside Vickers. Candidate: Tohmé, Gangle, and Caterina (2024). Verify.
3. Reread Barwise and Seligman's *Information Flow* with current CT background. Test whether channel theory gives anything not already available through Fong/Spivak or Lawvere. If not, document why and shelve.
4. Read *The Dream of Reality* (Segal on von Foerster). Connect to the observer-owns-interpretant thread from the Peirce/Saussure comparison.
5. Look into the Galois connection between syntax and semantics more carefully — distinguish the lattice-theoretic tradition (Dunn, Gehrke) from Lawvere's functorial semantics. Determine which, if either, is useful for the pipeline algebra.
6. Read the Trancón y Widemann papers (2010, 2015) on coalgebra-algebra homomorphisms in scientific modeling. Assess whether the fan/funnel correspondence is structural or superficial.
7. Investigate Jacobs' coalgebra draft more carefully. The algebra/coalgebra duality (constructive vs. observational) may formalize the fan/funnel distinction, but needs scrutiny.

### Editorial

8. Write epistemic status disclaimers for the root README and palgebra README. Frame formal work as exploratory, LLM-assisted, and awaiting expert review. Outreach to ACT practitioners is the validation path.
9. Audit introductory material for language implying LLM agency or partnership. Replace with framing that correctly locates judgment with the human. "Sensemaking partner" → something that preserves the affection without the epistemological confusion.
10. Review the Rise of the Machines notes for material connecting historical cybernetics hype cycles to current LLM discourse. May inform a future essay on pattern recurrence.

---

*Cross-references: wild/diary/2026-03-22-bradley-magnitude-tropical.md, wild/committee-games/, palgebra/, references/bradley-cyberneutics-references.md, wild/potential-to-sense/*
