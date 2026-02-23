# Repository Gap Analysis

## 1. Dangling Links
The following files are linked in existing documentation but do not exist in the repository:

(None — previously broken links to `pachinko-of-stored-literature.md` and `charts-on-a-manifold.md` in essays/README.md have been marked as "coming soon")



## 2. Planned Documents
The following documents are listed in `essays/README.md` or `artifacts/README.md` as "coming soon" or otherwise planned but are currently missing:

### Essays (not yet written, partially covered by existing material)
*   `pachinko-of-stored-literature.md`: The Pachinko of Stored Literature — metaphor previewed in Essays 01 and Stories All the Way Down
*   `charts-on-a-manifold.md`: Charts on a Manifold — metaphor developed in Stories All the Way Down and formalized in Decorated Texts
*   `eigenforms-narrative-convergence.md`: Eigenforms and Narrative Convergence — concept introduced in Essay 04
*   `editor-role-publishing.md`: The Editor's Role: Publishing Stories to Reality

### Essays (not yet written, corresponding artifacts exist)
*   `adversarial-committees-epistemic.md`: Adversarial Committees as Epistemic Triangulation — practical technique in `artifacts/adversarial-committees.md`, empirical backing in `societies-of-thought-synthesis.md`
*   `roberts-rules-information-theory.md`: Robert's Rules as Information-Theoretic Constraint — practical technique in `artifacts/roberts-rules-forcing-function.md`
*   `independent-evaluation-training.md`: Independent Evaluation as Adversarial Training — practical protocol in `artifacts/independent-evaluation.md`
*   `cross-scenario-institutional-memory.md`: Cross-Scenario Learning as Institutional Memory — practical template in `artifacts/cross-scenario-learning.md`

### Essays (not yet written, no existing coverage)
*   ~~`when-methodology-fails.md`: When This Methodology Fails~~ Done — `essays/when-methodology-fails.md`. Six failure modes (scope mismatch, character failure, hermeneutic circle persistence, editorial abdication, framing garbage-in, meta-circularity), each with mechanism, detection, and recovery. Scope map for practitioners. Self-application section.
*   `formalization-problem.md`: The Formalization Problem
*   `cognitive-overhead-diminishing-returns.md`: Cognitive Overhead and Diminishing Returns
*   `narrative-computing-extended-mind.md`: Narrative Computing and the Extended Mind
*   `epistemology-collaborative-sensemaking.md`: The Epistemology of Collaborative Sense-Making

### Artifacts & Examples
*   `examples/strategic-pivot-example.md`: Strategic Pivot Example
*   `examples/failure-case-example.md`: Failure Case Example

## 3. TODO Items

*   ~~**Start Here reading path** (methodology-adoption-strategy robust action)~~: Done — `artifacts/start-here.md`: 15-min path (gist → 01, 02, 03 → try quick-start or adversarial-committees). Linked from README "Getting started."
*   ~~**Full-pipeline worked example** (methodology-adoption-strategy robust action)~~: Done — `artifacts/examples/full-pipeline-worked-example.md`: methodology-adoption-strategy run (situation → scenarios → charter → deliberation → resolution) with commentary on what the process surfaced. Linked from artifacts/examples/README.md.
*   ~~**Consider splitting fiction from `the-stochastic-imps-of-happenstance.md`**~~: Done — story and epilogue extracted to `essays/tilt-sound-collective-story.md`; essay retains preamble, appendix, and coda with a bridge linking to the fiction.
*   ~~**Extract project plan from `societies-of-thought-synthesis.md`**~~: Done — extracted to `meta/research-plans/societies-of-thought-research-plan.md`; essay now has a bridging paragraph referencing the plan.
*   ~~**Cross-reference all cited documents against references directory**~~: Done — `references/README.md` rewritten as a comprehensive annotated bibliography covering all 39 sources cited across essays/ and palgebra/, organized into 9 thematic sections with consistent format and "Cited in" pointers.
*   ~~**Incorporate diary/2026-02-21-cyberneutics-dual-operations** and **wild/residuality-theory** into methodology, documents and palgebra formalism, and string diagram generation.~~: Done — Theory: `palgebra/duality-and-composition.md` and `essays/10-decisions-under-uncertainty.md`. Implementation: `/scenarios` skill (`.claude/skills/scenarios/SKILL.md`) with hybrid scenario roster (`agent/scenario-roster.md`, 4 fixed core + extension mechanism); `/probe` skill (`.claude/skills/probe/SKILL.md`) with variance report and decision landscape map schemas; committee skill extended for `scenario_context:` (backward-compatible); manual fan→funnel workflow documented (`artifacts/deliberated-choice-workflow.md`); practitioner guide (`artifacts/scenario-generation.md`); string diagram converter extended with `{spider: fan/funnel}` annotation, example equations (`decision-monad-equations.txt`), continuation-line joining, and UTF-8 encoding fix. CLAUDE.md updated with new skills.