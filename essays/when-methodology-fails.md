# When This Methodology Fails

> "A methodology that only tells you about its successes is marketing. This essay is engineering."

## The story you should worry about

You run `/scenarios` on a staffing decision. Four scenarios fan out — plausible, specific, internally consistent. You feed them into `/committee`. Maya raises political concerns. Vic demands evidence. Tammy traces feedback loops. After three rounds of structured debate, the committee resolves unanimously: promote the internal candidate, with a retention package as insurance against the Disruption scenario.

The resolution scores 13/15 on independent evaluation. Reasoning chains complete. Assumptions surfaced. Trade-offs explicit.

You promote the internal candidate. Three months later, you realize the actual problem was that the role shouldn't have existed at all. The team needed restructuring, not a new lead. The committee debated *who should fill the role* with impressive rigor — and never questioned whether the role was the right intervention. Neither did you. The pipeline's formal machinery made the wrong question look thoroughly analyzed.

This is what failure looks like. Not a crash. Not an obviously bad output. A confident, well-scored, traceable answer to the wrong question.

---

## Why this essay exists

The [adoption strategy committee](../examples/deliberations/methodology-adoption-strategy/02-deliberation.md) identified this essay as one of four robust actions — Maya argued it was "the single most credibility-building thing the project could produce." She was right.

Every methodology has a failure envelope. Knowing where the boundary is lets you work near it safely instead of accidentally crossing it. This essay maps that boundary for cyberneutics — not to undermine the methodology, but because understanding *where* a tool breaks is what distinguishes engineering from salesmanship.

A caveat before we begin: these are largely *predicted* failure modes, not empirically documented ones. The methodology is young. The committee runs in this repository are largely self-referential (the methodology evaluating itself). No practitioner has yet reported "I followed the process and it failed in this specific way." These failure modes are derived from the methodology's theoretical structure, from known LLM limitations, and from what happened to other methodologies with similar designs. They are a safety manual written before the accidents, not an accident report. As empirical failure cases accumulate, this essay should be updated to distinguish prediction from observation.

One partial exception: the [Phase A targeted reframing probe](../research-programs/evaluating-deliberative-architectures/results/phase-a-results.md) (2026-03-20) tested whether committee deliberation surfaces conceptual reframing that an effort-matched single AI misses. It returned a null result — the committee moved closer to a target insight but didn't reliably get there. This is relevant to Failure Modes 2 and 6: the committee characters may produce the *genre* of adversarial reframing without completing the actual conceptual move, and the methodology's self-evaluation (the committee deliberating on its own experimental design) produced the experiment that yielded the null. See [The test](#the-test) at the end of this essay.

The failure modes below are organized by root cause, not severity. Each has: a concrete scenario, the mechanism that produces the failure, observable signs that it's happening, and what to do about it. Where a failure mode connects to the theoretical foundations, that connection is made explicit — because the point isn't just "things go wrong" but "here is which load-bearing theoretical claim is failing and why."

---

## Failure Mode 1: The problem doesn't warrant this treatment

### The scenario

A developer asks the committee whether to use PostgreSQL or MySQL for a new microservice. Maya warns about vendor lock-in politics. Frankie insists on open-source values. Joe cites a 2019 migration disaster. Vic demands benchmarks. Tammy traces coupling feedback loops. The committee produces a rich, adversarial transcript.

The right answer was: check the company's existing infrastructure, pick whichever the team already knows, and move on. The problem was *complicated* (many factors) but not *complex* (no genuine uncertainty, no competing values, no hidden assumptions that change the answer). Thirty seconds of fact-gathering would have resolved it. Instead, the methodology spent its entire machinery exploring a decision space that didn't exist.

### The mechanism

The methodology is designed for wicked problems — situations where the question isn't "what's right?" but "what are we missing?" (The committee artifact [opens with this claim](../artifacts/adversarial-committees.md).) But narrative engines are happy to generate competing perspectives on *anything*. Give five characters any topic and they will produce five distinct takes, complete with tensions, trade-offs, and surfaced assumptions. The machinery doesn't know the difference between genuine complexity and manufactured complexity. It treats everything as if the decision space is rich enough to explore.

This connects to a specific theoretical claim: repetition produces difference (Essay 06, the Deleuzian foundation). When the underlying decision space is genuinely multidimensional, that difference is *signal* — each run reveals new territory. When the space is simple, the difference is *noise* — the pipeline generates apparent complexity from stochastic variation, not from genuine latent structure. The Deleuzian claim holds, but its *usefulness* depends on whether there was a meaningful virtual field to actualize in the first place.

### How to detect it

- **The resolution closely mirrors the initial framing.** If the committee's output is essentially "the answer that was obvious before we started, but with more words around it," the pipeline added ceremony, not insight.
- **Nothing surprised you.** The [surprise heuristic](../artifacts/troubleshooting.md) from the troubleshooting guide applies here: if no committee member said anything you hadn't already considered, the methodology didn't earn its cost.
- **The committee argued about dimensions that don't affect the decision.** If Maya's political analysis and Tammy's systems thinking both point to the same action, the adversarial tension was real but irrelevant — the problem didn't have enough degrees of freedom for the tension to matter.
- **A domain expert could have answered this in five minutes.** The methodology is a substitute for *missing perspectives*, not for *missing facts*. If the problem's difficulty comes from not knowing something that's knowable through direct inquiry, look it up.

### What to do

**Before running the pipeline**, ask: *Is the difficulty here about complexity (competing values, hidden assumptions, genuine uncertainty about what could happen) or about complication (many moving parts but knowable through research)?* If complicated, skip the committee. Use it as a checklist: have I considered politics (Maya's domain), values (Frankie's), history (Joe's), evidence (Vic's), systems effects (Tammy's)? A quick mental pass through the propensities, without the full pipeline, captures 80% of the value at 5% of the cost.

**If you realize mid-run that the problem is simpler than you thought**: that's actually a success — the methodology helped you see the problem more clearly. Stop the pipeline, act on what you now understand, and note what made the problem seem more complex than it was.

Note that even in this failure mode, the committee produced an inspectable record of the reasoning that led to the (unnecessary) analysis. Whether this record has archival or training value — showing *why* the team initially thought the problem was complex — is a separate question from whether the decision needed the methodology.

---

## Failure Mode 2: The committee characters don't deliver on their epistemic promise

### The scenario

You run `/committee` on a genuinely complex problem — an organizational restructuring with real competing values. The transcript looks right: Maya raises political concerns, Frankie defends the mission, Joe cites precedent, Vic demands evidence, Tammy traces loops. But when you read closely, every character is speaking in the same cadence. Maya's "paranoid realism" is a polite observation about stakeholder dynamics, not a genuine accusation of bad faith. Vic "demands evidence" by saying "we would need more data here" without specifying what data or what would change if we had it. The characters are hitting their marks superficially — recognizable propensities without novel insight.

### The mechanism

All five characters are generated by the same model from the same weights. The model has been trained through RLHF to be helpful, harmless, and honest — which creates a strong prior toward diplomatic synthesis. When instructed to roleplay an adversarial character, the model must overcome its training distribution to produce genuinely hostile cross-examination. Sometimes it does. Sometimes it produces *the genre of adversarial debate* — text that reads like hostile cross-examination in the same way that a TV courtroom drama reads like a trial.

This is the distinction between [narrative computing and narrative engineering](./07-bolands-narrative-engineering.md): the primitive (generating a narrative) is working correctly — the model produces text in the genre of adversarial debate. The *engineering* claim is that this genre-appropriate text, composed with forcing functions and independent evaluation, produces reliable outputs. That claim fails when the genre mimicry is shallow enough that the forcing functions can't compensate.

Four specific sub-failures:

**Voice collapse.** All characters converge to "helpful AI assistant" register. This is the [Bland Corporation](../artifacts/troubleshooting.md) problem — the model's RLHF training overwhelms the character instructions. Detection: characters start sentences with "It's important to consider..." regardless of propensity. Characters defer to each other ("Maya raises a good point, but...") instead of attacking.

**Shallow roleplaying.** Characters hit propensity marks without going deeper. Maya says something cynical, but her cynicism is generic rather than specific to the problem's actual political landscape. Vic demands evidence, but doesn't specify what evidence would change what conclusion. The propensities are templates, not lenses. Detection: you could swap the character names without changing the substance. Each character's contribution could have been generated by a generic "consider this angle" prompt.

**Sycophantic convergence.** Despite adversarial instructions, the committee reaches consensus within two rounds. The model's prior toward synthesis (finding the answer that satisfies all constraints) overwhelms the adversarial structure. This is the [Echo Chamber](../artifacts/troubleshooting.md) failure. Detection: unanimous or near-unanimous votes on the first motion. No character maintains an objection through to the final resolution. The resolution is a "balance everyone wins" synthesis rather than an explicit trade-off.

**Pattern-matching without domain knowledge.** The committee argues well within what the training data covers — organizational politics, strategic trade-offs, evidence standards. But for *your specific context* — your organization's actual power dynamics, your team's actual capabilities, your market's actual constraints — the characters can only pattern-match to similar-seeming situations from the training corpus. The analysis is *plausible-sounding but not actually about your situation*. This is the most dangerous sub-failure because it's the hardest to detect from inside the transcript. Detection: the committee's analysis would apply equally well to a dozen different organizations. Character references to "your situation" are generic enough to be true of anyone.

### What to do

**For voice collapse and shallow roleplaying**: the [troubleshooting guide](../artifacts/troubleshooting.md) covers remedies — increase temperature, force conflict via chair instructions, add negative constraints ("Do not start sentences with 'It's important'"), use script formatting. If these don't work, the model may not be capable of the character differentiation this run requires. Accept the limitation and treat the output as a structured brainstorm rather than adversarial deliberation.

**For sycophantic convergence**: require the Chair to reject the first motion. Add a structural constraint: "No vote may be called until at least one character has maintained an objection for a full round." If convergence still happens too quickly, that's informative — either the problem really does have an obvious answer (see Failure Mode 1) or the model can't generate genuine disagreement on this topic.

**For pattern-matching without domain knowledge**: **this is where the user's editorial role is most critical.** The committee can't know what it doesn't know. Inject domain-specific context directly: "Note: in our organization, the CTO and VP Engineering have a documented rivalry. The previous restructuring in Q2 2024 was blocked by the board." The more specific context you provide, the less the committee relies on generic pattern-matching. If you can't articulate what's specific about your situation, that's a sign you may not have the domain knowledge to evaluate the committee's output — which means you shouldn't trust it.

**An operational note**: Model capabilities change over time. Models get updated, retrained, fine-tuned, or replaced. Character calibration developed with one model version may not hold with the next. If the committee suddenly stops producing distinctive voices after a model update, the calibration may need re-testing — the roster's examples document what good and bad character behavior looks like, and those examples serve as regression tests.

---

## Failure Mode 3: The evaluation loop doesn't escape the hermeneutic circle

### The scenario

You run a committee deliberation, then pass it to `/review`. The independent evaluator scores it 13/15. You trust the score — after all, independent evaluation is supposed to [break the hermeneutic circle](../artifacts/independent-evaluation.md). But the evaluator is a different instance of the same model, trained on the same data, with the same systematic blind spots. It evaluates *formal properties* — were reasoning chains complete? were assumptions surfaced? — not *substantive correctness*. The committee produced a beautifully reasoned argument for a strategy that depends on an assumption about your market that the model has no way to verify.

### The mechanism

Independent evaluation is [positioned as the solution to self-confirming narratives](../artifacts/independent-evaluation.md): "Taking the output... passing it to a completely separate model instance... with no conversation history." This genuinely helps — a fresh instance without the generation context does catch formal deficiencies that the generating instance is blind to. The rubrics (reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness) are well-designed measures of *deliberation quality*.

But they are measures of *quality of reasoning*, not *correctness of conclusion*. A transcript can score 3/3 on every rubric and still be wrong, because:

- **Shared training distribution**: Both generator and evaluator inherit the same biases from training data. If the training corpus systematically overrepresents certain organizational patterns, both instances will treat those patterns as default. The evaluator can't catch a bias it shares.
- **Formal vs. substantive evaluation**: The rubrics check whether claims were challenged, evidence was demanded, and trade-offs were named. They don't check whether the claimed evidence is actually true, whether the named trade-offs are the real ones, or whether the entire framing is appropriate. Substantive evaluation requires domain knowledge the model may not have.
- **Confidence theater**: A score of 13/15 *feels* like calibrated quality assessment. But the score measures adherence to process norms, not predictive accuracy. There is currently no empirical data linking rubric scores to outcome quality — no study showing that deliberations scoring 13/15 produce better decisions than those scoring 9/15.

This is where the [confidence propagation rule](../palgebra/reference.md) — "confidence can only degrade through a pipeline" — applies in a way the formalism doesn't explicitly address. The rule says downstream operations can't increase confidence. But the evaluation enrichment *appears* to increase confidence by providing a quality score. The rubric score is confidence *about the process*, not confidence *about the conclusion*. Conflating the two is the specific error.

### How to detect it

- **The evaluation never flags substantive concerns.** If every evaluation comment is about formal properties ("reasoning chain could be more explicit at step 3") and never about content ("the assumption that market X is growing contradicts public data"), the evaluator is doing formal audit, not substantive review.
- **Scores are consistently high.** If your deliberations routinely score 12-15/15, either you're very good at this or the evaluator isn't adversarial enough. Consistency in high scores should prompt *skepticism*, not satisfaction.
- **The evaluation could apply to a different transcript on a different topic.** If the feedback is generic enough to describe any well-structured debate, it's measuring structure, not substance.

### What to do

**Augment formal evaluation with domain expertise.** The independent evaluator is good at formal quality. It is not a substitute for someone who knows the domain. For high-stakes decisions, have a human domain expert read the transcript — not to evaluate its structure, but to evaluate its *premises*. "The committee assumed the market is growing. Is it?"

**Treat rubric scores as necessary but not sufficient.** A score of 13/15 means the deliberation process was rigorous. It does not mean the conclusion is correct. Low scores are informative (something went wrong with the process). High scores are necessary but not conclusive.

**Track outcomes over time.** The strongest evidence for whether rubric scores predict decision quality is a track record: did high-scoring deliberations lead to better outcomes than low-scoring ones? Until that data exists, the scores are a measure of process compliance, not quality assurance.

---

## Failure Mode 4: The user abdicates the editorial role

### The scenario

A team lead adopts the methodology for quarterly planning. They run `/scenarios` and `/committee` diligently. The committee produces a well-scored resolution recommending Strategy A. The team lead implements Strategy A. Next quarter, same process, new strategy. After six months, a colleague asks why the team's direction keeps shifting. The team lead says, "That's what the committee recommended."

The user has outsourced judgment to the pipeline. The methodology — which [explicitly positions the user as editor](../essays/04-cybernetics-and-observation.md) who "collapses the potential by choosing one interpretation, based on what you value" — has become a black box that produces decisions.

### The mechanism

The pipeline's formal machinery creates powerful institutional pressure toward trust. A decision backed by a five-person committee, structured debate, independent evaluation, and a rubric score of 13/15 has *the appearance of rigor*. Challenging it requires challenging the process, which feels like challenging expertise.

Three sub-failures:

**Over-trust in process.** The methodology *looks* rigorous — multiple perspectives, adversarial debate, independent evaluation, formal scoring. A user who trusts the process stops exercising judgment. The methodology becomes a substitute for thinking rather than a tool for thinking better. This is the most dangerous failure mode in this essay because it's invisible from inside and gets worse with experience. The better the methodology works, the more the user trusts it, the less they engage critically with outputs.

**Asymmetric power.** When someone in authority uses the committee's output to justify a decision, the methodology's formal apparatus creates a power asymmetry. A subordinate who disagrees must now challenge not just the boss's judgment but a five-person committee, independent evaluation, and rubric scores. "I ran the committee and it agreed with me" is a more powerful rhetorical weapon than "I think we should do X." The methodology can be weaponized — not by design, but because formal processes always advantage the person who controls them.

**Confirmation bias amplification.** The committee produces five perspectives. The user selectively attends to the one that validates their prior view. "Maya agrees with what I was already thinking" becomes the takeaway, not "Frankie and Tammy raised concerns I need to address." The methodology generated genuine cognitive diversity, but the user consumed it selectively.

**Rubber-stamping resolutions.** The committee produces a single resolution with votes and rationale. The user's editorial step — which should be the moment of genuine human judgment — becomes approval of whatever the committee decided. Especially when the resolution is unanimous. Especially when the rubric scores are high. Especially when you're busy.

### How to detect it

- **You can't articulate why you disagree with the committee on anything.** If you've accepted every resolution for the past N runs without pushback, either you're selecting only easy problems or you've stopped reading critically.
- **The resolution is your first draft's action plan.** If the committee consistently recommends what you were going to do anyway, the pipeline is confirming rather than challenging. (This could mean you're good at anticipating the analysis — or it could mean the framing you provided already contained the answer and the committee elaborated rather than questioned.)
- **You defend decisions by citing the process.** "The committee said X" is not a reason. "The committee surfaced these tensions, I weighed them like this, and I chose X because of Y" is a reason.

### What to do

**Mandatory dissent exercise.** After reading a resolution, *before accepting it*, articulate at least one reason to reject it. If you can't find one, that's a signal — either the resolution is genuinely obvious (and didn't need the committee — see Failure Mode 1) or you're not engaging critically.

**Track your override rate.** A healthy override rate is 10–30% — you should disagree with or significantly modify the committee's recommendation roughly one time in four. If your override rate is 0%, you're rubber-stamping. If it's above 50%, the committee isn't calibrated to your context.

**Name your editorial judgment in the resolution.** When you accept a resolution, annotate it: "I accepted this because [your reasoning]. The committee's argument about X was decisive. I'm discounting Y because [reason]." This forces the editorial step to be substantive, not procedural.

---

## Failure Mode 5: Garbage in, sophisticated garbage out

### The scenario

A CEO frames the problem for the committee as: "Should we pivot to enterprise or stay consumer?" The committee deliberates brilliantly across this binary. Maya analyzes the political implications of each path. Vic demands revenue data. The resolution recommends enterprise with a consumer maintenance strategy.

Six months later, the company fails — not because enterprise was wrong, but because the real problem was product-market fit in *both* segments. The CEO's binary framing excluded the possibility that the product was wrong, not the market. The committee explored the decision space thoroughly... but it was the wrong decision space. The [confidence propagation rule](../palgebra/reference.md) says quality can't be added downstream. The framing is the furthest upstream element.

### The mechanism

The committee deliberates *within the problem as framed*. It surfaces assumptions within that frame — "you're assuming enterprise customers want the same product" — but it has a structural bias toward accepting the frame itself. The charter says "deliberate on X" and the committee deliberates on X, not on "should we be deliberating on X?"

Scenario generation (the fan) is supposed to mitigate this — the four lenses (Continuity, Disruption, Opportunity, Constraint) should surface framings the user didn't consider. But the scenarios inherit the situation description as their starting point. If the situation description embeds an assumption ("we need to choose between enterprise and consumer"), the scenarios explore different futures *within* that assumption.

This is the pipeline's garbage-in problem dressed in formal clothes. The more rigorous the downstream processing, the more trustworthy the output *appears*, and the harder it becomes to notice that the input was wrong. Formal machinery can make a thorough analysis of the wrong question look better than an informal analysis of the right one.

### How to detect it

- **The committee never questions the framing.** If all five characters accept the problem as stated and debate within it, the framing is either genuinely appropriate or it's an unexamined assumption. Distinguish these by asking: "Could this problem be stated differently? Would a different framing change the analysis?"
- **The scenarios all explore variations of the same theme.** If all four scenarios are versions of "enterprise works / enterprise doesn't work / consumer works / consumer doesn't work," the fan didn't diverge — it permuted within the user's binary frame.
- **Someone outside the process is confused by the question.** The "explain this to a colleague" test: if an outsider hears the committee's framing and says "but isn't the real question...?" — listen.

### What to do

**Pre-frame the framing.** Before running the pipeline, spend five minutes asking: "What problem am I actually trying to solve? What would a different framing look like? What am I assuming by framing it this way?" Write down the framing *and* at least one alternative framing.

**Add a frame-challenge step.** After drafting the situation description for `/scenarios`, ask a fresh instance (or a colleague): "What assumptions does this framing embed? What questions does it exclude?" If the answer is "none," your framing is either perfect or the challenger isn't trying hard enough.

**Watch for Tammy's feedback loops.** Tammy's systems-thinking propensity is the closest the committee has to a frame-challenger — she traces how the decision connects to broader dynamics. If Tammy's analysis stays within the presented frame, the committee has accepted the framing uncritically.

---

## Failure Mode 6: The meta-circularity trap

### The scenario

You use the methodology to evaluate the methodology. The committee deliberates on whether cyberneutics is effective. It produces a well-scored resolution: yes, with caveats. The methodology has confirmed its own value using its own tools. The [methodology-evolution document](../meta/methodology-evolution.md) cites "recursive self-improvement that stabilizes at actionable insights" as evidence it works.

### The mechanism

Self-referential validation has a fundamental bootstrap problem. The evaluation criteria — the five rubrics, the committee's propensities, the confidence propagation rules — were designed by the same framework they're evaluating. Of course the deliberation scores well against rubrics it was built to satisfy. This isn't fraud; it's self-consistency masquerading as validation.

The theoretical foundation most directly implicated is second-order cybernetics itself (Essay 04): the observer is part of the observed system, and observation changes state. When the methodology observes itself, it observes from within its own framework — which means it can only see what its framework makes visible. A methodology that can't find its own flaws isn't necessarily flawless. It might have a self-confirming evaluative lens.

Three specific manifestations:

**The rubrics measure what the methodology values.** Reasoning completeness, adversarial rigor, assumption surfacing, evidence standards, trade-off explicitness — these are the things cyberneutics was *designed* to produce. Evaluating against them is testing whether the tool does what it was built to do. It doesn't test whether what it was built to do is *useful*. A perfectly crafted hammer still fails if the problem is a screw.

**The committee characters share the methodology's assumptions.** Maya assumes political dynamics matter. Frankie assumes values should drive decisions. Vic assumes evidence is the arbiter. Tammy assumes systems have feedback loops. These are the methodology's own premises, distributed across characters. The characters *cannot* produce the critique "maybe competing perspectives aren't the right approach to this problem" because competing perspectives *is* their approach.

**Success stories are observationally selected.** The methodology is applied to problems the user has chosen, using the user's judgment about fit. The methodology's "track record" includes only cases where someone decided it was appropriate — excluding all the cases where it wasn't tried, wasn't needed, or was tried and quietly abandoned.

### How to detect it

- **All evaluations of the methodology use the methodology's own tools.** If the only evidence for the methodology's effectiveness is self-generated, that's a closed loop.
- **No one can articulate what would count as disconfirming evidence.** What outcome would make you say "this methodology doesn't work"? If the answer is "nothing" or "I'm not sure," the framework has become unfalsifiable.
- **The methodology's failures are always attributed to misuse, never to design.** "The committee produced a bad result because the user didn't frame the problem well" or "because the characters weren't well-calibrated" — these explain away failures without the design ever being questioned.

### What to do

**Seek external evaluation.** The strongest evidence for or against the methodology comes from people who aren't invested in it. Did someone try it, follow the process faithfully, and get a bad outcome? That's more valuable than a hundred self-generated high-scoring transcripts.

**Define falsification criteria.** Before claiming the methodology works, specify what would count as it not working. Candidates: committee recommendations that were demonstrably worse than the user's pre-committee intuition; decisions made with the methodology that produced significantly worse outcomes than comparable decisions without it; sustained failure to produce insights the user hadn't already considered.

**Treat this essay as a test.** If reading this essay doesn't make you somewhat less confident in the methodology, it failed. An honest accounting of limitations should *cost* something — it should reduce confidence slightly, not increase it. If you read this and think "well argued, my confidence is unchanged," the essay was itself captured by the meta-circularity: it performed honesty about limitations without actually exposing any.

---

## The scope map: when to use what

Not every decision needs the full pipeline. Here is a practical guide:

### Use the full pipeline (scenarios → committee → evaluation) when:

- The problem has **genuine uncertainty about what might happen** — you can't enumerate outcomes
- **Competing values** are at stake — reasonable people would optimize for different things
- **Hidden assumptions** are likely — you suspect you're missing something but don't know what
- The stakes are **high enough** to justify the time and cost
- You need a **traceable decision record** — the provenance chain matters for accountability

### Use the committee alone (no scenarios) when:

- The problem is well-framed — you know what the options are
- You need to **stress-test a plan**, not explore a possibility space
- The question is "what should we do about X?" not "what might happen with X?"

### Use a quick propensity check (no pipeline) when:

- The problem is complicated but not complex — many factors, but knowable through research
- You mainly need to ensure you haven't missed an angle
- Time is short and stakes are moderate
- A mental pass through Maya/Frankie/Joe/Vic/Tammy perspectives is sufficient

### Don't use this methodology at all when:

- The problem has a **factual answer** that can be looked up — the difficulty is ignorance, not uncertainty
- The decision-maker **has already decided** and is seeking validation — the methodology will either be ignored or used to rubber-stamp
- **No one will act on the output** — the pipeline's cost is only justified if the resolution changes behavior
- The **domain is so specialized** that no amount of narrative generation compensates for missing domain expertise — the committee can reason about the reasoning, but not about fields it has no training data for
- You **can't articulate the stakes** — if you don't know why the decision matters, the committee can't either

---

## How to make the methodology more robust

Six failure modes suggest six corresponding defenses:

1. **Pre-screening**: Before running the pipeline, answer: "Is the difficulty here about complexity or complication? What would change my mind about the answer?" If you can answer the second question easily, you don't need the committee.

2. **Character calibration audits**: Periodically evaluate transcripts specifically for voice collapse and shallow roleplaying. The [troubleshooting guide](../artifacts/troubleshooting.md) has remedies. If remedies consistently fail for a given model, document which models can and can't sustain character differentiation.

3. **Domain-expert review step**: Add a step between evaluation and acceptance where someone with actual domain knowledge reads the transcript — not for formal quality (the rubrics handle that) but for substantive accuracy. This doesn't scale to every decision, but for high-stakes ones, it's the single highest-value addition.

4. **Forced editorial engagement**: Require the user to annotate resolutions with their own reasoning, not just accept/reject. Track override rates. A healthy system has the user pushing back 10-30% of the time.

5. **Frame-challenge protocol**: Before entering the pipeline, explicitly generate at least one alternative framing of the problem. Ask: "If someone disagreed that this is the right question, what question would they ask instead?"

6. **External validation program**: Collect outcome data. After decisions made with the methodology, track what actually happened. Build a dataset of methodology-assisted decisions and their results. This is the only way to move from "the process felt rigorous" to "the process produced better outcomes."

---

## This essay's own failure modes

Intellectual honesty requires applying this analysis to itself.

**This essay could fail by being too gentle.** If the failure modes described above read as manageable problems with clear solutions, the essay has been captured by the methodology's optimism. Some failure modes — particularly the meta-circularity trap and the evaluation loop's substantive blindness — don't have clean fixes. They're structural limitations.

**This essay could fail by making the methodology look robustly self-aware rather than genuinely limited.** A methodology that documents its own failures with apparent rigor can paradoxically *increase* trust: "They're so honest about limitations!" This is the credibility paradox. If reading this essay makes you trust the methodology *more*, check whether the trust comes from the content (you now understand the failure envelope and can work within it) or from the *gesture* (they admitted problems, so they must be trustworthy). Only the first is warranted.

**This essay was written by an LLM — the same kind of system whose limitations it describes.** The author shares the training distribution, the bias toward coherent narratives, and the tendency toward synthesis that the essay warns about. The failure modes identified here are the ones visible from within that distribution. Failure modes outside it — the unknown unknowns of narrative computing — are by definition absent from this analysis.

This is not a minor caveat. It is the deepest limitation of the entire essay. The six failure modes above are failure modes that a system trained on methodology-critical literature *would* identify. They're the kinds of critiques that appear in papers about Agile's failures, design thinking's blind spots, and lean startup's domain boundaries. The essay pattern-matches to "what honest methodology critique looks like" — and it does this well enough to be useful. But pattern-matching to critique literature is not the same as identifying the *actual* failure modes specific to narrative computing with LLMs. Those modes might include phenomena that have no precedent in prior methodology failures — emergent behaviors of large language models that have no analogue in human committee deliberation, failure patterns that arise from the specific architecture of transformer models, or interaction effects between the user's cognitive biases and the model's training biases that produce novel kinds of confident wrongness.

We don't know what we don't know. The failure modes we can describe are the ones in the training distribution. The ones that matter most may be the ones we can't yet describe. The strongest version of this essay would be written five years from now, after extensive empirical use, by practitioners who discovered failure modes the hard way. Until then, treat this as a starting inventory, not a complete map.

---

## The test

If this methodology works, it should survive the following challenge:

Take a decision you've already made — one where you know the outcome. Run the methodology on it retroactively, without telling the committee what happened. Does the committee surface the considerations that turned out to matter? Does the resolution recommend the action that turned out to be right? Does it flag the risks that materialized?

If yes: the methodology adds value for that class of problem.

If no: either the problem was outside the methodology's scope, or the methodology's value proposition is weaker than claimed.

This isn't a one-time test. It's a calibration practice. The methodology's credibility should be proportional to its empirical track record — not to its theoretical elegance, not to its formal rigor, not to how good the transcripts look.

*Results, not resolutions.*

### First empirical data point (2026-03-20)

The [Black Swan Hindsight Framework Phase A](../research-programs/evaluating-deliberative-architectures/results/phase-a-results.md) ran a version of this test. Two constructed scenarios with known structural insights. Committee deliberation (five characters, adversarial debate) vs. a single AI given the same word count and instructions to analyze from multiple angles. Two specific insights were the targets: did the committee spot them when the single AI didn't?

Result: the committee did not reliably surface the insights the single AI missed. On one target (the phasing critique — recognizing that a phased migration tests the deployment tool, not the configuration), the committee got closer (one run scored "Partially present" vs. "Absent" for both single-AI runs) but never completed the reframe. On the other target (creation-vs-activity reframing), both conditions surfaced it — it wasn't a committee-specific capability.

This is a single data point on constructed scenarios with minimal statistical power. It doesn't settle the question. But it establishes the baseline: on these scenarios, the committee's advantage over an effort-matched single agent is directional, not categorical. The committee produced qualitatively different analysis — character-driven tensions, productive disagreements, argumentative pressure — without producing reliably different *insights* at the reframing level.

The finding connects to two failure modes in this essay. **Failure Mode 2** (shallow roleplaying): the committee characters generated the genre of adversarial reframing — Vic distinguished types of drift, Joe recalled institutional failures, Tammy traced feedback loops — but the collective argumentative pressure wasn't enough to complete the specific conceptual move. **Failure Mode 6** (meta-circularity): the committee deliberated on its own experimental design (twice), producing the pivot to the reframing probe. The methodology's self-governance worked well. Its performance on the test the self-governance designed did not pass the self-governance's own pre-registered criterion. That's an honest outcome.

The full narrative is in [the-story-so-far.md](../research-programs/evaluating-deliberative-architectures/results/the-story-so-far.md). The detailed evidence is in [the results directory](../research-programs/evaluating-deliberative-architectures/results/).

---

**Related artifacts**:
- [Troubleshooting Cyberneutics](../artifacts/troubleshooting.md) — operational fixes for common failure modes
- [Evaluation Rubrics Reference](../artifacts/evaluation-rubrics-reference.md) — the rubrics this essay critiques
- [Adversarial Committees](../artifacts/adversarial-committees.md) — the core technique and its known limitations

**Related essays**:
- [Why Narrative Engines Change Everything](./01-why-narrative-engines-change-everything.md) — the claims this essay stress-tests
- [The Synthesis](./05-the-synthesis.md) — the theoretical foundation whose load-bearing elements are identified here
- [Decisions Under Uncertainty](./10-decisions-under-uncertainty.md) — the composed pipeline whose failure modes are mapped here

**Related meta**:
- [Methodology Evolution](../meta/methodology-evolution.md) — the development history, including what we still don't know
