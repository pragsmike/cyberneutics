---
title: "The Philosophy of Residuality Theory — Summary"
author: "O'Reilly, Barry M."
year: 2021
venue: "Procedia Computer Science 184: 809–816"
doi: "10.1016/j.procs.2021.03.101"
license: "CC BY-NC-ND 4.0"
type: paper-summary
length_words: 1011
topics: [component-metaphor, residual-causality, post-structuralism, Serres, Latour, Stacey, cybernetics-critique, via-negativa]
companion_full_text: Residuality-Oreilly-2021.md
companion_pdf: pdfs/Residuality-Oreilly-2021.pdf
---

# The Philosophy of Residuality Theory

**O'Reilly, Barry M.** *Procedia Computer Science* 184 (2021): 809–816. CC BY-NC-ND 4.0.
8th International Workshop on Computational Antifragility and Antifragile Engineering, March 2021, Warsaw.
DOI: [10.1016/j.procs.2021.03.101](https://doi.org/10.1016/j.procs.2021.03.101)

*Philosophical grounding paper: establishes the implicit philosophy behind conventional architecture, critiques it, and locates residuality in post-structuralist and constructivist thought.*

---

## Summary

Software architecture has accumulated philosophical assumptions without ever examining them — a collection of borrowed ideas from business schools, physics, mathematics, and cybernetics that accidentally became the profession's worldview. This paper excavates those assumptions, names them collectively as the **component metaphor**, and argues that residuality theory represents a paradigm shift away from them.

The component metaphor rests on four pillars: **essentialism** (Platonic ideal forms underlying all real instances, manifest in OOP class hierarchies, reusable components, and SMART requirements); **causalities of certainty** (formative causality where cause is embedded in structure, rationalist causality where human reasoning masters outcomes, and efficient causality of direct cause-and-effect — together forming Stacey's "dominant discourse of management"); **cybernetics as machine metaphor** (mirroring human and social structures as machines, leading to simplistic control-focused models — the paper's critique of the VSM is pointed); and **structuralism** (seeking abstract underlying models with explicit relationship graphs, manifest in enterprise architecture and requirements engineering).

Residuality theory escapes this through **residual causality**: the acknowledgment that in complex environments the causal structure cannot be known in advance, and that structure itself becomes the risk. Rather than identifying ideal forms, residuality identifies residues — the actual leftovers after stress — and works via negativa: remove identifiable causes of future restriction rather than imposing structure. This aligns with post-structuralist thinking (Deleuze, Derrida, Serres) and constructivism, though O'Reilly emphasizes the practice-first origins: residuality was discovered through tinkering, not derived from Serres or Deleuze.

The paper concludes that the component metaphor and residuality theory can coexist on the same project; the component metaphor is itself a residue — what remained after complexity exposed the weaknesses of prior approaches.

---

## Key Claims

- Architecture as a profession has no examined philosophy; its assumptions were inherited accidentally.
- Essentialism, causalities of certainty, machine-metaphor cybernetics, and structuralism together form the component metaphor.
- The component metaphor treats structure as risk mitigation; residuality theory treats structure itself as risk.
- Residual causality: structure restricts future possibilities — this is the primary risk in software architecture, not external threats.
- Architecture as currently practiced requires ignoring residuality theory to engage in good faith with standard methods (requirements, patterns, risk management).
- Residuality is a post-structuralist, constructivist, via negativa approach that emerged from practice rather than theory.
- The component metaphor is itself a residue — a leftover from the stress complexity imposed on prior approaches.

---

## Key Quotations

> "One of the major errors in establishing the profession of the software or IT architect has been the inability or lack of interest to establish a philosophy of architecture." (p. 810)

> "Rather than being a way to reduce risk in a system, structure is a risk in the system." (p. 813)

> "This approach is via negativa — we cannot identify the perfect form for our software but we can identify residual cause and remove it, knowing that it is not the perfect form." (p. 813)

> "Residuality theory encourages noise where the component metaphor smothers it." (p. 813)

> "Residuality theory does not project a combative dichotomy with the component metaphor, both can coexist quite happily in the same project... The component metaphor is a residue that required the development of residuality theory." (p. 815)

---

## Critique of Cybernetics (§ on Cybernetics)

The paper explicitly critiques cybernetics as part of the problem: "Cybernetics is also firmly rooted in the causalities of certainty — illogically split between formative and rationalist causalities. The mirroring of human and social structures as machines has had a lasting effect on the philosophical worldview of software designers." The VSM is named as a "second order abstraction" that gives "a quasi scientific facade to decision making in conditions of high uncertainty."

This is important context for cyberneutics: the methodology must distinguish itself from the control-focused, machine-metaphor use of cybernetics that O'Reilly criticizes, and align with the second-order, observer-included cybernetics of von Foerster and Pask that the critique does not target.

---

## Philosophical Connections (Named in Paper)

- **Taleb**: Antifragile, Platonic folding, via negativa
- **Stacey**: Four causalities (formative, rationalist, efficient, adaptionist, transformative), dominant discourse
- **Serres/Latour**: Noise as information, Science in Action, Actor Network Theory, the parasite
- **Deleuze**: Post-structuralism's escape from rigid structures
- **Post-structuralism**: Targets rigidity, categorization, universal truths
- **Constructivism**: Residuality leans toward a constructivist interpretation

---

## Cyberneutics Connections

- **The critique applies selectively.** The cyberneutics approach is not machine-metaphor cybernetics but second-order cybernetics (von Foerster, Pask, Beer's deeper recursive structures). The VSM critique targets the machine-metaphor use of Beer; the recursive/viable system logic that the metacognition thread uses (System 3* as audit channel) is at a different level.
- **Via negativa and the fan.** The fan operation as divergent scenario generation is via negativa applied to decision spaces: run multiple stressors (scenarios), identify what breaks, design away from breakage rather than toward an ideal form.
- **Structure as risk.** The palgebra's confidence-can-only-degrade propagation rule expresses the same instinct: committed structure (pipeline decisions) introduces brittleness; the fan defers structural commitment until the residual picture is clearer.
- **Noise as information.** "Residuality encourages noise where the component metaphor smothers it" connects directly to the committee's requisite variety logic and to the Kalman/sensor-array argument in the narrative proof diary entry: uncorrelated noise from independent sources is the signal about problem structure.
- **Deleuze connection.** Both residuality (2023 paper) and cyberneutics cite Deleuze's *Difference and Repetition* as philosophically aligned. The stressor analysis as Deleuzian walk (see 2023 paper) connects to the diary entry `2026-04-03-narrative-proof.md`.

---

## Epistemic Status

LLM-extracted content. Page numbers refer to the *Procedia Computer Science* paginated version. The cybernetics critique paragraph and VSM naming are direct quotations verified against the PDF.

---

*Companion to: `pdfs/Residuality-Oreilly-2021.pdf`*
*See also: [`Residuality-Oreilly-2019-summary.md`](Residuality-Oreilly-2019-summary.md), [`Residuality-Oreilly-2020-summary.md`](Residuality-Oreilly-2020-summary.md), [`Residuality-Oreilly-2021-machine-in-the-ghost-summary.md`](Residuality-Oreilly-2021-machine-in-the-ghost-summary.md) (Machine in the Ghost — companion 2021 paper), [`Residuality-Oreilly-2022-summary.md`](Residuality-Oreilly-2022-summary.md), [`Residuality-Oreilly-2023-summary.md`](Residuality-Oreilly-2023-summary.md), [`Residuality-Oreilly-chronology.md`](Residuality-Oreilly-chronology.md)*
*Cyberneutics cross-references: `essays/10-decisions-under-uncertainty.md`, `wild/diary/2026-04-03-narrative-proof.md`, `palgebra/`*
