# Diary: Apophatic Steel and the Killed-Virus Vaccine

**Date:** 2026-05-03

**Context:** A weekend-ending conversation following from a few hours of cross-cutting reading: Cilliers's *Complexity and Postmodernism* alongside O'Reilly's residuality book, a paragraph of Deleuze's *Difference and Repetition*, a chapter of Agee's *Famous Men*, some Kleene after an Awodey video, a few pages of Taleb's *Antifragile*. Several threads converged on the same shape — what is preserved when rich relational structure is forced through serial channels — and the conversation produced a coinage worth holding onto. The entry closes with a section of notes-for-further-reading that came out of the conversation but that I have not yet worked through; that section is flagged as such.

---

## The pattern across the evening

Three convergences on relational-not-substantial framing surfaced over the course of the conversation: Cilliers via connectionism, Bradley via category theory, the fan/funnel via decision architecture. Three responses to the serialization problem: Faulkner, Agee, Cilliers. Three critiques of behaviorist accounts of internal models: Naur, Pask, the cyberneutics treatment of LLM reasoning. Each cluster reaches the third-convergence threshold — past coincidence; structural features of the underlying problem.

The unifying note is *what is preserved when rich relational structure is forced through serial channels, and what protocols can recover what's lost.* Apophatic steel preserves by exclusion. Killed-virus vaccines preserve form without function. Teachback recovers loss through iterated conversation. The fan generates multiple inadequate charts. Agee writes prose that has to be read at reading-speed. Different domains, the same family of solutions. The rest of the entry is the source material for the pattern.

## Cilliers, filled in

Kolmogorov and Chaitin as independent arrivals at the same idea. "Incompressible" means the shortest program is essentially the length of the sequence — there is no shorter description than the thing itself. Random strings are incompressible; "01010101…" compresses to "print '01' fifty times." Both Shannon entropy and algorithmic complexity peak at randomness, which is why neither is adequate to Cilliers's purpose: a random string is maximally informative by Shannon's measure and maximally Kolmogorov-complex, and yet it has no *structure*. The complexity-science tradition keeps reaching for something else — effective complexity, statistical complexity, logical depth. Cilliers points at the inadequacy without resolving it.

The two approaches to modeling complex systems are rule-based (symbolic) and connectionist. Cilliers's argument is that rule-based systems are inadequate to complex systems specifically because rules are static representations imposed on flux — the same move O'Reilly later borrows via the *phenomenal gap*. Connectionism is the better model because the structure *is* the pattern of interactions, not a representation of them. Cilliers reads connectionism through Saussure and Derrida, in 1998, before that was fashionable: meaning as differential relations across a network rather than as symbol-referent correspondence.

The science-without-philosophy aphorism is on page 13, in "Two Perspectives on Models." It is doing argumentative work — justifying the claim that models serve understanding rather than prediction — not serving as a free-floating epigram. The form echoes Kant's intuitions-without-concepts chiasmus from the *Critique of Pure Reason*, and Cilliers borrows the rhetorical structure consciously.

## Requisite variety as the load-bearing concept

Ashby's law and Cilliers's models-must-be-complex are duals — one about regulation, one about representation, both following from the impossibility of squeezing N bits of structure into fewer than N bits of channel without loss. This is the serialization problem in its most general form, and it shows up tonight for the third time in the stack: Faulkner's multiple narrators in *As I Lay Dying*, Agee's refusal of clean journalism in *Famous Men*, Cilliers's models in 1998. Three independent traditions naming the same constraint.

Where Cilliers and cyberneutics diverge is in the response. Cilliers stops at "we cannot predict, we seek to understand" — an epistemically modest post-structuralist position that leaves the practitioner with nothing to do except interpret. The fan/funnel takes the same impossibility as an *engineering* constraint: if no single representation is adequate, generate many representations, each inadequate in different directions, and read across them. The variance becomes diagnostic; the impossibility becomes informative. Cilliers as the philosopher's response to requisite variety; the fan as the engineer's response. Both honest, the engineer's version more useful.

## Hillis as the missing connectionist-engineer node

The Connection Machine as Society of Mind built in silicon — 65,536 processors gossiping at each other. Hillis was a Minsky student, and the Society architecture is in the stack already, which means there is a Hillis-shaped node that has not been drawn. He took the Society architecture seriously as engineering rather than as cognitive science. That puts him on the same node as Cilliers in a slightly different way: Cilliers reads connectionism *philosophically* and ends up with post-structuralism; Hillis builds connectionism *physically* and ends up with embarrassingly parallel hardware. Both downstream of the same insight — that the structure is the pattern of interactions — going opposite directions with it.

The Hillis line that prompted the inclusion is something like "I want to build a machine that will be proud of me." On memory, attribution solid enough to use conversationally but worth verifying against a primary source if it ever needs to be cited — possibly in *The Pattern on the Stone* or in one of the Connection Machine–era profile pieces. The reason it's the right line for this cluster is that *pride in* is a relational structure that requires the proud party to recognize the proud-of party as a project with standards. Pride is not a feeling; it is a relation with at least two terms, both of which have to have something like values. Hillis was setting himself a test his field has not passed.

## Bradley as the categorical machinery Cilliers reached for

Tai-Danae Bradley's enriched-category-of-language work formalizes meaning as the distribution of contexts an expression appears in — exactly the connectionist-Saussurean reading Cilliers was doing in prose, with the mathematical machinery he didn't have. The 2020 thesis (joint distributions as rank-one density operators, marginalization as quantum partial trace) is the thing *Complexity and Postmodernism* would have been if Cilliers had been a category theorist instead of a philosopher who happened to know about neural networks. Quantale-valued presheaves over a category of contexts is, in some real sense, the formalization of Cilliers's position. A real convergence, not a forced one. Belongs in the Bradley references file as another arrival-in-the-same-place from a different direction.

## Agee's *Famous Men* and the refusal to type-cast

The Emma chapter is the most charged passage on this theme. The poetry was a welcome change from technical reading after a day of philosophy and logic, and it is also doing structural work: the long looping syntax refuses to let Emma settle into a sociological type. Agee will not flatten her into "sharecropper's sister-in-law, twenty-something woman, rural Alabama, 1936" — the journalistic frame would falsify her into a category, and what he is seeing is irreducibly her. He writes around her, toward her, in sentences that refuse to land on a verdict. Walker Evans's photographs do the same refusal alongside the text: this face, this room, not "a sharecropper" or "a kitchen."

A through-line worth holding: Agee will not force Emma into a law-like generality, will not render her as an instance of a class. This is structurally adjacent to what Deleuze does with the law/repetition distinction in the paragraph I read this evening — law as instrument of generality, repetition as assertion of the singular. I have not yet worked out the relationship between Agee's literary practice and Deleuze's metaphysics myself; the closing section records what came out of the conversation as material to chew on rather than as conclusions reached.

## The pre-LLM corpus as scarce reference material

The technical name in the ML literature is *model collapse* — Shumailov et al., "The Curse of Recursion," 2023. The failure mode is what happens when models train on outputs from prior models: distribution narrows generation-on-generation, tails get amputated, the median wins. The pre-PFAS-blood-sample analogy I'd been using captures it well from the contamination side. The shipwreck-steel parallel surfaced independently in two unconnected conversations this week, which is the convergence threshold at which the framing stops being clever and starts being structural.

The technical name for that one is *low-background steel*: pre-1945 steel, mostly from the German fleet scuttled at Scapa Flow in 1919, used for shielding in radiation detectors and mass spectrometers because all post-Trinity steel is faintly radioactive from atmospheric testing. The contamination is global and atmospheric and irreversible. Same shape: pre-2022 text is the apophatic stock, the contamination propagates into how humans write unaided, and the boundary keeps moving backward as the contamination spreads forward. The 2019 corpus is more apophatic than the 2021 corpus. The economics shift accordingly: Project Gutenberg, the Internet Archive, and academic preprint servers have just become strategic resources in a way they were not a few years ago.

## Apophatic steel

The coinage of the evening, mine. Reference material constituted by what it does not contain. The negative-theology framing fits exactly — defined by what it isn't, valuable for what it lacks, knowable only through the absence of the contaminating signal. The category generalizes across radiation shielding, control samples in any experiment, dark frames in astronomical imaging, Faraday cages, the silence in Cage's 4'33", negative space in landscape painting, the unsaid in Pinter. Each is a referent constituted by exclusion.

The epistemological feature is that the apophatic reference is *more* informative than a positive reference, not less. A radiation detector calibrated against a known source tells you about that source; calibrated against apophatic steel, it tells you about every source the steel has been shielded from, including ones you didn't know to look for. The pre-LLM corpus has the same property — it is not a reference for any particular thing humans wrote, it is a reference for *human writing as such*, defined by being uncontaminated by the alternative. Without the apophatic corpus, model collapse becomes invisible because there is nothing left to compare against.

The temporal feature: apophasis with a half-life. The contamination keeps redefining what counts as uncontaminated. The boundary moves; the stock depletes; older corpora become more valuable in a way that has no analog in pre-PFAS blood samples (where the cutoff is fixed at 1950) but is exact for low-background steel (where new wrecks become more valuable as the existing supply is consumed by laboratory use). The corpus case is closer to the steel than to the blood.

*Apophatic corpus* for pre-LLM text. *Apophatic blood* for the 1950s samples. *Apophatic steel* as the named category. Worth a wild/ piece on its own; the cluster has reached the size where it deserves a name.

## The killed-virus vaccine

The Anderson reference is *Language Is a Virus* (1986), which borrows the line from Burroughs. My framing of the analogy: LLM-text as the active strain of the language-virus, a variant that has discovered a non-human replication path. Burroughs's claim taken seriously — that all language is viral, that humans are the substrate language runs on — makes the LLM the jump to a virus that has acquired its own ribosomes. Replication without comprehension. Model collapse as the mutation-accumulation phase of an unconstrained replicator.

The vaccine question becomes precise: what inactivated preparation could confer immunity? Recognition training (developing reader antibodies for LLM tells: the em-dashes, the tricolon-with-rising-stakes, the smoothed-over abstractions, the unearned authority). Provenance infrastructure (C2PA, content credentials, cryptographic signing). Critical literacy at scale, with the side-effect risk already documented in the dual-use entry from March — the same training that confers immunity to LLM-text also confers a cognitive distance that can be misused.

The conversation extended this to a stronger claim: that cyberneutics itself is a vaccine candidate, with committee transcripts as attenuated preparations of LLM-text presented in a frame that confers recognition rather than infection. I find it suggestive enough to record but want to think about whether it's a real reframe of the project or merely a pleasing one. If it survives reflection, it would give the project a public-health register complementary to the inspectable-reasoning-records register, and probably more legible to non-technical audiences. Holding it for now.

## Naur and Pask, paired

Naur's "Programming as Theory Building" diagnoses why team theory-transfer fails: the program is a *trace* of the theory the programmers built while writing it, and the theory itself lives only in their heads. The code records the decisions taken and not the alternatives considered, the constraints honored and not the constraints discovered-and-rejected. The standard responses — better documentation, better comments, better architectural decision records — are all attempts to *serialize the theory into text*, which is exactly the move Naur is warning against, because the theory is precisely what doesn't survive serialization. Same shape as Cilliers, same shape as Agee, same shape as everything else this evening.

Pask's teachback is the diagnostic instrument that *measures the loss*. Not a transmission mechanism — a verification mechanism. The new person teaches the theory back, in a form that would let a third person learn from them; the places where their teachback diverges from the original understanding are the places where the serialization failed. Teachback doesn't transfer the theory; it surfaces the gaps in the transfer that already happened. The pairing is more than additive: Naur without Pask leads to despair or to better-docs; Naur with Pask gives the practitioner something concrete to do.

Practical conditions for teachback to work. To a stranger rather than to the original explainer — teaching back to the original is corrupted by shared context, which defeats the diagnostic. Producing an artifact that can be diffed — verbal teachback is fine for quick checks but the value compounds when you can read both versions side by side. Bidirectional over time — six months in, the new person has built additions through contact with the system, and a teachback at that point reveals where the team's collective theory has drifted. Pask's deeper point was that conversation is how shared understanding *stays* shared, not just how it gets established once.

This is also a direct application of cyberneutics methodology to the team itself. The teachback is a tiny fan/funnel — the theory is the source situation, the new person's understanding is one chart of the manifold, the original explainer's understanding is another, and the diff between them characterizes the topology of where the theory resists transmission. Inspectable reasoning records, but for shared mental models rather than for decisions. For staff tomorrow, lead with the practical move and let the lineage stay implicit.

---

## Notes for further consideration: a Deleuzian reading of Agee

*This section is conversation output, not yet metabolized. Treat as syllabus for further reading rather than as a position I have taken. The points below are claims I want to sit with, check against the source texts, and either earn or reject as my reading of Deleuze deepens. The distinction matters: cross-tradition convergence claims are exactly the kind of move that's especially easy to confabulate when reading Deleuze with help.*

The frame Claude offered: Deleuze's argument in *Difference and Repetition* that representation operates by four coordinates — identity in the concept, opposition in the predicate, analogy in judgment, resemblance in perception. The "quadripartite yoke of representation." Type-casting Emma would activate all four at once, and Agee's prose is doing the work of refusing each operation as it would normally execute. Question to test on a re-read: does Agee's prose actually refuse all four, or only some? Worth re-reading the Emma passages with this lens explicitly in hand.

The technical sense of *singularity* in Deleuze: not just "a particular individual" but a point of inflection in a continuous variation, borrowed from differential geometry. A person encountered in their singularity is encountered *as* the place where the field of possibilities folds in a particular way that nowhere else folds in that way. Question: is this what Agee is doing, or is this being read in? The test would be to articulate what would distinguish "Agee renders Emma as singularity" from "Agee renders Emma with extreme particularity" — if the distinction collapses under examination, the Deleuzian reading is decoration rather than illumination.

The corresponding distinction on the reader's side: *encounter* versus *recognition*. Recognition closes the encounter before it happens; encounter forces thought. The book's difficulty — length, digressions, prefaces apologizing for itself — as the literary technology that sustains encounter against the reader's habit of recognition. Question: does this match what I actually experienced reading Agee tonight, or is it a post-hoc rationalization of his prose style? I should be able to answer this from memory of the reading, not from the framework.

A possible payoff for cyberneutics, if the reading holds: the funnel is at constant risk of becoming the recognition-machine, converting the fan's singular scenarios into instances of types. The committee transcripts as inspectable record would be the apparatus for refusing that conversion. The variance across multiple runs would not be noise around a true verdict but the inflectional structure of the singular field. *This is the strongest claim and the one most worth scrutinizing* — it's the kind of thing that sounds illuminating and might be merely flattering. Hold it lightly until I can defend it from the source texts.

Lineage to investigate when reading further: William James's radical empiricism (encountering the much-at-once of experience without prematurely sorting it), Whitehead's actual occasions (the singular event as the irreducible unit, not the type), and the modernist novelists Deleuze actually read (Faulkner explicitly, Joyce implicitly). If Agee converges with Deleuze, the convergence likely runs through this shared territory, not by direct line. Agee couldn't have read Deleuze; Deleuze probably never read Agee. The shared lineage is the explanation, if there is one.

Methodological note: the third-convergence pattern recommends taking cross-tradition convergence seriously. But the pattern is *also* the kind of move that's especially easy to confabulate when reading with conversational help. Independent verification — re-reading both texts on my own, in different sittings, and seeing whether the same connection re-presents itself — is the right test. If the connection survives unaided re-reading, it earns inclusion in the references. If it doesn't, this section is the record of the syllabus and that's enough.

---

## Actions

1. Add the page-13 Cilliers citation ("science without philosophy is blind…") to the references file with the "Two Perspectives on Models" section context. It is doing argumentative work, not serving as epigram.

2. Write up the requisite-variety / Cilliers / fan-funnel relationship as a short wild/ piece. Cilliers as the philosopher's response, fan as the engineer's response, both honest.

3. Verify the Hillis "machine that would be proud of me" quote against a primary source — likely *The Pattern on the Stone* or a *Wired* or *Whole Earth Review* profile from the Connection Machine years. Add a Hillis node to the connectionism cluster in the references either way; the Connection Machine as Society of Mind in silicon belongs in the lineage.

4. Add Bradley/Cilliers as a third convergence in the Bradley references file: enriched categorical structure as the math Cilliers reached for and didn't have.

5. Re-read the Emma passages in *Famous Men* with the Deleuzian quadripartite-yoke and singularity vocabulary explicitly in hand. The notes-for-further-consideration section above is the syllabus. The test is whether the Deleuzian reading earns its keep on a second reading without conversational scaffolding, or whether it dissolves on direct contact with the prose.

6. Draft a short wild/ piece on **apophatic steel** as a named category. Cluster includes: pre-LLM corpus, pre-PFAS blood samples, low-background steel, dark frames, control samples, Faraday cages, 4'33", negative space. Apophasis with a half-life as the temporal feature.

7. Sit with the **cyberneutics-as-vaccine-candidate** framing for a week before deciding whether to write it up. The pitch is attractive in a way that warrants suspicion. If it still seems sound after some distance, the public-health register is worth developing as a complement to the inspectable-record register. Note the dual-use risk already documented in 2026-03-29-ai-safety-dehumanization-dual-use.md.

8. The **Naur–Pask pairing** as a practical move for the team tomorrow. Lead with the practical pitch: docs aren't enough, teachback is the protocol that surfaces what didn't transfer. Let the lineage stay implicit. Document the staff outcome here in a follow-up entry.

9. Consider whether the **third-convergence pattern** itself deserves its own short note in research-programs/ rather than being repeatedly invoked in diary entries as folk wisdom. The threshold at which coincidence becomes implausible is doing real epistemological work and could use a stated formulation.

---

*Cross-references: [wild/diary/2026-02-17-bruner-kahneman-synthesis.md](2026-02-17-bruner-kahneman-synthesis.md) (paradigmatic/narrative dichotomy, symbolic vs. connectionist), [wild/diary/2026-04-09-stories-scenarios-serialization.md](2026-04-09-stories-scenarios-serialization.md) (serialization problem), [wild/diary/2026-04-13-convergences.md](2026-04-13-convergences.md) (Zurek/von Foerster/Deleuze convergence on relational stability — apophatic steel cluster connects here), [wild/diary/2026-04-11-biased-survivors-street-logic.md](2026-04-11-biased-survivors-street-logic.md) (biased survivors paragraph; pre-LLM corpus as apophatic), [wild/diary/2026-03-29-ai-safety-dehumanization-dual-use.md](2026-03-29-ai-safety-dehumanization-dual-use.md) (vaccine side effects), [references/bradley-cyberneutics-references.md](../../references/bradley-cyberneutics-references.md) (Bradley as Cilliers's missing math), [research-programs/metacognition/](../../research-programs/metacognition/) (third-convergence threshold), [palgebra/](../../palgebra/) (relational-not-substantial framing on the formal side)*
