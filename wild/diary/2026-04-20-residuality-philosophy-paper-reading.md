# 2026-04-20 — Residuality: the philosophy paper, read at last

A long conversation that started with Eric Normand's substack piece on residuality theory and ended with the 2021 Procedia paper itself in hand. The paper changes several things about how `wild/residuality-theory/` should be developed and how essay-13 should eventually be framed. Recording the findings while they are fresh.

## What prompted the re-reading

Normand's substack is the gentle intro — incidence matrix, K-reduction, a 10,000-lightbulb Kauffman network, a worked example with a country-based coupon banner service. Useful pedagogy, but the philosophical claims sit in the two Procedia papers he links. The 2020 paper is operational: how to build residual architectures. The 2021 paper is philosophical: why the method works, and what it assumes about reality. The 2023 "Residuality and Representation" paper is O'Reilly's own restatement of the 2021 philosophy paper with an expanded post-structural lineage. The 2021 paper is load-bearing for essay-13, and I had not actually read it.

I have now. Full text, eight pages, all in.

## What the 2021 paper actually argues

The spine is not "processuality, criticality, difference" — that is the 2023 restatement's organization. The 2021 paper is organized around a single target: the **component metaphor**. O'Reilly argues that the component metaphor (organizations modelable as capabilities, processes, use cases, and software components) is a heuristic that smuggles four philosophical commitments into architecture without architects noticing:

1. **Essentialism** — Platonic ideal forms, carried forward into OOP, EA repositories, reusable components, SMART requirements.
2. **The causalities of certainty** — Stacey's three: formative (structure dictates future), rationalist (human reasoning), efficient (Newtonian cause-effect). Together these underwrite scientific management's "dominant discourse."
3. **Cybernetics** — here O'Reilly names Stafford Beer's VSM specifically, as a "second-order abstraction" that gives a quasi-scientific facade to decision-making under uncertainty.
4. **Structuralism** — 1950s French structuralism, showing up in requirements engineering and enterprise architecture.

The counter-move is **residual causality**. Not "residuality uses a different causal model" — something sharper. *Structure itself is the risk.* Architectural decisions around structure will eventually destroy the system's ability to respond to its environment. The architect's conventional role — bringing order to chaos, Plato's demiurge — is inverted: the architect as "dangerous actor whose obsession with the removal of noise presents inherent danger to all stakeholders."

The via negativa move: we cannot identify perfect form, but we can identify residual cause and remove it.

## Where Deleuze actually sits in this

Less centrally than I had assumed. The 2021 paper name-checks Deleuze once, in a single sentence: *"Deleuze clearly saw post-structuralism's escape from rigid structures as a cause for celebration."* That is the full extent of the Deleuze citation. No *Difference and Repetition*, no technical use of "difference," no rhizome.

The heavy post-structural lifting is done by **Serres** (via Brown's 2002 paper in *Theory, Culture & Society*) and **Latour** (Actor-Network Theory, *Science in Action*). Serres on noise-as-worth-including, modeling, translation. Latour on the component metaphor as a constructed fact — a Latourian black box "validated by inclusion in thousands of texts yet with little scientific backing in the beginning."

The single most important passage for us is this one:

> "The techniques present in residuality theory were discovered through the kind of tinkering espoused by Taleb, and the similarities between residual analysis and Serres' thinking are uncanny, as these methods evolved not from an intellectual framework or knowledge of Serres' work, but from the need to survive and deliver structure in conditions of uncertainty."

O'Reilly himself frames the convergence as *after-the-fact alignment, not borrowing*. That is exactly the narrative-proof structure — epistemic compulsion from independent convergence across unrelated traditions. It is stronger than a citation chain.

## Three things this changes for us

**1. Essay-13's Deleuze framing has to be revised.** The earlier plan was to present residuality as borrowing from or deeply aligned with Deleuze. That over-reads the 2021 text. The honest framing is: the pattern "critique of representation as secondarizing difference/process" is recognizably Deleuzian at the level of argumentative shape, but O'Reilly's actual post-structural anchors are Serres and Latour. Essay-13 should cite them accordingly. Our own framework's Deleuzian commitments (essays 06, 07) are independent of residuality's, and the two citation chains should stay separate.

**2. The Stacey gap is real and larger than the Serres gap.** Stacey's *Complexity and Organizational Reality* is cited four times in the 2021 paper and underwrites the three-causalities-of-certainty framework that does the philosophical work. Stacey is not currently in our references/README.md or the books inventory. The Serres gap is similar but smaller (one cited paper, via Brown). Both are worth filling, but Stacey first.

**3. There is a cybernetics critique in the paper we have to answer directly.** O'Reilly calls out VSM specifically: "simplified models of reality, second order abstractions in Stacey's work, that are allowed to take the place of real world structures and give a quasi scientific facade to decision making in conditions of high uncertainty." Our framework uses Beer explicitly — the calibration register is System 3\*-adjacent. A careful reader of both will notice the tension. The honest response: the committee pipeline addresses the specific failure O'Reilly identifies. VSM hands architects a template (five systems, recursion) to apply before examining whether the terrain justifies it. The committee pipeline does the opposite — it refuses template-application and insists on stress-testing structure across scenarios. That is a defensible answer, but essay-13 has to make it explicitly, or we inherit the charge O'Reilly levels at Beer.

## Where residual causality plugs into open threads

The concept — decisions made long ago in different circumstances for different reasons constrain human action in an unknown future — is structurally the same problem the dual-use dehumanization concern is about. Teaching children to emotionally disengage from convincing AI agents is a structural decision that will constrain attractors no one is currently planning for. The cue-card pattern is residual causality in cognition: rehearsed positions installed for one purpose activate before analysis when new terrain arrives. Framing these as residual-causality cases gives us language that locates the harm in the structure itself, not in misuse — which is a sharper framing than "dual-use risk."

## Where the paper is honest about its own limits

O'Reilly closes the paper saying he is not interested in further post-structural theoretical development: *"Residuality theory was born in practice and it is there that the ideas should primarily continue to evolve. Debates around these concepts are not interesting to the architect, building resilient systems is."* And he is generous with the component metaphor — it can coexist with residuality, because the component metaphor *is itself a residue* (the leftover after complexity exposed architecture's weaknesses).

This is worth imitating. Essay-13 should not treat residuality as a universal solvent or a rival to component thinking. It should present both as charts, with residuality earning its place by covering terrain (genuine uncertainty, asymmetric blast radius, wicked problems) that the component metaphor handles poorly.

## Next moves

Separate from essay-12's graduation (now in motion), the sequence for residuality is:

1. Add O'Reilly (2020, 2021, 2023) and Normand (2024) to references/README.md under a new Residuality Theory subsection. Add Brown (2002) on Serres. Add Stacey (2009).
2. Consider buying or borrowing Stacey's *Complexity and Organizational Reality* and adding it to the inventory.
3. Sit with the 2021 paper. It is short and dense; one careful re-read will probably surface things this diary entry misses.
4. When essay-13 is drafted — after essay-12 has graduated and after at least one sprint of sitting with the paper — make the revisions above: Serres-and-Latour as primary anchors, Deleuze as pattern-match only, Stacey as load-bearing, the VSM critique answered explicitly, residual causality as the core concept connecting structure-as-risk to the pipeline's stress-testing posture.

## One line worth keeping

O'Reilly calls the role of the skeptical architect "the eye of the storm." The pipeline is the storm; the human gate is the eye. That framing might earn its way into an essay.
