arXiv:1612.08561v2[math.PR]24May2019

On the missing log in upper tail estimates

Lutz Warnke∗ 29 February, 2016; revised January 11, 2019

Abstract

In the late 1990s, Kim and Vu pioneered an inductive method for showing concentration of certain random variables X. Shortly afterwards, Janson and Rucin´ski developed an alternative inductive approach, which often gives comparable results for the upper tail P(X ≥ (1 + ε)EX). In some cases, both methods yield upper tail estimates which are best possible up to a logarithmic factor in the exponent, but closing this narrow gap has remained a technical challenge. In this paper we present a BK-inequality based combinatorial sparsiﬁcation idea that can recover this missing logarithmic term in the upper tail.

As an illustration, we consider random subsets of the integers {1, . . . , n}, and prove sharp upper tail estimates for various objects of interest in additive combinatorics. Examples include the number of arithmetic progressions, Schur triples, additive quadruples, and (r,s)-sums.

# 1 Introduction

Concentration inequalities are of great importance in discrete mathematics, theoretical computer science, and related ﬁelds. They intuitively quantify random ﬂuctuations of a given random variable X, by bounding the probability that X diﬀers substantially from its expected value µ = EX. In combinatorial applications, X often counts certain objects (e.g., the number of subgraphs or arithmetic progressions), in which case the random variable X can usually be written as a low-degree polynomial of many independent random variables. In this context concentration inequalities with exponentially small estimates are vital (e.g., to make union bound arguments amenable), and here Kim and Vu [20, 31, 33] achieved a breakthrough in the late 1990s. Their powerful concentration inequalities have since then, e.g., been successfully applied to many combinatorial problems, been included in standard textbooks, and earned Vu the George Po´lya Prize in 2008.

In probabilistic combinatorics, the exponential rate of decay of the lower tail P(X ≤ µ − t) and upper tail P(X ≥ µ + t) have received considerable attention, since they are of great importance in applications (of course, this is also an interesting problem in concentration of measure). The behaviour of the lower tail is nowadays well-understood due to the celebrated Janson- and Suen-inequalities [11, 22, 18, 17, 13]. By contrast, the behaviour of the ‘infamous’ upper tail has remained a well-known technical challenge (see also [14, 12]). Here the inductive method of Kim and Vu [20, 33] from around 1998 often yields inequalities of the form

P(X ≥ (1 + ε)µ) ≤ exp −c(ε)µ1/q , (1)

where q ≥ 1 is some constant. In 2000, Janson and Ruci´nski [15] developed an alternative inductive approach, which often gives comparable results for the upper tail, i.e., which recovers (1) up to the usually irrelevant numerical value of the parameter c. Studying the sharpness of the tail inequality (1) is an important problem according to Vu (see Section 4.8 in [33]). In fact, one main aim of the paper [15] was ‘to stimulate more research into these methods’ since ‘neither of [them] seems yet to be fully developed’. In other words, Janson and Ruci´nski were asking for further improvements of the aforementioned fundamental proof techniques (the papers [15, 33] already contained several tweaking options for decreasing q).

In this paper we address this technical challenge in cases where the inductive methods of Kim–Vu and Janson–Ruci´nski are nearly sharp. The crux is that, for several interesting classes of examples (naturally arising, e.g., in additive combinatorics), the upper tail inequality (1) is best possible up to a logarithmic factor

![image 1](<2016-warnke-missing-log-upper-tail_images/imageFile1.png>)

∗School of Mathematics, Georgia Institute of Technology, Atlanta GA 30332, USA. E-mail: warnke@math.gatech.edu. Research partially supported by NSF Grant DMS-1703516 and a Sloan Research Fellowship. Part of the work was done while the author was a member of the Department of Pure Mathematics and Mathematical Statistics, University of Cambridge.

in the exponent. Closing such narrow gaps has recently become an active area of research in combinatorial probability (see, e.g, [14, 12, 16, 6, 7, 36]). The goal of this paper is to present a new idea that can add such missing logarithmic terms to the upper tail. From a conceptual perspective, this paper thus makes a new eﬀect amenable to the rich toolbox of the Kim–Vu and Janson–Ruci´nski methods (we believe that our techniques will be useful elsewhere). For example, under certain somewhat natural technical assumptions, our methods allow us to improve the classical upper tail inequality (1) to estimates of the form

P(X ≥ (1 + ε)µ) ≤ exp −c(ε)min µ, µ1/qs with s ∈ log n, log(1/p) , (2)

where the reader may wish to tentatively think of the parameters n = ω(1) and p = o(1) as those in the binomial random graph Gn,p (here some extra assumptions are necessary, since there are examples where (1) is sharp, see Sections 1.1 and 6.1). This seemingly small improvement of (1) is conceptually important, since in several interesting applications the resulting inequality is best possible up to the value of c. Indeed, as we shall see, sharp examples with P(X ≥ (1+ε)µ) = exp −Θ(min µ,µ1/q log(1/p)) for ε = Θ(1) naturally arise when X counts various objects of great interest in additive combinatorics, such as the number of arithmetic progressions (of given length) or additive quadruples in random subsets of the integers [n] = {1,...,n}.

In the remainder of this introduction we illustrate our methods with some applications, outline our highlevel proof strategy, and discuss the structure of this paper. Noteworthily, our proof techniques do not solely rely on induction, but a blend of combinatorial and probabilistic arguments.

- 1.1 Flavour of the results


We now illustrate the main ﬂavour of our upper tail results with some concrete examples. Many important counting problems can be rephrased as the number of edges induced by the random induced subhypergraph Hp = H[Vp(H)] (see, e.g., [14, 23, 16, 36, 38]), where Vp(H) denotes the binomial random subset where each vertex v ∈ V (H) is included independently with probability p. Our methods yield the following upper tail inequality for Hp, which extends one of the main results from [36] for the special case q = 2, and sharpens one of the principle results of Janson and Ruci´nski [16] by a logarithmic factor in the exponent.

Theorem 1 (Counting edges of random induced subhypergraphs). Let 1 ≤ q < k and γ,D > 0. Assume that H is a k-uniform hypergraph with v(H) ≤ N vertices and e(H) ≥ γNq edges. Suppose that ∆q(H) ≤ D, where ∆q(H) denotes the maximum number of edges of H that contain q given vertices. Let X = e(Hp) and µ = EX. Then for any ε > 0 there is c = c(ε,k,γ,D) > 0 such that for all p ∈ (0,1] we have

P(X ≥ (1 + ε)µ) ≤ exp −c min µ, µ1/q log(e/p) . (3)

This upper tail inequality is conceptually best possible in several ways. First, the restriction to q < k is necessary (see Section 6.1 for a counterexample when q = k), Second, in several important applications (3) is sharp (yields the correct exponential rate of decay), i.e., there is a matching lower bound of form

P(X ≥ (1 + ε)µ) ≥ {1≤(1+ε)µ≤e(H)} exp −C(ε)min µ, µ1/q log(e/p) , (4)

where the restriction 1 ≤ (1 + ε)µ ≤ e(H) is natural.1 In particular, letting the edges of the hypergraph H with vertex-set V (H) = [n] encode classical objects from additive combinatorics and Ramsey Theory, sharp examples of type (3)–(4) include the number of k-term arithmetic progressions, Schur triples x + y = 2z, additive quadruples x1 + x2 = y1 + y2, and (r,s)-sums x1 + ··· + xr = y1 + ··· + ys in the binomial random subset [n]p = Vp(H) of the integers; see Section 1.1.1 and 6.1 for more details/concrete examples.

The two expressions in the exponent of the upper tail (3)–(4) correspond to diﬀerent phenomena.2 Namely, in some range we expect that X = e(Hp) is approximately Poisson, in which case P(X ≥ 2µ) decays roughly like exp(−cµ). Similarly, the exp(−cµ1/q log(1/p)) = pcµ

1/q

term intuitively corresponds to ‘clustered’ behaviour (see also [36, 28, 12]), where few vertices U ⊆ Vp(H) induce many edges in Hp = H[Vp(H)]: e.g., in each of the above-mentioned examples there always is such a set with |U| = cµ1/q and e(H[U]) ≥ 2µ, which readily implies P(X ≥ 2µ) ≥ P(U ⊆ Vp(H)) = pcµ

1/q

. Note that classical tail inequalities of form (1) fail to handle these phenomena properly (lacking Poisson behaviour and the extra log(1/p) term).

![image 2](<2016-warnke-missing-log-upper-tail_images/imageFile2.png>)

1Note that P(X ≥ (1 + ε)µ) = 0 when (1 + ε)µ > e(H), and that P(X ≥ (1 + ε)µ) = 1 − P(X = 0) when (1 + ε)µ < 1. 2A phenomenon not relevant for the qualitative accuracy of (3)–(4) is that |Vp(H)| can also be somewhat ‘bigger’

than E|Vp(H)|, which in some range yields sub-Gaussian type tail behaviour, see also [36, 28].

- 1.1.1 Upper tail examples from additive combinatorics and Ramsey theory In the following exemplary upper tail bounds (5)–(8) we tacitly allow the implicit constants to depend on ε.

- Example 2. Arithmetic progressions (APs) are central objects in additive combinatorics. Given k ≥ 3, let X = Xn,k,p denote the number of arithmetic progressions of length k in the binomial random subset [n]p of the integers (to clarify: we count k-subsets {x1,...,xk} ⊆ [n]p forming APs); note that µ = EX = Θ(n2pk). Then, for any ε > 0 and p = p(n) ∈ (0,1] satisfying 1 ≤ (1 + ε)µ ≤ Xn,k,1, we have

P(X ≥ (1 + ε)µ) = exp −Θ min µ, µ1/2 log(1/p) . (5)

- Example 3. Schur triples {x,y,z} ⊆ [n] with x+y = z (where x = y) are classical objects in Number theory and Ramsey theory (see, e.g., [10] and [9, 25]). Let X = Xn,p denote the number of Schur triples in [n]p; note that µ = EX = Θ(n2p3). Then, for any ε > 0 and p = p(n) ∈ (0,1] satisfying 1 ≤ (1 + ε)µ ≤ Xn,1, we have

P(X ≥ (1 + ε)µ) = exp −Θ min µ, µ1/2 log(1/p) . (6)

The same tail bound also holds for ℓ-sums (studied, e.g., in [1]), where the 3-element subsets satisfy x+y = ℓz.

- Example 4. Additive quadruples are 4-subsets {x1,x2,y1,y2} ⊆ [n] satisfying x1+x2 = y1+y2. The number of these quadruples is also called additive energy, which is an important quantity in additive combinatorics (see, e.g., [2, 5]). Let X = Xn,p denote the number of additive quadruples in [n]p; note that µ = EX = Θ(n3p4). Then, for any ε > 0 and p = p(n) ∈ (0,1] satisfying 1 ≤ (1 + ε)µ ≤ Xn,1, we have

P(X ≥ (1 + ε)µ) = exp −Θ min µ, µ1/3 log(1/p) . (7)

- Example 5. (r,s)-sums are (r+s)-subsets {x1,...,xr,y1,...,y2} ⊆ [n] satisfying x1+···+xr = y1+···+ys. In the special case r = s the number of these sets is called 2r-fold additive energy, which is useful in the context of Roth’s theorem (see, e.g., [5]). Given r,s ≥ 1 satisfying r + s ≥ 3, let X = Xn,r,s,p denote the number of (r,s)-sums in [n]p; note that µ = EX = Θ(nr+s−1pr+s). Then, for any ε > 0 and p = p(n) ∈ (0,1] satisfying 1 ≤ (1 + ε)µ ≤ Xn,r,s,1, we have


P(X ≥ (1 + ε)µ) = exp −Θ min µ, µ1/(r+s−1) log(1/p) . (8) Similar tail bounds also hold for integer solutions of linear homogeneous systems, see Section 6.1 for the details.

- 1.1.2 Subgraph counts in random graphs: sub-Gaussian type upper tail bounds


As a side-product, our proof techniques also yield new results with a slightly diﬀerent ﬂavour. To illustrate this with subgraph counts in the binomial random graph Gn,p, let X = XH denote the number of copies of H in Gn,p. Set µ = EX. Here sub-Gaussian type upper tail estimates3 of the form

P(X ≥ µ + t) ≤ C exp(−ct2/ VarX) (9)

have been extensively studied [24, 31, 15, 26, 19, 37, 38] during the last decades, usually with emphasis on small deviations of form √VarX ≤ t = o(µ), say (diﬀering from the large deviations regime t = Θ(µ) considered in the classical upper tail problem for subgraph counts). In particular, for so-called ‘strictly balanced’ graphs H three diﬀerent approaches [31, 15, 26] have been developed during the years 2000–2012, which each establish a form of inequality (9) for t ≤ µ = O(log n). Our methods allow us to break this logarithmic barrier slightly, answering a question of Janson and Ruci´nski [13]; see Section 6.2.1 for more details.

![image 3](<2016-warnke-missing-log-upper-tail_images/imageFile3.png>)

- Theorem 6 (Subgraph counts: sub-Gaussian type upper tail bounds). For any strictly balanced graph H there are n0,c,C,ξ > 0 such that inequality (9) holds whenever n ≥ n0 and 0 < t ≤ µ ≤ (log n)1+ξ.


![image 4](<2016-warnke-missing-log-upper-tail_images/imageFile4.png>)

3For subgraph counts lower tail estimates of sub-Gaussian type follow from Janson’s inequality (see, e.g., [18]).

- 1.2 Glimpse of the proof strategy


In contrast to most of the previous work, in this paper we take a more combinatorial perspective to concentration of measure (and avoid induction via a more iterative point of view). Our high-level proof strategy proceeds roughly as follows. In the deterministic part of the argument, we deﬁne several ‘good’ events Ei = Ei(H,ε), and show that the following implication holds:

all Ei hold =⇒ X < (1 + ε)EX. (10) In the probabilistic part of the argument, we show that for some suitable parameter Ψ we have

P(some Ei fails) ≤ exp(−Ψ). (11) Combining both parts then readily yields an exponential upper tail estimate of the form

P(X ≥ (1 + ε)EX) ≤ P(some Ei fails) ≤ exp(−Ψ).

In this paper we illustrate the above approach by implementing (10)–(11) in a general Kim–Vu/Janson– Ruci´nski type setup. To communicate our ideas more clearly, our below informal discussion again uses the simpler random induced subhypergraph setup (a more detailed sketch is given in Sections 3.1.2–3.1.3).

For the deterministic part (10), we shall crucially exploit a good event EQ,ε of the following form: all subhypergraphs with ‘small’ maximum degree have ‘not too many’ edges, i.e., that e(J ) < (1 + ε/2)EX holds for all J ⊆ Hp with ∆1(J ) ≤ Q, say. Our sparsiﬁcation idea proceeds roughly as follows. First, using combinatorial arguments (and further good events) we ﬁnd a nested sequence of subhypergraphs

Hp = Jq ⊇ Jq−1 ⊇ ··· ⊇ J2 ⊇ J1, (12)

which gradually decreases the maximum degree down to ∆1(J1) ≤ Q. The crux is that EQ,ε then implies e(J1) < (1 + ε/2)EX. In the second step we exploit various good events (and properties of the constructed sequence) to show that we obtained J1 by removing relatively few edges from Hp, such that

X = e(Hp) = e(J1) +

e(Jj+1 \ Jj) < (1 + ε/2)EX + (ε/2)EX = (1 + ε)EX. (13)

1≤j<q

In fact, the combinatorial arguments leading to (12)–(13) develop a ‘maximal matching’ based sparsiﬁcation idea from [36], which is key for handling some vertices of Hp with exceptionally high degrees, say.

The probabilistic part (11) works hand in hand with the above deterministic arguments. Similar to EQ,ε, we shall throughout work with ‘relative estimates’, i.e., which are valid for all subhypergraphs of Hp satisfying some extra properties (e.g., that ∆j(J ) ≤ Rj holds for all J ⊆ Hp with ∆j+1(J ) ≤ Rj+1). These estimates are crucial for bringing combinatorial arguments of type (12)–(13) into play (instead of relying solely on inductive reasoning), and they hinge on a concentration inequality from [36]. Perhaps surprisingly, this inequality allows us to estimate P(¬EQ,ε) and similar ‘relative’ events without taking a union bound over all subhypergraphs. For the matching based sparsiﬁcation idea brieﬂy mentioned above, we exploit the fact that the relevant ‘matchings’ guarantee the ‘disjoint occurrence’ of suitably deﬁned events. This observation allows us to estimate the probability of certain ‘bad’ events via BK-inequality based moment arguments.

Finally, in our probabilistic estimates the logarithmic terms in (2)–(3) arise in a fairly delicate way (which comes as no surprise, since there are examples where (1) is sharp). We now illustrate the underlying technical idea for binomial random variables X ∼ Bin(n,p) with µ = np, where for x ≥ e(e/p)αµ we have

x

αx

p e

n x

eµ x

px ≤

≤

= exp −αxlog e/p .

P(X ≥ x) ≤

![image 5](<2016-warnke-missing-log-upper-tail_images/imageFile5.png>)

![image 6](<2016-warnke-missing-log-upper-tail_images/imageFile6.png>)

Our proofs apply this ‘overshooting the expectation yields extra terms in the exponent’ idea to a set of carefully chosen auxiliary random variables. As the reader can guess, the technical details are, e.g., complicated by the fact that the edges of Hp are not independent, and that we may not assume x ≫ µ.

- 1.3 Guide to the paper


In Section 2 we introduce our key probabilistic tools. In Section 3 we give a fairly detailed proof outline, and present our main combinatorial and probabilistic arguments in the random induced subhypergraphs setup. In Section 4 we then extend the discussed arguments to a more general setup. In Section 5 we derive some concrete upper tail inequalities, which in Section 6 are then applied to several pivotal examples.

The reader interested in our proof techniques may wish to focus on Section 3, which contains our core ideas and arguments. The reader interested in applications may wish to skip to Section 6, where the ‘easyto-apply’ concentration inequalities of Section 5.1 are used in several diﬀerent examples. Finally, the reader interested in comparing our results with the literature may wish to focus on the general setup of Section 4.1 and the concentration inequalities in Section 5.2.

# 2 Probabilistic preliminaries

- 2.1 A Chernoﬀ-type upper tail inequality

In this subsection we state a powerful Chernoﬀ-type upper tail inequality from [36]. It might be instructive to check that, for sums X = i∈A ξi of independent random variables ξi ∈ [0,1], inequality (14) below reduces to the classical Chernoﬀ bound (writing i ∼ j if i = j, for Yi = ξi, I = A and C = 1 we have X = ZC). We think of ∼ as a ‘dependency relation’: α  ∼ β implies that the random variables Yα and Yβ are independent. For indicator random variables Yα ∈ {0,1} the condition maxβ∈J α∈J:α∼β Yα ≤ C essentially ensures that each variable Yβ with β ∈ J ‘depends’ on at most C variables Yα with α ∈ J . Intuitively, ZC deﬁned below thus corresponds to an approximation of X = α∈I Yα with ‘bounded dependencies’.

Theorem 7. Given a family of non-negative random variables (Yα)α∈I with α∈I EYα ≤ µ, assume that ∼ is a symmetric relation on I such that each Yα with α ∈ I is independent of {Yβ : β ∈ I and β  ∼ α}. Let ZC = max α∈J Yα, where the maximum is taken over all J ⊆ I with maxβ∈J α∈J:α∼β Yα ≤ C. Set ϕ(x) = (1 + x)log(1 + x) − x. Then for all C,t > 0 we have

P(ZC ≥ µ + t) ≤ exp −

ϕ(t/µ)µ C

![image 7](<2016-warnke-missing-log-upper-tail_images/imageFile7.png>)

= e−µ/C ·

eµ µ + t

![image 8](<2016-warnke-missing-log-upper-tail_images/imageFile8.png>)

(µ+t)/C

≤ min exp −

t2 2C(µ + t/3)

![image 9](<2016-warnke-missing-log-upper-tail_images/imageFile9.png>)

, 1 +

t 2µ

![image 10](<2016-warnke-missing-log-upper-tail_images/imageFile10.png>)

−t/(2C)

≤ 1 +

t µ

![image 11](<2016-warnke-missing-log-upper-tail_images/imageFile11.png>)

−t/(4C)

.

(14)

- Remark 8. In applications there often is a family of independent random variables (ξσ)σ∈A such that each Yα is a function of (ξσ)σ∈α. Then it suﬃces to deﬁne α ∼ β if α ∩ β = ∅ (as α  ∼ β implies that Yα and Yβ depend on disjoint sets of variables ξσ).
- Remark 9. Theorem 7 remains valid after weakening the independence assumption to a form of negative

correlation: it suﬃces if E( i∈[s] Yα

i

) ≤ i∈[s] EYα

i

for all (α1,...,αs) ∈ Is satisfying αi  ∼ αj for i = j. For example, writing α ∼ β if α∩ β = ∅, it is not hard to check that this weaker condition holds for variables of form Yα = wα {α∈H

m}, where the uniform model Hm = H[Vm(H)] is deﬁned as in Section 3.5.

- Remark 10. Replacing the assumption α∈I EYα ≤ µ of Theorem 7 with α∈I λα ≤ µ and minα∈I λα ≥ 0,

the correlation condition of Remark 9 can be further weakened to E( i∈[s] Yα

i

) ≤ i∈[s] λα

i

.

- Remark 11. Note that inequality (14) implies ϕ(ε) ≥ ε2/[2(1 + ε/3)] ≥ min{ε2,ε}/3 for ε ≥ 0.


Remarks 9–10 suggest that the proof of Theorem 7 is fairly robust (it exploits independence only in a limited way; see also the discussion in [36] and the proof of Lemma 4.5 in [34]).

- 2.2 The BK-inequality


In this subsection we state a convenient consequence of the BK-inequality of van den Berg and Kesten [3] and Reimer [21]. As usual in this context, we consider a sample space Ω = Ω1 ×···× ΩM with ﬁnite Ωi, and write ω = (ω1,...,ωM) ∈ Ω. Given an event E ⊆ Ω and an index set I ⊆ [M] = {1,...,M}, we deﬁne

E|I = ω ∈ E : for all π ∈ Ω we have π ∈ E whenever πj = ωj for all j ∈ I .

In intuitive words, the event E|I occurs if knowledge of the variables indexed by I already ‘guarantees’ the occurrence of E (note that all other variables are irrelevant for E|I). Given a collection (Ei)i∈C of events, for the purposes of this paper it seems easiest to introduce the convenient deﬁnition

⊡i∈C Ei = there are pairwise disjoint Ii ⊆ [M] such that

Ei|Ii occurs . (15)

i∈C

The event ⊡i∈CEi intuitively states that all Ei ‘occur disjointly’, i.e., that there are disjoint subsets of variables which guarantee the occurrence of each event Ei (the deﬁnition of ⊡ sidesteps that the usual box product is, in general, not associative). The general BK-inequality of Reimer [21] implies the following estimate.

Theorem 12. Let P be a product measure on Ω = Ω1×···×ΩM with ﬁnite Ωi. Then for any collection (Ei)i∈C of events we have

P ⊡i∈CEi ≤

P(Ei). (16)

i∈C

Remark 13. For increasing events Ei, [4] implies that inequality (16) also holds for P assigning equal probability to all outcomes ω ∈ {0,1}M with exactly m ones (as usual, an event E is called increasing if for all ω ∈ E and π ∈ Ω we have π ∈ E whenever ωj ≤ πj for all j ∈ [M]).

# 3 Core ideas and arguments

In this section we present our core combinatorial and probabilistic arguments in a slightly simpliﬁed setup. Our main focus is on the new proof ideas and methods (which we believe are more useful to the reader than the theorems), so we defer applications and concrete upper tail inequalities to Sections 5–6. This organization of the paper also makes the extension to the more general setup of Section 4 more economical. Indeed, similar to the high-level proof strategy discussed in Section 1.2, the main results of this section are Theorem 15 of form P(X ≥ (1 + ε)EX) ≤ i P(¬Ei) and Theorem 18 of form P(¬Ei) ≤ exp(−Ψi). Together they yield upper tail inequalities, and in Section 4.2 we adapt both to our more general setup.

In Section 3.1 we give a detailed proof overview, and introduce the simpler random induced subhypergraphs setup (where our main arguments and ideas are more natural). As a warm-up, in Section 3.2 we revisit existing inductive concentration methods, and reinterpret some of the underlying ideas. Section 3.3 contains our key combinatorial arguments, which hinge on ‘sparsiﬁcation’ ideas and the BK-inequality. In Section 3.4 these arguments are complemented by probabilistic estimates, which rely on the Chernoﬀ-type tail inequality Theorem 7. Finally, in Section 3.5 we demonstrate that our proofs are somewhat ‘robust’.

- 3.1 Overview


- 3.1.1 Simpliﬁed setup: random induced subhypergraph Hp


Our basic setup concerns random induced subhypergraphs. For a hypergraph H with vertex set V (H), let Vp(H) denote the binomial random vertex subset where each v ∈ V (H) is included independently with probability p. We deﬁne the subhypergraph of H induced by Vp(H) as

Hp = H[Vp(H)]. (17) Given non-negative weights (wf)f∈H, for every G ⊆ H we set

w(G) =

p}, (18)

wf {f∈H

f∈G

where our main focus is on the weighted number of induced edges w(H) = w(Hp). The ‘unweighted’ case with wf = 1 occurs frequently in the literature (see, e.g., [14, 23, 16, 36, 38]), where the random variable w(H) = e(Hp) simply counts the number of edges of H induced by Vp(H). Our arguments will also carry over to the uniform variant Hm = H[Vm(H)] deﬁned in Section 3.5 (see Remark 19).

To formulate our results, we need some more notation and deﬁnitions. As usual, we write

ΓU(H) = {f ∈ H : U ⊆ f}, (19) ∆j(H) = max

|ΓU(H)|. (20)

U⊆V (H):|U|=j

In concrete words, ΓU(H) corresponds to the set of all edges f ∈ H that contain the vertex subset U ⊆ V (H), and ∆j(H) denotes the maximum number of edges that contain j given vertices (which we think of as a ‘maximum degree’ parameter). Inspired by [15, 20, 31, 33], we now deﬁne the following two crucial assumptions (P’) and (Pq), where q ∈ N is a parameter:

(P’) Assume that maxf∈H |f| ≤ k, maxf∈H wf ≤ L and v(H) ≤ N. Deﬁne µ = Ew(H) and µj = max

p|f|−|U|. (21)

U⊆V (H):|U|=j

f∈ΓU(H)

(Pq) Assume that ∆q(H) ≤ D.

Property (P’) ensures that every edge f ∈ H has at most k vertices, that the associated edge weights satisfy 0 ≤ wf ≤ L, and that H contains at most v(H) ≤ N vertices. Although we shall not assume this, our main focus is on the common case where k + L = O(1) and N = ω(1) holds. Property (Pq) will be useful when D = O(1) holds for q < k (this is trivial for q = k). The key parameters µj intuitively quantify the ‘dependencies’ between the edges, and we think of them as average variants of the ‘maximum degree’ parameter ∆j(Hp) from (20). To see this, note that P(f ∈ Hp | U ⊆ Vp(H)) = p|f|−|U|, so (21) equals

E |ΓU(Hp)| U ⊆ Vp(H) . (22)

µj = max

U⊆V (H):|U|=j

In concrete words, after conditioning on the presence of any vertex subset U ⊆ Vp(H) of size |U| = j, the expected number of edges in Hp that contain U is at most µj (for this reason, µj can be interpreted as the ‘maximum average eﬀect’ of any j vertices or variables, see also [20, 33]). For example, if the edges of the k-uniform hypergraph H = Hn correspond to k-term arithmetic progressions, then we can take V (H) = [n], N = n, L = 1, µ = Θ(n2pk) and µj = Θ(n2−jpk−j) for 1 ≤ j ≤ q = 2 (note that ∆2(H) = O(1) holds).

- 3.1.2 The basic form of our tail estimates


In this subsection we discuss the approximate form of our upper tail estimates. As we shall see in Section 3.2, for hypergraphs H with ∆q(H) ≤ D the usual inductive concentration of measure methods [20, 15, 33] yield basic inequalities of the following form (omitting several technicalities). Given positive parameters (Rj)1≤j≤q with Rq ≥ D, for every ε > 0 there are positive constants a = a(ε,k) and b = b(k) such that roughly

bRj/Rj+1

µj Rj

P(e(Hp) ≥ (1 + ε)µ) ≤ exp −aµ/R1 +

, (23)

![image 12](<2016-warnke-missing-log-upper-tail_images/imageFile12.png>)

1≤j<q

say (see (76) of Claim 33; the freedom of choosing the parameters (Rj)1≤j≤q is part of the method, though one naturally aims at roughly µ/R1 ≈ Rj/Rj+1). The ‘prepackaged versions’ of these inequalities usually assume that the parameters satisfy roughly µ/R1 ≥ λ and Rj ≥ max{2µj,λRj+1} (see, e.g., Theorem 4.2 in [33] or Theorem 3.10 in [15]). In this case there are positive constants c = c(a,b) and C = C(q) such that

P(e(Hp) ≥ (1 + ε)µ) ≤ C exp −cλ . (24)

The punchline of this paper is that we can often improve the exponential decay of (24) if stronger bounds than Rj ≥ 2µj hold. For example, setting λ ≈ µ1/q and Rj ≈ λq−j (similar to, e.g., the proof of Corollary 6.3 in [33] or Theorem 2.1 in [32]), in the applications of Section 6.1 we naturally arrive at bounds of form

µj Rj ≈ max

max

![image 13](<2016-warnke-missing-log-upper-tail_images/imageFile13.png>)

1≤j<q

1≤j<q

µj µ(q−j)/j

= O(pα). (25)

![image 14](<2016-warnke-missing-log-upper-tail_images/imageFile14.png>)

It might be instructive to check that (25) holds with α = 1/2 for k-term arithmetic progressions with k ≥ 3. Intuitively, replacing Rj ≥ 2µj by the stronger assumption (25) improves the exponential decay of the sumterms in (23) by a factor of roughly log(1/p) for small p. Hence the exp −aµ/R1 term in (23) is the main obstacle for improving inequality (24). Here our new ‘sparsiﬁcation’ based approach is key: after some technical work it essentially allows us to replace R1 by

Q1 = max R1/ log(1/p), B ,

where B ≥ 1 is some constant (of course, we later need to be a bit careful when p ≈ 1 holds, e.g., replacing log(1/p) with log(e/p), say). More concretely, assuming (25), for µ/R1 ≥ λ, Rj ≥ λRj+1 and p = o(1) we eventually arrive (ignoring some technicalities) at a bound that is roughly of the form

P(e(Hp) ≥ (1 + ε)µ) ≤ exp −aµ/Q1 +

1≤j<q

µj Rj

![image 15](<2016-warnke-missing-log-upper-tail_images/imageFile15.png>)

bRj/Rj+1

+

µj Rj

![image 16](<2016-warnke-missing-log-upper-tail_images/imageFile16.png>)

aµ/R1

(26)

≤ C exp −c min µ, λlog(1/p) ,

with c = c(a,b,α,B) > 0 and C = q (see (80) of Theorem 34). In words, (26) essentially adds a logarithmic factor to the exponent of the classical bound (24). This improvement of (23)–(24) is conceptually important, since in several interesting examples the resulting estimate (26) is qualitatively best possible (see Section 6.1).

- 3.1.3 Sketch of the argument


In this subsection we expand on the high-level proof strategy from Section 1.2, and give a rough sketch of our main combinatorial line of reasoning (the full details are deferred to Sections 3.2–3.4 and 4.2). As we shall argue in Section 3.2, at the conceptual heart of the usual inductive concentration approaches lies the following combinatorial ‘degree’ event Dj: ∆j+1(Hp) ≤ Rj+1 implies ∆j(Hp) ≤ Rj. Given a hypergraph H with ∆q(H) ≤ Rq, for the induced number of edges e(Hp) the basic idea is that an iterative application of the events Dq−1 ∩ ··· ∩ D1 reduces the upper tail problem to

P(e(Hp) ≥ (1 + ε)µ) ≤ P(e(Hp) ≥ (1 + ε)µ and ∆q(Hp) ≤ Rq) ≤ P(e(Hp) ≥ (1 + ε)µ and ∆1(Hp) ≤ R1) +

P(¬Dj). (27)

1≤j<q

It turns out that all the probabilities on the right hand side of (27) can easily be estimated by the concentration inequality Theorem 7 (see Claim 14 and Theorem 18), which eventually yields a variant of the upper tail estimate (23). As before, the crux is that smaller values of the ‘maximum degree’ R1 translate into better tail estimates. To surpass the usual inductive approaches, similar to (26) our plan is thus to reduce the ‘degree bound’ R1 down to Q1, and here our new ‘sparsiﬁcation idea’ will be key, achieving this ‘degree reduction’ by deleting up to εµ/2 edges.

Our starting point is the observation that, via Theorem 7, we can strengthen the degree event Dj to all subhypergraphs G ⊆ Hp (see Claim 14 and Theorem 18). Namely, let Dj+ denote the event that ∆j+1(G) ≤ Qj+1 implies ∆j(G) ≤ Qj for all G ⊆ Hp. A crucial aspect of our argument is that the events Dj, Dj+ work hand in hand with the following combinatorial ‘sparsiﬁcation’ event Eq: ∆1(Hp) ≤ R1 implies existence of a subhypergraph G ⊆ Hp with e(Hp \ G) ≤ εµ/2 and ∆q−1(G) ≤ Qq−1 (tacitly assuming q ≥ 2). Intuitively, Eq states that the deletion of ‘few’ edges reduces the degree ∆q−1(Hp) down to ∆q−1(G) ≤ Qq−1.

The basic combinatorial idea of our approach is roughly as follows (see Section 3.3 for the more involved details). We ﬁrst (i) obtain the coarse degree bound ∆1(Hp) ≤ R1 via an iterative application of the degree events Dq−1 ∩ ··· ∩ D1, then (ii) exploit the sparsiﬁcation event Eq to ﬁnd a subhypergraph G ⊆ Hp with e(Hp \ G) ≤ εµ/2 and ∆q−1(G) ≤ Qq−1, and ﬁnally (iii) deduce the improved degree bound ∆1(G) ≤ Q1 via an iterative application of the degree events Dq+−2 ∩···∩ D1+. Taking into account that we obtain G ⊆ Hp by deleting up to εµ/2 edges, for hypergraphs H with ∆q(H) ≤ Rq we eventually arrive at

P(e(Hp) ≥ (1 + ε)µ) ≤ P(e(G) ≥ (1 + ε/2)µ and ∆1(G) ≤ Q1 for some G ⊆ Hp)

P(¬Dj+). (28)

P(¬Dj) + P(¬Eq) +

+

1≤j<q

1≤j<q−1

The crux is that we can again obtain good tail estimates for P(e(G) ≥ (1 + ε/2)µ ···) and P(¬Dj)+ P(¬Dj+) via Theorem 7 (see Claim 14 and Theorem 18), so in (28) it remains to bound P(¬Eq).

To estimate the probability that the sparsiﬁcation event Eq fails, we shall rely on combinatorial arguments and the BK-inequality, developing a ‘maximal matching’ based idea from [36]. Simplifying slightly (see

- Section 3.3.1 for the full details), for any vertex set U ⊆ V (H) with |U| = q − 1 we tentatively call KU ⊆ ΓU(H) = {f ∈ H : U ⊆ f} with |KU| = r an r-star, where we set r = Qq−1 for brevity. The basic idea is to take a maximal vertex disjoint collection of r-stars in Hp, which we denote by M (to clarify: the edges from any two distinct r-stars KU,KW ∈ M are vertex disjoint), and remove all edges f ∈ Hp that are incident to M, i.e., which share at least one vertex with some r-star from M. Denoting the resulting subhypergraph


by G ⊆ Hp, using maximality of M it is not diﬃcult to argue that ∆q−1(G) < r = Qq−1 holds (otherwise we could add another r-star to M). Furthermore, by construction the deleted number of edges is at most

e(Hp \ G) ≤

|Γ{v}(Hp)| ≤ |M| · r · k · ∆1(Hp). (29)

KU∈M f∈KU v∈f

Since the event Eq presupposes ∆1(Hp) ≤ R1, we thus see that |M| ≤ εµ/(2rkR1) implies |Hp\G| ≤ εµ/2. It remains to estimate the probability that |M| is big, and here we shall exploit the fact that the r-stars KU ∈ M satisfy two properties: they (i) are pairwise vertex disjoint, and (ii) each ‘guarantee’ that |ΓU(Hp)| ≥ r holds. Intuitively, the point of (i) and (ii) is that |M| events of from |ΓU(Hp)| ≥ r ‘occur disjointly’ in the sense of Section 2.2, which allows us to bring the BK-inequality (16) into play. Indeed, by analyzing a ⊡-based moment of U:|U|=q−1 {|Γ

U(Hp)|≥r}, we then eventually obtain suﬃciently good estimates for P(¬Eq), as desired (see the proofs of Lemma 16 and inequality (48) of Theorem 18).

As the reader can guess, the actual details are more involved. For example, instead of just Eq for ∆q−1(·), we also need to consider similar sparsiﬁcation events for the others degrees ∆j(·) with 1 ≤ j < q. In fact, analogous to Dj+, these events must moreover apply to all subhypergraphs G ⊆ Hp simultaneously (see Ej,ℓ(x,r,y,z) deﬁned in Section 3.3). Furthermore, due to technical reasons, the decomposition (28) requires some extra bells and whistles (see (33) of Theorem 15). Finally, we have also ignored how Theorem 7 and the BK-inequality (16) eventually allow us to convert the decompositions (27)–(28) into concrete upper tail inequalities of form (23) and (26); see Sections 3.3.1, 3.4, 4.2 and 5.3 for these technical calculations.

- 3.2 Inductive concentration proofs revisited


The goal of this warm-up section is to reinterpret the classical inductive concentration proofs from [15, 20, 33] using the following ‘degree intuition’: an (improved) upper bound for ∆j+1(Hp) and ∆1(Hp) translates into an improved upper tail estimate for ∆j(Hp) and w(Hp), respectively. We exemplify this with the following claim, which is usually stated for G = Hp only (the proof of is based on routine applications of Theorem 7, and thus deferred to Section 3.4). We ﬁnd inequalities (30)–(31) below remarkable, since they intuitively yield bounds for all subhypergraphs G ⊆ Hp without taking a union bound.

Claim 14. Given H, assume that (P’) holds. Then for all t,x,y > 0 and 1 ≤ j < k we have

−t/(4Lky)

t µ

P w(G) ≥ µ + t and ∆1(G) ≤ y for some G ⊆ Hp ≤ 1 +

, (30)

![image 17](<2016-warnke-missing-log-upper-tail_images/imageFile17.png>)

−x/(4ky)

x µj

P ∆j(G) ≥ µj + x and ∆j+1(G) ≤ y for some G ⊆ Hp ≤ Nj 1 +

. (31)

![image 18](<2016-warnke-missing-log-upper-tail_images/imageFile18.png>)

Now, by a straightforward iterative degree argument similar to (27), we obtain the simple estimate P w(G) ≥ µ + t and ∆q(G) ≤ Rq for some G ⊆ Hp ≤ P w(G) ≥ µ + t and ∆1(G) ≤ R1 for some G ⊆ Hp

P ∆j(G) > Rj and ∆j+1(G) ≤ Rj+1 for some G ⊆ Hp .

+

1≤j<q

(32)

Restricting to the special case w(Hp), using Claim 14 it turns out that inequality (32) is essentially equivalent to the basic induction of Janson and Ruci´nski [15] (see the proof of Theorem 3.10 in [15]), which in turn

qualitatively recovers the upper tail part of Kim and Vu [20] (see Section 5 of [15, 13]). The iterative point of view (32) is somewhat more ﬂexible than induction, making the arguments subjectively easier to modify (as there is no need to formulate a suitable induction hypothesis). Estimates for all subhypergraphs G ⊆ Hp also make room for additional combinatorial arguments, which is crucial for the purposes of this paper.

- 3.3 Combinatorial sparsiﬁcation: degree reduction by deletion


In this section we introduce our key combinatorial arguments, which eventually allow us to obtain improved upper tail estimates by ‘sparsifying’ Hp, i.e., deleting edges from Hp. Loosely speaking, via this sparsiﬁcation idea we can eﬀectively ignore certain ‘exceptional’ edges from Hp (which contain vertices with extremely high degree, say). For the purpose of this paper, we encapsulate this heuristic idea with the deﬁnition below. In intuitive words, for ℓ = 1 the ‘sparsiﬁcation’ event Ej,1(x,r,y,z) essentially ensures that every G ⊆ Hp with bounded ∆j+1(G) and ∆1(G) contains a large subhypergraph J ⊆ G with small ∆j(J ).

Deﬁnition (Sparsiﬁcation event). Let Ej,ℓ(x,r,y,z) denote the event that for every G ⊆ Hp with ∆j+1(G) ≤ y and ∆ℓ(G) ≤ z there is J ⊆ G with ∆j(J ) ≤ x and e(G \ J ) ≤ r.

Here one conceptual diﬀerence to the ‘deletion lemma’ of Ro¨dl and Ruci´nski [23, 14] is that our focus is on ‘local properties’ such as degrees (somewhat in the spirit of [30]), and not on ‘global properties’ such as subgraph counts. Furthermore, we are deleting edges from Hp = H[Vp(H)], whereas the classical approach corresponds to deleting vertices from Vp(H) = E(Gn,p), say.

With Ej,1(x,r,y,z) in hand, we now reﬁne4 the basic estimate (32) via the strategy outlined in Section 3.1.3 (see also (28) therein). We believe that the ideas used in the proof of Theorem 15 below are more important than its concrete statement (which is optimized for the purposes of this paper). Here one new ingredient is the edge deletion of the sparsiﬁcation events in Pj,3,ℓ of (36), which allows us to decrease certain maximum degrees. The total weight of the deleted edges can be as large as t/2, which is the reason why in (33) we need to relax w(G) ≥ µ+t to w(G) ≥ µ+t/2. In later applications we shall use Sj ≈ Rj/s with s = ω(1), and then the parametrization Qj = max{Sj,Dj} allows us to easily deal with Sj = o(1) border cases. The indicators in (35)–(36) can safely be ignored on ﬁrst reading (they mainly facilitate certain technical estimates). A key aspect of (33) is that we intuitively replace ∆1(G) ≤ R1 of (32) with ∆1(G) ≤ min{Q1,R1}, which by the discussion of Section 3.2 is crucial for obtaining improved tail estimates (see also Theorem 18).

Theorem 15 (Combinatorial decomposition of the upper tail). Given H with 1 ≤ q ≤ k, assume that (P’) holds. Suppose that t > 0. Given positive (Dj)1≤j≤q, (Rj)1≤j<q and (Sj)1≤j<q, deﬁne Rq = Qq = Dq and Qj = max{Sj,Dj} for 1 ≤ j < q. Then we have

P w(G) ≥ µ + t and ∆q(G) ≤ Dq for some G ⊆ Hp ≤ P w(G) ≥ µ + t/2 and ∆1(G) ≤ min{Q1,R1} for some G ⊆ Hp

(33)

+

Pj,1 + Pj,2 + Pj,3,1 ,

1≤j<q

where

- Pj,1 = P ∆j(G) > Rj and ∆j+1(G) ≤ Rj+1 for some G ⊆ Hp , (34)
- Pj,2 = {Q


j<Rj and Qj+1>Dj+1}P ∆j(G) > Qj and ∆j+1(G) ≤ Sj+1 for some G ⊆ Hp , (35) Pj,3,ℓ = {Q

j<Rj and Qj+1=Dj+1}P ¬Ej,ℓ(Qj,t/(2Lq),Dj+1,Rℓ) . (36)

The combinatorial proof proceeds in two sparsiﬁcation rounds. In the ﬁrst round we use our usual iterative degree argument to deduce that ∆q(G) ≤ Rq implies ∆j(G) ≤ Rj for all 1 ≤ j ≤ q. We start the second round with the sparsiﬁcation event, by deleting edges such that J ⊆ G satisﬁes ∆q−1(J ) ≤ Qq−1 (tacitly assuming Qq−1 < Rq−1, say). The idea is that our usual iterative degree argument should then allow us to deduce that ∆j+1(J ) ≤ Qj+1 implies ∆j(J ) ≤ Qj for all 1 ≤ j < q−1. Unfortunately, our later probabilistic estimates break down if the parameter Qj+1 is ‘too small’. With foresight we thus use our alternative ‘degree reduction’ argument whenever Qj+1 = Dj+1 holds, i.e., we again delete edges.

![image 19](<2016-warnke-missing-log-upper-tail_images/imageFile19.png>)

4Note that by setting Dj = Rj = Sj the indicators in (35)–(36) are zero, so (33) qualitatively reduces to (32).

Proof of Theorem 15. Inequality (33) is trivial for q = 1 (since R1 = Q1 = D1). For q ≥ 2 the plan is to show that properties (a)–(d) below deterministically imply that w(G) < µ + t for every G ⊆ Hp with ∆q(G) ≤ Dq. Using a union bound argument this then completes the proof (it is routine to check that (a)–(d) correspond to the complements of the events on the right hand side of (33), since Qj+1 > Dj+1 implies Sj+1 = Qj+1). Turning to the details, we henceforth assume that the following properties hold for all G ⊆ Hp and 1 ≤ j < q:

- (a) ∆1(G) ≤ min{Q1,R1} implies w(G) < µ + t/2,
- (b) ∆j+1(G) ≤ Rj+1 implies ∆j(G) ≤ Rj,
- (c) if Qj < Rj and Qj+1 > Dj+1, then ∆j+1(G) ≤ Qj+1 implies ∆j(G) ≤ Qj, and
- (d) if Qj < Rj and Qj+1 = Dj+1, then ∆j+1(G) ≤ Qj+1 and ∆1(G) ≤ R1 implies existence of J ⊆ G with ∆j(J ) ≤ Qj and e(G \ J ) ≤ t/(2Lq).


For the remaining deterministic argument we ﬁx G ⊆ Hp with ∆q(G) ≤ Dq, and claim that we can construct a hypergraph sequence G = Jq ⊇ ··· ⊇ J1 such that

Ri, if 1 ≤ i < j, min{Qi,Ri}, if j ≤ i ≤ q,

∆i(Jj) ≤

(37)

e(Jj+1 \ Jj) ≤ t/(2Lq). (38) With this sequence in hand, using (38) we have

wf · e(Jj+1 \ Jj) ≤ L · t/(2Lq) = t/(2q),

wf ≤ max

w(Jj+1 \ Jj) =

f∈Jj+1\Jj

f∈Jj+1\Jj

which together with ∆1(J1) ≤ min{Q1,R1} of (37) and (a) then yields w(G) = w(J1) +

w(Jj+1 \ Jj) < (µ + t/2) + (q − 1) · t/(2q) ≤ µ + t. (39)

1≤j<q

It thus remains to construct G = Jq ⊇ ··· ⊇ J1 with the claimed properties. For the base case G = Jq, using ∆q(Jq) = ∆q(G) ≤ Dq = Rq repeated applications of (b) yield that ∆i(Jq) ≤ Ri for all 1 ≤ i ≤ q, so (37) holds since ∆q(Jq) ≤ Rq = min{Rq,Qq}. Given Jj+1 with 1 ≤ j < q, our construction of Jj ⊆ Jj+1 distinguishes several cases; in view of ∆i(Jj) ≤ ∆i(Jj+1) it clearly suﬃces to check (37) for ∆j(Jj) only.

If Qj ≥ Rj, then we set Jj = Jj+1, which satisﬁes ∆j(Jj) = ∆j(Jj+1) ≤ Rj = min{Qj,Rj} by (37). If Qj < Rj and Qj+1 > Dj+1, then we set Jj = Jj+1, which by (37) satisﬁes ∆j+1(Jj) = ∆j+1(Jj+1) ≤

Qj+1. Hence (c) implies ∆j(Jj) ≤ Qj = min{Qj,Rj}.

Finally, if Qj < Rj and Qj+1 = Dj+1, then by (37) we have ∆j+1(Jj+1) ≤ Qj+1 and ∆1(Jj+1) ≤ R1. Hence (d) implies existence of Jj ⊆ Jj+1 satisfying ∆j(Jj) ≤ Qj = min{Qj,Rj} and e(Jj+1 \Jj) ≤ t/(2Lq), completing the proof.

![image 20](<2016-warnke-missing-log-upper-tail_images/imageFile20.png>)

![image 21](<2016-warnke-missing-log-upper-tail_images/imageFile21.png>)

![image 22](<2016-warnke-missing-log-upper-tail_images/imageFile22.png>)

![image 23](<2016-warnke-missing-log-upper-tail_images/imageFile23.png>)

The above proof demonstrates that estimates for all subhypergraphs G ⊆ Hp are extremely powerful along with combinatorial arguments. It seems likely that the above sparsiﬁcation approach can be sharpened in speciﬁc applications, i.e., that there is room for alternative (ad-hoc) arguments which apply the ‘degree reduction’ idea diﬀerently. For example, in [36] the degrees are iteratively reduced by a factor of two, say (replacing the ﬁnite sum in (39) by a convergent geometric series). In [28] the iterative argument also takes ‘trivial’ upper bounds for the ∆j(H) into account (which can be smaller than Rj or Qj).

- 3.3.1 A combinatorial local deletion argument


The goal of this subsection is to estimate P ¬Ej,1(x,r,y,z) , i.e., the probability that our ‘sparsiﬁcation’ event fails. As indicated in Section 3.1.3, our proof uses a maximal matching based idea which relies on combinatorial arguments and the BK-inequality. The following auxiliary event DU,x,y intuitively states that, in Hp, the vertex set U is the centre of a ‘star’ with at least x spikes (satisfying some degree constraint).

Deﬁnition (Auxiliary degree event). Let DU,x,y denote the event that there is K ⊆ ΓU(Hp) with |K| ≥ x and ∆|U|+1(K) ≤ y.

To put this deﬁnition into our ‘all subhypergraphs’ context, note that ¬DU,x,y implies |ΓU(G)| < x for all G ⊆ Hp with ∆|U|+1(G) ≤ y. It might also be instructive to note that a union bound argument yields

P(DU,x,y). (40)

P ∆j(G) ≥ x and ∆j+1(G) ≤ y for some G ⊆ Hp ≤

U⊆V (H):|U|=j

The next result relates the auxiliary event DU,x,y with the sparsiﬁcation event Ej,1(x,r,y,z). For example,

- U P(DU,x,y) ≤ B−x/y translates into P(¬Ej,1(x,r,y,z)) ≤ B−r/(kyz) by inequality (41).

Lemma 16 (Auxiliary result for the sparsiﬁcation event). Given H, assume that maxf∈H |f| ≤ k holds. Then for all x,r,y,z > 0 and 1 ≤ j < k we have

P ¬Ej,1(x,r,y,z) ≤

U⊆V (H):|U|=j

P(DU,x,y)

⌈r/(k⌈x⌉z)⌉

. (41)

Remark 17. Inequality (41) remains valid after dividing the right hand side by ⌈r/(k⌈x⌉z)⌉!.

The proof of Lemma 16 develops a combinatorial idea from [36], which in turn was partially inspired by [29, 14]. We call (U,KU) an (j,x,y)-star in G if U ⊆ V (G) and KU ⊆ ΓU(G) = {f ∈ G : U ⊆ f} satisfy |U| = j, |KU| = ⌈x⌉ and ∆j+1(KU) ≤ y. Note that we allow for overlaps of the edges f,g ∈ KU outside of the ‘centre’ U. Writing Sj,x,y(G) for the collection of all (j,x,y)-stars in G, we deﬁne Mj,x,y(G) as the size of the largest M ⊆ Sj,x,y(G) satisfying V (KU) ∩ V (KW) = ∅ for all distinct (U,KU),(W,KW) ∈ M. In intuitive words, Mj,x,y(G) denotes the size of the ‘largest (j,x,y)-star matching’ in G, i.e., vertex-disjoint collection of stars. We are now ready to follow the strategy sketched in Section 3.1.3 (see also (29) therein).

Proof of Lemma 16. Let r˜ = r/(k⌈x⌉z) and R = ⌈r˜⌉. We ﬁrst assume that Mj,x,y(Hp) ≤ r˜ holds, and claim that this implies the occurrence of Ej,1(x,r,y,z). For any G ⊆ Hp with ∆j+1(G) ≤ y and ∆1(G) ≤ z, it clearly suﬃces to show that there is J ⊆ G with ∆j(J ) ≤ x and e(G\J ) ≤ r. Let M ⊆ Sj,x,y(G) attain the maximum in the deﬁnition of Mj,x,y(G). We then remove all edges f ∈ G which overlap some star (U,KU) ∈ M, where overlap means that f ∩ g = ∅ for some edge g ∈ KU. We denote the resulting subhypergraph by J ⊆ G. Using ∆j+1(J ) ≤ ∆j+1(G) ≤ y and maximality of M, we then infer ∆j(J ) ≤ ⌈x⌉−1 < x (because otherwise we could add another (j,x,y)-star to M). Furthermore, since |M| = Mj,x,y(G) ≤ Mj,x,y(Hp) ≤ r˜ and ∆1(G) ≤ z, by construction the number of deleted edges is at most

e(G \ J ) ≤

KU∈M f∈KU v∈f

|Γ{v}(G)| ≤ |M| · ⌈x⌉ · max

f∈G

|f| · ∆1(G) ≤ r˜· ⌈x⌉kz = r. (42)

It follows that Mj,x,y(Hp) ≤ r˜ implies Ej,1(x,r,y,z), as claimed. For (41) it remains to estimate P(Mj,x,y(Hp) > r˜). Similar to the proof of Theorem 11 in [36], we set

ZR =

(U1,...,UR): Ui⊆V (H) and |Ui|=j

⊡i∈[R]DUi,x,y , (43)

where ⊡ is deﬁned as in (15). If Mj,x,y(Hp) > r˜, then there is M ⊆ Sj,x,y(Hp) of size |M| = ⌈r˜⌉ = R which satisﬁes V (KU) ∩ V (KW) = ∅ for all distinct (U,KU),(W,KW) ∈ M. So, since the disjoint vertex sets

- V (KU) ⊆ Vp(H) guarantee the occurrence of each event DU,x,y, it follows that ⊡(U,K


U)∈MDU,x,y occurs. As U ⊆ V (KU) holds, by vertex disjointness of the V (KU) we deduce that the corresponding ‘star-centres’ U are distinct. Since ZR counts ordered R-tuples, we thus infer ZR ≥ R!. Hence, Markov’s inequality yields

P(Mj,x,y(Hp) > r˜) ≤ P(ZR ≥ R!) ≤ (EZR)/R!. (44) Turning to EZR, using the BK-inequality (16) we readily obtain

P ⊡i∈[R]DUi,x,y

EZR =

(U1,...,UR): Ui⊆V (H)s and |Ui|=j

P(DUi,x,y) ≤

≤

i∈[R]

(U1,...,UR): Ui⊆V (H) and |Ui|=j

P(DU,x,y)

U⊆V (H):|U|=j

R

,

(45)

which together with (44) and R ≥ 1 completes the proof.

![image 24](<2016-warnke-missing-log-upper-tail_images/imageFile24.png>)

![image 25](<2016-warnke-missing-log-upper-tail_images/imageFile25.png>)

![image 26](<2016-warnke-missing-log-upper-tail_images/imageFile26.png>)

![image 27](<2016-warnke-missing-log-upper-tail_images/imageFile27.png>)

The ‘star-matching’ based deletion argument used in the above proof seems of independent interest. In applications it might be easier to avoid Ej,1(x,r,y,z), and directly work with the random variable Mj,x,y(Hp), see also [36, 28]. The above estimates (44)–(45) exploit the BK-inequality to relate Mj,x,y(Hp) with the simpler events DU,x,y. In Hp and other probability spaces one can sometimes also estimate P(Mj,x,y(Hp) ≥ z) more directly (see, e.g., the remark after the proof of Lemma 17 in [36], or the proof of Lemma 9 in [28]).

- 3.4 Probabilistic estimates


In this section we introduce our key probabilistic estimates, which complement the combinatorial decomposition of Theorem 15, i.e., allow us to bound the right hand side of (33). A key aspect of inequalities (46)–(47) is that improved degree constraints ∆i(G) ≤ y translate into improved tail estimates. In our applications (48) below often reduces to P ¬Ej,1(x,r,y,z) ≤ (eµj/x)−Θ(r/(yz)), say (see, e.g., the proof of Theorem 34).

Theorem 18 (Probabilistic upper tail estimates). Given H, assume that (P’) holds. Set ϕ(x) = (1 + x)log(1 + x) − x. Then for all x,r,y,z,t > 0 and 1 ≤ j < k we have

ϕ(t/µ)µ 4Lky

P w(G) ≥ µ + t/2 and ∆1(G) ≤ y for some G ⊆ Hp ≤ exp −

, (46)

![image 28](<2016-warnke-missing-log-upper-tail_images/imageFile28.png>)

x/(ky)

eµj x

P ∆j(G) ≥ x and ∆j+1(G) ≤ y for some G ⊆ Hp ≤ Nj

, (47)

![image 29](<2016-warnke-missing-log-upper-tail_images/imageFile29.png>)

⌈x⌉/(ky) ⌈r/(k⌈x⌉z)⌉

eµj ⌈x⌉

P ¬Ej,1(x,r,y,z) ≤ Nj

. (48)

![image 30](<2016-warnke-missing-log-upper-tail_images/imageFile30.png>)

The proofs of (46)–(47) are based on fairly routine applications of Theorem 7. The crux is that the restrictions ∆1(G) ≤ y and ∆j+1(G) ≤ y translate into bounds for the parameter C in (14), which intuitively controls the ‘largest dependencies’ (∆1(G) ≤ y ensures that every edge f ∈ G overlaps at most |f|·∆1(G) ≤ ky edges e ∈ G). For verifying the independence assumption of Theorem 7, we use the following simple observation: e ∩ f = ∅ implies that {e∈H

p(H)} are independent, since both depend on disjoint sets of independent variables ξσ = {σ∈V

p} = {e⊆V

p(H)} and {f∈H

p} = {f⊆V

p(H)}. Assuming (e∩f)\U = ∅, we below exploit that an analogous (conditional independence) reasoning works after conditioning on U ⊆ Vp(H). Proof of Theorem 18. With an eye on Theorem 7, inspired by Remark 8 we set ξσ = {σ∈V

p(H)}. We ﬁrst prove (46). Let Yf = wf {f∈H

p}, which satisﬁes Yf = wf σ∈f ξσ and f∈H EYf = Ew(H) = µ. Furthermore, w(G) = w∈G Yf for any G ⊆ Hp. Deﬁning α ∼ β if α ∩ β = ∅, the independence assumption of Theorem 7 holds by Remark 8. Observe that for any f ∈ G ⊆ H with ∆1(G) ≤ y we have

{e∈Hp} ≤ L ·

|Γ{v}(G)| ≤ L · |f| · ∆1(G) ≤ Lky.

we ·

Ye ≤ max

e∈G

v∈f

e∈G:e∼f

e∈G:e∩f =∅

To sum up, if w(G) ≥ µ + t/2 and ∆1(G) ≤ y for some G ⊆ Hp, then ZC ≥ µ + t/2 holds with C = Lky, where ZC is deﬁned as in Theorem 7 with I = H. So, applying (14), we deduce

ϕ(t/(2µ))µ Lky

P w(G) ≥ µ + t/2 and ∆1(G) ≤ y for some G ⊆ Hp ≤ P(ZC ≥ µ + t/2) ≤ exp −

. (49)

![image 31](<2016-warnke-missing-log-upper-tail_images/imageFile31.png>)

Using calculus (see, e.g., the proof of Lemma 13 in [36]) it is easy to check that ϕ(t/(2µ) ≥ ϕ(t/µ)/4. In view of (49) and (14), inequality (46) now follows.

Next we turn to (47), which hinges on the union bound estimate (40). Note that v(H) < 1 implies H = ∅,

- so (47) is trivial for N < 1 (the left hand side is zero). Similarly, (47) is also trivial for x ≤ eµj and N ≥ 1 (the expression on the right hand side is at least one). To sum up, we henceforth may assume x > eµj


and N ≥ 1. Given U ⊆ V (H) with |U| = j, set I := ΓU(H) = {f ∈ H : U ⊆ f}. Let Yf = {f∈H

p}, and deﬁne α ∼ β if (α ∩ β) \ U = ∅. Note that for any f ∈ K ⊆ I with ∆|U|+1(K) ≤ y we have

Ye =

e∈K:e∼f

e∈K:(e∩f)\U =∅

{e∈Hp} ≤

|ΓU∪{v}(K)| ≤ |f \ U| · ∆|U|+1(K) ≤ ky. (50)

v∈f\U

So, if DU,x,y occurs, then ZC ≥ x holds with C = ky, where ZC is deﬁned as in Theorem 7 with I = ΓU(H). For f ∈ I, note that U  ⊆ Vp(H) implies f  ∈ Hp = H[Vp(H)]. Recalling Yf = {f∈H

p(H)}, using the deﬁnition of µj (see (21)) it follows that

p} and ξσ = {σ∈V

E(Yf | (ξσ)σ∈U) =

f∈I

≤

P(f ∈ Hp | (ξσ)σ∈U) {U⊆V

p(H)}

f∈ΓU(H)

p|f|−|U| ≤ µ|U| = µj.

P(f ∈ Hp | U ⊆ Vp(H)) =

f∈ΓU(H)

f∈ΓU(H)

(51)

Furthermore, conditional on (ξσ)σ∈U, the independence assumption of Theorem 7 holds by the same reasoning as in Remark 8 (in the conditional space, each Yf is a function of the independent random variables (ξσ)σ∈f\U). So, applying (14) with µ = µj and µ + t = x > eµj, we deduce the conditional inequality

x/(ky)

eµj x

P(DU,x,y | (ξσ)σ∈U) ≤ P(ZC ≥ x | (ξσ)σ∈U) ≤

. (52) Taking expectations, by summing over all relevant U ⊆ V (H) we thus infer

![image 32](<2016-warnke-missing-log-upper-tail_images/imageFile32.png>)

x/(ky)

eµj x

EP(DU,x,y | (ξσ)σ∈U) ≤ Nj

P(DU,x,y) =

, (53)

![image 33](<2016-warnke-missing-log-upper-tail_images/imageFile33.png>)

U⊆V (H):|U|=j

U⊆V (H):|U|=j

and (47) follows in view of (40).

It remains to establish (48). Exploiting integrality of the underlying variables, note in (52) we can strengthen ZC ≥ x to ZC ≥ ⌈x⌉. In (52)–(53) we thus may replace (eµj/x)x/(ky) by (eµj/⌈x⌉)⌈x⌉/(ky), and

- so (48) follows from (41) of Lemma 16, with room to spare. The proof of Claim 14 (only used in our informal discussion) is very similar, and thus left to the reader.


![image 34](<2016-warnke-missing-log-upper-tail_images/imageFile34.png>)

![image 35](<2016-warnke-missing-log-upper-tail_images/imageFile35.png>)

![image 36](<2016-warnke-missing-log-upper-tail_images/imageFile36.png>)

![image 37](<2016-warnke-missing-log-upper-tail_images/imageFile37.png>)

- 3.5 Extension: uniform random induced subhypergraph Hm


The proofs in Sections 3.3–3.4 exploited the independence of Hp = H[Vp(H)] in a limited way. In this section we record that they extend to the uniform model Hm = H[Vm(H)], where the vertex subset Vm(H) ⊆ V (H) of size |Vm(H)| = m is chosen uniformly at random (this is a natural variant of Hp with mild dependencies).

Remark 19. Theorems 15 and 18 carry over to Hm after setting p = m/v(H) in (21). Proof. The proof of Theorem 15 is based on (deterministic) combinatorial arguments, and after replacing Hp with Hm thus carries over word-for-word to Hm.

Turning to Theorem 18, using Remark 9 it is easy to see that the proof of (46) carries over to Hm (with minor notational changes).

For (47) more care is needed. To avoid conditional probabilities and expectations, set Yf = {f\U⊆V

m(H)} for all f ∈ I := ΓU(H). Writing α ∼ β if (α ∩ β) \ U = ∅, note that inequality (50) readily carries over. It is folklore (analogous to, e.g., the proof of Theorem 15 in [18]) that EYf = P(f \ U ⊆ Vm(H)) ≤ p|f|−|f∩U| for p = m/v(H), so that f∈I EYf ≤ f∈ΓU(H) p|f|−|U| ≤ µj by (21). Recalling the deﬁnition of ∼, it is similarly folklore that the random variables Yf = {f\U⊆V

m(H)} satisfy the negative correlation condition of Remark 9. Mimicking the argument leading to (52), using Theorem 7 we obtain P(DU,x,y) ≤ P(ZC ≥ x) ≤ (eµj/x)x/(ky) for Hm, which by a simpler variant of (53) then establishes (47).

As the proof of (47) carries over, for (48) it remains to check that (41) holds for Hm. A close inspection of the proof of Lemma 16 reveals that only the usage of the BK-inequality in (45) needs to be justiﬁed. But, since DU,x,y is an increasing event, this application of (16) is valid by Remark 13, completing the proof.

![image 38](<2016-warnke-missing-log-upper-tail_images/imageFile38.png>)

![image 39](<2016-warnke-missing-log-upper-tail_images/imageFile39.png>)

![image 40](<2016-warnke-missing-log-upper-tail_images/imageFile40.png>)

![image 41](<2016-warnke-missing-log-upper-tail_images/imageFile41.png>)

# 4 More general setup

In this section we introduce our general Kim–Vu/Janson–Ruci´nski type setup, and show that the combinatorial and probabilistic arguments of Section 3 carry over with somewhat minor changes. Readers only interested in random induced subhypergraphs Hp may wish to skip to Section 5 (see Remark 29).

- 4.1 Setup


Our general setup is based on certain independence assumptions, i.e., we do not restrict ourselves to polynomials of independent random variables (and we also do not make any monotonicity assumptions). Given a hypergraph H and non-negative random variables (Yf)f∈H, for every G ⊆ H we set

X(G) =

Yf, (54)

f∈G

where our main focus5 is on the sum X(H) of all the variables Yf (sometimes H is also called the ‘supporting’ or ‘underlying’ hypergraph, see [20, 33]). Loosely speaking, the plan is to adapt the combinatorial arguments of Sections 3.3–3.4 to the associated random subhypergraph

Hp = {f ∈ H : Yf > 0}, (55)

which due to X(H) = X(Hp) loosely encodes all ‘relevant’ variables (recall that Yf ≥ 0). Similar to [15], we shall use the following independence assumption (Hℓ), where ℓ ∈ N is a parameter:

(Hℓ) Let (ξσ)σ∈A be a family of independent ﬁnite random variables. Suppose that there are families of subsets AU ⊆ A such that (i) each non-negative random variable Yf with f ∈ H is a function of the variables (ξσ)σ∈A

, (ii) we have Ae ∩ Af ⊆ Ae∩f for all e,f ∈ H, and (iii) we have Ae ∩ Af = ∅ for all e,f ∈ H with |e ∩ f| < ℓ.

f

p(H)}, Af = f and Yf = wf σ∈A

The setup of Section 3.1.1 corresponds to the special case ξσ = {σ∈V

ξσ. A key consequence of (Hℓ) is that Ye and Yf are independent whenever |e ∩ f| < ℓ, since by (i) and (iii) then both depend on disjoint sets of variables ξσ. The ‘structural’ assumption (i) that each Yf depends only on the variables ξσ with σ ∈ Af is very common in applications; often AU = U suﬃces. The ‘consistency’ assumption (ii) and ‘independence’ assumption (iii) of the index sets AU are also very natural. For example, in the frequent case AU = U we have Ae ∩ Af = Ae∩f, so Ae ∩ Af = ∅ if |e ∩ f| < 1. Example 22 in

f

- Section 4.1.1 illustrates the case ℓ = 1 with AU = {f ∈ E(Kn) : f ⊆ U}. We now introduce the modiﬁed key parameters µj, which intuitively quantify the ‘dependencies’ among


the variables Yf (in the spirit of [15, 20, 31, 33]). Recalling ΓU(H) = {f ∈ H : U ⊆ f}, with Section 3.1.1 in mind we now deﬁne the following two crucial assumptions (P) and (Pq), where q ∈ N is a parameter:

(P) Assume that maxf∈H |f| ≤ k, maxf∈H supYf ≤ L and v(H) ≤ N. Deﬁne µ = EX(H) and µj = max

supE |ΓU(Hp)| (ξσ)σ∈A

, (56)

U

U⊆V (H):|U|=j

where the supremum is over all values of the variables ξσ with σ ∈ AU. (Pq) Assume that ∆q(H) ≤ D.

In view of (22), property (P) is a natural extension of (P’) from the basic setup of Section 3.1.1. Our general setup lacks monotonicity, and so the conditioning in (56) is with respect to all possible values of the ξσ.

For the interested reader, we now brieﬂy discuss how our setup and assumptions diﬀer in some (usually irrelevant) minor details from the literature [15, 20, 31, 33]. Firstly, the ‘normal’ assumption of Vu implies maxf∈H supYf ≤ 1 in (P) above (see, e.g., Theorem 1.2 in [31] and Theorem 4.2 in [33]). Secondly, classical variants of the ‘maximum average eﬀect’ parameter µj (see, e.g., Sections 3 in [15] and Section 4 in [33]) are roughly deﬁned as the maximum over all supE( f∈Γ

) with |U| = j, but in most applications f∈Γ

U(Hp) Yf | (ξσ)σ∈A

U

U(Hp) Yf = Θ(|ΓU(Hp)|) holds, so the diﬀerence is usually immaterial. Thirdly, in (Hℓ) our assumptions for the index sets AU are slightly simpler than in Section 3 of [15]. Finally, in contrast to [15], we assume that the (ξσ)σ∈A are ﬁnite random variables, which is very natural in combinatorial applications (this technicality can presumably be removed by approximation arguments, but we have not pursued this).

![image 42](<2016-warnke-missing-log-upper-tail_images/imageFile42.png>)

5Usually we have X = f∈H wfIf in mind, for random variables If ∈ {0, 1} and constants wf ∈ (0, ∞). All examples and applications in [20, 31, 33, 15, 14, 16] are of this form, with wf = 1 (possibly after rescaling X by a constant factor).

- 4.1.1 Examples


The above assumptions (Hℓ) and (P) might seem a bit technical at ﬁrst sight, and for this reason we shall below spell out three pivotal examples (see Section 3 of [15] for more examples).

- Example 20 (Random induced subhypergaphs). For a given k-uniform hypergraph H, analogous to Sec-

tion 3.1.1 we consider X = e(Hp) = f∈H {f∈H

p}. Note that A = H, ξσ = {σ∈V

p(H)}, Af = f and Yf = σ∈A

f

ξσ ∈ {0,1} satisfy properties (H1) and (Pk). In fact, for (P) we can simplify the deﬁnition of µj. Namely, since U  ⊆ Vp(H) implies f  ∈ Hp = H[Vp(H)] for all f ∈ ΓU(H), we have

supE |ΓU(Hp)| (ξσ)σ∈A

U

= E |ΓU(Hp)| U ⊆ Vp(H) =

f∈ΓU(H)

P f ∈ Hp U ⊆ Vp(H) .

As H is k-uniform, for any f ∈ ΓU(H) it is easy to see that P f ∈ Hp U ⊆ Vp(H) = P f \ U ⊆ Vp(H) = pk−|U|. Combining these observations, it follows that (56) simpliﬁes for 1 ≤ j ≤ k to

µj = max

U⊆V (H):|U|=j

|ΓU(H)| · pk−j. (57)

- Example 21 (Subgraph counts in Gn,p: induced subhypergaphs approach). Subgraph counts in Gn,p can be viewed as a special case of Example 20, i.e., random induced subhypergaphs. Given a ﬁxed subgraph H with e = eH edges, v = vH vertices and minimum degree δ = δH ≥ 1, we consider the e-uniform hypergraph H with vertex set V (H) = E(Kn), where edges correspond to copies of H. Clearly, k = e and N = n2 suﬃce. Note that for the copy of H counted by Yf, any subset of the edges U ⊆ f ∩ E(Kn) ⊆ V (H) is isomorphic to some subgraph J ⊆ H. So, taking all subgraphs of H with exactly |U| = j edges into account, using (57) with k = e and V (H) = E(Kn) there is universal constant B = B(H) > 0 such that for 1 ≤ j ≤ e we have

µj ≤

J⊆H:eJ=j

max

U⊆E(Kn): U∼=J

|ΓU(H)| · pe−j ≤ B

J⊆H:eJ=j

nv−v

J

pe−j. (58)

Note that any q = e − δ + 1 ≤ e edges already determine the vertex set, so (Pq) holds with D = O(1). Finally, a minor variant of the described approach also applies to induced subgraph counts (with k = v

H

2 , by letting E(H) correspond to copies of the complete graph Kv

H

, and deﬁning Yf as the indicator for the event that the subgraph of Gn,p deﬁned by the edges in f is isomorphic to H).

- Example 22 (Subgraph counts in Gn,p: vertex exposure approach). Subgraph counts in Gn,p can also be treated via a ‘vertex exposure’ based approach. Given a ﬁxed subgraph H with e = eH edges and v = vH edges, we consider the complete v-uniform hypergraph H with vertex set V (H) = [n], so N = n and k = v. For I ⊆ V (H) with |I| = v the random variable YI counts the number of copies of H in Gn,p that have


vertex set I. Note that 0 ≤ YI ≤ L = O(1). Since X = I∈H YI, we take A = E(Kn), ξσ = {σ∈V

p(H)}, and AI = {f ∈ E(Kn) : f ⊆ I}. As AI ∩ AJ = AI∩J is empty whenever |I ∩ J| < 2, for ℓ = 2 properties (Hℓ) and (Pk) are satisﬁed. Conditioning on (ξσ)σ∈A

corresponds to conditioning on Gn,p[U], so bounding µj is conceptually analogous (58). Indeed, by similar reasoning as in Example 21, we arrive for 1 ≤ j ≤ v at

U

nv−jpe−e

µj ≤ B

, (59)

J

induced J⊆H:vJ=j

where B = B(H) > 0. Finally, induced subgraph counts can clearly be treated analogously.

- 4.2 Adapting the arguments of Sections 3.3–3.4


In this section we adapt the key results Theorem 15 and 18 from Sections 3.3–3.4 to our more general setup. The crux is that the random variables (Yf)f∈H satisfy Yf = Yf(ξσ : σ ∈ Af) by the independence assumption (Hℓ), so that the intersection properties of the index sets Af give us a handle on the dependencies. This allows us to adapt our combinatorial arguments to the auxiliary subhypergraph Hp = {f ∈ H : Yf > 0}.

We start with a natural analogue of Theorem 15, which is at the heart of our arguments.

Theorem 23 (Combinatorial decomposition of the upper tail: general setup). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ) and (P) hold. Suppose that t > 0. Given positive (Rj)ℓ≤j<q and (Dj)ℓ≤j≤q, deﬁne Rq = Qq = Dq and Qj = max{Sj,Dj} for ℓ ≤ j < q. Then we have

P X(G) ≥ µ + t and ∆q(G) ≤ Dq for some G ⊆ Hp ≤ P X(G) ≥ µ + t/2 and ∆ℓ(G) ≤ min{Qℓ,Rℓ} for some G ⊆ Hp

(60)

+

Pj,1 + Pj,2 + Pj,3,ℓ ,

ℓ≤j<q

where Pj,1, Pj,2 and Pj,3,ℓ are deﬁned as in (34)–(36).

Recalling X(G) = f∈G Yf and Hp = {f ∈ H : Yf > 0}, the deterministic proof of Theorem 15 carries over to Theorem 23 with minor obvious changes (inequality (60) is trivial if q = ℓ; for q > ℓ it suﬃces to construct

G = Jq ⊇ ··· ⊇ Jℓ, with indices of form ℓ ≤ i,j ≤ q in (37)); we omit the routine details. Next we state an analogue of Lemma 16 for the ‘sparsiﬁcation’ event Ej,ℓ(x,r,y,z) from Section 3.3.

Lemma 24 (Auxiliary result for the sparsiﬁcation event: general setup). Given H with 1 ≤ ℓ ≤ k, assume that (Hℓ) and maxf∈H |f| ≤ k hold. Then for all x,r,y,z > 0 and ℓ ≤ j < k we have

P ¬Ej,ℓ(x,r,y,z) ≤

P(DU,x,y)

U⊆V (H):|U|=j

r/ (k

)⌈x⌉z

ℓ

. (61)

Remark 25. Inequality (61) remains valid after dividing the right hand side by ⌈r/( kℓ ⌈x⌉z)⌉!.

For the proof of Lemma 24 we adapt the deﬁnition of Mj,x,y(G) used for Lemma 16. Intuitively, the idea is to replace ‘vertex disjoint’ by ‘depending on disjoint sets of variables’. Namely, here we deﬁne Mj,x,y(G) as the size of the largest collection M ⊆ Sj,x,y(G) of (j,x,y)-stars in G satisfying the following property for all distinct (U,KU),(W,KW) ∈ M: we have |e ∩ f| < ℓ for all e ∈ KU and f ∈ KW. The point will be (i) that each Yf is a function of the variables (ξσ)σ∈A

, and (ii) that |e ∩ f| < ℓ implies Ae ∩ Af = ∅ by (Hℓ).

f

Proof of Lemma 24. Using the above deﬁnition of Mj,x,y(G), we shall adapt the proof of Lemma 16. Let r˜ = r/ kℓ ⌈x⌉z and R = ⌈r˜⌉. We ﬁrst assume that Mj,x,y(Hp) ≤ r˜ holds, and claim that this implies the occurrence of Ej,ℓ(x,r,y,z). Fix G ⊆ Hp with ∆j+1(G) ≤ y and ∆ℓ(G) ≤ z, and let M ⊆ Sj,x,y(G) attain the maximum in the deﬁnition of Mj,x,y(G). We remove all edges f ∈ G which ‘overlap’ some star (U,KU) ∈ M, where overlap means that |f∩g| ≥ ℓ for some edge g ∈ KU. We denote the resulting subhypergraph by J ⊆ G. Recalling ∆j+1(J ) ≤ ∆j+1(G) ≤ y, by maximality of M we infer ∆j(J ) ≤ ⌈x⌉ − 1 < x. Similar to (42), using |M| = Mj,x,y(G) ≤ Mj,x,y(Hp) ≤ r˜ and ∆ℓ(G) ≤ z it is easy to see that we removed at most

|f| ℓ · ∆ℓ(G) ≤ r˜· ⌈x⌉

k ℓ

e(G \ J ) ≤ |M| · ⌈x⌉ · max

z = r (62)

f∈G

edges. It follows that Mj,x,y(Hp) ≤ r˜ implies Ej,ℓ(x,r,y,z), as claimed.

For (61) it remains to estimate P(Mj,x,y(Hp) > r˜). Suppose that Mj,x,y(Hp) > r˜ occurs. If M ⊆ Sj,x,y(Hp) attains the maximum in the deﬁnition of Mj,x,y(Hp), then we know (i) that |M| ≥ ⌈r˜⌉ = R holds, and (ii) that (U,K

U)∈M DU,x,y occurs. In the following we argue that these events DU,x,y ‘occur disjointly’ in the sense of Section 2.2. For each (U,KU) ∈ M, note that the variables indexed by

Af

V (KU) =

f∈KU

guarantee the occurrence of DU,x,y. The crux is now that for all distinct (U,KU),(W,KW) ∈ M, by (iii) of (Hℓ) we have Ae ∩ Af = ∅ for all e ∈ Ku and f ∈ KW (since |e ∩ f| < ℓ), so

V (KU) ∩ V (KW) =

(Ae ∩ Af) = ∅. (63)

e∈KU f∈KW

U)∈MDU,x,y occurs (since the disjoint sets of variables indexed by V (KU) guarantee the occurrence of each DU,x,y). Next we claim that all the corresponding sets U are distinct. To see this, note that for distinct (U,KU),(W,KW) ∈ M we have ℓ > |e ∩ f| ≥ |U ∩ W| by deﬁnition of M, which due to |U| = |W| = j ≥ ℓ implies U = W. To sum up, Mj,x,y(Hp) > r˜ implies ZR ≥ R!, where ZR is deﬁned as in (43). The arguments of (44) and (45) now carry over unchanged, completing the proof of (61).

It follows that ⊡(U,K

![image 43](<2016-warnke-missing-log-upper-tail_images/imageFile43.png>)

![image 44](<2016-warnke-missing-log-upper-tail_images/imageFile44.png>)

![image 45](<2016-warnke-missing-log-upper-tail_images/imageFile45.png>)

![image 46](<2016-warnke-missing-log-upper-tail_images/imageFile46.png>)

Finally, we state a natural analogue of Theorem 18, which contains our core probabilistic estimates (inequalities (64)–(66) allow us to bound the right hand side of (60) from Theorem 23). Theorem 26 (Probabilistic upper tail estimates: general setup). Given H with 1 ≤ ℓ ≤ k, assume that (Hℓ) and (P) hold. Set ϕ(x) = (1 + x)log(1 + x) − x. Then for all x,r,y,z,t > 0 and ℓ ≤ j < k we have

P X(G) ≥ µ + t/2 and ∆ℓ(G) ≤ y for some G ⊆ Hp ≤ exp −

P ∆j(G) ≥ x and ∆j+1(G) ≤ y for some G ⊆ Hp ≤ Nj

eµj x

![image 47](<2016-warnke-missing-log-upper-tail_images/imageFile47.png>)

P ¬Ej,ℓ(x,r,y,z) ≤ Nj

eµj ⌈x⌉

![image 48](<2016-warnke-missing-log-upper-tail_images/imageFile48.png>)

ϕ(t/µ)µ 4L kℓ y

, (64)

![image 49](<2016-warnke-missing-log-upper-tail_images/imageFile49.png>)

x/(ky)

, (65)

k ℓ

)⌈x⌉z

⌈x⌉/(4ky) r/ (

. (66)

The proof is based on a minor modiﬁcation of the proof of Theorem 18. As we shall see, our main task is to adapt the deﬁnitions of the dependency relations ∼. To this end recall (i) that each Yf is a function of the independent variables (ξσ)σ∈A

, and (ii) that (Hℓ) implies Ae ∩ Af = ∅ whenever |e ∩ f| < ℓ.

f

Proof of Theorem 26. For (64), note that f∈H EYf = EX(H) = µ. We deﬁne α ∼ β if |α ∩ β| ≥ ℓ. In view of properties (i) and (ii) discussed above, the independence assumption of Theorem 7 holds by analogous

reasoning as in Remark 8. Furthermore, for any f ∈ G ⊆ H with ∆ℓ(G) ≤ y we have

|f| ℓ · ∆ℓ(G) ≤ L

k ℓ

supYe ·

Ye ≤ max

|ΓU(G)| ≤ L ·

{f∈G} ≤ L ·

y.

e∈G

e∈G:e∼f

e∈G:|e∩f|≥ℓ

U⊆f:|U|=ℓ

Setting C = L kℓ y, the remaining proof of (46) readily carries over to (64) with obvious notational changes.

Next we turn to (65), which is again based on (40). As before, we may assume that x > eµj and N ≥ 1 (otherwise the claim is trivial). Furthermore, given U ⊆ V (H) with |U| = j, we set I = ΓU(H). With the random variables {Y

f>0} f∈I in mind, deﬁne α ∼ β if (α ∩ β) \ U = ∅. Note that, for any f ∈ K ⊆ I with ∆|U|+1(K) ≤ y, analogous to (50) we have e∈K:e∼f {Y

f>0} ≤ |f \ U| · ∆|U|+1(K) ≤ ky. Furthermore, by deﬁnition of I = ΓU(H), Hp = {f ∈ H : Yf > 0} and µj (see (56)) we obtain

f>0} | (ξσ)σ∈A

E {Y

U

f∈I

= E |ΓU(Hp)| (ξσ)σ∈A

U ≤ µ|U| = µj.

f>0} is now a function of the independent random variables (ξσ)σ∈A

, each {Y

Note that, conditional on (ξσ)σ∈A

U

f\AU. Furthermore, for all e,f ∈ I = {g ∈ H : U ⊆ g} we see that (e ∩ f) \ U = ∅ implies e ∩ f = U, so that (ii) of (Hℓ) yields Ae ∩ Af ⊆ Ae∩f = AU. For all e,f ∈ I we thus infer that e  ∼ f implies

(Ae \ AU) ∩ (Af \ AU) = (Ae ∩ Af) \ AU ⊆ AU \ AU = ∅. Conditional on (ξσ)σ∈A

, it follows (by the reasoning of Remark 8) that the independence assumption of Theorem 7 holds for the variables {Y

U

f>0} f∈I. The remaining proof of (47) readily carries over to (65).

Finally, for (66) we recall that (48) is based on Lemma 16 and the argument leading to (47). In view of Lemma 24 and the above proof of (65), the same line of reasoning carries over, establishing (66).

![image 50](<2016-warnke-missing-log-upper-tail_images/imageFile50.png>)

![image 51](<2016-warnke-missing-log-upper-tail_images/imageFile51.png>)

![image 52](<2016-warnke-missing-log-upper-tail_images/imageFile52.png>)

![image 53](<2016-warnke-missing-log-upper-tail_images/imageFile53.png>)

- 4.3 Adapting Section 3.5: vertex exposure approach for Hm


In this section we partially adapt our arguments to the uniform random induced subhypergraph Fm = F[Vm(F)]. Generalizing the ‘vertex exposure’ approach of Example 22, we rely on the following assumption.

(HℓP) Suppose that H, E and F are hypergraphs with V (H) = V (E), V (F) = {h ∈ E} and minh∈E |h| ≥ ℓ. Deﬁning AU = {h ∈ E : h ⊆ U} for all U ⊆ V (E), assume that F = f∈H F[Af] is a disjoint union of induced subhypergraphs. Suppose that (wg)g∈F are non-negative weights. For all f ∈ H, let

wg {g∈F

Yf =

m}. (67)

g∈F[Af]

Assume that maxf∈H |f| ≤ k, maxf∈H Yf ≤ L and v(H) ≤ N. Deﬁne µ = EX(H), p = m/v(F), and µj = max

p|g|−|g∩A

U|. (68)

U⊆V (E):|U|=j

f∈ΓU(H) g∈F[Af]

Example 27. Using the ‘vertex exposure’ setup discussed in Example 22, subgraph counts in Gn,m satisfy (HℓP) with ℓ = 2 and k = vH (by setting E = Kn, and deﬁning F as the hypergraph H of Example 21). In (68) the modiﬁed parameter µj is again bounded from above by the right hand side of (59).

- Remark 28. Theorems 23 and 26 remain valid after replacing the assumptions (Hℓ),(P) with (HℓP).

Proof. With the ideas of Remark 19 in mind, we only sketch the key modiﬁcations for (64)–(65) of Theorem 26.

For (64) it suﬃces to verify the negative correlation condition of Remark 9, writing α ∼ β if |α ∩ β| ≥ ℓ. Using (67) and the negative correlation properties of Fm (see Remark 9), it is not hard to check that

E

i∈[s]

Yα

i

=

g1∈F[Aα1]

···

gs∈F[Aαs]

E

i∈[s]

wg

i {gi∈Fm} ≤

i∈[s]

EYα

i

, (69)

and so the proof of (64) carries over (above we used that αi  ∼ αj implies F[Aαi

] ∩ F[Aαj

] = ∅). For (65) we deﬁne α ∼ β if (α ∩ β) \ U = ∅, and replace {Y

f>0} f∈I by {Y

f} f∈I, where Yf denotes the event that g\AU ⊆ Vm(F) for some g ∈ F[Af]. Let λf = g∈F[A

f] P(g\AU ⊆ Vm(F)). It is folklore that P(g\AU ⊆ Vm(F)) ≤ p|g|−|g∩A

U| (see Remark 19), so I = ΓU(H) and (68) yield f∈I λf ≤ µ|U| = µj. Since {Yf} ≤ g∈F[Af] {g\AU⊆Vm(F)}, analogous to (69) we infer E( i∈[s] {Y

αi}) ≤ i∈[s] λα

i

, establishing the correlation condition of Remark 10. Mimicking Remark 19, the proof of (47) then carries over to (65).

![image 54](<2016-warnke-missing-log-upper-tail_images/imageFile54.png>)

![image 55](<2016-warnke-missing-log-upper-tail_images/imageFile55.png>)

![image 56](<2016-warnke-missing-log-upper-tail_images/imageFile56.png>)

![image 57](<2016-warnke-missing-log-upper-tail_images/imageFile57.png>)

5 Corollaries: upper tail inequalities

The main results of Sections 3–4 are Theorems 15,23 of form P(X ≥ (1 + ε)EX) ≤ i P(¬Ei) and Theorems 18,26 of form P(¬Ei) ≤ exp(−Ψi). In this section we derive upper tail inequalities that are convenient for the applications of Section 6, and brieﬂy compare some of our more general estimates with the literature.

- Remark 29 (Random induced subhypergraph setup). The results in Sections 5.1–5.2 are stated for the general setup of Section 4.1. But, with minor changes, they remain valid in the simpler random induced subhypergraph setup of Section 3.1.1. Indeed, setting ℓ = 1 and replacing the assumptions (Hℓ),(P) with (P’), all results carry over to Hp by deﬁning X(J ) := w(J ). After setting p = m/v(H) in (21), these results for Hp then also carry over to the uniform variant Hm deﬁned in Section 3.5. Finally, after replacing the assumptions (Hℓ),(P) with (HℓP), all results in Sections 5.1–5.2 also remain valid in the setup of Section 4.3. Henceforth, we tacitly set ϕ(x) = (1 + x)log(1 + x) − x for brevity (as in Theorems 7, 18 and 26).


- 5.1 Easy-to-apply tail inequalities


In this section we state some simpliﬁed upper tail inequalities that suﬃce for all the applications in Section 6 (we have not optimized the usually irrelevant constants); the proofs are deferred to Section 5.3.

On ﬁrst reading of the following upper tail inequality for X(H) = f∈H Yf, the reader may wish to set ℓ = 1 and q = k, so that (72) is of form P(X(H) ≥ 2µ) ≤ exp(−dmin{µ,µ1/k log(e/π)}). Here our main novelty is the log(e/π) term: it allows us to gain an extra logarithmic factor if π ∈ {N−1,p}, which yields best possible tail estimates in the applications of Section 6.1. We think of (70) as a ‘balancedness’ condition, and mainly have parameters of form π ∈ {1,N−1,p} in mind. In fact, for π ∈ {N−1,p} the technical assumption (71) usually holds automatically for small τ (see Remark 31 and the proof of Theorem 36).

Theorem 30 (Easy-to-apply upper tail inequality). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ), (P) and (Pq) hold. If there are constants A,α,τ > 0 and a parameter π ∈ (0,1] such that

µj max{µ(q−j)/(q−ℓ+1),1}

≤ Aπα, (70)

max

![image 58](<2016-warnke-missing-log-upper-tail_images/imageFile58.png>)

ℓ≤j<q

Aµ1/(q−ℓ+1) ≥ {π>N−τ} log N, (71) then for ε > 0 we have

P(X(H) ≥ (1 + ε)µ) ≤ (1 + bN−ℓ)exp −c min ϕ(ε)µ, min ε2,1 µ1/(q−ℓ+1) log(e/π) ≤ (1 + bN−ℓ)exp −dmin ε2,1 min µ, µ1/(q−ℓ+1) log(e/π) ,

(72)

where b = 3q, c = c(ℓ,q,k,L,D,A,α,τ) > 0 and d = c/3. Remark 31. If π = N−1, then (71) is trivially satisﬁed for τ = 1/2, and log(e/π) ≥ log N holds in (72).

Simple applications of the inductive approaches [20, 15, 33] often implicitly assume (70) with π = 1, and replace (71) by the stronger assumption min{ε2,1}µ1/(q−ℓ+1) = ω(log N), say (see, e.g., the proof of Corollary 6.3 in [33] or Theorem 2.1 in [32]). Their conclusion is then of the form P(X(H) ≥ (1 + ε)µ) ≤ exp(−a min{ε2,1}µ1/(q−ℓ+1)), where µ1/(q−ℓ+1) = min µ,µ1/(q−ℓ+1) log(e/π) holds by assumption. In other words, our inequality (72) yields an extra logarithmic factor when π ∈ {N−1,p} in (70). To illustrate this, for subgraph counts in Gn,p the setup of Example 21 (with ℓ = 1, q = k = e and N = n2) naturally yields

µj µ(q−j)/(q−ℓ+1) ≤ max

max

![image 59](<2016-warnke-missing-log-upper-tail_images/imageFile59.png>)

1≤j<e

ℓ≤j<q

pe−j) Θ((nvpe)(e−j)/e) ≤ O(

J=j nv−v

O( J⊆H:e

J

![image 60](<2016-warnke-missing-log-upper-tail_images/imageFile60.png>)

J⊆H:1≤eJ <e

Jv/e−vJ),

ne

which is well-known to be O(n−β) for so-called ‘strictly balanced’ graphs and O(1) for ‘balanced’ graphs (the details are deferred to (104) and (115) in Section 6.2; see also Section 6.3 in [33]).

The next upper tail result assumes that all the parameters µj are decaying polynomially in N, which typically requires that µ = EX(H) is small (as v(H) ≤ N). On ﬁrst reading of Theorem 32 the reader may wish to set ℓ = 1, q = k and K = 1, so that (74) is of form P(X(H) ≥ µ+t) ≤ exp(−a min{t2/µ,t1/k log N}) when t ∈ [1,µ]. Here our main novelty is the t1/k log N term, which is key for the applications in Section 6.2.1.

Theorem 32 (Easy-to-apply upper tail inequality: the small expectations case). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ), (P) and (Pq) hold. If there are constants A,α > 0 such that

µj ≤ AN−α, (73)

max

ℓ≤j<q

then for t,K > 0 we have P(X(H) ≥ µ + t) ≤ (1 + bN−q)exp − min cϕ(t/µ)µ, max ct1/(q−ℓ+1),K log N ≤ (1 + bN−q)exp − min dt2/µ, dt, max ct1/(q−ℓ+1),K log N ,

where b = 2q, c = c(ℓ,q,k,L,D,A,α,K) > 0 and d = c/3.

(74)

The inductive approaches [31, 15] yield variants of (74) where max ct1/(q−ℓ+1),K is qualitatively replaced by K (see, e.g., Corollary 4.10 in [15]). For K large enough this gives bounds of the form P(X(H) ≥

(1 + ε)µ) ≤ N−β for µ ≥ C(ε,d,β)log n, and P(X(H) ≥ (1 + ε)µ) ≤ exp(−dε2µ) for µ ≤ log n and ε ≤ 1, say (see, e.g., Corollaries 4.11–4.12 in [15]). To illustrate assumption (73), for subgraph counts in Gn,p with p = O(n−v/e+σ), the setup of Example 21 (with ℓ = 1, q = k = e and N = n2) yields µ = O(neσ) and

nv−v

µj ≤ O(

max

J

ℓ≤j<q

J⊆H:1≤eJ <e

pe−e

) ≤ O(

J

J⊆H:1≤eJ <e

Jv/e−vJ+σ(e−eJ)),

ne

which for ‘strictly balanced’ graphs is well-known to be O(n−σ/2) for suﬃciently small σ > 0 (the details are deferred to (104) and (107) in Section 6.2; see also Claim 6.2 in [33]).

- 5.2 More general tail inequalities In this section we state some more general upper tail inequalities which (i) mimic the heuristic discussion of


- Section 3.1.2, and (ii) are easier to compare with the work of Kim–Vu/Janson–Ruci´nski [20, 31, 33, 15]; the proofs are deferred to Section 5.3. Readers primarily interested in applications may proceed to Section 6.


We start with a rigorous analogue of the basic upper tail inequality (23) from Section 3.1.2, which is inspired by very similar classical results for the special case G = Hp with ∆q(H) ≤ D (see, e.g., Theorem 3.10 in [15] and Theorem 4.2 in [33]). In applications convenient choices of the parameters (Rj)ℓ≤j<q and D are often of form D = Θ(1), Rj = λq−jD and λ = B max{µ1/(q−ℓ+1),1}, so that in (76) we have min{µ/Rℓ = Θ(λ) and Rj/Rj+1 = λ when µ ≥ 1 (see, e.g., the proof of Corollary 6.3 in [33] or Theorem 2.1 in [32]).

Claim 33 (Basic upper tail inequality). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ) and (P) hold. Suppose that t > 0. Given positive (Rj)ℓ≤j<q and D, let Rq = D. If inequality

eµj Rj

![image 61](<2016-warnke-missing-log-upper-tail_images/imageFile61.png>)

Rj/Rj+1

≤ N−4kj (75)

holds for all ℓ ≤ j < q, then there are a,b > 0 (depending only on ℓ,k,L) such that P(X(G) ≥ µ + t and ∆q(G) ≤ D for some G ⊆ Hp) ≤ exp −

bRj/Rj+1

eµj Rj

aϕ(t/µ)µ Rℓ

N−j

.

+

![image 62](<2016-warnke-missing-log-upper-tail_images/imageFile62.png>)

![image 63](<2016-warnke-missing-log-upper-tail_images/imageFile63.png>)

ℓ≤j<q

(76)

To familiarize the reader with the form of assumption (75) and inequality (76), it is instructive to brieﬂy relate them to work of Kim and Vu [20, 32, 33]. Theorem 4.2 in [33] qualitatively sets t = √λµRℓ, and (in our notation) its parametrization assumes roughly ∆q(H) ≤ D = Rq, µ/Rℓ ≥ λ = ω(log N), as well as Rj ≥ 2eµj and Rj/Rj+1 ≥ λ for all ℓ ≤ j < q, say. In this case (eµj/Rj)R

![image 64](<2016-warnke-missing-log-upper-tail_images/imageFile64.png>)

j/Rj+1 ≤ 2−λ = N−ω(1) follows, so assumption (75) holds. We also have t = µ λRℓ/µ ≤ µ, so that Remark 11 yields ϕ(t/µ)µ/Rℓ ≥ t2/(3µRℓ) = λ/3, say. Recalling ∆q(H) ≤ D, for suitable C = C(q) and c = c(a,b) it follows that (76) yields

![image 65](<2016-warnke-missing-log-upper-tail_images/imageFile65.png>)

P(X(Hp) ≥ µ + t) ≤ exp −aλ/3 + {q>ℓ}qN−ℓ2−bλ ≤ C exp −cλ , (77) which is of similar form as (24) or Theorem 4.2 [33].

We now state our improved variant6 of Claim 33, which corresponds to a rigorous analogue of the upper tail inequality (26) from Section 3.1.2. Convenient choices of the parameters (Rj)ℓ≤j<q and (Dj)ℓ≤j≤q are often of form Dj = Bq−jDq = Θ(1), Rj = λq−jDq and λ = B max{µ1/(q−ℓ+1),1}, so that in (80) we have Rj/Rj+1 = λ and t/Rℓ = Θ(λ) when t = Θ(µ) and µ ≥ 1. One key novelty of (80) is the µ/Qℓ = min{µs/Rℓ,µ/Dℓ} term, which intuitively allows us to sharpen inequality (76) whenever Rj = ω(µj) holds (by using s = ω(1) in (78), so that usually µ/Qℓ = ω(µ/Rℓ) in (80), say).

- Theorem 34 (Extended upper tail inequality). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ) and (P) hold. Suppose that s ≥ 1 and t > 0. Given positive (Rj)ℓ≤j<q and (Dj)ℓ≤j≤q with Rj ≥ Dj, deﬁne


Qj = max{Rj/s,Dj} (78)

![image 66](<2016-warnke-missing-log-upper-tail_images/imageFile66.png>)

6Note that by setting s = 1 and Dj = Rj we have Qj = Rj in (78), so the indicators in (79)–(80) are zero and Theorem 34 recovers Claim 33 up to irrelevant constant factors.

for ℓ ≤ j < q, and Rq = Qq = Dq. If inequality

Rj/Rj+1

eµj Qj

max

, {Q

j<Rj and Qj+1=Dj+1}

![image 67](<2016-warnke-missing-log-upper-tail_images/imageFile67.png>)

eµj Qj

![image 68](<2016-warnke-missing-log-upper-tail_images/imageFile68.png>)

Qj/Dj+1

≤ N−4kj (79)

holds for all ℓ ≤ j < q, then for a = 1/ 4L kℓ , b = 1/(2k) and d = 1/ 4Lqk kℓ we have P(X(G) ≥ µ + t and ∆q(G) ≤ Dq for some G ⊆ Hp) ≤ exp −

bRj/Rj+1

eµj Qj

aϕ(t/µ)µ Qℓ

N−j

+ 2

![image 69](<2016-warnke-missing-log-upper-tail_images/imageFile69.png>)

![image 70](<2016-warnke-missing-log-upper-tail_images/imageFile70.png>)

ℓ≤j<q

+

ℓ≤j<q

{Qj<Rj and Qj+1=Dj+1}N−j

eµj Qj

![image 71](<2016-warnke-missing-log-upper-tail_images/imageFile71.png>)

max dt/(RℓDj+1), bQj/Dj+1

.

(80)

To illustrate Theorem 34, in the applications of Sections 5.3.2 and 6.1 we have eµj/Rj ≤ pα/e with p ∈ (0,1], in which case s = log(e/pα/2) is a convenient choice. Indeed, xlog(e/x) ≤ 1 then implies eµj/Qj ≤ eµjs/Rj ≤ pα/2/e = e−s. We thus think of the (79) as a minor variant of the assumption (75) from Claim 33 (note that eµj/Rj ≤ e−s holds, and that Qj < Rj implies Qj = Rj/s). Using Dj = Θ(1) and the additional Kim–Vu type assumptions discussed below Claim 33, we now review inequality (80) of Theorem 34. Since 1/Qℓ = min{s/Rℓ,1/Dℓ}, using t/Rℓ = λµ/Rℓ ≥ λ we obtain analogous to (77) an estimate of the form

![image 72](<2016-warnke-missing-log-upper-tail_images/imageFile72.png>)

P(X(Hp) ≥ µ + t) ≤ exp −a˜ min{t2/µ,λs} + {q>ℓ}3qN−ℓe−dλs˜ ≤ C exp −c min{t2/µ,λlog(e/p)} .

(81)

If q > ℓ then t2/µ = λRℓ ≥ λq−ℓ+1Rq = ω(λlog N), so (81) usually decays like C exp(−cλlog(e/p)). When λ ≈ µ1/(q−ℓ+1) or t = εµ we similarly see that (81) decays like C exp(−c min{µ,λlog(e/p)}). In all these cases we thus improve the exponential decay of the classical bound (77) by an extra logarithmic factor.

The following upper tail inequality for polynomially small µj is a minor extension of Theorem 32. Note that (82) decays exponentially in min{t2/µ,t1/(q−ℓ+1) log N} for 1 ≤ t ≤ O(µ), which seems quite informative when µ = Θ(VarX(H)) holds (i.e., in the Poisson range).

- Theorem 35 (Upper tail inequality: the small expectations case). Given H with 1 ≤ ℓ ≤ q ≤ k, assume that (Hℓ) and (P) hold. If there are A,α > 0 such that inequality (73) holds, then for t,K > 0 we have


P(X(G) ≥ µ + t and ∆q(G) ≤ D for some G ⊆ Hp) ≤ exp −aϕ(t/µ)µ + {q>ℓ}2qN−q exp − max{bt1/(q−ℓ+1), K} logN ,

where a,b > 0 depend only on ℓ,q,k,L,D,A,α,K.

(82)

- 5.3 Proofs


- 5.3.1 Proofs of Claim 33 and Theorems 34–35 Combining Theorem 15 and 18, by setting Sj = Rj/s the proof of Theorem 34 is straightforward.


- Proof of Theorem 34. We ﬁrst consider the special case q = ℓ. Since Rq = Dq, using s ≥ 1 we thus infer max{Rℓ/s,Dℓ} = Dℓ = Rℓ. Hence (64) of Theorem 26 readily implies (80).


In the remainder we focus on the more interesting case q > ℓ. Analogous to the proof of Theorem 18, inequality (80) is trivial when N < 1 (the left hand side is zero). So we henceforth may assume N ≥ 1, and using the assumption (79) it follows that Qj ≥ eµj. Let Sj = Rj/s, and recall that Qj = max{Sj,Dj} in Theorem 23. Note that s ≥ 1 and Rj ≥ Dj imply Qj ≤ Rj. In view of (60) and (64) of Theorem 23 and 26, it

remains to estimate Pj,1, Pj,2 and Pj,3,ℓ deﬁned in (34)–(36). Starting with Pj,1 and Pj,2, using (65) together with Rj ≥ Qj, Qj/Sj+1 ≥ Sj/Sj+1 = Rj/Rj+1 and the assumption (79) we infer

Rj/(kRj+1)

Qj/(kSj+1)

eµj Qj

eµj Rj

+ Nj

Pj,1 + Pj,2 ≤ Nj

![image 73](<2016-warnke-missing-log-upper-tail_images/imageFile73.png>)

![image 74](<2016-warnke-missing-log-upper-tail_images/imageFile74.png>)

(83)

Rj/(kRj+1)

Rj/(2kRj+1)

eµj Qj

eµj Qj

≤ 2N−j

≤ 2Nj

.

![image 75](<2016-warnke-missing-log-upper-tail_images/imageFile75.png>)

![image 76](<2016-warnke-missing-log-upper-tail_images/imageFile76.png>)

Finally, for Pj,3,ℓ of (36) we henceforth tacitly assume Qj < Rj and Qj+1 = Dj+1. With an eye on (66), using Qj ≥ eµj and the assumption (79) we then (with foresight) similarly deduce

⌈Qj⌉/(kDj+1)

⌈Qj⌉/(kDj+1)

⌈Qj⌉/(2kDj+1)

eµj ⌈Qj⌉

eµj Qj

eµj Qj

≤ N−j

Π := Nj

≤ Nj

.

![image 77](<2016-warnke-missing-log-upper-tail_images/imageFile77.png>)

![image 78](<2016-warnke-missing-log-upper-tail_images/imageFile78.png>)

![image 79](<2016-warnke-missing-log-upper-tail_images/imageFile79.png>)

Since ⌈x⌉ ≥ max{x,1}, by applying (66) with (x,r,y,z) = (Qj,t/(2qL),Dj+1,Rℓ) it follows that

max dt/(RℓDj+1), bQj/Dj+1

eµj Qj

Pj,3,ℓ ≤ (Π)⌈t/(2Lq(k

)⌈Qj⌉Rℓ)⌉ ≤ N−j

.

ℓ

![image 80](<2016-warnke-missing-log-upper-tail_images/imageFile80.png>)

Recalling our tacit assumption for Pj,3,ℓ, this completes the proof in view of (60), (64) and (83).

![image 81](<2016-warnke-missing-log-upper-tail_images/imageFile81.png>)

![image 82](<2016-warnke-missing-log-upper-tail_images/imageFile82.png>)

![image 83](<2016-warnke-missing-log-upper-tail_images/imageFile83.png>)

![image 84](<2016-warnke-missing-log-upper-tail_images/imageFile84.png>)

The details of the similar but simpler proof of Claim 33 are omitted (the above proof carries over by setting s = 1 and Dj = Rj, since Qj = max{Rj/s,Dj} = Rj implies Pj,2 = Pj,3,ℓ = 0).

For the proof of Theorem 35 we need to deﬁne the parameters (Rj)ℓ≤j≤q and (Dj)ℓ≤j≤q of Theorem 15 and 18 in a suitable way. Intuitively, we shall set Rj = λq−jD, λ = max{t1/(q−ℓ+1),B} and Dj = Qj = Bq−jD = Θ(1), and the crux is that the assumption (73) eventually yields eµj/x ≤ N−Θ(1) in (65)–(66). We shall also exploit the indicators in Theorem 23 for estimating t/Rℓ in (80), see (86) below.

- Proof of Theorem 35. With foresight, let B = max 4qk/α,2kK/α,Ae/D,1 and λ = max{t1/(q−ℓ+1),B}. Deﬁne Dj = Sj = Bq−jD and Rj = λq−jD for all ℓ ≤ j ≤ q. Note that Qj = max{Sj,Dj} = Dj and min{Qj,Rj} = Dj, so that Pj,2 = 0 in (35). Combining (60) and (64) of Theorem 23 and 26, we obtain


ϕ(t/µ)µ 4L kℓ Dℓ

P(X(G) ≥ µ + t and ∆q(G) ≤ D for some G ⊆ Hp) ≤ exp −

+

Pj,1 + Pj,3,ℓ . (84)

![image 85](<2016-warnke-missing-log-upper-tail_images/imageFile85.png>)

ℓ≤j<q

Tacitly assuming q > ℓ, it remains to estimate Pj,1 and Pj,3,ℓ deﬁned in (34) and (36). Starting with Pj,1, by inserting (73) into (65), using Rj ≥ DB ≥ Ae and Rj/Rj+1 = λ ≥ B ≥ 4qk/α we infer

Rj/(kRj+1)

eµj Rj

≤ Nq µj/A λ/k ≤ Nq−αλ/k ≤ N−q−αλ/(2k). (85)

Pj,1 ≤ Nj

![image 86](<2016-warnke-missing-log-upper-tail_images/imageFile86.png>)

For Pj,3,ℓ, using ⌈Qj⌉ ≥ Ae and Qj/Dj+1 ≥ B ≥ 4qk/α we (with foresight) similarly deduce

⌈Qj⌉/(kDj+1)

eµj ⌈Qj⌉

≤ N−q−α⌈Q

j⌉/(2kDj+1).

Π := Nj

![image 87](<2016-warnke-missing-log-upper-tail_images/imageFile87.png>)

Note that λ = B implies Rj = Dj = Qj. Hence Qj < Rj ensures λ = t1/(q−ℓ+1), so that t/Rℓ = t1/(q−ℓ+1)/D. Recalling ⌈Qj⌉/Dj+1 ≥ B, by applying (66) with (x,r,y,z) = (Qj,t/(2qL),Dj+1,Rℓ) we thus infer

Pj,3,ℓ ≤ {Qj<Rj}(Π)⌈t/(2Lq(k

1/(q−ℓ+1)/Dj+1, αB/(2k) , (86)

)⌈Qj⌉Rℓ)⌉ ≤ N−q−max βt

ℓ

with β = α/(4Lqk kℓ D). With the above estimates (85) and (86) for Pj,1 and Pj,3,ℓ in hand, using B ≥ 2kK/α and Dj+1 ≤ Dℓ it follows by deﬁnition of λ = max{t1/(q−ℓ+1),B} that

Pj,1 + Pj,3,ℓ ≤ {q>ℓ}2qN−q exp − max bt1/(q−ℓ+1), K log N ,

ℓ≤j<q

- with b = min α/(2k),β/Dℓ . Recalling (84), this establishes (82) with a = 1/(4L kℓ Dℓ).


- 5.3.2 Proofs of Theorem 30 and 32


The ‘easy-to-apply’ inequalities from Section 5.1 are convenient corollaries of Theorems 34–35. Indeed, Remark 11 implies ϕ(t/µ)µ ≥ min{t2/µ,t}/3, so Theorem 32 follows readily from Theorem 35. For Theorem 30 the basic strategy is to apply Theorem 34 with s = log(e/πα/2), Rj = λq−jD, λ = B max{µ1/(q−ℓ+1),1} and Dj = Bq−jD = Θ(1). The crux is that the assumption (70) eventually yields eµj/Qj ≤ πα/2/e = e−s in (79)–(80). As before, the indicators in Theorem 34 facilitate estimating t/Rℓ in (80), see (89) below.

Proof of Theorem 30. The proof is naturally divided into four parts: (i) introducing deﬁnitions, (ii) estimating eµj/Qj, (iii) applying inequality (80) of Theorem 34, and (iv) verifying assumption (79).

Analogous to the proof of Theorem 18 and 34, we may henceforth assume N ≥ 1. Furthermore, by increasing A or D if necessary, we may of course assume A,D ≥ 1. With foresight, let β = α/2 and s = log(e/πβ). Set B = max{e2A/D,4k2/(τβ),4k2(4A)q,1} and λ = B max{µ1/(q−ℓ+1),1}. Deﬁne Rj = λq−jD and Dj = Bq−jD, so that Rj ≥ Dj and Rq = Dq = D.

Next we estimate eµj/Qj, where Qj ≥ Rj/s. Using assumption (70) and α = 2β, for ℓ ≤ j < q we have eµj Qj ≤

πβ e

eAπ2β log(e/πβ) DB ≤

eµjs Rj

eµjs DBq−j max{µ(q−j)/(q−ℓ+1),1}

= e−s, (87) where we tacitly used π ∈ (0,1] and xlog(e/x) ≤ 1 for all x ∈ [0,1].

≤

=

![image 92](<2016-warnke-missing-log-upper-tail_images/imageFile92.png>)

![image 93](<2016-warnke-missing-log-upper-tail_images/imageFile93.png>)

![image 94](<2016-warnke-missing-log-upper-tail_images/imageFile94.png>)

![image 95](<2016-warnke-missing-log-upper-tail_images/imageFile95.png>)

![image 96](<2016-warnke-missing-log-upper-tail_images/imageFile96.png>)

We now apply inequality (80) of Theorem 34, deferring the proof of the claim that assumption (79) holds. Using (87) and Rj/Rj+1 = λ, note that X(H) = X(Hp) and ∆q(H) ≤ D = Dq yield

P(X(H) ≥ (1 + ε)µ) ≤ P(X(G) ≥ µ + εµ and ∆q(G) ≤ Dq for some G ⊆ Hp) ≤ exp −

(88)

aϕ(ε)µ max{Rℓ/s,Dℓ}

{Qj<Rj}e−dεµs/(R

+ qN−ℓ 2e−bλs + max

ℓDj+1) .

![image 97](<2016-warnke-missing-log-upper-tail_images/imageFile97.png>)

ℓ≤j<q

Note that λ = B implies Rj = Dj, in which case s ≥ 1 yields Qj = Dj = Rj. Hence Qj < Rj ensures λ = Bµ1/(q−ℓ+1), so that Rℓ = (Bµ1/(q−ℓ+1))q−ℓD. Noting Dj+1 ≤ Dℓ, it follows that

d

{Qj<Rj}e−dεµs/(R

DℓBq−ℓD · εµ1/(q−ℓ+1)s . (89) Similarly, using s ≥ 1 we also see that Rℓ/s > Dℓ implies Rℓ = (Bµ1/(q−ℓ+1))q−ℓD. Hence

ℓDj+1) ≤ exp −

max

![image 98](<2016-warnke-missing-log-upper-tail_images/imageFile98.png>)

ℓ≤j<q

a Dℓ · ϕ(ε)µ,

a Bq−ℓD · ϕ(ε)µ1/(q−ℓ+1)s . (90)

aϕ(ε)µ max{Rℓ/s,Dℓ}

≤ exp − min

exp −

![image 99](<2016-warnke-missing-log-upper-tail_images/imageFile99.png>)

![image 100](<2016-warnke-missing-log-upper-tail_images/imageFile100.png>)

![image 101](<2016-warnke-missing-log-upper-tail_images/imageFile101.png>)

Remark 11 implies min{ϕ(ε),1,ε} ≥ min{ε2,1}/3. So, combining (88)–(90), using s ≥ min{1,β} log(e/π) and λ ≥ Bµ1/(q+ℓ−1) our ﬁndings thus establish (72) for suitable c = c(ε,k,q,D,L,α) > 0.

In the following we verify assumption (79), i.e., the claim omitted above. Note that Rj/Rj+1 = λ ≥ B and Qj/Dj+1 ≥ Dj/Dj+1 = B. Using (87), for π ≤ N−τ the left hand side of (79) can thus be bounded by

B

eµj Qj

2

≤ N−4kj. (91) For π > N−τ we defer the proof of the claim that for ℓ ≤ j < q we have

≤ πβB ≤ N−τβB ≤ N−4k

![image 102](<2016-warnke-missing-log-upper-tail_images/imageFile102.png>)

min{λ,Rj/Dj+1} ≥ 4k2 log N. (92) Using (87), s ≥ 1, Qj ≥ Rj/s and (92) we see that the left hand side of (79) can be bounded by

max e−1 Rj/Rj+1 , e−s Rj/(sDj+1) ≤ max e−λ,e−R

2

j/Dj+1 ≤ N−4k

≤ N−4kj.

To sum up, we have veriﬁed (79), assuming that (92) holds for π > N−τ. Turning to the remaining claim (92), using assumption (71) we see that π > N−τ implies

λ ≥ Bµ1/(q−ℓ+1) ≥ B(log N)/A ≥ 4k2 log N. Similarly, π > N−τ, ℓ ≤ j < q and N ≥ 1 imply

Rj/Dj+1 = λq−j/Bq−j−1 ≥ Bµ1/(q−ℓ+1) q−j/Bq−j−1 ≥ B (log N)/A q−j ≥ 4k2 log N, establishing (92). As discussed, this completes the proof of (72).

# 6 Applications

In this section we illustrate our concentration techniques, by applying the basic inequalities from Section 5.1 to several pivotal examples. In Section 6.1 we improve previous work of Janson and Ruci´nski [16] on random induced subhypergraphs, and derive sharp upper tail inequalities for several quantities of interest in additive combinatorics. In Section 6.2 we answer a question of Janson and Ruci´nski [13] on subgraph counts in binomial random graphs, and improve the main applications of Wolfovitz [38] and Sileikisˇ [26].

- 6.1 Random induced subhypergraphs


In probabilistic combinatorics, random induced subhypergraphs Hp are a standard test-bed for upper tail inequalities (see, e.g., Section 3 in the survey [14]). Janson and Ruci´nski studied the number of randomly induced edges in [16], and one of their principle results concerns k-uniform hypergraphs with v(H) = N vertices, e(H) ≥ γNq edges and ∆q(H) ≤ D (for easier comparison with Theorem 2.1 in [16], note that ∆j(H) ≤ Nmax{q−j,0}∆q(H) holds). Writing X = e(Hp) and µ = EX, they obtained bounds of form

exp −C(ε)µ1/q log(1/p) ≤ P(X ≥ (1 + ε)µ) ≤ exp −c(ε)µ1/q , (93)

determining log P(X ≥ (1+ε)µ) up to a missing logarithmic factor (in fact, their lower bound needs an extra assumption). For 2 ≤ q < k the following corollary of Theorem 30 improves the exponential rate of decay of (93) in the more general weighted case. Noteworthily, inequality (94) below closes the log(1/p) gap left open by Janson and Ruci´nski [16] (for the special case q = 2 this was already resolved in [36]).

- Theorem 36 (Weighted edge-count of random induced subhypergraphs). Let 1 ≤ q < k and γ,D,a,L > 0. Assume that H is a k-uniform hypergraph with v(H) ≤ N, e(H) ≥ γNq, ∆q(H) ≤ D, and wf ∈ [a,L] for all f ∈ H. Set X = w(Hp) and µ = EX. For any ε > 0 there is c = c(ε,k,γ,D,a,L) > 0 such that for all p ∈ (0,1] we have


P(X ≥ (1 + ε)µ) ≤ exp −c min µ, µ1/q log(e/p) . (94)

- Remark 37. Setting p = m/v(H), inequality (94) also carries over to Hm as deﬁned in Section 3.5.

Inequality (94) does not always hold in the excluded case q = k. A concrete counterexample is the complete k-uniform hypergraph H = HN with V (H) = [N] and wf = 1. Then q = k, X = |[N]

p|

k ≈ |[N]p|k/k! and µ = Nk pk ≈ (Np)k/k!. For µ = ω(1), p ≤ 1/2 and ε = Θ(1) it is routine to see that P(w(Hp) ≥ (1 + ε)µ) = exp −Θ(Np) = exp −Θ(µ1/q) holds, i.e., that there is no logarithmic term.

Concerning sharpness of (94), in applications we usually do not consider a single hypergraph H, but sequences of hypergraph (HN)N∈N which are nearly monotone, i.e., where HN ⊆ HN+1 holds up to some minor ‘defects’ (arising, e.g., due to boundary eﬀects). The following remark states that, in this frequent case, the upper tail inequality (94) is best possible up to the value of the parameter c (for 2 ≤ q < k).

- Remark 38 (Matching lower bound). Let 2 ≤ q < k and γ,D,a,L,n1,n2 > 0. Let (HN)N≥n


be a sequence of k-uniform hypergraphs such that all H = HN satisfy the assumptions of Theorem 36. Assume that there is β ∈ (0,1] such that e(HN ∩ HM) ≥ βe(HN) for all M ≥ N ≥ n2. Then for all ε > 0 there are n0 = n0(k,γ,D,a,L,β,n1,n2) > 0 and C = C(ε,γ,k,q,D,a,L,β,n1,n2,) > 0 such that for all H = HN with N ≥ n0, setting X = w(Hp) and µ = EX, for all p ∈ (0,1] we have

1

P(X ≥ (1 + ε)µ) ≥ {1≤(1+ε)µ≤w(H)} exp −C min µ, µ1/q log(1/p) . (95) We omit the proof of Remark 38, which mimics the lower bound techniques from [36] in a routine way.

- Proof of Theorem 36. Let δ = aγ, and note that µ ≥ e(H)pk · minf∈H wf ≥ δNqpk (we never use wf ≥ a again, i.e., we could weaken our assumptions). Inequality (94) holds trivially whenever N < k (since then


0 ≤ w(Hp) ≤ L·e(H) = 0), so we may henceforth assume N ≥ k. Our main task is to verify the assumptions of Theorem 30. Let ℓ = 1 and τ = q/(2k). As N1/2 ≥ log N for all N > 0, for p ≥ N−τ we have

µ1/(q−ℓ+1) = µ1/q ≥ δ1/qNpk/q ≥ δ1/qN1−kτ/q ≥ δ1/qN1/2 ≥ δ1/q log N. (96)

As discussed in Example 20, using (57) and |ΓU(H)| ≤ v(H)q−j · ∆q(H), for 1 ≤ j < q we thus have µj ≤ Nq−j · D · pk−j. (97)

- Recalling ℓ = 1, (96) and q < k, there thus is a constant A = A(D,δ) > 0 such that for 1 ≤ j < q we have


DNq−jpk−j

µj µ(q−j)/(q−ℓ+1) ≤

(µ1/q)q−j ≤ Dδj/q−1pj(k/q−1) ≤ Ap1/q. (98) Hence assumptions (70)–(71) hold with π = p and α = 1/q. Using (72) of Theorem 30 it follows that

![image 107](<2016-warnke-missing-log-upper-tail_images/imageFile107.png>)

![image 108](<2016-warnke-missing-log-upper-tail_images/imageFile108.png>)

P(w(Hp) ≥ (1 + ε)µ) ≤ (1 + 3qN−1)e−Π, (99) where Π = c′ min ε2,1 min{µ, µ1/(q−ℓ+1) log(e/p)} and c′ = c′(ℓ,q,k,L,D,A,δ) > 0.

The author ﬁnds (99) quite satisfactory, but in the literature the usually irrelevant prefactor 1+3qN−1 is often suppressed for cosmetic reasons. Below we shall achieve this by inﬂating the constant in the exponent (without assuming that n, p or Π are large). If Π ≥ 6, then N ≥ k ≥ q implies 3qN−1 ≤ 3 ≤ Π/2, so that

−1

P(w(Hp) ≥ (1 + ε)µ) ≤ e−Π+3qN

≤ e−Π/2. Otherwise 1 ≥ Π/6 holds, in which case ε/(1 + ε) ≥ min{1,ε}/2 and Markov’s inequality yield P(w(Hp) ≥ (1 + ε)µ) ≤

ε

1 1 + ε

1 + ε ≤ e−ε/(1+ε) ≤ e−min{1,ε}Π/12, establishing (94) for suitable c = c(ε,c′) > 0.

= 1 −

![image 109](<2016-warnke-missing-log-upper-tail_images/imageFile109.png>)

![image 110](<2016-warnke-missing-log-upper-tail_images/imageFile110.png>)

![image 111](<2016-warnke-missing-log-upper-tail_images/imageFile111.png>)

![image 112](<2016-warnke-missing-log-upper-tail_images/imageFile112.png>)

![image 113](<2016-warnke-missing-log-upper-tail_images/imageFile113.png>)

![image 114](<2016-warnke-missing-log-upper-tail_images/imageFile114.png>)

Combining Theorem 36 and Remark 38, we obtain the following convenient upper tail result (see [36] for a similar result in the special case q = 2). It applies to many widely-studied objects in additive combinatorics and Ramsey theory, each time closing the logarithmic gap present in previous work, see (93) and [16].

Corollary 39. Let 2 ≤ q < k and γ,D,a,L,n1 > 0. Let (Hn)n≥n

be k-uniform hypergraphs such that Hn ⊆ Hn+1, v(Hn) ≤ n, e(Hn) ≥ γnq, ∆q(Hn) ≤ D, and wf ∈ [a,L] for all f ∈ Hn. Then for all ε > 0 there are n0 = n0(k,γ,D,a,L,n1) > 0 and c,C > 0 (depending only on ε,k,γ,D,a,L,n1) such that for all H = Hn with n ≥ n0, setting X = w(Hp) and µ = EX, for all p ∈ (0,1] we have

1

{1≤(1+ε)µ≤w(H)} exp −CΨq,µ ≤ P(X ≥ (1 + ε)µ) ≤ exp −cΨq,µ , (100)

where Ψq,µ = min{µ, µ1/q log(1/p)}.

In particular, letting the edges of the k-uniform hypergraphs Hn with vertex-set V (H) = [n] encode the relevant objects, it is not diﬃcult to check that Corollary 39 with uniform weights wf = 1 implies7 all the upper tail bounds presented in Examples 2–5 of Section 1.1.1 (using q = 2 for k-term arithmetic progressions, (k,q) = (3,2) for Schur triples, (k,q) = (4,3) for additive quadruples, and (k,q) = (r +s,r + s −1) for (r,s)sums). Motivated by Section 2.1 in [16], we now record a further common generalization of these examples.

Example 40 (Integer solutions of linear homogeneous systems). Let 1 ≤ r ≤ k − 2. Let A be a r × k integer matrix. Following [16], we assume that every r × r submatrix B of A has full rank, i.e., rank(B) = r = rank(A). We also assume that there exists a distinct-valued positive integer solution to Ax = 0, where x = (x1,...,xk) is a column vector and 0 = (0,...,0) is an r-dimensional column vector. Let the edges of the k-uniform hypergraph Hn with V (Hn) = [n] encode solutions {x1,...,xk} ⊆ [n] of the system Ax = 0 with distinct xi. The discussion of Section 2.1 in [16] implies that (Hn)n≥n

![image 115](<2016-warnke-missing-log-upper-tail_images/imageFile115.png>)

![image 116](<2016-warnke-missing-log-upper-tail_images/imageFile116.png>)

![image 117](<2016-warnke-missing-log-upper-tail_images/imageFile117.png>)

satisﬁes the assumptions of Corollary 39 with q = k − r, so the upper tail inequality (100) holds for X = e(Hp), say.

1

![image 118](<2016-warnke-missing-log-upper-tail_images/imageFile118.png>)

7Note that using weights wf = 1 we count unordered objects, i.e., treat the objects as k-sets (if desired, we could also treat them as ordered k-vectors by using non-uniform weights wf > 0, say).

- 6.1.1 Small expectations case


Note that inequality (100) does not guarantee a similar dependence of c,C > 0 on ε. Of course, we can also ask for ﬁner results, which determine how the exponential decay of the upper tail depends on ε. The following corollary of Theorem 32 provides a partial answer for small p (see [36] for results which for q = 2 cover all p).

- Theorem 41. Let k ≥ 2. Let 1 ≤ q ≤ k and D,L > 0. Assume that H is a k-uniform hypergraph with

v(H) ≤ N, ∆q(H) ≤ D and maxf∈H wf ≤ L, where N ≥ 1. Set X = w(Hp) and µ = EX. For all σ,Λ > 0 there are c = c(σ,Λ,k,D,L) > 0 and d = d(q) ≥ 1 such that for all p ≤ ΛN−(q−1)/(k−1)−σ and t > 0 we have

P(X ≥ µ + t) ≤ dexp −c min ϕ(t/µ)µ, t1/q log N . (101) Furthermore, setting p = m/v(H), inequality (101) also holds with Hp replaced by Hm.

Assume that H = HN also satisﬁes e(HN) ≥ γNq, the monotonicity conditions of Remark 38, wf = 1 and 2 ≤ q < k. Mimicking the lower bound arguments from [36], inequality (101) can then shown to be best possible up to the values of d,c for some range of small p (we leave the details to the interested reader).

- Proof of Theorem 41. Our main task is to verify assumption (73) of Theorem 32. To this end we exploit that


q − 1 k − 1

![image 119](<2016-warnke-missing-log-upper-tail_images/imageFile119.png>)

= max

1≤j<q

q − j k − j

![image 120](<2016-warnke-missing-log-upper-tail_images/imageFile120.png>)

. Indeed, using (97) and N ≥ 1 there thus is a constant A = A(D,Λ) > 0 such that we have max

1≤j<q

µj ≤

1≤j<q

DNq−jpk−j ≤ D

1≤j<q

Λk−jN(q−j)−(k−j)(q−1)/(k−1)−(k−j)σ ≤ AN−σ.

Applying Theorem 32 (with σ = α and K = 1) now readily establishes inequality (101).

![image 121](<2016-warnke-missing-log-upper-tail_images/imageFile121.png>)

![image 122](<2016-warnke-missing-log-upper-tail_images/imageFile122.png>)

![image 123](<2016-warnke-missing-log-upper-tail_images/imageFile123.png>)

![image 124](<2016-warnke-missing-log-upper-tail_images/imageFile124.png>)

6.2 Subgraph counts in random graphs

In this section we consider subgraph counts in the binomial random graph Gn,p, which are pivotal examples for illustrating various concentration methods (see, e.g., [20, 32, 33, 14, 15, 12] and Examples 21–22 in Section 4.1.1). We shall discuss two qualitatively diﬀerent upper tail bounds in Sections 6.2.1 and 6.2.2. We henceforth tacitly write X = XH for the number of copies of H in Gn,p, and set µ = EX = Θ(nv

H

pe

H

). Let us recall some deﬁnitions from random graph theory. Writing d(J) = eJ/vJ, a graph H is called balanced if eH ≥ 1 and d(H) ≥ d(J) for all J H with vJ ≥ 1. If this holds with d(H) > d(J), then H is called strictly balanced. Writing d2(J) = (eJ − 1)/(vJ − 2), a graph H is called 2-balanced if eH ≥ 2 and d2(H) ≥ d2(J) for all J H with vJ ≥ 3. If this holds with d2(H) > d2(J), then H is called strictly 2-balanced.

- 6.2.1 Small deviations: sub-Gaussian type bounds


We ﬁrst consider sub-Gaussian type P(X ≥ µ + t) ≤ C exp(−ct2/ VarX) upper tail inequalities. Our main focus is on the Poisson range, where Var X ∼ EX = µ holds, which according to Kannan [19] is the more diﬃcult range. For small p the following simple corollary of Theorem 32 extends/sharpens several results from [31, 15, 26, 38, 19, 37], and implies Theorem 6. (For balanced and 2-balanced graphs H it is folklore that δH ≥ 1. Furthermore, with the exception of perfect matchings, all 2-balanced graphs are strictly balanced.)

- Theorem 42 (Subgraph counts in random graphs: small expectations case). Let H be a graph with v =


vH vertices, e = eH edges and minimum degree δ = δH. Let X = XH and µ = EX. Deﬁne s = min{v − 1,e − δ + 1}. If H is strictly balanced, then for every Λ > 0 there are c = c(Λ,H) > 0 and C = C(H) ≥ 1 such that for all n ≥ v, ε ∈ (0,Λ] and p ∈ [0,1] satisfying µ(s−1)/s ≤ Λ logn we have

P(X ≥ (1 + ε)µ) ≤ C exp −cε2µ . (102)

If H is 2-balanced, then for all σ,Λ > 0 there are c = c(σ,Λ,H) > 0 and C = C(H) ≥ 1 such that for all n ≥ v, 0 ≤ p ≤ Λn−(v−2)/(e−1)−σ and 0 < t ≤ Λ min{(µlog n)1/(2−1/s),µ} we have

P(X ≥ µ + t) ≤ C exp −ct2/µ . (103)

Remark 43. It is well-known that in (102)–(103) we have µ = EX ∼ Var X when p = o(1). The proof shows that the constants C can be replaced by 1+o(1), and that (102)–(103) both carry over to Gn,m. Furthermore, [27] demonstrates that the sub-Gaussian type tail inequality (102) can already fail for balanced graphs H.

To put Theorem 42 into context, in the year 2000 Vu [31] showed that the sub-Gaussian inequality (102) holds for strictly balanced graphs as long as ε = O(1) and µ ≤ log n (note that ε2µ ∼ (εµ)2/ VarX by Remark 43). Shortly afterwards, this result was reproved via a diﬀerent method by Janson and Ruci´nski [15], who also raised the question whether the restriction µ = O(log n) is necessary (see Section 6 in [13]). For the special case ε = Θ(1) the aforementioned results were yet again reproved by Sileikisˇ [26] in 2012. Our methods allow us (i) to go beyond all these three approaches from 2000–2012, and (ii) to answer the aforementioned question of Janson and Ruci´nski: inequality (102) still holds in the wider range µ = O((log n)1+ξ).

Wolfovitz demonstrated the applicability of his sub-Gaussian concentration result [38] via the complete graph Kr and the complete bipartite graph Kr,r, showing that inequality (103) holds for both strictly 2balanced graphs in certain ranges of the parameters p,t. Theorem 42 generalizes these main applications from [38] to all 2-balanced graphs (for a slightly wider parameter range). For n−1 ≤ p ≤ n−1/2−σ inequality (103) also slightly extends the t–range of two K3-speciﬁc results of Kannan [19] and Wolfovitz [37].

- Proof of Theorem 42. The proofs of (102)–(103) are very similar: each time we shall apply Theorem 32 twice, using the two diﬀerent setups of Examples 21–22. Hence our main task is to check assumption (73).


For (102) we assume that H is strictly balanced, in which case δ = δH ≥ 1 is folklore. By assumption there is a constant β = β(H) > 0 such that for all subgraphs J H with vJ ≥ 1 we have

e v ≥ eJ + β and eJ ·

v e ≤ vJ − β. (104)

vJ ·

![image 125](<2016-warnke-missing-log-upper-tail_images/imageFile125.png>)

![image 126](<2016-warnke-missing-log-upper-tail_images/imageFile126.png>)

Using the setup of Example 21, by (58) there is a constant B1 > 0 such that the corresponding µj satisfy max

pe−e

nv−v

µj ≤ B1

. (105)

J

J

1≤j<e−δ+1

J⊆H:1≤eJ <e−δ+1

Similarly, using the setup of Example 22, by (59) there is a constant B2 > 0 such that max

pe−e

nv−v

µj ≤ B2

. (106)

J

J

2≤j<v

J⊆H:2≤vJ<v

Recalling s = min{v − 1,e − δ + 1}, in our further estimates of (105)–(106) we may assume s > 1 (otherwise H = K2 and (105)–(106) are both equal to zero). Recalling µ = Θ(nvpe), we now pick S = S(Λ,H) ≥ 1 large enough such that the assumption µ(s−1)/s ≤ Λ log n implies p ≤ Sn−v/e+β/(2e) for all n ≥ v. Using δ = δH ≥ 1 and the density condition (104), it follows that there are constants B3,B4,B5 > 0 such that

pe−e

nv−v

Jv/e−vJ+β/2 ≤ B5n−β/2. (107)

ne

(105) + (106) ≤ B3

≤ B4

J

J

J⊆H:vJ≥2,eJ<e

J⊆H:vJ≥2,eJ<e

Armed with (107), we now apply Theorem 32 with K = 1, A = B5 and α = β/4, using the setup of Example 21 (with ℓ = 1, k = e, q = e − δ + 1 and N = n2) and Example 22 (with ℓ = 2, k = q = v and N = n). So, applying (74) twice, there is a constant c1 > 0 such that for t = εµ we have

P(X ≥ µ + t) ≤ 1 + 2 max{vH,eH}n−1 exp −c1 min t2/µ, t, t1/s log n . (108)

Since t = εµ ≤ Λµ, we infer t ≥ t2/(Λµ). Hence, after adjusting the constant c1, the t-term is irrelevant for the exponent of (108). As t2−1/s ≤ (Λµ)1+(s−1)/s = O(µlog n) by assumption, this establishes (102).

For (103) we proceed similarly, assuming that H is 2-balanced. In this case, for all subgraphs J H with 2 ≤ vJ < v, the assumption that H is 2-balanced (and noting that (109) is trivial when vJ = 2) implies

(e − 1) − (eJ − 1) (v − 2) − (vJ − 2) ≥

e − 1 v − 2

e − eJ v − vJ

=

. (109)

![image 127](<2016-warnke-missing-log-upper-tail_images/imageFile127.png>)

![image 128](<2016-warnke-missing-log-upper-tail_images/imageFile128.png>)

![image 129](<2016-warnke-missing-log-upper-tail_images/imageFile129.png>)

Analogous to (107), in Examples 21 and 22 (with 1 ≤ j < e − δ + 1 and 2 ≤ j < v) the assumption p ≤ Λn−(v−2)/(e−1)−σ and the density result (109) entail existence of constants B6,B7 > 0 such that

n(v−v

J)−(e−eJ)(v−2)/(e−1)−(e−eJ)σ ≤ B7n−σ. (110)

µj ≤ B6

J⊆H:vJ≥2,eJ<e

Armed with (110), we now obtain (108) by applying Theorem 32 twice (with A = B7 and α = σ/2) analogous to the proof of (102). Noting t ≤ Λµ and t2−1/s = O(µlog n) then readily completes the proof of (103).

![image 130](<2016-warnke-missing-log-upper-tail_images/imageFile130.png>)

![image 131](<2016-warnke-missing-log-upper-tail_images/imageFile131.png>)

![image 132](<2016-warnke-missing-log-upper-tail_images/imageFile132.png>)

![image 133](<2016-warnke-missing-log-upper-tail_images/imageFile133.png>)

Parts of Theorem 42 can be proved in a simpler/more direct way, but in view of the previous work [31, 15, 26, 38, 19, 37] here the main point is to illustrate that (102)–(103) follow routinely from our general bounds.

- 6.2.2 Large deviations: upper tail problem


Next we consider the classical upper tail problem for subgraph counts, which concerns P(X ≥ (1 + ε)µ) for constant ε > 0. Here our general methods usually give much weaker estimates than modern specialized approaches such as [12, 7, 6], but it turns out that our methods can routinely sharpen results based on classical inductive approaches (which might potentially be useful in other contexts). Indeed, for balanced graphs Kim and Vu used two diﬀerent inductions (see Sections 6.3 and 6.6 in [33]), which together establish the following tail estimate: if ε ≤ C and ε2 max{µ1/(v−1),µ1/e} = ω(log n), then

P(X ≥ (1 + ε)µ) ≤ exp −cε2 max µ1/(v−1),µ1/e . (111)

This inequality was reproved by Janson and Ruci´nski [15] via their alternative inductive method. Using Theorem 30, we shall go beyond both approaches for strictly balanced graphs: (i) we improve the exponential rate of decay by an extra logarithmic factor, and (ii) we remove the restriction to ‘large’ expectations µ.

Theorem 44. Let H be a strictly balanced graph with v = vH vertices and e = eH edges. Let X = XH and µ = EX. For any ε > 0 there is c = c(ε,H) > 0 such that for all n ≥ v and p ∈ [0,1] we have

P(X ≥ (1 + ε)µ) ≤ exp −c min µ, max µ1/(v−1),µ1/e log n . (112)

- Remark 45. Writing the exponent of (112) in the form exp(−cΨ), the proof shows that c = c′ min{ε2,1}

with c′ = c′(H) > 0 suﬃces when min{ε2,1}Ψ ≥ 1. Furthermore, inequality (112) also carries over to Gn,m.

- Remark 46. For balanced graphs H, the proof yields the following variant: for all n ≥ v, p ≥ ξn−v/e+σ and ε > 0 we have P(X ≥ (1 + ε)µ) ≤ exp(−cµ1/(v−1) log n), where c = c(σ,ξ,ε,H) > 0.


For r-armed stars H = K1,r inequality (112) yields an exp −Ω(min{µ,µ1/r log n}) exponential decay, which by [28] is best possible for p ≤ n−1/r and ε = Θ(1). However, for general graphs H other approaches such as [12, 7, 6] yield better estimates (as mentioned before), so we defer the proof of Theorem 44 to Appendix A.

Acknowledgement. We are grateful to the referees for helpful suggestions concerning the presentation.

# References

- [1] A. Baltz, P. Hegarty, J. Knape, U. Larsson, and T. Schoen. The structure of maximum subsets of {1, . . . , n} with no solutions to a + b = kc. Electron. J. Combin. 12 (2005), Paper 19.
- [2] M. Bateman, and N.H. Katz. New bounds on cap sets. J. Amer. Math. Soc. 25 (2012), 585–613.
- [3] J. van den Berg and H. Kesten. Inequalities with applications to percolation and reliability. J. Appl. Probab. 22

(1985), 556–569.

- [4] J. van den Berg and J. Jonasson. A BK inequality for randomly drawn subsets of ﬁxed size. Probab. Theory Related Fields 154 (2012), 835–844.
- [5] T. Bloom. A quantitative improvement for Roth’s theorem on arithmetic progressions. J. Lond. Math. Soc. 93

(2016), 643–663.

- [6] S. Chatterjee. The missing log in large deviations for triangle counts. Random Struct. Alg. 40 (2012), 437–451.
- [7] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Struct. Alg. 41 (2012), 469–487.


- [8] P. Erd˝s and P. Tetali. Representations of integers as the sum of k terms. Random Struct. Alg. 1 (1990), 245–261.
- [9] R. Graham, V. Ro¨dl, and A. Rucin´ski. On Schur properties of random subsets of integers. J. Number Theory 61

(1996), 388–408.

- [10] B. Green. The Cameron–Erd˝s conjecture. Bull. London Math. Soc. 36 (2004), 769–778.
- [11] S. Janson. Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221–229.
- [12] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math. 142 (2004), 61–92.
- [13] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Preprint (2000). http://www2.math.uu.se/~svante/papers/sj135_ppt.pdf
- [14] S. Janson and A. Rucin´ski. The infamous upper tail. Random Struct. Alg. 20 (2002), 317–342.
- [15] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica 24 (2004), 615–640.
- [16] S. Janson and A. Rucin´ski. Upper tails for counting objects in randomly induced subhypergraphs and rooted random graphs. Ark. Mat. 49 (2011), 79–96.
- [17] S. Janson. New versions of Suen’s correlation inequality. Random Struct. Alg. 13 (1998), 467–483.
- [18] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Struct. Alg. 48 (2016), 219–246.
- [19] R. Kannan. Two new Probability inequalities and Concentration Results. Preprint (2010). arXiv:0809.2477v4.
- [20] J.H. Kim and V.H. Vu. Concentration of multivariate polynomials and its applications. Combinatorica 20 (2000), 417–434.
- [21] D. Reimer. Proof of the van den Berg-Kesten conjecture. Combin. Probab. Comput. 9 (2000), 27–32.
- [22] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Struct. Alg. 46 (2015), 391–395.
- [23] V. Ro¨dl and A. Rucin´ski. Random graphs with monochromatic triangles in every edge coloring. Random Struct. Alg. 5 (1994), 253–270.
- [24] A. Rucin´ski. When are small subgraphs of a random graph normally distributed? Probab. Theory Related Fields 78 (1988), 1–10.
- [25] M. Schacht. Extremal results for random discrete structures. Ann. of Math. 184 (2016), 333–365.
- [26] M. Sileikis.ˇ On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin. 19 (2012), Paper 4.
- [27] M. Sileikisˇ and L. Warnke. A counterexample to the DeMarco-Kahn Upper Tail Conjecture. Random Struct. Alg., to appear. arXiv:1809.09595.
- [28] M. Sileikisˇ and L. Warnke. Upper tail bounds for Stars. Preprint (2019). arXiv:1901.10637.
- [29] J. Spencer. Counting extensions. J. Combin. Theory Ser. A 55 (1990), 247–255.
- [30] R. Spo¨hel, A. Steger and L. Warnke. General deletion lemmas via the Harris inequality. J. Combin. 4 (2013), 251–271.
- [31] V.H. Vu. On the concentration of multivariate polynomials with small expectation. Random Struct. Alg. 16

(2000), 344–363.

- [32] V.H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput. 10 (2001), 79–94.
- [33] V.H. Vu. Concentration of non-Lipschitz functions and applications. Random Struct. Alg. 20 (2002), 262–316.
- [34] L. Warnke. When does the K4-free process stop? Random Struct. Alg. 44 (2014), 355–397.
- [35] L. Warnke. On the method of typical bounded diﬀerences. Combin. Probab. Comput. 25 (2016), 269–299.
- [36] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math. 221 (2017), 317–365.
- [37] G. Wolfovitz. Sub-Gaussian tails for the number of triangles in G(n, p). Combin. Probab. Comput., 20(1):155–160, 2011.
- [38] G. Wolfovitz. A concentration result with application to subgraph count. Random Struct. Alg. 40 (2012), 254–267.


# A Proofs omitted from Section 6.2.2

In this appendix we give the proof of Theorem 44, which proceeds similar to Theorem 36 and 42. Namely, we prove (112) by two applications of Theorem 30 and Remark 31 (using the setups of Examples 21–22).

Proof of Theorem 44. We ﬁrst use the setup of Example 21 with ℓ = 1, q = k = e and N = n2. Using the bound (58) for µj, the expectation µ = Θ(nvpe) and the density result (104), for 1 ≤ j < e = eH we infer

pe−j (µ1/e)e−j ≤ B1

J=j nv−v

B J⊆H:e

J

µj µ(q−j)/(q−ℓ+1) ≤

Jv/e−vJ ≤ B2n−β. (113)

ne

![image 134](<2016-warnke-missing-log-upper-tail_images/imageFile134.png>)

![image 135](<2016-warnke-missing-log-upper-tail_images/imageFile135.png>)

J⊆H:eJ=j

Applying Theorem 30 and Remark 31 with A = B2 and α = β/2, there thus is c1 > 0 such that

P(X ≥ (1 + ε)µ) ≤ (1 + 3eHn−2)exp −c1 min ε2,1 min{µ, µ1/e log n} . (114) Next we use the setup of Example 22 with ℓ = 2, k = q = v and N = n. We distinguish several cases. If

p ≤ n−v/e, then using the bound (58) for µj and the density result (104), we infer for 2 ≤ j < v = vH that µj ≤ B

pe−e

nv−v

Jv/e−vJ ≤ B3n−β. (115)

ne

≤ B

J

J

J⊆H:vJ=j

J⊆H:2≤vJ<vH

Otherwise p ≥ n−v/e, so nvpe ≥ 1. Note that for j < v we have (v − j)/(v − 1) ≥ (v − j)/v + 1/v2.

- Recalling ℓ = 2 and q = v, using (59), µ = Θ(nvpe) and (104) we infer for 2 ≤ j < v = vH that


Je/v−eJ

J=j pv

B5 J⊆H:v

B6pβ (nvpe)1/v2

µj µ(q−j)/(q−ℓ+1) ≤

µj B4(nvpe)(v−j)/v+1/v2 ≤

(nvpe)1/v2 ≤

. (116)

![image 136](<2016-warnke-missing-log-upper-tail_images/imageFile136.png>)

![image 137](<2016-warnke-missing-log-upper-tail_images/imageFile137.png>)

![image 138](<2016-warnke-missing-log-upper-tail_images/imageFile138.png>)

![image 139](<2016-warnke-missing-log-upper-tail_images/imageFile139.png>)

Distinguishing n−v/e ≤ p ≤ n−v/(2e) and n−v/(2e) ≤ p ≤ 1, we see that µj

µ(q−j)/(q−ℓ+1) ≤ B6 max{n−βv/(2e),n−1/(2v)}. (117) Applying Theorem 30 and Remark 31 with A = max{B3,B6} and α = min{β,βv/(2e),1/(2v)}, we deduce

![image 140](<2016-warnke-missing-log-upper-tail_images/imageFile140.png>)

P(X ≥ (1 + ε)µ) ≤ (1 + 3vHn−1)exp −c2 min ε2,1 min{µ, µ1/(v−1) log n} . (118)

Finally, we combine the two upper bounds (114) and (118), and then remove (for cosmetic reasons) the multiplicative prefactor 1 + O(n−1) analogous to the proof of Theorem 36, which establishes (112). For Remark 46 the point is that for balanced graphs H the density condition (104) only holds with β = 0, so in (116) we need p ≥ ξn−v/e+σ to establish (117) with ≤ O(n−eσ/v

![image 141](<2016-warnke-missing-log-upper-tail_images/imageFile141.png>)

![image 142](<2016-warnke-missing-log-upper-tail_images/imageFile142.png>)

![image 143](<2016-warnke-missing-log-upper-tail_images/imageFile143.png>)

![image 144](<2016-warnke-missing-log-upper-tail_images/imageFile144.png>)

2

), say.

