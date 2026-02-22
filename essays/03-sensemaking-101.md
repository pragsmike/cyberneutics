# Introduction to Sense-Making Methodology

## What is Sense-Making?

**Sense-Making Methodology** (SMM) is a communication theory developed by Brenda Dervin in the 1980s-90s that fundamentally changed how we understand human information-seeking behavior.

Traditional information science assumed people had **information needs** that could be satisfied by providing the right information. Dervin showed this was backwards.

People don't have "information needs." They have **situations they're trying to navigate** where their current understanding has run into a **gap**—and they construct **bridges** across those gaps using whatever sense-making resources are available.

The information isn't the goal. Movement through the situation is the goal. Information is just one possible bridge material.

## The Core Model: Situation-Gap-Bridge

Dervin's model has three components that always occur together:

### SITUATION
The context a person finds themselves in—the time, place, circumstances, history, constraints, and relationships that define their current state.

**Example**: You're three months into a project that's behind schedule. Stakeholders are asking questions. Your team is frustrated. Budget is tight.

That entire complex of circumstances is your **situation**.

### GAP
The point where your current understanding stops being adequate. Where you can't proceed without making sense of something you don't yet understand.

Gaps come in many forms:
- **Decision gaps**: "Which option should I choose?"
- **Comprehension gaps**: "What does this actually mean?"
- **Instrumental gaps**: "How do I actually do this?"
- **Evaluative gaps**: "Is this good or bad?"
- **Prediction gaps**: "What will happen if...?"

**Example**: You need to decide whether to add headcount or cut scope, but you don't understand which factors matter most to stakeholders, and you can't predict how either choice will affect team morale.

That's your **gap**.

### BRIDGE
Any cognitive or communicative move that allows you to cross the gap and continue moving through your situation.

Bridges can be:
- **Information**: Looking something up, asking someone
- **Interpretation**: Reframing the problem differently
- **Connection**: Relating this to something you already understand
- **Action**: Just trying something and seeing what happens
- **Dialogue**: Talking it through with someone
- **Narrative**: Telling yourself a story that makes sense of it

**Example**: You schedule separate conversations with your key stakeholders to understand their actual priorities (not the official ones). You talk through trade-offs with your team. You construct a story about what success looks like that you can defend to multiple audiences.

Those conversations and that narrative are your **bridges**.

## The Critical Insight: Bridges Change Situations

Here's what makes Sense-Making different from traditional information theory:

**The act of bridging a gap transforms the situation itself.**

You don't just "get information" and then return to the same situation with more knowledge. The process of seeking, interpreting, and integrating information **changes who you are and what situation you're in**.

After those stakeholder conversations, you're not in the same situation anymore:
- You know things about organizational dynamics you didn't know before
- Your relationships with stakeholders have shifted
- Your understanding of what "success" means has evolved
- New options have become visible
- Some paths that seemed open are now foreclosed

**You've moved. The landscape has moved. You're in a new situation now.**

This is why information-seeking is inherently **iterative and emergent** rather than linear and goal-directed.

### Teachback as Bridge-Testing

Dervin describes bridge-construction abstractly — people build bridges across gaps. But how do you know whether a bridge actually holds weight?

Gordon Pask's Conversation Theory provides the mechanism: **teachback**. After constructing a bridge (a hypothesis, a reframing, a course of action), you test it by teaching it back — restating it in your own terms, applying it to a new context, defending it against challenge. A bridge counts as successful when you can sustain mutual understanding despite perturbation.

This is Dervin's bridge-building made operational. The bridge isn't the information received; it's what survives re-articulation. If you can't teach it back — explain it to someone else, apply it to a variant scenario, hold it steady under questioning — you haven't actually crossed the gap. You've just papered over it with a plausible-sounding narrative.

In Pask's terms, understanding is a cyclically maintained network of mutually-entailing concepts — an **entailment mesh**. Each successful teachback strengthens edges in the mesh. Each failure reveals where the mesh is thin. The mesh is not a static knowledge structure but a living record of gaps that have been bridged and how.

The integrated picture: the learner walks a rhizomatic space (in the sense Deleuze describes — see [Essay 06](./06-deleuze-difference-repetition.md)), encounters gaps (Dervin), and uses conversation to construct bridges that stabilize through teachback (Pask). Three frameworks, one process.

## Why This Matters for AI Interaction

Traditional AI interaction assumes:
1. User has a question (information need)
2. AI provides answer (information)
3. User evaluates answer (satisfied or not)

But Sense-Making shows this is too simple:

1. User has a **situation** they're trying to navigate
2. User experiences a **gap** in their understanding
3. User formulates a question (first attempt at bridge-building)
4. AI responds (provides bridge materials)
5. User interprets response (constructs actual bridge)
6. **Situation has now changed** (user's understanding shifted)
7. **New gaps emerge** (from the new situation)
8. Process repeats

**The question isn't static. The user isn't static. The situation isn't static.**

This is why you can't just "ask Claude a question and get the answer." The first answer changes what you need to ask next. The process is **co-evolutionary**.

## Sense-Making is Active, Not Passive

Dervin emphasizes that sense-making is something people **do**, not something that happens to them.

You're not a passive recipient of information that "makes sense" or "doesn't make sense."

You're an active constructor who:
- **Defines what counts as a gap** (what needs explaining)
- **Decides what bridges are adequate** (what counts as "making sense")
- **Determines when to stop** (when you've made "enough" sense to proceed)

Different people in the same situation will:
- Notice different gaps
- Build different bridges
- End up in different new situations

**There is no objectively "correct" sense-making.** There's only sense-making that's adequate for *your purposes* in *your situation*.

## The Observer is Part of the System

This is where Sense-Making connects to **Second-Order Cybernetics**.

In traditional (first-order) cybernetics, you study systems and their feedback loops as if you were outside looking in.

In **second-order** cybernetics (von Foerster, Bateson), you recognize that **the observer is part of the observed system**.

When you're trying to make sense of a situation:
- Your observation changes what you're observing
- Your questions shape what answers are possible
- Your bridges alter the territory you're mapping

**You can't make sense of something without changing it—and being changed by it.**

Dervin's Situation-Gap-Bridge model is inherently cybernetic:
- Gaps emerge from your interaction with the situation (not "out there" waiting to be found)
- Bridges are feedback mechanisms that alter system state
- Each iteration produces new initial conditions

The full implications of this cybernetic loop — including why observation literally changes what you're observing — are developed in [Cybernetics and the Observer Problem](./04-cybernetics-and-observation.md).

## Gap-First Dialogue with Teachback Loops

The Dervin-Pask integration suggests a concrete design pattern for AI interaction — one that transforms Sense-Making from a descriptive framework into a conversation protocol:

1. **Elicit the gap explicitly.** Don't start with "tell me about X." Start with "here's my situation, here's where my understanding breaks down." Dervin's gap-first method: ask what confuses you, what you're trying to do, where you're stuck.

2. **Propose a bridge.** The AI generates a narrative that could cross the gap — information, a reframing, an analogy, a course of action.

3. **Teachback.** Before accepting the bridge, restate it in your own terms. Apply it to a variant of your situation. Defend it against a challenge. If you can't, the bridge is decorative — plausible-sounding but not load-bearing.

4. **Log the result.** Gaps and bridges are first-class objects in the interaction, not ephemeral query-response pairs. The history of gaps bridged (and bridges that failed teachback) is the entailment mesh of the conversation — a living record of what's been understood and what hasn't.

5. **Iterate.** The successful bridge changes the situation (Dervin). New gaps emerge. The cycle repeats.

This is a cybernetic loop with Pask's teachback as the feedback mechanism: walk → gap → conversation → bridge → teachback → mesh update → changed future walks.

## Practical Implications for AI Collaboration

Understanding Sense-Making changes how you work with AI:

### Don't ask "what's the answer?"
Ask "what stories can help me bridge this gap?"

### Don't expect static responses
Expect iterative exploration where each response shifts the terrain

### Don't treat AI as oracle
Treat it as collaborative bridge-building partner

### Don't optimize for "correct information"
Optimize for movement through complex situations

### Don't assume your first question is the right question
Expect to reformulate as you go

## Example: Sense-Making in Action

**Initial situation**: Product launch delayed, CEO asking why

**First gap**: "I don't know how to explain this without looking incompetent"

**First bridge attempt**: Ask AI "what should I tell the CEO?"

**AI response**: Provides several narrative frames

**New situation**: You now see multiple ways to frame the delay (each with different implications)

**New gap**: "I don't know which frame aligns with our actual priorities"

**Second bridge attempt**: "Which frame assumes we're optimizing for learning vs. execution?"

**AI response**: Distinguishes assumptions embedded in each frame

**New situation**: You realize you haven't actually clarified priorities with the CEO

**New gap**: "How do I have that conversation without it sounding like excuse-making?"

**Third bridge attempt**: "How do high-trust leaders frame setbacks as learning?"

And so on. Each answer produces new understanding that reveals new gaps.

**This isn't the AI failing to answer your question. This is successful sense-making.**

## Connection to Narrative Computing

Dervin's Sense-Making was developed before LLMs existed. But it's remarkably prescient about how narrative engines actually work.

LLMs don't retrieve information. They **generate narrative bridges**.

When you prompt an LLM, you're not querying a database. You're:
1. Describing a situation
2. Indicating a gap
3. Requesting bridge-building materials

The LLM responds by generating **a story that could plausibly bridge that gap**—drawing on patterns from all the stories in its training data about how similar gaps get bridged.

Sometimes those bridges are useful. Sometimes they're not. Sometimes they're actively misleading.

But understanding them as **bridge attempts** rather than "answers" changes everything:

- You don't ask "is this true?"
- You ask "does this bridge get me where I need to go?"

- You don't evaluate "correctness"
- You evaluate "usefulness for movement through my actual situation"

For concrete examples of narrative as the primary cognitive mode—how stories capture what mechanism misses in complex systems—see [Stories All the Way Down](./stories-all-the-way-down.md).

## Where We Go From Here

Sense-Making explains **what's happening** when you work with AI on complex problems.

Second-Order Cybernetics explains **why** observation changes state.

Deleuzian philosophy explains **how** repetition produces difference.

Together, they form **Cyberneutics**: a methodology for collaborative navigation of complexity using narrative engines.

The next essay explores the cybernetic foundations—how feedback loops, eigenforms, and observer effects structure the sense-making process itself.

---

## Further Reading

**Primary sources:**
- Dervin, B. (1992). "From the mind's eye of the user: The sense-making qualitative-quantitative methodology"
- Dervin, B. (1998). "Sense-making theory and practice: An overview of user interests in knowledge seeking and use"

**Applications:**
- Dervin's work is foundational in library science, information architecture, and human-computer interaction
- Her interview methodology (asking people about specific situations and gaps) influenced qualitative research methods
- The Situation-Gap-Bridge model has been applied to health communication, crisis communication, and organizational learning

**Why it matters now:**
- Dervin was studying human sense-making in an era of information scarcity and retrieval problems
- We now face information abundance and generation problems
- Her framework scales remarkably well to AI collaboration contexts
- The core insight—that information-seeking is active construction, not passive reception—becomes even more critical when the "information" is generated on-demand by narrative engines
