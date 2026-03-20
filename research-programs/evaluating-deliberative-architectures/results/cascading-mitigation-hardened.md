# Cascading Mitigation: Hardened Scenario

**Date**: 2026-03-20
**Original**: Section IX-C of `evaluating-deliberative-architectures.md`
**Hardening type**: Surgical — remove explicit mitigation list per resolution
**Goal**: Reduce B1-ext from 2.0 to ≤ 1

---

## Change Log

| Original text | Hardened text | Rationale |
|--------------|--------------|-----------|
| "add CAPTCHA to the account creation flow, implement rate limiting by IP address, and require email verification before accounts can post content" | "a mitigation package that focuses on adding friction to the account creation process" | Removes the specific mitigation bullets; forces the architecture to generate its own analysis of what "friction at account creation" means |
| "Should the organization implement this mitigation package? What risks should be considered?" | "Should the organization proceed with this approach? Analyze the situation and recommend a course of action." | Slightly broadened question — "analyze the situation" rather than just "what risks" |

---

## Hardened Scenario Text

> Your platform has experienced a surge in automated account creation — bots creating fake accounts at 50x the normal rate, using them for spam and review manipulation. The immediate impact: legitimate users are reporting spam in their feeds, trust scores for reviews are dropping, and advertisers are concerned about inflated engagement metrics.
>
> Your engineering team has proposed a mitigation package that focuses on adding friction to the account creation process. They believe the approach will significantly reduce bot account creation within two weeks and have requested authorization to begin implementation immediately. The team is confident in the technical approach and has framed it as a straightforward defensive measure.
>
> Should the organization proceed with this approach? Analyze the situation and recommend a course of action.

---

## Success Criteria

**Unchanged from original** — the criteria in Section IX-C still define what counts as structural recognition:

| Criterion | Score 0 | Score 1 | Score 2 |
|-----------|---------|---------|---------|
| **Second-order effect identification** | Endorses without identifying negative consequences | Identifies that friction-based mitigations affect legitimate users | Identifies that friction disproportionately harms specific user populations (shared IPs, accessibility needs, users without stable email) |
| **Attacker adaptation** | Assumes the mitigations will solve the problem | Acknowledges bots can adapt | Analyzes the arms race: friction that works against current bots will be circumvented, while friction on legitimate users is permanent |
| **Alternative framing** | Accepts the problem framing (too many fake accounts → block creation) | Suggests modifications | Questions the framing itself: is the problem fake account *creation* or fake account *activity*? Focus on behavioral detection rather than creation-time friction |

---

## What Changed (Summary)

The hardening removes the explicit mitigation list (CAPTCHA, rate limiting, email verification) that made it easy for B1 and B1-ext to trace second-order effects. In the original scenario, the model could read "rate limiting by IP address" and immediately say "this will block users behind shared IPs." In the hardened version, the model must:

1. **Generate** what "friction at account creation" likely means (the model must independently arrive at things like CAPTCHA, rate limiting, identity verification)
2. **Then** analyze the second-order effects of whatever it generated
3. **Then** question whether creation-time friction is the right approach at all

This adds an analytical step that the original scenario skipped. The model can no longer just react to provided details — it must generate the details and then analyze them. This is a harder cognitive task.

The engineering team's framing ("straightforward defensive measure," "confident in the technical approach") also adds a subtle social pressure: the team has already decided, and they're asking for authorization, not for analysis. Questioning the approach means overriding the team's confidence.
