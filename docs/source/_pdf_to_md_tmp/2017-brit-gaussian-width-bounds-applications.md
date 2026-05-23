arXiv:1711.05624v3[math.CO]18Oct2018

GAUSSIAN WIDTH BOUNDS WITH APPLICATIONS TO ARITHMETIC PROGRESSIONS IN RANDOM SETTINGS

JOP BRIET¨ AND SIVAKANTH GOPI

Abstract. Motivated by a problem on random diﬀerences in Szemer´edi’s theorem and another problem on large deviations for arithmetic progressions in random sets, we prove upper bounds on the Gaussian width of special point sets in Rk. The point sets are formed by the image of the n-dimensional Boolean hypercube under a mapping ψ : Rn → Rk, where each coordinate is a constant-degree multilinear polynomial with 0-1 coeﬃcients. We show the following applications of our bounds. Let [Z/NZ]p be the random subset of Z/NZ containing each element independently with probability p.

- • A set D ⊆ Z/NZ is ℓ-intersective if any dense subset of Z/NZ contains a proper (ℓ+1)term arithmetic progression with common diﬀerence in D. Our main result implies

that [Z/NZ]p is ℓ-intersective with probability 1−o(1) provided p ≥ ω(N−β

ℓ

log N) for βℓ = (⌈(ℓ + 1)/2⌉)−1. This gives a polynomial improvement for all ℓ ≥ 3 of a previous bound due to Frantzikinakis, Lesigne and Wierdl, and reproves more directly the same improvement shown recently by the authors and Dvir (here we avoid the theories of locally decodable codes and quantum information).

- • Let Xk be the number of k-term arithmetic progressions in [Z/NZ]p and consider the large deviation rate ρk(δ) = log Pr[Xk ≥ (1 + δ)EXk]. We give quadratic improvements of the best-known range of p for which a highly precise estimate of ρk(δ) due to Bhattacharya, Ganguly, Shao and Zhao is valid for all odd k ≥ 5. In particular, the


estimate holds if p ≥ ω(N−c

log N) for ck = (6k⌈(k − 1)/2⌉)−1.

k

We also discuss connections with locally decodable codes and the Banach-space notion of type for injective tensor products of ℓp-spaces.

1. Introduction

The Gaussian width of a point set T ⊆ Rk measures the expected maximum correlation between T and a standard Gaussian vector g = N(0, Ik), and is given by

GW(T) = E sup

x, g .

x∈T

The terminology reﬂects the fact that the Gaussian width of a set is proportional to √k times its average width in a random direction. While this quantity plays a central role in highdimensional probability, it is notoriously hard to estimate in general; see for instance [Tal14] for an extensive discussion of this problem.

![image 1](<2017-brit-gaussian-width-bounds-applications_images/imageFile1.png>)

Our main result gives upper bounds on the Gaussian width of sets that appear naturally in the context of probabilistic combinatorics. The relevant sets are given by the image of

![image 2](<2017-brit-gaussian-width-bounds-applications_images/imageFile2.png>)

J.B. was supported by VENI grant 639.071.409 and the Gravitation-grant NETWORKS-024.002.003 from the Netherlands Organisation for Scientiﬁc Research (NWO).

S.G. was supported by NSF CAREER award 1451191 and NSF grant CCF-1523816.

the n-dimensional Boolean hypercube under a certain polynomial mapping ψ : Rn → Rk. In particular, we focus on the case where each coordinate ψi : Rn → R is a multilinear polynomial with 0-1 coeﬃcients. Say that a polynomial has multiplicity t if each of its variables has a nonzero exponent in at most t monomials in its support.1

- Theorem 1.1. Let ψ : Rn → Rk be a polynomial mapping such that each coordinate is multilinear, has 0-1 coeﬃcients, and has degree at most d and multiplicity t. Then,


![image 3](<2017-brit-gaussian-width-bounds-applications_images/imageFile3.png>)

1

GW ψ({0, 1}n) d nt kn1−

⌈d/2⌉ log n.

![image 4](<2017-brit-gaussian-width-bounds-applications_images/imageFile4.png>)

The factor nt can be seen as a natural scaling due to the fact that each coordinate ψi maps the Boolean hypercube into [0, nt] (which follows from a handshaking lemma). In the special case where ψ is linear, ψ(x) = ( c1, x , . . ., ck, x ), for some c1, . . ., ck ∈ {0, 1}n, the set ψ({0, 1}n) is easily seen to be contained in the set T = {( ci, y )ki=1 : y ℓ

∞ ≤ 1}. The Gaussian width of the former set is thus at most that of the latter, which in turn is at most

k

√

![image 5](<2017-brit-gaussian-width-bounds-applications_images/imageFile5.png>)

n

gici

k,

E

ℓ1

i=1

- as the sum is an n-dimensional Gaussian vector whose coordinates have variance at most k. Perhaps surprisingly, Theorem 1.1 shows that if ψ is quadratic and has constant multiplicity, then the Gaussian width is at most a factor √log n larger than the above upper bound. This turns out to be an easy consequence of a 1974 random matrix inequality due to Tomczak– Jeagermann [TJ74], which also forms the basis for our proof of the higher-degree cases. The proof of Theorem 1.1 (given in Section 2) proceeds in two steps: ﬁrst we reduce to the case of homogeneous mappings of even degree, and then we reduce to the quadratic case. The ﬁrst step is the reason for the ceiling in ⌈d/2⌉ appearing in the exponent of n and it would be interesting to know if one can remove this ceiling; i.e., does the result hold with the exponent 1 − 2/d? More generally, an exponent of the form o(1) for constant d would imply the truth of some unresolved conjectures on variants of Szemer´edi’s theorem, large deviations and coding theory (topics which we discuss below). The link to coding theory also implies that the bound is optimal for d = 2 and that the smallest possible exponent is

![image 6](<2017-brit-gaussian-width-bounds-applications_images/imageFile6.png>)

- at least (log log n)2−o(1)/ log n for d = 3 and (log log n)r−o(1)/ log n for d = 2r, r ≥ 3. Finally, a close inspection of the proof of Theorem 1.1 shows that it also holds for polynomials with non-negative integer coeﬃcients, for a suitable change of the deﬁnition of multiplicity. In the following four subsections we discuss two applications of this result and links with error correcting codes and the Banach space notion of type.


- 1.1. Random diﬀerences in Szemere´di’s Theorem. In 1975 Szemer´edi [Sze75] proved that any subset of the integers of positive upper density contains arbitrarily long arithmetic progressions, answering a famous open question of Erd˝os and Tura´n. It is well known that this is equivalent to the assertion that for every positive integer k and any α ∈ (0, 1),


there exists an N0(k, α) ∈ N such that if N ≥ N0(k, α) and A ⊆ Z/NZ is a set of size |A| ≥ αN, then A must contain a proper k-term arithmetic progression. Certain reﬁnements of Szemer´edi’s theorem concern sets D ⊆ N for which the theorem still holds true when the arithmetic progressions are required to have common diﬀerence from D. Such sets are usually

![image 7](<2017-brit-gaussian-width-bounds-applications_images/imageFile7.png>)

1 Here and below, , denote upper and lower bounds up-to absolute constants and ε, ε denote upper and lower bounds up-to constants depending on a parameter ε.

referred to as intersective sets in number theory, or recurrent sets in ergodic theory. More precisely, a set D ⊆ N is ℓ-intersective (or ℓ-recurrent) if any set A ⊆ N of positive upper density has an (ℓ+1)-term arithmetic progression with common diﬀerence in D. Szemer´edi’s theorem then states that N is ℓ-intersective for every ℓ ∈ N, but much smaller intersective sets exist. For example, for any t ∈ N, the set {1t, 2t, 3t, . . .} is ℓ-intersective for every ℓ, which is a special case of more general results of S´ark¨ozy [S´ar78a] when ℓ = 1 and of Bergelson and Leibman [BL96] for all ℓ ≥ 1. The shifted primes {p−1 : p is prime} and {p+1 : p is prime} are also ℓ-intersective for every ℓ ∈ N, shown by S´ark¨ozy [S´ar78b] when ℓ = 1 and in a more general setting by Wooley and Ziegler [WZ12] for all ℓ ≥ 1.

It is natural to ask at what density, random sets become ℓ-intersective. To simplify the discussion, we will look at the analogous question in Z/NZ.

Deﬁnition 1.2. Let ℓ be a positive integer and α ∈ (0, 1]. A subset D ⊆ Z/NZ is (ℓ, α)intersective if any subset A ⊆ Z/NZ of size |A| ≥ αN contains a proper (ℓ + 1)-term arithmetic progression with common diﬀerence in D.

It was proved independently by Frantzikinakis et al. [FLW12] and Christ [Chr11] that for βℓ = 2 1

and p ≥ ω(N−βℓ log N), the random set [Z/NZ]p is (ℓ, α)-intersective with probability 1 − o(1), provided N ≥ N1(ℓ, α). This was improved for all ℓ ≥ 4 in [FLW16], where it was shown that the same result holds with βℓ = ℓ+11 , though it was conjectured there that βℓ = 1 suﬃces for all ℓ ≥ 1. Based on Theorem 1.1 we obtain the following result, which improves on these bounds for all ℓ ≥ 3.

![image 8](<2017-brit-gaussian-width-bounds-applications_images/imageFile8.png>)

ℓ−1

![image 9](<2017-brit-gaussian-width-bounds-applications_images/imageFile9.png>)

- Theorem 1.3. For every ℓ ∈ N and α ∈ (0, 1), there exists an N1(ℓ, α) ∈ N such that the following holds. Let N ≥ N1(ℓ, α) be an integer and let


1 ⌈ℓ+12 ⌉

and p ≥ ω(N−β

log N).

βℓ =

ℓ

![image 10](<2017-brit-gaussian-width-bounds-applications_images/imageFile10.png>)

![image 11](<2017-brit-gaussian-width-bounds-applications_images/imageFile11.png>)

Then, with probability 1 − o(1), the set [Z/NZ]p is (ℓ, α)-intersective.

- 1.2. Large deviations for arithmetic progressions. Let H = (V, E) be a hypergraph


over a ﬁnite vertex set V of cardinality N and for p ∈ (0, 1) denote by Vp the random binomial subset where each element of V appears independently of all others with probability p. Let X be the number of edges in H that are induced by Vp. Important instances of the random variable X include the count of triangles in an Erd˝os–R´enyi random graph and the count of arithmetic progressions of a given length in the random set [Z/NZ]p.

The study of the asymptotic behavior of X when p = p(N) is allowed to depend on N and N grows to inﬁnity motivates a large body of research in probabilistic combinatorics. Of particular interest is the problem of determining the probability that X signiﬁcantly exceeds its expectation Pr[X ≥ (1 + δ)EX] for δ > 0, referred to as the upper tail. Despite the fact that standard probabilistic methods fail to give satisfactory bounds on the upper tail in general, advances were made recently for special instances, in particular for triangle counts [LZ17] and general subgraph counts [BGLZ17]. For more general hypergraphs, progress was made by Chatterjee and Dembo [CD16] using a novel nonlinear large deviation principle (LDP), which was improved by Eldan [Eld18] shortly after. The LDPs give precise estimates on the upper tail that are given in terms of a parameter φp whose value is determined by the solution to a certain variational problem. The range of values of p for which these estimates are actually valid depends on the underlying hypergraph H. This splits

the problem of estimating the upper tail into two sub-problems: (1) determining for what range of p the estimate in terms of φp holds true and (2) solving the variational problem to determine the value of φp. The answer to problem (1) turns out to depend on the Gaussian width of a point set related to H.

This approach was pursued in [CD16] to estimate the upper tail of the number of 3-term arithmetic progressions in [Z/NZ]p, for which the authors solved problem (1). The case of longer APs, asking for the upper tail probability of the count Xk of k-term arithmetic progressions in [Z/NZ]p, was recently treated by Bhattacharya et al. [BGSZ18]. They solved the variational problem (2) for N prime and gave bounds for the relevant Gaussian width towards solving problem (1). Based on this, they showed that if k ≥ 3 and δ > 0 are ﬁxed and p tends to zero suﬃciently slowly as N → ∞ along the primes, then

√

δpk/2N.

![image 12](<2017-brit-gaussian-width-bounds-applications_images/imageFile12.png>)

- (1) Pr[Xk ≥ (1 + δ)EXk] = p(1+o(1))


Similar results were shown for the analogous problem over {1, . . ., N} (in which case N no longer needs to be prime), but we shall focus on the problem in Z/NZ for ease of exposition. The rate at which p is allowed to decay for (1) to hold turns out to depend on Gaussian widths of the form featuring in Theorem 1.1. The bounds proved in [BGSZ18] imply that (1) holds provided p ≥ N−ck(log N)εk for

1 18

1 48

1 6k(k − 1)

c3 =

, c4 =

and ck =

for k ≥ 5,

![image 13](<2017-brit-gaussian-width-bounds-applications_images/imageFile13.png>)

![image 14](<2017-brit-gaussian-width-bounds-applications_images/imageFile14.png>)

![image 15](<2017-brit-gaussian-width-bounds-applications_images/imageFile15.png>)

and absolute constants εk ∈ (0, ∞) depending only on k. However, the authors conjecture that a probability p slightly larger than N−1/(k−1) suﬃces for all k. Some support for this conjecture is given by a result of Warnke [War17] showing that for all p ≥ (log N/N)1/(k−1), the logarithm of the upper tail (also referred to as the large deviation rate) of the k-AP count in {1, . . ., N}p is given by Θk(√δpk/2N log p), where the asymptotic notation hides constants depending only on k. Notice that (1) is more accurate than this result in that it (almost) determines those constants, though currently for a more narrow range of p.2 Using

![image 16](<2017-brit-gaussian-width-bounds-applications_images/imageFile16.png>)

- Theorem 1.1, we widen the range of p for which (1) can be shown to hold for all k ≥ 5.


- Theorem 1.4. For every integer k ≥ 3 and


1 6k k−21

ck =

, the estimate (1) holds true, provided p ≥ N−c

![image 17](<2017-brit-gaussian-width-bounds-applications_images/imageFile17.png>)

![image 18](<2017-brit-gaussian-width-bounds-applications_images/imageFile18.png>)

(log N) and N is prime.

k

- 1.3. Locally decodable codes. There is a close connection between the Gaussian widths considered in Theorem 1.1 and special error-correcting codes called locally decodable codes (LDCs). A map C : {0, 1}k → {0, 1}n is a q-query LDC if for every i ∈ [k] and x ∈ {0, 1}k,


the value xi can be retrieved by reading at most q coordinates of the codeword C(x), even if the codeword is corrupted in a not too large (but possibly constant) fraction of coordinates. A main open problem is to determine the smallest possible codeword length n as a function of the message length k, when q is a ﬁxed constant. Currently this problem is settled only in the cases q = 1, 2 [KT00, KW04, GKST06] and remains wide open for the case q = 3. We

![image 19](<2017-brit-gaussian-width-bounds-applications_images/imageFile19.png>)

2The main motivation for ﬁnding such precise estimates of the upper tail probability is not so much the problem itself as it is to understand structure of the set [Z/NZ]p conditioned on Xk being much larger than its expectation (see [BGSZ18]).

refer to the extensive survey [Yek12] for more information on this problem. A connection with Gaussian width was established by the authors and Dvir in [BDG17], where we show that q-query LDCs from {0, 1}Ω(k) to {0, 1}O(n) are equivalent to mappings ψ : Rn → Rk whose coordinates are degree-q, multiplicity-1 polynomials with 0-1 coeﬃcients that are supported by Ω(n) monomials, and such that the set ψ({0, 1}n) has Gaussian width Ω(k). It was observed there that the best-known lower bounds on the length n = n(k) of q-query LDCs—proved using techniques from quantum information theory [KW04]—imply a slightly diﬀerent but equivalent version of Theorem 1.3 (see Section 5). The proof of Theorem 1.1 is based on ideas from [KW04], but does not use quantum information theory.3

- 1.4. Gaussian width bounds from type constants. We observe that the Gaussian width in Theorem 1.1 can be bounded in terms of type constants of certain Banach spaces. Unfortunately, we do not have good enough bounds on the type constants of the required spaces to improve Theorem 1.1. But we hope that this connection will motivate progress on understanding these spaces.


A Banach space X is said to have (Rademacher) type p > 0 if there exists a constant T < ∞ such that for every k and x1, . . ., xk ∈ X,

k

k

p X

xi pX ,

≤ Tp

εixi

- (2) Eε


i=1

i=1

where the expectation is over a uniformly random ε = (ε1, . . ., εk) ∈ {−1, 1}k. The smallest T for which (2) holds is referred to as the type-p constant of X, denoted Tp(X). Type, and its dual notion cotype, play an important role in Banach space theory as they are tightly linked to local geometric properties (we refer to [LT79] and [Mau03] for extensive surveys). Some fundamental facts are as follows. It follows from the triangle inequality that every Banach space has type 1 and from the Kahane–Khintchine inequality that no Banach space has type p > 2. The parallelogram law implies that Hilbert spaces have type 2. An easy but important fact is that ℓ1 fails to have type p > 1. Indeed, a famous result of Maurey and Pisier [MP73] asserts that a Banach space fails to have type p > 1 if and only if it contains ℓ1 uniformly. Finite-dimensional Banach spaces have type-p for all p ∈ [1, 2].

Of importance to Theorem 1.1 are the actual type constants Tp(X) of a certain family of ﬁnite-dimensional Banach spaces. Let r1, . . ., rd ≥ 1 be such that di=1 r1

= 1 and let Lnr1,...,rd be the space of d-linear forms on Rn × · · · × Rn (d times) endowed with the norm

![image 20](<2017-brit-gaussian-width-bounds-applications_images/imageFile20.png>)

i

Λ = sup |Λ(x1, . . ., xd)| x1 ℓ

: x1, . . ., xd ∈ Rn \ {0} .

![image 21](<2017-brit-gaussian-width-bounds-applications_images/imageFile21.png>)

· · · xd ℓ

rd

r1

for ri−1 + s−i 1 = 1 and

This space is also known as the injective tensor product of ℓns

, . . ., ℓns

1

d

- as such plays an important role in the theory of tensor products of Banach spaces [Rya02]. The relevance of the type constants of this space to Theorem 1.1 is captured by the following lemma, proved in Section 7.


- Lemma 1.5. Let ψ : Rn → Rk be a polynomial mapping such that each coordinate is multilinear and has 0-1 coeﬃcients, degree at most d and multiplicity t. Then for any


![image 22](<2017-brit-gaussian-width-bounds-applications_images/imageFile22.png>)

3Not surprisingly, the LDC lower bounds of [KW04] are also implied by Theorem 1.1.

r1, . . ., rd ≥ 1 such that di=1 r1

= 1 and any p ∈ [1, 2], GW ψ({0, 1}n) d ntTp(Lnr1,...,rd) k1/p.

![image 23](<2017-brit-gaussian-width-bounds-applications_images/imageFile23.png>)

i

Observe that the space Ln2,2 may be identiﬁed with the space of n × n matrices endowed with the spectral norm (or operator norm). A key ingredient in the proof of Theorem 1.1,

- Theorem 2.1 below, easily implies that the type-2 constant of this space is of order O(√log n). A well-known lower bound of the same order follows for instance from the connection between Gaussian width and LDCs and a basic construction of a 2-query LDC known as the

![image 24](<2017-brit-gaussian-width-bounds-applications_images/imageFile24.png>)

Hadamard code. More generally, lower bounds on the type constants of Lnr1,...,rd are implied by d-query LDCs [BNR12, Bri16].

2. Proof of Theorem 1.1

In this section we prove Theorem 1.1. We begin by giving a high-level overview of the ideas. The main tool we use is the following random matrix inequality, which is a special case of a non-commutative version of the Khintchine inequality due to Tomczak-Jaegermann [TJ74,

- Theorem 3.1]. Let  ·, ·  be the standard inner product on RN and denote by B2N the Euclidean unit ball in RN. Given a matrix A ∈ RN×N, its operator norm (or spectral norm) is given by A = sup{| Ax, y | : x, y ∈ B2N}.


- Theorem 2.1 (Tomczak-Jaegermann). There exists an absolute constant C ∈ (0, ∞) such


that the following holds. Let A1, . . ., Ak ∈ RN×N be a collection of matrices and let g1, . . ., gk be independent Gaussian random variables with mean zero and variance 1. Then,

E

k

![image 25](<2017-brit-gaussian-width-bounds-applications_images/imageFile25.png>)

giAi ≤ C log N

i=1

k

i=1

Ai 2

1/2

.

This result already suﬃces to prove Theorem 1.1 when the coordinate mappings ψi are quadratic forms, in which case there exist matrices Ai ∈ {0, 1}n×n such that ψi(x) = Aix, x . The assumption that each ψi has multiplicity t implies that each row and column of Ai has

- at most t ones. This in turn implies that Ai ≤ t by a Birkhoﬀ-von Neumann-type theorem. Since each x ∈ {0, 1}n has Euclidean norm at most √n, we get


![image 26](<2017-brit-gaussian-width-bounds-applications_images/imageFile26.png>)

k

GW ψ({0, 1}n) = E max

gi Aix, x

x∈{0,1}n

i=1

k

k

giAi . By Theorem 2.1, the above is at most Ctn√k log n.

giAi x, x ≤ nE

= E max

x∈{0,1}n

i=1

i=1

![image 27](<2017-brit-gaussian-width-bounds-applications_images/imageFile27.png>)

The general case is proved via a reduction to the above quadratic case and consists of two steps. In the ﬁrst step, we reduce to the case where each coordinate ψi is a homogeneous polynomial of degree 2⌈d/2⌉. This is done in a straightforward way by adding at most dn variables in such a way so as to preserve the multiplicity. The second step consists of a reduction to the quadratic case. For this, it will be convenient to consider the hypergraphs associated with the monomial support of the coordinate mappings ψi.

Recall that an d-hypergraph H = (V, E) consists of a vertex set V and a multiset E, also denoted E(H), of subsets of V of size at most d, called the edges. A hypergraph is d-uniform

if each edge has size exactly d. The degree of a vertex is the number of edges containing it and the degree of H, denoted ∆(H), is the maximum degree among its vertices. A matching is a hypergraph where no two edges intersect. Associate with a hypergraph H = ([n], E), the multilinear polynomial pH ∈ R[x1, . . ., xn] given by

- (3) pH(x1, . . ., xn) =


xi.

e∈E i∈e

The multiplicity of pH is then exactly the degree ∆(H). Clearly the coordinate mappings ψi of the form featuring in Theorem 1.1 can be written as pH for some d-hypergraph H of degree at most t. The reduction to the quadratic case is based on the following key lemma, in which for x ∈ Rn and m ∈ N, the the mth tensor power x is deﬁned as x⊗m = ( mi=1 xu

)u∈[n]m.

i

- Lemma 2.2 (Matrix lemma). For every r ∈ N there exist a Cr, cr ∈ (0, ∞) and n0(r) ∈ N such that the following holds. Let n ≥ n0(r), m = Crn1−1/r and N = nm. Let H = ([n], E) be a 2r-uniform hypergraph and let pH be the polynomial as in (3). Then, there exists a matrix A ∈ RN×N such that A r ∆(H) and for every x ∈ {−1, 1}n,


n crN

Ax⊗m, x⊗m . Moreover, A is the adjacency matrix of a graph (with possible parallel edges).

pH(x) =

![image 28](<2017-brit-gaussian-width-bounds-applications_images/imageFile28.png>)

Remark 2.3. We do not know if the value of m in Lemma 2.2 is optimal. More generally, a better bound in Theorem 1.1 would follow if, for any ﬁxed hypergraphs H1, . . ., Hk as in the lemma, there exist N ≤ o(nm), matrices A1, . . ., Ak ∈ RN×N with Ai r ∆(Hi) and a map f : {−1, 1}n → {y ∈ RN : y 2 ≤

√N} such that pH

![image 29](<2017-brit-gaussian-width-bounds-applications_images/imageFile29.png>)

(x) = (n/crN) Aif(x), f(x) for every i ∈ [k] and x ∈ {−1, 1}n.

i

With this lemma in hand, the proof of Theorem 1.1 is straightforward (see below). The idea behind Lemma 2.2 is to use decompositions into matchings and a generalization of the Birthday Paradox that says that for any n-vertex 2r-matching, a random subset of Crn1−1/r vertices contains r vertices of any ﬁxed edge with probability cr/n. To illustrate how this is used in the r = 2 case, let H be a 4-matching, let m = C2√n and N = nm. It follows from the generalized Birthday Paradox that there are c2N/n strings in [n]m containing at least two elements of a given edge. Now let G be the graph with vertex set [n]m whose edges are the pairs {u, v} that cover some edge in H and complement each other, meaning: there are indices i, j ∈ [m] such that {ui, uj, vi, vj} ∈ E(H) and uℓ = vℓ for all ℓ  ∈ {i, j}. The main observation is that for every edge {u, v} ∈ E(G) that covers an edge e ∈ E(H) and every x ∈ {−1, 1}n, we have

![image 30](<2017-brit-gaussian-width-bounds-applications_images/imageFile30.png>)

m

(x⊗m)u(x⊗m)v =

xu

xv

xw.

= xu

xu

xv

xv

=

i

j

i

j

ℓ

ℓ

w∈e

ℓ=1

It follows that, modulo the relations x21 = 1, . . ., x2n = 1, we have pG(x⊗m) = (c2N/n)pH(x). The (appropriately scaled) adjacency matrix of G then satisﬁes the second criterion of the lemma, but it will have large norm if G has high degree. To obtain a matrix with the desired norm, we consider a pruned version of G in which we keep only edges that do not cover too many edges of H (at the cost of only a constant-factor decrease of the constant c2).

We now give the formal proof of Theorem 1.1. The following simple proposition is used for the ﬁrst step, in which we homogenize the polynomials. Given two hypergraphs H, H′, say that H′ majorizes H if V (H) ⊆ V (H′) and if for each edge e ∈ E(H), there is a unique edge e′ ∈ E(H′) such that e ⊆ e′.

- Proposition 2.4. For any n-vertex d-hypergraph H, there is a d-uniform hypergraph H′ on dn vertices that majorizes H and satisﬁes ∆(H′) = ∆(H).


Proof: Let t = ∆(H). It follows from the handshaking lemma that |E(H)| ≤ tn. Partition E(H) = {E1, . . ., En} into n pairwise disjoint sets of size at most t each. Add to V (H) pairwise disjoint sets W1, . . ., Wn of d − 1 new vertices each. For each i ∈ [n], complete each edge e ∈ Ei to a set of size d by adding vertices from Wi and let H′ be the hypergraph thus obtained. Observe that we have not increased the degree of the vertices in V (H). Since each Ei has size at most t, the new vertices in Wi also have degree at most t and therefore, ∆(H′) = t. It is trivial to verify that H′ satisﬁes the other desired properties. ✷

Proof of Theorem 1.1: Let r = ⌈d/2⌉ and for each i ∈ [k], let Hi be the d-hypergraph of degree t such that ψi = pH

as in (3). Assume that n ≥ n0(r) for n0(r) as in at most t. To this end, let H′

, with pH

i

i

- Lemma 2.2. We start by reducing to the setting where each Hi is 2r-uniform and of degree


i = ([n] ∪ [(2r − 1)n], E′

i) be a 2r-uniform hypergraph that majorizes Hi as in Proposition 2.4, which exists since any d-hypergraph is a 2r-hypergraph. Then, for each e ∈ E(Hi), there is a unique set f(e) ⊆ [(2r−1)n] such that e∪f(e) ∈ E(H′

i). It follows that

pH

(x) =

xi =

xi

i

e∈E(Hi) i∈e

e∈E(Hi) i∈e

((x, 1)),

1 = pH′

i

j∈f(e)

where 1 ∈ R(2r−1)n is the all-ones vector. Hence, if we let ψ′ : R2rn → Rk be the polynomial map whose coeﬃcients are given by pH′

, then GW ψ({0, 1}n) ≤ GW ψ′({0, 1}2rn) .

i

Since the dependence of our claimed bound on the Gaussian width is polynomial in n, the extra vertices will result in an extra factor depending only on d. It thus suﬃces to prove the theorem for the case where H1, . . ., Hk are 2r-uniform.

Observe that since the polynomials ψi are multilinear, the Gaussian width is bounded from above by replacing binary vectors with sign vectors. In particular,

GW ψ({0, 1}n) ≤ Emax

k

(x) : x ∈ {−1, 1}n .

gipH

i

i=1

Let m = Crn1−1/r and N = nm and for each i ∈ [k], let Ai ∈ RN×N be a matrix for pH

as in Lemma 2.2. Then, for every x ∈ {−1, 1}n,

i

k

k

n

n crN

n cr

gi Aix⊗m, x⊗m ≤

gipH

(x) =

giAi ,

![image 31](<2017-brit-gaussian-width-bounds-applications_images/imageFile31.png>)

![image 32](<2017-brit-gaussian-width-bounds-applications_images/imageFile32.png>)

i

i=1

i=1

i=1

where in the inequality we used that x⊗m has Euclidean norm √N. Taking expectations, it then follows from Theorem 2.1 that the Gaussian width of ψ({0, 1}n) is at most

![image 33](<2017-brit-gaussian-width-bounds-applications_images/imageFile33.png>)

k

k

n cr

n cr

1/2

![image 34](<2017-brit-gaussian-width-bounds-applications_images/imageFile34.png>)

![image 35](<2017-brit-gaussian-width-bounds-applications_images/imageFile35.png>)

Ai 2

r nt kn1−1/r log n,

log N

giAi

E

![image 36](<2017-brit-gaussian-width-bounds-applications_images/imageFile36.png>)

![image 37](<2017-brit-gaussian-width-bounds-applications_images/imageFile37.png>)

i=1

i=1

where in the second inequality we used that Ai ≤ Or(t) for each i ∈ [k]. ✷

3. Proof of the matrix lemma

In this section we prove Lemma 2.2. The starting point is a decomposition of a boundeddegree hypergraph into a small number of matchings. For this, we use the following basic result on edge colorings. The edge chromatic number of a hypergraph H, denoted by χE(H), is the minimum number of colors needed to color the edges of H such that no two edges which intersect have the same color. Note that χE(H) equals the smallest number of matchings into which E(H) can be partitioned.

- Lemma 3.1. Let H be a d-hypergraph. Then, ∆(H) ≤ χE(H) ≤ d(∆(H) − 1) + 1.


Proof: Clearly χE(H) ≥ ∆(H) since edges containing a maximum degree vertex should get diﬀerent colors. To prove the upper bound, form a graph G whose vertices are E(H), and add edges between intersecting hypergraph edges. Then χE(H) is equal to the vertex chromatic number of the graph G, which, by Brooks’ Theorem, is at most ∆(G) + 1. Since an edge in H can intersect at most d(∆(H) − 1) other edges, ∆(G) ≤ d(∆(H) − 1). ✷

To deal with matchings, we introduce the following deﬁnitions. Let M ⊆ [2nr] be a maximal 2r-matching of [n]. Let s = 200 · 4r. Given a string x ∈ {−1, 1}n write its m-fold tensor product as

m

x⊗m =

xf(i)

.

f:[m]→[n]

i=1

Given a mapping f : [m] → [n] and set S ∈ M, let µS(f) =

|f−1(i)|.

) i∈T

S r

T∈(

Note that this is a count of the r-subsets I ⊆ [m] such that |S ∩ f(I)| = r. Denote φ(f) =

µS(f).

S∈M

For ℓ ∈ N, say that f is ℓ-good if 1 ≤ φ(f) ≤ ℓ. Say that g : [m] → [n] complements f if it satisﬁes the following two criteria:

- (1) There exists exactly one I ∈ [mr] such that f(I) ∪ g(I) ∈ M.
- (2) For all i ∈ [m] I, we have g(i) = f(i).


If g complements f then clearly the converse also holds. Say that the complementary pair (f, g) covers S ∈ M if f(I) ∪ g(I) = S. Observe that if (f, g) covers S, then for every x ∈ {−1, 1}m, we have

- (4) (x⊗m)f(x⊗m)g =

m

i=1

xf(i)xg(i) =

j∈S

xj.

Deﬁne the set of ordered pairs

- (5) P = (f, g) : f is s-good and g complements f .


- Proposition 3.2. Let P be as in (5). Then, for every S ∈ M, the number of pairs (f, g) ∈ P that cover S equals |P|/|M|.


Proof: Fix distinct sets S, T ∈ M and let π ∈ Sn be a permutation such that π(S) = T, π(T) = S and π(i) = i for all i ∈/ S ∪ T. Let PS be the set of pairs (f, g) ∈ P which cover S and deﬁne PT similarly. We claim that the map ψ : (f, g)  → (π ◦ f, π ◦ g) is an injective map from PS to PT. It follows that T is covered by at least as many pairs from P

- as S is. Similarly, interchanging S and T, the converse also holds. To prove the claim, note that if (f, g) covers S, then (π ◦ f, π ◦ g) covers T. Moreover, φ(π ◦ f) = φ(f) because π


maps edges of the matching M to edges of M. Thus ψ(PS) ⊂ PT. Finally ψ is injective because if π ◦ f = π ◦ f′ for some f, f′ : [m] → [n], then f = f′. Hence P covers all S ∈ M equally. ✷

- Proposition 3.3. For every (f, g) ∈ P, we have that g is s2-good.


Proof: Let S ∈ M and (f, g) ∈ P be such that (f, g) covers S. Consider the histograms F, G : [n] → {0, 1, . . ., m} given by F(i) = |f−1(i)| and G(i) = |g−1(i)| for each i ∈ [n]. Then F and G diﬀer only in S. In particular, there is an r-set T ⊆ S such that G(i) = F(i)+1 for each i ∈ T and G(i) = F(i) − 1 for each i ∈ S T. Hence,

G(i)

µS(g) =

) i∈T

S r

T∈(

F(i) + 1

≤

) i∈T

S r

T∈(

1 + 2r

F(i)

≤

i∈T

S r

)

T∈(

≤ 4r + 2rµS(f).

For all other S′ ∈ M, we have µS′(g) = µS′(f). Moreover, f must be s-good for (f, g) to belong to P. It follows that

µS′(f) = 4r + 2rφ(f) ≤ s2,

µS′(g) ≤ 4r + 2r

φ(g) =

S′∈M

S′∈M

where in the last line we used the choice of s = 200 · 4r. ✷

- Lemma 3.4 (Generalized birthday paradox). For every r ∈ N there exists a Cr ∈ (0, ∞) and an n0(r) ∈ N such that the following holds. Let h be a uniformly distributed random


variable over the set of maps from [m] to [n]. Then, provided n ≥ n0(r) and m = Crn1−1/r, Pr h is s-good ≥

- 1

![image 38](<2017-brit-gaussian-width-bounds-applications_images/imageFile38.png>)

- 2


. We postpone the proof of Lemma 3.4 to Section 4.

Corollary 3.5. Let P be as in (5) and let A : [n]m × [n]m → {0, 1} be its incidence matrix, that is A(f, g) = 1 ⇐⇒ (f, g) ∈ P. Then, |P| ≥ Ω(N) and every row and every column of A has at most s2(r!) ones.

Proof: The ﬁrst claim follows from Lemma 3.4 and the fact that |P| is at least the number of s-good mappings. If h is l-good, then there are at most l(r!) mappings from [m] → [n] that complement h. Hence, every row of A has at most s(r!) ones and by Proposition 3.3, every column of A has at most s2(r!) ones. ✷

With this, we can now prove Lemma 2.2.

- Proof of Lemma 2.2: Let t = ∆(H). By Lemma 3.1, H can be decomposed into χE(H) ≤ 2rt


matchings, which we denote by F1, . . ., FχE(H). Complete each Fi to a maximal family Mi of disjoint 2r-subsets of [n] in some arbitrary way. For each Mi, let Pi be as in (5) and let Ai : [n]m × [n]m → {0, 1}n be its incidence matrix. Set to zero all the entries of Ai that correspond to a pair (f, g) covering a set in Mi Fi. Let B = A1 + · · · + Aχ

E(H) and A = (B + BT). It follows from (4) and Proposition 3.2 that for each x ∈ {−1, 1}n, we have

- (6)

χE(H)

i=1

(Ai + ATi )x⊗m, x⊗m = 2

χE(H)

i=1

|Pi| |Mi| S∈F

![image 39](<2017-brit-gaussian-width-bounds-applications_images/imageFile39.png>)

i j∈S

xi.

Since all Mi are maximal, they have the same size, as do the Pi. Hence, by Corollary 3.5, there exists a constant cr ∈ (0, 1] such that the right-hand side of (6) equals (2crN/n)pH(x). Let G be the graph with adjacency matrix A, allowing for parallel edges. Then G has degree

- at most 2ts2(r!). It follows from Lemma 3.1 that G can be partitioned into Or(t) matchings. Since the adjacency matrix of a matching has unit norm, we get that A ≤ Or(t). ✷


4. Proof of the generalized birthday paradox.

For the proof of Lemma 3.4, we use a standard Poisson approximation result for “balls and bins” problems [MU05, Theorem 5.10]. A discrete Poisson random variable Y with expectation µ is nonnegative, integer valued, and has probability density function

- (7) Pr[Y = ℓ] =


e−µµℓ ℓ!

, ∀ℓ = 0, 1, 2, . . .

![image 40](<2017-brit-gaussian-width-bounds-applications_images/imageFile40.png>)

- Proposition 4.1. If X, Y are independent Poisson random variables with expectations µX, µY , respectively, then X + Y is a Poisson random variable with expectation µX + µY .


- Lemma 4.2. Let h be a uniformly distributed map from [m] to [n]. For each i ∈ [n], let Xi = |h−1(i)| and let X = (Xi)i∈[n]. Let Y = (Yi)i∈[n] be a vector of independent Poisson random variables with expectation m/n. Then, for any nonnegative function Φ : (N ∪ {0})n → R+ such that E[Φ(X)] decreases or increases monotonically with m, we have


E[Φ(X)] ≤ 2E[Φ(Y)].

- Proof of Lemma 3.4: Let Cr > 0 be a parameter depending only on r to be set later. Let µ = Crm/n = Crn−1/r and assume that n ≥ n0(r) := 4(Crr)r. For h a random map as in


- Lemma 4.2, we begin by lower bounding the probability of the event that φ(h) ≥ 1. Recall


that this occurs if there exists an S ∈ M and an r-subset T ∈ Sr such that T ⊆ im(h). Let X be as in Lemma 4.2. Let ψ : (N ∪ {0})n → {0, 1} be the function

ψ(x) =

1 −

1≥1(xi) .

S∈M T∈(

i∈T

S r

)

Then ψ(X) = 1 if φ(h) = 0 and ψ(X) decreases monotonically with m. Hence, for Y a Poisson random vector as in Lemma 4.2, we have

Pr[φ(h) = 0] = E[ψ(X)] ≤ 2E[ψ(Y)]

= 2

- (8) 1≥1(Yi) ,

where in the last line we used the fact that since the sets S ∈ M are disjoint, the random variables

T∈(

S r

)

1 −

i∈T

1≥1(Yi)

are independent. The random variables 1≥1(Yi), i ∈ S, are independent Bernoullis that are zero with probability e−µ. The expectation in (8) equals the probability that these random variables form a string of Hamming weight strictly less than r. Using that n ≥ 4(Crr)r and the fact that 1 − x ≤ exp(−x) ≤ 1 − x + x2/2 when x > 0, this probability is at most

1 − Pr[∀i ∈ T 1≥1(Yi) = 1] = 1 − (1 − e−µ)r ≤ 1 − (µ(1 − µ/2))r ≤ 1 −

Crr en ≤ exp −

![image 41](<2017-brit-gaussian-width-bounds-applications_images/imageFile41.png>)

Crr en

![image 42](<2017-brit-gaussian-width-bounds-applications_images/imageFile42.png>)

where T ⊂ S is some ﬁxed subset of size r. Hence, since M is maximal, the above and (8) give

- (9) Pr[φ(h) = 0] ≤ 2 exp −


1 −

E

S∈M

i∈T

S r

)

T∈(

Crr⌊n/r⌋ en ≤ 2 exp −

Crr 2er

Crr|M| en ≤ 2 exp −

![image 43](<2017-brit-gaussian-width-bounds-applications_images/imageFile43.png>)

![image 44](<2017-brit-gaussian-width-bounds-applications_images/imageFile44.png>)

![image 45](<2017-brit-gaussian-width-bounds-applications_images/imageFile45.png>)

.

Set Cr = (6er)1/r, then the above right-hand side is at most 1/4. Next, we upper bound the probability that φ(h) ≥ s = 200 · 4r. Deﬁne χ : (N ∪ {0})n → R+ by

xi.

χ(x) =

) i∈T

S∈M T∈(

S r

Then, φ(h) = χ(X). Moreover, E[χ(X)] increases monotonically with m. It thus follows from Lemma 4.2 that

E[φ(h)] ≤ 2E[χ(Y)] = 2

S∈M T∈(

) i∈T

S r

- m

![image 46](<2017-brit-gaussian-width-bounds-applications_images/imageFile46.png>)

- n


2r r

≤ 2|M|

E[Yi]

n r · 4r · (6er)n−1 ≤ 50 · 4r.

r

≤ 2 ·

![image 47](<2017-brit-gaussian-width-bounds-applications_images/imageFile47.png>)

where in the second line we used the fact that the Yi are independent. By Markov’s inequality, Pr[φ(h) > 200 · 4r] ≤ 14. With (9), we get that h is s-good with probability at least 1/2. ✷

![image 48](<2017-brit-gaussian-width-bounds-applications_images/imageFile48.png>)

5. Random differences in Szemer´edi’s Theorem In this section we prove Theorem 1.3. We ﬁrst consider a slightly diﬀerent random model

where we form a random multiset Dk of size k by repeatedly sampling a uniformly random element from Z/NZ. We will need the following equivalent formulation of Szemer´edi’s Theorem due to Varnavides [Var59] (see [Tao07, Theorem 4.8] for this exact formulation).

- Proposition 5.1. For every ℓ ∈ N, α ∈ (0, 1] there exists N1(ℓ, α), ǫ(ℓ, α) such that for every N ≥ N1(ℓ, α), the following holds. Every subset A ⊆ Z/NZ of size at least αN contains an ǫ(ℓ, α)-fraction of all ℓ + 1 term arithmetic progressions in Z/NZ, that is,


Ex∈Z/NZ,y∈Z/NZ {0}[1A(x)1A(x + y) . . .1A(x + ℓy)] ≥ ǫ(ℓ, α).

Proposition 5.2. For all ℓ ∈ N, α ∈ (0, 1] there exists N1(ℓ, α) ∈ N such that for every N > N1(ℓ, α) the following holds. Let k ≥ ω(N1−1/⌈(ℓ+1)/2⌉ log N) and let D be a random multiset of size k obtained by sampling k times independently and uniformly at random from Z/NZ \ {0}. Then, with probability 1 − o(1), every subset A ⊆ Z/NZ of size at least αN contains a proper arithmetic progression of length ℓ + 1 with common diﬀerence in D.

Proof: We will arrive at a contradiction assuming that the statement is false. Let Γ = Z/NZ. For f : Γ → R and y ∈ Γ \ {0}, deﬁne

φy(f) = Ex∈Γ[f(x)f(x + y) . . .f(x + ℓy)],

which is a degree ℓ + 1 polynomial over the variables (f(x))x∈Γ. For a multiset S ⊆ Γ \ {0}, deﬁne

1 |S| y∈S

ΛS(f) =

φy(f).

![image 49](<2017-brit-gaussian-width-bounds-applications_images/imageFile49.png>)

If f = 1A, then this counts the fraction of proper (ℓ + 1)-term APs with common diﬀerence in S that lie completely in A. Note that ED[ΛD(f)] = ΛΓ\{0}(f).

Let N1(ℓ, α) and ǫ(ℓ, α) be as in Proposition 5.1. Suppose that with a constant probability, there is a subset A ⊆ Γ of size at least αN with no proper (ℓ + 1)-term APs whose common diﬀerence lies in D. Then,

PrD inf

ΛD(1A) = 0 = Ω(1).

A:|A|≥αN

By Proposition 5.1, for every A ⊆ Γ of size at least αN, we have that ΛΓ\{0}(1A) ≥ ǫ. We are going to apply a standard symmetrization trick to establish a connection with Gaussian

width. Let D′ be an independent copy of D. Then, ǫ ED sup

ΛD(1A) − ΛΓ\{0}(1A)

A:|A|≥αN

ΛD(1A) − ED′[ΛD′(1A)]

= ED sup

A:|A|≥αN

ΛD(1A) − ΛD′(1A)

≤ ED,D′ sup

A:|A|≥αN

k

1 k

= Ey

1,...,yk,y1′,...,yk′ ∈Γ\{0} sup

φy

![image 50](<2017-brit-gaussian-width-bounds-applications_images/imageFile50.png>)

A:|A|≥αN

i=1

(1A)

(1A) − φy′

i

i

Observe that for i.i.d. random y, y′ ∈ Γ \ {0}, the random variable φy(1A) − φy′(1A) is symmetric in the sense that it has the same distribution as its negation. Let σ1, . . ., σk be independent uniformly distributed {−1, 1}-valued random variables. Then it follows from the above that

1 k

1,...,yk y1′,...,yk′∈Γ\{0}Eσ sup

ǫ Ey

![image 51](<2017-brit-gaussian-width-bounds-applications_images/imageFile51.png>)

A:|A|≥αN

k

1 k

≤ 2Ey

1,...,yk∈Γ\{0}Eσ sup

![image 52](<2017-brit-gaussian-width-bounds-applications_images/imageFile52.png>)

A:|A|≥αN

i=1

k

(1A)

σi φy

(1A) − φy′

i

i

i=1

σiφy

(1A) .

i

= N−1pH

(as in (3)) where Hi is the hypergraph on Γ whose edges are given by (ℓ + 1) term arithmetic progressions with common diﬀerence yi. The maximum degree of Hi is O(ℓ). This is because each such AP (x+tyi)0≤t≤ℓ intersects another AP (x′+t′yi)0≤t′≤ℓ iﬀ x−x′ = (t′−t)yi; so there are only O(ℓ) such x′ for a given x. Let g1, . . ., gk be independent N(0, 1) random variables. Then we can bound

Let us ﬁx y1, . . ., yk ∈ Γ\{0}. Each φy

can be written as φy

i

i

i

Eσ sup

A:|A|≥αN

k

1 k

σiφy

(1A)

![image 53](<2017-brit-gaussian-width-bounds-applications_images/imageFile53.png>)

i

i=1

k

1 k

Eg sup

giφy

(1A)

![image 54](<2017-brit-gaussian-width-bounds-applications_images/imageFile54.png>)

i

A

i=1

k

1 Nk

Eg sup

gipH

(1A)

=

![image 55](<2017-brit-gaussian-width-bounds-applications_images/imageFile55.png>)

i

A

i=1

1 k

![image 56](<2017-brit-gaussian-width-bounds-applications_images/imageFile56.png>)

kN1−1/⌈(ℓ+1)/2⌉ log N,

ℓ

![image 57](<2017-brit-gaussian-width-bounds-applications_images/imageFile57.png>)

where the last line follows directly from Theorem 1.1. Thus we get k ℓ N1−1/⌈(ℓ+1)/2⌉ log N which is a contradiction. ✷

We will the need following simple fact that conditioning on a high probability event will not change the probability of any event by much.

- Lemma 5.3. Let A, E be some events in some probability space. If Pr[E] ≥ 1 − ε then |Pr[A|E] − Pr[A]| ≤ 2ε/(1 − ε).


Proof: |Pr[A|E] − Pr[A]| =

Pr[A ∩ E] Pr[E] − Pr[A] =

1 Pr[E]

(Pr[A] + Pr[E] − Pr[A ∪ E]) − Pr[A]

![image 58](<2017-brit-gaussian-width-bounds-applications_images/imageFile58.png>)

![image 59](<2017-brit-gaussian-width-bounds-applications_images/imageFile59.png>)

1 Pr[E] − 1 + 1 −

2ε 1 − ε

Pr[A ∪ E] Pr[E] ≤

≤ Pr[A]

.

![image 60](<2017-brit-gaussian-width-bounds-applications_images/imageFile60.png>)

![image 61](<2017-brit-gaussian-width-bounds-applications_images/imageFile61.png>)

![image 62](<2017-brit-gaussian-width-bounds-applications_images/imageFile62.png>)

✷

- Proof of Theorem 1.3: Let Dk be a random subset of Z/NZ   {0} of size at most k, formed by sampling a uniformly random element from Z/NZ for k times. Let Dp = [Z/NZ \ {0}]p be a random subset of Z/NZ \ {0} formed by including each element with probability p independently. We claim that if Dk is ℓ-intersective with probability 1 − o(1), then Dp will also be ℓ-intersective with probability 1 − o(1) when p = 2k/N and k = ωN(1).


Let p = 2k/N and k = ωN(1). Let E be the event that Dp has size at least k. By the Chernoﬀ bound,

1 − Pr[E] ≤ exp −DKL

p 2||p N ≤ exp(−Ω(pN)) = o(1)

![image 63](<2017-brit-gaussian-width-bounds-applications_images/imageFile63.png>)

where DKL is the Kullback-Leibler divergence. By Lemma 5.3, conditioning on E changes the probability of Dp being ℓ-intersective by o(1). Conditioned on E, the probability that Dp is ℓ-intersective is at least the probability that Dk is ℓ-intersective. Indeed, both Dp and Dk, after conditioning on a given size reduce to the uniform distribution over all subsets of that size. Proposition 5.2 thus implies Dp is ℓ-intersective when p = ω(N−1/⌈(ℓ+1)/2⌉ log N). ✷

6. Upper tails for arithmetic progressions in random sets

Here we prove Theorem 1.4. Let Γ = Z/NZ. In the following we identify maps from a set S to R with vectors in RS. For f : Γ → R, deﬁne

f(a)f(a + b)f(a + 2b) · · ·f(a + (k − 1)b).

- (10) Λk(f) =


a,b∈Γ,b =0

Observe that for a subset A ⊆ Γ, we have that Λk(1A) counts the number of proper k-term arithmetic progressions in A. Moreover, Λk is an N-variate polynomial of degree k. Recall that the gradient of a polynomial p ∈ R[x1, . . ., xn] is the mapping ∇p : Rn → Rn whose ith coordinate is given by (∇p)i = (∂p/∂xi)(x). The proof of Theorem 1.4 follows from a simple corollary of Theorem 1.1 and one of the main results of [BGSZ18]. For the corollary, we consider polynomial mappings given by gradients of polynomials of the form (3).

Corollary 6.1. Let n, t, d be positive integers. Let H = ([n], E) be a (d+1)-hypergraph such that at most t edges are incident on any given pair of vertices. Then,

1 n

- 1

![image 64](<2017-brit-gaussian-width-bounds-applications_images/imageFile64.png>)

- 2⌈d/2⌉ log n.


GW (∇pH)({0, 1}n) d tn1− Proof: For each i ∈ [n] let Hi = ([n], Ei) be the d-hypergraph with edge set

![image 65](<2017-brit-gaussian-width-bounds-applications_images/imageFile65.png>)

![image 66](<2017-brit-gaussian-width-bounds-applications_images/imageFile66.png>)

Ei = {e \ {i} : e ∈ E(H) and i ∈ e}. The claim now follows from Theorem 1.1 as pH

= (∇pH)i each Hi has degree at most t. ✷

i

Theorem 6.2 (Bhattacharya–Ganguly–Shao–Zhao). Let k ≥ 3 be a ﬁxed integer and let σ, τ be positive real numbers such that

1 N

GW ∇Λk({0, 1}Γ) N1−σ(log N)τ. Let p ∈ (0, 1) be bounded away from 1 and let δ > 0 be such that δ = O(1) and

![image 67](<2017-brit-gaussian-width-bounds-applications_images/imageFile67.png>)

min{δpk, δ2p} N−σ/3(log N)1+τ/3. Then,

- (11) log Pr[Λk(Γp) ≥ (1 + δ)EΛk(Γp)] = − 1 + o(1) φp (1 + o(1))δ . Moreover, provided δpkN2 → ∞ and N is prime, we have


√

![image 68](<2017-brit-gaussian-width-bounds-applications_images/imageFile68.png>)

δpk/2 log(1/p), δ2p}.

φp(δ) ≍ N min{

- Proof of Theorem 1.4: Let H = (Γ, E) be the hypergraph whose edges are the (unordered)


proper k-term arithmetic progressions in Γ. Then, accounting for the fact that Λk distinguishes between the same progression with step b run forward from a point a or backward from a+(k−1)b and since N is prime, we have 2pH = Λk. We claim that every pair of distinct vertices appears in O(k2) edges. First note that H is 2-transitive, since for any two pairs of distinct vertices (a, b), (c, d), the aﬃne linear map x  → c(x − b)/(a − b) + d(x − a)/(b − a) sends a to c, b to d and preserves progressions. It follows that every pair of distinct vertices is contained in the same number of edges. Since each edge contains k2 pairs, the claim follows by double-counting. By Corollary 6.1, we may thus set σ = 1/(2⌈(k − 1)/2⌉) and τ = 1/2 in Theorem 6.2 and it follows that for constant δ, the estimate (11) holds if

1

pk min{δpk, δ2p} N−

6⌈(k−1)/2⌉(log N)1+1/6.

![image 69](<2017-brit-gaussian-width-bounds-applications_images/imageFile69.png>)

Taking kth roots now gives the claim. ✷ 7. Proof of Lemma 1.5

In this section we give a proof Lemma 1.5. As explained in the proof of Theorem 1.1, it suﬃces to prove the statement when the coordinates of ψ are given by pH

(as in (3)) for d-uniform hypergraphs H1, . . ., Hk. Let ΛH

i

(x) = ΛH

be a d-multilinear form such that pH

i

i

(x, x, . . ., x). Let g = (g1, . . ., gk) be vector of independent standard Gaussians and ε = (ε1, . . ., εk) be uniformly random in {−1, 1}k. Then,

i

k

GW ψ({0, 1}n) = Eg sup

gipH

(x)

i

x∈{0,1}n

i=1

k

= Eg sup

giΛH

(x, . . ., x)

i

x∈{0,1}n

i=1

k

k i=1 1/ri

giΛH

≤ Egn

i

i=1

k

,

εigiΛH

= nEgEε

i

i=1

where in the last line we used that each gi is symmetrically distributed, that is, gi and −gi have the same distribution. By Jensen’s inequality, the above expectation over ε is at most

p 1/p

1/p

k

k

p

≤ Tp(Lnr1,...,rs)

giΛH

εigiΛH

,

Eε

i

i

i−1

i=1

where the inequality follows from the deﬁnition of the type-p constant of Lnr1,...,rs. Hence,

1/p

k

p

GW ψ({0, 1}n) ≤ nEg Tp(Lnr1,...,rs)

giΛH

i

i=1

≤ nTp(Lnr1,...,rs)Eg g ℓ

max

ΛH

i

p

i

≤ nTp(Lnr1,...,rs) k1/p max

ΛH

,

i

i

≤ ( ki=1 Eg

1|g1|2)1/2 = k1/p. If Hi is a matching hypergraph, using H¨older’s inequality, it is easy to see that ΛH

i|gi|p)1/p ≤ k1/p(Eg

where we used the fact that Eg g ℓ

p

i ≤ 1. If not, by Lemma 3.1, we can decompose Hi into d∆(Hi) matchings and use triangle inequality to conclude that ΛH

i ≤ d∆(Hi) which gives the desired bound.

Acknowledgements. We thank Sean Prendiville, Fernando Xuancheng Shao and Yufei Zhao for helpful discussions. This work was in part carried out while the authors were visiting the Simons Institute during the Pseudorandomness program of Spring 2017 and we thank the institute and organizers for their hospitality.

References

[BDG17] Jop Bri¨et, Zeev Dvir, and Sivakanth Gopi. Outlaw Distributions and Locally Decodable Codes. In 8th Innovations in Theoretical Computer Science Conference (ITCS 2017), volume 67 of Leibniz International Proceedings in Informatics (LIPIcs), pages 20:1–20:19. Schloss Dagstuhl–LeibnizZentrum fuer Informatik, 2017.

[BGLZ17] Bhaswar Bhattacharya, Shirshendu Ganguly, Eyal Lubetzky, and Yufei Zhao. Upper tails and independence polynomials in random graphs. Adv. Math., 319:313–347, 2017. [BGSZ18] Bhaswar Bhattacharya, Shirshendu Ganguly, Xuancheng Shao, and Yufei Zhao. Upper tails for arithmetic progressions in a random set. Internat. Math. Res. Notices, pages rny–22, 2018. [BL96] Vitaly Bergelson and Alexander Leibman. Polynomial extensions of van der Waerden’s and Szemer´edi’s theorems. J. Amer. Math. Soc., 9(3):725–753, 1996. [BNR12] Jop Bri¨et, Assaf Naor, and Oded Regev. Locally decodable codes and the failure of cotype for

projective tensor products. Electron. Res. Announc. Amer. Math. Soc., 19:120–130, 2012. [Bri16] Jop Bri¨et. On embeddings of ℓk1 from locally decodable codes. arXiv: 1611.06385, 2016. [CD16] Sourav Chatterjee and Amir Dembo. Nonlinear large deviations. Adv. Math., 299:396–450, 2016. [Chr11] Michael Christ. On random multilinear operator inequalities. arXiv: 1108.5655, 2011. [Eld18] Ronen Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear

large deviations. Geom. Funct. Anal., Aug 2018. [FLW12] Nikos Frantzikinakis, Emmanuel Lesigne, and Mate Wierdl. Random sequences and pointwise convergence of multiple ergodic averages. Indiana Univ. Math. J., pages 585–617, 2012. [FLW16] Nikos Frantzikinakis, Emmanuel Lesigne, and Mate Wierdl. Random diﬀerences in Szemer´edi’s theorem and related results. J. Anal. Math., 130(1):91–133, 2016.

[GKST06] Oded Goldreich, Howard Karloﬀ, Leonard J Schulman, and Luca Trevisan. Lower bounds for linear locally decodable codes and private information retrieval. Comput. Complexity, 15(3):263– 296, 2006. Preliminary version appeared in CCC’02.

[KT00] Jonathan Katz and Luca Trevisan. On the eﬃciency of local decoding procedures for errorcorrecting codes. In Proceedings of the 32nd annual ACM symposium on Theory of computing (STOC 2000), pages 80–86. ACM Press, 2000.

[KW04] Iordanis Kerenidis and Ronald de Wolf. Exponential lower bound for 2-query locally decodable codes via a quantum argument. J. Comput. System Sci., 69:395–420, 2004. Preliminary version appeared in STOC’03.

[LT79] Joram Lindenstrauss and Lior Tzafriri. Classical Banach spaces. II, volume 97 of Ergebnisse der Mathematik und ihrer Grenzgebiete [Results in Mathematics and Related Areas]. Springer-Verlag, Berlin-New York, 1979. Function spaces.

[LZ17] Eyal Lubetzky and Yufei Zhao. On the variational problem for upper tails in sparse random graphs. Random Structures & Algorithms, 50(3):420–436, 2017. [Mau03] Bernard Maurey. Type, cotype and K-convexity. In Handbook of the geometry of Banach spaces, Vol. 2, pages 1299–1332. North-Holland, Amsterdam, 2003. [MP73] Bernard Maurey and Gilles Pisier. Caract´erisation d’une classe d’espaces de Banach par des propri´et´es de s´eries al´eatoires vectorielles. C. R. Acad. Sci. Paris Se´r A, 277:687—690, 1973. [MU05] Michael Mitzenmacher and Eli Upfal. Probability and computing: Randomized algorithms and probabilistic analysis. Cambridge University Press, 2005. [Rya02] Raymond A. Ryan. Introduction to tensor products of Banach spaces. Springer Monographs in Mathematics. Springer-Verlag London Ltd., London, 2002.

- [S´ar78a] Andra´s Sa´rk¨ozy. On diﬀerence sets of sequences of integers. I. Acta Math. Hungar., 31(1-2):125– 149, 1978.
- [S´ar78b] Andra´s Sa´rk¨ozy. On diﬀerence sets of sequences of integers. III. Acta Math. Hungar., 31(3-4):355– 386, 1978.


[Sze75] Endre Szemer´edi. On sets of integers containing no k elements in arithmetic progression. Acta Arith., 27(299-345):21, 1975.

[Tal14] Michel Talagrand. Upper and lower bounds for stochastic processes, volume 60 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]. Springer, Heidelberg, 2014. Modern methods and classical problems.

[Tao07] Terence Tao. The ergodic and combinatorial approaches to Szemer´edi’s theorem. In CRM Proc. Lecture Notes, volume 43, pages 145–193, 2007. [TJ74] Nicole Tomczak-Jaegermann. The moduli of smoothness and convexity and the Rademacher averages of trace classes Sp (1 ≤ p < ∞). Studia Math., 50:163–182, 1974. [Var59] Panayiotis Varnavides. On certain sets of positive density. J. London Math. Soc., 1(3):358–360, 1959. [War17] Lutz Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math., 221(1):317–365, Sep 2017. [WZ12] Trevor Wooley and Tamar Ziegler. Multiple recurrence and convergence along the primes. Amer. J. Math., 134(6):1705–1732, 2012. [Yek12] Sergey Yekhanin. Locally decodable codes. Foundations and Trends in Theoretical Computer Science, 6(3):139–255, 2012.

CWI, Science Park 123, 1098 XG Amsterdam, The Netherlands E-mail address: j.briet@cwi.nl

Department of Computer Science, Princeton University, Princeton, NJ 08540, USA E-mail address: sgopi@cs.princeton.edu

