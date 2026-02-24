---
name: orientation
description: "Contextual guidance for when and how to use cyberneutics techniques"
---

# Orientation Skill

## When this skill applies

This skill fires when:
- The user seems to be facing a complex decision with competing considerations
- The user asks "what should we do about X?" and the answer isn't straightforward
- The user expresses genuine uncertainty ("I'm not sure whether...", "we're torn between...")
- The user asks for multiple perspectives or wants to stress-test a plan
- The user invokes any cyberneutics command for the first time

## When NOT to use cyberneutics

Not every problem needs a committee. Skip the methodology when:
- **The answer is clear**: If there's an obvious right answer, just act on it
- **It's a data lookup**: "What was our revenue last quarter?" doesn't need five perspectives
- **Time pressure is extreme**: If you must decide in minutes, a quick gut check beats a thorough deliberation you don't have time for
- **The stakes are low**: Don't run a committee on lunch plans
- **It's a single-expert question**: "How do I configure this server?" needs expertise, not deliberation

## The five core ideas

1. **Everything is narrative.** LLMs generate stories. So do humans. Math proofs, legal arguments, strategic plans — all narratives. Recognizing this is the starting point.

2. **Unreliable primitives, reliable systems.** A single AI response drifts and distorts. Multiple independent perspectives, structured conflict, and explicit evaluation make the system trustworthy — like how redundancy in engineering makes unreliable components reliable.

3. **Repetition produces difference.** Running the same question multiple times isn't checking for consistency — it's mapping the space of possible answers. Different runs reveal different territory.

4. **Observation changes state.** Every response you read changes what you think. The goal is navigating complexity, not delivering finality.

5. **You are the editor.** The system generates perspectives and framings. You decide which ones get published to reality.

## Command index: which tool for which problem

| Your situation | Use | Why |
|---------------|-----|-----|
| "What might happen?" | `/cyberneutics:scenarios` | Explore possible futures before committing |
| "What should we do?" | `/cyberneutics:committee` | Five perspectives stress-test your options |
| "Was our analysis rigorous?" | `/cyberneutics:review` | Independent evaluation against quality rubrics |
| "Is our decision robust?" | `/cyberneutics:probe` | Map the decision landscape, find fragile assumptions |
| "Capture this session" | `/cyberneutics:handoff` | Record what happened and what comes next |
| "Visualize this process" | `/cyberneutics:string-diagram` | Formalize workflows to reveal hidden structure |

## Common pitfalls

- **Collapsing to single answers prematurely.** If you find yourself with "the answer" quickly, you're probably missing something. Sit with the tensions.
- **Ignoring disagreement.** When agents disagree, that's the signal — it means there's a real trade-off. Don't smooth it over.
- **Skipping the review.** A deliberation that looks rigorous might not be. The review catches theatrical rigor.
- **Using the wrong tool.** Scenarios explore futures; committees evaluate options. Don't run a committee when you need scenarios, or vice versa.
