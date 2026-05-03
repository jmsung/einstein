"""Tammes (n=50) topology-mutation search.

Tests hypothesis H2 from wiki/questions/2026-05-02-p11-tammes-basin-escape.md —
"a topology-distinct optimum exists but lies in a deep basin not reached from
random starts or Hardin-Sloane perturbations."

Procedure: load the best known solution; for each trial pick K random vertices
and apply a tangent-space perturbation at scale sigma (much larger than the
1e-13 used by iterated_polish, which only smooths within the same basin); run
SLSQP active-pair polish; compute the contact-graph signature at tol=1e-6 and
compare to the reference.

A trial that lands at a strictly higher score with a different signature
disproves uniqueness (H1) and confirms H2. A trial that lands at any score
with a different signature catalogues an alternative topology (worth saving
for follow-up).

Outputs JSONL (one trial per line) + a summary table. Does NOT submit anything.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from einstein.tammes.evaluator import evaluate  # noqa: E402
from einstein.tammes.polish import (  # noqa: E402
    find_active_pairs,
    min_dist,
    normalize,
    slsqp_polish,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = REPO_ROOT / "results" / "problem-11-tammes"


def contact_signature(P: np.ndarray, sig_tol: float = 1e-6) -> tuple[str, list[tuple[int, int]]]:
    """Return (sha256_hash, sorted_pairs) for the contact graph at tol=sig_tol.

    sig_tol is intentionally tighter than the polish tol_active (1e-3) so the
    signature captures the basin's true topology rather than polish-slop pairs.
    """
    pairs, _ = find_active_pairs(P, tol=sig_tol)
    pairs_sorted = sorted(pairs)
    blob = ",".join(f"{i}-{j}" for i, j in pairs_sorted).encode()
    return hashlib.sha256(blob).hexdigest()[:16], pairs_sorted


def degree_sequence(pairs: list[tuple[int, int]], n: int = 50) -> tuple[int, ...]:
    """Return the sorted vertex-degree sequence — graph-isomorphism invariant."""
    deg = [0] * n
    for i, j in pairs:
        deg[i] += 1
        deg[j] += 1
    return tuple(sorted(deg))


def perturb(P: np.ndarray, k: int, sigma: float, rng: np.random.Generator) -> np.ndarray:
    """Tangent-space perturbation of K random vertices at magnitude sigma.

    Each chosen vertex gets a tangent vector of magnitude sigma in a random
    direction (uniform on the tangent circle), then we re-normalize. The other
    50 - K vertices are unchanged. Larger K and sigma test the basin further.
    """
    n = P.shape[0]
    Q = P.copy()
    idx = rng.choice(n, size=k, replace=False)
    for i in idx:
        g = rng.standard_normal(3)
        g = g - (g @ Q[i]) * Q[i]
        g_norm = float(np.linalg.norm(g))
        if g_norm < 1e-15:
            continue
        Q[i] = Q[i] + (sigma / g_norm) * g
    return normalize(Q)


def run_trial(
    P_seed: np.ndarray,
    k: int,
    sigma: float,
    polish_iters: int,
    rng: np.random.Generator,
) -> tuple[float, str, list[tuple[int, int]], tuple[int, ...]]:
    """Perturb, polish iteratively, return (score, sig_hash, pairs, deg_seq).

    Polish schedule recovers the contact graph after a moderate displacement:
    a wide-tol bootstrap pass (tol_active=5e-2) constrains all near-active
    pairs so SLSQP can navigate back toward a coherent basin, then narrowing
    iterations at tol=1e-3 refine the active set.
    """
    P = perturb(P_seed, k=k, sigma=sigma, rng=rng)
    # Bootstrap with wide tol — captures near-contact pairs lost to displacement
    for tol in (5e-2, 1e-2):
        P, _ = slsqp_polish(P, max_pairs=400, tol_active=tol, verbose=False)
    # Refining iterations at the recipe tol with tiny tangent jitter
    for _ in range(polish_iters):
        P, _ = slsqp_polish(P, max_pairs=300, tol_active=1e-3, verbose=False)
        g = rng.standard_normal(P.shape) * 1e-13
        g = g - (g * P).sum(axis=1, keepdims=True) * P
        P = normalize(P + g)
    P, _ = slsqp_polish(P, max_pairs=300, tol_active=1e-3, verbose=False)
    score = float(min_dist(P))
    sig, pairs = contact_signature(P)
    return score, sig, pairs, degree_sequence(pairs)


def main():
    parser = argparse.ArgumentParser(description="Tammes (n=50) topology-mutation search")
    parser.add_argument("--source", type=str, required=True,
                        help="Path to seed JSON (e.g. solution-best.json)")
    parser.add_argument("--n-trials", type=int, default=200)
    parser.add_argument("--ks", type=int, nargs="+", default=[1, 3, 5, 10],
                        help="Vertex-perturbation counts to sweep")
    parser.add_argument("--sigmas", type=float, nargs="+",
                        default=[1e-2, 5e-2, 1e-1, 2e-1],
                        help="Perturbation magnitudes to sweep")
    parser.add_argument("--polish-iters", type=int, default=5,
                        help="Inner polish iterations per trial (with 1e-13 jitter)")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--out", type=str, default=None)
    args = parser.parse_args()

    src = Path(args.source).expanduser().resolve()
    with open(src) as f:
        seed_data = json.load(f)
    P_seed = normalize(np.array(seed_data["vectors"], dtype=np.float64))
    seed_score = evaluate({"vectors": P_seed.tolist()})
    ref_sig, ref_pairs = contact_signature(P_seed)
    ref_deg = degree_sequence(ref_pairs)

    print(f"Source: {src}")
    print(f"Seed score: {seed_score:.16f}")
    print(f"Seed contact graph: {len(ref_pairs)} pairs at tol=1e-6, "
          f"sig={ref_sig}, deg_hist={dict(Counter(ref_deg))}")
    print()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else (
        RESULTS_DIR / f"topology-mutation-trials-{args.seed}.jsonl"
    )

    rng = np.random.default_rng(args.seed)
    best_score_by_sig: dict[str, float] = {}
    sig_count: Counter[str] = Counter()
    deg_count: Counter[tuple[int, ...]] = Counter()
    novel_better: list[dict] = []

    t0 = time.time()
    n_done = 0
    with open(out_path, "w") as f_out:
        for k in args.ks:
            for sigma in args.sigmas:
                trials_per_combo = max(1, args.n_trials // (len(args.ks) * len(args.sigmas)))
                for t in range(trials_per_combo):
                    n_done += 1
                    score, sig, pairs, deg = run_trial(
                        P_seed, k=k, sigma=sigma,
                        polish_iters=args.polish_iters, rng=rng,
                    )
                    rec = {
                        "trial": n_done,
                        "k": k,
                        "sigma": sigma,
                        "score": score,
                        "sig": sig,
                        "n_active": len(pairs),
                        "deg_seq": list(deg),
                        "novel_topology": sig != ref_sig,
                        "novel_isomorphism_class": deg != ref_deg,
                    }
                    f_out.write(json.dumps(rec) + "\n")
                    f_out.flush()
                    sig_count[sig] += 1
                    deg_count[deg] += 1
                    if sig not in best_score_by_sig or score > best_score_by_sig[sig]:
                        best_score_by_sig[sig] = score
                    if sig != ref_sig and score > seed_score - 1e-15:
                        novel_better.append(rec)
                    print(
                        f"[{n_done:4d}] k={k:2d} sigma={sigma:.2e} "
                        f"score={score:.16f} "
                        f"{'NEW-TOPO' if sig != ref_sig else 'same-topo':10s} "
                        f"{'NEW-ISO' if deg != ref_deg else 'same-iso':9s} "
                        f"npairs={len(pairs):3d}"
                    )

    elapsed = time.time() - t0
    print()
    print(f"=== Summary ({n_done} trials in {elapsed:.0f}s) ===")
    print(f"Reference sig: {ref_sig}  ({sig_count[ref_sig]} hits)")
    print(f"Distinct contact-graph signatures observed: {len(sig_count)}")
    print(f"Distinct degree-sequence classes observed: {len(deg_count)}")
    print(f"Novel-topology trials: {sum(1 for s in sig_count if s != ref_sig)}")
    print(f"Novel-isomorphism-class trials: "
          f"{sum(c for d, c in deg_count.items() if d != ref_deg)}")
    print()
    print("Top-10 distinct sigs by best score:")
    for sig, best in sorted(best_score_by_sig.items(), key=lambda x: -x[1])[:10]:
        delta_vs_seed = best - seed_score
        marker = "  (REF)" if sig == ref_sig else ""
        print(f"  {sig}  best={best:.16f}  Δ_seed={delta_vs_seed:+.3e}  "
              f"hits={sig_count[sig]}{marker}")
    print()
    print(f"Wrote per-trial log: {out_path}")
    if novel_better:
        print(f"\n!! {len(novel_better)} novel-topology trials at or above seed score !!")
        for r in novel_better[:5]:
            print(f"   trial {r['trial']}: score={r['score']:.16f} sig={r['sig']}")


if __name__ == "__main__":
    main()
