# Prompt for Claude Code: promote potential-to-sense, handle residuality bookkeeping

This is a set of file moves and edits. Each step is mechanical; do not introduce theoretical content of your own. If you encounter an ambiguity, stop and ask rather than guess.

## Context

Two things are happening at once:
1. Promoting `wild/potential-to-sense/` into the essays series as essay 12.
2. Some bookkeeping around the residuality theory PDF that was recently placed in `references/` and related bibliography updates.

The essay 12 draft is provided separately (attached as `12-potential-to-sense.md` for you to place). The diary entry for residuality is also provided separately (attached as `2026-04-20-residuality-philosophy-paper-reading.md`).

## Step 1: Place the new files

1. **Place the essay.** Copy the provided `12-potential-to-sense.md` into `essays/12-potential-to-sense.md`. Do not modify its contents.

2. **Place the diary entry.** Copy the provided `2026-04-20-residuality-philosophy-paper-reading.md` into `wild/diary/2026-04-20-residuality-philosophy-paper-reading.md`. Do not modify its contents.

## Step 2: Restructure references/ to accommodate papers

The existing `references/` directory contains annotated markdown surveys and reports. A PDF (`The-Philosophy-of-Residuality-Theory.pdf`) was recently added, which creates a mixed character. Clean this up:

1. **`references/papers/`** is already a subdirectory.
2. **It contains only `references/papers/The-Philosophy-of-Residuality-Theory.pdf`.
3. **Create `references/papers/README.md`** with the following content exactly:

   ```markdown
   # references/papers/

   Archived copies of papers cited elsewhere in the Cyberneutics repository, kept here because the source pages can be hard to find or behind paywalls. Papers are included under their original licenses — check each paper's copyright page for redistribution terms.

   Annotations and citations for these papers live in [../README.md](../README.md). This directory is storage; the bibliography is next door.

   ## Current contents

   - **The-Philosophy-of-Residuality-Theory.pdf** — Barry M. O'Reilly, "The Philosophy of Residuality Theory." *Procedia Computer Science* 184 (2021): 809–816. Licensed under CC BY-NC-ND 4.0. Proceedings of the 8th International Workshop on Computational Antifragility and Antifragile Engineering.
   ```

## Step 3: Add the Residuality Theory section to references/README.md

Open `references/README.md`. Find the existing `## Systems & Life` section (which currently contains a single entry for Robert Rosen's *Life Itself*). Immediately *after* that section, and *before* the `## AI & LLMs` section, insert a new section with the following content exactly:

```markdown
## Residuality Theory

**O'Reilly, Barry M.** "An Introduction to Residuality Theory: Software Design Heuristics for Complex Systems." *Procedia Computer Science* 170 (2020): 875–880. — The operational paper: incidence matrix technique, K-reduction heuristics, training/test holdout protocol. Provides the concrete method that the philosophy paper (below) grounds. Cited in: [Decisions Under Uncertainty](../essays/10-decisions-under-uncertainty.md), [Conversation Theory](../essays/11-conversation-theory.md), [wild/residuality-theory/](../wild/residuality-theory/).

**O'Reilly, Barry M.** "The Philosophy of Residuality Theory." *Procedia Computer Science* 184 (2021): 809–816. — The philosophical counterpart to the 2020 introduction. Introduces *residual causality*: structure itself imposes future-destroying constraints that cannot be predicted at design time. Targets the "component metaphor" (essentialism, causalities of certainty, cybernetics, structuralism) as the philosophical commitments that produce fragile architectures. Anchors its post-structural move in Serres (via Brown 2002) and Latour rather than Deleuze. Open access under CC BY-NC-ND; archived copy at [papers/The-Philosophy-of-Residuality-Theory.pdf](papers/The-Philosophy-of-Residuality-Theory.pdf). Cited in: [wild/diary/2026-04-20-residuality-philosophy-paper-reading.md](../wild/diary/2026-04-20-residuality-philosophy-paper-reading.md), [wild/residuality-theory/](../wild/residuality-theory/).

**O'Reilly, Barry M.** "Residuality and Representation: Toward a Coherent Philosophy of Software Architecture." *Procedia Computer Science* 224 (2023): 91–97. — Revised restatement of the 2021 philosophy paper, reorganized around three concepts: processuality, criticality, and difference. Expanded post-structural lineage (Kant, Deleuze, Derrida) compared to the 2021 paper's focus on Serres and Latour. Cited in: [wild/residuality-theory/](../wild/residuality-theory/).

**Normand, Eric.** "Residuality Theory." Eric Normand's Newsletter (Substack), May 2024. https://ericnormand.substack.com/p/residuality-theory — Practitioner introduction with a worked example (country-based coupon banner service); the clearest pedagogical on-ramp to the operational machinery. Cited in: [wild/diary/2026-04-20-residuality-philosophy-paper-reading.md](../wild/diary/2026-04-20-residuality-philosophy-paper-reading.md).

**Brown, Steven D.** "Michel Serres: Science, translation and the logic of the parasite." *Theory, Culture & Society* 19(3) (2002): 1–27. — The Serres interpretation O'Reilly (2021) cites for residuality's post-structural grounding. Serres on noise, modeling, external influence, and translation; the substantive post-structural anchor for residuality theory. Cited in: [wild/diary/2026-04-20-residuality-philosophy-paper-reading.md](../wild/diary/2026-04-20-residuality-philosophy-paper-reading.md).

**Stacey, Ralph D.** *Complexity and Organizational Reality: Uncertainty and the Need to Rethink Management after the Collapse of Investment Capitalism.* 2nd ed. Routledge, 2009. — Load-bearing citation underneath O'Reilly's philosophy of residuality. The three causalities of certainty (formative, rationalist, efficient) plus adaptionist and transformative; the "dominant discourse of management" critique. Directly relevant to the Cyberneutics argument that expected-utility decision theory fails under genuine uncertainty. Cited in: [wild/diary/2026-04-20-residuality-philosophy-paper-reading.md](../wild/diary/2026-04-20-residuality-philosophy-paper-reading.md).
```

Do not modify any other section of `references/README.md`. Do not renumber or reorder existing entries.

## Step 4: Update wild/residuality-theory/README.md to note the new reading

This step is optional and only if `wild/residuality-theory/README.md` exists and contains a section labeled something like "Status" or "Notes" at the top.

If such a section exists, append a single bullet to it noting: "2026-04-20: Full text of the 2021 philosophy paper now in the repository (see [references/papers/](../../references/papers/)); diary entry at [wild/diary/2026-04-20-residuality-philosophy-paper-reading.md](../diary/2026-04-20-residuality-philosophy-paper-reading.md)."

If the file structure does not clearly accommodate this addition, skip this step and flag it for later manual handling.

## Step 5: Update essay 11's "final essay" claim

Open `essays/11-conversation-theory.md`. Find the section heading `## What's Next` (it appears near the end of the file). The first paragraph under that heading currently begins:

> This is the final essay in the theoretical sequence. The eleven numbered essays establish...

Replace that sentence with:

> The theoretical sequence continues in [Essay 12](./12-potential-to-sense.md), which develops the epistemology of meaning-as-conversation that the pipeline's human gates operationalize. The twelve numbered essays together establish...

and adjust the rest of the paragraph accordingly — specifically, change "four theoretical traditions" language if it appears, and ensure the sentence reads coherently after the replacement.

Also: at the very bottom of essay 11, there is a line reading `**Previous essay**: [Decisions Under Uncertainty](./10-decisions-under-uncertainty.md)—the composed pipeline that Conversation Theory provides micro-mechanics for.`

Immediately after this line, add:

```markdown
**Next essay**: [From Semantic Potential to Situated Sense](./12-potential-to-sense.md) — the epistemology that explains why pipeline human gates are irreducible, not merely prudent.
```

## Step 6: Update essays/README.md

Open `essays/README.md`. Four specific edits, in order:

**Edit 6a** — In the Reading Time Estimates table, update the "Full numbered sequence" row:
- Change `Full numbered sequence (01–11) | All 11 | ~120 minutes` to `Full numbered sequence (01–12) | All 12 | ~130 minutes`.

**Edit 6b** — In the "For Theorists (Deep Dive)" reading path, after the current item 9 (Decisions Under Uncertainty), add a new item 10:

```markdown
10. **[From Semantic Potential to Situated Sense](./12-potential-to-sense.md)** (~15 min) - Why meaning in LLM interaction is co-produced, not extracted: the epistemology of pragmatic collapse and temporary eigenforms in coupled human-machine conversation
```

**Edit 6c** — In the "Core Essays" section, find the entry for Essay 11 (Conversation Theory). Immediately after Essay 11's entry (which ends before the next `---` separator), add a new entry in the same format used for the other essays:

```markdown
---

### [From Semantic Potential to Situated Sense](./12-potential-to-sense.md)

**The epistemology of pragmatic collapse**: LLMs maintain structured fields of semantic potential, not stored meanings. Human participation — with its purposes, corrections, embodied associations, and stakes — is what converts potential into situated sense. Meaning is a temporary eigenform of the coupled conversation, not a property of either participant alone.

**Key insight**: The unit of analysis for questions about meaning in human-LLM interaction is the interaction itself, not the model and not the user. The cybernetic control loop of prompt-proposal-feedback is where meaning actually stabilizes.

**Covers**:
- Distributional semantics and semantic potential fields
- Concepts as latent relational structure, not stored packets
- LLM-only discourse as exploration of state space (with attractors and degeneracies)
- Human participation as pragmatic collapse
- Pask, Berea, and von Foerster on meaning through recursive conversation
- Against the container model of meaning
- A cybernetic model of human-LLM interaction
- Implications for AI theory, interface design, epistemology, and multi-agent systems

**Read this if**: You want the theoretical grounding for why pipeline human gates are load-bearing rather than ornamental, and why LLM-only discourse drifts without them.
```

**Edit 6d** — If there is a note elsewhere in `essays/README.md` claiming that 11 is the last numbered essay, update it to reflect 12 as the current last.

## Step 7: Flag anything weird

If you encounter any of the following, stop and report rather than proceed:
- `essays/12-potential-to-sense.md` already exists
- `references/papers/` already exists with conflicting contents
- The specific text snippets quoted above (e.g. "This is the final essay in the theoretical sequence") do not match what you find in the files
- Any step would require editing more than the specifically named files

## What not to do

- Do not touch any essay other than 11 (for the single edit described) and 12 (for placement).
- Do not update artifacts/, palgebra/, applications/, or research-programs/ in this pass.
- Do not update `wild/potential-to-sense/` — leave the wild version in place as the source of record.
- Do not generate any new essay content, diary content, or bibliography annotations beyond what is specified above.
- Do not run any `git` commands; leave the changes staged for review.
