#!/usr/bin/env python3
"""
Update the metacognition register from all deliberations that have confidence data.

Scans agent/deliberations/ for directories with 03-resolution.md containing a
confidence block, loads trials (vote + confidence + correct), and overwrites
agent/metacog_register.md with:
  - Deliberation slugs included and last-updated date
  - Per-character: trial count, % correct (high conf 3-4, low conf 1-2)
  - Committee-wide: total trials, accuracy bands, pooled nR_S1/nR_S2 for HMeta-d

Run from repo root after new committee runs that recorded confidence. See
artifacts/metacognition-and-committee-veracity.md §6 (Tracking across runs).

Usage:
  python scripts/update_metacog_register.py
  python scripts/update_metacog_register.py -o agent/metacog_register.md
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_metacog_counts import (  # noqa: E402
    DEFAULT_K,
    trials_from_resolution,
    trials_to_counts,
)


def _repo_root() -> Path:
    return _REPO_ROOT


def _discover_deliberations_with_confidence(root: Path) -> list[tuple[str, Path]]:
    """Return (slug, path_to_03-resolution.md) for each deliberation that has confidence."""
    out = []
    deliberations_dir = root / "agent" / "deliberations"
    if not deliberations_dir.is_dir():
        return out
    for sub in sorted(deliberations_dir.iterdir()):
        if not sub.is_dir():
            continue
        res_path = sub / "03-resolution.md"
        if not res_path.exists():
            continue
        trials = trials_from_resolution(sub.name, res_path, DEFAULT_K)
        if trials:
            out.append((sub.name, res_path))
    return out


def _high_low_stats(trials: list[dict]) -> dict:
    """Return n_high, n_low, acc_high_pct, acc_low_pct."""
    high = [t for t in trials if t.get("confidence", 0) >= 3]
    low = [t for t in trials if t.get("confidence", 0) <= 2]
    n_high = len(high)
    n_low = len(low)
    acc_high = (100.0 * sum(1 for t in high if t.get("correct")) / n_high) if n_high else 0.0
    acc_low = (100.0 * sum(1 for t in low if t.get("correct")) / n_low) if n_low else 0.0
    return {
        "n_high": n_high,
        "n_low": n_low,
        "acc_high_pct": round(acc_high, 1),
        "acc_low_pct": round(acc_low, 1),
        "n_correct": sum(1 for t in trials if t.get("correct")),
        "n": len(trials),
    }


def run_update(register_path: Path | None = None) -> int:
    root = _repo_root()
    out_path = register_path or (root / "agent" / "metacog_register.md")
    if not out_path.is_absolute():
        out_path = root / out_path

    discovered = _discover_deliberations_with_confidence(root)
    if not discovered:
        print("No deliberations with confidence data found under agent/deliberations/.", file=sys.stderr)
        if out_path.exists():
            out_path.write_text(
                "# Metacognition register\n\n"
                "*No deliberations with confidence data. Run committee with confidence 1–4 per member, then re-run this script.*\n",
                encoding="utf-8",
            )
        return 0

    slugs = [s for s, _ in discovered]
    all_trials: list[dict] = []
    for slug, res_path in discovered:
        all_trials.extend(trials_from_resolution(slug, res_path, DEFAULT_K))

    k = DEFAULT_K
    by_char: dict[str, list[dict]] = {}
    for t in all_trials:
        name = (t.get("character") or "").strip()
        name = name.title() if name else "Unknown"
        by_char.setdefault(name, []).append(t)

    pooled_stats = _high_low_stats(all_trials)
    nR_S1, nR_S2 = trials_to_counts(all_trials, k)

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        "# Metacognition register",
        "",
        "Tracks confidence and accuracy **across committee runs** to support the end user (who to weight when interpreting advice). Does not change the committee's decision. Updated by `scripts/update_metacog_register.py`.",
        "",
        f"**Last updated:** {now}",
        "",
        "## Deliberations included",
        "",
    ]
    for s in slugs:
        lines.append(f"- {s}")
    lines.extend([
        "",
        "---",
        "",
        "## Per-character summary (across runs)",
        "",
        "| Character | Trials | Correct | High conf (3–4) acc % | Low conf (1–2) acc % |",
        "|-----------|--------|---------|------------------------|------------------------|",
    ])
    for char in sorted(by_char.keys()):
        tlist = by_char[char]
        st = _high_low_stats(tlist)
        n_correct = st["n_correct"]
        n = st["n"]
        pct = (100.0 * n_correct / n) if n else 0
        lines.append(
            f"| {char} | {n} | {n_correct} ({pct:.0f}%) | "
            f"{st['acc_high_pct']}% (n={st['n_high']}) | {st['acc_low_pct']}% (n={st['n_low']}) |"
        )
    lines.extend([
        "",
        "---",
        "",
        "## Committee-wide (pooled)",
        "",
        f"- **Total trials:** {pooled_stats['n']}",
        f"- **Overall correct:** {pooled_stats['n_correct']} ({100.0 * pooled_stats['n_correct'] / pooled_stats['n']:.1f}%)",
        f"- **High confidence (3–4):** {pooled_stats['n_high']} votes, **{pooled_stats['acc_high_pct']}%** correct.",
        f"- **Low confidence (1–2):** {pooled_stats['n_low']} votes, **{pooled_stats['acc_low_pct']}%** correct.",
        "",
        "### HMeta-d inputs (pooled)",
        "",
        "For `fit_meta_d_mcmc` in [HMeta-d](https://github.com/metacoglab/HMeta-d):",
        "",
        "```",
        f"nR_S1 = {nR_S1}",
        f"nR_S2 = {nR_S2}",
        "```",
        "",
        "For per-character efficiency use `python scripts/build_metacog_counts.py agent/deliberations --per-character` and `fit_meta_d_mcmc_group` in HMeta-d.",
        "",
    ])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {out_path} ({len(slugs)} deliberations, {len(all_trials)} trials).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Update metacognition register from all deliberations with confidence.")
    parser.add_argument("-o", "--output", type=Path, default=Path("agent/metacog_register.md"), help="Output path for register.")
    args = parser.parse_args()
    return run_update(register_path=args.output)


if __name__ == "__main__":
    sys.exit(main())
