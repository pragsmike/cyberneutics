# Knowledge Graph Embeddings

**What they offer**: KGE methods (TransE, RotatE, ConvE and successors) represent entities as vectors and relations as geometric transformations in embedding space. The corpus mesh defines a geometry; a new fragment's embedding compatibility is measured as geometric distance plus directional consistency. Type-augmented variants (TaKE, TransR, HCCE) explicitly incorporate entity and relation type information, preventing type confusion in the embedding.

**What they miss**: Standard KGE optimizes for link prediction (does this edge exist?) rather than type-consistency (is this edge of the right type?). The type-spoof signature — nodes embed well, edges don't — is a gap in existing methods. Type-preserving embeddings can be post-processed with a type-consistency oracle, but this two-step approach is less elegant than the sheaf formulation.

**Relevance to Pask mesh fitting**: KGE provides a fast, scalable node-embedding layer for initial fragment matching. However, for deeper relational consistency checking, KGE alone is insufficient — it compresses relational information into geometric space, losing the explicit edge typing needed for type-spoof detection.

**Key references**: TP-RotatE (2025, path-aware rotation embeddings); TaKE (type-augmented framework, Nature Scientific Reports 2023); SparseTransX (2025, 5× speedup enabling larger meshes).
