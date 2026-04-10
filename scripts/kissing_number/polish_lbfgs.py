"""L-BFGS-B smooth polish for the norm-2 basin (P6 Kissing Number).

A smooth-surrogate alternative for many-vector simultaneous descent. We
optimize the unit vectors u (594 x 11) on the unit sphere via free
parameters x = u and re-project to ||u||=1 each evaluation. The smooth
loss is a softplus replacement of max(0, 2-d) plus a small regularizer
that pulls the norms back to 1.

After L-BFGS-B converges (or stalls), we re-project to norm=2 and re-score
with the SLOW path. If the slow score improves, we save.

Note: at scores below ~1e-13 the softplus noise floor (log(2)/beta) can
exceed the true hinge loss, in which case the exact-subgradient
`polish_hinge_gd.py` or `polish_ulp_coord.py` is the right tool instead.

Usage:
    uv run python scripts/kissing_number/polish_lbfgs.py [--maxiter 5000] [--beta 1e6]
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

from einstein.kissing_number.evaluator import overlap_loss

RESULTS = Path("results/problem-6-kissing-number")
MB_ROOT = os.environ.get("EINSTEIN_MB_ROOT")
MB_SOLUTIONS = (
    Path(MB_ROOT) / "docs/problem-6-kissing-number/solutions" if MB_ROOT else None
)
N = 594
D = 11
NORM = 2.0


def smooth_loss_and_grad(x_flat: np.ndarray, beta: float) -> tuple[float, np.ndarray]:
    """Compute softplus-smoothed overlap loss and its gradient w.r.t. unit vectors.

    Loss = sum_{i<j} softplus_beta(2 - d_ij)
         + 0.5 * mu * sum_i (||u_i||^2 - 1)^2     # norm regularizer
    where softplus_beta(z) = (1/beta) * log(1 + exp(beta * z)) approximates max(0, z).

    Computed in unit-vector space (free parameters), with the norm regularizer pinning
    each row to ||u||=1.
    """
    u = x_flat.reshape(N, D)
    # ||u_i||
    norms = np.linalg.norm(u, axis=1)
    # centers c_i = 2 * u / ||u||  (matches arena verifier)
    inv = 1.0 / norms
    c = 2.0 * u * inv[:, None]  # (N, D)

    # pairwise diffs and dists
    diff = c[:, None, :] - c[None, :, :]  # (N, N, D)
    dist2 = np.sum(diff * diff, axis=-1)  # (N, N)
    np.fill_diagonal(dist2, 4.0)  # safe: self-pair contributes 0
    dist = np.sqrt(dist2)
    z = 2.0 - dist  # (N, N), positive when overlapping

    # softplus_beta(z) = log(1 + exp(beta z)) / beta. Stable form:
    bz = beta * z
    # Use log1p(exp(bz)) when bz << 0; bz + log1p(exp(-bz)) when bz >> 0
    pos = bz > 0
    sp = np.where(pos, bz + np.log1p(np.exp(-np.where(pos, bz, 0.0))), np.log1p(np.exp(np.where(pos, 0.0, bz))))
    sp /= beta
    np.fill_diagonal(sp, 0.0)
    pair_loss = 0.5 * float(np.sum(sp))  # half because dist matrix is symmetric

    # gradient of softplus = sigmoid(bz)
    sig = 1.0 / (1.0 + np.exp(-bz))  # (N, N)
    np.fill_diagonal(sig, 0.0)

    # d sp/d z = sigmoid(bz)
    # d z / d c[i,k] = -d dist/d c[i,k] = -(c[i,k] - c[j,k])/dist
    # gradient w.r.t. c[i] aggregating over all j (and j over all i, factor 2 since pair counted twice in loss)
    safe_dist = np.where(dist > 1e-12, dist, 1.0)
    coef = sig / safe_dist  # (N, N)
    # grad_c[i, k] = sum_j coef[i,j] * (c[j,k] - c[i,k])  (with sign from -d/d c)
    # Actually: dpair_loss / dc[i] = sum_j sig * (-d dist/d c[i]) = sum_j sig * -(c[i]-c[j])/dist
    #                              = sum_j coef[i,j] * (c[j] - c[i])
    # but pair_loss = 0.5 * sum_{i,j} sp, so d/dc[i] pair_loss = sum_j coef[i,j] * (c[j] - c[i])
    grad_c = -coef.sum(axis=1)[:, None] * c + coef @ c  # (N, D)

    # chain rule: c = 2 * u * inv = 2 * u / ||u||
    # dc[i,k]/du[i,l] = 2 * (delta_kl / ||u|| - u[k] u[l] / ||u||^3)
    # grad_u[i] = (2/||u||) * (grad_c[i] - (grad_c[i] . u_hat) * u_hat)  where u_hat = u/||u||
    u_hat = u * inv[:, None]
    proj = np.sum(grad_c * u_hat, axis=1, keepdims=True)
    grad_u = (2.0 * inv[:, None]) * (grad_c - proj * u_hat)

    # norm regularizer: 0.5 * mu * sum_i (||u_i||^2 - 1)^2
    mu = 1.0
    norm_err = norms * norms - 1.0  # (N,)
    reg_loss = 0.5 * mu * float(np.sum(norm_err * norm_err))
    # d reg / d u[i,k] = mu * (||u||^2 - 1) * 2 * u[i,k] = 2*mu*norm_err[i]*u[i,k]
    grad_reg = 2.0 * mu * norm_err[:, None] * u

    return pair_loss + reg_loss, (grad_u + grad_reg).ravel()


def project_to_norm(u: np.ndarray, norm: float) -> np.ndarray:
    return norm * u / np.linalg.norm(u, axis=1, keepdims=True)


def save_best(v: np.ndarray, score: float) -> None:
    p = RESULTS / "solution_best.json"
    out = {"vectors": v.tolist(), "score": score, "source": "polish_lbfgs.py"}
    tmp = p.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(out, f)
    os.replace(tmp, p)
    if MB_SOLUTIONS is not None:
        MB_SOLUTIONS.mkdir(parents=True, exist_ok=True)
        mb_p = MB_SOLUTIONS / f"lbfgs-{score:.6e}.json"
        with open(mb_p, "w") as f:
            json.dump(out, f)
    print(f"  >>> SAVED {score:.15e}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maxiter", type=int, default=2000)
    parser.add_argument("--betas", type=str, default="1e6,1e7,1e8,1e9,1e10")
    parser.add_argument(
        "--warm-start",
        type=str,
        default=str(RESULTS / "solution_best.json"),
    )
    args = parser.parse_args()

    print("=" * 72)
    print("L-BFGS-B SMOOTH POLISH")
    print(f"Warm start: {args.warm_start}")
    print("=" * 72)

    with open(args.warm_start) as f:
        data = json.load(f)
    v = np.array(data["vectors"], dtype=np.float64)
    # Convert to unit-vector parameters
    u = v / np.linalg.norm(v, axis=1, keepdims=True)

    start_score = overlap_loss(project_to_norm(u, NORM))
    print(f"Start score (slow):  {start_score:.15e}")

    best_u = u.copy()
    best_score = start_score
    save_best(project_to_norm(best_u, NORM), best_score)

    betas = [float(b) for b in args.betas.split(",")]
    for beta in betas:
        print(f"\n--- L-BFGS-B beta={beta:.0e} maxiter={args.maxiter} ---")
        x0 = best_u.ravel()
        t0 = time.time()
        result = minimize(
            smooth_loss_and_grad,
            x0,
            jac=True,
            args=(beta,),
            method="L-BFGS-B",
            options={
                "maxiter": args.maxiter,
                "ftol": 1e-20,
                "gtol": 1e-18,
                "maxcor": 50,
                "disp": False,
            },
        )
        elapsed = time.time() - t0
        new_u = result.x.reshape(N, D)
        v_proj = project_to_norm(new_u, NORM)
        new_score = overlap_loss(v_proj)
        print(
            f"  result: smooth={result.fun:.3e} nit={result.nit} status={result.message} {elapsed:.0f}s"
        )
        print(f"  slow score after projection: {new_score:.15e}")
        if new_score < best_score:
            best_score = new_score
            best_u = new_u.copy()
            save_best(v_proj, best_score)
        else:
            print("  no improvement at slow path")

    print()
    print("=" * 72)
    print(f"FINAL: {best_score:.15e}")
    print("=" * 72)


if __name__ == "__main__":
    main()
