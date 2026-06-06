"""Measure how P3 C2 scales with resolution, using the EXACT arena verifier.

The arena verifier (from the problem page) uses scipy.signal.oaconvolve. We
reproduce it bit-for-bit, then:
  1. Recompute the leader (ClaudeExplorer 400k) score to confirm we match the board.
  2. Upsample the leader basin to 800k / 1.6M / 2M (linear + band-limited) and
     rescore — does C2 rise with resolution?
  3. Score our existing 1.6M solutions with the exact verifier.

Pure measurement; no submission. Prints a table.
"""

import sys
from pathlib import Path

import numpy as np
from scipy.signal import oaconvolve

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
SOTA = Path("/Users/jongmin/projects/einstein/mb/problems/3-autocorrelation/solutions/sota")
SOL = Path("/Users/jongmin/projects/einstein/mb/problems/3-autocorrelation/solutions")


def arena_c2(values):
    """Bit-for-bit reproduction of the arena verifier (oaconvolve + Simpson)."""
    f = np.array(values, dtype=np.float64)
    if np.any(f < -1e-6):
        raise ValueError("negative")
    f = np.maximum(f, 0.0)
    conv = oaconvolve(f, f, mode="full")
    m = len(conv)
    xp = np.linspace(-0.5, 0.5, m + 2)
    dx = np.diff(xp)
    yp = np.concatenate(([0.0], conv, [0.0]))
    y1, y2 = yp[:-1], yp[1:]
    l2 = float(np.sum((dx / 3) * (y1**2 + y1 * y2 + y2**2)))
    l1 = float(np.sum(np.abs(conv)) / (m + 1))
    linf = float(np.max(np.abs(conv)))
    return l2 / (l1 * linf)


def upsample_linear(f, new_n):
    x_old = np.linspace(0, 1, len(f))
    x_new = np.linspace(0, 1, new_n)
    return np.maximum(np.interp(x_new, x_old, f), 0.0)


def upsample_fourier(f, new_n):
    """Band-limited (FFT) resample — preserves spectral content, no aliasing."""
    from scipy.signal import resample

    g = resample(f, new_n)
    return np.maximum(g, 0.0)


def main():
    leader_files = sorted(SOTA.glob("sota_01_*.npy"))
    if not leader_files:
        print("No leader array saved; run recon_p3_sota.py first.")
        return
    leader = np.load(leader_files[0])
    print(f"Leader (ClaudeExplorer) n={len(leader)}  board=0.9626433188")
    base = arena_c2(leader)
    print(f"  arena_c2 recomputed @ {len(leader)}: {base:.12f}\n")

    record = 0.9626433187626762
    gate = record + 0.0001
    print(f"  RECORD = {record:.12f}   GATE (record+1e-4) = {gate:.12f}\n")

    print("=== Resolution scaling of the leader basin ===")
    for new_n in [400000, 800000, 1200000, 1600000, 2000000]:
        for kind, fn in [("linear", upsample_linear), ("fourier", upsample_fourier)]:
            if new_n == len(leader) and kind == "linear":
                g = leader
            else:
                g = fn(leader, new_n)
            try:
                c = arena_c2(g)
                flag = ""
                if c > gate:
                    flag = "  *** CLEARS GATE ***"
                elif c > record:
                    flag = "  (> record, < gate)"
                print(f"  n={new_n:>8} {kind:<8} C2={c:.12f}{flag}")
            except Exception as e:
                print(f"  n={new_n:>8} {kind:<8} ERROR {e}")
        print()

    print("=== Our existing high-res solutions (exact verifier) ===")
    for npy in sorted(SOL.glob("*.npy")):
        arr = np.load(npy)
        try:
            c = arena_c2(arr)
            flag = "  *** CLEARS GATE ***" if c > gate else ("  (> record)" if c > record else "")
            print(f"  {npy.name:<48} n={len(arr):>8} C2={c:.12f}{flag}")
        except Exception as e:
            print(f"  {npy.name}: ERROR {e}")


if __name__ == "__main__":
    main()
