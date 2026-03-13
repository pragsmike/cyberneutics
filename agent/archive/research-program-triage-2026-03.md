# Research Program Triage: March 2026

**Date**: 2026-03-13
**Workstream**: Workstream 3 of refactoring sprint (audit phase)
**Scope**: Assessment of research program relevance, feasibility, blockers, and recommended action
**Assessor**: Claude (Haiku 4.5)
**Status**: Audit only — no repository modifications

---

## Overview

This triage evaluates eight active research programs and identifies implicit new programs suggested by recent wild material (Feb 2026 – Mar 2026). The assessment covers:
- Relevance to core uncertainties
- Prerequisites and blockers
- Changes since design that may invalidate or supersede assumptions
- Recommended action (run / update / archive / merge)
- Connections to contributor issues #6, #7, #11

---

## Executive Summary

**Core Finding**: The research portfolio is well-aligned, internally consistent, and strategically sound. Programs cover the three highest-priority uncertainties (does methodology outperform simpler approaches; does implementation architecture matter; does methodology transfer across domains) with complementary experimental designs.

**Key Recommendations**:
1. **Proceed with ablation study and agent-independence as planned** — these are the methodologically cleanest tests of core claims
2. **Promote potential-to-sense essay to essays/** — it is polished and provides essential theoretical grounding for human-gate requirements
3. **Add OpenCode to implementation taxonomy as Tier 2 candidate** — contributor issue #6 describes capabilities that could close the current Tier 2 gap
4. **Integrate legal domain test case into evaluating-deliberative-architectures** — issue #7 identifies a concrete pilot application
5. **Extend agent-independence to include multimodal inputs** — issue #11 suggests a natural follow-up direction
6. **Create three new research programs** from wild material:
   - Furry logic and soft-type classification (theoretical)
   - Open games formalization of committee structure (theoretical/validation)
   - Potential-to-sense as grounding framework for human gates (foundational)

**Timeline**: Ablation study and agent-independence are ready to start immediately. Multi-model-committee Phases 1–2 are feasible within 6 weeks. Societies of thought action items are modular and can proceed in parallel.

---

## Individual Program Assessments

### 1. Ablation Study: Component Contribution and Interaction Effects

**Status**: Not started
**Design**: Factorial or one-at-a-time removal of committee components
**Relevance**: HIGH — directly addresses "which components matter" question (highest priority per README)

#### Assessment

**(a) Is the question still interesting and relevant?**
Yes. The methodology has five major components (scenarios, committee, deliberated choice, evaluation loop, Robert's Rules structure). Understanding their individual and joint contributions is essential for:
- Prioritizing implementation effort
- Deciding which variants to support
- Identifying which components degrade gracefully vs. catastrophically

**(b) Are prerequisites met?**
All prerequisites are met:
- Evaluation dimensions (A–F) are formalized in `evaluation-schemes.md` with codebooks
- Comparison protocol exists (`condorcet-comparison.md` demonstrates the procedure)
- Rubric system is standardized across all programs
- Entry point and factor definitions are explicit

**(c) Has anything invalidated or superseded the design?**
No. The design remains the most cost-effective way to estimate component contributions. Two concerns from condorcet-comparison apply:
- "True independence is hard to guarantee in single-model session" — this is inherent to the methodology, not a design flaw; ablation should control for it
- Condorcet found that deliberation can change outcomes (code-of-conduct case) — this makes the ablation more valuable, not less (shows deliberation's value is real, not simulated)

**(d) Recommended action**: **RUN (immediately)**

This is a Phase 1 program with clear entry point, known procedure, and standalone results value. It should begin as soon as a contributor with experimental design skills is available (estimated 1 month timeline). No design changes needed.

**(e) Connection to wild material**: None direct. Complements the furry logic and open games work indirectly (both are theoretical explorations of what the ablation measures).

---

### 2. Agent Independence: Does Architectural Separation Improve Deliberation?

**Status**: Active (not started)
**Design**: Paired comparison (roleplay vs. independent agents) on 1–5 topics
**Relevance**: HIGH — tests the architectural-independence axis of the implementation taxonomy

#### Assessment

**(a) Is the question still interesting and relevant?**
Yes, and increasingly urgent. As of March 2026:
- Claude Code Agent Teams (launched Feb 5) provides a native platform for independent agents with peer-to-peer communication via SendMessage
- The Condorcet study noted that "true independence is hard to guarantee in single-context roleplay"
- This program directly addresses that limitation

**(b) Are prerequisites met?**
Yes, with one important caveat:
- Claude Code with Agent Teams feature: **confirmed available** (Opus 4.6, Feb 5 2026 launch)
- Roster and propensities: **in place** (`agent/roster.md`)
- Evaluation rubrics: **formalized** (condorcet-comparison and evaluation-schemes)
- Feasibility landscape: **surveyed** (`references/coding-agent-subagent-capabilities-2026-03.md` confirms 5-agent committees feasible, ~$30–50 cost, 10–20 min wall-clock)

The caveat: Agent Teams is experimental. Early-adopter reports show intermittent behavioral issues and feature surface changes; this is a **medium risk** but not a blocker (Phase 1 is one afternoon; if the feature breaks, the finding is valuable anyway).

**(c) Has anything invalidated or superseded the design?**
The design is more relevant now than when written (Feb 2026). The Cowork attempt (Feb 24) taught that hub-and-spoke communication fails for genuine peer deliberation; Agent Teams directly addresses this. The landscape survey (Mar 2026) provides detailed cost/capability data that updates but does not contradict the original design.

**(d) Recommended action**: **RUN (Phase 1 immediately, Phase 2 conditional)**

Phase 1 (paired comparison on 1 topic, 1 afternoon) should start immediately. It is a pure feasibility test with low resource cost. Phase 2 (5 topics, scored, 1–2 weeks) is conditional on Phase 1 producing observable differences.

**(e) Connection to wild material**:
- **Issue #6** (OpenCode capabilities): Mentions OpenCode has subagent control with cross-provider model selection and (tentatively) peer-to-peer communication. If OpenCode's design proposal ships, it would provide a Tier 2 implementation directly — making agent-independence + model-diversity testable on a single platform. This is a future enhancement, not a blocker.
- **Issue #11** (multimodal/discrete subagent deliberation): Suggests extending agent deliberation to handle images, diagrams, etc. This is a natural follow-up to Phase 2 but not a prerequisite.

---

### 3. Committee Implementation Taxonomy

**Status**: Active (reference document)
**Design**: Three-tier framework: Tier 1 (independent agents, single model), Tier 1+ (independent agents, intra-family models), Tier 2 (independent agents, cross-provider models), Tier 2.5 (Agent Teams + LiteLLM MCP tools), Tier 3 (external orchestration via LiteLLM)
**Relevance**: HIGH — organizes the design space for all implementation-focused research

#### Assessment

**(a) Is the framework still interesting and relevant?**
Yes. The two-axis framework (agent independence × model diversity) is conceptually clean and empirically testable. Programs map cleanly onto cells of the taxonomy.

**(b) Are prerequisites met?**
Largely yes. Landscape survey (`references/coding-agent-subagent-capabilities-2026-03.md`) is current as of March 2026. One gap:
- **Tier 2 (cross-provider agents with peer-to-peer) does not yet exist** — noted in the document as "partially exists" (Cursor 2.4 has cross-provider but hub-and-spoke; Claude Code Agent Teams has peer-to-peer but Claude-only; OpenCode has design proposal but not shipped).

**(c) Has anything changed since design?**
Yes, two important updates from contributor issue #6:
- **OpenCode capabilities**: Reporter describes "model selection, variant level, even a different provider, different system prompt... can talk to each other." This suggests OpenCode may provide Tier 2 (full cross-provider + peer-to-peer).
- **Current assessment in document**: "No product currently combines cross-provider multi-model with peer-to-peer agent communication" — this may become outdated if OpenCode ships.

The document notes this possibility but conservatively treats Tier 2 as "still in development." This is appropriate — contributor report is secondhand and not publicly verifiable.

**(d) Recommended action**: **UPDATE (add OpenCode as Tier 2 candidate)**

The document should be updated to reflect contributor issue #6 more explicitly:
- Add OpenCode.json configuration reference to the Tier 2 section
- Note that Tier 2 is "partially exists" → "in development / potentially shipping Q2 2026"
- Add a decision note: "If OpenCode ships with confirmed cross-provider + peer-to-peer support, programs collapse into one: run `/committee` with each character routed to a different model via platform-native mechanism. This would represent convergence of Tier 1 and Tier 3 into native platform support."

This is a minor update, not a design change. The framework is robust to the Tier 2 status change.

**(e) Connection to wild material**:
- **Issue #6**: Directly motivates the update above
- **Open games formalization** (`wild/committee-games/`): Adds theoretical depth to the taxonomy but does not change it. The taxonomy is implementation-focused; open games is game-theoretic. They are complementary.

---

### 4. Multi-Model Committee: Experimental Plan

**Status**: Active (not started)
**Design**: 4-phase protocol testing model diversity via LiteLLM orchestration (Tier 3)
**Relevance**: HIGH — tests the model-diversity axis; complementary to agent-independence

#### Assessment

**(a) Is the question still interesting and relevant?**
Yes. Model diversity is a distinct hypothesis from architectural independence:
- Agent-independence tests: "Do separate context windows improve deliberation?" (holding model constant)
- Multi-model tests: "Do different training distributions improve deliberation?" (via Tier 3 orchestration)

The two programs are orthogonal and together justify pursuing Tier 2.

**(b) Are prerequisites met?**
Most, but not all:
- **LiteLLM proxy**: Available, mature, well-documented ✓
- **API keys for 2+ providers**: User responsibility, not a blocker ✓
- **Clojure orchestrator (pcrit-llm)**: Preferred implementation language, exists as library ✓
- **Model personality profiles**: Feasible to generate, not pre-existing
- **Comparative analysis code**: Reference document provides Python templates; Clojure equivalent needed

The main blocker is **availability of contributor with Clojure expertise and access to multi-provider API keys**. This is a resource constraint, not a design issue. Python templates in reference.md provide a fallback.

**(c) Has anything invalidated or superseded the design?**
No. The design is comprehensive and well-grounded in multi-agent debate literature. One concern flagged in the document:
- "Loss of 'game within game'" (Risk, Section 5) — the single-model roleplay forces the model to generate and suppress its own tendencies, creating a second-order strategic layer. Multi-model removes this layer. The document mitigates this with Pattern 3 (no character prompting) and Pattern 4 (hybrid, tuned briefs) comparison.

This is not a flaw; it is a known trade-off documented in the mitigation.

**(d) Recommended action**: **RUN (Phase 1–2 in parallel with agent-independence)**

Phases 1–2 are 4–6 weeks and should start as soon as a contributor with LiteLLM expertise (or willingness to learn) is available. The program is self-contained and produces publishable results at each phase gate. Phase 2 decision gate (does hybrid multi-model beat single-model?) is the main commitment point.

If agent-independence (Phase 1) shows no improvement, multi-model becomes higher priority (suggests model diversity is the axis that matters). If both show improvement, the case for Tier 2 development becomes compelling.

**(e) Connection to wild material**:
- **Issue #6**: Multi-model program is Tier 3 (external LiteLLM orchestration). Issue #6 suggests Tier 2 (native platform support) may arrive. If Tier 2 ships, this program becomes a prototype for what production Tier 2 should replicate.
- **Open games formalization**: Applies equally well to multi-model committees. The game-theoretic structure does not depend on whether models are single or diverse.

---

### 5. Evaluating Deliberative Architectures: Black Swan Hindsight Framework

**Status**: Not started
**Design**: Test which deliberative architectures anticipate structural risks using historical cases and constructed scenarios
**Relevance**: HIGH — tests *anticipatory validity* (does methodology see what's coming?) rather than just output quality

#### Assessment

**(a) Is the question still interesting and relevant?**
Yes, and critically so. The evaluation-schemes framework tests "process quality" (do structured methods produce better-reasoned outputs). This program tests "foresight" (do structured methods anticipate risks that simpler methods miss). These are distinct and complementary.

The Black Swan framing is particularly valuable: it asks not "are you right?" but "did you see the failure case?" This is the right criterion for decision-support systems.

**(b) Are prerequisites met?**
Partially. The program requires:
- **Historical case corpus**: Requires research effort, but protocol is designed (Section VIII documents Glenda/Crock coercion and blast radius scenarios)
- **Knowledge contamination mitigations**: Documented (blind evaluation, constructed scenarios, Glenda/Crock protocol does not require historical research)
- **Scenario-generation and committee pipeline**: Already operational ✓
- **Evaluation rubrics**: Same as other programs ✓

The **Glenda/Crock protocol** (Section VIII) is a self-contained pilot that requires no historical research and tests the core claim directly. This is an excellent entry point.

**(c) Has anything invalidated or superseded the design?**
No direct invalidation. One clarification needed: The document explicitly relates to evaluation-schemes Design C (Section XI) and positions itself as complementary, not redundant. The distinction is clear: evaluation-schemes Design C asks "Does the committee process improve reasoning?"; this framework asks "Does it anticipate risks?" These are both worth answering.

The **legal domain test case from issue #7** is directly applicable here. The contributor suggests:
- Gather historic case documents
- Feed cyberneutics system the initial evidence
- Fan out to plausible narratives (scenario generation)
- Funnel to committee deliberation
- Compare committee verdict to historical outcome

This is almost exactly the Black Swan hindsight protocol with a concrete domain application.

**(d) Recommended action**: **RUN (Glenda/Crock protocol first; then integrate legal domain)**

The Glenda/Crock protocol should be piloted first (requires no historical research, tests core claim directly, low setup cost). If that succeeds, expand to real historical cases or the legal domain test case. The program is good as written; no design changes needed.

**(e) Connection to wild material**:
- **Issue #7** (legal domain): Provides a concrete pilot application. The contributor's understanding of the methodology is correct ("Juries are a bit different... Cyberneutics is more useful for problems that don't have a clear answer"), and the legal test case maps cleanly onto the Black Swan framework.

---

### 6. Evaluation Schemes for Cyberneutics Mechanisms

**Status**: Active (umbrella design document)
**Design**: Six evaluation designs (A–F) testing whether structured mechanisms produce measurably better decisions
**Relevance**: HIGHEST — addresses the core question: "Does committee-based deliberation beat simpler approaches?"

#### Assessment

**(a) Is the question still interesting and relevant?**
Yes, fundamental. This is the highest-priority uncertainty per the README. The evaluation-schemes framework is the canonical research design for addressing it.

**(b) Are prerequisites met?**
Yes. The framework is complete and grounded:
- **Core questions**: Well-articulated (Section I)
- **Why evaluation is hard**: Thoroughly analyzed (Section II)
- **Proposed dimensions**: Six rubrics with codebooks (Sections III, VIII)
- **Extracted designs**: Ablation study (Design F) and Condorcet comparison (Design D) are standalone executables with results locations

Condorcet comparison has already been run (2 runs, Feb 22, results in `condorcet-comparison/results/`). This provides partial evidence toward the main question.

**(c) Has anything changed since design?**
Yes, one valuable update: Condorcet comparison is now complete with preliminary findings:
- Deliberation can change outcomes (code-of-conduct case)
- The divergence mechanism is cross-examination
- Question type matters (hidden second-order concerns make deliberation more valuable)
- Deliberation produces richer output than independent aggregation

These findings support the main hypothesis ("structured deliberation produces better outcomes") but are based on two datapoints. The evaluation-schemes framework is designed for larger samples.

**(d) Recommended action**: **RUN (Phase 1: ablation study; Phase 2: blind panel; Designs D–F in parallel)**

This is the backbone research design. Ablation study (Phase 1, extraction Design F) should start immediately. Blind panel (Design A, Phase 2) is the main evidence-building effort and should follow ablation completion. Designs D, E, F can run in parallel as resources allow.

**(e) Connection to wild material**: None direct. Theoretical deepening of rubrics via furry logic (issue #3 on soft types and distributional membership) could improve dimension codebooks, but this is a future enhancement.

---

### 7. Societies of Thought: Research Plan (Ten Action Items)

**Status**: Active (implementation roadmap)
**Design**: Ten modular action items strengthening methodology infrastructure, testing generalization, formalizing theory, expanding evidence base, and integrating MOOLLM
**Relevance**: MEDIUM–HIGH — all items contribute to the research portfolio, but priority varies

#### Assessment

**(a) Is the framework still interesting and relevant?**
Yes. The ten items directly address gaps identified in the Societies of Thought paper analysis (`essays/societies-of-thought-synthesis.md`):
- Items 1–3: Infrastructure (personality, balance, reconciliation) — strengthen existing components
- Items 4–5: Generalization (transfer learning, domain variants) — expand scope
- Items 6–7: Theory (information theory, social scaling) — formalize foundations
- Items 8: Architecture (MOOLLM integration) — systematize patterns
- Items 9–10: Evidence (worked examples, comparative effectiveness) — build proof base

**(b) Are prerequisites met?**
Most items are self-contained with low dependencies:
- **Item 1** (Big Five characterization): Requires roster + psychology reference; can start immediately
- **Item 2** (balance metrics): Requires design of analyzer; can start immediately
- **Item 3** (reconciliation protocols): Requires design + testing; can start immediately
- **Items 4–5** (transfer, domain variants): Require experimental runs; depend on availability of someone to run `/committee`
- **Items 6–7** (information theory, social scaling): Require theoretical writing; low blocker
- **Item 8** (MOOLLM): Requires architecture knowledge + Don Hopkins collaboration; higher dependency
- **Items 9–10** (examples, comparative effectiveness): Require sustained experimental effort; low blocker

No item is fully blocked. All items are well-scoped and have explicit success criteria.

**(c) Has anything changed since design?**
Yes, two developments:
- **Wild material on potential-to-sense** (`wild/potential-to-sense/from_semantic_potential_to_situated_sense.md`) — directly supports Item 8's requirement for human gates. The essay makes the case that meaning emerges through pragmatic collapse in human-LLM interaction, not through model-internal representation. This is the theoretical foundation for why human participation is essential.
- **Open games formalization** (`wild/committee-games/committee-as-open-game.md`) — provides the game-theoretic underpinning for Item 6 (information-theoretic foundations). The open games framework makes explicit what information-theory essay should explain: why the committee structure optimizes for surprise and entropy injection.

These do not invalidate the plan; they provide theoretical scaffolding that makes execution easier.

**(d) Recommended action**: **RUN (Items 1–3 immediately; Items 4–10 in priority sequence)**

This is a modular plan. Items 1–3 are quick wins (infrastructure) and should start immediately. Items 4–5 (evidence building) and 9–10 (comparative study) are higher-effort but high-impact and should follow ablation completion. Items 6–7 (theory) are lower-priority but easy to run in parallel. Item 8 (MOOLLM) is lower-priority and blocked on Don Hopkins collaboration.

No design changes needed. The plan is well-structured.

**(e) Connection to wild material**:
- **Potential-to-sense essay**: Directly grounds Item 8 (human gates requirement)
- **Open games formalization**: Directly grounds Item 6 (information-theoretic foundations)
- **Furry logic diary**: Informs Item 2 (balance metrics) and Item 6 (dimensional analysis of rubrics)

---

### 8. Condorcet Comparison: Deliberative vs. CJT-Style

**Status**: Completed (2 runs, Feb 22 2026)
**Design**: Paired-pipeline comparison on same questions
**Relevance**: MEDIUM (provides partial evidence; completed, not ongoing)

#### Assessment

**(a) Is the result still interesting?**
Yes. The completed study provides the first empirical evidence that deliberation can change outcomes (code-of-conduct case: CJT-style said Aye, deliberative said Nay on same question, same roster). The mechanism is cross-examination — Vic and Tammy changed their votes when forced to confront Maya's enforcement objection.

This is valuable evidence, limited by sample size (two runs) but directionally clear.

**(b) Should it continue?**
Yes, as part of the evaluation-schemes framework (Design D). The protocol is reusable. Additional runs on different question types (especially value-laden questions with hidden second-order concerns, where divergence was highest) would build a stronger evidence base.

**(c) Recommended action**: **RUN (additional runs as part of evaluation-schemes Phase 2)**

The protocol is established (`artifacts/comparison-protocol-deliberative-vs-cjt.md`). Contrib

utor can run additional instances in 1–2 afternoons each. Recommended expansion: 5–10 additional runs covering different question domains to test whether divergence generalizes beyond the code-of-conduct case.

**(d) Connection to wild material**: None direct. The study is methodologically complete and provides good evidence toward evaluation-schemes framework.

---

## Implicit New Research Programs

The recent wild material (Feb–Mar 2026) suggests three new research programs not yet formalized:

### A. Furry Logic and Soft-Type Classification

**Source**: `wild/diary/2026-03-13-furry-logic.md`
**Core claim**: Soft types in palgebra handle graded membership in one type; furry logic handles genuine plurality of membership across multiple distinct types. A text can fully inhabit two different types simultaneously (e.g., evidence AND argument).

**Why it matters**:
- Pipeline routing depends on crisp or probabilistic type assignment. If types are distributions, routing becomes Bayesian decision-theoretic.
- The rubric system uses soft-type membership (e.g., "how much is this an argument?"). Extending to furry logic would allow multi-dimensional type analysis.
- Connects to soft-type theory in palgebra and formal concept analysis.

**Recommended action**: **FORMALIZE (essay + optional implementation)**
- Short-term (essay): Draft tentative essay outline (Section 7 of diary provides structure) — 2–3 weeks of writing
- Medium-term (optional): Build a multi-dimensional rubric analyzer that computes type distributions rather than single-type scores
- This work should follow Items 1–2 of societies-of-thought plan (Big Five mapping, balance metrics) to ensure rubric system is mature enough to extend

**Connection to existing programs**:
- Ablation study (Design F) uses six rubrics; furry logic would reinterpret scores as distributions rather than point estimates
- Evaluation-schemes framework would benefit from multi-type analysis of transcripts

---

### B. Open Games Formalization of Committee Structure

**Source**: `wild/committee-games/committee-as-open-game.md`
**Core claim**: Translate the committee architecture into open games (compositional game theory). Characters are non-utility-maximizing players (propensity-driven, not Nash-equilibrium-seeking). The committee reaches equilibrium when all perspectives are covered, not when preferences converge.

**Why it matters**:
- Palgebra provides resource-theoretic treatment; open games provide game-theoretic structure
- Makes explicit what is implicit in propensity-driven play: the strategy set is constrained by epistemic role, not utility
- Opens connection to ACT/Cybercat research community
- Clarifies the backward-flowing evaluation signal and how rubrics determine equilibrium behavior

**Recommended action**: **VALIDATE (publish bridge paper; optional Cybercat collaboration)**
- Short-term: Publish `committee-as-open-game.md` as a bridge document to the ACT community. It is well-written and complete.
- Medium-term: Engage with Cybercat researchers on dependent optics (Section 8 of the document) as a formal framework for the fan/funnel duality
- This is primarily a theoretical contribution, not an empirical program

**Connection to existing programs**:
- Provides formal grounding for why the committee structure works (complementary to information-theory essay planned in Item 6)
- Supports evaluating-deliberative-architectures by making architectural assumptions explicit
- Informs agent-independence and multi-model programs by clarifying what "equilibrium" means in a propensity-driven game

---

### C. Potential-to-Sense as Grounding Framework for Human Gates

**Source**: `wild/potential-to-sense/from_semantic_potential_to_situated_sense.md`
**Core claim**: LLMs maintain fields of semantic potential. Meaning becomes actual only through human participation, which introduces pragmatic, embodied, and social constraints that collapse potential into situated sense. This is a cybernetic process (control loop, feedback, recursive adjustment).

**Why it matters**:
- Explains why human gates (evaluation, resolution, deliberation direction-setting) are not optional
- Grounds the evaluation loop as a necessity, not a luxury
- Connects to conversation theory (Pask), constructivism (von Foerster), and pragmatic semantics
- Informs design of human-in-the-loop systems and interface requirements

**Recommended action**: **PROMOTE (move to essays/; use as foundational theory)**
- Immediate: Move `potential-to-sense/from_semantic_potential_to_situated_sense.md` from `wild/` to `essays/` — it is polished, well-argued, and provides essential theoretical grounding
- Update `essays/README.md` to include it in the essays index
- Use as reference material for Items 6–8 of societies-of-thought plan (theory and architecture)
- Consider as part of the formal methodology documentation

**Connection to existing programs**:
- Directly supports evaluation-schemes framework by explaining why evaluation is essential (it's how human participation converts potential into actionable sense)
- Grounds the ablation study's evaluation loop component (Item E)
- Informs agent-independence and multi-model programs by clarifying what human participation contributes that model-only discourse cannot

---

## Cross-Cutting Analysis

### Contributor Issues and Program Connections

**Issue #6** (OpenCode capabilities):
- Direct connection: Suggests Tier 2 (cross-provider + peer-to-peer) may exist or be shipping soon
- Recommended update: Add OpenCode to committee-implementation-taxonomy as a Tier 2 candidate with caveat ("under development, design proposal public, feature not yet verified")
- Impact: If confirmed, accelerates timeline for multi-model committee (could become native platform support rather than external orchestration)

**Issue #7** (legal domain test case):
- Direct connection: Legal deliberation is a natural pilot for evaluating-deliberative-architectures framework
- Recommended action: Use Glenda/Crock protocol first (no historical research needed); then expand to legal domain as Phase 2
- Impact: Provides a concrete, high-stakes application domain for validation

**Issue #11** (multimodal/discrete subagent deliberation):
- Direct connection: Extends agent-independence program to include image/diagram inputs
- Recommended action: Phase 1 of agent-independence uses text-only deliberation; Phase 2+ can explore multimodal inputs
- Impact: Tests whether architectural independence benefits generalize beyond text

### Should OpenCode be added to the implementation taxonomy?

**Yes, with caveats.**

Current status: Tier 2 (cross-provider + peer-to-peer) is listed as "partially exists" and "no product currently combines" the two.

Recommended change:
1. Add OpenCode.json reference to Section 3 (Three Implementation Tiers)
2. Rewrite Tier 2 status from "partially exists" to "in development":
   - Claude Code Agent Teams: peer-to-peer ✓, single-model only ✗
   - Cursor 2.4: cross-provider ✓, hub-and-spoke only ✗
   - OpenCode: design proposal published; cross-provider + peer-to-peer claimed by contributor; unverified by maintainer
3. Add decision note: "If OpenCode ships with confirmed support, Tier 2 becomes the reference implementation, and programs collapse: run `/committee` with model routing native to the platform."

**Impact**: This is a status update, not a design change. The taxonomy and programs remain valid under all scenarios (OpenCode ships / doesn't ship / ships partial).

### Should the legal domain test case become a pilot for evaluating-deliberative-architectures?

**Yes.**

The legal domain provides:
- **High stakes**: Verdicts have real consequences; ground truth is available (jury verdict vs. historical outcome)
- **Complexity**: Legal reasoning involves evidence, precedent, interpretation, and value judgment — ideal for testing committee's advantage over single-prompt approaches
- **Clear protocol**: The contributor understands the methodology and has suggested exactly the right experimental setup

Recommended action:
1. Run Glenda/Crock protocol first (constructed scenario, no historical research)
2. If successful, move to legal domain pilot using actual historical cases
3. Document the results as `evaluating-deliberative-architectures/results/legal-domain-pilot/`
4. Update the main program document to reference the legal pilot as Phase 2+

**Impact**: Provides a concrete application domain for the Black Swan framework and increases real-world relevance.

### Should any programs be merged?

**No significant mergers recommended.**

Potential candidate: **multi-model-committee + committee-implementation-taxonomy**
- Current state: Taxonomy is a reference framework (all three tiers documented); multi-model tests Tier 3
- These are complementary, not redundant. The taxonomy organizes the design space; multi-model runs an empirical test within that space.
- No merger needed. The taxonomy should remain as a design space reference; multi-model should remain as an empirical protocol.

Potential candidate: **ablation-study + societies-of-thought Item 10 (comparative effectiveness)**
- Current state: Ablation tests within-methodology variation; Item 10 tests against external baselines
- These are complementary. Ablation answers "which components matter?"; Item 10 answers "does it beat simpler approaches?"
- No merger needed. These should run in sequence: ablation first (faster, cheaper, identifies key components), then Item 10 (uses ablation insights to guide baseline selection).

---

## Implicit New Research Programs Suggested by Wild Material

Three new programs are suggested by recent wild material but not yet formalized:

1. **Furry logic and soft-type classification** — extends palgebra soft types to multi-type membership; impacts rubric system and routing
2. **Open games formalization** — provides game-theoretic grounding for committee structure; bridge to ACT/Cybercat
3. **Potential-to-sense essay** — explains why human gates are essential; should be promoted from wild/ to essays/

These should be:
- **Furry logic**: Formalized as an essay (2–3 weeks) after societies-of-thought Items 1–2 (establish rubric maturity)
- **Open games**: Published as bridge paper (already complete; ready to ship)
- **Potential-to-sense**: Promoted to essays/ immediately (move only; essay is complete and polished)

---

## Status Summary Table

| Program | Status | Priority | Feasibility | Blocker | Recommended Action |
|---------|--------|----------|-------------|---------|-------------------|
| **Ablation Study** | Not started | HIGHEST | Immediate | None | RUN (start now) |
| **Agent Independence** | Not started | HIGH | Immediate (Phase 1) | Medium (exp. feature) | RUN (Phase 1 now; Phase 2 conditional) |
| **Committee Taxonomy** | Reference doc | HIGH | N/A | None | UPDATE (add OpenCode as Tier 2 candidate) |
| **Multi-Model Committee** | Not started | HIGH | 4–6 weeks | Clojure expertise | RUN (Phases 1–2 parallel with ablation) |
| **Evaluating Deliberative Arch.** | Not started | HIGH | 4–6 weeks | None | RUN (Glenda/Crock first; legal domain Phase 2+) |
| **Evaluation Schemes** | Active | HIGHEST | Ongoing | None | RUN (Phase 1–2 sequentially) |
| **Societies of Thought** | Active | HIGH | Modular, 1–12 months | Some depend on prior work | RUN (Items 1–3 now; 4–10 sequentially) |
| **Condorcet Comparison** | Completed | MEDIUM | Ongoing (expand) | None | RUN (additional instances as part of eval-schemes) |
| **(Implicit) Furry Logic** | Diary entry | MEDIUM | 2–3 weeks | Rubric maturity | FORMALIZE (essay after societies-of-thought Items 1–2) |
| **(Implicit) Open Games** | Complete draft | MEDIUM | Ready | None | PUBLISH (bridge paper; already complete) |
| **(Implicit) Potential-to-Sense** | Draft essay | MEDIUM | Ready | None | PROMOTE (move to essays/) |

---

## Recommendations for Immediate Action

### This month (March 2026):
1. **Start ablation study Phase 1** if a contributor with experimental design skills is available
2. **Start agent-independence Phase 1** (paired comparison, 1 topic, 1 afternoon)
3. **Publish open-games bridge paper** (it is complete; ready for Cybercat engagement)
4. **Promote potential-to-sense essay** to essays/ (polished, foundational, ready)
5. **Update committee-implementation-taxonomy** to reference OpenCode as Tier 2 candidate

### Next 2–4 weeks:
6. **Glenda/Crock protocol** (evaluating-deliberative-architectures pilot) — 1 week setup, 1 week analysis
7. **Societies-of-thought Items 1–3** (Big Five, balance metrics, reconciliation) — 2–3 weeks, low blocker
8. **Multi-model Phase 1** (baseline + model profiles) — 1–2 weeks, if LiteLLM contributor available

### Contingent on Phase 1 results:
9. **Agent-independence Phase 2** (5 topics, scored) — conditional on Phase 1 showing observable differences
10. **Evaluating-deliberative-architectures Phase 2** (real historical cases or legal domain) — conditional on Glenda/Crock success
11. **Multi-model Phase 2** (comparative architectures) — conditional on Phase 1 baseline established

### Medium-term (by end of Q2 2026):
12. **Furry logic essay** — after societies-of-thought Items 1–2 establish rubric maturity
13. **Ablation study analysis** (Table 1–3, cost-benefit summary)
14. **Evaluation-schemes Phase 2** (blind panel design, rater coordination)

---

## Conclusion

The research portfolio is well-aligned, strategically sound, and ready to execute. The eight documented programs cover the three highest-priority uncertainties with complementary experimental designs. Three implicit new programs (furry logic, open games, potential-to-sense) add theoretical depth and should be formalized/promoted.

**No design invalidations identified.** Changes since program design (Condorcet completion, Agent Teams availability, OpenCode proposal, legal domain interest) strengthen the portfolio rather than undercutting it.

**Key recommendation**: Proceed with ablation study and agent-independence immediately. These are methodologically cleanest, lowest-resource, and most directly address core claims about the methodology's value and architecture.

**Timeline**: Ablation (1 month), agent-independence Phase 1 (1 afternoon), multi-model Phase 1 (1–2 weeks), evaluating-deliberative-architectures Glenda/Crock (2 weeks). By end of April 2026, the portfolio will have data on component contributions, architectural independence, model diversity, and risk anticipation.

---

**Document end**: Research program triage, 2026-03-13
