# Meta: Reflective Documentation

This directory contains documentation *about* the methodology's
evolution, adoption, and self-assessment — distinct from the
methodology itself (essays/, artifacts/) and from operational
session state (agent/).

| Audience | Directory |
|---|---|
| **Community, future committees, contributors** | `meta/` (this directory) |
| **Successor agents, session continuity** | `agent/` (handoffs, diaries, deliberation records) |
| **Practitioners learning the methodology** | `artifacts/` (techniques, templates, guides) |
| **Theorists understanding the foundations** | `essays/` (theoretical framework) |
| **Formalists specifying pipelines** | `palgebra/` (the algebra) |

## Contents

### [research-programs/](research-programs/README.md) ← **Start here if you want to contribute**

Research plans, experiment designs, evidence-building programs, and their results and findings are collected in **meta/research-programs/** with an index ordered by impact on uncertainty:

- **[Societies of Thought research plan](research-programs/societies-of-thought-research-plan.md)** — Ten action items derived from the [Societies of Thought analysis](../essays/societies-of-thought-synthesis.md): infrastructure (personality, balance, reconciliation), generalization (transfer, domain variants), theory (information-theory essay, social scaling), evidence (worked examples, comparative study), MOOLLM integration.
- **[Evaluation schemes](research-programs/evaluation-schemes.md)** — Research design for testing whether the methodology outperforms simpler approaches.
- **[Ablation study](research-programs/ablation-study.md)** — Component contribution and interaction effects (Phase 1 of evaluation).
- **[Multi-model committee](research-programs/multi-model-committee.md)** — Using different LLMs per character; architectures and experimental protocol.

The [research-programs README](research-programs/README.md) lists active and completed programs by theme. Pick an item that matches your skills or interests.

### [methodology-evolution.md](methodology-evolution.md)

How the methodology developed: mistakes made, dead ends explored,
patterns that emerged, and a chronological development trajectory
from January 29, 2026 through the present. Includes maturity
assessment and open questions.

### [uptake-and-usage.md](uptake-and-usage.md)

External adoption signals: forks, platform integrations, practitioner
feedback, and what they tell us about whether the methodology works
outside its birthplace. Tracks against the predictions made by the
Feb 1, 2026 self-evaluation.

### [is-author-crackpot.md](is-author-crackpot.md)

Two adversarial committee runs (Feb 17 and Feb 21, 2026) assessing
whether the repository's interdisciplinary synthesis is genuine or
crackpottery. Verdict: not a crackpot, but the live question is
whether the methodology outperforms simpler approaches. Includes
the probability distribution, debate history, and calibration anchors
for what evidence would change the numbers.

### [repository-review-and-run-guide.md](repository-review-and-run-guide.md)

In-depth review of the repo and a concrete run/test guide: what is
runnable (skills in an AI session, the string-diagram Python script),
how to run the methodology and the script, current testing state, and
recommended lightweight automation (including `scripts/test_string_diagram.py`).

## Why This Directory Exists

The methodology claims to be self-improving: applying Cyberneutics to
itself should produce measurable improvements. This directory is where
that claim gets tested.

- **research-programs/** is the active work queue — what needs doing and how (index + plans and results)
- **methodology-evolution.md** shows whether the methodology actually
  evolved through practice (not just accumulated documentation)
- **uptake-and-usage.md** shows whether anyone outside the project
  finds it useful (the external validation gap)

Future `/committee` deliberations about project direction should read
this directory first to understand the project's current state and
what external signals say about where to invest effort.
