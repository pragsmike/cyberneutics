---
title: "File-by-file edit plan: book-integration execution"
type: edit-plan
audience: "An agent (or mg) executing the book-integration changes"
created: 2026-04-26
status: "Plan only. Not executed. Companion to book-integration-plan.md (which organises by phase). This document organises by file and pins the editorial register per file."
parent_plan: book-integration-plan.md
---

# File-by-file edit plan

This is the execution-side companion to [`book-integration-plan.md`](book-integration-plan.md). The parent plan organises by phase (what changes conceptually); this plan organises by surface (what gets edited where, in what order, with what dependencies, in what register).

If you are executing: read the parent plan once for the conceptual map, then work file-by-file from this document. Mark each file's checklist items as you complete them.

## Execution-order summary

```
1. survey: state-of-residuality-2026.md          (largest surface; everything else references it)
2. bibliography: residuality-bibliography.md      (independent; can run in parallel with 1)
3. working note: cyberneutics-and-residuality.md  (depends on 1; needs Phase 1 re-check first)
4. working note: fan-as-stressor-generator.md     (depends on 1; small surface)
5. working note: assemblage-rhizome-nomad.md      (depends on 1; surfaces falsifier work)
6. README: wild/residuality-theory/README.md      (index update; depends on 1–5)
7. essay-13-readiness-plan.md                     (logs Phase 1 re-check + scope shift)
8. meta/project-state.md                          (logs the integration work as a whole)
```

Steps 1 and 2 can run in parallel. Steps 3, 4, 5 can run in parallel after 1 lands. Steps 6, 7, 8 sequence after the substantive work is done.

## Pre-execution gate: Phase 1 stability-window re-check

**Do this first.** Before any survey or working-note edits, complete the bilateral-note re-check from Phase 1 of the parent plan:

- Re-read [`cyberneutics-and-residuality.md`](cyberneutics-and-residuality.md) §2.4 ("two-step algorithm extended to sense-making generally") against the book's "stressor analysis + contagion analysis" framing.
- Decide: does the generalization claim survive the renaming, or does the contagion-vocabulary reframing change the substance?
- Record the result as a new subsection in [`essay-13-readiness-plan.md`](essay-13-readiness-plan.md) titled "Stability re-check 2026-04," stating either:
  - **"No flip — generalization claim survives renaming."** Continue to file 1 below.
  - **"Flip — restart 9b on YYYY-MM-DD."** Stop. Do not proceed with the substantive edits until 9b's window re-closes. Log the restart and notify mg.

The remaining edit plan assumes "no flip." If "flip," only step 7 (logging) and step 2 (bibliography, which is independent) should run.

---

## File 1 — `state-of-residuality-2026.md`

**Register**: third-person survey, neutral, paper-grounded with book as supplementary citation. The book's polemical voice ("nailing horseshoes to car tires") is **described**, not adopted. Quotations short, fair-use, attributed by chapter/subsection (no page numbers).

**Total surface**: ~5 substantive content additions + new section + provenance rewrite. Estimated ~1,200–1,800 net words added.

### Edit 1.1 — §3 (Hyperliminality): add ergodicity (A1)

Insert 1–2 paragraphs naming ergodicity as the property that makes the ordered/disordered distinction sharp. Cite as: book introduces ergodicity as the term that makes hyperliminality falsifiable in a way the papers' "complex environment" framing does not. Quote the book's definition briefly ("Ergodicity is the property of having a future that is already expressed in the past of a particular system…") and frame hyperliminality precisely as "a complicated, ergodic, ordered system executes inside a complex, non-ergodic, disordered context."

### Edit 1.2 — §6 (Residues and the stressor-driven design process): three additions

(a) **Robust software inside residual architecture (A2)** — new ~150-word subsection. The book separates *complicated software inside a residue* (which should be robust) from *the architectural envelope across residues* (which should be residual). Quote the book's "Software should be robust but its architecture should be residual" line.

(b) **Stressors-vs-X taxonomy (A3)** — new ~250–400-word subsection. Contrastive definitions distinguishing stressors from requirements, constraints, edge cases, scenarios, risks, volatility, chaos engineering, resilience. Sourced from book's "Stressors, Requirements, Risks, Scenarios, and Edge Cases" subsection. Survey-register prose; do not copy the book's structure verbatim.

(c) **Flow analysis as pre-stressor step (A6)** — one paragraph. Flows replace process/use-case mapping; cite Parnas (1971) per the book.

### Edit 1.3 — §6 or §8: add ICE-ing + AFIR worked-example punchline (A9)

One paragraph illustrating looping/criticality with the book's EV-charger example. The 2014-designed system survives EU AFIR 2023 regulation without architectural change because the failed-key-fob residue had decoupled membership from charging. This is the corpus's single best concrete demonstration of the looping phenomenon.

### Edit 1.4 — §8 (Ri and per-project falsifiability): note the cross-project significance claim (B2)

Add a short paragraph: the book asserts "experiments carried out thus far have revealed a statistically significant effect" across projects. This is an *advance over the corpus* — the papers stop at per-project Ri. Note that the underlying study is not publicly available as of 2026-04 (per Phase 0). Survey-register, not editorialised.

### Edit 1.5 — §9 (Processuality, criticality, difference): linear vs lateral (A4) + lateral as cognitive style (B5)

One short subsection (~150 words) treating linear-vs-lateral as the cognitive distinction the book makes load-bearing, and noting B5 (the book repositions residuality as cognitive style, not just methodology). The cyberneutics relevance is obvious but should not be elaborated here — that's the bilateral note's job.

### Edit 1.6 — §10 (Limits): expand with book's defences AND newly-grounded criticism

Two clusters of additions:

**Defences O'Reilly has prepared (per Phase 4 of parent plan)**:
- B4 (residuality vs. resilience: residuality moves between attractors; resilience stays in or returns to a fixed range)
- B3 (NFR claim: book asserts NFRs are not discoverable except by random simulation — flag as one of the more controversial claims)
- B6 (case-study refusal as methodological stance, defended)
- A8 (under-engineering diagnosis and structural-determinism critique)

**Newly-grounded criticism from Phase 0**:
- Empirical claim publicly unverifiable as of 2026-04 (the most substantive open question; sympathetic but honest framing)
- Reviewer-noted abstractness/rigor concerns (Goodreads cluster; cite Nicola 2025-01-03 "very abstract and not rigorous," Travis 2025-02-13 "half baked")
- Eric Normand's naming objection ("It's a terrible name")

Each criticism gets one or two sentences. Survey is reporting reception, not endorsing it.

### Edit 1.7 — New section between §11 and §12: "The 2024 book"

This is the largest single addition. Estimated ~600–900 words. Sub-structure:

1. **Framing**: book as practitioner-pitched compression of the corpus, post-2023 papers, paid Leanpub artefact, ~85pp.
2. **What the book adds beyond the papers**: A4 (linear/lateral if not folded into §9), A5 (PESTLE / BMC / 5-Forces), A7 (safety nets framing — the layered process as defence-in-depth), A10 (the seven heuristics list, **quoted in full** per fair use — short list, high signal).
3. **Tone shift to polemic** (C1): describe the book's register; cite the "nailing horseshoes to car tires" and "comfort blanket for STEM graduates" phrases as register-evidence; do not adopt the voice.
4. **What the book omits relative to the papers**: C5 (Beer/VSM critique softened to diffuse anti-structuralism), C6 (no residual-causality chapter, political framing of *Machine in the Ghost* absent), C7 (Naur, Pask, Cilliers all absent — note these connections remain cyberneutics-side; cross-reference the bilateral note).
5. **Forthcoming material** (C2 + D6): PhD thesis announced as forthcoming (June 2024 book Conclusion); promised "longer version" of the book. Phase 0 status: thesis announced + 2022/2024 self-identification as PhD student in complexity science (Stockholm), not publicly indexed at search date. Longer version not yet appeared.
6. **Reception** (D1, sourced from Phase 0): named-reviewer source-bundle. Sympathetic — Christian Marques 2024-12-18 ("excellent," "succinctly covering the theory"), Alejandro 2024-12-20 (bridges philosophy/complexity/architecture). Critical — Nicola 2025-01-03 (abstractness, tone toward developers), Travis 2025-02-13 (half baked). External — Eric Normand Substack (sympathetic but flags the name). Honest framing: reviews are sparse outside Goodreads; no major-venue critical essay located.
7. **Uptake** (mg's decision 2026-04-26): one paragraph noting practitioner-traction signals — VirtualDDD's "Practical Residuality" with hands-on matrix work, Avanscoperta workshop transcripts, software-architektur.tv interview, doubleSlash blog explainer. Frame as positive: residuality is being taught and discussed beyond O'Reilly's immediate circle, even if no major-venue critical essay has appeared.
8. **Author provenance** (one-line per Phase 0): O'Reilly is founder of Black Tulip Technology, currently identifying as PhD student in complexity science based in Stockholm, Sweden. Useful grounding; not biographical detail beyond what's publicly stated.
9. **Dedication and acknowledgements one-liner** (D5): "For Tanya, my stressor"; reviewers Bennett-Lovsey, Moir, Høst, Haegebaert; Mathias Verraes for inspiring the book; cover art by Alexander O'Reilly aged 11.

### Edit 1.8 — Provenance note rewrite (D1)

Lines 219 and 240 currently say the book was not consulted. Both must be rewritten:

- The book has been consulted (April 2026); cannot be quoted at length per copyright; passages referenced by chapter/subsection rather than page number.
- Reception material is sourced from the consulted book + Phase 0 reviews, not from the chronology's secondhand "reception is mixed" annotation.
- Forthcoming primary material (PhD thesis, longer version, cross-project significance test) is acknowledged as **announced but unverified**. The corpus is open. The empirical claim that most distinguishes residuality from competing methodologies is gated on material that has not yet been published.
- O'Reilly is a real-named individual: founder of Black Tulip Technology, identifying as PhD student in complexity science, Stockholm. The corpus is one researcher's program, not an institutional research consortium output.

### File 1 checklist

- [ ] 1.1 Ergodicity in §3
- [ ] 1.2a Robust-vs-residual subsection in §6
- [ ] 1.2b Stressors-vs-X taxonomy in §6
- [ ] 1.2c Flow analysis pre-stressor step in §6
- [ ] 1.3 ICE-ing/AFIR worked-example punchline
- [ ] 1.4 Cross-project significance claim in §8
- [ ] 1.5 Linear/lateral cognitive style in §9
- [ ] 1.6 §10 defences + Phase 0 criticism
- [ ] 1.7 New "2024 book" section (9 sub-pieces)
- [ ] 1.8 Provenance note rewrite

---

## File 2 — `residuality-bibliography.md`

**Register**: bibliography. Each entry follows the existing format; group by role per the file's existing organisation. No prose outside entries.

**Total surface**: ~12 new entries + 1 expanded *Residues* entry + pending-gaps section.

### Edit 2.1 — Add book-cited references

In the appropriate role-grouped sections:

- Schon (1979), *The Reflective Practitioner* — under foundational/philosophy
- Ralph & Tempero (2016), "Characteristics of decision-making during coding" — under software-design
- Parnas (1971), "On the criteria to be used in decomposing systems into modules" — under software-design (verify not already present)
- Parnas & Clements (1986), "A rational design process: How and why to fake it" — under software-design
- DeLanda (2013), *Intensive Science and Virtual Philosophy* — under philosophy/post-structuralism. **Annotate**: O'Reilly's only explicit citation to a Deleuze-trained complexity theorist; high relevance for assemblage-rhizome-nomad work.
- Marion (1999), *The Edge of Organization* — under complexity-science
- Prigogine & Stengers (1997), *The End of Certainty* — under complexity-science
- Bergson and Whitehead — bare cites; no specific titles in book; record as "cited in passing"
- Hole (2016) on antifragile ICT — verify against existing chronology before adding
- Osterwalder & Pigneur (2010), *Business Model Generation* — under practitioner-tools (new sub-grouping if needed)
- Porter (2008), "The Five Competitive Forces That Shape Strategy" — under practitioner-tools

### Edit 2.2 — Expand 2024 *Residues* entry

Add to the existing entry (or create if absent in current bib):
- One-line provenance note: founder of Black Tulip Technology; identifies as PhD student in complexity science, Stockholm
- One-line dedication/acknowledgement note: "For Tanya, my stressor"; reviewers Bennett-Lovsey, Moir, Høst, Haegebaert; Mathias Verraes editorial impetus
- Reception cross-reference: see survey §10 / new "2024 book" section

### Edit 2.3 — Add Phase 0 sources

Under a new "Practitioner talks, workshops, and reception" section (or expand the existing practitioner-introductions section):

- VirtualDDD: "An Introduction to Residuality Theory by Barry M. O'Reilly" — virtualddd.com link
- VirtualDDD: "Practical Residuality by Barry M. O'Reilly" — hands-on matrix work
- Avanscoperta workshop transcript (2023-11-27): "Residuality Theory for Antifragile Software Architecture" — blog.avanscoperta.it
- *software-architektur.tv* episode 279 (2023): transcript engaging residuality
- doubleSlash blog (2026): "Residuality Theory: Future-Proof Software Architecture Inspired by Insights from Biology"
- Goodreads reviews of *Residues* (2024): aggregate page; cite Marques (2024-12-18), Alejandro (2024-12-20), Nicola (2025-01-03), Travis (2025-02-13) as named contributors

### Edit 2.4 — Add "Pending — known gaps" section

Record as gaps in the bibliography itself (so future agents know what they would not be able to find):

- O'Reilly PhD thesis: announced in 2024 book Conclusion; not publicly indexed as of 2026-04; institutional affiliation unknown (Stockholm-area lead)
- "Longer version" of *Residues*: announced in book Conclusion; not yet appeared
- Cross-project significance-test paper: claimed in book ("statistically significant effect"); not publicly available

### File 2 checklist

- [ ] 2.1 Book-cited references (~10 entries)
- [ ] 2.2 *Residues* entry expanded
- [ ] 2.3 Phase 0 source bundle
- [ ] 2.4 Pending-gaps section

---

## File 3 — `cyberneutics-and-residuality.md`

**Register**: cyberneutics-internal working note. First-person plural acceptable ("we observe", "cyberneutics inherits"). Substantive analytical voice; not survey-neutral.

**Total surface**: 4 sections touched; ~250–400 net words added.

### Edit 3.1 — §2.4 (two-step algorithm extended to sense-making)

**Conditional on Phase 1 re-check**:
- If "no flip": re-frame the section using "stressor analysis + contagion analysis" naming. Update the generalization claim to reflect the renamed step 2. ~50 words touched.
- If "flip": substantive rewrite. Pause execution and notify mg before proceeding.

### Edit 3.2 — §2.5 (second-order cybernetics answer to VSM critique)

Two changes:

(a) Anchor the cybernetics-critique answer explicitly on the **2021 *Philosophy* paper's Beer-specific critique** (not on the 2024 book's diffuse anti-structuralism). Note the critique-target softened across the arc.

(b) **Add mg's hyperliminality observation**: Beer's VSM is a recursive blueprint that may still be useful at the "complicated" inside-boundary domain (the ergodic core) but fails at the "complex" environmental domain (the non-ergodic envelope). VSM may serve as a stick-in-the-ground starting point — a naïve architecture in residuality terms — from which iterative residuality steps depart. This is a substantive new claim; this is the right place for it. ~150 words.

### Edit 3.3 — §2.6 (Naur bridge) and §2.7 (Pask bridge)

One sentence each: note that the 2024 book does not move into Naur or Pask territory; these bridges remain entirely cyberneutics-side. Brief.

### Edit 3.4 — §2.1 and §2.2 (Probe + eigenform Ri): add empirical-gap angle as possibility

Per mg's decision (2026-04-26): **mention as a possibility worth investigating, not as a strong claim**.

In §2.1 and/or §2.2, add a short paragraph noting that O'Reilly's own empirical apparatus (cross-project Ri significance test) is not yet publicly available as of 2026-04, and that this *may* mean cyberneutics' Probe + eigenform-Ri framing has a temporary opportunity to publish first. Frame as "an angle worth exploring once O'Reilly's empirical material is published," not as "cyberneutics has the stronger empirical position." Avoid overclaiming on a temporary publication gap. ~80 words.

### Edit 3.5 — §5 contribution-back inventory

Update the two-axis classification table (evidence tier × stance) only if 3.4 promotes any item to a higher tier. Default: no change to the table; the empirical-gap angle is observational, not a new tier-(a) contribution.

### File 3 checklist

- [ ] Phase 1 re-check completed and result logged
- [ ] 3.1 §2.4 contagion-analysis renaming (or substantive rewrite if flip)
- [ ] 3.2a §2.5 anchor on 2021 *Philosophy* paper
- [ ] 3.2b §2.5 add hyperliminality + Beer/VSM observation
- [ ] 3.3 §2.6 and §2.7 Naur/Pask single sentences
- [ ] 3.4 §2.1/§2.2 empirical-gap possibility (carefully framed)
- [ ] 3.5 §5 inventory table — likely no change; verify

---

## File 4 — `fan-as-stressor-generator.md`

**Register**: residuality-practitioner-facing. Self-contained. Does not assume the reader has read cyberneutics essays.

**Total surface**: ~100 words changed in one section.

### Edit 4.1 — Soften "The problem" section's framing

Current framing: "the act of generating a good list is left largely to the architect's intuition." This is not quite right — the book *does* recommend PESTLE / Business Model Canvas / Porter's Five Forces in its "Coaching Stressor Analysis" subsection.

Rewrite to: O'Reilly does point at upstream aids (PESTLE, BMC, 5-Forces) but leaves the *integration and breadth-discipline* to architect intuition. The fan operation's contribution is more disciplined breadth via incommensurable lenses, not filling a vacuum. This is a more honest framing and is more defensible against a residuality-practitioner reading the note.

### File 4 checklist

- [ ] 4.1 Rewrite "The problem" section's framing

---

## File 5 — `assemblage-rhizome-nomad.md`

**Register**: cyberneutics-internal working note pitched at readers of both residuality and Deleuze-Guattari. Substantive analytical voice; willing to be load-bearing.

**Total surface**: 2 sections touched + falsifier paragraph (item 11) sharpened. ~300 words added.

### Edit 5.1 — Sharpen central claim with C3 evidence (book level)

The 2024 book amplifies the Deleuzian walk and omits assemblage / rhizome / nomadic distribution. Even though the book is the most accessible and most Deleuze-friendly text in the corpus, it does not invoke the *Mille Plateaux* vocabulary. This is the strongest possible evidence that the omission is a rhetorical choice rather than an absence of conceptual commitment.

### Edit 5.2 — Add Phase 0 corpus-wide negative result

The Phase 0 research found no public talk, blog post, podcast, workshop transcript, or social-media engagement in which O'Reilly invokes assemblage, rhizome, or nomadism. The omission is corpus-wide *and* teaching-wide, not paper-bounded. The cyberneutics-side mapping is unambiguously a cyberneutics observation, not a residuality claim. State this explicitly with the negative-search-result citation.

### Edit 5.3 — Add DeLanda citation and brief discussion

DeLanda (2013), *Intensive Science and Virtual Philosophy*, is O'Reilly's only explicit citation to a Deleuze-trained complexity theorist. The book is precisely the bridge between Deleuze and complex-systems science that residuality theory operates on. Note this in the assemblage-rhizome-nomad note as evidence that the conceptual lineage is *demonstrable* in O'Reilly's own citations even where the specific *Mille Plateaux* terms are not invoked.

### Edit 5.4 — Falsifier paragraph (item 11)

Per the readiness plan, item 11 is now load-bearing for the convergence spine. With Phase 0 evidence in hand, the falsifier paragraph becomes easier to write. Sharpen the §6 deterritorialization gesture into an explicit "what would refute the mapping" subsection. Name at least one feature of assemblage that does not map to residue, OR one residuality construct without a Deleuze-Guattarian counterpart. Use the corpus-wide negative-result citation as positive evidence that the mapping is cyberneutics-side, not O'Reilly-side; this affects how the falsifier should be phrased.

### File 5 checklist

- [ ] 5.1 Sharpen central claim with book-level C3 evidence
- [ ] 5.2 Add Phase 0 corpus-wide negative result
- [ ] 5.3 Add DeLanda citation
- [ ] 5.4 Falsifier paragraph (item 11)

---

## File 6 — `wild/residuality-theory/README.md`

**Register**: agent-facing navigation. Tables, links, status callouts.

**Total surface**: small. Table row updates + Status section bullet + recent-changes line.

### Edit 6.1 — Status section: add 2026-04-26 entry

Add a recent-changes line to the Status block at top:
> **2026-04-26** ([this directory](.)): Survey paper broadened to include the 2024 *Residues* book; bilateral note, fan note, and assemblage-rhizome-nomad note revised to reflect book material; bibliography expanded with book-cited and Phase 0 sources. See [`book-integration-plan.md`](book-integration-plan.md) and [`book-integration-edit-plan.md`](book-integration-edit-plan.md) for the integration record.

### Edit 6.2 — Source-material navigation table: update file descriptions

The "When to read" entries for `state-of-residuality-2026.md`, `cyberneutics-and-residuality.md`, `fan-as-stressor-generator.md`, and `assemblage-rhizome-nomad.md` all need brief updates reflecting the book-integration. Two lines or fewer per file.

### Edit 6.3 — "Cited but not archived locally" section

Update the *Residues* (2024) entry: change framing from "Reception is mixed; sympathetic and critical reviews both circulating" to a Phase-0-grounded version naming where reviews are found and acknowledging the empirical-claim and longer-version gaps.

### Edit 6.4 — Status section: integrations list

The "April 2026 integrations" bullet list mentions five items. After the book integration, consider whether to add a sixth ("Book-broadening of survey and downstream working notes") or to fold the new work under an extended "Survey of residuality theory" item. Default: add a sixth bullet rather than rewrite — preserves the integration record.

### File 6 checklist

- [ ] 6.1 Status block 2026-04-26 entry
- [ ] 6.2 Navigation table per-file updates
- [ ] 6.3 *Residues* entry under "Cited but not archived"
- [ ] 6.4 Integrations list (add sixth bullet)

---

## File 7 — `essay-13-readiness-plan.md`

**Register**: action document. Status snapshots, item lists, dissents.

**Total surface**: small. New subsection + status update.

### Edit 7.1 — Add "Stability re-check 2026-04" subsection

(Already triggered by Phase 1 re-check; this just records its existence in this file.) State the result of the bilateral-note re-check against contagion-vs-NKP terminology. One paragraph.

### Edit 7.2 — Status snapshot: add book-integration entry

Add to the "Done" list:
> **Done (2026-04-26, book integration)**: Survey broadened to include 2024 *Residues* book; bilateral, fan, and assemblage-rhizome-nomad notes revised; bibliography expanded; provenance updated. Phase 0 external research surfaced thesis-not-yet-indexed and longer-version-not-yet-appeared as honest open gaps.

### Edit 7.3 — Item 14 re-evaluation

Item 14 in the readiness plan is "consider extracting bilateral note's §4 (survey-extension proposals) as a separate document." After the survey broadening, that work may now be largely done in the survey itself. Mark item 14 for re-evaluation: if the survey now does the extraction work, item 14 collapses; if not, item 14 remains.

### File 7 checklist

- [ ] 7.1 "Stability re-check 2026-04" subsection (gates further work)
- [ ] 7.2 Status snapshot book-integration entry
- [ ] 7.3 Item 14 re-evaluation

---

## File 8 — `meta/project-state.md`

**Register**: project-wide status log. Brief entries.

**Total surface**: one entry.

### Edit 8.1 — Add 2026-04-26 entry

One paragraph logging the book-integration work, pointing at:
- [`wild/residuality-theory/book-integration-plan.md`](../wild/residuality-theory/book-integration-plan.md)
- [`wild/residuality-theory/book-integration-edit-plan.md`](../wild/residuality-theory/book-integration-edit-plan.md)
- [`wild/residuality-theory/oreilly-current-work-report.md`](../wild/residuality-theory/oreilly-current-work-report.md)
- the revised survey, bibliography, and three working notes

Note honest open gaps (thesis, longer version, cross-project significance test) and the watch-items for re-running thesis search later.

### File 8 checklist

- [ ] 8.1 2026-04-26 project-state entry

---

## Cross-cutting checks before declaring done

After all eight files are edited:

- [ ] Survey reads as a unified body; book material is not bolted-on appendix-style
- [ ] Survey's editorial register is consistent (third-person, neutral, paper-grounded; book voice described not adopted)
- [ ] Bibliography is internally consistent (DeLanda annotation cross-references assemblage-rhizome-nomad note; *Residues* entry cross-references survey §10 and "2024 book" section)
- [ ] No survey paragraph quotes more than ~3 consecutive sentences from the book (fair-use discipline)
- [ ] All Phase 0 citations resolve to the actual URLs in the research report
- [ ] Stability-window re-check result is recorded *before* any working-note edit lands
- [ ] Empirical-gap framing is consistent across survey §10, bilateral §2.1/§2.2, and the new book section: "announced but unverified," not "cyberneutics has the stronger position"
- [ ] Uptake paragraph in survey's new book section is positive and bounded (no overclaiming about wide adoption)
- [ ] README's recent-changes block is in chronological order with the 2026-04-26 entry on top
- [ ] essay-13-readiness-plan.md and meta/project-state.md both reference the integration plans

## Estimated total work

- Phase 1 re-check: ~30 minutes
- File 1 (survey): 2–3 hours
- File 2 (bibliography): 1 hour
- File 3 (bilateral note): 1–1.5 hours
- File 4 (fan note): 15 minutes
- File 5 (assemblage-rhizome-nomad note + falsifier): 1.5–2 hours
- Files 6, 7, 8 (index/log updates): 30 minutes total
- Cross-cutting checks: 30 minutes

**Total: roughly 7–9 hours of focused editing work.** The largest single piece is the survey; the highest-risk piece is the falsifier paragraph (item 11) because it's load-bearing for the convergence spine.

## What this plan does not do

- Does not pre-write any of the prose. The executing agent (or mg) writes register-appropriate prose at edit-time.
- Does not commit to a posture (A/B/C/D from the readiness plan's decision space). Posture choice remains item 17, mg's call, separate from this work.
- Does not draft essay-13. This is preparation only.
- Does not revisit the assemblage-rhizome-nomad mapping itself; it sharpens the existing claim with new evidence.
