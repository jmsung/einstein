arXiv:1902.04176v1[math.PR]11Feb2019

BIVARIATE FLUCTUATIONS FOR THE NUMBER OF ARITHMETIC PROGRESSIONS IN RANDOM SETS

YACINE BARHOUMI-ANDREANI´ Ruhr-Universit¨at Bochum, Fakult¨at f¨ur Mathematik, Universita¨tsstrasse 150, 44780 Bochum, Germany.

CHRISTOPH KOCH Department of Statistics, University of Oxford, St. Giles 24-29, Oxford OX1 3LB, UK.

HONG LIU Mathematics Institute and DIMAP, University of Warwick, Coventry, CV4 7AL, UK.

Abstract. We study arithmetic progressions {a, a+b, a+2b, . . . , a+(ℓ−1)b}, with ℓ ≥ 3, in random subsets of the initial segment of natural numbers [n] := {1, 2, . . . , n}. Given p ∈ [0, 1] we denote by [n]p the random subset of [n] which includes every number with probability p, independently of one another. The focus lies on sparse random subsets, i.e. when p = p(n) = o(1) as n → +∞.

Let Xℓ denote the number of distinct arithmetic progressions of length ℓ which are contained in [n]p. We determine the limiting distribution for Xℓ not only for ﬁxed ℓ ≥ 3 but also when ℓ = ℓ(n) → +∞. The main result

concerns the joint distribution of the pair (Xℓ, Xℓ′), ℓ > ℓ′, for which we prove a bivariate central limit theorem for a wide range of p. Interestingly, the question of whether the limiting distribution is trivial, degenerate, or nontrivial is characterised by the asymptotic behaviour (as n → +∞) of the threshold function ψℓ = ψℓ(n) := npℓ−1ℓ. The proofs are based on the method of moments and combinatorial arguments, such as an algorithmic enumeration of collections of arithmetic progressions.

Keywords: arithmetic progression, central limit theorem, bivariate ﬂuctuations, method of moments, exploration process Mathematics Subject Classiﬁcation: 60C05, 11B25, 05C80, 60F05

![image 1](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile1.png>)

E-mail addresses: yacine.barhoumi@rub.de, christoph.koch@stats.ox.ac.uk,

h.liu.9@warwick.ac.uk. Date: February 13, 2019. Y.B. was supported by EPSRC grant No. EP/L012154/1. C.K. was supported by EPSRC

Grant No. EP/N004833/1 and ERC Grant No. 639046. H.L. was supported by the Leverhulme Trust Early Career Fellowship ECF-2016-523.

1

1. Introduction and main results

An ℓ-term arithmetic progression (ℓ-AP) in a set X ⊂ Z is an (ordered) ℓ-tuple of distinct numbers (a,a+b,...,a+(ℓ−1)b) whose elements belong to X. In Dickson’s History of the Theory of Numbers, the analysis of APs is traced back to around 1770 when it became prominent due to Lagrange and Waring investigating how large the common diﬀerence of an ℓ-AP of primes must be. Ever since, the study of APs has remained an extremely active domain of research and led to several results of fundamental importance, for instance Dirichlet’s Theorem [10] proved in 1837 played a key role in the formation of analytic number theory. Perhaps unsurprisingly, APs also became objects of interest in other ﬁelds such as combinatorics: Erdo˝s stated a number of conjectures related to ℓ-APs [4, pp. 232-233]. In particular, he oﬀered $1000 to solve the following largest progression-free subset problem: ﬁnd the cardinality of the largest subset of {1,...,m} (m ∈ N) which does not contain any ℓ-AP. This problem was solved by Sz´emeredi with his celebrated density theorem [26]: a subset of N of non-zero upper asymptotic density contains ℓ-APs of any arbitrary length ℓ. Subsequently, based on Sz´emeredi’s Theorem, Green and Tao [15] proved the long-standing conjecture on prime APs: (dense subsets of) the primes contain inﬁnitely many ℓ-APs for all lengths ℓ.

In 1936, Cram´er [9] conjectured that the gaps between two consecutive primes remain asymptotically bounded by the square of their logarithms and backed this conjecture with a heuristic model that replaces the set P of primes by a random set P′ made out of Bernoulli random variables, where P(m ∈ P′) ≈ 1/ logm independently for all integers m ≥ 2. However, the study of APs in random sets does not only provide a nice heuristic for number theoretic problems but is also a very natural and interesting model from a probabilistic point of view. For instance, Kohayakawa,  Luczak, and Ro¨dl [21] proved that sparse uniformly random subsets M ⊆ {1,...,n} of size |M| = Ω(√n) have the property that any (suﬃciently) dense subset of M already contains a 3-AP with probability tending to 1 as n → +∞.

![image 2](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile2.png>)

In this article we focus our attention on longer APs in sparse binomial subsets of {1,...,n}, including ℓ-APs with length ℓ = ℓ(n) → +∞ as n → +∞. In particular, we determine the limiting distribution of the number of ℓ-APs and analyse the joint distribution of the numbers of ℓ-APs and ℓ′-APs of diﬀerent lengths ℓ = ℓ′.

- 1.1. Main results. We consider a family of random subsets of the initial segments


[n] := {1,...,n} ⊂ N of the integers. For any p = p(n) ∈ [0,1] let Ξ1,...,Ξn be a collection of independent identically distributed Be(p) random variables, denote their product measure by P, and let [n]p := {i ∈ [n]: Ξi = 1} be the p-percolation of [n], i.e. [n]p is the random subset of [n] obtained by deleting any of the elements with probability 1 − p, independently of all other elements. We use the term constant to mean independent of the parameter n, and any unspeciﬁed asymptotic notation (including limits) is to be understood with respect to n → +∞.

For any integer ℓ ∈ {3,...,n} we denote the set of all ℓ-APs in [n] by Aℓ and deﬁne Xℓ to be the random variable counting the number of ℓ-APs in [n]p, namely

Xℓ = Xℓ(n) := |Aℓ| =

T∈Aℓ

{T⊆[n]p}.

Clearly, [n] itself is an n-AP and any ℓ-AP contains a whole number of ℓ′-APs for each 3 ≤ ℓ′ ≤ ℓ − 1. Therefore, the family {Xℓ}3≤ℓ≤n is obviously correlated in

a non-trivial way. While the FKG inequality (e.g. Theorem 2.12 in [17]) implies that this family is actually positively correlated, it is a priori unclear whether this correlation is asymptotically relevant. The main goal of this article is to study the asymptotic behaviour of the joint distribution of the pair (Xℓ

,Xℓ

) with ℓ1 > ℓ2.

1

2

We start by determining the limiting distribution of the number of ℓ-APs to be either a Poisson distribution or a Gaussian distribution. Let σℓ := V(Xℓ) denote the standard deviation of Xℓ.

![image 3](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile3.png>)

- Theorem 1 (Univariate limiting distributions). Let ℓ ≥ 3 be either a constant, or ℓ = ℓ(n) → +∞ satisfying ℓ/ logn → 0, and let 0 < p = p(n) = o(1).

- (a) If n2pℓ/(ℓ − 1) → c, for some c ∈ R+, then Xℓ −→d Po(c/2).
- (b) If n2pℓ/(ℓ − 1) → +∞, then (Xℓ − E(Xℓ)) σℓ−1 −→d N(0,1).


While a priori ℓ could be as large as n, it is easy to see that the random subset [n]p with p = o(1) (i.e. in the sparse regime) asymptotically almost surely (a.a.s.) does not contain any ℓ-APs with ℓ = ℓ(n) ≥ C log n for any constant C > 0. This follows by a ﬁrst moment argument, since

E(Xℓ) Cl.

5

= (1 ± o(1))

n2pℓ 2(ℓ − 1) ≤ exp 2 logn − C log n log(p−1) = o(1), (1)

![image 4](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile4.png>)

and thus by Markov’s inequality P(Xℓ = 0) → 1. In other words, Theorem 1 is optimal concerning the range of ℓ.1

We remark that for constant ℓ ≥ 3, Theorem 1 hardly comes as a surprise

since Xℓ is a sum of “weakly dependent” Bernoulli random variables. The Gaussian approximation follows then from a suﬃcient criterion due to Mikhailov (cf.

Theorem 19), while the Chen-Stein method (cf. Theorem 16) yields the Poisson approximation. Yet, we could not ﬁnd a proof of this result in the literature. The fact that the proof carries through for growing ℓ = ℓ(n) → +∞ is largely due to the fact that the expectation in (1) decreases exponentially quickly in ℓ.

Our main result characterises the bivariate ﬂuctuations of the pair (Xℓ

1

,Xℓ

2

) when both random variables are within their respective Gaussian regimes, as determined in Theorem 1.

- Theorem 2 (Bivariate ﬂuctuations for APs of diﬀerent lengths). For i ∈ {1,2}, let ℓi ≥ 3 be either a constant, or ℓi = ℓi(n) → +∞, such that we have ℓ2 < ℓ1


(point-wise) and ℓ1/ logn → 0. Let 0 < p = p(n) < 1 be such that pℓ91 → 0 and n2pℓ

ℓ−1 9 → +∞. Then we have Xℓ

1

− E(Xℓ

− E(Xℓ

) σℓ

Xℓ

) σℓ

0 0

1 κℓ

−→ d N

1,ℓ2 κℓ

1

1

2

2

,

,

,

![image 5](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile5.png>)

![image 6](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile6.png>)

1,ℓ2 1

1

2

where κℓ

1,ℓ2 satisﬁes

 

1−1ℓ1 → 0; 1,ℓ2 < 1, if npℓ

1,ℓ2 = 0, if npℓ

κℓ

1−1ℓ1 → +∞ ∧ ℓ2 is a constant ; κℓ

1−1ℓ1 → c ∈ R+ ∨ npℓ

- 0 < κℓ




1−1ℓ1 → +∞ ∧ ℓ2 = ℓ2(n) → +∞.

1,ℓ2 = 1, if npℓ

![image 7](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile7.png>)

1Except for cases where we can only expect convergence along subsequence, for instance if ℓ = ℓ(n) alternates (periodically) between two or more constants.

Interestingly, the strength of the correlation is characterised by the asymptotic behaviour of the function

1−1ℓ1, (2)

(n) := npℓ

= ψℓ

ψℓ

1

1

which originates from the combinatorial structure of tuples of overlapping APs. There are two structures, loose pairs and overlap pairs (see Deﬁnition 6), which compete to dominate the centralised second moments of the pair (Xℓ

). The function ψℓ

,Xℓ

1

2

is obtained as the ratio of the contribution of loose pairs by that of overlap pairs (of ℓ1-APs); when ψℓ

1

1 → 0, overlap pairs dominate, and when ψℓ

1 → +∞, loose pairs dominate. We call the former the overlap pair regime, and the latter the loose pair regime. An explicit expression of κℓ

1,ℓ2 is given in Lemma 14 and its proof; its derivation is surprisingly intricate and involves an integral representation.

Furthermore, we want to highlight that when ℓ2 = ℓ2(n) → +∞ (and thus also ℓ1 = ℓ1(n) → +∞), the random variables Xℓ

are either asymptotically uncorrelated, or converge to the same random variable (once renormalised). However, in all other cases, there exists a regime where the asymptotic correlation is non-trivial.

and Xℓ

1

2

Lastly, we remark that the conditions are slightly more restrictive due to technical reasons, we strongly believe that the result remains true under the weaker assumptions n2pℓ

1−1ℓ−1 → +∞ and p → 0, which characterise the sparse Gaussian regime for ℓ1-APs, cf. Theorem 1(b).

- 1.2. Related work. In the literature, the study of Xℓ for random subsets of the integers is largely focused on ℓ ≥ 3 being a constant and estimating the probability of


large deviations from its mean, i.e. the upper tail probabilities P (Xℓ ≥ (1 + ε)E(Xℓ)), and the lower tail probabilities P (Xℓ ≤ (1 − ε)E(Xℓ)). For a recent survey on large deviations in random graphs (and related combinatorial structures) see [7].

For the upper tail, Janson and Ruci´nski [19] obtained upper and lower bounds

on − log P (Xℓ ≥ (1 + ε)E(Xℓ)) being apart by a factor of log(1/p) by extending an earlier result by Janson, Oleszkiewicz, and Ruci´nski [18] on large deviations for

subgraph counts in random graphs. Subsequently, Warnke [27] closed this gap by proving that

− logP(Xℓ ≥ (1 + ε)E(Xℓ)) = Θε(Φ(E(Xℓ))), Φ(x) := min{x,√xlog(1/p)},

![image 8](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile8.png>)

and also supplying the dependency on ε of the implied constants in Θε. Notably, provided that p is in the loose pair regime (more precisely, ψℓ ≥ log n, where ψℓ = npℓ−1ℓ as in (2)) the results in [27] also extend to moderate variations, i.e. events of the form {Xℓ ≥ E(Xℓ) + t} for any t ≥ σℓ. Complementing these results, Bhattacharya, Ganguly, Shao, and Zhao [2] pinned down the precise large deviation rate function for “suﬃciently large” p. By contrast to the approach in [27], the proof in [2] builds on the non-linear large deviation principle by Chatterjee and Dembo [8] and its reﬁnement due to Eldan [11] in terms of the concept of Gaussian width, a particular notion of complexity. Recently, Bri¨et and Gopi [6] derived an upper bound on the Gaussian width leading to an improvement of the lower bound on p given in [2]. The special case ℓ = 3 was already included in [8].

On the other hand, the lower tail has received less attention: for all constants ℓ ≥ 3, Janson and Warnke [20] determined the large deviation rate function up to

constants to be

− logP(Xℓ ≥ (1 − ε)E(Xℓ)) = Θ(ε2 min{E(Xℓ),np}), while Mousset, Noever, Panagiotou, and Samotij [24] concentrated on the probability of [n]p to be ℓ-AP free, and expressed − logP(Xℓ = 0) as an alternating sum of certain joint cumulants deﬁned in terms of the dependency graph associated to Xℓ. The results on ℓ-APs in [24] hold only for p within the overlap pair regime (ψℓ = o(1), where ψℓ = npℓ−1ℓ as in (2)).

We complement the literature on large and moderate deviations by considering

typical deviations and thereby determining the limiting distribution of Xℓ not only for all constants ℓ ≥ 3 but also when ℓ = ℓ(n) → +∞. Additionally, we also inves-

tigate the interaction of the number of APs of diﬀerent length occurring in [n]p, i.e. typical ﬂuctuations of the pair (Xℓ,Xℓ′). Strikingly, we ﬁnd a signiﬁcantly diﬀerent behaviour of their bivariate ﬂuctuations in the overlap pair regime, as compared to the loose pair regime. By contrast to the results on moderate deviations in [27] or the result in [24] which work only in one of the two regimes, we employ the same approach in both regimes.

- 1.3. Proof method and outline. The main goal of this article lies in the analysis


of bivariate ﬂuctuations of the pair (Xℓ

) based on the method of moments: we show that the joint moments of (Xℓ

,Xℓ

1

2

), once centred and rescaled, converge to the moments of a Gaussian random vector, which ensures the convergence in distribution. More formally, we apply the combination of the following two classical results.

,Xℓ

1

2

- Theorem 3 (e.g. Theorem 30.2 in [3]). Let Y be a random variable which is determined by its moments, and let (Yn)n∈N be a sequence of random variables having ﬁnite moments of all orders. If limn→+∞ E(Ynk) = E(Yk) for all k ∈ N, then

Yn −−−−→d

n→+∞

Y.

The same principle transfers to multivariate random variables, by application of the Cram´er-Wold device.

- Theorem 4 (Cram´er-Wold device, e.g. Theorem 29.4 in [3]). For any r ∈ N, let Y = (Y1,...,Yr) and Yn = (Yn,1,...,Yn,r), n ∈ N, be random vectors. Then


Yn −→d Y if and only if

r

r

uiYn,i −→d

uiYi, ∀u1,...,uk ∈ R.

i=1

i=1

Our approach for the analysis of the (normalised) joint moments was inspired by a recent result of Gao and Sato [14] determining the limiting distribution of the number of matchings of size ℓ = ℓ(n) in G(n,p) to be either a Normal or a Log-normal distribution. It is well-known that the odd moments of a centred, multivariate Gaussian distribution vanish, while the even moments can be expressed combinatorially: for k ∈ N the 2k-th moment is given by a sum over all perfect matchings of the set [2k]. Thus the heart of our proof lies in showing that the (even and centred) joint moments of (Xℓ

) are dominated by a similar matching structure. In fact, we will see that this combinatorial structure is encoded in the dependency graph Γ (cf. Deﬁnition 15) associated with the pair (Xℓ

,Xℓ

1

2

). Depending on the range of p, the main contribution will come from matchings consisting of

,Xℓ

1

2

overlap pairs and/or loose pairs, and can be determined explicitly. It then remains to bound the contributions of all non-matching conﬁgurations. This last step is based on an algorithmic exploration of the components in Γ; a similar argument was previously used by Bollob´s, Cooley, Kang, and the second author [5] in the context of jigsaw percolation on random hypergraphs. By contrast, in [14] this last step was based on the switching method introduced by McKay [22], which turned out to be diﬃcult to apply in the setting of APs due to their arithmetic structure.

We close with an outline of the article: Section 2 focusses on counting APs and pairs of APs, and deriving the joint second moments from these. Since we require a high level of precision, the counting argument for loose pairs of APs turns out to be surprisingly challenging. In Section 3 we complete the proof of Theorem 1 based on two suﬃcient criteria from the literature. The higher joint moments of the pair (Xℓ

) are analysed in Section 4, where we also complete the proof of Theorem 2 and provide an alternative proof of Theorem 1(b). We then conclude with a discussion of open problems in Section 5.

,Xℓ

1

2

2. Preliminaries: counting APs and pairs of APs

We start out with determining the asymptotics related to the set of APs in [n]. First, we consider the total number of ℓ-APs, denoted by Aℓ. Claim 5. For any 3 ≤ ℓ = ℓ(n) ≤ n, we have

 

2

(1 ± o(1)) n

2(ℓ−1) if ℓ/n → 0, Θ(n) if ℓ/n → c ∈ (0,1), (1 ± o(1))(n − ℓ + 1) if ℓ/n → 1.

![image 9](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile9.png>)

Aℓ =



In particular, the following asymptotics holds for all 3 ≤ ℓ = ℓ(n) ≤ n:

Aℓ = Θ(n(n − ℓ + 1)ℓ−1). Furthermore, for any 3 ≤ ℓ = ℓ(n) = o(n), we have

n2pℓ 2(ℓ − 1)

E(Xℓ) = Aℓpℓ = (1 ± o(1))

.

![image 10](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile10.png>)

Proof. Let R := nℓ−−11 − nℓ−−11 ·(ℓ − 1) and observe that 0 ≤ R ≤ ℓ − 2. We have

![image 11](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile11.png>)

![image 12](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile12.png>)

⌊

⌊

ℓ−1 ⌋

ℓ−1 ⌋

n−1

n−1

n

![image 13](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile13.png>)

![image 14](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile14.png>)

(n − δ(ℓ − 1))

Aℓ =

{m+(ℓ−1)δ≤n} =

m=1

δ=1

δ=1

n−1 ℓ−1 + 1

n(n − ℓ + 1) 2(ℓ − 1)

n − 1 ℓ − 1 · n − (ℓ − 1)

![image 15](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile15.png>)

=

=

+ f(R,ℓ),

![image 16](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile16.png>)

![image 17](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile17.png>)

2

2

where f(R,ℓ) := (R+1)(ℓ−1)−(R+1)

2(ℓ−1) . Furthermore, we observe that for all ℓ we have

![image 18](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile18.png>)

- 0 ≤ f(R,ℓ) ≤ (ℓ − 1)/8. It remains to distinguish three cases:


- • if ℓ/n → 0, then f(R,ℓ) = o(n) = o(n2/ℓ) and the claim follows immediately,
- • if ℓ/n → c for some constant c ∈ (0,1), then f(R,ℓ) = O(n) and again the


claim follows immediately,

• if ℓ/n → 1, the ℓ-AP contained in [n] is clearly an interval, hence the number of such choices is n − ℓ + 1, completing the proof.

- 2.1. Loose pairs and overlap pairs. Next, we consider pairs of APs of potentially diﬀerent lengths, and distinguish them by the size of their intersection. Deﬁnition 6. Let 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) ≤ n.


- (a) For any r ∈ [ℓ′], we deﬁne

Dℓ,ℓ(r)′ := {(T,T′) ∈ Aℓ × Aℓ′ : |T ∩ T′| = r} to be the set of (ordered) pairs of APs intersecting in precisely r elements.

- (b) We say that a pair (T,T′) ∈ Aℓ × Aℓ′ is a loose pair if |T ∩ T′| = 1. We use the shorthand Bℓ,ℓ′ := Dℓ,ℓ(1)′ for the set of all loose pairs.
- (c) We say that a pair (T,T′) ∈ Aℓ × Aℓ′ is an overlap pair if |T ∩ T′| = ℓ′, or

equivalently T′ ⊆ T. We use the shorthand Cℓ,ℓ′ := D(ℓ

′)

ℓ,ℓ′ for the set of all overlap pairs.

- (d) We denote the cardinalities of these sets by Dℓ,ℓ(·)′ := |Dℓ,ℓ(·)′|, Bℓ,ℓ′ := |Bℓ,ℓ′|, and Cℓ,ℓ′ := |Cℓ,ℓ′|, respectively. Furthermore, whenever ℓ = ℓ′ we drop one of the lower indices, e.g. we use Dℓ(2) := Dℓ,ℓ(2).


Computing the asymptotic behaviour of the number of overlap pairs is a Corollary of Claim 5. Corollary 7. For all 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) = o(n) we have

Cℓ,ℓ′ = Θ(1) · n2(ℓ − ℓ′ + 1)/ℓ′.

Proof. Note that the number of overlap pairs (T1,T2) ∈ Cℓ,ℓ′ is equal to Aℓ·M, where M is the number of ℓ′-APs in [ℓ]. Indeed, by Claim 5, we have M = Θ(ℓ(ℓ−ℓ′+1)/ℓ′) and Aℓ = Θ(n2ℓ−1) and the statement follows.

Similarly, we obtain an upper bound on the number of pairs intersecting in precisely r elements for 2 ≤ r ≤ ℓ′ − 1. Despite being somewhat crude, this bound will suﬃce for our purposes.

- Claim 8. For any 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) = o(n) and 2 ≤ r ≤ ℓ′ − 1 we have


Dℓ,ℓ(r)′ = O(n2ℓ(ℓ′)2). Furthermore, in case r ≥ ⌊2ℓ′/3⌋ + 1, we have

Dℓ,ℓ(r)′ = O(n2(ℓ − r + 1)(ℓ′ − r + 1)/ℓ′).

Proof. Note that a pair (T,T′) ∈ Dℓ,ℓ(r)′ is already uniquely determined by choosing the ﬁrst AP T, for which there are at most O(n2ℓ−1) many choices by Claim 5; and then ﬁxing the relative position of the ﬁrst two intersection elements within T and T′, for which there are at most ℓ2 and (ℓ′)2 many choices, respectively. The ﬁrst claim follows by multiplying.

As for the second bound, assume that r ≥ 2ℓ′/3, then any pair (T,T′) ∈ Dℓ,ℓ(r)′ induces an overlap pair consisting of the ℓ-AP T and the r-AP T ∩T′. By deﬁnition the number of such pairs is Cℓ,r and thus at most O(n2(ℓ−r+1)/ℓ′), by Corollary 7. Next, observe that once T and T ∩T′ are chosen, the common diﬀerence of T′ needs to be a divisor of the common diﬀerence of T ∩ T′. However, since r ≥ ⌊2ℓ′/3⌋ + 1 we have |T′ \ T| ≤ ℓ′ − ⌊2ℓ′/3⌋ − 1 ≤ ℓ′/3 < r − 1, implying that both T ∩ T′ and T′ have the same common diﬀerence. So we may only choose how many elements

of T′ \ T are smaller than the smallest element of T ∩ T′, the number of choices is at most ℓ′ − r + 1. Hence in total we obtain the claimed upper bound.

By contrast, determining the asymptotics of the number of loose pairs is much more diﬃcult. In the following we will use the convention that 1/0 = +∞, min{x,+∞} = x, and x := 1 − x for all x ∈ [0,1]. Moreover, for any 3 ≤ ℓ = ℓ(n) ≤ n we deﬁne a function µℓ by setting

![image 19](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile19.png>)

ℓ

1 ℓ − 1

µℓ(x) :=

{x≥(ι−1)/(ℓ−1)}, (3)

![image 20](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile20.png>)

ι=1

for all x ∈ [0,1]. Furthermore, we deﬁne functions hℓ: [0,1]  → [0,1] by the following Lebesgue-Stieltjes integral

1

x a

x a

![image 21](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile21.png>)

dµℓ(a). (4) We start by proving two technical properties of these functions

hℓ(x) :=

min

,

![image 22](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile22.png>)

![image 23](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile23.png>)

![image 24](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile24.png>)

0

- Claim 9. For any constant ℓ ≥ 3 the function hℓ is non-negative and has the following properties:


- (a) Uniformly for all 1/3 ≤ x ≤ 2/3, we have

hℓ(x) ≥

1 2(ℓ − 1)

![image 25](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile25.png>)

. (5)

- (b) For all 0 ≤ x ≤ 2(ℓ1−1) we have


![image 26](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile26.png>)

1 ℓ − 1

+ xHℓ−2, (6) where Ht := tj=1 1/j denotes the t-th harmonic number.

hℓ(x) =

![image 27](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile27.png>)

Proof. For the ﬁrst claim, we note that min a x, ax ≥ 1/2 for all 1/3 ≤ a ≤ 2/3 and 1/3 ≤ x ≤ 2/3. We conclude by noting that there is at least one ι in {1,2,...,ℓ} such that 1/3 ≤ (ι − 1)/(ℓ − 1) ≤ 2/3.

![image 28](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile28.png>)

![image 29](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile29.png>)

![image 30](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile30.png>)

![image 31](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile31.png>)

For the second claim, let x ≤ 2(ℓ1−1) and note that for all 1 ≤ ι ≤ ℓ − 1 we have

![image 32](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile32.png>)

- 1 − ιℓ−−11 ≥ ℓ−11 > x implying that


![image 33](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile33.png>)

![image 34](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile34.png>)

x(ℓ − 1) ℓ − ι

1 − x

x 1 − ιℓ−−11

min

=

.

,

![image 35](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile35.png>)

![image 36](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile36.png>)

![image 37](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile37.png>)

ι−1 ℓ−1

![image 38](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile38.png>)

![image 39](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile39.png>)

Therefore, we obtain

ℓ−1

x + (1 − x) ℓ − 1

1 ℓ − ι

1 ℓ − 1

+ x

+ xHℓ−2,

hℓ(x) =

=

![image 40](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile40.png>)

![image 41](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile41.png>)

![image 42](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile42.png>)

ι=2

as claimed. Next, let the entropy function h∞: [0,1]  → [0,1] be deﬁned by h∞(x) :=

xlog(1/x) + x log(1/x) if 0 < x < 1, 0 if x = 0 ∨ x = 1,

![image 43](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile43.png>)

![image 44](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile44.png>)

(7)

and observe that h∞ is continuous on [0,1]. The next statement shows that h∞ is obtained naturally from hℓ when ℓ = ℓ(n) → +∞.

- Claim 10. For any ℓ = ℓ(n) → +∞ with ℓ = o(n), the function hℓ converges to h∞ in L2 as n → +∞.


Proof. We ﬁrst observe that {dµℓ}ℓ∈N converges weakly to the uniform measure on [0,1] as n → +∞. Furthermore, the function a  → min xa, xa is bounded and continuous for all x ∈ [0,1], and thus we have

![image 45](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile45.png>)

![image 46](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile46.png>)

![image 47](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile47.png>)

![image 48](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile48.png>)

1

1

x a

x a

x a

x a

![image 49](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile49.png>)

![image 50](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile50.png>)

dµℓ(a) = (1 ± o(1))

da. Moreover, for all x ∈ (0,1) we have

hℓ(x) =

,

,

min

min

![image 51](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile51.png>)

![image 52](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile52.png>)

![image 53](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile53.png>)

![image 54](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile54.png>)

![image 55](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile55.png>)

![image 56](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile56.png>)

0

0

1

1

x a

x a {x≥a}

x a {x≤a}

x a

![image 57](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile57.png>)

![image 58](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile58.png>)

da =

,

+

da

min

![image 59](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile59.png>)

![image 60](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile60.png>)

![image 61](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile61.png>)

![image 62](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile62.png>)

![image 63](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile63.png>)

![image 64](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile64.png>)

![image 65](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile65.png>)

![image 66](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile66.png>)

0

0

1

1

da a

da a

![image 67](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile67.png>)

= x

+ x

![image 68](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile68.png>)

![image 69](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile69.png>)

![image 70](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile70.png>)

![image 71](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile71.png>)

x

x

![image 72](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile72.png>)

= xlog (1/x) + x log (1/x),

![image 73](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile73.png>)

![image 74](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile74.png>)

and this expression extends continuously for x ∈ [0,1]. In other words, hℓ converges point-wise to h∞.

However, since uniformly for all x ∈ [0,1] we have hℓ(x)2 ≤ 1, the Dominated Convergence Theorem implies that also hℓ → h∞ in L2.

With this preparation we will now determine the number of loose pairs asymptotically. Lemma 11. Let 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) = o(n).

- (a) If both ℓ and ℓ′ are constant, then we have Bℓ,ℓ′

![image 75](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile75.png>)

n3 −−−−→

n→+∞

1

0

hℓ(t)hℓ′(t)dt > 0.

- (b) If ℓ = ℓ(n) → +∞, but ℓ′ is a constant, then we have Bℓ,ℓ′

![image 76](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile76.png>)

n3 −−−−→

n→+∞

1

0

h∞(t)hℓ′(t)dt > 0.

- (c) If ℓ′ = ℓ′(n) → +∞, then we obtain


1

π2 18

Bℓ,ℓ′ n3 −−−−→

- 5

![image 77](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile77.png>)

- 6 −


h∞(t)2dt =

= 0.2850 ... .

![image 78](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile78.png>)

![image 79](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile79.png>)

n→+∞

0

Proof. Let ∆ := nℓ−−11 and ∆′ := ℓ n′−−11 . We enumerate the elements (T,T′) ∈

![image 80](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile80.png>)

![image 81](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile81.png>)

- Aℓ × Aℓ′, with T = (T(1),...,T(ℓ)) and T′ = (T′(1),...,T′(ℓ′)), by ﬁxing the common diﬀerences (δ,δ′) ∈ [∆] × [∆′], and the unique intersection point m ∈ [n] together with its positions (ι,ι′) ∈ [ℓ] × [ℓ′] within (T,T′). Then both ℓ-APs are to be contained in [n] if and only if


1 ≤ T(1) ∧ 1 ≤ T′(1) ∧ T(ℓ) ≤ n ∧ T′(ℓ′) ≤ n.

Expressing T(1), T′(1), T(ℓ), and T′(ℓ′) in terms of m, ι, ι′, δ, and δ′, this is equivalent to

1 + max{(ι − 1)δ,(ι′ − 1)δ′} ≤ m ≤ n − max{(ℓ − ι)δ,(ℓ′ − ι′)δ′}.

In other words, the number of valid choices for m is (n − max {(ι − 1)δ,(ι′ − 1)δ′} − max{(ℓ − ι)δ,(ℓ′ − ι′)δ′})+ ,

with x+ := max{x,0} = x {x≥0}, and by summing over all choices for (ι,ι′,δ,δ′) ∈ [ℓ] × [ℓ′] × [∆] × [∆′], we obtain

(n − max {(ι − 1)δ,(ι′ − 1)δ′} − max{(ℓ − ι)δ,(ℓ′ − ι′)δ′})+ .

Bℓ,ℓ′ =

(ι,ι′,δ,δ′)

It turns out to be convenient to divide this quantity by n to obtain

ι′ − 1 ℓ′ − 1

(ℓ′ − 1)δ′ n

ι − 1 ℓ − 1

(ℓ − 1)δ n

Bℓ,ℓ′ n

(8)

=

,

,

,

f

![image 82](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile82.png>)

![image 83](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile83.png>)

![image 84](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile84.png>)

![image 85](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile85.png>)

![image 86](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile86.png>)

(ι,ι′,δ,δ′)

where the function f : [0,1]4 → [0,1] is deﬁned by

f(a,a′,u,u′) := (1 − max{au,a′u′} − max{(1 − a)u,(1 − a′)u′})+ . Now note that we have

n ℓ − 1

n ℓ′ − 1

and ∆′ = (1 ± O(ℓ′/n))

∆ = (1 ± O(ℓ/n))

, implying

![image 87](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile87.png>)

![image 88](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile88.png>)

(ℓ′ − 1)δ′ n

δ′ ∆′

(ℓ − 1)δ n

δ ∆

= (1 ± O(ℓ′/n))

= (1 ± O(ℓ/n))

, and thus it is not hard to show that there exists a constant C > 0 such that for all

and

![image 89](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile89.png>)

![image 90](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile90.png>)

![image 91](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile91.png>)

![image 92](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile92.png>)

- 1 ≤ ι ≤ ℓ and 1 ≤ ι′ ≤ ℓ′ we have


ι′ − 1 ℓ′ − 1

(ℓ′ − 1)δ′ n − f

ι′ − 1 ℓ′ − 1

δ′ ∆′ ≤ C ·

ι − 1 ℓ − 1

(ℓ − 1)δ n

ι − 1 ℓ − 1

δ ∆

ℓ n

f

,

. Furthermore, let

,

,

,

,

,

![image 93](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile93.png>)

![image 94](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile94.png>)

![image 95](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile95.png>)

![image 96](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile96.png>)

![image 97](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile97.png>)

![image 98](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile98.png>)

![image 99](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile99.png>)

![image 100](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile100.png>)

![image 101](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile101.png>)

1 ∆∆′

νn(x,x′) :=

{x≤δ} {x′≤δ′}

![image 102](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile102.png>)

(δ,δ′)

and observe that {dνn}n∈N converges weakly to the uniform measure on [0,1]2. Since f is bounded and continuous, we therefore have

ι′ − 1 ℓ′ − 1

ι − 1 ℓ − 1

Bℓ,ℓ′ n∆∆′

,u,u′ dudu′. (9)

= (1 ± o(1))

,

f

![image 103](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile103.png>)

![image 104](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile104.png>)

![image 105](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile105.png>)

(ι,ι′) [0,1]2

The next goal is to deal with the positive part of the function f: we note that (R − Q)+ = R − min{R,Q}

and so, for any (a,a′,u,u′) ∈ [0,1]4, by setting R :=min{1 − au,1 − a′u′}, Q :=max{(1 − a)u,(1 − a′)u′},

we obtain f (a,a′,u,u′) = min{1 − au,1 − a′u′}

− min {min{1 − au,1 − a′u′},max{(1 − a)u,(1 − a′)u′}}. Recall the integral representation

+∞

min{x,y} =

{t≤x} {t≤y}dt,

0

which is valid for all (x,y) ∈ R2+. We may express f as

+∞

f (a,a′,u,u′) =

{t≤min{1−au,1−au}} 1 − {t≤max{(1−a)u,(1−a′)u′}} dt

0

1

{max{(1−a)u,(1−a′)u′}≤t≤min{1−au,1−au}}dt

=

0

1

{(1−a)u≤t≤1−au} {(1−a′)u′≤t≤1−a′u′}dt

=

0

1

=

0 {u≤min{t/a,t/a}} {u′≤min{t/a′,t/a′}}dt,

![image 106](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile106.png>)

![image 107](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile107.png>)

![image 108](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile108.png>)

![image 109](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile109.png>)

using the convention that 1/0 = +∞, min{x,+∞} = x, and x := 1 − x for all x ∈ [0,1]. Consequently, by integrating over (u,u′) ∈ [0,1]2 and using Fubini’s Theorem, we obtain

![image 110](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile110.png>)

f (a,a′,u,u′)dudu′ =

[0,1]2

1

min

0

![image 111](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile111.png>)

t a

t a

,

![image 112](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile112.png>)

![image 113](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile113.png>)

![image 114](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile114.png>)

min

![image 115](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile115.png>)

t a′

t a′

,

![image 116](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile116.png>)

![image 117](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile117.png>)

![image 118](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile118.png>)

dt.

Hence, (9) simpliﬁes to become

![image 119](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile119.png>)

![image 120](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile120.png>)

t a

t a′

Bℓ,ℓ′ n∆∆′(ℓ − 1)(ℓ′ − 1)

t a

t a′

dµℓ(a)dµℓ′(a′)dt,

= (1 ± o(1))

min

min

,

,

![image 121](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile121.png>)

![image 122](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile122.png>)

![image 123](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile123.png>)

![image 124](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile124.png>)

![image 125](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile125.png>)

![image 126](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile126.png>)

![image 127](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile127.png>)

[0,1]3

where µℓ and µℓ′ are the measures deﬁned in (3). Now, we observe that

n∆∆′(ℓ − 1)(ℓ′ − 1) = (1 ± o(1))n3, and so

2/3

1

Cl.9 ≥

- Bℓ,ℓ′


1 4(ℓ − 1)(ℓ′ − 1)

1 12(ℓ − 1)(ℓ′ − 1)

n3 −−−−→

hℓ(t)hℓ′(t)dt

dt =

> 0,

![image 128](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile128.png>)

![image 129](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile129.png>)

![image 130](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile130.png>)

n→+∞

1/3

0

completing the proof of Lemma 11 when both ℓ and ℓ′ are constant.

Assume now that ℓ′ is a constant, but ℓ = ℓ(n) → +∞ with ℓ = o(log n). Then by Claim 10 we have hℓ → h∞ in L2, furthermore, we have hℓ′ 2 ≤ 1, hence

1

hℓ′(t)(h∞(t) − hℓ(t))dt ≤ hℓ′ 2 · h∞ − hℓ 2 → 0. This implies that

0

1

2/3

Cl.9 ≥

Bℓ,ℓ′ n3 −−−−→

1 2(ℓ′ − 1)

log(3/2) 3(ℓ′ − 1)

h∞(t)dt ≥

h∞(t)hℓ′(t)dt

> 0,

![image 131](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile131.png>)

![image 132](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile132.png>)

![image 133](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile133.png>)

n→+∞

0

1/3

completing the claim for this case.

Similarly, if ℓ = ℓ(n) → +∞ and ℓ′ = ℓ′(n) → +∞ with ℓ′ ≤ ℓ = o(log n), then analogously to the previous case, we obtain

Bℓ,ℓ′ n3 −−−−→

![image 134](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile134.png>)

n→+∞

1

π2 18

- 5

![image 135](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile135.png>)

- 6 −


h∞(t)2dt =

![image 136](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile136.png>)

0

= 0.2850 ...,

where we evaluated the integral using SageMath [25].

Remark 12. The limits βℓ,ℓ′ := limn→+∞ Bℓ,ℓ′n−3 can be computed explicitly based on their integral representation (and the help of SageMath) for speciﬁc choices of ℓ and ℓ′; for instance, along the diagonal ℓ = ℓ′ we have

31 48 ≈ 0.6458 ; β4,4 =

130 243 ≈ 0.5350 ; β5,5 =

835 1728 ≈ 0.4832 ; ...

β3,3 =

![image 137](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile137.png>)

![image 138](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile138.png>)

![image 139](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile139.png>)

and similarly, we obtain β4,3 = 1296785 ≈ 0.6057, β5,3 = 335576 ≈ 0.5816, and also β5,4 = 25921339 ≈ 0.5166. Further values are easily computed explicitly, however we do not believe that there exists a closed form expression for βℓ,ℓ′ in general.

![image 140](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile140.png>)

![image 141](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile141.png>)

![image 142](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile142.png>)

- 2.2. Second moments. Given any subset T ⊆ [n], we deﬁne


p} − p|T| so E(ZT) = 0 for all T ⊂ [n], and for any 3 ≤ ℓ = ℓ(n) ≤ n we set X¯ℓ := Xℓ − E(Xℓ) =

ZT := {T⊆[n]

ZT.

T∈Aℓ

First, we prove that the main contribution of the centred second moments comes from loose pairs, overlap pairs, or a combination of both.

- Lemma 13. For 0 < p = p(n) = o(1) and any 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) = o(n) we have


′−1 + Cℓ,ℓ′pℓ . In particular, we have

E(X¯ℓX¯ℓ′) = (1 ± o(1)) Bℓ,ℓ′pℓ+ℓ

![image 143](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile143.png>)

σℓ = (1 ± o(1)) Bℓp2ℓ−1 + Cℓpℓ.

Proof. We observe that for any r ∈ [ℓ′] and (T,T′) ∈ Aℓ × Aℓ′ with |T ∩ T′| = r, we have

′−r, while for any (T,T′) ∈ Aℓ × Aℓ′ with |T ∩ T′| = 0 we have

′

′−r − pℓ+ℓ

′

E(ZTZT′) = E( {T∪T′⊆[n]p} − pℓ+ℓ

) = pℓ+ℓ

= (1 ± o(1))pℓ+ℓ

E(ZTZT′) = E(ZT)E(ZT′) = 0. By distinguishing the size of the intersection we obtain

E(X¯ℓX¯ℓ′) = (1 ± o(1))

ℓ′

′−r,

Dℓ,ℓ(r)′pℓ+ℓ

r=1

′)

and recall that by deﬁnition Dℓ,ℓ(1)′ = Bℓ,ℓ′ and D(ℓ

ℓ,ℓ′ = Cℓ,ℓ′.

Therefore, we ﬁrst consider the contribution of summands with 2 ≤ r ≤ ⌊2ℓ′/3⌋. By the ﬁrst estimate of Claim 8 we have

⌊2ℓ′/3⌋

⌊2ℓ′/3⌋

′−r = O(1)·

Dℓ,ℓ(r)′pℓ+ℓ

r=2

r=2

′−r = O(n2ℓ(ℓ′)3pℓ+ℓ

′/3) = o(Cℓ,ℓ′pℓ),

n2ℓ(ℓ′)2pℓ+ℓ

where for the last estimate, we recall that Cℓ,ℓ′ = Θ(n2(ℓ − ℓ′ + 1)(ℓ′)−1) by Corollary 7, and observe that ℓ(ℓ

′)4pℓ′/3

ℓ−ℓ′+1 = o(1) for all constellations of ℓ and ℓ′, since p = o(1).

![image 144](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile144.png>)

Next, we consider the contribution of summands with ⌊2ℓ′/3⌋ + 1 ≤ r ≤ ℓ′ − 1. By the second estimate of Claim 8 we obtain

ℓ′−1

ℓ′−1

′−r = O(1) ·

′−r

Dℓ,ℓ(r)′pℓ+ℓ

n2(ℓ − r + 1)(ℓ′)−1(ℓ′ − r + 1)pℓ+ℓ

r=⌊2ℓ′/3⌋+1

r=⌊2ℓ′/3⌋+1

⌈ℓ′/3⌉−2

= O(n2(ℓ − ℓ′ + 1)(ℓ′)−1pℓ) ·

(i + 2)2pi+1

i=0

= o(Cℓ,ℓ′pℓ), since the last sum is of order O(p) = o(1).

Hence, the main contribution to E(X¯ℓX¯ℓ′) comes from the summands for r = 1 and r = ℓ′, i.e. we have

′−1 + Cℓ,ℓ′pℓ ,

E(X¯ℓX¯ℓ′) = (1 ± o(1)) Bℓ,ℓ′pℓ+ℓ

as claimed by the ﬁrst statement. As for the second statement, we recall that by deﬁnition Bℓ,ℓ = Bℓ and Cℓ,ℓ = Cℓ = Aℓ.

For any 3 ≤ ℓ′ = ℓ(n) < ℓ = ℓ(n) ≤ n we deﬁne

E(X¯ℓX¯ℓ′) σℓσℓ′

κℓ,ℓ′ := lim

(10)

![image 145](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile145.png>)

n→+∞

and observe that 0 ≤ κℓ,ℓ′ ≤ 1, by the FKG inequality and the Cauchy-Schwarz inequality. The following proof shows implicitly that κℓ,ℓ′ is well-deﬁned, i.e. the limit in (10) exists.

- Lemma 14. Let 0 < p = p(n) = o(1) and 3 ≤ ℓ′ = ℓ′(n) < ℓ = ℓ(n) = o(n).


- (a) If npℓ−1ℓ → 0, then κℓ,ℓ′ = 0;
- (b) if npℓ−1ℓ → c ∈ R+, then 0 < κℓ,ℓ′ < 1;
- (c) if npℓ−1ℓ → +∞ and ℓ′ is a constant, then 0 < κℓ,ℓ′ < 1;
- (d) if npℓ−1ℓ → +∞ and ℓ′ = ℓ′(n) → +∞, then κℓ,ℓ′ = 1.


Proof. By Lemma 13, we have

2

′−1 + Cℓ,ℓ′pℓ

Bℓ,ℓ′pℓ+ℓ

E(X¯ℓX¯ℓ′) 2 σℓ2σℓ2′

= (1 ± o(1))

. First assume that npℓ−1ℓ → 0, then we have

![image 146](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile146.png>)

![image 147](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile147.png>)

[Bℓp2ℓ−1 + Aℓpℓ] · [Bℓ′p2ℓ′−1 + Aℓ′pℓ′]

Bℓp2ℓ−1 = Θ(n3p2ℓ−1) = o(n2ℓ−1pℓ) = o(Aℓpℓ), by Claim 5 and Lemma 11. Consequently we have

  

   .

2

′−1

Bℓ,ℓ′pℓ+ℓ

E(X¯ℓX¯ℓ′) 2 σℓ2σℓ2′

Cℓ,ℓ′pℓ 2 Aℓpℓ · Aℓ′pℓ′

= O(1) ·

+

![image 148](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile148.png>)

![image 149](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile149.png>)

![image 150](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile150.png>)

Aℓpℓ · Bℓ′p2ℓ′−1

Furthermore, using Claim 5 and Lemma 11 we obtain Bℓ,ℓ′pℓ+ℓ

2

′−1

= O(1) · npℓ−1ℓ = o(1), and similarly, from Claim 5 and Corollary 7 we deduce

![image 151](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile151.png>)

Aℓpℓ · Bℓ′p2ℓ′−1

Cℓ,ℓ′pℓ 2 Aℓpℓ · Aℓ′pℓ′

′

pℓ−ℓ

ℓ(ℓ − ℓ′ + 1)2 ℓ′

= O(1) ·

= o(1). Hence, letting n → +∞ we obtain

![image 152](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile152.png>)

![image 153](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile153.png>)

E(X¯ℓX¯ℓ′) σℓσℓ′

≤ 0, as claimed since we already argued that κℓ,ℓ′ ≥ 0 by the FKG inequality.

κℓ,ℓ′ = lim

![image 154](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile154.png>)

n→+∞

On the other hand, if npℓ−1ℓ → c ∈ R+, then Claim 5, Corollary 7, and Lemma 11 imply

′−1), and

′

′

′−1) = o(Bℓ′p2ℓ

= Θ(n2(ℓ′)−1pℓ

) = o(n3p2ℓ

Aℓ′pℓ

′−1). Thus we obtain

′−1) = o(Bℓ,ℓ′pℓ+ℓ

Cℓ,ℓ′pℓ = Θ(n2(ℓ − ℓ′ + 1)(ℓ′)−1pℓ) = o(n3pℓ+ℓ

2

′−1

Bℓ,ℓ′pℓ+ℓ

E(X¯ℓX¯ℓ′) 2 σℓ2σℓ2′

= (1 ± o(1)) ·

. (11)

![image 155](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile155.png>)

![image 156](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile156.png>)

[Bℓp2ℓ−1 + Aℓpℓ] · Bℓ′p2ℓ′−1

Now let ϕℓ := hℓ if ℓ is a constant, and ϕℓ := h∞ if ℓ = ℓ(n) → +∞; and deﬁne ϕℓ′ analogously. We note that both ϕℓ and ϕℓ′ are L2-integrable. Next, we take the limit n → +∞ in (11) and note that Lemma 11 implies

E(X¯ℓX¯ℓ′) 2 σℓ2σℓ2′

ϕℓ,ϕℓ′ 2 ϕℓ 22 ϕℓ′ 2

1 1 + γ ·

κℓ,ℓ′2 = lim

=

![image 157](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile157.png>)

![image 158](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile158.png>)

![image 159](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile159.png>)

n→+∞

2

where

ℓ

2(ℓ−1)c ϕℓ 22 if ℓ is ﬁnite

- Aℓpℓ

![image 160](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile160.png>)

- Bℓp2ℓ−1


![image 161](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile161.png>)

=

γ = γ(c,ℓ) := lim

.

1

2c ϕ∞ 22 otherwise

n→+∞

![image 162](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile162.png>)

In particular, the Cauchy-Schwarz inequality implies κℓ,ℓ′2 ≤

1 1 + γ

< 1,

![image 163](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile163.png>)

since γ > 0. On the other hand, Lemma 11 also guarantees that ϕℓ,ϕℓ′ > 0 and this implies

κℓ,ℓ′ > 0, completing the proof for the case npℓ−1ℓ → c ∈ R+. Assume now that npℓ−1ℓ → +∞, then Aℓ′pℓ

′−1), Aℓpℓ = o(Bℓp2ℓ−1), and Cℓ,ℓ′pℓ = Θ(n2(ℓ−ℓ′+1)(ℓ′)−1pℓ) = o(n3pℓ+ℓ

′

= o(Bℓ′p2ℓ

′−1), by Claim 5, Corollary 7, and Lemma 11. Therefore, we obtain

′−1) = o(Bℓ,ℓ′pℓ+ℓ

(Bℓ,ℓ′)2 Bℓ · Bℓ′

ϕℓ,ϕℓ′ 2 ϕℓ 22 ϕℓ′ 2

κℓ,ℓ′2 = lim

=

![image 164](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile164.png>)

![image 165](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile165.png>)

n→+∞

2

from Lemmas 13 and 11, using the notation of ϕℓ and ϕℓ′ as in the previous case. As before, we observe that ϕℓ,ϕℓ′ > 0 and this implies

κℓ,ℓ′ > 0. It remains to distinguish two cases: ﬁrst, if ℓ′ = ℓ′(n) → +∞, then also ℓ = ℓ(n) →

+∞ and thus ϕℓ = ϕℓ′ = h∞, but then clearly h∞,h∞ = h∞ 22, so κℓ,ℓ′ = 1.

On the other hand, if ℓ′ is a constant, then we observe that hℓ′ and h∞ are linearly independent in L2. To see this, let ε = ε(ℓ′) > 0 be a suﬃciently small constant, and observe that h∞(x)2 ≤ (2x+xlog(1/x))2 ≤ 9x for all x ≤ ε implying

ε

9 2

h∞(x)2dx ≤

ε2;

![image 166](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile166.png>)

0

however, by Lemma 9 (b), for suﬃciently small ε > 0, we have hℓ′(x) ≥ 1/(ℓ′ − 1) and thus

ε

1 (ℓ′ − 1)2

hℓ′(x)2dx ≥

ε. Consequently, for any suﬃciently small constant ε > 0 we obtain

![image 167](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile167.png>)

0

2

2

ε

ε

hℓ′(x) hℓ′

h∞(x) h∞

9 2 h∞ 2

1 (ℓ′ − 1)2 hℓ′ 2ε >

ε2 ≥

dx ≥

dx,

![image 168](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile168.png>)

![image 169](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile169.png>)

![image 170](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile170.png>)

![image 171](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile171.png>)

0

0

and so the functions hℓ′ and h∞ are not linearly dependent in L2, as claimed. Consequently, the Cauchy-Schwarz inequality is a strict inequality and we obtain

ϕℓ,ϕℓ′ 2 ϕℓ 22 ϕℓ′ 2

κℓ,ℓ′ =

< 1, completing the proof.

![image 172](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile172.png>)

2

3. Univariate fluctuations: proof of Theorem 1

In this section we focus on univariate ﬂuctuations of Aℓ, i.e. we prove the two statements of Theorem 1. First we treat the Poisson regime, where the result follows directly from an application of the Chen-Stein method and the preliminary computations performed in Section 2 (with ℓ′ = ℓ). Likewise, the Gaussian approximation is a consequence of a classical normality criterion.

- 3.1. Poisson regime: proof of Theorem 1(a). We start by introducing the notion of a dependency graph. We emphasize the fact that this deﬁnition is the one that ﬁts our purpose, and that there can be many other such notions (see e.g. [12, 17]).


Deﬁnition 15. Let (Yi)1≤i≤N be a sequence of random variables (on a common probability space). A (simple) graph G = (V,E) with vertex set V = [N] is called a dependency graph for (Yi)i∈[N] if and only if for all disjoint subsets U,U′ ⊆ V with E(U,U′) = ∅ we have

(Yi)i∈U is independent of (Yi)i∈U′, where E(U,U′) := {(i,j) ∈ E : i ∈ U and j ∈ U′} denotes the set of edges between U and U′. We denote the neighbourhood of a vertex i ∈ [N] by N(i) := NG(i) := {j ∈ U : (i,j) ∈ E} and let N(i) := N(i) ∪ {i}.

The dependency graph relevant to this paper is the following: given 3 ≤ ℓ′ = ℓ′(n) ≤ ℓ = ℓ(n) ≤ n we consider the graph

Gℓ,ℓ′ = Gℓ,ℓ′(n) := Aℓ ∪ Aℓ′, (T,T′) ∈ (Aℓ ∪ Aℓ′)2 : |T ∩ T′| ≥ 1 . (12) In other words, the vertices represent APs and edges indicate that the corresponding APs intersect. Clearly, Gℓ,ℓ′ is a dependency graph of the family {T∈[n]

p} T∈Aℓ∪Aℓ′. We deﬁne the following two quantities associated with a dependency graph G of

(Yi)1≤i≤N:

N

V1(G) :=

E(Yi)E(Yj),

i=1 j∈ NG(i)

N

V2(G) :=

E(YiYj).

i=1 j∈NG(i)

(13)

We use a variant of the Chen-Stein method due to Arratia, Goldstein, and Gordon [1] (in a slightly simpliﬁed form).

Theorem 16 (Theorem 1 in [1]). Let (Yi)1≤i≤N be Bernoulli random variables of expectation pi := E(Yi) > 0. Set

N

N

pi.

Yi, and ζ := E(SN) =

SN :=

i=1

i=1

Let G be a dependency graph of (Yi)1≤i≤N, and V1(G), V2(G) as in (13). Let Y be a Poisson random variable with mean E(Y) := ζ. Then, for any U ⊂ N,

|P(SN ∈ U) − P(Y ∈ U)| ≤ V1(G) + V2(G).

- Remark 17. The theorem given in [1] uses an additional quantity V3(G) given by


N

E E Yi − pi (Yj)j ∈ N

V3(G) :=

G(i)

i=1

but due to using a more restrictive notion of dependency graphs, we always have V3(G) = 0.

- Proof of Theorem 1(a). We ﬁx any 3 ≤ ℓ = ℓ(n) ≤ n and aim to apply Theorem 16


p} T∈Aℓ. The corresponding dependency graph Gℓ was deﬁned in (12). Clearly, for any T ∈ Aℓ we have E( {T⊆[n]

to the family {T∈[n]

p}) = pℓ and thus

ℓ

Dℓ(r) = O(n3p2ℓ),

p})E( {T′⊆[n]p}) = p2ℓ

V1(Gℓ) =

E( {T⊆[n]

r=1

T∈Aℓ T′∈ NGℓ(T)

where the last equality holds due to Corollary 7, Claim 8, and Lemma 11. Next, we note that E( {T⊆[n]

p} {T′⊆[n]p}) = p2ℓ−r for all 1 ≤ r ≤ ℓ − 1 and (T,T′) ∈ Dℓ(r). Thus, we obtain

ℓ−1

Dℓ(r)p2ℓ−r

V2(Gℓ) =

p} {T′⊆[n]p} =

E {T⊆[n]

r=1

T∈Aℓ T′∈NG(T)

= O(1) · n3p2ℓ−1 + n2ℓ3pℓ+1 ,

where the last estimate holds due to Claim 8 and Lemma 11.

Combining these two bounds and using the assumption n2pℓ/(ℓ − 1) → c for some c ∈ R+ yields

V1(Gℓ) + V2(Gℓ) = O(n−1+2/ℓ + n−2/ℓ) = o(1). The same bound holds when ℓ → +∞, ℓ = o(log n) and pℓ4 → 0. Thus Theorem 16 is applicable for the family {T∈[n]

p} T∈Aℓ and shows that for all U ⊆ N we have

  − P (Po(λ) ∈ U) ≤ o(1),



 T∈Aℓ

{T⊆[n]p} ∈ U

P

where

n2pℓ 2(ℓ − 1)

5

p}) Cl.

(1 ± o(1))

= c/2

E( {T⊆[n]

= lim

λ := lim

![image 173](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile173.png>)

n→+∞

n→+∞

T∈Aℓ

completing the proof of Theorem 1(a).

- Remark 18. If we do not suppose the assumption of Theorem 1(a), namely that n2pℓℓ−1 = O(1), we still have a Poisson approximation with Po(λn) where λn := n2pℓℓ−1 provided that V1(Gℓ) + V2(Gℓ) = o(1). This is the case if n3p2ℓ−1 → 0 and n2pℓ+1ℓ3 → 0, which is equivalent in the ﬁrst case to p ≪ n−3/(2ℓ−1), and in the second case to p ≪ n−2/(ℓ+1)ℓ−3/(ℓ+1). It is well known that a Poisson random variable with diverging parameter converges in distribution (after rescaling) to a Gaussian, hence, this case shows that we have a Gaussian regime for the range n−2/ℓℓ1/ℓ ≪ p ≪ min{n−3/(2ℓ−1),n−2/(ℓ+1)ℓ−3/(ℓ+1)}.


- 3.2. Gaussian regime: proof of Theorem 1(b). For the normal approximation we apply a criterion due to Janson [16], which was then reﬁned by Mikhailov [23]. This normality criterion is based on controlling mixed cumulants of sum of random variables by means of an associated dependency graph. We follow the notation of [17].


be a family of random variables with dependency graph Γn (as deﬁned in Deﬁnition 15) and suppose that there exist constants {Cr}r∈N independent of n, and quantities Mn and Qn such that

Theorem 19 (e.g. Theorem 6.21 in [17]). Let (Xi,n)1≤i≤N

n

E

Nn

|Xi,n| ≤ Mn, (14)

i=1

and for all V of constant size (i.e. |V | is independent of n), we have

E |Xi,n| (Xj,n)j∈V ≤ C|V |Qn, (15)

i∈N(V )

where N(V ) := ∪i∈V N(i) as in Deﬁnition 15. Let Sn := Ni=1n Xi,n and σn2 := V(Sn). If there exists an s > 2 such that

s−1

Qn σn

Mn σn

−−−−→

0 (16)

![image 174](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile174.png>)

![image 175](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile175.png>)

n→+∞

then, we have

Sn − E(Sn) σn

−−−−→d n→+∞

N(0,1).

![image 176](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile176.png>)

Note that the proof of Theorem 19 shows that the assumption (16) becomes weaker as s increases. However, we will see that for this application it is satisﬁed for any s > 0.

- Proof of Theorem 1(b). In the setting of ℓ-APs we have Sn := Xℓ, and note that by Claim 5 we have E(Xℓ) = pℓAℓ, i.e. we may choose Mn := pℓAℓ.


Now, for V ⊂ Aℓ, let Λ(V ) := ∪T∈V T ⊂ [n] be the set of points covered by APs in V . We write Z(V ) for the LHS of (15) and observe that

Z(V ) =

E

T∈N(V )

pℓ−|T∩Λ(V)|

Ξa

Ξa (Ξk)k∈Λ(V ) =

a∈T

a∈T∩Λ(V )

T∈N(V )

pℓ−|T∩Λ(V)|

≤

T∈N(V )

- as Ξa takes values in {0,1}. First, we consider APs T ∈ N(V ) in “loose conﬁgurations”, i.e. |T ∩ Λ(V )| = 1. Note that there are at most O|V |(nℓ) of these T and the contribution to Z(V ) of each of them is pℓ−1. On the other hand, there are
- at most O|V |(ℓ4) APs T ∈ N(V ) with |T ∩ Λ(V )| ≥ 2, and trivially, each of their contribution to Z(V ) is upper bounded by 1. Together this means that there exist constants {Cr}r∈N and we may choose Qn := npℓ−1ℓ+ℓ4 such that Z(V ) ≤ C|V |Qn for all V ⊂ Aℓ of constant size.


![image 177](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile177.png>)

Recall that Lemma 13 gives σn = (1 ± o(1)) Bℓp2ℓ−1 + Cℓpℓ with Cℓ = Aℓ = Θ(n2ℓ−1) and Bℓ = Θ(n3) by Claim 5 and Lemma 11, respectively. Thus we have σn = Θ( n2pℓℓ−1 (1 + npℓ−1ℓ)) and we distinguish two cases:

![image 178](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile178.png>)

If npℓ−1ℓ ≥ 10, then Mn/σn = O(n1/2p1/2ℓ−1) and Qn/σn ≤ npℓ−1ℓ5/σn = O(n−1/2p−1/2ℓ5). Thus, for any s > 2, we have

Mn σn

![image 179](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile179.png>)

Qn σn

![image 180](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile180.png>)

s−1

= O (np)−(s−2)/2ℓ5(s−1)−1 = o(1),

since np → +∞ polynomially in n and ℓ = o(log n).

Otherwise, we have npℓ−1ℓ ≤ 10 which implies Mn/σn = O(npℓ/2ℓ−1/2) and Qn/σn = O(n−1p−ℓ/2ℓ9/2). Consequently, for any s > 2, we obtain

Mn σn

![image 181](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile181.png>)

Qn σn

![image 182](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile182.png>)

s−1

= O (n2pℓ)−(s−2)/2ℓ(9s−10)/2 .

Next, we recall that by Remark 18 we may additionally assume that p is not too small, e.g. p ≥ εn−max{3/(2ℓ−1),2/(ℓ+1)} for any ε = ε(n) > 0 with ε → 0. It remains to observe that when ε is decreasing suﬃciently slowly this implies that n2pℓ ≫ eΩ(logn)/ℓ. Since ℓ = o(log n), it follows that (16) is satisﬁed and applying Theorem 19 completes the proof of Theorem 1(b).

4. Bivariate fluctuations: proof of Theorem 2

For the rest of this Section, let 3 ≤ ℓ2 = ℓ2(n) < ℓ1 = ℓ1(n) and 0 < p = p(n) < 1 such that

pℓ91 −−−−→

0, (17) n2pℓ

n→+∞

ℓ−1 9 −−−−→

+∞, (18) ℓ1

1

n→+∞

log n −−−−→

0. (19) Our goal is to apply the method of moments (cf. Theorems 3 and 4), therefore we want to determine the asymptotics of the k-th moments E uℓ

![image 183](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile183.png>)

n→+∞

k

X¯ℓ1 σℓ1 + uℓ

X¯ℓ2 σℓ2

![image 184](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile184.png>)

![image 185](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile185.png>)

1

2

![image 186](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile186.png>)

= E(X¯ℓ2

2 ∈ R. (We recall that σℓ

for all k ∈ N and uℓ

) denotes the standard deviation of Xℓ

,uℓ

i

1

i

for i ∈ {1,2}.) By deﬁnition we have

i

k =

  uℓ

X¯ℓ

X¯ℓ

k1(T) uℓ

k2(T)

uℓ

1

2

1

2

ZT (20)

+uℓ

E

E

![image 187](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile187.png>)

![image 188](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile188.png>)

![image 189](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile189.png>)

![image 190](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile190.png>)

2

1

σℓ

σℓ

σℓ

σℓ

1

2

1

2

T∈T

k

T∈ Aℓ

∪Aℓ

1

2

where ki(T) := |{T ∈ T: |T| = ℓi}|, for i ∈ {1,2}, is the number of ℓi-APs in T.

Remark 20. Note that despite our assumption that ℓ1 = ℓ2, our approach also includes the univariate scenario: for 3 ≤ ℓ = ℓ(n) = o(log n) and 0 < p = p(n) < 1

such that pℓ9 → 0 and n2pℓℓ−9 → +∞, we obtain the k-th moment E(X¯ℓk) by setting ℓ2 = ℓ, ℓ1 = 2ℓ, uℓ

= 0. Furthermore, we observe that in the univariate case the additional assumption (18) comes without loss of generality, since we already noticed in Remark 18 that X¯ℓσℓ−1 has a Gaussian limit if n2pℓℓ−1 → +∞ but n2pℓℓ−9 = O(1).

= 1, and uℓ

1

2

- 4.1. Main contribution to the moments. In (20) we expressed the k-th moment


of an arbitrary linear combination of X¯ℓ

and X¯ℓ

as a sum ranging over k-tuples of APs, each of length ℓ1 or ℓ2. We will now show that for even k the main contribution to this sum comes from k-tuples T = (T1,...,Tk) with a certain matching structure, namely there exists a bijective self-inverse mapping ν: [k] → [k] without ﬁxed point (we will call such permutation a matching) such that T satisﬁes

1

2

  = ∅. (21)

 

∀i ∈ [k]: Ti ∩ Tν(i) = ∅ ∧ Ti ∩

Tj

j∈[k]\{i,ν(i)}

We write Fν(k) for the set of (ordered) k-tuples satisfying (21) for a given matching ν, and observe that any two distinct sets Fν(k) and Fν′(k), ν = ν′, are disjoint and can be mapped bijectively onto each other. Thus let ν∗ be deﬁned by

ν∗(2i − 1) = 2i, ∀i ∈ [k/2], and note that there are precisely (k − 1)!! many distinct matchings ν. Let F(k) denote the contribution of k-tuples in F(k) := ˙

νFν(k) to the k-th moment E uℓ

k

X¯ℓ1 σℓ1 + uℓ

X¯ℓ2 σℓ2

, and set F(k) := ∅ for k odd. Then we let G(k) :=

![image 191](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile191.png>)

![image 192](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile192.png>)

1

2

k \ F(k) for all k ∈ N, and denote the contribution of G(k) by G(k). In other words, we have

Aℓ1 ∪ Aℓ2

k  = F(k) + G(k), (22)

  uℓ

X¯ℓ

X¯ℓ

1

2

+ uℓ

E

![image 193](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile193.png>)

![image 194](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile194.png>)

2

1

σℓ

σℓ

1

2

where

- F(k) := T∈F(k)

uℓ

1

![image 195](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile195.png>)

σℓ

1

k1(T) uℓ

2

![image 196](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile196.png>)

σℓ

2

k2(T)

E

T∈T

ZT

- G(k) := T∈G(k)


uℓ

1

![image 197](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile197.png>)

σℓ

1

k1(T) uℓ

2

![image 198](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile198.png>)

σℓ

2

k2(T)

E

ZT .

T∈T

We observe that by the previous argument we may express F(k) as

k/2

F(k) = (k − 1)!!

E

i=1

T∈Fν∗(k)

2i−1|ZT

u|T

2i−1

·

![image 199](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile199.png>)

σ|T

2i−1|

u|T

2i|ZT

2i

![image 200](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile200.png>)

σ|T

2i|

. (23)

2 ∈ R, then we have F(k) = (1 ± o(1))(k − 1)!! u2ℓ

Lemma 21. Let k ∈ 2N and uℓ

,uℓ

1

k/2 .

+ u2ℓ

uℓ

+ 2uℓ

κℓ

1,ℓ2

2

1

2

1

Proof. We enumerate the k-tuples T = (T1,...,Tk) ∈ Fν∗(k) in a speciﬁc order. Deﬁne for j ∈ {1,2},

Θj(T) := {i ∈ [k/2] : |T2i−1| = |T2i| = ℓj}.

and Θ3(T) := [k/2] \ (Θ1 ∪ Θ2). In other words, Θj(T) is the set of intersecting pairs of ℓj-APs in T, j ∈ {1,2}, and Θ3(T) is the set of mixed intersecting pairs.

Let θi := |Θi(T)| for i ∈ {1,2,3} so that 0 ≤ θ1 ≤ k/2, 0 ≤ θ2 ≤ k/2 − θ1 and θ3 = k/2 − θ1 − θ2. We now consider the set [k/2] as a set of distinct “labels”, and partition [k/2] into classes P1, P2, and P3 of sizes θ1, θ2, and θ3, respectively. Note that there are precisely θ k/2

1,θ2,θ3 many choices for this. We proceed in rounds i = 1,...,k/2 where we distinguish three cases according to the i-th label:

- (a) if i ∈ P1, then we choose an integer 1 ≤ mi ≤ ℓ1 and set

- Mi := (T,T′) ∈ A2ℓ1 : |T ∩ T′| = mi ;

(b) if i ∈ P2, then we choose an integer 1 ≤ mi ≤ ℓ2 and set

- Mi := (T,T′) ∈ A2ℓ2 : |T ∩ T′| = mi ;


- (c) and if i ∈ P3, then we choose an integer 1 ≤ mi ≤ ℓ2 and set


Mi := (T,T′) ∈ (Aℓ1 × Aℓ2) ∪ (Aℓ2 × Aℓ1): |T ∩ T′| = mi .

In each case, note that some of the elements (T,T′) of Mi might not be valid choices for (T2i−1,T2i), as T ∪T′ may contain elements from Tj for some j ∈ [2i−2] (thus violating (21) and the deﬁnition of F(k)). Nonetheless, we claim that almost all of them are indeed valid. More formally, let

 

 

  = ∅

 

2i−2

M∗i :=

(T,T′) ∈ Mi: (T ∪ T′) ∩

Tj





j=1

and note that j 2=1i−2 Tj ≤ kℓ1 for all i ∈ [k/2]. Now, observe that we can express (23) by

k/2−θ1

k/2

k/2 θ1,θ2,θ3

u2θ

1+θ3

ℓ1 u2θ

2+θ3 ℓ2

F(k) = (k − 1)!!

θ1=0

θ2=0

  . (24)



k/2

E(ZTZT′) σ|T|σ|T′|

 mi (T,T′)∈M∗i

×

![image 201](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile201.png>)

i=1

Claim 22. For any R ⊆ [n] of size at most kℓ1 we have |{(T,T′) ∈ Mi: (T ∪ T′) ∩ R = ∅}| = o(|Mi|).

Before we prove Claim 22, we show how to complete the argument assuming this statement. Indeed, as the contribution from each term in Mi is the same, Claim 22 shows that the error introduced by replacing M∗i with Mi in (24) is negligible: it is accounted for by a factor of (1 ± o(1)). Moreover, note that

 

E(X¯ℓ2

)/σℓ2

= 1, for i ∈ P1, E(X¯ℓ2

E(ZTZT′) σ|T|σ|T′|

1

1

)/σℓ2

=

= 1, for i ∈ P2, 2E(X¯ℓ

![image 202](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile202.png>)



2

2

X¯ℓ

mi (T,T′)∈Mi

) → 2κℓ

1,ℓ2, for i ∈ P3. Consequently, we obtain

σℓ

)/(σℓ

2

1

1

2

k/2−θ1

k/2

k/2 θ1,θ2,θ3

θ1 u2ℓ

θ2 (2uℓ

1,ℓ2)θ

u2ℓ

F(k) = (1 ± o(1))(k − 1)!!

κℓ

uℓ

3

2

1

1

2

θ1=0

θ2=0

k/2 ,

+ u2ℓ

= (1 ± o(1))(k − 1)!! u2ℓ

uℓ

+ 2uℓ

κℓ

1,ℓ2

2

1

2

1

- as claimed.


Proof of Claim 22. Fix an arbitrary R ⊆ [n] of size at most kℓ1. Denote M′i := {(T,T′) ∈ Mi: (T ∪ T′) ∩ R = ∅}. Note ﬁrst that once T is ﬁxed, the number of choices for T′ with |T ∩T′| ≥ 2 is at most O(ℓ41), as T′ is completely determined by choosing two elements in T (for which there are at most ℓ21 choices) and deciding their positions within T′ (also at most ℓ21 choices).

We ﬁrst deal with the case mi ≥ 2. We will see that |Mi| = Ω(n2/ℓ1) and |M′i| = O(nℓ51), and thus |M′i| = o(|Mi|) since ℓ1 = o(log n). Indeed, note that for every 2ℓ1-AP T′′, we can let T := {T′′(1),...,T′′(|T|)} and T′ := {T′′(|T| − mi + 1),...,T′′(|T| + |T′| − mi)}. Then (T,T′) ∈ Mi. Thus, |Mi| ≥ A2ℓ

=

1

n2

2(2ℓ1−1)(1 − o(1)) by Claim 5. On the other hand, to obtain a pair (T,T′) in M′i, we need to choose ﬁrst some x ∈ (T ∪ T′) ∩ R, which has at most |R| ≤ kℓ1 choices. Then the arithmetic progression containing x, say T, is determined by picking a common diﬀerence, for which there are at most n choices. Then by the observation above, the number of choices for T′ with |T ∩ T′| ≥ 2 is O(ℓ41). Therefore, |M′i| = O(ℓ1 · n · ℓ41) as claimed.

![image 203](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile203.png>)

We then deal with the case mi = 1. Similarly, we show that |Mi| = Ω(n3ℓ−1 2) and |M′i| = O(n2ℓ1), and hence |M′i| = o(|Mi|) since ℓ1 = o(log n). Indeed, to get a pair (T,T′) in Mi, we have at least Aℓ

choices to ﬁx T and then, upon choosing some x ∈ T as its intersection with T′, there are at least ℓn/2

1

1−1 choices to choose the common diﬀerence of T′. This is because if x ≥ n/2 (x ≤ n/2 respectively),

![image 204](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile204.png>)

then we can ﬁnd T′ with x as the last (ﬁrst respectively) element. Again there are

- at most O(ℓ51) such T′ intersecting with T at more than one place, we then have


1 · ℓn/2

1−1 − O(ℓ51) = Ω n3ℓ−1 2 , by Claim 5. On the other hand, a pair in M′i is determined by choosing their single intersection point with R and their common diﬀerences. So |M′i| ≤ |R| · n · n = O(n2ℓ1), completing the proof of the claim.

|Mi| ≥ Aℓ

![image 205](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile205.png>)

As demonstrated earlier, this also completes the proof of Lemma 21. 4.2. Minor contribution to the moments. Next we turn our attention to ktuples in G(k) = Aℓ1 ∪ Aℓ2

k \ F(k), where k ∈ N and F(k) = ∅ if k is odd. Lemma 23. Let k ∈ N, we have

k

i|ZT

u|T

i

= o(1).

G(k) =

E

![image 206](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile206.png>)

σ|T

i|

i=1

T∈G(k)

We start with some preparation. We will change the order of summation in an algorithmic fashion as described below. First we ﬁx an arbitrary total order π of the set Aℓ1 ∪ Aℓ2 such that all ℓ1-APs come before any ℓ2-AP, i.e. we have π(T) < π(T′) for all T ∈ Aℓ1 and T′ ∈ Aℓ2. We now explore any (non-empty) ﬁnite collection of APs component by component. Roughly speaking, given T, let H be an auxiliary k-vertex graph, in which each vertex represents an AP in T and two vertices are adjacent if and only if the corresponding APs have nonempty intersection. Then we will explore V (H), moving from one vertex to one of its neighbours according to the ordering π and start the search from a new component whenever the current one is exhausted. For T ∈ k∈N Aℓ1 ∪ Aℓ2

k, we set |T| := inf k ≥ 1 : T ∈ Aℓ1 ∪ Aℓ2

k . More precisely, we perform the following algorithm:

![image 207](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile207.png>)

k.

INPUT: T ∈ k∈N Aℓ1 ∪ Aℓ2

- (I) Initialise the inactive list Li and active list La: Li ← T, La ← ∅, and j ← 1.
- (II) Start a new component: If La = ∅, then let La ← {minπ Li}.
- (III) Set:

Tj ← min

π

La, sj ← |Tj|, (size of the current AP)

tj ← Tj ∩

j−1

j′=1

Tj′ , (size of the overlap with previous APs)

C ← {T ∈ Li: T ∩ Tj = ∅}. (current component)

- (IV) Update:

La ← (La ∪ C) \ {Tj}, Li ← Li \ C.

- (V) If j = |T|, then STOP; otherwise, set j ← j + 1 and return to step (II).


OUTPUT: π(T) := (T1,...,T|T|) and τ(T) := (t,s), where t = (t1,t2,...,t|T|) and s = (s1,s2,...,s|T|).

![image 208](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile208.png>)

Note that any permutation T′ of the input T will result in the same ordered

tuple π(T′) = (T1,...,T|T|). We now assume that |T| = k. Observe that t and s satisfy

∀i ∈ [k]: si ∈ {ℓ1,ℓ2}, (25) ∀i ∈ [k]: 0 ≤ ti ≤ si, (26) ∀i ∈ [k]: {ti = 0} =⇒ {si = ℓ1} ∨ {sj = ℓ2, ∀j = i,...,k}, (27)

where (27) follows from the choice of π. For r ∈ {0,1,...,ℓ1} and j ∈ {1,2} we deﬁne index sets Ir,ℓ

:= {i ∈ [k]: ti = r, si = ℓj}, Ir := Ir,ℓ

1 ∪ Ir,ℓ

. Additionally, note that if the input T is such that there exists i ∈ [k − 1] for which ti = ti+1 = 0, then Ti is disjoint from j∈[k]\{i} Tj implying E kj=1 ZT

j

2

i · E j∈[k]\{i} ZT

= EZT

j

= 0, i.e. such T does not contribute to G(k). Consequently, we have

j

∀i ∈ [k − 1]: ti + ti+1 > 0. (28) Similarly, tk > 0, since otherwise ZT

) and thus T does not contribute to G(k). We write

is independent from (ZT

# ,...,ZT

1

k

k−1

Tk := {t ∈ {0,1,...,ℓ1}k: t satisﬁes (28) and tk > 0} for the set of all type vectors of length k which do not contain two consecutive zeros and do not end in a zero. In particular, this implies that we may assume |I0| ≤ k2 − 1 for even k and |I0| ≤ k−21 for odd k, in other words, we have

![image 209](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile209.png>)

![image 210](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile210.png>)

2| ≤ ⌈k/2⌉ − 1. (29) Next, for any type vector t ∈ {0,1,...,ℓ1}k, we deﬁne the set of valid size-type

1| + |I0,ℓ

|I0,ℓ

vectors

Sk(t) := s ∈ {ℓ1,ℓ2}k: (t,s) satisﬁes (25), (26), and (27) .

The main idea is to enumerate the sum in (20) by ﬁrst choosing the vector t ∈ {0,1,...,ℓ1}k, then a valid size-type vector s ∈ Sk(t), and lastly a tuple (T1,...,Tk) ∈ G(k) such that τ(T1,...,Tk) = (t,s). In terms of formula, we obtain

u|T|ZT σ|T|

Mt,s · µt,s, (30)

G(k) =

=

E

![image 211](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile211.png>)

t∈Tk s∈Sk(t) T∈G(k) τ(T)=(t,s)

t∈Tk s∈Sk(t)

T∈T

where

Mt,s := |{T ∈ G(k): τ(T) = (t,s)}| denotes the number of tuples with given type vectors (t,s), and

  1

 

us

i

1 ···ZT

E(ZT

µt,s :=

)

![image 212](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile212.png>)

![image 213](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile213.png>)

k

σs

Mt,s

i

T∈G(k) τ(T)=(t,s)

i∈[k]

is the average contribution to G(k) of a k-tuple with given type vectors (t,s). We ﬁrst aim to bound the average contribution µt,s.

- Proposition 24. Let t ∈ Tk and s ∈ Sk(t), then we have


 

  p i∈[k](si−ti).

us

i

µt,s = (1 ± o(1))

![image 214](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile214.png>)

σs

i

i∈[k]

Proof. Let T = (T1,...,Tk) ∈ G(k) with τ(T) = (t,s). Here T1,...,Tk are in the order corresponding to the output of the exploring algorithm, hence we have |Ti| = si. We see that

 

  .

 =

 

{Ti⊆[n]p} − p|T

i|

−ps

Ti ⊆ [n]p

1 ···ZT

E(ZT

) = E

i P

k

R⊆[k] i∈R

i ∈R

i∈[k]

First observe that the summand Q∅ for R = ∅ is given by

  = p

 

k

i=1(si−ti),

Ti ⊆ [n]p

Q∅ := P

i∈[k]

- as si − ti = |Ti \ ∪i′≤i−1Ti′| and so i∈[k](si − ti) = | ∪i∈[k] Ti|. Thus, it only remains to show that the remaining (constantly many) summands are all of lower order.


Let r ∈ [k] and ﬁx an arbitrary subset R ⊆ [k] of size r. The absolute value of its contribution to E(ZT

1 ···ZT

) is equal to

k

  = p i∈R si+|∪i/∈RTi|.

 

ps

Ti ⊆ [n]p

QR :=

i P

i∈R

i ∈R

Note that

si + | ∪i/∈R Ti| =

i∈R

|Ti| + | ∪i/∈R Ti| ≥ | ∪i∈[k] Ti| =

i∈R

(si − ti).

i∈[k]

Furthermore, if this last inequality is not an equality, then QR ≤ p

k

k

i=1(si−ti) , i.e. QR is negligible compared to Q∅.

i=1(si−ti)+1 = o p

Next, suppose towards contradiction that the equality holds, so

|Ti| = | ∪i∈[k] Ti| − | ∪i/∈R Ti|. But at the same time we have

i∈R

|Ti| ≥ | ∪i∈R Ti| ≥ | ∪i∈[k] Ti| − | ∪i/∈R Ti|,

i∈R

and thus all intermediate inequalities above must be equalities. This happens for the ﬁrst inequality when {Ti}i∈R are pairwise disjoint and for the second inequality when (∪i∈RTi) ∩ (∪i/∈RTi) = ∅. But this in turn implies that for any i ∈ R, the set Ti is disjoint from ∪j =iTj, so ti = ti+1 = 0, contradicting (28).

Because these bounds are uniform over the choice of the k-tuple T the statement follows by taking the average.

We now aim at bounding the number of summands Mt,s. To do so, recall that in the dependency graph Gℓ1,ℓ2 deﬁned in (12), each vertex represents an AP in Aℓ1 ∪Aℓ2, and two vertices form an edge if and only if the corresponding APs have non-empty intersection.

- Proposition 25. For all t ∈ Tk and s ∈ Sk(t), we have


|I0|

n2 sr

rj+1=1}(s2r

s2r

j+1) {t

j+1) {t

· (nsr

Mt,s = O(1) ·

![image 215](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile215.png>)

j

j

j=1

rj+1−1

·

i=rj+2

rj+1≥2}− {tr

j+1=srj+1=srj

}

(s2i ℓ21)

(nℓ1)

{ti=1}

{ti≥2}

.

Proof. First, note that for any T such that τ(T) = (t,s) and π(T) = (T1,...,Tk), the component structure of the induced subgraph Gℓ1,ℓ2 i∈[k] Ti is already determined by the type-vector t. More precisely, for j = 1,...,|I0|, let

rj := min{i ∈ [k] \ {r1,...,rj−1}: ti = 0} denote the j-th zero entry of t, and set r|I

0|+1 := k + 1. Note that r1 = 1 and {Tr

j+1−1} forms a component of Gℓ1,ℓ2 i∈[k] Ti for all j = 1,...,|I0|.

,...,Tr

j

We will construct tuples T with τ(T) = (t,s) in the order given by its reordering π(T) = (T1,...,Tk). In particular, this means that we consider one component of Gℓ1,ℓ2 i∈[k] Ti after the other. Let j = 1,...,|I0| and assume that T1,...,Tr

j−1

have already been chosen. Observe that, by (28), the j-th component contains at least two APs Tr

and Tr

j

starts a new component (tr

j+1. As Tr

is

= 0), the number of choices for Tr

j

j

j

= O(n2s−r 1

) by Claim 5. Next we choose Tr

- at most As


j+1:

rj

j

- (a) if tr

j+1 = 1, then the number of choices is at most O(nsr

j

), since there are at most sr

j

choices for the common vertex x ∈ Tr

j ∩ Tr

j+1, at most sr

j+1 choices for the position of x within Tr

j+1 and O(n/sr

j+1) for the common diﬀerence of Tr

j+1;

- (b) if tr

j+1 = sr

j+1 = sr

j

, then there is only one possibility Tr

j+1 = Tr

j

;

- (c) otherwise, Tr


and their respective positions within Tr

j+1 is determined by choosing two elements from Tr

j

j+1, which amounts to at most O(s2r

s2r

j+1) many choices.

j

Similarly, for any remaining i = rj + 2,...,rj+1 − 1 (there might be none), we use the following bounds on the number of choices for Ti:

- (a) if tr

j+1 = 1, then the number of choices is at most O(nℓ1), since there are at most O(ℓ1) choices for the common vertex x ∈ Ti ∩ Tr

j ∪ ··· ∪ Ti−1 , at most si choices for the position of x within Ti and O(n/si) for the common diﬀerence of Ti;

- (b) otherwise, Ti is determined by choosing two elements from Tr


j ∪ ···∪ Ti−1 and

their respective positions within Ti, which amounts to at most O(ℓ21s2i ) many choices.

The claim follows by multiplying for all j = 1,...,|I0| and i = rj,...,rj+1 − 1.

With this preparation we are now ready to prove Lemma 23. We will bound the contribution of each k-tuple to G(k) = t,s µt,sMt,s from above component-wise

Proof of Lemma 23. First observe that Lemma 13 implies that for any ℓ ≥ 3 we have

5

σℓ−1 = O(Aℓpℓ)−1/2 C.

= O(n−1p−ℓ/2ℓ1/2), (31) and also

11

σℓ−1 = O(Bℓp2ℓ−1)−1/2 L.

= O(n−3/2p−ℓ+1/2). (32) Using Propositions 24 and 25 the expression in (30) becomes

gt,s(i)σs−1

G(k) = O(1) ·

, (33)

i

t∈Tk s∈Sk(t) i∈[k]

where



n2s−i 1ps

if ti = 0; nsips

i

i−1 if ti = 1 ∧ ti−1 = 0; nℓ1ps

i−1 if ti = 1 ∧ ti−1 > 0; 1 if ti = si = si−1 ∧ ti−1 = 0; s2is2i−1ps



gt,s(i) :=

i−ti if 2 ≤ ti ≤ si − 1 ∧ ti−1 = 0; s2is2i−1 if ti = si ∧ si = si−1 ∧ ti−1 = 0; s2iℓ21ps



i−ti if ti ≥ 2 ∧ ti−1 > 0.

Moreover, we recall the notation rj = min{i ∈ [k] \ {r1,...,rj−1}: ti = 0} and r|I

0|+1 := k + 1 used in the proof of Proposition 25. These indices split the interval [k] into |I0| parts, i.e. [k] = ˙ |I

0|

j=1{rj,...,rj+1 − 1}, where each part has size at least two as, by (28), t does not have consecutive zeros. Now, ﬁx any j ∈ [|I0|]. We ﬁrst bound the ﬁrst two factors together:

- (a) If tr

j+1 = 1, then we have gt,s(rj)gt,s(rj + 1)

![image 216](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile216.png>)

σs

rj

σs

rj+1

= n2s−r 1

j

ps

rj

· nsr

j+1ps

rj+1−1 · σs−1

rj

σs−1

rj+1

(32=) O(1),

because the validity condition (27) implies sr

j+1 ≤ sr

j

, since tr

j

= 0 .

- (b) If 2 ≤ tr

j+1 ≤ sr

j+1 − 1, then we have gt,s(rj)gt,s(rj + 1)

![image 217](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile217.png>)

σs

rj

σs

rj+1

= n2s−r 1

j

ps

rj

· s2r

j

s2r

j+1ps

rj+1−trj+1 · σs−1

rj

σs−1

rj+1

(31=) O p1+(s

rj−srj+1)/2ℓ41 = o(ℓ−1 1) since pℓ51 → 0, by assumption (17).

- (c) If tr

j+1 = sr

j+1 ≤ sr

j − 1, then we have gt,s(rj)gt,s(rj + 1)

![image 218](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile218.png>)

σs

rj

σs

rj+1

= n2s−r 1

j

ps

rj

· s2r

j

s2r

j+1 · σs−1

rj

σs−1

rj+1

(31=) O p(s

rj−srj+1)/2ℓ41 = o(1), since p1/2ℓ41 → 0, by assumption (17).

- (d) If tr


j+1 = sr

j+1 = sr

, then we have gt,s(rj)gt,s(rj + 1)

j

(31=) O(1).

ps

· σs−1

= n2s−r 1

σs−1

rj

![image 219](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile219.png>)

σs

σs

j

rj

rj+1

rj

rj+1

We now treat any (potentially) remaining indices i = rj + 2,...,rj+1 − 1 and estimate gt,s(i)σs−1

one by one.

i

- (a) If ti = 1, then we have

gt,s(i)σs−1

i

= nℓ1ps

i−1σs−1

i

(32=) O((np)−1/2ℓ1) = o(1), since 3 ≤ ℓ1 = o(log n) and np = Ω(n1−2/ℓ

1

) = nΩ(1), by assumption (18).

- (b) If 2 ≤ ti ≤ si − 1, then we have

gt,s(i)σs−1

i

≤ s2i ℓ21ps

i−tiσs−1

i

= O(pℓ41) = o(ℓ−1 1), since σs−1

i

= O(1) by assumption (18) and because pℓ51 → 0, by assumption (17).

- (c) However, if ti = si, then we have


ℓ41) (31=) O(n−1p−ℓ

1/2ℓ91/2) = o(1), since n2pℓ

= O(σℓ−1

gt,s(i)σs−1

≤ s2iℓ21σs−1

i

i

1

ℓ−1 9 → +∞, by assumption (18).

1

Next, we observe that by (29), we have |I0| ≤ ⌈k/2⌉ − 1, implying that there must be at least one j ∈ |I0| such that there exists an integer i0 satisfying rj + 2 ≤ i0 ≤ rj+1 − 1. But then, the previous computation shows that the corresponding factor gt,s(i0)σs−1

must be small. More precisely, we have

i0

= o(1) · ℓ−

≤si0

−1}

{2≤ti0

gt,s(i0)σs−1

1 . Consequently, from (33) and multiplying the bounds for all i ∈ [k] we obtain G(k) = O(1) ·

i0

o(ℓ−1 Q(t,s)),

t∈Tk s∈Sk(t)

where

Q(t,s) := |{i ∈ [k]: 2 ≤ ti ≤ si − 1}|. Last, for any q ∈ {0,1,...,k}, the number of summands with Q(·) = q is at most ℓq13k−q2k = O(ℓq1) yielding

G(k) = o(1), thereby completing the proof of Lemma 23.

4.3. Completing the argument: application of the method of moments. It remains to apply the method of moments to show the convergence to a (bivariate) Gaussian distribution.

Proof of Theorem 2. Recall from (22) that we have

  uℓ

k  = F(k) + G(k),

X¯ℓ

X¯ℓ

1

2

+ uℓ

E

![image 220](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile220.png>)

![image 221](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile221.png>)

1

2

σℓ

σℓ

1

2

2 ∈ R. Furthermore, we have computed the asymptotics for F(k) and G(k) in Lemmas 21 and 23, implying that for even k we have

for all k ∈ N and uℓ

,uℓ

1

k  = (1 ± o(1))(k − 1)!! u2ℓ

  uℓ

X¯ℓ

X¯ℓ

k/2 ,

+ u2ℓ

1

2

+ 2κℓ

+ uℓ

uℓ

1,ℓ2uℓ

E

![image 222](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile222.png>)

![image 223](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile223.png>)

2

2

1

1

σℓ

σℓ

2

1

1

2

and for odd k we have

k  = o(1).

  uℓ

X¯ℓ

X¯ℓ

1

2

+ uℓ

E

![image 224](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile224.png>)

![image 225](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile225.png>)

2

1

σℓ

σℓ

1

2

Letting n → +∞ we obtain the k-th moments of the bivariate standard Gaussian distribution with covariance κℓ

1,ℓ2. Hence, Theorems 3 and 4 imply that X ¯ℓ

X¯ℓ

0 0

1 κℓ

−−−−→ d n→+∞

1,ℓ2 κℓ

1

2

,

N

.

,

![image 226](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile226.png>)

![image 227](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile227.png>)

1,ℓ2 1

σℓ

σℓ

1

2

The distinction of the diﬀerent regimes in Theorem 2 follows from Lemma 14, completing the proof.

The same proof also applies for the study of univariate ﬂuctuations.2

Alternative proof of Theorem 1(b). For 3 ≤ ℓ = ℓ(n) = o(log n) and 0 < p = p(n) < 1 such that pℓ9 → 0 and n2pℓℓ−9 → +∞, we obtain

k

X ¯ℓ σℓ

(1 ± o(1))(k − 1)!! for k even, o(1) if for k odd,

=

E

![image 228](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile228.png>)

= 0. Letting n → +∞ Theorem 3 shows that

= 1, and uℓ

from Lemmas 21 and 23 by setting ℓ2 = ℓ, ℓ1 = 2ℓ, uℓ

1

2

X¯ℓ σℓ

−−−−→d n→+∞

N(0,1), as claimed.

![image 229](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile229.png>)

5. Concluding remarks

The main topic at stake in this article was to study the joint distribution of the numbers of APs of diﬀerent length in some random subsets M of the integers. In the most general setup, we would like to understand the growth behaviour of the family {Xℓ}3≤ℓ≤n where Xℓ = Xℓ(M) denotes the number of ℓ-APs of integers which are (entirely) contained in M. Here, we took a ﬁrst step in this direction by determining the joint limiting distribution of (Xℓ

) in M = [n]p for a signiﬁcant range of parameters p and 3 ≤ ℓ2 < ℓ1 = o(log n). We believe that our approach should also allow us to determine the limiting distribution of r-tuples (Xℓ

,Xℓ

1

2

) for r ≥ 3 (within the intersection of their respective Gaussian

,Xℓ

,...,Xℓ

1

2

r

regimes), hence, to give a functional Central Limit Theorem for e.g. X⌊sℓ⌋ s∈[0,1] with ℓ = ℓ(n) = o(log n). In particular, it would be interesting to know whether

for some constants ℓ1,ℓ2,...,ℓr, with (constant) r ≥ 3, the Gaussian limit becomes degenerate. We observed it for r = 2 when ℓ1 = ℓ1(n),ℓ2 = ℓ2(n) → +∞ suﬃciently slowly: Xℓ

are then either asymptotically uncorrelated or converge to the same Gaussian random variable (after re-normalisation).

and Xℓ

1

2

ℓ−1 9 → +∞ which guarantees that both Xℓ

Furthermore, recall that Theorem 2 uses the assumption n2pℓ

1

are within their respective Gaussian regimes. One may thus ask what happens for smaller values of p. At least heuristically, our results for the overlap pair regime (i.e. npℓ

and Xℓ

1

2

1−1ℓ1 → 0) suggest that a good candidate for

![image 230](<2019-barhoumiandreani-bivariate-fluctuations-number-arithmet_images/imageFile230.png>)

2Albeit with the mild additional assumption pℓ9 → 0 for technical reasons.

the joint limit consists of two independent random variables having the appropriate marginal distributions (Gaussian or Poisson) determined in Theorem 1.

Throughout the article, we focused on ℓ-APs where ℓ = o(log n), the reason being that typically the random set [n]p will not contain any longer APs as long as p = o(1). In order to witness any ℓ-APs with ℓ/ logn → +∞ we would need to consider p = p(n) → 1. Borrowing some intuition from Gao and Sato’s work [14] on large matchings in the random graph G(n,p) – namely the log-normal paradigm of Gao [13] – we might expect to see another change of regime to a Log-normal limiting distribution for very long APs. However, in this regime, various estimates derived in this paper cease to hold and we leave this as an open problem.

Another question of interest concerns the behaviour of the joint cumulants of (Xℓ

) in the various regimes encountered here. In the Gaussian regime, since the moments of the rescaled random variables converge to the Gaussian moments, their cumulants of order r ≥ 3 converge to 0. One can ask if the BFS coding allows to see such a behaviour in a ﬁne way, for instance with an asymptotic expansion.

,Xℓ

1

2

Lastly, we would like to move in a slightly diﬀerent direction: let 0 < s < t and consider the coupling [⌊tn⌋]p = [⌊sn⌋]p ∪ {⌊sn⌋ + 1,...,⌊tn⌋}p for any p ∈ [0,1]. What can be said about the joint distribution of Xℓ([⌊sn⌋]p),Xℓ([⌊tn⌋]p) ? More generally, does the random process Xℓ([⌊tn⌋]p) t≥0 satisfy a functional central limit theorem? What about X⌊sℓ⌋([⌊tn⌋]p) s,t≥0 for ℓ = ℓ(n) = o(log n)?

References

- [1] R. Arratia, L. Goldstein, L. Gordon, Two moments suﬃce for Poisson approximations: The Chen-Stein method, Ann. Probab. 17:9–25 (1989).
- [2] B.B. Bhattacharya, S. Ganguly, X. Shao, Y. Zhao, Upper tails for arithmetic progressions in a random set, arXiv preprint, arXiv:1605.02994 (2016).
- [3] P. Billingsley, Probability and Measure, John Wiley & Sons (2008).
- [4] B. Bollob´as, To prove and conjecture: Paul Erd˝s and his mathematics, The American Mathematical Monthly, 105(3):209–237 (1998).
- [5] B. Bollob´as, O. Cooley, M. Kang, and C. Koch, Jigsaw percolation on random hypergraphs, Journal of Applied Probability, 54(4):1261–1277 (2017).
- [6] J. Bri¨et, and S. Gopi, Gaussian width bounds with applications to arithmetic progressions in random settings, arXiv preprint, arXiv:1711.05624 (2017).
- [7] S. Chatterjee, An introduction to large deviations for random graphs, Bulletin of the American Mathematical Society, 53(4):617–642 (2016).
- [8] S. Chatterjee, A. Dembo, Nonlinear large deviations, Advances in Mathematics, 299:396–450

(2016).

- [9] H. Cram´er, On the order of magnitude of the diﬀerence between consecutive prime numbers Acta Arithmetica, 2:23–46 (1936).
- [10] P. G. L. Dirichlet, Beweis des Satzes, dass jede unbegrenzte arithmetische Progression, deren erstes Glied und Diﬀerenz ganze Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele Primzahlen entha¨lt, Abhandlungen der K¨niglichen Preußischen Akademie der Wissenschaften zu Berlin, 48 45–71 (1837).
- [11] R. Eldan, Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations, arXiv preprint arXiv:1612.04346 (2016).
- [12] V. F´eray, Weighted dependency graphs, arXiv preprint, arXiv:1605.03836 (2016).
- [13] P. Gao, Distributions of sparse spanning subgraphs in random graphs, SIAM J. Discrete Math., 27(1):386–401 (2013).
- [14] P. Gao, C.M. Sato, A transition of limiting distributions of large matchings in random graphs, J. Combin. Theory Ser. B, 116:57–86 (2016).
- [15] B. Green, T. Tao, The primes contain arbitrarily long arithmetic progressions, Annals of Math., 167:481–547 (2008).


- [16] S. Janson, Normal convergence by higher semiinvariants with applications to sums of dependent random variables and random graphs, Annals of Probability, 16(1):305–312 (1988).
- [17] S. Janson, T.  Luczak, A. Rucin´ski, Random graphs, volume 45 of Wiley Series in Discrete Mathematics and Optimization. Wiley-Interscience (2000).
- [18] S. Janson, K. Oleszkiewicz, A. Rucin´ski, Upper tails for subgraph counts in random graphs, Israel Journal of Mathematics, 142(1):61–92 (2004).
- [19] S. Janson, A. Rucin´ski, The infamous upper tail, Random Structures & Algorithms, 20(3):317–342 (2002).
- [20] S. Janson, L. Warnke, The lower tail: Poisson approximation revisited, Random Structures & Algorithms, 48(2):219–246 (2016).
- [21] Y. Kohayakawa, T.  Luczak, V. Ro¨dl, Arithmetic progressions of length three in subsets of a random set, Acta Arithmetica, 75(2):133–163 (1996).
- [22] B.D. McKay, Asymptotics for symmetric 0 − 1 matrices with prescribed row sums., Ars Combin., 19:15–25 (1985).
- [23] V.G. Mikhailov, On a theorem of Janson, Theory of Probability & Its Applications, 36(1):173– 176 (1991).
- [24] F. Mousset, A. Noever, K. Panagiotou, W. Samotij, On the probability of nonexistence in binomial subsets arXiv preprint, arXiv:1711.06216 (2017).
- [25] SageMath, the Sage Mathematics Software System (Version 8.3), http://www.sagemath.org/

(2018).

- [26] E. Szemer´edi, On sets of integers containing k elements in arithmetic progression, Acta Arithmetica, 27(1):199–245 (1975).
- [27] L. Warnke, Upper tails for arithmetic progressions in random subsets, Israel J. Math., 221(1):317–365 (2017).


