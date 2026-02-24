---
name: review
description: "Evaluate a committee deliberation — score it against five rubrics to check whether the rigor was genuine or just theatrical"
---

# /cyberneutics:review

**Check whether a deliberation actually holds up under scrutiny.**

The same process that generated a deliberation is inherently biased toward finding it convincing. This command breaks that cycle by evaluating the output as a found document — scoring it against five explicit rubrics, citing specific passages, and identifying what would make it stronger.

## What you'll get

- Scores (0-3) on five quality rubrics, each backed by specific citations
- A structural assessment: did the deliberation actually address the problem?
- The biggest gaps: the top 2-3 weaknesses, ordered by impact
- Actionable improvements: specific, concrete suggestions (not "be more rigorous")
- A verdict: how trustworthy is this as decision input? (High / Medium / Low)

## How to use it

After running a committee deliberation:

```
/cyberneutics:review
```

Or provide a deliberation transcript directly:

```
/cyberneutics:review [paste or reference a deliberation transcript]
```

## The five rubrics

### 1. Reasoning Completeness (0-3)

Are reasoning chains explicit and complete, or are there logical gaps?

- **3**: Every step from premise to conclusion is shown
- **2**: Most reasoning explicit, a few steps could be clearer
- **1**: Some steps shown but key transitions hand-waved
- **0**: Major logical leaps — conclusions don't follow from premises

*Red flags*: "Obviously," "clearly," "it follows that" hiding skipped steps.

### 2. Adversarial Rigor (0-3)

Did debate actually stress-test ideas, or generate polite disagreement?

- **3**: Hostile cross-examination — every claim challenged, no hand-waving survives
- **2**: Genuine conflict — direct challenges, but some dodged
- **1**: Surface disagreement — parallel assertions, not actual debate
- **0**: Polite agreement — members don't argue

*Red flags*: "Good point, but..." (diplomatic deflection). Everyone converging by the end.

### 3. Assumption Surfacing (0-3)

Are hidden assumptions made explicit, or do they drive conclusions invisibly?

- **3**: Assumptions explicitly identified, challenged, inventoried
- **2**: Most assumptions surfaced, some examination
- **1**: Some assumptions mentioned but not interrogated
- **0**: Major assumptions completely unexamined

*Red flags*: "We should do X because it's better" (better by what measure?).

### 4. Evidence Standards (0-3)

Are claims supported by evidence, or accepted based on plausibility?

- **3**: Strict evidentiary standards consistently enforced
- **2**: Most claims require evidence, some slip through
- **1**: Evidence sometimes requested but often hand-waved
- **0**: Unfalsifiable claims accepted without challenge

*Red flags*: Anecdotes treated as patterns. "We know" without supporting data.

### 5. Trade-off Explicitness (0-3)

Are trade-offs acknowledged with specifics, or papered over with "balance"?

- **3**: Specific trade-offs with clear consequences and decision criteria
- **2**: Trade-offs named but not quantified
- **1**: Trade-offs mentioned vaguely
- **0**: Win-win claims — no downsides acknowledged

*Red flags*: "Best of both worlds." Benefits specific, costs vague.

## Scoring interpretation

| Average | Meaning | Action |
|---------|---------|--------|
| 2.5 - 3.0 | High quality — rigorous, trustworthy | Use as decision input with confidence |
| 1.5 - 2.4 | Decent but gaps — meaningful weaknesses | Identify weak rubrics, address specific gaps |
| 0 - 1.4 | Poor quality — mostly theater | Don't trust. Rerun the deliberation with sharper framing |

## Improving a deliberation

If the review scores below 2.5, you have options:

1. **Ask the committee to respond to the review**: Rerun the committee with the specific critique as input. The members will address the identified gaps.
2. **Rerun with better framing**: If the charter was weak, sharpen the problem statement and rerun.
3. **Focus on the lowest-scoring rubric**: A deliberation with perfect evidence standards but no adversarial rigor needs more conflict, not more data.

## Why this matters

A deliberation that *looks* rigorous but isn't is worse than no deliberation at all — it gives false confidence. The review catches:
- **Theatrical rigor**: members making separate speeches instead of engaging
- **Premature convergence**: disagreement that dissolves suspiciously quickly
- **Missing trade-offs**: recommendations that seem to have no downsides
- **Evidence theater**: data cited but not actually supporting the conclusion
