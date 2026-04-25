"""Multi-start L-BFGS on filler position with BW16 fixed.

For each random tangent direction u, L-BFGS from f = cos(δ)*v0 + sin(δ)*u
with smoothed hinge loss (softplus) over the 4321-pair set.

Logs the minimum non-trivial score achieved across all starts.
"""

from __future__ import annotations

import argparse
import time

import numpy as np
from scipy.optimize import minimize

from einstein.p23_kissing_d16.baseline import bw16_min_vectors
from einstein.p23_kissing_d16.evaluator import overlap_loss_fast


def hinge_score_filler(filler: np.ndarray, core_centers: np.ndarray) -> tuple[float, np.ndarray]:
    """Return (score, gradient) for hinge sum of filler against fixed core (centers c_i)."""
    f = filler / np.linalg.norm(filler)
    c_f = 2.0 * f
    diff = c_f[None, :] - core_centers
    dist = np.sqrt((diff ** 2).sum(axis=1))
    pen_active = dist < 2.0
    score = float(np.maximum(0.0, 2.0 - dist).sum())
    # Gradient w.r.t. unconstrained filler isn't trivial — return score only here.
    return score, None


def smooth_hinge(filler: np.ndarray, core_centers: np.ndarray, beta: float = 200.0) -> tuple[float, np.ndarray]:
    """Smooth hinge sum over filler vs fixed core centers.

    softplus(beta * h)/beta where h = 2 - dist. Returns scalar + gradient w.r.t. raw filler.
    """
    norm = np.linalg.norm(filler)
    f = filler / norm
    c_f = 2.0 * f
    diff = c_f[None, :] - core_centers  # (N, 16)
    dist2 = (diff ** 2).sum(axis=1)
    dist = np.sqrt(dist2 + 1e-30)
    h = 2.0 - dist  # (N,)
    bh = beta * h
    # softplus(x) = log(1 + e^x); use stable form
    sp = np.where(bh > 30, bh, np.log1p(np.exp(np.minimum(bh, 30))))
    score = float(sp.sum() / beta)

    # gradient: d sp / dh = sigmoid(bh)
    sig = 1.0 / (1.0 + np.exp(-np.clip(bh, -500, 500)))
    # d h / d c_f = -diff / dist
    dh_dc = -(diff / dist[:, None])  # (N, 16)
    # d c_f / d f = 2 I
    # d f / d filler (Jacobian of unit-normalize): (I - f f^T) / norm
    # so d f_k / d filler_l = (delta_kl - f_k f_l) / norm
    # gradient of sp wrt c_f: sum_i sig_i * dh_dc_i
    grad_cf = (sig[:, None] * dh_dc).sum(axis=0)  # (16,)
    grad_f = 2.0 * grad_cf
    grad_filler = (grad_f - (grad_f @ f) * f) / norm
    return score, grad_filler


def optimize_filler(core: np.ndarray, init: np.ndarray, beta_schedule=(50, 200, 1000)) -> tuple[float, np.ndarray]:
    """Filler-only L-BFGS with annealing."""
    core_centers = 2.0 * core / np.linalg.norm(core, axis=1, keepdims=True)
    f = init.copy()
    for beta in beta_schedule:
        res = minimize(
            lambda x: smooth_hinge(x, core_centers, beta=beta),
            f,
            jac=True,
            method="L-BFGS-B",
            options={"maxiter": 200, "ftol": 1e-18, "gtol": 1e-12},
        )
        f = res.x / np.linalg.norm(res.x)
    return overlap_loss_fast(np.vstack([core, f[None, :]])), f


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-starts", type=int, default=200)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--mode", choices=["random", "tangent"], default="tangent",
                        help="random=uniform on S^15; tangent=perturb v0 by random tangent")
    parser.add_argument("--delta", type=float, default=0.05, help="perturbation magnitude (tangent mode)")
    args = parser.parse_args()

    bw = bw16_min_vectors()
    v0 = bw[0]
    rng = np.random.default_rng(args.seed)

    best_score = np.inf
    best_filler = None
    t_start = time.time()
    for k in range(args.n_starts):
        if args.mode == "random":
            init = rng.standard_normal(16)
            init /= np.linalg.norm(init)
        else:
            u = rng.standard_normal(16)
            u -= (u @ v0) * v0
            u /= np.linalg.norm(u)
            init = np.cos(args.delta) * v0 + np.sin(args.delta) * u

        score, f = optimize_filler(bw, init)
        if score < best_score:
            best_score = score
            best_filler = f
            elapsed = time.time() - t_start
            print(f"[{k+1}/{args.n_starts}] new best score = {score:.10f} (elapsed {elapsed:.0f}s)")

    print(f"\nFinal best score after {args.n_starts} starts: {best_score:.12f}")


if __name__ == "__main__":
    main()
