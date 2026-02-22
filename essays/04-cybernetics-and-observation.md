# Cybernetics and the Observer Problem

> "Objectivity is the delusion that observations could be made without an observer." — Heinz von Foerster

## The Loop You Can't Step Out Of

Traditional science (and traditional engineering) is built on **First-Order Cybernetics**.

In First-Order Cybernetics, the engineer stands outside the system. You look at the engine. You tweak a valve. The engine runs differently. You measure the output. You are the god-like operator, distinct from the machine.

This is a useful fiction for steam engines. It is a disastrous fiction for Narrative Engines.

**Second-Order Cybernetics** is the cybernetics of observing systems. It recognizes a fundamental truth: **You cannot observe a complex system without being part of it.**

When you interact with an LLM, you are not "measuring" its knowledge. You are coupling with it. Your prompt doesn't just retrieve information; it alters the system's state. It sets the initial conditions for a trajectory that wouldn't exist without your specific observation.

## Prompting is Control Theory

We need to stop thinking of prompts as "queries" (database metaphor) or "instructions" (programmer metaphor).

**A prompt is a control signal.**

In control theory, you inject a signal into a dynamic system to steer its behavior.
*   **The System**: The LLM's vast, high-dimensional latent space.
*   **The Signal**: Your text input.
*   **The Trajectory**: The generated text.

When you refine a prompt, you are not "fixing code." You are adjusting the gain on a feedback loop. You are trying to find the control sequence that steers the system's trajectory through the region of the latent space that aligns with your intent.

But unlike a mechanical system, the "steersman" (cybernetes) is changed by the output.

1.  You ask a question.
2.  The model answers.
3.  The answer changes your understanding of the problem.
4.  You ask a *different* question.

This is a coupled oscillator. You and the AI are two dynamic systems adjusting each other's states in real-time.

## The Physics of Deleuze: Actualization via Observation

This is where the engineering of Cybernetics meets the metaphysics of [Deleuze](./06-deleuze-difference-repetition.md). The concepts below — virtuality, actuality, actualization — receive their full philosophical treatment in [Essay 06](./06-deleuze-difference-repetition.md). What follows is a working sketch: enough to see how they connect to cybernetics, without the full philosophical apparatus.

Deleuze argues that reality consists of a **Virtual** field (potentials) that gets collapsed into **Actual** existence.
Cybernetics provides the mechanism for this collapse: **Observation.**

### The Virtual Field
The LLM's weights are the Virtual. They contain the potential for every possible sentence the model could generate. But they contain no *actual* sentences. Just tendencies, probabilities, and latent structures.

### The Actualization
When you observe the system (prompt it), you force it to collapse that infinite potential into a specific string of tokens. You have **actualized** the virtual.

But here is the catch: **How you observe determines what actualizes.**

If you observe the system with a "Schoolteacher" persona ("Grade this essay"), you actualize a critical, pedantic trajectory.
If you observe it with a "Collaborator" persona ("Help me improve this"), you actualize a supportive, constructive trajectory.

Measurement creates the reality. The "facts" the model produces are not sitting in a database waiting to be found. They are produced on the fly by the collision between the Virtual field and your Observer constraint.

## Eigenforms: How Stability Emerges from Noise

If everything is a loop of becoming, how does anything ever stay still? How do we get facts, stable meanings, or consistent personalities?

Heinz von Foerster gave the mathematical answer: **Eigenforms.**

Von Foerster developed the concept at the Biological Computer Laboratory (BCL) at the University of Illinois (1958–1975), the interdisciplinary hub he directed where cybernetics, cognition research, and experimental computing converged. The BCL brought together engineers, philosophers, biologists, and social scientists in a shared systems-oriented conversation — the kind of fertile collision between disciplines that second-order cybernetics both theorizes and requires. Von Foerster's radical constructivism — captured in his slogan "It is like I tell it," in contrast to "Tell it like it is" — grounded the eigenform concept in a broader epistemological commitment: observers don't discover pre-existing stable structures, they *participate in producing them*.

An eigenform is a recursive fixed point — a specific state that a function creates, which then creates itself.
xₜ₊₁ = F(xₜ)

If this loop stabilizes such that x = F(x), you have found an Eigenform.

In AI interaction, we are hunting for Eigenforms at multiple scales.

*   **Dialogue**: When you and the AI finally "get" each other, and the conversation flows effortlessly? You have entered a stable eigen-behavior.
*   **Conversational eigenforms**: Gordon Pask's Conversation Theory provides a complementary lens. For Pask, a conversation reaches an eigenform when both participants can correctly describe the other's understanding of a topic and that understanding persists under perturbation — when you can *teach back* the other's position and the teachback survives challenge. The entailment mesh (Pask's term for the network of mutually-supporting concepts that participants build through dialogue) is the residual structure that persists through conversational shocks. Eigenforms in dialogue are not just mathematical fixed points; they are **shared understandings that survive re-articulation**.
*   **Adversarial Committees**: We use the committee structure to *prevent* premature eigenforms. We don't want the system to stabilize on the first easy answer. We inject noise (character conflict) to kick the system out of shallow eigen-states, reshaping the function $F(x)$ until the only stable solution is a robust, well-reasoned truth. In Pask's terms: we force repeated teachback under adversarial conditions, so that only genuinely robust understandings survive.

**Eigenforms are the engineer's version of Deleuze's "becoming-stabilized."** They prove that you don't need fixed objects to have stability. You just need stable processes. Von Foerster showed this mathematically; Pask showed it conversationally; the adversarial committee operationalizes both.

For empirical validation of eigenforms and recursive stabilization in LLM reasoning—where trained models learn to simulate exactly these dialogic structures internally—see [Societies of Thought](./societies-of-thought-synthesis.md). For the full treatment of eigenforms — including premature convergence, deliberate destabilization, and the connection to Deleuzian process philosophy — see [Deleuzian Foundations](./06-deleuze-difference-repetition.md).

## The Observer's Responsibility

Understanding this changes how you use the tool.

If you treat the AI as an oracle (First-Order), you will accept its outputs as "true" or "false." You will say "The model hallucinated."

If you treat it as a coupled cybernetic system (Second-Order), you realize: **"My control signal steered the system into a hallucination regime."**

You stop blaming the car for going off the road and start looking at your hands on the wheel.

*   **You supply the context.**
*   **You set the temperature.**
*   **You define the persona.**
*   **You interpret the result.**

You are not the user. You are the Co-System.

### Explainability as First-Order Thinking

The demand for "explainable AI"—that we should be able to inspect why models produce their outputs—is a first-order cybernetic move. It wants to open the black box, examine the mechanism, understand the causal chain from input to output. "Show me the reasoning steps inside the model."

This makes sense for first-order systems where the observer stands outside. If you're debugging a rule-based expert system with explicit if-then logic, inspecting the reasoning chain is exactly the right approach. The system's behavior is determined by inspectable rules.

But large language models aren't rule-based systems. They're dynamical systems with millions of parameters trained through gradient descent. The "reasoning" (if we can call it that) is distributed across weights, emergent from training, and not localizable to inspectable steps. Demanding internal transparency is demanding the wrong thing from the wrong kind of system.

The second-order move is different: **observe the system dynamics, not the component internals**. Von Foerster's radical constructivism makes the point sharply: the demand for explainability assumes an objective world whose mechanisms we can lay bare. But second-order cybernetics reframes this — we are explaining how we *construct* our understanding, not how the system "really" works. The relevant question is not "what is the model doing internally?" but "what happens when we observe it under these conditions?"

Don't try to see inside the neural network. Instead, architect the interaction so the process becomes observable: multiple perspectives argue, claims get challenged, evidence gets cited, assumptions surface. The transcript is the observable. The discourse is the measurement.

This is the Shannon/von Neumann principle: reliable systems from unreliable components through composition and feedback. You don't need transparent parts if you have observable systems. The individual model responses remain opaque (statistically determined pattern completion), but the system of deliberation is legible (you can read the debate, see what survived scrutiny, verify what evidence was demanded).

First-order: "Explain why you said that" (trying to inspect the component).  
Second-order: "Let me observe how multiple perspectives interact and what survives cross-examination" (observing the system).

The unit of analysis shifts. Not the individual model's internals but the coupled system's behavior. Not "what reasoning did the neural network execute?" but "what arguments emerged when multiple perspectives were forced to contest?" The hermeneutic circle remains unbroken—the model that generated text will find it convincing—but we break the circle by introducing new observers (independent evaluation instances) who see only the artifact, not the generation process.

## Summary

1.  **AI interaction is a loop**, not a line.
2.  **Prompts are control signals**, steering a trajectory through a latent space.
3.  **Observation is Actualization**: You collapse the Deleuzian Virtual into the Actual through the act of querying.
4.  **Eigenforms are the goal**: We look for stable patterns that survive the recursive loop of questioning, answering, and questioning again.

We build these loops intentionally. That provides the "How."
Deleuze provides the "What."
And Dervin provides the "Why."

Together, they form the Cyberneutics machine.

---

**Related artifacts**:
- [Adversarial Committees](../artifacts/adversarial-committees.md) — the loop that forces divergence
- [Robert's Rules as Forcing Functions](../artifacts/roberts-rules-forcing-function.md) — the governor that prevents the loop from spinning too fast
- [Independent Evaluation Protocols](../artifacts/independent-evaluation.md) — breaking the hermeneutic circle

**Related essays**:
- [The Synthesis](./05-the-synthesis.md) — how the three frameworks (Dervin, cybernetics, Deleuze) compose
- [Deleuzian Foundations](./06-deleuze-difference-repetition.md) — the "What" that completes the machine
