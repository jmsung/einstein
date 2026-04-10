"""High-precision active-set polisher for P6 Kissing Number.

Strategy
--------
1. Lift vectors into mpmath at high dps.
2. Work on centers C = 2 * v / ||v|| directly; the constraint is ||C|| = 2.
3. Compute hinge-loss gradient in mpmath over all pairs with dist < 2 (the
   active set is a few-thousand-pair subset of the 176,121 total).
4. Tangential-project the gradient (remove radial component), step, then
   renormalize each center to ||C|| = 2 in mpmath.
5. Armijo backtracking on the mpmath score — accept only strict improvements.
6. Round to float64 periodically and re-evaluate — the arena ultimately
   receives float64 JSON, so the float64-rounded score is what counts.
7. Checkpoint to results/ on every new mpmath-best and f64-best.

Usage
-----
    uv run python scripts/kissing_number/polish_mpmath_active.py \
        --warm-start results/problem-6-kissing-number/solution_best.json \
        --budget 1800 --dps 50 --lr 1e-13
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
from mpmath import mp, mpf, sqrt as mpsqrt

from einstein.kissing_number.evaluator import overlap_loss_mpmath

N = 594
D = 11
RESULTS = Path("results/problem-6-kissing-number")
MB_ROOT = os.environ.get("EINSTEIN_MB_ROOT")
MB_SOLUTIONS = (
    Path(MB_ROOT) / "docs/problem-6-kissing-number/solutions" if MB_ROOT else None
)


def load_vectors(path: str) -> list[list[float]]:
    """Load vectors from either an arena API dump or a plain solution file."""
    with open(path) as f:
        data = json.load(f)
    if "data" in data and "vectors" in data["data"]:
        return data["data"]["vectors"]
    if "vectors" in data:
        return data["vectors"]
    raise ValueError(f"no vectors found in {path}")


def to_mp(vecs: list[list[float]]) -> list[list[mpf]]:
    """Lift float64 vectors to mpmath, preserving every bit via repr()."""
    return [[mpf(repr(float(x))) for x in row] for row in vecs]


def _compute_centers(V: list[list[mpf]]) -> list[list[mpf]]:
    """c_i = 2 * v_i / ||v_i|| in mpmath (arena's internal normalization)."""
    two = mpf(2)
    out = []
    for row in V:
        nrm = mpsqrt(sum(x * x for x in row))
        out.append([two * x / nrm for x in row])
    return out


def _f64_candidate_pairs(V: list[list[mpf]], margin: float = 1e-10) -> list[tuple[int, int]]:
    """Screen pairs likely to be active using vectorized float64 (on centers).

    We compute c_i = 2*v_i/||v_i|| in float64, then mark (i,j) a candidate
    when f64 dist² ≤ 4 + margin. f64 vs mpmath dist² differs by at most
    O(d*eps) ~ 1e-14, so margin=1e-10 is extremely safe.
    """
    v_arr = np.array([[float(x) for x in row] for row in V], dtype=np.float64)
    norms = np.linalg.norm(v_arr, axis=1, keepdims=True)
    c_arr = 2.0 * v_arr / norms
    gram = c_arr @ c_arr.T  # <c_i, c_j>
    n = c_arr.shape[0]
    # dist² = ||c_i||² + ||c_j||² - 2<c_i,c_j>; ||c||=2 ⇒ dist² = 8 - 2*gram
    dist2_f64 = 8.0 - 2.0 * gram
    iu, ju = np.triu_indices(n, k=1)
    d2 = dist2_f64[iu, ju]
    mask = d2 <= 4.0 + margin
    return list(zip(iu[mask].tolist(), ju[mask].tolist()))


def score_and_active_grad_v(
    V: list[list[mpf]], candidates: list[tuple[int, int]] | None = None
) -> tuple[mpf, list[list[mpf]], int]:
    """Compute mpmath overlap loss + descent direction on v.

    Loss: L = sum_{i<j} max(0, 2 - ||c_i - c_j||)  with c_i = 2 v_i / ||v_i||.

    Descent direction wrt v (for each pair (i,j) with dist_ij < 2):
        u_i = v_i / ||v_i||
        r_ij = (c_i - c_j) / dist_ij
        -∇_{v_i} L_{ij} = (2/||v_i||) * (r_ij - <r_ij, u_i> u_i)
    i.e. the tangential projection at u_i of r_ij, scaled by 2/||v_i||.

    We return descent_direction (already sign-flipped so callers can += it).
    """
    two = mpf(2)
    one = mpf(1)
    n = len(V)
    d = len(V[0])

    # norms and unit vectors
    nrm = [mpsqrt(sum(x * x for x in row)) for row in V]
    inv_nrm = [one / nrm[i] for i in range(n)]
    U = [[V[i][k] * inv_nrm[i] for k in range(d)] for i in range(n)]
    C = [[two * U[i][k] for k in range(d)] for i in range(n)]

    total = mpf(0)
    grad = [[mpf(0)] * d for _ in range(n)]
    n_active = 0

    if candidates is None:
        pair_iter = ((i, j) for i in range(n) for j in range(i + 1, n))
    else:
        pair_iter = iter(candidates)

    for i, j in pair_iter:
        Ci = C[i]
        Cj = C[j]
        diff = [Ci[k] - Cj[k] for k in range(d)]
        dist2 = sum(t * t for t in diff)
        dist = mpsqrt(dist2)
        if dist < two:
            total += two - dist
            n_active += 1
            inv_d = one / dist
            # r = diff / dist, unit vector from c_j toward c_i
            r = [diff[k] * inv_d for k in range(d)]
            # descent direction in c: +r for c_i (push away from j), -r for c_j
            # descent in v via chain rule: project (+r)/(-r) onto tangent space at u_i/u_j,
            # scaled by 2/||v||. Tangential projection: p(x, u) = x - <x,u> u.
            dot_i = sum(r[k] * U[i][k] for k in range(d))
            dot_j = sum(r[k] * U[j][k] for k in range(d))
            s_i = two * inv_nrm[i]  # = 2/||v_i||
            s_j = two * inv_nrm[j]
            for k in range(d):
                # v_i descent: s_i * (r - <r,u_i> u_i)
                grad[i][k] += s_i * (r[k] - dot_i * U[i][k])
                # v_j descent: s_j * (-r + <r,u_j> u_j)
                grad[j][k] += s_j * (-r[k] + dot_j * U[j][k])
    return total, grad, n_active


def step_v(
    V: list[list[mpf]], grad: list[list[mpf]], lr: mpf
) -> list[list[mpf]]:
    """Apply v_new = v + lr * grad. No renormalization — the score function
    normalizes internally, so the arena's normalization on submission matches.
    """
    d = len(V[0])
    return [[V[i][k] + lr * grad[i][k] for k in range(d)] for i in range(len(V))]


def mp_score_only(
    V: list[list[mpf]], candidates: list[tuple[int, int]] | None = None
) -> tuple[mpf, int]:
    """Score sum max(0, 2 - ||c_i-c_j||) for state V (v-space). Normalizes v→c internally."""
    two = mpf(2)
    n = len(V)
    d = len(V[0])

    nrm = [mpsqrt(sum(x * x for x in row)) for row in V]
    C = [[two * V[i][k] / nrm[i] for k in range(d)] for i in range(n)]

    total = mpf(0)
    n_active = 0

    if candidates is None:
        pair_iter = ((i, j) for i in range(n) for j in range(i + 1, n))
    else:
        pair_iter = iter(candidates)

    for i, j in pair_iter:
        Ci = C[i]
        Cj = C[j]
        diff2 = mpf(0)
        for k in range(d):
            t = Ci[k] - Cj[k]
            diff2 += t * t
        dist = mpsqrt(diff2)
        if dist < two:
            total += two - dist
            n_active += 1
    return total, n_active


def mp_to_f64(V: list[list[mpf]]) -> np.ndarray:
    """Round mpmath state v directly to float64. No re-normalization.

    The arena computes c_i = 2*v_i/||v_i|| in mpmath after it receives the
    submission, so the submitted v need only be nonzero. Re-normalizing v to
    exactly norm 2 in float64 before submission adds ~1 ulp per coordinate
    and destroys the precision we built up in mpmath.
    """
    return np.array([[float(x) for x in row] for row in V], dtype=np.float64)


def save_solution(v: np.ndarray, score: float, tag: str, seed: int = 0) -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    out = {
        "vectors": v.tolist(),
        "score": score,
        "source": f"polish_mpmath_active:seed{seed}:{tag}",
    }
    path = RESULTS / "solution_best_mpmath.json"
    # Only replace the global best if we're actually better than whatever's there
    try:
        with open(path) as f:
            cur_best = json.load(f).get("score", float("inf"))
    except FileNotFoundError:
        cur_best = float("inf")
    if score < cur_best:
        tmp = path.with_suffix(".json.tmp")
        with open(tmp, "w") as f:
            json.dump(out, f)
        os.replace(tmp, path)
    if MB_SOLUTIONS is not None:
        MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
        mb = MB_SOLUTIONS / f"mpmath-polish-seed{seed}-{tag}-{score:.6e}.json"
        with open(mb, "w") as f:
            json.dump(out, f)
    print(f"  >>> SAVED {score:.12e}  [seed={seed} {tag}]", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--warm-start",
        type=str,
        required=True,
        help="Path to warm-start solution JSON (arena dump or plain solution)",
    )
    parser.add_argument("--dps", type=int, default=50, help="mpmath precision")
    parser.add_argument("--budget", type=int, default=1800, help="seconds")
    parser.add_argument(
        "--lr",
        type=str,
        default="1e-14,1e-15,1e-16",
        help="Comma-separated list of step sizes (descending)",
    )
    parser.add_argument("--max-back", type=int, default=20)
    parser.add_argument(
        "--target",
        type=float,
        default=None,
        help="Optional score-to-beat for progress reporting (no default).",
    )
    parser.add_argument(
        "--verify-dps",
        type=int,
        default=80,
        help="High precision for final verification",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Random seed for input perturbation (0 = no noise)",
    )
    parser.add_argument(
        "--noise",
        type=float,
        default=0.0,
        help="Noise magnitude added to warm-start in units of ulps (~2.2e-16)",
    )
    args = parser.parse_args()

    target_str = f"target<{args.target:.4e}" if args.target is not None else "no target"
    print("=" * 78)
    print(f"MPMATH ACTIVE-SET POLISHER   dps={args.dps}   {target_str}")
    print("=" * 78)

    mp.dps = args.dps

    raw_vecs = load_vectors(args.warm_start)

    # Optional input perturbation for multi-seed exploration. The f64 polish
    # basin has thousands of equivalent local minima; different starting points
    # round to different f64 lattice points.
    if args.noise > 0.0:
        rng = np.random.default_rng(args.seed)
        arr = np.array(raw_vecs, dtype=np.float64)
        ulp = 2.220446049250313e-16
        perturb = rng.standard_normal(arr.shape) * (args.noise * ulp)
        arr = arr + perturb
        raw_vecs = arr.tolist()
        print(f"  [seed={args.seed}  noise={args.noise:g} ulps applied to warm-start]")

    V = to_mp(raw_vecs)

    # initial score + active candidate list
    start_cands = _f64_candidate_pairs(V, margin=1e-10)
    start_score, start_active = mp_score_only(V, candidates=start_cands)
    print(f"Warm-start: {args.warm_start}")
    print(
        f"  initial mpmath score = {float(start_score):.10e}  "
        f"(candidates={len(start_cands)}, active_mp={start_active})"
    )
    if args.target is not None:
        print(f"  margin vs target     = {args.target - float(start_score):+.4e}")

    best_V = [row[:] for row in V]
    best_score = start_score
    best_active = start_active

    # initial checkpoint: the warm-start round-tripped through mpmath (should be
    # bit-identical to the input f64 if to_mp is repr-based and mp_to_f64 is direct).
    v_f64 = mp_to_f64(best_V)
    f64_score = overlap_loss_mpmath(v_f64, dps=args.dps)
    print(f"  round-tripped score  = {f64_score:.10e}  (should equal warm-start)")
    best_f64_score = f64_score

    lrs = [mpf(x) for x in args.lr.split(",")]
    t_start = time.time()
    total_steps = 0

    for lr in lrs:
        if time.time() - t_start > args.budget:
            break
        print(f"\n--- lr = {float(lr):.0e} ---", flush=True)
        cur_lr = lr
        n_no_improve = 0
        while True:
            if time.time() - t_start > args.budget:
                print("  budget exhausted")
                break

            t0 = time.time()
            cands = _f64_candidate_pairs(best_V, margin=1e-10)
            cur_score, grad, n_act = score_and_active_grad_v(best_V, candidates=cands)
            # Armijo backtracking
            step_lr = cur_lr
            accepted = False
            for _back in range(args.max_back):
                new_V = step_v(best_V, grad, step_lr)
                new_score, new_act = mp_score_only(new_V, candidates=cands)
                if new_score < cur_score:
                    accepted = True
                    break
                step_lr = step_lr / mpf(2)
            dt = time.time() - t0
            total_steps += 1

            if accepted:
                delta = float(cur_score - new_score)
                best_V = new_V
                best_score = new_score
                best_active = new_act
                n_no_improve = 0
                print(
                    f"  step {total_steps:4d}  lr={float(step_lr):.1e}  "
                    f"mp={float(new_score):.6e}  act={new_act}  "
                    f"Δ={delta:+.2e}  [{dt:.1f}s]",
                    flush=True,
                )

                # periodically evaluate f64-rounded state
                target_hit = args.target is not None and float(new_score) < args.target
                if total_steps % 5 == 0 or target_hit:
                    v_f64 = mp_to_f64(best_V)
                    f64_score = overlap_loss_mpmath(v_f64, dps=args.dps)
                    if f64_score < best_f64_score:
                        best_f64_score = f64_score
                        save_solution(v_f64, f64_score, f"step{total_steps}", seed=args.seed)
                    print(
                        f"        f64_round={f64_score:.6e}  (best_f64={best_f64_score:.6e})",
                        flush=True,
                    )
            else:
                n_no_improve += 1
                print(
                    f"  step {total_steps:4d}  lr={float(cur_lr):.1e}  REJECTED  [{dt:.1f}s]",
                    flush=True,
                )
                if n_no_improve >= 3:
                    print("  stalled at this lr")
                    break

    # final high-precision verify
    mp.dps = args.verify_dps
    v_f64 = mp_to_f64(best_V)
    final_score = overlap_loss_mpmath(v_f64, dps=args.verify_dps)

    print()
    print("=" * 78)
    print(f"FINAL mpmath-continuous: {float(best_score):.10e}  (active={best_active})")
    print(f"FINAL f64-rounded:       {final_score:.10e}  (dps={args.verify_dps} verify)")
    print(f"Best f64 during run:     {best_f64_score:.10e}")
    if args.target is not None:
        print(f"Margin vs target:        {args.target - final_score:+.4e}")
    print(f"Total accepted steps:    {total_steps}")
    print("=" * 78)


if __name__ == "__main__":
    main()
