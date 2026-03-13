# Rubric: Repository Internal Consistency and Validation

**Status**: Draft extension to the Audience Experience rubric. These dimensions complement but do not replace repo-audience-experience.md.

**Purpose**: Score the Cyberneutics repository for internal consistency (do claims agree across documents?), temporal currency (are docs still accurate?), pipeline health (how mature is wild content?), formal rigor (does palgebra notation align?), and real-world validation (has the methodology been tested outside the repo?). Used to surface data quality and maturity issues that audience-experience assessment doesn't capture.

**Scope**: Applies to all content tiers—essays, artifacts, palgebra, wild, and meta—as specified by the review prompt. Focuses on consistency *between* documents and with external reality, not on internal document quality (covered by audience-experience rubric).

**Scoring**: 0–3 per dimension. Dimensions are independent; a repo can score high on audience experience and low on consistency, or vice versa.

---

## Quick Reference

| Dimension | 0 | 1 | 2 | 3 |
|-----------|---|---|---|---|
| **Internal consistency** | Multiple major contradictions | Some contradictions; some reconciliation | Minor inconsistencies resolved | All cross-document claims agree; terminology stable |
| **Currency/staleness** | Most docs clearly outdated | Mixed; some current, some stale | Most current; a few needing refresh | All docs current or explicitly versioned; refresh dates tracked |
| **Pipeline velocity** | Wild content unmarked; status unclear | Some status labels; unclear promotion paths | Most wild content has status; some topics graduated | Clear pipeline: active/dormant/promoted/archived; health metrics visible |
| **Formal consistency (palgebra)** | Multiple notation conflicts | Some notation unified; gaps in definitions | Mostly consistent notation; minor gaps | Type names, composition laws, operators unified; formalism complete |
| **Practical validation** | No evidence of real-world use | Claimed but unverified; example runs only | Some external testing; limited scope | Published evidence; external adoption; empirical case studies |

---

## Dimension 1: Internal Consistency

**What this measures**: Whether claims, definitions, and terminology agree across documents. If essay A says "the committee is adversarial" and artifact B says "the committee finds consensus," that's a consistency failure. Do type names stay constant? Do core concepts (deliberation, narrative engine, resource equation) mean the same thing throughout?

Consistency failures undermine trust and make the methodology harder to apply. They signal either incomplete thinking or poor communication. Readers navigating multiple documents should encounter one coherent idea, not contradictory variants.

- **0 — Major contradictions**: Core claims contradict across documents (e.g. "methodology scales to teams of 10" vs. "tested only 1:1"). Type names drift significantly (palgebra calls something `Probe` while artifacts call it `probe-run`). Key concepts have incompatible definitions (deliberation as "open debate" in one essay, "structured synthesis" in another). Reader cannot reconcile without external help.

- **1 — Some contradictions with attempted reconciliation**: Noticeable contradictions exist (e.g. on when committees work, cost, required skills) but some are addressed via footnotes or "also called" clauses. Terminology mostly stable but with a few unreconciled synonyms. One or two cross-document claims hard to reconcile without charity.

- **2 — Minor inconsistencies resolved**: Terminology and definitions largely stable across tiers. A few minor conflicts (e.g. one doc says "high-stakes decisions" and another says "strategic decisions" without explanation) but easily reconciled by a careful reader. No major contradictions; cross-references work.

- **3 — Fully consistent**: All substantial claims agree across documents. Terminology unified or explicitly aliased ("also called X"). If the same claim appears in multiple places, it's stated the same way. Type names and operator syntax stable across essays, artifacts, and palgebra. Reader can move between documents and encounter one coherent methodology.

### Evaluation Questions

1. When the same concept appears in multiple documents, is it defined the same way?
2. Are there contradictions about when/why/how the methodology works? If so, are they explained or resolved?
3. Do type names and terminology stay consistent across essays, artifacts, and palgebra?
4. Are synonyms explicitly acknowledged ("also called X") or hidden (reader discovers them by accident)?
5. Could a reader follow claims across documents without confusion?

---

## Dimension 2: Currency and Staleness

**What this measures**: Whether documentation reflects current truths. Is the README accurate as of today? Were the examples run this year or three years ago? Is a claimed constraint (e.g. "only works with Claude 3") still valid?

Stale documentation erodes trust and wastes reader time. A methodology whose docs say "tested with GPT-4" but you're using Claude 3.5 creates uncertainty. A tool whose "quick start" references removed features is unusable.

Staleness is measured by: (1) explicit refresh dates or version markers, (2) observable drift (e.g. API changes, deprecated examples, outdated compatibility claims), (3) proportion of docs with recent verification. A repo can be current in some sections (actively maintained essays) and stale in others (ancient archive entries).

- **0 — Clearly outdated**: Most docs lack refresh dates. Observable drift: examples use removed APIs, claim compatibility with old models, reference past tool names. Claims about methodology state ("we tested with X") clearly false as of today. Reader cannot trust which claims are current. Archive material is not labeled and reads as live content.

- **1 — Mixed freshness**: Some docs clearly current (README, recent essays); others stale (artifact examples using old syntax, wild-dir entries from 2024 with no dates). A few docs have refresh dates; most don't. Some backward-compatibility flags exist; others missing. Reader unsure which docs are authoritative versions.

- **2 — Mostly current**: Most docs current or explicitly dated. Observable drift is minimal. Examples use current APIs/models. Compatibility claims align with current platforms. A few sections (e.g. one wild-dir topic, one old example) need refresh; noted but not blocking. Stale archive is labeled as such.

- **3 — Maintained currency**: All live docs current or explicitly versioned (e.g. "last verified 2026-03-13"). Examples use current APIs and platforms. Compatibility claims include effective dates. Refresh dates visible. If a claim is potentially stale (e.g. "tested only with Claude 3.5"), it includes verification date and procedure for checking currency. Archive is clearly labeled; live content is not stale. No drift between docs and observable reality.

### Evaluation Questions

1. When was each major document last verified? Is that date visible?
2. Are examples and API references current, or do they use obsolete syntax/models?
3. When the repo claims compatibility with a tool or model, is that claim dated?
4. If a document makes a claim about "current" practice, is the claim still true today?
5. Can a reader distinguish live, current docs from archived or historical material?

---

## Dimension 3: Pipeline Velocity

**What this measures**: For wild content and emerging ideas: how healthy is the pipeline from exploration (diary, incoming ideas) to formalization (essays, artifacts, palgebra)? Do topic directories have clear status markers (active, dormant, promoted, archived)? How many topics have graduated to core content? How many are stuck in exploration?

A healthy pipeline keeps wild content from becoming technical debt while protecting exploratory freedom. A repo with 20 untagged wild-dir topics is disorienting. A repo where topics graduate explicitly (e.g. "potential-to-sense moved from wild to essays on 2026-03-13") shows velocity.

Pipeline health includes: (1) status visibility (every wild topic is marked), (2) graduation criteria (when does something move from wild to core?), (3) promotion rate (how many topics actually graduate?), (4) dormancy handling (what happens to inactive topics?).

- **0 — No status tracking**: Wild content unmarked; reader cannot tell what is active, dormant, or abandoned. No graduation path documented. Topics pile up with no clear status. No aging metrics. Looks like a todo heap, not a pipeline. Archive exists but content is mixed with active.

- **1 — Partial status tracking**: Some topics tagged (active/dormant); others unmarked. Graduation path mentioned vaguely (e.g. "good wild content moves to essays") but not formalized or applied. A few topics have graduated; most languish. Archive exists but unclear what moves there and when. Staleness not actively managed.

- **2 — Mostly clear status**: Most wild topics have visible status (active, dormant, candidate for promotion). Graduation path documented (e.g. "move to essays when 3+ references or ready to teach"). Some topics have graduated; pipeline is working but modest flow. Archive labeled clearly. A few topics unclear on status; marked for review.

- **3 — Healthy, visible pipeline**: Every wild topic has explicit status (active, dormant, promoted, archived). Graduation criteria documented and enforced (e.g. "candidate for essays when X, Y, Z met"). Topics move through pipeline regularly; promoted work is visible and dated. Archive clearly separated. Dormancy is managed (old inactive topics reviewed periodically). Pipeline velocity is observable (reader can see what's moving and why).

### Evaluation Questions

1. Can you find the status of each wild topic quickly? Is it marked?
2. Is there a documented path for wild content to graduate to core (essays/artifacts/palgebra)?
3. How many wild topics have actually graduated? When?
4. Are inactive (dormant) topics managed—reviewed, archived, or actively reactivated?
5. Could someone reading wild/README.md understand the health and velocity of the pipeline?

---

## Dimension 4: Formal Consistency (Palgebra)

**What this measures**: Specific to palgebra and formal machinery. Do type definitions agree across documents? Is the notation (e.g., how are resource equations written) consistent? Do composition laws stay the same? Are operator precedence and syntax uniform?

This dimension applies narrowly but deeply to the formal tier. It's about internal coherence of the mathematical/categorical foundations, not pedagogical clarity (covered by audience-experience). A palgebra reader should see one consistent formal system, not fragmented notations or conflicting definitions.

Formal consistency includes: (1) type name agreement (is it `Probe` or `probe`? Is it defined the same way everywhere?), (2) notation (are resource equations written with → or ⊢ or something else? Does it vary?), (3) composition laws (do functorial properties of compose hold uniformly?), (4) operator definitions (is `fan` defined the same in two places?).

- **0 — Multiple notation conflicts**: Type names conflict (e.g. one essay uses `deliberate` as a function, another uses `Deliberate` as a type; unclear which is which). Resource equation syntax varies across docs without explanation (→ vs. ⊢ vs. ∘). Composition laws stated differently (associativity shown in one context, assumed in another). Operators (fan, funnel, etc.) defined inconsistently. Reader cannot apply formalism uniformly.

- **1 — Some unification with gaps**: Notation mostly consistent but a few variants (e.g. minor syntax variation across two papers). Type definitions mostly agree with a few informal aliases. Composition laws mostly consistent but one or two edge cases undefined. Operators have definitions but one lacks full specification. Formalism is usable but requires careful reading.

- **2 — Mostly consistent notation**: Type names, notation, composition laws consistent across palgebra docs. A few minor gaps (e.g. operator precedence not fully specified, one theorem stated but not proven). Some informal material lacks formal parallel (e.g. an artifact concept mentioned but not formalized yet). Formalism is solid; minor cleanup needed.

- **3 — Fully coherent formalism**: All type names unified and consistently defined. Notation (equations, operators, precedence) uniform across docs. Composition laws explicit and consistent. All operators fully specified. Theorems stated with uniform rigor. Informal concepts from artifacts/essays have formal parallels or are explicitly noted as open (not yet formalized). Reader can apply formalism directly without reconciliation.

### Evaluation Questions

1. Do type names stay the same across all palgebra documents? Are variants explained?
2. Is the notation for resource equations consistent (same symbols, precedence, reading direction)?
3. Are composition laws (e.g., associativity, functoriality) stated uniformly, or do they vary?
4. Are operator definitions complete and consistent? Could you implement them from the docs?
5. When palgebra documents discuss the same concept, do they describe it formally the same way?

---

## Dimension 5: Practical Validation

**What this measures**: How much of the methodology has been tested outside the repo itself? Have external users applied the techniques? Is there published evidence (papers, case studies, blog posts) of real-world use? Have failure modes been identified empirically, not just theoretically?

Validation is the gap between "we tested this with Claude" and "five teams ran committees and here's what happened." A mature methodology shows evidence in the wild, not just in-house testing. This dimension captures confidence that the methodology will work for someone else, not just its authors.

Validation includes: (1) external adoption (outside teams, companies, or researchers using it), (2) published evidence (case studies, papers, conference presentations), (3) empirical failure modes (identified by real use, not speculation), (4) scope documentation (works for X but not Y; we verified this).

- **0 — No external validation**: No mention of external use. All examples are in-house, author-generated. Claims about effectiveness ("methodology helps teams decide") are unsupported. Failure modes are hypothetical. Scope (when it works, when it doesn't) is unclear or untested. Reader has no way to assess whether this will work for them.

- **1 — Claimed but unverified**: Methodology presented as widely useful, but evidence is thin. A few anecdotes ("a team tried it and liked it") without detail. Example runs in repo are author-generated. One or two case studies mentioned but not documented. Failure modes guessed, not observed. Scope claims unverified. Reader unsure if methodology is mature or aspirational.

- **2 — Some external testing**: Methodology has been used by some external teams or contexts. Case study or two documented (if brief). Some empirical failure modes identified (e.g. "committees fail when stakeholders don't share values"). Scope is partially tested (works for strategic decisions, tested less for tactical). Author claims some external validation but depth is limited.

- **3 — Strong external evidence**: Methodology has been applied in published case studies or papers. Multiple external teams have adopted it; evidence is documented. Failure modes identified empirically and documented (e.g. "here's what went wrong and why"). Scope is well-mapped (effective for X, inappropriate for Y; verified by external use). Reader has confidence this will work for them, with known caveats.

### Evaluation Questions

1. Is there evidence of external teams or researchers using the methodology? How is it documented?
2. Are case studies or published papers available? How recent and rigorous?
3. Have failure modes been identified by external use, or are they only theoretical?
4. Is the scope of applicability (when it works, when it doesn't) tested against real-world use?
5. Could someone unfamiliar with the authors judge whether this methodology will work for their problem?

---

## How to Use This Rubric

### With the Audience Experience Rubric

This rubric complements `repo-audience-experience.md`. Use both together for comprehensive assessment:

- **Audience Experience** measures: Are readers oriented? Is the path clear? Is the writing good? Will someone understand how to apply this?
- **Consistency and Validation** measures: Are the facts correct? Do they agree? Have they been tested? Is the content current?

A repo can score high on Audience Experience (great writing, clear paths) and low on Consistency (contradictions, stale examples). Or vice versa. Together, they give a complete picture.

### Workflow

1. **Apply Audience Experience rubric** (repo-audience-experience.md) per its instructions. Score 0–3 on seven dimensions.
2. **Apply this rubric** (repo-consistency.md) independently. Score 0–3 on five dimensions.
3. **Synthesize**: For each dimension in both rubrics, note the score and key evidence. Identify priority fixes.
4. **Prioritize**: Audience-experience fixes (paths, coherence, actionability) drive reader experience first. Consistency fixes (contradictions, staleness, validation) build confidence and maintainability.

### Interpretation

- **High Audience Experience + High Consistency**: Excellent repo. Readers are well served and confident.
- **High Audience Experience + Low Consistency**: Readers feel oriented but discover contradictions or stale material when they dig. Fix: resolve cross-document inconsistencies, date content, add caveats.
- **Low Audience Experience + High Consistency**: Content is sound but hard to navigate or understand. Fix: add context, reorder, create reading paths, improve examples.
- **Low Audience Experience + Low Consistency**: Major work needed. Prioritize fixes to audience experience (paths, coherence) first, then consistency (facts, validation).

---

## Reference

**See also**:
- `repo-audience-experience.md` — Complementary rubric for audience experience
- `artifacts/evaluation-rubrics-reference.md` — For committee deliberations (different context)
- `meta/project-state.md` — Current state including recent changes and consistency status
- `agent/onboarding-core.md` — Canonical onboarding guide; consistency baseline
