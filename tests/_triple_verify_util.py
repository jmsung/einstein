"""Shared helpers for the per-problem triple-verify tests (Goal 2)."""

from __future__ import annotations

import gzip
import itertools
import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))


def load_seed(rel_path: str) -> dict:
    """Load a seed JSON (transparently gunzips ``.gz``) and unwrap any
    ``{"payload": ...}`` wrapper to the bare solution dict."""
    p = _REPO / rel_path
    raw = gzip.decompress(p.read_bytes()) if p.suffix == ".gz" else p.read_bytes()
    d = json.loads(raw)
    if "payload" in d and isinstance(d["payload"], dict):
        d = d["payload"]
    return d


def max_pairwise_delta(result) -> float:
    nums = [result.fast, result.exact, result.cross]
    assert all(n is not None for n in nums), f"missing numbers: {nums}"
    return max(abs(a - b) for a, b in itertools.combinations(nums, 2))
