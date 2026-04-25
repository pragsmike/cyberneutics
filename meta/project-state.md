# Project State

Last updated: 2026-04-25

This document is the canonical current-state reference for repo structure, compatibility truths, and live open questions. It replaces the old stale backlog-file role with a narrower, actively maintained state doc.

## Current architecture truths

- `agent/onboarding-core.md` is the canonical onboarding source.
- `AGENTS.md`, `CLAUDE.md`, and `.cursor/rules` are thin tool-specific entry points.
- Canonical skill bodies live only in `.claude/skills/`.
- Claude and Cursor command discovery is handled by thin wrappers in `.claude/commands/` and `.cursor/commands/`.
- Live outputs belong in external situation directories resolved via `--situation`, `.claude/cyberneutics-config.yaml`, or `~/situations/<topic-slug>/`.
- Checked-in run records in this repo are examples or historical records. They are not live runtime outputs.
- Archive directories (`agent/archive/`, `wild/archive/`) are historical only and excluded from onboarding unless provenance is explicitly requested.
- When adding cross-references in README files, use markdown links, not backtick paths (convention established 2026-03-07).

## Compatibility migration status

Complete as of 2026-03-07. All items resolved:

- Canonical onboarding doc established.
- Root wrappers aligned to the canonical onboarding doc.
- Canonical skill-source rule established: `.claude/skills/` only.
- Repo-local command wrappers added for Claude and Cursor.
- Runtime-path language converted to situation-directory language.
- Checked-in scenario and deliberation records labeled and housed as examples.
- Structural linting in place to keep these invariants from drifting.

## Recent changes (2026-03-08 through 2026-03-20)

### New content added (2026-03-08)

- `wild/committee-games/committee-as-open-game.md` — Translation of adversarial committee into open games (compositional game theory). Bridge to ACT/Cybercat community.
- `wild/diary/2026-03-13-furry-logic.md` — Diary entry exploring distributional type membership ("furry logic"), extending soft types from graded single-type to multi-type measurement.
- `wild/potential-to-sense/from_semantic_potential_to_situated_sense.md` — Essay on meaning as co-produced in conversation; theoretical grounding for human gates.
- `palgebra/categorical-structures.md` — Pedagogical treatment of category-theoretic constructions in the pipeline (products, coproducts, equalizers, pullbacks, pushouts, fan/funnel as spiders, Probe as universal property test).
- `wild/issues/` — Five GitHub issues from contributors (subagent capabilities, legal domain test case, narrative/archetypes, multimodal deliberation, emotional modeling).

### Documentation updates (2026-03-13)

- Created README.md for `wild/committee-games/` and `wild/potential-to-sense/`.
- Reorganized `wild/README.md` from flat list to categorized sections covering all fourteen topic directories.
- Added `categorical-structures.md` entry to `palgebra/README.md`.
- Completed `cyber-sense` → `cyberneutics` rename sweep in live content (diary entries, example deliberations). Archive files left as historical.
- Refactoring sprint plan created: `agent/prompts/refactoring-sprint-2026-03.md`.

### New content added (2026-03-15)

- `wild/communicating-absent-parties/README.md` — Seven-section synthesis from a 40-page Perplexity deep research report on absent-party communication across eight domains (nuclear semiotics, Pask CT, decipherment, Berea, SETI, information cascades, hermeneutics, biosemiotics). Bridges to organ/bloodstream distinction, calibration register at zero-feedback limit, and furry logic.
- `wild/potential-to-sense/pask-machine-machine.md` — Pask's Colloquy of Mobiles (1968) as machine-machine conversation; chameleon-mirror problem, bisimulation as propensity constraint, Pask's machine trajectory from Musicolour to THOUGHTSTICKER.
- `wild/potential-to-sense/README.md` — Updated with pask-machine-machine.md entry and cross-references.
- `wild/diary/2026-03-15-absent-parties-and-chameleons.md` — Absent-party communication as unifying thread; organ/bloodstream mapping at calibration register limit; Pask's chameleon-mirror problem; Berea bridge.
- `wild/diary/2026-03-15-emotional-attention-steering.md` — Addresses GitHub issue #13; emotional state as continuous PID-controlled variables per character; bricking/exclusion mechanisms.
- `wild/diary/2026-03-15-mystic-narrative.md` — Jean Houston's Four Levels model as pre-narrative conditioners; maps across shamanic and Diana's Grove lineages; connects to Bruner-Kahneman synthesis.

### Black Swan Phase A committee deliberation (2026-03-17)

- `../situations/black-swan-phase-a/deliberations/` — Full deliberation record (00–06): charter, convening, roster, deliberation (4 rounds), resolution, evaluation-1 (10/15), remediation-1, evaluation-2 (13/15 — at bar). Decision: targeted revision with reassessment trigger.
- `meta/project-state.md` — Active research section updated with committee decision and execution plan.

### Prompt and agent maintenance (2026-03-16)

- `agent/prompts/improve-repo-next-step.md` — Updated bias areas to reflect post-sprint state.
- `agent/prompts/editorial-review.md` — Added `essays/glossary.md` to scope.

### LLM-math-inquiry recording and planning (2026-03-20)

- `agent/onboarding-core.md` — Added "Epistemic positions the agent must know" section (inspectability, epistemic status, LLM-math-inquiry). Epistemic caveat added to palgebra row in repository map.
- `meta/project-state.md` — Added "Epistemic positions (recorded 2026-03-20)" section.
- `wild/llm-mathematical-inquiry-outline.md` — New: rough research program outline (scope, methods, dependencies, relationship diagram).
- `agent/handoff-2026-03-20-llm-math-inquiry.md` — New: handoff with placement plan for seven locations across main documents.

### Onboarding repair and cross-agent compatibility (2026-03-20)

- `agent/onboarding-core.md` — Added Step 0 (repo root verification) and strengthened Step 1 (list-before-read with failure guidance). Updated compatibility model with Cowork, Cursor auto-load, and Antigravity entries.
- `.claude/skills/handoff/SKILL.md` — Added step 6: update `meta/project-state.md` during handoff. Updated Usage section.
- `.cursor/rules` — New file. Cursor onboarding entry point mirroring `CLAUDE.md` and `AGENTS.md`.
- Diagnosed and fixed silent onboarding failure in Cowork where relative paths caused agents to miss handoff files when cwd ≠ repo root.

### Repo trimming and archive reorganization (2026-03-20)

- **Examples trimmed**: Reduced from 14 deliberation + 3 scenario directories to 5 deliberation + 1 scenario. Kept representative set covering distinct deliberation types: `is-author-crackpot`, `is-author-crackpot-revisited` (mandated), `methodology-adoption-strategy` (full-pipeline worked example), `eval-delib-architectures` (protocol evaluation with remediation cycles), `soft-type-extension` (extended feedback loop). Scenario: `methodology-adoption-strategy` (paired with kept deliberation).
- **Black-swan references fixed**: Four files updated to point from `examples/deliberations/black-swan-*` to `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-*` (the canonical location after the example copies were removed).
- **`wild/archive/` created**: Four dormant wild topics moved to `wild/archive/`: residuality-theory, harness-engineering, neo-cybernetics, software-factories. `wild/README.md` updated.
- **Onboarding updated**: Step 4 now covers both `agent/archive/` and `wild/archive/`. Wild detail section lists the archive directory.

### Repo trimming pass 2 (2026-03-20)

- **`bradley_thesis.pdf` deleted** (8 MB): publicly available thesis; citation retained in research survey.
- **`wild/subagent-personas-for-debate/` archived**: moved to `wild/archive/` (was marked SUPERSEDED).
- **`cowork-plugin/` removed**: superseded by native `.claude/skills/` structure. Cowork Plugin section removed from `README.md`.
- **39 archived handoffs digested**: replaced with `agent/archive/handoff-digest-2026-01-to-03.md`. Active handoffs (03-07c through 03-20) retained.
- **Pask-mesh-fitting research consolidated**: 7 short research notes merged into `research/research-survey.md`; tractability analysis kept separate.
- **Deferred**: Essay 07 (~30% redundant with 01/05/06 per editorial review) flagged for future editorial trim.

### Bradley bibliography merge and architecture doc revisions (2026-03-22)

- **Master bibliography expanded**: `references/README.md` gained 26 new entries. 11 NEW papers from the Bradley–cyberneutics conversation (density operators, enriched language categories, magnitude, tropical geometry). 14 palgebra-cited papers that were missing from the master bibliography (Fritz, Cho & Jacobs, Perrone, Kock, Heunen et al., Jacobs, Ghani et al., Spivak operad, Lawvere 1973, Leinster, Rosenthal, Atkey, Danos & Ehrhard, Bradley thesis). 1 Vickers-Faith-Rossiter semiotics paper. Kelly annotation enriched. CT&F section restructured into 7 subsections.
- **Palgebra architecture docs revised**: §2d (closure/self-reference) and §2e (morphisms as texts) added to `categorical-structures.md`. Terminology note disambiguating SWE vs. Kelly senses of "enrichment" added to §2b. Cross-references planted in `soft-type-theory.md`, `decorated-texts.md`, `reference.md`, `README.md`. "Self-applicable" entry added to key-ideas list.
- **Prompts archived**: `cowork-merge-bradley-references.md` and `cowork-revise-architecture-docs.md` moved to `agent/archive/`.

### Fuzzy type theory investigation (2026-03-22)

- **`wild/fuzzy-type-theory/north-cyberneutics-comparison.md`** — Combined report comparing North's fuzzy type theory, Mulder-North-Péroux "Measuring Data Types" paper, and cyberneutics soft type / furry logic system. Conclusion: sibling constructions, not specialization. Key finding: measuring coalgebras as formal model for rubric scoring. Adoption triage: acknowledge North as prior art (now), investigate Set^M enrichment and C-inductive types (medium-term), defer dependent types.
- **`wild/fuzzy-type-theory/` directory restructured**: Three files with distinct roles — `README.md` (navigation map, research question, adoption triage summary), `norths-fuzzy-type-theory.md` (standalone reference summary of North's program, rewritten from earlier report), `north-cyberneutics-comparison.md` (comparative analysis, compressed §1-§2 to avoid overlap with reference file). Old untracked `fuzzy-type-theory-report.md` deleted.

### Diary skill integration and new diary entry (2026-03-26)

- **`.claude/skills/diary/SKILL.md`** — New skill for writing diary entries. Documents file conventions, document structure, public-facing privacy filters, relationship to other artifacts, and common mistakes. Format-fixed to match other skills (YAML frontmatter added).
- **`.claude/commands/diary.md`** — New thin slash command wrapper for diary skill.
- **`agent/onboarding-core.md`** — Added `/diary` row to Available Workflows table.
- **`wild/diary/2026-03-26-echo-chamber-immune-organs.md`** — New diary entry: echo chambers reframed as immune organs via organ/bloodstream distinction; emotion-first vs. inference-first as thymic discrimination signal; dark shares as organ/bloodstream interface morphism; missing System 3* (calibration gap).
- **`applications/narrative-immune-systems/references-choe-echo-chamber-studies.md`** — New: six verified studies with full citations, key findings, and cyberneutics cross-references (Simchon SDT inoculation meta-analysis, Van der Linden Instagram prebunking, Kim voter suppression, Bond 61M mobilization, CIRCLE youth sources, Civic Power IPO report).

### Residuality theory: survey, bilateral note, fan-as-stressor-generator, Deleuzian-grammar working note (2026-04-25)

- **Five new files in `wild/residuality-theory/`**: `state-of-residuality-2026.md` (~5,400-word survey paper drawing on all six O'Reilly papers), `residuality-bibliography.md` (~2,900-word union bibliography), `cyberneutics-and-residuality.md` (~4,200-word bilateral relationship note), `fan-as-stressor-generator.md` (~2,300-word standalone working note pitched at residuality practitioners), `assemblage-rhizome-nomad.md` (~3,000-word working note on the Deleuze-Guattari conceptual grammar that operates in residuality theory beneath O'Reilly's explicit Deleuze citations).
- **Directory README rewritten** as agent-facing navigation hub: source-material navigation table, cited-but-not-archived list, practitioner-introduction links, three-step reading recommendation. Existing Cyberneutics-internal content (Deleuzian thread, residues-vs-eigenforms, palgebra connection) preserved.
- **Major framing correction recorded**: the 2026-04-20 diary's "Deleuze as name-check only" claim was bounded to the 2021 *Philosophy* paper. The 2023 *Residuality and Representation* paper develops Deleuze substantively (five in-text engagements, three secondary references). The recommendation to "soften the Deleuze framing in essays 06 and 10" is **retracted**. Essays 06 and 10 stand as written. Corpus has multiple primary philosophical anchors across its arc, not one.
- **Stacey ordered.** *Complexity and Organizational Reality* (Routledge 2009) ordered late April 2026; arrival expected late April / early May. Essay-13 drafting waits on this delivery for primary-source engagement with the cybernetics-critique answer.
- **Cleanup pass on false signals**: 14 items addressed across `wild/README.md`, the bilateral note, the survey, the residuality-theory README, the 2026-04-20 diary, `essays/README.md`, and this file.

### references/papers/ audit + Machine in the Ghost assimilation (2026-04-24)

- **Audit findings** surfaced 10 issues including missing 2022 entry in chronology, master bib out of sync (missing 2019 and 2022 papers), asymmetric See-also footers, naming inconsistency for the 2021 *Philosophy* paper, two contradictory not-archived lists, and absent agent-discoverability scaffolding (token-budget guidance, Cite-which-for-what table, frontmatter).
- **Fixes applied** (items 1–7 + 9 + 10): chronology gained the missing 2022 entry; master bib in `references/README.md` gained 2019, 2022, and *Machine in the Ghost* entries with archive cross-links; See-also footers symmetrized across all 6 summaries; 2021 paper renamed under unified `Residuality-Oreilly-2021` slug via `git mv`; all 12 paper-related markdowns + chronology gained YAML frontmatter (title, author, year, venue, DOI, license, type, length_words, topics, companions); `papers/README.md` rewritten with Reading-order-for-agents + Cite-which-paper-for-what tables; add-paper workflow expanded from 7 to 8 steps with explicit master-bib registration as new step 5; not-archived footer reconciled into single canonical 4-row table.
- **`Residuality-Oreilly-2021-machine-in-the-ghost.{md,-summary.md,pdf}`**: NEW. Extraction (~7,360 words) and full summary for *The Machine in the Ghost: Autonomy, Hyperconnectivity, and Residual Causality*, *Philosophies* 6(4):81 (2021). The corpus's only non-Procedia journal piece; develops residual causality at journal length and reframes it as a threat to autonomy in hyperconnected society. mg downloaded the PDF manually after MDPI/Akamai blocked all automated fetches from this environment.
- **Repo workflow lesson recorded**: future paper additions must update master bib (`references/README.md`) — the gap that caused 2019 and 2022 to be missing for an unknown duration is now closed in the workflow.

### Emotional attention steering directory (2026-03-26)

- **`wild/emotional-attention-steering/`** — New directory with README.md, references.md, and 6sec-emotion-blend-chart.png. Research question: how to model emotional dynamics in committee deliberation via external PID control, and what scoring vocabulary the orchestrator needs. References cover Plutchik primary sources and algebraic formalizations, 6sec blend chart, computational emotion classification (Li et al. EMNLP 2024), and connections to furry logic.
- **`wild/diary/2026-03-15-emotional-attention-steering.md`** — Addendum on emotion blend vocabularies as scoring apparatus: Plutchik's Z₂ × Z₈ skeleton and 6sec's 5×5 blend matrix as measurement/scoring vocabulary feeding into PID loop (distinct from PID state variables). Drift detection via blend calibration.
- **`wild/README.md`** — Added "Emotion and Attention" subsection.

### ACT review and remediation of wild/fuzzy-type-theory (2026-03-22)

- **ACT-focused review completed**: `wild/fuzzy-type-theory/act-review-2026-03-22.md` — assessed shared-ancestor claim (sound), sibling-not-specialization (sound with caveats), measuring-coalgebra parallel (plausible but underspecified), magnitude connection (correctly flagged speculation). External references verified via web search.
- **10-change remediation executed**: quantale clarification, weighted-limit fix, Markov measurability note, §5c endofunctor rewrite (flagged as open question), authorship expansion to "North et al." (3 files), Set^M prominence elevated in §1, adoption triage adjusted (Set^M moved to adopt-now, dependent types deferral strengthened), notation glossary added to README.md, forward-reference in `palgebra/soft-type-theory.md`, worked example §5d (evidence type presheaf with full arithmetic, functoriality, confidence propagation, Chapman-Kolmogorov). All verified by independent consistency check.
- **Adoption triage updated**: "Adopt now" items now include Set^M enrichment design exploration and measuring-coalgebra research note (not yet produced). "Investigate" refocused on endofunctor existence question. "Defer" strengthened with revisit trigger for dependent types.

## Epistemic positions (recorded 2026-03-20)

Three positions recorded in `agent/onboarding-core.md` (section "Epistemic positions the agent must know"):

1. **Committee inspectability vs. decision quality**: The committee's load-bearing claim is inspectable reasoning records, not superior decisions. These are independent axes; the inspectability claim holds regardless of ablation results.
2. **Formal work is provisionally useful but untrusted**: palgebra, furry logic, and open games constructions are working hypotheses, not theorems. They need human expert review (hence the ACT outreach).
3. **LLM-steered mathematical inquiry**: The formal work is simultaneously subject matter and test case. A rough research program outline is in `wild/llm-mathematical-inquiry-outline.md`.

## Open decisions

- Whether to record rubric scores as persistent metadata beyond the current review artifacts.
- Whether `wild/potential-to-sense/` should be promoted to `essays/` (polished draft, strong connections to existing theory).
- Whether to add OpenCode to the multi-model committee research program as a Tier 2 platform candidate (per contributor issue #6).
- Whether multimodal inputs (images, diagrams) should be explored as a new research direction (per contributor issue #11).

## Active sprint

A refactoring sprint plan is at `agent/prompts/refactoring-sprint-2026-03.md`. It defines seven workstreams across two passes (core content first, then wild).

Pass 1 audit phase complete (2026-03-13). Reports:
- WS-1 editorial review: `agent/archive/editorial-review-report-2026-03.md` — all 7 dimensions score 2/3; 10-item remediation plan.
- WS-2 cross-reference audit: `agent/archive/cross-reference-audit-2026-03.md` — zero broken links; Bruner edit plan fully executed (9/9, verified 2026-03-16).
- WS-3 research program triage: `agent/archive/research-program-triage-2026-03.md` — all 8 programs relevant; ablation study and agent-independence ready to start.
- WS-7 rubric extensions: `agent/rubrics/repo-consistency.md` — draft of 5 new dimensions (internal consistency, currency, pipeline velocity, formal consistency, practical validation).

Pass 2 complete (2026-03-13). mg reviewed Pass 1 findings and approved remediation (directive: "don't reorder the essays"). Completed:
- WS-4 editorial remediation:
  - Character roster introduction added to `essays/README.md` (Note on the Committee Characters section).
  - Principles vs. Instantiations section added to `essays/05-the-synthesis.md`.
  - Pask forward reference resolved in `essays/05-the-synthesis.md` (Essay 11 callout).
  - Reading difficulty note added to theorist path in `essays/README.md`.
  - Concepts and Definitions index table (19 entries) added to `essays/README.md`.
  - Status and Evolution section rewritten with validated/theoretical/gaps distinction.
  - Societies of Thought arXiv DOI added to README entry.
- WS-5 wild triage: `agent/archive/wild-triage-2026-03.md` — 2 directories ready to promote (potential-to-sense, committee-games); 7 graduation-ready within 4 weeks; 4 remain active research; 1 superseded.
- WS-6 wild cleanup: Status notes added to all 12 wild subdirectory READMEs. Status indicators added to `wild/README.md` with triage report link.

Sprint status: **Complete**. Bruner edits 2/5/8 verified applied (2026-03-16). Remaining longer-term items (worked example, essay promotions from wild/) belong in future sprints.

### Post-sprint: categorical-structures.md focused review (2026-03-13)

`palgebra/categorical-structures.md` received a focused mathematical consistency review against the older palgebra documents. Review report: `agent/archive/categorical-structures-review-2026-03.md`. Key changes: lax/approximate coherence framing added (Mac Lane coherence doesn't hold strictly in stochastic pipelines); overclaimed universal properties weakened to design targets; category **Text** precisely defined; Kleisli and enriched category structures acknowledged; cross-references to committee-games open-game formalization and furry logic distributional types added. Also fixed monad composition direction bug in `palgebra/duality-and-composition.md` (was "Fan ∘ Funnel", should be "Funnel ∘ Fan").

## Scheduled reviews

- **2026-06-08 — Contributor gatekeeping changes**: Has anyone contributed to `wild/` or `wild/diary/`? Has the diary-to-wild-to-formalization pipeline worked for external contributors? Has the maintainer labor model held? Source: `meta/deliberations/contributor-gatekeeping/03-resolution.md`.

## Active research: Black Swan Hindsight Framework (Phase A)

**Status**: Phase A complete. **Result: DOES NOT PASS.** C2 does not reliably surface reframing insights absent from B1-ext on the tested scenarios.
**Results**: `research-programs/evaluating-deliberative-architectures/results/`
**Phase A report**: `results/phase-a-results.md`
**Prompt**: `agent/prompts/black-swan-first-run.md` (steps annotated with completion status)
**Deliberation records**: `research-programs/evaluating-deliberative-architectures/results/deliberations/`

- Pre-Gate 1 (contamination probes): ✅ Complete — all 3 historical case types pass.
- Pre-Gate 2 (scenario difficulty pilot): ✅ Complete — scoring reliable (10/10 agreement), but scenarios are easier than expected for frontier LLMs (only 1 of 5 at B1 ≤ 1). Two structural features were missed by both conditions, and the Deliberation-Neutral scenario discriminated in the expected inverse direction. The externally-sourced scenario (Intel FDIV) was recognized and needs replacement.
- Committee deliberation on proceed-or-revise: ✅ Complete (2026-03-16/17). Full fan→funnel→evaluation→remediation→re-evaluation cycle. Score: 10/15 → remediated → 13/15 (at bar). Decision: targeted revision with reassessment trigger.
- **Targeted revision (2026-03-20)**: ✅ Complete. Replaced externally-sourced scenario (Longford-derived, conditional contamination pass). Hardened Glenda/Crock and Cascading Mitigation. Re-piloted all three (6 runs, dual-scored). **Finding: hardening reduces B1 scores but NOT B1-ext scores.** Zero scenarios meet B1-ext ≤ 1. **Reassessment trigger activated.** The structural problem is that the B1-ext multi-angle prompt instructs the model to perform the exact analytical task the scoring system rewards.
- **Reassessment deliberation (2026-03-20)**: ✅ Complete. Committee reconvened, scored 13.5/15 (HIGH, no remediation needed). Unanimous decision: **pivot Phase A to Targeted Reframing Probe** — test whether C2 surfaces conceptual reframes (phasing critique, creation-vs-activity) that B1-ext completely misses. Key insight (Vic): B1-ext captures "deepening" but may miss "reframing." Phase A reclassified from Protocol Calibration to Targeted Reframing Probe. Scope reduced to 8 runs on 2 scenarios. Deliberation record: `research-programs/evaluating-deliberative-architectures/results/deliberations/black-swan-phase-a-reassessment/`.
- **Protocol amendment (2026-03-20)**: ✅ Complete. Section X-A added to protocol document. Phase A reclassified, run plan specified, three-level binary feature scoring defined, pass criterion formalized. Resolution ratified by user.
- **B1-ext replication (2026-03-20)**: ✅ Complete. 4 runs (2 × Blast Radius, 2 × Cascading Mitigation hardened). Feature 2 (creation-vs-activity) eliminated as discrimination target — B1-ext Run 3 scored "Present." Only Feature 1 (phasing critique) remained viable.
- **C2 runs (2026-03-20)**: ✅ Complete. 4 runs (2 × Blast Radius, 2 × Cascading Mitigation hardened). All dual-scored by Sonnet + Opus evaluators.
- **Phase A result (2026-03-20)**: ✅ **DOES NOT PASS.** C2's best score on Feature 1 is "Partially present" (Run 5); pass criterion requires "Present." C2 moved closer to the phasing critique than B1-ext (Partially present vs. Absent) but did not reliably complete the reframe. Feature 2 surfaced by both conditions (not discriminating). Full report: `results/phase-a-results.md`.

**Next steps for this research program**: Per protocol if-fail path — report the null result, proceed to Phase B (new scenarios with established discrimination) or document the null and pause. Decision pending.

### Committee decision summary (2026-03-17)

The committee's key insight (surfaced in the remediation round): **the comparison that matters is C2 vs. B1-ext, not C2 vs. B1.** B1-ext is the effort-matched control for token count. This changes:
- Difficulty criterion: B1-ext ≤ 1 (not B1 ≤ 1) — harder bar
- Re-pilot: B1 AND B1-ext on revised scenarios (6 runs, not 3)
- Go/no-go: reassessment trigger if zero scenarios score B1-ext ≤ 1 (replaces unconditional "proceed regardless")
- Portfolio framing: valid for Deliberation-Neutral only; ad hoc for other scenarios

**Next action**: Execute the implementation plan from `03-resolution.md`:
1. Construct replacement externally-sourced scenario (avoid Therac-25/Ariane 5; use obscure published case; cap 2 attempts)
2. Surgical hardening of Glenda/Crock and Cascading Mitigation
3. Re-pilot with B1 + B1-ext on 3 revised scenarios (6 runs, dual-scored)
4. Assess against B1-ext ≤ 1 criterion → reassessment trigger or proceed
5. If proceeding: B2, B3, C1, C2×2, C3 on all 5 scenarios; foreground C2 vs. B1-ext comparison

## Blocked or prerequisite-dependent items

- A full empirical failure case for `essays/when-methodology-fails.md` still depends on real practice data.
- Some evidence-building tasks in `research-programs/` still depend on running fresh situation-directory workflows rather than repo-local examples.
- ~~The Bruner-Kahneman diary entry 9-edit plan~~ — All 9 edits verified applied as of 2026-03-16. Item closed.

## Docs still needing sweep

- `project-state.md` itself should be updated after each sprint workstream completes. Last sweep: 2026-03-22.
- If this becomes stale, update this section rather than reintroducing a catch-all backlog file.
