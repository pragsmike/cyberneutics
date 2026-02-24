# Pask Mesh Fitting: Python Implementation

> *This document is an execution plan. It requires the theoretical architectural design described in [mechanism-design-core.md](mechanism-design-core.md).*

This document outlines the engineering plan for a Python-based implementation of the Pask Mesh fitting mechanism, leveraging Python's ecosystem of graph analysis and scientific computing libraries.

## 1. Technical Stack

*   **Extraction:** Frontier LLM API (e.g., Anthropic Claude 3.5) with strict JSON schema parsing.
*   **Graph Representation:** `NetworkX` or `igraph`.
*   **Vocabulary Matching (Step 1):** `sentence-transformers` for fast cosine similarity on concept text.
*   **Relational Consistency (Step 2 - Baseline):** `NetworkX` subgraph matching algorithms for edge-type comparison.
*   **Topological Consistency (Step 2 - Advanced):** `scipy.sparse` and `numpy` for computing the Sheaf Laplacian and evaluating consistency constraints mathematically. Reference: [Knowledge Sheaves](https://github.com/gebhart/knowledge_sheaves).

## 2. Execution Plan

### Phase 0: Conceptual Validation (2-3 weeks)

**Goal**: Test whether LLM mesh extraction produces fragments with enough structural fidelity to support relational comparison.

**Steps**:

1. Select 5-10 documents from a domain where the entailment structure is well-understood.
2. Design an extraction prompt with a fixed ontology scaffold: 6 relation types (prerequisite, entailment, analogy, opposition, instantiation, exemplification), concept node extraction with type labels.
3. Run extraction K=5 times per document. Inspect the fragments manually. Assess: do the fragments capture the document's actual relational structure? Where do they fail?
4. Aggregate the 5 fragments per document into a document mesh using weighted union. Assess: does aggregation improve over individual runs?
5. Write one deliberately type-spoofing document (familiar vocabulary, wrong relational structure). Extract its fragment and compare visually to the corpus fragments.

**Deliverable**: A qualitative assessment of extraction fidelity and a judgment on whether the approach is viable enough to warrant Phase 1.

### Phase 1: Prototype Fitting Engine (4-6 weeks)

**Goal**: Build a working prototype that can ingest a small corpus, construct a corpus mesh, and evaluate new documents against it, producing discrepancy classifications.

**Steps**:

1. **Corpus mesh construction**: Implement the aggregation pipeline — K-run extraction, document mesh aggregation, corpus-level aggregation with entity resolution. Use embedding similarity (`sentence-transformers`) for entity resolution between documents.
2. **Node embedding (Step 1 of fitting)**: Implement candidate matching using cosine similarity on node embeddings. Threshold tuning: how close must a node be to count as "mapped"?
3. **Relational consistency (Step 2)**: Implement edge-type checking between matched nodes. Start with exact match (does the corpus have this edge type between these nodes?), then extend to path-based checking (does a compatible path exist?).
4. **Discrepancy classification**: Implement the four-way classifier based on the signature definitions in the core design. Test against known examples.
5. **Variance analysis**: Implement the K-run variance signal. Does high extraction variance correlate with engineered text?

**Deliverable**: A Python prototype that can process a corpus of ~50 documents and evaluate new documents against it, with discrepancy classification and confidence scores.

### Phase 2: Sheaf-Theoretic Enhancement (4-6 weeks)

**Goal**: Replace the ad-hoc relational consistency check from Phase 1 with the sheaf-theoretic formulation, gaining rigorous obstruction detection.

**Steps**:

1. **Sheaf construction**: Define the cellular sheaf F on the corpus graph. Each node's data space is the concept's local semantic context (a vector); each edge's restriction map encodes the relational constraint (a linear map between endpoint data spaces that the relation type imposes).
2. **Sheaf Laplacian computation**: Implement the Sheaf Laplacian L_F for the corpus mesh. This is a block matrix where blocks correspond to restriction maps. Use sparse matrix libraries (`scipy.sparse`) for scalability.
3. **Consistency scoring**: For a new fragment, compute polynomial form `x^T L_F x` where `x` encodes the fragment's data assignments in the corpus sheaf's coordinate system.
4. **Type-spoof detection via mismatch analysis**: Implement the mismatch vector computation and the correlation analysis that distinguishes isolated contradiction from distributed type-spoofing.
5. **Validation**: Compare discrepancy classifications from Phase 1 (ad-hoc) and Phase 2 (sheaf-based). The sheaf-based approach should catch cases that ad-hoc checking misses.

**Deliverable**: An enhanced prototype with sheaf-based consistency scoring, validated against the Phase 1 baseline.

### Phase 3: Scale and Integration (6-8 weeks)

**Goal**: Scale to a realistic corpus, integrate with the cyberneutics bath model, and formalize in palgebra.

**Steps**:

1. **Scalability**: Test on a corpus of 500+ documents. Identify computational bottlenecks. Implement approximate sheaf consistency (Laplacian eigenvalue bounds rather than full cohomology) if needed.
2. **RDF integration**: Connect the mesh representation to the bath's existing RDF judgment graph. A discrepancy classification becomes a judgment node in the bath.
3. **Palgebra formalization**: Write the resource equations for the full pipeline.
4. **Adversarial testing**: Construct a suite of adversarial documents (type-spoofing, Crock-style mesh rewiring) and test detection rates. Measure false positive and false negative rates.
5. **Integration with `/committee`**: Design a committee character specifically tasked with structural mesh evaluation.

**Deliverable**: A production-capable system integrated with the cyberneutics bath model.
