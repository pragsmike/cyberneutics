---
name: diary
description: >
  Write diary entries for wild/diary/ — the repo's rawest exploratory record.
  Entries capture ideas from conversations in connected prose with cross-references,
  open questions, and public-facing privacy filters. Use when the user types
  '/diary' or asks to write a diary entry, or when a conversation produces
  exploratory ideas that should be recorded.
---

# Diary Entry Authoring

## When to use

Use this skill when asked to write, draft, or outline a diary entry for `wild/diary/`. Diary entries are the primary record of exploratory conversations — ideas developed in real-time that may later feed into essays, research programs, or formal work. They are public-facing documents in the repository.

---

## File conventions

- **Location**: `wild/diary/`
- **Naming**: `YYYY-MM-DD-short-title.md` (date-prefixed, lowercase, hyphenated)
- **One file per idea session**. A single conversation may produce one entry. Multiple related conversations on the same day may share an entry or get separate entries — use judgment.

---

## Document structure

A diary entry has the following sections in this order:

### 1. Title and metadata block

```markdown
# Diary: [Descriptive Title]

**Date:** YYYY-MM-DD

**Context:** [2–4 sentences. What prompted this exploration — a conversation, a paper, an external article, a repo issue. Enough for a reader encountering this entry cold to understand why it exists and what question it addresses.]
```

If the entry contains ideas that appear to be novel contributions (not previously encountered in the literature or the repo), add a **Potentially novel contributions** block after the context paragraph. Number each contribution with a 1–2 sentence summary of what is claimed and why it might be new. This block serves as a flag for future verification — "novel" means "we haven't seen this elsewhere," not "we've confirmed no one has done this." Frame accordingly.

### 2. Body sections

Numbered thematic sections, each with a descriptive heading. No "Section N:" prefix — just the heading.

Conventions for body prose:

- **Write in connected prose, not bullet lists.** Diary entries are narrative, not outlines. Use paragraphs. Lists are acceptable only for genuinely enumerated items (e.g., "three candidate implementations").
- **Develop one idea per section.** Each section should be 2–6 paragraphs. If a section exceeds this, it probably contains two ideas and should be split.
- **Show the reasoning, not just the conclusion.** The diary records how an idea developed, including the intermediate steps, the analogies that worked, and the ones that didn't. A diary entry that states only conclusions is a summary, not a diary.
- **Include worked examples where the idea is novel or non-obvious.** If a section introduces a new distinction (e.g., a new discrimination signal, a new topology), show it applied to a concrete case.

### 3. Open questions

A section titled `## Open Questions` near the end. These are genuine unknowns surfaced by the exploration — not rhetorical questions and not disguised claims. Each question should be specific enough that someone could investigate it. Include failure modes and adversarial cases where relevant.

### 4. Cross-references

A final italic line listing related files in the repo using relative paths:

```markdown
*Cross-references: path/to/file.md, path/to/other-file.md, ...*
```

Include only files that are genuinely connected — not every file that touches a shared keyword. The reader should be able to follow any cross-reference and find material that directly extends or grounds the diary entry's ideas.

---

## Public-facing filters

Diary entries are in a public repository. Apply these filters:

- **No identifiable individuals.** Do not name people discussed in conversation. Use role descriptions: "a practitioner with experience in X," "a computational social scientist," "the platform operator." Named researchers are acceptable only when citing their published work (e.g., "Bond et al. (2012)").
- **No identifiable institutions** in editorial or evaluative context. Published institutional research can be cited normally. Do not name institutions when making judgments about their behavior — describe the behavior structurally instead ("a platform that removed its fact-checking infrastructure").
- **Neutral judgments.** The diary analyzes structures, not motives. "The architecture lacks a feedback mechanism" is appropriate. "The author failed to consider X" is not. When evaluating external work, focus on structural properties (what is present, what is missing, what follows from the design) rather than quality judgments about the author.
- **Associative register.** The diary's voice is analytical but not formal — closer to a working notebook than a published paper. Technical precision is expected; academic hedging is not. State what you think is true and flag what is uncertain, without burying claims in qualifications.

---

## Relationship to other artifacts

- Diary entries are **upstream** of everything else. Ideas that survive develop into `wild/` topic directories, then into essays or research programs. The diary is the rawest form of recorded thinking in the repo.
- Diary entries are **not** referenced by essays or main documents. If a diary idea makes it into an essay, the essay develops the idea independently and cites primary sources, not the diary. The diary may cross-reference downstream documents that developed its ideas, but not vice versa.
- Diary entries **do not** require a handoff, a deliberation, or maintainer approval. They are the lowest-barrier artifact in the repo. Write and commit.

---

## Common mistakes

- **Outline masquerading as diary entry.** If every section is 1–2 sentences, it's an outline, not an entry. Expand to connected prose or label it explicitly as an outline.
- **Missing context block.** A reader who encounters the entry without having been in the conversation needs enough context to follow. The context block is not optional.
- **Naming individuals from conversations.** The filters exist because the repo is public. Check before committing.
- **Treating cross-references as a bibliography.** Cross-references point to related repo files. Published works go in the body text or in a references section if warranted. Do not mix the two.
- **Omitting open questions.** If the exploration surfaced no genuine unknowns, the exploration was probably not pushing hard enough. Every diary entry should end with questions the author cannot yet answer.
