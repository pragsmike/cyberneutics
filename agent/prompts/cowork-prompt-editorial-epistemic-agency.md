# Cowork Task: Editorial — Epistemic Status and LLM-Agency Language Audit

**Context**: A diary entry (2026-03-25) identified two editorial actions that affect how casual browsers perceive the repo. Both concern the repo's self-presentation to people who arrive without context.

**Priority**: These are public-facing credibility issues, not internal housekeeping. Get them right.

---

## Action 1: Strengthen epistemic status disclaimers on formal work

### What's already done

The palgebra README already has an epistemic status block:

> **Epistemic status**: The constructions here are provisionally useful for organizing thinking about LLM pipelines, but they have not been reviewed by domain experts in category theory. They should be treated as working hypotheses, not established results.

The root README already has a parenthetical on the palgebra line in the "What's in this repository?" section:

> (currently at working-hypothesis status pending expert review; see LLM-mathematical-inquiry outline)

`agent/onboarding-core.md` already has a section "Epistemic positions the agent must know" covering this.

### What's missing

The **root README** needs a more prominent statement — not buried in a parenthetical in the file listing, but visible in the opening sections where a casual browser forms their first impression. The current opening ("collaborative sense-making partners") jumps straight into methodology claims. Someone arriving from an ACT community link needs to see within the first scroll that the formal work is exploratory and LLM-assisted.

**Suggested placement**: After the "What is Cyberneutics?" section or within it. A short, honest paragraph — not a disclaimer wall. Something that says: the methodology is grounded in engineering practice; the formal connections to category theory are the author's attempt to understand why the architecture works; that formalization is exploratory, generated in collaboration with LLMs, and has not been validated by domain experts; outreach to ACT practitioners is the intended validation path.

**Tone**: Confident about the engineering, honest about the math. Not self-deprecating — "we know what we have and what we don't have yet."

### Also check

- `wild/committee-games/README.md` — the open games translation. No epistemic caveat was visible in earlier reviews. Add one if still missing.
- `wild/fuzzy-type-theory/README.md` — same check.
- Any other `wild/` README that presents formal categorical content without an epistemic status note.

---

## Action 2: Audit and revise LLM-agency language

### The problem

The repo's core claim is that LLM outputs need inspectable reasoning chains *because* LLMs are unreliable narrators. But some introductory language implies partnership or agency in ways that undercut this message. A reader encountering "collaborative sense-making partners" alongside "storytelling machines" receives a mixed signal.

The intent behind "partner" language is affectionate and pragmatic — like saying "my books are my friends." It's not a claim that machines are people. But casual browsers don't have that context, and the language can be misconstrued.

### What to audit

Search the following files for language that implies LLM agency, partnership, or collaborative relationship in ways that could be read as attributing judgment or reliability to the machine:

**Primary targets (public-facing, high-traffic)**:
1. `README.md` — "collaborative sense-making partners" in the opening definition
2. `essays/01-why-narrative-engines-change-everything.md` — "Collaborative sense-making partners that help us think better" near the end
3. `agent/onboarding-core.md` — "collaborative sense-making partners" in the "What this repo is" section

**Secondary targets (check but may not need changes)**:
4. `essays/02-from-practice-to-theory.md`
5. `essays/03-sensemaking-101.md`
6. `essays/stories-all-the-way-down.md`
7. `wild/potential-to-sense/from_semantic_potential_to_situated_sense.md`

**Archive files**: Don't modify. They're historical.

### What NOT to do

- Don't mechanically find-and-replace "partner" everywhere. Some uses are fine in context (e.g., "collaborative participant in a cybernetic sense-making loop" in the Stochastic Imps essay is appropriate — it's describing the loop structure, not attributing agency).
- Don't strip all warmth from the language. The repo has a distinctive voice. The goal is precision, not sterility.
- Don't add lengthy disclaimers. A phrase-level revision is usually sufficient.

### Guidance on replacements

The core reframe: the human does the thinking; the LLM provides material to think *with*. The value is in the human's cognitive process (exploring scenarios, evaluating arguments, noticing gaps), not in the machine's output.

Useful framings already in the repo:
- "narrative engines" / "storytelling machines" (established vocabulary)
- "narrative generators" (used in root README)
- "rapid story generators that help us navigate complexity" (root README)
- The Eisenhower principle: "Plans are useless, but planning is essential" — the process is the product

The rubber-duck framing from the diary entry: LLMs are like rubber ducks that talk back — explaining the problem to them forces you to put it into words, and they bring in threads you hadn't considered, but the conclusions are yours. This framing may or may not belong in the repo text, but it captures the right epistemics.

Possible replacement for "collaborative sense-making partners": something like "structured sense-making tools" or "narrative engines harnessed for structured deliberation" or simply drop the anthropomorphizing and describe what the methodology does rather than what the LLM is.

### Deliverable

For each file audited:
- List the specific phrases found
- State whether each needs revision, and why or why not
- Provide the revised text for any that need changing
- Make the edits

Write a summary of all changes made, suitable for inclusion in a handoff.

---

## Reading list for context

Before starting, read:
1. The most recent handoff in `agent/` (for current repo state)
2. `agent/onboarding-core.md` section "Epistemic positions the agent must know"
3. `wild/diary/2026-03-25-language-epistemology-sensemaking.md` — the diary entry that prompted this task (the "Bogdanov problem" and "rubber ducks" sections are the rationale)
4. The root `README.md` (the primary public-facing document)
5. `palgebra/README.md` (the existing epistemic status block — use as a tone model)

---

## Constraints

- **Additive where possible**: Prefer adding a paragraph or sentence over rewriting existing prose, unless the existing prose is actively misleading.
- **Preserve voice**: The repo has a distinctive register — direct, slightly irreverent, intellectually honest. Match it.
- **Don't touch archive/**: Historical files are historical.
- **Don't touch essays that are working well**: If an essay uses "partner" language in a context where it's clearly about loop dynamics (not LLM agency), leave it alone and note why in your audit.
- **Commit nothing**: Produce the edits. mg will review and commit.
