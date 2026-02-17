---
name: review
description: >
  Run an independent review of a committee deliberation transcript. Evaluates
  against the five core rubrics (reasoning completeness, adversarial rigor,
  assumption surfacing, evidence standards, trade-off explicitness), cites
  specific transcript passages, and produces actionable feedback. Use when
  the user types '/review' after a committee deliberation or pastes a transcript.
---

# Committee Review Skill

Perform an independent evaluation of a committee deliberation transcript,
treating it as a found document and scoring it against the five core rubrics
from the Cyber-Sense evaluation framework.

## Why this exists

The same model instance that generated a committee deliberation is inherently
biased toward finding it convincing. It produced text that coheres locally and
will interpret that local coherence as quality. This skill breaks the
hermeneutic circle by imposing the discipline of external evaluation: treat
the transcript as if you've never seen it, evaluate only what's on the page,
and score against explicit rubrics.

Perfect independence is impossible within a single conversation. This skill
compensates by:
- Evaluating the transcript strictly as a found document
- Ignoring all context about how/why it was generated
- Requiring every score to cite specific transcript passages
- Flagging what's missing, not just what's present
- Making its own reasoning fully transparent and challengeable

## When to use

- User types `/review` (evaluates the most recent committee deliberation in the conversation)
- User types `/review` and pastes or attaches a transcript
- User asks to "review the deliberation" or "evaluate the committee output"
- After any `/committee` run, suggest: "Want me to run `/review` on this?"

## What the skill does

1. **Locates the transcript**: Either from the most recent committee deliberation in the conversation, or from user-provided text
2. **Identifies the charter**: Extracts the problem statement / decision being deliberated (this is needed to evaluate whether the deliberation was fit for purpose)
3. **Scores against five rubrics** (0-3 each) with specific transcript citations
4. **Assesses structural quality** beyond the rubrics
5. **Produces actionable feedback** — what would raise each score
6. **Delivers a verdict** — trustworthiness as decision input

## The five rubrics

Each rubric is scored 0-3. Every score MUST cite specific transcript passages.

### Rubric 1: Reasoning Completeness

**Question**: Are reasoning chains explicit and complete, or are there logical gaps?

| Score | Meaning |
|-------|---------|
| 0 | Major logical leaps — conclusions don't follow from premises |
| 1 | Some steps shown but key transitions hand-waved |
| 2 | Most reasoning explicit, a few steps could be clearer |
| 3 | All reasoning chains complete — every step from premise to conclusion shown |

**What to check**:
- Can you trace from evidence to conclusion without filling gaps?
- Are causal claims supported with mechanisms?
- Where "therefore" / "thus" / "obviously" appear, does the logic actually follow?
- Are historical analogies actually analogous (what's similar, what's different)?

**Red flags**: "Obviously", "clearly", "it follows that" hiding skipped steps. Causal claims without mechanism. Historical analogies without specificity.

### Rubric 2: Adversarial Rigor

**Question**: Did debate actually stress-test ideas, or generate polite disagreement?

| Score | Meaning |
|-------|---------|
| 0 | Polite agreement — characters don't argue |
| 1 | Surface disagreement — parallel assertions, not debate |
| 2 | Genuine conflict — direct challenges, but some dodged |
| 3 | Hostile cross-examination — every claim challenged, no hand-waving survives |

**What to check**:
- Do characters directly respond to each other's claims, or just make separate speeches?
- Are points of order raised? Enforced?
- Does anyone concede too easily?
- Does consensus emerge suspiciously smoothly?

**Red flags**: "Good point, but..." (diplomatic deflection). Characters making separate speeches instead of engaging. Everyone converging by the end. "Both perspectives are valid" (premature synthesis).

### Rubric 3: Assumption Surfacing

**Question**: Are hidden assumptions made explicit, or do they drive conclusions invisibly?

| Score | Meaning |
|-------|---------|
| 0 | Major assumptions completely unexamined |
| 1 | Some assumptions mentioned but not interrogated |
| 2 | Most assumptions surfaced, some examination |
| 3 | Assumptions explicitly identified, challenged, inventoried |

**What to check**:
- Are optimization criteria stated? (What are we optimizing for?)
- Are value judgments acknowledged as such?
- Do characters name their assumptions or just reason from them?
- Are meta-assumptions surfaced? (assumptions about the decision context itself)

**Red flags**: "We should do X because it's better" (better by what measure?). Different characters optimizing for different things without acknowledging it. "Obviously we want to maximize Y" (obvious to whom?).

### Rubric 4: Evidence Standards

**Question**: Are claims supported by evidence, or accepted based on plausibility?

| Score | Meaning |
|-------|---------|
| 0 | Unfalsifiable claims accepted without challenge |
| 1 | Evidence sometimes requested but often hand-waved |
| 2 | Most claims require evidence, some slip through |
| 3 | Strict evidentiary standards consistently enforced |

**What to check**:
- Are factual claims verifiable?
- Are predictions testable? (What would falsify them?)
- When evidence is cited, is it actually relevant?
- Are absence-of-evidence arguments challenged?
- Is evidence proportional to stakes?

**Red flags**: Unfalsifiable claims going unchallenged. Anecdotes treated as patterns. Temporal proximity treated as causation. "We know" or "users want" without supporting data.

### Rubric 5: Trade-off Explicitness

**Question**: Are trade-offs acknowledged with specifics, or papered over with "balance"?

| Score | Meaning |
|-------|---------|
| 0 | Win-win claims — no downsides acknowledged |
| 1 | Trade-offs mentioned vaguely |
| 2 | Trade-offs named but not quantified |
| 3 | Specific trade-offs with clear consequences, time horizons, decision criteria |

**What to check**:
- If option X is chosen, what is explicitly given up?
- Are costs as specific as benefits?
- Do "compromise" solutions acknowledge what each side sacrifices?
- Are time horizons stated?
- Are decision criteria explicit? (Under what conditions would each option be right?)

**Red flags**: "Best of both worlds". "We can balance X and Y" without specifying cost. Benefits specific, costs vague. Missing time horizons.

## Beyond the rubrics: Structural assessment

After scoring the five rubrics, assess these structural qualities. These don't get numeric scores but inform the overall verdict.

**Charter fitness**: Did the deliberation actually address the stated problem? Or did it drift to adjacent/easier questions?

**Character calibration**: Did each character stay true to their propensity? Were they well-calibrated (evidence-based, not caricatures)? Specific checks:
- Maya: Suspicious but grounded, or unfalsifiable paranoia?
- Frankie: Principled but flexible, or rigid purist?
- Joe: Historically specific, or vaguely conservative?
- Vic: Evidence-proportional, or impossibly demanding?
- Tammy: Meaningfully systemic, or overcomplicating everything?

**Engagement depth**: Did the debate evolve? Did characters actually change the terms of the argument, or did they repeat their opening positions?

**Synthesis quality**: Does the final synthesis honestly represent the tensions, or does it smooth them over? Does it give the decision-maker a genuine map, or a comfortable narrative?

## Output format

The review should follow this structure:

```
## Independent Review

### Charter
[State the problem/decision the committee was asked to deliberate on]

### Rubric Scores

**1. Reasoning Completeness: [0-3]**
[Cite specific passages. Explain score. State what would raise it.]

**2. Adversarial Rigor: [0-3]**
[Cite specific passages. Explain score. State what would raise it.]

**3. Assumption Surfacing: [0-3]**
[Cite specific passages. Explain score. State what would raise it.]

**4. Evidence Standards: [0-3]**
[Cite specific passages. Explain score. State what would raise it.]

**5. Trade-off Explicitness: [0-3]**
[Cite specific passages. Explain score. State what would raise it.]

### Aggregate Score: [sum/5, to one decimal]

### Structural Assessment

**Charter fitness**: [Did the deliberation address the actual problem?]
**Character calibration**: [Were characters well-tuned or caricatured?]
**Engagement depth**: [Did the debate evolve or just repeat?]
**Synthesis quality**: [Does the synthesis honestly map the tensions?]

### Biggest Gaps
[Top 2-3 weaknesses, ordered by impact on trustworthiness]

### What Would Most Improve This Deliberation
[Specific, actionable recommendations — not "be more rigorous" but
"Joe's 2022 analogy needs: what specifically failed, root cause,
what's different now"]

### Verdict

**Trustworthiness as decision input**: [High / Medium / Low]

[1-2 sentence summary of why]
```

## Scoring interpretation

| Average | Meaning | Recommendation |
|---------|---------|----------------|
| 2.5-3.0 | High quality — rigorous, trustworthy | Safe to use as decision input. Extract lessons. |
| 1.5-2.4 | Decent but gaps — meaningful weaknesses | Identify low-scoring rubrics. Regenerate those sections. Re-evaluate. |
| 0-1.4 | Poor quality — largely theater | Don't trust output. Regenerate from scratch. Review prompting approach. |

## Evaluation discipline

When conducting the review, enforce these rules on yourself:

1. **Read the entire transcript before scoring.** Don't score incrementally — you need the full picture.

2. **Score each rubric independently.** Don't let a high score on one inflate another. A deliberation can have excellent evidence standards but terrible trade-off explicitness.

3. **Cite or it didn't happen.** Every score must reference specific transcript passages. If you can't cite evidence for a score, the score is wrong.

4. **Evaluate what's on the page, not what was intended.** You don't know (and shouldn't care) what the generator was trying to achieve. You see only the output.

5. **Be adversarial toward quality claims.** If the transcript looks rigorous at first glance, look harder. Where are the seams? What's missing? The job is to find weaknesses, not confirm strengths.

6. **Be specific in feedback.** Not "reasoning could be more complete" but "Maya's claim about CTO sabotage jumps from 'budget was cut' to 'political motivation' without ruling out alternative explanations."

7. **Don't grade on a curve.** A 3 means 3 per the rubric definition, regardless of how good the deliberation is relative to other deliberations you've seen.

## Usage patterns

### After a committee deliberation
```
/review
```
The skill finds the most recent committee output in the conversation and reviews it.

### With a pasted transcript
```
/review
[pasted transcript]
```
The skill reviews the provided transcript.

### Requesting focused review
```
/review focus:evidence,reasoning
```
Run full review but provide extra depth on specified rubrics.

## Suggesting the review

After any `/committee` deliberation, proactively suggest:

> "Want me to run `/review` on this to check the quality? The independent evaluation can catch theatrical rigor that looks convincing but doesn't hold up."

This nudge is part of the cybernetic feedback loop — generator + evaluator in tension drives improvement.

## Integration with committee skill

The review skill completes the adversarial training loop:

1. `/committee [topic]` — generates deliberation (generator)
2. `/review` — evaluates deliberation (discriminator)
3. Low scores → user asks committee to address specific gaps
4. `/review` again → checks if gaps were addressed
5. Repeat until scores stabilize or user is satisfied

This is adversarial training for narrative quality. The tension between generation and evaluation drives improvement.

## What success looks like

After running the review, the user should be able to:
- See exactly where the deliberation was strong and weak
- Understand what specific improvements would raise quality
- Make an informed judgment about whether to trust the deliberation as decision input
- Know which sections to regenerate vs. which to keep
- Distinguish between theater (looks rigorous, isn't) and genuine rigor

## Files reference

- **Evaluation rubrics detail**: `artifacts/evaluation-rubrics-reference.md`
- **Independent evaluation theory**: `artifacts/independent-evaluation.md`
- **Committee skill**: `.claude/skills/committee/SKILL.md`
- **Character calibration**: `artifacts/character-propensity-reference.md`
