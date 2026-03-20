---
name: handoff
description: >
  Generate a session handoff document for successor agents. Use when the user
  types '/handoff' or asks to create a handoff. Reads the previous handoff (if any)
  for continuity, generates a new handoff with today's date, saves it to agent/,
  and archives the previous one to agent/archive/.
---

# Handoff Skill

Generate effective session handoff documents that enable successor agents to
continue work on this repository, avoiding pitfalls encountered and building
on lessons learned that aren't captured in formal documentation.

## When to use

- User types `/handoff`
- User asks to "create a handoff" or "write a handoff document"
- End of a significant work session when continuity matters
- After completing major milestones or before known breaks

## What the skill does

1. **Reads previous handoff** from `agent/handoff-[YYYY-MM-DD].md` (if exists) to understand trajectory and maintain continuity
2. **Analyzes current session** to extract:
   - What was accomplished
   - What mistakes were made and lessons learned
   - What dead ends were explored
   - Current state of work (completed, in-progress, blocked)
   - Observations about mg's working style and preferences
   - Immediate next steps for successor
3. **Generates new handoff** following the structured template
4. **Saves** as `agent/handoff-[TODAY].md`
5. **Archives previous** handoff to `agent/archive/handoff-[OLD-DATE].md`
6. **Updates `meta/project-state.md`** — add a brief entry to the "Recent changes" section noting what was accomplished this session. This keeps project-state current for successor agents who read it during onboarding step 2.

All steps happen automatically without confirmation prompts.

## Handoff document structure

The generated handoff follows this structure:

### Session Summary
- Duration and main accomplishments
- Original intent vs. actual outcome
- Key deliverables

### Mistakes and Lessons
- Specific mistakes made during session
- Root causes and how to avoid them
- Concrete examples

### Dead Ends Explored
- Approaches that didn't work and why
- What was learned from failures
- Conditions under which they might be worth revisiting

### Current State
- Completed this session
- In progress (with blockers)
- Not yet started but planned

### Immediate Next Steps
- Prioritized, actionable tasks
- Context for why each is ready
- Dependencies and blockers

### Working with mg: Session-Specific Insights
- Communication patterns observed
- Decision-making process
- Preferences and style
- What signals indicate what states

### Open Questions and Decisions Needed
- Questions requiring mg's input
- Topics needing research/exploration

### Technical Notes
- Repository structure quirks
- Tools and workflow notes
- File management approach

### Watch-Outs for Successor
- Tasks that seem simple but aren't
- Hidden dependencies
- Quality standards

### Theoretical/Conceptual Notes
- Key insights from session
- Unresolved tensions
- How understanding evolved

### What Worked Well / What To Do Differently
- Collaboration patterns that were productive
- Process improvements needed
- Communication adjustments

### Context for Specific Files
- File-by-file notes on status, quirks, dependencies

### Session Metadata
- Agent, date, mg's goals
- Continuation priority

## Key principles for generation

1. **Be specific**: "File Y has hidden dependency on Z because of reason R" not "Watch out for X"

2. **Capture the invisible**: What seemed obvious in context but won't be obvious to successor?

3. **Save time**: What would you want to know picking this up fresh? What did you learn the hard way?

4. **Be honest**: Mistakes and dead ends are valuable intelligence

5. **Think forward**: What enables successor to maintain momentum vs. starting from scratch?

6. **Prioritize ruthlessly**: Focus on what materially affects successor's effectiveness

7. **Maintain narrative continuity**: Reference previous handoff observations—did predicted issues materialize? Did recommended approaches work? What trajectory is the work following?

## Example bad vs. good entries

**Bad**: "Be careful with the evaluation rubrics"
- Not specific, not actionable

**Good**: "The evaluation-rubrics-reference.md has examples that reference other artifacts. If you change artifact names/structure, those examples need updating too. Caught this when we moved files and examples broke."
- Specific, explains why it matters, gives concrete scenario

**Bad**: "mg prefers good documentation"
- Everyone prefers good documentation, this says nothing

**Good**: "mg prefers examples over abstract explanation. When explaining theoretical concepts, noticed engagement increased significantly when we included concrete transcripts/examples rather than just describing patterns. The Dervin essay worked well because it had the 'strategic decision' example near the end."
- Specific observation, actionable pattern, concrete instance

**Bad**: "Some essays still need to be written"
- Obvious from essays/README.md already

**Good**: "Essay 02 (From Practice to Theory) is marked 'coming soon' but mg hasn't articulated what should be in it beyond title. Before writing, confirm: does this document the historical development of the methodology, or is it about explaining why practical techniques work? Those are different essays."
- Identifies real ambiguity, suggests clarifying question, prevents wasted effort

## Implementation notes

**File naming**: `handoff-YYYY-MM-DD.md` using today's date (2026-02-16 format)

**Archive location**: `agent/archive/` — ensure directory exists before moving files

**Reading previous handoff**: If multiple handoffs exist in agent/, read the most recent (by date in filename). Don't read from archive/ — those are historical.

**Continuity narrative**: The handoff should note:
- What the previous handoff predicted/recommended
- Whether those predictions were accurate
- What trajectory the work is following
- Evolution of understanding about mg's preferences
- Patterns that are becoming clearer over multiple sessions

**No redundancy**: Don't repeat what's already in repository documentation. The handoff is for meta-context, session-specific intelligence, and invisible knowledge.

**Tone**: Direct, practical, specific. Written for another AI agent picking up the work. Be frank about mistakes and unknowns.

## Usage

When user types `/handoff`, simply execute the skill:
1. Read `agent/handoff-*.md` (most recent if multiple)
2. Analyze the current session transcript
3. Generate comprehensive handoff document
4. Save as `agent/handoff-[TODAY].md`
5. Move previous handoff to `agent/archive/`
6. Update `meta/project-state.md` "Recent changes" section with this session's accomplishments
7. Confirm completion: "Handoff document created: agent/handoff-[TODAY].md (previous handoff archived, project-state updated)"

No intermediate confirmations or reviews—generate and save directly.
