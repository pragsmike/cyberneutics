# Rubric: Repository Audience Experience

**Purpose**: Score the Cyberneutics repository's contents for how well they meet the needs of their target audiences and how delightful (orienting, trustworthy, low-friction, satisfying) the experience is. Used by the editorial-review prompt to assess current state and to drive a remediation plan.

**Scope**: Applies to the documented surface of the repo: essays, artifacts, palgebra (and optionally README, CLAUDE.md, meta, applications) as specified by the review prompt. Not a measure of methodological correctness—only of whether the *presentation* serves readers.

**Audiences** (from README and essays/README): Practitioners (want to use the methodology), Theorists (want the synthesis), Skeptics (want evidence and limits), Formalists (want precise machinery). Plus: Researchers, "anyone frustrated" with shallow AI—served via same paths.

**Scoring**: 0–3 per dimension. Total or per-dimension scores can be used to prioritize remediation. "High" = consistently 2–3 across dimensions and no dimension at 0.

---

## Quick Reference

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Audience paths** | No clear paths or wrong | Paths exist but incomplete/wrong | Paths coherent, minor gaps | Each audience has entry + coherent path |
| **Conceptual coherence** | Undefined terms, broken order | Some definitions, some forward refs | Mostly coherent, small fixes | First-use definitions, consistent terms, clear progression |
| **Tone and register** | Inconsistent or wrong for audience | Mixed; some jarring shifts | Mostly "serious but accessible" | Consistent, audience-appropriate, no talk-down or unexplained jargon |
| **Actionability** | Can't do anything after reading | Partial (e.g. theory but no try) | Can try technique or follow argument | Practitioners can run; theorists get full argument; skeptics get evidence; formalists get notation |
| **Trust and honesty** | Hand-waving, hidden limits | Some limits, some unsupported claims | Limits and evidence mostly present | Limits explicit, claims supported or flagged, skeptics addressed |
| **Navigation and findability** | Lost in structure, broken links | Structure exists but misleading | Mostly findable, minor link/description issues | READMEs/indexes accurate, links work, structure matches mental model |
| **Delight / experience** | Frustrating, disoriented, no payoff | Some payoff, noticeable friction | Good payoff, minor friction | Oriented quickly, low friction, satisfying payoff (insight or first success) |

---

## Dimension 1: Audience Paths

**What this measures**: Whether each defined audience has a clear entry point and a reading/doing path that is documented, accurate, and coherent.

- **0 — No clear paths or paths wrong**: No audience-specific guidance, or paths point to wrong/missing content, or paths contradict each other.
- **1 — Paths exist but incomplete or wrong**: Some paths documented (e.g. in essays/README) but missing audiences, or paths skip essential material, or descriptions don't match content.
- **2 — Paths coherent with minor gaps**: Each audience has an entry and a sequence; one or two essays/artifacts miscategorized, or one path (e.g. Theorist) omits items that are in Core Essays without explanation.
- **3 — Each audience well served**: Clear entry (e.g. Start Here, Quick Start, or first essay); path is complete and logically ordered; any intentional omissions (e.g. "minimal theorist sequence") are stated; paths are easy to discover from README/essays README.

---

## Dimension 2: Conceptual Coherence and Exposition

**What this measures**: First-use definitions, consistent terminology, logical progression within and across documents. No concept used before it is introduced; no unexplained synonym drift.

- **0 — Major coherence failures**: Key concepts used undefined; terminology drifts without acknowledgment; reading order assumes later material; broken or circular cross-references.
- **1 — Some coherence**: Some concepts defined on first use; some forward references or undefined terms; terminology mostly stable but with notable exceptions.
- **2 — Mostly coherent**: First-use definitions and progression largely correct; a few forward refs or redundant restatements that could be tightened.
- **3 — Fully coherent**: Every key concept defined before or at first use; consistent terms (or explicit "also called X"); clear build order within and across essays/artifacts; cross-references accurate and helpful.

---

## Dimension 3: Tone and Register

**What this measures**: Consistency of voice ("serious but accessible"), appropriateness for each audience, and absence of talking down or unexplained jargon.

- **0 — Inconsistent or wrong**: Voice swings arbitrarily (e.g. academic then chatty); audience mismatch (e.g. practitioner path is jargon-heavy); condescension or unexplained specialist language.
- **1 — Mixed**: Some essays/sections hit the right register; others jar (e.g. one essay much denser than the rest without warning); some jargon not glossed.
- **2 — Mostly consistent**: Collection feels "serious but accessible" overall; a few passages too dry or too casual; audience appropriateness generally good.
- **3 — Consistently appropriate**: Register stable across the collection; each path matches its audience (practitioners get plain language and examples, theorists get rigor, skeptics get no hand-waving); no talking down; jargon introduced when used.

---

## Dimension 4: Actionability

**What this measures**: Whether readers can *do* something valuable after engaging—run a technique, follow a full argument, check evidence, or use formal machinery.

- **0 — Not actionable**: Practitioners can't run anything; theorists get incomplete arguments; formalists lack definitions or notation; skeptics get no testable claims or evidence.
- **1 — Partially actionable**: Some paths lead to action (e.g. quick start exists) but others don't; or one audience (e.g. formalists) is well served and others aren't; or first success is blocked by missing steps.
- **2 — Largely actionable**: Practitioners can run at least one technique with documented steps; theorists get complete arguments along their path; skeptics get failure modes and scope; formalists get usable notation. Minor gaps (e.g. one artifact underspecified).
- **3 — Fully actionable**: Each audience can achieve a clear payoff—practitioner runs a committee, theorist follows the synthesis, skeptic sees limits and evidence, formalist applies the algebra. No critical missing step.

---

## Dimension 5: Trust and Honesty

**What this measures**: Explicit acknowledgment of limitations and failure modes; support or clear labeling of claims (citation, argument, or "open question"); no hand-waving where evidence is expected (especially for skeptics).

- **0 — Undermines trust**: Limitations hidden; strong claims unsupported; failure modes or scope unmentioned; skeptic path would see hand-waving.
- **1 — Partial**: Some limits or failure modes mentioned; some claims cited; other claims presented as fact without support; skeptic path has some honest material but gaps.
- **2 — Mostly trustworthy**: Limitations and failure modes documented (e.g. when-methodology-fails); most substantive claims supported or flagged; open questions identified. Minor unsupported claims or one audience under-served.
- **3 — High trust**: Limits and failure modes explicit and findable; claims either supported (citation/argument) or clearly flagged (e.g. "open question," "we predict"); skeptic path is evidence-aware and scope-aware; no deceptive or oversold claims.

---

## Dimension 6: Navigation and Findability

**What this measures**: Whether READMEs, indexes, and directory structure accurately describe content; links work; and the structure matches how audiences think (getting started, theory, techniques, reference).

- **0 — Hard to navigate**: Structure confusing or misleading; broken links; descriptions don't match content; readers routinely lost.
- **1 — Navigable with effort**: Main entry points exist; some broken or outdated links; indexes incomplete or inaccurate; readers can get there but with friction.
- **2 — Generally findable**: README and essays/artifacts READMEs describe content well; links mostly work; structure supports "I want theory" / "I want to try" / "I want the formalism." A few link or description fixes needed.
- **3 — Excellent findability**: READMEs and indexes accurate and scannable; all links valid; structure aligns with audience mental models; cross-references between essays, artifacts, and palgebra are correct.

---

## Dimension 7: Delight / Experience

**What this measures**: Subjective but observable—readers feel oriented (not lost), experience low friction (don't hit dead ends or confusion spikes), and reach a satisfying payoff (insight or first success) without persistent frustration.

- **0 — Frustrating**: Readers report being lost, blocked, or misled; payoff (e.g. first committee run, understanding the synthesis) is unreachable or feels like a bait-and-switch; high friction throughout.
- **1 — Payoff exists but friction high**: Some readers succeed; others hit dead ends, wrong order, or "I still don't know how to start." Examples or summaries help but aren't enough to overcome structure issues.
- **2 — Good experience with minor friction**: Most readers can orient, follow a path, and reach a payoff; a few friction points (e.g. one essay too long, one link wrong, one concept introduced late). Experience is "good" but improvable.
- **3 — Delightful**: Quick orientation ("I know where I am and what to do next"); minimal friction; payoff is reachable and satisfying (e.g. "I ran my first deliberation" or "I see how the theory hangs together"). Metaphors and examples land; no persistent frustration.

---

## How to Use This Rubric

1. **Define scope**: Apply to the set of documents specified in the editorial-review prompt (e.g. essays 01–11 plus supporting essays, plus README/essays README; optionally artifacts, palgebra, root README).
2. **Score per dimension**: Walk the repo (and each reading path) and assign 0–3 for each of the seven dimensions. Cite specific files, sections, or links that justify the score.
3. **Summarize**: Report dimension scores and a short justification. Flag dimensions at 0 or 1 as priority for remediation.
4. **Remediation**: Use low scores to drive a concrete plan—changes to content, structure, or cross-references—so that the repo scores 2–3 on every dimension. Prioritize by impact (e.g. audience paths and actionability first) and effort.

**Reference**: README.md (Who is this for? Getting started), essays/README.md (Reading paths, Core/Supplementary), CLAUDE.md (repository map, voice), artifacts/README.md (techniques index).
