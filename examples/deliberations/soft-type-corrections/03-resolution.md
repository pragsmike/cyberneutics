---
resolution:
  date: 2026-03-19
  topic: "Correcting mathematical errors in soft-type-theory §§5-7"
  outcome: PASSED
  decision: "Apply all 9 edits: oplax fix (§5, both docs), three-statement coend rewrite (§6, v2), canonical topology bridge and sheaf-equilibrium conjecture relabel (§7, v2), two new open questions (§8, v2), verification notes in review file."
  summary: >
    The committee unanimously recommends correcting the three errors and two
    clarification issues identified in the mathematical review. The oplax fix is
    mechanical. The coend section gets a three-statement rewrite that preserves
    the intuition but is honest about the gap between categorical coend (join)
    and probabilistic expectation (weighted average), redirecting the coend's
    value to its universal property. The sheaf section gets a bridging sentence
    and a conjecture relabel. New open questions capture observations from the
    deliberation (soft routing dinaturality, sheaf-equilibrium empirical test).
  implementation_plan:
    - action: "Fix §5 collapse functor in both documents"
      description: "Change lax → oplax, reverse inequality description. Three edits."
    - action: "Rewrite §6 coend-expectation passage in v2"
      description: "Replace lines 606-626 with three-statement structure (A: coend as join, B: expectation as separate construction, C: honest bridge with universal property). Cite Kelly 3.69."
    - action: "Add canonical topology bridge in §7 of v2"
      description: "One sentence linking categorical and semantic characterisations via §2's refinement definition."
    - action: "Relabel mechanism design connection in §7 of v2"
      description: "Conjecture (sheaf-equilibrium connection) with explicit scope statement."
    - action: "Add two open questions to §8 of v2"
      description: "Soft routing dinaturality, sheaf-equilibrium empirical test."
    - action: "Update review file with §5 verification status"
      description: "Note what's been verified vs. assumed in §5."
  votes:
    - member: Maya
      vote: "YES"
    - member: Frankie
      vote: "YES"
    - member: Vic
      vote: "YES"
    - member: Joe
      vote: "YES"
    - member: Tammy
      vote: "YES"
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "Pending user confirmation"
---

# Resolution: Soft Type Theory Mathematical Corrections

## Decision

Apply all 9 edits as specified in the deliberation's Final Consensus section. The edits correct three mathematical errors and two presentation issues, preserve the document's expository flow, and make explicit the boundary between proven and conjectured claims.

## Vote Record

5-0 unanimous. All members agree on the specific edits. The only point of contention (scope of §5 audit) was resolved by noting verification status in the review file rather than adding disclaimers to the document.

## Key Principle

**Better to have an honest gap than a dishonest bridge.** The coend section's value shifts from "here's how to compute an aggregate grade" (which is vacuous) to "here's a structural guarantee about type-decomposition-independent constructions" (which is non-trivial and professionally defensible).
