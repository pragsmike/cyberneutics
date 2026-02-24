---
name: fan-funnel
description: "Guidance on the exploration/commitment duality — when to diverge (scenarios) vs. converge (committee) vs. compose (probe)"
---

# Fan/Funnel Skill

## When this skill applies

This skill fires when:
- The user is exploring possible futures or weighing options
- The user asks about uncertainty — "what if?", "what might happen?", "how do we choose?"
- The user has run scenarios and wants to know what to do next
- The user has run a committee and wants to test robustness
- The user asks about the relationship between scenarios and committee

## The duality

Two fundamental operations underlie decision-making under uncertainty:

### Fan (one-to-many) = `/cyberneutics:scenarios`

**Purpose**: Explore before committing. Generate multiple distinct futures from one situation.

```
One situation → Multiple scenarios
```

Use when the uncertainty is about **what might happen** — you need to see the possibility space before you can reason about what to do.

### Funnel (many-to-one) = `/cyberneutics:committee`

**Purpose**: Commit after exploring. Converge multiple perspectives into a justified decision.

```
Multiple perspectives → One resolution (with dissents)
```

Use when you have a decision to make and need to **stress-test it** from different angles.

### Composed = `/cyberneutics:probe`

**Purpose**: Deliberated choice. Explore futures, then deliberate across them.

```
Situation → [Scenarios] → [Committee per scenario] → Landscape map
```

Use when the stakes are high enough to warrant understanding the **entire decision landscape** — not just one path through it.

## How they sequence

```
EXPLORE (fan)  →  DELIBERATE (funnel)  →  DECIDE (you)
   |                    |                     |
 scenarios         committee              your call
 "what if?"      "what should we do?"    "I choose X"
```

Each step feeds the next. Scenarios provide context for the committee. The committee provides analysis for your decision. Your decision is yours.

## When to use each

| Signal | Operation | Command |
|--------|-----------|---------|
| "I don't know what might happen" | Fan (explore) | `/cyberneutics:scenarios` |
| "I know the options, need to evaluate" | Funnel (converge) | `/cyberneutics:committee` |
| "I need to explore AND evaluate" | Fan then funnel | Scenarios, then committee |
| "Is my decision robust?" | Composed, iterated | `/cyberneutics:probe` |

## The key insight

**Running the same pipeline multiple times is not redundancy — it's landscape mapping.** Each run takes a different path through the possibility space. Comparing runs reveals:
- **Stable findings** (eigenforms): conclusions that persist across runs — commit with confidence
- **Variable findings** (residues): conclusions that shift — investigate what's driving the variance
- **Critical boundaries**: the specific assumptions where small changes flip the outcome
