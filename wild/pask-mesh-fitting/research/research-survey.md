# Pask Mesh Fitting: Research Survey

This document consolidates the six independent research notes on mathematical and computational frameworks that underpin Pask Mesh Fitting — the mechanism by which an unprovenanced document fragment is structurally evaluated against a trusted corpus mesh to detect contradiction and "type-spoofing" (disinformation). For tractability analysis and validation experiments, see [tractability-and-risks.md](tractability-and-risks.md).

---

## Knowledge Graph Embeddings

KGE methods (TransE, RotatE, ConvE and successors) represent entities as vectors and relations as geometric transformations in embedding space. The corpus mesh defines a geometry; a new fragment's embedding compatibility is measured as geometric distance plus directional consistency. Type-augmented variants (TaKE, TransR, HCCE) explicitly incorporate entity and relation type information, preventing type confusion in the embedding.

Standard KGE optimizes for link prediction (does this edge exist?) rather than type-consistency (is this edge of the right type?). The type-spoof signature — nodes embed well, edges don't — is a gap in existing methods. KGE provides a fast, scalable node-embedding layer for initial fragment matching, but for deeper relational consistency checking it alone is insufficient.

Key references: TP-RotatE (2025, path-aware rotation embeddings); TaKE (type-augmented framework, Nature Scientific Reports 2023); SparseTransX (2025, 5× speedup enabling larger meshes).

## Sheaf Theory and Consistency Checking

Sheaf theory provides the mathematical language for detecting obstructions to gluing local fragments into a global whole. A cellular sheaf on the corpus graph assigns data spaces to nodes and restriction maps to edges. Sheaf cohomology (H¹) measures the failure of local consistency to yield global consistency. The Sheaf Laplacian provides a continuous consistency measure: its eigenvector structure reveals the "grain" of consistency in the corpus.

The four discrepancies through sheaves: novel-coherent → H¹ = 0, section extends; contradictory → local conflict, high Laplacian at specific edges; type-spoofing → restriction map violations, cohomology in the type layer; domain-foreign → disjoint component, no sections exist.

Computational complexity (O(n³) for n nodes) limits direct application to large meshes. Few off-the-shelf implementations exist for knowledge graphs specifically.

Key references: Gebhart (2023), Knowledge Sheaves; Hansen & Ghrist, spectral theory of cellular sheaves; Robinson (2014), Topological Signal Processing.

## LLM-Based Knowledge Graph Extraction

The field has reached production maturity. Schema-guided systems achieve 85–90% precision for entity and relation extraction within a fixed ontology. Schema-free systems can discover relation types dynamically.

Adversarial robustness is the critical weakness. The KGPA framework (2024) demonstrates that knowledge graphs can be poisoned via prompt injection. Models with stronger reasoning capabilities are *more* sensitive to KG poisoning. Multi-run extraction (the fan) is the primary defense: documents that produce high extraction variance under adversarial conditions are flagged. The two-layer defense (extraction robustness + structural fitting) is stronger than either alone.

Key references: Neo4j LLM Knowledge Graph Builder (2025); Ontogenia (metacognitive prompting); KGPA (adversarial robustness, 2024); LLM4RGNN (KDD 2025).

## Topological Data Analysis

Persistent homology computes the "shape" of a graph fragment across multiple scales. Features that persist across scales are structural; those that appear and vanish are noise. The persistence diagram is a compact signature of the fragment's shape.

Comparing persistence diagrams of new fragments against the corpus mesh's persistence signature provides a scale-free, embedding-independent structural comparison. Type-spoofing fragments may have similar persistence at coarse scales but diverge at fine scales where edge-type distortion becomes visible. Computational cost is O(n³) worst case, though optimized implementations (GUDHI, Ripser) are faster in practice.

Key references: Dist2Cycle (simplicial neural networks for homology localization); topological deep learning survey (2025); GUDHI library.

## Graph Matching and Subgraph Embedding

The "does this fragment embed into the corpus mesh?" question is a typed subgraph matching problem. Neural approaches (NeuroMatch, HFrame) achieve 100× speedup over classical algorithms. HFrame (2024–2025) handles subgraph homomorphism with 0.962 accuracy.

For Pask mesh fitting, typed subgraph matching is essential — the embedding must respect both node types and edge types. Subgraph matching is NP-complete in worst case; even neural approaches have practical limits around 500K-node target graphs.

Key references: NeuroMatch (Stanford, GNN-based); HFrame (2024–2025, hybrid); VF3 (classical backtracking).

## Algebra, Statistics, and Quantum Probability

Based on Tai-Danae Bradley's 2020 thesis *"At the Interface of Algebra and Statistics"*, this framework models hierarchical relationships using quantum probability. Joint probability distributions are represented as rank-one density operators; marginalizing via quantum partial trace recovers formal concepts (Galois connections) from pure statistics.

Relevance to Pask Mesh Fitting: if the corpus is modeled as a density operator, entailment becomes a geometric consequence. Type-spoofing documents would have correct diagonal elements (classical statistics match) but wrong off-diagonal elements (relational structure diverges). Quantum relative entropy between fragment and corpus density matrices could serve as a sensitive type-spoof detector.

Limitation: tensor product spaces scale exponentially with sequence length, requiring approximation (Matrix Product States, Tensor Networks).

Key references: Bradley (2020), *At the Interface of Algebra and Statistics* (PhD Thesis); Formal Concept Analysis (Ganter & Wille).

## Adjacent Frameworks

Three complementary approaches: Relational Message Passing (RelGNN, 2025) — composite message passing respecting relation types during GNN learning; Hypergraph Neural Networks (PGNN, 2025) — supporting multimodal flow and nested relations via the Hypergraph Interchange Format; Ologs (category-theoretic knowledge representation) — commutative diagrams enforce consistency constraints, functors enable schema integration, connecting to palgebra formalism and sheaf theory.
