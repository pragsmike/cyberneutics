# Phase 2: Deliberation

**Topic:** Should we add a short glossary of key terms (e.g. 'fan', 'funnel', 'meta-d'') to the README or a dedicated doc?  
**Protocol:** Robert's Rules; adversarial engagement.

---

## Opening Statements

### Maya
A glossary in the README is a maintenance trap. Every new term we add creates a promise we have to keep updated. If we put it in the README, we're saying "this is the canonical list" — and then when we introduce a term in an essay and forget the README, we look sloppy. Dedicated doc is slightly better (one place to update) but still adds surface area. I'd rather link to the palgebra reference and key artifacts than maintain a separate glossary. Nay unless we commit to a lightweight process.

### Frankie
New readers hit jargon immediately: fan, funnel, meta-d', resolution, deliberation. If we don't define them in one place, we're asking people to hunt. That's a barrier to the mission. A short glossary — in README or a one-pager — signals "we want you to get this." I'm Aye for a minimal glossary (5–10 terms) with one-line definitions and links to depth. README keeps it visible; dedicated doc keeps README short. I'll take either.

### Joe
We've seen glossaries go stale. Projects add them with good intentions; six months later half the terms are wrong or missing. The palgebra reference already defines fan, funnel, and the algebra. So we have definitions — they're just not called "glossary." The question is whether we add a *redundant* short list for the README. I'm conditional Aye: add a glossary only if we tie it to a single source of truth (e.g. "drawn from palgebra/reference.md") and review it at release time.

### Vic
What problem are we solving? "People don't understand the terms" — do we have evidence? If it's hypothesis, we can test: add a three-term glossary (fan, funnel, resolution), see if we get fewer "what is X?" issues. I'm Aye for a minimal pilot: three to five terms, in README, with a note that we'll expand or move based on feedback. That's testable.

### Tammy
From a systems view, a glossary is a node in the information graph. If we add it, we create a dependency: other docs will point to it or assume it exists. So the decision is "do we want that node?" Yes if the payoff (lower friction) outweighs maintenance. I'm Aye for a short glossary in README or a doc that README links to, with clear ownership (who updates it when we add terms).

---

## Initial Positions Summary

| Member  | Stance | Confidence | Key Concern |
|---------|--------|------------|-------------|
| Maya    | Nay (conditional) | 2 | Maintenance trap; link to palgebra instead |
| Frankie | Aye    | 4 | Lower barrier; 5–10 terms |
| Joe     | Aye (conditional) | 3 | Tie to source of truth; review at release |
| Vic     | Aye (pilot) | 3 | Minimal pilot; testable |
| Tammy   | Aye    | 3 | Add node; clear ownership |

---

## Round 1

**Chair:** Four conditional or full Aye, one Nay. Maya, what would move you?

**Maya:** If the glossary is explicitly "drawn from palgebra and key artifacts; update when those change," I can accept a minimal list. So conditional Aye: glossary with a single source of truth and a review trigger.

**Vic:** I'll support that. Pilot: 5–10 terms, README or linked doc, "definitions follow palgebra/reference and artifacts; review when we add terms." That's my Aye.

**Chair:** Motion — Add a short glossary (5–10 terms: fan, funnel, meta-d', resolution, deliberation, etc.) in README or a dedicated doc linked from README; definitions drawn from palgebra/reference and key artifacts; review when we add new terms. All in favor?

**Maya:** Aye (conditional). **Frankie:** Aye. **Joe:** Aye. **Vic:** Aye. **Tammy:** Aye.

---

## Final Consensus

- **Motion:** Aye. Add minimal glossary (5–10 terms), README or linked doc, source of truth = palgebra + artifacts; review on new terms.
- **Status:** DELIBERATION COMPLETE.

---

## KEY TENSIONS IDENTIFIED
- **Visibility vs. maintenance:** README = visible but longer; dedicated doc = one place to update.
- **Redundancy:** Palgebra already defines terms; glossary would duplicate or summarize.

## ASSUMPTIONS SURFACED
- That a glossary reduces friction (Frankie, Tammy); Maya and Joe worried about staleness.
- That we can tie glossary to a single source of truth (Joe, Maya).

## RECOMMENDED NEXT STEPS
- Draft 5–10 terms with one-line definitions and links. Decide README vs. dedicated doc in implementation.
