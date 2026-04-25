---
title: "The Fan Operation as a Stressor-List Generator for Residual Analysis"
audience: "Residuality theory practitioners; software architects who already use stressor analysis and want a more disciplined way to produce stressor lists"
type: working-note
length_words: ~2400
status: "Working note. The fan operation is implemented in the cyberneutics methodology elsewhere in this repository; this note describes its specific use as a tool for residual analysis without requiring adoption of the surrounding methodology."
---

# The Fan Operation as a Stressor-List Generator for Residual Analysis

This note is for someone already practicing residuality theory who wants a more disciplined way to produce the stressor list that residual analysis takes as input. It describes a tool — the **fan operation** — that another methodology has built and tested, and explains how it slots directly into the residuality workflow without requiring adoption of anything else.

The note is self-contained. It does not assume the reader has read the cyberneutics essays, the palgebra, or the survey paper. Pointers to the surrounding methodology are given for those who want them; nothing here depends on those pointers.

---

## The problem

Residual analysis, as described in O'Reilly's 2020 *Introduction to Residuality Theory* and the 2022 *Random Simulation and Attractor Networks* papers, takes a stressor list as input. The papers describe several techniques for producing the list — playfulness, removal of probability/impact filters, deliberate inclusion of impossible and irrelevant events — but the act of generating a good list is left largely to the architect's intuition.

This is the part of residual analysis that practitioners report as hardest. The 2022 paper acknowledges the failure mode directly: "Traditional methods in software architecture viewed as random simulations would seem to suffer from the curse of dimensionality — distributions tend to return to areas of high probability." A stressor list produced by a single architect, however well-intentioned, drifts toward what that architect can imagine — which is itself a probability-weighted distribution shaped by their experience. Residual analysis works in proportion to the breadth of the stressor list, and the breadth is hard to defend without a discipline for generating it.

Eric Normand's substack introduction to residuality theory illustrates the issue. The worked example (a country-based coupon banner service) generates a stressor list that is plausible and useful, but the list is identifiably the output of one practitioner working in good faith. Anyone running the same exercise on the same system would produce a substantially different list, and there is no way to compare the two for breadth or to verify that either is good enough.

The 2022 paper introduces *bagging and boosting* — randomly partitioning the stressor list into training and testing sets — as a defence against this. Bagging tests architectural robustness across stressor partitions, but it cannot improve the underlying breadth of the list. If the list is narrow, all bagged partitions are narrow.

What residuality theory needs is a discipline for stressor *generation* that operates upstream of bagging and produces a measurably broader list than a single architect's enumeration.

## The fan operation

The fan operation is a structured procedure for generating divergent narrative material from a single situation prompt. It was developed in a methodology called cyberneutics (a sense-making discipline using LLMs as narrative engines for decisions under uncertainty), and it is implemented in this repository as a slash command (`/scenarios`) backed by a roster of named characters and a procedure that can be run repeatedly with controlled variation.

The mechanics, stripped of cyberneutics-specific vocabulary:

1. **Define a roster of characters.** Each character has a propensity — a worldview lens through which they engage the situation. The propensities are chosen to be incommensurable: one character is preoccupied with regulatory exposure, another with infrastructural fragility, another with social and political dynamics, another with adversarial actors, and so on. The point is not that the characters are realistic; the point is that they are *deliberately partial*, each refusing to be reasonable about anything outside their lens.
2. **Present the situation.** The system under design is described once, briefly, with enough context for any character to engage but no anticipation of which stressors matter.
3. **Generate divergent material.** Each character produces material in their own register — usually scenarios or narratives, but the output type is configurable. The key constraint is that each character is required to engage from their lens regardless of whether their lens seems applicable. Impossible, irrelevant, and adversarial cases are *required* outputs, not allowed exceptions.
4. **Capture the union.** The output is the union of what every character produced. No filtering by probability, no relevance ranking, no consensus. The list grows.
5. **Optionally re-run.** The fan operation is stochastic; running it again with the same roster on the same situation produces a different but overlapping list. Multiple runs converge on a stable union.

In residual-analysis terms, what the fan operation produces *is* a stressor list. The narrative wrapping each item — the scenario, the character, the rationale — is incidental; the stressor itself (the event the system was not designed for) is what feeds into incidence-matrix construction.

## Why the fan defeats the curse-of-dimensionality bias

Three structural features matter.

**Roster-driven divergence breaks the single-perspective bias.** A single architect's stressor list reflects what that architect can imagine. A roster of incommensurable characters refuses single-perspective enumeration by construction. A character whose lens is *infrastructural fragility* will surface stressors that an architect focused on *regulatory exposure* would never produce, and vice versa. Multi-character generation is the architectural equivalent of bagging at the perspective level rather than at the partition level — it samples the stressor space along axes the architect's own intuition does not cover.

**Required engagement defeats the silent-pruning failure mode.** The most damaging form of curse-of-dimensionality bias in standard practice is not that the architect refuses to consider unlikely stressors — it is that the architect never thinks of them in the first place. The fan operation makes thinking of them mandatory: characters are required to produce material from their lens, including impossible-from-that-lens material, before they exit. The discipline is to *produce*, not to *select*. Selection is residuality's incidence-matrix step, downstream.

**LLM narrative generation is structurally well-suited to this.** O'Reilly's papers note that residual analysis benefits from the architect collecting *narratives* rather than abstract risks: stories about how the system might fail, told in concrete enough detail that the implications can be traced into the architecture. LLMs as narrative engines are unusually good at producing narrative-grade stressor descriptions on demand. They are mediocre at deciding which stressors matter — which is exactly why selection is downstream and why residual analysis's matrix techniques exist. The division of labour matches the technology's strengths and weaknesses.

## How to use it

A practical workflow, suitable for adoption inside an existing residual-analysis practice:

1. **Define the system under design.** A short description (~200–500 words). The same description will be presented to every character in the roster. Concision matters; the fan does not need to be primed with the architect's own threat model, because the threat model is what we want the fan to surface.

2. **Choose a roster.** Five to eight characters is typical. The cyberneutics methodology has its own roster ([`agent/scenario-roster.md`](../../agent/scenario-roster.md)) tuned for decision deliberation, but for residual analysis a more architecture-pitched roster is likely better. Candidate lenses for a software-architecture residual analysis:
   - The regulator who reads every change as an audit risk
   - The internal political actor who reads every change as a power shift
   - The adversary who reads every change as an attack surface
   - The infrastructure operator who reads every change as a runtime liability
   - The market participant who reads every change as a competitive signal
   - The end user whose workflow is invisible to the system designer
   - The future maintainer who has no context the original team did not write down
   - The journalist who will summarize a failure to a non-technical audience
   The choice of roster is itself an architectural decision; rosters with a single dominant lens (all-engineering, all-security) reproduce the single-perspective bias the fan is supposed to defeat. Diversity of lenses is the design parameter.

3. **Run the fan.** Each character generates material — typically 5–10 scenarios or stressors per character, depending on time budget. The output is the union, deduplicated lightly but not aggressively (near-duplicates from different characters often reveal that the underlying stressor is approachable from multiple lenses, which is itself information).

4. **Feed into existing residual analysis.** The deduplicated list is the input to the standard 2020-paper workflow: incidence-matrix construction, K-reduction, training/test partitioning, bagging-and-boosting. Nothing else changes.

5. **Optional: bag at the fan level.** Run the fan operation twice with different rosters or different temperatures; compare the two stressor lists. The intersection is what multiple fan-runs surface; the symmetric difference is what one roster sees that the other does not. This is bagging-and-boosting at the *generation* layer rather than at the *partition* layer, and it gives a measurable handle on whether the chosen roster is broad enough.

## Empirical claim

The fan-as-stressor-generator workflow makes a specific empirical claim that is testable using residual analysis's own machinery: **a stressor list produced by a multi-character fan operation will produce a residual architecture with a higher Ri than a stressor list produced by a single-architect enumeration on the same system.**

The protocol:

1. Have an architect produce a stressor list for system S in the standard way. Call this list A.
2. Run a fan operation on the same description of system S with a roster of n characters. Call the resulting list F.
3. Build two residual architectures, R_A from list A and R_F from list F, using identical incidence-matrix and K-reduction procedures.
4. Score both R_A and R_F against the same testing-set stressors (held out from both A and F). Compute Ri_A and Ri_F.
5. Report Ri_F − Ri_A.

A positive Ri_F − Ri_A is evidence that fan-generated stressor lists produce more resilient architectures. A consistently positive difference across multiple systems is evidence the fan is a reliable upstream tool for residual analysis. A null or negative result is evidence the fan does not contribute, and the architect's intuition is doing better than the LLM-driven roster.

This is exactly the empirical move residuality theory's own residual index makes possible. The fan operation does not require new measurement apparatus; it slots into Ri's existing falsifiability framework and inherits its empirical posture.

## What the fan does *not* do

The fan operation is a stressor *generator*. It does not:

- Decide which stressors matter (that is the incidence-matrix step, downstream).
- Build the residual architecture (that is the architect's job).
- Replace the architect's judgment about K-reduction or component-merging.
- Eliminate the need for bagging-and-boosting on the resulting list.
- Make the residual analysis less idiographic — Ri remains a per-project test.
- Validate that the chosen roster is the right one for this system (that is itself a design decision, and a poorly chosen roster will produce a narrow list).

It also does not commit the practitioner to anything else in the cyberneutics methodology. The fan is a single operation. Adopting the fan does not require adopting committee deliberation, the calibration register, the palgebra, or any of the philosophical commitments. It is a tool, not a methodology.

## Where to find the implementation

The fan operation is implemented as a slash command in this repository:

- The skill body: [`.claude/skills/scenarios/SKILL.md`](../../.claude/skills/scenarios/SKILL.md)
- The roster: [`agent/scenario-roster.md`](../../agent/scenario-roster.md) (cyberneutics-tuned; readers may want to substitute a software-architecture roster as described above)
- An example output structure: [`examples/scenarios/methodology-adoption-strategy/`](../../examples/scenarios/methodology-adoption-strategy/) (an example fan run on a different domain, kept as illustration of output shape)

Operating the fan does not require this specific implementation. Any LLM-orchestration setup that supports multi-character prompting with controlled propensity will work. The structural claims of this note depend on the *shape* of the operation (multi-character, divergent, required engagement, capture-the-union), not on the specific tooling.

## Why this works in 2026 and would not have worked in 2019

The 2019 *No More Snake Oil* paper notes that the architect's hardest job is producing a wide enough VUCA enumeration. The 2020 paper inherits this; the 2022 paper acknowledges it without solving it. The reason the gap was hard to fill in 2019–2022 is that there was no reliable way to outsource divergent narrative generation. A human team could be convened to brainstorm, but team brainstorms suffer from social-conformity pressures that narrow the output, and convening a team for every architecture is expensive enough that practitioners do not do it.

The 2022–2026 LLM generation has a property that human teams do not: it is willing to engage from a lens regardless of whether the lens seems reasonable, and it is fast enough that running a multi-character fan is cheap relative to the architecture work it informs. The technology O'Reilly's papers gesture at without naming — *something that produces breadth on demand* — is now available, and the cyberneutics methodology has done the engineering work of making it disciplined rather than chaotic.

The contribution back to residuality theory, then, is not theoretical. It is operational: here is a tool that does what your papers describe needing, with a clean integration path into your existing workflow, and an empirical handle (Ri-on-fan-generated-lists) that lets you decide whether the tool earns its keep on your projects.

---

## See also

- [`state-of-residuality-2026.md`](state-of-residuality-2026.md) — the survey paper
- [`cyberneutics-and-residuality.md`](cyberneutics-and-residuality.md) §2.9 — the contribution-back framing
- [`residuality-bibliography.md`](residuality-bibliography.md) — references for the residuality corpus
- [`README.md`](README.md) — directory navigation

For the surrounding cyberneutics methodology (not required to use the fan as a stressor generator):

- [Essay 10 — Decisions Under Uncertainty](../../essays/10-decisions-under-uncertainty.md) — the fan/funnel pipeline as cyberneutics practice
- [`palgebra/`](../../palgebra/) — the formal categorical treatment of fan and funnel as composable operations
