"""Parallel 400k new-basin hunt for P3 — use the whole M5 Max.

Measured facts (see findings/p3-resolution-is-the-lever-2026-06.md):
- Arena scores at submitted length; POST cap ~4.5MB; n=400000 fits at leader
  sparsity. ZERO cross-resolution transfer, so 400k is the playing field.
- The top agents (ClaudeExplorer, CHRONOS) sit in ONE basin (shape corr 0.999).
  Beating 0.9626433 requires a structurally DIFFERENT, higher 400k basin.

Strategy: many workers (one per core) run L-BFGS Dinkelbach from a diverse seed
pool — the saturated basin + large-perturbation escapes + structured-from-scratch
constructions + random — looping in rounds that intensify around the best while
keeping a fresh-diverse fraction. Auto-submits any verified candidate that beats
live #1 by a real margin AND fits the payload cap.

Run:
    EINSTEIN_AUTO_SUBMIT=1 nohup uv run python scripts/autocorrelation/parallel_400k.py \
        --budget 36000 --workers 16 --log mb/problems/3-autocorrelation/parallel400k.log &
"""

import argparse
import importlib.util
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "src"))

from einstein.autocorrelation.fast import fast_evaluate, score_from_conv  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "dinkelbach_cpu_v2", REPO / "scripts/autocorrelation/dinkelbach_cpu_v2.py"
)
dink = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dink)
lbfgs_refine = dink.lbfgs_refine

SOL = Path("/Users/jongmin/projects/einstein/mb/problems/3-autocorrelation/solutions")
SOTA = SOL / "sota"
N = 400_000
RECORD = 0.9626433187626762
GATE = RECORD + 0.0001
PAYLOAD_CAP = 4.4e6
SUBMIT_MARGIN = 1e-7

T0 = time.time()
LOG_FH = None
GLOBAL_BEST = 0.0


def log(m):
    line = f"[{time.time()-T0:8.1f}s] {m}"
    print(line, flush=True)
    if LOG_FH:
        LOG_FH.write(line + "\n")
        LOG_FH.flush()


# ---- payload-aware finalize (the array we'd actually submit) ----------------
def payload_bytes(values):
    return len(json.dumps({"problem_id": 3, "solution": {"values": values}}).encode())


def best_finalize(f):
    for sig in (10, 9, 8, 7, 6):
        best = None
        for thr in (0.0, 1e-6, 1e-5, 5e-5, 1e-4):
            g = np.maximum(f, 0.0).copy()
            if thr > 0:
                g[g < thr * g.max()] = 0.0
            vals = [float(f"%.{sig}g" % x) if x > 0 else 0.0 for x in g]
            nb = payload_bytes(vals)
            if nb < PAYLOAD_CAP:
                sc = fast_evaluate(np.asarray(vals))
                if best is None or sc > best[1]:
                    best = (vals, sc, nb, sig, thr)
        if best is not None:
            return best
    return None


# ---- seed constructions -----------------------------------------------------
def _structured(kind, rng):
    """From-scratch 400k seeds with ~25% centered support (diverse basins)."""
    f = np.zeros(N)
    w = int(0.26 * N)
    lo = (N - w) // 2
    x = np.linspace(0, 1, w)
    if kind == "tri":
        bump = 1.0 - np.abs(2 * x - 1)
    elif kind == "parab":
        bump = 1.0 - (2 * x - 1) ** 2
    elif kind == "rcos":
        bump = 0.5 * (1 - np.cos(2 * np.pi * x))
    elif kind == "twobump":
        bump = np.exp(-((x - 0.3) ** 2) / 0.01) + np.exp(-((x - 0.7) ** 2) / 0.01)
    elif kind == "flat":
        bump = np.ones(w)
    else:  # random smooth
        bump = np.abs(rng.standard_normal(w))
        bump = np.convolve(bump, np.ones(101) / 101, mode="same")
    f[lo : lo + w] = np.maximum(bump, 0.0)
    return f


def _perturb(f, rng, scale):
    g = f.copy()
    nz = np.where(g > 1e-12)[0]
    if len(nz) == 0:
        return g
    k = max(1, int(len(nz) * min(0.5, 0.05 + scale)))
    idx = rng.choice(nz, size=k, replace=False)
    g[idx] *= 1.0 + scale * rng.standard_normal(k)
    return np.maximum(g, 0.0)


def make_seeds(best_f, leader, chronos, rng, n_seeds):
    """Half intensify around best, half diverse-explore."""
    seeds = []
    base = best_f if best_f is not None else leader
    # intensify
    for s in (0.05, 0.1, 0.2, 0.4):
        seeds.append(("intensify", _perturb(base, rng, s)))
    # escape from the saturated basin
    for s in (0.8, 1.5, 3.0):
        seeds.append(("escape", _perturb(leader, rng, s)))
    seeds.append(("chronos", _perturb(chronos, rng, 0.1)))
    # from-scratch structured
    for kind in ("tri", "parab", "rcos", "twobump", "flat", "rand"):
        seeds.append((f"struct_{kind}", _structured(kind, rng)))
    # pad with random structured if more workers
    while len(seeds) < n_seeds:
        seeds.append((f"rand{len(seeds)}", _structured("rand", rng)))
    return seeds[:n_seeds]


# ---- worker (top-level, picklable) -----------------------------------------
def _worker(args):
    tag, seed_f, slice_time, wseed = args
    rng = np.random.default_rng(wseed)
    w0 = np.sqrt(np.maximum(seed_f, 1e-12))
    beta_sched = [1e5, 3e5, 1e6, 3e6, 1e7]
    best_w, _ = lbfgs_refine(
        w0, N, beta_sched, outer_per_beta=4, maxiter=200, time_limit=slice_time
    )
    f = best_w * best_w
    # one basin-hop inside the worker
    fb = _perturb(f, rng, 0.1)
    w1 = np.sqrt(np.maximum(fb, 1e-12))
    bw2, _ = lbfgs_refine(
        w1, N, beta_sched[-3:], outer_per_beta=3, maxiter=150, time_limit=slice_time / 2
    )
    f2 = bw2 * bw2
    conv = fftconvolve(f, f, mode="full")
    conv2 = fftconvolve(f2, f2, mode="full")
    s1, s2 = score_from_conv(conv), score_from_conv(conv2)
    out = f if s1 >= s2 else f2
    return tag, float(max(s1, s2)), out.astype(np.float64)


def triple_verify(values):
    import einstein.triple_verify.problems.p03_autocorrelation  # noqa: F401
    from einstein.triple_verify.core import get_verifier, verify

    return verify({"values": np.asarray(values, dtype=np.float64)}, get_verifier(3))


def checkpoint_and_submit(f):
    """Finalize, checkpoint if new best, submit if it beats #1 by a real margin."""
    global GLOBAL_BEST
    bf = best_finalize(f)
    if bf is None:
        return
    vals, sc, nb, sig, thr = bf
    if sc <= GLOBAL_BEST:
        return
    GLOBAL_BEST = sc
    (SOL / f"par400k_n{N}_{sc:.12f}.json").write_text(
        json.dumps({"values": vals, "score": sc, "n": N})
    )
    log(
        f"  NEW BEST {sc:.12f} vsRECORD {sc-RECORD:+.3e} vsGATE {sc-GATE:+.3e} "
        f"payload={nb/1e6:.2f}MB sig={sig} thr={thr:.0e}"
    )
    if sc <= RECORD + SUBMIT_MARGIN or nb >= PAYLOAD_CAP:
        return
    log("  beats #1 by real margin — triple-verify then submit")
    res = triple_verify(vals)
    log(f"  triple-verify passed={res.passed} fast={res.fast} exact={res.exact} cross={res.cross}")
    if not res.passed:
        return
    from einstein.auto_submit import try_submit

    out = try_submit(
        3,
        {"values": vals},
        res.exact,
        triple_verify={"passed": True, "fast": res.fast, "exact": res.exact, "cross": res.cross},
        min_improvement=1e-8,
        minimize=False,
    )
    log(f"  SUBMIT: submitted={out.submitted} gate={out.rejected_at_gate} reason={out.reason}")


def main():
    global LOG_FH
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=36000.0)
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--slice", type=float, default=240.0, help="seconds per worker task")
    ap.add_argument("--log", type=str, default=str(SOL.parent / "parallel400k.log"))
    args = ap.parse_args()
    LOG_FH = open(args.log, "a")
    rng = np.random.default_rng(2026)

    leader = np.load(sorted(SOTA.glob("sota_01_*.npy"))[0]).astype(np.float64)
    chronos = np.load(sorted(SOTA.glob("sota_02_*.npy"))[0]).astype(np.float64)
    log("=== P3 parallel 400k new-basin hunt ===")
    log(f"workers={args.workers} slice={args.slice}s budget={args.budget}s")
    log(f"leader C2={fast_evaluate(leader):.10f}  RECORD={RECORD:.12f} GATE={GATE:.12f}")
    checkpoint_and_submit(leader)  # establishes GLOBAL_BEST=0.96264 (no submit: margin)

    best_f = leader.copy()
    rnd = 0
    while time.time() - T0 < args.budget:
        seeds = make_seeds(
            best_f if GLOBAL_BEST > RECORD + SUBMIT_MARGIN else None,
            leader,
            chronos,
            rng,
            args.workers,
        )
        tasks = [(tag, sf, args.slice, int(rng.integers(1, 2**31))) for tag, sf in seeds]
        log(f"round {rnd}: dispatching {len(tasks)} workers (best={GLOBAL_BEST:.10f})")
        round_best = (GLOBAL_BEST, None)
        with ProcessPoolExecutor(max_workers=args.workers) as ex:
            futs = [ex.submit(_worker, t) for t in tasks]
            for fut in as_completed(futs):
                try:
                    tag, sc, f = fut.result()
                except Exception as e:
                    log(f"  worker error: {e}")
                    continue
                if sc > round_best[0]:
                    round_best = (sc, f)
                if sc > RECORD - 1e-3:  # only log near-misses to keep noise down
                    log(f"  [{tag}] {sc:.10f}")
                checkpoint_and_submit(f)
        if round_best[1] is not None and round_best[0] > fast_evaluate(best_f):
            best_f = round_best[1]
            log(f"round {rnd} improved working-best -> {round_best[0]:.10f}")
        rnd += 1

    log(
        f"=== done. global best C2={GLOBAL_BEST:.12f} "
        f"(vsRECORD {GLOBAL_BEST-RECORD:+.3e}, vsGATE {GLOBAL_BEST-GATE:+.3e}) ==="
    )


if __name__ == "__main__":
    os.environ.setdefault("OMP_NUM_THREADS", "1")  # one BLAS thread per worker
    main()
