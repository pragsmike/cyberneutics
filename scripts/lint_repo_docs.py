from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

EXCLUDED_PREFIXES = (
    'agent/archive/',
    'agent/diary/',
    'examples/',
)
EXCLUDED_FILES: set[str] = set()

COMMAND_NAMES = (
    'committee',
    'scenarios',
    'probe',
    'review',
    'handoff',
    'string-diagram',
)

INDEX_FILES = (
    'README.md',
    'artifacts/README.md',
    'essays/README.md',
    'meta/README.md',
    'research-programs/README.md',
    'examples/README.md',
    'agent/onboarding-core.md',
)

CONTRIBUTOR_GUIDE = 'meta/contributor-guide.md'

FORBIDDEN_PATTERNS = {
    'removed gap-analysis path': 'agent/gap_analysis.md',
    'repo-local scenario runtime path': 'agent/scenarios/',
    'repo-local deliberation runtime path': 'agent/deliberations/',
    'retired comparisons redirect stub': 'agent/comparisons/',
    'duplicate Codex skill tree path': '.Codex/skills',
    'stale transcript contribution path': 'Submit transcripts` in `artifacts/examples/',
}

LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def is_live_doc(path: Path) -> bool:
    rel_path = rel(path)
    if rel_path in EXCLUDED_FILES:
        return False
    if rel_path.startswith('agent/handoff-'):
        return False
    if rel_path.startswith('research-programs/') and '/results/' in rel_path:
        return False
    return not any(rel_path.startswith(prefix) for prefix in EXCLUDED_PREFIXES)


def live_docs() -> list[Path]:
    return sorted(path for path in REPO_ROOT.rglob('*.md') if is_live_doc(path))


def check_forbidden_patterns(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        text = path.read_text(encoding='utf-8')
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern in text:
                errors.append(f"{rel(path)} contains forbidden {label}: {pattern}")
    return errors


def check_onboarding_docs() -> list[str]:
    errors: list[str] = []
    for rel_path in ('AGENTS.md', 'CLAUDE.md', 'agent/onboarding-core.md'):
        path = REPO_ROOT / rel_path
        text = path.read_text(encoding='utf-8').lower()
        if 'agent/archive/' not in text or 'historical only' not in text:
            errors.append(f"{rel_path} must explicitly mark agent/archive/ as historical only")
    return errors


def check_command_wrappers() -> list[str]:
    errors: list[str] = []
    for name in COMMAND_NAMES:
        for prefix in ('.claude/commands', '.cursor/commands'):
            path = REPO_ROOT / prefix / f'{name}.md'
            if not path.exists():
                errors.append(f"Missing command wrapper: {rel(path)}")
    return errors


def check_index_links() -> list[str]:
    errors: list[str] = []
    for rel_path in INDEX_FILES:
        path = REPO_ROOT / rel_path
        text = path.read_text(encoding='utf-8')
        for target in LINK_RE.findall(text):
            target = target.strip()
            if not target or target.startswith('#'):
                continue
            if re.match(r'^[a-z]+://', target):
                continue
            if target.startswith('mailto:'):
                continue
            target_path = target.split('#', 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(f"Broken local link in {rel_path}: {target}")
    return errors


def check_expected_index_entries() -> list[str]:
    errors: list[str] = []
    artifacts_index = (REPO_ROOT / 'artifacts/README.md').read_text(encoding='utf-8')
    if 'category-theory-connection.md' not in artifacts_index:
        errors.append('artifacts/README.md must index artifacts/category-theory-connection.md')

    if not (REPO_ROOT / CONTRIBUTOR_GUIDE).exists():
        errors.append('meta/contributor-guide.md must exist')

    root_readme = (REPO_ROOT / 'README.md').read_text(encoding='utf-8')
    if 'Contributor Guide' not in root_readme:
        errors.append('README.md must link to meta/contributor-guide.md for repo contributors')

    contributing = (REPO_ROOT / 'CONTRIBUTING.md').read_text(encoding='utf-8')
    if CONTRIBUTOR_GUIDE not in contributing:
        errors.append('CONTRIBUTING.md must link to meta/contributor-guide.md')

    return errors


def main() -> int:
    docs = live_docs()
    errors: list[str] = []
    errors.extend(check_forbidden_patterns(docs))
    errors.extend(check_onboarding_docs())
    errors.extend(check_command_wrappers())
    errors.extend(check_index_links())
    errors.extend(check_expected_index_entries())

    if errors:
        print('lint_repo_docs.py: FAIL')
        for error in errors:
            print(f'- {error}')
        return 1

    print(f'lint_repo_docs.py: OK ({len(docs)} live markdown docs checked)')
    return 0


if __name__ == '__main__':
    sys.exit(main())