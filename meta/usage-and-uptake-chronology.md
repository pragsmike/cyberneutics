# Uptake and Usage: Chronology

Dated event log for external adoption signals and practitioner feedback.
The current state and brief trajectory are in [uptake-and-usage.md](uptake-and-usage.md).

---

## Event log

### 2026-02-01 — Self-evaluation: external validation as top gap

The committee self-evaluation (repository readiness review) identified
external validation as the #1 gap. This document and the main
[uptake-and-usage.md](uptake-and-usage.md) were created to track
evidence as it arrives.

**Predicted signals** (for later comparison):

| Predicted signal | Status as of last chronology update |
|---|---|
| External practitioners attempt to use the methodology | Two forks confirmed |
| Techniques are adopted by other platforms | MOOLLM integration confirmed |
| Different committee makeups tested for different domains | Fork #1 investigated Condorcet; tested CJT-style (independent vote) as alternative pipeline |
| Rubric scores from external deliberations available | Partial: Condorcet deliberation scored 13/15 (High) on internal review |
| Failure reports from practitioners | Not yet |
| Sustained multi-session use by external users | Not yet |
| Deliberation vs. aggregation compared empirically | Two comparison runs — same verdict on one question, opposite verdicts on another |

---

### 2026-02-19 — Repository fork: committee makeup extension

**Who**: External practitioner (details TBD)  
**What**: Forked the cyberneutics repository with the stated intent to use and extend the adversarial committee deliberation feature.

**Specific interest**: Experimenting with different committee makeups to compare results for different kinds of problems. This is exactly the extensibility the committee system was designed for — the character-propensity-reference and committee-setup-template documents support custom rosters, and the `/committee` skill can be invoked with different character configurations.

**What this validated**: The committee concept is comprehensible to someone outside the project; the extension they chose (different rosters for different domains) is architecturally sound — in palgebra terms, they're keeping the morphisms and changing the catalytic objects.

**What we don't know yet**: Whether they succeed in running deliberations, whether different makeups produce measurably different results, what friction they encounter.

---

### 2026-02-19 (on or before) — MOOLLM platform integration

**Who**: SimHacker / MOOLLM project  
**What**: Incorporated the adversarial committee mechanism into the MOOLLM platform.

**Context**: The `artifacts/integration-with-moollm.md` document maps Cyberneutics primitives to MOOLLM primitives (Characters → Cards, Committee Sessions → Rooms, Lessons → Files). This integration was anticipated in the architecture but not previously confirmed as implemented.

**What this validated**: The technique is portable; the MOOLLM mapping is workable in practice; the methodology can run on infrastructure that provides room isolation, persistent state, protocol enforcement.

**What we don't know yet**: How faithfully the committee mechanism was adapted; whether MOOLLM's infrastructure improves deliberation quality; whether MOOLLM users who haven't read the essays can use the committee feature effectively.

---

### 2026-02-20 — Fork update: Condorcet and mRNA

Contributor gave more detail on their direction.

*Condorcet theorem*: They intend to investigate the Condorcet jury theorem as a formal foundation for the committee technique. If the contributor formalizes this connection, it would strengthen the theoretical section of `artifacts/adversarial-committees.md` and add a new dimension to `essays/societies-of-thought-synthesis.md`.

*mRNA and the immune analogy*: They suggested considering mRNA as relevant to the immune system analogy — "narrative mRNA" as carefully designed fictional exemplars of misinformation patterns that train pattern recognition without contact with live attack vectors. Worth a committee deliberation on how to design such training material.

---

### 2026-02-20 — Repository fork: Deleuzian walks and Residuality Theory

**Who**: New external contributor (details TBD)  
**What**: Forked the repository and engaged with the Deleuze material (`essays/06-deleuze-difference-repetition.md`), specifically noting a connection between Deleuzian walks and Barry O'Reilly's Residuality Theory via the concept of Architectural walks.

**Why this is interesting**: The committee deliberation process is already implicitly a kind of architectural walk; the Condorcet connection speaks to *why* multiple walkers converge on better answers; the Residuality connection speaks to *what* they're looking for — the features of the problem space that survive reframing. There's also a potential connection to the palgebra formalism: the deliberation record (00–04 files) as residue.

**What this validated**: The Deleuze essay is accessible to external readers; the methodology is attracting contributors interested in theoretical depth; Residuality Theory is an adjacent conceptual framework worth tracking.

---

### 2026-02-22 — Condorcet investigation completed; PR merged

The contributor produced a substantial body of work that has been reviewed and merged:

- **Committee deliberation** (`meta/research-programs/condorcet-comparison/results/condorcet-jury-theorem-process/`): The committee recommended *documenting* the relationship to CJT, not changing the process. Review scored 13/15 (High). Key finding: the committee process deliberately violates CJT's conditions because it optimizes for adversarial stress-testing and decision-space mapping, not for maximizing the probability of a correct binary vote. A CJT-compliant variant would be a *different pipeline* — independent generation then aggregation — not a correction to this one.
- **Artifact created**: `artifacts/condorcet-jury-theorem-and-committee.md` — design goals first, CJT as motivating analogy, explicit deviations table, and the fork (CJT-compliant = different pipeline). Cross-linked from `artifacts/adversarial-committees.md`.
- **Comparison protocol**: `artifacts/comparison-protocol-deliberative-vs-cjt.md` — how to run both pipelines (deliberative and CJT-style independent vote) on the same question and compare.
- **Two comparison runs** (`meta/research-programs/condorcet-comparison/results/`):
  - *second-ci-job*: Both pipelines said Nay. CJT 4–1, Deliberative 5–0 (same verdict; one vote changed in deliberation, revisit condition added).
  - *code-of-conduct*: **Opposite verdicts.** CJT Aye 3–2, Deliberative Nay 5–0. Three characters (Frankie, Vic, Tammy) voted Aye in isolation but flipped to Nay after debate. The enforcement/weaponization objection was pressed in deliberation, and three votes changed.

**What this validated — first empirical evidence for deliberation over aggregation**: (1) Robert's Rules as forcing function works. (2) Adversarial back-and-forth is the value, not the number of perspectives. (3) The Condorcet artifact's own claim is supported: a CJT-compliant variant would sacrifice deliberation and stress-testing for independence and aggregability.

**What we still don't know**: Whether the deliberative verdict was *better*; whether the pattern generalizes; whether a CJT-style pipeline with more voters would converge toward the deliberative result.

**Significance**: This is the closest thing to a controlled experiment the methodology has produced. The comparison protocol is reusable for future runs.

---

### 2026-02-23 — Repository stars

**What**: The git repository had two stars on the hosting platform (e.g. GitHub).

**Note**: A lightweight adoption signal; indicates at least two accounts have bookmarked or endorsed the repo. No direct feedback or usage data implied.

---

## Feedback log (chronological)

*(Record practitioner feedback here as it arrives — date, source, verbatim if possible, brief analysis.)*

No feedback received yet beyond the adoption events above.

---

**Chronology last updated**: February 24, 2026
