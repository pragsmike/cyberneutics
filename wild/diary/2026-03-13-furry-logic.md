# Diary: Furry Logic — Type Membership as Measurement

**Date:** 2026-03-13
**Context:** Improvisational conversation exploring the type theory of texts, motivated by the palgebra soft-type system and its inadequacy with texts that genuinely span multiple types. This entry captures ideas for potential development into an essay.

---

## 1. The Problem

Soft types in palgebra handle graded membership — a text inhabits a type *to a degree*. Fuzzy logic does the same thing: a single membership function returns a grade in [0,1]. But graded membership in *one* type is not the same problem as membership spread across *many distinct* types.

A text can fully inhabit two different types simultaneously. A news article can be evidence *and* argument. A committee transcript can be data *and* metadata. The multiplicity here is not a matter of partial membership — it is a matter of genuine type plurality. The text is not 0.5 evidence and 0.5 argument; it is 1.0 of each along orthogonal axes.

Fuzzy logic has no answer to this. Neither does description logic.

---

## 2. Prior Art: The DL Historical Arc

Description logic (DL) was the dominant approach to text classification in the early semantic web era — OWL, RDF, the vision of a machine-readable web of meaning. DL encodes type membership as *links in a graph*: "mammal" subsumes "dog" is an explicit edge. Classification is graph reachability. The reasoner walks the graph.

This was a heroic attempt to do formally what human librarians do intuitively. It required someone to manually curate the ontology — to declare, in advance, every type and every subsumption relation. The bet was that findability could be solved by making type membership *explicit and traversable*.

Then PageRank happened, and then distributional semantics, and the eigenvector approaches discovered implicit type structure from co-occurrence statistics without any explicit ontology. Classification emerged from geometry rather than declaration. The semantic web largely collapsed as a research program for general findability, surviving mainly in constrained domains (biomedical ontologies, Wikidata, knowledge graphs for structured queries).

The structural difference matters: DL classifiers are *links*; soft-type classifiers are *partial functions over text-space*. In DL, a text spanning two types gets two ABox assertions — clean, but it loses the internal structure of *why* the text spans types. In the functional picture, a bimodal scoring function is information: it tells you the text has two modes, two centers of gravity in type-space.

---

## 3. Furry Logic

**Fuzzy logic** grades membership in one type. A text is 0.7 evidence.

**Furry logic** distributes membership across many types. A text's type is a *measure* on type-space, not a point or a grade. Single-type texts are delta functions. Fuzzy membership is a smeared delta. Texts that genuinely span two types are bimodal distributions.

The name is available. There is a popular science book called *Furry Logic* about animal physics, and various informal uses of the phrase, but nothing in formal logic or type theory.

The name earns its keep beyond wordplay. Animals are the canonical example of natural kinds that resist crisp boundaries — is a virus alive? is a platypus a mammal in the same sense as a dog? The furriness is not a defect of our classification system; it reflects genuine structure in the world. Texts are the same.

More precisely: furry logic is to fuzzy logic as a probability distribution is to a point estimate. Fuzzy logic collapses the distribution to its mode. Furry logic keeps the full shape.

---

## 4. The Measurement Framing

The key conceptual move — applicable to both soft types and furry logic — is from *declaration* to *measurement*.

In DL, you ask: what type *is* this text? The answer is a fact in the ABox.

In the measurement framing, you ask: what does *this rubric* read when applied to this text? The rubric is the instrument. Different rubrics give different readings of the same text. The type is not an intrinsic property of the text; it is a relational property between text and instrument.

This is the same move distributional semantics made against symbolic AI: meaning is not a label attached to a token, it is a position in a high-dimensional space defined by co-occurrence relations. Type is not a property of the text; it is a geometry.

Operationally: you don't ask whether a text is evidence. You apply an evidence rubric and get a score. You apply an argument rubric and get a score. The text's "type" is the vector of scores across your rubric library. Furry logic is the logic of that vector.

---

## 5. Illuminating Constructions

Several categorical constructions from the conversation are worth preserving:

**Coproduct (A + B)** — a text that is a tagged union of two types. The tags tell you which type each part came from. Real texts don't arrive with tags; the decomposition has to be inferred. This is the problem furry logic is trying to solve.

**Coend** — the canonical way to eliminate a "dummy variable" you're uncertain about. When you don't know which decomposition A + B is the right one, the coend integrates over all possible decompositions. Formally the right tool for untagged mixed-type texts, though operationally demanding.

**Pushout** — given two texts that share a common sub-text, the pushout is the most economical text containing both. This is the synthesis operation: the minimal text that respects two divergent positions. Relevant for the funnel's convergence and for merging evidence sources.

**Pullback** — the dual: the most general text that inhabits two types simultaneously. The intersection type, but with categorical guarantees about tightness.

**Tensor product vs. cartesian product** — A × B says "an A and a B, independently." A ⊗ B says "an A and a B that may share resources or context." For texts generated from a common situation, the tensor is usually more honest than the product. Two evidence files from the same case are not independent.

---

## 6. The Routing Consequence

Why does this matter operationally? Pipeline routing.

In a standard typed pipeline, routing is a switch statement: if type = evidence, send to aggregator; if type = argument, send to evaluator. This works when type membership is crisp.

When type membership is a distribution, routing becomes a decision under uncertainty. The pipeline has to commit — texts can only go to one place — but the commitment has to be made from a probability distribution, not a known fact. This is familiar territory from signal detection theory and Bayesian decision theory. The pipeline's router is a Bayesian classifier making a MAP estimate.

The furry logic framing makes explicit what was implicit in every real-world classification pipeline: you are always making a bet, and the distribution over types is the thing you're betting with.

---

## 7. Essay Structure (Tentative)

Main essay, for engineers and practitioners:
1. The problem: texts that genuinely span types
2. Why fuzzy logic doesn't solve it (graded membership in one type ≠ membership across many types)
3. The DL historical arc as contrast (declaration vs. measurement)
4. The measurement framing: type as rubric reading
5. Furry logic: type membership as a distribution over type-space
6. The routing consequence: why this matters in practice

Appendix, for cybercat aficionados:
- Mapping to formal constructions: coproduct, coend, pushout, pullback, tensor
- Furry logic as measure on type-space; composition as convolution or Wasserstein transport
- Open questions: does furry logic need a new proof theory? Is there a Curry-Howard correspondence for soft types? Relation to graded/quantitative type theory (Atkey et al.)
- Relation to Gärdenfors' conceptual spaces (convex regions in geometric space as a geometric version of the same idea)

---

## Agent Instructions

1. Save this file as `agent/diary/2026-03-13-furry-logic.md`.
2. No structural changes to the repo are implied by this entry. Ideas need further development.
3. The essay outlined in Section 7 is a candidate for the essay series, probably after the civic application essay (Avenue C from the narrative immune systems diary). The appendix structure — same core text, technical spine visible only to those who want it — should be the model for future essays aimed at mixed audiences.
4. The DL historical arc (Section 2) connects to the bath model formalization (Promising Avenue A from narrative immune systems). If that work proceeds, this diary entry's DL treatment should inform it.
