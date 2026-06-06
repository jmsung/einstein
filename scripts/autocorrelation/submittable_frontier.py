"""P3 submittable-frontier campaign — beat 0.96264 within the 4.5MB payload cap.

The arena POST limit is ~4.5MB (Vercel FUNCTION_PAYLOAD_TOO_LARGE). The leaders
sit at n=400000, 74% zeros, 2.7MB, C2=0.9626433. Their resolution is capped by
payload, not by the problem's stated 2M limit. The unexploited lever: a SPARSE
solution can carry more points (higher resolution -> higher C2) under the same
byte budget. We optimize natively at submittable n (400k-700k), keep the support
sparse, and finalize to a compact-rounded array whose exact JSON is < 4.5MB.

Auto-submits any candidate that (a) fits under the payload cap AND (b) is
verified (triple-verify) to beat the live arena #1. The board ranks by raw
score, so > arena #1 takes #1. Throttle/daily-cap/audit gates still apply.

Run:
    EINSTEIN_AUTO_SUBMIT=1 nohup uv run python scripts/autocorrelation/submittable_frontier.py \
        --budget 36000 --log mb/problems/3-autocorrelation/frontier.log &
"""

import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "src"))

from einstein.autocorrelation.fast import fast_evaluate  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "dinkelbach_cpu_v2", REPO / "scripts/autocorrelation/dinkelbach_cpu_v2.py"
)
dink = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dink)
lbfgs_refine = dink.lbfgs_refine

SOL = Path("/Users/jongmin/projects/einstein/mb/problems/3-autocorrelation/solutions")
SOTA = SOL / "sota"
RECORD = 0.9626433187626762
GATE = RECORD + 0.0001
PAYLOAD_CAP = 4.4e6  # bytes; stay safely under the ~4.5MB server limit

T0 = time.time()
LOG_FH = None
GLOBAL_BEST = 0.0


def log(m):
    line = f"[{time.time()-T0:8.1f}s] {m}"
    print(line, flush=True)
    if LOG_FH:
        LOG_FH.write(line + "\n")
        LOG_FH.flush()


def payload_bytes(values):
    return len(json.dumps({"problem_id": 3, "solution": {"values": values}}).encode())


def finalize(f, sig=8, thr_frac=0.0):
    """Round to `sig` sig-figs and zero values below thr_frac*max; return
    (rounded_list, exact_score, bytes). The submitted array is EXACTLY this."""
    g = np.maximum(f, 0.0).copy()
    if thr_frac > 0:
        g[g < thr_frac * g.max()] = 0.0
    vals = [float(f"%.{sig}g" % x) if x > 0 else 0.0 for x in g]
    a = np.asarray(vals, dtype=np.float64)
    return vals, fast_evaluate(a), payload_bytes(vals)


def best_finalize(f):
    """Find the most accurate finalization that still fits the payload cap."""
    best = None
    # prefer more sig-figs / less thresholding; back off only to fit
    for sig in (10, 9, 8, 7, 6):
        for thr in (0.0, 1e-6, 1e-5, 5e-5, 1e-4):
            vals, sc, nb = finalize(f, sig=sig, thr_frac=thr)
            if nb < PAYLOAD_CAP:
                if best is None or sc > best[1]:
                    best = (vals, sc, nb, sig, thr)
        if best is not None:
            break
    return best  # (vals, score, bytes, sig, thr) or None


def upsample_linear(f, new_n):
    x_old = np.linspace(0, 1, len(f))
    x_new = np.linspace(0, 1, new_n)
    return np.maximum(np.interp(x_new, x_old, f), 0.0)


def triple_verify(values):
    import einstein.triple_verify.problems.p03_autocorrelation  # noqa: F401
    from einstein.triple_verify.core import get_verifier, verify

    return verify({"values": np.asarray(values, dtype=np.float64)}, get_verifier(3))


def checkpoint(vals, score, nb, tag):
    """Record a strictly-improved global best. Returns True iff it improved."""
    global GLOBAL_BEST
    if score <= GLOBAL_BEST:
        return False
    GLOBAL_BEST = score
    out = SOL / f"frontier_{tag}_n{len(vals)}_{score:.12f}.json"
    out.write_text(json.dumps({"values": vals, "score": score, "n": len(vals), "tag": tag}))
    log(
        f"  NEW BEST {score:.12f} vsRECORD {score-RECORD:+.3e} vsGATE {score-GATE:+.3e} "
        f"payload={nb/1e6:.2f}MB ({tag}, n={len(vals)})"
    )
    return True


# Require a real margin over #1 before even attempting a submit. Reproducing the
# leader scores RECORD + float-noise (~3e-13); without this guard every restart
# fires a doomed triple-verify + audit-log row. 1e-7 is well below the arena's
# 1e-4 acceptance band but safely above evaluator nondeterminism.
SUBMIT_MARGIN = 1e-7


def maybe_submit(vals, score, nb, tag):
    """Submit a payload-fitting candidate that beats live #1, after triple-verify."""
    if score <= RECORD + SUBMIT_MARGIN:
        return
    if nb >= PAYLOAD_CAP:
        log(f"  beats record but payload {nb/1e6:.2f}MB >= cap — not submittable")
        return
    log(f"  candidate beats #1 ({score:.12f}) and fits ({nb/1e6:.2f}MB) — triple-verify")
    res = triple_verify(vals)
    log(f"  triple-verify passed={res.passed} fast={res.fast} exact={res.exact} cross={res.cross}")
    if not res.passed:
        log("  triple-verify FAILED — not submitting")
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


def optimize_at(seed_f, n, label, budget, rng):
    f = upsample_linear(seed_f, n) if len(seed_f) != n else seed_f.copy()
    log(f"[{label}] n={n} seed raw C2={fast_evaluate(f):.10f}")
    bf = best_finalize(f)
    if bf and checkpoint(bf[0], bf[1], bf[2], label + "_seed"):
        maybe_submit(bf[0], bf[1], bf[2], label + "_seed")
    t_end = time.time() + budget
    beta_sched = [1e5, 3e5, 1e6, 3e6, 1e7]
    restart = 0
    cur = f
    while time.time() < t_end:
        slice_budget = min(900.0, t_end - time.time())
        if slice_budget < 30:
            break
        # restart 0 = unperturbed (reproduce/refine); later restarts escalate the
        # perturbation to escape the leader basin toward a possibly-higher one.
        w0 = np.sqrt(cur if restart == 0 else _perturb(cur, rng, 0.05 * (1 + restart % 6)))
        bw, _ = lbfgs_refine(
            w0, n, beta_sched, outer_per_beta=4, maxiter=150, time_limit=slice_budget
        )
        fb = bw * bw
        raw = fast_evaluate(fb)
        bf = best_finalize(fb)
        if bf:
            log(
                f"[{label}] restart {restart}: raw={raw:.10f} finalized={bf[1]:.10f} "
                f"({bf[2]/1e6:.2f}MB sig={bf[3]} thr={bf[4]:.0e}) best={GLOBAL_BEST:.10f}"
            )
            if bf[1] > fast_evaluate(cur):
                cur = fb
            if checkpoint(bf[0], bf[1], bf[2], label):
                maybe_submit(bf[0], bf[1], bf[2], label)
        restart += 1


def _perturb(f, rng, scale):
    g = f.copy()
    nz = np.where(g > 1e-12)[0]
    if len(nz) == 0:
        return g
    k = max(1, len(nz) // 20)
    idx = rng.choice(nz, size=k, replace=False)
    g[idx] *= 1.0 + scale * rng.standard_normal(k)
    return np.maximum(g, 0.0)


def main():
    global LOG_FH
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, default=36000.0)
    ap.add_argument("--log", type=str, default=str(SOL.parent / "frontier.log"))
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument(
        "--only-n", type=int, default=0, help="run a single resolution n (parallel mode)"
    )
    args = ap.parse_args()
    LOG_FH = open(args.log, "a")
    rng = np.random.default_rng(args.seed)

    lf = sorted(SOTA.glob("sota_01_*.npy"))
    if not lf:
        log("no leader array — run recon_p3_sota.py first")
        return
    leader = np.load(lf[0]).astype(np.float64)
    log("=== P3 submittable-frontier campaign ===")
    log(f"leader n={len(leader)} C2={fast_evaluate(leader):.10f} (the bar to beat)")
    log(f"RECORD={RECORD:.12f} GATE={GATE:.12f} payload_cap={PAYLOAD_CAP/1e6:.2f}MB")

    # CORRECTED 2026-06-05: raw upsample craters (400k->600k ~0.90), BUT Dinkelbach
    # RECOVERS the crater and then climbs ABOVE the source — proven: our 0.96272
    # came from upsampling the leader 400k -> 1.6M + Dinkelbach (gained +7.6e-5 over
    # 0.96264). The earlier "zero transfer" read was from raw upsample alone; with a
    # long Dinkelbach polish the basin tracks upward with resolution. So the live
    # lever is cross-resolution transfer to the PAYLOAD FRONTIER: upsample leader to
    # the largest submittable n (4.5MB cap fits ~700-800k at leader sparsity) then a
    # long Dinkelbach polish. Expected ~0.96267-0.96270 (between 400k and 1.6M),
    # above the record AND under the cap. Three submittable high-res prongs.
    prongs = [
        (leader, 450_000, "x450k", 11),
        (leader, 500_000, "x500k", 23),
        (leader, 550_000, "x550k", 47),
        (leader, 600_000, "x600k", 71),
        (leader, 650_000, "x650k", 97),
        (leader, 700_000, "x700k", 131),
    ]
    if args.only_n:
        # parallel mode: this process owns one resolution for the whole budget
        optimize_at(
            leader,
            args.only_n,
            f"x{args.only_n//1000}k",
            args.budget,
            np.random.default_rng(args.seed),
        )
    else:
        per = args.budget / len(prongs)
        for seed_f, npts, label, sd in prongs:
            if time.time() - T0 > args.budget:
                break
            optimize_at(seed_f, npts, label, per, np.random.default_rng(sd))

    log(
        f"=== done. global best C2={GLOBAL_BEST:.12f} "
        f"(vsRECORD {GLOBAL_BEST-RECORD:+.3e}, vsGATE {GLOBAL_BEST-GATE:+.3e}) ==="
    )


if __name__ == "__main__":
    main()
