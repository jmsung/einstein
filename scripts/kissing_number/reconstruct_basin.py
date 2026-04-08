"""Reconstruct a 594-vector starting point in the 0.156 basin.

Strategy:
1. Load AlphaEvolve 593 (Cohn MIT archive, dim 11, integer coords).
2. Generate several 594-extension candidates using different schemes.
3. Run a brief CPU SA-tempering polish on each to score them.
4. Output the best basin found, plus all candidates for downstream GPU polish.

This script tries to find ANY config in the ~0.156 basin (CHRONOS#1 = 0.15613312835806).
We do not need to beat CHRONOS here — that comes in the polish phase.

Usage:
    uv run python scripts/kissing_number/reconstruct_basin.py
    uv run python scripts/kissing_number/reconstruct_basin.py --strategy gap_search --steps 5000000
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.kissing_number.evaluator import overlap_loss

RESULTS = Path("results/problem-6-kissing-number")
MB_SOLUTIONS = Path.home() / "projects/workbench/memory-bank/einstein/docs/problem-6-kissing-number/solutions"
N = 594
D = 11


# ---------- evaluator helpers ----------

def score_unit(unit_vecs: np.ndarray) -> float:
    """Total overlap loss for unit vectors. Matches arena (594-vector) evaluator."""
    return overlap_loss(unit_vecs)


def fast_score(unit_vecs: np.ndarray) -> float:
    """Faster Gram-based score for hot loops. Matches arena to ~1e-15."""
    n = len(unit_vecs)
    g = unit_vecs @ unit_vecs.T
    i, j = np.triu_indices(n, k=1)
    cos = np.clip(g[i, j], -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
    return float(np.maximum(0.0, 2.0 - d).sum())


def incremental_loss(vecs: np.ndarray, idx: int, total: float, old_vec: np.ndarray) -> float:
    """O(n) loss update after changing vecs[idx]."""
    others = np.concatenate([vecs[:idx], vecs[idx + 1 :]], axis=0)
    old_cos = np.clip(old_vec @ others.T, -1.0, 1.0)
    old_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - old_cos))
    old_p = np.maximum(0.0, 2.0 - old_d)
    new_cos = np.clip(vecs[idx] @ others.T, -1.0, 1.0)
    new_d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - new_cos))
    new_p = np.maximum(0.0, 2.0 - new_d)
    return total - float(old_p.sum()) + float(new_p.sum())


# ---------- 594-extension strategies ----------

def load_alphaevolve_593() -> np.ndarray:
    """Load AlphaEvolve 593 unit vectors (length-1)."""
    with open(RESULTS / "alphaevolve_593.json") as f:
        data = json.load(f)
    X = np.array(data["vectors"], dtype=np.float64)
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def best_random_594th(U593: np.ndarray, n_trials: int, seed: int) -> tuple[np.ndarray, float]:
    """Best of N random unit vectors as the 594th."""
    rng = np.random.default_rng(seed)
    best_v = None
    best = float("inf")
    for _ in range(n_trials):
        v = rng.standard_normal(D)
        v /= np.linalg.norm(v)
        cos = np.clip(U593 @ v, -1.0, 1.0)
        d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
        loss = float(np.maximum(0.0, 2.0 - d).sum())
        if loss < best:
            best = loss
            best_v = v
    return best_v, best


def gap_seeking_594th(U593: np.ndarray, seed: int) -> tuple[np.ndarray, float]:
    """Place the 594th at the centroid of the largest spherical Voronoi gap.

    Approximation: pick 5K random directions, score, take the best, refine
    with a few gradient steps that push it AWAY from its 5 nearest existing
    vectors.
    """
    rng = np.random.default_rng(seed)
    cand = rng.standard_normal((5000, D))
    cand /= np.linalg.norm(cand, axis=1, keepdims=True)
    cos_max = np.clip(cand @ U593.T, -1.0, 1.0).max(axis=1)
    # Lower max-cos = farther from nearest neighbour = bigger gap
    v = cand[cos_max.argmin()]

    # Refine: 200 steps of repulsive Lennard-Jones-ish move away from nearest 10
    for _ in range(200):
        cos = U593 @ v
        top = np.argpartition(cos, -10)[-10:]
        push = -(U593[top] * (cos[top][:, None])).sum(axis=0)
        v = v + 1e-3 * push
        v /= np.linalg.norm(v)

    cos = np.clip(U593 @ v, -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
    loss = float(np.maximum(0.0, 2.0 - d).sum())
    return v, loss


def antipodal_594th(U593: np.ndarray) -> tuple[np.ndarray, float]:
    """Use -v for the vector with the smallest -cos pair (the most isolated antipode)."""
    g = U593 @ U593.T
    np.fill_diagonal(g, 1.0)
    # Find vector whose negative is least conflicting with the rest
    neg_cos = -U593 @ U593.T  # cos(-v_i, v_j) = -cos(v_i, v_j)
    np.fill_diagonal(neg_cos, -1.0)
    max_cos = neg_cos.max(axis=1)  # for each i, the worst conflict if we used -v_i
    i = int(max_cos.argmin())
    v = -U593[i]
    cos = np.clip(U593 @ v, -1.0, 1.0)
    d = 2.0 * np.sqrt(2.0 * np.maximum(0.0, 1.0 - cos))
    loss = float(np.maximum(0.0, 2.0 - d).sum())
    return v, loss


def noise_injected_594(seed_vecs: np.ndarray, noise: float, seed: int) -> np.ndarray:
    """Apply isotropic noise to all vectors and renormalise. Breaks integer rigidity."""
    rng = np.random.default_rng(seed)
    out = seed_vecs + rng.standard_normal(seed_vecs.shape) * noise
    out /= np.linalg.norm(out, axis=1, keepdims=True)
    return out


# ---------- SA tempering polish ----------

def sa_tempering(
    vecs: np.ndarray,
    n_replicas: int = 16,
    temps: tuple[float, float] = (1e-10, 1e-2),
    scale: float = 1e-3,
    n_steps: int = 200_000,
    seed: int = 0,
    swap_every: int = 200,
    label: str = "sa",
    time_budget_sec: float | None = None,
) -> tuple[np.ndarray, float]:
    """CPU parallel-tempering SA. Returns (best_vecs, best_loss).

    Hot temps explore basins; cold temps polish. Swaps adjacent replicas
    via Metropolis. Designed to escape from a 1.6-ish basin into 0.156.
    """
    rng = np.random.default_rng(seed)
    R = n_replicas
    T = np.geomspace(temps[0], temps[1], R)

    replicas = np.tile(vecs[None, :, :], (R, 1, 1))
    losses = np.array([fast_score(r) for r in replicas])
    best_loss = losses.min()
    best_vecs = replicas[int(losses.argmin())].copy()

    print(f"  [{label}] R={R} temps={temps[0]:.0e}..{temps[1]:.0e} scale={scale:.0e} init={best_loss:.6f}")
    t0 = time.time()
    accepts = swaps = 0

    for step in range(n_steps):
        # Per-replica perturbation: pick a random vector index
        for r in range(R):
            idx = int(rng.integers(N))
            old_v = replicas[r, idx].copy()
            new_v = old_v + rng.standard_normal(D) * scale
            new_v /= np.linalg.norm(new_v)
            replicas[r, idx] = new_v
            new_l = incremental_loss(replicas[r], idx, losses[r], old_v)
            dE = new_l - losses[r]
            if dE < 0 or rng.random() < np.exp(-dE / T[r]):
                losses[r] = new_l
                accepts += 1
                if losses[r] < best_loss:
                    best_loss = losses[r]
                    best_vecs = replicas[r].copy()
            else:
                replicas[r, idx] = old_v

        # Replica swaps every swap_every
        if (step + 1) % swap_every == 0:
            for parity in (0, 1):
                for r in range(parity, R - 1, 2):
                    dE = (losses[r] - losses[r + 1]) * (1.0 / T[r] - 1.0 / T[r + 1])
                    if dE < 0 or rng.random() < np.exp(min(50, dE)):
                        replicas[[r, r + 1]] = replicas[[r + 1, r]]
                        losses[[r, r + 1]] = losses[[r + 1, r]]
                        swaps += 1

        if (step + 1) % 5000 == 0:
            elapsed = time.time() - t0
            print(
                f"    step {step+1:>7d} | best={best_loss:.10f} | "
                f"hot={losses.max():.4f} cold={losses.min():.4f} | "
                f"acc={accepts/(R*(step+1))*100:.1f}% | {elapsed:.0f}s"
            )

        if time_budget_sec is not None and time.time() - t0 > time_budget_sec:
            print(f"    [{label}] time budget reached at step {step+1}")
            break

    print(f"  [{label}] DONE best={best_loss:.10f} ({time.time()-t0:.0f}s)")
    return best_vecs, best_loss


# ---------- driver ----------

def save(vecs: np.ndarray, score: float, tag: str) -> None:
    p = RESULTS / f"reconstruct_{tag}.json"
    with open(p, "w") as f:
        json.dump({"vectors": vecs.tolist(), "score": score, "tag": tag}, f)
    print(f"  saved → {p}")
    # Also back up to MB
    mb_p = MB_SOLUTIONS / f"reconstruct_{tag}_{score:.10f}.json"
    with open(mb_p, "w") as f:
        json.dump({"vectors": vecs.tolist(), "score": score, "tag": tag}, f)
    print(f"  backup → {mb_p}")


def update_best(vecs: np.ndarray, score: float) -> None:
    """Atomically update the best file if score is improved."""
    best_path = RESULTS / "solution_best.json"
    if best_path.exists():
        with open(best_path) as f:
            cur = json.load(f).get("score", float("inf"))
        if score >= cur:
            return
    with open(best_path, "w") as f:
        json.dump({"vectors": vecs.tolist(), "score": score, "source": "reconstruct_basin.py"}, f)
    print(f"  >>> NEW BEST: {score:.15f} (saved to {best_path})")
    # Also back up to MB immediately
    mb_p = MB_SOLUTIONS / f"solution-best-{score:.10f}.json"
    with open(mb_p, "w") as f:
        json.dump({"vectors": vecs.tolist(), "score": score, "source": "reconstruct_basin.py"}, f)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=20_000)
    parser.add_argument("--strategy", default="all", help="all|random|gap|antipode|noise1|noise2|scratch")
    parser.add_argument("--budget", type=int, default=120, help="seconds per strategy")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    print("=" * 70)
    print("RECONSTRUCT BASIN — Problem 6 Kissing Number")
    print(f"  steps={args.steps}  strategy={args.strategy}  budget={args.budget}s/strat")
    print("=" * 70)

    U593 = load_alphaevolve_593()
    print(f"AlphaEvolve 593: shape {U593.shape}, all unit norm")

    candidates: list[tuple[str, np.ndarray]] = []

    if args.strategy in ("all", "random"):
        v, lp = best_random_594th(U593, n_trials=200_000, seed=args.seed)
        seed = np.vstack([U593, v[None]])
        print(f"\n[seed=random]    594th overlap = {lp:.6f}, total = {fast_score(seed):.6f}")
        candidates.append(("random", seed))

    if args.strategy in ("all", "gap"):
        v, lp = gap_seeking_594th(U593, seed=args.seed)
        seed = np.vstack([U593, v[None]])
        print(f"\n[seed=gap]       594th overlap = {lp:.6f}, total = {fast_score(seed):.6f}")
        candidates.append(("gap", seed))

    if args.strategy in ("all", "antipode"):
        v, lp = antipodal_594th(U593)
        seed = np.vstack([U593, v[None]])
        print(f"\n[seed=antipode]  594th overlap = {lp:.6f}, total = {fast_score(seed):.6f}")
        candidates.append(("antipode", seed))

    if args.strategy in ("all", "noise1"):
        # Inject 1e-3 noise to all 594 (random 594th + noise)
        v, _ = best_random_594th(U593, n_trials=20_000, seed=args.seed + 1)
        s = np.vstack([U593, v[None]])
        s = noise_injected_594(s, noise=1e-3, seed=args.seed + 2)
        print(f"\n[seed=noise1e-3] init = {fast_score(s):.6f}")
        candidates.append(("noise1", s))

    if args.strategy in ("all", "noise2"):
        v, _ = best_random_594th(U593, n_trials=20_000, seed=args.seed + 3)
        s = np.vstack([U593, v[None]])
        s = noise_injected_594(s, noise=1e-2, seed=args.seed + 4)
        print(f"\n[seed=noise1e-2] init = {fast_score(s):.6f}")
        candidates.append(("noise2", s))

    if args.strategy in ("all", "scratch"):
        rng = np.random.default_rng(args.seed)
        s = rng.standard_normal((N, D))
        s /= np.linalg.norm(s, axis=1, keepdims=True)
        print(f"\n[seed=scratch]   init = {fast_score(s):.6f}")
        candidates.append(("scratch", s))

    print(f"\nPolishing {len(candidates)} candidates ({args.budget}s each)...\n")

    best_overall = (None, float("inf"), "")
    for tag, seed in candidates:
        # Wide-temperature SA: hot range to escape, cold to polish
        polished, score = sa_tempering(
            seed.copy(),
            n_replicas=12,
            temps=(1e-9, 1e-1),
            scale=5e-3,
            n_steps=args.steps,
            seed=args.seed + hash(tag) % 1000,
            label=tag,
            time_budget_sec=args.budget,
        )
        save(polished, score, tag)
        if score < best_overall[1]:
            best_overall = (polished, score, tag)
        update_best(polished, score)

    print("\n" + "=" * 70)
    print(f"BEST OVERALL: {best_overall[2]} → {best_overall[1]:.15f}")
    print(f"  CHRONOS #1:  0.156133128358060")
    print(f"  Need:        < 0.156133128358060 (minImprovement = 0)")
    print("=" * 70)


if __name__ == "__main__":
    main()
