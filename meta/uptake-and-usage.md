# Uptake and Usage

External adoption signals, practitioner feedback, and what they tell
us about whether the methodology actually works outside its birthplace.

**Why this file exists**: The Feb 1, 2026 self-evaluation identified
external validation as the #1 gap. This document summarizes **current
state** and **brief trajectory**. For a dated event log, see
[usage-and-uptake-chronology.md](usage-and-uptake-chronology.md).

---

## Current state (as of March 2026)

- **Two external forks, both active** — one focused on committee makeup and Condorcet/jury-theorem comparison (with merged PR and new artifacts), one on Deleuzian walks and Residuality Theory. Both show the methodology is comprehensible and extensible by outsiders; the first produced the first controlled comparison of deliberative vs. independent-aggregation pipelines (opposite verdicts on a value-laden question).
- **Two new PRs outstanding** (as of 2026-03-05):
  - *Condorcet contributor*: Proposes a method for tracking individual committee member performance longitudinally — examining how each character contributes across multiple deliberations over time. A meeting is scheduled (2026-03-06) to discuss how the new agent architecture taxonomy (roleplay vs. independent subagents vs. multi-model) might affect longitudinal tracking, since character identity works differently when characters are independent processes vs. roles within a single context.
  - *Residuality contributor*: Essay on software engineering practice and agents, arguing that implementation language familiarity is becoming less important to programmers in the age of AI coding assistants, and that Clojure yields simpler code structures that are easier for both humans and agents to reason about. This aligns with and independently supports the project’s recent decision to prefer Clojure over Python for the multi-model committee orchestrator (see `research-programs/committee-implementation-taxonomy.md`).
- **MOOLLM integration** — the adversarial committee mechanism has been incorporated into the MOOLLM platform, making the technique available to that platform’s user base.
- **Repository stars** — as of 2026-02-23, the git repository had two stars on the hosting platform (lightweight adoption signal).
- **Evidence so far**: Internal comparison runs and one external deliberation review (Condorcet run scored 13/15 High) support “suitable for early adopters” and give initial empirical evidence that deliberation structure (Robert’s Rules, adversarial back-and-forth) changes outcomes vs. independent vote. No failure reports or sustained multi-session external use reported yet; no rubric scores from purely external deliberations.

---

## Trajectory in brief

Uptake moved quickly after the Feb 1 gap call: two forks and MOOLLM integration by mid–late Feb 2026. One fork delivered concrete artifacts (Condorcet–committee relationship, comparison protocol, two comparison runs) and demonstrated that process structure can flip verdicts. The other fork engaged with theory (Deleuze, Residuality). That combination — portable technique plus theoretical extension — is a stronger signal than originally expected at this stage.

By early March 2026, both contributors remain active with new PRs. The contributions are deepening: the Condorcet contributor is moving from "does deliberation structure matter?" (answered: yes) toward "can we track individual character contributions over time?" — a longitudinal dimension the methodology hasn't explored. The Residuality contributor is connecting the project's Clojure implementation preference to a broader argument about language simplicity and agent-readability in software engineering practice. Both PRs extend the methodology in directions the core team was already moving, which suggests the design is legible enough that independent contributors converge on productive directions without coordination.

The full dated event log is in [usage-and-uptake-chronology.md](usage-and-uptake-chronology.md).

---

## Open questions for practitioners

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

**Last updated**: March 5, 2026
