# From Practice to Theory: How We Got Here; The Game within a Game

We didn't start with critical theory. We started with broken agents and a rigged game.

This essay explains the genesis of the Cyberneutics methodology: how practical engineering failures with Large Language Models (LLMs) led to a rediscovery of narrative theory, and why "treating the model like a committee" is actually a game-theoretic defense against entropy.

> *This is a personal narrative — the origin story of how the methodology emerged from practical frustration. It uses first-person voice; the other essays in this collection use "we" or "you."*

## The Engineering Problem: The Stochastic Imps

Like many early adopters, I began by treating LLMs as better search engines or smarter databases. I wanted them to solve problems: generate code, analyze data, make decisions.

And like everyone else, I hit the **plausibility wall**.

The models would produce outputs that looked perfect at first glance. They followed the genre conventions of a correct answer. They used the right terminology. They had the right structure.

But they were frequently, confidently, subtly wrong.

### The "Statistical Ghost"

I realized I wasn't interacting with a reasoning mind. I was interacting with a **statistical ghost** of human discourse—or what we might call the "stochastic imps of happenstance."

When I asked a question, the model wasn't "thinking." It was traversing a high-dimensional latent space to find the most probable completion for the pattern I had initiated. It was a **narrative engine**, conjuring a story about what an answer *should* look like based on its training data.

The model isn't malicious. It's just operating in an environment where the state space of "plausible sounding nonsense" is vastly larger than the state space of "truth." Entropy favors the nonsense. Murphy's Law isn't a curse; it's a probability distribution.

## The Pivot: Narrative as Feature, Not Bug

If the tool is a narrative engine, treating it like a calculator is a category error. You don't get mad at a car for not flying; you learn to drive.

I started asking: **If this thing is intrinsically a storyteller, what kinds of problems are best solved by telling stories?**

It turns out, almost all the important ones.

### Humans Are Narrative Engines Too

We like to think of ourselves as rational agents, but cognitive science suggests otherwise. We make sense of the world by constructing narratives.

*   **Legal Systems**: We don't just apply code; we tell stories about precedent and intent.
*   **Business Strategy**: We don't just optimize metrics; we tell stories about market position and future growth.
*   **Scientific Discovery**: We frame hypotheses as stories about how the universe might work, then try to break them.

Humans have faced "wicked problems"—problems with no single correct answer, where the definition of the problem itself is contested—for millennia. And our primary tool for handling them has been **adversarial narrative generation**.

### The Outer Game is Rigged

Here lies the core insight: **We cannot change the laws of the model (the Outer Game).**

The Outer Game is rigged by entropy; the stochastic imps will always try to pull the narrative toward the most generic, least-resistant path. If you just ask the model for an answer, you are playing the Outer Game, and the house eventually wins. It will give you the most probable, least interesting, statistically average answer.

But we can construct a **Game Within the Game**.

This is exactly what biological life does to cheat entropy (locally, anyway).

## Rediscovering the Committee

A game is just a specialized kind of narrative with explicit rules and roles. By imposing our own structure, we can constrain the entropy. We can build a "game" where the winning condition is rigor, not just plausibility.

How do humans make high-stakes decisions when truth is uncertain? We rarely do it alone.

We form committees. We empanel juries. We seek second opinions. We create structures where conflict is not a bug, but the method of discovery.

I decided to try this with the LLM. Instead of asking one agent for "the answer," I built a game with five players (Maya, Vic, Frankie, Joe, Tammy), each with a specific "winning condition":

*   **The Paranoid (Maya)** wins if she finds a hidden risk.
*   **The Skeptic (Vic)** wins if he destroys an unsupported claim.
*   **The Idealist (Frankie)** wins if he identifies a new opportunity.

Then I imposed a rule engine: **Robert's Rules of Order**, to constrain the chaos and force the players to engage.

### Why It Works: Constraining Latent Space

From a theoretical perspective, the "Committee" approach avoids the trap of the most probable path.

A single model query tends to collapse towards the mode of the distribution—the most generic, safe answer.

An adversarial committee forces the system to explore the **tails of the distribution**.
*   The Paranoid forces the narrative into the "failure mode" region of latent space.
*   The Idealist forces it into the "success scenario" region.
*   The rules act as a **forcing function**, preventing the conversation from looping or dissolving into incoherence.

We aren't creating consciousness. We are creating a **dynamic system of constraints**—a constructed game—that forces the narrative engine to generate something richer, more specific, and more rigorous than it would on its own.

## Connection to MOOLLM

This aligns perfectly with the philosophy behind **[MOOLLM](https://github.com/SimHacker/MOOLLM)** — Don Hopkins' project that builds a governance framework for LLMs. MOOLLM provides structured environments ("worlds") where AI interactions are constrained by explicit rules, roles, and protocols — a runtime for exactly the kind of structured narrative games this methodology requires. Hopkins frames it as a system of "games" and "worlds."

*   **MOOLLM** provides the engine to run the game (the physics, the objects, the protocols).
*   **Cyberneutics** designs the *rules* of the specific game we are playing (the Sense-Making Game).

## The Theory Emerges

This practical success led me backward into theory.

*   **Cybernetics**: The system (human + AI committee) is a feedback loop. My observation of the debate changes the debate. The system is steering itself through the problem space.
*   **Sense-Making**: We aren't "finding" the answer. We are *constructing* a bridge across a gap in our understanding, exactly as Brenda Dervin described.
*   **Narrative Rationality**: We are judging the output not just by logical validity, but by narrative coherence and fidelity to the constraints we set.

## Conclusion

This repository—**Cyberneutics**—is not a philosophy project. It is an engineering log.

The techniques documented here (Adversarial Committees, Robert's Rules, Independent Evaluation) are not abstract rituals. They are **strategies for winning the Inner Game**.

They are the "driving lessons" for the vehicle we actually have, rather than the "flying lessons" for the AGI we wish we had.

If we accept that LLMs are storytelling machines and impose game-theoretic constraints on them, we can stop trying to force them to be calculators. Instead, we can stop fighting the stochastic imps and start using these tools to help us write better, truer stories about the wicked problems we face.

---

**Next**: [Introduction to Sense-Making](./03-sensemaking-101.md) - The theoretical foundation for treating interpretation as cybernetic process
