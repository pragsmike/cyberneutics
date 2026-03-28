---
resolution:
  date: 2026-03-27
  topic: "Appropriate framework for AI engagement by informed practitioners"
  outcome: PASSED
  decision: >
    Structured AI use by informed practitioners is provisionally justified as
    a method of generating the evidence needed to evaluate the safety claim,
    subject to five explicit conditions.
  summary: >
    The committee acknowledges that the safety case for structured AI use has
    not been established by controlled study and that the evidence base for
    harm from unstructured use is serious and documented. The committee finds
    that non-engagement also carries costs — loss of safety-infrastructure
    development, inability to generate the evidence needed to evaluate safety
    claims, and ceding the field to unstructured users. Structured provisional
    use is justified not because the safety case is established but because the
    safety case cannot be established without engagement. This justification is
    explicitly conditional on five requirements, and the committee documents
    three unresolved concerns that the precautionary position raised and the
    committee could not fully address.
  details: |
    ## Conditions for Provisional Adoption

    1. **Evidence generation**: Every structured-use session produces inspectable
       records suitable for future evaluation. Calibration data is tracked
       longitudinally with minimum 12-month horizon.

    2. **Failure-mode documentation**: The three characterized failure modes
       (false assurance from clean records, calibration drift across domain
       boundaries, hermeneutic closure when human circuit-breaker disengages)
       are documented in framework materials and monitored in practice.

    3. **Off-ramps**: Pre-specified criteria for suspending the practice are
       defined before provisional adoption begins. If longitudinal evidence
       shows the framework does not improve decision quality, the practice
       is suspended.

    4. **Architectural circuit-breaker**: The human serves as active
       quality-control layer, not passive consumer. This is enforced through
       architectural design (human review required at decision points, not
       optional), not individual discipline.

    5. **Metacognitive monitoring**: Override frequency, practice-change
       frequency, and calibration-response rate are tracked as operational
       metrics to detect circuit-breaker disengagement.

    ## Unresolved Concerns

    1. **Denominator problem**: The framework reaches voluntary adopters, not
       the at-risk population. This is conceded. The framework is a practitioner
       discipline, not a public health intervention. It does not address the
       population most harmed by unstructured AI use.

    2. **Controlled evidence gap**: No randomized comparison of structured AI
       deliberation vs. structured non-AI deliberation exists. The committee
       recommends this study but cannot condition provisional adoption on it
       without creating the circularity Reva identified (requiring evidence
       that can only come from the practice being evaluated).

    3. **Propagation mechanism**: The causal chain from "practitioner uses
       framework carefully" to "vulnerable population is protected" has not
       been specified. Frankie's "prerequisite for regulation" argument is
       plausible but unverified. The framework's broader social value beyond
       its direct users remains aspirational.
  implementation_plan:
    - action: "Define off-ramp metrics"
      description: "Specify what evidence would trigger suspension of practice, before further provisional use"
    - action: "Begin longitudinal calibration tracking"
      description: "12-month program, minimum 10 practitioners, comparing prediction accuracy over time"
    - action: "Publish failure-mode inventory"
      description: "Document the three characterized failure modes in framework materials"
    - action: "Design circuit-breaker monitor"
      description: "Implement metacognitive tracking as operational metric"
    - action: "Design controlled comparison study"
      description: "Structured AI deliberation vs. structured non-AI deliberation, pre-registered, independently evaluated"
  votes:
    - member: Maya
      vote: "YES — conditional on off-ramps being real, not aspirational"
    - member: Frankie
      vote: "YES"
    - member: Joe
      vote: "YES — conditional on acknowledging the nuclear-vs-asbestos question remains open"
    - member: Vic
      vote: "YES — the evidence generation conditions are the minimum acceptable standard"
    - member: Tammy
      vote: "YES — conditional on circuit-breaker monitoring implementation"
    - member: Reva
      vote: "CONDITIONAL NO — I do not vote against the conditions. I vote against the conclusion that provisional use is justified before those conditions are met. The conditions described are necessary but have not been implemented. Voting yes on a plan is not the same as voting yes on a practice. When the conditions are implemented and the first 12 months of calibration data are available, I will reassess."
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution: AI Engagement Framework

**Outcome**: PASSED (5-1, with Reva's conditional dissent)

## Decision

Structured AI use by informed practitioners is provisionally justified as a method of generating the evidence needed to evaluate the safety claim, subject to five explicit conditions: evidence generation, failure-mode documentation, off-ramps, architectural circuit-breaker enforcement, and metacognitive monitoring.

## The Dissent

Reva's dissent is not a rejection of the conditions. It is a rejection of the temporal ordering: the committee votes to adopt the practice provisionally while the conditions are being implemented, whereas Reva would implement the conditions first and adopt the practice only after initial evidence is available. This disagreement is substantive, not rhetorical, and the committee records it as an unresolved tension.

## What This Resolution Does Not Claim

- It does not claim that structured AI use is safe. It claims that provisional use under explicit conditions is a defensible method of generating the evidence to evaluate safety.
- It does not claim that the framework protects the at-risk population. It concedes the denominator problem.
- It does not claim that individual practitioner discipline will propagate into institutional protection. It identifies this as an unverified aspiration.
- It does not claim Reva's position has been refuted. It documents that her core demands (controlled evidence, failure-mode analysis, off-ramps) have been accepted as conditions, and that her objection to the temporal ordering remains live.
