# Task: Create `wild/emotional-attention-steering/` directory and amend diary entry

## Context

The emotional attention steering thread currently lives only in a single diary entry (`wild/diary/2026-03-15-emotional-attention-steering.md`). A conversation on 2026-03-26 identified new material that warrants elevating this to a `wild/` subdirectory with collected references. The conversation also identified a gap: the diary entry's negative decision ("do not attempt a rich emotional ontology") is correct for the PID state variables, but there's a second layer — the diagnostic/scoring vocabulary used by the orchestrator to evaluate transcript emotional tone — that the diary doesn't address. Plutchik's wheel and the 6sec emotion blend chart provide that vocabulary.

The uploaded image `6sec-emotion-blend-chart.png` should be placed in the new directory.

## Files to create

### 1. `wild/emotional-attention-steering/README.md`

Follow the pattern of `wild/fuzzy-type-theory/README.md` — research question, current answer, files list, related files elsewhere, epistemic status.

**Research question:** How should emotional dynamics be modeled in the adversarial committee to steer attention and argument intensity during deliberation? What vocabulary and measurement apparatus is needed to score emotional tone in transcripts?

**Current answer (summarize from existing diary entry + new material):**

- Emotional state modeled as a small set of continuous PID-controlled variables per character (urgency, frustration, confidence, engagement), updated by an external orchestrator between rounds — not simulated by the LLM.
- Negative decisions: don't attempt a rich emotional ontology for the state variables; don't ask a single LLM to simulate emotional dynamics; keep the calibration register mechanism-agnostic.
- The PID state variables are engineering control variables, not emotion labels. But the orchestrator's scoring function — which evaluates the previous round's transcript to compute PID inputs — needs a finer diagnostic vocabulary than the four state dimensions provide.
- Plutchik's wheel of emotions (8 generators, Z₂ opposition, graded dyads by cyclic distance, intensity rays, opposite annihilation) and the 6sec emotion blend chart (5 generators, 25 blends) provide candidate vocabularies for this scoring layer.
- The blend vocabularies also serve as calibration instruments: if a committee member's target emotional operating point is "protective skepticism" but their output reads as "dread," that's a detectable drift.
- This is a long-term design target, not a near-term implementation. Prerequisites: metacognition measurement instrumentation (calibration register) and independent fresh agents.

**Status:** Exploratory — architectural design target. No experiment protocol or implementation yet. Prerequisites not met (metacog instrumentation, independent agents).

**Files in this directory:**

- `README.md` — this file
- `references.md` — collected references on emotion blend taxonomies and formal models
- `6sec-emotion-blend-chart.png` — the chart that prompted this investigation (source: 6seconds.org)

**Related files elsewhere:**

- `wild/diary/2026-03-15-emotional-attention-steering.md` — the originating diary entry; PID architecture, state variables, bricking detection, calibration separation
- `wild/diary/2026-03-15-mystic-narrative.md` — Houston's Four Levels model; emotional and mythic layers as pre-narrative conditioners of sense-making (the theoretical upstream)
- `wild/diary/2026-03-08-cospans-open-games.md` — open games framing; selection functions as the mechanism through which emotional state would modulate strategy choice
- `wild/diary/2026-03-06-metacog-sdt-beer.md` — calibration register design; meta-d'/d' as noise figure
- `wild/committee-games/committee-as-open-game.md` — propensity as constraint on strategy set; emotional state as dynamic modulation of selection function

**Epistemic status:** The PID architecture is a sound engineering design but untested. The emotion blend vocabularies are borrowed from psychology (Plutchik) and EQ practice (6sec) and have not been validated as useful for LLM transcript scoring. The algebraic observations about Plutchik's wheel (Z₂ × Z₈ skeleton, graded dyads) are original to this project and informal.

### 2. `wild/emotional-attention-steering/references.md`

Collect these references with brief annotations:

**Plutchik (primary sources):**
- Plutchik, R. (1962). *The Emotions: Facts, Theories, and a New Model*. Random House.
- Plutchik, R. (1980). *Emotion: A Psychoevolutionary Synthesis*. Harper & Row. — The original wheel model. Eight basic emotions as four opposed pairs (Joy/Sadness, Fear/Anger, Anticipation/Surprise, Disgust/Trust). Dyads graded by cyclic distance: primary (adjacent), secondary (2 apart), tertiary (3 apart). Opposites annihilate. Intensity varies along a radial axis (e.g., annoyance → anger → rage). The color-wheel analogy is deliberate: emotions shade into each other along a spectrum and can be mixed.
- Plutchik, R. (2001). "The Nature of Emotions: Human emotions have deep evolutionary roots." *American Scientist*, 89(4), 344–350. — Most cited accessible summary.
- Plutchik, R. (2003). *Emotions and Life: Perspectives from Psychology, Biology, and Evolution*.

**Algebraic / computational formalizations of Plutchik:**
- Tayari Meftah, I., Le Thanh, N., & Ben Amar, C. (2010). "Towards an algebraic modeling of emotional states." *ICIW 2010*, pp. 513–518. — Formalizes Plutchik as 8-dimensional vector space; each basic emotion is a basis vector in ℝ⁸; blends are vector sums; uses projection and decomposition for analysis. Part of the Emotica project.
- Tayari Meftah, I., Le Thanh, N., & Ben Amar, C. (2011). "Sharing Emotional Information Using A Three Layer Model." *ICIW 2011*. — Three-layer model: psychological layer (Plutchik), formal computational layer (algebraic vectors), language layer (XML exchange). Vector addition for multimodal emotion fusion.
- Semeraro, A., Vilella, S., & Ruffo, G. (2021). "PyPlutchik: Visualising and comparing emotion-annotated corpora." *PLoS ONE*, 16(9), e0256503. PMC8409663. — Python library for Plutchik-annotated corpus visualization. Displays primary, secondary, tertiary, and opposite dyads. Useful as a reference implementation for the annotation vocabulary.

**Computational emotion classification using Plutchik:**
- Li, J. et al. (2024). "Integrating Plutchik's Theory with Mixture of Experts for Enhancing Emotion Classification." *EMNLP 2024*. — Uses Plutchik's dyad structure to relabel training data (GoEmotions, SemEval-2018), improving MoE-based emotion classifiers. Demonstrates that the dyad algebra is computationally useful for NLP, not just theoretical.

**6seconds / EQ practice:**
- Six Seconds (6seconds.org) — Global nonprofit founded 1997, largest organization dedicated to emotional intelligence. Publishes SEI (Six Seconds Emotional Intelligence) assessment, used by 1M+ people. Annual *State of the Heart* report tracks global EQ trends. The emotion blend chart in this directory is their popularized adaptation of Plutchik, simplified from 8 to 5 base emotions (Joy, Sadness, Disgust, Fear, Anger) with a 5×5 symmetric blend matrix.
- Six Seconds' research is practitioner-oriented (training, certification, organizational consulting), not formal or computational. Useful as a source of curated emotion vocabularies but not for algebraic structure.

**Algebraic observations (original to this project, informal):**
- The 6sec chart is a symmetric bilinear form on a 5-element set. Not closed (products not in generating set), so not even a magma. Self-products are intensifications (ecstasy, despair, abhorrence, terror, rage). The chart is structurally similar to the furry logic problem: each blend genuinely inhabits both parent types simultaneously, not a graded mixture.
- Plutchik's wheel has more structure: 8 generators on a cyclic group, Z₂ involution (opposition), dyad distance grading (primary/secondary/tertiary), intensity rays, and annihilation of opposites. The skeleton is approximately Z₂ × Z₈. Still not closed — the 24 dyads don't recombine — but the grading gives a way to specify how "far" a committee member's emotional blend should reach.

**Houston Four Levels (upstream theory):**
- Houston, J. — Four Levels model of apprehending reality (sensory, psychological, mythic, spiritual). See `wild/diary/2026-03-15-mystic-narrative.md`. Emotions as Type 1 (System 1) conditioners of narrative formation. Committee member propensities as stable configurations of these levels.

**Cyberneutics connection to furry logic:**
- Emotion blends as soft-typed texts: "dread" (Sadness × Fear) fully inhabits both parent types, not partially. This is the furry logic situation. Cross-reference `wild/fuzzy-type-theory/`.

### 3. Copy the image

Copy `6sec-emotion-blend-chart.png` (from uploads or provide path) into `wild/emotional-attention-steering/`.

### 4. Amend the diary entry

Append a new section to `wild/diary/2026-03-15-emotional-attention-steering.md` before the Cross-references section:

```markdown
---

## Addendum: Emotion blend vocabularies as scoring apparatus (2026-03-26)

The negative decision above — do not attempt a rich emotional ontology for the state variables — holds. But it addresses only half the problem. The PID state variables (urgency, frustration, confidence, engagement) are engineering control variables. The orchestrator's *scoring function* — which evaluates the previous round's transcript to compute PID inputs — needs a finer diagnostic vocabulary to characterize *what emotional tone a character's output actually exhibits*.

Two candidate vocabularies emerged from examining emotion blend taxonomies:

**Plutchik's wheel of emotions** (1980). Eight generators (Joy, Trust, Fear, Surprise, Sadness, Disgust, Anger, Anticipation) arranged as four opposed pairs on a cyclic group. Dyads graded by distance: primary (adjacent, frequently felt — e.g. Love = Joy + Trust), secondary (2 apart, sometimes felt — e.g. Envy = Sadness + Anger), tertiary (3 apart, seldom felt — e.g. Shame = Fear + Disgust). Opposites annihilate. Intensity varies along a radial axis (annoyance → anger → rage). The structure has a Z₂ × Z₈ skeleton — considerably more algebraic than the 6sec chart below. Still not closed (the 24 dyads don't recombine), but the grading gives a way to specify how "far" a committee member's emotional blend should reach: primary dyads for natural/frequent blends, tertiary for rarer, more unstable combinations.

**6sec emotion blend chart** (6seconds.org). Five generators (Joy, Sadness, Disgust, Fear, Anger) with a 5×5 symmetric blend matrix producing 25 named combinations. Self-products are intensifications (ecstasy, despair, abhorrence, terror, rage). Not closed — not even a magma. But useful as a compact reference grid for blend vocabulary and drift detection.

**Role in the architecture.** These vocabularies are not state variables in the PID loop. They are part of the measurement/scoring apparatus that feeds *into* the PID. When the orchestrator scores the previous round's transcript — "was Maya's output anxious or merely cautious? Is Frankie's tone ironic or contemptuous?" — it needs discriminators finer than the four state dimensions. The blend taxonomies provide those. They also serve as calibration instruments: if a character's target operating point is "protective skepticism" (Fear × Joy in Plutchik's terms) but their output reads as "dread" (Sadness × Fear), that's detectable emotional drift.

**Connection to furry logic.** Each blend genuinely inhabits both parent types simultaneously — "dread" is fully Sadness and fully Fear, not 60/40. This is exactly the soft-type situation that furry logic addresses: fuzzy logic's graded single-type membership misrepresents what's happening. See `wild/fuzzy-type-theory/`.

**Prior art.** Tayari Meftah et al. (2010, 2011) formalized Plutchik algebraically as an 8-dimensional vector space (Emotica project). Semeraro et al. (2021) built PyPlutchik for corpus-level emotion annotation. Li et al. (2024, EMNLP) used Plutchik's dyad structure to improve MoE emotion classifiers. Collected references in `wild/emotional-attention-steering/references.md`.
```

### 5. Update `wild/README.md`

Add an entry under "Known Limitations and Research Directions" (or wherever it fits best):

```markdown
- **[Emotional Attention Steering](emotional-attention-steering/)** — *EXPLORATORY* — Architectural design for emotional state modulation in committee deliberation via external PID control loop. Emotion blend vocabularies (Plutchik, 6sec) as scoring apparatus for transcript evaluation. Long-term design target; prerequisites: metacog instrumentation, independent agents.
```

### 6. Check for dangling cross-reference

The diary entry references `research-programs/metacognition/` which does not exist. Note this but do not create it — it's a separate decision about when the metacog work is ready to graduate from diary-only to a research program.

## Image file

The image to copy into the new directory is at the path where it was uploaded. It's a PNG showing a 5×5 emotion blend matrix from 6seconds.org, titled "What do you get when your emotions combine?" Rename it to `6sec-emotion-blend-chart.png` in the new directory.
