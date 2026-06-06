"""Goal 1 signed-parameterisation search for P4 (third autocorrelation).

Targets the lever isolated in Goal 0
(findings/p4-fragmentation-not-fraction-shared-envelope): high-frequency sign
fragmentation on a shared low-frequency envelope. Three init modes:

  fourier-cold   both-sign random Fourier ansatz (the literal Goal 1 brief);
                 NOT warm-started from our 23.6% basin.
  leader-frag    leader's low-pass envelope + fresh high-frequency signed
                 perturbation (the higher-EV Goal 0 path).
  ours-frag      our envelope + fresh signed perturbation (control / ablation).

A negative-content schedule (``--neg-target``) nudges the negative fraction up
toward the target during the early β stages, then anneals to 0 so the final
stages optimise the true arena objective. Multistart over ``--restarts`` seeds.

Usage:
    uv run python scripts/third_autocorrelation/optimize_signed.py \\
        --n 6400 --init leader-frag --neg-target 0.30 \\
        --beta 1e4,3e4,1e5,3e5,1e6,3e6,1e7,3e7 --iters 800 \\
        --restarts 8 --out results/problem-4-third-autocorrelation/signed_v1.json
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    both_sign_fourier_init,
    load_warmstart,
    lowpass_envelope,
    signed_descent,
    upsample,
)

MB = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER = MB / "sol-organon-rank1-p4-1.4523043332.json"
OURS = MB / "solution-feat-third-autocorrelation-1.4525211550469.json"


def make_init(
    mode: str, n: int, neg_bias: float, env_keep: int, detail_scale: float, rng
) -> np.ndarray:
    """Build a fresh signed initial condition per the chosen mode.

    ``detail_scale`` (frag modes only) sizes the high-frequency perturbation as a
    fraction of the envelope's typical magnitude. Small (≈0.03) keeps the start
    near the reference basin so the cascade can descend; large destroys the
    envelope. ``neg_bias`` controls only the cold Fourier ansatz.
    """
    if mode == "fourier-cold":
        return both_sign_fourier_init(n, n_modes=max(20, n // 200), neg_bias=neg_bias, rng=rng)
    ref = LEADER if mode == "leader-frag" else OURS
    v = load_warmstart(ref)
    if len(v) != n:
        v = upsample(v, n)
    env = lowpass_envelope(v, keep=env_keep)
    # Fresh small high-frequency signed perturbation on the shared envelope.
    detail = rng.normal(scale=detail_scale * np.abs(env).mean(), size=n)
    return env + detail


def optimize(args):
    betas = [float(b) for b in args.beta.split(",")]
    best_c = float("inf")
    best_v = None
    for r in range(args.restarts):
        rng = np.random.default_rng(args.seed + r)
        init_v = make_init(args.init, args.n, args.neg_bias, args.env_keep, args.detail_scale, rng)
        t0 = time.time()
        v, c = signed_descent(init_v, betas, args.iters, args.lr, args.neg_target, args.neg_weight)
        frac = float((v < 0).mean())
        print(
            f"  restart {r:2d}: C={c:.13f}  neg={frac * 100:5.2f}%  ({time.time() - t0:.1f}s)",
            flush=True,
        )
        if c < best_c:
            best_c, best_v = c, v
    return best_v, best_c


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--n", type=int, required=True)
    p.add_argument(
        "--init", choices=["fourier-cold", "leader-frag", "ours-frag"], default="leader-frag"
    )
    p.add_argument("--beta", type=str, required=True, help="Comma-separated β cascade")
    p.add_argument("--iters", type=int, default=800)
    p.add_argument("--lr", type=float, default=0.8)
    p.add_argument("--restarts", type=int, default=8)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--neg-target", type=float, default=0.30, help="Target negative fraction")
    p.add_argument("--neg-weight", type=float, default=2.0, help="Nudge weight (anneals to 0)")
    p.add_argument("--neg-bias", type=float, default=0.4, help="Cold-Fourier negative bias")
    p.add_argument("--env-keep", type=int, default=2048, help="rFFT modes kept for the envelope")
    p.add_argument(
        "--detail-scale", type=float, default=0.03, help="Frag perturbation size (frac of envelope)"
    )
    p.add_argument("--out", type=Path, default=None)
    args = p.parse_args()

    print(
        f"Signed search: n={args.n} init={args.init} neg_target={args.neg_target} "
        f"restarts={args.restarts}"
    )
    best_v, best_c = optimize(args)
    leader = 1.4523043331832
    verdict = "BEATS" if best_c < leader - 1e-8 else "does NOT beat"
    print(f"\nBest C = {best_c:.13f}  (n={args.n}, init={args.init})")
    print(f"Leader  = {leader:.13f}  → {verdict} leader")

    if args.out and best_v is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w") as fh:
            json.dump(
                {
                    "values": best_v.tolist(),
                    "score": best_c,
                    "n": args.n,
                    "init": args.init,
                    "neg_frac": float((best_v < 0).mean()),
                },
                fh,
            )
        print(f"Saved: {args.out}")


if __name__ == "__main__":
    main()
