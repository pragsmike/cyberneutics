# Contributor Guide

This guide is for people who want to improve the Cyberneutics repository without disrupting the reader paths that already serve the repo's core audiences.

## Who This Repo Already Serves

Cyberneutics already has explicit reading and usage paths for several audiences:

| Audience | Primary need | Start here |
|---|---|---|
| **Practitioners** | Learn the methodology well enough to run it | `artifacts/start-here.md`, `artifacts/quick-start-guide.md` |
| **Theorists** | Understand the synthesis and argument structure | `essays/README.md` |
| **Skeptics** | Evaluate evidence, limits, and failure modes | `essays/README.md` and `essays/when-methodology-fails.md` |
| **Formalists** | Work with the precise machinery and notation | `palgebra/reference.md` and `essays/README.md` |
| **Research collaborators** | Contribute evidence, experiments, and validation work | `research-programs/README.md` |

Contributor-facing changes should preserve these paths rather than flatten them into a single generic onboarding flow.

## Choose Your Contribution Path

### Improve practical usage

Work in `artifacts/` when you are clarifying or extending the methodology as something a practitioner can actually use.

Typical contributions:
- new technique or protocol
- clearer setup or troubleshooting guidance
- better examples of when to use a technique

### Improve theory or synthesis

Work in `essays/` when you are strengthening the conceptual argument, clarifying terminology, or improving the reading paths for theorists and skeptics.

Typical contributions:
- new essay
- terminology clarification
- cross-references or sequence fixes

### Improve evidence or validation

Work in `research-programs/` when you are proposing, extending, or executing a research program.

Typical contributions:
- new experiment design
- status updates and linked results
- clearer contributing blocks or prerequisites

### Preserve examples or historical records

Work in `examples/` only when a run is worth keeping as a checked-in example or historical reference.

Use `artifacts/examples/` for prose walkthroughs and worked-example writeups, not for raw runtime outputs.

### Improve repo structure or navigation

Work in root docs, `meta/`, or carefully selected README files when you are improving findability, contributor guidance, or architectural clarity.

## First Contributions

If you are new to the repo, prefer one of these bounded tasks first:

1. Fix a broken, missing, or misleading cross-reference in a README or index.
2. Improve one `research-programs/` entry so its prerequisites, scope, and expected outputs are explicit.
3. Tighten a contributor-facing doc so it matches the current runtime-vs-example architecture.
4. Add or improve a short worked-example pointer in `artifacts/README.md` or another index page.
5. Preserve a checked-in example under `examples/` and annotate what makes it worth keeping.

## Where Things Go

- Live committee, scenario, review, and probe runs belong in an external situation directory.
- Checked-in scenario and deliberation records belong under `examples/` when they are being preserved as examples or historical records.
- Worked-example prose belongs under `artifacts/examples/`.
- Operational agent continuity material belongs under `agent/`.
- Current project-state and reflective repo documentation belong under `meta/`.

Canonical runtime/output rules live in `agent/onboarding-core.md` and `meta/project-state.md`.

## Minimum Quality Bar

Every contribution should meet these baseline expectations:

- Put the content in the correct directory for its purpose.
- Update the relevant index or README if you add a new file that users should discover.
- Preserve the existing audience paths instead of replacing them with contributor-only framing.
- Keep claims proportionate to evidence; if something is speculative, label it clearly.
- Use relative links and verify they resolve.

## Validation

Before opening a PR:

1. Run `py -3 scripts/lint_repo_docs.py`.
2. If you changed the string-diagram tool or related formalism surfaces, run `py -3 scripts/test_string_diagram.py`.
3. Read the surrounding README or index to ensure your change still fits the local navigation and tone.
4. Check that you did not reintroduce repo-local runtime output instructions.

## Audience Impact Check

Before merging a contributor-facing change, ask:

- Does this help contributors without making the root README heavier than necessary?
- Does this preserve the practitioner, theorist, skeptic, and formalist reading paths?
- Does this keep live outputs in external situation directories and examples in `examples/`?
- Does this avoid pushing maintainer-only or agent-only detail into reader-facing docs?
- Does this improve one audience without confusing another?

If the answer to any of these is no, adjust the change or move the detail into a more appropriate doc.
