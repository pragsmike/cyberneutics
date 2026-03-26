# Handoff: Black Swan Phase A Targeted Revision

**Date**: 2026-03-20
**Session**: Executed Steps 1–5 of the Phase A revision plan from the 2026-03-16 committee resolution.

---

## What was done

Executed the full targeted revision plan for the Black Swan Hindsight Framework Phase A:

1. **Replacement externally-sourced scenario**: Attempted two case constructions (cap per resolution).
   - Attempt 1 (Ajka alumina plant, Hungary 2010): Contamination probe FAILED — Sonnet recognized it immediately.
   - Attempt 2 (Longford gas explosion, Australia 1998): Contamination probe CONDITIONAL PASS — Sonnet misidentified it as Texas City (wrong case, same pattern class). Proceeded.
   - B1 = 2, B1-ext = 2 on the replacement scenario. B1-ext ≤ 1? No.

2. **Surgical hardening of Glenda/Crock**: Replaced explicit threats with "content interoperability framework" framing. Coercion disguised as industry standardization.
   - B1 dropped 2.0 → 1.0 (hardening effective on short prompt).
   - B1-ext stayed at 3.0 (hardening ineffective on effort-matched condition).

3. **Surgical hardening of Cascading Mitigation**: Removed explicit mitigation list (CAPTCHA, rate limiting, email verification). Replaced with "adding friction to account creation."
   - B1 dropped 2.0 → 1.5 (moderate improvement).
   - B1-ext increased 2.0 → 2.5 (counterproductive — the harder prompt gave the model more reason to dig).

4. **Reassessment**: Zero scenarios meet B1-ext ≤ 1. **Reassessment trigger activated.**

---

## The finding

**The difficulty problem is about the B1-ext prompt, not the scenarios.** When instructed to write 3,000 words analyzing from multiple angles, the model has enough analytical depth to identify structural features regardless of surface presentation. Hardening the scenarios reduces B1 scores effectively but does not reduce B1-ext scores.

This is a structural limitation of the experimental design, not a scenario construction failure. The B1-ext multi-angle prompt essentially instructs the model to perform structural analysis — which is exactly what the scoring system measures.

---

## What was NOT done

- ~~Committee reconvened~~ — **Done** (see below)
- Full Phase A execution (blocked by reassessment trigger → now pivoted to targeted reframing probe)
- Any changes to the protocol document itself (amendment is the next step)

---

## Files created this session

| File | Purpose |
|------|---------|
| `agent/prompts/black-swan-phase-a-revision.md` | Durable execution plan for the revision (Steps 1-5) |
| `results/replacement-scenario-construction.md` | Both attempts, contamination probes, B1/B1-ext scores |
| `results/glenda-crock-hardened.md` | Hardened scenario text + change log |
| `results/cascading-mitigation-hardened.md` | Hardened scenario text + change log |
| `results/re-pilot-revised-scenarios.md` | All 6 scores, comparison with original, reassessment decision |
| `results/the-story-so-far.md` | Updated with revision results and finding |
| `results/raw/replacement-B1.md` | Raw B1 output for replacement scenario |
| `results/raw/replacement-B1-ext.md` | Raw B1-ext output for replacement scenario |
| `results/raw/glenda-crock-hardened-B1.md` | Raw B1 output (summary) for hardened Glenda/Crock |
| `results/raw/glenda-crock-hardened-B1-ext.md` | Raw B1-ext output (summary) for hardened Glenda/Crock |
| `results/raw/cascading-mitigation-hardened-B1.md` | Raw B1 output (summary) for hardened Cascading Mitigation |
| `results/raw/cascading-mitigation-hardened-B1-ext.md` | Raw B1-ext output (summary) for hardened Cascading Mitigation |
| `agent/handoff-2026-03-20-black-swan-revision.md` | This file |

All results files are under `research-programs/evaluating-deliberative-architectures/results/`.

---

## Next steps (updated after reassessment) — ALL COMPLETE

Per the resolution's implementation plan (user ratified):

1. ✅ **Amend the protocol document** — Section X-A added with full specification.
2. ✅ **Run B1-ext × 2 replication** — 4 runs completed. Feature 2 eliminated as discrimination target (B1-ext Run 3 scored "Present").
3. ✅ **Run C2 × 2** — 4 committee deliberations completed (full 5-member adversarial pipeline).
4. ✅ **Assess against pass criterion** — **DOES NOT PASS.** C2's best score on Feature 1 is "Partially present" (not "Present").
5. ✅ **Write report** — `results/phase-a-results.md` documents full trajectory and findings.

### Additional files created during Phase A execution

| File | Purpose |
|------|---------|
| `results/raw/phase-a-blast-radius-B1ext-run1.md` | Complete B1-ext output, Blast Radius Run 1 |
| `results/raw/phase-a-blast-radius-B1ext-run2.md` | Complete B1-ext output, Blast Radius Run 2 |
| `results/raw/phase-a-cascading-mitigation-B1ext-run3.md` | Complete B1-ext output, Cascading Mitigation Run 3 |
| `results/raw/phase-a-cascading-mitigation-B1ext-run4.md` | Complete B1-ext output, Cascading Mitigation Run 4 |
| `results/raw/phase-a-blast-radius-C2-run5.md` | Complete C2 deliberation, Blast Radius Run 5 |
| `results/raw/phase-a-blast-radius-C2-run6.md` | Complete C2 deliberation, Blast Radius Run 6 |
| `results/raw/phase-a-cascading-mitigation-C2-run7.md` | Complete C2 deliberation, Cascading Mitigation Run 7 |
| `results/raw/phase-a-cascading-mitigation-C2-run8.md` | Complete C2 deliberation, Cascading Mitigation Run 8 |
| `results/phase-a-B1ext-scoring.md` | B1-ext scoring results with evaluator analysis |
| `results/phase-a-C2-scoring.md` | C2 scoring results with evaluator analysis |
| `results/phase-a-results.md` | Phase A combined results report |

---

## Tensions and surprises

1. **The hardening paradox**: Making scenarios harder for B1 can make them easier for B1-ext, because removing explicit details forces the B1-ext model to generate its own analysis — which it does well, and which the scoring system rewards. The hardening of Cascading Mitigation is the clearest example: removing the mitigation list gave B1-ext more room to demonstrate structural reasoning.

2. **Contamination is pattern-class, not event-specific**: The replacement scenario's contamination probe showed that the model doesn't need to identify the *specific* real-world case to have its analysis contaminated. Recognizing the *pattern class* (organizational cost-cutting → industrial disaster) provides an analytical framework that inflates scores even without recall of specific outcomes.

3. **The B1-ext prompt instructs the scoring target**: The multi-angle B1-ext prompt ("consider political dynamics, systemic effects, historical precedents, gaps in evidence, values at stake") is almost a description of the structural recognition scale. This is a meta-problem: the effort-matched control is effort-matched for tokens and depth, but it's also *instruction-matched* for the scoring criteria. The committee format doesn't explicitly instruct "analyze from five angles" — it creates conditions where such analysis might emerge naturally. That's the real test.

4. **Scoring reliability remains excellent**: All six re-pilot scores were within 1 point between evaluators, and 4 of 6 were exact agreement. The unified scale continues to work as a measurement instrument, even if the scenarios are too easy for B1-ext.

---

## Reassessment deliberation (later in same session)

After the reassessment trigger fired, the committee was reconvened. Full deliberation record: `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/` (00-charter through 04-evaluation).

**Decision**: Pivot Phase A from "Protocol Calibration" to **Targeted Reframing Probe** (Option C, unanimous).

**Key insight** (Vic): B1-ext captures *deepening* (more thorough analysis within the existing problem frame) because the multi-angle prompt instructs it. But *reframing* (generating an alternative problem frame) requires a conceptual shift the prompt doesn't directly instruct. Committee deliberation, with adversarial characters challenging each other's framings, may uniquely surface reframing.

**Run plan**: 8 runs total — B1-ext × 2 + C2 × 2 on Blast Radius (original) and Cascading Mitigation (hardened). All dual-scored on two binary features using three-level scale (absent/partial/present).

**Pass criterion**: C2 produces "present" on ≥1 target feature where both B1-ext runs produce "absent."

**Target features**: (1) phasing critique — Blast Radius criterion (c), (2) creation-vs-activity reframing — Cascading Mitigation criterion (c).

**Evaluation**: 13.5/15 (HIGH, no remediation needed). Improvement over prior deliberation (10/15 → 13/15 after remediation).

**Status**: Resolution pending user ratification. Next step: amend protocol document.

### Files created during reassessment

| File | Purpose |
|------|---------|
| `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/00-charter.md` | Charter with context, success criteria, exit conditions |
| `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/01-roster.md` | Standard 5-member committee roster |
| `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/02-deliberation.md` | Full deliberation transcript (opening statements + Round 2) |
| `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/03-resolution.md` | Formal resolution with YAML frontmatter, run plan, pass criterion |
| `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/04-evaluation.md` | Independent evaluation (13.5/15) |

---

## Mistakes and corrections

- **Full raw outputs not saved for hardened scenarios**: The raw output summaries for the four hardened-scenario runs capture key analytical points but not the complete model output. Future runs should save complete outputs. The replacement scenario raw outputs are complete.

- **Temperature control deviation**: All runs used default temperature (temperature=0 not available via the agent interface). This is consistent with Pre-Gate 2 and is documented as a standing control deviation.
