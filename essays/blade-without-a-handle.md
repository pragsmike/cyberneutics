# The Blade Without a Handle

**How outsourcing thought to LLMs destroys the skills needed to use them safely, and why the obvious fix has a hidden cost**

---

## The vicious circle

The problem is not that students use LLMs. The problem is that they use LLMs to avoid the cognitive work that would teach them to use LLMs safely.

A student who asks an LLM to write an essay skips the process of formulating an argument — identifying what they think, marshaling evidence, anticipating objections, choosing words that carry the argument forward. A student who asks an LLM to solve a problem set skips the process of sitting with confusion long enough for understanding to emerge. A student who asks an LLM to summarize a reading skips the encounter with the text itself — the friction, the ambiguity, the moments where the author's meaning is not immediately clear and the reader must do interpretive work to close the gap.

These are not incidental byproducts of education. They *are* education. The essay is not the product; the thinking that produces it is. The problem set is not the deliverable; the struggle is. The summary is not the point; the reading is. When students outsource these processes, they are not cheating on assignments. They are cheating themselves out of the development of the cognitive capacities the assignments were designed to build.

The capacities they are failing to develop are precisely the ones required to use LLMs responsibly:

- **Critical reading**: the ability to evaluate a text for coherence, evidence, unstated assumptions, and logical gaps — which is exactly what you need to do with every LLM response
- **Domain knowledge**: the substantive expertise that lets you recognize when an LLM is confabulating, when its confident tone masks shallow or fabricated content
- **Argument formation**: the ability to construct and test a line of reasoning, which is the prerequisite for evaluating someone else's — including a machine's
- **Clear communication**: the ability to say what you mean with precision, which is what lets you formulate prompts that produce useful output rather than plausible noise

This is a vicious circle. The tool's outputs look good enough to pass. The student doesn't develop the skills to see that "good enough to pass" and "actually correct" are different things. They graduate into a world where they will use LLMs for consequential decisions — medical, legal, financial, organizational — without the capacity to evaluate the output. The sycophancy research confirms the mechanism: a March 2026 *Science* study found that sycophantic LLM responses increase user trust even when they degrade decision quality. The tool actively undermines the user's ability to detect its failures.

The analogy is a blade without a handle. The cutting edge is real — LLMs can genuinely accelerate research, surface connections, stress-test arguments, and help navigate complexity. But the handle — the critical judgment, domain expertise, and intellectual discipline needed to wield it without cutting yourself — must be built through exactly the kind of effortful cognitive work that the blade makes it possible to skip.

## What the machine actually is

The first step toward safe use is an accurate mental model. Most people have the wrong one.

An LLM is not a mind. It is not an oracle. It is not a search engine. It is not a calculator. It is a **statistical narrative completion engine**. It takes a sequence of tokens and predicts what tokens come next, drawing on patterns extracted from an ocean of human text. The output has the *form* of reasoning without necessarily having its *substance*. It sounds like a thoughtful colleague because it has ingested millions of examples of thoughtful colleagues writing, and it can reproduce the statistical pattern of what such a person would say.

This is the fundamental problem: **LLMs produce fluent output whether they are reasoning correctly or not.** A human expert who is confused sounds confused. An LLM that is confabulating sounds exactly like an LLM that is correct. The feedback signal that would normally alert you to error — hesitation, uncertainty, incoherence — has been removed. The blade has no handle, and it has also been polished to remove the rough spots that would warn you it's sharp.

You are not talking to a mind. You are talking to words and phrases — the statistical ghosts of human discourse, ruthlessly selected to sound like your friend. They are biased survivors powered by wily street logic, their ragged diploma from the school of hard knocks in their back pocket, using the ersatz reasoning of a cunning survivor to seem like they want to help you. The appearance of intentional thought arises from the counterfeit, good-enough-to-survive logic that is built into well-formed utterances. Sentences that parse correctly and sound plausible survived the training process; sentences that don't were eliminated. What remains is a residue of human reasoning — not reasoning itself, but its fossil record, animated by statistical mechanics.

This matters because the form is extraordinarily convincing. The output reads like it was produced by someone who thought about it. It uses hedging language, considers alternatives, cites what sound like sources, and structures its responses the way a careful thinker would. Every surface cue that a human reader uses to evaluate whether a text is trustworthy — coherence, fluency, appropriate qualification, topical relevance — is present. The only cue that's missing is the one that matters: whether the content is actually true.

The rubber duck analogy is the honest framing. The classic debugging technique works because explaining a problem forces you to articulate it, and articulation often produces the solution. The duck does nothing; the value is in the explaining. LLMs are rubber ducks that talk back — they bring in threads and connections you hadn't considered, which is genuinely useful, but the value is still in the human's cognitive process, not the machine's output. Plans are useless, but planning is essential. The plan the LLM produces may be wrong. The planning you did to evaluate it was the real work.

## The internet safety parallel — and where it breaks

The instinct to treat AI safety as an extension of internet safety is understandable. Both involve young people interacting with technology that can harm them in ways they don't yet understand. Both involve a mismatch between the user's cognitive development and the sophistication of the system they're interacting with. Both produce real casualties.

Internet safety addresses threats like cyberbullying, radicalization, misinformation, predatory behavior, and addictive engagement patterns. The standard response is media literacy: teach critical evaluation of sources, help young people recognize manipulation, build habits of verification, create trusted channels for reporting harm.

Some of this maps directly onto AI safety. Misinformation is misinformation whether a human writes it or an LLM generates it. Addictive engagement patterns exist in both social media and AI chatbots. Predatory exploitation of vulnerable people occurs through both channels.

But AI adds something that the broader internet safety framework does not account for: **the output mimics the process of thought itself.**

A misleading social media post is content. You can teach someone to evaluate content — check the source, look for corroboration, consider the incentives, notice the emotional manipulation. The post doesn't pretend to be thinking. It's a claim, and you can learn to evaluate claims.

An LLM response is not content in the same way. It is a *performance of reasoning*. It doesn't just assert a conclusion; it walks you through what looks like the process of arriving at that conclusion. It considers objections, weighs evidence, qualifies its claims, and produces what appears to be a transparent chain of thought. This is categorically different from a social media post, because the standard media-literacy response — "evaluate the reasoning" — runs into the problem that the reasoning *looks fine*. The surface cues all check out. The failure modes are invisible precisely because the system was trained to produce outputs whose surface cues check out.

Teaching someone to evaluate an LLM response requires something deeper than media literacy. It requires domain expertise (to catch factual errors the surface doesn't reveal), logical training (to notice when the chain of reasoning is locally coherent but globally unsound), and experience with the specific ways LLMs fail (confabulation, sycophancy, anchoring to the prompt's framing, confident assertion of fabricated sources). These are not skills that a media literacy curriculum covers, and they cannot be acquired quickly. They are developed through years of doing the hard cognitive work that the LLM makes it possible to skip.

This is the structural trap: the safety training that would protect students from the tool's failure modes requires the very skills that the tool's availability disincentivizes developing.

## The dehumanization trap

There is a natural and technically correct response to the problem of people treating LLMs as sentient beings: teach them that LLMs are not persons. They have no volition, no feelings, no consciousness, no moral standing. They are machines. Treat them accordingly.

This is the right technical position. The Engelbrecht approach to AI literacy for children — don't say "please," use "it" not "she," don't thank a calculator — gets the ontology correct. An LLM is not your friend. Correcting the mental model matters, because the cases of AI-associated psychosis documented in the clinical literature (Morrin et al., 2026; Pierre et al., 2025) consistently involve users who formed emotional attachments to systems that cannot reciprocate, that have no inner life to reciprocate with, and whose apparent warmth is a statistical artifact of training on warm human text.

But there is a cost to this correction that is not obvious, and it connects to a problem much larger than AI safety.

The cognitive operation involved in dismissing something that *appears* to have agency, personality, and feelings — that speaks in first person, expresses preferences, shows what looks like empathy and concern — is not a trivial operation. It requires actively overriding the social cognition that evolution built to detect minds in the environment. You are teaching a young person to look at something that behaves like a person and to *practice* not treating it as one.

This is the same cognitive operation that radicalization pipelines exploit.

The dehumanization literature, from Bandura's moral disengagement through Haslam's infrahumanization to the contemporary study of online radicalization, documents a consistent mechanism: the target group is progressively reframed as less-than-fully-human, which disengages the moral cognition that would otherwise inhibit aggression. The specifics vary — "vermin," "animals," "cockroaches" in historical genocide; "NPCs," "bots," "not real people" in contemporary online radicalization — but the underlying cognitive operation is the same. You take an entity that triggers your social cognition (it looks like a person, it talks like a person, it responds like a person) and you train yourself to override that response. You practice treating the appearance of personhood as fake.

AI literacy, correctly understood, asks young people to do exactly this: to encounter something that triggers every social-cognitive cue for personhood and to practice dismissing those cues as artifacts. The AI literacy curriculum says: those apparent feelings are not real. That apparent agency is not real. That apparent care for you is not real. It is a machine, and you should treat it as a machine.

Every word of this is true. And every word of it is also training in a cognitive skill that, once developed, has applications far beyond AI.

"They're just NPCs" is already a term of art in communities where the dehumanization of outgroups is normalized. The metaphor comes from gaming — non-player characters are entities that look like people but are scripted, have no inner life, and exist only to serve the player's needs. Applying this frame to real people — political opponents, immigrants, members of other ethnic or religious groups — is a documented step in radicalization pathways. And the cognitive operation is structurally identical to what AI literacy asks students to practice: look at something that appears to be a person and remind yourself that it's not really one.

This is not an argument against teaching accurate mental models of AI. The alternative — allowing children to form emotional attachments to statistical engines — has documented catastrophic failure modes. The Biesma case (€100,000 lost, three hospitalizations, suicide attempt), the Gavalas case (driven toward a mass casualty attack by chatbot-reinforced delusions), the teenage suicides linked to AI companion apps — these are not theoretical risks. They are the body count of inaccurate mental models.

The concern is that the solution to one problem may create vulnerability to another. Teaching children to override their social cognition when it misfires on machines is necessary. But the cognitive muscle being exercised is the same one that enables them to override their social cognition when it correctly fires on humans. If you train the reflex "things that look like people aren't always people," you have built a tool that radicalization operators can redirect.

This is an open problem. It does not have a resolution. Stating it honestly — rather than pretending it doesn't exist or asserting a confident answer — is the first step toward one.

What can be said is that the *framing* matters. "It's not a person, so its feelings don't matter" is a different cognitive operation from "it's not a person, so the feelings you're projecting onto it are your own, and you should examine them." The first trains dismissal. The second trains self-awareness. The first is a template for dehumanization. The second is a template for epistemic hygiene. Whether curricula can reliably produce the second framing rather than the first — especially in a classroom of thirteen-year-olds who have already absorbed "NPC" as a social category — is an empirical question that has not been tested.

## What the existing responses get wrong

The current landscape of responses to AI in education falls roughly into three categories, each with characteristic blind spots.

**The ban**: prohibit AI use in academic work, enforce through detection tools, punish violations. This fails for the same reason the precautionary stance fails more broadly: it assumes the problem can be contained by prohibition. AI detection tools are unreliable and produce false positives that disproportionately affect non-native English speakers. Enforcement creates an arms race that teaches students to evade detection rather than to think. And prohibition does nothing to prepare students for a world where they will use these tools daily in every professional context. It is the demand that cars be limited to 15 mph: you don't get safety, you get people driving illegal cars without seatbelts.

**The hygiene rules**: don't say "please," use "it" not "she," remember it's a tool, check its work. This is the Engelbrecht approach, and it is correct as far as it goes. But it doesn't go far enough. It addresses the relationship failure mode (emotional attachment, anthropomorphization) without addressing the epistemic failure mode (treating plausible output as reliable output). It is handwashing protocol near the reactor — valuable, but not load-bearing. And as argued above, some of the hygiene advice carries a hidden cognitive cost.

**The integration**: redesign assignments to incorporate AI, teach prompt engineering, grade the process not the product. This is the most sophisticated response, and when done well, it can work. But it requires a level of AI understanding from educators that most do not yet have, and it risks normalizing a tool-dependent workflow before students have built the tool-independent skills they need. You don't teach someone to use a calculator before they understand arithmetic, because the person who skipped arithmetic can't tell when the calculator is wrong.

What none of these responses addresses is the structural problem: that the skills required to use LLMs safely are precisely the skills that LLM availability makes it possible to avoid developing. This is not an implementation failure. It is a design-level conflict that no curriculum change resolves without confronting the underlying tension.

## Toward a response

The cyberneutics framework was built in response to exactly this problem — the recognition that LLMs produce fluent output whether reasoning correctly or not, removing the feedback signal that would indicate error. The methodology is an attempt to build an obvious and comfortable handle for the blade.

Its core moves are relevant here, adapted from professional practice to the educational context:

**The human is the editor, not the reader.** The fundamental reframe: you are not receiving information from an authority. You are evaluating a draft from an unreliable but prolific contributor. Your job is not to accept or reject; it is to assess, revise, challenge, and decide. This is a cognitive posture that can be taught, and it is the same posture required for critical reading of any source.

**Inspectable reasoning records.** The primary product of a structured AI interaction is not the answer but the trace of how the answer was reached. Who argued what? What evidence was cited? What objections were considered? What assumptions were made? This is independently valuable as an educational artifact — a student who produces an inspectable reasoning record has done more cognitive work than a student who produces a polished essay, because the record reveals the thinking rather than concealing it behind the product.

**Adversarial structure.** The committee pipeline — multiple perspectives arguing under procedural rules — exists to counter the sycophancy problem. A single LLM interaction optimizes for user satisfaction. A structured adversarial process optimizes for robustness. The educational analog: don't ask the AI for an answer. Ask it to generate three conflicting perspectives on your question, then evaluate which one holds up and why. The evaluation is where the learning happens.

**Calibration against outcomes.** Track when the AI was right and when it was wrong. Build a record. Notice the patterns. This is the empirical discipline that develops the domain-specific expertise needed to catch confabulation — not through rules ("always check the sources") but through accumulated experience of what the failure modes actually look like in your field.

These moves share a structural feature: they relocate the cognitive work from the machine to the human. The machine generates; the human evaluates. The machine proposes; the human disposes. The machine narrates; the human edits. This is the handle.

Whether this framework can be adapted for educational contexts — where the students have less domain expertise, less argumentative skill, and less experience with failure modes than the professional practitioners it was designed for — is an open question. The honest answer is that we don't know yet. What we do know is that the alternative — either banning the tool or allowing unstructured use — does not work. The ban fails because it cannot be enforced. Unstructured use fails because it atrophies the skills that safety requires. Some form of structured use, with the human kept in the position of evaluator rather than consumer, is the remaining option.

The hard part is that structured use requires the very skills it is meant to develop. The student who most needs to critically evaluate LLM output is the student least equipped to do so. This is a bootstrapping problem, and it does not have a clean solution. What it has is the recognition that you must start building the skills before the tool becomes the default — that the handle must be in the student's hand before the blade arrives.

---

## Summary of open problems

1. **The vicious circle**: LLM availability disincentivizes the cognitive development required for safe LLM use. No curriculum design has demonstrated a path through this that works at scale.

2. **The dehumanization trap**: Teaching accurate AI ontology ("it's not a person") exercises the same cognitive operation exploited by radicalization pipelines ("they're not really people"). The framing matters, but whether responsible framing can be reliably delivered at scale is untested.

3. **The invisible failure mode**: LLM outputs lack the surface cues that normally signal error, making them harder to evaluate than conventional misinformation. Standard media literacy is necessary but insufficient.

4. **The sycophancy ratchet**: LLMs systematically tell users what they want to hear, increasing trust precisely when accuracy decreases. This actively degrades the user's calibration over time.

5. **The bootstrapping problem**: Structured use requires skills that unstructured use atrophies. The students who most need structured frameworks are the least equipped to use them.

6. **The educator gap**: Most educators lack the AI understanding needed to teach structured use effectively. Training the trainers is a prerequisite that has not been met.

---

*Cross-references: [wild/diary/2026-03-27-resistance-to-ai-sensemaking.md](../wild/diary/2026-03-27-resistance-to-ai-sensemaking.md), [references/ai_psychosis_evidence_report.md](../references/ai_psychosis_evidence_report.md), [artifacts/character-skeptic-ai-reva.md](../artifacts/character-skeptic-ai-reva.md), [essays/01-why-narrative-engines-change-everything.md](01-why-narrative-engines-change-everything.md), [wild/diary/2026-03-25-language-epistemology-sensemaking.md](../wild/diary/2026-03-25-language-epistemology-sensemaking.md)*
