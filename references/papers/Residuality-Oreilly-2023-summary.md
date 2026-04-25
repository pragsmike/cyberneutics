---
title: "Residuality and Representation — Summary"
author: "O'Reilly, Barry M."
year: 2023
venue: "Procedia Computer Science 224: 91–97"
doi: "10.1016/j.procs.2023.09.015"
license: "CC BY-NC-ND 4.0"
type: paper-summary
length_words: 1164
topics: [phenomenal-gap, processuality, criticality, difference, Deleuzian-walk, Kant, Cilliers, process-philosophy]
companion_full_text: Residuality-Oreilly-2023.md
companion_pdf: pdfs/Residuality-Oreilly-2023.pdf
---

# Residuality and Representation: Toward a Coherent Philosophy of Software Architecture

**O'Reilly, Barry M.** *Procedia Computer Science* 224 (2023): 91–97. CC BY-NC-ND 4.0.
20th International Conference on Mobile Systems and Pervasive Computing, August 2023, Halifax.
DOI: [10.1016/j.procs.2023.09.015](https://doi.org/10.1016/j.procs.2023.09.015)

*Philosophical maturation paper: introduces the phenomenal gap, frames residuality as process philosophy, and makes the Deleuze connection explicit through processuality, criticality, and difference.*

---

## Summary

This paper addresses why architects keep reverting to substance-focused static representations even after encountering residuality. The answer is philosophical: western philosophy — and software architecture's unconscious inheritance of it — is overwhelmingly a **substance philosophy**, focused on objects and their properties. Residuality is a **process philosophy**, and the shift requires rethinking what representation is for.

The key concept is the **phenomenal gap**: following Kant's noumena/phenomena distinction, the gap between a thing as it exists independently (noumena) and our sensory impression of it (phenomena). In simple, ordered systems this gap is small and manageable — we can predict, control, test. In complex systems — particularly enterprise environments — the gap is enormous and irreducible. Software must execute inside these environments, so any architecture based on representations of the environment is built on a phenomenally gapped foundation. The gap causes: non-linearity (behavior deviates from model predictions), emergence (behaviors not predicted by the representation), and unintended consequences of intervention.

Residuality responds to the phenomenal gap with three concepts that together constitute the architectural shift:

- **Processuality**: the world is constant becoming, not static entities. Residuality describes things as processes; substance is residue — the accidental leftovers of processes.
- **Criticality**: the goal of architecture shifts from correctness (a hangover from mathematical roots) to criticality — an internal structure capable of reorganizing to survive different attractors.
- **Difference**: residues represent not the whole system but only what differs between attractor states. Each residue is the difference a particular stressor makes. This is explicitly Deleuzian: identity is constituted through differences, not prior to them.

The Deleuzian walk metaphor: the first walk is one experience; subsequent walks reveal differences — seasonal changes, altered paths, new buildings. The walk's meaning is the accumulating sum of its differences, not the first traversal. Stressor analysis is this walk applied to software: each stressor reveals a different residue, and the architecture emerges from the pattern of differences.

---

## Key Claims

- Software architecture is unconsciously operating within a substance philosophy that is unsuited to complex environments.
- The phenomenal gap — the irreducible distance between our representation of an enterprise environment and the environment itself — is the root cause of architectural failure.
- Representation that imposes static objects on flux produces model compression, brittleness, and constant staleness.
- Residuality is process philosophy applied to software: substance is residue (leftover of process), not the foundation.
- The architect's goal should be criticality (structural capacity to survive attractor transitions), not correctness.
- Residues represent only differences, not total states. This is both philosophically aligned with Deleuze and practically tractable.
- Post-structuralism (Deleuze, Derrida, Cilliers) and the complexity sciences are describing the same problem — the phenomenal gap — from different vantage points.
- Residuality "forces a sharpening" of post-structural ideas and brings them to empirical inquiry.

---

## Key Quotations

> "Residuality is a skeptical, Humean treatment of complexity theory — reducing complexity to the minimum of what can be said, removing, as far as possible, opinion and speculation." (p. 93)

> "The residue is a centering of our fallibility — the idea that things will crumble, and that stress, flux, and volatility cannot be engineered or wished away." (p. 96)

> "Residuality is better described as anti-structuralism — constantly warning of the risks of structuralism and providing a means to question and mitigate the risk of naïve structure." (p. 96)

> "There is no representation of residue that is correct. This can be an incredibly difficult concept to grasp — but residues do not need to be accurately represented for the resulting architecture to demonstrably reach criticality." (p. 97)

> "The generation of each model is a Deleuzian walk, and the architect's understanding of the hyperliminal environment... grows with each walk." (p. 95)

---

## Philosophical Sources Named

- **Kant**: noumena/phenomena distinction; phenomenal gap as conceptual framework
- **Hume**: Humean constant conjunction; residuality as skeptical/minimalist treatment of causality
- **Deleuze** (*Difference and Repetition*): difference as constitutive of identity; stressor analysis as Deleuzian walk; Bergsonian processuality; repetition revealing differences
- **Derrida**: deconstruction as challenging incumbent structure and seeking fault lines
- **Cilliers**: bridge between complexity sciences and post-structuralism
- **Spinoza** (via Deleuze): "a thing is more about its conditions than its properties"
- **Bateson**: difference as foundational
- **Whitehead**: fallacy of misplaced concreteness — the error of treating abstract models as concrete
- **Wittgenstein** (late): tolerance for blurry pictures in the phenomenal gap
- **Bergson**: science lacks a metaphysics (echoed by residuality's filling of that gap)
- **Kuhn**: paradigm crisis; software architecture as Kuhnian crisis without a new paradigm
- **Schön**: reflective practice vs. technical rationality; the Deleuzian walk as reflective practice

---

## Cyberneutics Connections

- **Processuality and the committee.** The committee pipeline embodies process philosophy at the methodology level: it defers substance (the committed resolution) until process (deliberation) has run. The fan is processual; the funnel produces the residue.
- **Phenomenal gap and wicked problems.** The phenomenal gap is the technical concept underlying what cyberneutics calls wicked problems: the gap between any representation and the complex environment in which decisions must be made. Residuality and cyberneutics both respond by making the gap explicit (via stressor analysis / fan) rather than pretending it away.
- **Criticality vs. correctness.** Cyberneutics explicitly rejects "best answer" as the evaluation target for the committee, substituting inspectable reasoning chains. This is the same shift as correctness → criticality: the value is not being right but being structurally capable of being right in the relevant class of conditions.
- **Difference as information.** The funnel doesn't pick the best scenario — it preserves the structure of disagreements between them. Each character's perspective is a walk that reveals different residues. The narrative proof entry makes this explicit: the *differences* between formulations are as informative as the similarities.
- **Deleuze connection.** The 2026-04-03 narrative proof diary entry engages Deleuze directly and connects his difference/repetition framework to the fan operation. O'Reilly independently arrived at the same connection through practice. This is itself a case of narrative proof — the convergence strengthens both formulations.
- **The phenomenal gap and organ/bloodstream.** The organ regime is the tractable, small-phenomenal-gap regime: controlled channels, inspectable transformations, tight coupling between representation and reality. The bloodstream is large-phenomenal-gap: unprovenanced, loosely typed, requiring external judgment. Residuality's hyperliminal condition is the architecture-level version of operating in bloodstream.

---

## Epistemic Status

LLM-extracted content. Page numbers refer to the *Procedia Computer Science* paginated version. The philosophical connections to Kant and Deleuze are extensive and direct; quotations verified against the PDF.

---

*Companion to: `pdfs/Residuality-Oreilly-2023.pdf`*
*See also: [`Residuality-Oreilly-2019-summary.md`](Residuality-Oreilly-2019-summary.md), [`Residuality-Oreilly-2020-summary.md`](Residuality-Oreilly-2020-summary.md), [`Residuality-Oreilly-2021-summary.md`](Residuality-Oreilly-2021-summary.md) (Philosophy of Residuality), [`Residuality-Oreilly-2021-machine-in-the-ghost-summary.md`](Residuality-Oreilly-2021-machine-in-the-ghost-summary.md) (Machine in the Ghost), [`Residuality-Oreilly-2022-summary.md`](Residuality-Oreilly-2022-summary.md), [`Residuality-Oreilly-chronology.md`](Residuality-Oreilly-chronology.md)*
*Cyberneutics cross-references: `wild/diary/2026-04-03-narrative-proof.md`, `essays/10-decisions-under-uncertainty.md`, `essays/06-deleuze-difference-repetition.md`, `palgebra/`*
