# Diary Entry: 2026-03-06 — Metacognition, Signal Detection, and the Trust Register

## Context

A collaborator has supplied working Python code for a calibration register and an optional feedback mechanism for applying register data to future deliberations. This entry records the theoretical grounding developed in preparation for a meeting with that contributor, focusing on why their contribution is significant and how it connects to the larger framework.

---

## Signal Detection Theory as the right formal language

The collaborator's framing — metacognition, calibration — points directly to signal detection theory (SDT), which provides the precise formal language the project needs. The treatment here follows the Van Trees lineage in detection and estimation theory, which is the right starting point for anyone with a communications background.

### The classical setup

In detection theory you have a signal-plus-noise problem. An observer receives a noisy observation and must decide: signal present or absent? The key separation is between two distinct quantities:

**d'** (d-prime): the discriminability index — the separation between the signal and noise distributions in ROC space, invariant to the observer's decision criterion. This is the SNR at the decision point in communications terms.

**Criterion (β or c)**: the observer's operating point on the ROC curve, determined by priors, costs, and everything outside the signal itself. Shifting criterion does not change d'.

SDT applies this structure to perception and cognition. The observer emits two outputs: a first-order decision (yes/no) and a confidence rating. The question the theory asks about confidence is whether the observer's internal confidence tracks the actual likelihood ratio — or whether there is slippage between the two.

### Meta-d' and metacognitive efficiency

The central construct is meta-d'. The computation proceeds as follows:

Given a corpus of trials, you have first-order decisions (correct/incorrect) and confidence ratings. You construct the type 2 ROC curve — the ROC built from treating the confidence rating as a second detection problem: given that the observer expressed high confidence, was it correct? This is a detection problem about the observer's self-knowledge rather than about the external signal.

Meta-d' is the d' value you would need to explain the observer's type 2 ROC behavior, assuming the observer were an ideal metacognitive agent — one who uses all available information when reporting confidence.

The ratio **meta-d'/d'** is metacognitive efficiency. Its interpretation:

- **= 1**: The observer uses all available signal when reporting confidence. Confidence is perfectly calibrated to actual discriminability. No information is lost between the primary detector and the metacognitive monitor.
- **< 1**: The observer's confidence reports are underinformed relative to actual performance. There is noise between the first-order decision process and the confidence reporting process — information is lost. The observer may be performing well but not "knowing" that it is performing well.
- **> 1**: Confidence is amplified beyond what discriminability warrants. Overconfidence. The observer claims more certainty than its accuracy justifies.

In communications terms: d' is the SNR at the primary decision point. Meta-d' is the SNR you would observe at a second decision point downstream that operates on the same underlying observation. Meta-d'/d' is the noise figure for self-knowledge — how much SNR is lost between the primary detector and the metacognitive monitor.

This framing is exact, not metaphorical. It gives you a dimensionless number per observer, per domain, computable from outcome data. Peters and Maniscalco (2024) provide the definitive treatment of optimal type 2 criteria under four objective functions: maximizing type 2 accuracy, maximizing type 2 reward, calibrating confidence to accuracy, and maximizing the type 2 hit rate / false alarm rate difference. The choice of objective has design implications for how calibration trials are scored.

---

## Application to the committee

Each committee character (Maya, Frankie, Joe, Vic, Tammy) makes first-order claims and expresses confidence during deliberation. Over a corpus of runs — especially the historical black swan cases where outcomes are known — you can score each character's positions against ground truth and accumulate type 2 data from confidence expressions.

The calibration register is the data structure that accumulates these trials. Meta-d'/d' per character is then computable from the register contents. It answers: is this character's expressed confidence *informative*, or is it rhetoric?

A character with meta-d'/d' near 1 is a calibrated signal source. Its confidence expressions can be trusted as indicators of actual reliability. A character with low metacognitive efficiency is confident in ways that do not predict accuracy. Possible causes: role-capture (the character performs its persona rather than reasons), systematic domain bias, or sycophancy pressure from the group. A character with meta-d'/d' greater than 1 is systematically overconfident — its confidence expressions should be discounted.

The optional feedback path in the register uses these efficiency estimates to condition future deliberations. Rather than treating all character contributions as equally weighted, the chair (or the orchestration layer) can apply calibration priors derived from the register. This is not a correction to the deliberation — it is information about the deliberation fed back into itself.

---

## The committee as epistemic sensor array

The SDT framing opens a second analytical dimension beyond individual character reliability: the inter-character correlation structure.

In a detection array — multiple receivers combining signals — the SNR improvement from combination depends on receiver correlation. Uncorrelated sensors add in quadrature; their contributions are genuinely independent and the array gain is real. Redundant sensors (high correlation) produce no improvement — the array is effectively a single sensor dressed as multiple sensors.

The committee is an epistemic sensor array. The design question the societies-of-thought research program has been approaching informally — does balance matter? do the personas produce genuine diversity? — becomes a formal empirical question: what is the inter-character confidence correlation matrix, and does it support real array gain?

The register, over enough runs, can estimate this matrix. Two characters that consistently agree — even when both are correct — may be highly correlated sensors providing less epistemic value than their apparent independence suggests. Two characters with low confidence correlation but similar accuracy rates are genuinely independent sensors and together provide more information than either alone.

No existing MAD framework performs this analysis. The literature measures group output accuracy without decomposing the array structure of individual contributors. This is a research contribution the project can pioneer.

---

## Stafford Beer and the viable system

The deepest framing for what the register achieves comes from Stafford Beer's viable system model.

Beer's core claim: a system is viable only if it has the internal variety to match the variety of its environment, and viability requires recursive self-modeling — the system must contain a model of itself adequate to regulate its own behavior.

Without the register, cyberneutics is an open-loop processor. Situation in, deliberated choice out. The committee does not know its own performance characteristics. This is a pipeline, not a viable system.

With the register and the feedback path, the architecture becomes recursive. The committee deliberates on its environment (the problem). The register models the committee's own performance over time. The feedback path uses that model to condition subsequent deliberations. The system now contains a model of itself adequate to regulate itself — which is Beer's definition of viability.

The specific Beer concept that applies is System 3* — the audit function in the viable system model. Beer designed 3* as a sporadic, direct channel from System 3 (operational management) that bypasses the normal reporting hierarchy to get ground truth about what's actually happening in the operational elements. The register does exactly this: it bypasses the committee's self-presentation and accumulates outcome data that the characters themselves cannot confabulate away. It is the audit channel that gives the system reliable information about its own behavior independent of that behavior's self-report.

The Cybersyn precedent is also relevant. Beer's attempt to build real-time regulatory infrastructure for the Chilean economy used the same principle: not optimizing the system directly, but providing the system with the information it needs to regulate itself. The register is not trying to make the committee smarter. It is giving the deliberative system the data it needs to know when to trust itself.

---

## The trust argument crystallized

The practical significance is this: the cyberneutics framework has always addressed one dimension of the trust risk — making reasoning visible. The committee produces an auditable chain of argument rather than a black-box output. A decision-maker can inspect the reasoning and make a judgment about its quality.

But visible reasoning is not sufficient for trust in adversarial or high-stakes contexts. A decision-maker who cannot distinguish a well-reasoned wrong answer from a well-reasoned right answer is still exposed to the trust risk. They need a track record — evidence that the framework's outputs correlate with good outcomes over time.

The register provides that track record, expressed in the formal language of metacognitive efficiency. A character's meta-d'/d' in a given domain is a number that means something precise: how much of its available signal is it using when it reports confidence? That number, communicated to a decision-maker, is analogous to a weather forecaster's Brier score. You do not trust the forecast because the forecaster sounds confident. You trust it because you have a characterized track record showing that when this forecaster says 70% probability, it rains 70% of the time.

The register enables cyberneutics to make that claim. Not on theoretical grounds, but on empirical grounds accumulated from real deliberations on real cases.

---

## Structural implications

**Metacognition as its own research program**: Given the scope — a working code artifact, formal theory in SDT, connection to the historical evaluation program, and implications for the societies-of-thought research — metacognition warrants its own research program rather than living as a component of the societies-of-thought plan. The societies-of-thought program addresses character design (personality, balance, reconciliation). The metacognition program addresses the empirical instrumentation layer that character design questions depend on.

**Historical evaluation as unified data-generating process**: The hindsight framework (running the committee on historical cases with known outcomes) and the calibration register are not separate programs. The historical evaluation *is* the calibration training corpus. Designing the historical evaluation without the register in mind from the start would be a structural error — confidence capture protocol, outcome scoring rubric, and register schema need to be aligned before the first run.

**Math development co-design**: The SDT calibration enriches the categorical structure. Meta-d'/d' lives naturally in an enriched category where the hom-sets carry confidence lattices — already in the palgebra reference list (Kelly 1982 on enriched category theory). The deliberation functor would need to preserve not just the decision structure but the calibration metadata. Palgebra development and metacognition design need to proceed together, not sequentially.

**Research programs directory**: Moving research-programs to top level from meta/ is a practical acknowledgment that the research program structure has become a primary navigation surface for the project, not a subdirectory of housekeeping documents.

---

## Open questions

1. Which SDT objective function does the register optimize? (Calibration accuracy? Hit rate / false alarm difference?) This has design implications for trial scoring.
2. How is confidence currently captured — verbalized numeric ratings, ordinal expressions, or inferred posture?
3. Does the feedback mechanism condition character prompts directly, or does it operate at the chair / orchestration layer?
4. What is the minimum run corpus needed for stable meta-d'/d' estimates? (This determines the breakeven point where the register becomes useful.)
5. How do calibration curves get communicated to decision-makers who are not familiar with ROC analysis?
