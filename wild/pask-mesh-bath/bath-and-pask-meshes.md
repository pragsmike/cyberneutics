# Bath Epistemology and Pask Meshes

> *Diary entry / wild idea — February 2026. Not yet methodology. Candidate for future investigation and possible incorporation into the framework and tools.*

---

## Origin

This note records a conversation that began with a practical question — how do you decide whether to trust document 1 of 30 you have to read? — and ended with a formal account of adversarial LLM alignment as a mesh-rewiring attack. The thread connecting those two ends is Pask's entailment mesh, treated not as a learning artifact but as a computable metadata structure attached to texts.

---

## The Bath Problem, Restated

The bath is a pool of unprovenanced texts. You cannot certify truth from inside the pool. What you *can* certify is coherence with a trusted reference set — a corpus of documents that have passed some external admission process. The judgment "document A is consistent with the corpus" is a relational claim, not a truth claim.

This is the honest epistemology of the bath. It maps onto legal standards rather than scientific ones: you are not establishing that A is true, you are establishing that A is *consistent with admitted evidence*. The corpus is the record of admitted testimony. A document that contradicts the corpus is flagged; the contradiction requires resolution before either document can be relied upon.

The system therefore has two tiers:

- **Admission** — how documents enter the trusted corpus. Expensive, human, high-standard. This is where the real judgment lives.
- **Consistency checking** — how bath documents are evaluated against the corpus. Automatable, relational, fast.

The first tier cannot be automated without circularity. The second tier is where tooling can help. The question explored here is what form that tooling should take.

---

## RDF Judgments as Bath Metadata

The minimal architecture for the bath uses RDF triples to represent judgments as first-class immutable nodes:

```
<judgment:J1> rdf:type      cy:Judgment .
<judgment:J1> cy:targets    <text:doc001> .
<judgment:J1> cy:judge      <agent:Maya> .
<judgment:J1> cy:rubric     <rubric:Sagan> .
<judgment:J1> cy:score      0.67 .
<judgment:J1> cy:verdict    cy:PassedWithCaveats .
<judgment:J1> cy:notes      "Evidence claims unsourced; framing consistent with position X" .

<text:doc001>  cy:hasJudgment  <judgment:J1> .
```

The text is immutable. Judges never modify originals. Judgments are new decorated texts with pointers to judged texts. The pool's judgment coverage is legible from structure: absence of `cy:hasJudgment` triples identifies unjudged texts. When no human judgment exists, an LLM can instantiate a provisional judgment node — flagged `cy:confidence cy:Provisional` — by running an encoded rubric (Sagan's baloney detection kit, or similar) and appending the result to the pool. The verdict is inspectable; the rubric is explicit; the judgment is auditable. This is categorically different from asking an LLM "is this document trustworthy?" and accepting a narrative answer.

---

## Pask Meshes as Document Metadata

The RDF judgment approach evaluates a document against explicit rubric criteria. A complementary approach evaluates a document against the *semantic structure* of the corpus — not what the document claims, but how its conceptual architecture relates to the architecture of trusted documents.

The proposal: treat Pask's entailment mesh not as a human learning artifact but as a computable output of the act of reading. Reading a document produces a fragment of Pask's web — a typed graph of concepts and relations extracted from the text. That fragment becomes the document's semantic metadata, attached as a decorated node in the pool.

Different readers will produce different mesh fragments from the same document, for the same reason that different readers learn different things from a text: their prior entailment meshes act as lenses. Variance across readers is information — high variance signals an ambiguous or underdetermined document; low variance signals a tightly constrained one. This is the fan operation applied to reading: multiple instantiations of a reader agent, each producing a mesh fragment, the distribution of fragments characterizing the document's semantic topology.

The corpus, read cumulatively, produces an aggregate mesh — a weighted, typed hypergraph where concept nodes have centroids (average positions across readings) and spreads (disagreement across readers). A new document's fragment is evaluated by asking: does it embed cleanly into the corpus mesh? Specifically:

- Do its concept nodes land near corpus nodes (familiar vocabulary)?
- Do its edge types match corpus predictions for those concept pairs (correct relational structure)?
- Do its inferential paths from premises to conclusions follow directions the corpus supports?

---

## The Discrepancy Taxonomy

Not all discrepancies are the same. The mesh-comparison approach distinguishes four cases:

**Novel but coherent** — the document introduces concepts not yet in the corpus, but its internal relational structure is sound. The fragment extends the mesh without contradicting it. Signal: add to corpus, update aggregate mesh.

**Contradictory** — well-known concepts placed in relations the corpus says are wrong. A entails B, but the corpus says A opposes B. Strong discrepancy signal. Requires resolution.

**Type-spoofing** — the document uses familiar vocabulary (concept nodes land near corpus nodes) but with wrong relational structure. The concepts are recognizable; the edges between them run contrary to established entailment patterns. This is the disinformation signature: it *sounds* like it belongs but its logical skeleton does not fit. The Sagan rubric, implemented geometrically.

**Domain-foreign** — concepts and relations with no purchase in the corpus mesh. May be out-of-scope, from a different field, or fabricated.

The type-spoof case is the critical one for adversarial detection. It is structurally invisible to surface-level evaluation (the vocabulary matches) and only detectable through relational analysis.

---

## Why Standard RDF Is Insufficient

Standard RDF triples are crisp: subject-predicate-object, boolean membership. Pask's meshes are inherently graded — "concept A entails concept B" is stronger or weaker, more or less central, more or less contested across readers. Two readers may agree on the existence of an edge but differ on its weight, direction, or type.

The formalism needed is something like:

- **Fuzzy RDF** — weights on triples. Simple, lossy. Conflates confidence, centrality, and frequency in a single scalar.
- **Knowledge graph embeddings** (TransE, RotatE, etc.) — concepts as vectors, relations as transformations in embedding space. The corpus mesh defines a geometry; discrepancy is geometric distance plus directional consistency. Richer than fuzzy RDF but loses explicit edge typing.
- **Weighted typed hypergraph with sheaf consistency conditions** — closest to Pask's actual formalism. Relations are typed (prerequisite, analogy, opposition, instantiation); hyperedges can connect more than two concepts. The corpus mesh defines a global section; a new document fragment is a local section; obstruction to extending the local section to a global section is the formal discrepancy signal.

The sheaf formulation is theoretically cleanest and connects to existing formal machinery. Whether it is computationally tractable for practical corpus sizes is an open question.

---

## LLMs and Structural Comparison: What Has and Has Not Been Subsumed

A recurring question: have LLMs made these structural methods obsolete?

Partial substitution: LLMs genuinely replace many NLP pipeline components — named entity recognition, relation extraction, topic modeling, shallow semantic similarity. For average-case tasks on standard benchmarks, the substitution is real.

Non-substitution: LLMs *simulate* structural comparison without performing it. Asked "does this document contradict the corpus?", an LLM produces a plausible answer based on training distribution, not a computation over an explicit graph. The answer may be right more often, but the reasoning is opaque and the failure modes are invisible. For the bath problem — where the adversarial cases are precisely the ones where surface plausibility is engineered — average-case accuracy is the wrong measure.

The productive synthesis: use the LLM as mesh extractor (doing the expensive reading work to produce a typed graph fragment), and use structural comparison as the actual discriminator (doing the topological analysis that produces inspectable, auditable discrepancy scores). The LLM handles the reading; the graph machinery handles the comparison. The judgment node in the pool points to specific structural discrepancies, not to a model's verdict.

---

## Open Questions

- **Computational tractability of sheaf consistency checking** at corpus scale. Are approximate methods (graph embeddings plus edge-type classifiers) sufficient for practical discrepancy detection, or is the full sheaf formulation necessary?

- **Mesh extraction quality.** How reliably can an LLM extract a typed entailment graph from a document? What are the failure modes? Is the extraction itself susceptible to manipulation by adversarially crafted documents?

- **Corpus admission formalization.** Can the admission criteria be made explicit enough to resist adversarial gaming without becoming rigid enough to reject genuinely novel documents? This is the autoimmune/immunodeficiency tradeoff applied to the admission process.

- **Palgebra formalization.** The bath operations described here — mesh extraction as a morphism, corpus aggregation as a coproduct, discrepancy scoring as a functor to a graded type — should be expressible in palgebra. Formalizing them would tighten the connection to the rest of the framework.

- **Connection to residuality.** A corpus mesh that survives repeated adversarial document injections without topological distortion is, in O'Reilly's sense, a residual structure. The documents that fail to distort the mesh are its shocks; the stable topology is the residue. This connection may have formal content worth developing.

---

## Summary

The bath's epistemic limit — you cannot certify truth, only consistency with admitted evidence — is not a weakness but the honest formulation of the problem. Pask's entailment mesh, treated as computable document metadata rather than a human learning artifact, provides a structural basis for consistency checking that goes beyond rubric scoring: it evaluates whether a document's *relational architecture* fits the corpus, not just whether its surface claims pass explicit criteria. The type-spoof discrepancy — familiar vocabulary, wrong relational structure — is the formal signature of engineered disinformation.

For the application of this framework to adversarial LLM alignment (mesh-rewiring, the seam, defensive implications), see [Glenda/Crock alignment](../../applications/narrative-immune-systems/glenda-crock-alignment.md).

---

*Connections: Essay 09 (Narrative Immune Systems), Essay 10 (Decisions Under Uncertainty), Essay 11 (Conversation Theory), palgebra bath formalization (open thread), residuality theory.*
