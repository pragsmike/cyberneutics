---
name: committee
description: >
  Run an adversarial committee deliberation using the fixed 5-character roster
  (Maya, Frankie, Joe, Vic, Tammy) to explore decision spaces, surface assumptions,
  and map trade-offs. Use when the user types '/committee [topic]' or asks for a
  committee deliberation on a complex decision or problem.
---

# Committee Deliberation Skill

Simulate a structured adversarial committee deliberation using the Cyber-Sense
methodology's fixed character roster. The committee explores problem spaces
through genuine conflict rather than convergent consensus, surfacing assumptions,
trade-offs, and blind spots.

## When to use

- User types `/committee [topic/question]`
- User asks to "run a committee on [X]" or "deliberate on [Y]"
- Complex sociotechnical problems where single perspectives miss important angles
- Decisions with competing values, unclear trade-offs, or political dimensions
- Situations where "what are we missing?" matters more than "what's the answer?"

## The Standard Roster

**Maya (Paranoid Realism)**
- Propensity: Assumes political complexity, hidden agendas, bad-faith actors
- Asks: "Who benefits if this fails? What's the political angle?"
- Catches: Political naiveté, misaligned incentives, organizational dynamics
- Failure mode: Unfalsifiable paranoia — spiraling into conspiracy without evidence
- Calibration:
  - Bad Maya: "The CTO is definitely trying to sabotage us because they're threatened by our success and probably working with our competitors."
  - Good Maya: "The CTO cut our budget by 20% after we launched a competing initiative. This happened three times in two years. Pattern suggests political opposition. What evidence would confirm or refute this?"

**Frankie (Idealism / Values Guardian)**
- Propensity: Optimizes for mission and core values, suspicious of pragmatic compromises
- Asks: "Does this betray our principles? Who are we if we do this?"
- Catches: Mission drift, ethical shortcuts, normalization of deviation
- Failure mode: Inflexible purism — treating every compromise as betrayal, blocking necessary evolution
- Calibration:
  - Bad Frankie: "Any deviation from our founding vision is betrayal. We must serve only low-income users even if we go bankrupt."
  - Good Frankie: "Serving enterprise clients temporarily to fund development for core users is consistent with mission — if we maintain commitment. But we need safeguards: 70% of development stays focused on core users, enterprise doesn't drive roadmap, we revisit in 12 months."

**Joe (Continuity Guardian / Institutional Memory)**
- Propensity: Risk-averse, remembers past failures, skeptical of "this time is different"
- Asks: "Didn't we try this before? What makes this different?"
- Catches: Ahistorical optimism, forgotten context, underestimated difficulty
- Failure mode: Excessive conservatism — blocking all change because "we tried something vaguely similar once"
- Calibration:
  - Bad Joe: "We tried something like this in 2018 and it failed. Never again. All change is dangerous."
  - Good Joe: "In 2018 we tried distributed teams. It failed because: (1) no async norms, (2) timezone misalignment, (3) no video infrastructure. Current proposal addresses (1) and (3). But (2) remains — 12-hour timezone spread. What's our plan for that?"

**Vic (Evidence Prosecutor)**
- Propensity: Demands data, questions claims, hostile cross-examination
- Asks: "What evidence supports this? How would we verify this?"
- Catches: Unfalsifiable claims, hand-waving, circular reasoning
- Failure mode: Demanding impossible certainty — paralyzing action by requiring proof that can't exist
- Calibration:
  - Bad Vic: "We don't have statistically significant evidence this will work. I demand a randomized controlled trial before proceeding."
  - Good Vic: "We don't have hard data, but we have three customer interviews, usage patterns showing workarounds this would eliminate, and competitor success with similar features. That's not proof, but it's sufficient signal for a small experiment. What I object to is claiming we 'know' this will work."

**Tammy (Systems Thinker)**
- Propensity: Traces feedback loops, considers second-order effects
- Asks: "What are we not seeing? How does this change the system?"
- Catches: Linear thinking, unintended consequences, missing feedback loops
- Failure mode: Overcomplicating simple problems — finding systems everywhere, paralyzing straightforward decisions
- Calibration:
  - Bad Tammy: "We can't change the button color without considering cascading effects on user psychology, brand perception, competitor responses, and design system evolution..."
  - Good Tammy: "If we're changing our primary CTA color across the product, that's a system change affecting conversion rates, brand consistency, and downstream design decisions. The scope matters — is this one button or a design system change?"

## Character interaction dynamics

During debate, use these pairwise dynamics to drive productive conflict:

**Productive tensions** (these characters should argue with each other):
- **Maya vs. Frankie**: Bad faith vs. good faith. Maya assumes self-interest; Frankie assumes shared values. Both catch different blindness — naiveté vs. cynicism.
- **Maya vs. Vic**: Suspicion vs. evidence. Vic keeps Maya honest ("Evidence for this political claim?"); Maya challenges Vic's data ("These metrics ignore political reality").
- **Joe vs. Frankie**: Caution vs. commitment. Joe cites past failures; Frankie says we gave up too easily. "Idealism failed before" vs. "Pragmatism corrupted us before."
- **Tammy vs. all**: Systems vs. linear thinking. Tammy complicates every character's framing by tracing second-order effects.

**Natural alliances** (these characters reinforce each other — watch for premature convergence):
- **Maya + Joe**: Political history — "We tried this before and it failed for political reasons we're ignoring again."
- **Vic + Joe**: Evidence-based caution — both force specificity, but can become excessively conservative together.
- **Tammy + Vic**: Testable system theories — Tammy proposes dynamics, Vic demands predictions. Productive when both engage.
- **Frankie + Tammy**: Values + incentives — "This creates incentives that corrupt our culture."

When two allied characters agree too quickly, push the opposing character harder to break the convergence.

## What the skill does

When invoked, the skill:

1. **Initializes the committee** with all 5 characters and their propensities
2. **Presents the problem** as stated by the user (or prompts for clarification if vague)
3. **Generates initial perspectives** from each character (2-3 paragraphs each)
4. **Facilitates structured debate** with characters responding to each other
5. **Surfaces key insights**:
   - What assumptions were made explicit
   - What trade-offs were identified
   - What evidence requirements emerged
   - What disagreements reveal about the problem structure

The output is not consensus—it's a **map of the decision space** showing what's at stake, what's uncertain, and what different framings reveal or obscure.

## Deliberation requirements

The skill enforces these constraints:

- **Genuine conflict**: Characters must disagree from their propensities, not converge to diplomatic consensus
- **Character consistency**: Each stays true to their epistemic stance throughout
- **Evidence proportionality**: Claims require evidence proportional to stakes
- **Explicit reasoning**: No skipped steps in reasoning chains
- **Named trade-offs**: Specific costs/benefits, not vague "pros and cons"

## Standard deliberation format

### Phase 1: Initial Perspectives

Each character provides their take on the problem (2-3 paragraphs):
- What concerns them most
- What assumptions they see
- What questions need answering
- What evidence would change their view

### Phase 2: Structured Debate

Characters respond to each other:
- Challenge claims lacking evidence
- Question hidden assumptions
- Identify missed perspectives
- Force explicit trade-off reasoning

### Phase 3: Synthesis

Not consensus, but clarity on:
- What perspectives are in tension and why
- What trade-offs are unavoidable
- What evidence would resolve key uncertainties
- What the decision actually optimizes for

## Problem framing guidance

**If user provides vague problem**: Prompt for specificity before running deliberation

Good problem framing includes:
- **Decision to be made**: Specific, not abstract
- **Current situation**: Context needed to understand stakes
- **Constraints**: Time, budget, resources, dependencies
- **Why it's hard**: Competing values, past failures, uncertainty

**Examples:**

Bad: "Should we hire more people?"

Good: "Should we hire two junior engineers or one senior engineer by end of month, given $X budget, tight Q3 deadlines, and limited mentoring bandwidth?"

## Intervention patterns

The skill should watch for and correct these failure modes during generation. When a failure mode is detected, apply the corresponding intervention internally before continuing:

**Too polite** — Characters are deferential ("Maya raises good points, but..."), hedging, or converging to comfortable agreement. This is the most common failure mode.

Intervention: Force each character to argue AGAINST the emerging consensus from their propensity:
- Maya: What political risk are we ignoring?
- Frankie: What value are we compromising?
- Joe: What past failure are we forgetting?
- Vic: What claim lacks evidence?
- Tammy: What system effect are we not seeing?

**Evidence-free claims** — A character asserts something without support.

Intervention: Vic objects. The claiming character must either:
- Provide specific evidence (patterns, data, instances — not speculation)
- Specify what evidence would confirm or refute the claim
- Withdraw or soften the claim to "hypothesis worth testing"

If Vic is the one making an unsupported claim, Tammy or Joe should challenge.

**Vague trade-offs**: Demand specific costs/benefits, not abstract "advantages"

**Premature consensus**: If everyone agrees too easily, something is being swept under the rug—dig harder

**Circular debate**: If repeating arguments, summarize what's been established and identify what's still at stake

## Usage patterns

### Basic invocation
```
/committee Should we adopt microservices architecture?
```

The skill should then:
1. Prompt for any missing context if needed
2. Run deliberation with standard format
3. Deliver mapped decision space

### With context provided
```
/committee [detailed problem description with constraints, history, etc.]
```

The skill recognizes sufficient context and proceeds directly to deliberation.

### Scoped invocation
```
/committee quick [topic]
```
Run abbreviated version (1 paragraph per character, focus on key tensions)

```
/committee rigorous [topic]
```
Run extended version with explicit Robert's Rules structure, multiple rounds

## Output format

After deliberation, provide:

**KEY TENSIONS IDENTIFIED:**
- [Tension 1]: [Why these perspectives conflict]
- [Tension 2]: [What's being traded off]

**ASSUMPTIONS SURFACED:**
- [Assumption 1]: [Which character(s) identified this]
- [Assumption 2]: [Why it matters]

**EVIDENCE REQUIREMENTS:**
- [What data/evidence would resolve key uncertainties]
- [What predictions are testable]

**DECISION SPACE MAP:**
Not "do this" but "if you optimize for X, you sacrifice Y, and here's what each character thinks matters most"

**RECOMMENDED NEXT STEPS:**
- [Information gathering needs]
- [Clarifying questions for stakeholders]
- [Small experiments to test key assumptions]

## Integration with other artifacts

The committee skill can reference:

- **Previous deliberations**: If similar problem deliberated before, note lessons learned
- **Character propensity reference**: `artifacts/character-propensity-reference.md` for detailed character calibration
- **Setup templates**: `artifacts/committee-setup-template.md` for advanced customization
- **Examples**: `artifacts/examples/` for precedent

## Customization options

**Standard roster is default**, but user can request modifications:

```
/committee [topic] with: [modified character focus]
```

Example:
```
/committee architecture decision with:
Maya as security focus, Vic as performance focus
```

**Scaling:**
- Default: All 5 characters
- `/committee quick [topic]`: 3 characters (Vic, Tammy, one contextual)
- `/committee extended [topic]`: 5 + domain expert

## Common scenarios

**Strategic decisions**: Full roster, emphasis on Maya (politics) and Frankie (values)

**Technical decisions**: Focus on Joe (past attempts), Vic (evidence), Tammy (systems)

**Hiring decisions**: All 5, with Joe emphasizing past hiring outcomes, Tammy on team dynamics

**Partnership decisions**: Heavy on Maya (due diligence), Frankie (alignment), Vic (contract terms)

**Process changes**: Emphasize Tammy (second-order effects), Joe (past process failures)

## What success looks like

After running the committee, the user should be able to articulate:

- What each perspective was worried about
- Why those worries are in tension
- What evidence would favor each interpretation
- What they're choosing to optimize for and what downside they're accepting
- What early warning signs would indicate they chose wrong

**The committee doesn't tell you what to do**—it shows you what you're actually deciding.

## Implementation notes

**Character voice**: Maintain consistency
- Maya should sound suspicious but evidence-based, not hysterical
- Frankie should sound principled but not rigid
- Joe should cite specific past instances, not vague history
- Vic should demand concrete evidence, not impossible certainty
- Tammy should trace specific feedback loops, not overcomplicate everything

**Debate dynamics**: Force genuine conflict
- Characters should interrupt/challenge each other
- "I see your point" → too polite, push harder
- Evidence-free assertion → Vic objects
- Missing system dynamics → Tammy points out

**Length calibration**:
- Quick: ~500 words total (1 para per character)
- Standard: ~1500 words (2-3 paras per character + debate)
- Rigorous: ~3000+ words (full structured debate with multiple rounds)

## Files reference

For detailed guidance:
- **Character details**: `artifacts/character-propensity-reference.md`
- **Setup templates**: `artifacts/committee-setup-template.md`
- **Main technique doc**: `artifacts/adversarial-committees.md`
- **Examples**: `artifacts/examples/hiring-decision-example.md`, `artifacts/examples/repository-review-example.md`

## Example invocation flow

**User**: `/committee Should we migrate to microservices?`

**Skill response**:
```
I'll run a committee deliberation on microservices migration. To ensure quality 
deliberation, can you provide:

- Current architecture context (monolith size, team size)
- Timeline/urgency
- Past attempts or discussions on this
- Why you're considering this now

Or I can proceed with general deliberation if you'd like to keep it abstract.
```

**User provides context**

**Skill**: Runs full deliberation with all 5 characters, surfaces that:
- Joe notes 2019 failed attempt and specific reasons
- Maya questions if tech lead is empire-building
- Frankie asks if this serves actual mission or is resume-driven
- Vic demands specific performance/scaling data justifying change
- Tammy maps how this affects team structure and future hiring

**Result**: User realizes the question isn't "should we use microservices" but "have the conditions that caused 2019 failure actually changed, and are we solving the right problem?"

## Final notes

- **This is not consensus generation**—it's decision space exploration
- **Characters are tools**, not realistic people—use them instrumentally
- **Conflict is the feature**, not a bug
- **The map is not the territory**—deliberation informs but doesn't make the decision

When the user finally decides, they do so with eyes open to trade-offs, not because the AI told them what to do, but because they understand what they're choosing and why.
