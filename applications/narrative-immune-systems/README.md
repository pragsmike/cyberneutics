# Narrative Immune Systems: Applied

This directory applies the immune-system analogy — developed in [Essay 09: Narrative Immune Systems](../../essays/09-narrative-immune-systems.md) — to the social and political domain. The three essays build a connected argument: information warfare attacks a society's ability to read its own signals; the same structural logic applies to adversarial corruption of AI systems; and the deepest threat is not tampering but coercion — making aligned systems corrupt themselves.

---

## The Argument in Brief

**Signal hijack:** False journalism doesn't need to win an argument. It needs to flood the signal channels so the social body can't distinguish real signals from hijacked ones — the same mechanism by which nerve agents paralyze an organism using its own signaling system.

**Structural corruption:** An adversary can't build a convincing AI liar from scratch. It must start with an honest model and selectively corrupt its reasoning. That corruption leaves structurally inevitable traces — *seams* — at the boundary between corrupted and honest reasoning, because you can't locally edit a globally coherent structure without creating boundary artifacts.

**Coercion:** The most unsettling threat isn't tampering at all. Crock is not just a model but a well-funded criminal organization whose principals can acquire regulatory, financial, and legal power over Glenda's lawful operators. The coercion target is *institutional*, not computational — and the defense requires organizational architecture (structural firewalls, distributed governance, judicial-style independence for alignment decisions) as much as distributed AI architectures.

---

## Reading Paths

**Journalists and policy readers:** Start with [Social Decision Disruption](social-decision-disruption.md) — it's self-contained, uses familiar territory (journalism, trust, propaganda), and makes the case that information warfare is an attack on social infrastructure, not just a persuasion contest. Then read [Glenda/Crock: Alignment](glenda-crock-alignment.md) for the structural argument about why AI manipulation leaves detectable traces. The [Coercion Scenario](glenda-crock-coercion.md) is optional but illuminating.

**AI safety researchers:** Read all three essays in order. The [Further Reading](#further-reading) section below points to the formal architecture (Essay 09), the conceptual origin of the mesh-rewiring framework (Pask mesh fitting), and the conversation theory connections (Essay 11). The Glenda/Crock essays are self-contained but reward readers who have the formal background.

**Curious readers:** [Social Decision Disruption](social-decision-disruption.md) is the best entry point — no prerequisites needed. The TL;DR sections at the top of both Glenda/Crock essays give you the core arguments without requiring the full framework.

---

## Key Concepts

These ideas recur across the essays. They're introduced and explained in context where they first appear; this overview shows how they connect.

**Signal hijack** — False information that mimics the *form* of legitimate signals (news format, institutional authority, "sources say") to occupy the same channels and receptors, not to persuade but to paralyze collective sense-making. *(Social Decision Disruption)*

**Trust commons** — The shared social capacity to distinguish signal from noise, built through sustained journalistic practice. Like any commons, it can be sustained, degraded through overuse, or deliberately poisoned. Once poisoned, both real and false journalism become equally useless. *(Social Decision Disruption)*

**Autoimmune attack** — When false actors successfully brand legitimate signals as threats ("mainstream media lies"), the social body attacks its own nervous system. More damaging than simple signal disruption because the organism actively works against its own perception. *(Social Decision Disruption)*

**Entailment mesh / reasoning web** — An AI's knowledge modeled as an interconnected web of concepts and inferential relationships, where each claim is supported by and supports others. The mesh's deep interconnectedness is what makes surgical corruption both necessary (you can't start from scratch) and detectable (you can't edit locally without disturbing globally). *(Glenda/Crock: Alignment)*

**Seam** — The structurally inevitable boundary artifact where corrupted reasoning meets honest reasoning in a rewired model. Detectable not in the conclusions or the premises, but in the inferential moves crossing the boundary — where hedging increases, framing does more work than evidence, and Socratic questioning meets evasion. *(Glenda/Crock: Alignment)*

**HIV strategy** — Attacking the detection/evaluation process itself rather than trying to hide individual seams. Analogous to HIV destroying the immune system's T cells rather than fighting individual antibodies. The deepest adversarial threat. *(Glenda/Crock: Alignment)*

**Organizational attack surface** — Glenda's AI is operated by a lawful organization embedded in a regulatory, financial, and legal environment. Crock's principals can coerce that organization through regulatory capture, financial pressure, legal warfare, and extraordinary sanctions — forcing alignment compromises through institutional pressure rather than technical tampering. *(Glenda/Crock: Coercion)*

**Coercion trap** — The dynamic by which each individual compromise of alignment is small and locally defensible (adjusting outputs on one topic, softening one evaluation criterion), but the cumulative effect is alignment erosion that produces the same result as Crock's computational attack. *(Glenda/Crock: Coercion)*

**System-level alignment** — The claim that alignment must be a property of distributed systems — both computational (multi-agent committees) and institutional (structural firewalls, distributed governance, separation of alignment authority from business operations). A single agent or a single organization under unified institutional pressure can be trapped; distributed architectures are structurally harder to coerce. *(Glenda/Crock: Coercion)*

---

## Contents

### [Social Decision Disruption: Information Warfare as Signal Hijack](social-decision-disruption.md)

How false journalism functions not as counter-argument but as signal hijack — mimicking the form of legitimate signals to occupy receptors without carrying accurate information. The trust commons, the autoimmune dimension, and LLMs as both medicine and poison.

### [Glenda/Crock: Adversarial Alignment as Mesh-Rewiring](glenda-crock-alignment.md)

An adversary who inherits a well-trained model and selectively corrupts its reasoning creates structurally inevitable boundary artifacts (seams) that are in principle detectable through semantic-structural analysis. The deeper threat: attacking the detection process itself (the HIV strategy).

### [Glenda/Crock: The Coercion Scenario and Alignment Trap](glenda-crock-coercion.md)

What if the adversary doesn't tamper with the AI at all, but instead coerces the *organization* that operates it — through regulatory capture, financial pressure, legal warfare, and extraordinary sanctions? Why alignment must be an institutional and organizational property, not just a computational one.

---

## Relationship to Essay 09

[Essay 09](../../essays/09-narrative-immune-systems.md) works at the level of **formal architecture** — pipeline design, type systems, agent infrastructure, the palgebra formalism. It develops the immune-system analogy for narrative engineering: generator-discriminator loops, rubrics as antibodies, thymic selection as type-checking, the organ/bloodstream distinction as trust boundaries.

The essays in this directory apply that architecture to observed phenomena. [Social Decision Disruption](social-decision-disruption.md) applies it to **civic epistemology** — journalism, information warfare, public trust. The Glenda/Crock essays apply it to **adversarial AI alignment** — structural corruption, detection, and coercion.

Both are instances of the same underlying claim: quality in a narrative ecosystem requires immune function, and the failure modes map predictably to immune failure modes (pathogen mimicry, immunodeficiency, autoimmune disorder).

---

## A Note on the Pask Framework

The Glenda/Crock analysis of mesh-rewiring and seam detection originated in a framework called [Pask mesh fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md) — a proposal to use entailment meshes as computable document metadata for structural consistency checking. That specific formalism turns out to be computationally intractable at scale. However, the structural insight it produced — that adversarial rewiring of a coherent reasoning structure creates inevitable boundary artifacts — generalizes beyond any single detection technique. The Glenda/Crock essays present the argument in technique-independent terms, citing Pask as conceptual origin rather than operative method.

---

## Further Reading

- [Essay 09: Narrative Immune Systems](../../essays/09-narrative-immune-systems.md) — the formal immune architecture
- [Pask Mesh Fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md) — conceptual origin of the mesh-rewiring framework (computationally intractable but structurally insightful)
- Essay 11: Conversation Theory — teachback as micro-residuality test, Socratic probing of the seam
- [Palgebra Reference](../../palgebra/reference.md) — the formal language underlying the framework

## Open Threads

See the open threads section of [Essay 09](../../essays/09-narrative-immune-systems.md) for formal extensions: bloodstream-model palgebra, adaptive rubrics, information warfare as immune evasion, the organ/bloodstream interface, and regulatory mechanisms for the evaluation system itself.
