---
type: source
kind: paper
title: What does a typical metric space look like?
authors: Gady Kozma, Tom Meyerovitch, Ron Peled, Wojciech Samotij
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.01689v2
source_local: ../raw/2021-kozma-what-does-typical-metric.pdf
topic: general-knowledge
cites:
---

arXiv:2104.01689v2[math.PR]29May2022

WHAT DOES A TYPICAL METRIC SPACE LOOK LIKE?

GADY KOZMA, TOM MEYEROVITCH, RON PELED AND WOJCIECH SAMOTIJ

To the memory of Dima Ioﬀe, our friend and colleague. Mathematical physicist, probabilist and a dear person who freely shared his good advice and insight. His passing is a great loss to our community.

Abstract. The collection Mn of all metric spaces on n points whose diameter is at most 2 can naturally be viewed as a compact

), known as the metric polytope. In this paper, we study the metric polytope for large n and show that it is close to the cube [1,2](n

convex subset of R(n

2

) ⊆ Mn in the following two senses. First, the volume of the polytope is not much larger than that of the cube, with the following quantitative estimates:

2

(1/6 + o(1))n3/2 ≤ log Vol(Mn) ≤ O(n3/2). Second, when sampling a metric space from Mn uniformly at random, the minimum distance is at least 1−n−c with high probability, for some c > 0. Our proof is based on entropy techniques. We discuss alternative approaches to estimating the volume of Mn using exchangeability, Szemer´edi’s regularity lemma, the hypergraph container method, and the K˝va´ri–So´s–Tur´an theorem.

1. Introduction

For a positive integer n, let n := {1, . . ., n} and let n 2 be the set of all unordered pairs of distinct elements in n . A ﬁnite metric space on n ≥ 2 points can be regarded as an array (dij) with {i, j} ∈ n 2 , where dij denotes the distance between the ith and jth points in the space. Such a metric space may also be regarded as an element of R(

n 2

)

![image 1](<2021-kozma-what-does-typical-metric_images/imageFile1.png>)

The research of G.K. was supported by the ISF, by the Jesselson foundation, and by Paul and Tina Gardner. The research of T.M. was supported by ISF Grants 626/14 and 1052/18. The research of R.P. was supported by ISF Grants 1048/11, 861/15 and 1971/19, by IRG Grant SPTRF, and ERC grant LocalOrder. The research of W.S. was supported by ISF Grants 1147/14 and 1145/18.

1

satisfying certain restrictions among its coordinates. Speciﬁcally, the set of all such metric spaces is the cone

n 2

) : dij > 0 and dij ≤ dik + dkj for all i, j, k}.

Cn := {(dij) ∈ R(

Our goal in this work is to study a ‘uniformly chosen metric space on n points’. This is interpreted as a metric space sampled according to the Lebesgue measure from a suitable bounded subset of Cn. There are several natural choices for such a bounded subset. In this work, we focus on the diameter normalisation, that is, we bound the maximal diameter of the space from above. We thus deﬁne the metric polytope

Mn := {(dij) ∈ Cn : dij ≤ 2 for all i, j}.

The speciﬁc upper bound on the diameter amounts only to a scaling factor, with the constant two chosen to simplify some of the later expressions.

Understanding the structure of a uniformly chosen metric space in Mn is intimately related to understanding the volume of Mn. By construction, we have the trivial upper bound

n 2

). (1)

Vol(Mn) ≤ 2(

To obtain a lower bound, we make the following observation: Any triple x, y, z ∈ [1, 2] satisﬁes the triangle inequality x ≤ y + z and,

n 2

). This yields the lower bound

consequently, Mn contains the cube [1, 2](

Vol(Mn) ≥ 1. (2)

The precise behaviour of the volume Vol(Mn) seems diﬃcult to study. For instance, while intuitive, we do not know whether Vol(Mn+1) ≥ Vol(Mn) for all n (see also Section 7.1). It is thus interesting to note that at least the ‘radius’ Vol(Mn)1/(

n 2

) exhibits some regularity. Proposition 1.1. The sequence n  → Vol(Mn)1/(

n 2

) is non-increasing.

The proposition is deduced from Shearer’s inequality, see Section 4.1. It allows to obtain increasingly reﬁned volume estimates for Vol(Mn) via ﬁnite computations. For instance, one may check that Vol(M3) = 4 (see Figure 1) and hence we have the inequality

n 2

) for all n ≥ 3, (3) improving upon the trivial upper bound (1). Mascioni [32] calculated Vol(M4) = 13615 and used it to deduce a bound on Vol(Mn) that is

(

1 3

Vol(Mn) ≤ 4

![image 2](<2021-kozma-what-does-typical-metric_images/imageFile2.png>)

![image 3](<2021-kozma-what-does-typical-metric_images/imageFile3.png>)

stronger than (3) but weaker than what can be deduced from Proposition 1.1. The proposition and (2) imply that the limit

n 2

) (4) exists, which raises the natural question of ﬁnding its value.

Vol(Mn)1/(

lim

n→∞

Our main result is that a uniformly chosen metric space is ‘almost in [1, 2](

n 2

)’, as the following two theorems make precise. Our ﬁrst theorem shows that the limiting constant (4) equals one, that is,

2) as n → ∞. (5)

Vol(Mn) = 2o(n

In fact, our analysis goes much further and determines the second-order term in the logarithm of the volume up to a multiplicative constant.1

- Theorem 1.2. The following asymptotic estimates hold as n → ∞: exp (1/6 − o(1))n3/2 ≤ Vol(Mn) ≤ exp Cn3/2 (6)

for some absolute constant C.

Our second theorem studies the minimum distance in a typical metric space in Mn. Let d be a uniformly sampled metric space from Mn. Since

P min

i,j

dij > 1 − δ ≤

(1 + δ)(

n 2

) Vol(Mn)

![image 4](<2021-kozma-what-does-typical-metric_images/imageFile4.png>)

,

the lower bound in Theorem 1.2 implies that, for any a < 13, P min

![image 5](<2021-kozma-what-does-typical-metric_images/imageFile5.png>)

i,j

dij ≤ 1 −

a √n → 1 as n → ∞. (7)

![image 6](<2021-kozma-what-does-typical-metric_images/imageFile6.png>)

![image 7](<2021-kozma-what-does-typical-metric_images/imageFile7.png>)

Complementing this fact, we show that, in a typical metric space, the minimum distance is polynomially close to one.

- Theorem 1.3. There exist constants C, c > 0 such that, for all n ≥ 2, if d is a uniformly sampled metric space from Mn, then


dij ≤ 1 − n−c ≤ Cn−c.

P min

i,j

It would be interesting to ﬁnd the typical order of 1 − mini,j dij, see also Section 7.1. Our proof shows that it is at most n−1/30.

![image 8](<2021-kozma-what-does-typical-metric_images/imageFile8.png>)

) if we chose to normalise the diameter of Mn to be M, instead of 2.

), which would become (M/2)(

1Note that (6) hides the ﬁrst-order term (2/2)(

n 2

n 2

Figure 1. M3 inside [0, 2]3.

Reader’s guide. The heart of this work is the proof of the upper bound on the volume of Mn in (6), which relies on entropy techniques; a conceptual outline of our argument is presented in the next section. We review the relevant background on diﬀerential entropy in Section 2. The volume estimate itself is then proved in Section 4.3. One of the main ingredients in the argument is an upper bound on the maximum entropy of a vector of independent random variables that is almost supported in a given compact, convex set; this result is derived in Section 3. Several alternative approaches to proving upper bounds on the volume of Mn, which lead to results weaker than Theorem 1.2, are reviewed in Section 6.

Our proof of the lower bound on the volume is a fairly simple application of the Local Lemma of Erd˝os and Lova´sz [18], see Section 4.2.

The starting point for the proof of Theorem 1.3, given in Section 5, is an upper bound on the probability that the distance between a ﬁxed pair of points is shorter than one (Proposition 4.5), which is a byproduct of our proof of the upper bound on the volume of Mn. The assertion of the theorem is then deduced via elementary, but nontrivial, combinatorial arguments.

Section 7 contains some further discussion and a selection of open questions.

A remark on precedence. This paper has been long in writing and a number of results have appeared in the interim, notably Mubayi and Terry [34] and Balogh and Wagner [8], who considered the number of metric spaces with distances in the discrete set {1, . . ., M}. The methods of [8] also yielded the upper bound Vol(Mn) ≤ exp(n11/6+o(1)). (We elaborate on the relation between the discrete and the continuous model in Section 7.2.) These papers have kindly acknowledged

- our precedence, but, for fairness, it should be noted that we did not have the upper bound of Theorem 1.2 then, only a bound of the form


Vol(Mn) ≤ exp(n2−c); in particular, the volume bound of [8] was stronger than ours. Several months before we streamlined the entropy argument underlying the proof of the upper bound in Theorem 1.2 to yield the estimate Vol(Mn) ≤ exp(Cn3/2), in a joint work with Rob Morris, we found a more eﬃcient version of the argument of Balogh and Wagner [8], based on the method of hypergraph containers, that gives the estimate Vol(Mn) ≤ exp Cn3/2(log n)3 ; we present a detailed sketch of this argument in Section 6.3.

Further directions and related work. We believe that the general method of relating entropy and independence that underlies our proof of Theorem 1.2 will ﬁnd many further applications. In particular, the ﬁrst and the fourth named authors adapted the methods of this work, and combined them with the arguments underlying the proofs of the hypergraph container theorems [6, 36], to study lower tails of random variables that can be expressed as polynomials of independent Bernoulli random variables [28].

Similar ideas of relating entropy and independence were used by Tao [38, Lemma 4.3] to develop a probabilistic interpretation of Szemer´edi’s regularity lemma. Concurrently with the writing of this paper, Ellis, Friedgut, Kindler, and Yehudayoﬀ [15] used a related approach to prove stability versions of the Loomis–Whitney inequality and the more general Uniform Cover inequality. The pigeonhole principle argument that appears in our proof outline below (see also Lemma 4.3) is somewhat reminiscent of the Lova´sz–Szeg´edy Hilbert space regularity lemma, see the proof of [31, Lemma 4.1] (we thank Bala´zs Ra´th for pointing out this connection).

- 1.1. Proof outline. Suppose that d is a uniformly chosen metric space from Mn. Conceptually, our argument consists of three steps.


- Step I (conditioning). We say that a subset F ⊆ n 2 has the conditioned almost independence property if the following holds: Conditioned on all the distances df with f ∈ F, for each triangle {i, j, k} whose edges lie outside of F, the distances dij, dik, and djk become close to mutually independent.


The goal of the ﬁrst step is to ﬁnd a ‘small’ set F with the above property. In order to show this, for m ≥ 0, deﬁne the set

n 2

: max{s, t} > n − m

Fm := {s, t} ∈

and examine the conditional entropy h(Fm) := H d12 | {df : f ∈ Fm} .

Since Fm+1 ⊇ Fm, monotonicity of conditional entropy implies that the sequence m  → h(Fm) is nonincreasing. Moreover, it is not diﬃcult to bound h(F0) from above and h(F√n) from below by absolute constants. Thus, the pigeonhole principle produces an m0 with 0 ≤ m0 ≤

![image 9](<2021-kozma-what-does-typical-metric_images/imageFile9.png>)

√n for which

![image 10](<2021-kozma-what-does-typical-metric_images/imageFile10.png>)

C √n

) − h(Fm

0+1) ≤

h(Fm

(8)

![image 11](<2021-kozma-what-does-typical-metric_images/imageFile11.png>)

0

![image 12](<2021-kozma-what-does-typical-metric_images/imageFile12.png>)

for some absolute constant C. The set F described above is taken to be Fm

. Its cardinality is at most m0n ≤ n3/2. We now argue that F has the conditioned almost independence property. Since {1, n − m0}, {2, n − m0} ∈ Fm

0

0+1 \ Fm

, inequality (8) gives (again using the monotonicity of conditioned entropy)

0

C √n

h(F) − h F ∪ {{1, n − m0}, {2, n − m0}} ≤

.

![image 13](<2021-kozma-what-does-typical-metric_images/imageFile13.png>)

![image 14](<2021-kozma-what-does-typical-metric_images/imageFile14.png>)

Symmetry considerations show that, in fact, for every ordered triple of distinct i, j, k ∈ n − m0 , we have

C √n

H dij | {df : f ∈ F} − H dij | {df : f ∈ F} ∪ {dik, djk} ≤

. (9)

![image 15](<2021-kozma-what-does-typical-metric_images/imageFile15.png>)

![image 16](<2021-kozma-what-does-typical-metric_images/imageFile16.png>)

Inequality (9) is the notion of almost independence that we need. It may be conveniently restated in terms of the average Kullback–Leibler divergence between the conditional (on all df with f ∈ F) joint distribution of dij, dik, djk and the product of the (conditional) marginal distributions of dij, dik, and djk:

E DKL ((dij, dik, djk) dij × dik × djk) ≤

C √n

. (10)

![image 17](<2021-kozma-what-does-typical-metric_images/imageFile17.png>)

![image 18](<2021-kozma-what-does-typical-metric_images/imageFile18.png>)

- Step II (subadditivity). Since d is a uniformly sampled metric space from Mn,


H(d) = log Vol(Mn) . Using the chain rule for conditional entropy, we may write

+ H({df : f ∈/ F} | {df : f ∈ F})

H(d) = H({df : f ∈ F})

. (11)

![image 19](<2021-kozma-what-does-typical-metric_images/imageFile19.png>)

![image 20](<2021-kozma-what-does-typical-metric_images/imageFile20.png>)

![image 21](<2021-kozma-what-does-typical-metric_images/imageFile21.png>)

![image 22](<2021-kozma-what-does-typical-metric_images/imageFile22.png>)

α

β

Since df ∈ [0, 2] for every f ∈ F, we have α ≤ |F| log2. By considering an arbitrary Steiner triple system on n−O(1) vertices, one sees that the complement of F can be partitioned into a family T of edge-disjoint

triangles and a leftover set of pairs G with |G| ≤ C(|F| + n). Using subadditivity of entropy,

β ≤ |G| log 2 +

H(dij, dik, djk | {df : f ∈ F}). (12)

{i,j,k}∈T

- Step III (entropy-maximising distributions). Combining the above two


steps, we arrive at the problem of bounding H(dij, dik, djk | {df : f ∈ F}), which, by conditioned almost independence, amounts to estimating the largest entropy of a vector that is supported on M3 and satisﬁes (10). We ﬁrst observe that (10) implies the following inequality:

C √n

E P(dij × dik × djk ∈/ M3) ≤

,

![image 23](<2021-kozma-what-does-typical-metric_images/imageFile23.png>)

![image 24](<2021-kozma-what-does-typical-metric_images/imageFile24.png>)

see Lemma 2.7. This allows us to bound H(dij, dik, djk | {df : f ∈ F}) by the largest entropy of a vector of (fully) independent random

variables that is almost supported on M3. To this end, we prove a general statement (Theorem 3.1) showing that the largest entropy of a vector of independent random variables that is almost supported on a convex set P cannot be much larger than the logarithm of the volume of the largest box contained in P. In the case P = M3, the (unique) largest such box is [1, 2]3 (Lemma 3.4) and, consequently, the entropy cannot be much larger than zero.

The three steps suﬃce to show that the volume of Mn is exp(o(n2)), that is, that the limiting constant in (4) is one. Moreover, the various error terms are polynomially related and the above argument shows the quantitative estimate Vol(Mn) ≤ exp(Cn2−c) for an explicit c > 0. To obtain the sharp exponent 3/2, as in the statement of Theorem 1.2, several enhancements to the above argument are made. In particular, the following two bounds are proved:

n−2

n−2

|Fm+1 \ Fm| · h(Fm) ≤ n ·

log(Vol(Mn)) ≤

h(Fm), (13)

m=0

m=0

h(Fm) ≤ C h(Fm) − h(Fm+1) 1/3. (14)

The bound (14) implies that h(Fm) ≤ C′(m + 1)−1/2, as shown in Lemma 4.2, which gives the claimed estimate after substituting it into (13). The estimate (13) improves upon the subadditivity step, making use of the symmetry inherent in the speciﬁc choice of the sets Fm, see (63). Inequality (14) is obtained using a more careful analysis in steps one and three above.

2. Entropy and almost independence

- 2.1. Diﬀerential entropy. We now recall the notion and some properties of diﬀerential entropy, the entropy of continuous random variables. Readers who are used to the entropy of discrete random variables (Shannon’s entropy) should keep in mind that in the continuous case entropies can be either positive or negative, the value 0 plays no special role.


Given an absolutely continuous probability measure µ on Rk with density f and a random variable X ∼ µ, the diﬀerential entropy (or simply entropy) of µ (or of X) is deﬁned as

H(µ) := H(X) := − log(f(x))f(x)dx = − log (f(x))dµ(x),

(15) whenever the above integral is well-deﬁned. As is customary, if random variables X1, . . ., Xm have a joint density function, we will write H(X1, . . ., Xm) for the entropy of the random vector (X1, . . ., Xm). Throughout the paper, we write log to denote the natural logarithm.

Observe that if X takes values in a compact set K ⊆ Rk, then by Jensen’s inequality,

1 f(x)

H(X) = −

log(f(x))f(x)dx =

log

f(x)dx

![image 25](<2021-kozma-what-does-typical-metric_images/imageFile25.png>)

K∩{f>0}

K

(16)

1 f(x)

f(x)dx ≤ log(Vol(K)).

≤ log

![image 26](<2021-kozma-what-does-typical-metric_images/imageFile26.png>)

K∩{f>0}

Diﬀerential entropy may be negative, e.g., if Vol(K) < 1 above. It could even happen that H(X) = −∞. However, one easily checks that if the density f is bounded, then H(X) > −∞. In view of this, for the sake of simplicity, from now on we focus on probability measures on Rk that are compactly supported and admit a bounded density. We denote the family of all such measures by A (Rk). We emphasize that A (Rk) is closed under projections.

Fact 2.1. If X ∈ Rk

and Y ∈ Rk

have a joint distribution in A (Rk

1

2

1+k2), then the distribution of X is in A (Rk

).

1

Keeping in mind the case of equality in Jensen’s inequality and applying it to (16), let us note the following for future reference.

- Lemma 2.2. If the distribution of a random variable X is in A (Rk) and X takes values in a compact set K, then


−∞ < H(X) ≤ log(Vol(K)).

The second inequality holds with equality if and only if X is uniform on K.

Further use is made of the following generalisation of (16) for which we also provide a quantitative ‘stability’ estimate.

- Lemma 2.3. Let K ⊆ Rk be a bounded measurable set and let f : Rk → [0, ∞) be a bounded measurable function. Set p := K f(x)dx. Then


Vol(K) p

−

f(x) log(f(x))dx ≤ p log

, (17)

![image 27](<2021-kozma-what-does-typical-metric_images/imageFile27.png>)

K

where we interpret the right-hand side as 0 if p = 0, and deﬁne 0 log 0 = 0 for the left-hand side.

Moreover, if K admits a partition K = K1 ∪ K2 for measurable K1, K2 and either

K1 f(x)dx K f(x)dx ≤

1 10 ·

Vol(K1) Vol(K)

![image 28](<2021-kozma-what-does-typical-metric_images/imageFile28.png>)

![image 29](<2021-kozma-what-does-typical-metric_images/imageFile29.png>)

![image 30](<2021-kozma-what-does-typical-metric_images/imageFile30.png>)

then

f(x)dx K f(x)dx ≥ 10 ·

Vol(K1) Vol(K)

or K

1

![image 31](<2021-kozma-what-does-typical-metric_images/imageFile31.png>)

![image 32](<2021-kozma-what-does-typical-metric_images/imageFile32.png>)

−

Vol(K) p −

f(x) log(f(x)) dx ≤ p log

![image 33](<2021-kozma-what-does-typical-metric_images/imageFile33.png>)

K

p 4 · max

Vol(K1) Vol(K)

![image 34](<2021-kozma-what-does-typical-metric_images/imageFile34.png>)

![image 35](<2021-kozma-what-does-typical-metric_images/imageFile35.png>)

f(x)dx K f(x)dx

, K

1

![image 36](<2021-kozma-what-does-typical-metric_images/imageFile36.png>)

. (18)

Proof. The bound is trivial if p = 0. Otherwise, since g := f/p satisﬁes −

f(x) log(f(x)) dx = −p

g(x) log(g(x)) dx − p log p,

K

K

it suﬃces to prove the results when p = 1, as we now assume. The estimate (17) follows from the same calculation as in (16). We proceed to prove (18). Set r := K

f(x)dx

K f(x)dx = K

f(x)dx and

1

![image 37](<2021-kozma-what-does-typical-metric_images/imageFile37.png>)

1

- q := Vol(K


1)

Vol(K) so that either r ≤ 101 q or r ≥ 10q. Invoking (17) twice yields

![image 38](<2021-kozma-what-does-typical-metric_images/imageFile38.png>)

![image 39](<2021-kozma-what-does-typical-metric_images/imageFile39.png>)

−

f(x) log(f(x))dx = −

K

≤ r log

+

K2

K1

Vol(K1) r

![image 40](<2021-kozma-what-does-typical-metric_images/imageFile40.png>)

f(x) log(f(x))dx

+ (1 − r) log

Vol(K2) (1 − r)

![image 41](<2021-kozma-what-does-typical-metric_images/imageFile41.png>)

,

which, by the deﬁnition of q, is easily seen to be equivalent to:

log(Vol(K)) +

f(x) log(f(x))dx

K

1 − r 1 − q

r q

+ (1 − r) log

≥ r log

.

![image 42](<2021-kozma-what-does-typical-metric_images/imageFile42.png>)

![image 43](<2021-kozma-what-does-typical-metric_images/imageFile43.png>)

Deﬁne D(x) := xlog(x/q)+(1−x) log((1−x)/(1−q)), so that the righthand side above is D(r). (An observant reader will recognise that D(r) is the Kullback–Leibler divergence between Bernoulli random variables with success probabilities r and q, respectively.) Note that D(q) = 0 and that

1 − x 1 − q

x q − log

D′(x) = log

. (19)

![image 44](<2021-kozma-what-does-typical-metric_images/imageFile44.png>)

![image 45](<2021-kozma-what-does-typical-metric_images/imageFile45.png>)

Observe further that D′(x) is an increasing function of x and D′(q) = 0. This implies that, in the case where r ≤ q/10,

q − r 2 · −D′

9q 20 · log

q 4

r + q 2 ≥

20 11 ≥

D(r) ≥

![image 46](<2021-kozma-what-does-typical-metric_images/imageFile46.png>)

![image 47](<2021-kozma-what-does-typical-metric_images/imageFile47.png>)

![image 48](<2021-kozma-what-does-typical-metric_images/imageFile48.png>)

![image 49](<2021-kozma-what-does-typical-metric_images/imageFile49.png>)

![image 50](<2021-kozma-what-does-typical-metric_images/imageFile50.png>)

and, in the case where r ≥ 10q,

r − q 2 · D′

r + q 2 ≥

9r 20 · log

D(r) ≥

![image 51](<2021-kozma-what-does-typical-metric_images/imageFile51.png>)

![image 52](<2021-kozma-what-does-typical-metric_images/imageFile52.png>)

![image 53](<2021-kozma-what-does-typical-metric_images/imageFile53.png>)

r 4

11 2 ≥

.

![image 54](<2021-kozma-what-does-typical-metric_images/imageFile54.png>)

![image 55](<2021-kozma-what-does-typical-metric_images/imageFile55.png>)

- 2.2. Conditional entropy. For random variables X ∈ Rk


and Y ∈ Rk

1

1+k2, the conditional entropy of X given Y , denoted by H(X | Y ), is the average over Y of the entropy of the conditional distribution of X given Y . Formally, if we write

having a joint density f on Rk

- 2


- f(x, y)

![image 56](<2021-kozma-what-does-typical-metric_images/imageFile56.png>)

- g(y)


g(y) := f(x, y) dx and fy(x) :=

, (20)

with fy deﬁned for almost every y with respect to the distribution of Y , then

H(X | Y ) := H(X{Y=y})g(y) dy = − log (fy(x)) fy(x)dxg(y) dy,

(21) whenever the above integral is well deﬁned, where X{Y=y} denotes the random variable X conditioned on the event {Y = y}. Note that, using Fact (2.1), H(X | Y ) is well deﬁned and ﬁnite whenever the joint distribution of X and Y is in A (Rk

1+k2).

- 2.3. Kullback–Leibler divergence. Given two absolutely continu-

ous probability measures µ and ν on Rk with densities f and g, respectively, and random variables X ∼ µ and Y ∼ ν, we deﬁne the Kullback–Leibler divergence between µ and ν (or between X and Y ) by

DKL (µ ν) := DKL (X Y ) := log

- f(x)

![image 57](<2021-kozma-what-does-typical-metric_images/imageFile57.png>)

- g(x)


f(x) dx. (22)

Since log y ≥ 1 − 1/y for every y > 0, we see that

DKL (µ ν) ≥ 1 −

g(x) f(x)

![image 58](<2021-kozma-what-does-typical-metric_images/imageFile58.png>)

f(x) dx = 0. (23)

In particular, the integral in (22) is well deﬁned, possibly as +∞.

We note a simple relation between the entropy of a pair of random variables and their Kullback–Leibler divergence. Let X and Y be random variables taking values in Rk

1

and Rk

2

, respectively, with a joint distribution in A (Rk

1+k2). A direct calculation shows that

H(X, Y ) = H(X) + H(Y ) − DKL ((X, Y ) X × Y ) , (24)

where we use the notation X × Y to denote a random variable whose distribution is the product of the marginal distribution of X and the marginal distribution of Y ; in other words, X × Y is composed of independent copies of X and Y .

- 2.4. Properties of entropy. We now recall some standard facts about entropy.


- Lemma 2.4. Suppose X ∈ Rk


, Y ∈ Rk

, Z ∈ Rk

have a joint distribution in A (Rk

1

2

3

1+k2+k3). Then

- (i) H(X, Y ) = H(X | Y ) + H(Y ),
- (ii) H(X | Y ) ≤ H(X),
- (iii) H(X, Y ) ≤ H(X) + H(Y ),
- (iv) H(X | Y, Z) ≤ H(X | Y ).


Proof. Note ﬁrst that our assumption on the joint distribution of X, Y , and Z implies that all entropies appearing in the statement of the lemma are well deﬁned, see Fact 2.1 and Lemma 2.2. To see (i), let f

be the joint density of X and Y and deﬁne g and fy as in (20). Then H(X, Y ) = − log(f(x, y))f(x, y) dxdy

= − log(fy(x)g(y))fy(x)g(y) dxdy

= − log(fy(x))fy(x) dxg(y) dy − log(g(y))g(y) fy(x) dxdy

= H(X | Y ) + H(Y ).

Inequality (iii) is a direct consequence of (23) and (24) whereas (ii) follows immediately from (i) and (iii). To see (iv), let f be the joint density of X, Y , and Z, and let

g(y) := f(x, y, z) dxdz. It is not hard to see that

H(X | Y, Z) = H(X{Y=y} | Z{Y=y})g(y)dy

≤ H(X{Y=y})g(y)dy = H(X | Y ), where the inequality follows from (ii).

A powerful tool for comparing entropies is the following inequality originally proved by Shearer (see [10]) for Shannon’s entropy. As the literature usually deals with the discrete case, we provide a short proof based on the treatment in [3].

- Theorem 2.5 (Shearer’s inequality). Let X1, . . ., Xm be random variables with a joint density which is bounded and compactly supported. Let I ⊆ 2 m be a collection of subsets which r-covers the set m , i.e., has the property that for each i ∈ m ,


|{I ∈ I : i ∈ I}| = r. (25) Then

1 r I∈I

H({Xi : i ∈ I}). (26)

H(X1, . . ., Xm) ≤

![image 59](<2021-kozma-what-does-typical-metric_images/imageFile59.png>)

(since we did not preclude ∅ ∈ I , let us deﬁne that the entropy of an empty collection of random variables is zero).

Proof. We prove the statement by induction on r. The case r = 1 follows immediately from (iii) in Proposition 2.4. Suppose now that

- r > 1. If m ∈ I , then we easily obtain (26) invoking the inductive


assumption with I replaced by the (r−1)-cover I \{ m }. Otherwise, assume I1, I2 ∈ I satisfy that both I1 \ I2 and I2 \ I1 are non-empty. It follows from (iv) in Proposition 2.4 that

H(I1 \ I2 | I2) ≤ H(I1 \ I2 | I1 ∩ I2) (27)

where we denote H(I) as a short for H({Xi : i ∈ I}), and similarly for conditioned entropies. Consequently, by (i) in Proposition 2.4,

H(I1 ∪ I2) + H(I1 ∩ I2) (=i) H(I1 \ I2 | I2) + H(I2) + H(I1 ∩ I2)

(27)

≤ H(I1 \ I2 | I1 ∩ I2) + H(I2) + H(I1 ∩ I2) (=i) H(I1) + H(I2)

If we now replace I1 and I2 with I1∪I2 and I1∩I2, then I remains an rcover and the sum in the right-hand side of (26) can only decrease. It is clear that after a ﬁnite number of such modiﬁcations we will eventually arrive at the case when m ∈ I .

We remark that, due to the fact that diﬀerential entropy may be negative and unlike the Shannon entropy case (the entropy of discrete random variables), inequality (26) need not hold when the equals sign in the r-cover condition (25) is changed to a greater-or-equal sign.

- 2.5. A triangle inequality for the Kullback–Leibler divergence. The proof of Theorem 1.2 will require the following simple ‘triangle inequality’ for Kullback–Leibler divergences.


- Lemma 2.6. Suppose that X, Y , and Z are R-valued random variables with a joint distribution in A (R3). Then


DKL ((X, Y, Z) X × Y × Z)

≤ DKL ((X, Y, Z) X × (Y, Z)) + DKL ((X, Y, Z) (X, Y ) × Z). Proof. The deﬁnition of Kullback–Leibler divergence gives

DKL ((X, Y, Z) X × Y × Z)

= DKL ((X, Y, Z) X × (Y, Z)) + DKL ((Y, Z) Y × Z).

The second term in the right-hand side may be bounded from above, using (24) and Lemma 2.4 (iv), as follows:

DKL ((Y, Z) Y × Z) = H(Z) − H(Z | Y ) ≤ H(Z) − H(Z | X, Y )

= DKL ((X, Y, Z) (X, Y ) × Z).

- 2.6. Relations between entropy and independence. As explained above, a key step in our proof of Theorem 1.2 is showing that the indi-


vidual distances in a uniformly sampled metric space from Mn become almost independent random variables after we condition on the values

of some small fraction of all n2 distances. We shall establish this almost independence property by bounding the entropies of various vectors of

distances in the random metric space. The connection between almost independence and entropy will be provided by the following lemma, relating the Kullback–Leibler divergence of two measures with the difference of their supports. The lemma will be used to bound from above the error term in the upper bound on entropy given by Theorem 3.1, see Claim 4.4.

- Lemma 2.7. Let µ, ν be probability measures in A (Rk). Then DKL (µ ν) ≥ sup{ν(A) : A ⊆ Rk Borel satisfying µ(A) = 0}. (28)


Proof. Denote by f(x) the density of µ and by g(x) the density of ν. Let A ⊆ Rk be a Borel subset and suppose that µ(A) = 0. Recalling that log(y) ≥ 1 − y1 for all y > 0 we conclude that

![image 60](<2021-kozma-what-does-typical-metric_images/imageFile60.png>)

- f(x)

![image 61](<2021-kozma-what-does-typical-metric_images/imageFile61.png>)

- g(x)


- f(x)

![image 62](<2021-kozma-what-does-typical-metric_images/imageFile62.png>)

- g(x)


DKL (µ ν) = log

f(x) dx =

log

f(x) dx

Ac

g(x) f(x)

f(x) dx = 1 − ν(Ac) = ν(A).

≥

1 −

![image 63](<2021-kozma-what-does-typical-metric_images/imageFile63.png>)

Ac

Observe that the quantity in the right-hand side of (28) is a lower bound on the total variation distance between µ and ν. Therefore, it seems natural to relate it to the Kullback–Leibler divergence between µ and ν using Pinsker’s inequality [35], which states that2

DKL (µ ν) ≥ 2 (dTV(µ, ν))2 . (29)

This, in fact, was done in our proof of an earlier, weaker version of Theorem 1.2. While (29) is optimal for certain pairs of µ and ν, in our setting, the more specialised Lemma 2.7 yields much better dependence between the two quantities involved. Similar considerations are discussed in [15], which also uses a version of Lemma 2.7 in place of Pinsker’s inequality.

![image 64](<2021-kozma-what-does-typical-metric_images/imageFile64.png>)

2Originally, Pinsker proved (29) with the multiplicative constant 2 replaced by 1/(2 log2). The version stated in (29) was obtained somewhat later by Csisza´r [13], Kemperman [25], and Kullback [29].

3. Entropy-maximising product distributions

The ﬁrst part of this section is devoted to deriving an upper bound on the largest entropy of a vector of independent random variables that is almost supported in a given compact, convex subset P ⊆ Rd. It turns out that this largest entropy is close to the logarithm of the largest volume of a box that is fully contained in P. In a short, second part of the section, we compute this volume in the speciﬁc case that P is the (closure of the) 3-dimensional metric polytope M3. The results of this section are a central ingredient in the proof of the volume upper bound in Theorem 1.2.

- 3.1. Entropy-maximising product distributions on convex sets. The following theorem is the main result of this section.


- Theorem 3.1. Let M > 0 and let P ⊆ [−M, M]d, d ≥ 2, be a closed,


convex set with non-empty interior. Let V0 be the maximal volume of an axis-parallel box fully contained in P, that is,

V0 := max

d

(bi − ai) : [a1, b1] × · · · × [ad, bd] ⊆ P . (30)

i=1

There exists a ﬁnite C = C(M, P) such that the following holds. Suppose X1, . . ., Xd are independent random variables with bounded densities supported in [−M, M]. Then

d

H(Xi) ≤ log(V0) + C · P (X1, . . ., Xd) ∈/ P 1/d.

H(X1, . . ., Xd) =

i=1

Let us comment on the assumptions and the conclusion of the theorem. First, since we will only use this result for a very speciﬁc P (the closure of the 3-dimensional metric polytope M3), we do not need the exact dependence of C on P, but let us nonetheless note that C depends only on d, M, and V0.

The assumption d ≥ 2 is required for the conclusion. Indeed, when d = 1, there exist examples where the error term has an additional logarithmic factor (see (38) below for a complementary upper bound). To see this, consider P = [0, 1] ⊆ [−2, 2] and let X1 be a random variable that, with probability 1 − ε, is uniform on P and, with probability ε, is uniform on [1, 2]. Here, P(X1 ∈/ P) = ε whereas H(X1) = (1 − ε) log(1/(1 − ε)) + ε log(1/ε) ≥ log(V0) + ε log(1/ε).

Aside from the constant factor C, the dependence of the error term on P (X1, . . ., Xd) ∈/ P is optimal. To see this, consider the simplex

P := (x1, . . ., xd) ∈ [0, d]d : x1 + · · · + xd ≤ d ⊆ [−d, d]d. The AM–GM inequality implies that [0, 1]d is the largest box contained in P and thus log(V0) = 0. Let X1, . . ., Xd be i.i.d. random variables distributed uniformly on the interval [0, 1 + δ], for some δ ≤ 1/d. On the one hand, we have

|Xi| > 1 − (d − 1)δ ≤ (dδ)d. On the other hand,

P (X1, . . ., Xd) ∈/ P ≤ P min

i

H(X1, . . ., Xd) = d · H(X1) = d log(1 + δ) ≥ dδ/2. Thus, H(X1, . . ., Xd) ≥ log(V0) + P (X1, . . ., Xd) ∈/ P 1/d/2.

The ﬁrst step in our proof of Theorem 3.1 is Lemma 3.2, below. The lemma supplies an axis-parallel box fully contained in P that supports most of the distribution of the vector (X1, . . ., Xd). The existence of such a box already implies an upper bound on H(X1, . . ., Xd) that differs from the one stated in Theorem 3.1 by an extra logarithmic factor in the error term (see (38)). The proof of the lemma is short; following it, the bulk of the proof of Theorem 3.1 is devoted to removing this superﬂuous logarithmic term. (If one substitutes the bound (38) for Theorem 3.1 in the argument presented in Section 4.3, one obtains the following weaker version of the upper bound in Theorem 1.2: Vol(Mn) ≤ exp C(nlog n)3/2 .)

The second step in the proof of Theorem 3.1 is Proposition 3.3, below. The proposition (combined with Lemma 3.2) may be regarded as a strengthening of the conclusion of the theorem. The extra information it provides will be used in our analysis of the minimum distance in a typical sample from the metric polytope (Theorem 1.3).

We start the proof of Theorem 3.1 with several deﬁnitions that we will use throughout.

Let M > 0 and ﬁx a closed convex set P ⊆ [−M, M]d with nonempty interior. At this point the dimension is allowed to be any d ≥ 1 but the restriction d ≥ 2 will be placed in Proposition 3.3. Write V0 for the maximal volume of an axis-parallel box fully contained in P, deﬁned formally in (30). Our assumptions on P imply that V0 > 0. Let X1, . . ., Xd be independent random variables with bounded densities supported in [−M, M]. Deﬁne

ε := P (X1, . . ., Xd) ∈/ P 1/d, (31)

so that our goal is to show that, for a ﬁnite C = C(M, P),

H(X1, . . ., Xd) =

d

H(Xi) ≤ log(V0) + Cε. (32)

i=1

We may (and will) assume without loss of generality that ε ≤ 61, as otherwise the statement follows by taking C = 6(d log(2M)−log(V0)) ≥ 0 (as H(Xi) ≤ log(2M) by Lemma 2.2 and V0 ≤ (2M)d).

![image 65](<2021-kozma-what-does-typical-metric_images/imageFile65.png>)

For each i ∈ d , deﬁne the upper and lower ε-quantiles of the distribution of Xi,

so that

ai := sup{a ∈ R : P(Xi < a) ≤ ε}, bi := inf{b ∈ R : P(Xi > b) ≤ ε},

(33)

P Xi ≤ ai = P Xi ≥ bi = ε. (34) In particular, the interval [ai, bi] is nonempty by our assumption that ε ≤ 61. Denote the volume spanned by these intervals by

![image 66](<2021-kozma-what-does-typical-metric_images/imageFile66.png>)

d

V := Vol [a1, b1] × · · · × [ad, bd] =

(bi − ai). (35)

i=1

Finally, writing fi for the density of Xi, let H(Xi; A) := −

fi(x) log(fi(x))dx (36)

A

be the contribution to the diﬀerential entropy of Xi from the measurable set A.

Our ﬁrst lemma shows that the box spanned by the intervals ([ai, bi]) is fully contained in P.

- Lemma 3.2. In every dimension d ≥ 1, [a1, b1] × · · · × [ad, bd] ⊆ P. (37)


In particular, V ≤ V0.

Proof. Suppose, to obtain a contradiction, that (37) fails. Hence, as P is closed, there exists (x1, . . ., xd) ∈/ P with ai < xi < bi for all i. This implies, as P is convex, that there is a choice of signs (s1, . . ., sd) ∈ {−1, 1}d so that the orthant

O := (y1, . . ., yd) : si(yi − xi) ≥ 0 for all i ∈ d

does not intersect P. In particular, εd = P (X1, . . ., Xd) ∈/ P ≥ P (X1, . . ., Xd) ∈ O ≥

d

min{P(Xi ≤ xi), P(Xi ≥ xi)}

i=1

d

min{P(Xi ≤ ai), P(Xi ≥ bi)} = εd,

>

i=1

where the strict inequality uses that ai < xi < bi and the deﬁnition (33). This contradiction shows that (37) must in fact hold.

The volume statement is now deduced from the deﬁnition of V0. We digress from the proof of Theorem 3.1 to note that Lemma 3.2

implies the following version of the theorem, which holds in every dimension d ≥ 1 but has an extra logarithmic factor in the error term,

d

H(Xi) ≤ log(V0) + Cε log(2/ε) (38)

i=1

with ε as in (31) and C = C(d, M, V0) ﬁnite. The case ε > 61 is handled directly as before. For ε ≤ 16, note ﬁrst that, for some C′ = C′(d, M),

![image 67](<2021-kozma-what-does-typical-metric_images/imageFile67.png>)

![image 68](<2021-kozma-what-does-typical-metric_images/imageFile68.png>)

d

H(Xi) ≤ (1 − 2ε) log(V ) + C′ε log(2/ε) (39)

i=1

Indeed, for each i ∈ d , by (34) and Lemma 2.3, H(Xi) = H(Xi; [−M, M] \ [ai, bi]) + H(Xi; [ai, bi]) ≤ 2ε log

2M − (bi − ai) 2ε

bi − ai 1 − 2ε

+ (1 − 2ε) log

![image 69](<2021-kozma-what-does-typical-metric_images/imageFile69.png>)

![image 70](<2021-kozma-what-does-typical-metric_images/imageFile70.png>)

M ε

1 1 − 2ε

≤ (1 − 2ε) log(bi − ai) + 2ε log

+ (1 − 2ε) log

![image 71](<2021-kozma-what-does-typical-metric_images/imageFile71.png>)

![image 72](<2021-kozma-what-does-typical-metric_images/imageFile72.png>)

and the bound (39) follows by summing this estimate over all i. To deduce (38), replace V by V0 using Lemma 3.2 and absorb the factor 2ε log(V0) in the error term.

We return to the proof of Theorem 3.1 and will show the following key proposition.

Proposition 3.3. In dimensions d ≥ 2, there exists a ﬁnite C = C(M, P) such that

d

- 1

![image 73](<2021-kozma-what-does-typical-metric_images/imageFile73.png>)

- 2


H(Xi) ≤

i=1

log(V0) +

d

H(Xi; [ai, bi]) + Cε.

i=1

It will be convenient to denote by c and C ﬁnite positive constants which depend only on d, M, and V0. These constants, and their numbered versions, may change from line to line.

Let us see how Proposition 3.3 and Lemma 3.2 imply Theorem 3.1. Combining the proposition with Lemma 2.3, recalling (34), (35), and our assumption that ε ≤ 61, and applying Lemma 3.2 we have

![image 74](<2021-kozma-what-does-typical-metric_images/imageFile74.png>)

d

bi − ai 1 − 2ε

- 1

![image 75](<2021-kozma-what-does-typical-metric_images/imageFile75.png>)

- 2


log(V0) + (1 − 2ε)

H(X1, . . ., Xd) ≤

log

+ Cε

![image 76](<2021-kozma-what-does-typical-metric_images/imageFile76.png>)

i=1

- 1

![image 77](<2021-kozma-what-does-typical-metric_images/imageFile77.png>)

- 2


log(V0) + (1 − 2ε) log(V ) + Cε ≤ log(V0) + Cε.

≤

Proof of Proposition 3.3. There are three constants in the proof that deserve their own letters, β, µ, and K, also depending only on d, M, and V0. We will not specify these explicitly, and only point out here that we ﬁrst choose β (small), then µ (even smaller), and then K (very large). In symbols (treating d, M, and V0 as constants),

K−1 ≪ µ ≪ β ≪ 1. Let us introduce the following quantity,

Kε2 s

t := sup s > 0 : ∃i max{P(Xi ≤ ai − s), P(Xi ≥ bi + s)} ≥

![image 78](<2021-kozma-what-does-typical-metric_images/imageFile78.png>)

where we set t = 0 if the above set is empty. As each Xi is supported on [−M, M], we have t ≤ 2M. On the other hand, by the deﬁnition of ai and bi, see (34), either t = 0 or t ≥ Kε.

The proposition is obtained by summing the following inequalities:

d

- 1

![image 79](<2021-kozma-what-does-typical-metric_images/imageFile79.png>)

- 2


H(Xi; [ai − t, ai] ∪ [bi, bi + t]) +

Mt :=

H(Xi; [ai, bi])

i=1

- 1

![image 80](<2021-kozma-what-does-typical-metric_images/imageFile80.png>)

- 2


≤

log(V0) + Cε. (40) and, for each i ∈ d ,

H(Xi; R \ [ai − t, bi + t]) ≤ Cε. (41)

We ﬁrst prove (41). For each k ≥ 1, let λk be the Lebesgue measure of the set

{x ∈/ [ai − t, bi + t] : e−k ≤ fi(x) ≤ e−k+1} and note that, as −y log y < 0 for y > 1,

∞

ke−k+1λk.

H(Xi; R \ [ai − t, bi + t]) ≤

k=1

For every k ≥ 1, λk ≤ 2εk2 + ek · P(Xi ≤ ai − t − εk2) + P(Xi ≥ bi + t + εk2)

2Kε2 t + εk2 ≤ 2k2 +

2Kek

(∗)

≤ 2εk2 + ek ·

k2 · ε where (∗) follows from the deﬁnition of t. Hence

![image 81](<2021-kozma-what-does-typical-metric_images/imageFile81.png>)

![image 82](<2021-kozma-what-does-typical-metric_images/imageFile82.png>)

∞

∞

∞

2k3 ek−1 +

2eK

ke−k+1λk ≤

k2 · ε ≤ Cε, which proves (41).

![image 83](<2021-kozma-what-does-typical-metric_images/imageFile83.png>)

![image 84](<2021-kozma-what-does-typical-metric_images/imageFile84.png>)

k=1

k=1

k=1

It remains to argue that (40) holds as well. For this we apply

- Lemma 2.3 and get for each i (using also log y ≤ y − 1 for y > 0),


bi − ai 1 − 2ε

H(Xi; [ai, bi]) ≤ (1 − 2ε) log

![image 85](<2021-kozma-what-does-typical-metric_images/imageFile85.png>)

(42)

≤ (1 − 2ε) log(bi − ai) + 2ε

and, if t > 0,

H(Xi; [ai − t, ai] ∪ [bi, bi + t]) ≤ 2ε log

t ε

![image 86](<2021-kozma-what-does-typical-metric_images/imageFile86.png>)

, (43)

where we used the fact that t ≥ Kε ≥ eε, which implies that the function δ  → δ log(t/δ) is increasing for δ ∈ [0, ε]. We split the remainder of the argument into two cases, depending on how close V , the volume of [a1, b1] × · · · × [ad, bd], is to V0.

- Case 1. We ﬁrst assume that log(V ) ≤ log(V0) − βt. (44)


In this case, summing (43) and half of (42) over all i gives

Mt ≤

≤

≤

d

- 1

![image 87](<2021-kozma-what-does-typical-metric_images/imageFile87.png>)

- 2


(1 − 2ε)

log(bi − ai) + dε + 2dε log

i=1

- 1

![image 88](<2021-kozma-what-does-typical-metric_images/imageFile88.png>)

- 2


(1 − 2ε) (log(V0) − βt) + dε + 2dε log

- 1

![image 89](<2021-kozma-what-does-typical-metric_images/imageFile89.png>)

- 2


t ε · {t>0} −

log(V0) + d + 2d log

![image 90](<2021-kozma-what-does-typical-metric_images/imageFile90.png>)

![image 91](<2021-kozma-what-does-typical-metric_images/imageFile91.png>)

t ε · {t>0}

![image 92](<2021-kozma-what-does-typical-metric_images/imageFile92.png>)

t ε · {t>0}

![image 93](<2021-kozma-what-does-typical-metric_images/imageFile93.png>)

t ε − log(V0) · ε.

β 4 ·

![image 94](<2021-kozma-what-does-typical-metric_images/imageFile94.png>)

The claimed estimate (40) now follows as, for every c > 0, the function y  → log(y) − cy is bounded from above.

- Case 2. Assume now that (44) does not hold. This means, in particular, that t > 0 (due to Lemma 3.2). Since our variables are continuous,


Kε2 t for some index i. By permuting and reﬂecting the coordinates, if necessary, we may assume that

max{P(Xi ≤ ai − t), P(Xi ≥ bi + t)} =

![image 95](<2021-kozma-what-does-typical-metric_images/imageFile95.png>)

P(X1 ≤ a1 − t) = Kε2/t. (45) We claim that

[a1 − t, b1] ×

d

[ai + µt, bi − µt] P. (46)

i=2

Indeed, if this were not true, then

b1 − a1 + t b1 − a1

log(V0)−log(V ) ≥ log

![image 96](<2021-kozma-what-does-typical-metric_images/imageFile96.png>)

Since (44) does not hold, we have

d

+

log

i=2

bi − ai − 2µt bi − ai

![image 97](<2021-kozma-what-does-typical-metric_images/imageFile97.png>)

. (47)

e−βt · V0 (2M)d−1 ≥

V (2M)d−1 ≥

V0 (2M)d

(bi − ai) ≥

min

,

![image 98](<2021-kozma-what-does-typical-metric_images/imageFile98.png>)

![image 99](<2021-kozma-what-does-typical-metric_images/imageFile99.png>)

![image 100](<2021-kozma-what-does-typical-metric_images/imageFile100.png>)

i

where the last inequality holds as t ≤ 2M and β is small. It follows that the ﬁrst term in the right-hand side of (47) is at least c1t, for some positive constant c1 = c1(d, M, V0) (independent of β as long as β is small), and, if µ is suﬃciently small, each of the d − 1 summands is at least −C1µt, for some positive constant C1 = C1(d, M, V0). In particular, if β and µ are suﬃciently small, then the right-hand side of (47) is larger than βt, contradicting our assumption.

Let x be some point demonstrating (46), namely

x ∈ [a1 − t, b1] ×

d

[ai + µt, bi − µt] \ P,

i=2

and notice that x1 ∈ [a1 − t, a1), as i[ai, bi] ⊆ P by Lemma 3.2. Since P is convex there is a hyperplane separating x from P, that is,

a vector v such that

∀y ∈ P v, x < v, y . (48)

First, let us apply (48) to y = (a1, x2, . . ., xd), which we may since xi ∈ [ai, bi] for all i ≥ 2. We get v1(a1 − x1) > 0, so v1 > 0 and we may normalise v to assume v1 = 1. Moreover, by permuting the coordinates, if necessary, we may assume that vi ≥ 0 for i ∈ {2, . . ., j} and vi < 0 for i ∈ {j + 1, . . ., d}. We may also assume that j ≥ 2, the complementary case j + 1 = 2 being essentially identical. (Note that we do use the assumption that d ≥ 2 here.) These assumptions imply that

j

d

(−∞, ai] ×

[bi, ∞)

(−∞, a1 − t] × (−∞, a2 + µt] ×

i=3

i=j+1

is disjoint from P. Indeed, if z is an arbitrary point in this orthant, we have vizi ≤ vixi for each i and hence v, z < v, y for all y ∈ P. It follows that

P(X1 ≤ a1 − t) · P(a2 ≤ X2 ≤ a2 + µt) ·

j

P(Xi ≤ ai) ·

i=3

d

P(Xi ≥ bi) ≤ εd,

i=j+1

and therefore, as P(Xi ≤ ai) = P(Xi ≥ bi) = ε, P(a2 ≤ X2 ≤ a2 + µt) ≤

ε2 P(X1 ≤ a1 − t)

t K

(=45)

.

![image 101](<2021-kozma-what-does-typical-metric_images/imageFile101.png>)

![image 102](<2021-kozma-what-does-typical-metric_images/imageFile102.png>)

Thus we have shown some inhomogeneity in the distribution of X2. If we require K > 10(b2−a2)/µ(1−2ε), then this inhomogeneity is strong enough to apply (18) in Lemma 2.3, so let us make this requirement. We get

1 − 2ε 4 ·

b2 − a2 1 − 2ε −

µt b2 − a2 ≤ (1 − 2ε) log(b2 − a2) + 2ε −

H(X2; [a2, b2]) ≤ (1 − 2ε) log

![image 103](<2021-kozma-what-does-typical-metric_images/imageFile103.png>)

![image 104](<2021-kozma-what-does-typical-metric_images/imageFile104.png>)

![image 105](<2021-kozma-what-does-typical-metric_images/imageFile105.png>)

µ 20M · t. (49)

![image 106](<2021-kozma-what-does-typical-metric_images/imageFile106.png>)

Summing (43) and half of (42) over all i, as in Case 1, but using the improved estimate (49) in place of (42) when i = 2 yields

µ 40M · t. A calculation similar to the one done in Case 1, using that V ≤ V0 by

- 1

![image 107](<2021-kozma-what-does-typical-metric_images/imageFile107.png>)

- 2


t ε −

Mt ≤

(1 − 2ε) log(V ) + dε + 2dε log

![image 108](<2021-kozma-what-does-typical-metric_images/imageFile108.png>)

![image 109](<2021-kozma-what-does-typical-metric_images/imageFile109.png>)

- Lemma 3.2, yields the upper bound (40) on Mt. This completes the proof of the proposition (and hence also of Theorem 3.1).

- 3.2. The largest box in M3. Theorem 3.1 will be applied to the (closure of the) 3-dimensional metric polytope. To this end, we study here the largest box contained in M3.


- Lemma 3.4. Suppose that P is an axis-parallel box contained in the closure of the metric polytope M3, that is,


) ∼= R3. Then

P = [a1, b1] × [a2, b2] × [a3, b3] ⊆ M3 ⊆ R(

3 2

![image 110](<2021-kozma-what-does-typical-metric_images/imageFile110.png>)

Vol(P) ≤ 1 (50)

and equality holds if and only if [ai, bi] = [1, 2] for each i ∈ {1, 2, 3}. Furthermore, for some absolute constant C,

3

i=1

|ai − 1| + |bi − 2| ≤ C(1 − Vol(P)).

The furthermore clause is not required for our analysis of the volume of the metric polytope (Theorem 1.2) but will be used in analysing the typical minimum distance (Theorem 1.3).

The following proof was suggested to us by Shoni Gilboa; it replaced our previous, less transparent argument.

![image 111](<2021-kozma-what-does-typical-metric_images/imageFile111.png>)

- Proof of Lemma 3.4. Our assumption that P ⊆ M3 implies that b1 ≤ a2 + a3 and, similarly, b2 ≤ a1 + a3 and b3 ≤ a1 + a2. Summing these three inequalities yields


b1 + b2 + b3 ≤ 2(a1 + a2 + a3). (51) Consequently, by the AM–GM inequality,

3

3

3

3

bi − ai 3

b1 + b2 + b3 6

(bi − ai) ≤

≤

≤ 1, (52)

Vol(P) =

![image 112](<2021-kozma-what-does-typical-metric_images/imageFile112.png>)

![image 113](<2021-kozma-what-does-typical-metric_images/imageFile113.png>)

i=1

i=1

where the second inequality is precisely (51) and the last inequality holds by our assumption that P ⊆ M3 ⊆ [0, 2]3, which ensures that b1, b2, b3 ≤ 2.

![image 114](<2021-kozma-what-does-typical-metric_images/imageFile114.png>)

For the second and third assertions of the lemma, suppose that Vol(P) ≥ 1 − ε for some ε ≥ 0. Inequality (52) implies that

3

b1 + b2 + b3 2 ≥

(bi − ai) ≥ 3(1 − ε)1/3 ≥ 3(1 − ε) (53)

![image 115](<2021-kozma-what-does-typical-metric_images/imageFile115.png>)

i=1

and, consequently, as maxi bi ≤ 2, that mini bi ≥ 2 − 6ε. Moreover, summing the inequalities a1 + a2 ≥ b3 and a1 + a3 ≥ b2, we obtain

3

a1 ≥ b2 + b3 − (a1 + a2 + a3) =

(bi − ai) − b1 ≥ 1 − 3ε,

i=1

where the last inequality follows from (53) and the assumption b1 ≤ 2. By symmetry, mini ai ≥ 1 − 3ε. Using again (53), we have

3

3(1 − ε) ≤

(bi − ai) ≤ 6 − 2 min

ai − a1,

i

i=1

giving a1 ≤ 1 + 9ε. By symmetry, maxi ai ≤ 1 + 9ε. Hence

3

3

|ai − 1| + |bi − 2| ≤

9ε + 6ε = 45ε,

i=1

i=1

as needed.

4. Estimating the volume of the metric polytope

In this section, we prove Proposition 1.1 and Theorem 1.2. The proof of Proposition 1.1 is a short application of Shearer’s inequality (Theorem 2.5) and is presented in Section 4.1. The lower bound on the volume of Mn is obtained via the Local Lemma of Erd˝os and Lova´sz [18]; it is presented in Section 4.2. The proof of the upper bound on the volume, whose outline is given in the introduction, is presented in Section 4.3.

- 4.1. Monotonicity. In this section, we prove Proposition 1.1. Recall


n 2

) is non-increasing. We will show that this fact is a simple consequence of Shearer’s inequality (Theorem 2.5). Alternatively, one can derive it from a generalisation of the Loomis–Whitney inequality [30] due to Bollob´s and Thomason [9].

that said proposition states that the sequence n  → Vol(Mn)1/(

Proof of Proposition 1.1. Let n ≥ 2 and let d be a uniformly sampled metric space in Mn+1. By Lemma 2.2,

H(d) = log (Vol(Mn+1)) . (54)

For each i ∈ n + 1 , let Ji := n + 1 \ {i} and let Ii be the set of all unordered pairs of distinct elements in Ji. Observe that, for each {j, k} ∈ n+1 2 , we have

|{i ∈ n + 1 : {j, k} ∈ Ii}| = n − 1.

Since d may be naturally viewed as a random vector of distances, Shearer’s inequality (Theorem 2.5) implies that

n+1

1 n − 1

H {djk : {j, k} ∈ Ii} . (55)

H(d) ≤

![image 116](<2021-kozma-what-does-typical-metric_images/imageFile116.png>)

i=1

Finally, observe that for each i ∈ n + 1 , the restriction of d to the pairs in Ii is a metric space on n points that belongs to Mn. Thus, by Lemma 2.2,

H {djk : {j, k} ∈ Ii} ≤ log(Vol(Mn)) (56) Putting together (54), (55), and (56), we conclude that

n + 1 n − 1

log(Vol(Mn+1)) ≤

log(Vol(Mn)). Since this inequality holds for any n ≥ 2 and (n + 1)/(n − 1) =

![image 117](<2021-kozma-what-does-typical-metric_images/imageFile117.png>)

n 2

) is nonincreasing, as claimed.

2 / n2 , we conclude that the sequence n  → Vol(Mn)1/(

n+1

- 4.2. Lower bound. In this section, we prove the lower bound on


Vol(Mn) from Theorem 1.2. Recall that it was Vol(Mn) ≥ exp((1/6 + o(1))n3/2). The proof below, which uses the Local Lemma of Erd˝os and Lova´sz [18], is due to Dor Elboim (our original argument, based on Harris’s inequality [22], gave 1/24 instead of 1/6).

We may and will assume that n is suﬃciently large. Let δ = 1/(2√n)

![image 118](<2021-kozma-what-does-typical-metric_images/imageFile118.png>)

and let (dij), {i, j} ∈ n 2 , be an array of independent and identically distributed random variables, each uniform on the interval [1 − δ, 2].

Deﬁne the event

G := {(dij) ∈ Mn}. Observe that, by deﬁnition,

n 2

)

(

- 1

![image 119](<2021-kozma-what-does-typical-metric_images/imageFile119.png>)

- 2√n


n 2

) P(G) = 1 +

Vol(Mn) ≥ (1 + δ)(

P(G). (57) We shall derive a lower bound on P(G) from the Local Lemma.

![image 120](<2021-kozma-what-does-typical-metric_images/imageFile120.png>)

- Lemma 4.1 ([3, Lemma 5.1.1]). Let Bv, v ∈ V , be events in an arbitrary probability space. Suppose that there is an integer k such that,


for each v ∈ V , there is a set Dv ⊆ V \ {v} with at most k elements such that Bv is mutually independent of all the events Bw with w ∈ V \ (Dv ∪ {v}). If a real p ∈ [0, 1] satisﬁes P(Bv) ≤ p(1 − p)k for each v ∈ V , then

Bvc ≥ (1 − p)|V|.

P

v∈V

For a triple of distinct indices {i, j, k} ∈ n 3 , let Bijk denote the event that (dij, dik, djk) is not in M3, that is, one of the three triangle inequalities is violated. Observe that

3 1 + δ

P(Bijk) = 3P(dij + djk < dik) =

![image 121](<2021-kozma-what-does-typical-metric_images/imageFile121.png>)

2δ

(2δ − x)2 2

3 (1 + δ)3

dx =

=

![image 122](<2021-kozma-what-does-typical-metric_images/imageFile122.png>)

![image 123](<2021-kozma-what-does-typical-metric_images/imageFile123.png>)

0

2δ

P(dij + djk < 2 − x) dx

0

4δ3 (1 + δ)3

.

![image 124](<2021-kozma-what-does-typical-metric_images/imageFile124.png>)

Since the event Bijk is mutually independent of all events Bi′j′k′ such that |{i, j, k} ∩ {i′, j′, k′}| ≤ 1, we may invoke Lemma 4.1 to conclude that, for every p satisfying

4δ3

(1 + δ)3 ≤ p(1 − p)3(n−3), (58) we have

![image 125](<2021-kozma-what-does-typical-metric_images/imageFile125.png>)

n 3

Bijkc ≥ (1 − p)(

). (59)

P(G) = P

n 3

)

{i,j,k}∈(

It is easy to see that if p = an−3/2 for some constant a > 1/2, then (58) is satisﬁed for all suﬃciently large n. In particular, (57) and (59) imply that, for each a > 1/2,

- 1

![image 126](<2021-kozma-what-does-typical-metric_images/imageFile126.png>)

- 2√n


Vol(Mn) ≥ 1 +

![image 127](<2021-kozma-what-does-typical-metric_images/imageFile127.png>)

1 4 −

= exp

![image 128](<2021-kozma-what-does-typical-metric_images/imageFile128.png>)

n 2

)

(

n 3

)

(

a n3/2

1 −

![image 129](<2021-kozma-what-does-typical-metric_images/imageFile129.png>)

a 6

+ o(1) n3/2 .

![image 130](<2021-kozma-what-does-typical-metric_images/imageFile130.png>)

Since a was an arbitrary constant greater than 1/2, this yields the lower bound in (6).

- 4.3. Upper bound. In this section, we deduce the upper bound on


Vol(Mn) stated in Theorem 1.2 from the entropy estimate of Theorem 3.1.

Let n ≥ 3 and let d be a uniformly sampled metric space in Mn, which we view as a vector in R(

n 2

). By Lemma 2.2,

log(Vol(Mn)) = H(d). For each m ∈ {0, . . ., n − 1}, let us denote by Fm the set of all pairs ij ∈ n 2 with max{i, j} > n − m, that is,

n − m 2

n 2 \

(60) and set, for m ≤ n − 2,

Fm :=

hm := H(d12 | (de)e∈F

), (61) where h0 = H(d12). Observe that, by symmetry, hm = H(dij|(de)e∈F

m

)

m

for every ij ∈ n− 2m . Since d12 ∈ [0, 2], then h0 ≤ log 2, by Lemma 2.2. Since Fm ⊆ Fm+1 for every m, it follows from Lemma 2.4 (iv) that

hn−2 ≤ · · · ≤ h1 ≤ h0 ≤ log 2. (62) Additionally, as F0 = ∅ and Fn−1 = n 2 , Lemma 2.4 (i) and (iii) give

n−2

m+1\Fm | (df)f∈F

H (de)e∈(

) =

H (de)e∈F

n 2

m

m=0

n−2

H (de | (df)f∈F

≤

)

m

m=0 e∈Fm+1\Fm

n−2

n−2

(n − m − 1) · hm. (63) In particular, it suﬃces to prove the following estimate.

|Fm+1 \ Fm| · hm =

=

m=0

m=0

- Lemma 4.2. There exists a K > 0 such that, for all m ∈ {0, . . ., n−2},


K √m + 1

hm ≤

.

![image 131](<2021-kozma-what-does-typical-metric_images/imageFile131.png>)

![image 132](<2021-kozma-what-does-typical-metric_images/imageFile132.png>)

Indeed, substituting this bound into (63) gives

n−1

log(Vol(Mn)) = H(d) ≤ K

m=1

n − m √m ≤ Cn3/2

![image 133](<2021-kozma-what-does-typical-metric_images/imageFile133.png>)

![image 134](<2021-kozma-what-does-typical-metric_images/imageFile134.png>)

for some absolute constant C > 0, establishing the theorem.

- Lemma 4.2 is a fairly simple consequence of the monotonicity of the


sequence (hm) and the following estimate, which lies at the heart of the matter.

- Lemma 4.3. There exists a C > 0 such that, for all m ∈ {0, . . ., n−3}, hm ≤ C (hm − hm+1)1/3 .


Proof. Fix an m ∈ {0, . . ., n − 3}. Since {1, n − m}, {2, n − m} ∈ Fm+1 \ Fm, Lemma 2.4 (iv) implies that

, d1,n−m, d2,n−m) ≤ hm.

hm+1 ≤ H(d12 | (de)e∈F

m

By symmetry, we may replace n − m in the above inequality with any element of {3, . . ., n − m}. In particular,

, d13, d23) ≥ hm+1 and thus,

H(d12 | (de)e∈F

m

, d13, d23) ≤ hm − hm+1. (64)

) − H(d12 | (de)e∈F

H(d12 | (de)e∈F

m

m

Condition on all the distances dij with ij ∈ Fm and denote by (X1, X2, X3) the random vector whose distribution is the conditioned distribution of (d12, d13, d23), so that

) = E[H(X1)] = E[H(X2)] = E[H(X3)].

hm = H(d12 | (de)e∈F

m

We write X1×X2×X3 to denote the random variable whose distribution is the product of the marginal distributions of X1, X2, and X3.

Claim 4.4. We have E P(X1 × X2 × X3 ∈/ M3) ≤ 2(hm − hm+1). Proof of Claim 4.4. By (24), inequality (64) is equivalent to

![image 135](<2021-kozma-what-does-typical-metric_images/imageFile135.png>)

E DKL ((X1, X2, X3) X1 × (X2, X3)) ≤ hm − hm+1. (65) By symmetry, inequality (64) continues to hold for any permutation of (d12, d13, d23) and hence (65) continues to hold for any permutation of (X1, X2, X3). It thus follows from Lemma 2.6 that

E DKL ((X1, X2, X3) X1 × X2 × X3) ≤ 2(hm − hm+1). (66)

![image 136](<2021-kozma-what-does-typical-metric_images/imageFile136.png>)

Since (X1, X2, X3) ∈ M3 with probability one, Claim 4.4 now follows from (66) and Lemma 2.7.

We may now apply Theorem 3.1 (to the distribution of X1×X2×X3) to bound the entropies of X1, X2, and X3. Lemma 3.4 states that the largest volume of an axis-parallel box contained in M3 is one and thus, by Theorem 3.1,

![image 137](<2021-kozma-what-does-typical-metric_images/imageFile137.png>)

H(X1) + H(X2) + H(X3) ≤ C · P(X1 × X2 × X3 ∈/ M3)1/3.

![image 138](<2021-kozma-what-does-typical-metric_images/imageFile138.png>)

By Jensen’s inequality (applied to the concave function x  → x1/3) and Claim 4.4,

3hm = E H(X1) + H(X2) + H(X3) ≤ C · 2(hm − hm+1) 1/3, as we wanted to prove.

- Proof of Lemma 4.2. Let K be a suﬃciently large absolute constant,


to be ﬁxed later. If hm ≤ √mK+1 for all m then there is nothing to prove. Otherwise, aiming to obtain a contradiction, deﬁne

![image 139](<2021-kozma-what-does-typical-metric_images/imageFile139.png>)

![image 140](<2021-kozma-what-does-typical-metric_images/imageFile140.png>)

K √m + 1

m0 := min m : 0 ≤ m ≤ n − 2 and hm >

![image 141](<2021-kozma-what-does-typical-metric_images/imageFile141.png>)

![image 142](<2021-kozma-what-does-typical-metric_images/imageFile142.png>)

.

Taking K ≥ log 2 we necessarily have m0 ≥ 1 by (62). It follows from

- Lemma 4.3 and the deﬁnition of m0 that


)1/3 ≤ C

0−1 ≤ C (hm

0−1 − hm

hm

0

K √m0 + 1

K √m0 −

![image 143](<2021-kozma-what-does-typical-metric_images/imageFile143.png>)

![image 144](<2021-kozma-what-does-typical-metric_images/imageFile144.png>)

![image 145](<2021-kozma-what-does-typical-metric_images/imageFile145.png>)

![image 146](<2021-kozma-what-does-typical-metric_images/imageFile146.png>)

1/3

.

As √1x−√x1+1 ≤ 2x13/2

for all x > 0, we may continue the above inequality to obtain

![image 147](<2021-kozma-what-does-typical-metric_images/imageFile147.png>)

![image 148](<2021-kozma-what-does-typical-metric_images/imageFile148.png>)

![image 149](<2021-kozma-what-does-typical-metric_images/imageFile149.png>)

![image 150](<2021-kozma-what-does-typical-metric_images/imageFile150.png>)

![image 151](<2021-kozma-what-does-typical-metric_images/imageFile151.png>)

CK1/3 21/3√m0 ≤

K √m0 + 1 if only K is suﬃciently large compared with C. Fix K to satisfy this condition. This contradicts the deﬁnition of m0 as hm

0−1 ≤

hm

![image 152](<2021-kozma-what-does-typical-metric_images/imageFile152.png>)

![image 153](<2021-kozma-what-does-typical-metric_images/imageFile153.png>)

![image 154](<2021-kozma-what-does-typical-metric_images/imageFile154.png>)

![image 155](<2021-kozma-what-does-typical-metric_images/imageFile155.png>)

0 ≤ hm

0−1 by (62). This ﬁnishes the proof of Lemma 4.2, and thus also of Theorem 1.2.

- 4.4. The lower tail of a typical distance. The proof of Theorem 1.3, presented in Section 5 below, uses as input an upper bound on P(d12 < 1) where, as before, (dij) denotes a uniformly chosen metric space in Mn. We record this in the following result, which further points out a nearly-matching lower bound.


- Proposition 4.5. There are absolute constants C, c > 0 such that c


C √n

√nlog(n + 1) ≤ P(d12 < 1) ≤

.

![image 156](<2021-kozma-what-does-typical-metric_images/imageFile156.png>)

![image 157](<2021-kozma-what-does-typical-metric_images/imageFile157.png>)

![image 158](<2021-kozma-what-does-typical-metric_images/imageFile158.png>)

![image 159](<2021-kozma-what-does-typical-metric_images/imageFile159.png>)

We continue to use the notation H(X; A) := − A f(x) log(f(x))dx for a random variable X with bounded and compactly-supported density f and measurable A.

The lower bound in Proposition 4.5 is a simple consequence of the volume lower bound in Theorem 1.2. To see this, assume, to reach a

contradiction, that the lower bound does not hold. Then, by Lemma 2.3 and the fact that log y ≤ y − 1 for all y > 0,

H(d12) = H(d12; [0, 1)) + H(d12; [1, 2]) ≤ P(d12 < 1) log

1 P(d12 < 1)

1 P(d12 ≥ 1) ≤ P(d12 < 1) log

+ P(d12 ≥ 1) log

![image 160](<2021-kozma-what-does-typical-metric_images/imageFile160.png>)

![image 161](<2021-kozma-what-does-typical-metric_images/imageFile161.png>)

1 P(d12 < 1)

+ 1 − P(d12 ≥ 1)

![image 162](<2021-kozma-what-does-typical-metric_images/imageFile162.png>)

2c √n

e P(d12 < 1) ≤

= P(d12 < 1) log

![image 163](<2021-kozma-what-does-typical-metric_images/imageFile163.png>)

![image 164](<2021-kozma-what-does-typical-metric_images/imageFile164.png>)

![image 165](<2021-kozma-what-does-typical-metric_images/imageFile165.png>)

for each c > 0 and n suﬃciently large. Thus, by the subadditivity of entropy,

n 2

H(d12) ≤ cn3/2

log(Vol(Mn)) ≤

for all large n. For small c, this leads to a contradiction with the lower bound in Theorem 1.2.

We proceed to prove the upper bound in Proposition 4.5. The following lemma, which relies on the entropy bounds of Section 3, is the main ingredient.

- Lemma 4.6. There exist absolute constants C, c > 0 such that the


following holds. Let X1, X2, X3 be independent random variables supported in [0, 2]3. Then

3

H(Xi) ≤ C P((X1, X2, X3) ∈/ M3)1/3 − c

![image 166](<2021-kozma-what-does-typical-metric_images/imageFile166.png>)

i=1

3

P(Xi < 1).

i=1

Proof. Set ε := P((X1, X2, X3) ∈/ M3)1/3 and use (33) to deﬁne (ai), (bi) for 1 ≤ i ≤ 3. Proposition 3.3 and (50) imply that

![image 167](<2021-kozma-what-does-typical-metric_images/imageFile167.png>)

3

3

1 2

H(Xi) ≤

H(Xi; [ai, bi]) + Cε (67)

![image 168](<2021-kozma-what-does-typical-metric_images/imageFile168.png>)

i=1

i=1

for an absolute C > 0.

We proceed to estimate the right-hand side of (67). First, Lemma 3.2 shows that P := [a1, b1]×[a2, b2]×[a3, b3] is contained in the closure of M3. Hence, Lemma 3.4 implies that

3

V := Vol(P) ≤ 1 − c1

i=1

|ai − 1| + |bi − 2| (68)

for an absolute 0 < c1 < 1. Second, we shall prove that H(Xi; [ai, bi]) ≤ (1 − 2ε) log(bi − ai) + 2ε

P(Xi < 1) 20

+ c1 |ai − 1| + |bi − 2| −

+ ε (69) for each 1 ≤ i ≤ 3. Lastly, plugging this estimate in (67) gives

![image 169](<2021-kozma-what-does-typical-metric_images/imageFile169.png>)

3

- 1 − 2ε

![image 170](<2021-kozma-what-does-typical-metric_images/imageFile170.png>)

- 2


log(V ) + (C + 29)ε

H(Xi) ≤

![image 171](<2021-kozma-what-does-typical-metric_images/imageFile171.png>)

i=1

3

P(Xi < 1) 20

c1 2

|ai − 1| + |bi − 2| −

.

+

![image 172](<2021-kozma-what-does-typical-metric_images/imageFile172.png>)

![image 173](<2021-kozma-what-does-typical-metric_images/imageFile173.png>)

i=1

Using log(V ) ≤ V − 1 and (68) gives

3

- 1 − 2ε

![image 174](<2021-kozma-what-does-typical-metric_images/imageFile174.png>)

- 2


1 2 − c1

(|ai − 1| + |bi − 2|) + 9c1ε,

log(V ) ≤

![image 175](<2021-kozma-what-does-typical-metric_images/imageFile175.png>)

i=1

where we used the inequality |ai − 1| + |bi − 2| ≤ 3 to bound the error term. We see that the terms containing i |ai −1|+|bi −2| cancel and we are left with

3

c1 40

H(Xi) ≤ Cε −

![image 176](<2021-kozma-what-does-typical-metric_images/imageFile176.png>)

i=1

3

P(Xi < 1),

i=1

as needed.

It remains to prove (69). Fix 1 ≤ i ≤ 3. Lemma 2.3 and the inequality log y ≤ y − 1, valid for all y > 0, give that

bi − ai 1 − 2ε ≤ (1 − 2ε) log(bi − ai) + 2ε.

H(Xi; [ai, bi]) ≤ (1 − 2ε) log

![image 177](<2021-kozma-what-does-typical-metric_images/imageFile177.png>)

Thus it suﬃces to show that the sum of the third and fourth terms in (69) is non-negative. This is the case if: (i) ai ≥ 1, since c1 < 1 and the deﬁnition of ai implies that P(Xi < ai) = ε (see (34)); (ii) bi ≤ 1; (iii) bi − ai ≤ 21; or (iv) ai < 1 and P(ai < Xi < 1) ≤ 20(1 − ai) since

![image 178](<2021-kozma-what-does-typical-metric_images/imageFile178.png>)

P(Xi < 1) = P(ai < Xi < 1) + P(Xi < ai) = P(ai < Xi < 1) + ε. (70)

We thus assume that ai < 1, bi > 1, bi − ai > 21 and P(ai < Xi < 1) > 20(1 − ai). In particular,

![image 179](<2021-kozma-what-does-typical-metric_images/imageFile179.png>)

P(ai < Xi < 1) P(ai < Xi < bi) ≥ 10 ·

1 − ai bi − ai

![image 180](<2021-kozma-what-does-typical-metric_images/imageFile180.png>)

![image 181](<2021-kozma-what-does-typical-metric_images/imageFile181.png>)

Applying the second clause of Lemma 2.3, with the partition [ai, bi] = [ai, 1) ∪ [1, bi], then shows that

P(ai < Xi < 1) 4

bi − ai 1 − 2ε −

H(Xi; [ai, bi]) ≤ (1 − 2ε) log

. This implies (69), again using (70) and the fact that c1 < 1.

![image 182](<2021-kozma-what-does-typical-metric_images/imageFile182.png>)

![image 183](<2021-kozma-what-does-typical-metric_images/imageFile183.png>)

Now recall the notation Fm and hm from (60) and (61), respectively. The following simple lemma is our second ingredient in the proof of the upper bound in Proposition 4.5.

- Lemma 4.7. There exists an absolute constant K > 0 and some 31n ≤ m ≤ 32n for which


![image 184](<2021-kozma-what-does-typical-metric_images/imageFile184.png>)

![image 185](<2021-kozma-what-does-typical-metric_images/imageFile185.png>)

K √n

K n3/2

hm > −

and hm − hm+1 ≤

.

![image 186](<2021-kozma-what-does-typical-metric_images/imageFile186.png>)

![image 187](<2021-kozma-what-does-typical-metric_images/imageFile187.png>)

![image 188](<2021-kozma-what-does-typical-metric_images/imageFile188.png>)

Proof. Recall that m  → hm is decreasing (62) and hm ≤ C/√m + 1 for each m, by Lemma 4.2. We ﬁrst claim that, for some K suﬃciently large,

![image 189](<2021-kozma-what-does-typical-metric_images/imageFile189.png>)

K √n

h⌈2n/3⌉ > −

. (71) Indeed, if it were not the case then from (63) we would get

![image 190](<2021-kozma-what-does-typical-metric_images/imageFile190.png>)

![image 191](<2021-kozma-what-does-typical-metric_images/imageFile191.png>)

n−2

(63)

≤

(n − m − 1)hm

log(Vol(Mn))

m=0

⌈2n/3⌉−1

n−2

K(n − m − 1) √n ≤ Cn3/2 − Kn3/2,

C(n − m − 1) √m + 1 −

≤

![image 192](<2021-kozma-what-does-typical-metric_images/imageFile192.png>)

![image 193](<2021-kozma-what-does-typical-metric_images/imageFile193.png>)

![image 194](<2021-kozma-what-does-typical-metric_images/imageFile194.png>)

![image 195](<2021-kozma-what-does-typical-metric_images/imageFile195.png>)

m=0

m=⌈2n/3⌉

which would contradict the fact that Vol(Mn) ≥ 1, provided that K is suﬃciently large.

Finally, it follows from the pigeonhole principle that for some m with ⌈n/3⌉ ≤ m < ⌈2n/3⌉, we have

C/ n/3 + 1 + K/√n ⌊n/3⌋

![image 196](<2021-kozma-what-does-typical-metric_images/imageFile196.png>)

h⌈n/3⌉ − h⌈2n/3⌉ ⌊n/3⌋

![image 197](<2021-kozma-what-does-typical-metric_images/imageFile197.png>)

K n3/2

hm − hm+1 ≤

≤

≤

. (72)

![image 198](<2021-kozma-what-does-typical-metric_images/imageFile198.png>)

![image 199](<2021-kozma-what-does-typical-metric_images/imageFile199.png>)

![image 200](<2021-kozma-what-does-typical-metric_images/imageFile200.png>)

Moreover, hm ≥ h⌈2n/3⌉ > −K/√n, as claimed. We now ﬁnish the proof of the upper bound in Proposition 4.5. Let 13n ≤ m ≤ 32n be as in Lemma 4.7. Condition on all the distances

![image 201](<2021-kozma-what-does-typical-metric_images/imageFile201.png>)

![image 202](<2021-kozma-what-does-typical-metric_images/imageFile202.png>)

![image 203](<2021-kozma-what-does-typical-metric_images/imageFile203.png>)

dij with ij ∈ Fm and write (X1, X2, X3) for the conditional versions of

(d12, d13, d23). The distribution of (X1, X2, X3) is regarded as random (a function of the variables conditioned upon). Lemma 4.6 shows that

3

H(Xi) ≤ C P(X1 × X2 × X3 ∈/ M3)1/3 − c

i=1

3

P(Xi < 1).

i=1

Averaging over the conditioning, using Jensen’s inequality (for the concave function x  → x1/3), and applying Claim 4.4, we conclude that

3hm ≤ C (2hm − 2hm+1)1/3 − 3cP(d12 < 1) Thus, by Lemma 4.7,

C′ √n

P(d12 < 1) ≤

![image 204](<2021-kozma-what-does-typical-metric_images/imageFile204.png>)

![image 205](<2021-kozma-what-does-typical-metric_images/imageFile205.png>)

for some absolute constant C′, ﬁnishing the proof.

5. The shortest distance in the metric space

In this section, we prove Theorem 1.3, showing that, with high probability, the minimum distance in a uniformly chosen metric space from Mn is only polynomially shorter than one. In order to introduce several key ideas used in the proof of the theorem, we ﬁrst sketch an argument yielding the weaker result that all distances are larger than 2−8. This result will not need any ﬁne estimates on the volume and it will yield an exponential bound on the probability of having a short distance. The ﬁrst step is the following simple proposition.

- Proposition 5.1. For every α ∈ (0, 1/2],


n 2

Vol {d ∈ Mn : min

dij ≤ α} ≤

i,j

(2α)n−2 · Vol(Mn−1).

Proof. By symmetry, it suﬃces to show that the volume of those d ∈ Mn for which dn−1,n ≤ α is at most (2α)n−2 · Vol(Mn−1). Assume that dn−1,n ≤ α and note that, for each i ∈ n − 2 , the distance din must belong to the interval [di,n−1−α, di,n−1+α]. In other words, the volume of the possible values for (din)in=1−2, given all the other distances, is at most (2α)n−2. This gives the desired estimate.

Suppose that d is sampled uniformly from Mn. We could already conclude that P(minij dij ≤ α) is exponentially small in n, for every constant α < 1/2, if we knew that Vol(Mn−1) ≤ eo(n) · Vol(Mn). Such an estimate does indeed hold, as will be shown in Proposition 5.3. Since the proof of Proposition 5.3 is rather involved (even though it is quite natural to conjecture that n  → Vol(Mn) is increasing, see Section 7.1)

and it crucially relies on the volume estimate provided by Theorem 1.2, let us sketch here a self-contained argument showing that

Vol(Mn) ≥ 2−6n · Vol(Mn−1), (73) which is enough to deduce that, for some constants c, C > 0,

dij ≤ 2−8) ≤ Ce−cn. (74)

P(min

i,j

Sketch of a proof of (73). Deﬁne F(d) := min

2 min

dij

A⊆ n

j∈ n \{i}

i∈A

(so that F(d) = 1 if dij ≥ 1/2 for all {i, j}). We claim that, for all suﬃciently large n and all F ∈ (0, 1),

n 2

Vol {d ∈ Mn : F(d) ≤ F} ≤ Fn/10 · 2(

). (75)

Since a stronger estimate will be proved in Lemma 5.6, we only sketch the main idea here. The proof of (75) is similar in spirit to the calculation done in the proof of Proposition 5.1. It relies on the key observation that, if dij is small, the n − 2 pairs of distances (dik, djk) are constrained to a strip in [0, 2]2 of width 2dij. In particular, if F(d) is small, then this signiﬁcantly constrains all distances. For details, we refer the reader to the proof of Lemma 5.6.

Examine the set

Mn1 := {d ∈ Mn : F(d) > 2−5n}. It follows from (75) that

- 1

![image 206](<2021-kozma-what-does-typical-metric_images/imageFile206.png>)

- 2 ≤


- 1

![image 207](<2021-kozma-what-does-typical-metric_images/imageFile207.png>)

- 2


Vol(Mn \ Mn1) ≤

Vol(Mn),

so that Vol(Mn1) ≥ 21Vol(Mn). We claim that the volume of possible extensions of any ﬁxed d ∈ Mn1 to a metric space in Mn+1 is reasonably large. Indeed, denote I(ρ) := [3/2 − ρ/2, 3/2 + ρ/2] and extend d to [0, 2](

![image 208](<2021-kozma-what-does-typical-metric_images/imageFile208.png>)

n+1 2

) by requiring that, for all i ∈ n ,

di,n+1 ∈ I min min

dij, 1

j∈ n \{i}

It is straightforward to check that one obtains a metric space, and further, that the volume of the extension is at least F(d)/2n. (A version of this argument is presented in the proof of Proposition 5.3.) Hence,

Vol(Mn+1) ≥ 2−6n · Vol(Mn1) ≥ 2−6n−1 · Vol(Mn).

Let us point out here that, regardless of other losses in the argument above, using Proposition 5.1 or examining the quantity F gives absolutely no information about distances between 21 and 1; for these, more involved analysis is required.

![image 209](<2021-kozma-what-does-typical-metric_images/imageFile209.png>)

- 5.1. Proof of Theorem 1.3. Giving up optimising various estimates in favour of simplifying the presentation (and because we believe that further ideas would be needed to obtain the optimal value of c), we shall prove the theorem with


c = 1/30.

The starting point of our proof is Proposition 4.5, which states that there exists a constant C such that, when d is a uniformly sampled metric space from Mn,

P(dij < 1) ≤ Cn−1/2 for every {i, j} ∈

n 2

. (76)

This allows us to conclude that a typical metric space sampled from Mn has relatively few distances shorter than one. More precisely, letting

Gn := d ∈ Mn : dij < 1 for at most n5/3 pairs {i, j} , we have

Vol(Gn) > 1 − Cn−1/6 Vol(Mn). (77)

To see (77), let d be a uniformly sampled metric space in Mn and let X be the number of pairs {i, j} such that dij < 1. By Markov’s inequality and (76), we have

E[X] n5/3 ≤ Cn−1/6,

P(X > n5/3) <

![image 210](<2021-kozma-what-does-typical-metric_images/imageFile210.png>)

as needed. In particular, we may restrict our attention to spaces in Gn. Deﬁne

dij < 1 − n−c}.

Bn := {d ∈ Gn : min

i,j

Our argument will comprise two independent parts. First, we will show that the volume of Bn is extremely small when compared to the volume of Mn−2.

Proposition 5.2. For all suﬃciently large n, we have

n1−2c 5 · Vol(Mn−2).

Vol(Bn) ≤ exp −

![image 211](<2021-kozma-what-does-typical-metric_images/imageFile211.png>)

This bound would yield the desired result if we knew that Vol(Mn−2) is not much larger than Vol(Mn). It seems plausible that, in fact,

Vol(Mn) ≥ Vol(Mn−2) (78) holds for all n. However, we have been unable to establish this, see Section 7. We should point out that the volume estimates of Theorem 1.2 imply that (78) holds for an inﬁnite sequence of n and thus

- Proposition 5.2 is suﬃcient to yield the assertion of Theorem 1.3 for that sequence. In order to establish the theorem for all suﬃciently large n, we shall prove the following weaker bound, which still suﬃces for our purposes.
- Proposition 5.3. For all suﬃciently large n, we have Vol(Mn+1) ≥ exp −n1−3c log(n) · Vol(Mn).


We postpone the proofs of Propositions 5.2 and 5.3 to the next two sections and ﬁnish the current section with a short derivation of Theorem 1.3.

Proof of Theorem 1.3. Recalling the deﬁnitions of Gn and Bn, we have P(min

Vol(Mn \ Gn) Vol(Mn)

Vol(Bn) Vol(Mn)

dij < 1 − n−c) ≤

+

.

![image 212](<2021-kozma-what-does-typical-metric_images/imageFile212.png>)

![image 213](<2021-kozma-what-does-typical-metric_images/imageFile213.png>)

i,j

Estimate (77) states that the ﬁrst term in the right-hand side is at most Cn−1/6 whereas Propositions 5.2 and 5.3 give

n1−2c 5 ·

Vol(Mn−2) Vol(Mn) ≤ exp −

Vol(Bn) Vol(Mn) ≤ exp −

![image 214](<2021-kozma-what-does-typical-metric_images/imageFile214.png>)

![image 215](<2021-kozma-what-does-typical-metric_images/imageFile215.png>)

![image 216](<2021-kozma-what-does-typical-metric_images/imageFile216.png>)

n1−2c 6

n1−2c 5

+ 2n1−3c log(n) ≤ exp −

, provided that n is suﬃciently large.

![image 217](<2021-kozma-what-does-typical-metric_images/imageFile217.png>)

![image 218](<2021-kozma-what-does-typical-metric_images/imageFile218.png>)

- 5.2. Bounding the volume of spaces with a short distance. In


this section, we prove Proposition 5.2. We shall split the set Bn into two parts, depending on whether or not there is a point i ∈ n at distance signiﬁcantly shorter than one from many other points, and use diﬀerent arguments to estimate the volume of each of these parts. More precisely, for a metric space d ∈ Mn and an i ∈ n , we deﬁne the set of close neighbours of i by

n−2c 4 and let m := ⌊n1−3c⌋.

Si(d) := j ∈ n \ {i} : dij < 1 −

![image 219](<2021-kozma-what-does-typical-metric_images/imageFile219.png>)

Our ﬁrst lemma uses Theorem 1.2 to provide a very strong upper bound on the volume of all spaces d ∈ Gn (and not only d ∈ Bn) for which |Si(d)| > m for some i ∈ n .

- Lemma 5.4. For all suﬃciently large n, we have

Vol {d ∈ Gn : max

i

|Si(d)| > m} ≤ exp −

n2−8c 16

![image 220](<2021-kozma-what-does-typical-metric_images/imageFile220.png>)

.

Our second lemma bounds the volume of those d ∈ Bn for which |Si(d)| ≤ m for all i ∈ n in terms of the volume of Mn−2.

- Lemma 5.5. For all suﬃciently large n, we have


n1−2c 4 · Vol(Mn−2).

Vol {d ∈ Bn : max

|Si(d)| ≤ m} ≤ exp −

![image 221](<2021-kozma-what-does-typical-metric_images/imageFile221.png>)

i

Proof of Proposition 5.2. Using the estimates of the two lemmas, we may conclude that, for all suﬃciently large n,

n2−8c 16 ≤ exp −

n1−2c 4 · Vol(Mn−2) + exp −

Vol(Bn) ≤ exp −

![image 222](<2021-kozma-what-does-typical-metric_images/imageFile222.png>)

![image 223](<2021-kozma-what-does-typical-metric_images/imageFile223.png>)

n1−2c

5 · Vol(Mn−2), as c < 1/6 and Vol(Mn−2) ≥ 1.

![image 224](<2021-kozma-what-does-typical-metric_images/imageFile224.png>)

- Proof of Lemma 5.4. For i ∈ n , S ⊆ n with |S| = m, and T ⊆ n 2 with |T| = ⌊n5/3⌋, we let


Gni,S,T := d ∈ Gn : Si(d) ⊇ S and djk ≥ 1 if {j, k} ∈/ T .

Note that if d ∈ Gni,S,T and {j, k} ∈ S2 , then necessarily djk ≤ 2(1 − n−2c/4), as follows from the triangle inequality djk ≤ dij + dik. Thus, Gni,S,T is contained in the product set

n−2c

4 · M|S| ×

) ∈ 1 −

(djk){j,k}∈(

S 2

![image 225](<2021-kozma-what-does-typical-metric_images/imageFile225.png>)

{djk ≤ 2}

S 2

)

{j,k}∈T\(

It follows that

n−2c 4

Vol(Gni,S,T) ≤ 1 −

![image 226](<2021-kozma-what-does-typical-metric_images/imageFile226.png>)

|S| 2

(

n 2

{j,k}∈(

S 2

)\(T∪(

{1 ≤ djk ≤ 2}.

))

)

Vol(M|S|) · 2|T| · 1.

|W|
|---|


≈ n−c

Figure 2. W inside [1 − n−2c/4, 2]2.

Estimating Vol(M|S|) using Theorem 1.2 gives

n−2c 4

n2−8c 10

m 2

Vol(Gni,S,T) ≤ exp −

+ C1m3/2 + n5/3 ≤ exp −

![image 227](<2021-kozma-what-does-typical-metric_images/imageFile227.png>)

![image 228](<2021-kozma-what-does-typical-metric_images/imageFile228.png>)

,

where we have used that m = ⌊n1−3c⌋, that c is suﬃciently small (so that 2 − 8c > 5/3) and that n is suﬃciently large. Summing over all possible choices for i, S, and T yields

n2−8c 10 ≤ exp (m + 1) log(n) + n5/3 log(n2) −

n2 ⌊n5/3⌋

n m

exp −

Vol {d ∈ Gn : max

|Si(d)| > m} ≤ n

![image 229](<2021-kozma-what-does-typical-metric_images/imageFile229.png>)

i

n2−8c 16

n2−8c 10 ≤ exp −

,

![image 230](<2021-kozma-what-does-typical-metric_images/imageFile230.png>)

![image 231](<2021-kozma-what-does-typical-metric_images/imageFile231.png>)

where we again used the assumption that 2 − 8c > 5/3.

- Proof of Lemma 5.5. For S ⊆ n with |S| = 2m, we let


BnS := d ∈ Gn : S1(d) ∪ S2(d) ⊆ S and d12 < 1 − n−c and note that, by symmetry,

n 2

Vol(BnS). (79)

Vol {d ∈ Bn : max

|Si(d)| ≤ m} ≤

i

S⊆ n ,|S|=2m

The crucial observation is that if d12 < 1 − n−c, then, for any j  ∈ S, we have (d1j, d2j) ∈ W, where

n−2c

4 ≤ a, b ≤ 2, |a − b| ≤ 1 − n−c . Since

W := (a, b) : 1 −

![image 232](<2021-kozma-what-does-typical-metric_images/imageFile232.png>)

n−2c 4

Vol(W) = 1 +

![image 233](<2021-kozma-what-does-typical-metric_images/imageFile233.png>)

2

−

n−2c 4

+ n−c

![image 234](<2021-kozma-what-does-typical-metric_images/imageFile234.png>)

2

n−2c 2

≤ 1 −

,

![image 235](<2021-kozma-what-does-typical-metric_images/imageFile235.png>)

bounding the volume of (dij : i ∈ {1, 2}, j ∈ S) crudely by 22|S|, we get Vol(BnS) ≤ 22|S| · Vol(W)n−2−|S| · Vol(Mn−2) ≤ 16m · exp −

1 3

n1−2c · Vol(Mn−2),

![image 236](<2021-kozma-what-does-typical-metric_images/imageFile236.png>)

provided that n is suﬃciently large. Substituting this bound into (79) gives the result, since

n 2

n 2m ≤ exp (2m + 2) log(n) ≤ 16−m · exp

n1−2c 12

![image 237](<2021-kozma-what-does-typical-metric_images/imageFile237.png>)

.

- 5.3. Comparing volumes of metric polytopes. This section is devoted to the proof of Proposition 5.3. We show that a large portion of the spaces in Mn admit a signiﬁcant volume of extensions to spaces in Mn+1. To this end, we study certain typical properties of metric spaces in Gn. The ﬁrst step is establishing that, in a typical space in Gn, there are not too many vertices that are incident to a distance that


is signiﬁcantly shorter than 21. Deﬁne, for a set A ⊆ n and a space d ∈ Mn,

![image 238](<2021-kozma-what-does-typical-metric_images/imageFile238.png>)

2 min

dij . (80)

FA(d) :=

j∈ n \{i}

i∈A

(In particular, F∅(d) = 1.)

- Lemma 5.6. If n is suﬃciently large, then for any F ∈ (0, 1), we have


FA(d) ≤ F} ≤ Fn/10 · exp n5/3 log(n) .

Vol {d ∈ Gn : min

A⊆ n

Proof. For a metric space d ∈ Mn and a set B n , deﬁne

FB∗(d) :=

2 min

dij .

j∈ n \B

i∈B

The diﬀerence between FB and FB∗ is that, in the deﬁnition of FB, the index j minimising dij is chosen arbitrarily while, in the deﬁnition of FB∗, it is chosen from outside of B. For each i ∈ B, let jiB(d) denote an (arbitrary) such index, that is, jiB(d) is an arbitrary j ∈ n \ B for which dij = mink∈ n \B dik. We shall shorthand ji(d) := ji{i}(d).

Suppose that d ∈ Gn and that FA(d) ≤ F for some A ⊆ n . We ﬁrst show that there exists a subset B ⊆ A such that

n 2

and FB∗(d) ≤ F1/4. (81)

|B| ≤

![image 239](<2021-kozma-what-does-typical-metric_images/imageFile239.png>)

To see this, let R be a uniformly chosen random subset of n with ⌊n/2⌋ elements, let

B = {i ∈ A ∩ R : ji(d) ∈/ R}, and note that

E log FB∗(d) =

P(i ∈ B) · log 2di,j

i(d) = p · log FA(d) ,

i∈A

where

p = ⌊n/2⌋⌈n/2⌉ n(n − 1) ≥

1 4

.

![image 240](<2021-kozma-what-does-typical-metric_images/imageFile240.png>)

![image 241](<2021-kozma-what-does-typical-metric_images/imageFile241.png>)

Since FA(d) ≤ F ≤ 1, there exists a choice of R for which the set B satisﬁes FB∗(d) ≤ FA(d)1/4 ≤ F1/4.

For a set B ⊆ n with at most n/2 elements, a function J : n → n , and a set T ⊆ n 2 with |T| = ⌊n5/3⌋, deﬁne

GnB,T,J := d ∈ Mn : FB∗(d) ≤ F1/4, jiB(d) = J(i) for all i ∈ B, and dij ≥ 1 if {i, j} ∈/ T .

We may construct each space in GnB,T,J as follows. We ﬁrst choose all the distances dij with {i, j} ∈ n2 \B ∪ B2 and the |B| distances di,J(i) with i ∈ B. Since dij ∈ [1, 2] when ij ∈/ T and dij ∈ [0, 2] otherwise, the volume of all such choices is at most 2|T|. Now, for every i ∈ B and k ∈/ B ∪{J(i)}, the distance dik must satisfy |dik −dJ(i),k| ≤ di,J(i). As a result, given all the other distances, the volume of the set of valid choices for all such dik is not more than

2di,J(i) = FB∗(d)n−|B|−1 ≤ F(n−|B|−1)/4.

i∈B k/∈B∪{J(i)}

We thus get

5/3

Vol(GnB,T,J) ≤ 2|T| · F(n−|B|−1)/4 ≤ 2n

Fn/10,

for n suﬃciently large. Summing over all possible choices for B, T, and J, we have

n2 ⌊n5/3⌋

5/3

Fn/10 ≤ Fn/10 · exp n5/3 log(n) ,

· 2n

FA(d) ≤ F} ≤ 2nnn

Vol {d ∈ G : min

A⊆ n

as claimed.

The second step in the proof of Proposition 5.3 is showing that, in a typical metric space in Gn, distances signiﬁcantly shorter than one do not form large matchings. To this end, for a constant ρ > 0 and d ∈ Mn, we deﬁne

n 2

: dij < 1 − n−ρ . (82)

Tρ(d) := {i, j} ∈

- Lemma 5.7. If µ and ρ are positive constants satisfying


1 3

, (83) then, for all suﬃciently large n,

µ + 2ρ <

![image 242](<2021-kozma-what-does-typical-metric_images/imageFile242.png>)

Vol {d ∈ Gn : Tρ(d) contains a matching of size at least n1−µ} ≤ exp −

n2−2ρ−µ 4

![image 243](<2021-kozma-what-does-typical-metric_images/imageFile243.png>)

.

Proof. Let µ and ρ be positive constants satisfying (83). For disjoint M, T ⊆ n 2 such that M is a matching with |M| = ⌈n1−µ⌉ and |T| = ⌊n5/3⌋, let

GnM,T := {d ∈ Mn : Tρ(d) ⊇ M and dij ≥ 1 if {i, j} ∈/ T}. Denote by V (M) the set of 2|M| endpoints of edges of M and let  LM,T be the set of all triangles that contain an edge of M and two edges that are not in T and whose common endpoint is not in V (M), that is,

 LM,T := ({i, j}, k) ∈ M × n : {i, k}, {j, k}  ∈ T, k  ∈ V (M) .

Observe that every edge in T can ‘prevent’ no more than one triangle from belonging to  LM,T, since M is a matching and since k is not allowed to be in V (M). Hence,

n2−µ 2

| LM,T| ≥ |M|(n − 2|M|) − |T| ≥

, (84) as 2 − µ > 5/3, by (83), and n is suﬃciently large.

![image 244](<2021-kozma-what-does-typical-metric_images/imageFile244.png>)

As in the proof of Lemma 5.5, the crucial observation is that, if ({i, j}, k) ∈  LM,T, then (dik, djk) ∈ W′, where

W′ := (a, b) : 1 ≤ a, b ≤ 2, |a − b| ≤ 1 − n−ρ . Consequently, GnM,T is contained in the following product set:

{(dik, djk) ∈ W′}

{dij ≤ 2}

{1 ≤ dij ≤ 2}.

({i,j},k)∈ LM,T

{i,j}∈T

remaining {i,j}

Since

Vol(W′) = 1 − n−2ρ, we conclude, using (84), that

- 1

![image 245](<2021-kozma-what-does-typical-metric_images/imageFile245.png>)

- 2n2−µ


M,T| ≤ 2n

5/3

· 1 − n−2ρ ≤ exp −n2−µ−2ρ/3 ,

Vol(GnM,T) ≤ 2|T| · Vol(W′)| L

where in the last inequality we used (83). Summing over all possible choices for M and T, we have

Vol {d ∈ Gn : Tρ(d) contains a matching of size at least n1−µ} ≤

n2 ⌊n5/3⌋

n2 ⌈n1−µ⌉

exp −n2−µ−2ρ/3 , from which the lemma follows, again using (83).

The two lemmas enable us to compare the volumes of Mn and Mn+1.

Proof of Proposition 5.3. Recall the deﬁnition of Tρ(d) from (82) and the deﬁnition of FA(d) from (80). Recall also that c = 1/30 and let

ϕ := 6c, ρ := 3c, and µ := 3c. (85) Deﬁne

- Mn1 := d ∈ Mn : min

A⊆ n

FA(d) > exp(−n1−ϕ) ,

- Mn2 := Tρ(d) contains no matching of size at least n1−µ


and let

M∗

n := Gn ∩ Mn1 ∩ Mn2. Since 2 − ϕ > 5/3 and µ + 2ρ = 9c < 1/3, we may use estimate (77),

- Lemma 5.6, Lemma 5.7, and the estimate Vol(Mn) ≥ 1 to conclude that, for suﬃciently large n,


- 1

![image 246](<2021-kozma-what-does-typical-metric_images/imageFile246.png>)

- 2


Vol(M∗

n) ≥

Vol(Mn). (86) For d ∈ Mn deﬁne

n−ρ 2 and let

1 2 −

Q(d) := i ∈ n : min

dij <

![image 247](<2021-kozma-what-does-typical-metric_images/imageFile247.png>)

![image 248](<2021-kozma-what-does-typical-metric_images/imageFile248.png>)

j∈ n \{i}

V (d) := {the vertices of a largest matching in Tρ(d)} ,

where, if there are several largest matchings, we let V (d) to be the vertex set of an arbitrary one of them. For the sake of brevity, from now on we shall write Q and V in place of Q(d) and V (d).

Let d ∈ M∗

n. We aim to deﬁne a set of metric spaces in Mn+1 which extend d. More precisely, we shall ﬁnd a voluminous family of metric spaces d′ ∈ Mn+1 which satisfy

n 2

d′ij = dij, {i, j} ∈

. (87) To this end, deﬁne, for δ > 0,

I(δ) :=

and the following quantities

3 2 −

- 2

,

- 3


δ

δ 2

+

![image 249](<2021-kozma-what-does-typical-metric_images/imageFile249.png>)

![image 250](<2021-kozma-what-does-typical-metric_images/imageFile250.png>)

![image 251](<2021-kozma-what-does-typical-metric_images/imageFile251.png>)

![image 252](<2021-kozma-what-does-typical-metric_images/imageFile252.png>)

2

δ1(i) :=

n−ρ, if i ∈ V , 1, otherwise,

δ2(i) :=

minj =i dij, if i ∈ Q, 1, otherwise.

n+1 2

) satisfying (87) and having d′i,n+1 ∈ I min δ1(i), δ2(i), 1 − 2n−ρ

Claim 5.8. Every d′ ∈ [0, 2](

belongs to Mn+1.

Proof. Since d is a metric space, by (87), it suﬃces to verify the triangle inequality for triangles {i, j, n + 1} with {i, j} ∈ n 2 . Note that d′i,n+1, d′j,n+1 ≥ 1 whereas d′ij = dij ≤ 2, so that we only need to verify that

|d′i,n+1 − d′j,n+1| ≤ dij. (88) We consider three cases, according to the value of dij.

- • If dij < 21 − 12n−ρ, then i, j ∈ Q and |d′i,n+1 − d′j,n+1| ≤

![image 253](<2021-kozma-what-does-typical-metric_images/imageFile253.png>)

![image 254](<2021-kozma-what-does-typical-metric_images/imageFile254.png>)

- 1

![image 255](<2021-kozma-what-does-typical-metric_images/imageFile255.png>)

- 2


min

k =i

dik + min

k =j

djk ≤ dij.

- • If 12 − 21n−ρ ≤ dij < 1 − nρ, then at least one of i and j is in V , as {i, j} ∈ Tρ(d) and V is the vertex set of a largest matching in Tρ(d), and


![image 256](<2021-kozma-what-does-typical-metric_images/imageFile256.png>)

![image 257](<2021-kozma-what-does-typical-metric_images/imageFile257.png>)

- 1

![image 258](<2021-kozma-what-does-typical-metric_images/imageFile258.png>)

- 2 −


- 1

![image 259](<2021-kozma-what-does-typical-metric_images/imageFile259.png>)

- 2


- 1

![image 260](<2021-kozma-what-does-typical-metric_images/imageFile260.png>)

- 2


n−ρ + (1 − 2n−ρ) =

|d′i,n+1 − d′j,n+1| ≤

n−ρ ≤ dij.

• Finally, if dij ≥ 1 − n−ρ, then |d′i,n+1 − d′j,n+1| ≤

- 1

![image 261](<2021-kozma-what-does-typical-metric_images/imageFile261.png>)

- 2


(1 − 2n−ρ) + (1 − 2n−ρ) ≤ dij. The proof of the claim is now complete.

Claim 5.8 implies a lower bound on the ratio of the volumes of Mn+1 and M∗

n. More precisely, for each d ∈ M∗

n, the volume of extensions of d to a d′ ∈ Mn+1 is at least

n

min{δ1(i), δ2(i), 1 − 2n−ρ} ≥ n−ρ |V| ·

dij · (1 − 2n−ρ)n.

min

j =i

i∈Q

i=1

By the deﬁnition of FQ(d), see (80),

dij = 2−|Q| · FQ(d), while the deﬁnition of Q ensures that

min

j =i

i∈Q

−ρ

FQ(d) ≤ 1 − n−ρ |Q| ≤ exp − |Q| · n−ρ ≤ 2−|Q| n

. Since the fact that d ∈ Mn1 gives FQ(d) > exp(−n1−ϕ), we deduce that 2−|Q| · FQ(d) ≥ FQ(d)n

ρ+1 > exp −2n1−ϕ+ρ . Finally, as d ∈ Mn2, we have |V | ≤ 2n1−µ and we conclude that Vol(Mn+1) ≥ n−ρ 2n

1−µ

· exp − 2n1−ϕ+ρ · 1 − 2n−ρ n · Vol(M∗

n)

≥ exp −n1−3c log(n) · Vol(Mn), where the last inequality follows from (85), (86), and our assumption that n is suﬃciently large.

6. Other approaches to estimating the volume

A coloured graph on vertex set V with palette C is simply a function in C(

V 2

). Recall that a hereditary property is a family of coloured graphs that is closed under taking subgraphs and isomorphisms. Questions about the asymptotic growth rate of the volume and the distribution of the edge lengths for a random point in the metric polytope can be viewed as instances of the following very general class of problems: Describe the distribution of a ‘uniformly sampled’ coloured graph (more generally, coloured hypergraph) on n vertices, conditioned to satisfy a given hereditary property P, when n is large. The relevance to our setting is the following: We let V = n and consider the collection of

functions d : V2 → (0, 2] satisfying the hereditary property:

dik ≤ dij + djk for all i, j, k ∈ V . A few related approaches have been used to study problems from this class: exchangeable families of random variables, Szemer´edi’s regularity lemma, graph limits, and the method of hypergraph containers. We refer to the survey paper [4] and references within for a discussion of the

![image 262](<2021-kozma-what-does-typical-metric_images/imageFile262.png>)

![image 263](<2021-kozma-what-does-typical-metric_images/imageFile263.png>)

![image 264](<2021-kozma-what-does-typical-metric_images/imageFile264.png>)

![image 265](<2021-kozma-what-does-typical-metric_images/imageFile265.png>)

Method Upper bound on log Vol(Mn) Main result (Theorem 1.2) O(n3/2) Exchangeability o(n2) Szemer´edi regularity lemma o(n2) Hypergraph container method O n3/2(log n)3 Ko˝va´ri–So´s–Tura´n O n

![image 266](<2021-kozma-what-does-typical-metric_images/imageFile266.png>)

![image 267](<2021-kozma-what-does-typical-metric_images/imageFile267.png>)

![image 268](<2021-kozma-what-does-typical-metric_images/imageFile268.png>)

![image 269](<2021-kozma-what-does-typical-metric_images/imageFile269.png>)

![image 270](<2021-kozma-what-does-typical-metric_images/imageFile270.png>)

![image 271](<2021-kozma-what-does-typical-metric_images/imageFile271.png>)

![image 272](<2021-kozma-what-does-typical-metric_images/imageFile272.png>)

![image 273](<2021-kozma-what-does-typical-metric_images/imageFile273.png>)

![image 274](<2021-kozma-what-does-typical-metric_images/imageFile274.png>)

![image 275](<2021-kozma-what-does-typical-metric_images/imageFile275.png>)

![image 276](<2021-kozma-what-does-typical-metric_images/imageFile276.png>)

![image 277](<2021-kozma-what-does-typical-metric_images/imageFile277.png>)

![image 278](<2021-kozma-what-does-typical-metric_images/imageFile278.png>)

![image 279](<2021-kozma-what-does-typical-metric_images/imageFile279.png>)

![image 280](<2021-kozma-what-does-typical-metric_images/imageFile280.png>)

![image 281](<2021-kozma-what-does-typical-metric_images/imageFile281.png>)

![image 282](<2021-kozma-what-does-typical-metric_images/imageFile282.png>)

2(log log n)2 log n

![image 283](<2021-kozma-what-does-typical-metric_images/imageFile283.png>)

![image 284](<2021-kozma-what-does-typical-metric_images/imageFile284.png>)

![image 285](<2021-kozma-what-does-typical-metric_images/imageFile285.png>)

![image 286](<2021-kozma-what-does-typical-metric_images/imageFile286.png>)

![image 287](<2021-kozma-what-does-typical-metric_images/imageFile287.png>)

Table 1. The upper bounds on the volume of the metric polytope provided by our main result and by the alternative approaches presented in Section 6.

connection between exchangeability, the regularity lemma, and graph limits; for an introduction to the method of hypergraph containers, the reader is referred to the survey paper [7]. In this section, we discuss the problem of estimating the volume of the metric polytope using some of these approaches. These approaches may also be used to obtain some structural information on typical samples from the metric polytope.

- 6.1. Limiting model and exchangeability. The purpose of this section is to give a ‘soft’ proof of a qualitative version of our main result on the volume. Precisely, we shall show that


log Vol(Mn) = o(n2), (89) as in (5). The presented proof relies on exchangeability.

To motivate the proof method, let us start by recalling de Finetti’s theorem [14]. It states that the distribution of an exchangeable sequence of random variables is a mixture of distributions of i.i.d. sequences of random variables. Here, we recall that: (i) a sequence (Xn) of random variables is called exchangeable if, for every ﬁnitelysupported permutation σ, the sequence (Xσ(n)) has the same joint distribution as the sequence (Xn); (ii) the distribution of a sequence is a mixture of distributions of i.i.d. random variables if it can be sampled by ﬁrst randomly sampling a distribution D and then sampling the variables of the sequence independently from the distribution D.

De Finetti’s theorem implies the following conditional independence property: If (Xn) is exchangeable, then, for each n0, after conditioning on {Xn : n > n0} the random variables X1, . . ., Xn

become independent and identically distributed. Indeed, the conditioning determines which distribution D is used in the underlying i.i.d. sequence and independence follows.

0

As metric spaces (dij) are indexed by unordered pairs {i, j}, their relevant context is not that of exchangeable sequences but rather that of exchangeable arrays. An exchangeable array is a two-dimensional array of random variables (Xij), with the index set being all unordered pairs of distinct positive integers, such that, for each ﬁnitely-supported permutation σ, the array (Xσ(i)σ(j)) has the same distribution as the array (Xij). (The names weak exchangeability and partial exchangeability are also used for notions of this type. Higher-dimensional versions and variants where diﬀerent permutations are applied to the coordinates have also been discussed in the literature.) A representation theorem similar to, but more complicated than, de Finetti’s theorem exists for exchangeable arrays; see [1, 23, 24] and especially [2, Theorem 14.21]. It again implies a conditional independence property, stated as follows.

- Lemma 6.1. Let (Xij) be an exchangeable array. For each integer n0 ≥ 1, conditioned on {Xij : max{i, j} > n0} the random variables {Xij : i, j ≤ n0} become independent.


We note that, unlike de Finneti’s theorem, the random variables {Xij : i, j ≤ n0} are not necessarily identically distributed after the conditioning. For completeness, we provide a short proof.

- Proof of Lemma 6.1. The proof is by induction on n0. If n0 ∈ {1, 2}, then the assertion of the lemma is vacuously true (as the set {Xij : i, j ≤ n0} is either empty or contains only one variable). Suppose then that n0 ≥ 3 and that the result has already been established for n0 −1.


Write FnN and Fn for the sigma algebras generated by the collections {Xij : n ≤ max{i, j} ≤ N} and {Xij : max{i, j} ≥ n}, respectively. Let A ⊆ R(

n0−1 2

) be a Borel set. Levy’s upward theorem (a consequence of the martingale convergence theorem) shows that

0−1 ∈ A | FnN

P (Xij)i,j≤n

→ P (Xij)i,j≤n

0−1 ∈ A | Fn

, (90) P (Xij)i,j≤n

0

0

0−1 ∈ A | FnN+1

0+1 → P (Xij)i,j≤n

0−1 ∈ A | Fn

0+1 ,

as N → ∞, almost surely. In addition, the fact that (Xij) is an exchangeable array implies that, for each N ≥ n0 + 1,

= d P (Xij)i,j≤n

0−1 ∈ A | FnN+1

0−1 ∈ A | FnN

P (Xij)i,j≤n

0+1 . Consequently,

0

= d P (Xij)i,j≤n

P (Xij)i,j≤n

0−1 ∈ A | Fn

0−1 ∈ A | Fn

0+1 , which implies that, in fact,

0

P (Xij)i,j≤n

0−1 ∈ A | Fn

0

= P (Xij)i,j≤n

0−1 ∈ A | Fn

0+1 (91)

almost surely. To see the last conclusion, observe that if X is a random variable with ﬁnite second moment and G1 ⊆ G2 are sigma algebras, then

E E[X | G2]2 = E E[X | G1]2 + E (E[X | G2] − E[X | G1])2 .

Thus, if E[X | G1] =d E[X | G2], then E[X | G1] = E[X | G2] almost surely.

As (91) holds for arbitrary Borel A, we conclude (recalling the definition of Fn) that, conditioned on Fn

0+1, the collection of random variables {Xij : i, j ≤ n0 − 1} is independent of the collection {Xij : max{i, j} = n0}. Together with the induction hypothesis this implies that, conditioned on Fn

0+1, the random variables {Xij : i, j ≤ n0 − 1} become independent. These facts together with another use of the exchangeability property imply the lemma.

We proceed to discuss the metric polytope, aiming to prove (89). It is convenient to pass to a discrete problem, to avoid questions on the existence of densities and convergence issues. Speciﬁcally, given integers M and n, deﬁne the discrete metric polytope MnM by

n 2

) : dij ≤ dik + dkj for all i, j, k , see also Section 7.2. We shall prove that, for each ﬁxed even M,

MnM := (dij) ∈ {1, . . ., M}(

log(|MnM|) n 2

M + 2 2

≤ log

. (92)

limsup

![image 288](<2021-kozma-what-does-typical-metric_images/imageFile288.png>)

![image 289](<2021-kozma-what-does-typical-metric_images/imageFile289.png>)

n→∞

n 2

)

(

As Vol(Mn) ≤ M 2

|MnM| for all n, M, see (106) in Section 7.2 below, (92) will imply (89).

![image 290](<2021-kozma-what-does-typical-metric_images/imageFile290.png>)

) by setting all distances involving points i > n to zero. Denote by µMn the uniform distribution on MnM, viewed as a distribution on the space M (

Fix an even M. To apply Lemma 6.1, embed MnM into M (

N 2

) via this embedding. As the set of probability measures on this space is compact with respect to convergence in distribution, there exists a subsequence nm on which the limit superior in (92) is realized and such that µMn

N 2

converges in distribution. Denote the limit

m

measure by µM∞ and note that it is necessarily supported on the inﬁnitedimensional discrete metric polytope

) : dij ≤ dik + dkj for all i, j, k .

M∞M := (dij) ∈ {1, . . ., M}(

N 2

Write d∞ = (d∞ij ) for a sample from µM∞. Note that d∞ is an exchangeable array, inheriting its exchangeability properties from the

measures (µMn ). As before, we write FnN and Fn for the sigma algebras generated by the collections {d∞ij : n ≤ max{i, j} ≤ N} and {d∞ij : max{i, j} ≥ n}, respectively. Lemma 6.1 shows that, conditioned on F4, the random variables (d∞12, d∞13, d∞23) become independent. Thus the support of their (conditional) joint distribution is in some axis-parallel discrete box fully contained in M3M. An analogue of Lemma 3.4 (with an analogous proof) shows that such a box has cardinality at most M2+2 3. In particular,

![image 291](<2021-kozma-what-does-typical-metric_images/imageFile291.png>)

M + 2 2

HS(d∞12, d∞13, d∞23 | F4) ≤ 3 log

, (93)

![image 292](<2021-kozma-what-does-typical-metric_images/imageFile292.png>)

where HS denotes Shannon’s entropy. Recalling our use of Levy’s upward theorem in (90), and noting that (d∞12, d∞13, d∞23) is supported on a ﬁnite set, we see that the conditional distribution of these random variables given F4N converges as N → ∞ to their conditional distribution given F4, almost surely. In particular (again, by the ﬁnite support),

HS(d∞12, d∞13, d∞23 | F4N) = HS(d∞12, d∞13, d∞23 | F4). (94) Let ε > 0. Combining (93) and (94) shows that, for some N0,

lim

N→∞

HS(d∞12, d∞13, d∞23 | FN

4 ) ≤ 3 log

0

M + 2 2

![image 293](<2021-kozma-what-does-typical-metric_images/imageFile293.png>)

+ ε.

Let dn = (dnij) be a sample from µMn . Similar to the above, the fact that µMn

m → µM∞ and {dnij : i, j ≤ N0} is ﬁnitely-supported implies that HS dn

M + 2 2

12 , dn

13 , dn

23 | dn

ij : 4 ≤ max{i, j} ≤ N0 ≤ 3 log

+2ε

m

m

m

m

![image 294](<2021-kozma-what-does-typical-metric_images/imageFile294.png>)

for all large m. By symmetry and monotonicity of conditional entropy, we conclude that, for all large m and all distinct i, j, k ∈ {1, . . ., nm − N0 + 4},

jk | dn

HS dn

ik , dn

ij , dn

ij : nm − N0 + 4 ≤ max{i, j} ≤ nm ≤ 3 log

m

m

m

m

M + 2 2

+ 2ε.

![image 295](<2021-kozma-what-does-typical-metric_images/imageFile295.png>)

We may now apply the subadditivity argument from the proof outline, Section 1.1, to obtain that, for all large m,

log(|MnM

m|) ≤ C log(M)N0nm + log

M + 2 2

![image 296](<2021-kozma-what-does-typical-metric_images/imageFile296.png>)

- 2

![image 297](<2021-kozma-what-does-typical-metric_images/imageFile297.png>)

- 3


ε ·

+

nm 2

for an absolute constant C. Finally, recalling that the limit superior in (92) is realized along nm, and noting that ε is arbitrary and N0 is a function only of ε and µM∞, we conclude that (92) holds.

- 6.2. The Szemere´di regularity lemma approach. In this section, we show how a fairly standard application of (a multi-coloured version of) Szemer´edi’s regularity lemma gives an alternative proof of (5). The argument presented here may be seen as an adaptation of the classical argument of Erd˝os, Frankl, and Ro¨dl [16] proving that the number of H-free graphs with n vertices is 2ex(n,H)+o(n2), where ex(n, H) denotes the maximum number of edges in an H-free graph with n vertices. This approach was independently pursued by Mubayi and Terry [34].


Recall that a bipartite graph G with parts V1 and V2 is ε-regular if, for every W1 ⊆ V1 with |W1| ≥ ε|V1| and W2 ⊆ V2 with |W2| ≥ ε|V2|, we have

eG(W1, W2) |W1||W2|

![image 298](<2021-kozma-what-does-typical-metric_images/imageFile298.png>)

eG(V1, V2) |V1||V2|

−

![image 299](<2021-kozma-what-does-typical-metric_images/imageFile299.png>)

≤ ε,

where eG(W1, W2) is the number of edges connecting a vertex of W1 to a vertex of W2. An equipartition of a set V is a partition of V into V1, . . ., Vk such that |Vi|−|Vj| ≤ 1 for all i and j. The celebrated regularity lemma of Szemer´edi [37] states that, for every positive ε, there exists a constant R such that the vertex set of every graph G admits an equipartition into at most R parts with the property that the bipartite subgraphs of G induced by all but at most an ε-proportion of all pairs of parts are ε-regular. We shall be needing the following straightforward generalisation of this statement to edge-coloured graphs. For the remainder of this section, given a positive integer M, we shall refer to a colouring of all pairs of elements of a set V with elements of M as an M-graph with vertex set V . Moreover, given an M-graph G and a c ∈ M , we shall denote by G(c) the graph whose edges are all pairs of vertices to which G assigns the colour c. The following straightforward generalisation of Szemer´edi’s regularity lemma to M-graphs was formulated in [5]. It may be easily deduced from the standard proof of the regularity lemma.

Theorem 6.2 ([5]). For every ε > 0, M, and r0, there exists an integer R with the following property. The vertex set of an arbitrary M-graph

- G admits an equipartition {V1, . . ., Vr}, where r0 ≤ r ≤ R, such that,


for all but at most ε 2 r pairs {i, j} ∈ r 2 , the bipartite subgraph of G(c) induced by Vi and Vj is ε-regular for every c ∈ M .

For the sake of brevity, we shall refer to partitions satisfying the assertion of the theorem as ε-regular partitions. As in most standard

applications of the regularity lemma, we shall use the following straightforward property of ε-regular graphs, the embedding lemma for triangles. For a more general version of the embedding lemma, we refer the reader to the classical survey of Koml´os and Simonovits [26].

- Proposition 6.3. Let ε ∈ (0, 1/2), suppose that V1, V2, and V3 are pairwise disjoint sets, and let G be a graph with vertex set V1 ∪V2 ∪V3.


If, for each pair {i, j} ∈ 3 2 , the bipartite subgraph of G induced by Vi and Vj is ε-regular and satisﬁes eG(Vi, Vj) ≥ 2ε|Vi||Vj|, then G contains a triangle.

As in the previous section, given integers M and n, we deﬁne MnM := (dij) ∈ {1, . . ., M}(

n 2

) : dij ≤ dik + dkj for all i, j, k , see also Section 7.2 below. We shall prove that

2

|MnM| ≤ Mδn

·

M + 2 2

![image 300](<2021-kozma-what-does-typical-metric_images/imageFile300.png>)

n 2

(

)

(95)

for each ﬁxed even M and δ > 0, provided that n is suﬃciently large. We remark here that Mubayi and Terry [34] independently used a similar approach, combined with a delicate stability analysis, to prove the

n 2

(

)

much more accurate estimate |MnM| = (1 + e−Ω(n)) M2+2

for each ﬁxed even M. As Vol(Mn) ≤ M 2

![image 301](<2021-kozma-what-does-typical-metric_images/imageFile301.png>)

n 2

(

)

|MnM|, see (106) in Section 7.2 below, (95) will imply that Vol(Mn) = 2o(n2).

![image 302](<2021-kozma-what-does-typical-metric_images/imageFile302.png>)

As proofs of both (95) and the improved estimate of [34] rely on the regularity lemma, the rate of convergence implicit in the o(n2) term in the exponent is very slow. Possibly, one could use weaker forms of the regularity lemma to improve this rate of convergence. We do not pursue this direction here, but only mention that one such regularity lemma, guaranteeing a regular partition whose number of parts is only exponential in ε−2, was obtained by Frieze and Kannan [19, 20], see also [11, Section 1.4]. (In our context, a multi-coloured version of such a regularity lemma would most likely have been required.)

Fix an even integer M and δ ∈ (0, 1/2) and let ε = 10M log(1δ /δ) and

![image 303](<2021-kozma-what-does-typical-metric_images/imageFile303.png>)

r0 = 2/δ. Choose an arbitrary G ∈ MnM, which may be viewed as an M-graph with vertex set n , and apply Theorem 6.2 to G to obtain

an ε-regular partition {V1, . . ., Vr} of n with r0 ≤ r ≤ R for some constant R = R(M, δ). For every pair {i, j} ∈ 2 r , deﬁne

Dij = c ∈ M : eG(c)(Vi, Vj) ≥ 2ε|Vi||Vj|

and observe that all but at most a 2Mε-proportion of pairs in Vi×Vj are coloured with an element of Dij. Call a triple {i, j, k} ∈ r 3 regular if the bipartite subgraphs of G(1), . . ., G(M) induced by (Vi, Vj), (Vi, Vk), and (Vj, Vk) are all ε-regular. It follows from Proposition 6.3 that, for every regular triple {i, j, k}, we must have Dij × Dik × Djk ⊆ M3M. Indeed, otherwise G would contain a triple of distances that do not satisfy the triangle inequality. A discrete analogue of Lemma 3.4 (with an analogous proof) shows that Dij ×Dik×Djk has cardinality at most

3. As {V1, . . ., Vr} is an ε-regular partition of G, all but at most 3ε r3 triples {i, j, k} ∈ 3 r are regular. Consequently,

M+2 2

![image 304](<2021-kozma-what-does-typical-metric_images/imageFile304.png>)

1 r−2

![image 305](<2021-kozma-what-does-typical-metric_images/imageFile305.png>)

|Dij||Dik||Djk|

|Dij| =

r 3

)

{i,j,k}∈(

r 2

)

{i,j}∈(

1 r−2

r 3

r 2

)

3(1−3ε)(

(

)

![image 306](<2021-kozma-what-does-typical-metric_images/imageFile306.png>)

M + 2 21−3ε

M + 2 2

r 3

)

M9ε(

≤

≤

. (96)

![image 307](<2021-kozma-what-does-typical-metric_images/imageFile307.png>)

![image 308](<2021-kozma-what-does-typical-metric_images/imageFile308.png>)

Since G was arbitrary, the above analysis shows that one may con-

struct each element of MnM as follows. First, choose r, the equipartition {V1, . . ., Vr}, and the sets Dij ⊆ M ; the number of choices for all three combined is 2O(n) (with implicit constant depending on M and

δ). Next, for each {i, j} ∈ r 2 , choose a set Xij ⊆ Vi × Vj of at most 2Mε|Vi||Vj| pairs whose colour will not belong to Dij; there are at most

n 2

) ⌊2Mε(

(

)⌋ ≤ exp Mε log(e/(2Mε))n2 ways to do it. Finally, choose

n 2

colours for all n2 pairs in such a way that each pair in Vi × Vj \ Xij is assigned a colour from Dij; the number of ways one can do this is

i,j

n 2

)− i,j |Vi×Vj\Xij|. (97)

i×Vj\Xij| · M(

|Dij||V

Recalling that |Vi × Vj| ≥ ⌊n/r⌋2 and |Xij| ≤ 2Mε|Vi||Vj| for each {i, j} ∈ 2 r , inequality (96) implies that (97) is at most

r 2

)·(1−2Mε)⌊n/r⌋2

(

M + 2 21−3ε

r 2

n 2

)·(1−2Mε)⌊n/r⌋2. (98)

)−(

· M(

![image 309](<2021-kozma-what-does-typical-metric_images/imageFile309.png>)

Finally, as n2 − 2 r ⌊n/r⌋2 ≤ 1r n2 + r(n − 1) and r0 ≤ r ≤ R, a straightforward calculation shows that (98) is at most

![image 310](<2021-kozma-what-does-typical-metric_images/imageFile310.png>)

M + 2 2

![image 311](<2021-kozma-what-does-typical-metric_images/imageFile311.png>)

n 2

)

(

2

n 2

+2Mε+3ε+2nR (

).

1 r0

![image 312](<2021-kozma-what-does-typical-metric_images/imageFile312.png>)

![image 313](<2021-kozma-what-does-typical-metric_images/imageFile313.png>)

This yields the claimed upper bound on |MnM| stated in (95), provided that n is suﬃciently large, by our choice of ε = ε(M, δ) and r0 = r0(δ).

- 6.3. The hypergraph container method. In this section, which is based on joint work with Rob Morris, we shall show how the method of hypergraph containers can be used to derive a volume estimate of the form


Vol(Mn) ≤ exp Cn3/2(log n)3 , (99) which falls just a little short of the upper bound established in Theorem 1.2 using entropy methods. We point out that the arguments presented here are inspired by the (earlier) work of Balogh and Wagner [8], who were the ﬁrst to use the container method for enumerating ﬁnite metric spaces and obtained the bound Vol(Mn) ≤ exp(n11/6+o(1)).

The hypergraph container theorems, proved simultaneously, but separately, in [6] and [36], state that the family of independent sets of any uniform hypergraph whose edges are suﬃciently evenly distributed can be covered by a small family of containers, subsets of vertices of the hypergraph that themselves are nearly independent. The wide applicability of this abstract statement stems from the fact that many discrete structures may be naturally represented as independent sets of some auxiliary hypergraph; in particular, this is the case with the metric spaces in MnM. The particular version of the hypergraph container theorem stated below was proved in [33]; see also [7] for a survey.

Suppose that H is a k-uniform hypergraph, i.e. each (hyper)edge has exactly k vertices. We write V (H ) to denote the vertex set of

- H and we identify H with its (hyper)edge set; we denote by v(H ) and e(H ) the numbers of vertices and edges of H , respectively. A set I ⊆ V (H ) is called independent if it contains no edges of H . We moreover deﬁne, for every ℓ ∈ {1, . . ., k},


V (H ) ℓ

∆ℓ(H ) = max |{S ∈ H : T ⊆ S}|: T ∈

.

In other words, ∆ℓ(H ) is the maximum number of edges of H that a single ℓ-element set of vertices can be contained in.

We say that a family C of subsets of V (H ) is a family of containers for (the independent sets of) H if every independent set is contained in some B ∈ C. Every hypergraph H admits two trivial families of containers: the one-element family {V (H )} and the family of all (maximal) independent sets of H . The following proposition guarantees the existence of a family of containers that interpolates between these two

extremes: it is much smaller than the family of all independent sets but each of the containers is signiﬁcantly smaller than V (H ).

- Proposition 6.4. Let H be a non-empty k-uniform hypergraph. Suppose that positive integers b and r satisfy


∆ℓ(H ) ≤

b v(H )

![image 314](<2021-kozma-what-does-typical-metric_images/imageFile314.png>)

ℓ−1 e(H ) r

![image 315](<2021-kozma-what-does-typical-metric_images/imageFile315.png>)

for every ℓ ∈ {1, . . ., k}. Then there exists a collection C of at most exp kblog(v(H )) subsets of V (H ) such that:

- (i) every independent set of H is contained in some B ∈ C;
- (ii) |B| ≤ v(H ) − 2−k(k+1) · r for every B ∈ C.


In a typical application of the proposition, such as the one presented in this section, one takes r to be close to v(H ) while b = v(H )α for some α ∈ (0, 1).

Call a triple (a, b, c) of numbers non-metric if some permutation of (a, b, c) does not satisfy the triangle inequality, that is, if a + b < c, a + c < b, or b + c < a. Given positive integers n and M, deﬁne the hypergraph HnM of non-metric triangles as follows. The vertex set of HnM is n 2 × M and its edges are all triples {(ei, di)}3i=1 such that

- • {e1, e2, e3} is the set of edges of some triangle in the complete graph on n ,
- • (d1, d2, d3) is a non-metric triple.


It is not hard to see that the elements of MnM are in a one-to-one correspondence with independent subsets of HnM that contain exactly one element of the set {e} × M for each e ∈ n 2 .

Now, given a set A ⊆ n 2 × M , deﬁne, for each e ∈ n 2 , Ae := {d ∈ M : (e, d) ∈ A}.

Viewing A as a representation of the product set e Ae, we deﬁne its volume by

|Ae|,

Vol(A) :=

n 2

)

e∈(

which is precisely the number of sets I ⊆ A that contain exactly one element of the set {e} × M for each e ∈ n 2 .

The following supersaturation statement for HnM is the key ingredient in our application of the container method to the setting of discrete metric spaces.

- Proposition 6.5. Let n and M be positive integers, with M even and n ≥ 3. Suppose that A ⊆ n 2 × M satisﬁes


n 2

(

)

(1 + ε)M 2

Vol(A) ≥

![image 316](<2021-kozma-what-does-typical-metric_images/imageFile316.png>)

for some ε ≥ 16/M. Then there exist an m ∈ M and a set A′ ⊆ A with |A′| ≤ mn2 such that

- • e(HnM[A′]) ≥ εm2M n3 /(32 log2 M),
- • ∆1(HnM[A′]) ≤ 4nm2,
- • ∆2(HnM[A′]) ≤ 2m,


where H [B] denotes the subhypergraph of H induced by the subset B, that is, the hypergraph whose vertex set is B and whose edges are all edges of H that are fully contained in B.

The basic building block in the proof of Proposition 6.5 is the following elementary lemma, which one can prove combining the ideas in the proofs of Lemmas 3.2 and 3.4.

Lemma 6.6. Let M and m be positive integers, with M ≥ 16 even, and suppose that A, B, C ⊆ M . Let A′ ⊆ A comprise the m largest and the m smallest elements of A and deﬁne B′ and C′ analogously. If |A| · |B| · |C| ≥ (M/2 + 2m)3, then the set A′ × B′ × C′ contains m3 non-metric triples.

n 2

), we may assume that ε ≤ 1 and hence M ≥ 16. Let T be the family of edge sets of all triangles in the complete graph with vertex set n . Since each edge (of the complete graph) belongs to exactly n − 2 triangles,

Proof of Proposition 6.5. As Vol(A) ≤ M(

n 3

(

)

(1 + ε)M 2

n−2 3

3|)1/3 = Vol(A)

(|Ae

1||Ae

2||Ae

≥

. (100)

![image 317](<2021-kozma-what-does-typical-metric_images/imageFile317.png>)

![image 318](<2021-kozma-what-does-typical-metric_images/imageFile318.png>)

e1e2e3∈T

We partition the family T as follows. Set smax = ⌊log2 M⌋ − 2 and, for each s ∈ {0, . . ., smax}, deﬁne

M 2

M 2

3|)1/3 ∈

+ 2s+1,

+ 2s+2 ;

Ts := e1e2e3 ∈ T : (|Ae

1||Ae

2||Ae

![image 319](<2021-kozma-what-does-typical-metric_images/imageFile319.png>)

![image 320](<2021-kozma-what-does-typical-metric_images/imageFile320.png>)

moreover, let T∗ := T \ ssmax=0 Ts. Observe that T∗ contains only e1e2e3 with |Ae

3| < (M2 + 2)3, as 2s

max+2 > M/2, and thus

1||Ae

2||Ae

![image 321](<2021-kozma-what-does-typical-metric_images/imageFile321.png>)

smax

|Ts|

|T∗|

M 2

M 2

3|)1/3 ≤

+ 2s+2

·

2||Ae

1||Ae

(|Ae

+ 2

. (101)

![image 322](<2021-kozma-what-does-typical-metric_images/imageFile322.png>)

![image 323](<2021-kozma-what-does-typical-metric_images/imageFile323.png>)

s=0

e1e2e3

We claim that there is an s ∈ {0, . . ., smax} satisfying |Ts| ≥

n 3

εM 2s+5 log2 M

.

![image 324](<2021-kozma-what-does-typical-metric_images/imageFile324.png>)

Indeed, if this were not true, then (101) would contradict (100), as 16/M ≤ ε ≤ 1 and smax + 1 ≤ log2 M (we omit the straightforward calculation).

Finally, let m = 2s and let A′ be the set of all pairs (e, d) ∈ A such that d is among the m largest or the m smallest elements of Ae. This deﬁnition guarantees that |A′| ≤ 2m n2 ≤ mn2, that ∆1(HnM[A′]) ≤ (2m)2n, and that ∆2(HnM[A′]) ≤ 2m. For each e1e2e3 ∈ Ts, we may invoke Lemma 6.6 with (A, B, C) ← (Ae

) to deduce that the set A′e

, Ae

, Ae

1

2

3

×A′e

×A′e

contains at least m3 non-metric triples. In particular,

1

2

3

εMm2 32 log2 M

n 3

e(HnM[A′]) ≥ |Ts| · m3 ≥

, which concludes the proof of the proposition.

![image 325](<2021-kozma-what-does-typical-metric_images/imageFile325.png>)

Fix a large integer n and let M = 2⌊n2⌋. Suppose that A ⊆ n 2 × M satisﬁes Vol(A) = (1+2ε)M

![image 326](<2021-kozma-what-does-typical-metric_images/imageFile326.png>)

n 2

)

(

for some 16/M ≤ ε ≤ 1 and let m and A′ be as in Proposition 6.5. It is straightforward to verify that the (3-uniform) hypergraph HnM[A′] satisﬁes the assumption of Proposition 6.4 with

![image 327](<2021-kozma-what-does-typical-metric_images/imageFile327.png>)

b := n3/2 and r :=

εM n3 128nlog2 M ≥

εMn2 210 log2 M

.

![image 328](<2021-kozma-what-does-typical-metric_images/imageFile328.png>)

![image 329](<2021-kozma-what-does-typical-metric_images/imageFile329.png>)

The proposition supplies a family C′ of at most exp 3n3/2 log(n2M) containers for independent sets of HnM[A′], each of cardinality at most |A′| − 222εMnlog22M. Therefore, the collection

![image 330](<2021-kozma-what-does-typical-metric_images/imageFile330.png>)

C := C(A) := {(A \ A′) ∪ B′ : B′ ∈ C ′}

is a family of containers for independent sets of HnM[A], with the same cardinality as C, that satisﬁes, for every B ∈ C,

εMn2 222 log2 M

n 2

)

(

(1 + ε′)M 2

M − 1 M

![image 331](<2021-kozma-what-does-typical-metric_images/imageFile331.png>)

Vol(B) ≤

· Vol(A) =

,

![image 332](<2021-kozma-what-does-typical-metric_images/imageFile332.png>)

![image 333](<2021-kozma-what-does-typical-metric_images/imageFile333.png>)

for some ε′ ≤ 1 − 222log1 2M ε.

![image 334](<2021-kozma-what-does-typical-metric_images/imageFile334.png>)

We build a family C of containers for the independent sets of MnM recursively as follows. We start with the trivial family containing only

the set n 2 × M . As long as our family contains some set A with

n 2

)

(

(1 + ε0)M 2

,

Vol(A) >

![image 335](<2021-kozma-what-does-typical-metric_images/imageFile335.png>)

where ε0 := 1/√n ≥ 16/M, we replace A with the elements of the family C (A) deﬁned above. We claim that the depth of the recursion is

![image 336](<2021-kozma-what-does-typical-metric_images/imageFile336.png>)

bounded by t := C log2(M) log(n), for some large constant C. Indeed, if a set B reached the t-th level of the recursion, then

n 2

)

(

(1 + εt)M 2

Vol(B) ≤

, where

![image 337](<2021-kozma-what-does-typical-metric_images/imageFile337.png>)

t

1 222 log2 M

16 M ≤ ε0,

εt = max 1 −

,

![image 338](<2021-kozma-what-does-typical-metric_images/imageFile338.png>)

![image 339](<2021-kozma-what-does-typical-metric_images/imageFile339.png>)

a contradiction. It follows that |C| ≤ exp 3n3/2 log(n2M) · t ≤ exp Cn3/2(log n)3 .

Since each space in MnM corresponds to an independent set of HnM and is thus described by one of the containers, we obtain

n 2

(

)

M 2

Vol(B) ≤ exp Cn3/2(log n)3 + n3/2 ·

|MnM| ≤

.

![image 340](<2021-kozma-what-does-typical-metric_images/imageFile340.png>)

B∈C

Finally, this translates to the following upper bound on the volume:

n 2

)

(

2 M

· |MnM| ≤ exp Cn3/2(log n)3 , see (106) in Section 7.2 below.

Vol(Mn) ≤

![image 341](<2021-kozma-what-does-typical-metric_images/imageFile341.png>)

- 6.4. The K˝ov´ari–S´os–Tur´an approach. In this section, we shall show yet another approach to the volume estimate. The estimate it gives is


Cn2(log log n)2 log n

Vol(Mn) ≤ exp

, (102)

![image 342](<2021-kozma-what-does-typical-metric_images/imageFile342.png>)

better than what we obtained using the exchangeability or the regularity lemma approaches, but not as good as what is proved by the entropy or the hypergraph container methods. Our argument bears similarities to the classical work of Erd˝os, Kleitman, and Rotschild [17], which estimates the number of graphs that do not contain a clique of a given size.

Given a positive integer t, we shall write Kt,t for the complete bipartite graph with t vertices on each side. The Tur´n number for Kt,t, denoted ex(n, Kt,t), is the largest number of edges in an n-vertex graph that does not contain Kt,t as a (not necessarily induced) subgraph. The following well-known upper bound on ex(n, Kt,t) was obtained by Ko˝va´ri, S´os, and Tura´n [27], see also [21, Section 3].

Theorem 6.7 (K˝ov´ri–So´s–Tura´n [27]). For every t ≥ 2, ex(n, Kt,t) ≤

- 1

![image 343](<2021-kozma-what-does-typical-metric_images/imageFile343.png>)

- 2


(t − 1)1/tn2−1/t + (t − 1)n .

Fix integers n and t ≥ 2 and a real δ ∈ (0, 1). For a d ∈ Mn, let T(d) := {i, j} ∈

n 2

: dij < 1 − δ

![image 344](<2021-kozma-what-does-typical-metric_images/imageFile344.png>)

and partition Mn into Mnt,δ and Mnt,δ, where

![image 345](<2021-kozma-what-does-typical-metric_images/imageFile345.png>)

Mnt,δ := {d ∈ Mn : T(d) Kt,t} and Mnt,δ := Mn \ Mnt,δ. Since |T(d)| ≤ ex(n, Kt,t) for every d ∈ Mnt,δ, we have

n 2

n 2

)−ex(n,Kt,t)

t,t) · (1 + δ)(

Vol(Mnt,δ) ≤

ex(n, Kt,t) · 2ex(n,K

≤ exp 3ex(n, Kt,t) log n + δn2 . It follows from Theorem 6.7 and simple calculus that, if n ≥ t2 ≥ 4,

Vol(Mnt,δ) ≤ exp 5n2−1/t log n + δn2 . (103) We now derive an upper bound on the volume of Mnt,δ. Lemma 6.8. If t ≥ 6, n ≥ 4t2, and δ ≥ 3 log(4t)/t, then

![image 346](<2021-kozma-what-does-typical-metric_images/imageFile346.png>)

![image 347](<2021-kozma-what-does-typical-metric_images/imageFile347.png>)

Vol(Mnt,δ) ≤ e−n · Vol(Mn−2t).

![image 348](<2021-kozma-what-does-typical-metric_images/imageFile348.png>)

Proof. Suppose that d ∈ Mnt,δ. By deﬁnition, we may ﬁnd two disjoint t-element sets I, J ⊆ n such that dij < 1 − δ for every pair (i, j) ∈

- I × J. Fix any such pair (I, J) and suppose that k ∈ n \ (I ∪J). Let


aI = min

dik, bI = max

dik, aJ = min

djk, bJ = max

djk.

i∈I

i∈I

j∈J

j∈J

Since all distances between I and J are shorter than 1−δ, both bJ −aI and bI − aJ must be smaller than 1 − δ and, consequently,

2

(bI − aI) + (bJ − aJ) 2

< (1 − δ)2.

(bI − aI)(bJ − aJ) ≤

![image 349](<2021-kozma-what-does-typical-metric_images/imageFile349.png>)

In other words, all distances between k and I and between k and J fall into intervals AI and AJ, respectively, where |AI| · |AJ| < (1 − δ)2. In particular, if W denotes the set of all 2t-dimensional vectors (d′ik)i∈I∪J which may be used to complete (de)e∈(

) to a metric space on I ∪J ∪ {k}, then

I∪J 2

Vol(W) ≤ t4 · 24 · (1 − δ)2t−4, as there are at most t4 choices for the i, i′ ∈ I and j, j′ ∈ J for which aI = dik, bI = di′k, aJ = djk, and bJ = dj′k. By our assumption on t and δ,

Vol(W) ≤ 2te−δ(t−2)/2 4 ≤ 2te−δt/3 4 ≤ 2−4.

![image 350](<2021-kozma-what-does-typical-metric_images/imageFile350.png>)

We may now bound the volume of Mnt,δ as follows. First, the number of choices for I and J is at most nt 2 and the volume of the distances between pairs in I ∪ J does not exceed 2(

2t 2

). Next, bounding the volume of (dik)i∈I∪J,k/∈I∪J as above and the volume of (dij)i,j /∈I∪J by Vol(Mn−2t), we obtain

2

n t

2t 2

) · Vol(W)n−2t · Vol(Mn−2t) ≤ n2t · 22t

· 2(

![image 351](<2021-kozma-what-does-typical-metric_images/imageFile351.png>)

Vol(Mnt,δ) ≤

2

· 2−4n+8t · Vol(Mn−2t), which, with our assumption on n and t, implies the claimed bound.

One may now derive (102) by induction on n using Lemma 6.8 and

the upper bound on Vol(Mnt,δ) given by (103). In the inductive step, one may take t = log n/(2 log log n) and δ = 3 log(4t)/t, say. We leave the details to the reader.

7. Discussion and open questions

- 7.1. Further questions. As we remarked, we were not able to decide


whether Vol(Mn) is increasing in n. If one could prove that this is indeed the case, this would greatly simplify our proof of Theorem 1.3 on the shortest distance in the metric space sampled uniformly from Mn.

Suppose that d is a metric space sampled uniformly from Mn. A key ingredient in our proof of Theorem 1.3 is the upper bound on P(d12 < 1) established in Proposition 4.5. It would be interesting to obtain additional information about the distribution of d12. In particular, is it true that P(d12 < 1) = Θ(n−1/2)? We believe that this is the case and our belief seems to be supported by the lower bound of Proposition 4.5. Going even further and writing fn for the density of the random variable d12, one may ask whether the function [0, ∞) ∋ t  → fn(1 − √tn) has

![image 352](<2021-kozma-what-does-typical-metric_images/imageFile352.png>)

![image 353](<2021-kozma-what-does-typical-metric_images/imageFile353.png>)

a limit as n → ∞? It would also be very interesting to estimate the probability P(d12 < 1 − √tn) for t ≫ 1. Propositions 5.1 and 5.3 imply that P(d12 < α) is exponentially small in n for every ﬁxed α < 1/2, see also (74), but we are not ready to make any conjectures about the range t ≤

![image 354](<2021-kozma-what-does-typical-metric_images/imageFile354.png>)

![image 355](<2021-kozma-what-does-typical-metric_images/imageFile355.png>)

√n/2.

![image 356](<2021-kozma-what-does-typical-metric_images/imageFile356.png>)

Do the empirical measures of individual distances (and tuples of distances) satisfy a large deviation principle? If so, what is the rate function? Is it possible to recover our result about the minimum distance from such a large deviation estimate?

- 7.2. Relation with the discrete problem. One may naturally consider a discrete analogue of the problem we study in this paper, where we require the distances between every pair of points to be integers. More speciﬁcally, given integers M ≥ 1 and n ≥ 2, one may consider the space MnM deﬁned by


n 2

) : dij ≤ dik + dkj for all i, j, k ,

MnM := (dij) ∈ {1, . . ., M}(

which is closely related to the metric polytope Mn. Indeed, for every n, Mn is naturally obtained as a limit of M 2 MnM as M tends to inﬁnity. We proceed to discuss some of the quantitative aspects of this relation.

![image 357](<2021-kozma-what-does-typical-metric_images/imageFile357.png>)

As with the continuous problem, observing that the cube

M 2

![image 358](<2021-kozma-what-does-typical-metric_images/imageFile358.png>)

,

M 2

![image 359](<2021-kozma-what-does-typical-metric_images/imageFile359.png>)

+ 1, . . ., M

n 2

)

(

(104)

is fully contained in MnM, one gets the following simple lower bound on the cardinality of MnM:

n 2

(

)

M + 1 2

|MnM| ≥

. (105)

![image 360](<2021-kozma-what-does-typical-metric_images/imageFile360.png>)

In fact, one may obtain bounds on |MnM| from bounds on Vol(Mn) and vice-versa. In one direction, consider the map ϕ: (0, 2](

n 2

) → {1, . . ., M}(

n 2

) deﬁned by

Mdij 2

.

ϕ(d)ij =

![image 361](<2021-kozma-what-does-typical-metric_images/imageFile361.png>)

Observe that ϕ maps Mn to MnM (as ⌈x⌉ + ⌈y⌉ ≥ ⌈z⌉ whenever x + y ≥ z) and that Vol(ϕ−1(d′)) = M 2

n 2

)

(

n 2

). Consequently,

for any d′ ∈ {1, . . ., M}(

![image 362](<2021-kozma-what-does-typical-metric_images/imageFile362.png>)

n 2

)

(

2 M

|MnM|.

Vol(Mn) ≤

![image 363](<2021-kozma-what-does-typical-metric_images/imageFile363.png>)

In the other direction, consider the map ψ from MnM to the power set of (0, 2](

n 2

) deﬁned by ψ(d) =

2 M + 2

2 M + 2

(dij + 1),

(dij + 2) .

![image 364](<2021-kozma-what-does-typical-metric_images/imageFile364.png>)

![image 365](<2021-kozma-what-does-typical-metric_images/imageFile365.png>)

i,j

Observe that ψ maps each d ∈ MnM to a cube that is fully contained in Mn (as x + y ≥ z implies that (x + ∆x) + (y + ∆y) ≥ (z + ∆z) for all ∆x, ∆y, ∆z ∈ (1, 2]) so that cubes corresponding to diﬀerent d are disjoint. It follows that

n 2

)

(

2 M + 2

|MnM|

≤ Vol(Mn). Putting these bounds together yields

![image 366](<2021-kozma-what-does-typical-metric_images/imageFile366.png>)

M 2

![image 367](<2021-kozma-what-does-typical-metric_images/imageFile367.png>)

n 2

(

)

Vol(Mn) ≤ |MnM| ≤

M 2

+ 1

![image 368](<2021-kozma-what-does-typical-metric_images/imageFile368.png>)

n 2

(

)

Vol(Mn). (106)

Concurrently with the writing of this paper, Mubayi and Terry [34] studied the discrete problem in the regime where M is ﬁxed and n tends to inﬁnity, proving that

|MnM| =   

n 2

(

)

1 + e−Ω(n) M2 + 1

if M is even,

![image 369](<2021-kozma-what-does-typical-metric_images/imageFile369.png>)

(107)

n 2

)+o(n2) if M is odd

(

M+1 2

![image 370](<2021-kozma-what-does-typical-metric_images/imageFile370.png>)

(with additional structural information in the odd M case).

The above bound reveals that for even M, the structure of a uniformly chosen space from MnM is very rigid: the probability that even a single distance lies outside the discrete interval {M/2, . . ., M} is exponentially small. This strong rigidity property stems from the assumption that M is ﬁxed and does not hold in the continuous setting. Indeed, the bound (7) shows that the minimum distance is smaller than 1 − √cn in typical samples from Mn. Handling such microscopic ﬂuctuations contributes to the diﬃculty in controlling the volume of Mn and understanding the structure of typical samples from it.

![image 371](<2021-kozma-what-does-typical-metric_images/imageFile371.png>)

![image 372](<2021-kozma-what-does-typical-metric_images/imageFile372.png>)

- 7.3. Metric preserving maps. A map φ: [0, ∞) → [0, ∞) is metric preserving if φ(d) = φ(dij) is a metric on some set whenever d = (dij) is, e.g., the ceiling operation from the previous subsection. There are many interesting examples of such maps, see [12]. Every metric


preserving map φ such that supx∈[0,2] φ(x) ≤ 2 induces a self-map of the metric polytope. We wonder how metric preserving maps can be utilized to further study the structure of the metric polytope.

- 7.4. Other models for random metric spaces. In this paper we investigated a certain model of a ‘random metric space’, which in some sense is natural. The conclusion of our results is that on a large scale this model essentially reduces to the ‘trivial’ model where all distances are in the interval [1, 2], and the triangle inequality is trivially satisﬁed. It would be interesting to ﬁnd other models for a ‘random metric space’, which are ‘natural’ on the one hand, and ‘interesting’ on the other hand, in the sense that they reveal new phenomena about metric spaces. In [39] Vershik considered one natural candidate for a random metric space, and proved that it is essentially the Urysohn universal metric space. As remarked within the paper, ‘An obvious drawback of our construction is that it is not invariant with respect to the numbering of points’.


Acknowledgments. We thank Itai Benjamini for asking the question and Gil Kalai for informing us that this object is known as the metric polytope. We thank Omer Angel, Dor Elboim, Ronen Eldan, Ehud Friedgut, Shoni Gilboa, Rob Morris, Bal´sz Ra´th and Johan Wa¨stlund for many interesting discussions. Special thanks are due to Rob Morris, who kindly agreed to us presenting the results of our joint work with him in Section 6.3 of this paper.

References

- [1] D. J. Aldous. Representations for partially exchangeable arrays of random variables. J. Multivariate Anal., 11(4):581–598, 1981.
- [2] D. J. Aldous. Exchangeability and related topics. In Ecole´ d’e´te´ de probabilite´s de Saint-Flour, XIII—1983, volume 1117 of Lecture Notes in Math., pages 1–198. Springer, Berlin, 1985.
- [3] N. Alon and J. H. Spencer. The probabilistic method. Wiley-Interscience Series in Discrete Math. and Optimization. John Wiley & Sons Inc., Hoboken, NJ, third edition, 2008.
- [4] T. Austin. On exchangeable random variables and the statistics of large graphs and hypergraphs. Probab. Surv., 5:80–145, 2008.
- [5] M. Axenovich and R. Martin. A version of Szemer´edi’s regularity lemma for multicolored graphs and directed graphs that is suitable for induced graphs. arXiv:1106.2871.
- [6] J. Balogh, R. Morris, and W. Samotij. Independent sets in hypergraphs. J. Amer. Math. Soc., 28(3):669–709, 2015.
- [7] J. Balogh, R. Morris, and W. Samotij. The method of hypergraph containers. In Proceedings of the International Congress of Mathematicians—Rio de Janeiro 2018. Vol. 3, pages 3045–3078, 2018.
- [8] J. Balogh and A. Z. Wagner. Further applications of the container method. In Recent trends in combinatorics, volume 159 of IMA Vol. Math. Appl., pages 191–213. Springer, [Cham], 2016.


- [9] B. Bollob´as and A. Thomason. Projections of bodies and hereditary properties of hypergraphs. Bull. London Math. Soc., 27(5):417–424, 1995.
- [10] F. R. K. Chung, R. L. Graham, P. Frankl, and J. B. Shearer. Some intersection theorems for ordered sets and graphs. J. Combin. Theory Ser. A, 43(1):23–37, 1986.
- [11] D. Conlon and J. Fox. Bounds for graph regularity and removal lemmas. Geom. Funct. Anal., 22(5):1191–1256, 2012.
- [12] P. Corazza. Introduction to metric-preserving functions. Amer. Math. Monthly, 106(4):309–323, 1999.
- [13] I. Csisza´r. A note on Jensen’s inequality. Studia Sci. Math. Hungar., 1:185–188, 1966.
- [14] B. de Finetti. La probabilita` e la statistica nei rapporti con l’induzione, secondo i diversi punti di vista. In Induzione e statistica Lectures given at a Summer School of the Centro Internazionale Matematico Estivo (C.I.M.E.) held in Varenna (Como), Italy, June 1-10, 1959, pages 1–122. Springer, 1959. English translation in: B. de Finetti, Probability, induction and statistics. The art of guessing. John Wiley & Sons, London-New York-Sydney, 1972, chapter 9.
- [15] D. Ellis, E. Friedgut, G. Kindler, and A. Yehudayoﬀ. Geometric stability via information theory. Discrete Anal., pages Paper No. 10, 29, 2016.
- [16] P. Erdo˝s, P. Frankl, and V. Ro¨dl. The asymptotic number of graphs not containing a ﬁxed subgraph and a problem for hypergraphs having no exponent. Graphs Combin., 2(2):113–121, 1986.
- [17] P. Erdo˝s, D. J. Kleitman, and B. L. Rothschild. Asymptotic enumeration of

Kn-free graphs. In Colloquio Internazionale sulle Teorie Combinatorie (Rome, 1973), Tomo II, pages 19–27. Atti dei Convegni Lincei, No. 17. Accad. Naz. Lincei, Rome, 1976.

- [18] P. Erdo˝s and L. Lov´asz. Problems and results on 3-chromatic hypergraphs and some related questions. In Inﬁnite and ﬁnite sets (Colloq., Keszthely, 1973; dedicated to P. Erdo˝s on his 60th birthday), Vol. II, pages 609–627. NorthHolland, Amsterdam, 1975.
- [19] A. Frieze and R. Kannan. The regularity lemma and approximation schemes for dense problems. In 37th Annual Symposium on Foundations of Computer Science (Burlington, VT, 1996), pages 12–20. IEEE Comput. Soc. Press, Los Alamitos, CA, 1996.
- [20] A. Frieze and R. Kannan. Quick approximation to matrices and applications. Combinatorica, 19(2):175–220, 1999.
- [21] Z. F¨uredi and M. Simonovits. The history of degenerate (bipartite) extremal graph problems. In Erdo¨s centennial, volume 25 of Bolyai Soc. Math. Stud., pages 169–264. J´anos Bolyai Math. Soc., Budapest, 2013.
- [22] T. E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc., 56:13–20, 1960.
- [23] D. N. Hoover. Row-column exchangeability and a generalized model for probability. In Exchangeability in probability and statistics (Rome, 1981), pages 281–291. North-Holland, Amsterdam, 1982.
- [24] O. Kallenberg. On the representation theorem for exchangeable arrays. J. Multivariate Anal., 30(1):137–154, 1989.
- [25] J. H. B. Kemperman. On the optimum rate of transmitting information. Ann. Math. Statist., 40:2156–2177, 1969.


- [26] J. Koml´os and M. Simonovits. Szemer´edi’s regularity lemma and its applications in graph theory. In Combinatorics, Paul Erdo˝s is eighty, Vol. 2 (Keszthely, 1993), volume 2 of Bolyai Soc. Math. Stud., pages 295–352. J´anos Bolyai Math. Soc., Budapest, 1996.
- [27] T. K˝ova´ri, V. T. So´s, and P. Tur´an. On a problem of K. Zarankiewicz. Colloquium Math., 3:50–57, 1954.
- [28] G. Kozma and W. Samotij. Lower tails via relative entropy. arXiv:2104.04850.
- [29] S. Kullback. A lower bound for discrimination information in terms of variation. IEEE Transactions on Information Theory, 13:126–127, 1967.
- [30] L. H. Loomis and H. Whitney. An inequality related to the isoperimetric inequality. Bull. Amer. Math. Soc, 55:961–962, 1949.
- [31] L. Lov´asz and B. Szegedy. Szemer´edi’s lemma for the analyst. Geom. Funct. Anal., 17(1):252–270, 2007.
- [32] V. Mascioni. On the probability that ﬁnite spaces with random distances are metric spaces. Discrete Math., 300(1-3):129–138, 2005.
- [33] R. Morris, W. Samotij, and D. Saxton. An asymmetric container lemma and the structure of graphs with no induced 4-cycle. arXiv:1806.03706.
- [34] D. Mubayi and C. Terry. Discrete metric spaces: structure, enumeration, and 0-1 laws. The Journal of Symbolic Logic, 84(4):1293–1325, 2019.
- [35] M. S. Pinsker. Information and information stability of random variables and processes. Translated and edited by Amiel Feinstein. Holden-Day, Inc., San Francisco, Calif.-London-Amsterdam, 1964.
- [36] D. Saxton and A. Thomason. Hypergraph containers. Invent. Math., 201(3):925–992, 2015.
- [37] E. Szemer´edi. Regular partitions of graphs. In Proble`mes combinatoires et the´orie des graphes (Colloq. Internat. CNRS, Univ. Orsay, Orsay, 1976), volume 260 of Colloq. Internat. CNRS, pages 399–401. CNRS, Paris, 1978.
- [38] T. Tao. Szemer´edi’s regularity lemma revisited. Contrib. Discrete Math., 1(1):8–28, 2006.
- [39] A. M. Vershik. Random metric spaces and universality. Uspekhi Mat. Nauk, 59(2(356)):65–104, 2004.


Department of Mathematics, the Weizmann Institute of Science,

Rehovot 76100, Israel Email address: gady.kozma@weizmann.ac.il Department of Mathematics, Ben Gurion University of the Negev,

Be’er Sheva 8410501, Israel Email address: mtom@bgu.ac.il URL: http://www.math.bgu.ac.il/~mtom

School of Mathematical Sciences, Tel Aviv University, Tel Aviv

6997801, Israel Email address: peledron@tauex.tau.ac.il URL: http://www.math.tau.ac.il/~peledron

School of Mathematical Sciences, Tel Aviv University, Tel Aviv

6997801, Israel Email address: samotij@tauex.tau.ac.il URL: http://www.math.tau.ac.il/~samotij

