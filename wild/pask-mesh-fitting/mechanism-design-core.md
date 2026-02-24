# Pask Mesh Fitting: Mechanism Design and Theoretical Framework

> *Produced for cyberneutics — February 2026. Responds to the design prompt in `agent/prompts/pask-mesh-fitting-design.md`. Status: design document, not yet methodology.*

---

## Contents

1. [Architectural & Theoretical Design](#1-architectural--theoretical-design)
2. [Research Synthesis](#2-research-synthesis)
3. [Evaluation Rubric](#3-evaluation-rubric)
4. [Palgebra Formalization](#appendix-palgebra-formalization)

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

This architectural design synthesizes several distinct fields of mathematical and computational research. The deep-dive analyses for each theoretical pillar can be found in the `research/` directory:

*   **[Knowledge Graph Embeddings](research/knowledge-graph-embeddings.md)**: Using TransE and RotatE for geometric consistency checking.
*   **[Sheaf Theory and Consistency Checking](research/sheaf-theory-consistency.md)**: Using sheaf cohomology and the Sheaf Laplacian to detect topological obstructions.
*   **[LLM-Based Knowledge Graph Extraction](research/llm-kg-extraction.md)**: Evaluating the reliability, schema adherence, and adversarial robustness of the extraction fan.
*   **[Topological Data Analysis](research/topological-data-analysis.md)**: Alternative structural comparison using persistent homology.
*   **[Graph Matching and Subgraph Embedding](research/graph-matching.md)**: Neural approaches to typed subgraph homomorphism.
*   **[Adjacent Frameworks](research/adjacent-frameworks.md)**: Relational Message Passing, Hypergraph Neural Networks, and Ologs.

---

## 3. Evaluation Rubric

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
