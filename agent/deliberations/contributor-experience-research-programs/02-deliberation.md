# Phase 2: Deliberation

**Topic**: Contributor experience in the research-programs directory — how can we make it easier for a researcher to contribute?

**Protocol**: Robert's Rules (modified for committee deliberation)

---

## Opening Statements

### Maya (Paranoid Realism)

Let me walk through what actually happens when someone arrives at this directory. They click into `meta/research-programs/README.md` and see a priority table with five programs. Good so far. Then they click on, say, `multi-model-committee.md` — the one listed as "High" priority — and they hit *1,730 lines*. That's not a research plan. That's a finished monograph. It has Python implementation code, API pricing calculations, YAML configuration templates. A contributor reading that will either think "this is already done, what's left for me?" or "I cannot possibly enter this in the middle."

Now consider the incentive structure. Who benefits from the current opacity? The project maintainer. If the barrier to entry is high, only deeply committed people contribute — which filters for quality but also filters for everyone. If the stated goal is "pick a plan that matches your skills and interests," but the plans don't *tell you* what skills are needed, the real message is: "figure it out yourself, and if you can't, you're not the right contributor." That's a gatekeeping function disguised as an open invitation.

I'm also suspicious of the "by impact on uncertainty" ordering. It sounds objective, but who decided what reduces uncertainty most? The maintainer. A contributor has no way to validate that ordering. They're being told what matters without being shown why. That's not collaborative — it's directive with collaborative aesthetics.

### Frankie (Idealism / Values Guardian)

The opening line of the README says: "The goal is to give contributors one place to find work that reduces uncertainty about whether and when the methodology works." That's a good aspiration. But the directory doesn't live up to it. The README is organized for someone who already understands the project's architecture — priority tables referencing "evaluation-schemes" and "ablation-study" and "Design F" assume familiarity with a vocabulary the newcomer hasn't learned yet.

The project's core principle is that LLMs are narrative engines and the user is an editor. If we believe in that principle, the research-programs directory should *narrate* a contributor's journey, not present a catalog and expect them to self-navigate. Right now it's a catalog. A good catalog, organized three ways (priority, status, theme) — but still a catalog.

What's missing is the *human* layer: What does each program *feel like* to work on? Which one can a solo contributor do in an afternoon? Which one requires running multi-model API calls and statistical analysis? The societies-of-thought plan gets this partially right — it says "pick an item that matches your skills or interests and run with it" and lists ten concrete items. But even there, Item 1 (Big Five characterization) and Item 10 (comparative effectiveness study recruiting 20-30 decision problems with expert raters) are presented at the same level despite requiring completely different commitment levels.

We should be asking: what would make someone *excited* to contribute, not just *able* to?

### Joe (Continuity Guardian)

I want to note that this directory just went through a restructuring. Two sessions ago, `research-plans/` was renamed to `research-programs/`, the ablation study was extracted from evaluation-schemes, and the condorcet comparison was consolidated from scattered locations. That restructure established conventions (Status/Runs/Results headers, results folders next to plans). Three of five plans still lack those headers — the handoff explicitly calls this out as optional cosmetic work.

My concern is that we're about to propose *another* restructuring on top of a restructure that hasn't fully landed. The conventions aren't even uniformly applied yet. If we add contributor-facing metadata (difficulty ratings, skill requirements, time estimates) to plans that don't even have consistent Status headers, we're layering new inconsistency on existing inconsistency.

History says: documentation restructures that happen in rapid succession tend to leave artifacts — stale references, conflicting conventions, half-migrated states. The condorcet consolidation already produced redirect stubs and empty directories that couldn't be deleted. Adding more structure now, before the current structure has settled, risks the same kind of debris.

My recommendation: finish applying the existing conventions (Status/Runs/Results on all five plans) *first*. Then assess whether additional contributor-facing metadata is needed. Don't treat a half-finished restructure as the baseline for a new one.

### Vic (Evidence Prosecutor)

What evidence do we actually have that contributors are confused? I see a problem statement — "a researcher discovers the project and wants to contribute" — but no data. Has anyone actually tried to contribute and bounced off? Is there a GitHub issue from a confused newcomer? A message saying "I wanted to help but couldn't figure out where to start"?

We're designing a solution for a hypothetical problem. The research-programs directory might be perfectly fine for its actual audience, which may be — given the project's niche — a small number of highly motivated researchers who are comfortable navigating complex documentation.

Let me be specific about what I can verify. The README has three organizing tables (priority, active, completed). That's standard documentation practice. The plans link to each other and to results directories. The conventions section explains where results go. The "pick a plan that matches your skills" instruction is admittedly vague, but it's also the standard approach for open-source research projects.

What I *can* point to as evidence of a problem: the variance in plan maturity is real and measurable. `ablation-study.md` is 140 lines with a clear procedure. `multi-model-committee.md` is 1,730 lines with implementation code. That 12x length difference, presented at the same level in the README table, is objectively misleading about the effort required. A contributor choosing between them has no way to know one is a clean experimental design and the other is an architectural proposal with a full prototype.

But before we redesign anything, I want to know: who is the target contributor? A grad student? A practitioner? An AI agent? The answer changes everything about what "easier" means.

### Tammy (Systems Thinker)

I want to map the feedback loops at work here, because the obvious fix ("add metadata to make plans more accessible") has second-order effects that aren't being discussed.

**Loop 1: Maintenance burden**. Every piece of contributor-facing metadata (difficulty rating, skill requirements, time estimates) is something that must be updated when plans change. The ablation study is "not started" today — in a month it might be "in progress" with different skill requirements. If nobody updates the metadata, it becomes misleading. Stale metadata is worse than no metadata, because it creates false confidence.

**Loop 2: The contributor funnel**. Making the directory easier to navigate increases the number of people who *start* engaging with a plan. But does it increase the number who *complete* meaningful contributions? If the bottleneck isn't "finding a plan" but "executing the research" (which requires domain knowledge, statistical skills, access to multiple LLM APIs), then improving the directory optimizes the wrong step. You get more people who start and bounce, not more finished contributions.

**Loop 3: Audience collision**. The research-programs directory currently serves two audiences: (a) the project maintainer tracking research progress, and (b) potential contributors looking for work. These audiences want different things. The maintainer wants accurate status tracking, cross-references, and archival conventions. The contributor wants a clear entry point, skill matching, and scope estimation. Optimizing for one degrades the other — a contributor-friendly "Good First Issue" tag on plans makes the directory noisier for the maintainer; rigorous cross-referencing (which the maintainer needs) overwhelms the contributor.

The system question is: should one directory serve both audiences, or should there be a separation — a contributor-facing "guide" that *references* the research-programs directory but doesn't live inside it?

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Skeptical of cosmetic fixes; the opacity is structural | High | Current structure gatekeeps while appearing open |
| Frankie | The directory should narrate a contributor journey | High | Mission alignment — accessibility is a stated value |
| Joe | Finish existing conventions before adding new ones | High | Restructuring on unstable ground creates debris |
| Vic | No evidence of actual contributor confusion; define target audience first | Medium | Solving a hypothetical problem without data |
| Tammy | Separate contributor-facing layer from maintainer-facing tracking | Medium | Dual-audience collision, maintenance burden feedback loop |

---

## Key Tensions Identified

1. **Accessibility vs. Gatekeeping** (Maya vs. Frankie): Is the current complexity an accidental barrier or a functional filter?
2. **Act now vs. Stabilize first** (Frankie vs. Joe): Add contributor metadata now, or finish applying existing conventions first?
3. **Hypothetical vs. Real problem** (Vic vs. all): Do we have evidence that anyone has actually been confused?
4. **Single directory vs. Separation** (Tammy): Should one artifact serve two audiences?
5. **Metadata maintenance** (Tammy vs. Frankie): Adding helpful metadata creates a maintenance obligation. Who services it?

---

## Round 1

**Chair**: Let's start with Vic's challenge. Do we have evidence this is a real problem, or are we designing for a phantom contributor?

**Vic**: I want to be clear — I'm not saying the directory is perfect. I'm saying we should distinguish between "this would be nice" and "this is blocking someone." The project has existed for weeks, not years. There may not *be* a confused contributor yet. The question is whether to invest effort now (proactive design) or wait for signal (reactive improvement). Both are valid strategies.

**Maya**: Vic's asking for evidence we can't have yet. The project is young enough that there are no external contributors. But look at the *structural* evidence: a 1,730-line plan file with no executive summary, no skill requirements, no scope estimate. That's not "might confuse someone" — that's objectively poor information design. You don't need a confused user to know that a document should signal what it is before you have to read all of it.

**Frankie**: And the README itself says "If you want to contribute: pick a plan that matches your skills and interests." That's the project *inviting* contributions. If you invite people, you owe them a navigable path. You can't put up a sign saying "come in" and then have the lobby be an unmarked maze.

**Vic**: Fair. I'll concede that the *invitation* creates an obligation. If the README didn't claim to be contributor-facing, I'd say leave it as an internal tracker. But it does claim that, so it should deliver. My question stands, though: who is the target contributor? The answer materially changes what we recommend.

**Joe**: I want to address this. Looking at the project's content — it's a methodology for working with LLMs as sense-making partners, with formalized algebra, pipeline composition, adversarial committees. The target contributor is probably someone with: (a) experience with LLMs and prompt engineering, (b) interest in decision-making under uncertainty, (c) comfort with research methodology. That's not a mass audience. That's maybe a few hundred people in the world who would both find this interesting and be equipped to contribute.

**Tammy**: Which actually changes the calculation. If the contributor pool is small and self-selecting, heavy-duty onboarding infrastructure might be over-engineering. But *minimal* signaling — difficulty, scope, skills needed — would still help even expert contributors triage plans efficiently. The question isn't "make it easy for anyone" but "make it efficient for the right people."

### Round 1 Analysis

- **Emerging consensus**: The invitation in the README creates an obligation to make the directory navigable. The target audience is expert but the plans still lack basic triage information.
- **New tension**: Scale of intervention — minimal metadata additions vs. structural reorganization.
- **Status**: Moving toward "what specifically should change" rather than "should anything change."
- **Next**: Concrete proposals and their trade-offs.

---

## Round 2

**Chair**: We've established that something should change. Let's hear concrete proposals. What specifically would help, and what does each cost?

**Tammy**: I want to propose a layered approach that addresses the audience-collision problem. Three changes, from lightest to heaviest:

**Layer 1** (Low cost, high impact): Add a metadata block to each plan file — 5-10 lines at the top, after the Status section. Fields: `Skills needed`, `Estimated scope` (afternoon / week / month), `Contributor type` (solo / collaborative), `Entry point` (what to read first, what to do first). This costs maybe an hour of maintainer time per plan, and it degrades gracefully — if it goes stale, the plan itself is still there.

**Layer 2** (Medium cost): Add a "Contributor Quick-Start" section to the README, *above* the priority table. Three to five sentences: "New here? Start with [ablation-study] if you want a self-contained experiment. Start with [societies-of-thought Item 1] if you want to improve the existing infrastructure. Start with [condorcet-comparison] if you want to see how a completed program looks." This gives the newcomer three doors instead of five equally opaque ones.

**Layer 3** (Higher cost, questionable ROI): Create a separate `CONTRIBUTING.md` in the repo root that covers the full contributor journey — from "what is this project" through "how to submit results." This is standard open-source practice but adds a maintenance artifact.

**Joe**: I support Layer 1 on the condition that we *first* finish the Status/Runs/Results headers on the three plans that lack them. Otherwise we're adding a second inconsistent metadata scheme on top of a first inconsistent one. The order matters: conventions first, contributor metadata second.

**Maya**: Layer 1 is fine but it's the easy part. The real problem is what happens *after* someone picks a plan. Take the ablation study. Clean procedure, clear factors, defined run budget. But actually running it requires: choosing N decisions, generating outputs through multiple pipeline conditions, recruiting raters, computing effect sizes. Where does the contributor find "N decisions"? How do they "generate outputs through full methodology"? The plan assumes you already know how to run `/committee` and `/scenarios` — which means you need to understand the entire methodology, the skill system, the agent directory... The rabbit hole is deeper than the README suggests.

**Frankie**: Maya's point is important. The plans are written for someone who already understands the project. They reference artifacts, skills, and conventions without explaining how to access them. Even Layer 1 metadata won't fix that — it can tell you "Skills needed: familiarity with committee pipeline" but it can't teach you the committee pipeline. The missing piece is a *learning path*: "To contribute to the ablation study, first read [X], then try [Y], then you're ready to run [Z]."

**Vic**: Now we're conflating two different problems. One is "the research-programs directory lacks triage information" — solvable with metadata. The other is "the project lacks onboarding documentation" — a much larger problem that isn't the directory's job to solve. If we scope creep from "improve this directory" to "write an onboarding guide for the entire methodology," we'll never ship anything.

**Maya**: Vic's right that they're different problems, but wrong that the directory can ignore the second one. If you put up a sign saying "contribute here" and the contributor can't contribute because they lack prerequisite knowledge, the sign is misleading regardless of how well-organized the directory is. Either remove the invitation or provide the prerequisites.

**Joe**: Which is exactly what happened with the wild/ directory intake convention — it says "read both files before drawing on the material." Clear prerequisite. We could do the same: "Before contributing to a research program, ensure you've read [artifacts/adversarial-committees.md] and can run `/committee` on a test topic." That's a prerequisite statement, not an onboarding guide.

### Round 2 Analysis

- **Emerging consensus**: A layered approach — metadata blocks on plans (Layer 1) + quick-start section in README (Layer 2). Layer 3 (CONTRIBUTING.md) is lower priority.
- **New tension**: Plan-level metadata vs. project-level onboarding. The directory can signal difficulty and scope, but can't substitute for missing prerequisite documentation.
- **Status**: Converging on concrete recommendations; residual disagreement on whether prerequisites should be stated or taught.
- **Next**: Address the multi-model-committee length problem and finalize recommendations.

---

## Round 3

**Chair**: The multi-model-committee document came up early as a specific problem — 1,730 lines presented as a "plan" alongside 140-line plans. What do we do about it?

**Vic**: Let me quantify the variance. Here are the line counts:
- `ablation-study.md`: ~140 lines
- `condorcet-comparison.md`: ~100 lines
- `societies-of-thought-research-plan.md`: ~250 lines
- `evaluation-schemes.md`: ~800 lines
- `multi-model-committee.md`: ~1,730 lines

The mean is ~600, the median is ~250, and multi-model-committee is 3 standard deviations above the mean. It contains: a hypothesis section, five architectural patterns with code, model personality profiles, orchestration details, a full experimental protocol (4 phases), an evaluation framework, cost analysis, and a production readiness checklist. This isn't a plan — it's a plan, a design document, a prototype, and an architecture review rolled into one file.

**Tammy**: The system problem here is that the README presents all five as "plans" at the same level of abstraction. But they're fundamentally different artifacts. `ablation-study.md` is a clean experimental protocol: objective, procedure, expected output. `multi-model-committee.md` is a research *program* in the sense of "everything you'd need to build and evaluate a multi-model system." Presenting them side-by-side as "plans" is a category error.

**Maya**: And notice the political implication. If a contributor looks at multi-model-committee and thinks "this is what a plan looks like here," they'll either feel inadequate (can't match that level of detail) or conclude the work is already done (why contribute if 1,700 lines of design already exist?). Either way, it's a contribution suppressor.

**Frankie**: The fix seems clear: the multi-model-committee document should have an executive summary and a "how to contribute" section at the top. Something like: "This document describes a research program for multi-model committees. The *plan* is in the Experimental Protocol section. Phases 1-2 are the immediate priorities. If you want to contribute, start with Phase 1 (model profiling) — it requires API access to multiple LLMs and approximately 20 hours."

**Joe**: That's the Layer 1 metadata approach applied to multi-model-committee specifically. I'd go further: that document should probably be split. The hypothesis and architectural patterns (the "why and what" part) are a *reference document*. The experimental protocol (the "how to test it" part) is the actual *plan*. They serve different readers at different times. But splitting it is a larger change and should wait until the document's author (or a session with mg) approves the restructure.

**Vic**: Agreed on the split recommendation, but I want to note: splitting is a proposal for a future session. For now, the actionable fix is metadata at the top of each plan. That's implementable in 30 minutes. The split requires authorial judgment about how to partition.

**Tammy**: Let me synthesize what I think we're converging on. Three recommendations, ordered by implementation cost:

1. **Add a metadata/triage block to each plan file** (Layers 1). Fields: Status (already in convention), Skills, Scope, Contributor type, Entry point. Apply to all five plans. This takes about an hour.

2. **Add a "Quick Start for Contributors" section to the README**, above the priority table. Three curated entry points keyed to contributor profile (experimenter, infrastructure builder, theory builder). Include a prerequisites line. This takes about 20 minutes.

3. **Recommend (don't implement now) that multi-model-committee.md be restructured** — either split into reference + protocol, or given a strong executive summary that directs readers to the actionable section. Flag for mg's next session.

**Maya**: I want to add a fourth: **state prerequisites explicitly**. The README should say something like: "Contributing to most programs requires familiarity with the adversarial committee pipeline. If you haven't run `/committee` before, start by reading `artifacts/adversarial-committees.md` and running a test deliberation." Without that, all the metadata in the world won't help someone who doesn't know the methodology.

**Frankie**: I agree with all four. And I want to note that the *tone* matters. The current README is written like an internal tracking document — functional, precise, bureaucratic. Contributor-facing text should be slightly warmer. Not marketing copy, but something that communicates "we want you here and here's how to get started" rather than "here is the catalog; self-serve."

**Joe**: One caution on tone: this project's voice is deliberately non-hyperbolic. The CLAUDE.md says "don't collapse to single answers prematurely" and "don't optimize for looking rigorous." Warm is fine; enthusiastic-startup-README is not. Keep the tone consistent with the rest of the repo.

**Vic**: Final point. Whatever we recommend, it should be cheap to implement and cheap to maintain. The worst outcome is a beautiful contributor guide that goes stale in two weeks. Everything we recommend should either be self-maintaining (links to plans that stay current) or require minimal update effort (a metadata block that only changes when the plan's status changes — which is already tracked).

### Round 3 Analysis

- **Emerging consensus**: Four concrete recommendations (metadata blocks, quick-start section, multi-model restructure flag, prerequisites statement). Ordered by cost and urgency.
- **Residual tension**: How much warmth/tone shift is appropriate (Frankie vs. Joe). Whether prerequisites should be stated or taught (Maya vs. Vic).
- **Status**: DELIBERATION COMPLETE.

---

## Final Consensus

- **Unanimous**: Add triage metadata blocks to all five plan files (Skills, Scope, Contributor type, Entry point).
- **Unanimous**: Add a "Quick Start for Contributors" section to the research-programs README.
- **Unanimous**: State prerequisites explicitly in the README (what a contributor should read/do before tackling a program).
- **Majority (4-1, Joe abstains)**: Recommend restructuring multi-model-committee.md in a future session (Joe wants to wait until existing conventions are fully applied first, but doesn't object to flagging the recommendation).
- **Unanimous**: Finish applying Status/Runs/Results headers to the three plans that lack them, as a prerequisite to the above changes.
- **Noted**: The project lacks broader onboarding documentation, but that is out of scope for this directory-focused deliberation.

---

## KEY TENSIONS IDENTIFIED

- **Catalog vs. Narrative**: The README organizes plans as a catalog (tables, links). A contributor needs a narrative ("if you're interested in X, start here"). Tension between maintainer convenience (tables are easy to update) and contributor experience (narrative guides are easier to follow).
- **Minimal metadata vs. Full onboarding**: Adding triage metadata to plans is cheap and helpful. But it doesn't solve the deeper problem that plans assume familiarity with the methodology. The boundary is: metadata tells you *what* a plan involves; onboarding teaches you *how* to do it.
- **Consistency before expansion**: Three plans lack even the basic Status/Runs/Results headers. Adding contributor metadata on top of missing basic metadata creates layered inconsistency. Joe's argument: apply existing conventions first.
- **Document scope vs. Contributor expectations**: multi-model-committee.md is a plan, design doc, prototype, and architecture review in one file. Presenting it alongside 140-line experiment protocols is misleading about effort required.
- **Tone and audience**: Internal tracking document vs. contributor-facing guide. The README currently serves the maintainer. Making it serve contributors means slightly different writing — not a rewrite, but a shift in framing.

## ASSUMPTIONS SURFACED

- **There will be external contributors** (Maya questions this; if the contributor pool is essentially zero, the investment is wasted)
- **Contributors are technically sophisticated but unfamiliar with this specific project** (Joe's characterization; changes what "easier" means)
- **The plans themselves are the right unit of contribution** (Tammy notes that a contributor might want to work at a finer granularity — one action item from societies-of-thought, one phase from multi-model-committee)
- **Metadata will be maintained** (Tammy flags the stale-metadata failure mode; Vic argues for self-maintaining approaches)
- **Prerequisite knowledge can be pointed to, not taught** (consensus position; the directory's job is to link, not to educate)

## EVIDENCE REQUIREMENTS

- **Actual contributor feedback**: Has anyone attempted to contribute and bounced? GitHub issues, messages, or abandonment signals would validate or invalidate the problem.
- **Time-to-triage measurement**: How long does it take a knowledgeable reader to pick a plan and understand what's involved? Baseline this before and after changes.
- **Maintenance cost tracking**: After adding metadata, track how often it goes stale and what effort is needed to keep it current.

## DECISION SPACE MAP

| If you optimize for... | You sacrifice... | Key character's concern |
|------------------------|-----------------|------------------------|
| Contributor accessibility | Maintainer simplicity, document length | Frankie: the invitation must be real |
| Minimal changes | Contributor experience improvements | Joe: stability over novelty |
| Comprehensive onboarding | Implementation speed, scope control | Vic: avoid scope creep |
| Internal tracking accuracy | Contributor friendliness | Tammy: audience collision |

## RECOMMENDED NEXT STEPS

1. **Immediate (this session or next)**: Apply Status/Runs/Results headers to `multi-model-committee.md`, `societies-of-thought-research-plan.md`, and `evaluation-schemes.md` — finishing the existing convention.
2. **Short-term (next 1-2 sessions)**: Add triage metadata blocks to all five plans. Add "Quick Start for Contributors" section and prerequisites statement to the README.
3. **Flag for mg**: Recommend restructuring `multi-model-committee.md` (split or add executive summary + contributor section). This requires authorial judgment.
4. **Deferred**: Broader project onboarding guide (CONTRIBUTING.md in repo root). Only invest if external contributors actually appear.
5. **Monitor**: If changes are implemented, watch for stale metadata and adjust maintenance approach.
