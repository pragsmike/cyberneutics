---
charter:
  goal: "Determine how to rigorously test the deliberated-choice workflow (fan→funnel composition) as a first live validation of the newly implemented /scenarios, scenario-aware /committee, and their composition seam."
  context: >
    The deliberated-choice workflow composes /scenarios (fan, divergent exploration)
    with /committee scenario_context: (funnel, convergent deliberation). All three
    skills — /scenarios, scenario-aware /committee, and their composition — have been
    implemented but never run on a real problem. The handoff identifies this as the
    top validation priority. We need to choose a test problem, define what success
    looks like, and specify what to check at each stage.
  success_criteria:
    - "Committee identifies what makes a good test problem for this workflow"
    - "Committee surfaces risks of testing with a toy problem vs. a real problem"
    - "Committee specifies concrete acceptance criteria for each pipeline stage"
    - "Committee addresses how to evaluate the composition seam (charter bridging)"
    - "Resolution produces an actionable test plan with specific checkpoints"
  exit_conditions:
    - "Committee has mapped the decision space: what to test, how to test, what 'passing' means"
    - "Resolution specifies a test problem and stage-by-stage verification criteria"
  deliverable_format: "Resolution Artifact + Decision Space Map"
---

# Charter: Testing the Deliberated-Choice Workflow

The deliberated-choice workflow is the composed fan→funnel pipeline: `/scenarios` generates divergent futures, the user reviews, then `/committee scenario_context:` deliberates across those futures to produce a scenario-aware resolution. This workflow has been specified (`artifacts/deliberated-choice-workflow.md`), formalized (`palgebra/duality-and-composition.md`), and implemented (skill files for `/scenarios` and scenario-aware `/committee` mode), but never executed.

The committee's task is to deliberate on **how to test this workflow** — what test problem to use, what to check at each stage, what "passing" means, and what risks exist in the test design itself.
