arXiv:1406.1248v1[math.PR]5Jun2014

The lower tail: Poisson approximation revisited

Svante Janson∗ and Lutz Warnke† May 27, 2014

Abstract

The well-known “Janson’s inequality” gives Poisson-like upper bounds for the lower tail probability P(X (1 − ε)EX) when X is the sum of dependent indicator random variables of a special form. We show that, for large deviations, this inequality is optimal whenever X is approximately Poisson, i.e., when the dependencies are weak. We also present correlation-based approaches that, in certain symmetric applications, yield related conclusions when X is no longer close to Poisson. As an illustration we, e.g., consider subgraph counts in random graphs, and obtain new lower tail estimates, extending earlier work (for the special case ε = 1) of Janson,  Luczak and Rucin´ski.

# 1 Introduction

In probabilistic combinatorics and related areas it often is important to estimate the probability that a sum X of dependent indicator random variables is small or zero (to, e.g., show that few or none of a collection of events occurs). Moreover, it frequently is desirable that these probabilities are exponentially small (to, e.g., make union bound arguments amenable). In this paper we focus on such sharp estimates for the lower tail P(X (1 − ε)EX), where X is of a form that is commonly used in, e.g., applications of the probabilistic method or random graph theory, see [1, 16]. More precisely, the underlying probability space is the random subset Γp ⊆ Γ, with |Γ| = N and p = (pi)i∈Γ, where each i ∈ Γ is included, independently, with probability pi. Given a family Q(α) α∈X of subsets of Γ (often X ⊆ 2Γ and Q(α) = α is convenient) we deﬁne Iα = {Q(α)⊆Γ

p}, so that

X =

Iα (1)

α∈X

counts the number of sets Q(α) that are entirely contained in Γp. We write α ∼ β if Q(α) ∩ Q(β) = ∅ and α = β, which intuitively means that there are ‘dependencies’ between Iα and Iβ. Let

µ = EX =

EIα, Π = max α∈X

EIα,

α∈X

EIαIβ = (1 + δ)µ.

Λ = µ +

(α,β)∈X×X:α∼β

(We write µ(X), Π(X), Λ(X) and δ(X) in case of ambiguity.) Note that δ measures how dependent the indicators Iα are (with δ = 0 in the case of independent summands), and that VarX Λ holds. In [13] the ﬁrst author proved the following lower tail analogue (often called Janson’s inequality, see, e.g., [1]) of the Bernstein and Chernoﬀ bounds for sums of independent indicators (the case δ = 0): with ϕ(x) = (1+x)log(1+x)−x, for all ε ∈ [0,1] we have

P(X (1 − ε)EX) exp −ϕ(−ε)µ/(1 + δ) = exp −ϕ(−ε)µ2/Λ , (2)

![image 1](<2014-janson-lower-tail-poisson-approximation_images/imageFile1.png>)

∗Department of Mathematics, Uppsala University, PO Box 480, SE-751 06 Uppsala, Sweden. E-mail: svante.janson@math.uu.se. Partly supported by the Knut and Alice Wallenberg Foundation.

†Department of Pure Mathematics and Mathematical Statistics, Wilberforce Road, Cambridge CB3 0WB, UK. E-mail: L.Warnke@dpmms.cam.ac.uk.

where ϕ(−1) = 1, ε2/2 ϕ(−ε) ε2 and ϕ(−ε) = ε2/2 + O(ε3) for ε ∈ [0,1]. As discussed in [13, 16, 1], inequality (2) is quite attractive because it (i) yields Poisson-like tail estimates in the weakly dependent case δ = O(1), (ii) usually corresponds to a (one-sided) exponential version of Chebyshev’s inequality, and (iii) often qualitatively matches the tail behaviour suggested by the central limit theorem. For example, it is well-known (and not hard to check) that Λ = Θ(VarX) if p = max{Π,maxi pi} is bounded away from one, that p → 0 implies Λ ∼ VarX, and that δ,Π → 0 implies Λ ∼ µ ∼ VarX.

The inequality (2) is nowadays a widely used tool in probabilistic combinatorics (see, e.g., [1, 16] and the references therein), which makes it important to understand how ‘sharp’ it is, i.e., whether the exponential rate of decay given by (2) is best possible. For sums of independent Bernoulli random variables we have δ = 0 and (2) coincides with the Chernoﬀ bounds, where the exponent is well-known to be best possible if maxi pi = o(1). However, it is doubtful whether such examples are of any signiﬁcance for concrete applications with δ > 0. Fortunately, whenever Π < 1, Harris’ inequality [12] gives, as noted in [15],

P(X = 0)

(1 − EIα) exp −µ/(1 − Π) . (3)

α∈X

The point is that (2) and (3) yield log P(X = 0) ∼ −µ whenever δ,Π → 0. This raises the intriguing question whether the exponent of (2) is also sharp for other choices of ε, in particular when ε → 0 (which, of course, is also an interesting problem in concentration of measure).

- 1.1 Main result


In this paper we prove that “Janson’s inequality” (2) is close to best possible in many situations of interest. Our ﬁrst result shows that, for large deviations, the rate of decay of (2) is optimal for any random variable

- X of type (1) that is approximately Poisson, i.e., whenever δ,Π → 0 (see [13]). Theorem 1. With notations as above, if ε ∈ [0,1], max{Π, {ε<1}δ} 2−14 and ε2µ {ε<1}, then


P(X (1 − ε)EX) exp −(1 + ξ)ϕ(−ε)µ , (4) with ξ = 135 max{Π1/8, {ε<1}δ1/8, {ε<1}(ε2µ)−1/4}.

With ϕ(−1) = 1 in mind, note that (4) qualitatively extends the lower bound (3) resulting from Harris’ inequality [12] to general ε. Here the condition ε2µ = Ω(1) is natural in the context of exponentially small probabilities since (1 + ξ)ϕ(−ε) = Θ(ε2). As discussed, our favourite range is when δ,Π → 0. For large deviations, i.e., when ε2µ → ∞ holds, (2) and (4) then yield

log P(X (1 − ε)EX) ∼ −ϕ(−ε)µ.

In words, Theorem 1 determines the large deviation rate function log P(X (1 − ε)EX) up to second order error terms, closing a gap that was left open by the ﬁrst author nearly 25 years ago. Indeed, Theorem 2 in [13] gives a lower bound, but it is at best oﬀ from the upper bound (2) by a (multiplicative) constant factor in the exponent, and even this holds only for a more restricted range of the parameters. Furthermore,

- Theorem 1 with δ = 0 also implies the optimality of the Chernoﬀ bounds mentioned above. Our second result yields a related conclusion when δ = O(1) and Π is bounded away from one. More

precisely, in this ‘weakly dependent’ case Theorem 2 shows that the decay of the inequality (2) is best possible up to constant factors in the exponent.

- Theorem 2. With notations as above, if ε ∈ [0,1], Π < 1 and ε2µ {ε<1/50}(1 + δ)−1/2, then P(X (1 − ε)EX) exp −Kϕ(−ε)µ(1 + δ∗) exp −Kε2µ(1 + δ∗) , (5)


with K = 5000/(1 − Π)5 and δ∗ = {ε<1/50}δ.

A key feature of (5) is that it holds for any Π < 1 (and that the dependence of K on Π is explicit). Note that usually K = Θ(1). Whenever δ = O(1), inequalities (2) and (5) then yield

log P(X (1 − ε)EX) = −Θ(ε2µ),

where the implicit constants diﬀer by a factor of at most 2K(1 + δ)2 = O(1). This subsumes the folklore fact that Chernoﬀ bounds (where δ = 0) are sharp up to constants in the exponent if maxi pi is bounded away from one. While the numerical value of K is often immaterial, better constant factors can typically be obtained, if desired, by reworking the proof (optimizing certain parameters to the situation at hand).

The proofs of Theorem 1 and 2 hinge on Ho¨lder’s inequality and several estimates of the Laplace transform (which in turn are based on correlation inequalities), see Section 2. In fact, an inspection of the proofs reveals that Theorem 1 and 2 (as well as (3), Theorem 6 and Lemma 7) remain valid for the more general correlation conditions (and setup) stated by Riordan and Warnke [23]. It would be interesting to know whether similar results also hold under the weaker dependency assumptions of Suen’s inequality [28, 14].

- 1.2 Main example


From an applications point of view it is important to also understand the sharpness of (2) in the case δ = Ω(1), i.e., when X is no longer close to Poisson. In Section 3 we present correlation-inequality based bootstrapping approaches which often allow us to deal with this remaining ‘strongly dependent’ case. The punchline seems to be that, in the presence of certain symmetries, the inequality (2) is oftentimes best possible up to constant factors in the exponent.

In this paper our main example is the number of small subgraphs in the binomial random graph Gn,p, which is a classical topic in random graph theory (see, e.g., [10, 3, 24]). It frequently serves as a test-bed for new probabilistic estimates (see, e.g., [2, 15, 27, 21, 18, 17, 7]), and we shall use it to demonstrate the applicability of our bootstrapping approaches. In fact, we consider the more general random hypergraph G(n,pk), with k 2, where each of the nk edges of the complete k-uniform hypergraph Kn(k) is included, independently, with probability p. Given a k-uniform hypergraph H, or brieﬂy k-graph, we deﬁne XH = XH(n,p) as the number of copies of H in G(n,pk), where by a copy we mean, as usual, a subgraph isomorphic to H. Furthermore, we write eH = |E(H)| and vH = |V (H)| for the number of edges and vertices of H, respectively. Theorem 3 shows that the lower tail of the distribution of XH is governed by ΦH, i.e., the expected number of copies of the ‘least expected’ subgraph of H. This exponential rate of decay is consistent with normal approximation heuristics since ΦH = Θ (1 − p)(EXH)2/ VarXH , see Lemma 3.5 in [16].

- Theorem 3. Let H be a k-graph with eH 1. Deﬁne ΦH = ΦH(n,p) = min{EXJ : J ⊆ H,eJ 1}. There are positive constants c, C, D and n0, all depending only on H, such that for all n n0, p ∈ [0,1) and ε ∈ [0,1] satisfying ε2ΦH {ε<1}D we have


exp −(1 − p)−5Cε2ΦH P(XH (1 − ε)EXH) exp −cε2ΦH . (6)

The upper bound of (6) follows from (2) via standard calculations (see, e.g., [16] or Lemma 22), and so the real content of this theorem is the ‘matching’ lower bound. A key feature of Theorem 3 is that ε is not ﬁxed, but may depend on n. In the context of exponentially decaying probabilities, note that the ε2ΦH = Ω(1) condition is natural (unless p ≈ 1). In applications p is typically bounded away from one (in fact, p = o(1) is often standard), in which case (6) yields

log P(XH (1 − ε)EXH) = −Θ(ε2ΦH), (7)

determining the large deviation rate function of XH up to constants factors. For the special case ε = 1 (and k = 2) this was established more than 25 years ago by Janson,  Luczak and Ruci´nski [15], and for ε ε0 an analogous statement is nowadays easily deduced from (2) and (3), see also (73). By contrast, the case ε → 0 seems to have eluded further attention, and Theorem 3 rectiﬁes this (surprising) gap in the literature.

Although not our primary focus, in certain ranges our proof techniques are strong enough to establish the ﬁner behaviour of the large deviation rate function. In particular, for the case in which there is only one subgraph G ⊆ H with EXG = Θ(ΦH) we have two results that determine the leading constant in (7). More precisely, Theorem 4 applies if there is only one copy of G in H (which includes the case G = H), and Theorem 5 applies if G is an edge (in which case there are eH copies of G in H). To state these results, for any given k-graph H we set

eJ − 1 vJ − k

mk(H) = {e

H 2} max

![image 2](<2014-janson-lower-tail-poisson-approximation_images/imageFile2.png>)

J⊆H,eJ 2

+ {e

H=1}

1 k

. (8)

![image 3](<2014-janson-lower-tail-poisson-approximation_images/imageFile3.png>)

In addition, we deﬁne ex(n,H) as the maximum number of edges in an H-free k-graph with n vertices. It is well-known (see, e.g., [20]) that πH = limn→∞ ex(n,H)/ nk exists, with πH ∈ [0,1), and that for graphs (i.e., k = 2) we have πH = 1 − 1/(χ(H) − 1), where χ(H) is the chromatic number of H.

- Theorem 4. Let G ⊆ H be k-graphs with eG 1. Assume that there is exactly one copy of G in H, and that p = p(n) = o(1) is such that EXG = o(EXJ) for all G = J ⊆ H with eJ 1. If ε = ε(n) ∈ (0,1] satisﬁes

ε2EXG {ε<1}ω 1 + {G =H,e

G 2} log(1/ε) , then we have log P(XH (1 − ε)EXH) ∼ −ϕ(−ε)EXG. (9)

- Theorem 5. Let H be a k-graph with eH 1. If p = p(n) = o(1) and ε = ε(n) ∈ [0,1] satisfy p =

ω(n−1/m

k(H)) and ε2 nk p = ω(1), then we have

log P(XH (1 − ε)EXH) ∼

−ϕ(−ε) nk p/e2H, if ε = o(1), −ϕ(−ε) nk p(1 − πH), if ε = 1 − o(1).

(10)

Here our main contributions are the tight lower bound of (9), and the case ε = o(1) of (10). Theorem 4 is a natural extension of earlier work of Janson,  Luczak and Ruci´nski [15] for the special case ε = 1 (and k = 2). Theorem 5 partially solves an open problem of [15], but in the relevant case ε = 1 inequality (10) is a fairly simple consequence of the recent ‘hypergraph container’ results of Saxton and Thomason [25], see also Lemma 23. With ϕ(−ε) = Θ(ε2) in mind the conditions involving ε2 are natural in both results – up to the logarithmic term in case of Theorem 4, which seems to be an artefact of our proof (we leave its removal as an open problem, see Section 3.2). The form of the exponent in Theorem 5 diﬀers in an intriguing way for ε = o(1) and ε = 1 − o(1). In particular, (10) provides a natural example where the inequality (2) does not always give the correct constants in the exponent when δ = ω(1): in the case ε = 1−o(1), the ‘extremal’ structural properties of H-free graphs come into play. We leave it as an open problem to determine the ﬁner behaviour of the exponent (i.e., with explicit constants) in the ‘intermediate’ range ε = Θ(1). This seems of particular interest since Theorem 4 and 5 nearly cover all edge probabilities p for balanced k-graphs with eH 2 and mk(H) = (eH − 1)/(vH − k), where G = H for p = o(n−1/m

k(H)); for k = 2 (when this class usually is called 2-balanced) this class includes, e.g., trees, cycles, complete graphs, complete r-partite graphs Kt,...,t and the d-dimensional cube.

Finally, Theorems 3–5 compare favourable with related work for the upper tail probability P(XH (1+ε)EXH), where the case ε = Θ(1) has been extensively studied for k = 2, see, e.g., [27, 29, 17, 5, 8, 26, 6] and the references therein. Indeed, for most graphs H the order of magnitude of the large deviation rate function log P(XH (1+ε)EXH) is only known up to logarithmic factors when ε = Θ(1), whereas Theorem 3 determines log P(XH (1 − ε)EXH) up to constant factors, even when ε = ε(n) → 0. For triangles the ﬁner behaviour of log P(XK

3

(1 + ε)EXK

3

) has very recently been determined for ε = Θ(1) and n−1/42+o(1) p = o(1), see [22]. By contrast, for all balanced k-graphs H (which for k = 2 includes H = K3) Theorems 4–5 apply for essentially all p = o(1) of interest, excluding only p = Θ(n−1/m

k(H)). However, the key conceptual diﬀerence is that Theorem 4 includes the case ε = ε(n) → 0.

The rest of the paper is organized as follows. First, in Section 2, we prove Theorem 1 and 2. Next, in Section 3, we present several bootstrapping approaches that yield lower bounds for the lower tail, which are subsequently illustrated in Section 4. Namely, in Section 4.1 we apply them to the number of arithmetic progressions in random subsets of the integers, and in Section 4.2 we apply them to subgraph counts in random hypergraphs and prove Theorems 3–5.

2 Lower bounds for the lower tail

In this section we prove Theorem 1 and 2, i.e., establish lower bounds for the lower tail. Since our core argument breaks down when ε is very close to one, en route to Theorem 1 we establish the following (slightly sharper) complementary estimates.

- Theorem 6. Let X = α∈X Iα, µ = EX, Π and δ be deﬁned as in Section 1. If e(1 − ε)ε2µ 1 and


- 0 ε 1 − 4 max{Π1/4,δ1/4}, then P(X < (1 − ε)EX) exp −(1 + ξ)ϕ(−ε)µ , (11)


with ξ = 135 max{Π1/4,δ1/4,[e(1 − ε)ε2µ]−1/2}.

- Lemma 7. Let X = α∈X Iα, µ = EX and Π be deﬁned as in Section 1. If 1 − e−1 ε 1 and Π < 1, then

P(X (1 − ε)EX) P(X = 0) exp −(1 + ζ)ϕ(−ε)µ , (12) with ζ = 10 max{

√1 − ε,Π/(1 − Π)}.

![image 4](<2014-janson-lower-tail-poisson-approximation_images/imageFile4.png>)

While Lemma 7 follows from (3) via calculus (see Lemma 11), the remaining proofs are not a mere reﬁnement of [13], but contain several new ideas and ingredients. This includes integrating the logarithmic derivative of the Laplace transform over the interval [r,t] instead of the usual [0,t] (see the proof of Lemma 9), using Ho¨lder’s inequality with parameter p → 1 instead of the Cauchy–Schwarz inequality (see Section 2.2), and a careful treatment of second order error terms (see, e.g., Lemma 8 and 14).

- 2.1 Preliminaries We ﬁrst collect some basic estimates of the Laplace transform of X as deﬁned in Section 1.


- Lemma 8. For all s 0 satisfying λ = Π(1 − e−s) < 1 we have

Ee−sX exp −µ(1 − e−s) −

µΠ(1 − e−s)2 2(1 − λ)

![image 5](<2014-janson-lower-tail-poisson-approximation_images/imageFile5.png>)

. (13)

Proof. The FKG inequality [11] (or Harris’s inequality [12]) yields Ee−sX = E

α∈X

e−sI

α

α∈X

Ee−sI

α

=

α∈X

1 − EIα(1 − e−s) .

Now, for x ∈ [0,1) we have

log(1 − x) = −

j 1

xj j −x −

![image 6](<2014-janson-lower-tail-poisson-approximation_images/imageFile6.png>)

x2 2(1 − x)

![image 7](<2014-janson-lower-tail-poisson-approximation_images/imageFile7.png>)

, (14)

and (13) follows since EIα Π and µ = α∈X EIα.

![image 8](<2014-janson-lower-tail-poisson-approximation_images/imageFile8.png>)

![image 9](<2014-janson-lower-tail-poisson-approximation_images/imageFile9.png>)

![image 10](<2014-janson-lower-tail-poisson-approximation_images/imageFile10.png>)

![image 11](<2014-janson-lower-tail-poisson-approximation_images/imageFile11.png>)

- Lemma 9. For all t r 0 we have Ee−rX

![image 12](<2014-janson-lower-tail-poisson-approximation_images/imageFile12.png>)

Ee−tX

exp

µ 1 + δ

![image 13](<2014-janson-lower-tail-poisson-approximation_images/imageFile13.png>)

e−(1+δ)r − e−(1+δ)t . (15)

Proof. Let Ψ(x) = Ee−xX. The proof of Lemma 1 in [13] establishes −dxd log Ψ(x) µe−(1+δ)x for x 0 (see also [23]). Hence

![image 14](<2014-janson-lower-tail-poisson-approximation_images/imageFile14.png>)

log

Ee−rX Ee−tX

![image 15](<2014-janson-lower-tail-poisson-approximation_images/imageFile15.png>)

= − logΨ(t) + log Ψ(r) =

t

r

−

d dx

![image 16](<2014-janson-lower-tail-poisson-approximation_images/imageFile16.png>)

log Ψ(x) dx

t

r

µe−(1+δ)xdx =

µ 1 + δ

![image 17](<2014-janson-lower-tail-poisson-approximation_images/imageFile17.png>)

e−(1+δ)r − e−(1+δ)t ,

and (15) follows.

![image 18](<2014-janson-lower-tail-poisson-approximation_images/imageFile18.png>)

![image 19](<2014-janson-lower-tail-poisson-approximation_images/imageFile19.png>)

![image 20](<2014-janson-lower-tail-poisson-approximation_images/imageFile20.png>)

![image 21](<2014-janson-lower-tail-poisson-approximation_images/imageFile21.png>)

Next, we state some technical estimates of ϕ(−ε) = (1 − ε)log(1 − ε) + ε for later reference (these can safely be skipped on ﬁrst reading). Following standard conventions, for k ∈ {1,2} we have 0 logk(0) = limεր1(1 − ε)logk(1 − ε) = 0, so that ϕ(−1) = 1.

- Lemma 10. For all ε ∈ [0,1] we have max (1 − ε)log2(1 − ε),ε2 2ϕ(−ε) min log2(1 − ε),2ε2 . (16)
- Lemma 11. For all 1 − e−1 ε 1 we have ϕ(−ε) 1 (1 + 5√1 − ε)ϕ(−ε). (17)


![image 22](<2014-janson-lower-tail-poisson-approximation_images/imageFile22.png>)

- Lemma 12. For all ε ∈ [0,1] and A ∈ [0,∞) we have, with γ = A − 1,


ϕ(−Aε)

(1 + Aε)A2ϕ(−ε), if Aε 1, (1 + √γ)ϕ(−ε), if 0 3√γ 1 − ε.

![image 23](<2014-janson-lower-tail-poisson-approximation_images/imageFile23.png>)

![image 24](<2014-janson-lower-tail-poisson-approximation_images/imageFile24.png>)

The elementary proofs of Lemma 10–12 are deferred to Appendix A.

(18)

- 2.2 Proof strategy

We start with a general lower bound for P(X < (1 − ε)EX). If p,q ∈ (1,∞) satisfy 1/p + 1/q = 1, then Ho¨lder’s inequality implies

E(e−sX {X<(1−ε)EX}) (Ee−psX)1/pP(X < (1 − ε)EX)1/q. Noting that q = q/p + 1 = 1/(p − 1) + 1, we infer

P(X < (1 − ε)EX)

E(e−sX {X<(1−ε)EX}) (Ee−psX)1/p

![image 25](<2014-janson-lower-tail-poisson-approximation_images/imageFile25.png>)

q

=

E(e−sX {X<(1−ε)EX}) Ee−sX

![image 26](<2014-janson-lower-tail-poisson-approximation_images/imageFile26.png>)

p p−1

![image 27](<2014-janson-lower-tail-poisson-approximation_images/imageFile27.png>)

·

Ee−sX Ee−psX

![image 28](<2014-janson-lower-tail-poisson-approximation_images/imageFile28.png>)

1 p−1

![image 29](<2014-janson-lower-tail-poisson-approximation_images/imageFile29.png>)

Ee−sX.

(19)

In the following we heuristically outline how we estimate P(X < (1 −ε)EX) when δ,Π → 0 and ε < 1 (to be precise, ε bounded away from one). The idea is to ﬁrst consider p > 1 and s > z = − log(1 − ε), and then let p → 1 and s → z. Since Π → 0, using Lemma 8 we have

Ee−sX exp −µ 1 − e−s + o(1) . (20)

So, using Lemma 9 together with δ → 0, we expect that (replacing the diﬀerence quotient by the derivative), as p → 1,

Ee−sX Ee−psX

![image 30](<2014-janson-lower-tail-poisson-approximation_images/imageFile30.png>)

1 p−1

![image 31](<2014-janson-lower-tail-poisson-approximation_images/imageFile31.png>)

exp µs

e−(1+δ)s − e−(1+δ)ps (1 + δ)(p − 1)s

![image 32](<2014-janson-lower-tail-poisson-approximation_images/imageFile32.png>)

= exp µ se−s + o(1) . (21)

The point is that 1−e−s −se−s → ϕ(−ε) as s → z. So, if (20) and (21) essentially determine the right hand side of (19), then our previous considerations suggest

P(X < (1 − ε)EX) exp −µ ϕ(−ε) + o(1) .

Luckily, our later calculations conﬁrm that (for suitable choices of p and s) we can indeed essentially ignore the ﬁrst term on the right hand side of (19) for large deviations, i.e., when ε2µ → ∞ holds.

- 2.3 Proofs of Theorem 2 and 6 Assume that ε,τ ∈ (0,1) and σ ∈ (0,∞). Let


p = 1 + σ and q = 1 + 1/σ, (22) so that p,q ∈ (1,∞) and 1/p + 1/q = 1. Furthermore, let

z = − log(1 − ε) and s = pz. (23) With (19) in mind, the following two lemmas are at the heart of our argument.

- Lemma 13. With deﬁnitions as above, if Π(1 − e−s) 1/2, then Ee−sX

![image 33](<2014-janson-lower-tail-poisson-approximation_images/imageFile33.png>)

Ee−psX

1 p−1

![image 34](<2014-janson-lower-tail-poisson-approximation_images/imageFile34.png>)

Ee−sX e−(1+η)ϕ(−ε)µ, (24)

with η = 2p2(σ + pδ + Π) + 2pσ. Proof. Since f(x) = −e−x satisﬁes f′(x) = e−x, the mean value theorem implies that there is ζ ∈ [1,p] such that

e−(1+δ)s − e−(1+δ)ps (1 + δ)(p − 1)s

![image 35](<2014-janson-lower-tail-poisson-approximation_images/imageFile35.png>)

= e−(1+δ)ζs e−(1+δ)ps. (25)

Furthermore, since g(x) = e−x satisﬁes g′(x) = −e−x and g′′(x) = e−x 0, using Taylor’s theorem with remainder, we obtain

e−(1+δ)ps e−s − (1 + δ)p − 1 se−s. (26) Note that (1 + δ)p − 1 = σ + pδ. Furthermore, since s = −p log(1 − ε), Bernoulli’s inequality yields

(1 − e−s)2 = (1 − (1 − ε)p)2 p2ε2. (27) So, by combining Lemmas 8 and 9 with (25)–(27), using Π(1 − e−s) 1/2, it follows that

Ee−sX Ee−psX

![image 36](<2014-janson-lower-tail-poisson-approximation_images/imageFile36.png>)

1 p−1

![image 37](<2014-janson-lower-tail-poisson-approximation_images/imageFile37.png>)

Ee−sX exp

µs e−(1+δ)s − e−(1+δ)ps

![image 38](<2014-janson-lower-tail-poisson-approximation_images/imageFile38.png>)

(1 + δ)(p − 1)s − µ(1 − e−s) − µΠ(1 − e−s)2 exp −µ 1 − e−s − se−s + σ + pδ s2e−s + Πp2ε2 .

Let g(x) = 1−e−x −xe−x, and note that g(z) = ϕ(−ε). Furthermore, for z x s we have g′(x) = xe−x se−z. So, using Taylor’s theorem with remainder, we deduce that

1 − e−s − se−s ϕ(−ε) + (s − z)se−z. Consequently, since s = pz z, we obtain

Ee−sX Ee−psX

![image 39](<2014-janson-lower-tail-poisson-approximation_images/imageFile39.png>)

1 p−1

![image 40](<2014-janson-lower-tail-poisson-approximation_images/imageFile40.png>)

Ee−sX exp −ϕ(−ε)µ − z2e−zη1 + ε2η2 µ ,

where η1 = p2(σ + pδ) + pσ and η2 = p2Π. Finally, recalling z = − log(1 − ε), the point is that Lemma 10 yields max{z2e−z,ε2} 2ϕ(−ε), yielding the result with η = 2η1 + 2η2.

![image 41](<2014-janson-lower-tail-poisson-approximation_images/imageFile41.png>)

![image 42](<2014-janson-lower-tail-poisson-approximation_images/imageFile42.png>)

![image 43](<2014-janson-lower-tail-poisson-approximation_images/imageFile43.png>)

![image 44](<2014-janson-lower-tail-poisson-approximation_images/imageFile44.png>)

- Lemma 14. With deﬁnitions as above, if λ = Π(1−e−s) < 1 and (1−τ)σ2(1−ε)p p2Π/(1−λ)+δ/(1+δ), then


p p−1

![image 45](<2014-janson-lower-tail-poisson-approximation_images/imageFile45.png>)

E(e−sX {X<(1−ε)EX}) Ee−sX

4p τσ3(1 − ε)pε4µ2

exp −

ϕ(−ε)µ . (28)

![image 46](<2014-janson-lower-tail-poisson-approximation_images/imageFile46.png>)

![image 47](<2014-janson-lower-tail-poisson-approximation_images/imageFile47.png>)

Proof. As p = 1 + σ, we write

E(e−sX {X<(1−ε)µ}) Ee−sX

![image 48](<2014-janson-lower-tail-poisson-approximation_images/imageFile48.png>)

p p−1

![image 49](<2014-janson-lower-tail-poisson-approximation_images/imageFile49.png>)

E(e−sX {X (1−ε)µ}) Ee−sX

= 1 −

![image 50](<2014-janson-lower-tail-poisson-approximation_images/imageFile50.png>)

p σ

![image 51](<2014-janson-lower-tail-poisson-approximation_images/imageFile51.png>)

. (29)

Let t = z/(1 + δ). Recalling ϕ(−ε) = (1 − ε)log(1 − ε) + ε, note that

ϕ(−ε)µ 1 + δ

µ 1 + δ

1 − e−(1+δ)t = −

t(1 − ε)µ −

.

![image 52](<2014-janson-lower-tail-poisson-approximation_images/imageFile52.png>)

![image 53](<2014-janson-lower-tail-poisson-approximation_images/imageFile53.png>)

So, using t s and Lemma 9 (with r = 0), it follows that

ϕ(−ε)µ 1 + δ

E(e−sX {X (1−ε)µ}) e−(s−t)(1−ε)µ · Ee−tX exp −s(1 − ε)µ −

![image 54](<2014-janson-lower-tail-poisson-approximation_images/imageFile54.png>)

. (30)

Set h(x) = (1 − ε)x − (1 − e−x), and note that h(z) = −ϕ(−ε) and h′(z) = 0. Furthermore, for x s we have h′′(x) = e−x e−s. So, using Taylor’s theorem with remainder, we obtain

(1 − ε)s − (1 − e−s) −ϕ(−ε) + (s − z)2e−s/2. (31)

Recalling p = 1 +σ, s = pz and λ = Π(1 −e−s), by combining Lemma 8 with (30), (31) and (1 − e−s)2 s2, we infer

E(e−sX {X (1−ε)µ}) Ee−sX

Πs2 2(1 − λ) exp −µ

ϕ(−ε) 1 + δ −

exp −µ (1 − ε)s − (1 − e−s) +

![image 55](<2014-janson-lower-tail-poisson-approximation_images/imageFile55.png>)

![image 56](<2014-janson-lower-tail-poisson-approximation_images/imageFile56.png>)

![image 57](<2014-janson-lower-tail-poisson-approximation_images/imageFile57.png>)

σ2(1 − ε)pz2 2 −

Πp2z2 2(1 − λ) −

δϕ(−ε) 1 + δ

.

![image 58](<2014-janson-lower-tail-poisson-approximation_images/imageFile58.png>)

![image 59](<2014-janson-lower-tail-poisson-approximation_images/imageFile59.png>)

![image 60](<2014-janson-lower-tail-poisson-approximation_images/imageFile60.png>)

Since Lemma 10 gives ϕ(−ε) log2(1 − ε)/2 = z2/2, we have, by assumption, E(e−sX {X (1−ε)µ}) Ee−sX

exp −τσ2(1 − ε)pz2µ/2 . (32)

![image 61](<2014-janson-lower-tail-poisson-approximation_images/imageFile61.png>)

Now, inserting (32) into (29), using the fact that e−x + e−1/x 1 for x > 0 (as in the proof of Theorem 2 in [13]), we obtain

p p−1

![image 62](<2014-janson-lower-tail-poisson-approximation_images/imageFile62.png>)

E(e−sX {X<(1−ε)µ}) Ee−sX

2p τσ3(1 − ε)pz2µ

exp −

.

![image 63](<2014-janson-lower-tail-poisson-approximation_images/imageFile63.png>)

![image 64](<2014-janson-lower-tail-poisson-approximation_images/imageFile64.png>)

Finally, recalling z = − log(1 − ε), Lemma 10 yields z2 ε2 and 1 2ϕ(−ε)/ε2.

![image 65](<2014-janson-lower-tail-poisson-approximation_images/imageFile65.png>)

![image 66](<2014-janson-lower-tail-poisson-approximation_images/imageFile66.png>)

![image 67](<2014-janson-lower-tail-poisson-approximation_images/imageFile67.png>)

![image 68](<2014-janson-lower-tail-poisson-approximation_images/imageFile68.png>)

Combining (19) with Lemma 13 and 14, the proofs of Theorem 2 and 6 reduce to deﬁning suitable parameters σ and τ (our choices are somewhat ad-hoc, and yield fairly transparent error-terms). Proof of Theorem 6. With foresight, let τ = 5/8 and

σ = max Π1/4,δ1/4,[e(1 − ε)ε2µ]−1/2 . (33)

Note that the assumption 0 ε 1 − 4 max{Π1/4,δ1/4} implies max{Π,δ} 4−4, so that λ = Π(1 − e−s) Π 1/5. Hence, using e(1 − ε)ε2µ 1, we see that σ 1 and thus p 2. Consequently, by (33), we have

σ4(1 − ε)pε4µ2 σ4(1 − ε)2ε4µ2 e−2 (34)

and σ2 max{Π1/2,δ1/2}. In addition, by assumption, we have (1 − ε)p (1 − ε)2 16 max{Π1/2,δ1/2}. Since 16(1 − τ) = 6 and p2/(1 − λ) 5, it follows that

(1 − τ)σ2(1 − ε)p 6 max{Π,δ} p2Π/(1 − λ) + δ/(1 + δ). Now, combining (19) with Lemmas 13–14 and (34), we obtain

P(X < (1 − ε)µ) e−(1+κ)ϕ(−ε)µ,

with κ = 2p2(σ + pδ + Π) + 2pσ + 4e2τ−1pσ. Finally, using σ σ4 max{δ,Π}, p 2 and τ = 5/8, we see that κ 135σ.

![image 69](<2014-janson-lower-tail-poisson-approximation_images/imageFile69.png>)

![image 70](<2014-janson-lower-tail-poisson-approximation_images/imageFile70.png>)

![image 71](<2014-janson-lower-tail-poisson-approximation_images/imageFile71.png>)

![image 72](<2014-janson-lower-tail-poisson-approximation_images/imageFile72.png>)

Proof of Theorem 2. Let τ = (1 − Π)/5, so that, by assumption, τ ∈ (0,1/5]. The proof distinguishes two cases, which eventually establish (5) by noting that Lemma 10 gives ϕ(−ε) ε2.

First, we assume 0 ε < τ2/2. Note that then, by assumption, we have 0 < ε < 1/50 and δ = δ∗. Let p = 2/τ and σ = p − 1. Analogous to (27) we have 1 − e−s = 1 − (1 − ε)p pε, so that Π 1 implies

λ = Π(1 − e−s) Πpε τ,

which in particular yields λ 1/2, with room to spare. Next observe that, since σ/p = 1 − 1/p and max{2/p,pε,λ} = τ, by the deﬁnition of τ we have

(1 − τ)σ2(1 − ε)p(1 − λ) p2 −

1 p2

(1 − τ)(1 − 2/p)(1 − pε)(1 − λ) − τ2/4 (1 − τ)4 − τ2/4 1 − 5τ = Π,

![image 73](<2014-janson-lower-tail-poisson-approximation_images/imageFile73.png>)

![image 74](<2014-janson-lower-tail-poisson-approximation_images/imageFile74.png>)

which in turn readily yields (1 − τ)σ2(1 − ε)p p2Π/(1 − λ) + δ/(1 + δ). Similarly, using σ p/2 = τ−1 and τ 1/2 we obtain

τσ3(1 − ε)p τ−2(1 − τ) τ−2/2.

Since ε4µ2 (1 + δ)−1 by assumption, analogously to the proof of Theorem 6, using (19) together with Lemmas 13–14, we obtain

P(X (1 − ε)µ) P(X < (1 − ε)µ) e−(1+κ)ϕ(−ε)µ,

with κ = 2p2(σ + pδ + Π) + 2pσ + 8τ2p(1 + δ). Now, using max{Π,τ} 1 and σ p = 2/τ = 10/(1 − Π), a short calculation shows that, say,

1 + κ 17 + 2p3 + 4p2 + (2p3 + 16)δ 2500(1 + δ)/(1 − Π)3.

Finally, we assume τ2/2 ε 1. Using the lower bound (3) resulting from Harris’ inequality [12], it follows that

P(X (1 − ε)µ) P(X = 0) e−µ/(1−Π). (35) The point is that, by assumption, we have 2/ε2 8/τ4 = 5000/(1 − Π)4, so that Lemma 10 implies

- 1 5000ϕ(−ε)/(1 − Π)4.


![image 75](<2014-janson-lower-tail-poisson-approximation_images/imageFile75.png>)

![image 76](<2014-janson-lower-tail-poisson-approximation_images/imageFile76.png>)

![image 77](<2014-janson-lower-tail-poisson-approximation_images/imageFile77.png>)

![image 78](<2014-janson-lower-tail-poisson-approximation_images/imageFile78.png>)

- 2.4 Proofs of Theorem 1 and Lemma 7 The remaining proofs of Theorem 1 and Lemma 7 are straightforward. Proof of Lemma 7. Note that, by assumption, 5√1 − ε 5e−1/2 4. So, using Lemma 11, we infer


![image 79](<2014-janson-lower-tail-poisson-approximation_images/imageFile79.png>)

1/(1 − Π) (1 + 5√1 − ε) 1 + Π/(1 − Π) ϕ(−ε) (1 + ζ)ϕ(−ε), with ζ = 10 max{

![image 80](<2014-janson-lower-tail-poisson-approximation_images/imageFile80.png>)

√1 − ε,Π/(1−Π)}. Now an application of (3), analogous to (35), completes the proof. Proof of Theorem 1. Note that, using the assumption,

![image 81](<2014-janson-lower-tail-poisson-approximation_images/imageFile81.png>)

![image 82](<2014-janson-lower-tail-poisson-approximation_images/imageFile82.png>)

![image 83](<2014-janson-lower-tail-poisson-approximation_images/imageFile83.png>)

![image 84](<2014-janson-lower-tail-poisson-approximation_images/imageFile84.png>)

![image 85](<2014-janson-lower-tail-poisson-approximation_images/imageFile85.png>)

η = max{4Π1/4, {ε<1}4δ1/4, {ε<1}e−1(ε2µ)−1/2}

satisﬁes η ∈ [0,e−1]. If 1 − η ε 1, then ε 1 − e−1 and 1 − ε η, so that Lemma 7 implies (4). If 0 ε < 1 − η, then e(1 − ε)ε2µ eηε2µ (ε2µ)1/2 1 and ε 1 − 4 max{Π1/4,δ1/4}, so that Theorem 6 establishes (4).

![image 86](<2014-janson-lower-tail-poisson-approximation_images/imageFile86.png>)

![image 87](<2014-janson-lower-tail-poisson-approximation_images/imageFile87.png>)

![image 88](<2014-janson-lower-tail-poisson-approximation_images/imageFile88.png>)

![image 89](<2014-janson-lower-tail-poisson-approximation_images/imageFile89.png>)

# 3 Bootstrapping lower bounds for the lower tail

As discussed, Theorem 1 and 2 only give reasonable lower bounds for the lower tail if δ = O(1), i.e., as long as the dependencies are ‘weak’. In this section we present a bootstrapping strategy, which often allows us to deal with the remaining case, where δ = Ω(1) holds.

In order to establish a competent lower bound on the lower tail, we usually need to (approximately) identify the most likely way to obtain X (1 − ε)EX. At ﬁrst glance it seems that this would require fairly detailed information about the random variable X, where µ = EX. However, in the general setting of this paper, we discovered that, perhaps surprisingly, we can systematically guess suitable (nearly) ‘extremal’ events by only inspecting the form of the variance VarX Λ = Λ(X). Indeed, assume that there is a random variable Y , of the same type as (1), satisfying

Λ = Θ(µ2/EY ) and δ(Y ) = O(1). (36)

For example, if XH counts the number of copies of a given graph H in Gn,p, then (36) holds for X = XH with Y = XG, where G ⊆ H is a suitable subgraph (see [15, 16] or Lemma 22). Deﬁning E as the event that

- Y (1 − ε)EY holds, our starting point is the basic inequality P(X (1 − ε)EX) P(X (1 − ε)EX | E)P(E). (37)


Assuming that Theorem 1 or 2 applies to Y , using (36) there are constants c1,c2 > 0 such that P(E) e−c

2ϕ(−ε)µ2/Λ. (38)

1ϕ(−ε)EY e−c

Hence it remains to estimate P(X (1 − ε)EX | E) from below. It turns out that if X and Y are suitably related (as in the subgraphs example), then under fairly mild conditions we can prove that E(X | E) is quite

- a bit smaller than (1 − ε)EX. In other words, by conditioning on E we intuitively ‘convert’ the rare event X (1 − ε)EX into a typical one (this subtle conditioning idea is at the heart of our approach). With this in mind it seems plausible that we have, say,


P(X (1 − ε)EX | E) = Ω(1), (39) although e−c

3ϕ(−ε)µ2/Λ suﬃces for our purposes. Note that for the special case ε = 1 this inequality is immediate in the subgraphs example (where XG = 0 implies XH = 0). Finally, by combining (37)–(39) we obtain

2ϕ(−ε)µ2/Λ)), (40) which qualitatively matches the upper bound of (2), as desired.

P(X (1 − ε)EX) = Ω(e−c

To implement this proof strategy, we need to be able to verify that (39) holds (or a related inequality). Here the main technical challenge is that, after conditioning on E, the i ∈ Γ are no longer added independently to Γp. In Sections 3.1–3.3 we present three approaches that, in symmetric situations, allow us to routinely overcome this diﬃculty (each of them hinges on an event that is similar to E). Since we are interested in large deviations (with exponentially small probabilities), here (εµ)2 = Ω(Λ) is a natural condition in view of (2), (40) and the fact ϕ(−ε) = Θ(ε2).

- 3.1 Binomial random subset


The ﬁrst approach is motivated by the following simple observation: if |Γp| = 0, then deterministically X = 0. Indeed, this yields

P(X (1 − ε)EX) P(X = 0) P(|Γp| = 0),

which for ε = Θ(1) may give a fair lower bound. The next theorem, for the case of equal pi, is based on the following heuristic extension of this observation: if |Γp| is ‘too small’, then we expect that X is typically also ‘too small’. As we shall see, the crux is that conditioning on |Γp| (1−ε)E|Γp| decreases the expected value of X, which intuitively increases the probability that X (1 − ε)EX occurs. Note that E(X | |Γp| = 0) = 0 conﬁrms this phenomenon in the special case ε = 1.

Theorem 15. Let X = α∈X Iα, µ = EX and Λ be deﬁned as in Section 1. Suppose that p = (p,...,p) ∈ [0,1]N and minα∈X |Q(α)| 2. For all ε ∈ (0,1] satisfying (εµ)2 {ε<1}Λ, with c = 1/2 + {ε=1}1/2,

P(X (1 − ε)EX) cP(|Γp| (1 − ε)E|Γp|). (41)

In the proof of Theorem 15 we use the following one-sided version of Chebyshev’s inequality (see, e.g., Theorem A.17 in [9]). Claim 16. If VarZ v, then P(Z EZ + t) v/(v + t2) for all t > 0. Proof of Theorem 15. Given 0 j N, we write P(· | |Γp| = j) = Pj(·) for brevity. Note that for

- m = (1 − ε)Np = (1 − ε)E|Γp| we have


P(X (1 − ε)µ)

Pj(X (1 − ε)µ)P(|Γp| = j)

0 j m

P(|Γp| m) min

Pj(X (1 − ε)µ).

0 j m

(42)

Since P0(X (1 − ε)µ) P0(X = 0) = 1, we henceforth may assume m 1. Consequently ε < 1 and p > 0 hold, so that µ minα∈X EIα pN > 0.

In the following we estimate the conditional expected value and variance of X. Given 0 j m, we write E(· | |Γp| = j) = Ej(·) and Var(· | |Γp| = j) = Varj(·) for brevity. Let Γj ⊆ Γ with |Γj| = j be chosen uniformly at random. Since p = (p,...,p), it follows that Γp conditioned on |Γp| = j has the same distribution as Γj. As |Q(α)| 2 and j m N, using Iα = {Q(α)⊆Γ

p} we infer

N−|Q(α)| j−|Q(α)| N

j − i N − i j

= {|Q(α)| j}

Ej(Iα) = {|Q(α)| j}

![image 90](<2014-janson-lower-tail-poisson-approximation_images/imageFile90.png>)

![image 91](<2014-janson-lower-tail-poisson-approximation_images/imageFile91.png>)

(43)

j

0 i<|α|

|Q(α)|

(1 − ε)|Q(α)|p|Q(α)| (1 − ε)2EIα.

![image 92](<2014-janson-lower-tail-poisson-approximation_images/imageFile92.png>)

N

p}, we analogously obtain Ej(IαIβ) (1 − ε)2E(IαIβ). Furthermore, if Q(α) ∩ Q(β) = ∅ and |Q(α)| + |Q(β)| j, then a similar calculation shows that

Since IαIβ = {Q(α)∪Q(β)⊆Γ

N−|Q(β)|−|Q(α)| j−|Q(β)|−|Q(α)| N−|Q(β)| j−|Q(β)|

j − |Q(β)| − i N − |Q(β)| − i

Ej(Iα | Iβ = 1) =

Ej(Iα).

=

![image 93](<2014-janson-lower-tail-poisson-approximation_images/imageFile93.png>)

![image 94](<2014-janson-lower-tail-poisson-approximation_images/imageFile94.png>)

0 i<|Q(α)|

If |Q(α) ∪ Q(β)| > j then, trivially, Ej(IαIβ) = 0. It follows that Q(α) ∩ Q(β) = ∅ implies Ej(IαIβ) − Ej(Iα)Ej(Iβ) 0. Combining our ﬁndings, we deduce that

Ej(X) (1 − ε)2µ and max

max

0 j m

0 j m

Varj(X) (1 − ε)2Λ. (44)

Finally, using (44) and the one-sided Chebyshev’s inequality (Claim 16) we infer that for every 0 j m we have

Pj(X > (1 − ε)µ) Pj(X Ej(X) + (1 − ε)εµ) Λ/(Λ + (εµ)2), which together with (εµ)2 Λ and (42) establishes (41).

![image 95](<2014-janson-lower-tail-poisson-approximation_images/imageFile95.png>)

![image 96](<2014-janson-lower-tail-poisson-approximation_images/imageFile96.png>)

![image 97](<2014-janson-lower-tail-poisson-approximation_images/imageFile97.png>)

![image 98](<2014-janson-lower-tail-poisson-approximation_images/imageFile98.png>)

The proof shows that (41) holds with c replaced by 1 − {ε<1,µ>0}Λ/(Λ + (εµ)2), and that the left hand side of (41) can be strengthened to P(X < (1 − ε)EX) whenever ε ∈ (0,1) and µ > 0 (we henceforth omit analogous remarks).

In applications where constant factors in the exponent are important, the following variant of Theorem 15 usually gives better results when ε → 0 and L = (εµ)2/Λ → ∞ (by setting τ = 6 max{ε,L−1/2}; see Lemma 12 with A = (1 + τ)/k).

- Theorem 17. Let X = α∈X Iα, µ = EX and Λ be deﬁned as in Section 1. Suppose that p = (p,...,p) ∈ [0,1]N and minα∈X |Q(α)| k 1. For all ε,τ ∈ (0,1] satisfying τ {k>1}6ε and (εµ)2 4τ−2Λ, with c = 1/2,


P(X (1 − ε)EX) cP(|Γp| (1 − (1 + τ)ε/k)E|Γp|). (45) Proof. Let λ = (1 + τ)ε/k and m = (1 − λ)E|Γp|. As (45) is trivial otherwise, we henceforth assume

- P(|Γp| m) > 0, which implies m 0. Now, (42) carries over mutatis mutandis, and, with similar reasoning as in the proof of Theorem 15, we may henceforth assume min{m,p,µ} > 0. Furthermore, as minα∈X |Q(α)| k, the calculations leading to (44) imply


Ej(X) (1 − λ)kµ and max

max

Varj(X) Λ. (46)

0 j m

0 j m

If k = 1, then (1 − ε) − (1 − λ)k = λ − ε = τε, and we now establish a similar bound for k > 1. Note that λk = (1 + τ)ε 2ε τ/3 < 1 and

(1 − λ)k e−λk 1 − λk +

j 2

(λk)j j!

![image 99](<2014-janson-lower-tail-poisson-approximation_images/imageFile99.png>)

(λk)2 2(1 − λk)

1 − λk +

.

![image 100](<2014-janson-lower-tail-poisson-approximation_images/imageFile100.png>)

Recalling λk = (1 + τ)ε, ε τ/6 and τ 1, a short calculation shows that

(1 + τ)2ε 2τ(1 − (1 + τ)ε)

(1 − ε) − (1 − λ)k τε 1 −

τε/2.

![image 101](<2014-janson-lower-tail-poisson-approximation_images/imageFile101.png>)

Consequently, using (46) and the one-sided Chebyshev’s inequality (Claim 16), we infer that for every 0 j m we have

Pj(X > (1 − ε)µ) Pj(X Ej(X) + τεµ/2) Λ/(Λ + τ2(εµ)2/4), which together with (εµ)2 4τ−2Λ and (42) establishes (45).

![image 102](<2014-janson-lower-tail-poisson-approximation_images/imageFile102.png>)

![image 103](<2014-janson-lower-tail-poisson-approximation_images/imageFile103.png>)

![image 104](<2014-janson-lower-tail-poisson-approximation_images/imageFile104.png>)

![image 105](<2014-janson-lower-tail-poisson-approximation_images/imageFile105.png>)

- 3.2 Symmetric decomposition


In general, the conditional expected value of X is diﬃcult to compute (as we do not have explicit formulas as in (43)). Our second approach shows that we can overcome this obstacle using a symmetric decomposition of X. As an illustration, we again consider the number of copies of H in Gn,p. Clearly, for every G ⊆ H we have P(XH = 0) P(XG = 0). The basic idea is now that, by counting the number of H-copies extending each copy of G, we ought to be able to argue as follows: if XG is ‘too small’, then the (conditional) expected value of XH is also ‘too small’. To avoid clutter, we henceforth use the abbreviation

Iα\β = {Q(α)\Q(β)⊆Γ

p}. (47) Let H = Hn contain all subgraphs isomorphic to H in Kn, and deﬁne Q(α) = E(α) for all α ∈ H (here

- Q(α) = α is crucial to allow for isolated vertices in H). The key observation is that, by symmetry, there is a constant w > 0 such that we may write


XH = w

Iβ

β∈G

Iα\β,

α∈H:β⊆α

where E α∈H:β⊆α Iα\β is independent of the choice of β ∈ G. The point is that, since E(IβIα\β) = EIβEIα\β and XG = β∈G Iβ, this allows us to factorize EXH in terms of EXG. Indeed, for any β˜ ∈ G we have

Iα\β˜ .

EIβ = wEXGE

EXH = wE

Iα\β˜

α∈H:β˜⊆α

α∈H:β˜⊆α

β∈G

Intuitively, our approach exploits that correlation inequalities can be used to obtain a similar factorization of the conditional expected value of XH.

With the subgraphs example in mind, the following theorem should be interpreted under the premise that the lower bound is exponentially small in Θ((εµ)2/Λ). In other words, the multiplicative γε errorterm ought to be negligible as long as, say, γε e−(εµ)

2/Λ holds. The crux is that this inequality is equivalent to (εµ)2/Λ log 1/(γε) , which matches our usual condition up to the logarithmic factor. On ﬁrst reading it might be useful to consider the important special case exempliﬁed above, where wα,β = w > 0, X(β) = {α ∈ X : Q(β) ⊆ Q(α)} and κ = 0.

- Theorem 18. Let Y = β∈Y Iβ, where Q(β) β∈Y is a family of subsets of Γ. Suppose that there are wα,β ∈


[0,∞) and families Q(α) α∈X(β) of subsets of Γ such that X = β∈Y IβXβ, where Xβ = α∈X(β) wα,βIα\β satisﬁes maxβ∈Y EXβ (1 + κ)minβ∈Y EXβ for κ ∈ [0,∞). For all ε ∈ [0,1] and γ ∈ [0,∞) satisfying γε 2κ and {EY=0}γε 2, with c = 1/2,

P(X (1 − ε)EX) cγεP(Y (1 − (1 + γ)ε)EY ). (48) If ε ր 1 or ε = 1 holds, then, by applying Lemma 7 to Y , we often can improve (48) via

P(X (1 − ε)EX) P(X = 0) P(Y = 0). (49)

The proof of Theorem 18 hinges on the following simple consequence of Harris’ inequality [12], which was observed by Bollob´s and Riordan (see Lemma 6 in [4]).

Claim 19. For the probability space induced by Γp, suppose that D is a decreasing event with P(D) > 0, and that I1 and I2 are increasing events with P(I1 ∩ I2) = P(I1)P(I2). Then

P(I1 ∩ I2 | D) P(I1)P(I2 | D). (50)

Proof of Theorem 18. Let y = (1 − (1 + γ)ε)EY and µ = EX. As (48) is trivial otherwise, we henceforth assume γε > 0 and P(Y y) > 0, which since Y 0 implies y 0. If EY = 0, then P(Y = 0) = P(Y y), and, since we then assume 1 γε/2, (49) establishes (48). Henceforth we thus assume EY > 0, so that y 0 implies 1 (1 + γ)ε > max{ε,γε}. Note that

P(X (1 − ε)µ) P(Y y)P(X (1 − ε)µ | Y y). (51) Since E(IβIα\β) = EIβEIα\β, using the deﬁnitions of X, Xβ and Y we deduce

µ = EX =

EXβ (1 + κ)−1EY max β∈Y

EIβEXβ EY min β∈Y

EXβ. (52)

β∈Y

We write Iα and Iα\β for the increasing events that Iα = 1 and Iα\β = 1, respectively. Hence P(Iα\βIβ) = P(Iα\β)P(Iβ). Clearly, Y y is a decreasing event. Using Claim 19 together with (52) and (1−(1+γ)ε)(1+ κ) 1 − (1 + γ/2)ε, it follows that

wα,βP(Iα\βIβ | Y y)

E(X | Y y) =

β∈Y α∈X(β)

P(Iβ | Y y)

β∈Y

α∈X(β)

E(Y | Y y)max

EXβ (1 − (1 + γ/2)ε)µ.

EXβ y max β∈Y

β∈Y

wα,βP(Iα\β)

(53)

Let λ = 1 + γ/2. If µ > 0, then, using Markov’s inequality, we infer from (53)

1 − λε 1 − ε

(λ − 1)ε 1 − ε

P(X > (1 − ε)µ | Y y)

= 1 −

1 − γε/2, (54)

![image 106](<2014-janson-lower-tail-poisson-approximation_images/imageFile106.png>)

![image 107](<2014-janson-lower-tail-poisson-approximation_images/imageFile107.png>)

which together with (51) establishes (48). Finally, if µ = 0, then P(X > 0) = 0 and (48) follows trivially from the fact 1 > γε established above.

![image 108](<2014-janson-lower-tail-poisson-approximation_images/imageFile108.png>)

![image 109](<2014-janson-lower-tail-poisson-approximation_images/imageFile109.png>)

![image 110](<2014-janson-lower-tail-poisson-approximation_images/imageFile110.png>)

![image 111](<2014-janson-lower-tail-poisson-approximation_images/imageFile111.png>)

It would be desirable to use Chebyshev’s inequality in (54), since this presumably would improve the seemingly suboptimal γε term. Here one technical obstacle is that Claim 19 can, in general, not be strengthened to

P(I1 ∩ I2 | D) P(I1 | D)P(I2 | D). (55) Indeed, a short calculation shows that, for Γ = [n] = {1,...,n} and p = (p,...,p) with n 3 and p ∈ (0,1), the events Ii = {i ∈ Γp} and D = {|Γp| 1 or Γp = {1,2}} provide a counterexample (where, moreover, equality holds in (50)). It would be interesting to know whether there is perhaps some approximate version of (55) that suﬃces for our purposes.

The existence of a symmetric decomposition may not always be obvious. We hope that the following two examples from additive combinatorics serve as inspiration for future applications of Theorem 18 (or its method of proof). In both we consider p = (p,...,p) and Q(α) = α, and the basic idea is to ‘symmetrize’ X using non-uniform ‘weights’ wα,β (and κ = 0). In the ﬁrst example, we let X contain all arithmetic progressions of length k 2 in Γ = [n], i.e., each α ∈ X equals {b,b + d,...,b + (k − 1)d} ⊆ [n] for some

- b = bα and d = dα with bα,dα 1. For every β ∈ Y = [n] we deﬁne X(β) as the set of α ∈ X where β = bα or β = bα + (k − 1)dα, and set wα,β = 1/2. Since each α ∈ X contributes to exactly two Xβ, we have X = β∈Y IβXβ. Furthermore, careful counting yields


n − β k − 1

β − 1 k − 1

n 2(k − 1)

- 1

![image 112](<2014-janson-lower-tail-poisson-approximation_images/imageFile112.png>)

- 2


pk−1 =

+ O(1) pk−1,

+

EXβ =

![image 113](<2014-janson-lower-tail-poisson-approximation_images/imageFile113.png>)

![image 114](<2014-janson-lower-tail-poisson-approximation_images/imageFile114.png>)

![image 115](<2014-janson-lower-tail-poisson-approximation_images/imageFile115.png>)

so κ = O(1/n) suﬃces. In the second example, we let X contain all Schur triples in Γ = [n], i.e., each α ∈ X equals {x,y,x + y} ⊆ [n] for some x = xα and y = yα with 1 xα < yα. For every β ∈ Y = [n] we deﬁne

X(β) as the set of all α ∈ X with β ∈ α. We set wα,β = 1/2 if β = xα + yα, and wα,β = 1/4 otherwise. By counting triples, it is not hard to see that X = β∈Y IβXβ and

EXβ =

- 1

![image 116](<2014-janson-lower-tail-poisson-approximation_images/imageFile116.png>)

- 2


β − 1 2

![image 117](<2014-janson-lower-tail-poisson-approximation_images/imageFile117.png>)

max{n − 2β,0} + min{n − β,β − 1} 4

+

![image 118](<2014-janson-lower-tail-poisson-approximation_images/imageFile118.png>)

p2 =

n 4

+ O(1) p2,

![image 119](<2014-janson-lower-tail-poisson-approximation_images/imageFile119.png>)

so κ = O(1/n) suﬃces. Finally, in both examples routine calculations (analogous to Example 3.2 in [16]) give µ2/Λ = Θ(min{µ,np}). Since κ = O(1/n) and µ2/Λ = O(np), the natural condition (εµ)2 = Ω(Λ) thus implies κ/ε = O(1/n · µ2/Λ) = O( p/n) = o(1). In other words, the assumption γε 2κ in Theorem 18 is very mild, i.e., allows for γ = o(1).

![image 120](<2014-janson-lower-tail-poisson-approximation_images/imageFile120.png>)

![image 121](<2014-janson-lower-tail-poisson-approximation_images/imageFile121.png>)

- 3.3 Vertex symmetry


In many applications the set Γ has additional structure, and here our main focus is on the case where Γ contains the edges of some hypergraph. Intuitively, ‘seeing’ the underlying vertices introduces quite a bit of extra symmetry, and our third approach exploits this to step aside the conditioning issue we faced in the previous subsection. As an illustration, we consider, as before, the number of copies of H in Gn,p. The basic idea is to partition the vertex set into U and [n] \ U with |U| ≈ n/2, and then, for suitable G ⊆ H, to focus on the number of copies of G completely contained in U, which we denote by YG. Note that EYG = Θ(EXG). Perhaps rashly, we would like to argue that YG (1 − ε)EYG typically entails XH (1 − ε)EXH. However, this is overly ambitious: since YG is somewhat ‘local’, we loose a bit when going to the ‘global’ random variable XH, and thus we need a slightly larger deviation of YG. Instead of counting all copies of H, a technical reduction allows us to focus on the number of pairs (H′,G′) of copies of H and G with G′ ⊆ H′, V (G′) ⊆ U and V (H′) \ V (G′) ⊆ [n] \ U. Now, to make variance calculations feasible (i.e., to overcome the obstacle that (55) may fail), we do not condition on YG, but rather on all edges with both endvertices in U (satisfying additional typical properties). For technical reasons, here our argument requires that all edges in the relevant graphs H′ \ G′ have at least one endvertex outside of U, which, e.g., holds if all copies of G in H are induced subgraphs. Luckily, it is not hard to check (see Lemma 22) that the former condition always holds for some G ⊆ H that determines the exponent, i.e., satisﬁes Λ(XH) = Θ((EXH)2/EXG).

In the statement of the next theorem we restrict ourselves to subgraph counts in random hypergraphs. The approach works in a more general setting, but we resist the temptation of stating a very technical theorem (that would be diﬃcult to apply). Instead, we tried to write the proof in a way that hopefully makes the basic setup and symmetry assumptions fairly transparent. In Theorem 20 the diﬀerence between YG and XG is usually irrelevant in applications where constant factors in the exponent are immaterial: the point is that Gn,p(k)[U] has the same distribution as G(nk′),p with n′ = |U| ≈ n/2. In comparison with Theorem 18, the key feature of Theorem 20 is that the natural condition (εEXH)2 = Ω(Λ(XH)) suﬃces.

- Theorem 20. Let G ⊆ H be k-graphs with eG 1, where every copy of G in H is induced. Let XH be the number of copies of H in G(n,pk), and let YG be the number of copies of G in G(n,pk)[U], where U ⊆ [n] satisﬁes


|U| − n/2 ℓ. For all n n0 = n0(H,ℓ), p ∈ [0,1] and ε ∈ (0,1] satisfying (εEXH)2 Λ(XH), with λ = 2v

v2

H+3 and c = 2−(4

G+2),

P(XH (1 − ε)EXH) cP(YG (1 − λε)EYG). (56)

Proof. Let µ = EXH, Λ = Λ(XH), Γ = E(Kn(k)) and p = (p,...,p), so that Γp = E(G(n,pk)). Let H and G contain all subgraphs isomorphic to H and G in Kn(k), respectively. Deﬁne Q(σ) = E(σ) for σ ∈ H ∪ G. For brevity we henceforth use I(α

1∪σ2 = {Q(σ

1)∪Q(α2)]\[Q(β1)∪Q(β2)]⊆Γp} and Iσ

1∪α2)\(β1∪β2) = {[Q(α

1)∪Q(σ2)⊆Γp} analogous to (47). Set Z = (α,β)∈H×G {β⊆α}Iα. By symmetry, we have β∈G {β⊆α} = τ = τ(H,G) 1 for all α ∈ H. Hence Z = τX, EZ = τEXH, VarZ = τ2 VarXH and

P(XH (1 − ε)EXH) = P(Z (1 − ε)EZ). (57) With foresight, we set ZS = (α,β)∈H×G {α∈H(S,β) and β∈G(S)}Iα for all S ⊆ [n], where

H(S,β) = {α ∈ H : β ⊆ α and V (α) \ V (β) ⊆ [n] \ S}, G(S) = {β ∈ G : V (β) ⊆ S}.

Deﬁne RU = Z − ZU, z = (1 − ελ/2)EZU and r = (1 − ε)EZ − z. Using Z = RU + ZU and Harris’ inequality, it follows that

P(Z (1 − ε)EZ) P(RU r and ZU z) P(RU r)P(ZU z). (58)

The remainder of the proof is devoted to the following two inequalities, which together with (57), (58) and (εµ)2 Λ imply (56):

P(RU r) 1 − {µ>0}Λ/(Λ + (εµ)2), (59) P(ZU z) 1 − {µ>0}Λ/(Λ + 2(εµ)2) 4cP(YG (1 − λε)EYG). (60)

We note ﬁrst that in the trivial case µ = 0, almost surely X = 0 and thus Z = 0 which implies RU = ZU = 0; hence also z = 0 and r = 0 so that (59)–(60) follow trivially. We may thus assume µ > 0.

We next estimate EZU. Let X ⊆ [n] with |X| = |U| be chosen uniformly at random, and independent of Γp. With the deﬁnitions of H(·,β) and G(·) in mind, using linearity of expectation we deduce

E(ZX | Γp) =

(α,β)∈H×G

{β⊆α}P(V (β) ⊆ X and V (α) \ V (β) ⊆ [n] \ X)Iα, (61)

where the measure P is with respect to the (random) choice of X. Note that, whenever β ⊆ α, we have

n−vH |U|−vG n |U|

σα,β = P(V (β) ⊆ X and V (α) \ V (β) ⊆ [n] \ X) =

.

![image 122](<2014-janson-lower-tail-poisson-approximation_images/imageFile122.png>)

Recall that |U| − n/2 ℓ. For ﬁxed ℓ, vG and vH a short calculation shows that σα,β → 2−v

as

H

H+1) = 4λ−1 for n n0(H,ℓ). Using (61) and the deﬁnition of Z we infer E(ZX | Γp) 4λ−1Z, so that E(ZX) 4λ−1EZ. By deﬁnition, we have E(ZX | X = S) = EZS for all S ⊆ [n] with |S| = |U|. Since EZS = EZU by symmetry, we infer EZX = EZU, so that

- n → ∞, so that σα,β 2−(v


EZU 4λ−1EZ. (62)

Turning to (59), note that RU is a restriction of Z to a subset of all pairs (α,β) ∈ H × G. As Harris’ inequality implies E(Iα

, it follows that VarRU VarZ = τ2 VarXH τ2Λ. Recalling ERU = EZ−EZU and the deﬁnitions of r and z, using (62) we have r−ERU = (ελ/2)EZU−εEZ εEZ = τεµ. So, if µ > 0, then the one-sided Chebyshev’s inequality (Claim 16) yields

EIα

) EIα

Iα

2

1

2

1

P(RU > r) P(RU ERU + τεµ) τ2Λ/(τ2Λ + (τεµ)2) = Λ/(Λ + (εµ)2).

In the remainder we focus on (60). Observing that YG = β∈G(U) Iβ, we denote by E the event that YG (1−λε)EYG holds. With foresight, we deﬁne Xβ = α∈H(U,β) Iα\β and Xβ

1∪α2)\(β1∪β2), where

1,α2)∈H(β1,β2) I(α

1,β2 = (α

H(β1,β2) = (α1,α2) ∈ H(U,β1) × H(U,β2) : Q(α1) ∩ Q(α2) \ Q(β1) ∪ Q(β2) = ∅ . Let F be the family of all pairwise non-isomorphic graphs that are unions of two (not necessarily distinct)

- copies of G. The point is that F naturally deﬁnes a partition (PF)F∈F of the set of all pairs of graphs (β1,β2) ∈ G(U)×G(U) with H(β1,β2) = ∅ (as each β1∪β2 is isomorphic to some F ∈ F). Furthermore, since


every F ∈ F satisﬁes vG vF 2vG, we have, say, |F| 2(2v

) · 2v

2

G 2

4v

1∪β2, and deﬁne D as the event that ΨF 2EΨF for all F ∈ F. Using Harris’ inequality and Markov’s inequality, we deduce

1,β2)∈PF Iβ

G. Let ΨF = (β

G

P(ΨF 2EΨF) 2−|F|P(E) 4cP(E). (63)

P(E ∩ D) P(E)

F∈F

For brevity, we write P∗ for the conditional measure with respect to the status of all edges in G(n,pk)[U]. We use E∗ and Var∗ analogously. Since E ∩ D is determined by E(G(n,pk)[U]), we have

P(ZU z) P({ZU z} ∩ E ∩ D) = E P∗(ZU z) {E∩D} . (64)

In the following we estimate P∗(ZU z) whenever E ∩D holds. Recall that for all β ∈ G(U) and α ∈ H(U,β) we have β ⊆ α, V (β) ⊆ U and V (α) \ V (β) ⊆ [n] \ U. Since every copy of G in H is induced, for all

f ∈ Q(α) \ Q(β) we infer f  ∈ E(Kn(k)[U]). Using Q(β) ⊆ Q(α) it follows that E∗Iα = IβE∗Iα\β = IβEIα\β. By symmetry, EXβ is independent of the choice of β ∈ G(U), and so E∗ZU = β∈G(U) IβEXβ = YGEXβ˜ for any β˜ ∈ G(U). Taking expectations, we deduce EZU = EYGEXβ˜. Consequently E∗ZU (1 − λε)EZU whenever E holds, in which case, using the deﬁnition of z and (62), we have

z − E∗ZU (ελ/2)EZU 2εEZ = 2τεµ. (65) Turning to the conditional variance of ZU, note that, by symmetry (analogous as for Z), we have

τ2Λ =

α∈H (β1,β2)∈G×G: β1⊆α,β2⊆α

EIβ

=

1∪β2

(β1,β2)∈G×G

EIα

EIα +

1∪α2

(α1,α2)∈H×H:α1∼α2 (β1,β2)∈G×G: β1⊆α1,β2⊆α2

EI(α

1∪α2)\(β1∪β2).

(α1,α2)∈H×H:β1⊆α1,β2⊆α2, Q(α1)∩Q(α2) =∅

(66)

1∪β2E∗I(α

As before, E∗Iα

1∪α2)\(β1∪β2) for all (β1,β2) ∈ G(U) × G(U) and (α1,α2) ∈ H(U,β1) × H(U,β2). It follows that

1∪β2EI(α

1∪α2)\(β1∪β2) = Iβ

1∪α2 = Iβ

Var∗ ZU

EI(α

1∪α2)\(β1∪β2).

Iβ

1∪β2

(α1,α2)∈H(U,β1)×H(U,β2): [Q(α1)∩Q(α2)]\[Q(β1)∪Q(β2)] =∅

(β1,β2)∈G(U)×G(U)

1,β2, F and ΨF, we infer Var∗ ZU

Now, recalling the deﬁnitions of H(β1,β2), Xβ

1∪β2EXβ

Iβ

1,β2.

EXβ

ΨF max

1,β2

(β1,β2)∈PF

F∈F

F∈F (β1,β2)∈PF

1,β2 for all F ∈ F. So, with analogous considerations as above, whenever D holds we have

1,β2)∈PF EXβ

1,β2 = min(β

1,β2)∈PF EXβ

By symmetry, we have max(β

Var∗ ZU 2

1∪β2EXβ

EIβ

EΨF min

1,β2 = 2

EXβ

1,β2

(β1,β2)∈PF

F∈F

F∈F (β1,β2)∈PF

(67)

1∪α1)\(β1∪β2) 2τ2Λ,

EI(α

EIβ

= 2

1∪β2

(α1,α2)∈H(β1,β2)

(β1,β2)∈G(U)×G(U)

where the last inequality follows by comparison with (66). If µ > 0, then, using (65), the one-sided Chebyshev’s inequality (Claim 16) and (67), whenever E ∩ D holds we have

P∗(ZU > z) P∗(ZU E∗ZU + 2τεµ) 2τ2Λ/(2τ2Λ + (2τεµ)2) = Λ/(Λ + 2(εµ)2). (68) Inserting (68) into (64), we infer (for µ > 0)

P(ZU z) 1 − Λ/(Λ + 2(εµ)2) P(E ∩ D), which together with (63) implies (60) by deﬁnition of E.

![image 123](<2014-janson-lower-tail-poisson-approximation_images/imageFile123.png>)

![image 124](<2014-janson-lower-tail-poisson-approximation_images/imageFile124.png>)

![image 125](<2014-janson-lower-tail-poisson-approximation_images/imageFile125.png>)

![image 126](<2014-janson-lower-tail-poisson-approximation_images/imageFile126.png>)

A variant of the proof applies to rooted copies of H, see, e.g., Section 3 in [19] for a precise deﬁnition. The basic idea is to map the vertex set of the root R to [r], and the remaining vertices of G and H to U ⊆ [n]\[r] and [n] \ (U ∪ [r]), respectively; we leave the details to the interested reader.

# 4 Applications

In this section we illustrate the bootstrapping approaches of Section 3 via pivotal examples from additive and probabilistic combinatorics. In Section 4.1 we consider the lower tail of the number of arithmetic progressions (and Schur triples) in random subsets of the integers. In Section 4.2 we then turn to our main example: the lower tail of subgraph counts in random hypergraphs.

- 4.1 Random subsets of the integers

Let Xk = Xk(n,p) be the number of arithmetic progressions of length k 2 in the binomial random subset Γp of the integers Γ = [n] = {1,...,n}, where p = (p,...,p). Note that EXk = Θ(n2pk); see also Section 3.2. The following theorem gives fair exponential bounds for the lower tail of Xk, and its proof closely follows the strategy outlined in Section 3.

Theorem 21. Given k 2, let Ψk = Ψk(n,p) = min{n2pk,np}. There are positive constants c, C, D and n0, all depending only on k, such that for all n n0, p ∈ [0,1) and ε ∈ (0,1] satisfying ε2Ψk {ε<1}D we have

exp −(1 − p)−5Cε2Ψk P(Xk (1 − ε)EXk) exp −cε2Ψk . (69)

Proof. Let µ = EXk, Λ = Λ(Xk) and δ = δ(Xk). Routine calculations, analogous to Example 3.2 in [16], reveal that

δ = Θ(npk−1 + p) and µ2/Λ = µ/(1 + δ) = Θ(Ψk), (70) where the implicit constants depend only on k. Hence the upper bound of (69) is an immediate consequence of (2). For the lower bound we pick, with foresight, D = D(k) 1 such that EXk Ψk/D and µ2/Λ Ψk/D for n n0(k).

If Ψk = n2pk, then Theorem 2 (with X = Xk) yields P(Xk (1 − ε)EXk) exp −Θ((1 − p)−5ε2Ψk) since ε2EXk ε2Ψk/D {ε<1}, Π(Xk) = pk p, δ = O(1) and EXk = Θ(Ψk).

If Ψk = np, then Theorem 15 (with X = Xk) and Theorem 2 (with X = |Γp|) yield, with d = 1/2 + {ε=1}1/2,

P(Xk (1 − ε)EXk) dP(|Γp| (1 − ε)E|Γp|) exp − {ε<1} log 2 − Θ((1 − p)−5ε2Ψk) since (εµ)2 Λε2Ψk/D {ε<1}Λ, ε2E|Γp| = ε2Ψk {ε<1} and E|Γp| = Ψk. This completes the proof of

(69) since {ε<1} log 2 {ε<1}D (1 − p)−5ε2Ψk.

![image 127](<2014-janson-lower-tail-poisson-approximation_images/imageFile127.png>)

![image 128](<2014-janson-lower-tail-poisson-approximation_images/imageFile128.png>)

![image 129](<2014-janson-lower-tail-poisson-approximation_images/imageFile129.png>)

![image 130](<2014-janson-lower-tail-poisson-approximation_images/imageFile130.png>)

For Schur triples, which are deﬁned in Section 3.2, the same calculations carry over (with k = 3; the point is that (70) holds), yielding an analogous lower tail estimate. Related results for the upper tail of arithmetic progressions and Schur triples have been established by Warnke [30].

- 4.2 Random hypergraphs


Finally, we consider the lower tail of the number XH = XH(n,p) of copies of a given k-graph H in G(n,pk), and prove Theorems 3–5. Here the following precise analysis of Λ(XH) is at the heart of our approach. In fact, Lemma 22 is essentially given in [15] (for k = 2), but the restriction to subgraphs from IH is new and crucial for our purposes: the key point is that every copy of G ∈ IH in H is induced. Recall that mk(H) is deﬁned by (8).

- Lemma 22. Let H be a k-graph with eH 1. Deﬁne IH as the collection of all non-isomorphic subgraphs J ⊆ H which satisfy eJ max{eK,1} for all K ⊆ H with vK = vJ. For all p = p(n) ∈ (0,1] we have


(EXH)2 EXJ

(EXH)2 minJ∈I

CJ,H2

Λ(XH) = (1 + o(1))

, (71)

= Θ

![image 131](<2014-janson-lower-tail-poisson-approximation_images/imageFile131.png>)

![image 132](<2014-janson-lower-tail-poisson-approximation_images/imageFile132.png>)

EXJ

H

J∈IH

min

EXJ = o( min

EXJ), (72)

J∈IH

J⊆H,eJ 1,J ∈∗IH

where CJ,H denotes the number of copies of J in H, and J ∈∗IH means that there is no J′ ∈ IH which is isomorphic to J. In addition, p = ω(n−1/m

EXJ = nk p and Λ(XH) = (1 + o(1))e2H(EXH)2/[ nk p].

k(H)) implies minJ∈I

H

The fairly standard proof of Lemma 22 is deferred to Appendix A. In the following proofs of Theorems 3–

- 5 we shall not explicitly discuss the upper bounds: once the form of (EXH)2/Λ(XH) has been established, these are immediate consequences of (2).


- Proof of Theorem 3. Let d = 2−(4

v2

H+2), λ = 2v

H+3 and ε0 = (2λ)−1. Since the claim is trivial otherwise, we henceforth assume p > 0. Furthermore, we use the convention that all implicit constants depend only on H, and tacitly assume n n0(H) whenever necessary. Suppose that ΦH = EXG for G ⊆ H with eG 1. Using (71) and (72) we infer G ∈ IH, (EXH)2/Λ(XH) = Θ(ΦH) and δ(XG) = O(1). With foresight, we pick D = D(H) log(1/d) such that (EXH)2/Λ(XH) ΦH/D holds.

If ε ∈ [ε0,1], then Π(XG) = pe

G

p, EXG = ΦH, 1 ε−0 2ε2 and (3) yield P(XH (1 − ε)EXH) P(XH = 0) P(XG = 0) exp −(1 − p)−1ε−0 2ε2ΦH . (73)

It remains to establish (6) when ε < ε0. We shall eventually apply Theorem 20 with U = [⌊n/2⌋], where YG counts the total number of copies of G whose vertex sets are completely contained in U. Since G(n,pk)[U] has the same distribution as G(nk′),p with n′ = |U| ≈ n/2, we readily deduce 3−v

G

EXG EYG EXG and δ(YG) = Θ(δ(XG)). Furthermore, G ∈ IH implies that every copy of G in H is induced. So, using λε 1/2, Π(YG) p, δ(YG) = O(1) and EYG = Θ(ΦH), a combination of Theorem 20 and Theorem 2 yields

P(XH (1 − ε)EXH) dP(YG (1 − λε)EYG) exp − log(1/d) − Θ((1 − p)−5λ2ε2ΦH) since ε2(EXH)2 ε2ΦHΛ(XH)/D Λ(XH) and (λε)2EYG λ23−v

G

ε2EXG ε2ΦH D 1. This completes the proof of (6) since log(1/d) D (1 − p)−5ε2ΦH.

![image 133](<2014-janson-lower-tail-poisson-approximation_images/imageFile133.png>)

![image 134](<2014-janson-lower-tail-poisson-approximation_images/imageFile134.png>)

![image 135](<2014-janson-lower-tail-poisson-approximation_images/imageFile135.png>)

![image 136](<2014-janson-lower-tail-poisson-approximation_images/imageFile136.png>)

- Proof of Theorem 4. Since the claim is trivial otherwise, we henceforth assume p > 0. Furthermore, since p = o(1) we have Π = o(1). Recalling the properties of G, using (71) and (72) we infer G ∈ IH, (EXH)2/Λ(XH) = (1 + o(1))EXG and δ(XG) = o(1).

In the special case eG = 1, note that uniqueness of G in H implies eH = 1, and that minimality of EXG implies vG = k. Thus XH = XG v n−k

H−k and δ(XG) = 0. Using P(XH (1−ε)EXH) = P(XG (1−ε)EXG), the lower bound of (9) now follows from Theorem 1 (applied to XG), where ξ = o(1) by our assumptions.

Henceforth we thus assume eG 2. Now, in case of H = G the lower bound of (9) follows directly from Theorem 1. In the main case, where G H and eG 2, there exists, by assumption, ω = ω(n) → ∞ such that ε2EXG {ε<1}ω log(e/ε). Setting γ = 2 exp{−ω1/2} = o(1) we have (when ω 1) ε2EXG

{ε<1}ω1/2 log(2/(γε)), which together with Lemma 10 yields 2−1γε {ε<1} exp{−2ω−1/2ϕ(−ε)EXG}. So, if (1 + γ)ε < 1 and 3√γ < 1 − ε, then a combination of Theorem 18 (with X = XH, Y = XG and κ = 0), Theorem 1 (for XG) and Lemma 12 (with A = 1+γ) establishes (9). Otherwise ε 1−max{γ/(1+γ),3√γ} = 1−o(1) holds, and then a combination of (49) (with X = XH and Y = XG) and Lemma 7 (for XG) completes the proof.

![image 137](<2014-janson-lower-tail-poisson-approximation_images/imageFile137.png>)

![image 138](<2014-janson-lower-tail-poisson-approximation_images/imageFile138.png>)

![image 139](<2014-janson-lower-tail-poisson-approximation_images/imageFile139.png>)

![image 140](<2014-janson-lower-tail-poisson-approximation_images/imageFile140.png>)

![image 141](<2014-janson-lower-tail-poisson-approximation_images/imageFile141.png>)

![image 142](<2014-janson-lower-tail-poisson-approximation_images/imageFile142.png>)

- Proof of Theorem 5. We start with the main case ε = o(1). Note that Lemma 22 implies minJ∈I


EXJ =

H

n k p = E|Γp| and (EXH)2/Λ(XH) = (1 + o(1))E|Γp|/e2H. By assumption, there is ω = ω(n) → ∞ such that

ε 1/ω and ε2 nk p ω. Let τ = 6eHω−1/2 = o(1) and A = (1+τ)/eH, so that ϕ(−Aε) (1+o(1))ϕ(−ε)/e2H by Lemma 12. Since p = o(1), a combination of Theorem 17 (with X = XH and k = eH) and Theorem 1

(with X = |Γp|) establishes (10), where the factor c = 1/2 is negligible due to ϕ(−ε) nk p → ∞.

The remaining ε = 1 − o(1) estimate of (10) follows from Lemma 23 below and Lemma 11 since 1 − p = e−(1+o(1))p and ϕ(−ε) = 1 + o(1) for p = o(1) and ε = 1 − o(1), respectively.

![image 143](<2014-janson-lower-tail-poisson-approximation_images/imageFile143.png>)

![image 144](<2014-janson-lower-tail-poisson-approximation_images/imageFile144.png>)

![image 145](<2014-janson-lower-tail-poisson-approximation_images/imageFile145.png>)

![image 146](<2014-janson-lower-tail-poisson-approximation_images/imageFile146.png>)

The proof above used the following lemma, which follows from results of Saxton and Thomason [25].

- Lemma 23. Let H be a k-graph with eH 1. If p = p(n) ∈ [0,1] and ε = ε(n) ∈ (0,1] satisfy p =


ω(n−1/m

k(H)) and ε = 1 − o(1), then we have

H)(n

). (74)

P(XH (1 − ε)EXH) = (1 − p)(1+o(1))(1−π

k

Proof. For the lower bound, let Tn,H be any hypergraph which achieves equality in the deﬁnition of ex(n,H). As every subgraph of Tn,H is H-free, it follows that

P(XH (1 − ε)EXH) P(XH = 0) P(G(n,pk) ⊆ Tn,H) = (1 − p)(n

)−e(Tn,H).

k

This establishes the lower bound of (74) since e(Tn,H) = (πH + o(1)) nk and 1 − πH ∈ (0,1].

Turning to the corresponding upper bound, we ﬁrst consider the case eH 2. Let 0 < δ (1 − πH)/3. Theorem 9.2 in [25] implies that there is c = c(H,δ) > 0 such that for n c the following holds for all q ∈ [n−1/m

k(H),1/c]: there exists s c and a mapping T  → C(T) of sequences T = (T1,...,Ts) with Ti ⊆ E(Kn(k)) to sets C(T) ⊆ E(Kn(k)) such that for every k-graph G on n vertices with less than nv

qe

H

H

- copies of H there exists T = (T1,...,Ts) such that E(G) ⊆ C(T), |C(T)| (πH + δ) nk = F and further 1 i s |Ti| cqnk = U and 1 i s Ti ⊆ E(G). (Recall that E(Kn(k)) is the set of all edges in the complete


k-graph Kn(k). The mapping T  → C(T) is quite complicated; the point of it is that we can bound the number of ’containers’ C(T) by the number of sequences T.)

By assumption we have 1 − ε 1/ω and p ωn−1/m

k(H), where ω = ω(n) → ∞. Let q = ω−1/e

p, so that (1 − ε)EXH < ω−1nv

H

and n−1/m

k(H) q ω−1/e

qe

= nv

pe

1/c for n n0(c). Note that we can construct a superset of all possible T = (T1,...,Ts) as follows: we ﬁrst decide on | 1 i s Ti| = u, then select u edges of Kn(k) and decide on all the Ti in which they appear. So, taking the union bound over all choices of T that are possible for G = G(n,pk), using 1 i s Ti ⊆ E(G(n,pk)) and E(G(n,pk)) \ C(T) = ∅ it follows that

H

H

H

H

H

P(XH (1 − ε)EXH)

0 u U

n k

u

(2s)upu(1 − p)(n

)−F. (75)

k

Hence, recalling the deﬁnitions of F and U, for any θ ∈ (0,1] we obtain

n k

)−Fθ−U

P(XH (1 − ε)EXH) (1 − p)(

n k

(2s)upuθu

u

(76)

0 u U

)

(

n k

n k

).

n k

)ecqn

k log(1/θ)+2spθ(

H−δ)(

n k

)−Fθ−U 1 + 2spθ

(1 − p)(

(1 − p)(1−π

Choose θ = q/p = o(1). Then q log(1/θ) = pθ log(1/θ) = o(p), ep (1−p)−1 and (76) yield, for n n0(c,s,δ),

n k

). (77)

n k

)) (1 − p)(1−π

H−2δ)(

n k

)eo(p(

H−δ)(

P(XH (1 − ε)EXH) (1 − p)(1−π

It follows as usual that there is some δ(n) → 0 such that (77) holds with δ = δ(n) for n n0, which together with 1 − πH ∈ (0,1] establishes the upper bound of (74) when eH 2.

Finally, in the remaining case eH = 1 (where Theorem 9.2 in [25] does not apply) we have XH = e(Gn,p(k)) v n−k

H−k . Hence XH (1 − ε)EXH is equivalent to e(G(n,pk)) (1 − ε) nk p. Since e(G(n,pk)) ∼ Bin nk ,p and πH = 0, (74) follows by standard calculations. (For example, (75) holds with s = 0 and U = F = (1 − ε)p nk , and the reasoning of (76)–(77) carries over since F = o(p nk ) and U ω−1pnk = qnk.) Acknowledgement. We would like to thank Andrew Thomason for giving us a draft of [25] together with helpful comments on it.

![image 147](<2014-janson-lower-tail-poisson-approximation_images/imageFile147.png>)

![image 148](<2014-janson-lower-tail-poisson-approximation_images/imageFile148.png>)

![image 149](<2014-janson-lower-tail-poisson-approximation_images/imageFile149.png>)

![image 150](<2014-janson-lower-tail-poisson-approximation_images/imageFile150.png>)

# References

- [1] N. Alon and J. Spencer. The probabilistic method. Third edition. Wiley-Interscience Series in Discrete Mathematics and Optimization. John Wiley & Sons Inc., Hoboken, NJ (2008).
- [2] A.D. Barbour. Poisson convergence and random graphs. Math. Proc. Cambridge Philos. Soc. 92 (1982), 349–359.
- [3] B. Bollob´s. Threshold functions for small subgraphs. Math. Proc. Cambridge Philos. Soc. 90 (1981), 197–206.
- [4] B. Bollob´s and O. Riordan. Colorings generated by monotone properties. Random Struct. Alg. 12 (1998), 1–25.
- [5] S. Chatterjee. The missing log in large deviations for triangle counts. Random Struct. Alg. 40 (2012), 437–451.
- [6] S. Chatterjee and A. Dembo. Nonlinear large deviations. Preprint, 2014. arXiv:1401.3495.
- [7] S. Chatterjee and S.R.S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin. 32 (2011), 1000–1017.
- [8] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Struct. Alg. 41 (2012), 469–487.
- [9] L. Devroye, L. Gyo¨rﬁ, and G. Lugosi. A probabilistic theory of pattern recognition. Applications of Mathematics (New York) 31. Springer-Verlag, New York (1996).


- [10] P. Erd˝s and A. Re´nyi. On the evolution of random graphs. Magyar Tud. Akad. Mat. Kutat´o Int. K¨ozl. 5 (1960), 17–61.
- [11] C.M. Fortuin, P.W. Kasteleyn, and J. Ginibre. Correlation inequalities on some partially ordered sets. Comm. Math. Phys. 22 (1971), 89–103.
- [12] T.E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc. 56 (1960), 13–20.
- [13] S. Janson. Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221–229.
- [14] S. Janson. New versions of Suen’s correlation inequality. Random Struct. Alg. 13 (1998), 467–483.
- [15] S. Janson, T.  Luczak, and A. Rucin´ski. An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph. In Random graphs ’87 (Poznan´, 1987), pp. 73–87, Wiley, Chichester (1990).
- [16] S. Janson, T.  Luczak, and A. Rucin´ski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York (2000).
- [17] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math. 142 (2004), 61–92.
- [18] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica 24 (2004), 615–640.
- [19] S. Janson and A. Rucin´ski. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat. 49 (2011), 79–96.
- [20] P. Keevash. Hypergraph Tur´an problems. In Surveys in combinatorics (Exeter 2011), pp. 83–139, Cambridge Univ. Press, Cambridge (2011).
- [21] J.H. Kim and V.H. Vu. Concentration of multivariate polynomials and its applications. Combinatorica 20 (2000), 417–434.
- [22] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Preprint (2014). arXiv:1402.6011.
- [23] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Struct. Alg., to appear. arXiv:1203.1024.
- [24] A. Rucin´ski. When are small subgraphs of a random graph normally distributed? Probab. Theory Related Fields 78 (1988), 1–10.
- [25] D. Saxton and A. Thomason. Hypergraph containers. (Revised version of arXiv:1204.6595v2.) Preprint (2014).
- [26] M. Sileikis.ˇ On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin. 19 (2012), Paper 4.
- [27] J. Spencer. Counting extensions. J. Combin. Theory Ser. A 55 (1990). 247–255.
- [28] W.-C. Suen. A correlation inequality and a Poisson limit theorem for nonoverlapping balanced subgraphs of a random graph. Random Struct. Alg. 1 (1990), 231–242.
- [29] V.H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput. 10 (2001), 79–94.
- [30] L. Warnke. Upper tails for arithmetic progressions in random subsets. Preprint (2013).


# A Appendix

In this appendix we prove Lemmas 10–12 and 22.

- Proof of Lemma 10. By our conventions, (16) is trivial for ε = 1, and so we henceforth assume ε ∈ [0,1). First, let f(x) = 2ϕ(−x)−(1−x)log2(1−x). Since f′(x) = log2(1−x) 0 for x ∈ [0,1), we infer f(ε) f(0) =

- 0. Second, let g(x) = 2ϕ(−x) − x2. Since 1 − x e−x implies g′(x) = −2 log(1 − x) − 2x 0 for x ∈ [0,1), we infer g(ε) g(0) = 0. Next, let h(x) = log2(1 − x) − 2ϕ(−x). Since h′(x) = −2x(1 − x)−1 log(1 − x) 0 for x ∈ [0,1), we infer h(ε) h(0) = 0. Finally, 1 − ε e−ε implies ϕ(−ε) = (1 − ε)log(1 − ε) + ε ε2.


![image 151](<2014-janson-lower-tail-poisson-approximation_images/imageFile151.png>)

![image 152](<2014-janson-lower-tail-poisson-approximation_images/imageFile152.png>)

![image 153](<2014-janson-lower-tail-poisson-approximation_images/imageFile153.png>)

![image 154](<2014-janson-lower-tail-poisson-approximation_images/imageFile154.png>)

- Proof of Lemma 11. As (17) is trivial otherwise, we henceforth assume ε < 1. Since ϕ′(x) = log(1 + x) 0 for x ∈ [−1,0], we infer ϕ(−ε) ϕ(−1) = 1, which establishes the ﬁrst inequality of (17).


Next, deﬁne y = 1 − ε, and note that y ∈ (0,e−1]. Let g(x) = φ(x − 1) = 1 − xlog(e/x). Since g′(x) = log x 0 for x ∈ (0,1], we infer g(y) g(e−1) = (e − 2)/e > 0. Let h(x) = √x log(e/x), and note that h(y) > 0. Since h′(x) = − log(ex)/(2√x) 0 for x ∈ (0,e−1], we infer h(y) h(e−1) = 2/√e. It follows that

![image 155](<2014-janson-lower-tail-poisson-approximation_images/imageFile155.png>)

![image 156](<2014-janson-lower-tail-poisson-approximation_images/imageFile156.png>)

![image 157](<2014-janson-lower-tail-poisson-approximation_images/imageFile157.png>)

√yh(y) g(y)

2√ey e − 2

5√1 − ε, which establishes the second inequality of (17).

1 − g(y) g(y)

1 ϕ(−ε) − 1 =

![image 158](<2014-janson-lower-tail-poisson-approximation_images/imageFile158.png>)

![image 159](<2014-janson-lower-tail-poisson-approximation_images/imageFile159.png>)

![image 160](<2014-janson-lower-tail-poisson-approximation_images/imageFile160.png>)

=

![image 161](<2014-janson-lower-tail-poisson-approximation_images/imageFile161.png>)

![image 162](<2014-janson-lower-tail-poisson-approximation_images/imageFile162.png>)

![image 163](<2014-janson-lower-tail-poisson-approximation_images/imageFile163.png>)

![image 164](<2014-janson-lower-tail-poisson-approximation_images/imageFile164.png>)

![image 165](<2014-janson-lower-tail-poisson-approximation_images/imageFile165.png>)

![image 166](<2014-janson-lower-tail-poisson-approximation_images/imageFile166.png>)

![image 167](<2014-janson-lower-tail-poisson-approximation_images/imageFile167.png>)

![image 168](<2014-janson-lower-tail-poisson-approximation_images/imageFile168.png>)

- Proof of Lemma 12. We ﬁrst consider the case y = Aε 1, so that y ∈ [0,1]. Since log(1 − x) =


− j 1 xj/j −x − x2/2 for x ∈ [0,1), we see that ϕ(−y) = (1 − y)log(1 − y) + y (1 + y)y2/2, where the inequality is trivial for y = 1 due to ϕ(−1) = 1. By Lemma 10 we have ε2/2 ϕ(−ε), so that

ϕ(−Aε) (1 + Aε)(Aε)2/2 (1 + Aε)A2ϕ(−ε).

Turning to the second inequality of (18) we henceforth assume γ > 0 and ε ∈ [0,1), as the claim is trivial otherwise. Let ρ(x) = ϕ(−x), and note that ρ′(x) = − log(1 − x) and ρ′′(x) = 1/(1 − x). Since log(1 − x) −x/(1 − x) for x ∈ [0,1), c.f. (14), we see that ρ′(ε) ε/(1 − ε). Note that γ > 0 and 3√γ 1 − ε imply 0 < 3γ3/2 γ − γε 1 − (1 + γ)ε. So, recalling ε2/2 ϕ(−ε) and A = 1 + γ, using Taylor’s theorem with remainder it follows that 0 Aε < 1 and

![image 169](<2014-janson-lower-tail-poisson-approximation_images/imageFile169.png>)

ϕ(−Aε) ϕ(−ε) + γε2/(1 − ε) + (γε)2/[2(1 − (1 + γ)ε)] 1 + 2γ/(1 − ε) + γ2/(1 − (1 + γ)ε) ϕ(−ε) (1 + √γ)ϕ(−ε),

![image 170](<2014-janson-lower-tail-poisson-approximation_images/imageFile170.png>)

completing the proof of (18). Proof of Lemma 22. Deﬁne SH as the collection of all non-isomorphic subgraphs J ⊆ H with eJ 1. Let N(n,H) denote the number of copies of H in Kn(k). Note that N(n,H) = Θ(nv

![image 171](<2014-janson-lower-tail-poisson-approximation_images/imageFile171.png>)

![image 172](<2014-janson-lower-tail-poisson-approximation_images/imageFile172.png>)

![image 173](<2014-janson-lower-tail-poisson-approximation_images/imageFile173.png>)

![image 174](<2014-janson-lower-tail-poisson-approximation_images/imageFile174.png>)

). By double counting pairs (J′,H′) of copies of J and H with J′ ⊆ H′ ⊆ Kn(k), using symmetry we infer that, in Kn(k), there are exactly

H

N(n,H)CJ,H N(n,J)

H−vJ) (78)

= Θ(nv

λJ,H(n) =

![image 175](<2014-janson-lower-tail-poisson-approximation_images/imageFile175.png>)

copies of H containing any given copy of J. Since EXJ = N(n,J)pe

and CH,H = 1, by distinguishing all possible intersections of H-copies it follows that

J

H−eJ =

N(n,J)λ2J,H(n)p2e

Λ(XH) EXH +

J∈SH

J∈SH:J =H

(EXH)2 EXJ

CJ,H2

. (79)

![image 176](<2014-janson-lower-tail-poisson-approximation_images/imageFile176.png>)

pe

Recall that EXJ = Θ(nv

). By deﬁnition, for every K ∈ SH \ IH there is J ∈ IH with vJ = vK and

J

J

- eJ eK + 1. Using EXK = Ω(p−1EXJ) we infer

Λ(XH)

J∈IH

1 + {e

J 2}O(p) CJ,H2

(EXH)2 EXJ

![image 177](<2014-janson-lower-tail-poisson-approximation_images/imageFile177.png>)

. (80)

Suppose that ω = ω(n) → ∞ satisﬁes 1 ω n1/(2m

k(H)+1). Using mk(H) (eK − 1)/(vK − k) when

- eK 2, note that for p ωn−1/m


k(H) we have min K∈SH:vK>k

K−kpe

K−1 min n, min

K−1 ω. (81)

nv

ωe

K∈SH:eK 2

Thus the ‘edge-term’ with eJ = 1 and vJ = k dominates (80) for p ωn−1/m

k(H): indeed, K = J implies EXK = Ω(ωEXJ). As ωn−1/m

k(H) ω−1, the 1 + {e

J 2}O(p) factor in (80) can thus be replaced by

- 1 + O(ω−1), establishing the upper bound of (71). Furthermore, by combining EXK = Ω(p−1EXJ) and EXK = Ω(ωEXJ) in an analogous way, it is not diﬃcult to see that (72) holds. For the lower bound of (71) we argue similar as for (79), but restrict our attention to intersections in subgraphs J ∈ IH only. Moreover, to avoid overcounting (due to additional intersections outside of J), in the case J = H we replace λ2J,H(n) by


λG,H(n) = 1 − O(n−1) λ2J,H(n),

λJ,H(n) λJ,H(n) − O

J′ G⊆H:J′∼=J

where we used (78) and that every copy of J ∈ IH in H is induced (which implies vG vJ + 1). With these modiﬁcations, the lower bound of (71) follows.

![image 178](<2014-janson-lower-tail-poisson-approximation_images/imageFile178.png>)

![image 179](<2014-janson-lower-tail-poisson-approximation_images/imageFile179.png>)

![image 180](<2014-janson-lower-tail-poisson-approximation_images/imageFile180.png>)

![image 181](<2014-janson-lower-tail-poisson-approximation_images/imageFile181.png>)

