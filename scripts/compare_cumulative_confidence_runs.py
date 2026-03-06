#!/usr/bin/env python3
"""
Compare two committee runs (baseline vs with-register) for the cumulative-confidence smoke test.

Reads 04-evaluation-1.md from both directories for transcript_review sum and verdict,
and scans the with-register run's 02-deliberation.md and 03-resolution.md for
calibration-related language. Outputs a short report to stdout and optionally to a file.

Usage:
  python scripts/compare_cumulative_confidence_runs.py agent/deliberations/<baseline-slug> agent/deliberations/<slug>-with-register
  python scripts/compare_cumulative_confidence_runs.py agent/deliberations/readme-glossary agent/deliberations/readme-glossary-with-register -o agent/cumulative_confidence_comparison.md

See artifacts/cumulative-confidence-smoke-test.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent

# Keywords that suggest the committee used calibration/register (case-insensitive)
CALIBRATION_KEYWORDS = [
    "calibration",
    "calibrated",
    "past run",
    "past runs",
    "register",
    "veracity",
    "well-calibrated",
    "overconfident",
    "weight",
    "weighting",
    "hedge",
    "hedging",
    "confidence track",
    "confidence tracked",
    "meta-d",
    "metacog",
    "cumulative confidence",
]


def _repo_root() -> Path:
    return _REPO_ROOT


def _extract_yaml_front_matter(path: Path) -> str | None:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 2:
        return None
    return parts[1].strip()


def _get_transcript_review_sum_verdict(eval_path: Path) -> tuple[int | None, str | None]:
    """Parse 04-evaluation-1.md for transcript_review.sum and transcript_review.verdict. Returns (sum, verdict)."""
    yaml_str = _extract_yaml_front_matter(eval_path)
    if not yaml_str:
        return None, None
    sum_val = None
    verdict_val = None
    in_transcript_review = False
    for line in yaml_str.splitlines():
        line = line.rstrip()
        if line.startswith("transcript_review:"):
            in_transcript_review = True
            continue
        if in_transcript_review and line and not line[0].isspace():
            in_transcript_review = False
        if in_transcript_review:
            m = re.match(r"^\s+sum:\s*(\d+)\s*$", line)
            if m:
                sum_val = int(m.group(1))
            m = re.match(r"^\s+verdict:\s*[\"']?(\w+)[\"']?\s*$", line)
            if m:
                verdict_val = m.group(1)
    return sum_val, verdict_val


def _count_calibration_mentions(text: str) -> list[str]:
    """Return list of calibration keywords found in text (case-insensitive)."""
    found = []
    lower = text.lower()
    for kw in CALIBRATION_KEYWORDS:
        if kw.lower() in lower:
            found.append(kw)
    return found


def run_comparison(
    baseline_dir: Path,
    with_register_dir: Path,
    report_path: Path | None = None,
) -> int:
    root = _repo_root()
    base = (baseline_dir if baseline_dir.is_absolute() else root / baseline_dir).resolve()
    wreg = (with_register_dir if with_register_dir.is_absolute() else root / with_register_dir).resolve()

    if not base.is_dir():
        print(f"Baseline directory not found: {base}", file=sys.stderr)
        return 1
    if not wreg.is_dir():
        print(f"With-register directory not found: {wreg}", file=sys.stderr)
        return 1

    base_eval = base / "04-evaluation-1.md"
    wreg_eval = wreg / "04-evaluation-1.md"
    base_sum, base_verdict = _get_transcript_review_sum_verdict(base_eval) if base_eval.exists() else (None, None)
    wreg_sum, wreg_verdict = _get_transcript_review_sum_verdict(wreg_eval) if wreg_eval.exists() else (None, None)

    wreg_delib = wreg / "02-deliberation.md"
    wreg_res = wreg / "03-resolution.md"
    delib_text = wreg_delib.read_text(encoding="utf-8") if wreg_delib.exists() else ""
    res_text = wreg_res.read_text(encoding="utf-8") if wreg_res.exists() else ""
    combined = delib_text + "\n" + res_text
    mentions = _count_calibration_mentions(combined)
    mentions_unique = sorted(set(mentions))

    lines = [
        "# Cumulative confidence smoke test: comparison report",
        "",
        f"**Baseline:** `{base.name}`",
        f"**With register:** `{wreg.name}`",
        "",
        "## Review scores (transcript_review)",
        "",
        f"| Run | Sum (0–15) | Verdict |",
        f"|-----|------------|---------|",
        f"| Baseline | {base_sum if base_sum is not None else '—'} | {base_verdict or '—'} |",
        f"| With register | {wreg_sum if wreg_sum is not None else '—'} | {wreg_verdict or '—'} |",
        "",
    ]
    if base_sum is not None and wreg_sum is not None:
        diff = wreg_sum - base_sum
        if diff > 0:
            lines.append(f"With-register run scores **higher** by {diff} point(s).")
        elif diff < 0:
            lines.append(f"With-register run scores **lower** by {-diff} point(s).")
        else:
            lines.append("Scores are **equal**.")
        lines.append("")

    lines.extend([
        "## Calibration-aware content (with-register run)",
        "",
    ])
    if mentions_unique:
        lines.append(f"The with-register deliberation or resolution mentions: **{', '.join(mentions_unique)}**.")
        lines.append("")
    else:
        lines.append("No calibration-related keywords found in the with-register 02-deliberation.md or 03-resolution.md.")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("See `artifacts/cumulative-confidence-smoke-test.md` for interpretation.")
    lines.append("")

    report = "\n".join(lines)
    print(report)

    if report_path:
        out = (report_path if report_path.is_absolute() else root / report_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"Report written to {out}", file=sys.stderr)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compare baseline vs with-register committee runs for cumulative-confidence smoke test.",
    )
    parser.add_argument("baseline_dir", type=Path, help="Baseline deliberation directory (e.g. agent/deliberations/readme-glossary).")
    parser.add_argument("with_register_dir", type=Path, help="With-register deliberation directory (e.g. agent/deliberations/readme-glossary-with-register).")
    parser.add_argument("-o", "--output", type=Path, metavar="FILE", help="Write report to FILE.")
    args = parser.parse_args()
    return run_comparison(args.baseline_dir, args.with_register_dir, report_path=args.output)


if __name__ == "__main__":
    sys.exit(main())
