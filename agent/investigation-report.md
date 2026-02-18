# Investigation Report: MOOLLM Debate Structure and Cyber-Sense Alignment

**Purpose:** Understand how the mg-moollm debate (source-code-organization) was structured and conducted, infer plausible prompts and workflow, and identify how to align cyber-sense committee and review skills with the same deliberation-record structure. All work is self-contained under the cyber-sense directory.

**Artifacts examined:**
- `mg-moollm/debates/source-code-organization/` (00–04, DEBATE.yml, ROOM.yml)
- `MOOLLM/skills/adversarial-committee/` (SKILL.md, SELECTION.md)
- `cyber-sense/.claude/skills/committee/SKILL.md`
- `cyber-sense/.claude/skills/review/SKILL.md`
- `cyber-sense/artifacts/` (character-propensity-reference, committee-setup-template, evaluation-rubrics-reference)

---

## 1. MOOLLM Deliberation Record Structure (Numeric Prefix)

The **essential** files are those with numeric prefixes; they define the debate lifecycle. Non-prefixed files (e.g. ROOM.yml, DEBATE.yml) support MOOLLM room/adventure conventions and are optional for a self-contained cyber-sense implementation.

| File | Role | Essential for cyber-sense |
|------|------|---------------------------|
| **00-charter.yml** | Goal, context, success_criteria, exit_conditions, deliverable_format | Yes |
| **01-roster.yml** | Committee name, size, members (name, role; MOOLLM uses `file:` to character YAMLs) | Yes |
| **01-convening.md** | Phase 1 convening: date, selection strategy, rationale, composition notes, outcome | Yes |
| **02-deliberation.md** | Phase 2: topic, protocol, opening statements, rounds, analyses, final consensus | Yes |
| **03-resolution.yml** | Phase 3: decision, summary, details, implementation_plan, votes, signatures | Yes |
| **04-evaluation.yml** | Phase 4: rubric scores, decision (e.g. RATIFIED), critique, recommendation | Yes |
| DEBATE.yml | Global state: name, topic, current_phase, participants, state, io status | Optional |
| ROOM.yml | Room description, working_set, exits, objects | Optional (MOOLLM-specific) |

---

## 2. How the Debate Was Conducted (Plausible Reconstruction)

### 2.1 Phase 0: Charter

- **00-charter.yml** defines:
  - **goal:** one-sentence objective (e.g. strategy for source code organization).
  - **context:** 2–3 sentences (current situation, why the question matters).
  - **success_criteria:** bullet list (clear boundary, mechanism for user content, plan for dependencies).
  - **exit_conditions:** what “done” means (consensus, recommended changes).
  - **deliverable_format:** e.g. “Resolution Artifact (YAML)”.

**Plausible prompt:** Given a topic/question, produce a charter YAML with goal, context, success_criteria, exit_conditions, and deliverable_format so the committee has a single shared mandate.

### 2.2 Phase 1: Roster and Convening

- **01-roster.yml** lists a named committee, size (e.g. 6), and members with `name`, `file` (path to character YAML), and `role` (devil's_advocate, opportunity_scout, historian, evidence_checker, systems_analyst, operational_reality_check).
- **01-convening.md** records:
  - Date and **selection strategy** (e.g. “Balanced (FORM-SMART)”).
  - **Selection rationale:** why these members (core 5 + optional 6th), diversity, risk balance.
  - **Composition notes:** tensions (e.g. Maya vs Frankie), grounding (Joe, Vic, Samir), exploration (Tammy, Frankie, Maya), consensus potential, blind-spot coverage.
  - **Outcome:** e.g. “Committee successfully convened with 6 members.”

**Plausible prompts:**
1. From charter + character pool: select a committee (e.g. FORM-SMART/balanced) and emit **01-roster.yml**.
2. From roster: write **01-convening.md** (selection rationale, composition, outcome) so the debate has an auditable “why this committee” record.

MOOLLM uses 6 members (Maya, Frankie, Joe, Vic, Tammy, Samir); cyber-sense uses the fixed 5 (no Samir). Roster content should stay within cyber-sense’s existing roster (see Section 4).

### 2.3 Phase 2: Deliberation

- **02-deliberation.md** is a long markdown transcript containing:
  - **Header:** Phase 2, topic (question), protocol (e.g. Robert’s Rules).
  - **Opening statements:** one subsection per member (name + role), 1–3 paragraphs each.
  - **Initial positions summary:** table (Member, Stance, Confidence, Key Concern).
  - **Key tensions identified:** numbered list.
  - **Rounds:** e.g. “Round 1: Separation vs. Integration” with Chair directing and members responding in character; after each round, **Round N Analysis** (emerging consensus, new tension, status, next step).
  - **Final consensus:** bullet list of agreed points (e.g. “Federalist Directory Model”) and status “DELIBERATION COMPLETE.”

**Plausible prompts:**
1. **Opening statements:** Given charter + roster (and character references), each member produces an opening statement from their propensity; output is collected under “Opening Statements” and “Initial Positions Summary” and “Key Tensions Identified.”
2. **Rounds:** Chair introduces a tension or question; members respond in turn; after each round, analyst (or same model) produces “Round N Analysis” and sets “Next” (e.g. next round or “Phase 3: Resolution”).
3. **Closing:** Final whip-around and “Final Consensus” section.

So the debate is conducted as **multi-step generation**: charter → roster/convening → opening statements + summary + tensions → one or more rounds with analyses → final consensus. Robert’s Rules is the named protocol; the actual flow is “Chair + members + round analysis.”

### 2.4 Phase 3: Resolution

- **03-resolution.yml** is structured YAML:
  - **resolution:** date, topic, outcome (e.g. PASSED Unanimous), decision (one line), summary (paragraph), details (structure/mechanics), implementation_plan (list of actions), votes (per member), signatures (chair, ratified_by).

**Plausible prompt:** From charter + 02-deliberation.md (especially Final Consensus), produce a resolution YAML that satisfies the charter’s deliverable_format and records who agreed and how.

### 2.5 Phase 4: Evaluation

- **04-evaluation.yml** is produced by an **independent evaluator** that does **not** see the transcript:
  - **inputs:** charter (00-charter.yml), resolution (03-resolution.yml) only.
  - **rubric:** criteria (e.g. alignment_with_goal, completeness, feasibility, risk_mitigation).
  - **scores:** per criterion, score (e.g. 5/5), rationale.
  - **decision:** outcome (e.g. RATIFIED), confidence.
  - **critique:** strengths, weaknesses.
  - **recommendation:** e.g. “Proceed to Implementation.”

**Plausible prompt:** Given only 00-charter.yml and 03-resolution.yml, score the resolution against the stated rubric and output 04-evaluation.yml. This mirrors cyber-sense’s “review as found document” idea but applied to the resolution artifact instead of the full transcript.

---

## 3. Differences from Current Cyber-Sense Behavior

| Aspect | MOOLLM (source-code-organization) | Cyber-sense (current) |
|--------|-----------------------------------|------------------------|
| **Output shape** | Directory of files (00–04 + optional) | Single inline transcript (or one .md file) |
| **Charter** | Explicit 00-charter.yml | Implicit (topic + context in prompt) |
| **Roster** | 01-roster.yml + 01-convening.md | Fixed 5 in skill text + artifacts |
| **Deliberation** | 02-deliberation.md with rounds + analyses | One flow: perspectives → debate → synthesis |
| **Resolution** | 03-resolution.yml (structured) | Free-form “DECISION SPACE MAP” + “VERDICT” in transcript |
| **Evaluation** | 04-evaluation.yml (charter + resolution only) | /review on full transcript, five rubrics, no resolution artifact |
| **Roster size** | 6 (with Samir) | 5 (Maya, Frankie, Joe, Vic, Tammy) |
| **Character refs** | External `file:` per member | In-repo artifacts/character-propensity-reference.md |

---

## 4. Cyber-Sense Roster and Artifacts (Self-Contained)

Cyber-sense already has a **fixed 5-member roster** and supporting artifacts under its own tree:

- **Roster:** Maya, Frankie, Joe, Vic, Tammy (no Samir). Roles and propensities are in:
  - `.claude/skills/committee/SKILL.md` (standard roster and dynamics)
  - `artifacts/character-propensity-reference.md` (calibration, failure modes)
  - `artifacts/committee-setup-template.md` (prompt templates)
- **Evaluation:** Five rubrics (reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness) in:
  - `.claude/skills/review/SKILL.md`
  - `artifacts/evaluation-rubrics-reference.md`
  - `artifacts/independent-evaluation.md`

The augmentation plan should **not** refer to files outside cyber-sense. All roster and rubric references must stay under `cyber-sense/` (e.g. `artifacts/...`, `.claude/skills/...`). Deliberation records (the new directory structure) will live under something like `cyber-sense/agent/deliberations/<topic-slug>/` so everything remains self-contained.

---

## 5. Summary: What to Reuse and What to Add

- **Reuse from MOOLLM:** The **numeric-prefix directory layout** (00–04) and the **lifecycle**: charter → roster/convening → deliberation → resolution → evaluation. Also the idea of **evaluation from charter + resolution only** (no transcript) for an independent check.
- **Reuse from cyber-sense:** The **existing 5-character roster**, character propensity reference, committee setup template, and the **five rubrics** used by the review skill. Committee and review behavior (adversarial rigor, evidence, trade-offs) stay as-is; only the **output layout** and **artifact types** change.
- **Add under cyber-sense:** A defined **deliberation record directory** (e.g. `agent/deliberations/<topic>/`) containing 00–04 (and optionally a minimal DEBATE.yml if useful). Committee skill extended to **write** these files; review skill extended to **read** from this structure and optionally **write** 04-evaluation.yml. No references to MOOLLM or mg-moollm paths; all file paths are relative to cyber-sense.

The next document (**augmentation-plan.md**) specifies concrete steps to augment the committee and review skills so they produce and consume this structure using only cyber-sense’s roster and artifacts.
