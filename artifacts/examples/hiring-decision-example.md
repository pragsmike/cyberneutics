---
type:
  template: committee-deliberation-with-review
  rubric: evaluation-rubrics-reference-v1
charter: >
  Whether to extend a hiring offer to "Alex," a high-productivity engineer
  with reported interpersonal difficulties, given a team with existing
  psychological safety norms and significant technical debt.
deliberation:
  date: 2025-05-14
  variant: standard (3 rounds, Robert's Rules invoked Round 2)
  roster: [Maya, Frankie, Joe, Vic, Tammy]
  outcome: "Conditional hire — pair programming test with junior staff required before offer"
review:
  date: 2026-02-16
  rubrics-applied:
    - reasoning-completeness
    - adversarial-rigor
    - assumption-surfacing
    - evidence-standards
    - trade-off-explicitness
  aggregate-score: 1.6
  verdict: Medium
  methodology: independent-evaluation-protocol-v1
provenance:
  deliberation-source: artifacts/examples/hiring-decision-example.md (original)
  review-skill: .claude/skills/review/SKILL.md
  rubric-reference: artifacts/evaluation-rubrics-reference.md
  theory-reference: artifacts/independent-evaluation.md
---

# Example: The "10x Engineer" Hiring Decision

This worked example demonstrates the Cyberneutics methodology applied to a high-stakes hiring decision, followed by an independent review that scores the deliberation against the five core evaluation rubrics.

It shows how the "Adversarial Committee" structure (the Inner Game) wins against the "Stochastic Imps" of entropy (bias, halo effects, and wishful thinking) that typically plague hiring — and how independent evaluation reveals where even a good deliberation falls short.

## The Problem

**Scenario**: You are a CTO. You have a chance to hire "Alex," a brilliant engineer known for 10x productivity but also rumored to be "difficult" and "abrasive." The team is split. The codebase is a mess and needs saving. Alex could save it—or kill the culture.

**The Temptation**: Hire the genius. Save the product. Hope the culture survives.

**The Stochastic Imp**: Your brain (and a standard LLM) will generate a soothing narrative: *"Brilliance is rare; we can manage the personality; the code is the priority."*

## The Committee Roster

We empanel the standard Adversarial Committee to fight this narrative.

*   **Maya (The Paranoid)**: Winning condition = Finding the hidden cost of the hire.
*   **Frankie (The Idealist)**: Winning condition = Maximizing the potential upside.
*   **Vic (The Skeptic)**: Winning condition = Demanding proof of "10x" impact.
*   **Joe (The Continuity Guardian)**: Winning condition = Protecting existing team cohesion.
*   **Tammy (The Systems Thinker)**: Winning condition = Mapping second-order effects.

---

## Round 1: The Deliberation

**Chair (User)**: The motion is to extend an offer to Alex.

**Frankie (Idealist)**: I move we hire. Look at the GitHub portfolio. This isn't just code; it's poetry. The refactoring they did on the Stripe integration in 4 hours took our current team three weeks. We are dying of technical debt. Alex is the medicine. We can't let "vibes" kill actual excellence.

**Joe (Continuity)**: Objection. "Medicine" can be poison. I talked to his reference from the last startup. They said, "Alex writes great code, but two junior devs quit within three months of him joining." We spent two years building a psychological safety net for this team. You drop a shark in the tank, you don't get a faster tank. You get a bloody tank.

**Vic (Skeptic)**: Hold on. Let's look at the "10x" claim. Frankie, you cited the Stripe integration. That was a solo project. Effective immediately. But our codebase is a monolith with six years of legacy cruft. Does Alex's velocity hold up when they have to negotiate with three other teams? Or does he just rewrite everything in Rust and leave us with unmaintainable alien tech? Show me the evidence of him collaborating, not just soloing.

**Maya (Paranoid)**: It's worse than that. Why is he available? If he's a 10x god, why isn't he founding his own thing or getting retained by Google? The reference Joe cited... notice what they *didn't* say. They didn't say "we miss him." They said "he writes great code." That's the sound of a legal department approving a neutral references policy to avoid a lawsuit. There's a hidden liability here.

**Tammy (Systems)**: Let's trace the feedback loop. We hire Alex. He rewrites the core. It works. The rest of the team feels stupid and marginalized because Alex doesn't document or explain—he just "solves." They disengage. Velocity goes *up* for Alex, but *down* for the other 8 developers. Net system velocity... likely negative. We are optimizing a node at the expense of the network.

**Frankie**: But we're *already* at negative velocity! The ship is sinking. You don't ask the guy with the bucket if he's nice. You ask if he can bail.

**Maya**: Unless he drills a hole in the hull to let the water out faster.

---

## Round 2: The Rules (Forcing Function)

**Chair**: The debate is circular. Invoking Robert's Rules. I need a motion to amend.

**Vic**: I move to amend the proposal: "Hire Alex on a 3-month contract-to-hire basis, with explicit solo-project isolation."

**Maya**: Objection. He'll behave for 3 months. That's the honeymoon. The toxicity is a long-tail risk.

**Tammy**: Second the objection. Isolation defeats the purpose. If he's isolated, he's not fixing the core debt. If he's touching the core, he's touching the team.

**Chair**: Motion fails. I need a new motion to structure the decision criteria.

**Joe**: I move that we require a "Do No Harm" interview. Put him in a room with our two most junior devs for a pair programming session. If they come out feeling small, it's a hard no. No matter how good the code is.

**Frankie**: I'll second that. If he's really a genius, he should be able to teach. If he can't teach, he's not a 10x engineer, he's just a 10x coder. There's a difference.

**Vic**: Accepted. That's an evidentiary standard. We move from "rumors of abrasion" to "observed interaction."

---

## Round 3: The Verdict

**Chair**: The proposal is: *Reject the immediate offer. Schedule a pair-programming session with junior staff. If and only if that passes, offer a position with a rigorous Code of Conduct addendum.*

**Voting:**
*   **Frankie**: Aye. (Wants the talent, accepts the test).
*   **Joe**: Aye. (Protects the team).
*   **Vic**: Aye. (Generates new evidence).
*   **Maya**: Abstain. (Still thinks the risk is concealed, but the test is better than nothing).
*   **Tammy**: Aye. (System test).

**Outcome**: Motion carries.

---

## Independent Review

*The transcript above was passed to a fresh evaluator instance with no context beyond the text itself, scored against the five core rubrics from the [Evaluation Rubrics Reference](../evaluation-rubrics-reference.md). See [Independent Evaluation Protocols](../independent-evaluation.md) for the methodology.*

### Charter

Whether to extend a hiring offer to "Alex," an engineer with demonstrated high productivity but reported interpersonal difficulties, given a team with existing psychological safety norms and significant technical debt.

### Rubric Scores

**1. Reasoning Completeness: 2/3**

Most reasoning chains are traceable but several contain gaps that require reader inference.

*Strong chains:*
- Tammy's feedback loop is the most complete reasoning in the transcript: hire Alex → he rewrites without documenting → team feels marginalized → team disengages → individual velocity up but team velocity down → net negative. Every step is shown with a mechanism.
- Vic's challenge to the 10x claim draws a clear distinction: Stripe integration was solo work; the actual codebase requires cross-team negotiation. The conclusion (solo velocity ≠ collaborative velocity) follows from the premise.

*Incomplete chains:*
- Joe cites that "two junior devs quit within three months" but doesn't establish the causal mechanism. Did they quit *because of* Alex? Were there confounding factors? Joe leaps from temporal proximity to causation.
- Maya's inference about the reference ("That's the sound of a legal department approving a neutral references policy") is colorful but unfalsifiable as stated. What evidence distinguishes "neutral reference due to legal caution" from "neutral reference because the person was fine but unremarkable to work with"?
- Frankie's claim that the Stripe refactoring "took our current team three weeks" versus Alex's "4 hours" is presented as fact but never examined. Is this an apples-to-apples comparison? Same scope? Same constraints? The implied 75x productivity multiplier is accepted without scrutiny.

*What would raise this to 3:* Joe needs to establish causation (not just correlation) for the junior dev departures. Maya needs to distinguish her interpretation of the reference from alternative explanations. Frankie's productivity comparison needs to be interrogated for validity — Vic started this but didn't finish it.

**2. Adversarial Rigor: 2/3**

Genuine conflict exists — characters directly engage with each other's claims — but several challenges are dropped rather than pursued to resolution.

*Strong engagement:*
- Vic directly challenges Frankie's 10x claim by distinguishing solo from collaborative work: "Show me the evidence of him collaborating, not just soloing." This is a real challenge that reframes the evidentiary basis.
- Maya and Tammy's joint objection to Vic's contract-to-hire motion is substantive: Maya argues the trial period is too short to surface long-tail risk, Tammy argues isolation is self-defeating. The motion fails on merit.
- Maya's one-liner ("Unless he drills a hole in the hull to let the water out faster") is a direct counter to Frankie's sinking-ship metaphor that reframes the same image.

*Dropped challenges:*
- Vic asks Frankie to "show me the evidence of him collaborating, not just soloing" — but this challenge is never answered. The debate moves on. This is the central evidentiary question and it goes unresolved.
- No one challenges Tammy's systems claim. "Net system velocity... likely negative" is asserted but the word "likely" hides a probabilistic claim with no basis. Vic, the evidence prosecutor, lets this pass entirely.
- Frankie's claim that they're "already at negative velocity" — a strong claim about current team state — is never examined. This assertion shapes the urgency framing for the entire deliberation.

*What would raise this to 3:* Vic's challenge to the 10x claim needs to be answered, not abandoned. Tammy's "likely negative" needs interrogation. Frankie's "already at negative velocity" needs evidence or withdrawal.

**3. Assumption Surfacing: 1/3**

Characters operate from strong assumptions throughout, but these are mostly implicit rather than named and examined.

*Partially surfaced:*
- The committee implicitly operates with competing optimization criteria — Frankie optimizes for technical capability, Joe for team cohesion, Maya for risk avoidance — but nobody names this conflict explicitly. No one says "we're optimizing for different things and need to choose."
- Frankie's "10x engineer vs. 10x coder" distinction in Round 2 surfaces one assumption (that teaching ability is part of engineering excellence), but this is a new assertion rather than an examination of prior assumptions.

*Major unsurfaced assumptions:*
- **That Alex is actually as good as claimed.** The entire deliberation takes the "10x" premise as given and debates whether to accept the associated risk. Vic gestures at this but doesn't follow through.
- **That the technical debt crisis requires a single brilliant hire.** The committee never examines alternatives: Could two solid senior engineers address the debt without the cultural risk? Is the debt actually the binding constraint?
- **That the pair programming test will be diagnostic.** Joe proposes it, Frankie seconds it, Vic endorses it — and nobody asks whether a single session can actually surface toxicity. Maya abstains but doesn't articulate why the test is insufficient.
- **What "psychological safety" means operationally** and how it would be measured as degraded. Joe spent "two years building" it — what does that mean concretely? How fragile is it?

*What would raise this to 2-3:* Characters need to name their optimization criteria explicitly and acknowledge the conflict. The "10x" premise itself needs examination. The deliberation needs to surface the meta-assumption that this is a binary hire/don't-hire decision — alternatives to hiring Alex specifically are never discussed.

**4. Evidence Standards: 2/3**

Evidence is demanded in several places but inconsistently enforced, and some significant claims pass without challenge.

*Good evidence discipline:*
- Vic's challenge to the 10x claim is a genuine evidentiary demand: solo performance ≠ collaborative performance, show me the collaborative evidence.
- Joe cites a specific reference ("two junior devs quit within three months"). This is at least a concrete data point, even if the causal inference is weak.
- The committee's final decision — to gather new evidence via pair programming rather than decide on existing evidence — is itself an evidence-respecting move.

*Evidence failures:*
- Frankie's "4 hours vs. three weeks" comparison is never subjected to scrutiny. This is the foundational claim for Alex's value and it passes unchallenged.
- Maya's reading of the reference language is unfalsifiable as presented. Nobody asks what evidence would distinguish Maya's interpretation from alternatives.
- Tammy's feedback loop, while structurally complete, has no evidential basis for any of its steps. "The rest of the team feels stupid and marginalized" — based on what? It's presented as inevitable system dynamics rather than as a hypothesis.
- Frankie's "already at negative velocity" — possibly the most important factual claim in the entire deliberation, since it establishes urgency — goes completely unexamined.

*What would raise this to 3:* Every factual claim needs challenge, not just the convenient ones. Frankie's productivity comparison, Frankie's negative-velocity claim, and Tammy's feedback loop all need evidentiary grounding or explicit labeling as hypotheses.

**5. Trade-off Explicitness: 1/3**

Trade-offs are gestured at but never specified with costs, time horizons, or decision criteria.

*What's present:*
- Tammy's node-vs-network framing implicitly identifies a trade-off (individual velocity vs. system velocity), but doesn't quantify either side.
- The committee's final proposal (conditional hire pending pair test) implicitly trades speed of decision for quality of evidence. But this trade-off isn't named.

*What's missing:*
- No quantification of any kind. How much technical debt exists? What's the cost of *not* hiring Alex in terms of product timeline? What's the cost of team attrition if the hire goes badly?
- No time horizons. If Alex is hired, when do we expect results? When do we expect cultural damage? The pair programming test is proposed without specifying what "pass" or "fail" looks like operationally.
- No comparison of alternatives. The deliberation treats this as "hire Alex with test" vs. "don't hire Alex." What about: hire a different senior engineer? Hire two mid-levels? Contract out the tech debt work?
- The final proposal's costs are unstated. Delaying the hire costs time. If Alex fails the test, they're back to square one.

*What would raise this to 2-3:* Name the cost of each option. Quantify where possible (even rough estimates). State time horizons. Compare the pair-programming-test path against at least one alternative. Make explicit: "By choosing this, we accept [specific cost] in exchange for [specific benefit]."

### Aggregate Score: 1.6/3.0

### Structural Assessment

**Charter fitness:** Good. The deliberation stays focused on the hiring question throughout. The evolution from "should we hire?" to "how do we generate better evidence before deciding?" is a legitimate and useful reframing. The committee didn't drift — it refined.

**Character calibration:** Mixed. Vic is well-calibrated in Round 1 (evidence-proportional challenge to the 10x claim) but goes quiet in Round 2 — the evidence prosecutor doesn't demand evidence for the pair programming test's validity. Maya is colorful and specific but edges toward unfalsifiable interpretation (the reference-language reading). Joe is appropriately concrete (cites specific reference) but makes a causal leap. Frankie is the most consistent — clearly advocates from propensity, shifts position when presented with a test that could vindicate the hire. Tammy delivers one strong systems contribution but then fades; the systems thinker should have had more to say about the pair programming test as a system intervention.

**Engagement depth:** Moderate. The debate genuinely evolves from Round 1 (should we hire?) through Round 2 (how do we structure the decision?) to Round 3 (conditional protocol). Characters respond to each other, not just to the question. However, several threads are dropped rather than resolved — particularly Vic's collaboration-evidence challenge and the question of whether the tech debt crisis actually requires this specific hire.

**Synthesis quality:** The final proposal (conditional hire with pair programming test) is a genuine third option — better than binary yes/no. Maya's abstention honestly represents unresolved tension rather than forcing consensus. However, the synthesis doesn't map what was left unresolved: the unanswered question about collaborative evidence, the unexamined urgency claim, the unconsidered alternatives.

### Biggest Gaps

1. **The alternative-free decision frame.** The entire deliberation assumes the choice is "Alex or no Alex." No one asks "what else could we do about the tech debt?" This artificially narrows the trade-off space and inflates Alex's apparent necessity. This is the most consequential gap because it shapes every other judgment in the transcript.

2. **Unexamined urgency.** Frankie's "already at negative velocity" and "the ship is sinking" establish a crisis framing that drives the deliberation toward speed over caution. This factual claim is never examined. If the team is *not* actually at negative velocity, the entire risk calculus changes. Vic should have caught this.

3. **The pair programming test is accepted uncritically.** The committee's final proposal rests entirely on this test's ability to surface toxicity in a single session. Nobody asks: Is one session enough? What specific behaviors constitute a "fail"? Can a skilled manipulator pass this test while still being toxic over six months? Maya's abstention gestures at this concern but doesn't articulate it.

### What Would Most Improve This Deliberation

1. **Have Vic challenge Frankie's urgency claim.** "You say we're at negative velocity. What's the evidence? What's our actual sprint velocity trend? If the situation is less dire than you claim, does that change the risk calculus?"

2. **Have someone — probably Tammy — introduce alternatives.** "We're debating Alex specifically. But the actual problem is technical debt. What are three other ways to address it? How do those options compare on risk, cost, and timeline?"

3. **Have Vic interrogate the pair programming test.** "What does 'pass' look like, operationally? What does 'fail' look like? What's the false-negative rate — can someone be toxic at scale but fine in a single observed session?"

### Verdict

**Trustworthiness as decision input: Medium**

The deliberation successfully generates a third option (conditional hire with evidence-gathering test) that is genuinely better than binary yes/no. Characters engage with each other, not just the question. But the decision rests on an unexamined urgency claim, an artificially narrow option space, and an untested testing protocol. A decision-maker using this output should treat it as a starting point that needs the three improvements above before it becomes reliable.

---

## Lessons Extracted

1.  **The "Genius" Trap**: The "Stochastic Imp" narrative wants to tell a story about a Savior Engineer. The committee successfully broke this by framing high-performance as a system attribute (Node vs. Network), not an individual attribute.
2.  **Brilliance is a Lagging Indicator**: We can see code he *already* wrote.
3.  **Toxicity is a Leading Indicator**: How he treats people *now* predicts future system velocity.
4.  **The Third Option**: The adversarial process didn't just pick a winner (Hire vs. No Hire); it generated a new protocol (The Junior Pair Test) that changed the information landscape.
5.  **Independent review reveals invisible gaps.** The original deliberation *felt* rigorous — characters argued, a motion failed, a third option emerged. The review exposed that the urgency claim driving the deliberation was never examined, the option space was artificially narrow, and the proposed test was accepted without the same rigor applied to the hiring decision itself. Theater can be sophisticated.

## Why This Worked

If you had asked a generic LLM "Should I hire a toxic genius?", it would have given you a bland "On the one hand... on the other hand..." bulleted list.

By **playing the game**—giving roles winning conditions and forcing them to argue—we simulated the actual social complexity of the decision and arrived at a specific, actionable protocol (The Pair Test) rather than generic advice.

By **reviewing the game**—passing the transcript to an independent evaluator—we discovered that the deliberation, despite feeling rigorous, had meaningful gaps: an unexamined urgency premise, a missing alternative analysis, and an untested test. The review doesn't invalidate the deliberation; it tells you exactly where to push harder.
