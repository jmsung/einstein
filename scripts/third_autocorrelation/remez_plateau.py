"""Goal 5 — Remez-on-the-plateau: exact active-set minimax descent (council move).

The leader's f★f is flat to 1e-6 over ~92% of t. Smooth-max L-BFGS has near-zero
gradient on a flat plateau, so it STALLS (returns the leader unchanged) — but a
stall is not a proof of minimality. The council (Tao stage B / Hilbert backup):
the correct final descent is a Remez/exchange step that pushes the ENTIRE active
plateau down together via an LP, which smooth-max cannot do.

Linearise: conv(f+δf)_k ≈ conv_k + 2·(M δf)_k,  M_{k,j}=f_{k-j}. For the active
set A (top-K conv positions) solve:
    min η  s.t.  conv_k + 2(M_A δf)_k ≤ η  (k∈A),  Σδf = 0 (keep ∫f),  |δf|≤tr
Then exact-C line-search f ← f + αδf, recompute A, iterate. If C drops below
1.4523043332 the leader basin had hidden headroom (smooth-max stall, not minimum).

Run from the leader at n=100000. Triple-verify; target 1.4522043.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import scipy.signal
from scipy.optimize import linprog

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import arena_c

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
OUT = Path("results/problem-4-third-autocorrelation")
K_ACTIVE = 400  # number of top conv positions used as active constraints
N_ITERS = 25


def active_rows(f, K):
    """M_A (K×n) with M_A[a,j]=f[k_a - j]; k_a = top-K conv positions. Plus conv_A."""
    n = len(f)
    conv = np.convolve(f, f, mode="full")  # length 2n-1
    A = np.argpartition(conv, -K)[-K:]
    A = A[np.argsort(conv[A])[::-1]]
    j = np.arange(n)
    idx = A[:, None] - j[None, :]  # (K, n)
    valid = (idx >= 0) & (idx < n)
    M = np.where(valid, f[np.clip(idx, 0, n - 1)], 0.0)
    return M, conv[A], conv.max()


def step(f, tr):
    n = len(f)
    M, convA, M_max = active_rows(f, K_ACTIVE)
    # vars: [δf (n), η (1)]. min η s.t. 2 M δf - η ≤ -convA ; Σδf=0 ; |δf|≤tr
    c = np.zeros(n + 1)
    c[-1] = 1.0
    A_ub = np.hstack([2.0 * M, -np.ones((K_ACTIVE, 1))])
    b_ub = -convA
    A_eq = np.zeros((1, n + 1))
    A_eq[0, :n] = 1.0
    b_eq = [0.0]
    bounds = [(-tr, tr)] * n + [(None, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method="highs")
    if not res.success:
        return f, arena_c(f), False
    df = res.x[:n]
    best_c, best_f, improved = arena_c(f), f, False
    for alpha in np.linspace(0.1, 1.5, 18):
        g = f + alpha * df
        if g.sum() <= 0:
            continue
        c2 = arena_c(g)
        if c2 < best_c - 1e-14:
            best_c, best_f, improved = c2, g, True
    return best_f, best_c, improved


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    f = np.array(json.load(open(LEADER))["values"], float)
    c = arena_c(f)
    tr = 0.02 * np.abs(f).mean()
    print(
        f"Remez-plateau from leader C={c:.13f} (target {TARGET:.13f}) K={K_ACTIVE} tr={tr:.3g}",
        flush=True,
    )
    for it in range(N_ITERS):
        t0 = time.time()
        f, c, improved = step(f, tr)
        print(
            f"[{it:2d}] C={c:.13f} {'↓' if improved else '(stall)'} ({time.time() - t0:.0f}s)",
            flush=True,
        )
        if not improved:
            tr *= 0.5
            if tr < 1e-6 * np.abs(f).mean():
                break
        json.dump(
            {"values": f.tolist(), "score": c, "n": len(f)}, open(OUT / "remez_best.json", "w")
        )

    dx = 0.5 / len(f)
    c1 = verify_and_compute(f.tolist())
    c2 = abs((scipy.signal.fftconvolve(f, f, "full") * dx).max()) / (f.sum() * dx) ** 2
    print(f"\nFINAL C={c:.13f} leader {LEADER_C:.13f} target {TARGET:.13f}")
    print(f"triple-verify: arena={c1:.13f} scipy={c2:.13f} spread={abs(c1 - c2):.2e}")
    print(
        "*** RECORD ***"
        if c < TARGET and abs(c1 - c2) < 1e-9
        else (
            "beats leader!"
            if c < LEADER_C - 1e-8
            else "leader basin has no headroom (stall confirmed)"
        )
    )


if __name__ == "__main__":
    main()
