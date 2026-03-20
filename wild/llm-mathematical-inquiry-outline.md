# LLM-Steered Mathematical Inquiry: Research Program Outline (ROUGH DRAFT)

**Status**: Rough outline for mg's review. Not a committed research program.
**Date**: 2026-03-20
**Origin**: Three insights recorded in `agent/onboarding-core.md` (section "Epistemic positions the agent must know") and `meta/project-state.md`.

---

## The question this program answers

How do we steer LLM pipelines to do reliable mathematics, and how do we know when they have?

This is distinct from:

- **Metacognition program** (not yet created, outlined in `wild/diary/2026-03-06-metacog-sdt-beer.md`): Focuses on SDT calibration of committee confidence — asks "is the committee's confidence informative?" The metacognition program measures the *noise figure* of the committee's self-knowledge. This program asks whether the committee can do *mathematics* at all, which is prior to asking whether it knows when it's doing mathematics well.
- **Ablation study** (`research-programs/ablation-study.md`): Asks "does the committee help?" — component contribution analysis. This program asks "can the committee do *mathematics*?" — a different task domain with different success criteria.
- **Formal development threads** (palgebra, furry logic, open games): Those are *doing* the math. This program sits at the meta-level — the epistemics of LLM-assisted formal reasoning. The formal threads are simultaneously subject matter and test case for this program.

## Scope

### Core questions

1. **Reliability**: Under what conditions do LLM pipelines produce mathematically correct results when harnessed through structured deliberation? Where do they systematically fail?
2. **Detectability**: How do we distinguish correct LLM-generated mathematics from plausible-but-wrong LLM-generated mathematics? What are the failure signatures?
3. **Calibration tracking**: What does the calibration register need to track to support trust judgments about formal outputs? (Connects to the metacognition program's infrastructure.)
4. **Human expert role**: What is the minimum viable human expert involvement needed to certify LLM-generated mathematics? What can the pipeline do without expert review, and where is expert review load-bearing?

### What it does NOT cover

- Whether the committee outperforms solo prompting in general (ablation study's question)
- SDT calibration mechanics (metacognition program's question)
- The actual category theory itself (palgebra/furry logic development threads)

## Method candidates

### 1. Expert review of existing formal work (ACT outreach)
Submit palgebra, furry logic, and open games constructions to ACT practitioners (Cybercat community) for review. This is already motivated by the ACT outreach. The research value: expert verdicts become ground truth labels for calibrating trust in LLM-generated mathematics.

**Dependencies**: ACT outreach succeeding; willing reviewers.

### 2. Known-result benchmarking
Run the committee on mathematical problems with known solutions. Compare LLM-generated proofs/constructions against textbook results. Score on: structural correctness, proof validity, appropriate use of definitions, absence of hallucinated lemmas.

**Candidates for test problems**:
- Simple category theory (products, coproducts in **Set** — results are textbook)
- Monad laws for specific monads (mechanically checkable)
- String diagram translations (the `/string-diagram` tool already does this — check its outputs against manual derivation)

**Dependencies**: Problem set design; scoring rubric.

### 3. Structural fidelity comparison
Compare LLM-generated proofs against textbook proofs not just for correctness but for *structural fidelity*: Does the LLM proof use the same key moves? Does it introduce unnecessary machinery? Does it hallucinate structure that isn't there?

**Dependencies**: Requires someone who can read both the LLM output and the textbook and judge structural alignment.

### 4. Adversarial probing
Use the committee itself to probe its own formal outputs. Does a skeptical committee member (Vic) find genuine holes in palgebra constructions that a solo LLM misses? This tests whether adversarial deliberation improves mathematical reliability specifically.

**Dependencies**: Well-designed prompts; this is partly what the existing categorical-structures review (2026-03-13) already did informally.

## Dependencies

- **Calibration register**: For tracking which mathematical claims survived review and which didn't. This is shared infrastructure with the metacognition program (being developed by a contributor; not yet committed to `research-programs/`).
- **Human expert engagement**: Methods 1 and 3 require human experts. The ACT outreach is the primary path to obtaining this.
- **Existing formal work as corpus**: The palgebra, furry logic, and open games documents are the initial test corpus. The program needs them to exist (they do) but should not modify them.

## Relationship to existing programs

```
                    ┌─────────────────────┐
                    │  LLM-Math-Inquiry   │  ← this program (epistemics of LLM math)
                    │  "Can it do math?"  │
                    └────────┬────────────┘
                             │ uses infrastructure from
                             ▼
                    ┌─────────────────────┐
                    │  Metacognition      │  ← SDT calibration, register design
                    │  "Is it calibrated?"│
                    └────────┬────────────┘
                             │ provides ground truth to
                             ▼
              ┌──────────────┴──────────────┐
              │                             │
    ┌─────────┴─────────┐     ┌─────────────┴────────────┐
    │  Palgebra / Furry  │     │  Open Games / Committee   │
    │  Logic development │     │  Games formalization      │
    │  (doing the math)  │     │  (doing the math)         │
    └────────────────────┘     └──────────────────────────┘
```

- **Upstream of** palgebra and furry logic: provides the epistemic framework they need (are these results trustworthy?)
- **Downstream of** metacognition: uses the calibration infrastructure (register, scoring)
- **Adjacent to** ablation study: different question ("can the committee do mathematics?" vs. "does the committee help?")
- **Dependent on** ACT outreach: expert review is the primary source of ground truth

## Pitch to ACT community

"Here's a compositional framework for harnessing LLMs as mathematical exploration tools, and here's how we propose to calibrate trust in their outputs."

This is more honest and more interesting than "we used LLMs to do category theory." It acknowledges the epistemic status of the work (provisional, untrusted) while framing the interesting research question (how to make it trustworthy). The ACT community gets genuine research problems — characterizing when compositional reasoning pipelines produce valid mathematics — rather than a fait accompli claiming LLMs have done category theory.

## Open questions for mg

1. Does this warrant its own file in `research-programs/`, or should it remain a framing lens applied across existing programs?
2. Should the known-result benchmarking (Method 2) be designed now, or does it wait for the metacognition register infrastructure?
3. Is the ACT expert review (Method 1) already in flight via the open games / Cybercat outreach, or does it need separate coordination?
4. Should the categorical-structures review (2026-03-13) be retroactively scored as a Method 4 pilot run?
