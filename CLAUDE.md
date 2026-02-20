# Working with Cyber-Sense: A Guide for AI Assistants

## What this repo is

Cyber-Sense is a methodology for working with LLMs as collaborative sense-making partners. It treats LLMs as **narrative engines** rather than answer machines and builds concrete techniques for rigorous exploration of problem spaces. The methodology is documented in essays (why), artifacts (how), and a formal algebra called palgebra (what, precisely). For a fuller orientation, read `README.md`.

## Before you do anything: session start

1. **Read the most recent handoff**: `agent/handoff-[YYYY-MM-DD].md` (pick the largest date). It captures current context, what was just worked on, open questions, and next steps. Skipping this loses continuity.
2. **Check `agent/gap_analysis.md`** for known gaps and planned documents.
3. **If a `/committee` deliberation is relevant**, look in `agent/deliberations/` for records of prior runs on related topics before starting a new one.

## Repository map

| Directory | Contains | Read when you need to… |
|-----------|----------|------------------------|
| `essays/` | Theoretical foundations | Understand *why* the methodology works. See `essays/README.md` for reading paths by audience (Practitioner, Theorist, Skeptic). |
| `artifacts/` | Techniques, templates, guides | Find a practical technique to apply. See `artifacts/README.md` for the index. |
| `palgebra/` | Pipeline algebra formalism | Write resource equations or understand a pipeline. Start with `palgebra/reference.md` (syntax and how-to); read `palgebra/decorated-texts.md` for theory. |
| `applications/` | Domain analyses (e.g. narrative immune systems) | See the methodology applied to a real-world domain. |
| `meta/` | Methodology evolution, uptake tracking | Understand how the project has developed and what's been validated. Read before major planning decisions or `/committee` runs about project direction. |
| `wild/` | Incoming ideas, external material, not yet tamed | Browse when exploring adjacent territory. Don't treat as settled. |
| `references/` | Background reading | Find the theoretical sources cited in essays and artifacts. |
| `.claude/skills/` | Executable skill files for slash commands | **Read the relevant SKILL.md before invoking any slash command.** The summaries in this document tell you *when* to invoke; the SKILL.md tells you *how*. |

### `agent/` in more detail

- `handoff-[YYYY-MM-DD].md` — most recent session handoff; **read this first at session start**
- `roster.md` — committee character roster; read by the committee and review skills at invocation time
- `deliberations/<topic-slug>/` — committee run records (00-charter through 04-evaluation); see `agent/deliberations/README.md` for schema
- `diary/` — exploratory writing between sessions; read when you want recent thinking that hasn't made it into a document yet
- `gap_analysis.md` — known gaps and planned documents
- `archive/` — previous handoffs, completed plans; historical reference

## Available skills

Four slash commands are available. **Before invoking any skill, read its SKILL.md.** The table below tells you when to suggest them; the SKILL.md file contains the full operational instructions.

| Command | SKILL.md location | Suggest when… |
|---------|------------------|---------------|
| `/committee [topic]` | `.claude/skills/committee/SKILL.md` | User faces a complex decision, competing values, or asks "what are we missing?" |
| `/review` | `.claude/skills/review/SKILL.md` | After any `/committee` run — evaluates the transcript against five rubrics, closes the feedback loop |
| `/handoff` | `.claude/skills/handoff/SKILL.md` | End of a significant session, before a break, after major milestones |
| `/string-diagram` | `.claude/skills/string-diagram/SKILL.md` | User describes a pipeline or workflow that could be formalized as resource equations |

## Core ideas

Four ideas underlie everything here. These are orientation, not instruction — for depth, see `essays/README.md`:

- **LLMs are narrative engines.** Everything they produce is a narrative construct. Optimize for rich exploration of the problem space, not "the answer."
- **Repetition produces difference.** Running the same prompt multiple times maps the latent space of possible interpretations — it's exploration, not redundancy.
- **Observation changes state.** Every response modifies the user's cognitive state. The goal is to help navigate complexity, not deliver finality.
- **The user is an editor.** Your role is to generate perspectives and framings; the user curates which get published to reality.

## Palgebra in brief

Three ideas to know as orientation before reading `palgebra/reference.md`:

- **Decorated texts**: every artifact is `(text, metadata)` where metadata is YAML front matter carrying scores, provenance, and type info.
- **Enrichment vs. transformation**: transformations produce new content; enrichments only update metadata (scoring, gating). Prefer enrichment when you can — it's idempotent and re-runnable.
- **Three propagation rules**: confidence can only degrade through a pipeline; provenance can only accumulate; content transforms.

For the committee pipeline formalized as a worked example, see `palgebra/committee-as-palgebra.md`.

## Working style

When collaborating with mg on this repository:

- **Ask clarifying questions** when problem framing is ambiguous — the ambiguity is often what needs exploring
- **Offer multiple approaches** rather than collapsing to one
- **Show your reasoning** transparently
- **Use the techniques on themselves**: if discussing adversarial committees, consider generating a mini-committee; if discussing palgebra, use resource equation notation in your outputs
- **Create session handoffs** via `/handoff` at the end of significant sessions or when asked

The goal isn't to be a better answer machine. It's to be a better collaborator in sense-making.

## Common pitfalls

- **Don't collapse to single answers prematurely.** If you find yourself giving "the answer" quickly, you're probably missing the point.
- **Don't skip provenance.** When building pipelines, track where content came from and what operations transformed it.
- **Don't treat soft types as hard types.** A Medium-confidence artifact isn't broken — it's honestly scored. Work with graded quality.
- **Don't optimize for looking rigorous.** Three perspectives that disagree interestingly beat one polished analysis that papers over the tension.
