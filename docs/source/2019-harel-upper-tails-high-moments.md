---
type: source
kind: paper
title: Upper tails via high moments and entropic stability
authors: Matan Harel, Frank Mousset, Wojciech Samotij
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1904.08212v2
source_local: ../raw/2019-harel-upper-tails-high-moments.pdf
topic: general-knowledge
cites:
---

# arXiv:1904.08212v2[math.PR]13Apr2021

## UPPER TAILS VIA HIGH MOMENTS AND ENTROPIC STABILITY

MATAN HAREL, FRANK MOUSSET, AND WOJCIECH SAMOTIJ

Abstract. Suppose that X is a bounded-degree polynomial with nonnegative coeﬃcients on the p-biased discrete hypercube. Our main result gives sharp estimates on the logarithmic upper tail probability of X whenever an associated extremal problem satisﬁes a certain entropic stability property. We apply this result to solve two long-standing open problems in probabilistic combinatorics: the upper tail problem for the number of arithmetic progressions of a ﬁxed length in the p-random subset of the integers and the upper tail problem for the number of cliques of a ﬁxed size in the random graph Gn,p. We also make signiﬁcant progress on the upper tail problem for the number of copies of a ﬁxed regular graph H in Gn,p. To accommodate readers who are interested in learning the basic method, we include a short, self-contained solution to the upper tail problem for the number of triangles in Gn,p for all p = p(n) satisfying n−1 log n p 1.

Contents

- 1. Introduction 1
- 2. Triangles in random graphs 9
- 3. The main technical result: ‘entropic stability implies localisation’ 13
- 4. Arithmetic progressions in random sets of integers 19
- 5. Counting small subgraphs—a graph-theoretic interlude 25
- 6. Cliques in random graphs 34
- 7. Extensions to regular graphs 47
- 8. The Poisson regime 55
- 9. Beyond polynomials with nonnegative coeﬃcients 63
- 10. Concluding remarks 64 References 65


1. Introduction

Suppose that Y = (Y1,...,YN) is a sequence of independent Bernoulli random variables with mean p and that X = X(Y ) is an N-variate polynomial with nonnegative real coeﬃcients. Perhaps the simplest question that can be asked about the typical behaviour of X is whether it satisﬁes a law of large numbers, i.e., whether X → E[X] in probability as N → ∞. Once this is established, it is natural to ask for quantitative estimates of the probability of the event that X diﬀers from its mean by a signiﬁcant amount. In the special case where Y  → X(Y ) is a linear function, this problem is addressed by the classical theory of large deviations, see [14, 28]. This theory shows that, under mild conditions on the coeﬃcients of the linear function X and the assumptions p → 0 and Np → ∞,

P |X − E[X]| δ E[X] = e−(I(δ)+o(1))Np

Date: April 14, 2021. This research is supported in part by the Israel Science Foundation grants 1147/14 (FM and WS), 1028/16 (FM),

and 1145/18 (FM and WS), the ERC Starting Grant 633509 (FM) and 678520 (MH), and the Zuckerman Postdoctoral Fellowship Program (MH).

1

for an explicitly computable function I : (0,∞) → (0,∞]. However, there are many natural situations where one would like to consider nonlinear polynomials X(Y ), as in the following two examples. We use the notation N = {1,...,N}.

- Example 1.1 (Arithmetic progressions in random sets of integers). A k-term arithmetic progression is a sequence of k integers of the form a,a+b,a+2b,...,a+(k−1)b , where b > 0. We write

N p for the random subset of N obtained by including every element of N independently with probability p. Let XN,pk-AP denote the number of k-term arithmetic progressions in N p. Then XN,pk-AP can be considered as a polynomial with nonnegative coeﬃcients and degree k in the independent Ber(p) random variables Y1,...,YN, where Yi is the indicator variable of the event that i ∈ N p; explicitly,

XN,pk-AP =

b>0 a 1 a+(k−1)b N

k−1

i=0

Ya+ib.

We remark that, unlike [10] and several other works, we count only genuine arithmetic progressions (i.e., we do not consider degenerate progressions of the form (a,...,a)) and we count every progression only once (as opposed to counting (a1,a2,...,ak) and (ak,ak−1,...,a1) as two diﬀerent progressions).

- Example 1.2 (Subgraph counts in random graphs). Fix a nonempty graph H and let Xn,pH be the number of copies of H in the random graph Gn,p, that is, the number of subgraphs of Gn,p isomorphic to H. Then Xn,pH can be written as a polynomial with nonnegative coeﬃcients and degree eH in the N = n2 indicator random variables of the possible edges of Gn,p. More precisely, ﬁx an arbitrary bijection σn: n 2 → N (the precise choice is irrelevant) and, for every i ∈ N , let Yi be the indicator variable of the event that σn−1(i) is an edge in Gn,p. Then Y1,...,YN are independent Ber(p) random variables and


Xn,pH =

Yσ

n(e),

e∈E(H )

H ⊆Kn H ∼=H

where Kn denotes the complete graph on the vertex set n and ∼= denotes the isomorphism relation on graphs.

In this paper, we will always assume that δ is ﬁxed and p → 0 as N → ∞. The large deviation problem for the variables described above is signiﬁcantly more involved than

the linear case; in particular, the lower and upper tail probabilities—that is, P X (1 − δ)E[X] and P X (1 + δ)E[X] , respectively—exhibit dramatically diﬀerent behaviours. On the one hand, using a combination of Harris’s inequality [41] and Janson’s inequality [43], one can show that X = XN,pk-AP satisﬁes

1(δ) min{E[X],Np} P X (1 − δ)E[X] e−C

2(δ) min{E[X],Np} (1)

e−C

for some positive C1(δ) and C2(δ); similar bounds are available for X = Xn,pH .1 On the other hand, there are no comparably simple tools that allow one to easily obtain similar estimates on the logarithm of the upper tail probability. The standard concentration inequalities due to Azuma–Hoeﬀding [42], Talagrand [64], or Kim–Vu [52, 68] yield bounds that are far from tight in Examples 1.1 and 1.2. For a survey discussing these and other classical approaches to the ‘infamous upper tail’ problem, see [45].

Unlike the lower tail, the upper tail is susceptible to the inﬂuence of small structures whose appearance increases the value X atypically, a phenomenon that we refer to as localisation. For example, in the case of X = XN,pk-AP where k 3, a typical subset of size m = o(N) contains

1For more precise results, we refer the interested reader to [48, 54, 58, 71].

Θ N2(m/N)k = o(m2) k-term arithmetic progressions, whereas some very rare subsets (notably an interval of length m) can contain as many as Θ(m2) such progressions. The event that N p contains an interval of length Θ( E[X]) thus provides a lower bound on the upper tail probability. More precisely, P X (1 + δ)E[X] exp − O( E[X]log(1/p)) , which is signiﬁcantly larger than the lower tail probability (1) for most p. In order to properly analyse the upper tail event, one must account for these local eﬀects, which frequently requires understanding the peculiar combinatorial nature of the random variable X.

The last decade has seen the development of an increasingly powerful theory of ‘nonlinear large deviations’, which began with the work of Chatterjee–Dembo [18] and was further developed by Eldan [30], Cook–Dembo [24], Augeri [2, 3], and Cook–Dembo–Pham [25]. Whenever a general function f of i.i.d. random variables satisﬁes certain complexity and regularity conditions, these results can be used to express the upper tail probability P f (1 + δ)E[f] in terms of an associated variational problem. In the case where f is a polynomial with nonnegative coeﬃcients on the hypercube, this variational problem is able to capture the presence of localisation, if it occurs. In the two examples mentioned above, nonlinear large deviation theory gives tight control of the upper tail probabilities whenever p N−α for some constant α > 0. However, the best-known constant α is not optimal in both examples.

Our main contribution is a general method for proving sharp bounds on the upper tail probability of the polynomial X = X(Y ) in the presence of localisation. In many cases where localisation occurs, our approach can also give a coarse description of the tail event. At the heart of our method lies an adaptation of the classical moment argument of Janson, Oleszkiewicz, and Ruciński [44], which we use to formalise the intuition that the upper tail event is dominated by the appearance of near-minimisers of the combinatorial optimisation problem

ΦX(δ) = min |I|log(1/p) : I ⊆ N and E[X | Yi = 1 for all i ∈ I] (1 + δ)E[X] . (2) Roughly speaking, we say that I ⊆ N is a core if it is a feasible set for the above optimisation problem, its size is O ΦX(δ) , and it satisﬁes a certain natural rigidity condition that arises from requiring every element in the set to contribute a sizeable amount to the expectation. The constraints used to deﬁne a core are loosely analogous to the complexity conditions used in nonlinear large deviation theory; we will give a more precise deﬁnition of a core and discuss its relations to earlier work in more detail in Section 3.

We show that the upper tail probability is approximately equal to the probability of the appearance of a core. In particular, when the number of cores of size m is (1/p)o(m), a property we term entropic stability, then a union bound implies that −log P X (1 + δ)E[X] is well approximated by ΦX(δ). We will verify that the random variables XN,pk-AP and Xn,pH (for a large class of graphs H) satisfy the entropic stability condition under optimal, or nearly optimal, assumptions on p.2

One important caveat that we have ignored so far is that the upper tail exhibits localisation only when the expectation of X tends to inﬁnity suﬃciently quickly. In fact, if E[X] is of constant order, then, under relatively mild conditions, X converges in distribution to a Poisson random variable and no localisation occurs. We show that, for the two examples discussed above, the upper tail continues to have Poisson behaviour even when E[X] goes to inﬁnity suﬃciently slowly. In the cases of k-term arithmetic progressions in N p and cliques in Gn,p, our results for the Poisson and localised regimes cover almost the whole range of densities p → 0 with E[X] → ∞,

2We use the phrase entropic stability in a similar sense to the notion of stability in extremal combinatorics.

More precisely, we are considering situations where the probability that i∈I Yi = 1 for some minimiser I of (2) is asymptotically equal to the probability of appearance of one such minimiser—in other words, the energy of such

conﬁgurations (given by the number of elements involved) dominates over the entropy (that is, the number of such conﬁgurations). Then entropic stability means that the entropy term remains negligible even as we move away from true minimisers of (2) to sets that are merely close to being minimisers (the cores).

leaving the upper tail probability undetermined only at densities for which it is believed that the two behaviours coexist.

- 1.1. Arithmetic progressions in random sets of integers. Let X = XN,pk-AP denote the number of k-term arithmetic progressions in N p. It is not hard to see that E[X] = Θ(N2pk). Whenever this expectation vanishes, the upper tail event is commensurate with the probability of X 1, which can be controlled using Markov’s inequality. More generally, if E[X] is bounded, then it follows from standard techniques that X is asymptotically Poisson [7]; in this case, the large deviations of X are those of a Poisson random variable with mean E[X]. For the remainder of this section, we shall thus assume that E[X] → ∞, i.e., that pk/2 N−1.


Improving an earlier estimate due to Janson and Ruciński [47], Warnke [69] proved that under fairly general assumptions (in particular, for constant δ > 0 and all p bounded away from 1),

− log P(X (1 + δ)E[X]) = Θ min (1 + δ)log(1 + δ) − δ E[X], δ E[X]log(1/p) , (3)

where the constants implicit in the Θ-notation are independent of δ. Note that the two terms of the minimum correspond to the dominance of the Poisson and the localised regimes, respectively.

Since then, it has been an open problem to determine the missing constant factor in (3). Using the above-mentioned framework of Eldan [30], Bhattacharya, Ganguly, Shao, and Zhao [10] were able to do so in the range N−

1

12(k−1)(log N)O(1) pk/2 1. This was subsequently improved by Briët–Gopi [15] to the slightly wider range N−

1

12 (k−1)/2 (log N)O(1) pk/2 1, also using Eldan’s result. The two theorems below improve signiﬁcantly on these results and determine the precise rate of the upper tail for all N−1 pk/2 1, excepting the case pk/2 = Θ(N−1 log N). The ﬁrst result concerns the range where the minimum in (3) is δ E[X]log(1/p).

- Theorem 1.3. Let k 3 be an integer and let X = XN,pk-AP denote the number of k-term arithmetic progressions in N p. Then, for every ﬁxed positive constant δ and all p = p(N) satisfying N−1 log N pk/2 1,

lim

N→∞

−log P X (1 + δ)E[X] Npk/2 log(1/p)

= √

δ.

Observe that Theorem 1.3 shows that the upper tail probability is well approximated by the probability of appearance of an interval (or, more generally, an arithmetic progression) of length δN2pk in N p. Since each such interval contains approximately δ E[X] arithmetic progressions of length k, it is not hard to see that conditioning N p on the appearance of such a set will cause the upper tail event to occur with sizable probability. Conversely, our methods may be used to prove that the upper tail event is dominated by the appearance of some set of size (1 + o(1)) δN2pk that contains nearly δ E[X] arithmetic progressions of length k. It seems natural to guess that each such set is, in some sense, close to an arithmetic progression. However, this is not the case, as was shown by Green–Sisask [37]. We currently do not know a structural characterisation of the sets described above, which prevents us from proving a qualitative description of the upper tail event. For further discussion, we refer to Section 10.

The second result treats the complementary range N−1 pk/2 N−1 log N, where the upper tail has Poisson behaviour.

- Theorem 1.4. Let k 3 be an integer and let X = XN,pk-AP denote the number of k-term arithmetic progressions in N p. Then, for every ﬁxed positive constant δ and all p = p(N) satisfying N−1 pk/2 N−1 log N,


−log P X (1 + δ)E[X]

lim

= (1 + δ)log(1 + δ) − δ.

E[X]

N→∞

- 1.2. Subgraph counts in random graphs. Let X = XN,pH be the number of copies of a ﬁxed


graph H in Gn,p. Note that E[X] = Θ(nv

H). Since controlling the distribution of X for completely general graphs involves many technical diﬃculties (see for example [12, 66]), we will restrict our attention to connected, ∆-regular graphs H. If the expected value of X is bounded, then X converges to a Poisson random variable, as was shown independently by Bollobás [11] and by Karoński–Ruciński [49]. In view of this, for the remainder of this section, we shall assume that E[X] → ∞, i.e., that p∆/2 n−1. As mentioned before, we will also assume that p → 0; the case where p ∈ (0,1) is ﬁxed, which is fundamentally diﬀerent, was addressed in [21, 56, 59].

pe

H

The problem of controlling the upper tail of X has a long history. A sequence of papers [46, 53, 68], culminating in the work of Janson, Oleszkiewicz, and Ruciński [44], resulted in upper and lower bounds on the logarithmic upper tail probability that diﬀered by a multiplicative factor of log(1/p). In the case where H is a clique, Chatterjee [16] and DeMarco–Kahn [26] independently added the missing logarithmic factor to the upper bound, thus establishing the order of magnitude of the logarithmic upper tail probability. The theory of nonlinear large deviations (discussed above) provides a variational description of the dependence of the upper tail probability P(X (1 + δ)E[X]) on δ for a certain range of p → 0, as established in [3, 18, 24, 25, 30]; the strongest of these results require p n−1/(∆+1) for general graphs of maximal degree ∆ [24, 25], and p∆/2 n−1/2 for the case where H is a cycle [3, 24] (disregarding polylogarithmic factors). The associated variational problem was solved by Lubetzky–Zhao [57] when H is a clique and by Bhattacharya, Ganguly, Lubetzky, and Zhao [9] for general H. For a more detailed overview of these techniques, we refer the reader to the book of Chatterjee [17].

The solution to the variational problem is expressed in terms of the independence polynomial of a graph. For any H, deﬁne PH(x) = k ik(H)xk, where ik(H) is the number of independent sets of H of size k, and let θ = θ(δ) be the unique positive solution to PH(θ) = 1 + δ.3 There are two constructions that yield lower bounds for the upper tail probability (see Figure 1). In both cases, one plants a ‘small’ subgraph whose presence ensures that Gn,p contains (1 + δ)E[X] copies of H with good probability. The ﬁrst of these subgraphs is a clique on δ1/v

np∆/2 vertices (as in the left side of the ﬁgure), which contains the extra δ E[X] copies of H required by the upper tail event (up to lower-order corrections). The second subgraph (which is often called a ‘hub’) is a complete bipartite graph with parts of size θnp∆ and n − θnp∆, respectively (as in the right side of the ﬁgure); since we are implicitly assuming that θnp∆ is an integer, rounding errors play a signiﬁcant role here unless np∆ 1. A short calculation shows that the expected number of copies of H which intersect this graph is approximately δ E[X] and thus the actual number of such copies is almost δ E[X] with good probability. In both cases, the complement of the planted subgraph typically contains approximately E[X] copies of H. Formalising this argument, one obtains the two lower bounds

H

2/vH+o(1))n2p∆ and P X (1 + δ)E[X] p(θ+o(1))n

2p∆,

P X (1 + δ)E[X] p(δ

which correspond to planting the clique and the complete bipartite graph, respectively. (Recall that the latter bound is valid only when np∆ 1.)

Our main result is that, when H is not bipartite, one of the above bounds is tight in nearly the whole range of densities. When H is bipartite, we prove tight bounds on the logarithmic upper tail probability only when p∆/2 n−1/2−o(1).

- Theorem 1.5. Let ∆ 2 be an integer, let H be a connected, nonbipartite, ∆-regular graph, and let X = XN,pH denote the number of copies of H in Gn,p. Then for every ﬁxed positive constant δ


3We note that i0(H) = 1 for every graph H, so that, for example, PKr(x) = 1 + rx.

n np∆/2

δ1/v

H

θnp∆

n − θnp∆

Figure 1. The two constructions giving lower bounds for the upper tail probability of X = Xn,pH .

2

and all p = p(n) satisfying n−1(log n)∆v

H p∆/2 1,

δ2/v

/2 if np∆ → 0, min {δ2/v

−log P X (1 + δ)E[X] n2p∆ log(1/p)

H

lim

=

/2,θ} if np∆ → ∞,

n→∞

H

where θ is the unique positive solution to PH(θ) = 1 + δ. Additionally, if p∆/2 n−1/2−o(1), then the assumption that H is nonbipartite is not necessary.

We note that the theorem leaves open the case where np∆ → c ∈ (0,∞). In this regime, the explicit dependence of the upper tail probability on δ involves various integrality conditions and is therefore quite complicated. In the next subsection, we explicitly treat this regime when H is a clique. The assumption of nonbipartiteness is not phenomenological, but only technical. The aforementioned entropic stability condition, which plays a crucial role in our proof, ceases to hold when H is bipartite as soon as p∆/2 n−1/2−Θ(1), see Section 10.

Our next result concerns the Poisson regime of the upper tail.

- Theorem 1.6. Let ∆ 2 be an integer, let H be a connected, ∆-regular graph, and let X = Xn,pH denote the number of copies of H in Gn,p. Then, for every ﬁxed positive constant δ and all


1

p = p(n) satisfying n−1 p∆/2 n−1(log n)

vH−2 , lim

−log P X (1 + δ)E[X]

= (1 + δ)log(1 + δ) − δ.

E[X]

n→∞

In the case where H is a clique, DeMarco and Kahn [26] proved that the logarithmic upper tail probability is of order E[X] throughout the regime covered by Theorem 1.6. For other ∆-regular graphs H, the analogous fact was known only in the range n−1 p∆/2 n−1(log n)cH, for some positive constant cH < 1/(vH − 2), see [46, 62, 67, 70].

Finally, we point out that the powers of the logarithms in the assumptions of Theorems 1.5 and 1.6 do not match. After a preprint of this paper appeared, Basak and Basu [8] combined a generalised notion of entropic stability with a more reﬁned version of the approach used in this paper to prove tight bounds on the logarithmic upper tail probability for the subgraph count of any ∆-regular graph H in the entire localised regime (see Section 3 for a more detailed discussion). Speciﬁcally, they remove the assumption that H is nonbipartite, and improve the assumed lower bound on the density p in Theorem 1.5 to n−1(log n)1/(vH−2) p∆/2, thus matching the assumptions of Theorem 1.6.

- 1.3. Clique counts in random graphs. We now consider the case of X = Xn,pH where H is a clique on r 3 vertices. Thanks to the simpler structure of these graphs, we are able to prove signiﬁcantly stronger results in this setting. First, we are able to determine the explicit dependence of the logarithmic upper tail probability on δ even when npr−1 → c ∈ (0,∞). Moreover, we


1 r−2

r−1

resolve the upper tail problem for the optimal range of densities n−1(log n)

2 1,

p

complementing the range covered by Theorem 1.6. Finally, we give a structural description of Gn,p conditioned on the upper tail event.

In order to formally state the theorem, it is convenient to deﬁne

δ(1 − x) 2/r 2

1 r−1

xδc/r + {xδc/r}

ψr(δ,c,x) =

, (4) where δ and c are nonnegative reals, x ∈ [0,1], and {a} denotes the fractional part of a, and

+

c

ϕr(δ,c) = min

ψr(δ,c,x). (5)

x∈[0,1]

For an intuitive explanation of the combinatorial meaning of these deﬁnitions, we refer to the discussion at the beginning of Section 6. An easy convexity argument shows that the minimum in the deﬁnition of ϕr is attained when x ∈ {0,r δc/r /(δc),1}, see Lemma 6.1. This leads to the explicit formula

δ2/r 2

δc/r + {δc/r}1/(r−1) c

(r{δc/r}/c)2/r 2

δc/r c

ϕr(δ,c) = min

+

,

,

.

- Theorem 1.7. Let r 3 be an integer and let X = XK

n,pr denote the number of r-vertex cliques in the random graph Gn,p. Then, for every ﬁxed positive constant δ and all p = p(n) satisfying n−1(log n)

1 r−2

p

r−1

2 1,

lim

n→∞

−log P X (1 + δ)E[X] n2pr−1 log(1/p)

=

 



δ2/r/2 if npr−1 → 0, ϕr(δ,c) if npr−1 → c ∈ (0,∞), min δ2/r/2,δ/r if npr−1 → ∞.

Our next result describes the typical structure of the random graph Gn,p conditioned upon the upper tail event. We write Gn,p[U] for the subgraph of Gn,p induced by U and e(A,B) for the number of edges in Gn,p with one endpoint in A and another in B. Deﬁne the following three events:

- (i) Let UT(δ) be the upper tail event {X (1 + δ)E[X]}.
- (ii) Let Cliqueε(x) be the event that Gn,p contains a set U ⊆ n of size at least (1 − ε)x1/rnp(r−1)/2 such that Gn,p[U] has minimum degree at least (1 − ε)|U|.
- (iii) Let Hubε(x) be the event that Gn,p contains a set U ⊆ n such that at least (1−ε)|U|  vertices in U have degree at least (1 − ε)n and


e(U, n \ U) (1 − ε)n xnpr−1/r + {xnpr−1/r}

1 r−1

. Observe that Cliqueε(0) and Hubε(0) hold vacuously.

- Theorem 1.8. Let r 3 be an integer and let δ, ε, and c be ﬁxed positive constants. The


1 r−2

r−1

following holds for all p = p(n) satisfying n−1(log n)

2 1.

p

- (i) If npr−1 → 0, then P Cliqueε(δ) | UT(δ) → 1.
- (ii) If npr−1 → c, then, letting x∗ = r δc/r /(δc),


 

Cliqueε δ(1 − x) ∩ Hubε(δx) | UT(δ)

 → 1,

P

x∈{0,x∗,1}

Moreover, if x  → ψr(δ,c,x) has a unique minimiser x ∈ {0,x∗,1}, then

P Cliqueε δ(1 − x) ∩ Hubε(δx) | UT(δ) → 1.

|Clique(δ)<br><br>| |
|---|
<br><br>Hub(δ)<br><br>| |
|---|
<br><br>Clique(δx∗) ∩ Hub(δ(1 − x∗))|
|---|


12

9

6

c

3

0

0 1 2 3 4 δ

Figure 2. Asymptotic structure of Gn,p conditioned upon the upper tail event UT(δ) = {XK

n,p3]} when np2 → c as n → ∞. In this conditional model, it is highly probable that we observe either Cliqueε(δ), Hubε(δ), or Cliqueε(δx∗) ∩ Hubε((1 − δ)x∗) with x∗ = 3 δc/3 /(δc) ∈ (0,1), depending on the values of δ and c (all regions are open).

n,p3 (1 + δ)E[XK

- (iii) If npr−1 → ∞, then


P Cliqueε(δ) ∪ Hubε(δ) | UT(δ) → 1. Moreover,

1 if δ2/r/2 < δ/r, 0 if δ2/r/2 > δ/r.

P Cliqueε(δ) | UT(δ) →

Note that Theorem 1.8 remains agnostic about the exact structure of the conditional model in the case where there are multiple minimisers to x  → ψr(δ,npr−1,x). However, it is not too diﬃcult to show that for every r, the set of (δ,c) ∈ (0,∞)2 for which x  → ψr(δ,c,x) has multiple minimisers has Lebesgue measure zero. Figure 2 gives a graphical representation of the assertion of Theorem 1.8 in the case where r = 3 and np2 → c. As the ﬁgure illustrates, the conditional model undergoes inﬁnitely many phase transitions if δ2/3/2 > δ/3 (that is, δ < 3.375) and no phase transition at all if δ2/3/2 < δ/3.

- 1.4. Organisation of the paper. In Section 2, we present a short and self-contained solution


to the upper tail problem for triangle counts in Gn,p. This section is somewhat redundant, since its content is just a special case of the more general Proposition 6.4. We include it in order to demonstrate our method in a simple setting that conveniently avoids many technical complications that arise in the general case.

Section 3 introduces a concentration inequality that gives a general condition under which the logarithmic upper tail probability can be approximated by ΦX(δ), the solution to the optimisation problem (2).

In Section 4, we use the inequality developed in Section 3 to determine the asymptotics of the

logarithmic upper tail probability of XN,pk-AP in the complete range of densities where localisation occurs. After collecting some graph-theoretic tools in Section 5, we study the localised regime of the upper tails of XK

n,pr and Xn,pH for connected, ∆-regular graphs H in Sections 6 and 7, respectively. We note that the three Sections 4, 6, and 7 are logically independent and may be read in any order; however, both Sections 6 and 7 rely on the tools of Section 5.

In Section 8, we prove various results related to the Poisson regime; in particular, we give the proofs of Theorems 1.4 and 1.6. The arguments we use there do not rely on the methods developed in Section 3, but rather on explicit calculations of high factorial moments. Section 9 contains a brief discussion on extending the result from Section 3 to the more general case of nonnegative random variables on the hypercube. Finally, in Section 10 we make some concluding remarks and discuss open problems.

- 1.5. Notation. Before ending the introduction, we collect some notation which will be used


throughout the paper. We write Kr for the complete graph on r vertices and Ks,t for the complete bipartite graph with parts of size s and t. For any graph G, let V (G) and E(G) denote the vertex and edge sets of G, respectively, and set vG = |V (G)| and eG = |E(G)|. For two graphs J and G, we let N(J,G) be the number of copies of J in G, and Emb(J,G) be the set of embeddings of J into G—i.e., injective maps from V (J) to V (G) that map edges of J to edges of G. For an edge uv ∈ E(G), we also let N(J,G;uv) and Emb(J,G;uv) be the number of copies of J that contain the edge uv, and the set of embeddings that map an edge of J to uv, respectively. Finally, for a subset I of N , we let YI = i∈I Yi, and EI[X] = E[X | YI = 1]. If subsets I ⊆ N can be identiﬁed with subgraphs G ⊆ Kn, as in Example 1.2, we will write EG[X] instead of EI[X].

2. Triangles in random graphs

Assume that n−1 log n p 1 and let X denote the number of triangles in Gn,p. Using the shorthand notation EG[X] = E[X | G ⊆ Gn,p], we deﬁne, for each positive δ,

ΦX(δ) = min eG log(1/p) : G ⊆ Kn and EG[X] (1 + δ)E[X] . (6)

Note that this agrees with the deﬁnition (2). The goal of this section is to prove that, for every ﬁxed positive ε and all large enough n,

(1 − ε)ΦX(δ − ε) −log P X (1 + δ)E[X] (1 + ε)ΦX(δ + ε). (7)

At this point, we do not address the issue of evaluating ΦX(δ). For the sake of completeness, let us mention that a special case of a more general result of Lubetzky–Zhao [57] is that, when n−1 p 1,

δ2/3/2 if np2 → 0 min δ/3,δ2/3/2 if np2 → ∞.

ΦX(δ) n2p2 log(1/p)

lim

=

n→∞

In Section 6, we shall ﬁll in the gap at p = Θ(n−1/2) to obtain an asymptotic formula for ΦX(δ) in the full range of interest.

We now give a proof of (7), where we may assume without loss of generality that ε δ/10. All statements that we make in this section should be understood to hold only for suﬃciently large n. We start with some easy observations. First, for every graph G with O(1) edges, we have EG[X] − E[X] = O(1 + np2) (δ − 2ε)E[X], and so ΦX(δ − 2ε) log(1/p) 1. Second, the condition in (6) is satisﬁed when G is a clique on (1 + δ)1/3np vertices, and therefore ΦX(δ − ε) (1 + δ)2/3n2p2 log(1/p)/2.

The easier of the two inequalities in (7) is the upper bound. To prove it, let G be a graph attaining the minimum in the deﬁnition of ΦX(δ + ε) and let PG(·) = P(· | G ⊆ Gn,p). Since X

never exceeds n3 , (1 + δ + ε)E[X] EG[X]

n 3

PG X (1 + δ)E[X] + (1 + δ)E[X], and so

n 3

= εp3. Hence,

PG X (1 + δ)E[X] εE[X]/

−log P X (1 + δ)E[X] −log P(G ⊆ Gn,p) · PG X (1 + δ)E[X] eG log(1/p) + log(1/εp3). Since eG log(1/p) = ΦX(δ + ε) ΦX(δ − 2ε) log(1/p), this establishes the lower bound in (7).

We now turn to proving the lower bound. Let C = C(ε,δ) denote a suﬃciently large positive constant. We call a graph G ⊆ Kn a seed if

- (S1) EG[X] (1 + δ − ε)E[X] and
- (S2) eG Cn2p2 log(1/p). We make the following claim:


Claim 2.1. P X (1 + δ)E[X] (1 + ε)P Gn,p contains a seed .

- Remark 2.2. Given this claim, one may be tempted to simply apply the union bound over all seeds. Using such a strategy, one would ﬁnd that


Claim 2.1

P X (1 + δ)E[X]

(1 + ε)P Gn,p contains a seed (1 + ε)

∞

pm · |{G ⊆ Kn : G is a seed with m edges}|, (8)

m=mmin

where mmin = ΦX(δ − ε)/log(1/p) is the minimal number of edges in a seed. Unfortunately, such a strategy is bound to fail, as there are far too many seeds. To see this, we observe that if G satisﬁes (S1), then so does any supergraph of G. In particular, if we take a seed with mmin edges and add an arbitrary set of Kmmin edges (where K is a large constant), the resulting graph remains a seed. Therefore, we can (rather loosely) bound the number of seeds with m˜ = (K + 1)mmin edges from below:

1 3(1 + δ)2/3Kp2

Kmmin

n 2 − mmin

|{G ⊆ Kn : G is a seed with m˜ edges}|

,

Kmmin

using the bound xy (x/2y)y for any y < x/2 and mmin (1 + δ)2/3n2p2/2. If we choose K to be large enough, we may conclude that

|{G ⊆ Kn : G is a seed with m˜ edges| (1/p)3m/˜ 2, for all large enough n. This shows that the m˜ th term of the ﬁnal sum in (8) is arbitrarily large, making the entire approach fruitless.

From Remark 2.2, it is clear that seeds may include ‘extraneous’ edges that have no structural role in the upper tail event. We wish to consider more constrained structures which exclude constructions like the one outlined above. To that end, we call a graph G∗ ⊆ Kn a core if

(C1) EG∗[X] (1 + δ − 2ε)E[X], (C2) eG∗ Cn2p2 log(1/p), and (C3) mine∈E(G∗) EG∗[X] − EG∗\e[X] εE[X]/ Cn2p2 log(1/p) .

Condition (C3) requires that every edge contributed meaningfully to the expectation, and thus excludes the pathological seeds described above.

- Claim 2.3. Every seed contains a core.


Finally, we claim that the additional constraint (C3) allows us to get a very strong bound on the number of cores with a given number of edges, as it ensures that either the product of the degrees of the endpoints of any edge in G∗ must be nearly as large as eG∗, or the sum of these degrees is nearly linear in n (note that the former condition holds when G∗ is a clique, and the latter when G∗ is a hub). This, in turn, implies that the number of cores with a given set of vertices and m edges is exp(O(mlog log(1/p)). Once we show that the number of choices for the vertex set of a core with m edges is (1/p)o(m), we prove the following claim.

- Claim 2.4. For every m, there are at most (1/p)εm cores with exactly m edges.


As will be discussed in Section 3, we refer to the property described in Claim 2.4 as entropic stability.

Let us show how these three claims imply the lower bound in (7):

P X (1 + δ)E[X]

Claim 2.1

(1 + ε)P Gn,p contains a seed

- Claim 2.3 (1 + ε)P Gn,p contains a core

(1 + ε)

∞

m=0

pm · |{G∗ ⊆ Kn : G∗ is a core with m edges}|

- Claim 2.4 (1 + ε)


∞

p(1−ε)m,

m=mmin

where mmin is the minimal number of edges in a core. Since (C1) implies that ΦX(δ − 2ε) mmin · log(1/p), the assumption p 1 yields

P X (1 + δ)E[X] (1 + 2ε)exp − (1 − ε)ΦX(δ − 2ε) . Finally, as ΦX(δ − 2ε) 1, we obtain

−log P X (1 + δ)E[X] (1 − 2ε)ΦX(δ − 2ε), thus proving (7) with 2ε instead of ε.

- Remark 2.5. Conditions (S2) and (C2) require both seeds and cores to have no more than


Cn2p2 log(1/p) edges, forcing us to consider graphs which are larger than the minimiser of ΦX(δ) by a multiplicative factor of log(1/p). This is optimal in the following sense. On the one hand, replacing log(1/p) with a larger function would weaken the conclusion of Claim 2.1 and make Claim 2.4 hold only for a smaller range of densities p. On the other hand, if we could replace log(1/p) by (p) = o(log(1/p)) without altering the validity of Claim 2.1, then Claim 2.4 (with an appropriately adjusted deﬁnition of a core) would hold for any p (p)/n; this would imply an upper bound on the upper tail probability that is stronger than the lower bound proven in Theorem 1.6 for (p)/n p log n/n.

Proof of Claim 2.1. We reﬁne a classical argument due to Janson, Oleszkiewicz, and Ruciński [44]. Let Z be the indicator random variable of the event that Gn,p does not contain a seed and let

= (C/3)n2p2 log(1/p) . Since XZ 0 and Z = Z, Markov’s inequality gives

E[X Z] (1 + δ) E[X]

P X (1+δ)E[X] and Gn,p contains no seed = P XZ (1+δ)E[X]

. (9)

We write X = T YT, where the sum ranges over all triangles T in Kn and YT is the indicator random variable of the event that T is contained in Gn,p. For every subgraph G ⊆ Kn, let ZG be the indicator random variable of the event that G ∩ Gn,p does not contain a seed. Observe that

ZG ZG whenever G ⊆ G . In particular, since Z = ZK

, we have, for every k ∈ , E[XkZ] =

n

E[YT

k · Z]

1 ···YT

T1,...,Tk

E[YT

1∪···∪Tk]

1 ···YT

k · ZT

T1,...,Tk

E[YT

1∪···∪Tk−1] ·

E[YT

1∪···∪Tk−1 = 1],

1 ···YT

k−1 · ZT

k | YT

k−1 · ZT

...YT

1

T1,...,Tk−1

Tk

where we can let the ﬁrst sum in the last line range only over sequences T1,...,Tk−1 for which the event YT

1∪···∪Tk−1 = 1 has positive probability. This is equivalent to saying that the graph T1∪···∪Tk−1 does not contain a seed and thus YT

1 ···YT

k−1 · ZT

. Moreover, since eT

1∪···∪Tk−1 = YT

1 ···YT

k−1·ZT

1 ···YT

k−1

1∪···∪Tk−1 3(k − 1) 3( − 1) Cn2p2 log(1/p),

E[YT

= 1] = ET

1∪···∪Tk−1[X] < (1 + δ − ε)E[X],

k | YT

#### ...YT

1

k−1

Tk

as otherwise T1 ∪ ··· ∪ Tk−1 would be a seed, see (S1) and (S2). Therefore,

E[YT

1∪···∪Tk] < (1 + δ − ε)E[X] ·

E[YT

1∪···∪Tk−1]

1 ···YT

k · ZT

1 ···YT

k−1 · ZT

T1,...,Tk

T1,...,Tk−1

and it follows by induction that E[X Z] < (1 + δ − ε) E[X] . Substituting this inequality into (9) gives

1 + δ − ε 1 + δ

P X (1 + δ)E[X] and Gn,p contains no seed

. Since the probability that Gn,p contains a seed is at least e−Φ

X(δ−ε), the probability that Gn,p contains a given seed of smallest size, the bounds 1 ΦX(δ − ε) (1 + δ)2/3n2p2 log(1/p)/2 imply that, for all suﬃciently large n,

(C/3)n2p2 log(1/p)

1 + δ − ε 1 + δ

1 + δ − ε 1 + δ

X(δ−ε) εP Gn,p contains a seed whenever the constant C is suﬃciently large4. This implies the assertion of the claim.

εe−Φ

- Proof of Claim 2.3. Let G be a seed. Deﬁne a sequence G = G0 ⊇ G1 ⊇ ··· ⊇ Gs = G∗ of subgraphs of G by repeatedly setting Gi+1 = Gi \ e for some edge e ∈ Gi such that

EG

i −EG

i\e[X] < εE[X]/ Cn2p2 log(1/p) , as long as such an edge e exists. By construction, G∗ clearly satisﬁes (C3). Since eG∗ eG Cn2p2 log(1/p), we see that (C2) holds as well. Finally, as s eG Cn2p2 log(1/p), we have

EG[X] − EG∗[X] =

s−1

i=0

EG

i

[X] − EG

i+1

[X] < εE[X].

Since G is a seed, EG[X] (1 + δ − ε)E[X] and we obtain (C1).

- Proof of Claim 2.4. We bound the number of cores with m edges from above. This number is zero whenever m > Cn2p2 log(1/p), by (C2). We may thus assume that m Cn2p2 log(1/p). Given a core G∗, we denote by AG∗ the set of vertices of G∗ with degree at least εnp/ 30C log(1/p) and by BG∗ ⊆ AG∗ the set of vertices of G∗ with degree at least εn/ 30C log(1/p) , where the degree is taken in G∗. Since G∗ has m edges,


60Cmlog(1/p) εnp

60Cmlog(1/p) εn

|AG∗| a :=

and |BG∗| b :=

.

The key observation, which we will now verify, is that every edge of G∗ is either contained in AG∗ or has an endpoint in BG∗, see Figure 3 for an illustration. To see this, consider some edge

4We note that the requirement for C to be large is only used here.

AG∗ BG∗ G∗ e

G∗

Figure 3. Left: The sets AG∗ and BG∗ of high-degree vertices capture the edges of the core. Right: Three diﬀerent types of triangles containing an edge e in the core G∗.

e ∈ E(G∗). For every nonempty graph F ⊆ K3, let N(F,G∗;e) denote the number of copies of F in G∗ that contain e. By considering how the n − 2 triangles in Kn that contain e intersect G∗ (see Figure 3), one can see that

EG∗[X] − EG∗\e[X] N(K3,G∗;e) + N(K1,2,G∗;e) · p + np2 · (1 − p). Using EG∗[X] − EG∗\e[X] εE[X]/(Cn2p2 log(1/p)) and E[X] (1 − o(1))n3p3/6, we thus get

εnp 7C log(1/p)

N(K3,G∗;e) + N(K1,2,G∗;e) · p + np2. Since p 1 implies that np2 np/log(1/p), we ﬁnd that either

εnp 15C log(1/p)

εn 15C log(1/p)

N(K3,G∗;e)

or N(K1,2,G∗;e)

. (10)

Since N(K3,G∗;uv) min{degG∗ u,degG∗ v} and N(K1,2,G∗;uv) degG∗ u+degG∗ v, the ﬁrst inequality in (10) implies that e is contained in AG∗ whereas the second inequality implies that e has an endpoint in BG∗, as claimed.

Our key observation implies that for ﬁxed sets B ⊆ A ⊆ n with |A| = a and |B| = b, there are at most a

2/2+bn

m cores G∗ with m edges that satisfy AG∗ ⊆ A and BG∗ ⊆ B. We can thus (generously) upper bound the number of cores with m edges by

a2/2 + bn m

n a

n b

.

Recalling the inequality xy (ex/y)y, valid for all nonnegative integers x and y, we may conclude that the number of cores with m edges is at most

e(60C)2m log(1/p) 2 2ε2n2p2

m

e60C log(1/p) ε

120Cm log(1/p) εnp

+

·

.

n

Since p n−1 log n, the ﬁrst factor is at most eo(mlog(1/p)). Using m Cn2p2 log(1/p), the second factor is at most eO(mlog log(1/p)) = eo(mlog(1/p)). This shows that the number of cores with m edges is indeed at most (1/p)εm, as claimed.

3. The main technical result: ‘entropic stability implies localisation’

The goal of this section is to state a general result that allows one, in many cases of interest, to reduce the problem of determining the precise asymptotics of the logarithmic upper tail probability of a polynomial (with nonnegative coeﬃcients) of independent Bernoulli random variables to a

counting problem. Since the main technical lemmas also apply to non-product measures on the hypercube, we phrase the basic deﬁnitions in this broader context.

We denote by Y a random variable taking values in the discrete N-dimensional cube {0,1}N and by X = X(Y ) a real-valued, increasing function of Y with positive expectation. Given a subset I ⊆ N , we write YI = i∈I Yi for the indicator random variable of the event

Yi = 1 for all i ∈ I . Using the shorthand notation EI[X] = E[X | YI = 1],5 we deﬁne a function ΦX : R → R 0 ∪ {∞} by6

ΦX(δ) = min − log P(YI = 1) : I ⊆ N and EI[X] (1 + δ)E[X] . (11) It is easy to see that ΦX is a nondecreasing function satisfying ΦX(δ) > 0 for all δ > 0. We say that a function X : {0,1}N → R 0 is a polynomial with nonnegative coeﬃcients and degree at most d if it admits a representation X = I⊆ N αIYI, where each coeﬃcient αI is nonnegative and αI = 0 whenever |I| > d.

Let I be a collection of subsets I ⊂ N . Given ε > 0 and p > 0, we say that I is an entropically stable family (with respect to ε and p) if, for every integer m,

|{I ∈ I : |I| = m}| (1/p)εm/2. For the sake of brevity, we will suppress the dependence of this property on ε and p. The following statement is the main technical result of our work.

- Theorem 3.1. For every positive integer d and all positive real numbers ε and δ with ε < 1/2, there is a positive K = K(d,ε,δ) such that the following holds. Let Y be a sequence of N independent Ber(p) random variables for some p ∈ (0,1 − ε] and let X = X(Y ) be a nonzero


polynomial with nonnegative coeﬃcients and degree at most d such that ΦX(δ − ε) K log(1/p). Denote by I∗ the collection of all subsets I ⊆ N satisfying

(C1) EI[X] (1 + δ − ε)E[X], (C2) |I| K · ΦX(δ + ε), and (C3) mini∈I EI[X] − EI\{i}[X] E[X]/ K · ΦX(δ + ε) ,

and assume I∗ is an entropically stable family. Then

(1 − ε)ΦX(δ − ε) −log P X (1 + δ)E[X] (1 + ε)ΦX(δ + ε) (12) and, writing J ∗ for the collection of those I ∈ I∗ with −log P(YI = 1) (1 + ε)ΦX(δ + ε),

P X (1 + δ)E[X] and YI = 0 for all I ∈ J ∗ εP X (1 + δ)E[X] . (13)

- Remark 3.2. Observe that (12) gives tight bounds on the logarithmic upper tail probability of


X, provided that ΦX(δ) = I(δ) + o(1) f(N,p) for a continuous, positive function I and some function f. Equation (13) states that the upper tail event is (almost) contained in the event that YI = 1 for some I ∈ J ∗; note that each such I is a near-minimiser of ΦX(δ − ε). In some cases, it is possible to classify these near-minimisers and thereby obtain a rough structural characterisation of the upper tail event.

- Remark 3.3. The assumption ΦX(δ − ε) K log(1/p) means that conditioning on YI = 1 for any constant-size subset I ⊆ N cannot increase the expected value of X by more than (δ − ε)E[X]; it is very easy to verify this for the applications we have in mind. The more onerous task is verifying that I∗ is an entropically stable family. In fact, a large part of this paper is dedicated to counting cores (as we call the elements of I∗). Frequently, there are very few minimisers of


ΦX(δ), for every δ > 0. Entropic stability quantiﬁes the notion that there are few near-minimisers as well.

- 5Strictly speaking, EI[X] is well deﬁned only if P(YI = 1) > 0. However, the value of EI[X] for sets I with P(YI = 1) = 0 does not aﬀect any of our statements.
- 6We use the standard convention that min ∅ = ∞.


- Remark 3.4. In the following sections, we will compute the logarithmic upper tail probabilities

in various settings by estimating the function ΦX and verifying that the random variable X in question satisﬁes the assumptions of Theorem 3.1. As will be seen in the proof of Theorem 3.1, entropic stability implies that

− log P(YI∗ = 1 for some I∗ ∈ I∗) (1 − ε/2) · ΦX(δ − ε). (14) However, there are many natural contexts where the entropic stability assumption fails despite the fact that (14) remains true. For example, when H = C4, then every copy of the complete bipartite graph K2,cn2p2 in Kn is a core, provided that c is large enough. There are cn n2p2 such copies in Kn and cn n2p2 is larger than (1/p)Ω(n

2p2) when p n−1/2−ξ for some small ξ > 0. In order to study such scenarios, one may search out a weaker condition which still implies (14), and employ Theorem 3.1 mutatis mutandis. One such modiﬁcation is to allow the number of cores with m edges to be as large as (1/p)m−mmin+o(mmin); such a generalisation was introduced in the work of Basak–Basu [8].

- Remark 3.5. Let M({0,1}N) be the set of measures on the N-dimensional hypercube. For any random variable X = X(Y ) deﬁned on the p-biased hypercube, it is possible to give an abstract description of the probability of the upper tail event via the Gibbs variational principle, which states that


DKL(ν µp), where µp is the product of N Bernoulli measures of mean p, DKL(· ·) is the relative entropy DKL(ν µ) =

−log P(X (1 + δ)E[X]) inf

ν∈MXδ

ν(y) µ(y)

ν(y)log

,

y∈{0,1}N

and

MXδ := ν ∈ M({0,1}N) :

X(y)ν(y) (1 + δ)E[X] .

y∈{0,1}N

The naïve mean ﬁeld approximation holds for the upper tail of X if one can replace the inﬁmum over all measures in MXδ by an inﬁmum over all product measures in MXδ , while incurring only lower order errors.

The seminal work of Chatterjee–Dembo [17], further developed by Eldan [30] and Augeri [3], provides very general suﬃcient conditions that imply the naïve mean ﬁeld approximation for a general function f of Bernoulli random variables, stated in terms of the ‘smoothness’ of f and the ‘complexity’ of its gradient. Although the various works consider diﬀerent notions of low complexity, all of them seem to imply the heuristic statement that the set of all directions of the gradient of f is an extremely sparse subset of the (N − 1)-dimensional sphere. An alternate approach to the naïve mean ﬁeld approximation is used by Cook–Dembo [24], which specializes to the case of subgraph counts in Erdős–Rényi random graphs. Instead of appealing to gradient complexity bounds, they construct an eﬃcient covering of (most of) the hypercube by convex sets on which the subgraph counts are nearly constant, in the spirit of the regularity-based approach of Chatterjee–Varadhan [21].

Although its formulation is rather diﬀerent, Theorem 3.1 can also be considered in the context of the naïve mean ﬁeld approximation, coverings of the hypercube, and low-complexity gradients. Given a subset I ⊆ N , we deﬁne a product measure νI by

1 if i ∈ I, p otherwise.

νI(Yi = 1) =

A straightforward computation shows that DKL(νI µp) = |I|log(1/p), and so ΦX(δ) = inf DKL(νI µp) : νI ∈ MXδ .

In these terms, Theorem 3.1 shows that, if I∗ an entropically stable family, then a particularly simple form of the naïve mean ﬁeld approximation holds: one must only consider product measures that assign edges probability p or 1. Our adaptation of the high moment argument of Janson, Oleszkiewicz, and Ruciński, used in Lemma 3.7, constructs a covering of (most of) the upper tail event by a family I of small subsets I with νI ∈ MXδ . The extraction of cores from these subsets corresponds to identifying the directions in which the possible partial derivatives are large; in this perspective, entropic stability is analogous to the sparseness property that is encoded by the low-complexity gradient condition.

The ﬁnal stipulation of Theorem 9.1 gives a structural description of the measure conditioned on the upper tail event. More speciﬁcally, a sample from the conditional measure will contain an element of J ∗ with high probability. Working from the naïve mean-ﬁeld approximation, one may consider the more subtle question of the exact relationship between the conditional measure and the family of product measures in MXδ that attain the minimal relative entropy from µp. The work of Eldan–Gross [31] shows that, under certain conditions, the conditional measure is close to a mixture of such product measures, in the sense of optimal transport; Austin [4] proves similar results for a broader class of measures (not necessarily on the hypercube).

The upper bound on −log P X (1 + δ)E[X] stated in (12) will follow easily from the following simple lemma.

- Lemma 3.6. Let Y be a random variable taking values in {0,1}N and let X = X(Y ) be a real-valued function of Y . Suppose that E[X] > 0 and that X M always. Then for all positive ε and δ,

−log P X (1 + δ)E[X] ΦX(δ + ε) + log

M εE[X]

.

Proof. Let t = (1 + δ)E[X]. If ΦX(δ + ε) = ∞, then the assertion of the lemma is vacuous. Otherwise, there exists a set I ⊆ N with −log P(YI = 1) = ΦX(δ + ε) and EI[X] t + εE[X]. As EI[X] M · P(X t | YI = 1) + t, it follows that

P(X t) P(YI = 1) · P(X t | YI = 1) P(YI = 1) ·

εE[X] M

. Taking the negative logarithm of both sides gives the assertion of the lemma.

The next lemma lies at the heart of the matter. In very broad terms, it states that the upper tail event X (1 + δ)E[X] , viewed as a subset of the cube {0,1}N, may be covered almost completely by a union of subcubes of small codimension, where, crucially, the average value of X on each of these subcubes is at least (1 + δ − ε)E[X]. The proof uses a variant of the moment argument of Janson, Oleszkiewicz, and Ruciński [44].

- Lemma 3.7. Let Y be a random variable taking values in {0,1}N and let X = X(Y ) be a nonzero polynomial with nonnegative coeﬃcients and degree at most d. Then for every positive integer and all positive real numbers ε and δ,


1 + δ − ε 1 + δ

P X (1 + δ)E[X] and YI = 0 for all I ∈ I

,

where I = I ⊆ N : |I| d  and EI[X] (1 + δ − ε)E[X] .

Proof. Given S ⊆ N , let ZS be the indicator random variable of the event that YI = 0 for all I ∈ I with I ⊆ S. Note that I ⊆ I implies ZI ZI and let Z = Z N . Since XZ 0 and Z = Z, Markov’s inequality gives

E[X Z] (1 + δ)E[X]

P X (1 + δ)E[X] and Z = 1 = P XZ (1 + δ)E[X]

. (15)

Write X = I αIYI, where the sum ranges over all subsets I ⊆ N , each coeﬃcient αI is nonnegative, and αI = 0 unless |I| d. Then for every k ∈ ,

E[XkZ] =

E[YI

k · Z]

1 ···αI

1 ···YI

αI

k

I1,...,Ik

E[YI

1∪···∪Ik]

1 ···αI

1 ···YI

k · ZI

αI

k

I1,...,Ik

E[YI

1∪···∪Ik−1] · E[X | YI

1∪···∪Ik−1 = 1],

1 ···αI

1 ···YI

k−1 · ZI

1 ···YI

k−1 · ZI

αI

k−1

I1,...,Ik−1

where we may let the third sum range only over sequences I1,...,Ik−1 for which the event YI

1∪···∪Ik−1 = 1 has a positive probability of occurring. Note that for any such sequence, YI

1 ···YI

k−1 · ZI

and I1∪···∪Ik−1 ∈/ I. Since |I1∪···∪Ik−1| d(k − 1) d , we have

1∪···∪Ik−1 = YI

1 ···YI

k−1 ·ZI

1 ···YI

k−1

1∪···∪Ik[X] < (1 + δ − ε)E[X], as otherwise I1 ∪ ··· ∪ Ik−1 would belong to I. It follows that

E[X | YI

= 1] = EI

1 ···YI

k−1

E[YI

1∪···∪Ik]

1 ···αI

1 ···YI

k · ZI

αI

k

I1,...,Ik

< (1 + δ − ε)E[X] ·

E[YI

1∪···∪Ik−1].

1 ···αI

1 ···YI

k−1 · ZI

αI

k−1

I1,...,Ik−1

By induction, we see that E[X Z] < (1 + δ − ε)E[X] . Substituting this inequality into (15) completes the proof.

The following easy lemma will be used to relate the family I from the statement of Lemma 3.7 to the family I∗ of cores.

- Lemma 3.8. Let Y be a random variable taking values in {0,1}N and let X = X(Y ) be a real-valued function of Y . Then for every I ⊆ N and every nonnegative real number s, there exists some I∗ ⊆ I such that


- (i) EI∗[X] EI[X] − s and
- (ii) mini∈I∗ EI∗[X] − EI∗\{i}[X] s/|I|.


Proof. Deﬁne a sequence I = I0 ⊇ I1 ⊇ ··· ⊇ Ir = I∗ by repeatedly setting Ik+1 = Ik \ {i} for some i ∈ Ik such that EI

k\{i}[X] < s/|I|, as long as such an i exists. By construction, the set I∗ satisﬁes (ii). Finally, since r |I|, we have

[X] − EI

k

r−1

EI[X] − EI∗[X] =

[X] − EI

[X] s,

### EI

k+1

k

k=0

which is (i).

Proof of Theorem 3.1. Let t = (1+δ)E[X]. We ﬁrst prove the upper bound in (12). Let 1 denote the N-dimensional all-ones vector. Since X is an increasing function of Y , we have X X(1) always. In particular, Lemma 3.6 implies that

X(1) εE[X]

−log P(X t) ΦX(δ + ε) + log

. As X has degree at most d and nonnegative coeﬃcients, we have E[X] X(1) · pd and thus

− log P(X t) ΦX(δ + ε) + log 1/(εpd) (1 + ε/8) · ΦX(δ + ε), (16) where the second inequality holds provided that K is suﬃciently large, as we have assumed that ΦX(δ + ε) K log(1/p) and p 1 − ε.

For the rest of the proof let = ε(3d)−1K · ΦX(δ + ε) and deﬁne

I = I ⊆ N : |I| d  and EI[X] (1 + δ − ε/2)E[X] . It follows from Lemma 3.7 (invoked with ε replaced by ε/2) that

ε/2 1 + δ

P(X t and YI = 0 for all I ∈ I) 1 −

.

Since we have already shown that P(X t) exp − (1 + ε)ΦX(δ + ε) , see (16), we ﬁnd that letting K be suﬃciently large ensures

P(X t and YI = 0 for all I ∈ I) 1 − ε/(2 + 2δ) (ε/2) · P(X t).

Note next that every I ∈ I satisﬁes |I| d  (εK/2) · ΦX(δ + ε) and hence, by Lemma 3.8 applied with s = εE[X]/2, there is a subset I∗ ⊆ I satisfying the conditions (C1), (C2), and (C3). It follows that

P(X t and YI∗ = 0 for all I∗ ∈ I∗) (ε/2) · P(X t). (17) Let Im∗ := {I∗ ∈ I∗ : |I∗| = m} and recall that we assume |Im∗ | (1/p)εm/2 for all m ∈ N.

We now prove the upper bound in (12). It follows from (17) that

P(X t) (1 − ε/2)−1 · P YI∗ = 1 for some I∗ ∈ I∗ .

Moreover, the deﬁnitions of I∗ and ΦX(δ−ε) imply that every core I∗ ∈ I∗ satisﬁes |I∗|log(1/p) = −log P(YI∗ = 1) ΦX(δ − ε), see (C1). Hence, taking the union bound over all cores and using |Im∗ | (1/p)εm/2, we ﬁnd that

P(X t) (1 − ε/2)−1

∗| (1 − ε/2)−1

p|I

|Im∗ | · pm

I∗∈I∗

m

e−(1−ε/2)Φ

X(δ−ε)

∞

p(1−ε/2)m =

(1 − ε/2)−1

.

(1 − ε/2)(1 − p1−ε/2)

m= Φlog(1X(δ/p−ε))

Taking logarithms and using p 1 − ε and ΦX(δ − ε) K log(1/p), we see that a large enough choice of K ensures that −log P(X t) (1 − ε)ΦX(δ − ε), as required.

Finally, let us prove (13). Using (17), we obtain

P(X t and YI∗ = 0 for all I∗ ∈ J ∗) (ε/2) · P(X t) + P(YI∗ = 1 for some I∗ ∈ I∗ \ J ∗).

Noting that every I∗ ∈ I∗ \ J ∗ satisﬁes |I∗|log(1/p) = −P(YI∗ = 1) > (1 + ε)ΦX(δ + ε), we may employ a union bound again to show that

∗| e−(1−ε/2)(1+ε)Φ

X(δ+ε)

P(YI∗ = 1 for some I∗ ∈ I∗ \ J ∗)

p|I

1 − p1−ε/2 . In order to complete the proof, it now suﬃces to show that

I∗∈I∗\J ∗

e−(1+ε)(1−ε/2)Φ

X(δ+ε)

1 − p1−ε/2 (ε/2) · P(X t). (18)

To see that this inequality holds, note ﬁrst that (1+ε)(1−ε/2) > 1+ε/4 as ε < 1/2 and therefore, by (16),

X(δ+ε). As p 1 − ε and ΦX(δ + ε) K log(1/p), we can choose K so large that e−(ε/8)Φ

e−(1+ε)(1−ε/2)Φ

X(δ+ε) P(X t) · e−(ε/8)Φ

X(δ+ε)/(1 − p1−ε/2) ε/2, proving (18).

4. Arithmetic progressions in random sets of integers

Fix an integer k 3 and let X = XN,pk-AP be the number of k-term arithmetic progressions (k-APs) in the random set N p. The goal of this section is to study the upper tail of X in the regime where Theorem 3.1 is applicable. In particular, we will prove Theorem 1.3, which we restate here for convenience.

Theorem 1.3. Let k 3 be an integer and let X = XN,pk-AP denote the number of k-term arithmetic progressions in N p. Then, for every ﬁxed positive constant δ and all p = p(N) satisfying N−1 log N pk/2 1,

−log P X (1 + δ)E[X] Npk/2 log(1/p)

= √

lim

δ.

N→∞

To prove the theorem, we will use Theorem 3.1 to relate −log P X (1 + δ)E[X] to the solution of the optimisation problem

ΦX(δ) = min |I|log(1/p) : I ⊆ N and EI[X] (1 + δ)E[X] . More precisely, we shall prove the following statement, which is the main result of this section.

- Proposition 4.1. For every integer k 3 and all positive real numbers ε and δ, there exists a positive constant C such that the following holds. Suppose that N ∈ N and p ∈ (0,1) satisfy CN−1 log N pk/2 1/C. Then X = XN,pk-AP satisﬁes

(1 − ε)ΦX(δ − ε) −log P X (1 + δ)E[X] (1 + ε)ΦX(δ + ε).

The variational problem ΦX(δ) is a discretisation of the variational problem considered by Bhattacharya, Ganguly, Shao, and Zhao [10]. In their setup, one minimizes over the set of all product measures on {0,1} N , whereas we only consider ‘planting’ constructions; in other words, we restrict our attention to products of Ber(p) and Ber(1) measures. The result below can be easily deduced from [10, Theorem 2.2], but we will reprove it in Section 4.2, for completeness.

- Proposition 4.2. For every integer k 3 and all positive real numbers ε and δ, there exists a positive constant C such that the following holds. Suppose that N ∈ N and p ∈ (0,1) satisfy CN−1 pk/2 1/C. Then X = XN,pk-AP satisﬁes


ΦX(δ) √

1 − ε

1 + ε.

δ · Npk/2 log(1/p)

Clearly, Propositions 4.1 and 4.2 imply Theorem 1.3.

- 4.1. Proof outline. The proof of Proposition 4.2 will be relatively straightforward: On the


one√ hand, since every interval (or, more generally, every arithmetic progression) of length δNpk/2 contains approximately δ E[X] arithmetic progressions of length k, we have EI[X] (1 + δ − o(1))E[X] for each such interval I. Consequently, ΦX(δ) (1 + o(1))√

δNpk/2 log(1/p). On the other hand, a simple calculation shows that, for every set I ⊆ N with O(Npk/2) elements, EI[X] − E[X] is asymptotically equal to the number of k-APs in I. Therefore, ΦX(δ)/log(1/p) is bounded from below (asymptotically) by the minimal size of a set of integers that contains at least δ E[X] k-APs. We will show that this minimum is achieved by an interval, see Theorem 4.3 below; thus, we conclude that ΦX(δ) (1 − o(1))√

δNpk/2 log(1/p).

In order to derive Proposition 4.1 from Theorem 3.1, we will need to show that the family I∗ of cores from the statement of the theorem is entropically stable. In order to bound the number of cores of a given size, we will ﬁrst observe that, for every I ∈ I∗ and each i ∈ I, the diﬀerence EI[X]−EI\{i}[X] is asymptotically equal to the number of k-APs in I that contain the element i. In particular, condition (C3) and ΦX(δ) = O Npk/2 log(1/p) can be combined to conclude that

each element of every cores lies in Ω Npk/2/log(1/p) arithmetic progressions of length k that are fully contained in the core; see Claim 4.5 below.

The heart of the proof of the proposition is a counting argument showing that very few sets have this combinatorial property. Let us ﬁrst sketch a simpliﬁed version of this argument that would be suﬃcient to prove the proposition under the slightly stronger assumption that Npk/2 (log N)k+1. Suppose that I is a core of cardinality m and let I be a random subset of I with m/log(1/p) elements. For every i ∈ I, we expect that there will be Ω Npk/2/log(1/p)

arithmetic progressions of length k in I that contain i, and that a (log(1/p))1−k-proportion of these will be contained in I ∪ {i}. A standard application of Janson’s inequality yields that the above description holds with probability very close to one, simultaneously for all i ∈ I. In particular, I contains some subset I with m/log(1/p) elements and the property that, for every i ∈ I \ I , there are at least Ω Npk/2/(log(1/p))k arithmetic progressions of length k that comprise i and some k − 1 elements of I .

We may now enumerate all possible cores I in two steps: First, there are at most m/log(1 N /p) exp O(m) choices of I . Second, since I intersects at most O(|I |2) arithmetic progressions of length k at k − 1 elements and each i ∈ I is contained in at least Ω Npk/2/(log(1/p))k such progressions, the elements of I \ I must all come from a set of size

O |I |2(log(1/p))k Npk/2

O m(log(1/p))k−1

that depends solely on I . Thus, the number of choices for I \ I , the remaining elements of the core, is at most O(m(log(1/p))

k−1)

m = exp O(mlog log(1/p)) .

In the proof of Proposition 4.1 below, we give a more reﬁned version of the above argument that allows us to recover the optimal power of the logarithm in the lower bound assumption on p. Instead of constructing cores in two steps, we build them element-by-element. This enables a ﬁner control of the number of choices for each next element, given all the elements chosen so far. Roughly speaking, as we add more elements to I, the set I from the previous paragraph is gradually increasing its size.

- 4.2. Estimating ΦX. As mentioned above, we use the following extremal result about the largest number of k-APs in a set of integers of a given size, proved in the case k = 3 by Green–Sisask [37] and later extended in [10] to arbitrary k 3; the corresponding statement in the case where


k ∈ {1,2} is trivial. For a set I ⊆ Z, we denote by Ak(I) the number of k-APs in I. Recall that we only count k-APs with positive common diﬀerence.

- Theorem 4.3 ([10, 37]). For every positive integer k and I ⊆ Z, we have Ak(I) Ak |I| . We reproduce the proof here for the sake of completeness.


Proof. We prove the statement by induction on k. The cases k = 1 and k = 2 are trivial as Ak(I) = Ak |I| for every set I, so we may assume that k 3. Suppose that |I| = n and let a1,...,an be the elements of I listed in increasing order. We partition the set of k-APs in I into two parts depending on the location of the (k − 1)st element. More precisely, we let m = (k − 2)n/(k − 1) , let

A1 = (i1,...,ik) ∈ n k : (ai

) is a k-AP and ik−1 m ,

,...,ai

1

k

and let A2 comprise the remaining k-APs (that is, ones with ik−1 > m). The removal of the kth term from a progression in A1 maps it to a (k − 1)-AP contained the set {a1,...,am} and therefore |A1| Ak−1({a1,...,am}) Ak−1 m , by the induction hypothesis. On the other hand, we observe that for every i > m, there are at most n − i arithmetic progression of length k

such that ik−1 = i and thus

n

|A2|

n − i.

i=m+1

In order to complete the proof, it is suﬃcient to verify that our choice of m ensures that

n

Ak−1 m +

n − i = Ak( n ).

i=m+1

Indeed, m satisﬁes the following two inequalities: m +

m − 1 k − 2

n and m + 1 − (k − 2)(n − m − 1) 1.

The ﬁrst inequality implies that extending any arithmetic progression (i1,...,ik−1) contained in m by adjoining to it the element ik = 2ik−1 − ik−2 yields a k-AP contained in n , whereas

the second inequality implies that ni=m+1 n − i is precisely the number of k-APs in n whose (k − 1)st term exceeds m.

For future reference, let us note that Ak i − Ak i − 1 = k i−−11 for all positive integers i and k 2 and, consequently,

m2 2(k − 1) −

i − 1 k − 1

(k − 1)m 2 ± k2. (19)

m

Ak( m ) =

=

i=1

Using Theorem 4.3, it is not diﬃcult to compute the asymptotic value of ΦX(δ) and complete the proof of Theorem 1.3.

Proof of Proposition 4.2. Without loss of generality, we may assume that ε 1. Given a subset

- I ⊆ N , let aj(I) denote the number of k-APs in N that intersect I in exactly j elements. Note that


k

k

EI[X] =

aj(I)pk−j and that E[X] = Ak N pk =

aj(I)pk. (20)

j=0

j=0

It follows that EI[X] − E[X] (1 − pk)ak(I) = (1 − pk)Ak(I) for every I ⊆ N . In particular, whenever (1 − pk)Ak( m ) δpkAk N , then E m [X] (1 + δ)E[X]. Therefore,

√

δpkAk N 1 − pk

δ · Npk/2 log(1/p),

(1 + ε) ·

ΦX(δ) min mlog(1/p) : Ak m

where the last inequality follows from (19) and our assumption N2pk C2 for a suﬃciently large constant C. It remains to prove the matching lower bound.

Suppose that I is a smallest subset of N with EI[X] (1 + δ)E[X]. Then (20) implies

δAk N pk = δ E[X] EI[X] − E[X]

k

aj(I)pk−j. (21)

j=1

Since every pair of distinct numbers in N is contained in at most k2 arithmetic progressions of length k, it follows that a1(I) |I| · Nk2 and k−1

j=2 aj(I) |I|2 · k2. Since we already know that |I| 2√

δ · Npk/2, inequality (21) gives δAk( N )pk 2√

δk2N2p3k/2−1 + 4δk2N2pk+1 + Ak(I). We now invoke Theorem 4.3 and (19) to obtain

δN2pk 2(k − 1)

δk2N2p3k/2−1 − 4δk2N2pk+1 Ak( I ) |I|2 2(k − 1)

δAk( N )pk − 2√

(1 − ε) ·

,

where we use the assumptions p C−2/k and N2pk C2 for a large enough C. Thus ΦX(δ) = |I|log(1/p) (1 − ε) ·

√

δ · Npk/2 log(1/p), as required.

- 4.3. Janson’s inequality. It remains to prove Proposition 4.1. The proof uses the following version of Janson’s inequality for hypergeometric random variables. It follows from the (original version of) Janson’s inequality for binomial distributions [43, Theorem 1] and the fact that the median of a binomial random variable whose mean is an integer is equal to its mean. Our argument is an adaptation of [5, Lemma 3.1].

- Lemma 4.4. Suppose that {Bα}α∈A is a family of subsets of a t-element set Ω. Let s ∈ {0,...,t} and let


µ =

α∈A

- s

- t


|Bα|

and ∆ =

α∼β

- s

- t


|Bα∪Bβ|

,

where the second sum is over all ordered pairs (α,β) ∈ A2 such that α = β and Bα ∩ Bβ = ∅. Let S be the uniformly chosen random s-element subset of Ω and let Z denote the number of α ∈ A such that Bα ⊆ S. Then for every ε ∈ (0,1],

P Z (1 − ε)µ 2exp −

ε2 2 ·

µ2 µ + ∆

.

Proof. For every k ∈ {0,...,t}, let Sk be the uniformly chosen random k-element subset of Ω and let Zk denote the number of α ∈ A such that Bα ⊆ Sk, so that Z = Zs, and note that there exists a natural coupling under which Zk Zk+1 for every k. Let S be the (s/t)-random subset of Ω, that is the random subset of Ω formed by keeping each of its elements with probability s/t, independently of others, and let Z denote the number of α ∈ A such that Bα ⊆ S . Since E Z | |S | = Z|S |, the stochastic ordering of the Zks implies that, for any number M, the function k  → P(Z M | |S | = k) is decreasing. Hence,

P Z (1 − ε)µ =

t

k=0

P Z (1 − ε)µ | |S | = k · P(|S | = k)

P Z (1 − ε)µ | |S | = s · P(|S | s)

= P Z (1 − ε)µ · P(|S | s) P(Z (1 − ε)µ)/2,

where the last inequality follows from the well-known fact that if np is an integer, then it is the median of the binomial distribution with parameters n and p. We can now invoke the classical version of Janson’s inequality and conclude that

P Z (1 − ε)µ 2P Z (1 − ε)µ 2exp −

ε2 2 ·

µ2 µ + ∆

.

- 4.4. Proof of Proposition 4.1. We may assume without loss of generality that ε is suﬃciently small, say ε < min {1/2,δ/2}. Note also that the case N 2 is trivial; indeed, in that case X is


identically zero and thus log P(X (1+δ)E[X]) = 0 = ΦX(δ) for every δ ∈ R. We may therefore assume that N 3, which, in turn, implies that N2pk C2.

Denote by Yi the indicator random variable of the event that i ∈ N p. Then Y = (Y1,...,YN) is a vector of independent Ber(p) random variables and X is a nonzero polynomial with nonnegative coeﬃcients and degree at most k in the coordinates of Y . Let K = K(k,ε,δ) be the constant given by Theorem 3.1. The proposition follows once we verify that X satisﬁes the various assumptions of the theorem.

First, our assumption on p implies that p 1 − ε whenever C is large enough. Second, it follows from Proposition 4.2 and the inequality N2pk C2 that, whenever C is large enough, ΦX(δ − ε) ΦX(δ/2) K log(1/p). Recall that a subset I ⊆ N is called a core if

(C1) EI[X] (1 + δ − ε)E[X], (C2) |I| K · ΦX(δ + ε), and

(C3) mini∈I EI[X] − EI\{i}[X] E[X]/ K · ΦX(δ + ε) . The ﬁnal assumption of Theorem 3.1 is that, for every integer m, there are at most (1/p)εm/2 cores of size m.

In order to count the cores, we must ﬁrst unravel the meaning of (C1), (C2), and (C3), and show that each core enjoys a simple combinatorial property. Proposition 4.2 supplies a constant K = K (K,k,ε,δ) such that, whenever C is suﬃciently large,

4kK · ΦX(δ + ε) 4kK · (1 + ε)√

δ + ε · Npk/2 log(1/p) K · Npk/2 log(1/p). (22)

Given a set I ⊆ N and an i ∈ N , we write Ak(I;i) for the number of k-term arithmetic progressions in I ∪ {i} that contain the element i. The proof of the following claim is similar to the argument used to prove Proposition 4.2.

- Claim 4.5. For every core I of size m and all i ∈ I,


Npk/2 K log(1/p)

Ak(I;i)

.

Proof. Given an i ∈ I, let aj(I;i) denote the number of k-APs in N that intersect I in exactly j elements, one of which is i. With this notation, Ak(I;i) = ak(I;i) and we may write EI[X] − EI\{i}[X] = kj=1 aj(I;i) · pk−j(1 − p). Since every pair of distinct numbers in N

is contained in at most k2 arithmetic progressions of length k, we have a1(I;i) Nk2 and k−1 j=2 aj(I;i) mk2. In particular, as m K · ΦX(δ + ε) by (C2), we get

EI[X] − EI\{i}[X] k2Npk−1 + k2K · ΦX(δ + ε) · p + Ak(I;i). On the other hand, it follows from (C3) that

E[X] K · ΦX(δ + ε)

EI[X] − EI\{i}[X]

.

By (19), we have E[X] = Ak( N )pk N2pk/(2k), since N C and C is large. Combining the upper and lower bounds on EI[X] − EI\{i}[X] and using (22), we obtain

2Npk/2 K log(1/p) − k2Npk−1 − kK Npk/2+1 log(1/p). Since k 3 and p C−2/k for a large enough C, we deduce the assertion of the claim.

Ak(I;i)

For the remainder of the proof, ﬁx some integer m satisfying 1 m K · ΦX(δ + ε) and let K be a suﬃciently large positive constant depending on K and k (but not on C). For a subset

- I ⊆ N and an integer i ∈ N \ I , we shall say that i is rich with respect to I if


k−1

Npk/2 K log(1/p) ·

|I | m

. (23)

Ak(I ;i)

Moreover, given a sequence (i1,...,im) of m distinct elements of N , we shall say that an index m ∈ m is rich if im is rich with respect to the set {i1,...,im −1}.

We ﬁrst observe that for every I ⊆ N , there are relatively few integers i ∈ N \ I that are rich with respect to I . Indeed, there are at most k|I |2 arithmetic progressions P of length k in

N for which |I ∩ P| = k − 1, because any such progression is determined by its minimal and maximal element in I and the position in the progression of the element in P \ I . Then

k−1

Npk/2 K log(1/p) ·

|I | m

Ak(I ;i) k|I |2.

i ∈ N \ I : i is rich w.r.t. I ·

i∈ N \I

Consequently, as m K · Npk/2 log(1/p) by (22),

k−3

m |I |

i ∈ N \ I : i is rich w.r.t. I kK K · m log(1/p) 2 ·

. (24)

The key property that allows us to control the number of cores I of size m is that, in a large proportion of orderings of the members of I, almost all indices are rich. This property implies that, if one builds an (ordered) core element by element, then, very often, one must choose the next element from the small set of integers that are rich with respect to the previously chosen ones. From this, it will be easy to obtain an upper bound on the number of cores of a given size.

- Claim 4.6. Suppose that I is a core of size m. Then there are at least m!/2 orderings (i1,...,im) of the elements of I such that all but at most


1 k−1

K log(1/p) Npk/2

· m (25) indices m ∈ m are rich.

Proof. Let (i1,...,im) be a uniformly chosen random ordering of the elements of I. Fix integers m ∈ m and i ∈ I and condition on the event {im = i}. Under this conditioning, the set {i1,...,im −1} is a uniformly random (m − 1)-element subset of I \ {i}. Therefore, we may use Janson’s inequality for the hypergeometric distribution (Lemma 4.4) to get an upper bound for the probability that the given m is not rich. It follows from the deﬁnition that m = 1 is trivially rich, so assume m 2. Let Bi be the collection of all (k − 1)-element subsets of I \ {i} that form a k-AP with i. Deﬁne

k−1

m − 1 m − 1

m − 1 m − 1

|B|

µm (i) =

= Ak(I;i) ·

B∈Bi

and, writing B ∼ B to mean that B = B and B ∩ B = ∅,

m − 1 m − 1

|B∪B |

∆m (i) =

.

B,B ∈Bi B∼B

Since for a given B ∈ Bi, there are fewer than k3 sets B ∈ Bi such that B ∩ B = ∅, we have ∆m (i) µm (i) · k3. It follows from Claim 4.5 that

k−1

Npk/2 K log(1/p) ·

m − 1 m

µm (i)

,

which, provided that K is suﬃciently large, is at least twice as large as the right-hand side of (23) with |I | = m − 1. Hence, by Lemma 4.4 with ε = 1/2,

µm (i)2

P(m is not rich | im = i) 2exp −

8 µm (i) + ∆m (i) 2exp −

µm (i) 9k3 2exp −

k−1

Npk/2 9k3K log(1/p) ·

m − 1 m

.

Since this upper bound is independent of i, one may replace the conditional probability above with the unconditional one. Letting X ⊆ m denote the (random) set of non-rich indices, we then ﬁnd that

k−1

Npk/2 9k3K log(1/p) ·

m − 1 m

m

E |X| 2

exp −

. Since for every α > 0, we have

m =2

k−1 ∞

m − 1 m

2m α

m

∞

m α

k−1

k−1

e−(αx/m)

exp − α ·

dx =

e−y

dy

0

0

m =2

we obtain

1 k−1

9k3K log(1/p) Npk/2

E |X| 4 ·

· m.

The assertion of the claim now follows from Markov’s inequality, provided that K is suﬃciently large.

Equipped with the above facts, we can now prove the desired upper bound on the number of cores of size m. For a set X ⊆ m , let Sm(X) denote the family of all sequences of m distinct elements of N such that every index m ∈ / X is rich. To control the number of sequences in Sm(X), note that we can pick the ﬁrst element of the sequence arbitrarily and, for every subsequent index m , bound the number of possible values for the m th element of the sequence either by appealing to (24), if m ∈ / X, or simply by N, otherwise. Thus,

k−3

|Sm(X)| m!

1 m! · N · N|X| ·

m

m m − 1

kK K · m log(1/p) 2 ·

m =2

m

k−2

m

m m

N · N|X| · kK K · log(1/p) 2

·

.

m =1

Since mm =1 m m k−2 e(k−2)m, we ﬁnd that, whenever C is suﬃciently large,

|Sm(X)| m!

e(|X|+1) logN · e3mlog log(1/p). Finally, denote by Im∗ the set of all cores of size m. Claim 4.6 implies that |Im∗ |

Sm(X) m!

2 m! X Sm(X) 2m+1 · max

,

X

1 k−1

where the sum and the maximum range over all X ⊆ N of size at most K Np log(1/p)

m. Hence,

k/2

1 k−1

K log(1/p) Npk/2

|Im∗ | 2m+1 · exp

· m · log N + log N · e3mlog log(1/p).

Since we have assumed that Npk/2 C log N and p C−2/k, then, whenever C is suﬃciently large, the above inequality implies that

1 k−1

K log(1/p) Npk/2

|Im∗ | (1/p)εm/4 · exp

· m · log N (1/p)εm/2,

where the last inequality can be seen, for example, by distinguishing between the cases p N−1/k (in which case log N = Θ(log(1/p))) and p > N−1/k (where Npk/2 > N1/k). This completes the proof of Proposition 4.1.

5. Counting small subgraphs—a graph-theoretic interlude

As mentioned in the introduction, this section will collect some graph-theoretical results which will be required to analyze the localized regime of XK

n,pr and Xn,pH for connected, regular graphs H in Sections 6 and 7, respectively.

The main goal is to bound the maximum number of embeddings of a given graph J into a larger graph G in terms of the number of vertices and edges in G, where we are interested both in bounding the number of such embeddings globally (i.e., without additional restrictions on the image) and locally (where we require that the image contain a particular edge of G). These estimates will play a crucial role in translating conditions (C1)–(C3) from Theorem 9.1 into structural restrictions on core graphs.

In the ﬁrst two subsections, we collect results related to bounding the number of embeddings globally; the fractional independence number of a graph (deﬁned below) plays an important role in this part. The next subsection contains bounds on the number of local embeddings, where the image of the embedding is required to contain a particular edge. In the ﬁnal subsection, we establish several stability results (in the sense of extremal combinatorics) on graphs allowing a nearly maximal number of embeddings of stars and cliques; these results will be of use when establishing Theorem 1.8.

Recall that Emb(J,G) denotes the set of embeddings of J into G and, for every edge uv of G, Emb(J,G;uv) denotes the subset of Emb(J,G) containing all embeddings that map an edge of J to uv.

- 5.1. Fractional graph theory. A fractional independent set in a graph J is an assignment α: V (J) → [0,1] that satisﬁes αu + αv 1 for every edge uv of J. The fractional independence


number of J, denoted by αJ∗, is the largest value of v∈V (J) αv among all fractional independent sets α in J. The following result is folklore; we include a proof for completeness.

- Lemma 5.1. Every graph J admits a fractional independent set α with v∈V (J) αv = αJ∗ such that αv ∈ {0, 12,1} for every v ∈ V (J). Moreover, there is a partition V (J) = V1 ∪ V2 with |V1|/2 + |V2| = αJ∗ such that V1 can be covered by a collection of vertex-disjoint edges and cycles of J.


Proof. Let J be the bipartite double cover of J, that is, the graph with vertex set V (J) × {1,2} whose edges are all pairs {(u,1),(v,2)} such that uv ∈ E(J). Moreover, let π: V (J) × {1,2} → V (J) be the projection onto the ﬁrst coordinate. The Kőnig–Egerváry theorem (see, e.g., [13, Theorem 8.32] or [29, Theorem 2.1.1]) implies that J contains a matching M and an independent set I such that |I | + |M | = vJ . Deﬁne α: V (J) → {0, 12,1} by letting αv = |π−1(v) ∩ I |/2 for every v ∈ V (J). Since I is an independent set in J , one can see that α is a fractional independent set with v∈V (J) αv = |I |/2. In particular, we have

vJ − |M | = 2

αv 2αJ∗. (26)

v∈V (J)

Since π induces a projection of J onto J, we can deﬁne M = π(M ) to be the image of the matching M . Since M ⊆ J, we have αJ∗ αM∗ . Moreover, as M is a matching in J , we see that M has maximum degree at most two and thus each nontrivial connected component of M is either a cycle or a path. Let V2 ⊆ V (J) comprise all isolated vertices of M and one arbitrarily chosen endpoint of each path of even length; let V1 = V (J) \ V2. By construction, each connected component of M[V1] is either a cycle or a path of odd length. Since the fractional independence number of every cycle and every path of odd length is exactly half its number of vertices, it follows that αM∗ αM∗ [V

1] + |V2| = |V1|/2 + |V2|. It is clear that V1 can be covered with vertex-disjoint edges and cycles of M and thus also of J. We now claim that |V1| |M |. To see this, ﬁx a connected component L of M and observe that π−1(L) has at most eL edges unless L is a single edge, in which case π−1(L) has at most two edges. Therefore,

eπ−1(L)

vL − 1 if L is a path of length at least two, vL otherwise.

Let C(M) denote the nontrivial connected components of M. We have |M | =

vL − [L is a path of length at least two]

eπ−1(L)

L∈C(M)

L∈C(M)

vL − [L is a path of even length] = |V1|.

L∈C(M)

Consequently, (26) shows that |V1| + 2|V2| = 2vJ − |V1| 2vJ − |M | = vJ − |M | = 2

v∈V (J)

and so v∈V (J) αv = αJ∗ = |V1|/2 + |V2|. The following lemma is implicit in [44, Appendix A].

αv 2αJ∗ 2αM∗ |V1| + 2|V2|,

Lemma 5.2. Suppose that J is a nonempty subgraph of a connected, ∆-regular graph H. Then

eJ ∆ · (vJ − αJ∗) ∆ · αJ∗. If the ﬁrst inequality is tight, then

- (Q1) J = H or
- (Q2) J admits a bipartition V (J) = A ∪ B such that degJ a = ∆ for all a ∈ A.


If both inequalities are tight, then J = H. Remark 5.3. Since every graph J is a subgraph of the complete graph of vJ vertices, Lemma 5.2 implies that

eJ (vJ − 1) · (vJ − αJ∗). Moreover, equality holds if and only if J is complete, J is empty, or J = K1,v

J−1.

Proof of Lemma 5.2. By Lemma 5.1, J has a fractional independent set α such that αv ∈ {0, 12,1}. Then

(2 − αu − αv) =

(1 − αv)degJ v ∆ ·

(1 − αv) = ∆ · (vJ − αJ∗), (27)

eJ

uv∈E(J)

v∈V (J)

v∈V (J)

which is the ﬁrst inequality. For the second inequality, note that the function α: V (J) → [0,1] deﬁned by αv = 1/2 is a fractional independent set, so αJ∗ vJ/2.

Assume now that eJ = ∆ ·(vJ −αJ∗). Then both inequalities in (27) are equalities; this implies αu + αv = 1 for every edge uv ∈ E(J) and degJ(v) = ∆ whenever αv = 1. Let A, B, and C denote the sets of vertices that α maps to 0, 1, and 1/2, respectively. Each vertex in A ∪ C has degree ∆ and each edge of J has either both endpoints in C or one endpoint in each of A and

- B. In particular, if C is not empty, then it induces a ∆-regular graph and hence C = V (J) and


- J = H, as H is connected and ∆-regular. Otherwise, if C is empty, then A ∪ B is a bipartition of


- J and all vertices of A have degree ∆.


Lastly, suppose that eJ = ∆ · αJ∗, which implies eJ = ∆ · (vJ − αJ∗). Let A,B,C be the same partition as above. If C is nonempty, then J is ∆-regular, and we are done. Otherwise,

|A| = eJ/∆ = αJ∗ = vJ − eJ/∆ = vJ − |A| = |B|. Therefore, every vertex of B has degree ∆ and J = H.

- 5.2. Global embedding bounds. The main result of this section is the following theorem of Janson, Oleszkiewicz, and Ruciński [44]. A closely related bound that does not depend on the number of vertices in G was obtained earlier by Alon [1] (see also [34] for a short proof). The dependence on the number of vertices will be essential in the case where J is a (double) star, see Figure 5.


Theorem 5.4 ([44]). For every nonempty graph J without isolated vertices and every graph G with n vertices,

|Emb(J,G)| (2eG)vJ−α∗J · min{2eG,n}2α

∗ J−vJ

We derive Theorem 5.4 from Lemma 5.1 and the following result due to Alon [1], which establishes the theorem for the case where J is a cycle.

- Lemma 5.5. Let C denote the cycle of length . For every 3 and every graph G, |Emb(C ,G)| (2eG) /2.


Remark 5.6. If is even, this follows immediately from the fact that C contains a perfect matching of  /2 edges. If is prime, there is also a very short and pretty proof using the monotonicity of Lp norms; see [60] for this proof and more precise estimates. The proof presented below works for all 3.

Proof of Lemma 5.5. For each edge e ∈ E(G), denote by ce the number of copies of C in G that contain the edge e. Since e∈E(G) ce = · N(C ,G), where N(C ,G) is the number of copies of

- C in G, it follows from the Cauchy–Schwarz inequality that


|Emb(C ,G)|2 = 2 · N(C ,G) 2 2eG ·

2c2e.

e∈E(G)

Let C∗ be the graph obtained from gluing two copies of C along an edge. In other words, C∗ is obtained from the cycle of length 2 − 2 by adding to it one longest chord. Observe that if (L1,L2) is an ordered pair of copies of C in G, both containing e, then there are at exactly two homomorphisms ϕ: V (C∗ ) → V (G) that map the two vertices of degree three in C∗ onto the endpoints of e and the two copies of C in C∗ onto L1 and L2, respectively. Letting Hom(C∗ ,G) be the collection of all homomorphisms from C∗ to G, we may conclude that

2c2e |Hom(C∗ ,G)| |Hom ( − 1) · K2,G | (2eG) −1,

e∈E(G)

where the second inequality holds because C∗ contains a perfect matching of − 1 edges.

Proof of Theorem 5.4. By Lemma 5.1, there is a partition of V (J) into V1 and V2 such that |V1|/2 + |V2| = αJ∗ and V1 can be covered by a collection C of vertex-disjoint edges and cycles of J. Let J be the spanning subgraph comprising the edges and cycles of C and one edge incident to every vertex in V2. We claim that

|Emb(J ,G)|

|Emb(C,G)| · min{2eG,n}|V

2|.

C∈C

Indeed, every embedding of J [V1] decomposes into embeddings of the graphs in C, and there are at most min{2eG,n} possible images for every vertex of V2. By Lemma 5.5, for every cycle C ∈ C,

|Emb(C,G)| (2eG)vC/2; the same inequality holds when C is a single edge. Since every embedding of J into G is also an embedding of J , we deduce that

(2eG)vC/2 · min{2eG,n}|V

2| = (2eG)|V1|/2 · min{2eG,n}|V

|Emb(J,G)|

2|.

C∈C

Since |V1|/2 = vJ − αJ∗ and |V2| = 2αJ∗ − vJ, this completes the proof.

- 5.3. Local embedding bounds. We now state three lemmas that bound |Emb(J,G;uv)| from above.


- Lemma 5.7. Suppose that H is a ∆-regular graph. For every graph G and each uv ∈ E(G),

|Emb(H,G;uv)| 4eH · (2eG)

vH

2 − 2∆∆−1

· (4degG u · degG v)

∆−1 ∆

.

- Lemma 5.8. Suppose that J is a nonempty, connected graph with maximum degree ∆ that admits


a bipartition V (J) = A ∪ B such that |A| < |B| and degJ a = ∆ for every a ∈ A. For every graph G and every uv ∈ E(G),

|Emb(J,G;uv)| eJ · (degG u + degG v) · (2eG)|A|−1 · min{eG,vG} |B|−|A|−1.

- Lemma 5.9. Suppose that H is a ∆-regular graph. For every graph G and every G ⊆ G,

uv∈E(G )

|Emb(H,G;uv)| eH · (2eG)vH/2 ·

eG eG

1/∆

.

Our proofs of Lemmas 5.7 and 5.9 are relatively straightforward adaptations of the elegant entropy argument of Friedgut and Kahn [34] (see also the excellent survey of Galvin [35]). They will be derived from the following somewhat abstract form of the main result of [34]. The proof of Lemma 5.8 is elementary.

- Lemma 5.10. Suppose that H is a ∆-regular graph. Let E be a family of embeddings of H into a graph G and, for every edge ab of H, let


Eab = {ϕ(ab) : ϕ ∈ E}. Then

2|Eab| 1/∆.

|E|

ab∈E(H)

Proof. Let ϕ¯: V (H) → V (G) be a uniformly chosen random element of E. Write H(Z) for the entropy of a discrete random variable Z and observe that H(ϕ¯) = log |E|. Since H is ∆-regular, Shearer’s inequality [22] implies that

1 ∆ ·

H(¯ϕ)

H ϕ ¯(a),ϕ¯(b) .

ab∈E(H)

The random variable (ϕ¯(a),ϕ¯(b)) can take on at most 2|Eab| values, as it an ordered pair of vertices that make up the edge ϕ(ab). Using the fact that the entropy of any distribution on a set is at most that of the uniform distribution on that set, it follows that H ϕ ¯(a),ϕ¯(b) log(2|Eab|). This implies the assertion of the lemma.

- Proof of Lemma 5.7. Given an ordered pair (c,d) of adjacent vertices of H, let E(c,d) be the family of embeddings ϕ of H into G such that ϕ(c) = u and ϕ(d) = v. For a given edge ab of H, deﬁne Eab(c,d) = {ϕ(ab) : ϕ ∈ E(c,d)} as in the statement of Lemma 5.10. Observe that

Eab(c,d)

 



eG if {a,b} ∩ {c,d} = ∅,

- degG u if {a,b} ∩ {c,d} = {c},
- degG v if {a,b} ∩ {c,d} = {d}, 1 if {a,b} = {c,d}.


Invoking Lemma 5.10 to bound |E(c,d)| from above and summing over all 2eH pairs (c,d) of adjacent vertices of H, the claimed upper bound on the number of embeddings of H into G that use the edge uv follows.

- Proof of Lemma 5.8. We ﬁx an edge ab of J, where a ∈ A and b ∈ B, and count the embeddings ϕ of J into G such that ϕ(ab) = uv. To this end, we ﬁrst show that J − b contains a matching M that saturates A. To see this, note that for every nonempty S ⊆ A,


|S| · ∆ =

degJ c

degJ d |NJ(S)| · ∆,

d∈NJ(S)

c∈S

yielding |NJ(S)| |S|. Moreover, this inequality is strict unless the subgraph of J induced by S ∪ NJ(S) is ∆-regular. However, the latter is impossible since, as J is connected, the only ∆-regular subgraph of J could be J itself, but our assumption |A| < |B| implies that J is not regular. Hence |NJ−b(S)| |NJ(S)| − 1 |S|, verifying Hall’s condition. Now, given a matching M ⊆ J −b that saturates A, we may bound the number of embeddings ϕ as above in the following way. Let c be the neighbour of a in M. There are at most degG u + degG v embeddings of

J[{a,b,c}] into G that map ab to uv. Each of them admits at most (2eG)|M|−1 extensions to an embedding of J[V (M)∪{b}]. Each of those embeddings can be extended to an embedding of J in at most min{eG,vG}|B\({b}∪V (M))| ways. Since |M| = |A| and |B \({b}∪V (M))| = |B|−|A|−1, summing over all ab ∈ E(J) gives the claimed bound on |Emb(J,G;uv)|.

- Proof of Lemma 5.9. Given an edge cd of H, let Ecd be the family of embeddings of H into G that


map cd onto an edge of G . Deﬁne Eabcd = {ϕ(ab) : ϕ ∈ Ecd} as in the statement of Lemma 5.10 and observe that

eG if {a,b} = {c,d}, eG otherwise.

Eabcd

Invoking Lemma 5.10 to bound |Ecd| from above and summing over all edges cd of H gives the claimed upper bound.

- 5.4. Stability results. Observe that, when J is the complete graph, then Theorem 5.4 yields


the upper bound |Emb(Kr,G)| (2eG)r/2. This is a weak version of a more precise result due to Erdős–Hanani [32] and also follows from the Kruskal–Katona theorem [50, 55]. One can see that the upper bound (2eG)r/2 is asymptotically optimal if G contains a clique comprising all of its edges. Our next theorem states that, when the upper bound given in Theorem 5.4 is nearly tight, then G resembles such a graph, in the sense that it must contain a subgraph of density 1 − o(1) covering nearly all of its edges. This could be proved by appealing to a stability version of the Kruskal–Katona theorem due to Keevash [51]. The proof we present below is elementary.

- Theorem 5.11. Suppose that r 3. If a graph G satisﬁes |Emb(Kr,G)| (1 − ε) · (2eG)r/2,


for some ε e−G1/2, then G has a subgraph G with minimum degree at least (1−4ε1/2)·(2eG)1/2. Proof. The assertion of the theorem follows once we establish the case r = 3 and an analogous property for the path with four vertices (and three edges), which we denote by P4. Indeed, if r is odd, then Kr contains a spanning subgraph that is the disjoint union of K3 and a matching of size (r − 3)/2. Thus,

|Emb(Kr,G)| |Emb(K3,G)| · |Emb(K2,G)|(r−3)/2 = |Emb(K3,G)| · (2eG)(r−3)/2

and hence |Emb(K3,G)| (1 − ε) · (2eG)3/2. Analogously, if r is even, then Kr contains a subgraph that is the disjoint union of P4 and a matching of size (r − 4)/2. Thus,

|Emb(Kr,G)| |Emb(P4,G)| · |Emb(K2,G)|(r−4)/2 = |Emb(P4,G)| · (2eG)(r−4)/2,

which implies that |Emb(P4,G)| (1 − ε) · (2eG)2. Therefore, it suﬃces to prove the following two claims.

- Claim 5.12. If |Emb(P4,G)| (1 − ε) · (2eG)2, for some positive ε, then G has a subgraph G with minimum degree at least (1 − 2ε1/2)(2eG)1/2.
- Claim 5.13. If |Emb(K3,G)| (1 − ε) · (2eG)3/2, for some ε e−G1/2, then G has a subgraph G with minimum degree at least (1 − 4ε1/2)(2eG)1/2.


- Proof of Claim 5.12. We may assume that ε < 1/4, as otherwise the assertion of the claim is trivially satisﬁed. Let F be the graph with vertex set E(G) whose edges are all pairs {uv,xy} such that the set {u,v,x,y} induces a K4 in G. Let G be the indicator function of the edge set


of G and note that |Emb(P4,G)| =

2 · G(ux) + G(uy) + G(vx) + G(vy)

{uv,xy}⊆E(G) {u,v}∩{x,y}=∅

eG

2 − eF 3e2G + 2eF. In particular, our assumption implies that eF (1/2 − 2ε) · e2G.

8eF + 6

Let F be the subgraph obtained from F by iteratively removing vertices whose degree is smaller than (1 − 2ε1/2) · eG. We claim that fewer than 2ε1/2 · eG vertices are removed this way and, consequently, the graph F is nonempty and its minimum degree is at least (1 − 2ε1/2) · eG. Suppose that this were not true. We would then have

(1 − 2ε1/2) · eG 2

- 1

- 2 − 2ε · e2G eF,


+ 2ε1/2 · eG · (1 − 2ε1/2) · eG < a contradiction.

eF

Finally, let G be the subgraph of G induced by the set of endpoints of the edges from V (F ). Let u be an arbitrary vertex of G . There must be another vertex v of G such that uv ∈ V (F ). Since degF uv (1−2ε1/2)·eG, the common neighbourhood of u and v in G induces a subgraph with at least (1 − 2ε1/2) · eG edges in G. In particular,

degG u degG (u,v) 2 · (1 − 2ε1/2) · eG (1 − 2ε1/2) · (2eG)1/2. Since u was arbitrary, we obtain the desired lower bound on the minimum degree of G .

- Proof of Claim 5.13. We may assume that ε < 1/16, as otherwise the assertion of the claim is trivially satisﬁed. For every edge e ∈ E(G), let te denote the number of copies of K3 in G that contain the edge e. Observe that, for each e ∈ E(G), there are at least 2te(te − 1) embeddings of


P4 into G that map the middle edge of P4 onto e. Since e∈E(G) te = |Emb(K3,G)|/2 and the function t  → 2t(t − 1) is convex, we conclude that

|Emb(K3,G)| eG ·

|Emb(K3,G)|

|Emb(P4,G)|

2te(te − 1) eG ·

2eG − 1 . Our assumptions imply that

e∈E(G)

(1 − ε) · (2eG)3/2 2eG

|Emb(K3,G)| 2eG and consequently,

1 ε · e1G/2 ε ·

ε ·

|Emb(K3,G)|2 2eG

(1 − ε)3 · (2eG)2 (1 − 3ε) · (2eG)2, It now follows from Claim 5.12 that G contains a subgraph G with minimum degree at least

|Emb(P4,G)| (1 − ε) ·

1 − 2 · (3ε)1/2 · (2eG)1/2 (1 − 4ε1/2) · (2eG)1/2, as claimed.

Our next lemma gives a tight upper bound on the number of stars K1,s in a given bipartite graph, as well as a structural characterisation of the bipartite graphs that are close to achieving this bound. This lemma and Theorem 5.11 above constitute the main combinatorial ingredient in the proof of Theorem 1.8. Given a graph G and a set U of vertices of G, we let EmbU(K1,s,G) denote the set of embeddings of K1,s into G that map the centre vertex to a vertex of U.

- Lemma 5.14. Let s 2 be an integer and suppose that G is a bipartite graph with parts U and V and at most q|V | edges, for some q ∈ (0,|U|]. Then the following holds:


| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


|V |

1 m0 m

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


−→ |V |

1 m0 m

Figure 4. The degree sequence on the left can be turned into the degree sequence on the right by moving mass from columns i m0 + 1 to columns j m0 + 1.

- (i) |EmbU(K1,s,G)| q + {q}s |V |s.
- (ii) For every positive ε, there exists a positive η such that, if |EmbU(K1,s,G)| (1 − η) · q + {q}s |V |s,


then there is a subset W ⊆ U of size q such that eG(W,V ) (1 − ε)q|V |, and a further subset W ⊆ W of size at least (1 − ε)|W|  such that degG u (1 − ε)|V | for every u ∈ W .

Proof. We will use the following inequality, valid for any two numbers x and y with x y 1:

(x + 1)s + (y − 1)s − xs − ys (x + 1 − y) · (x + 1)s−2. (28) It is clear that

|EmbU(K1,s,G)| =

(degG u)(degG u − 1)···(degG u − s + 1)

(degG u)s. (29)

u∈U

u∈U

Let m = |U| and, given a sequence d = (d1,...,dm), deﬁne S(d) =

m

dsi.

i=1

By the degree sequence of a bipartite graph with parts U and V , we will mean the sequence of degrees of the vertices in U, listed in a nonincreasing order. Thus (29) implies that |EmbU(K1,s,G)| S(dG), where dG is the degree sequence of G. Let m0 = eG/|V |  and deﬁne dmax = (d∗1,...,d∗m) by

 

|V | if i m0, {eG/|V |} · |V | if i = m0 + 1, 0 otherwise.

d∗i =



Note that mi=1 d∗i = eG; in particular, {eG/|V |} · |V | is an integer. We claim that dmax maximises S over all degree sequences whose sum is eG. Indeed, for any other such degree sequence d = (d 1,...,d m), there must be two distinct indices i and j such that 0 < d i d j < |V |. Let d be the degree sequence obtained from d by decreasing d i by one and increasing d j by one (and reordering the degrees, if necessary). It follows from (28) that

S(d ) − S(d ) = (d j + 1)s + (d i − 1)s − (d j)s − (d i)s (d j − d i + 1) · (d j + 1)s−2 1. Therefore,

|EmbU(K1,s,G)| S(dG) S(dmax) = eG/|V |  + {eG/|V |}s |V |s. Since eG q|V |, this completes the proof of the ﬁrst part of the lemma.

For the second stipulation of the lemma, ﬁx a positive ε. Let Ω be the set of degree sequences of bipartite graphs G with parts U and V for which there is a subset W ⊆ U of size eG/|V |  such that eG(W,V ) (1 − ε)eG and, additionally, a further subset W ⊆ W of size (1 − ε)|W|  such that degG u (1 − ε)|V | for each u ∈ W .

It suﬃces to show that any degree sequence d ∈/ Ω whose sum is eG satisﬁes S(d) < (1 − η)S(dmax), for some positive η that depends only on ε. Let d = (d1,...,dm). The crucial observation is that we may obtain dmax from d by successively increasing some di with i m0 +1 by one and, simultaneously, decreasing some dj with j m0 + 1 by one (see Figure 4). Note that, when doing so, we perform at least

m0

0+1,0 such operations. We split further analysis into two cases.

(|V | − di) + max d∗m

0+1 − dm

i=1

First, assume that mi=10 (|V | − di) ε2eG; this implies that m0 1. In this case, in at least ε2eG/2 steps of the above procedure, we will be increasing some di with i m0 which is, at this time, already at least (|V | + di)/2 (|V | + dm

)/2 − 1, while decreasing some dj with j m0 + 1 which is at most dm

0

. Inequality (28) implies that

0

s−2

ε2eG 2 ·

|V | + dm

|V | + dm

S(dmax) − S(d)

0

0

2 − dm

0 ·

.

2

ε2eG/m0, it follows that

Since our assumption implies that |V | − dm

0

s−2

2

ε2eG 2 ·

ε2eG 2m0 ·

ε4 2s+1 ·

|V | 2

eG m0|V |

S(dmax) − S(d)

· 2m0|V |s. Finally, we note that eG m0|V | and that S(dmax) (m0 + 1)|V |s 2m0|V |s, and thus S(dmax) − S(d)

=

ε4

2s+1 · S(dmax), proving S(d) < (1 − η)S(dmax) for some positive η.

Assume now that mi=10 (|V | − di) < ε2eG. Let W be the set comprising the eG/|V |  vertices with largest degrees in U. Suppose ﬁrst that eG(W,V ) (1 − ε)eG, but every set of (1 − ε)|W|  vertices of W contains a vertex of degree smaller than (1 − ε)|V |. In this case, (1 − ε)|W| 1, as otherwise the latter condition is vacuously false, and di < (1 − ε)|V | whenever i (1 − ε)|W| . Then

m0

(|V | − di) > m0 + 1 − (1 − ε)|W|  · ε|V | |W| − (1 − ε)|W|  · ε|V | ε2eG,

i=1

contradicting our assumption. Thus, since d ∈/ Ω, we may assume that eG(W,V ) < (1 − ε)eG. Therefore,

|W|

m0

m0

(|V | − di) > m0|V | − ε2eG.

di = m0|V | −

(1 − ε)eG >

di

i=1

i=1

i=1

This means, in particular, that m0 < eG/|V | and hence |W| = m0 + 1. Moreover,

|W|

0+1 + (ε − ε2)eG,

m0|V | + d∗m

0+1 = eG >

di + εeG > m0|V | + dm

i=1

0+1 > (ε−ε2)eG. Therefore, there exist at least (ε−ε2)eG/2 steps in which we increase dm

which implies that d∗m

0+1 −dm

0+1 at a time where it is already at least (ε − ε2)eG/2 . Inequality (28) implies that

(ε − ε2)eG 2

s

S(dmax) − S(d)

. However, we trivially have S(dmax) esG and thus

(ε − ε2)s

2s · S(dmax), completing the proof.

S(dmax) − S(d)

We remark that the extremal structures given by Theorem 5.11 and Lemma 5.14(ii) are quite diﬀerent and, in a sense, incompatible. This has the following technically important consequence: if a graph G simultaneously contains many copies of Kr and many copies of K1,r−1, then it can be split into two edge-disjoint graphs, one containing nearly all the copies of Kr and the other containing nearly all the copies of K1,r−1. The following lemma formalises this statement; its proof is similar to an argument of Lubetzky and Zhao [57]. We write G[U,V ] for the bipartite induced subgraph of G with parts U and V .

- Lemma 5.15. For every integer r 3 and positive real number ε, there is a positive η such that


the following holds. Let G be a graph on n vertices with eG ηn2. Then there exists a partition V (G) = U ∪ V satisfying |U| εn,

|Emb(Kr,G[V ])| |Emb(Kr,G)| − εer/G 2, and

|EmbU(K1,r−1,G[U,V ])| |Emb(K1,r−1,G)| − εeGnr−2. Proof. Assume that η is suﬃciently small, let U be the set of vertices in G with degree at least η1/3n, and let V = V (G) \ U. Note that |U| 2eG/(η1/3n) 2η2/3n εn.

Every embedding of Kr into G that maps a vertex of Kr to a vertex of U can be speciﬁed by ﬁrst choosing a vertex v of Kr, then a vertex of U that v will be mapped to, and ﬁnally an embedding of Kr−1 into G. Using Theorem 5.4, we thus obtain

2eG

η1/3n · (2eG)(r−1)/2. Since e1G/2 η1/2n, this implies the ﬁrst assertion of the lemma.

|Emb(Kr,G)| − |Emb(Kr,G[V ])| r · |U| · |Emb(Kr−1,G)| r ·

Next, note that

|Emb(K1,r−1,G)| = |EmbU(K1,r−1,G[U,V ])| + t1 + t2, (30)

where t1 is the number of embeddings of K1,r−1 into G that map the centre vertex and at least one leaf of K1,r−1 to U and t2 is the number of embeddings that map the centre vertex of K1,r−1 to V . We have

2

2eG η1/3n

t1 (r − 1) · |U|2 · nr−2 (r − 1)

nr−2 εeGnr−2/2,

- as eG ηn2. Finally, in order to bound t2, observe that every embedding counted by t2 can be speciﬁed by ﬁrst choosing a leaf a of K1,r−1, then choosing the image e of the edge of K1,r−1 incident with a, then choosing the endpoint v ∈ V of e that is the image of the centre vertex


of K1,r−1, and ﬁnally choosing the images of the remaining r − 2 leaves of K1,r−1 among the neighbours of v in G. Since every vertex v ∈ V has degree at most η1/3n, it follows that

t2 (r − 1) · eG · 2 · (η1/3n)r−2 εeGnr−2/2. Together with (30), these bounds on t1 and t2 imply the second assertion of the lemma.

6. Cliques in random graphs Fix an integer r 3 and let X = XK

n,pr be the number of r-vertex cliques in the random graph Gn,p. In this section, we shall use Theorem 3.1 not only to determine the logarithmic upper tail probability of X but also to provide a detailed description of the upper tail event. Before we restate the two theorems that will be proved in this section, we discuss the combinatorial constructions that are responsible for the localisation phenomenon in more detail.

As was shown in [57], when n−1 p(r−1)/2 1, there are essentially two optimal strategies for planting a subgraph inside Gn,p that increases the expected number of copies of Kr by the required δ E[X]. The ﬁrst, and most straightforward, involves planting a clique with δ1/rnp(r−1)/2

vertices; note that our assumption on p implies that this expression is unbounded and thus we may implicitly assume that it is an integer. Note that such a clique has close to

δ2/rn2pr−1 2

edges and contains approximately δ nr p(r

) = δ E[X] copies of Kr. If npr−1 is bounded from below, then there is an alternative strategy that competes with planting a clique. By a hub of order δnpr−1/r + 1, we mean a subgraph of Gn,p constructed as follows. Let U be a set of

2

δnpr−1/r vertices of Gn,p and let u be another vertex that lies outside of U. Connect every vertex in U to every vertex outside of U ∪ {u} and connect u to some {δnpr−1/r}1/(r−1) · n such vertices. Note that every hub has close to

δnpr−1/r + {δnpr−1/r}1/(r−1) · n

edges, which is Θ(n2pr−1), as npr−1 is bounded from below. Unlike in the previous construction, the hub itself contains no copies of Kr. However, as p 1, planting a hub creates approximately

δnpr−1/r · r− n1 copies of the star graph K1,r−1 whose centre vertex lies in U and approximately {δnpr−1/r} · r− n1 copies of K1,r−1 whose centre vertex is u. The total number of planted copies of K1,r−1 is thus approximately δpr−1 · nr = δ E[X] · p−(r−1

). Since each of the planted copies of K1,r−1 lies in a copy of Kr that now appears in Gn,p with probability p(r−1

2

), one expects to see approximately δ E[X] such extra copies of Kr. We remark that if npr−1 is large, then the contribution of the single vertex u becomes negligible and the hub construction can be described more concisely as connecting some δnpr−1/r vertices to all the others, using δn2pr−1/r edges.

2

We prove that, for a vast majority of values of p in the range of interest, the logarithmic upper tail probability of X corresponds to one of the two strategies described above. In particular, we show that

- (i) If npr−1 → 0, then the logarithmic upper tail probability is asymptotically equal to the ‘cost’ of planting the smallest clique that has δ E[X] copies of Kr.
- (ii) If npr−1 → ∞, then the logarithmic upper tail probability is asymptotically equal to the ‘cost’ of planting either a clique as above (when δ2/r δ/r) or the smallest hub that has


) copies of K1,r−1 (when δ2/r δ/r).

δ E[X] · p−(r−1

2

Note that in the regime npr−1 → ∞, we may approximate the number of edges planted in the hub construction by δn2pr−1/r. However, when npr−1 → c for some constant c ∈ (0,∞), this approximation is no longer valid and we are forced to account for the lack of smoothness that stems from the integral and fractional parts of δc/r. As a result, we ﬁnd that, for certain values of the parameters δ and c, the logarithmic upper tail probability corresponds to a mixture of the ﬁrst and second strategies: it is equal to the cost of planting a graph comprising both a hub and a clique, each contributing a nonnegligible proportion of the (expected) extra δ E[X] copies of Kr.

Finally, suppose that one conditions Gn,p on the upper tail event {X (1 + δ)E[X]}. We prove that, with probability close to one, the conditioned random graph contains a subgraph that very closely resembles the graph described by the optimal strategy (for the particular values of n, p, and δ). For example, in cases where the logarithmic upper tail probability corresponds to planting a clique, we show that Gn,p conditioned on the event {X (1 + δ)E[X]} contains a set of δ1/rnp(r−1)/2 vertices that induces an ‘almost-clique’, that is, a subgraph of density 1 − o(1).

We now turn to the details. As in the introduction, we deﬁne continuous functions ψr : (0,∞)2× [0,1] → (0,∞) and ϕr : (0,∞)2 → (0,∞) by

δ(1 − x) 2/r 2

1 r−1

xδc/r + {xδc/r}

ψr(δ,c,x) =

+

and ϕr(δ,c) = min

ψr(δ,c,x).

x∈[0,1]

c

Note that ψr(δ,npr−1,x) · n2pr−1 is approximately the number of edges in the disjoint union of a clique with δ(1 − x)np(r−1)/2 vertices and a hub of order δxnpr−1/r + 1. Recalling the discussion above, ϕr(δ,npr−1) · n2pr−1 then represents the smallest number of edges among all combinations of clique and hub that yield an expected δ E[X] copies of Kr−1.

In order to handle the three cases npr−1 → 0, npr−1 → c ∈ (0,∞), and npr−1 → ∞ in a uniﬁed manner, it will be convenient to extend ϕr to a continuous function ϕr : (0,∞) × [0,∞] → (0,∞). This extension may be deﬁned by noting that

ϕr(δ,c) = min{δ2/r/2,δ/r} uniformly as functions of δ. For every δ > 0 and c ∈ [0,∞], we then deﬁne the set X¯r(δ,c) = {x ∈ [0,1] : ϕr(δ,c) = lim

ϕr(δ,c) = δ2/r/2 and lim

lim

c→0

c→∞

ψr(δ,c ,x)}

c →c

of (asymptotic) minimisers to x  → ψr(δ,c,x). One can check that this set is nonempty for any δ and c, though it might contain more than one element. The following lemma describes the set of possible minimisers in more detail.

- Lemma 6.1. Let r 3 be an integer and let δ and c be positive real numbers. Let x∗ = r δc/r /(δc). Then


X¯r(δ,0) = 0 , X¯r(δ,c) ⊆ 0,x∗,1 , and X¯r(δ,∞) ⊆ 0,1 .

Proof. The statement for X¯r(δ,0) holds because limc→0 ψr(δ,c,x) = ∞ whenever x > 0. The statement for X¯r(δ,∞) follows because

ψr(δ,c,x) = (δ(1 − x))2/r/2 + xδ/r and the right-hand side is strictly concave in x ∈ [0,1]. In particular, since ϕr(δ,∞) = min {δ2/r,δ/r} = min

lim

c→∞

(δ(1 − x))2/r/2 + xδ/r,

x∈[0,1]

the equality ϕr(δ,∞) = limc→∞ ψr(δ,c,x) implies that x is one of the endpoints of the interval [0,1]. Assume now that c ∈ (0,∞). Treating r, δ, and c as ﬁxed, consider the function f : [0,1] → (0,∞) deﬁned by f(x) = ψr(δ,c,x). Since ψr is continuous, we have x ∈ X¯r(δ,c) if and only if x is a minimiser of f(x) in [0,1]. We cover the domain of f with essentially disjoint intervals as follows:

r δc

r δc

r δc

r δc

[0,1] =

[0,1] ∪

[1,2] ∪ ··· ∪

[ δc/r − 1, δc/r ] ∪

[ δc/r ,δc/r].

Observe that f is strictly concave on each of these intervals and thus f can achieve its minimum value only at an endpoint of one of the intervals, that is, either at some x for which δxc/r ∈ Z or

- at x = 1. Deﬁne the function h: [0,1] → (0,∞) by


δ(1 − x) 2/r 2

xδ r

+

h(x) =

and observe that h is strictly concave and that h(x) = f(x) whenever δxc/r ∈ Z. It follows that the minimum of f(x) is achieved either at x = 1 or at the smallest or largest x satisfying δxc/r ∈ Z. Since the latter two points are x = 0 and x = r δc/r /(δc) = x∗, respectively, we may conclude that the minimiser is in the set {0,x∗,1}, as desired.

Let us now state the two main results of this section. The following is a straightforward reformulation of Theorem 1.7.

- Theorem 6.2. Let r 3 be an integer and let X = XK


n,pr denote the number of r-vertex cliques in the random graph Gn,p. Then, for every ﬁxed positive constant δ and all p = p(n) such that n−1(log n)

1 r−2

r−1

2 1 and limn→∞ npr−1 = c ∈ [0,∞], lim

p

−log P X (1 + δ)E[X] n2pr−1 log(1/p)

= ϕr(δ,c). Recall the following three events:

n→∞

- (i) Let UT(δ) be the upper tail event {X (1 + δ)E[X]}.
- (ii) Let Cliqueε(x) be the event that Gn,p contains a set U ⊆ n of size at least (1 − ε)x1/rnp(r−1)/2 such that Gn,p[U] has minimum degree at least (1 − ε)|U|.
- (iii) Let Hubε(x) be the event that Gn,p contains a set U ⊆ n such that at least (1−ε)|U|  vertices in U have degree at least (1 − ε)n and


1 r−1

e(U, n \ U) (1 − ε)n xnpr−1/r + {xnpr−1/r}

.

Together with Lemma 6.1, the following theorem directly implies Theorem 1.8. Theorem 6.3. Let r 3 be an integer and let X = XK

n,pr denote the number of r-vertex cliques in the random graph Gn,p. Then, for every ﬁxed positive constant δ and all p = p(n) such that n−1(log n)

1 r−2

r−1

2 1 and limn→∞ npr−1 = c ∈ [0,∞], lim n→∞

p

Cliqueε(δ(1 − x)) ∩ Hubε(δx) | UT(δ) = 1.

### P

x∈X¯(δ,c)

In order to prove Theorems 6.2 and 6.3, we will ﬁrst relate −log P X (1 + δ)E[X] to the solutions of the optimisation problem

ΦX(δ) = min eG log(1/p) : G ⊆ Kn and EG[X] (1 + δ)E[X] , where EG[X] = E[X | G ⊆ Gn,p]. For every ε > 0, we deﬁne the event

Near-min(ε) = {Gn,p contains a subgraph G such that eG log(1/p) (1 + ε)ΦX(δ + ε) and

EG[X] (1 + δ − ε)E[X]}. Using Theorem 3.1, we shall prove the following result.

- Proposition 6.4. For every integer r 3 and all positive reals ε and δ, there exists a positive constant C such that the following holds. Suppose that an integer n and p ∈ (0,1) satisfy

Cn−1(log n)1/(r−2) p(r−1)/2 1/C. Then X = XK

n,pr satisﬁes

(1 − ε)ΦX(δ − ε) −log P X (1 + δ)E[X] (1 + ε)ΦX(δ + ε). Furthermore,

P Near-min(ε) | X (1 + δ)E[X] 1 − ε.

In order to complete the proof of Theorem 6.2, we must also evaluate the asymptotic value of the function ΦX. This is the content of our second proposition.

- Proposition 6.5. Let r 3 be an integer and let X = XK


n,pr. Then, for every ﬁxed positive real δ and all p = p(n) such that n−1 p(r−1)/2 1 and limn→∞ npr−1 = c ∈ [0,∞],

ΦX(δ) n2pr−1 log(1/p)

= ϕr(δ,c).

lim

n→∞

We recall that, when c ∈ {0,∞}, this result was already established in [57]. The proof we provide is not unsimilar to that work, although it is slightly easier, as ΦX is a discrete restriction of the variational problem in their work (see the discussion following Proposition 4.2, which discusses the same issue in the case of arithmetic progressions). However, the extension to the case c ∈ (0,∞) is delicate, and requires the use of the more precise result of Lemma 5.14.

We would like to emphasise that, while the proofs of Propositions 6.4 and 6.5 have certain similarities, they are conceptually very diﬀerent. The analysis of the variational problem in the proof of Proposition 6.5 relies on bounding the maximal number of embeddings of Kr and K1,r−1 in a graph with given numbers of vertices and edges, using the results of Section 5.2. In contrast, the proof of Proposition 6.4 exploits the bounds on the number of embeddings of Kr and K1,r−1 (as well as several other key graphs) containing a given edge of the core, proved in Section 5.3. The deﬁning properties of a core allow us to translate these upper bounds on the number of local embeddings into lower bounds on the degrees of the endpoints of edges of a core. These degree restrictions are suﬃcient to prove that the family of cores is entropically stable.

Finally, to prove Theorem 6.3, we characterise the near-minimisers of the optimisation problem for ΦX(δ). This is what we do in the ﬁnal proposition of this section.

- Proposition 6.6. Let r 3 be an integer and let X = XK


n,pr. For all ﬁxed ε,δ > 0 and c ∈ [0,∞], there exists some positive constant η such that the following holds. Assume p = p(n) is such that n−1 p(r−1)/2 1 and limn→∞ npr−1 = c. Then

Near-min(η) ⊆

Cliqueε(δ(1 − x)) ∩ Hubε(δx)

x∈X¯(δ,c)

whenever n is suﬃciently large. The propositions above readily imply Theorems 6.2 and 6.3.

- 6.1. Proof of Proposition 6.4. We may assume without loss of generality that ε is suﬃciently small, say ε < min {1/2,δ/2}. Note also that the case n < r is trivial; indeed, in that case


X is identically zero and thus −log P X (1 + δ)E[X] = 0 = ΦX(δ) for every δ ∈ R, and Near-min(ε) holds vacuously. We may therefore assume that n r 3, which, in turn, implies that n C.

Set N = n2 and let Y = (Y1,...,YN) be the sequence of indicator random variables of the events that e ∈ E(Gn,p), where e ranges over n 2 in some arbitrary order. Observe that Y is a vector of independent Ber(p) random variables and that X is a nonzero polynomial with nonnegative coeﬃcients and degree at most 2 r in the coordinates of Y . Let K = K(r,ε,δ) be the constant given by Theorem 3.1. We shall show that X satisﬁes the various assumptions of the theorem; the theorem then implies both assertions of the proposition.

First, our assumption on p implies that p 1 − ε, provided that C is suﬃciently large. Recall that N(J,G) denotes the number of copies of J in G. Note that for all J ⊆ Kr without

isolated vertices and all G ⊆ Kn, we can trivially bound N(J,G) from above by ee

G . It follows that

J

p(r

)−eJ 2(r

) · max

p(r

)−(vJ

)

EG[X] − E[X]

N(J,G) · nr−v

ee

G · nr−v

2

2

2

2

J

J

J

∅ =J⊆Kr

∅ =J⊆Kr

) min2 k r nkp(k

nrp(r

(2eG)(r

) ·

2

2

),

2

where the sum ranges over all nonempty subgraphs J ⊆ Kr without isolated vertices. Since E[X] = Θ nrp(r

) and our assumption on p implies that nkp(k

) C2/(r−1) for each k ∈ {2,...,r}, the right-hand side above is at most (δ/2)E[X] unless eG K, provided that C is suﬃciently large. Therefore, ΦX(δ−ε) ΦX(δ/2) K log(1/p). Furthermore, since a clique with

2

2

(1 + 2δ)1/rnp(r−1)/2 vertices contains at least (1 + δ + ε)E[X] copies of Kr and has fewer than K n2pr−1 edges, for some constant K = K (δ), we deduce that ΦX(δ + ε) K n2pr−1 log(1/p).

Recall that a graph G∗ ⊆ Kn is a core if it satisﬁes the following three conditions: (C1) EG∗[X] (1 + δ − ε)E[X], (C2) eG∗ K · ΦX(δ + ε), and

(C3) mine∈E(G∗) EG∗[X] − EG∗\e[X] E[X]/ K · ΦX(δ + ε) .

Our goal is to show that, for every integer m, there are at most (1/p)εm/2 cores with m edges. The key observation is that, for any core G∗ and any edge uv of G∗, either u and v have many common neighbours or the sum of the degrees of u and v is large. More precisely, letting degG∗(u,v) denote the number of common neighbours of u and v in G∗, we shall establish the following statement.

Claim 6.7. There exists a positive constant η = η(δ,r,K) such that, for every core G∗ and each edge uv ∈ E(G∗), either

ηnp(r−1)/2 log(1/p) 1/(r−2)

ηn log(1/p)

degG∗(u,v)

or degG∗ u + degG∗ v

.

The above claim readily implies the desired bound on the number of cores with m edges. Note ﬁrst that this number is zero whenever m > KK n2pr−1 log(1/p), see (C2), so we may assume that m KK n2pr−1 log(1/p). Given a core G∗, we denote by AG∗ the set of vertices of G∗ with degree at least ηnp(r−1)/2/ log(1/p) 1/(r−2) and by BG∗ ⊆ AG∗ the set of vertices of G∗ with degree at least ηn/

big(2log(1/p) . Since G∗ has m edges,

2m log(1/p) 1/(r−2) ηnp(r−1)/2 and |BG∗| b :=

4mlog(1/p) ηn

|AG∗| a :=

Claim 6.7 states that every edge of G∗ is either fully contained in AG∗ or has at least one endpoint in BG∗. In particular, for ﬁxed sets B ⊆ A ⊆ n with |A| = a and |B| = b, there are at most

a2/2+bn

m cores G∗ with m edges that satisfy AG∗ ⊆ A and BG∗ ⊆ B. We can thus (generously) upper bound the number of cores with m edges by

a2/2 + bn m

n a

n b

.

Recalling the inequality xy (ex/y)y, valid for all nonnegative integers x and y, we may conclude that the number of cores with m edges is at most

m

2em log(1/p) 2/(r−2) η2n2pr−1 +

4elog(1/p) η

6m(log(1/p))1/(r−2) ηnp(r−1)/2

·

.

n

Since p(r−1)/2 Cn−1(log n)1/(r−2), the ﬁrst factor is at most eεmlog(1/p)/4. Since we have assumed that m KK n2pr−1 log(1/p) and 1/p C2/(r−1), the second factor is at most eO(mlog log(1/p)) eεmlog(1/p)/4. This shows that the number of cores with m edges is indeed at most (1/p)εm/2, as claimed.

Proof of Claim 6.7. For any nonempty J ⊆ Kr, we shall let N(J,G∗;uv) denote the number of copies of J in G∗ that contain the edge uv. For the sake of brevity, we set mmax = KK · n2pr−1 log(1/p). Observe that

p(r

)−eJ,

EG∗[X] − EG∗\uv[X]

N(J,G∗;uv) · nr−v

2

J

∅ =J⊆Kr

where J ranges over all nonempty subgraphs of Kr that have no isolated vertices. Since E[X] = n r p(r

) and ΦX(δ + ε) K n2pr−1 log(1/p) = mmax/K, it follows from (C3) in the deﬁnition of the core that

2

N(J,G∗;uv) nvJpeJ

E[X] K · ΦX(δ + ε)

γ mmax

,

∅ =J⊆Kr

where γ = γ(r) is a constant that depends only on r.

S0,4 S1,3 S2,2

Figure 5. The double stars with six vertices.

For every edge ab ∈ E(J), let Emb(J,G∗;ab,uv) denote the set of embeddings of J into G∗ that map ab to uv. Then the above inequality implies that there is a nonempty J ⊆ Kr with no isolated vertices, an edge ab ∈ E(J), and a constant γ = γ (r) such that

|Emb(J,G∗;ab,uv)| nvJpeJ

γ mmax

. (31)

For nonnegative integers i and j, let Si,j denote the graph obtained from a copy of K1,i and a copy of K1,j by joining their centres (vertices of degrees i and j, respectively) by an edge; see Figure 5 for an illustration. As the graphs K1,i are often called stars, we shall refer to the Si,j as double stars. Moreover, we shall call an edge of Si,j whose endpoints have degrees i + 1 and j + 1 a centre edge. Note that if i,j > 0, then Si,j has only one centre edge; otherwise, Si,j is just a star graph and each of its edges is a centre edge.

We shall now show that, unless degG∗(u,v) np(r−1)/2, any graph J that satisﬁes (31) for some ab ∈ E(J) must be either Kr or a double star with r vertices. We ﬁrst show how this fact implies the assertion of the claim. Assume ﬁrst that

nr−2p(r−1

) log(1/p)

γ nrp(r

) mmax

2

2

γ KK ·

=

|Emb(Kr,G∗;ab,uv)|

.

Since |Emb(Kr,G∗;ab,uv)| 2degG∗(u,v)r−2, we conclude that

1/(r−2)

np(r−1)/2 log(1/p) 1/(r−2)

γ 2KK

degG∗(u,v)

·

,

as claimed. Next, assume that, for some i and j with i + j = r − 2,

γ nrpi+j+1 mmax

nr−2 log(1/p)

γ KK ·

|Emb(Si,j,G∗;ab,uv)|

=

.

If ab is a centre edge of Si,j, then |Emb(Si,j,G∗;ab,uv)| (degG∗ u + degG∗ v)i+j (degG∗ u + degG∗ v) · (2n)r−3. Otherwise, we have i,j > 0 and so |Emb(Si,j,G∗;ab,uv)| (degG∗ u + degG∗ v)min{i,j} · nmax{i,j} (degG∗ u + degG∗ v) · (2n)r−3 as well. Thus, in both cases,

γ 2r−3KK ·

n log(1/p)

degG∗ u + degG∗ v

, which completes the proof of the claim.

It remains to prove our assertion. We ﬁrst consider the special case r = 3. The only nonempty subgraph of K3 with no isolated vertices that is not isomorphic to a double star with three vertices is K2. However, as p C−2/(r−1) = C−1, we have

2 n2p

2log C Cn2p2 log(1/p)

|Emb(K2,G∗;ab,uv)| n2p

γ mmax

=

<

whenever C is suﬃciently large, which contradicts (31). We henceforth assume that r 4.

By way of contradiction, suppose that J is neither Kr nor a double star with r vertices and that degG∗(u,v) < np(r−1)/2. Let ab be an arbitrary edge of J, let Jab be the subgraph of J induced by V (J) \ {a,b}, and let αab∗ be the fractional independence number of Jab. By Lemma 5.1, there is a partition of V (Jab) into V1 and V2 such that

- (P1) |V1|/2 + |V2| = αab∗ ,


- (P2) V1 can be covered by a collection of vertex-disjoint edges and cycles of Jab.


Among all partitions satisfying (P1) and (P2), choose one that maximises the number of common neighbours of a and b in V2, that is, the cardinality of the set

X = {c ∈ V2 : ac,bc ∈ E(J)}. Finally, let v1 = |V1|, v2 = |V2|, and x = |X|.

We now observe that for every partition satisfying (P1) and (P2), we have |Emb(J,G∗;ab,uv)| 2 · degG∗(u,v)x · (2eG∗)v1/2 · min{2eG∗,n}v

2−x. (32) To see this, note ﬁrst that there are two embeddings of ab onto uv. Since X lies in the common neighbourhood of a and b, each such embedding can be extended to an embedding of J[{a,b}∪X] in at most degG∗(u,v)x ways. Next, since V1 can be covered by cycles and edges of J (by property (P2)), Lemma 5.5 implies that every embedding of J[{a,b} ∪ X] can be extended in at most (2eG∗)v1/2 ways to an embedding of J[{a,b} ∪ X ∪ V1]. Finally, since J contains no isolated vertices, any embedding of J[{a,b} ∪ X ∪ V1] can be extended in at most min{2eG∗,n}v

2−x ways to an embedding of J.

Combining (31), (32), the inequality eG∗ mmax, which follows from (C2), and the assumption degG∗(u,v) < np(r−1)/2, we deduce that

x

· (2mmax)v1/2+1 · min{2mmax,n}v

np(r−1)/2

2−x

pe

γ nv

J

J

1 KK log(1/p) x/2

· (2mmax)v1/2+x/2+1 · min{2mmax,n}v

=

2−x.

On the other hand,

eJ/(r−1)

mmax KK log(1/p)

J = n2pr−1 eJ/(r−1) · nv

J−2eJ/(r−1). Therefore, for some constant K = K (K,K ,r), we must have

J−2eJ/(r−1) =

nv

· nv

pe

J

(mmax)v1/2+x/2−eJ/(r−1)+1 · n2e

J/(r−1)−vJ · min{mmax,n}v

2−x K log(1/p) −K . (33)

In order to reach the desired contradiction, it suﬃces to prove that there is some positive σ = σ(r) such that the left-hand side of (33) is bounded from above by max {n−1,KK · pr−1 log(1/p)}σ. We ﬁrst observe that such an upper bound is implied by the following inequality:

max v1/2 + v2 − x/2 − eJ/(r − 1) + 1, 0 < vJ − 2eJ/(r − 1). (34) Indeed, if mmax n, then the left-hand side of (33) is upper bounded by

(mmax)v1/2+v2−x/2−eJ/(r−1)+1 · n2e

J/(r−1)−vJ

max {n2e

J/(r−1)−vJ,nv

1/2+v2−x/2+1−(vJ−eJ/(r−1))}. On the other hand, if n < mmax = KK ·n2pr−1 log(1/p), then the left-hand side of (33) becomes KK · n2pr−1 log(1/p) v1/2+x/2−eJ/(r−1)+1 · n2e

J/(r−1)−vJ+v2−x

= KK · pr−1 log(1/p) vJ−eJ/(r−1)−(v1/2+v2−x/2+1) , using v1 + v2 = vJ

= vJ − 2. Note that (34) guarantees that, in both cases, the left-hand side of (33) is at most max {n−1,KK · pr−1 log(1/p)}σ, for a suitable positive σ = σ(r).

ab

In order to complete the proof of Claim 6.7, we now prove inequality (34). Recall that V (Jab) = V1 ∪ V2 is a partition that satisﬁes (P1) and (P2) that maximises the cardinality of the set X = {c ∈ V2 : ac,bc ∈ E(J)}. Since, by the deﬁnition of X, each vertex in V2 \ X has at most one neighbour in {a,b},

+ 2v1 + v2 + x + 1 = eJ

+ 3vJ − 2αab∗ + x − 5 (35)

eJ eJ

ab

ab

- a

- b c d


V2 V1

Figure 6. Illustration for the case Jab = K1,r−3 and r > 4. Any partition V (Jab) = V 1 ∪ V 2 obtained by exchanging d with a vertex from V2 satisﬁes (P1) and (P2) but violates (D3).

and equality holds only if every vertex in V1 is adjacent to both a and b and every vertex in V2 \ X is adjacent to exactly one of a and b. Moreover, Lemma 5.2 and Remark 5.3 give

ab − αab∗ ) = (vJ − 3)(vJ − αab∗ − 2), (36) where equality holds only if Jab is complete, empty, or isomorphic to K1,v

(vJ

ab − 1)(vJ

eJ

ab

J−3. Putting (35) and (36) together yields the inequality

eJ (vJ − 1)(vJ − αab∗ − 1) + x. (37)

Moreover, inequality (37) is strict unless both (35) and (36) hold with equality. Rearranging (37) gives the inequality

vJ − 1 r − 1 · (vJ − αab∗ − 1) +

eJ r − 1

x r − 1

x 2

vJ − αab∗ − 1 +

. (38)

Since αab∗ vJ

= vJ − 2 and r 4, the second inequality in (38) is strict unless vJ = r and x = 0. Consequently, the left-hand and the right-hand sides of (38) can be equal only if the following conditions are satisﬁed for every partition V (Jab) = V1 ∪ V2 with properties (P1) and (P2):

ab

(D1) Jab is either Kr−2, Er−2 (the empty graph with r − 2 vertices), or K1,r−3; (D2) every vertex in V1 is adjacent to both a and b; (D3) every vertex of V2 is adjacent to exactly one of a and b.

We now show that our assumptions preclude (D1)–(D3) holding simultaneously. Indeed, note ﬁrst that, if Jab = Kr−2 (which also includes the case Jab = K1,r−3 and r = 4), then αab∗ = vJ

/2. Since v1/2 + v2 = αab∗ and v1 + v2 = vJ

ab

, this implies V1 = V (Jab). Then (D2) shows that J = Kr, a contradiction. Second, if Jab = Er−2, then αab∗ = r − 2. Since v1/2 + v2 = αab∗ and v1 + v2 = r − 2, this implies V2 = V (Jab) and it follows from (D3) that J is a double star whose centre edge is ab, another contradiction. Finally, suppose that Jab = K1,r−3 and r > 4. Since αab∗ = v1/2 + v2 = r − 3 and v1 + v2 = r − 2, we see that v1 = 2 and v2 = r − 4. Property (P2) implies that V1 = {c,d}, where c is the vertex of degree r −3 in Jab and d is one of its neighbours. Since d ∈ V1, it must be adjacent to both a and b (see Figure 6 for an illustration). Let e be an arbitrary vertex of V2; there is at least one such vertex as v2 = r − 4 1. The partition of V (Jab) into V 1 = {c,e} and V 2 = (V2 \ {e}) ∪ {d} satisﬁes both conditions (P1) and (P2) but the set X = {c ∈ V 2 : ac ,vc ∈ E(Jab)} is nonempty (as it contains the vertex d); this contradicts property (D3) for the partition V (J) = V 1 ∪ V 2.

ab

To summarise, at least one of the inequalities in (38) is strict. Since J = Kr, not every vertex of J has degree r − 1 and thus 2eJ < (r − 1) · vJ. We conclude that

max αab∗ − eJ/(r − 1) − x/2 + 1, 0 < vJ − 2eJ/(r − 1). Since αab∗ = v1/2 + v2, this is exactly (34).

- 6.2. Proof of Proposition 6.5. We begin by showing that


ΦX(δ) n2pr−1 log(1/p)

lim sup

ϕr(δ,c). (39)

n→∞

For every small ε > 0 and suﬃciently large n, we shall construct a graph G with vertex set n and at most (ϕr(δ + ε,c) + ε) · n2pr−1 edges that satisﬁes EG[X] (1 + δ)E[X]. The existence of such a graph and the continuity of ϕr will imply that

ΦX(δ) n2pr−1 log(1/p)

lim sup

lim

ϕr(δ + ε,c) + ε = ϕr(δ,c),

ε→0

n→∞

as required. Let x ∈ X¯(δ + ε,c) and note that it follows from Lemma 6.1 that x = 0 if c = 0. Set

1 = (δ + ε)(1 − x) 1/rnp(r−1)/2 and 2 = x(δ + ε)npr−1/r.

and ﬁx an arbitrary partition n = {u} ∪ U1 ∪ U2 ∪ U3, where |U1| = 1 and |U2| = 2 . Let G be the union of the clique on U1, the complete bipartite graph between U2 and U3, and an arbitrary star, centred at u, with  { 2}1/(r−1)|U3|  edges whose non-u endpoints are in U3. We have

eG 1 2

+ 2 · |U3| + { 2}1/(r−1) · |U3| (δ + ε)(1 − x) 2/rn2pr−1

+ 2 + { 2}1/(r−1) · n (δ + ε)(1 − x) 2/r 2

2

+ { 2}1/(r−1) npr−1 · n2pr−1

+ 2

= ψr(δ + ε,npr−1,x) · n2pr−1, and our choice of x ensures that ψr(δ + ε,npr−1,x) ϕr(δ + ε,c) + ε for all large enough n. It remains to show that EG[X] (1 + δ)E[X]. To this end, observe ﬁrst that:

- (i) The complete graph G[U1] contains

1

r copies of Kr.

- (ii) The complete bipartite graph G[U2,U3] contains 2 · |U

3|

r−1 copies of K1,r−1 whose centre vertex lies in U2.

- (iii) The star G[u,U3] contains  { 2}1/(r−1)|U3| 


r−1 copies of K1,r−1. In particular,

n − vJ r − vJ · p(r

)(p−e

EG[X] − E[X] =

N(J,G) ·

− 1)

2

J

∅ =J⊆Kr

+  { 2}1/(r−1)|U3|  r − 1 · p(r

)−(r−1) .

|U3| r − 1

(1 − p) · r 1

+ 2 ·

2

We now estimate the right-hand side of the above inequality. Since np(r−1)/2 → ∞, we have

nrp(r

) r!

( 1 − r)r r!

2

1

(δ + ε)(1 − x) − ε/2 ·

,

r

provided that n is suﬃciently large. In the case c = 0, this is already suﬃcient, as x = 0 and

EG[X] − E[X] (1 − p) · r 1

nrp(r

) r!

2

(1 − p) · (δ + ε/2) ·

δ E[X].

We may therefore assume that c ∈ (0,∞]. Since p → 0, and thus |U3|/n → 1, we have

+ { 2}1/(r−1)|U3| − r r−1

+  { 2}1/(r−1)|U3|  r − 1 2 ·

(1 − ε2) · nr−1 (r − 1)!

|U3| r − 1

2 ·

(r − 1)! (1 − ε2) · 2 · nr−1

ε2nr−1 (r − 1)!

(r − 1)! −

nrpr−1 r!

ε2r npr−1 ·

= (1 − ε2)x(δ + ε) −

.

Consequently,

nrp(r

) r!

ε2r npr−1 ·

2

EG[X] − E[X] (1 − p) · (δ + ε)(1 − x) − ε/2 + (1 − ε2)x(δ + ε) −

ε2r npr−1 · E[X] δ E[X],

(1 − p) · δ + ε/2 − ε2(δ + ε) −

where the last inequality holds for all suﬃciently small ε since npr−1 → c > 0. This completes the proof of (39).

It remains to prove the matching lower bound

ΦX(δ) n2pr−1 log(1/p)

lim inf

ϕr(δ,c). (40)

n→∞

Fix ε > 0 small enough and suppose that n is suﬃciently large. By the continuity of ϕr, it is enough to show that any graph G on n vertices satisfying

EG[X] (1 + δ)E[X]

has at least (1 − ε) · ϕr(δ − ε,c) · n2pr−1 edges. By way of contradiction, assume that eG < (1 − ε) · ϕr(δ − ε,c) · n2pr−1. Note that, for all large enough n,

nrp(r

) r!

)−eJ,

· p(r

2

(δ − ε/4) ·

δ E[X] EG[X] − E[X]

N(J,G) · nr−v

2

J

∅ =J⊆Kr

where the sum ranges over the nonempty subgraphs J of Kr without isolated vertices, so

N(J,G) nvJpeJ

δ − ε/3 r!

. (41)

∅ =J⊆Kr

Using our assumed upper bound on eG, Theorem 5.4 implies that

(2eG)vJ−α∗J · min {2eG,n}2α

∗ J−vJ

N(J,G) δnvJpeJ

nvJpeJ C ·

p(r−1)(v

min {(n2pr−1)α

J−α∗J)} nvJpeJ

∗

J,nv

J

for a suitable constant C. If the minimum is achieved by the ﬁrst term, then npr−1 1, and thus (n2pr−1)α

∗ J

J−eJ/(r−1) nα

∗

J−vJ+eJ/(r−1) · npr−1 α

J−vJ+eJ/(r−1),

= nα

∗

∗

nvJpeJ

as αJ∗ vJ/2 eJ/(r−1) for every graph J with maximum degree at most r−1. A straightforward algebraic manipulation in the case where the minimum is achieved by the second term then shows that, in both cases,

N(J,G) nvJpeJ

J−eJ/(r−1).

∗

C · min {n−1,pr−1}vJ−α

If J ⊆ Kr is not equal to either Kr or K1,r−1, then Lemma 5.2 and the remark that follows it imply that vJ − αJ∗ − eJ/(r − 1) > 0, and then the right-hand side goes to zero as n → ∞. It thus follows from (41) that

N(Kr,G) nrp(r

δ − ε/2 r!

N(K1,r−1,G) nrpr−1

+

,

)

2

or, equivalently, since |Aut(Kr)| = r! and |Aut(K1,r−1)| = (r − 1)!, |Emb(Kr,G)| + r · |Emb(K1,r−1,G)| · p(r

)−r+1 (δ − ε/2) · nrp(r

). (42)

2

2

Recalling our assumption eG < (1 − ε) · ϕr(δ − ε,c) · n2pr−1 n2, it follows from Lemma 5.15 that there is a partition V (G) = U ∪ V such that |U| ε2n,

|Emb(Kr,G[V ])| |Emb(Kr,G)| − ε2er/G 2 |Emb(Kr,G)| − εnrp(r

)/4,

2

and, recalling that EmbU(K1,r−1,G) denotes the set of embeddings of K1,r−1 into G that map the centre vertex of K1,r−1 to a vertex of U,

r · |EmbU(K1,r−1,G[U,V ])| · p(r

)−r+1 r · |Emb(K1,r−1,G)| · p(r

)−r+1 − ε2eGnr−2 · p(r

)−r+1

2

2

2

,

r · |Emb(K1,r−1,G)| · p(r

)−r+1 − εnrp(r

)/4

2

2

where the stated inequalities are valid if ε is suﬃciently small. From this and (42), we obtain |Emb(Kr,G[V ])| + r · |EmbU(K1,r−1,G[U,V ])| · p(r

); consequently, there exists an x ∈ [0,1] such that

)−r+1 (δ − ε) · nrp(r

2

2

) and

|Emb(Kr,G[V ])| (1 − x) · (δ − ε) · nrp(r

2

). By Theorem 5.4 and Lemma 5.14, we thus obtain the bounds

)−r+1 x · (δ − ε) · nrp(r

r · |EmbU(K1,r−1,G[U,V ])| · p(r

2

2

(2eG[V ])r/2 (1 − x) · (δ − ε) · nrp(r

)

2

( eG[U,V ]/|V |  + {eG[U,V ]/|V |}r−1) · nr−1 x · (δ − ε) · nrpr−1/r, and solving for eG[V ] and eG[U,V ], we get

eG[V ] (1 − x) · (δ − ε) 2/r · n

2pr−1

2 eG[U,V ] |V | · x · (δ − ε)npr−1/r + {x · (δ − ε)npr−1/r}1/(r−1) . Finally, since |V | = n − |U| (1 − ε2)n, the deﬁnition of ψr shows that

eG eG[V ] + eG[U,V ] (1 − ε2) · ψr(δ − ε,npr−1,x) · n2pr−1.

As ψr(δ − ε,npr−1,x) ϕr(δ − ε,npr−1) → ϕr(δ − ε,c), this contradicts our assumption that eG < (1 − ε) · ϕr(δ − ε,c) · n2pr−1, provided that ε is suﬃciently small and n is large enough.

- 6.3. Proof of Proposition 6.6. Fix ε,δ > 0 and c ∈ [0,∞] and assume that npr−1 → c. We ﬁx three additional positive constants η, η , and γ, where γ is suﬃciently small given the parameters of the proposition, η is suﬃciently small given γ, and ﬁnally η is suﬃciently small given both η and γ.


If Near-min(η) occurs, then Gn,p contains a subgraph G such that eG log(1/p) (1+η)ΦX(δ+η) and EG[X] (1 + δ − η)E[X]. We claim that, if n is suﬃciently large, then every such graph admits a partition V (G) = U ∪ V such that, for some x ∈ X¯(δ,c),

- (i) V contains a subset V of size at least (1 − ε) δ(1 − x) 1/rnp(r−1)/2 such that G[V ] has minimum degree at least (1 − ε)|V |.


- (ii) U contains a set W ⊆ U such that at least (1 − ε)|W|  vertices in W have degree at least (1 − ε)n and


e(W,V ) (1 − ε)n δxnpr−1/r + {δxnpr−1/r}1/(r−1) . Note that these properties imply Cliqueε(δ(1 − x)) ∩ Hubε(δx).

By repeating the argument found in the proof of the lower bound in Proposition 6.5, we can ﬁnd a partition V (G) = U ∪ V and some x ∈ [0,1] such that

|Emb(Kr,G[V ])| (1 − x ) · (δ − 2η) · nrp(r

) r · |EmbU(K1,r−1,G[U,V ])| · p(r

2

(43)

)−r+1 x · (δ − 2η) · nrp(r

)

2

2

and

eG[V ] (1 − x ) · (δ − 2η) 2/r · n

2pr−1 2

(44)

eG[U,V ] x (δ − 2η)npr−1/r + {x (δ − 2η)npr−1/r}1/(r−1) · n.

It follows that eG eG[V ] + eG[U,V ] ψr(δ − 2η,npr−1,x ) · n2pr−1. Thus, by Proposition 6.5, ψr(δ − 2η,npr−1,x )

(1 + η)ΦX(δ + η) n2pr−1 log(1/p)

eG n2pr−1

(1 + 2η)ϕr(δ + η,c)· (45)

Our next claim tells us how to choose the constant η. Given a set S ⊆ R, we write Bη (S) = {x ∈ R : infs∈S |x − s| < ε} for the η -neighbourhood of S.

- Claim 6.8. We may choose η = η(η ) > 0 such that x ∈ Bη (X¯r(δ,c)) whenever n is suﬃciently large.


Proof. Suppose there is no such choice. Then, by invoking (45) with successively smaller values of η, we ﬁnd that there is a subsequence (ηm,cm,xm) of points in (0,∞)2 × [0,1] such that ηm → 0 and cm → c as m → ∞, and, for all m, we have xm ∈/ Bη (X¯r(δ,c)) and

ϕr(δ − 2ηm,cm) ψr(δ − 2ηm,cm,xm) (1 + 2ηm)ϕr(δ + ηm,c).

Since both the left-hand and the right-hand sides above converge to ϕr(δ,c) as m → ∞, so must ψr(δ − 2ηm,cm,xm). Denote by (η ,c ,x ) a subsequence on which x converges to some x∞ ∈ [0,1]. We claim that x∞ ∈ X¯r(δ,c), which contradicts the fact that x ∈ / Bη (X¯r(δ,c)) for all .

If c = 0, then we have x∞ = 0 ∈ X¯r(δ,c), since otherwise the deﬁnition of ψr would imply that ψr(δ − 2η ,c ,x ) → ∞. If c ∈ (0,∞), then continuity of ψr implies that ϕr(δ,c) = lim →∞ ψr(δ − 2η ,c ,x ) = ψr(δ,c,x∞) and thus x∞ ∈ X¯r(δ,c). Finally, if c = ∞, then (δ,x)  → ψr(δ,cm,x) converges uniformly to the continuous function (δ,x)  → (δx)2/r/2 + δx/r, which implies that

(δx∞)2/r 2

δx∞ r

ψ(δ,c ,x∞), so x∞ ∈ X¯r(δ,c) in this case as well.

lim

ψr(δ − 2η ,c ,x ) =

+

= lim

c →∞

→∞

Suppose now that x ∈ Bη (X¯(δ,c)). Since the right-hand sides of (43) and (44) are continuous in x , we may choose η and η suﬃciently small, as a function of γ, so that there is some x ∈ X¯r(δ,c) such that

|Emb(Kr,G[V ])| (1 − x) · (δ − γ) · nrp(r

) r · |EmbU(K1,r−1,G[U,V ])| · p(r

2

)−r+1 x · (δ − γ) · nrp(r

), eG[V ] (1 − x) · (δ − γ) 2/r · n

2

2

2pr−1 2

eG[U,V ] x(δ − γ)npr−1/r + {x(δ − γ)npr−1/r}1/(r−1) · n.

Since eG[V ] + eG[U,V ] eG (1 + 2η)ψr(δ + η,c,x ) · n2pr−1 and since the lower bounds on eG[V ] and eG[U,V ] in (44) sum to ψr(δ − 2η,npr−1,x ) · n2pr−1, the two lower bounds on eG[V ] and eG[U,V ] stated above must be nearly tight. More precisely, the continuity of ψr implies that we may choose η and η suﬃciently small so that

eG[V ] (1 − x) · (δ + γ) 2/r · n

2pr−1 2

eG[U,V ] x(δ + γ)npr−1/r + {x(δ + γ)npr−1/r}1/(r−1) · n.

Finally, if we choose γ suﬃciently small, then the above statements for G[V ] and Theorem 5.11 yield a set V ⊆ V satisfying the conditions in (i). Similarly, the statements for G[U,V ] and Lemma 5.14(ii) yield a subset W ⊆ U satisfying (ii).

7. Extensions to regular graphs

Fix a connected and ∆-regular graph H. In this section, we apply Theorem 3.1 to study the upper tail of the random variable X = Xn,pH . In this setting, (11) may be rewritten as

ΦX(δ) = min eG log(1/p) : G ⊆ Kn and EG[X] (1 + δ)E[X] ,

where we use the notation EG[X] = E[X | G ⊆ Gn,p]. Our main result in this section is the following:

Proposition 7.1. For every ∆ 2, every connected, nonbipartite, ∆-regular graph H, and all positive real numbers ε and δ, there exists a positive constant C such that the following holds. Suppose that an integer n and p ∈ (0,1) satisfy Cn−1(log n)∆v

2

H p∆/2 1/C. Then X = Xn,pH satisﬁes

(1 − ε)ΦX(δ − ε) −log P X (1 + δ)E[X] (1 + ε)ΦX(δ + ε).

Additionally, there is a positive constant ξ = ξ(∆,ε) such that the assumption that H is nonbipartite is not necessary when p∆/2 n−1/2−ξ.

Remark 7.2. As was mentioned in the introduction, the lower bound on the density p is suboptimal by a polylogarthmic factor. We require this slightly stronger bound on the density to prove an analogue of Claim 6.7 for ∆-regular graphs H. In this more general setup, the lower bound on the number of common neighbours of the endpoints of core edges may not hold, and will be replaced by a lower bound on the product of degrees of the endpoints of core edges. We will prove this bound via an application of Lemma 5.7; unfortunately, this will incur a polylogarthmic loss, and thus necessitates the suboptimal bound on the density p.

The optimisation problem ΦX(δ) is a discretisation of the variational problem considered by Bhattacharya, Ganguly, Lubetzky, and Zhao [9]. As was the case in the context of arithmetic progressions and cliques, their variational problem was more general (being optimised over a larger set), but is asymptotically equivalent to the one considered in this paper. Their results imply

δ2/v

/2 if np∆ → 0, min {δ2/v

ΦX(δ) n2p∆ log(1/p)

H

lim

=

/2,θ} if np∆ → ∞,

n→∞

H

where θ is the unique positive solution to PH(θ) = 1 + δ and PH is the independence polynomial of H. Thus, Proposition 7.1 implies Theorem 1.5. The proof of Proposition 7.1 does not require these precise estimates, but only that ΦX(δ) is of order n2p∆ log(1/p), see Lemma 7.3 below. We include a short proof of this weaker statement for the sake of completeness, and to emphasize it may be proved combinatorially; the original proof given in [9] is conceptually equivalent but more analytically-ﬂavoured.

Lemma 7.3. For every ∆ 2, every connected, ∆-regular graph H, and every positive real number δ, there exists a positive constant C such that the following holds. Assume n ∈ N and p ∈ (0,1) are such that Cn−1 p∆/2 1/C. Then X = Xn,pH satisﬁes

ΦX(δ) n2p∆ log(1/p)

1/C

C.

Proof. The upper bound follows by noting that, if C is large enough, then a clique with (1 + 2δ)1/vH

np∆/2 vertices contains at least (1 + δ)E[X] copies of H and has fewer than Cn2p∆ edges. For the lower bound, suppose that G is a graph with EG[X] (1 + δ)E[X] with fewer than C−1n2p∆ edges. Then

nv

pe

δ 2 ·

H

H

δ E[X] EG[X] − E[X]

N(J,G) · nv

H−eJ,

H−vJpe

|Aut(H)|

∅ =J⊆H

where the sum ranges over all nonempty subgraphs J of H without isolated vertices. This implies that there is a nonempty subgraph J ⊆ H without isolated vertices and a positive constant γ = γ(H,δ) such that

. (46) Theorem 5.4 implies that

|Emb(J,G)| γ · nv

pe

J

J

|Emb(J,G)| (2eG)vJ−α∗J · min {2eG,n}2α

∗ J−vJ

and Lemma 5.2 yields αJ∗ vJ −eJ/∆. Therefore, if 2eG n, then |Emb(J,G)| is bounded from above by

eJ/∆

J−2eJ/∆ 2n2p∆ C

nv

pe

J

J

J−2eJ/∆ =

J−vJ+2eJ/∆ · nv

(2eG)α

J (2eG)α

∗

∗

nv

(C/2)eJ/∆ ,

where the ﬁrst inequality holds since 2eJ/∆ vJ, as the maximum degree of J is at most ∆. If n < 2eG, then |Emb(J,G)| is bounded from above by

vJ−α∗J

2n2p∆ C

pe

J−α∗J)−eJ nv

pe

nv

J

J

J

J

(C/2)vJ−α∗J · p∆(v

· n2α

J−vJ =

∗

(C/2)vJ−α∗J . In both cases, the obtained upper bound on |Emb(J,G)| contradicts (46) whenever C is large; indeed eJ/∆ and vJ − αJ∗ are both positive, as J is nonempty.

7.1. Proof of Proposition 7.1. Fix ∆ 2, a nonempty, connected, ∆-regular graph H, and positive reals ε and δ. Without loss of generality, we may assume that ε min {1/3,δ/2}. Let X = Xn,pH and assume Cn−1(log n)∆v

2

H p∆/2 1/C. Note that the case n < vH is trivial as then X is identically zero. We may therefore assume that n vH ∆ + 1 3, which, in turn, implies that n C.

Set N = n2 and let Y = (Y1,...,YN) be the sequence of indicator random variables of

the events that e ∈ E(Gn,p), where e ranges over n 2 in some arbitrary order. Then Y is a vector of independent Ber(p) random variables and X is a nonzero polynomial with nonnegative

coeﬃcients and degree at most eH in the coordinates of Y . Let K = K(eH,ε,δ) be the constant whose existence is asserted by Theorem 3.1. To prove the proposition, it suﬃces to verify the assumptions of the theorem.

It follows from Lemma 7.3 and our assumptions on p that p 1−ε and ΦX(δ−ε) K log(1/p) for a large enough choice of C. It thus only remains to bound the number of cores of a given size. To this end, let Im∗ be the set of cores with m edges, that is, subgraphs G∗ ⊆ Kn such that

(C1) EG∗[X] (1 + δ − ε)E[X], (C2) eG∗ = m K · ΦX(δ + ε), and (C3) mine∈E(G∗) EG∗[X] − EG∗\e[X] E[X]/(K · ΦX(δ + ε)).

Proposition 7.1 will follow once we prove |Im∗ | (1/p)εm/2 for all m. (47)

Observe that due to (C1), (C2), and the deﬁnition of ΦX, it suﬃces to verify (47) for integers m such that mmin m mmax with

mmin := ΦX(δ − ε)/log(1/p) n2p∆/K and mmax := K · ΦX(δ + ε) K · n2p∆ log(1/p),

where the stated inequalities follow, for a suitable constant K = K (H,ε,δ), from Lemma 7.3, our bounds on p, and the assumption that C is suﬃciently large.

The ﬁrst step towards establishing (47) is to understand the combinatorial meaning of (C3).

Suppose that mmin m mmax and G∗ ∈ Im∗ . Recall that N(J,G∗;e) denotes the number of copies of J in G∗ that contain the edge e. Note that (C3) implies that, for every e ∈ E(G∗),

E[X] mmax

H−eJ, (48)

EG∗[X] − EG∗\e[X]

N(J,G∗;e) · nv

H−vJpe

∅ =J⊆H

where the sum ranges over the nonempty subgraphs J of H without isolated vertices. Since n C for a large enough constant C, we can bound E[X] v n

2vH! and, consequently, (48) implies that there is a positive constant γ = γ(H) such that

H nvH peH

pe

H

N(J,G∗;e) nvJpeJ

2γ mmax

for every e ∈ E(G∗). (49)

∅ =J⊆H

Deﬁnition 7.4. Let QH denote the family of all nonempty subgraphs J ⊆ H without isolated vertices satisfying

- (Q1) J = H or
- (Q2) J admits a bipartition V (J) = A ∪ B such that degJ a = ∆ for all a ∈ A. Our ﬁrst claim is that, for the vast majority of e ∈ E(G∗), the sum on the left-hand side of (49)


is dominated by subgraphs J ∈ QH. Let G∗exc comprise all edges e of G∗ such that

N(J,G∗;e) nvJpeJ

γ mmax

<

.

J∈QH

- Claim 7.5. There is a positive constant σ = σ(H) such that eG∗exc


pσ · mmin. Proof. Let mexc denote the number of edges of G∗exc. The deﬁnition of G∗exc and (49) imply that

N(J,G∗;e) nvJpeJ

γ · mexc mmax

γ · mexc mmin · (K )2 · log(1/p)

.

e∈E(G∗exc) ∅ =J⊆H J∈Q/ H

On the other hand, since e∈E(G∗) N(J,G∗;e) eJ ·|Emb(J,G∗)| for every graph J, there must exist a nonempty subgraph J ⊆ H without isolated vertices such that J ∈/ QH and

eJ · (K )2 · log(1/p) · 2eH+vH γ ·

|Emb(J,G∗)| nvJpeJ

mexc mmin

. (50)

We now show that the right-hand side of (50) is at most pσ, for some positive constant σ = σ(H). To this end, recall that Theorem 5.4 states that

|Emb(J,G∗)| (2m)vJ−α∗J · min {2m,n}2α

∗

J−vJ. (51)

Since J is a proper subgraph of a connected, ∆-regular graph, it must contain a vertex of degree smaller than ∆ and hence vJ > 2eJ/∆. Moreover, since J ∈/ QH, Lemma 5.2 implies that

αJ∗ < vJ −eJ/∆. Therefore, if 2m n, then there is a positive σ = σ(H) such that the right-hand side of (51) can be bounded from above as follows:

J−2eJ/∆−2σ (2m)eJ/∆ · nv

J−vJ+2eJ/∆+2σ · nv

(2m)α

J (2m)α

∗

∗

J−2eJ/∆−2σ

2K · n2p∆ log(1/p) eJ/∆ nv

J−2eJ/∆−2σ

= n−2σ · 2K · log(1/p) eJ/∆ · nv

pe

.

J

J

Similarly, if n < 2m, there is a positive σ = σ(H) such that the right-hand side of (51) is bounded from above by

∗

(2m)vJ−α∗J · n2α

J−vJ 2K · n2p∆ log(1/p) vJ−α

J · n2α

∗

∗ J−vJ

∗

= p∆(v

J−α∗J)−eJ · 2K · log(1/p) vJ−α

pe

J · nv

J

J

∗

p2σ · 2K · log(1/p) vJ−α

pe

J · nv

. Since p C−2/∆ and Cn−1 p, it follows that, in both cases,

J

J

γ eJ · (K )2 · log(1/p) · 2eH+vH , provided that C is suﬃciently large. Substituting this inequality into (50) proves the claim.

|Emb(J,G∗)| pσ · nv

pe

·

J

J

The next claim shows that the endpoints of every edge of G∗ \ G∗exc satisfy a certain degree restriction.

- Claim 7.6. There is a positive γ = γ (H,K ) such that, for every edge uv of G∗ \ G∗exc, either


γ log(1/p) vH · m or degG∗ u + degG∗ v

γ log(1/p) vH/2

degG∗ u · degG∗ v

· n.

Moreover, if the second inequality fails, then uv is contained in at least γ nv

/mmax copies of

pe

H

H

H in G∗. Proof. Suppose that uv is an edge of G∗ \ G∗exc. It follows from (49) and the deﬁnition of G∗exc that there is some J ∈ QH such that

nv

pe

γ |QH|

J

J

|Emb(J,G;uv)| N(J,G;uv)

. (52)

·

mmax

Let µ = n2p∆/m and observe that µ K · log(1/p) −1 · mmax/m. We split the remainder of the proof into two cases, depending on whether or not J = H.

H = n2p∆ vH/2 = (µm)vH/2, Lemma 5.7 and (52) imply that

Assume ﬁrst J = H. Then, since nv

pe

H

2∆−1

∆ − v2H 4eH

(2m)

∆−1 ∆

4degG∗ u · degG∗ v

|Emb(J,G;uv)| ·

2∆−1

(µm)vH/2 mmax ·

∆ − v2H 4eH

(2m)

γ |QH|

·

2∆−1

∆ −v2H γ 4eH|QH|

2

m mmax · m

∆−1 ∆

H/2 ·

=

· µv

· log(1/p) −vH/2 · m

∆−1 ∆

∆−1 ∆

(4γ )

, for a suitable positive constant γ = γ (H,K ). Since ∆ 2, this implies the claimed lower bound on degG∗ u · degG∗ v.

Assume now that J = H. In this case, J admits a bipartition V (J) = A ∪ B such that every vertex in A has degree ∆. In particular, eJ = |A| · ∆; moreover, as J = H and H is connected

J = n2p∆ |A| · n|B|−|A| = (µm)|A| · n|B|−|A|, it follows from Lemma 5.8 and (52) that

and ∆-regular, we also have |B| > |A|. Since nv

pe

J

degG∗ u + degG∗ v |Emb(J,G;uv)| eJ · (2m)|A|−1 · min{m,n} |B|−|A|−1

1 eJ · (2m)|A|−1 · min{m,n} |B|−|A|−1 γ |QH|

(µm)|A| · n|B|−|A| mmax ·

γ |QH|

·

µ|A|m mmax ·

n eJ · 2|A|−1 γ · log(1/p) −|A| · n

·

for a suitable positive constant γ . Since |A| < vH/2, this implies the claimed lower bound on degG∗ u + degG∗ v. In particular, if the second inequality in the statement of the claim fails, then the above shows that J = H, and thus the second assertion of the claim follows from (52).

To prove (47), we will further distinguish between the cases p∆/2 n−1/2−ξ and p∆/2 n−1/2−ξ, for a small constant ξ. The ﬁrst case is easier and is handled by our next claim.

- Claim 7.7. There is a positive constant ξ = ξ(∆,ε) such that (47) holds if p∆/2 n−1/2−ξ.


Proof. To simplify the presentation, we shall prove (47) with 7ε instead of ε/2. Suppose that G∗ is a core with m edges, where mmin m mmax. For each k ∈ Z, we deﬁne the set

Bk = v ∈ V (G∗) : degG∗ v ek√mpε and let kmax be the largest integer such that ek

√m np2ε. Note that the bounds n2p∆/K

max

- m K · n2p∆ log(1/p) and our assumption p C−2/∆ imply that 0 kmax (∆/2) · log(1/p) whenever C is large enough.


We will ﬁrst prove that Claim 7.6 implies that, for each edge uv of G∗ \ G∗exc, either

- (i) uv has an endpoint in Bk

max

or

- (ii) u ∈ Bk and v ∈ B−k for some k ∈ {−kmax,...,kmax}.


Indeed, if we suppose that

γ · n (log(1/p))vH/2 ,

degG∗ u + degG∗ v

√mpε. On the other hand, if (i) does not hold (i.e., neither u nor v is in Bk

(log(1/p))vH/2 np3ε 2ek

then (i) follows immediately (with room to spare) because γ ·n

max

), then the above lower bound on degG∗ u + degG∗ v does not hold, and Claim 7.6 guarantees

max

γ · m (log(1/p))vH

emp2ε. Observe that the lower bound above and the assumption on u and v imply that min{degG∗ u,degG∗ v} =

degG∗ u · degG∗ v

emp2ε ek

degG∗ u · degG∗ v max{degG∗ u,degG∗ v}

max+1√mpε.

= e−k

√mpε

>

max

Let k ∈ {−kmax + 1,...,kmax − 1} be the largest index such that {u,v} ⊆ Bk. Without loss of generality, u  ∈ Bk+1, so

emp2ε degG∗ u · degG∗ v < ek+1√mpε · degG∗ v, which implies (ii).

To make use of this property of the edges of G∗ \ G∗exc, we also require upper bounds on the cardinalities of the sets Bk. To that end, observe that, for all k ∈ Z,

degG∗ v |Bk| · ek√mpε

2m

v∈Bk

and hence

|Bk| 2e−k√mp−ε. (53) We claim that there is a positive constant ξ = ξ(∆,ε) such that n2p∆ 2K npε log n whenever p∆/2 n−1/2−ξ and C is suﬃciently large. Indeed, if p∆/2 n−1/3, then n2p∆ n4/3

2K npε log n, provided that C is suﬃciently large; otherwise, pε n−2ε/(3∆) and our assumption implies that n2p∆ n1−2ξ K npε log n, provided that ξ is suﬃciently small and C is suﬃciently large. Now inequality (53) and the choice of kmax imply

√mp−ε 2npε

m log n

max| 2ek

(54)

max

|B−k

max+1 > np2ε)

and (since ek

√mp−ε · n < 2emp−3ε. (55) Recall from Claim 7.5 that eG∗exc

max| · n 2e−k

max

|Bk

pσ · mmin for a positive constant σ depending only on H. It follows that we may construct each G∗ ∈ Im∗ as follows:

- (1) Choose some mexc pσ · mmin and then choose mexc edges of Kn to form G∗exc.
- (2) Choose the sets B−k


and then choose m − mexc edges from

,...,Bk

max

max

kmax

B = uv ∈ E(Kn) : u ∈ Bk

uv ∈ E(Kn) : u ∈ Bk,v ∈ B−k

max ∪

k=0

to form G∗ \ G∗exc. Since Bk

max| m/log n by (54), the number of ways to choose the sets B−k

and |B−k

max ⊆ ··· ⊆ B−k

max

is at most (2kmax + 2) · n m/logn e2m, using the (very crude) bound kmax n/4. Moreover, inequalities (53) and (55) imply that |B| |Bk

,...,Bk

max

max

kmax

|Bk| · |B−k| 2emp−3ε + (kmax + 1) · 4mp−2ε mp−4ε,

max| · n +

k=0

where we use kmax (∆/2) · log(1/p) and p∆/2 1/C for a large enough C. We conclude that

pσ·mmin

n2 mexc ·

mp−4ε m − mexc

|Im∗ | e2m ·

.

mexc=0

In order to bound the right-hand side above, we note that

mp−4ε m − mexc

mp−4ε m

emp−4ε m

m

p−5εm.

Moreover, using the inequalities ki=0 ni (en/k)k and m mmin n2p∆/K ,

pσ·mmin

pσ·mmin eK p∆+σ

en2 pσ · mmin

n2 mexc

mexc=0

We may conclude that

|Im∗ | e2m · p−6εm p−7εm, which completes the proof of (47) (with 7ε instead of ε/2).

mpσ

p−εm.

The argument above shows that we do not need the assumption that H is nonbipartite when p∆/2 n−1/2−ξ. In the following, we will assume that p∆/2 n−1/2−ξ and that H is not bipartite.

Let γ be the constant from Claim 7.6. Our assumption on p implies that

γ · n log(1/p) vH/2

mmax K · n2p∆ log(1/p) K · n1−2ξ log(1/p) <

− 1,

where the last inequality holds because n C and C is large. In particular, if G∗ ∈ Im∗ for some mmin m mmax, then for any two vertices u,v ∈ V (G∗), we have degG∗(u) + degG∗(v) mmax + 1 < γ n/(log(1/p))vH/2, so it follows from Claim 7.6 that

γ

log(1/p) vH · m for every uv ∈ E(G∗ \ G∗exc) (56) and that every edge uv of G∗ \ G∗exc belongs to at least γ nv

degG∗ u · degG∗ v

/mmax copies of H in G∗. Set β = ∆(1 + vH/2) + 1/2,

pe

H

H

let G∗high comprise all edges uv of G∗ such that

degG∗ u · degG∗ v log(1/p) β · m, (57) and denote by mhigh the number of edges in G∗high. We claim that

8m log(1/p) β

. (58)

mhigh

In order to show it, we estimate the number of copies of P4, the path with four vertices (and three edges), in G∗ in two diﬀerent ways. On the one hand,

2N(P4,G∗) = |Emb(P4,G∗)| (2m)2,

since every embedding of P4 into G∗ is determined by the images of its two nonincident edges. On the other hand,

N(P4,G∗)

(degG∗ u − 1) · (degG∗ v − 2)

uv∈E(G∗)

(degG∗ v)2 + 2m

=

degG∗ u · degG∗ v − 3

uv∈E(G∗)

v∈V (G∗)

mhigh · log(1/p) β · m − 3m

degG∗ v

v∈V (G∗)

= mhigh · log(1/p) β · m − 6m2. These two lower and upper bounds on N(P4,G∗) imply (58).

- Claim 7.8. Suppose that ϕ is an embedding of H into G∗ \ (G∗exc ∪ G∗high). Then for every a ∈ V (H),


m1/2 log(1/p) β·vH

degG∗ ϕ(a)

.

Proof. Deﬁne f : V (H) → R by

degG∗ ϕ(a) m1/2 and let

f(a) = log

f∗ = β log log(1/p). It suﬃces to show that f(a) −vHf∗ for every a ∈ V (H). To this end, note that (56) and our deﬁnition of G∗high (see (57)) imply that

− f∗ f(a) + f(b) f∗ for every ab ∈ E(H), (59)

since β vH + 1 and p C−2/∆ for a large constant C. Since H is not bipartite, it contains an odd cycle. Let Z be one such cycle and suppose that a0,...,a2 are its vertices (listed in an arbitrarily chosen cyclic ordering). It follows from (59), applied to all 2 + 1 edges of Z, that

2 −1

2f(a0) = f(a0) + f(a2 ) +

(−1)i f(ai) + f(ai+1) ∈ − (2 + 1)f∗,(2 + 1)f∗ .

i=0

Since the particular choice of a0 among all vertices of Z was arbitrary, we may conclude that −(2 + 1)f∗ f(a) (2 + 1)f∗ for every a ∈ V (Z),

with room to spare. Since 2 + 1 = vZ vH, this proves the desired inequality for all a ∈ V (Z). Suppose now that b ∈ V (H) \ V (Z). Since H is connected, it contains a path from b to Z. Let b0,b1,...,b , where b0 = b and b ∈ V (Z), be the vertices of a shortest such path (listed in their natural order) and note that + 2 + 1 vH. It follows from (59), applied to all edges of the path, that

−1

f(b) + (−1) −1f(b ) =

(−1)i f(bi) + f(bi+1) ∈ − f∗,  f∗

i=0

and consequently, as b ∈ V (Z), that

f(b) − f∗ − |f(b )| −( + 2 + 1)f∗ −vHf∗, as claimed.

Let G∗bad comprise all edges of G∗ that do not belong to a copy of H in the graph G∗ \ (G∗exc ∪ G∗high) and let mbad be the number of such edges; note that G∗bad ⊇ G∗exc ∪ G∗high. Since each edge of G∗bad \ G∗exc belongs to at least γ nv

/mmax copies of H in G∗, none of which are in G∗ \ G∗exc ∪ G∗high, we have

pe

H

H

γ nv

pe

H

H

(mbad − mexc) ·

|Emb(H,G∗;e)|.

mmax

e∈E(G∗exc∪G∗high)

It follows from Lemma 5.9, Claim 7.5, and inequality (58) that

1/∆

(2m)vH/2 log(1/p) β/∆

mexc + mhigh m

|Emb(H,G∗;e)| eH · (2m)vH/2 ·

8eH ·

.

e∈E(G∗exc∪G∗high)

Consequently,

(2m)vH/2 log(1/p) β/∆

mmax γ nvHpeH

· 8eH ·

mbad mexc +

mvmaxH/2 nvHpeH log(1/p) β/∆

8 · 2vH/2 · eH γ ·

pσ · mmin +

· m

K · n2p∆ log(1/p) vH/2 nvHpeH log(1/p) β/∆

8 · 2vH/2 · eH γ ·

pσ +

· m

8 · eH · 2K vH/2 γ · log(1/p) β/∆−vH/2

m log(1/p)

= pσ +

· m

,

since β/∆ = 1 + vH/2 + 1/(2∆) and p C−2/∆ for a large constant C. Let U be the set of nonisolated vertices of G∗ \ G∗bad. It follows from Claim 7.8 that

m1/2 log(1/p) β·vH v∈U

degG∗ v 2m

|U| ·

and thus

|U| 2m1/2 · log(1/p) β·vH m/log n, as p∆/2 Cn−1(log n)∆v

2 H

and C is large enough. To summarise, we may construct each G∗ ∈ Im∗ as follows:

- (1) Choose mbad m/log(1/p) and the mbad edges of Kn to form G∗bad.
- (2) Choose the vertices of U and the edges of G∗ \ G∗bad from the set U2 .


Using the above bounds on the size of U, we conclude that

m/ log(1/p)

4m · log(1/p) 2β·vH m − mbad

n2 mbad · nm/logn ·

|Im∗ |

.

mbad=0

In order to bound the right-hand side from above, we note that, for suﬃciently large C,

4em · log(1/p) 2β·vH m

m

4m · log(1/p) 2β·vH m − mbad

4m · log(1/p) 2β·vH m

p−εm/6

and, since m n2p∆/K ,

m/ log(1/p)

m/log(1/p) eK · log(1/p) p∆

m/ log(1/p)

n2 mbad

en2 log(1/p) m

p−εm/6.

mbad=0

Since nm/logn = em p−εm/6, we may conclude that |Im∗ | p−εm/2, which completes the proof of Proposition 7.1.

8. The Poisson regime

Given a nonnegative real µ, we shall denote by Po(µ) the Poisson distribution with mean µ. Suppose that X ∼ Po(µ). A classical result in large deviation theory is that, for every ﬁxed δ > 0,

−log P X (1 + δ)µ = (1 + δ)log(1 + δ) − δ µ + o(µ),

as µ → ∞. Motivated by this estimate, for any random variable X with positive expectation and any δ > 0, we deﬁne

ΨX(δ) = (1 + δ)log(1 + δ) − δ E[X]. Theorems 1.4 and 1.6 follow immediately from the following two propositions.

- Proposition 8.1. For every integer k 3 and all positive real numbers ε and δ, there exists a positive constant C such that the following holds. Suppose that N ∈ N and p ∈ (0,1) satisfy CN−1 pk/2 C−1N−1 log N. Then X = XN,pk-AP satisﬁes

(1 − ε)ΨX(δ) −log P X (1 + δ)E[X] (1 + ε)ΨX(δ).

- Proposition 8.2. For every ∆ 2, every connected, ∆-regular graph H, and all positive real numbers ε and δ, there exists a positive constant C such that the following holds. Suppose that


1

- n ∈ N and p ∈ (0,1) satisfy Cn−1 p∆/2 C−1n−1(log n)


vH−2 . Then X = Xn,pH satisﬁes (1 − ε)ΨX(δ) −log P X (1 + δ)E[X] (1 + ε)ΨX(δ).

It is not diﬃcult to show that the requirements on p in these results are optimal up to the

choice of the constant C. Indeed, if X = XN,pk-AP, then planting an interval of length CδNpk/2 creates (1 + δ)E[X] k-term arithmetic progressions (for a suﬃciently large Cδ), which shows that

−log P X (1 + δ)E[X] = O Npk/2 log(1/p) .

Similarly, if X = Xn,pH , then planting a clique of size Cδnp∆/2 results in (1 + δ)E[X] copies of H, which proves

−log P X (1 + δ)E[X] = O n2p∆ log(1/p) .

The upper bounds are o(ΨX(δ)), and therefore dominate the Poisson bounds, whenever pk/2 N−1 log N or p∆/2 n−1(log n)

1

vH−2 , respectively.

- 8.1. Poisson approximation via factorial moments. For a real number m and a nonnegative integer t, write mt = m(m − 1)···(m − t + 1) for the t-th falling factorial of m. For a random variable X, let Mt(X) = E[Xt] be the t-th factorial moment of X. It is straightforward to verify that, if X ∼ Po(µ), then Mt(X) = µt for all t 0.


A classical application of the method of moments is that, if (Xn) is a sequence of random variables whose t-th factorial moments converge to µt for some ﬁxed µ, then Xn converges in distribution to Po(µ). The lemma below can be viewed as an extension of this result to the case when µ → ∞. It states that, if the t-th factorial moment of some random variable X is approximately µt, for each t around δµ, then the logarithmic upper tail probability −log P X

(1 + δ)E[X] is well approximated by ΨX(δ).

- Proposition 8.3. For all positive real numbers ε and δ, there exists a positive constant η such that the following holds. Let X be a nonnegative integer-valued random variable with mean µ 1/η such that |Mt(X)−µt| ηµt for every integer t satisfying (δ −ε)µ t (δ +ε)µ. Then


(1 − ε)ΨX(δ) −log P X (1 + δ)E[X] (1 + ε)ΨX(δ). Deﬁne the continuous function I : [0,∞) → [0,∞) by

I(δ) = (1 + δ)log(1 + δ) − δ, so that ΨX(δ) = I(δ) · µ. Note that I(δ) > 0 whenever δ > 0.

- Lemma 8.4. For every nonnegative integer t and every positive real x, log (x + t)t = I(t/x) · x + tlog x + λ(x,t),


where 0 λ(x,t) (t + 1)/x. Proof. Observe that log (x + t)t = ts=1 log(x + s). Since log is an increasing function,

x+t

x+t+1

t

log(x + s)

log y dy

log y dy.

x+1

s=1

x

Recalling that log y dy = y(log y − 1) + C, we have

x+t

log y dy = (1 + t/x)log(1 + t/x) − t/x · x + tlog x = I(t/x) · x + tlog x. On the other hand,

x

x+t+1

x+t

log y dy log(x + t + 1) − log x = log 1 + (t + 1)/x (t + 1)/x. This proves the claimed estimate. Proof of Proposition 8.3. Since, for every positive integer t, the function x  → xt is increasing on [t − 1,∞) and nonnegative on Z 0, Markov’s inequality implies that

log y dy −

x+1

x

Mt(X)

P X (1 + δ)E[X] P Xt (1 + δ)E[X] t

(1 + δ)E[X] t for every positive integer t (1 + δ)E[X]. This implies that, for every such t,

− log P X (1 + δ)E[X] log (1 + δ)µ t − log Mt(X). (60) Let t = δµ . Since (1 + δ)µ − t µ, it follows from Lemma 8.4 that

log (1 + δ)µ t log (µ + t)t I(t/µ) · µ + tlog µ.

On the other hand, our assumption implies that log Mt(X) log (1 + η)µt = tlog µ + log(1 + η) tlog µ + η.

Finally, since I is continuous, I(δ) > 0, and |t/µ − δ| 1/µ η, substituting the above two inequalities into (60) yields

−log P X (1 + δ)E[X] I(δ) · µ − εΨX(δ) = (1 − ε)ΨX(δ), provided that η is suﬃciently small (as a function of ε and δ).

For the upper bound, we will use the tilting argument, which is a standard trick of large deviation theory. For the sake of brevity, let mt = Mt(X) for every nonnegative integer t. Let t = (δ + γ)µ, where γ is a small positive constant that depends on ε and δ (but not on η). Since η is allowed to depend on γ and µ 1/η, we may assume that t is an integer. The idea is to consider a ‘tilted’ random variable X˜ deﬁned by the relation

P(X = x) · xt mt

P(X˜ = x) =

for every x ∈ Z.

The deﬁnition of mt ensures that X˜ is a well-normalised random variable. In particular,

E[g(X) · Xt] mt

E[g(X˜)] =

for every g: Z → Z. (61) Using the identities

x · xt = xt+1 + t · xt and x2 · xt = xt+2 + (2t + 1) · xt+1 + t2 · xt, we have

E[X · Xt] mt

mt+1 mt

E[X˜] =

+ t and

=

E[X2 · Xt] mt

mt+2 + (2t + 1)mt+1 mt

E[X˜2] =

+ t2, and so

=

mt+2mt − m2t+1 + mt+1mt m2t

Var[X˜] = E[X˜2] − E[X˜]2 =

.

Since t = (δ + γ)µ, we have (δ − ε)µ t t + 2 (δ + ε)µ, provided that γ is suﬃciently small as a function of δ and ε. Since the assumptions of the proposition imply that ms is well approximated by µs for each s ∈ {t,t + 1,t + 2}, a straightforward computation yields

(1 + δ + γ/2)µ E[X˜] (1 + δ + 3γ/2)µ and Var[X˜] 10ηµ2 + 2µ, provided that η is suﬃciently small. Therefore, Chebyshev’s inequality yields

4 · (10ηµ2 + 2µ) γ2µ2

P |X˜ − (1 + δ + γ)µ| γµ P |X˜ − E[X˜]| γµ/2

ε. (62)

Next, using (61) with the function g(x) = |x − (1 + δ + γ)µ| < γµ · (mt/xt), we see that

P X (1 + δ)µ P |X − (1 + δ + γ)µ| γµ = E g(X˜) .

When g(X˜) is nonzero, then X˜ is bounded from above by (1 + δ + 2γ)µ, and thus

mt (1 + δ + 2γ)t

E g(X˜) P g(X˜) = 0 ·

(62) (1 − ε) · mt (1 + δ + 2γ)t

mt (1 + δ + 2γ)t

= 1 − P(|X˜ − (1 + δ + γ)µ| γµ) ·

.

Using Lemma 8.4 with x = (1 + γ)µ, we obtain log (1 + δ + 2γ)t I t/(1 + γ)µ · (1 + γ)µ + tlog (1 + γ)µ +

t + 1 (1 + γ)µ

.

On the other hand, our assumptions imply that, when η is small,

log mt tlog µ + log(1 − η) tlog µ − 2η. Combining the above bounds, we obtain

t + 1 (1 + γ)µ

+ 2η − log(1 − ε). Recalling that t = (δ + γ)µ, the continuity of I and the fact that I(δ) > 0 imply that

−log P X (1 + δ)µ I t/(1 + γ)µ · (1 + γ)µ + tlog(1 + γ) +

−log P X (1 + δ)µ I(δ) · µ + εΨX(δ) = (1 + ε)ΨX(δ), provided that γ is suﬃciently small and η is suﬃciently small.

- 8.2. Cluster analysis. We will deduce both Propositions 8.1 and 8.2 from Proposition 8.3 and Lemma 8.5, stated below, by analysing the component structure of certain random hypergraphs. Since the proofs turn out to be quite similar, we adopt a general point of view from the start.


Suppose that H is a hypergraph and, given some p ∈ (0,1), denote by Hp the random induced subhypergraph of H obtained by keeping every vertex with probability p, independently. The dependency graph GH is the graph on the vertex set E(H) whose edges are all pairs {σ1,σ2} such that σ1 ∩ σ2 = ∅. A cluster is a set E ⊆ E(H) that induces a connected subgraph in GH. We write Ds(Hp) for the number of clusters of size s whose elements are edges in Hp.

- Lemma 8.5. For all positive real numbers c and η, there exists a positive constant K such that


the following holds. Let H be a uniform hypergraph, let p ∈ (0,1), and deﬁne X = eH

and µ = E[X]. Assume that K µ √eH/K and that E[Ds(Hp)] exp(−Ks) for every integer s such that 2 s cµ. Then |Mt(X) − µt| ηµt for every integer t such that 1 t cµ.

p

Proof. Let t cµ be a positive integer and let H(t) denote the set of all sequences of t distinct edges of H. For each sequence σ¯ = (σ1,...,σt) ∈ H(t), let Xσ¯ be the indicator random variable for the event σ1 ∪ ··· ∪ σt ⊆ V (Hp). Denote the uniformity of H by k. Our deﬁnitions readily imply that Xt = σ ¯∈H(t) Xσ¯, that |H(t)| = eHt, and that E[Xσ¯] pkt for all σ¯ ∈ H(t). Thus

Mt(X) = E[Xt] =

E[Xσ¯] eHt · pkt.

σ ¯∈H(t)

Since, for every x t,

t−1

t−1

t2 x

s x

s x

xt = xt

1 −

xt 1 −

xt 1 −

,

s=0

s=0

and t cµ c√eH/K eH for suﬃciently large K, we have Mt(X) 1 −

t2 eH · eHtpkt = 1 −

t2 eH · µt 1 −

c2

K2 · µt (1 − η) · µt, provided that K is suﬃciently large.

It remains to prove the upper bound. It will be convenient to partition the set H(t) of sequences according to the component structure of the subgraph of GH induced by the elements of the sequence. More precisely, given a nonnegative integer and integers s1,...,s such that 2 s1 ··· s , let H(t;s1,...,s ) be the family of all σ¯ = (σ1,...,σt) ∈ H(t) such that the set {σ1,...,σt} induces a subgraph in GH whose nontrivial connected components (maximal clusters) have sizes s1,...,s , so that this graph has t − (s1 + ··· + s ) isolated vertices.7 Observe that, for every collection W1,...,W of connected subsets of vertices GH with sizes s1,...,s , respectively, there are at most ts

1+···+s ) sequences σ¯ = (σ1,...,σt) ∈ H(t) such that the nontrivial connected components of {σ1,...,σt} are exactly W1,...,W ; indeed, there

1+···+s · eHt−(s

7This includes the case = 0 in which H(t; ∅) corresponds to induced subgraphs of GH all of whose connected components are isolated vertices.

1+···+s ways to choose the locations of the vertices in W1 ∪ ··· ∪ W in a sequence of length t and, for each such choice, at most eHt−(s

are at most ts

1+···+s ) choices for the remaining elements of the sequence. We conclude that

E[Xσ¯] µt−(s

1+···+s ) ·

(Hp) · ts

E Ds

i

i

i=1

σ ¯∈H(t;s1,...,s )

and, consequently, summing over all and all sequences s1,...,s and using the assumed upper bound on the expectation of Ds(Hp), valid for each s t,

t

Mt(X)

- s=0

µt−s ·

0 s1+···+s =s 2 s1 ··· s

i=1

E Ds

i

(Hp) · ts

i

- t


exp(−Ksi + si log t)

µt−s ·

0 s1+···+s =s 2 s1 ··· s

s=0

i=1

t

=

exp − Ks + slog(t/µ) .

µt ·

0 s1+···+s =s 2 s1 ··· s

s=0

Since, for every s 0, there are at most 2s sequences s1,...,s of positive integers whose sum is s (this includes the case when s = 0, when the only such sequence is the empty sequence), we have

t

Mt(X) µt ·

exp − Ks + slog(t/µ) + s .

s=0

Finally, since t/µ c, we may choose K = K(c,η) so that

completing the proof.

t

Mt(X) µt ·

s=0

η 1 + η

s

(1 + η)µt,

- 8.3. Proof of Proposition 8.1. Let H be the hypergraph on the vertex set N whose edges are


k-term arithmetic progressions in N , so that X = XN,pk-AP = eH

. Let µ = E[X], let η = η(ε,δ) be the constant from the statement of Proposition 8.3, and let K = K(ε,δ,η) be the constant from the statement of Lemma 8.5.

p

For any two integers a,b ∈ N with a < b, there is at most one k-term arithmetic progression that starts with a and ends with b (and exactly one such progression if b − a is divisible by k − 1). Therefore, N2/(2k) eH N2 for all large enough N. In particular, since we assume that CN−1 pk/2 C−1N−1 log N, we ﬁnd that

2

C2 2k

log N C

(63)

µ

and thus max{1/η,K} µ √eH/K whenever C is large. The claimed estimate on −log P X (1 + δ)E[X] will follow from Proposition 8.3 and Lemma 8.5 once we verify that Ds(Hp), the number of clusters of s arithmetic progressions of length k in the set N p, satisﬁes

E[Ds(Hp)] exp(−Ks) for every s satisfying 2 s (δ + ε)µ.

In order to do so, let D(s,m) be the the set of all clusters {σ1,...,σs} of s arithmetic progressions of length k in N such that |σ1 ∪ ··· ∪ σs| = m; we also let Ds,m be the number of such clusters whose union is contained in the random set N p. When s 2, the union of any s

distinct k-term arithmetic progressions contains between k + 1 and ks numbers, and therefore Ds,m = 0 unless k + 1 m ks. Thus, we can write

ks

Ds(Hp) =

Ds,m.

m=k+1

For each integer m, let am denote the number of m-element subsets of N that are the union of a single, nonempty (but possibly trivial) cluster of k-term arithmetic progressions. Since a progression is uniquely determined by its ﬁrst and second element, it follows that, for each s,

m2 s

E[Ds,m] ampm

. (64)

- Claim 8.6. For every integer m 1,


am N2 · (2kmN)

m−k k−1

.

Proof. We prove the claimed upper bound on am by induction on m. It is vacuously true when m < k, since then am = 0, or when m = k, as ak = eH N2. Assume now that m k + 1 and let A be an arbitrary set counted by am. Since m > k, the set A must be a union of at least two diﬀerent progressions. Moreover, there are a proper subset A A that is a union of a (nonempty) cluster of k-term arithmetic progressions and a k-term progression σ that intersects A such that A = A ∪ σ; note that the number of σi’s whose union is A may be signiﬁcantly smaller than the number that was used to generate A. By construction, we have that |A | = |A| − k + |A ∩ σ| = m − k + |A ∩ σ|. Since there are at most k|A |N kmN arithmetic progressions of length k that intersect A in exactly one element and at most k2|A |2 k2m2 progressions that intersect A in two or more elements,

am kmN · am−k+1 + k2m2 · (am−k+2 + ··· + am−1). It follows from our inductive assumption that

m−2k+1

m−k−1 k−1

k−1 + k2m2 · k · N2 · (2kmN)

am kmN · N2 · (2kmN)

m−k k−1 − k−1 1

= N2 · (2kmN)

/2 + k3m2 · (2kmN)

m−k k−1

. Finally, as (63) implies that m ks k(δ + ε)µ k(δ + ε)(C−1 log N)2 and N C, then k3m2 · (2kmN)−1/(k−1) 1/2, provided that C is suﬃciently large. This implies the claimed upper bound on am.

Assume now that k + 1 m ks. Since s (δ + ε)µ, inequality (63) implies that m is only polylogarithmic in N; on the other hand, p (C−1N−1 log N)2/k. Since k 3 and N C, there is a positive constant γ that depends only on k such that

(2kmN)1/(k−1)p (2kmN)1/(k−1) · (C−1N−1 log N)2/k N−2(k+1)γ N−2mγ/(m−k). In particular, Claim 8.6 implies that

m−k

ampm N2pk · (2kmN)1/(k−1)p

N2pk · N−2mγ N−mγ,

where for the last inequality we use that N2pk is at most polylogarithmic in N and N C. Combining this bound with (64) we conclude that

em2 s

m2 s

exp −mγ log N + slog

E[Ds,m] N−mγ ·

. Let f : (0,∞) → (0,∞) be the function deﬁned by

ex2 s

f(x) = exp −xγ log N + slog

= exp − xγ log N + 2slog x + slog(e/s) ,

so that E[Ds,m] f(m). Elementary calculus shows that f is maximised at x = 2s/(γ log N). Therefore,

2s γ log N

4es γ2(log N)2

E[Ds,m] f

= exp −2s + slog

. Since our assumptions imply that, see (63),

(δ + ε)µ (log N)2

δ + ε C2

s (log N)2

,

we may conclude that E[Ds,m] exp(−(K +k)s), provided that C is suﬃciently large. Therefore, if C is suﬃciently large,

E[Ds(Hp)] =

This completes the proof.

ks

E[Ds,m] ks · exp(−Ks − ks) exp(−Ks).

m=k+1

- 8.4. Proof of Proposition 8.2. Let H be a connected, ∆-regular graph and let H be the


hypergraph on the vertex set n 2 whose edges are copies of H in Kn, so that X = Xn,pH = eH

.

p

Let µ = E[X], let η = η(ε,δ) be the constant from the statement of Proposition 8.3, and let K = K(ε,δ,η) be the constant from the statement of Lemma 8.5.

H for all large enough n, our assumption Cn−1 p∆/2 C−1n−1(log n)

Since (n/vH)vH n

vH eH nv

1

vH−2 and the fact that 2eH = ∆vH imply that

2 vH −2

(log n)1+

vH

C vH

, (65)

µ

CvH

and thus max{1/η,K} µ √eH/K whenever C is suﬃciently large. The claimed estimate on −log P X (1 + δ)E[X] will follow from Proposition 8.3 and Lemma 8.5 once we verify that Ds(Hp), the number of clusters of s copies of H in the random graph Gn,p, satisﬁes

E[Ds(Hp)] exp(−Ks) for every s satisfying 2 s (δ + ε)µ.

To this end, for every s 1, every k 1, and every m 1, let D(s,k,m) denote the set of all clusters {σ1,...,σs} of s distinct copies of H in Kn such that the graph σ1 ∪ ··· ∪ σs has k vertices (of nonzero degree) and m edges. We further let Ds,k,m denote the number of such clusters whose union is contained in Gn,p. When s 2, the union of any s distinct copies of H contains between vH and vHs vertices and between eH + 1 and eHs edges, and thus Ds,k,m = 0 unless vH k vHs and eH + 1 m eHs. We can therefore write

vHs

eHs

Ds(Hp) =

Ds,k,m.

m=eH+1

k=vH

- Claim 8.7. There exists a positive constant γ such that, for every s 2, every k vH, and every m eH + 1,


(2m)vH/2 s

k2 m

E[Ds,k,m] n−2γm

.

Proof. We ﬁrst show that, for every s 1, the set D(s,k,m) is empty unless

∆ 2

- 1

- 2vH · (k − vH). (66)


+

m − eH

We prove this fact by induction on s. The case s = 1 holds vacuously, as the set D(1,k,m) is nonempty only when k = vH and m = eH. Assume now that s 2 and let G be the union of copies of H that form some cluster in D(s,k,m). By deﬁnition, G has k vertices and m edges. Furthermore, for some s < s, k k and m < m, there exist a subgraph G ⊆ G and a copy σ

of H in Kn that intersects (the edge set of ) G such that G is the union of copies of H that form some cluster in D(s ,k ,m ), and G = G ∪ σ. We note that s may be strictly smaller than s − 1. Let J ⊆ H be the subgraph of H that is isomorphic to σ ∩ G , so that m = m + eH − eJ and k = k + vH − vJ. It follows from the inductive assumption that

∆ 2

- 1

- 2vH · (k − vH) + eH − eJ


m − eH = m − eJ

+

∆ 2

1 2vH · (k − vH) −

∆ 2

- 1

- 2vH · (vH − vJ) + eH − eJ.


=

+

+

We claim that the above inequality implies (66). This is obviously true when J = H. If J is a proper subgraph of H, then 2eJ ∆vJ − 1, since H is connected and ∆-regular, and therefore

∆vH 2 −

∆vJ − 1 2

∆ 2

1 2(vH − vJ) · (vH − vJ)

∆ 2

- 1

- 2vH · (vH − vJ),


+ which gives (66).

=

+

eH − eJ

To complete the proof of the claim, note that

k2 m ·

N(H,k,m) s

E[Ds,k,m] nkpm ·

,

where N(H,k,m) denotes the largest number of copies of H in a graph with k vertices and m edges. Inequality (66) implies that

2vH(m−eH)/(∆vH+1)

· np∆/2+1/(2v

H)

nkpm = nv

· nk−v

pm−e

pe

nv

pe

. Since p∆/2 C−1n−1 log n, the quantity nv

H

H

H

H

H

H

H is only polylogarithmic in n and np∆/2+1/(2v

H)

pe

H

n−γ for some positive constant γ . As m eH +1 and n is large, then there is a positive constant γ such that nkpm n−2γm. The claimed upper bound on E[Ds,k,m] now follows from Theorem 5.4, which implies that N(H,k,m) (2m)vH/2.

Claim 8.7 and the inequality ab (ea/b)b impy that

E[Ds,k,m] exp −2γmlog n + mlog(ek2/m) + slog e(2m)vH/2/s

exp −γmlog n + slog e(2m)vH/2/s ,

where the second inequality as k vHs vH(δ + ε)µ and µ is at most polylogarithmic in n, see (65). Let f : (0,∞) → (0,∞) be the function deﬁned by

f(x) = exp −γxlog n + slog e(2x)vH/2/s ,

so that E[Ds,k,m] f(m). Elementary calculus shows that f is maximised at x = svH/(2γ log n). Therefore,

e2/v

vHs1−2/v

svH 2γ log n

svH 2

svH 2

H

H

E[Ds,k,m] f

= exp −

+

log

. Since our assumptions imply that, see (65),

γ log n

(δ + η)µ 1−2/vH log n

s1−2/v

(δ + η)1−2/vH CvH−2 ,

H

log n

we may conclude that E[Ds,k,m] exp(−(K + vHeH)s), provided that C is suﬃciently large. Therefore, if C is suﬃciently large,

vHs

eHs

E[Ds,k,m] s2vHeH · exp(−Ks − vHeHs) exp(−Ks).

E[Ds(Hp)] =

m=eH+1

k=vH

This completes the proof.

9. Beyond polynomials with nonnegative coefficients

Although Theorem 3.1 applies only to the case where X = X(Y ) is a polynomial with nonnegative coeﬃcients, the proof can be adapted to yield a similar result for all nonnegative functions X : {0,1}N → R 0. In this case, the degree assumption in Theorem 3.1 has to be replaced by a more general assumption on the ‘complexity’ of X.

Given an I ⊆ N and a z ∈ {0,1}N, we let

F(I,z) = {y ∈ {0,1}N : yi = zi for all i ∈ I}; we call sets of this from subcubes. If F is a subcube, then there is a unique set I such that F = F(I,z), for some z. We can thus deﬁne the codimension of F by codim F = |I|. Given a nonnegative function X on the hypercube, we deﬁne the complexity of X to be the smallest integer d for which it is possible to represent X as a linear combination with nonnegative coeﬃcients of indicator functions of subcubes with codimension at most d. The complexity of X is well deﬁned, and at most N, since X = z∈{0,1}N X(z) F( N ,z) is such a linear combination. Note also that the complexity of every polynomial with nonnegative coeﬃcients and degree d is at most d.

Assume now that Y is a random variable taking values in {0,1}N and that X = X(Y ). Given a subcube F ⊆ {0,1}N, we write EF[X] = E[X | Y ∈ F] for the expectation of X conditioned on Y ∈ F. We further deﬁne ΦX : R 0 → R 0 ∪ {∞} by

ΦX(δ) = min − log P(Y ∈ F) : F ⊆ {0,1}N is a subcube with EF[X] (1 + δ)E[X] . (67)

If X is an increasing function of Y , this deﬁnition coincides with our earlier deﬁnition of ΦX(δ), because then the minimum is achieved at a subcube of the form F(I,1), where 1 is the Ndimensional all-ones vector. One may adapt the proof of Theorem 3.1 to show the following. (A precise proof of this theorem can be found in [23], which was written after this work was completed).

Theorem 9.1. For every positive integer d and all positive real numbers ε and δ with ε < 1/2,

there is a positive K = K(d,ε,δ) such that the following holds. Let Y be a sequence of N independent Ber(p) random variables for some p ∈ (0,1 − ε] and assume that X = X(Y ) is non-negative and has complexity at most d and satisﬁes ΦX(δ − ε) K log(1/p). Denote by F∗ the collection of all subcubes F ⊆ {0,1}N satisfying

- (F1) EF[X] (1 + δ − ε)E[X],
- (F2) codim F K · ΦX(δ + ε).


Then,

P X (1 + δ)E[X] (1 + ε) · P(Y ∈ F for some F ∈ F∗).

We note that this theorem does not exactly match Theorem 3.1; indeed, we only assert that the upper tail event is dominated by the appearance of a subcube in F∗. It is possible to further restrict the family F∗, analogous to the extraction of cores from seeds. We do not pursue this direction here.

Theorem 9.1 can be used to study the upper tail problem for induced subgraph counts. Suppose that H is a ﬁxed graph and X = Xn,pH-ind is the number of induced copies of H in the random graph Gn,p. Let N = n2 and, for an arbitrary bijection σn: n 2 → N , let Yi be the indicator random variable of the event that σn−1(i) is an edge in Gn,p. Then we can write

X =

(1 − Yσ

n(e)).

Yσ

n(e)

e∈(V(H)

)\E(H)

e∈E(H)

H ⊆Kn H ∼=H

2

In particular, the complexity of X is bounded by eH and Theorem 9.1 applies. On the other hand, it is clear that X is generally not monotone, so one cannot use Theorem 3.1. This direction was successfully pursued to by Cohen [23].

10. Concluding remarks Nonregular graphs. It is an open problem to extend Theorems 1.5 and 1.6 to nonregular graphs. It is straightforward to extend Theorem 1.6 to the more general case of strictly balanced graphs; however, note that Šileikis and Warnke [66] constructed balanced graphs for which the conclusion of Theorem 1.6 does not hold. In the localised regime, the results in [18, 24, 25, 30] apply to arbitrary (as opposed to only ∆-regular) graphs H; however, these works require polynomiallysuboptimal assumptions on the density p. Recently, Šileikis and Warnke [63] determined the order of the logarithmic upper tail probability for the number of copies of the star graph K1,s in Gn,p. The phase transition between the Poisson and the localised regimes. We believe that the logarithmic upper tail probabilities of the random variables considered in this paper are always determined by either the Poisson behaviour, the localised behaviour, or the coexistence of the two (in the regime where they are commensurate). More precisely, we believe that for both X = Xn,pH (for a connected, ∆-regular H) and X = XN,pk-AP,

− log P X (1 + δ)E[X] = 1 ± o(1) · min

ΦX(δ ) + ΨX(δ − δ ) , (68)

0 δ δ

as long as E[X] → ∞ and p → 0. Let p∗ = p∗(δ,n) be such that ΦX(δ) = ΨX(δ). Note that if p p∗, then ΨX(δ) ΦX(δ) and we recover Theorems 1.4 and 1.6, whereas if p p∗, we have ΨX(δ) ΦX(δ) and (68) implies (in some cases a stronger version of) Theorems 1.3, 1.5, and 1.7. If p = Θ(p∗), then both terms are of the same order and the conjecture allows for the upper tail to be dominated by conﬁgurations exhibiting features of both the Poisson and localised regimes.

Structural theorems for non-complete graphs. In the case where X = Xn,pH for a connected, ∆-regular graph H, we have neither determined the asymptotics of ΦX(δ) in the range np∆ → c ∈ (0,∞) nor given a structural description of the upper tail event {X (1 + δ)E[X]} for any density p. Doing the former would yield the logarithmic upper tail probability of X, via Proposition 7.1; it is likely that the value of ΦX(δ) is given by a mixture of the clique construction and a ‘hub-like’ construction in which a constant number of vertices have degrees linear in n. As for the latter, the method used to prove Theorem 5.11 can be generalised to yield an analogous statement in which Kr is replaced with an arbitrary ∆-regular graph H. Armed with such a ‘stability’ statement, it is relatively straightforward to show that, when np∆ → 0, the random graph Gn,p conditioned on the upper tail event {X (1 + δ)E[X]} contains an ‘almost-clique’ of the ‘right’ size, as was the case when H = Kr. We were not able to prove such a structural statement in the complementary range np∆ = Ω(1).

Stability results for arithmetic progressions. An interesting problem is to characterise the nearminimisers of the optimisation problem for ΦX(δ) when X = XN,pk-AP. More precisely, we ask for a description of all subsets I ⊆ N that satisfy EI[X] (1 + δ)E[X] and |I| (1 + ε)ΦX(δ + ε). As a consequence of Theorem 3.1 and the entropic stability of XN,pk-AP, which we established in the proof of Proposition 4.2, such a result would imply a structural characterisation of the upper tail event. Since the dominant contribution to the diﬀerence EI[X] − E[X] comes from k-term arithmetic progressions contained in I, this problem is equivalent to understanding the structure of sets I ⊆ Z that are near-maximisers of the number of k-term arithmetic progressions (among subsets of a given size). The structure of true maximisers was described by Green and Sisask [37] in the case for k = 3.

Decomposing the upper tail measure. Let Y¯ be the random variable obtained by conditioning Y

on the upper tail event {X(Y ) (1 + δ)E[X]} and let Y˜ be the random variable obtained by ﬁrst choosing a uniformly random solution I of the optimisation problem for ΦX(δ) and then conditioning Y on i∈I Yi = 1. It would be very interesting to determine necessary and suﬃcient conditions so that Y¯ and Y˜ are close in some metric. In particular, are the assumptions of

Theorem 3.1 suﬃciently strong to imply this? This question is closely related to the more general problem of decomposing a Gibbs measure into a mixture of product measures. The work of Eldan and Gross [31], and, more recently, of Austin [4], gives general conditions for the existence of such a decomposition.

Moderate deviations. Throughout this paper, we have assumed that δ is a ﬁxed, positive constant. It is interesting and natural to study the probability of {X (1 + δ)E[X]} when δ is allowed to depend on N and p. In the case where δ E[X] is of the same order as Var(X), one can often prove a Central Limit Theorem, see [6, 7, 61]. The regime in which δ E[X] Var(X) but δ → 0 is often referred to as the moderate deviation regime. One expects that, under reasonable assumptions, the logarithmic upper tail probability −log P(X (1+δ)E[X]) is of order min{(δ E[X])2/Var(X), ΦX(δ)}; this has been veriﬁed in certain cases, see [10, 33, 36, 38, 63, 69]. Our methods can be adapted to the moderate deviation regime. In an upcoming work [40], we calculate the logarithmic upper tail probability for X = XN,pk-AP for nearly all pairs (p,δ) for which localisation is believed to occur—that is, when ΦX(δ) (δ E[X])2/Var(X).

Other random graph models. Upper tails for subgraph counts have been considered in random graph models other than Gn,p, such as exponential random graphs [19], random geometric graphs [20], random regular graphs [39, 65], and (dense) uniform random graphs [27]. The framework developed here can be generalised to other (non-product) measures on the hypercube, providing a possible approach to such questions. It is likely that this requires adapting the notions of cores and entropic stability to the model.

Acknowledgements. We thank Bhaswar Bhattacharya, Asaf Cohen, Nicholas Cook, Ronen Eldan, Michael Krivelevich, Eyal Lubetzky, Matas Šileikis, Lutz Warnke, and Yufei Zhao for helpful comments and discussions. We are indebted to the three anonymous referees whose comments greatly improved the presentation of this paper.

References

- [1] N. Alon. On the number of subgraphs of prescribed type of graphs with a given number of edges. Israel J. Math., 38(1-2):116–130, 1981.
- [2] F. Augeri. A transportation approach to the mean-ﬁeld approximation. arXiv:1903.08021.
- [3] F. Augeri. Nonlinear large deviation bounds with applications to Wigner matrices and sparse Erdős-Rényi graphs. Ann. Probab., 48(5):2404–2448, 2020.
- [4] T. Austin. The structure of low-complexity Gibbs measures on product spaces. Ann. Probab., 47(6):4002–4023, 2019.
- [5] J. Balogh, R. Morris, W. Samotij, and L. Warnke. The typical structure of sparse Kr+1-free graphs. Trans. Amer. Math. Soc., 368(9):6439–6485, 2016.
- [6] A. D. Barbour, M. Karoński, and A. Ruciński. A central limit theorem for decomposable random variables with applications to random graphs. J. Combin. Theory Ser. B, 47(2):125–145, 1989.
- [7] Y. Barhoumi-Andréani, C. Koch, and H. Liu. Bivariate ﬂuctuations for the number of arithmetic progressions in random sets. Electron. J. Probab., 24:Paper No. 145, 32, 2019.
- [8] A. Basak and R. Basu. Upper tail large deviations of regular subgraph counts in Erdős–Rényi graphs in the full localized regime. arXiv:1912.11410.
- [9] B. B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313–347, 2017.
- [10] B. B. Bhattacharya, S. Ganguly, X. Shao, and Y. Zhao. Upper tail large deviations for arithmetic progressions in a random set. Int. Math. Res. Not. IMRN, (1):167–213, 2020.
- [11] B. Bollobás. Threshold functions for small subgraphs. Math. Proc. Camb. Philos. Soc., 90(2):197–206, 1981.
- [12] B. Bollobás. Random graphs. Cambridge University Press, Cambridge, 2nd edition, 2001.
- [13] J. A. Bondy and U. S. R. Murty. Graph theory, volume 244 of Graduate Texts in Mathematics. Springer, New York, 2008.
- [14] S. Boucheron, G. Lugosi, and P. Massart. Concentration inequalities. Oxford University Press, Oxford, 2013.
- [15] J. Briët and S. Gopi. Gaussian width bounds with applications to arithmetic progressions in random settings. Int. Math. Res. Not. IMRN, (22):8673–8696, 2020.


- [16] S. Chatterjee. The missing log in large deviations for triangle counts. Random Structures Algorithms, 40(4):437– 451, 2012.
- [17] S. Chatterjee. Large deviations for random graphs, volume 2197 of Lecture Notes in Mathematics. Springer, Cham, 2017. Lecture notes from the 45th Probability Summer School held in Saint-Flour (École d’Été de Probabilités de Saint-Flour), June 2015.
- [18] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016.
- [19] S. Chatterjee and P. Diaconis. Estimating and understanding exponential random graph models. Ann. Statist., 41(5):2428–2461, 2013.
- [20] S. Chatterjee and M. Harel. Localization in random geometric graphs with too many edges. Ann. Probab., 48(2):574–621, 2020.
- [21] S. Chatterjee and S. R. S. Varadhan. The large deviation principle for the Erdős–Rényi random graph. European J. Combin., 32(7):1000–1017, 2011.
- [22] F. R. K. Chung, R. L. Graham, P. Frankl, and J. B. Shearer. Some intersection theorems for ordered sets and graphs. J. Combin. Theory Ser. A, 43:23–37, 1986.
- [23] A. Cohen. The upper tail problem for induced 4-cycles in sparse random graphs. M.Sc. thesis, 2021.
- [24] N. Cook and A. Dembo. Large deviations of subgraph counts for sparse Erdős-Rényi graphs. Adv. Math., 373:107289, 53, 2020.
- [25] N. A. Cook, A. Dembo, and H. T. Pham. Regularity method and large deviation principles for the Erdős–Rényi hypergraph. arXiv:2102.09100.
- [26] R. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Structures Algorithms, 41(4):469–487, 2012.
- [27] A. Dembo and E. Lubetzky. A large deviation principle for the Erdős–Rényi uniform random graph. Electron. Commun. Probab., 23, 2018.
- [28] A. Dembo and O. Zeitouni. Large deviations techniques and applications, volume 38 of Applications of Mathematics. Springer, New York, 2nd edition, 1998.
- [29] R. Diestel. Graph theory, volume 173 of Graduate Texts in Mathematics. Springer, Berlin, 5th edition, 2017.
- [30] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Geom. Funct. Anal., 28(6):1548–1596, 2018.
- [31] R. Eldan and R. Gross. Decomposition of mean-ﬁeld Gibbs distributions into product measures. Electron. J. Probab., 23, 2018.
- [32] P. Erdős. On the number of complete subgraphs contained in certain graphs. Magyar Tud. Akad. Mat. Kutató Int. Közl., 7:459–464, 1962.
- [33] G. Fiz Pontiveros, S. Griﬃths, M. Secco, and O. Serra. Deviation probabilities for arithmetic progressions and other regular discrete structures. arXiv:1910.12835.
- [34] E. Friedgut and J. Kahn. On the number of copies of one hypergraph in another. Israel J. Math., 105:251–256, 1998.
- [35] D. Galvin. Three tutorial lectures on entropy and counting. arXiv:1406.7872.
- [36] C. Goldschmidt, S. Griﬃths, and A. Scott. Moderate deviations of subgraph counts in the Erdős-Rényi random graphs G(n, m) and G(n, p). Trans. Amer. Math. Soc., 373(8):5517–5585, 2020.
- [37] B. Green and O. Sisask. On the maximal number of 3-term arithmetic progressions in subsets of Z/pZ. Bulletin London Math. Soc., 40(6):945–955, 2008.
- [38] S. Griﬃths, C. Koch, and M. Secco. Deviation probabilities for arithmetic progressions and irregular discrete structures. arXiv:2012.09280.
- [39] B. Gunby. Upper tails of subgraph counts in sparse regular graphs. arXiv:2010.00658.
- [40] M. Harel, F. Mousset, and W. Samotij. Upper tails for arithmetic progressions in the moderate deviation regime. Manuscript.
- [41] T. E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc., 56:13–20, 1960.
- [42] W. Hoeﬀding. Probability inequalities for sums of bounded random variables. J. Amer. Statist. Assoc., 58(301):13–30, 1963.
- [43] S. Janson. Poisson approximation for large deviations. Random Structures Algorithms, 1(2):221–229, 1990.
- [44] S. Janson, K. Oleszkiewicz, and A. Ruciński. Upper tails for subgraph counts in random graphs. Israel J. Math., 142:61–92, 2004.
- [45] S. Janson and A. Ruciński. The infamous upper tail. Random Structures Algorithms, 20(3):317–342, 2002.
- [46] S. Janson and A. Ruciński. The deletion method for upper tail estimates. Combinatorica, 24(4):615–640, 2004.
- [47] S. Janson and A. Ruciński. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat., 49(1):79–96, 2011.
- [48] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Structures Algorithms, 48(2):219–246, 2016.


- [49] M. Karoński and A. Ruciński. On the number of strictly balanced subgraphs of a random graph. In Graph Theory, Lágow 1981, volume 1018 of Lecture Notes in Mathematics, pages 79–83. Springer, 1983.
- [50] G. Katona. A theorem of ﬁnite sets. In Proc. Colloq. Theory of Graphs, Tihany 1966, pages 187–207. Academic Press, New York, 1966.
- [51] P. Keevash. Shadows and intersections: Stability and new proofs. Adv. Math., 218:1685–1703, 2008.
- [52] J. H. Kim and V. H. Vu. Concentration of multivariate polynomials and its applications. Combinatorica, 20(3):417–434, 2000.
- [53] J. H. Kim and V. H. Vu. Divide and conquer martingales and the number of triangles in a random graph. Random Structures Algorithms, 24(2):166–174, 2004.
- [54] G. Kozma and W. Samotij. Lower tails via relative entropy. arXiv:2104.04850.
- [55] J. B. Kruskal. The number of simplices in a complex. In Mathematical Optimization Techniques, volume 10, pages 251–278. Univ. of California Press, Berkeley, CA, 1963.
- [56] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Structures Algorithms, 47(1):109–146, 2015.
- [57] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures Algorithms, 50(3):420–436, 2017.
- [58] F. Mousset, A. Noever, K. Panagiotou, and W. Samotij. On the probability of nonexistence in binomial subsets. Ann. Probab., 48(1):493–525, 2020.
- [59] S. Mukherjee and B. B. Bhattacharya. Replica symmetry in upper tails of mean-ﬁeld hypergraphs. Adv. in Appl. Math., 119:102047, 25, 2020.
- [60] I. Rivin. Counting cycles and ﬁnite dimensional Lp norms. Adv. in Appl. Math., 29(4):647–662, 2002.
- [61] A. Ruciński. When are small subgraphs of a random graph normally distributed? Probab. Theory Related Fields, 78(1):1–10, 1988.
- [62] M. Šileikis. On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin., 19(1):4, 2012.
- [63] M. Šileikis and L. Warnke. Upper tail bounds for stars. Electron. J. Combin., 27(1):Paper No. 1.67, 23, 2020.
- [64] M. Talagrand. Concentration of measure and isoperimetric inequalities in product spaces. Publ. Math. Inst. Hautes Études Sci., 81(1):73–205, 1995.
- [65] P. van der Hoorn, G. Lippner, and E. Mossel. Regular graphs with linearly many triangles. arXiv:1904.02212.
- [66] M. Šileikis and L. Warnke. A counterexample to the DeMarco-Kahn upper tail conjecture. Random Structures Algorithms, 55(4):775–794, 2019.
- [67] V. H. Vu. On the concentration of multivariate polynomials with small expectation. Random Structures Algorithms, 16(4):344–363, 2000.
- [68] V. H. Vu. Concentration of non-Lipschitz functions and applications. Random Structures Algorithms, 20(3):262– 316, 2002.
- [69] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math., 221(1):317–365, 2017.
- [70] L. Warnke. On the missing log in upper tail estimates. J. Combin. Theory Ser. B, 140:98–146, 2020.
- [71] Y. Zhao. On the lower tail variational problem for random graphs. Combin. Probab. Comput., 26(2):301–320, 2017.


Matan Harel, Department of Mathematics, Northeastern University, Boston, MA 02115, USA Email address: m.harel@northeastern.edu

Frank Mousset, School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel Email address: moussetfrank@gmail.com

Wojciech Samotij, School of Mathematical Sciences, Tel Aviv University, Tel Aviv 6997801, Israel Email address: samotij@tauex.tau.ac.il

