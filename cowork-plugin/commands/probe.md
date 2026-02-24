---
name: probe
description: "Map the decision landscape — run scenarios and committee deliberation to find which conclusions are robust and which are fragile"
---

# /cyberneutics:probe

**Discover whether your decision is robust or fragile.**

A single deliberation gives you one perspective on a decision. A probe gives you the landscape — running the scenarios-then-committee pipeline and analyzing which conclusions hold up and which are sensitive to framing or assumptions.

Use this for high-stakes decisions where you need to know: "Would we reach the same conclusion if we ran this again?"

## What you'll get

- A set of scenarios exploring possible futures for your situation
- A committee deliberation on what to do across those futures
- A **landscape map** identifying:
  - **Robust conclusions** (eigenforms): findings that persist — safe to commit to
  - **Fragile conclusions** (residues): findings that vary — signals of sensitivity
  - **Critical boundaries**: the specific assumptions where small changes flip the outcome
  - **Monitoring plan**: early warning signs to watch

## How to use it

```
/cyberneutics:probe Should we acquire this competitor, given regulatory uncertainty and our current cash position?
```

Or reference previously generated scenarios:

```
/cyberneutics:probe [decision question] — using the scenarios above
```

## How the probe works

### Step 1: Scenario generation

Runs `/cyberneutics:scenarios` on your situation (or accepts pre-existing scenarios as input). This produces 4 distinct possible futures.

### Step 2: Deliberation across futures

For each scenario, runs `/cyberneutics:committee` with that scenario as context. Each deliberation asks: "Given this future, what should we do?"

### Step 3: Comparison and analysis

Collects all committee resolutions and identifies:

| Finding type | What it means | What to do |
|-------------|---------------|------------|
| **Eigenform** (appears across multiple scenarios) | This conclusion is robust — it holds regardless of which future materializes | Commit with confidence |
| **Residue** (appears only in some scenarios) | This conclusion is sensitive to assumptions | Investigate the assumptions it depends on |
| **Critical boundary** | A specific assumption where changing it flips the outcome | This is where your decision actually hinges — focus your research here |

### Step 4: Landscape map

A summary showing:
- The terrain: how many distinct clusters of conclusions exist
- What separates them: the load-bearing assumptions
- What's safe: actions that work across most futures
- What to watch: early warning signs indicating which future is unfolding

## Output: the landscape map

**(Scenario → Resolution → Confidence) table**

| Scenario | Committee resolution | Confidence |
|----------|---------------------|------------|
| Continuity | [resolution summary] | Medium |
| Disruption | [resolution summary] | Low |
| Adaptation | [resolution summary] | High |
| Constraint | [resolution summary] | Medium |

**Robust actions** (safe across most scenarios):
- [Action]: appears in 3/4 deliberations

**Contingent actions** (depend on which future materializes):
- [Action]: only if [assumption] holds

**Critical assumptions** (where the decision hinges):
- If [X], then [conclusion A]; if not [X], then [conclusion B]

**Monitoring plan**:
- Watch for [signal] — indicates [scenario] is materializing

## Cost and scope

A probe runs scenario generation plus a full committee deliberation for each of the 4 scenarios. That's 4 complete five-member deliberations — a substantial operation. Expect this to take several minutes and use significant context.

For lighter-weight exploration, consider running `/cyberneutics:scenarios` first, reading the output, and then running `/cyberneutics:committee` only on the 1-2 scenarios that seem most decision-relevant.

## For rigorous landscape mapping

For high-stakes decisions, run this command 3-5 times and compare the outputs. Stable resolutions across runs are robust. Unstable ones signal a decision near a critical boundary — that's where you need more information before committing.

## When to use probe vs. committee vs. scenarios

| Question | Tool |
|----------|------|
| "What might happen?" | `/cyberneutics:scenarios` |
| "What should we do?" | `/cyberneutics:committee` |
| "Is our decision robust?" | `/cyberneutics:probe` |
| "Where exactly does the decision hinge?" | `/cyberneutics:probe` (multiple runs) |
