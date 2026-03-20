# Evaluating Deliberative Architectures

## What this research program tests

Does an adversarial AI committee produce better analysis than a single AI given the same amount of space to think?

The committee format (five characters with clashing propensities debating under Robert's Rules) is the core technique of the cyberneutics methodology. Its load-bearing claim is that it produces **inspectable reasoning records** — you can trace how a conclusion was reached, which assumptions were challenged, and where disagreements remain. A stronger but unproven claim is that committee debate surfaces **insights the single AI misses** — particularly conceptual reframing, where the committee questions the problem's frame rather than just analyzing within it.

This program tests the stronger claim empirically.

## What has been done

### Phase A: Targeted Reframing Probe (complete, 2026-03-20)

**Result: does not pass.**

Phase A tested whether committee deliberation (C2) surfaces conceptual reframing that an effort-matched single-agent analysis (B1-ext) misses. Eight runs total — four single-agent, four committee — on two scenarios, scored by two independent evaluators on two specific reframing insights.

The key findings:

- **The committee moved closer to one target insight but didn't get there.** On the phasing critique ("a phased server migration tests the deployment tool, not the configuration"), the committee scored "Partially present" where the single agent scored "Absent." Closer, but not enough to pass.
- **The other target insight appeared in both conditions.** The creation-vs-activity reframe ("the problem is bot activity, not bot creation") was surfaced by both the single agent and the committee, meaning it doesn't discriminate between them.
- **Two runs per condition is enough for variance checking, not for statistical power.** A subtler effect could exist but would need more runs or different scenarios to detect.

The null result is informative. It doesn't touch the inspectability claim (committee records *are* more traceable than single-agent outputs — that's structural, not empirical). It does mean the "better insights" story is undemonstrated on these scenarios.

For the general-audience narrative of how Phase A unfolded — including the preliminary tests, scenario hardening, committee reassessments, and the finding itself — see **[the-story-so-far.md](results/the-story-so-far.md)**.

### What Phase A also revealed (methodological findings)

The path to the null result was itself informative:

- **Effort-matched baselines change everything.** A short-prompt AI scored poorly on the test scenarios. A 3,000-word multi-angle analysis scored well on everything. The committee format also produces ~3,000-5,000 words. Comparing committee output to the short prompt would have inflated the committee's apparent advantage — the real comparison is with the effort-matched baseline, and that's a much harder bar.
- **Scenario hardening doesn't work against long prompts.** Making scenarios harder (removing explicit cues, disguising structures) reduced scores for the short prompt but not the long one. When you tell an AI to analyze from five angles in 3,000 words, it reasons through the disguise.
- **The committee used its own methodology on itself.** When Phase A's original design proved unworkable, an adversarial committee deliberated on what to do next. Twice. Those committee deliberations produced the pivot to the targeted reframing probe — which is itself a data point about the methodology's value for self-governance, even if the reframing probe returned a null.

## What's next (open avenues)

**Phase B: Anticipatory validity on historical cases.** The framework's core question — whether committee deliberation anticipates structural risks in historical business decisions — remains untested. Phase B requires constructing knowledge-bounded presentations of real cases where the outcome is known, then running blind comparisons. This is the evidential phase. Decision to proceed is pending.

**Alternative: focus on the inspectability claim.** If the "better insights" story can't be demonstrated, the research program could pivot to testing the inspectability claim directly — whether committee records are more useful for post-hoc audit, learning, and accountability than single-agent outputs. This is a different kind of evaluation (qualitative, human-judged) and may be harder to formalize.

**Alternative: increase statistical power on Phase A.** The reframing probe used the minimum sample (2 runs per condition). A larger study with more runs and more scenarios could detect a subtler reframing advantage if it exists. Whether that's worth the effort depends on how plausible the reframing hypothesis remains after the null.

## Reading guide

| If you want to... | Read this |
|---|---|
| Understand the finding quickly | [the-story-so-far.md](results/the-story-so-far.md) |
| See the formal protocol and experimental design | [evaluating-deliberative-architectures.md](../evaluating-deliberative-architectures.md) (the protocol document) |
| Inspect the raw evidence | [results/](results/) — scoring files, raw outputs, deliberation transcripts |
| Understand the committee characters | [agent/roster.md](../../agent/roster.md) and [character-propensity-reference.md](../../artifacts/character-propensity-reference.md) |
| See the committee deliberate on its own methodology | [results/deliberations/](results/deliberations/) — two full committee deliberations on Phase A's design |
| Understand what the methodology claims and where it fails | [when-methodology-fails.md](../../essays/when-methodology-fails.md) |

## File inventory

```
evaluating-deliberative-architectures/
├── README.md                              ← you are here
├── protocol-evaluation-2026-03-16.md      ← initial protocol evaluation
├── protocol-evaluation-rubric.md          ← evaluation rubric
├── protocol-re-evaluation-2026-03-16.md   ← re-evaluation after remediation
└── results/
    ├── the-story-so-far.md                ← general-audience narrative
    ├── phase-a-results.md                 ← Phase A combined results
    ├── phase-a-B1ext-scoring.md           ← B1-ext scoring details
    ├── phase-a-C2-scoring.md              ← C2 scoring details
    ├── pre-gate-1-contamination-probes.md
    ├── pre-gate-2-scenario-difficulty-pilot.md
    ├── re-pilot-revised-scenarios.md
    ├── replacement-scenario-construction.md
    ├── glenda-crock-hardened.md
    ├── cascading-mitigation-hardened.md
    ├── deliberations/                     ← committee deliberation records
    │   ├── black-swan-phase-a/            ← initial proceed-or-revise deliberation
    │   └── black-swan-phase-a-reassessment/ ← reassessment after trigger
    └── raw/                               ← complete model outputs (8 Phase A runs + pilots)
```
