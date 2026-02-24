---
name: handoff
description: "Create a session handoff — capture what was worked on, what was decided, and what comes next for continuity"
---

# /cyberneutics:handoff

**Save a summary of this working session for future reference.**

Creates a handoff document that captures what happened, what was decided, and what to do next. Useful at the end of a working session, after completing a major analysis, or before handing off to a colleague.

## What you'll get

A markdown file saved to your current working directory named `handoff-YYYY-MM-DD.md` containing:

- **Topic**: What this session was about
- **Techniques used**: Which cyberneutics commands were run (scenarios, committee, probe, review)
- **Key outputs**: The important findings, decisions, or insights produced
- **Open questions**: What wasn't resolved and why
- **Recommended next steps**: Prioritized, actionable items with context for why each is ready

## How to use it

At the end of a working session:

```
/cyberneutics:handoff
```

The command analyzes your session and generates the handoff automatically.

## What makes a good handoff

- **Specific**: "The committee identified GDPR compliance as the blocking issue with Medium confidence" not "There were some concerns"
- **Actionable**: "Next: gather evidence on GDPR compliance cost from three vendors" not "Look into GDPR"
- **Honest**: Include what didn't work, what was inconclusive, and what surprised you

## When to use it

- End of a significant working session
- After completing a major deliberation or probe
- Before handing off analysis to a colleague
- When you want a record of your reasoning process for later reference
