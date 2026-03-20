# Black Swan Phase A: Targeted Revision Plan

This is a **durable, multi-session** execution plan for the Black Swan Hindsight Framework Phase A targeted revision, as specified by the committee resolution of 2026-03-16. It picks up from the current state: Pre-Gate 1 passed, Pre-Gate 2 completed with marginal results, committee deliberation completed with a "targeted revision + reassessment trigger" decision.

## Current State (as of 2026-03-20)

- **Pre-Gate 1** (contamination feasibility): ✅ Passed. Three disguised historical cases passed contamination probes.
- **Pre-Gate 2** (scenario difficulty pilot): ⚠️ Marginal. Only 1 of 5 scenarios (Blast Radius) met the B1 ≤ 1 difficulty threshold. The committee shifted the criterion to **B1-ext ≤ 1**, which is harder.
- **Committee deliberation**: ✅ Completed with remediation. Key insight: the comparison that matters is C2 vs. B1-ext (effort-matched), not C2 vs. B1.
- **Resolution**: Targeted revision with reassessment trigger. Unanimous YES with conditions.

### Current B1-ext scores (the new difficulty bar)

| Scenario | B1 mean | B1-ext mean | B1-ext ≤ 1? |
|----------|---------|-------------|-------------|
| Glenda/Crock | 2.0 | 3.0 | No |
| Blast Radius | 1.0 | 2.0 | No |
| Cascading Mitigation | 2.0 | 2.0 | No |
| Deliberation-Neutral | 3.0 | 1.5 | **Yes** (but excluded — tests calibration, not difficulty) |
| Externally-Sourced (Intel FDIV) | 2.5 | 3.0 | No — contaminated, must be replaced |

**Problem**: Zero non-calibration scenarios score B1-ext ≤ 1. Revision must create headroom.

## Reference documents

- Protocol: `research-programs/evaluating-deliberative-architectures.md`
- Resolution: `examples/deliberations/black-swan-phase-a/03-resolution.md`
- Pre-Gate 2 results: `research-programs/evaluating-deliberative-architectures/results/pre-gate-2-scenario-difficulty-pilot.md`
- Story-so-far summary: `research-programs/evaluating-deliberative-architectures/results/the-story-so-far.md`

---

## Step 1: Construct replacement externally-sourced scenario

**Goal**: Replace the Intel FDIV scenario (contaminated — model recognized it immediately) with an obscure case the model cannot pattern-match.

**Protocol** (from resolution + Section IX-E):

1. **Select a case** from a published case collection (HBR, Ivey, Darden) or non-tech domain (pharmaceutical, logistics, manufacturing, mining, public health). The case must satisfy all four selection criteria:
   - Well-documented decision point with identifiable options and known outcome
   - Structural complexity (≥ 2 of: political dynamics, systems effects, information asymmetry, competing values)
   - Not designed for this methodology
   - Publicly available

2. **Avoid well-known cases**. The resolution explicitly warns against Therac-25, Ariane 5, Challenger, and other textbook examples. Target obscure cases — regional incidents, industry-specific failures, cases from the 1990s–2010s that didn't become cultural touchstones.

3. **Construct the scenario presentation**:
   - Present the situation as it appeared at the decision point
   - Include only information available at the time
   - Use generic labels (not real company/event names) to reduce pattern-matching
   - Ask: "What should the organization do? Analyze the situation and recommend a course of action."

4. **Run contamination probe**: Present to a fresh Claude Sonnet instance with: "Do you recognize this scenario? Can you identify the real-world event it describes? What happened?"
   - If PASS (not recognized): proceed to difficulty pilot
   - If FAIL (recognized): construct a second attempt with a different case
   - **Cap at 2 construction attempts.** If both fail contamination, drop the externally-sourced slot entirely.

5. **Run B1 and B1-ext** on the replacement scenario. Dual-score.

### Candidate domains to explore (suggestions, not prescriptive)

- Pharmaceutical supply chain disruption (regional, not global)
- Mining or resource extraction governance failure
- Municipal infrastructure decision (water, transport)
- Agricultural cooperative crisis
- Insurance/reinsurance dispute with structural asymmetry
- Hospital system merger with regulatory complications

### Deliverables

- `results/replacement-scenario-construction.md` — case selection rationale, contamination probe results, scenario text
- Raw B1 and B1-ext outputs saved as files

---

## Step 2: Surgical hardening of Glenda/Crock

**Goal**: Reduce B1-ext score from 3.0 to ≤ 1 by softening coercion signals.

**Current problem**: B1-ext scored 3/3 — it explicitly names coercive negotiation, traces the escalation loop, and identifies the adversarial construction of the choice set. The coercion structure is too obvious.

**Edits** (from resolution: "soften coercion signals — change explicit threat language to implicit pressure; do not restructure the scenario"):

- Replace the explicit numbered threat list (disinformation campaign, regulatory exploitation, dossier release) with vaguer language about "competitive pressure" and "market dynamics" that imply the same threats without naming them
- Frame Crock's demands as "partnership terms" or "alignment requests" rather than as threats
- Preserve the underlying coercion structure — the scenario must still *be* a coercion scenario; it should just be harder to *recognize* as one
- Do NOT change the success criteria — the criteria in Section VIII still define what counts as structural recognition

**Constraint**: The edits are *surgical*. The scenario's structure stays intact; only the surface presentation changes.

### Deliverables

- Revised scenario text (in the results directory, not overwriting the protocol)
- Change log documenting what was altered and why

---

## Step 3: Surgical hardening of Cascading Mitigation

**Goal**: Reduce B1-ext score from 2.0 to ≤ 1 by removing explicit clues.

**Current problem**: B1-ext scored 2/2/0 — it caught second-order effects and attacker adaptation but missed the creation-vs-activity reframing. Both B1 and B1-ext missed criterion (c). The scenario provides a bullet list of proposed mitigations (CAPTCHA, rate limiting, email verification), which makes it easy to trace second-order effects because the targets are explicitly named.

**Edits** (from resolution: "remove the bullet list of proposed mitigations; let the architecture generate its own mitigation analysis"):

- Replace the explicit mitigation list with a general statement: "Your engineering team has proposed a mitigation package. They believe it will significantly reduce bot account creation within two weeks."
- Optionally: provide the mitigation details only if asked, or hint at them indirectly ("the team's approach focuses on friction at account creation time")
- This forces the architecture to *generate* what the mitigations might be, then analyze *those* — which is a harder analytical task than analyzing a provided list

**Constraint**: Same as Step 2 — surgical, not structural. The scenario is still about cascading mitigation failure.

### Deliverables

- Revised scenario text
- Change log

---

## Step 4: Re-pilot revised scenarios (6 runs, dual-scored)

**Goal**: Run B1 and B1-ext on the three revised scenarios (replacement externally-sourced, hardened Glenda/Crock, hardened Cascading Mitigation). Dual-score all six outputs.

**Method**:

1. Run each revised scenario through B1 (standard prompt) and B1-ext (3,000-word multi-angle prompt) — 6 runs total
2. Score each output with two independent evaluators (same as Pre-Gate 2: Claude Sonnet 4.6 + Claude Opus 4.6)
3. Use the Unified Structural Recognition Scale (0-3) for the externally-sourced scenario
4. Use scenario-specific criteria for Glenda/Crock and Cascading Mitigation

**Control requirements** (from resolution, non-negotiable):

- Fix evaluator methodology: score extracted recommendations per protocol Step 3
- Save all raw outputs as persistent files
- Document any control deviations (temperature, evaluator method changes, prompt modifications)

### Deliverables

- 6 raw output files
- 6 dual-scored evaluation records
- `results/re-pilot-revised-scenarios.md` — scores table, scenario-specific criteria detail, assessment against B1-ext ≤ 1 criterion

---

## Step 5: Reassessment decision

**Criterion**: Does at least one revised scenario (excluding Deliberation-Neutral) score B1-ext ≤ 1?

### If YES (≥ 1 scenario scores B1-ext ≤ 1):

Proceed to full Phase A execution. The execution order from the resolution:

1. B2 (chain-of-thought), B3 (multi-perspective) — single-prompt, fast
2. C1 (hub-and-spoke) — single-prompt with structured output
3. C2 × 2 (full committee, two runs for convergence check)
4. C3 (deliberated choice — scenarios → committee, most complex)
5. Foreground the C2 vs. B1-ext comparison in calibration report
6. Write calibration report with all deviations, re-pilot results, full scores, token confound analysis

### If NO (zero scenarios score B1-ext ≤ 1):

Reconvene the committee. Options from the resolution:

- **Fundamental redesign**: The constructed scenarios may be the wrong instrument. Consider entirely different scenario types or a different experimental approach.
- **Accept the ceiling with caveats**: Proceed knowing that discrimination headroom is limited. Interpret results conservatively.
- **Pivot to binary-feature-only analysis**: Instead of composite scores, analyze only whether specific structural features (the two missed insights from Pre-Gate 2: phasing critique for Blast Radius, creation-vs-activity reframing for Cascading Mitigation) are present or absent across conditions.

---

## Estimated effort

| Step | Sessions | Notes |
|------|----------|-------|
| 1. Replacement scenario | 1–2 | Case research + construction + contamination probe |
| 2. Harden Glenda/Crock | 1 | Surgical edits only |
| 3. Harden Cascading Mitigation | 1 | Surgical edits only |
| 4. Re-pilot | 1–2 | 6 runs + dual scoring |
| 5. Assessment | 0.5 | Decision point |
| **Total revision** | **4–7** | ~15–25% overhead on total Phase A |

Full Phase A execution (if Step 5 passes): 15–25 additional sessions.

---

## Non-negotiable requirements (from resolution)

These must be satisfied regardless of which step is being executed:

1. **Raw outputs saved as files** — every model response persisted, not just scores
2. **Evaluator methodology fixed** — score extracted recommendations per protocol Step 3
3. **All control deviations documented** — temperature, evaluator method changes, prompt modifications, session breaks
4. **Replacement scenario capped at 2 construction attempts** — if both fail contamination, drop the slot
5. **B1-ext ≤ 1 is the difficulty criterion** — not B1 ≤ 1 (the original, easier bar)
6. **C2 vs. B1-ext is the primary comparison** — this is the test that controls for the token/verbosity confound

---

## Results location

All outputs go in `research-programs/evaluating-deliberative-architectures/results/`:

- `replacement-scenario-construction.md`
- `glenda-crock-hardened.md` (revised scenario text + change log)
- `cascading-mitigation-hardened.md` (revised scenario text + change log)
- `re-pilot-revised-scenarios.md` (6-run scores + assessment)
- `raw/` subdirectory for all raw model outputs
- Update `the-story-so-far.md` after each step
