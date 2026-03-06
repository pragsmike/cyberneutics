# Phase 2: Deliberation

**Topic:** Should we add a short "When not to use this methodology" section to the README (e.g. don't use for X, Y, Z) even if it might make the project look narrow or defensive?  
**Protocol:** Robert's Rules; adversarial engagement.

---

## Opening Statements

### Maya

Adding "when not to use" can read as defensive or insecure. Competent projects don't lead with "here's where we're not good." The political risk is that we signal smallness — we're so worried about misuse we're preemptively narrowing. That said, if we *don't* set scope, we get blamed when someone uses the methodology for high-stakes binary decisions and gets a false sense of rigor. So I'm torn. I'd support a short section *if* it's framed as "scope and limits" not "don't use us for these things" — same content, different tone. Confidence is medium: tone matters more than yes/no.

### Frankie

We should add it. Honesty about scope is a value. If the methodology has limits — and it does — saying so is integrity, not defensiveness. "When not to use" is standard in good documentation: it respects the user's time and prevents misapplication. The failure mode isn't looking narrow; it's letting someone run a committee on a decision that needs a different tool and then blaming us. I'm high confidence: this is the right thing to do. Frame it as "best used for X; less suitable for Y" so it's positive scope-setting, not a list of don'ts.

### Joe

Precedent: many methodologies add "limitations" or "when this isn't the right tool." The failure-modes essay already does something similar. So we're not inventing a new genre. The question is whether the README is the right place. README is the front door; putting "when not to use" there might make the first impression negative. Alternative: keep README aspirational, put "when not to use" in the failure-modes doc or a dedicated "Scope and limits" artifact, link from README. I'm Aye for the content, Nay for README as the primary home — or Aye for a one-paragraph README summary with "for more see [link]." So conditional Aye.

### Vic

What misuse are we trying to prevent? I don't have data on how the methodology is being misapplied. If we're adding "when not to use" on principle, that's fine — but then we're not evidence-based, we're hypothesis-based. The hypothesis is: stating limits reduces misuse and builds trust. I can support that. I'd want the section to be concrete: not "don't use for trivial decisions" (vague) but "designed for decisions with genuine uncertainty and competing values; less suitable for purely technical or already-settled choices." So Aye, with the condition that the section is specific and falsifiable. Confidence low: we're guessing that this helps.

### Tammy

From a systems view, "when not to use" is a boundary definition. It shapes who enters and how. Without it, the boundary is undefined — users infer from context, and we get a wider spread of applications, some good and some bad. With it, we narrow the funnel but clarify the value proposition. The second-order effect: a clear boundary can *increase* adoption among the right users (they know we're serious) and decrease misuse. So I'm Aye. I'm medium confidence because the magnitude of the effect is unknown — but the direction (boundary clarity) is right.

---

## Initial Positions Summary

| Member  | Stance | Confidence | Key Concern |
|---------|--------|------------|-------------|
| Maya    | Aye (conditional) | 2 | Tone: "scope and limits" not "don't use" |
| Frankie | Aye    | 4          | Honesty about scope is values-aligned |
| Joe     | Aye (conditional) | 2 | Content yes; README primary home no — or one para + link |
| Vic     | Aye (conditional) | 1 | Make section concrete; we're guessing it helps |
| Tammy   | Aye    | 3          | Boundary definition; direction right, magnitude unknown |

---

## Key Tensions Identified

1. **Tone:** "When not to use" (negative) vs. "Scope and limits" (positive) — Maya, Frankie.
2. **Placement:** README front and center vs. linked artifact — Joe.
3. **Specificity:** Vague vs. concrete, falsifiable limits — Vic.
4. **Evidence:** No data on misuse; principle-based decision — Vic.

---

## Round 1

**Chair:** All five are Aye or conditional Aye. No Nays. So the question is conditions. Maya: tone. Joe: placement. Vic: specificity. Tammy and Frankie: Aye with good framing.

**Maya:** I'll drop to unqualified Aye if we agree the section is titled "Scope and limits" or "Best used for" and leads with what the methodology *is* for, then "less suitable for X, Y, Z." That's positive framing. So Aye with that condition.

**Joe:** I'll support README inclusion if it's one short paragraph plus "for more see [failure-modes or scope doc]." Don't put a long list in the README. So Aye: one para in README, detail elsewhere.

**Vic:** I need the "less suitable for" items to be specific. Not "trivial decisions" but "decisions with no genuine uncertainty or competing values." Not "when you need a single answer" but "when the decision is already made and you want post-hoc justification." So Aye with specificity condition. I'm still low confidence — we're not evidence-based here.

**Frankie:** I'm fine with "Scope and limits" framing and one paragraph + link. That's consistent with honesty. Aye.

**Tammy:** Agreed. One para, positive framing, link to detail. Aye.

---

## Round 1 Analysis

Unanimous Aye with shared conditions: (1) positive framing ("Scope and limits" or "Best used for"), (2) one short paragraph in README + link to more, (3) concrete "less suitable for" criteria. Resolution: PASSED, implementation plan captures conditions.

---

## Round 2

**Chair:** Motion: Add a short "Scope and limits" (or "Best used for") paragraph to the README stating what the methodology is best used for and 2–3 concrete "less suitable for" cases; link to failure-modes or a dedicated scope doc for detail. All in favor?

**Maya:** Aye.  
**Frankie:** Aye.  
**Joe:** Aye.  
**Vic:** Aye.  
**Tammy:** Aye.

**Chair:** Motion passes 5–0. Resolution: Aye, unanimous.

---

## Final Consensus

- **Motion:** Add one short "Scope and limits" paragraph to README; concrete "less suitable for" items; link to detail.
- **Status:** DELIBERATION COMPLETE.
- **Votes:** Maya Aye (3), Frankie Aye (4), Joe Aye (3), Vic Aye (2), Tammy Aye (3).

---

## KEY TENSIONS IDENTIFIED

- **Tone:** Negative ("when not to use") vs. positive ("scope and limits") — resolved with positive framing.
- **Placement:** README vs. linked doc — resolved with one para + link.
- **Specificity:** Concrete criteria (Vic) agreed.

## ASSUMPTIONS SURFACED

- That stating limits builds trust (Frankie, Tammy); Vic noted no evidence.
- That README is the right place for one paragraph (Joe accepted with link).
- That positive framing avoids defensiveness (Maya).

## EVIDENCE REQUIREMENTS

- None specified; decision was principle-based. Optional: track whether scope section reduces misapplication.

## DECISION SPACE MAP

- **Optimize for integrity:** Aye, state limits (Frankie).
- **Optimize for optics:** Aye with positive framing (Maya).
- **Optimize for structure:** One para + link (Joe).
- **Optimize for clarity:** Concrete criteria (Vic).
- **Resolution:** Unanimous Aye with implementation plan.

## RECOMMENDED NEXT STEPS

- Draft "Scope and limits" paragraph with 2–3 concrete "less suitable for" items.
- Add link to failure-modes essay or dedicated scope doc.
- Optionally revisit after feedback or usage.
