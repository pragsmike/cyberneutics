# Editorial Review: Cyberneutics Repository — Audience Experience

**Date**: 2026-02-24
**Scope**: All 11 numbered essays, 7 supporting essays, essays/README.md, root README.md, CLAUDE.md
**Rubric**: `agent/rubrics/repo-audience-experience.md` (seven dimensions, 0–3)

---

## Executive Summary

The Cyberneutics essay collection is an intellectually ambitious and largely successful body of work. Its greatest strengths are the quality of the theoretical synthesis (the four-pillar integration of Dervin, von Foerster, Deleuze, and Pask is genuinely novel and well-argued), the honesty of the self-assessment (`when-methodology-fails` is among the best pieces in the collection), and the vividness of the core metaphors (game within a game, charts on a manifold, pachinko of stored literature). The writing voice is distinctive and engaging — it earns the right to introduce difficult concepts by keeping the reader oriented with concrete examples and direct address.

The systemic weaknesses cluster around two themes: **inconsistent navigation infrastructure** and **uneven audience calibration**. The Previous/Next essay links are incomplete and use inconsistent formatting across the numbered sequence. The four reading paths defined in `essays/README.md` are reasonable in structure but the Practitioner path dead-ends in theory without bridging to doing, and the Theorist path omits two core essays (07, 09) that its own path description acknowledges elsewhere. Several essays have substantial overlap that could be compressed or explicitly cross-referenced rather than restated. The register shifts across the collection — from the informal storytelling of Tilt Sound Collective to the category-theoretic density of Essay 08 — are mostly appropriate to audience but not always signposted for readers following a path.

Against the rubric, the repo currently scores in the **low-to-mid 2 range** on most dimensions, with Trust and Honesty at 3 (a genuine strength) and Navigation at a borderline 1-2 due to broken navigation chains. No dimension is at 0. The priority remediation targets are: (1) complete and standardize essay navigation links, (2) add a "bridge to doing" step at the end of the Practitioner reading path, (3) tighten the Theorist path, and (4) reduce unproductive overlap in Essays 07 and `narrative-computing-history`.

---

## Rubric Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **1. Audience Paths** | **2** | Four paths defined in `essays/README.md` with clear entry points. Practitioner path dead-ends at Essay 03 with no onward pointer to artifacts. Theorist path omits 07 and 09 (acknowledged in line 39 but easy to miss). Skeptic and Formalist paths are coherent and complete. |
| **2. Conceptual Coherence** | **2** | The four-term glossary (narrative computing / narrative engineering / cyberneutics / cybernetic hermeneutics) in `essays/README.md` is excellent. First-use definitions are mostly good. Issues: "MOOLLM" appears in Essays 02 and `societies-of-thought-synthesis` without adequate context. "Eigenform" is well-handled. Scene-1 uses different character names (Kaelen/Elena/Silas) without flagging this as a separate roster, potentially confusing readers. Some forward references (e.g., the "pachinko" standalone treatment promised in `essays/README.md` line 323 that doesn't exist). |
| **3. Tone and Register** | **2** | "Serious but accessible" is the dominant register and it works well. Essay 06 (Deleuze) dives into continental philosophy that would lose Practitioners. Essay 08 is appropriately technical for its bridge role. `societies-of-thought-synthesis` shifts to second-person advocacy ("Your edge: ...") which is inconsistent with the rest. Root README's Hunter Thompson / Lester Bangs quotes are fun but tonally discontinuous. The Tilt Sound Collective story and stochastic-imps essay have a warmer, more personal register — appropriate for their narrative function. |
| **4. Actionability** | **2** | Artifacts exist and are well-developed (adversarial-committees, quick-start-guide, start-here). But the essay collection itself rarely bridges to action. Essay 08 bridges to palgebra. `when-methodology-fails` has an excellent scope map. The Practitioner reading path doesn't end with "now go try this." Formalists get strong material. Skeptics get `when-methodology-fails`. Theorists get the full argument. The gap is: Practitioners reading essays don't know when to stop reading and start doing. |
| **5. Trust and Honesty** | **3** | The collection's standout dimension. `when-methodology-fails` is exceptional: six failure modes with mechanisms, detection heuristics, self-application, and honest acknowledgment that the essay itself shares the limitations it describes. Root README's Status section is calibrated ("early-stage documentation"). The Condorcet non-claim is explicit. The evidence base section distinguishes what's validated from what remains to be validated. The caveat that failure modes are predicted rather than empirical is exactly the right epistemic posture. |
| **6. Navigation and Findability** | **2-** | `essays/README.md` is detailed and accurate. Root README lists all files. But: Previous/Next links are incomplete across the numbered sequence (Essays 03, 04, 05, 06, 07 have inconsistent or missing sequential navigation). Link formatting is inconsistent (some use "Previous essay" / "Next essay," others use "Related essays" or "See also"). All internal file links appear valid (artifacts, palgebra, essays all resolve). `essays/README.md` line 323 promises a standalone "Pachinko of Stored Literature" treatment that doesn't exist — minor but a broken promise. |
| **7. Delight / Experience** | **2** | The writing is engaging. Core metaphors (game within a game, charts on a manifold, pachinko) are vivid and memorable. The opening scenario of `when-methodology-fails` is excellent — it hooks instantly by showing a confident wrong answer. The Tilt Sound Collective story is genuinely entertaining. Friction points: the sheer volume (18 essays plus artifacts plus palgebra) can overwhelm. Some essays (07, `narrative-computing-history`) are long and could be tightened. The bridge from "I understand the theory" to "I can do something" requires leaving the essay collection entirely. |

**Priority dimensions**: Navigation (2-) and Audience Paths (2) are the lowest-scoring and most impactful to fix. Trust (3) is the strongest and should be preserved.

---

## Per-Essay Notes

### Essay 01: `01-why-narrative-engines-change-everything.md`
- **Tone**: Strong, confident opening. Sets the register well for the collection. The pachinko metaphor is vivid and lands immediately.
- **Exposition**: Three-era framing (numeric → symbolic → narrative) is clear and well-argued. Terms defined on first use.
- **Accessibility**: Good for all audiences. Practitioners get concrete framing. Theorists get the paradigm claim. Skeptics get the problem statement.
- **Specific issues**:
  - The essay works well as an entry point for all four reading paths.
  - Has a "Next essay" link to 02. No "Previous" (appropriate — it's the first).

### Essay 02: `02-from-practice-to-theory.md`
- **Tone**: Personal narrative register — "how we got here." Appropriate and engaging.
- **Exposition**: MOOLLM is mentioned (§ "Connection to MOOLLM") without enough context for readers who don't know what it is. A one-sentence gloss would help.
- **Accessibility**: Strong for Practitioners (it's a practice story). Adequate for Theorists. May bore Skeptics who want evidence, not origin stories.
- **Specific issues**:
  - Has a "Next" link to 03. Missing an explicit "Previous" link back to 01.

### Essay 03: `03-sensemaking-101.md`
- **Tone**: Expository, clear. Good introduction to Dervin.
- **Exposition**: Situation-Gap-Bridge model explained well. Clean definitions.
- **Accessibility**: The Practitioner path ends here without pointing forward to artifacts. This is the dead-end problem — the reader has absorbed theory (01, 02, stories-all-the-way-down, 03) but doesn't know what to do next.
- **Specific issues**:
  - Missing Previous/Next sequential navigation links.
  - This is where the Practitioner path needs a "Now try it →" pointer to `artifacts/start-here.md` or `artifacts/quick-start-guide.md`.

### Essay 04: `04-cybernetics-and-observation.md`
- **Tone**: More technical. Introduces von Foerster, eigenforms, second-order cybernetics. Still accessible but requires more attention.
- **Exposition**: Eigenform concept well-introduced through multiple examples. The "prompting as control theory" section is excellent.
- **Accessibility**: Good for Theorists and Formalists. Practitioners may lose the thread in the von Foerster material without the practical grounding of prior essays.
- **Specific issues**:
  - Missing Previous/Next sequential navigation. Has only a "Related essays" section.
  - The conceptual progression from 03 → 04 is strong (sense-making → cybernetic feedback → they're the same thing) but the link between them is made explicit only in 05, not in 04 itself.

### Essay 05: `05-the-synthesis.md`
- **Tone**: Integrative, builds excitement. The "grand unification" framing works.
- **Exposition**: Pulls together Dervin, von Foerster, Deleuze effectively. This is a key essay for Theorists.
- **Accessibility**: Assumes familiarity with all three frameworks. Appropriate for its position in the sequence.
- **Specific issues**:
  - Has "See also" and "Next" links but formatting is inconsistent with 08-11's "Previous essay" / "Next essay" pattern.
  - "Cybernetic hermeneutics" is defined here but not prominently re-introduced in later essays that use it.

### Essay 06: `06-deleuze-difference-repetition.md`
- **Tone**: The most philosophically dense essay. Opens accessibly but the Deleuze material (rhizome, lines of flight, virtual/actual) gets dense.
- **Exposition**: The "charts on a manifold" metaphor is introduced here and used throughout the rest of the collection. Well-defined.
- **Accessibility**: Strong for Theorists. Challenging for Practitioners. The section on "Practical Implications" helps but comes late.
- **Specific issues**:
  - Missing Previous/Next sequential navigation. Has only "Related to Cyberneutics" and "Related essays" sections — inconsistent with later essays.
  - The "lines of flight" / "rhizome" terminology from Deleuze is used here but rarely appears in later essays. This is fine (the later essays translate Deleuze into cyberneutics vocabulary) but the translation could be made more explicit.

### Essay 07: `07-bolands-narrative-engineering.md`
- **Tone**: Comparative — analyzing an external work. Good register.
- **Exposition**: The narrative computing vs. narrative engineering distinction is excellently developed here.
- **Accessibility**: Core for Theorists (independent convergence validates the framework). Should be on the Theorist path.
- **Specific issues**:
  - Missing Previous link to 06 and Next link to 08. Only has a "Further Reading" section.
  - Significant overlap with `narrative-computing-history.md` on Bruner's paradigmatic/narrative modes. Both essays develop the Bruner material at length. The overlap is productive (different angles) but not acknowledged — a cross-reference would help.
  - This essay is long. Sections II.D and III.A restate material from Essays 01 and 06 at length. These could be tightened with cross-references.
  - Not on the Theorist reading path despite being listed in Core Essays.

### Essay 08: `08-from-methodology-to-formalism.md`
- **Tone**: Bridging — moves between philosophical and algebraic vocabulary. Well-controlled register shift.
- **Exposition**: Excellent. Each section pairs a philosophical concept with its algebraic formalization. The table in §3 (exploration vs. assessment) is particularly clear.
- **Accessibility**: The intended bridge audience. Assumes familiarity with both vocabularies (appropriate for its position).
- **Specific issues**:
  - Has clean Previous (07) and Next (09) links. Good navigation.
  - §9 mentions "four representations" (equations, diagrams, files, philosophical narrative) but the essay itself primarily bridges only two (philosophy ↔ algebra). The claim is stronger than the demonstration.
  - The "Related" links section at the bottom has inconsistent spacing — the "Next essay" line isn't preceded by a blank line, which could render as a continuation of the Related list rather than a separate section.

### Essay 09: `09-narrative-immune-systems.md`
- **Tone**: Extended analogy — the immune system mapping. Dense but internally consistent.
- **Exposition**: The organ/bath distinction is clearly developed and becomes load-bearing for later material (wild/pask-mesh-bath). The Postel's Law application is elegant.
- **Accessibility**: Strong for Theorists and Formalists. The immune analogy may feel forced for Skeptics (the essay addresses this by showing it's functorial, not merely metaphorical).
- **Specific issues**:
  - Has clean Previous (08) and Next (10) navigation links.
  - Not on the Theorist reading path (acknowledged in `essays/README.md` line 39). Should at least be flagged as recommended supplementary reading on that path.
  - The "Civic Application" section on mis/dis/malinformation is important but feels somewhat disconnected from the pipeline formalism earlier in the essay. A bridging sentence connecting "this is where the immune analogy meets the real world" would help.

### Essay 10: `10-decisions-under-uncertainty.md`
- **Tone**: Prescriptive — "here's what to do." Clear, confident.
- **Exposition**: Fan/funnel duality well-explained. The decision monad section is accessible for its level of abstraction. The Sagan analogy table is excellent — it translates formal concepts into heuristics.
- **Accessibility**: Strong for all audiences. Practitioners get the Sagan table. Theorists get the monad laws. Formalists get the composition.
- **Specific issues**:
  - Has Previous (09) link but no Next link (it's the penultimate numbered essay; 11 follows but isn't linked).
  - The residuality theory connection (§ "Repetition as instrument") is well-handled but references O'Reilly without a citation — a footnote or parenthetical noting the book title would help readers find the source.

### Essay 11: `11-conversation-theory.md`
- **Tone**: Integrative — adds Pask as the "fourth pillar." Accessible.
- **Exposition**: Teachback, entailment mesh, walk styles all clearly introduced. The mapping to committee characters is well done.
- **Accessibility**: Strong for Theorists. The Pask material is specialized but the essay provides enough context.
- **Specific issues**:
  - Has Previous (10) link but no Next link (it's the last numbered essay — appropriate, but a "What's next" paragraph pointing to artifacts or applications would be useful).
  - The "Four-Pillar Architecture" table at the end is excellent — it's the payoff of the entire theoretical sequence. Consider making this table findable from `essays/README.md`.

### `stories-all-the-way-down.md`
- **Tone**: Accessible, example-rich. Good entry point for Practitioners and Skeptics.
- **Exposition**: "Charts on a manifold" introduced here and in Essay 06. The legal theory parallel and math proofs examples are effective.
- **Accessibility**: Excellent for Practitioners and Skeptics. On both reading paths.
- **Specific issues**:
  - Character names (Maya, Frankie, Joe, Vic, Tammy) are used in examples without introduction — assumes the reader has encountered them. On the Practitioner path, this essay comes before any character introduction (which lives in `stochastic-imps`). This is a forward reference.

### `the-stochastic-imps-of-happenstance.md`
- **Tone**: The most personal and essayistic piece. Includes the character sheets (the original introduction of Maya, Frankie, Joe, Vic, Tammy).
- **Exposition**: "Game within a game" framework clearly developed. Character introductions are vivid and memorable.
- **Accessibility**: Excellent for Skeptics (it's about trust calibration). On the Skeptic path.
- **Specific issues**:
  - This is where the committee characters are first introduced in the essay collection. But on the Practitioner and Theorist paths, readers may encounter character names in other essays first (e.g., `stories-all-the-way-down` uses them).
  - The essay is long — the Preamble + The Deeper Problem + The Threat Landscape sections could be tightened. The character sheets and committee dynamics sections are the most valuable parts.

### `societies-of-thought-synthesis.md`
- **Tone**: Research synthesis + advocacy. Second-person address ("Your edge: ...," "What we're missing: ...") is inconsistent with the rest of the collection's third-person/first-person-plural register.
- **Exposition**: The Google/UChicago/Santa Fe Institute paper connection is well-drawn. Information-theoretic framing of surprise markers is valuable.
- **Accessibility**: Strong for Theorists. The "Part III: What They're Missing (And You Can Fill)" section reads as internal planning notes rather than polished essay.
- **Specific issues**:
  - References "MOOLLM integration" and "rooms as cognitive contexts" without adequate explanation for general readers.
  - Part IV (action items) points to a research plan file. This is appropriate but the shift from essay to project management is abrupt.
  - The second-person "you" throughout should be standardized to match the rest of the collection.

### `narrative-computing-history.md`
- **Tone**: Academic but accessible. Well-structured historical survey.
- **Exposition**: Bruner's two modes explained in great detail (§ "The Cognitive Thread"). Kahneman's System 1/2 mapping is effective. Rosen's complexity vs. complication distinction is well-introduced.
- **Accessibility**: Strong for Theorists. Somewhat long for other audiences.
- **Specific issues**:
  - Substantial overlap with Essay 07 on Bruner's paradigmatic/narrative modes. Both essays develop this material at length without cross-referencing each other.
  - The Kahneman/System 1/System 2 section is excellent and doesn't appear elsewhere in the collection — it's unique value. The Rosen section is also unique.
  - The "Societies of Thought" reference in the Kahneman section ("discussed in our synthesis essay") uses informal self-reference.
  - This essay is long (~280 lines). The Computational Thread (§ "Early Story Generation") section could be compressed — TALESPIN and early story generators are interesting but tangential.

### `scene-1.md`
- **Tone**: Dramatic/dialog form. Distinct from everything else in the collection.
- **Exposition**: Demonstrates the synthesis through performance. Effective as a pedagogical device.
- **Accessibility**: Engaging for readers who've absorbed the three-framework synthesis. Confusing for newcomers.
- **Specific issues**:
  - Uses Kaelen/Elena/Silas characters, not the Maya/Frankie/Joe/Vic/Tammy roster. `essays/README.md` describes this correctly but a header note in the scene itself explaining "this is a different committee with different characters" would prevent confusion.
  - No cross-reference links at the bottom.

### `when-methodology-fails.md`
- **Tone**: The best-written essay in the collection. Opens with a devastating concrete scenario, maintains honest engineering posture throughout, and closes with genuine epistemic humility.
- **Exposition**: Six failure modes clearly structured with scenario → mechanism → detection → remedy. The scope map is immediately actionable.
- **Accessibility**: Excellent for all audiences. Skeptics get exactly what they need. Practitioners get the scope map. Theorists see which load-bearing claims could fail.
- **Specific issues**:
  - The self-application section at the end is extraordinary. The "credibility paradox" observation is exactly the kind of meta-aware critique that earns trust.
  - No significant issues. This essay should be flagged more prominently — it's a differentiator for the project.

### `tilt-sound-collective-story.md`
- **Tone**: Narrative fiction. Warm, human, concrete. Different register from everything else — appropriately so.
- **Exposition**: Dramatizes the concepts without formal explanation. Effective as a companion to `stochastic-imps`.
- **Accessibility**: Most accessible essay in the collection. Anyone can read this.
- **Specific issues**:
  - Works well in its current position as supplementary material.
  - No significant issues.

---

## Cross-Cutting Issues

### 1. Inconsistent essay navigation (affects: Navigation, Delight)

The Previous/Next navigation links across the 11 numbered essays are incomplete and use inconsistent formatting. Essays 08, 09 have clean "**Previous essay**: [title](link) / **Next essay**: [title](link)" formatting. Essays 03, 04, 05, 06, 07 have missing or non-standard navigation (using "Related essays," "See also," or no sequential links at all). Essay 10 has no Next link to 11. This makes it impossible to read the numbered sequence by clicking through — readers must return to `essays/README.md` to find the next essay.

### 2. Practitioner path dead-ends in theory (affects: Audience Paths, Actionability)

The Practitioner reading path in `essays/README.md` lists four items (01, 02, stories-all-the-way-down, 03) and then stops. There's no "now go do something" pointer to `artifacts/start-here.md` or `artifacts/quick-start-guide.md`. The root README has a "Getting started" section that bridges to artifacts, but a reader following the Practitioner path in `essays/README.md` wouldn't see it.

### 3. Bruner overlap between Essay 07 and `narrative-computing-history` (affects: Coherence, Tone)

Both essays develop Bruner's paradigmatic/narrative distinction at length. Essay 07 does it through the lens of Boland's convergence; `narrative-computing-history` does it through cognitive science and Kahneman. The overlap is intellectually productive (different framings of the same idea) but is not acknowledged — neither essay cross-references the other on this shared material. Readers encountering both will feel they've read the same material twice without understanding why.

### 4. MOOLLM references without adequate context (affects: Coherence)

MOOLLM is mentioned in Essay 02 (§ "Connection to MOOLLM"), `societies-of-thought-synthesis` (§ "Social Scaling Without Formal Architecture"), root README (§ "Why Cyberneutics"), and `artifacts/integration-with-moollm.md`. The root README gives the most context ("MOOLLM is the platform, Cyberneutics is the practice"), but readers encountering MOOLLM in essays won't necessarily have read the root README first. A one-sentence gloss at first use in the essay collection would help.

### 5. Character roster confusion between Scene-1 and main committee (affects: Coherence)

Scene-1 uses Kaelen (Entropy), Elena (Constraint), Silas (Integration) — a separate three-person committee. The main committee uses Maya, Frankie, Joe, Vic, Tammy. `essays/README.md` identifies the Scene-1 characters correctly but Scene-1 itself doesn't note that it's using a different roster. Readers encountering Scene-1 after absorbing the five-character committee may be confused.

### 6. Register inconsistency in `societies-of-thought-synthesis` (affects: Tone)

This essay uses second-person "you" and "your" throughout ("Your edge: ...", "What we're missing: ..."), reading like internal project notes rather than a published essay. The rest of the collection uses first-person plural ("we") or third-person. The tone should be standardized.

### 7. Theorist path omits core essays (affects: Audience Paths)

The Theorist reading path in `essays/README.md` acknowledges (line 39) that Essays 07 and 09 "are in Core Essays below" but doesn't include them. A Theorist following the path would miss the narrative-engineering distinction (07) and the immune-system extension (09). The "minimal theorist sequence" framing is reasonable but should include at least a note: "Also recommended: 07 (independent convergence validates the synthesis) and 09 (extends the formalism to trust boundaries)."

### 8. No "What's next" at the end of the numbered sequence (affects: Delight, Actionability)

Essay 11 is the final numbered essay. It has a Previous link but no forward pointer. A reader who's just finished the full theoretical sequence deserves a "congratulations, here's what to do now" paragraph pointing to artifacts, palgebra, and applications.

---

## Recommended Actions

### High Priority (comprehension-affecting, low effort)

1. **Complete and standardize Previous/Next links across all 11 numbered essays.** Use the format from 08-09: `**Previous essay**: [Title](./NN-filename.md)` / `**Next essay**: [Title](./NN-filename.md)`. This is mechanical work affecting Navigation and Delight.

2. **Add "Now try it" pointer at the end of the Practitioner reading path** in `essays/README.md`. After the four listed essays, add: "Ready to try it? → [Start Here](../artifacts/start-here.md) or [Quick Start Guide](../artifacts/quick-start-guide.md)." Affects Audience Paths and Actionability.

3. **Add header note to Scene-1** clarifying that it uses a different committee roster (Kaelen/Elena/Silas) than the main committee (Maya/Frankie/Joe/Vic/Tammy). One sentence suffices. Affects Coherence.

4. **Add a forward pointer at the end of Essay 11** — a "What's next" paragraph pointing to artifacts for doing, palgebra for formalizing, and applications for seeing the framework applied. Affects Delight.

### Medium Priority (audience experience, moderate effort)

5. **Expand the Theorist path** in `essays/README.md` to include 07 and 09 as recommended additions (not necessarily inline — a note after the path saying "Also recommended: Essay 07 (independent convergence) and Essay 09 (trust boundary extension)" suffices). Affects Audience Paths.

6. **Standardize register in `societies-of-thought-synthesis.md`** — change second-person "you/your" to first-person-plural "we/our" throughout. Affects Tone.

7. **Add cross-references between Essay 07 and `narrative-computing-history`** where they overlap on Bruner. Each should acknowledge the other: "For the cognitive science grounding of Bruner's two modes, see [Narrative Computing as Historical Progression](./narrative-computing-history.md)" in 07, and the reverse in `narrative-computing-history`. Affects Coherence.

8. **Add a one-sentence MOOLLM gloss** at its first appearance in the essay collection (Essay 02): "MOOLLM (Don Hopkins) is a runtime environment for multi-agent LLM interaction — the platform on which Cyberneutics' techniques are implemented." Affects Coherence.

### Lower Priority (polish, higher effort)

9. **Tighten Essay 07** — sections II.D and III.A restate material from Essays 01 and 06. Replace with concise cross-references: "For the three-era argument, see Essay 01; for the Deleuzian foundation, see Essay 06." This could reduce the essay by ~15-20% without losing substance. Affects Delight.

10. **Tighten `narrative-computing-history.md`** — the "Early Story Generation" section (TALESPIN, etc.) is interesting but tangential. It could be compressed to 2–3 paragraphs with a note that the full history is available in the computational narrative intelligence literature. Affects Delight.

11. **Remove or flag the "Pachinko of Stored Literature" standalone treatment** mentioned in `essays/README.md` line 323. Currently reads as a promise ("A standalone treatment may follow") for content that doesn't exist. Either remove the mention or change to "The pachinko metaphor appears in Essay 01 and Stories All the Way Down; no standalone treatment is currently planned." Affects Navigation (broken promise).

12. **Tighten `stochastic-imps` Preamble and Threat Landscape sections** — the material is good but could be more concise. The character sheets and committee dynamics are the irreplaceable parts. Affects Delight.

### Fine As-Is

- `when-methodology-fails.md` — leave untouched. It's the collection's strongest piece.
- `tilt-sound-collective-story.md` — works perfectly in its current role.
- The root README — well-structured, honest, comprehensive.
- The four-term glossary in `essays/README.md` — clear and correct.
- The palgebra cross-references from Essay 08 — accurate and helpful.

---

## Remediation Plan

### Goals

Raise all rubric dimensions to a consistent 2–3. Current priority targets:

| Dimension | Current | Target | Primary lever |
|-----------|---------|--------|---------------|
| Audience Paths | 2 | 3 | Fix Practitioner endpoint; expand Theorist path |
| Conceptual Coherence | 2 | 2-3 | Cross-references; MOOLLM gloss; Scene-1 note |
| Tone and Register | 2 | 2-3 | Standardize `societies-of-thought-synthesis` |
| Actionability | 2 | 2-3 | "Now try it" pointers at path endpoints |
| Trust and Honesty | 3 | 3 | Preserve — no changes needed |
| Navigation | 2- | 3 | Complete Prev/Next links; fix Pachinko promise |
| Delight | 2 | 2-3 | Tighten long essays; add forward pointers |

### Prioritized Changes

**Phase 1: Navigation infrastructure** (mechanical, no content judgment required — do first)

1. Add standardized Previous/Next links to Essays 02, 03, 04, 05, 06, 07. Use the 08/09 format: `**Previous essay**: [Title](./link.md)` on its own line, then `**Next essay**: [Title](./link.md)`. [Navigation]
2. Add `**Next essay**: [Conversation Theory](./11-conversation-theory.md)` to Essay 10. [Navigation]
3. Fix inconsistent link formatting in Essays 01, 05 to match the standard format. [Navigation]
4. Remove or revise the "Pachinko of Stored Literature" standalone treatment mention in `essays/README.md` line 323. [Navigation]

**Phase 2: Path endpoints and audience calibration** (requires one-paragraph additions)

5. Add "Now try it → [Start Here](../artifacts/start-here.md)" paragraph at the end of the Practitioner path in `essays/README.md`. [Audience Paths, Actionability]
6. Add recommended-supplementary note for Essays 07 and 09 on the Theorist path in `essays/README.md`. [Audience Paths]
7. Add "What's next" paragraph at the end of Essay 11 pointing to artifacts, palgebra, applications. [Delight, Actionability]
8. Add a header note to Scene-1 explaining the different character roster. [Coherence]

**Phase 3: Cross-references and glosses** (requires targeted edits within existing content)

9. Add MOOLLM one-sentence gloss at first essay-collection use (Essay 02). [Coherence]
10. Add bidirectional Bruner cross-references between Essay 07 and `narrative-computing-history`. [Coherence]
11. Standardize register in `societies-of-thought-synthesis` (second-person → first-person-plural). [Tone]

**Phase 4: Tightening** (higher effort, lower urgency — can be deferred)

12. Tighten Essay 07 §§ II.D and III.A with cross-references to 01 and 06. [Delight]
13. Compress `narrative-computing-history` § "Early Story Generation." [Delight]
14. Tighten `stochastic-imps` Preamble and Threat Landscape sections. [Delight]

### Dependencies

- Phase 1 has no dependencies — do it first. It's pure infrastructure.
- Phase 2 depends on Phase 1 only insofar as the "What's next" paragraph in Essay 11 should include a correct Next link if one is added.
- Phase 3 has no dependencies on Phase 1 or 2.
- Phase 4 depends on Phase 3 (specifically item 10 — the Bruner cross-references should exist before tightening Essay 07's overlapping sections).

### Out of Scope (deferred)

- **Writing the Pachinko standalone essay**: The idea is interesting but not needed for rubric scoring. Removing the promise is sufficient.
- **Restructuring the essay numbering**: The current order (theoretical build → synthesis → formalism → extensions) is sound. Re-numbering would break many cross-references for marginal gain.
- **Merging `narrative-computing-history` into Essay 07**: They serve different audiences (07 is about Boland's convergence; NCH is about cognitive/computational/systems-theoretic history). Cross-referencing is preferable to merging.
- **Adding empirical case studies**: `when-methodology-fails` correctly identifies this gap but it requires real-world usage data that doesn't yet exist. The honest labeling ("predicted, not empirical") is the right posture for now.
