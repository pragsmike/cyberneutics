# 2.5 Graph Matching and Subgraph Embedding

**What it offers**: The "does this fragment embed into the corpus mesh?" question is a typed subgraph matching problem. Neural approaches (NeuroMatch, HFrame) achieve 100× speedup over classical algorithms with high accuracy. HFrame (2024-2025) specifically handles subgraph homomorphism (allowing some flexibility in the matching), achieving 101× speedup with 0.962 accuracy.

**Type preservation**: Standard implementations treat edges as untyped or uniformly typed. For Pask mesh fitting, typed subgraph matching is essential — the embedding must respect both node types and edge types. This requires extending existing tools with type constraint layers, or using a two-phase approach: find candidate node matchings respecting types, then verify edge type compatibility.

**Limitations**: Subgraph matching is NP-complete in worst case; even neural approaches have practical limits around 500K-node target graphs. The corpus mesh may grow beyond this threshold for large corpora, requiring hierarchical or approximate matching strategies.

**Key references**: NeuroMatch (Stanford, GNN-based subgraph matching); HFrame (2024-2025, hybrid algorithmic+ML subgraph homomorphism); VF3 (classical backtracking with pruning).
