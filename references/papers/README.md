# references/papers/

Archived papers cited elsewhere in the Cyberneutics repository.

## Organization

Each paper exists in two forms:

- **Markdown (`<name>.md`)** — extracted full text, structure preserved, boilerplate stripped. **This is the primary form.** Read the markdown, not the PDF.
- **Summary (`<name>-summary.md`)** — curated summary with key claims, selected quotations, and cyberneutics connections.
- **PDF (`pdfs/<name>.pdf`)** — original file, kept as a forensic source to verify the extraction. Do not read PDFs during normal work; they are binary, slow to process, and the markdown already contains the full text. Read a PDF only if explicitly instructed to do so, or if there is a specific reason to check the original against the extraction.

---

## Adding a paper

When a new PDF is dropped into this directory, assimilate it by following these steps. The scheme is the one already in use across every existing paper; the instructions here exist so you don't have to rediscover it.

1. **Place the PDF** at `pdfs/<name>.pdf` using the same naming convention as siblings (e.g. `Residuality-Oreilly-2019.pdf`, `The-Philosophy-of-Residuality-Theory.pdf`).

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

4. **Register the paper in this README.** Add an H3 block with bold `**Citation:**`, bold `**Summary:**` one-paragraph line, and three bulleted links (full text, summary, PDF). Update the series intro blurb if the new paper changes the arc count or ordering. Remove the paper from any trailing "Note" paragraph if it was listed there as "not archived."

5. **Update the `See also:` footer of every other summary in the directory** so all summaries cross-reference each other symmetrically.

6. **Update any chronology or reading-map files** (e.g. `Residuality-Oreilly-chronology.md`) that catalogue the corpus this paper belongs to.

7. **Verify.** `ReadLints` the touched files; re-read this README to confirm links and the arc blurb render correctly; spot-check two or three page-cited quotations in the new summary against the PDF.

---

## O'Reilly — Residuality Theory series

Five papers from Barry M. O'Reilly's ongoing development of residuality theory, in chronological order. Together they form a self-contained arc: antifragility-driven heuristics and the first statement of criticality-over-correctness (2019) → the residual analysis process, incidence matrices, and training/test holdout (2020) → philosophical critique of the component metaphor (2021) → complexity-science formalization via Kauffman networks and the NKP residual index (2022) → process-philosophy treatment of representation, criticality, and difference (2023). Read them in order for the full argument; each paper builds explicitly on the prior ones.

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

- [Full text](The-Philosophy-of-Residuality-Theory.md)
- [Summary and cyberneutics connections](The-Philosophy-of-Residuality-Theory-summary.md)
- [Original PDF](pdfs/The-Philosophy-of-Residuality-Theory.pdf)

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

**Note:** The 2021 paper ("The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality", *Philosophies* 6(4):81) and the 2021 "Hyperliminal Coupling" (Cutter Consortium) are cited in the series but not archived here.
