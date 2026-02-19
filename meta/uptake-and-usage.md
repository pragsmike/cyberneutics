# Uptake and Usage

External adoption signals, practitioner feedback, and what they tell
us about whether the methodology actually works outside its birthplace.

**Why this file exists**: The Feb 1, 2026 self-evaluation identified
external validation as the #1 gap. This document tracks evidence —
positive, negative, and ambiguous — as it arrives.

---

## Adoption Events

### 1. Repository Fork: Committee Makeup Extension

**Date**: February 19, 2026
**Who**: External practitioner (details TBD)
**What**: Forked the cyber-sense repository with the stated intent to
use and extend the adversarial committee deliberation feature.

**Specific interest**: Experimenting with different committee makeups
to compare results for different kinds of problems. This is exactly
the extensibility the committee system was designed for — the
character-propensity-reference and committee-setup-template documents
support custom rosters, and the `/committee` skill can be invoked
with different character configurations.

**What this validates**:
- The committee concept is comprehensible to someone outside the
  project — they understood it well enough to identify a specific
  extension direction
- The extension they chose (different rosters for different domains)
  is architecturally sound — it doesn't require changing the pipeline
  structure, only the catalytic inputs (character propensities)
- In palgebra terms: they're keeping the morphisms and changing the
  catalytic objects, which is exactly how the formalism says you
  customize a pipeline

**What we don't know yet**:
- Whether they succeed in running deliberations
- Whether different makeups actually produce measurably different
  results
- What problems they apply it to
- What friction they encounter (documentation gaps, unclear
  instructions, tool assumptions)

**Follow-up**: If they share results, this would be the first
external deliberation data. Especially valuable if they run the
`/review` evaluation against their transcripts — that would give us
comparative rubric scores across different roster configurations.

---

### 2. MOOLLM Platform Integration

**Date**: On or before February 19, 2026
**Who**: SimHacker / MOOLLM project
**What**: Incorporated the adversarial committee mechanism into the
MOOLLM platform.

**Context**: The `artifacts/integration-with-moollm.md` document maps
Cyber-Sense primitives to MOOLLM primitives (Characters → Cards,
Committee Sessions → Rooms, Lessons → Files). This integration was
anticipated in the architecture but not previously confirmed as
implemented.

**What this validates**:
- The technique is portable — it can be extracted from the
  cyber-sense repository and embedded in a different platform
- The MOOLLM mapping (characters as persistent cards with
  calibration state, sessions as bounded rooms with protocol
  enforcement) is workable in practice
- The methodology can run on infrastructure that provides features
  the ad-hoc approach lacks (room isolation, persistent state,
  protocol enforcement)

**What we don't know yet**:
- How faithfully the committee mechanism was adapted (full roster?
  Robert's Rules? Independent evaluation?)
- Whether MOOLLM's infrastructure features (room isolation,
  persistent cards) improve deliberation quality compared to
  the ad-hoc approach
- Whether MOOLLM users who haven't read the cyber-sense essays
  can use the committee feature effectively

**Significance**: MOOLLM integration is a different kind of adoption
than an individual fork. It makes the committee available to MOOLLM's
user base, potentially multiplying exposure. If MOOLLM users produce
deliberations and share feedback, the sample size grows faster.

---

## What the Feb 1 Self-Evaluation Predicted

The committee self-evaluation (repository readiness review) identified
several conditions that would signal the methodology is working:

| Predicted signal | Status |
|---|---|
| External practitioners attempt to use the methodology | First fork confirmed |
| Techniques are adopted by other platforms | MOOLLM integration confirmed |
| Different committee makeups tested for different domains | Fork practitioner intends this |
| Rubric scores from external deliberations available | Not yet |
| Failure reports from practitioners | Not yet |
| Sustained multi-session use by external users | Not yet |

Two of six predicted signals have appeared within three weeks of the
self-evaluation. This is consistent with "suitable for early adopters"
but too early to claim broad validation.

---

## Feedback Log

*(Record practitioner feedback here as it arrives — positive,
negative, and ambiguous. Date, source, verbatim if possible,
analysis.)*

No feedback received yet beyond the adoption events above.

---

## Open Questions for Practitioners

If you've forked or used this methodology, the most valuable
feedback would be:

1. **What worked?** Which techniques produced useful results?
2. **What didn't?** Where did the methodology fail or add friction
   without value?
3. **What's missing?** What did you need that wasn't documented?
4. **What surprised you?** Anything the methodology predicted that
   you didn't expect, or anything it missed that you did expect?
5. **Rubric scores**: If you ran `/review` on your deliberations,
   what scores did you get? How did they compare across different
   problem types or committee makeups?

---

**Last Updated**: February 19, 2026
