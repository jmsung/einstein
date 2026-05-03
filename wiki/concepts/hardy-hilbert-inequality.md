---
type: concept
author: agent
drafted: 2026-05-02
related_problems: [P2, P3, P4]
related_techniques: [larger-n-cascade.md, dinkelbach-fractional-programming.md, lp-cutting-plane-warmstart.md]
related_findings: [equioscillation-escape.md, optimizer-recipes.md]
related_personas: [hilbert.md, riemann.md, tao.md]
cites:
  - ../personas/hilbert.md
  - autocorrelation-inequality.md
  - sidon-sets.md
---

# Hardy–Hilbert inequality (and the autocorrelation family's functional-analytic spine)

## TL;DR

The **Hardy–Hilbert inequality** is the functional-analytic ground truth that bounds bilinear forms involving `1/(m+n)` kernels on sequences in `ℓ²`. For the einstein arena's autocorrelation family (P2/P3/P4), it's the *upstream* inequality — every sharper bound on `‖f ★ f‖` ratios eventually reduces to a Hardy–Hilbert-style integral inequality with a specific kernel choice. When stuck on autocorrelation problems, ask: *can the ratio be reformulated as a Hilbert-space inner product whose Hardy–Hilbert dual gives a cleaner bound?*

## What it is

The classical statement (sequence form):

> For non-negative real sequences `(a_m), (b_n) ∈ ℓ²` with `Σ a_m² < ∞`, `Σ b_n² < ∞`,
>
> ```
> Σ_{m,n ≥ 1}  (a_m · b_n) / (m + n)  ≤  π · √( Σ a_m² ) · √( Σ b_n² )
> ```
>
> with equality only in the limit (the constant `π` is sharp).

Continuous form (more relevant for the autocorrelation family):

> For non-negative `f, g ∈ L²(0, ∞)`,
>
> ```
> ∫∫_{(0,∞)²}  f(x) g(y) / (x + y)  dx dy  ≤  π · ‖f‖₂ · ‖g‖₂
> ```

The kernel `1/(x+y)` is called the **Hilbert kernel**. The inequality says: the integral operator `T_H f(y) = ∫ f(x)/(x+y) dx` has operator norm exactly `π` on `L²(0,∞)`.

The Schur test (a generalization of the same idea) gives Hardy–Hilbert as a special case and is the standard tool for *deriving* Hardy–Hilbert-style bounds for arbitrary positive kernels.

## When it applies

In the autocorrelation family:

- **P2 First Autocorrelation** (`min  max(f★f) / (∫f)²`) — the ratio is a bilinear-form-over-norm structure. Hardy–Hilbert with kernel `1/(x+y)` gives a *baseline* bound; tightening requires a sharper kernel (typically the Sidon-set autoconvolution kernel from Cloninger–Steinerberger 2017).
- **P3 Second Autocorrelation** (`max  ‖f★f‖₂² / (‖f★f‖₁ · ‖f★f‖∞)`) — Cauchy–Schwarz + Hardy–Hilbert gives a clean upper bound on `‖f★f‖∞` in terms of `‖f‖₂`; the ratio's denominator `‖f★f‖₁ = (∫f)²` is exact.
- **P4 Third Autocorrelation** (`min |max(f★f)| / (∫f)²` with f signed) — the signed-f case requires a *generalized* Hardy–Hilbert with a sign-aware kernel; this is where the larger-n escape technique ([larger-n-cascade.md](../techniques/larger-n-cascade.md)) helps the discrete optimizer find configurations that saturate the continuous bound.

Outside the autocorrelation family:

- **Sidon-set extremal bounds** ([sidon-sets.md](sidon-sets.md)) — the Vinuesa thesis derives Sidon-set existence bounds via Hardy–Hilbert on the indicator function's autoconvolution.
- **Spectral bounds on integral operators** — anywhere the operator has positive kernel, Hardy–Hilbert is a candidate ceiling.

## Why it works

The Hilbert kernel `K(x,y) = 1/(x+y)` is invariant under the dilation `(x,y) → (λx, λy)`. By the Mellin transform / Plancherel theorem, this dilation invariance turns the integral operator into a multiplication operator on the Mellin side, where `‖T_H‖ = π` falls out from `Γ(s) Γ(1-s)`-type identities. The Schur test makes this concrete: pick a positive function `φ` with `T_H φ ≤ A φ`; if `T_{H,*} φ⁻¹ ≤ A φ⁻¹` too, then `‖T_H‖ ≤ A`. For Hardy–Hilbert with `φ(x) = 1/√x`, this gives the sharp constant `π`.

This is the same machinery Cohn–Elkies use for sphere-packing LP bounds (different kernel, same Schur-test structure) and the same machinery Tao uses in his blog when reformulating uncertainty principles as positive-operator bounds.

## Classic examples

1. **The original 1925 Hardy–Hilbert inequality** (Hilbert 1906 lectures, written up by Hardy 1925). The constant `π` is sharp; equality only in the limit.
2. **Schur test (Schur 1911)** — generalizes Hardy–Hilbert: any positive integral operator with a "test function" obeying the dual conditions has operator norm bounded by the test constant. Workhorse for deriving sharp bounds on autoconvolution.
3. **Continuous autoconvolution bounds (Cloninger–Steinerberger 2017)** ([source/papers/2017-cloninger-autoconvolution-sidon.md](../../source/papers/2017-cloninger-autoconvolution-sidon.md)) — improved Hardy–Hilbert-like bound for the autoconvolution-supremum problem; the LP relaxation we use for P2/P3 is essentially a discretization of this.
4. **Matolcsi–Vinuesa (2010)** ([source/papers/2010-matolcsi-autoconvolution.md](../../source/papers/2010-matolcsi-autoconvolution.md)) — disproof of the Schinzel–Schmidt symmetry conjecture via an explicit asymmetric `f` that nearly saturates a Hardy–Hilbert-style bound.

## Related to / distinguished from

- **[autocorrelation-inequality](autocorrelation-inequality.md)** — the *family* of arena problems. Hardy–Hilbert is the *backbone tool*; autocorrelation-inequality is the *target*.
- **[sidon-sets](sidon-sets.md)** — Hardy–Hilbert is one tool in the Sidon-set toolkit (specifically for B₂[g] cardinality bounds via autoconvolution).
- **[lp-duality](lp-duality.md)** — discretized Hardy–Hilbert becomes an LP; the LP dual gives a *certificate* of the bound. The bridge from Hardy–Hilbert to the arena's discrete optimizer goes through LP duality.
- **Cauchy–Schwarz** — strictly weaker; gives `(∫fg)² ≤ ‖f‖₂² · ‖g‖₂²` regardless of kernel. Hardy–Hilbert is sharper because it incorporates the kernel `1/(x+y)`.
- **Schur test** — strictly more general; specializes to Hardy–Hilbert under the right test-function choice.

## How the agent should use it

When the council dispatch returns an autocorrelation-family problem (P2/P3/P4):

1. **Hilbert persona** ([personas/hilbert.md](../personas/hilbert.md)) explicitly asks: *"can the ratio be reformulated as a Hilbert-space inner product? Does Hardy–Hilbert (or Schur test) give a baseline bound? Can the kernel be sharpened to a Sidon-set kernel?"* — that's the entry point.
2. Pair with **Tao persona** for the harmonic-analysis side: Fourier-dual formulation often reveals when Hardy–Hilbert is tight and when it isn't.
3. **Riemann persona** for the spectral side: Hardy–Hilbert's `π` constant comes from the operator's spectrum on `ℓ²` / `L²`; equioscillation in the primal is dual to spectral saturation in the Mellin side.
4. The **larger-n cascade technique** ([techniques/larger-n-cascade.md](../techniques/larger-n-cascade.md)) is empirically the way to get the discrete optimizer to saturate the Hardy–Hilbert continuous bound — discretization at small n misses the saturating extremizer.

## Limits

- **Hardy–Hilbert is a specific kernel** — not every autocorrelation problem has a `1/(x+y)`-style kernel structure. P3 (the autoconvolution-norm ratio) involves a more complex operator; Hardy–Hilbert provides a baseline but the sharp constant requires Sidon-set/B_h[g] machinery (Vinuesa).
- **Sharp constant `π` is asymptotic** — equality only in the limit; finite-n discrete bounds are strictly looser. The arena's score = ratio at finite n; Hardy–Hilbert tells you the asymptotic ceiling, not the achievable score at fixed n.
- **Doesn't directly handle signed `f`** — P4's signed-f case requires a generalized Hardy–Hilbert with sign accounting; not a plug-in.

## See also

- [`personas/hilbert.md`](../personas/hilbert.md) — the persona that reaches for Hardy–Hilbert
- [`concepts/autocorrelation-inequality.md`](autocorrelation-inequality.md) — target problem family
- [`source/papers/2017-cloninger-autoconvolution-sidon.md`](../../source/papers/2017-cloninger-autoconvolution-sidon.md) — sharper kernels for autoconvolution
- [`source/papers/2010-matolcsi-autoconvolution.md`](../../source/papers/2010-matolcsi-autoconvolution.md) — explicit Hardy–Hilbert-saturating extremizer
- [`source/papers/2010-vinuesa-sidon-thesis.md`](../../source/papers/2010-vinuesa-sidon-thesis.md) — B_h[g] machinery built on Hardy–Hilbert
