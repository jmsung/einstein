"""Goal 5 — Cohn's signed dual lower bound for P4 (decides feasibility of a record).

Cohn's certificate (no moment lifting, so it avoids the Lasserre-L2 collapse):
the objective is min C s.t. (f★f)_k ≤ C·(Σf)²·dx ∀k (signed f; only the positive
peak binds — negatives free). Dual: a nonnegative measure y_k ≥ 0 (Σy_k = 1) on
the autoconvolution lags with the Fourier-positivity certificate

    Σ_k y_k (f★f)_k ≥ λ (Σf)²   for ALL signed f
    ⟺  G(y) − λ·11ᵀ ⪰ 0,   where  G(y)_{ij} = y_{i+j}   (Hankel of the measure).

Then for any feasible f:  λ(Σf)² ≤ Σ y_k (f★f)_k ≤ max_k(f★f)_k = C(Σf)²·dx,
so  **C ≥ λ / dx**  — a valid lower bound for n-sample signed f.

Compute λ(n)/dx at increasing n. If it converges ≥ 1.4523, a record at 1.4522 is
INFEASIBLE (the infimum is ~the leader). If it stays below 1.4522, headroom
exists and the dual's active lags map the construction.

Usage: uv run python scripts/third_autocorrelation/signed_dual_bound.py
"""

from __future__ import annotations

import json
from pathlib import Path

import cvxpy as cp
import numpy as np

OUT = Path("results/problem-4-third-autocorrelation")
LEADER_C = 1.4523043331832


def dual_bound(n: int):
    """Solve the dual SDP at resolution n; return (bound_on_C, status)."""
    dx = 0.5 / n
    nlags = 2 * n - 1
    y = cp.Variable(nlags, nonneg=True)
    lam = cp.Variable()
    # G(y)_{ij} = y_{i+j}: Hankel matrix built as a linear map of y.
    # Build via index matrix: G = sum_k y_k * E_k where E_k has 1 on antidiagonal i+j=k.
    rows, cols = np.meshgrid(np.arange(n), np.arange(n), indexing="ij")
    kidx = (rows + cols).ravel()  # which lag each (i,j) maps to
    G = cp.reshape(y[kidx], (n, n), order="C")
    ones = np.ones((n, n))
    constraints = [cp.sum(y) == 1, G - lam * ones >> 0]
    prob = cp.Problem(cp.Maximize(lam), constraints)
    prob.solve(solver=cp.CLARABEL, verbose=False)
    if prob.status not in ("optimal", "optimal_inaccurate"):
        return None, prob.status
    return float(lam.value) / dx, prob.status


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for n in [20, 40, 60, 80, 100, 140, 180]:
        try:
            bound, status = dual_bound(n)
        except Exception as e:
            print(f"n={n}: ERROR {e}", flush=True)
            continue
        if bound is None:
            print(f"n={n}: solver status {status}", flush=True)
            continue
        verdict = (
            "record INFEASIBLE (bound ≥ leader)"
            if bound > LEADER_C - 1e-4
            else f"headroom to {bound:.6f}"
            if bound < LEADER_C - 1e-4
            else "near leader"
        )
        rows.append({"n": n, "bound": bound, "status": status})
        print(f"n={n:4d}: C ≥ {bound:.10f}   (leader {LEADER_C:.6f})  {verdict}", flush=True)
        json.dump({"leader": LEADER_C, "rows": rows}, open(OUT / "dual_bound.json", "w"), indent=2)

    if rows:
        best = max(r["bound"] for r in rows)
        print(f"\nStrongest lower bound: C ≥ {best:.10f}")
        if best > LEADER_C:
            print("⇒ leader is ABOVE the bound — consistent; record at 1.4522 may be feasible.")
        print(
            "Trend tells the story: rising toward 1.4523 ⇒ infimum≈leader (no record);"
            " saturating below 1.4522 ⇒ headroom exists."
        )


if __name__ == "__main__":
    main()
