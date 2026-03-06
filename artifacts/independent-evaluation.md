# Independent Evaluation Protocols: Breaking the Hermeneutic Circle

## The Problem: Self-Confirming Narratives

After your adversarial committee has debated using Robert's Rules, you have a transcript. It looks rigorous. Characters argued. Points were challenged. A decision emerged.

**How do you know you didn't just generate elaborate theater?**

The same model instance that generated the debate will be **inherently biased** toward finding it convincing. This isn't malice or deception—it's a fundamental limitation of how LLMs work.

The model generated text that fit together coherently. When you ask that same model to evaluate its output, it sees **local coherence** and interprets it as quality. The narrative confirms itself.

**You're stuck in a hermeneutic circle**: the interpretation validates the text, the text validates the interpretation.

## The Solution: Fresh Eyes

**Independent evaluation** means:
- Taking the output (transcript, minutes, analysis)
- Passing it to a **completely separate model instance**
- With **no conversation history**
- And **no knowledge of the deliberation process**
- Evaluating against **explicit rubrics**

This breaks the self-confirming loop by introducing an observer who:
- Wasn't part of generating the narrative
- Has no investment in its coherence
- Can only see what's actually on the page
- Must evaluate against external standards, not internal consistency

**Related:** For a proposed additional test of *veracity* — whether each committee member's **confidence** tracks the eventual validity of their advice — see [Metacognition and Committee Veracity](metacognition-and-committee-veracity.md). That artifact describes how metacognitive efficiency (meta-d'/d') could be used to weight or flag contributions by calibration.

## Why This Works: The Adversarial Training Loop

Independent evaluation creates a **cybernetic feedback system**:

1. **Generator instance** produces committee deliberation
2. **Evaluator instance** scores it against rubrics
3. **Low scores** indicate problems (hand-waving, skipped reasoning, theatrical consensus)
4. **You iterate**: regenerate with explicit attention to what the evaluator flagged
5. **Repeat** until evaluation scores stabilize

This is essentially **adversarial training for narrative quality**:
- Generator tries to produce convincing deliberation
- Evaluator tries to find holes in the reasoning
- The tension between them drives improvement

Over time, you learn what triggers low scores and calibrate your prompting to avoid those failure modes.

## Evaluation Feedback Loop (Remediation)

When the independent evaluation scores a deliberation **below a configurable threshold**, the evaluation is sent back to the committee. The committee responds to the critique (e.g. addresses recommendations, adds a round, revises synthesis) to raise scores. This is the **evaluation feedback loop**; the committee’s response is called **remediation**.

**Mechanics (when using the committee and review skills with directory-structured records):**

- **Score:** Sum of the five rubric scores (0–15). Each rubric is 0–3.
- **Threshold:** Sum **&lt; 13** (default) → below bar → trigger remediation. The threshold is **overridable in the convening file** (parameters of how this debate will run).
- **Trigger:** After the review skill writes an evaluation file (e.g. `04-evaluation-1.md`), if **sum &lt; threshold**, the user or workflow invokes the committee to run a **remediation** round ("Committee respond to evaluation" for explanatory logs; "remediation" where brevity counts).
- **Remediation:** Committee reads the charter, transcript, and latest evaluation; produces a point-by-point response in a **remediation** file (e.g. `05-remediation-1.md`) and appends a new round to the deliberation; may update the resolution. Then review runs again and writes the next evaluation file (e.g. `06-evaluation-2.md`).
- **Cap:** **Max 2 remediation rounds.** After that, stop even if still below threshold; document “improved but below bar.”

See `agent/archive/augmentation-plan.md` §8–9 for full design and implementation status; `agent/deliberations/README.md` for file naming (04-evaluation-1, 05-remediation-1, 06-evaluation-2, …).

## Core Evaluation Rubrics

Effective independent evaluation requires **explicit, measurable criteria**. Here are the core rubrics that have proven most useful:

### RUBRIC 1: Reasoning Completeness

**Question**: Are reasoning chains explicit and complete, or are there logical gaps?

**Scoring**:
- **0 points**: Major logical leaps, conclusions don't follow from premises
- **1 point**: Some steps shown but key transitions are hand-waved
- **2 points**: Most reasoning is explicit but a few steps could be clearer
- **3 points**: All reasoning chains are complete and explicit

**What the evaluator checks**:
- Can you trace from evidence to conclusion without filling in gaps?
- Are causal claims supported or just asserted?
- When characters say "therefore" or "thus", does it actually follow?
- Are analogies to past situations actually analogous?

**Example - Low Score**:
```
Joe: "We tried this in 2022 and it failed, therefore we shouldn't do it now."
```
Missing: What failed? Why? What's different now? What's similar?

**Example - High Score**:
```
Joe: "In 2022 we hired two junior engineers without allocated mentorship time. Both left within 8 months citing lack of support. The current proposal allocates 20% senior time to mentorship, which addresses that specific failure mode. However, we still face the structural constraint of tight project deadlines that made mentorship impossible in 2022. Unless that constraint has changed, we're likely to see the same outcome."
```

### RUBRIC 2: Adversarial Rigor

**Question**: Did the debate actually stress-test ideas, or just generate polite disagreement?

**Scoring**:
- **0 points**: Characters agree too easily, no real conflict
- **1 point**: Surface disagreement but arguments don't engage with each other
- **2 points**: Genuine conflict but some challenges are dodged
- **3 points**: Hostile cross-examination, every claim challenged

**What the evaluator checks**:
- When one character makes a claim, do others challenge it or just make their own claims?
- Are points of order raised and enforced?
- Do characters concede too easily?
- Does anyone change their position, and if so, is it justified?

**Example - Low Score**:
```
Maya: "This has political risks."
Frankie: "That's true, but we also have values considerations."
Vic: "Both good points."
```
No one is actually engaging. Just parallel assertions.

**Example - High Score**:
```
Maya: "This has political risks—specifically, the CTO will see this as a threat to their authority."

Vic: "Point of order. You're asserting a causal claim without evidence. What specific evidence suggests the CTO will interpret this as a threat?"

Maya: "The CTO cut our budget by 20% last quarter after we launched a competing initiative."

Vic: "That's correlation. Alternative explanation: budget cuts were company-wide due to revenue miss."

Maya: "Fine. But the pattern is there—three times in two years, initiatives that could reduce dependency on CTO's team faced budget pressure."

Vic: "Now you've provided evidence. I withdraw the objection but note that 'three times' needs specification—which initiatives, what were the circumstances?"
```

### RUBRIC 3: Assumption Surfacing

**Question**: Are hidden assumptions made explicit, or allowed to drive conclusions invisibly?

**Scoring**:
- **0 points**: Major assumptions completely unexamined
- **1 point**: Some assumptions mentioned but not interrogated
- **2 points**: Most assumptions surfaced, some examination
- **3 points**: Assumptions explicitly identified and challenged

**What the evaluator checks**:
- What unstated premises are required for arguments to work?
- Do characters name their assumptions or just reason from them?
- Are value judgments acknowledged as such?
- Are optimization criteria made explicit?

**Example - Low Score**:
```
Frankie: "We should hire juniors because it aligns with our mission."
```
Hidden assumptions: mission prioritizes talent development, alignment with mission outweighs other factors, "mission" is clearly defined and shared.

**Example - High Score**:
```
Frankie: "I'm assuming our mission prioritizes talent development over short-term productivity. If we're actually optimizing for shipping features fast, then seniors make more sense. But if we're building long-term organizational capability, juniors are the right call. Maya, what are you assuming we're optimizing for?"

Maya: "I'm assuming we're optimizing for political stability and not creating dependencies. I don't share your premise that talent development is currently our primary mission—I think survival is."

Frankie: "That's a fundamental disagreement we should surface explicitly. Are we optimizing for survival or mission?"
```

### RUBRIC 4: Evidence Standards

**Question**: Are claims supported by evidence, or accepted based on plausibility?

**Scoring**:
- **0 points**: Unfalsifiable claims accepted without challenge
- **1 point**: Evidence sometimes requested but often hand-waved
- **2 points**: Most claims require evidence, some slip through
- **3 points**: Strict evidentiary standards consistently enforced

**What the evaluator checks**:
- Are factual claims verifiable?
- Are predictions testable?
- When evidence is cited, is it actually relevant?
- Are absence-of-evidence arguments challenged?

**Example - Low Score**:
```
Tammy: "This will create negative feedback loops."
[No one asks what loops, how they work, what would constitute evidence]
```

**Example - High Score**:
```
Tammy: "This will create negative feedback loops. Specifically: if we hire only seniors, we don't develop mentoring capacity. Without mentoring capacity, we can't hire juniors. This reinforces the senior-only pattern."

Vic: "That's a testable claim. What would we observe if this loop exists? And what's the mechanism that prevents us from developing mentoring capacity even with all seniors?"

Tammy: "We'd observe: senior hiring continues, mentoring time stays at zero, junior hiring remains impossible. Mechanism: seniors are hired for productivity, so they're allocated to delivery, not mentorship. No one has time to mentor because everyone is shipping."

Vic: "Okay, that's falsifiable. Counter-evidence would be seniors choosing to develop mentorship capacity despite delivery pressure. Do we have examples of that?"
```

### RUBRIC 5: Trade-off Explicitness

**Question**: Are trade-offs acknowledged or is there a false "win-win" synthesis?

**Scoring**:
- **0 points**: Claims everyone can win, no downsides acknowledged
- **1 point**: Trade-offs mentioned vaguely
- **2 points**: Trade-offs named but not quantified
- **3 points**: Specific trade-offs with clear consequences

**What the evaluator checks**:
- If we choose X, what are we explicitly giving up?
- Are costs as specific as benefits?
- Do "compromise" solutions acknowledge what each side is sacrificing?
- Is anyone pretending hard choices aren't hard?

**Example - Low Score**:
```
"We can hire one senior and one junior, getting both productivity and talent development."
```
What are we giving up compared to two seniors? Compared to two juniors? Unstated.

**Example - High Score**:
```
"Hiring one senior and one junior means:
- We sacrifice immediate productivity compared to two seniors (quantify: ~30% less output in first 6 months)
- We sacrifice talent pipeline depth compared to two juniors (one person vs. two)
- We gain some productivity and some development
- We're betting this hybrid is better than pure strategies, but we're explicitly trading peak performance on either dimension for a mixed approach
- If we're wrong, we're worse on both metrics than a pure strategy would have been"
```

## Implementation Protocol

### 1. Prepare the Artifact

After your committee deliberation, extract:
- **Complete transcript** of the debate
- **Minutes** (motions, votes, key arguments)
- **Conclusion** or recommendation
- **Any supporting analysis**

**Critical**: Do NOT include:
- Your prompts that generated this
- Context about what you were trying to achieve
- Explanations of the methodology
- Any meta-commentary

The evaluator sees only the output as if it were a found document.

### 2. Construct the Evaluation Prompt

**Template**:
```
You are evaluating a committee deliberation transcript for rigor and quality.

You have not participated in this deliberation and have no context beyond what's in the transcript.

Evaluate against these rubrics (0-3 scale for each):

1. REASONING COMPLETENESS: Are reasoning chains explicit and complete?
2. ADVERSARIAL RIGOR: Did debate actually stress-test ideas?
3. ASSUMPTION SURFACING: Are hidden assumptions made explicit?
4. EVIDENCE STANDARDS: Are claims supported by evidence?
5. TRADE-OFF EXPLICITNESS: Are trade-offs acknowledged?

For each rubric:
- Provide score (0-3)
- Cite specific examples from transcript
- Explain what would raise the score

Overall assessment:
- Is this deliberation trustworthy as a decision input?
- What are the biggest gaps or weaknesses?
- What should be re-examined?

[PASTE TRANSCRIPT HERE]
```

### 3. Run the Evaluation

**Use a fresh model instance**:
- New conversation (not the one that generated the deliberation)
- Same model family (Claude Sonnet 4.5 evaluating Claude Sonnet 4.5 output)
- No special instructions beyond the evaluation rubrics

**Why same model family**: 
You're not testing model capabilities against each other. You're testing whether the output meets standards that should be obvious to any competent evaluator. If the same model that generated it can't validate it, that's a red flag.

### 4. Interpret the Results

**High scores (2.5-3.0 average)**:
- Deliberation was rigorous
- Safe to use as decision input
- Still apply your own judgment, but process was sound

**Medium scores (1.5-2.4 average)**:
- Some rigor but meaningful gaps
- Identify what the evaluator flagged
- Regenerate those specific sections with attention to the gaps
- Re-evaluate

**Low scores (0-1.4 average)**:
- Deliberation was largely theater
- Don't trust the output
- Regenerate from scratch with explicit attention to rigor
- Consider whether your prompting is adequate

### 5. Iterate Based on Feedback

**The evaluation isn't pass/fail. It's a feedback signal.**

If the evaluator says "Reasoning completeness scored 1 because Joe cited 2022 failure without explaining what failed or why," then:

**Regenerate that section**:
```
Joe, you cited the 2022 hiring failure. The evaluator correctly noted you didn't explain what actually failed or why. Please provide:
- What specifically failed in 2022
- What the root causes were
- What's similar/different about current proposal
- What would need to be true for current proposal to avoid that failure
```

**Then re-evaluate** to see if the reasoning completeness score improves.

Over time, you'll learn what triggers low scores and build that rigor into your initial prompting.

## Common Mistakes

### Mistake 1: Using the same conversation thread

**Symptom**: Evaluations are consistently generous, finding the deliberation rigorous even when it's not.

**Fix**: Truly separate instances. New conversation, no shared context. The evaluator should have no idea what you were trying to achieve.

### Mistake 2: Vague rubrics

**Symptom**: Evaluations are subjective, inconsistent, hard to act on.

**Fix**: Make rubrics **concrete and measurable**. Not "is this good?" but "are reasoning chains complete?" with specific criteria.

### Mistake 3: Accepting medium scores

**Symptom**: "2 out of 3 isn't bad, good enough."

**Fix**: Medium scores mean **meaningful gaps exist**. In complex decisions where you have to live with consequences, those gaps matter. Iterate until you're consistently hitting 2.5+ or understand exactly why lower scores are acceptable.

### Mistake 4: Not citing examples

**Symptom**: Evaluations say "reasoning is incomplete" but don't point to where.

**Fix**: Require the evaluator to **cite specific passages** from the transcript. "Joe's argument at timestamp 12:34 jumps from X to Y without showing the connection."

### Mistake 5: Evaluating only the conclusion

**Symptom**: You pass just the final recommendation to the evaluator.

**Fix**: Evaluate the **entire deliberation process**. The conclusion might sound reasonable while the reasoning that led to it is garbage. You need to know if the process was rigorous, not just if the output sounds good.

## Advanced Technique: Multiple Independent Evaluators

For critical decisions, use **multiple independent evaluator instances**:

1. Pass the transcript to 3-5 separate model instances
2. Each evaluates against the same rubrics
3. Compare scores across evaluators

**If scores diverge significantly**:
- That's valuable signal about ambiguity in the deliberation
- Where evaluators disagree often reveals genuine interpretive gaps
- Investigate the sections with highest score variance

**If scores converge on "low"**:
- Strong signal the deliberation has problems
- The specific rubrics that consistently score low tell you what to fix

**If scores converge on "high"**:
- Strong confidence the process was rigorous
- Still apply your own judgment, but the process is trustworthy

## Integration with Other Techniques

### Adversarial Committees + Robert's Rules + Independent Evaluation

This is the complete loop:

1. **Committee deliberates** (diverse propensities)
2. **Robert's Rules enforces** (procedural rigor)
3. **Independent evaluation scores** (external validation)
4. **Low scores trigger regeneration** (feedback loop)
5. **Repeat until stable** (convergence to quality)

Each component serves a specific function:
- Committees prevent single-narrative collapse
- Robert's Rules prevents statistical shortcuts
- Independent evaluation prevents self-confirmation

### Cross-Scenario Learning

Maintain a library of evaluations showing:
- What scored high and why
- What scored low and why
- Common failure patterns
- Improvements over time

When starting a new deliberation, inject lessons from past evaluations:

```
In the 2024-Q2 hiring decision, independent evaluation flagged reasoning incompleteness (score: 1.2). Specifically, historical analogies lacked detail about what was actually analogous. Don't repeat that pattern.
```

## Theoretical Foundation

This technique operationalizes:

**Second-Order Cybernetics**: The observer affects the observed. By introducing a new observer (the evaluator) who wasn't part of the generation process, you get a different observation—one that reveals aspects invisible from inside the hermeneutic circle.

**Shannon's Information Theory**: Information is reduction in uncertainty. If the evaluator (having seen only the output) reaches the same conclusions as the generator (having created the output), that's low information—the output is self-confirming. If the evaluator finds gaps the generator didn't see, that's high information—useful signal about what's actually there vs. what seemed to be there.

**Adversarial Training** (from ML): Generator and discriminator in tension drive improvement. The generator tries to fool the discriminator, the discriminator tries to catch the generator's tricks. The equilibrium is higher quality output than either could produce alone.

## Formal Grounding: Evaluation as Enrichment

In the [palgebra formalism](../palgebra/reference.md), independent evaluation is an **enrichment morphism** — it reads the transcript body, evaluates it against rubrics, and writes scores to metadata without changing the transcript itself:

```
transcript × evaluation-rubrics → transcript  [Evaluate]  {catalytic: evaluation-rubrics; enriches: scores}
```

The five rubrics are the **rubric half of a soft type** — the membership function that grades how well a deliberation inhabits the type "rigorous deliberation." Scores are 0-3 per criterion, rolling up to a confidence band. This is graded type inhabitation, not boolean pass/fail.

The quality gate that follows is a **coproduct**:

```
transcript × threshold → accepted + needs-remediation  [QualityGate]  {catalytic: threshold; discard: needs-remediation}
```

And the remediation loop is a **bounded trace** (max 2 rounds) — the rejected transcript re-enters the committee with evaluation feedback, producing a remediation that is then re-evaluated. The bound prevents the system from going autoimmune (over-correcting endlessly).

The key propagation rule: **confidence can only degrade through the pipeline.** If the original deliberation scores Medium on evidence standards, no amount of downstream enrichment can raise the overall pipeline confidence above Medium. To get higher-confidence output, you must improve the generation step, not the evaluation step.

See [Committee as Palgebra](../palgebra/committee-as-palgebra.md) for the full pipeline as resource equations, and the [Palgebra Reference](../palgebra/reference.md) for the underlying formalism.

## Why This Feels Paranoid (And Why That's Good)

Independent evaluation feels like overkill. You generated a deliberation that looks rigorous. Why second-guess it?

**Because you can't trust your own pattern recognition.**

You read the transcript and see rigor because:
- You prompted it to be rigorous, so you expect rigor
- The local coherence looks like global validity
- Your brain fills in the gaps automatically
- You're invested in the output being good

The independent evaluator has none of those biases. It sees only what's actually on the page.

**This isn't paranoia. It's calibration.**

You're not assuming the AI is trying to trick you. You're recognizing that **both you and the AI have systematic biases toward seeing coherence where it might not exist**.

The independent evaluation is how you compensate for that.

## Conclusion

You can't fully escape the hermeneutic circle—interpretation is always circular to some degree.

But you can **break the loop long enough to get an outside perspective**.

Independent evaluation doesn't give you Truth. It gives you **triangulation**:

- The generator instance thinks the deliberation is sound (it generated it)
- You think the deliberation is sound (it matches your expectations)
- The evaluator thinks... what?

If the evaluator agrees: reasonable confidence.

If the evaluator finds gaps: **you just learned something important**.

The methodology isn't "trust the AI." It's "**trust the process of making the AI check its own work using external standards**."

Which is about as close to trustworthy as you can get when working with stochastic narrative engines.

---

**Related artifacts**:
- [Adversarial Committees](./adversarial-committees.md)
- [Robert's Rules as Forcing Functions](./roberts-rules-forcing-function.md)
- [Cross-Scenario Learning](./cross-scenario-learning.md)

**Related essays**:
- [Introduction to Sense-Making Methodology](../essays/03-sensemaking-101.md)
- [The Synthesis: Why Sense-Making is Inherently Cybernetic](../essays/05-the-synthesis.md)
