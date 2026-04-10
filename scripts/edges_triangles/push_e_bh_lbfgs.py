"""P13 push: Basin-hopping with L-BFGS as local minimizer.

Combines perturbation (escapes basins) with true gradient optimization.
Re-assigns scallop indices after each perturbation so points can migrate
across scallop boundaries (the previous optimizer held k fixed).
"""

import json
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_densities, compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import (  # noqa: E402
    assign_scallops,
    initialize_raw_gaps_from_multi,
    load_xs_from_solution,
    score_torch,
)

RESULTS = Path("results/problem-13-edges-triangles")
torch.set_default_dtype(torch.float64)


def lbfgs_polish(
    multi_xs: np.ndarray, bi_xs: np.ndarray, x_lo: float, x_hi: float,
    max_rounds: int = 20,
) -> tuple[np.ndarray, float]:
    """L-BFGS from given multi_xs, returns (new_multi_xs, score)."""
    bi_t = torch.tensor(bi_xs, dtype=torch.float64)
    k_np = assign_scallops(multi_xs)
    k_t = torch.tensor(k_np, dtype=torch.int64)
    raw_np = initialize_raw_gaps_from_multi(multi_xs, x_lo, x_hi)
    raw = torch.tensor(raw_np, dtype=torch.float64, requires_grad=True)

    opt = torch.optim.LBFGS(
        [raw], lr=1.0, max_iter=30,
        tolerance_grad=1e-18, tolerance_change=1e-18,
        history_size=80, line_search_fn="strong_wolfe",
    )

    best_score = -float("inf")
    best_raw = raw.detach().clone()

    def closure():
        opt.zero_grad()
        s = score_torch(raw, bi_t, k_t, x_lo, x_hi)
        loss = -s
        loss.backward()
        return loss

    prev_score = None
    for r in range(max_rounds):
        loss = opt.step(closure)
        with torch.no_grad():
            cur = -loss.item()
        if cur > best_score:
            best_score = cur
            best_raw = raw.detach().clone()
        if prev_score is not None and abs(cur - prev_score) < 1e-16:
            break
        prev_score = cur

    with torch.no_grad():
        pos = torch.nn.functional.softplus(best_raw)
        pos = pos / pos.sum() * (x_hi - x_lo)
        new_multi = (x_lo + torch.cumsum(pos[:-1], dim=0)).numpy()
    new_multi = np.clip(new_multi, x_lo + 1e-14, x_hi - 1e-14)
    new_multi.sort()
    return new_multi, best_score


def perturb_log_gaps(
    multi_xs: np.ndarray, x_lo: float, x_hi: float,
    noise_scale: float, rng: np.random.Generator,
) -> np.ndarray:
    """Perturb via log-gap noise (gap-space jump, preserves ordering)."""
    gaps = np.empty(len(multi_xs) + 1)
    gaps[0] = multi_xs[0] - x_lo
    gaps[1:-1] = np.diff(multi_xs)
    gaps[-1] = x_hi - multi_xs[-1]
    gaps = np.maximum(gaps, 1e-15)
    log_gaps = np.log(gaps) + rng.normal(0, noise_scale, size=len(gaps))
    new_gaps = np.exp(log_gaps)
    new_gaps = new_gaps / new_gaps.sum() * (x_hi - x_lo)
    new_multi = x_lo + np.cumsum(new_gaps[:-1])
    new_multi = np.clip(new_multi, x_lo + 1e-14, x_hi - 1e-14)
    new_multi.sort()
    return new_multi


def reconstruct_weights(bi_xs: np.ndarray, multi_xs: np.ndarray) -> np.ndarray:
    all_xs = np.concatenate([bi_xs, multi_xs])
    return np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])


def true_score(bi_xs: np.ndarray, multi_xs: np.ndarray) -> float:
    return compute_score(reconstruct_weights(bi_xs, multi_xs))


def save_solution(bi_xs: np.ndarray, multi_xs: np.ndarray, tag: str) -> Path:
    w = reconstruct_weights(bi_xs, multi_xs)
    score = compute_score(w)
    RESULTS.mkdir(parents=True, exist_ok=True)
    out = RESULTS / f"solution-{tag}.json"
    with open(out, "w") as f:
        json.dump({"weights": w.tolist()}, f)
    print(f"  Saved {out}  score={score:.14f}")
    backup_dir = os.environ.get("EINSTEIN_BACKUP_DIR")
    if backup_dir:
        bd = Path(backup_dir)
        bd.mkdir(parents=True, exist_ok=True)
        shutil.copy2(out, bd / f"solution-push-e-{score:.10f}.json")
    return out


def main():
    sol_path = RESULTS / "solution.json"
    bi_xs, multi_xs = load_xs_from_solution(sol_path)
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f} ({len(multi_xs)} multipartite pts)")

    x_lo, x_hi = 0.5, 0.95

    # First polish the starting point
    print("\n=== Initial L-BFGS polish ===")
    multi_polished, poli_score = lbfgs_polish(multi_xs, bi_xs, x_lo, x_hi, max_rounds=30)
    truth = true_score(bi_xs, multi_polished)
    print(f"After polish: torch={poli_score:.14f}  true={truth:.14f}")

    best_multi = multi_polished.copy()
    best_score = truth

    # Basin hopping with L-BFGS polish
    SEEDS = 16
    NOISE_SCHEDULE = [0.15, 0.1, 0.07, 0.05, 0.03, 0.02, 0.015, 0.01, 0.008, 0.005]

    print(f"\n=== BH+L-BFGS ({SEEDS} seeds × {len(NOISE_SCHEDULE)} noise levels) ===")
    t0 = time.time()
    n_improvements = 0

    for seed in range(SEEDS):
        rng = np.random.default_rng(seed * 7 + 13)
        base_multi = best_multi.copy()
        base_score = best_score
        for noise in NOISE_SCHEDULE:
            pert = perturb_log_gaps(base_multi, x_lo, x_hi, noise, rng)
            try:
                new_multi, new_torch = lbfgs_polish(pert, bi_xs, x_lo, x_hi, max_rounds=25)
                new_score = true_score(bi_xs, new_multi)
            except Exception as e:
                print(f"  seed={seed} noise={noise:.3f}: L-BFGS failed ({e})")
                continue
            improved = new_score > best_score + 1e-12
            marker = " NEW BEST" if improved else ("*" if new_score > base_score else "")
            if improved:
                best_multi = new_multi.copy()
                best_score = new_score
                n_improvements += 1
                print(f"  seed={seed:2d} noise={noise:.3f}: {new_score:.14f}{marker} (+{new_score-init_score:.2e})")
                base_multi = new_multi.copy()
                base_score = new_score
                # save intermediate
                save_solution(bi_xs, best_multi, f"push-e-seed{seed}-n{noise:.3f}".replace(".", "p"))
            elif new_score > base_score:
                print(f"  seed={seed:2d} noise={noise:.3f}: {new_score:.14f}{marker}")

    elapsed = time.time() - t0
    print(f"\nDone. {n_improvements} improvements in {elapsed:.0f}s")
    print(f"Initial : {init_score:.14f}")
    print(f"Final   : {best_score:.14f}")
    print(f"Gain    : {best_score - init_score:+.2e}")

    if best_score > init_score:
        save_solution(bi_xs, best_multi, "push-e-final")
        print("\n** IMPROVED — saved as solution-push-e-final.json")


if __name__ == "__main__":
    main()
