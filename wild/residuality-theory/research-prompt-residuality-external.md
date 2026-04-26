---
title: "Research-agent prompt: External grounding for residuality-theory survey"
type: research-prompt
audience: "A research agent (general-purpose / web-research) tasked with finding material outside this repository"
created: 2026-04-26
purpose: "Gather O'Reilly's PhD thesis, reviews of Residues (2024), and adjacent grounding material to feed into book-integration-plan.md Phase 0"
---

# Research-agent prompt

Copy the section below verbatim into a research agent. The agent should produce a single research report in markdown, not modify any files in this repository.

---

## Prompt to the research agent

You are researching Barry M. O'Reilly's body of work on **Residuality Theory** in software architecture. Your job is to gather external material that we cannot find by reading the local repository, and to report it back in a single markdown document. Do not modify any files. Do not infer or speculate beyond what you can cite.

### Background you need

Barry M. O'Reilly is a software architect and consultant who has published a series of papers on Residuality Theory through *Procedia Computer Science* (2019, 2020, 2021, 2022, 2023), one journal piece in MDPI's *Philosophies* (2021), and a 2024 Leanpub book titled *Residues: Time, Change, and Uncertainty in Software Architecture*. He has spoken at NDC London 2024, NDC Oslo 2024, and several Cutter Consortium events. He has been associated with **Black Tulip Technology** (a consultancy) and at various times with consulting/research roles in continental Europe (the dedication of his book is to "Tanya O'Reilly," and the cover art is by his son "Alexander O'Reilly, aged 11"; minor biographical signals only). The book's June 2024 Introduction explicitly says: *"This work will culminate shortly in the form of a PhD thesis."* Affiliation has been hinted at as a Belgian or Dutch institution in talks but is not confirmed in the materials we have.

We do not have direct access to:
- His PhD thesis (announced as forthcoming June 2024)
- Reviews of *Residues* (2024) — known to exist; we only have secondhand "reception is mixed"
- The Cutter Consortium pieces from 2018, 2020, 2021 (paywalled; do not attempt to retrieve full text)
- The promised "longer version" of the *Residues* book

### What to find — three priorities

#### 1. O'Reilly's PhD thesis

- Search academic repositories (Google Scholar, ProQuest, OpenAIRE, DART-Europe, NARCIS, Belgian and Dutch university repositories, Trinity College Dublin, KU Leuven, TU Delft, University of Antwerp, Vrije Universiteit Brussel, any other plausible European institutions)
- Search by author name "Barry M. O'Reilly" or "Barry O'Reilly" combined with "residuality," "software architecture," "complexity," "hyperliminal," "attractor"
- Confirm: institution, supervisor(s), defence date, abstract, full-text availability, DOI or persistent URL
- If the thesis is not yet defended/published, find any conference presentations, working papers, preprints, or doctoral consortium submissions that may be precursors
- Note any academic affiliation past or present (university, research group, advisor relationship)

If you find the thesis: report bibliographic details, abstract, table of contents (if available), and link to any open-access version. Do not download or paste full text — note what is available and where.

#### 2. Reviews of *Residues* (2024)

- Search for reviews on Goodreads, Amazon, Leanpub itself, software-architecture blogs, InfoQ, IEEE Software, *Communications of the ACM*, the C2 wiki, Hacker News discussion threads, /r/softwarearchitecture and adjacent subreddits, LinkedIn longform posts by named software architects, Mastodon, Bluesky
- Look specifically for both **sympathetic** and **critical** reviews — we have heard reception is mixed but have not seen the actual reviews
- For each review found: capture reviewer name, venue, date, overall stance (positive / mixed / negative), and the *specific* points of praise or criticism (e.g., "praised for accessibility," "criticized for dismissing SOLID," "questioned falsifiability," "objected to anti-requirements stance")
- Particular value: any review that engages with O'Reilly's empirical-significance claim, his rejection of case studies, his treatment of resilience engineering, or his critique of Beer's VSM

If reviews are sparse, note that explicitly. Do not invent reviews.

#### 3. Adjacent grounding material

In rough order of value:

- **Cited statistical-significance experiments.** The 2024 book claims "experiments carried out thus far have revealed a statistically significant effect." Find the underlying study. Likely candidates: a Procedia paper we may have missed, a conference talk reporting empirical results, a doctoral-consortium submission, a chapter of the (forthcoming) thesis available as preprint. Confirm whether the empirical claim is published or unpublished as of search date.
- **The promised "longer version" of the book.** The book's Conclusion says "In the near future a longer version will appear." Has it appeared? Where? Same Leanpub? A traditional publisher?
- **The 2018 Cutter "No More Snake Oil"**, the 2020 *There Is No Spoon* compilation, and the 2021 *Hyperliminal Coupling* Cutter pieces. We know these are paywalled; we are not asking you to retrieve full text. We are asking you to confirm publication metadata, year, length, and any open-access excerpts or summaries that exist.
- **Talks and podcasts** beyond the two NDC 2024 talks we already know about. Specifically: any Boundaryless podcast episodes (one is referenced in our chronology, may be others); any GOTO; any QCon; any DDD Europe; any Software Architecture Summit; any Domain-Driven Design conference; any Wardley-mapping community appearances. For each: title, venue, date, link, brief one-paragraph description.
- **Workshops, masterclasses, or training material.** O'Reilly has run residuality workshops; if any have public outlines or syllabi, these reveal the practitioner-pitched compression of the methodology.
- **Other people writing about residuality theory.** Eric Normand's Substack essay (May 2024) is the one we have. Are there others? Specifically: practitioners attempting to *use* residuality on real systems and reporting results. Any blog posts, conference talks, or writeups by people who are not O'Reilly.
- **Adjacent academic literature** that cites O'Reilly's residuality papers. Use Google Scholar or Semantic Scholar to find papers citing *Residuality Theory, Random Simulation, and Attractor Networks* (2022) and *The Machine in the Ghost* (2021). Note any paper that builds on, criticises, or extends residuality. Particular value: any work that engages residuality from complexity-science, software-architecture, or philosophy-of-engineering angles.
- **Any published engagement between O'Reilly and Ralph Stacey's work.** O'Reilly cites Stacey but has not (per the materials we have) engaged at depth. Has he published anything specifically on the Stacey connection? Has any reviewer made the connection? (We are independently planning to read Stacey directly; this is just to know what's already been done.)
- **Any indication of an O'Reilly position on the assemblage / rhizome / nomadic-distribution concepts from Deleuze and Guattari's *A Thousand Plateaus*.** We have observed that O'Reilly cites Deleuze's *Difference and Repetition* (the walk metaphor) but never invokes the *Mille Plateaux* concepts explicitly. We are interested in whether he has *anywhere* — in a talk, podcast, blog post, comment, social-media reply — engaged with assemblage, rhizome, or nomadism. Negative results are valuable here too. If you find no such engagement, say so explicitly.

### Output format

A single markdown document, structured as:

```
# External research on residuality theory (YYYY-MM-DD)

## 1. PhD thesis
[findings, with full citations]

## 2. Reviews of Residues (2024)
[findings, sympathetic and critical, with citation, date, venue, stance, specific points]

## 3. Adjacent grounding material
### 3a. Statistical-significance experiments
### 3b. Longer-version book
### 3c. Cutter pieces (paywalled — metadata only)
### 3d. Talks and podcasts
### 3e. Workshops and training
### 3f. Other people writing about residuality
### 3g. Adjacent academic citations
### 3h. Stacey engagement
### 3i. Mille Plateaux engagement (negative results valuable)

## 4. Open questions and gaps
[anything you searched for and did not find; anything that warrants follow-up]

## 5. Source notes
[search strategies that worked; search strategies that did not; any sources whose reliability is unclear]
```

### Constraints

- **Cite everything.** Every claim should have a URL or full bibliographic citation. If you cannot cite, do not state.
- **Do not paraphrase reviews into your own voice.** Either quote briefly or summarise with attribution. Reviews are themselves data; their phrasing matters.
- **Do not retrieve paywalled full text.** Note paywall, capture metadata, move on.
- **Negative results count.** "Searched X databases under Y queries, found nothing" is a useful finding. Do not pad.
- **No speculation about O'Reilly's intentions, beliefs, or biography beyond what is publicly stated.**
- **Word budget**: aim for under 3000 words in the report. Use links rather than block quotes. The goal is a navigable index, not a literature review.

### When done

Return the markdown document as your single response. We will integrate selected findings into `state-of-residuality-2026.md` and `residuality-bibliography.md` per the plan in `book-integration-plan.md` Phase 0 → Phases 3, 4, 5.
