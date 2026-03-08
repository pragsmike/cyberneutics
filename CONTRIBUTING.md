# Contributing to Cyberneutics

Thank you for your interest in contributing to Cyberneutics.

We welcome contributions at every level of polish — from fully-formed artifacts to half-formed ideas. For a workflow-based entry point, see [meta/contributor-guide.md](meta/contributor-guide.md). This file explains what kinds of work fit here, where they go, and what to check before opening a PR.

## Contribution Types

Cyberneutics welcomes contributions in five main categories:

- **Techniques and protocols** in `artifacts/`
- **Essays and theoretical clarification** in `essays/`
- **Research and validation work** in `research-programs/`
- **Checked-in examples and historical records** in `examples/`
- **Repo structure, navigation, and reflective docs** in root docs or `meta/`
- **Exploratory ideas and lateral connections** in `wild/` and `wild/diary/`

## Placement Rules

- Live committee, scenario, review, and probe runs belong in an external situation directory, not in this repo.
- Checked-in scenario and deliberation records belong in `examples/` when they are being preserved as examples or historical references.
- Prose walkthroughs and worked-example writeups belong in `artifacts/examples/`.
- Agent continuity material belongs in `agent/`.
- Canonical onboarding and current-state rules live in `agent/onboarding-core.md` and `meta/project-state.md`.
- Exploratory ideas, field notes, and early-stage connections belong in `wild/`. Raw sketches with no structure go in `wild/diary/`; ideas with enough shape to warrant a topic directory go directly in `wild/`.

## Exploratory Contributions

Contributions to `wild/` and `wild/diary/` have a different lifecycle. They are reviewed periodically by the maintainer, not in real time. Acceptance means the idea is being held — not that it will necessarily be developed into a formal artifact. Ideas that connect to existing threads may be promoted to `wild/` topic directories, folded into research programs, or remain as seeds for future work.

The only convention for `wild/diary/` is a date-prefixed filename (`YYYY-MM-DD-short-title.md`). No structural requirements beyond that.

## Minimum Standard

Every contribution should:

- solve a clear problem or improve a real part of the user experience
- land in the correct directory for its purpose
- maintain the repo's existing audience paths for Practitioners, Theorists, Skeptics, Formalists, and Research collaborators
- keep claims proportionate to evidence
- use working relative links

## Update the Relevant Index

If you add or substantially change a document that users should discover, update the relevant index or README.

Typical examples:
- `artifacts/README.md`
- `essays/README.md`
- `research-programs/README.md`
- `meta/README.md`
- root `README.md`

## Validate Before Opening a PR

1. Run `py -3 scripts/lint_repo_docs.py`.
2. If your change touches the string-diagram tool or related formalism surfaces, run `py -3 scripts/test_string_diagram.py`.
3. Re-read the surrounding README or index so your change still fits the local navigation and tone.
4. Confirm that you did not reintroduce repo-local runtime output instructions.

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License (for code/artifacts) and CC BY-SA 4.0 (for essays/text), as defined in the root README.
