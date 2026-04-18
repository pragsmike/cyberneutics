# Diary: Convergences — Freud, eigenforms, Rice, and local charts

**Date:** 2026-04-13

**Context:** A wide-ranging conversation touching several threads: completing Rid's *Rise of the Machines*, Freud as preparation for reading Deleuze and Guattari, a Facebook post on Zurek's einselection, the Morrin et al. *Lancet Psychiatry* paper, and Rice's theorem as the formal limit on alignment verification. An essay on AI safety in education ("The Blade Without a Handle") and a corresponding README section were drafted separately; this entry covers the material not captured there.

---

## The cybernetics visibility arc

Finished Rid's *Rise of the Machines*. The last chapter, "The Fall of the Machines," covers the tapering of the term "cybernetics" — a case where the ideas won and the label lost. Cybernetics fragmented into its successful children (control theory, AI, cognitive science, systems biology, network science) and the unifying frame dissolved.

A concrete marker from the shelf: a Scientific American compilation titled *Automatic Control* (SH-P3 in the inventory, sparse metadata). It was worth a dedicated special publication in its era. By the 1980s, when I went to engineering school, automatic control was just part of the wallpaper — background curriculum, not a named frontier.

The parallel to the current AI moment is direct. "AI" is in the special-publication phase now — everything foregrounded, named, hyped. The cybernetics trajectory suggests that if the useful parts succeed, they'll be absorbed into how things work and the term will fade. The question is whether anything important gets lost in that transition. With cybernetics, arguably yes: the integrative frame, the emphasis on circular causality and the observer's role, the connection between communication and control. Those didn't get absorbed into the wallpaper. They got left on the floor. Cyberneutics is partly an attempt to pick them back up.

## Rider and the concrete-to-abstract arc

A related artifact: John F. Rider's *Automatic Volume Control*, from the "Hour a Day with Rider" series, encountered around age ten. The book covers AVC — what we'd now call AGC (automatic gain control) — in consumer radios. It's feedback control as a concrete circuit problem: variable-mu tubes adjusting their own gain in response to signal strength. Years before any abstract framework for it.

Rider (1900–1985) was a prolific publisher of radio servicing manuals. Signal Corps background (Lt. Colonel), no confirmed RadLab connection despite adjacency to that world. The full AVC book is available online: [World Radio History PDF](https://www.worldradiohistory.com/BOOKSHELF-ARH/Technology/Rider-Books/Rider-Automatic-Volume-Control-1936-Hour-a-Day.pdf).

The progression from Rider's AVC circuits to Schaum's *Feedback and Control Systems* (DiStefano, SH-AN1) to the cyberneutics project traces the concrete-to-abstract arc: specific circuit → general discipline → methodology for structured deliberation. Each step absorbs the previous one and forgets the specificity that made it vivid. The early encounter with the concrete version — feedback as a thing tubes do — may be why the general theory felt like recognition rather than novelty when it arrived in engineering school.

## Freud as preparation for Deleuze

Planning to read some primary Freud before returning to *Anti-Oedipus*. The question: which branches of Freud's work are load-bearing for Deleuze and Guattari, and which can be set aside?

**Must understand:**

- The unconscious as a productive system (not a garbage bin but an active process that generates dreams, symptoms, slips). *The Interpretation of Dreams*, the metapsychology papers.
- Drive theory (Trieb/libido as psychic energy that attaches, redirects, sublimates). D&G transform this into desiring-production — keeping the energetics, rejecting the idea that desire is structured by lack. *Three Essays on the Theory of Sexuality*.
- The death drive (Thanatos). D&G take this seriously and rework it as the body without organs. Large stretches of *Anti-Oedipus* are unintelligible without it. *Beyond the Pleasure Principle*.
- The Oedipus complex and everything attached to it (castration, phallus as signifier, identification, superego formation). This is what D&G are dismantling. *The Ego and the Id*.
- The repression model. D&G reverse it: repression is secondary, imposed on a productive unconscious that was already working. The question shifts from "what has been repressed?" to "who benefits from organizing desire this way?"

**Background but not the main target:** The two topographies (conscious/preconscious/unconscious vs. id/ego/superego). Narcissism and ego as libidinal object. Transference (D&G argue the analytic session is itself a machine for producing Oedipal subjects).

**Can mostly set aside:** Dream interpretation mechanics (condensation, displacement). Most case histories, except Schreber (D&G use his psychosis as evidence that desire operates outside the Oedipal frame). The late cultural writings.

**The non-nuclear family problem.** Freud built the Oedipus complex around the bourgeois European nuclear family and treated it as universal. He didn't examine orphanages, communes, or matrilineal kinship structures — the theory doesn't have room for the question. Absent fathers are treated as pathological variations, not as evidence that the triangular structure might not be foundational. Malinowski raised the objection early, based on Trobriand kinship. Freud's camp responded by insisting the structure was deeper than surface arrangements — the kind of move that makes the theory unfalsifiable, which is not a compliment. This is exactly what D&G seize on: if Oedipus only shows up in nuclear-family cultures, it's not a discovery about the unconscious but a projection of a particular social arrangement onto it.

**The biographical irony.** Freud's own record — extended cocaine use with public denial, the seduction theory reversal (reframing patients' reports of sexual abuse as fantasy, under professional pressure), the probable affair with his sister-in-law Minna Bernays — adds up to a remarkable capacity for compartmentalization. Which is exactly what his own theory predicts. The man who built the theory of the unconscious was, by the available evidence, unable or unwilling to apply it to himself.

## Minsky's deliberate debt to Freud

The Freud → Minsky → cyberneutics committee pipeline lineage is not an accidental parallel. It's a direct, documented connection.

In an early paper on the Society of Mind theory (developed with Papert from the early 1970s), Minsky explicitly names Freud and Piaget as playing important roles. He describes mental abilities emerging from interactions between agents organized into "quasi-political hierarchies," culminating in "almost Freudian agencies for self-discipline that compare one's behavior with fragments of self-images." The architecture includes "critics" and "censors." Coherent personality emerges not from simple cybernetic principles but from the interaction of communities of agents under elaborate genetic control.

The key move Minsky made was computational: Freud's agencies are interpretive constructs (you infer the id from its effects); Minsky's agents are meant to be buildable. But the topology is the same — subsystems with different objectives, negotiating through interaction, producing emergent coherence that no single subsystem controls.

This is the rediscovery pattern noted in the memory: the structural insight — emergent behavior from interacting sub-agents — keeps being independently arrived at. Freud's id/ego/superego → Minsky's society of mind → the cyberneutics committee pipeline. Each iteration makes the interacting-agencies structure more concrete and more inspectable. The committee pipeline adds what neither Freud nor Minsky had: an explicit inspectable reasoning record of the negotiation.

## Zurek, von Foerster, and Deleuze: stability as relational

A Facebook post on Wojciech Zurek's einselection (environment-induced superselection) prompted a three-way comparison.

**Zurek's pointer states:** The quantum substrate contains superpositions — multiple possibilities coexisting. The environment continuously measures the system, and only states that are robust against that measurement survive. These "pointer states" are what we observe as classical reality. Stability is not intrinsic to the state; it's a product of the state's relationship to its environment.

**Von Foerster's eigenforms:** A fixed point of recursive operation — the thing that persists when you keep applying the process. Stability is what falls out of repeated interaction, not a property of the object.

**Deleuze's virtual-to-actual:** The virtual is a field of real but not yet actualized potentials, structured by relations (entanglement) rather than by identity. Actualization is the process by which the virtual differentiates into identifiable entities. Pointer states are what Deleuze would call the extensive, the individuated.

The convergence: all three say stability is relational, not intrinsic. What persists is what survives interaction with a structured environment. The divergence: Zurek treats the suppressed superpositions as physically inaccessible. Deleuze would keep them in the picture as the virtual ground that makes the actual possible — the unseen substrate without which the visible structure has no meaning. Von Foerster sits between them: eigenforms depend on the operator, change the operator and different things stabilize.

The cyberneutics connection: the committee pipeline's fan/funnel architecture is a selection-through-interaction process. Multiple scenarios (superpositions, virtual potentials) are generated; interaction with a structured evaluation environment (the committee, the rubrics, the adversarial process) selects the ones that are robust. The surviving resolution is a pointer state — stable under the interactions that actually occurred. The inspectable reasoning record preserves what was not selected, which is the Deleuzian move: keeping the virtual ground visible rather than discarding it.

## Morrin et al. and the epistemic ally convergence

The Morrin et al. *Lancet Psychiatry* paper (March 2026) proposes a safeguarding framework for vulnerable users of LLMs, built around four components. The structural mapping to cyberneutics is close enough to constitute a narrative proof convergence — clinical psychiatrists arriving at essentially the same architecture from a completely different direction.

| Morrin et al. component | Cyberneutics analog | Notes |
|---|---|---|
| Personalised instruction protocols | Charter | Setting the terms of engagement before the interaction begins |
| Reflective check-ins | Calibration register | Periodic reality-testing against the interaction's trajectory |
| Digital advance statements | *Gap* | Pre-commitments made while lucid about what the system should do if the user starts drifting. Cyberneutics doesn't have this explicitly and should consider it. |
| Escalation safeguards | Human gate | Recognition that the system is out of its depth; handoff to a person |

The key reframe: the AI as "epistemic ally" rather than therapist or friend. This is the rubber duck framing in clinical dress. The system helps you think; it doesn't think for you, and it doesn't pretend to care about you.

The difference in target population is instructive. Morrin et al. design for the most vulnerable users (psychosis-prone, emotionally dependent). Cyberneutics designs for functioning practitioners who need discipline to stay honest. The structural architecture is the same; the failure modes it protects against are at different points on the severity spectrum. This strengthens both: the underlying pattern (structured engagement with explicit epistemic boundaries) appears robust across populations.

The digital advance statement concept is worth importing. A user who is functioning well *now* could specify in advance: "If I start treating the AI as sentient, if I'm using it past 2 AM, if I'm asking it for emotional validation rather than analytical input — flag it." This is the cybernetic loop applied to the user's own cognitive state. The calibration register tracks the system's reliability; the advance statement tracks the user's.

DOI: 10.1016/S2215-0366(25)00396-7. Full text behind Elsevier's paywall.

## Rice's theorem, verification, and alignment as local charts

Rice's theorem: for any non-trivial semantic property of programs, there is no general algorithm that decides whether an arbitrary program has that property. "Semantic" means about what the program *does*, not what it *looks like*. This is a generalization of the halting problem to all interesting behavioral properties.

**Implication for LLM verification:** You cannot build a general-purpose verifier that takes an arbitrary LLM response and certifies it as correct. Not because we haven't found the right technique yet, but because the problem is provably undecidable.

**Implication for alignment:** Alignment is a semantic property of a system's behavior in context. Rice says you can't decide semantic properties generally. Therefore "aligned" is not a state you achieve; it is a condition you maintain, locally, provisionally, with known gaps.

**The manifold metaphor.** Each alignment technique is a local chart — a bounded patch of behavior space where you have verified coverage. RLHF covers some region. Constitutional AI covers an overlapping but different region. Red-teaming covers another. Each is locally valid. No finite atlas covers the whole manifold, because the behavior space of a sufficiently complex system is not compact — it's open-ended, and novel inputs can reach regions no existing chart covers.

The adversarial case — Crock, in cyberneutics vocabulary — is specifically the search for inputs that fall between charts, in the unmapped gaps. The Glenda/Crock dynamic is an alignment problem expressed as a mesh-rewiring attack: Crock needs Glenda's well-formed mesh for surface coherence but wants to redirect it toward extraction. The attack targets the gaps between charts.

**The time constraint.** Even if you could enumerate all the charts you'd need, you can't compute them fast enough. The system is deployed, interacting with billions of users, encountering novel situations faster than any verification process can cover them. You're charting the territory while people are already living in it, and the territory is being actively reshaped by inhabitants — including adversaries looking for the blank spaces.

This is why every other safety-critical domain (aviation, nuclear, medicine) does not claim its systems are "safe" in the absolute sense. They claim verification against a specific set of failure modes, with specific margins, under specific operating conditions. Step outside those conditions and the verification no longer applies. The charts are local.

The connection to the Bogdanov problem is direct. The Bogdanov brothers published papers with the syntactic structure of physics — correct formatting, plausible terminology, real citations — but whose semantic content was, by the consensus of the field, nonsense. They passed peer review. Structural checks cleared. Semantic verification failed. Rice tells you this will always be possible in principle. No verification system is airtight against all possible inputs. The question is not "can we achieve certainty?" but "can we build verification structures that catch the failure modes that actually occur in practice, often enough to be useful?"

That's an engineering question, not a logical one. And the answer is a qualified yes — qualified by the recognition that the verification is always partial, always domain-specific, and always defeatable by a sufficiently well-constructed counterfeit.

---

## Actions

1. Import the digital advance statement concept from Morrin et al. into the calibration register design. A pre-commitment mechanism for the user's own cognitive state, specified while lucid.

2. Add Rice's theorem to the theoretical foundations as the formal limit on verification. It belongs in the same neighborhood as the Bogdanov problem and the morphisms-are-primary principle: you can check relational structure (syntactic), you cannot generally verify semantic content.

3. The Zurek/von Foerster/Deleuze convergence on stability-as-relational should be written up as a section in the communicating-absent-parties thread or as its own wild/ note. The fan/funnel as a selection-through-interaction process, with the inspectable record preserving the virtual ground, is a clean connection.

4. The Freud → Minsky → cyberneutics lineage, now with documentation (Minsky's early paper explicitly naming Freud), should be added to the societies-of-thought essay or as a cross-reference from the committee architecture documentation.

5. Check Morrin et al. PsyArXiv preprint ("Delusions by design?", August 2025) for accessibility — may contain the full argument without Elsevier's paywall.

---

*Cross-references: [essays/blade-without-a-handle.md](../../essays/blade-without-a-handle.md) (companion essay drafted same session), [wild/diary/2026-03-27-resistance-to-ai-sensemaking.md](2026-03-27-resistance-to-ai-sensemaking.md), [references/ai_psychosis_evidence_report.md](../../references/ai_psychosis_evidence_report.md), [artifacts/character-skeptic-ai-reva.md](../../artifacts/character-skeptic-ai-reva.md), [essays/societies-of-thought-synthesis.md](../../essays/societies-of-thought-synthesis.md), [palgebra/reference.md](../../palgebra/reference.md) (morphisms-as-texts, verification stays inside the category), [wild/communicating-absent-parties/](../communicating-absent-parties/) (eigenform connection)*
