# Cross-Reference and Synthesis Plan

**Date**: 2026-02-16
**Scope**: Full repo review — opportunities to cross-reference, synthesize, clarify, and improve audience paths
**Constraint**: Do not change the first section of the top-level README (Narrative Computing intro, lines 1-17)

---

## Executive Summary

After reading every file in the repository, I found three categories of opportunity:

1. **Disconnected material** — files that exist but aren't referenced from any index or navigation path
2. **Missing cross-references** — documents that discuss the same concepts without linking to each other
3. **Audience path problems** — the essays/README has excellent reading paths that the top-level README doesn't surface; audiences are defined differently in different places

The plan below is organized from highest impact to lowest.

---

## 1. Surface the Reading Paths from essays/README.md

**Problem**: The `essays/README.md` has three excellent reading paths — Practitioner, Theorist, Skeptic — each curated with specific sequences and rationale. The top-level README's "Getting started" section has simpler paths that partially overlap but don't reference these. A reader following the top-level README would never discover the curated paths.

**Proposed change**: In the top-level README's "Getting started" section (below the Narrative Computing intro), add a sentence pointing to the essays/README reading paths. Something like:

> For curated reading paths by audience (Practitioner, Theorist, Skeptic), see the [Essays directory](essays/README.md#reading-paths).

**Files to modify**: `README.md` (in "Getting started" section, after existing links)

**Impact**: High — this connects two navigation systems that currently exist independently.

---

## 2. Connect scene-1.md to the Rest of the Repository

**Problem**: `essays/scene-1.md` is a committee debate transcript (Kaelen/Elena/Silas bootstrapping "cybernetic hermeneutics") that demonstrates the methodology applied to its own theoretical synthesis. It's not referenced from any index — not `essays/README.md`, not `artifacts/examples/README.md`, not the top-level README.

**Proposed change**:
- Add to `essays/README.md` in a new "Supplementary" or "Transcripts" subsection, with a note explaining it's a worked example of the methodology applied to itself
- Optionally reference from `artifacts/examples/README.md` as a third example alongside hiring-decision and repository-review

**Files to modify**: `essays/README.md`; optionally `artifacts/examples/README.md`

**Impact**: Medium-high — this is a demonstration of the methodology in action, which the repo-review example identified as something the repo needs more of.

---

## 3. Cross-Reference the Stochastic Imps Origin Story with Character Reference

**Problem**: `essays/the-stochastic-imps-of-happenstance.md` contains the *origin story* of all five committee characters (Maya, Frankie, Joe, Vic, Tammy) as members of "Tilt Sound Collective" running a sound studio. This is where the characters came from — their backstories, motivations, and epistemic stances are grounded in this narrative. But `artifacts/character-propensity-reference.md` (the 860-line character manual) never references it. A reader studying the characters wouldn't discover their narrative source.

**Proposed change**:
- Add a "Character Origins" note near the top of `artifacts/character-propensity-reference.md` linking to the stochastic imps essay as the source narrative
- Add a note in the stochastic imps essay's introduction pointing readers to the character reference for operational use

**Files to modify**: `artifacts/character-propensity-reference.md`, `essays/the-stochastic-imps-of-happenstance.md`

**Impact**: Medium-high — connects narrative grounding to operational reference. Helps readers understand *why* these specific characters work.

---

## 4. Triage the "Coming Soon" List

**Problem**: `artifacts/gap_analysis.md` lists 14 planned essays and 3 planned artifacts as missing. The `essays/README.md` lists these same essays with *(coming soon)* tags. Many of these have been partly written already — for example, `integration-with-moollm.md` exists and is listed in the gap analysis as missing, but it actually exists in `artifacts/`. The gap analysis is stale.

More importantly, the long list of "coming soon" essays creates an impression of incompleteness that may discourage readers. Some of these planned essays are now partially covered by existing material (e.g., "Robert's Rules as Information-Theoretic Constraint" is substantially covered in `artifacts/roberts-rules-forcing-function.md`).

**Proposed changes**:
- Update `artifacts/gap_analysis.md` to remove `integration-with-moollm.md` (it exists)
- In `essays/README.md`, consider reorganizing the "coming soon" items:
  - Mark which ones are substantially covered by existing artifacts/essays (with cross-references)
  - Distinguish "planned and likely" from "aspirational"
  - Remove or relocate items that create false expectation

**Files to modify**: `artifacts/gap_analysis.md`, `essays/README.md`

**Impact**: Medium — reduces reader confusion and maintains credibility. A repo that promises 14 unwritten essays looks abandoned; one that honestly shows what's covered where looks honest.

---

## 5. Add Cross-References Between Parallel Treatments

**Problem**: Several concepts are treated in both essays and artifacts without linking to each other. Readers following one path miss the complementary treatment.

Specific gaps:

| Concept | Essay Treatment | Artifact Treatment | Missing Link |
|---------|----------------|-------------------|--------------|
| Robert's Rules | Essay 02 discusses it briefly; essays/README promises dedicated essay | `artifacts/roberts-rules-forcing-function.md` (comprehensive, 458 lines) | No link from essay side to artifact |
| Independent evaluation | Essay 05 mentions observer problem | `artifacts/independent-evaluation.md` (441 lines) | No link from essay side to artifact |
| Characters/propensities | `stochastic-imps.md` creates them; `concept-extraction-stochastic-imps.md` analyzes them | `character-propensity-reference.md` operationalizes them | No cross-links (see item 3) |
| Soft types and decorated texts | `palgebra/decorated-texts.md` formalizes them | CLAUDE.md summarizes them | No link from artifacts that use type concepts (evaluation rubrics are essentially rubric halves of soft types) |
| Eigenforms | Essay 04 (cybernetics) discusses eigenforms extensively | The concept appears in committee character calibration (convergent debate patterns) | No cross-reference |
| Societies of Thought | `societies-of-thought-synthesis.md` provides empirical validation | Committee skill/artifacts describe the practice being validated | No link from committee artifacts to this validation essay |

**Proposed changes**: Add "Related essays" / "Related artifacts" footer sections where missing. Most artifacts already have these (e.g., `roberts-rules-forcing-function.md` links to adversarial-committees and independent-evaluation). The essays generally don't.

**Files to modify**: Several essays (especially 04, 05, stochastic-imps), `artifacts/character-propensity-reference.md`, `artifacts/evaluation-rubrics-reference.md`

**Impact**: Medium — makes the web of connections visible. Readers following any thread find related material.

---

## 6. Surface concept-extraction-stochastic-imps.md Appropriately

**Problem**: `essays/concept-extraction-stochastic-imps.md` is a working document that extracts theoretical concepts from the stochastic imps essay. It's not referenced in `essays/README.md` or anywhere else. It reads like an intermediate working document rather than a finished essay.

**Proposed change**: Either:
- (a) Add to `essays/README.md` under a "Working Documents" section with appropriate framing ("intermediate analysis, not polished essay")
- (b) Fold its key insights into other documents and remove it
- (c) Leave it as-is but add a note at the top identifying it as a working document

**Recommendation**: Option (c) — add a brief header note. It has value as an example of the concept-extraction process itself (meta-methodology), but shouldn't be in the main reading paths.

**Files to modify**: `essays/concept-extraction-stochastic-imps.md` (add header note); optionally `essays/README.md`

**Impact**: Low-medium — prevents reader confusion if they find it by browsing.

---

## 7. Align Audience Definitions

**Problem**: Different documents define the target audience differently:

- **Top-level README** (line 29-34): Practitioners, Researchers, Anyone frustrated, Theorists
- **essays/README.md**: Practitioners, Theorists, Skeptics
- **Repository-review example**: Early adopters and researchers
- **CONTRIBUTING.md**: New artifacts/techniques, Essays/theory, Examples/case studies

These aren't contradictory but they're inconsistent. The essays/README "Skeptic" path is useful but doesn't appear in the top-level README.

**Proposed change**: In the top-level README's "Who is this for?" section, add the "Skeptic" audience and link to the Skeptic reading path:

> * **Skeptics** wondering if this is just prompt engineering theater → [start here](essays/README.md#for-skeptics-show-me-why-this-matters)

**Files to modify**: `README.md` (in "Who is this for?" section)

**Impact**: Low-medium — small change but the Skeptic path is one of the most valuable entry points.

---

## 8. Link Palgebra to Artifacts That Embody It

**Problem**: The palgebra essay (`palgebra/decorated-texts.md`) describes resource equations, soft types, enrichment vs. transformation morphisms, and human gates. Several artifacts *implement* these concepts without naming them:

- **Evaluation rubrics** are the rubric half of soft types `(template, rubric)`
- **Independent evaluation** is an enrichment morphism (scores added to metadata without changing payload)
- **Committee deliberation → evaluation → iteration** is the pipeline from the palgebra essay's simplified evaluation pipeline
- **The `/string-diagram` skill** converts resource equations to diagrams — the operational form of the palgebra formalism

**Proposed change**: Add a brief note in `palgebra/decorated-texts.md` at the end (or in a "Connections to Artifacts" section) showing how the artifacts embody the formalism. Something like:

> The artifacts in this repository instantiate several of these concepts:
> - Evaluation rubrics (`artifacts/evaluation-rubrics-reference.md`) are the rubric half of our soft types
> - Independent evaluation (`artifacts/independent-evaluation.md`) is an enrichment morphism — scores added without changing the deliberation text
> - The `/string-diagram` skill converts these resource equations to visual Mermaid diagrams

**Files to modify**: `palgebra/decorated-texts.md`

**Impact**: Low-medium — helps theoretically-inclined readers see the formalism as operational, not just abstract.

---

## 9. Add the Societies of Thought Essay to the README

**Problem**: `essays/societies-of-thought-synthesis.md` provides empirical validation of the adversarial committee methodology from Google/UChicago/SFI research. It's listed in `essays/README.md` but not in the top-level README's essay list. Given that "show me the evidence" is a common reader reaction, this is a missed opportunity.

**Proposed change**: Add to the top-level README's essay list (in "What's in this repository?" → Essays section). Could also be referenced from the Skeptic audience path.

**Files to modify**: `README.md` (essay list — already done in a prior session, verify it's there)

**Impact**: Low — but important for credibility with skeptical readers.

---

## 10. Improve the References Directory

**Problem**: `references/README.md` is sparse — just 5 bullet points listing planned contents. Meanwhile, `essays/README.md` has a full "For Further Reading" section with 12 properly cited references organized by theoretical tradition. These should be connected.

**Proposed change**: Either:
- (a) Move the essays/README bibliography into `references/README.md` as a proper annotated bibliography
- (b) Have `references/README.md` link to the essays/README bibliography
- (c) Expand `references/README.md` with the same references plus annotations

**Recommendation**: Option (b) for now — it's the least work and avoids duplication. Add a sentence: "For a bibliography organized by theoretical tradition, see the [Further Reading section](../essays/README.md#for-further-reading) of the essays directory."

**Files to modify**: `references/README.md`

**Impact**: Low — but prevents the references directory from looking neglected.

---

## 11. Consider the Repository-Review Example's Own Recommendations

**Problem**: `artifacts/examples/repository-review-example.md` contains a self-review that identified five amendments. Some have been implemented, some haven't:

| Amendment | Status | Notes |
|-----------|--------|-------|
| 1. Clarify maturity statement | ✅ Done | README says "stable behavioral equilibrium" |
| 2. Restructure Getting Started | ❌ Partially | Quick Start isn't the *first* link yet |
| 3. Add evidence base statement | ❌ Not done | No "what evidence exists" section in README |
| 4. Create references document | ✅ Partially | `references/README.md` exists but sparse |
| 5. Surface development insights | ✅ Done | `meta/methodology-evolution.md` exists |

**Proposed changes**:
- Amendment 2: Move the Quick Start Guide link higher in the "Getting started" section (or add a "Try it now" line before the theory paths)
- Amendment 3: Add a brief "Evidence and Status" section to the README (or expand the existing "Status" section) documenting what evidence exists and what's needed

**Files to modify**: `README.md`

**Impact**: Medium — these were identified by the methodology's own self-review process. Implementing them is walking the talk.

---

## Priority Order

If implementing incrementally:

1. **Item 1** (surface reading paths) — trivial change, high value
2. **Item 7** (add Skeptic audience) — trivial change, connects to valuable path
3. **Item 11** (implement self-review amendments 2-3) — medium effort, walks the talk
4. **Item 3** (stochastic imps ↔ character reference cross-links) — small effort, connects narrative to operational
5. **Item 2** (connect scene-1.md) — small effort, adds a third example
6. **Item 4** (triage coming-soon list) — medium effort, reduces false promises
7. **Item 5** (cross-references between parallels) — distributed effort, many small touches
8. **Item 8** (palgebra ↔ artifacts connections) — small effort, helps theorists
9. **Item 9** (societies-of-thought in README) — verify/trivial
10. **Item 6** (concept-extraction header note) — trivial
11. **Item 10** (references directory link) — trivial

---

## Committee Debate Transcripts Found

The user asked to look for committee debate transcripts. Found:

1. **`essays/scene-1.md`** — A three-character (Kaelen/Elena/Silas representing Entropy/Constraint/Integration) debate bootstrapping the "cybernetic hermeneutics" synthesis. Uses the committee methodology to develop the theoretical framework itself. Not referenced from any index.

2. **`artifacts/examples/hiring-decision-example.md`** — The "10x Engineer" hiring decision. Full three-round deliberation with all five characters, Robert's Rules forcing function, independent evaluation, and lessons extracted. Referenced from artifacts/README.md and top-level README.

3. **`artifacts/examples/repository-review-example.md`** — Self-review of the Cyber-Sense repository using the methodology. Full deliberation with amendments, evaluation scores, and lessons. Referenced from artifacts/examples/README.md.

scene-1.md is the most interesting from a synthesis perspective — it's the methodology being used to develop its own theory, which is a powerful demonstration. Its disconnection from the rest of the repo is the biggest gap I found.

---

## Observations on Overall Coherence

The repository is surprisingly well-integrated for something developed over a short period. The main structural issues are:

- **Navigation fragmentation**: The essays/README, artifacts/README, and top-level README each provide navigation but don't reference each other's paths well enough
- **Working documents mixed with published material**: `concept-extraction-stochastic-imps.md` and `scene-1.md` are both valuable but sit alongside polished essays without any status distinction
- **The palgebra formalism is isolated**: It's mentioned in the top-level README and CLAUDE.md but the artifacts don't reference it, even though they instantiate its concepts. The `/string-diagram` skill bridges this gap operationally but not documentarily.
- **The "coming soon" debt**: 14 promised essays and 2 promised examples create expectation debt. Some of these are substantially covered by existing material under different names.

None of these are critical — the repo is usable and the material is strong. These are refinements that would make the strong material more discoverable.
