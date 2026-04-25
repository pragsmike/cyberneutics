---
title: "O'Reilly Residuality Publications: Chronology"
type: chronology
covers: [O'Reilly residuality corpus 2018–2024]
purpose: "Reading map and Cite-which-for-what guide. Orientation layer above the per-paper summaries."
---

# O'Reilly Residuality Publications: Chronology

A chronology of Barry M. O'Reilly's published work on residuality theory, with notes on what each piece adds and how it sits in the lineage. Useful as an orientation document when working with the corpus or deciding which paper to cite for which claim.

For the bibliography proper (full annotations, formal citations), see [README.md](README.md). This file is supplementary — a reading map.

---

## At a glance

| Year | Title | Venue | Role in the corpus |
|------|-------|-------|---------------------|
| 2018 | "No More Snake Oil" | Cutter Consortium *Executive Update* | Practitioner version of the 2019 paper. Working out criticality-over-correctness in front of a non-academic audience. |
| 2019 | "No More Snake Oil: Architecting Agility through Antifragility" | *Procedia Computer Science* 151: 884–890 | First academic paper. Earliest formal statement of criticality-over-correctness. Antifragility (Taleb) is the primary theoretical anchor. |
| 2020 | "An Introduction to Residuality Theory: Software Design Heuristics for Complex Systems" | *Procedia Computer Science* 170: 875–880 | The operational paper. Incidence matrix technique, K-reduction heuristics, training/test holdout protocol. |
| 2020 | "There Is No Spoon — The Path to Residuality Theory" | Cutter Consortium collection | Compilation of Cutter pieces 2018–2020. Practitioner-facing synthesis bridging the 2019 and 2020 academic papers. |
| 2021 | "The Philosophy of Residuality Theory" | *Procedia Computer Science* 184: 809–816 | Philosophical counterpart to the 2020 paper. Component-metaphor critique; residual causality; Serres and Latour as primary post-structural anchors. |
| 2021 | "The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality" | *Philosophies* 6(4):81 | The non-Procedia journal piece. Journal-length development of *residual causality*, framed around political/autonomy stakes the workshop papers don't reach. Includes the reflexive "how residuality came to be" genealogy. Open access (MDPI, CC BY). |
| 2021 | "Hyperliminal Coupling, Why Software Projects Fail Repeatedly" | Cutter Consortium | Origin of the *hyperliminal coupling* concept that the 2022 paper inherits. Practitioner-pitched. Paywalled. |
| 2022 | "Residuality Theory, Random Simulation, and Attractor Networks" | *Procedia Computer Science* 201: 639–645 | Theoretical-consolidation paper. Grounds residuality in complexity science via Kauffman networks; formalizes the two-step algorithm (random stressor simulation + NKP analysis); introduces the residual index Ri as a per-project empirical test. |
| 2023 | "Residuality and Representation: Toward a Coherent Philosophy of Software Architecture" | *Procedia Computer Science* 224: 91–97 | Restatement of the 2021 *Philosophy* paper organized around three concepts: processuality, criticality, difference. Expanded post-structural lineage including Kant, Deleuze, Derrida. |
| 2024 | *Residues: Time, Change, and Uncertainty in Software Architecture* | Leanpub (~60 pp.) | Book-length practitioner synthesis. Treats the theory as ready for application rather than continued development. Mixed practitioner reviews. |

The five Procedia papers (2019, 2020, 2021, 2022, 2023) all appeared in the *International Workshop on Computational Antifragility and Antifragile Engineering* (the ANTIFRAGILE workshop series) — except the 2023 paper, which moved to the *International Conference on Mobile Systems and Pervasive Computing*. All are CC BY-NC-ND open access.

---

## What each piece adds

### 2018 — "No More Snake Oil" (Cutter Consortium)

Practitioner-facing piece in Cutter Consortium's *Business & Enterprise Architecture Executive Update*. The "snake oil" framing names the target: business-architecture frameworks and enterprise-agility programs sold as solutions to complexity but built on philosophical commitments (essentialism, formative causality) that the underlying complexity dissolves.

This is where the *vocabulary* of residuality is being worked out — "stressors," "residues," "naive architecture" — but the formal apparatus is not yet in place. It reads as a practitioner's case for taking complexity seriously rather than as a methodology paper. The Cutter version is closer in voice to O'Reilly's NDC talks than to the Procedia papers.

**Cite this when**: motivating residuality for a practitioner audience; tracing the vocabulary's origin; noting that the criticality-over-correctness move was already in place before the academic papers.

### 2019 — "No More Snake Oil: Architecting Agility through Antifragility" (Procedia 151)

The academic version of the 2018 piece, presented at the 6th ANTIFRAGILE workshop. This is the chronologically *first* formal residuality paper.

Two things make it load-bearing:

1. **First academic statement of criticality-over-correctness.** The reframing of the architect's goal — surviving the unknown rather than satisfying specifications — appears here for the first time in a peer-reviewed venue. Later papers cite [2] (Taleb's *Antifragile*) as background and assume the criticality move is settled; that move *originates here*.
2. **Antifragility is the primary anchor.** The 2019 paper develops antifragility (Taleb) as the architectural target more directly than any later paper. The 2020 introduction paper shifts to operational mechanics; the 2021 philosophy paper shifts to post-structural epistemology; the 2023 paper reorganizes around a different conceptual triad. The 2019 paper is where the Taleb connection is most explicit.

A common error is to cite the 2020 introduction paper for "criticality over correctness." That phrase and its argumentative weight come from the 2019 paper. The 2020 paper assumes it.

**Cite this when**: tracing the genealogy of the criticality concept; engaging with the Taleb connection directly; addressing the antifragility-is-the-architectural-target claim.

### 2020 — "An Introduction to Residuality Theory: Software Design Heuristics for Complex Systems" (Procedia 170)

The operational paper. This is what Eric Normand's substack pedagogy is teaching. The incidence-matrix technique, the K-reduction heuristics (split high-coupling columns, merge identically-signaturing columns, add mitigations), the training/test holdout protocol for empirical verification — all here.

Theoretical content is thin compared to the 2021 and 2023 papers. The justification for *why* the method works is largely deferred: Kauffman networks, attractors, and Monte Carlo sampling of attractor space are gestured at but not philosophically grounded. The 2021 paper is where the grounding lives.

**Cite this when**: describing the matrix technique, the merge/split heuristics, or the empirical protocol; pointing readers at the practitioner-accessible methodology rather than the philosophy.

### 2020 — "There Is No Spoon: The Path to Residuality Theory" (Cutter Consortium)

A compilation of O'Reilly's Cutter pieces from 2018 through early 2020, framed by a foreword that places residuality in the context of his earlier writing. Useful as a single-document source for the practitioner pieces.

The title is a Matrix reference: components and processes are not real, they are byproducts of system execution rather than its structure ("designing cars based on tire tracks in a muddy field"). This is the most accessible form of the process/substance inversion.

**Cite this when**: introducing the process-not-substance move to a non-academic audience; quoting O'Reilly's own voice on the practitioner side; tracing the genealogy of the Cutter material.

### 2021 — "The Philosophy of Residuality Theory" (Procedia 184)

The philosophical counterpart to the 2020 introduction paper. Where the 2020 paper says how, the 2021 paper says what about reality has to be true for the how to work.

Key contributions:

1. **The component-metaphor critique** — organizations modeled as capabilities/processes/use cases/components is a heuristic that smuggles in four philosophical commitments (essentialism, the causalities of certainty, cybernetics, structuralism) without architects examining them.
2. **Residual causality** — structure itself is the risk. Architectural decisions impose future-destroying constraints that cannot be predicted at design time. Architecture as risk source rather than risk reduction.
3. **Post-structural anchoring via Serres and Latour, not Deleuze.** Deleuze is name-checked once as endorsing post-structuralism's "escape from rigid structures." The substantive theoretical work is done by Brown's reading of Serres (noise, modeling, translation) and Latour's actor-network theory and *Science in Action*.

The 2021 paper is where O'Reilly explicitly names the cybernetics critique that engaging frameworks (including those that draw on Stafford Beer's VSM) need to answer. It cites Stacey four times; Stacey's *Complexity and Organizational Reality* (2009) is load-bearing for this paper specifically.

**Cite this when**: making the structure-as-risk argument; engaging with the post-structural commitments of residuality; addressing the cybernetics critique directly; tracing residual causality as a concept distinct from the operational matrix technique.

### 2021 — "The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality" (*Philosophies* 6(4):81)

The non-Procedia journal piece. Open access in MDPI's *Philosophies* (CC BY 4.0). Treated by O'Reilly as the extended development of *residual causality* — the concept that the *Philosophy of Residuality Theory* paper introduces and that the 2022 and 2023 papers assume. The 2022 paper cites it as ref [7] alongside the Procedia *Philosophy* paper ([6]) when it gestures at the philosophical foundations.

The Procedia 2021 paper is short (8 pp.) and pitched at the ANTIFRAGILE workshop audience. *Philosophies* gave O'Reilly room to develop the same arguments at journal length (~7,400 words; the Procedia papers are ~3,500–4,300) and pitch them at a philosophy-of-technology audience.

Three things make this paper distinct from the rest of the corpus:

1. **The political/autonomy framing.** Residual causality is reframed as a *threat to human autonomy* in a hyperconnected society, with the COOP ransomware attack (Sweden, June 2021) as the opening case. The workshop papers stay inside the architecture-quality frame; this paper goes external.
2. **The reflexive §5.** O'Reilly narrates how residuality theory came into being through his own random walk through the literature — Taleb, Cynefin, Stacey, Peirce's Tychism, Prigogine, Serres, Latour, Heidegger, Baudrillard — and explicitly frames that walk as the philosophical equivalent of stressor analysis. Random reading stresses the worldview of the architect and reveals invisible coupling between embedded paradigmatic assumptions and design behaviour. This is the only paper where O'Reilly tells the theory's intellectual genealogy.
3. **Most explicit list of philosophical sources in the corpus.** Heidegger (technology obscures other ways of seeing), Peirce (Tychism), Prigogine ("order floating on disorder" — the source phrasing for hyperliminality), Serres via Latour 1987 (gestalt switch), Stacey (dominant discourse), Taleb, Baudrillard (simulacra). Each is named as load-bearing for a specific construct.

The paper is archived locally (see [`Residuality-Oreilly-2021-machine-in-the-ghost-summary.md`](Residuality-Oreilly-2021-machine-in-the-ghost-summary.md)).

**Cite this when**: residual causality is itself the topic, not a stepping-stone to the matrix technique; the political/autonomy frame matters; engaging with a philosophy-of-technology audience; tracing the genealogy of how residuality emerged; pulling on Peirce's Tychism, Prigogine, or Heidegger as anchors for hyperliminality. **Don't cite this when**: the audience needs the four-pillar component-metaphor structure done concretely (use the Procedia *Philosophy* paper instead — it's tighter on that point).

### 2022 — "Residuality Theory, Random Simulation, and Attractor Networks" (Procedia 201)

The theoretical-consolidation paper, presented at the 9th ANTIFRAGILE workshop (Porto). This is where residuality is reframed as a complexity-science theory: the constructs from 2019–2021 are summarized through the lens of a single two-step algorithm (random stressor simulation followed by NKP network analysis on the software architecture), and the underlying logic is filled in via Kauffman networks and attractor theory.

Two contributions matter most:

1. **The two-step algorithm.** Software design *in general* is reframed as random simulation + network analysis; residuality is the variant that makes both steps explicit and amplifies their randomness/explicitness. This is the move that lets residuality be compared to other software design methodologies on a common axis rather than as a separate paradigm.
2. **The residual index Ri.** A per-project empirical test: divide stressors into training and testing sets, build the residual architecture from training, score the testing set against both naïve and residual architectures. Ri > 0 means the residual approach handled out-of-sample stress better than the naïve baseline. This is the falsifiability move the philosophy papers gesture at.

The paper also names *NKP analysis* as the architectural lens: N (number of components), K (max connections per component), P (bias toward a particular outcome). Loose coupling, cohesion, granularity — the practitioner vocabulary — are recast as NKP-tuning operations. Edge of chaos as the design target.

This paper is the clearest single statement of how residuality fits inside the complexity sciences. If you cite only one paper for the full theory-as-theory story, this is it.

**Cite this when**: relating residuality to complexity science (Kauffman, attractors, edge of chaos); using the two-step algorithm or NKP analysis vocabulary; needing the residual index Ri as the per-project empirical test; comparing residuality to other software methodologies on a shared axis.

### 2023 — "Residuality and Representation" (Procedia 224)

The restatement. Two years on, O'Reilly reorganizes the 2021 paper's arguments around a different conceptual structure: processuality, criticality, difference. The post-structural lineage is broadened — Kant gets the Critique-of-Pure-Reason citation, Deleuze and Derrida appear by name, the lineage now runs Kant → Cilliers (post-structural complexity) → Deleuze/Derrida → residuality.

This is also where the term **phenomenal gap** (borrowed from Cilliers) gets named: the gap between the processes that drive a system and the static representations we can form of it. Post-structuralism, complexity science, and reflective practice are framed as three charts of the same territory.

The 2023 paper is the better text if your audience is academic-philosophical. The 2021 paper is the better text if your audience needs to see the component-metaphor critique done concretely. Both papers cite each other and are best read as a pair.

**Cite this when**: working with the processuality/criticality/difference triad; engaging with the Kant lineage or the broader post-structural reading; using the phenomenal-gap terminology.

### 2024 — *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub)

A short book (~60 pages, ~45 at the writing of some early reviews) consolidating the theory for practitioners. O'Reilly is finishing a PhD in complexity science at the Open University around the time of publication; the book is the practitioner-facing companion to the academic corpus.

Practitioner reception is mixed. Sympathetic reviewers describe it as a clear and accessible introduction. Critical reviewers — including at least one extended Goodreads review — argue that the theory is "unfalsifiable," "self-defeating," and dismissive of effective principles (SOLID, DRY, modularity patterns). The book does not attempt formal mathematical foundations, which reviewers in formal-methods traditions find unsatisfying.

For our purposes, the existence of critical reviews matters: it means there is a small but real critical literature on residuality from outside O'Reilly's own writing. Engaging with that literature (rather than working from O'Reilly's papers alone) is the kind of move the cyberneutics narrative-proof argument benefits from.

**Cite this when**: introducing residuality to a working architect; engaging with practitioner reception; or explicitly addressing the "where is the formal foundation" critique.

---

## Reading paths

If you have read none of it: start with **Normand's substack piece** (linked in [README.md](README.md)), then the **2020 introduction paper**. That gets you operational mechanics in roughly two hours.

If you have read the operational material and want the philosophy: read the **2021 philosophy paper** first, then the **2023 restatement**. Reading them in publication order shows you what O'Reilly was working out and what he then reorganized; reverse order risks projecting the 2023 lineage backward onto the 2021 paper.

If you are tracing the genealogy of "criticality over correctness": go to the **2019 paper**. The phrase and its argumentative weight originate there.

If you are writing for practitioners: the **2018 Cutter piece** and the **2024 book** are the most accessible entry points. The Procedia papers are short but academically pitched.

For cyberneutics-internal use: the **2021 paper** is the load-bearing citation for residual causality, the component-metaphor critique, and the cybernetics critique that essay-13 has to answer. The **2020 paper** carries the matrix technique and the empirical protocol. The other papers are valuable but secondary for our purposes.

---

## Adjacent works worth tracking

These are not O'Reilly's residuality papers, but they are repeatedly cited within the corpus and are part of any serious engagement with it.

- **Stacey, Ralph D.** *Complexity and Organizational Reality* (2009). Routledge. — Cited four times in the 2021 paper. The three causalities of certainty and the dominant-discourse critique come from here.
- **Brown, Steven D.** "Michel Serres: Science, translation and the logic of the parasite." *Theory, Culture & Society* 19(3) (2002): 1–27. — The Serres interpretation O'Reilly uses.
- **Cilliers, Paul.** *Complexity and Postmodernism* (1998). Routledge. — The phenomenal-gap concept and the post-structural-complexity bridge originate here.
- **Taleb, Nassim Nicholas.** *Antifragile* (2012). Allen Lane. — Cited as [2] across all four Procedia papers.
- **Kauffman, Stuart A.** *The Origins of Order* (1993). Oxford. — The NK network framework and the attractor argument the 2020 paper appeals to.
- **Latour, Bruno.** *Science in Action* (1987) and *Reassembling the Social* (2007). — The constructivist anchor for the 2021 paper.

Of these, Stacey is the most directly load-bearing and the most worth adding to the inventory if not already present.

---

## Notes on retrieval

The Procedia papers are open access (CC BY-NC-ND) and *should* be fetchable from ScienceDirect, but ScienceDirect's robots.txt blocks automated fetches. Working routes:

- Direct URL via a browser: ScienceDirect serves the PDFs without a paywall for these specific papers.
- The Open University repository (oro.open.ac.uk) hosts at least the 2023 paper, sometimes returning 403 for automated requests but accessible via browser.
- ResearchGate hosts at least the 2019 "No More Snake Oil" paper.
- The 2018–2020 Cutter Consortium collection is hosted on cutter.com and is freely downloadable as a single PDF.

The 2024 book is on Leanpub. Leanpub's standard policy includes a 60-day full refund window, which makes it low-risk to purchase for review.

NDC talks (Oslo 2024, London 2024) are on YouTube and are O'Reilly's most accessible long-form presentations of the theory in his own voice. The Boundaryless podcast interview (Feb 2023) is shorter and more focused on the philosophical commitments.
