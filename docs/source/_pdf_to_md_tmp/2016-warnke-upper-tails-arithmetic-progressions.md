arXiv:1612.08559v1[math.CO]27Dec2016

Upper tails for arithmetic progressions in random subsets

Lutz Warnke∗ July 10, 2013; revised March 14, 2016

Abstract

We study the upper tail of the number of arithmetic progressions of a given length in a random subset of {1, . . . , n}, establishing exponential bounds which are best possible up to constant factors in the exponent. The proof also extends to Schur triples, and, more generally, to the number of edges in random induced subhypergraphs of ‘almost linear’ k-uniform hypergraphs.

# 1 Introduction

What is the (typical) behaviour of a given function depending on many independent random variables ξj? This fundamental concentration-of-measure question is of great interest in various areas of pure and applied mathematics, including functional analysis, statistical mechanics, and theoretical computer science. In applications, concentration inequalities are particularly important: these quantify random ﬂuctuations of

- X = f(ξ1,...,ξn) by bounding the probability that X deviates signiﬁcantly from its mean EX. During the last decades a wide variety of diﬀerent methods for proving such inequalities have been developed (see, e.g., [28, 13, 6]), including martingale based methods [30, 27], Talagrand’s methodology [42], combinatorial approaches [24], and information theoretic methods [12, 5].


Despite this large body of work, in concrete applications our understanding is often still far from satisfactory – even if we restrict our attention to the important case where X is a sum of (dependent) indicator variables and ξj ∈ {0,1}. For example, in probabilistic combinatorics the random variable X often counts objects, for instance the number of certain subgraphs in random graphs. Here Janson’s and Suen’s inequalities [19, 20, 26, 33] usually give sharp estimates for the lower tail P(X ≤ (1 − ε)EX). In contrast, obtaining tight estimates for P(X ≥ (1 + ε)EX) is more delicate, and this ‘upper tail problem’ is well-known to be a technical challenge (see, e.g., [23, 25]).

In fact, in many such counting problems each indicator variable depends only on a few ξj, in which case X has a special structure: it is a low-degree polynomial of independent Bernoulli random variables. With this in mind, it is surprising that, despite intensive research of Kim and Vu [27, 43] and many others (see, e.g., [24, 39, 45, 28, 13, 6]), there is no concentration inequality that routinely gives the ‘correct’ upper tail behaviour in these basic situations. Consequently the investigation of these and related problems is an important issue – not only from an applications point of view, but also as a question in concentration-ofmeasure.

In this context, Janson, Oleszkiewicz and Ruci´nski [22] developed in 2002 a moment-based method that, for subgraph counts in random graphs, gives estimates for P(X ≥ (1 + ε)EX) which are best possible up to logarithmic factors in the exponent. Subsequently, Janson and Ruci´nski [25] extended this technique so that it also gives comparable estimates for arithmetic progressions in random subsets. To be more concrete, given k ≥ 3, let X be the number of arithmetic progressions of length k in [n]p, the random subset of [n] = {1,...,n} where each element is included independently with probability p. In [25] it was shown that for essentially all p and ε > 0 of interest we have

√EX , (1)

√EX log(1/p) ≤ P(X ≥ (1 + ε)EX) ≤ exp −c(ε,k)

![image 1](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile1.png>)

![image 2](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile2.png>)

exp −C(ε,k)

![image 3](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile3.png>)

∗Department of Pure Mathematics and Mathematical Statistics, University of Cambridge, Wilberforce Road, Cambridge CB3 0WB, UK. E-mail: L.Warnke@dpmms.cam.ac.uk.

determining, as in [22], the upper tail up to a factor of O(log(1/p)) in the exponent for constant ε. The problem of closing this logarithmic gap in the approach of Janson et al. [22, 25] has remained open for several years, and only very recently have there been some breakthroughs by Chatterjee [7] and DeMarco and Kahn [10, 11] for certain subgraph counts.

In this paper we solve the upper tail problem for a wide class of random variables, including arithmetic progressions and Schur triples, by establishing upper and lower bounds which match up to constant factors in the exponent. For simplicity, we ﬁrst consider the special case of arithmetic progressions (in Section 1.1 we turn to the general results). In particular, (2) below shows that log P(X ≥ (1 + ε)EX) = −Θ(min{EX,

√EX log(1/p)}) for constant ε, closing the log(1/p) gap that was present until now.

![image 4](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile4.png>)

- Theorem 1. Given k ≥ 3, let X = Xk,n,p be the number of arithmetic progressions of length k in [n]p. Set µ = EX. There are n0,b,B > 0 (depending only on k) such that for all n ≥ n0, p ∈ (0,1] and ε > 0 we have

{1≤(1+ε)µ≤Xk,n,1} exp −C(ε)Φ ≤ P(X ≥ (1 + ε)µ) ≤ exp −c(ε)Φ , (2) where Φ = min µ,√µlog(1/p) , c(ε) = b min{ε3,ε1/2} and C(ε) = B max{1,ε2}.

![image 5](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile5.png>)

Note that µ = EX = Θ(n2pk), and that p and ε may depend on n (we do not assume n ≥ n0(ε), ε = Θ(1) or p ≥ n−2/k, which are common in this context). The additional condition (1+ε)µ ≤ Xk,n,1 assumed for the lower bound is necessary (and also implies p ≤ (1 + ε)−1/k < 1); otherwise X ≥ (1 + ε)µ is impossible. The condition (1 + ε)µ ≥ 1, which holds automatically under common assumptions such as µ = ω(1) or µ ≥ 1, is natural; otherwise P(X ≥ (1 + ε)µ) = P(X ≥ 1). The form of the exponent in (2) can be motivated as follows. Since an interval [m] = {1,...,m} contains Θ(m2) arithmetic progressions of length k, for suitable

- m = Θ(√µ) we have P(X ≥ 2µ) ≥ P([m] ⊆ [n]p) = pΘ(√µ) = e−Θ(√µlog(1/p)). Moreover, for small p (say, p = n−2/k) we expect that X is approximately Poisson, which suggests P(X ≥ 2µ) ≈ e−Θ(µ). Theorem 1 essentially states that the larger of these bounds determines the decay of the upper tail for constant ε.


![image 6](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile6.png>)

![image 7](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile7.png>)

![image 8](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile8.png>)

A weakness of Theorem 1 is that is does not guarantee a similar dependence of c(ε) and C(ε) on ε. Although results of this form (see, e.g., [7, 11, 10, 22]) are the widely accepted standard for the ‘infamous’ upper tail problem [23], here we go much further. Our next result establishes, over a wide range of the parameters, the dependence of the upper tail on ε, up to constants (that are independent of ε). In the language of large deviations, (3) below determines, for p bounded away from one, the order of magnitude of the large deviation rate function log P(X ≥ (1 + ε)EX) for all ε ≥ n−α of interest.

- Theorem 2. Given k ≥ 3, let X = Xk,n,p be the number of arithmetic progressions of length k in [n]p. Set µ = EX and ϕ(x) = (1 + x)log(1 + x) − x. Given γ ∈ (0,1), there are n0,α > 1/(6k) (depending only on k) and c,C > 0 (depending only on γ,k) such that for all n ≥ n0, p ∈ (0,1−γ] and ε ≥ n−α satisfying Φ(ε) ≥ 1 we have

{1≤(1+ε)µ≤Xk,n,1} exp −CΦ(ε) ≤ P(X ≥ (1 + ε)µ) ≤ exp −cΦ(ε) , (3) where Φ(ε) = min ϕ(ε)µ2/ VarX,√εµlog(1/p) .

![image 9](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile9.png>)

It is not hard to check that VarX = Θ(µ(1+npk−1)) for p bounded away from one (see, e.g., Example 3.2 and Lemma 3.5 in [21]). Note that the condition Φ(ε) ≥ 1 is natural since our focus is on exponentially small probabilities. The function ϕ(x) appears in standard Chernoﬀ bounds; it satisﬁes ϕ(x) = Θ(xlog(1 + x)) for x ≥ 0, so that ϕ(x) = Θ(x2) as x → 0. The proof of Theorem 2 shows that the form of the exponent in (3) is determined by Normal approximation considerations (the ϕ(ε)µ2/ VarX term) and the interval clustering idea (the √εµlog(1/p) term). The sharp estimates of Theorem 2 are conceptually quite diﬀerent from previous work on the upper tail problem. Indeed, somewhat related work for subgraph counts in the binomial random graph Gn,p (which aims to determine the precise constants in the exponent as n → ∞, see, e.g., [8, 9, 29]) focuses on the case where ε is constant and p is large (with p = Θ(1) or p ≥ n−δ). In fact, for moderately large p, our next result completely resolves the qualitative behaviour of the upper tail.

![image 10](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile10.png>)

- Theorem 3. Given k ≥ 3, let X = Xk,n,p be the number of arithmetic progressions of length k in [n]p. Set µ = EX. Given γ ∈ (0,1), there are n0 > 0 (depending only on k) and c,C > 0 (depending only on γ,k)


√VarX we have

such that for all n ≥ n0, (log n)1/(k−1)n−1/(k−1) ≤ p ≤ 1 − γ and t ≥

![image 11](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile11.png>)

{µ+t≤Xk,n,1} exp −CΨ(t) ≤ P(X ≥ µ + t) ≤ exp −cΨ(t) , (4)

where Ψ(t) = min t2/ VarX,√tlog(1/p) .

![image 12](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile12.png>)

Finally, as the reader can guess, in Theorem 2 and 3 various conditions (for ε and p) are not best possible. However, for ease of exposition we defer more precise results to the next section, where we state our more general tail estimates (which include Theorems 1–3 as special cases or corollaries). Here we just mention that there is a tradeoﬀ between p and t = εµ in Theorem 2 and 3. Indeed, Theorem 2 works for all 0 < p ≤ 1−γ, but (3) is restricted to deviations of form ε ≥ n−α (for some ﬁxed α > 0). By contrast, Theorem 3 requires n−1/(k−1)+o(1) ≤ p ≤ 1 − γ, but (4) applies to essentially all exponentially small deviations t > 0 (note that Ψ(t) ≤ 1 for t ≤

√Var X).

![image 13](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile13.png>)

1.1 Counting edges of random induced subhypergraphs

In this section we present the main results of this paper, Theorem 4 and 6, which resolve the upper tail problem (up to constant factors in the exponent) for a large class of random variables, including arithmetic progressions and Schur triples. We shall phrase our results in the language of random induced subhypergraphs. More precisely, given a k-uniform hypergraph H with vertex set V (H), let Vp(H) be the random subset of V (H) where each vertex is included independently with probability p. Deﬁne Hp = H[Vp(H)] and

X = e(Hp),

so that X counts the number of edges induced by Vp(H). Note that EX = e(H)pk. Random variables of this form occur frequently in probabilistic combinatorics (see, e.g, [34, 23, 38, 15, 47, 36]), and, in the setting of Theorems 1–3, the edges of H = Hn are all k-subsets {x1,...,xk} ⊆ [n] = V (H) forming an arithmetic progression of length k. To state our results, we deﬁne

∆j(H) = max

|{f ∈ H : S ⊆ f}|,

S⊆V (H):|S|=j

which for j ∈ {1,2} corresponds to the maximum degree and codegree of H, respectively. The main examples of [25] concern k-uniform hypergraphs H = Hn with v(H) = n vertices and e(H) = Θ(n2) edges that are almost linear, i.e., with ∆2(H) = O(1), and satisfy property X(H,D,(1 + ε)µ) with D = Θ(1), where

√x,1} and e(H[W]) ≥ x. (5)

![image 14](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile14.png>)

X(H,D,x): there exists W ⊆ V (H) with |W| ≤ D max{

Note that H = Hn encoding k-term arithmetic progressions in [n] is of this form (see also Remark 5 below). Under the aforementioned conditions, Janson and Ruci´nski [25] proved that the upper tail of X = e(Hp) is of type (1), leaving a log(1/p) gap between the upper and lower bounds for constant ε (see Theorem 2.1 in [25] with q = 2). The following theorem rectiﬁes this issue, by closing the gap.

- Theorem 4. Given k ≥ 3, a > 0 and D ≥ 1, suppose that H = Hn is a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Let X = e(Hp) and µ = EX. There are n0,b,B > 0 (depending only on k,a,D) such that for all n ≥ n0, p ∈ (0,1] and ε > 0 we have, with c(ε) = b min{ε3,ε1/2},


P(X ≥ (1 + ε)µ) ≤ exp −c(ε)min µ, √µlog(e/p) . (6)

![image 15](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile15.png>)

If, in addition, X(H,D,(1 + ε)µ) and (1 + ε)µ ≥ 1 hold, then we have, with C(ε) = B max{1,ε2},

P(X ≥ (1 + ε)µ) ≥ exp −C(ε)min µ, √µlog(1/p) . (7)

![image 16](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile16.png>)

Remark 5. In many applications X(H,D,x) holds automatically for all x ≤ e(H). Indeed, often we consider sequences (Hn)n∈N of hypergraphs satisfying e(Hn ∩Hm) ≥ βe(Hm) for all n ≥ m ≥ n0, where β ∈ (0,1] and

- n0 ≥ 1 are constants (β = 1 for monotone sequences, where Hn ⊆ Hn+1). Then X(Hn,D′,x) follows (by


√x,1}).

increasing D) from v(Hm) ≤ Dm and e(Hm) ≥ am2 for m = min{r,n} and suitable r = Θ(max{

![image 17](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile17.png>)

Note that an2 ≤ e(H) ≤ (v(H))2∆2(H) ≤ D3n2, so µ = Θ(n2pk). For (7), the necessary condition (1+ε)µ ≤ e(H) usually entails X(H,D,(1+ε)µ) by Remark 5, and, as discussed, (1+ε)µ ≥ 1 is very natural (in fact, usually vacuous). The assumption k ≥ 3 is also necessary. Indeed, for a concrete counterexample

with k = 2, let H = Hn contain all pairs {x,y} ⊆ [n]. Since |[n]p| has a binomial distribution, using

2 ≈ |[n]p|2/2 it is not diﬃcult to see that log P(X ≥ (1 + ε)EX) = −Θ(√EX) for constant ε (so there is no extra logarithmic factor).

- X = e(Hp) = |[n]


p|

![image 18](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile18.png>)

Turning to applications, using Remark 5 it is easy to see that Theorem 4 applies to the number of arithmetic progressions of length k in [n]p, and so implies Theorem 1. The assumptions of Theorem 4 are also satisﬁed by Schur triples, which are classical objects in Number theory and Ramsey theory (see, e.g., [17, 37] and [16, 38]): in this case H = Hn contains all 3-element subsets {x,y,z} ⊆ [n] satisfying x+ y = z. A similar remark applies to the more general notion of ℓ-sums (studied, e.g., in [2, 35]), where the 3-element subsets {x,y,z} ⊆ [n] satisfy x + y = ℓz. Finally, the arguments in Section 2.1 of [25] reveal that Theorem 4 also applies to the number of integer solutions of certain homogeneous linear systems of equations with rank k − 2.

While results similar to Theorem 4 (with constants c,C depending on ε) are usually already considered satisfactory, in this paper we obtain much more precise estimates. Indeed, with Theorem 6 below we recover, in a very wide range, the dependence of the upper tail on t = εµ (up to constants). Theorem 6 looks hard to digest, so we will now spend some time motivating and explaining it. As a warm-up, let us ﬁrst informally discuss the asymptotic form of its upper tail estimates for X = e(Hp). In particular, since our focus is on exponentially decaying probabilities, in (9) and (10) below the multiplicative factors of 1 + n−1 and d are usually negligible (i.e., can be removed by adjusting the constants c,C). Hence, assuming n−2/k(log n)2/k ≤ p ≤ 1/2 and t ≥

√

![image 19](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile19.png>)

VarX, say, via Remarks 7–8 the form of (9)–(10) eventually simpliﬁes to

√

t2 VarX

![image 20](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile20.png>)

log P(X ≥ µ + t) = −Θ min

,

tlog(1/p) . (8)

![image 21](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile21.png>)

With this in mind, Theorem 6 essentially states that the upper tail of X = e(Hp) is either of sub-Gaussian type exp −ct2/ VarX or of ‘clustered’ type exp −c√tlog(1/p) , and that the transition between the two happens roughly for t around (VarX)2/3. In this context the upper bound (9) of Theorem 6 is very satisfactory. Namely, it holds via (a) for all t > 0 unless p is close to p0 = n−1/(k−1), in which case (9) still holds for t ≥ (VarX)2/3(log n)4/3 via (b). In words, our upper bound (9) recovers the qualitative behaviour of the upper tail for all t > 0, unless p is in a tiny exceptional interval around p0 (where we basically only miss the sub-Gaussian regime).

![image 22](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile22.png>)

Theorem 6. Given k ≥ 3, a > 0 and D ≥ 1, suppose that H = Hn is a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Let X = e(Hp), µ = EX, Λ = µ(1 + npk−1) and ϕ(x) = (1 + x)log(1 + x) − x. Given γ ∈ (0,1), there are n0 > 0 (depending only on k,a,D) as well as c,C,d > 0 and λ ≥ 1 (depending only on γ,k,a,D) such that for all n ≥ n0, p ∈ (0,1] and t > 0 the following holds. If one of

- (a) p  ∈ n−1/(k−1)−γ,γn−1/(k−1)(log n)1/(k−1) , or
- (b) t ≥ γ min{(VarX)2/3,µ2/3}(log n)4/3, or
- (c) t ≥ µp(k−2)/3−γ.


holds, then we have the upper bound P(X ≥ µ + t) ≤ (1 + n−1)exp −c min ϕ(t/µ)µ2/Λ,

√

![image 23](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile23.png>)

tlog(e/p) . (9) Furthermore, if one of

- (i) p ≤ n−2/(k+1/3), or
- (ii) t ≥ min{(VarX)2/3,µ2/3}(log n)2/3 and p ≤ n−1/(k−1) log n, or
- (iii) t ≥ min{


√

√

![image 24](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile24.png>)

![image 25](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile25.png>)

Λ} and γn−1/(k−1) ≤ p ≤ 1 − γ. holds, then X(H,D,min{λt,µ + t}) and µ + t ≥ 1 imply the lower bound

Var X,

√

P(X ≥ µ + t) ≥ dexp −C min ϕ(t/µ)µ2/Λ,

![image 26](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile26.png>)

tlog(1/p) . (10)

- Remark 7. It is routine to check that VarX = Θ (1 − p)Λ , where the implicit constants depend only on k,a,D (analogously to, e.g., Example 3.2 and Lemma 3.5 in [21]). In particular, Λ = Θ(VarX) holds whenever p is bounded away from one.


- Remark 8. If p ≥ γn−2/k(log n)2/k or t ≤ µ, then (9)–(10) hold with ϕ(t/µ)µ2/Λ replaced by t2/Λ.


In the above assumptions (a)–(c) and (i)–(iii), the use of µ and Λ is convenient for applications (see, e.g., (11) below), while Var X seems more insightful from a conceptual point of view. In particular, since we are interested in exponentially small probabilities, by central limit theorem considerations a natural target assumption is t ≥

√VarX, say. We now discuss the lower bound (10) of Theorem 6, which tends to have fewer applications. Indeed, for our purposes (10) is mainly important from a concentration-of-measure perspective, since it rigorously proves that our upper bound (9) is sharp in a wide range. In view of (i)+(iii), our lower bound (10) only falls short of the target assumption t ≥

![image 27](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile27.png>)

√VarX for p ∈ n−2/(k+1/3),n−1/(k−1) , where t ≥ (VarX)2/3(log n)2/3 suﬃces by (ii). Perhaps surprisingly, these gaps are solely due to lacking lower bounds of sub-Gaussian type (note that the variance undergoes a transition around p0 = n−1/(k−1) by Remark 7), which until now have been widely ignored in the upper tail literature (see, e.g., [43, 47]). Here our current approaches seem not strong enough to work for all relevant p and t. We leave it as an open problem to develop a generic method for obtaining suitable sub-Gaussian type lower bounds (see Section 4.2). Finally, we also conjecture that the upper tail estimates (9)–(10) remain valid for all p ∈ (0,1 − γ] and t ≥

![image 28](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile28.png>)

√

![image 29](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile29.png>)

Var X.

Turning to the remaining applications stated in the introduction, Theorem 3 for arithmetic progressions follows easily by combining (a)+(iii) of Theorem 6 with Remarks 5, 7 and 8. For Theorem 2 we use that, modulo obvious assumptions, the tail estimates (9)–(10) both apply if t > 0 satisﬁes, say,

 

0, if 0 < p ≤ n−2/(k+1/3), µ2/3(log n)4/3, if n−2/(k+1/3) < p < n−1/(k−1)(log n)1/(k−1), √Λ, if n−1/(k−1)(log n)1/(k−1) ≤ p ≤ 1 − γ.

t ≥

(11)

![image 30](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile30.png>)



(Using (a)+(i) for p ≤ n−2/(k+1/3), (b)+(ii) for larger p < n−1/(k−1)(log n)1/(k−1), and (a)+(iii) otherwise.) As µ ≥ an2pk and Λ = µ(1 + npk−1), a short calculation reveals that, say, t ≥ µn−1/(5k+1) implies (11) for all n ≥ n0(k,a) and p ∈ (0,1]. Hence, using Remarks 5 and 7, inequality (3) of Theorem 2 follows.

The proofs of the upper and lower bounds of Theorem 4 and 6 are based on completely diﬀerent techniques. For the upper bounds (6) and (9), the most important ingredients are two new concentration inequalities of Chernoﬀ-type, which we prove in Section 2. These allow us to combine and extend the combinatorial and probabilistic ideas used in the ‘deletion method’ and the ‘approximating by a disjoint subfamily’ technique of Janson and Ruci´nski [24] and Spencer [41, 23], respectively. The idea of applying the BK-inequality of van den Berg and Kesten [4] and Reimer [32] in the context of the ‘infamous’ upper tail problem [23] may perhaps also be of independent interest. For the lower bounds (7) and (10), we analyze three diﬀerent mechanisms that yield deviations of X = e(Hp), and with some care (using, e.g., Harris’ inequality [18] and the Paley–Zygmund inequality) we recover the correct dependence of the exponent on t = εµ.

The remainder of this paper is organized as follows. In Section 2 we introduce our new concentration inequalities, and in Section 3 we apply them (together with combinatorial arguments) to prove the upper bounds of Theorem 4 and 6. Finally, in Section 4 we establish the corresponding lower bounds (and also prove Remark 8).

# 2 Concentration inequalities

In this section we introduce our main probabilistic tools: two concentration inequalities which essentially state that Chernoﬀ-type upper tail estimates hold whenever X is bounded from above by a sum of random variables with ‘well-behaved dependencies’. They develop ideas of Janson and Ruci´nski [24], Erdo˝s and Tetali [14], and Spencer [41], and seem of independent interest. On ﬁrst reading of Theorem 9 it might be useful to consider the special case where there are independent random variables (ξi)i∈A such that each

- Yα ∈ {0,1} with α ∈ I is a function of (ξi)i∈α. Then, deﬁning α ∼ β if α ∩ β = ∅, it is immediate that the independence assumption holds (as α  ∼ β implies that Yα and Yβ depend on disjoint sets of variables ξi). Now, consider X = α∈I Yα with µ = EX, J = I and C = maxβ∈I |{α ∈ I : α ∼ β}|. Then X = ZC, where maxβ∈J α∈J:α∼β Yα ≤ C intuitively corresponds to a Lipschitz-like condition. With this in mind, part of the power of (12) is that the exponent scales with 1/C (instead of the usual 1/C2), and that the Lipschitz condition need not hold deterministically (it suﬃces if X ≤ ZC or X ≈ ZC holds oﬀ some exceptional event).


Theorem 9. Given a family of non-negative random variables (Yα)α∈I with α∈I EYα ≤ µ, assume that ∼ is a symmetric relation on I such that each Yα with α ∈ I is independent of {Yβ : β ∈ I and β  ∼ α}. Let ZC = max α∈J Yα, where the maximum is taken over all J ⊆ I with maxβ∈J α∈J:α∼β Yα ≤ C. Set ϕ(x) = (1 + x)log(1 + x) − x. Then for all C,t > 0 we have

(µ+t)/C

ϕ(t/µ)µ C

eµ µ + t

= e−µ/C ·

P(ZC ≥ µ + t) ≤ exp −

![image 31](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile31.png>)

![image 32](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile32.png>)

(12)

−t/(2C)

t2 2C(µ + t/3)

t 2µ

≤ min exp −

, 1 +

.

![image 33](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile33.png>)

![image 34](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile34.png>)

Remark 10. Theorem 9 remains valid after weakening the independence assumption to a form of negative correlation: it suﬃces if E( i∈[s] Yα

for all (α1,...,αs) ∈ Is satisfying αi  ∼ αj for i = j.

) ≤ i∈[s] EYα

i

i

Theorem 9 extends several upper tail inequalities discussed in the survey of Janson and Ruci´nski [23]. Indeed, consider X = α∈I Yα with µ = EX and J = I. For independent Yα ∈ [0,1] we have X = Z1 (note that α ∼ α for non-constant Yα), so that (12) reduces to the classical Chernoﬀ bound, see, e.g., Theorem 2.1 in [21]. Similarly, for generic Yα ∈ [0,1] with dependency graph G = G(I), where distinct α,β ∈ I = V (G) form an edge if α ∼ β (cf. Section 2.6 in [23]), we have X = Z∆

1(G)+1. Hence (12) improves Theorem 5 in [23], which is based on the ‘breaking into disjoint matchings’ technique of Ro¨dl and Ruci´nski [34]. Furthermore, using C = t/(2r) it is easy to see that Theorem 9 tightens Theorem 2.1 in [24], i.e., the basic theorem of the ‘deletion method’ of Janson and Ruci´nski. In addition, (12) extends Lemma 2 in [23], i.e., the main probabilistic ingredient of Spencer’s ‘approximating by a disjoint subfamily’ technique [41]. Theorem 9 is also related to a concentration inequality of Chatterjee [7]; our assumptions are less technical and subjectively easier to check (e.g., readily implying Proposition 4.1 in [7] via C = 3εℓnp). Remark 10 is useful in the context of the uniform random graph Gn,m (and related uniform models). To illustrate this we consider

n,m)} and set α ∼ β if α ∩ β = ∅. In that case it is well-known (and not hard to check) that the negative correlation condition of Remark 10 holds, demonstrating that Theorem 9 applies to Gn,m.

- Yα = {α⊆E(G


Proof of Theorem 9. The proof is based on a variant of the m-th factorial moment which ‘forces independence’. In fact, we closely follow Lemma 2.3 in [24] and Lemma 2.46 in [21], but diﬀer in some important details. Assume that m ∈ N satisﬁes 1 ≤ m ≤ ⌈(µ + t)/C⌉. For all K ⊆ I and s ∈ N with s ≥ 1 we deﬁne

Ms(K) = ∗

,

Yα

i

(α1,...,αs)∈Ks i∈[s]

where ∗(α

1,...,αs)∈Ks denotes the sum over all tuples (α1,...,αs) ∈ Ks satisfying αi  ∼ αj for i = j. The key point is that, by construction, the factors Yα

i ≥ 0 in each term of Ms(K) are independent. Hence

m

EMm(I) = ∗

= ∗

≤ µm. (13)

i ≤

EYα

Yα

EYα

## E

i

α∈I

(α1,...,αm)∈Im

(α1,...,αm)∈Im i∈[m]

i∈[m]

Now assume that ZC ≥ µ+t and ZC = α∈J Yα hold. Note that, by construction, M1(J ) = α∈J Yα = ZC ≥ µ + t. Furthermore, by choice of J (see the deﬁnition of ZC), for all (α1,...,αs) ∈ J s we have

Yα ≤

Yα ≤ Cs.

α∈J :α∼αi for some i ∈ [s]

i∈[s] α∈J :α∼αi

So, for all s ∈ N with 1 ≤ s < m ≤ ⌈(µ + t)/C⌉ it follows that

Ms+1(J ) = ∗

i ·

Yα ≥ Ms(J ) · (µ + t − Cs), (14)

Yα −

Yα

α∈J

α∈J :α∼αi for some i ∈ [s]

(α1,...,αs)∈J s i∈[s]

which by induction yields Mm(J ) ≥ mj=0−1(µ + t − Cj).

Combining the above estimates for Mm(I) ≥ Mm(J ) and EMm(I) with Markov’s inequality, we obtain

m−1

m−1

µ µ + t − Cj

(µ + t − Cj) ≤

P(ZC ≥ µ + t) ≤ P Mm(I) ≥

. (15)

![image 35](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile35.png>)

j=0

j=0

Set m = ⌈t/C⌉ ≥ 1. If µ = 0, then P(ZC ≥ µ + t) = 0 by (15), and (12) is trivial, so we henceforth assume µ > 0. For 0 ≤ x ≤ t/C, the function f(x) = log(µ/(µ + t − Cx)) is increasing and satisﬁes f(x) ≤ 0. As

f(t/C) = 0, it follows that f(j) ≤ j min{j+1,t/C} f(x)dx for 0 ≤ j ≤ t/C. We deduce

⌈t/C⌉−1

log P(ZC ≥ µ + t) ≤

log

j=0

µ µ + t − Cj ≤

![image 36](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile36.png>)

t/C

log

0

µ µ + t − Cx

![image 37](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile37.png>)

dx =: Ψ.

Using log(a/b) = log a − log b, integration yields Ψ = −ϕ(t/µ)µ/C. It is well-known that

ϕ(x) ≥ x2/(2 + 2x/3) (16) for x ≥ 0 (see, e.g., the proof of Theorem 2.1 in [21]), so Ψ ≤ −t2/ 2C(µ + t/3) . Finally, for u = t/(2C) we have Ψ = 0 t/C f(x)dx ≤ 0 u f(x)dx ≤ uf(u), which establishes (12).

![image 38](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile38.png>)

![image 39](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile39.png>)

![image 40](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile40.png>)

![image 41](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile41.png>)

For all integers x ≥ 1, by formally deﬁning xC = µ+t and m = x in the above proof (so that µ+t−Cj = C(x − j) holds), note that inequality (15) and Stirling’s formula imply

√

x

x

eµ xC

µ C

![image 42](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile42.png>)

/x! ≤

P(ZC ≥ xC) ≤

/

2πx. (17)

![image 43](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile43.png>)

![image 44](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile44.png>)

While this estimate is often weaker than (12), for C = 1 it extends, in the upper tail context, the so-called ‘disjointness lemma’ of Erdo˝s and Tetali [14], see, e.g., Lemma 8.4.1 in [1]. In the proof of Theorem 9, inequality (13) is the only step in which anything is assumed about the Yα, and independence is used in a limited way: E( Yα

) suﬃces (in fact, replacing the assumption EYα ≤ µ with λα ≤ µ and λα ≥ 0, it suﬃces if E( Yα

) ≤ E(Yα

i

i

) ≤ λα

holds). This suggests that the argument is rather robust, since, e.g., ad-hoc upper bounds for E( Yα

i

i

) are enough to obtain tail inequalities, see the proof of Lemma 4.5

i

in [44]. Finally, in (14) there is also potential for relaxing maxβ∈J α∈J:α∼β Yα ≤ C to an accumulative condition (e.g., replacing Cs by t/2).

The following variant of Theorem 9 exploits the BK-inequality [4] to further relax the independence assumption. Clearly, two events E1, E2 depending on disjoint sets of independent random variables are independent. For our purposes it intuitively suﬃces if, for each possible outcome ω ∈ Ω, we can ‘certify’ the occurrence of E1 and E2 by disjoint sets of variables (which may depend on ω). For ω = (ω1,...,ωM) ∈ Ω = Ω1 × ··· × ΩM and K ⊆ [M] = {1,...,M} we write ω|K = (ωi)i∈K and [ω]K = {ω′ ∈ Ω : ω′|K = ω|K}. If [ω]K ⊆ E, then ω|K is called a certiﬁcate for the occurrence of the event E (in words, E occurs on all sample points that agree with ω restricted to K). Intuitively speaking, in Theorem 11 the random variable Z counts the maximum number of events that ‘occur disjointly’, i.e., have disjoint certiﬁcates. With this in mind, a key feature of inequalities (12) and (17) is that they are dimension-free: they do not involve the sizes of the certiﬁcates (in contrast to ‘certiﬁcate-based’ variants of Talagrand’s inequality such as Theorem 2 in [31]).

Theorem 11. Given a product space Ω = Ω1 × ··· × ΩM, with ﬁnite Ωi, let (Eα)α∈I be a family of events with α∈I P(Eα) ≤ µ. Let Z = max |J |, where the maximum is taken over all J ⊆ I for which there are disjoint Ki ⊆ [M] satisfying [ω]K

for all αi ∈ J . Then (12) and (17) hold with C = 1 and Z1 = Z.

i ⊆ Eαi

Remark 12. Theorem 11 remains valid after weakening the product space assumption: restricting to increasing events Eα ⊆ Ω = {0,1}M, it suﬃces if P satisﬁes the BK-inequality (18) for increasing events (in this case is associative, so we may replace Z by the maximum of |J | over all J ⊆ I for which α∈J Eα holds).

The proof of Theorem 11 is based on the BK-inequality, which is a partial converse to Harris’ inequality [18]. Intuitively, A B means that the events A and B have disjoint certiﬁcates. Formally, we deﬁne

A B = {ω ∈ Ω : there are disjoint K,L ⊆ [M] such that [ω]K ⊆ A and [ω]L ⊆ B},

which need not be associative. The general BK-inequality of Reimer [32] states that for any product space Ω = Ω1 × ··· × ΩM, with ﬁnite Ωi, the following holds: for any two events A,B ⊆ Ω we have

P(A B) ≤ P(A)P(B). (18)

Proof of Theorem 11. The proof uses a -based variant of the m-th moment (inspired by Theorem 9). For all m ∈ N we deﬁne D(α1,...,αm) = ((···(Eα1 Eα2

) Eαm

) ···) Eαm−1

and

Mm(K) =

(α1,...,αm)∈Km

{D(α1,...,αm)}.

Using the BK-inequality (18) inductively, we obtain P(D(α1,...,αm)) ≤ i∈[m] P(Eαi

). So, analogous to (13), we deduce EMm(I) ≤ µm. Now assume that Z ≥ y and Z = |J | hold. For each m ≤ ⌈y⌉ ≤ |J |, by deﬁnition of Z we see that D(α1,...,αm) occurs for all m-element subsets {α1,...,αm} ⊆ J . Hence

m−1

|J | m

(y − j).

Mm(I) ≥ Mm(J ) ≥

m! ≥

j=0

Let Z1 = Z and C = 1. With y = µ + t, the proof of Theorem 9 carries over unchanged from (15) onwards, and (12) follows. Similarly, with y = x, m = x and µ + t = x, (15) establishes (17).

![image 45](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile45.png>)

![image 46](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile46.png>)

![image 47](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile47.png>)

![image 48](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile48.png>)

The suﬃcient condition of Remark 12 has recently been established in [3] for P assigning equal probability to all ω ∈ {0,1}M with exactly k ones. Hence Theorem 11 applies to Gn,m and related uniform models.

# 3 Upper bounds

In this section we establish the upper bounds (6) and (9) of Theorem 4 and 6. The executive summary of our proof strategy is as follows: using combinatorial arguments we shall approximate X = e(Hp) using several ‘well-behaved’ auxiliary random variables, which we in turn estimate by the concentration inequalities of Section 2. Of course, the actual details are much more involved, and our arguments in fact develop combinatorial and probabilistic ideas of the ‘deletion method’ [24] and the ‘approximating by a disjoint subfamily’ technique [41, 23]. We have added a substantial amount of informal discussion and motivation to the remainder of this section, in an attempt to make the underlying ideas and techniques more accessible (the actual proofs could be recorded in a much shorter way). For example, in order to milden some of the technical diﬃculties, we shall not only informally discuss the intriguing log(e/p) factors in the exponent, but also prove (6) using a simpliﬁed version our arguments (instead of proving (6) and (9) in a uniﬁed way).

The remainder of this section is organized as follows. In Section 3.1 we motivate parts of our proof strategy, and illustrate how logarithmic terms arise in our tail estimates. In Section 3.2 we then present our basic proof framework, and establish the upper bound of Theorem 4. Finally, in Section 3.3 we reﬁne the aforementioned framework, and prove the more involved upper bound of Theorem 6.

- 3.1 Warming up


The upper bounds of Theorem 4 and 6 involve exponentially small probabilities, so error probabilities of form o(1) are too crude for our purposes (and the proofs require more care). In fact, the exponents in (6) and (9) are fairly involved, and both contain somewhat unusual log(e/p) terms. With these non-standard features in mind, the goals of this informal section are two-fold: (i) to motivate some details of our upcoming proof strategy, and (ii) to illustrate the way in which we eventually obtain the log(e/p) factors.

- 3.1.1 Motivation and preliminaries Let us start with a basic estimate for the number of induced edges X = e(Hp). For brevity we set


Γv(G) = {f ∈ G : v ∈ f},

so that |Γv(Hp)| equals the degree of vertex v in Hp. Clearly, for all r > 0 we have P(X ≥ µ + t) ≤ P(X ≥ µ + t and ∆1(Hp) ≤ r) + P(∆1(Hp) > r) ≤ P(X ≥ µ + t and ∆1(Hp) ≤ r) +

P(|Γv(Hp)| > r). (19)

v∈V (H)

A similar decomposition forms the basis of the inductive ‘deletion method’ of Janson and Ruci´nski [24], see, e.g., Theorem 2.5 and Section 3 in [24]. The inductive approach of Kim and Vu [27] is also based on a related idea, see, e.g., Section 3.2 in [43].

One bottleneck of the above approach (19) is that it relies on a uniform upper bound on the degree of all vertices. We shall rectify this issue via the following sparsiﬁcation strategy (which allows for some vertices with larger degrees): we ﬁrst decrease the maximum degree of Hp by removing some carefully chosen edges, and then estimate the number of remaining edges via the Chernoﬀ-type tail inequality Theorem 9. In other words, our plan is to ﬁrst apply further combinatorial arguments to Hp, before using any probabilistic tail estimates or induction. An embryonic version of this idea is contained in the ‘approximating by a disjoint subfamily’ technique of Spencer [41, 23], but Janson and Ruci´nski argued in their upper tail survey [23] that this technique is ‘never better’ than the ‘deletion method’ [24] (see Remark 2 in Section 2.3.4 and Example 7 in Section 3.2 of [23]). In Sections 3.2–3.3 we shall, in some sense, crossbred ideas of both approaches to go one step further.

- 3.1.2 Extra logarithmic factors in tail estimates?


Let us illustrate how extra logarithmic factors can arise in our upper tail estimates. To this end we shall now have, in the context of Theorem 4, a heuristic look at the exponential decay of the degrees |Γv(H)|. Here the key observation is that the dependencies among the edges in Γv(Hp) ⊆ Γv(H) are severely limited by the codegree condition ∆2(H) = O(1): for every e ∈ Γv(H) there are only at most k∆2(H) = O(1) edges f ∈ Γv(H) which intersect e \ {v}, i.e., with (f ∩ e) \ {v} = ∅ (because all such f contain v and at least one vertex from e \ {v}). As H is k-uniform, it thus seems plausible that, conditioned on v ∈ Vp(H), the upper tail of |Γv(Hp)| decays roughly like a binomial random variable Y ∼ Bin(|Γv(H)|,pk−1). Note that for all positive integers x, we have

P Y ≥ x ≤

|Γv(H)| x

|Γv(H)|pk−1 x x! ≤

p(k−1)x ≤

![image 49](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile49.png>)

O(npk−1) x

![image 50](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile50.png>)

x

, (20)

where we used |Γv(H)| ≤ |V (H)| · ∆2(H) = O(n) for the last inequality. As expected, the decay of |Γv(Hp)| turns out to be very similar to (20). Indeed, ignoring a number of technicalities, we later approximately show (see (37) in the proof of Lemma 17) that for a certain range of x we have

P(|Γv(Hp)| ≥ x) ≤

P(∆1(Hp) ≥ x) ≤

v∈V (H)

O(npk−1) x

![image 51](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile51.png>)

Θ(x)

. (21)

With this in mind, the basic idea for ‘extra’ logarithmic terms is simple: if x ≫ ynpk−1 holds, then (21) suggests P(∆1(Hp) ≥ x) ≤ exp −Θ(xlog y) . In words, if the deviation x ‘overshoots’ the expectation |Γv(H)|pk−1 = O(npk−1) signiﬁcantly, then we should win a logarithmic factor in the exponent.

In Sections 3.2–3.3 we shall exploit the aforementioned ‘overshooting’ phenomenon for a range of diﬀerent degrees (to intuitively show that there are not too many vertices with high degrees). Of course, using this approach we shall eventually need to check a number of technical conditions such as npk−1/x = O pΘ(1) : these are key for obtaining the log(e/p) factors missing in previous work of Janson and Ruci´nski [25].

- 3.2 Basic proof framework


In this section we introduce our basic proof framework (for arbitrary hypergraphs H), which seems of independent interest. In the combinatorial part we implement the sparsiﬁcation idea mentioned in Section 3.1.1, and essentially show the number of induced edges X = e(Hp) can be estimated via two carefully deﬁned auxiliary random variables Xr = Xr(Hp) and Mr = Mr(Hp). In the probabilistic part we systematically obtain

upper tail estimates for Xr and Mr, by exploiting the Chernoﬀ-type concentration inequalities of Section 2. Finally, we demonstrate the applicability of this framework by proving the upper bound of Theorem 4.

Recall that our strategy is to decrease the maximum degree of Hp by removing edges. To estimate the upper tail of the remaining edges, we now introduce the following ‘smooth approximation’ of X = e(Hp):

Xr = max e(G) : G ⊆ Hp and ∆1(G) ≤ r . (22)

In words, Xr = Xr(Hp) denotes the maximum number of edges in any subhypergraph G ⊆ Hp with maximum degree at most r. Via Theorem 9 this ‘bounded degree’ property eventually yields (23), i.e, a general upper tail estimate for Xr. For ε = Θ(1) and k = Θ(1), note that (23) yields P(Xr ≥ (1 + ε/2)µ) ≤ exp(−Θ(µ/r)).

- Lemma 13. Suppose that H satisﬁes maxf∈H |f| ≤ k. Set X = e(Hp), µ = EX and ϕ(x) = (1 + x)log(1 + x) − x. Then, for all p ∈ [0,1] and r,t > 0 we have

P(Xr ≥ µ + t/2) ≤ exp −

ϕ(t/µ)µ 4kr ≤ exp −

![image 52](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile52.png>)

min{t,t2/µ} 12kr

![image 53](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile53.png>)

. (23)

The main observation required to deduce Lemma 13 from Theorem 9 is that every edge f ∈ G ⊆ H is incident to at most k∆1(G) other edges of G. This allows us to bring the Lipschitz-like condition of Theorem 9 into play (with C = kr).

Proof of Lemma 13. Deﬁning Yf = {f⊆V

p(H)}, we have f∈H EYf = EX = µ. Set e ∼ f if e ∩ f = ∅. Hence, by the discussion preceding Theorem 9, the independence assumption of Theorem 9 holds (here the ξi = {i∈V

p(H)} are independent indicators, so Yf = i∈f ξi). Observe that for all f ∈ G ⊆ H we have

e∈G:e∼f

Ye ≤

v∈f e∈G:v∈e

Ye ≤ |f| · max

v∈f

|Γv(G)| ≤ k∆1(G).

Hence, for C = kr we deduce Xr ≤ ZC, where ZC is deﬁned as in Theorem 9 with I = H. So, using (12),

P(Xr ≥ µ + t/2) ≤ P(ZC ≥ µ + t/2) ≤ exp −

ϕ t/(2µ) µ kr

![image 54](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile54.png>)

,

and it remains to rewrite this estimate. Since (16) implies (by distinguishing the cases x ≥ 1 and x ≤ 1) that

ϕ(x) ≥ min{x,x2}/3, (24) we see that (23) follows if ϕ(t/(2µ)) ≥ ϕ(t/µ)/4. To sum up, it suﬃces to prove that

ϕ(x/2) ≥ ϕ(x)/4 (25)

for x ≥ 0. To this end we consider f(x) = ϕ(x/2) − ϕ(x)/4. Now, for x ≥ 0 we have 4f′(x) = log (1 + x/2)2/(1 + x) ≥ 0, so that f(x) ≥ f(0) = 0, completing the proof.

![image 55](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile55.png>)

![image 56](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile56.png>)

![image 57](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile57.png>)

![image 58](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile58.png>)

Our sparsiﬁcation strategy intuitively focuses on high-degree vertices (with degree at least r). To quantify the number of removed edges, we shall introduce the auxiliary variable Mr = Mr(Hp), which essentially counts high-degree vertices with ‘disjoint certiﬁcates’ (in the sense of Section 2). More precisely, we call S = (v,W)

an r-star in G if W = {f1,...,f⌈r⌉} ⊆ Γv(G) and |W| = ⌈r⌉. We write V (S) = 1≤i≤⌈r⌉ fi, which contains all vertices of the r-star S. Note that V (S) ⊆ Vp(H) implies |Γv(Hp)| ≥ ⌈r⌉, i.e., that vertex v has degree at least ⌈r⌉. Writing Tr(G) for the collection of all r-stars S = (v,W) in G, we deﬁne

Mr(G) = max |M| : M ⊆ Tr(G) and V (S1) ∩ V (S2) = ∅ for all distinct S1,S2 ∈ M . (26)

In words, Mr(Hp) denotes the size of the largest vertex disjoint collection of r-stars in Hp, i.e., r-star matching. (As indicated earlier, it might be useful to think of Mr(Hp) as the maximum number of degree ≥ r vertices that ‘occur disjointly’.) For future reference we note the following basic relation between ∆1(Hp) and Mr(Hp).

- Lemma 14. Given H, for all p ∈ [0,1] and z > 0 we have P(∆1(Hp) ≥ z) = P(Mz(Hp) ≥ 1).


![image 59](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile59.png>)

![image 60](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile60.png>)

![image 61](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile61.png>)

![image 62](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile62.png>)

The following combinatorial lemma is at the heart of our basic sparsiﬁcation strategy: it intuitively relates X = e(Hp) with the auxiliary random variables Xr and Mr(Hp). In fact, inequality (27) below is inspired by the main deterministic ingredient of the ‘approximating by a disjoint subfamily’ technique (see, e.g., Lemma 3 in [23], which is used to count vertices in an auxiliary graph with V (G) = Hp). While Spencer’s technique hinges on the fact that disjoint edges are nearly independent (see also [41, 14]), here one important conceptual diﬀerence is that we allow for dependencies, i.e., overlaps of the edges (via r ≥ 2 in Xr). For our applications the crux of (27) is that Xr < (1 + ε/2)µ and k⌈r⌉Mr(Hp)∆1(Hp) < εµ/2 together imply X < (1 + ε)µ.

- Lemma 15. Suppose that H satisﬁes maxf∈H |f| ≤ k. Then, for all p ∈ [0,1] and r > 0 we have

Xr ≤ X ≤ Xr + {∆

1(Hp)>r}k⌈r⌉Mr(Hp)∆1(Hp). (27)

The proof idea is simple: if M ⊆ Tr(Hp) attains the maximum in the deﬁnition of Mr(Hp), then after removing all edges incident to some star S = (v,W) ∈ M we obtain a hypergraph G with maximum degree at most ⌈r⌉ − 1 ≤ r (otherwise we could add another r-star to the vertex disjoint collection M), so e(G) ≤ Xr. Inequality (27) combines this observation with trivial estimates for the number of removed edges.

- Proof of Lemma 15. The lower bound X = e(Hp) ≥ Xr is immediate. For the upper bound, note that X = Xr whenever ∆1(Hp) ≤ r, so we may henceforth assume ∆1(Hp) > r. We ﬁx some M ⊆ T⌈r⌉(Hp) which attains the maximum in (26), so Mr(Hp) = |M|. We remove all edges from Hp which contain at least one vertex from (the edges of) some r-star S = (v,{f1,...,f⌈r⌉}) ∈ M, and denote the remaining hypergraph by G. As every edge contains at most maxf∈H |f| ≤ k vertices, we removed at most e(Hp)−e(G) ≤ |M| · ⌈r⌉k · ∆1(Hp) edges from Hp. Clearly ∆1(G) ≤ ⌈r⌉ − 1 ≤ r, because otherwise we could add another r-star to M (contradicting maximality). Hence G contains at most e(G) ≤ Xr edges, and (27) follows.

![image 63](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile63.png>)

![image 64](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile64.png>)

![image 65](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile65.png>)

![image 66](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile66.png>)

Next, we shall exploit the disjoint-like structure of Mr(Hp) via the BK-inequality based Theorem 11. This leads to (28), a generic upper tail estimate for the size of the largest r-star matching Mr(Hp). Note that P(∆1(Hp) ≥ r) ≤ v∈V (H) P(|Γv(Hp)| ≥ ⌈r⌉) = Φr. In this paper we mainly have very unlikely degrees in mind, where Φr ≤ Q−r for some Q > 1. Then the probability that at least y of such high-degree vertices (with degree at least r) ‘occur disjointly’ is roughly at most Q−ry by (28) below.

Lemma 16. Given H, for all p ∈ [0,1] and y,r > 0 we have

P(Mr(Hp) ≥ y) ≤

Φ⌈ry⌉ ⌈y⌉! ≤

![image 67](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile67.png>)

- 1

![image 68](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile68.png>)

![image 69](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile69.png>)

- 2π⌈y⌉


eΦr ⌈y⌉

![image 70](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile70.png>)

⌈y⌉

, (28)

where Φr = v∈V (H) P(|Γv(Hp)| ≥ ⌈r⌉).

The main idea is very intuitive: if M ⊆ Tr(Hp) attains the maximum in the deﬁnition of Mr(Hp), then Hp contains |M| vertex disjoint stars Sv = (v,W) ∈ M, each of which ‘certiﬁes’ that the corresponding vertex v has degree at least ⌈r⌉ in Hp (in the sense of Section 2). Hence Mr(Hp) = |M| events of form Ev = {|Γv(Hp)| ≥ ⌈r⌉} ‘occur disjointly’, which allows us to bring (17) of Theorem 11 into play (with C = 1).

- Proof of Lemma 16. We claim that Mr(Hp) ≤ Z for Z = Z1 as deﬁned in Theorem 11 with I = V (H), where Ev denotes the event that |Γv(Hp)| ≥ ⌈r⌉. This claim implies P(Mr(Hp) ≥ y) ≤ P(Z ≥ y) ≤ P(Z ≥ ⌈y⌉), and we then deduce (28) by applying (17) with C = 1.




To establish Mr(Hp) ≤ Z, we pick any M ⊆ Tr(Hp) which attains the maximum in (26), so that Mr(Hp) = |M|. For every r-star Sv = (v,{f1,v,...,f⌈r⌉,v}) ∈ M we know that V (Sv) = 1≤i≤⌈r⌉ fi,v ⊆ Vp(H) holds, which in turn implies Ev. In other words, the presence of the vertices V (Sv) ⊆ Vp(H) constitutes a certiﬁcate for the event Ev (using the notation of Section 2, we have [ω]V(S

v) ⊆ Ev). By deﬁnition of Mr(Hp) these certiﬁcates V (Sv) S

v∈M are all disjoint, so Z ≥ |M| = Mr(Hp), as claimed.

![image 71](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile71.png>)

![image 72](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile72.png>)

![image 73](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile73.png>)

![image 74](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile74.png>)

To summarize our proof framework: Lemmas 13–16 apply to arbitrary hypergraphs H with maxf∈H |f| ≤ k, and they basically reduce the upper tail problem for X = e(Hp) to the upper tail problem for the degrees of Hp, i.e., to Φx = v P(|Γv(Hp)| ≥ ⌈x⌉); see also (29) below. (These ideas are developed further in [46].)

In general, by noting P(|Γv(Hp)| ≥ ⌈x⌉) ≤ P(|Γv(Hp)| ≥ ⌈x⌉ | v ∈ Vp(H)) there is room for induction (on the number of vertices per edge), analogous to [24, 27]. However, for the purposes of Theorem 4 and 6 it seems easier to exploit the codegree condition ∆2(H) = O(1) more directly (see the proof of Lemma 17).

- 3.2.1 Sketch of the upper bound of Theorem 4

In this section we sketch the proof of upper bound of Theorem 4, illustrating the discussed proof framework. As we shall see, the desired ‘overshooting’ phenomenon (which yields the extra log(e/p) factor in the exponent) arises naturally. First, using Lemma 15, for all r,y,z > 0 satisfying {y>1}k⌈r⌉yz ≤ εµ/2 we obtain

P(X ≥ (1 + ε)µ) ≤ P(Xr ≥ (1 + ε/2)µ) + P(Mr(Hp) ≥ y) + {y>1}P(∆1(Hp) ≥ z). (29)

(To clarify: for the indicator {y>1} we exploited that Mr(Hp) < 1 implies Mr(Hp) = 0, which in turn entails ∆1(Hp) < r.) Turning to further estimates of the right-hand side of (29), for ε = Θ(1) Lemma 13 yields

P(Xr ≥ (1 + ε/2)µ) ≤ exp −Θ µ/r . This suggests that, in order to ‘match’ the exponent of our target bound (6), we should pick r = Θ max{1, √µ/ log(e/p)} . (30)

![image 75](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile75.png>)

It later turns out, see (45), that this natural choice satisﬁes npk−1/r = o(p1/4) for k ≥ 3 (this fails for k = 2). In view of (21), we thus expect to obtain an extra log(e/p) factor in the exponent for x ≥ r:

Φx =

v∈V (H)

P(|Γv(Hp)| ≥ ⌈x⌉) ≤

p e

![image 76](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile76.png>)

1/4 Θ(x)

= exp −Θ xlog(e/p) . (31)

By Lemma 16 it thus seems plausible that for x ≥ r we have

P(Mx(Hp) ≥ y) ≤ Φx ⌈y⌉ ≤ exp −Θ xy log(e/p) . (32) Combining our heuristic ﬁndings with Lemma 14, for ε = Θ(1) and z ≥ r we thus expect that

P(X ≥ (1 + ε)µ) ≤ exp −Θ µ/r + exp −Θ ry log(e/p) + {y>1} exp −Θ z log(e/p) . (33)

To ‘match’ the exponent of our target bound (6), in view of (30) it seems natural to set y = z/r and z = εµ/(4k), say. In fact, these choices also satisfy two further technical conditions used above. Namely, that k⌈r⌉yz ≤ 2kryz = 2kz2 ≤ εµ/2 holds, and that y > 1 implies z ≥ r. Hence, if r is chosen as in (30), then for ε = Θ(1) and µ ≥ 1 we expect that

![image 77](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile77.png>)

P(X ≥ (1 + ε)µ) ≤ exp −Θ min µ,√µlog(e/p) , (34)

![image 78](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile78.png>)

which ‘matches’ the target bound (6) of Theorem 4. With hindsight, the freedom that via Mr(Hp) we can pick z ≫ r in (29) seems key for going beyond the more basic decomposition (19).

- 3.2.2 Proof of the upper bound of Theorem 4


In this section we follow our heuristic proof sketch, and establish the upper bound of Theorem 4. We start with the size of the largest r-star matching Mr(Hp), and make the upper tail estimate (32) rigorous via

- Lemma 17 below (its statement is formulated with an eye on on the upcoming proof of Theorem 6, where the n2(max{y,1})3/2 ≥ 1 term facilitates union bound arguments). The technical assumption (35) intuitively ensures that vertices with degree at least r are suﬃciently concentrated (recall that the expected degree should be O(npk−1), see the discussion in Section 3.1.2). For example, r = C(1 + npk−1) satisﬁes (35) when npk−1 ≥ log n or npk−1 ≤ n−γ for C = C(γ,B,k,D) suﬃciently large, but for npk−1 ≈ 1 a somewhat larger choice of r seems necessary (unless we impose additional constraints on y in (36) below). By the heuristics of Section 3.2.1, for r as deﬁned in (30) we expect that npk−1/x ≤ p1/4 holds in inequality (36), i.e., as in (32) we should gain an extra logarithmic factor in the exponent of the upper tail by ‘overshooting’.


- Lemma 17. Given k ≥ 2, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn and ∆2(H) ≤ D. Then there are B,n0 ≥ 1 (depending on k,D), such that for all n ≥ n0, p ∈ [0,1], r > 0 satisfying


Bnpk−1/r r ≤ n−8kD (35) the following holds. For all x ≥ r and y > 0 we have

xy/(2kD)

npk−1 ex

1 n2(max{y,1})3/2

P(Mx(Hp) ≥ y) ≤

. (36)

![image 79](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile79.png>)

![image 80](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile80.png>)

Our plan is to deduce Lemma 17 from inequality (28) of Lemma 16, and in view of the parameter Φx =

v∈V (H) P(|Γv(Hp)| ≥ ⌈x⌉) we thus study the degrees |Γv(Hp)|. Here our main observation is simple. Namely, as discussed in Section 3.1.2, every edge e ∈ Γv(H) intersects at most k∆2(H) = O(1) edges f ∈ Γv(H), which suggests that the dependencies between the edges in Γv(Hp) are extremely weak. It thus seem plausible that, conditioned on v ∈ Vp(H), the tails of |Γv(Hp)| are comparable to those of Bin(|Γv(H)|,pk−1) with |Γv(H)|pk−1 = O(npk−1), see also (20)–(21). This line of reasoning can easily be made rigorous via Theorem 9, but below we take a more direct combinatorial route (which suﬃces for our purposes).

- Proof of Lemma 17. It suﬃces to prove that for all x ≥ r and n ≥ n0(D) we have


x/(2kD)

npk−1 ex

1 en2

P(|Γv(Hp)| ≥ ⌈x⌉) ≤

. (37)

Φx =

![image 81](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile81.png>)

![image 82](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile82.png>)

v∈V (H)

Indeed, since y > 0 implies ⌈y⌉ ≥ max{y,1}, by applying (28) of Lemma 16 it then follows that

xy/(2kD)

npk−1 ex

eΦx ⌈y⌉ ⌈y⌉ · ⌈y⌉⌈y⌉

![image 83](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile83.png>)

P(Mx(Hp) ≥ y) ≤ P(Mx(Hp) ≥ ⌈y⌉) ≤

≤

.

![image 84](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile84.png>)

![image 85](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile85.png>)

n2(max{y,1})3/2

![image 86](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile86.png>)

In the remainder we verify inequality (37), by focusing on combinatorial implications of the degree event |Γv(Hp)| ≥ ⌈x⌉. To this end we pick a subset W ⊆ Γv(Hp) of the edges which is size maximal subject to the restriction that all edges of W are vertex disjoint outside of the centre vertex v, i.e., that all distinct edges fi,fj ∈ W satisfy (fi ∩ fj) \ {v} = ∅. Note that for every edge e ∈ Γv(Hp) there are a total of (including e itself) at most k∆2(H) ≤ kD = C edges f ∈ Γv(Hp) with (f ∩e)\{v} = ∅ (because all such edges f contain v and at least one vertex from e \ {v}). Hence, |Γv(Hp)| ≥ ⌈x⌉ implies

|W| ≥ |Γv(Hp)|/C ≥ x/C. Since the union of all edges in W contains exactly | f∈W f| = 1 + (k − 1)|W| vertices, it follows that P(|Γv(Hp) ≥ ⌈x⌉) ≤

|Γv(H)| ⌈x/C⌉

p1+(k−1)⌈x/C⌉.

Recalling |Γv(H)| ≤ |V (H)|∆2(H) ≤ D2n, mz ≤ (em/z)z and p ≤ 1, we obtain

⌈x/C⌉

eD2Cnpk−1 x

⌊D2n⌋ ⌈x/C⌉

p(k−1)⌈x/C⌉ ≤

. (38)

P(|Γv(Hp)| ≥ ⌈x⌉) ≤

![image 87](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile87.png>)

Deﬁning B = e3D4C2, using C = kD, x ≥ r, and the assumption (35) it follows that

x/(2kD)

x/(2kD)

Bnpk−1 r ·

npk−1 ex

npk−1 ex

≤ n−4 ·

P(|Γv(Hp)| ≥ ⌈x⌉) ≤

.

![image 88](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile88.png>)

![image 89](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile89.png>)

![image 90](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile90.png>)

Recalling |V (H)| ≤ Dn, this readily establishes inequality (37) for n ≥ n0(D), completing the proof.

![image 91](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile91.png>)

![image 92](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile92.png>)

![image 93](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile93.png>)

![image 94](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile94.png>)

For the interested reader we remark that from the above proof idea it, e.g., also directly follows that

|Γv(H)| ⌈r/C⌉

p(1+(k−1)⌈r/C⌉)|U|,

P(Mr(Hp) ≥ x) ≤

v∈U

U⊆V (H): |U|=⌈x⌉

which can alternatively be used to derive (36). We ﬁnd our general BK-inequality based approach more informative and ﬂexible (e.g., with respect to possible extensions and generalizations, see [46]).

We are now ready to prove the upper bound of Theorem 4. Below we shall ﬁrst pick r as in (30), and then closely mimic the heuristic considerations (33)–(34) of Section 3.2.1. Only afterwards we verify npk−1/r = O(p1/4), the technical condition (35), and the heuristic tail inequality (32).

Proof of (6) of Theorem 4. With foresight, we deﬁne

s = log(e/pγ), γ = 1/4, and A = max eB/√a, 16k2D/γ , (39) where B = B(k,D) ≥ 1 is as in Lemma 17. Furthermore, analogous to our heuristic outline, we set

![image 95](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile95.png>)

r = Amax 1, √µ/s , z = εµ/(4k), and y = z/r, (40) so that k⌈r⌉yz ≤ 2kz2 = εµ/2. Since y > 1 implies z ≥ r, using inequality (29) and Lemma 14 we obtain

![image 96](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile96.png>)

![image 97](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile97.png>)

P(X ≥ (1 + ε)µ) ≤ P(Xr ≥ µ + εµ/2) + P(Mr(Hp) ≥ y) + {z≥r}P(Mz(Hp) ≥ 1). (41) We defer the proof of the technical claim that for all for x ≥ r and y > 0 we have

xys 2kD

P(Mx(Hp) ≥ y) ≤ exp −

. (42) Inserting (42) into (41), using Lemma 13, ry = z and the deﬁnitions of r,z from (40) we infer

![image 98](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile98.png>)

min{ε,ε2}µ 12kr

zs 2kD

+ 2 exp −

P(X ≥ (1 + ε)µ) ≤ exp −

![image 99](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile99.png>)

![image 100](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile100.png>)

min{ε,ε2} min µ,√µs 12kA

√εµs 2kD

![image 101](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile101.png>)

![image 102](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile102.png>)

√

+ 2 exp −

= exp −

.

![image 103](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile103.png>)

![image 104](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile104.png>)

![image 105](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile105.png>)

4k

Noting s ≥ γ log(e/p) and min{ε,ε2,√ε} = min{ε2,ε1/2}, there is d = d(k,A,D,γ) > 0 such that P(X ≥ (1 + ε)µ) ≤ 3 exp −dmin{ε2,ε1/2} min{µ,√µlog(e/p)} =: 3 exp −Ψ . (43)

![image 106](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile106.png>)

![image 107](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile107.png>)

We claim that (6) holds with c(ε) = b min{ε3,ε1/2} and b = d/6. In the main case Ψ ≥ 3 this is obvious (as 3e−5Ψ/6 ≤ 1 and min{ε2,ε1/2} ≥ min{ε3,ε1/2}). In the degenerate case 1 ≥ Ψ/3, Markov’s inequality yields

εΨ 3(1 + ε)

ε 1 + ε ≤ exp −

ε 1 + ε ≤ exp −

1 1 + ε

= 1 −

P(X ≥ (1 + ε)µ) ≤

,

![image 108](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile108.png>)

![image 109](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile109.png>)

![image 110](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile110.png>)

![image 111](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile111.png>)

which due to ε/(1 + ε) · min{ε2,ε1/2} ≥ min{ε3,ε1/2}/2 establishes the claim.

In the remainder we verify the claimed estimate (42). Our below proof is based on Lemma 17, which requires us to check the technical condition (35). Calculus shows that

pγs = pγ log(e/pγ) ≤ 1. (44) Using r ≥ A√µ/2, µ = e(H)pk ≥ an2pk, and k ≥ 3 (this is the only time k ≥ 2 is not enough), we obtain

![image 112](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile112.png>)

npk−1s A√µ ≤

npk−1 r ≤

p(k−2)/2s A√a ≤

p1/2s A√a

p2γs A√a ≤

pγ eB

. (45)

=

![image 113](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile113.png>)

![image 114](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile114.png>)

![image 115](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile115.png>)

![image 116](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile116.png>)

![image 117](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile117.png>)

![image 118](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile118.png>)

![image 119](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile119.png>)

![image 120](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile120.png>)

![image 121](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile121.png>)

![image 122](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile122.png>)

which also implies r ≥ eBnpk−1−γ. Observe that p ≥ n−1/(2k) implies r ≥ n1/2, say, and that p ≤ n−1/(2k) implies pγ ≤ n−γ/(2k). Using r ≥ A, for n ≥ n0(k,D) we thus infer

Bnpk−1/r r ≤ pγ/e r ≤ min{e−r, pγA} ≤ {p>n−1/(2k)}e−n

1/2

+ {p≤n−1/(2k)}n−γA/(2k) ≤ n−8kD,

establishing (35). As (45) and B ≥ 1 imply npk−1/x ≤ e−s for all x ≥ r, inequality (36) of Lemma 17 now readily establishes the technical estimate (42), completing the proof.

![image 123](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile123.png>)

![image 124](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile124.png>)

![image 125](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile125.png>)

![image 126](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile126.png>)

Since our proofs are based on applications of Theorem 9 and 11, using Remark 10 and 12 it is not diﬃcult to see that all arguments carry over (essentially unchanged) to the uniform model Hm = H[Vm(H)] with k ≤ m ≤ v(H) and p = m/v(H), say, where Vm(H) ⊆ V (H) with |Vm(H)| = m is chosen uniformly at random (note that e(Hm) = 0 if m < k). A similar remark also applies to the weighted case, where X = e∈H

we

p

for positive constants we ∈ [˜a,D˜], say. In both cases we leave the straightforward details to the interested reader (these variations also carry over to the upcoming proofs of Section 3.3).

- 3.3 Some reﬁnements (proof of the upper bound of Theorem 6)


In this section we reﬁne our basic proof framework, and establish the more precise upper bound (9) of Theorem 6. Recall that the exponent of (9) is essentially either of sub-Gaussian type exp −ct2/ VarX or clustered type exp −c√tlog(1/p) ; see also (8). Heuristically speaking, the corresponding phase transition near (VarX)2/3 causes some technical diﬃculties for the approach taken in Section 3.2 (for p ≥ n−1/(k−1)+o(1) it turns out that sharp tail estimates are easier when t is far away from (Var X)2/3). Here one bottleneck is Lemma 15, which on an intuitive level only distinguishes between two ranges of the degrees: smaller and larger than r. In this section we shall rectify this issue, by distinguishing between a wide range of diﬀerent degrees.

![image 127](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile127.png>)

More concretely, our reﬁned sparsiﬁcation strategy is to iteratively decrease the maximum degree of Hp, until we are able to bound the number of remaining edges by Xr as deﬁned in (22). Using the convention N = {0,1,...}, we shall eventually implement this strategy via T (β,γ,r,t), which is the event that

√

√

![image 128](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile128.png>)

![image 129](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile129.png>)

(Hp) < β

ts/rj for all j ∈ N with rj <

Mr

t/s, and (46) Mr

j

√

√

![image 130](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile130.png>)

![image 131](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile131.png>)

(Hp) < β

t/rj for all j ∈ N with rj ≥

t/s, (47) where we tacitly used the following convenient parametrization:

j

s = s(γ) = log(e/pγ), rj = rj(r) = 2jr.

(48)

(The intricate form of (46)–(47) is hard to digest on ﬁrst sight; both events are based on a delicate interplay between the combinatorial and probabilistic estimates in the upcoming proofs of Lemma 18 and 19.)

The following combinatorial lemma intuitively states that X ≈ Xr whenever T (β,γ,r,t) holds.

- Lemma 18. Given k ≥ 1, suppose that H satisﬁes maxf∈H |f| ≤ k. Then, for all β ∈ 0,1/(32k)], r ≥ 1 and γ,t > 0, the event T (β,γ,r,t) implies Xr ≤ X ≤ Xr + t/2.


The idea is to iterate the proof of Lemma 15: using the resulting hypergraph sequence Hp = GJ ⊇ ··· ⊇ G0 we shall estimate X = e(Hp) in terms of the step-wise diﬀerences: X = e(G0) + 0≤j<J[e(Gj+1) − e(Gj)]. The deﬁnition of T (β,γ,r,t) then ensures that 0≤j<J[e(Gj+1) − e(Gj)] ≤ t/2 and e(G0) ≤ Xr hold.

- Proof of Lemma 18. The lower bound X = e(Hp) ≥ Xr is trivial, so we henceforth focus on the upper bound.


√t. We now construct the sequence (Gj)0≤j≤J with GJ = Hp and ∆1(Gj) ≤ ⌊rj⌋. For GJ = Hp, observe that (47) and β ≤ 1 ≤ s imply Mr

![image 132](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile132.png>)

Let J be the smallest integer J ≥ 0 with rJ ≥

√t. Hence, since ∆1(Hp) ≥ ⌈rj⌉ implies Mr

![image 133](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile133.png>)

(Hp) < β ≤ 1 for all rj ≥

j

(Hp) ≥ 1, it follows that ∆1(GJ) = ∆1(Hp) ≤ ⌈rJ⌉ − 1 ≤ ⌊rJ⌋. Given Gj+1 with 0 ≤ j < J, we ﬁx some M ⊆ T⌈rj⌉(Gj+1) which attains the maximum in (26), so that |M| = Mr

j

(Hp) by monotonicity. We remove all edges from Gj+1 which contain at least one vertex from some rj-star S ∈ M, and denote the resulting hypergraph by Gj. Hence ∆1(Gj) ≤ ⌈rj⌉−1 ≤ ⌊rj⌋, because otherwise we could add another rj-star to M (contradicting the maximality of |M|).

(GJ) = Mr

(Gj+1) ≤ Mr

j

j

j

Next we estimate X = e(Hp) in terms of the hypergraph sequence (Gj)0≤j≤J. Since each rj-star consists of ⌈rj⌉ edges, for 0 ≤ j < J it follows by construction and monotonicity (using Mr

(Hp), ⌈rj⌉ ≤ rj + 1 ≤ 2rj and ∆1(Gj+1) ≤ rj+1 = 2rj) that

(Gj+1) ≤ Mr

j

j

(Hp) · 4krj2.

(Gj+1) · ⌈rj⌉ max f∈H

|f| · ∆1(Gj+1) ≤ Mr

e(Gj+1) − e(Gj) ≤ Mr

j

j

√t we readily obtain X = e(GJ) ≤ e(G0) + 4k

![image 134](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile134.png>)

Hence, using Hp = GJ, (46)–(47) and max0≤j<J rj ≤

√

(Hp)rj2 ≤ e(G0) + 4βk

![image 135](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile135.png>)

rj +

rj .

Mr

t s

j

0≤j<J

√t/s 0≤≤j<Jrj≤:

0≤j<J: rj≤

√t

√t/s

![image 136](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile136.png>)

![image 137](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile137.png>)

![image 138](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile138.png>)

For any z > 0, in view of rj = 2jr it is easy to see that

2−j = 2z. (49)

rj/z ≤ z

rj = z

j∈N:rj≤z

j∈N:rj≤z

j∈N

Thus, noting that ∆1(G0) ≤ ⌊r0⌋ ≤ r implies e(G0) ≤ Xr, using β ≤ 1/(32k) it follows that

X ≤ e(G0) + 16βkt ≤ Xr + t/2, completing the proof.

![image 139](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile139.png>)

![image 140](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile140.png>)

![image 141](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile141.png>)

![image 142](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile142.png>)

In view of Lemma 13 and 18, we now focus on the probability of the event ¬T (β,γ,r,t). Ignoring some technical assumptions (which are similar to those of Lemma 17), the following result essentially states that P(¬T (β,γ,r,t)) is negligible for our purposes (the 1/n prefactor in (50) is ad-hoc, and eventually becomes the usually irrelevant n−1 term in (9) of Theorem 6).

- Lemma 19. Given k ≥ 3, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Set X = e(Hp), µ = EX and ϕ(x) = (1 + x)log(1 + x) − x. Then there are B,n0 ≥ 1 (depending on k,D), such that for all n ≥ n0, p ∈ (0,1], β ∈ (0,1], γ ∈ (0,1/8], and r,t > 0 satisfying (35) we have


P(¬T (β,γ,r,t)) ≤

min{a,β} 2kD

1 n

exp −

min

![image 143](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile143.png>)

![image 144](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile144.png>)

ϕ(t/µ)µ2 Λ

,

![image 145](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile145.png>)

√

![image 146](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile146.png>)

ts . (50)

The deﬁnition of T (β,γ,r,t) is, in some sense, already a signiﬁcant part of the proof. Indeed, writing C = 2kD, our argument hinges on the fact that (36) of Lemma 17 yields, in our case, a bound of the form

rjy/C

npk−1 erj

1 n2

min e−r

jy/C,

(Hp) ≥ y) ≤

.

P(Mr

![image 147](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile147.png>)

![image 148](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile148.png>)

j

(Hp) ≥ β√ts/rj) ≤ n−2e−β

√t/s it turns out that usually npk−1/(erj) ≤ pγ/e = e−s holds, so P(Mr

√ts/C. Furthermore, for rj ≥

![image 149](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile149.png>)

![image 150](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile150.png>)

![image 151](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile151.png>)

Hence P(Mr

j

(Hp) ≥ β√t/rj) ≤ n−2e−β

√ts/C by ‘overshooting’. Recalling (46)–

![image 152](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile152.png>)

![image 153](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile153.png>)

j

(47), using a careful union bound argument this reasoning eventually establishes inequality (50).

- Proof of Lemma 19. Let C = 2kD. We use B = B(k,D) ≥ 1 as given by Lemma 17, so that (36) holds for


all x = rj and y > 0. Note that (35) entails r ≥ Bnpk−1 ≥ npk−1. With (36) in hand, we now estimate P(¬T (β,γ,r,t)) by a delicate union bound argument. With foresight, we ﬁrst assume r ≥ aΦ, where

ϕ(t/µ)µ

npk−1 . (51) Note that Mr

Φ =

![image 154](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile154.png>)

(Hp) = 0 for all j ≥ 0, which in view of (46) and (47) implies T (β,γ,r,t). Hence, using r0 = r ≥ max{npk−1,aΦ} and (36), we infer

(Hp) = 0 entails Mr

j

0

r/C

npk−1 er

1 n

1 n

≤

(Hp) > 0) = P(Mr(Hp) ≥ 1) ≤

P(¬T (β,γ,r,t)) ≤ P(Mr

exp −aΦ/C . (52)

![image 155](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile155.png>)

![image 156](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile156.png>)

![image 157](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile157.png>)

0

We henceforth assume r < aΦ. Using Lemma 17, rj = 2jr ≥ npk−1 and s ≥ 1, we infer for n ≥ n0(β) that P((46) fails) ≤

√

![image 158](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile158.png>)

ts/rj⌉)

(Hp) ≥ ⌈β

P(Mr

j

√t/s

![image 159](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile159.png>)

j∈N:rj≤

(53)

rj3/2 n2(β√ts)3/2 · exp −β

√

√

- 1

![image 160](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile160.png>)

- 2n


![image 161](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile161.png>)

![image 162](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile162.png>)

exp −β

≤

ts/C ≤

ts/C ,

![image 163](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile163.png>)

![image 164](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile164.png>)

√t/s

![image 165](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile165.png>)

j∈N:rj≤

(Hp) ≥ 1, for n ≥ n0(β) a similar argument (exploiting that rj ≥

(Hp) ≥ 1 implies Mr

where the last inequality follows analogously to (49). Observing that Mr

√t implies β√t/rj ≤ β ≤ 1) yields P((47) fails) ≤

j

j+1

![image 166](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile166.png>)

![image 167](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile167.png>)

√

![image 168](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile168.png>)

(Hp) ≥ ⌈β

t/rj⌉)

P(Mr

j

j∈N:√t/s≤rj≤max{2√t,r}

![image 169](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile169.png>)

![image 170](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile170.png>)

(54)

β√t/C

β√t/C

![image 171](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile171.png>)

![image 172](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile172.png>)

npk−1 erj

npk−1s e√t

- 1

![image 173](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile173.png>)

- 2n


- 1

![image 174](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile174.png>)

- 2n


≤

≤

.

max

√t/s

![image 175](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile175.png>)

![image 176](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile176.png>)

![image 177](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile177.png>)

![image 178](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile178.png>)

j∈N:rj≥

(To clarify: the condition rj ≤ max{2√t,r} ensures that the considered range of rj is non-empty.) In the following we exploit the assumption r < aΦ to further estimate (54). Note that log(1 + x) ≤ x implies

![image 179](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile179.png>)

ϕ(x) = (1 + x)log(1 + x) − x ≤ x2. (55) In view of (51) and (55), using Φ > r/a ≥ npk−1/a and µ = e(H)pk ≥ an2pk we deduce

t2 ≥ ϕ(t/µ)µ2 = Φµnpk−1 ≥ n4p3k−2. (56) Since k ≥ 3 and γ ≤ 1/8 (in fact, γ ≤ (k − 2)/8 suﬃces), using (56) and (44) we obtain

npk−1s e√t ≤

p(k−2)/4s e ≤

p(k−2)/4−γ e ≤

p1/4−γ e ≤

pγ e

= e−s. (57)

![image 180](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile180.png>)

![image 181](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile181.png>)

![image 182](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile182.png>)

![image 183](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile183.png>)

![image 184](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile184.png>)

![image 185](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile185.png>)

Now, inserting (57) into (54), in view of (53) we infer (for r < aΦ) that

P(¬T (β,γ,r,t)) = P((46) or (47) fails) ≤

√

1 n

![image 186](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile186.png>)

exp −β

ts/C ,

![image 187](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile187.png>)

which together with (52), C = kD and Φ ≥ ϕ(t/µ)µ2/Λ completes the proof of (50).

![image 188](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile188.png>)

![image 189](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile189.png>)

![image 190](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile190.png>)

![image 191](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile191.png>)

We are now ready to prove the upper bound of Theorem 6, and our main remaining task is to pick a suitable parameter r. Here the technical condition (35) prevents the natural choice r = CΛ/µ = Θ(1+npk−1) when npk−1 ≈ 1, which explains the more involved form of r in the next proof (this complication is only needed in the pedestrian case (iii) below).

- Proof of (9) of Theorem 6. It suﬃces to consider the following three cases: (i) p ≥ γn−1/(k−1)(log n)1/(k−1), (ii) p ≤ n−1/(k−1)−γ, and (iii) t ≥ min γ min{(VarX)2/3,µ2/3}(log n)4/3,µp(k−2)/3−γ . Of course, in all cases we may assume γ ≤ 1/8 (decreasing γ yields less restrictive assumptions), and in case (iii) we may also assume n−1/(k−1)−γ ≤ p ≤ n−1/(2k), say (otherwise case (i) or (ii) applies). We start by introducing several parameters. By Remark 7 there is a constant b = b(k,a,D) ∈ (0,1] such that for all p ∈ [0,1/2] we have


VarX ≥ bΛ. (58) Let β = 1/(32k). Deﬁne s = s(γ) as in (48), and set

32k2D γk−1 ,

3B min{1,a1/2,b}

Λ µ

24kD min{1,a1/2,b}γ3/2

ϕ(t/µ)µ √ts

r = Ar,˜ A = max

, and r˜ = max

,

,

,

![image 192](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile192.png>)

![image 193](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile193.png>)

![image 194](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile194.png>)

![image 195](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile195.png>)

![image 196](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile196.png>)

![image 197](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile197.png>)

- where B = B(k,D) is as in Lemma 19. We defer the proof of the claim that r satisﬁes the technical condition (35), and ﬁrst apply Lemmas 13 and 18–19. So, using the deﬁnition of r, it follows that


P(X ≥ µ + t) ≤ P(Xr ≥ µ + t/2) + P(¬T (β,γ,r,t)) ≤ exp −

min{a,β} 2kD

1 n

ϕ(t/µ)µ 4kr

exp −

+

min

![image 198](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile198.png>)

![image 199](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile199.png>)

![image 200](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile200.png>)

ϕ(t/µ)µ2 Λ

min{a,β,1} 4kA

≤ (1 + n−1)exp −

min

,

![image 201](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile201.png>)

![image 202](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile202.png>)

ϕ(t/µ)µ2 Λ

,

![image 203](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile203.png>)

√

![image 204](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile204.png>)

ts .

√

![image 205](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile205.png>)

ts

Since s = log(e/pγ) ≥ γ log(e/p), this establishes (9) with c = γ min{a,β,1}/(4kA).

In the remainder we verify the technical condition (35). For later reference, note that r˜ ≥ Λ/µ ≥ max{npk−1,1}. (59)

Recalling r = Ar˜, in case (i) we have r ≥ Anpk−1 ≥ Aγk−1 log n, and in case (ii) we have npk−1 ≤ n−(k−1)γ and r ≥ A. In both cases, using r ≥ max{eBnpk−1,B} and r ≥ A ≥ 8kD/γk−1 we infer that

Bnpk−1/r r ≤ min e−r, (npk−1)r ≤ max n−Aγ

k−1

, n−A(k−1)γ ≤ n−8kD. (60) The remaining case (iii) requires somewhat tedious case distinctions. Recalling (24), it follows that

µ1/2 3s

min{t1/2,t3/2/µ} 3s ≥ {t≥µ}

ϕ(t/µ)µ √ts ≥

r˜ ≥

![image 206](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile206.png>)

![image 207](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile207.png>)

![image 208](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile208.png>)

![image 209](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile209.png>)

t3/2 3µs

+ {t<µ}

. (61)

![image 210](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile210.png>)

With foresight, note that (44) and p ≥ n−1/(k−1)−γ imply, for n ≥ n0, that s = log(e/pγ) ≤ min{1 + γ log(1/p), p−γ} ≤ min{logn, p−γ}. (62)

Using (58) and p = o(1) we have VarX ≥ bµ, where b ∈ (0,1]. Combining this estimate with the assumed lower bound for t in the case (iii), using µ = e(H)pk ≥ an2pk and (62) it follows that

µ1/2p(k−2)/2−3γ/2 s ≥ min γ3/2b logn, a1/2npk−1−γ/2 . (63)

γ3/2b(log n)2 s

t3/2 µs ≥ min

,

![image 211](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile211.png>)

![image 212](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile212.png>)

![image 213](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile213.png>)

Since k ≥ 3 and γ ≤ 1/8 imply 1 ≥ p(k−2)/2−3γ/2, note that the ﬁnal expression in (63) is also a lower bound for µ1/2/s. In view of (61), we thus infer

r˜ ≥ 3−1 min{a1/2,b} · min γ3/2 log n, npk−1−γ/2 . (64)

If the minimum in (64) is attained by the γ3/2 log n term, then r = Ar˜ ≥ eBr˜ and (59) imply (Bnpk−1/r)r ≤ e−r = e−Ar˜, so that Ar˜ ≥ 8kD log n establishes (35). Otherwise the minimum in (64) is attained by the npk−1−γ/2 term, in which case r = Ar˜ implies (Bnpk−1/r)r ≤ (pγ/2)r by choice of A. Using p ≤ n−1/(2k) and r = Ar˜ ≥ A ≥ 32k2D/γ, this readily establishes (35), completing the proof.

![image 214](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile214.png>)

![image 215](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile215.png>)

![image 216](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile216.png>)

![image 217](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile217.png>)

# 4 Lower bounds

In this section we establish the lower bounds (7) and (10) of Theorem 4 and 6. The proofs are based on three diﬀerent ‘conﬁgurations’ of the vertices in Vp(H), which each yield a distinct lower bound for the upper tail of X = e(Hp). The heuristic idea is that one of them should hopefully always approximate the most likely way to obtain X ≈ (1 + ε)µ or X ≈ µ + t, respectively. In brief, we shall use conﬁgurations where many edges cluster on few vertices (Section 4.1), where many edges arise disjointly (Section 4.2), or where there are overall too many vertices (Section 4.3). Here one main novelty is on a conceptual level: in contrast to previous work we obtain, in a wide range, the correct dependence on t = εµ.

- 4.1 Conﬁgurations with clustering


The ﬁrst lower bound is based on property X(H,D,x) deﬁned in (5), which intuitively states that many edges can cluster on comparatively few vertices. In other words, enforcing W ⊆ Vp(H) for a reasonably small set of vertices W is enough to guarantee that the number of induced edges X = e(Hp) = e(H[Vp(H)]) is fairly large. A related approach was taken in [25] and [22] for arithmetic progressions and subgraphs, respectively.

- Theorem 20. Given a hypergraph H, set X = e(Hp) and µ = EX. For all D ≥ 1, p ∈ (0,1] and t ≥ 0 satisfying X(H,D,µ + t) and µ + t ≥ 1 we have


P(X ≥ µ + t) ≥ exp −D√µ + tlog(1/p) . (65)

![image 218](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile218.png>)

Proof. By X(H,D,µ + t) there is W ⊆ V (H) satisfying |W| ≤ D√µ + t and e(H[W]) ≥ µ + t. Hence P(X ≥ µ + t) ≥ P(W ⊆ Vp(H)) = p|W| ≥ pD

![image 219](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile219.png>)

√µ+t, completing the proof.

![image 220](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile220.png>)

![image 221](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile221.png>)

![image 222](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile222.png>)

![image 223](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile223.png>)

![image 224](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile224.png>)

Using a new ‘local’ variant of the above argument we now improve the √µ + t in the exponent of (65) to √t, which is crucial when t = o(µ). The basic idea is to ‘create’ at least µ + t edges as follows: (i) ﬁrst we use the above clustering construction to ‘locally’ enforce, say, 2t edges, and (ii) then we use correlation inequalities and a one-sided version of Chebyshev’s inequality to show that typically at least µ − t of the remaining r = e(H) − 2t edges are present in Hp. (The crux is that the expected number of remaining edges is at least rpk = µ − 2tpk.) This approach seems of independent interest, and a similar reasoning can, e.g., be used to reﬁne the lower bounds for subgraph counts obtained by Janson, Oleszkiewicz and Ruci´nski [22].

![image 225](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile225.png>)

![image 226](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile226.png>)

- Theorem 21. Given k ≥ 2, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Set X = e(Hp), µ = EX and Λ = µ(1 + npk−1). Given α ∈ (0,1), there are n0 > 0 (depending only on k,a,D) and c,λ ≥ 1 (depending only on α,k,a,D) such that for all n ≥ n0, p ∈ (0,1 − α] and t ≥ {µ≥1/2} min{


√

√

![image 227](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile227.png>)

![image 228](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile228.png>)

Λ} satisfying X(H,D,min{λt,µ + t}) and µ + t ≥ 1 we have

VarX,

√

![image 229](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile229.png>)

P(X ≥ µ + t) ≥ exp −c

tlog(1/p) . (66)

√

√

![image 230](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile230.png>)

![image 231](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile231.png>)

Λ} will be convenient later on. Before giving the proof of Theorem 21, let us informally discuss the structure of the argument. The clustering construction intuitively ‘marks’ a set of 2t edges in H. Let Z denote the number of ‘unmarked’ edges that occur in Hp, so EZ = (e(H) − 2t)pk = µ − 2tpk. The punchline is that the clustering construction (which enforces the 2t ‘marked’ edges) allows us to shift our focus from the unlikely event X ≥ EX +t to the ‘typical’ event Z ≥ EZ −t/2. Indeed, it turns out that, using Harris’ inequality [18] and µ = EZ + 2tpk, for suitable W ⊆ V (H) with |W| = O(√t) and e(H[W]) ≥ 2t we eventually arrive at

We remark that the form of the somewhat strange-looking assumption t ≥ {µ≥1/2} min{

VarX,

![image 232](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile232.png>)

√t) · P(Z ≥ EZ − t + 2tpk).

![image 233](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile233.png>)

P(X ≥ µ + t) ≥ P(W ⊆ Vp(H)) · P(Z ≥ µ − t) ≥ pΘ(

It seems plausible that Var Z = O(Var X) holds. A folklore variant of the Paley–Zygmund inequality states that, given any random variable Y ≥ 0, for all 0 ≤ t < EY we have

t2 VarY + t2

P(Y ≥ EY − t) ≥

. (67)

![image 234](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile234.png>)

√

![image 235](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile235.png>)

So, assuming p ≤ 1/2 (which implies 2pk ≤ 1/2 for k ≥ 2), for t ≥

VarX we should intuitively obtain

t2 VarZ + t2

P(Z ≥ EZ − t + 2tpk) ≥ P(Z ≥ EZ − t/2) ≥ Ω

= Ω(1).

![image 236](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile236.png>)

The proof below makes this reasoning rigorous, but there are a number of subtle issues (which make the details somewhat cumbersome). For example, the parameter t may be very small, so we can not, as usual, ignore rounding issues. Furthermore, to allow for p ≤ 1 − α we need to plant λt copies (instead of just 2t copies) for carefully chosen λ = λ(α,k) > 0. In addition, the W ⊆ Vp(H) based construction does not work if λt is larger than the total number of edges e(H), so we shall only enforce min{λt,µ + t} copies.

- Proof of Theorem 21. We defer the elementary proof of the fact that there is λ = λ(α,k) > 0 satisfying λt ≥ 2. (68)


Deﬁning x = min{λt,µ + t}, by X(H,D,x) there is W ⊆ V (H) satisfying |W| ≤ D√λt and e(H[W]) ≥ x. To later avoid rounding issues, we pick β + 1 ∈ [λ/2,λ] such that (β + 1)t is an integer. Deﬁning y = min{(β + 1)t,µ + t}, note that there is G ⊆ H[W] with e(G) = ⌈y⌉. Deﬁne Y = e(G[Vp(H)]). Clearly,

![image 237](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile237.png>)

√

![image 238](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile238.png>)

P(Y ≥ y) = P(Y ≥ min{(β + 1)t,µ + t}) ≥ P(W ⊆ Vp(H)) = p|W| ≥ pD

λt. (69)

In the case µ ≤ βt we have µ + t ≤ y, so that P(X ≥ µ + t) ≥ P(X ≥ y) ≥ P(Y ≥ y) and (69) establish inequality (66) for any constant c satisfying c ≥ D

√

![image 239](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile239.png>)

λ (we defer the precise choice of c).

Henceforth we focus on the more interesting case µ > βt. Deﬁne Z = X − Y . Since Y ≥ (β + 1)t and Z ≥ µ − βt are both increasing events, using X = Y + Z, Harris’ inequality [18], and (69) we infer

P(X ≥ µ + t) ≥ P(Y ≥ (β + 1)t and Z ≥ µ − βt) ≥ P(Y ≥ (β + 1)t)P(Z ≥ µ − βt) ≥ pD

(70)

√

![image 240](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile240.png>)

λtP(Z ≥ µ − βt).

We defer the proof of the conceptually straightforward (but slightly tedious) claim that

EY ≤ (β − 1)t, (71) VarZ ≤ Ct2, (72)

- where C = C(k,a,D,λ) ≥ 1. Using EZ −t = EX −EY −t ≥ µ−βt and the Paley–Zygmund inequality (67), for d = log1−α(1/(C + 1)) > 0 it follows (exploiting 1 − α ≥ p and 1 ≤ λt) that


t2 Var Z + t2 ≥

√

1 C + 1

![image 241](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile241.png>)

λt. (73)

= (1 − α)d ≥ pd ≥ pd

P(Z ≥ µ − βt) ≥ P(Z ≥ EZ − t) ≥

![image 242](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile242.png>)

![image 243](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile243.png>)

√

√

![image 244](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile244.png>)

![image 245](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile245.png>)

Inserting (73) into (70) establishes inequality (66) with c = D

λ + d

λ.

It remains to prove the auxiliary claims (68) and (71)–(72). Let λ = 4/(1 − (1 − α)k). Writing Ye = {e⊆Vp(H)}, note that Harris’ inequality yields E(YeYf) ≥ EYeEYf. As EYe2 = EYe, we infer

E(YeYf) − EYeEYf ≥

VarX =

(e,f)∈H×H

(1 − EYe)EYe ≥ (1 − pk)µ ≥ (1 − (1 − α)k)µ = 4µ/λ. (74)

e∈H

Observing Λ ≥ µ and t ≥ 1 − µ, using the assumed lower bound for t (and λ ≥ 4) it follows that

λt ≥ λ {µ≥1/2} min 4µ/λ,√µ + {µ<1/2}(1 − µ) ≥ 2,

![image 246](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile246.png>)

![image 247](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile247.png>)

establishing the claimed inequality (68). Recall that we only need to prove (71)–(72) whenever µ > βt. In this case ⌈y⌉ = (β + 1)t holds by choice of β, so that (1 − α)k = 1 − 4/λ and β + 1 ≥ λ/2 imply

EY = ⌈y⌉pk ≤ (β + 1)(1 − α)kt = β + 1 − (β + 1)4/λ t ≤ (β − 1)t,

establishing the claimed inequality (71). To get a handle on VarZ in (72), note that Z is a restriction of X to a subset of the edges of H. So, with (74) and E(YeYf)− EYeEYf ≥ 0 in mind, it is not diﬃcult to see that VarZ ≤ VarX holds. By Remark 7 there is a constant A = A(k,a,D) > 0 such that

VarX ≤ AΛ = Aµ(1 + npk−1). (75)

Recalling µ ≥ an2pk, it is easy to see that µ < 1/2 implies p = O(n−2/k) and VarX ≤ B = B(A,k,a,D) > 0. Using (75) and the assumed lower bound for t in case of µ ≥ 1/2, it follows (exploiting 1 ≤ λt) that

VarZ ≤ VarX ≤ {µ<1/2}B + {µ≥1/2} max{A,1}t2 ≤ max{Bλ2,A,1}t2, completing the proof.

![image 248](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile248.png>)

![image 249](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile249.png>)

![image 250](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile250.png>)

![image 251](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile251.png>)

√p VarX,1}, say. Furthermore, for p = o(1) and t = O(µ) with t = ω(1) we can easily improve the constant c by planting only (1 + o(1))t edges (in some cases, this approach presumably yields the ‘optimal’ form of the exponent).

![image 252](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile252.png>)

Using a variant of the above proof, it alternatively suﬃces to assume t ≥ max{

- 4.2 Conﬁgurations with many disjoint edges


The second lower bound is based on the heuristic that, for small p, most edges of Hp should arise disjointly. Exploiting the implied ‘approximate independence’ of the edges, we obtain the following Chernoﬀ-like lower bound. In fact, (76) is of sub-Gaussian type since EX = (1 + o(1))VarX for the p under consideration.

- Theorem 22. Given k ≥ 3, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Set X = e(Hp), µ = EX and ϕ(x) = (1 + x)log(1 + x) − x. There are n0,c,d > 0 (depending only on k,a,D) such that for all n ≥ n0, 0 < p ≤ n−2/(k+1/3) and t ≥ 0 satisfying 1 ≤ µ + t ≤ 9 max{µ,n1/(2k)} we have


P(X ≥ µ + t) ≥ dexp −cϕ(t/µ)µ ≥ dexp −ct2/µ . (76)

We have not tried to optimize p ≤ n−2/(k+1/3), but conjecture that this condition can be relaxed to p = O(n−1/(k−1)). In fact, it would be interesting to have a general method which yields such Poisson-type lower bounds for the upper tail when VarX = (1 + o(1))EX holds (for the lower tail this was very recently settled by Janson and Warnke [26]). In the proof of Theorem 22 we shall use the idea that, for small p, most edges f ∈ H should appear disjointly (and thus nearly independently) in Hp. The next lemma makes this more precise: it relates P(X = m) with P(Bin(e(H),pk) = m) over a convenient (but ad-hoc) range of m.

Lemma 23. Given k ≥ 3, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Set X = e(Hp) and µ = EX. There are n0,b > 0 (depending only on k,a,D) such that for all n ≥ n0, 0 < p ≤ n−2/(k+1/3) and integers 0 ≤ m ≤ 99 max{µ,n1/(2k)} we have

e(H) m

pkm(1 − pk)e(H)−m. (77)

P(X = m) ≥ e−b

With Lemma 23 in hand, the proof of Theorem 22 essentially reduces to folklore lower bounds for the binomial distribution (based on Stirling’s formula); we include the details in Appendix A for completeness (some minor care is needed when t is small). A similar analysis can be used to tighten related results in the theory of random graphs due to DeMarco and Kahn [11] and Sileikisˇ [40].

Let us informally discuss the strategy used in the proof of Lemma 23. For (77) the basic plan is to consider the event that Hp consists of exactly m vertex disjoint edges. It turns out that, for small m, there are roughly e(mH) ways to select such edge collections, and with probability pkm their m disjoint edges are all present. Of course, we also need to take into account that all of the remaining e(H) − m edges are not present (to avoid overcounting). If these were independent events, then this would yield another factor of (1− pk)e(H)−m, and for small p we expect that this is usually close to the truth. The proof below follows the discussed outline, dropping the (de facto redundant) disjointness condition. However, we need to deal with one subtle technicality that we ignored so far: given a collection of edges {f1,...,fm} ⊆ H, it can happen that the union of their vertex sets i∈[m] fi induces additional ‘extra’ edges from H (even if all the fi are vertex disjoint). In particular, for our construction this means that the second part is impossible: in this ‘bad’ case at least one of the remaining e(H) − m edges must occur. Luckily, such bad edge collections are rare for small m, so we can simply ignore them in our proof (see the deﬁnition of Sm below).

Proof of Lemma 23. Deﬁne

Sm = I ⊆ H : e(I) = m, and there are no g ∈ H \ I with g ⊆

f . (78)

f∈I

Recall that f ∈ Hp if and only if f ⊆ Vp(H). As the union of all edges in I ∈ Sm contains at most km vertices, we have P(I ⊆ Hp) ≥ pkm (for disjoint edges this would hold with equality.) So, since the events {I = Hp}I∈Sm

are mutually exclusive, using P(I = Hp) = P(I ⊆ Hp)P(I = Hp | I ⊆ Hp) it follows that P(X = m) ≥

P(I ⊆ Hp)P(I = Hp | I ⊆ Hp) ≥ |Sm|pkm min

P(I = Hp | I ⊆ Hp). (79)

I∈Sm

I∈Sm

It remains to estimate |Sm| and P(I = Hp | I ⊆ Hp) from below. We defer the routine proof of the auxiliary claim that there is λ = λ(k,a,D) > 0 such that for n ≥ n0(k,a,D) we have

k3D3nm2/e(H) ≤ 1/2 and max nm3/e(H), m2p, nmpk−1 ≤ λ. (80)

We bound |Sm| from below by constructing certain edge-subsets I = {f1,...,fm} ∈ Sm, counting the number of choices in each step. For 0 ≤ j < m we iteratively select fj+1 ∈ H \ (B1,j+1 ∪ B2,j+1), where

Bx,j+1 = f ∈ H : there is g ∈ H with |g ∩

fi| ≥ x and |g ∩ f| ≥ 3 − x .

i∈[j]

Since {f1,...,fj} ⊆ B1,j+1 holds (consider g = f = fi), all edges fi are distinct (in fact, vertex disjoint). Next, aiming at a contradiction, suppose there is an edge g ∈ H \ I and an index ℓ ∈ [m] such that

g ⊆ i∈[ℓ] fi and g  ⊆ i∈[ℓ−1] fi. If |g ∩ i∈[ℓ−1] fi| = 1, then |g ∩ fℓ| = k − 1 ≥ 2 implies fℓ ∈ B1,ℓ. If |g∩ i∈[ℓ−1] fi| ≥ 2, then |g∩fℓ| ≥ 1 implies fℓ ∈ B2,ℓ. Both conclusions contradict fℓ  ∈ (B1,ℓ∪B2,ℓ), showing that all constructed sets I = {f1,...,fm} indeed satisfy I ∈ Sm. Turning to the number of choices in the above greedy construction, note that |B1,j+1| ≤ kj · ∆1(H) · k2 ∆2(H) and |B2,j+1| ≤ kj2 ∆2(H) · k∆1(H). Since ∆2(H) ≤ D and ∆1(H) ≤ v(H)∆2(H) ≤ D2n, we infer that for each edge fj+1 there are at least

e(H) − |B1,j+1| + |B2,j+1| ≥ e(H) − k3D3nj/2 + k3D2nj2/2 ≥ e(H) − k3D3nj2

choices. Recall that 1 − x ≥ e−2x if x ∈ [0,1/2]. Since each edge-subset I can be generated in up to m! diﬀerent ways by our greedy construction, using zy/y! ≥ y z and (80) it follows for b = 8k3D3λ that, say,

e(H) − k3D3nj2 m! ≥

e(H)m m!

|Sm| ≥ 0≤j<m

![image 253](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile253.png>)

![image 254](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile254.png>)

e(H) m

e(H) m

exp −2k3D3nm3/e(H) ≥

≥

k3D3nm2 e(H)

1 −

![image 255](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile255.png>)

e−b/4.

m

(81)

Next, we estimate P(I = Hp | I ⊆ Hp) for all I ∈ Sm. Let F2 contain all g ∈ H\I with 2 ≤ |g∩ f∈I f| < k. Similarly, let F1 contain all g ∈ H\I with |g ∩ f∈I f| = 1. Set F0 = H\(I ∪F1 ∪F2), and note that by deﬁnition of Sm, see (78), all g ∈ F0 satisfy |g ∩ f∈I f| = 0. Since f ∈ Hp if and only if f ⊆ Vp(H), using Harris’ inequality [18] we deduce, say,

P(I = Hp | I ⊆ Hp) = P

{g  ⊆ Vp(H)} |

f ⊆ Vp(H)

g∈F0∪F1∪F2

f∈I

≥ (1 − pk)|F

0|(1 − pk−1)|F

1|(1 − p)|F

2|.

Note that |F1| ≤ km · ∆1(H) and |F2| ≤ km2 · ∆2(H). Since ∆1(H) ≤ D2n and ∆2(H) ≤ D, using (80) we infer, by choice of b = 8k3D3λ, that

|F1|pk−1 + |F2|p ≤ kD2nmpk−1 + k2Dm2p ≤ (kD2 + k2D)λ ≤ b/4. Recalling 1 − x ≥ e−2x if x ∈ [0,1/2], using p ≤ 1/2 and |F0| ≤ e(H) − m we thus obtain P(I = Hp | I ⊆ Hp) ≥ (1 − pk)|F

1|pk−1+|F2|p) ≥ (1 − pk)e(H)−me−b/2, which together with (79) and (81) establishes inequality (77), with room to spare.

0|e−2(|F

In the remainder we sketch the veriﬁcation of (80), using the convention that all implicit constants may depend on k,a,D. Let α = 2/(k + 1/3) and β = 2 − kα = 2/(3k + 1) = α/3, so that µ = O(n2pk), p ≤ n−α and 1/(2k) ≤ β imply m = O(nβ). Using e(H) = Ω(n2), p ≤ n−α and β < 1/3 it now is routine to check that (80) holds for suitable λ > 0 (as 2β−1 < 0 and max{3β−1, 2β−α, 1+β−(k−1)α} ≤ 0 for k ≥ 3).

![image 256](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile256.png>)

![image 257](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile257.png>)

![image 258](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile258.png>)

![image 259](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile259.png>)

- 4.3 Conﬁgurations with too many vertices


Our third lower bound is based on the following heuristic: if Vp(H) contains ‘too many vertices’ (more than expected), then it seems likely that the induced subgraph Hp = H[Vp(H)] also contains ‘too many edges’ (more than the average number). For moderately large p, this approach eventually yields the following lower bound of sub-Gaussian type (by Remark 7 we have Λ = Θ(VarX), since p is bounded away from one).

Theorem 24. Given k ≥ 2, a > 0 and D ≥ 1, let H = Hn be a k-uniform hypergraph satisfying v(H) ≤ Dn, e(H) ≥ an2 and ∆2(H) ≤ D. Set X = e(Hp), µ = EX, Λ = µ(1 + npk−1) and ϕ(x) = (1 + x)log(1 + x) − x. Given α ∈ (0,1), there are n0 > 0 (depending only on k,a,D) and β,c > 0 (depending only on α,k,a,D) such that for all n ≥ n0, αn−1/(k−1) ≤ p ≤ 1 − α and min{

√Λ,√VarX} ≤ t ≤ βµ we have

![image 260](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile260.png>)

![image 261](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile261.png>)

P(X ≥ µ + t) ≥ exp −cϕ(t/µ)µ2/Λ ≥ exp −ct2/Λ . (82)

The key observation is that µ2/Λ = Θ(np) for the relevant range of p. With this in mind, the proof of Theorem 24 is based on the following two ideas: (i) since Vp(H) ∼ Bin(v(H),p) and v(H) = Θ(n), with probability at least exp(−Θ(ε2np)) = exp(−Θ((εµ)2/Λ)) we have |Vp(H)| ≥ (1 + ε)E|Vp(H)|, and (ii) conditioning on |Vp(H)| ≥ (1+ε)E|Vp(H)| intuitively increases the expected number e(Hp) = e(H[Vp(H)]) of induced edges, eﬀectively turning the unlikely event X ≥ µ+t into a ‘typical’ one; see also (83) below. For the number of copies of H in the binomial random graph Gn,p an analogous reasoning (based on a deviation of the number of edges) applies for p = Ω(n−1/m

2(H)), where m2(H) is the so-called 2-density of H; for the lower tail this idea was used by Janson and Warnke [26].

We now informally discuss the high-level structure of the proof, which is similar to Theorem 21. Let µ = EX, ε = t/µ and m = (1 + ε)E|Vp(H)|. Applying (i) as outlined above, using monotonicity we expect that

P(X ≥ µ + t) ≥ P(|Vp(H)| ≥ m) · P X ≥ µ + t |Vp(H)| ≥ m ≥ e−Θ(t

2/Λ) · P X ≥ µ + t | |Vp(H)| = m . Thinking of the uniform random graph Gn,m, using E|Vp(H)| = v(H)p it seems plausible that E(X | |Vp(H)| =

- m) is approximately e(H)· m/v(H) k = (1+ε)kEX. Similarly, we expect Var(X | |Vp(H)| = m) = O(Var X) for ε = O(1). Noting t = εEX and (1+ε)k > 1+2ε, we see that E(X | |Vp(H)| = m)−t ought to be roughly

at least (1 + ε)EX = µ + t. To sum up, for t ≥

√VarX the Paley–Zygmund inequality (67) should yield

![image 262](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile262.png>)

P X ≥ µ + t |Vp(H)| = m ≥ P X ≥ E X |Vp(H)| = m − t |Vp(H)| = m ≥ Ω

t2 VarX + t2

![image 263](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile263.png>)

= Ω(1),

(83)

and the following proof basically makes this rigorous (with some care about border cases).

Proof of Theorem 24. Let ε = t/µ, N = v(H), and m = (1 + ε)Np. Given 0 ≤ j ≤ N, we henceforth write Pj(·) = P(· | |Vp(H)| = j) for brevity. We analogously use Ej(·) and Varj(·), respectively. Note that, by monotonicity, we have

P(X ≥ µ + t) ≥

j≥m

Pj(X ≥ µ + t)P(|Vp(H)| = j) ≥ Pm(X ≥ µ + t)P(|Vp(H)| ≥ m). (84)

It remains to estimate Pm(X ≥ µ + t) and P(|Vp(H)| ≥ m) from below. We start by deﬁning β = β(α,k,a,D) ∈ (0,1) in a somewhat technical way (that will be convenient in border cases). We use the convention that all implicit constants may depend on k,a,D (but not on α). In particular, e(H) = Ω(n2) and ∆2(H) = O(1) imply v(H) = Ω(n), so that N = Θ(n). Observing that ΛNp/µ2 = Θ(1 + (npk−1)−1) holds, we infer

ε2Np = Ω(ε2µ2/Λ) and ε2Np = O (1 + α−(k−1))ε2µ2/Λ . (85) Furthermore, by assumption and Remark 7 we have εµ = t ≥ min{

√Λ,√VarX} = Ω(√αΛ), so that ε2Np = Ω(α) by (85). With ε ≤ β in mind, we now pick β ∈ (0,α/4] small enough such that

![image 264](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile264.png>)

![image 265](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile265.png>)

![image 266](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile266.png>)

εNp = ε2Np/ε = Ω(αβ−1) ≥ 2k2 and Np = Ω(αβ−2) ≥ 16α−2. (86) Note that m = (1 + ε)Np ≤ (1 + α)(1 − α)N < N. So, since N = Θ(n) and |Vp(H)| ∼ Bin(N,p), for

- n ≥ n0(k,a,D) folklore estimates for binomial random variables yield P(|Vp(H)| ≥ m) = P(|Vp(H)| ≥ (1 + ε)Np) ≥ d1 exp −c1ε2Np) , (87)


where the constants c1,d1 > 0 depend only on α,k,a,D. (This can, e.g., be deduced analogous to the proof of Theorem 22 by means of Stirling’s formula. One minor diﬀerence in the estimates is perhaps that in (97) we can, e.g., via 1 − q = 1 − p ≥ α and j ≤ 4T = 4 max{εNp,√Np} here directly obtain j2/ (1 − q)N = O(α−1ε2Np + α−1), say. To be pedantic, by choice of β in (86) we have also ensured that M ≤ Np + 4T = Np(1 + 4 max{ε,1/√Np}) ≤ N(1 − α)(1 + α) < N holds.)

![image 267](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile267.png>)

![image 268](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile268.png>)

Turning to Pm(X ≥ µ + t), note that ε ≤ β ≤ 1 implies ϕ(ε) = Θ(ε2) via (24) and (55). So, in view of (85), (87) and ε = t/µ, we see that (82) follows if Pm(X ≥ µ + t) ≥ d2 = d2(α,k,a,D) > 0. Deﬁne If = {f⊆V

p(H)}, so that X = f∈H If. Let Vm(H) ⊆ V (H) with |Vm(H)| = m be chosen uniformly at random. Observe that Vp(H) conditioned on |Vp(H)| = m has the same distribution as Vm(H). Using m = (1 + ε)Np ≥ 2k2, |f| = k ≥ 2 and EIf = pk it follows that

N − k m − k

m − i N − i ≥ (1 − k/m)k(m/N)k ≥ (1 − k2/m)(1 + ε)2EIf.

N m

Em(If) =

=

![image 269](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile269.png>)

0≤i<k

Hence Em(X) ≥ (1 − k2/m)(1 + ε)2EX. Furthermore, by (86) we have m = (1 + ε)Np ≥ 2k2(1 + ε)ε−1, which implies (1 − k2/m)(1 + ε) ≥ 1 + ε/2. So, recalling t = εµ = εEX, we obtain

Em(X) − t/2 ≥ (1 + ε/2)(1 + ε)EX − εEX/2 ≥ (1 + ε)EX = µ + t. (88) Similar standard calculations (see, e.g., the proof of Theorem 15 in [26]) show that, say,

Em(IeIf) − Em(Ie)Em(If) ≤ (1 + ε)2k

E(IeIf). (89)

Varm(X) =

(e,f)∈H×H:e∩f =∅

(e,f)∈H×H

It is not diﬃcult to see that the ﬁnal expression of (89) is at most 4k · O(Λ), so that Remark 7 and 1 − p ≥ α imply Varm(X) = O(α−1 min{Λ,VarX}), say. Using the assumed lower bounds for t, we now infer Varm(X) = O(α−1t2). Recalling (88), the Paley–Zygmund inequality (67) implies

(t/2)2 Varm(X) + (t/2)2

Pm(X ≥ µ + t) ≥ Pm(X ≥ Em(X) − t/2) ≥

= Ω

![image 270](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile270.png>)

which, as discussed, completes the proof.

1 α−1 + 1

![image 271](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile271.png>)

,

![image 272](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile272.png>)

![image 273](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile273.png>)

![image 274](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile274.png>)

![image 275](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile275.png>)

- 4.4 Proof of the lower bounds of Theorem 4 and 6 (and Remark 8)


In this section we combine the previous estimates, and prove the lower bounds of Theorem 4 and 6 (as well as Remark 8). This is in principle straightforward but, at least as written here, requires several case distinctions (that are not very illuminating). Some complications are due to the fact that the results of Sections 4.1–4.3 are only valid in some range of the parameters (they need to be merged seamlessly), whereas others stem from the fact that our estimates are uniform (e.g., our n0 does not depend on ε or γ), from the fact that our assumptions are very weak (e.g., p > 0 instead of p ≥ n−2/k), or from the fact that the exponents are more involved than usual (e.g., (10) yields up to ﬁve diﬀerent asymptotic expressions).

Proof of (7) of Theorem 4. The case √µlog(1/p) ≤ µ is easy: then Theorem 20 implies P(X ≥ (1 + ε)µ) ≥ exp −2D max{1,√ε}

![image 276](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile276.png>)

√µlog(1/p) . (90)

![image 277](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile277.png>)

![image 278](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile278.png>)

In the remainder we may thus assume √µlog(1/p) ≥ µ, which for n ≥ n0(k,a) implies p ≤ n−2/(k+1/3), with room to spare. If εµ ≤ max{µ,n1/(2k)}, then Theorem 22 and 1 ≤ 2 max{µ,εµ} (as (1 + ε)µ ≥ 1) yield

![image 279](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile279.png>)

P(X ≥ (1 + ε)µ) ≥ exp − log(1/d) − cε2µ ≥ exp −2 max{2 log(1/d),c} max{1,ε2}µ . (91)

It remains to consider the case εµ ≥ max{µ,n1/(2k)}. Since p log(1/p) ≤ 1 analogous to (44), using µ ≤ D3n2pk and p ≤ n−2/(k+1/3) it follows for n ≥ n0(k,D) that

√µlog(1/p) ≤ {p≤n−4/(k−2)}D3/2np(k−2)/2 · p log(1/p) + {p≥n−4/(k−2)}4D3/2npk/2 log(n) ≤ n1/(2k) ≤ εµ.

![image 280](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile280.png>)

Since √1 + ε ≤ 2ε (as εµ ≥ µ implies ε ≥ 1), now Theorem 20 gives

![image 281](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile281.png>)

![image 282](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile282.png>)

P(X ≥ (1 + ε)µ) ≥ exp −D (1 + ε)µlog(1/p) ≥ exp −2Dε2µ . (92) To sum up, (90)–(92) readily establish the lower bound (7), completing the proof.

![image 283](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile283.png>)

![image 284](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile284.png>)

![image 285](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile285.png>)

![image 286](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile286.png>)

- Proof of (10) of Theorem 6 and Remark 8. Note that we may assume γ ≤ 1/2 (since decreasing γ yields less restrictive assumptions). We use the convention that all implicit constants may depend on k,a,D (not


on γ), and tacitly assume n ≥ n0(k,a,D) whenever necessary. With foresight, we start with some technical but useful auxiliary estimates. Recalling (24), for t = βµ we have ϕ(t/µ)µ2 ≥ min{β,β2}µ2/3. Since µ = Θ(n2pk) and Λ = µ(1 + npk−1), it follows for t = βµ that

min β1/2,β3/2 µ1/2 3(1 + npk−1)log(1/p)

ϕ(t/µ)µ2 √tlog(1/p)Λ ≥

![image 287](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile287.png>)

![image 288](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile288.png>)

![image 289](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile289.png>)

Ω(npk/2) log(1/p)

Ω(1) pk/2−1 log(1/p)

= min β1/2,β3/2 {p<n−1/(k−1)}

+ {p≥n−1/(k−1)}

![image 290](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile290.png>)

![image 291](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile291.png>)

.

(93)

Analogously to (44), calculus yields p1/2 log(1/p) ∈ (0,2] for p ∈ (0,1). Since k ≥ 3 entails pk/2−1 ≤ p1/2, we see that γn−2/k(log n)2/k ≤ p ≤ 1 − γ and t ≥ µ imply C1√tlog(1/p) ≤ ϕ(t/µ)µ2/Λ, where C1 = C1(γ,k,a,D) > 0. Replacing log(1/p) with log(e/p) in (93), we similarly see that C2√tlog(e/p) ≤ ϕ(t/µ)µ2/Λ for all γn−2/k(log n)2/k ≤ p ≤ 1 and t ≥ µ, where C2 = C2(γ,k,a,D) > 0. Since (24) and (55) imply ϕ(t/µ)µ2 = Θ(t2) for t ≤ µ, this completes the proof of Remark 8 (by adjusting the constants n0,c,C).

![image 292](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile292.png>)

![image 293](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile293.png>)

We turn to (10) of Theorem 6, and start with case (iii), where γn−1/(k−1) ≤ p ≤ 1 − γ. Applying Theorem 21 and 24 (with α = γ) there is β = β(γ,k,a,D) > 0 such that

√

tlog(1/p) , {t≤βµ} exp −c2ϕ(t/µ)µ2/Λ . (94)

![image 294](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile294.png>)

P(X ≥ µ + t) ≥ max exp −c1

Proceeding as in the discussion following (93), for t ≥ βµ we infer A√tlog(1/p) ≤ ϕ(t/µ)µ2/Λ, where A = A(β,γ,a,k,D) > 0. Replacing c2 by c3 = max{c2,c1/A} we thus can remove the indicator {t≤βµ} in (94), establishing (10).

![image 295](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile295.png>)

Next we consider case (ii) in the range n−1/(k−1) ≤ p ≤ n−1/(k−1) log n. As in (58), by Remark 7 we have VarX ≥ bΛ ≥ bµ, where b = b(k,a,D) ∈ (0,1]. Since Λ = O(µ(log n)k−1) and µ = Ω(n(k−2)/(k−1)), it is easy to see that t ≥ b2/3µ2/3(log n)2/3 ≥

√Λ holds. Hence, by case (iii) above there is nothing to show.

![image 296](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile296.png>)

We now turn to case (i), where p ≤ n−2/(k+1/3). If √tlog(1/p) ≤ ϕ(t/µ)µ2/Λ holds, then using ϕ(t/µ)µ2 ≤ t2, see (55), and Λ = Θ(µ) we infer t ≥ Λ2/3(log(1/p))2/3 ≥ {µ≥1/2}

![image 297](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile297.png>)

√Λ, so Theorem 21 applies. Noting µ2/Λ = Θ(µ), it thus remains to show that Theorem 22 applies when ϕ(t/µ)µ2/Λ ≤

![image 298](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile298.png>)

√tlog(1/p). Aiming at a contradiction, we now assume that t ≥ 8 max{µ,n1/(2k)}. Noting that ϕ(x) = (1 + x)log(1 + x) − x ≥ x(log x)/2 for x ≥ e2 ≈ 7.4, using Λ = Θ(µ) we infer

![image 299](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile299.png>)

ϕ(t/µ)µ2 √tlog(1/p)Λ ≥

t1/2µlog(t/µ) 2 log(1/p)Λ

log(t/µ) log(1/p)

= n1/(4k) · Ω

1 ≥

. (95)

![image 300](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile300.png>)

![image 301](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile301.png>)

![image 302](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile302.png>)

![image 303](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile303.png>)

We now argue that the right hand side of (95) is ω(1). Observe that p ≤ n−2/(k−1) implies t/µ ≥ Ω(n1/(2k)/(n2pk) = ω(p−1), and that p ≥ n−2/(k−1) implies log(t/µ)/ log(1/p) ≥ Ω((log n)−1). In both cases we readily obtain a contradiction in (95) for large n, which by our above discussion establishes (10).

Finally, by case (i) above it remains to verify case (ii) in the range n−2/(k+1/3) ≤ p ≤ n−1/(k−1). Note that Λ = Θ(µ), VarX ≥ bΛ ≥ bµ, and µ = Ω(n2/(k+1)) imply t ≥ b2/3µ2/3(log n)2/3 ≥

√

![image 304](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile304.png>)

Λ and µ + t ≥ 1, with room to spare. In case of t ≤ µ, by (24) we have ϕ(t/µ)µ2 ≥ t2/3, so that Λ = Θ(µ) yields

ϕ(t/µ)µ2 √tlog(1/p)Λ ≥

t3/2 3 log(1/p)Λ ≥

bµlog n 3 log(1/p)Λ

= Ω(1).

![image 305](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile305.png>)

![image 306](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile306.png>)

![image 307](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile307.png>)

![image 308](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile308.png>)

Using the discussion after (93) in case of t ≥ µ, it thus follows (in both cases) that B√tlog(1/p) ≤ ϕ(t/µ)µ2/Λ, where B = B(b,γ,k,a,D) > 0. Hence an application of Theorem 21 establishes (10).

![image 309](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile309.png>)

![image 310](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile310.png>)

![image 311](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile311.png>)

![image 312](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile312.png>)

![image 313](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile313.png>)

Acknowledgements. I would like to thank Oliver Riordan and Matas Sileikisˇ for many useful remarks on an earlier version of this paper, and Svante Janson for a helpful discussion. I am also grateful to the referee for an exceptionally careful reading, and for numerous constructive suggestions concerning the presentation.

# References

- [1] N. Alon and J. Spencer. The probabilistic method. Third edition. Wiley-Interscience Series in Discrete Mathematics and Optimization. John Wiley & Sons Inc., Hoboken, NJ (2008).
- [2] A. Baltz, P. Hegarty, J. Knape, U. Larsson, and T. Schoen. The structure of maximum subsets of {1, . . . , n} with no solutions to a + b = kc. Electron. J. Combin. 12 (2005), Paper 19.
- [3] J. van den Berg and J. Jonasson. A BK inequality for randomly drawn subsets of ﬁxed size. Probab. Theory Related Fields 154 (2012), 835–844.
- [4] J. van den Berg and H. Kesten. Inequalities with applications to percolation and reliability. J. Appl. Probab. 22

(1985), 556–569.

- [5] S. Boucheron, G. Lugosi, and P. Massart. Concentration inequalities using the entropy method. Ann. Probab. 31 (2003), 1583–1614.
- [6] S. Boucheron, G. Lugosi, and P. Massart. Concentration inequalities. A nonasymptotic theory of independence. Oxford Univ. Press, Oxford (2013).
- [7] S. Chatterjee. The missing log in large deviations for triangle counts. Random Struct. Alg. 40 (2012), 437–451.
- [8] S. Chatterjee and P.S. Dey. Applications of Stein’s method for concentration inequalities. Ann. Probab. 38

(2010), 2443–2485.

- [9] S. Chatterjee and S.R.S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin. 32 (2011), 1000–1017.
- [10] B. DeMarco and J. Kahn. Upper tails for triangles. Random Struct. Alg. 40 (2012), 452–459.
- [11] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Struct. Alg. 41 (2012), 469–487.
- [12] A. Dembo. Information inequalities and concentration of measure. Ann. Probab. 25 (1997), 927–939.
- [13] D.P. Dubhashi and A. Panconesi. Concentration of measure for the analysis of randomized algorithms. Cambridge Univ. Press, Cambridge (2009).
- [14] P. Erd˝s and P. Tetali. Representations of integers as the sum of k terms. Random Struct. Alg. 1 (1990), 245–261.
- [15] E. Friedgut, V. Ro¨dl, and M. Schacht. Ramsey properties of random discrete structures. Random Struct. Alg. 37 (2010), 407–436.
- [16] R. Graham, V. Ro¨dl, and A. Rucin´ski. On Schur properties of random subsets of integers. J. Number Theory 61

(1996), 388–408.

- [17] B. Green. The Cameron–Erd˝s conjecture. Bull. London Math. Soc. 36 (2004), 769–778.
- [18] T.E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc. 56 (1960), 13–20.
- [19] S. Janson. Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221–229.
- [20] S. Janson. New versions of Suen’s correlation inequality. Random Struct. Alg. 13 (1998), 467–483.
- [21] S. Janson, T.  Luczak, and A. Rucin´ski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York (2000).
- [22] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math. 142 (2004), 61–92.
- [23] S. Janson and A. Rucin´ski. The infamous upper tail. Random Struct. Alg. 20 (2002), 317–342.
- [24] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica 24 (2004), 615–640.
- [25] S. Janson and A. Rucin´ski. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat. 49 (2011), 79–96.
- [26] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Struct. Alg. 48 (2016), 219–246.
- [27] J.H. Kim and V.H. Vu. Concentration of multivariate polynomials and its applications. Combinatorica 20 (2000), 417–434.
- [28] M. Ledoux. The concentration of measure phenomenon, vol. 89 of Mathematical Surveys and Monographs. American Mathematical Society, Providence (2001).
- [29] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Struct. Alg., to appear. arXiv:1210.7013.
- [30] C. McDiarmid. On the method of bounded diﬀerences. In Surveys in Combinatorics (Norwich, 1989), London Math. Soc. Lecture Note Ser., vol. 141, pp. 148–188. Cambridge Univ. Press, Cambridge (1989).
- [31] C. McDiarmid and B. Reed. Concentration for self-bounding functions and an inequality of Talagrand. Random Struct. Alg. 29 (2006), 549–557.
- [32] D. Reimer. Proof of the van den Berg-Kesten conjecture. Combin. Probab. Comput. 9 (2000), 27–32.


- [33] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Struct. Alg. 46 (2015), 391–395.
- [34] V. Ro¨dl and A. Rucin´ski. Random graphs with monochromatic triangles in every edge coloring. Random Struct. Alg. 5 (1994), 253–270.
- [35] J. Rue´ and A. Zumalac´rregui. Threshold functions for systems of equations on random sets. Preprint (2012). arXiv:1212.5496.
- [36] W. Samotij. Stability results for random discrete structures. Random Struct. Alg. 44 (2014), 269–289.
- [37] A.A. Sapozhenko. The Cameron–Erd˝s conjecture. Dokl. Akad. Nauk 393 (2003), 749–752.
- [38] M. Schacht. Extremal results for random discrete structures. Preprint (2009).
- [39] W. Schudy and M. Sviridenko. Concentration and moment inequalities for polynomials of independent random variables. In Proceedings of the Twenty-Third Annual ACM-SIAM Symposium on Discrete Algorithms (SODA ’12), pp. 437–446, SIAM (2012). arXiv:1104.4997.
- [40] M. Sileikis.ˇ On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin. 19 (2012), Paper 4.
- [41] J. Spencer. Counting extensions. J. Combin. Theory Ser. A 55 (1990). 247–255.
- [42] M. Talagrand. Concentration of measure and isoperimetric inequalities in product spaces. Inst. Hautes Etudes´ Sci. Publ. Math. 81 (1995), 73–205.
- [43] V.H. Vu. Concentration of non-Lipschitz functions and applications. Random Struct. Alg. 20 (2002), 262–316.
- [44] L. Warnke. When does the K4-free process stop? Random Struct. Alg. 44 (2014), 355–397.
- [45] L. Warnke. On the method of typical bounded diﬀerences. Combin. Probab. Comput. 25 (2016), 269–299.
- [46] L. Warnke. On the missing log in upper tail estimates. Preprint (2016).
- [47] G. Wolfovitz. A concentration result with application to subgraph count. Random Struct. Alg. 40 (2012), 254–267.


# A Appendix

The following proof is based on Stirling’s approximation formula 1 ≤ x!/[√2πx(x/e)x] ≤ e1/(12x). Some of the minor complications below stem from the fact that our assumption µ + t ≥ 1 is extremely weak.

![image 314](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile314.png>)

- Proof of Theorem 22. With foresight, let T = max{t,√µ}, L = ⌈µ + T⌉ and M = ⌈µ + 2T⌉. Clearly,


![image 315](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile315.png>)

P(X ≥ µ + t) ≥ P(X ≥ µ + T) ≥

P(X = m). (96)

m∈N:L≤m≤M

In view of Lemma 23, we now estimate the right hand side of (77). To avoid clutter, let N = e(H) and q = pk. Recalling 1 − x ≤ e−x, µ = Nq > 0 and Stirling’s formula, standard (somewhat tedious but simple) calculations show that for any µ + j ∈ N satisfying 1 ≤ µ + j < N we have, say,

N µ + j

exp −12(µ1+j) − 12(N−1µ−j) 2π(µ + j)(1 − q − Nj ) 1 + µj

![image 316](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile316.png>)

![image 317](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile317.png>)

qµ+j(1 − q)N−µ−j ≥

![image 318](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile318.png>)

N−µ−j

µ+j

![image 319](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile319.png>)

1 − N−j µ

![image 320](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile320.png>)

![image 321](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile321.png>)

![image 322](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile322.png>)

2

exp −16 − (µ + j)log(1 + j/µ) − j − j

![image 323](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile323.png>)

![image 324](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile324.png>)

(1−q)N

≥

.

![image 325](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile325.png>)

![image 326](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile326.png>)

2π(µ + j)

(97)

Note that (µ+j)log(1+j/µ)−j = ϕ(j/µ)µ, and that ϕ(j/µ) is monotone increasing in j ≥ 0. Since µ+t ≥ 1 implies T ≥ 1/2, we deduce M − µ ≤ 2T + 1 ≤ 4T. Since N = e(H) ≥ an2, from the proof of Lemma 23 it follows that M ≤ µ + 4T = O(nβ) satisﬁes M2/N = o(1) and M < N. In particular, q = pk ≤ 1/2 implies j2/ (1 − q)N ≤ 2M2/N = o(1). By combining (96) with Lemma 23 and (97), we now infer that, say,

exp −(b + 1) − ϕ(4T/µ)µ √2πM

P(X ≥ µ + t) ≥ ⌊max{T,1}⌋ ·

.

![image 327](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile327.png>)

![image 328](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile328.png>)

√

M ≥ 1/√4. Next we estimate ϕ(4T/µ)µ. If T = √µ holds, then ϕ(4T/µ)µ ≤ 16T2/µ = 16 by (55), and if T = t holds, then ϕ(4T/µ)µ ≤ 16ϕ(t/µ)µ by applying (25) twice. Combining our ﬁndings, it follows that, say,

Noting that max{T,1} = max{t,√µ,1} and M ≤ 4 max{t,µ,1}, we deduce max{T,1}/

![image 329](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile329.png>)

![image 330](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile330.png>)

![image 331](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile331.png>)

![image 332](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile332.png>)

√

P(X ≥ µ + t) ≥ e−(b+17)/

![image 333](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile333.png>)

32π · exp − {t>√µ}16ϕ(t/µ)µ ,

![image 334](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile334.png>)

which together with (55) readily establishes (76) with c = 16 and d = e−(b+17)/√32π.

![image 335](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile335.png>)

![image 336](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile336.png>)

![image 337](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile337.png>)

![image 338](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile338.png>)

![image 339](<2016-warnke-upper-tails-arithmetic-progressions_images/imageFile339.png>)

