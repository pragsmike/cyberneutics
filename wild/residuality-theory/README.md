# Residuality Theory

> "Every time I repeat the walk I notice small differences from my previous experiences, and those small differences add up to solid knowledge about this walk." — Barry O'Reilly

Barry O'Reilly's Residuality Theory is a philosophy of software architecture that treats **residues** — what remains after a stressor impacts a system — as the fundamental unit of architectural design. Rather than designing for anticipated failures, you design with residues as building blocks so the system can survive stressors it wasn't designed for: antifragility rather than correctness.

Its three core philosophical commitments (from O'Reilly's NDC talks) mirror those of cyber-sense:

- **Process over substance** — systems are becomings, not static things
- **Criticality over correctness** — the goal is surviving the unknown, not satisfying specifications
- **Difference over essence** — knowledge accumulates through repeated traversal and attention to variation

---

## Architectural Walks

The concept introduced at [31:16 in the NDC Oslo 2024 talk](https://www.youtube.com/watch?v=H8ZOp8ayluU&t=1876s):

An **architectural walk** is knowledge-building through repeated traversal. You walk a system (or a problem space) multiple times; each repetition differs slightly from the last; the differences accumulate into genuine understanding that no single pass — and no static model — can provide. The architecture is discovered through walking, not specified in advance.

O'Reilly explicitly roots this in Deleuze: the walk is an instance of process philosophy in action — each repetition is not the same repetition, because both the walker and the path are different. This is precisely the Deleuzian "smooth space" traversal: following connections rather than a predetermined grid, letting difference lead.

---

## Connection to Cyber-Sense

### The Deleuzian thread

O'Reilly's philosophical sources overlap substantially with cyber-sense's:

- He explicitly cites Deleuze's process philosophy, difference over essence, and the primacy of change
- His walk-as-knowledge-building directly parallels cyber-sense's "repetition produces difference" insight from `essays/06-deleuze-difference-repetition.md`
- His positivism critique (architects who model reality until nothing of reality remains) echoes the second-order cybernetics material in `essays/04-cybernetics-and-observation.md`

The committee deliberation process can be read as an architectural walk through a problem space: each character follows their propensity-driven line of flight through the problem; the deliberation traces the topology of the decision space; the 02-deliberation.md transcript is what the walk leaves behind.

### Residues and eigenforms

A potential contributor raised the question: are residues akin to eigenforms?

**Short answer**: related but not identical, and the distinction is productive.

Both are about what *survives transformation* — what is invariant under a process. But:

- **Eigenform** (von Foerster): a fixed point of a *recursive self-referential* process — x such that F(x) = x. The stability emerges from repeated self-application; the eigenform is what the process converges *to* when run on its own outputs. See `essays/04-cybernetics-and-observation.md`.
- **Residue** (O'Reilly): what persists after *external* transformation — what survives disruption, refactoring, unknown stressors. Found by walking; what you discover when you return.

In the committee context this distinction is useful:

- A **single deliberation** produces a residue: the key tensions, surfaced assumptions, the resolution — what the architectural walk left behind in the 03-resolution.md.
- **Repeated deliberations** on the same topic hunt for the eigenform: the framing that only stabilizes after the recursive feedback loop has kicked the system out of shallow stable states. The committee → `/review` → remediation → `/review` cycle is literally F(F(F(x))).

Essay 04 puts it directly: "We use the committee structure to *prevent premature eigenforms*. We inject noise (character conflict) to kick the system out of shallow eigen-states, reshaping F(x) until the only stable solution is a robust, well-reasoned truth."

So: residues are what you find on one walk. Eigenforms are what you keep finding every time you walk. The remediation feedback loop is the process of distinguishing local fixed points from robust ones.

### Residuality and palgebra

Residuality Theory's framing (what persists through transformation) is adjacent to but distinct from the palgebra framing (what metadata accumulates through pipeline stages). They're complementary:

- Palgebra asks: what does each operation *add* to the artifact (enrichment) or produce from it (transformation)?
- Residuality asks: what *survives* across all those operations? What is the fixed architectural substrate?

A deliberation record (00-04 files) is both a palgebra artifact chain *and* the residue of the committee process. These framings illuminate different aspects of the same object.

---

## Definitive Resources

### Primary sources

- **Book**: [Residues: Time, Change, and Uncertainty in Software Architecture](https://leanpub.com/residuality) — O'Reilly's main text (Leanpub)
- **Academic paper**: [Residuality and Representation: Toward a Coherent Philosophy of Software Architecture](https://oro.open.ac.uk/98044/) — Open University repository
- **Academic paper**: [The Philosophy of Residuality Theory](https://www.sciencedirect.com/science/article/pii/S1877050921007420) — ScienceDirect

### Talks

- **NDC London 2024**: [An Introduction to Residuality Theory](https://www.youtube.com/watch?v=_MPUoiG6w_U) — comprehensive introduction
- **NDC Oslo 2024**: [The Philosophy of Architecture](https://www.youtube.com/watch?v=H8ZOp8ayluU) — the philosophical foundations; Architectural walks introduced at [31:16](https://www.youtube.com/watch?v=H8ZOp8ayluU&t=1876s)

### Practitioner overview

- [Applying Residuality Theory for Better Software Design](https://www.cutter.com/article/residuality-theory-introduction) — Cutter Consortium

---

## Status

Incoming — not yet tamed. This directory was created because an external contributor (second fork, February 2026) noted the Deleuzian walks → Architectural walks connection and because the eigenform question opened a productive theoretical seam. See `meta/uptake-and-usage.md` for context.

Possible directions:
- A committee deliberation on the question: what is the committee process in residuality terms? What are the residues of deliberation?
- Connecting O'Reilly's "criticality" (survive unknown stressors) to the evaluation rubric system (how do you know a deliberation is critical rather than just locally coherent?)
- Whether the 2-round remediation cap makes sense in eigenform terms — are we stopping at local fixed points?
