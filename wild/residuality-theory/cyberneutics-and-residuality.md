---
title: "Cyberneutics and Residuality Theory: Inheritance, Contribution, and Connection"
type: working-note
audience: "Repository contributors and successor agents thinking about essay-13 development"
companion_survey: state-of-residuality-2026.md
companion_bibliography: residuality-bibliography.md
status: "Working note. Not a polished publication; a stocktake of the relationship between the two programs as the corpus stands in April 2026."
---

# Cyberneutics and Residuality Theory: Inheritance, Contribution, and Connection

This note inventories the relationship between cyberneutics and Barry M. O'Reilly's residuality theory as both stand in April 2026. It draws on every residuality-related file in this repository — the survey here, the diary entries in [`wild/diary/`](../diary/), the relevant essays (especially [04](../../essays/04-cybernetics-and-observation.md), [06](../../essays/06-deleuze-difference-repetition.md), [08](../../essays/08-from-methodology-to-formalism.md), [10](../../essays/10-decisions-under-uncertainty.md), [11](../../essays/11-conversation-theory.md)), the [Pask conversation-theory wild file](../cybernetics/conversation-theory.md), and the six O'Reilly papers archived in [`references/papers/`](../../references/papers/).

The note answers three questions:

1. **What in cyberneutics is directly influenced by residuality theory?**
2. **What could cyberneutics contribute back to residuality theory?**
3. **What other structural connections exist that are neither inheritance nor contribution?**

A closing section proposes how the survey paper [`state-of-residuality-2026.md`](state-of-residuality-2026.md) could be modified or extended in light of these observations.

---

## 1. What cyberneutics inherits from residuality theory

The borrowed vocabulary is concentrated in essays 06, 10, and 11, with reinforcement in essay 08's methodology-to-formalism bridge.

### 1.1 The architectural-walks vocabulary

Essays 06 and 10 take O'Reilly's *architectural walk* — knowledge built through repeated traversal — and use it as the operational name for what the Probe operation does. Essay 06 introduces the connection at [§Architectural Walks](../../essays/06-deleuze-difference-repetition.md): "O'Reilly's three philosophical commitments — process over substance, criticality over correctness, difference over essence — are Deleuze translated into software practice." Essay 10 then carries the vocabulary into its decision-theory presentation: "The composed fan → funnel pipeline is an architectural walk through a decision space" ([essay 10 §Architectural walks](../../essays/10-decisions-under-uncertainty.md)).

This is the most visible inheritance. The cyberneutics Probe operation is now described in terms residuality supplied. Without O'Reilly's vocabulary, the cyberneutics literature would have to talk about "iterated pipeline runs" — accurate but ungrounded. Architectural walks gives the iteration a philosophical name and a practitioner audience.

### 1.2 The residue/eigenform distinction

This is the load-bearing inheritance. Essay 10 ([§Residues and eigenforms](../../essays/10-decisions-under-uncertainty.md)) names a distinction that the philosophical sources alone (Deleuze, von Foerster) had only gestured at:

- **Residues** are what any single walk discovers. Local, trajectory-dependent.
- **Eigenforms** are what every walk discovers. Global, fixed under repetition.

The distinction was already in the cyberneutics palgebra in less crisp form (eigenforms as recursive fixed points, from von Foerster). Residuality supplies the *complement*. A single deliberation produces a residue; only repeated deliberations hunt eigenforms. This sharpens what the remediation loop is doing (hunting *local* eigenforms within a single run) versus what the Probe operation is doing (hunting *global* eigenforms across runs). The vocabulary lives in essays 04, 06, 08, 10, and the palgebra's `categorical-structures.md`.

The diary entry [2026-02-26 cyberneutics field notes](../diary/2026-02-26-cyberneutics-field-notes.md) recorded the early form of this question — "residuality theory re universal properties over shocks; human observer's role in categorical framework" — before the eigenform framing crystallized. The current presentation in essay 10 is the resolved version of that working note.

### 1.3 Criticality over correctness as the evaluation target

Essay 10's final section ("What this means in practice") is structured around a minimax-rather-than-expected-value commitment that traces directly to O'Reilly's "criticality over correctness" move: "Pick the action whose worst case across scenarios is survivable." This is residuality's core architectural goal applied to decision-theoretic practice. The cyberneutics methodology refuses "best answer" as the deliberation's evaluation target and substitutes inspectable reasoning chains; the structure of that refusal is the criticality move at the deliberation layer, not at the systems-engineering layer.

The handoff from the 2026-04-20 [residuality philosophy paper reading diary](../diary/2026-04-20-residuality-philosophy-paper-reading.md) made this connection explicit: residuality theory's "structure itself is the risk" diagnosis and cyberneutics' "the deliberation transcript *is* the product, not a byproduct" position are the same move at different scales.

### 1.4 Stressor vocabulary at micro-scale (teachback as micro-residuality)

Essay 11's [§Teachback as Micro-Residuality](../../essays/11-conversation-theory.md) takes residuality's macro-scale vocabulary (stressors, residues, architectures) and applies it to Pask's teachback at conversation scale. Each conversational move (challenge, rephrasing, application, role-reversal) is a shock; what survives the shocks is the residual structure of understanding. The wild file [`wild/cybernetics/conversation-theory.md`](../cybernetics/conversation-theory.md) develops this in more detail: "knowledge is not initial design/description; it is the residue of failed attempts to break it."

This is borrowing in both directions of metaphor: O'Reilly's residue concept is reused at the micro scale, and Pask's teachback concept is re-described as macro-residuality. The unification — "a Paskian understanding is a residual architecture of concepts; an O'Reilly residue is a Paskian understanding scaled to systems engineering" — is a cyberneutics formulation that depends on residuality's vocabulary to land.

### 1.5 Residual causality as a frame for dual-use harm

The 2026-04-20 diary flags this potential extension: residual causality — "decisions made long ago in different circumstances for different reasons constrain human action in an unknown future" — is structurally the same problem as the dual-use AI literacy concern that essays 09 and adjacent material wrestle with. Teaching children to emotionally disengage from convincing AI agents is a structural decision that will constrain attractors no one is currently planning for. This is residuality theory inherited as *diagnostic vocabulary* rather than as architectural method, applied to a problem domain (AI-mediated cognition) outside O'Reilly's home territory. The framing has not yet been written into a finished essay; the diary records it as an open thread.

---

## 2. What cyberneutics could contribute to residuality theory

The contributions go both ways. Cyberneutics has crystallized several things that residuality theory leaves implicit, and several connections that O'Reilly does not himself make.

### 2.1 The Probe operation as a quantitative apparatus for architectural walks

O'Reilly describes architectural walks but does not specify *how many walks*, *how to compare them*, or *how to decide when to stop*. Cyberneutics' Probe operation gives this an apparatus: a variance report, a decision-landscape map (basins, ridges, robust actions), and a diagnostic taxonomy for when repeated runs disagree (situation framing ambiguous; assumptions load-bearing; pipeline noisy — see [essay 10 §Diagnosing instability](../../essays/10-decisions-under-uncertainty.md)). This generalizes the architectural-walks idea into an instrument that can be operated by a team without philosophical commitment.

If residuality theory wants a falsifiability move at the *walk* level (analogous to Ri at the architecture level), the variance-report apparatus is a candidate. "How stable is the residual architecture under repeated walks of this scenario set?" is a measurable per-project question, and stability across walks is itself a form of criticality the residual index does not measure.

### 2.2 The local/global eigenform distinction made operational

O'Reilly uses "residue" but does not sharpen it against eigenform. The cyberneutics distinction — single-walk findings (residues) versus repeated-walk findings (eigenforms) — resolves an under-defined corner of residuality. It also explains *why* the bagging-and-boosting move in residual analysis works: bagging hunts global eigenforms across stressor partitions; what survives multiple partitions is structurally robust in a way that single-partition residues are not.

This vocabulary is sufficient to add a measurable dimension to the residual index. Ri > 0 says the residual architecture beat the naïve baseline on the testing set. *Eigenform Ri* — the fraction of residues that recur across bagged partitions — would say something stronger: the residual architecture's *invariants* are stable across stressor sampling, not just its averaged performance.

> **Status: Untested.** Eigenform Ri is proposed; it has not been computed for any deliberation in this repository. The Black Swan deliberations have multiple runs and dual-scoring; the variance is computable but has not been computed. Treat as proposal, not contribution, until the measurement is performed.

### 2.3 Inspectable reasoning records as criticality at the deliberation layer

Residuality theory specifies criticality for systems but says little about how an architect *knows* they have it. The committee deliberation transcript is a candidate answer at the deliberation layer: the trace of what survived adversarial cross-examination is exactly the residue analogue, and the inspectability of that trace is what makes the criticality verifiable rather than asserted. This generalizes residuality from architecture to deliberation, and gives the criticality goal an evidentiary form.

The 2026-04-25 diary entry records the convergence: the committee's value proposition is "the residue of theory-formation made deliberate." That framing is residuality applied to sense-making practice, and it is a generalization that O'Reilly has not made in print.

### 2.4 The two-step algorithm extended to sense-making generally

O'Reilly's 2022 paper claims that any software design methodology is implicitly a two-step algorithm: random simulation of the environment, then network analysis of the architecture. Residuality just makes both steps explicit. Cyberneutics' fan→funnel pipeline is the *generalization* of that claim to sense-making methodologies generally: the fan is the random simulation (divergent scenario generation); the funnel is the network analysis (committee deliberation across scenarios). The palgebra formalization makes this a checkable claim rather than a metaphor — the resource equations and string diagrams give the two-step algorithm a categorical type signature.

This is contribution back: residuality theory's claim was about software design specifically. Cyberneutics demonstrates the structure works for decision-making under genuine uncertainty across domains. Anyone working through O'Reilly's papers and looking for "where else does this two-step algorithm apply?" can be pointed at the cyberneutics palgebra and at the situation-directory worked examples in this repository.

### 2.5 A second-order cybernetics answer to O'Reilly's cybernetics critique

The 2021 *Philosophy* paper attacks Beer's VSM specifically as "second-order abstraction... that gives a quasi-scientific facade to decision making in conditions of high uncertainty." Cyberneutics inherits from a different cybernetics line — von Foerster, Pask, observer-included recursion — that already broke with the machine metaphor from the inside. The cyberneutics methodology answers the specific failure mode O'Reilly identifies: VSM hands architects a template (five systems, recursion) to apply before examining whether the terrain justifies it; the committee pipeline does the opposite — it refuses template-application and insists on stress-testing structure across scenarios.

Naming this answer explicitly is a contribution. "Here is what residuality-aligned cybernetics looks like, and here is why it does not inherit the failure modes of the cybernetics tradition O'Reilly is critiquing" is a useful clarification for readers of both bodies of work, and the 2026-04-20 diary already drafted the response that essay-13 will need to make load-bearing.

### 2.6 The Naur bridge: theory-formation as residue, the artifact as precipitate

The 2026-04-25 diary records a unification that O'Reilly does not make: residuality and Peter Naur's *Programming as Theory Building* are the same diagnosis from different angles. Both point at *the artifact is not the unit*. Components-as-Lego presumes the joints are clean and the interfaces total; residuality says the durable thing is what survives the shock; Naur says the durable thing is the team's living theory. The unification is sharper than either source alone: the artifact (code, architecture diagram, deliberation transcript) is precipitate; the durable unit is the theory; residuality is what survives in the code, theory-building is what survives in the team's heads.

This is a contribution residuality theory has not absorbed. Adding Naur as an adjacent foundation would broaden the theory's reach into knowledge work generally, and would give residuality a partner that addresses the "where does the residue live when there is no code yet?" question that the design-time orientation of residual analysis leaves unanswered.

### 2.7 The Pask bridge: residuality at conversation scale

Essay 11's teachback-as-micro-residuality and the wild [conversation-theory file](../cybernetics/conversation-theory.md) develop a bridge O'Reilly has not made: Pask's conversation theory is residuality at the scale of two interlocutors building shared understanding. The connection works in both directions. From cyberneutics' side, it grounds the committee deliberation in a tradition (Pask) older than residuality. From residuality's side, it suggests that residual-analysis vocabulary applies wherever knowledge is being shock-tested, including in conversation, education, and curriculum design — domains where "stressor" and "residue" are not native vocabulary but where the structural pattern holds.

A residuality-side reader looking for "what would residuality-aligned curriculum design look like?" can be pointed at Pask's teachback. A Pask-side reader looking for "what does residuality contribute to conversation theory?" can be pointed at residual-analysis-of-curriculum as a design-time discipline parallel to teachback's runtime discipline.

### 2.8 Calibration register as long-run criticality measurement

O'Reilly's residual index Ri is a per-project test. Cyberneutics' calibration register tracks deliberation outcomes across many runs over time. This extends the empirical move into a long-run feedback loop: not "did this architecture survive the testing set?" but "do the *kinds of failures* the residual approach catches reliably stay caught across projects, and do new failure modes emerge that the residual approach misses?" The calibration register is, structurally, a long-run version of Ri, with the same falsifiability commitment but operating on a portfolio of decisions rather than a single architecture.

This too is contribution back. Ri demonstrates per-project falsifiability; the calibration register demonstrates that residuality-aligned methods can carry their falsifiability commitment into longitudinal practice. The two are complementary: one says "this project worked," the other says "the methodology continues to work."

> **Status: Architectural commitment, not implementation.** The calibration register is a planned mechanism dependent on agent-substrate support for inter-agent communication (Claude Code, Codex, etc., as the platforms mature). Until that substrate exists, "calibration register as long-run Ri" is a design target, not a deployed instrument.

### 2.9 The fan operation as a stressor-list generator for residual analysis

This is the most directly actionable contribution back. Residual analysis (the 2020 and 2022 papers) takes a stressor list as input. Building the list well is harder than the papers acknowledge: O'Reilly characterizes the practice as "playfulness," notes the 2021 *Philosophy* paper's emphasis on "naive ideas about cause/effect as information," and observes that practitioners often default to probability-weighted enumeration that the methodology explicitly rejects. The standard failure mode is the curse of dimensionality — distributions return to areas of high probability, and the architect's stressor list becomes a refined version of the risk register the methodology was built to escape.

The cyberneutics fan operation is engineered for exactly this problem in the decision domain. The fan produces divergent narrative material from a roster of characters whose propensities are deliberately incommensurable, with explicit instructions to include impossible, irrelevant, and adversarial cases. Both moves answer specific failure modes O'Reilly names. Roster-driven divergence defeats the single-perspective bias that produces probability-weighted lists; deliberate inclusion of impossible stressors operationalizes the playfulness the papers prescribe.

The offer to a residuality practitioner is concrete: *use a structured LLM fan operation to generate the stressor list, with characters chosen to cover the dimensions the system will be exposed to (regulatory, infrastructural, social, adversarial, market, internal-political, etc.); accept the divergent output as input to incidence-matrix analysis; bag-and-boost across multiple fan runs the way bagging-and-boosting already operates across stressor partitions in residual analysis.* This adds a documented, reproducible upstream stage to residual analysis — and the upstream stage is itself empirically falsifiable in the same way Ri is, because two stressor lists produced by different fan-operation configurations can be compared by Ri on the same naïve architecture.

This is a tool the 2022 paper's two-step algorithm calls for but does not provide. Cyberneutics has it built and tested. A residuality practitioner can adopt the fan as their stressor generator without committing to anything else in the cyberneutics methodology.

Treated as a contribution, this means: the fan is not just *a generalization of* the random-simulation step (the structural claim of §2.4 above); it is *a working implementation of the random-simulation step that residuality theory currently leaves to the architect's intuition*. See the standalone working note [`fan-as-stressor-generator.md`](fan-as-stressor-generator.md) for the practitioner-facing offer.

---

## 3. Other connections (parallels, neither inheritance nor contribution)

These are structural alignments that exist in the corpus but are not framed as borrowings.

- **Hyperliminality ↔ organ/bloodstream.** Both are the same structural diagnosis: an ordered, controlled regime nested inside a disordered, ambient one, with the cross-regime interface as the locus of risk. The vocabularies developed independently and could be unified, but the parallel is more useful kept visible than merged. This is flagged in the [`wild/residuality-theory/README.md`](README.md) Remaining Directions list.

- **Random reading as stressor analysis applied to one's worldview ↔ the fan operation.** The reflexive §5 of the [2021 *Machine in the Ghost*](../../references/papers/Residuality-Oreilly-2021-machine-in-the-ghost.md) paper explicitly frames O'Reilly's own random walk through the literature (Heidegger, Peirce, Prigogine, Serres, Latour, Stacey, Taleb, Baudrillard) as stressor analysis applied to the worldview of the architect. The cyberneutics fan operation does the same move in the decision domain. The convergence between O'Reilly arriving at this through residuality and cyberneutics arriving at it through committee deliberation is one seam in cyberneutics' [narrative-proof](../diary/2026-04-03-narrative-proof.md) web — narrow because n=2 with overlapping intellectual environments, but real where the structural pattern recurs. This is a candidate diary-entry seam not yet written.

- **The eye-of-the-storm architect ↔ the human gate.** O'Reilly's framing of the skeptical architect as "the eye of the storm" maps neatly onto the cyberneutics editorial human gate — the moment in the pipeline where the recursive deliberation terminates and a commitment is made. The 2026-04-20 diary recorded this as "one line worth keeping." It has not yet been used in any essay, but it is sitting in the wild ready for promotion.

- **Component metaphor critique ↔ Naur's theory-as-unit ↔ cyberneutics inspectability claim.** All three are the same diagnosis: the artifact is precipitate, not unit; the durable thing is what is harder to see. The 2026-04-25 diary developed this as the structural claim that the LLM cost shift makes operationally undeniable. None of the three sources frames itself in the others' vocabulary, but the unification is real and the diary records it.

- **The pask-mesh-fitting "mesh as accumulated funnel residue" framing.** [`wild/pask-mesh-fitting/mechanism-design-core.md`](../pask-mesh-fitting/mechanism-design-core.md) explicitly frames the entailment mesh as the accumulated residue of repeated funnel operations: "the mesh structure that survives repeated document admission is the eigenform of the corpus." This is residuality vocabulary (residue, eigenform) applied to a Pask-derived structure (entailment mesh) inside a cyberneutics operation (funnel). The framing is internal to the repository and is a working hypothesis about how Pask, residuality, and cyberneutics integrate at the corpus-curation layer.

- **Stacey as shared anchor.** Stacey's *Complexity and Organizational Reality* underwrites residuality theory's three-causalities-of-certainty critique and cyberneutics' resistance to expected-utility decision theory. Cyberneutics references Stacey only via the residuality bibliography; residuality references Stacey directly four times in the 2021 paper. **Stacey has been ordered (late April 2026); delivery expected late April / early May 2026.** Once in hand, primary-source engagement is the next move; until then the cybernetics-critique answer that essay-13 must make load-bearing is drafted on a secondhand reading.

- **The 2023 paper's processuality/criticality/difference triad ↔ cyberneutics' bridge=feedback=differentiation=teachback synthesis.** Essay 11's four-pillar synthesis (Dervin, von Foerster, Deleuze, Pask) and O'Reilly's 2023 triad cover overlapping territory in different vocabularies. Both are answers to "what's the unit of architecture-as-process?" The two sets of pillars could be cross-mapped: processuality ↔ Dervin (the gap is dynamic); criticality ↔ Pask (teachback as criticality test); difference ↔ Deleuze (explicit). The residuality side would benefit from the cyberneutics multi-pillar reading; the cyberneutics side would benefit from the residuality terms-of-art being recognized as load-bearing in essay 11 rather than as supporting analogy.

- **Assemblage, rhizome, and nomadic distribution as residuality's operative grammar.** Three concepts from Deleuze and Guattari's *A Thousand Plateaus* — assemblage, rhizome, and nomadic distribution — map onto load-bearing residuality constructs (the residue, the hypernetwork of residues, the architectural walk) closely enough to qualify as conceptual structure rather than analogy. The vocabulary itself is absent from O'Reilly's papers; the *commitments* are present in the corpus and most explicit in the 2023 paper. The full development is in [`assemblage-rhizome-nomad.md`](assemblage-rhizome-nomad.md). This finding sharpens the case for treating residuality and cyberneutics as two traditions arriving at Deleuze-Guattarian architectural commitments through different practical routes, rather than two systems with shared citations. Essay-13's spine candidate: the convergence under this grammar is one seam in the [narrative-proof](../diary/2026-04-03-narrative-proof.md) web — narrow because n=2 with overlapping intellectual environments — and the grammar's load-bearing claim (that it does explanatory work neither tradition could do alone) is testable via the falsifier paragraph in [`assemblage-rhizome-nomad.md`](assemblage-rhizome-nomad.md).

> **Correction note (2026-04-25).** The earlier diary entry [2026-04-20](../diary/2026-04-20-residuality-philosophy-paper-reading.md) characterized the 2021 *Philosophy* paper's Deleuze engagement as "name-check only" and recommended that essay-13's Deleuze framing be revised in favor of Serres and Latour. That characterization was accurate *for the 2021 paper alone* but mis-extrapolated to the corpus; the 2023 paper develops Deleuze substantively, with five in-text engagements and three secondary references. The recommendation to "soften the Deleuze framing in essays 06 and 10" — flowing from the diary — is therefore retracted. The corrected position is that Deleuze is a primary anchor in the 2023 paper, alongside the Serres-and-Latour anchor of the 2021 paper, and that essay-13 should reflect the multi-anchor reality of the corpus. See [`assemblage-rhizome-nomad.md`](assemblage-rhizome-nomad.md) for the full analysis.

---

## 4. Modifying or extending the survey paper

The survey [`state-of-residuality-2026.md`](state-of-residuality-2026.md) was written with care to present *O'Reilly's* residuality theory rather than the cyberneutics reading of it. Cyberneutics-side material was deliberately kept out so the survey could stand as a faithful third-party presentation. The following extensions stay within that constraint while adding clarity or completeness.

### 4.1 Add a worked example using Normand's coupon-banner case

The survey is currently light on concrete worked examples. Eric Normand's substack piece walks through a country-based coupon banner service end-to-end: stressor list, residue identification, incidence-matrix construction, K-reduction. ~300 words inserted into §6 (Residues and the stressor-driven design process) or §7 (The two-step algorithm) would give grounded readers something to anchor the abstractions to. Source: [Normand 2024 on Substack](https://ericnormand.substack.com/p/residuality-theory).

### 4.2 Add a "Residuality outside software architecture" subsection

Currently the survey ends at the historical-development section. A short §10.5 or §11.5 could note three extensions of residuality vocabulary that are happening outside the software-architecture corpus:

- **Naur's theory-building** as a parallel diagnosis (the artifact is precipitate; the durable thing is the team's living theory).
- **Pask's teachback** as conversation-scale residuality (knowledge is what survives shock-testing).
- **Sense-making methodologies** (the cyberneutics fan→funnel pipeline) as the two-step algorithm extended beyond software design.

Each in two or three sentences, with a footnote to the relevant repository file. This would broaden the survey's reach for readers who arrive at residuality theory from an adjacent domain.

### 4.3 Strengthen the "limits and external critique" section

Currently §10 raises four limits (unfalsifiability charge, definitional looseness, thin empirical case, selective cybernetics critique). Two more could be added:

- **The post-structural lineage is contingent.** O'Reilly is explicit that residuality was discovered in practice and only retroactively tied to Serres, Latour, Deleuze, Derrida. A different anchor (pragmatist, second-order systems-theoretic, Naur-style theory-building) would support similar architectural conclusions without committing to post-structuralism. The post-structural reading is one valid reading among possible readings of the same practice. The survey already gestures at this in §10, but it could be sharpened.
- **The two-step algorithm's generality is asserted, not demonstrated.** The 2022 paper claims that any software design methodology implicitly uses the two-step algorithm. The claim is plausible, but the paper does not work through (say) functional programming, formal-methods, or model-driven development to show how each instantiates the algorithm. This is empirical work residuality theory has not yet done.

### 4.4 Note the methodology-level recommendation that practitioners read philosophy

O'Reilly's NDC talks include explicit advice to practitioners to read philosophy. The 2021 *Machine in the Ghost* paper §5 is the textual home for this; the talks make it actionable. The survey currently treats philosophy as background to residuality theory. A sentence or two acknowledging that *recommending that architects read philosophy as a methodological prescription* is itself part of O'Reilly's program, not just an academic inheritance, would round out §11 (history) or §12 (reading paths).

### 4.5 Add a forward-looking section

The survey closes at §12 (Reading paths). A §13 — *Open work and what's missing* — could note:

- The unfalsifiability critique deserves engagement by a serious formal-methods critic.
- Larger-scale empirical validation of Ri (independent of O'Reilly's own circle) is a research gap.
- The Stacey/Serres/Latour anchors are load-bearing but under-engaged in the practitioner-level treatments.
- Residuality theory's intersection with theory-building (Naur), conversation theory (Pask), and sense-making methodologies (cyberneutics) is unwritten.

This would frame the survey as a starting point for further work rather than a finished portrait, which is the honest state of the literature.

### 4.6 Add a "tools that residual analysis lacks but should have" subsection

A practitioner reading the survey will reach §6 (residues + stressor process) and notice that the *operational* description of stressor generation is thin — "list stressors" is a step, but the act of producing a good stressor list is left to the architect's playfulness. A short note (~200 words) at the end of §6 or §7 could acknowledge this gap and point at LLM-driven divergent scenario generation as a candidate tool, with the cyberneutics fan operation as the worked example. This stays within the third-party-presentation constraint because the gap is real in O'Reilly's papers; flagging it does not require importing cyberneutics machinery into the survey.

### 4.7 The cyberneutics-side material that should *not* enter the survey

To be explicit about what stays out: the residue/eigenform distinction in its essay-10 form, the Probe-as-architectural-walks formalization, the inspectable-reasoning-records-as-criticality move, the Naur bridge, the calibration-register-as-long-run-Ri framing — these are cyberneutics contributions not part of O'Reilly's stated program as of 2024. The most directly actionable one — the fan operation as a stressor-list generator for residual analysis — has been written up in residuality-facing form as [`fan-as-stressor-generator.md`](fan-as-stressor-generator.md) (a self-contained note pitched at residuality practitioners). The other contributions remain Cyberneutics-internal as of this writing; whether and when they get residuality-facing treatment is open.

The current state therefore has four documents in the residuality multi-document set, each with its own audience: the survey [`state-of-residuality-2026.md`](state-of-residuality-2026.md) presents O'Reilly's view to a third-party reader; this bilateral note records the cyberneutics-↔-residuality relationship for repository contributors; the fan-as-stressor-generator note offers a single tool to a residuality practitioner without requiring methodology buy-in; the assemblage-rhizome-nomad note ([`assemblage-rhizome-nomad.md`](assemblage-rhizome-nomad.md)) develops the Deleuze-Guattarian grammar that operates in the corpus beneath O'Reilly's explicit citations. Essay-13 will be the cyberneutics-side numbered-essay statement, drafted after Stacey arrives; retention of the surrounding working notes is decided by deletion test once the essay is drafted.

---

## 5. Summary table

The table groups every connection by direction (inherited / contributed / parallel) and classifies contributed-back items along two orthogonal axes: **evidence tier** ((a) demonstrated in this repository / (b) implemented but not measured / (c) proposed but not implemented / (d) speculative or theoretical only) and **stance** (tool-or-cultural-practice × offer-or-prescription). Items classified as prescription are filed under "research directions about cyberneutics' practice" rather than as contributions to residuality theory; the prescriptive register would conscript the receiving tradition rather than offer to it.

Of the contributed-back items, the fan-as-stressor-generator is the only one written up in residuality-facing form. Two further items reach tier (a) (Probe as quantitative apparatus; situation-directory pattern as residue-from-live-process); the rest are scaffolding pending essay-13's drafting and any decision to externalize.

| Direction | Item | Where it lives now | Evidence tier | Stance |
|---|---|---|---|---|
| Inherited from residuality | Architectural-walks vocabulary | Essays 06, 10 | — | — |
| Inherited from residuality | Residue/eigenform distinction | Essays 04, 06, 08, 10; palgebra | — | — |
| Inherited from residuality | Criticality over correctness | Essay 10; methodology framing | — | — |
| Inherited from residuality | Stressor vocabulary at micro-scale | Essay 11; wild/cybernetics/conversation-theory.md | — | — |
| Inherited from residuality | Residual causality as dual-use frame | Diary 2026-04-20 | — | open thread |
| Contributed back | Probe as quantitative apparatus for walks | Essay 10; palgebra | (a) | tool, offer |
| Contributed back | Local/global eigenform distinction | Essays 04, 10 | (a) | tool, offer |
| Contributed back | Two-step algorithm generalized to sense-making | Essay 10; palgebra | (a) | tool, offer |
| Contributed back | Situation-directory pattern as residue-from-live-process | This repo's situation-directory practice | (a) | cultural practice, offer |
| Contributed back | Inspectable records as criticality | Methodology framing; diary 2026-04-25 | (b) | cultural practice, offer |
| Contributed back | Decision-landscape mapping as NKP generalization | Essay 10; palgebra; not yet formalized as NKP claim | (b) | tool, offer |
| Contributed back | Eigenform Ri (proposal §2.2) | §2.2 above | (c) untested | tool, offer |
| Contributed back | Calibration register as long-run Ri | §2.8 above; design target pending multi-agent substrate | (c) not implemented | tool, offer |
| Contributed back | Fan operation as stressor-list generator | [`fan-as-stressor-generator.md`](fan-as-stressor-generator.md); §2.9 above | (b) tool implemented; (c) Ri_F − Ri_A protocol untested | tool, offer |
| Contributed back | Second-order cybernetics answer to VSM critique | Diary 2026-04-20; §2.5 above | (d) | conceptual position, offer |
| Contributed back | Naur bridge | Diary 2026-04-25; §2.6 above | (d) | conceptual position, offer |
| Contributed back | Pask bridge | Essay 11; wild/cybernetics/conversation-theory.md; §2.7 above | (d) | conceptual position, offer |
| Research direction (not contribution) | Diary discipline as residuality-style organizational practice | This repo's diary practice | (d) | cultural practice, prescription |
| Research direction (not contribution) | Failure catalog for first-order applications of residuality | Not yet written | (d) | tool/framework, prescription |
| Parallel, not borrowed | Hyperliminality ↔ organ/bloodstream | Repo navigation | — | — |
| Parallel, not borrowed | Random reading ↔ fan operation | Diary 2026-04-20 (open seam) | — | candidate diary entry |
| Parallel, not borrowed | Eye of the storm ↔ human gate | Diary 2026-04-20 | — | candidate essay material |
| Parallel, not borrowed | Component metaphor ↔ Naur ↔ cyberneutics inspectability | Diary 2026-04-25 | — | stable framing |
| Parallel, not borrowed | Mesh as accumulated funnel residue | wild/pask-mesh-fitting | — | working hypothesis |
| Parallel, not borrowed | Stacey as shared anchor | References | — | under-engaged on cyberneutics side |
| Parallel, not borrowed | Triad ↔ four-pillar synthesis | Essay 11 vs O'Reilly 2023 | — | cross-mapping not written |

---

## See also

- [`state-of-residuality-2026.md`](state-of-residuality-2026.md) — survey paper
- [`residuality-bibliography.md`](residuality-bibliography.md) — union bibliography
- [`README.md`](README.md) — directory navigation
- [Diary 2026-04-20](../diary/2026-04-20-residuality-philosophy-paper-reading.md) — first careful reading of the 2021 *Philosophy* paper; the diary that records most of the inheritance/contribution distinction in working form
- [Diary 2026-04-25](../diary/2026-04-25-when-theory-formation-stops-being-free.md) — Naur bridge and the cost-shift framing
- [Essay 10 §Repetition as instrument](../../essays/10-decisions-under-uncertainty.md) — where the residue/eigenform distinction is presented as cyberneutics methodology
- [Essay 11 §Teachback as Micro-Residuality](../../essays/11-conversation-theory.md) — where the Pask bridge is developed
- [`wild/cybernetics/conversation-theory.md`](../cybernetics/conversation-theory.md) — fuller working note on the Pask/residuality unification
