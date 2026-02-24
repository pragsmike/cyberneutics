# Research: LLM Knowledge Graph Extraction Reliability and Variance

## Core Concepts
Using Large Language Models to extract structured knowledge graphs (ontologies) from unstructured text is a rapidly developing field. It is the "fan" operation in the Pask Mesh fitting framework.

## Reliability and Consistency
- **Human-like Performance:** Advanced LLMs (like GPT-4, Claude 3 Opus) demonstrate ontology extraction accuracy comparable to human evaluators for defined tasks.
- **The "Relations" Problem:** LLMs are generally excellent at identifying entities (classes/individuals) but struggle significantly more with extracting the correct *properties* (relations) between them. They may introduce inconsistent properties or hallucinate relations not present in the text.
- **Prompt Engineering:** Complex "Chain-of-Thought" prompting is sometimes counter-productive for exact extraction, which is fundamentally a pattern recognition task. Ontology-guided prompting (providing the LLM with a schema of allowed edge types) significantly reduces variance and maintains semantic consistency.

## Managing Variance
- **Hallucinations vs. Variance:** Hallucinations involve inventing facts. Variance involves two different LLMs (or two runs) structuring the exact same text differently.
- **Schema Constraints:** Consistency dramatically improves when the LLM is constrained to a specific schema.
- **Interactive/Iterative Refinement:** Production systems use iterative approaches, asking the LLM to cross-check its own generated triples against the source text.

## Application to Pask Mesh Fitting
For the Clojure implementation, treating the LLM invocation as a single, infallible function `(extract-graph text)` is a category error.

Instead, the mechanism must:
1. **Use Strict Schemas:** The prompt must constrain the LLM to a predefined set of relation types (e.g., `entails`, `opposes`, `is-analogous-to`).
2. **Exploit Concurrency:** Use Clojure's `core.async` to run $N$ independent extractions of the same document concurrently (temperature > 0).
3. **Calculate Distribution:** Aggregate the results. If an edge `(A, entails, B)` appears in 8 out of 10 runs, it gets a high confidence weight. If an edge appears in only 1 run, it is likely an LLM hallucination and is pruned. This turns LLM variance into a measurable confidence interval.
