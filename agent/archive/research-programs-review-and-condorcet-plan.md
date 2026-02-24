# Research-Programs Review & Condorcet Integration Plan

**Date**: 2026-02-24
**Purpose**: (1) Verify consistency of `meta/research-programs/`, (2) locate and summarize the condorcet experiment, (3) plan its incorporation as a research program.

---

## Part 1: Review and Verification of `meta/research-programs/`

### What was checked

- All five files in the directory: `README.md`, `evaluation-schemes.md`, `ablation-study.md`, `multi-model-committee.md`, `societies-of-thought-research-plan.md`
- The `ablation-study/results/README.md` placeholder
- External references from: `meta/README.md`, `meta/research-plan.md`, `agent/handoff-2026-02-22.md`, `agent/gap_analysis.md`, `essays/societies-of-thought-synthesis.md`, `meta/methodology-evolution.md`, `references/README.md`, `CLAUDE.md`

### Consistency with Conventions

The Conventions section of `research-programs/README.md` specifies three rules: (a) each study has a plan file + results folder, (b) completed studies get a Status section with Runs and links, (c) plans are not archived on completion.

| Plan file | Convention compliance | Notes |
|-----------|----------------------|-------|
| `ablation-study.md` | **Good.** Has Status ("Not started"), Runs ("none yet"), and a results link to `ablation-study/results/`. Results folder exists with a README placeholder. Matches the convention exactly. | — |
| `evaluation-schemes.md` | **Acceptable.** Has a Status line ("Ready for implementation") at the bottom, but not in the structured `Status: / Runs: / Results:` format the convention describes. No results folder (none needed yet — it's a design doc, not a study with runs). Design F (ablation) is correctly extracted to its own plan. | Minor: could add a formal Status/Runs section at the top for consistency with ablation-study.md. |
| `multi-model-committee.md` | **Missing Status section.** No Status/Runs/Results block. The document is an experimental protocol, not yet executed — "Not started" status would be appropriate. No results folder. | Recommend adding a Status section at the top. |
| `societies-of-thought-research-plan.md` | **Missing Status section.** Ten action items but no overall Status/Runs block. Individual items don't have status markers either. No results folder. | Recommend adding either an overall Status or per-item status checkboxes (the success criteria at the end have checkboxes but these are aspirational, not run-tracking). |

**Internal links between programs**: The `evaluation-schemes.md` → `ablation-study.md` link works correctly. The `ablation-study.md` → `evaluation-schemes.md` back-link works. The `README.md` priority table links to all four plans correctly. The "Related" section at the bottom of README links to `meta/README.md`, `essays/societies-of-thought-synthesis.md`, and `agent/gap_analysis.md` — all paths correct with proper relative paths.

**"Where to start" / "Active research programs" / "By theme" index accuracy**: The priority table lists all four active plans plus gap_analysis as reference. The "Active research programs" table lists all four. The "Completed / reference programs" table lists four archived plans in `agent/archive/`. The "By theme" table covers Validation, Theory, Infrastructure, Integration. All accurate and complete for the programs that currently exist. The condorcet work (comparisons, protocol, artifact) is **not listed** — see Part 3.

### External References Check

| Source file | What it says | Status |
|-------------|-------------|--------|
| `meta/README.md` | Links to `research-programs/README.md` and lists all four active plans by name with correct paths | **Correct** |
| `meta/research-plan.md` | Redirect stub pointing to `research-programs/README.md` and three specific plans | **Correct** |
| `essays/societies-of-thought-synthesis.md` | Links to `meta/research-programs/societies-of-thought-research-plan.md` (two references) | **Correct** |
| `meta/methodology-evolution.md` | Mentions `meta/research-programs/societies-of-thought-research-plan.md` (one reference, line 280) | **Correct** (path is a narrative mention, not a markdown link, but accurate) |
| `references/README.md` | Links to `meta/research-programs/README.md` in the MOOLLM entry | **Correct** |
| `agent/gap_analysis.md` | References extraction of research plan to `meta/research-programs/societies-of-thought-research-plan.md` | **Correct** |
| `agent/handoff-2026-02-22.md` | Describes research-programs creation, lists all files, notes redirect | **Correct** |
| `CLAUDE.md` | Does not directly reference `meta/research-programs/` (references `meta/` generally and `agent/gap_analysis.md`) | **No issue** — CLAUDE.md's repo map points to `meta/` broadly |

**No stale references found.** No documents still point at old locations like `meta/research-plan.md` as the primary plan (the redirect is in place), `agent/evaluation-schemes-analysis.md`, or `agent/multi-model-committee-analysis.md`. The move and reference update from the 2026-02-22 session was thorough.

### Recommended Fixes (Part 1)

1. **Add Status sections** to `multi-model-committee.md` and `societies-of-thought-research-plan.md` (top of file, matching `ablation-study.md` format: `**Status**: Not started / **Runs**: (none yet) / **Results**: [path]`).
2. **Consider adding a Status section** to `evaluation-schemes.md` at the top for visual consistency, even though it's primarily a design doc rather than a single study.
3. These are minor formatting inconsistencies, not broken references or structural problems.

---

## Part 2: The Condorcet Experiment — What Exists

### Origin and Design

The condorcet work was produced in a single session on 2026-02-22 (documented in `agent/archive/handoff-2026-02-22-condorcet.md`). The question was: **does the deliberative committee pipeline produce different outcomes than a CJT-style (Condorcet jury theorem) independent-vote-then-aggregate pipeline on the same question?**

The experiment had three phases:

1. **Conceptual clarification**: A committee deliberation asked "should we correct for Condorcet's jury theorem?" The committee unanimously recommended: document the relationship, don't change the process. This produced the artifact `artifacts/condorcet-jury-theorem-and-committee.md`, which states the committee's design goals first, treats CJT as a motivating analogy, lists three explicit deviations (no independence, no binary outcome, no literal competence probability), and concludes that a CJT-compliant variant would be a *different* pipeline.

2. **Protocol design**: A reusable comparison protocol was created (`artifacts/comparison-protocol-deliberative-vs-cjt.md`) defining how to run both pipelines (deliberative via `/committee` and CJT-style via independent votes) on the same question with the same roster and charter, then compare outcomes.

3. **Two comparison runs** using the protocol, stored in `agent/comparisons/`:
   - **second-ci-job**: "Should we add a second CI job?" Both pipelines said Nay. CJT 4-1, Deliberative 5-0. Same verdict; deliberation changed one vote (Frankie Aye→Nay) and added a revisit condition.
   - **code-of-conduct**: "Should we add a Code of Conduct?" **Opposite verdicts.** CJT Aye 3-2, Deliberative Nay 5-0. Three votes flipped after debate on enforcement and weaponization risk.

### Artifacts Produced and Their Locations

| Artifact | Location | Type |
|----------|----------|------|
| Condorcet deliberation (5 files) | `agent/deliberations/condorcet-jury-theorem-process/` (00-charter through 04-evaluation) | Deliberation record |
| Condorcet conceptual artifact | `artifacts/condorcet-jury-theorem-and-committee.md` | Published artifact |
| Comparison protocol | `artifacts/comparison-protocol-deliberative-vs-cjt.md` | Published artifact (reusable) |
| Comparisons README | `agent/comparisons/README.md` | Index |
| second-ci-job comparison (4 files) | `agent/comparisons/second-ci-job/` | Comparison run |
| second-ci-job deliberation (2 files) | `agent/deliberations/second-ci-job/` | Deliberation record |
| code-of-conduct comparison (4 files) | `agent/comparisons/code-of-conduct/` | Comparison run |
| code-of-conduct deliberation (2 files) | `agent/deliberations/code-of-conduct/` | Deliberation record |
| Condorcet session handoff | `agent/archive/handoff-2026-02-22-condorcet.md` | Session record |
| PR review of condorcet work | `agent/archive/condorcet-pr-review.md` | Review |
| Cross-ref in adversarial-committees | `artifacts/adversarial-committees.md` (one-line link added) | Cross-reference |

### Findings and Conclusions

The PR review (`agent/archive/condorcet-pr-review.md`) provides the most thorough assessment:

- **Headline finding**: On the code-of-conduct question, CJT-style said Aye (3-2) while deliberative said Nay (5-0). Three characters voted Aye in isolation but flipped to Nay after the enforcement/weaponization objection was raised in debate. The key objection existed in the CJT run (Maya and Joe raised it) but the Aye voters never had to respond to it. In deliberation, the Chair forced engagement.

- **Interpretation**: The comparison provides initial empirical evidence that process matters — same question, same roster, different process, different verdict. Value-laden questions with hidden enforcement or second-order concerns appear to be the question types where the pipelines diverge.

- **Limitations acknowledged**: Two datapoints, not a study. Independence is imperfect (single model session). No ground truth — we can't say the deliberative answer was *better*, only that it was different and more rigorously arrived at.

- **Fit with methodology**: The PR review confirms strong fit with all five core ideas and specifically notes that the comparison runs are "the methodology's first empirical evidence for the value of structured deliberation" and "the strongest evidence yet for why Robert's Rules matters."

### Current Citation in research-programs

The condorcet work is **not currently cited** in `meta/research-programs/README.md`. It is mentioned in `meta/methodology-evolution.md` (lines 306-309) as a milestone but not as a research program. The `evaluation-schemes.md` "highest priority" row addresses the same overarching question ("Does committee-based deliberation beat simpler prompting?") but does not reference the condorcet comparisons as existing evidence. The gap_analysis does not mention the condorcet work.

---

## Part 3: Plan to Add a Condorcet Research Program

### Target Format

Following the conventions in `research-programs/README.md` and using `ablation-study.md` as a structural template:

- **Plan file**: `meta/research-programs/condorcet-comparison.md`
- **Results directory**: `meta/research-programs/condorcet-comparison/results/`
- **Structure**: Objective, Procedure, Status (with Runs), Results link, Findings summary
- **Key difference from previous plan**: Experimental results (deliberation records, comparison records) are **moved** into the program's results directory so that the completed study is self-contained under `research-programs/`, as if it had been conducted under the current protocols from the start. Handoffs, PR reviews, and published artifacts stay where they are.

### Inventory: What Moves and What Stays

**Moves into `meta/research-programs/condorcet-comparison/results/`:**

| Current location | Contents | Move to |
|------------------|----------|---------|
| `agent/comparisons/second-ci-job/` (5 files: 00-charter, 01-deliberative-summary, 02-cjt-style-votes, 03-cjt-style-result, 04-comparison-summary) | CJT-style votes, charter, comparison summary for Run 1 | `results/second-ci-job/` |
| `agent/comparisons/code-of-conduct/` (5 files: same structure) | CJT-style votes, charter, comparison summary for Run 2 | `results/code-of-conduct/` |
| `agent/deliberations/condorcet-jury-theorem-process/` (6 files: 00-charter, 01-convening, 01-roster, 02-deliberation, 03-resolution, 04-evaluation-1) | Conceptual deliberation: "should we correct for CJT?" | `results/condorcet-jury-theorem-process/` |
| `agent/deliberations/second-ci-job/` (5 files: 00-charter, 01-convening, 01-roster, 02-deliberation, 03-resolution) | Deliberative pipeline transcript for Run 1 | `results/second-ci-job-deliberation/` |
| `agent/deliberations/code-of-conduct/` (5 files: same structure) | Deliberative pipeline transcript for Run 2 | `results/code-of-conduct-deliberation/` |
| `agent/comparisons/README.md` | Index of comparison runs | `results/comparisons-README.md` (kept as provenance; replaced at origin by redirect) |

**Stays in place (not experimental results):**

| Location | Why it stays |
|----------|-------------|
| `artifacts/condorcet-jury-theorem-and-committee.md` | Published artifact — conceptual document, not a result file |
| `artifacts/comparison-protocol-deliberative-vs-cjt.md` | Published artifact — reusable protocol, not tied to a single experiment |
| `agent/archive/handoff-2026-02-22-condorcet.md` | Session handoff — operational agent record |
| `agent/archive/condorcet-pr-review.md` | PR review — editorial record |
| `artifacts/adversarial-committees.md` (cross-ref line) | Existing cross-reference stays; will be updated to point at new location |

### Step-by-Step Plan

**Step 1: Create the directory structure**

```
meta/research-programs/condorcet-comparison/
meta/research-programs/condorcet-comparison/results/
meta/research-programs/condorcet-comparison/results/second-ci-job/
meta/research-programs/condorcet-comparison/results/second-ci-job-deliberation/
meta/research-programs/condorcet-comparison/results/code-of-conduct/
meta/research-programs/condorcet-comparison/results/code-of-conduct-deliberation/
meta/research-programs/condorcet-comparison/results/condorcet-jury-theorem-process/
```

**Step 2: Move experimental result files**

Move (not copy) the following directories' contents into the results tree:

- `agent/comparisons/second-ci-job/*` → `results/second-ci-job/`
- `agent/comparisons/code-of-conduct/*` → `results/code-of-conduct/`
- `agent/deliberations/condorcet-jury-theorem-process/*` → `results/condorcet-jury-theorem-process/`
- `agent/deliberations/second-ci-job/*` → `results/second-ci-job-deliberation/`
- `agent/deliberations/code-of-conduct/*` → `results/code-of-conduct-deliberation/`

Then remove the now-empty source directories from `agent/comparisons/` and `agent/deliberations/`.

**Step 3: Leave redirects at old locations**

(a) **Replace `agent/comparisons/README.md`** with a redirect stub:

```markdown
# Comparison Runs (moved)

The deliberative-vs-CJT comparison runs have been consolidated into the condorcet-comparison research program:

- **Program plan**: [meta/research-programs/condorcet-comparison.md](../../meta/research-programs/condorcet-comparison.md)
- **Results**: [meta/research-programs/condorcet-comparison/results/](../../meta/research-programs/condorcet-comparison/results/)

The comparison protocol remains at [artifacts/comparison-protocol-deliberative-vs-cjt.md](../../artifacts/comparison-protocol-deliberative-vs-cjt.md).
```

If no other comparison runs exist in `agent/comparisons/`, the directory can be left with just this redirect. (Currently no other runs exist.)

(b) No redirect needed for the moved deliberation subdirectories — `agent/deliberations/` contains many other deliberation records (ci-string-diagram-test, etc.) that are not part of this experiment and remain in place. Only the three condorcet-related subdirectories are moved.

**Step 4: Create `results/README.md`**

A results index that orients readers to the structure:

```markdown
# Condorcet Comparison — Results

Result files from each run of the deliberative-vs-CJT comparison.
See the plan and procedure in [../../condorcet-comparison.md](../../condorcet-comparison.md).

## Conceptual deliberation

- [condorcet-jury-theorem-process/](condorcet-jury-theorem-process/) — Committee deliberation on whether to "correct for" CJT. Unanimous: document, don't change process. Review 13/15.

## Run 1: second-ci-job (2026-02-22)

- [second-ci-job/](second-ci-job/) — Comparison records (charter, CJT-style votes, result, comparison summary)
- [second-ci-job-deliberation/](second-ci-job-deliberation/) — Full deliberative pipeline transcript

**Outcome**: Both pipelines Nay. CJT 4-1, Deliberative 5-0. One vote changed; deliberation added revisit condition.

## Run 2: code-of-conduct (2026-02-22)

- [code-of-conduct/](code-of-conduct/) — Comparison records
- [code-of-conduct-deliberation/](code-of-conduct-deliberation/) — Full deliberative pipeline transcript

**Outcome**: Opposite verdicts. CJT Aye 3-2, Deliberative Nay 5-0. Three votes flipped after enforcement/weaponization debate.
```

**Step 5: Create the plan file `meta/research-programs/condorcet-comparison.md`**

Populate from existing documentation. The content should include:

- **Objective**: Compare deliberative committee pipeline against CJT-style independent-vote-then-aggregate pipeline on the same questions, to test whether structured deliberation produces different (and better-mapped) outcomes than independent aggregation. References: `artifacts/condorcet-jury-theorem-and-committee.md` (conceptual foundation), `artifacts/comparison-protocol-deliberative-vs-cjt.md` (procedure).
- **Procedure**: Summarize the comparison protocol — same question, same roster, same charter; Pipeline A (deliberative via `/committee`), Pipeline B (CJT-style independent votes then majority); compare outcomes, vote shifts, rationale quality. Link to the full protocol artifact.
- **Status**: Completed (initial two-run study). Two runs executed 2026-02-22.
- **Runs**:
  - `2026-02-22 Run 1 (second-ci-job)` → `condorcet-comparison/results/second-ci-job/`
  - `2026-02-22 Run 2 (code-of-conduct)` → `condorcet-comparison/results/code-of-conduct/`
- **Key findings** (one-line per run):
  - second-ci-job: Same verdict (Nay); deliberation added nuance (one vote change, revisit condition).
  - code-of-conduct: Opposite verdicts (CJT Aye 3-2, Deliberative Nay 5-0); three votes flipped after enforcement debate.
- **Overall finding**: Initial evidence that deliberation can change outcomes, especially on value-laden questions with hidden second-order concerns. Two datapoints — further runs needed to establish a pattern.
- **Limitations**: Two runs only. Single-model independence caveat. No ground truth. Binary comparison (two pipelines) vs. the three-method comparison in evaluation-schemes.
- **Connection to other programs**: This is partial evidence toward the evaluation-schemes "highest priority" question. The comparison protocol is a lightweight precursor to the full blind panel evaluation (Design A). Link to `evaluation-schemes.md`.

**Step 6: Update `meta/research-programs/README.md`**

Three changes:

(a) **"Where to start" priority table**: Add a row or extend the "Highest" row. The condorcet comparison directly addresses the same uncertainty as evaluation-schemes ("Does committee-based deliberation beat simpler prompting?"). Either add `[condorcet-comparison.md](condorcet-comparison.md) — deliberative vs. CJT-style comparison (2 runs, completed)` to the existing Highest row's Plans column, or add a new row at High priority.

(b) **"Completed / reference programs" table**: Add an entry:

| Plan | Status | Location |
|------|--------|----------|
| Condorcet comparison (deliberative vs. CJT-style) | Completed (2 runs, 2026-02-22) | [condorcet-comparison.md](condorcet-comparison.md) |

(c) **"By theme" table**: Add condorcet-comparison to the "Validation / evidence" row.

**Step 7: Update `meta/research-programs/evaluation-schemes.md`**

Add a brief note in Section V (Experimental Designs) or Section VI (Composition and Sequencing) acknowledging that two deliberative-vs-CJT comparison runs have already been executed as a lightweight precursor, with a link to `condorcet-comparison.md`. This contextualizes the ablation/blind-panel designs as building on existing evidence rather than starting from zero.

**Step 8: Update `meta/README.md`**

Add condorcet-comparison to the bullet list of research programs:

```
- **[Condorcet comparison](research-programs/condorcet-comparison.md)** — Deliberative vs. CJT-style comparison; two runs completed, initial evidence that deliberation changes outcomes on value-laden questions.
```

**Step 9: Fix internal links that pointed at old locations**

Documents that reference the moved files and need path updates:

(a) `artifacts/comparison-protocol-deliberative-vs-cjt.md` — "Where to store comparison runs" section references `agent/comparisons/<topic-slug>/`. Update to point at `meta/research-programs/condorcet-comparison/results/` as the canonical location for these runs, noting the protocol remains reusable for future runs (which could go in either location depending on whether they're part of this program or a new one).

(b) `agent/archive/handoff-2026-02-22-condorcet.md` — References `agent/comparisons/` and `agent/deliberations/` for condorcet-related files in the "Completed This Session" table and elsewhere. Add a note at the top: "Note: The comparison and deliberation records listed below were later moved to `meta/research-programs/condorcet-comparison/results/`."

(c) `meta/methodology-evolution.md` (lines 306-309) — Update the paths in the condorcet milestone entries to point at the new locations under `meta/research-programs/condorcet-comparison/results/`, and add a note that the work is now documented as a research program.

(d) `artifacts/adversarial-committees.md` — Has a cross-reference to the Condorcet doc (which stays in `artifacts/`), so no change needed here.

(e) Check `agent/archive/condorcet-pr-review.md` — References `agent/comparisons/` and `agent/deliberations/`. Add a note at the top similar to (b): records have been moved to research-programs.

**Step 10: Verify no dangling references remain**

Grep the repo for `agent/comparisons/second-ci-job`, `agent/comparisons/code-of-conduct`, `agent/deliberations/condorcet-jury-theorem-process`, `agent/deliberations/second-ci-job`, and `agent/deliberations/code-of-conduct` to catch any references not covered in Step 9. Update or annotate as needed.

### What This Plan Does NOT Do

- **Does not move** `artifacts/condorcet-jury-theorem-and-committee.md` or `artifacts/comparison-protocol-deliberative-vs-cjt.md`. These are published artifacts (conceptual doc and reusable protocol). The research program *references* them.
- **Does not move** handoff or PR review records (`agent/archive/handoff-2026-02-22-condorcet.md`, `agent/archive/condorcet-pr-review.md`). These are agent operational records.
- **Does not move** non-condorcet deliberations that happen to share `agent/deliberations/` (e.g. `ci-string-diagram-test/`).
- **Does not change** the comparison protocol or the committee process.

---

## Summary

**Part 1**: The research-programs directory is structurally sound. All external references point to correct paths; no stale references to old locations. Three plan files (`evaluation-schemes.md`, `multi-model-committee.md`, `societies-of-thought-research-plan.md`) lack the formal Status/Runs/Results section that the conventions describe and that `ablation-study.md` exemplifies. These are minor formatting fixes.

**Part 2**: The condorcet experiment is well-documented across ~26 files in `agent/deliberations/`, `agent/comparisons/`, `artifacts/`, and `agent/archive/`. Its headline finding — deliberative and CJT-style pipelines produced opposite verdicts on a value-laden question — is the methodology's first empirical evidence for the value of structured deliberation. It is currently referenced in `methodology-evolution.md` but not in the research-programs index.

**Part 3**: Ten steps to create a self-contained condorcet-comparison research program: (1) create directory structure, (2) move experimental result files (3 deliberation directories + 2 comparison directories → results tree), (3) leave redirect at `agent/comparisons/`, (4) create results README, (5) create plan file, (6) update research-programs README index, (7) cross-reference from evaluation-schemes, (8) update meta/README, (9) fix internal links in handoff, PR review, methodology-evolution, and comparison protocol, (10) verify no dangling references. Published artifacts and agent handoff/review records stay in place.
