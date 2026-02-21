# Scenario Generation: Divergent Narrative Exploration of Possible Futures

## The Core Problem

When facing genuine uncertainty — the kind where you don't know what might happen, not just which option is best — the committee technique has a blind spot. It deliberates brilliantly across perspectives, but it deliberates within the framing the user provides. If that framing is too narrow, the committee stress-tests a single future when it should be exploring several.

This is premature convergence at the input level. The committee is the funnel — it converges multiple perspectives into commitment. But convergence without prior divergence anchors on whatever framing arrived first.

## The Solution: Structured Divergent Exploration

Instead of jumping straight to "what should we do?", first ask "what could happen?":

1. **Frame the situation** — structure the ambiguity, name the uncertainties
2. **Deploy narrative lenses** — independent characters each generate a distinct future
3. **Assess coverage** — check that the scenario set spans the space of plausible futures
4. **Feed into deliberation** — the committee now deliberates across explored futures, not a single framing

The output isn't a forecast. It isn't a probability distribution. It's a **set of internally consistent narratives** that collectively map the space of plausible futures — so you can prepare for several, not bet on one.

## Why Narrative Scenarios (Not Probability Trees)

Probability trees require you to know the branches. Scenario narratives surface branches you hadn't imagined.

A probability tree says: "60% market grows, 40% market shrinks." A scenario narrative says: "The market grows, but growth concentrates in a segment you don't serve, because a regulatory change you weren't tracking made your core segment uneconomical. Meanwhile, your best engineer gets recruited by the company serving the growing segment, taking institutional knowledge with them."

The narrative does three things the tree cannot:
- **Surfaces hidden dependencies** (regulatory change → segment shift → talent loss)
- **Makes failure modes concrete** (not "market risk" but a specific cascade)
- **Generates early warning signs** (the regulatory proposal, the recruiter's call)

## The Scenario Roster

The scenario roster (`agent/scenario-roster.md`) provides four core narrative lenses designed to span the space of plausible futures:

| Character | Lens | Explores |
|-----------|------|----------|
| **Continuity** | Baseline extrapolation | What happens if current trends persist? Where does slow accumulation create sudden consequences? |
| **Disruption** | What breaks | What single point of failure cascades into systemic change? What assumption is load-bearing? |
| **Opportunity** | Latent potential | What undervalued asset becomes decisive? What door opens? |
| **Constraint** | What tightens | What happens when resources contract? Which freedoms are we taking for granted? |

These span two axes:
- **Change**: Continuity ↔ Disruption (what stays vs. what breaks)
- **Valence**: Opportunity ↔ Constraint (what opens vs. what closes)

The four quadrants ensure minimum viable divergence. For domain-specific problems, add 1–2 extension characters (see the roster file for the extension mechanism).

**Key difference from the committee roster**: scenario characters narrate *independently*. They don't argue. They don't know about each other's scenarios. The divergence comes from their different worldviews, not from adversarial interaction. Adversarial interaction is the committee's job — it happens downstream.

## How to Frame a Situation

Good scenario generation starts with a well-framed situation. The framing should make the ambiguity explicit:

**Include:**
- **What's uncertain**: the dimensions along which the future could diverge
- **What's at stake**: why these futures matter, what depends on them
- **Time horizon**: how far out the scenarios should project (default: 2–3 years)
- **Key actors**: who or what has agency in this situation

**Avoid:**
- Embedding your preferred outcome in the framing
- Narrowing the uncertainty to a binary (most situations have more than two futures)
- Omitting constraints (scenarios need boundaries to be useful)

### Example: Good vs. Bad Framing

**Bad**: "Should we build the new feature?"

This is a decision question, not a situation. It belongs with the committee.

**Bad**: "What happens if AI takes over?"

Too vague. No stakes, no actors, no time horizon.

**Good**: "Our 50-person B2B SaaS company has 18 months of runway. Our largest customer (38% of revenue) is in a sector facing regulatory upheaval. The founding team disagrees on whether to diversify the customer base (slower growth, more resilience) or double down on the core sector (faster growth, more risk). Key uncertainty: whether the regulatory change helps or hurts our core sector."

This has: specific stakes, identified uncertainty, named actors, implied time horizon, genuine ambiguity about the future.

## How to Choose Divergence Axes

Divergence axes are the dimensions along which your scenarios should differ. The core roster provides one set (change × valence), but you can specify additional axes relevant to your situation.

**Good axes** are:
- **Genuinely uncertain** — you don't know which pole will obtain
- **Consequential** — the difference between poles changes the right course of action
- **Independent** — they can vary separately (dependent axes collapse into one)

**Example axes:**
- Market consolidation ↔ fragmentation
- Regulatory tightening ↔ loosening
- Technology matures ↔ technology stalls
- Key talent stays ↔ key talent leaves

Two axes give four quadrants. Three axes give eight corners. More than three axes usually means some are dependent or inconsequential — simplify.

## How to Read the Output

The scenario set is in `agent/scenarios/<topic-slug>/02-scenarios.md`. For each scenario:

1. **Read the assumptions first.** The assumptions are the scenario's premises. If you reject the premises, the scenario is still useful — it tells you which assumptions are load-bearing.

2. **Look for surprises.** The scenarios that surprise you are the most valuable. They reveal futures your mental model excludes.

3. **Check the early warning signs.** These are the observable signals that a scenario is materializing. They convert abstract futures into concrete things to watch for.

4. **Compare across scenarios.** Where do scenarios agree? (Likely robust.) Where do they disagree? (That's where the interesting uncertainty lives.) What actions appear in multiple scenarios? (Those are robust commitments.)

5. **Check the coverage assessment** (`03-assessment.md`). Are there gaps? If the assessment identifies blind spots, consider regenerating with adjusted parameters or extension characters.

## When to Use Scenarios vs. Committee Directly

| Situation | Use |
|-----------|-----|
| "What should we do about X?" — the problem is well-framed, options are clear | Committee directly |
| "What might happen with X?" — genuine uncertainty about the future | Scenarios first, then committee |
| "We're facing a big decision but haven't thought it through" | Scenarios to explore, then committee to decide |
| "We have a plan — is it robust?" | Committee to stress-test |
| "We have a plan — what could go wrong?" | Scenarios to explore failure modes, then committee to assess |

The rule of thumb: if the ambiguity is about **what could happen**, fan first. If the ambiguity is about **what to do**, funnel directly.

## The Deliberated Choice: Composing Scenarios with Committee

Scenarios alone are storytelling without selection. The committee alone risks anchoring on the first framing. The **deliberated choice** composes both:

1. Run `/scenarios` to generate divergent futures
2. Review the scenario set; optionally adjust and regenerate
3. Run `/committee` with `scenario_context:` pointing to the scenario directory
4. The committee deliberates *across* the scenarios — which futures to optimize for, which to survive, which to dismiss
5. The resolution is a justified commitment grounded in explored futures

This is the fan → funnel composition formalized in `palgebra/duality-and-composition.md` as the **decision monad**. For the step-by-step workflow, see `artifacts/deliberated-choice-workflow.md`.

## Common Mistakes

### Mistake 1: Treating scenarios as predictions
Scenarios are not forecasts. They don't have probabilities. Their value is in **coverage** — did you explore enough of the possibility space? — not in accuracy.

**Fix**: Judge scenarios by whether they surface useful assumptions and early warning signs, not by whether they seem "likely."

### Mistake 2: Making all scenarios equally dramatic
Not every future is a crisis. The Continuity scenario (nothing dramatic happens, but slow trends compound) is often the most useful and the most underexplored.

**Fix**: Ensure the Continuity narrator generates a scenario. The boring future is frequently the most probable and the least planned-for.

### Mistake 3: Stopping at scenarios
Scenarios without deliberation are creative but uncommitted. They explore without resolving.

**Fix**: Feed the scenario set into `/committee`. The composition is where decision-making happens.

### Mistake 4: Using the committee roster for scenario generation
Committee characters (Maya, Frankie, Joe, Vic, Tammy) have epistemic propensities — they think differently. Scenario characters have worldview lenses — they see different futures. Using the committee roster for scenarios collapses the duality: you get perspectives on one future instead of multiple futures.

**Fix**: Use the scenario roster for divergent exploration; the committee roster for convergent deliberation.

## Where This Fits: The Pipeline View

In the [palgebra formalism](../palgebra/reference.md), scenario generation is the **fan** operation — the categorical dual of the committee (funnel):

```
situation × scenario-roster × scenario-parameters → scenario-set  [Fan]
  {catalytic: scenario-roster, scenario-parameters}
```

The scenario roster and parameters are **catalytic inputs** — they shape the divergence without being consumed. This is why the core roster is reusable: like the committee roster, it's infrastructure, not per-problem artifacts.

The fan is a **one-to-many spider** in string diagram terms: one input (situation) branches into multiple outputs (scenarios). The funnel is a **many-to-one spider**: multiple inputs (perspectives/scenarios) merge into one output (resolution). Composing them yields the decision monad.

For the full formalization — types, equations, monad structure, iteration — see `palgebra/duality-and-composition.md`.

## Theoretical Foundation

This technique operationalizes:

- **Bruner's narrative mode**: Scenario characters operate in narrative mode (System 1, associative, possibility-generating) rather than paradigmatic mode (System 2, rule-governed, truth-testing). The committee operates in paradigmatic mode. The composition provides "binocular vision" — both modes applied to the same problem.
- **Schwartz/van der Heijden scenario planning**: Scenarios as narratives, not forecasts; value in coverage, not probability; the 2×2 matrix of driving forces.
- **Deleuzian difference**: Multiple scenario runs from the same situation produce difference, not redundancy — each lens reveals futures the others miss.

See `essays/10-decisions-under-uncertainty.md` for the philosophical bridge.

---

**Related artifacts**:
- [Adversarial Committees](./adversarial-committees.md) — the convergent half
- [Deliberated Choice Workflow](./deliberated-choice-workflow.md) — the composed pipeline
- [Robert's Rules as Forcing Functions](./roberts-rules-forcing-function.md) — used in the funnel half

**Related essays**:
- [Decisions Under Uncertainty](../essays/10-decisions-under-uncertainty.md) — why fan then funnel
- [Narrative Engineering](../essays/07-bolands-narrative-engineering.md) — Bruner's two modes
