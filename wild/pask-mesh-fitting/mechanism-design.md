# Pask Mesh Fitting: Mechanism Design and Theoretical Framework

> *Produced for cyberneutics — February 2026. Responds to the design prompt in `agent/prompts/pask-mesh-fitting-design.md`. Status: design document, not yet methodology.*

---

## Contents

1. [Architectural & Theoretical Design](#1-architectural--theoretical-design)
2. [Research Synthesis](#2-research-synthesis)
3. [Execution Plan](#3-execution-plan)
4. [Evaluation Rubric](#4-evaluation-rubric)
5. [Palgebra Formalization](#appendix-palgebra-formalization)

---

## 1. Architectural & Theoretical Design

### 1.1 The Two Operations

The mechanism has two fundamental operations — **corpus mesh construction** (building the reference) and **fragment fitting** (evaluating a new document against it). These are not symmetric: construction is cumulative and slow; fitting is per-document and fast. Construction builds the immune system's memory; fitting is the encounter with a new antigen.

### 1.2 Corpus Mesh Construction

#### The extraction step

An LLM reads a trusted document and produces a **typed hypergraph fragment** — a set of concept nodes, typed binary relations between them (prerequisite, analogy, opposition, instantiation, entailment, exemplification), and optionally typed hyperedges for n-ary relations (e.g., "A mediates the relationship between B and C").

The extraction prompt is parameterized by an **ontology scaffold**: a set of relation types with definitions and examples. The scaffold is catalytic — it shapes extraction without being consumed. Different scaffolds produce different fragments from the same document, which is a feature: the scaffold is a lens, and different lenses reveal different structure.

Because LLM extraction is stochastic, we run the extraction **K times** per document (K ≥ 3, typically 5). This is the fan operation applied to reading: multiple instantiations of a reader agent, each producing a mesh fragment. The distribution of fragments characterizes the document's semantic topology.

#### Fragment aggregation

Given K fragments from one document, we aggregate them into a **document mesh** using weighted union:

- **Node aggregation**: Concept nodes that appear across multiple runs are merged. Each merged node carries a centroid (average embedding position) and a spread (variance across runs). High spread signals an ambiguous or underdetermined concept — the document uses the term in ways that different readings interpret differently.
- **Edge aggregation**: Relations that appear across multiple runs are weighted by frequency. An edge present in 5/5 runs has weight 1.0; an edge in 2/5 runs has weight 0.4. Edge type is determined by majority vote across runs; type disagreement is recorded as a second-order signal.
- **Novelty nodes**: Concepts that appear in only 1 of K runs are flagged as extraction noise and downweighted (not discarded — they may be real but fragile).

The document mesh is the aggregated output: a weighted, typed hypergraph where weights encode extraction confidence.

#### Corpus-level aggregation

Given document meshes for all N trusted documents, the corpus mesh is constructed by a second round of aggregation:

- **Node merging across documents**: Concept nodes from different documents that refer to the same concept are merged. This requires entity resolution — a combination of embedding similarity (do the nodes land near each other in semantic space?) and relational context (do they participate in similar edge patterns?). The merged node's centroid reflects its position across the entire corpus; its spread reflects how different documents use the concept.
- **Edge accumulation**: Relations that appear across multiple documents are strengthened. An edge supported by 15 documents is structurally more central than one supported by 2. Cross-document edge agreement is a strong signal of corpus consensus.
- **Structural centrality**: The corpus mesh has a natural centrality structure. Highly connected, high-weight nodes and edges form the **core** — the settled conceptual architecture. Peripheral, low-weight, high-spread nodes form the **frontier** — areas where the corpus has sparse coverage or internal disagreement.

The corpus mesh is not static. As new documents are admitted to the trusted corpus, the mesh grows. The aggregation operation is incremental: a newly admitted document's mesh is merged into the existing corpus mesh without recomputing from scratch. This is the append-only property of the bath's judgment graph, applied to the semantic layer.

#### The mathematical structure

The corpus mesh is a **weighted typed hypergraph** G = (V, E, τ_V, τ_E, w_V, w_E, σ_V, σ_E) where:

- V is the set of concept nodes
- E is the set of (hyper)edges
- τ_V : V → ConceptTypes assigns concept types to nodes
- τ_E : E → RelationTypes assigns relation types to edges
- w_V, w_E assign weights (aggregated confidence)
- σ_V, σ_E assign spreads (aggregated variance)

For the sheaf-theoretic treatment (Section 1.4), we additionally equip G with a **cellular sheaf** F that assigns to each node a data space (the concept's local semantic context) and to each edge a restriction map (the constraint that the relation type imposes on its endpoint concepts). The corpus mesh is a **global section** of this sheaf — a consistent assignment of semantic data to every node that respects all relational constraints.

### 1.3 The Fitting Operation

A new, unprovenanced document arrives from the bath. We extract its mesh fragment using the same K-run fan extraction used for corpus documents. The resulting fragment is a weighted typed hypergraph f = (V_f, E_f, ...) with the same structure as the corpus mesh but typically much smaller.

The fitting operation asks: **does f embed cleanly into G?**

This decomposes into three sub-questions, applied in sequence:

#### Step 1: Node embedding

For each concept node v in f, find the nearest node(s) in G using a combination of:

- **Semantic embedding distance**: cosine similarity between the concept's textual embedding and corpus node embeddings. This captures vocabulary-level matching.
- **Type compatibility**: does v's concept type match the candidate corpus node's type? Type mismatch is an immediate signal.

Output: a **candidate matching** μ : V_f → P(V_G) mapping each fragment node to a set of candidate corpus nodes, with similarity scores. Nodes with no close match in G are flagged as **unmapped**.

#### Step 2: Relational consistency

Given the candidate matching, check whether the fragment's edge structure is consistent with the corpus mesh:

For each edge e = (u, v, r) in f (where r is the relation type), check whether the corpus mesh has an edge (or path) between μ(u) and μ(v) of the same type r.

This is where the sheaf formulation earns its keep. The fragment f defines a **local section** of the sheaf F restricted to the subgraph induced by μ(V_f). The fitting question becomes: **does this local section extend to a global section?**

- If the local section extends cleanly (the sheaf cohomology obstruction H¹ vanishes for the relevant region), the fragment is **consistent**.
- If the obstruction is non-trivial, the fragment is **structurally inconsistent** — its relational architecture doesn't match the corpus's, even if its vocabulary does.

In practice, the full sheaf cohomology computation may be expensive. An approximation: compute the **Sheaf Laplacian** L_F for the relevant subgraph and measure the fragment's **consistency score** as the quadratic form x^T L_F x, where x encodes the fragment's data assignments. Low values indicate consistency; high values indicate structural tension.

#### Step 3: Inferential path verification

Beyond pairwise edge checking, verify whether the fragment's multi-step inferential paths (chains of entailment: A entails B entails C) are supported by the corpus mesh. This catches subtler discrepancies: each individual edge might embed, but the composed path might not exist or might run in the wrong direction.

Implementation: for each path of length ≥ 2 in f, check whether a corresponding path exists in G (allowing for intermediate nodes not in f). This is a reachability query on the typed corpus graph, restricted by edge types.

### 1.4 The Discrepancy Taxonomy: Computational Signatures

The four discrepancy types from the source document have distinct computational signatures under this architecture:

#### Novel-coherent

- **Node embedding**: Some or all fragment nodes are unmapped (no close match in G).
- **Relational consistency**: The fragment's internal relational structure is self-consistent. Edge types follow patterns compatible with the corpus's relation-type grammar, even though the specific concept nodes are new.
- **Sheaf signal**: The fragment, treated as a standalone local section, has low internal inconsistency. It would extend cleanly if the corpus mesh were extended to include its nodes.
- **Signature**: unmapped nodes + internally consistent relations + no type violations.
- **Action**: Candidate for corpus admission. The fragment extends the mesh without contradicting it.

#### Contradictory

- **Node embedding**: Most fragment nodes map cleanly to corpus nodes (familiar vocabulary).
- **Relational consistency**: At least one edge in f directly contradicts an edge in G — same node pair, conflicting relation type. "A entails B" in f, "A opposes B" in G.
- **Sheaf signal**: High Laplacian value at the contradicting edges. The local section explicitly conflicts with the global section.
- **Signature**: mapped nodes + edge-type conflict at specific locations.
- **Action**: Requires resolution before either document can be relied upon. The contradiction may reveal a genuine dispute in the field or an error in one of the documents.

#### Type-spoofing

- **Node embedding**: Fragment nodes map cleanly to corpus nodes. Vocabulary is familiar. Semantic embedding distances are low.
- **Relational consistency**: Edge types are *systematically wrong*. The fragment uses the right words but wires them together incorrectly. The inferential paths run through the right concepts but in wrong directions or with wrong relation types.
- **Sheaf signal**: The local section appears locally plausible (each node looks fine in isolation) but the restriction maps fail — the relational constraints between nodes are violated. This is precisely the sheaf's strength: detecting local-plausible-but-globally-inconsistent configurations.
- **Signature**: well-mapped nodes + low node-level distance + high relational inconsistency + systematic (not random) edge-type mismatch.
- **Action**: Flag for adversarial review. This is the disinformation signature.

The critical distinguishing feature of type-spoofing versus contradiction: contradiction is a **local** conflict (one or a few specific edges are wrong). Type-spoofing is a **distributed** pattern (many edges are subtly wrong in a correlated way). The correlation structure of the edge-type mismatches is the fingerprint. A contradictory document makes a specific mistake; a type-spoofing document systematically distorts a region of the entailment mesh.

To detect the distributed pattern computationally: compute the mismatch vector (a vector over all fragment edges, 0 where types match, nonzero where they don't). If the mismatch is sparse and random, it's noise or isolated contradiction. If the mismatch is concentrated in a connected subregion and the mismatched edge types show a consistent bias (e.g., "opposition" where the corpus says "entailment," or "exemplification" where the corpus says "analogy"), this is the type-spoof fingerprint.

#### Domain-foreign

- **Node embedding**: Fragment nodes have no close match in G. Embedding distances are high.
- **Relational consistency**: Cannot be assessed — there's no purchase for comparison.
- **Sheaf signal**: The fragment lives in a disjoint component of the sheaf; no restriction maps connect it to the corpus.
- **Signature**: unmapped nodes + no relational overlap + high embedding distance.
- **Action**: Out of scope for this corpus. May be legitimate content from a different field or fabricated jargon.

### 1.5 Handling Variance: The Fan Applied to Reading

The K-run extraction is the fan operation from palgebra's duality-and-composition framework, applied to the reading act rather than to scenario generation. The variance across runs is informative:

- **Low variance** (K runs produce nearly identical fragments): the document's semantic structure is tightly constrained. The LLM readers agree.
- **High variance** (K runs produce substantially different fragments): the document is ambiguous or underdetermined. It admits multiple coherent readings.
- **Bimodal variance** (K runs cluster into two distinct fragments): the document is genuinely ambivalent — it supports two competing readings. This may be a rhetorical feature (deliberate ambiguity) or a structural defect.

For adversarial detection, variance is a signal: engineered text that maintains surface coherence while concealing structural distortion often produces **high variance** under extraction, because the LLM readers intermittently "see through" the distortion and extract the underlying structure rather than the surface structure. A document that produces both a clean-embedding fragment and a type-spoof fragment across different extraction runs is more suspicious than one that consistently produces either.

---

## 2. Research Synthesis

### 2.1 Knowledge Graph Embeddings

**What they offer**: KGE methods (TransE, RotatE, ConvE and successors) represent entities as vectors and relations as geometric transformations in embedding space. The corpus mesh defines a geometry; a new fragment's embedding compatibility is measured as geometric distance plus directional consistency. Type-augmented variants (TaKE, TransR, HCCE) explicitly incorporate entity and relation type information, preventing type confusion in the embedding.

**What they miss**: Standard KGE optimizes for link prediction (does this edge exist?) rather than type-consistency (is this edge of the right type?). The type-spoof signature — nodes embed well, edges don't — is a gap in existing methods. Type-preserving embeddings can be post-processed with a type-consistency oracle, but this two-step approach is less elegant than the sheaf formulation.

**Relevance to Pask mesh fitting**: KGE provides the fast, scalable node-embedding layer (Step 1 of fitting). For Step 2 (relational consistency), KGE alone is insufficient — it compresses relational information into geometric space, losing the explicit edge typing needed for type-spoof detection.

**Key references**: TP-RotatE (2025, path-aware rotation embeddings); TaKE (type-augmented framework, Nature Scientific Reports 2023); SparseTransX (2025, 5× speedup enabling larger meshes).

### 2.2 Sheaf Theory and Consistency Checking

**What it offers**: Sheaf theory provides the mathematical language for detecting exactly what Pask mesh fitting needs — obstructions to gluing local fragments into a global whole. A cellular sheaf on the corpus graph assigns data spaces to nodes and restriction maps to edges. Sheaf cohomology (H¹) measures the failure of local consistency to yield global consistency. The Sheaf Laplacian provides a continuous consistency measure: its eigenvector structure reveals the "grain" of consistency in the corpus.

**Applied implementations**: Knowledge Sheaves (Gebhart, 2023) directly frames KG embedding as sheaf learning, incorporating the Sheaf Laplacian into the embedding loss. Sheaf Neural Networks (Hansen et al.) generalize GNNs with sheaf structure, computing cohomology during message passing. Opinion Dynamics on Discourse Sheaves (Hansen & Ghrist) models competing narrative constraints — directly relevant when the corpus contains internal tensions.

**The four discrepancies through sheaves**: Novel-coherent → H¹ = 0, section extends. Contradictory → local conflict, high Laplacian at specific edges. Type-spoofing → restriction map violations, cohomology in the type layer. Domain-foreign → disjoint component, no sections exist.

**Limitations**: Computational complexity (O(n³) for n nodes) limits direct application to large meshes. Approximate methods — the Sheaf Laplacian as a consistency proxy rather than full cohomology computation — are necessary for practical corpus sizes. Tool maturity is limited: few off-the-shelf implementations exist for knowledge graphs specifically.

**Key references**: Gebhart (2023), Knowledge Sheaves; Hansen & Ghrist, spectral theory of cellular sheaves and the gentle introduction to graph sheaves; Robinson (2014), Topological Signal Processing and its application to data fusion.

### 2.3 LLM-Based Knowledge Graph Extraction

**What it offers**: The field has reached production maturity. Schema-guided systems (KARMA, Neo4j's LLM Knowledge Graph Builder) achieve 85-90% precision for entity and relation extraction when operating within a fixed ontology. Schema-free systems (Ontogenia, AutoSchemaKG) can discover relation types dynamically, which is relevant when the corpus contains novel conceptual territory.

**Quality and reliability**: Best-case precision around 89.7%; realistic range 75-85%. Relation extraction is harder than entity extraction. Common relation types extract more reliably than rare ones. Multi-run extraction with ensemble voting improves reliability at the cost of compute.

**Adversarial robustness**: This is the critical weakness. The KGPA framework (2024) demonstrates that knowledge graphs can be poisoned via prompt injection. Adversarially crafted documents can manipulate the extraction process to produce fragments that embed cleanly but encode false relations. Worse, models with stronger reasoning capabilities are *more* sensitive to KG poisoning — the same capability that makes them good extractors makes them susceptible to manipulation.

**Mitigation**: Multi-run extraction (the fan) is the primary defense. Documents that produce high extraction variance under adversarial conditions are flagged. Post-extraction validation against the corpus mesh catches fragments that pass extraction but fail structural consistency. The two-layer defense (extraction robustness + structural fitting) is stronger than either alone.

**Key references**: Neo4j LLM Knowledge Graph Builder (2025); Ontogenia (metacognitive prompting); KGPA (adversarial robustness, 2024); LLM4RGNN (KDD 2025, LLM-based graph purification).

### 2.4 Topological Data Analysis

**What it offers**: Persistent homology computes the "shape" of a graph fragment across multiple scales. Represent the fragment as a simplicial complex; track topological features (connected components, cycles, voids) as a threshold parameter varies. Features that persist across scales are structural; those that appear and vanish are noise. The persistence diagram is a compact signature of the fragment's shape.

**Relevance**: Comparing persistence diagrams of new fragments against the corpus mesh's persistence signature provides a scale-free, embedding-independent structural comparison. Novel-coherent fragments should have persistence diagrams similar in shape but extended (new persistent features). Contradictory fragments show features that conflict with the corpus signature. Type-spoofing fragments may have similar persistence at coarse scales but diverge at fine scales (where the edge-type distortion becomes visible).

**Limitations**: Computational cost (O(n³) worst case, though optimized implementations like GUDHI and Ripser are much faster in practice). The threshold selection for building simplicial complexes from knowledge graphs is somewhat arbitrary. Integration with LLM confidence scores is not natural.

**Key references**: Dist2Cycle (simplicial neural networks for homology localization); topological deep learning survey (2025); GUDHI library for practical computation.

### 2.5 Graph Matching and Subgraph Embedding

**What it offers**: The "does this fragment embed into the corpus mesh?" question is a typed subgraph matching problem. Neural approaches (NeuroMatch, HFrame) achieve 100× speedup over classical algorithms with high accuracy. HFrame (2024-2025) specifically handles subgraph homomorphism (allowing some flexibility in the matching), achieving 101× speedup with 0.962 accuracy.

**Type preservation**: Standard implementations treat edges as untyped or uniformly typed. For Pask mesh fitting, typed subgraph matching is essential — the embedding must respect both node types and edge types. This requires extending existing tools with type constraint layers, or using a two-phase approach: find candidate node matchings respecting types, then verify edge type compatibility.

**Limitations**: Subgraph matching is NP-complete in worst case; even neural approaches have practical limits around 500K-node target graphs. The corpus mesh may grow beyond this threshold for large corpora, requiring hierarchical or approximate matching strategies.

**Key references**: NeuroMatch (Stanford, GNN-based subgraph matching); HFrame (2024-2025, hybrid algorithmic+ML subgraph homomorphism); VF3 (classical backtracking with pruning).

### 2.6 Adjacent Frameworks

**Relational Message Passing (RelGNN, 2025)**: Composite message passing that respects relation types during graph neural network learning. Directly applicable to learning typed embeddings of both corpus mesh and fragments.

**Hypergraph Neural Networks**: The typed hypergraph representation of Pask meshes is naturally handled by hypergraph neural networks. Petri Graph Neural Networks (PGNN, 2025) support multimodal flow and nested relations. The emerging Hypergraph Interchange Format (HIF) provides a standard for cross-tool compatibility.

**Ologs (Ontology Logs)**: A category-theoretic approach to knowledge representation where every olog is a category, objects are concept types, and morphisms are relations. Commutative diagrams enforce consistency constraints. Functors between ologs enable data migration and schema integration. Connects directly to the palgebra formalism and to sheaf theory.

---

## 3. Execution Plan

### Phase 0: Conceptual Validation (2-3 weeks)

**Goal**: Test whether LLM mesh extraction produces fragments with enough structural fidelity to support relational comparison.

**Steps**:

1. Select 5-10 documents from a domain where the entailment structure is well-understood (e.g., introductory logic, basic physics, or a well-mapped subdomain within cyberneutics itself).
2. Design an extraction prompt with a fixed ontology scaffold: 6 relation types (prerequisite, entailment, analogy, opposition, instantiation, exemplification), concept node extraction with type labels.
3. Run extraction K=5 times per document. Inspect the fragments manually. Assess: do the fragments capture the document's actual relational structure? Where do they fail?
4. Aggregate the 5 fragments per document into a document mesh using weighted union. Assess: does aggregation improve over individual runs?
5. Write one deliberately type-spoofing document (familiar vocabulary, wrong relational structure). Extract its fragment and compare visually to the corpus fragments.

**Deliverable**: A qualitative assessment of extraction fidelity and a judgment on whether the approach is viable enough to warrant Phase 1.

**Tools**: Any frontier LLM for extraction; NetworkX or igraph for graph representation; manual inspection.

### Phase 1: Prototype Fitting Engine (4-6 weeks)

**Goal**: Build a working prototype that can ingest a small corpus, construct a corpus mesh, and evaluate new documents against it, producing discrepancy classifications.

**Steps**:

1. **Corpus mesh construction**: Implement the aggregation pipeline — K-run extraction, document mesh aggregation, corpus-level aggregation with entity resolution. Use embedding similarity (sentence-transformers) for entity resolution between documents.
2. **Node embedding (Step 1 of fitting)**: Implement candidate matching using cosine similarity on node embeddings. Threshold tuning: how close must a node be to count as "mapped"?
3. **Relational consistency (Step 2)**: Implement edge-type checking between matched nodes. Start with exact match (does the corpus have this edge type between these nodes?), then extend to path-based checking (does a compatible path exist?).
4. **Discrepancy classification**: Implement the four-way classifier based on the signature definitions in Section 1.4. Test against known examples: genuine corpus documents (should score as consistent), novel-coherent documents (from an adjacent field), contradictory documents (manually constructed), type-spoofing documents (manually constructed).
5. **Variance analysis**: Implement the K-run variance signal. Does high extraction variance correlate with engineered text?

**Deliverable**: A Python prototype (likely using NetworkX, sentence-transformers, and a frontier LLM API) that can process a corpus of ~50 documents and evaluate new documents against it, with discrepancy classification and confidence scores.

**Tools**: Python; NetworkX or igraph; sentence-transformers for embeddings; LLM API for extraction; pytest for validation.

### Phase 2: Sheaf-Theoretic Enhancement (4-6 weeks)

**Goal**: Replace the ad-hoc relational consistency check from Phase 1 with the sheaf-theoretic formulation, gaining rigorous obstruction detection.

**Steps**:

1. **Sheaf construction**: Define the cellular sheaf F on the corpus graph. Each node's data space is the concept's local semantic context (a vector); each edge's restriction map encodes the relational constraint (a linear map between endpoint data spaces that the relation type imposes).
2. **Sheaf Laplacian computation**: Implement the Sheaf Laplacian L_F for the corpus mesh. This is a block matrix where blocks correspond to restriction maps. Use sparse matrix libraries for scalability.
3. **Consistency scoring**: For a new fragment, compute x^T L_F x where x encodes the fragment's data assignments in the corpus sheaf's coordinate system. This replaces the edge-type checking from Phase 1 with a continuous, geometrically grounded consistency measure.
4. **Type-spoof detection via mismatch analysis**: Implement the mismatch vector computation and the correlation analysis that distinguishes isolated contradiction from distributed type-spoofing.
5. **Validation**: Compare discrepancy classifications from Phase 1 (ad-hoc) and Phase 2 (sheaf-based). The sheaf-based approach should catch cases that ad-hoc checking misses, particularly subtle type-spoofing.

**Deliverable**: An enhanced prototype with sheaf-based consistency scoring, validated against the Phase 1 baseline.

**Tools**: NumPy/SciPy for sparse linear algebra; the Knowledge Sheaves framework (Gebhart) as reference implementation; custom sheaf construction code.

### Phase 3: Scale and Integration (6-8 weeks)

**Goal**: Scale to a realistic corpus, integrate with the cyberneutics bath model, and formalize in palgebra.

**Steps**:

1. **Scalability**: Test on a corpus of 500+ documents. Identify computational bottlenecks. Implement approximate sheaf consistency (Laplacian eigenvalue bounds rather than full cohomology) if needed.
2. **RDF integration**: Connect the mesh representation to the bath's existing RDF judgment graph. A discrepancy classification becomes a judgment node in the bath, with typed pointers to the specific structural discrepancies detected.
3. **Palgebra formalization**: Write the resource equations for the full pipeline (see Appendix). Verify that the three propagation rules hold. Generate string diagrams.
4. **Adversarial testing**: Construct a suite of adversarial documents (type-spoofing, Crock-style mesh rewiring) and test detection rates. Measure false positive and false negative rates.
5. **Integration with `/committee`**: Design a committee character specifically tasked with structural mesh evaluation — a character whose propensity is to trace entailment chains and probe seam regions.

**Deliverable**: A production-capable system integrated with the cyberneutics bath model and formalized in palgebra.

---

## 4. Evaluation Rubric

The following rubric evaluates any implementation attempt against five criteria, scored 0-3 per criterion. The criteria are designed to be orthogonal — good performance on one does not guarantee performance on others.

### Criterion 1: Extraction Fidelity (0-3)

*Does the mesh extraction step capture the document's actual relational structure?*

- **0**: Extraction produces fragments with no recognizable correspondence to the document's conceptual architecture. Relation types are random or incoherent.
- **1**: Extraction captures some correct concept nodes but relation types are frequently wrong or missing. Manual inspection reveals that fewer than half of extracted edges correspond to actual relations in the document.
- **2**: Extraction captures the dominant relational structure. Most concept nodes and the majority of edge types are correct. Some peripheral or subtle relations are missed. Multi-run aggregation improves reliability.
- **3**: Extraction reliably captures both dominant and secondary relational structures. Edge types are accurate. Extraction variance across runs is interpretable (low variance = tightly constrained document; high variance = genuinely ambiguous). The extraction prompt and ontology scaffold are well-calibrated to the domain.

### Criterion 2: Discrepancy Discrimination (0-3)

*Can the system reliably distinguish the four discrepancy types?*

- **0**: The system cannot distinguish discrepancy types. All non-embedding fragments receive the same classification or a random one.
- **1**: The system can distinguish domain-foreign (no embedding at all) from the other three, but conflates novel-coherent, contradictory, and type-spoofing.
- **2**: The system can distinguish three of four types. Typically, novel-coherent and domain-foreign are correctly classified, and either contradictory or type-spoofing is reliably detected, but not both.
- **3**: All four types are reliably distinguished. Novel-coherent fragments are correctly identified as extending the mesh. Contradictory fragments are flagged with the specific conflicting edges identified. Type-spoofing is detected via the distributed mismatch pattern. Domain-foreign fragments are identified as out-of-scope.

### Criterion 3: Adversarial Robustness (0-3)

*Does the system detect type-spoofing and resist adversarial manipulation?*

- **0**: The system is trivially fooled by type-spoofing documents. Familiar vocabulary causes clean embedding regardless of relational distortion.
- **1**: The system detects obvious type-spoofing (where relational distortion is crude and widespread) but misses subtle cases where only a few edges are rewired.
- **2**: The system detects type-spoofing with moderate rewiring (10-30% of edges distorted). It correctly identifies the seam region between inherited and rewired mesh. Extraction variance serves as a complementary signal.
- **3**: The system detects subtle type-spoofing (< 10% of edges rewired). The correlation structure of mismatches is used to distinguish deliberate distortion from extraction noise. The system explicitly identifies the seam — the boundary between rewired and inherited mesh — and rates its confidence in the identification.

### Criterion 4: Computational Tractability (0-3)

*Can the system operate at a practical corpus scale with acceptable latency?*

- **0**: The system is computationally intractable beyond toy examples (< 10 documents).
- **1**: The system handles small corpora (50-100 documents) but fitting latency is minutes per document, making interactive use impractical.
- **2**: The system handles moderate corpora (100-500 documents) with fitting latency under 30 seconds per document. Corpus mesh construction is batch-processable overnight.
- **3**: The system handles large corpora (500+ documents) with fitting latency under 5 seconds. Incremental corpus mesh updates (adding a newly admitted document) complete in under a minute. The system identifies and uses approximations (Laplacian eigenvalue bounds, hierarchical matching) where exact computation is too expensive, with explicit approximation quality bounds.

### Criterion 5: Auditability (0-3)

*Can a human inspector understand why a document was flagged and trace the reasoning?*

- **0**: The system produces a binary flag (consistent/inconsistent) with no explanation.
- **1**: The system produces a discrepancy classification with a numeric score but no structural detail. A human can see that the document was flagged as type-spoofing but cannot see which edges were distorted or why.
- **2**: The system identifies the specific concept nodes and edges involved in the discrepancy. A human can inspect the mismatch and evaluate whether the system's classification is correct. The judgment is auditable.
- **3**: The system produces a full discrepancy report with: (a) the specific structural discrepancies, (b) the corpus edges they conflict with, (c) the confidence in the classification, (d) the extraction variance signal, and (e) a natural-language summary suitable for a non-specialist reviewer. The report is a decorated text with provenance metadata pointing to specific structural evidence. It functions as a judgment node in the bath.

### Scoring

| Band | Score range | Interpretation |
|------|-------------|----------------|
| **High** | 12-15 | System is production-viable for corpus-scale deployment |
| **Medium** | 8-11 | System demonstrates the approach's viability with known limitations |
| **Low** | 4-7 | Proof of concept only; significant gaps remain |
| **Insufficient** | 0-3 | Approach does not work as designed |

Note: a score of 0 on Criterion 3 (adversarial robustness) should cap the overall assessment at Low regardless of other scores, since type-spoof detection is the system's primary raison d'être.

---

## Appendix: Palgebra Formalization

### Resource equations for the full pipeline

```
# ══════════════════════════════════════════════════════════════════
# PASK MESH FITTING PIPELINE
# ══════════════════════════════════════════════════════════════════

# ── Extraction (fan applied to reading) ─────────────────────────
# A document is read K times by LLM reader agents, each producing
# a typed hypergraph fragment. The ontology scaffold is catalytic.

document × ontology-scaffold → mesh-fragment-set  [ExtractMeshes]
  {catalytic: ontology-scaffold; fan: K}

# ── Document mesh aggregation ───────────────────────────────────
# The K fragments are aggregated into a single document mesh via
# weighted union. This is an enrichment: the document gains
# structured semantic metadata without the text changing.

mesh-fragment-set → document-mesh  [AggregateFragments]
  {enriches: semantic-metadata}

# ── Corpus mesh construction (incremental) ──────────────────────
# Document meshes from admitted documents are merged into the
# corpus mesh via entity resolution and edge accumulation.

document-mesh × corpus-mesh → corpus-mesh  [MergeIntoCorpus]
  {catalytic: corpus-mesh → corpus-mesh; feedback: corpus-mesh}

# ── Fitting: new document evaluation ────────────────────────────
# A bath document undergoes the same extraction pipeline, then
# its fragment is fitted against the corpus mesh.

bath-document × ontology-scaffold → bath-mesh-fragment-set  [ExtractMeshes]
  {catalytic: ontology-scaffold; fan: K}

bath-mesh-fragment-set → bath-document-mesh  [AggregateFragments]
  {enriches: semantic-metadata}

# ── Node embedding (Step 1) ─────────────────────────────────────
bath-document-mesh × corpus-mesh → candidate-matching  [MatchNodes]
  {catalytic: corpus-mesh}

# ── Relational consistency (Step 2) ─────────────────────────────
candidate-matching × corpus-mesh × corpus-sheaf → consistency-report  [CheckConsistency]
  {catalytic: corpus-mesh, corpus-sheaf}

# ── Inferential path verification (Step 3) ──────────────────────
candidate-matching × corpus-mesh → path-report  [VerifyPaths]
  {catalytic: corpus-mesh}

# ── Discrepancy classification ──────────────────────────────────
consistency-report × path-report × extraction-variance → discrepancy-judgment  [Classify]

# ── Judgment emission ───────────────────────────────────────────
# The discrepancy judgment becomes a judgment node in the bath,
# pointing to the bath document and carrying structural evidence.

discrepancy-judgment × bath-document → bath-judgment-node  [EmitJudgment]
  {enriches: bath-document with cy:hasJudgment pointer}
```

### Decorated text structure for a discrepancy judgment

```yaml
---
type:
  template: discrepancy-judgment-v1
  rubric: mesh-fitting-rubric-v1
classification: type-spoof  # or: novel-coherent, contradictory, domain-foreign
scores:
  node-embedding-quality: 0.92
  relational-consistency: 0.31
  path-verification: 0.28
  extraction-variance: 0.67
  overall-confidence: Medium
discrepancy-detail:
  mismatched-edges: 12
  total-edges: 34
  mismatch-concentration: 0.85  # fraction in largest connected component
  seam-region: [concept-A, concept-B, concept-C, concept-D]
  dominant-type-shift: "opposition → entailment"
provenance:
  extracted-by: ExtractMeshes
  aggregated-by: AggregateFragments
  matched-by: MatchNodes
  consistency-by: CheckConsistency
  classified-by: Classify
  corpus-version: 2026-02-24
  extraction-runs: 5
  ontology-scaffold: entailment-scaffold-v2
---

## Discrepancy Report

Document [bath-doc-0042] exhibits the type-spoof signature: vocabulary
maps cleanly to corpus nodes (node embedding quality 0.92) but relational
structure is systematically distorted (relational consistency 0.31).
Twelve of 34 extracted edges carry incorrect relation types, concentrated
in a connected subregion touching concepts A through D. The dominant
type shift is from "opposition" (corpus) to "entailment" (document) —
the document presents as agreement what the corpus records as conflict.

Extraction variance across 5 runs is elevated (0.67), consistent with
engineered text where surface coherence masks structural distortion.
```

### Propagation rules verification

The three palgebra propagation rules hold for this pipeline:

1. **Confidence can only degrade**: Extraction confidence (how reliably the LLM produced the fragment) sets the ceiling for all downstream scores. A low-fidelity extraction cannot produce a high-confidence discrepancy judgment, regardless of how sophisticated the fitting operation is.

2. **Provenance can only accumulate**: Each stage stamps the judgment's metadata with its operation name, parameters, and version. The final judgment carries the full chain from extraction through classification.

3. **Content transforms**: The document's text is never modified. The pipeline produces new content (the discrepancy report) that is a transformation of the structural comparison. The document itself gains only enrichment metadata (the `cy:hasJudgment` pointer).

### Connection to the decision monad

The mesh fitting pipeline connects to the fan/funnel duality from `palgebra/duality-and-composition.md` at two levels:

**The extraction fan**: The K-run extraction is structurally identical to the scenario generation fan — one input (document), multiple outputs (fragments), catalytic parameters (ontology scaffold). The aggregation step is the funnel that compresses K fragments into one mesh.

**The corpus as accumulated funnel output**: Each document admission is a micro-funnel — the judgment process (whether automated or human) converges on an admit/reject decision. The corpus mesh is the accumulated residue of all admission funnels. It grows by residuality: the mesh structure that survives repeated document admission is the eigenform of the corpus.

**Fitting as a single-pass funnel**: The fitting operation compresses the comparison between fragment and corpus into a single discrepancy classification. It is a judgment funnel: multiple structural signals (node embedding, relational consistency, path verification, variance) converge into one decorated judgment.

---

*Connections: [Pask Mesh Fitting](pask-mesh-fitting.md) (source material), Essay 09 (Narrative Immune Systems), Essay 11 (Conversation Theory), [Glenda/Crock](../../applications/narrative-immune-systems/glenda-crock-alignment.md) (adversarial application), [Decorated Texts](../../palgebra/decorated-texts.md) (formalism), [Duality and Composition](../../palgebra/duality-and-composition.md) (fan/funnel).*
