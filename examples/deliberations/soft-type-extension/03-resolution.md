---
resolution:
  date: 2026-03-19
  topic: "Soft type theory extension: conservative vs. full treatment"
  outcome: PASSED
  decision: "Adopt conservative version as canonical; retain v2 in palgebra/ pending review; merge v2's new sections after independent mathematical review passes."
  summary: "The committee unanimously recommends a conditional adoption path. The conservative version (§5 product quantale only) becomes canonical immediately. The full treatment (v2, with §§6-7 coend and sheaf condition) remains in palgebra/ with explicit 'pending review' status. Seven specific mathematical claims in v2 are identified for independent review. If review passes, v2's new sections merge into the canonical document. This preserves the document's earned stability while keeping the formalization pipeline moving."
  implementation_plan:
    - action: "Update v2 header"
      description: "Change v2's subtitle to indicate 'pending independent mathematical review' status. [DONE]"
    - action: "Cross-reference from conservative to v2"
      description: "Update conservative version's §6 open questions to reference v2's §§6-7 as 'proposed treatments, pending review.' [DONE]"
    - action: "Run tiered review"
      description: >
        Run /review on v2 with claims prioritized by consequence:
        Tier 3 (primary focus): (4) probabilistic interpretation of coend as expected score,
        (6) sheaf condition conjecture from measurement framing.
        Tier 2 (secondary): (2) colimit interpretation via Kelly 3.73, (5) Grothendieck
        topology on preorder via Mac Lane-Moerdijk III.2, plus spot-check of §5's collapse
        functor lax monoidality.
        Tier 1 (spot-checks): (1) coend simplification, (3) V_5 cocompleteness,
        (7) restricted sheaf settings.
    - action: "Merge or remediate"
      description: "If review scores at/above threshold, merge v2's §§6-7 into canonical document. If below, remediate per standard loop."
  votes:
    - member: Maya
      vote: "YES"
      statement: "Conditional adoption addresses my concern about unverified content wearing earned credibility."
    - member: Frankie
      vote: "YES"
      statement: "The explicit review recommendation prevents indefinite deferral. Acceptable compromise."
    - member: Joe
      vote: "YES"
      statement: "This follows the precedent set by categorical-structures.md: content first, review second, corrections third."
    - member: Vic
      vote: "YES"
      statement: "Scoped review of the seven enumerated claims is the right verification approach."
    - member: Tammy
      vote: "YES"
      statement: "Formalization pipeline moves forward without premature canonical promotion. The system works as designed."
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "Pending user ratification"
---

# Resolution: Soft Type Theory Extension

## Decision

Adopt the conservative version of `soft-type-theory.md` (with §5 product quantale and updated §6 open questions) as canonical. Retain `soft-type-theory-v2.md` in `palgebra/` with explicit "pending independent mathematical review" status. Merge v2's new sections into the canonical document after independent review passes.

## Rationale

The committee's recommendation is procedural, not substantive: v2's content may be correct, but it has not been independently verified. The conservative version maintains the document's earned credibility (§§1-4 reviewed; §5 technically contained and verifiable). V2's §§6-7 introduce novel categorical constructions (coend, sheaf condition analysis) that require independent mathematical review before carrying the authority of a canonical palgebra document.

## Vote Record

5-0 in favor. Unanimous.
