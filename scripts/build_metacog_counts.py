#!/usr/bin/env python3
"""
Build nR_S1 / nR_S2 count vectors from committee deliberation resolutions for HMeta-d.

Reads 03-resolution.md from one or more agent/deliberations/<slug>/ directories,
extracts votes and confidence (if present), infers resolution direction (Aye/Nay),
codes accuracy (vote matches resolution = correct), and outputs:
  - trials CSV: deliberation_slug, character, vote, confidence, correct
  - per-character or pooled nR_S1, nR_S2 (HMeta-d format; k = number of confidence levels).

Confidence scale in resolutions is 1..k (default k=4). Only trials with a
confidence value are included. Resolutions without a 'confidence' block are skipped
for count output (trials CSV will be empty for those).

Usage:
  python scripts/build_metacog_counts.py agent/deliberations/slug1 agent/deliberations/slug2 ...
  python scripts/build_metacog_counts.py agent/deliberations --pool          # pool all into one subject
  python scripts/build_metacog_counts.py agent/deliberations --per-character  # one subject per character
  python scripts/build_metacog_counts.py agent/deliberations -k 4 -o trials.csv  # write trials to CSV

Run from repository root. See artifacts/metacognition-and-committee-veracity.md.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

# Default confidence levels (scale 1..k)
DEFAULT_K = 4

# Response mapping: we use Aye = response S1, Nay = response S2 for HMeta-d.
# nR_S1 order (stimulus = correct): Aye conf k, k-1, ..., 1, Nay conf 1, 2, ..., k.
# nR_S2 order (stimulus = incorrect): same.


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _extract_yaml_front_matter(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---")
    if len(parts) < 2:
        return None
    return parts[1].strip()


def _parse_resolution_yaml(raw: str) -> dict:
    """Parse resolution YAML: use PyYAML if available, else regex fallback for votes/confidence/decision."""
    try:
        import yaml
        data = yaml.safe_load(raw)
        if data and "resolution" in data:
            return data["resolution"]
        return data or {}
    except ImportError:
        pass
    # Fallback: extract resolution block and parse votes/confidence/decision by regex
    out: dict = {"votes": {}, "confidence": {}, "decision": ""}
    in_votes = in_confidence = False
    for line in raw.splitlines():
        s = line.rstrip()
        if not s:
            continue
        if re.match(r"^  votes:\s*$", s):
            in_votes, in_confidence = True, False
            continue
        if re.match(r"^  confidence:\s*$", s):
            in_votes, in_confidence = False, True
            continue
        if re.match(r"^  \w+:", s) and not re.match(r"^  (votes|confidence)\s*:", s):
            in_votes, in_confidence = False, False
        if in_votes:
            m = re.match(r'^\s{4}(\w+):\s*["\']?([^"\']+)["\']?\s*$', s) or re.match(r"^\s{4}(\w+):\s*(.+)$", s)
            if m:
                out["votes"][m.group(1).strip()] = m.group(2).strip().strip('"')
        if in_confidence:
            m = re.match(r"^\s{4}(\w+):\s*(\d+)\s*$", s)
            if m:
                out["confidence"][m.group(1).strip()] = int(m.group(2))
        if s.startswith("  decision:") and len(s) > 11:
            out["decision"] = s[11:].strip().strip('"')
    return out


def _normalize_vote(v: str) -> str | None:
    """Map vote string to Aye or Nay. Returns None if abstain or unparseable."""
    v = (v or "").strip().upper()
    # Strip parentheticals for binary
    v = re.sub(r"\s*\([^)]*\).*", "", v).strip().upper()
    if v in ("AYE", "YES", "Y"):
        return "Aye"
    if v in ("NAY", "NO", "N"):
        return "Nay"
    return None


def _infer_resolution_direction(votes: list[tuple[str, str]], decision: str) -> str | None:
    """Infer Aye or Nay from votes (and optionally decision text)."""
    aye = sum(1 for _, v in votes if v == "Aye")
    nay = sum(1 for _, v in votes if v == "Nay")
    if aye > nay:
        return "Aye"
    if nay > aye:
        return "Nay"
    # Tie: try decision text
    d = (decision or "").lower()
    if "do not" in d or "don't" in d or "reject" in d or "against" in d:
        return "Nay"
    if "add" in d and "do not add" in d:
        return "Nay"
    return "Aye" if aye >= nay else "Nay"


def _collect_votes_and_confidence(resolution: dict) -> tuple[list[tuple[str, str]], dict[str, int]]:
    """Extract (member, vote) list and {member: confidence}. Handles both vote formats."""
    votes_out: list[tuple[str, str]] = []
    conf_out: dict[str, int] = {}
    votes_block = resolution.get("votes")
    conf_block = resolution.get("confidence") or {}
    if not votes_block:
        return votes_out, conf_out
    # Format 1: list of {member: X, vote: Y}
    if isinstance(votes_block, list):
        for item in votes_block:
            if isinstance(item, dict):
                name = (item.get("member") or item.get("name") or "").strip()
                v = (item.get("vote") or "").strip()
            else:
                continue
            norm = _normalize_vote(v)
            if norm and name:
                votes_out.append((name, norm))
    # Format 2: dict Maya: "Nay"
    elif isinstance(votes_block, dict):
        for name, v in votes_block.items():
            if isinstance(v, dict):
                v = v.get("vote") or v.get("value") or ""
            v = str(v).strip()
            norm = _normalize_vote(v)
            if norm:
                votes_out.append((name.strip(), norm))
    # Confidence: dict Maya: 3 (keep original key for lookup; we'll match case-insensitively when using)
    for name, c in (conf_block if isinstance(conf_block, dict) else {}).items():
        try:
            conf_out[name.strip()] = int(c)
        except (TypeError, ValueError):
            pass
    return votes_out, conf_out


def _get_confidence(confidence: dict[str, int], member_name: str) -> int | None:
    """Get confidence for a member; match by key first, then case-insensitive."""
    name = member_name.strip()
    if name in confidence:
        return confidence[name]
    for k, v in confidence.items():
        if k.lower() == name.lower():
            return v
    return None


def load_resolution(path: Path) -> dict | None:
    """Load and parse 03-resolution.md; return resolution dict or None."""
    yaml_str = _extract_yaml_front_matter(path)
    if not yaml_str:
        return None
    try:
        data = _parse_resolution_yaml(yaml_str)
        return data.get("resolution") or data
    except Exception:
        return None


def trials_from_resolution(slug: str, resolution_path: Path, k: int) -> list[dict]:
    """Extract trials (character, vote, confidence, correct) from one resolution file."""
    res = load_resolution(resolution_path)
    if not res:
        return []
    votes_list, confidence = _collect_votes_and_confidence(res)
    if not votes_list:
        return []
    decision = res.get("decision") or ""
    direction = _infer_resolution_direction(votes_list, decision)
    if not direction:
        return []
    trials = []
    for name, vote in votes_list:
        conf = _get_confidence(confidence, name)
        if conf is None or conf < 1 or conf > k:
            continue
        correct = 1 if vote == direction else 0
        trials.append({
            "deliberation_slug": slug,
            "character": name,
            "vote": vote,
            "confidence": conf,
            "correct": correct,
        })
    return trials


def trials_to_counts(trials: list[dict], k: int) -> tuple[list[int], list[int]]:
    """Convert list of {vote, confidence, correct} to nR_S1, nR_S2 (length k*2).
    Order: Aye conf k..1, Nay conf 1..k (response S1 = Aye, S2 = Nay).
    """
    nR_S1 = [0] * (k * 2)  # stimulus = correct (S1)
    nR_S2 = [0] * (k * 2)  # stimulus = incorrect (S2)
    for t in trials:
        vote = t.get("vote") or "Aye"
        conf = int(t.get("confidence") or 1)
        correct = int(t.get("correct") or 0)
        if conf < 1 or conf > k:
            continue
        # Index: Aye = response 1 -> indices 0..k-1 (conf k down to 1); Nay = response 2 -> indices k..2k-1 (conf 1..k)
        if vote == "Aye":
            idx = (k - conf)  # 0..k-1
        else:
            idx = k + (conf - 1)  # k..2k-1
        if correct:
            nR_S1[idx] += 1
        else:
            nR_S2[idx] += 1
    return nR_S1, nR_S2


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build nR_S1/nR_S2 from committee deliberation resolutions for HMeta-d.",
    )
    parser.add_argument(
        "dirs",
        nargs="+",
        type=Path,
        help="Deliberation directories (e.g. agent/deliberations/slug) or one parent dir to scan for 03-resolution.md",
    )
    parser.add_argument(
        "-k",
        type=int,
        default=DEFAULT_K,
        metavar="K",
        help=f"Number of confidence levels (1..k). Default {DEFAULT_K}.",
    )
    parser.add_argument(
        "--pool",
        action="store_true",
        help="Pool all trials into one subject (single nR_S1, nR_S2).",
    )
    parser.add_argument(
        "--per-character",
        action="store_true",
        help="Output nR_S1/nR_S2 per character (one subject per character across deliberations).",
    )
    parser.add_argument(
        "-o", "--trials-csv",
        type=Path,
        metavar="FILE",
        help="Write trial-level CSV to FILE.",
    )
    parser.add_argument(
        "--matlab",
        action="store_true",
        help="Print nR_S1/nR_S2 in MATLAB cell array style for copy-paste into HMeta-d.",
    )
    args = parser.parse_args()
    root = _repo_root()

    # Resolve deliberation directories
    resolution_paths: list[tuple[str, Path]] = []
    for d in args.dirs:
        p = (d if d.is_absolute() else root / d).resolve()
        if (p / "03-resolution.md").exists():
            resolution_paths.append((p.name, p / "03-resolution.md"))
        elif p.is_dir():
            for sub in p.iterdir():
                if sub.is_dir() and (sub / "03-resolution.md").exists():
                    resolution_paths.append((sub.name, sub / "03-resolution.md"))

    if not resolution_paths:
        print("No 03-resolution.md found in given dirs.", file=sys.stderr)
        return 1

    all_trials: list[dict] = []
    for slug, res_path in resolution_paths:
        all_trials.extend(trials_from_resolution(slug, res_path, args.k))

    if args.trials_csv:
        out_path = args.trials_csv if args.trials_csv.is_absolute() else root / args.trials_csv
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["deliberation_slug", "character", "vote", "confidence", "correct"])
            w.writeheader()
            w.writerows(all_trials)
        print(f"Wrote {len(all_trials)} trials to {out_path}", file=sys.stderr)

    if not all_trials:
        print("No trials with confidence data. Add 'confidence:' to 03-resolution.md in deliberations.", file=sys.stderr)
        return 0

    if args.pool:
        nR_S1, nR_S2 = trials_to_counts(all_trials, args.k)
        print("Pooled (single subject):")
        print("nR_S1 =", nR_S1)
        print("nR_S2 =", nR_S2)
        if args.matlab:
            print("% MATLAB: nR_S1 =", str(nR_S1).replace("'", ""), "; nR_S2 =", str(nR_S2).replace("'", ""), ";")
        return 0

    if args.per_character:
        by_char: dict[str, list[dict]] = {}
        for t in all_trials:
            c = t["character"]
            by_char.setdefault(c, []).append(t)
        print("Per-character counts (for fit_meta_d_mcmc_group):")
        for char in sorted(by_char.keys()):
            nR_S1, nR_S2 = trials_to_counts(by_char[char], args.k)
            print(f"  {char}: nR_S1 = {nR_S1}, nR_S2 = {nR_S2}")
        if args.matlab:
            print("% MATLAB cell arrays (one cell per character, same order as above):")
            nR_S1_cells = [trials_to_counts(by_char[c], args.k)[0] for c in sorted(by_char.keys())]
            nR_S2_cells = [trials_to_counts(by_char[c], args.k)[1] for c in sorted(by_char.keys())]
            print("nR_S1 = {" + "; ".join(str(x) for x in nR_S1_cells) + "};")
            print("nR_S2 = {" + "; ".join(str(x) for x in nR_S2_cells) + "};")
        return 0

    # Default: one subject per deliberation (per-run committee)
    by_slug: dict[str, list[dict]] = {}
    for t in all_trials:
        s = t["deliberation_slug"]
        by_slug.setdefault(s, []).append(t)
    print("Per-deliberation (committee per run):")
    for slug in sorted(by_slug.keys()):
        nR_S1, nR_S2 = trials_to_counts(by_slug[slug], args.k)
        print(f"  {slug}: nR_S1 = {nR_S1}, nR_S2 = {nR_S2}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
