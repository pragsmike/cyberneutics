# LLM-Based Knowledge Graph Extraction

**What it offers**: The field has reached production maturity. Schema-guided systems (KARMA, Neo4j's LLM Knowledge Graph Builder) achieve 85-90% precision for entity and relation extraction when operating within a fixed ontology. Schema-free systems (Ontogenia, AutoSchemaKG) can discover relation types dynamically, which is relevant when the corpus contains novel conceptual territory.

**Quality and reliability**: Best-case precision around 89.7%; realistic range 75-85%. Relation extraction is harder than entity extraction. Common relation types extract more reliably than rare ones. Multi-run extraction with ensemble voting improves reliability at the cost of compute.

**Adversarial robustness**: This is the critical weakness. The KGPA framework (2024) demonstrates that knowledge graphs can be poisoned via prompt injection. Adversarially crafted documents can manipulate the extraction process to produce fragments that embed cleanly but encode false relations. Worse, models with stronger reasoning capabilities are *more* sensitive to KG poisoning — the same capability that makes them good extractors makes them susceptible to manipulation.

**Mitigation**: Multi-run extraction (the fan) is the primary defense. Documents that produce high extraction variance under adversarial conditions are flagged. Post-extraction validation against the corpus mesh catches fragments that pass extraction but fail structural consistency. The two-layer defense (extraction robustness + structural fitting) is stronger than either alone.

**Key references**: Neo4j LLM Knowledge Graph Builder (2025); Ontogenia (metacognitive prompting); KGPA (adversarial robustness, 2024); LLM4RGNN (KDD 2025, LLM-based graph purification).
