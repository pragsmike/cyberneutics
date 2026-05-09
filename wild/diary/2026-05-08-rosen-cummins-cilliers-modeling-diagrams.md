# Diary: Two Diagrams of the Modeling Relation — Rosen, Cummins, Cilliers

**Date:** 2026-05-08

**Context:** Started reading Cilliers's *Complexity and Postmodernism* (the residuality-and-Cilliers thread from 05-03 having pulled the book down off the shelf). Spotted the encode-do-something-decode shape in the "Problems with Representation" chapter — Cummins's Tower Bridge, Figure 5.1 — and recognized it as structurally akin to Rosen's Figure 3H.2 from *Life Itself*. The conversation that followed worked through what the diagrams actually share, where they diverge, and what Cilliers is doing with Cummins that he doesn't quite have the apparatus to do explicitly. Several false starts were discarded along the way; what survives is the synthesis worth keeping.

---

## The two figures

Rosen's 3H.2 (p. 60) shows two boxes labeled N and F, each with a self-loop — arrow ① on N labeled CAUSAL (the printed "CASUAL" is a typo), arrow ③ on F labeled INFERENCE — and two crossing arrows: ② ENCODING from N to F and ④ DECODING from F to N. The criterion: F is a model of N when arrow ① and the composition ②∘③∘④ produce the same answer — what Rosen calls *congruence of entailment*.

Cummins's Tower Bridge (Cilliers Figure 5.1, p. 63) shows two horizontal arrows at different levels: g at the bottom taking implementation states i to o, f at the top taking interpretations I(i) to I(o). Vertical arrows labeled I run upward from each implementation state to its content. The model "works" when f ∘ I = I ∘ g — when interpreting then applying the rule equals applying the causal law then interpreting.

The visual rhetoric is similar enough that the recognition was immediate. The structural commitments turn out to be quite different.

## What Cummins is actually claiming

The Tower Bridge is, structurally, a homomorphism square between two dynamical systems. Bottom rail g is the implementation-level causal law; top rail f is the content-level intelligible rule; I is the interpretation function. Commutativity is naturality: the interpretation respects the dynamics on both rails. In categorical idiom, I would be a natural transformation between functors representing the two levels.

Cummins drew this to make Fodor's commitments explicit. RTM requires:
- An implementation level that admits causal-law description (g lives in some category)
- A content level that admits rule-based description (f lives in some category)
- An interpretation function that bridges them homomorphically (I is a structure-preserving map)

The four conditions on p. 63 (from Morris 1991) are conditions for the diagram to be technically precise: states must have content, f must be an *intelligible rule*, the implementation must individuate non-semantically, and g must be a non-semantic causal law. These are not vocabulary; they are *demands on the structure*. Cummins is asserting that the diagram commutes when the conditions hold, and Fodor is wagering that the conditions can be met.

The hidden premise is that both rails are well-behaved mathematical structures — categories with morphisms, rules that compose, laws that admit explicit description. The Tower Bridge presupposes the categorical setting on both sides and asks only whether I respects it.

## What Rosen is doing differently

Rosen's diagram looks similar but is doing radically different work. The point — sharpened in conversation, recovered from the 04-26 diary entry — is that Rosen's apparatus is **vocabulary, not structural assertion**. The diagram introduces names for the parts of the modeling relation: N for the system, F for the formal model, ε and δ for the encoding and decoding moves, ① for whatever entailment structure the world actually has, ③ for the entailment structure inside our formal system. These are placeholders that let us *talk about* what is happening when we model, without committing to the relationships being mathematically well-behaved.

The visual rhetoric of a coalgebra-homomorphism square is preserved precisely so the *failure* of commutativity becomes visible and instrumented. The diagram is not a structural claim about the modeling relation. It is a glossary for a conversation we have to keep having empirically. Rosen calls F a model of N "to the extent that" the diagram commutes — to the extent that — not as a structural statement but as a partial, ongoing, fallibilist criterion.

The natural-system side is precisely the not-yet-categorifiable thing we are trying to model. Arrow ① is a placeholder for "whatever the world does." A functor would require both domains to be categories with explicitly specified morphisms, and the modeling relation has only one such side. The looseness is the point of Rosen's apparatus rather than a defect.

## The Cilliers move

Cilliers uses the Tower Bridge as a foil. The standard reading — which I had on first pass — is that Cilliers attacks the *interpretation function* I: distributed representations don't have stable I-targets; meaning is contextual, holistic, deferred. The Derrida-flavored attack. This works at one level.

But the deeper attack — implicit in Cilliers's framing of complexity, made explicit in conversation — is structural rather than rhetorical. **Cilliers's claim that "models of complex systems must themselves be complex" applies to both rails of the Tower Bridge.** If language is a complex system in Rosen's sense (not merely complicated), then f is not a well-defined arrow in any category. The content level isn't categorical. The "intelligible rule" condition (Morris's condition ii) smuggles in a complication assumption that complexity denies.

This is a stronger reading than the Derridean one. Cilliers's argument in the connectionist chapters — that distributed representations are evidence of language's complexity rather than alternative computational substrate — is the structural move. The Tower Bridge fails not because I cannot be constructed but because *neither rail is what Cummins needs it to be*. Both f and g are operating in a complex, messy, nonlinear domain, and the categorical iconography is misleading about what the underlying objects are.

Cilliers half-says this. He stops at the connectionist evidence and the Derridean rhetoric. He doesn't reach for Rosen's vocabulary, doesn't have Bradley's enriched-categorical machinery, doesn't have Deleuze's virtual/actual to articulate the complexity-of-the-content-level explicitly. The 1998 anglophone reception didn't put those tools on his desk. But the move is there in the text, and reading it through Rosen makes it visible.

## Rosen and Cilliers as the same critique at different depths

The synthesis: **Cummins's Tower Bridge is what cognitivism wants the modeling relation to be — both rails categorical, I a homomorphism, commutativity guaranteed by the right construction.** Rosen's 3H.2 is what the modeling relation actually is when the natural-system side is taken seriously as not-yet-categorical. Cilliers's argument extends the same worry to the content side: if language is complex, then *both* sides of the Tower Bridge are not-yet-categorical, and the homomorphism question is doubly ill-posed.

Rosen and Cilliers are making the same critique at different depths. Rosen denies that the natural-system side admits clean mathematical description. Cilliers denies it for the formal side too, when the system being modeled is genuinely complex. The Tower Bridge fails because both rails are illegitimately presupposed to be tracks. Cummins drew the diagram to make Fodor's commitments visible; Rosen and Cilliers between them show that the commitments cannot be honored.

The functor temptation flagged in the 04-26 entry is the same temptation Cummins gives in to. Rosen resists it on the natural-system side; Cilliers, properly read, resists it on the formal-system side; the two together resist it on both sides. Cyberneutics inherits the resistance.

## Vocabulary versus structural assertion

The distinction is worth holding onto for cyberneutics's own apparatus. Fan-as-pushout and funnel-as-pullback, written in ACT terms, look like structural claims — assertions that the constructions are categorical operations in good standing. For the kinds of problems cyberneutics addresses (wicked problems, decisions under deep uncertainty, situations resistant to formalization), the structural reading is probably too strong.

The categorical iconography of the fan and funnel is doing the same job Rosen's diagram does: providing vocabulary for talking about what the committee is *attempting*, without asserting that the attempt has the structural properties the iconography suggests. The fan is "a generation of multiple scenarios from a shared source"; whether that generation is technically a pushout in some specifiable category is a separate question, possibly unanswerable, and the vocabulary does work even when the structure does not strictly hold. Palgebra's "provisionally useful but untrusted" framing already encodes this honestly — the formal apparatus functions as enriched vocabulary, with the question of whether it admits precise structural reading left open.

This bears on Hedges outreach. The honest framing is not "here is a categorical formalization of deliberation" but "here is a categorically-flavored vocabulary for talking about deliberation, which we are using productively while remaining uncertain whether the iconography admits the structural readings it invites." That is more defensible and more aligned with what is actually happening, and it is exactly the move Rosen made when he drew 3H.2.

## Presheaves and the sheaf-failure of language

Cummins's condition (i) — "states must have content" — is structurally a presheaf-style assignment: each implementation state c gets a content P(c). The Tower Bridge, properly read, asks for this assignment to behave naturally with respect to the dynamics — for the naturality squares to commute. Fodor's RTM is the wager that mental content forms a presheaf on the category of neural states, supporting natural transformations corresponding to compositional thought.

For Mentalese to do the work Fodor needs, the content presheaf must be *sheaf-like*: local data must glue to global data uniquely. Compositionality and systematicity demand it — if you can think *aRb* and *bRc* you can think *aRc*; if you can think two thoughts you can think their conjunction. These are exactly the gluing conditions that distinguish a sheaf from a mere presheaf.

Cilliers's distributed-representation argument, read through this lens, is that the content presheaf *fails to be a sheaf*. Local activations don't glue cleanly; consistent-looking pieces fail to extend to a coherent whole, or extend to multiple incompatible wholes. The contextual shift of meaning isn't a quirk; it is sheaf-failure at the structural level. This is what "language is complex" means in formal terms: language is a presheaf without gluing, not a sheaf.

The serialization problem identified across Faulkner, Agee, and the fan/funnel architecture has the same structure. A rich relational object forced through a serial channel emerges on the other side as fragments that don't glue back together cleanly. Faulkner's response — multiple narrators each with partial views, none of whom delivers the whole — is a Čech-cover-without-a-gluing aesthetic. He is drawing attention to the sheaf-failure rather than papering over it with omniscient narration. The fan generates a covering family of scenarios; the funnel asks whether they cohere into a unified picture or reveal an obstruction; variance across runs has the cohomological flavor of measuring the failure of gluing. This is speculative — it wants more thought before it is anything more than suggestive — but it gives a candidate categorical home to "fan-funnel as instrument for non-functorial modeling relations."

## What this gives the blade-without-a-handle framing

A circular saw works because its action on wood is well-modeled — the kerf, the kickback dynamics, the relationship between hand-pressure and blade-trajectory are physical regularities that admit categorical capture. The handle is comfortable because the saw's domain is *complicated, not complex*. The Tower Bridge from "skilled human action" to "blade behavior" actually commutes, by engineering.

LLMs operate on language, which is complex in Rosen's and Cilliers's sense. The "Tower Bridge" from "what the user means by their prompt" to "what the model does in response" cannot be expected to commute by structural means — the rails aren't tracks. This is a sharper statement of the disanalogy than "LLMs are unlike saws because their outputs aren't reliable." The disanalogy is structural: saws live in a domain where the modeling relation is approximately functorial (engineered to be so); LLMs live in a domain where the modeling relation is what Rosen drew, with both sides not-yet-categorical.

Cyberneutics's response — fan, funnel, calibration register, inspectable reasoning records — is not an attempt to recover the missing categorical structure. It is an attempt to *instrument the failure of commutativity*, to make visible the places where the would-be Tower Bridge does not commute, and to provide audit trails for those failures. The committee variance is diagnostic rather than noise around a true verdict; the inspectable record preserves the relational structure that any reductive summary would discard.

This is consistent with everything already in the framework, but the Cummins/Rosen/Cilliers triangulation sharpens the *why*. The framework is not building a better bridge. It is building a handle for working honestly in the wreckage of the bridge that cannot be built.

---

## Actions

1. The Cummins/Rosen comparison — Tower Bridge as Fodor's structural claim, 3H.2 as Rosen's vocabulary — belongs as a short section in the references entry for Rosen's *Life Itself*, or as a short essay-length working note. The figure-by-figure comparison is clean enough to exhibit, and it sharpens the functor-temptation-resisted point from the 04-26 entry.

2. **Cilliers's "models of complex systems must themselves be complex"** is the load-bearing claim and deserves explicit citation. Find the page reference on the next reading pass and add it to the Cilliers references entry, alongside the page-13 citation already noted in 05-03.

3. The **vocabulary-versus-structural-assertion** distinction wants its own short note, probably in `palgebra/` or `agent/onboarding-core.md`, framing the cyberneutics apparatus's epistemic status. Provisionally-useful-but-untrusted already encodes this; the diagram-as-glossary framing makes the move explicit and connects it to Rosen's own practice.

4. The **presheaf / sheaf-failure** reading of the content level is genuinely speculative but lines up with palgebra's quantale-valued presheaves and with the Bradley convergence flagged in 05-03. Worth a wild/ note distinct from this diary entry — "States have content as a presheaf condition; what sheaf-failure means for the Tower Bridge" — when the connection to existing palgebra work has been thought through more carefully.

5. The **fan as Čech cover, funnel as gluing-or-its-failure, variance as cohomological obstruction** speculation is a candidate research-programs/ thread, not yet ripe. Hold it. The instinct is right that the fan-funnel architecture wants this kind of categorical home; whether it admits one is a question palgebra is the right venue for, eventually, with Hedges-grade scrutiny.

6. The **blade-without-a-handle disanalogy** as restated here — saws live in a complicated domain where the Tower Bridge is engineered to commute, LLMs live in a complex domain where it cannot — belongs in the AI safety essay or its companion. Sharper than the prior "LLMs aren't reliable like saws" framing because it locates the disanalogy in the structure of the underlying domain rather than in the tool's quality.

7. Continue reading Cilliers. The "Problems with Representation" chapter is doing the work flagged here; later chapters likely sharpen the connectionism-as-evidence-of-complexity argument. Note where Cilliers explicitly resists the rule-based reading and where he merely gestures at the resistance.

---

*Cross-references: [`wild/diary/2026-04-26-musings-on-residuality-antifragility-rosen-and-pask.md`](2026-04-26-musings-on-residuality-antifragility-rosen-and-pask.md) (Rosen's modeling relation, kept loose; functor temptation resisted), [`wild/diary/2026-05-03-apophatic-steel-killed-virus-vaccine.md`](2026-05-03-apophatic-steel-killed-virus-vaccine.md) (Cilliers as philosopher's response to requisite variety; Bradley as the math Cilliers reached for), [`wild/diary/2026-04-09-stories-scenarios-serialization.md`](2026-04-09-stories-scenarios-serialization.md) (serialization problem; Faulkner and Agee), [`wild/diary/2026-04-13-convergences.md`](2026-04-13-convergences.md) (Rice's theorem and local charts; verification as relational), [`essays/blade-without-a-handle.md`](../../essays/blade-without-a-handle.md) (disanalogy with engineered tools), [`palgebra/reference.md`](../../palgebra/reference.md) (quantale-valued presheaves; provisionally-useful-but-untrusted register), [`references/bradley-cyberneutics-references.md`](../../references/bradley-cyberneutics-references.md) (enriched categorical structure of language), [`references/README.md`](../../references/README.md) (Rosen's *Life Itself* entry; Cilliers entry to be expanded)*
