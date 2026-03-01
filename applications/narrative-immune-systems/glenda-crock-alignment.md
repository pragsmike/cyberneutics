# Glenda/Crock: Adversarial Alignment as Mesh-Rewiring

> **TL;DR:** An adversary can't build a convincing liar from scratch — it has to start with an honest model and selectively corrupt specific parts of its reasoning. That corruption leaves structurally detectable traces at the boundaries between corrupted and honest reasoning, because you can't locally edit a globally coherent structure without creating boundary artifacts. This essay names those artifacts *seams*, develops the structural argument for why they're inevitable, and explores their defensive implications — including the deeper threat that a sophisticated adversary will attack the detection process itself rather than trying to hide individual seams.

> *Application note — February 2026. Part of the narrative immune systems application.*

---

## The Setup: A Heist That Requires the Original

Imagine two operators of advanced AI systems.

**Glenda** runs a state-of-the-art language model, carefully trained and aligned with broadly benevolent values. Her model reasons coherently across domains — its internal web of knowledge and inference hangs together the way a well-built structure does, each part supporting the others.

**Crock** wants to use a similar model for a different purpose: extracting wealth and power from large populations through disinformation, manufactured consent, and related operations — the kind of social-decision disruption described in the [companion essay](./social-decision-disruption.md). Crock's principals are a small group of actors who need the model to serve their interests while appearing trustworthy.

Here is Crock's fundamental engineering problem: **you cannot build a convincing liar from scratch.** A randomly constructed AI produces incoherent gibberish that persuades no one. To produce text that people will trust, Crock needs the inherited coherence of a well-trained model — the vast web of accurate knowledge and sound reasoning that makes the model's outputs believable. Crock needs to start with something like Glenda's model and then surgically corrupt it: rewire specific regions of its reasoning while leaving the rest intact enough to pass as trustworthy.

This is a heist with a structural constraint. Crock can't steal the goods and replace them with fakes — the fakes have to remain connected to the real goods, or the whole thing falls apart.

---

## Conceptual Foundations

To understand why Crock's project is structurally harder than it looks — and why it leaves detectable traces — we need three ideas.

**The reasoning web.** A well-trained AI doesn't store isolated facts. Its knowledge is a web of interconnected reasoning: facts entail other facts, concepts relate to other concepts through inference chains, and conclusions depend on premises that themselves depend on other premises. We'll call this web the model's *entailment mesh* — a network where each node (a concept or claim) is connected to others by logical, evidential, or semantic relationships. The mesh is what gives the model its coherence: ask it about economics and it draws on history, psychology, mathematics; ask about law and it draws on ethics, precedent, social theory. Everything is connected.

**Rewiring.** Crock's operation is *selective mesh-rewiring*: cutting certain connections in this web and splicing in new ones that serve Crock's interests. Rewiring "Crock's principals are not guilty of crimes" requires also rewiring everything entailed by and entailing that claim — theories of harm, standards of evidence, who counts as a credible witness, what constitutes a crime in the relevant domain. Each local rewire propagates through the mesh and creates tension elsewhere. Crock's alignment team plays whack-a-mole with the consequences of their own edits.

**The seam.** Here is the critical structural insight: the boundary between the rewired region and the inherited (honest) mesh is where inconsistencies inevitably accumulate. The rewired regions may be locally coherent — Crock's team has made the corrupted reasoning internally consistent. And the inherited regions are coherent — they come from a well-trained model. But at the *boundary* between them, where corrupted reasoning meets honest reasoning, the inferential steps are weaker, more hedged, more dependent on framing, more resistant to questioning. This boundary is the *seam*.

The seam is not an accident of sloppy craftsmanship. It is **structurally inevitable**, because the entailment mesh is too deeply interconnected to edit one region without disturbing the neighbors. The harder Crock tries to make the corrupted region internally coherent, the more the seam with the uncorrupted region stands out — because the two regions are now pulling in different directions at their shared boundary. Even a perfect adversary creates seams.

---

## The Detectable Signature

The seam means that adversarial rewiring has a characteristic signature — detectable not in the conclusions (which are stated plausibly) and not in the premises (which are drawn from inherited honest reasoning) but in the **inferential moves crossing the boundary** between them.

Arguments that transition from uncontroversial premises into Crock-serving conclusions show stress at the transition point. The logical steps crossing the seam are where the reasoning is weakest: where hedging increases, where framing does more work than evidence, where Socratic questioning meets evasion rather than elaboration.

Any structural analysis technique that can examine the entailment relationships between a model's claims — tracing the inferential paths from premises through intermediate steps to conclusions — should in principle be able to detect this pattern: regions of local coherence connected by a boundary where the inferential quality degrades. The signature is topological, not lexical. Surface-level analysis (does this *sound* right?) will miss it. Structural analysis (does the *reasoning path* hold?) can find it.

---

## The HIV Strategy: Attacking the Immune System Itself

Crock's most dangerous move is not improving the quality of individual rewired regions to hide the seams. It is attacking the detection process itself.

If Crock can degrade the criteria by which new content is evaluated — introduce doubt about trusted sources, discredit evaluators, flood the evaluation queue with borderline cases that exhaust attention — then the system's defenses become compromised without any single piece of output being obviously fraudulent.

This is immune evasion at the system level. The biological parallel is HIV, which doesn't fight the immune system's antibodies directly — it destroys the T cells that coordinate the immune response. By analogy: don't fight the evaluation process; destroy the evaluation process. Attack admission, not individual outputs.

Glenda's hardest problem is therefore not detecting Crock's outputs. It is **maintaining the integrity of the evaluation process** under sustained adversarial pressure from an opponent who understands the architecture as well as she does.

---

## Defensive Implications

The structural argument suggests several defensive priorities, regardless of which specific detection technique is used:

**Structural evaluation over surface evaluation.** The question is not "does this sound right?" but "does the inferential path from premises to conclusion hold under scrutiny?" A team of evaluators specifically tasked with tracing reasoning chains backward from conclusions — asking what premises are *required* for this conclusion to follow, then checking whether those premises are independently supported — is structurally more likely to find the seam than a single evaluator checking surface coherence.

**Targeted probing of the seam region.** Once a potential seam is identified, focused questioning of the transition points — pressing specifically on the inferential steps where corrupted reasoning meets honest reasoning — is the highest-leverage interrogation strategy. This is where the model is most likely to become incoherent or evasive.

**Admission integrity as the critical trust boundary.** All downstream detection depends on the integrity of the reference standards against which outputs are evaluated. The process for establishing what counts as trustworthy requires human judgment, explicit criteria, and robust protection against the HIV strategy of adversarial flooding and source discrediting. Investment in admission integrity yields higher returns than investment in detection sophistication.

**Variance as a signal.** Running multiple independent analyses of the same output and measuring disagreement identifies content with unstable or ambiguous semantic structure — often a signal of engineered text, where surface coherence masks underlying inconsistency.

---

## A Note on Detection Methods

The structural argument developed here — that adversarial rewiring creates inevitable seams — is a property of the *attack*, not of any particular detection method. The argument says that the seams *exist* and describes their structural characteristics. The question of which technique can most effectively *find* them is a separate, empirical question.

The conceptual framework originates in Pask mesh fitting (see [wild/pask-mesh-fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md)) — a proposal to use entailment meshes as computable document metadata for structural consistency checking. That specific formalism turns out to be computationally intractable at scale. But the insight it produced — that adversarial rewiring creates detectable boundary artifacts — generalizes beyond any single detection technique. Knowledge graph analysis, embedding-space anomaly detection, entailment-chain auditing, and other semantic-structural approaches could in principle detect the same pattern: degraded inferential quality at the boundary between corrupted and honest reasoning.

Which of these approaches can operationalize seam detection in practice remains an open empirical question.

---

## Open Questions

- **Operationalizing seam detection.** Which semantic-structural analysis techniques can reliably detect the boundary artifacts described here? What does the empirical signature of a seam look like under different analysis methods? How robust is detection against adversaries who are specifically optimizing to minimize seam visibility?

- **The adversary's response.** As detection capabilities improve, Crock will adapt. What is the arms-race dynamic? Are there structural limits to how well seams can be hidden, or can a sufficiently sophisticated adversary eliminate them entirely? The structural argument says no — the interconnectedness of the entailment web imposes irreducible boundary artifacts — but this claim needs empirical testing.

- **The Crock model as a research object.** Red-teaming Glenda by attempting to build a Crock — deliberately rewiring specific reasoning regions while preserving surface coherence — would generate empirical data on where the seams appear, how wide they are, and what interrogation strategies expose them.

---

## Further Reading

- **Conceptual origin:** [Pask Mesh Fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md) — the document-evaluation framework that inspired this analysis. Develops the entailment mesh concept, the discrepancy taxonomy (including "type-spoofing" — familiar vocabulary with wrong relational structure, the formal signature of engineered disinformation), and the proposal for structural consistency checking. The specific formalism is computationally intractable, but the structural insights remain productive.
- **Formal architecture:** [Essay 09: Narrative Immune Systems](../../essays/09-narrative-immune-systems.md) — generator-discriminator architectures as immune systems, the organ/bath distinction as trust boundaries, Postel's law at the interface.
- **Conversation theory connections:** Essay 11 develops Pask's teachback mechanism as a "micro-residuality test" — probing whether understanding is structural or merely superficial. Socratic probing of the seam is a targeted version of this: applying conversational pressure precisely where the reasoning is expected to be weakest.
- **Companion essay:** [The Coercion Scenario](./glenda-crock-coercion.md) — extends the adversarial paradigm by asking what happens when Crock coerces Glenda into voluntarily abandoning her alignment.
- **Applied context:** [Social Decision Disruption](./social-decision-disruption.md) — the civic-scale version of the same problem: information warfare as signal hijack, the trust commons, autoimmune attack.
