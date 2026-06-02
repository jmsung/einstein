"""Tests for the generic dual-gate ULP-polish library (einstein.ulp_polish).

Covers the reusable core extracted in Phase 2a:
- `ulp_neighbors` bit-level stepping (round-trip, ordering, not multiplicative).
- `to_mp` reads the exact binary float64, not the shortest decimal.
- `dual_gate_accept` implements the four-quadrant table from
  findings/mpmath-ulp-polish-dual-gate-p14.md (accept only when feasible AND
  float64-not-worse AND exact-strictly-better).
- `ulp_polish` climbs a synthetic capped objective to its feasibility ceiling
  and stops, never violating the dual gate.
"""

from __future__ import annotations

import struct
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

_REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_REPO / "src"))

from einstein.ulp_polish import (  # noqa: E402
    dual_gate_accept,
    to_mp,
    ulp_neighbors,
    ulp_polish,
)

# ---------------- ulp_neighbors ----------------


def test_ulp_neighbors_are_bit_steps():
    x = 0.11514888016002124
    nbrs = ulp_neighbors(x, steps=(-2, -1, 1, 2))
    assert len(nbrs) == 4
    assert nbrs[0] < nbrs[1] < x < nbrs[2] < nbrs[3]
    bits = struct.unpack("<q", struct.pack("<d", x))[0]
    plus1 = struct.unpack("<d", struct.pack("<q", bits + 1))[0]
    assert ulp_neighbors(x, steps=(1,))[0] == plus1
    assert plus1 != x * (1 + 1e-16)  # NOT multiplicative scaling


def test_ulp_neighbors_round_trip():
    x = 0.5
    plus1 = ulp_neighbors(x, steps=(1,))[0]
    back = ulp_neighbors(plus1, steps=(-1,))[0]
    assert back == x


# ---------------- to_mp ----------------


def test_to_mp_uses_exact_binary_value():
    mp.mp.dps = 80
    arr = np.array([[0.1, 0.1]], dtype=np.float64)
    got = to_mp(arr)[0][0]
    assert got == mp.mpf(float(0.1)), "must equal exact binary 0.1"
    assert got != mp.mpf("0.1"), "must NOT equal the decimal-parsed 0.1"


# ---------------- dual_gate_accept (the four-quadrant table) ----------------


def _merits():
    """A toy 1-coord problem: merit = the single value, exact via mpmath."""

    def merit_f64(c):
        return float(c[0, 0])

    def merit_mp(c, dps):
        return mp.mpf(float(c[0, 0]))

    return merit_f64, merit_mp


def test_dual_gate_accepts_genuine_improvement():
    mp.mp.dps = 50
    merit_f64, merit_mp = _merits()
    cur = np.array([[0.5]], dtype=np.float64)
    cand = np.array([[ulp_neighbors(0.5, (1,))[0]]], dtype=np.float64)  # +1 ulp
    out = dual_gate_accept(
        cand,
        0,
        cur_f64=0.5,
        cur_mp=mp.mpf(0.5),
        merit_f64=merit_f64,
        merit_mp=merit_mp,
        dps=50,
        feasible=None,
    )
    assert out is not None and out > mp.mpf(0.5)


def test_dual_gate_rejects_float64_regression():
    """A move that lowers the float64 merit is rejected even if exact says up.

    Mirrors the finding's "float64-regress" quadrant: the arena scores in
    float64, so a float64-worse move can never be banked."""
    mp.mp.dps = 50
    merit_f64, _ = _merits()

    # Exact says strictly up, float64 says down → must reject.
    def merit_mp_up(c, dps):
        return mp.mpf(float(c[0, 0])) + mp.mpf(1)

    down = np.array([[ulp_neighbors(0.5, (-1,))[0]]], dtype=np.float64)
    out = dual_gate_accept(
        down,
        0,
        cur_f64=0.5,
        cur_mp=mp.mpf(0.5),
        merit_f64=merit_f64,
        merit_mp=merit_mp_up,
        dps=50,
        feasible=None,
    )
    assert out is None


def test_dual_gate_rejects_no_exact_improvement():
    """float64-not-worse but exact-not-better (a tie) → reject (no real gain)."""
    mp.mp.dps = 50
    merit_f64, merit_mp = _merits()
    same = np.array([[0.5]], dtype=np.float64)
    out = dual_gate_accept(
        same,
        0,
        cur_f64=0.5,
        cur_mp=mp.mpf(0.5),
        merit_f64=merit_f64,
        merit_mp=merit_mp,
        dps=50,
        feasible=None,
    )
    assert out is None


def test_dual_gate_rejects_infeasible():
    """An exact-and-float64 improvement that violates feasibility → reject."""
    mp.mp.dps = 50
    merit_f64, merit_mp = _merits()
    cand = np.array([[ulp_neighbors(0.5, (1,))[0]]], dtype=np.float64)
    out = dual_gate_accept(
        cand,
        0,
        cur_f64=0.5,
        cur_mp=mp.mpf(0.5),
        merit_f64=merit_f64,
        merit_mp=merit_mp,
        dps=50,
        feasible=lambda c, k: False,
    )
    assert out is None


# ---------------- ulp_polish engine ----------------


def test_ulp_polish_climbs_to_feasibility_ceiling():
    """Maximise two coords by ulp steps, each capped 3 ulps above its start.

    The engine should climb each coord exactly to its ceiling and stop — never
    overshooting (feasibility) and never stalling early (it keeps sweeping while
    a feasible improving move exists)."""
    mp.mp.dps = 60
    start_vals = np.array([[0.5], [0.25]], dtype=np.float64)
    ceilings = [ulp_neighbors(0.5, (3,))[0], ulp_neighbors(0.25, (3,))[0]]

    def merit_f64(c):
        return float(np.sum(c))

    def merit_mp(c, dps):
        return mp.fsum(mp.mpf(float(v)) for v in c[:, 0])

    def feasible(c, key):
        i = key
        return c[i, 0] <= ceilings[i]

    def candidates_for(c, key):
        i = key
        for v in ulp_neighbors(c[i, 0], (1, 2)):
            if v > c[i, 0]:
                cand = c.copy()
                cand[i, 0] = v
                yield cand

    polished, info = ulp_polish(
        start_vals,
        keys=range(2),
        candidates_for=candidates_for,
        merit_f64=merit_f64,
        merit_mp=merit_mp,
        report_f64=lambda c: float(np.sum(c)),
        feasible=feasible,
        dps=60,
        max_iter=50,
    )
    assert polished[0, 0] == ceilings[0]
    assert polished[1, 0] == ceilings[1]
    assert info.delta > 0
    assert info.n_accept >= 2
    # converged before the cap (climbed 3 ulps each → a few sweeps, not 50)
    assert info.sweeps < 50
