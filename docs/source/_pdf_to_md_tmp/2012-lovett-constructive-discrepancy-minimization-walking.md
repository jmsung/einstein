arXiv:1203.5747v2[cs.DS]11Oct2012

Constructive Discrepancy Minimization by Walking on The Edges

Shachar Lovett∗ Institute for Advanced Study slovett@math.ias.edu

Raghu Meka† Institute for Advanced Study raghu@math.ias.edu

Abstract

Minimizing the discrepancy of a set system is a fundamental problem in combinatorics. One of the cornerstones in this area is the celebrated six standard deviations result of Spencer (AMS 1985): In any system of n sets in a universe of size n, there always exists a coloring which achieves discrepancy 6√n. The original proof of Spencer was existential in nature, and did not give an eﬃcient algorithm to ﬁnd such a coloring. Recently, a breakthrough work of Bansal (FOCS 2010) gave an eﬃcient algorithm which ﬁnds such a coloring. His algorithm was based on an SDP relaxation of the discrepancy problem and a clever rounding procedure. In this work we give a new randomized algorithm to ﬁnd a coloring as in Spencer’s result based on a restricted random walk we call Edge-Walk. Our algorithm and its analysis use only basic linear algebra and is “truly” constructive in that it does not appeal to the existential arguments, giving a new proof of Spencer’s theorem and the partial coloring lemma.

![image 1](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile1.png>)

# 1 Introduction

Minimizing the discrepancy of a set system is a fundamental problem in combinatorics with many applications in computer science (see [Mat99, Cha02]). Here, we are given a collection of sets S from a universe V = {1,... ,n} and the goal is to ﬁnd a coloring χ : V → {1,−1} that minimizes the maximum discrepancy χ(S) = maxS∈S | i∈S χ(i)|. We denote the minimum discrepancy of S by disc(S).

There is by now a rich body of literature on discrepancy minimization with special focus on the ‘discrete’ formulation described above. One of the cornerstones in this area is the celebrated six standard deviations result of Spencer [Spe85].

- Theorem 1. For any set system (V,S) with |V | = n, |S| = m, there exists a coloring χ : V → {1,−1} such that χ(S) < K n · log2(m/n), where K is a universal constant (K can be 6 if m = n).


![image 2](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile2.png>)

One remarkable aspect of the above theorem is that for m = O(n), the discrepancy is just O(√n), whereas a random coloring has discrepancy O(√nlog n). Spencer’s original proof relied on an ingenious pigeon-hole principle argument based on Beck’s partial coloring approach [Bec81]. However, due to the use of the pigeon-hole principle, the proof was non-constructive: Spencer’s proof does not give an eﬃcient (short of enumerating all possible colorings) way to ﬁnd a good coloring χ as in the theorem. This was a longstanding open problem in discrepancy minimization

![image 3](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile3.png>)

![image 4](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile4.png>)

![image 5](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile5.png>)

∗Supported by NSF grant DMS-0835373. †Supported by NSF grants DMS-0835373 and CCF-0832797.

and it was even conjectured that such an algorithm cannot exist [AS11]. In a recent breakthrough work, Bansal [Ban10] disproved this conjecture and gave the ﬁrst randomized polynomial time algorithm to ﬁnd a coloring with discrepancy O(√n · log(m/n)), thus matching Spencer’s bound up to constant factors for the important case of m = O(n).

![image 6](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile6.png>)

In this work we give a new elementary constructive proof of Spencer’s result. Our algorithm and its analysis use only basic linear algebra and perhaps more importantly is “truly” constructive. Bansal’s algorithm while giving a constructive solution, still implicitly uses Spencer’s original nonconstructive proof to argue the correctness of the algorithm. Our algorithm on the other hand also gives a new (constructive) proof of Spencer’s original result.

- Theorem 2. For any set system (V,S) with |V | = n, |S| = m, there exists a randomized algorithm running in time O˜((n+m)3) 1 that with probability at least 1/2, computes a coloring χ : V → {1,−1} such that χ(S) < K n · log2(m/n), where K is a universal constant.

![image 7](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile7.png>)

The constant K above can be taken as 13 for the case of m = n. Observe that our bound matches Spencer’s result for all ranges of m,n, whereas Bansal’s result loses an additional factor of Ω( log(m/n)).

![image 8](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile8.png>)

We also get a similar constructive proof of Srinivasan’s result [Sri97] for minimizing discrepancy in the “Beck-Fiala Setting” where each variable is constrained to occur in a bounded number of sets. Bansal was able to use his SDP based approach to give a constructive proof of Srinivasan’s result. Our techniques for Theorem 2 also extend to this setting matching the best known constructive bounds.

- Theorem 3. Let (V,S) be a set-system with |V | = n, |S| = m and each element of V contained in at most t sets from S. Then, there exists a randomized algorithm running in time O˜((n+m)5) that with probability at least 1/2 computes a coloring χ : V → {1,−1} such that χ(S) < K√t · log n, where K is a universal constant.


![image 9](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile9.png>)

We remark that non-constructively, a better bound of O(√t · log n) was obtained by Banaszczsyk [Ban98] using techniques from convex geometry. Beck and Fiala [BF81] proved that disc(S) < 2t and conjectured that disc(S) = O(√t) and this remains a major open problem in discrepancy minimization.

![image 10](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile10.png>)

![image 11](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile11.png>)

# 2 Outline of Algorithm

To describe the algorithm we ﬁrst set up some notation. Fix a set system (V,S) with V = {1,... ,n} and |S| = m. As is usually done, we shall assume that m ≥ n – the general case can be easily reduced to this situation. Similar to Spencer’s original proof our algorithm also works by ﬁrst ﬁnding a “partial coloring”: χ : V → [−1,1] such that

- • For all S ∈ S, |χ(S)| = O( nlog(m/n)).

![image 12](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile12.png>)

- • |{i : |χ(i)| = 1}| ≥ cn, for a ﬁxed constant c > 0.


Given such a partial coloring, we can then recurse (as in Spencer’s original proof) by running the algorithm on the set of variables assigned values in (−1,1) without changing the colors of variables

![image 13](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile13.png>)

1Throughout, O˜( ) hides polylogarithmic factors.

assigned values in {1,−1}. Eventually, we will converge to a full coloring and the total discrepancy (a geometrically decreasing series with ratio roughly √1 − c) can be bounded by O( nlog(m/n)). Henceforth, we will focus on obtaining such a partial coloring.

![image 14](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile14.png>)

![image 15](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile15.png>)

Let v1,... ,vm ∈ Rn be the indicator vectors of the sets in S. Then, the discrepancy of χ on S is χ(S) = maxi∈[m] | χ,vi  |. Our partial coloring algorithm (as does Spencer’s approach) works in the more general context of arbitrary vectors, and we will work in this general context.

- Theorem 4 (Main Partial Coloring Lemma). Let v1,... ,vm ∈ Rn be vectors, and x0 ∈ [−1,1]n


be a “starting” point. Let c1,... ,cm ≥ 0 be thresholds such that mj=1 exp(−c2j/16) ≤ n/16. Let δ > 0 be a small approximation parameter. Then there exists an eﬃcient randomized algorithm

which with probability at least 0.1 ﬁnds a point x ∈ [−1,1]n such that

- (i) | x − x0,vj  | ≤ cj vj 2.
- (ii) |xi| ≥ 1 − δ for at least n/2 indices i ∈ [n].


Moreover, the algorithm runs in time O((m + n)3 · δ−2 · log(nm/δ)).

Note that the probability of success 0.1 can be boosted by simply running the algorithm multiple times. Given the above result, we can get the desired partial coloring needed for minimizing set discrepancy by applying the theorem to the indicator vectors of the sets S ∈ S with δ = 1/n, and x0 = 0n. Combining the above with the recursive analysis gives Theorem 2 with a running time of O˜((n + m)5). It was pointed to us by Spencer that we can in fact take δ = 1/log n and then use randomized rounding to get the running time stated in Theorem 2.

We stress that Spencer’s original approach shows the existence of a true partial coloring (the colors take values in {−1,0,1}), whereas our approach gives a fractional coloring—the colors take values in [−1,1] though many of the colors are close to {−1,1}.

The constructive proof of Srinivasan’s result, Theorem 3, follows a similar outline starting from our partial coloring lemma. We defer the details to Section 6.

We now describe the proof of the partial coloring lemma.

## 2.1 Partial Coloring by Walking on The Edge

We will ﬁnd the desired vector x by performing a constrained random walk that we refer to as Edge-Walk for reasons that will become clear later.

We ﬁrst describe the algorithm conceptually, ignoring the approximation parameter δ. We will assume throughout that v1 2 = ... = vm 2 = 1 as this normalization does not change the problem. Consider the following polytope P which describes the legal values for x ∈ Rn,

P := {x ∈ Rn : |xi| ≤ 1 ∀i ∈ [n], | x − x0,vj  | ≤ cj ∀j ∈ [m]}.

We will refer to the constraints |xi| ≤ 1 as variable constraints and to the constraints | x − x0,vj  | ≤ cj as discrepancy constraints. The partial coloring lemma can be rephrased in terms of the polytope P as follows: there exists a point x ∈ P that satisﬁes at least n/2 variable constraints without any slack. Intuitively, this corresponds to ﬁnding a point x in P that is as far away from origin as possible; the hope being that if x 2 is large, then in fact many of the coordinates of x will be close to 1 in absolute value. We ﬁnd such a point (and show it’s existence) by simulating a constrained Brownian motion in P. (If uncomfortable with Brownian motion, the reader can view the walk as taking very small discrete Gaussian steps, which is what we will do in the actual analysis.)

Consider a random walk in P corresponding to the Browninan motion starting at x = x0. Whenever the random walk reaches a face of the polytope, it continues inside this face. We continue the walk until we reach a vertex x ∈ P. The idea being that we want to get away from origin, but do not want to cross the polytope – so whenever a constraint (variable or discrepancy) becomes tight we do not want to change the constraint and continue in the subspace orthogonal to the deﬁning constraint. We call this random walk the “Edge-Walk” in P.

By deﬁnition, the random walk is constrained to P, and | x − x0,vj  | ≤ cj for all j ∈ [m]. We show that as long as exp(−c2j) ≪ n, the random walk hits many variable constraints with good probability. That is, the end vertex x has xi ∈ {−1,1} for many indices. This step relies on a martingale tail bound for Gaussian variables and an implicit use of the ℓ2-norm as a potential function for gauging the number of coordinates close to 1 in absolute value.

The actual algorithm diﬀers slightly from the above description. First, we will not run the walk until we reach a vertex of P, but after a certain ‘time’ has passed, which will still guarantee the above conditions. Second, we will approximate the continuous random walk by many small discrete steps.

# 3 Comparison with Entropy Method

Here we contrast our result with Beck’s partial coloring lemma [Bec81] based on the Entropy method which has many applications in discrepancy theory. While similar in spirit, our partial coloring lemma is incomparable and in particular, even the existence of the vector x as in Theorem 4 does not follow from Beck’s partial coloring lemma.

We ﬁrst state Beck’s partial coloring lemma as formulated in [Mat98].

- Theorem 5 (Entropy Method). Let (V,S) be a set-system with V = {1,... ,n}. Let ∆ : S → R+ be such that S∈S g(∆S/ |S|) ≤ n/5, where g : R+ → R+ is deﬁned by,


![image 16](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile16.png>)

Ke−λ2/9, λ > 0.1 K ln(1/λ), λ ≤ 0.1

,

g(λ) =

where K is an absolute constant. Then, there exists χ ∈ {−1,0,1}n with |{i : χi = 0}| ≥ n/2 such that | i∈S χi| ≤ ∆S for every S ∈ S.

By applying our Theorem 4 to the indicator vectors of the sets in S and δ = 1/poly(n) suﬃciently small we get the following corollary. Corollary 6. Let (V,S) be a set-system with V = {1,... ,n}. Let ∆ : S → R+ be such that

exp(−∆2S/16|S|) ≤ n/16.

S∈S

Then, there exists χ ∈ [−1,1]n with |{i : |χi| = 1}| ≥ n/2, such that | i∈S χi| ≤ ∆S + 1/poly(n), for every S ∈ S. Moreover, there exists a randomized poly(|S|,n)-time algorithm to ﬁnd χ.

The above result strengthens the Entropy method in two important aspects. Firstly, our method is constructive. In contrast, the entropy method is non-constructive and the constructive discrepancy minimization algorithms of Bansal do not yield the full partial coloring lemma as in Theorem 5.

Secondly, the above result can tolerate many more stringent constraints than the Entropy method. For instance, the entropy method can only allow O(n/log n) of the sets in S to have discrepancy 1/n, whereas our result can allow Ω(n) of the sets to have such small discrepancy. We believe that this added ﬂexibility in achieving much smaller discrepancy for a constant fraction of sets could be useful elsewhere.

One weakness of Theorem 4 is that we do not strictly speaking get a proper partial coloring: the non {1,−1} variables in our coloring χ can take any value in (−1,1). This however does not appear to be a signiﬁcant drawback, as Corollary 6 can also be made to work from an arbitrary starting point x0 as in the statement of Theorem 4.

- 4 Preliminaries We start with some notation and few elementary properties of the Gaussian distributions.


## 4.1 Notation

Let [n] = {1,... ,n}. Let e1,... ,en denote the standard basis for Rn. We denote random variables by capital letters and distributions by calligraphic letters. We write X ∼ D for a random variable X distributed according to a distribution D.

## 4.2 Gaussian distribution

Let N(µ,σ2) denote the Gaussian distribution with mean µ and variance σ2. A Gaussian distribution is called standard if µ = 0 and σ2 = 1. If G1 ∼ N(µ1,σ12) and G2 ∼ N(µ2,σ22) then for t1,t2 ∈ R we have

t1G1 + t2G2 ∼ N(t1µ1 + t2µ2,t21σ12 + t22σ22).

Let V ⊆ Rn be a linear subspace. We denote by G ∼ N(V ) the standard multi-dimensional Gaussian distribution supported on V : G = G1v1+...+Gdvd, where {v1,... ,vd} is an orthonormal basis for V and G1,... ,Gd ∼ N(0,1) are independent standard Gaussian variables. It is easy to check that this deﬁnition is invariant of the choice of the basis {v1,... ,vd}. We will need the following simple claims.

- Claim 7. Let V ⊆ Rn be a linear subspace and let G ∼ N(V ). Then, for all u ∈ Rn, G,u ∼ N(0,σ2), where σ2 ≤ u 22.

Proof. Let G = G1v1+...+Gdvd where {v1,... ,vd} is an orthonormal basis for V and G1,... ,Gd ∼ N(0,1) are independent. Then G,u = di=1 u,vi · Gi is Gaussian with mean zero and variance

d i=1 u,vi 2 ≤ u 22.

![image 17](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile17.png>)

![image 18](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile18.png>)

![image 19](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile19.png>)

![image 20](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile20.png>)

- Claim 8. Let V ⊆ Rn be a linear subspace and let G ∼ N(V ). Let G,ei ∼ N(0,σi2). Then n i=1 σi2 = dim(V ).


Proof. Let G = G1v1+...+Gdvd where v1,... ,vd are an orthonormal basis for V and G1,... ,Gd ∼ N(0,1) are independent. Then, ni=1 σi2 = ni=1 E[| G,ei  |2] = E[ G 22] = di=1 vi 22 · E[G2i] = d = dim(V ).

![image 21](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile21.png>)

![image 22](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile22.png>)

![image 23](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile23.png>)

![image 24](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile24.png>)

The following is a standard tail bound for Gaussian variables.

- Claim 9. Let G ∼ N(0,1). Then, for any λ > 0, Pr[|G| ≥ λ] ≤ 2exp(−λ2/2).


We will also need the following tail bound on martingales with Gaussian steps. It is a mild generalization of Lemma 2.2 in [Ban10] and we omit the proof.

- Lemma 10 ([Ban10]). Let X1,... ,XT be random variables. Let Y1,... ,YT be random variables where each Yi is a function of Xi. Suppose that for all 1 ≤ i ≤ T, x1,... ,xi−1 ∈ R, Yi|(X1 = x1,X2 = x2,... ,Xi−1 = xi−1) is Gaussian with mean zero and variance at most one (possibly diﬀerent for each setting of x1,... ,xi−1). Then for any λ > 0,

Pr[|Y1 + ... + YT| ≥ λ

√

![image 25](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile25.png>)

T] ≤ 2exp(−λ2/2).

5 Main Partial Coloring Lemma

We are now ready to present our main partial coloring algorithm and prove Theorem 4. We shall use the notation from the theorem statement and Section 2.1.

Let γ > 0 be a small step size so that δ = O(γ log(nm/γ)). We note that the correctness of the algorithm is not aﬀected by the choice of γ, as long as it is small enough; only the running time is aﬀected.

![image 26](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile26.png>)

Let T = K1/γ2, where K1 = 16/3. We assume that δ < 0.1. The algorithm will produce intermediate steps X0 = x0,X1,... ,XT ∈ Rn according to the following update process2

Edge-Walk: For t = 1,... ,T do

- • Let Ctvar := Ctvar(Xt−1) = {i ∈ [n] : |(Xt−1)i| ≥ 1−δ} be the set of variable constraints ‘nearly hit’ so far.
- • Let Ctdisc := Ctdisc(Xt−1) = {j ∈ [m] : | Xt−1 − x0,vj | ≥ cj − δ} be the set of discrepancy constraints ‘nearly hit’ so far.
- • Let Vt := V(Xt−1) = {u ∈ Rn : ui = 0 ∀i ∈ Ctvar, u,vj = 0 ∀j ∈ Ctdisc} be the linear subspace orthogonal to the ‘nearly hit’ variable and discrepancy constraints.
- • Set Xt := Xt−1 + γUt, where Ut ∼ N(Vt). The following lemma captures the essential properties of the random walk.


- Lemma 11. Consider the random walk described above. Assume that mj=1 exp(−c2j/16) ≤ n/16. Then, with probability at least 0.1,


- 1. X0,... ,XT ∈ P.
- 2. |(XT)i| ≥ 1 − δ for at least n/2 indices i ∈ [n].


![image 27](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile27.png>)

2We call the random walk “Edge-Walk” because geometrically, once the walk (almost) hits an edge (face) of the polytope P, it stays on the edge.

Theorem 4 follows immediately from Lemma 11 by setting x = XT. Note that computing Ctvar,Ctdisc, given Xt−1 takes time O(nm). Further, once we know the set of constraints deﬁning Vt, we can sample from N(Vt) in time O((n + m)3) by ﬁrst constructing an orthogonal basis U for Vt and setting Ut = u∈U Guu, where Gu ∼ N are chosen independently.

We prove Lemma 11 in the remainder of this section. We start with a simple observation that Ctvar,Ctdisc can only increase during the random walk.

- Claim 12. For all t < T we have Ctvar ⊆ Ctvar+1 and Ctdisc ⊆ Ctdisc+1. In particular, for 1 ≤ t < T, dim(Vt) ≥ dim(Vt+1).

Proof. Let i ∈ Ctvar. That is, |(Xt−1)i| ≥ 1 − δ. Then by deﬁnition of the random walk, Ut ∈ Vt and (Ut)i = 0. Thus, (Xt)i = (Xt−1)i and i ∈ Ctvar+1. The argument for discrepancy constraints is analogous.

![image 28](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile28.png>)

![image 29](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile29.png>)

![image 30](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile30.png>)

![image 31](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile31.png>)

We next show that the walk stays inside P with high probability.

- Claim 13. For γ ≤ δ/ C log(mn/γ) and C a suﬃciently large constant, with probability at least 1 − 1/(mn)C−2, X0,... ,XT ∈ P.


![image 32](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile32.png>)

Proof. The proof involves a simple application of the tail bound from Claim 9. Clearly X0 = x0 ∈ P. Let Et := {Xt ∈/ P|X0,... ,Xt−1 ∈ P} denote the event that Xt is the ﬁrst element outside P, so Pr[X0,... ,XT ∈ P] = 1 − Tt=1 Pr[Et].

In order to calculate Pr[Et], note that if Et holds then Xt must violate either a variable constraint or a discrepancy constraint. Assume for example that Xt violates a variable constraint, say (Xt)i > 1. Since Xt−1 ∈ P we must have (Xt−1)i ≤ 1. However, we we must in fact have |(Xt−1)i| ≤ 1 − δ as otherwise we would have i ∈ Ctvar and hence (Ut)i = 0 and (Xt)i = (Xt−1)i. Thus, in order for this situation to occur we must have that |(Ut)i| ≥ δ/γ. We will show this is very unlikely.

Let W := {e1,... ,en,v1,... ,vm}. We conclude that if Et holds then | Xt − Xt−1,w  | ≥ δ for some w ∈ W. That is, | Ut,w  | ≥ δ/γ. We next bound the probability of these events. Since Ut ∼ N(Vt) we have by Claim 7 that Ut,w is Gaussian with mean 0 and variance at most 1. Hence by Claim 9,

Pr[| Ut,w  | ≥ δ/γ] ≤ 2exp(−(δ/γ)2/2). By our setting of parameters δ/γ = C log(nm/γ)) and T = O(1/γ2). Thus,

![image 33](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile33.png>)

Pr[X0,... ,XT ∈/ P] =

T

Pr[Et] ≤

t=1

T

γ2 (mn)C ≤

1 (mn)C−2

Pr[| Ut,w  | ≥ δ/γ] ≤ T · (nm) ·

,

![image 34](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile34.png>)

![image 35](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile35.png>)

t=1 w∈W

for C large enough. We are now ready to prove Lemma 11. The intuition behind the proof is as follows. We ﬁrst

![image 36](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile36.png>)

![image 37](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile37.png>)

![image 38](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile38.png>)

![image 39](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile39.png>)

use the hypothesis on the thresholds cj,j ∈ [m], to argue that E[|CTdisc|] ≪ n. This follows from the deﬁnition of the walk and a simple application of the martingale tail bound of Lemma 10. Note that

to prove the lemma it essentially suﬃces to argue that E[|CTvar|] = Ω(n) (we can then use Markov’s inequality). Roughly speaking, we do so by a “win-win” analysis. Consider an intermediate update

step t ≤ T. Then, either |Ctvar| is large, in which case we are done, or |Ctvar| is small in which case dim(Vt−1) is large so that E[ Xt 2] increases signiﬁcantly (with noticeable probability) due to Claim 8. On the other hand, Xt 2 ≤ n as all steps stay within the polytope P (with high

probability). Hence, |Ctvar| cannot be small for many steps and in particular |CTvar| will be large with noticeable probability.

We ﬁrst argue that E[|CTdisc|] is small. That is, on average only a few discrepancy constraints are ever nearly hit.

- Claim 14. E[|CTdisc|] < n/4. Proof. Let J := {j : cj ≤ 10δ}. To bound the size of J, we have

n/16 ≥

j∈J

exp(−c2j/16) ≥ |J| · exp(−100δ2/16) ≥ |J| · exp(−1/16) > 9|J|/10,

and hence |J| ≤ 1.2n/16. Now, for j ∈/ J, if j ∈ CTdisc, then | XT − x0,vj | ≥ cj − δ ≥ 0.9cj. We will bound the probability that this occurs. Recall that XT = x0 + γ(U1 + ... + UT) and deﬁne Yi = Ui,vj . Then, for j ∈/ J, we have

Pr[j ∈ CTdisc] ≤ Pr[|Y1 + ... + YT| ≥ 0.9cj/γ ].

We next apply Lemma 10. Note that the conditions of the lemma apply, since U1,... ,UT is a sequence of random variables, Yi is a function of Ui and Yi|(U1,... ,Ui−1) is Gaussian with mean zero and variance at most one (by Claim 7). Hence,

Pr[j ∈ CTdisc] ≤ 2exp(−(0.9cj)2/2γ2T) = 2exp(−(0.9cj)2/2K1T) < 2exp(−c2j/16). So

E[|CTdisc|] ≤ |J| +

j /∈J

Pr[j ∈ CTdisc] ≤ 1.2n/16 + 2n/16 < n/4.

![image 40](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile40.png>)

![image 41](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile41.png>)

![image 42](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile42.png>)

![image 43](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile43.png>)

- Claim 15. E[ XT 22] ≤ n.

Proof. We will show that E[(XT)2i] ≤ 1 for all i ∈ [n]. Conditioning on the ﬁrst t for which i ∈ Ctvar (or that no such t exists), we get

E[(XT)2i ] = Pr[i ∈/ CTvar]E[(XT)2i |i ∈/ CTvar] +

T

t=1

Pr[i ∈ Ctvar \ Ctvar−1]E[(XT)2i |i ∈ Ctvar \ Ctvar−1].

Clearly E[(XT)2i |i ∈/ CTvar] ≤ 1. For t ≤ T, we have E[(XT)2i |i ∈ Ctvar \ Ctvar−1] = E[(Xt)2i |i ∈ Ctvar \ Ctvar−1] ≤ 1 − δ + γE[|(Ut)i|22] ≤ 1,

where we used the fact that (Ut)i is a Gaussian variable with mean zero and variance at most one (by Claim 7).

![image 44](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile44.png>)

![image 45](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile45.png>)

![image 46](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile46.png>)

![image 47](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile47.png>)

Finally, we show that E[|CTvar|] is large. That is, on average we will nearly hit a constant fraction of the variable constraints.

- Claim 16. E[|CTvar|] ≥ 0.56n.


Proof. We start by computing the average norm of Xt. E[ Xt 22] = E[ Xt−1 + γUt 22] = E[ Xt−1 22] + γ2E[ Ut 22] = E[ Xt−1 22] + γ2E[dim(Vt)],

where we used that fact that given Xt−1, E[Ut|Xt−1] = 0 and E[ Ut 22|Xt−1] = dim(Vt), by Claim 8. Hence, by Claim 15,

n ≥ E[ XT 22] ≥ γ2

T

E[dim(Vt)] ≥ γ2|T|·E[dim(VT)] = K1·E[dim(VT)] = K1E[(n−|CTvar|−|CTdisc|)].

t=1

Therefore, E[|CTvar|] ≥ n(1 − 1/K1) − E[|CTdisc|] ≥ n(1 − 1/K1 − 1/4) > (0.56)n, where the second inequality follows from Claim 14.

![image 48](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile48.png>)

![image 49](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile49.png>)

![image 50](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile50.png>)

![image 51](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile51.png>)

Lemma 11 now follows immediately from Claim 13 and Claim 16.

Proof of Lemma 11. From Claim 16 and the fact that |CTvar| ≤ n, it follows that P[|CTvar| ≥ n/2] ≥ 0.12. Combining with Claim 13, with probability at least 0.12 − 1/poly(m,n) > 0.1, |CTvar| ≥ n/2 and XT ∈ P which shows the lemma.

![image 52](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile52.png>)

![image 53](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile53.png>)

![image 54](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile54.png>)

![image 55](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile55.png>)

# 6 Discrepancy Minimization from Partial Coloring We now derive Theorem 2 and Theorem 3 from our partial coloring lemma.

- Proof of Theorem 2. Let (V,S) be a system with |V | = n and |S| = m. Let v1,... ,vm ∈ Rn be the indicator vectors of the sets in S. We set δ = 1/(8log m). Let α(m,n) = 8 log(m/n). Then, m · exp(−α(m,n)2/16) < n/16. Therefore, by Theorem 4 applied to v1,... ,vm and starting point x0 = 0n, with probability at least 0.1 we ﬁnd a vector x1 ∈ [−1,1]n such that | vj,x1 | < √n · α(m,n) for all j ∈ m and |{i : |(x1)i| ≥ 1 − δ}| ≥ n/2. We can boost this probability further by repeating the algorithm O(log n) times; from now on we will ignore the probability that the algorithm does not ﬁnd such a vector.


![image 56](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile56.png>)

![image 57](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile57.png>)

Let I1 = {i : |(x1)i| < 1 − δ} be the coordinates not ‘ﬁxed’ in the ﬁrst step and set n1 = |I1|. We now iteratively apply Theorem 4 to the restricted system described by the vectors v11 = (v1)I1,... ,vm1 = (vm)I1 ∈ Rn1 and starting point (x1)I1 to get another vector x2 ∈ [−1,1]n1 such that | vj1,x2 | < √n1 · α(m,n1) for all j ∈ [m] and |{i : |(x2)i| ≥ 1 − δ}| ≥ n1/2. By iterating this procedure for at most t = 2log n times and concatenating the resulting vectors appropriately we get x ∈ Rn such that |xi| ≥ 1 − δ for all i ∈ [n] and for every j ∈ [m],

![image 58](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile58.png>)

| vj,x  | < √n · α(m,n) + √n1 · α(m,n1) + ··· + √nt · α(m,nt) < √n

![image 59](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile59.png>)

![image 60](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile60.png>)

![image 61](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile61.png>)

∞

![image 62](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile62.png>)

8 log(m · 2r/n) 2r/2 < C n · log(m/n),

![image 63](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile63.png>)

![image 64](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile64.png>)

r=0

![image 65](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile65.png>)

for C a universal constant. We now round x to get a proper coloring χ ∈ {1,−1}n. Let χ ∈ {1,−1}n be obtained from x

- as follows: for i ∈ [n], χi = sign(xi) with probability (1 + |xi|)/2 and −sign(xi) with probability


(1 − |xi|)/2, so that E[χi] = xi. Let Y = χ − x. Fix some j ∈ [m]. Then, the discrepancy of χ with vj is

![image 66](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile66.png>)

| χ,vj  | ≤ | x,vj  | + | Y,vj  | ≤ C nlog(m/n) + | Y,vj  |. We will show that with high probability, | Y,vj | ≤

√n for all 1 ≤ j ≤ m. Fix some j ∈ [m] and consider Y,vj . We have that |Yi| ≤ 2, E[Yi] = 0 and Var(Yi) ≤ δ. We also have vj 2 ≤

![image 67](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile67.png>)

√n and vj ∞ ≤ 1. Thus, by a standard Chernoﬀ bound (see e.g., Theorem 2.3 in [CL06]),

![image 68](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile68.png>)

√

![image 69](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile69.png>)

![image 70](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile70.png>)

P | Y,vj | > 2 2log m ·

nδ ≤ 2exp(−2log m) < 1/2m.

Therefore, by the union bound and our choice of δ, with probability at least 1/2 we have that | Y,vj | ≤

√n for all 1 ≤ j ≤ m. Therefore, | χ,vj | ≤ C nlog(m/n) + √n for all 1 ≤ j ≤ m.

![image 71](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile71.png>)

![image 72](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile72.png>)

![image 73](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile73.png>)

The running time is dominated by the O(log2 n) uses of Theorem 4. Thus, the total running time is O((n + m)3 log5(mn)) = O˜((n + m)3).

![image 74](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile74.png>)

![image 75](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile75.png>)

![image 76](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile76.png>)

![image 77](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile77.png>)

The constant in the theorem can be sharpened to be 13 by ﬁne tuning the parameters. We do not dwell on this here. We next prove Theorem 3.

- Proof of Theorem 3. The proof is similar to the above argument and we only sketch the full proof. Set δ = 1/n. Let (V,S) be the set system. Let v1,... ,vm be the indicator vectors of the sets in S and let cj = C√t/ vj 2 for C to be chosen later. Observe that j vj 22 ≤ nt as each element


![image 78](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile78.png>)

appears in at most t sets. In particular, the number of vectors vj with vj 22 in [2rt,2r+1t] is at most n/2r. Therefore,

j

exp(−c2j/16) <

∞

n · exp(−C2/16 · 2r+1) 2r

< n/16,

![image 79](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile79.png>)

r=0

for C a suﬃciently large constant. Thus, by applying Theorem 4 to the vectors vj and thresholds cj for j ∈ [m], with probability at least 0.1 we get a vector x1 ∈ [−1,1]n such that | vj,x1 | < C√t for all j ∈ [m] and |{i : |(x1)i| ≥ 1 − δ}| > n/2.

![image 80](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile80.png>)

By iteratively applying the same argument as in the proof of Theorem 4 for 2log n steps, we get a vector x ∈ [−1,1]n with |xi| ≥ 1 − δ for all i and | vj,x  | < 2C√tlog n for all j ∈ [m]. The theorem now follows by rounding the x to the nearest integer coloring χ: χi = sign(xi) for all i ∈ [m].

![image 81](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile81.png>)

![image 82](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile82.png>)

![image 83](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile83.png>)

![image 84](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile84.png>)

![image 85](<2012-lovett-constructive-discrepancy-minimization-walking_images/imageFile85.png>)

Acknowledgments We would like to thank Oded Regev for many discussions and collaboration

- at the early stages of this work. We thank Joel Spencer for his encouragement and enthusiasm about this work: part of our presentation is inspired by a lecture he gave on this result at the Institute for Advanced Study, Princeton. We also thank him for the observation on improving the run time of Theorem 4 and allowing us to include it here. We thank Nikhil Bansal for valuable comments and discussions.


# References

[AS11] N. Alon and J.H. Spencer. The Probabilistic Method. Wiley Series in Discrete Mathematics and Optimization. John Wiley & Sons, 2011.

[Ban98] Wojciech Banaszczyk. Balancing vectors and gaussian measures of n-dimensional convex bodies. Random Struct. Algorithms, 12(4):351–360, 1998.

[Ban10] Nikhil Bansal. Constructive algorithms for discrepancy minimization. In FOCS, pages 3–10, 2010.

[Bec81] J. Beck. Roths estimate of the discrepancy of integer sequences is nearly sharp. Combinatorica, 1(4):319–325, 1981.

[BF81] J. Beck and T. Fiala. Integer-making theorems. Discrete Applied Mathematics, 3(1):1–8, 1981.

[Cha02] B. Chazelle. The Discrepancy Method: Randomness and Complexity. Cambridge University Press, 2002.

[CL06] Fan Chung and Linyuan Lu. Complex Graphs and Networks. American Mathematical Society, 2006.

- [Mat98] Jirı´ Matousˇek. An lp version of the beck-ﬁala conjecture. Eur. J. Comb., 19(2):175–182, 1998.
- [Mat99] J. Matousˇek. Geometric Discrepancy: An Illustrated Guide. Algorithms and Combinatorics. Springer, 1999.


[Spe85] Joel Spencer. Six standard deviations suﬃce. Transactions of the American Mathematical Society, 289(2):679–706, 1985.

[Sri97] A. Srinivasan. Improving the discrepancy bound for sparse matrices: Better approximations for sparse lattice approximation problems. In ACM-SIAM Symposium on Discrete Algorithms, pages 692–701, 1997.

