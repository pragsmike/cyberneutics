# Session Handoff: 2026-03-13 (Palgebra Phases 1–2 — Markov Foundations + Honest Downgrades)

---

## Session Summary

**Trigger**: mg directed work on the palgebra, starting from the ACT review
(`palgebra/act-review-2026-03.md`). The review identified 10 prioritized gaps
and classified 18 categorical claims by warrant level. Fritz (2020) was flagged
as the most consequential missing citation (Gap #7).

**Actual outcome**: Phase 1 of the remediation plan (Foundations) is complete.
The Fritz reference was added, a detailed remediation plan was written, and
`categorical-structures.md` was substantially revised to ground the palgebra
in Fritz's Markov category framework.

---

## What was done

### 1. Fritz reference added to `palgebra/reference.md`

Full citation: Fritz, T. (2020). "A synthetic approach to Markov kernels,
conditional independence and theorems on sufficient statistics." *Advances in
Mathematics* 370, 107239. arXiv:1908.07021.

Committed in `8122666`.

### 2. Remediation plan written: `palgebra/remediation-plan.md`

Six-phase plan addressing all 10 gaps from the review. Phases:

1. Foundations (define Text precisely, Markov category, enrichment base)
2. Honest downgrades (decision monad, Frobenius, equalizer framing)
3. Formalize strongest claims (coproduct end-to-end, approximation metric)
4. Novel contributions (Probe as statistical test, soft type theory)
5. Integration (layer compatibility, editorial consistency)
6. Bibliography (missing citations, deeper engagement)

Committed in `8122666`.

### 3. `palgebra/categorical-structures.md` revised (Phase 1 execution)

305 insertions, 35 deletions. Changes:

**§1 (Preliminaries)**: Replaced "Coherence is approximate, not strict"
framing with "Stochastic does not mean incoherent." Now cleanly separates
compositional coherence (exact, by Markov category structure) from universal
properties (genuinely approximate, tested by Probe). Removed the word "lax."

**§2 (Objects and Morphisms)**: Replaced the Kleisli overclaim ("every
morphism is properly a Kleisli arrow of a nondeterminism monad") with a
forward reference to §2a. Added a closing note connecting the
transformation/enrichment distinction to Fritz's deterministic morphisms
(Definition 10.1).

**§2a (new: Text as a Markov category)**: States Fritz Definition 2.1 in
full. Builds a correspondence table mapping Fritz's framework to palgebra
notation. Verifies each axiom:
- Coassociativity/counitality: trivial (copy is pass-by-reference)
- Commutativity: by construction
- Monoidal compatibility: tupling of independent artifacts
- Naturality of del: **design discipline** — the most substantive axiom,
  enforced by operation isolation (no side effects beyond declared outputs)

Explains what the Markov category framing buys: exact associativity,
semicartesian (not cartesian) monoidal structure, comonoid status for
catalytic inputs, independence from specifying a monad (Corollary 3.2).
Defines deterministic morphisms and identifies them with enrichments.

**§2b (new: The enrichment base)**: Defines V = ({L,M,H}, min, High) as a
commutative quantale. States the enriched composition law. Verifies the
Kelly Ch. 1.2 enrichment axioms. Explains multi-dimensional scoring
(semiring, Pareto) as internal to scoring morphisms, not part of the
enrichment.

**§9**: Updated stale back-reference to old "lax/approximate" language.

**References**: Added Fritz with specific definition/theorem/lemma numbers.
Deepened Kelly citation to reference Ch. 1.2 specifically.

Not yet committed — this handoff and these changes go in the same commit.

---

### 4. Phase 2: Honest downgrades (second commit)

**2.1 Decision monad** — Rewrote the monad section of
`duality-and-composition.md`. Attempted to define η (trivial deliberation as
unit) and μ (flattening nested fan-funnel via a resolution→situation coercion).
Identified two gaps preventing a formal monad claim: (a) η may itself be
stochastic if it involves any LLM call, (b) μ requires a resolution→situation
coercion whose well-behavedness is empirical. Adopted honest framing:
"monad-inspired pipeline with operationally testable quality criteria derived
from the monad laws." The bind operation is well-defined regardless (it's just
composition of Markov kernels). Also removed the Kleisli interpretation
subsection (which depended on the old unspecified-monad framing) and replaced
with a bind-and-iteration subsection grounded in the Markov category.

**2.2 Frobenius terminology** — Dropped "multiplication" / "comultiplication"
from the symmetry table in `duality-and-composition.md` (replaced with
"Convergent (many-to-one)" / "Divergent (one-to-many)"). Rewrote §8 of
`categorical-structures.md`: renamed to "Divergent and Convergent Spiders,"
added explicit note that the Frobenius equation has not been verified and
likely does not hold, retained spider visual. Updated spider descriptions in
`duality-and-composition.md` (convergent/divergent node instead of
comultiplication/multiplication).

**2.3 Equalizer/pullback reframing** — Added italicised framing paragraph at
top of §6 of `categorical-structures.md` stating that §§6–7 are categorical
design specifications, not claims about existing operations. The morphisms
they require don't exist yet; the value is prescriptive.

## What was NOT done (remaining phases)

### Phase 3: Formalize strongest claims
- **3.1** Scenario-set coproduct end-to-end (the review's best candidate)
- **3.2** Give "approximate" a metric (reconstruction error via Probe)

### Phase 4: Novel contributions
- **4.1** Probe as statistical test of universal properties (potentially publishable)
- **4.2** Soft type theory as enriched presheaves (longer-term)

### Phase 5: Integration
- **5.1** Explicitly state the three-layer architecture (base → Markov → enriched)
- **5.2** Editorial consistency pass across all documents

### Phase 6: Bibliography
- Add Cho & Jacobs, Perrone, Kock, Heunen et al.
- Deepen engagement with Fong and Kelly beyond name-drops

See `palgebra/remediation-plan.md` for full details and execution order.

---

## Key design decisions

1. **Kept §2 as informal overview, added §2a/§2b as formal treatment.**
   mg's preference: give a taste first, promise precision in the next section.
   The reader who trusts the informal picture can skip ahead; the ACT reader
   can find the axioms.

2. **Naturality of del identified as the most substantive axiom.** It
   requires operation isolation (no side effects). This is a design discipline,
   not a structural guarantee. Violations (context-window leakage) would break
   the Markov category structure. The template system exists to maintain it.

3. **Dropped the Kleisli-with-unspecified-M framing.** Replaced with the
   synthetic Markov category approach (work with axioms directly, don't commit
   to a specific monad). Fritz Corollary 3.2 noted as the compatibility bridge
   if someone later pins down M.

---

## Files modified this session

| File | Status |
|------|--------|
| `palgebra/reference.md` | Fritz citation added (committed 8122666) |
| `palgebra/remediation-plan.md` | New file (committed 8122666) |
| `palgebra/categorical-structures.md` | Phase 1: §1 rewritten, §2 edited, §2a/§2b added, §9 updated, refs expanded. Phase 2: §8 rewritten (Frobenius dropped), §6 framing added |
| `palgebra/duality-and-composition.md` | Phase 2: monad section rewritten with explicit η/μ and honest status assessment, Frobenius terminology removed from symmetry table and spider descriptions |
| `agent/handoff-2026-03-13-palgebra-phase1.md` | This file |
