---
title: "The State of Residuality Theory: A Practitioner Survey"
author: "Survey by [unsigned]; subject: Barry M. O'Reilly's residuality theory"
audience: "Seasoned software architects, technical leads, and engineering managers"
type: survey
length_words: ~6800
status: "Survey paper drawing on O'Reilly's published works: the six papers (2019–2023) archived in references/papers/, the 2024 Leanpub book Residues, and the practitioner reception material gathered in 2026-04."
companion_bibliography: residuality-bibliography.md
---

# The State of Residuality Theory: A Practitioner Survey

> A reading of Barry M. O'Reilly's residuality theory as it stands in his published works as of April 2026 — six Procedia/Philosophies papers (2019–2023) and the 2024 Leanpub book *Residues* — written for a working architect who wants the current synthesis without reconstructing it from the source documents one at a time.

This survey presents residuality theory as a single coherent body of work rather than as the chronological sequence in which O'Reilly developed it. The first nine sections describe the theory in its current form, drawing on the papers as the rigorous foundation and the book as the practitioner-pitched compression. Section 11 tracks the historical development across papers and book; section 12 treats the 2024 book in its own right (its register, its specific additions, its omissions, its reception, and its open gaps); section 13 gives reading paths. A companion file, [residuality-bibliography.md](residuality-bibliography.md), gives the union of references cited across the corpus.

All citations resolve to local archives wherever possible. The 2024 book cannot be quoted at length per its commercial copyright; it is referenced by chapter and subsection rather than by page number, and quotations are kept to short fair-use snippets. Source material outside the local repository is identified explicitly.

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

The 2024 book sharpens the distinction by importing the technical concept of **ergodicity** from the complexity-science literature. An ergodic system is one whose future behaviour is already expressed in its past — past trajectories sample the same state space the future will sample, so prediction is in principle possible. A non-ergodic system is one in which past sampling does not exhaust future state space; the future contains genuinely new configurations the past did not contain (O'Reilly 2024, *Architecture / Ergodicity and Hyperliminality*). Software is mostly ergodic; the human systems software is embedded in are not. Hyperliminality, in the book's restated definition, is "a complicated, ergodic, ordered system [executing] inside a complex, non-ergodic, disordered context." This is a tighter formulation than the corpus's earlier "complex environment" framing, and it gives the term a falsifiability anchor: one can ask, of a specific system, whether its environment's past trajectories sample the future state space — a question that "complex" alone does not afford.

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

A **residue** is what is left of a system after a stressor impacts it. It is the surviving and reconfigured subset of components, infrastructure, people, and information flows that the system uses to absorb the stressor and continue operating. A **stressor** is any event the system was not designed for — anything outside the architect's current model of the context, in the 2024 book's sharper formulation. The residue is deliberately under-defined; in any specific project, it contains what is relevant to that environment and that stressor (O'Reilly 2020, [§2](../../references/papers/Residuality-Oreilly-2020.md); O'Reilly 2021a, [Abstract](../../references/papers/Residuality-Oreilly-2021.md); O'Reilly 2024, *Walking with Stressors*).

The architectural shift this enables is the move from **components** to **residues** as the primary design unit. Where conventional architecture asks "what components do we need?", residuality asks "what residues must exist if the system is to survive these stressors?" — and the stressors are deliberately wide-ranging, including events that are impossible, irrelevant, and improbable (O'Reilly 2020, [§3](../../references/papers/Residuality-Oreilly-2020.md)).

### Stressors versus the concepts they are most often confused with

The 2024 book devotes a chapter to drawing boundaries between *stressor* and the seven concepts practitioners most often collapse it into (O'Reilly 2024, *Walking with Stressors / Stressors, Requirements, Risks, Scenarios, and Edge Cases*). The boundaries matter because each of the seven represents a way of pruning the stressor space that residuality theory specifically refuses.

- **Requirement.** A statement of desire by a stakeholder at a moment in time. Requirements presuppose that the relevant features can be enumerated; stressors do not.
- **Constraint.** Treated as fixed by the design, but in fact moving as the context moves. Constraints are stressors-in-waiting.
- **Edge case.** A patch to an existing abstraction. Frequent edge cases are a sign that the abstraction itself is wrong and needs stressing — not that the abstraction is correct and the case is exceptional.
- **Scenario.** A likely event, socially acceptable to discuss. Scenarios are pruned by stakeholder consensus; stressors are produced precisely to defeat that pruning.
- **Risk.** An event with attached probability and impact, both usually opinion. Stressors discard probability and impact at the generation stage on principle.
- **Volatility.** Something that changes. In a complex environment everything changes, so the term carries no information.
- **Chaos engineering.** Production-time fault injection. Useful but post-architectural; cannot inform design decisions before the architecture exists.
- **Resilience.** Treated separately in §10 below. The book's claim, briefly: resilience is the system's capacity to *return to* a stable attractor; residuality is the architecture's capacity to *move between* attractors.

The taxonomy answers a recurring objection — "you have just renamed a thing we already had a word for" — by showing that each of the seven existing concepts presupposes a kind of pruning the stressor concept exists to refuse.

### Robust software inside a residual architecture

The book makes a distinction the papers leave implicit. The complicated software *inside* a residue — the code itself — should be *robust*: stable, predictable, well-engineered. The architectural envelope *across* residues should be *residual*: flexible, capable of moving the system between attractors as the environment moves. The book's compressed formulation: "Software should be robust but its architecture should be residual" (O'Reilly 2024, *Walking with Stressors / Resilience*).

The distinction is intellectual hygiene. Without it, residuality can be misread as advocating instability *inside* the system, which it does not. The complicated core is the ergodic part, and traditional engineering — testing, type discipline, formal methods — applies inside it. The disordered envelope is the non-ergodic part, and residual analysis applies to it. The architect's mistake, in the book's framing, is applying the techniques of either regime to the other.

### Operational steps

Operationally, residual analysis proceeds in steps that have remained stable across the 2020 introduction paper, the 2022 consolidation paper, and the 2024 book:

1. **Produce a naïve architecture** using current methods (OOP, SOA, microservices). This is the baseline against which residual gains will later be measured.
2. **Describe the system as a set of information flows** between actors. The 2024 book elevates this step explicitly: a *flow* is the movement of information between two actors (a person, a group, a company, or a software component), and flow-based decomposition replaces the process-based or use-case-based decomposition that O'Reilly (citing Parnas 1971) treats as the central error of conventional architecture (O'Reilly 2024, *A Worked Example / Flow Analysis*). Use cases and processes lock the architecture into a particular sequence of operations and make residue extraction harder; flows do not.
3. **List stressors.** Wide-ranging, deliberately playful, with no probability or impact filter. This is the central novelty: standard methodologies prune the stressor space using probability and impact; residuality theory expands it precisely because the unpredictable has, by definition, no probability the architect can reliably attach to it. The 2024 book recommends three upstream aids for generation — PESTLE analysis, the Business Model Canvas, and Porter's Five Forces — as scaffolding when the architect's intuition runs dry; the breadth-discipline is then layered on top (O'Reilly 2024, *Walking with Stressors / Coaching Stressor Analysis*).
4. **Describe the residues** for each stressor and the functions that allow the residue to survive its defining stressor.
5. **Investigate component structure inside residues** using Design Structure Matrices (Cai et al. 2011) and incidence matrices, surfacing the dependencies and potential groupings that absorb stress.
6. **Consolidate residues to prevent contagion.** Components that appear in similar incidence patterns can share structure; components that diverge become services. The 2024 book renames the second step of the methodology as *contagion analysis* — the investigation of how stress spreads through hyperliminally-coupled components — with NKP analysis (the 2022 paper's name) absorbed into it as one tool among several.
7. **Iterate using training and testing stressor sets** — bagging and boosting, in the machine-learning sense — to verify that the residual architecture handles stressors not used to design it.
8. **Compare** residual against naïve to confirm the residual architecture is more resilient.

The 2024 book describes this layered process under the rubric of *safety nets*: each step catches what earlier steps missed (O'Reilly 2024, *A Worked Example / Safety Nets*). Stressor analysis catches what the naïve architecture missed; contagion analysis catches the dangerous coupling introduced by residue compression; ATAM catches political and cost-balance issues; FMEA catches technical failures introduced by added components; the empirical Ri test catches whether the work as a whole moved the architecture in the right direction. The book's defence of the multi-step process is that no single step is the bottleneck — the discipline is in the layering.

The process produces an architecture that is multidimensional — each residue is a separate dimension of the system — rather than the two-dimensional component diagrams traditional architecture produces (O'Reilly 2020, [§4.1](../../references/papers/Residuality-Oreilly-2020.md)). The metaphor O'Reilly offers is "a stack of shadows we cannot see without turning various lights on and off" (O'Reilly 2020, [§2](../../references/papers/Residuality-Oreilly-2020.md), p. 877).

### A demonstration of the looping phenomenon: ICE-ing and AFIR

The book's only worked example — a globally-deployed EV-charger management system — illustrates the *looping* effect that drives the theory's empirical leverage. An early stressor in the analysis was failure of the customer key-fob (the device authenticating each charge). To survive that stressor, the architect added an alternative authentication path: read the licence plate of the parked vehicle, then bill or convert-to-subscription afterwards. This decoupled customer membership from charging.

A second stressor introduced security cameras (against accidental damage to the chargers). A third introduced sliding-scale time-based billing (against drivers who park indefinitely). Years later, two events the original architect could not have predicted hit the deployed system. *ICE-ing* — drivers of internal-combustion vehicles parking in front of EV chargers to spite EV owners — was already covered: the camera caught them, the licence plate identified them, and the sliding-scale billing made the behaviour expensive. *EU AFIR 2023*, the regulation requiring EV chargers to accept ad-hoc credit-card payments, was also already covered: the membership/charging decoupling left the architecture with a clean extensibility point for a new payment method (O'Reilly 2024, *A Worked Example / Stressor Analysis*).

The point is the *looping*: a stressor surfaces a residue; the residue, once present, survives stressors that nobody on the original team imagined. Mathematically, the leverage comes from the asymmetry between the number of attractors (small) and the number of stressors that route the system into each attractor (large). One identified stressor protects against many unidentified ones that share its attractor. This is the structural reason residuality theory's stressor analysis can be deliberately playful and still produce a robust architecture.

### The residue concept and the methodological refusal to taxonomize

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

The 2024 book makes a stronger empirical claim than the papers do. In its *Empirical Test* and *Conclusion* chapters O'Reilly states that residuality experiments have "revealed a statistically significant effect" across projects — an advance over the per-project Ri framing of 2022 (O'Reilly 2024, *Empirical Test*; *Conclusion*). The cross-project claim is a substantively different assertion: per-project Ri shows that residual analysis worked *here*; cross-project significance would show that the method is reliably more effective than the alternatives in general. As of April 2026 the underlying study has not been published; no separate methods/results paper is publicly available, and the announced PhD thesis that would presumably contain the analysis (see §12) is not yet indexed in any institutional repository the survey author could find. The empirical promise of residuality theory is therefore real but, on its strongest version, presently unverified outside O'Reilly's own circle.

---

## 9. Processuality, criticality, difference: the philosophical triad

The 2023 paper, *Residuality and Representation*, reorganizes the philosophical line of the theory around three concepts: **processuality, criticality, and difference**. They are the answer to a question the earlier papers gestured at but did not name: why do architects keep reverting to substance-focused static representations even after encountering residuality? The answer is that the entire intellectual culture of software architecture is substance-philosophical, and residuality theory is process-philosophical, and the two require different cognitive moves (O'Reilly 2023, [§3; §4](../../references/papers/Residuality-Oreilly-2023.md)).

**Processuality**. The world is constant becoming, not a collection of static entities. Residuality describes things as processes; substance is residue — the accidental leftover of processes, not the foundation. This is process philosophy in the Bergson/Whitehead/Deleuze line, but residuality stays pragmatic about it: the goal is not to defend a metaphysics but to describe systems in a way that lets architects work with flux rather than against it (O'Reilly 2023, [§4](../../references/papers/Residuality-Oreilly-2023.md)).

**Criticality**. The proper goal of architecture is not *correctness* — a hangover from software engineering's mathematical roots — but *criticality*: an internal structure capable of reorganizing to survive transitions between attractors. Correctness asks "does the system meet its specification?" Criticality asks "does the system retain function as the environment moves through its attractor space?" These are different evaluation targets, and the choice between them is consequential. Correctness rewards systems that succeed in stable environments and fail in unstable ones. Criticality rewards systems that survive the attractor transitions that destroy stable-environment optima (O'Reilly 2023, [§4.1](../../references/papers/Residuality-Oreilly-2023.md)).

**Difference**. Residues represent only what *differs* between attractor states, not the totality of the system. The architectural model is a stack of differences — what changes when this stressor hits, what changes when that one hits — rather than a unified picture of the whole. This is explicitly Deleuzian and the 2023 paper develops the connection at length. O'Reilly: "Inspired by Bergsonian processuality and the concept of difference, it is Deleuze who brings a metaphysical investigation that foreshadows residuality in the closest way. Deleuze rejects the Platonic, substance-fueled tendency to reduce things to their substance-based identity, instead emphasizing the importance of change, the unending process of differential change through repetition and the defining of identity through these differences" ([§5](../../references/papers/Residuality-Oreilly-2023.md)). The Deleuzian walk is the metaphor — the first walk is one experience; subsequent walks reveal seasonal change, altered paths, new buildings; the meaning of the walk is the sum of differences across repetitions, not the first traversal. Stressor analysis is the architectural form of this walk: "the generation of each model is a Deleuzian walk." Residuality, O'Reilly writes, "integrates these Deleuzian instincts into an empirical framework." Three secondary references underwrite the line: Cisney's *Deleuze and Derrida*, Deleuze's *Difference and Repetition*, and Williams's secondary commentary on it.

The 2023 paper makes Deleuze a primary anchor in his own right — alongside Cilliers (the phenomenal gap), Kant (noumena/phenomena), Bateson (form, substance, and difference), and Whitehead (the fallacy of misplaced concreteness). This is a different anchoring than the 2021 *Philosophy* paper, where Serres and Latour are the primary post-structural anchors and Deleuze appears once. The corpus has multiple primary philosophical anchors across the arc, not a single one; readers approaching the theory through 2021 will see one philosophical line, readers approaching through 2023 will see another, and both are correct readings of the paper they are reading.

The 2023 paper introduces a fourth important concept: the **phenomenal gap**, drawn from Cilliers's reading of Kant. Noumena are things as they exist independent of our senses; phenomena are our impressions of them. In simple, ordered systems the gap is small and the impression suffices. In complex systems — and especially in enterprise environments — the gap is enormous and irreducible. The phenomenal gap is the technical name for what residuality theory has been describing all along under the labels of complexity, hyperliminality, and the limits of representation (O'Reilly 2023, [§3](../../references/papers/Residuality-Oreilly-2023.md)).

The triad gives residuality theory a coherent philosophical position to defend, rather than just a critique to deploy. Processuality is the metaphysical commitment; criticality is the architectural goal; difference is the representational unit. Each addresses a specific way the substance-philosophical default mis-fits the architect's actual problem.

### Linear and lateral thinking: the cognitive-style framing

The 2024 book reorganises one part of the philosophical line as a claim about *cognitive style* rather than methodology. The book distinguishes **linear thinking** (mathematical, exact, step-by-step, demanding correctness at every move, fixated on definitions) from **lateral thinking** (comfortable with provisional structure, tolerant of being wrong for long stretches, willing to use imagination to fill gaps the stakeholders cannot describe). The book's claim — pitched in a deliberately memorable form — is that "for the mythical 10X developer, 9X is lateral thinking" (O'Reilly 2024, *How we learn a domain / Linear and Lateral Thinking*).

This framing repositions residuality theory not just as a set of techniques but as the institutionalisation of a cognitive style that senior architects already use intuitively. The matrices, the stressor lists, the safety nets — all are scaffolding to make lateral thinking executable by teams who would otherwise default to linear thinking. The book's claim is that linear thinking, applied alone, produces the under-engineered architecture the field's failure rate reflects. Linear thinking is necessary inside the ergodic core (programming, formal correctness); lateral thinking is necessary in the non-ergodic envelope (architecture across attractors). The two are paired, and the book treats the architect's job as the deliberate switching between them.

The cognitive-style framing is not in the papers. It is the book's most distinctive contribution to how the methodology should be taught.

---

## 10. Limits, open questions, and external critique

Residuality theory is a working program rather than a finished theory, and several of its commitments are contested. Where the 2024 book has explicitly *defended* a position the corpus had left implicit, the defence is noted alongside the criticism.

**The unfalsifiability charge.** Critical reviewers of the 2024 *Residues* book argue that the theory is "very abstract and not rigorous" (Goodreads, Nicola, 2025-01-03) and "feels half baked at best" (Goodreads, Travis, 2025-02-13). Earlier objections — that residuality dismisses effective principles like SOLID, DRY, and modularity patterns — also circulate. The unfalsifiability claim is partly answered by Ri (per-project falsifiability is built in); residuality theory's broader response is that idiographic testability is the only kind of testability complex systems admit. The book additionally defends the position that residuality replaces — does not supplement — requirements engineering and risk management for the architectural envelope, while leaving them in place inside the ergodic core. Whether the defence holds depends on the reader's prior commitments. As of April 2026 the book has not been engaged by a serious formal-methods critic in a major venue (no review located in InfoQ, IEEE Software, CACM, or comparable outlets), and that engagement is overdue.

**The empirical case is publicly thin.** The Ri values O'Reilly reports in the 2022 paper are anecdotal, from lab-scale experiments not run under stringent conditions. The 2024 book's stronger claim — a "statistically significant effect" across projects (O'Reilly 2024, *Empirical Test*; *Conclusion*) — would be qualitatively new evidence if it were openly available, but as of search date the underlying methods/results paper is not publicly indexed. The PhD thesis announced in the book's Introduction would presumably contain the analysis, but no institutional repository entry, defence date, or open-access PDF was located in April 2026 (see §12). Larger-scale empirical studies by teams independent of O'Reilly's circle do not exist in publicly indexed form. The theory's claim that systems designed using residuality outperform naïve baselines is plausible and corroborated by O'Reilly's own report; broad demonstration awaits the publication of the supporting material.

**Definitional looseness.** The deliberate under-definition of "residue" is methodologically motivated (a tighter definition would reinstate structuralism), but it makes the theory difficult to teach and difficult to apply consistently. Practitioners report uncertainty about when they have correctly identified a residue — a complaint that O'Reilly acknowledges but does not fully resolve (O'Reilly 2021b, [§5](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md)). Eric Normand's 2024 Substack essay, while sympathetic to the methodology, separately objects to the *name* of the theory as a barrier to adoption.

**Residuality is not resilience engineering, and the distinction matters.** The 2024 book devotes a sustained subsection to drawing a hard line between residuality and the resilience-engineering tradition (O'Reilly 2024, *Walking with Stressors / Resilience*). The argument: resilience treats software as part of a complex adaptive system, and works by *staying within* or *returning to* a fixed range of attractors using human adaptive capacity. Residuality treats the software as complicated *inside* a complex envelope and works by *moving between* attractors at the architecture level. The two have different goals — preserving identity versus surviving identity-change — and produce different design choices (post-incident retrospection and chaos engineering for resilience; residual analysis and contagion analysis for residuality). Misreading residuality as resilience-by-another-name leads to under-engineered software because the resilience tradition assumes human adaptive capacity covers slack that residuality says must be present in the architecture itself.

**Non-functional requirements: the strong claim.** The 2024 book makes a noticeably stronger claim about NFRs than the papers do: NFRs "simply don't exist in a way that is discoverable by any other means than random simulation" (O'Reilly 2024, *Residuality / Hyperliminal Coupling*). This positions residual analysis as the *only* viable NFR-elicitation method, not one option among several. Practitioners with backgrounds in NFR-elicitation methodologies (ATAM stakeholder workshops, ISO/IEC 25010 quality-attribute workshops, scenario-based architecture analysis) will push back on this. The defence rests on hyperliminal coupling: NFRs are by definition the cross-cutting concerns that arise from environment-mediated coupling, and that coupling is invisible to any method that does not stress the system across stressors.

**The case-study refusal is methodological, not evasive.** The 2024 book deliberately omits case studies and explains the omission: "Just because something works in a particular context does not guarantee that it will work everywhere... the inclusion of case studies would be an attempt to bolster the argument and this would be marketing rather than science" (O'Reilly 2024, *A Worked Example*). The book offers one worked example (the EV-charger system, summarised in §6 above) without claiming generality. Critics who want concrete demonstrations of efficacy will find the position unsatisfying; the book's defence is that the empirical Ri test, run by the practitioner on their own project, is the proper substitute for case studies.

**The under-engineering diagnosis as practitioner critique.** The 2024 book diagnoses a specific failure mode of conventional practice: under-engineering of the architecture *combined with* over-engineering of the technology, both driven by structural-determinist assumptions inherited from traditional engineering ("structuralism is a comfort blanket for STEM graduates working with human systems far outside of their comfort zone," O'Reilly 2024, *Residuality / Random simulation*). The framing is sharper than the papers' and is one of the reasons reviewers describe the book's tone as polemical (see §12). Whether the diagnosis is accurate is a question for empirical work the book promises but has not yet delivered.

**Cybernetics critique applies selectively.** The 2021 *Philosophy* paper's critique of cybernetics targets Beer-style VSM applications and the machine-metaphor reading of cybernetic principles. The von Foerster line of second-order cybernetics — observer-included, recursive, anti-control — is not the target, but readers unfamiliar with the distinction can assume residuality theory rejects all cybernetics, which it does not (O'Reilly 2021a, [§Cybernetics](../../references/papers/Residuality-Oreilly-2021.md)). The 2024 book softens this critique: it attacks "structuralism" and "the engineering paradigm" generically without naming Beer or VSM specifically, so readers approaching residuality through the book may miss the precise target the papers identified.

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

The 2024 *Residues* book consolidates the theory for practitioners — a fourth phase, treated in §12 below.

---

## 12. The 2024 *Residues* book

The 2024 book *Residues: Time, Change, and Uncertainty in Software Architecture* is the practitioner-pitched compression of the corpus, ~85 pages, self-published on Leanpub. Its job is "to present the ideas in less formal, academic language than the series of papers" (O'Reilly 2024, *Introduction*). The book consolidates the theory's vocabulary and adds five things the papers do not have: the ergodicity definition of hyperliminality (§3 above), the stressors-versus-X taxonomy (§6), the robust-versus-residual distinction (§6), the linear-versus-lateral cognitive-style framing (§9), and a sustained intellectual hygiene against being read as resilience engineering (§10). It also adds the worked EV-charger example (§6), the cross-project significance claim (§8), and a single concentrated heuristics list (below). It omits, relative to the papers, the political/autonomy framing of *Machine in the Ghost*, the specific Beer/VSM target of the *Philosophy* paper, and the dense post-structural anchoring of *Residuality and Representation*.

### The seven heuristics

The book closes with a compressed heuristics list that captures the methodology in seven lines (O'Reilly 2024, *Heuristics*):

> - You cannot map hyperliminal systems
> - You cannot control hyperliminal systems
> - Random simulation is better than requirements, risks, and predictions
> - Flows are better than process or use case mapping
> - Residues replace components or patterns as the unit of architecture
> - Matrices are better than component decomposition by pattern or framework
> - No probability or cost until the architecture is explored for weaknesses

This is the book's single most quotable artefact and the corpus's single best compressed statement of the methodology.

### Tone and register

The book is the most polemical text in the corpus. It frames the field's dominant approaches in deliberately memorable phrases — software engineering's borrowing from traditional engineering "has been tantamount to nailing horseshoes to car tires" (*Architecture / Ergodicity and Hyperliminality*); structuralism is "a comfort blanket for STEM graduates working with human systems far outside of their comfort zone" (*Residuality / Random simulation*). The papers maintain academic restraint; the book does not. Reviewers note the tone explicitly, with one Goodreads reviewer (Nicola, 2025-01-03) objecting that the book "references software developers as some sort of immature people." The polemical register is a deliberate rhetorical choice — the book opens by framing itself as a Kuhnian paradigm shift requiring direct confrontation with inherited assumptions — and is one of the things future readers should be prepared for.

The book also commits to one-researcher provenance: it is dedicated "For Tanya, my stressor"; reviewers are named in the acknowledgements (Riccardo Bennett-Lovsey, Blair Moir, Einar Høst, Jeroen Haegebaert); the editor who pushed the book into existence is named (Mathias Verraes); the cover art is by O'Reilly's son Alexander, aged 11. The book reads as personal, not institutional.

### What the book omits

Several connections the papers carry are absent from the book. The *Machine in the Ghost* political framing — residual causality as a structural threat to societal autonomy — does not appear; the book stays on architectural ground. The 2021 *Philosophy* paper's specific Beer/VSM critique is softened to a generic critique of "structuralism" and "the engineering paradigm." The 2023 paper's dense post-structural anchoring (Cilliers, Bateson, Wittgenstein, Spinoza-via-Deleuze) is absent; Deleuze is invoked only via the walk metaphor in *Difference and Repetition*. Naur, Pask, and von Foerster — who would naturally connect residuality to the systems-theoretic and conversation-theory traditions — are absent. The book is consistent with the papers everywhere it speaks; its omissions are register-driven, not retractions.

### Author and forthcoming work

O'Reilly identifies in the book's *Introduction* and in adjacent talks as a software architect, founder of the consultancy Black Tulip Technology, and a PhD student in complexity science currently based in Stockholm, Sweden. The book's *Introduction* announces "this work will culminate shortly in the form of a PhD thesis," and the *Conclusion* announces a forthcoming "longer version" of the book. As of April 2026 neither has appeared in publicly indexed form: no thesis is registered in DiVA (the Swedish national academic repository), KTH's repository, Stockholm University's repository, or the European thesis aggregators searched; no expanded edition or traditional-publisher imprint of *Residues* has appeared. The corpus is therefore *open* — the most rigorous and most empirically substantiated piece of the work is forthcoming, not in hand.

### Reception

Reception is real but sparse. The 2024 book is reviewed publicly on Goodreads, which is the only place a cluster of named-reviewer responses can be found. Sympathetic reviews praise the book as "excellent" and "succinctly covering the theory" (Christian Marques, 2024-12-18) and as bridging "philosophy, complexity science, and software architecture" (Alejandro, 2024-12-20). Critical reviews call the ideas "very abstract and not rigorous" (Nicola, 2025-01-03) and "half baked at best" (Travis, 2025-02-13), and object to tone toward developers. Eric Normand's May 2024 Substack essay is sympathetic to the methodology but criticises the *name* — "It's a terrible name" — as a barrier to adoption. No major-venue critical engagement was located in InfoQ, IEEE Software, *Communications of the ACM*, or comparable outlets at search date; the absence may be a search-strategy artefact, but it is honest to report it as the current state of the public discussion.

### Practitioner uptake

Beyond the published reviews, the book has visible practitioner uptake. O'Reilly continues to teach the methodology in venues outside his own consultancy: the VirtualDDD community has run sessions titled "An Introduction to Residuality Theory" and "Practical Residuality" (the latter involving hands-on work with incidence matrices); Avanscoperta has hosted an Advanced Software Architecture workshop, since transcribed; *software-architektur.tv* has interviewed him at length (episode 279, 2023). Independent practitioner explainers exist (the doubleSlash blog's 2026 piece "Residuality Theory: Future-Proof Software Architecture Inspired by Insights from Biology" is one example), and discussion threads in *r/ExperiencedDevs* and similar communities show working architects engaging with the methodology after reading the book. Residuality theory has therefore acquired some traction outside O'Reilly's immediate circle, even if no major-venue critical essay has yet appeared.

---

## 13. Reading paths

For the practitioner who wants to enter the corpus efficiently:

- **Quickest pedagogical on-ramp**: Eric Normand's *Residuality Theory* essay on Substack (May 2024). About 30 minutes, with a worked example (a country-based coupon banner service). It is the clearest single piece available for someone who has not read O'Reilly directly.
- **Practitioner-pitched single-volume entry**: O'Reilly 2024, *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub, ~85pp.). Two to three hours. The book is paid; it is the most accessible single artefact in the corpus and contains the worked EV-charger example, the seven heuristics, the stressors-versus-X taxonomy, the linear/lateral framing, and the explicit residuality-vs-resilience hygiene that the papers leave implicit.
- **Operational mechanics**: O'Reilly 2020, *An Introduction to Residuality Theory*. Roughly an hour. The matrix techniques, training/testing protocol, and the consolidation step that the practitioner literature elaborates.
- **The complexity-science backing**: O'Reilly 2022, *Random Simulation and Attractor Networks*. About an hour. The two-step algorithm, NKP analysis, and the residual index Ri.
- **The philosophy**: O'Reilly 2021a (Procedia *Philosophy*) for the concise component-metaphor critique; O'Reilly 2023 (*Residuality and Representation*) for the processuality/criticality/difference triad and the phenomenal gap. Read in publication order, not reverse.
- **The political stake**: O'Reilly 2021b (*Machine in the Ghost*), *Philosophies* 6(4):81. About 90 minutes; the only paper with the autonomy framing and the only one with O'Reilly's first-person genealogy.
- **Talks**: NDC London 2024 *Introduction to Residuality Theory* (~50 minutes) and NDC Oslo 2024 *The Philosophy of Architecture* (~60 minutes) for O'Reilly in his own voice. The architectural-walks vocabulary is introduced at 31:16 of the Oslo talk. VirtualDDD's "Practical Residuality" session is the best practitioner-led hands-on entry to the matrix work.

The companion file [residuality-bibliography.md](residuality-bibliography.md) gives the union of references across the corpus, organized by role. It should be the first place to look for any cited work this survey mentions.

---

## Provenance note

This survey was written from the six O'Reilly papers archived in [`references/papers/`](../../references/papers/) (2019, 2020, 2021 *Philosophy*, 2021 *Machine in the Ghost*, 2022, 2023) and the 2024 Leanpub book *Residues: Time, Change, and Uncertainty in Software Architecture*. It does not consult the 2018 Cutter *Executive Update*, the 2020 *There Is No Spoon* Cutter compilation, or the 2021 *Hyperliminal Coupling* Cutter piece (all paywalled); those are referenced where the corpus mentions them but were not read directly.

The 2024 book is referenced by chapter and subsection rather than by page number (Leanpub pagination is not a stable reference) and quoted only in short fair-use snippets, since the book is a commercial artefact. Reception material in §10 and §12 is sourced from the consulted book combined with public reviews gathered in April 2026 (Goodreads named-reviewer cluster, Eric Normand's Substack essay, and practitioner-traction signals from VirtualDDD, Avanscoperta, and *software-architektur.tv*); it is not from the chronology's earlier secondhand "reception is mixed" annotation.

Several pieces of forthcoming primary material are *announced but unverified* as of April 2026: O'Reilly's PhD thesis (announced in the 2024 book Introduction; not located in any institutional repository at search date), a "longer version" of the book (announced in the book Conclusion; not yet appeared), and the cross-project significance test that the book asserts has been performed (no separate methods/results paper publicly available). The survey reflects this honestly: the empirical claim that most distinguishes residuality from competing methodologies is gated on material that has not yet been published. The corpus is open, not closed.

O'Reilly is one researcher: founder of Black Tulip Technology, currently identifying as a PhD student in complexity science based in Stockholm, Sweden. The corpus is one researcher's program developed over roughly a decade, not the output of an institutional research consortium. This is worth being transparent about.

The voice is third-person survey, not O'Reilly's own. The book's polemical voice ("nailing horseshoes to car tires," "comfort blanket for STEM graduates working with human systems") is *described* in §10 and §12 as a register fact about the book; it is not adopted in the survey's own voice. Where the survey states an implication that O'Reilly does not himself make explicit, the implication is conservative — drawn directly from juxtaposing claims he does make — and presented as such.
