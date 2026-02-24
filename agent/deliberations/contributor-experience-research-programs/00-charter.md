---
charter:
  goal: "Evaluate the experience of a researcher looking to contribute to the Cyberneutics project by inspecting the research-programs directory, and identify concrete improvements to make onboarding and contribution easier."
  context: >
    The meta/research-programs/ directory collects five research plans (societies-of-thought,
    evaluation-schemes, ablation-study, multi-model-committee, condorcet-comparison) plus
    completed/archived programs. The README provides priority ordering, conventions, and
    thematic grouping. Plans vary enormously in maturity, detail level, and length (from
    the 140-line ablation-study to the 1700-line multi-model-committee). A new researcher
    arriving at this directory must figure out: what's available, what's tractable, what
    skills are needed, and where to start. The question is whether the current structure
    serves that goal or creates unnecessary barriers.
  success_criteria:
    - "Identify specific friction points a new contributor would encounter"
    - "Distinguish structural problems (information architecture) from content problems (missing information)"
    - "Produce actionable recommendations that don't require rewriting the entire directory"
    - "Consider trade-offs between serving newcomers and serving the project's existing users"
  exit_conditions:
    - "Committee has mapped the key tensions between accessibility and depth"
    - "At least 3 concrete, implementable recommendations with named trade-offs"
    - "Dissenting positions documented where committee disagrees"
  deliverable_format: "Resolution Artifact + Decision Space Map"
---

# Charter: Contributor Experience in research-programs

**Date**: 2026-02-23
**Convened by**: User request

## Problem Statement

A researcher discovers the Cyberneutics project and wants to contribute. They navigate to `meta/research-programs/` as instructed by the README. What happens next? Do they find a clear path to contribution, or do they bounce off the complexity?

## Context

The research-programs directory currently contains:

- **README.md**: Priority table, active/completed tables, conventions, by-theme table, related links
- **5 plan files** of wildly varying length and maturity:
  - `ablation-study.md` (~140 lines, structured, clear procedure)
  - `condorcet-comparison.md` (~100 lines, completed, results linked)
  - `evaluation-schemes.md` (~800 lines, umbrella design doc)
  - `societies-of-thought-research-plan.md` (~250 lines, 10 action items)
  - `multi-model-committee.md` (~1730 lines, detailed architecture + experimental protocol)
- **2 results directories**: `ablation-study/results/`, `condorcet-comparison/results/`

The README tells contributors to "pick a plan that matches your skills and interests" but does not specify what skills each plan requires, estimate difficulty, or suggest an entry point.

## Key Questions for the Committee

1. What does a contributor's journey look like today? Where do they get stuck?
2. What information is missing that would unblock them?
3. What structural changes (if any) would help without adding maintenance burden?
4. Is the problem the directory itself, or the plans within it, or both?
5. What trade-offs arise between making the directory contributor-friendly and keeping it useful as an internal research tracker?
