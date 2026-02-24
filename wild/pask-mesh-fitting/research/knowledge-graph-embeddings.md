# Research: Knowledge Graph Embeddings (KGE) and Discrepancy Detection

## Core Concepts
Knowledge Graph Embeddings represent entities (nodes) and relations (edges) as vectors or matrices in a continuous space. 

1. **TransE (Translating Embeddings):**
   - Models relations as translations: $head + relation \approx tail$.
   - **Limitations:** Struggles with symmetric relations (if A is sibling to B, $A + r = B \implies B + r = A$, which implies $r = 0$, heavily distorting the space), and Many-to-1 / 1-to-Many relationships.
   - **Discrepancy context:** If a corpus has a contradictory edge that violates the learned geometry, TransE might just smooth it over or produce a highly sub-optimal embedding, making confident anomaly detection difficult.

2. **RotatE (Relational Rotation in Complex Space):**
   - Represents entities in complex vector space and relations as rotations: $head \circ relation \approx tail$ (Hadamard product).
   - **Strengths:** Can explicitly model symmetry (rotation by $0$ or $\pi$), antisymmetry, inversion, and composition. 
   - **Discrepancy context:** Because it models relationship patterns explicitly, an edge that violates an established pattern (e.g., asserting a symmetric link on an antisymmetric relation) results in a high "energy" or distance score.

## Application to Pask Mesh Fitting
RotatE is a highly pragmatic alternative to the heavy mathematics of Sheaf Theory for detecting structural contradictions (Type-Spoofing or Contradictory discrepancies). 

In the Clojure implementation:
- The corpus mesh can be periodically embedded using a KGE approach.
- When an LLM extracts a fragment, we look up the vector representations of the vocabulary in the corpus.
- We then apply the RotatE function: does $head_{corpus} \circ relation_{fragment} \approx tail_{corpus}$?
- A high distance score indicates a structural contradiction. If the distance is high but the vocabulary vectors exist and are tight, we have identified a **Type-Spoof**.
