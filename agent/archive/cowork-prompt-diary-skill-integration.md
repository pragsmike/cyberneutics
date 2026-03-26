# Task: Integrate diary skill and related files from 2026-03-26 conversation

## Context

A conversation in Claude Chat produced three files that need to be placed in the repo and integrated with existing infrastructure. The files are in the project's uploaded files or outputs. You need to find them, review them, place them correctly, and wire them into the repo's discovery mechanisms.

## Read first

1. `agent/onboarding-core.md` — understand the repo structure and skill discovery model
2. `.claude/skills/handoff/SKILL.md` — understand skill file format conventions by example
3. `.claude/skills/committee/SKILL.md` — another example of skill format and structure
4. `wild/diary/README.md` — understand the diary's current documentation
5. `CONTRIBUTING.md` — check for consistency with any changes you make

## Files to place

### 1. Diary authoring skill → `.claude/skills/diary/SKILL.md`

**Source**: `SKILL-diary.md` in uploaded files or outputs.

**Actions**:
- Read the file carefully. Check that it is consistent with the format conventions used by other skills in `.claude/skills/`. Specifically check:
  - Does it have the right frontmatter style? Other skills don't use YAML frontmatter — they just start with a markdown heading. Adjust if needed.
  - Is the placement note at the top necessary or redundant once the file is in its correct location? Remove if it's just telling the reader where the file lives.
  - Does the "When to use" section clearly describe trigger conditions, consistent with how other skills describe theirs?
  - Are the conventions it documents actually consistent with existing diary entries? Spot-check against 2–3 entries in `wild/diary/` to verify.
  - Is anything missing that you'd want to know as an agent asked to write a diary entry?
  - Is anything over-specified that would constrain useful variation?
- Place the cleaned file at `.claude/skills/diary/SKILL.md`.

### 2. References file → `applications/narrative-immune-systems/references-choe-echo-chamber-studies.md`

**Source**: `references-choe-echo-chamber-studies.md` in uploaded files or outputs.

**Actions**:
- The diary entry's cross-references already point to `applications/narrative-immune-systems/references-choe-echo-chamber-studies.md`. Place the file there.
- Read the file. Check that cross-references to other repo files use correct relative paths from the new location. Fix any broken paths.
- Check that the file's header accurately describes what it contains.
- Do NOT add this file to any README index unless the directory's README has a pattern of listing individual reference files. Check first.

### 3. Diary entry → `wild/diary/2026-03-26-echo-chamber-immune-organs.md`

**Source**: `diary-2026-03-26-echo-chamber-immune-organs.md` in uploaded files or outputs.

**Actions**:
- Read the full entry. Check that:
  - Cross-references at the bottom use correct relative paths from `wild/diary/`.
  - The references file path matches where you actually placed file #2.
  - No individuals are named outside of published research citations (Bond et al., Kim et al., Simchon et al. are fine; no other names should appear).
  - No institutions are named in evaluative context (check for platform names — structural descriptions of behavior are fine, named judgments are not).
  - The "potentially novel contributions" block makes appropriately hedged claims (flagging for verification, not asserting confirmed novelty).
- Place the cleaned file at `wild/diary/2026-03-26-echo-chamber-immune-organs.md`.

## Integration tasks

After placing all three files:

### A. Update `agent/onboarding-core.md`

Find the skills inventory (the section that lists available skills like committee, scenarios, probe, review, handoff, string-diagram). Add a row for the diary skill:

- **Name**: diary
- **Location**: `.claude/skills/diary/SKILL.md`  
- **When to use**: Writing or drafting diary entries for `wild/diary/`
- **Trigger**: User asks to write, draft, or outline a diary entry; or conversation produces exploratory ideas that should be recorded

Match the format and level of detail used by adjacent rows.

### B. Consider a slash command wrapper

Check `.claude/commands/` for the pattern used by existing slash commands. If each command is a thin wrapper that points to a skill file, create `.claude/commands/diary.md` following the same pattern. If the command structure is more complex or there's a reason not to add one, skip this and note why.

### C. Verify cross-references are bidirectional where appropriate

The diary entry cross-references several files. Check whether any of those files have a pattern of back-referencing diary entries. If they do, add a back-reference. If they don't (which is expected — diary entries are upstream-only), don't add one. The skill file documents this convention; verify the entry follows it.

## Verification checklist

Before committing:

- [ ] `.claude/skills/diary/SKILL.md` exists and is consistent with other skill files in format
- [ ] `applications/narrative-immune-systems/references-choe-echo-chamber-studies.md` exists with correct internal paths
- [ ] `wild/diary/2026-03-26-echo-chamber-immune-organs.md` exists with correct cross-reference paths
- [ ] `agent/onboarding-core.md` has a diary skill row in its inventory
- [ ] No names of non-published individuals appear in any placed file
- [ ] No institutions are named in evaluative context in the diary entry
- [ ] Spot-check: the skill's conventions match what existing diary entries actually do (check at least `2026-03-15-emotional-attention-steering.md` and `2026-03-15-absent-parties-and-chameleons.md`)
- [ ] Run `py -3 scripts/lint_repo_docs.py` if it exists — confirm pass

## What NOT to do

- Do not rewrite the diary entry's content or analytical substance. You are checking paths, filters, and format — not editing the ideas.
- Do not add the diary entry or references file to any essay or main document. Diary entries are upstream only.
- Do not modify any existing diary entries to match the new skill's conventions. The skill was derived from existing entries, not the other way around.
- Do not create a handoff for this task unless the session involves other substantial work. This is a file-placement task, not a research session.
