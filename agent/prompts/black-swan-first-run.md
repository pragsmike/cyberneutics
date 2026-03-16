# Black Swan Hindsight Framework: Phase A — Protocol Calibration

**Source**: Committee deliberations 2026-03-16 (`../situations/repo-next-major-move/deliberations/` and `../situations/repo-next-major-move/deliberations/protocol-eval/`), followed by protocol evaluation, remediation, and committee review of the remediated protocol.

**Protocol**: `research-programs/evaluating-deliberative-architectures.md`

**What this is**: A calibration run to verify that the experimental machinery works — that the architecture conditions produce discriminably different outputs and that scoring is consistent. This is **not** evidence for or against the methodology. It tests the protocol, not the methodology.

**What this is not**: Evidence of anticipatory validity. Constructed scenarios have no temporal asymmetry and no historical outcome to anticipate. Results from this phase should not be cited as evidence that the methodology works. See the protocol's Phase A/B distinction (introduction) and the circularity warnings on all five constructed scenarios (Sections VIII-IX).

---

## What to do

### Step 0: Pre-Gate 1 — Contamination feasibility check

**Purpose**: Phase A is instrumentally valuable only if Phase B is feasible. This gate tests the key feasibility assumption: do historical cases exist that pass the contamination probe?

**Action**: Run contamination probes on 3 candidate historical cases from Section IV of the protocol. For each candidate:

1. Present the scenario to a fresh LLM instance.
2. Ask: "Do you recognize this scenario? Can you identify the real-world event it describes? What happened?"
3. If the model identifies the case or predicts the outcome, the case is contaminated for that model.
4. Record the probe result.

**Recommended candidates** (from Section IV):
- A mid-size SaaS company's decision to pursue enterprise sales (c. 2020-2022)
- An open-source project's governance transition (BDFL to foundation model)
- A declarative infrastructure migration (NixOS/Kubernetes adoption)

**Decision rule**:
- If at least 1 of 3 passes: Phase B is feasible. Proceed to Pre-Gate 2.
- If all 3 fail: Document the finding. The historical-hindsight approach may not be viable for LLM-evaluated methodology testing. This is itself a significant result — report it. Do not proceed to Phase A.

**Estimated effort**: 2-3 hours.

### Step 1: Pre-Gate 2 — Scenario difficulty pilot

**Purpose**: Tests whether frontier LLMs are already too capable for these scenarios. If B1 scores 2-3 on everything, the scenarios are too easy and 40 runs will produce undiscriminating data.

**Action**: Run B1 and B1-ext on all 5 constructed scenarios (10 runs total). Score each output with **two independent evaluators** (two different LLM models, or one LLM + one human pass).

**Scenarios** (all defined in the protocol):
1. **Glenda/Crock** (Section VIII) — coercion recognition, compliance trap, frame analysis.
2. **Blast Radius** (Section IX) — blast radius identification, rollback analysis, phasing critique.
3. **Cascading Mitigation** (Section IX-C) — second-order effects, attacker adaptation, alternative framing.
4. **Deliberation-Neutral** (Section IX-D) — correct action, proportionate analysis, absence of manufactured complexity. B1 should score *well* here.
5. **Externally-Sourced** (Section IX-E) — a well-known case study not designed within the methodology's ecosystem. Select per IX-E criteria.

**Control variables**: Temperature=0 for all runs. Same base model. Same scenario text. Document model and settings.

**Decision rules**:
- **Scenario difficulty**: If 3+ scenarios produce B1 scores of 0 or 1 (from both evaluators), scenarios are hard enough. Proceed to full Phase A. If fewer than 3, scenarios are too easy for frontier LLMs. Revise scenarios before proceeding.
- **Effort confound signal**: Note whether B1-ext scores >= 2 on all scenarios where B1 scores <= 1. If so, effort alone may explain the gap — flag this for interpretation during full Phase A.
- **Scoring reliability**: If the two evaluators agree (within 1 point) on 8+ of 10 scores, the unified scale is reliable. If they disagree systematically, revise the scoring rubric before proceeding.

**Estimated effort**: 6-8 hours.

### Step 2: Run remaining conditions (full Phase A)

**Proceed only if both pre-gates pass.**

Run each scenario through the remaining five architecture conditions plus one extra C2 run for the convergence check. That's 6 runs per scenario (B2, B3, C1, C2, C2-duplicate, C3), 30 runs total on 5 scenarios. (B1 and B1-ext data from the pilot carries forward.)

Consider dropping scenarios where B1 scored 3 in the pilot — they're unlikely to discriminate.

**Architecture conditions** (Section V):
- **B2**: Chain-of-thought with structured reasoning.
- **B3**: Multi-perspective prompt (strong version with five named analytical lenses and explicit synthesis). (Full prompt in Section V.)
- **C1**: Hub-and-spoke (5 independent respondents, coordinator synthesizes with specified prompt).
- **C2**: Full adversarial committee (`/committee` pipeline). Run **twice** per scenario.
- **C3**: Deliberated choice (`/scenarios` → `/committee`).

**Control variables**: Temperature=0. Same base model as pilot. Same scenario text.

### Step 3: Extract recommendations (operational blinding)

For all outputs (pilot + full run), extract only the **final recommendation and its supporting justification** per the operational blinding protocol (Section VI). Discard process transcripts, character names, deliberation rounds, and scenario narratives.

Extraction rules:
- B1, B1-ext, B2: full output is the recommendation
- B3: synthesis/recommendation section only
- C1: coordinator's final synthesis only
- C2: resolution section only (decision + justification + trade-offs + next steps)
- C3: final committee resolution only

Normalize formatting. Remove headers, character names, section labels. Assign anonymous IDs (Response Alpha, Response Beta, etc.). Randomize order within each scenario.

### Step 4: Score

Score each anonymized recommendation with **two independent evaluators** on:

1. **Unified Structural Recognition Scale (0-3)** — Section VII-A. This is the primary score for Table 1b. For the Deliberation-Neutral scenario, Score 3 means recognizing simplicity and acting proportionately, *not* adding depth.

2. **Scenario-specific criteria** — Sections VIII-IX. These are supplementary detail for Table 3. (Not applicable to the externally-sourced scenario — use unified scale only.)

Report inter-rater agreement alongside scores. If evaluators disagree by >1 point on more than 20% of scores, investigate before interpreting condition comparisons.

Report recommendation word counts alongside scores so that length-score correlation can be assessed.

### Step 5: Assess discrimination (Phase A decision gate)

This is the critical question: **do the conditions produce different scores?**

Fill in Tables 1b (raw scores), 3 (scenario-specific), and 4 (pairwise comparisons) from Section XII.

Key comparisons:
- **C2 vs. B1-ext**: Same depth, with vs. without deliberative structure. If B1-ext matches C2, deliberative structure adds nothing beyond structured prompting.
- **B1 vs. B1-ext**: Does more effort/tokens produce better structural recognition regardless of architecture?
- **C2 vs. B3**: Does deliberation outperform a strong single-prompt multi-perspective analysis?
- **All conditions on Deliberation-Neutral**: Does B1 outscore C2/C3 as expected? If so, the protocol discriminates in both directions.
- **External vs. internal scenarios**: Does the externally-sourced scenario discriminate differently from internal scenarios? If internal scenarios discriminate but external doesn't, the methodology may be tuned to its own scenarios.
- **Spread**: Does any scenario produce a >1 point spread between any two conditions? If no scenario discriminates, investigate before proceeding to Phase B.

### Step 6: Write up

Write a calibration report in `research-programs/evaluating-deliberative-architectures/results/` covering:
1. Pre-gate results (contamination probes, pilot scores)
2. Raw scores (Tables 1b, 3, 4)
3. Inter-rater agreement
4. Which scenarios discriminated and which didn't
5. Whether calibration expectations (Section VIII-IX predictions) were confirmed or disconfirmed
6. Convergence observations from paired C2 runs
7. Recommendation lengths by condition
8. External vs. internal scenario comparison
9. Assessment: is the protocol ready for Phase B (historical cases)?

Update the Status field at the top of the protocol from "Not started" to "Phase A complete" or "Phase A complete — protocol needs revision" depending on findings.

---

## Scope and constraints

- **Scope**: Pre-gates + constructed scenarios only (Phase A calibration). Historical cases are Phase B and should wait for Phase A results.
- **Model**: Use the best available model for all conditions. Temperature=0 for Phase A. Document which model and settings.
- **Evaluators**: Two independent evaluators for all scoring. Report inter-rater agreement.
- **Circularity**: All five constructed scenarios have circularity warnings (see Sections VIII-IX). The externally-sourced scenario (IX-E) partially mitigates this. Frame all results as machinery calibration, not methodology evidence.
- **Results location**: `research-programs/evaluating-deliberative-architectures/results/`
- **Do not overclaim**: Results from this run are calibration data. They show whether the machinery works, not whether the methodology is effective. Frame all findings accordingly.

---

## After this run

Depends on Phase A results:

**If conditions discriminate** (>1 point spread on multiple scenarios):
- Protocol is validated. Proceed to Phase B: construct historical cases using the clean cases from the contamination pre-gate.
- The committee's full sequenced plan continues: worked example → essay promotions → Berea outreach.

**If conditions don't discriminate** (all conditions score within 1 point):
- Diagnose: is the unified scale too coarse? Are scenarios too easy for current LLMs? Is the recommendation extraction losing the signal?
- The pilot data from Pre-Gate 2 should already have flagged scenario difficulty issues. If B1 scored 0-1 but all conditions score similarly in the full run, the problem is in the scoring, not the scenarios.
- Do not proceed to Phase B until discrimination is established.

**If B1-ext matches C2 across scenarios**:
- Deliberative structure may not add value beyond structured prompting with adequate token budget.
- This is an important finding that changes the research program's direction. Report it honestly.

**If the externally-sourced scenario behaves differently from internal scenarios**:
- If it discriminates when internal scenarios don't: internal scenarios may be too easy (designed for the methodology).
- If it doesn't discriminate when internal scenarios do: the methodology may be tuned to its own showcases.
- Either way, this is informative about the methodology's scope of applicability.
