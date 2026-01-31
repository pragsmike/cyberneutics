# Implementation Plan: Hiring Decision Example Artifact

## Goal Description
Create a comprehensive example artifact (`artifacts/examples/hiring-decision-example.md`) that demonstrates the Cyber-Sense methodology in action. The example will feature a full deliberation by the "Adversarial Committee" on a high-stakes hiring decision, showcasing the "Game Within a Game" concepts (characters as players with winning conditions).

## Proposed Changes

### [artifacts/examples]

#### [NEW] [hiring-decision-example.md](file:///c:/Users/prags/Documents/cyber-sense/artifacts/examples/hiring-decision-example.md)
*   **Scenario**: Hiring "Alex," a brilliant but potentially toxic 10x engineer.
*   **Characters**:
    *   **Maya (Paranoid)**: Flags the risk to team cohesion.
    *   **Frankie (Idealist)**: Argues for the potential upside and brilliance.
    *   **Vic (Skeptic)**: Demands evidence of actual 10x impact vs. just noise.
    *   **Joe (Continuity)**: Worries about the existing team's morale.
    *   **Tammy (Systems)**: Analyzes the second-order effects on the codebase and culture.
*   **Structure**:
    1.  **Scenario Setup**: The candidate profile and the dilemma.
    2.  **Round 1: Initial Takes**: The "Statistical Ghost" (default LLM answer) vs. the Committee's opening moves.
    3.  **Round 2: The Debate**: Conflict/Argumentation using Robert's Rules.
    4.  **Round 3: The Vote**: Final decision.
    5.  **Independent Evaluation**: A fresh model instance grading the transcript against the "Rigorous Reasoning" rubric.
    6.  **Lessons Extracted**: What we learned (e.g., "Brilliance is a lagging indicator; toxicity is a leading indicator").

## Verification Plan

### Manual Verification
*   **Read-Through**: Verify that the characters sound distinct (Maya sounds paranoid, Vic sounds skeptical).
*   **Link Check**: Ensure the new artifact is properly linked from `artifacts/examples/README.md`.
*   **Concept Check**: Ensure it vividly illustrates the "Game Within a Game" concept (e.g., mention "Maya wins this round by finding the hidden risk").
