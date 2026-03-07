---
resolution:
  date: 2026-02-21
  topic: "Testing the deliberated-choice workflow"
  outcome: PASSED
  decision: "Run single end-to-end test with three-tier staged verification on a genuine strategic question about the project's direction."
  summary: >
    The committee resolved to test the deliberated-choice workflow by running
    the full fan→funnel pipeline on "The cyberneutics methodology currently has
    no external adoption. What happens to the project over the next 12 months
    under different strategic choices?" This problem is strategic, concrete,
    genuinely uncertain, and relevant without being self-referential. The test
    applies three-tier verification (structural, process, quality) at each
    pipeline stage with findings classified as PASS/DEVIATION/FAIL. The
    composition seam (charter bridging) receives extra scrutiny for information
    loss. A post-run assessment compares the scenario-aware output against
    existing standard deliberations for format and substance differences.
  implementation_plan:
    - action: "Run /scenarios"
      description: >
        Generate scenarios for "cyberneutics methodology adoption strategy
        over 12 months." Verify Tier 1 (directory structure, file presence,
        YAML schemas), Tier 2 (assumption counts, early warning signs, coverage
        assessment), and Tier 3 (scenario distinctness, specificity, surprise).
    - action: "Run /committee with scenario_context"
      description: >
        Run committee deliberation on "Given these futures, what strategic
        direction should cyberneutics pursue?" with scenario_context pointing
        to the scenarios output. Verify Tier 1 (charter bridge fields,
        deliberation structure), Tier 2 (scenario reference counts, scenario-
        aware resolution sections), and Tier 3 (genuine engagement vs. name-
        dropping, cross-scenario reasoning, charter bridge fidelity).
    - action: "Write post-run assessment"
      description: >
        Document all findings as PASS/DEVIATION/FAIL per tier. Compare the
        scenario-aware resolution format against is-author-crackpot/03-resolution.md.
        Record reflexive value: did the pipeline surface anything genuinely new
        about the project's strategic direction?
  votes:
    - member: Maya
      vote: "YES — provided the charter bridge gets explicit scrutiny for information loss"
    - member: Frankie
      vote: "YES — with reflexive value check included as a Tier 3 item"
    - member: Joe
      vote: "YES — first run is mechanical validation; quality testing needs more runs"
    - member: Vic
      vote: "YES — with three-outcome classification and stage-gated verification"
    - member: Tammy
      vote: "YES — with diagnostic isolation: per-stage failure attribution"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: Testing the Deliberated-Choice Workflow

## Decision

Run a single end-to-end test of the deliberated-choice workflow using the problem: **"The cyberneutics methodology currently has no external adoption. What happens to the project over the next 12 months under different strategic choices?"**

## Test Plan

### Test Problem

The cyberneutics methodology is documented but has zero external uptake. Key uncertainties: whether depth (more essays), breadth (new domain applications), or accessibility (onboarding guides) would drive adoption. Natural divergence axes map to the 4-core scenario roster without extensions needed. Concrete enough for specific scenarios; uncertain enough that the outcome isn't obvious.

### Verification Tiers

**Tier 1 — Structural Integrity** (binary pass/fail):

| Stage | Check | Criterion |
|-------|-------|-----------|
| Scenarios | Directory created | `agent/scenarios/<slug>/` exists with 5 files |
| Scenarios | YAML schemas | Front matter matches SKILL.md spec |
| Scenarios | File count | 4 scenarios in 02-scenarios.md (one per core character) |
| Committee | Directory created | `agent/deliberations/<slug>/` exists with standard files |
| Committee | Charter bridge | 00-charter.md contains `scenario_context` and `scenarios_summary` |
| Committee | Summary fidelity | `scenarios_summary` entries match scenario set (narrators, titles) |

**Tier 2 — Process Compliance** (countable):

| Stage | Check | Criterion |
|-------|-------|-----------|
| Scenarios | Assumptions | ≥2 explicit assumptions per scenario |
| Scenarios | Early warnings | ≥2 early warning signs per scenario |
| Scenarios | Coverage | 03-assessment.md identifies divergence axes and quadrant coverage |
| Committee | Scenario refs | Each member's opening statement names ≥2 scenarios |
| Committee | Resolution format | Contains: robust actions, scenario-dependent actions, monitoring plan, dismissed futures |

**Tier 3 — Quality Judgment** (qualitative review):

| Stage | Check | Criterion |
|-------|-------|-----------|
| Scenarios | Distinctness | Scenarios differ on at least one divergence axis (not same narrative relabeled) |
| Scenarios | Specificity | Scenarios contain concrete events, not vague trends |
| Committee | Engagement | Committee reasons *about* scenarios, not just *names* them |
| Committee | Cross-scenario debate | Debate ranges across futures, not collapsing to single framing |
| Committee | Bridge fidelity | Charter summary preserves material information from full scenarios |
| Composed | Format difference | Resolution structurally differs from standard (is-author-crackpot) resolution |
| Composed | Reflexive value | Pipeline surfaces at least one genuinely new insight about strategic direction |

### Finding Classification

- **PASS**: Output matches spec and quality is adequate
- **DEVIATION**: Output doesn't match spec but content is sound — spec needs calibration
- **FAIL**: Output is malformed, missing, or vacuous

### Execution Order

1. Run `/scenarios` → verify Gates 1a–1c → proceed if no FAILs
2. Run `/committee scenario_context:` → verify Gates 2a–2c → proceed if no FAILs
3. Write post-run assessment with per-tier findings and format comparison

### Success Criteria for First Run

- **Mechanical success**: Zero FAILs across Tier 1 and Tier 2. DEVIATIONs acceptable (record for spec calibration).
- **Quality bonus**: At least 3 of 7 Tier 3 items rated PASS.
- **Overall**: The pipeline demonstrably composes — scenarios feed into committee, committee produces scenario-aware output.
