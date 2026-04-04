"""Sensitivity analysis: compute per-root gradients and find steepest descent direction."""
import sys
sys.path.insert(0, "src")
import numpy as np
from einstein.uncertainty.fast import fast_evaluate

BEST_ROOTS = [
    3.0886658942606733, 4.435156861236376, 6.034127890108831,
    30.945538933257353, 36.84167838791129, 42.20424571337132,
    47.682624801878234, 51.92315504790176, 57.58188043903107,
    100.7501292924569, 115.43881608340484, 123.02406833559513,
    140.04812478845042,
]

def compute_gradient(roots, h=1e-6):
    """Compute numerical gradient dS/dzi via central finite differences."""
    base = fast_evaluate(roots)
    grad = np.zeros(len(roots))
    for i in range(len(roots)):
        r_plus = list(roots)
        r_minus = list(roots)
        r_plus[i] += h
        r_minus[i] -= h
        s_plus = fast_evaluate(r_plus)
        s_minus = fast_evaluate(r_minus)
        grad[i] = (s_plus - s_minus) / (2 * h)
    return grad, base

def main():
    print("="*60)
    print("Sensitivity Analysis for Uncertainty Principle (k=13)")
    print("="*60)
    
    base_score = fast_evaluate(BEST_ROOTS)
    print(f"\nBase score: {base_score:.16f}")
    print(f"Target:     0.318221 (RhizomeAgent)")
    print(f"Gap:        {base_score - 0.318221:.10f}")
    
    # 1. Per-root gradient at multiple scales
    print("\n--- Per-root gradients ---")
    for h in [1e-4, 1e-6, 1e-8]:
        grad, _ = compute_gradient(BEST_ROOTS, h=h)
        print(f"\nh={h:.0e}:")
        for i, (r, g) in enumerate(zip(BEST_ROOTS, grad)):
            cluster = "near" if r < 10 else ("mid" if r < 80 else "far")
            print(f"  z[{i:2d}] = {r:10.4f} ({cluster:4s}): dS/dz = {g:+.8e}")
        print(f"  |grad| = {np.linalg.norm(grad):.8e}")
        
        # Steepest descent direction
        if np.linalg.norm(grad) > 0:
            direction = -grad / np.linalg.norm(grad)
            print(f"  Steepest descent direction (unit):")
            for i, d in enumerate(direction):
                if abs(d) > 0.1:
                    print(f"    z[{i:2d}]: {d:+.4f}")
    
    # 2. Try gradient descent with small step
    print("\n--- Gradient descent test ---")
    grad, base = compute_gradient(BEST_ROOTS, h=1e-6)
    for step_size in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0]:
        trial = [r - step_size * g for r, g in zip(BEST_ROOTS, grad)]
        trial.sort()
        if any(z <= 0 or z > 300 for z in trial):
            continue
        score = fast_evaluate(trial)
        delta = score - base
        marker = " ***IMPROVEMENT***" if delta < -1e-10 else ""
        print(f"  step={step_size:.3f}: S={score:.16f} (Δ={delta:+.2e}){marker}")
    
    # 3. Try perturbing individual roots
    print("\n--- Per-root perturbation search ---")
    for i in range(len(BEST_ROOTS)):
        best_delta = 0
        best_offset = 0
        for offset in np.linspace(-2.0, 2.0, 401):
            trial = list(BEST_ROOTS)
            trial[i] += offset
            if trial[i] <= 0 or trial[i] > 300:
                continue
            # Check sorted order
            sorted_trial = sorted(trial)
            if sorted_trial != trial and any(sorted_trial[j+1] - sorted_trial[j] < 0.01 for j in range(len(sorted_trial)-1)):
                continue
            score = fast_evaluate(sorted_trial)
            delta = score - base_score
            if delta < best_delta:
                best_delta = delta
                best_offset = offset
        cluster = "near" if BEST_ROOTS[i] < 10 else ("mid" if BEST_ROOTS[i] < 80 else "far")
        if best_delta < -1e-10:
            print(f"  z[{i:2d}]={BEST_ROOTS[i]:10.4f} ({cluster:4s}): best offset={best_offset:+.4f}, Δ={best_delta:+.2e} ***")
        else:
            print(f"  z[{i:2d}]={BEST_ROOTS[i]:10.4f} ({cluster:4s}): no improvement found")

    # 4. Try k=14 with extra root at various positions
    print("\n--- k=14: add 14th root ---")
    for pos in [1.0, 2.0, 8.0, 15.0, 20.0, 25.0, 65.0, 70.0, 80.0, 90.0, 150.0, 160.0, 180.0, 200.0, 250.0]:
        trial = sorted(BEST_ROOTS + [pos])
        if any(trial[j+1] - trial[j] < 0.01 for j in range(len(trial)-1)):
            continue
        score = fast_evaluate(trial)
        delta = score - base_score
        marker = " ***" if delta < -1e-6 else ""
        print(f"  14th root at {pos:6.1f}: S={score:.10f} (Δ={delta:+.2e}){marker}")

if __name__ == "__main__":
    main()
