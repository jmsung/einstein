# arXiv:2003.10765v2[math.CA]3Aug2020

## ON REGULARITY AND MASS CONCENTRATION PHENOMENA FOR THE SIGN UNCERTAINTY PRINCIPLE

FELIPE GONC¸ALVES, DIOGO OLIVEIRA E SILVA, AND JOAO˜ P. G. RAMOS

Abstract. The sign uncertainty principle of Bourgain, Clozel & Kahane asserts that if a function f : Rd → R and its Fourier transform f are nonpositive at the origin and not identically zero, then they cannot both be nonnegative outside an arbitrarily small neighborhood of the origin. In this article, we establish some equivalent formulations of the sign uncertainty principle, and in particular prove that minimizing sequences exist within the Schwartz class when d = 1. We further address a complementary sign uncertainty principle, and show that corresponding near-minimizers concentrate a universal proportion of their positive mass near the origin in all dimensions.

1. Introduction

Motivated by a problem in the theory of zeta functions over algebraic number ﬁelds, Bourgain, Clozel & Kahane [1] investigated the class of functions A+(d), deﬁned as follows. Given d ≥ 1, a function f : Rd → R is said to be eventually nonnegative if f(x) ≥ 0 for all suﬃciently large |x|. Normalize the Fourier transform,

- (1.1) f(ξ) =

Rd

f(x)e−2πi x,ξ dx,

where  ·,·  represents the usual inner product in Rd. Let A+(d) denote the set of functions f : Rd → R which satisfy the following conditions:

- • f ∈ L1(Rd), f ∈ L1(Rd), and f is real-valued (i.e. f is even);
- • f is eventually nonnegative while f(0) ≤ 0;
- • f is eventually nonnegative while f(0) ≤ 0.


Note that any function f ∈ A+(d) is uniformly continuous. Consider the quantity r(f) := inf{r > 0 : f(x) ≥ 0 if |x| ≥ r},

which corresponds to the radius of the last sign change of f. The product r(f)r( f) is unchanged if we replace f with x  → f(λx) for some λ > 0, and thus becomes a natural object to consider. One of the initial observations in [1] is that the quantity

- (1.2) A+(d) := inf


f∈A+(d)\{0}

r(f)r( f)

2010 Mathematics Subject Classiﬁcation. 42A85, 42B10, 46A11. Key words and phrases. Sign uncertainty principle, Fourier transform, Schwartz class, bandlimited

function, mass concentration.

1

is uniformly bounded from below away from zero. In fact, the following two-sided inequality is established in [1, §3]:

- (1.3)

1 √2πe ≤ liminf

d→∞

A+(d) √

d ≤ limsup

d→∞

A+(d) √

d ≤

1 √2π

.

In particular, the radii r(f),r( f) of the last sign change of f, f, respectively, cannot both be made arbitrarily small, unless f ∈ A+(d) is identically zero. Consequently, the aforementioned results can be regarded as manifestations of a sign uncertainty principle.

The sign uncertainty principle of Bourgain, Clozel & Kahane inspired a number of subsequent works [4, 6, 7]; see also [2, 8]. Gonc¸alves, Oliveira e Silva & Steinerberger [7] proved that radial minimizers for (1.2) exist. More precisely, in each dimension d ≥ 1, they showed that there exists a radial function f ∈ A+(d), satisfying f = f,f(0) = 0, and r(f) = A+(d), and that such a minimizer must necessarily vanish at inﬁnitely many radii greater than A+(d). The precise shape of minimizers remained a mystery in all dimensions d ≥ 1, until Cohn & Gon¸calves [4] exhibited an explicit minimizer in twelve dimensions. In particular, they relied on the following ingredients in order to show that A+(12) = √2:

- • A Poisson-type summation formula for radial Schwartz functions f : R12 → C based on the modular form E6;
- • An explicit construction via a remarkable integral transform discovered by Viazosvska [16] which turns modular forms into radial eigenfunctions of the Fourier transform.


The ﬁrst ingredient leads to the lower bound A+(12) ≥

√2. The second ingredient

produces√2. Moreover,the explicitthe minimizerminimizer,is shownand intoparticularbelong toleadsthe toSchwartzthe upperclassboundS(R12A),+(12)and to≤ be a +1 eigenfunction of the Fourier transform; see [4, Fig. 1] for the corresponding plots. It then becomes natural to consider a complementary problem, associated to −1 eigenfunctions of the Fourier transform, which we now describe.

Let A−(d) denote the set of integrable functions f : Rd → R, with integrable, realvalued Fourier transform f, such that f(0) ≤ 0 while f is eventually nonnegative, and

- f(0) ≥ 0 while − f is eventually nonnegative. Deﬁne the quantity


- (1.4) A−(d) := inf


r(f)r( f).

f∈A−(d)\{0}

Then [4, Theorem 1.4] guarantees that the chain of inequalities (1.3) still holds if A+(d) is replaced by A−(d). It further ensures the existence of radial minimizers for (1.4) which are −1 eigenfunctions of the Fourier transform, and necessarily have inﬁnitely many zeros after the last sign change. Logan [12] has solved the optimization problem

- (1.4) in the one-dimensional case d = 1. Problem (1.4) turns out to be closely related to the sphere packing problem and, in light of the recent breakthroughs [5, 16], it has also been solved in dimensions d ∈ {8,24}; see [3, Prop. 7.1] and [4, §1]. In particular,


A−(1) = 1, A−(8) = √2, and A−(24) = 2. Moreover, if d ∈ {8,24}, then minimizers for (1.4) belong to the Schwartz class, and modulo symmetries are unique within this

class. However, no such reﬁned regularity properties can be asserted a priori in any other dimension.

- 1.1. Main results. In this article, we investigate regularity properties and mass concentration phenomena exhibited by minimizing sequences of (1.2) and (1.4).


We use the letter s to denote a sign from {+,−}, and shall sometimes identify the signs {+,−} with the integers {+1,−1}. A function f : Rd → R is said to be bandlimited if the support of its distributional Fourier transform f is compact, denoted supp( f) Rd. For s ∈ {+,−}, deﬁne the quantities

r(f)r( f); ASs (d) := inf

ABs (d) := inf

r(f)r( f),

f∈As(d)∩S(Rd)\{0}

f∈As(d)\{0} supp( f) Rd

where the inﬁma are taken over nonzero functions in As(d) which are bandlimited and belong to the Schwartz space, S(Rd), respectively. It is then natural to wonder about

the relationship between the sharp constants As(d), ABs (d), and ASs (d).

The identities A−(8) = AS−(8), A−(24) = AS−(24), and A+(12) = AS+(12) are known, simply because the corresponding minimizers in S(Rd) have been explicitly constructed. If (s,d) = (−,1), then uniqueness of minimizers (modulo symmetries) in S(R) fails, but from knowledge of the corresponding minimizers one can likewise infer that A−(1) = AS−(1). According to [1, The´or`eme 3.2], the two-sided inequality

- (1.5) As(d) ≤ ASs (d) ≤ 2As(d)


holds when s = +1, and the argument presented there can be easily adapted to the case s = −1. As remarked in [1], it is not at all clear that the ﬁrst inequality in (1.5) should be an equality.1 Our ﬁrst main result settles this question for (s,d) = (+,1), where all three aforementioned sign uncertainty principles are seen to be equivalent.

- Theorem 1. A+(1) = AB+(1) = AS+(1).


For other combinations of signs and dimensions, barely anything is known about regularity properties of near-minimizers for As(d), and the following conjecture remains open in its full generality.

Conjecture 1. For any s ∈ {+,−} and d ≥ 1, it holds that As(d) = ABs (d) = ASs (d).

The proof of Theorem 1 builds upon a few observations from [1]: Given f ∈ A+(d), there exists x0 ∈ Rd satisfying |x0| ≤ r(f), such that f(x0) < 0. Convolving with the sum of Dirac measures δx

+ 2δ0 yields a new function g ∈ A+(d), satisfying

### + δ−x

0

0

- g(0) < 0 and r(g) ≤ 2r(f). This provides additional room for a further convolution with an appropriate smooth function, and ultimately enables selected minimizing sequences to be found within a smoother function space. To improve on this in the one-dimensional setting, we show that any minimizer of (1.2) is strictly negative on a punctured neigh-


borhood of the origin; in particular, the point x0 can be taken arbitrarily close to the origin if d = 1.

1[1, p. 1218]: “Il n’est point ´evident que la borne A d´eﬁnie par A = inf A(f), quand on impose de surcroıˆt ` f d’appartenir ` S, coı¨ncide avec celle d´eﬁnie pour f parcourant L1.”

The previous paragraph and the explicit minimizer found in [4] together imply the existence of minimizers which are nonpositive in a neighbourhood of the origin in dimensions d ∈ {1,12}. In fact, the minimizer in twelve dimensions is nonpositive on the

open ball B√122 ⊆ R12 centered at the origin of radius √2 = A+(12), which makes it tempting to conjecture that such a property holds in arbitrary dimensions. The numer-

ical examples from [4, 6, 7] provide further evidence for this possibility; see [6, Fig. 1] for the plot of a numerical approximation of a minimizer for A+(1).

An adaptation of the proof of Theorem 1 yields the following improvement over (1.5) in higher dimensions d > 1: There exist constants δd ∈ (0,1), satisfying

√

d(2πe)d/2δd → 1, as d → ∞, such that

- (1.6) AS+(d) ≤ (2 − δd)A+(d).

In fact, if d > 1, then we are able to identify small, but not arbitrarily small, values of |x0| for which a given minimizer f satisﬁes f(x0) < 0. This is the main reason why our methods do not seem suﬃcient to establish Conjecture 1 for the Schwartz class if (s,d) = (+,1). For further details, see §2.3 below.

Even though our current techniques do not seem ﬁt to establish any non-trivial equivalence for the −1 sign uncertainty principle, one might still hope to identify other regularity properties exhibited by near-minimizers. As previously mentioned, problem (1.4) has been solved if d ∈ {1,8,24}. Moreover, if d ∈ {8,24}, then the minimizer is unique modulo symmetries, belongs to the Schwartz class, and is nonnegative in a neighborhood of the origin. If d = 1, then uniqueness fails, but the nonnegative property still holds in all known examples; see Figure 1. In particular, one may expect every suitable function which is suﬃciently close to a minimizer to concentrate a universal proportion of its positive mass on the smallest ball centered at the origin that contains all of its negative mass. Our second main result conﬁrms these heuristics in all dimensions. Before stating it, recall (as shown in [1, 4]) that we can restrict attention to radial functions. More precisely, the quantity As(d) coincides with the minimal value of r(g) in the following optimization problem.

Fourier Eigenvalue Linear Programming Problem (s-FELPP). Let s ∈ {+,−}. Minimize r(g) over all radial g : Rd → R such that

- • g ∈ L1(Rd) \ {0} and g = sg;
- • g(0) = 0 and g is eventually nonnegative.


Given r > 0, let Brd ⊆ Rd denote the open ball of radius r centered at the origin, and g+ := max{g,0}.

- Theorem 2. Given d ≥ 1, there exist constants εd,σd > 0, such that


- (1.7)


g+ ≥ σd g L1(Rd),

Brd(g)

whenever g ∈ A−(d) is a radial function such that g = −g,g(0) = 0, and satisﬁes |r(g) − A−(d)| ≤ εd.

0.05

-4 -2 2 4

- -0.15

- -0.10

- -0.05


2(πξ) (πξ)2 . The function g is a minimizer of the −1-FELPP when d = 1.

Figure 1. Plot of g := f − f, where f(x) = (1 − |x|)+, f(ξ) = sin

We conclude the Introduction with a remark connecting bandlimited functions, Poisson summation, and reconstruction formulae. According to Theorem 1, A+(1) = AB+(1). From this and the Poisson summation formula, a non-trivial conclusion can be withdrawn as in [11, 12]. We record it in the following result, as it may prove useful in further investigations surrounding the Fourier Eigenvalue Linear Programming Problem.

- Proposition 1. Let f ∈ A+(1) be a nonzero, bandlimited function, such that supp( f) ⊆ [−12, 12]. Then r(f) ≥ 1. Moreover, r(f) = 1 if and only if there exists α > 0, such that


sin2(πx−21) x2 − 1

.

f(x) = α

- 1.2. Outline. We prove Theorem 1 in §2, Theorem 2 in §3, and Proposition 1 in §4. The arguments rely on several lemmata which we choose to formulate in general dimensions whenever possible, and prove in §5. We dedicate the ﬁnal §6 to a connection with the sign uncertainty principle for Fourier series on the torus, recently established in [6].
- 1.3. Notation. Let N := {1,2,...} and N0 := N ∪ {0}. Given f : Rd → R, let f+ := max{f,0}, and f− := max{−f,0}. In this way, f+,f− are nonnegative functions which are never positive at the same point, and satisfy f = f+ − f− and |f| = f+ + f−. Given a set E ⊆ Rd, its indicator function is denoted by E, and its Lebesgue measure


by |E|. Given r > 0, we continue to let Brd ⊆ Rd denote the open ball of radius r centered at the origin.

2. Proof of Theorem 1

- 2.1. Proof of A+(1) = AB+(1). It suﬃces to show that A+(1) ≥ AB+(1), and we proceed in four steps.


- Step 1. Let f ∈ A+(1) be a minimizer for (1.2) satisfying f = f, f(0) = 0. Then there exists ε > 0, such that f(x) < 0, for every x ∈ (−ε,ε) \ {0}.


The proof of Step 1 hinges on two distinct observations, the ﬁrst of which is inspired by work of Logan [11, 12] on various extremal problems concerning the behavior of positivedeﬁnite bandlimited functions. The following result holds for any sign s ∈ {+,−} in arbitrary dimensions d ≥ 1, and should be compared with [11, Lemma], where a onedimensional variant of the same result is proved.

- Lemma 1. Given s ∈ {+,−}, d ≥ 1, let f ∈ As(d) be radial, such that f = sf, f(0) = 0. Suppose that there exists a sequence {xn}n∈N ⊆ Rd \ {0}, such that xn → 0,


d |y|2|f(y)|dy < +∞, and

as n → ∞, and sf(xn) ≥ 0, for all n. Then R

- (2.1)

Rd

|y|2f(y)dy ≤ 0.

The second observation is that a chain of rearrangement-type inequalities can be set up in such a way as to contradict estimate (2.1). A similar approach already proved fruitful in [7, §4]. To implement it in the present context, let f ∈ A+(1) be a minimizer for (1.2), which we suppose to be L1-normalized, f L1 = 1, and to satisfy f = f, f(0) = 0; see [7, §3]. If f fails to be strictly negative on any punctured neighborhood of the origin, then the hypotheses of Lemma 1 for s = +1 are veriﬁed. Writing f = f+−f−, we then have that

- (2.2)

∞

0

y2f(y)dy =

r(f)

0

y2f+(y)dy −

r(f)

0

y2f−(y)dy +

∞

r(f)

y2f(y)dy ≤ 0.

Setting σ(f) := f+ L1(0,r(f)), and appealing to [7, Lemma 12], we can bound each of the integrals on the right-hand side of (2.2) as follows:

r(f)

0

y2f+(y)dy ≥

σ(f)

0

- (2.3) y2 dy;

r(f)

0

y2f−(y)dy ≤

r(f)

r(f)−41

- (2.4) y2 dy;

∞

r(f)

y2f(y)dy ≥

r(f)+14−σ(f)

r(f)

- (2.5) y2 dy.


To see why this is the case, note that f L∞ ≤ 1, and that

f+ +

R

f− =

R

|f| = 1;

R

f+ −

f− =

f = f(0) = 0,

R

R

R

and thus R f+ = R f− = 21; moreover, the functions f,f± are even, and so their masses are equally spread over the positive and negative half-lines. Estimates (2.2)–

- (2.5) immediately imply that


r(f)3 − (r(f) − 14)3 3

σ(f)3 3 −

(r(f) + 14 − σ(f))3 − σ(f)3 3 ≤ 0,

+

which can be equivalently rewritten as

- (2.6) r(f) +

1 4

σ(f) r(f) +

1 4 − σ(f) ≥

r(f) 8

.

We seek for a suﬃciently good upper bound for σ(f) which will then force the desired contradiction. With this purpose in mind, observe that the left-hand side of (2.6) deﬁnes an increasing function of σ(f), provided σ(f) < 41. The next result provides a slight improvement over [7, Lemma 14] in terms of the admissible radius r(f).

Lemma 2. Let f ∈ A+(1) be such that f L1 = 1, f = f, f(0) = 0, and r(f) ∈ [41, √12]. Then the following inequality holds:

- (2.7) f+(x) ≤

- 1

- 2


+

sin(2π(r(f) − 41)x) − sin(2πr(f)x) πx

, for every x ∈ [0,r(f)].

With the two observations in place, we may now ﬁnish the proof of Step 1. Since f L∞ ≤ f L1 = f L1 = 1 and f− L1(0,r(f)) = 14, the following superlevel set estimate

holds:

- (2.8) |{x ∈ [0,r(f)] : f(x) ≥ 0}| ≤ r(f) −

1 4

.

Since f is a minimizer for (1.2), and f = f, it follows from [7, Theorem 2] that 0.45 ≤ r(f) ≤ 0.595; in particular, r(f) ∈ [14, √12]. As a consequence, we may appeal to (2.8) in order to estimate

σ(f) =

[0,r(f)]

f+ ≤ sup

J⊆[0,r(f)] |J|=r(f)− 1

4

J

- (2.9) f+


≤

r(f)

1 4

sin(2π(r(f) − 41)x) − sin(2πr(f)x) πx

- 1

- 2


+

dx := Φ(r(f)),

where from the ﬁrst to the second line we invoked Lemma 2 and [7, Lemma 11], using the fact that the integrand on the right-hand side deﬁnes an increasing function of x. We are thus reduced to a straightforward analysis of the function Φ. It is easy to check that Φ(r(f)) ≤ Φ(0.595) < 0.121, and therefore the chain of inequalities (2.9) implies σ(f) < 0.121. But if σ(f) < 0.121 and 0.45 ≤ r(f) ≤ 0.595, then (2.6) does not hold. This yields the desired contradiction, and concludes the proof of Step 1.

- Step 2. There exists a minimizing sequence {fn}n∈N ⊆ A+(1) for (1.2), such that the following conditions hold, for every n:


- (a) fn(0) < 0;
- (b) fn(x) > 0, for every |x| > r(fn);
- (c) fn = fn;
- (d) x2fn(x) ≥ cn, for some cn > 0 and all suﬃciently large |x|.


Let f ∈ A+(1) be a minimizer for +1-FELPP. By Step 1, there must exist a sequence {xn}n∈N ⊆ (0,∞) such that xn → 0, as n → ∞, and f(xn) < 0, for every n. Deﬁne an associated sequence {Tn}n∈N of tempered distributions via

Tn := δx

### + δ−x

+ 2δ0.

n

n

Setting gn := Tn ∗ f, one easily checks that {gn}n∈N ⊆ A+(1) is a minimizing sequence for (1.2). Indeed, the quantity

gn(x) = f(x − xn) + f(x + xn) + 2f(x)

is nonnegative if x ≥ r(f) + xn, and satisﬁes gn(0) = 2f(xn) < 0 (in particular, gn does not vanish identically). On the other hand,

Tn(ξ) = 2cos(2πxnξ) + 2 ≥ 0,

and so gn(0) = 4 f(0) ≤ 0. By the scaling argument detailed in [7, §3.3], we lose no generality in assuming that r( gn) = r(gn). In this case, {gn + gn}n∈N ⊆ A+(1) is a minimizing sequence for (1.2) satisfying conditions (a) and (c). Condition (b) can be achieved by further adding a suitable Gaussian function: Setting

gn(0) + gn(0) 2

exp(−π·2),

hn := gn + gn −

one again checks that {hn}n∈N ⊆ A+(1) is a minimizing sequence for (1.2) which satisﬁes conditions (a)–(c). In order to further ensure condition (d), we make use of the following simple observation.

- Lemma 3. Given d ≥ 1, there exists a function η ∈ A+(d), such that η = η, η(0) < 0, and |x|d+1η(x) ≥ 1, for all suﬃciently large values of |x|.


Let η ∈ A+(1) be given by Lemma 3, and pick the smallest r0 > 0 such that x2η(x) ≥ 1, for every |x| ≥ r0. Given n ∈ N, set βn = 1 whenever r(hn) ≥ r0. Otherwise, given δ > 0 which is suﬃciently small so that r(hn) + nδ < r0, set βn = βn(δ) > 0 in such a way that

hn(x) + βnη(x) > 0, for every x ∈ r(hn) + nδ ,r0 . That such a choice of βn is possible follows from the fact that each function hn is eventually (strictly) positive. Then the sequence {fn := hn + βnη}n∈N ⊆ A+(1) is minimizing for (1.2), and satisﬁes properties (a), (c), and (d). Letting δ → 0+, we ensure that condition (b) is fulﬁlled as well. This concludes the veriﬁcation of Step 2.

- Step 3. Let f ∈ A+(1) be such that f L1 = 1, f = f, f(0) < 0. Suppose that there exist constants c,R > 0, such that


- (i) f(x) > 0, for every |x| > r(f);
- (ii) x2f(x) ≥ c, for every |x| ≥ R.


Then, given ε > 0, there exists a bandlimited function g ∈ A+(1), such that g(x) > 0, for every |x| ≥ r(f) + ε.

Fix a nonnegative, even, compactly supported, smooth function ψ ∈ C0∞(R), such that ψ L2 = 1. Set ϕ := ψ ∗ ψ and ϕδ(x) := ϕ(δx). As δ → 0+, the family { ϕδ}δ>0 constitutes an approximation to the identity. Therefore the bandlimited function gδ :=

f ∗ ϕδ should provide a good approximation for f, for small enough values of δ. We turn to the details.

Let f,c,R be as above, and let ε > 0 be arbitrary but given. We show that δ = δ(f,c,R,ε) can be chosen suﬃciently small, so that g = gδ belongs to A+(1), and satisﬁes g(x) > 0, for every |x| ≥ r(f) + ε. Let R1 ≥ R be such that

- (2.10) | ϕ(ξ)| ≤ 10−6c|ξ|−3, for every |ξ| ≥ R1. This is certainly possible since ϕ is rapidly decreasing. By letting δ → 0+, the diﬀerence

- f − gδ can be made uniformly close to 0 in the interval [r(f) + ε,2R1]. Thus it suﬃces to consider |x| > 2R1, in which case the following chain of inequalities holds, as long as δ > 0 is suﬃciently small:

gδ(x) =

∞

−∞

f(x − ξ) ϕδ(ξ)dξ ≥

δ1/2

−δ1/2

f(x − ξ) ϕδ(ξ)dξ −

x+r(f)

x−r(f)

ϕδ(ξ)dξ

≥

c 4x2

δ1/2

−δ1/2

ϕδ(ξ)dξ −

x+r(f)

x−r(f)

ϕδ(ξ)dξ ≥

c 8x2 −

x+r(f)

x−r(f)

(2.11) ϕδ(ξ)dξ.

In the ﬁrst inequality, we used hypothesis (i) to ensure that f(x − ξ) ≥ 0 unless ξ ∈ [x − r(f),x + r(f)], and the fact that f L∞ ≤ 1; the second inequality holds for suﬃciently small δ > 0, in view of hypothesis (ii); and the third inequality holds for suﬃciently small δ > 0 since { ϕδ}δ>0 is an approximation to the identity. Invoking

- (2.10), we have that


0 ≤ ϕδ(ξ) = δ−1 ϕ(δ−1ξ) ≤

1 δ

c 106|δ−1ξ|3

=

cδ2 106|ξ|3

,

for every |ξ| ≥ δR1. Since |x| > 2R1, it follows that |x − r(f)| ≥ δR1, and therefore the last integral on the right-hand side of (2.11) can be estimated as follows:

(2.12)

x+r(f)

x−r(f)

ϕδ(ξ)dξ ≤

cδ2 106

x+r(f)

x−r(f)

dξ |ξ|3

≤

c/2 106

δ2 (x − r(f))2 ≤

2c 106

δ2 x2 ≤

c 104x2

,

provided 2δ2 < 102. Estimates (2.11), (2.12) together imply that gδ(x) > 0, for every |x| > 2R1, as long as δ > 0 is suﬃciently small. Finally, one easily checks that

- gδ ∈ A+(1), provided δ > 0 is suﬃciently small. For instance, gδ(0) ≤ 0 since f(0) < 0 (the strict inequality is crucial here) and f is continuous. Step 3 follows.




- Step 4. Conclude. Consider a minimizing sequence {fn}n∈N ⊆ A+(1) for (1.2), satisfy-


ing fn L1 = 1, fn(0) < 0, fn(x) > 0 if |x| ≥ r(fn), fn = fn, and x2fn(x) ≥ cn if |x| is suﬃciently large. The existence of such a sequence follows from Step 2. Running the

proof of Step 3 on each fn individually, we ﬁnd that there exists a bandlimited function gn = fn ∗ ϕδ ∈ A+(1), such that r(gn) ≤ r(fn) + n1. Since gn = fnϕδ has pointwise the same sign as fn, we may let n → ∞ and conclude that {gn}n∈N ⊆ A+(1) is a minimizing sequence for (1.2) consisting of bandlimited functions, as desired.

- 2.2. Proof of A+(1) = AS+(1). Following [1, §1], consider the restricted classes A˜+(d) := {f ∈ A+(d) : f = f,f(0) < 0};


A˜S+(d) := {f ∈ A+(d) ∩ S(Rd) : f = f,f(0) < 0}, and deﬁne the corresponding optimal constants

r(f)r( f); A˜S+(d) := inf

A˜+(d) := inf

r(f)r( f). Our next result reveals that these constants coincide in all dimensions.

f∈A˜S+(d)\{0}

f∈A˜+(d)\{0}

- Proposition 2. Let d ≥ 1. Then A˜+(d) = A˜S+(d).

- Proof of Proposition 2. It suﬃces to show that A˜+(d) ≥ A˜S+(d). With this goal in mind, let f ∈ A˜+(d). Given δ > 0, consider a nonnegative, radial, compactly supported, smooth function ψδ ∈ C0∞(Rd), such that supp(ψδ) ⊆ Bδd; further assume ψδ to be L1-normalized, ψδ L1 = 1. Deﬁne ϕδ := ψδ ∗ ψδ, g := f ∗ ϕδ, and

(2.13) h := g ∗ ϕδ + g ϕδ. The following lemma lists the key properties of the function h.

Lemma 4. Let f ∈ A˜+(d). Given ε > 0, there exists δ > 0, such that the function h deﬁned in (2.13) above satisﬁes the following properties:

- (a) h ∈ S(Rd), h = h,h(0) < 0;
- (b) r(h) ≤ r(f) + ε.


Part (a) of Lemma 4 implies that h ∈ A˜S+(d), and the inequality A˜+(d) ≥ A˜S+(d) then follows from part (b) of Lemma 4 by letting ε → 0+.

The desired identity, A+(1) = AS+(1), follows from the chain of inequalities (2.14) A+(1) ≤ AS+(1) ≤ A˜S+(1) ≤ A˜+(1) ≤ A+(1). The ﬁrst two inequalities in (2.14) are trivial, and the third one follows from Proposition

2. Our next result addresses the last inequality in (2.14). Proposition 3. A˜+(1) ≤ A+(1).

While the argument in Proposition 2 could be adapted to handle the present case as well, we oﬀer a diﬀerent proof which does not hinge on Lemma 4 and could prove of independent interest.

- Proof of Proposition 3. Let f ∈ A+(1) be a minimizer for (1.2) satisfying f = f, f(0) = 0; in particular, r(f) = A+(1). Given ε > 0, we can invoke Step 1 of §2.1 in order to ensure that there exists x0 ∈ (−ε,ε), such that f(x0) < 0. Similarly to Step 2 of §2.1,




consider the measure T := δx

### + δ−x

+ 2δ0, which is positive-deﬁnite in the sense that

0

0

- (2.15) T(ξ) = 2cos(2πx0ξ) + 2 ≥ 0, for every ξ, and deﬁne g := T ∗ f. Since
- (2.16) g(x) = f(x − x0) + f(x + x0) + 2f(x),


- it follows that g is real-valued, integrable, and even. Moreover, g(0) = 2f(x0) < 0. Since |x0| ≤ ε, it follows from (2.16) that
- (2.17) g(x) ≥ 0, if |x| ≥ r(f) + ε.

In light of (2.15), we have that g(ξ) = T(ξ) f(ξ) ≥ 0 if and only if f(ξ) ≥ 0. In particular,

- (2.18) g(ξ) ≥ 0, if |ξ| ≥ r(f).

Moreover, g(0) = 4f(0) = 0. Consider the dilation h := g(λ·), where λ := (1+ε/r(f))1/2. Then h(0) = g(0) < 0, h(0) = λ−1 g(0) = 0, and the functions h, h are nonnegative on the interval [(r(f)2 + εr(f))1/2,∞). Real-valuedness, integrability, and evenness of h, h follow from those of g. Therefore h + h ∈ A˜+(1), whence A˜+(1) ≤ (r(f)2 + εr(f))1/2. Letting ε → 0+, it follows that A˜+(1) ≤ r(f) = A+(1).

2.3. A short proof of the higher dimensional improvement (1.6). Let f ∈ A+(d) be a nonzero function, for which the product r(f)r( f) is suﬃciently close to A+(d)2. By the usual reductions, we may assume that the function f is radial, and satisﬁes f = f, f(0) = 0, and f L1 = 1. In particular,

|{x ∈ Brd(f): f(x) < 0}| ≥

Brd(f)

f− = 21. This implies the following superlevel set estimate:

- (2.19) |{x ∈ Brd(f): f(x) ≥ 0}| ≤ νdr(f)d − 12,

where, as usual, νd = 2d−1π

d

2Γ(d2)−1 is the Lebesgue measure of the unit ball in Rd. Suppose that r > 0 is such that f(x) ≥ 0, for every x ∈ Brd. Trivially, r < r(f). In order to improve on this, we simply note that (2.19) implies rd ≤ r(f)d −(2νd)−1. Thus there exists x0 ∈ Rd, satisfying

|x0| ≤ r(f)d − (2νd)−1

1 d

, and f(x0) < 0.

The rest of the argument follows very similar ideas to those in §2.2. In particular, we obtain the following inequality:

- (2.20) AS+(d) ≤


 1 + 1 −

 A+(d).

1 d

1 2νdA+(d)d

Setting θd := (2νd)−1A+(d)−d, we estimate

1

1 d

θd d

1

1

d−1 dt ≥

1 − (1 − θd)

t

d =

.

1−θd

√

d(2πe)−d/2, for some absolute constant C > 0. Plugging this back into (2.20) yields (1.6).

Stirling’s formula and (1.3) together imply that θd ≥ C

3. Proof of Theorem 2

The proof of Theorem 2 proceeds by contradiction. We start by establishing the following claim. If Theorem 2 does not hold, then there exists a radial minimizer f ∈ A−(d) of (1.4), satisfying f = −f, f(0) = 0, such that f(x) ≤ 0 for all x ∈ Brd(f).

To see why this is necessarily the case, start by observing that, if Theorem 2 does not hold, then there exists a minimizing sequence {fn}n∈N ⊆ A−(d) for (1.4) consisting of radial functions, satisfying fn = −fn, fn(0) = 0, fn L1 = 1, |r(fn) − A−(d)| ≤ n1, and

1 n

(fn)+ ≤

- (3.1)


.

Brd(fn)

No generality is lost in assuming that the sequence {r(fn)}n∈N is strictly decreasing. By Jaming’s higher dimensional version of Nazarov’s uncertainty principle [9], there exists a constant Kd > 0 such that, for every n ∈ N,

- (3.2)

Brd(fn)

fn ≤ −Kd.

In fact, this amounts to a straightforward modiﬁcation of [7, Lemma 23], as was already observed in [4, §3.2]. Since fn = −fn and fn L1 = 1, it follows that

fn 2L2 ≤ fn L1 fn L∞ ≤ fn L1 fn L1 = fn 2L1 = 1.

The Banach–Alaoglu Theorem then implies, possibly after extraction of a subsequence, that the sequence {fn}n∈N converges weakly to some function f ∈ L2. Since A−(d) is convex, we can then apply Mazur’s Lemma to produce a sequence {gn}n∈N which converges strongly to f in L2, with each gn being a ﬁnite convex combination of elements from {fm}m≥n. For each n ∈ N, gn is radial, gn = −gn, gn(0) = 0, gn L2 ≤ 1, and, possibly after passing to a further subsequence, the following additional properties hold:

|r(gn) − A−(d)| ≤

1 n

- (3.3) ;

Brd(gn)

(gn)+ ≤

1 n

- (3.4) ;

Brd(gn)

gn ≤ −

Kd 2

- (3.5) ;
- (3.6) gn → f almost everywhere, as n → ∞.


Property (3.3) follows from the fact that the sequence {r(fn)}n∈N is decreasing, together with each gn being a convex combination of elements from the tail sequence {fm}m≥n. Properties (3.4), (3.5) follow from the latter observation, together with the elementary inequality (x + y)+ ≤ x+ + y+, valid for every x,y ∈ R, and estimates (3.1), (3.2). Property (3.6) follows at once by extracting a further subsequence. In particular, from

- (3.5) it follows that


Kd 4

f ≤ −

,

### and therefore f does not vanish identically. Moreover, (3.4) implies that

f+ = 0,

Brd(f)

hence f ≤ 0 in Brd(f). To conclude the proof of the claim, we still have to check that f satisﬁes all required properties. From (3.3) it follows that r(f) = A−(d). From (3.6) it follows that f is radial. That f = −f follows at once from weak convergence. Setting r1 := r(f1) = supn∈N r(fn), we may apply Fatou’s Lemma to the sequence {gn+ Bd

### }n∈N (consisting of nonnegative functions which converge almost everywhere to f + Bd

r1

) and deduce that f ∈ L1, and that

r1

f(0) =

f ≤ liminf

gn = 0.

n→∞ Rd

Rd

In particular, f(0) = − f(0) ≥ 0. Since f ≤ 0 in Brd(f), it follows that f(0) = 0. This concludes the veriﬁcation of the claim.

We will need a higher dimensional version of the rearrangement inequalities used in §2.1. The following elementary result from [10, §1.14] suﬃces for our application.

- Lemma 5 (Bathtub Principle, [10]). Let h : Rd → R be a measurable function, such that |{x ∈ Rd: h(x) < t}| is ﬁnite for all t ∈ R. Let the number G > 0 be given, and deﬁne a class of measurable functions on Rd by


CG = g : Rd → [0,1] :

Then the minimization problem

g = G .

Rd

- (3.7) I = inf

g∈CG Rd

gh

is solved by g(x) = {h<s}(x) + c {h=s}(x), where

s = sup{t ∈ R: |{x ∈ Rd : h(x) < t}| ≤ G}; c|{x ∈ Rd: h(x) = s}| = G − |{x ∈ Rd: h(x) < s}|.

The minimizer is unique if G = |{x ∈ Rd: h(x) < s}| or if G = |{x ∈ Rd: h(x) ≤ s}|. If Theorem 2 does not hold, then we have already veriﬁed the existence of a radial

minimizer f ∈ A−(d) of (1.4), satisfying f = −f, f(0) = 0, such that f ≤ 0 on Brd(f). Normalizing f L1 = 1, so that f L∞ ≤ 1, we then have that

- (3.8) −


- 1

- 2


f =

f =

.

Rd\Brd(f)

Invoking Lemma 1 with s = −1, and then Lemma 5 with h(y) = |y|2, we have that 0 ≥

- (3.9) |y|2f(y)dy

≥

Btd\Brd(f)

|y|2 dy −

Brd(f)\Bsd

- (3.10) |y|2 dy

=

νd 1 + 2/d

- (3.11) (td+2 + sd+2 − 2r(f)d+2).


|y|2f(y)dy =

### |y|2f(y)dy +

Rd

Rd\Brd(f)

Brd(f)

d

2Γ(d2)−1 denotes the Lebesgue measure of the unit ball B1d ⊆ Rd and, in light of (3.8), the radii s < t in (3.10) are deﬁned in such a way as to ensure that |Brd(f) \ Bsd| = |Btd \ Brd(f)| = 12. Equivalently,

Here, νd := 2d−1π

1/d

1/d

- 1

- 2νd


- 1

- 2νd


s = r(f)d −

, t = r(f)d +

.

2

The strict convexity of the function x  → |x|1+

d implies that

d+2 d

td + sd 2

td+2 + sd+2 > 2

= 2r(f)d+2,

hence (3.11) deﬁnes a positive quantity. The chain of inequalities (3.9)–(3.11) then leads to the desired contradiction. This concludes the proof of Theorem 2.

4. Proof of Proposition 1

Let f ∈ A+(1) \ {0} be a bandlimited function, such that supp( f) ⊆ [−21, 12]. With the Fourier transform normalized as in (1.1), the Poisson summation formula implies

f(n) =

f(k).

n∈Z

k∈Z

Dilating by a parameter α > 0, and translating by an arbitrary β ∈ R, yields

f α k exp 2πiαβk .

- (4.1) α


f(αn + β) =

n∈Z

k∈Z

The function f is continuous, and so f(±21) = 0. Thus the right-hand side of (4.1) equals f(0) provided α ≤ 2, and so

f(αn + β) = α−1 f(0) ≤ 0,

- (4.2)


n∈Z

for every (α,β) ∈ (0,2] × R. Aiming at a contradiction, suppose r(f) < 1. Given α ∈ (0,2] so that r(f) ≤ α2 ≤ 1, set β = α2. From (4.2), it follows that

f((2n + 1)β) ≤ 0,

- (4.3)


n∈Z

for every β ∈ [r(f),1]. But f(x) ≥ 0, for every |x| ≥ r(f), and so (4.3) implies f(x) = 0, for every x ∈ [r(f),1].

Being the Fourier transform of a compactly supported function, the function f extends to an entire function on the whole complex plane, and as such it cannot vanish on a non-degenerate interval without being identically zero. This shows that r(f) ≥ 1.

Now, suppose r(f) = 1. Then replicating the argument from the previous paragraph with β = α2 = 1 yields

- (4.4) f(2n + 1) = 0, for every n ∈ Z. Since the function f does not change signs at the zeros ±3,±5,..., we also have that
- (4.5) f (2n + 1) = 0, for every n ∈ Z \ {−1,0}.

Set g(x) := f(2x + 1). Then g ∈ L2(R), and g is supported on [−1,1]. By the Paley–Wiener–Schwarz Theorem [14], the function g coincides with the restriction to R of a complex-valued entire function of exponential type 2π. It follows from Vaaler’s interpolation formula [15, Theorem 9] that

g(x) =

sinπx π

2

m∈Z

g(m) (x − m)2

+

n∈Z

g (n) x − n

,

where the expression on the right-hand side converges uniformly on compact subsets of the real line. Conditions (4.4), (4.5) then translate into

g(x) =

sinπx π

2 g (−1) x + 1

+

g (0) x

,

which can be rewritten in terms of the original function f as

f(2x + 1) =

sinπx π

2 2f (−1) x + 1

+

2f (1) x

.

Since f is even, f (−1) = −f (1). Consequently,

f(2x + 1) = 2f (1)

sinπx π

2 1 x(x + 1)

.

A change of variables yields

- (4.6) f(x) =


sin2(πx−21) x2 − 1

8f (1) π2

,

which belongs to the class A+(1) if and only if f (1) ≥ 0. For the converse direction, note that the Fourier transform of the function f given by (4.6) is easy to calculate:

4f (1) π

2,0] − [0,12])(ξ)sin(2πξ).

( [−1

f(ξ) =

In particular, this shows that f is a bandlimited function with Fourier support [−21, 12]; see Figure 2. It is easy to check that f ∈ A+(1), and that r(f) = 1. This concludes the proof of Proposition 1.

-4 -2 2 4

- -1.0

- -0.5


sin2(π x−21)

### Figure 2. Plot of the function f(x) = π8

x2−1 (thick), and of its Fourier transform f(ξ) = π4( [−1

2

2,0] − [0,12])(ξ)sin(2πξ) (dashed).

5. Proofs of Lemmata

- Proof of Lemma 1. Let s ∈ {+,−} and f ∈ A−(d) be as in the statement of the lemma. Since f = sf, f is even, and sf(xn) ≥ 0 = f(0), we have that


f(0) − sf(xn) |xn|2

- (5.1)


1 − cos(2π xn,y ) |xn|2

1 − cos(2π xn,y ) |xn|2

f(y)dy ≤ 0.

=

f(y)dy +

Rd\Brd(f)

Brd(f)

Uniformly on compact subsets of the real line,

1 − cos(2πtu) t2

= 2π2u2.

- (5.2) lim


t→0

It follows that the ﬁrst summand on the right-hand side of (5.1) is bounded independently of the sequence {xn}n∈N, and tends to a ﬁnite limit, as n → ∞.

Let ek ∈ Rd denote the k-th coordinate unit vector, and write y = (y1,...,yd) ∈ Rd. Since f is radial, we lose no generality in assuming that xn = λnek, for some λn > 0 and 1 ≤ k ≤ d. Then |xn| = λn and xn,y = λnyk. Given R ≥ r(f), the second summand on the right-hand side of (5.1) (whose integrand is nonnegative on the region of integration) can be bounded from below as follows:

1 − cos(2π xn,y ) |xn|2

1 − cos(2π xn,y ) |xn|2

f(y)dy ≥

f(y)dy.

Rd\Brd(f)

BRd \Brd(f)

It then follows from (5.1), (5.2) that sup

yk2f(y)dy < +∞,

R≥r(f) BRd \Brd(f)

d |y|2|f(y)|dy < +∞. Finally, (2.1) follows from noting that

whence R

1 − cos(2π xn,y ) |xn|2

- 1

- 2π2


yk2f(y)dy =

f(y)dy ≤ 0, and summing in k.

lim

n→∞ Rd

Rd

- Proof of Lemma 2. Reasoning as in the proof of [1, Th´eore`me 1.1], we have that

- (5.3) f+(x) ≤ 2

∞

0

f−(y)(1 − cos(2πxy))dy.

If x ∈ [0,r(f)], then y  → 1 − cos(2πxy) deﬁnes a nonnegative, increasing function of y on the interval [0,r(f)], provided r(f) ≤ √12. Since supp(f−) ⊆ [−r(f),r(f)], and

- f− L1(0,r(f)) = 41 ≤ r(f), by [7, Lemma 11] it then follows that


∞

0

f−(y)(1 − cos(2πxy))dy ≤

r(f)

r(f)−41

(1 − cos(2πxy))dy

=

1 4

+

sin(2π(r(f) − 14)x) − sin(2πr(f)x) 2πx

- (5.4) . Estimate (2.7) follows at once from (5.3), (5.4), and the lemma is proved.

Proof of Lemma 3. Let Bd

1

denote the indicator function of the unit ball B1d ⊂ Rd, and deﬁne the convolutions χ := Bd

1

∗ B1d and ϕ := χ ∗ χ. Explicitly, χ(x) = (2 − |x|)+, χ(ξ) =

Jd/2(2π|ξ|) |ξ|d/2

2

,

where Jd/2 denotes the Bessel function of the ﬁrst kind. One easily checks that ϕ, ϕ ∈ L1. Moreover, the function ϕ is bandlimited, and standard decay properties of the Bessel functions imply the existence of a constant A > 0, such that

ϕ(x) =

B2d

(2 − |t|)

Jd/2 2(2π|x − t|) |x − t|d

dt ≥ A|x|−(d+1),

provided |x| is suﬃciently large. Let ψ := ϕ + ϕ. Then ψ = ψ, and |x|d+1ψ(x) ≥ A, for all suﬃciently large values of |x|. This is still not the desired function since ψ(0) > 0, but one can simply add an appropriate Gaussian function. For instance, the function x  → η(x) := A−1(ψ(x) − 2ψ(0)exp(−π|x|2)) ∈ A+(d) satisﬁes all the required properties.

Proof of Lemma 4. If δ > 0 is small enough, then

- (5.5) g(0) =




fϕδ < 0,

B2dδ

since the function f is continuous and f(0) < 0. Moreover, g(0) = f(0)( ψδ(0))2 < 0. Further note that g(x) ≥ 0, provided f ≥ 0 on the ball x + B2dδ, and so it suﬃces to take δ ≤ 2ε in order to ensure that r(g) ≤ r(f)+ε. With these preliminary observations in place, we are now ready for the proof of the lemma.

For part (a), one easily checks that h is a Schwartz function which coincides with its own Fourier transform. Moreover,

h(0) = ( g ∗ ϕδ)(0) + g(0)( ψδ(0))2, where both summands are negative. For the ﬁrst summand, note that ( g ∗ ϕδ)(0) =

B2dδ gϕδ is negative if δ > 0 is small enough, since the function g is continuous and g(0) < 0. For the second summand, this is clear in light of (5.5) and the real-valuedness of ψδ.

For part (b), we seek to verify that h(x) ≥ 0, if |x| ≥ r(f)+ε, which will follow from ( g ∗ ϕδ)(x) ≥ 0 and g(x) ϕδ(x) ≥ 0, if |x| ≥ r(f) + ε.

The lower bound for g ϕδ follows immediately from r(g) ≤ r(f) + ε, whereas f = f implies

g ∗ ϕδ = ( f · ϕδ) ∗ ϕδ = (f · ϕδ) ∗ ϕδ.

But r(f · ϕδ) ≤ r(f) since ϕδ = ( ψδ)2 ≥ 0, and so the lower bound for g ∗ ϕδ follows as before. This concludes the veriﬁcation of part (b), and the proof of the lemma.

6. From continuous to discrete uncertainty

Very recently, the authors [6] established new and very general sign uncertainty principles which apply to certain classes of bounded linear operators and metric measure spaces. As a corollary, we obtained a sign uncertainty principle for Fourier series on the d-torus Td = Rd/Zd, which we proceed to describe.

Given s ∈ {+,−} and d ≥ 1, let Ps(Td) denote the class of continuous, even functions

- g : Td → R, such that g ∈ 1, g(0) ≤ 0, and s g is eventually nonnegative while sg(0) ≤ 0. Given g ∈ Ps(Td), deﬁne the quantities2


√

r(g;Td) := inf{r > 0 : g(x) ≥ 0 if

d

2 ≥ |x|2 ≥ r}; ks( g) := min{k ≥ 1: s g(n) ≥ 0 if |n|2 ≥ k},

(here, | · |2 denotes the Euclidean norm) together with the optimal constant

- (6.1) Ps(Td) := inf


r(g;Td)ks( g). A straightforward application of [6, Theorem 1.2] reveals that

g∈Ps(Td)\{0}

d 2πe

Ps(Td) ≥ (1 + o(1))

.

Identity A+(1) = AB+(1) from Theorem 1 leads to the following connection between the continuous and discrete versions of the one-dimensional +1 sign uncertainty principle.

- Proposition 4. Given s ∈ {+,−} and d ≥ 1, it holds that


Ps(Td) ≤ ABs (d). In particular,

P+(T1) ≤ A+(1). 2Trivially, r(g;Td) ≤

√

2 for all continuous functions g : Td → R.

d

Proof. Let f ∈ As(d) be nonzero and bandlimited. Assume that supp( f) ⊆ [−a,a]d, for some a > 0. Let fλ(x) := f(λx), in which case fλ(ξ) = λ−d f(ξ/λ) and supp( fλ) ⊆ [−aλ,aλ]d. Note that, as long as 2aλ < 1, fλ can be seen as a function on Td [−12, 12]d. Set λ = r(nf), where n ∈ N is suﬃciently large so that 2aλ < 1, and deﬁne g(ξ) := s fλ(ξ). By the higher dimensional version of a result of Plancherel & Po´lya [13],

| g(k)| =

|f(λk)| < ∞,

- (6.2)


k∈Zd

k∈Zd

whence g ∈ Ps(Td) \ {0}. Moreover, r(g;Td) = r( fλ) = r(nf)r( f), and ks( g) ≤ n. Therefore

Ps(Td)2 ≤ r(g;Td)ks( g) ≤ r(f)r( f).

Since f ∈ As(d) was an arbitrary nonzero bandlimited function, this ﬁnishes the proof of the proposition.

Acknowledgements

F.G. acknowledges support from the Deutsche Forschungsgemeinschaft through the Collaborative Research Center 1060. D.O.S. is supported by the EPSRC New Investigator Award “Sharp Fourier Restriction Theory”, grant no. EP/T001364/1. J.P.G.R. acknowledges ﬁnancial support from the Deutscher Akademischer Austauschdienst. The authors are indebted to the anonymous referees for careful reading and valuable suggestions.

References

- [1] J. Bourgain, L. Clozel, and J.-P. Kahane, Principe d’Heisenberg et fonctions positives. Ann. Inst. Fourier 60 (2010), no. 4, 1215–1232.
- [2] E. Carneiro, M. B. Milinovich, and K. Soundararajan, Fourier optimization and prime gaps. Comment. Math. Helv. 94 (2019), no. 3, 533–568.
- [3] H. Cohn and N. Elkies, New upper bounds on sphere packings. I. Ann. of Math. (2) 157 (2003), no. 2, 689–714.
- [4] H. Cohn and F. Gonc¸alves, An optimal root uncertainty principle in twelve dimensions via modular forms. Inv. Math. 217 (2019), no. 3, 799–831.
- [5] H. Cohn, A. Kumar, S. D. Miller, D. Radchenko, and M. Viazovska, The sphere packing problem in dimension 24. Ann. Math. 185 (2017), no. 3, 1017–1033.
- [6] F. Gonc¸alves, D. Oliveira e Silva, and J. P. G. Ramos, New sign uncertainty principles. Preprint at arXiv:2003.10771.
- [7] F. Gon¸calves, D. Oliveira e Silva, and S. Steinerberger, Hermite polynomials, linear ﬂows on the torus, and an uncertainty principle for roots. J. Math. Anal. Appl. 451 (2017), no. 2, 678–711.
- [8] D. V. Gorbachev, V. I. Ivanov, and S. Yu. Tikhonov, Uncertainty principles for eventually constant sign bandlimited functions. Preprint at arXiv:1904.11328.
- [9] P. Jaming, Nazarov’s uncertainty principles in higher dimension. J. Approx. Theory 149 (2007), no. 1, 30–41.
- [10] E. Lieb and M. Loss, Analysis. Volume 14 of Graduate Studies in Mathematics (2001).
- [11] B. F. Logan, Extremal problems for positive-deﬁnite bandlimited functions. I. Eventually positive functions with zero integral. SIAM J. Math. Anal. 14 (1983), no. 2, 249–252.
- [12] B. F. Logan, Extremal problems for positive-deﬁnite bandlimited functions. II. Eventually negative functions. SIAM J. Math. Anal. 14 (1983), no. 2, 253–257.


- [13] M. Plancherel and G. P´lya, Fonctions enti´eres et inte´grales de fourier multiples. Comment. Math. Helv. 10 (1937), no. 1, 110–163.
- [14] L. Schwartz, Transformation de Laplace des distributions. Comm. S´em. Math. Univ. Lund [Medd. Lunds Univ. Mat. Sem.] 1952, (1952). Tome Suppl´ementaire, 196–206.
- [15] J. Vaaler, Some extremal functions in Fourier analysis. Bull. Amer. Math. Soc. (N.S.) 12 (1985), no. 2, 183–216.
- [16] M. Viazovska, The sphere packing problem in dimension 8. Ann. Math. 185 (2017), no. 3, 991– 1015.


Hausdorff Center for Mathematics, 53115 Bonn, Germany E-mail address: goncalve@math.uni-bonn.de

School of Mathematics, University of Birmingham, B15 2TT, England, UK E-mail address: d.oliveiraesilva@bham.ac.uk

Instituto Nacional de Matematica´ Pura e Aplicada, 22460-320 Rio de Janeiro, Brazil E-mail address: jpgramos@impa.br

