# Narrative Computing as Historical Progression

## The Paradigm Claim

Each generation of computing hardware has forced humans to adapt how we think about expressing and solving problems. This isn't a metaphor—it's a pattern with specific historical instances.

When we got fast arithmetic machines in the 1940s, we had to learn numerical analysis, error propagation, and stability theory. We called this era **numeric computing**, and it produced disciplines like computational physics and operations research.

When we got symbol manipulation machines in the 1970s, we had to learn formal logic, type theory, and algorithm complexity. We called this era **symbolic computing**, and it produced disciplines like software engineering and knowledge representation.

Now we have machines that generate coherent narrative on demand. This essay argues that **narrative computing** represents a comparable paradigm shift—not an incremental improvement to symbolic computing, but a categorical change requiring new methodology.

This is a strong claim. To defend it, we'll trace three intellectual threads that converge on the present moment: the cognitive science of narrative thought, the computational narrative intelligence research tradition, and systems-theoretic critiques of mechanism. Each thread contributes something essential. Together, they explain why Cyberneutics methodology isn't arbitrary—it's grounded in established science while addressing a genuinely new problem.

---

## The Cognitive Thread: Narrative as Mode of Thought

### Bruner's Two Modes

In 1986, cognitive psychologist Jerome Bruner proposed something that seemed almost heretical to the dominant information-processing paradigm: there are two irreducible modes of human thought, and neither can be reduced to the other.

He called them the **paradigmatic mode** (or logico-scientific) and the **narrative mode**. The paradigmatic mode seeks truth through formal analysis, logical proof, and empirical verification. It deals in categories, abstractions, and context-independent propositions. Its imaginative application produces good theory and tight analysis.

The narrative mode operates differently. It deals with human intentions and their vicissitudes—what happens when plans meet reality, when expectations collide with events. Its imaginative application produces good stories, believable accounts, and gripping drama. It concerns itself not with truth conditions but with **lifelikeness**—whether a story rings true to human experience.

Crucially, Bruner argued these modes are complementary but irreducible:

> "Efforts to reduce one mode to the other or to ignore one at the expense of the other inevitably fail to capture the rich diversity of thought."

This wasn't postmodern relativism. Bruner was making a precise cognitive claim: humans have two distinct systems for organizing experience, and both are necessary for navigating the world.

The implications for AI collaboration are profound. If narrative is an irreducible cognitive mode—not a primitive version of logic but a different function entirely—then treating LLMs as "reasoning engines" that happen to output text is a category error. They're **narrative engines**. The text they produce follows narrative logic (coherence, plausibility, dramatic structure) rather than formal logic (validity, soundness, proof).

### Narrative Cognition Research

Bruner's insight sparked decades of research confirming that narrative isn't just how we communicate—it's how we think.

Lee Roy Beach's Theory of Narrative Thought (2010) went further, arguing that narrative is the **primary** mode of human cognition. We maintain what he called a "prime narrative"—an ongoing chronicle of our experience organized by time and causation. This prime narrative is the bedrock of intuitive reasoning, the source of private thought, and the basis for communication.

When we encounter new situations, we don't first analyze them logically and then translate to narrative for communication. We understand them *as* narrative from the start—characters with intentions, events with causes, outcomes that follow (or violate) expectations.

Empirical research supports this. Pennington and Hastie's studies of jury decision-making (1986, 1992) demonstrated that jurors construct narrative representations of evidence, not logical matrices. They organize testimony into stories, and the story that best accounts for the evidence wins. This isn't a bug in human reasoning—it's how complex judgment under uncertainty actually works.

The connection to Cyberneutics methodology is direct: if humans naturally think through narrative, then framing AI collaboration as narrative generation and evaluation isn't artificial. It's working *with* human cognition rather than against it. Adversarial storytelling works because it leverages how humans actually process complex situations.

### From Cognition to Implementation: Kahneman and the Neural Substrate

Bruner's two modes find their implementation in both human neuroscience and machine architecture. Daniel Kahneman's *Thinking, Fast and Slow* (2011) gives us another lens on the same dichotomy: System 1 (fast, automatic, associative) and System 2 (slow, deliberate, logical).

System 1 corresponds to Bruner's narrative mode. It operates through pattern recognition and completion, finding coherence through association rather than analysis. When you see dark clouds and feel rain is coming, or read a face and know someone is angry, or encounter a familiar situation and intuitively grasp what's happening—that's System 1. It's fast because it runs on pattern-matching: your brain recognizes the configuration and retrieves the most likely completion.

System 2 corresponds to Bruner's paradigmatic mode. When you work through a multi-step proof, analyze competing explanations, or force yourself to check assumptions you'd normally accept, you're engaging System 2. It's slow because it requires sustained attention, explicit reasoning steps, and conscious effort.

At the neural level, the distinction maps onto computational architecture. System 1 is essentially a single forward pass through trained weights—millions of neurons firing in parallel, each performing a small computation (fundamentally linear algebra), and the aggregate producing pattern recognition at scale. This is what neocortical columns do: they're miniature pattern matchers, "piles of linear algebra" that recognize features and feed results forward. System 1 is one sweep through this machinery.

System 2 is more expensive: it's iterative loops routing System 1 outputs through additional checking, comparison, and state-holding. You run System 1, examine the result, run it again with adjusted context, compare outputs, maintain working memory of what you've checked. This requires sustained recurrent activity across multiple brain regions—prefrontal cortex orchestrating, working memory holding intermediate states, attention mechanisms selecting what to process next. It's "piles of piles" doing logical reasoning at greater metabolic cost.

The parallel to LLMs is striking and consequential. Large language models natively operate in System 1. Base inference is a single forward pass through transformer layers—pattern completion at enormous scale. The model sees a prompt and generates the most likely continuation according to its training. This is fast, cheap, and associative. It follows narrative logic: what typically comes next, what sounds right, what completes the pattern coherently.

Chain-of-thought prompting, adversarial committees, and the structured deliberation protocols in Cyberneutics methodology all induce System 2 behavior in a System 1 substrate. You're forcing the model through multiple passes, maintaining state across iterations, comparing perspectives, checking claims against each other. The individual model responses are still System 1 (pattern completion), but the orchestration creates System 2 reasoning through composition.

This helps explain why methodology matters so much. Without structured iteration, LLMs default to System 1: plausible-sounding pattern completion that gravitates toward statistical likelihood. The first coherent story wins. But real reasoning—the kind that catches errors, surfaces assumptions, weighs trade-offs, and resists premature closure—requires System 2. Since LLMs don't do this natively, we must induce it through architecture: adversarial prompting forces multiple perspectives, Robert's Rules forces checking, independent evaluation forces comparison.

The *Societies of Thought* research (discussed in our synthesis essay) reveals something remarkable: when reasoning models are trained with reinforcement learning, they learn to do internally what Cyberneutics does externally. They develop internal dialog, simulate multiple agents, and engage in debate with themselves. In effect, they're learning to implement System 2 reasoning through iterated System 1 calls. The methodology we designed as external scaffolding turns out to mirror what optimized reasoning architectures discover through training.

This also illuminates the 60-year debate in AI between symbolic and connectionist approaches. The symbolic AI tradition (GOFAI, production rules, logic engines) was essentially trying to build System 2 / paradigmatic reasoning directly: represent knowledge explicitly, manipulate symbols according to logical rules, chain inference steps mechanically. The connectionist tradition (neural networks, parallel distributed processing, deep learning) built System 1 / narrative reasoning: learn patterns from data, complete configurations through association, generate outputs that cohere with training distribution.

Each camp insisted its approach represented "real" intelligence. Both were right and both were incomplete. Bruner's insight applies: these are irreducible modes, and both are necessary. Modern AI breaks the impasse not by choosing one, but by composing them: System 1 (pattern completion) as the computational primitive, System 2 (logical checking) as the orchestrated loop. Neural networks provide the fast associative substrate; methodology provides the slow deliberate structure.

### Bruner's Dichotomy as Sense-Making Tool

There's something worth noting explicitly about how this framework functions. Bruner's paradigmatic/narrative dichotomy isn't just a classification scheme—it's a tool for thought that transforms how we see existing materials. Once you have this lens, pieces that seemed disconnected suddenly slot together and illuminate each other stereoscopically.

Cyberneutics methodology (cybernetics, control theory, formal evaluation protocols) follows paradigmatic logic. Boland's Narrative Engineering (continental philosophy, Gödel as parable, diegetic frames) follows narrative logic. The convergence between them isn't coincidence—it's two irreducible cognitive modes, applied to the same domain, necessarily arriving at compatible structural features. This explains why the essay collection itself uses both modes: dialog scenes are narrative, information theory essay is paradigmatic. Both are needed because both capture aspects the other can't.

This is itself an instance of Dervin's sense-making in action: we had a situation (collection of essays and techniques), encountered a gap (how do these relate at a deeper level?), and built a bridge (Bruner's framework). The result isn't just classification—it's transformed understanding. The paradigmatic/narrative split now organizes relationships throughout the material: System 1/System 2, symbolic/connectionist AI, explainability demands versus discourse-based observation, first-order versus second-order cybernetics. The framework makes the topology of ideas visible.

---

## The Computational Thread: Making Machines Tell Stories

### Early Story Generation

The dream of computational storytelling predates modern AI—Ada Lovelace asked whether Babbage's Analytical Engine could be creative in 1843. Story generation systems emerged by the 1960s, with systems like TALESPIN (Meehan, 1977) generating original Aesop-style fables by simulating characters with goals, plans, and beliefs.

These early systems revealed something important: **narrative coherence isn't just logical coherence**. TALESPIN could produce stories that were technically consistent but narratively unsatisfying—characters pursuing goals through logically valid but absurd chains of action. The systems could generate plot structures but couldn't evaluate whether those structures made good stories.

### Computational Narrative Intelligence

By the 1990s and 2000s, researchers like Riedl had begun developing more sophisticated approaches under the banner of **computational narrative intelligence**—defined as "the ability to craft, tell, understand, and respond affectively to stories."

This work produced impressive results within constrained domains. Planning-based systems could generate stories that satisfied author-specified constraints. Interactive narrative systems could adapt stories in real-time based on user actions. Training simulations used computational storytelling to create engaging educational experiences.

But there was a persistent limitation: these systems required explicit knowledge engineering. Every character's possible actions, every object's properties, every causal relationship had to be hand-specified. You could build a compelling interactive story in a well-defined microworld (a game, a training simulation), but you couldn't generate narrative about arbitrary real-world situations.

The systems could make machines tell stories. But they couldn't make machines that understood stories the way humans do—flexibly, contextually, with vast background knowledge brought to bear automatically.

### The Pre-LLM Gap

This was the state of computational narrative intelligence before large language models: sophisticated techniques that worked brilliantly within constrained domains but couldn't scale to open-world complexity.

The gap wasn't just technical. It was also conceptual. Computational narrative research focused primarily on **machines generating stories for humans to consume**—entertainment, education, training. The question of **humans using narrative machines as thinking partners** received less attention. There was no pressing need for methodology around human-AI narrative collaboration because the AI couldn't hold up its end of the collaboration.

What changed with LLMs wasn't just capability—it was the **kind** of capability. For the first time, we had systems that could generate coherent narrative about virtually any topic, drawing on vast implicit knowledge, producing outputs that follow genre conventions and maintain internal consistency across extended passages.

This created a new problem: the outputs *sound* authoritative but aren't grounded in truth. The narrative coherence that makes LLM outputs readable is exactly what makes them dangerous. A confident-sounding story can be completely wrong.

We needed methodology for working with powerful narrative engines. Computational narrative intelligence had given us theory and techniques for building such engines. What we lacked was theory and techniques for **collaborating** with them.

---

## The Systems-Theoretic Thread: Why Mechanism Fails

### Rosen's Challenge to Reductionism

While cognitive scientists studied narrative thought and AI researchers built story generators, theoretical biologist Robert Rosen was developing a rigorous argument for why certain systems—living systems especially—cannot be understood through reductionist analysis.

In *Life Itself* (1991), Rosen argued that the Cartesian-Newtonian paradigm, which treats organisms as complicated machines, is fundamentally inadequate. The problem isn't that organisms are very complex machines. It's that they're not machines at all, in the precise sense that matters.

A machine, in Rosen's framework, can be fully characterized by listing its parts and their interactions. Given complete knowledge of components and initial conditions, the machine's behavior follows deterministically. This is what makes machines simulable—you can build a model that captures everything relevant.

Living systems have a different property: **organization** that cannot be reduced to component interactions. The whole is not merely greater than the sum of parts—the whole has causal efficacy that isn't localizable in any subset of parts. Rosen called this **complexity** (in a technical sense distinct from mere complication) and demonstrated it rigorously using category theory.

The key insight for our purposes: **complex systems require semantic description**. You can describe a machine purely syntactically—rules for symbol manipulation, algorithms for state transitions. But you cannot capture a living system, or any truly complex system, without semantics—meaning, function, purpose.

### Organization vs. Mechanism

Rosen's work on anticipatory systems extended this analysis. Living organisms, he argued, contain models of their environment that allow them to anticipate future states and act accordingly. This anticipatory capacity isn't reducible to stimulus-response; it involves internal representations that carry meaning about the external world.

This has direct implications for understanding LLMs. Large language models are, at one level, pure syntax manipulation—statistical patterns over token sequences, no grounding in external reality. They produce outputs that are **syntactically** coherent (well-formed sentences, consistent style, genre-appropriate structure) but have no intrinsic **semantic** grounding (no verification against reality, no understanding of truth conditions, no causal connection to the world).

When we ask an LLM for analysis or advice, we get narrative that follows the conventions of good analysis or advice. The syntax is right. But semantic validity—whether the analysis actually applies to our situation—requires something the model cannot provide: judgment that connects symbols to reality.

This is why methodology matters. The model produces syntactically coherent narrative. Humans must supply semantic grounding through evaluation, verification, and judgment. Cyberneutics methodology structures this division of labor: AI generates candidate narratives, humans evaluate which narratives merit belief and action.

### Second-Order Cybernetics

The cybernetic tradition adds another crucial insight: the observer is part of the system being observed.

Heinz von Foerster and the second-order cyberneticians emphasized that any observation changes the system observed. There's no view from nowhere. When you examine a system, you become entangled with it.

Applied to LLM interaction: when you prompt a model, you're not querying a static knowledge base. You're initiating a dynamic process where your framing, context, and even your presence in the conversation shape the output. The model that generated a response will find that response convincing—it was, after all, constructed to be convincing.

This explains why **independent evaluation** is essential. The generator instance and evaluator instance must be separate precisely because the hermeneutic circle is real. You cannot evaluate your own outputs without bias. The evaluator must come to the artifact fresh, without investment in its coherence, able to see only what's actually on the page.

---

## The Synthesis: What's Actually Novel

### The Convergence Point

Around 2022, these threads converged in a way that created new demands.

LLMs reached sufficient capability to generate coherent narrative across virtually any domain. Suddenly, the abstract possibility of "narrative engines" became practical reality. Anyone could generate plausible-sounding analysis, advice, arguments, and explanations on any topic.

This created urgent need for methodology that hadn't existed before. Bruner told us narrative is an irreducible cognitive mode, but he wasn't thinking about AI collaboration. Riedl and the computational narrative researchers gave us techniques for building story generators, but not for partnering with them on complex problems. Rosen explained why semantic grounding can't emerge from syntax alone, but he wasn't addressing the practical question of how humans should work with syntactic narrative generators.

The application domain was new. As the characters in the synthesis essay observe: "We've never had narrative engines powerful enough to make this methodology necessary before."

### What Cyberneutics Contributes

The novelty of Cyberneutics methodology isn't in its components:

- Adversarial process comes from legal tradition, peer review, red teams
- Explicit reasoning chains come from mathematical proof and philosophical argument
- Evidence standards come from empirical science and journalism
- Procedural constraints come from parliamentary tradition
- Independent evaluation comes from separation of concerns in software and double-blind review in science

What's novel is the **synthesis and application**: adapting these existing practices into a coherent methodology for human-AI narrative collaboration.

The methodology treats AI as what it actually is—a narrative engine—and designs interaction patterns appropriate to that reality. It doesn't pretend LLMs are reasoning systems that happen to output text. It takes seriously that narrative generation and truth-seeking are different processes, and builds in the adversarial structures, evaluation protocols, and human judgment that bridge the gap.

The theoretical synthesis is also novel: combining Dervin's sense-making (gaps produce bridges that change situations), second-order cybernetics (observation changes state), and Deleuzian philosophy of difference (repetition produces novelty) into what we might call **cybernetic hermeneutics**—using cybernetic principles to design interpretive protocols for AI interaction.

### Why "Narrative Computing" as Term

The terminology matters. "AI assistant" sets wrong expectations—it implies the system understands your intent, has access to truth, and acts in your interest. "Chatbot" trivializes what these systems can do. "Generative AI" is too broad—it covers image generation, code synthesis, and much else.

"Narrative computing" names what's distinctive: **the machine generates narrative**, and this shapes everything about how we must use it.

Just as "numeric computing" emphasized that you had to frame problems numerically to use arithmetic machines, and "symbolic computing" emphasized that you had to frame problems formally to use logic machines, "narrative computing" emphasizes that you must frame problems as stories to use storytelling machines.

This isn't limitation—it's recognition. Each paradigm expanded the class of problems computers could help with. Narrative computing extends to the messy, contextual, intention-laden problems that resisted both numeric and symbolic approaches.

But just as numeric computing required numerical analysis and symbolic computing required software engineering, narrative computing requires its own engineering discipline. **Narrative engineering** is that discipline: composing unreliable narrative primitives (individual LLM calls) into reliable systems through redundancy, feedback, iteration, and staged composition. The relationship between narrative computing and narrative engineering parallels the relationship between symbolic computing and software engineering — the former names what the machine does, the latter names how we compose those operations into systems that work.

---

## Implications and Open Questions

### Methodological Maturation

Numeric computing took roughly 30 years to develop mature methodology—from ENIAC to widespread scientific computing with established practices for numerical analysis, error handling, and algorithm design.

Symbolic computing followed a similar arc—from LISP to enterprise software with established practices for software engineering, testing, and formal verification.

We're in the early days of narrative engineering — the discipline that grows from narrative computing, just as software engineering grew from symbolic computing. The methodologies aren't settled. Best practices are still emerging. Cyberneutics represents one contribution to this developing field, not the final word.

What will narrative engineering require? Adversarial deliberation, certainly. Evidence standards adapted for narrative claims. Assumption surfacing techniques. Institutional memory management. Perhaps entirely new practices we haven't yet imagined.

### Risks of Getting It Wrong

The stakes are significant. LLMs are being deployed at scale right now—for strategic decisions, medical triage, legal research, code generation, educational assessment, content moderation.

Most deployment treats LLMs as better versions of symbolic systems—faster search, smarter assistants, automated reasoning. This is the category error that Cyberneutics methodology addresses.

If we don't develop appropriate methodology, we get:
- Confident-sounding bullshit at scale
- Decisions based on plausible but wrong stories  
- Automation of bias dressed as objectivity
- Trust in systems that can't bear the weight

### The Optimistic Case

Here's what's possible if we get this right:

Narrative engines can generate and evaluate more candidate solutions than humans could explore alone. They can surface perspectives we wouldn't naturally consider. They can make implicit assumptions explicit and force trade-offs into the open. They can maintain institutional memory that persists across conversations and contexts.

Not because AI is magic. Because we've developed methodologies appropriate to the tool.

The disciplines we use for high-stakes decisions—adversarial process, independent review, evidence standards—become accessible for everyday decisions. Rigorous sense-making at scale, with human judgment remaining central but amplified by narrative generation capacity.

---

## Conclusion

The three-eras framing—numeric, symbolic, narrative—is defensible, not hype. Each paradigm is defined by what the machine does (arithmetic, logic, story generation) and the engineering discipline humans develop to compose those primitives into reliable systems.

Narrative computing is the current paradigm. LLMs are narrative engines — the transistors of this era. Treating them as oracles or reasoning systems is a category error with practical consequences. Narrative engineering — composing unreliable narrative primitives into trustworthy systems through redundancy, feedback, and staged composition — is the discipline this era demands. Cyberneutics is one methodology within it.

The intellectual foundations are solid. Bruner established narrative as irreducible cognitive mode. Rosen demonstrated that complex systems require semantic description beyond syntactic manipulation. Computational narrative intelligence developed techniques for story generation and analysis. Second-order cybernetics explained why observer and observed are entangled.

What's new is the application domain and the synthesis. We have powerful narrative engines now. We need narrative engineering — the practical discipline for composing them into systems that catch their own errors and produce assessable artifacts. The components exist in other fields—adversarial process, evidence standards, procedural constraints, independent evaluation. The contribution is adapting these into coherent practice for human-AI narrative collaboration.

We're in the early days. The discipline will evolve. But the fundamental insight is clear: if the tool is a narrative engine, treating it like a calculator is a category error. You don't get mad at a car for not flying; you learn to drive.

For the philosophical path to these same conclusions—through Gödel, Kuhn, operational closures, and category theory (where Bruner's dichotomy reappears as the lens explaining why independent convergence was inevitable)—see [Narrative Engineering](./07-bolands-narrative-engineering.md).

---

## References

Bender, Emily M., Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021. "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?" *FAccT '21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, 610-623.

Beach, Lee Roy. 2010. *The Psychology of Narrative Thought: How the Stories We Tell Ourselves Shape Our Lives*. Xlibris.

Bruner, Jerome S. 1986. *Actual Minds, Possible Worlds*. Harvard University Press.

Dervin, Brenda. 1998. "Sense-Making Theory and Practice: An Overview of User Interests in Knowledge Seeking and Use." *Journal of Knowledge Management* 2(2): 36-46.

Kahneman, Daniel. 2011. *Thinking, Fast and Slow*. Farrar, Straus and Giroux.

Pennington, Nancy, and Reid Hastie. 1992. "Explaining the Evidence: Tests of the Story Model for Juror Decision Making." *Journal of Personality and Social Psychology* 62(2): 189-206.

Piper, Andrew, Richard Jean So, and David Bamman. 2021. "Narrative Theory for Computational Narrative Understanding." *Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing*, 298-311.

Riedl, Mark O. 2016. "Computational Narrative Intelligence: A Human-Centered Goal for Artificial Intelligence." arXiv:1602.06484.

Rosen, Robert. 1991. *Life Itself: A Comprehensive Inquiry into the Nature, Origin, and Fabrication of Life*. Columbia University Press.

Shanahan, Murray. 2024. "Talking About Large Language Models." arXiv:2212.03551.

von Foerster, Heinz. 2003. *Understanding Understanding: Essays on Cybernetics and Cognition*. Springer.

---

**Related essays**:
- [Why Narrative Engines Change Everything](./01-why-narrative-engines-change-everything.md) — the concise version of this historical argument
- [Narrative Engineering](./07-bolands-narrative-engineering.md) — Boland's independent convergence on similar conclusions

**Related artifacts**:
- [Integration with MOOLLM](../artifacts/integration-with-moollm.md) — how Cyberneutics maps onto an infrastructure designed for narrative computing
