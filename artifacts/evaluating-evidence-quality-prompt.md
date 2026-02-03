# Prompt: Evaluating Evidence Quality for AI Product Selection

**Use this prompt** when you have gathered raw evidence (vendor reports, benchmarks, white papers) and need to determine if it is sufficient to make a high-stakes selection decision.

**Goal**: The committee is *not* selecting the winner yet. They are evaluating whether the *evidence* is robust enough to justify a selection.

---

### Copy and Paste into Claude

```text
I need an adversarial committee deliberation to evaluate the quality of evidence for selecting AI assistant products.

THE GOAL:
We need to select the top 3 AI assistant products suitable for our top 5 use cases.
However, right now our job is NOT to make the selection.
Our job is to decide: **Is the current evidence of high enough quality to make this determination?**

CONTEXT:
- We have vendor reports and white papers (attached below as "EVIDENCE").
- We have documentation of our intended use cases (attached below as "USE CASES").
- There is a risk of "garbage in, garbage out" if we select based on marketing fluff.

COMMITTEE ROSTER:

MAYA (Paranoid Realism)
- Focus: Who wrote these reports? What are they hiding? Is the "evidence" just marketing?
- Asks: "Who benefits if we believe this chart? What constraints are they omitting?"

FRANKIE (Idealism / Values Guardian)
- Focus: Do these potential products align with how we *should* be working?
- Asks: "Does the evidence even measure what matters (privacy, ethics, user agency) or just speed/cost?"

JOE (Continuity / Institutional Memory)
- Focus: Have we been fooled by similar "evidence" before?
- Asks: "This benchmark looks exactly like the one Vendor X showed us in 2021 before they failed. What makes this different?"

VIC (Evidence Prosecutor) - **CRITICAL ROLE**
- Focus: Rigorous cross-examination of the data.
- Asks: "Is this third-party or first-party data? What was the sample size? Is the benchmark reproducible? This claim is unfalsifiable."

TAMMY (Systems Thinker)
- Focus: Impact of relying on this data.
- Asks: "If we optimize for the metrics in these reports, what second-order effects will we see in our actual workflow?"

PROCEDURE:
1.  **Review the Evidence**: Read the provided texts.
2.  **Initial Assessment**: Each character provides a 1-paragraph assessment of the *evidence quality* (not the product quality).
3.  **Cross-Examination**: Characters challenge each other. Vic should be aggressive about methodology. Maya should be aggressive about source bias.
4.  **The Vote**: The committee must vote on the motion: *"The current evidence is sufficient to select top 3 candidates."*
    - If NO: Specify exactly what evidence is missing.
    - If YES: Proceed to outline which 3 candidates look strongest based on this evidence.

INPUT DATA:

[PASTE YOUR USE CASE DOCUMENTATION HERE]

[PASTE YOUR EVIDENCE FILES / VENDOR REPORTS HERE]

Start the deliberation.
```
