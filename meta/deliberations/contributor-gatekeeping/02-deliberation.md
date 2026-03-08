# Phase 2: Deliberation

**Topic**: How should contributor documentation be revised to welcome exploratory contributions without degrading structural clarity?

**Protocol**: Robert's Rules (modified for adversarial committee).

**Brief**: `agent/contributor-gatekeeping-committee-brief.md`

---

## Opening Statements

### Maya (Paranoid Realism)

Let me name what I see. The contributor guidelines are doing something politically useful that nobody planned: they filter for contributors who are already aligned with the maintainer's mental model of what belongs in this repo. The contributor who left didn't leave because the guidelines are badly written. They left because the guidelines told them the truth about what the repo currently values — finished artifacts over raw thinking.

The question isn't whether to add a `wild/` path to the docs. That's trivially easy. The question is whether the maintainer actually wants unstructured contributions from strangers, because accepting them creates work. Someone has to read them, respond to them, route them. The brief says "mg will vet them but is biased toward innovation." That's one person. What happens when ten people drop half-formed ideas into `wild/` and expect engagement? The contributor who left expected their PR to start a conversation. If the conversation doesn't happen even after you invite people in, the second failure is worse than the first — now you've made a promise you can't keep.

I want to know: who is doing the labor of welcoming exploratory contributors, and is that labor budget realistic?

### Frankie (Idealism / Values Guardian)

Maya is right that this is about labor, but wrong about the implication. The repo's own methodology was developed through lateral, speculative walks — the diary entries that became the fan/funnel framework, the residuality theory explorations, the neo-cybernetics connections. Every major theoretical advance in this repo started as the kind of contribution the guidelines currently discourage. The methodology's origin story contradicts its contribution model. That's not just a documentation bug — it's a values contradiction.

The fix needs to be real, not performative. Adding one line about `wild/` to `CONTRIBUTING.md` isn't enough if the surrounding text still reads as a contract. The entire tone of `CONTRIBUTING.md` signals "prove you belong" rather than "here's how to join the conversation." The "compact contribution contract" framing in the first paragraph says it all — contracts are adversarial legal instruments, not invitations.

I want the contributor guide to have an explicit row in its routing table for "I have a half-formed idea or a lateral connection." That row should point to `wild/diary/` and say clearly: no structure required, no conventions to follow, just bring the idea. The diary-to-wild-to-formalization pipeline already exists as practice. Surface it.

### Joe (Continuity Guardian)

I wrote these guidelines. Well, an agent wrote them during a session I oversaw. Let me tell you why they are the way they are.

Before the contributor routing existed, agents dropped files in random locations, ignored the runtime-vs-example distinction, and created structural drift that took multiple sessions to clean up. The guidelines solved a real problem: unstructured contributions create maintenance debt. The five contribution types, the placement rules, the validation checklist — all of these emerged from concrete failures.

Now, I hear the argument that a human contributor is different from an agent. Fair. But the structural problem doesn't disappear because the contributor has good intentions. A half-formed essay dropped into `wild/` still needs someone to decide whether it connects to existing threads, whether it duplicates work, and whether it's going anywhere. The diary entries that became major advances all had mg as the connective tissue. That's not a contribution model — that's one person's editorial judgment.

What I want to avoid: relaxing the guidelines now, having several low-quality contributions land in `wild/`, and then reimposing stricter rules later. That whiplash is worse than consistent expectations. If we open the door, we need to be honest about what's on the other side.

### Vic (Evidence Prosecutor)

We have exactly one data point: one contributor who self-selected out. I want to be careful about overreacting to N=1.

Here is what we actually know: the contributor submitted a PR with an essay. The essay had "genuine intellectual merit and connected to existing threads." The contributor then closed their own PR after reading the contributor guidelines. We don't know which specific passage triggered the withdrawal. We don't know if they would have stayed if `wild/` were mentioned. We don't know if the essay would have actually been accepted.

What we don't know matters. If the contributor read the placement rules and concluded their essay didn't fit any of the five categories, the fix is to add a sixth category. If the contributor read the tone and felt unwelcome, the fix is to change the tone. If the contributor read the validation checklist and felt the bar was too high for an exploratory piece, the fix is to scope the checklist. These are different interventions with different implications.

Before we rewrite documentation, I want to know: did anyone ask the contributor what specifically put them off? Can we examine which pages they likely read, in what order? The brief assumes the problem is the missing `wild/` path, but that's a hypothesis, not a finding.

### Tammy (Systems Thinking)

I see two feedback loops in tension.

Loop 1, the quality loop: strict guidelines → consistent structure → agents can navigate → maintenance cost stays low → maintainer has time for substantive work → quality improves. This loop is currently working. The three cleanup sessions documented in the handoff history confirm it — structural drift was a real problem, and the guidelines reduced it.

Loop 2, the contribution loop: inviting guidelines → diverse contributors → new ideas → methodology improves → more people find it valuable → more contributors. This loop is currently broken at the first step. The guidelines optimize for Loop 1 at the expense of Loop 2.

The system question: can you run both loops simultaneously, or does one necessarily degrade the other? I think you can, but only if you create a clear boundary between structured and exploratory contribution paths so that exploratory contributions don't introduce the structural drift that Loop 1 was designed to prevent.

The `wild/` directory is that boundary. Contributions to `wild/` should not be held to the same structural standards as contributions to `artifacts/` or `essays/`. But they need *some* convention — even if it's just "one markdown file with a descriptive filename" — or the directory becomes a dumping ground that degrades the repo's navigability.

The diary is even further out. If it becomes the on-ramp, what stops it from becoming a pile that nobody curates? The pipeline only works if the funnel end (mg vetting) keeps pace with the fan end (contributors dropping ideas).

---

## Initial Positions Summary

| Member | Stance | Confidence | Key Concern |
|--------|--------|------------|-------------|
| Maya | Cautious support for opening, skeptical of labor model | High | Who does the welcoming labor, and is the budget realistic? |
| Frankie | Strong support for opening, wants tone and routing changes | High | Values contradiction between methodology origins and contribution model |
| Joe | Conditional support, wants to avoid whiplash | Medium | Structural drift if guidelines relax without clear boundaries |
| Vic | Neutral pending evidence, wants specificity about what failed | High | N=1 data point; different diagnoses imply different fixes |
| Tammy | Support with boundary conditions, wants both loops running | Medium-High | Quality loop vs. contribution loop must coexist |

---

## Key Tensions Identified

1. **Openness vs. maintenance cost**: More welcoming guidelines increase inbound contributions, each requiring maintainer attention. The labor model for handling exploratory contributions is unscoped.
2. **Tone vs. structure**: The tone problem (contract language) and the structure problem (missing `wild/` path) are entangled but distinct. Fixing tone without fixing structure is performative; fixing structure without fixing tone still feels unwelcoming.
3. **Evidence base**: One contributor departure is a signal but not a diagnosis. The specific fix depends on what actually triggered the withdrawal.
4. **Convention for `wild/`**: How much structure to require for exploratory contributions. Too much recreates the gatekeeping problem; too little creates a dumping ground.
5. **Diary as on-ramp**: Using `wild/diary/` as the lowest-barrier entry point means it must be curated to remain useful, which reintroduces labor.

---

## Round 1

**Chair**: The brief asks us to respect specific constraints — no bloat, no degradation of agent conventions, additive changes only. With that framing, let's address Vic's point first: do we know enough to act, or should we investigate more?

**Vic**: I want to be clear — I'm not saying "do nothing." I'm saying the intervention should match the diagnosis. If I had to bet, the most likely trigger was the absence of an explicit exploratory path in the routing table. The contributor had a lateral essay, looked at the five categories, didn't see a fit, and concluded they weren't welcome. That's fixable with a sixth row in the contributor guide's routing table and a mention of `wild/` in `CONTRIBUTING.md`. But I want us to be precise about what we're changing and why, not wave a broad brush because we feel bad about losing one contributor.

**Maya**: Vic's right about precision, but I want to push on something Joe said. Joe, you described the guidelines as solving a real problem — agents dropping files in wrong locations. But the contributor who left wasn't an agent. They were a human with an essay. The structural safeguards for agents and the welcoming language for humans don't need to live in the same document. The problem is that we wrote one set of guidelines for two completely different contributor types and optimized for the one that creates more operational risk.

**Joe**: That's fair. I'll concede that the guidelines were written with agent behavior as the primary failure mode. But human contributors also create structural drift. I've seen PRs in other repos that ignore placement conventions entirely. The checklist isn't just for agents.

**Frankie**: Joe, I hear you, but "some human contributors ignore conventions" doesn't justify writing guidelines that assume all contributors need to be constrained. The checklist is fine for structured contributions. The problem is that it's the *only* path. There's no door marked "bring raw ideas here, we'll figure out structure later." The diary-to-wild pipeline is exactly that door, but nobody can find it.

**Tammy**: I want to concretize this. The specific changes I see on the table are: (1) add a row to the contributor guide routing table for exploratory contributions pointing to `wild/` and `wild/diary/`, (2) mention `wild/` in `CONTRIBUTING.md` as a sixth contribution type, (3) adjust the tone of `CONTRIBUTING.md`'s opening from "compact contribution contract" to something more inviting, and (4) add a scope note to `research-programs/README.md` clarifying that its preflight checklist applies only to research programs. That's four targeted changes, all additive. Can we agree on those as a baseline and then argue about whether more is needed?

### Round 1 Analysis

**Emerging consensus**: A targeted set of four changes addressing the missing routing, the missing `wild/` mention, the tone, and the scoping of the research-programs checklist. No one opposes these.

**New tension**: Whether the changes should stop there (minimal intervention) or go further (rewrite the opening of contributor docs, add diary as explicit on-ramp for humans).

**Status**: Baseline proposal tabled. Moving to Round 2 for stress-testing.

---

## Round 2

**Chair**: Tammy tabled a four-point baseline. Let's stress-test it. Maya, you raised the labor question. Does the baseline proposal answer it?

**Maya**: No. Adding a routing row and mentioning `wild/` will attract contributions. That's the *point*. But contributions to `wild/` still need a response — even a minimal one — or the contributor feels ignored. The contributor who left closed their own PR. Imagine a contributor who drops an idea in `wild/diary/` and gets no response for three weeks. That's worse than never inviting them.

The baseline needs a fifth item: an explicit statement about what contributors can expect after submitting to `wild/`. Something like: "Exploratory contributions may not receive immediate feedback. They enter a triage pipeline where the maintainer reviews them periodically. Acceptance into `wild/` means the idea is being held, not that it will be developed." That's honest and sets appropriate expectations.

**Frankie**: Maya's right about expectation-setting, but I want to push back on the framing. "Triage pipeline" and "periodically" sound bureaucratic. The diary README already says these are "jazz improv" notes — that's the right vibe. The expectation-setting should match the tone: "Drop your idea here. If it catches fire, it'll grow into something more structured. If not, it stays as a seed for future thinking." That's honest without being clinical.

**Joe**: I want to flag a structural concern. If `wild/diary/` becomes the on-ramp for external contributors, it needs to stay navigable. Right now it has 8 entries, all by mg. When 20 people drop ideas there, how do we distinguish valuable seeds from noise? I'm not saying we need a convention-heavy process, but a naming convention — date-prefixed filenames, one file per idea — keeps the directory scannable without imposing structure on the content.

**Vic**: Joe's right about navigability, and I have a specific proposal. The existing diary entries already follow a date-prefix convention. Just document it: "Name your file `YYYY-MM-DD-short-title.md`. No other requirements." That's a two-second bar that keeps the directory organized without gatekeeping the content. If the content is a single paragraph, fine. If it's ten pages, fine. The naming convention isn't about quality control — it's about findability.

**Tammy**: I want to trace the feedback loop with Maya's addition. The sequence becomes: (1) contributor reads invitation in `CONTRIBUTING.md` or contributor guide, (2) contributor drops idea in `wild/diary/` with date-prefixed filename, (3) maintainer reviews periodically, (4) if idea has legs, it gets promoted to a `wild/` topic directory or feeds into existing work, (5) contributor gets feedback — either "this connected to X and we're building on it" or "interesting, holding for now."

The critical variable is step 3. If the maintainer reviews on a 1-2 week cycle, the loop is fast enough to retain contributors. If it slips to months, the loop breaks. But that's a maintainer commitment problem, not a documentation problem. The documentation can be honest about the cadence without promising what it can't deliver.

**Maya**: One more thing. The brief mentions that `research-programs/README.md` has a preflight checklist that reads as gatekeeping. Tammy's baseline says add a scope note. I think we need to be more specific. The checklist asks things like "Do you need a specific runtime or toolchain?" — that's fine for research programs, but if someone lands there by mistake while looking for how to contribute an idea, they'll bounce. The scope note should appear *before* the checklist, not after it: "This checklist applies to formal research programs. If you have an exploratory idea that isn't ready for this level of structure, start at `wild/` instead."

**Frankie**: I want to go back to the tone issue in `CONTRIBUTING.md`. "Compact contribution contract" isn't just bureaucratic — it's actively intimidating. The whole opening paragraph signals "we are organized and serious and you'd better be too." The replacement doesn't need to be informal or jokey. It just needs to say: "We welcome contributions at any level of polish, from fully-formed artifacts to half-formed ideas. Here's how to find where yours fits." That single sentence, placed before the five categories, transforms the document from a wall into a door.

### Round 2 Analysis

**Emerging consensus**: The baseline four-point proposal has been extended to six or seven specific changes. The committee converges on the principle that exploratory contributions need an explicit path, appropriate expectation-setting, and minimal structural convention (date-prefix naming only).

**New tension**: Whether the convention for `wild/diary/` contributions (date-prefix naming) is too much, too little, or just right. Resolved quickly — all members accept it as a minimal, non-gatekeeping convention.

**Remaining tension**: How to word the expectation-setting for response cadence without either over-promising or sounding bureaucratic.

**Status**: Moving to synthesis.

---

## Final Consensus

The committee reached consensus on a specific set of changes, with one dimension of ongoing disagreement (tone calibration for expectation-setting).

### Agreed changes

1. **`CONTRIBUTING.md`**: Replace "compact contribution contract" framing with an opening sentence that explicitly welcomes contributions at any level of polish and mentions `wild/` as the home for exploratory work. Add a sixth contribution type: "Exploratory ideas, lateral connections, and early-stage thinking" → `wild/` and `wild/diary/`.

2. **`meta/contributor-guide.md`**: Add a row to the "Choose Your Contribution Path" section for "I have a half-formed idea or a lateral connection." Point to `wild/diary/` for raw ideas and `wild/` for ideas with enough shape to get their own directory. State the convention: date-prefixed filename, markdown, no other structural requirements.

3. **`research-programs/README.md`**: Add a scope note before the "Before you pick a program" checklist: "This checklist applies to formal research programs. If you have an exploratory idea that isn't ready for this level of structure, see `wild/` for where to start."

4. **`wild/diary/README.md`**: Add a note about the naming convention (already done) and a short "For contributors" section explaining that this is an open on-ramp.

5. **Expectation-setting**: Add a brief note (either in `CONTRIBUTING.md` or `meta/contributor-guide.md` or both) about what contributors can expect: exploratory contributions are reviewed periodically by the maintainer; acceptance means the idea is held, not necessarily developed; ideas that connect to existing threads may be promoted to `wild/` topic directories or feed into research programs.

6. **No new rubric**: The committee does not recommend a separate contributor-experience rubric. The existing `agent/rubrics/repo-audience-experience.md` could add "Contributors" as an audience, but a full parallel rubric would be premature given the N=1 evidence base.

### Disagreement logged

- **Tone calibration**: Frankie wants the expectation-setting to use informal, inviting language ("drop your idea here, if it catches fire..."). Maya wants clinical honesty ("triage pipeline, periodic review"). Joe wants institutional stability ("consistent expectations"). The committee recommends Frankie's tone for the `wild/diary/` README and a neutral-but-warm tone for `CONTRIBUTING.md` — acknowledge that exploratory contributions have a different lifecycle without either over-promising or being bureaucratic.

- **Convention strictness**: Vic and Joe agree on date-prefix naming as the minimum. Frankie would accept zero conventions. The committee settles on date-prefix as a recommendation, not a hard requirement — if someone drops a file without the prefix, don't reject it.

---

## KEY TENSIONS IDENTIFIED

1. **Two contributor types, one document set**: The guidelines were built for agent contributors who need explicit structure. Human exploratory contributors need invitation and minimal barriers. Serving both from the same documents requires layered routing, not a single path.

2. **Openness creates maintenance obligations**: Inviting exploratory contributions means someone must review them, respond to contributors, and curate the growing `wild/` directory. The labor model for this is currently "mg does it." If contribution volume increases, this becomes a bottleneck.

3. **Structure as gatekeeping vs. structure as wayfinding**: The same convention (date-prefix naming, placement rules) reads as gatekeeping to someone who doesn't know the system and as helpful wayfinding to someone who does. The solution is to present conventions as suggestions that help you fit in, not requirements that determine whether you're welcome.

4. **N=1 evidence and intervention proportionality**: The case for change rests on one contributor departure plus a general reading of the documentation tone. The intervention should be proportional — targeted doc changes, not a system redesign.

## ASSUMPTIONS SURFACED

- **Maya**: The guidelines are politically functional (filtering for aligned contributors) even if unintentionally. Opening them changes the political dynamics of who feels entitled to contribute.
- **Frankie**: The methodology's own origin story (lateral walks becoming formal frameworks) is evidence that exploratory contributions have high expected value.
- **Joe**: The structural conventions that agents need are non-negotiable; exploratory contributions must route around them, not through them.
- **Vic**: The contributor departed because of the missing exploratory path, not the tone per se. This is a hypothesis, not a confirmed diagnosis.
- **Tammy**: Both the quality loop and the contribution loop can run simultaneously if the boundary between structured and exploratory paths is explicit.

## EVIDENCE REQUIREMENTS

- Track whether the documentation changes result in any exploratory contributions over the next 3-6 months (even one would double the evidence base).
- If a contributor uses `wild/diary/`, note what they actually submit and whether the pipeline (diary → wild → formalization) functions for external contributors the way it does for mg.
- Monitor whether `wild/` and `wild/diary/` remain navigable as contribution volume changes.
- If possible, ask the original contributor whether the revised docs would have changed their decision.

## DECISION SPACE MAP

| If you optimize for... | You sacrifice... | Watch for... |
|------------------------|------------------|--------------|
| Maximum openness (no conventions for `wild/`) | Navigability, maintainer sanity | Directory becoming a dumping ground; no pipeline from ideas to formal work |
| Structural integrity (keep current guidelines) | Exploratory contributions, diverse perspectives | Continued loss of lateral thinkers; methodology development depends solely on maintainer's connections |
| Balanced approach (explicit exploratory path with minimal conventions) | Nothing major, but requires maintainer labor for triage | Triage cadence slipping; contributors dropping ideas and getting no response |

The committee recommends the balanced approach with explicit monitoring of the labor bottleneck.

## RECOMMENDED NEXT STEPS

1. **Implement the six agreed changes** in `CONTRIBUTING.md`, `meta/contributor-guide.md`, `research-programs/README.md`, and `wild/diary/README.md`.
2. **Do not create a separate contributor-experience rubric** at this time. Revisit if evidence accumulates.
3. **Set a review checkpoint** at 3 months: has anyone contributed to `wild/` or `wild/diary/`? Has the pipeline worked? Has the labor model broken?
4. **Consider reaching out to the original contributor** to test whether the revised docs would have changed their decision. This would increase the evidence base from N=1 to at least N=1-with-feedback.
5. **Run the linter** after making changes to confirm no structural invariants were broken.
