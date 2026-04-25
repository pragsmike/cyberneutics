---
title: "The State of Residuality Theory: A Practitioner Survey"
author: "Survey by [unsigned]; subject: Barry M. O'Reilly's residuality theory"
audience: "Seasoned software architects, technical leads, and engineering managers"
type: survey
length_words: ~5200
status: "Survey paper drawing on the six O'Reilly papers archived in references/papers/"
companion_bibliography: residuality-bibliography.md
---

# The State of Residuality Theory: A Practitioner Survey

> A reading of Barry M. O'Reilly's residuality theory as it stands in the corpus of papers published between 2019 and 2023, written for a working architect who wants the current synthesis without having to reconstruct it from six separate papers.

This survey presents residuality theory as a single coherent body of work rather than as the chronological sequence in which O'Reilly developed it. The first nine sections describe the theory in its current form. A separate section near the end tracks the historical development for readers who want to see how the ideas accumulated, and what shifted along the way. A companion file, [residuality-bibliography.md](residuality-bibliography.md), gives the union of references cited across the corpus.

All citations resolve to local archives wherever possible. Source material outside the local repository is identified explicitly.

---

## 1. The problem residuality theory addresses

Software systems do not execute in a vacuum. They live inside organizations, markets, and societies that change in ways no requirements document and no risk register can capture in advance. The dominant tradition of software design — from object-orientation through SOA to microservices — treats this gap as a temporary inconvenience: tighten the requirements, refine the components, and the gap closes. Residuality theory begins from the opposite premise. The gap is constitutive. Architects do not build systems for a known environment; they build systems for an environment they cannot adequately represent, and the structural decisions they make today will constrain the system's response to events they cannot predict (O'Reilly 2019, [§1; §2](../../references/papers/Residuality-Oreilly-2019.md); O'Reilly 2021a, [§1](../../references/papers/Residuality-Oreilly-2021.md); O'Reilly 2023, [§1; §2](../../references/papers/Residuality-Oreilly-2023.md)).

The diagnosis is not novel — Parnas raised much of it in 1972, the Cynefin framework reframed it for management practitioners in the mid-2000s, and Nassim Taleb's *Antifragile* gave it a popular vocabulary in 2012. What residuality theory adds is a coherent design discipline that takes the diagnosis seriously: a vocabulary, a process, an empirical falsifiability move, and an underlying philosophical position that explains why most existing methods produce the failures they do.

This survey is for architects who want the result. The sections below set out residuality theory's current shape under nine headings, then return to the historical arc.

---

## 2. The current synthesis at a glance

Residuality theory's main propositions, as they stand across the 2019–2023 corpus:

1. **Hyperliminality.** Software is an ordered system embedded in a disordered environment. The architect must work across the boundary between the two without confusing one for the other (O'Reilly 2021b, [§2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md); O'Reilly 2022, [§1.3](../../references/papers/Residuality-Oreilly-2022.md)).
2. **Hyperliminal coupling.** Two software components that share an external stressor are coupled, even when no internal connection exists. This coupling is invisible to the designer until the stressor materializes (O'Reilly 2021b, [§2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md); O'Reilly 2022, [§1.4](../../references/papers/Residuality-Oreilly-2022.md)).
3. **The component metaphor is unexamined inheritance.** Architecture's accidental philosophy — essentialism, the causalities of certainty, machine-metaphor cybernetics, structuralism — produces fragile systems by treating dynamic environments as static (O'Reilly 2021a, [§The Component Metaphor](../../references/papers/Residuality-Oreilly-2021.md)).
4. **Residual causality.** Structural decisions impose future-destroying constraints that cannot be predicted at design time. Structure is itself a risk in the system, not just a way to mitigate risk (O'Reilly 2021a, [§Residual causality](../../references/papers/Residuality-Oreilly-2021.md); O'Reilly 2021b, [§1; §2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)).
5. **Residues are the design unit.** A residue is what remains of a system after a stressor impacts it — a working subset of components, infrastructure, people, and information flows. Architecture is a stack of residues, not a tree of components (O'Reilly 2020, [§2](../../references/papers/Residuality-Oreilly-2020.md); O'Reilly 2021a, [Abstract; §Moving Beyond](../../references/papers/Residuality-Oreilly-2021.md)).
6. **The two-step algorithm.** Software design is, in fact, always a random simulation of the environment followed by a network analysis of the architecture; residuality theory makes both steps explicit and amplifies them (O'Reilly 2022, [§2; §3](../../references/papers/Residuality-Oreilly-2022.md)).
7. **NKP analysis at the edge of chaos.** The architectural lens is N (number of components), K (max connections per component), P (bias toward an outcome). Tuning NKP toward the edge of chaos — stable enough to function, flexible enough to move between attractors — is the design target (O'Reilly 2022, [§3.2; §3.3](../../references/papers/Residuality-Oreilly-2022.md)).
8. **The residual index Ri.** A per-project empirical falsifiability test: divide the stressor list into training and testing sets, build the residual architecture from training, score the testing set against both naïve and residual architectures (O'Reilly 2020, [§3](../../references/papers/Residuality-Oreilly-2020.md); O'Reilly 2022, [§4](../../references/papers/Residuality-Oreilly-2022.md)).
9. **Processuality, criticality, difference.** The philosophical triad. Reality is process, not substance. The architect's goal is *criticality* (structural capacity to survive transitions between attractors), not correctness. Residues represent only what *differs* between attractor states (O'Reilly 2023, [§4–§5](../../references/papers/Residuality-Oreilly-2023.md)).

Each of these is developed in the sections that follow.

---

## 3. Hyperliminality: ordered software inside a disordered environment

A mechanical engineer designing a bridge knows the load characteristics, the material tolerances, and the relevant physics. The world the bridge will operate in is, for engineering purposes, the same world the engineer can model. Software is different. The code is an ordered, highly constrained system — testable, predictable, mappable. The environment in which the code executes is none of those things: it is the organization, the market, the regulatory regime, the social fabric, all of which are dynamic, growing, and unpredictable. O'Reilly calls this condition **hyperliminality**: an ordered system inside a disordered system (O'Reilly 2021b, [§2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md); O'Reilly 2022, [§1.3](../../references/papers/Residuality-Oreilly-2022.md)).

Hyperliminality is more than a slogan about complexity. It identifies a *structural* problem: the two regimes require different epistemologies. Inside the ordered software you can use the techniques of testing, measurement, and prediction. Inside the disordered environment those techniques produce the simulacrum O'Reilly (drawing on Baudrillard) calls the *component metaphor* — a model of the environment that the architect treats as the environment, with the messy reality safely out of frame (O'Reilly 2021b, [§5](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)). Successful architects, O'Reilly argues, intuitively switch between these epistemologies without making the switch explicit. Residuality theory is the attempt to articulate that switching as a discipline.

The technical consequence is **hyperliminal coupling**. If two software components each have a relationship with a node in the disordered environment — say, both invoke an authentication service that depends on the same upstream policy — they are coupled even when no direct internal call connects them. The coupling lives in the environment, not in the code. The architect cannot see it from inside the codebase, and standard tools for measuring coupling (call graphs, dependency matrices) do not reveal it. Hyperliminal coupling is what surfaces, all at once, when an external stressor activates the shared environmental dependency (O'Reilly 2021b, [§2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md); O'Reilly 2022, [§1.4](../../references/papers/Residuality-Oreilly-2022.md)).

The 2021 *Machine in the Ghost* paper draws the political consequence: as connectivity increases, hyperliminal coupling propagates through society. The June 2021 ransomware attack that closed 800 Swedish COOP supermarkets through a single payment-processing component is not a one-off — it is the structural pattern (O'Reilly 2021b, [§1](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)). Software architecture is, on this reading, autonomy infrastructure for hyperconnected society, and the architect's unexamined assumptions are now public-policy concerns.

For the practitioner, the operational claim is more modest: any design method that treats the environment as a controlled input will systematically miss the kind of failures that actually destroy projects. Hyperliminality says explicitly what most methods leave implicit, and residuality theory is built on that explicit acknowledgement.

---

## 4. The component metaphor and the philosophy architects don't know they hold

O'Reilly's most disruptive move is to argue that software architecture has a *philosophy*, that the philosophy is largely accidental, and that it is the source of most of the trouble. He calls the bundle of accidental commitments the **component metaphor** (O'Reilly 2021a, [§The Component Metaphor](../../references/papers/Residuality-Oreilly-2021.md)).

The component metaphor consists of four interlocking commitments:

- **Essentialism**, with its Platonic root: the belief that systems have ideal forms. Object-oriented class hierarchies, reusable components, SMART requirements, the enterprise-architecture repository — all are essentialist artefacts, treating the system as if it had a Platonic identity that the implementation merely instantiates (O'Reilly 2021a, [§Essentialism](../../references/papers/Residuality-Oreilly-2021.md)).
- **The causalities of certainty.** Following Stacey, O'Reilly identifies three causal models that the dominant management discourse leans on: formative causality (cause embedded in structure), rationalist causality (cause through human reasoning), and efficient causality (Newtonian cause-and-effect). Each makes prediction and control look reasonable. Together they sustain the belief that uncertainty can be reduced to manageable risk (O'Reilly 2021a, [§The Causalities of Certainty](../../references/papers/Residuality-Oreilly-2021.md); Stacey 2009).
- **Cybernetics as machine metaphor.** Beer's Viable System Model and adjacent control-theoretic approaches model human and organizational systems as machines, importing assumptions that the underlying complexity dissolves. O'Reilly is careful: the critique targets the *machine-metaphor* use of cybernetics, not second-order cybernetics in the von Foerster sense, but the dominant practitioner reading of "applying cybernetic principles to enterprise" is the targeted one (O'Reilly 2021a, [§Cybernetics](../../references/papers/Residuality-Oreilly-2021.md)).
- **Structuralism.** The mid-twentieth-century French intellectual movement that sought to ground social-system understanding in underlying abstract models. Requirements engineering, process modelling, and most of enterprise architecture inherit from structuralism without recognizing it (O'Reilly 2021a, [§Structuralism](../../references/papers/Residuality-Oreilly-2021.md)).

These commitments are unexamined. They were inherited accidentally from mathematics, physics, business school, and trend-driven popularization. The component metaphor is not actively defended in academic computer science because it is treated as too obviously correct to require defence — a "post-positivist approach is assumed" (O'Reilly 2021b, [§3](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)). The 2023 paper extends the diagnosis: substance philosophy, the focus on objects and their properties, is the deeper assumption underneath the four commitments. Process philosophy — the world as constant becoming rather than as static entities — is the alternative (O'Reilly 2023, [§2; §4](../../references/papers/Residuality-Oreilly-2023.md)).

The point is not that the component metaphor is always wrong. For simple, ordered systems, where the phenomenal gap between representation and reality is small, it works adequately, and that fact is precisely what causes architects to extrapolate it to complex environments where it does not. Residuality theory is not a replacement for the component metaphor; it is what the component metaphor *cannot* do. The two coexist in the same project (O'Reilly 2021a, [conclusion](../../references/papers/Residuality-Oreilly-2021.md)).

---

## 5. Residual causality: structure as risk source

If the component metaphor cannot describe the environment accurately, then any structural decision based on a component-metaphor representation imposes a constraint that the future environment will not respect. The constraint may be invisible at design time, may even produce short-term efficiency gains, but eventually it limits the system's ability to respond to events the architect did not foresee. O'Reilly calls this **residual causality**: structure itself is the risk in the system, not the mitigation (O'Reilly 2021a, [§Residual causality](../../references/papers/Residuality-Oreilly-2021.md); O'Reilly 2021b, [§2](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)).

The construction is via negativa. Architects cannot identify the perfect form for a system, but they can identify causes of future restriction and remove them — knowing that what remains is not the perfect form, only a less restricted one (O'Reilly 2021a, [§Residual causality](../../references/papers/Residuality-Oreilly-2021.md)). This is the inversion that gives residuality theory its name. Where conventional architecture asks "what is the right structure?", residuality asks "what does this structure foreclose?" The first question presupposes that a right structure exists. The second presupposes only that any structure forecloses something, and that the architect's job is to identify and remove the foreclosures that matter.

This shift has practical implications. It removes the requirement to predict the future — a requirement that, in a complex environment, is mathematically impossible (O'Reilly 2021b, [§1](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md), citing Peters 2019 on non-ergodicity). It also removes the requirement to specify causality precisely. In hyperliminal environments, the architect cannot reliably distinguish cause from effect; "constant conjunction" in Hume's sense is often the most one can say. Residual causality treats this Humean limitation as a working condition rather than an obstacle, using narratives of effect to drive design without requiring the architect to defend a theory of cause (O'Reilly 2021a, [§Residual causality](../../references/papers/Residuality-Oreilly-2021.md)).

The political extension matters. The 2021 *Machine in the Ghost* paper argues that residual causality is a structural threat to human autonomy in a hyperconnected society. Software design decisions made long ago, in different circumstances, for different reasons, constrain present and future human action invisibly. The constraint propagates through the network of inter-connected systems and cannot be undone by users or operators downstream of the design decision. The architect, on this reading, is not a neutral technician but a load-bearing actor in the maintenance of social autonomy (O'Reilly 2021b, [§1](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)).

---

## 6. Residues and the stressor-driven design process

A **residue** is what is left of a system after a stressor impacts it. It is the surviving and reconfigured subset of components, infrastructure, people, and information flows that the system uses to absorb the stressor and continue operating. A **stressor** is any event the system was not designed for. The residue is deliberately under-defined; in any specific project, it contains what is relevant to that environment and that stressor (O'Reilly 2020, [§2](../../references/papers/Residuality-Oreilly-2020.md); O'Reilly 2021a, [Abstract](../../references/papers/Residuality-Oreilly-2021.md)).

The architectural shift this enables is the move from **components** to **residues** as the primary design unit. Where conventional architecture asks "what components do we need?", residuality asks "what residues must exist if the system is to survive these stressors?" — and the stressors are deliberately wide-ranging, including events that are impossible, irrelevant, and improbable (O'Reilly 2020, [§3](../../references/papers/Residuality-Oreilly-2020.md)).

Operationally, residual analysis proceeds in steps that have remained stable across the 2020 introduction paper and the 2022 consolidation paper:

1. **Produce a naïve architecture** using current methods (OOP, SOA, microservices). This is the baseline against which residual gains will later be measured.
2. **Describe the system as a set of information flows** between actors. This breaks the system down into units of communication that prevent premature commitments to use cases or processes.
3. **List stressors.** Wide-ranging, deliberately playful, with no probability or impact filter. This is the central novelty: standard methodologies prune the stressor space using probability and impact; residuality theory expands it precisely because the unpredictable has, by definition, no probability the architect can reliably attach to it.
4. **Describe the residues** for each stressor and the functions that allow the residue to survive its defining stressor.
5. **Investigate component structure inside residues** using Design Structure Matrices (Cai et al. 2011) and incidence matrices, surfacing the dependencies and potential groupings that absorb stress.
6. **Consolidate residues to prevent contagion.** Components that appear in similar incidence patterns can share structure; components that diverge become services.
7. **Iterate using training and testing stressor sets** — bagging and boosting, in the machine-learning sense — to verify that the residual architecture handles stressors not used to design it.
8. **Compare** residual against naïve to confirm the residual architecture is more resilient.

The process produces an architecture that is multidimensional — each residue is a separate dimension of the system — rather than the two-dimensional component diagrams traditional architecture produces (O'Reilly 2020, [§4.1](../../references/papers/Residuality-Oreilly-2020.md)). The metaphor O'Reilly offers is "a stack of shadows we cannot see without turning various lights on and off" (O'Reilly 2020, [§2](../../references/papers/Residuality-Oreilly-2020.md), p. 877).

The residue concept absorbs much of what conventional architecture treats as separate. Resilience is not a property of the architecture; it is what the residual analysis makes visible. Antifragility is not a magic outcome; it is the directional result of consolidating residues across many stressors, including ones that turn out to be irrelevant — a phenomenon O'Reilly calls **non-linear system responsiveness**, drawing on the biological concept of exaptation. After enough stressors, new mitigations are increasingly absorbed by structure already present (O'Reilly 2019, [§5](../../references/papers/Residuality-Oreilly-2019.md); O'Reilly 2020, [§3](../../references/papers/Residuality-Oreilly-2020.md)).

The deliberately ill-defined character of the residue is itself a methodological choice. O'Reilly is explicit that any tightening of the definition — making residues into another taxonomy with formal categories — would reinstate the structuralism the theory rejects (O'Reilly 2021a, [§Moving Beyond](../../references/papers/Residuality-Oreilly-2021.md)). Residues are useful because they refuse to collapse into the static representations the component metaphor demands.

---

## 7. The two-step algorithm and NKP analysis

The 2022 consolidation paper makes a stronger claim than the 2020 introduction did: software design *in general* is a two-step algorithm — a random simulation of the environment followed by a network analysis of the software structure. Most methodologies just hide one or both steps. Residuality theory makes both explicit and amplifies their randomness and explicitness (O'Reilly 2022, [§2](../../references/papers/Residuality-Oreilly-2022.md)).

The first step, **random simulation**, is stressor analysis as described above. The 2022 paper's contribution is to recast it as Monte Carlo sampling of a state space too large to enumerate. Standard requirements engineering and risk analysis are random simulations too — they are just very poorly randomized ones, biased by experience, stakeholder politics, and the curse of dimensionality (O'Reilly 2022, [§3.1](../../references/papers/Residuality-Oreilly-2022.md)). Residuality's deliberate use of impossible and irrelevant stressors counters this bias by forcing the simulation to cover state-space that probability-weighted methods systematically prune.

The second step, **NKP analysis**, draws on Stuart Kauffman's work on Random Boolean Networks. Kauffman showed that complex systems made of autonomous interacting elements settle into a small number of recurring states — *attractors* — and that the structure of the network determines how many attractors a system has and how easily it moves between them. Three variables matter:

- **N** is the number of nodes (in software: components).
- **K** is the maximum number of connections a node can have (coupling).
- **P** is the bias of a node toward a particular outcome (predictability — pushed by contracts, schemas, policies, fewer branches in code).

Increasing N and K produces more attractors and harder-to-manage systems. Increasing P reduces outcomes and improves predictability. The architectural target is the **edge of chaos**: stable enough to function, flexible enough to move between attractors when stress demands it. Too ordered, and the system is brittle to unexpected change; too chaotic, and the system is unable to maintain function under any stress (O'Reilly 2022, [§3.2](../../references/papers/Residuality-Oreilly-2022.md), drawing on Kauffman 1993).

In practice NKP analysis is performed using two matrix techniques: **adjacency matrices** (directed, for dependency between nodes of the same type — components, flows, functions) and **incidence matrices** (mapping stressors against residues). The matrices reveal patterns that are difficult to see in code or diagrams: bidirectional coupling that lets stressors propagate; components that share incidence patterns and could be consolidated; dangerous stressors that activate many residues at once. Standard practitioner vocabulary — loose coupling, cohesion, granularity — translates directly into NKP-tuning operations (O'Reilly 2022, [§3.3](../../references/papers/Residuality-Oreilly-2022.md)).

The two-step algorithm gives residuality a comparative axis with other methodologies. Any design method can be reframed as a particular choice of how to randomize the simulation and how to perform the network analysis. That makes residuality theory empirically commensurable with its alternatives rather than incommensurable with them — an important move if the theory is to be testable rather than merely persuasive.

---

## 8. The residual index Ri and per-project falsifiability

The 2022 paper introduces the residual index **Ri** as a per-project empirical falsifiability test. The protocol:

1. Divide the stressor list into a training set and a testing set.
2. Build the residual architecture from the training set.
3. Score both the naïve architecture and the residual architecture against the testing set.
4. Compute Ri as a comparison of the two scores.

A residual index Ri > 0 means the residual architecture handled stressors not in its training set better than the naïve baseline did. This is direct empirical evidence — within the project — that the residual approach produced more resilient design (O'Reilly 2022, [§4](../../references/papers/Residuality-Oreilly-2022.md)). O'Reilly reports anecdotal Ri values of 0.27–0.57 from a hurried lab-scale experiment, while explicitly noting that the experiment was not run under stringent empirical conditions and does not constitute proof of efficacy.

The residual index is a striking move because it provides a falsifiability lever that most architectural methods do not. A team can run the protocol, get a number, and either confirm or disconfirm that residual analysis produced a better architecture *for this specific project*. The number is not a benchmark to compare across projects (idiographic concerns about software make that fragile), but it is enough to defeat the criticism that residuality theory is unfalsifiable in principle.

The bagging-and-boosting move — re-running the analysis with different training/testing partitions — comes directly from machine learning practice. The point is not to pick the best partition but to surface the architectural patterns that hold across partitions. Architectures whose Ri stays positive across many bagged runs are robust in a way that one-shot validation cannot demonstrate (O'Reilly 2020, [§3](../../references/papers/Residuality-Oreilly-2020.md); O'Reilly 2022, [§4](../../references/papers/Residuality-Oreilly-2022.md)).

---

## 9. Processuality, criticality, difference: the philosophical triad

The 2023 paper, *Residuality and Representation*, reorganizes the philosophical line of the theory around three concepts: **processuality, criticality, and difference**. They are the answer to a question the earlier papers gestured at but did not name: why do architects keep reverting to substance-focused static representations even after encountering residuality? The answer is that the entire intellectual culture of software architecture is substance-philosophical, and residuality theory is process-philosophical, and the two require different cognitive moves (O'Reilly 2023, [§3; §4](../../references/papers/Residuality-Oreilly-2023.md)).

**Processuality**. The world is constant becoming, not a collection of static entities. Residuality describes things as processes; substance is residue — the accidental leftover of processes, not the foundation. This is process philosophy in the Bergson/Whitehead/Deleuze line, but residuality stays pragmatic about it: the goal is not to defend a metaphysics but to describe systems in a way that lets architects work with flux rather than against it (O'Reilly 2023, [§4](../../references/papers/Residuality-Oreilly-2023.md)).

**Criticality**. The proper goal of architecture is not *correctness* — a hangover from software engineering's mathematical roots — but *criticality*: an internal structure capable of reorganizing to survive transitions between attractors. Correctness asks "does the system meet its specification?" Criticality asks "does the system retain function as the environment moves through its attractor space?" These are different evaluation targets, and the choice between them is consequential. Correctness rewards systems that succeed in stable environments and fail in unstable ones. Criticality rewards systems that survive the attractor transitions that destroy stable-environment optima (O'Reilly 2023, [§4.1](../../references/papers/Residuality-Oreilly-2023.md)).

**Difference**. Residues represent only what *differs* between attractor states, not the totality of the system. The architectural model is a stack of differences — what changes when this stressor hits, what changes when that one hits — rather than a unified picture of the whole. This is explicitly Deleuzian: identity is constituted through differences, not prior to them. The Deleuzian walk is the metaphor — the first walk is one experience; subsequent walks reveal seasonal change, altered paths, new buildings; the meaning of the walk is the sum of differences across repetitions, not the first traversal. Stressor analysis is the architectural form of this walk (O'Reilly 2023, [§5](../../references/papers/Residuality-Oreilly-2023.md), drawing on Deleuze 1994).

The 2023 paper introduces a fourth important concept: the **phenomenal gap**, drawn from Cilliers's reading of Kant. Noumena are things as they exist independent of our senses; phenomena are our impressions of them. In simple, ordered systems the gap is small and the impression suffices. In complex systems — and especially in enterprise environments — the gap is enormous and irreducible. The phenomenal gap is the technical name for what residuality theory has been describing all along under the labels of complexity, hyperliminality, and the limits of representation (O'Reilly 2023, [§3](../../references/papers/Residuality-Oreilly-2023.md)).

The triad gives residuality theory a coherent philosophical position to defend, rather than just a critique to deploy. Processuality is the metaphysical commitment; criticality is the architectural goal; difference is the representational unit. Each addresses a specific way the substance-philosophical default mis-fits the architect's actual problem.

---

## 10. Limits, open questions, and external critique

Residuality theory is a working program rather than a finished theory, and several of its commitments are contested.

**The unfalsifiability charge.** Critical reviewers of the 2024 *Residues* book — including a substantial Goodreads review — argue that the theory is "unfalsifiable" and "self-defeating," and that it dismisses effective principles like SOLID, DRY, and modularity patterns. The unfalsifiability claim is partly answered by Ri (per-project falsifiability is built in), but the broader concern — that a methodology insisting on the irreducibility of complexity cannot be tested across projects — is real. Residuality theory's response is that idiographic testability is the only kind of testability complex systems admit. Whether that response is satisfying depends on the reader's prior commitments. The book has not yet been engaged by a serious formal-methods critic, and that engagement is overdue.

**Definitional looseness.** The deliberate under-definition of "residue" is methodologically motivated (a tighter definition would reinstate structuralism), but it makes the theory difficult to teach and difficult to apply consistently. Practitioners report uncertainty about when they have correctly identified a residue — a complaint that O'Reilly acknowledges but does not fully resolve (O'Reilly 2021b, [§5](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)).

**The empirical case is thin.** The Ri values O'Reilly reports are anecdotal, from lab-scale experiments not run under stringent conditions. Larger-scale empirical studies, ideally by teams independent of O'Reilly's circle, do not yet exist. The theory's claim that systems designed using residuality outperform naïve baselines is plausible but not yet broadly demonstrated.

**Cybernetics critique applies selectively.** The 2021 *Philosophy* paper's critique of cybernetics targets Beer-style VSM applications and the machine-metaphor reading of cybernetic principles. The von Foerster line of second-order cybernetics — observer-included, recursive, anti-control — is not the target, but readers unfamiliar with the distinction can assume residuality theory rejects all cybernetics, which it does not (O'Reilly 2021a, [§Cybernetics](../../references/papers/Residuality-Oreilly-2021.md)).

**The post-structural line is genuine but selectively read.** Residuality theory leans on Serres (via Brown 2002), Latour, Deleuze, and Derrida. O'Reilly is explicit that residuality theory was discovered in practice and only retroactively connected to these sources; the philosophical reading is therefore one valid reading among possible readings of the same practice. A different philosophical anchor — pragmatist, second-order systems-theoretic, even certain neo-Kantian readings — could in principle support similar architectural conclusions. Residuality theory is not forced onto the post-structural line by its own internal logic (O'Reilly 2021a, [§Moving Beyond](../../references/papers/Residuality-Oreilly-2021.md)).

These limits do not invalidate the theory. They mark the open frontier of work that residuality theory invites rather than forecloses.

---

## 11. Historical development

For readers who want to see how residuality theory accumulated its current shape, the corpus arcs across roughly seven years and shows three distinct phases.

### Phase 1: Antifragility as the architectural target (2018–2020)

The 2018 Cutter Consortium *Executive Update* and the 2019 Procedia paper *No More Snake Oil* are practitioner-pitched and academic-pitched versions of the same argument. Antifragility, in Taleb's (2012) sense, is the architectural goal; agility is downstream of it; the four properties of antifragile ICT systems (modularity, weak links, redundancy, diversity, from Hole 2016) are the levers. Antifragile Systems Design — VUCA analysis, Flow First Design, ATAM review, modified FMEA — operationalizes these levers with no tooling beyond a spreadsheet. The vocabulary of later residuality theory (stressors, residues, naïve architecture) is not yet in place; the conceptual work is done through "VUCA elements," "mitigations," and "exaptation / nonlinear system responsiveness" (O'Reilly 2019, [§3–§5](../../references/papers/Residuality-Oreilly-2019.md)).

The 2020 paper *An Introduction to Residuality Theory* is where the named vocabulary appears. Stressors, residues, the incidence-matrix technique, Design Structure Matrices, K-reduction heuristics, training/testing stressor sets, and the residual index Ri all enter the theory in this paper (O'Reilly 2020, [§2; §3](../../references/papers/Residuality-Oreilly-2020.md)). The claim that residues, not components, are the primary unit of design is fully formed here. The justification for *why* the method works is comparatively thin in 2020 — Kauffman networks and attractor theory are gestured at but not philosophically developed.

### Phase 2: The philosophical underpinning (2021)

Two 2021 papers do the philosophical work the 2020 introduction deferred. The Procedia *Philosophy of Residuality Theory* (workshop paper, ~3,800 words) introduces the component metaphor and its four pillars, the concept of residual causality, and the post-structural anchoring in Stacey, Serres (via Brown), and Latour. Deleuze appears once, as an endorsement of post-structuralism's escape from rigid structures, but the substantive work is done by Serres and Latour (O'Reilly 2021a).

The MDPI *Philosophies* paper *The Machine in the Ghost* (~7,400 words, the only non-Procedia journal piece) develops the same arguments at journal length and adds the political/autonomy framing. Residual causality is reframed as a structural threat to human autonomy in a hyperconnected society. The reflexive section §5 narrates how residuality theory came into being through O'Reilly's own random walk through the literature — Taleb, Cynefin, Stacey, Peirce's Tychism, Prigogine, Heidegger, Serres, Latour, Baudrillard. This is the only paper where O'Reilly tells the theory's intellectual genealogy, and it explicitly frames random reading as stressor analysis applied to one's own worldview. The 2021 *Hyperliminal Coupling* Cutter piece (not archived locally) introduces the hyperliminal-coupling concept that the 2022 paper inherits (O'Reilly 2021b, [§5](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)).

### Phase 3: Complexity-science consolidation and process philosophy (2022–2023)

The 2022 paper *Residuality Theory, Random Simulation, and Attractor Networks* is the theoretical-consolidation paper. It reframes residuality theory as a complexity-science theory built on Kauffman networks and attractor theory; introduces the two-step algorithm (random simulation + NKP analysis); names NKP analysis as the architectural lens; formalizes the residual index Ri as the per-project falsifiability test. This is the single best paper for the residuality-as-complexity-science story (O'Reilly 2022).

The 2023 paper *Residuality and Representation* restates the philosophical line around the new triad of processuality, criticality, and difference. The lineage broadens: Kant gets the *Critique of Pure Reason* citation, Cilliers's bridge from complexity to post-structuralism is named explicitly, Deleuze and Derrida appear by name and at length, Spinoza is invoked via Deleuze, late Wittgenstein is acknowledged, Bateson's "form, substance and difference" becomes load-bearing. The phenomenal gap (from Cilliers's reading of Kant) becomes the technical concept underlying complexity. The 2023 paper is the better text for academic-philosophical audiences; the 2021 *Philosophy* paper is the better text for the concrete component-metaphor critique (O'Reilly 2023).

### What shifted across the arc

- **The theoretical anchor shifted twice**: Taleb (2019) → Stacey + Serres + Latour (2021) → Kant + Cilliers + Deleuze + Derrida (2023). The Taleb anchor never disappears, but it becomes background after 2021.
- **The unit of analysis matured**: VUCA elements (2019) → residues (2020) → residues + hyperliminality (2021) → residues + attractors + NKP (2022) → residues + difference + criticality (2023).
- **The empirical move shifted**: nonlinear system responsiveness as an aspirational claim (2019) → training/testing stressor protocol (2020) → residual index Ri as falsifiability test (2022).
- **The political stake emerged**: from a software-quality concern (2019) to a threat to societal autonomy (2021b).

The 2024 *Residues* book consolidates the theory for practitioners. It is paid (Leanpub, ~60pp.), not consulted directly in this survey, and reception is mixed: sympathetic reviewers describe it as accessible; critical reviewers raise the unfalsifiability and dismissal-of-SOLID concerns flagged in §10 above.

---

## 12. Reading paths

For the practitioner who wants to enter the corpus efficiently:

- **Quickest pedagogical on-ramp**: Eric Normand's *Residuality Theory* essay on Substack (May 2024). About 30 minutes, with a worked example (a country-based coupon banner service). It is the clearest single piece available for someone who has not read O'Reilly directly.
- **Operational mechanics**: O'Reilly 2020, *An Introduction to Residuality Theory*. Roughly an hour. The matrix techniques, training/testing protocol, and the consolidation step that the practitioner literature elaborates.
- **The complexity-science backing**: O'Reilly 2022, *Random Simulation and Attractor Networks*. About an hour. The two-step algorithm, NKP analysis, and the residual index Ri.
- **The philosophy**: O'Reilly 2021a (Procedia *Philosophy*) for the concise component-metaphor critique; O'Reilly 2023 (*Residuality and Representation*) for the processuality/criticality/difference triad and the phenomenal gap. Read in publication order, not reverse.
- **The political stake**: O'Reilly 2021b (*Machine in the Ghost*), *Philosophies* 6(4):81. About 90 minutes; the only paper with the autonomy framing and the only one with O'Reilly's first-person genealogy.
- **Talks**: NDC London 2024 *Introduction to Residuality Theory* (~50 minutes) and NDC Oslo 2024 *The Philosophy of Architecture* (~60 minutes) for O'Reilly in his own voice. The architectural-walks vocabulary is introduced at 31:16 of the Oslo talk.

The companion file [residuality-bibliography.md](residuality-bibliography.md) gives the union of references across the corpus, organized by role. It should be the first place to look for any cited work this survey mentions.

---

## Provenance note

This survey was written from the six O'Reilly papers archived in [`references/papers/`](../../references/papers/) (2019, 2020, 2021 *Philosophy*, 2021 *Machine in the Ghost*, 2022, 2023). It does not consult the 2018 Cutter *Executive Update*, the 2020 *There Is No Spoon* Cutter compilation, the 2021 *Hyperliminal Coupling* Cutter piece, or the 2024 *Residues* Leanpub book — those are referenced where the corpus mentions them but were not read directly. Critical reception of the 2024 book is acknowledged in §10 from the chronology's annotation, not from primary engagement with the critical literature.

The voice is third-person survey, not O'Reilly's own. Where the survey states an implication that O'Reilly does not himself make explicit, the implication is conservative — drawn directly from juxtaposing claims he does make — and presented as such.
