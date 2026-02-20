# Cyber-Sense: Towards methodology for narrative computing

> If the tool is a narrative engine, treating it like a calculator is a category error. You don't get mad at a car for not flying; you learn to drive.

## Narrative computing

Each generation of computing hardware forced us to adapt how we think about expressing and solving problems. Each generation widened the class of problems they could help with.

*Numeric computing*: We framed our problems numerically when we got fast arithmetic machines.  
*Symbolic computing*: We framed problems in symbolic logic when we got bitstring crunchers.  
*Narrative computing*: Now we have storytelling engines, and we must learn to frame our problems as stories.  

As always, the computers won't completely solve the problems for us, but they can amplify our capacity to think them through.

[From Practice to Theory](./essays/02-from-practice-to-theory.md) tells the story of how these practices grew, and the theory used to guide their development.

The essay [Stories All the Way Down](./essays/stories-all-the-way-down.md) explains how everything is a story, how stories are a way to deal with wicked problems, and how we are constantly editing and re-editing the stories we tell ourselves about the world.

## What is Cyber-sense?

**Cyber-Sense** is a methodology for working with AI systems as collaborative sense-making partners rather than oracles that deliver answers.

It builds upon the runtime environment of **[MOOLLM](https://github.com/SimHacker/moollm)** (Don Hopkins) and aligns with the philosophy of **[Narrative Engineering](https://alexbo.land/essays/narrative_engineering_2023.html)** (Alex Boland). Think of it as: **MOOLLM is the platform, Cyber-Sense is the practice.**

> "We've never had narrative engines powerful enough to make this methodology necessary before."

Large Language Models are not databases. They are not logic engines. They are **narrative generators** - storytelling machines operating through what we call "the pachinko of stored literature." This changes everything about how we should work with them.

## Who is this for?

*   **Practitioners** working with AI on complex sociotechnical problems
*   **Researchers** exploring human-AI collaboration
*   **Anyone frustrated** with shallow AI outputs who suspects there's a better way
*   **Skeptics** wondering if this is just prompt engineering theater → [start here](essays/README.md#for-skeptics-show-me-why-this-matters)
*   **Theorists** interested in narrative computing, cybernetics, or sense-making

## Getting started

**New to these ideas?**
1.  **Read**: [Why Narrative Engines Change Everything](essays/01-why-narrative-engines-change-everything.md)
2.  **Try**: [Adversarial Committees](artifacts/adversarial-committees.md) (a concrete technique you can use today)

**Want the theory?**
*   Read the [Essays](essays/) in order, starting with [From Practice to Theory](./essays/02-from-practice-to-theory.md).
*   For the formal pipeline algebra, see [Decorated Texts](./palgebra/decorated-texts.md).
*   For curated reading paths by audience (Practitioner, Theorist, Skeptic), see the [Essays directory](essays/README.md#reading-paths).

**Want practical techniques?**
*   Start with the [Quick Start Guide](artifacts/quick-start-guide.md) — your first committee deliberation in 30 minutes.
*   Then explore the full [Artifacts](artifacts/) directory.

## Why does this matter?

Most AI interaction fails because we treat LLMs like search engines or calculators. We ask questions expecting definitive answers. But LLMs are most powerful when understood as **rapid story generators** that help us navigate complexity through narrative exploration.

The methodology documented here has produced:
- More rigorous problem analysis
- Better identification of blind spots and assumptions  
- Richer exploration of decision spaces
- More useful artifacts (not just chat transcripts)

These aren't incremental improvements. They represent a fundamentally different approach to human-AI collaboration.

## What's in this repository?

**[Essays](essays/)** - Theoretical foundations and synthesis
- [Why narrative engines change everything](./essays/01-why-narrative-engines-change-everything.md)
- [From practice to theory: how we got here](./essays/02-from-practice-to-theory.md)
- [Introduction to Sense-Making Methodology](./essays/03-sensemaking-101.md)
- [The Stochastic Imps of Happenstance](./essays/the-stochastic-imps-of-happenstance.md)
- Cybernetics and the observer problem
- The synthesis: why sense-making is inherently cybernetic
- [Societies of Thought: From Neural Evidence to Methodological Action](./essays/societies-of-thought-synthesis.md)

**[Artifacts](artifacts/)** - Practical techniques and protocols
- [Adversarial committees with fixed character rosters](./artifacts/adversarial-committees.md)
- Robert's Rules as forcing functions
- Independent evaluation protocols
- [Hiring Decision Example](./artifacts/examples/hiring-decision-example.md)
- [Worked examples and transcripts](./artifacts/examples/README.md)

**[Palgebra](palgebra/)** - Formal algebra for LLM pipelines
- **[Reference Card](./palgebra/reference.md)** — start here: syntax, operators, morphism types, propagation rules, composition laws
- **[Decorated Texts](./palgebra/decorated-texts.md)** — full essay developing the formalism from first principles (soft types, enrichment vs. transformation, confidence propagation, human gates as collapse operators)
- **[Committee as Palgebra](./palgebra/committee-as-palgebra.md)** — worked example: the adversarial committee pipeline formalized as resource equations
- Adapts Fong and Spivak's resource-theoretic framework (*Seven Sketches in Compositionality*, Ch. 2) to LLM pipelines. Three isomorphic representations: resource equations, string diagrams, and YAML-decorated artifact files

The essays describe *why* narrative engines need structured methodology. The artifacts provide *how* — concrete techniques like adversarial committees and evaluation rubrics. Palgebra provides *what, precisely* — a formal language for specifying pipelines, their types, their quality propagation, and their composition laws. An adversarial committee is a transformation morphism; a rubric evaluation is an enrichment morphism; a human review gate is a collapse operator. The formalism makes these relationships explicit and composable.

**[Applications](applications/)** - Domain analyses applying the framework to real-world phenomena
- [Narrative Immune Systems](./applications/narrative-immune-systems/) — information warfare, journalism, and the trust commons, analyzed through the immune analogy

**[References](references/)** - Background reading
- Dervin's Sense-Making Methodology
- Second-Order Cybernetics (von Foerster, Bateson)
- Deleuzian philosophy (becoming, difference, repetition)
- [Narrative Engineering](https://alexbo.land/essays/narrative_engineering_2023.html) (Alex Boland)

**Agent Skills** — Slash commands available when working with an AI agent on this repo

| Command | What it does | When to use |
|---------|-------------|-------------|
| `/committee [topic]` | Runs a 5-character adversarial committee deliberation | Complex decisions, competing values, "what are we missing?" problems |
| `/review` | Independent evaluation of a committee transcript against five rubrics | After any `/committee` run, or on a pasted transcript — completes the feedback loop |
| `/string-diagram` | Converts resource equations to Mermaid diagrams | Visualizing pipelines, formalizing workflows, editing equation sets |
| `/handoff` | Generates a session handoff for successor agents | End of work sessions, before breaks, after major milestones |

These skills are the methodology made executable: `/committee` operationalizes the adversarial committee technique, `/review` operationalizes independent evaluation, `/string-diagram` operationalizes the palgebra formalism, and `/handoff` maintains continuity across agent sessions.

## Core insights

1. **LLMs are storytelling machines.** Everything they produce - mathematical proofs, legal analysis, code, decision trees - are narrative constructs, not mechanistic solutions.

2. **Observation changes state.** Every AI response is a control signal that modifies your cognitive state. You cannot ask a question without being changed by the answer.

3. **Gaps produce bridges that change situations.** The act of articulating a problem transforms the problem. Sense-making isn't discovery - it's production.

4. **Repetition produces difference.** Asking "the same" question multiple times isn't failure - it's exploration of latent space, mapping the territory of possible interpretations.

5. **The analyst is an editor.** Your role isn't truth-seeker but curator of which stories get "published to reality."

## Why "Cyber-Sense"?

LLMs produce what we might call "cybersense" - narratives that emerge from cybernetic feedback between human queries and machine-generated responses. 

This can go two ways:

**Undisciplined cybersense**: High-entropy narratives that sound locally plausible but collapse to statistical likelihood. The "stochastic parrots" problem.

**Disciplined cybersense**: Rigorous methodology that treats narrative generation as a controllable process, using techniques like adversarial committees and forcing functions to prevent premature collapse.

This repository documents the latter.

## Status

This is early-stage documentation of an emerging methodology. The techniques described here have been refined through iterative practice and have reached stable behavioral equilibrium. The theoretical framework is being formalized.

**Evidence base**: The adversarial committee technique has empirical support from research on multi-agent reasoning — see [Societies of Thought](essays/societies-of-thought-synthesis.md) for a synthesis of findings from Google, UChicago, and the Santa Fe Institute showing that perspective-switching and conversational scaffolding improve reasoning quality. The theoretical foundations draw on established work in sense-making methodology (Dervin), second-order cybernetics (von Foerster, Bateson), and process philosophy (Deleuze). What remains to be validated is the specific combination of techniques and their calibration across problem domains.

Feedback, questions, and contributions welcome.

## License

CC BY-SA 4.0 for essays, MIT for code artifacts

---

*"In complex systems, mechanism fails to comprehend the full picture, but stories can capture enough relevant structure to be useful."*
