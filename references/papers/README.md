# references/papers/

Archived papers cited elsewhere in the Cyberneutics repository.

## Reading order for agents

If you are looking up "what does X cite for Y" or doing background reading, **start with the summary**. The full extractions exist for verification and for deep reading; they are 3–10× the size of the summaries.

| Layer | Purpose | Approx. size |
|---|---|---|
| Summary (`<slug>-summary.md`) | Curated key claims, quotations, and cyberneutics connections. The default reading layer. | ~80 lines / ~2–3K tokens |
| Full text (`<slug>.md`) | Extracted body of the paper. Read when you need a specific passage or argument the summary doesn't cover. | ~120–190 lines / ~6–25K tokens |
| PDF (`pdfs/<slug>.pdf`) | Original file. Forensic only. Don't read it; it's binary and slow. Open only to verify the extraction or check a typesetting artifact. | n/a |

The chronology is the navigation layer: see [Residuality-Oreilly-chronology.md](Residuality-Oreilly-chronology.md) for which paper to cite for which claim, the relationships between papers, and notes on retrieval.

## Cite which paper for what

Quick picker for the O'Reilly residuality corpus. The chronology has the long form; this is the one-table version.

| To cite for... | Use | Why |
|---|---|---|
| Antifragility as the architectural target; the Taleb anchor; "criticality over correctness" | [2019](Residuality-Oreilly-2019-summary.md) | Origin of the criticality move; later papers assume it. The 2020 paper is often miscited for this. |
| Incidence matrices, K-reduction heuristics, the training/test stressor protocol | [2020](Residuality-Oreilly-2020-summary.md) | Operational paper. What practitioners apply. |
| The component-metaphor critique; residual causality as a concept; the cybernetics critique | [2021 *Philosophy*](Residuality-Oreilly-2021-summary.md) | Philosophical counterpart to the 2020 paper. Serres + Latour as the post-structural anchors. |
| Residual causality as a stand-alone concept; the political/autonomy stakes of software; reflexive genealogy of how residuality emerged; the "machine in the ghost" formulation | [2021 *Machine in the Ghost*](Residuality-Oreilly-2021-machine-in-the-ghost-summary.md) | The non-Procedia journal piece. Journal-length development; political framing the workshop papers don't have; the only paper where O'Reilly narrates the theory's intellectual genealogy in the first person. |
| Kauffman networks, NKP analysis, edge of chaos, the residual index Ri, the two-step algorithm | [2022](Residuality-Oreilly-2022-summary.md) | Theoretical-consolidation paper. Where residuality is reframed inside complexity science with an empirical falsifiability move. |
| The phenomenal gap; processuality / criticality / difference; the Deleuzian walk; Kant lineage | [2023](Residuality-Oreilly-2023-summary.md) | Restatement of the philosophical arguments around a different conceptual triad. Better text for academic-philosophical audiences. |

For the genealogy, the philosophical lineage shifts, common miscitations, and reading paths, see [Residuality-Oreilly-chronology.md](Residuality-Oreilly-chronology.md).

---

## Adding a paper

When a new PDF is dropped into this directory, assimilate it by following these steps. The scheme is the one already in use across every existing paper; the instructions here exist so you don't have to rediscover it.

1. **Place the PDF** at `pdfs/<name>.pdf` using the same naming convention as siblings (e.g. `Residuality-Oreilly-2019.pdf`, `Residuality-Oreilly-2021.pdf`).

2. **Extract the text to `<name>.md`** with `pdftotext -layout pdfs/<name>.pdf -` and hand-clean:
   - Strip ScienceDirect/Elsevier/Procedia boilerplate, running heads, and page-footer copyright blocks.
   - Fix hyphenation artifacts (`pro- vides` → `provides`) and layout-mode interleaving (common in the abstract, where two-column flow confuses `-layout`).
   - Preserve numbered sections as `## N. Title` and subsections as `### N.N. Title`. Keep the full numbered reference list under `## References`.
   - Include abstract, keywords, acknowledgements if present.
   - Do **not** silently correct typos in the source. Preserve them and flag them in the summary's Epistemic Status section.

3. **Write `<name>-summary.md`** using the template every existing summary follows. Required sections, in order:
   - H1 title, bold citation line + DOI link, italic one-line positioning.
   - `## Summary`, `## Key Claims`, `## Key Quotations` (page-cited, verified against the PDF).
   - One or two paper-specific sections (a process table, a list of philosophical sources named, etc.).
   - `## Cyberneutics Connections`, `## Epistemic Status`.
   - Three-line footer: `*Companion to: …*`, `*See also: …*`, `*Cyberneutics cross-references: …*`.

4. **Register the paper in this README.** Add an H3 block with bold `**Citation:**`, bold `**Summary:**` one-paragraph line, and three bulleted links (full text, summary, PDF). Update the series intro blurb and the *Cite which paper for what* table if the new paper changes the arc, ordering, or coverage of distinct claims. Remove the paper from the "Cited but not archived" table if it was listed there.

5. **Register the paper in `references/README.md`** — the master bibliography. Add an entry under the appropriate tradition section with citation, one-line annotation, and a link back to the local archive. The master bib is the discovery surface for agents reading from the top of the references tree; missing it here means future readers won't know the paper is locally available.

6. **Update the `See also:` footer of every other summary in the directory** so all summaries cross-reference each other symmetrically. The footer should list every sibling summary plus the chronology file.

7. **Update any chronology or reading-map files** (e.g. `Residuality-Oreilly-chronology.md`) that catalogue the corpus this paper belongs to. Both the at-a-glance table and the per-paper "What each piece adds" section need an entry. If the new paper changes which paper to cite for which claim, update the `Cite which paper for what` table at the top of this README.

8. **Verify.** Re-read this README to confirm links and the arc blurb render correctly; spot-check two or three page-cited quotations in the new summary against the PDF; run `Grep` on the old "Cited but not archived" entry to confirm no other doc still lists the paper as missing.

---

## O'Reilly — Residuality Theory series

Six papers from Barry M. O'Reilly's ongoing development of residuality theory, in chronological order. Together they form a self-contained arc: antifragility-driven heuristics and the first statement of criticality-over-correctness (2019) → the residual analysis process, incidence matrices, and training/test holdout (2020) → paired philosophical 2021 papers (the Procedia *Philosophy of Residuality Theory* critiques the component metaphor; the *Machine in the Ghost* journal piece develops residual causality at length and frames it as a threat to autonomy in hyperconnected society) → complexity-science formalization via Kauffman networks and the NKP residual index (2022) → process-philosophy treatment of representation, criticality, and difference (2023). Read them in order for the full argument; each paper builds explicitly on the prior ones.

---

### No More Snake Oil: Architecting Agility through Antifragility (2019)

**Citation:** O'Reilly, B. M. "No More Snake Oil: Architecting Agility through Antifragility." *Procedia Computer Science* 151 (2019): 884–890. CC BY-NC-ND 4.0.

**Summary:** Proposes Antifragile Systems Design as a third way between waterfall and Agile: a four-step process (VUCA analysis → Flow First Design decomposition → ATAM review → modified FMEA) that balances Hole's four antifragile properties (modularity, weak links, redundancy, diversity) against VUCA elements in the business model, and retargets architecture from correctness to antifragility via induced nonlinear system responsiveness.

- [Full text](Residuality-Oreilly-2019.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2019-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2019.pdf)

---

### An Introduction to Residuality Theory (2020)

**Citation:** O'Reilly, B. M. "An Introduction to Residuality Theory: Software Design Heuristics for Complex Systems." *Procedia Computer Science* 170 (2020): 875–880. CC BY-NC-ND 4.0.

**Summary:** Introduces residuality theory as a design discipline that treats a system's stress residues — what survives after each stressor — as the primary unit of architecture, replacing component-first approaches with a process of stressor analysis, incidence matrices, and bagging/boosting across training and testing stressor sets.

- [Full text](Residuality-Oreilly-2020.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2020-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2020.pdf)

---

### The Philosophy of Residuality Theory (2021)

**Citation:** O'Reilly, B. M. "The Philosophy of Residuality Theory." *Procedia Computer Science* 184 (2021): 809–816. CC BY-NC-ND 4.0.

**Summary:** Diagnoses the "component metaphor" — the cluster of essentialism, causalities of certainty, machine-metaphor cybernetics, and structuralism that underlies conventional software architecture — and argues that residuality theory constitutes a post-structuralist, constructivist paradigm shift grounded in Taleb, Stacey, Latour, and Serres.

- [Full text](Residuality-Oreilly-2021.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2021-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2021.pdf)

---

### The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality (2021)

**Citation:** O'Reilly, B. M. "The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality." *Philosophies* 6(4):81 (2021). CC BY 4.0.

**Summary:** The corpus's only non-Procedia journal piece, in MDPI's *Philosophies*. Develops *residual causality* at journal length and reframes it as a structural threat to human autonomy in a hyperconnected society — the political/autonomy stakes the workshop papers don't reach. Includes a reflexive section in which O'Reilly narrates how residuality theory came to be through his own random walk through the literature (Heidegger, Peirce's Tychism, Prigogine, Serres, Latour, Stacey, Taleb, Baudrillard) — explicitly framing random reading as stressor analysis applied to one's worldview.

- [Full text](Residuality-Oreilly-2021-machine-in-the-ghost.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2021-machine-in-the-ghost-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2021-machine-in-the-ghost.pdf)

---

### Residuality Theory, Random Simulation, and Attractor Networks (2022)

**Citation:** O'Reilly, B. M. "Residuality Theory, Random Simulation, and Attractor Networks." *Procedia Computer Science* 201 (2022): 639–645. CC BY-NC-ND 4.0.

**Summary:** Formalizes residuality theory as a two-step algorithm — random stressor simulation followed by NKP network analysis — grounded in Kauffman networks and attractor theory, and proposes the residual index Ri as an empirically falsifiable measure of architectural improvement.

- [Full text](Residuality-Oreilly-2022.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2022-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2022.pdf)

---

### Residuality and Representation (2023)

**Citation:** O'Reilly, B. M. "Residuality and Representation: Toward a Coherent Philosophy of Software Architecture." *Procedia Computer Science* 224 (2023): 91–97. CC BY-NC-ND 4.0.

**Summary:** Argues that traditional architectural representation is structurally harmful because it imposes static substance-philosophy models on a hyperliminal environment, and that residuality — through the concepts of processuality, criticality, and Deleuzian difference — offers a coherent alternative that represents flux rather than identity.

- [Full text](Residuality-Oreilly-2023.md)
- [Summary and cyberneutics connections](Residuality-Oreilly-2023-summary.md)
- [Original PDF](pdfs/Residuality-Oreilly-2023.pdf)

---

## Cited but not archived

These O'Reilly works are cited within the corpus or named in the chronology but not present locally. Listed in chronological order. The chronology has fuller annotations.

| Year | Title | Venue | Status |
|---|---|---|---|
| 2018 | "No More Snake Oil" | Cutter Consortium *Executive Update* | Practitioner version of the 2019 paper. cutter.com (free download). |
| 2020 | "There Is No Spoon: The Path to Residuality Theory" | Cutter Consortium collection | Compilation of 2018–2020 Cutter pieces. cutter.com (free download). |
| 2021 | "Hyperliminal Coupling, Why Software Projects Fail Repeatedly" | Cutter Consortium | Origin of the *hyperliminal coupling* concept used heavily in the 2022 paper. Paywalled. |
| 2024 | *Residues: Time, Change, and Uncertainty in Software Architecture* | Leanpub (~60 pp.) | Book-length practitioner synthesis. Paid (60-day refund window per Leanpub policy). |
