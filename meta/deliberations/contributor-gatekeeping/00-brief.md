# The Contributor Gatekeeping Problem: Committee Brief

**Purpose**: This document summarizes a known problem with the contributor
experience in the Cyberneutics repository, identifies the specific files and
passages where the problem manifests, and poses a prompt for a committee
deliberation to remedy it. It is intended to be read alongside the relevant
files before convening.

---

## The Problem

The contributor documentation was designed to provide structure — clear
placement rules, conventions, and routing — primarily to enable agents to
operate cleanly within the repository. This was a legitimate goal. Agents
do need explicit rules; ambiguity causes drift.

The unintended consequence is that the documentation reads as a contract
more than an invitation. The framing is correctness-oriented: what belongs
where, what must be present before a PR, what the structural invariants
are. What is absent is any acknowledgment that contributors may arrive
with ideas that are not yet fully formed, and that this is not a defect.

The real-world signal: a contributor submitted a pull request containing
an essay that reasoned about software engineering in the agent era from an
external theoretical perspective. The essay had genuine intellectual merit
and connected to existing threads in the repository. The contributor then
closed their own PR, citing the contributor guidelines. The conversation
never happened. The idea walked out the door.

This is the failure mode in concrete form. The guidelines functioned as a
wall at precisely the moment they should have functioned as a door.

---

## How It Arose

The contributor documentation was built by agents, for agents, during a
session focused on improving "contributor routing." The session chose
additive layering as its strategy and produced a routing system that is
structurally coherent. The problem is not that the system is wrong — it
is that it optimizes for one contributor type (structured, technically
prepared, arriving with a complete artifact) and has no path for another
type (lateral thinker, arriving with a connection or half-formed idea).

The `wild/` directory exists and is described as the home for "incoming
ideas and external material not yet integrated." But it is not mentioned
in any contributor-facing document as an explicit on-ramp. A contributor
reading `CONTRIBUTING.md` or `meta/contributor-guide.md` would not know
that `wild/` exists or that it is an appropriate destination for
exploratory work.

The `wild/diary` directory, meanwhile, is described as even more exploratory
than other directories in `wild/` — "unstructured, highly speculative, field
notes." But it had been located inside `agent/`, which signaled that it is
operational infrastructure for automated agents. Its actual purpose is closer to
a working notebook: a place where ideas swirl before they are tamed. Moving it
to `wild/` aligned its location with purpose.  That move is done, but there may be lingering references to its old location that must be updated.

---

## Where the Troubled Material Lives

The following files contain the passages that need revision or
supplementation. The committee should read these before deliberating.

| File | Issue |
|------|-------|
| `CONTRIBUTING.md` | Framed as a "compact contribution contract." No mention of `wild/`. No path for exploratory or early-stage contributions. Tone is correctness-oriented. |
| `meta/contributor-guide.md` | Intent-based routing table ("I want to... → Start here") has no row for "I have a half-formed idea / lateral connection." The table implicitly requires the contributor to already know what kind of artifact they have. |
| `research-programs/README.md` | Contains a preflight checklist that is appropriate for structured research programs but will read as gatekeeping to someone arriving with a partial idea. No scope note clarifying that the checklist applies only to research programs. |
| `agent/onboarding-core.md` | Describes `wild/` as "incoming ideas and external material" but this description is in agent onboarding, not contributor-facing docs. The routing is invisible to human contributors. |
| `wild/diary/README.md` | Describes the diary as more exploratory than `wild/`, and describes a pipeline from diary → `wild/` → formalization. This is the right model, but it had been buried in `agent/` where contributors won't find it. now it's in `wild/` but documents must be updated to point there.|

The `agent/rubrics/repo-audience-experience.md` rubric scores the repo on
audience paths, actionability, and delight — but does not include
contributors as a scored audience. This may be appropriate given that the
rubric is for readers, not contributors. The committee should consider
whether a parallel rubric for contributor experience is warranted, or
whether the fix is simpler: revising the existing documents listed above.

---

## What Is Already Good

The routing system is structurally sound. The five contribution types in
`CONTRIBUTING.md` are accurate. The `meta/contributor-guide.md`
intent-based table is the right idea. The `wild/` directory is already
well-established and has a clear character. The diary-to-wild pipeline
already exists as a practice, even if it is undocumented in
contributor-facing surfaces.

The committee should not redesign the system. It should extend it to
serve a second contributor type.

---

## Prompt for the Committee

**Situation**: The Cyberneutics repository's contributor documentation
inadvertently gatekeeps lateral, exploratory contributions while
successfully serving structured, technically-prepared ones. A real
contributor self-selected out after reading the guidelines. The `wild/`
directory is the natural home for early-stage ideas but is invisible to
contributors. The diary directory (now at `wild/diary/`) was previously
mislocated inside `agent/` relative to its actual purpose; that move is
done. The problem is not structural complexity but a missing on-ramp.

**Question for deliberation**: How should the contributor documentation
be revised — and how should the repository structure be adjusted — to
make it unambiguously clear that early-stage, exploratory, and lateral
contributions are genuinely welcome, without degrading the structural
clarity that agents and structured contributors depend on?

**Constraints the committee must respect**:
- Do not bloat `README.md` or collapse differentiated audience paths
- Do not degrade the structural conventions that agents use
- Changes should be additive or clarifying, not wholesale rewrites
- The `wild/` on-ramp must be visible from contributor-facing docs
- The fix must work for both human contributors and agent contributors

**Evidence the committee should weigh**:
- One contributor self-selected out after reading the guidelines
- The `wild/` directory has precedent: neo-cybernetics, residuality
  theory, harness engineering, software factories — all started there
- The diary README already describes the diary→wild→formalization
  pipeline; this model is sound and just needs surfacing
- The repo's own methodology was developed through exploratory lateral
  walks, not structured research programs; the contribution model should
  reflect that

**Dimensions of disagreement the committee should surface**:
- How much do you relax structure before agents start producing drift?
- Should `wild/` submissions require any conventions at all, or be
  explicitly convention-free?  mg will vet them but is biased toward innovation.
- Does a second routing tier (structured vs. exploratory) require a
  second rubric, or does the existing audience-experience rubric cover it?
