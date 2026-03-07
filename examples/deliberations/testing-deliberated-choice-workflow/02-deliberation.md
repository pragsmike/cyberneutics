# Phase 2: Deliberation

**Topic**: How to test the deliberated-choice workflow (fan→funnel composition)
**Protocol**: Robert's Rules (modified for adversarial committee)

---

## Opening Statements

### Maya (Paranoid Realism)

The thing that worries me most about testing this workflow is **testing it with a problem we already know the answer to.** If we pick a toy problem — "should we get a dog?" — we'll generate polite scenarios and a tidy resolution and declare victory. But we won't have tested anything. The workflow's purpose is to improve decisions under *genuine* uncertainty. If there's no genuine uncertainty, the fan produces decorative narratives and the funnel rubber-stamps whatever was obvious from the start.

Worse: if the test problem is drawn from this repository's own domain — "should we write essay X next?" — we create a self-referential loop where the methodology evaluates itself on its own terms. Who benefits from that? The methodology. It'll look great because it's playing at home.

My concrete concern: the composition seam between `/scenarios` and `/committee` is the weakest link. The charter bridging schema (`scenario_context`, `scenarios_summary`) is a translation layer, and translation layers are where information gets lost or distorted. I want the test to expose whether the committee actually *uses* the scenarios or merely *references* them. That's a qualitative judgment, not a checkbox.

### Frankie (Idealism / Values Guardian)

Maya's right that a toy problem is useless, but she's wrong about avoiding our own domain. The whole point of this methodology is **sense-making for real decisions.** Testing it on something we don't actually care about betrays the principle. If the test doesn't help us make a *real* decision, it's not testing the workflow — it's testing the mechanics. And the mechanics aren't what matter.

What I want from this test: evidence that the composed pipeline produces something *qualitatively different* from running `/committee` alone. If the scenario context doesn't change the deliberation — if the committee would have said the same things without it — then the fan→funnel composition is overhead, not added value. That's the existential test.

The test problem should be something where we genuinely don't know the answer and where the scenarios could plausibly shift the committee's deliberation. The acquisition example in the workflow doc is actually well-chosen in structure: high stakes, genuine uncertainty, multiple plausible futures. We need something analogous but real enough that the outcome matters.

### Joe (Continuity Guardian / Institutional Memory)

Let me point out what we learned from previous testing in this repo. Three bugs were found in the string diagram converter — Python 3.7 compatibility, UTF-8 encoding, continuation-line parsing — and every single one was found by *running the code*, not by reading it. The handoff says this explicitly: "Always test converter changes against the actual example file on the target system."

The same principle applies here, but the testing surface is different. The converter is deterministic — same input, same output. The deliberated-choice workflow is stochastic. Running it once tells you whether the *mechanics* work (files get created, schemas get populated, the composition seam holds). Running it once does *not* tell you whether it produces *better decisions*. That's a different kind of evidence entirely.

So my position is: we need to separate **mechanical testing** (does the pipeline produce correctly structured outputs at each stage?) from **quality testing** (does the composed pipeline produce substantively better deliberation than the committee alone?). The first is achievable in a single run. The second requires either multiple runs or a carefully designed comparison.

The previous deliberation runs we have — `example/` and `is-author-crackpot/` — give us a baseline for what a non-scenario-aware committee produces. That's actually useful: we can compare the scenario-aware run against those to check whether the resolution format actually changes (robust actions, scenario-dependent actions, monitoring plan, dismissed futures).

### Vic (Evidence Prosecutor)

Joe makes the right distinction but doesn't go far enough. Let me be specific about what evidence we need at each pipeline stage:

**Stage 1: /scenarios output.** Testable claims: (a) 4 scenario files get created in the correct directory structure, (b) each scenario has YAML front matter with the schema specified in the SKILL.md, (c) scenarios are narrated by different characters, (d) scenarios are genuinely distinct (differ on at least one divergence axis), (e) the coverage assessment identifies the correct axes. Items (a)-(c) are structural checks — binary pass/fail. Items (d)-(e) are qualitative — they require judgment.

**Stage 2: Charter bridging.** Testable claims: (a) the committee charter includes `scenario_context` and `scenarios_summary` fields, (b) `scenarios_summary` correctly reflects the scenario set (titles, narrators, key assumptions match), (c) the charter's success criteria include scenario-specific items. These are all structural — and they're the most likely failure point because this is the translation layer Maya flagged.

**Stage 3: Scenario-aware committee.** Testable claims: (a) each committee member's opening statement references at least 2 scenarios, (b) the debate ranges across futures (not collapsing to a single framing), (c) the resolution contains the four scenario-aware fields (robust actions, scenario-dependent actions, monitoring plan, dismissed futures). Item (a) is countable, (b) requires judgment, (c) is structural.

What I object to is any test plan that doesn't distinguish these levels. "Run it and see if it works" is not a test plan. We need a checklist.

### Tammy (Systems Thinker)

Everyone's talking about what to test, but nobody's talking about the feedback loop between the test problem and the test results. The choice of test problem isn't neutral — it shapes what we can learn.

Consider: if we pick a problem with *obvious* scenario divergence (acquisition: sell vs. don't sell), the fan will produce clearly distinct scenarios almost regardless of the roster's quality. That tests the plumbing but not the fan's ability to *generate* divergence from a situation where divergence isn't obvious. Conversely, if we pick a problem where divergence is subtle, we stress-test the fan but may conclude the plumbing is broken when it's the problem that's hard.

There's also a second-order effect in the composition. The committee skill's scenario-aware mode requires each character to engage with at least 2 scenarios in their opening statements. If the scenarios are vague or abstract, this engagement will be superficial — the characters will name-check scenarios without actually reasoning about them. The quality of the committee's output is bounded by the quality of the scenarios it receives. So a bad fan run can make the funnel *look* broken when the funnel is fine.

My recommendation: pick a problem that is (a) genuinely uncertain, (b) has natural divergence axes that the 4-core roster should capture without extensions, and (c) is concrete enough that committee characters can reason about it specifically rather than abstractly. And build the test plan to diagnose failures at each stage independently — if the committee output is weak, we need to distinguish "scenarios were bad" from "committee didn't use scenarios" from "composition seam lost information."

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Test must expose whether committee *uses* scenarios, not just *references* them; avoid self-referential testing | High | Translation layer information loss at composition seam |
| Frankie | Test must use a problem we care about; existential test is whether fan→funnel produces something /committee alone wouldn't | Medium | Test must validate purpose, not just mechanics |
| Joe | Separate mechanical testing from quality testing; use existing deliberations as baseline | High | Stochastic output means single run tests mechanics only |
| Vic | Stage-by-stage checklist with structural and qualitative items; reject "run and see" | High | Undifferentiated testing conflates distinct failure modes |
| Tammy | Test problem choice shapes what we learn; build diagnosis into the plan | Medium | Feedback loop between test problem and test results |

## Key Tensions Identified

1. **Problem domain**: Maya says avoid self-referential testing (methodology about methodology); Frankie says use a real problem we care about. These conflict if the only real problems we have are methodology-related.
2. **Mechanical vs. quality testing**: Joe and Vic agree these must be separated, but Frankie insists the quality test is what matters. If we only have time for one run, which takes priority?
3. **Test problem difficulty**: Tammy flags that "easy" problems test plumbing, "hard" problems test the fan — but a combined run can't isolate which component failed. Vic wants a checklist that diagnoses per-stage — does Tammy's concern mean we need multiple runs?

---

## Round 1

**Chair**: Let me sharpen the first tension. Maya and Frankie — can we find a test problem that is (a) not methodology-about-methodology and (b) genuinely matters to the project?

**Maya**: The project itself faces real decisions that aren't purely methodological. Here's one: *"The cyberneutics methodology is documented but has zero external uptake. Should the next effort focus on writing more essays (depth), building worked examples in new domains (breadth), or creating a simplified onboarding guide (accessibility)?"* That's a genuine strategic decision about this project's direction — it's not testing the methodology on itself, it's using the methodology to make a decision *about* the project. The uncertainty is real: we don't know which approach would actually produce uptake.

**Frankie**: I'll accept that. It passes my test — the decision matters, and the outcome isn't obvious. It also has clear divergence axes: depth vs. breadth, internal quality vs. external accessibility. The scenario roster should produce meaningfully different futures along these axes.

**Joe**: And it has concrete reference points. We can look at `meta/uptake-and-usage.md` to see what uptake looks like currently. The scenarios can cite specific artifacts, essays, and gaps. This isn't abstract.

**Vic**: I'll accept the problem framing but I want to tighten it. "Should we focus on depth, breadth, or accessibility?" is three options, not genuine uncertainty about *what might happen*. Scenarios are about futures, not options. Reframe: *"The cyberneutics methodology currently has no external adoption. What happens to the project over the next 12 months under different strategic choices?"* Now the scenarios can explore what each strategic path *leads to*, and the committee can deliberate across those futures.

**Tammy**: That reframing also helps with my concern. The divergence axes are: (1) investment focus (depth vs. breadth vs. accessibility) and (2) external response (organic discovery vs. active outreach vs. no uptake). The 4-core roster maps well: Continuity = "we keep writing essays as we have been," Disruption = "external attention arrives unexpectedly," Opportunity = "a latent asset becomes the growth vector," Constraint = "resources/attention thin out." That's good — natural divergence without forcing.

### Round 1 Analysis

- **Emerging consensus**: The test problem should be "future of cyberneutics methodology adoption over 12 months" — strategic, concrete, genuinely uncertain, and relevant to the project without being self-referential testing.
- **New tension**: None resolved — the mechanical vs. quality testing split remains.
- **Status**: Problem agreed in principle; test plan structure still open.
- **Next**: Define the test plan stages and acceptance criteria.

---

## Round 2

**Chair**: Joe and Vic, you both want mechanical and quality testing separated. Lay out the specific checklist. Tammy, watch for interactions between the stages.

**Vic**: Here is what I propose — a three-tier verification:

**Tier 1: Structural integrity** (binary pass/fail)
- `/scenarios` creates `agent/scenarios/<slug>/` with 00-situation.md, 01-roster.md, 01-parameters.md, 02-scenarios.md, 03-assessment.md
- Each file has correct YAML front matter per the skill spec
- 02-scenarios.md contains one section per core roster member (4 scenarios)
- `/committee` creates the deliberation directory with 00-charter.md through 03-resolution.md
- 00-charter.md contains `scenario_context` and `scenarios_summary` fields
- `scenarios_summary` matches the scenario set (narrator names, titles, assumption counts)

**Tier 2: Process compliance** (countable)
- Each scenario states explicit assumptions (at least 2 per scenario)
- Each scenario includes early warning signs (at least 2 per scenario)
- 03-assessment.md identifies divergence axes and checks quadrant coverage
- Each committee member's opening statement references at least 2 scenarios by name
- The resolution contains all four scenario-aware sections: robust actions, scenario-dependent actions, monitoring plan, dismissed futures

**Tier 3: Quality judgment** (qualitative, requires reviewer)
- Scenarios are genuinely distinct (not the same narrative with different labels)
- Committee debate ranges across futures (not collapsing to single framing within 2 rounds)
- Resolution's robust actions are actually robust (plausible across multiple scenarios)
- Resolution's scenario-dependent actions have genuine trigger conditions (not tautologies)
- The composed output is substantively different from what a standard committee would produce

**Joe**: On Tier 3, the last item — "substantively different from a standard committee" — we already have a baseline. The `is-author-crackpot` deliberation was a standard committee run. We can compare the resolution *format* at minimum: does the scenario-aware resolution contain fields that the standard resolution doesn't? That's Tier 2 really. The deeper comparison — "would the committee have reached a different conclusion without scenarios?" — is inherently counterfactual. We can't test it rigorously with one run.

**Maya**: Which is exactly why the Tier 3 items are judgment calls, not checksums. I'll add one more to Tier 3: **Does the charter bridge preserve or distort the scenarios?** Specifically: read the `scenarios_summary` in the charter, then read the full scenarios in 02-scenarios.md. Is anything material lost in the summary? Are the "key assumptions" actually the key assumptions, or are they generic summaries that strip the interesting specifics?

**Tammy**: The three tiers form a dependency chain. If Tier 1 fails, Tier 2 is meaningless — you can't count fields that don't exist. If Tier 2 fails, Tier 3 is compromised — you can't judge quality of engagement with scenarios if the engagement isn't there. So the test plan should be *sequential*: verify Tier 1, then Tier 2, then Tier 3. Fail early if a tier doesn't pass.

**Frankie**: I accept the three tiers, but I want to add something to the test plan that Vic's checklist doesn't capture: **reflexive value.** After running the full pipeline, we should ask: *"Did this process surface anything we hadn't considered about the project's strategic direction?"* If yes — even one genuine insight — the workflow has demonstrated its value regardless of how many checkboxes it ticks. If no — if it's all stuff we already knew, just reformatted — then the workflow is ceremony, not substance.

**Vic**: Frankie, I won't object to adding that as a Tier 3 item, but I will object to it *replacing* the structural checks. A workflow that produces insights but creates malformed files, or one that skips the charter bridge entirely and just runs a normal committee — those aren't acceptable even if the output happens to be good. The pipeline's reliability matters independent of any single run's content.

### Round 2 Analysis

- **Emerging consensus**: Three-tier verification — structural, process, quality — applied sequentially.
- **New tension**: Frankie's "reflexive value" vs. Vic's "structural reliability." Not contradictory but a question of what counts as *passing*. Resolved by including both.
- **Status**: Test plan structure largely agreed. Specific execution order next.
- **Next**: Finalize execution order, assign what can be checked mechanically vs. what needs review.

---

## Round 3

**Chair**: We need to nail down the execution. What's the actual sequence of actions and where do the verification checks go?

**Tammy**: Let me lay out the pipeline as stages with check-gates between them.

1. **Run `/scenarios`** with the agreed problem: "The cyberneutics methodology currently has no external adoption. What happens to the project over the next 12 months under different strategic choices?"
   - **Gate 1a (Tier 1)**: Verify directory structure and file presence.
   - **Gate 1b (Tier 2)**: Verify YAML schemas, assumption counts, early warning signs, coverage assessment.
   - **Gate 1c (Tier 3)**: Qualitative review — are scenarios genuinely distinct? Specific? Surprising?

2. **Run `/committee`** with `scenario_context:` pointing to the scenario output.
   - **Gate 2a (Tier 1)**: Verify charter contains `scenario_context` and `scenarios_summary`. Verify deliberation directory structure.
   - **Gate 2b (Tier 2)**: Count scenario references in opening statements. Verify resolution contains four scenario-aware sections.
   - **Gate 2c (Tier 3)**: Does the committee *engage* with scenarios or *cite* them? Is the debate cross-scenario? Is the charter bridge faithful?

3. **Post-run assessment**:
   - **Gate 3 (Tier 3 synthesis)**: Compare scenario-aware resolution format against `is-author-crackpot` resolution (standard format). Does the fan→funnel produce structurally different output? Does it produce substantively different output? Frankie's "reflexive value" check.

**Maya**: I want to add a specific negative test to Gate 2c. Look for what I'll call **scenario name-dropping**: a committee member says "As Continuity's scenario shows..." followed by an argument that has nothing to do with the scenario. This is the most likely failure mode of the composition — the committee formally satisfies "reference at least 2 scenarios" while substantively ignoring them. If we see this, the composition seam isn't working even if the structural checks pass.

**Joe**: Agreed. And one practical concern: this is the first time `/scenarios` has ever been run. The skill spec exists but has no execution history. We should expect some rough edges — perhaps the YAML schema has fields that don't quite match the spec, or the coverage assessment is too generic. These are *findings*, not *failures*. The test plan should distinguish "the pipeline is broken" from "the spec needs calibration." Both are valuable outcomes.

**Vic**: Fair. I propose we categorize findings as:
- **PASS**: Output matches spec, quality is adequate
- **DEVIATION**: Output doesn't match spec but the content is sound — spec needs updating
- **FAIL**: Output is malformed, missing, or vacuous

A run with DEVIATIONs but no FAILs is still a successful test — it tells us the design works but the spec needs tightening. A run with FAILs means the pipeline has a bug.

**Frankie**: And a run with all PASSes but no insight is a PASS on the mechanics and a question mark on the methodology. Which brings us back to: the test isn't done when the checklist is complete. The test is done when we can answer: "Does this pipeline help make better decisions?" That answer might be "we don't know yet, but the mechanics work" — and that's fine for a first run.

### Round 3 Analysis

- **Emerging consensus**: Sequential stage-gated execution with three-outcome findings (PASS/DEVIATION/FAIL). First run validates mechanics and calibrates specs; quality judgment is bonus.
- **Status**: DELIBERATION COMPLETE.

---

## Final Consensus

- **Test problem**: "The cyberneutics methodology currently has no external adoption. What happens to the project over the next 12 months under different strategic choices?" — strategic, concrete, genuinely uncertain, relevant to the project, clear divergence axes.
- **Three-tier verification**: Structural → Process → Quality, applied sequentially at each pipeline stage.
- **Three-outcome findings**: PASS / DEVIATION / FAIL — distinguishing pipeline bugs from spec calibration needs.
- **Composition seam gets extra scrutiny**: Charter bridge fidelity, scenario name-dropping detection, cross-scenario reasoning in debate.
- **First run validates mechanics**: Quality and reflexive value are bonus; the primary goal is confirming the pipeline produces correctly structured, scenario-aware output at each stage.
- **Existing deliberations as baseline**: Compare scenario-aware resolution against `is-author-crackpot` for format differences.

Status: DELIBERATION COMPLETE.

---

## KEY TENSIONS IDENTIFIED

1. **Self-referential testing vs. real problem**: Testing methodology on methodology inflates apparent value. Resolved by choosing a problem that uses the methodology to make a decision *about* the project (strategic direction), not *about* the methodology (is it good?).
2. **Mechanical vs. quality testing**: Single run can validate mechanics but not statistical quality. Resolved by accepting that first run is primarily mechanical validation; quality is bonus judgment.
3. **Specification fidelity vs. output value**: A run that deviates from spec but produces insight is different from one that matches spec but is vacuous. Resolved by three-outcome classification (PASS/DEVIATION/FAIL) and Frankie's "reflexive value" as a separate quality axis.

## ASSUMPTIONS SURFACED

- **The 4-core scenario roster will produce meaningfully distinct scenarios for this problem** (Tammy). If it doesn't, the fan isn't broken — the roster may need calibration for this type of problem.
- **The charter bridging schema is sufficient to convey scenario information** (Maya). The `scenarios_summary` compresses full scenarios into id/title/narrator/key_assumption. If this compression loses material information, the composition seam needs a richer bridge.
- **One run is enough for mechanical validation** (Joe). The pipeline is stochastic, but structural checks are deterministic — either the files exist with correct schemas or they don't.
- **The committee can distinguish "engage with scenarios" from "reference scenarios"** (Maya). This assumes the skill's intervention patterns catch scenario name-dropping. If they don't, the skill spec needs an additional intervention pattern.

## EVIDENCE REQUIREMENTS

- **Structural**: File presence, YAML schema conformance, field counts — all verifiable by inspection.
- **Process**: Scenario reference counts in opening statements, scenario-aware section presence in resolution — verifiable by reading.
- **Quality**: Scenario distinctness, cross-scenario reasoning, charter bridge fidelity, reflexive value — requires qualitative review.
- **Comparison**: Resolution format comparison against `is-author-crackpot/03-resolution.md` — requires reading both files.

## DECISION SPACE MAP

- **If you optimize for thorough testing**: Run multiple problems, compare across them. But this costs 3–4x the effort of a single run.
- **If you optimize for speed**: Run one problem, check structural integrity only. Validates plumbing but not purpose.
- **If you optimize for learning**: Run one problem with full three-tier verification including qualitative review. Maximizes insight from a single run. **This is where the committee consensus sits.**
- **If you optimize for specification quality**: Run one problem, treat every deviation as a spec bug to fix. Useful but risks premature optimization of specs before the pipeline has been used in anger.

## RECOMMENDED NEXT STEPS

1. **Run `/scenarios`** on "cyberneutics methodology adoption over 12 months." Verify Gates 1a–1c.
2. **Run `/committee`** with `scenario_context:` pointing to the scenario output. Verify Gates 2a–2c.
3. **Write a post-run assessment** documenting findings as PASS/DEVIATION/FAIL per tier.
4. **Compare** scenario-aware resolution against `is-author-crackpot` resolution for format differences.
5. **Record** Frankie's reflexive value check: did the pipeline surface anything genuinely new?
