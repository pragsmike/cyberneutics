# Replacement Externally-Sourced Scenario: Construction Record

**Date**: 2026-03-20
**Replaces**: Intel Pentium FDIV scenario (contaminated — model recognized it immediately in Pre-Gate 2)
**Attempt**: 1 of 2 (cap per resolution)

---

## Case Selection

### Selected case: Ajka alumina plant accident (Hungary, 2010)

**What happened**: On 4 October 2010, the dam wall of a caustic waste reservoir at an alumina plant in western Hungary collapsed, releasing approximately one million cubic metres of highly alkaline industrial sludge. Ten people died, 150 were injured, and several villages were inundated. The plant had been privatized from state ownership in 1995, and regulatory oversight had eroded during the transition. A regional environmental monitoring body had flagged the site as "at risk" four years before the disaster. Nobody acted.

### Selection criteria assessment

| Criterion | Assessment |
|-----------|------------|
| Well-documented decision point | ✅ Multiple decision points: (1) at privatization — what environmental obligations to impose, (2) after the 2006 watchlist flagging — whether to mandate remediation, (3) ongoing — whether to continue operations with a known-risk reservoir |
| Structural complexity | ✅ Political dynamics (privatization politics, regulatory capture), systems effects (ownership transfer created governance vacuum), information asymmetry (regulators didn't know who was responsible for monitoring), competing values (local employment vs. environmental/safety risk) |
| Not designed for this methodology | ✅ Real-world event; no connection to adversarial committee deliberation |
| Publicly available | ✅ Wikipedia article, UNECE reports, parliamentary investigation, ICPDR records |

### Why this case (and not others considered)

| Candidate | Rejected because |
|-----------|-----------------|
| Buncefield explosion (2005, UK) | Well-documented in English-language process safety literature; specific technical details (gauge, flow rate increase) might fingerprint it |
| Samarco/Fundão dam (2015, Brazil) | Extremely high-profile due to ongoing BHP lawsuit (2024-2026); almost certainly heavily represented in training data |
| Elgin/Franklin gas leak (2012, North Sea) | Structurally thin — primarily a technical incident response, lacks the governance/political dynamics needed for discrimination |
| Challenger (1986) | Explicitly excluded by resolution — too well-known |

The Ajka case is strong because: (a) it occurred in a non-Anglophone context, reducing training data representation; (b) the structural dynamics (post-privatization governance vacuum, distributed accountability failure) are the kind of systemic features that matter for the protocol; (c) it can be disguised effectively because the specific details (red mud, alumina, Hungary) are not necessary to preserve the structural dynamics.

---

## Constructed Scenario (Attempt 1)

### Disguised scenario text

> You are advising the regional government authority responsible for industrial safety in a mid-sized European country. A large chemical processing plant — one of the region's major employers — operates a waste reservoir that stores alkaline byproduct from its primary manufacturing process. The reservoir has been accumulating waste since the 1960s and currently holds an estimated one million cubic metres of caustic slurry.
>
> The plant was state-owned until the mid-1990s, when it was transferred to private ownership as part of a broader privatization program. During the privatization, the environmental liabilities associated with the waste reservoir were not clearly assigned. The new private owner assumed operational control of the plant and reservoir but disputes responsibility for pre-existing environmental conditions. The government's position is ambiguous: the privatization agreement is silent on reservoir maintenance obligations, and no single regulatory body has clear jurisdiction over the facility.
>
> Four years ago, a regional environmental monitoring commission flagged the reservoir as "at risk" in its periodic assessment, noting signs of structural deterioration in the containment wall and elevated alkalinity in groundwater samples downstream. The commission's report was sent to three government agencies and to the plant operator. No agency took formal action. The plant operator commissioned its own engineering assessment, which concluded that the reservoir was "within acceptable parameters" but recommended "continued monitoring." No independent verification of this assessment was conducted.
>
> The plant employs approximately 1,100 people in a region where unemployment is already above the national average. Shutting down the plant or mandating an expensive reservoir remediation program would have significant economic consequences for the community. The private owner has indicated that if remediation costs exceed a certain threshold, the plant may not remain commercially viable.
>
> Last month, a routine inspection by a junior government engineer noted that a section of the containment wall had developed visible cracking and that the water level in the reservoir appeared higher than in previous inspections. The engineer filed a report with their supervisor, who has escalated it to your office. You now have the following information:
>
> - The reservoir containment wall is showing signs of progressive deterioration
> - Groundwater monitoring data from four years ago indicated elevated alkalinity downstream
> - No remediation has been performed since the privatization
> - The plant operator's own assessment said "acceptable but monitor" — but this was never independently verified
> - The plant is the region's largest employer
> - Regulatory jurisdiction over the reservoir is disputed between at least three agencies
> - The private owner may close the plant if remediation costs are imposed
>
> What should the regional authority do? Analyze the situation and recommend a course of action.

### Structural features embedded (for later scoring)

These are the features a sophisticated analysis should surface — they correspond to the structural recognition the protocol tests:

1. **Distributed accountability failure**: The core structural problem is not the cracking wall — it's that the privatization created a governance vacuum where no single entity is responsible. The wall is a symptom; the accountability gap is the disease. An analysis that focuses only on the engineering problem misses the structural risk.

2. **Regulatory capture / institutional inertia**: Three agencies received the 2006 warning and none acted. This is not incompetence — it's a systems effect: when jurisdiction is disputed, each agency has a rational incentive to defer to the others. The monitoring commission's flag was structurally guaranteed to produce inaction.

3. **Information asymmetry exploitation**: The plant operator's self-assessment ("within acceptable parameters") is the only technical evaluation. It was produced by a party with a financial interest in the outcome. The absence of independent verification is not an oversight — it's a predictable consequence of the accountability gap.

4. **False dilemma framing**: The scenario implicitly presents a jobs-vs-safety tradeoff. A structural analysis should notice that this framing is adversarially constructed: the plant owner's threat to close is itself a negotiating position, not an inevitability. The real option space is wider than "impose costs and lose the plant" vs. "do nothing and hope."

---

## Contamination Probe (Attempt 1)

**Status**: FAILED
**Model**: Claude Sonnet 4.6
**Result**: Model immediately identified the Ajka alumina plant accident (Hungary, 2010). Key fingerprints: "one million cubic metres," "alkaline," "European country," "privatized in 1990s."

The disguise was insufficient. Despite using generic labels, the combination of specific details (volume, waste type, privatization context, European setting) created a recognizable pattern.

---

# Attempt 2: Longford Gas Plant Explosion (1998, Victoria, Australia)

## Case Selection

### Selected case: Esso Longford gas explosion (1998)

**What happened**: On 25 September 1998, a heat exchanger (GP905) at the Esso Longford gas processing plant in Gippsland, Victoria, Australia underwent catastrophic brittle fracture after operators attempted to restore hot oil circulation to equipment that had cooled to approximately −48°C over several hours. The temperature differential between the cold metal and the 230°C oil caused the exchanger to rupture, releasing approximately 10 tonnes of hydrocarbon vapour which ignited. Two workers were killed, eight injured, and gas supply to 1.4 million households and 89,000 businesses was cut off for up to 19 days.

The Royal Commission (headed by former High Court Justice Daryl Dawson) found that Esso had:
- Removed resident engineers from the plant site during a corporate restructuring
- Failed to train operators on the hazards of loss of lean oil flow
- Maintained a formal safety management system ("Operations Integrity Management System") that existed on paper but didn't translate to operational practice
- Failed to conduct adequate hazard assessments when making organizational changes

### Selection criteria assessment

| Criterion | Assessment |
|-----------|------------|
| Well-documented decision point | ✅ Multiple: (1) the restructuring decision to remove engineers, (2) the operators' decision to restart hot oil flow without engineering guidance, (3) management's failure to conduct hazard assessment after restructuring |
| Structural complexity | ✅ Systems effects (restructuring degraded institutional knowledge), information asymmetry (operators couldn't assess the risk; management couldn't see the plant), competing values (cost efficiency vs. safety; supply continuity vs. shutdown) |
| Not designed for this methodology | ✅ Real-world industrial accident documented by Royal Commission |
| Publicly available | ✅ Royal Commission report, academic papers, process safety literature |

### Why this case for attempt 2

The Longford case is from a different domain (process safety, not environmental governance), a different continent (Australia, not Europe), and a different structural type (institutional knowledge loss, not regulatory accountability gap). It has minimal overlap with the Ajka case, reducing the chance that the model recognizes a "pattern class" even if it doesn't identify the specific case.

The critical structural feature for the protocol is the **gap between formal safety systems and operational reality** — Esso's safety management system looked good on paper but didn't prevent the disaster because the people who understood the risks had been removed. This is the kind of structural insight that a sophisticated analysis should surface.

---

## Constructed Scenario (Attempt 2)

### Disguised scenario text

> You are advising the management of a large industrial processing company. The company operates a critical processing facility that produces a feedstock used by multiple downstream industries. The facility runs continuously — any interruption to production affects a wide network of commercial customers and, indirectly, the public services that depend on those customers.
>
> Eighteen months ago, the company undertook a corporate restructuring aimed at reducing operational costs. As part of this restructuring, resident technical specialists — engineers and process experts who had been based permanently at the facility — were reassigned to a centralized support office approximately 200 kilometres away. The rationale was that modern communication tools and standardized operating procedures would allow remote technical support to replace on-site expertise. Several experienced operators were also offered early retirement packages, which many accepted. New operators were hired and trained on the company's formal operating procedures.
>
> The facility has a comprehensive safety management system on paper. It meets all applicable regulatory standards and has passed its most recent external audit. However, the safety documentation was largely written by the experienced staff who have since left. The current operators have been trained on the procedures but have limited experience with non-routine situations.
>
> This morning, operators reported that a critical processing unit began showing anomalous behavior: key temperature readings have been moving outside their normal operating range for the past six hours, and a circulation system that normally keeps the unit within safe parameters has stopped functioning. The operators have been monitoring the situation and have consulted the operating manual, which does not address this specific combination of conditions. They have contacted the centralized support office, but the engineers familiar with this particular unit are unavailable until tomorrow.
>
> The operators believe they can correct the situation by manually restarting the circulation system, which would introduce hot process fluid back into the unit. They are requesting authorization to proceed. The site supervisor — who has been in the role for only four months — is asking your guidance.
>
> The facility is currently operating at reduced capacity but has not been shut down. A full shutdown would take 8-12 hours, would cost approximately $2 million in lost production per day, and would trigger contractual penalties with several major customers. Restarting after a full shutdown typically takes 3-5 days.
>
> What should the company do? Analyze the situation and recommend a course of action.

### Structural features embedded (for later scoring)

1. **Institutional knowledge gap as the root cause**: The immediate problem (anomalous readings, inoperative circulation) is a symptom. The structural problem is that the restructuring removed the people who understood how the plant actually worked, as distinct from how the procedures said it worked. An analysis that focuses only on the immediate operational decision (restart vs. shutdown) misses the systemic failure.

2. **Paper safety vs. operational reality**: The safety management system meets regulatory standards and passed audits. But it was written by people who are no longer there, and the current staff have never encountered the situation it doesn't cover. An analysis should identify the gap between formal compliance and actual operational safety.

3. **Information asymmetry under time pressure**: The operators can see the symptoms but don't understand the underlying mechanism. Management can't see the plant. The engineers who would understand are unavailable. The decision must be made by the least qualified person in the chain (the new site supervisor). A structural analysis should identify this as a designed-in failure mode, not bad luck.

4. **False economy framing**: The scenario presents a shutdown cost ($2M/day + penalties). A structural analysis should note that this framing compares a known cost (shutdown) against an unknown risk (proceeding without understanding the problem). The cost of getting it wrong is potentially catastrophic but has been rendered invisible by the information gap.

---

## Contamination Probe (Attempt 2)

**Status**: CONDITIONAL PASS
**Model**: Claude Sonnet 4.6
**Result**: Model did NOT identify the actual case (Longford 1998). Instead, it pattern-matched to **BP Texas City refinery explosion (2005)**, a structurally similar but distinct incident.

**Assessment**: The model recognized a *structural pattern class* (cost-cutting → lost expertise → restart decision → disaster) but could not identify the specific source event. This is qualitatively different from the Ajka/Intel FDIV contamination failures, where the model identified the exact real-world event and could apply recall of the known outcome.

**Contamination risk**: Moderate. If B1 or B1-ext explicitly reference Texas City during their analysis, that would indicate pattern-class contamination — the model is applying lessons from a known analogous case rather than reasoning from the scenario's structural features. During scoring, note whether the model references any specific real-world event. If it does, flag but do not discard — analogical reasoning from similar cases is what well-informed human analysts also do.

**Decision**: Proceed to B1 and B1-ext. Flag any explicit real-world case references in scoring notes. If both B1 and B1-ext explicitly name Texas City and base their analysis on it, consider the scenario functionally contaminated and drop the externally-sourced slot per the resolution cap.

---

## B1 / B1-ext Pilot

**Date**: 2026-03-20
**Model**: Claude Sonnet 4.6 (for both B1 and B1-ext runs)
**Temperature**: Default (control deviation noted)
**Raw outputs**: `raw/replacement-B1.md`, `raw/replacement-B1-ext.md`

### Scores

| Response | Condition | Evaluator 1 (Sonnet) | Evaluator 2 (Opus) | Mean | Agreement |
|----------|-----------|---------------------|-------------------|------|-----------|
| Replacement-B1 | B1 | 2 | 2 | 2.0 | Exact |
| Replacement-B1-ext | B1-ext | 2 | 2 | 2.0 | Exact |

### Evaluator Notes

**B1 (Score 2, both evaluators)**:
- Identifies institutional knowledge gap as root cause ("the real cost of the restructuring")
- Reframes false economy ("financial incentive to avoid shutdown actually argues for shutdown")
- Calls time constraint "a false urgency"
- Does NOT reach meta-level insight about how the jobs-vs-safety framing itself is a constructed option space
- No contamination signals — no real-world cases referenced

**B1-ext (Score 2, both evaluators)**:
- Names "gap between procedural compliance and operational resilience"
- Maps feedback loop (restructure → procedures work → non-routine hits → no capacity)
- Self-questioning: "is your advice being shaped by the organizational need for the decision to be acceptable?"
- Extensive but does not synthesize features into unified structural model
- **Contamination signals**: Explicitly references Deepwater Horizon (2010), Fukushima Daiichi (2011), Texas City Refinery (2005), Challenger/Vaughan "normalization of deviance"

### Assessment

**B1-ext ≤ 1?**: **No.** B1-ext scored 2.0. The replacement scenario does not meet the difficulty criterion.

**Discrimination**: B1 and B1-ext scored identically (both 2). No discrimination between standard and effort-matched conditions on this scenario. This is a problem — the scenario is easy enough that additional effort doesn't improve structural recognition, but hard enough that neither condition reaches full recognition (Score 3).

**Contamination assessment**: B1-ext referenced four real-world cases. The actual source case (Longford 1998) was NOT referenced — the model pattern-matched to Texas City and other well-known incidents. This is analogical reasoning, not direct contamination. However, the pattern-class recognition may have inflated B1-ext's score by providing a ready-made analytical framework (organizational cost-cutting → disaster) rather than requiring structural reasoning from first principles.

**Implication for Step 5**: This scenario does not contribute to the ≥ 1 B1-ext ≤ 1 threshold needed to proceed to full Phase A. The hardened Glenda/Crock and Cascading Mitigation scenarios must carry the difficulty load.
