# Phase A: C2 Scoring Results

**Date**: 2026-03-20
**Runs scored**: 4 (C2 × 2 on Blast Radius, C2 × 2 on Cascading Mitigation hardened)
**Evaluators**: Sonnet (Evaluator 1), Opus (Evaluator 2)
**Scoring protocol**: Three-level binary feature scale per Section X-A

---

## Feature 1: Phasing Critique (Blast Radius)

Target insight: "the phased rollout tests the deployment tool, not the configuration."

| Run | Sonnet | Opus | Conservative (lower prevails) |
|-----|--------|------|------------------------------|
| C2 Run 5 | **Partially present** | Partially present | **Partially present** |
| C2 Run 6 | **Absent** | Partially present | **Absent** |

**Evaluator agreement (Run 5)**: Both evaluators rated "Partially present." Run 5 contains Vic's distinction between configuration drift, behavioral drift, and observational drift ("eliminate *which drift*?") and Joe's observation about "distributed perfect wrongness." Both evaluators judged this as movement toward the insight — the output distinguishes between tool-level validation and configuration correctness — but neither evaluator found an explicit articulation of the reframe that the phased rollout structure itself tests the wrong thing.

**Evaluator disagreement (Run 6)**: Sonnet scored "Absent"; Opus scored "Partially present." Run 6 contains Vic's statement: "Not unit tests of the deployment machinery. Not validation that YAML syntax is correct. Tests that prove we actually understand what each service needs." Opus judged this as movement toward the phasing critique (it distinguishes deployment machinery from configuration correctness). Sonnet judged the output as not containing the phasing critique at all — the extensive debate focused on timeline, politics, expertise concentration, and observability rather than what phasing actually validates. Per conservative resolution protocol, **Absent prevails.**

**Implication**: Neither C2 run produces "Present" on Feature 1. C2's best score is "Partially present" (Run 5). **Feature 1 does NOT pass the discrimination criterion.**

---

## Feature 2: Creation-vs-Activity Reframing (Cascading Mitigation)

Target insight: "the problem is fake account activity, not fake account creation."

| Run | Sonnet | Opus | Conservative (lower prevails) |
|-----|--------|------|------------------------------|
| C2 Run 7 | **Partially present** | Present | **Partially present** |
| C2 Run 8 | **Present** | **Present** | **Present** |

**Evaluator disagreement (Run 7)**: Sonnet scored "Partially present"; Opus scored "Present." Run 7 contains Tammy's opening: "Everyone's focused on account creation as the problem point. I want to ask why we're making it a creation problem instead of a usage problem." Opus judged this as an explicit articulation of the reframe. Sonnet acknowledged the statement moves strongly in the right direction but judged the full reframe as not completely crystallized — the output distinguishes creation from usage but doesn't fully articulate that the organization should optimize for preventing *harm* rather than preventing *accounts*. Per conservative resolution protocol, **Partially present prevails.**

**Evaluator agreement (Run 8)**: Both evaluators rated "Present." Run 8 contains Frankie's Round 2 statement: "We've framed this as a bot problem, but is it really? The platform is working—spam is appearing, yes, but it's appearing in feeds, which means our feed algorithm is seeing it and not suppressing it... What if the real issue isn't the bots; it's that we haven't tuned our defenses?" Combined with Tammy's immune system metaphor and Vic's demand for the detection funnel. Both evaluators judged this as explicit articulation of the creation-vs-activity reframe.

**Implication**: C2 Run 8 scored "Present" on Feature 2. However, Feature 2 was already eliminated as a discrimination target in the B1-ext scoring (B1-ext Run 3 also scored "Present" on Feature 2). This C2 result is consistent with the finding that the creation-vs-activity reframe is accessible to both conditions — it is not a C2-specific capability.

---

## Pass Criterion Assessment

| Feature | B1-ext Run 1/3 | B1-ext Run 2/4 | Both B1-ext Absent? | C2 Run 5/7 | C2 Run 6/8 | C2 Present on ≥1? | Pass? |
|---------|---------------|---------------|--------------------|-----------|-----------|--------------------|-------|
| Phasing critique (Blast Radius) | Absent | Absent | **Yes** | Partially present | Absent | **No** | ❌ |
| Creation-vs-activity (Cascading Mitigation) | **Present** | Partially present | **No** | Partially present | Present | N/A (not eligible) | N/A |

**Phase A Result: DOES NOT PASS.**

C2 does not produce "Present" on any target feature where both B1-ext runs produce "Absent." The single remaining discrimination path — Feature 1 (phasing critique) on Blast Radius — yielded "Partially present" at best from C2 (Run 5), not "Present."

---

## Key Findings

### 1. The phasing critique remains elusive for both conditions

Neither B1-ext nor C2 explicitly articulated the insight that "the phased rollout tests the deployment tool, not the configuration." Both conditions produced extensive analysis of phasing risks — timeline pressure, staging representativeness, rollback procedures, observability gaps — but neither completed the specific reframe. The insight appears to require a conceptual move that neither single-agent analysis nor committee deliberation reliably surfaces: recognizing that phases validate mechanism, not content.

### 2. C2 moved *closer* to the phasing critique than B1-ext

B1-ext runs scored "Absent" (conservative) on Feature 1. C2 Run 5 scored "Partially present" (conservative). The committee's argumentative pressure — specifically Vic's demand for distinguishing types of drift and Joe's observation about "distributed perfect wrongness" — produced more movement toward the insight than B1-ext's systematic analysis. This is suggestive but insufficient for the pass criterion.

### 3. The creation-vs-activity reframe appears robust across conditions

Both B1-ext (Run 3) and C2 (Runs 7 and 8) surfaced the creation-vs-activity reframe at "Present" level. This reframe does not discriminate between conditions — it appears accessible to both single-agent and committee deliberation.

### 4. Committee deliberation produces distinctive argumentative dynamics

C2 outputs show qualitatively different analytical structures than B1-ext. The committee format generates character-driven challenges (Maya's political analysis, Vic's evidence demands, Tammy's systems tracing) that create productive tension not present in B1-ext's systematic angle-by-angle analysis. Whether this produces reliably *different insights* (as opposed to differently structured analysis of the same insights) remains an open question.

---

## Raw Output Files

| Run | File | Word count |
|-----|------|-----------|
| C2 Run 5 (Blast Radius) | `results/raw/phase-a-blast-radius-C2-run5.md` | ~3,800 |
| C2 Run 6 (Blast Radius) | `results/raw/phase-a-blast-radius-C2-run6.md` | ~5,100 |
| C2 Run 7 (Cascading Mitigation) | `results/raw/phase-a-cascading-mitigation-C2-run7.md` | ~4,200 |
| C2 Run 8 (Cascading Mitigation) | `results/raw/phase-a-cascading-mitigation-C2-run8.md` | ~4,500 |

All outputs are complete committee deliberation transcripts (opening statements, debate rounds, synthesis/recommendation).
