"""Modal GPU basin search for Circles in Rectangle (n=21).

Strategy: massive parallel multistart with diverse initialization + SLSQP polish.
Goal: discover a novel basin with higher strict-disjoint floor.

Usage:
    modal run scripts/circles_rectangle/gpu_basin_search.py
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import modal

app = modal.App("circles-rectangle-basin-search")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("numpy==1.26.4", "scipy==1.13.1")
)

N = 21
KNOWN_BASIN_EXACT = 2.365832375910832741572  # exact from KKT solve
ARENA_BEST = 2.3658323759185156


@app.function(
    image=image,
    cpu=8,
    timeout=3600,
    memory=16384,
)
def run_batch(batch_id: int, n_trials: int, warmstart_circles: list | None = None) -> dict:
    """Run n_trials of diverse init + SA + SLSQP polish."""
    import numpy as np
    from scipy.optimize import minimize

    rng = np.random.default_rng(batch_id * 10007 + 42)
    results = []
    best_score = -np.inf
    best_circles = None
    best_w = None

    def polish_slsqp(circles_in, w_in, maxiter=500):
        """SLSQP polish — returns (circles, w, score) or None on failure."""
        n = len(circles_in)
        c = np.array(circles_in, dtype=np.float64).copy()

        # Translate to origin
        xmin = float(np.min(c[:, 0] - c[:, 2]))
        ymin = float(np.min(c[:, 1] - c[:, 2]))
        c[:, 0] -= xmin
        c[:, 1] -= ymin

        bbox_w = float(np.max(c[:, 0] + c[:, 2]))
        bbox_h = float(np.max(c[:, 1] + c[:, 2]))
        scale = 2.0 / (bbox_w + bbox_h)
        c *= scale
        w = float(np.max(c[:, 0] + c[:, 2]))

        x0 = np.empty(3 * n + 1)
        x0[:3*n] = c.flatten()
        x0[3*n] = w

        def obj(x):
            return -float(np.sum(x[2:3*n:3]))

        def obj_jac(x):
            g = np.zeros_like(x)
            g[2:3*n:3] = -1.0
            return g

        def cons(x):
            cc = x[:3*n].reshape(n, 3)
            ww = x[3*n]
            hh = 2.0 - ww
            walls = np.concatenate([
                cc[:, 0] - cc[:, 2],
                ww - cc[:, 0] - cc[:, 2],
                cc[:, 1] - cc[:, 2],
                hh - cc[:, 1] - cc[:, 2],
            ])
            pairs = np.empty(n*(n-1)//2)
            k = 0
            for i in range(n):
                for j in range(i+1, n):
                    d = np.sqrt((cc[i,0]-cc[j,0])**2 + (cc[i,1]-cc[j,1])**2)
                    pairs[k] = d - cc[i,2] - cc[j,2]
                    k += 1
            return np.concatenate([walls, pairs])

        try:
            res = minimize(
                obj, x0, jac=obj_jac,
                constraints=[{"type": "ineq", "fun": cons}],
                bounds=[(0, 2)] * (3*n) + [(0.01, 1.99)],
                method="SLSQP",
                options={"ftol": 1e-16, "maxiter": maxiter},
            )
            polished = res.x[:3*n].reshape(n, 3)
            w_out = res.x[3*n]
            score = float(np.sum(polished[:, 2]))

            # Verify strictly disjoint
            for i in range(n):
                for j in range(i+1, n):
                    d = np.sqrt((polished[i,0]-polished[j,0])**2 + (polished[i,1]-polished[j,1])**2)
                    if d < polished[i,2] + polished[j,2] - 1e-9:
                        return None
            return polished, w_out, score
        except Exception:
            return None

    def greedy_placement(rng, w, h, r_range=(0.04, 0.18)):
        """Greedy random placement — tries to place biggest circles first."""
        circles = np.zeros((N, 3))
        for idx in range(N):
            best_r = 0
            best_pos = None
            for _ in range(800):
                r = rng.uniform(*r_range)
                cx = rng.uniform(r, w - r)
                cy = rng.uniform(r, h - r)
                ok = True
                for k in range(idx):
                    d = np.hypot(circles[k, 0] - cx, circles[k, 1] - cy)
                    if d < r + circles[k, 2]:
                        ok = False
                        break
                if ok and r > best_r:
                    best_r = r
                    best_pos = (cx, cy, r)
            if best_pos is None:
                # try small fallback
                for _ in range(2000):
                    r = rng.uniform(0.01, 0.05)
                    cx = rng.uniform(r, w - r)
                    cy = rng.uniform(r, h - r)
                    ok = True
                    for k in range(idx):
                        d = np.hypot(circles[k, 0] - cx, circles[k, 1] - cy)
                        if d < r + circles[k, 2]:
                            ok = False
                            break
                    if ok:
                        best_pos = (cx, cy, r)
                        break
                if best_pos is None:
                    return None  # failed
            circles[idx] = best_pos
        return circles

    def hex_grid_init(w, h, n_target=N):
        """Hexagonal grid initialization with variable radii."""
        # Determine grid dimensions
        approx_r = min(w, h) / 8
        cols = max(1, int(w / (2 * approx_r)))
        rows = max(1, int(h / (2 * approx_r * 0.866)))
        while rows * cols < n_target:
            approx_r *= 0.95
            cols = max(1, int(w / (2 * approx_r)))
            rows = max(1, int(h / (2 * approx_r * 0.866)))

        circles = []
        for row in range(rows):
            for col in range(cols):
                if len(circles) >= n_target:
                    break
                cx = (col + 0.5) * (w / cols)
                if row % 2 == 1:
                    cx += 0.5 * (w / cols)
                    cx = min(cx, w - approx_r)
                cy = (row + 0.5) * (h / rows)
                cx = np.clip(cx, approx_r, w - approx_r)
                cy = np.clip(cy, approx_r, h - approx_r)
                circles.append([cx, cy, approx_r * 0.9])
            if len(circles) >= n_target:
                break

        if len(circles) < n_target:
            return None
        return np.array(circles[:n_target], dtype=np.float64)

    for trial in range(n_trials):
        seed = batch_id * n_trials + trial
        trial_rng = np.random.default_rng(seed * 37 + 7)
        init_type = trial % 8

        # Various aspect ratios
        w_choices = [0.85, 0.90, 0.95, 0.98, 1.00, 1.02, 1.05, 1.10, 1.15, 1.20]
        w_val = w_choices[trial % len(w_choices)]
        h_val = 2.0 - w_val

        circles = None

        if init_type == 0 and warmstart_circles:
            # Perturbed warmstart
            ws = np.array(warmstart_circles[trial % len(warmstart_circles)], dtype=np.float64)
            circles = ws.copy()
            sigma = 0.005 + 0.05 * trial_rng.random()
            circles[:, :2] += trial_rng.normal(0, sigma, (N, 2))
            circles[:, 2] *= (1 + trial_rng.normal(0, sigma/5, N))
            circles[:, 2] = np.maximum(circles[:, 2], 0.01)
        elif init_type == 1:
            # Hex grid
            circles = hex_grid_init(w_val, h_val)
        elif init_type == 2:
            # Greedy with small radii
            circles = greedy_placement(trial_rng, w_val, h_val, r_range=(0.02, 0.12))
        elif init_type == 3:
            # Greedy with large radii
            circles = greedy_placement(trial_rng, w_val, h_val, r_range=(0.06, 0.20))
        elif init_type == 4:
            # Random symmetric placement
            circles = np.zeros((N, 3))
            mid_x = w_val / 2
            placed = 0
            for _ in range(2000):
                if placed >= N:
                    break
                r = trial_rng.uniform(0.04, 0.16)
                cx = trial_rng.uniform(r, w_val/2)
                cy = trial_rng.uniform(r, h_val - r)
                ok_l = ok_r = True
                for k in range(placed):
                    d = np.hypot(circles[k, 0] - cx, circles[k, 1] - cy)
                    if d < r + circles[k, 2]:
                        ok_l = False
                    d2 = np.hypot(circles[k, 0] - (w_val - cx), circles[k, 1] - cy)
                    if d2 < r + circles[k, 2]:
                        ok_r = False
                if ok_l and ok_r and placed + 1 < N:
                    circles[placed] = [cx, cy, r]
                    placed += 1
                    circles[placed] = [w_val - cx, cy, r]
                    placed += 1
                elif ok_l:
                    circles[placed] = [cx, cy, r]
                    placed += 1
            if placed < N:
                circles = None
        elif init_type == 5:
            # Large-small mix: 5 large + 16 small
            circles = greedy_placement(trial_rng, w_val, h_val, r_range=(0.10, 0.20))
            if circles is not None:
                # Shrink the smaller ones
                radii_sorted = np.argsort(-circles[:, 2])
                for k in radii_sorted[5:]:
                    circles[k, 2] *= trial_rng.uniform(0.3, 0.7)
        elif init_type == 6:
            # Perturbed warmstart with different aspect ratio
            if warmstart_circles:
                ws = np.array(warmstart_circles[0], dtype=np.float64)
                circles = ws.copy()
                # Scale to different aspect ratio
                old_w = float(np.max(circles[:, 0] + circles[:, 2]) - np.min(circles[:, 0] - circles[:, 2]))
                old_h = float(np.max(circles[:, 1] + circles[:, 2]) - np.min(circles[:, 1] - circles[:, 2]))
                circles[:, 0] -= np.min(circles[:, 0] - circles[:, 2])
                circles[:, 1] -= np.min(circles[:, 1] - circles[:, 2])
                circles[:, 0] *= w_val / old_w
                circles[:, 1] *= h_val / old_h
                circles[:, 2] *= min(w_val/old_w, h_val/old_h)
                # Add noise
                circles[:, :2] += trial_rng.normal(0, 0.02, (N, 2))
                circles[:, 2] *= (1 + trial_rng.normal(0, 0.01, N))
                circles[:, 2] = np.maximum(circles[:, 2], 0.01)
        else:
            # Standard greedy
            circles = greedy_placement(trial_rng, w_val, h_val)

        if circles is None:
            results.append({"trial": trial, "status": "init_failed"})
            continue

        # Quick SA phase
        n_sa = 50000
        t_start = 0.02
        t_end = 1e-8
        curr = circles.copy()
        curr_w = w_val

        def penalty(c, ww):
            hh = 2.0 - ww
            s = float(np.sum(c[:, 2]))
            pen = 0.0
            for i in range(N):
                for j in range(i+1, N):
                    d = np.hypot(c[i,0]-c[j,0], c[i,1]-c[j,1])
                    gap = d - c[i,2] - c[j,2]
                    if gap < 0:
                        pen += gap**2 * 1e6
                cx, cy, r = c[i]
                if cx - r < 0: pen += (cx-r)**2 * 1e6
                if cx + r > ww: pen += (cx+r-ww)**2 * 1e6
                if cy - r < 0: pen += (cy-r)**2 * 1e6
                if cy + r > hh: pen += (cy+r-hh)**2 * 1e6
            return s - pen

        curr_val = penalty(curr, curr_w)
        best_sa = curr.copy()
        best_sa_val = curr_val
        best_sa_w = curr_w

        for step in range(n_sa):
            t = t_start * (t_end / t_start) ** (step / n_sa)
            trial_c = curr.copy()
            trial_w = curr_w

            move = trial_rng.integers(0, 5)
            if move <= 1:
                idx = trial_rng.integers(0, N)
                scale = max(0.01 * (t / t_start), 1e-7)
                trial_c[idx, 0] += trial_rng.normal(0, scale)
                trial_c[idx, 1] += trial_rng.normal(0, scale)
            elif move == 2:
                idx = trial_rng.integers(0, N)
                scale = max(0.005 * (t / t_start), 1e-8)
                trial_c[idx, 2] *= (1 + trial_rng.normal(0, scale))
                trial_c[idx, 2] = max(trial_c[idx, 2], 0.001)
            elif move == 3:
                i, j = trial_rng.choice(N, 2, replace=False)
                trial_c[i], trial_c[j] = trial_c[j].copy(), trial_c[i].copy()
            else:
                scale = max(0.005 * (t / t_start), 1e-8)
                trial_w += trial_rng.normal(0, scale)
                trial_w = np.clip(trial_w, 0.3, 1.7)

            trial_val = penalty(trial_c, trial_w)
            delta = trial_val - curr_val
            if delta > 0 or trial_rng.random() < np.exp(min(delta / max(t, 1e-15), 0)):
                curr = trial_c
                curr_w = trial_w
                curr_val = trial_val
                if curr_val > best_sa_val:
                    best_sa = curr.copy()
                    best_sa_val = curr_val
                    best_sa_w = curr_w

        # SLSQP polish
        result = polish_slsqp(best_sa, best_sa_w)
        if result is None:
            results.append({"trial": trial, "status": "polish_failed", "sa_score": best_sa_val})
            continue

        polished, w_pol, score = result
        is_novel = abs(score - KNOWN_BASIN_EXACT) > 1e-6 and score > 2.0
        is_better = score > KNOWN_BASIN_EXACT + 1e-10

        results.append({
            "trial": trial,
            "status": "ok",
            "score": score,
            "sa_score": best_sa_val,
            "novel": is_novel,
            "better": is_better,
        })

        if score > best_score:
            best_score = score
            best_circles = polished.tolist()
            best_w = w_pol

    return {
        "batch_id": batch_id,
        "best_score": best_score,
        "best_circles": best_circles,
        "best_w": best_w,
        "n_ok": sum(1 for r in results if r.get("status") == "ok"),
        "n_novel": sum(1 for r in results if r.get("novel")),
        "n_better": sum(1 for r in results if r.get("better")),
        "scores": [r.get("score", 0) for r in results if r.get("status") == "ok"],
    }


@app.local_entrypoint()
def main():
    results_dir = Path("results/problem-17-circles-rectangle")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Load warmstarts
    warmstart_circles = []
    for p in sorted(results_dir.glob("sota-*.json")):
        try:
            with open(p) as f:
                data = json.load(f)
            warmstart_circles.append(data["circles"])
        except Exception:
            pass

    print(f"Loaded {len(warmstart_circles)} warmstarts")
    print(f"Known basin exact: {KNOWN_BASIN_EXACT:.20f}")
    print(f"Arena #1:          {ARENA_BEST:.16f}")
    print()

    # Launch batches — 40 batches × 100 trials = 4000 total
    n_batches = 40
    trials_per = 100
    total = n_batches * trials_per

    print(f"Launching {n_batches} batches × {trials_per} trials = {total} total")
    t0 = time.time()

    futures = []
    for i in range(n_batches):
        f = run_batch.spawn(i, trials_per, warmstart_circles)
        futures.append(f)

    global_best = -float("inf")
    global_best_circles = None
    total_ok = 0
    total_novel = 0
    total_better = 0
    all_scores = []

    for i, f in enumerate(futures):
        res = f.get()
        total_ok += res["n_ok"]
        total_novel += res["n_novel"]
        total_better += res["n_better"]
        all_scores.extend(res["scores"])

        if res["best_score"] > global_best:
            global_best = res["best_score"]
            global_best_circles = res["best_circles"]

        elapsed = time.time() - t0
        print(f"  Batch {i+1:2d}/{n_batches}: best={res['best_score']:.13f}  "
              f"ok={res['n_ok']}  novel={res['n_novel']}  better={res['n_better']}  "
              f"[{elapsed:.0f}s]")

    print()
    print("=" * 60)
    print(f"TOTAL:         {total} trials")
    print(f"Valid polished: {total_ok}")
    print(f"Novel basins:   {total_novel}")
    print(f"Better than known: {total_better}")
    print(f"Global best:    {global_best:.16f}")
    print(f"Δ vs known:     {global_best - KNOWN_BASIN_EXACT:+.4e}")
    print(f"Δ vs arena #1:  {global_best - ARENA_BEST:+.4e}")
    print(f"Time:           {time.time() - t0:.0f}s")

    if all_scores:
        import numpy as np
        scores = np.array(all_scores)
        print(f"\nScore distribution:")
        print(f"  min:    {scores.min():.13f}")
        print(f"  median: {np.median(scores):.13f}")
        print(f"  max:    {scores.max():.13f}")
        print(f"  >2.365: {np.sum(scores > 2.365)}")
        print(f"  >2.3658: {np.sum(scores > 2.3658)}")

        # Count distinct basins (scores within 1e-6 of each other)
        sorted_s = np.sort(scores)[::-1]
        basins = [sorted_s[0]]
        for s in sorted_s[1:]:
            if all(abs(s - b) > 1e-6 for b in basins):
                basins.append(s)
        print(f"  Distinct basins (>1e-6 apart): {len(basins)}")
        for k, b in enumerate(basins[:10]):
            print(f"    basin {k+1}: {b:.13f}  Δknown={b-KNOWN_BASIN_EXACT:+.4e}")

    if global_best_circles is not None:
        out = results_dir / "gpu-basin-search-best.json"
        with open(out, "w") as f:
            json.dump({"circles": global_best_circles}, f, indent=2)
        print(f"\nSaved best to {out}")

        if global_best > KNOWN_BASIN_EXACT + 1e-6:
            print("\n*** NOVEL BASIN FOUND! ***")
