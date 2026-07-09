"""Certified ceiling for the P7 board via a weak-duality box certificate.

For any entrywise-nonnegative dyadic dual y = Y/2^P (Y integer), the value
    B(y) = TOL * sum_m y_m  +  10 * sum_{k=2..K} |r_k|,
    r_k  = -(ln k)/k - N_k/(k*2^P),   N_k = sum_i Y_i*(k*floor(m_i/k) - m_i)
                                          = -sum_i Y_i*(m_i mod k)   [k*floor(m/k)-m = -(m mod k)]
is a certified UPPER bound on S*(K) = max_{f in [-10,10]} { -sum f(k)ln(k)/k :
sum_k f(k)(floor(m/k)-m/k) <= TOL }. (Weak LP duality; the box term is 10*|reduced cost|.)

N_k is exact big-integer; every ln(k)/k is an outward-rounded mpmath interval, so the
certified inequality has no unenclosed float. Replicates Russell/CHRONOS 2026
(DOI 10.5281/zenodo.21221207); source/2026-russell-pnt-ceiling-certificates.md.

    uv run python scripts/prime/ceiling_certify.py --dual <dual.npz>        # from an npz (m,Y,denom_pow,K)
    uv run python scripts/prime/ceiling_certify.py --verify-ref <K4800.npz> # reproduce their bound
"""

from __future__ import annotations

import argparse

import numpy as np
from mpmath import iv, mpf


def certify(m: np.ndarray, Y: np.ndarray, denom_pow: int, K: int, TOL: str = "1.0001",
            prec_bits: int = 400) -> dict:
    """Return the certified upper bound on S*(K) for dual y = Y/2^denom_pow."""
    iv.prec = prec_bits
    two_p = 1 << denom_pow
    m = m.astype(np.int64)
    Y_obj = Y.astype(object)  # exact Python ints

    sum_Y = int(Y_obj.sum())                       # exact
    sum_y = mpf(sum_Y) / mpf(two_p)                # for reporting

    # term1 = TOL * sum_y, as an interval (TOL is exact decimal -> rational)
    tol_iv = iv.mpf(TOL)
    term1 = tol_iv * (iv.mpf(sum_Y) / iv.mpf(two_p))

    # sum_k |r_k| certified upper. k*floor(m/k)-m = -(m mod k).
    sum_abs_r = iv.mpf(0)
    max_abs_r_f = 0.0
    ks = np.arange(2, K + 1, dtype=np.int64)
    for k in ks:
        res = (m % k)                              # small ints in [0, k)
        Nk = -int((Y_obj * res.astype(object)).sum())   # exact integer
        # r_k = -(ln k)/k - Nk/(k*2^P)  as an interval; |r_k| upper = max|endpoint|
        rk = -(iv.log(int(k)) / int(k)) - iv.mpf(Nk) / (iv.mpf(int(k)) * iv.mpf(two_p))
        ark = abs(rk)
        sum_abs_r = sum_abs_r + ark
        if float(ark.b) > max_abs_r_f:
            max_abs_r_f = float(ark.b)

    B = term1 + iv.mpf(10) * sum_abs_r
    B_upper = B.b                                  # certified upper endpoint
    return {
        "K": K, "sum_y_float": float(sum_y), "sum_abs_r_upper": float(sum_abs_r.b),
        "ten_sum_abs_r_upper": float((iv.mpf(10) * sum_abs_r).b),
        "max_abs_r_float": max_abs_r_f,
        "B_upper": B_upper, "B_upper_str": iv.nstr(B_upper, 25),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dual", help="npz with m, Y, denom_pow, K")
    ap.add_argument("--verify-ref", help="reference npz to reproduce (prints expected B_float)")
    ap.add_argument("--prec-bits", type=int, default=400)
    args = ap.parse_args()

    path = args.dual or args.verify_ref
    d = np.load(path, allow_pickle=True)
    m, Y, dp, K = d["m"], d["Y"], int(d["denom_pow"]), int(d["K"])
    TOL = str(d["TOL"]) if "TOL" in d else "1.0001"
    r = certify(m, Y, dp, K, TOL=TOL, prec_bits=args.prec_bits)
    print(f"K={r['K']}  sum_y={r['sum_y_float']:.16f}  10*sum|r|_upper={r['ten_sum_abs_r_upper']:.6e}")
    print(f"CERTIFIED:  S*({r['K']}) <= {r['B_upper_str']}")
    if args.verify_ref and "B_float" in d:
        exp = float(d["B_float"])
        ours = float(r["B_upper"])
        print(f"reference B_float = {exp:.16f}  |  ours = {ours:.16f}  |  Δ = {ours - exp:+.2e}")
        print("MATCH" if abs(ours - exp) < 1e-12 else "MISMATCH — investigate")


if __name__ == "__main__":
    main()
