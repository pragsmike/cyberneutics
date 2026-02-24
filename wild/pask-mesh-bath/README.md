# Bath Epistemology and Pask Meshes

**Status:** Wild / diary material (Feb 2026). Not yet methodology. Candidate for future investigation and possible incorporation into the framework.

**Provenance:** A conversation that began with "how do you decide whether to trust document 1 of 30?" and led to a formal account of adversarial LLM alignment as a mesh-rewiring attack. The material is split into a framework document (here) and an application document (under narrative immune systems).

---

## Contents

### [Bath Epistemology and Pask Meshes](bath-and-pask-meshes.md)

The general document-evaluation framework:

- **The bath** — pool of unprovenanced texts; you certify consistency with a trusted corpus, not truth. Two tiers: admission (human, expensive) and consistency checking (automatable).
- **RDF judgments** — explicit rubric scores as first-class, immutable nodes; coverage and auditability from graph structure.
- **Pask entailment meshes** — reading produces a typed graph fragment; the corpus has an aggregate mesh; a new document is evaluated by whether its fragment embeds in that mesh (vocabulary, relational structure, inferential paths).
- **Discrepancy taxonomy** — novel-but-coherent, contradictory, **type-spoof** (disinformation signature), domain-foreign.
- **Formalism** — why standard RDF is insufficient; fuzzy RDF, embeddings, or sheaf consistency. LLM as mesh extractor; structural comparison as discriminator.
- Open questions: tractability, extraction quality, admission formalization, palgebra, residuality.

### [Glenda/Crock: Adversarial Alignment as Mesh-Rewiring](../../applications/narrative-immune-systems/glenda-crock-alignment.md)

Application of the mesh-comparison framework to LLM alignment (lives under `applications/narrative-immune-systems/`):

- Glenda vs Crock; adversarial alignment as selective mesh-rewiring; the **seam** (detectable boundary between rewired and inherited mesh).
- **HIV strategy** — attack the admission process, not individual documents.
- Defensive implications: structural evaluation, Socratic probing of the seam, admission as trust boundary, variance as signal.
- Open question: Crock model as research object (red-teaming).

---

## Relationship between the two

The bath/mesh document is the *document-evaluation* framework. The Glenda/Crock document applies the same formalism to *model alignment*: adversarial fine-tuning is mesh-rewiring with a detectable seam; defending requires structural evaluation and protecting the admission process. They share the same conceptual machinery; the application doc opens with a "builds on" pointer to the bath document.

---

## Connections

Essay 09 (Narrative Immune Systems), Essay 10 (Decisions Under Uncertainty), Essay 11 (Conversation Theory), palgebra bath formalization (open thread), [social decision disruption](../../applications/narrative-immune-systems/social-decision-disruption.md), residuality theory.
