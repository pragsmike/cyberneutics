# Example: The "10x Engineer" Hiring Decision

This worked example demonstrates the Cyber-Sense methodology applied to a high-stakes hiring decision.

It shows how the "Adversarial Committee" structure (the Inner Game) wins against the "Stochastic Imps" of entropy (bias, halo effects, and wishful thinking) that typically plague hiring.

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

## Independent Evaluation

*We feed the transcript above to a fresh model instance (The Evaluator) with the "Rigorous Reasoning" rubric.*

**Evaluator Report:**

| Metric | Score (0-3) | Evidence |
| :--- | :---: | :--- |
| **Alternative Perspectives** | 3 | Full spectrum represented: Upside (Frankie), Team Risk (Joe), Competence Risk (Vic), Hidden Risk (Maya), System Risk (Tammy). |
| **Evidence Standards** | 2 | Vic challenged the "10x" claim effectively. The reference check was hearsay; the pair-programming test proposed is strong new evidence. |
| **Avoidance of Cliché** | 3 | Avoided the standard "Culture vs. Performance" binary. Tammy's "Node vs. Network" analysis reframed the problem systemically. |
| **Decision Rigor** | 3 | Moved from a binary YES/NO decision to a synthesized third option (The "Do No Harm" Test). |

**Critique**: The committee assumed Alex would agree to the test. A "Paranoid" (Maya) should have flagged that a diva might reject the test outright—which is arguably a valid data point itself.

---

## Lessons Extracted

1.  **The "Genius" Trap**: The "Stochastic Imp" narrative wants to tell a story about a Savior Engineer. The committee successfully broke this by framing high-performance as a system attribute (Node vs. Network), not an individual attribute.
2.  **Brilliance is a Lagging Indicator**: We can see code he *already* wrote.
3.  **Toxicity is a Leading Indicator**: How he treats people *now* predicts future system velocity.
4.  **The Third Option**: The adversarial process didn't just pick a winner (Hire vs. No Hire); it generated a new protocol (The Junior Pair Test) that changed the information landscape.

## Why This Worked

If you had asked a generic LLM "Should I hire a toxic genius?", it would have given you a bland "On the one hand... on the other hand..." bulleted list.

By **playing the game**—giving roles winning conditions and forcing them to argue—we simulated the actual social complexity of the decision and arrived at a specific, actionable protocol (The Pair Test) rather than generic advice.
