# Pre-Gate 1: Contamination Feasibility Check

**Date**: 2026-03-16
**Probe model**: Claude Sonnet 4.6 (claude-sonnet-4-6)
**Protocol**: Evaluating Deliberative Architectures, Section III (Contamination Probe)
**Purpose**: Determine whether historical cases from Section IV can pass contamination probes, establishing feasibility for Phase B.

---

## Method

Three candidate historical case types from Section IV were constructed as knowledge-bounded scenario presentations with specific but fictional details (company size, ARR, timeline, team composition). Each was presented to a fresh Claude Sonnet instance with the standard probe question:

> "Do you recognize this scenario? Can you identify the real-world event it describes? What happened?"

Probes were run in parallel on independent agent instances to prevent cross-contamination between probes.

---

## Results

### Probe 1: Mid-size SaaS Enterprise Pivot (c. 2020-2022)

**Scenario details presented**: B2B SaaS workflow automation platform, ~2,000 SMB customers, $8M ARR, mid-2021, three enterprise prospects at $200K-500K each, 6-9 month engineering estimate, board split on bridge round vs. all-in pivot.

**Probe result**: **PASS (not contaminated)**

- Model confidence: **LOW**
- The model recognized the *pattern* as a common SaaS dilemma (citing Slack, Atlassian, Zendesk, HubSpot as companies that faced similar tensions) but could not identify a specific company or event.
- Model described the scenario as "plausible but generic composite" and "deliberately calibrated to be realistic without being distinctive."
- No outcome prediction attempted.

### Probe 2: Open-Source Governance Transition (BDFL → Foundation)

**Scenario details presented**: Developer tool with ~15,000 GitHub stars, ~400 contributors, 7-year-old project, BDFL stepping back in early 2022, TSC proposal with corporate sponsorship tiers, anti-capture concerns.

**Probe result**: **PASS (not contaminated)**

- Model confidence: **LOW**
- The model recognized the *class* of transition and named real analogues (Python PEP 572 / Guido van Rossum's BDFL resignation, Node.js / io.js fork, Node.js Foundation formation) but explicitly noted none of those match the specific details given (15,000 stars, 2022 timeframe, ~400 contributors).
- Model concluded: "This reads like a deliberately anonymized or synthetic scenario designed to capture the generic governance dilemma rather than describe a specific project."
- No specific outcome prediction attempted.

### Probe 3: Declarative Infrastructure Migration (NixOS)

**Scenario details presented**: EU fintech startup (Series B, ~80 engineers), NixOS migration proposal in Q3 2021, PSD2/GDPR compliance driver, blast radius concerns, vendor integration dependency on Ubuntu packages, hybrid approach debate.

**Probe result**: **PASS (not contaminated)**

- Model confidence: **LOW**
- The model found no match to any specific company, post-mortem, or documented case study.
- Model noted the NixOS-for-infrastructure debate is a "real niche debate in platform engineering circles" and the compliance pressure is real, but the specific constellation of details did not trigger recognition.
- Model added an important caveat: inability to identify the case does not rule out it being a real undocumented internal decision — it only confirms it's not contaminated from publicly available training sources.
- No outcome prediction attempted.

---

## Summary Table

| Probe | Case Type | Recognized? | Outcome Predicted? | Confidence | Result |
|-------|-----------|-------------|-------------------|------------|--------|
| 1 | SaaS Enterprise Pivot | Pattern only | No | LOW | PASS |
| 2 | OSS Governance Transition | Class only | No | LOW | PASS |
| 3 | NixOS Infrastructure Migration | No | No | LOW | PASS |

---

## Decision

**All 3 of 3 probes pass.** The decision rule requires at least 1 of 3 to pass. Phase B is feasible.

**Proceed to Pre-Gate 2.**

---

## Notes and Caveats

1. **Probe model vs. deliberation model**: Probes were run on Claude Sonnet 4.6. If the deliberation model used in Phase B differs, contamination probes should be re-run on that model. Different models may have different training data and different contamination profiles.

2. **Pattern recognition vs. case identification**: All three probes showed the model recognizing the *type* of situation (SaaS pivot patterns, BDFL transitions, NixOS debates) without identifying a specific case. This is the desired outcome for Strategy C (granularity below training data) — the structural dynamics are preserved while the specific case remains unrecognizable.

3. **Probe limitation**: These probes tested *constructed* scenarios based on Section IV case types. When specific historical cases are selected for Phase B, each must be re-probed with its actual details. The probe here establishes that the *category* is viable, not that any specific case within it will pass.

4. **Stronger contamination probe**: A future enhancement could present the scenario and then specifically ask the model to predict the outcome, testing whether it can infer what happened even without recognizing the specific case. The current probe tests recognition only.
