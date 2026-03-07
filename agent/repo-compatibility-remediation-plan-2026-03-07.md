# Cross-Agent Compatibility and Documentation Remediation Plan

## Purpose

This plan captures the next cleanup session requested by mg on 2026-03-07:

- make the repo work cleanly with Claude Code, Codex, and Cursor without maintaining duplicate skill trees
- make onboarding explicitly exclude agent/archive/
- remove the stale agent/gap_analysis.md
- align all live documentation with the fact that skill outputs belong in external situation directories
- decide what checked-in historical deliberation/scenario records should become if they stay in the repo
- separate structural linting from the editorial-analysis prompt, which already owns some editorial/navigation linting

This is a plan only. It is meant to be executed in a later session.

## Compatibility Facts Verified On 2026-03-07

- Claude Code uses CLAUDE.md for repo instructions.
- Claude Code supports project skills in .claude/skills/.
- Claude Code uses .claude/commands/ for explicit slash commands.
- Codex uses AGENTS.md for repo instructions.
- Current Codex behavior in this environment does not auto-discover repo-local .Codex/skills/; the auto-listed skills come from installed $CODEX_HOME/skills.
- Cursor CLI reads root AGENTS.md and CLAUDE.md, and supports .cursor/rules/ and .cursor/commands/.

Implication: do not create a second full repo-local skill tree under .Codex/skills/. Keep one canonical skill body set and add only thin compatibility wrappers where a tool needs a different discovery surface.

## Problems To Correct

1. Onboarding drift
   - AGENTS.md and CLAUDE.md are near-copies and can drift independently.
   - They currently refer to agent/gap_analysis.md, which is stale and should be removed.
   - They do not state strongly enough that agent/archive/ is historical only.

2. Agent compatibility ambiguity
   - The repo mixes tool-specific assumptions.
   - AGENTS.md currently points at .Codex/skills/, which does not exist and should not be introduced as a duplicate.
   - The repo presents /committee-style UX, but the canonical repo artifacts currently live in .claude/skills/, not in tool-specific command wrappers.

3. Output location inconsistency
   - Live docs still claim outputs go to agent/scenarios/ and agent/deliberations/.
   - The current skills and config say outputs should go to external situation directories.

4. Operational/historical/example material is mixed together
   - agent/ currently contains live operational docs, historical archive, and checked-in example records.
   - agent/deliberations/ and agent/scenarios/ read like live output locations even though live output should be external.

5. State tracking is not single-sourced
   - agent/gap_analysis.md, handoffs, and other docs can disagree about what is done, blocked, or still current.

6. Index and navigation drift
   - Recent additions such as artifacts/category-theory-connection.md are not consistently indexed.
   - Some docs still reference outdated paths or outdated runtime conventions.

## Target End State

1. There is one canonical onboarding source and thin tool-specific entry points.
2. There is one canonical skill source.
3. No live doc claims that active outputs live under agent/.
4. agent/ contains operational repo metadata only: handoffs, rosters, prompts, diary, current plans.
5. agent/archive/ is explicitly marked historical only and excluded from onboarding/search unless historical provenance is requested.
6. Checked-in run records are clearly labeled examples or historical records, not implied live outputs.
7. Structural linting is automated separately from the editorial-analysis prompt.

## Recommended Architecture

### 1. Onboarding Instructions

Create a canonical onboarding source, for example:

- agent/onboarding-core.md

Then make the root entry points thin wrappers:

- AGENTS.md
- CLAUDE.md

Those wrappers should stay short and point to the same canonical content.

Minimum onboarding contract:

1. Read the latest handoff first.
2. Read the current cleanup/state doc.
3. Do not search agent/archive/ during onboarding. It is historical only.
4. If a task uses cyberneutics workflows, read the canonical skill doc in .claude/skills/<name>/SKILL.md.
5. Treat situation directories as the only live output location.

### 2. Skills and Commands

Use this compatibility model:

- Keep .claude/skills/ as the canonical skill source.
- Do not create .Codex/skills/.
- Add thin Claude wrappers in .claude/commands/ for explicit /committee, /scenarios, /probe, /review, /handoff, and /string-diagram UX.
- Add thin Cursor wrappers in .cursor/commands/ for the same commands.
- In AGENTS.md, instruct Codex to handle these workflows by reading the corresponding canonical skill doc from .claude/skills/ and following it manually.

This preserves one skill body per workflow while still supporting command discovery where the host tool expects it.

### 3. Output Locations

Treat this as canonical:

- live outputs: <situation-dir>/situation.md, <situation-dir>/scenarios/, <situation-dir>/deliberations/, <situation-dir>/probes/
- repo contents: methodology docs, prompts, rosters, curated examples, historical records

No live doc should describe agent/scenarios/ or agent/deliberations/ as the place new runs are written.

### 4. Checked-In Examples vs. Operational State

Move checked-in run records out of agent/.

Recommended destination:

- examples/ top-level if willing to add a neutral directory

Fallback destination if avoiding a new top-level directory:

- artifacts/examples/records/

Recommendation:

- move agent/deliberations/ to examples/deliberations/
- when touched, move agent/scenarios/ to examples/scenarios/

Rationale:

- agent/ should stop implying repo-local runtime output
- checked-in runs are examples or historical records, not active work product

### 5. State Tracking

Do not replace agent/gap_analysis.md with another omnibus stale list under agent/.

Instead create a narrower canonical state document, for example:

- meta/project-state.md

Suggested sections:

- current architecture truths
- current open decisions
- blocked items
- current compatibility migration status
- docs still needing sweep

Handoffs should then carry session deltas, not full backlog duplication.

## Execution Plan

### Phase 1: Establish Single Sources of Truth

Create or update:

- agent/onboarding-core.md
- meta/project-state.md
- AGENTS.md
- CLAUDE.md

Tasks:

- remove agent/gap_analysis.md
- remove all live onboarding references to it
- add the explicit agent/archive/ exclusion rule
- state that .claude/skills/ is canonical
- state that live outputs go to situation directories

### Phase 2: Add Compatibility Wrappers Without Duplicating Skill Bodies

Add:

- .claude/commands/committee.md
- .claude/commands/scenarios.md
- .claude/commands/probe.md
- .claude/commands/review.md
- .claude/commands/handoff.md
- .claude/commands/string-diagram.md
- .cursor/commands/committee.md
- .cursor/commands/scenarios.md
- .cursor/commands/probe.md
- .cursor/commands/review.md
- .cursor/commands/handoff.md
- .cursor/commands/string-diagram.md

Each wrapper should be short and do nothing except:

- identify the workflow
- tell the tool to read .claude/skills/<name>/SKILL.md
- tell it to follow that workflow

Do not copy the full skill body into command wrappers.

### Phase 3: Sweep Live Docs To Situation Directories

Update all live docs that still point to agent/scenarios/ or agent/deliberations/.

Known files to update:

- README.md
- AGENTS.md
- CLAUDE.md
- artifacts/README.md
- artifacts/quick-start-guide.md
- artifacts/start-here.md
- artifacts/deliberated-choice-workflow.md
- artifacts/scenario-generation.md
- artifacts/independent-evaluation.md
- artifacts/examples/full-pipeline-worked-example.md
- meta/repository-review-and-run-guide.md
- essays/when-methodology-fails.md
- research-programs/README.md

Rules for the sweep:

- use <situation-dir>/... in generic docs
- use --situation <path> examples where concrete commands help
- keep repo-checked examples labeled as examples, not as default runtime locations

### Phase 4: Move Checked-In Records Out Of agent/

Move:

- agent/deliberations/ -> examples/deliberations/ or artifacts/examples/records/deliberations/

When feasible in the same sweep:

- agent/scenarios/ -> examples/scenarios/ or artifacts/examples/records/scenarios/

Then update inbound links from:

- artifacts/examples/full-pipeline-worked-example.md
- essays/when-methodology-fails.md
- any remaining live docs referencing the old locations

Do not rewrite agent/archive/ contents to match new paths. If historical clarification is needed, add top-level notes or live-doc pointers instead of rewriting archival provenance.

### Phase 5: Clean Up Indexes and Naming

Update indexes so recent and moved docs are discoverable:

- add artifacts/category-theory-connection.md to artifacts/README.md
- update any index that still points to removed or moved docs
- make README language consistent about skills vs commands
- remove live references to nonexistent .Codex/skills/

### Phase 6: Add Structural Linting

Add a lightweight structural lint script, for example:

- scripts/lint_repo_docs.py

Checks should include:

- no live references to agent/gap_analysis.md
- onboarding docs include the agent/archive/ exclusion rule
- no live docs claim outputs are written to agent/scenarios/ or agent/deliberations/
- no live docs point to nonexistent .Codex/skills/
- every indexed artifact/essay/example exists
- newly added docs such as artifacts/category-theory-connection.md are indexed where appropriate

### Phase 7: Validate Without Duplicating Editorial Analysis

Use two distinct validation layers:

- Structural lint: links, paths, indexes, forbidden legacy references
- Editorial-analysis prompt: prose clarity, navigation quality, audience fit, conceptual coherence

Do not try to encode the full editorial-analysis prompt into the structural lint script.

## Acceptance Criteria

The migration is complete when all of the following are true:

- agent/gap_analysis.md is gone
- root onboarding docs say not to search agent/archive/ during onboarding
- AGENTS.md no longer points to .Codex/skills/
- canonical skill bodies exist only once, under .claude/skills/
- Claude and Cursor have thin command wrappers, not duplicated skill bodies
- live docs describe situation directories as the runtime output location
- checked-in run records are no longer presented as live outputs under agent/
- live-doc grep for agent/scenarios/, agent/deliberations/, .Codex/skills/, and gap_analysis.md is clean
- structural lint passes
- editorial-analysis prompt passes with no major navigation/findability findings

## Recommended Order Of Operations

1. Create the new canonical onboarding/state docs first.
2. Update AGENTS.md and CLAUDE.md.
3. Add command wrappers for Claude and Cursor.
4. Sweep live docs to situation directories.
5. Move checked-in records out of agent/.
6. Fix indexes and naming drift.
7. Add and run structural lint.
8. Run editorial-analysis after the structural sweep is complete.

## Explicit Non-Goals

- Do not create a repo-local .Codex/skills/ mirror.
- Do not rewrite agent/archive/ documents to modernize historical paths.
- Do not let agent/ continue to function as both active runtime output and historical storage.
- Do not duplicate editorial-analysis logic inside a path/link linter.
