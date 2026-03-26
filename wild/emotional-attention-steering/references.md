# References: Emotion Blend Taxonomies and Formal Models

Collected references for the emotional attention steering thread. Covers Plutchik's primary sources, algebraic and computational formalizations, 6sec practitioner material, and upstream theory connections.

---

## Plutchik (primary sources)

- **Plutchik, R. (1962).** *The Emotions: Facts, Theories, and a New Model*. Random House.

- **Plutchik, R. (1980).** *Emotion: A Psychoevolutionary Synthesis*. Harper & Row. — The original wheel model. Eight basic emotions as four opposed pairs (Joy/Sadness, Fear/Anger, Anticipation/Surprise, Disgust/Trust). Dyads graded by cyclic distance: primary (adjacent), secondary (2 apart), tertiary (3 apart). Opposites annihilate. Intensity varies along a radial axis (e.g., annoyance → anger → rage). The color-wheel analogy is deliberate: emotions shade into each other along a spectrum and can be mixed.

- **Plutchik, R. (2001).** "The Nature of Emotions: Human emotions have deep evolutionary roots." *American Scientist*, 89(4), 344–350. — Most cited accessible summary.

- **Plutchik, R. (2003).** *Emotions and Life: Perspectives from Psychology, Biology, and Evolution*.

---

## Algebraic / computational formalizations of Plutchik

- **Tayari Meftah, I., Le Thanh, N., & Ben Amar, C. (2010).** "Towards an algebraic modeling of emotional states." *ICIW 2010*, pp. 513–518. — Formalizes Plutchik as 8-dimensional vector space; each basic emotion is a basis vector in ℝ⁸; blends are vector sums; uses projection and decomposition for analysis. Part of the Emotica project.

- **Tayari Meftah, I., Le Thanh, N., & Ben Amar, C. (2011).** "Sharing Emotional Information Using A Three Layer Model." *ICIW 2011*. — Three-layer model: psychological layer (Plutchik), formal computational layer (algebraic vectors), language layer (XML exchange). Vector addition for multimodal emotion fusion.

- **Semeraro, A., Vilella, S., & Ruffo, G. (2021).** "PyPlutchik: Visualising and comparing emotion-annotated corpora." *PLoS ONE*, 16(9), e0256503. PMC8409663. — Python library for Plutchik-annotated corpus visualization. Displays primary, secondary, tertiary, and opposite dyads. Useful as a reference implementation for the annotation vocabulary.

---

## Computational emotion classification using Plutchik

- **Li, J. et al. (2024).** "Integrating Plutchik's Theory with Mixture of Experts for Enhancing Emotion Classification." *EMNLP 2024*. — Uses Plutchik's dyad structure to relabel training data (GoEmotions, SemEval-2018), improving MoE-based emotion classifiers. Demonstrates that the dyad algebra is computationally useful for NLP, not just theoretical.

---

## 6seconds / EQ practice

- **Six Seconds (6seconds.org)** — Global nonprofit founded 1997, largest organization dedicated to emotional intelligence. Publishes SEI (Six Seconds Emotional Intelligence) assessment, used by 1M+ people. Annual *State of the Heart* report tracks global EQ trends. The emotion blend chart in this directory is their popularized adaptation of Plutchik, simplified from 8 to 5 base emotions (Joy, Sadness, Disgust, Fear, Anger) with a 5×5 symmetric blend matrix.

- Six Seconds' research is practitioner-oriented (training, certification, organizational consulting), not formal or computational. Useful as a source of curated emotion vocabularies but not for algebraic structure.

---

## Algebraic observations (original to this project, informal)

- The 6sec chart is a symmetric bilinear form on a 5-element set. Not closed (products not in generating set), so not even a magma. Self-products are intensifications (ecstasy, despair, abhorrence, terror, rage). The chart is structurally similar to the furry logic problem: each blend genuinely inhabits both parent types simultaneously, not a graded mixture.

- Plutchik's wheel has more structure: 8 generators on a cyclic group, Z₂ involution (opposition), dyad distance grading (primary/secondary/tertiary), intensity rays, and annihilation of opposites. The skeleton is approximately Z₂ × Z₈. Still not closed — the 24 dyads don't recombine — but the grading gives a way to specify how "far" a committee member's emotional blend should reach.

---

## Houston Four Levels (upstream theory)

- **Houston, J.** — Four Levels model of apprehending reality (sensory, psychological, mythic, spiritual). See `wild/diary/2026-03-15-mystic-narrative.md`. Emotions as Type 1 (System 1) conditioners of narrative formation. Committee member propensities as stable configurations of these levels.

---

## Cyberneutics connection to furry logic

- Emotion blends as soft-typed texts: "dread" (Sadness × Fear) fully inhabits both parent types, not partially. This is the furry logic situation. Cross-reference `wild/fuzzy-type-theory/`.
