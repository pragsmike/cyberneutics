# Augmentation Plan: Committee and Review Skills with Directory-Structured Deliberation Records

**Goal:** Augment the cyber-sense committee and review skills so deliberation records follow the same directory structure as the MOOLLM debates (numeric-prefix files 00–04), while remaining **self-contained under the cyber-sense directory** and using only the **existing committee roster and artifacts**.

**Reference:** `agent/investigation-report.md` (how the debate was conducted, what’s essential, what differs from current cyber-sense).

---

## 1. Target Structure: Deliberation Record Directory

Each deliberation gets its own directory under cyber-sense. Recommended location:

```
cyber-sense/agent/deliberations/<topic-slug>/
  00-charter.yml
  01-roster.yml
  01-convening.md
  02-deliberation.md
  03-resolution.yml
  04-evaluation.yml
```

- **topic-slug:** Short, filesystem-safe name derived from the topic (e.g. `microservices-migration`, `is-author-crackpot`). No references to paths outside `cyber-sense/`.
- **Optional:** A minimal `DEBATE.yml` (name, topic, current_phase) can be added later if useful for tooling; **ROOM.yml is omitted** (MOOLLM-specific).

All paths in skill text and artifacts are relative to the cyber-sense repo (e.g. `artifacts/character-propensity-reference.md`, `agent/deliberations/<topic>/02-deliberation.md`).

---

## 2. File Schemas (Cyber-Sense Variant)

Schemas below are tailored to cyber-sense: fixed 5-member roster, no external character `file:` references, rubrics from existing review skill.

### 2.1 `00-charter.yml`

```yaml
# Phase 0: Charter
charter:
  goal: "<one-sentence objective>"
  context: |
    <2-4 sentences: current situation, why the question matters>
  success_criteria:
    - "<criterion 1>"
    - "<criterion 2>"
  exit_conditions:
    - "<what 'done' looks like>"
  deliverable_format: "Resolution Artifact (YAML) + Decision Space Map"
```

Filled from the user’s topic (and any clarification). No external refs.

### 2.2 `01-roster.yml`

```yaml
# Phase 1: Roster (fixed cyber-sense committee)
roster:
  committee_name: "Cyber-Sense Adversarial Committee"
  size: 5
  members:
    - name: "Maya"
      role: devil's_advocate
      propensity: paranoid_realism
    - name: "Frankie"
      role: opportunity_scout
      propensity: idealism
    - name: "Joe"
      role: historian
      propensity: continuity_guardian
    - name: "Vic"
      role: evidence_checker
      propensity: evidence_prosecutor
    - name: "Tammy"
      role: systems_analyst
      propensity: systems_thinking
```

No `file:` fields. Character details stay in `artifacts/character-propensity-reference.md` and the committee skill. Optional: add a `source: "artifacts/character-propensity-reference.md"` at roster level for documentation only.

### 2.3 `01-convening.md`

Markdown with:

- **Date**, **Selection strategy** (e.g. “Standard 5-member roster”).
- **Rationale:** Why this roster (diversity, tensions, coverage) — can be a short paragraph referencing the standard roster.
- **Composition notes:** Tensions (e.g. Maya vs Frankie), grounding (Joe, Vic), exploration (Tammy, Frankie).
- **Outcome:** e.g. “Committee convened with 5 members. See 01-roster.yml.”

No external links; all references stay under cyber-sense.

### 2.4 `02-deliberation.md`

Markdown with the same **content** as today’s committee output, but **structured** to match the MOOLLM-style phases:

- **Phase 2: Deliberation** — Topic, protocol (Robert’s Rules).
- **Opening Statements** — One subsection per member (Maya, Frankie, Joe, Vic, Tammy), 2–3 paragraphs each.
- **Initial Positions Summary** — Table: Member, Stance, Confidence, Key Concern.
- **Key Tensions Identified** — Numbered list.
- **Round 1, 2, …** — Chair + member exchanges; after each round, **Round N Analysis** (emerging consensus, new tension, status, next).
- **Final Consensus** — Bullet list; status: DELIBERATION COMPLETE.
- **KEY TENSIONS IDENTIFIED** / **ASSUMPTIONS SURFACED** / **EVIDENCE REQUIREMENTS** / **DECISION SPACE MAP** / **RECOMMENDED NEXT STEPS** (and if applicable **VERDICT** or **CONCLUSION**) — same as current committee skill output, so existing behavior is preserved while fitting the file.

So 02-deliberation.md is the **single canonical transcript** for this deliberation; the committee skill will be instructed to emit this structure into that file (or into the conversation in the same shape, then written to the file).

### 2.5 `03-resolution.yml`

```yaml
# Phase 3: Resolution
resolution:
  date: "<YYYY-MM-DD>"
  topic: "<topic string>"
  outcome: "PASSED | DEFERRED | NO_CONSENSUS"
  decision: "<one-line decision>"
  summary: |
    <paragraph summarizing what was decided>
  details:
    # Optional key-value structure
  implementation_plan: []  # Optional list of { action, description }
  votes:
    maya: "YES | NO | ABSTAIN | conditional text"
    frankie: "..."
    joe: "..."
    vic: "..."
    tammy: "..."
  signatures:
    chair: "Committee (Cyber-Sense)"
    ratified_by: "User"
```

Filled from the deliberation’s Final Consensus and DECISION SPACE MAP / VERDICT. Keeps resolution as a first-class artifact for evaluation.

### 2.6 `04-evaluation.yml`

Two possible sources of evaluation in cyber-sense:

- **A) Resolution-only evaluation (MOOLLM-style):** Independent evaluator sees only `00-charter.yml` and `03-resolution.yml`; scores alignment_with_goal, completeness, feasibility, risk_mitigation; outputs RATIFIED / REVISE / REJECT and critique. No transcript.
- **B) Transcript review (current /review):** Evaluator sees `02-deliberation.md` (and optionally charter) and scores the five rubrics (reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness).

**Plan:** Support both.

- **04-evaluation.yml** holds the **resolution-only** evaluation (schema below), so the directory has a clean “charter + resolution → score” record.
- The **review skill** continues to evaluate the **transcript** (02-deliberation.md) with the five rubrics; it can optionally **write** its summary into 04-evaluation.yml under a second key (e.g. `transcript_review`) or into a separate section so one file captures both resolution evaluation and transcript review.

Suggested **04-evaluation.yml** schema (resolution-only part):

```yaml
# Phase 4: Evaluation (resolution vs charter)
evaluation:
  id: "eval-<topic-slug>-001"
  timestamp: "<ISO8601>"
  inputs:
    charter: "00-charter.yml"
    resolution: "03-resolution.yml"
  rubric:
    criteria:
      - alignment_with_goal
      - completeness
      - feasibility
      - risk_mitigation
  scores:
    alignment_with_goal: { score: "5/5", rationale: "..." }
    completeness: { score: "4/5", rationale: "..." }
    feasibility: { score: "5/5", rationale: "..." }
    risk_mitigation: { score: "4/5", rationale: "..." }
  decision:
    outcome: "RATIFIED | REVISE | REJECT"
    confidence: "High | Medium | Low"
  critique:
    strengths: []
    weaknesses: []
  recommendation: "<one sentence>"
  # Optional: transcript_review summary (scores from /review) if review skill writes here
```

All paths in this file are relative to the deliberation directory (e.g. `00-charter.yml`, `03-resolution.yml`).

---

## 3. Committee Skill Augmentation

**Location:** `.claude/skills/committee/SKILL.md`

**Changes:**

1. **Output mode: directory vs inline**
   - Add an option (e.g. “when saving to a deliberation record” or “when user requests structured output”) to write the deliberation into `agent/deliberations/<topic-slug>/` instead of (or in addition to) inline response.
   - Topic-slug: derive from topic (lowercase, replace spaces with `-`, strip special chars). Example: “Should we adopt microservices?” → `microservices-adoption` or `microservices-migration`.

2. **Phased file production**
   - **Before deliberation:** From topic (+ optional user context), generate and write:
     - `00-charter.yml` (goal, context, success_criteria, exit_conditions, deliverable_format).
     - `01-roster.yml` (fixed 5-member roster as above; no external files).
     - `01-convening.md` (standard roster rationale, composition notes, outcome).
   - **During/after deliberation:** Write:
     - `02-deliberation.md` (full transcript in the structure of Section 2.4: opening statements, table, tensions, rounds + analyses, final consensus, KEY TENSIONS, ASSUMPTIONS, EVIDENCE REQUIREMENTS, DECISION SPACE MAP, RECOMMENDED NEXT STEPS, VERDICT/CONCLUSION if any).
   - **After synthesis:** Generate and write:
     - `03-resolution.yml` from Final Consensus and DECISION SPACE MAP / VERDICT (votes, summary, implementation_plan if applicable).

3. **References (self-contained)**
   - Skill text must only reference paths under cyber-sense, e.g.:
     - `artifacts/character-propensity-reference.md`
     - `artifacts/committee-setup-template.md`
     - `agent/deliberations/<topic-slug>/00-charter.yml` (and other 01–03 files).
   - Remove or generalize any mention of “previous deliberations” that pointed outside cyber-sense; “previous deliberations” = other directories under `agent/deliberations/`.

4. **Roster**
   - Keep the existing roster (Maya, Frankie, Joe, Vic, Tammy) and dynamics; 01-roster.yml is a **serialization** of that roster, not a new roster definition. No Samir, no external character files.

5. **Backward compatibility**
   - If the user does **not** request “structured output” or “save to deliberation record,” behavior remains: produce the same inline deliberation (phases 1–3 and output format as today). So existing `/committee [topic]` usage is unchanged unless the user opts in to directory output.

6. **Documentation in skill**
   - Add a short “Deliberation record directory” section describing the 00–04 layout and when it is used. Point to `agent/deliberations/` and `agent/augmentation-plan.md` (or a short `agent/deliberations/README.md` if added).

---

## 4. Review Skill Augmentation

**Location:** `.claude/skills/review/SKILL.md`

**Changes:**

1. **Input: from directory**
   - When the user runs `/review` and indicates a **deliberation directory** (e.g. “review agent/deliberations/microservices-migration” or “review the last deliberation record”), the skill should:
     - Resolve the directory (e.g. `agent/deliberations/<topic-slug>/`).
     - Read `02-deliberation.md` as the transcript (and optionally `00-charter.yml` for charter).
     - Optionally read `04-evaluation.yml` if it exists (to append or compare transcript review).
   - If no directory is given, keep current behavior: use the most recent committee output in the conversation or user-pasted transcript.

2. **Output: write 04-evaluation.yml (transcript review)**
   - When reviewing from a deliberation directory, the skill may **optionally** write the **transcript review** into that directory. Two options:
     - **A)** Add a `transcript_review` section to `04-evaluation.yml` (scores for the five rubrics, verdict, biggest gaps, recommendations). If 04-evaluation.yml does not exist yet, create it with only `transcript_review` (resolution-only evaluation can be added later or left empty).
     - **B)** Write a separate file, e.g. `04-transcript-review.yml` or `04-transcript-review.md`, and keep `04-evaluation.yml` for resolution-only evaluation.
   - Recommendation: **A)** single 04-evaluation.yml with optional keys `resolution_evaluation` and `transcript_review` so one file holds both evaluations.

3. **References (self-contained)**
   - All paths in the review skill stay under cyber-sense: `artifacts/evaluation-rubrics-reference.md`, `artifacts/independent-evaluation.md`, `agent/deliberations/<topic-slug>/...`.

4. **Integration with committee**
   - After a committee run that wrote to a deliberation directory, suggest: “Want me to run `/review` on this deliberation? I can evaluate the transcript and optionally update 04-evaluation.yml.”

---

## 5. New and Updated Artifacts Under cyber-sense

- **agent/deliberations/**  
  - Top-level directory for all deliberation records. Add `agent/deliberations/README.md` describing the 00–04 structure and that it is self-contained (no refs outside cyber-sense).

- **agent/deliberations/README.md** (optional but recommended)  
  - Short description: purpose of the directory, list of files (00–04), that roster comes from committee skill and `artifacts/character-propensity-reference.md`, and that evaluation uses `artifacts/evaluation-rubrics-reference.md`. No links outside cyber-sense.

- **agent/investigation-report.md** (done)  
  - Investigation summary; no external paths.

- **agent/augmentation-plan.md** (this file)  
  - Plan and file schemas; all paths relative to cyber-sense.

---

## 6. Implementation Order

1. **Create** `agent/deliberations/` and optionally `agent/deliberations/README.md` describing the 00–04 structure.
2. **Add** to committee skill: section “Deliberation record directory,” phased file production (00 → 01 → 02 → 03), topic-slug rule, self-contained path references. Keep inline mode as default; directory output opt-in.
3. **Implement** 00–03 file generation in committee flows (or in agent instructions that call the skill): charter from topic, fixed roster + convening, deliberation content into 02, resolution into 03.
4. **Add** to review skill: “Review from deliberation directory” (read 02-deliberation.md [+ 00-charter.yml]), optional write of transcript review into 04-evaluation.yml (or 04-transcript-review), self-contained paths.
5. **Define** who produces resolution-only 04 (e.g. separate “evaluator” step or a second pass of the review skill with only charter + resolution). Document in review skill or in `agent/deliberations/README.md`.
6. **Test** with one full run: create a deliberation directory, run committee with “save to deliberation record,” then run review on that directory and confirm 02 and 04 (and optionally 00, 01, 03) are present and consistent.

---

## 7. Out of Scope (Explicit)

- **ROOM.yml, DEBATE.yml:** Omitted unless we add minimal DEBATE.yml for tooling; no dependency on MOOLLM room/adventure semantics.
- **External character files:** Roster lives in skill + artifacts; 01-roster.yml has no `file:` pointing outside cyber-sense.
- **Samir / 6th member:** Not added; roster remains the existing 5.
- **References to MOOLLM or mg-moollm:** All documentation and paths stay under cyber-sense; the “same structure” is the numeric-prefix lifecycle (00–04), not shared files or repos.

This plan makes the deliberation record a **first-class, directory-shaped artifact** under cyber-sense while keeping committee and review behavior and roster unchanged except for output layout and file I/O.
