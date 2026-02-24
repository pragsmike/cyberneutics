# Research Programs

This directory collects research plans, experiment designs, evidence-building programs, and their **results and findings** for the Cyberneutics methodology. The goal is to give contributors one place to find work that reduces uncertainty about whether and when the methodology works, and how to improve it.

**If you want to contribute:** pick a plan that matches your skills and interests. The sections below order programs by how much they reduce key uncertainties, and list active vs completed work.

---

## Conventions

**Where results go:** Each study with its own plan file has a **results** location next to it. For example, the ablation study has [ablation-study.md](ablation-study.md) (plan) and [ablation-study/results/](ablation-study/results/) (run outputs: tables, summaries, raw data). The umbrella doc (e.g. evaluation-schemes) does not hold results; each extracted design has its own plan and results folder.

**Recording completed studies:** In the **plan file**, add a **Status** section: *Not started | In progress | Completed*; list **Runs** with date and link to results (e.g. `2026-03-15 Run 1 — results/2026-03-run1.md`); optionally one-line finding. In the umbrella doc, add a column or sentence linking to the study’s results when available.

**Archiving:** Plans are **not** archived when a study completes; the plan stays in place and is updated with status and links to results. **Archive only** when a plan is superseded or retired (e.g. move to `research-programs/archive/` and link from the new plan or this README). Completed runs live in the study’s results folder.

---

## Where to start (by impact on uncertainty)

These programs are ordered by how much they reduce the main open uncertainties: *Does the methodology outperform simpler approaches? When does it help? How do we know?*

| Priority | Uncertainty reduced | Plan(s) |
|----------|---------------------|---------|
| **Highest** | Does committee-based deliberation beat simpler prompting? When is it worth the cost? | [evaluation-schemes.md](evaluation-schemes.md) — research design for empirical comparison; [ablation-study.md](ablation-study.md) — component contribution (Phase 1); [societies-of-thought-research-plan.md](societies-of-thought-research-plan.md) Item 10 (comparative effectiveness study) |
| **High** | Would different LLMs per character improve deliberation? | [multi-model-committee.md](multi-model-committee.md) — hypothesis, five architectures, experimental protocol |
| **High** | Does the methodology transfer across domains? When does roster composition matter? | [societies-of-thought-research-plan.md](societies-of-thought-research-plan.md) Items 4, 5, 9 (transfer learning, domain variants, worked examples) |
| **Medium** | Why does it work? Can we formalize and cite it? | [societies-of-thought-research-plan.md](societies-of-thought-research-plan.md) Items 1–3, 6–7 (personality/balance/reconciliation, information-theory essay, social scaling theory) |
| **Medium** | How do we implement it in a formal platform? | [societies-of-thought-research-plan.md](societies-of-thought-research-plan.md) Item 8 (MOOLLM integration) |
| **Reference** | What docs and TODOs are still open? | [agent/gap_analysis.md](../../agent/gap_analysis.md) — planned essays, artifacts, and follow-ups (not a single experiment; kept in agent/ for session continuity) |

---

## Active research programs

| Plan | Summary |
|------|---------|
| [societies-of-thought-research-plan.md](societies-of-thought-research-plan.md) | Ten action items from the Societies of Thought paper: strengthen infrastructure (Big Five, balance metrics, reconciliation), test generalization (transfer, domain variants), formalize theory (information-theory essay, social scaling), expand evidence (worked examples, comparative study), MOOLLM integration. Phased roadmap. |
| [evaluation-schemes.md](evaluation-schemes.md) | Research design for evaluating the methodology: core questions, why direct evaluation is hard, proposed dimensions (assumption coverage, trade-off explicitness, etc.), protocols. No ground truth required. |
| [ablation-study.md](ablation-study.md) | Component contribution and interaction effects (Design F). Full procedure, factor definitions, run budget, results tabulation. Results: [ablation-study/results/](ablation-study/results/). |
| [multi-model-committee.md](multi-model-committee.md) | Using different LLMs for different committee characters: hypothesis, five architectural patterns, trade-offs, experimental protocol. |

---

## Completed / reference programs

These plans have been executed or implemented. They live in [agent/archive/](../../agent/archive/) and are linked here for pattern and history.

| Plan | Status | Location |
|------|--------|----------|
| Wild material incorporation | Executed and verified | [agent/archive/wild-material-incorporation-plan.md](../../agent/archive/wild-material-incorporation-plan.md) |
| Cross-reference and synthesis | Executed (11/11 items) | [agent/archive/cross-reference-synthesis-plan.md](../../agent/archive/cross-reference-synthesis-plan.md) |
| Augmentation (deliberation structure, evaluation loop) | Implemented | [agent/archive/augmentation-plan.md](../../agent/archive/augmentation-plan.md) |
| Evaluation feedback loop | Merged into augmentation plan | [agent/archive/evaluation-feedback-loop-plan.md](../../agent/archive/evaluation-feedback-loop-plan.md) |

---

## By theme

| Theme | Plans | Status |
|-------|-------|--------|
| **Validation / evidence** | evaluation-schemes, ablation-study, societies-of-thought Items 9–10 | Active |
| **Theory / foundations** | societies-of-thought Items 6–7 | Active |
| **Infrastructure / process** | societies-of-thought Items 1–3, 8; augmentation | Active / Implemented |
| **Integration** | wild-material-incorporation, multi-model-committee | Executed / Active |

---

## Related

- [meta/README.md](../README.md) — overview of the meta directory and link to this collection
- [essays/societies-of-thought-synthesis.md](../../essays/societies-of-thought-synthesis.md) — source analysis for the Societies of Thought research plan
- [agent/gap_analysis.md](../../agent/gap_analysis.md) — planned documents and TODOs (referenced by CLAUDE.md and when-methodology-fails)
