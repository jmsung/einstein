"""P13 push: BH + L-BFGS with STRICT scallop bounds.

Fixes the scallop-crossing bug in push_e. Parameterizes each x_i as:
    x_i = scallop_lo_i + (scallop_hi_i - scallop_lo_i) * sigmoid(raw_i)
This GUARANTEES each point stays within its assigned scallop, so the fixed
k_vec formulas remain valid.

Between BH steps, reassigns scallops based on the best solution found.
"""

import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import assign_scallops, load_xs_from_solution, turan_y_torch  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")
MB_SOL = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-13-edges-triangles/solutions"
torch.set_default_dtype(torch.float64)


def scallop_bounds(k: np.ndarray, eps: float = 1e-12) -> tuple[np.ndarray, np.ndarray]:
    """For each k, return (x_lo, x_hi) scallop interval with margin."""
    lo = 1.0 - 1.0 / k + eps
    hi = 1.0 - 1.0 / (k + 1) - eps
    return lo, hi


def score_torch_bounded(
    raw: torch.Tensor,
    bi_xs: torch.Tensor,
    lo: torch.Tensor,
    hi: torch.Tensor,
    k_vec: torch.Tensor,
) -> torch.Tensor:
    """Differentiable score. raw → x via per-point sigmoid bounds.

    raw: (m,) unconstrained
    lo, hi: (m,) scallop bounds
    k_vec: (m,) integer scallop
    """
    xs = lo + (hi - lo) * torch.sigmoid(raw)
    # Sort by xs (differentiable via gather — but we need the perm)
    sort_idx = torch.argsort(xs)
    xs_sorted = xs[sort_idx]
    k_sorted = k_vec[sort_idx]
    ys = turan_y_torch(xs_sorted, k_sorted)

    zero = torch.zeros(1, dtype=xs.dtype)
    one = torch.ones(1, dtype=xs.dtype)
    bi_ys = torch.zeros_like(bi_xs)

    xs_full = torch.cat([zero, bi_xs, xs_sorted, one])
    ys_full = torch.cat([zero, bi_ys, ys, one])

    hs = xs_full[1:] - xs_full[:-1]
    dys = ys_full[1:] - ys_full[:-1]
    y1 = ys_full[1:]
    y0 = ys_full[:-1]

    area_a = y1 * hs
    area_b = -dys * dys / 6.0 + y1 * hs
    area_c = y0 * hs + 1.5 * hs * hs
    area_per = torch.where(dys < 0, area_a, torch.where(dys <= 3.0 * hs, area_b, area_c))
    area = area_per.sum()
    max_gap = hs.max()
    return -(area + 10.0 * max_gap)


def inverse_sigmoid_param(xs: np.ndarray, lo: np.ndarray, hi: np.ndarray) -> np.ndarray:
    """Invert xs = lo + (hi-lo)*sigmoid(raw) → raw."""
    u = (xs - lo) / (hi - lo)
    u = np.clip(u, 1e-14, 1 - 1e-14)
    return np.log(u / (1 - u))


def lbfgs_polish_bounded(
    multi_xs: np.ndarray, bi_xs: np.ndarray,
    max_rounds: int = 40,
) -> tuple[np.ndarray, float]:
    """L-BFGS with strict scallop bounds."""
    k_np = assign_scallops(multi_xs)
    lo_np, hi_np = scallop_bounds(k_np)
    # Clamp starting point into bounds
    multi_clamped = np.clip(multi_xs, lo_np, hi_np)
    raw_np = inverse_sigmoid_param(multi_clamped, lo_np, hi_np)

    bi_t = torch.tensor(bi_xs, dtype=torch.float64)
    lo_t = torch.tensor(lo_np, dtype=torch.float64)
    hi_t = torch.tensor(hi_np, dtype=torch.float64)
    k_t = torch.tensor(k_np, dtype=torch.int64)
    raw = torch.tensor(raw_np, dtype=torch.float64, requires_grad=True)

    opt = torch.optim.LBFGS(
        [raw], lr=1.0, max_iter=30,
        tolerance_grad=1e-18, tolerance_change=1e-18,
        history_size=80, line_search_fn="strong_wolfe",
    )

    def closure():
        opt.zero_grad()
        s = score_torch_bounded(raw, bi_t, lo_t, hi_t, k_t)
        loss = -s
        loss.backward()
        return loss

    best_score = -float("inf")
    best_raw = raw.detach().clone()
    prev = None
    for r in range(max_rounds):
        loss = opt.step(closure)
        cur = -loss.item()
        if cur > best_score:
            best_score = cur
            best_raw = raw.detach().clone()
        if prev is not None and abs(cur - prev) < 1e-17:
            break
        prev = cur

    with torch.no_grad():
        new_xs = lo_t + (hi_t - lo_t) * torch.sigmoid(best_raw)
        new_xs = torch.sort(new_xs).values.numpy()
    return new_xs, best_score


def true_score(bi_xs: np.ndarray, multi_xs: np.ndarray) -> float:
    all_xs = np.concatenate([bi_xs, multi_xs])
    w = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
    return compute_score(w)


def save_solution(bi_xs: np.ndarray, multi_xs: np.ndarray, tag: str) -> Path:
    all_xs = np.concatenate([bi_xs, multi_xs])
    w = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
    score = compute_score(w)
    out = RESULTS / f"solution-{tag}.json"
    with open(out, "w") as f:
        json.dump({"weights": w.tolist()}, f)
    print(f"  Saved {out}  score={score:.14f}")
    MB_SOL.mkdir(parents=True, exist_ok=True)
    shutil.copy2(out, MB_SOL / f"solution-push-g-{score:.10f}.json")
    return out


def perturb_log_gaps(
    multi_xs: np.ndarray, x_lo: float, x_hi: float,
    noise_scale: float, rng: np.random.Generator,
) -> np.ndarray:
    gaps = np.empty(len(multi_xs) + 1)
    gaps[0] = multi_xs[0] - x_lo
    gaps[1:-1] = np.diff(multi_xs)
    gaps[-1] = x_hi - multi_xs[-1]
    gaps = np.maximum(gaps, 1e-15)
    log_gaps = np.log(gaps) + rng.normal(0, noise_scale, size=len(gaps))
    new_gaps = np.exp(log_gaps)
    new_gaps = new_gaps / new_gaps.sum() * (x_hi - x_lo)
    new_multi = x_lo + np.cumsum(new_gaps[:-1])
    return np.sort(np.clip(new_multi, x_lo + 1e-14, x_hi - 1e-14))


def main():
    sol_path = RESULTS / "solution.json"
    bi_xs, multi_xs = load_xs_from_solution(sol_path)
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f} ({len(multi_xs)} multipartite pts)")

    # Initial polish
    print("\n=== Initial bounded L-BFGS polish ===")
    polished, torch_score = lbfgs_polish_bounded(multi_xs, bi_xs, max_rounds=50)
    polished_true = true_score(bi_xs, polished)
    print(f"torch={torch_score:.14f}  true={polished_true:.14f}  delta={polished_true-init_score:+.2e}")

    best_multi = polished if polished_true > init_score else multi_xs.copy()
    best_score = max(init_score, polished_true)

    # BH with bounded L-BFGS as local minimizer
    SEEDS = 30
    NOISE_LEVELS = [0.3, 0.2, 0.12, 0.08, 0.05, 0.03, 0.02, 0.01]

    print(f"\n=== BH + Bounded L-BFGS ({SEEDS} seeds × {len(NOISE_LEVELS)} levels) ===")
    t0 = time.time()
    n_improvements = 0

    for seed in range(SEEDS):
        rng = np.random.default_rng(seed * 31 + 7)
        base = best_multi.copy()
        for noise in NOISE_LEVELS:
            pert = perturb_log_gaps(base, 0.5, 0.95, noise, rng)
            try:
                pol, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=30)
                sc = true_score(bi_xs, pol)
            except Exception:
                continue
            if sc > best_score + 1e-13:
                best_multi = pol.copy()
                best_score = sc
                n_improvements += 1
                print(f"  seed={seed:2d} noise={noise:.3f}: {sc:.14f} NEW BEST (+{sc-init_score:.3e})")
                base = pol.copy()
                save_solution(bi_xs, best_multi, f"push-g-intermediate-seed{seed}")

    elapsed = time.time() - t0
    print(f"\nDone. {n_improvements} improvements in {elapsed:.0f}s")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    if best_score > init_score + 1e-12:
        save_solution(bi_xs, best_multi, "push-g-final")
        print("\n** IMPROVED — saved as solution-push-g-final.json")


if __name__ == "__main__":
    main()
