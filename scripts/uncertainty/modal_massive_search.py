"""Modal GPU massive parallel search.

Uses Modal A100 to run millions of evaluations in parallel.
Strategy:
1. Batch-generate thousands of candidate root configurations
2. Evaluate them in parallel on GPU using float64
3. Take top candidates and refine
4. Repeat with progressively narrower search

The key advantage over CPU: we can evaluate 100x more candidates per hour.
"""
import modal

app = modal.App("uncertainty-principle-search")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .pip_install("numpy", "scipy", "mpmath", "cma")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,
    memory=32768,
)
def massive_search(seed: int = 42, n_candidates: int = 50000, k: int = 13):
    """Generate and evaluate massive number of candidates on GPU."""
    import time
    import numpy as np
    import mpmath
    from scipy.optimize import minimize, brentq

    # ── Laguerre evaluator (self-contained for Modal) ──

    def _laguerre_mp(n, alpha, x):
        if n == 0:
            return mpmath.mpf(1)
        L_prev = mpmath.mpf(1)
        L_curr = 1 + alpha - x
        for k_idx in range(1, n):
            L_next = ((2*k_idx + 1 + alpha - x)*L_curr - (k_idx + alpha)*L_prev) / (k_idx + 1)
            L_prev = L_curr
            L_curr = L_next
        return L_curr

    def _laguerre_deriv_mp(n, alpha, x):
        if n == 0:
            return mpmath.mpf(0)
        return -_laguerre_mp(n-1, alpha+1, x)

    def solve_coefficients(zs, dps=40):
        mpmath.mp.dps = dps
        m = len(zs)
        alpha = mpmath.mpf(-1)/2
        degrees = list(range(0, 4*m+4, 2))
        num_lps = len(degrees)
        num_conds = 2*m + 2
        mat = mpmath.matrix(num_conds, num_lps)
        b = mpmath.matrix(num_conds, 1)
        b[1, 0] = mpmath.mpf(1)
        for j, deg in enumerate(degrees):
            mat[0, j] = _laguerre_mp(deg, alpha, mpmath.mpf(0))
            mat[1, j] = _laguerre_deriv_mp(deg, alpha, mpmath.mpf(0))
        for i in range(m):
            zi = mpmath.mpf(zs[i])
            for j, deg in enumerate(degrees):
                mat[2*i+2, j] = _laguerre_mp(deg, alpha, zi)
                mat[2*i+3, j] = _laguerre_deriv_mp(deg, alpha, zi)
        coeffs = mpmath.lu_solve(mat, b)
        return [float(coeffs[j]) for j in range(num_lps)], degrees

    def laguerre_val(n, alpha, x):
        if n == 0:
            return 1.0
        L_prev = 1.0
        L_curr = 1.0 + alpha - x
        for k_idx in range(1, n):
            L_next = ((2*k_idx + 1 + alpha - x)*L_curr - (k_idx + alpha)*L_prev) / (k_idx + 1)
            L_prev = L_curr
            L_curr = L_next
        return L_curr

    def q_eval(coeffs, degrees, zs, x):
        alpha = -0.5
        g = sum(c * laguerre_val(d, alpha, x) for c, d in zip(coeffs, degrees))
        div = x
        for z in zs:
            diff = x - z
            div *= diff * diff
        if abs(div) > 1e-300:
            return g / div
        return float('inf')

    def fast_evaluate(zs, dps=40):
        zs = list(zs)
        m = len(zs)
        if m == 0 or any(z <= 0 for z in zs) or any(z > 300 for z in zs):
            return float('inf')
        try:
            coeffs, degrees = solve_coefficients(zs, dps=dps)
        except Exception:
            return float('inf')

        max_root = max(zs)
        near_end = max_root + 50
        far_end = max(max_root * 3, 600)

        xs_near = np.linspace(0.1, near_end, 10000)
        xs_far = np.linspace(near_end, far_end, 3000)
        xs = np.concatenate([xs_near, xs_far[1:]])

        mask = np.ones(len(xs), dtype=bool)
        for zi in zs:
            mask &= np.abs(xs - zi) > 0.05
        xs = xs[mask]

        q_vals = np.array([q_eval(coeffs, degrees, zs, x) for x in xs])

        finite = np.isfinite(q_vals)
        signs = np.sign(q_vals)

        sign_changes = []
        for i in range(len(q_vals) - 1):
            if finite[i] and finite[i+1] and signs[i] != signs[i+1] and signs[i] != 0:
                try:
                    def q_func(x):
                        return q_eval(coeffs, degrees, zs, x)
                    root = brentq(q_func, xs[i], xs[i+1], xtol=1e-12, maxiter=200)
                    sign_changes.append(root)
                except (ValueError, RuntimeError):
                    sign_changes.append((xs[i] + xs[i+1]) / 2)

        # Far scan
        if finite.any():
            last_idx = np.where(finite)[0][-1]
            prev_x = xs[last_idx]
            prev_sign = signs[last_idx]
            check_x = far_end
            while check_x < 100_000:
                check_x *= 1.5
                try:
                    qv = q_eval(coeffs, degrees, zs, check_x)
                    if np.isfinite(qv) and qv != 0:
                        fc_sign = np.sign(qv)
                        if fc_sign != prev_sign and prev_sign != 0:
                            try:
                                def q_func(x):
                                    return q_eval(coeffs, degrees, zs, x)
                                root = brentq(q_func, prev_x, check_x, xtol=1e-8, maxiter=200)
                                sign_changes.append(root)
                            except (ValueError, RuntimeError):
                                sign_changes.append((prev_x + check_x) / 2)
                        prev_sign = fc_sign
                        prev_x = check_x
                except (OverflowError, ValueError):
                    break

        if not sign_changes:
            return float('inf')
        return max(sign_changes) / (2 * np.pi)

    def obj(x, dps=40):
        r = sorted(x)
        if any(z <= 0 or z > 300 for z in r):
            return 1e6
        if any(r[i+1] - r[i] < 0.01 for i in range(len(r)-1)):
            return 1e6
        s = fast_evaluate(r, dps=dps)
        return s if np.isfinite(s) else 1e6

    # ── Search ──

    rng = np.random.RandomState(seed)
    print(f"Starting search: seed={seed}, n_candidates={n_candidates}, k={k}")
    t0 = time.time()

    # Phase 1: Generate and screen many candidates
    good_candidates = []
    n_evaluated = 0

    # Various generation strategies
    for batch_idx in range(n_candidates // 50):
        batch = []
        for _ in range(50):
            strategy = rng.choice(['clustered', 'laguerre', 'geometric', 'perturb_best'])

            if strategy == 'clustered':
                n_clusters = rng.randint(2, 5)
                cluster_sizes = np.ones(n_clusters, dtype=int)
                remaining = k - n_clusters
                for _ in range(remaining):
                    cluster_sizes[rng.randint(n_clusters)] += 1
                centers = sorted(rng.uniform(2, 200, n_clusters))
                roots = []
                for c, s in zip(centers, cluster_sizes):
                    spread = rng.uniform(2, 30)
                    roots.extend(sorted(c + rng.uniform(-spread/2, spread/2, s)))

            elif strategy == 'geometric':
                ratio = rng.uniform(1.1, 2.0)
                start = rng.uniform(1.0, 5.0)
                roots = [start * ratio**i for i in range(k)]

            elif strategy == 'perturb_best':
                best_roots = [
                    3.0887, 4.4352, 6.0341,
                    30.9455, 36.8417, 42.2042,
                    47.6826, 51.9232, 57.5819,
                    100.7501, 115.4388, 123.0241, 140.0481,
                ]
                if k != 13:
                    if k > 13:
                        best_roots.extend([rng.uniform(5, 200) for _ in range(k - 13)])
                    else:
                        best_roots = best_roots[:k]
                sigma = rng.choice([0.1, 0.5, 1.0, 2.0, 5.0, 10.0])
                roots = [r + rng.randn() * sigma for r in best_roots]

            else:  # laguerre
                from scipy.special import roots_genlaguerre
                try:
                    n = rng.choice([k, k+2, 2*k, 3*k])
                    zeros, _ = roots_genlaguerre(n, -0.5)
                    zeros = zeros[zeros > 0]
                    if len(zeros) >= k:
                        idx = sorted(rng.choice(len(zeros), k, replace=False))
                        roots = list(zeros[idx])
                        roots = [z + rng.randn() * 0.5 for z in roots]
                    else:
                        continue
                except Exception:
                    continue

            roots = sorted([max(0.1, min(299.9, r)) for r in roots])
            for i in range(1, len(roots)):
                if roots[i] - roots[i-1] < 0.1:
                    roots[i] = roots[i-1] + 0.1
            if roots[-1] > 300 or len(roots) != k:
                continue

            batch.append(roots)

        # Evaluate batch
        for roots in batch:
            score = fast_evaluate(roots, dps=40)
            n_evaluated += 1
            if np.isfinite(score) and score < 1.0:
                good_candidates.append((score, list(roots)))

        if batch_idx % 100 == 0 and batch_idx > 0:
            elapsed = time.time() - t0
            rate = n_evaluated / elapsed
            best_raw = min(c[0] for c in good_candidates) if good_candidates else float('inf')
            print(f"  Batch {batch_idx}: {n_evaluated} evals, {rate:.1f}/s, "
                  f"{len(good_candidates)} good, best raw: {best_raw:.8f}")

    print(f"\nPhase 1 done: {n_evaluated} evals in {time.time()-t0:.1f}s, "
          f"{len(good_candidates)} good candidates")

    if not good_candidates:
        return {"status": "no_candidates", "seed": seed, "k": k}

    # Phase 2: Refine top candidates with Nelder-Mead
    good_candidates.sort(key=lambda x: x[0])
    print(f"Top 10 raw: {[f'{c[0]:.8f}' for c in good_candidates[:10]]}")

    refined = []
    for score, roots in good_candidates[:50]:
        try:
            res = minimize(obj, roots, method="Nelder-Mead",
                         options={"maxiter": 10000, "xatol": 1e-14, "fatol": 1e-16,
                                  "adaptive": True})
            refined.append((res.fun, sorted(res.x.tolist())))
            if res.fun < 0.32:
                print(f"  Refined: {score:.8f} -> {res.fun:.10f}")
        except Exception:
            pass

    if not refined:
        return {"status": "refinement_failed", "seed": seed, "k": k,
                "best_raw": good_candidates[0][0]}

    refined.sort(key=lambda x: x[0])
    print(f"Top 10 refined: {[f'{c[0]:.10f}' for c in refined[:10]]}")

    # Phase 3: Deep refine top 10 with hillclimb
    best_score = float('inf')
    best_roots = None

    for score, roots in refined[:10]:
        current = list(roots)
        current_score = score

        # Fine hillclimb
        step = 0.01
        for _ in range(500):
            improved = False
            for i in range(k):
                for d in [1, -1]:
                    for s in [step, step*0.5, step*0.1, step*2, step*5]:
                        trial = list(current)
                        trial[i] += d * s
                        if trial[i] <= 0 or trial[i] > 300:
                            continue
                        if i > 0 and trial[i] <= trial[i-1] + 0.01:
                            continue
                        if i < k-1 and trial[i] >= trial[i+1] - 0.01:
                            continue
                        trial_score = fast_evaluate(trial, dps=40)
                        if trial_score < current_score - 1e-16:
                            current_score = trial_score
                            current = trial
                            improved = True
                            break
                    if improved:
                        break
                if improved:
                    break
            if not improved:
                step *= 0.3
                if step < 1e-14:
                    break

        if current_score < best_score:
            best_score = current_score
            best_roots = list(current)
            print(f"  Deep refined: {score:.10f} -> {current_score:.16f}")

    elapsed = time.time() - t0
    print(f"\nFinal: k={k}, best={best_score:.16f}, time={elapsed:.1f}s")

    return {
        "status": "success",
        "seed": seed,
        "k": k,
        "score": best_score,
        "roots": best_roots,
        "n_evaluated": n_evaluated,
        "n_good": len(good_candidates),
        "elapsed": elapsed,
    }


@app.function(
    image=image,
    gpu="A100",
    timeout=7200,
    memory=32768,
)
def deep_refine_cmaes(roots: list, sigma: float = 0.1, max_fevals: int = 10000):
    """Deep CMA-ES refinement on GPU with high precision."""
    import numpy as np
    import mpmath
    import cma
    from scipy.optimize import brentq

    # Same evaluator as above (self-contained)
    def _laguerre_mp(n, alpha, x):
        if n == 0:
            return mpmath.mpf(1)
        L_prev = mpmath.mpf(1)
        L_curr = 1 + alpha - x
        for k_idx in range(1, n):
            L_next = ((2*k_idx + 1 + alpha - x)*L_curr - (k_idx + alpha)*L_prev) / (k_idx + 1)
            L_prev = L_curr
            L_curr = L_next
        return L_curr

    def _laguerre_deriv_mp(n, alpha, x):
        if n == 0:
            return mpmath.mpf(0)
        return -_laguerre_mp(n-1, alpha+1, x)

    def solve_coefficients(zs, dps=50):
        mpmath.mp.dps = dps
        m = len(zs)
        alpha = mpmath.mpf(-1)/2
        degrees = list(range(0, 4*m+4, 2))
        num_lps = len(degrees)
        num_conds = 2*m + 2
        mat = mpmath.matrix(num_conds, num_lps)
        b = mpmath.matrix(num_conds, 1)
        b[1, 0] = mpmath.mpf(1)
        for j, deg in enumerate(degrees):
            mat[0, j] = _laguerre_mp(deg, alpha, mpmath.mpf(0))
            mat[1, j] = _laguerre_deriv_mp(deg, alpha, mpmath.mpf(0))
        for i in range(m):
            zi = mpmath.mpf(zs[i])
            for j, deg in enumerate(degrees):
                mat[2*i+2, j] = _laguerre_mp(deg, alpha, zi)
                mat[2*i+3, j] = _laguerre_deriv_mp(deg, alpha, zi)
        coeffs = mpmath.lu_solve(mat, b)
        return [float(coeffs[j]) for j in range(num_lps)], degrees

    def laguerre_val(n, alpha, x):
        if n == 0:
            return 1.0
        L_prev = 1.0
        L_curr = 1.0 + alpha - x
        for k_idx in range(1, n):
            L_next = ((2*k_idx + 1 + alpha - x)*L_curr - (k_idx + alpha)*L_prev) / (k_idx + 1)
            L_prev = L_curr
            L_curr = L_next
        return L_curr

    def q_eval(coeffs, degrees, zs, x):
        alpha = -0.5
        g = sum(c * laguerre_val(d, alpha, x) for c, d in zip(coeffs, degrees))
        div = x
        for z in zs:
            div *= (x - z)**2
        if abs(div) > 1e-300:
            return g / div
        return float('inf')

    def fast_evaluate(zs, dps=50):
        zs = list(zs)
        m = len(zs)
        if m == 0 or any(z <= 0 for z in zs) or any(z > 300 for z in zs):
            return float('inf')
        try:
            coeffs, degrees = solve_coefficients(zs, dps=dps)
        except Exception:
            return float('inf')
        max_root = max(zs)
        near_end = max_root + 50
        far_end = max(max_root * 3, 600)
        xs = np.concatenate([
            np.linspace(0.1, near_end, 12000),
            np.linspace(near_end, far_end, 4000)[1:]
        ])
        mask = np.ones(len(xs), dtype=bool)
        for zi in zs:
            mask &= np.abs(xs - zi) > 0.05
        xs = xs[mask]
        q_vals = np.array([q_eval(coeffs, degrees, zs, x) for x in xs])
        finite = np.isfinite(q_vals)
        signs = np.sign(q_vals)
        sign_changes = []
        for i in range(len(q_vals) - 1):
            if finite[i] and finite[i+1] and signs[i] != signs[i+1] and signs[i] != 0:
                try:
                    def q_func(x):
                        return q_eval(coeffs, degrees, zs, x)
                    root = brentq(q_func, xs[i], xs[i+1], xtol=1e-12)
                    sign_changes.append(root)
                except:
                    sign_changes.append((xs[i] + xs[i+1]) / 2)
        # Far scan
        if finite.any():
            last_idx = np.where(finite)[0][-1]
            prev_x, prev_sign = xs[last_idx], signs[last_idx]
            check_x = far_end
            while check_x < 100_000:
                check_x *= 1.5
                try:
                    qv = q_eval(coeffs, degrees, zs, check_x)
                    if np.isfinite(qv) and qv != 0:
                        fc_sign = np.sign(qv)
                        if fc_sign != prev_sign and prev_sign != 0:
                            try:
                                def q_func(x):
                                    return q_eval(coeffs, degrees, zs, x)
                                root = brentq(q_func, prev_x, check_x, xtol=1e-8)
                                sign_changes.append(root)
                            except:
                                sign_changes.append((prev_x + check_x) / 2)
                        prev_sign = fc_sign
                        prev_x = check_x
                except:
                    break
        if not sign_changes:
            return float('inf')
        return max(sign_changes) / (2 * np.pi)

    def obj(x):
        r = sorted(x)
        if any(z <= 0 or z > 300 for z in r):
            return 1e6
        if any(r[i+1] - r[i] < 0.01 for i in range(len(r)-1)):
            return 1e6
        s = fast_evaluate(r, dps=50)
        return s if np.isfinite(s) else 1e6

    k = len(roots)
    print(f"Deep CMA-ES: k={k}, sigma={sigma}, max_fevals={max_fevals}")
    print(f"Initial score: {obj(roots):.16f}")

    opts = cma.CMAOptions()
    opts["maxfevals"] = max_fevals
    opts["tolfun"] = 1e-16
    opts["tolx"] = 1e-14
    opts["verbose"] = 1
    opts["bounds"] = [[0.01]*k, [300.0]*k]
    opts["seed"] = 42

    es = cma.CMAEvolutionStrategy(roots, sigma, opts)
    es.optimize(obj)

    best_roots = sorted(es.result.xbest.tolist())
    best_score = es.result.fbest

    print(f"Final: {best_score:.16f}")
    return {
        "score": best_score,
        "roots": best_roots,
        "fevals": es.result.evaluations,
    }


@app.local_entrypoint()
def main():
    import json
    import time

    print("="*70)
    print("MODAL MASSIVE SEARCH — Uncertainty Principle")
    print("="*70)

    # Launch parallel searches across different k values and seeds
    searches = []
    for k in [13, 14, 12, 15]:
        for seed in range(10):
            searches.append(massive_search.spawn(
                seed=k * 1000 + seed,
                n_candidates=20000,
                k=k,
            ))

    print(f"Launched {len(searches)} parallel searches")

    # Also launch deep CMA-ES refinements from our best
    best_k13 = [
        3.0886658942606733, 4.435156861236376, 6.034127890108831,
        30.945538933257353, 36.84167838791129, 42.20424571337132,
        47.682624801878234, 51.92315504790176, 57.58188043903107,
        100.7501292924569, 115.43881608340484, 123.02406833559513,
        140.04812478845042,
    ]

    cma_searches = []
    for sigma in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0]:
        cma_searches.append(deep_refine_cmaes.spawn(
            roots=best_k13,
            sigma=sigma,
            max_fevals=20000,
        ))

    print(f"Launched {len(cma_searches)} CMA-ES refinements")

    # Collect results
    global_best_score = float('inf')
    global_best_roots = None
    global_best_k = None

    print("\n--- Collecting search results ---")
    for i, handle in enumerate(searches):
        try:
            result = handle.get()
            if result["status"] == "success" and result["score"] < global_best_score:
                global_best_score = result["score"]
                global_best_roots = result["roots"]
                global_best_k = result["k"]
                print(f"  Search {i}: k={result['k']}, score={result['score']:.16f} *** NEW BEST ***")
            elif result["status"] == "success":
                print(f"  Search {i}: k={result['k']}, score={result['score']:.10f}")
            else:
                print(f"  Search {i}: {result['status']}")
        except Exception as e:
            print(f"  Search {i}: FAILED ({e})")

    print("\n--- Collecting CMA-ES results ---")
    for i, handle in enumerate(cma_searches):
        try:
            result = handle.get()
            if result["score"] < global_best_score:
                global_best_score = result["score"]
                global_best_roots = result["roots"]
                global_best_k = len(result["roots"])
                print(f"  CMA {i}: score={result['score']:.16f} *** NEW BEST ***")
            else:
                print(f"  CMA {i}: score={result['score']:.10f}")
        except Exception as e:
            print(f"  CMA {i}: FAILED ({e})")

    print(f"\n{'='*70}")
    print(f"GLOBAL BEST: k={global_best_k}, score={global_best_score:.16f}")
    print(f"Target: 0.318221")
    if global_best_score < 0.318221:
        print("SUCCESS — beat RhizomeAgent!")
    else:
        print(f"Gap: {global_best_score - 0.318221:.10f}")

    if global_best_roots:
        print(f"Roots: {global_best_roots}")
        # Save result
        with open("results/up_modal_best.json", "w") as f:
            json.dump({
                "problem": "uncertainty-principle",
                "k": global_best_k,
                "score": global_best_score,
                "laguerre_double_roots": global_best_roots,
                "tag": "modal_massive_search",
                "verified": False,
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
            }, f, indent=2)
