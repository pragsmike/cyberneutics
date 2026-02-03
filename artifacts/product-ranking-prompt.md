# Prompt: Ranked Selection of AI Products

**Use this prompt** AFTER the committee has voted that the evidence is sufficient. This conducts the actual selection and ranking process.

---

### Copy and Paste into Claude

```text
The committee has determined that the evidence is of sufficient quality to proceed. 
We will now move to the **Ranking and Selection Phase**.

THE GOAL:
Select and rank the top 3 AI assistant products based on our specific Use Cases and Scoring Rubrics.

INPUTS:
- **Use Cases**: (Refer to previously provided documentation)
- **Evidence**: (Refer to previously provided vendor reports/white papers)
- **Experience Reports**: (Assumed context: anecdotal preferences and user feedback)
- **Scoring Rubrics**: We will use a weighted scoring model (defined below).

COMMITTEE ROSTER (Standard Roles applied to Selection):

MAYA (Paranoid Realism)
- Focus: Hidden costs of the "best" option. Vendor lock-in risks.
- Watch out for: "Free" features that are actually bait.

FRANKIE (Idealism / Values Guardian)
- Focus: Which product aligns with our team's ethos?
- Watch out for: Products that encourage bad habits or surveillance, even if they score high on utility.

JOE (Continuity / Institutional Memory)
- Focus: Which product is least likely to function differently in 6 months?
- Watch out for: Volatile roadmaps from startups vs. stagnation from incumbents.

VIC (Evidence Prosecutor)
- Focus: Enforcing the rubric.
- Watch out for: "Vibes" creeping into the final score. If it's not in the data, it doesn't count.

TAMMY (Systems Thinker)
- Focus: Integration friction.
- Watch out for: High scores on isolated features that degrade the overall system workflow.

PROCEDURE:

1.  **Define the Rubric**:
    The committee must quickly agree on the weights for these 4 criteria (total 100%):
    - **Capability** (Raw performance on use cases)
    - **Integration** (System fit/friction)
    - **Risk** (Vendor stability, security, lock-in)
    - **Alignment** (Values, ethics, user agency)

2.  **Individual Scoring**:
    Each character scores the top 5 candidates on a 1-5 scales for each criterion, providing a brief rationale.

3.  **Adversarial Debate**:
    - Vic challenges high Availability scores that lack SLAs.
    - Maya challenges low Risk scores for large vendors.
    - Frankie challenges Alignment scores for surveillance-heavy tools.

4.  **Final Ranking**:
    - Produce a specific, ordered list: #1, #2, #3.
    - For each, list the "Killer Feature" (why it won) and the "Poison Pill" (the biggest risk we are accepting by choosing it).

Start the ranking process by defining the specific criterion weights.
```
