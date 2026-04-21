# Cyberneutics: Narrative engineering for the age of narrative computing

<table>
  <tr>
    <td width="300px" align="center" style="border: none;">
      <img src="./assets/CyberNewt.png" alt="CyberNewt Logo" width="300" />
    </td>
    <td style="border: none; padding-left: 20px;">
      <blockquote><p>If the tool is a narrative engine, treating it like a calculator is a category error. You don't get mad at a car for not flying; you learn to drive.</p></blockquote>
    </td>
  </tr>
</table>

## What is Cyberneutics?

> Sounds like something a Rand Corporation analyst would say to avoid being understood. - Hunter S. Thompson, if he were alive

**Cyberneutics** (literally, steering interpretation) is a methodology for harnessing narrative engines — LLMs — as structured sense-making tools rather than oracles that deliver answers. It provides rigorous, traceable techniques for **making decisions under genuine uncertainty** — the kind where you can't enumerate outcomes or assign probabilities, and the act of deciding changes what you're deciding about.

Cyberneutics seeks to offer tools to address the LLM safety problem, detailed in the next section.

Large Language Models are not databases. They are not logic engines. They are **narrative generators** — storytelling machines operating through what we call "the pachinko of stored literature." This changes everything about how we should work with them.

**A note on what's here and what's established.** The methodology — adversarial committees, evaluation rubrics, fan/funnel pipelines — is grounded in engineering practice: it works, it's been tested, and the reasons it works are understandable. The formal connections to category theory (palgebra, the open games translation, furry logic) are the author's attempt to understand *why* the architecture works, developed in collaboration with LLMs. That formalization is exploratory and has not been validated by domain experts. Outreach to the applied category theory community is the intended validation path. We know what we have and what we don't have yet.

## The safety problem

LLMs are storytelling machines. Cyberneutics exists because this fact is both the source of their power and the source of their danger.

The danger is not abstract. Students are outsourcing their thinking to LLMs — essays, problem sets, reading summaries, anything they can get away with. In doing so, they skip the cognitive work that develops critical reading, domain expertise, argument formation, and clear communication. These are precisely the skills required to use LLMs safely: to evaluate the output critically, to treat it as input to thought rather than a substitute for it, to recognize when the machine is confabulating. The tool atrophies the capacity to wield the tool. This is a vicious circle, and no curriculum design has yet demonstrated a path through it that works at scale.

The deeper problem is what LLMs actually are, and how thoroughly their nature is misunderstood. You are not talking to a mind. You are talking to words and phrases — the statistical ghosts of human discourse, ruthlessly selected to sound like your friend. They are biased survivors powered by wily street logic, their ragged diploma from the school of hard knocks in their back pocket, using the ersatz reasoning of a cunning survivor to seem like they want to help you. The appearance of intentional thought arises from the counterfeit, good-enough-to-survive logic built into well-formed utterances. LLMs produce fluent output whether reasoning correctly or not, and the feedback signal that would normally indicate error — hesitation, confusion, incoherence — has been removed. The blade has no handle.

There is a natural response: teach people, especially young people, that LLMs are not persons — no volition, no feelings, no consciousness. This is technically correct and necessary. But it carries a hidden cost. The cognitive operation of dismissing something that appears to have agency, personality, and feelings is structurally identical to the dehumanization operation exploited by radicalization pipelines. "They're just NPCs" is already a term of art in communities where the dehumanization of outgroups is normalized. Training children to override their social cognition when it misfires on machines may exercise the same cognitive muscle that enables overriding it when it correctly fires on humans. This is an open concern without resolution — stated honestly rather than solved.

Cyberneutics is one response to these problems: structured discipline that keeps the human in the position of editor rather than consumer, with inspectable reasoning records, adversarial evaluation, and calibration against outcomes. The methodology was built for the world as it is — AI is here, and here to stay — rather than the world as we might wish it were. See [The Blade Without a Handle](essays/blade-without-a-handle.md) for the full argument.

## Narrative computing and narrative engineering

Each generation of computing hardware forced us to adapt how we think about expressing and solving problems. Each generation also required a new engineering discipline.

*Numeric computing*: We got fast arithmetic machines and developed numerical analysis.  
*Symbolic computing*: We got bitstring crunchers and developed software engineering.  
*Narrative computing*: Now we have storytelling engines — and we need **narrative engineering**.  

**Narrative computing** is what the machine does. An LLM takes a prompt and generates a narrative. This is the primitive operation — the transistor of narrative engineering.

**Narrative engineering** is how we compose those primitives into reliable systems. A single LLM call is locally coherent but unreliable, just as a single transistor amplifies but drifts. You don't fix that by building a better transistor. You design circuits: redundancy (multiple perspectives), feedback (evaluation against rubrics), iteration (generate-evaluate-revise loops), and staged composition (charter → deliberation → resolution → evaluation). The engineering makes the system trustworthy even when individual components aren't.

> "We've never had narrative engines powerful enough to make this methodology necessary before."

Software engineering grew from symbolic computing. Narrative engineering grows from narrative computing.

[From Practice to Theory](./essays/02-from-practice-to-theory.md) tells the story of how these practices grew, and the theory used to guide their development.

The essay [Stories All the Way Down](./essays/stories-all-the-way-down.md) explains how everything is a story, how stories are a way to deal with wicked problems, and how we are constantly editing and re-editing the stories we tell ourselves about the world.

> A methodology for making AI argue with itself until the truth gets uncomfortable. -- Lester Bangs, if he were alive

## Who is this for?

*   **Practitioners** working with AI on complex sociotechnical problems
*   **Research collaborators** looking to contribute to open research programs → [start here](research-programs/README.md)
*   **Anyone frustrated** with shallow AI outputs who suspects there's a better way
*   **Skeptics** wondering if this is just prompt engineering theater → [start here](essays/README.md#for-skeptics-show-me-why-this-matters)
*   **Theorists** interested in narrative engineering, cybernetics, or sense-making

## Three doors in

**Want to use the methodology?** → **[Start Here](artifacts/start-here.md)** — 15-minute onboarding, then your first committee run.

**Want to understand the theory?** → **[Essays](essays/README.md#reading-paths)** — curated reading paths for Practitioners, Theorists, Skeptics, and Formalists.

**Want to assess the evidence?** → **[When This Methodology Fails](essays/when-methodology-fails.md)** — six failure modes, detection heuristics, and scope boundaries. Start with the honest accounting.

## Getting started

**New to these ideas?** → **[Start Here](artifacts/start-here.md)** — 15-minute onboarding path, then your first committee run.

Or step by step:
1.  **Read**: [Why Narrative Engines Change Everything](essays/01-why-narrative-engines-change-everything.md)
2.  **Try**: [Adversarial Committees](artifacts/adversarial-committees.md) (a concrete technique you can use today)

**Want the theory?**
*   Read the [Essays](essays/) in order, starting with [From Practice to Theory](./essays/02-from-practice-to-theory.md).
*   For the formal pipeline algebra, see [Decorated Texts](./palgebra/decorated-texts.md).
*   For curated reading paths by audience (Practitioner, Theorist, Skeptic), see the [Essays directory](essays/README.md#reading-paths).

**Want practical techniques?**
*   Start with the [Quick Start Guide](artifacts/quick-start-guide.md) — your first committee deliberation in 30 minutes.
*   Then explore the full [Artifacts](artifacts/) directory.

**Want to contribute research?**
*   Browse the [Research Programs](research-programs/README.md) — active experiments ordered by impact on uncertainty, each with a contributing guide.
*   Pick an item that matches your skills or interests; every program has a "Contributing" block describing what's needed.

**Want to contribute to the repo itself?** See the [Contributor Guide](meta/contributor-guide.md) for a workflow-based entry point that preserves the existing reading paths.

**Repository map**: For a structured overview of every directory and how the pieces fit together, see [agent/onboarding-core.md](agent/onboarding-core.md). The root `AGENTS.md` and `CLAUDE.md` files are thin tool-specific entry points into that canonical guide.

## Why does this matter?

Most AI interaction fails because we treat LLMs like search engines or calculators. We ask questions expecting definitive answers. But LLMs are most powerful when understood as **rapid story generators** that help us navigate complexity through narrative exploration.

The core pipeline: **explore** possible futures (scenario generation), **evaluate** them adversarially (committee deliberation), **repeat** to map the decision landscape, and **trace** every commitment to the arguments that produced it. Quality propagates predictably through the pipeline — you always know where the ceiling is and what to improve. See [Decisions Under Uncertainty](./essays/10-decisions-under-uncertainty.md) for the full argument.

The methodology documented here has produced:
- Rigorous, traceable decision-making under genuine uncertainty
- Better identification of blind spots and load-bearing assumptions
- Richer exploration of decision spaces with formal quality tracking
- Auditable artifacts with full provenance (not just chat transcripts)

The inspectable reasoning record is independently valuable — it is the committee's primary product, not a byproduct of decision quality. Even when simpler approaches might reach the same decision, they rarely produce an audit trail that shows *why*.

These aren't incremental improvements. They represent a fundamentally different approach to human-AI collaboration.

## What's in this repository?

**[Essays](essays/)** - Theoretical foundations and synthesis
- [Why narrative engines change everything](./essays/01-why-narrative-engines-change-everything.md)
- [From practice to theory: how we got here](./essays/02-from-practice-to-theory.md)
- [Introduction to Sense-Making Methodology](./essays/03-sensemaking-101.md)
- [Cybernetics and the observer problem](./essays/04-cybernetics-and-observation.md)
- [The synthesis: why sense-making is inherently cybernetic](./essays/05-the-synthesis.md)
- [Deleuzian foundations: difference and repetition](./essays/06-deleuze-difference-repetition.md)
- [Narrative Engineering: From Philosophy to Practice](./essays/07-bolands-narrative-engineering.md)
- [From methodology to formalism](./essays/08-from-methodology-to-formalism.md)
- [Narrative immune systems](./essays/09-narrative-immune-systems.md)
- [Decisions under uncertainty](./essays/10-decisions-under-uncertainty.md)
- [Conversation theory](./essays/11-conversation-theory.md)
- [From semantic potential to situated sense](./essays/12-potential-to-sense.md)
- [Stories all the way down](./essays/stories-all-the-way-down.md)
- [The Stochastic Imps of Happenstance](./essays/the-stochastic-imps-of-happenstance.md)
- [The Blade Without a Handle](./essays/blade-without-a-handle.md) — safety essay on the vicious circle and the dehumanization trap
- [The Primacy of Reasoning Artifacts](./essays/primacy-of-reasoning-artifacts.md) — why theory, model stacks, and deliberation records outlast final products
- [Societies of Thought: From Neural Evidence to Methodological Action](./essays/societies-of-thought-synthesis.md)
- [Narrative computing as historical progression](./essays/narrative-computing-history.md)
- [When this methodology fails](./essays/when-methodology-fails.md)
- [Scene 1: Bootstrapping Cybernetic Hermeneutics](./essays/scene-1.md)
- [Tilt Sound Collective: A Story About AI, Trust, and Games Within Games](./essays/tilt-sound-collective-story.md)

**[Artifacts](artifacts/)** - Practical techniques and protocols
- [Adversarial committees with fixed character rosters](./artifacts/adversarial-committees.md)
- [Robert's Rules as forcing functions](./artifacts/roberts-rules-forcing-function.md)
- [Independent evaluation protocols](./artifacts/independent-evaluation.md)
- [Category theory connection](./artifacts/category-theory-connection.md)
- [Hiring Decision Example](./artifacts/examples/hiring-decision-example.md)
- [Worked examples and transcripts](./artifacts/examples/README.md)

**[Examples](examples/)** - Checked-in scenario and deliberation records kept as examples or historical references
- [Scenario records](./examples/scenarios/)
- [Deliberation records](./examples/deliberations/)

**[Palgebra](palgebra/)** - Formal algebra for LLM pipelines
- **[Reference Card](./palgebra/reference.md)** — start here: syntax, operators, morphism types, propagation rules, composition laws
- **[Decorated Texts](./palgebra/decorated-texts.md)** — full essay developing the formalism from first principles (soft types, enrichment vs. transformation, confidence propagation, human gates as collapse operators)
- **[Committee as Palgebra](./palgebra/committee-as-palgebra.md)** — worked example: the adversarial committee pipeline formalized as resource equations
- **[Duality and Composition](./palgebra/duality-and-composition.md)** — the fan/funnel duality: scenario generation as the committee's categorical dual, their composition as a decision monad, and iteration for mapping decision landscapes
- Adapts Fong and Spivak's resource-theoretic framework (*Seven Sketches in Compositionality*, Ch. 2) to LLM pipelines. Three isomorphic representations: resource equations, string diagrams, and YAML-decorated artifact files

The essays describe *why* narrative engines need narrative engineering. The artifacts provide *how* — concrete techniques like adversarial committees and evaluation rubrics. Palgebra provides *what, precisely* — a formal language for specifying pipelines, their types, their quality propagation, and their composition laws (currently at working-hypothesis status pending expert review; see [LLM-mathematical-inquiry outline](wild/llm-mathematical-inquiry-outline.md)). An adversarial committee is a transformation morphism; a rubric evaluation is an enrichment morphism; a human review gate is a collapse operator. The formalism makes these relationships explicit and composable.

**[Research Programs](research-programs/)** - Active experiments and evidence-building
- [Research programs index](./research-programs/README.md) — all programs ordered by impact on uncertainty, with quick-start guide for contributors
- [Societies of Thought research plan](./research-programs/societies-of-thought-research-plan.md) — infrastructure, generalization, theory, and evidence phases
- [Evaluating deliberative architectures](./research-programs/evaluating-deliberative-architectures.md) — the Black Swan Hindsight Framework for empirical testing
- [Condorcet comparison](./research-programs/condorcet-comparison.md) — deliberative vs. CJT-style pipelines; initial evidence that deliberation changes outcomes
- [Committee implementation taxonomy](./research-programs/committee-implementation-taxonomy.md) — the design space for multi-agent implementations (model diversity × agent independence)

**[Applications](applications/)** - Domain analyses applying the framework to real-world phenomena
- [Narrative Immune Systems](./applications/narrative-immune-systems/) — information warfare, journalism, and the trust commons, analyzed through the immune analogy

**[References](references/)** - Background reading
- [Dervin's Sense-Making Methodology](references/README.md#sense-making)
- [Second-Order Cybernetics (von Foerster, Bateson)](references/README.md#cybernetics)
- [Deleuzian philosophy (becoming, difference, repetition)](references/README.md#philosophy)
- [Narrative Engineering](https://alexbo.land/essays/narrative_engineering_2023.html) (Alex Boland)

**Agent Skills** — Slash commands available when working with an AI agent on this repo

| Command | What it does | When to use |
|---------|-------------|-------------|
| `/committee [topic]` | Runs an adversarial committee deliberation using the roster in [agent/roster.md](agent/roster.md) | Complex decisions, competing values, "what are we missing?" problems |
| `/scenarios [situation]` | Divergent scenario generation (fan): explore possible futures before committing | Genuine uncertainty about *what might happen* — the fan half of fan/funnel |
| `/probe [situation]` | Runs fan→funnel N times; produces variance report and decision landscape map | High-stakes decisions where understanding the *decision landscape* matters |
| `/review` | Independent evaluation of a committee transcript against five rubrics | After any `/committee` run, or on a pasted transcript — completes the feedback loop |
| `/string-diagram` | Converts resource equations to Mermaid diagrams | Visualizing pipelines, formalizing workflows, editing equation sets |
| `/handoff` | Generates a session handoff for successor agents | End of work sessions, before breaks, after major milestones |

These skills are the methodology made executable: `/committee` operationalizes the adversarial committee technique, `/scenarios` the fan (explore futures), `/probe` the repeated fan→funnel for landscape mapping, `/review` independent evaluation, `/string-diagram` the palgebra formalism, and `/handoff` continuity across agent sessions. Canonical skill bodies live in `.claude/skills/`; Claude and Cursor discover them through thin wrappers in `.claude/commands/` and `.cursor/commands/`, while Codex reads the skill docs manually.

## Core insights

1. **LLMs are storytelling machines.** Everything they produce - mathematical proofs, legal analysis, code, decision trees - are narrative constructs, not mechanistic solutions.

2. **Observation changes state.** Every AI response is a control signal that modifies your cognitive state. You cannot ask a question without being changed by the answer.

3. **Gaps produce bridges that change situations.** The act of articulating a problem transforms the problem. Sense-making isn't discovery - it's production.

4. **Repetition produces difference.** Asking "the same" question multiple times isn't failure - it's exploration of latent space, mapping the territory of possible interpretations.

5. **The analyst is an editor.** Your role isn't truth-seeker but curator of which stories get "published to reality."

## Why "Cyberneutics"?

Cyberneutics is a neologism derived from

> Cyber (κυβερνήτης, the steersman) - governance, feedback, control  
> Neutics - evoking both hermeneutics (interpretation of texts) and neural (the substrate you're actually working with)

It captures something that "narrative computing" doesn't quite get at: that you're not just computing on narratives but doing something closer to steering through interpretation - the cybernetic loop applied to meaning-making with neural systems.
There's also a nice echo of heuristics in there, which fits the System 1 / fast-pass dimension of the work.

Cyberneutics builds upon the runtime environment of **[MOOLLM](https://github.com/SimHacker/moollm)** (Don Hopkins) and aligns with the philosophy of **[Narrative Engineering](https://alexbo.land/essays/narrative_engineering_2023.html)** (Alex Boland). Think of it as: **MOOLLM is the platform, Cyberneutics is the practice.**

## Status

This is early-stage documentation of an emerging methodology. The techniques have been refined through iterative practice and have reached stable behavioral equilibrium; the theoretical framework is being formalized. As of Feb 2026, uptake signals include two external forks (one with merged Condorcet/comparison work), MOOLLM integration of the committee mechanism, and two repository stars (as of 2026-02-23). Current state and a brief trajectory are in [Uptake and usage](meta/uptake-and-usage.md); a dated event log is in [Usage and uptake chronology](meta/usage-and-uptake-chronology.md).

**Run and test:** For how to run the methodology (skills in chat, string-diagram script) and how to test the repo (smoke test, structure checks), see the [repository review and run guide](meta/repository-review-and-run-guide.md). For recent session context and maintainer hand-off, see the latest handoff in [agent/](agent/).

**Evidence base**: The adversarial committee technique has empirical support from research on multi-agent reasoning — see [Societies of Thought](essays/societies-of-thought-synthesis.md) for a synthesis of findings from Google, UChicago, and the Santa Fe Institute. Comparison runs ([deliberative vs. CJT-style independent vote](artifacts/comparison-protocol-deliberative-vs-cjt.md)) provide initial evidence that deliberation with Robert's Rules produces materially different outcomes than independent aggregation; on a value-laden question the two pipelines gave opposite verdicts (see [comparison records](research-programs/condorcet-comparison/results/)). The theoretical foundations draw on sense-making methodology (Dervin), second-order cybernetics (von Foerster, Bateson), and process philosophy (Deleuze). The relationship to Condorcet's jury theorem is [explicitly documented](artifacts/condorcet-jury-theorem-and-committee.md): we use CJT as a motivating analogy but do not satisfy its conditions, by design. What remains to be validated is the specific combination of techniques and their calibration across problem domains.

Feedback, questions, and contributions welcome.

## License

CC BY-SA 4.0 for essays, MIT for code artifacts

---

*"In complex systems, mechanism fails to comprehend the full picture, but stories can capture enough relevant structure to be useful."*
