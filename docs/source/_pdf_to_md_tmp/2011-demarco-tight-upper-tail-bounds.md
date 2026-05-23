arXiv:1111.6687v2[math.PR]9Nov2012

Tight upper tail bounds for cliques

B. DeMarco∗ and J. Kahn†

Abstract

With ξk = ξkn,p the number of copies of Kk in the usual (Erd˝osR´enyi) random graph G(n,p), p ≥ n−2/(k−1) and η > 0, we show when k > 1

)} . This is tight up to the value of the constant in the exponent.

Pr(ξk > (1 + η)Eξk) < exp −Ωη,k min{n2pk−1 log(1/p),nkp(

k 2

# 1 Introduction

Let G(n,p) be the Erd˝os-Re´nyi random graph on n vertices, in which every edge occurs independently with probability p, and let H be a ﬁxed graph with vH = |V (H)| and eH = |E(H)|. A copy of H in G(n,p) is any subgraph of G(n,p) isomorphic to H. It has been a long studied question (e.g. [5, 6, 11, 12, 13, 15, 17]) to estimate, for η > 0 and ξH = ξHn,p the number of copies of H in G(n,p),

Pr(ξH > (1 + η)EξH) . (1)

To avoid irrelevancies, let us declare at the outset that we always assume

- p ≥ n−1/mH, where, as usual (e.g. [10, p.6]), mH = max{eK/vK : K ⊆ H} (2)


(so n−1/mH is a threshold for “G ⊇ H”; see [10, Theorem 3.4]); in particular, when H = Kk we assume p ≥ n−2/(k−1). For smaller p the problem is not

![image 1](<2011-demarco-tight-upper-tail-bounds_images/imageFile1.png>)

AMS 2000 subject classiﬁcation: 60F10, 05C80 Key words and phrases: upper tails, large deviations, random graphs, subgraph counts

* supported by the U.S. Department of Homeland Security under Grant Award Number 2007-ST-104-000006.

† Supported by NSF grant DMS0701175.

very interesting (e.g. for bounded η the probability in (1) is easily seen to be Θ(min{nvKpeK : K ⊆ H,eK > 0}); see [10, Theorem 3.9] for a start), and we will not pursue it here.

Janson and Rucin´ski [12] oﬀer a nice overview of the methods used prior to 2002 to obtain upper bounds on the probability in (1), by far the more challenging part of the problem. To get an idea of the diﬃculty, note that even for the case that H is a triangle, only quite poor upper bounds were known until a breakthrough result of Kim and Vu [15], who used, inter alia, the “polynomial concentration” machinery of [14] to show, for p > n−1 log n,

expp[Oη(n2p2)] < Pr(ξH > (1 + η)EξH) < exp[−Ωη(n2p2)]. (3)

(The easy lower bound, seemingly ﬁrst observed in [17], is, for example, the probability of containing a complete graph on something like (1 + η)1/3np vertices. Of course the subscript η in the lower bound is unnecessary if, for example, η ≤ 1, which is what we usually have in mind.) Polynomial concentration was also used by Vu [16] to show that if H is strictly balanced and EξH ≤ log n, then

Pr(ξH > (1 + η)EξH) < exp[−Ωη(EξH)]. (4)

The result of [15] was vastly extended in a beautiful paper of Janson, Oleszkiewicz and Rucin´ski [11], where it was shown that for any H and η,

expp[OH,η(MH(n,p))] < Pr(ξH > (1 + η)EξH) < exp[−ΩH,η(MH(n,p))],

(5) thus determining the probability (1) up to a factor O(log(1/p)) in the exponent for constant η. A deﬁnition of M is given in Section 10; for now we just mention that (for p ≥ n−2/(k−1)) MKk(n,p) = n2pk−1. (It should also be noted that in the limited range where it applies, the upper bound in (4) is better than the one in (5).)

While it seems natural to expect that the lower bound in (5) is “usually” the truth (see Section 10 for a precise guess), the only progress in this direction until quite recently was [13], which established the upper bound exp[−Ω(MH(n,p)log1/2(1/p))] for H = K4 or C4 (the 4-cycle) and some values of p.

The log(1/p) gap was ﬁnally closed for the case H = K3 by Chatterjee [5] and, independently, the present authors [6]. More precisely, [5] showed that for a suitable C depending on η and p > Cn−1 log n,

Pr(ξK3 > (1 + η)EξK3) < pΩη(n2p2), while [6] showed, somewhat more generally, that for p > n−1,

exp[−Oη(f(3,n,p))] < Pr(ξK3 > (1 + η)EξK3) < exp[−Ωη(f(3,n,p))],

where f(k,n,p) := min{n2pk−1 log(1/p),nkp(k2)}. (In what follows we will often abbreviate f(k,n,p) = f(k,n).)

In this paper we considerably extend the method of [6] to settle the problem for general cliques and a bit more.

- Theorem 1.1. Assume H on k vertices has minimum degree at least k − 2 (that is, the complement of H is a matching). Then for all η > 0 and

p ≥ n−2/(k−1), Pr(ξH ≥ (1 + η)E(ξH)) ≤ exp [−Ωη,H(f(k,n,p))] .

- Theorem 1.2. For H = Kk and for all p ≥ n−2/(k−1), Pr(ξH ≥ 2E(ξH)) ≥ exp [−OH(f(k,n,p))] .


Remarks. 1. We are most interested in the “nonpathological” range where f(k,n,p) = n2pk−1 log(1/p), so when p ≥ n−2/(k−1)(log n)2/[(k−1)(k−2)] (or a bit less). It may be helpful to think mainly of this range as we proceed.

- 2. Though mainly concerned with the case H = Kk in Theorem 1.1, we prove the more general statement for inductive reasons. For noncliques the bound of Theorem 1.1 is not usually tight; more precisely: it is tight (up


to the constant in the exponent) if p = Ω(1) or if ∆ := ∆H = k − 1 and p = Ω(n−1/∆), in which cases our upper bound agrees with the lower bound in (5); it is not tight if ∆ = k −2 and p = o(1) (see the proof of Lemma 2.4) or if H = Kk and p < n−c/∆ for some ﬁxed c > 1 (see the proof of Lemma 2.5; in fact p = o(n−1/∆) is probably enough here—which would complete this little story—but we don’t quite show this).

In the next section we show that Theorem 1.1 follows from an analogous assertion for k-partite graphs; most of the paper (Sections 3-8) is then concerned with this modiﬁed problem. Section 9 gives the proof of Theorem

- 1.2 and Section 10 contains a few concluding remarks.


# 2 Reduction

For the rest of the paper we set t = log(1/p) and take H to be a graph with vertices v1,v2,... ,vk. We deﬁne G = G(n,p,H) to be the random graph with vertex set V = V1 ∪ ··· ∪ Vk, where the Vi’s are disjoint n-sets and Pr(xy ∈ E(G)) = p whenever x ∈ Vi and y ∈ Vj for some vivj ∈ E(H), these choices made independently. We deﬁne a copy of H in G to be a set of vertices {x1,... ,xk} with xi ∈ Vi and xixj ∈ E(G) whenever vivj ∈ E(H); use XHn,p for the number of such copies; and set Ψ(H,n,p) = E(XHn,p) = nkpeH. When there is no danger of confusion we will often use XHn —or, for typographical reasons X(H,n)—for XHn,p and Ψ(H,n) for Ψ(H,n,p).

The next two propositions show an equivalence between G(n,p) and

- G with regard to upper tails for subgraph counts. In each we set α =


|Aut(H)|nk/(kn)k ∼ k−k|Aut(H)| (where as usual (a)b = a(a − 1)··· (a − b + 1)).

- Proposition 2.1. For η > 0 and ε = η/(2 + η),

Pr(XHn,p ≥ (1 + ε)Ψ(H,n,p)) >

αε 1 − α + αε

![image 2](<2011-demarco-tight-upper-tail-bounds_images/imageFile2.png>)

Pr(ξHkn,p ≥ (1 + η)E(ξHkn,p))

We omit the proof of Proposition 2.1 since it is a straightforward generalization of the case H = K3 proved in [6].

- Proposition 2.2. For any ε > 0 there is a C = Cε,H such that for p > Cn−1/mH,


Pr XHn,p ≥ (1 + ε)Ψ(H,n,p) < 2Pr(ξHkn,p ≥ (1 + αε/2)E(ξHkn,p)).

(See (2) for mH.) Proof. We may choose G∗ = G(kn,p) by ﬁrst choosing G = G(n,p,H) and then letting

E(G∗) = E(G) ∪ S

where Pr(xy ∈ S) = p whenever x = y, x ∈ Vi and y ∈ Vj for some vivj  ∈ E(H), these choices made independently. Write ξ and X for the numbers

of copies of H in G∗ and G respectively (thus ξ = ξHkn,p and X = XHn,p), and set ξ∗ = ξ − X. Since EX = αEξ, we have, using Harris’ Inequality,

Pr(ξ > (1 + αε2 )Eξ) ≥ Pr(X > (1 + ε)EX)Pr(ξ∗ > Eξ∗ − αε2 Eξ); (6)

![image 3](<2011-demarco-tight-upper-tail-bounds_images/imageFile3.png>)

![image 4](<2011-demarco-tight-upper-tail-bounds_images/imageFile4.png>)

so we need to say that the second probability on the right is at least 1/2. This is standard, but we summarize the argument for completeness.

A result of Janson from [9] (see [10, (2.14)]) gives

Pr(ξ∗ ≤ Eξ∗ − t) < exp[−2t∆2¯ ], (7) with

![image 5](<2011-demarco-tight-upper-tail-bounds_images/imageFile5.png>)

∆¯ = ∗σ∼τ EIσIτ ≤ σ∼τ EIσIτ, (8) where (recycling notation a little) H1,... are the copies of H in Kkn; Iσ = 1{Hσ⊆G∗}; “σ ∼ τ” means Hσ and Hτ share an edge (so σ ∼ σ); and ∗ means we sum only over σ,τ for which Hσ,Hτ cannot appear in G. But (very wastefully),

∆¯ < nvH {nvH−vKp2eH−eK : K ⊆ H,eK > 0} < n2vHp2eH {n−vK(Cn−1/mH)−eK : K ⊆ H,eK > 0}

= O(C−1E2ξ),

where C is the constant from (9), which may be taken large compared to the implied constant in “O(·).” Thus, using (7) with the above bound on ∆¯ and t = (αε/2)Eξ, we ﬁnd that the second probability on the right side of (6) is at least 1 − exp[−Ω((αε)2C)] > 1/2.

![image 6](<2011-demarco-tight-upper-tail-bounds_images/imageFile6.png>)

According to Proposition 2.1, Theorem 1.1 will follow from the corresponding k-partite statement, viz. Theorem 2.3. If H has minimum degree at least k − 2, then

- (a) for all ε > 0,

Pr XHn,p ≥ (1 + ε)Ψ(H,n,p) < exp [−ΩH,ε (f(k,n,p))];

- (b) for any τ ≥ 1,


Pr XHn,p ≥ 2τΨ(H,n,p) < exp[−ΩH(f(k,nτ1/k,p))].

Note that (b) for a given H follows from (a), since (noting that τΨ(H,n) = Ψ(H,nτ1/k) and using (a) for the second inequality)

Pr(XHn ≥ 2τΨ(H,n)) ≤ Pr XHnτ1/k ≥ 2Ψ(H,nτ1/k) ≤ exp −ΩH f(k,nτ1/k,p) . We include (b) because it will be needed for induction; that is, for a given

- H we just prove (a), occasionally appealing to earlier cases of (b).


We have formulated the theorem for all p so that the inductive parts of the proof don’t require checking that p falls in some suitable range. Note, however, that for the proof we can assume (for our choice of positive constants C and c depending on H and ε)

p > Cn−2/(k−1), (9) since for smaller p (> n−1/mH) the theorem is trivial, and

p < c, (10)

since above this the desired bound is given by (5). As detailed in the next two lemmas, (5), together with some auxiliary results from [11], also allows us to ignore certain other cases of Theorem 2.3(a).

- Lemma 2.4. If ∆H ≤ k − 2 then

Pr XHn,p ≥ (1 + ε)Ψ(H,n,p) ≤ pΩH,ε(n2pk−1). Proof. By Proposition 2.2, it is enough to show

Pr ξHn,p ≥ (1 + ε)E(ξHn,p) ≤ pΩH,ε(n2pk−1); (11) but this follows from (5), which since MH(n,p) ≥ n2p∆H (see [11, Lemma

- 6.2]), bounds the left side of (11) by exp[−ΩH,ε(n2p∆H)] ≤ exp[−ΩH,ε(n2pk−1t)].


![image 7](<2011-demarco-tight-upper-tail-bounds_images/imageFile7.png>)

- Lemma 2.5. For any H = Kk on k vertices and γ > 0, if p < n−(1+γ)/(k−1) then


Pr(XHn ≥ (1 + ε)Ψ(H,n)) < pΩH,ε,γ(n2pk−1).

Proof. By Lemma 2.4 we may assume ∆ := ∆H = k − 1 (and will write ∆ in place of k − 1 in this section). By Proposition 2.2 it’s enough to show

Pr(ξHn,p ≥ (1 + ϑ)E(ξHn,p)) < pΩϑ,H(n2p∆),

which, in view of (5) and the deﬁnition of MH(n,p), will follow if we show that, for any K ⊆ H, nvKpeK = Ω((n2p∆t)α∗K), or, more conveniently,

nvK−2α∗KpeK−∆α∗K = Ω(tα∗K). (12) We need one easy observation from [11] (see their Lemma 6.1):

eK ≤ ∆(vK − α∗K).

Then, noting that

eK − ∆α∗K < 0 (13)

(since eK < ∆vK/2 ≤ ∆α∗K) and using our upper bound on p, we ﬁnd that the left side of (12) is at least

nvK−2α∗K−(1+γ)(eK−∆α∗K)/∆ ≥ nvK−2α∗K−(vK−2α∗K)+γ(∆α∗K−eK)/∆

= nγ(∆α∗K−eK)/∆, which (again using (13)) gives (12).

![image 8](<2011-demarco-tight-upper-tail-bounds_images/imageFile8.png>)

# 3 Large deviations

This section collects a few standardish large deviation basics that will be used throughout the paper. It’s perhaps worth noting that these elementary inequalities are the only “machinery” we will need.

We use B(m,α) for a random variable with the binomial distribution Bin(m,α). The next lemma, which is easily derived from [2, Theorem A.1.12] and [10, Theorem 2.1] respectively (for example), will be used repeatedly, eventually without explicit mention.

- Lemma 3.1. There is a ﬁxed C > 0 so that for any λ ≤ 1, K > 1 + λ, m and α,


Pr(B(m,α) ≥ Kmα) < min{(e/K)Kmα,exp[−Cλ2Kmα]}. (14)

Remark. We may assume Kmα ≥ 1. Thus, if emαc < 1 then e/K < α1−c and the bound in (14) is at most α(1−c)Kmα.

The next lemma, an immediate consequence of Lemma 3.1 (and the above Remark), will also be used repeatedly, usually following a preliminary application of Lemma 3.1 to justify the assumption enqc < 1.

- Lemma 3.2. Fix c < 1 and assume enqc < 1. If S ⊆ Vi is random with Pr(x ∈ S) ≤ q ∀x ∈ Vi, these events independent, then for any T,

Pr(|S| ≥ T) < q(1−c)T.

We also need the following inequality, which is an easy consequence of, for example, [3, Lemma 8.2].

- Lemma 3.3. Suppose w1,... ,wm ∈ [0,z]. Let ξ1,... ,ξm be independent Bernoullis, ξ = ξiwi, and Eξ = µ. Then for any η > 0 and λ ≥ ηµ,

Pr(ξ > µ + λ) < exp[−Ωη(λ/z)].

- 4 Outline


In this section we list the steps in the proof of Theorem 2.3(a), ﬁlling in some deﬁnitions as we go along. The proof proceeds by induction on (say) k2 + eH, so that in proving the statement for H we may assume its truth for all graphs with either fewer than k vertices or with k vertices and fewer than eH edges. The case k = 2 is trivial and k = 3 is the main result of [6], so we assume throughout that k ≥ 4.

Most of the proof (Lemmas 4.1-4.3) consists of identifying certain anomalies, for example vertices of unusually high degree, and bounding the number of copies of H in which they appear. The remaining copies are then easily handled (in Lemma 4.4) using Lemma 3.3.

Here and throughout we use C and Cε for (positive) constants depending on (respectively) H and (H,ε), diﬀerent occurrences of which will usually denote diﬀerent values. Similarly, we use Ω and Ωε as shorthand for ΩH and ΩH,ε. We say an event E occurs with large probability (w.l.p.) if Pr(E) > 1 − exp[−Ωε(n2pk−1t)], and write “α <∗ β” for “w.l.p. α < β” (where ε is as in the statement of the theorem). Note that (9) (with a suitable C) guarantees that an intersection of, for example, n5 w.l.p. events is itself a w.l.p. event, a fact we will sometimes use without mention in what follows.

By Lemma 2.4 we may assume ∆H = k − 1. We reorder the vertices of H so that k − 1 = d(v1) ≥ d(v2) ≥ ... ≥ d(vk) and if d(v2) = k − 2 then

v2  ∼ v3. We set A = V1,B = V2,C = V3 and always take a,b and c to be elements of A,B and C respectively. For disjoint X,Y ⊆ V we use ∇(X,Y ) for the set of edges with one end in each of X and Y , and ∇(X) for the set of edges with one end in X. We use N(x) for the neighborhood of (set of vertices adjacent to) a vertex x.

For K ⊆ H with vertex set {vi : i ∈ T} (T ⊆ [k]), deﬁne a copy of K in G (= G(n,p,H)) to be a set of vertices {xi : i ∈ T} with xi ∈ Vi and xixj ∈ E(G) whenever vivj ∈ E(K). For x1,x2,... ,xl vertices belonging to distinct Vi’s we use wK(x1,... ,xl) for the number of copies of K containing x1,... ,xl; when K = H we call this the weight of {x1,... ,xl}. We use HS = H −{vi : i ∈ S} (S ⊂ [k]), and abbreviate H{i} = Hi, wHS(·) = wS(·), w{i} = wi and w∅(·) (= wH(·)) = w(·).

Set ϑ = .05ε and deﬁne δ by (1 + δ)k = 2. For x ∈ V and i ∈ [k], let di(x) = |N(x) ∩ Vi|, and set d(x) = max{di(x) : i ∈ [k]}. Say a vertex x is high degree if d(x) > (1 + δ)np, and a copy of H is type one if contains a high degree vertex from A,B or C.

- Lemma 4.1. W.l.p. G contains less than 7ϑΨ(H,n) type one copies of H.

Let A′,B′,C′ denote the subsets of A,B,C respectively of vertices which are not high degree. For vertices x,y ∈ G let dj(x,y) = |N(x) ∩ N(y) ∩ Vj| and d(x,y) = maxj≥4 dj(x,y). A pair of vertices (x,y) is high degree if d(x,y) > np3/2. For k > 4 a copy of H is type two if it contains a high degree pair (x,y) belonging to either A′ × C′ or B′ × C′; for k = 4 we don’t need this, and simply declare that there are no copies of type two.

- Lemma 4.2. W.l.p. G contains less than 2ϑΨ(H,n) type two copies of H.

Set s = min{t,nk−2p

k−1

2 }, the two regimes corresponding to the two ranges of f(k,n,p) (= n2pk−1s). Deﬁne w∗(·) in the same way as w(·), but with the count restricted to copies of H that are not type one or two. Set

ζ =

3k−2Ψ(H,n,p)/(n2pk−1s) if k ≥ 5 225Ψ(H,n,p)/(n2p3s) if k = 4

(15)

and (in either case) say ab ∈ ∇(A,B) is heavy if w∗(a,b) > ζ. Finally, say a copy of H is type three if it is not type one or two and contains a heavy edge, and type four if it is not type one, two or three.

- Lemma 4.3. W.l.p. G contains less than 4ϑΨ(H,n) type three copies of H.


- Lemma 4.4. With probability at least 1 − exp[−Ωε(f(k,n,p))] G contains less than (1 + 2ϑ)Ψ(H,n) type four copies of H.

Of course Theorem 2.3(a) (for k ≥ 4) follows from Lemmas 4.1-4.4; these are proved in the next four sections.

- 5 Proof of Lemma 4.1


For i ∈ [3] set D1(i) = {x ∈ Vi : d(x) > np2/5} and D2(i) = {x ∈ Vi : np2/5 ≥ d(x) > (1 + δ)np}, and for j ∈ [2] set Sj(i) = {d(x) : x ∈ Dj(i)}. We will show

- Proposition 5.1. For all 1 ≤ i ≤ 3,

w.l.p. ∀x ∈ Dj(i), w(x)/d(x) <

2nk−2peH−(k−1) if j = 1 2nk−2peH−k+2(k−1)/5 if j = 2

and

- Proposition 5.2. For all 1 ≤ i ≤ 3,


ϑn2pk−1 if j = 1 kn2pk−1t if j = 2.

w.l.p. Sj(i) <

(16)

The lemma follows since the number of type one copies of H is at most

3

(S1(i) · 2nk−2peH−(k−1) + S2(i) · 2nk−2peH−k+2(k−1)/5)

w(x) <∗

i=1

x:xhigh degree

<∗ 3(2ϑΨ(H,n) + 2kΨ(H,n)p2(k−1)/5−1t) < 7ϑΨ(H,n),

using Propositions 5.1 and 5.2 for the ﬁrst and second inequalities.

![image 9](<2011-demarco-tight-upper-tail-bounds_images/imageFile9.png>)

- Proof of Proposition 5.1. Fix i and condition on ∇(Vi) (thus determining D1(i) and D2(i)). If dH(vi) = k −1, then for any x ∈ D1(i), induction gives


Pr(w(x) ≥ 2Ψ(Hi,d(x))) < exp[−Ω(f(k − 1,d(x)))], whence (noting Ψ(Hi,·) = Ψ(H1,·))

Pr(∃x ∈ D1(i) : w(x) ≥ 2Ψ(H1,d(x))) < nexp[−Ω(f(k − 1,np2/5))] < pn2pk−1. (17)

Similarly,

2/5

Pr(∃x ∈ D2(i) : w(x) ≥ 2Ψ(H1,np2/5)) < nPr(Xnp

Hi ≥ 2Ψ(Hi,np2/5)) < nexp[−Ω(f(k − 1,np2/5))] < pn2pk−1 (18)

Note that, here and throughout, we omit the routine veriﬁcations of inequalities like those in the last lines of (17) and (18).

If d(vi) = k − 2, then vi  ∼ vj for some j ∈ [k]. We partition Vj = P1 ∪ ··· ∪ P⌊1/p⌋ with each Pℓ of size at most (1 + δ)np, and write wℓ(x) for the number of copies of H containing x and meeting Pℓ. Noting that here Ψ(H1,·) = p−1Ψ(Hi,·) (and w(x) = ℓ wℓ(x)), we have

Pr (w(x) ≥ 2Ψ(H1,d(x))) < Pr(∃ℓ wℓ(x) ≥ 2Ψ(Hi,d(x)))

< p−1 exp [−Ω(f(k − 1,d(x)))] for a given x, so that

Pr(∃x ∈ D1(i) : w(x) ≥ 2Ψ(H1,d(x))) < np−1 exp −Ω(f(k − 1,np2/5)) < pn2pk−1, (19)

and Pr(∃x ∈ D2(i) : w(x) ≥ 2Ψ(H1,np2/5)) < np−1 Pr(Xnp

2/5

Hi ≥ 2Ψ(Hi,np2/5)) < np−1 exp[−Ω(f(k − 1,np2/5))] < pn2pk−1. (20)

Finally, (17)-(20) imply that w.l.p. w(x)/d(x) < 2Ψ(H1,d(x))/d(x) = 2(d(x))k−1peH−(k−1)/d(x)

≤ 2nk−2peH−(k−1) ∀x ∈ D1(i) and

w(x)/d(x) < 2Ψ(H1,np2/5)/d(x) = 2(np2/5)k−1peH−(k−1)/d(x) ≤ 2nk−2peH−k+2(k−1)/5 ∀x ∈ D2(i).

![image 10](<2011-demarco-tight-upper-tail-bounds_images/imageFile10.png>)

- Proof of Proposition 5.2. We bound |∇(Dj(i))|, which is, of course, an upper bound on Sj(i). We ﬁrst assert that, for any i ∈ [3], w.l.p.


|D1(i)| < ϑnpk−7/5 and |D2(i)| < npk−2t. (21)

This will follow from Lemmas 3.1 and 3.2 (so really two applications of Lemma 3.1), a combination we will see repeatedly. For a given i and j the events {x ∈ Dj(i)} (x ∈ Vi) are independent with (using Lemma 3.1)

Pr(x ∈ D1(i)) < k Pr(B(n,p) > np2/5) < k(ep3/5)np2/5 < p0.5np2/5 and

Pr (x ∈ D2(i)) < k Pr(B(n,p) > (1 + δ)np) < exp[−Ω(np)]. An application of Lemma 3.2 now shows that (21) holds w.l.p.

![image 11](<2011-demarco-tight-upper-tail-bounds_images/imageFile11.png>)

Assume then that (21) holds, and for convenience rename its bounds ϑnpk−7/5 = r and npk−2t = u; we may of course assume r ≥ 1 if proving the ﬁrst bound in (16) and u ≥ 1 if proving the second. We have (a bit crudely)

Pr(|∇(D1(i))| ≥ ϑn2pk−1) < Pr(∃T ∈ Vr(i) : |∇(T)| ≥ ϑn2pk−1) < nr Pr(B((k − 1)rn,p) ≥ ϑn2pk−1) < nr(e(k − 1)p3/5)ϑn2pk−1 < pΩε(n2pk−1)

and

Pr(|∇(D2(i))| ≥ kn2pk−1t) < Pr(∃T ∈ Vu(i) : |∇(T)| ≥ kn2pk−1t) < nu Pr(B((k − 1)un,p) ≥ kn2pk−1t) < nu exp[−Ω(n2pk−1t)]

< pΩ(n2pk−1), with the third inequality in each case given by Lemma 3.1.

![image 12](<2011-demarco-tight-upper-tail-bounds_images/imageFile12.png>)

# 6 Proof of Lemma 4.2

(Here we are only interested in k ≥ 5.) We bound the contribution of highdegree (A′,C′)-pairs, the argument for (B′,C′)-pairs being similar.

Let A′′ be the (random) set of vertices of A′ involved in high-degree (A′,C′)pairs—that is, A′′ = {a ∈ A′ : ∃c ∈ C′ d(a,c) > np3/2}—and deﬁne C′′ similarly. We will show that

w.l.p. |A′′|,|C′′| < npk−5/2 (22) and

w.l.p. w(a,c) < 2tΨ(H{1,3},(1 + δ)np) ∀(a,c) ∈ A′ × C′. (23) Combining these we ﬁnd that the total weight of high degree (A′,C′)-pairs is w.l.p. at most

(npk−5/2)22tΨ(H{1,3},(1 + δ)np) < 4n2p3k−7tΨ(H{1,3},n) < ϑΨ(H,n),

where the second inequality uses Ψ(H{1,3},n) ≤ n−2p−(2k−3)Ψ(H,n) and 4pk−4t < ϑ (see (10)). Since, as noted above, the same argument shows that the contribution of high-degree (B′,C′)-pairs is w.l.p. at most ϑΨ(H,n), the lemma follows.

- Proof of (22). Given ∇(C), the events {a ∈ A′′} are independent, with Pr a ∈ A′′ < n(k − 2)Pr[B((1 + δ)np,p) > np3/2]

< n(k − 2)(e(1 + δ)p1/2)np3/2 < p0.4np3/2 =: q,

where we use (9), (10) and k ≥ 5 for the last inequality. Thus, since enq1/2 < 1, Lemma 3.2 gives (22) for A′′, and of course the same argument applies to C′′.

![image 13](<2011-demarco-tight-upper-tail-bounds_images/imageFile13.png>)

- Proof of (23). Here we have lots of room and just bound max{w3(a) : a ∈ A′}, a trivial upper bound on max{w(a,c) : a ∈ A′,c ∈ C′}. Since


d(a) < (1 + δ)np (for a ∈ A′) and v1 ∼ vℓ ∀ℓ ∈ [k] \ {2,3}, Theorem 2.3(b) gives (inductively)

Pr[∃a ∈ A′ w3(a) ≥ 2tΨ(H{1,3},(1 + δ)np)] < nexp[−Ω(f(k − 2,(1 + δ)npt

1 k−2

))] < pΩ(n2pk−1)

![image 14](<2011-demarco-tight-upper-tail-bounds_images/imageFile14.png>)

(with veriﬁcation of the second inequality, which does need (9) at one point, again left to the reader).

![image 15](<2011-demarco-tight-upper-tail-bounds_images/imageFile15.png>)

# 7 Proof of Lemma 4.3

This requires special treatment when k = 4; see the beginning of Section 7.2 for the reason for the split. In Sections 7.1 and 7.2 we set A′′ = {a : di(a) ≤ (1 + δ)np ∀i ≥ 3} ⊇ A′ and deﬁne B′′ similarly.

- 7.1 Proof for k ≥ 5


For reasons that will be explained as we proceed, we need somewhat diﬀerent arguments for large and small values of p.

- Case 1: np(k−1)/2 ≥ log4 n. Let Cb = {c ∈ C ∩ N(b) : d(b,c) ≤ np3/2} and


w1(b,c) > ζ} ⊇ {a : ∃b, w∗(a,b) > ζ}

W(A) = {a : ∃b ∈ B′′,

c∈Cb∩N(a)

(see (15) for ζ), and deﬁne W(B) similarly.

Remark. While it may seem more natural to deﬁne W(A), W(B) in terms of w(a,b) or w∗(a,b), the present deﬁnition has the advantage of not depending on ∇(A,B). We will see something similar in Case 2.

The point requiring most work here is w.l.p. |W(A)|,|W(B)| < ϑnp(k−1)/2t3. (24) Given this, the rest of the argument goes as follows. According to Lemma

- 3.1, (24) implies w.l.p. |∇(W(A),W(B))| < ϑn2pk−1 (25)


(since, given the inequality in (24), |∇(W(A),W(B))| ∼ B(m,p) for some m < ϑ2n2pk−1t6; note the inequalities in (24) and (25) depend on separate sets of random edges). On the other hand, an inductive application of Theorem 2.3(b) gives

w.l.p. w∗(a,b) < 2Ψ(H{1,2},(1 + δ)np) ∀a,b (26)

(using the fact that we are in Case 1 and noting that d(a) > (1 + δ)np implies w∗(a,b) = 0).

Finally, the combination of (25) and (26) bounds the number of type three copies of H by ϑn2pk−1 · 2Ψ(H{1,2},(1 + δ)np) < 4ϑΨ(H,n).

![image 16](<2011-demarco-tight-upper-tail-bounds_images/imageFile16.png>)

Proofs of the two assertions in (24) being similar, we just deal with W(A). We ﬁrst show

w.l.p. w1(b,c) < 2tnk−3peH−(3k−3)/2 =: γ ∀b ∈ B′′ and c ∈ Cb (27)

and

w.l.p. w1(b) < 4nk−2peH−(k−1) ∀b ∈ B′′. (28)

These will imply, via Lemma 3.3, that the events {a ∈ W(A)} are unlikely, and then (24) will be an application of Lemma 3.2.

Each of (27) and (28) is given (inductively) by Theorem 2.3(b), with small diﬀerences in arithmetic depending on d(v2) and d(v3): say we are in (a),(b) or (c) according to whether (d(v2),d(v3)) is (k−1,k−1), (k−1,k−2) or (k − 2,k − 2).

For (27) we ﬁrst observe that, given ∇(B ∪ C) and c ∈ Cb, w1(b,c) is stochastically dominated by X := X(H{1,2,3},np3/2) in (a) and (c), and by the sum of ⌊1/p⌋ copies of X in (b). (For the latter assertion, let ℓ be the

index for which v3  ∼ vℓ and, recalling that b ∈ B′′, partition N(b) ∩ Vℓ = V1 ∪···∪V⌊1/p⌋ with each block of size at most np3/2.) Theorem 2.3(b) thus gives the upper bound

n2⌊1/p⌋exp[−Ω(f(k − 3,np3/2t1/(k−3))] < pΩ(n2pk−1) (29) on either

Pr(∃b ∈ B′′,c ∈ Cb : w1(b,c) > 2tΨ(H{1,2,3},np3/2))

- (if we are in (a) or (c)) or Pr(∃b ∈ B′′,c ∈ Cb : w1(b,c) > 2t⌊1/p⌋Ψ(H{1,2,3},np3/2))
- (if we are in (b)), the inequality in (29) holding because we are in Case 1. (Note that in (29) the ⌊1/p⌋ is needed only when we are “in (b),” and the term involving t only when k = 5.)


To complete the proof of (27) it just remains to check that γ (recall this is the right hand side of (27)) is an upper bound on 2tΨ(H{1,2,3},np3/2) if we are in (a) or (c), and on 2t⌊1/p⌋Ψ(H{1,2,3},np3/2) if we are in (b).

![image 17](<2011-demarco-tight-upper-tail-bounds_images/imageFile17.png>)

The proof of (28) is similar. Here, because we are in Case 1, Theorem

- 2.3(b) gives the bound n⌊1/p⌋exp[−Ω(f(k − 2,(1 + δ)np)] < pΩ(n2pk−1)


on Pr(∃b ∈ B′′ w1(b) > 2Ψ(H{1,2},(1 + δ)np)) if we are in (a) or (b), and on Pr(∃b ∈ B′′ w1(b) > 2⌊1/p⌋Ψ(H{1,2},(1 + δ)np)) if we are in (c); and it’s easy to check that 2Ψ(H{1,2},(1 + δ)np) or 2⌊1/p⌋Ψ(H{1,2},(1 + δ)np) (as appropriate) is less than 4nk−2peH−(k−1).

![image 18](<2011-demarco-tight-upper-tail-bounds_images/imageFile18.png>)

Finally we return to (24). Fix (and condition on) any value of E(G) \ ∇(A,C) satisfying the inequalities in (27) and (28). It is enough to show that, under this conditioning and for any a,

Pr(a ∈ W(A)) < exp[−Ω(np(k−1)/2/t2)] =: q, (30)

since then Lemma 3.2 implies, using enq1/2 < 1 and the fact that the events {a ∈ W(A)} are independent,

|W(A)| <∗ ϑnp(k−1)/2t3.

(The assertion enq1/2 < 1 (or enqc < 1) imposes the most stringent requirement on p for Case 1.)

For (30) we observe that (28) gives (for any a and b ∈ B′′)

E

w1(b,c) = p

c∈Cb

c∈Cb∩N(a)

w1(b,c) ≤ p w1(b) < 4nk−2peH−k+2 < ζ/2,

whence, using Lemma 3.3 with (27), we have

Pr(a ∈ W(A)) < Pr ∃b ∈ B′′ {w1(b,c) : c ∈ Cb ∩ N(a)} > ζ < nexp[−Ω(ζ/γ)] < nexp[−Ω(np(k−1)/2/t2)] < exp[−Ω(np(k−1)/2/t2)].

![image 19](<2011-demarco-tight-upper-tail-bounds_images/imageFile19.png>)

- Case 2: np(k−1)/2 < log4 n. Recall that for very small p—in particular for p in the present range—and H = Kk, Theorem 2.3 is contained in Lemma


- 2.5; we may thus assume H = Kk. Let H′ = H − v1v2 and, writing w′ for wH′, set


W(A) = {a : ∃b ∈ B′′,w′(a,b) > ζ} ⊇ {a : ∃b w∗(a,b) > ζ}, (31)

and deﬁne W(B) similarly. (We could also work directly with w(a,b) and avoid the extra deﬁnitions; but the present treatment, which we will see

again below, is more natural in that it allows us to ignore the essentially irrelevant ∇(A,B).)

The argument here is similar to that for Case 1. We again show that membership in W(A), W(B) is unlikely, leading to

w.l.p. |W(A)|,|W(B)| < log8 n, (32) which, in view of Lemma 3.1, again gives

w.l.p. |∇(W(A),W(B))| < ϑn2pk−1. (33)

On the other hand we will show, by an argument somewhat diﬀerent from others seen here,

w.l.p. w∗(a,b) < nk−2p(k−21) ∀a,b. (34)

Combining this with (33) gives Lemma 4.3 (for the present case). Proof of (32). Of course it’s enough to prove the assertion for W(A). We ﬁrst observe that

w.l.p. w1(b) < 2tΨ(H{1,2},(1 + δ)np) < 4tlog4k−8 n =: m ∀b ∈ B′′; (35)

as elsewhere, this is given by an inductive application of Theorem 2.3(b), which says that, for any b ∈ B′′,

Pr(w1(b) > 2tΨ(H{1,2},(1 + δ)np)) < exp[−Ω(f(k − 2,(1 + δ)npt1/(k−2)))] < pΩ(n2pk−1).

(Note that for very small p the extra factor t in (35)—which did not appear in (28)—is needed for the ﬁnal inequality here.)

We now condition on E(G) \ ∇(A) and assume that, as in (35), w1(b) < m ∀b ∈ B′′. Note that a ∈ W(A) means (at least) that there is some b ∈ B′′ with

w′(a,b) ≥ 3k−2. (36)

For i ∈ {3,... ,k} (and any b), let Vi∗(b) be the set of vertices of Vi lying on copies of H1 that contain b. Since

w′(a,b) ≤ ki=3 |N(a) ∩ Vi∗(b)|,

(36) at least requires |N(a)∩(∪ki=3Vi∗(b))| ≥ 3(k−2); so the probability (for a given a) that there is some b for which (36) holds is at most

nPr(B((k − 2)m,p) ≥ 3(k − 2)) < p−(k−1)/2+(1−o(1))3(k−2) < pk−1 =: q.

But then, since (say) enq3/4 < 1, Lemma 3.2 gives (32).

![image 20](<2011-demarco-tight-upper-tail-bounds_images/imageFile20.png>)

Remark. Of course (34) is the counterpart of (26) of Case 1 (since H is now Kk the two bounds diﬀer only by small constant factors); but for very small p the simple inductive derivation of (26) using Theorem 2.3(b) no longer applies, since f(k − 2,(1 + δ)np) may be much smaller than f(k,n).

Proof of (34). We may assume b ∈ B′ as otherwise w∗(a,b) = 0. For i ∈ {3,... ,k} let

Vi∗(a,b) = {v ∈ Vi : some copy of H on a,b contains v}. We will show that

w.l.p. |∇(Vi∗(a,b),Vj∗(a,b))| < n2pk−1 ∀i,j,a and b ∈ B′. (37)

That this gives (34) is essentially a special case of a theorem of N. Alon [1], the precise statement used here (see the proof of Theorem 1.1 in [7]) being: an r-partite graph with at most ℓ edges between any two of its parts contains at most ℓr/2 copies of Kr.

For the proof of (37) we ﬁx a,b and i < j, and think of choosing edges of G in the order: (i) ∇(b,V3 ∪···∪Vk); (ii) ∇(Vα,Vβ) for all 3 ≤ α < β ≤ k except (α,β) = (i,j); (iii) ∇(a,Vi ∪ Vj); (iv) ∇(Vi,Vj). (The remaining edges are irrelevant here.)

Let H′′ = H1 − vivj. Since b ∈ B′, Lemma 2.5 gives (since we are in Case 2)

wH′′(b) <∗ 2Ψ(H1,2 − vivj,(1 + δ)np) =: m. (38)

Let Vi∗ be the set of vertices of Vi contained in copies of H′′ that contain b, and deﬁne Vj∗ similarly.

If the bound in (38) holds, then each of Vi∗,Vj∗ has size at most m < p−1 logO(1) n; an application of Lemma 3.1 thus shows that w.l.p. each of N(a) ∩ Vi∗, N(a) ∩ Vj∗ (and thus also Vi∗(a,b), Vj∗(a,b)) has size at most (say) p−1/4, and a second application gives (37).

![image 21](<2011-demarco-tight-upper-tail-bounds_images/imageFile21.png>)

## 7.2 Proof for k = 4

For k = 4, as in Case 2 above, we can’t simply invoke induction to obtain (26), since f(2,(1+δ)np) (≈ n2p3) is smaller than f(4,n). This is the main reason a separate argument is needed for k = 4.

Proof. In this section, for x,y ∈ G let d(x,y) = maxj≥3 dj(x,y). We consider the possibilities H = K4 and H = K4− (K4 with an edge removed) separately.

Case 1. H = K4. Now ab is heavy if w∗(a,b) > 225n2p3/s. Here it will be helpful to work with w rather than w∗. We treat (heavy) ab’s with w(a,b) > n2p3 and those with w(a,b) ∈ (225n2p3/s,n2p3] separately.

To bound the contribution of edges of the ﬁrst type, set A∗ = {a : ∃b ∈ B′′,w′(a,b) > n2p3} ⊇ {a : ∃b ∈ B′,w(a,b) > n2p3}

(where w′ is as in the paragraph containing (31)), and deﬁne B∗ similarly. We ﬁrst show

w.l.p. |A∗|,|B∗| < np7/4. (39)

To see this (for A∗, say) we condition on the value of ∇(B,C ∪ V4) and consider Pr(a ∈ A∗). Noting that for any a and b ∈ B′′,

Pr(w′(a,b) ≥ n2p3) ≤ Pr(d(a,b) > np5/4)+Pr(w′(a,b) ≥ n2p3|d(a,b) ≤ np5/4) (where 5/4 is just a convenient value between 1 and 3/2), we have Pr (a ∈ A∗) < n[2Pr(B((1 + δ)np,p) > np5/4) + Pr(B(n2p5/2,p) > n2p3)]

≤ pΩ(np5/4) + pΩ(n2p3). (40)

Since (given ∇(B,C ∪V4)) the events {a ∈ A∗} are independent, Lemma 3.2 now gives (39). (Note that when the second term dominates (40), Lemma

- 3.2 gives A∗ = ∅ w.l.p.) On the other hand, again using Lemma 3.1, we have


Pr(∃a ∈ A,b ∈ B′ : w(a,b) > n2p3t) < n2 Pr(B((1 + δ)2n2p2,p) > n2p3t)

< pΩ(n2p3), and combining this with (39) gives

{w∗(a,b) : w(a,b) > n2p3} <∗ |A∗||B∗|n2p3t <∗ n4p6.5t (< ϑn4p6).

For ab of the second type (i.e. with w(a,b) ∈ (225n2p3/s,n2p3]), we take J = 15np3/2/√s, set AJ = {a : ∃b ∈ B′′,d(a,b) > J}, and deﬁne BJ similarly. Given ∇(B,C ∪ V4) the events {a ∈ AJ} are independent with, for each a,

![image 22](<2011-demarco-tight-upper-tail-bounds_images/imageFile22.png>)

Pr(a ∈ AJ) < 2nPr(B((1 + δ)np,p) > J) < 2np(1−o(1))J/2 =: q.

(using e(1 + δ)np3/2+o(1) < J for the second inequality). Since enq1/2 < 1 (to see this, note J is always at least 15, and is nΩ(1) if p > n−2/3+Ω(1)), Lemma 3.2 gives

√

|AJ| <∗

ϑn2p3/J.

![image 23](<2011-demarco-tight-upper-tail-bounds_images/imageFile23.png>)

Of course an identical discussion applies to |BJ|, so we have |AJ||BJ| <∗ ϑsn2p3 and, by Lemma 3.1,

|∇(AJ,BJ)| <∗ ϑn2p3. Thus, ﬁnally,

{w∗(a,b) : ab heavy, w(a,b) ∈ (n2p3/s,n2p3]} <∗ |∇(AJ,BJ)|n2p3 = ϑn4p6

![image 24](<2011-demarco-tight-upper-tail-bounds_images/imageFile24.png>)

Case 2: H = K4−. Recall that v3v4 is the missing edge and an edge ab is heavy if w∗(a,b) > 225Ψ(H,n,p)/(n2p3s) = 225n2p2/s. We proceed more or less as in the second part of Case 1.

Set J = 15np/√s, AJ = {a : ∃b ∈ B′′,d(a,b) > J} and BJ = {b : ∃a ∈ A′′,d(a,b) > J}. Given ∇(B,C ∪ V4) the events {a ∈ AJ} are independent with, for each a,

![image 25](<2011-demarco-tight-upper-tail-bounds_images/imageFile25.png>)

Pr(a ∈ AJ) ≤ 2nPr(B((1 + δ)np,p) > J) < 2npJ/2 < pJ/3 =: q

(using Lemma 3.1 and J > ep−1/2(1+δ)np2 for the second inequality). Since (say) enq1/2 < 1, Lemma 3.2 gives

|AJ| <∗ n2p3/J,

and similarly for BJ. Since ab heavy at least requires a ∈ AJ,b ∈ BJ and a ∈ A′ (and since a ∈ A′ implies w(a,b) < ((1 + δ)np)2), this says that the number of type three copies of H is at most

|AJ||BJ|((1 + δ)np)2 <∗ (n2p3/J)2((1 + δ)np)2 < ϑn4p5

![image 26](<2011-demarco-tight-upper-tail-bounds_images/imageFile26.png>)

# 8 Proof of Lemma 4.4

As earlier, set H′ = H − v1v2 and w′ = wH′. Let X′ = a∈A,b∈B w′(a,b). Then X′ = XH′ depends only on E(G) \ ∇(A,B). Thus

X′ <∗ (1 + ϑ)Ψ(H′,n) = (1 + ϑ)Ψ(H,n)/p, (41)

where the inequality is given by induction if d(v2) = k − 1 and by Lemma 2.4 if d(v2) = k − 2.

Then Y :=

min{w′(a,b),ζ}1{ab∈E(G)} ≥

w∗(a,b)1{w∗(a,b)≤ζ}.

a∈A,b∈B

a∈A,b∈B

In view of (41) it’s enough to show that under any conditioning on E(G) \ ∇(A,B) for which X′ < (1 + ϑ)Ψ(H,n)/p,

Pr(Y > (1 + 2ϑ)Ψ(H,n)) < exp[−Ωϑ(n2pk−1s)] (= exp[−Ωϑ(f(k,n,p))]).

But under any such conditioning (or any conditioning on E(G) \ ∇(A,B)), the r.v.’s 1{ab∈E(G)} are independent; so, noting EY ≤ pX′ < (1+ϑ)Ψ(H,n) and using Lemma 3.3, we have

Pr (Y > (1 + 2ϑ)Ψ(H,n)) < exp[−Ωϑ(Ψ(H,n)/ζ)] = exp[−Ωϑ(n2pk−1s)].

![image 27](<2011-demarco-tight-upper-tail-bounds_images/imageFile27.png>)

# 9 Proof of Theorem 1.2

Recall here H = Kk. Set r = ⌈2EξH⌉ = ⌈2 nk p(k2)⌉. Note that we only need to prove Theorem 1.2 for small p, for simplicity say p < n−2/(k−1) log n, since above this f(k,n,p) = n2pk−1 log(1/p) and the theorem is given by the lower bound in (5). It will thus be enough to show Proposition 9.1. For n−2/(k−1) ≤ p < n−2/(k−1) log n,

Pr(ξH = r) > exp[−O(r)]

Proof. (This is an easy generalization of the argument for k = 3 given in [6].) The number of sets S of r vertex-disjoint copies of H in Kn is

(n)rk r!(k!)r

s :=

>

![image 28](<2011-demarco-tight-upper-tail-bounds_images/imageFile28.png>)

nk rkk

![image 29](<2011-demarco-tight-upper-tail-bounds_images/imageFile29.png>)

r

. (42)

For such an S, let QS and RS be the events {G contains all members of S} and {S is the set of H’s of G}. We have Pr(QS) = pr(k2) and will show (for any S)

Pr(RS|QS) = exp[−O(r)], (43) whence (using (42))

Pr(ξH = r) >

>

Pr(QS)Pr(RS|QS) = spr(k2) exp[−O(r)]

S

r

nkp(k2) rkk

exp[−O(r)] = exp[−O(r)].

![image 30](<2011-demarco-tight-upper-tail-bounds_images/imageFile30.png>)

For the proof of (43), ﬁx S; let W be the union of the vertex sets of the copies of H in S; and for i = 0,... ,k, let T(i) be the set of H’s (in Kn) having exactly i vertices outside W. We have

k

|T(i)|

1 − p(2i)+(k−i)i

Pr(RS|QS) ≥ (1 − p)|T(0)|

(44)

i=1

= exp[−O(r)].

Here the ﬁrst inequality is given by Harris’ Inequality [8] (which for our purposes says that for a product probability measure µ on {0,1}E (with E a ﬁnite set) and events Ai ⊆ {0,1}E that are either all increasing or all decreasing, µ(∩Ai) ≥ µ(Ai)), and for the second we can use, say, |T(i)| < ni(rk)k−i for 0 ≤ i ≤ k. (We omit the easy arithmetic, just noting that all factors but the last (that is, i = k) in (44) are actually much larger than exp[−O(r)].)

![image 31](<2011-demarco-tight-upper-tail-bounds_images/imageFile31.png>)

# 10 Concluding Remarks

Of course the big question is, what is the true behavior of the probability (1) for general H? We continue to use ξH for ξHn,p, and here conﬁne ourselves to η = 1; that is, we’re interested in Pr(ξH > 2EξH). As usual we don’t ask for more than the order of magnitude of the exponent.

One can show, mainly following the argument of Section 9, that for any K ⊆ H

Pr (ξH ≥ 2EξH) > exp[−OH(Ψ(K,n,p))] (45)

(where, recall, Ψ(K,n,p) = nvKpeK). As far as we can see, it could be that the truth in (1) is always given by the largest of the lower bounds in (45) and (5). For the latter we (ﬁnally) deﬁne

MH(n,p) =

n2p∆H if p ≥ n−1/∆H minK⊆H(Ψ(K,n,p))1/α∗K if n−1/mH ≤ p ≤ n−1/∆H

(46)

(where, as usual, α∗ is fractional independence number; see e.g. [11] or [4]). This is not quite the same as the quantity MH∗ (n,p) used in [11], but, as shown in their Theorem 1.5, the two agree up to a constant factor; so the diﬀerence is irrelevant here.

Conjecture 10.1. For any H and p > n−1/mH, Pr (ξH ≥ 2EξH) = exp[−ΘH(min{ min

Ψ(K,n,p),MH(n,p)t})].

K⊆H,eK>0

(47)

(Recall t = log(1/p).) We remark without proof (it is not quite obvious as far as we know) that, for a given H, the set of p for which the (outer) minimum in (47) is MH(n,p)t is the interval [pK,1], where K is a smallest subgraph of H with mK = mH and pK is the unique p for which Ψ(K,n,p) = MH(n,p)log(1/p).

Conjecture 10.1 gives a diﬀerent perspective on the observation from [11, Section 8.1] that H = K2 shows that the lower bound in (5) is not always tight. In this case MH(n,p) = n2p for the full range of p above and, of course, ξH is just Bin( n2 ,p); so the upper bound in (5) is the truth. But in fact (45) shows (with a little thought) that the lower bound in (5) is not tight for any H and suﬃciently small p (> n−1/mH), since for small enough p one of the terms Ψ(K,n,p) in (47) is o(MH(n,p)t). What’s special about K2 is that it is the only (connected) H for which the best lower bound is never given by (5); that is, the minimum in (47) is never MH(n,p)t.

It also seems interesting to estimate Pr(ξH ≥ γEξH) (48)

when γ = γ(n) = ω(1). The present results essentially do this for H = Kk and “generic” p; precisely, Theorem 2.3(b) implies (using a mild variant of

Proposition 2.1) Pr(ξH > 2τΨ(H,n,p)) < exp[−Ω(f(k,nτ1/k,p))], (49)

which, for p in the range where f(k,nτ1/k,p) = n2τ2/kpk−1t, is (up to the constant in the exponent) the probability of containing a clique of size np(k−1)/2(2τ)1/k (provided this is not more than nk ). Of course the trick that gets Theorem 2.3(b) from Theorem 2.3(a) is general, so results on Conjecture 10.1 give corresponding upper bounds for (48); but these bounds will not be tight in general, and at this writing we don’t have a good guess as to the general truth in (48).

Acknowledgment. We would like to thank one of the referees for an exceptionally careful reading and for pointing out [16].

# References

- [1] N. Alon, On the number of subgraphs of prescribed type of graphs with a given number of edges. Israel J. Math. 38 (1981), no. 1-2, 116-130.
- [2] N. Alon and J.H. Spencer, The Probablistic Method, Wiley, New York, 2000.
- [3] J. Beck and W. Chen, Irregularities of Distribution, Cambridge Univ. Pr., Cambridge, 1987.
- [4] B. Bollob´s, Modern Graph Theory, Springer, New York, 1998.
- [5] S. Chatterjee, The missing log in large deviations for subgraph counts

(2010), http://arxiv.org/abs/1003.3498.

- [6] B. DeMarco and J. Kahn, Upper Tails for Triangles (2010), http://arxiv.org/abs/1005.4471.
- [7] E. Friedgut and J. Kahn, On the number of copies of one hypergraph in another Israel J. Math. 105 (1998), 251-256.
- [8] T.E. Harris, A lower bound on the critical probability in a certain percolation process, Proc. Cam. Phil. Soc. 56 (1960), 13-20.
- [9] S. Janson, Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221-230.


- [10] S. Janson, T.  Luczak and A. Rucin´ski, Random Graphs, Wiley, New York, 2000.
- [11] S. Janson, K. Oleszkiewicz and A. Rucin´ski, Upper tails for subgraph counts in random graphs, Israel J. Math. 142 (2004), 61-92.
- [12] S. Janson and A. Rucin´ski, The infamous upper tail, Random Structures & Algorithms 20 (2002), 317-342.
- [13] S. Janson and A. Rucin´ski, The deletion method for upper tail estimates, Combinatorica 24 (2004), 615-640.
- [14] J. H. Kim and V. H. Vu, Concentration of multivariate polynomials and its applications, Combinatorica 20 (2000), 417-434.
- [15] J. H. Kim and V. H. Vu, Divide and conquer martingales and the number of triangles in a random graph, Random Structures & Algorithms 24 (2004), 166-174.
- [16] V.H Vu, On the concentration of multivariate polynomials with small expectation, Random Structures & Algorithms, 16(4) (2000),344-363.
- [17] V. H. Vu, A large deviation result on the number of small subgraphs of a random graph, Combin. Probab. Comput. 10 (2001), 79-94.


Department of Mathematics Rutgers University Piscataway NJ 08854 rdemarco@math.rutgers.edu jkahn@math.rutgers.edu

