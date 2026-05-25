#!/usr/bin/env python3
"""slsqp_polish.py — strict-tol SLSQP polisher for P14 (Circle Packing in Square, n=26).

Wraps `src/einstein/circle_packing_square/polish.polish()` with the
autonomous-loop dispatch contract:

  - Reads the canonical warm-start from `scripts/circle_packing_square/seeds/p14_canonical.json`
    (in-repo, deterministic — no dependence on the gitignored `results-temp/`).
  - Runs SLSQP at **strict tol=0** (`overlap_slack=0.0`) — every pair contact
    is forbidden to overlap, every wall constraint is forbidden to violate.
    This is the closed-loop axiom-A1 contract: triple-verify the result with
    `evaluator.evaluate_strict()` before reporting a score.
  - Emits `{"score": float, "payload": {"circles": [[cx, cy, r] × 26]}}` to
    `results/circle_packing_square/slsqp_polish_result.json` per the
    `json_score_payload` parser in `optimizer_dispatch.py`.

Why this exists (Goal-7 dogfood receipt):
  The autonomous loop's first live LLM cycle (P14, 2026-05-24) diagnosed that
  the only optimizer wired for P14 — `newton_max` — defaults to
  `--pair-gap=-9e-10`, the arena-tolerance-band exploit explicitly rejected
  after the 2026-04-09 false-breakthrough 500-pt penalty. See
  `docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md` and the
  open question
  `docs/wiki/questions/2026-05-24-p14-strict-tol-manifest-wiring.md`.
  This script is the answer.

Usage (via dispatch):
    uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy slsqp_polish

Usage (standalone):
    uv run python scripts/circle_packing_square/slsqp_polish.py
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

# Make src/einstein importable when invoked as a script (cwd=repo root).
_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.circle_packing_square.evaluator import evaluate_strict  # noqa: E402
from einstein.circle_packing_square.polish import polish  # noqa: E402

DEFAULT_SEED = _REPO / "scripts" / "circle_packing_square" / "seeds" / "p14_canonical.json"
DEFAULT_OUTPUT = _REPO / "results" / "circle_packing_square" / "slsqp_polish_result.json"

log = logging.getLogger("slsqp_polish")


def _load_seed(path: Path) -> list[list[float]]:
    if not path.is_file():
        raise FileNotFoundError(
            f"warm-start seed not found at {path}. The seed lives in-repo at "
            f"`scripts/circle_packing_square/seeds/p14_canonical.json`; if it's "
            f"missing, the wire-fix branch wasn't installed correctly."
        )
    data = json.loads(path.read_text())
    circles = data.get("circles") or data
    if not isinstance(circles, list) or len(circles) != 26:
        raise ValueError(
            f"seed {path} must contain a 26-element circles list, got "
            f"{type(circles).__name__} of length "
            f"{len(circles) if hasattr(circles, '__len__') else '?'}"
        )
    return circles


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--seed",
        type=Path,
        default=DEFAULT_SEED,
        help=f"Warm-start JSON (default: {DEFAULT_SEED}).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Result file path (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--maxiter",
        type=int,
        default=1000,
        help="SLSQP iteration cap (default 1000).",
    )
    parser.add_argument(
        "--ftol",
        type=float,
        default=1e-16,
        help="SLSQP ftol (default 1e-16).",
    )
    args = parser.parse_args(argv)

    circles = _load_seed(args.seed)
    log.info("loaded warm-start: %d circles from %s", len(circles), args.seed)

    polished, info = polish(
        initial_circles=circles,
        method="SLSQP",
        maxiter=args.maxiter,
        ftol=args.ftol,
        overlap_slack=0.0,  # STRICT — no pair overlap allowed
        verbose=False,
    )
    log.info(
        "polish: success=%s n_iter=%s score=%.14f",
        info.get("success"),
        info.get("n_iter"),
        info.get("score"),
    )

    # Triple-verify shoulder: re-score via the strict evaluator to ensure the
    # polished configuration actually satisfies the arena's tolerance contract.
    # evaluate_strict raises if any pair overlaps or wall is violated.
    payload = {"circles": polished.tolist()}
    strict_score = evaluate_strict(payload)
    log.info("strict evaluator score: %.14f", strict_score)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            {"score": float(strict_score), "payload": payload},
            indent=2,
        )
    )
    log.info("wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
