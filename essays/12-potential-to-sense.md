# From Semantic Potential to Situated Sense

*LLMs, Conversation, and the Collapse of Meaning*

> "Knowledge is not a matter of extracting content from a box; it is a matter of negotiating with a probabilistic partner whose contributions are real but structurally incomplete."

## Why This Essay Exists

The theoretical sequence through Essay 11 establishes a framework for collaborative sense-making with AI: Dervin's phenomenology of gap-bridging, von Foerster's second-order cybernetics, Deleuze's geometry of difference, Pask's micro-mechanics of understanding. The framework explains how the committee pipeline produces auditable deliberation, why adversarial structure matters, how teachback stabilizes understanding.

What the sequence so far has not settled is the question underneath all of it: *what is meaning, in this setting, such that these techniques operate on it?*

Pipeline practice commits the methodology to a specific answer. Human gates are treated as irreducible, not merely prudent. Multi-agent deliberation without eventual human participation is treated as drift-prone. These are operational commitments; they have not yet been argued from first principles. This essay provides the argument. It claims that meaning in LLM interaction is co-produced in coupled human-machine conversation rather than stored in model weights or extracted by prompting, and it shows what follows from that claim for how we use these systems.

The argument has four stages. First, what LLMs actually maintain (not stored meanings but structured fields of semantic potential). Second, what LLM-only discourse produces in the absence of human grounding (exploration with attractors and degeneracies, not pure creative freedom). Third, what human participation adds that models cannot supply each other (pragmatic collapse — relevance, correction, embodiment, consequences). Fourth, how this synthesizes into a cybernetic account of human-LLM interaction that gives the pipeline's human gates their theoretical weight.

---

## 1. Semantic Potential

The starting point is distributional semantics. The meaning of a word or expression is not an intrinsic property of the word in isolation; it is constituted by the pattern of relations the word enters into with other words across large bodies of text. You know what a word means, in important part, by knowing the company it keeps.

An LLM extends this dramatically. It does not merely encode which words co-occur with which; it models conditional continuation across enormous linguistic contexts. Given any prefix — a sentence, a paragraph, an entire exchange — the model has learned to assign probabilities to possible next tokens. The result is not a dictionary in which each entry maps to a fixed definition. It is a dynamic field: a highly structured probability distribution over possible continuations, shaped by everything the model has encountered in training and everything the current context has so far provided.

Before a response is generated, there is not yet a determinate meaning. There is a distribution. Many continuations remain open simultaneously. Some paths are highly probable, others vanishingly unlikely, but none has yet been selected. The model is not a storage system containing crisp propositional content that it retrieves and delivers on demand. It maintains a structured space of potential responses — a semantic potential field, organized by the enormous regularities of natural language but not collapsed to any single determination.

This framing has consequences. If meanings are not stored but enacted, then the question of what a model "knows" becomes inseparable from the question of how the model is prompted, by whom, and to what end. The "pachinko of stored literature" image from [Essay 06](./06-deleuze-difference-repetition.md) — all the patterns, relationships, and narrative structures compressed into the weights, with each token drop actualizing a path through that space — is exactly this picture in Deleuzian vocabulary. The model's weights encode a virtual field; each prompt actualizes one trajectory through it.

## 2. Concepts as Latent Structure

If meanings are not stored but distributed, what becomes of concepts? The temptation is to think of a concept as a packet — a unit of content that can be formed in one mind, encoded in language, transmitted through a medium, and unpacked by another. This picture has deep roots in the philosophy of language. But it sits uneasily with what we now know about distributional representations.

A more useful approach treats a concept not as a fixed entity but as a latent structural pattern recoverable from a distribution. Concepts are not stored at particular addresses; they are recurrent modes of organization within a relational field. The analogy is to eigenvectors in linear algebra: stable directions in a high-dimensional space that characterize the essential structure of a transformation without being identical to any particular instance of it. Conceptual content, on this view, is an invariant structure identifiable across many particular expressions, not something any single expression fully contains.

Formal concept analysis offers a complementary perspective. There, a concept is defined not as a token passed between minds but as a relation: specifically, the relation between a set of objects that share certain attributes and the set of attributes those objects share. Concepts are relational entities, not monadic ones. They depend on the structure of a domain and the way objects in that domain cluster together. A concept, in this sense, is not a thing in anyone's head — it is a structural regularity that emerges from a field of relations.

What both perspectives share is a move away from the container model of concepts toward a structural and relational model. A concept names an emergent regularity within a field of relations — something that can be identified and used without being fully possessed by any individual participant. This has immediate implications for how we think about LLMs: if concepts are latent structures in relational fields, then a model trained on natural language is the kind of system in which such structures can exist, at least in potential form.

This aligns with Pask's entailment mesh ([Essay 11](./11-conversation-theory.md)): a concept as a node in a cyclically mutually-entailing network. The mesh is not in the learner's head; it is the relational structure through which topics entail, support, and constrain each other. An LLM trained on natural language contains the statistical shadow of such meshes — but as potential, not as actualized understanding.

## 3. LLM-Only Discourse as Exploration of State Space

With this in place, we can describe what happens when language models interact only with each other, with no human participant in the loop. Each turn opens multiple possible continuations. The model responding to another model's output traverses the same probability landscape described above, but the constraints shaping that landscape now come entirely from prior model outputs rather than from any grounding in human purposes or lived situations.

Over the course of recursive exchanges, interesting things can happen. Local conventions emerge: particular phrasings that become stable within the exchange, ways of framing problems that persist across turns, something like a shared vocabulary that differs from what any single participant would generate independently. The system explores a state space, and that exploration can generate novelty — new combinations, new framings, conceptual moves that might not have appeared in any individual training corpus.

It would be tempting to describe this as pure creative freedom, semantic space travel unconstrained by external demands. That picture overstates the case. The landscape being explored is not flat or featureless. It has its own attractors: highly probable continuations that the models are systematically drawn toward, patterns that tend to recur because they are well-represented in training data, and degeneracies that pull toward cliché, circular elaboration, or self-reinforcing jargon. Without external grounding, LLM-only discourse can drift into loops that are locally coherent but globally disconnected from anything that matters to anyone.

LLM-only discourse is therefore not pure freedom but exploration inside a statistical landscape with its own topology. It is bounded by the attractors built into the models' representations. What it lacks is not variety — it can generate remarkable variety — but the kind of constraint that comes from outside the language system itself.

This is directly relevant to the pipeline's architecture. The fan stage generates divergent scenarios; the funnel stage produces convergent deliberation. Neither, operating in isolation, is reliable. The fan explores state space but cannot by itself distinguish productive exploration from drift. The funnel converges, but on what? Without external constraint, the funnel can stabilize on locally coherent eigenforms that are globally wrong — the premature convergence failure mode discussed in [Essay 06](./06-deleuze-difference-repetition.md). What prevents both failure modes is not more computation. It is the kind of constraint that only human participation introduces.

## 4. Human Participation as Pragmatic Collapse

When a human enters a conversation with a language model, something happens that is structurally analogous to measurement in quantum mechanics: a distribution over many possible states is resolved into something more determinate. The analogy is metaphorical rather than literal. There is no wave function collapse in a technical sense; the probabilities involved are not quantum probabilities; the mathematics of quantum measurement does not straightforwardly transfer. What the analogy captures is a structural pattern: the transition from a field of multiple live possibilities to something more specific and usable.

The term *pragmatic collapse* marks this transition while keeping clear that the mechanism is conversational, not physical. What humans bring to an exchange with a language model that models cannot supply for each other includes at least the following.

**Relevance.** Humans have purposes that extend beyond the conversation itself. They are not asking questions as an exercise in exploring semantic space; they are asking because answers matter for something they are trying to do or understand. This introduces a dimension of relevance that the statistical landscape of the model cannot generate from within itself.

**Correction.** Humans notice when responses miss the mark and say so, providing feedback that shapes subsequent turns. This is not merely a constraint on the response space; it is information about how the response space connects to a world the model does not independently observe.

**Embodiment and social norms.** Human meaning is grounded in a body with a history, a social position, a culture, and a set of practical engagements with an environment. When a human uses the word *heavy* or *warm* or *urgent*, these terms carry resonances no statistical distribution over text can fully capture, because they are anchored in kinds of experience that text does not exhaustively encode.

**Consequences.** Human participants are accountable for what they do with information in ways models are not. A doctor using a model to think through a diagnosis, a lawyer researching a precedent, a teacher designing a lesson — each brings a layer of stakes that organizes the interaction, making some responses genuinely better than others in a sense that goes beyond statistical plausibility.

Together, these contributions constitute pragmatic collapse. The human does not merely watch the model generate text; she selects among possibilities, rejects some continuations and reinforces others, demands coherence with lived situations, and brings the conversation to bear on things that matter in a world beyond the text window. In doing so, she converts semantic potential into *situated sense* — meaning that is not merely possible but actual, not merely consistent but useful.

## 5. Conversation Theory and the Constitutive Role of Exchange

The analysis converges with a tradition of thinking about communication that runs through Gordon Pask's conversation theory and the work of scholars including Anamaria Berea on communicative constitution. The shared thread is a rejection of what we might call the transmission model of communication: the idea that meaning is formed in a sender's mind, encoded in a signal, transmitted through a medium, and decoded by a receiver who ends up with approximately the same meaning the sender began with.

Pask's conversation theory, developed at length in [Essay 11](./11-conversation-theory.md), replaces this picture. Two interlocutors do not simply send packets of information back and forth; they engage in recursive exchange in which each attempts to demonstrate understanding of what the other has expressed, and the exchange continues until closure is reached. Meaning is not transferred; it is constructed through the process of attempting to construct it. What a concept means, in any operationally significant sense, is inseparable from the process by which interlocutors arrive at a shared ability to use it.

Berea's work extends this by insisting on the constitutive role of communicative dynamics. Communication is not a secondary layer of decoration applied to concepts already fully formed in individual minds. The communicative process is part of what makes a concept the concept it is. The patterns of uptake, correction, elaboration, and repair that characterize real exchanges shape the very content of what participants come to understand. Concepts become operationally real through conversational closure, not through storage or retrieval.

Applied to human-LLM interaction, this framework suggests that the question "what does the model mean by X?" may often be malformed. The model does not mean anything by X in advance of an exchange. What X means emerges from the exchange itself — from the way the human responds to the model's use of X, the corrections she offers, the contexts she supplies, the demands she makes. Meaning is not something the model outputs; it is something the human-LLM system produces together.

This is what the teachback mechanism from [Essay 11](./11-conversation-theory.md) tests. A successful teachback shows that the bridge across a conceptual gap is load-bearing — that what one participant said has been understood well enough by the other to be restated, applied, and defended. Teachback failure reveals where the mesh is thin. In human-LLM interaction, the role of the human is not only to provide prompts but to perform teachbacks: to re-articulate what the model has offered in the human's own terms, apply it to the human's situation, and test whether it holds.

## 6. Eigenforms and Stabilized Distinctions

Von Foerster's concept of the eigenform, introduced in [Essay 04](./04-cybernetics-and-observation.md), offers another way to think about stabilization. An eigenform is a fixed point — a form that, when operated upon, yields itself. It is not a pre-existing object that the operation discovers; it is a stable form that the recursive operation itself produces and maintains.

In the context of cognition and communication, von Foerster used eigenforms to think about how stable experiential objects arise from the continuous activity of a nervous system. We do not perceive a chair and then separately construct a concept of the chair; the stable experience of chairness is the product of recursive neural operations that have converged on a fixed form. The object is constituted by the operations that recognize it.

A concept as it functions in a human-LLM exchange can be understood as an eigenform of the conversational process — a stable distinction produced and maintained by recursive activity of the exchange rather than stored in either participant's representations in advance. The model brings structural potential; the human brings grounding constraints; the conversation, through its recursive adjustments, converges on something stable enough to be used.

This synthesis draws together the threads developed so far. From distributional semantics comes the picture of latent structural modes — regularities in a relational field. From conversation theory comes the picture of meaning as achieved through recursive exchange. From von Foerster comes the constructivist account of stable forms produced by operations. The synthesis is a picture of concepts as *temporary eigenforms of coupled human-machine conversations*: stable enough to function, but dependent on the ongoing dynamics of the interaction that produces them.

Meaning is therefore neither a purely internal representation sitting inside the model nor a mere external label applied by the human. It is a stable form enacted in recursive interaction — something real, but real as a process rather than as a static object.

The pipeline's treatment of eigenforms as resolution-content invariants across Probe runs (the repeated-pipeline-execution technique developed in [Essay 10](./10-decisions-under-uncertainty.md)) is the formal expression of this account. What recurs across many walks of the decision landscape is what the process has stabilized on — what it has collapsed into a usable form. What varies across walks is residue: local, trajectory-dependent, informative about particular walks but not about the landscape.

## 7. Against the Container Model of Meaning

It is worth making explicit what this account rejects, because the container model of meaning has enough intuitive appeal to resurface even among people who know better. The container model says, roughly: meanings are objects; minds (or now, models) are containers; communication is the transfer of objects from one container to another; and the quality of communication is measured by how faithfully the object arrives at the destination matching what was sent.

Applied to LLMs, this model generates a series of misleading questions. Does the model "really understand" what it says, or is it just shuffling tokens? Does it "actually have" the concept of justice, or is it simulating having it? Is there a meaning "in" the model, or just statistical patterns that mimic meaning? These questions all presuppose the container model and ask whether the model qualifies as a proper container.

The account developed here suggests these questions are ill-posed. Concepts are not packets sitting inside the model, waiting to be extracted. Communication is not the delivery of intact conceptual cargo from model to user. Text does not carry meaning by itself, apart from the interpretive systems — human and computational — that engage with it. What looks like "meaning in the model" is better understood as structured potential that becomes meaning only in the context of an interpretive exchange.

The replacement picture: meaning is a temporary stabilization in a coupled system consisting of the model, the prompt history, the user, and the larger context of use. It is not located at any one node. It is a property of the system's configuration at a moment in its dynamic evolution. When that configuration changes — a new user takes over, a new purpose is introduced, the conversation shifts — the stabilization shifts too, and what counted as meaning a moment ago may need to be renegotiated.

This is not deflationary. It does not mean LLMs are meaningless or that human-LLM interactions are merely the appearance of communication. It means that meaning, here as elsewhere, is something that *happens* rather than something that is stored. The container model was always too static; the conversational model better captures what meaning is, even in human-to-human exchanges. LLMs simply make the dynamic, constructed character of meaning harder to ignore.

## 8. A Cybernetic Model of Human–LLM Interaction

The analysis has moved through several frameworks — distributional semantics, formal concept analysis, conversation theory, constructivist eigenforms. That picture can now be given a unified formulation in cybernetic terms.

In cybernetics, the unit of analysis is not the individual component of a system but the organization of the whole — the pattern of information flow and feedback that constitutes the system as a system. When we apply this to human-LLM interaction, the appropriate unit of analysis becomes the interaction itself, not either participant taken alone.

The interaction can be described as a control loop. The human introduces a prompt, which functions as a control signal: it specifies the current state of the conversation and the direction in which it should proceed. The model generates a response, which functions as a proposal: a candidate output that satisfies the statistical constraints of the context as the model has represented them. The human reacts to the response — accepting it, correcting it, elaborating on it, redirecting the exchange — and this reaction constitutes feedback that re-enters the system as the next prompt. Through this cycle of prompt, proposal, and feedback, the system progressively constrains the space of acceptable continuations and converges on phrasings, framings, and distinctions both participants can work with.

Stable shared terminology that emerges from a sustained exchange is an example of temporary closure in this loop: a point at which recursive adjustment has produced something fixed enough to be relied upon, at least for the duration of the conversation and purpose at hand. This closure is not permanent, and it is not pre-given. It is achieved through the dynamics of the coupled system.

The cybernetic picture also clarifies what makes a prompt good or bad. A good prompt is not simply one that is grammatically well-formed or that contains the right keywords. It is one that effectively constrains the proposal space in the direction of what the human actually needs — that introduces enough structure to guide the system toward useful closure while leaving enough openness for the model's structural potential to contribute something the human could not have generated alone. Prompt engineering, on this view, is *loop tuning*: the human is adjusting the control signal to improve the dynamics of the coupled system.

This is also where the framework's human gate earns its theoretical weight. In [Essay 09](./09-narrative-immune-systems.md), the human gate is described operationally as the point where pipeline output is committed to or revised. The account here provides the epistemological argument: the human gate is not merely prudent, it is load-bearing. Without it, the pipeline's outputs are not yet meaning — they are structured potential in search of grounding. The human gate is where potential becomes sense.

The unit of analysis should therefore be the interaction, not either participant alone. Neither the model nor the human "has" the meaning that emerges from a good exchange. Both contribute to a coupled process whose output is more than either could produce independently.

## 9. Implications

**For AI theory.** Studying meaning in LLMs primarily through analysis of model weights or activation patterns — while valuable — is necessarily incomplete. Meaning in these systems is dynamic and interactional, not simply representational. A full account requires attention to the conversational dynamics through which the model's structural potential is actualized. This points toward interaction-centered approaches to evaluation and interpretability, in which the quality of a model's representations is assessed not in isolation but in the context of the exchanges those representations support.

**For interface design.** If meaning is co-produced rather than extracted, then good human-LLM interfaces should be designed to support the collaborative dynamics of production rather than merely optimize for speed of retrieval. This means supporting iterative grounding — the progressive convergence on shared framings that good conversations achieve. It means building in affordances for teachback and clarification, so users can signal when the model's proposal has missed the mark and redirect efficiently. It means making visible the degree to which the current exchange has achieved stable closure and the degree to which the meaning of terms in play remains contested or underdetermined.

**For epistemology.** The dominant metaphor for knowledge extraction from AI systems — the idea that the model is a box containing information, and that prompting is the method of retrieval — needs revision. Knowledge in the context of LLMs is not a matter of extracting content from a box; it is a matter of negotiating with a probabilistic partner whose contributions are real but structurally incomplete. The user is not a passive recipient of information; she is a participant in the construction of meaning, and the quality of what she gets depends essentially on the quality of her participation. This is epistemologically demanding, but more accurate than the extraction model.

**For multi-agent AI.** The analysis of LLM-only discourse as exploration of a statistical landscape — rich in possibilities but vulnerable to attractors and degeneracies — has direct implications for multi-agent AI systems. As these systems become more prevalent, the question of grounding becomes more urgent. A society of language models can generate internally consistent and elaborately structured semantic worlds. But without human participation, those worlds are not grounded in anything beyond the statistical regularities of training data. Human participation remains crucial not merely as a source of feedback on performance, but as the mechanism by which the system's outputs are anchored to a reality that extends beyond the text.

This is the answer to a standing question about the cyberneutics pipeline: why can the fan and funnel not simply be composed and run to completion without human intervention? The pipeline can be composed, and it can be run. But what comes out the other end is not yet decision-ready output. It is structured potential. Without the human gate, the output is a proposal generated by a system operating entirely within its own statistical landscape. With the human gate, the output is situated sense — meaning that has been converted from potential to actual by the pragmatic collapse only a human participant can supply.

## 10. Conclusion

The path traced in this essay runs from the distributional foundations of semantic representation in large language models to an account of meaning as co-produced in conversational interaction. It passed through several key ideas: that LLMs maintain structured fields of semantic potential rather than storing determinate meanings; that concepts are best understood as latent structural regularities emergent in relational fields; that LLM-only discourse explores a statistical landscape with its own attractors and degeneracies; that human participation introduces pragmatic, embodied, and social constraints that convert potential into situated sense; that conversation theory and constructivist accounts of eigenforms provide frameworks for understanding how this conversion happens through recursive interaction; and that the appropriate unit of analysis for questions about meaning in these systems is the interaction itself, not either participant alone.

The opening image — LLMs traversing a probability landscape, humans collapsing that landscape into something usable — can now be stated more precisely. The collapse is pragmatic rather than physical: it is driven by purposes, corrections, embodied resonances, and social stakes that no purely statistical system generates from within itself. What results from the collapse is not a fixed meaning that gets stored anywhere. It is a temporary eigenform of a coupled human-machine conversation — stable enough to be used, but dependent on the ongoing dynamics of the exchange that produced it.

The implications reach beyond AI theory into questions about knowledge, design, and the conditions under which human-machine interaction can be genuinely productive. But the most fundamental implication is also the simplest: what looks like "meaning in the model" is better understood as temporary stabilization in a conversational system. The model brings potential; the human brings grounding; the conversation brings them into contact. Meaning, as always, is something that happens between participants — not something any one of them possesses alone.

This is the epistemological argument underneath the methodology's operational commitments. Pipeline human gates are not a concession to user expectations or a defensive measure against hallucination. They are the mechanism by which structured potential becomes situated sense. Removing them does not produce a faster pipeline — it produces a pipeline whose outputs have not yet become meaning.

---

## Further Reading

**On distributional semantics and latent structure**:
- Bradley, Tai-Danae, Terilla, John, and Vlassopoulos, Yiannis. "An Enriched Category Theory of Language: From Syntax to Semantics." *La Matematica* (2022). The enriched category structure of text that makes the "semantic potential" framing precise.
- Bradley, Tai-Danae, and Vigneaux, Juan Pablo. "The Magnitude of Categories of Texts Enriched by Language Models." *Theory and Applications of Categories* 44(37) (2025). Develops language category structure for LLM-generated text specifically.

**On conversation theory and eigenforms**:
- See Essay 11 (Conversation Theory) and Essay 04 (Cybernetics and the Observer Problem) for the development of the Paskian and von Foersterian material this essay builds on.
- Von Foerster, Heinz. *Understanding Understanding* (2003). The eigenforms essays are foundational here.

**Related artifacts**:
- [Adversarial Committees](../artifacts/adversarial-committees.md) — the deliberation element where pragmatic collapse is distributed across characters and a human gate
- [Palgebra: Decorated Texts](../palgebra/decorated-texts.md) — the formal treatment of the human gate as a collapse operator

---

**Previous essay**: [Conversation Theory](./11-conversation-theory.md) — the micro-mechanics this essay provides the epistemology for.

**Related in the sequence**:
- [Essay 04](./04-cybernetics-and-observation.md) — second-order cybernetics and eigenforms
- [Essay 06](./06-deleuze-difference-repetition.md) — virtuality, actualization, and charts on a manifold
- [Essay 09](./09-narrative-immune-systems.md) — the human gate as narrative immune function
- [Essay 10](./10-decisions-under-uncertainty.md) — eigenforms as Probe-run invariants
