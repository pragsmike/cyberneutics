---
resolution:
  date: 2026-03-08
  topic: "Contributor gatekeeping: making exploratory contributions welcome"
  outcome: PASSED
  decision: "Implement targeted documentation changes to add an explicit exploratory contribution path via wild/ and wild/diary/, with minimal conventions and honest expectation-setting."
  summary: >
    The committee found that the contributor documentation successfully serves structured
    contributors but inadvertently gatekeeps exploratory ones by omitting any path for
    half-formed ideas. The fix is additive: surface wild/ and wild/diary/ in contributor-facing
    docs, adjust tone from "contract" to "invitation" for exploratory work, scope the
    research-programs checklist to its intended audience, and set honest expectations about
    review cadence. No new rubric is recommended. The committee noted that the intervention
    rests on thin evidence (N=1) and should be monitored.
  implementation_plan:
    - action: "Add exploratory contribution type to CONTRIBUTING.md"
      description: "Replace 'compact contribution contract' framing. Add sixth type: exploratory ideas → wild/ and wild/diary/. Add opening sentence welcoming contributions at any level of polish."
    - action: "Add exploratory routing row to meta/contributor-guide.md"
      description: "Add 'I have a half-formed idea or lateral connection' → wild/diary/ for raw ideas, wild/ for shaped ideas. State convention: date-prefixed filename, markdown, no other requirements."
    - action: "Scope research-programs/README.md checklist"
      description: "Add scope note before 'Before you pick a program' checklist redirecting exploratory contributors to wild/."
    - action: "Update wild/diary/README.md for contributors"
      description: "Confirm on-ramp language and naming convention are present (already partially done during diary move)."
    - action: "Add expectation-setting note"
      description: "In CONTRIBUTING.md or contributor-guide.md: exploratory contributions reviewed periodically; acceptance means idea is held, not necessarily developed."
    - action: "Set 3-month review checkpoint"
      description: "Review whether any exploratory contributions arrived, whether the pipeline worked, whether the labor model held."
  votes:
    - member: Maya
      vote: "YES — conditional on expectation-setting being honest about maintainer bandwidth"
    - member: Frankie
      vote: "YES"
    - member: Joe
      vote: "YES — conditional on structural conventions for agents remaining intact"
    - member: Vic
      vote: "YES — with note that evidence base is thin and monitoring is essential"
    - member: Tammy
      vote: "YES"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: Contributor Gatekeeping Problem

## Decision

Implement targeted documentation changes to create an explicit exploratory contribution path. The changes are additive — they extend the existing system rather than replacing it.

## Key Findings

The contributor documentation was built by agents for agents during a contributor-routing session. It solves a real structural problem (preventing agent-caused drift) but inadvertently gatekeeps human contributors arriving with exploratory ideas. The `wild/` directory and `wild/diary/` pipeline already exist as the correct destination for such contributions, but they are invisible from contributor-facing surfaces.

The committee recommends six specific changes (see implementation plan in front matter) and explicitly recommends against creating a new contributor-experience rubric at this time.

## Conditions and Monitoring

The resolution carries two conditions:

1. **Honest expectation-setting**: Contributors must understand that exploratory contributions enter a periodic review pipeline, not a real-time conversation. The language should be warm but not over-promising.

2. **Three-month review**: Evaluate whether the changes attracted any exploratory contributions, whether the diary → wild → formalization pipeline works for external contributors, and whether the maintainer labor model held.

## What We Are Not Doing

- Not rewriting the structural conventions that agents depend on
- Not creating a parallel rubric for contributor experience
- Not removing the validation checklist from research-programs (just scoping it)
- Not promising real-time engagement with exploratory contributors
- Not redesigning the contribution system — extending it with one additional path

## Dissent Record

No member voted against the resolution. Logged disagreements concern tone calibration (Frankie prefers informal invitation language; Maya prefers clinical honesty; Joe prefers institutional stability) and convention strictness (date-prefix naming is recommended but not required). These are calibration questions, not directional disagreements.
