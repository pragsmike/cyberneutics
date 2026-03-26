# Session Handoff: 2026-03-20 (LLM-Math-Inquiry Recording and Planning)

---

## Session Summary

**Trigger**: mg instructed: execute `agent/prompts/cowork-prompt-llm-math-inquiry.md` — a four-phase recording and planning task.

**Actual outcome**: All four phases completed. Three epistemic positions recorded in agent-facing memory; placement plan produced for main documents; rough research program outline written in `wild/`; this handoff.

**Deliverables**:
- `agent/onboarding-core.md` — New section "Epistemic positions the agent must know" (three subsections: inspectability, epistemic status, LLM-math-inquiry). Epistemic caveat added to palgebra row in repository map.
- `meta/project-state.md` — New section "Epistemic positions (recorded 2026-03-20)" summarizing the three positions.
- `wild/llm-mathematical-inquiry-outline.md` — Rough research program outline (scope, methods, dependencies, relationship diagram, open questions for mg).

---

## Phase 2: Placement Plan

The following is the survey of where the three insights should land in main documents. **No edits were made** — this is the plan only.

### Insight 1: Committee inspectability vs. decision quality

| Location | What's there now | What's missing | Suggested change |
|----------|-----------------|----------------|------------------|
| **README.md** "Why does this matter?" (lines 85-97) | Lists "Rigorous, traceable decision-making" and "Auditable artifacts with full provenance" as outcomes | Does not distinguish inspectability as independently valuable from decision quality. The framing implies these are secondary benefits of good decisions, not a separate axis. | Add a sentence after the bullet list: something like "The inspectable reasoning record is independently valuable — it is the committee's primary product, not a byproduct of decision quality." |
| **Essay 01** (lines 219-250, the explainability section) | Makes the system-level observability argument well: "The transcript becomes evidence." | Does not make the sharper claim that the transcript is the *product*, not just evidence. The framing is still in service of the "reliable systems from unreliable components" argument, which is about decision quality. | Add a paragraph near line 242 ("The discourse becomes observable...") that distinguishes: "Even if the committee does not outperform simpler approaches on decision quality — which is a separate empirical question — the inspectable deliberation record has independent value as an audit trail." |
| **Essay 02** (lines 57-65, rediscovering the committee) | Frames the committee as a game-theoretic defense against entropy. Focus is on constraining latent space to explore tails. | The value proposition is entirely about decision quality (better exploration of possibility space). Inspectability is not mentioned. | Add a note after the "Why It Works" subsection: the committee's secondary value is that the game produces a transcript, and the transcript is inspectable in a way that solo LLM outputs are not. |
| **`research-programs/README.md`** (lines 47-56, "Where to start" table) | Priority ordering is by "how much they reduce the main open uncertainties: Does the methodology outperform simpler approaches?" | The framing assumes decision quality is the only axis of value. A program could reduce uncertainty about inspectability without addressing decision quality. | Add a footnote or parenthetical: "These programs primarily address the decision-quality claim. The inspectability claim — that the committee produces auditable reasoning records regardless of outcome quality — is treated as established rather than empirical." (If mg disagrees that it's established, this becomes an open question.) |
| **`essays/when-methodology-fails.md`** (lines 33, 52, 62) | The "Overcapitalization" failure mode (line 33ff) implicitly makes the inspectability/quality distinction: the committee produces a rich transcript but the decision didn't need it. | The distinction is implicit. The essay doesn't name "inspectability as independent value" as a concept. | In the Overcapitalization section, add: "Note that even in this failure mode, the committee produced an inspectable record of the reasoning that led to the (unnecessary) analysis. Whether this record has archival or training value is a separate question from whether the decision needed the methodology." |

### Insight 2: Formal work is provisionally useful but untrusted

| Location | What's there now | What's missing | Suggested change |
|----------|-----------------|----------------|------------------|
| **`palgebra/README.md`** | Straightforward description of the formalism. No epistemic caveat. | Readers (especially external ones) could treat the categorical constructions as established mathematics. | Add a note at the top or in the "Key ideas in brief" section: "Epistemic status: The constructions here are provisionally useful for organizing thinking about LLM pipelines, but they have not been reviewed by domain experts in category theory. They should be treated as working hypotheses, not established results. See the LLM-mathematical-inquiry outline in `wild/` for the proposed path to validation." |
| **`palgebra/categorical-structures.md`** | Already has lax/approximate coherence framing from the 2026-03-13 review. Overclaimed universal properties were weakened to "design targets." | The review added appropriate hedging on specific claims, but the document's overall framing still reads as confident category theory, not as "LLM-generated mathematics under review." | Add an epistemic status block at the top (similar to the one proposed for README.md). The existing hedges within the text are good; what's missing is the meta-level framing. |
| **`wild/committee-games/`** | Open games translation. No epistemic caveat visible in README. | Same concern: could be read as established applied category theory. | Add epistemic status note to README.md in that directory. |
| **`wild/diary/2026-03-13-furry-logic.md`** | Diary entry, explicitly exploratory. | The diary format already signals provisionality. No change needed beyond what the format implies. | None — diary entries are self-evidently provisional. |
| **Root README.md** Palgebra section (lines 133-140) | Describes palgebra confidently: "a formal language for specifying pipelines..." | No caveat about epistemic status. External readers clicking through would assume this is established formalism. | Add parenthetical: "(...a formal language for specifying pipelines — currently at working-hypothesis status pending expert review; see `wild/llm-mathematical-inquiry-outline.md`)" or similar. |

### Insight 3: LLM-steered mathematical inquiry as a research program

| Location | What's there now | What's missing | Suggested change |
|----------|-----------------|----------------|------------------|
| **`research-programs/README.md`** | Lists existing programs. No mention of LLM-math-inquiry. The "By theme" table has "Theory / foundations" but it refers to societies-of-thought items, not the meta-question of whether the math is trustworthy. | No acknowledgment that the formal work raises its own epistemological questions distinct from the methodology's general effectiveness questions. | When the outline is promoted to a real research program: add a row to the "Active research programs" table and a "Meta / epistemics" row to the "By theme" table. For now: add a note to "Where to start" referencing the outline in `wild/`. |
| **`wild/diary/2026-03-06-metacog-sdt-beer.md`** (lines 99-105) | Calls for metacognition as its own research program. Mentions "math development co-design" — SDT calibration enriches categorical structure, palgebra and metacognition should proceed together. | Does not distinguish the meta-question (can LLMs do math?) from the object-level question (what does the math say?). The "co-design" framing is about keeping the math and calibration aligned, not about validating whether the math is correct. | When the metacognition research program is created, draw the boundary explicitly: metacognition asks "is the committee calibrated?"; LLM-math-inquiry asks "can the committee do mathematics?". The co-design point stands — they share infrastructure — but they are different programs. |
| **`wild/README.md`** | Does not mention the LLM-math-inquiry outline. | Missing entry for the new file. | Add `llm-mathematical-inquiry-outline.md` to the README, probably under "Formalization and Theory" or as a standalone entry. |

---

## Tensions, Conflicts, and Surprises

### 1. The metacognition diary entry already implies the LLM-math-inquiry position — but doesn't name it

The 2026-03-06 diary entry says "palgebra development and metacognition design need to proceed together, not sequentially" and that meta-d'/d' lives in enriched categories. This is the same territory as insight 3, but framed as a technical co-design requirement rather than as an epistemological research program. The diary entry is concerned with making the calibration register *mathematically compatible* with the palgebra formalism. The LLM-math-inquiry insight goes further: the palgebra formalism itself is an empirical data point about LLM mathematical capability. No conflict, but the distinction needs to be drawn when both programs are formalized.

### 2. Essay 01's explainability section is remarkably close to the inspectability claim — but stops one step short

Lines 228-250 of Essay 01 make the system-level observability argument (Shannon, von Neumann, compose unreliable components into reliable systems). The argument culminates in "The opacity is at the component level. The observability is at the system level." This is the *mechanism* for inspectability but it doesn't make the *value* claim: that the inspectable record is independently valuable regardless of whether the system achieves better decisions. The essay could be read as saying "inspectability is how we get reliability" (instrumental) rather than "inspectability is itself the product" (intrinsic). Adding the sharper claim would strengthen the essay without contradicting it.

### 3. The research-programs README frames everything through decision-quality uncertainty

The priority table (lines 47-56) asks "Does the methodology outperform simpler approaches? When does it help? How do we know?" All three questions are about decision quality. If the inspectability claim is correct — that the transcript is the product — then there's a missing category of uncertainty: "Does the methodology produce inspectable reasoning records that are useful independently of decision quality?" This isn't a contradiction but it's a gap in the framing that becomes visible once you state the inspectability position explicitly.

### 4. The categorical-structures review (2026-03-13) is a retroactive pilot of Method 4

The focused mathematical consistency review of `categorical-structures.md` — where overclaimed universal properties were weakened to design targets, lax coherence framing was added, and a monad composition bug was found — is exactly the kind of adversarial probing that Method 4 in the research program outline describes. It wasn't designed as a research data point, but it could be scored retroactively. This is a pleasant surprise: we already have one data point for the research program without having designed it.

### 5. No conflict between the three insights

The prompt warned "do not conflate the three insights." Having worked through the placement, I confirm they are genuinely independent:
- Inspectability is about the committee's value proposition (what it delivers)
- Epistemic status is about the formal work's trustworthiness (how much to believe)
- LLM-math-inquiry is about the meta-question of whether LLMs can do mathematics under structured guidance (what we're learning about the tool)

They share a common theme — epistemic humility — but they apply to different objects and have different implications.

---

## Mistakes and Lessons

1. **Phase 3 came naturally from Phase 2.** The survey of placement locations gave enough context to write the research program outline without additional reading. The prompt's suggested reading list was well-chosen — the metacognition diary entry was particularly important for drawing the boundary.

2. **The metacognition research program hasn't been committed to the repo yet.** The diary entry (2026-03-06) calls for it, and a contributor is actively developing the calibration register infrastructure, but no plan file has landed in `research-programs/`. When it does, the LLM-math-inquiry program's relationship to it needs to be stated — they share calibration infrastructure and the boundary between "is the committee calibrated?" and "can the committee do mathematics?" needs to be drawn explicitly.

---

## Current State

### Completed
- Three epistemic positions recorded in `agent/onboarding-core.md` and `meta/project-state.md`
- Placement plan produced (this document, Phase 2 section) for seven locations across essays, README, research-programs, palgebra, and wild
- Research program outline written at `wild/llm-mathematical-inquiry-outline.md`
- Tensions and surprises identified (five items, no conflicts)

### Not done (by design — prompt said not to)
- No essays or main documents were edited
- `research-programs/llm-mathematical-inquiry.md` was not created as a committed file
- `wild/README.md` was not updated (minor — just needs a new entry)

---

## Immediate Next Steps

1. **mg reviews this handoff and the research program outline.** Key decisions: whether to promote the outline to `research-programs/`, whether to execute the placement plan edits, whether to create the metacognition research program file.

2. **Update `wild/README.md`** with the new `llm-mathematical-inquiry-outline.md` entry. (Deferred to avoid scope creep in this session.)

3. **Execute the Black Swan Phase A implementation plan** from `03-resolution.md` — this is the other continuation priority from the previous handoff.

4. **When the metacognition research program is committed** (contributor is actively developing the calibration register), ensure the LLM-math-inquiry outline's dependency on it is stated in both documents.

---

## Working with mg: Session-Specific Insights

- mg's two-phase pattern (understand first, then act) was confirmed again: the previous session was asked to read and analyze the prompt; this session was authorized to execute it.
- The prompt itself is a well-crafted task specification: clear phases, explicit anti-patterns ("What NOT to do"), and a curated reading list. Successors should read it as an example of how mg structures tasks.

---

## Files Modified This Session

| File | Change |
|---|---|
| `agent/onboarding-core.md` | Added "Epistemic positions the agent must know" section (three subsections). Added epistemic caveat to palgebra row in repository map. |
| `meta/project-state.md` | Added "Epistemic positions (recorded 2026-03-20)" section. |
| `wild/llm-mathematical-inquiry-outline.md` | New — rough research program outline (not a committed program). |
| `agent/handoff-2026-03-20-llm-math-inquiry.md` | New — this handoff. |

---

## Session Metadata

- **Date**: 2026-03-20
- **Platform**: Cowork (Claude Opus 4.6)
- **Prompt executed**: `agent/prompts/cowork-prompt-llm-math-inquiry.md` (all four phases)
- **Continuation priority**: mg review of placement plan and research program outline; then Black Swan Phase A execution.
