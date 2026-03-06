---
resolution:
  date: 2026-02-22
  topic: "Should we keep and recommend the metacognition process (confidence at resolution, register, optional with-register runs, cumulative-confidence test) as a supported part of the methodology?"
  outcome: PASSED
  decision: "Keep and recommend the metacog process with a tiered recommendation and a sunset clause; do not recommend with-register as default until we have more comparison evidence."
  summary: |
    The committee voted to keep the full metacognition process as a supported part of the methodology. Recommendation is tiered: (1) Confidence at resolution — recommend (already default in the skill). (2) Register — recommend when the user runs multiple committees and wants a calibration snapshot; document how and when to run the register script. (3) With-register runs and the cumulative-confidence comparison test — support as the way to test whether the register helps; do not recommend with-register as default until we have at least three comparison runs showing consistent benefit (with-register ≥ baseline and calibration mentioned). Add a review/sunset clause to the artifacts or run guide (see implementation plan for exact trigger). This preserves user benefit (veracity signal) while avoiding overcommit and methodology bloat.
    **Assumptions (added in remediation):** We use review sum and calibration-mentioned as *proxies* for user benefit; this assumption is not yet validated; the sunset treats no improvement in these proxies as grounds to deprecate with-register. Register usage by end users is unknown; primary consumers are the with-register committee run (which reads the register) and maintainers; the sunset review will consider evidence of broader use and may simplify to confidence-only or maintainer-only register if there is none.
  implementation_plan:
    - action: "Update metacognition and cumulative-confidence-smoke-test artifacts"
      description: "State the tiered recommendation (confidence recommended, register when running many committees, with-register supported but not default). State explicitly: review sum and calibration-mentioned are proxies for user benefit, unvalidated; sunset uses these proxies. State: register usage unknown; primary consumers are with-register run and maintainers; sunset review will consider evidence of use."
    - action: "Add sunset trigger (one sentence)"
      description: "Deprecate with-register if fewer than 3 of the first 5 comparison runs show with-register ≥ baseline AND calibration mentioned in the resolution or transcript. Revisit at 12 months or 5 comparison runs, whichever comes first."
    - action: "Run additional comparison tests"
      description: "2–3 more baseline vs with-register runs on new topics; log in cumulative_confidence_smoke_log.md to accumulate evidence."
    - action: "Revisit at trigger"
      description: "At 12 months or 5 comparison runs, evaluate using the trigger above; if triggered, deprecate with-register from recommended path and document confidence + register only; sunset review will also consider register usage evidence."
  votes:
    Maya: YES
    Frankie: YES
    Joe: YES
    Vic: YES
    Tammy: YES
  confidence:
    Maya: 3
    Frankie: 4
    Joe: 4
    Vic: 4
    Tammy: 3
  signatures:
    chair: "Committee (Cyberneutics)"
    ratified_by: "User"
---

# Resolution

**Outcome:** PASSED

**Decision:** Keep and recommend the metacog process with a tiered recommendation and a sunset clause; do not recommend with-register as default until we have more comparison evidence.

**Votes:** Maya Aye (3), Frankie Aye (4), Joe Aye (4), Vic Aye (4), Tammy Aye (4). Unanimous.

**Summary:** See front matter. The committee agreed the process is useful in principle and worth keeping, but the *strength* of recommendation should be tiered and conditional on evidence for the heavier part (with-register). Confidence at resolution is recommended; register is recommended when running many committees; with-register is supported and testable, with a defined revisit to simplify if it doesn't pay off.
