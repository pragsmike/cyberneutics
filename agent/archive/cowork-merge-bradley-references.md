# Task: Merge Bradley-Cyberneutics References into References Directory

## Context

`references/bradley-cyberneutics-references.md` contains 28 papers compiled
from a conversation about Tai-Danae Bradley's magnitude paper and its
connections to the cyberneutics categorifications. Of the 28, 17 are already
cited somewhere in the repository (palgebra docs, references/README.md, or
research-survey.md). 11 are new.

The file marks each paper as ✓ (already cited) or **NEW** with a priority
level (high, medium, low).

## What to do

1. **Read** `references/README.md` to understand the existing section
   structure (organized by theoretical tradition: Narrative & Cognition,
   Cybernetics, Category Theory & Formalism, etc.).

2. **Read** `references/bradley-cyberneutics-references.md` for the full
   list with annotations and priority markings.

3. **For each NEW paper**, add it to the appropriate section of
   `references/README.md` following the existing format:
   - Bold author name, title in italics or quotes, publication venue, year.
   - Em-dash annotation explaining relevance to cyberneutics.
   - "Cited in:" pointer to the repository file(s) where it's referenced
     (for new papers not yet cited elsewhere, use
     `references/bradley-cyberneutics-references.md` as the citation source
     and note that the connection is documented in
     `wild/diary/2026-03-22-bradley-magnitude-tropical.md`).

4. **For each ✓ paper already in references/README.md**, check whether the
   annotation in bradley-cyberneutics-references.md adds information not
   currently in the README entry. If so, enrich the existing annotation.
   Do not duplicate entries.

5. **For ✓ papers cited in palgebra docs but NOT in references/README.md**,
   add them to references/README.md. The references README is supposed to
   be the master bibliography — everything cited anywhere should appear there.

6. **Section placement guidance** for the new papers:
   - Bradley's own papers (items 1–8): Create a new subsection under
     "Category Theory & Formalism" called "Language, Enrichment, and
     Magnitude" or similar. These form a coherent arc and should be grouped.
   - Leinster, Leinster-Shulman, Vigneaux, Willerton (items 11–14):
     Place in "Category Theory & Formalism" near existing Leinster, Kelly,
     Lawvere entries.
   - Vlassopoulos-Gaubert tropical paper (item 25): Place in "Category
     Theory & Formalism" with a note about the tropical/min-lattice
     connection.
   - Vickers-Faith-Rossiter semiotics paper (not in the Bradley list but
     mentioned in the diary entry — arXiv:1311.4376): Add to a new
     subsection "Semiotics & Visualization" or place under an existing
     section that fits. This paper connects Peircean/Saussurean semiotics
     to category theory via commutative diagrams.

7. **Do not modify** bradley-cyberneutics-references.md itself — it serves
   as a standalone companion document to the diary entry.

## Verification

After merging, confirm:
- No duplicate entries in references/README.md
- All 11 NEW papers from the Bradley list appear in references/README.md
- All ✓ papers that were in palgebra docs but missing from references/README.md
  have been added
- The Vickers-Faith-Rossiter semiotics paper has been added
- Section headings are consistent with existing style
