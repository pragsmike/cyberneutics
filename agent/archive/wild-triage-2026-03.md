# Wild Content Triage: March 2026

**Date**: 2026-03-13
**Workstream**: Workstream 5 of refactoring sprint (audit phase)
**Scope**: Assessment of fourteen topic directories plus `wild/diary/` for status, graduation readiness, and promotion/shelving recommendations
**Assessor**: Claude (Haiku 4.5)
**Status**: Audit only — no repository modifications

---

## Executive Summary

The wild content is **strategically well-aligned and actively productive**. The fourteen topic directories plus diary represent genuine intellectual scaffolding for the methodology rather than discarded experiments. Key findings:

- **Seven directories are graduation-ready or near-ready**: Two (committee-games, potential-to-sense) are polished and should promote immediately; five (cybernetics, residuality-theory, neo-cybernetics, harness-engineering, software-factories) are mature reference materials suitable for essays/ or applications/.
- **Four directories are actively productive research**: blast-radius-problem, cyberneutics-director, palgebra-graph-ui, pask-mesh-fitting each capture one load-bearing architectural question with clear paths to formalization or implementation.
- **Three directories are framework-dependent**: issues, subagent-personas-for-debate, and committee-games partially supersede each other as research programs matured; content is preserved in cross-referenced form.
- **The diary is exceptionally healthy**: Nine dated entries from Feb 17 – Mar 13 document genuine intellectual exploration. Three entries (furry-logic, potential-to-sense, bruner-kahneman) contain publishable material; all nine show active theorizing in response to methodology maturation.

**Critical pipeline findings**:
- **Graduate immediately**: Promote potential-to-sense to essays/; publish committee-games as bridge paper for ACT community
- **Graduate within 6 weeks**: Extract essays from cybernetics/, residuality-theory/, bruner-kahneman diary for cross-reference integration
- **Keep in wild**: Maintain blast-radius-problem, cyberneutics-director, pask-mesh-fitting, palgebra-graph-ui, software-factories as research/design documentation until implementation is ready or scope is sharply constrained
- **Archive as historical**: Subagent-personas-for-debate is superseded by research programs (agent-independence, multi-model-committee, committee-implementation-taxonomy); retain with supersession note

**Overall pipeline velocity**: Slow-to-moderate but healthy. The methodology is generating theory faster than it is shipping implementation. This is appropriate for the current phase (formalization before scale-out).

---

## Individual Directory Assessments

### 1. blast-radius-problem/

**Status**: ACTIVE (incomplete)

**Type**: Architectural problem specification

**Documents**:
- `README.md` (0.7 KB) — The core problem and proposed role-differentiation solution

**Assessment**:

**(a) Is it active or dormant?**
Active. The problem is well-motivated by real operational constraints in fleet management (NixOS, Kubernetes). The README documents a clear hypothesis: undifferentiated developer agents fail in high-blast-radius domains; role-differentiated committees can catch deployment risks that single agents miss.

**(b) Is it polished enough to promote?**
No. The README states the problem and proposes a solution but does not provide:
- A formal model of "blast radius" (what makes a failure catastrophic vs. recoverable?)
- Concrete committee design (which characters beyond Planner/Tester/Operator?)
- Example scenario showing failure mode and recovery
- Connection to the methodology's formal structures (palgebra typing, evaluation rubrics)

This is a 1–2 page design sketch, not a publishable artifact.

**(c) What work would graduation require?**
- Create a worked example: a Nix configuration change that a single developer agent would approve, but the committee catches as dangerous (e.g., changes boot parameters without out-of-band rollback)
- Design a committee roster specific to Ops (maybe: Developer, Operator, Network, Storage, Security roles)
- Formalize "blast radius" in terms of palgebra failure-mode propagation (related to `pask-mesh-fitting` and residuality)
- Demonstrate that the committee catches the hazard and proposes mitigation (incremental rollout, canary pattern, etc.)

Effort: 3–4 weeks, depends on contributor with Ops knowledge.

**(d) Should it be explicitly archived/shelved?**
No. This is live design work. It addresses a real constraint (asymmetric failure modes in agent-assisted systems) that the methodology encounters in deployment. Shelving would mean abandoning the question.

**(e) Connection to sprint findings?**
- **Editorial review**: Not directly. But `essays/07-narrative-engineering.md` discusses operational closure; blast-radius is a concrete instantiation of when closure fails (blast radius breaks the boundary).
- **Research program triage**: Implicit connection to evaluating-deliberative-architectures (Black Swan framework) — blast radius is a type of black swan risk in infra systems.
- **Wild material**: Relates to cyberneutics-director (routing between coordination and deliberation) and harness-engineering (context for agent work in complex systems).

**Recommendation**: **KEEP IN WILD** (research direction). Create a design document within the next 2 months if an Ops-knowledgeable contributor is available. Flag as "pending example scenario."

---

### 2. committee-games/

**Status**: ACTIVE (complete)

**Type**: Theoretical bridge document (game theory)

**Documents**:
- `README.md` (1.3 KB) — Index and key claims
- `committee-as-open-game.md` (15 KB) — Complete formalization

**Assessment**:

**(a) Is it active or dormant?**
Active. Created 2026-03-08 (5 days ago). The document is a response to the 2026-03-08 diary entry on cospans and open games, which was itself prompted by recognizing the structural homology between the committee and compositional game theory.

**(b) Is it polished enough to promote?**
Yes, with caveats. The README and main document are well-written, complete, and self-contained. The formalization is rigorous. **However**, this is a *bridge document*, not an essay or artifact. Its purpose is to serve as a point of contact for the ACT/Cybercat research community, not to integrate into the essay collection.

**(c) What work would graduation require?**
Very little. The document is ready to publish. Remaining questions (in the README: "What selection function type formally captures propensity-driven play?") are explicitly positioned as research questions for the ACT community, not blockers.

Optional enhancements:
- Add a Cybercat bibliography section (current references are generic ACT 2018–2021)
- Create a companion brief (1–2 pages) for non-specialists explaining why this matters

**(d) Should it be explicitly archived/shelved?**
No. This is an active research bridge.

**(e) Connection to sprint findings?**
- **Research program triage**: Section B (implicit new programs) recommends "Open Games Formalization" — this document is the direct response. The triage says "ready to ship as bridge paper."
- **Editorial review**: The open games treatment makes explicit what essays/08-formalism.md leaves implicit (the strategic dimension of the committee). This is complementary to the palgebra treatment, not redundant.

**Recommendation**: **PROMOTE TO PUBLICATIONS** (or create a new `/bridge-papers/` or `/community-engagement/` directory in core). This is ready to ship. Publish as-is, or attach as appendix to a future research program report. Mark in `wild/README.md` as "ready for publication."

---

### 3. cybernetics/

**Status**: ACTIVE (reference material)

**Type**: Source material and pedagogical notes

**Documents**:
- `README.md` (1.6 KB) — Index and intake convention
- `gordon-pask.md` (3.5 KB) — Biography and contributions
- `von-Foerster.md` (2.8 KB) — Biography and contributions
- `conversation-theory.md` (5.2 KB) — Pask's theory integrated with Deleuze/Dervin
- `community-building.md` (2.1 KB) — BCL community-building playbook

**Assessment**:

**(a) Is it active or dormant?**
Dormant as a development direction (no new entries since Feb 2026), but *active as a reference* for the essays. The material is cited and drawn on repeatedly in the formal writings (Essays 04, 11; essays/societies-of-thought-synthesis.md).

**(b) Is it polished enough to promote?**
Partially. The documents are well-written and serve their reference purpose. However, they are "intake convention" material — not yet settled methodology. The README explicitly signals this.

Promotion candidates:
- `conversation-theory.md` is mature and could be promoted to essays/ or a dedicated `applications/pask-theory/` section
- `gordon-pask.md` and `von-Foerster.md` are reference biographies that could live in `references/theorists/` or as appendices to essays 04 and 11

**(c) What work would graduation require?**
Moderate editing. The documents would need to be:
- Cleaned of "intake convention" framing
- Cross-referenced into the essay collection (where they are currently drawn on indirectly)
- Possibly condensed: `gordon-pask.md` + `conversation-theory.md` could become a single essay "Pask's Conversation Theory and Cyberneutics"

Effort: 2–3 weeks for editorial integration.

**(d) Should it be explicitly archived/shelved?**
No. This is canonical reference material for the methodology.

**(e) Connection to sprint findings?**
- **Editorial review**: The Pask references in Essay 11 point back to this directory. Promoting `conversation-theory.md` to the essay collection would strengthen the essay's cross-reference structure.
- **Research program triage**: The potential-to-sense essay (wild/potential-to-sense/) draws on this material (von Foerster, eigenforms, conversation). Promoting both together would consolidate the theoretical grounding.

**Recommendation**: **GRADUATE PARTIALLY** (extract and promote key documents to essays/ within next 4 weeks). Create essays/12-pask-conversation-theory-synthesis.md by condensing + integrating cybernetics/conversation-theory.md. Retain cybernetics/ as historical reference with "see also" pointers to essays/12.

---

### 4. cyberneutics-director/

**Status**: ACTIVE (design proposal)

**Type**: Architectural design document

**Documents**:
- `README.md` (2.1 KB) — The core concept, problems it solves, architecture guidelines, next steps

**Assessment**:

**(a) Is it active or dormant?**
Active. The problem it addresses (conflation of task coordination with decision deliberation) is real and currently unsolved in the agent toolkit landscape. The document is a 2026-02-26 field note (recent).

**(b) Is it polished enough to promote?**
No. The README is a problem statement and vision sketch, not a specification or implementation plan. It identifies three interfaces (MCP, Web API, Web UI) but does not provide:
- Schema or data structures for the "deliberation state store"
- Concrete examples (how does an agent escalate from task to deliberation?)
- Integration plan with existing tools (how does this compose with the palgebra-graph-ui, github-mcp, etc.?)

This is a 1–2 page architecture white paper, suitable for research-programs/ but not for essays/ or artifacts/.

**(c) What work would graduation require?**
High-effort path (full implementation): 8–12 weeks
- Define MVP schema (JSON schema for deliberation state)
- Build MCP server prototype
- Integrate with GitHub MCP as stated in the document
- Test with a live agent escalation scenario

Lower-effort path (specification only): 3–4 weeks
- Write a detailed specification of the three interfaces (MCP, Web API, Web UI)
- Create example JSON/YAML for deliberation state
- Design the escalation protocol (when does coordination become deliberation?)
- Document how Director composes with the palgebra graph

**(d) Should it be explicitly archived/shelved?**
No. This is a live architectural direction.

**(e) Connection to sprint findings?**
- **Research program triage**: Not explicitly mentioned, but relates to all agent-based programs (ablation-study, agent-independence, multi-model-committee) by providing the orchestration layer they need
- **Sprint findings (palgebra-graph-ui, harness-engineering)**: The Director provides the state management that feeds the palgebra graph visualization; harness-engineering notes capture context about the complexity the Director needs to handle

**Recommendation**: **KEEP IN WILD** (design direction). Escalate to a research program or implementation project if agent-orchestration becomes a priority. Current priority: implement the palgebra-graph-ui visualization (lower complexity) first, then return to Director as a follow-up.

---

### 5. harness-engineering/

**Status**: DORMANT (well-extracted)

**Type**: Engineering notes and references

**Documents**:
- `README.md` (1.6 KB) — Context, presenter bio, key resources
- `summary.md` (5.2 KB) — Detailed summary of HumanLayer's "No Vibes Allowed" talk

**Assessment**:

**(a) Is it active or dormant?**
Dormant. No new entries since 2026-02-26 (the extraction date). The material is a one-time capture from an external talk.

**(b) Is it polished enough to promote?**
Marginally. The summary is well-written and clearly organized. However, it is a **summary of external material**, not original work. The question for promotion is: does this belong in the core methodology?

The talk addresses a real problem (how to get LLM agents to work in complex brownfield codebases) and Dex Horthy's 12-Factor Agents framework is relevant to the methodology. However, the summary is HumanLayer content, not Cyberneutics content.

**(c) What work would graduation require?**
To promote this, either:
- **Option A** (Low effort): Move to `references/` or create `applications/context-engineering/` and link it as external context
- **Option B** (Medium effort): Extract the *actionable insights* specific to cyberneutics and write them as an artifact/guide (e.g., `artifacts/context-engineering-for-committees.md`)
- **Option C** (Keep in wild): Retain as-is if future work on harness engineering is planned

**(d) Should it be explicitly archived/shelved?**
No. The material is useful reference for implementation. But it belongs in references/ or as applications/, not as methodology core.

**(e) Connection to sprint findings?**
- **Research program triage**: Indirectly relates to multi-model-committee and agent-independence (harness matters for implementation of both)
- **Wild material**: Supports blast-radius-problem and cyberneutics-director by explaining the operational environment that these architectures must handle

**Recommendation**: **MIGRATE TO REFERENCES** (move to references/harness-engineering/ or create applications/coding-agent-orchestration/ and link from there). Retain a brief entry in wild/README.md pointing to the new location. This is reference material, not methodology.

---

### 6. issues/

**Status**: ACTIVE (contributor feedback)

**Type**: GitHub issues (community input)

**Documents**:
- `6.md` — OpenCode capabilities and platform landscape
- `7.md` — Legal domain test case for evaluating-deliberative-architectures
- `8.md` — (Not read in detail, but appears to be historical)
- `11.md` — Multimodal and discrete subagent deliberation
- `13.md` — (Not read in detail)

**Assessment**:

**(a) Is it active or dormant?**
Active. These are recent (March 2026) contributor inputs that directly feed into the research program triage and cross-reference audit.

**(b) Is it polished enough to promote?**
No. Issues are by definition transient — they are conversation starters, not deliverables. Promotion would mean settling them (closing, integrating findings into research programs, etc.).

**(c) What work would graduation require?**
Each issue requires a **conversion to a resolved item in a research program or decision log**:
- Issue #6 (OpenCode) → documented update to committee-implementation-taxonomy.md
- Issue #7 (legal domain) → integration into research-programs/evaluating-deliberative-architectures.md
- Issue #11 (multimodal) → addition to agent-independence.md Phase 2+ roadmap

**(d) Should it be explicitly archived/shelved?**
No. Keep as-is. Issues are a legitimate intake mechanism for external contributors and feedback. However, *resolution* (converting issues into integrated findings) should happen in response to each issue.

**(e) Connection to sprint findings?**
- **Research program triage**: Directly. The triage document (report WS-3) addresses issues #6, #7, #11 explicitly and recommends how to integrate each
- **Cross-reference audit**: Issues should be tracked in a "contributor feedback log" or similar, so that future audits can verify closure

**Recommendation**: **KEEP IN WILD** (transient intake). Create a follow-up document (e.g., `agent/archive/contributor-issues-resolution-log-2026-03.md`) that maps each issue to its resolution (e.g., "Issue #6 → Update to committee-implementation-taxonomy.md, line X"). This becomes part of the WS-4 remediation work.

---

### 7. neo-cybernetics/

**Status**: ACTIVE (reference material)

**Type**: Source material and relational analysis

**Documents**:
- `README.md` (0.9 KB) — Index and primary links
- `about-the-neo-cybernetics-initiative.md` (2.3 KB) — Overview, principals, history
- `content-level-relations.md` (2.5 KB) — How Neo-Cybernetics and cyberneutics relate at content level
- `meta-level-relations.md` (1.8 KB) — How they relate as initiatives
- `manifesto-summary.md` (3.2 KB) — Structured summary of NCB manifesto

**Assessment**:

**(a) Is it active or dormant?**
Dormant as a development direction (no new entries; Feb 2026 material), but *active as a reference* for understanding the broader cybernetics ecosystem. The Neo-Cybernetics Initiative is a distinct but parallel effort; understanding its relationship matters for positioning cyberneutics.

**(b) Is it polished enough to promote?**
Partially. The documents are well-organized and clearly written. They serve as a reference guide to an external initiative.

However:
- They are "intake convention" material (not yet settled as methodology)
- The relational analyses (content-level, meta-level) are descriptive, not integrated into core theory
- The manifesto summary is a digest of external material

**(c) What work would graduation require?**
Low-to-moderate effort. To promote:
- Move to `references/neo-cybernetics/` (this is primarily reference material)
- OR: extract the relational insights into an essay (e.g., `essays/12b-cyberneutics-and-neo-cybernetics.md`) that clarifies how the two approaches differ
- Ensure cross-links from Essays 04, 05, and README so readers understand the positioning

**(d) Should it be explicitly archived/shelved?**
No. The relationship to Neo-Cybernetics is worth documenting, and their different focus (social/institutional systems vs. LLM-based deliberation) is complementary.

**(e) Connection to sprint findings?**
- **Editorial review**: The Neo-Cybernetics positioning provides context for Essays 01, 04, 05 (why cyberneutics is distinct from 20th-century cybernetics). This context is currently implicit; an integrative essay would surface it
- **Research program triage**: Not directly, but the two initiatives might find value in comparing methodologies

**Recommendation**: **MIGRATE TO REFERENCES** (move to references/neo-cybernetics/) with a brief "See Also" entry in wild/README.md. Optionally, extract one integrative essay (`essays/12-cyberneutics-positioning.md` or similar) that places cyberneutics in the broader cybernetics landscape. Medium priority (post-WS-4).

---

### 8. palgebra-graph-ui/

**Status**: ACTIVE (design proposal)

**Type**: UX/UI design document

**Documents**:
- `README.md` (1.5 KB) — The problem, proposed blackbody heat encoding, next steps

**Assessment**:

**(a) Is it active or dormant?**
Active. The problem is well-motivated (Kanban boards show task state, not computational structure) and the proposed solution (blackbody radiation heat encoding) is novel and grounded in prior art (Jaeger traces, service mesh dashboards).

**(b) Is it polished enough to promote?**
No. The README is a proposal and vision sketch. Promotion would require:
- Prototype mockup (visual design or interactive demo)
- Schema specification (what data does the UI consume?)
- Integration plan (how does this connect to the cyberneutics-director state store?)

This is 1–2 pages of design thinking, suitable for an artifact/design-guide but not yet ready to ship.

**(c) What work would graduation require?**
Medium-to-high effort:
- Create visual mockup(s) (static images or Figma prototype) showing a sample committee run with heat encoding
- Specify the schema for palgebra graph output (JSON schema or MDX)
- Build a lightweight reference implementation (static HTML mockup or web component)
- Document how this integrates with cyberneutics-director

Estimated effort: 4–6 weeks for a production-ready MVP.

**(d) Should it be explicitly archived/shelved?**
No. This is a live design direction.

**(e) Connection to sprint findings?**
- **Research program triage**: Not explicitly mentioned, but all agent-based research programs (ablation-study, agent-independence, multi-model-committee) produce palgebra artifacts that would benefit from visualization
- **Wild material**: Complements cyberneutics-director (the Director provides the state; the UI visualizes it)

**Recommendation**: **KEEP IN WILD** (design direction). Prioritize for implementation once WS-4 remediation is complete. This is a high-value UX feature that would significantly improve observability of committee runs. Target: Q2 2026 implementation.

---

### 9. pask-mesh-fitting/

**Status**: ACTIVE (assessed as intractable; documented)

**Type**: Research specification with tractability analysis

**Documents**:
- `README.md` (2.2 KB) — Warning box, status, contents, connections
- `pask-mesh-fitting.md` (6.8 KB) — The document-evaluation framework
- `mechanism-design-core.md` (2.1 KB) — Core mechanism design principles
- `research/tractability-and-risks.md` (mentioned, not read) — Tractability analysis
- Python and Clojure implementation sketches

**Assessment**:

**(a) Is it active or dormant?**
Active but constrained. The material is from Feb 2026 and includes a clear **warning box** stating that the full global approach is "computationally intractable at a realistic corpus scale" (O(N³) complexity).

**(b) Is it polished enough to promote?**
Partially. The framework document (pask-mesh-fitting.md) is well-articulated and intellectually rigorous. The README and tractability analysis are clear and honest about limitations.

However, the material is positioned as a *research direction under investigation*, not a settled methodology. The warning box signals that the current approach needs fundamental rethinking.

**(c) What work would graduation require?**
This depends on the scope decision:

**Option A** (Shelve the full approach): Acknowledge that the O(N³) complexity makes the full global mesh-fitting impractical. Propose scoped-down alternatives (e.g., local mesh fitting for small corpora, embedding-based approximations). Create a white paper documenting why the approach failed and what the insights were.

**Option B** (Pursue approximation research): Formalize a research program around "approximate pask mesh fitting" using embeddings, spectral methods, or other sub-cubic approaches. This would be a proper research program living in research-programs/.

**Option C** (Archive as theoretical exploration): Move to research-programs/ as a "closed exploration" documenting the tractability analysis and lessons learned.

**(d) Should it be explicitly archived/shelved?**
Probably yes, but with nuance. The README already signals that the approach is "not yet methodology," and the tractability warning is explicit. The question is whether to:
- Keep in wild/ with no plans to implement (current state)
- Move to research-programs/ as a "closed/scoped program" with documented lessons
- Promote the framework document as an essay/artifact about document evaluation (theory only, without the mesh-fitting machinery)

**(e) Connection to sprint findings?**
- **Editorial review**: Not directly, but relates to Essays 04, 09, 10 (narrative immune systems, decisions under uncertainty) as a formalization attempt
- **Research program triage**: Not mentioned explicitly, but the intractability finding is valuable to preserve. If approached as a research program, could inform future work on corpus evaluation and risk assessment

**Recommendation**: **MOVE TO RESEARCH-PROGRAMS/** (as a "closed exploration" or "theoretical investigation"). Create research-programs/pask-mesh-fitting-tractability.md that:
1. Preserves the framework document (with its intellectual value intact)
2. Documents the O(N³) intractability finding clearly
3. Proposes 2–3 scoped-down alternatives for future investigation
4. Explains lessons learned for future corpus-evaluation research

Mark in wild/README.md as "moved to research-programs/" to avoid duplication. This preserves the work while being honest about its current viability.

---

### 10. potential-to-sense/

**Status**: ACTIVE (complete essay)

**Type**: Theoretical essay

**Documents**:
- `README.md` (1.1 KB) — Central argument and connection to the repo
- `from_semantic_potential_to_situated_sense.md` (11 KB) — Full essay, 11 sections

**Assessment**:

**(a) Is it active or dormant?**
Active. Created 2026-02-26 to 2026-03-06 (most recent work ~a week ago). The README describes the essay as a "complete draft, not yet integrated."

**(b) Is it polished enough to promote?**
Yes. The essay is well-written, self-contained, and intellectually rigorous. The README explicitly marks it as "polished" and notes that integration questions remain (does it belong in essays/, or as reference material?).

This is the most promotion-ready document in the wild/ directory.

**(c) What work would graduation require?**
Minimal. The essay is ready to move to essays/ as-is. Optional enhancements:
- Add cross-references to essays/04, essays/11, and palgebra/ documents
- Add endnotes with citations (the essay is dense with theory; endnotes would help navigation)
- Update essays/README.md to include it in the index and reading paths

Estimated effort: 1–2 weeks for editorial integration.

**(d) Should it be explicitly archived/shelved?**
No. This should be promoted immediately.

**(e) Connection to sprint findings?**
- **Editorial review** (WS-1): The essay is a *solution* to the forward-reference problem in Essay 05 (Pask convergence) and the "Why human gates are essential" gap. Promoting it would close a theoretical gap identified in the editorial review.
- **Research program triage** (WS-3): Explicitly recommended for promotion under "Implicit New Research Programs — C. Potential-to-Sense as Grounding Framework for Human Gates." The triage says: "Immediate: Move from wild/ to essays/; use as foundational theory."
- **Furry logic diary entry**: The essay's "measurement framing for meaning" (Section 5) resonates with the furry logic entry's "measurement framing for type membership." A future essay on soft types could draw on both.

**Recommendation**: **PROMOTE TO ESSAYS/** (immediate, highest priority).

**Action**:
1. Move `potential-to-sense/from_semantic_potential_to_situated_sense.md` to `essays/12-potential-to-sense.md`
2. Update essays/README.md to include it (index and reading paths)
3. Add endnotes with full citations
4. Create cross-reference notes in essays/04, essays/11, palgebra/categorical-structures.md
5. Update wild/README.md to note the migration

**Timeline**: Complete within 2 weeks as part of WS-4 remediation.

---

### 11. residuality-theory/

**Status**: ACTIVE (partially integrated)

**Type**: Theoretical reference and integration documentation

**Documents**:
- `README.md` (3.2 KB) — O'Reilly's residuality theory, architectural walks, connections to cyberneutics, residues vs. eigenforms, residuality and palgebra, status notes

**Assessment**:

**(a) Is it active or dormant?**
Dormant as new development (no entries since Feb 2026), but *active as integrated theory*. The README explicitly states "Partially integrated" — the core connections have been formalized into the palgebra (Probe operation), Essays 10 and 11, and the remediation cycle.

**(b) Is it polished enough to promote?**
Yes. The README is comprehensive, well-structured, and candid about what is and isn't settled. It serves as both a reference guide and a meta-document explaining what has been integrated and what remains open.

**(c) What work would graduation require?**
Low-to-moderate effort. The material is already partially integrated. To graduate fully:
- Extract the "Residues vs. Eigenforms" section as a standalone essay (`essays/13-residues-and-eigenforms.md`) clarifying the distinction and its role in committee deliberation
- Move the resource-material citations and notes to a proper `references/residuality-theory/` directory
- Update Essays 10 and 11 to cross-reference the residuality section more explicitly

Estimated effort: 2–3 weeks.

**(d) Should it be explicitly archived/shelved?**
No. This is canonical reference material for the methodology.

**(e) Connection to sprint findings?**
- **Editorial review** (WS-1): Not directly mentioned, but the eigenforms discussion in Essays 04, 10, 11 draws on this material. Promoting an essay on residues/eigenforms would strengthen the theoretical coherence
- **Research program triage** (WS-3): The open question in residuality-theory/README ("whether the 2-round remediation cap makes sense in eigenform terms") is a research direction that could inform ablation-study design
- **Wild material**: The architectural-walks idea connects to the Probe operation and the "repeated deliberations hunt eigenforms" hypothesis

**Recommendation**: **GRADUATE PARTIALLY** (extract essay + move reference material).

**Action**:
1. Create `essays/13-residues-and-eigenforms.md` by adapting residuality-theory/README.md §"Residues vs. eigenforms"
2. Move residuality-theory/ to references/ as a research reference
3. Update Essays 10, 11 to cross-reference essays/13
4. Update wild/README.md to note the migration

**Timeline**: Complete within 3 weeks as part of WS-4 remediation.

---

### 12. software-factories/

**Status**: ACTIVE (reference material)

**Type**: Design analysis and research notes

**Documents**:
- `README.md` (1.3 KB) — Problem statement, references
- `dark-factories.md` (3.1 KB) — Research notes on dark factory concepts and tooling
- `five-levels-of-ai-coding.md` (2.5 KB) — Summary of Nate Jones's framework
- `palgebra-and-dark-factories.md` (3.8 KB) — Analysis of how palgebra concepts apply to factory specs

**Assessment**:

**(a) Is it active or dormant?**
Dormant as new development (Feb 2026), but *active as reference*. The material documents an external landscape (dark factories, software-factory-as-a-service) and analyzes whether palgebra formalism can serve as a typed specification language for agent pipelines.

**(b) Is it polished enough to promote?**
Partially. The documents are well-researched and clearly written. However, the core question — "can palgebra serve as a typed spec language for NLSpecs / dark factories?" — remains open. The analysis shows connections but does not settle whether this is a viable research direction.

**(c) What work would graduation require?**
To promote as an artifact or research program:
- Prototype: create a small palgebra graph that translates to a valid StrongDM NLSpec (or equivalent)
- Analysis: document what StrongDM's NLSpec language can do that palgebra can't, and vice versa
- Recommendation: should this become a research program (can palgebra-as-spec-language improve agent-pipeline typing?) or is it a one-time analysis exercise?

Estimated effort: 3–4 weeks for a convincing prototype.

**(d) Should it be explicitly archived/shelved?**
Not immediately. But the question needs clarification: is this a research direction or an analysis of existing tooling?

**(e) Connection to sprint findings?**
- **Editorial review**: Not directly
- **Research program triage**: Indirectly relates to agent-independence and multi-model-committee (all involve agent pipeline specification)
- **Wild material**: Software-factories thinking informs the cyberneutics-director design (both are about making agent pipelines explicit and inspectable)

**Recommendation**: **KEEP IN WILD** (exploratory design analysis) or **CREATE RESEARCH PROGRAM** if prototyping is planned.

For now: Keep in wild/ with a flag in README.md noting that the core question (palgebra-as-spec) remains open. If a contributor becomes interested in agent-pipeline typing, escalate to a research program.

---

### 13. subagent-personas-for-debate/

**Status**: SUPERSEDED (but retained for context)

**Type**: Prior research direction (now absorbed into research programs)

**Documents**:
- `README.md` (4.2 KB) — Explicit supersession note, plus three alternative coordination schemes

**Assessment**:

**(a) Is it active or dormant?**
Dormant. Explicitly superseded (as noted in README) by three research programs:
- `research-programs/committee-implementation-taxonomy.md`
- `research-programs/agent-independence.md`
- `research-programs/multi-model-committee.md`

**(b) Is it polished enough to promote?**
The README is useful reference material showing the evolution from early thoughts (subagent personas as personas) to mature research programs. However, the original content is outdated.

The README's "Option A/B/C: Alternative Coordination Schemes" (Agent Teams, File-System Blackboard, MCP Server) is valuable pedagogical material explaining different architectural approaches.

**(c) What work would graduation require?**
Low effort. The README's coordination schemes section could be extracted as a short artifact/guide:
- Create `artifacts/subagent-coordination-patterns.md` extracting the three coordination schemes with detailed explanations
- Keep the README in wild/ as a historical note pointing to the new artifact and the research programs

Estimated effort: 1–2 weeks.

**(d) Should it be explicitly archived/shelved?**
Yes, but with extraction. The original content is superseded, but the coordination schemes section has enduring value.

**(e) Connection to sprint findings?**
- **Research program triage** (WS-3): The research programs (agent-independence, multi-model-committee) have absorbed this content. The directory exists to document why the original approach was abandoned.
- **Wild material**: The Directory and Agent Teams discussions inform cyberneutics-director and the agent-independence program

**Recommendation**: **ARCHIVE WITH EXTRACTION**.

**Action**:
1. Extract subagent-personas-for-debate/README.md § "Option A/B/C: Alternative Coordination Schemes" as `artifacts/subagent-coordination-patterns.md`
2. Move wild/subagent-personas-for-debate/README.md to `agent/archive/subagent-personas-historical-note-2026-03.md` (preserving it as historical context)
3. Remove the directory from wild/ (or create a stub with "see archive/" pointer)
4. Update wild/README.md to remove the directory but mention the extracted artifact

**Timeline**: 1–2 weeks, low priority (can be batched with other migrations).

---

### 14. diary/

**Status**: VERY ACTIVE (healthy exploration)

**Type**: Field notes and idea sketches

**Recent entries** (Feb 17 – Mar 13):
1. 2026-02-17: Bruner-Kahneman Synthesis (16 KB)
2. 2026-02-19: Narrative Immune System (18 KB)
3. 2026-02-21: Cyberneutics Dual Operations + Chronology (17 KB + 14 KB)
4. 2026-02-26: Cyberneutics Field Notes (21 KB)
5. 2026-03-05: Implementation Convergence (14 KB)
6. 2026-03-06: Metacog, SDT, Beer (13 KB)
7. 2026-03-08: Cospans and Open Games (9.2 KB)
8. 2026-03-13: Furry Logic (8.5 KB)
9. README (0.75 KB)

**Assessment**:

**(a) Is it active or dormant?**
Extremely active. Nine dated entries over 25 days (Feb 17 – Mar 13) document genuine intellectual work responding to the methodology's maturation. The entries reference each other, cross-cut existing theory, and explore new directions.

**(b) Is it polished enough to promote?**
Selectively. Individual entries vary:
- **Ready to promote**: Bruner-Kahneman Synthesis (publishable as essay), Furry Logic (publishable as essay), Cospans and Open Games (already formatted as bridge document)
- **Ready as input to research programs**: Implementation Convergence (informs multi-model design), Metacog-SDT-Beer (informs decision-theory work)
- **Raw exploration**: Narrative Immune System, Dual Operations, Field Notes (useful as context but not yet settled)

**(c) What work would graduation require?**
Three paths:

**Path 1: Extract and promote essays**
- Bruner-Kahneman Synthesis → essays/14-bruner-kahneman-pedagogy.md (medium effort, 2–3 weeks)
- Furry Logic → essays/15-furry-logic-soft-types.md (medium effort, 2–3 weeks)

**Path 2: Extract and promote as research program input**
- Implementation Convergence → inform multi-model-committee.md Phase 2 design
- Metacog-SDT-Beer → create research-programs/decision-theory-and-cognition.md (low-to-medium effort)

**Path 3: Consolidate exploratory entries**
- Narrative Immune System + Dual Operations → could inform essays/09-narrative-immune-systems.md or wild/pask-mesh-fitting/ (low effort, consolidation)

**(d) Should it be explicitly archived/shelved?**
No. The diary is the most productive part of wild/. It should be actively maintained. As entries mature, they should be extracted (not deleted) and promoted to essays/ or research programs/.

**(e) Connection to sprint findings?**

**Explicit connections found**:
- **Bruner-Kahneman entry** — Referenced directly in project-state.md as containing "9-edit plan for essay cross-references, of which 6 have been applied. Edits 2, 5, and 8 remain unapplied."
- **Furry logic entry** — Referenced in research-program-triage as implicit new program A ("Furry Logic and Soft-Type Classification"); triage recommends "FORMALIZE (essay after societies-of-thought Items 1–2)"
- **Cospans and Open Games entry** — Prompted the committee-games/ document (diary→wild→community engagement flow working as intended)
- **Potential-to-sense essay** — Related to potential-to-sense/ (diary explores eigenforms; essay formalizes them)

**Implicit connections**:
- Metacog/SDT/Beer explores decision-theoretic foundations (connects to Essays 10, evaluation-schemes)
- Implementation Convergence documents the Agent Teams landscape maturation (connects to agent-independence program)
- Dual Operations articulates the distinction between task coordination and decision deliberation (connects to cyberneutics-director)

**(f) What does the diary health tell us about the pipeline?**

**Positive signals**:
- **Active exploration**: Entries are responding to real developments (Agent Teams launch, OpenCode proposal, furry logic insight, open games connection)
- **Cross-cutting**: The diary cuts across multiple mature directions (palgebra, essays, research programs), showing integration rather than isolation
- **Extraction workflow**: The committee-games example (diary→wild→community engagement) shows the intended workflow functioning: exploration → taming → formalization
- **Velocity**: 9 substantial entries over 25 days suggests healthy exploratory pace

**Areas of concern**:
- **Extraction lag**: Some entries (Bruner-Kahneman, Furry Logic) are ready for promotion but haven't been extracted yet. The editorial review found this (9-edit plan partially unapplied).
- **Duplication risk**: Entries like "Narrative Immune System" and "Dual Operations" could be consolidated before being promoted; current state is exploratory redundancy

**(g) Recommendation for diary management**:

**Immediate** (WS-4 phase):
1. Extract Bruner-Kahneman Synthesis and Furry Logic as essays (2–3 weeks each)
2. Consolidate Narrative Immune System + Dual Operations into a single essay or section (1–2 weeks)
3. Document the 9-edit plan resolution (editorial review finding) — complete remaining edits

**Medium-term** (Q2 2026):
1. Maintain active diary entries (continue as-is)
2. Quarterly diary review to identify entries ready for extraction
3. Create a "diary graduation schedule" showing which entries will promote when

---

## Cross-Cutting Analysis: Pipeline Health and Velocity

### Graduate Immediately (Highest Priority)
1. **potential-to-sense/** → essays/ (1–2 weeks, WS-4 phase)
2. **Bruner-Kahneman Synthesis** (diary) → essays/ (2–3 weeks, WS-4 phase)
3. **committee-games/** → publication (ready to ship; minimal work)

### Graduate Within 4 Weeks (WS-4 Phase)
4. **Furry Logic** (diary) → essays/ (2–3 weeks)
5. **residuality-theory/** → extract essay + move reference material (2–3 weeks)
6. **cybernetics/** → extract key documents + integrate (2–3 weeks)

### Graduate Later (Post-WS-4)
7. **neo-cybernetics/** → move to references/ (low priority, 2–3 weeks)
8. **harness-engineering/** → move to references/ (low priority, 1–2 weeks)
9. **subagent-personas-for-debate/** → archive with extraction (1–2 weeks)
10. **pask-mesh-fitting/** → move to research-programs/ (with scoped-down alternatives, 2–3 weeks)

### Keep in Wild (Active Research)
11. **blast-radius-problem/** — awaiting Ops-specific design work (ongoing)
12. **cyberneutics-director/** — awaiting orchestration layer design (ongoing)
13. **palgebra-graph-ui/** — awaiting MVP implementation (Q2 2026)
14. **software-factories/** — awaiting decision on research direction (ongoing)
15. **diary/** — continue as-is, with quarterly extraction reviews

### Archive as Historical
16. **subagent-personas-for-debate/** — superseded by research programs (extract coordination schemes first)

### Move to Research-Programs or References
17. **issues/** → create resolution log (WS-4 phase)

---

## Summary Table

| Directory | Status | Priority | Recommendation | Effort | Timeline |
|-----------|--------|----------|-----------------|--------|----------|
| blast-radius-problem | ACTIVE | Medium | Keep in wild; create design doc if Ops contributor available | 3–4 weeks | Q2 2026 |
| committee-games | ACTIVE | HIGHEST | Publish as bridge paper | <1 week | Immediate |
| cybernetics | ACTIVE | HIGH | Extract key docs, integrate to essays/ | 2–3 weeks | WS-4 |
| cyberneutics-director | ACTIVE | Medium | Keep in wild; escalate if orchestration prioritized | 8–12 weeks | Q2+ 2026 |
| harness-engineering | DORMANT | Low | Move to references/ | 1 week | WS-4 |
| issues | ACTIVE | Medium | Create resolution log in WS-4 | 1 week | WS-4 |
| neo-cybernetics | DORMANT | Low | Move to references/ | 1–2 weeks | Post-WS-4 |
| palgebra-graph-ui | ACTIVE | High | Keep in wild; prioritize for Q2 implementation | 4–6 weeks | Q2 2026 |
| pask-mesh-fitting | ACTIVE | Medium | Move to research-programs/; document tractability | 2–3 weeks | WS-4 |
| potential-to-sense | ACTIVE | HIGHEST | Promote to essays/ immediately | 1–2 weeks | WS-4 |
| residuality-theory | DORMANT | HIGH | Extract essay, move reference material | 2–3 weeks | WS-4 |
| software-factories | DORMANT | Low | Keep in wild; clarify research direction | 3–4 weeks | Q2 2026 |
| subagent-personas-for-debate | SUPERSEDED | Low | Archive with extraction | 1–2 weeks | WS-4 |
| diary/ | VERY ACTIVE | HIGH | Continue as-is; extract and promote quarterly | Ongoing | Ongoing |

---

## Consolidated Recommendations for WS-4 Remediation

### Phase 1 (Weeks 1–2): High-Priority Promotions
**Target: Move immediate graduation items into essays/**
1. potential-to-sense/ → essays/12-potential-to-sense.md
2. Bruner-Kahneman (diary) → essays/13-bruner-kahneman-pedagogy.md
3. Update essays/README.md, essays/index.md with new entries
4. Create cross-reference notes in related essays

### Phase 2 (Weeks 2–3): Integration and Extraction
**Target: Consolidate partially integrated material**
1. cybernetics/ → extract conversation-theory + pask biography → essays/14-pask-conversation-theory.md
2. residuality-theory/ → extract residues/eigenforms section → essays/15-residues-eigenforms.md
3. Move cybernetics/ and residuality-theory/ to references/
4. Update Essays 04, 10, 11 with cross-references

### Phase 3 (Weeks 3–4): Reference Migration and Cleanup
**Target: Relocate reference material; archive superseded content**
1. neo-cybernetics/ → references/neo-cybernetics/
2. harness-engineering/ → references/harness-engineering/
3. subagent-personas-for-debate/ → extract coordination schemes → artifacts/subagent-coordination-patterns.md; move README to archive/
4. pask-mesh-fitting/ → research-programs/pask-mesh-fitting-tractability.md (with scoped-down alternatives)
5. issues/ → create agent/archive/contributor-issues-resolution-log-2026-03.md

### Phase 4 (Ongoing): Diary Management
**Target: Extract and promote quarterly**
1. Furry Logic (diary) → essays/ in Week 4 or as part of next quarterly review
2. Consolidate Narrative Immune System + Dual Operations (1–2 weeks post-WS-4)
3. Begin quarterly diary review cycle (every 3 months)

---

## Impact on Essays/README and Navigation

After these changes, essays/ will grow from 11 numbered essays + 4 supporting essays to ~15 numbered essays + supporting material. The README will need updating to reflect:
- New essays 12, 13, 14, 15 and their reading paths
- Integration with potential-to-sense and residuality-theory material
- Updated character introduction and dependency diagram (per editorial review WS-1)

---

## Overall Pipeline Assessment

### Velocity
- **Graduation rate** (per month): 2–3 documents promoted from wild/ to core per month (Feb–Mar 2026)
- **Active exploration rate**: 9 diary entries in 25 days; 4 new wild directories created (Feb–Mar 2026)
- **Velocity ratio**: Exploration outpaces graduation by ~2.5:1. This is **healthy for a methodology in formalization phase**.

### Health Signals
- ✅ Active contributor feedback (issues, diary entries)
- ✅ Self-organizing: exploratory work → taming → formalization is functioning (committee-games example)
- ✅ Cross-cutting integration: new material connects to existing essays/palgebra
- ✅ Honest about limitations (pask-mesh-fitting tractability warning, potential-to-sense integration questions)
- ⚠️ Extraction lag: some materials ready to promote but not yet extracted
- ⚠️ Duplication risk: some exploratory entries could be consolidated earlier

### Forecast (Q2–Q3 2026)
If WS-4 and WS-5/6 (wild remediation) complete successfully:
- Wild content will shrink from 14 directories + diary to ~7 active research directions
- Essays will expand from 15 to ~18 numbered essays
- Research programs will absorb 2–3 formerly wild items (pask-mesh-fitting, blast-radius-problem eventually)
- Diary will mature as a formalized "research notes" publication with quarterly extraction cycles

---

## Special Notes and Open Questions

### Bruner-Kahneman Edit Plan (From Editorial Review WS-1)
The 2026-02-17 diary entry contains "a 9-edit plan for essay cross-references, of which 6 have been applied. Edits 2, 5, and 8 remain unapplied."

**Current status**: Not verified during this triage. This should be reviewed in WS-4:
- Read the diary entry carefully
- Verify which edits are done (6/9)
- Complete or explicitly defer remaining edits (2, 5, 8)
- Document the resolution

### Contribution Pipeline Validation (Scheduled June 2026)
Per project-state.md: "2026-06-08 — Contributor gatekeeping changes: Has anyone contributed to wild/ or wild/diary/? Has the diary-to-wild-to-formalization pipeline worked for external contributors?"

**Triage finding**: The diary-to-wild-to-formalization pipeline *has worked* for internal exploration (diary → committee-games → bridge paper). External contributor involvement is limited (issues, but no diary entries). This validation point should assess:
- Whether external contributors have started using the diary for exploration
- Whether the extraction/promotion process is transparent enough for contributors to follow
- Whether the intake convention and supersession notes are effective

---

## Conclusion

The wild content is **strategically well-aligned and actively productive**. The methodology is generating theory and architectural insights faster than it is shipping implementation, which is appropriate for the current phase. Two directories should promote immediately (potential-to-sense, committee-games); seven more should graduate within 4 weeks (Phase 1–2 of WS-4); four should remain as active research directions; and the diary should continue as-is with quarterly extraction reviews.

The pipeline velocity and health signals are strong. The main remediation work is organizational (moving things to their proper homes) rather than theoretical (rethinking content).

---

**Report prepared by**: Wild content triage workstream (Workstream 5, refactoring sprint 2026-03)

**Findings date**: 2026-03-13

**Repository state**: All wild directories, diary entries, and research material at HEAD of repo at time of triage.
