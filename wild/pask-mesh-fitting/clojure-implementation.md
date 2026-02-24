# Pask Mesh Fitting: Clojure Implementation

> *This document is an execution plan. It requires the theoretical architectural design described in [mechanism-design-core.md](mechanism-design-core.md).*

Based on the prompt requirements (`agent/prompts/pask-mesh-fitting-design.md`) and research into computational tractability, this document outlines the mechanism design and architectural plan for implementing the Pask Mesh Fitting workflow organically in **Clojure**.

## 1. Architectural Mechanisms

The system relies on Clojure's strengths: immutable data structures, concurrent processing (`core.async`), and relational logic (`core.logic` / Datalog).

### The Corpus Mesh (The Coproduct Aggregation)
The corpus mesh is not a static object but an accumulating state. In Clojure, this is best modeled using a Datalog-based graph database like **DataScript** (in-memory) or **XTDB** (persisted, bitemporal). 
- **Structure:** The mesh is a set of Datalog facts: `[entity attribute value confidence]`.
- **Graded Relations:** Because Pask meshes are fuzzy, every edge `(A, relation, B)` has a `confidence` weight and a `variance` metric derived from multiple readings.

### The Extraction Funnel (Handling LLM Variance)
An LLM reading a text will produce different hypergraph fragments depending on temperature and framing. We treat this variance not as an error, but as a distribution.
- **Mechanism:** We use `core.async` to fan out $N$ concurrent LLM extraction requests for the same unprovenanced document.
- **Constraints:** To prevent unbounded hallucination, the LLMs are constrained via prompt engineering to a strict schema of allowed relational edge types (e.g., `entails`, `opposes`, `is-instance-of`).
- **Aggregation:** We `reduce` the $N$ fragments. Edges that appear in $>(N/2)$ fragments are kept; their frequency becomes their `confidence` weight. This produces the stable **document fragment**.

---

## 2. The "Fitting" Operation (Discrepancy Detection)

Taking the document fragment and fitting it into the DataScript/XTDB corpus mesh involves three distinct layers of checking.

### Layer 1: Vocabulary Matching (Familiarity)
- **Check:** Do the concept nodes in the fragment exist in the corpus?
- **Implementation:** Simple Datalog queries or nearest-neighbor text embedding search (via an interop library like `clj-djl`).

### Layer 2: Logical Validation (Contradiction)
- **Check:** Does the fragment assert an edge that directly violates a corpus hard rule?
- **Implementation:** Datalog queries. If the corpus contains `[A :opposes B]` with high confidence, and the fragment asserts `[A :entails B]`, this is a direct contradiction.

### Layer 3: Structural/Topological Alignment (Type-Spoofing Detection)
This is the core of the immune system. Type-spoofing means the vocabulary matches (Layer 1 passes) and no hard logical rules are broken (Layer 2 passes), but the *relational geometry* is wrong.
- **Theoretical Approach:** We use **Knowledge Graph Embeddings (Specifically RotatE)**. While Sheaf Theory (cohomological obstructions) is mathematically elegant for this, RotatE is computationally tractable.
- **Implementation:** The corpus is periodically embedded into a complex vector space using RotatE (via Java interop to a deep learning library). 
- **The Metric:** For every edge in the fragment `(h, r, t)`, we retrieve the corpus vectors for $h$ and $t$. We apply the rotation $r$. The distance $||h \circ r - t||$ is the "energy" or discrepancy score. If this distance is high, it means the fragment is connecting familiar concepts in a way that violates the structural geometry of the trusted corpus. This is a **Type-Spoof**.

---

## 3. Implementation Plan (Phased Execution)

**Phase 1: Substrate and Extraction**
- Initialize a DataScript store.
- Write the schema for nodes, edges, and confidence metadata.
- Build the `core.async` extraction pipeline that takes a text, fans out to an LLM API, parses the JSON responses, and reduces them into a single, weighted Clojure map representing the fragment.

**Phase 2: Aggregation and Hard Queries**
- Implement the "merge" function that adds a validated fragment to the active DataScript corpus.
- Write Datalog queries for Layer 1 (Vocabulary) and Layer 2 (Contradiction) detection.

**Phase 3: Geometric Discriminator**
- Integrate a Java library (e.g., DJL) or use a pure Clojure matrix library (`neanderthal`) to calculate RotatE embeddings for the Datalog corpus.
- Implement the scoring function that calculates the distance metric for a new fragment against the existing vector space.
- Write the reporting function that categorizes the document into the four discrepancy types (Novel, Contradictory, Type-Spoof, Domain-Foreign) based on the combined Layer 1, 2, and 3 thresholds.

---

## 4. Evaluation Rubric for the Mechanism

| Score | Criteria |
|---|---|
| **5 (Exceptional)** | Mechanism provides a mathematically sound, completely computationally tractable method (e.g., KGEs or bounded Sheaf Laplacians) for detecting Type-Spoofing. Clojure implementation leans heavily on core data structures, `core.async` for extraction variance, and Datalog for logical querying. Architecture is robust against LLM hallucinations. |
| **4 (Strong)** | Theory is sound. Implementation plan is solid. Employs concurrent extraction and clear metric scoring, though the integration between the Datalog logical layer and the continuous vector/topological layer might have minor friction points. |
| **3 (Adequate)** | Understands the extraction variance and proposes basic aggregation. Discrepancy detection relies mostly on surface Datalog queries (contradiction) rather than deeper geometric/topological (Type-Spoofing) detection. |
| **2 (Weak)** | Treats LLM extraction as a reliable 1:1 operation without handling variance. Misses the distinction between discrete logic contradictions and continuous structural type-spoofs. Implementation plan is not idiomatic to Clojure. |
| **1 (Failing)** | Misunderstands the fundamental bath/corpus distinction. Proposes using an LLM to simply "evaluate if the document is true" rather than extracting and comparing structural metadata. |
