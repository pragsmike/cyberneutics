# Troubleshooting Cyberneutics

> "The map is not the territory, but if the map shows a bridge and your territory shows a cliff, stop driving."

This guide addresses common failure modes when implementing Cyberneutics methodology. It follows a **Problem → Diagnosis → Fix** pattern.

## 1. The Echo Chamber

**Problem**: All committee characters agree immediately. The debate feels like a group hug.
**Diagnosis**:
1.  **Premature Convergence**: The model's latent probability distribution has a very strong peak around the "safe" answer.
2.  **Insufficient Divergence**: Character propensities aren't distinct enough (or aren't incompatible enough).
3.  **Temperature Too Low**: The model isn't sampling wide enough to find the character voices.

**Fix**:
*   **Increase Temperature**: Bump from 0.7 to 0.9 or 1.0. High temperature rewards lower probability tokens, which helps distinct voices emerge.
*   **Force Conflict**: Add an explicit instruction to the Chair: *"The Chair must reject the first motion and demand a counter-proposal."*
*   **Extremize Propensities**: Rewrite character cards to be caricatures. Make the Skeptic paranoid. Make the Visionary reckless. You can dial them back later, but you need to break the consensus first.

## 2. The Bland Corporation

**Problem**: Characters speak in "AI Voice"—polite, verbose, structured lists, starting with "It's important to consider..." regardless of who is talking.
**Diagnosis**:
1.  **Model Mode Collapse**: The model is reverting to its RLHF safety training (the "Helpful Assistant" persona).
2.  **Weak Formatting**: Character names are just labels, not stylistic instructions.

**Fix**:
*   **Style Injection**: Add explicit style cues to character cards. *"Frankie speaks in short, punchy sentences. No jargon."* *"Vic uses academic hedging and cites specific policies."*
*   **Negative Constraints**: Tell the model what NOT to do. *"Do not use bullet points. Do not start sentences with 'It is crucial'."*
*   **The "Script Format" Trick**: Explicitly formatting as a dramatic script (SCENE STARTS) often switches the model from "Assistant Mode" to "Storyteller Mode."

## 3. The Infinite Filibuster

**Problem**: The debate goes in circles. Characters repeat points. No decision is reached.
**Diagnosis**:
1.  **Lack of Forcing Function**: Robert's Rules are missing or being ignored. There is no mechanism to force a vote.
2.  **Undefined Output State**: The committee doesn't know *what* it is trying to produce (a motion, a document, a score).

**Fix**:
1.  **Enforce the Clock**: Give the Chair a hard limit. *"The Chair must call for a vote after 4 turns."*
2.  **Define the Deliverable**: Ensure the prompt requires a specific artifact. *"The goal is to produce a 100-word Motion text, not to discuss."*
3.  **Intervene**: As the operator/Chair, step in. *"Order. We have heard this point. Is there a motion on the floor?"*

## 4. The Hallucination Spiral

**Problem**: Characters invent facts, policies, or previous decisions that don't exist, and other characters accept them as true.
**Diagnosis**:
1.  **Unchecked Narrative Drift**: The "Yes, and..." nature of LLMs means one small fabrication gets accepted as context for the next turn.
2.  **Temperature Too High**: The model is creative but untethered.

**Fix**:
1.  **Inject Ground Truth**: In the Chair's prompt, re-inject the actual facts. *"Reminder: Our budget is $50k, not $500k as stated by Vic."*
2.  **The "Fact Check" Character**: Assign one character (usually the Skeptic) the explicit role of verifying claims against the provided context.
3.  **Lower Temperature**: Drop to 0.5 or 0.4 for factual reviews, then back up for debate.

## 5. The Tautological Lesson

**Problem**: The "Lesson Extracted" is uselessly broad. *"We learned that communication is important."*
**Diagnosis**:
1.  **Shallow Gap Definition**: The original confusion wasn't specific enough.
2.  **Generic Query**: You asked "What did we learn?" instead of "What assumption proved false?"

**Fix**:
*   **Target the Delta**: Ask: *"What did the Skeptic see that the Visionary missed?"*
*   **Force Concrete Nouns**: *"Write the lesson using only concrete nouns. No abstract concepts like 'communication' or 'synergy'."*
*   **The "Surprise" Heuristic**: Ask the model: *"What was the most surprising moment in this debate?"* If nothing was surprising, the debate failed (see #1).

## 6. The Refusal ("I cannot roleplay...")

**Problem**: The model refuses to simulate the debate, claiming it cannot simulate people or opinions.
**Diagnosis**:
1.  **Safety Triggers**: You hit a refusal trigger (simulating real people, potential harm, sensitive topics).
2.  **Framing Failure**: The model thinks you want *it* to have an opinion.

**Fix**:
*   **The "Fictional Scenario" Frame**: Explicitly state: *"This is a fictional dialogue for educational purposes involving invented characters."*
*   **Third-Person Distance**: Don't ask *"What do you think?"* Ask *"Write a dialogue where Character A argues X."*
*   **Depersonalize**: Use archetypes instead of names if specific names trigger issues.

## Summary Checklist

If it's broken, check the **Cybernetic Loop**:

1.  **Signal**: Is the prompt (control signal) clear?
2.  **Gain**: Is the temperature (variance) correct?
3.  **Feedback**: Are you feeding the output back into the next turn with correction?
4.  **Constraints**: Are the "Walls" (Robert's Rules) solid enough to channel the flow?

Don't blame the model. Adjust the loop.
