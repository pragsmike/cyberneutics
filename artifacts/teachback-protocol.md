# Teachback Protocol: Verifying Mutual Understanding in Deliberations

## The Problem: Parallel Monologues Without Engagement

Committee deliberations sometimes produce sophisticated-sounding disagreement that masks a simpler reality: the characters aren't actually understanding each other. They state positions, argue past each other, find points of genuine tension—but none of them have reconstructed their opponents' logic from the inside.

The resolution may synthesize surface-level points without capturing the deep structure of the disagreement. You're left with:
- "We've heard all perspectives"
- "Everyone's points are valid"
- "The real question is X"

**But have the characters actually understood each other's positions, or just heard them?**

This matters because:
1. **Misunderstanding disguises as comprehension.** "I understand why you think that" often means "I've categorized your argument" not "I could reconstruct it from a different starting point."
2. **Unexamined assumptions stay invisible.** If no one has tried to build your position from their own framework, they haven't identified what they'd need to believe to accept it.
3. **Residual disagreement goes unsurfaced.** If the disagreement is about values, mechanisms, or evidence, teachback reveals which. If you skip it, you don't know.

## The Solution: Reconstruction from an Alien Framework

**Teachback** is a quality assurance step inserted after the main deliberation but before resolution. Each character articulates the strongest version of every other character's argument—not by paraphrasing or summarizing, but by **reconstructing it from their own propensity**.

This operationalizes Gordon Pask's central insight: understanding is demonstrated not by agreement or repetition, but by the ability to reconstruct another's position **from a different starting point**.

### How It Works

In a teachback round:

**Maya** (paranoid realist) teaches back **Frankie's** (values-first) position: "The strongest version of your argument, stated in terms I find compelling, is that organizational survival over the long term depends on building a culture that attracts people who care about the mission. If we abandon that culture for short-term pragmatism, we lose what makes us coherent and attractive. That's not naive idealism—it's a claim about cultural incentives."

**Vic** (evidence prosecutor) teaches back **Tammy's** (systems thinker) position: "The feedback loop you're describing—hire seniors only → no mentoring capacity → can't hire juniors → reinforces senior-only hiring—is falsifiable. I can verify it by checking: Do we observe zero mentoring capacity? Do junior candidates choose not to apply? Has our hiring pattern actually shifted? If those observations hold, your mechanism is credible."

**Tammy** teaches back **Joe's** (continuity guardian) position: "Your claim isn't just 'we failed before.' It's more precise: 'we had a specific failure mode (mentorship without time allocation) and it will recur unless the structural constraint (deadline pressure) changes.' That's a testable prediction. If deadline pressure has actually decreased, your objection is weaker."

### Success Criteria

A teachback succeeds when:

1. **Recognition**: The original character recognizes their position in the teaching-back character's articulation. Not "that's exactly what I said" but "yes, that's the structure of my argument."

2. **Addition**: The teaching-back character has added something—a sharper formulation, a different angle, a clarification—that the original character acknowledges. The teachback isn't repetition; it's reconstruction that reveals something about the position that wasn't explicit before.

3. **Residual disagreement preserved**: The teachback does not collapse into agreement. Maya teaching back Frankie's values argument doesn't mean Maya agrees with the values. It means she understands what premises Frankie needs to be true for her position to hold.

A teachback fails when:

1. **Non-recognition**: The original character says "that's not what I meant" or "that's a mischaracterization." This means the teaching-back character has imposed their own framework so heavily that they've obscured the original position.

2. **Pure repetition**: The teaching-back character only quotes or paraphrases without reconstruction. True teachback requires understanding the position well enough to articulate it in a different voice from a different epistemic position.

3. **Straw-manning**: The teachback reduces the position to a caricature or worst-case interpretation. The goal is the strongest version, not a weak strawman that's easy to dismiss.

## When to Insert Teachback

**After main deliberation rounds, before resolution.**

Teachback is an intermediate step in the deliberation pipeline:

```
Committee Charter
    ↓
[Deliberation Rounds 1-N with Robert's Rules]
    ↓
[TEACHBACK ROUND - verify mutual understanding]
    ↓
[Resolution / Synthesis round]
    ↓
[Independent Evaluation]
```

Insert teachback when:

1. **The deliberation has shown conflicting interpretations.** If characters are making different causal claims, value assertions, or risk assessments, teachback surfaces whether disagreement is real or just talking past each other.

2. **Independent evaluation previously scored low on "Adversarial Rigor."** This indicates the committee may be generating polite agreement rather than genuine engagement. Teachback often reveals that agreement is premature.

3. **Assumptions have been mentioned but not really examined.** Teachback forces explicit reconstruction of the premises that would need to be true for each position to hold.

4. **The problem is complex enough that misunderstanding is likely.** High-dimensional decision spaces (multiple stakeholders, trade-offs, feedback loops) create natural misunderstanding risk. Teachback compensates.

## When NOT to Use Teachback

**Quick, low-stakes deliberations** where the overhead isn't worth the rigor.

If the committee is deciding between two straightforward options with no deep value conflict or causal disagreement, teachback adds time without insight.

**Deliberations that already show strong cross-character engagement.**

Watch for: Characters directly responding to each other's specific points. "You mentioned X, but that assumes Y which I disagree with because..." If characters are already building on and challenging each other's actual positions, teachback may be redundant.

**When time constraints are tight.**

Teachback requires additional rounds and model calls. If your timeline doesn't allow iteration, deprioritize it for faster basic deliberation instead.

## Template: Teachback Round Prompt

Use this prompt structure to insert a teachback round. Replace the character names and position summaries with what's actually in your deliberation.

```
---

## Teachback Round

You've just completed the main deliberation. Before moving to resolution,
verify that characters have understood each other's positions—not just heard them.

In this round, each character will articulate the strongest version of every
other character's argument, from their own propensity. The goal is to demonstrate
that you understand the position well enough to reconstruct it in your own voice.

**Rules for teachback**:
- Restate the position, don't quote it
- Articulate it in a way that makes sense from your perspective
- Identify the premises or assumptions the position rests on
- Add clarity about what it would take for that position to be right
- Preserve genuine disagreement—teachback is not agreement

---

### Maya teaches back Frankie's position

Frankie, in your view the central claim is: [specify what Maya
understands Frankie to be claiming about values, mission, or organizational identity].
From my perspective as someone focused on incentives and political dynamics,
the strongest version of this argument is...

[Teach back from paranoid-realist lens: what would need to be true for
values-first reasoning to be sound? What does Frankie assume about how
culture drives long-term viability?]

Is that a fair articulation?

---

### Frankie teaches back Maya's position

Maya, your claim focuses on [specify what Frankie understands Maya to be
warning about]. From my perspective as someone focused on mission and values,
the strongest version of your concern is...

[Teach back from values-first lens: what organizational risks does Maya
identify? What mechanisms create those risks?]

Is that fair?

---

### Vic teaches back Tammy's position

Tammy, you're describing a feedback loop. From my perspective as someone
focused on evidence and falsifiability, the strongest version of your claim is...

[Teach back from evidence-focused lens: What is the loop? What would
constitute evidence that it exists or doesn't? What observations would
make this prediction wrong?]

Accurate?

---

### Tammy teaches back Vic's position

Vic, you're raising evidentiary concerns about [specify]. From my perspective
as someone focused on systems and second-order effects, the strongest version
of your objection is...

[Teach back from systems-thinker lens: What evidence does Vic require?
What would happen downstream if we ignored that evidentiary standard?]

Fair characterization?

---

### Joe teaches back [remaining characters as needed]

[Follow the same pattern: Joe articulates each remaining position from
continuity-guardian perspective, identifying what assumptions would need
to hold and what institutional memory might be relevant.]

---

**After all teachbacks**:

Reflect briefly: Where did teachback reveal genuine understanding? Where
did it expose misunderstanding or hidden assumptions? Are there positions
that can't be understood from an opposing framework—indicating they rest
on incommensurable values rather than empirical disagreement?

---
```

## Connection to Evaluation Rubrics

Teachback directly targets:

**Rubric 2: Adversarial Rigor**
- Low scores often mean characters are making parallel claims without genuine engagement
- A teachback round that demonstrates actual understanding often raises Adversarial Rigor scores
- If characters can reconstruct each other's positions accurately, they've moved beyond polite disagreement to genuine deliberation

**Rubric 3: Assumption Surfacing**
- Teachback forces explicit reconstruction of assumptions
- "What would need to be true for that position to hold?" makes assumptions visible
- Successful teachback connects premises to conclusions in a way that identifies hidden dependencies

**Rubric 1: Reasoning Completeness** (partial)
- Teachback reveals gaps in reasoning chains
- If Maya can't reconstruct Frankie's logic, that often indicates the logic hasn't been fully articulated
- The need to build from a different starting point makes incomplete reasoning more visible

## Connection to Residuality and Robustness

Teachback is a **shock to the original argument**.

In the palgebra formalism, each teachback attempt is a perturbation — the position is restated from an adversarial perspective. What survives teachback — what the original character recognizes as fair even when articulated by someone with opposing propensities — is genuinely robust. What doesn't survive was decorative coherence, not structural understanding.

This connects to the broader principle: **iterations produce robustness**. One character's take on a position is vulnerable. When the position survives articulation from an opposing epistemic stance, it's been tested. When it survives articulation by multiple opposing stances, it's been pressure-tested.

## Example: Hiring Decision Teachback

**From the original deliberation**, these positions emerged:

- **Frankie**: Hire two junior engineers; it aligns with our mission of developing talent
- **Maya**: Political risk—creates dependency on whoever mentors them
- **Joe**: We tried this in 2022, failed; seniors are safer
- **Vic**: Need specific data on mentorship ROI before hiring juniors
- **Tammy**: Creates feedback loop—no junior-development capacity → can't hire juniors → never build capacity

**Teachback round**:

**Maya teaches back Frankie's position:**
"Frankie, what you're arguing—stated so I understand it—is that if we only hire seniors because it's operationally easier, we're optimizing for short-term productivity at the cost of long-term organizational capability. You're betting that building a culture of development attracts people with alignment and values, which matters for retention. Is that right?"

**Frankie**: "Yes, exactly. If we only extract value instead of building people, we become a place talent leaves."

**Vic teaches back Tammy's feedback loop:**
"Tammy, your claim is that we're stuck in a dynamic where we can't build junior capacity because we're optimized for senior output, and this becomes self-reinforcing. The observable signs would be: zero mentoring time allocated, junior candidates declining offers, and a decades-long trend of senior-only hiring. Is that what you're claiming?"

**Tammy**: "Right. And the mechanism is: we hire seniors for delivery pressure, so every senior's time is allocated to projects, not mentorship."

**Joe teaches back Maya's political concern:**
"Maya, you're not just saying juniors are risky. You're identifying a specific mechanism: mentoring creates a relationship, which creates influence, which means the mentor becomes a bottleneck for decision-making. We'd then have a junior pipeline dependent on one person's time. That's a structural vulnerability."

**Maya**: "Exactly. And whoever is mentoring becomes indispensable in ways that create political dynamics."

**[After all teachbacks]**:

**Chair**: What did teachback reveal?

**Frankie**: "Turns out Maya and I disagree on something deeper than I thought. She thinks the risk is structural (dependency), I think the risk is cultural (loss of mission alignment). These are different problems with different solutions."

**Vic**: "And I realize Tammy's feedback loop claim is testable. We can measure whether mentoring time actually goes to zero when juniors arrive. That's better than handwaving."

**Tammy**: "I also understand Joe's 2022 data better now—the failure wasn't 'juniors are bad,' it was 'we didn't have mentoring capacity,' which is different. So the real question is whether mentoring capacity exists *now*."

---

**Result of teachback**: The disagreement wasn't eliminated, but it became precise. The committee moved from vague concerns to specific, testable claims that can actually be addressed. The resolution can now be targeted at the real questions (Does mentoring capacity exist? Can we protect it from delivery pressure? How do we prevent mentor-dependency dynamics?) rather than abstract trade-offs.

## Implementation Notes

### Prompt Clarity

When running teachback, be explicit:
- "You're teaching back, not critiquing"
- "Make it in your own voice, not a summary"
- "Identify what the position assumes"
- "Preserve disagreement—this is not consensus-building"

### Regeneration on Failure

If a character's teachback is rejected ("That's not what I meant"), regenerate with more specific guidance:

```
Your teachback was rejected. Try again.
Specific guidance:
- Frankie said you misunderstood their mechanism
- Focus on: What does Frankie believe causes long-term retention?
- Articulate that mechanism in terms that make sense from your paranoid-realist perspective
- Don't critique it—just build it from your starting point
```

### Length and Depth

Teachback rounds are typically shorter than full deliberation rounds (2-3 minutes per character, not 5-10). They're focused, not exhaustive.

If teachback is productive and revealing, you can iterate once more. But don't let teachback become its own endless deliberation—it's a verification step, not a replacement for substantive debate.

### Recording Teachback Outcomes

When recording the deliberation:

```
## Teachback Results

[Specify which teachbacks succeeded/revealed understanding]
[Specify which teachbacks failed or exposed misunderstanding]
[What assumptions did teachback surface?]
[What remained in genuine disagreement even after mutual understanding?]
```

This becomes part of the input to evaluation and resolution.

## Common Mistakes

### Mistake 1: Characters Being Too Generous

**Symptom**: "Oh yes, I understand what you're saying now" followed by actual agreement.

**Problem**: Teachback is not about agreement. It's about understanding despite disagreement.

**Fix**: Remind characters: "Teach back the position so the person recognizes it, not so you agree with it. Preserve what you still find problematic."

### Mistake 2: Teaching Back Only the Conclusion

**Symptom**: "You think we should hire juniors because of talent development."

**Problem**: That's the conclusion, not the structure of the argument.

**Fix**: Demand mechanism: "What's the causal chain from hiring juniors to achieving your actual goal? What do you assume about how people stay or leave?"

### Mistake 3: Avoiding Teachback of Disagreement

**Symptom**: Characters teachback the points they agree with, skip the ones they disagree with.

**Problem**: Teachback is most valuable for mutual understanding of *disagreements*.

**Fix**: Explicitly assign: "Vic, teachback the point you most disagree with—the values claim from Frankie. Don't critique it; articulate it so Frankie would recognize it."

### Mistake 4: Teachback Devolving Into Debate

**Symptom**: After the teaching-back, debate restarts rather than moving to resolution.

**Problem**: Teachback is a verification step, not another round of substantive argument.

**Fix**: Structure it clearly: teachback round is closed once all characters have articulated and original characters have confirmed/corrected. Then move explicitly to resolution. Don't reopen the substantive debate.

## Integration with Other Techniques

### Before Robert's Rules / During Deliberation

Teachback can be used during earlier deliberation rounds (not just at the end) as a **forcing function** similar to Robert's Rules. If a character makes a claim and another character seems to misunderstand, call for immediate teachback:

"Maya, before you respond, teach back what Frankie just said so we know whether you're actually engaging with her argument or addressing a strawman."

This keeps deliberation honest in real-time.

### Before Independent Evaluation

A successful teachback round should improve evaluation scores on Adversarial Rigor and Assumption Surfacing. Before passing the deliberation to independent evaluation, note:

```
This deliberation included a teachback round that verified mutual understanding
of key disagreements. Evaluators: the transcript includes reconstructions of
positions from opposing frameworks. Assess whether these reconstructions demonstrate
genuine understanding or mask continued misunderstanding.
```

### After Low Evaluation Scores

If independent evaluation scores low on Adversarial Rigor or Assumption Surfacing, a remediation strategy is to insert a teachback round:

"Evaluation flagged that your debate showed surface disagreement without genuine engagement. Run a teachback round to verify you're actually understanding each other's positions."

## Theoretical Foundation

**Gordon Pask's Conversation Theory**: Understanding is not agreement or repetition. It's the ability to reconstruct another's distinction from your own framework. Teachback operationalizes this by requiring each character to demonstrate understanding through reconstruction.

**Second-Order Cybernetics**: The observer affects the observed. By introducing a teachback round that forces articulation from opposing perspectives, you change what gets made explicit. Positions that seemed coherent from inside become clearer (or more problematic) when articulated from outside.

**Adversarial Collaboration**: In psychological research, adversarial collaboration means proponents of competing theories work together to design experiments that could falsify either. Teachback is the deliberative equivalent—it forces deep engagement with opposing positions rather than surface-level debate.

## Conclusion

Teachback protocol operationalizes a simple question: **Do you actually understand each other, or just think you do?**

The answer often surprises. Disagreements that seemed irreconcilable become precise once both sides articulate what the other position requires to be true. Hidden assumptions surface. What looked like logical necessity reveals itself as value preference. Genuine feedback loops become visible.

It's not a way to force agreement. It's a way to make disagreement honest—which is the only foundation for real deliberation.

---

**Related artifacts**:
- [Adversarial Committees](./adversarial-committees.md)
- [Robert's Rules as Forcing Functions](./roberts-rules-forcing-function.md)
- [Independent Evaluation Protocols](./independent-evaluation.md)
- [Evaluation Rubrics Reference](./evaluation-rubrics-reference.md)
- [Character Propensity Reference](./character-propensity-reference.md)

**Related essays**:
- [Decisions Under Genuine Uncertainty](../essays/10-decisions-under-uncertainty.md)
- [The Synthesis: Why Sense-Making is Inherently Cybernetic](../essays/05-the-synthesis.md)
