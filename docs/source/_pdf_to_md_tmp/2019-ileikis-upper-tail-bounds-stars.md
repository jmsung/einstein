arXiv:1901.10637v1[math.PR]30Jan2019

Upper tail bounds for Stars

Matas Sileikisˇ ∗ and Lutz Warnke† 29 January 2019

Abstract

For r ≥ 2, let X be the number of r-armed stars K1,r in the binomial random graph Gn,p. We study the upper tail P(X ≥ (1+ε)EX), and establish exponential bounds which are best possible up to constant factors in the exponent (for the special case of stars K1,r this solves a problem of Janson and Rucin´ski, and conﬁrms a conjecture by DeMarco and Kahn). In contrast to the widely accepted standard for the upper tail problem, we do not restrict our attention to constant ε, but also allow for ε ≥ n−α deviations.

# 1 Introduction

The study of (the distribution of) small subgraphs in the binomial random graph Gn,p is one of the most fundamental and inﬂuential problems in the theory of random graphs. Starting with the seminal work of Erdo˝s and R´enyi [11] from 1960, the early results for the number XH of copies of H in Gn,p concerned the threshold of appearance (i.e., when P(XH > 0) → 1) and the range of edge-probabilities p for which XH is asymptotically normal; these basic features were eventually resolved in the 1980s by Bollob´as [2] and Ruci´nski [25]. Later the focus changed to ﬁner details of the distribution of XH, and the lower tail P(XH ≤ (1 − ε)EXH) was studied intensively in the late 1980s (often for the special case ε = 1). This led to the discovery of Janson’s inequality [13, 14, 24], which gives exponential bounds for P(XH ≤ (1 − ε)EXH) that are best possible up to constant factors in the exponent (cf. the recent work of Janson and Warnke [20]).

Since the early 1990s the ‘infamous’ upper tail P(XH ≥ (1 + ε)EXH) has remained an important challenge, providing a well-known testbed for concentration inequalities (see, e.g., [16]). After polynomial bounds around 1990 by Spencer [29] and exponential bounds in the late 1990s via the Kim–Vu polynomial concentration method [21, 30], in 2002 Janson, Oleszkiewicz and Ruci´nski [17] obtained a breakthrough: via a moment based method they obtained exponential estimates for P(XH ≥ (1 + ε)EXH) that, for constant ε, are best possible up to logarithmic factors in the exponent (see also [9, 19] for extensions to random hypergraphs, and arithmetic progressions in random subsets of integers). The upper tail problem of closing the aforementioned logarithmic gap has remained open during the last decade, and only recently this has been settled for cliques Kr by DeMarco and Kahn [6, 7] (see also Chatterjee [3] for r = 3), and for arithmetic progressions by Warnke [31]. Modern large deviation theory also gives partial results [4, 23, 1, 8] for large edge-probabilities p ≥ n−δ

(this restriction sidesteps some diﬃculties of the upper tail problem).

H

In this paper we solve the upper tail problem for r-armed stars K1,r, and as a conceptual novelty we will also allow ε to depend on n (i.e., do not restrict our attention to constant ε, as usual). The casual reader might suspect that tail estimates for r-armed stars are essentially trivial, but this is only true for r = 1 (where XK

= |E(Gn,p)| since K1,1 = K2). To put this into context, Janson, Oleszkiewicz and Ruci´nski [17] proved that for r-regular graphs H, such as cliques Kr+1, the upper tail satisﬁes

1,1

H,ε(n2pr) ≤ P(XH ≥ (1 + ε)EXH) ≤ e−Ω

H,ε(n2pr),

pO

where the subscripts in OH,ε and ΩH,ε indicate that the implicit constants may depend on H and ε. They also highlighted K1,r (with r ≥ 2) as key example where the form of the exponent is more complicated,

![image 1](<2019-ileikis-upper-tail-bounds-stars_images/imageFile1.png>)

∗Department of Theoretical Computer Science, Institute of Computer Science of the Czech Academy of Sciences, 182 07 Prague, Czech Republic. E-mail: matas.sileikis@gmail.com. With institutional support RVO:67985807. Research supported by the Czech Science Foundation, grant number GJ16-07822Y.

†School of Mathematics, Georgia Institute of Technology, Atlanta GA 30332, USA. E-mail: warnke@math.gatech.edu. Research partially supported by NSF Grant DMS-1703516 and a Sloan Research Fellowship. Part of the work was done while the author was a member of the Department of Pure Mathematics and Mathematical Statistics, University of Cambridge.

i.e, has diﬀerent expressions for diﬀerent ranges of p. This surprising intricacy is further manifested by the history of the infamous upper tail problem. Namely, Vu [30] argued in 2000 that his general results were essentially unimprovable due to r-armed stars, for which he obtained bounds of the form

r,ε(n1+1/rp) ≤ P(XK

pO

1,r

≥ (1 + ε)EXK

1,r

r,ε(n1+1/rp). (1)

) ≤ e−Ω

However, Janson, Oleszkiewicz and Rucinski [17] later discovered that the upper tail behavior of K1,r is more delicate (the lower bound in (1) is not always correct), and obtained bounds of the more involved form

r,ε(max{n1+1/rp, n2pr}) ≤ P(XK

pO

1,r

≥ (1 + ε)EXK

1,r

r,ε(max{n1+1/rp, n2pr}). (2)

) ≤ e−Ω

In words, for stars the form of the upper tail changes around p ≈ n−1/r, which is an intriguing phenomenon (that does not occur for cliques). In fact, a recent conjecture of DeMarco and Kahn [7, 28] for general H suggests that in (2) the ‘correct’ exponent involves yet another term µ := EXK

= Θr(nr+1pr), see (3). However, despite some partial results [26, 27, 33], the quest for matching bounds in (1)–(2) remained open.

1,r

- 1.1 Main results


Our ﬁrst basic result settles the upper tail problem of r-armed stars for constant ε, by closing the existing log(1/p) gap in the exponent for all p ∈ (0,1]. In particular, (3) below conﬁrms1 Conjecture 10.1 of DeMarco and Kahn [7] in the special case H = K1,r. For subgraph counts this is the ﬁrst example of a sharp upper tail estimate where, for constant ε, the form of the exponent undergoes multiple phases (i.e., has more more than two diﬀerent expressions for diﬀerent ranges of p).

- Theorem 1 (Upper tail problem for constant ε). Given r ≥ 2, let X = Xr,n,p be the number of copies of K1,r in Gn,p. Set µ := EX. For p ∈ (0,1] and ε > 0 satisfying 1 ≤ (1 + ε)µ ≤ Xr,n,1 we have

− log P(X ≥ (1 + ε)µ) = Θr,ε Φ with Φ := min µ, max µ1/r,µ/nr−1 log(1/p) . (3)

Note that the assumption (1 + ε)µ ≤ Xr,n,1 is necessary (since X > Xr,n,1 is impossible), and that the assumption (1 + ε)µ ≥ 1 is natural (since otherwise P(X ≥ (1 + ε)µ) = P(X ≥ 1) = 1 − P(X = 0) holds). We now motivate the intricate form of the exponent in (3) for ε = 1. First, Poisson approximation heuristics suggest that P(X ≥ 2µ) ≈ e−Θ(µ) for small edge-probabilities p. Second, it turns out that m = Θr(max{µ1/r,µ/nr−1}) appropriately clustered2 edges F suﬃce to create 2µ copies of K1,r, which implies P(X ≥ 2µ) ≥ P(F ⊆ Gn,p) ≥ pm = emlog(1/p). Intuitively, Theorem 1 conﬁrms that the more likely of these two mechanisms (the one with larger probability) controls the upper tail behaviour for constant ε.

Our second result determines the correct dependence of the stars upper tail on ε, up to constant factors in the exponent (this contrasts Theorem 1 above, where the implicit constants may depend on ε). In particular, (4) below solves Problem 6.1 of Janson and Ruci´nski [18] in the special case H = K1,r. For subgraph counts this is the ﬁrst example where, for p bounded away from one, the order of the large deviation rate function − logP(X ≥ (1 + ε)µ) is determined for ε = ε(n) of form ε ≥ n−α (the assumption Φ(ε) ≥ 1 is natural, since it ensures that we are dealing with exponentially small probabilities).

- Theorem 2 (Upper tail problem for ε = ε(n) ≥ n−α). Given r ≥ 2, let X = Xr,n,p be the number of copies of K1,r in Gn,p. Set µ := EX, σ2 := VarX, and ϕ(x) := (1 + x)log(1 + x) − x. Given ξ ∈ (0,1) there is α = α(r) > 0 such that, for p ∈ (0,1 − ξ] and ε ≥ n−α satisfying Φ(ε) ≥ 1 and 1 ≤ (1 + ε)µ ≤ Xr,n,1, we have


− log P(X ≥ (1 + ε)µ) = Θr,ξ Φ(ε) , (4) with

Φ(ε) := min ϕ(ε)µ2/σ2, max (εµ)1/r,(εµ)/nr−1 log(e/p) . (5)

Remark 3. The variance satisﬁes σ2 = Θr((1−p)µ(1+(np)r−1)); see, e.g., Lemma 3.5 in [15]. Furthermore, if µ1−1/r ≥ log n holds, then in (5) we can replace ϕ(ε)µ2/σ2 by (εµ)2/σ2; see Lemma 12.

![image 2](<2019-ileikis-upper-tail-bounds-stars_images/imageFile2.png>)

- 1Using Corollary 1.8 in [17] and the discussion of Remark 8.3 in [17] it is not diﬃcult to check that the special case H = K1,r


of Conjecture 10.1 in [7] indeed reduces to (3) with ε = 1; see also equation (4.27) in [27] and Remark 2 in [26].

2For example, complete bipartite graphs Ky,z with suitable y = Θr(min{µ1/r, n}) and z = Θr(µ/yr) suﬃce: they contain ≥ z yr = Θr(zyr) = Θr(µ) stars and yz = Θr(µ/yr−1) = Θr(max{µ1/r, µ/nr−1}) edges; see Lemma 14 for more details.

Conjecture 4 (Correct upper tail behaviour). Theorem 2 remains valid without the assumption ε ≥ n−α. We now motivate the somewhat unusual form of the exponent in (4). First, normal approximation heuristics3 suggest that P(X ≥ (1 + ε)µ) ≈ e−Θ

r((εµ)2/σ2) for very small ε, and this sub-Gaussian tail is consistent with the ϕ(ε)µ2/σ2 term in (5) since ϕ(ε) = Θ(ε2) as ε → 0 (the function ϕ is well-known from Chernoﬀ bounds). Second, in Gn,p we usually expect to have at least (1 − ε)µ copies of K1,r, say, so enforcing 2εµ extra copies via m = Θr(max{(εµ)1/r,(εµ)/nr−1}) appropriately clustered4 edges F should thus be enough to give a total of (1 + ε)µ copies of K1,r; this heuristic loosely suggests P(X ≥ (1 + ε)µ) ≥ Ωr(1) · P(F ⊆ Gn,p) ≥ Ωr(pm) ≥ e−O

r(mlog(1/p)). Intuitively, Conjecture 4 predicts that the form of the upper tail is indeed determined by either sub-Gaussian or ‘clustered’ behaviour, and Theorem 2 conﬁrms this for ε = ε(n) ≥ n−α.

Our third result approaches the upper tail problem from a conceptually slightly diﬀerent perspective, studying P(X ≥ µ+t) for general deviations t (this contrasts Theorem 1 and 2 above, where we focus on the large deviations range t = εµ and then put restrictions on ε). For subgraph counts, inequality (6) below is the ﬁrst example where, for moderately large edge-probabilities p, the order of − logP(X ≥ µ + t) is completely resolved for all exponentially small deviations (where t ≥ σ is the natural target assumption). We complement this result with inequality (7) below, which is the ﬁrst example where the order of − logP(X ≥ µ + t) is resolved for nearly all deviations t where the ‘clustered’ behaviour determines the exponent (here t2/σ2 ≥ M(t)log(e/p) is the natural target assumption for µ1−1/r ≥ log n; see (5), Remark 3, and Conjecture 4).

Theorem 5 (General upper tail bounds: moderate deviations and clustered regime). Given r ≥ 2, let X = Xr,n,p be the number of copies of K1,r in Gn,p. Set µ := EX and σ2 := Var X. Given ξ ∈ (0,1), then the following holds whenever p ∈ (0,1 − ξ] and 1 ≤ µ + t ≤ Xr,n,1.

- (i) If p ≥ (log n)/n and t ≥ σ, then − log P(X ≥ µ + t) = Θr,ξ Ψ(t) with Ψ(t) := min t2/σ2, M(t)log(e/p) . (6)
- (ii) If µ ≥ ξ and t > 0 satisﬁes t2/σ2 ≥ M(t)log(e/p) · (log n)2r, then − log P(X ≥ µ + t) = Θr,ξ M(t)log(e/p) with M(t) := max t1/r,t/nr−1 . (7)


By Remark 3, inequalities (6)–(7) provide further evidence for Conjecture 4 (and verify it for p ≥ (log n)/n).

- 1.2 Some comments


The main focus of this paper are upper bounds on the upper tail P(X ≥ (1 + ε)µ). Developing [31, 33], here our high-level proof strategy is based on the idea that (after ignoring certain ‘bad’ events with negligible probabilities) using combinatorial arguments we can ﬁnd a ‘well-behaved’ subgraph G0 ⊆ Gn,p in the sense that (i) the number of stars K1,r in G0 and Gn,p are approximately the same (diﬀer by at most εµ/2, say), and (ii) the maximum degree of GJ is ‘not too large’ (which intuitively helps for showing concentration of stars). Using modern Chernoﬀ-like upper tail bounds, we then show that it is very unlikely to have a ‘bad’ subgraph G′ ⊆ Gn,p with ‘not too large’ maximum degree and ‘many’ stars (at least (1 + ε/2)µ many, say). Putting things together, the punchline is then that we can only have X ≥ (1 + ε)µ many stars if one of the discussed unlikely ‘bad’ events occur, which (after some technical work) eventually gives the desired upper bounds on the upper tail P(X ≥ (1 + ε)µ); see Section 2 for more details.

Finally, let us brieﬂy compare our upper tail results for stars with very recent results from the large deviation theory literature, which are spearheaded by Chatterjee, Dembo, Lubetzky, Varadhan, Zhao, and many others (see, e.g., [5, 22, 4, 23, 10, 1, 8]). For general H, these aim at determining the asymptotics of − logP(XH ≥ (1 + ε)EXH) for constant ε and large edge-probabilities of form p = Θ(1) or p ≥ n−δ

. For stars H = K1,r, inequality (4) from Theorem 2 is weaker in the sense that it only determines − logP(XK

H

≥ (1 + ε)EXK

1,r

) up to constant factors, but it is stronger in the sense that it covers a much wider range of the parameters, including ε = ε(n) ≥ n−α and all p = p(n) of interest. Obtaining such tail estimates with increased ranges of applicability is useful for combinatorial applications, where one is usually ‘willing to give up a little bit on the tail’, in particular on the ‘inessential numerical constants’ in the exponent (see [30, 18]). Furthermore, estimates of form (6)–(7) are also quite satisfactory from a concentration inequality perspective. Overall, we hope that our results stimulate more research into such estimates for other graphs H.

1,r

![image 3](<2019-ileikis-upper-tail-bounds-stars_images/imageFile3.png>)

- 3The same normal heuristic suggests that in (3) we should perhaps have used µ2/σ2 instead of µ, but it turns out that then the µ2/σ2 term would only matter for Φ (i.e., determine the minimum) in a range of p where µ2/σ2 = Θr,ε(µ) holds.
- 4As before, complete bipartite graphs Ky,z with suitable y = Θr(min{(εµ)1/r, n}) and z = Θr(εµ/yr) suﬃce (see Lemma 14).


- 1.3 Organization


In Section 2 we prove the upper bounds on the upper tail from Theorem 1, 2, and 5 (and discuss a simple extension). The corresponding (fairly routine) lower bounds are then established in Appendix A.

# 2 Upper bounds on the upper tail

In this section we establish the upper bounds on the upper tail P(X ≥ (1 + ε)µ) from Theorem 1, 2, and 5. Our core argument has two strands. In the ﬁrst combinatorial part we iteratively decrease the maximum degree of the random graph Gn,p = GJ ⊇ ··· ⊇ G0 by edge-deletion (the idea is to remove large stars K1,D

j

with Dj ≫ r from Gj) until the ﬁnal graph G0 has suﬃciently low maximum degree, say at most D. This degree bound allows us to estimate the number of stars K1,r in G0 via a ‘well-behaved’ auxiliary random variable XD. Taking into account the number of stars Kr which are removed when passing from Gn,p = GJ to G0, this allows us (by means of a technical event T ) to approximate the number X = Xr,n,p of copies of K1,r in Gn,p using XD and several further auxiliary random variables ND

(which intuitively bound the number of K1,D

j

in Gn,p). In the second probabilistic part we then estimate the upper tails of these auxiliary variables using a concentration inequality of Warnke [31] and ad-hoc arguments (exploiting the careful deﬁnitions of the variables XD and ND

j

given in Section 2.1). Putting things together, the core argument then proceeds roughly as follows: by the combinatorial part X ≥ (1 + ε)µ can only happen if at least one of the auxiliary variables XD or ND

j

is ‘large’, and by the probabilistic part the probability of this ‘bad’ event is at most the desired ‘correct’ upper tail probability (for suitable choices of the degree constraint D and other parameters).

j

In Section 2.1 we ﬁrst illustrate this argument for the simpler setup of Theorem 1, and in Section 2.2 we then extend the argument to the more precise tail estimates of Theorem 2 and 5. Finally, in Section 2.3 we also brieﬂy discuss a straightforward extension (to a certain sum of iid variables).

- 2.1 Core argument for Theorem 1


We start by introducing the main random variables and events for Theorem 1 (as we shall see, their careful deﬁnitions will facilitate the interplay between the combinatorial and probabilistic parts of our argument). For x ≥ 0, let Xx denote the maximum number of copies of K1,r in any subgraph H ⊆ Gn,p with maximum degree at most x. For y > 0, let Ny denote the maximum size of any collection of edge-disjoint K1,⌈y⌉ in Gn,p. For β,D,t > 0 let T = T (β,D,t) denote the ‘technical’ event that

ND

j

βM Dj

<

![image 4](<2019-ileikis-upper-tail-bounds-stars_images/imageFile4.png>)

for all j ∈ N = {0,1,...} , (8)

where we tacitly used the following convenient parametrization:

M = M(t) := max t1/r, t/nr−1 , Dj = Dj(D) := 2jD.

(9)

(In this subsection we shall only use t = εµ; working with general t is convenient for the later extensions.)

The following combinatorial lemma is at the heart of our argument, and it intuitively states that X ≈ XD whenever the event T = T (β,D,t) holds. Its proof is inspired by ideas developed in [31, 33], but contains several new ideas. For example, instead of iteratively sparsifying an auxiliary hypergraph (which encodes the edge-sets of all stars K1,r in Gn,p) we here iteratively sparsify the random graph Gn,p itself. Furthermore, in order to obtain the correct tail behaviour, in inequality (8) we need to work with M = max{t1/r,t/nr−1} instead of the simpler choice M = t1/r suggested by [31] (we achieve this by adding an extra degree bound to the argument, bounding the initial maximum degree by M = min{M,n} instead of just M).

![image 5](<2019-ileikis-upper-tail-bounds-stars_images/imageFile5.png>)

Lemma 6. Given β ∈ (0,1/32] and D,t > 0, the event T (β,D,t) implies XD ≤ X ≤ XD + t/2.

The lower bound X ≥ XD of Lemma 6 is trivial. For the upper bound the idea is to iteratively decrease the maximum degree of Gn,p, yielding Gn,p = GJ ⊇ ··· ⊇ G0. By bounding the number of K1,r which are removed when passing from Gj+1 to Gj, this eventually allows us to estimate the total number of K1,r.

![image 6](<2019-ileikis-upper-tail-bounds-stars_images/imageFile6.png>)

![image 7](<2019-ileikis-upper-tail-bounds-stars_images/imageFile7.png>)

Proof of Lemma 6. Deﬁne M := min{M,n}. Let J be the smallest integer J ≥ 0 with DJ ≥ M. We set GJ = Gn,p and inductively construct GJ ⊇ ··· ⊇ G0. Given Gj+1, 0 ≤ j ≤ J − 1, let Cj+1 be a maximal set of edge-disjoint collection of stars K1,⌈D

j⌉. We remove all edges from Gj+1 which are incident to a centre vertex of some star in Cj+1, and denote the resulting graph by Gj.

Writing ∆j = ∆(Gj) for the maximum degree of Gj, we claim that ∆j ≤ Dj for all 0 ≤ j ≤ J. For GJ = Gn,p we use a case distinction. If M ≥ n, then trivially ∆J ≤ n = M ≤ DJ. Otherwise DJ ≥ M = M, in which case (8) entails ND

![image 8](<2019-ileikis-upper-tail-bounds-stars_images/imageFile8.png>)

![image 9](<2019-ileikis-upper-tail-bounds-stars_images/imageFile9.png>)

J⌉, and ∆J ≤ ⌈DJ⌉−1 ≤ DJ follows. Further considering Gj+1 with 0 ≤ j ≤ J − 1, we note that ∆j ≤ ⌈Dj⌉ − 1 ≤ Dj by construction, because otherwise we could add another K1,⌈D

< β < 1, so Gn,p = GJ contains no K1,⌈D

J

j⌉ to Cj+1 (contradicting maximality).

With GJ ⊇ ··· ⊇ G0 in hand, we now count the total number of copies of K1,r in Gn,p = GJ. Note that, given an edge e = {v1,v2} of Gj+1 with 0 ≤ j < J, we can construct any K1,r in Gj+1 containing e by ﬁrst selecting a centre vertex vc ∈ {v1,v2} and then r − 1 additional neighbours of vc. Hence in Gj+1 any edge is contained in at most 2 ∆

r−1 ≤ 2rDjr−1/(r − 1)! ≤ 4Djr−1 copies of K1,r. Recalling the deﬁnition of ND

, note that when, passing from Gj+1 to Gj, we remove at most ND

j+1

j

Dj edges. So, since G0 contains at most XD

∆j+1 ≤ 2ND

j

j

![image 10](<2019-ileikis-upper-tail-bounds-stars_images/imageFile10.png>)

= XD copies of K1,r, using (8) and max0≤j<J Dj ≤ M it follows that X ≤ XD +

0

Djr−1. (10)

Dj · 4Djr−1 ≤ XD + 8βM ·

2ND

j

0≤j<J

![image 11](<2019-ileikis-upper-tail-bounds-stars_images/imageFile11.png>)

j∈N:Dj≤M

Recalling Dj = 2jD and r ≥ 2, using M = min{M,n}, M = max{t1/r, t/nr−1} and β ≤ 1/32 we infer

![image 12](<2019-ileikis-upper-tail-bounds-stars_images/imageFile12.png>)

X − XD ≤ 8βM · 2Mr−1 ≤ 16β · min{Mr,Mnr−1} ≤ t/2, (11) which completes the proof.

![image 13](<2019-ileikis-upper-tail-bounds-stars_images/imageFile13.png>)

![image 14](<2019-ileikis-upper-tail-bounds-stars_images/imageFile14.png>)

![image 15](<2019-ileikis-upper-tail-bounds-stars_images/imageFile15.png>)

![image 16](<2019-ileikis-upper-tail-bounds-stars_images/imageFile16.png>)

![image 17](<2019-ileikis-upper-tail-bounds-stars_images/imageFile17.png>)

Applying Lemma 6 with t = εµ, in the probabilistic part of the argument it remains to estimate P(XD ≥ µ + εµ/2) and P(¬T (β,D,εµ)). We shall exploit the maximum degree constraint of XD via the following upper tail inequality of Warnke [31], which extends classical Chernoﬀ bounds to random variables with ‘well-behaved dependencies’ (and allows us to go beyond the method of typical bounded diﬀerences [32]).

Theorem 7 (Corollary of [31, Theorem 9]). Let (ξi)i∈S be a ﬁnite family of independent random variables with ξi ∈ {0,1}. Given a family I of subsets of S, consider random variables Yα := i∈α ξi with α ∈ I, and suppose α∈I EYα ≤ µ. Deﬁne ZC := max α∈J Yα, where the maximum is taken over all J ⊆ I with maxβ∈J |{α ∈ J : α ∩ β = ∅}| ≤ C. Set ϕ(x) := (1 + x)log(1 + x) − x. Then, for all C,t > 0,

ϕ(t/µ)µ C

P(ZC ≥ µ + t) ≤ exp −

![image 18](<2019-ileikis-upper-tail-bounds-stars_images/imageFile18.png>)

t2 2C(µ + t)

≤ exp −

![image 19](<2019-ileikis-upper-tail-bounds-stars_images/imageFile19.png>)

. (12)

The main observation is that, in every subgraph H ⊆ Gn,p with maximum degree at most D, any star K1,r shares edges with O(Dr−1) other stars. For XD this allows us to routinely apply Theorem 7 with Lipschitz-like parameter C = O(Dr−1), making inequality (13) plausible. For Theorem 1 the crux is that our choice of D will ensure µ/Dr−1 = Θr(Φ), so (13) suggests that XD ≤ µ + εµ/2 fails with probability at most e−Ω

r,ε(Φ). Corollary 8. For all n ≥ 1, p ∈ (0,1] and D,t > 0 we have

ϕ(t/µ)µ 16Dr−1

P(XD ≥ µ + t/2) ≤ exp −

![image 20](<2019-ileikis-upper-tail-bounds-stars_images/imageFile20.png>)

min{t2/µ,t} 48Dr−1

≤ exp −

![image 21](<2019-ileikis-upper-tail-bounds-stars_images/imageFile21.png>)

. (13)

Proof. Let K1,r(G) contain all edge-subsets of G that are isomorphic to K1,r. Writing Yα := {α⊆E(G

n,p)}, there is a subgraph H ⊆ Gn,p with maximum degree at most ⌊D⌋ such that XD = α∈J Yα for J := K1,r(H). Given β ∈ J , we construct all edge-intersecting stars α ∈ J as in the proof of Lemma 6, and infer

max

|{α ∈ J : α ∩ β = ∅}| ≤ r · 2

β∈J

⌊D⌋ r − 1

2rDr−1 (r − 1)!

≤ 4Dr−1 =: C. (14)

≤

![image 22](<2019-ileikis-upper-tail-bounds-stars_images/imageFile22.png>)

It follows that XD ≤ ZC, where ZC is deﬁned as in Theorem 7 with I = K1,r(Kn). It is well-known (and easy to check by calculus) that for x ≥ 0 we have

ϕ(x/2) ≥ ϕ(x)/4 and x2 ≥ ϕ(x) ≥ min{x,x2}/3. (15)

Putting things together, using Theorem 7 and (15) it follows that

ϕ(t/µ)µ 4C

P(XD ≥ µ + t/2) ≤ P(ZC ≥ µ + t/2) ≤ exp −

![image 23](<2019-ileikis-upper-tail-bounds-stars_images/imageFile23.png>)

min{t,t2/µ} 12C

≤ exp −

![image 24](<2019-ileikis-upper-tail-bounds-stars_images/imageFile24.png>)

, (16)

which completes the proof of (13) by choice of C (see (14) above). We shall estimate P(¬T (β,D,εµ)) via a union bound argument and the following upper tail estimate for ND

![image 25](<2019-ileikis-upper-tail-bounds-stars_images/imageFile25.png>)

![image 26](<2019-ileikis-upper-tail-bounds-stars_images/imageFile26.png>)

![image 27](<2019-ileikis-upper-tail-bounds-stars_images/imageFile27.png>)

![image 28](<2019-ileikis-upper-tail-bounds-stars_images/imageFile28.png>)

. The technical assumption (17) intuitively ensures that vertices with degree at least D are unlikely. For Theorem 1 the crux is that our choice of D will also ensure np/(eDj) ≤ pΩ(1), so applications of inequality (18)

j

- with x = βM/Dj suggest that T and thus (8) fails with probability at most n · n−3pΩ(M) ≤ n−2pΩ


ε(Φ), say.

- Lemma 9. For all n ≥ 1, p ∈ (0,1], and D > 0 satisfying e3np/D D ≤ n−8 (17)


the following holds. For all x > 0 we have

P(ND

j

1 n3

≥ x) ≤

![image 29](<2019-ileikis-upper-tail-bounds-stars_images/imageFile29.png>)

np e⌈Dj⌉

![image 30](<2019-ileikis-upper-tail-bounds-stars_images/imageFile30.png>)

xDj/2

{Dj≤n}. (18)

Proof. As mz ≤ (me/z)z for all integers m,z ≥ 1, by exploiting the disjointness condition of ND

we infer

j

P(ND

j

≥ x) ≤ n⌈x⌉

n ⌈Dj⌉

⌈x⌉

p⌈x⌉⌈D

j⌉ ≤ n

enp ⌈Dj⌉

![image 31](<2019-ileikis-upper-tail-bounds-stars_images/imageFile31.png>)

⌈Dj⌉ ⌈x⌉

(19)

As the function x  → (e3np/x)x is decreasing for x ≥ e2np, and (17) implies ⌈Dj⌉ ≥ D ≥ e3np, we deduce

enp ⌈Dj⌉

![image 32](<2019-ileikis-upper-tail-bounds-stars_images/imageFile32.png>)

⌈Dj⌉

=

e3np ⌈Dj⌉

![image 33](<2019-ileikis-upper-tail-bounds-stars_images/imageFile33.png>)

⌈Dj⌉ 2

![image 34](<2019-ileikis-upper-tail-bounds-stars_images/imageFile34.png>)

np e⌈Dj⌉

![image 35](<2019-ileikis-upper-tail-bounds-stars_images/imageFile35.png>)

⌈Dj⌉ 2

![image 36](<2019-ileikis-upper-tail-bounds-stars_images/imageFile36.png>)

≤

e3np D

![image 37](<2019-ileikis-upper-tail-bounds-stars_images/imageFile37.png>)

D 2

![image 38](<2019-ileikis-upper-tail-bounds-stars_images/imageFile38.png>)

·

np e⌈Dj⌉

![image 39](<2019-ileikis-upper-tail-bounds-stars_images/imageFile39.png>)

⌈Dj⌉ 2

![image 40](<2019-ileikis-upper-tail-bounds-stars_images/imageFile40.png>)

≤ n−4

np e⌈Dj⌉

![image 41](<2019-ileikis-upper-tail-bounds-stars_images/imageFile41.png>)

⌈Dj⌉/2

.

Plugging this into (19) readily establishes inequality (18), since trivially ND

j

= 0 when Dj > n.

![image 42](<2019-ileikis-upper-tail-bounds-stars_images/imageFile42.png>)

![image 43](<2019-ileikis-upper-tail-bounds-stars_images/imageFile43.png>)

![image 44](<2019-ileikis-upper-tail-bounds-stars_images/imageFile44.png>)

![image 45](<2019-ileikis-upper-tail-bounds-stars_images/imageFile45.png>)

For the proof of the upper bound of Theorem 1 it remains to pick suitable D, i.e., which satisﬁes the technical assumption (17) and yields the ‘correct’ exponent in (13) and suitable applications of (18).

- Proof of the upper bound in (3) of Theorem 1. For concreteness, deﬁne β := 1/32 and γ := 1/(16r), as well as


A := max e4, 8/γ , s := log(e/pγ), and D := A · max 1,

min{µ1/r,n} s1/(r−1)

![image 46](<2019-ileikis-upper-tail-bounds-stars_images/imageFile46.png>)

.

For later reference, we record that there is a constant d = d(r) > 0 such that, for n ≥ n0(r),

dnr+1pr ≤ µ ≤ nr+1pr. (20) By Lemma 6, the upper tail of the number X = Xr,n,p of K1,r-copies satisﬁes

P(X ≥ (1 + ε)µ) ≤ P(XD ≥ µ + εµ/2) + P(¬T (β,D,εµ)). (21)

Gearing up to bound P(¬T (β,D,εµ)) via Lemma 9, using e = pγes and inequality (20) together with the bound s1/(r−1) ≤ s = 1 + log p−γ ≤ p−γ (as 1 + x ≤ ex) it follows that

e−s A

np1−γe−s D

np eD

=

≤ {p≤n−1/(1−γ)}

![image 47](<2019-ileikis-upper-tail-bounds-stars_images/imageFile47.png>)

![image 48](<2019-ileikis-upper-tail-bounds-stars_images/imageFile48.png>)

![image 49](<2019-ileikis-upper-tail-bounds-stars_images/imageFile49.png>)

e−s Amin{d1/rn1/rp2γ, p2γ−1}

≤

+ {p>n−1/(1−γ)}

![image 50](<2019-ileikis-upper-tail-bounds-stars_images/imageFile50.png>)

e−s A

≤ e−s, (22)

![image 51](<2019-ileikis-upper-tail-bounds-stars_images/imageFile51.png>)

where here and below we shall always tacitly assume n ≥ n0(r,d) whenever necessary. Since the above calculation also gives D ≥ Anp1−γ, together with D ≥ A it follows that

e3np/D D ≤ (pγ/e)D ≤ {p≤n−1}n−Aγ + {p>n−1}e−Anp

1−γ

≤ n−8.

Applying a union bound argument, using estimates (18), Dj = 2jD ≥ D, and (22) it follows that P(¬T (β,D,εµ)) ≤

βM/2

1 n3

1 n2

np eD

· e−βMs/2. (23)

≥ βM/Dj) ≤ n ·

P(ND

≤

![image 52](<2019-ileikis-upper-tail-bounds-stars_images/imageFile52.png>)

![image 53](<2019-ileikis-upper-tail-bounds-stars_images/imageFile53.png>)

![image 54](<2019-ileikis-upper-tail-bounds-stars_images/imageFile54.png>)

j

j∈N

Recalling (21) and the deﬁnition of M = M(εµ), by applying Corollary 8 with t := εµ it follows that there is a constant c = c(β,A,γ,r) > 0 and suitable parameters ζ,Π > 0 such that

min{ε,ε2}µ 48Dr−1

1 n2

βMs 2 ≤ (1 + n−2) · exp −c min{ε, ε2, ε1/r}

+

exp −

P(X ≥ (1 + ε)µ) ≤ exp −

![image 55](<2019-ileikis-upper-tail-bounds-stars_images/imageFile55.png>)

![image 56](<2019-ileikis-upper-tail-bounds-stars_images/imageFile56.png>)

![image 57](<2019-ileikis-upper-tail-bounds-stars_images/imageFile57.png>)

min µ, max µ1/r, µ/nr−1 s

![image 58](<2019-ileikis-upper-tail-bounds-stars_images/imageFile58.png>)

![image 59](<2019-ileikis-upper-tail-bounds-stars_images/imageFile59.png>)

![image 60](<2019-ileikis-upper-tail-bounds-stars_images/imageFile60.png>)

![image 61](<2019-ileikis-upper-tail-bounds-stars_images/imageFile61.png>)

=:ζ

=:Π

.

(24)

We ﬁnd the above upper tail estimate very satisfactory, but in the literature it has become standard to suppress multiplicative factors such as 1+n−2 in (24), which is straightforward when cζΠ ≥ 1 holds (rescaling the exponent cζΠ by a factor of 1/2, say). In the remaining case 1 > cζΠ Markov’s inequality gives

ε 1 + ε

ε 1 + ε

1 1 + ε

≤ exp −2c min{ε,1}ζΠ . Finally, noting s = log(e/pγ) ≥ log(1/pγ) = γ log(1/p) then establishes the upper bound in (3).

= 1 −

≤ exp −

P(X ≥ (1 + ε)µ) ≤

![image 62](<2019-ileikis-upper-tail-bounds-stars_images/imageFile62.png>)

![image 63](<2019-ileikis-upper-tail-bounds-stars_images/imageFile63.png>)

![image 64](<2019-ileikis-upper-tail-bounds-stars_images/imageFile64.png>)

![image 65](<2019-ileikis-upper-tail-bounds-stars_images/imageFile65.png>)

![image 66](<2019-ileikis-upper-tail-bounds-stars_images/imageFile66.png>)

![image 67](<2019-ileikis-upper-tail-bounds-stars_images/imageFile67.png>)

![image 68](<2019-ileikis-upper-tail-bounds-stars_images/imageFile68.png>)

![image 69](<2019-ileikis-upper-tail-bounds-stars_images/imageFile69.png>)

- 2.2 Extension of the argument to Theorem 2 and 5


We now extend the arguments from Section 2.1 to the upper bounds of Theorem 2 and 5. To obtain subGausssian decay ϕ(ε)µ2/σ2 in the exponent of tail-inequality (13) for XD, in view of the well-known variance estimate σ2 = Θr,ξ((1 + (np)r−1)µ) from Remark 3 we here would like to pick D = Θr,ξ(1 + np) for some range of t = εµ. However this choice causes a major problem:5 in the key estimate (22) we can no longer win an extra log-factor (via np/(eD) ≤ e−s) when we bound the ND

variables using (18) from Lemma 9. Our strategy for overcoming this obstacle is to reﬁne the technical event T = T (β,D,t), by enforcing diﬀerent upper bounds on ND

j

when Dj = 2jD is small (so that in the probabilistic arguments we automatically win an extra logarithmic factor, without destroying the combinatorial counting arguments from Lemma 6). Turning to the details, for γ,β,D,t > 0 let T + = T +(γ,β,D,t) denote the ‘technical’ event that

j

ND

j

ND

j

βMs Dj

<

![image 70](<2019-ileikis-upper-tail-bounds-stars_images/imageFile70.png>)

βM Dj

<

![image 71](<2019-ileikis-upper-tail-bounds-stars_images/imageFile71.png>)

for all j ∈ N with Dj < min{M,n}/s1/(r−1), and (25)

for all j ∈ N with Dj ≥ min{M,n}/s1/(r−1), (26)

where, in addition to the parameters M = max{t1/r,t/nr−1} and Dj = 2jD from (9), we tacitly used s = s(γ) := log(e/pγ). (27)

- Lemma 10. Given β ∈ (0,1/64] and γ,D,t > 0, the event T +(γ,β,D,t) implies XD ≤ X ≤ XD + t/2.


Proof. The proof of Lemma 6 carries over, except for the ﬁnal inequalities (10)–(11) that bound X from above. Recalling that M = min{M,n}, by mimicking the argument leading to (10) we here obtain

![image 72](<2019-ileikis-upper-tail-bounds-stars_images/imageFile72.png>)

X − XD ≤

0≤j<J

Dj · 4Djr−1 ≤ 8βM · s

2ND

j

j∈N:Dj<M/s1/(r−1)

![image 73](<2019-ileikis-upper-tail-bounds-stars_images/imageFile73.png>)

Djr−1 +

Djr−1 .

j∈N:M/s1/(r−1)≤Dj≤M

![image 74](<2019-ileikis-upper-tail-bounds-stars_images/imageFile74.png>)

![image 75](<2019-ileikis-upper-tail-bounds-stars_images/imageFile75.png>)

Recalling Dj = 2jD and r ≥ 2, using β ≤ 1/64 it then follows similarly to (10)–(11) that

X − XD ≤ 8βM · 4Mr−1 ≤ 32β · min{Mr,Mnr−1} ≤ t/2, which completes the proof.

![image 76](<2019-ileikis-upper-tail-bounds-stars_images/imageFile76.png>)

![image 77](<2019-ileikis-upper-tail-bounds-stars_images/imageFile77.png>)

![image 78](<2019-ileikis-upper-tail-bounds-stars_images/imageFile78.png>)

![image 79](<2019-ileikis-upper-tail-bounds-stars_images/imageFile79.png>)

![image 80](<2019-ileikis-upper-tail-bounds-stars_images/imageFile80.png>)

![image 81](<2019-ileikis-upper-tail-bounds-stars_images/imageFile81.png>)

5For D = Θr,ξ(1 + np) another problem is that the technical assumption (17) of Lemma 9 then breaks when np is close to one, which partially explains why in the upcoming Theorem 11 we shall exclude fairly small t when np ∈ (n−γ, γ log n).

We are now ready to prove the following slightly more general upper tail estimate for the number X = Xr,n,p of K1,r-copies in Gn,p, which (as we shall see) implies the upper bounds in Theorems 2 and 5. Theorem 11 (Upper tail bounds: technical result). Given r ≥ 2, let X = Xr,n,p. Set µ := EX, Λ := µ(1 + (np)r−1), and ϕ(x) := (1 + x)log(1 + x) − x. Given γ > 0, suppose that either

np  ∈ (n−γ,γ log n) or t2/µ ≥ {t≤min{µ,nr}}γ min t1/r(log n)r, Ms(log n)r−1 holds, where the parameters M and s are deﬁned in (9) and (27). Then we have

P(X ≥ µ + t) ≤ (1 + n−1) · exp −Ωr,γ min ϕ(t/µ)µ2/Λ, M log(e/p) . (28)

Proof. Let β := 1/64. We distinguish the following three cases: (i) np ≥ γ log n, (ii) np ≤ n−γ, and

- (iii) t2/µ ≥ {t≤min{µ,nr}}γ min{t1/r(log n)r,Ms(log n)r−1}. Note that in all three cases we may assume γ ≤ 1/(16r), since decreasing γ yields a less restrictive assumption. Furthermore, in case (iii) we may also assume that n−γ ≤ np ≤ log n holds (otherwise case (i) or (ii) apply). For concreteness, deﬁne


A := max e4, 8 · (3/γ)1/(r−1), 8/γ and D := A · max 1 + np,

ϕ(t/µ)µ Ms

![image 82](<2019-ileikis-upper-tail-bounds-stars_images/imageFile82.png>)

1/(r−1)

.

(We remark that in cases (i)–(ii) the simpler choice D = A(1+np) suﬃces.) We defer the somewhat technical proofs of the following claims regarding Lemma 9: (a) assumption (17) holds, and (b) inequality (18) implies

P ¬T +(β,γ,D,t) ≤

1 n

max e−βMs/2, e−Ψ with Ψ := ϕ(t/µ)µ2/Λ, (29)

![image 83](<2019-ileikis-upper-tail-bounds-stars_images/imageFile83.png>)

where here and below we shall again tacitly assume n ≥ n0(r). Analogously to inequalities (21) and (24), by ﬁrst applying Lemma 10 and Corollary 8, and then using (1 + np)r−1 = Θr(Λ/µ), it follows that

ϕ(t/µ)µ 16Dr−1

+ n1 exp −β2 min Ψ, Ms ≤ (1 + n−1) · exp −Ωr,γ min Ψ, Ms . Since s = log(e/pγ) ≥ γ log(e/p), this establishes inequality (28).

P(X ≥ µ + t) ≤ exp −

![image 84](<2019-ileikis-upper-tail-bounds-stars_images/imageFile84.png>)

![image 85](<2019-ileikis-upper-tail-bounds-stars_images/imageFile85.png>)

![image 86](<2019-ileikis-upper-tail-bounds-stars_images/imageFile86.png>)

It remains to verify claims (a) and (b) above, and start with claim (a), i.e., that the assumption (17) of Lemma 9 holds. Note that D ≥ A(1 + np) ≥ e4np. Furthermore, in case (i) we have D ≥ Aγ log n, and in case (ii) we have np ≤ n−γ and D ≥ A. So, in both cases, using A ≥ 8/γ we infer

e3np/D D ≤ min e−D,(np)D ≤ n−Aγ ≤ n−8. (30)

Proceeding analogously, in the cumbersome case (iii) it suﬃces to show D ≥ 8 log n. Using γ ≤ 1/(16r), p ≥ n−1−γ and (20), it is routine to see that s ≤ log n and µ ≥ n1/2. Assuming t ≥ µ, by ﬁrst using (15) and then distinguishing the cases t ≥ nr (where M = t/nr−1) and t ≤ nr (where M = t1/r), it follows that

Ar−1ϕ(t/µ)µ Ms

Dr−1 ≥

≥

![image 87](<2019-ileikis-upper-tail-bounds-stars_images/imageFile87.png>)

Ar−1t 3Ms

![image 88](<2019-ileikis-upper-tail-bounds-stars_images/imageFile88.png>)

Ar−1 min nr−1, µ1−1/r 3 logn

≥ (Alog n)r−1. (31)

≥

![image 89](<2019-ileikis-upper-tail-bounds-stars_images/imageFile89.png>)

Assuming t ≤ µ, we note that assumption p ≤ (log n)/n implies µ ≤ nr (hence t ≤ nr and thus M = t1/r, as noted above). Hence, by ﬁrst using (15) and then the assumed lower bound on t from case (iii), we infer

Ar−1ϕ(t/µ)µ Ms

Dr−1 ≥

≥

![image 90](<2019-ileikis-upper-tail-bounds-stars_images/imageFile90.png>)

Ar−1t2 3µMs

γAr−1 min{t1/r(log n)r,Ms(log n)r−1} 3Ms

= γ/3 · (Alog n)r−1.

≥

![image 91](<2019-ileikis-upper-tail-bounds-stars_images/imageFile91.png>)

![image 92](<2019-ileikis-upper-tail-bounds-stars_images/imageFile92.png>)

Each time D ≥ 8 logn follows readily by deﬁnition of A, establishing claim (a), as discussed above.

Finally, we verify claim (b), i.e., that inequality (18) implies estimate (29). We start by observing that if T +(β,γ,D,t) fails then a fortiori ND

≥ 1. Hence, using (18) with x = 1 and D0 = D ≥ e3np, we deduce

0

P(¬T +(β,γ,D,t)) ≤ P(ND

0

≥ 1) ≤

1 n3

· e−D. (32)

![image 93](<2019-ileikis-upper-tail-bounds-stars_images/imageFile93.png>)

Analogously to (23), using inequality (18) and Dj = 2jD ≥ e3np it also follows that P(¬T +(β,γ,D,εµ)) ≤

≥ βMs/Dj) +

P(ND

P(ND

j

![image 94](<2019-ileikis-upper-tail-bounds-stars_images/imageFile94.png>)

![image 95](<2019-ileikis-upper-tail-bounds-stars_images/imageFile95.png>)

j∈N:Dj≤M/s1/(r−1)

j∈N:Dj≥M/s1/(r−1)

βM/2

1 n2

1 n2

np e M/s1/(r−1)

· e−βMs +

≤

.

·

![image 96](<2019-ileikis-upper-tail-bounds-stars_images/imageFile96.png>)

![image 97](<2019-ileikis-upper-tail-bounds-stars_images/imageFile97.png>)

![image 98](<2019-ileikis-upper-tail-bounds-stars_images/imageFile98.png>)

![image 99](<2019-ileikis-upper-tail-bounds-stars_images/imageFile99.png>)

≥ βM/Dj)

j

(33)

We now use a fairly technical case distinction to verify that the two estimates (32)–(33) together imply (29). Assuming M ≥ np1−2γ, analogously to the proof of (22) we have nps/M ≤ p2γs ≤ pγ = e1−s, so that

![image 100](<2019-ileikis-upper-tail-bounds-stars_images/imageFile100.png>)

![image 101](<2019-ileikis-upper-tail-bounds-stars_images/imageFile101.png>)

np e M/s1/(r−1)

![image 102](<2019-ileikis-upper-tail-bounds-stars_images/imageFile102.png>)

![image 103](<2019-ileikis-upper-tail-bounds-stars_images/imageFile103.png>)

βM/2

≤

nps eM

![image 104](<2019-ileikis-upper-tail-bounds-stars_images/imageFile104.png>)

![image 105](<2019-ileikis-upper-tail-bounds-stars_images/imageFile105.png>)

βM/2

≤ e−βMs/2 when M ≥ np1−2γ. (34)

![image 106](<2019-ileikis-upper-tail-bounds-stars_images/imageFile106.png>)

Next we assume p ≤ n−1/(1−γ), which implies np/e ≤ pγ/e = e−s, so that

np e M/s1/(r−1)

![image 107](<2019-ileikis-upper-tail-bounds-stars_images/imageFile107.png>)

![image 108](<2019-ileikis-upper-tail-bounds-stars_images/imageFile108.png>)

βM/2

≤

np e

![image 109](<2019-ileikis-upper-tail-bounds-stars_images/imageFile109.png>)

βM/2

≤ e−βMs/2 when p ≤ n−1/(1−γ). (35)

In the remaining case M < np1−2γ and p ≥ n−1/(1−γ) hold. Since M < n implies M = M, we infer t ≤ Mr = (M)r ≤ nrpr−2rγ. So, recalling that Ψ ≤ t2/Λ ≤ t2/[(np)r−1µ] by (15) and that µ ≥ dnr+1pr by (20), using D ≥ np, p ≥ n−1/(1−γ) and γ ≤ 1/(16r) we deduce that

![image 110](<2019-ileikis-upper-tail-bounds-stars_images/imageFile110.png>)

![image 111](<2019-ileikis-upper-tail-bounds-stars_images/imageFile111.png>)

![image 112](<2019-ileikis-upper-tail-bounds-stars_images/imageFile112.png>)

![image 113](<2019-ileikis-upper-tail-bounds-stars_images/imageFile113.png>)

t2 (np)rµ

Ψ D

≤

![image 114](<2019-ileikis-upper-tail-bounds-stars_images/imageFile114.png>)

![image 115](<2019-ileikis-upper-tail-bounds-stars_images/imageFile115.png>)

nrpr−4rγ µ

≤

![image 116](<2019-ileikis-upper-tail-bounds-stars_images/imageFile116.png>)

1 dnp4rγ

≤

≤

![image 117](<2019-ileikis-upper-tail-bounds-stars_images/imageFile117.png>)

1 dn1−4rγ/(1−γ)

![image 118](<2019-ileikis-upper-tail-bounds-stars_images/imageFile118.png>)

1 dn1/2

≤

≤ 1,

![image 119](<2019-ileikis-upper-tail-bounds-stars_images/imageFile119.png>)

establishing D ≥ Ψ. It follows that

e−D ≤ e−Ψ when M < np1−2γ and p ≥ n−1/(1−γ), (36) which together with inequalities (32)–(35) implies the claimed estimate (29).

![image 120](<2019-ileikis-upper-tail-bounds-stars_images/imageFile120.png>)

![image 121](<2019-ileikis-upper-tail-bounds-stars_images/imageFile121.png>)

![image 122](<2019-ileikis-upper-tail-bounds-stars_images/imageFile122.png>)

![image 123](<2019-ileikis-upper-tail-bounds-stars_images/imageFile123.png>)

![image 124](<2019-ileikis-upper-tail-bounds-stars_images/imageFile124.png>)

We now deduce the upper bounds of Theorem 2 and 5 from the upper tail inequality (28).

- Proof of the upper bound in (4) of Theorem 2. Let γ := 1/(9r). For t := εµ ≥ n−αµ and n ≥ n0(r) it is routine to check that t2−1/r/µ ≥ {np≥n−γ}γ(log n)r holds for α = α(r) > 0 suﬃciently small. Hence Theorem 11 applies with t = εµ, where Λ = Θr,ξ(σ2) by Remark 3. Using Φ(ε) ≥ 1 it follows that


P(X ≥ (1 + ε)µ) ≤ (1 + n−1) · e−Ω

r,ξ(Φ(ε)) ≤ e−Ω

r,ξ(Φ(ε)), (37)

establishing the upper bound in (4). For Theorem 5 we shall simplify the form of the exponent in (28) via the following auxiliary result, writing an ≍ bn instead of an = Θ(bn) for typographic reasons (the assumption p ≥ n−9 in (ii) is ad-hoc). Lemma 12. Given ξ ∈ (0,1), the following holds whenever p ∈ (0,1 − ξ].

![image 125](<2019-ileikis-upper-tail-bounds-stars_images/imageFile125.png>)

![image 126](<2019-ileikis-upper-tail-bounds-stars_images/imageFile126.png>)

![image 127](<2019-ileikis-upper-tail-bounds-stars_images/imageFile127.png>)

![image 128](<2019-ileikis-upper-tail-bounds-stars_images/imageFile128.png>)

- (i) If t ≤ µ, then t2/σ2 ≍ ϕ(t/µ)µ2/σ2 ≍r,ξ ϕ(t/µ)µ2/Λ. (38)
- (ii) If t ≥ µ and t1−1/r ≥ (log n) {p<1/n}, then p ≥ n−9 implies t2/σ2 ≥ ϕ(t/µ)µ2/σ2 ≍r,ξ ϕ(t/µ)µ2/Λ = Ωr,ξ M log(e/p) . (39)
- (iii) If t2/σ2 ≥ min{M,1} and µ + t ≥ 1, then t = Ωr,ξ(1).


Proof. Inequality (38) and the ﬁrst two estimates of equation (39) follow immediately from (15) and Λ = Θr,ξ(σ2), see Remark 3. We now turn to the ﬁnal inequality of equation (39). By combining (15) and Λ/µ = 1+(np)r−1 with M = max{t1/r,t/nr−1} and t1−1/r ≥ (log n) {p<1/n}+µ1−1/r {p≥1/n}, using p ≥ n−9 and µ1−1/r = Ωr(n1/r(np)r−1), see (20), it follows similarly to (31) that

ϕ(t/µ)µ2/Λ M

≥

![image 129](<2019-ileikis-upper-tail-bounds-stars_images/imageFile129.png>)

tµ 3ΛM

![image 130](<2019-ileikis-upper-tail-bounds-stars_images/imageFile130.png>)

min{t1−1/r, nr−1} 6 max{1, (np)r−1}

≥

≥

![image 131](<2019-ileikis-upper-tail-bounds-stars_images/imageFile131.png>)

1 6

min log n,

![image 132](<2019-ileikis-upper-tail-bounds-stars_images/imageFile132.png>)

µ1−1/r (np)r−1

, nr−1,

![image 133](<2019-ileikis-upper-tail-bounds-stars_images/imageFile133.png>)

1 pr−1

![image 134](<2019-ileikis-upper-tail-bounds-stars_images/imageFile134.png>)

= Ωr log(e/p) ,

where we exploited that calculus gives pr−1 log(e/p) = Or(1); this completes the proof of claims (i)–(ii).

For claim (iii) we may of course assume t ≤ 1/2 (otherwise there is nothing to show). Hence t2/σ2 ≥ min{M,1} ≥ min{t1/r,1} = t1/r implies t2−1/r ≥ σ2 = Ωr,ξ(µ) by Remark 3, which in turn gives t = Ωr,ξ(1), because t + µ ≥ 1 and t ≤ 1/2 together imply µ ≥ 1 − t ≥ 1/2, completing the proof.

![image 135](<2019-ileikis-upper-tail-bounds-stars_images/imageFile135.png>)

![image 136](<2019-ileikis-upper-tail-bounds-stars_images/imageFile136.png>)

![image 137](<2019-ileikis-upper-tail-bounds-stars_images/imageFile137.png>)

![image 138](<2019-ileikis-upper-tail-bounds-stars_images/imageFile138.png>)

- Proof of the upper bound in (6) of Theorem 5. Applying Theorem 11 (with γ = 1), using (i)–(ii) of Lemma 12

it follows that inequality (28) holds with Ωr,ξ(Ψ(t)) in the exponent, where Ψ(t) ≥ min{1,t1/r} = Ωr,ξ(1) by (iii) of Lemma 12. Absorbing the 1+n−1 factor similar to (37) then establishes the upper bound in (6).

![image 139](<2019-ileikis-upper-tail-bounds-stars_images/imageFile139.png>)

![image 140](<2019-ileikis-upper-tail-bounds-stars_images/imageFile140.png>)

![image 141](<2019-ileikis-upper-tail-bounds-stars_images/imageFile141.png>)

![image 142](<2019-ileikis-upper-tail-bounds-stars_images/imageFile142.png>)

- Proof of the upper bound in (7) of Theorem 5. Since σ2 = Ωr,ξ(µ) by Remark 3, note that the assumption t2/σ2 ≥ M log(e/p) · (log n)2r (40)


implies t2/µ ≥ M log(e/p) · (log n)r−1, so that Theorem 11 (with γ = 1) applies. Using (40), by (iii) of Lemma 12 we also infer that M ≥ t1/r = Ωr,ξ(1). Absorbing the 1 + n−1 factor as before, it remains to show that the exponent of inequality (28) is Ωr,ξ(M log(e/p)). For t ≤ µ this follows from (38) of Lemma 12 and (40). For t ≥ µ this follows from (39) of Lemma 12, since (40) and p < n−1 imply t2/(log n)2r+1 ≥ σ2M = Ωr,ξ(µ) = Ωr,ξ(1) and thus t1−1/r ≥ (log n) {p<1/n}, as required.

![image 143](<2019-ileikis-upper-tail-bounds-stars_images/imageFile143.png>)

![image 144](<2019-ileikis-upper-tail-bounds-stars_images/imageFile144.png>)

![image 145](<2019-ileikis-upper-tail-bounds-stars_images/imageFile145.png>)

![image 146](<2019-ileikis-upper-tail-bounds-stars_images/imageFile146.png>)

- 2.3 Straightforward extension to a certain sum of iid variables


We close this section by recording that minor (and in fact simpler) variants of our proofs also apply to the following sum of independent random variables:

X :=

i∈[n]

Yi r

with independent Yi ∼ Bi(n,p). (41)

Indeed, in view of the structural similarities to the number of r-armed stars in Gn,p (which satisﬁes Xn,r,p =

dv

Yi r , and deﬁne Nx as the number

r , writing dv for the degree of v), here we set Xx := i∈[n]:Y

v∈[n]

i≤⌊x⌋

of i ∈ [n] with Yi ≥ ⌈x⌉. Now the proofs of Lemma 6 and 10 carry over with minor changes: exploiting that there are no dependencies between the Yi, using a simple dyadic decomposition we here obtain

X ≤ XD +

0≤j<J

·

ND

j

⌊Dj+1⌋ r

≤ XD + 2

ND

0≤j<J

Djr ≤ ··· ≤ XD + t/2.

j

For the proof of Corollary 8 it suﬃces to show that XD ≤ ZC holds in the present setting. Since Yi is a sum of n independent indicators ξi,j, we may write each Y

r as a sum of nr dependent indicators (which each are products of some r distinct independent variables ξi,j). Using the constraint Yi ≤ ⌊D⌋ the analogous left hand side of (14) is thus bounded by r· ⌊rD−1⌋ ≤ 2Dr−1, which in turn implies XD ≤ ZC, as desired. Since the proof of Lemma 9 also remains valid (as inequality (19) carries over), we thus arrive at the following result. Theorem 13 (Upper tail bounds: an extension). The upper bounds on the upper tail P(X ≥ (1 + ε)µ) from Theorem 1, 2, 5, and 11 remain valid for the random variable X deﬁned in (41).

i

Perhaps surprisingly, we are not aware of any standard method or inequality (for sums of iid variables) which can routinely recover the upper tail bounds from Theorem 13. Here one technical diﬃculty seems to be that each summand Y

r has an upper tail that decays slower than exponentially (for r ≥ 2), which presumably is closely linked to the somewhat non-standard log(1/p) term in the exponent. Acknowledgements. We would like to thank Svante Janson for a helpful discussion, and the CPC referee report from June 2015 (on an earlier version of this paper) for suggestions concerning the presentation.

i

# References

- [1] B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math. 319 (2017), 313–347.
- [2] B. Bollob´s. Threshold functions for small subgraphs. Math. Proc. Cambridge Philos. Soc. 90 (1981), 197–206.
- [3] S. Chatterjee. The missing log in large deviations for triangle counts. Random Struct. Alg. 40 (2012), 437–451.
- [4] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math. 299 (2016), 396–450.
- [5] S. Chatterjee and S.R.S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin. 32 (2011), 1000–1017.
- [6] B. DeMarco and J. Kahn. Upper tails for triangles. Random Struct. Alg. 40 (2012), 452–459.
- [7] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Struct. Alg. 41 (2012), 469–487.
- [8] A. Dembo and N. Cook. Large deviations of subgraph counts for sparse Erd˝s–Re´nyi graphs. Preprint (2018). arXiv:1809.11148.
- [9] A. Dudek, J. Polcyn, and A. Rucin´ski. Subhypergraph counts in extremal and random hypergraphs and the fractional q-independence. J. Comb. Optim., 19, (2010), 184–199.
- [10] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Geom. Funct. Anal., 28, (2018), 1548–1596.
- [11] P. Erd˝s and A. Re´nyi. On the evolution of random graphs. Magyar Tud. Akad. Mat. Kutat´o Int. K¨ozl. 5 (1960), 17–61.
- [12] T.E. Harris. A lower bound for the critical probability in a certain percolation process. Proc. Cambridge Philos. Soc. 56 (1960), 13–20.
- [13] S. Janson. Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221–229.
- [14] S. Janson, T.  Luczak, and A. Rucin´ski. An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph. In Random graphs ’87 (Poznan´, 1987), pp. 73–87, Wiley, Chichester (1990).
- [15] S. Janson, T.  Luczak, and A. Rucin´ski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York (2000).
- [16] S. Janson and A. Rucin´ski. The infamous upper tail. Random Struct. Alg. 20 (2002), 317–342.
- [17] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math. 142 (2004), 61–92.
- [18] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica 24 (2004), 615–640.
- [19] S. Janson and A. Rucin´ski. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat. 49 (2011), 79–96.
- [20] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Struct. Alg. 48 (2016), 219–246.
- [21] J.H. Kim and V.H. Vu. Concentration of multivariate polynomials and its applications. Combinatorica 20 (2000), 417–434.
- [22] E. Lubetzky and Y. Zhao. On replica symmetry of large deviations in random graphs. Random Struct. Alg. 47

(2015), 109–146.

- [23] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Struct. Alg. 50 (2017), 420–436.
- [24] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Struct. Alg. 46 (2015), 391–395.
- [25] A. Rucin´ski. When are small subgraphs of a random graph normally distributed? Probab. Theory Related Fields 78 (1988), 1–10.
- [26] M. Sileikis.ˇ On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin. 19 (1) Paper 4

(2012), 14 pages.

- [27] M. Sileikis.ˇ Inequalities for Sums of Random Variables: a combinatorial perspective. PhD thesis, AMU Poznan´

(2012). Available from https://sites.google.com/site/matassileikis/

- [28] M. Sileikisˇ and L. Warnke. A counterexample to the DeMarco-Kahn Upper Tail Conjecture. Preprint (2018). arXiv:1809.09595.
- [29] J. Spencer. Counting extensions. J. Combin. Theory Ser. A 55 (1990). 247–255.
- [30] V.H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput. 10 (2001), 79–94.
- [31] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math. 221 (2017), 317–365.
- [32] L. Warnke. On the method of typical bounded diﬀerences. Combin. Probab. Comput. 25 (2016), 269–299.
- [33] L. Warnke. On the missing log in upper tail estimates. Preprint (2016). arXiv:1612.08561.


# A Appendix: Lower bounds on the upper tail

In this appendix we establish fairly routine lower bounds on the upper tail P(X ≥ (1+ε)µ) from Theorem 1, 2, and 5 (omitting some straightforward details). Following [31] we obtain our lower bounds via the following three events: that many copies of K1,r ‘cluster’ on few edges (see Lemma 14 and 16), that most copies of K1,r arise disjointly (see Lemma 15 and 17), and that Gn,p contains more edges than expected (see Lemma 18).

- A.1 Basic argument for Theorem 1


- For Theorem 1 we shall use two diﬀerent lower bounds, and the ﬁrst one is based on the idea that relatively few edges (which ‘cluster’ in an appropriate way) can create fairly many stars K1,r. This is formalized by the following result, which implies P(Xr,n,p ≥ x) ≥ P(F ⊆ Gn,p) = p|E(F)| since F ⊆ Gn,p enforces Xr,n,p ≥ x.


- Lemma 14 (Clustering). For every r ≥ 1 there is D = D(r) > 0 so that for all n ≥ 1 and 0 < x ≤ Xr,n,1 there is F ⊆ Kn with |E(F)| ≤ D max{x1/r,x/nr−1,1} edges such that F contains at least x copies of K1,r.

Inspired by the proofs of Theorem 1.3 and 1.5 in [17], the idea is to use a complete bipartite graph F = Ky,z with y = Θr(min{x1/r,n}) and z = Θr(x/yr), which contains yz = Θr(x/yr−1) = Or(max{x1/r,x/nr−1}) edges and at least z yr = Θr(zyr) = Ωr(x) copies of K1,r (certain border cases require minor care).

Proof of Lemma 14. Let x0 := 2(4r)r, n0 := (r+1)x0, and D := n20. If (i) x0 ≤ x ≤ nr+1/D and n ≥ n0, then we let F := Ky,z, with y := ⌈min{x1/r,n}/4⌉ and z := ⌈rrx/yr⌉. Note that F ⊆ Kn exists, since it is easy to check that 1 < y ≤ n/2 and 1 < z ≤ n/2, say (we leave the details to the reader). Furthermore, F contains

at least z yr ≥ z(y/r)r ≥ x many K1,r, and |E(F)| = yz ≤ 2rrx/yr−1 ≤ D max{x1/r,x/nr−1} edges.

If either (ii) 1 ≤ n < n0 or (iii) x > nr+1/D and n ≥ n0, then we let F := Kn, which trivially contains Xr,n,1 ≥ x copies of K1,r, and |E(F)| < n2 < max{n20,Dx/nr−1} = D max{1,x/nr−1} edges.

Finally, if (iv) x < x0 and n ≥ n0, then we let F := Kn

0

, which contains at least n0/(r + 1) = x0 > x vertex disjoint copies of K1,r and |E(F)| < n20 = D edges, completing the proof.

![image 147](<2019-ileikis-upper-tail-bounds-stars_images/imageFile147.png>)

![image 148](<2019-ileikis-upper-tail-bounds-stars_images/imageFile148.png>)

![image 149](<2019-ileikis-upper-tail-bounds-stars_images/imageFile149.png>)

![image 150](<2019-ileikis-upper-tail-bounds-stars_images/imageFile150.png>)

The second lower bound is inspired by the fact that X = Xn,r,p is approximately Poisson for small p, in which case most K1,r arise disjointly. Indeed, the following standard result bounds P(X = m) from below by the probability that there are exactly m vertex-disjoint copies of K1,r (see [7, 26, 31] for similar arguments), which for m = (1 + ε)µ will imply P(X ≥ m) ≥ e−O

r,ε(m); the precise form of (42) will be useful later on.

- Lemma 15 (Disjoint approximation). Given r ≥ 2 there are n0,b > 0 (depending only on r) such that, for all n ≥ n0, 0 < p ≤ n−1−1/(r+1) and integers m ∈ N satisfying 0 ≤ m ≤ 99 max{µ,n1/(r+1)}, we have


P(X = m) ≥ e−b ·

Xr,n,1 m

prm(1 − pr)X

n,r,1−m. (42)

Proof. Let K contain all copies of K1,r in Kn. Deﬁne Sm as the collection of all m-element subsets of K in which all stars K1,r are vertex disjoint. Given C ⊆ Sm, deﬁne IC as the event that all stars K1,r of C are present, and deﬁne DC as the event that none of the stars K1,r in K \ C are present. Note that

P(X = m) ≥

P(IC and DC) =

C∈Sm

P(IC)P(DC | IC) ≥ |Sm|prm · min

P(DC | IC).

C∈Sm

C∈Sm

Distinguishing the number of edges in which each star α ∈ K \ C overlaps with some star K1,r from the vertex-disjoint collection C ∈ Sm, using Harris inequality [12] and np = o(1) we routinely obtain

P(DC | IC) ≥ (1 − pr)X

n,r,1−m

r(mnr−j) ≥ (1 − pr)X

(1 − pr−j)O

n,r,1−me−O

r(mnp),

1≤j<r

where mnp = O(max{nr+2pr+1,n1+1/(r+1)p}) = O(1). Furthermore, with (z − y)y/y! ≤ y z ≤ zy/y!, 1 − x ≥ e−2x and Xn,r,1 = n n−r 1 in mind, basic counting (and a short calculation) gives

m

n − (r + 1)m r

Xn,r,1 m

r(m2/n).

e−O

|Sm| ≥ (n − m)

m! ≥

This completes the proof of (42) since m2 = O(max{n2(r+1)p2r,n2/(r+2)}) = O(n2/(r+2)) = o(n).

![image 151](<2019-ileikis-upper-tail-bounds-stars_images/imageFile151.png>)

![image 152](<2019-ileikis-upper-tail-bounds-stars_images/imageFile152.png>)

![image 153](<2019-ileikis-upper-tail-bounds-stars_images/imageFile153.png>)

![image 154](<2019-ileikis-upper-tail-bounds-stars_images/imageFile154.png>)

Combining the above two results, we now prove the lower bound of Theorem 1.

- Proof of the lower bound in (3) of Theorem 1. We shall tacitly assume n ≥ n0(r,ε) whenever necessary. Applying Lemma 14 with x := (1 + ε)µ, there is F ⊆ Kn with |E(F)| ≤ Or,ε(max{µ1/r,µ/nr−1}) edges that contains at least (1 + ε)µ copies of K1,r. If Φ = max{µ1/r,µ/nr−1} log(1/p), then it follows that


P(X ≥ (1 + ε)µ) ≥ P(F ⊆ Gn,p) = p|E(F)| ≥ e−O

r,ε(Φ). (43)

Otherwise Φ = µ, which by a short calculation implies µ ≤ (log n)3, say (since µ ≥ (log n)3 implies p = Ωr(n−1−1/r) ≥ n−2 and thus max{µ1/r,µ/nr−1} log(1/p) = Or(max{µ1/r,µ/nr−1} log n) < µ). Applying

- Lemma 15 with m := ⌈(1 + ε)µ⌉ < n1/(r+1), using y z ≥ (z/y)y, µ = Xn,r,1pr, 1 − x ≥ e−2x and m ≥ (1 + ε)µ ≥ 1 it follows that

P(X ≥ (1 + ε)µ) ≥ P(X = m) ≥ e−O

r(1) ·

µ m

![image 155](<2019-ileikis-upper-tail-bounds-stars_images/imageFile155.png>)

m

e−2µ ≥ e−Θ

r,ε(m) ≥ e−O

r,ε(Φ), (44)

establishing the lower bound in (3).

![image 156](<2019-ileikis-upper-tail-bounds-stars_images/imageFile156.png>)

![image 157](<2019-ileikis-upper-tail-bounds-stars_images/imageFile157.png>)

![image 158](<2019-ileikis-upper-tail-bounds-stars_images/imageFile158.png>)

![image 159](<2019-ileikis-upper-tail-bounds-stars_images/imageFile159.png>)

A.2 Reﬁned arguments for Theorem 2 and 5

For Theorem 2 and 5 we shall reﬁne the previous two lower bounds, and also introduce a new third lower bound. Each time some care is needed to obtain the ‘correct’ dependence on t = εµ in the exponent, and we start by reﬁning the ‘clustering’ based lower bound from Lemma 14 and (43).

- Lemma 16 (Reﬁned clustering bound). Given r ≥ 1 and ξ ∈ (0,1) there are n0,c > 0 (depending only on r,ξ) such that, for all n ≥ n0, p ∈ (0,1 − ξ] and t ≥ σ satisfying 1 ≤ µ + t ≤ Xr,n,1, we have

P(X ≥ µ + t) ≥ exp −c max{t1/r,t/nr−1} log(1/p) . (45)

In case of p = o(1) the basic proof idea is to obtain µ+t copies of K1,r as follows: (i) we ﬁrst use the clustering construction from Lemma 14 to plant 2t copies of K1,r, and (ii) then use Harris’ inequality and a one-sided Chebychev’s inequality to show that typically ≥ µ − t of the remaining X˜n,r,1 := Xn,r,1 − 2t other copies of K1,r are present (the crux is that the expected number of such copies is X˜n,r,1pr = µ−o(t), so having ≥ µ−t of them intuitively seems likely). For the resulting lower bound step (i) with probability pO

r(max{t1/r,t/nr−1}) thus ought to give the main contribution, making (45) plausible. For technical reasons, in the actual argument we have to plant min{(β + 1)t,⌈µ + t⌉} copies of K1,r for carefully chosen β > 0. By mimicking the proof of Theorem 21 in [31] we then easily arrive at (45) above; we leave the details to the reader.

We next reﬁne the ‘disjoint approximation’ based lower bound used in Lemma 15 and (44) for small p. The idea is that inequality (42) intuitively relates X = Xn,r,p to a binomial random variable with mean µ = Xn,r,1 · pr, which makes the following Chernoﬀ-type bound for the upper tail plausible.

- Lemma 17 (Disjoint approximation: Chernoﬀ-type lower bound). Given r ≥ 2 there are n0,c,d > 0 (depending only on r) such that, for all n ≥ n0, 0 < p ≤ n−1−1/(r+1) and t > 0 satisfying 1 ≤ µ + t ≤ 9 max{µ,n1/(r+1)}, we have

P(X ≥ µ + t) ≥ dexp(−cϕ(t/µ)µ). (46)

Noting the binomial-like form of inequality (42) it is routine to check that Lemma 15 indeed implies (46) above (e.g., by summing (42) as in the proof of Theorem 22 in [31]); we leave the details to the reader.

Our third lower bound for moderately large p it is based on the idea that a deviation in the number of edges should typically entail a deviation in the number of K1,r copies (in concrete words: if Gn,p has substantially more than n2 p edges, then we expect to have more K1,r copies than on average).

- Lemma 18 (Deviation in number of edges: sub-Gaussian type lower bound). Given r ≥ 2 and ξ ∈ (0,1)


there are n0,β,c > 0 (depending only on r,ξ) such that, setting Λ := µ(1 + (np)r−1), for all n ≥ n0, ξn−1 ≤ p ≤ 1 − ξ and σ ≤ t ≤ βµ we have

P(X ≥ µ + t) ≥ exp −cϕ(t/µ)µ2/Λ ≥ exp −ct2/Λ . (47)

Remark 19. By Remark 3, in inequality (47) we have Λ = Θr,ξ(σ2), where σ2 = VarX.

Setting ε := t/µ, the basic proof idea is to (i) condition on having |E(Gn,p)| ≥ (1+ε) n2 p edges, and (ii) then show that this conditioning converts X ≥ µ+t = (1+ε)µ into a typical event (the crux is that this conditioning

drives up the expected value of X = Xn,r,p; to see this it might help to think of the uniform random graph Gn,m with m = (1 + ε) n2 p edges). For the resulting lower bound the conditioning thus ought to give the main contribution, which by folklore results satisﬁes P(|E(Gn,p)| ≥ (1 + ε) n2 p) = exp −Θξ(ε2 n2 p)) . This makes inequality (47) plausible, since ε2 n2 p = ε2 · Θr,ξ(µ2/Λ) = Θr,ξ(t2/Λ) for the considered range of p. A simple modiﬁcation of the proof of Theorem 24 in [31] makes this idea rigorous and establishes (47) above; we leave the details to the reader (we mention in passing that a tilting argument also works here).

Stitching the above three results together, we now prove the lower bounds of Theorem 2 and 5.

Proof of the lower bound in (7) of Theorem 5. By (iii) of Lemma 12 we infer that M ≥ t1/r = Ωr,ξ(1), which in turn implies t2/σ2 ≥ M log(e/p) · (log n)2r ≥ 1 and thus t ≥ σ. Hence an application of Lemma 16 (see inequality (45)) establishes the lower bound in (7).

![image 160](<2019-ileikis-upper-tail-bounds-stars_images/imageFile160.png>)

![image 161](<2019-ileikis-upper-tail-bounds-stars_images/imageFile161.png>)

![image 162](<2019-ileikis-upper-tail-bounds-stars_images/imageFile162.png>)

![image 163](<2019-ileikis-upper-tail-bounds-stars_images/imageFile163.png>)

Proof of the lower bound in (6) of Theorem 5. We shall only assume p ≥ n−1 instead of p ≥ n−1 log n. Applying Lemmas 16 and 18, and using Remark 19, it follows that there is β = β(r,ξ) > 0 such that

r,ξ(t2/σ2) . (48)

r,ξ(M log(e/p)), {t≤βµ}e−Θ

P(X ≥ µ + t) ≥ max e−Θ

By a virtually identical calculation as in the proof of (39) from Lemma 12, for t ≥ βµ it follows that t2/σ2 ≥ Ωr,ξ(M log(e/p)) holds. After adjusting the implicit constants, it follows that we can remove the indicator in inequality (48), which in view of Ψ(t) = min{t2/σ2,M log(e/p)} establishes the lower bound in (6).

![image 164](<2019-ileikis-upper-tail-bounds-stars_images/imageFile164.png>)

![image 165](<2019-ileikis-upper-tail-bounds-stars_images/imageFile165.png>)

![image 166](<2019-ileikis-upper-tail-bounds-stars_images/imageFile166.png>)

![image 167](<2019-ileikis-upper-tail-bounds-stars_images/imageFile167.png>)

- Proof of the lower bound in (4) of Theorem 2. Set t := εµ and M := max{t1/r,t/nr−1}, as usual. Using (15) we have (εµ)2/σ2 ≥ ϕ(ε)µ2/σ2 ≥ Φ(ε) ≥ 1 by assumption, so t ≥ σ follows. In the following we shall distinguish the three cases (i) n−1 ≤ p ≤ 1 − ξ, (ii) n−1−1/(r+1) ≤ p < n−1, and (iii) 0 < p < n−1−1/(1+r).


In cases (i)–(ii) note that, say, µ1−1/r = Ωr(n1/3r) > log n holds. Using (i)–(ii) of Lemma 12, it thus suﬃces to prove the lower bound of (4) with exponent Φ(ε) replaced by Ψ(t) deﬁned in (6). In case (i) this bound follows from the above proof (valid for n−1 ≤ p ≤ 1 − ξ) of the lower bound in (6), and in case (ii) we shall now argue that this bound follows from inequality (45) of Lemma 16, by establishing that t2/σ2 = Ωr,ξ(M log(e/p)) holds. Indeed, since p < n−1 and Remark 3 imply σ2 = Θr(µ), after recalling µ1−1/r = Ωr(n1/3r) and t = εµ ≥ n−αµ it then follows for α = α(r) > 0 suﬃciently small (say, α < 1/6r) that

t2/σ2 M log(e/p)

![image 168](<2019-ileikis-upper-tail-bounds-stars_images/imageFile168.png>)

min t2−1/r, tnr−1 σ2 log(e/p)

=

![image 169](<2019-ileikis-upper-tail-bounds-stars_images/imageFile169.png>)

min µ1−1/rn−2α, nr−1−α Θr,ξ(log n)

≥

≥ 1, (49)

![image 170](<2019-ileikis-upper-tail-bounds-stars_images/imageFile170.png>)

completing the proof in cases (i)–(ii). In the remaining case (iii) Lemmas 16 and 17 imply that, for some constant d = d(r) ∈ (0,1], we have

r,ξ(M log(e/p)), {µ+t≤9 max{µ,n1/(r+1)}}e−Θ

r,ξ(ϕ(t/µ)µ) . (50)

P(X ≥ µ + t) ≥ d · max e−Θ

We claim that for µ+t > 9 max µ,n1/(r+1) we have ϕ(t/µ)µ = Ωr (M log(e/p)). Indeed, noting that ϕ(x) ≥ x(log x)/2 for x ≥ e2 ≈ 7.4 (which is easy to check by calculus), it follows that

ϕ(t/µ)µ M log(e/p)

≥

![image 171](<2019-ileikis-upper-tail-bounds-stars_images/imageFile171.png>)

min{t(r−1)/r, nr−1} log(t/µ) 2 log(e/p)

2+r) ·

= Ωr n(r−1)/(r

![image 172](<2019-ileikis-upper-tail-bounds-stars_images/imageFile172.png>)

log(t/µ) log(e/p)

![image 173](<2019-ileikis-upper-tail-bounds-stars_images/imageFile173.png>)

.

Furthermore, log(t/µ)/ log(e/p) = Ωr(1) when µ ≤ p, and log(t/µ)/ log(e/p) = Ωr((log n)−1) when µ > p. In each case the claimed inequality holds, which allows omitting the indicator in (50). Since µ = Θr(µ2/σ2) by Remark 3, now P(X ≥ µ + t) ≥ d · e−Θ

r,ξ(Φ(ε)) follows, which in view of Φ(ε) ≥ 1 completes the proof.

![image 174](<2019-ileikis-upper-tail-bounds-stars_images/imageFile174.png>)

![image 175](<2019-ileikis-upper-tail-bounds-stars_images/imageFile175.png>)

![image 176](<2019-ileikis-upper-tail-bounds-stars_images/imageFile176.png>)

![image 177](<2019-ileikis-upper-tail-bounds-stars_images/imageFile177.png>)

