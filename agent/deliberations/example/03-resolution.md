---
resolution:
  date: "YYYY-MM-DD"
  topic: "[Topic string]"
  outcome: "PASSED"   # or DEFERRED | NO_CONSENSUS
  decision: "[One-line decision]"
  summary: |
    [Paragraph summarizing what was decided.]
  votes:
    maya: "YES"
    frankie: "YES"
    joe: "YES"
    vic: "YES"
    tammy: "YES"
  # Optional: for metacognition/veracity analysis (1=low, 4=high). Omit if not collected.
  confidence:
    maya: 3
    frankie: 2
    joe: 4
    vic: 3
    tammy: 2
  signatures:
    chair: "Committee (Cyber-Sense)"
    ratified_by: "User"
---
