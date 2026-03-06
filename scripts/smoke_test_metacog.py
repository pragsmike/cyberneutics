#!/usr/bin/env python3
"""
Metacognition smoke test: run committee on three fixed topics, then run this script
to compare how confidence relates to accuracy across topics and to produce
nR_S1/nR_S2 for HMeta-d.

The three topics are chosen to encourage variation in confidence (different
propensities engage differently):
  1. Quickstart one-page (under 10 min) — accessibility vs rigor
  2. Default roster 5 vs 3 — process design, evidence vs precedent
  3. README "when not to use" — values vs optics

Prerequisites:
  - Run /committee on each topic in an AI session; ensure each resolution
    includes a confidence block (1–4 per member). Topic slugs must match
    METACOG_SMOKE_TOPICS below (or pass custom dirs as arguments).

Usage:
  python scripts/smoke_test_metacog.py
  python scripts/smoke_test_metacog.py -o agent/metacog_smoke_report.md
  python scripts/smoke_test_metacog.py --topics agent/deliberations/quickstart-one-page agent/deliberations/...  # custom dirs

Exit: 0 if all required deliberations have confidence data and report is written;
      1 if any deliberation is missing or has no confidence (with instructions).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Import from same directory
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_metacog_counts import (  # noqa: E402
    DEFAULT_K,
    trials_from_resolution,
    trials_to_counts,
)

# Topic slug (directory name under agent/deliberations/) and human-readable title
METACOG_SMOKE_TOPICS = [
    (
        "quickstart-one-page",
        "Should we add a one-page Quickstart that gets someone to their first committee run in under 10 minutes, even if it skips some nuance?",
    ),
    (
        "default-roster-5-vs-3",
        "Should the default committee run use the full 5-member roster, with a documented 'quick' 3-member variant as optional (rather than 5 as the only default)?",
    ),
    (
        "readme-when-not-to-use",
        "Should we add a short 'When not to use this methodology' section to the README (e.g. don't use for X, Y, Z) even if it might make the project look narrow or defensive?",
    ),
]


def _repo_root() -> Path:
    return _REPO_ROOT


def _deliberation_path(slug: str) -> Path:
    return _repo_root() / "agent" / "deliberations" / slug


def _resolution_path(slug: str) -> Path:
    return _deliberation_path(slug) / "03-resolution.md"


def run_smoke_test(
    topic_slugs: list[tuple[str, str]] | None = None,
    topic_dirs: list[Path] | None = None,
    report_path: Path | None = None,
) -> int:
    """Load trials from each topic, compute per-topic and cross-topic stats, write report. Returns 0 on success, 1 on missing data."""
    root = _repo_root()
    report_file = report_path or (root / "agent" / "metacog_smoke_report.md")

    if topic_dirs:
        # Custom dirs: (slug, title) from path name and placeholder title
        topics = [(p.name, p.name) for p in topic_dirs]
        resolution_paths = {p.name: p / "03-resolution.md" for p in topic_dirs if (p / "03-resolution.md").exists()}
        missing = [p.name for p in topic_dirs if (p / "03-resolution.md").exists() is False]
    else:
        topics = topic_slugs or METACOG_SMOKE_TOPICS
        resolution_paths = {slug: _resolution_path(slug) for slug, _ in topics}
        missing = [slug for slug, _ in topics if not resolution_paths[slug].exists()]
    if missing:
        print("Missing deliberation(s). Run /committee on these topics (ensure confidence 1-4 is recorded):", file=sys.stderr)
        for slug, title in topics:
            if slug in missing:
                print(f"  - {slug}: {title}", file=sys.stderr)
        print("\nThen run: python scripts/smoke_test_metacog.py", file=sys.stderr)
        return 1

    # Load trials per topic
    k = DEFAULT_K
    per_slug: dict[str, list[dict]] = {}
    for slug, _ in topics:
        path = resolution_paths[slug] if topic_dirs else _resolution_path(slug)
        trials = trials_from_resolution(slug, path, k)
        per_slug[slug] = trials

    # Require confidence data in all three
    no_conf = [slug for slug, t in per_slug.items() if len(t) == 0]
    if no_conf:
        print("No confidence data in:", no_conf, file=sys.stderr)
        print("Add a 'confidence:' block (1–4 per member) to 03-resolution.md for each. See agent/deliberations/example/03-resolution.md.", file=sys.stderr)
        return 1

    all_trials: list[dict] = []
    for t in per_slug.values():
        all_trials.extend(t)

    # Per-topic stats
    rows = []
    for slug, title in topics:
        trials = per_slug[slug]
        n = len(trials)
        n_correct = sum(1 for t in trials if t.get("correct"))
        confs = [t["confidence"] for t in trials]
        mean_conf = sum(confs) / n if n else 0
        var_conf = sum((c - mean_conf) ** 2 for c in confs) / n if n else 0
        sd_conf = var_conf ** 0.5
        n_aye = sum(1 for t in trials if t.get("vote") == "Aye")
        n_nay = n - n_aye
        # Resolution direction: vote that matched outcome (correct). If none correct, use majority.
        correct_votes = [t["vote"] for t in trials if t.get("correct")]
        direction = correct_votes[0] if correct_votes else ("Aye" if n_aye >= n_nay else "Nay")
        acc_pct = (100.0 * n_correct / n) if n else 0
        rows.append({
            "slug": slug,
            "title": title,
            "n": n,
            "direction": direction,
            "n_aye": n_aye,
            "n_nay": n_nay,
            "conf_mean": mean_conf,
            "conf_sd": round(sd_conf, 2),
            "conf_min": min(confs),
            "conf_max": max(confs),
            "accuracy_pct": round(acc_pct, 1),
        })

    # Cross-topic: confidence vs accuracy (how does metacognition impact committee decision making?)
    high_conf = [t for t in all_trials if t.get("confidence", 0) >= 3]  # 3–4
    low_conf = [t for t in all_trials if t.get("confidence", 0) <= 2]  # 1–2
    n_high = len(high_conf)
    n_low = len(low_conf)
    acc_high = (100.0 * sum(1 for t in high_conf if t.get("correct")) / n_high) if n_high else 0
    acc_low = (100.0 * sum(1 for t in low_conf if t.get("correct")) / n_low) if n_low else 0

    nR_S1, nR_S2 = trials_to_counts(all_trials, k)

    # Build report
    lines = [
        "# Metacognition smoke test report",
        "",
        "Compares three committee deliberations chosen to elicit variation in confidence, and summarizes how **confidence relates to accuracy** (metacognition impact on committee decision making).",
        "",
        "**What this is for:** Metacognition helps the *end user* interpret and weight the committee's advice when making their own decision (e.g. whose confidence to trust). It does not change or improve the committee's decision itself.",
        "",
        "## Topics (run /committee on each with confidence recorded)",
        "",
    ]
    for slug, title in topics:
        lines.append(f"- **{slug}**: {title}")
    lines.extend(["", "---", "", "## Per-topic summary", ""])
    lines.append("| Topic | Resolution | Aye | Nay | Confidence (mean ± sd) | Accuracy |")
    lines.append("|-------|------------|-----|-----|------------------------|----------|")
    for r in rows:
        lines.append(
            f"| {r['slug']} | {r['direction']} | {r['n_aye']} | {r['n_nay']} | "
            f"{r['conf_mean']:.1f} ± {r['conf_sd']} (range {r['conf_min']}-{r['conf_max']}) | {r['accuracy_pct']}% |"
        )
    lines.extend([
        "",
        "---",
        "",
        "## Metacognition impact (confidence vs accuracy)",
        "",
        f"- **High confidence (3–4):** {n_high} votes, **{acc_high:.1f}%** correct.",
        f"- **Low confidence (1–2):** {n_low} votes, **{acc_low:.1f}%** correct.",
        "",
    ])
    if n_high and n_low:
        diff = acc_high - acc_low
        if diff > 5:
            lines.append("When members were more confident, they were more often aligned with the resolution (positive metacognitive signal).")
        elif diff < -5:
            lines.append("When members were less confident, they were more often aligned with the resolution (overconfidence when wrong).")
        else:
            lines.append("Confidence and accuracy were similar across high vs low confidence in this small sample; run more deliberations or fit meta-d'/d' (HMeta-d) for a formal efficiency estimate.")
    lines.extend([
        "",
        "---",
        "",
        "## HMeta-d inputs (pooled across all three topics)",
        "",
        "For hierarchical meta-d' (e.g. `fit_meta_d_mcmc` in [HMeta-d](https://github.com/metacoglab/HMeta-d)):",
        "",
        "```",
        f"nR_S1 = {nR_S1}",
        f"nR_S2 = {nR_S2}",
        "```",
        "",
        "See `artifacts/metacognition-and-committee-veracity.md` and `scripts/build_metacog_counts.py --per-character` for per-character efficiency across runs.",
        "",
    ])

    report_file = report_file if report_file.is_absolute() else root / report_file
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text("\n".join(lines), encoding="utf-8")

    print("Metacognition smoke test OK.")
    print(f"  Report: {report_file}")
    print(f"  Per-topic: {len(rows)} deliberations, {len(all_trials)} trials total.")
    print(f"  High confidence (3–4): {acc_high:.1f}% correct. Low confidence (1–2): {acc_low:.1f}% correct.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Smoke test: compare metacognition across three committee topics.",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("agent/metacog_smoke_report.md"),
        metavar="FILE",
        help="Write report to FILE (default: agent/metacog_smoke_report.md).",
    )
    parser.add_argument(
        "--topics",
        nargs="+",
        type=Path,
        metavar="DIR",
        help="Use these deliberation directories instead of the default three (slug = dir name).",
    )
    args = parser.parse_args()
    if args.topics:
        return run_smoke_test(topic_dirs=[p if p.is_absolute() else _repo_root() / p for p in args.topics], report_path=args.output)
    return run_smoke_test(report_path=args.output)


if __name__ == "__main__":
    sys.exit(main())
