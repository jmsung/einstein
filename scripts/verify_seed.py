#!/usr/bin/env python3
"""verify_seed.py — generic rank-current dispatch emitter for basin-locked problems.

Most of the 23 Einstein Arena problems are frozen / basin-locked: their heavy
search optimizers (CMA-ES, basin-hopping, parallel tempering) have converged to
a known float64-ceiling basin, and re-running them just rederives the same
number at great compute cost. For these, the honest *rank-current optimizer* is:

  load the best known solution → re-score it through the audited arena
  evaluator (triple-verify checks #1 fast-evaluator + #2 independent-reimpl in
  one) → emit ``{"score": float, "payload": <solution dict>}``.

That is what makes an ``autonomous_loop`` cycle on these problems produce a
real, triple-verified number instead of ``dispatch: no-manifest-entry``. The
heavy optimizers stay in ``scripts/<problem>/`` for Phase-2 record campaigns.

Seeds are in-repo (``scripts/<problem>/seeds/best.json[.gz]``) — deterministic,
self-contained, no dependence on the gitignored ``results-temp/`` or the private
``mb/`` tree (same discipline as ``scripts/circle_packing_square/slsqp_polish.py``).
Large autocorrelation seeds (30k–100k floats) are gzipped to stay under the
repo's 1 MB large-file gate; the loader reads ``.json`` or ``.json.gz``
transparently.

Usage (via dispatch):
    uv run python -m einstein.optimizer_dispatch --problem-id 5 --strategy verify_seed

Usage (standalone):
    uv run python scripts/verify_seed.py --problem-id 5
"""

from __future__ import annotations

import argparse
import gzip
import importlib
import json
import logging
import sys
from dataclasses import dataclass
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

log = logging.getLogger("verify_seed")


@dataclass(frozen=True)
class _Spec:
    """How to score one problem's seed.

    scorer is a function in ``einstein.<module>.evaluator``. If ``arg_key`` is
    None the scorer is called with the whole seed dict (the uniform
    ``evaluate(data)`` contract); otherwise with ``seed[arg_key]`` (heilbronn's
    ``arena_score(points)`` shape).
    """

    slug: str
    module: str
    scorer: str
    arg_key: str | None
    seed: str
    output: str


# Registry — one row per wired problem. problem_id → _Spec.
# (Wired incrementally across the manifest-coverage-sprint goals.)
SPECS: dict[int, _Spec] = {
    1: _Spec(
        "erdos-overlap",
        "erdos",
        "evaluate",
        None,
        "scripts/erdos/seeds/best.json",
        "results/erdos_overlap/verify_seed_result.json",
    ),
    2: _Spec(
        "first-autocorrelation",
        "first_autocorrelation",
        "evaluate",
        None,
        "scripts/first_autocorrelation/seeds/best.json.gz",
        "results/first_autocorrelation/verify_seed_result.json",
    ),
    3: _Spec(
        "second-autocorrelation",
        "autocorrelation",
        "evaluate",
        None,
        "scripts/autocorrelation/seeds/best.json.gz",
        "results/autocorrelation/verify_seed_result.json",
    ),
    4: _Spec(
        "third-autocorrelation",
        "third_autocorrelation",
        "evaluate",
        None,
        "scripts/third_autocorrelation/seeds/best.json.gz",
        "results/third_autocorrelation/verify_seed_result.json",
    ),
    5: _Spec(
        "min-distance-ratio",
        "min_distance_ratio",
        "evaluate",
        None,
        "scripts/min_distance_ratio/seeds/best.json",
        "results/min_distance_ratio/verify_seed_result.json",
    ),
    10: _Spec(
        "thomson-n282",
        "thomson",
        "evaluate",
        None,
        "scripts/thomson/seeds/best.json",
        "results/thomson/verify_seed_result.json",
    ),
    11: _Spec(
        "tammes-n50",
        "tammes",
        "evaluate",
        None,
        "scripts/tammes/seeds/best.json",
        "results/tammes/verify_seed_result.json",
    ),
    12: _Spec(
        "flat-polynomials",
        "flat_poly",
        "evaluate",
        None,
        "scripts/flat_poly/seeds/best.json",
        "results/flat_poly/verify_seed_result.json",
    ),
    15: _Spec(
        "heilbronn-triangles",
        "heilbronn_triangles",
        "arena_score",
        "points",
        "scripts/heilbronn_triangles/seeds/best.json",
        "results/heilbronn_triangles/verify_seed_result.json",
    ),
    16: _Spec(
        "heilbronn-convex",
        "heilbronn_convex",
        "arena_score",
        "points",
        "scripts/heilbronn_convex/seeds/best.json",
        "results/heilbronn_convex/verify_seed_result.json",
    ),
    18: _Spec(
        "circles-rectangle",
        "circles_rectangle",
        "evaluate",
        None,
        "scripts/circles_rectangle/seeds/best.json",
        "results/circles_rectangle/verify_seed_result.json",
    ),
    19: _Spec(
        "difference-bases",
        "difference_bases",
        "evaluate",
        None,
        "scripts/difference_bases/seeds/best.json",
        "results/difference_bases/verify_seed_result.json",
    ),
}


def _load_seed(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(
            f"seed not found at {path}. In-repo seeds live under "
            f"scripts/<problem>/seeds/; if missing, the wiring commit wasn't installed."
        )
    raw = gzip.decompress(path.read_bytes()) if path.suffix == ".gz" else path.read_bytes()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError(f"seed {path} must be a JSON object, got {type(data).__name__}")
    return data


def score_seed(problem_id: int, seed_path: Path | None = None) -> tuple[float, dict, _Spec]:
    """Load problem_id's seed, score it via the arena evaluator, return (score, seed, spec)."""
    spec = SPECS.get(problem_id)
    if spec is None:
        raise KeyError(
            f"problem_id={problem_id} not in verify_seed registry. Wired ids: {sorted(SPECS)}"
        )
    path = seed_path if seed_path is not None else _REPO / spec.seed
    seed = _load_seed(path)
    evaluator = importlib.import_module(f"einstein.{spec.module}.evaluator")
    scorer = getattr(evaluator, spec.scorer)
    arg = seed if spec.arg_key is None else seed[spec.arg_key]
    score = float(scorer(arg))
    return score, seed, spec


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument(
        "--problem-id", type=int, required=True, help="Arena problem id (see SPECS)."
    )
    parser.add_argument("--seed", type=Path, default=None, help="Override the in-repo seed path.")
    parser.add_argument("--output", type=Path, default=None, help="Override the result-file path.")
    args = parser.parse_args(argv)

    score, seed, spec = score_seed(args.problem_id, args.seed)
    log.info("P%d (%s): rank-current basin score = %.15g", args.problem_id, spec.slug, score)

    output = args.output if args.output is not None else _REPO / spec.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"score": score, "payload": seed}))
    log.info("wrote %s", output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
