# Quick Start Guide: Your First Committee Deliberation

## What This Guide Does

Gets you from "I've read about this methodology" to "I've run my first adversarial committee deliberation" in about 30 minutes.

This is the **minimal viable implementation**—enough to see if the approach works for your problem, not the full sophisticated protocol you'll develop over time.

## The fast path: slash commands

If you're working with an AI agent on this repository, the methodology is available as executable skills:

- **`/committee [topic]`** — runs a full adversarial committee deliberation, writes structured output to `agent/deliberations/`
- **`/review`** — independent evaluation of the transcript against five rubrics, with remediation feedback loop

These automate the five-step process described below. Try `/committee Should we hire two juniors or one senior?` to see it in action. The rest of this guide explains what the skills do and why, so you can use the methodology manually or adapt it to other tools.

## Prerequisites

- Access to Claude (or similar LLM)
- A real problem to work on (not a toy example)
- 30-45 minutes of focused time
- A way to save/organize output (text editor, note app, etc.)

## The Five-Step Process

### Step 1: Frame Your Problem (5 minutes)

Write down:

**What decision needs to be made?**
```
Example: Should we hire two junior engineers or one senior engineer?
```

**What's the current situation?**
```
Example: Team of 4 engineers, 6-month roadmap, tight deadlines, 
budget for 2 juniors OR 1 senior, CTO wants faster delivery
```

**What constraints apply?**
```
Example: Must decide by Friday, budget locked, can't change 
roadmap priorities, limited mentorship bandwidth
```

**What does success look like?**
```
Example: Hire decision that balances immediate delivery needs 
with long-term team capability
```

**Why is this hard?**
```
Example: Conflicting priorities (speed vs. talent development), 
unclear which matters more, past hiring mistakes still stinging
```

If you can't articulate why it's hard, you probably don't need this methodology. Just decide.

### Step 2: Initialize the Committee (5 minutes)

Copy this prompt template and fill in your problem:

```
I need an adversarial committee to help me think through a decision.

The committee roster is defined in agent/roster.md. Paste the character
definitions here, or if your tool can read files, reference that file
directly. Each character needs: name, propensity, key question, and
what they catch.

[PASTE CHARACTER DEFINITIONS FROM agent/roster.md]

The problem:
[PASTE YOUR PROBLEM FRAMING FROM STEP 1]

Please have each committee member respond with their initial perspective
on this decision. Keep responses to 2-3 paragraphs each. Be genuinely
adversarial—these perspectives should conflict, not converge.
```

> **Note**: If you're using the `/committee` skill in this repository, it reads the roster automatically from `agent/roster.md`. The template above is for manual use outside the skill.

### Step 3: Run the Debate (15 minutes)

After you get initial responses, push for actual conflict:

```
These initial responses are too polite. I need genuine adversarial 
debate, not diplomatic disagreement.

Using simplified Robert's Rules:

1. Someone make a specific motion (not vague suggestion)
2. Someone else must second it
3. Each character gets 2 minutes to argue for/against
4. Raise points of order if claims lack evidence
5. Vote on the motion

Make a motion and let's see real debate.
```

**Watch for these failure modes** (examples below use the standard roster names from `agent/roster.md`):

**Problem**: Characters agree too easily
**Fix**:
```
Stop. This consensus emerged too quickly. What conflict is being
papered over? [Paranoid realist], what specifically concerns you that
others are ignoring? [Evidence prosecutor], what evidence is missing
from this "agreement"?
```

**Problem**: Debate goes in circles
**Fix**:
```
Point of order: We're repeating arguments. Call the question. 
Let's vote on the current motion and move forward.
```

**Problem**: Claims without evidence
**Fix**:
```
Vic should challenge that. [Character] just claimed [X] without 
evidence. Vic, demand falsifiability criteria.
```

**Problem**: Skipped reasoning steps
**Fix**:
```
That jumped from premise to conclusion without showing the 
connection. Explain the intermediate steps.
```

### Step 4: Quick Evaluation (5 minutes)

In a **new conversation** (important: fresh instance), paste this prompt:

```
Evaluate this committee deliberation transcript for rigor.

Score each rubric 0-3:
1. REASONING COMPLETENESS: Are reasoning chains explicit?
2. ADVERSARIAL RIGOR: Did debate actually stress-test ideas?
3. ASSUMPTION SURFACING: Are hidden assumptions made explicit?
4. EVIDENCE STANDARDS: Are claims supported?
5. TRADE-OFF EXPLICITNESS: Are trade-offs acknowledged?

For each: give score, cite specific examples, explain what would 
raise the score.

[PASTE TRANSCRIPT HERE]
```

**Interpret scores:**

- **2.5-3.0**: Good deliberation, use it
- **1.5-2.4**: Decent but gaps exist, note what evaluator flagged
- **0-1.4**: Redo it, this was theater not deliberation

### Step 5: Extract One Lesson (5 minutes)

Write down:

**What worked well?**
```
Example: When we quantified trade-offs (2 seniors = +30% 
productivity, -100% pipeline), the decision space became clear
```

**What failed?**
```
Example: Joe cited "we tried this in 2022" without explaining 
what actually failed or why
```

**What would you do differently next time?**
```
Example: Demand explicit similarity analysis when anyone cites 
historical precedent
```

Save this. You've just created your first cross-scenario lesson.

## What You Should Have Now

After these 5 steps:

1. ✅ A deliberation transcript showing multiple perspectives
2. ✅ Explicit trade-offs and assumptions
3. ✅ Evaluation scores showing rigor level
4. ✅ One lesson for next time
5. ✅ Better understanding of your decision

**You still have to decide.** The committee didn't tell you what to do. But now you know:
- What you're trading off
- What assumptions you're making
- What could go wrong from multiple angles
- What evidence would change your mind

## Common First-Time Mistakes

### Mistake 1: "The AI didn't give me an answer"

**That's not a mistake—that's the point.**

The methodology helps you think, not replaces your thinking. You should end with clarity about trade-offs, not a recommendation to blindly follow.

**What to do**: Make your own decision based on the trade-offs that were surfaced. The committee's job is exploration, not conclusion.

### Mistake 2: "The characters were too polite"

**Fix**: Explicitly demand hostility.
```
This is too diplomatic. Maya should be paranoid. Vic should be 
prosecutorial. Make them fight.
```

If it's still too polite, try:
```
Pretend this is a high-stakes courtroom. Each character is trying 
to WIN the argument, not find common ground.
```

### Mistake 3: "I don't know if I did it right"

**There's no "right."** The question is: **did it help?**

Ask yourself:
- Do I understand my decision better than before?
- Did I discover assumptions I didn't know I was making?
- Did I consider perspectives I would have missed?
- Do I feel more confident (even if less certain)?

If yes → you did it right.

If no → what specifically didn't help? That's useful information.

### Mistake 4: "This took way longer than 30 minutes"

**Probably means:**
- Problem was more complex than you thought (good to discover!)
- Characters got too verbose (tell them to be concise)
- You went down rabbit holes (use "call the question" to move forward)
- You're iterating to improve scores (that's fine, skip for first run)

**For your actual first attempt**: Don't iterate, don't perfectize. Run it once, evaluate once, extract one lesson, move on.

### Mistake 5: "The evaluation was too harsh / too generous"

**If too harsh**: Fresh instances sometimes are stricter. That's okay—the gaps it flags are real even if you disagree with the severity.

**If too generous**: You might have used the same conversation thread (not fresh). Or your deliberation really was rigorous. Check against the rubric descriptions yourself.

## When This Approach Works Well

**Good fits:**
- Strategic decisions with multiple stakeholders
- Resource allocation with competing priorities
- Situations where you have a "gut feeling" you can't articulate
- Problems where you've been burned before
- Decisions where you need to defend your reasoning later

**Poor fits:**
- Simple factual questions
- Decisions with clear right answers
- Time-critical emergencies (no time for deliberation)
- Problems where you already have strong consensus
- Situations where analysis paralysis is the real risk

## What to Do Next

### If this helped:

**Read the detailed techniques**:
- [Adversarial Committees](./adversarial-committees.md) - character design and calibration
- [Robert's Rules as Forcing Functions](./roberts-rules-forcing-function.md) - procedural rigor
- [Independent Evaluation Protocols](./independent-evaluation.md) - comprehensive rubrics
- [Cross-Scenario Learning](./cross-scenario-learning.md) - building institutional memory

**Try it on another problem**:
- Different domain to test generality
- Inject the lesson you extracted from this run
- See if evaluation scores improve

**Start building your lesson library**:
- Extract lessons after each deliberation
- Organize by category or scenario type
- Inject relevant lessons into new deliberations

### If this didn't help:

**Diagnose why**:
- Was the problem actually simple? (methodology is overkill for straightforward decisions)
- Did characters not conflict enough? (try being more explicit about adversarial requirements)
- Was evaluation useless? (might need to calibrate rubrics for your domain)
- Did it feel like busywork? (might not be the right tool for your thinking style)

**Alternative approaches**:
- Simple pros/cons list might be enough
- Red team / premortem exercises
- Decision trees or quantitative models
- Just decide and learn from the outcome

**Not every decision needs this methodology.** If it's not helping, don't force it.

## Example: The 10-Minute Version

If you only have 10 minutes and need to see if this is worth exploring:

**1. Pick a real decision you're facing (30 seconds)**

**2. Paste this ultra-minimal prompt (30 seconds)**:
```
I need quick adversarial takes on this decision from 5 perspectives
(see agent/roster.md for full definitions): paranoid realist, idealist,
risk-averse historian, evidence prosecutor, systems thinker.

Decision: [YOUR DECISION]

Context: [2-3 SENTENCES]

Give me 1 paragraph each, maximum conflict between perspectives.
```

**3. Read the responses (5 minutes)**

**4. Ask yourself (2 minutes)**:
- Did this surface something I wasn't thinking about?
- Do I understand the decision space better?
- Is there genuine tension between perspectives?

**5. Decide (2 minutes)**:
- Worth exploring the full methodology?
- Or was this enough to unstick my thinking?
- Or was this not useful for this problem?

## Ready to Start?

You don't need to read anything else. You have enough to try this on a real problem right now.

Pick a decision you're facing. Frame it. Initialize the committee. See what happens.

The worst case: you spend 30 minutes and learn this approach doesn't work for you. That's valuable information.

The best case: you discover a methodology that makes your AI collaboration genuinely useful for complex problems.

Either way, you'll know more than you do right now.

**Go try it.**

---

**Still have questions?** See [Troubleshooting](./troubleshooting.md) for common problems and solutions.

**Want to see examples?** Check [Example Transcripts](./examples/) for worked cases.

**Ready to go deeper?** Read the [Core Techniques](#core-techniques) for comprehensive protocols.
