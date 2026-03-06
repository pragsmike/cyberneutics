# Phase 2: Deliberation

**Topic:** Should we keep and recommend the metacognition process (confidence at resolution, register, optional with-register runs, cumulative-confidence test) as a supported part of the methodology?

**Protocol:** Robert's Rules; adversarial exploration of decision space.

---

## Opening Statements

### Maya

I'm suspicious of anything that looks like rigor theater. We added confidence ratings, a register, a comparison test — but who actually uses this? The end user gets a resolution with votes and now a number from 1 to 4. Does that number change anyone's decision in practice? I've seen methodology projects pile on "quality signals" that look good in docs and never get used. The overhead is real: every committee run has to record confidence; someone has to remember to run the register script; the smoke test is two committee runs plus two reviews plus a compare script. That's a lot of process for a signal we haven't shown changes user behavior. I'm not saying remove it — I'm saying we should be honest that we're recommending an unvalidated add-on. Keep it optional, document it as experimental, and define a kill condition: if after N runs or 12 months we have no evidence users weight by calibration, we simplify or drop it.

### Frankie

The principle matters. The methodology says the user is the editor — they curate what gets published to reality. If we're serious about that, we owe them information that helps them curate. Confidence at resolution is exactly that: not "the committee said Aye" but "Maya said Aye and was highly confident; Joe said Nay and was low confidence." That's a better input to the user's decision. The register extends it across runs: "In past deliberations, when Vic was confident he was usually right; when Maya was confident she was often wrong." That's a veracity signal. Keeping it optional is fine — not everyone will run with-register — but we should *recommend* it as part of the methodology. The alternative is pretending the committee output is undifferentiated. We shouldn't pretend. If we keep it optional but clearly recommend it, we're being honest about what we think helps the user.

### Joe

We've been here before. We add a layer — evaluation rubrics, remediation rounds, scenario-aware mode — and each time we say "it's optional" or "it's just one more step." Then the docs multiply, the runbook gets longer, and new users hit a wall of "which of these do I actually need?" The metacog process is the same pattern. Confidence at resolution: one extra thing to record. Register: one more script to run. With-register mode: a second run per topic if you want to test it. I'm not against the idea — knowing who's been well-calibrated could help — but I want a clear default path. "Run committee, maybe review" should still be the default. Metacog should be "if you want to go further." And we need a sunset clause. If in six months we have three with-register comparisons and they're all null or negative, we deprecate the with-register flow and keep only confidence + register as a lightweight signal. Don't let this become permanent scaffolding without evidence.

### Vic

I need evidence. The artifact says metacognition helps the user "decide how to use the committee's advice." Where's the evidence? We have a comparison test: baseline vs with-register, review both, compare. That's the right design. But we've run it how many times? If we've run it once or twice, we have no idea if the register actually improves decisions or if we're fooling ourselves. I'm not voting to remove it — I'm voting to keep it *conditional*. Keep confidence at resolution and the register; they're low cost and at least give us data. Keep the comparison test as the way we *get* evidence. But don't recommend "with register" as default until we have, say, three or more comparison runs showing with-register ≥ baseline and calibration mentioned. Right now we're recommending a process we haven't validated. That's backwards. Recommend the minimal path; recommend the full metacog path only when we have positive signal.

### Tammy

The system we're changing is "user runs committee → gets advice → decides." Adding confidence and a register doesn't just add information; it changes what we're optimizing for. If characters know their confidence is being tracked and will show up in a register, do they game it? Do they understate confidence to look calibrated? More importantly: the user's decision is already influenced by who said what. Adding a number might make that influence more explicit, or it might give a false sense of precision — "Maya was 3, Joe was 2" — when the real signal is in the transcript. I'm worried about second-order effects: we're building a subsystem (register, with-register runs) that could become load-bearing in the docs even if the benefit is small. My position: keep confidence and register as optional, document them clearly, but don't make with-register a recommended default. Let the comparison test accumulate. If the data show a consistent benefit, we can upgrade the recommendation. If not, we've kept the option without overcommitting the methodology.

---

## Initial Positions Summary

| Member | Stance | Key concern |
|--------|--------|-------------|
| Maya | Keep optional; treat as experimental; define kill condition | Rigor theater; no evidence users use it |
| Frankie | Keep and recommend; principle of giving user a veracity signal | User deserves information to curate |
| Joe | Keep optional; protect default path; sunset clause if no benefit | Methodology bloat; we've added before and regretted it |
| Vic | Keep conditional on evidence; don't recommend with-register until 3+ positive comparisons | Backwards to recommend unvalidated process |
| Tammy | Keep optional; don't default to with-register; let data accumulate | Second-order effects; false precision; don't overcommit |

---

## Key Tensions Identified

1. **Recommend vs optional:** Frankie wants to recommend the full metacog path; Vic and Joe want recommendation only after evidence or never as default.
2. **User benefit assumed vs evidenced:** Maya and Vic question whether the user actually uses confidence/register; Frankie treats the principle as sufficient.
3. **Overhead vs signal:** Joe and Maya emphasize cost (script, two runs, docs); Frankie and Tammy accept cost if the signal is real.
4. **Default path:** Everyone agrees the minimal path (committee, maybe review) must stay; disagreement is whether "committee + confidence + register" or "committee + confidence + register + with-register" is ever the recommended path.

---

## Round 1

**Chair:** We have a split. Frankie wants to recommend; Vic wants evidence first; Joe wants a sunset clause; Maya wants a kill condition; Tammy wants to avoid overcommit. Vic — what would count as evidence that the user actually benefits?

**Vic:** The comparison test is the right design. Baseline vs with-register, same topic, both reviewed. We compare review sum and verdict, and we check whether the with-register run mentions calibration. If with-register consistently scores at least as high and the resolution or transcript references past calibration, that's evidence the process is being used and not harming quality. I'd want at least three such runs on different topics before we say "recommend with-register." For confidence and register alone — we're not asking the user to do much. Record confidence; run a script. The burden of proof is lower. We can recommend "record confidence and update the register" as good practice without waiting for with-register evidence.

**Frankie:** So you're willing to recommend confidence + register now, but not with-register until we have three positive comparisons?

**Vic:** Yes. Confidence and register are low cost and give the user a summary of who's been well-calibrated. That summary is available whether or not they run a second committee with the register. With-register is the heavier lift — two runs, two reviews, compare — and we're claiming it improves the synthesis. That claim needs data.

**Maya:** I'll push back. "Recommend confidence + register" still means we're telling users to run an extra script and to care about a file they might never look at. How many users will actually open the register? If it's zero, we're recommending busywork. I'd rather say: "We support confidence and a register; here's how. Use them if you're running multiple committees and want a calibration snapshot." Not "we recommend you do this."

**Tammy:** Maya's point is a systems point. If we recommend something, we're nudging the default. New users will think they're supposed to run the register. So the question is: do we want the default user to run it? I don't think we have evidence either way. So I'm with Vic on with-register — don't recommend until we have runs. On confidence + register: I'm okay recommending "record confidence" because the committee skill already does it; the marginal cost is zero. Recommending "run the register script after each run" is a bigger nudge. I'd document it as supported and useful-if-you-run-many-committees, not as standard practice.

**Joe:** So we're converging on: keep it all, support it in docs, but tier the recommendation. Confidence at resolution — we already record it; call it recommended or at least default in the skill. Register — document it, say "run this if you want a cross-run calibration snapshot." With-register runs and the comparison test — document as "how to test whether the register helps," and don't recommend with-register as something every user should do until we have evidence. And we add a sunset or review clause: in X months or after Y comparison runs, we revisit whether with-register stays in the methodology or gets demoted to experimental only.

---

## Round 2

**Chair:** Joe proposed a tiered recommendation and a revisit clause. Frankie, does that satisfy "we recommend the metacog process"?

**Frankie:** Partially. I'm fine with tiering. Recommend confidence at resolution — yes, we're already doing it. Register — I'm okay with "recommended when you run multiple committees" rather than "every time." With-register — I can live with "supported, test it and see" until we have more comparison runs. What I don't want is us saying "this is experimental, might remove later" in a way that signals we don't believe in it. We added it because we think it helps the user. We should say that. The revisit is "we'll check if the evidence supports that"; not "we're not sure it's worth having."

**Vic:** I'm fine with that framing. We believe it could help; we're gathering evidence; we'll revisit. That's honest.

**Maya:** I want the kill condition written down. Not just "revisit" but "if after N comparison runs we see no positive signal, we simplify: drop with-register from the recommended path and consider whether the register script stays or becomes optional-only." So we're not just adding and never subtracting.

**Tammy:** Seconded. Sunset clause: e.g. "After 12 months or 5 comparison runs, if with-register has not shown consistent benefit (e.g. ≥3 runs with with-register ≥ baseline and calibration mentioned), we deprecate with-register as a recommended option and document only confidence + register." That gives us an exit.

**Joe:** I'll support that. And in the implementation plan we say: keep and recommend confidence at resolution; document register and when to use it; document with-register and the comparison test as the way to test; add the sunset/review clause to the artifact or run guide.

---

## Round 2 Analysis

- **Emerging consensus:** Keep the full metacog process; tier the recommendation (confidence recommended, register when running many committees, with-register supported but not default until evidence); add a sunset/review clause.
- **Remaining tension:** Wording of "recommend" — Frankie wants clear belief that it helps; Maya wants clear exit if it doesn't.
- **Next:** Synthesize resolution and implementation plan.

---

## Final Consensus

- **Keep** confidence at resolution, register, with-register mode, and the cumulative-confidence comparison test as supported parts of the methodology.
- **Recommend** confidence at resolution (already default in skill); **recommend** running the register when the user runs multiple committees and wants a calibration snapshot; **support** with-register and the comparison test as the way to test whether the register helps, without recommending with-register as default until we have more comparison evidence.
- **Add** a review/sunset clause: after a defined period or number of comparison runs, if with-register has not shown consistent benefit, deprecate it as a recommended option and simplify docs to confidence + register only.
- **Document** clearly what the user gets and when (resolution table in metacognition artifact); keep overhead and optional-vs-default explicit.

**Status:** DELIBERATION COMPLETE.

---

## KEY TENSIONS IDENTIFIED

- **Recommend vs evidence:** Recommend confidence + register now; don't recommend with-register as default until we have 3+ comparison runs showing benefit.
- **Principle vs proof:** Frankie: user deserves the signal; Vic/Maya: we need evidence they use it.
- **Exit condition:** All agree on a sunset/review clause so we can simplify if the process doesn't pay off.

## ASSUMPTIONS SURFACED

- The comparison test (baseline vs with-register, review both, compare) is the right way to get evidence.
- "Recommend" tiers: confidence = recommended; register = recommended when running many committees; with-register = supported, not default until evidence.
- Methodology bloat is a risk; default path must stay simple (committee, maybe review).

## EVIDENCE REQUIREMENTS

- More comparison runs (different topics) to test whether with-register consistently matches or beats baseline and mentions calibration.
- Optional: user interviews or feedback on whether they use the register or confidence when deciding.

## DECISION SPACE MAP

- **If we optimize for "user gets best signal"** → recommend full metacog path; accept overhead and doc complexity.
- **If we optimize for "don't overcommit without evidence"** → tier recommendation, sunset clause, keep with-register as supported-but-not-default.
- **If we optimize for "minimal default"** → confidence + register documented as optional only; no "recommend" language.
- Committee landed on the middle: recommend confidence and register (tiered), support with-register, add exit.

## RECOMMENDED NEXT STEPS

- Update metacognition and cumulative-confidence-smoke-test artifacts to state the tiered recommendation and the review/sunset clause.
- Run 2–3 more comparison tests on new topics; log results (e.g. cumulative_confidence_smoke_log.md).
- At 12 months or 5 comparison runs, revisit: if with-register has not shown consistent benefit, deprecate it from recommended path.

---

## Response to evaluation (motion to recommit)

The independent review (04-evaluation-1.md) scored the deliberation 11/15 and identified three gaps: (1) the link between review score and user benefit is assumed, not stated; (2) Maya's question "who opens the register?" was left unanswered; (3) the sunset clause could be one unambiguous sentence. The committee reconvenes to address these.

---

## Round 3: Metacog process — addressing evaluation

**Chair:** We've received an independent evaluation. Sum 11, below our threshold. Three recommendations: state explicitly that review sum and calibration-mentioned are proxies for user benefit; answer the register-usage question; tighten the sunset to one sentence. I'm treating this as a motion to recommit. We'll take each in order.

**Vic:** I'll state the proxy assumption. We're using review rubric sum and "calibration mentioned in the resolution or transcript" as *proxies* for "the user benefits." We have not validated that. We don't have a direct measure of whether the end user makes better decisions when they get a with-register run. So for the sunset, "no consistent benefit" means: these proxies don't improve — we don't see with-register ≥ baseline and calibration mentioned in at least three of five runs. If we ever get user feedback or a better outcome measure, we can tighten the claim. I move we add this to the implementation plan and to the artifacts: "We assume review sum and calibration-mentioned are proxies for user benefit; this assumption is not yet validated; the sunset treats no improvement in these proxies as grounds to deprecate with-register."

**Maya:** I support that. It's what I was pushing for — we're not claiming we've proved user benefit, we're claiming we have a testable process and an exit if the process doesn't show signal.

**Chair:** Seconded. Anyone want to amend?

**Frankie:** I'll take the register question. We don't have data on how many users open the register. I'm not claiming every user reads it. The register does two things: it's an *input* to the with-register committee run — the skill reads it and injects it into the charter — and it's there for maintainers or anyone running multiple committees who want a calibration snapshot. So "who opens the register?" — the with-register run "opens" it programmatically; beyond that we don't know. I move we add to the resolution: "Register usage by end users is unknown; we assume the primary consumers are the with-register committee run and maintainers; the sunset review will consider whether there is evidence of broader use, and if not, we may simplify to confidence-only or document register as maintainer-only."

**Joe:** That works. We're not overclaiming. We're saying: here's what we know, here's what we don't know, here's when we'll revisit.

**Tammy:** For the sunset, I'll make it one sentence so there's no ambiguity. Move: "Deprecate with-register if fewer than 3 of the first 5 comparison runs show with-register ≥ baseline AND calibration mentioned in the resolution or transcript." So we run five comparison tests; we need at least three where with-register's review sum is at least the baseline's and the with-register run mentions calibration. If we get fewer than three, we deprecate. Time trigger stays: or after 12 months, whichever comes first.

**Vic:** Seconded. That's falsifiable. We can check after five runs.

**Chair:** All three motions are accepted. We'll update the resolution to include: (1) the proxy assumption in the implementation plan or summary; (2) the register-usage assumption; (3) the one-sentence sunset trigger. Any objection? … None. Round 3 complete. Resolution will be updated accordingly.

---

## Round 3 Analysis

- **Additions:** Explicit proxy assumption (review sum and calibration-mentioned are unvalidated proxies for user benefit; sunset uses them as the criterion). Register usage: unknown; primary consumers are with-register run and maintainers; sunset review will consider evidence of use. Sunset trigger: "Deprecate if fewer than 3 of the first 5 comparison runs show with-register ≥ baseline AND calibration mentioned."
- **Resolution update:** 03-resolution.md will be updated to reflect these three additions.
