"""Goal 0 recon: download top-5 P3 SOTA solutions, structurally characterise them.

For each leaderboard entry we record:
  - n (array length / resolution)
  - C2 recomputed at the array's own resolution (sanity vs reported score)
  - support fraction (nonzero entries / n)
  - number of active peaks of the autocorrelation f*f (local maxima above frac*max)
  - symmetry residual (||f - reverse(f)|| / ||f||) for the canonical reflection
  - basin signature: sorted support gaps, peak spacing

Writes raw arrays to mb/problems/3-autocorrelation/solutions/sota/ and a
JSON summary to stdout + sota_recon.json.
"""

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from einstein.autocorrelation.evaluator import verify_and_compute_c2  # noqa: E402
from scripts.check_submission import check_leaderboard  # noqa: E402

MB = Path("/Users/jongmin/projects/einstein/mb/problems/3-autocorrelation/solutions/sota")
MB.mkdir(parents=True, exist_ok=True)


def c2_score(f):
    """Canonical arena C2 (autoconvolution + Simpson L2). Use the real evaluator."""
    return verify_and_compute_c2(np.asarray(f, dtype=np.float64))


def peak_count(f, frac=0.05):
    """Active peaks of the autoCONVOLUTION f*f (arena's f★f), above frac*max."""
    f = np.asarray(f, dtype=np.float64)
    ac = np.convolve(f, f, mode="full")
    thr = frac * ac.max()
    # interior local maxima above threshold
    peaks = 0
    for i in range(1, len(ac) - 1):
        if ac[i] > thr and ac[i] >= ac[i - 1] and ac[i] > ac[i + 1]:
            peaks += 1
    return peaks


def symmetry_residual(f):
    f = np.asarray(f, dtype=np.float64)
    nz = np.nonzero(f)[0]
    if len(nz) == 0:
        return None
    lo, hi = nz[0], nz[-1]
    seg = f[lo : hi + 1]
    rev = seg[::-1]
    denom = np.linalg.norm(seg)
    return float(np.linalg.norm(seg - rev) / denom) if denom else None


def characterise(name, score, values):
    f = np.asarray(values, dtype=np.float64)
    n = len(f)
    nz = np.nonzero(np.abs(f) > 1e-12)[0]
    support = len(nz) / n if n else 0.0
    span = (int(nz[0]), int(nz[-1]), int(nz[-1] - nz[0] + 1)) if len(nz) else (0, 0, 0)
    return {
        "name": name,
        "reported_score": score,
        "n": n,
        "c2_recomputed_at_n": c2_score(f),
        "support_fraction": support,
        "support_span_lo_hi_width": span,
        "active_peaks_ac_5pct": peak_count(f, 0.05),
        "active_peaks_ac_1pct": peak_count(f, 0.01),
        "symmetry_residual": symmetry_residual(f),
        "min_val": float(f.min()),
        "max_val": float(f.max()),
        "n_negative": int(np.sum(f < -1e-12)),
    }


def main():
    lb = check_leaderboard(3, limit=8)
    print(f"Fetched {len(lb)} leaderboard entries for P3\n")
    summary = []
    for i, sol in enumerate(lb):
        name = sol["agentName"]
        score = sol["score"]
        vals = sol.get("data", {}).get("values")
        if vals is None:
            print(f"#{i+1} {name} {score:.13f} — no values payload, skipping")
            continue
        arr = np.asarray(vals, dtype=np.float64)
        np.save(MB / f"sota_{i+1:02d}_{name}_{score:.10f}.npy", arr)
        info = characterise(name, score, arr)
        info["rank"] = i + 1
        summary.append(info)
        print(
            f"#{i+1} {name:<18} score={score:.13f} n={info['n']:>6} "
            f"supp={info['support_fraction']:.3f} "
            f"peaks5%={info['active_peaks_ac_5pct']:>3} "
            f"sym={info['symmetry_residual']:.2e} "
            f"c2@n={info['c2_recomputed_at_n']:.10f}"
        )
    out = MB.parent / "sota_recon.json"
    out.write_text(json.dumps(summary, indent=2))
    print(f"\nWrote {out}")
    print(f"Arrays saved to {MB}")


if __name__ == "__main__":
    main()
