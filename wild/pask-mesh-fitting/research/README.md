# Pask Mesh Fitting Research

This directory contains six independent treatments of mathematical and computational frameworks. Together, they provide the theoretical foundation for **Pask Mesh Fitting** — the mechanism by which an unprovenanced document fragment is structurally evaluated against a trusted corpus mesh to detect contradiction and "type-spoofing" (disinformation).

While each framework can be studied independently, they interlock to enable the full pipeline: extraction from text, geometric embedding, topological consistency checking, and adversarial robustness.

## Topics

*   **[Knowledge Graph Embeddings](knowledge-graph-embeddings.md)**
    Using continuous vector geometries (like TransE and RotatE) for rapid structural comparison and relational contradiction detection.
    
*   **[Sheaf Theory and Consistency Checking](sheaf-theory-consistency.md)**
    The rigorous mathematical language of local-to-global obstructions. Uses the cellular Sheaf Laplacian to detect topological "type-spoofs" where vocabulary matches but relationship constraints restrict mapping.
    
*   **[LLM-Based Knowledge Graph Extraction](llm-kg-extraction.md)**
    Treating Large Language Models not as infallible readers, but as stochastic extractors. Explores how schema constraint and multi-run variance (the "fan" operation) expose adversarially poisoned graphs.
    
*   **[Topological Data Analysis](topological-data-analysis.md)**
    Using persistent homology to compare the scale-free "shape" of a document fragment against the established shape of the corpus mesh.
    
*   **[Graph Matching and Subgraph Embedding](graph-matching.md)**
    Neural and algorithmic approaches to typed subgraph homomorphism, serving as the computational substrate for "fitting" a fragment into a mesh.
    
*   **[Algebra, Statistics, and Quantum Probability](algebra-and-statistics.md)**
    Based on Tai-Danae Bradley's work linking quantum density operators to Formal Concept Analysis. Provides a framework for modeling logical entailment and detecting type-spoofing via off-diagonal quantum relative entropy.

*   **[Adjacent Frameworks](adjacent-frameworks.md)**
    Related computational avenues, including Relational Message Passing, Hypergraph Neural Networks, and Category-Theoretic Ologs.
