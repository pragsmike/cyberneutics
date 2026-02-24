# Cyberneutics

**Structured adversarial deliberation for decisions under genuine uncertainty.** Five independent AI agents with radically different worldviews stress-test your thinking, surface hidden assumptions, and map the trade-offs you're actually facing.

## The three things you can do

- **Explore possible futures** (`/cyberneutics:scenarios`) — Generate distinct scenarios for your situation so you can prepare for multiple possibilities, not just the one you expect.

- **Stress-test a decision** (`/cyberneutics:committee`) — Five independent agents examine your problem from political, values-based, historical, evidentiary, and systems perspectives. The output is a map of the decision space, not a recommendation.

- **Test decision robustness** (`/cyberneutics:probe`) — Run scenarios and deliberation together, then analyze which conclusions hold up across different futures and which are fragile.

## Quick start

**You're considering whether to expand into a new market.** You're not sure if the market will consolidate or fragment, your team is split, and the board wants an answer.

**Step 1: Explore the futures.**

```
/cyberneutics:scenarios Our B2B SaaS company is considering European expansion. Revenue $5M ARR, growing 40%. Main competitor just opened London office. No EU presence, no GDPR specialist. Board wants a decision by Q2.
```

You'll get four distinct scenarios — what if trends continue? What if something breaks? What if key actors adapt? What if conditions tighten? — each with concrete events, assumptions, and early warning signs.

**Step 2: Deliberate across those futures.**

```
/cyberneutics:committee Should we expand into Europe now or wait? Consider the scenarios above.
```

Five agents debate your options. Maya asks who benefits politically if expansion fails. Frankie asks whether this serves your mission or just your growth metrics. Joe recalls the last failed international push. Vic demands evidence on market size and GDPR costs. Tammy traces how expansion changes your team dynamics and product roadmap.

**Step 3: Check the quality.**

```
/cyberneutics:review
```

An independent evaluation scores the deliberation against five rubrics. Did the agents actually argue, or just make polite separate speeches? Were trade-offs specific or vague? Were claims evidence-backed?

## When to use this

- Complex decisions with competing considerations and no obvious right answer
- Genuine uncertainty about what might happen
- Situations where you need to explain your reasoning afterward
- When "what are we missing?" matters more than "what's the answer?"
- Strategic planning, partnership decisions, organizational changes, market entry, hiring strategy

## When NOT to use this

- Simple questions with clear right answers
- Data lookups or factual queries
- Extreme time pressure that doesn't allow for deliberation
- Low-stakes decisions where the cost of being wrong is trivial

## Command reference

| Command | What it does |
|---------|-------------|
| `/cyberneutics:scenarios [situation]` | Generate 4 distinct possible futures |
| `/cyberneutics:committee [decision]` | Run a 5-agent adversarial deliberation |
| `/cyberneutics:probe [situation]` | Map the decision landscape (scenarios + committee) |
| `/cyberneutics:review` | Evaluate a deliberation's quality against 5 rubrics |
| `/cyberneutics:handoff` | Save a session summary for continuity |
| `/cyberneutics:string-diagram [workflow]` | Visualize a process as a resource equation diagram |
