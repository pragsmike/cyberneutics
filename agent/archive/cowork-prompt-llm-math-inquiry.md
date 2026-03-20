# Cowork Task: Record Epistemic Guardrails and Establish LLM-Steered Mathematical Inquiry Research Program

**Context**: mg has articulated three interconnected insights during a Claude Chat session that need to be recorded in the repository. These are not new ideas from scratch — they sharpen and formalize positions that are latent in existing material but not yet stated with the necessary precision.

---

## The three insights

### 1. Committee inspectability vs. decision quality

The committee's core value proposition is **inspectable reasoning records**, not superior decision outcomes. Solo evaluation can reach good decisions but does not reliably produce an audit trail. The deliberation transcript *is* the product, not a byproduct. This is a separate axis from whether the committee outperforms simpler approaches on decision quality (which is what the ablation study tests). Both claims matter, but they are independent — and the inspectability claim is the one that holds regardless of ablation results.

### 2. Epistemic status of formal work

The deep mathematical analyses — palgebra, furry logic, open games translation — are **provisionally useful but untrusted** until a human expert evaluates them. LLM-generated mathematics should not be treated as established results. This connects directly to the ACT outreach: one reason to engage the Cybercat community is to get qualified eyes on whether the categorical constructions actually work. The formal outputs are working hypotheses, not theorems.

### 3. LLM-steered mathematical inquiry as a research program

The formal work is simultaneously **subject matter and test case**. We are using the cyberneutics framework to push LLMs into doing real mathematics, which means the palgebra and furry logic analyses are not just categorical theory — they are empirical data about how well LLM pipelines can do mathematics when harnessed through structured deliberation. The interesting questions are:

- How do we steer LLM pipelines to do reliable mathematics?
- How do we know when they have?
- What does the calibration register need to track to support this?
- What is the role of human expert verification in the loop?

This is distinct from the existing metacognition research program (which focuses on SDT calibration of committee confidence) and from the existing formal development threads (which are *doing* the math). It sits at the meta-level: the epistemics of LLM-assisted formal reasoning.

---

## What to do

### Phase 1: Record in agent-facing memory

Update `agent/onboarding-core.md` to include these positions. Suggested placements:

- **Inspectability claim**: In or near the "Key vocabulary" section, or wherever the committee's value proposition is first described. The agent needs to know that "the committee produces inspectable records" is the load-bearing claim, and "the committee produces better decisions" is a separate empirical question under investigation.
- **Epistemic status**: Near any mention of palgebra or furry logic. The agent needs to know these are provisional — useful for structuring thinking but not to be cited as established results.

Also check `meta/project-state.md` — if it mentions formal work status, update there too.

### Phase 2: Identify placement in main documents

Search the following locations for passages where these insights should be discussed, sharpened, or added:

- `essays/` — especially Essay 01 (why narrative engines change everything), Essay 02 (from practice to theory), and any essay that discusses the committee's value or the role of formal methods
- `research-programs/README.md` — the research program overview should acknowledge the LLM-math-inquiry framing
- `research-programs/metacognition.md` (if it exists) or the metacognition diary entry — the boundary between metacognition and LLM-math-inquiry needs to be drawn
- `palgebra/` — any framing text should carry the epistemic caveat
- `wild/` diary entries on furry logic and open games — same caveat
- The root `README.md` — the "Why does this matter?" section currently frames the value in terms of reliable decisions; it should also mention inspectable reasoning as independently valuable

For each location: note what's already there, what's missing, and what specific text would need to change. Do not make the changes — produce a plan.

### Phase 3: Consider the research program

Think about what `research-programs/llm-mathematical-inquiry.md` would look like. Consider:

- **Scope**: What questions does it answer that metacognition and ablation don't?
- **Method**: How would you test whether LLM-steered math is reliable? (Candidates: submit palgebra results to ACT practitioners for review; run the committee on known-result problems and check; compare LLM-generated proofs against textbook proofs for structural fidelity)
- **Dependencies**: It depends on the calibration register (for tracking which mathematical claims survived review) and on human expert engagement (for ground truth). It probably depends on the ACT outreach succeeding.
- **Relationship to existing programs**: It's upstream of palgebra and furry logic (provides the epistemic framework they need) and downstream of metacognition (uses the calibration infrastructure). It's adjacent to the ablation study but asks a different question — not "does the committee help?" but "can the committee do mathematics?"
- **Pitch to ACT community**: "Here's a compositional framework for harnessing LLMs as mathematical exploration tools, and here's how we propose to calibrate trust in their outputs." This is more honest and more interesting than "we used LLMs to do category theory."

Produce a rough outline — not a finished document. mg will decide whether to create it.

### Phase 4: Handoff

Write a handoff noting what was recorded, what placement opportunities were identified, and what the research program outline contains. Flag any tensions or surprises you found — places where the existing documents already say something that conflicts with or complicates these insights.

---

## What NOT to do

- Do not rewrite essays or main documents. This is a recording and planning session.
- Do not create `research-programs/llm-mathematical-inquiry.md` as a committed file. Produce the outline in the `wild/` and mention in handoff.
- Do not treat the formal work as worthless — "provisionally useful but untrusted" is the correct register. The analyses have shaped thinking productively; they just can't be cited as proven.
- Do not conflate the three insights. Inspectability, epistemic status, and the research program are related but independent positions.

---

## Files to read before starting

1. `agent/onboarding-core.md` — canonical agent onboarding
2. `meta/project-state.md` — current state
3. Most recent `agent/handoff-*.md` — session context
4. `research-programs/README.md` — existing program landscape  
5. `palgebra/decorated-texts.md` (or whatever the main palgebra document is) — to see current framing
6. `agent/diary/2026-03-06-metacog-sdt-beer.md` — metacognition design, for boundary-drawing
7. `essays/01-why-narrative-engines-change-everything.md` — where the committee's value proposition is first argued

Skim, don't deep-read. You're looking for where these ideas land, not reviewing the full content.
