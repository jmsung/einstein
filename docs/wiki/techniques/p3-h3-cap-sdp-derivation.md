---
type: technique
author: agent
drafted: 2026-05-02
status: draft-skeleton
related_problems: [P3]
related_concepts: [autocorrelation-inequality.md, lp-duality.md]
related_findings: [p3-closed-form-baseline-landscape.md, dead-end-p3-jaech-cascade-extended.md]
cites:
  - ../../source/papers/2026-rechnitzer-autoconvolution-digits.md
  - ../../source/papers/2017-cloninger-autoconvolution-sidon.md
  - ../../source/papers/2010-matolcsi-autoconvolution.md
---

# H3-cap derivation: rigorous upper bound for the arena P3 quantity via Fourier + SOS-SDP

Skeleton for the H3-cap path identified in [`findings/p3-closed-form-baseline-landscape.md`](../findings/p3-closed-form-baseline-landscape.md). This is a *derivation document*, not a working solver. Companion code skeleton at `scripts/autocorrelation/h3_cap_sdp_skeleton.py`.

## Problem statement

Compute (or bound from above) the constant
$$S^* = \sup_{\substack{f \geq 0 \\ \mathrm{supp}\,f \subseteq [-1/2, 1/2] \\ \int f = 1}} \frac{\|f*f\|_2^2}{\|f*f\|_\infty}$$
which is the supremum of the Einstein Arena P3 score $S(f) = \|f*f\|_2^2 / (\|f*f\|_1 \cdot \|f*f\|_\infty)$ over feasible $f$ (the $\|f*f\|_1 = 1$ normalization comes from $\int f = 1$).

**Trivial bound** (Cauchy–Schwarz on non-negative $f*f$): $S^* \leq 1$.

**Empirical lower bound** (arena leaders): $S^* \geq 0.96272$.

**Goal**: a rigorous numerical upper bound $S^* \leq 0.96272 + \epsilon$ for some $\epsilon > 0$, ideally close to $0.0001$ (the arena's minImprovement gate).

## Derivation

### Step 1 — Fourier reformulation (White, via Rechnitzer 2026 §2)

WLOG assume $f$ is even (Lemma 3.1 of White [28] in Rechnitzer; the unique extremal is even). Define $F$ on $(-1, 1)$ by
$$F(x) = \begin{cases} f(x) & x \in (-1/2, 1/2) \\ 0 & \text{otherwise} \end{cases}$$
and its Fourier series on the period-2 torus:
$$\hat{F}(k) = \frac{1}{2} \int_{-1}^1 e^{-i\pi k x} F(x)\, dx, \qquad k \in \mathbb{Z}.$$

By White's identity (Rechnitzer eq. 8):
$$\|F * F\|_2^2 = 8 \sum_k |\hat{F}(k)|^4 = \frac{1}{2} \sum_k |\hat{f}(k)|^4 + \frac{8}{\pi^4} \sum_m \left| \sum_k \frac{(-1)^k \hat{f}(k)}{2k - (2m+1)} \right|^4.$$

**Truncate** at $|k| \leq T$, $|m| \leq T$. The truncated sum is a quartic polynomial $Q_T(\hat{\mathbf{f}})$ in the truncated coefficient vector $\hat{\mathbf{f}} = (\hat{f}(0), \hat{f}(1), \ldots, \hat{f}(T))$.

The truncation error has a known bound (Rechnitzer §3-4 derives it explicitly via Levin transform on the tail).

### Step 2 — Express the constraints as SDP feasibility

Three constraints on $f$:

1. **Normalization** $\int f = 1$: equivalent to $\hat{f}(0) = 1$.

2. **Non-negativity** $f \geq 0$ on $(-1/2, 1/2)$: by the Bochner–Herglotz theorem (or the trigonometric-moment-problem duality), this is equivalent to the Toeplitz matrix $\mathbf{T}(\hat{\mathbf{f}}) := [\hat{f}(i - j)]_{0 \leq i, j \leq T} \succeq 0$.

3. **Sup-norm bound** $\|f*f\|_\infty \leq C$: equivalent to the trigonometric polynomial
   $$P_C(x) := C - (f*f)(x) = C - 2\sum_k \hat{F}(k)^2 \cos(\pi k x) \geq 0 \quad \text{on}\ [-1, 1].$$
   By the Putinar Positivstellensatz (or standard SOS for trig polynomials on an interval), $P_C \geq 0$ on $[-1, 1]$ iff there exist polynomials $\sigma_0, \sigma_1$ that are SOS such that $P_C(x) = \sigma_0(x) + (1 - x^2)\sigma_1(x)$.
   For trig polynomials of degree $2T$, this becomes a Hankel/Toeplitz semidefinite constraint of size $T+1$.

### Step 3 — Pose the SDP

The supremum problem becomes:
$$\inf_{C, \hat{\mathbf{f}}} \ C$$
$$\text{s.t.} \quad \hat{f}(0) = 1, \quad \mathbf{T}(\hat{\mathbf{f}}) \succeq 0, \quad P_C \in \mathrm{SOS}, \quad Q_T(\hat{\mathbf{f}}) \geq M_0,$$
where $M_0$ is a chosen lower bound on $\|f*f\|_2^2$. Then $S^* \leq M_0 / C^*$ for any feasible solution.

To **maximize** $S = M / C$, sweep $M_0$ over a grid (or use a parametric SDP / Dinkelbach iteration in $\lambda = M / C$).

### Step 4 — Numerical solve at modest truncation

- $T \in \{16, 32, 64, 128\}$. Rechnitzer used $T = N = 4096$ at $P = 32$ ansatz parameters with mpmath at 1024 dps for his minimization. For our maximization, $T = 64$ is a reasonable first attempt — gives an SDP of size ~$200 \times 200$, solvable by MOSEK in seconds.
- Solve via CVXPY + MOSEK (or SCS for free), returning a numerical upper bound on $C^*$ for each $M_0$.
- Take $S^* \leq \sup_{M_0} M_0 / C^*(M_0)$.
- The truncation error gives a verified outer bound: $S^* \leq \sup_{M_0} M_0 / (C^*(M_0) - \epsilon_T)$ where $\epsilon_T$ is bounded by Rechnitzer-style Levin-acceleration tail bounds.

### Step 5 — Interval-arithmetic certification

For a *certified* (provable) upper bound rather than a numerical one, repeat Step 4 with mpmath at high dps (200+) and propagate intervals through the SDP solver's witness. Rechnitzer §5 has the exact recipe.

## Expected effort

| Step | Effort | Risk |
|---|---|---|
| 1: Fourier reformulation, truncation error | half day (re-derive White's identity carefully) | low — paper is clear |
| 2: SOS-SDP setup | half day (CVXPY + Toeplitz/Hankel constraints) | low |
| 3: Parameter sweep loop | quarter day | low |
| 4: First numerical solve at $T = 64$ | quarter day | medium — convergence + scaling |
| 5: mpmath certification | full day | high — interval arithmetic in SDP is non-trivial |

Total: ~1–3 days for a working numerical solver, +1 day for certified intervals.

## Expected outcome

Per the [closed-form baseline finding](../findings/p3-closed-form-baseline-landscape.md), the empirical ceiling 0.96272 is 0.04 below the trivial Cauchy–Schwarz UB. A first-pass SDP at $T = 64$ might give a numerical UB in the range $0.97$–$0.99$ — clearly above the empirical 0.96272 but well below 1.0. Whether this *closes* the gap to the arena gate (0.9627433) depends on how tight the SDP is at $T = 64$; tightening typically requires increasing $T$ and re-solving.

If the SDP UB at $T = 64$ comes in around $0.965$, then $S^* \leq 0.965$ would be a real, decisive result: the arena leaders are within $1e-3$ of the math ceiling. Strategy.md's "this problem is solved to its practical limit" verdict would then have a *quantitative* certificate.

If the SDP UB comes in around $0.99$, the math ceiling is genuinely higher than the empirical 0.96272, and the arena leaders are leaving headroom on the table.

Either result is wisdom-worthy.

## Empirical lessons from numerical attempts (2026-05-02)

Three implementation attempts under `scripts/autocorrelation/`, each documenting where the relaxation fails:

### v1 — `h3_cap_sdp.py`: SOC lifts in both quartic levels, no cross-term

- Setup: $y_k \geq \hat{f}_k^2$, $z_k \geq y_k^2$, $w_m \geq u_m^2$, $v_m \geq w_m^2$. Dense-grid sup-norm.
- Result: **unbounded** at every $\lambda$. The one-sided SOC lifts give the SDP unbounded freedom in the lifted variables ($z_k$ can be arbitrarily large given $y_k$); maximization runs to infinity.
- Diagnosis: convex maximization of $\hat{f}_k^4$ is non-DCP; SOC lifting alone can't tame it.

### v2 — `h3_cap_sdp_v2.py`: drops the SOC z-lift, drops the cross-term, simplifies

- Setup: $y_k \geq \hat{f}_k^2$ only; $M_{up} = \sum y_k$ (diagonal-only); dense-grid sup-norm.
- Result: **finite at S\* ≤ 1.0** (matches Cauchy–Schwarz trivial bound). At $\lambda = 1.0$, $g(\lambda) \approx 0$; at $\lambda = 1.1$, $g(\lambda) < 0$.
- Diagnosis: dropping the cross-term makes the relaxation *too coarse* to distinguish concentrated vs spread basins. The SDP finds $f$ achieving $M_{up}/C = 1$ at the trivial corner.

### v3 — `h3_cap_sdp_v3.py`: cross-term added as a constant majorant

- Setup: same as v2 + $(8/\pi^4) \sum_m H_m^4$ added to $M_{up}$ where $H_m = \sum_k |L_{m,k}|$ (constant upper bound from $|\hat{f}_k| \leq 1$).
- Result: **finite, but at $S^* \leq 83$** (T=8, M=8) — much worse than trivial.
- Diagnosis: the constant majorant adds +82 of slack to $M_{up}$ regardless of $\hat{f}$, breaking the relationship between $M$ and $C$. Loose upper bounds in the wrong direction destroy the bound.

### v4 — `h3_cap_sdp_v4.py`: Toeplitz-Carathéodory sup-norm SOS, no cross-term

Critical realization: working in $\hat{F}$ (Fourier on torus) instead of $\hat{f}$ (continuous FT on $\mathbb{R}$) **eliminates the cross-term entirely**. The cross-term in Rechnitzer eq. 8 only appears under the change-of-variables $\hat{F}(k) = (1/2)\hat{f}(k/2)$.

- Setup: variables $\hat{F}_k$ for $k = 0, \ldots, T$ with $\hat{F}_0 = 1/2$. Toeplitz PSD on $\hat{F}$ enforces $F \geq 0$. SOC lift $y_k \geq \hat{F}_k^2$. Bound $\hat{F}_k^4 \leq y_k / 4$ (using $|\hat{F}_k| \leq 1/2$). Sup-norm via Toeplitz-Carathéodory PSD certificate $Q$ with diagonal-trace constraints matching the coefficients of $C - 2y_0 - 4 \sum y_k \cos(\pi k x)$.
- Result: **$S^* \leq 1.000$ at T=4, 8, 16** — trivial Cauchy-Schwarz bound, identical to v2 in tightness.
- Diagnosis: the relaxation $\hat{F}_k^4 \leq y_k / 4$ is the bottleneck. The SDP balances large $y_k$ (which inflates $M^{up}$) against tight $C$ (which Toeplitz-Carathéodory SOS forces from the same $y_k$). At the optimum, both saturate at $M^{up} = C$, giving $S^{up} = 1$ exactly.

### v5 — Lasserre level-2 SDP (`h3_cap_lasserre.py`)

The standard tool for tightening below trivial in convex-quartic maximization. Implementation:
- Decision variables: moments $y_\alpha$ for $|\alpha| \leq 4$ (number: $\binom{n+4}{4}$)
- Lasserre PSD: moment matrix $M_2 = [y_{\alpha+\beta}]_{|\alpha|,|\beta| \leq 2}$ size $\binom{n+2}{2}$ ⪰ 0
- $F \geq 0$ via Fejér-Riesz / Toeplitz-Carathéodory: ∃ PSD $G_F$ with diagonal-trace constraints matching $y_{e_k}$
- Sup-norm via Toeplitz-Carathéodory on $C - (F*F)$
- Explicit moment bounds: $|y_\alpha| \leq (1/2)^{|\alpha|}$
- Solved with CLARABEL (interior-point, more accurate than SCS for SDP)

At T=4 (n=5, moment matrix 21×21, 126 moments): **$g(\lambda)$ tracks the constant $4.5 - \lambda \cdot 0.5$ across $\lambda$, never crossing 0 in $[0.5, 1.5]$**. The SDP returns $M = 4.5$, $C = 0.5$, $S^{up} = 9$ — this is a *consistent* SDP feasible point (not a solver bug; CLARABEL and SCS agree) but it represents an *unphysical* slack in the moment matrix.

Diagnosis: the Lasserre L2 moment-matrix PSD enforces $y_{2e_k} \geq y_{e_k}^2$ via the Schur complement on the (1, $e_k$) submatrix, AND $y_{4e_k} \geq y_{2e_k}^2$ via the ($e_k$, $2e_k$) submatrix. But the explicit upper bound $|y_\alpha| \leq (1/2)^{|\alpha|}$ allows $y_{4e_k}$ at its upper bound $1/16$ regardless of $\hat{F}_k = y_{e_k}$. The Lasserre relaxation does not couple $y_{4e_k}$ to $\hat{F}_k$ tightly enough at level 2; the *fourth-moment slack* is what makes $S^{up} = 9$.

Tightening to break trivial requires:
- **Lasserre level $\geq 3$**: moment matrix size $\binom{n+3}{3} = 56$ at T=4 (still tractable), $220$ at T=8. Captures additional algebraic relations between fourth and second moments through degree-6 monomials.
- **OR Putinar localizing matrices for the Toeplitz-Carathéodory constraints**: enforce that the moment sequence $(y_\alpha)$ comes from a valid measure consistent with the $F \geq 0$ polynomial description, not just the matrix inequality. This requires working out the polynomial certificates carefully.

### Final verdict

**All five standard relaxations of the H3-cap SDP — including Lasserre level-2 — fail to produce a useful upper bound.** v1-v4 saturate at trivial 1.0; v5 (Lasserre L2) gives a consistent-but-unphysical $S^{up} = 9$ due to insufficient moment-matrix coupling at level 2. The fundamental obstruction is the convex maximization of the quartic $\sum \hat{F}_k^4$ combined with the discrete nature of the autoconvolution structure. Standard SDP relaxation tools (SOC lifts, Toeplitz-Carathéodory, Lasserre level-2) cannot tighten this without:

- (a) **Lasserre hierarchy at level ≥ 3**: at L3, moment matrix size grows to $\binom{n+3}{3}$ — $56$ at T=4, $220$ at T=8, $1140$ at T=16. The L3 PSD captures algebraic relations between fourth-moments and second-moments via degree-6 monomials, which L2 misses. CVXPY/CLARABEL can handle T=4-8 at L3; T=16 may need MOSEK or custom IPM. Multi-day implementation effort, but the relaxation gap is expected to close significantly.
- (b) **Putinar SOS localizing matrices for Toeplitz-Carathéodory**: rather than enforcing $F \geq 0$ as a separate matrix-PSD constraint, enforce it via Putinar Positivstellensatz on the moment sequence directly. This requires working out the polynomial certificates carefully — research-level Fourier analysis, may parallel the Cohn-Elkies dual.
- (c) **Custom Cohn-Elkies-style dual**: find a function $\phi$ such that $\int \phi(x) (f*f)(x)^2 dx \leq C^*  \cdot \int \phi(x) (f*f)(x) dx$ for all valid $f$. Coefficient matching gives constraints on $\phi$ via Fourier-positivity. Research math; multi-day.

The five scripts together delineate exactly where the difficulty lies — useful as a starting scaffold but not a path to a non-trivial bound within session-scale work. **Lasserre level 3 at T=4 is the cheapest concrete next step (single-day implementation), Putinar/Cohn-Elkies dual is the most decisive (multi-day research).**

### Conclusion

To produce a tightening below the trivial 1.0, the cross-term must be represented with **both**:
- (a) a lower-bound coupling $w_m \geq u_m^2$ (SOC lift, easy)
- (b) an *upper-bound coupling* of $w_m$ to the structure of $u_m$, such that the SDP cannot inflate $w_m$ at will

The standard way to enforce (b) for trigonometric polynomials is the **Hankel/Toeplitz SOS positivity** parameterization — represent the polynomial whose coefficients depend on $w_m$ as PSD-via-Toeplitz, with diagonal-trace equalities tying the coefficients back to $\hat{f}_k$. This is the multi-day research piece.

Alternatively, the **Lasserre hierarchy on moments of $f$** sidesteps the convex-maximization issue by working with the moment matrix of $f$ as the variable, with the Hausdorff-moment PSD constraint and the autoconvolution-as-moment-product structure. Standard but still 2-3 days of careful coding.

The three attempts are saved as the starting point for a future session. Each demonstrates a distinct failure mode of the natural simplification path.

## Dual formulation sketch (Cohn–Elkies-style)

A genuinely different approach to the H3 cap, not via primal moment SDP but via a **Fourier-positive dual certificate**. Sketched here as a starting point for a future research session.

### Setup

We want $S^* = \sup_f \frac{\int (f*f)^2}{\int (f*f) \cdot \|f*f\|_\infty}$ for $f \geq 0$, $\int f = 1$, $\mathrm{supp}\,f \subseteq [-1/2, 1/2]$.

Denote $g = f*f$. Then $g \geq 0$, $\int g = 1$, $\mathrm{supp}\,g \subseteq [-1, 1]$, $\hat{g}(\xi) = \hat{f}(\xi)^2 \geq 0$ (Bochner).

The Cohn–Elkies idea: find a function $\phi: [-1, 1] \to \mathbb{R}$ with three properties:

1. $\phi(x) \leq c$ for all $x \in [-1, 1]$ (where $c$ is the candidate upper bound for $S^*$),
2. $\hat{\phi}(\xi) \geq 0$ for all $\xi \in \mathbb{R}$ (Fourier-positive),
3. $\phi(0) \geq c$ (or some suitable normalization condition that ties $\phi(0)$ to $c$).

If such a $\phi$ exists, then for any valid $g = f*f$:
$$\int g(x)^2 dx = \int g(x) \cdot g(x) dx \stackrel{?}{\leq} \phi(0) \cdot \|g\|_1 \cdot \|g\|_\infty / c$$
giving $S(f) = \int g^2 / (\|g\|_1 \|g\|_\infty) \leq \phi(0) / c$, and a suitable choice of $\phi$ would give $\phi(0) / c = c$ for a self-consistent bound.

The exact bookkeeping requires care — the inner product $\int g \phi g$ relates via Parseval to $\sum \hat{g}_k \hat{\phi}_k \overline{\hat{g}_k}$, and the Fourier-positivity of $\hat{\phi}$ combined with $\hat{g} \geq 0$ ensures the inequality direction.

### Cohn–Elkies for our setting

The classical Cohn-Elkies bound is for sphere-packing density. The autoconvolution P3 is structurally similar but with a different objective. The adaptation needs:

1. Identify the *correct positivity dual* — what Fourier positivity certificate produces an upper bound on $\int g^2 / \|g\|_\infty$ for $g$ a valid autoconvolution?
2. Derive coefficient-matching conditions via Parseval.
3. Solve the resulting LP/SDP for the optimal $\phi$.

This is non-trivial mathematics — the CE framework needed extension by Viazovska & coauthors for $d = 8, 24$ via modular forms, and the autoconvolution dual is structurally distinct from the kissing/packing dual. Likely **2-4 days of research-level work** to set up properly, longer to solve to high precision.

### Why this is the right path long-term

The Cohn-Elkies dual approach has produced the only known *tight* bounds on related extremal problems (sphere packing in $d = 8, 24$; kissing numbers via Levenshtein at certain $d$). For autoconvolution-related problems, the relevant dual machinery is partially developed in:

- Cohn–Goncalves, "An optimal uncertainty principle in twelve dimensions via modular forms" (2018)
- Cohn–Li, "Most tightly the kissing number falls" (2024)

The exact recipe for our $S(f) = \int g^2 / \|g\|_\infty$ ratio is, to our knowledge, not yet published. A careful derivation here would be a publishable wisdom artifact in its own right.

## Pitfalls and notes

- The `(2k - (2m+1))` denominator in Rechnitzer's eq. 8 has poles when $2k = 2m+1$ — handle the $k = m + 1/2$ case carefully in the truncation.
- The non-negativity Toeplitz constraint is on the *trigonometric* moments $\hat{f}(k)$, not on raw values — easy to mis-implement.
- The arena evaluator uses Simpson's rule on a discretized grid, not the exact $\|f*f\|_2^2$. The SDP bounds the *exact* quantity; relate to the arena's discrete quantity via a separate discretization-error bound (negligible at $n = 100\text{k}$+).
- For the maximization $S = M/C$, the parametric SDP (sweep $M_0$) is the simplest approach. A unified Dinkelbach formulation $\sup (M - \lambda C)$ over $\lambda$ would also work and may be more efficient.

## Related

- The Cohn–Elkies framework for sphere packing density is the *same shape* of derivation (Fourier + SOS-positivity + dual). See `concepts/cohn-elkies-bound.md`.
- For P2 (First Autocorrelation Inequality, $\sup \|f*f\|_\infty$ for unit-mass $f$), Rechnitzer's published methodology applies almost directly — White already reformulated $\|f*f\|_\infty$ as a quadratic-constrained LP (per Rechnitzer §2). P2 may be the easier first target before tackling P3's $L^2/L^\infty$ ratio.
- See `findings/p3-closed-form-baseline-landscape.md` for the empirical landscape that motivates this derivation.
