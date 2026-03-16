# Protocol Evaluation Rubric: Experimental Designs for Deliberative Architectures

**Purpose**: Score an experimental protocol on the properties that determine whether it can produce trustworthy, useful evidence about the relative effectiveness of deliberative architectures. Designed to be applied to the Black Swan Hindsight Framework (`evaluating-deliberative-architectures.md`) and to any future protocol in this research program.

**Scoring**: 0–3 per dimension (9 dimensions, max 27). Target: consistent 2–3 across dimensions. A protocol scoring 0 or 1 on any dimension has a structural flaw that should be addressed before execution. See "Using this rubric" for weighting guidance.

**How to use**: Read the protocol end to end. For each dimension, gather specific evidence (section numbers, claims, design features) and assign a score using the criteria below. Cite the evidence. Then identify which low-scoring dimensions can be fixed by protocol revision vs. which require fundamental redesign.

---

## Dimension 1: Construct Validity

*Does the protocol test what it claims to test?*

The protocol states a research question. The experimental design should produce evidence that bears on that question — not on a related but different question. The gap between "what the protocol says it tests" and "what the design actually tests" is the construct validity gap.

| Score | Criteria |
|-------|----------|
| 0 | The design does not test the stated question. The measurements are disconnected from the construct (e.g., claims to test "anticipation" but measures keyword presence). |
| 1 | The design tests something related to the stated question but with a significant gap. The construct is partially operationalized — some aspects are captured, others are missed or distorted. |
| 2 | The design tests the stated question through reasonable operationalizations. The gap between construct and measure is acknowledged and bounded. Minor aspects of the construct may escape measurement. |
| 3 | The design tightly operationalizes the stated question. The relationship between what is measured and what is claimed is explicit, justified, and robust to alternative interpretations. |

**Evaluation questions**:
- What is the stated research question? What does the protocol actually measure? Is there a gap?
- Could high scores on the measured metrics coexist with failure on the stated research question (or vice versa)?
- Are the constructed scenarios testing the construct (structural anticipation) or a proxy (structural feature recognition from a checklist)?
- Do the evaluation criteria measure what matters, or what's easy to measure?

---

## Dimension 2: Confound Control

*Are alternative explanations for observed differences adequately controlled?*

If architecture C2 outperforms B1, can we attribute that to deliberative structure — or could it be explained by token count, prompt complexity, scenario familiarity, evaluator recognizability, or another confound?

| Score | Criteria |
|-------|----------|
| 0 | Major confounds are uncontrolled and unacknowledged. Results would be uninterpretable regardless of outcome. |
| 1 | Major confounds are acknowledged but not controlled. The protocol notes limitations but doesn't design around them. Results would be suggestive but not evidential. |
| 2 | Major confounds are controlled or bounded. The protocol includes specific design features to isolate the independent variable. Some residual confounds remain but are identified and their likely impact estimated. |
| 3 | All identified confounds are controlled. The protocol includes explicit controls (token-matched baselines, effort-equalized conditions, structural blinding). Residual confounds are minor and documented. |

**Evaluation questions**:
- **Token/effort confound**: Does B1 (one prompt) produce 200 words while C3 (scenarios + committee) produces 5,000? If so, is the comparison "deliberation vs. none" or "200 words vs. 5,000 words"?
- **Structural blinding**: Can the evaluator distinguish conditions by output format (single paragraph vs. multi-character transcript)? If so, "blind" evaluation isn't blind.
- **Scenario provenance**: Were the constructed scenarios designed by people familiar with the methodology? If so, could they unconsciously embed features the methodology is tuned to detect?
- **Prompt engineering confound**: Is the B3 (multi-perspective) prompt a maximally strong version, or a strawman? Would a better B3 prompt close the gap with C2?
- **Model self-knowledge**: Does the LLM generating C2 outputs "know" the committee methodology from training data? If so, it may perform well on C2 not because deliberation helps but because it recognizes and performs the expected pattern.

---

## Dimension 3: Discriminant Power

*Can the protocol distinguish between conditions in a way that's informative?*

A protocol that produces identical scores across all conditions tells us nothing. A protocol where one condition dominates on all scenarios tells us something, but less than one that reveals *when and why* different architectures succeed or fail.

| Score | Criteria |
|-------|----------|
| 0 | The protocol is unlikely to produce score variation across conditions. Scenarios are too easy (all conditions score high) or too hard (all score low), or the scoring criteria are too coarse to discriminate. |
| 1 | The protocol may produce variation but lacks the resolution to interpret it. Scores are binary or near-binary; there are too few scenarios to establish a pattern; differences could be noise. |
| 2 | The protocol is designed to produce interpretable variation. Scenarios span a range of difficulty. Scoring has enough granularity to distinguish partial from full recognition. Sample size is marginal but sufficient for directional claims. |
| 3 | The protocol maximizes discriminant power. Scenarios are calibrated to the expected performance range (neither floor nor ceiling). Multiple difficulty levels reveal where each architecture breaks down. Sample size supports reliable effect estimates. |

**Evaluation questions**:
- Are the constructed scenarios hard enough that B1 will genuinely fail, or will a capable LLM get them right regardless of architecture?
- Are the scoring criteria fine-grained enough to show partial success, or do they collapse to "got it / didn't get it"?
- With N scenarios, how many different orderings of conditions are possible? Can the protocol distinguish the ordering it predicts from alternatives?
- Would running the same scenario twice with the same condition produce the same score, or is scoring so subjective that intra-condition variance swamps inter-condition variance?
- **Does the protocol include a mechanism for pre-testing scenario difficulty against baseline conditions?** A pilot run of the simplest condition (B1) on all scenarios can reveal floor/ceiling effects before the full investment. Score 3 requires either pre-tested scenarios or a built-in pilot gate.

---

## Dimension 4: Internal Consistency

*Do all parts of the protocol fit together without contradiction?*

The research question, conditions, scenarios, metrics, evaluation protocol, and results tabulation should form a coherent whole. Tensions between sections indicate design drift or unresolved disagreements.

| Score | Criteria |
|-------|----------|
| 0 | The protocol contradicts itself. The research question implies one design but the protocol implements another. Key definitions shift between sections. |
| 1 | Minor inconsistencies exist between sections. Definitions are mostly stable but edge cases create ambiguity. The metrics and the conditions don't perfectly align. |
| 2 | The protocol is internally consistent on all major points. Minor terminological variations don't affect interpretation. Each section serves the overall design. |
| 3 | The protocol is tightly integrated. Each section references and builds on others. Definitions are stable throughout. The results tabulation exactly captures what the evaluation protocol produces. |

**Evaluation questions**:
- Does the research question (structural risk anticipation) match what the metrics measure (anticipation + epistemic humility)?
- Do the constructed scenario criteria (binary checklists) match the general metric scales (0-3 ordinal)?
- Are the "anticipated results" (Section VIII predictions) consistent with the claim that this is an open empirical question?
- Does the protocol use "anticipation" to mean the same thing in the general metrics (Section VII) and in the constructed scenario criteria (Sections VIII-IX)?
- Do the results tables match what the evaluation protocol actually produces?

---

## Dimension 5: Executability

*Can the protocol be run as written with available resources?*

An elegant design that can't be executed is worse than a rougher design that can. The protocol should specify what's needed, and those requirements should be satisfiable.

| Score | Criteria |
|-------|----------|
| 0 | The protocol requires resources that don't exist or aren't available (specific human raters, unavailable models, undefined scenarios). Execution would require substantial improvisation. |
| 1 | The protocol is partially executable. Some steps require interpretation, missing definitions, or resource substitution. An executor would need to make significant design decisions not covered in the protocol. |
| 2 | The protocol is executable with minor adaptation. All major steps are specified. Some operational details are left to the executor's judgment but don't affect the design's integrity. Feasible within likely resource constraints. |
| 3 | The protocol is fully executable as written. All steps, scenarios, prompts, scoring criteria, and results formats are specified. An executor can follow it mechanically. Resource requirements are explicit and satisfiable. |

**Evaluation questions**:
- Are all scenario prompts provided verbatim, or does the executor need to write them?
- Are the evaluation criteria precise enough that two independent evaluators would produce similar scores?
- Does the protocol assume human raters? If so, are they available? If not, does it specify how LLM evaluation should work?
- Are the architecture conditions specified precisely enough to reproduce? (E.g., what exactly is the C1 "coordinator" prompt? What's the B3 "synthesize" instruction?)
- Is the blind evaluation operationally feasible given that outputs differ in length and structure?
- **Does the protocol distinguish between "fully specified" and "feasible within stated resource constraints"?** A protocol can be perfectly specified yet infeasible for a solo researcher (e.g., requiring human raters at $50/hour, 100+ LLM runs at significant cost). Score should account for whether the stated resources match what's likely available.

---

## Dimension 6: Statistical Adequacy

*Given the design's sample size and measurement scale, can it detect the effects it aims to measure?*

A protocol should be honest about what its statistical power allows it to claim. Overstating precision from small samples is worse than acknowledging directional-only evidence.

| Score | Criteria |
|-------|----------|
| 0 | The sample size and measurement approach are fundamentally inadequate for any quantitative claims. Statistical methods described cannot be meaningfully applied. |
| 1 | The sample size supports qualitative or directional claims only. The protocol overstates precision (e.g., reporting confidence intervals from N < 5). |
| 2 | The sample size is marginal but the protocol correctly frames its claims as preliminary or directional. Statistical methods match the data type and sample size. |
| 3 | The sample size supports the claimed level of precision. Statistical methods are appropriate. The protocol includes power analysis or explicit precision targets. |

**Evaluation questions**:
- With N = 4 constructed scenarios and ordinal 0-3 scoring, what statistical claims are possible?
- Does the protocol request "mean [95% CI]" or "Cohen's d" from data that can't support these calculations?
- Are the results tables calibrated to the actual achievable precision, or do they promise more than the design can deliver?
- Does the protocol distinguish between "this is what we'd ideally compute" and "this is what our sample size supports"?

---

## Dimension 7: Falsifiability

*Could the results genuinely disconfirm the hypothesis that deliberative architectures outperform simpler ones?*

A protocol that can only produce confirming evidence — by design, by scenario selection, by metric choice, or by interpretive framing — is not an experiment. It's a demonstration.

| Score | Criteria |
|-------|----------|
| 0 | The protocol cannot produce disconfirming results. Scenarios, metrics, or interpretive framing guarantee the hypothesis is confirmed. |
| 1 | Disconfirmation is theoretically possible but the design makes it unlikely. Scenarios are chosen to favor the methodology; metrics capture the methodology's strengths but not its weaknesses; the interpretive frame can absorb negative results. |
| 2 | Disconfirmation is genuinely possible and the protocol would report it honestly. Some design choices still favor the methodology, but not overwhelmingly. The protocol includes explicit statements about what disconfirmation would look like. |
| 3 | The protocol is designed to maximize the chance of informative disconfirmation. Scenarios include cases where simpler approaches might win. The methodology's predicted advantages are stated in advance as falsifiable predictions. Negative results are framed as valuable findings, not failures. |

**Evaluation questions**:
- Were the scenarios designed by people who believe in the methodology? If so, might they unconsciously avoid scenarios where deliberation doesn't help?
- Does the protocol define what a "negative result" looks like? (E.g., "if C2 does not outscore B3 by at least 1 point on Anticipation, the hypothesis is not supported.")
- Are there scenarios where the correct answer is "don't deliberate — just decide quickly"? Speed and simplicity are genuine advantages of B1 that the protocol doesn't measure.
- Could a reasonable person look at the protocol and conclude "this was designed to confirm, not to test"?

---

## Dimension 8: Honest Framing

*Does the protocol accurately represent what it can and cannot show?*

Overstatement erodes trust. A protocol that says "this is a preliminary test of structural feature recognition using constructed scenarios" is more valuable than one that says "this tests whether deliberative architectures anticipate structural risks" — if the former is accurate and the latter is not.

| Score | Criteria |
|-------|----------|
| 0 | The protocol's framing significantly overstates what the design can show. Claims and design are misaligned. |
| 1 | The framing is partially accurate but inflates the design's reach. Key limitations are acknowledged in a limitations section but not reflected in the main framing. |
| 2 | The framing is mostly accurate. The protocol distinguishes between what it tests directly and what it suggests. Limitations are integrated into the main narrative, not siloed. |
| 3 | The framing is precisely calibrated to the design's actual reach. Every claim is bounded by what the evidence can support. The protocol is useful precisely because it doesn't overclaim. |

**Evaluation questions**:
- Does the title/abstract/introduction promise more than the design delivers?
- Is there a gap between the Section I framing ("anticipatory validity") and what the constructed scenarios actually test (structural feature recognition)?
- Does the protocol distinguish between "what we learn from historical cases" and "what we learn from constructed cases"? These are different kinds of evidence.
- Are the predictions in Section VIII honest (advance registration of falsifiable expectations) or rhetorical (creating an expectation that confirmation validates and disconfirmation must be explained away)?

---

## Dimension 9: Adaptive Design and Responsible Use

> **Amendment note (2026-03-16)**: Added per committee recommendation ([deliberations/protocol-eval/03-resolution.md](../../situations/repo-next-major-move/deliberations/protocol-eval/03-resolution.md)). Dimensions 1-8 evaluate whether a protocol is well-designed and honestly framed. This dimension evaluates whether the protocol specifies what happens *after* it produces results — how findings should be interpreted, what decisions they should inform, and what protections exist against overinterpretation.

*Does the protocol specify decision gates, revision triggers, and protections against overinterpretation?*

A protocol that produces results without specifying how to use them responsibly is incomplete. This dimension covers three aspects: (a) adaptive design — does the protocol respond to its own findings? (b) audience guidance — does it specify who should and shouldn't draw conclusions from results? (c) overinterpretation protection — does it bound what can be claimed?

| Score | Criteria |
|-------|----------|
| 0 | The protocol has no decision gates, no revision triggers, and no guidance on how results should be interpreted or used. Results could be overclaimed without violating anything the protocol says. |
| 1 | The protocol has a limitations section but no operational decision gates. Audience guidance is vague ("interpret with caution"). No specified response to different outcome patterns. |
| 2 | The protocol includes decision gates (e.g., "if X, proceed; if Y, revise") and distinguishes what different types of results can and cannot show. Some audience guidance. Overinterpretation is warned against but not structurally prevented. |
| 3 | The protocol has explicit decision gates with specified responses to each outcome pattern. Different audiences are named with specific guidance on what they can conclude. The protocol's structure makes overinterpretation difficult — claims are bounded by design, not just by disclaimers. Revision triggers are specific and actionable. |

**Evaluation questions**:
- Does the protocol specify what to do if results confirm expectations? What if they disconfirm?
- Are there decision gates that prevent proceeding when prerequisites aren't met?
- Does the protocol name its intended audience and specify what that audience should and shouldn't conclude?
- Does the protocol distinguish between "this is what we can claim from these results" and "this is what we'd like to be able to claim"?
- If results were cherry-picked or misrepresented, would the protocol's own framing make that visible?

---

## Using this rubric

**Weighting note**: The nine dimensions are **not equally important**. Construct Validity (1) and Falsifiability (7) are foundational — a protocol scoring 0 or 1 on either should not be run, regardless of other scores. Confound Control (2) and Honest Framing (8) are next in priority — uncontrolled confounds make results uninterpretable, and dishonest framing makes even good results harmful. The remaining dimensions (3-6, 9) are important but their deficiencies are more likely fixable by protocol revision. The aggregate score (sum of all dimensions, max 27) is reported as a convenience but should not be treated as a single measure of protocol quality. Evaluators should prioritize specific dimensions when deciding whether a protocol is ready to run.

1. **Score each dimension 0–3** with citations to specific protocol sections.
2. **Identify critical failures** (any dimension at 0 or 1).
3. **Classify fixes**: Which low scores can be fixed by protocol revision? Which require new scenarios, different conditions, or fundamental redesign?
4. **Produce a remediation plan**: prioritized changes that would raise the protocol to consistent 2–3 across dimensions.

A protocol need not score 3 on every dimension to be worth running. A protocol scoring 2 on all dimensions is a solid preliminary study. But a protocol scoring 0 or 1 on Construct Validity or Falsifiability should not be run until those issues are addressed — the results would not be interpretable.
