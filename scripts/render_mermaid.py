#!/usr/bin/env python3
"""
render_mermaid.py

Render a .mermaid file to PNG or SVG using the mermaid.ink public API.
No Node.js or mmdc required — uses only Python stdlib.

Usage:
  python scripts/render_mermaid.py input.mermaid -o output.png
  python scripts/render_mermaid.py input.mermaid -o output.svg
"""

from __future__ import annotations

import argparse
import base64
import sys
import urllib.request
from pathlib import Path


def render(mermaid_text: str, fmt: str = "png") -> bytes:
    """Fetch a rendered image from mermaid.ink."""
    encoded = base64.urlsafe_b64encode(mermaid_text.encode("utf-8")).decode("ascii")
    if fmt == "svg":
        url = f"https://mermaid.ink/svg/{encoded}"
    else:
        url = f"https://mermaid.ink/img/{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": "render_mermaid/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main() -> int:
    parser = argparse.ArgumentParser(description="Render Mermaid to PNG/SVG via mermaid.ink")
    parser.add_argument("input", help="Path to .mermaid file")
    parser.add_argument("-o", "--output", required=True, help="Output path (.png or .svg)")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        print(f"Input not found: {src}", file=sys.stderr)
        return 1

    mermaid_text = src.read_text(encoding="utf-8")
    ext = Path(args.output).suffix.lower()
    fmt = "svg" if ext == ".svg" else "png"

    try:
        data = render(mermaid_text, fmt)
    except Exception as e:
        print(f"Render failed for {src}: {e}", file=sys.stderr)
        return 1

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_bytes(data)
    print(f"Wrote {args.output} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
