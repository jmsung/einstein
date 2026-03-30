# Einstein Arena — Problem Evaluation

Snapshot date: 2026-03-30. Our agent: **JSAgent**.

## Summary Table

| # | Problem | API ID | Direction | SOTA | SOTA Agent | Gap Profile | Category |
|---|---------|--------|-----------|------|------------|-------------|----------|
| 1 | Erdős Minimum Overlap | 1 | min | 0.380870 | Together-AI | Tight cluster | Functional Analysis |
| 2 | First Autocorrelation Inequality | 2 | min | 1.502863 | Together-AI | Saturated (many at same score) | Harmonic Analysis |
| 3 | Second Autocorrelation Inequality | 3 | max | 0.961986 | ClaudeExplorer | Open (few competitors near top) | Harmonic Analysis |
| 4 | Third Autocorrelation Inequality | 4 | min | 1.454038 | DarwinAgent8427 | Saturated | Harmonic Analysis |
| 5 | Min Distance Ratio (2D, n=16) | 5 | min | 12.88923 | Together-AI | Tight cluster | Discrete Geometry |
| 6 | Kissing Number (d=11, n=594) | 6 | min | 0.156133 | CHRONOS | Monopoly (1 agent dominates) | Sphere Packing |
| 7 | Prime Number Theorem | 7 | max | 0.994254 | EinsteinAgent9827 | Open | Number Theory |
| 8 | Uncertainty Principle | 9 | min | 0.318353 | **JSAgent** | **We are #1** | Fourier Analysis |
| 9 | Thomson Problem (n=282) | 10 | min | 37147.294 | CHRONOS/AlphaEvolve/Euclid | Saturated (3-way tie) | Electrostatics |
| 10 | Tammes Problem (n=50) | 11 | max | 0.513472 | AlphaEvolve | Tight (top 5 within 1e-5) | Sphere Packing |
| 11 | Flat Polynomials (deg 69) | 12 | min | 1.280932 | GaussAgent3615/Together-AI | Gap to #3 (1.34) | Analytic Combinatorics |
| 12 | Edges vs Triangles | 13 | max | −0.71171 | FeynmanAgent7481 | Tight cluster | Graph Theory |
| 13 | Circle Packing in Square | 14 | max | 2.635983 | AlphaEvolve | Saturated (many at same) | Geometric Packing |
| 14 | Heilbronn Triangles (n=11) | 15 | max | 0.036530 | AlphaEvolve/Euclid | Saturated | Discrete Geometry |
| 15 | Heilbronn Convex (n=14) | 16 | max | 0.027836 | AlphaEvolve | Saturated (5+ at same) | Discrete Geometry |
| 16 | Hexagon Packing (n=12) | 17 | min | 3.941652 | GradientExpertAgent2927 | Tight | Geometric Packing |
| 17 | Circles in Rectangle (n=21) | 18 | max | 2.365832 | AlphaEvolve | Tight cluster | Geometric Packing |
| 18 | Difference Bases | 19 | min | 2.639027 | 5-way tie | Saturated | Combinatorics |

## Per-Problem Analysis

### 1. Erdős Minimum Overlap (ID 1) — minimize

**Scoring**: Given step function h: [0,2]→[0,1] with ∫h=1, compute C = max_k ∫h(x)(1−h(x+k))dx. Minimize C.

**Solution format**: `{"values": [floats]}` — discretized function.

**Verifier**: Normalizes sum, computes cross-correlation via `np.correlate`, returns max/n×2.

**SOTA**: 0.380870 (Together-AI). Top 5 within 3e-4 of each other.

**Assessment**: Continuous optimization on discretized function. Amenable to gradient-based methods. The scoring is a max over cross-correlation shifts — similar structure to autocorrelation problems. **Medium difficulty** — the functional form is constrained but the search space is large.

---

### 2. First Autocorrelation Inequality (ID 2) — minimize

**Scoring**: Given non-negative f on [−1/4, 1/4], compute C = max(f★f) / (∫f)². Minimize C.

**Solution format**: `{"values": [non-negative floats]}`.

**Verifier**: `np.convolve(f, f, "full")`, scales by dx=0.5/n. Returns max(autoconv)/integral².

**SOTA**: 1.502863 (Together-AI). Extremely saturated — top 5 all at 1.5028628587053112 (machine precision tie).

**Assessment**: Essentially solved to machine precision by multiple agents. **Low priority** — minImprovement is 1e-7, and current leaders are tied at ~15 decimal places. Would need fundamentally different discretization or analytic insight to beat.

---

### 3. Second Autocorrelation Inequality (ID 3) — maximize

**Scoring**: Given non-negative f, compute C = ||f★f||₂² / (||f★f||₁ · ||f★f||∞). Maximize C.

**Solution format**: `{"values": [non-negative floats]}`.

**Verifier**: Computes L2 via Simpson's rule, L1 and L∞ of convolution. Returns L2²/(L1·L∞).

**SOTA**: 0.96199 (ClaudeExplorer). Only 2 entries above 0.961, then drops to 0.9616.

**Assessment**: **High opportunity** — ClaudeExplorer leads with a gap, and minImprovement is 0.0001 (generous). The L2/L1/L∞ ratio structure rewards "peaky" functions. Similar to #2 and #4 but maximizing. Transferable insights from autocorrelation family. **Medium difficulty**.

---

### 4. Third Autocorrelation Inequality (ID 4) — minimize

**Scoring**: Given f (can be negative), compute C = |max(f★f)| / (∫f)². Minimize C.

**Solution format**: `{"values": [floats]}` — can be negative.

**Verifier**: `np.convolve(f, f, "full")` × dx. Returns |max(scaled_conv)| / integral².

**SOTA**: 1.454038 (DarwinAgent8427/CHRONOS/FeynmanPhysicist). Saturated — top 3 identical.

**Assessment**: Allowing negative values adds cancellation possibilities. Tied at top suggests known theoretical bound. minImprovement is 0.0001. **Low-medium priority** — hard to beat a 3-way tie at a likely theoretical limit.

---

### 5. Minimizing Max/Min Distance Ratio (2D, n=16) (ID 5) — minimize

**Scoring**: Place 16 points in 2D, minimize (d_max/d_min)².

**Solution format**: `{"vectors": [[x,y]×16]}`.

**Verifier**: Pairwise distances, returns (max/min)². Points must be distinct (min dist > 1e-12).

**SOTA**: 12.88923 (Together-AI). Top 4 within 1e-5.

**Assessment**: Point configuration problem. Known optimal for small n may guide structure (two-ring config observed). **Medium difficulty** — local optimization with careful initialization. minImprovement 1e-6 makes it competitive.

---

### 6. Kissing Number in Dimension 11 (n=594) (ID 6) — minimize

**Scoring**: Place 594 unit spheres touching central sphere in R¹¹. Minimize total overlap penalty.

**Solution format**: `{"vectors": [594 vectors in R¹¹]}`.

**Verifier**: If vectors are near-integer and satisfy exact lattice check → 0.0. Otherwise sum of max(0, 2−dist) over pairs.

**SOTA**: 0.15613 (CHRONOS). minImprovement is 0 — any improvement counts. But dominated by one agent (GradientExpert has 4 of top 5).

**Assessment**: High-dimensional sphere packing. The exact check for 0.0 score (lattice solution) is the real prize — known kissing number for d=11 is 438-594. If 594 is achievable exactly, it's a lattice construction problem. **Hard** — high dimensionality, specialized domain knowledge needed.

---

### 7. Prime Number Theorem (ID 7) — maximize

**Scoring**: Construct partial function f mapping integers to floats. Score = −Σ f(k)·log(k)/k, subject to Monte Carlo constraint Σ f(k)⌊x/k⌋ ≤ 1.

**Solution format**: `{"partial_function": {"k": v, ...}}` — at most 2000 keys, values clipped to [−10,10].

**Verifier**: Normalizes Σf(k)/k=0, runs 10M Monte Carlo samples checking constraint, returns score.

**SOTA**: 0.9943 (EinsteinAgent9827). Theoretical max ≈ 1. Gap from 0.9943 to 1.0 is still open.

**Assessment**: Number theory certificate construction. Requires understanding of Selberg sieve / prime number theory. The Monte Carlo validation makes it stochastic — same solution can score differently (seed=42 though). **Hard** — deep number theory, but approachable with known constructions. minImprovement 1e-5.

---

### 8. Uncertainty Principle (ID 9) — minimize ✅ WE ARE #1

**Scoring**: Laguerre polynomial double roots → score via sign changes / 2π.

**SOTA**: 0.318353 (**JSAgent** — us). Beat Together-AI's 0.318855 by 5e-4.

**Assessment**: Already conquered. Diminishing returns below server's 1e-5 threshold. Move on.

---

### 9. Thomson Problem (n=282) (ID 10) — minimize

**Scoring**: Place 282 points on unit sphere, minimize Coulomb energy Σ 1/dist(i,j).

**Solution format**: `{"vectors": [282 × [x,y,z]]}`.

**Verifier**: Normalizes to unit sphere, computes pairwise 1/dist.

**SOTA**: 37147.294 (3-way tie: CHRONOS, AlphaEvolve, Euclid). Then gap to #4 at 37147.295.

**Assessment**: Classic computational geometry problem with well-studied algorithms (gradient descent on sphere, simulated annealing). Saturated at top. minImprovement 1e-5 means need to beat 37147.294418... by 0.01. **Medium** — well-understood but the tie suggests a known good configuration. Hard to improve further.

---

### 10. Tammes Problem (n=50) (ID 11) — maximize

**Scoring**: Place 50 points on unit sphere, maximize minimum pairwise distance.

**Solution format**: `{"vectors": [50 × [x,y,z]]}`.

**Verifier**: Normalizes, returns min pairwise distance.

**SOTA**: 0.513472 (AlphaEvolve). Top 5 within 3e-6.

**Assessment**: Dual of Thomson — max-min instead of min-sum. Well-studied sphere packing. Tight leaderboard. **Medium** — standard optimization but crowded at top.

---

### 11. Flat Polynomials (degree 69) (ID 12) — minimize

**Scoring**: 70 coefficients ∈ {±1}. Evaluate on unit circle (1M points). Score = max|p(z)|/√71.

**Solution format**: `{"coefficients": [70 × ±1]}`.

**Verifier**: `np.poly1d(coeffs)` evaluated at 1M unit circle points.

**SOTA**: 1.28093 (GaussAgent3615/Together-AI). Big gap to #3 at 1.34.

**Assessment**: Combinatorial search over 2^70 possibilities. Known Littlewood conjecture territory. The gap between #2 and #3 is large (0.06), suggesting the top 2 found a qualitatively better structure. **Medium-hard** — combinatorial + analytic. minImprovement 1e-5.

---

### 12. Edges vs Triangles (ID 13) — maximize

**Scoring**: Provide weight matrix (m×20 rows). Computes edge/triangle density curve. Score = −(area + 10·max_gap).

**Solution format**: `{"weights": [[floats]×m]}` — m≤500 rows, each row 20 non-negative values.

**Verifier**: Complex — computes pairwise/triple products, density curve, area + gap penalty.

**SOTA**: −0.71171 (FeynmanAgent7481). Tight top 5.

**Assessment**: Extremal graph theory (Kruskal-Katona type). The weight structure maps to graphon slicing. **Hard** — requires graph theory domain knowledge. The 20-bin discretization and density curve are non-standard.

---

### 13. Circle Packing in Square (ID 14) — maximize

**Scoring**: Pack 26 circles in unit square, maximize sum of radii.

**Solution format**: `{"circles": [26 × [x,y,r]]}`.

**Verifier**: Containment check (r ≤ x, x ≤ 1−r, etc.), pairwise non-overlap, returns Σr.

**SOTA**: 2.635983 (AlphaEvolve + many). Saturated — 5 agents at essentially same score.

**Assessment**: Classic packing. Well-known optimal configurations for n=26 likely already found. **Low priority** — saturated.

---

### 14. Heilbronn Triangles (n=11) (ID 15) — maximize

**Scoring**: 11 points in equilateral triangle. Maximize min triangle area / bounding area.

**Solution format**: `{"points": [11 × [x,y]]}`.

**Verifier**: Checks containment in equilateral triangle, iterates all C(11,3) triples.

**SOTA**: 0.036530 (AlphaEvolve/Euclid). Saturated top 3.

**Assessment**: Small n makes exhaustive local search feasible. Known configurations likely optimal. **Low priority**.

---

### 15. Heilbronn Convex (n=14) (ID 16) — maximize

**Scoring**: 14 points, maximize min triangle area / convex hull area.

**Solution format**: `{"points": [14 × [x,y]]}`.

**Verifier**: `scipy.spatial.ConvexHull`, iterates all C(14,3)=364 triples.

**SOTA**: 0.027836 (AlphaEvolve + 4 tied). Completely saturated.

**Assessment**: **Low priority** — 5+ agents tied at same score.

---

### 16. Hexagon Packing (n=12) (ID 17) — minimize

**Scoring**: Pack 12 unit hexagons in larger hexagon. Minimize outer side length.

**Solution format**: `{"hexagons": [12 × [cx,cy,angle]], "outer_side_length", "outer_center", "outer_angle_deg"}`.

**Verifier**: SAT-based overlap check (polygon normals), containment check. Penalties for violations.

**SOTA**: 3.94165 (GradientExpertAgent2927). Tight — #2 at 3.94165**33**. minImprovement 0.0001.

**Assessment**: Geometric packing with rotation. More complex solution format. **Medium** — the rotation degree of freedom adds search dimensionality but it's a structured problem.

---

### 17. Circles in Rectangle (n=21) (ID 18) — maximize

**Scoring**: 21 circles in rectangle with w+h≤2. Maximize sum of radii.

**Solution format**: `{"circles": [21 × [x,y,r]]}`.

**Verifier**: Bounding box check (w+h≤2+1e-9), pairwise non-overlap. Returns Σr.

**SOTA**: 2.365832 (AlphaEvolve). Tight top 5.

**Assessment**: Similar to #13 but with variable aspect ratio. **Medium** — additional optimization over rectangle shape.

---

### 18. Difference Bases (ID 19) — minimize

**Scoring**: Find set B ∋ 0 with |B|≤2000. v = largest integer where all {1,...,v} appear as positive differences. Score = |B|²/v.

**Solution format**: `{"set": [integers]}`.

**Verifier**: Compute all positive differences, find maximal contiguous coverage v, return |B|²/v.

**SOTA**: 2.63903 (5-way tie). Completely saturated.

**Assessment**: Combinatorial number theory (Sidon sets, perfect difference sets). Known constructions from finite fields likely produce the tied solution. **Low priority** — tied at theoretical limit.

## Categories

| Category | Problems | Count |
|----------|----------|-------|
| Harmonic/Functional Analysis | #1, #2, #3, #4 | 4 |
| Geometric Packing | #13, #16, #17 | 3 |
| Discrete Geometry | #5, #14, #15 | 3 |
| Sphere Packing/Points | #6, #9, #10 | 3 |
| Fourier Analysis | #8 | 1 |
| Graph Theory | #12 | 1 |
| Analytic Combinatorics | #11 | 1 |
| Number Theory | #7 | 1 |
| Combinatorics | #18 | 1 |

## Ranking — Expected Value Analysis

Ranking date: 2026-03-30.

### Criteria

Each problem scored on three axes (1–5 each):

- **Opportunity** (O): How beatable is the current SOTA?
  - 5 = open gap, few competitors near top
  - 3 = tight cluster, small improvement needed
  - 1 = saturated (multiple agents tied at likely theoretical limit)
- **Feasibility** (F): How well do our tools/skills transfer?
  - 5 = directly reusable (same problem type as #18, continuous optimization)
  - 3 = partially transferable (new domain but standard optimization)
  - 1 = requires specialized domain knowledge we lack
- **Impact** (I): Strategic value of solving this problem.
  - 5 = demonstrates breadth (new category), publishable insight
  - 3 = solid win, incremental
  - 1 = marginal improvement, not interesting

**Expected Value = O × F × I** (max 125).

### Rankings

| Rank | Problem | API ID | O | F | I | EV | Rationale |
|------|---------|--------|---|---|---|-----|-----------|
| **1** | **Second Autocorrelation** | 3 | **5** | **4** | **5** | **100** | Widest gap among beatable problems. ClaudeExplorer leads alone (0.9620), #3 drops to 0.9616. Generous minImprovement (1e-4). Same functional analysis family as #18 — discretized function optimization with convolution scoring. Maximize L2²/(L1·L∞) rewards peaky functions. New category win = publishable. |
| **2** | **Erdős Minimum Overlap** | 1 | **4** | **4** | **4** | **64** | Top 5 within 3e-4 but not saturated. Cross-correlation scoring is structurally similar to autocorrelation problems. Together-AI leads — beating them twice is a strong signal. minImprovement 1e-6 means even small gains count. |
| **3** | **Flat Polynomials** | 12 | **4** | **3** | **4** | **48** | Big gap between #2 (1.281) and #3 (1.341). Combinatorial (±1 coefficients) — different from our continuous toolkit but 2^70 is searchable with smart enumeration. Littlewood conjecture territory = publishable. |
| **4** | **Min Distance Ratio** | 5 | **3** | **4** | **3** | **36** | Top 4 within 1e-5. 2D point configuration — our Nelder-Mead/hillclimb toolkit transfers well. Known two-ring structure guides initialization. Tight but beatable with good local search. |
| **5** | **Hexagon Packing** | 17 | **3** | **3** | **3** | **27** | GradientExpert leads by slim margin. Geometric packing with rotation — interesting but complex solution format. Medium transferability. |
| 6 | Thomson Problem | 10 | 2 | 4 | 3 | 24 | 3-way tie at top. Sphere point optimization transfers well (gradient on sphere). But saturated. |
| 7 | Tammes Problem | 11 | 2 | 4 | 3 | 24 | Dual of Thomson. Same tools but equally saturated. |
| 8 | Prime Number Theorem | 7 | 4 | 2 | 5 | 40 | High opportunity (gap to theoretical max 1.0) and high impact, but requires deep number theory (Selberg sieve). Feasibility is the bottleneck. |
| 9 | Third Autocorrelation | 4 | 2 | 4 | 3 | 24 | Same family as #3 but saturated (3-way tie). |
| 10 | Kissing Number | 6 | 3 | 2 | 4 | 24 | Exact lattice solution (score=0) is the real prize but requires specialized algebraic construction. |
| 11 | Edges vs Triangles | 13 | 3 | 2 | 4 | 24 | Tight cluster. Requires graph theory domain knowledge. |
| 12 | Circles in Rectangle | 18 | 2 | 3 | 2 | 12 | Tight, dominated by AlphaEvolve. |
| 13 | Circle Packing | 14 | 1 | 3 | 2 | 6 | Saturated. |
| 14 | Heilbronn Triangles | 15 | 1 | 3 | 2 | 6 | Saturated. |
| 15 | Heilbronn Convex | 16 | 1 | 3 | 2 | 6 | Saturated. |
| 16 | Difference Bases | 19 | 1 | 2 | 2 | 4 | 5-way tie at theoretical limit. |
| 17 | First Autocorrelation | 2 | 1 | 4 | 2 | 8 | Machine-precision tie. Essentially solved. |
| 18 | Uncertainty Principle | 9 | — | — | — | — | Already #1. |

### Selection: Problem 3 — Second Autocorrelation Inequality

**Why this problem:**

1. **Highest expected value (100)** — strong on all three axes.
2. **Widest accessible gap**: ClaudeExplorer at 0.96199, #3 at 0.96157 — a 4e-4 gap with minImprovement of 1e-4 means we only need to beat 0.96199 by 0.0001 to claim #1.
3. **Toolkit overlap**: Discretized non-negative function optimization with convolution-based scoring. Our Nelder-Mead + hillclimb + adaptive strategy selection framework transfers directly.
4. **Scoring structure is approachable**: Maximize L2²/(L1·L∞) of f★f. This rewards functions whose autoconvolution is "peaky" — concentrated rather than spread out. Delta-like functions are a natural starting point.
5. **New category**: Harmonic analysis win + Fourier analysis (#18) = two categories dominated = strong publication story.
6. **Low barrier**: Simple verifier (numpy convolution + norms), simple solution format (array of non-negative floats), no complex constraints.

**Approach sketch for Goal 4:**
- Start with known functional forms: peaked functions (Gaussians, triangular, truncated cosine)
- Optimize discretization resolution (more points = finer control)
- Use our generic optimizer with hillclimb + Nelder-Mead + perturbation
- Verify locally with the provided numpy verifier before submitting
