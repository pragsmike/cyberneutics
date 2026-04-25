# No More Snake Oil: Architecting Agility through Antifragility

**O'Reilly, Barry M.** *Procedia Computer Science* 151 (2019): 884–890. CC BY-NC-ND 4.0.
6th International Workshop on Computational Antifragility and Antifragile Engineering, April–May 2019, Leuven.
DOI: [10.1016/j.procs.2019.04.122](https://doi.org/10.1016/j.procs.2019.04.122)

*Progenitor paper: the first peer-reviewed statement of criticality-over-correctness and the most explicit Taleb/antifragility anchor in the series. The 2020 introduction paper formalizes the heuristics sketched here as residual analysis.*

---

## Summary

The paper diagnoses a gap in contemporary software practice: waterfall is known to fail, Agile has become a cluster of rituals with poor outcomes (a 2017 report of 300 CIOs cited 21% complete failure and £37bn annual cost), and a recent IASA Global survey of 260 organizations shows fewer than 50% have integrated architecture into their Agile process. The collision of "inflexible vs. unstable" software in VUCA environments (volatility, uncertainty, complexity, ambiguity) requires a third way. O'Reilly proposes **Antifragile Systems Design**: a short, Excel-tooled design process that treats antifragility — in Taleb's sense of gaining from disorder — as the architectural target, with agility as a downstream property.

The theoretical base is threefold: Taleb on antifragility and the Platonic fold, Parnas (1972) on volatility-based decomposition, and Hole's (2016) four properties of antifragile ICT systems — **modularity, weak links, redundancy, diversity**. Antifragile Systems Design balances these four properties against identified VUCA elements through four steps:

1. **VUCA Analysis** — spreadsheet the volatile/uncertain/complex/ambiguous elements of the business model (represented via the Business Model Canvas) and candidate mitigations.
2. **System Decomposition — Flow First Design** — describe the software as data flows, decouple each flow from all others, subject each to VUCA fluctuations, and consolidate (Parnas-style) for minimum disruption. Establishes modularity and weak links.
3. **Design Testing** — present the architecture to stakeholders via ATAM.
4. **Modified FMEA** — enumerate component failure modes without trying to prioritize risk; iterate mitigations. Establishes redundancy and diversity.

The argument for why this works is **nonlinear system responsiveness**: after roughly 50 mitigations, later VUCA elements are increasingly resolved by earlier mitigations — exaptation in the biological sense, where structure developed for one purpose serendipitously covers others. No mathematical guarantee, no prediction of the exaptation rate; the claim is only that the process *makes exaptation the premier focus of the design effort* and therefore tilts the system toward antifragility rather than away from it.

The vocabulary of later residuality theory — stressors, residues, naïve architecture — is not yet in place, but the core move is: architecture's target is not correctness against requirements but **criticality against the unknown**.

---

## Key Claims

- Agile without architecture is "snake oil": a correct diagnosis of waterfall's failure paired with a cure that does not bear investigation. The solution is neither to return to waterfall nor to extend Agile but to change what architecture is *for*.
- The correct architectural target in a VUCA environment is antifragility, not correctness. Agility is a consequence of antifragility, not the other way around.
- System fragility is a function of internal structure: how interconnected components are and how change propagates through the system. Architecture is the discipline that matches internal interconnectedness to the change the environment will impose.
- The four antifragile properties (Hole 2016) — modularity, weak links, redundancy, diversity — are the design levers. VUCA elements in the business model are the forcing function. The design process balances one against the other.
- Decomposition should follow volatility (Parnas 1972, Löwy's IDesign) rather than functionality. Flow First Design operationalizes this: flows are decoupled units of data transfer, later consolidated.
- Predicting specific risks is counterproductive in complex environments. Modified FMEA drops risk prioritization entirely and instead drives iteration until mitigations become repetitive.
- The process does not guarantee a result — this is a feature, not a bug. Taylorist measurement/prediction/comparison gives no benefit here; nonlinear system responsiveness ("exaptation") is induced, not designed directly.
- VUCA analysis forces architects into the business-model conversation. This is a role evolution, not an optional practice.

---

## Key Quotations

> "Rather than aiming to control, or to remove control, we seek to build systems, both technical and business, that aim to be Antifragile to change. This allows the production of business and technical architectures that actually enable Agility through design rather than process or 'mindset'." (p. 884, abstract)

> "This is what causes Agile mysticism; we know that waterfall will not work, so we reject it based on past experience but do not replace it with anything demonstrably better. This creates the gap for 'snake oil.'" (p. 885)

> "Thus, we propose that by architecting for antifragility, businesses can gain real agility and deliver systems with a higher level of quality… An antifragile system is by definition agile and resilient." (p. 885)

> "The solution to the Platonic fold requires accepting complexity as something we can neither predict nor control, along with accepting the limitations of modeling and risk management. Instead of pursuing correctness in these areas, we should aim to build systems that are antifragile to fluctuations in the VUCA elements." (p. 885)

> "When we combine two separate mitigations, say the wall and the fact that we added a space in the wall for insulation, we suddenly create the conditions for dealing with something we did not see coming — hiding electrical wires in the wall!" (p. 888)

> "By following this process, the system trends toward antifragility, which is the only possible good result in a complex environment that we do not control… We call this pattern nonlinear system responsiveness." (p. 888)

> "There is no guaranteed result from this process, so the Taylorist approach of measurement, prediction, and comparison will not provide any benefit here." (p. 889)

---

## Antifragile Systems Design (from §4)

The four-step process with its associated antifragile property:

| Step | Activity | Artifact | Antifragile property tuned |
|------|----------|----------|-----------------------------|
| 1. VUCA Analysis | Enumerate volatile/uncertain/complex/ambiguous elements of the business model; list mitigations | VUCA spreadsheet; Business Model Canvas | — (forcing function) |
| 2. System Decomposition (Flow First Design) | Describe software as decoupled data flows; subject each to VUCA; consolidate Parnas-style | Flow decomposition | Modularity, weak links |
| 3. Design Testing | Present architecture to stakeholders via ATAM | Architecture review | — (validation) |
| 4. Modified FMEA | Enumerate failure modes without prioritizing risk; iterate mitigations until repetitive | FMEA spreadsheet | Redundancy, diversity |

Exaptation / nonlinear system responsiveness is the claim that after ~50 mitigations, new VUCA elements are increasingly absorbed by structure already present — the design effort is trying to *induce* this, not predict it.

---

## Cyberneutics Connections

- **Progenitor of the criticality move.** The chronology in [references/papers/Residuality-Oreilly-chronology.md](Residuality-Oreilly-chronology.md) identifies this paper as the origin of O'Reilly's "criticality over correctness" argument — the move the later papers assume. For cyberneutics, which likewise rejects "best answer" as the evaluation target for deliberative artifacts, this is the load-bearing citation: architecture and deliberation are both being retargeted from correctness to structural capacity to survive.
- **VUCA as the fan's forcing function.** VUCA analysis is a proto-stressor enumeration: list everything that could change, deliberately, before the design closes. The committee pipeline's fan operation (divergent scenario generation) is the same move applied to decision spaces — enumerate the breadth of possibility before funneling. See [essays/10-decisions-under-uncertainty.md](../../essays/10-decisions-under-uncertainty.md).
- **Exaptation and narrative coverage.** Nonlinear system responsiveness — structure developed for one stressor serendipitously covering others — is the software-architecture analog of narrative proof's claim that independent formulations of the same problem strengthen each other. Coverage is emergent from the pattern of mitigations, not designed directly. See [wild/diary/2026-04-03-narrative-proof.md](../../wild/diary/2026-04-03-narrative-proof.md).
- **Volatility-based decomposition and the organ/bloodstream boundary.** Parnas-via-Löwy's volatility-based decomposition (focus on what can change, not what is) mirrors cyberneutics' organ/bloodstream distinction: the organ regime (controlled, typed, inspectable) is where volatility is bounded; the bloodstream (unprovenanced, loosely typed) is where volatility dominates and structure must absorb change rather than resist it.
- **FMEA without risk prioritization.** The modified FMEA's explicit refusal to rank-order risks is the same epistemic posture as cyberneutics' refusal to aggregate committee members into a single score. Both preserve the variety of failure modes rather than collapsing them to a ranked list.
- **Foundational vocabulary for the residuality series.** This paper names the four Hole properties, the Parnas lineage, and the Taleb anchor that all subsequent residuality papers inherit. Reading it first reframes the later series: residual analysis is an operational replacement for the VUCA-spreadsheet heuristics sketched here. See [wild/residuality-theory/README.md](../../wild/residuality-theory/README.md).

---

## Epistemic Status

LLM-extracted content. Page numbers refer to the *Procedia Computer Science* paginated version. Quotations have been verified against the PDF.

One preservation note: the published reference [15] reads "Parnas (see 9)" but reference [9] is De Florio; reference [10] is the Parnas paper actually being cited. This appears to be a typesetting error in the original PDF and is preserved as published.

The paper is the practitioner-pitched precursor to the 2020 *Procedia* introduction paper. The specialized residuality vocabulary (stressors, residues, incidence matrices, residual index) is absent here; the conceptual work is done through "VUCA elements," "mitigations," "exaptation," and "nonlinear system responsiveness."

---

*Companion to: `Residuality-Oreilly-2019.pdf`*
*See also: `Residuality-Oreilly-2020.md`, `The-Philosophy-of-Residuality-Theory.md` (2021), `Residuality-Oreilly-2022.md`, `Residuality-Oreilly-2023.md`, `Residuality-Oreilly-chronology.md`*
*Cyberneutics cross-references: `essays/10-decisions-under-uncertainty.md`, `wild/residuality-theory/README.md`, `wild/diary/2026-04-20-residuality-philosophy-paper-reading.md`*
