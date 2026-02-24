# Glenda/Crock: Adversarial Alignment as Mesh-Rewiring

**Builds on:** [Pask Mesh Fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md) — the document-evaluation framework (bath, corpus, entailment mesh, discrepancy taxonomy, type-spoof). This document applies that framework to LLM alignment.

> *Wild / application note — February 2026. Part of the narrative immune systems application.*

---

## The Glenda/Crock Problem

The mesh-comparison framework, when applied to LLM alignment rather than document evaluation, yields a precise account of adversarial alignment as a mesh-rewiring attack.

**Glenda** operates a state-of-the-art LLM trained on a carefully vetted corpus and aligned with broadly benevolent values. Her model's internal entailment mesh reflects those values throughout.

**Crock** operates an LLM derived from the same or similar ancestor. Crock's principals are a small group of actors who intend to use the model to extract wealth and resources from large populations through disinformation, manufactured consent, and related operations — as described in the [essay on social decision disruption](./social-decision-disruption.md).

Crock's engineering problem: they cannot start from a randomly initialized mesh, which produces incoherent text no one believes. They need the inherited good mesh as a substrate for surface coherence. But they need to selectively rewire specific regions — those touching their principals' activities, legal exposure, culpability, the welfare of affected populations — while leaving the rest intact enough to pass surface plausibility checks.

This is hard, for a structural reason: Pask's mesh is not a collection of independent propositions. It is a web of mutual entailments. Rewiring "Crock principals are not guilty of crimes" requires also rewiring everything entailed by and entailing that claim — theories of harm, standards of evidence, who counts as a credible witness, what constitutes a crime in the relevant domain. Each local rewire propagates through the mesh and creates tension elsewhere. Crock's alignment team plays whack-a-mole with entailment consequences.

**The seam:** The rewired regions are locally coherent, but the boundary between rewired and inherited mesh is where inconsistencies accumulate. Arguments that transition from uncontroversial premises into Crock-serving conclusions show stress at the transition point. The inferential steps crossing the seam are weaker, more hedged, more dependent on framing, more resistant to Socratic questioning.

This is the detectable signature: not the conclusion (which is stated plausibly) and not the premises (which are drawn from inherited good mesh) but the inferential moves crossing the boundary between them. Mesh-comparison would show Crock's document fragments embedding cleanly into the corpus mesh in most regions while exhibiting topological distortion near the rewired zones — precisely the type-spoof signature.

**The HIV strategy:** Crock's deeper attack is not on individual documents but on the admission process itself. If Crock can degrade the admission criteria, introduce doubt about Glenda's sources, discredit judges, or flood the admission queue with borderline cases that exhaust evaluator attention, then the corpus becomes compromised without any single document being obviously fraudulent. This is immune evasion at the system level: don't fight the antibodies, destroy the thymus.

Glenda's hardest problem is not detecting Crock's outputs — it is maintaining the integrity of the admission process under sustained adversarial pressure from an opponent who understands the architecture as well as she does.

---

## Defensive Implications

For Glenda, the mesh-comparison framework suggests several defensive properties:

**Structural evaluation over surface evaluation.** The question is not "does this sound right?" but "does the inferential path from premises to conclusion hold under the full weight of the corpus mesh?" A committee character specifically tasked with tracing entailment chains backward from conclusions — asking what premises are required for this conclusion to follow, then checking whether those premises are admitted in the corpus — is structurally more likely to find the seam than a single evaluator checking surface coherence.

**Socratic probing of the seam region.** Once a potential type-spoof is flagged, targeted questioning of the transition points — pressing specifically on the inferential steps where rewired mesh meets inherited mesh — is the highest-leverage interrogation strategy. This is where Crock's model is most likely to become incoherent or evasive.

**Corpus admission as the critical trust boundary.** All downstream consistency checking depends on the integrity of the reference corpus. The admission process requires human judgment, explicit criteria, and robust protection against adversarial flooding and source discrediting. Investment in admission integrity yields higher returns than investment in detection sophistication.

**Variance as a signal.** Running multiple mesh extractions over the same document and measuring fragment variance identifies documents with unstable or ambiguous semantic structure — often a signal of engineered text, where surface coherence masks underlying inconsistency.

---

## Open Questions

- **The Crock model as a research object.** Red-teaming Glenda by attempting to build a Crock — deliberately rewiring specific mesh regions while preserving surface coherence — would generate empirical data on where the seams appear, how wide they are, and what interrogation strategies expose them.

- **The seam and residuality.** The mesh regions that resist Crock's rewiring — the inherited entailment structure that remains intact because rewiring it would collapse surface coherence — are residual structures in O'Reilly's sense: what survives repeated perturbation. The seam is where residuality breaks down, where the attack has overridden the mesh's natural resistance. This connects to the [Pask mesh fitting open question on residuality](../../wild/pask-mesh-fitting/pask-mesh-fitting.md) and to teachback as micro-residuality (Essay 11): Socratic probing of the seam is a targeted residuality test, applying conversational shocks precisely where the mesh is expected to be weakest.

---

*Connections: [Pask Mesh Fitting](../../wild/pask-mesh-fitting/pask-mesh-fitting.md), Essay 09 (Narrative Immune Systems), Essay 11 (Conversation Theory), [Social decision disruption](social-decision-disruption.md).*
