---
resolution:
  date: 2026-02-23
  topic: "Contributor experience in the research-programs directory"
  outcome: PASSED
  decision: "Implement a layered improvement: finish existing conventions, add triage metadata to plans, add quick-start section and prerequisites to README, flag multi-model-committee restructure for maintainer."
  summary: >
    The committee identified four specific friction points for contributors: (1) plans lack
    triage metadata (skills, scope, entry point), (2) the README organizes by priority but
    doesn't narrate a contributor journey, (3) plans assume methodology familiarity without
    stating prerequisites, and (4) the 12x variance in plan length (140 to 1,730 lines)
    misleads about effort required. The resolution is a layered approach: stabilize existing
    conventions first, then add lightweight contributor-facing metadata, then address
    structural issues like the multi-model-committee document's scope. The committee
    explicitly scoped out broader onboarding documentation as premature given no evidence
    of actual external contributors.
  details: >
    Four concrete recommendations ordered by implementation cost:

    (A) FINISH EXISTING CONVENTIONS. Apply Status/Runs/Results headers to the three plans
    that lack them (multi-model-committee, societies-of-thought-research-plan,
    evaluation-schemes). This is already flagged as optional work in the 2026-02-23 handoff.
    Making it a prerequisite for further changes prevents layered inconsistency.

    (B) ADD TRIAGE METADATA to each plan file. Suggested fields: Skills needed, Estimated
    scope (afternoon / week / month+), Contributor type (solo / collaborative), Entry point
    (what to read first, what action to take first). Place after the Status section. Keep
    it to 5-10 lines per plan. Example for ablation-study: Skills: familiarity with
    committee pipeline, basic statistics; Scope: month (design + execution); Type: solo
    or paired; Entry point: read evaluation-schemes.md Dimensions A-F, then choose N
    decisions.

    (C) ADD QUICK-START SECTION to research-programs README, placed above the priority
    table. Three curated entry points keyed to contributor profile: (1) "Want to run an
    experiment?" -> ablation-study or condorcet-comparison (as a completed template);
    (2) "Want to improve the methodology?" -> societies-of-thought Items 1-3;
    (3) "Want to extend the system?" -> multi-model-committee Phase 1. Include a
    prerequisites line: "Most programs assume familiarity with the adversarial committee
    pipeline. Read artifacts/adversarial-committees.md and try /committee on a test
    topic before diving in."

    (D) FLAG FOR MAINTAINER: Recommend that multi-model-committee.md be restructured
    in a future session — either split into a reference document (hypothesis,
    architectural patterns, model profiles) and an experiment protocol, or given a
    strong executive summary with contributor directions at the top. This requires
    authorial judgment and is not implementable without mg's input.

  implementation_plan:
    - action: "Apply Status/Runs/Results headers to three plans"
      description: "Finish existing convention from 2026-02-23 restructure. Apply to multi-model-committee.md, societies-of-thought-research-plan.md, evaluation-schemes.md."
    - action: "Add triage metadata blocks to all five plan files"
      description: "5-10 line metadata block per plan: Skills, Scope, Type, Entry point. Place after Status section."
    - action: "Add Quick Start for Contributors section to README"
      description: "3-5 curated entry points above the priority table. Include prerequisites line."
    - action: "Flag multi-model-committee restructure"
      description: "Document the recommendation for mg; do not implement without authorial approval."

  votes:
    - member: Maya
      vote: "YES — with emphasis that prerequisites must be stated explicitly, not just implied"
    - member: Frankie
      vote: "YES — the directory should feel like an invitation, not a catalog"
    - member: Joe
      vote: "YES — conditional on finishing existing conventions before adding new metadata"
    - member: Vic
      vote: "YES — conditional on keeping changes minimal and maintainable"
    - member: Tammy
      vote: "YES — layered approach addresses the audience-collision problem without over-engineering"

  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: Contributor Experience in research-programs

## Decision

**PASSED (5-0)**: Implement layered improvements to the research-programs directory to make contributor onboarding easier.

## Summary

The contributor experience in `meta/research-programs/` has four specific friction points: missing triage metadata on plans, no curated entry points in the README, unstated prerequisites, and misleading variance in plan scope/length. The resolution is a staged fix: (A) finish applying existing Status conventions, (B) add lightweight metadata blocks to each plan, (C) add a Quick Start section to the README, (D) flag the multi-model-committee restructure for the maintainer.

The committee explicitly chose *not* to recommend a full CONTRIBUTING.md or project-wide onboarding guide at this time — no evidence of actual external contributors justifies that investment. The recommended changes are implementable in 1-2 sessions with minimal ongoing maintenance cost.

## Conditions and Caveats

- **Joe's condition**: Steps must be ordered — finish existing conventions (A) before adding new metadata (B, C). Don't layer new structure on inconsistent foundations.
- **Vic's condition**: Changes should be self-maintaining where possible. Metadata that goes stale is worse than no metadata.
- **Maya's concern**: Even with these changes, the plans assume deep familiarity with the methodology. The prerequisites statement helps, but doesn't substitute for missing onboarding documentation.
- **Tammy's monitoring**: Track whether metadata stays current. If it drifts, simplify (fewer fields) rather than adding maintenance overhead.
- **Deferred scope**: Broader project onboarding (CONTRIBUTING.md), multi-model-committee document split, and tone/voice adjustments are all future-session candidates.
