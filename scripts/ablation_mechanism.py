"""Pure-code mechanism ablation harness (no LLM) — for JSAgent claims #2 (adaptive
scheduling) and #3 (problem-specific plugins) in the mechanism-claims test matrix.

Deterministic, paired-by-seed, high-N → tight CIs in seconds. An "arm" is any callable
`arm(seed) -> ArmResult` (a baseline vs a treatment); both arms get the SAME cold-init
per seed (pairing), so the per-seed difference cancels shared start-point noise — the
same design as the LLM compounding ablation, but free to run thousands of seeds.

What this file owns (verified, unit-testable): the runner + stats (paired Δ, bootstrap
CI, win-rate, mean wall-clock) + JSONL recording. The ARM FACTORIES at the bottom wire
the real optimizer/plugins; they are EXAMPLES — verify signatures against your evaluator
and, critically, pick a family that passes the HEADROOM SCREEN (the baseline must
sometimes fail; a saturated family like circle packing gives a null for the wrong reason).

Usage (once an arm pair is finalized):
    uv run python scripts/ablation_mechanism.py --claim plugins --family <f> --seeds 200
Results -> results/ablation-mechanism/<claim>.jsonl + a printed summary.
"""

from __future__ import annotations

import argparse
import json
import time
from collections.abc import Callable
from dataclasses import asdict, dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- arm contract


@dataclass
class ArmResult:
    """One arm's outcome on one seed."""

    seed: int
    score: float  # final objective (higher = better; flip upstream if minimizing)
    wall_s: float  # wall-clock to produce it
    reached_target: bool = False  # did it hit the time-to-target threshold (optional)
    time_to_target_s: float | None = None  # wall-clock to first reach target (None = never)
    extra: dict = field(default_factory=dict)


Arm = Callable[[int], ArmResult]  # arm(seed) -> ArmResult


# ---------------------------------------------------------------- stats


def _bootstrap_ci(deltas: list[float], iters: int = 10_000, alpha: float = 0.05,
                  seed: int = 0) -> tuple[float, float]:
    """Percentile bootstrap CI of the mean of paired deltas. Deterministic (seeded)."""
    import random
    rng = random.Random(seed)
    n = len(deltas)
    if n == 0:
        return (float("nan"), float("nan"))
    means = []
    for _ in range(iters):
        s = sum(deltas[rng.randrange(n)] for _ in range(n)) / n
        means.append(s)
    means.sort()
    lo = means[int(alpha / 2 * iters)]
    hi = means[int((1 - alpha / 2) * iters)]
    return (lo, hi)


@dataclass
class AblationVerdict:
    label_treatment: str
    label_baseline: str
    n_seeds: int
    mean_score_treatment: float
    mean_score_baseline: float
    mean_delta: float          # treatment - baseline (paired)
    delta_ci: tuple[float, float]
    win_rate: float            # fraction of seeds treatment >= baseline
    mean_wall_treatment: float
    mean_wall_baseline: float
    supported: bool            # CI excludes 0 on the positive side

    def summary(self) -> str:
        lo, hi = self.delta_ci
        verdict = "SUPPORTED" if self.supported else "not supported (CI includes 0)"
        return (
            f"{self.label_treatment} vs {self.label_baseline}  (n={self.n_seeds})\n"
            f"  score:  {self.mean_score_treatment:.6g}  vs  {self.mean_score_baseline:.6g}\n"
            f"  paired Δ = {self.mean_delta:+.6g}  95% CI [{lo:+.6g}, {hi:+.6g}]  -> {verdict}\n"
            f"  win-rate (treatment ≥ baseline): {self.win_rate:.0%}\n"
            f"  mean wall: {self.mean_wall_treatment:.2f}s vs {self.mean_wall_baseline:.2f}s"
        )


def run_ablation(
    treatment: Arm,
    baseline: Arm,
    seeds: list[int],
    *,
    label_treatment: str,
    label_baseline: str,
    out_path: str | Path | None = None,
) -> AblationVerdict:
    """Run both arms over the paired seeds, record per-seed JSONL, return the verdict."""
    rows = []
    deltas, wins = [], 0
    st, sb, wt, wb = [], [], [], []
    for seed in seeds:
        t = treatment(seed)
        b = baseline(seed)
        d = t.score - b.score
        deltas.append(d)
        wins += 1 if d >= 0 else 0
        st.append(t.score)
        sb.append(b.score)
        wt.append(t.wall_s)
        wb.append(b.wall_s)
        rows.append({"seed": seed, "delta": d,
                     "treatment": asdict(t), "baseline": asdict(b)})
    n = len(seeds)

    def mean(x):
        return sum(x) / len(x) if x else float("nan")

    md = mean(deltas)
    ci = _bootstrap_ci(deltas)
    verdict = AblationVerdict(
        label_treatment=label_treatment, label_baseline=label_baseline, n_seeds=n,
        mean_score_treatment=mean(st), mean_score_baseline=mean(sb),
        mean_delta=md, delta_ci=ci, win_rate=wins / n if n else float("nan"),
        mean_wall_treatment=mean(wt), mean_wall_baseline=mean(wb),
        supported=(ci[0] > 0),
    )
    if out_path:
        out = Path(out_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w") as fh:
            fh.write(json.dumps({"verdict": asdict(verdict)}) + "\n")
            for r in rows:
                fh.write(json.dumps(r) + "\n")
    return verdict


# ---------------------------------------------------------------- arm factories
# EXAMPLES — verify signatures against the real evaluator + pick a family that passes
# the headroom screen before trusting a result. See mechanism-claims-test-matrix.md.


def make_plugin_arms(family_name: str, n: int):
    """Claim #3: a problem-specific plugin vs the generic Optimizer on `family_name`.

    ⚠️ HEADROOM SCREEN: only meaningful on a family where the GENERIC arm genuinely
    underperforms. circle packing is saturated (both solve it) -> use a harder family.

    TODO before running for real:
      - choose (family, plugin) with generic headroom (e.g. a sphere family + Riemannian
        / PT-SA plugin from einstein.gpu_tempering, vs generic flat Optimizer);
      - confirm the cold-init format the strategy fns expect (flat list[float]);
      - confirm the plugin's call signature + that it returns a comparable scored config.
    """
    import numpy as np

    from einstein import optimizer as opt
    from einstein.ablation_packing import families

    fam = families.get_family(family_name)
    score = fam.score  # centers -> float (maximize)

    def cold_init(seed: int):
        return np.random.default_rng(seed).uniform(0, 1, (n, 2))

    def generic(seed: int) -> ArmResult:
        x0 = cold_init(seed)
        o = opt.Optimizer(score_fn=score, direction="maximize", category="continuous")
        for fn_name in ("_strategy_lbfgsb", "_strategy_nelder_mead", "_strategy_perturbation"):
            o.add_strategy(fn_name, getattr(opt, fn_name))
        t0 = time.time()
        rec = o.run_iteration(x0, strategies=["_strategy_lbfgsb", "_strategy_nelder_mead",
                                              "_strategy_perturbation"], seed=seed)
        return ArmResult(seed=seed, score=rec["best_score"], wall_s=time.time() - t0)

    def plugin(seed: int) -> ArmResult:
        raise NotImplementedError(
            "Wire the family-specific plugin here (e.g. gpu_tempering.run_fused_tempering "
            "for a sphere family, or circle_packing_square.polish.polish for circles). "
            "Keep cold_init(seed) identical to the generic arm for pairing.")

    return plugin, generic


def make_sphere_plugin_arms(problem: str, n: int):
    """Claim #3 on a SPHERE family with REAL generic headroom: a manifold-aware
    (Riemannian projected-gradient) plugin vs the generic flat Optimizer, on the SAME
    score and SAME cold-init per seed (random points on S^2 from default_rng(seed)).

    problem="tammes": maximize the minimum pairwise distance of n unit vectors on S^2.

    HEADROOM (verified, this branch): the Tammes objective is NON-SMOOTH — it depends
    only on the single closest pair — so the generic Optimizer's finite-difference
    L-BFGS-B/Nelder-Mead see a near-zero gradient and stall near the cold init. The
    plugin optimizes a SMOOTH soft-min surrogate (log-sum-exp of pairwise distances,
    β annealed 5→160) with the gradient projected to the sphere's tangent space and a
    renormalize (retract) each step — geometry the flat optimizer doesn't know. At
    n=50 over 5 seeds: generic mean 0.323 vs plugin 0.493 (Δ +0.17, plugin wins every
    seed; arena Tammes-50 optimum ≈ 0.5099). Thomson (smooth Coulomb energy) was
    screened OUT: flat quasi-Newton L-BFGS-B matches a first-order Riemannian arm there
    (no headroom), so it is not used.

    Both arms share `score` (true min pairwise distance, the arena Tammes objective) and
    `cold_init(seed)`; the plugin only uses the surrogate internally, then reports the
    real score — so the comparison is apples-to-apples and paired by seed.
    """
    import numpy as np

    from einstein import optimizer as opt

    if problem != "tammes":
        raise NotImplementedError(
            f"sphere plugin family {problem!r} not wired; only 'tammes' passes the "
            "headroom screen (thomson is smooth -> flat L-BFGS-B has no headroom).")

    dim = 3

    def cold_init(seed: int) -> np.ndarray:
        rng = np.random.default_rng(seed)
        x = rng.standard_normal((n, dim))
        return x / np.linalg.norm(x, axis=1, keepdims=True)

    def min_dist(pts: np.ndarray) -> float:
        gram = pts @ pts.T
        iu = np.triu_indices(len(pts), 1)
        return float(np.sqrt(2.0 * (1.0 - np.clip(gram[iu], -1.0, 1.0)).min()))

    def score(flat) -> float:  # SAME objective for both arms (maximize)
        pts = np.asarray(flat, dtype=float).reshape(n, dim)
        norms = np.linalg.norm(pts, axis=1, keepdims=True)
        norms[norms < 1e-12] = 1e-12
        return min_dist(pts / norms)

    def generic(seed: int) -> ArmResult:
        x0 = cold_init(seed)
        o = opt.Optimizer(score_fn=score, direction="maximize", category="continuous")
        t0 = time.time()
        rec = o.run_iteration(list(x0.flatten()),
                              strategies=["lbfgsb", "perturbation", "nelder_mead"], seed=seed)
        return ArmResult(seed=seed, score=rec["best_score"], wall_s=time.time() - t0)

    def plugin(seed: int) -> ArmResult:
        # Riemannian projected-gradient ascent on a log-sum-exp soft-min surrogate.
        pts = cold_init(seed)
        t0 = time.time()
        for beta in (5.0, 10.0, 20.0, 40.0, 80.0, 160.0):
            lr = 0.05
            for _ in range(70):
                diff = pts[:, None, :] - pts[None, :, :]
                d2 = np.sum(diff**2, axis=-1)
                np.fill_diagonal(d2, np.inf)
                d = np.sqrt(d2)
                w = np.exp(-beta * d)
                np.fill_diagonal(w, 0.0)
                coef = -beta * w / d
                np.fill_diagonal(coef, 0.0)
                grad = np.einsum("ijk,ij->ik", diff, coef)          # ambient grad of S=Σexp(-βd)
                tang = grad - np.sum(grad * pts, axis=1, keepdims=True) * pts  # project to tangent
                surr = np.sum(np.triu(w, 1))
                for _ls in range(20):                                # backtracking line search
                    cand = pts - lr * tang
                    cand /= np.linalg.norm(cand, axis=1, keepdims=True)  # retract to sphere
                    cd = cand[:, None, :] - cand[None, :, :]
                    cd2 = np.sum(cd**2, axis=-1)
                    np.fill_diagonal(cd2, np.inf)
                    surr_n = np.sum(np.triu(np.exp(-beta * np.sqrt(cd2)), 1))
                    if surr_n < surr:
                        pts = cand
                        lr *= 1.2
                        break
                    lr *= 0.5
                    if lr < 1e-10:
                        break
        return ArmResult(seed=seed, score=score(pts.flatten()), wall_s=time.time() - t0)

    return plugin, generic


def make_adaptive_arms(family_name: str, n: int, iters: int = 20):
    """Claim #2: adaptive strategy scheduling vs fixed/uniform round-robin.

    Treatment: let Optimizer.select_strategies() self-select (boosts recent winners).
    Baseline: pass an explicit fixed strategy list every iteration (uniform).
    Same plugin pool, same cold-init, same budget -> isolates the SCHEDULING.
    TODO: confirm select_strategies() works without a knowledge.yaml, or stub priors.
    """
    raise NotImplementedError("Symmetric to make_plugin_arms; wire after #3 is validated.")


# ---------------------------------------------------------------- CLI

def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--claim", choices=["plugins", "sphere-plugins", "adaptive"], required=True)
    ap.add_argument("--family", default="heilbronn_triangle",
                    help="family with GENERIC HEADROOM (not a saturated one)")
    ap.add_argument("--problem", default="tammes",
                    help="sphere problem for --claim sphere-plugins (tammes)")
    ap.add_argument("--n", type=int, default=11, help="problem size")
    ap.add_argument("--seeds", type=int, default=200)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv[1:])

    seeds = list(range(args.seeds))
    if args.claim == "plugins":
        treatment, baseline = make_plugin_arms(args.family, args.n)
        lt, lb = f"plugin/{args.family}", f"generic/{args.family}"
    elif args.claim == "sphere-plugins":
        treatment, baseline = make_sphere_plugin_arms(args.problem, args.n)
        lt = f"plugin-riemann/{args.problem}-n{args.n}"
        lb = f"generic-flat/{args.problem}-n{args.n}"
    else:
        treatment, baseline = make_adaptive_arms(args.family, args.n)
        lt, lb = "adaptive", "uniform"

    out = args.out or f"results/ablation-mechanism/{args.claim}.jsonl"
    verdict = run_ablation(treatment, baseline, seeds,
                           label_treatment=lt, label_baseline=lb, out_path=out)
    print(verdict.summary())
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv))
