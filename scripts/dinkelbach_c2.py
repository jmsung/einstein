"""Dinkelbach + LogSumExp + L-BFGS optimizer for Problem 3 (PATH B).

Maximize C = (2*sum(c^2) + sum(c_i*c_{i+1})) / (3 * sum(c) * max(c))
where c = convolve(f, f, mode='full') and f >= 0.

Two-level optimization:
  1. Outer: simulated annealing on support structure (which positions are nonzero)
  2. Inner: Dinkelbach + L-BFGS on values at fixed positions

This hybrid avoids the plateau issue where gradient methods can't change the
support structure (zero -> nonzero transitions are invisible to gradients on w).

Target: C > 0.90 at n=2000 on CPU.
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize
from scipy.signal import fftconvolve

from einstein.autocorrelation import evaluate
from einstein.autocorrelation_fast import diagnose, fast_evaluate, score_from_conv

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def save_result(f, score, tag=""):
    """Save a result to disk."""
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": f.tolist() if isinstance(f, np.ndarray) else f,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"c2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")
    return fname


# ---------------------------------------------------------------------------
# Score computation
# ---------------------------------------------------------------------------
def compute_score(f):
    """Compute C from f using FFT convolution + exact arena formula."""
    conv = fftconvolve(f, f, mode="full")
    return score_from_conv(conv)


# ---------------------------------------------------------------------------
# LogSumExp smooth max and gradient
# ---------------------------------------------------------------------------
def logsumexp_max_and_grad(c, beta):
    """LogSumExp smooth max proxy and gradient."""
    c_max_val = np.max(c)
    if c_max_val <= 0:
        return 0.0, np.zeros_like(c)
    z = np.clip(beta * (c / c_max_val - 1.0), -700, 0)
    exp_z = np.exp(z)
    nc = len(c)
    mean_exp_z = np.sum(exp_z) / nc
    if mean_exp_z <= 0:
        return c_max_val, np.zeros_like(c)
    proxy = c_max_val * mean_exp_z ** (1.0 / beta)
    grad = mean_exp_z ** (1.0 / beta - 1.0) * exp_z / nc
    return proxy, grad


# ---------------------------------------------------------------------------
# Fixed-support optimizer: optimize values at given positions
# ---------------------------------------------------------------------------
def optimize_values_at_positions(positions, n, v_init=None, beta_schedule=(5000, 50000, 500000),
                                  outer_iters=5, maxiter_lbfgs=300, time_limit=5):
    """Optimize values at fixed positions using Dinkelbach + L-BFGS.

    Only optimizes the K values at the given positions (much smaller problem).
    """
    k = len(positions)
    positions = np.asarray(positions)

    if v_init is None:
        v_init = np.ones(k)
    v_init = np.maximum(v_init, 0.0)
    w = np.sqrt(v_init + 1e-12)

    def make_f(vals):
        f = np.zeros(n)
        f[positions] = vals
        return f

    best_f = make_f(v_init)
    best_score = compute_score(best_f)
    t0 = time.time()

    f0 = make_f(w * w)
    conv = fftconvolve(f0, f0, mode="full")
    lam = score_from_conv(conv)

    for beta in beta_schedule:
        if time.time() - t0 > time_limit:
            break

        for outer in range(outer_iters):
            if time.time() - t0 > time_limit:
                break

            def obj_grad(w_k):
                vals = w_k * w_k
                f = make_f(vals)
                conv = fftconvolve(f, f, mode="full")

                if not np.all(np.isfinite(conv)):
                    return 1e30, np.zeros_like(w_k)

                sum_c2 = np.sum(conv * conv)
                sum_cc = np.sum(conv[:-1] * conv[1:])
                numer = 2.0 * sum_c2 + sum_cc

                c_sum = np.sum(conv)
                proxy_max, d_proxy_dc = logsumexp_max_and_grad(conv, beta)
                denom_proxy = 3.0 * c_sum * proxy_max

                if not np.isfinite(numer) or not np.isfinite(denom_proxy):
                    return 1e30, np.zeros_like(w_k)

                phi = numer - lam * denom_proxy
                obj = -phi

                dnumer_dc = 4.0 * conv.copy()
                dnumer_dc[1:] += conv[:-1]
                dnumer_dc[:-1] += conv[1:]

                ddenom_dc = 3.0 * (proxy_max + c_sum * d_proxy_dc)
                dphi_dc = dnumer_dc - lam * ddenom_dc

                # d(phi)/d(f_i) = 2 * sum_k dphi_dc[k] * f[k-i]
                dphi_df_full = 2.0 * fftconvolve(dphi_dc, f[::-1], mode="full")
                dphi_df_full = dphi_df_full[n - 1: 2 * n - 1]

                # Extract gradient only at positions
                dphi_dv = dphi_df_full[positions]

                # Chain: d(-phi)/d(w_k_i) = -dphi_dv_i * 2 * w_k_i
                dobj_dw = -dphi_dv * 2.0 * w_k
                dobj_dw = np.clip(dobj_dw, -1e15, 1e15)
                dobj_dw = np.nan_to_num(dobj_dw, nan=0.0, posinf=1e15, neginf=-1e15)

                return obj, dobj_dw

            result = minimize(
                obj_grad, w, method="L-BFGS-B", jac=True,
                options={
                    "maxiter": maxiter_lbfgs,
                    "maxfun": maxiter_lbfgs * 3,
                    "ftol": 1e-15, "gtol": 1e-10, "maxls": 40,
                },
            )

            w = result.x
            vals = w * w
            # Normalize
            s = np.sum(vals)
            if s > 0:
                vals *= k / s
                w = np.sqrt(vals)

            f_current = make_f(vals)
            score = compute_score(f_current)
            lam = score

            if score > best_score:
                best_score = score
                best_f = f_current.copy()

            if result.nit <= 1:
                break

    return best_f, best_score


# ---------------------------------------------------------------------------
# Full optimizer (all n dimensions)
# ---------------------------------------------------------------------------
def optimize_full(n, f_init, beta_schedule=(5000, 50000, 500000),
                  outer_iters=5, maxiter_lbfgs=500, time_limit=10):
    """Full-space Dinkelbach + L-BFGS optimization."""
    f = np.maximum(f_init, 0.0).copy()
    s = np.sum(f)
    if s > 0:
        f *= n / s
    w = np.sqrt(f)
    best_f = f.copy()
    best_score = fast_evaluate(f)
    t0 = time.time()

    conv = fftconvolve(f, f, mode="full")
    lam = score_from_conv(conv)

    for beta in beta_schedule:
        if time.time() - t0 > time_limit:
            break
        for outer in range(outer_iters):
            if time.time() - t0 > time_limit:
                break

            def obj_grad(w_flat):
                ff = w_flat * w_flat
                ff_sum = np.sum(ff)
                if ff_sum < 1e-30:
                    return 0.0, np.zeros_like(w_flat)

                conv = fftconvolve(ff, ff, mode="full")
                if not np.all(np.isfinite(conv)):
                    return 1e30, np.zeros_like(w_flat)

                sum_c2 = np.sum(conv * conv)
                sum_cc = np.sum(conv[:-1] * conv[1:])
                numer = 2.0 * sum_c2 + sum_cc
                c_sum = np.sum(conv)
                proxy_max, d_proxy_dc = logsumexp_max_and_grad(conv, beta)
                denom_proxy = 3.0 * c_sum * proxy_max

                if not np.isfinite(numer) or not np.isfinite(denom_proxy):
                    return 1e30, np.zeros_like(w_flat)

                phi = numer - lam * denom_proxy
                obj = -phi

                dnumer_dc = 4.0 * conv.copy()
                dnumer_dc[1:] += conv[:-1]
                dnumer_dc[:-1] += conv[1:]
                ddenom_dc = 3.0 * (proxy_max + c_sum * d_proxy_dc)
                dphi_dc = dnumer_dc - lam * ddenom_dc

                dphi_df = 2.0 * fftconvolve(dphi_dc, ff[::-1], mode="full")
                dphi_df = dphi_df[n - 1: 2 * n - 1]
                dobj_dw = -dphi_df * 2.0 * w_flat
                dobj_dw = np.clip(dobj_dw, -1e15, 1e15)
                dobj_dw = np.nan_to_num(dobj_dw, nan=0.0)

                return obj, dobj_dw

            result = minimize(
                obj_grad, w, method="L-BFGS-B", jac=True,
                options={
                    "maxiter": maxiter_lbfgs,
                    "maxfun": maxiter_lbfgs * 3,
                    "ftol": 1e-15, "gtol": 1e-10, "maxls": 40,
                },
            )

            w = result.x
            f_current = w * w
            s = np.sum(f_current)
            if s > 0:
                f_current *= n / s
                w = np.sqrt(f_current)

            conv = fftconvolve(f_current, f_current, mode="full")
            score = score_from_conv(conv)
            lam = score

            if score > best_score:
                best_score = score
                best_f = f_current.copy()

            if result.nit <= 1:
                break

    return best_f, best_score


# ---------------------------------------------------------------------------
# Support structure mutations
# ---------------------------------------------------------------------------
def mutate_support(positions, n, rng, n_changes=3):
    """Mutate support: add/remove/shift some positions."""
    positions = list(positions)
    k = len(positions)
    pos_set = set(positions)

    for _ in range(n_changes):
        action = rng.integers(4)

        if action == 0 and k > 5:
            # Remove a random position
            idx = rng.integers(k)
            pos_set.discard(positions[idx])
            positions.pop(idx)
            k -= 1

        elif action == 1:
            # Add a new position (near existing or random)
            if rng.random() < 0.7 and k > 0:
                # Near existing
                base = positions[rng.integers(k)]
                offset = rng.integers(-10, 11)
                new_pos = base + offset
            else:
                new_pos = rng.integers(0, n)
            if 0 <= new_pos < n and new_pos not in pos_set:
                positions.append(new_pos)
                pos_set.add(new_pos)
                k += 1

        elif action == 2 and k > 0:
            # Shift a position
            idx = rng.integers(k)
            old_pos = positions[idx]
            shift = rng.integers(-5, 6)
            new_pos = old_pos + shift
            if 0 <= new_pos < n and new_pos not in pos_set:
                pos_set.discard(old_pos)
                pos_set.add(new_pos)
                positions[idx] = new_pos

        elif action == 3 and k > 1:
            # Swap: remove one, add one elsewhere
            idx = rng.integers(k)
            pos_set.discard(positions[idx])
            positions.pop(idx)
            k -= 1
            new_pos = rng.integers(0, n)
            while new_pos in pos_set:
                new_pos = rng.integers(0, n)
            positions.append(new_pos)
            pos_set.add(new_pos)
            k += 1

    return sorted(positions)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Dinkelbach + LogSumExp + L-BFGS Optimizer (PATH B)")
    print("Target: C > 0.90 at n=2000")
    print("=" * 60)

    t_start = time.time()
    n = 2000
    rng = np.random.default_rng(42)

    # Phase 1: Quick scan of cluster initializations with full optimizer
    print(f"\n--- Phase 1: Init scan at n={n} ---")
    best_f = None
    best_score = 0.0

    for nc in [15, 20, 25, 30, 40, 50, 60]:
        for cw in [1, 2, 3, 4]:
            if time.time() - t_start > 40:
                break
            f_init = np.zeros(n)
            seed = rng.integers(100000)
            r = np.random.default_rng(seed)
            spacing = n // nc
            for c in range(nc):
                center = c * spacing + spacing // 2
                for offset in range(-cw, cw + 1):
                    idx = center + offset
                    if 0 <= idx < n:
                        f_init[idx] = abs(1.0 + 0.3 * r.standard_normal())

            f, score = optimize_full(
                n, f_init, (1000, 5000, 50000, 200000), 4, 300, time_limit=3,
            )
            if score > best_score:
                best_score = score
                best_f = f.copy()
                nnz = np.count_nonzero(f > 1e-10)
                print(f"  cl_{nc}_w{cw}: C={score:.8f} nnz={nnz} *** BEST")
        if time.time() - t_start > 40:
            break

    print(f"  Phase 1 best: C={best_score:.8f}")

    # Phase 2: Intensive optimization with support structure mutations
    print(f"\n--- Phase 2: Support mutation + value optimization ---")

    # Extract support from best solution
    positions = list(np.where(best_f > 1e-10)[0])
    values = best_f[best_f > 1e-10]

    stale_count = 0

    for rnd in range(200):
        elapsed = time.time() - t_start
        if elapsed > 200:
            break

        if rnd == 0:
            # First round: just optimize values at current positions
            f, score = optimize_values_at_positions(
                positions, n, values,
                beta_schedule=(5000, 50000, 500000), outer_iters=5,
                maxiter_lbfgs=500, time_limit=5,
            )
        else:
            # Mutate support, then optimize values
            n_changes = 1 + int(3 * rng.random())
            if stale_count > 10:
                n_changes = 5 + int(10 * rng.random())

            new_positions = mutate_support(positions, n, rng, n_changes)

            # Initialize values: inherit from best_f where possible, else random
            v_init = np.zeros(len(new_positions))
            for i, p in enumerate(new_positions):
                if best_f[p] > 1e-10:
                    v_init[i] = best_f[p]
                else:
                    v_init[i] = rng.exponential(np.mean(values))

            f, score = optimize_values_at_positions(
                new_positions, n, v_init,
                beta_schedule=(5000, 50000, 500000), outer_iters=4,
                maxiter_lbfgs=300, time_limit=3,
            )

        if score > best_score + 1e-6:
            best_score = score
            best_f = f.copy()
            positions = list(np.where(best_f > 1e-10)[0])
            values = best_f[best_f > 1e-10]
            stale_count = 0
            print(f"  R{rnd+1}: C={score:.8f} nnz={len(positions)} *** NEW BEST")
        else:
            stale_count += 1
            if rnd % 20 == 0:
                print(f"  R{rnd+1}: C={score:.8f} (best={best_score:.8f}, stale={stale_count})")

    print(f"\n  Phase 2 best: C={best_score:.8f}")

    # Phase 3: Full-space refinement from best solution
    print(f"\n--- Phase 3: Full-space refinement ---")
    for rnd in range(15):
        elapsed = time.time() - t_start
        if elapsed > 265:
            break

        # Small perturbation of best
        f_start = best_f.copy()
        if rnd > 0:
            mask = f_start > 1e-10
            f_start[mask] *= np.exp(0.1 * rng.standard_normal(np.sum(mask)))
            f_start = np.maximum(f_start, 0.0)

        f, score = optimize_full(
            n, f_start, (10000, 100000, 1000000), 8, 600, time_limit=6,
        )

        if score > best_score + 1e-7:
            best_score = score
            best_f = f.copy()
            print(f"  R{rnd+1}: C={score:.8f} *** NEW BEST")

    print(f"  Phase 3 best: C={best_score:.8f}")
    save_result(best_f, best_score, "dinkelbach_n2000")

    # Final verification
    print(f"\n{'='*60}")
    print("Final Verification")
    print(f"{'='*60}")

    arena_score = evaluate({"values": best_f.tolist()})
    fast_score = fast_evaluate(best_f)

    print(f"  Fast evaluator:  C={fast_score:.10f}")
    print(f"  Arena evaluator: C={arena_score:.10f}")
    print(f"  n={len(best_f)}, nonzero={np.count_nonzero(best_f > 1e-10)}")

    d = diagnose(best_f)
    print(f"  Blocks: {d['n_blocks']}, mean width: {d['mean_block_width']:.1f}")
    print(f"  Conv std/mean: {d['conv_std_over_mean']:.4f}")

    save_result(best_f, arena_score, "dinkelbach_final")

    total_time = time.time() - t_start
    print(f"\n  Total time: {total_time:.1f}s")
    print(f"  {'TARGET MET (>0.90)!' if arena_score > 0.90 else 'Below target (0.90)'}")


if __name__ == "__main__":
    main()
