# Pask's Machine-Machine Conversations and the Bisimulation Question

## 1. The Colloquy of Mobiles (1968)

Gordon Pask's Colloquy of Mobiles, exhibited at Jasia Reichardt's *Cybernetic Serendipity* exhibition at the ICA London in 1968, is the earliest known system in which machines conversed with machines in a Paskian framework. ZKM (Zentrum für Kunst und Medien, Karlsruhe) describes it as "the first example of machines conversing with machines."

The system consisted of five computer-controlled mobiles suspended from the ceiling: two "males" and three "females." They communicated via light and sound, autonomously, independent of human intervention.

The design embodied complementary incompleteness:

- Males could project beams of light but could not satisfy their own drive to have light play on their periphery.
- Females could reflect light but could not generate it.
- Neither type could achieve satisfaction alone. Cooperation was forced by the architecture.

The mobiles learned to optimize their behavior, reaching satisfaction states with minimum energy expenditure. Pask designed the system explicitly as a "social system" and described it as an "aesthetically potent environment." Visitors could enter the conversation using flashlights and mirrors, but were optional — the machines conversed without them.

A full-scale replica was built in 2018 by Paul Pangaro and Tim McLeish at the College for Creative Studies in Detroit. It was subsequently shown at Centre Pompidou and entered ZKM's permanent collection.

**Sources:**
- Media Art Net: http://www.medienkunstnetz.de/works/colloquy-of-mobiles/
- ZKM: https://zkm.de/en/artwork/the-colloquy-of-mobiles
- Colloquy 2018 Project: https://www.colloquyofmobiles.com
- Pangaro's account: https://pangaro.com/designconversation/2018/01/remaking-pasks-colloquy-of-mobiles/
- Pask's original description in Reichardt (ed), *Cybernetics, Art and Ideas* (1971)

## 2. The Chameleon-Mirror Problem

The Colloquy solves a fundamental design problem that anyone building multi-agent LLM systems inherits whether they know it or not.

Put two identical adaptive systems facing each other — two chameleons on a mirror. Each adapts to the other's state, but since both run the same adaptation function, they either converge on a shared attractor (losing any productive tension), oscillate between states (never stabilizing), or deadlock (each waiting for the other to move). There is no ground truth to break the symmetry. The system is closed under its own dynamics.

Pask's solution was asymmetry. Not identical agents with different random seeds, but structurally complementary agents with different capability profiles. Males emit, females reflect. Different functional incompleteness creates a productive interaction space where convergence is possible because satisfaction *requires the other*. The asymmetry is not a workaround — it is the mechanism that makes conversation possible at all.

This maps directly onto LLM pipeline design. Run N identical model instances with identical system prompts, and you get the chameleon-mirror problem: responses converge toward shared attractors, disagreements are shallow and performative, and the system rapidly settles into consensus without having explored the space. The cyberneutics committee's propensity system — different worldview lenses per character, each with distinct epistemic commitments and distinct blind spots — is the same structural move as Pask's male/female asymmetry. Functional incompleteness in different dimensions forces genuine interaction rather than mimetic convergence.

The key insight is that the asymmetry must be in capability, not merely in opinion. Two agents who "disagree" but have identical reasoning structures will converge as soon as one persuasive argument appears. Two agents whose reasoning structures are complementarily incomplete — one can see what the other cannot — remain productively different because their convergence requires actual information transfer, not just social pressure.

## 3. Bisimulation as the Right Frame

The question "do the committee characters really have needs/drives/propensities?" is ill-formed. It demands access to internal states that are, by construction, unobservable. The bisimulation framing dissolves it.

Two systems are bisimilar if every observable transition one can make, the other can match, recursively. You don't need to open the box. If a committee character produces responses observationally indistinguishable from what an entity with a given propensity would produce — challenges the right claims, asks the right follow-ups, updates in the right direction — then for the purposes of the pipeline's function, it *has* that propensity.

Pask himself would have endorsed this framing. He designed the Colloquy mobiles with a "sexual analogy" (his term) as a design decision about observable complementarity, not a claim about machine desire. The mobiles didn't "want" satisfaction — they were specified such that certain states reduced activity and others increased it. From outside, that looks like wanting. From inside, it's a control loop. The difference is underdetermined by observation, and by Bateson's criterion — "a difference that makes a difference" — an underdetermined difference carries no information. It is not a question.

This cleans up the committee-as-open-game formulation (`wild/committee-games/committee-as-open-game.md`). Propensity is a constraint on the observable transition function, not a psychological claim. It restricts which moves a character can make in the game. The selection function in the open game formalism doesn't ask *why* a strategy was chosen, only which strategies are available and how payoffs propagate. A character with a "skeptical empiricist" propensity is one whose available moves are restricted to those a skeptical empiricist would make — measured by bisimulation against the specified profile, not by introspection.

The calibration register then becomes a bisimulation monitor: it tracks whether the observed transition history of each character remains bisimilar to the specified propensity profile. Bisimulation failure — the character starts making moves inconsistent with its specification — is measurable degradation, detectable without access to internal states. This is what the meta-d' framework does operationally: it measures the consistency between observed behavior and expected behavior under the specified profile.

## 4. Connection to the Absent-Party Problem

The Colloquy mobiles could be observed in real time. You can watch the bisimulation play out: male emits, female reflects, male adjusts, female repositions, and the cycle converges toward mutual satisfaction. The observer has access to the full transition history of both parties.

Absent-party communication (see `wild/communicating-absent-parties/`) removes half the observation. You have the artifacts — the text, the glyphs, the genetic code, the nuclear warning marker — but you cannot observe the sender's transitions. You cannot watch them encode, cannot see what they intended, cannot verify whether your decoding matches their encoding. You are left with traces and must infer a transition system that could have produced them.

Decipherment is constructing a bisimulation partner for a system you can never observe directly. Alice Kober building her Linear B triplets — groups of three related sign sequences sharing a common root but with different endings — was constructing a hypothetical transition system bisimilar to whatever the Minoans were doing when they inflected their words. She didn't need to know what the words meant. She needed to detect that the transition structure was consistent with inflectional morphology. The structural regularity was sufficient to reconstruct the transition system up to bisimilarity, even though the sender had been absent for three thousand years.

For the calibration register: in the contemporaneous committee case (characters running live on LLM instances), you can check bisimulation directly — you can detect when a character drifts out of its specified propensity by comparing its current transitions against its profile. In the absent-party case, no such check is possible. There is no ground truth. You can only check the internal consistency of your *model* of the absent party — whether your reconstructed transition system is self-coherent and consistent with all available evidence.

This is the meta-d' limit. Meta-d' measures how well the system's confidence tracks its accuracy, but accuracy requires a ground truth signal. When ground truth is unavailable — the sender is dead, interstellar, or merely absent — the register must fall back on internal consistency: does the interpretation cohere with itself and with the broader evidential mesh? The calibration register needs a zero-feedback mode that tracks coherence rather than correspondence.

## 5. Pask's Machine Trajectory

Context for the Colloquy's position in Pask's broader experimental program:

**Musicolour (1953–57).** A light show that responded to live keyboard input. The machine adapted to the performer's playing patterns; the performer adapted to the machine's light responses. Genuine bidirectional adaptation — conversation in Pask's sense — but always human-machine. The machine could not converse with another machine.

**SAKI (1956).** Self-Adaptive Keyboard Instructor. The machine adapted to the human learner's performance, adjusting task difficulty to maintain optimal challenge. Adaptive, but strictly machine-to-human. The human was always in the loop as the entity being modeled.

**Electrochemical "ear" (late 1950s, with Stafford Beer).** Self-organizing thread networks grown in ferrous sulphate solution. The threads adapted to electrical stimuli, rewired after damage, and developed sensitivity to sound frequencies. Arguably machine-environment "conversation" — the system adapted to external signals — but not machine-machine in the Paskian sense. There was no second adaptive system to converse with.

**Colloquy of Mobiles (1968).** The breakthrough. Machines conversing with machines, humans optional. The first system where both parties in the conversation were artificial, both adapted, and the interaction met Pask's criteria for conversation (mutual adaptation toward satisfaction states that neither could achieve alone).

**CASTE (early 1970s).** Course Assembly System and Tutorial Environment. The machine built an explicit model of the learner's entailment structure and adapted its teaching strategy accordingly. Sophisticated machine-human conversation, but always with human learners as the conversational partners.

**THOUGHTSTICKER (1970s–80s).** Group learning system. Multiple humans interacted through a shared computational environment that tracked their entailment structures and identified agreements, disagreements, and potential bridging topics. Machine-mediated human-human conversation — the machine was the medium, not a conversant.

The trajectory shows Pask consistently working toward machine autonomy in conversation, with the Colloquy as the pivotal moment where human participation shifted from necessary to optional. Before 1968, every Pask system required at least one human conversant. After 1968, the question was open: if machines can converse with each other, what do they produce?

## 6. Open Questions

- **Pure machine-machine runs.** Did Pask ever run the Colloquy (or a similar system) with humans completely excluded for extended periods? The exhibition context means humans were always potentially present. A pure machine-machine run with systematic observation of what the system converges on — without any possibility of human intervention steering the dynamics — would be the strong test case. Whether this was ever done is unclear from the published record.

- **Interaction of Actors Theory and machine collectives.** Pask's later Interaction of Actors Theory (IA), developed with Gerard de Zeeuw, extended CT to three or more actors entering and leaving conversations across time. IA is the natural framework for multi-agent systems. Was IA ever applied to purely machine collectives, or was it always theorized with human actors in mind?

- **Minimum variety for linguistic agents.** The Colloquy's asymmetry solution works for complementary drives (emit/reflect). The cyberneutics committee has characters whose propensities are more subtle than binary complementarity — they operate in high-dimensional linguistic space where the chameleon-mirror problem manifests as rhetorical convergence, shared framing assumptions, and collective blind spots. How much asymmetry is enough to prevent mimetic convergence in linguistically capable systems? Is there a minimum variety threshold (in Ashby's sense) for committee composition? The intuition is that the dimensionality of the propensity space must exceed the dimensionality of the dominant attractors in the LLM's response distribution, but this is not formalized.

- **Categorical formulation.** Bisimulation is a relation on objects in a category of labeled transition systems. The committee characters are objects; propensity defines the available morphisms (transitions); the calibration register tracks whether observed morphisms are consistent with specified propensity. When an absent party's transition system is unobservable, you work from trace alone — reconstructing the object up to bisimilarity from its output sequence. The question is whether there is a formal treatment of "trace-bisimulation" (reconstruction from observed output sequences rather than full transition access) that fits the absent-party case, and how it connects to the decorated cospan formalism in the palgebra.

- **What the Colloquy converged on.** Pask's published accounts describe the mobiles reaching satisfaction states, but the qualitative character of the converged state — its stability, its sensitivity to perturbation, whether multiple equilibria existed and how the system selected among them — is not well documented. For the cyberneutics committee, the analog question is: when committee characters with complementary propensities deliberate without a human gate, what do they converge on? The `wild/potential-to-sense/` essay argues that LLM-only discourse drifts toward statistical attractors without pragmatic grounding. The Colloquy's physical embodiment (light beams, mirrors, actual positions in space) may have provided grounding that purely linguistic LLM discourse lacks.

**Cross-references:**
- `wild/communicating-absent-parties/` — absent-party communication, frozen entailment meshes, taxonomy of absence
- `wild/cybernetics/gordon-pask.md` — conversation theory foundations, Pask biographical context
- `wild/cybernetics/conversation-theory.md` — CT formalism, entailment meshes
- `references/LLM-deliberation-prior-art--metacognition.md` — calibration register, meta-d', ground truth requirements
- `wild/committee-games/committee-as-open-game.md` — propensity as strategy-set constraint, selection functions
- `applications/narrative-immune-systems/` — bisimulation failure as detectable degradation, adversarial mesh-rewiring
- `wild/potential-to-sense/from_semantic_potential_to_situated_sense.md` — LLM-only discourse, pragmatic collapse, eigenforms
