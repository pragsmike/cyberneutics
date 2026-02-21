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
**What**: Forked the cyberneutics repository with the stated intent to
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

**Update — February 20, 2026**: Contributor has given more detail on their direction.

*Condorcet theorem*: They intend to investigate the Condorcet jury theorem as a formal foundation for the committee technique. The theorem (Condorcet, 1785) states that if each member of a majority-vote group is independently more likely than not to make a correct judgment, the probability of the majority being correct exceeds any individual's, and approaches 1 as group size grows. This would formalize *why* multi-perspective adversarial deliberation improves decision quality — it's not just a heuristic. The existing empirical support in `essays/societies-of-thought-synthesis.md` (Google, UChicago, Santa Fe Institute work) is consistent with this prediction but doesn't invoke Condorcet explicitly. If the contributor formalizes this connection, it would strengthen the theoretical section of `artifacts/adversarial-committees.md` and add a new dimension to `essays/societies-of-thought-synthesis.md`.

*mRNA and the immune analogy*: They suggested considering mRNA as relevant to the immune system analogy in `essays/09-narrative-immune-systems.md` and `applications/narrative-immune-systems/`. The implication is apt: mRNA vaccines deliver instructions to cells to produce a recognizable fragment of a pathogen so the immune system can learn the pattern *without exposure to the actual pathogen*. Applied to narrative immune systems: rather than exposing a community to real misinformation to build resistance (risky — the exposure itself can cause anchoring or radicalization), you could construct "narrative mRNA" — carefully designed fictional exemplars of misinformation patterns that train pattern recognition without contact with live attack vectors. This is a meaningful extension of the analogy beyond what the current essay captures. Worth a committee deliberation or a `/committee` run on the question of how to design such training material.

---

### 2. MOOLLM Platform Integration

**Date**: On or before February 19, 2026
**Who**: SimHacker / MOOLLM project
**What**: Incorporated the adversarial committee mechanism into the
MOOLLM platform.

**Context**: The `artifacts/integration-with-moollm.md` document maps
Cyberneutics primitives to MOOLLM primitives (Characters → Cards,
Committee Sessions → Rooms, Lessons → Files). This integration was
anticipated in the architecture but not previously confirmed as
implemented.

**What this validates**:
- The technique is portable — it can be extracted from the
  cyberneutics repository and embedded in a different platform
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
- Whether MOOLLM users who haven't read the cyberneutics essays
  can use the committee feature effectively

**Significance**: MOOLLM integration is a different kind of adoption
than an individual fork. It makes the committee available to MOOLLM's
user base, potentially multiplying exposure. If MOOLLM users produce
deliberations and share feedback, the sample size grows faster.

---

### 3. Repository Fork: Deleuzian Walks and Residuality Theory

**Date**: February 20, 2026
**Who**: New external contributor (details TBD)
**What**: Forked the repository and engaged with the Deleuze material
(`essays/06-deleuze-difference-repetition.md`), specifically noting a
connection between Deleuzian walks and Barry O'Reilly's Residuality
Theory via the concept of Architectural walks.

**The connection they're drawing**: A "Deleuzian walk" is nomadic
traversal through smooth space — following connections rather than
following a predetermined grid, letting difference lead rather than
imposing identity. In O'Reilly's Residuality Theory, an Architectural
walk is a method for understanding complex systems by moving through
them and observing what *residues* — essential, persistent elements —
survive change and transformation. The contributor suggests that
Residuality Theory's Architectural walk concept may have been
influenced by, or at minimum parallels, the Deleuzian model of
movement through space.

**Why this is interesting for cyberneutics**: The committee deliberation
process is already implicitly a kind of architectural walk — each
character traverses the problem space from their propensity-driven
starting point, following their epistemic "line of flight," and the
synthesis traces what residues persist across all the different
traversals. The Condorcet connection (from contributor #1) speaks to
*why* multiple walkers converge on better answers; the Residuality
connection speaks to *what* they're looking for — the features of the
problem space that survive reframing.

There's also a potential connection to the palgebra formalism: if the
committee is a set of traversals through a problem space, the
deliberation record (the 00-04 files) is the residue — what the
process leaves behind as a persistent artifact.

**What this validates**:
- The Deleuze essay is accessible to external readers and legible as
  something that connects to live theoretical work elsewhere
- The methodology is attracting contributors interested in theoretical
  depth, not just practitioners who want the committee technique
- Residuality Theory is an adjacent conceptual framework worth tracking;
  see `wild/` for where to put exploratory reading

**What to track**:
- Whether this contributor develops the connection formally
- Barry O'Reilly's Residuality Theory as a potential theoretical
  neighbor — the "residue" framing (what persists through transformation)
  is distinct from but complementary to the "decorated text" framing
  (what metadata accumulates through pipeline stages)

---

## What the Feb 1 Self-Evaluation Predicted

The committee self-evaluation (repository readiness review) identified
several conditions that would signal the methodology is working:

| Predicted signal | Status |
|---|---|
| External practitioners attempt to use the methodology | Two forks confirmed |
| Techniques are adopted by other platforms | MOOLLM integration confirmed |
| Different committee makeups tested for different domains | Fork #1 intends this; investigating Condorcet as formal basis |
| Rubric scores from external deliberations available | Not yet |
| Failure reports from practitioners | Not yet |
| Sustained multi-session use by external users | Not yet |

Two of six predicted signals have appeared, plus a second fork showing
theoretical engagement (Deleuze / Residuality Theory). This is
consistent with "suitable for early adopters" but too early to claim
broad validation. The theoretical depth of the engagement — Condorcet,
mRNA analogy extension, Deleuzian walks — is a stronger signal than
expected at this stage: these contributors are not just consuming the
technique, they're extending the theoretical scaffolding.

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

**Last Updated**: February 20, 2026
