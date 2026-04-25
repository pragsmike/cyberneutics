# An Introduction to Residuality Theory: Software Design Heuristics for Complex Systems

**O'Reilly, Barry M.** *Procedia Computer Science* 170 (2020): 875–880. CC BY-NC-ND 4.0.
7th International Workshop on Computational Antifragility and Antifragile Engineering, April 2020, Warsaw.
DOI: [10.1016/j.procs.2020.03.120](https://doi.org/10.1016/j.procs.2020.03.120)

*First paper to present residuality theory as a formal framework (building on the 2019 heuristics paper).*

---

## Summary

Standard software design methodologies — OOP, SOA, microservices — treat systems as collections of components whose structure is determined by functional requirements and predicted change. O'Reilly argues this approach is constitutively inadequate for complex environments: it assumes that uncertainty can be reduced to manageable risk through requirements engineering, when in fact the stressors that cause project failure are precisely those not anticipated by requirements or risk analysis. The paper introduces residuality theory as an alternative design foundation.

A **residue** is the subset of a system that survives when a specific stressor impacts it — "the leftovers." A **stressor** is any event not designed for. Rather than starting design from components, residuality starts from residues: what would remain of this system under this form of stress? Iterating across many stressors, the design emerges as a multi-dimensional structure of interacting residues, described using Design Structure Matrices (DSMs) and incidence matrices. The resulting architecture places non-functional properties (resilience, antifragility) as first-class inputs to design rather than post-production afterthoughts.

The process borrows from machine learning: the stressor list is divided into training and testing sets (bagging and boosting), and residual architectures are compared against the naïve architecture using a **residual index Ri** — a direct measure of resilience improvement before building. The key claim: each adapted residue handles more stressors than the one that defined it, due to overlapping information flows. Exaptation rather than targeted protection.

---

## Key Claims

- Designing for change is insufficient: accurate prediction in complex environments is impossible by definition.
- Residues, not components, are the appropriate units of design in complex environments.
- Architecture is multidimensional; each residue is a separate dimension.
- The most important architectural boundaries are between residues, not between components or use cases.
- Structural decisions *restrict* future possibility — structure is a risk, not just a risk mitigation.
- A residual index (Ri > 0) provides pre-build empirical evidence of resilience improvement.
- Component structure is less important than residual boundaries.
- Rejects patterns as design inputs; solutions should be derived from first principles.
- Assumes that the set of all possible residues is smaller than the set of all possible stressors (Ashby's Law of Requisite Variety): each adapted residue handles multiple stressors.

---

## Key Quotations

> "Designing for change gives a false sense of security, since accurately predicting change in complex environments is, by definition, impossible." (p. 877)

> "Residuality theory reveals a system as actually being made up of a stack of shadows which we cannot see without turning various lights on and off." (p. 877)

> "Component structure is less important than residual boundaries." (p. 879)

> "Rather than starting with objects, microservices, or patterns, we start by analysing residues — unrelated to the structure of the underlying technology." (p. 877)

---

## Process of Residual Analysis (from §3)

1. Produce a naïve architecture using current methods.
2. Describe the system as a set of information flows between actors.
3. List stressors.
4. Describe residues and add functions allowing each to survive its defining stressor.
5. Investigate component structure inside residues using DSMs and incidence matrices.
6. Consolidate residues to prevent contagion (shared components where incidence matrices are similar; break out differing components as services).
7. Iterate with different training/testing stressor sets (bagging/boosting).
8. Compare residual architecture against naïve architecture using Ri.

---

## Cyberneutics Connections

- **Black Swan / wicked problems**: The core claim — that stressors causing failure are precisely those not anticipated — is the same structural diagnosis as the cyberneutics concern with wicked problems. The fan operation (divergent scenario generation) is the residuality stressor analysis applied to decision spaces rather than software systems.
- **Requisite variety**: Explicitly invoked (Ashby). Residuality theory operationalizes requisite variety as a design method: the architecture must have enough variety to absorb the variety of its stressor environment.
- **Via negativa**: Residual causality (§3) is explicitly via negativa — identify and remove causes of future restriction rather than identifying the ideal form. The committee pipeline similarly resists premature convergence.
- **Serialization problem**: The "stack of shadows" metaphor (each stressor illuminates a different residue) maps onto the committee's multiple-chart problem — no single description covers the system under all conditions.

---

## Epistemic Status

LLM-extracted content. Page numbers refer to the *Procedia Computer Science* paginated version. Quotations have been verified against the PDF. The residual index formula is mentioned but not algebraically stated in this paper; the 2022 paper develops it further.

---

*Companion to: `Residuality-Oreilly-2020.pdf`*
*See also: `Residuality-Oreilly-2019.md`, `The-Philosophy-of-Residuality-Theory.md` (2021), `Residuality-Oreilly-2022.md`, `Residuality-Oreilly-2023.md`*
*Cyberneutics cross-references: `essays/10-decisions-under-uncertainty.md`, `wild/diary/2026-02-21-cyberneutics-dual-operations.md`*
