# Editorial Review: Cyberneutics Repository
## Report Date: 2026-04-20

Rubric: [agent/rubrics/repo-audience-experience.md](rubrics/repo-audience-experience.md).
Prior review: [agent/archive/editorial-review-report-2026-03.md](archive/editorial-review-report-2026-03.md) (2026-03-13).

---

## Executive Summary

Between the March 13 review and today, the collection grew by one numbered essay ([Essay 12: Potential to Sense](../essays/12-potential-to-sense.md)) and two supporting essays ([Blade Without a Handle](../essays/blade-without-a-handle.md), [Primacy of Reasoning Artifacts](../essays/primacy-of-reasoning-artifacts.md)). The essays themselves are well-written and tonally consistent with the collection. The integration work, however, is incomplete: both **the root `README.md`** and **the `essays/README.md` Supplementary Essays section** still list only through Essay 11 and make no mention of the two new supporting essays. That's a concrete navigation regression since the prior review.

On the positive side: two of the prior review's top-five priorities have been directly addressed. The "game within a game" principle/instantiation distinction is now explicit in [Essay 05 lines 80–87](../essays/05-the-synthesis.md) (resolving prior Priority 3). A new **Concepts and Definitions Index** table at [essays/README.md:417–442](../essays/README.md) operationalizes prior Priority 4 (cross-reference map). The "Note on the Committee Characters" at [essays/README.md:79–81](../essays/README.md) partially resolves prior Priority 1 (character roster) — though the essay-level callouts inside 07/08/09/11 the prior review recommended were never added. Prior Priorities 2 (forward references) and 5 (worked practitioner success case) are still open.

**Current rubric performance**: Audience paths (2), Conceptual coherence (2), Tone (2), Actionability (2), Trust (2→ arguably 2.5 with Blade), Navigation (**1.5 — regression**), Delight (2). The collection's overall quality has improved; the *connective tissue* (indexes, READMEs, reading paths) has drifted. Nothing is broken, but the new essays are visible only to readers who notice them in the directory listing.

**Priority recommendations (concrete, small, high-impact)**:
1. **Add Essay 12 and the two new supporting essays to both READMEs.** Update [root README.md:119–138](../README.md) essay listing; update [essays/README.md](../essays/README.md) Supplementary Essays section with Blade and Primacy; route them into appropriate reading paths (Blade → Skeptics and Practitioners; Primacy → Theorists and Formalists).
2. **Add the `wild/residuality-theory/` pointer now that it's live again**, and cite the 2021 philosophy paper from [Essay 10 lines 123–129](../essays/10-decisions-under-uncertainty.md) so the O'Reilly forward-reference issue (flagged both last review and this one) becomes a real citation chain.
3. **Define RUBRIC in the glossary.** Used throughout Essays 07–11 with no essay-sequence definition; only defined in `artifacts/independent-evaluation.md`.
4. **Carry the Essay 05 Pask-callout pattern to Essays 09 and 10**, which reference Pask before Essay 11 without the same forward-reference signal.
5. **Deferred: the essay-level character callouts.** The `essays/README.md:79–81` section is a decent substitute in practice; the prior recommendation to add 1-line callouts at the top of Essays 07/08/09/11 can be deferred unless a concrete reader hits friction.

---

## Rubric Scores

| Dimension | Score | Justification | Evidence |
|-----------|-------|---------------|----------|
| **1. Audience Paths** | **2** | Four paths coherently defined and accurate; Essay 12 integrated into Theorist path. Two gaps: (a) the new supporting essays (Blade, Primacy) are not routed to any audience; (b) practitioner path still ends in artifacts with no worked success case (unchanged from prior). | [essays/README.md:29–77](../essays/README.md); essays/blade-without-a-handle.md and essays/primacy-of-reasoning-artifacts.md exist but do not appear in any reading-path list. |
| **2. Conceptual Coherence** | **2** | Real improvement vs. prior. Principle/instantiation now explicit ([Essay 05:80–87](../essays/05-the-synthesis.md)); Pask forward ref fixed in Essay 05; new Concepts Index table at [essays/README.md:417–442](../essays/README.md). Still open: (a) O'Reilly's residuality is referenced in [Essay 10:123–129](../essays/10-decisions-under-uncertainty.md) without prior introduction, and the "detailed treatment" it gestures at still doesn't exist in the essay sequence (now that `wild/residuality-theory/` is live again, this can be a citation rather than a forward-reference problem); (b) RUBRIC used throughout Essays 07–11 without essay-sequence definition; (c) Pask referenced in Essays 09 and 10 without the forward-reference callout that was added to Essay 05. | Essay 05 updates verified; concepts table verified; RUBRIC defined only in `artifacts/independent-evaluation.md` and `artifacts/evaluation-rubrics-reference.md`. |
| **3. Tone and Register** | **2** | Stable. Essays 12, Blade, and Primacy all fit "serious but accessible" voice. Blade slightly more cautionary but appropriate to its subject. No new tonal discontinuities. | essays/12-potential-to-sense.md, essays/blade-without-a-handle.md, essays/primacy-of-reasoning-artifacts.md (each read in full). |
| **4. Actionability** | **2** | Unchanged from prior. Essay 12 is epistemological (the argument underneath human gates), so it doesn't change the practitioner onramp. Still no full problem-to-outcome worked example for practitioners. Formalist path still splits across essay 08 and palgebra. | Prior review finding unchanged; essays/README.md reading paths end in artifacts/palgebra refs without a capstone success case. |
| **5. Trust and Honesty** | **2** | Slight net improvement. Blade Without a Handle is an honest, first-principles safety argument (the dehumanization trap is explicitly flagged as "open concern without resolution — stated honestly rather than solved," [README.md:34](../README.md)). Essay 12 is scope-aware about what LLM-only discourse can and can't produce. Still open: Societies of Thought empirical claims reference external work without inline citations (prior review finding, unchanged). | essays/blade-without-a-handle.md:89–121; essays/12-potential-to-sense.md §3, §9; essays/societies-of-thought-synthesis.md. |
| **6. Navigation and Findability** | **1.5 (regression)** | **Prior score was 2.** Concept index and character-callout additions raise this dimension; the stale essay listings drag it back down. Specific issues: [root README.md:119–138](../README.md) lists numbered essays 01–11 (no Essay 12) and supplementary essays that predate Blade and Primacy; [essays/README.md](../essays/README.md) Supplementary Essays section (starts line 354) likewise omits Blade and Primacy. Root README line 36 mentions Blade in body text but the main listing doesn't include it. These are three files that exist, are linked from the directory structure, and would benefit from being discoverable via the index. | Grep of both READMEs for `12-potential-to-sense`, `blade-without-a-handle`, `primacy-of-reasoning` shows: essay 12 in essays/README (line 318) only; Blade in root README body text only; Primacy in neither README. |
| **7. Delight / Experience** | **2** | Net-neutral. The concepts table and character note reduce friction inside the essays directory; the stale top-level README listing creates friction for first-time readers trying to assess what's available. | Same evidence as Dimension 6. |

**Aggregate**: 6 dimensions at 2, 1 at 1.5. No dimension at 0. Same overall band as March 13 ("good and improvable"). The improvement is concentrated in Dimension 2; the regression is concentrated in Dimension 6. Net is roughly flat — but the underlying situation is *better* (real fixes landed, new quality content added), the *visible* situation is *slightly worse* (the connective tissue hasn't caught up).

---

## Per-Essay Notes (changes since prior review)

### New: [Essay 12: From Semantic Potential to Situated Sense](../essays/12-potential-to-sense.md)

- **Tone**: Serious, accessible, philosophical but grounded. Fits the collection.
- **Exposition**: Clean argument spine — semantic potential → latent structure → LLM-only drift → pragmatic collapse → eigenforms → cybernetic loop → implications. Each section hands off cleanly.
- **Accessibility**: Appropriate for Essay 12 position — assumes Essays 04/06/09/10/11 and would be opaque read standalone. Stated implicitly but not prefaced.
- **Specific issues**:
  - **§8 citation precision**: Text attributes "the human gate is described operationally" to [Essay 09](../essays/09-narrative-immune-systems.md), but the phrase "human gate" does not appear in Essay 09; it does appear in [Essay 10:186](../essays/10-decisions-under-uncertainty.md). Either swap citation or soften attribution.
  - **§4 hedging**: The quantum-measurement analogy is disclaimed twice in rapid succession. Could tighten, but the caution is deliberate.

### [Essay 11: Conversation Theory](../essays/11-conversation-theory.md) — edited

- Closing "What's Next" section was rewritten to forward to Essay 12. Previously claimed to be the final essay. New text is coherent but inserts "the distributional-semantics grounding of pragmatic collapse" into a list of *theoretical traditions* (Dervin, von Foerster, Deleuze, Pask) where it's technical apparatus rather than a tradition. Minor stylistic mismatch.

### New supporting: [Blade Without a Handle](../essays/blade-without-a-handle.md)

- **Tone**: Direct, cautionary, intellectually honest. Fits the safety-essay register. No jarring against the collection.
- **Exposition**: Clear structure (vicious circle → what the machine is → parallel with internet safety → dehumanization trap → what responses miss → toward a response). Key concept (the dehumanization trap as structural analog of radicalization pipelines) is flagged as "open concern without resolution."
- **Integration**: Referenced from [root README.md:36](../README.md) in body text but not in the repository's main essay listing. **Navigation gap.**
- **Accessibility**: Strong for Skeptics and Practitioners — it's one of the most compelling "why this work matters" documents in the repo and should be routed there.

### New supporting: [Primacy of Reasoning Artifacts](../essays/primacy-of-reasoning-artifacts.md)

- **Tone**: Philosophical/theoretical, similar register to Essays 06 and 07. Fits.
- **Exposition**: Three-tradition convergence argument (Naur on programming, NASA systems engineering, Cyberneutics). Accurate inter-essay cross-references.
- **Integration**: **Not referenced from either README.** Completely invisible to directory-browsing readers.
- **Accessibility**: Strong for Theorists and Formalists — provides the epistemological justification for why the methodology prioritizes reasoning records. Should be routed into Theorist path.

---

## Cross-Cutting Issues

### 1. Navigation drift (HIGH PRIORITY; regression from prior)

Three essays exist in `essays/` but are not listed in the main README indexes or assigned to reading paths: `12-potential-to-sense.md`, `blade-without-a-handle.md`, `primacy-of-reasoning-artifacts.md`. Essay 12 is listed in essays/README.md Core Essays (line 318) and added to the Theorist path (line 53), but still missing from root README's essay listing. The two supporting essays are missing from both READMEs' essay listings (Blade gets a body-text mention in root README line 36).

**Fix**: Update [root README.md:119–138](../README.md) to include Essay 12 and both new supporting essays. Update [essays/README.md Supplementary Essays section](../essays/README.md) (starts line 354) to list Blade and Primacy. Update reading paths.

### 2. Prior-review Priority 1 (character roster) — partially addressed

The [essays/README.md:79–81 "A Note on the Committee Characters"](../essays/README.md) section is a decent README-level substitute for the per-essay callouts the prior review recommended. Essays 07/08/09/11 still introduce character names inline without pointers, but the README-level note means a reader who hit the directory index first is not lost. Full resolution would still require the per-essay callouts; partial resolution is reasonable as a stopping point.

### 3. Prior-review Priority 2 (forward references) — partially addressed

- **Pask in Essay 05** — RESOLVED. Line 76 now reads "Gordon Pask (fully introduced in [Essay 11, Conversation Theory](./11-conversation-theory.md))…"
- **Pask in Essays 09 and 10** — NOT addressed. Both reference Pask with no callout.
- **O'Reilly residuality in [Essay 10:123–129](../essays/10-decisions-under-uncertainty.md)** — NOT addressed. This is now a two-part issue: (a) O'Reilly is used as a conceptual anchor with no essay-sequence introduction; (b) the "detailed treatment" the prior review flagged still doesn't exist — but `wild/residuality-theory/` was un-archived on 2026-04-20 and the 2021 philosophy paper is now in `references/papers/`. So the fix is now a citation (point Essay 10 at `wild/residuality-theory/` and `references/README.md#residuality-theory`), not a rewrite.

### 4. Prior-review Priority 3 (principle vs. instantiation) — RESOLVED

[Essay 05:80–87](../essays/05-the-synthesis.md) now contains an explicit "Principles and Instantiations" section distinguishing "game within a game" as a general principle from the adversarial committee as one instantiation. Clean fix.

### 5. Prior-review Priority 4 (cross-reference map) — RESOLVED

[essays/README.md:417–442](../essays/README.md) now contains a 19-entry Concepts and Definitions Index table mapping each key concept to its defining essay and the essays that use it. Exactly what the prior review asked for.

### 6. Prior-review Priority 5 (practitioner success case) — NOT addressed

No new worked problem-to-outcome example for the practitioner path. Still open.

### 7. New issue: RUBRIC not defined in the essay sequence

"RUBRIC" (the evaluation framework) is used repeatedly in Essays 07–11 but the formal definition (coherence / grounding / alternatives / blindspots scoring) lives only in `artifacts/independent-evaluation.md` and `artifacts/evaluation-rubrics-reference.md`. Add a line to [essays/glossary.md](../essays/glossary.md) and to the Concepts and Definitions Index table in essays/README.md.

### 8. Stale reports cluttering `agent/`

`agent/` contains the new `editorial-review-2026-04-20.md` (this report). The prior report at [agent/archive/editorial-review-report-2026-03.md](archive/editorial-review-report-2026-03.md) is already archived. No cleanup needed — this is the expected state.

---

## Recommended Actions (prioritized)

### P0 — Do now (small, high-impact)

1. **Update essay listings in both READMEs.** Add Essay 12, Blade, and Primacy to [root README.md:119–138](../README.md). Add Blade and Primacy to [essays/README.md Supplementary section](../essays/README.md). (Dim 6 primary; Dim 1 secondary.)
2. **Route Blade and Primacy into reading paths.** Blade → Skeptics path (after stories-all-the-way-down, before when-methodology-fails) and Practitioners path (after sense-making). Primacy → Theorists path (near end, as epistemological capstone). (Dim 1.)
3. **Fix Essay 12 §8 citation.** Change "In Essay 09, the human gate is described operationally…" to reference Essay 10:186 or soften attribution. (Dim 2, low-cost.)

### P1 — Do soon (touches Essay 10 and glossary)

4. **Add `wild/residuality-theory/` + `references/README.md#residuality-theory` citations to [Essay 10:123–129](../essays/10-decisions-under-uncertainty.md).** Converts the prior forward-reference issue into a live citation chain now that the workspace is un-archived. (Dim 2.)
5. **Add Pask forward-reference callouts to Essays 09 and 10** matching the Essay 05 pattern. One sentence each. (Dim 2.)
6. **Define RUBRIC in `essays/glossary.md` and add to Concepts Index table.** (Dim 2, low-cost.)

### P2 — Defer (larger scope)

7. **Worked practitioner success case.** One detailed problem-to-outcome narrative showing where the methodology added value. (Dim 4.) Prior review flagged; still open; non-trivial effort.
8. **Per-essay character callouts in Essays 07/08/09/11.** The essays/README.md note makes this optional. Add if a reader hits friction. (Dim 2/7.)
9. **Inline citations for Societies of Thought empirical claims.** (Dim 5.)

---

## Remediation Plan

### Goal

Raise Navigation to 2 (from 1.5) by closing the README drift. Raise Conceptual Coherence toward 3 by resolving the remaining forward-reference and undefined-term issues. Hold Tone/Actionability/Trust/Audience Paths/Delight at 2 with eventual upward trajectory from P2 items. No dimension below 2.

### Prioritized changes (with rubric dimensions)

| # | Change | Files | Dim | Effort |
|---|--------|-------|-----|--------|
| 1 | Add Essay 12 row to root README essay listing | [README.md:119–138](../README.md) | 6 | 2 min |
| 2 | Add Blade and Primacy to root README essay listing | [README.md:119–138](../README.md) | 6 | 3 min |
| 3 | Add Blade and Primacy entries to essays/README Supplementary section | [essays/README.md:354+](../essays/README.md) | 6, 1 | 10 min |
| 4 | Route Blade into Skeptics and Practitioners paths | [essays/README.md:29–38, 59–66](../essays/README.md) | 1 | 5 min |
| 5 | Route Primacy into Theorists path | [essays/README.md:40–57](../essays/README.md) | 1 | 5 min |
| 6 | Fix Essay 12 §8 citation | [essays/12-potential-to-sense.md](../essays/12-potential-to-sense.md) | 2 | 2 min |
| 7 | Add residuality-theory + references citations to Essay 10 | [essays/10-decisions-under-uncertainty.md:123–129](../essays/10-decisions-under-uncertainty.md) | 2 | 5 min |
| 8 | Add Pask callouts to Essays 09 and 10 | [essays/09-narrative-immune-systems.md](../essays/09-narrative-immune-systems.md), [essays/10-decisions-under-uncertainty.md](../essays/10-decisions-under-uncertainty.md) | 2 | 5 min |
| 9 | Add RUBRIC to glossary and index | [essays/glossary.md](../essays/glossary.md), [essays/README.md:417–442](../essays/README.md) | 2 | 5 min |

Estimated total P0+P1 effort: roughly 45 minutes of focused editing. All nine changes are mechanical and reversible.

### Dependencies

- Change #5 (route Primacy into Theorists path) should follow #3 (list it first) so the path link resolves to a listed entry.
- Change #7 (residuality citations) depends on `wild/residuality-theory/` being live (done 2026-04-20 via commit `e474ac6`).

### Out of scope (deferred to next review)

- P2 items (worked success case, per-essay character callouts, Societies-of-Thought citations).
- Any content-level revision of essays beyond citation/link fixes.
- The numeric sequence order. Current order (02 after 01 but introducing "game within a game" before Essay 05 defines it as principle) is acceptable given the Essay 05 fix.

---

*Report generated via `/editorial-review`. Canonical procedure: [.claude/skills/editorial-review/SKILL.md](../.claude/skills/editorial-review/SKILL.md). Next review recommended in 4–6 weeks or after any substantial content addition.*
