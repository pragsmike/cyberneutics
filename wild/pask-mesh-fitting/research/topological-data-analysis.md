# Topological Data Analysis

**What it offers**: Persistent homology computes the "shape" of a graph fragment across multiple scales. Represent the fragment as a simplicial complex; track topological features (connected components, cycles, voids) as a threshold parameter varies. Features that persist across scales are structural; those that appear and vanish are noise. The persistence diagram is a compact signature of the fragment's shape.

**Relevance**: Comparing persistence diagrams of new fragments against the corpus mesh's persistence signature provides a scale-free, embedding-independent structural comparison. Novel-coherent fragments should have persistence diagrams similar in shape but extended (new persistent features). Contradictory fragments show features that conflict with the corpus signature. Type-spoofing fragments may have similar persistence at coarse scales but diverge at fine scales (where the edge-type distortion becomes visible).

**Limitations**: Computational cost (O(n³) worst case, though optimized implementations like GUDHI and Ripser are much faster in practice). The threshold selection for building simplicial complexes from knowledge graphs is somewhat arbitrary. Integration with LLM confidence scores is not natural.

**Key references**: Dist2Cycle (simplicial neural networks for homology localization); topological deep learning survey (2025); GUDHI library for practical computation.
