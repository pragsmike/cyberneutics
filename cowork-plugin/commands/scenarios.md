---
name: scenarios
description: "Generate divergent scenarios — explore 4 distinct possible futures for your situation before committing to a decision"
---

# /cyberneutics:scenarios

**Explore possible futures before you commit to a plan.**

When you face genuine uncertainty about *what might happen* — not just what to do — this command generates a set of distinct, plausible futures. Each scenario is narrated from a different lens, making assumptions explicit and tracing concrete consequences.

The output is not a forecast. It's a map of the possibility space — showing you which uncertainties matter most and what early warning signs to watch for.

## What you'll get

- 4 distinct narrative scenarios, each exploring a different possible future
- Explicit assumptions underlying each scenario
- Key implications: what each future means for your decision
- Early warning signs: observable signals that would indicate a particular future is materializing
- A coverage assessment: are there important futures you haven't considered?

## How to use it

```
/cyberneutics:scenarios Our main product faces potential disruption from open-source alternatives
```

Or with more detail:

```
/cyberneutics:scenarios Our 50-person B2B SaaS company has been approached by a larger competitor about acquisition. The offer is 3x revenue. We have 18 months of runway. The founding team is split — CTO wants to sell, CEO wants to raise Series B. Key uncertainty: will the market consolidate or fragment?
```

A good situation description includes:
- **What's uncertain**: The ambiguities the scenarios should explore
- **What's at stake**: Why this situation matters
- **Time horizon**: How far into the future to project (default: 2-3 years)
- **Key actors**: Who has agency in this situation

## The four lenses

Each scenario is narrated independently by a character with a distinct worldview:

| Lens | Explores | Asks |
|------|----------|------|
| **Continuity** | What if current trends continue? | "What does the future look like if nothing fundamentally changes?" |
| **Disruption** | What if a major break occurs? | "What would it look like if the rules of the game changed?" |
| **Adaptation** | What if actors adjust creatively? | "How might the key players reinvent themselves?" |
| **Constraint** | What if external forces tighten? | "What happens if regulation, resources, or conditions get harder?" |

## What each scenario contains

Each scenario is a short narrative (2-3 paragraphs) — a vivid, specific story, not a bullet list. It includes:

- **Title**: A memorable name for this future
- **Assumptions**: What this scenario assumes is true (stated explicitly)
- **Narrative**: A coherent story of how this future unfolds — with names, numbers, dates, and concrete events
- **Key implications**: What this future means for your decision (2-3 bullets)
- **Early warning signs**: Observable signals that this future is materializing (2-3 bullets)

## After the scenarios

The command ends with a brief assessment:
- Which scenarios are **most plausible** (given what you know today)
- Which are **most consequential** (would require the biggest response)
- Which are **easiest to probe for early signals** (where you could test assumptions cheaply)

## What to do next

**If you want to decide**: Feed the scenarios into a committee deliberation:
```
/cyberneutics:committee [your decision question] — considering the scenarios above
```
The committee will debate which futures to optimize for, which to survive, and which to dismiss.

**If you want to explore further**: Run scenarios again with different parameters or a different time horizon. Variance between runs reveals which futures are robust and which are sensitive to framing.

**If you want the full picture**: Use `/cyberneutics:probe` to run scenarios + committee multiple times and map the entire decision landscape.

## When to use scenarios vs. committee

| Situation | Use |
|-----------|-----|
| "What might happen?" | `/cyberneutics:scenarios` |
| "What should we do?" | `/cyberneutics:committee` |
| "What should we do given what might happen?" | Scenarios first, then committee |
| "How robust is our decision?" | `/cyberneutics:probe` |
