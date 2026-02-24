---
name: committee
description: "Run an adversarial committee deliberation — five independent perspectives stress-test your decision from radically different angles"
---

# /cyberneutics:committee

**Run a structured adversarial deliberation on any complex decision or problem.**

Five independent committee members — each with a genuinely different worldview — examine your situation, argue with each other, and produce a map of the decision space. The output is not "the answer." It's a clear picture of what's at stake, what's uncertain, and what different framings reveal.

## What you'll get

- Five distinct opening positions on your problem
- A structured cross-examination where the members challenge each other
- A synthesis that maps the tensions, assumptions, and trade-offs — without papering over disagreements
- Specific next steps: what evidence to gather, what questions to ask, what to monitor

## How to use it

```
/cyberneutics:committee Should we expand into the European market?
```

Or provide more context for a sharper deliberation:

```
/cyberneutics:committee We're a 30-person SaaS company considering European expansion. Revenue is $5M ARR, growing 40% YoY. Our main competitor just opened a London office. We have no EU presence, no GDPR specialist, and our CTO is skeptical. Board wants a decision by Q2.
```

The more context you provide, the more specific and useful the deliberation will be. If your input is too vague, the committee will ask clarifying questions before proceeding.

## The five committee members

Each member runs independently — they don't see each other's work until the cross-examination phase. Full character definitions are in `skills/committee/characters/`.

| Member | Lens | Asks |
|--------|------|------|
| **Maya** | Political realism | "Who benefits if this fails? What are the hidden incentives?" |
| **Frankie** | Values & mission | "Does this betray our principles? Who gets affected?" |
| **Joe** | Institutional memory | "Didn't we try this before? What specifically is different?" |
| **Vic** | Evidence prosecution | "What evidence supports this? How would we verify it?" |
| **Tammy** | Systems thinking | "What's the feedback loop? What are the second-order effects?" |

## How the deliberation works

### STAGE 1 — Charter (the orchestrator)

Before invoking any members, the orchestrator drafts a one-paragraph charter: restating the topic as a genuine question, identifying what kind of uncertainty is present, and naming what a good deliberation would produce.

### STAGE 2 — Independent positions (all five members, in parallel)

Each member receives:
- The original topic/question
- The charter from Stage 1
- Instruction: produce your opening position independently, without seeing other members' views

All five positions are collected before proceeding.

### STAGE 3 — Cross-examination (each member sees all positions)

Each member receives:
- The original topic
- All five opening positions
- Instruction: respond to the positions you most agree with and most disagree with; sharpen or revise your own view

This is where the real value emerges. Members challenge each other directly. Polite agreement is a failure mode — the members are designed to argue.

### STAGE 4 — Synthesis (the orchestrator)

The orchestrator identifies:
- **Points of genuine agreement** — where all or most agents converge despite different lenses
- **Irresolvable tensions** — where the members disagree and the disagreement reflects a real trade-off, not a misunderstanding
- **What each position implies for action** — the practical consequences of each framing
- **The committee's recommendation** — with explicit dissents noted

### STAGE 5 — Confidence and provenance

The committee states its overall confidence (Low/Medium/High) and explains what would need to change to increase it. Key assumptions the recommendation depends on are listed explicitly.

## What the output looks like

**KEY TENSIONS IDENTIFIED:**
- [Tension 1]: Why these perspectives conflict
- [Tension 2]: What's being traded off

**ASSUMPTIONS SURFACED:**
- [Assumption 1]: Which member identified this
- [Assumption 2]: Why it matters

**EVIDENCE REQUIREMENTS:**
- What data/evidence would resolve key uncertainties
- What predictions are testable

**DECISION SPACE MAP:**
Not "do this" but "if you optimize for X, you sacrifice Y, and here's what each member thinks matters most"

**RECOMMENDED NEXT STEPS:**
- Information to gather
- Questions to ask stakeholders
- Small experiments to test key assumptions

## Important notes

**Traceability**: Every claim in the synthesis traces back to a specific member's position. You can always ask "who said that and why?"

**Disagreement is the signal**: If all five members agree easily, something is being swept under the rug. The value is in the tension between perspectives, not in consensus.

**Re-running is a feature**: Running this command multiple times on the same topic and comparing outputs reveals the topology of the decision space. If the outputs are similar each time, the decision is robust. If they differ, you've found a sensitivity — something worth investigating.

**The committee doesn't decide for you**: It shows you what you're actually deciding — the trade-offs, the assumptions, the risks. The decision is yours.

## Execution references

This command is executed by the `committee-orchestrator` agent (see `agents/committee-orchestrator.md`). The orchestrator reads the five committee member definitions from `skills/committee/characters/` (maya.md, frankie.md, joe.md, vic.md, tammy.md) and runs each through the five-stage protocol. Background knowledge about member interaction dynamics is in `skills/committee/SKILL.md`.
