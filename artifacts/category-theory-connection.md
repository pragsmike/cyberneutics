# Category Theory and Narrative Engineering

> "Cybernetics is the science or the art of manipulating defensible metaphors; showing how they may be constructed and what can be inferred as a result of their existence." — Gordon Pask, *The Cybernetics of Human Learning and Performance* (1966)

## Why category theory is relevant

There is a formal parallel between Deleuzian philosophy and category theory that illuminates both — and that explains structurally why narrative engines behave the way they do.

This artifact extracts and develops the category-theoretic material from [Essay 06 (Deleuzian Foundations)](../essays/06-deleuze-difference-repetition.md) into a standalone reference for readers with the relevant mathematical background. Readers without that background lose nothing by skipping this — the practical implications are summarized in Essay 06 itself. For the full formalism applied to pipelines, see the [Palgebra Reference](../palgebra/reference.md).

---

## Arrows over objects

**Category theory privileges arrows over objects.** In traditional mathematics, you define objects (sets, groups, spaces) and then study functions between them. In category theory, the morphisms (arrows, transformations) are primary. Objects are just the sources and targets of morphisms. What matters is how things relate, not what things "are."

This is Deleuze's inversion in mathematical form. Identity (what an object IS) becomes secondary to difference (how objects relate and transform).

## Isomorphism replaces equality

In category theory, you rarely ask whether two things are "equal." You ask whether they're isomorphic — structurally the same for relevant purposes, even if not identical. Two groups can be isomorphic without being the same group. Two categories can be equivalent without containing the same objects.

This is a weaker notion than equality, and it's more useful. It lets you say "these are the same in the ways that matter" without claiming they're identical in all respects.

For narrative engineering, this matters directly:

- Two stories can be "equivalent" for decision-making purposes without being the same story
- Two committee outputs can be isomorphic in their recommendation structure even if they differ in wording
- Multiple interpretations can be categorically equivalent — different objects, same morphisms

## LLMs as lossy compression

LLMs have been described as "lossy but extremely capacious compression algorithms." Category theory helps explain what's preserved and what's lost.

What's preserved: **structure**. The relationships between concepts, the patterns of narrative, the morphisms that connect ideas. When the model compresses "all of human text," it keeps the arrows — how things relate to other things.

What's lost: **particulars**. Specific facts, exact quotes, ground truth. The objects get fuzzy; the arrows stay sharp.

This is why LLMs are good at generating plausible continuations (following structural patterns), producing multiple valid framings (different objects, same morphisms), and recognizing genre and style (structural, not particular). And bad at precise factual recall (particulars, not structure), exact quotation (specific objects, not relationships), and distinguishing between structurally similar but factually different claims.

Deleuze would say: the compression preserves difference (relations) and loses identity (fixed objects). That's not a bug. That's what compression that respects the primacy of difference looks like.

## Charts on a manifold (categorical framing)

The charts-on-a-manifold metaphor from Essay 06 — committee characters as different coordinate patches on a problem manifold — has a precise categorical description: the charts are objects, the transition functions are morphisms, and the manifold emerges from their categorical structure. Deleuze provides the philosophy: what's primary is the *differences* between charts, not some underlying identity they're all approximating.

## Further reading

**Category Theory Background**:
- Lawvere, F. William and Schanuel, Stephen. *Conceptual Mathematics* (1997) — Accessible introduction emphasizing conceptual over technical
- Spivak, David. *Category Theory for the Sciences* (2014) — Applications-focused introduction
- Fong, Brendan and Spivak, David. *Seven Sketches in Compositionality* (2019) — Resource-theoretic framework that palgebra adapts

**Related in this repo**:
- [Palgebra Reference](../palgebra/reference.md) — the formalism that makes these ideas composable
- [Decorated Texts](../palgebra/decorated-texts.md) — the full development of pipeline algebra from first principles
- [Essay 08: From Methodology to Formalism](../essays/08-from-methodology-to-formalism.md) — bridging the philosophical and algebraic vocabularies
