"""Joint Riemannian SGD on all 4321 vectors with smoothed hinge loss.

Starts from BW16 + duplicate, perturbs all vectors together. This searches
for second-order escape paths from the 2.0 basin.
"""

from __future__ import annotations

import argparse
import time

import numpy as np

from einstein.p23_kissing_d16.baseline import bw16_plus_duplicate
from einstein.p23_kissing_d16.evaluator import overlap_loss_fast


def smooth_hinge_score_grad(vectors: np.ndarray, beta: float) -> tuple[float, np.ndarray]:
    """Returns (score, gradient) for smoothed hinge sum over all pairs."""
    norms = np.linalg.norm(vectors, axis=1)
    unit = vectors / norms[:, None]
    centers = 2.0 * unit
    n = len(centers)

    diff = centers[:, None, :] - centers[None, :, :]  # (n, n, 16)
    dist2 = (diff ** 2).sum(axis=-1) + 1e-30
    dist = np.sqrt(dist2)
    h = 2.0 - dist

    bh = beta * h
    bh_clip = np.minimum(bh, 30.0)
    sp = np.where(bh > 30.0, bh, np.log1p(np.exp(bh_clip)))
    iu, ju = np.triu_indices(n, k=1)
    score = float(sp[iu, ju].sum() / beta)

    sig = 1.0 / (1.0 + np.exp(-np.clip(bh, -500, 500)))
    np.fill_diagonal(sig, 0.0)
    sig[ju, iu] = 0.0  # only upper triangle
    weight = sig / dist  # weight for each pair, shape (n, n)
    grad_centers = -(weight[:, :, None] * diff).sum(axis=1) - (-(weight.T)[:, :, None] * diff.transpose(1, 0, 2)).sum(axis=1)
    # grad on c_i; equivalently, project: d centers / d unit = 2I; d unit / d v = (I - u u^T)/||v||
    grad_units = 2.0 * grad_centers
    grad_v = grad_units / norms[:, None]
    grad_v = grad_v - (np.einsum("ij,ij->i", grad_v, unit)[:, None] * unit)
    return score, grad_v


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--lr", type=float, default=1e-4)
    parser.add_argument("--beta", type=float, default=200.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--init-perturb", type=float, default=1e-4)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    v = bw16_plus_duplicate()
    # tiny random perturbation
    v = v + args.init_perturb * rng.standard_normal(v.shape)
    v /= np.linalg.norm(v, axis=1, keepdims=True)

    print(f"Initial smooth score: {smooth_hinge_score_grad(v, args.beta)[0]:.6f}")
    print(f"Initial hard score:   {overlap_loss_fast(v):.6f}")

    t0 = time.time()
    for step in range(args.steps):
        score, grad = smooth_hinge_score_grad(v, args.beta)
        if step % 10 == 0:
            hard = overlap_loss_fast(v)
            print(f"step {step:>4}  smooth={score:.8f}  hard={hard:.8f}  "
                  f"grad_norm={np.linalg.norm(grad):.2e}  elapsed={time.time()-t0:.0f}s", flush=True)
        v = v - args.lr * grad
        v /= np.linalg.norm(v, axis=1, keepdims=True)

    final_hard = overlap_loss_fast(v)
    print(f"\nFinal hard score: {final_hard:.8f}")


if __name__ == "__main__":
    main()
