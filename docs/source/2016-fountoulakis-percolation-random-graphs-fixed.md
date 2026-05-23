---
type: source
kind: paper
title: Percolation on random graphs with a fixed degree sequence
authors: Nikolaos Fountoulakis, Felix Joos, Guillem Perarnau
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1611.08496v2
source_local: ../raw/2016-fountoulakis-percolation-random-graphs-fixed.pdf
topic: general-knowledge
cites:
---

PERCOLATION ON RANDOM GRAPHS WITH A FIXED DEGREE SEQUENCE

NIKOLAOS FOUNTOULAKIS, FELIX JOOS AND GUILLEM PERARNAU

arXiv:1611.08496v2[math.CO]11Jan2022

Abstract. We consider bond percolation on random graphs with given degrees and bounded average degree. In particular, we consider the order of the largest component after the random deletion of the edges of such a random graph. We give a rough characterisation of those degree distributions for which bond percolation with high probability leaves a component of linear order, known usually as a giant component. We show that essentially the critical condition has to do with the tail of the degree distribution. Our proof makes use of recent technique which is based on the switching method and avoids the use of the classic conﬁguration model on degree sequences that have a limiting distribution. Thus our results hold for sparse degree sequences without the usual restrictions that accompany the conﬁguration model.

keywords: random graphs with given degrees, bond percolation, giant component, power law 2010 AMS Subj. Class.: 05C80, 05C82

1. Introduction

Random graphs with a given degree sequence have become an integral part of the theory of random graphs. Let n ≥ 2 and let D = (d1,... ,dn) be a degree sequence of length n; that is, a vector of non-negative integers which represent the degrees of the set of vertices [n] := {1,... ,n}. In other words, vertex i has degree di for each i ∈ [n]. Without loss of generality, we assume that d1 ≤ ... ≤ dn. In fact, our results deal with properties that are closed under automorphisms and remain valid when relabelling the vertex set. If not stated otherwise, we will assume that d1 ≥ 1. The results for degree sequences containing vertices of degree 0 can be easily deduced from the analysis of degree sequences without them. We will also assume that D is feasible; that is, there exists at least one graph with degree sequence D. The main object of our study is GD, which is a graph chosen uniformly at random among all simple graphs on [n] having degree sequence D.

Random graphs with a given degree distribution appear also in the context of graph enumeration. Bender and Canﬁeld [4], as well as Bollob´s [6] and Wormald [26], came up with the now well-known conﬁguration model, which has become a standard tool in the analysis of random graphs that are sampled uniformly from the set of all simple graphs with a given degree sequence. However, the study of such random graphs through the conﬁguration model has some limitations, as it often requires bounds on the growth of the maximum degree of the degree sequence. Typically, these are implicitly imposed by bounds on the second (or higher) moment of the degree sequence.

In 1995, Molloy and Reed [18] investigated the component structure of GD and, more speciﬁcally, the emergence of the giant component (a component containing at least a constant fraction of the vertices). This is one of the central questions in the theory of random graphs. They provided a condition on D that characterises the emergence of a giant component in GD given that D satisﬁes a number of technical conditions. This result has been widely applied to the analysis of a variety of complex networks [1, 2, 5, 22] and there are several reﬁnements of it [8, 12, 14, 16, 19]. The technical restrictions on D in [18] result from the use of the conﬁguration model. These restrictions have been weakened in subsequent papers [8, 14]. Recently, Joos, Perarnau, Rautenbach, and Reed [15] managed to completely remove all restrictions on D by using an analysis based on the switching method. This provides a new criterion for the existence of a giant component in GD that can be applied to every degree sequence.

![image 1](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile1.png>)

Felix Joos was supported by the EPSRC, grant no. EP/M009408/1. Guillem Perarnau was supported by Ministerio de Economı´a y Competitividad grant MTM2017-82166-P and the Ministerio de Ciencia e Innovaci´on grant PID2020-113082GB-I00.

1

In this paper, we follow this novel approach and consider the component sizes of a random graph with a given degree sequence under the random deletion of its edges. For a graph G and a real number p ∈ [0,1], we denote by Gp the random subgraph of G in which every edge of G is retained independently with probability p. This is commonly known as bond percolation on G. The theme of this paper is the component structure of GDp . Since GD itself is a random graph, GDp should be understood as follows: ﬁrst, we choose a graph GD uniformly at random from the set of all simple graphs with degree sequence D and thereafter each edge of GD is retained independently with probability p.

The structure of GD has been studied in great detail for the case di = d for all i ∈ [n] and some d ∈ N (in this case we also write G(n,d) for GD). The bond percolation of G(n,d) was ﬁrst studied by Goerdt [11]. He proved that there exists a critical value pcrit = 1/(d − 1) such that the existence of a giant component depends on whether p < pcrit or p > pcrit. Bond percolation of G(n,d) near the critical probability pcrit has been extensively studied [21, 23, 24]. The ﬁrst author [10] and Janson [13] considered the bond percolation of GD, proving the existence of a critical probability, provided that D satisﬁes some technical conditions, similar to those required in [18]. These results have been extended to a more general setting by Bollob´s and Riordan [8].

In the present work, we determine those conditions on D which ensure that pcrit is bounded away from 0. We consider arbitrary degree sequences without restrictions as in [8, 10, 13, 18] and we only insist that the total number of edges grows linearly with the number of vertices n. We call those sequences sparse. (We brieﬂy discuss the non-sparse case at the end of the paper.) Besides the mathematical motivation, sparse graphs are also the main focus in the theory of complex networks as this is a property that is observed in several networks that arise in applications [2].

Consider a sequence of degree sequences D = (Dn)n≥2, where Dn = (d(1n),... ,d(nn)). Let Dn be the random variable that is the degree in Dn of a vertex selected uniformly at random. For c ∈ N, we deﬁne W(c,D) := {i : di ≥ c}; that is, W(c,D) is the set of vertices of degree at least c and set Wn(c) := W(c,Dn). The sequence (Dn)n≥2 is uniformly integrable if for every ε > 0, there exist c,n0 such that for every n ≥ n0, we have

- (1) d(in) ≤ εn,

and strongly uniformly integrable if for every ε > 0, there exists c0 such that for any c ≥ c0 there exists n0 such that for every n ≥ n0, we have

i∈Wn(c)

d(in) ≤

ε

![image 2](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile2.png>)

- (2) c · n.

Strong uniform integrability can be seen as a weaker version of bounded second moment conditions. We say that (Dn)n≥2 robustly fails the strong uniform integrability assumption if there exists a function f : R → R, such that f(x) → ∞ as x → ∞, and a c0 > 0 with the property that for any c ≥ c0 there exists n0 such that for all n ≥ n0 we have

i∈Wn(c)

d(in) >

f(c)

![image 3](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile3.png>)

- (3) c · n.


i∈Wn(c)

For a graph G, we denote by L1(G) the number of vertices in the largest component (ties are resolved following the lexicographic ordering of the vertices).

We now state our main result in the context of sequences of degree sequences that satisfy a mild convergence condition.

- Theorem 1. Suppose that d¯ ≥ 1 and let D = (Dn)n≥2 be a sequence of degree sequences such that for all n ≥ 2 the average degree of Dn is at most d¯. Suppose that


,1  

max  

i∈V \Wn(c) d(in)(d(in) − 1) i∈V \Wn(c) d(in)

d = d(D) := sup

lim

![image 4](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile4.png>)

n→∞

c≥1

exists. Let Dn be the degree in Dn of a vertex chosen uniformly at random. Then

- (i) if the sequence (Dn)n≥2 is strongly uniformly integrable and d < ∞, then for every ǫ > 0 the following hold:

- - if 0 ≤ p ≤ (1 − ǫ)1d, then P[L1(GDp n) = o(n)] = 1 − o(1) ;

![image 5](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile5.png>)

- - if (1 + ǫ)1d ≤ p ≤ 1, then there exists ρ = ρ(ǫ) such that P[L1(GDp n) > ρn] = 1 − o(1) .


![image 6](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile6.png>)

- (ii) if either d = ∞ or the sequence robustly fails the strong uniform integrability assumption, then for all p,δ ∈ (0,1), there exist ρ > 0 and n0 such that for all n ≥ n0, we have


P[L1(GDp n) > ρn] ≥ 1 − δ .

The proof of this theorem relies on a dichotomy within the class of all sparse degree sequences D of length n. This dichotomy is expressed through Theorems 2 and 3 below, which are much stronger, albeit somewhat technical, results. Roughly speaking, if the tail of the degree sequence D is suﬃciently thin (conditions A1 and A2 below are satisﬁed), then there exists a critical probability pcrit bounded away from 0 (essentially determined by D) such that when p crosses pcrit the fraction of vertices that belong to the largest component undergoes a rapid increase with high probability. On the other hand, if the tail is suﬃciently heavy (either A1 or A2 are not satisﬁed), then for every p ∈ (0,1], there is a giant component with high probability.

Let us now make these statements precise. For every x > 0 and every c ∈ N, we say that D satisﬁes A1(x,c) if

x

- (4) c · n .

For all x > 0 and c1,c2 ∈ N, we say that D satisﬁes A2(x,c1,c2) if

i∈W(c1,D)\W(c2,D)

d2i ≤

x

![image 7](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile7.png>)

- (5) 4 · n .

Note that being strongly uniformly integrable is equivalent to satisfying condition A1(ε,c0) for every ε > 0 and c0 = c0(ε). Also observe that these integrability notions naturally extend to Dn, even if the sequence Dn does not converge in distribution.

The ﬁrst part of this dichotomy describes which degree sequences have a percolation threshold.

- Theorem 2. For all ǫ,γ ∈ (0,1), all c1,c2 ∈ N and d¯≥ 1, there exist ρ = ρ(ǫ,c1), η = η(γ,ǫ,c1) and n0 such that for every n ≥ n0 and every degree sequence D = (d1,... ,dn) with average degree at most d¯ that satisﬁes A1(η,c2), then for


pcrit := pcrit(c2,D) = min i∈V \W(c2)

di i∈V \W(c2) di(di − 1)

![image 8](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile8.png>)

- (6) ,1


di ≤

![image 9](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile9.png>)

i∈W(c,D)

we have

- (i) if 0 ≤ p ≤ (1 − ǫ)pcrit, then P[L1(GDp ) > γn] = o(1) ;
- (ii) if D satisﬁes A2(ǫ,c1,c2) and (1 + ǫ)pcrit ≤ p ≤ 1, then


P[L1(GDp ) > ρn] = 1 − o(1) .

In order to obtain a meaningful statement we need to apply Theorem 2 as follows: ﬁrst, choose ε (width of the transition window) and c1,c2,d¯. This ﬁxes the value of pcrit and ρ. Now, choose γ which might be arbitrarily smaller than ρ. This ﬁxes η and n0. After these choices, the theorem then gives a suﬃcient criterion for degree sequences whose size of the largest component jumps from at most γn to at least ρn in a window of width 2ε around pcrit.

Interestingly, this theorem gives a criterion for the existence of “sudden” jumps in L1(GDp ) that do not necessarily correspond to the phase transition of the appearance of a linear order component. In particular, it applies to cases where the degree sequence is not uniformly integrable. In Section 1.3 we will see an example of this behaviour.

The other part of the dichotomy settles the case of robust degree sequences.

- Theorem 3. For all p,δ ∈ (0,1) and all d¯ ≥ 1, there exist K,c0 ∈ N such that for every c ≥ c0, there exist ρ > 0 and n0 ∈ N such that for every n ≥ n0 and every degree sequence D = (d1,... ,dn) with average degree at most d¯ that does not satisfy A1(K,c) or A2(K,0,c), then


P[L1(GDp ) > ρn] ≥ 1 − δ .

As deﬁned in (6), we have pcrit > 0 (assuming that 0/0 = 1). Intuitively speaking, Theorem 3 classiﬁes the degree sequences that have a “critical percolation threshold” at p = 0. It is also worth noticing that if p = p(n) → 0 and d¯= O(1), then L1(GDp ) is at most the number of edges in GDp , which is O(pdn¯ ) = o(n) with probability 1 − o(1).

Theorems 2 and 3 show that the existence of a critical p for the emergence of a giant component is determined by the shape of the degree sequence for degrees that are bounded by a constant as well as by the degree sum of vertices of larger degree. For example, whether a degree sequence contains one vertex of degree n/2 or n/(2log n) vertices of degree log n does not make any diﬀerence.

- 1.1. Approach to the proof of Theorems 2 and 3. Previous work on bond percolation in GD

relies on the study of the conﬁguration model. Given D = (d1,... ,dn), let GˆD denote the random (multi)graph obtained using the conﬁguration model (see e.g. [27]). The ﬁrst author observed

that the percolated random graph GˆDp has the same distribution as GˆDp where Dp = (dp1,... ,dpn) is the random sequence obtained by choosing dpi distributed as a binomial random variable with parameters di and p, conditional on Σi∈[n]dpi being even (see Lemma 3.1 in [10]). Loosely speaking, this result states that one could interchange the two random processes, percolating ﬁrst the degree sequence conditional on its sum being even) and then choosing a random graph with the percolated degree sequence. Using this observation one can transfer results for the conﬁguration model to its percolated instances [8, 10, 13]. These results can be transferred to the simple random graph GDp provided D satisﬁes certain technical conditions (see Section 1.2).

Joos et al. [15] established a criterion for the existence of a linear order component for any degree sequence. Following the previous observation of interchanging the two random processes, one could hope that the largest component of GDp could be studied directly, applying this criterion. However, the following example discusses a degree sequence for which the random graphs GDp and GDp are drastically diﬀerent.

- Example 1. Consider the degree sequence Dn = (n/4,n/4,1,1... ,1) and let p = 1/2. By standard concentration inequalities, with high probability, the degree sequence Dp satisﬁes dp1,dp2 = (1 + o(1))n/8 and Σi∈[n]dpi = (1 + o(1))3n/4. The sequence Dp, if feasible, it is highly likely to satisfy v1v2 ∈ E(GDp) (this can be shown by an easy switching argument; see Section 3.1). However, by deﬁnition, the probability that v1v2 ∈ E(GDp ) is at most 1/2. As all vertices diﬀerent from v1 and v2 have degree one, the order of the largest component will strongly depend on the existence of the edge v1v2. So the component structure of GDp and GDp is diﬀerent.


- 1.2. Comparison of Theorem 1 to previous results. The strongest statements in our paper are Theorems 2 and 3. However, as previous results deal with sequences of degree sequences D = (Dn)n≥2, it is more convenient to compare them to Theorem 1. Additionally, we will assume that Dn converges in distribution to the random variable D, denoted by Dn → D, where D has ﬁnite and positive mean E[D]; that is, there exists a probability distribution (rk)k≥0 such that for every k ∈ N


{i ∈ [n] : d(in) = k} n

lim

- (7) = rk .


![image 10](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile10.png>)

n→∞

and E[D] = k≥0 krk ∈ (0,∞). Observe that (7) implies that d(D) exists.

Note that Theorem 1 only requires the existence of d. This is a slightly weaker condition than the convergence of Dn in distribution, but it is similar in spirit.

In this context, consider the following condition on the convergence of means lim

- (8) E[Dn] = E[D] .

Condition (8) can be easily replaced by the slightly weaker condition that D is uniformly integrable (see e.g. Remark 2.2 in [14]). Moreover, given that Dn → D, the condition that Dn is (strongly) uniformly integrable as in (1) (and (2)) is equivalent to D being (strongly) uniformly integrable.

Additionally, we say that the sequence (Dn)n≥2 has bounded second moment if

- (9) E[Dn2] = O(1) . Under the assumption Dn → D, we have following implications:


n→∞

d(D) < ∞ ⇐ Bounded second moment ⇒ (Strong) uniform integrability All the implications are straightforward to check, so we omit their proofs.

We now state the two central results from the literature on bond percolation.

- Theorem 4 (Proposition 3.1 in [13]). Suppose D = (Dn)n≥2 is a sequence of degree sequences such that Dn → D and (Dn)n≥2 has bounded second moment. If p > 1/d(D), there exists ξ > 0 such that

L1(GDp n) n

![image 11](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile11.png>)

→p ξ , and if p < 1/d(D), then

L1(GDp n) n

![image 12](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile12.png>)

→p 0 .

Now, let ρ(D) be the survival probability of a Galton-Watson tree with oﬀspring distribution given by D. Let Dp be the p-thinned version of D, deﬁned by

P[Dp = i] =

j≥i

P[D = j]

j i

pi(1 − p)j−i .

- Theorem 5 (Theorem 22 in [8]). Suppose D = (Dn)n≥2 is a sequence of degree sequences such that Dn → D and (Dn)n≥2 is uniformly integrable. Then for every p ∈ (0,1)


L1(GDp n) n

→p ρ(Dp) .

![image 13](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile13.png>)

The aim of this paper is to obtain results on the existence of a linear order component in GDp that are as widely applicable as possible, even if some precision is lost due to their generality. While Theorems 4 and 5 are more precise in their conclusions, they require conditions on D (bounded second moment and uniform integrability, respectively) that are not necessary in Theorem 1. For instance, the results in Theorem 1 (ii) when D is not uniformly integrable are not implied by any of the previous results in the literature. As we will show in the next sub-section, the case of non-uniformly integrable sequences is particularly interesting, and one cannot hope for very strong results in this setting. In conclusion, Theorem 1 and the previous results complement each other, and their use is a compromise between precision and generality.

- 1.3. Non-uniformly integrable sequences. Roughly speaking, a degree sequence is not uniformly integrable if the vertices of unbounded degree have non-negligible contribution to the average degree. Here, we include two illustrative examples.


- Example 2. The order of the largest component may not be concentrated. Consider again the degree sequence Dn = (n/4,n/4,1,1... ,1) given in Example 1 and let p ∈ (0,1). Using switchings, one can show that v1v2 ∈ E(GDn) with probability 1 − o(1). Hence, for any ﬁxed p ∈ (0,1) the probability that v1v2 ∈ E(GDp n) is (1 −o(1))p, bounded away from 0 and 1. If v1,v2


are adjacent in GDp n, the order of the largest component will be distributed as Bin(n/2 − 2,p); otherwise, it will be distributed as the maximum over two independent copies of Bin(n/4,p).

This example can be generalised to produce degree sequences Dn satisfying the following: for every ρ > 0, there exists δ > 0 such that

- (10) P[L1(GDp n) < ρn] > δ P[L1(GDp n) > (1 − ρ)n] > δ .


Thus, one cannot expect that n−1L1(GDp n) converges in probability to a constant as in Theorems 4 and 5. Moreover, (10) shows that the statement of Theorem 1 (ii) cannot hold with probability 1 − o(1).

- Example 3. As mentioned above, Theorem 2 can be used to detect sudden changes of the order of the largest component that do not coincide with the birth of the giant component. Consider the following degree sequence Dn = (ξn,3,3,... ,3), for some ξ > 0. Theorem 3 shows that the size of the largest component of GDp n is linear for every p > 0, in fact, it stochastically dominates a Bin(ξn,p). However, we can also apply Theorem 2 with pcrit = 1/2.In particular, given ε,γ,ρ, we can choose ξ suﬃciently small so Theorem 2 gives a jump in L1(GDp n) from at most γn to at least ρn in a window of width 2ε around pcrit. Hence the birth of the giant component is at p = 0 (by Theorem 3) and there is a boost at p = 1/2 (by Theorem 2).


Intuitively, if a sequence is not uniformly integrable, then it has linearly many edges in vertices of unbounded degree. Under some weak conditions, these vertices will typically form a connected core, even after percolation. This core contains linearly many edges and it typically creates a linear order component. However, if pcrit > 0, then for p > pcrit, the vertices of bounded degree will percolate even without the help of unbounded degree vertices, and thus, the growth of the giant component changes at pcrit. To our knowledge, this critical point has not been studied in the literature. It would be interesting to get a better understanding of the size of the largest component around this point.

Structure of the paper: The paper is structured as follows. In Section 2, we provide the basic notation and some technical estimates that will be used throughout the proof. Section 3 presents the main combinatorial tool we will use, the switching method, and provides an overview of the proof of Theorem 2 and 3. In Section 4, we present three important technical propositions. Assuming them, in Section 5 and 6 we prove Theorem 2 and 3, respectively. In Section 7, 8 and 9 we prove these three propositions. Section 10 is devoted to the proof of Theorem 1. We provide an application of the results obtained to power-law degree sequences in Section 11. Finally, in Section 12, we state some remarks of our results and discuss a number of open questions.

2. Notation and some probabilistic tools

We consider labelled graphs G with vertex set V = V (G) = [n] := {1,... ,n} and edge set E(G). If we refer to a graph or degree sequence on the set V , we always implicitly assume that V = [n] and thus |V | = n. We say that a graph G on V has degree sequence D = (d1,... ,dn) if for every i ∈ [n], the degree of i is di. We let ΣD denote the sum of these degrees; that is, ΣD := ni=1 di. We denote by |D| the length of the degree sequence.

For an arbitrary vertex v ∈ V , we will often write d(v) = dG(v) for its degree. Let H be a subgraph of G; if v ∈ V (H), then dH(v) denotes the degree of v in H; if v ∈ V \ V (H), then dH(v) = 0. For a graph G, a subset of vertices U ⊆ V and v ∈ V , we occasionally use the notation dG(v,U) to denote the number of neighbours of v in G that are in the subset U. Given a degree sequence D and a graph G, we denote by ∆(D) (and δ(D)) and by ∆(G) (and δ(G)) the maximum (and minimum) degree of the sequence D and of the graph G, respectively.

We denote by N(v) = NG(v) the set of neighbours of v in G. For S ⊆ V , we use N(S) = NG(S) for the set of vertices in V \ S that have a neighbour in S. We also use N[S] = NG[S] for the set of vertices that are either in S or in N(S). For S ⊆ V , we denote by G[S] the (sub)graph of G induced by S. For disjoint S,T ⊆ V , we denote by G[S,T] the bipartite graph induced between S and T.

We will make use of some classical concentration inequalities that can be found in [20].

- Lemma 6 (Chernoﬀ’s inequality). Let X1,... ,XN be a set of independent Bernoulli random variables with expected value p and let X = Ni=1 Xi. Then, for every 0 < t < Np

P[|X − E[X]| > t] ≤ 2e−

t2

![image 14](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile14.png>)

3Np .

- Lemma 7 (McDiarmid’s inequality). Let X1,... ,Xs be a set of independent random variables taking values in [0,1]. Let f : [0,1]s → R be a function of X1,... ,Xs that satisﬁes for every 1 ≤ i ≤ s, every x1,... ,xs ∈ [0,1] and every x′i ∈ [0,1],


|f(x1,... ,xi,... ,xs) − f(x1,... ,x′i,... ,xs)| ≤ ci , for some ci > 0. Then, for every t > 0

− s2t2 i=1

![image 15](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile15.png>)

c2

P[|f(X1,... ,Xs) − E[f(X1,... ,Xs)]| > t] ≤ 2e

i .

Many of our results have complicated hierarchies of constants. To be precise, if we say that a statement holds whenever a ≪ b ≪ c ≤ 1, then this means that there are non-decreasing functions f,g : (0,1] → (0,1] such that the result holds for all 0 < a,b,c ≤ 1 with a ≤ f(b) and b ≤ g(c). In particular, such hierarchies need to be read from right to left. We will not calculate these functions explicitly in order to simplify the presentation, but one could easily calculate them from inspecting our proofs. Hierarchies with more terms are deﬁned in a similar way. Finally, we write x = a ± b to denote that x ∈ [a − b,a + b], for real numbers x,a,b.

3. Overview of the proofs

In this section we present an overview of the proofs of Theorems 2 and 3 as well as of the main method used in them.

- 3.1. The switching method. Let GD be the set of simple graphs with degree sequence D. Throughout our proofs we want to consider the probability that GD, a uniformly chosen element of GD, satisﬁes a certain property. We will slightly abuse notation by indistinctly referring to GD as a set of graphs and as a probability space equipped with the uniform distribution. Similarly, we will consider F ⊆ GD and talk about the probability of F, thought as an event in the probability space GD.


The main combinatorial tool that we use to estimate diﬀerent probabilities in GD is the switching method. Given a graph G with degree sequence D and two ordered edges uv,xy ∈ E(G) we can perform the following graph operation, called a {uv,xy}-switch, or simply a switch: obtain G′ by deleting the edges uv and xy from G and adding the edges ux and vy in G. Observe that the {uv,xy}-switch is diﬀerent from the {vu,xy}-switch, but equal to the {vu,yx}-switch. If either ux or vy are edges of G, the graph G′ will have multiple edges, and if either u = x or v = y, the graph G′ will have loops. Since we restrict here to simple graphs, we say that a switch is valid if none of these occur.

The basic idea of the switching method is the following. In order to determine the probability of F ⊆ GD in terms of the probability of F′ ⊆ GD, we use the average number of valid switches between a graph in F and a graph in F′, denoted by d(F → F′), and vice versa. A simple double-counting of such switches gives

d(F′ → F)

- (11) d(F → F′) · P[F′] .


P[F] =

![image 16](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile16.png>)

Although this relation is very simple, the switching method is very powerful. In particular, we avoid the use of the conﬁguration model and all the technicalities that come with it.

- 3.2. The emergence of the giant component. In [15], a characterisation is given of those degree sequences D for which the random graph GD has a giant component with high probability. Let jD be the smallest j ∈ N such that


j

di(di − 2) > 0

i=1

if such j exists and else jD = n. Also, they set RD := ni=jD di and MD := i:d

i =2 di. Eﬀectively, GD has a giant component with high probability if and only if RD grows linearly in MD.

As we deal with bond percolation on GDp , we need to consider generalizations of these quantities.

- (i) Let jpD be the minimum between n and the smallest natural number j such that j

i=1

di(p(di − 1) − 1) > 0 .

- (ii) Let RpD := ni=jD


(p(di − 1) − 1). Observe that if ni=1 di(p(di − 1) − 1) ≤ 0, we have RpD = p(dn − 1) − 1. Note that in the case p = 1, the deﬁnition of jpD coincides with the deﬁnition of jD. Moreover,

p

R1D ≤ RD ≤ 3R1D. In our setting we do not need to deﬁne an analogue of MD since vertices of degree 2 play no special role here (see Section 12 for a detailed discussion). Also note that vertices

of degree 0 have no contribution to these parameters. So, it is useful to assume, and we will do so if not stated otherwise, that di ≥ 1 for every i ∈ [n]. The result for degree sequences containing vertices of degree 0 can be easily deduced from the analysis of degree sequences without them.

Theorem 2 and 3 essentially distinguish between two cases on the tail of the degree sequence. In Theorem 2, we show that a critical percolation threshold pcrit exists if the two conditions A1(·,c1,c2) and A2(·,c2) hold. These conditions bound the number of edges incident to vertices of large degree. One should note that the two conditions are only required for particular values of the degrees, namely c1 and c2, and thus, they are much weaker than a domination condition on the whole tail of the degree sequence. The heart of the proof of Theorem 2 is the analysis of an exploration process, in which we reveal the components of GDp by exposing the neighbours of each vertex sequentially (cf. Proposition 9). To avoid technical diﬃculties that arise due to high degree vertices, we include them together with their neighbours in the initial set of explored vertices. So during the process, we only reveal the connections of vertices of low or moderatelygrowing degree. Let S denote the set of high degree vertices (we will specify the exact magnitude during the proof). We show that if v ∈N[S] d(v)(p(d(v)−1)−1) is negative and actually decays linearly with n, then the exploration process is subcritical in the sense that all components it reveals are sub-linear. If v ∈N[S] d(v)(p(d(v)−1)−1) is positive and grows linearly, then one can use condition A2 to ensure that RpD grows linearly. In that case, it turns out that the exploration process will reveal a component of linear order with high probability. In Sections 5 and 6, we show how these two conditions give a critical value pcrit such that when p goes from less than (1−ǫ)pcrit, to at least (1+ǫ)pcrit, the fraction of vertices in the largest component undergoes an abrupt increase.

Regarding Theorem 3, recall that its premises cover degree sequences that have a quite heavy tail, that is, either Condition A1 or Condition A2 fails. Here, we distinguish between two subcases. The ﬁrst is that a set S1 of very high (growing) degree vertices have linear total degree. The boundedness of the average degree implies that S1 is small (of sub-linear size). Moreover, we show that with high probability GDp [S1] is connected and that more than half of the edges incident to S1 in GD, have their other endpoint in V \S1. Deleting each such edge with probability that is bounded away from 0 leaves with high probability a giant component. This is stated in Proposition 10. Now, if S1 does not have linear total degree, then we show that its removal leaves a degree sequence D′ that is super-critical: the quantity RpD′ grows linearly in n. One can then apply again Proposition 9 to ﬁnd a giant component, concluding the proof of Theorem 3.

The transition from RpD to RpD′ requires a result (Proposition 8) which shows that if RpD grows linearly in n and we remove a set of vertices of small total degree, then the resulting degree sequence D′ is such that RpD′ still grows linearly, albeit with a smaller coeﬃcient.

Finally, the proof of Theorem 1 is a relatively straightforward application of both Theorem 2 and 3 and it is proved in Section 10.

4. Three technical propositions

In this section we introduce three important propositions that will allow us to prove Theorem 2 and 3. We defer their proofs to Sections 7, 8 and 9, respectively.

The ﬁrst one is a deterministic proposition which proves the following. Suppose G is a graph with degree sequence D and S ⊆ V (G) such that u∈S d(u) is small. Suppose D′ is a possible degree sequence of the graph G − S, then RpD′ is bounded from below by RpD/50.

- Proposition 8. Suppose 1/n ≪ ν, 400ν ≤ µ ≤ 1, and p ∈ (0,1]. Suppose D is a degree sequence

on V with RpD ≥ µn and let S ⊆ V be such that v∈S d(v) ≤ νn. Assume that G′ is a graph obtained from a graph G with degree sequence D by deleting all vertices in S and afterwards by

deleting all vertices of degree 0. Let D′ be the degree sequence of G′ and assume it has length n′. Then n′ ≥ (1 − 2ν)n and RpD′ ≥ 50µ n′.

![image 17](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile17.png>)

Moreover, if G = GD and D′ is the degree sequence of G′, then G′ is a uniformly random graph with degree sequence D′, that is G′ = GD′.

The key ingredient for the proof of both Theorem 2 and 3 is the following proposition that gives us the component structure of GDp . This proposition can be viewed as the extension of the main theorem in [15]. It states that if the drift on the bulk of the vertices (that is, excluding vertices of very high degree and their neighbours) is negative, then the fraction of vertices in the largest component is a.a.s. bounded by some small constant. On the other hand, if ∆(D) ≤ n1/4 and RpD ≥ µn, then we have a.a.s. a component containing a constant fraction of all vertices.

- Proposition 9. Suppose n ∈ N and 1/n ≪ α ≪ γ ≪ µ,1/d,p¯ ≤ 1. Let D be a degree sequence on V with ΣD ≤ dn¯ .

- (i) If there exists a set S ⊆ V such that d(v) ≤ n1/4 for every v ∈/ S, and for every graph G

with degree sequence D one has u∈N

G[S] d(u) ≤ αn, and u∈V\N

G[S] d(u)(p(d(u)−1)−

1) ≤ −µn, then

P[L1(GDp ) ≤ γn] = 1 − o(1) .

- (ii) If ∆(D) ≤ n1/4 and RpD ≥ µn, then


P[L1(GDp ) ≥ γn] = 1 − o(1) .

Our last result is a version of Theorem 3 for degree sequences that have many edges incident to vertices of unbounded degree. Recall that for c ∈ N, W(c,D) denotes the set of vertices of degree at least c.

- Proposition 10. For all p,δ,ǫ ∈ (0,1) and all d¯ ≥ 1, there exist γ > 0,n0 ≥ 1 such that for every n ≥ n0 and every degree sequence D on V with ΣD ≤ dn¯ that satisﬁes


di ≥ ǫn ,

i∈W(log2 n,D)

we have

P[L1(GDp ) > γn] ≥ 1 − δ .

In the next two sections we proceed with the proof of Theorem 2 and 3 assuming these three propositions.

5. Degree sequences with thin tails: proof of Theorem 2

- Proof of Theorem 2. Let D be a degree sequence on V . Recall that W(c,D) = {i ∈ V : di ≥ c}; for convenience, we denote W(c) := W(c,D). We assume that η is small enough with respect to ǫ,γ,1/c1 so that the inequalities in this proof hold. Next, let pcrit := pcrit(c2,D) be as in (6). Note that the deﬁnition of pcrit excludes the contribution of all the vertices of degree at least c2. Moreover, with this deﬁnition we have


- (12) di(pcrit(di − 1) − 1) ≤ 0

and equality holds if pcrit < 1.

We ﬁrst prove Theorem 2 (i). Suppose that p ≤ (1 − ǫ)pcrit. Our strategy is to apply Proposition 9 (i) with W(c2), 2η and ǫ/3 playing the role of S, α and µ, respectively. In order to do so, we need to give an upper bound on i∈N[W(c

2)] di and on i∈V\N[W(c

2)] di(p(di − 1) − 1) for every graph G with degree sequence D.

By assumption, A1(η,c2) holds; that is,

- (13) |N(W(c2))| ≤ i∈W(c2)

di ≤

η c2 · n,

![image 18](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile18.png>)

and therefore

i∈N[W(c2)]

di ≤

i∈W(c2)

di +

i∈N(W(c2))

di ≤

η c2 · n + c2|N(W(c2))| ≤ (1 + c2)

![image 19](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile19.png>)

η

![image 20](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile20.png>)

- (14) c2 · n ≤ 2ηn .

We next bound i∈V \N[W(c

2)] di(p(di − 1) − 1) from above. Since di(p(di − 1) − 1) ≥ −di for every i ∈ V , we obtain

i∈V \N[W(c2)]

di(p(di − 1) − 1) =

i∈V \W(c2)

di(p(di − 1) − 1) −

i∈N(W(c2))

di(p(di − 1) − 1)

≤

i∈V \W(c2)

di(p(di − 1) − 1) + c2|N(W(c2))|

(13) ≤

i∈V \W(c2)

- (15) di(p(di − 1) − 1) + ηn .

It follows that

i∈V \W(c2)

di(p(di − 1) − 1) ≤ (1 − ǫ)

i∈V \W(c2)

di(pcrit(di − 1) − 1) − ǫ

i∈V \W(c2)

di

(12) ≤ −ǫ

i∈V \W(c2)

di .

Using that di ≥ 1, we obtain

- (16) i∈V \W(c2)

di =

i∈V

di −

i∈W(c2)

di ≥ n −

i∈W(c2)

di

(13) ≥

n 2

![image 21](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile21.png>)

.

Therefore,

i∈V \W(c2)

di(p(di − 1) − 1) ≤ −

ǫ 2 · n.

![image 22](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile22.png>)

Using (15), it follows that

i∈V \N[W(c2)]

di(p(di − 1) − 1) ≤ −

ǫ 2 · n + ηn ≤ −

![image 23](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile23.png>)

ǫ

![image 24](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile24.png>)

- (17) 3 · n As (14) and (17) hold, Proposition 9 (i) completes the proof of Theorem 2 (i).


i∈V \W(c2)

We proceed with the proof of Theorem 2 (ii). Suppose now that p ≥ (1+ǫ)pcrit. Here we may assume that pcrit < 1 as otherwise p > 1 does not satisfy the assumption of part (ii). We will ﬁrst show that there exists µ = µ(ǫ,d,c¯ 1) such that RpD ≥ µn.

For k ∈ {1,2}, we deﬁne jk := min{n + 1,i ∈ [n] : di ≥ ck}. Since pcrit < 1, (12) holds with equality. Using the deﬁnition of jpD, we obtain

j2−1

di(p(di − 1) − 1) =

i=jpD

j2−1

di(p(di − 1) − 1) −

i=1

jpD−1

di(p(di − 1) − 1)

i=1

j2−1

di(p(di − 1) − 1)

≥

i=1

j2−1

j2−1

di(pcrit(di − 1) − 1) + ǫ

≥ (1 + ǫ)

di

i=1

i=1

j2−1

(16)

ǫ

(12)= 0 + ǫ

≥

- (18) 2 · n .


di

![image 25](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile25.png>)

i=1

It follows from A2(ǫ,c1,c2) that

j1−1

(18) ≥

di(p(di − 1) − 1)

![image 26](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile26.png>)

i=jpD

ǫ 2 · n −

j2−1

ǫ 2 · n −

di(p(di − 1) − 1) ≥

![image 27](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile27.png>)

i=j1

j2−1

ǫ 4 · n.

d2i ≥

![image 28](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile28.png>)

i=j1

We conclude that

n

RpD =

(p(di − 1) − 1) ≥

i=jpD

j1−1

1 c1

(p(di − 1) − 1) ≥

![image 29](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile29.png>)

i=jpD

j1−1

ǫ 4c1 · n =: µn.

di(p(di − 1) − 1) ≥

![image 30](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile30.png>)

i=jpD

2) di ≤ cη

· n ≤ ηn. Since we can choose η small enough in terms of µ, we can apply Proposition 8 with η and W(c2) playing the role of ν and S. Let D′ be the random degree sequence of the subgraph GD[V \ W(c2)]. Let D0 be the set of degree sequences D0 that satisfy P[D′ = D0] > 0. By Proposition 8, we deduce that if D0 ∈ D0, then RpD0 ≥ µn/50 and |D0| ≥ n2. Moreover, conditional on D′ = D0, we have that GD[V \W(c2)] and GD0 have the same probability distribution. Now we select ρ such that η ≪ ρ ≪ µ,1/d,p¯ . We can apply Proposition 9 (ii) to the degree sequence D0 with 2ρ playing the role of γ, from which Theorem 2 (ii) follows:

Recall that, by assumption, we have i∈W(c

![image 31](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile31.png>)

2

![image 32](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile32.png>)

P[L1(GDp ) > ρn] ≥ P[L1(GDp [V \ W(c2)]) > ρn] ≥ min

P[L1(GDp 0)) > 2ρ|D0|]

D0∈D0

= 1 − o(1) .

6. Robust degree sequences: proof of Theorem 3

- Proof of Theorem 3. Let c0 and K be such that 1/c0 ≪ 1/K ≪ δ,p,ǫ,1/d¯. For any given c ≥ c0, assume that n0 is such that 1/n0 ≪ 1/c. Let n ≥ n0.


Suppose ﬁrst that i∈W(log2 n) di ≥ Kn/c3. We apply Proposition 10 with K/c3 playing the role of ǫ and obtain a γ1 such that P[L1(GDp ) > γ1n] ≥ 1 − δ.

Hence we may assume that i∈W(log2 n) di ≤ Kn/c3. Let S := W(log2 n). We will show that the (random) subgraph GDp [V \ S] has a giant component, and thus also GDp has a giant component. Let us ﬁrst show that RpD ≥ 16Kpc · n. We consider two cases:

![image 33](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile33.png>)

- Case 1: A1 (K,c) does not hold; that is, i∈W(c) di ≥ Kn/c.


We deﬁne j1 := min{j ∈ [n] : dj ≥ c} and let j2 be the smallest integer j such that ji=j

di ≥ Kn/(2c). Since A1 (K,c) does not hold, j1 and j2 are well-deﬁned. We have

1

j2

di(p(di − 1) − 1) = p

i=1

j2

≥ cp

d2i − (1 + p)

i=1

j2

di − 2dn¯ ≥

i=j1

j2

j2

d2i − (1 + p)dn¯

di ≥ p

i=j1

i=1

Kp 2 − 2d¯ n .

![image 34](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile34.png>)

Therefore, jpD ≤ j2. Since 1/dj2 ≤ 1/c ≤ 1/c0 ≪ p, we conclude that p(dj − 1) − 1 ≥ pdj/4 for all j ≥ j2. By the deﬁnition of j2 and using A1(K,c) (in fact, its negation), it follows that

di

 

j2−1

n

n

p 4

p 4

Kp 16c · n .

RpD ≥

(p(di − 1) − 1) ≥

di ≥

 ≥

di −

![image 35](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile35.png>)

![image 36](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile36.png>)

![image 37](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile37.png>)

i=j2

i=j1

i=j2

i∈W(c)

- Case 2: A2 (K,0,c) does not hold; that is, i∈V\W(c) d2i ≥ Kn/4.


Now let j3 be the smallest integer j such that ji=1 d2i ≥ Kn/8. Since A2 (K,0,c) does not hold, j3 is well-deﬁned and dj3 < c. Using the deﬁnition of jpD, similarly as before

j3

dj(p(dj − 1) − 1) ≥

j=jpD

j3

dj(p(dj − 1) − 1)

j=1

j3

d2j − (1 + p)dn¯

≥ p

j=1

Kp 8 − 2d¯ n >

Kp

≥

16 · n . Thus

![image 38](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile38.png>)

![image 39](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile39.png>)

j3

j3

Kp 16c · n .

1 c

RpD ≥

dj(p(dj − 1) − 1) ≥

(p(dj − 1) − 1) >

![image 40](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile40.png>)

![image 41](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile41.png>)

j=jpD

j=jpD

Let D′ be the random degree sequence of the subgraph GD[V \ S]. Let D0 be the set of degree sequences D0 that satisfy P[D′ = D0] > 0. By Proposition 8 applied to S with K/c3 and Kpn/(16c) playing the role of ν and µ (note that 400ν ≤ µ), we obtain that, for every

D0 ∈ D0, one has RpD0 ≥ Kpn/(800c) and |D0| ≥ n2. Moreover, conditional on D′ = D0, we have that GD[V \ S] and GD0 have the same probability distribution. Using that for every D0 ∈ D0, ∆(D0) ≤ log2 n and RpD0 ≥ Kpn/(800c), we can apply Proposition 9 (ii) and obtain γ2 > 0 such that

![image 42](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile42.png>)

P[L1(GDp ) > γ2n] ≥ P[L1(GDp [V \ S]) > γ2n] ≥ min

P[L1(GDp 0)) > 2γ2|D0|] ≥ 1 − o(1) .

D0∈D0

We conclude the proof of the theorem by setting γ := min{γ1,γ2}.

7. Proof of Proposition 8

Although the statement of Proposition 8 may sound very natural and also easy to prove, the fact that some edge deletions may cause signiﬁcant reordering in ordered degree sequences makes the proof technical and complex.

Proof of Proposition 8. We start with the last part of the proposition. By exposing D′, we only ﬁx the degree of each vertex in V \ S towards S. Take any realisation G′ of a graph on V \ S with degree sequence D′. The number of extensions of G′ to a graph on V with degree sequence

D is clearly independent from the structure of G′. That is, for any choice of G′ there is the same number of extensions, and the law of GD[V \ S] coincides with that of GD′.

It remains to prove the main part. For every k ∈ [n], let d′k be the degree of the vertex k in G′ and deﬁne rk := dk − d′k. Note that rk = dk for every k ∈ S whereby

rk ≤ 2νn .

k∈V

Clearly, by deleting at most k∈S dk ≤ νn edges, we have created at most 2νn vertices of degree 0, which we do not consider in D′. Let n′ be the number of vertices with positive degree after

the deletion of S. Thus n′ ≥ (1 − 2ν)n.

Note that the statement follows if ∆(G) ≥ µn/(40p), since then a vertex of maximum degree is not contained in S and has degree at least ∆(G) − νn in D′, whereby

µn′ 50

µ 50 · n ≥

RpD′ ≥ p((∆(G) − νn) − 1) − 1 ≥

, where we used that 400ν ≤ µ. Thus, we may now assume that ∆(G) < µn/(40p).

![image 43](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile43.png>)

![image 44](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile44.png>)

We deﬁne fk := p(dk − 1) − 1 and fk′ := p(d′k − 1) − 1 for all i ∈ [n]. Recall that d1 ≤ ··· ≤ dn and that jpD is the smallest integer j such that

- j
- k=1


dk(p(dk − 1) − 1) =

- j
- k=1


dkfk > 0 .

Let A := {k ∈ [n] : k < jpD} and B := [n] \ A. Observe that the fks are increasing with respect to k, and thus k ∈ B implies fk > 0. Let σ be a permutation such that d′σ1 ≤ ... ≤ d′σn where we set d′k := 0 if vertex k is deleted. Note that d′kfk′ = 0 if d′k = 0. Thus RpD′ does not change if we add isolated vertices to D′. For the sake of simplicity, we consider D′ to be a degree sequence on [n] with isolated vertices. Let A′ := {k ∈ [n]: σk < jDp ′} and B′ := [n] \ A′.

Let T := {k ∈ B : fk′ ≥ fk/2}. Observe that if we delete an edge ij from G, then fi and fj decrease by p, respectively. Thus

(fk − fk′) = 2p

fk ≤ 2

rk ≤ 4pνn.

k∈B\T

k∈B\T

k∈B\T

Hence

- 4µ

![image 45](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile45.png>)

- 5


fk = RpD −

fk ≥ µn − 4pνn ≥

- (19) n .

Suppose k ∈ T. Then,

d′k =

1 + fk′ p

![image 46](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile46.png>)

+ 1 ≥

1 + fk/2 p

![image 47](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile47.png>)

+ 1 =

1 + fk 2p

![image 48](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile48.png>)

+

- 1

![image 49](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile49.png>)

- 2p


+ 1 =

dk 2

![image 50](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile50.png>)

+

- 1

![image 51](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile51.png>)

- 2p


+

- 1

![image 52](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile52.png>)

- 2 ≥


dk 2

![image 53](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile53.png>)

.

We deﬁne c := djD

p

. It follows that,

k∈T

d′kfk′ ≥

1 4 k∈T

![image 54](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile54.png>)

dkfk ≥

c 4 k∈T

![image 55](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile55.png>)

fk

(19) ≥

cµ 5

![image 56](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile56.png>)

- (20) n .

- Let T1 ⊆ T be such that


k∈T1

d′kfk′ >

cµ 20

![image 57](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile57.png>)

- (21) n ,


k∈T

k∈B\T

- and max{σk : k ∈ T1} is minimized (choose the set of consecutive vertices in T smallest with respect to the order σ1,... ,σn). By (21) such a set exists. Let kmax = arg max{σk : k ∈ T1}. So the above deﬁnition implies that


cµ 20

d′kfk′ ≤

n .

![image 58](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile58.png>)

k∈T1\{kmax}

≤ p∆(G) ≤ µn/40 and that d′k ≥ dk/2 ≥ c/2 for each k ∈ T1 (whereby

Observe also that fk′

max

2 cd′k ≥ 1). We conclude that

![image 59](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile59.png>)

fk′ =

fk′ − fk′max

fk′ −

k∈T

k∈T\T1

k∈T1\{kmax}

- 1

![image 60](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile60.png>)

- 2 k∈T


2 c

d′kfk′ − fk′max

≥

fk −

![image 61](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile61.png>)

k∈T1\{kmax}

(19)

µ 10

µ 40

µ 4

2µ 5

n −

n −

n ≥

≥

- (22) n .

Let B1 := {k ∈ B : fk′ < 0} and note that B1 ⊆ B \ T and B1 ⊆ A′. Recall that d′k = dk −rk and that fk′ = fk −prk. By the deﬁnition of A and c, we observe that k∈A dkfk ≥ −c(p(c − 1) − 1). Thus

k∈A

d′kfk′ ≥

k∈A

dkfk −

k∈A

rk(fk + pdk)

≥ −c(p(c − 1) − 1) −

k∈A

rk(p(2c − 1) − 1)

≥ −pc2 − 4cpνn . If k ∈ B1, then fk > 0 and from fk′ < 0, we obtain dk < 1/p + rk + 1. Thus

k∈B1

d′kfk′ =

k∈B1

((dk − rk)fk − prk(dk − rk))

≥ −

k∈B1

prk(dk − rk)

> −

k∈B1

rk(1 + p) ≥ −2(1 + p)νn ≥ −4cpνn ,

where we used that 1/c ≤ p in the last line. Since A and B1 are disjoint, we deduce that

k∈A∪B1

d′kfk′ ≥ −pc2 − 8cνpn .

- Let T2 ⊆ T be such that


k∈T2

d′kfk′ > pc2 + 8cνpn ,

- and max{σk : k ∈ T2} is minimized (choose the set of consecutive vertices in T smallest with respect to the order σ1,... ,σn). As ∆(G) ≤ µn/(40p), we conclude that pc2 ≤ cµn/40. Since 8cνpn ≤ cµn/40 by hypothesis, using (21) we conclude that T2 exists. Note also that T2 ⊆ T1. Therefore, by using (22), we obtain


k∈T\T2

fk′ ≥

µn 4

![image 62](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile62.png>)

- (23) .

Since A ∪ B1 and T2 are disjoint, we conclude that

k∈A∪B1∪T2

- (24) d′kfk′ > 0 .


![image 63](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile63.png>)

![image 64](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile64.png>)

![image 65](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile65.png>)

![image 66](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile66.png>)

The previous inequality suggests that the vertices in T \T2 might belong to B′ and thus contribute to RpD′. However, in the new ordering σ, there might be vertices in A with larger degree than some of the vertices in T \ T2. Let P := (T \ T2) ∩ A′. If k∈P fk′ ≤ µn8 , then (23) implies

![image 67](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile67.png>)

µn′ 8

µn 4 −

µn 8

µn 8 ≥

RpD′ ≥

fk′ ≥

=

,

![image 68](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile68.png>)

![image 69](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile69.png>)

![image 70](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile70.png>)

![image 71](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile71.png>)

k∈(T\T2)∩B′

and we are done.

Hence, we may assume k∈P fk′ > µn8 . Recall that, since P ⊆ T, we have d′k ≥ dk/2 ≥ c/2 for every k ∈ P and hence, by (24),

![image 72](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile72.png>)

cµn 16

d′kfk′ >

- (25) .

Thus a signiﬁcant amount of vertices in A ∪ B1 ∪ T2 ∪ P need to be in B′. Let Q := (A ∪ B1 ∪ T2 ∪ P) ∩ B′. Since fk′ < 0 only for k ∈ A ∪ B1, and fk′ > 0 all k ∈ B′, (25) implies

k∈Q

d′kfk′ >

cµn 16

![image 73](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile73.png>)

- (26) .


![image 74](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile74.png>)

k∈A∪B1∪T2∪P

Observe that B1 ∪ P ⊆ A′. By our choice of T2, the degree of a vertex in T2 in G′ is at most the degree of a vertex in P in G′; that is, vertices in T2 are smaller than vertices in P with respect to the ordering σ. Thus if a vertex of T2 is contained in Q, then P = ∅ and this a contradiction to our assumption. Therefore, Q = A ∩ B′ and hence d′k ≤ dk ≤ c for each k ∈ Q. Using (26) we obtain,

cµ 16

µ 16

1 c ·

1 c k∈Q

RpD′ ≥

d′kfk′ ≥

fk′ ≥

fk′ ≥

n ≥

n .

![image 75](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile75.png>)

![image 76](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile76.png>)

![image 77](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile77.png>)

![image 78](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile78.png>)

k∈B′

k∈Q

This completes the proof.

8. Proof of Proposition 9

Let GD be a graph chosen according to the uniform distribution on GD. The proof of Proposition 9 will consist of a careful analysis of an exploration of the diﬀerent components of GDp and will heavily rely on the switching method. Our proofs are similar in spirit to those in [15], but the additional level of randomness that is due to bond percolation makes the arguments more involved and additional arguments are needed.

In order to bound the number of switches it is more convenient to denote by d(u) the degree of a vertex u ∈ V , instead of using di for i ∈ V . We will use this notation in this and in the next section.

- 8.1. Connection probabilities via the switching method. The following three technical lemmas provide the necessary tools needed for proving that the random exploration process follows closely to what we expect it to do. To prove these lemmas we make extensive use of the switching method and, in particular, of inequality (11).


- Lemma 11. Suppose n ∈ N and 1/n ≪ 1 and let Z′ ⊆ V . Suppose H′ is a graph with vertex set Z′ and F′ is a bipartite graph with vertex partition (Z′,V \ Z′). Suppose u ∈ Z′ and v ∈ V \ Z′ such that uv ∈/ E(F′). Suppose D is a degree sequence on V such that


- (E1) d(u) ≤ n1/4,
- (E2) if w ∈ V and d(w) > n1/4, then w ∈ Z′ and d(w) = dH′(w), and
- (E3) w∈V\Z′(d(w) − dF′(w)) ≥ n/20.


Then,

P[uv ∈ E(GD) | GD[Z′] = H′, F′ ⊆ GD] ≤ 30n−1/2.

Proof. Let F+ be the set of graphs with degree sequence D such that G[Z′] = H′, F′ ⊆ G and uv ∈ E(G), and let F− be the set of graphs with degree sequence D such that G[Z′] = H′, F′ ⊆ G and uv ∈/ E(G). We will only perform switches that involve edges that are not contained in E(H′)∪E(F′). This ensures that the graph G0 obtained from a switch also satisﬁes G0[Z′] = H′ and F′ ⊆ G0. As this is the ﬁrst proof that involves the switching method, we will provide an extra level of detail.

For every G ∈ F+, let s+(G) be the number of switches that transform G into a graph in F−. We seek for a lower bound on s+(G). Indeed, we will ﬁnd many edges xy such that the {uv,xy}-switch leads to a graph in F−. For this, it suﬃces to select an edge xy such that xy is at distance at least 2 from uv, we have xy ∈/ E(F′), and x ∈ V \ Z′. By (E3), there are at

least n/20 edges that have one endpoint in V \ Z′ and are not contained in E(F′). Therefore, it suﬃces to count how many of them lie at distance at most 1 from uv. Note that d(u),d(v) ≤ n1/4. Moreover, v has no neighbour with degree larger than n1/4. While u can have neighbours w ∈ Z′ with degree larger than n1/4, all the edges incident to w have both endpoints in Z′ (by (E2)). It follows, that there are at most 2n1/2 edges at distance at most 1 from uv with at least one endpoint in V \ Z′. Note that for any such xy, the {uv,xy}-switch transforms G into a simple graph G0 with degree sequence D, G0[Z′] = H′, F′ ⊆ G0, and uv ∈/ E(G0). Therefore,

n 20 − 2n1/2 ≥

n 30

s+(G) ≥

.

![image 79](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile79.png>)

![image 80](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile80.png>)

For every G ∈ F−, let s−(G) be the number of switches that transform G into a graph in F+. We bound s−(G) from above. Clearly, any such switch is of the form {ux,vy} for some x,y ∈ V . Since d(u),d(v) ≤ n1/4, there are at most d(u)d(v) ≤ n1/2 choices for the edges ux and vy. Therefore,

s−(G) ≤ n1/2 . Using (11) we obtain

s−(G) s+(G) · P[uv ∈/ E(GD) | GD[Z′] = H′, F′ ⊆ GD]

P[uv ∈ E(GD) | GD[Z′] = H′, F′ ⊆ GD] ≤

![image 81](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile81.png>)

30n1/2

n · P[uv ∈/ E(GD) | GD[Z′] = H′, F′ ⊆ GD] ≤ 30n−1/2 .

≤

![image 82](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile82.png>)

For a graph G, a vertex v and set of vertices S in G, we write dG(v,S) for the number of neighbours of v in S.

- Lemma 12. Suppose n ∈ N and 1/n ≪ ν ≪ 1. Suppose Z′ ⊆ V . Suppose H′ is a graph with vertex set Z′, and F′ is a bipartite graph with vertex partition (Z′,V \ Z′). Suppose x ∈ V \ Z′ and z ∈ Z′. Suppose D is a degree sequence on V such that


- - if w ∈ V and d(w) > n1/4, then w ∈ Z′ and d(w) = dH′(w),
- - w∈Z′(d(w) − dH′(w) − dF′(w)) ≤ νn,
- - w∈V\Z′(d(w) − dF′(w)) ≥ n/20, and
- - xz ∈/ E(F′),


Then, for every i ≥ 0 and Z′′ := Z′ \ {z}, P[dGD(x,Z′′) − dF′(x) > ⌊

√ν(d(x) − dF′(x))⌋ + i | GD[Z′] = H′, F′ ⊆ GD, E] ≤ (22√ν)i+1 , where E ∈ {{xz ∈ E(GD)},{xz ∈/ E(GD)}}. Therefore, by averaging, we also have

![image 83](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile83.png>)

![image 84](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile84.png>)

√ν(d(x) − dF′(x))⌋ + i | GD[Z′] = H′, F′ ⊆ GD] ≤ (22√ν)i+1 . Proof. Let K := ⌊

P[dGD(x,Z′′) − dF′(x) > ⌊

![image 85](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile85.png>)

![image 86](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile86.png>)

√ν(d(x) − dF′(x))⌋. For every k ≥ K, let Fk = Fk(E) be the set of graphs G with degree sequence D such that G[Z′] = H′, F′ ⊆ G, dG(x,Z′′)−dF′(x) = k, and E is satisﬁed. As before, we will only perform switches using edges that are not contained in E(H′) ∪ E(F′).

![image 87](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile87.png>)

Consider a graph in Fk. Then in any of the two possibilities for E, there are at most (d(x) − dF′(x))νn switches that lead to a graph in Fk+1.

For every graph in Fk+1, arguing similar as in Lemma 11, there are at least (k + 1)(n/20 − νn − 2n1/2) ≥ (k + 1)n/21 switches that lead to a graph in Fk. This is the number of pairs of edges where one element is among the k+1 edges between x and Z′′ and which are not contained in E(F′), and the other element is among the edges with both endpoints in V \ Z′ (at least n/20 − νn − 2n1/2) which are at distance at least 2 from the endpoints of the ﬁrst element.

Thus, for k ≥ K, we obtain P[Fk+1] ≤

P[Fk] ≤ 22√νP[Fk] ,

21(d(x) − dF′(x))νn (k + 1)n

![image 88](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile88.png>)

![image 89](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile89.png>)

which implies that P[dGD(x,Z′′) − dF′(x) > K + i | GD[Z′] = H′, F′ ⊆ GD,E] ≤ (22√ν)i+1 .

![image 90](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile90.png>)

- Lemma 13. Suppose n ∈ N and 1/n ≪ ν ≪ 1. Suppose Z ⊆ V . Suppose H is a graph with vertex set Z and F is a bipartite graph with vertex partition (Z,V \ Z). Suppose z ∈ Z and x ∈ V \ Z


such that xz ∈/ E(F). Suppose D is a degree sequence on V (write dˆ(u) = d(u) − dH(u) − dF(u) for all u ∈ V ) such that

- - if w ∈ V and d(w) > n1/4, then w ∈ Z and d(w) = dH(w),
- - w∈Z dˆ(w) ≤ νn, and
- - M := w∈V \Z dˆ(w) ≥ n/10.


Then,

dˆ(x)dˆ(z) M

(1 ± 25√ν).

P[xz ∈ E(GD) | GD[Z] = H, F ⊆ GD] =

![image 91](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile91.png>)

![image 92](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile92.png>)

Proof. Let Fxz+ be the set of graphs G with degree sequence D such that G[Z] = H, F ⊆ G and xz ∈ E(G) and Fxz− the set of graphs with degree sequence D such that G[Z] = H, F ⊆ G but xz  ∈ E(G). As before, we consider only switches using edges that are not contained in E(H) ∪ E(F).

First, note that if min{dˆ(x),dˆ(z)} = 0, then the statement holds trivially. Therefore, we may assume that dˆ(x),dˆ(z) ≥ 1. Suppose G ∈ Fxz− . Applying Lemma 12 with Z′ = Z, H′ = H,

- F′ = F and i = 0, we deduce that


√νdˆ(x) | G[Z] = H,F ⊆ G,xz ∈/ E(G)] ≤ 22√ν .

![image 93](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile93.png>)

![image 94](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile94.png>)

P[dG(x,Z) − dF(x) ≥

Let Fˆxz− denote the subset of Fxz− where dG(x,Z) < dF(x) + √νdˆ(x) holds. Then the above implies that

![image 95](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile95.png>)

- (27) |Fˆxz− | ≥ (1 − 22√ν)|Fxz− |. In other words, for at least (1−22√ν)|Fxz− | of the graphs in Fxz− , the vertex x has at most √νdˆ(x) neighbours z′ ∈ Z \ {z} with xz′ ∈/ E(F).

![image 96](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile96.png>)

![image 97](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile97.png>)

![image 98](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile98.png>)

Since dˆ(z) ≥ 1, the vertex z has at least one neighbour V \Z through an edge not in E(F). We

now partition the set Fˆxz− into sets according to the neighbours of z in V \ Z and the neighbours of x in Z (through edges that do not belong to E(F)). We will use y¯ to denote sets of vertices

in {y1,... ,yr} ⊆ V \ (Z ∪ {x}) and z¯ to denote sets of vertices in {z1,... ,zm} ⊆ Z \ {z}. We deﬁne Fˆxz− (¯y,z¯) to be the subset of graphs in Fˆxz− such that the vertices in y¯ are the neighbours of z in V \ Z and the vertices in z¯ are the neighbours of x in Z. In both cases, we only consider the neighbours that are connected to either z or x by an edge not in E(F).

Thus, Fˆxz− is the disjoint union of all subsets Fˆxz− (¯y,z¯), ranging over all y¯ and z¯ as speciﬁed above; that is, in particular, |y¯| = dˆ(z) and |z¯| ≤

√νdˆ(x). We will now use Lemma 11 to show that for most members of Fˆxz− (¯y,z¯), the vertex x is not adjacent to any vertex in y¯.

![image 99](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile99.png>)

To apply Lemma 11, we set Z′ := Z ∪ {x}, V (H′) = Z′, and E(H′) consists of E(H), the edges that join x and z¯, and the edges in F that are incident to x. The graph F′ is the bipartite graph with vertex set (Z′,V \Z′) and edge set E(F)\{xzˆ : zˆ ∈ Z}. Also observe that (E1), (E2), and (E3) are satisﬁed; in particular, w∈V\Z′(d(w) − dF′(w)) ≥ M − d(x) ≥ n/20 holds. Let Fˆxz−−(¯y,z¯) be the subset of Fˆxz− (¯y,z¯) in which x is not adjacent to a vertex in y¯. Since xy ∈/ E(F′) for each y ∈ y¯, Lemma 11 implies that

- (28) |Fˆxz−−(¯y,z¯)| ≥ (1 − 30n−1/2n1/4)|Fˆxz− (¯y,z¯)| = (1 − 30n−1/4)|Fˆxz− (¯y,z¯)|, because y¯ contains at most dˆ(z) ≤ n1/4 vertices.


Next, we partition the set Fˆxz−−(¯y,z¯) according to the neighbours of x in V \ Z. We will use w¯ to denote the set of neighbours of x in V \ Z. Thus w¯ does not contain any member of y¯ ∪ {x} and (1 −

√ν)dˆ(x) ≤ |w¯| ≤ dˆ(x). For such a w¯, we let Fˆxz−−(¯y,z,¯ w¯) be the subset of Fˆxz−−(¯y,z¯) where w¯ are the neighbours of x in V \ Z.

![image 100](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile100.png>)

√ν)dˆ(x) ≤ ℓ ≤ dˆ(x). We ﬁx some i ∈ [r] and j ∈ [ℓ]. An straightforward switching argument as for example performed in Lemma 11 shows that for at least (1−n−1/10)|Fˆxz−−(¯y,z,¯ w¯)| graphs in Fˆxz−−(¯y,z,¯ w¯), the edge yiwj is not present. In this case, we apply the switch {zyi,xwj}. Thus, in total, the number of switches from graphs in Fˆxz−−(¯y,z,¯ w¯) to graphs in Fxz+ is at least

Assume now that y¯ = {y1,... ,yr} and w¯ = {w1,... ,wℓ}, with r = dˆ(z) and (1 −

![image 101](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile101.png>)

√ν)dˆ(x)dˆ(z)|Fˆxz−−(¯y,z,¯ w¯)|. Hence the number of switches from graphs in Fˆxz− (¯y,z¯) to graphs in Fxz+ is at least

(1 − n−1/10)ℓr|Fˆxz−−(¯y,z,¯ w¯)| ≥ (1 − n−1/10)(1 −

![image 102](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile102.png>)

(28) ≥ (1 − 2√ν)dˆ(x)dˆ(z)|Fˆxz− (¯y,z¯)|.

√ν)dˆ(x)dˆ(z)|Fˆxz−−(¯y,z¯)|

(1 − n−1/10)(1 −

![image 103](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile103.png>)

![image 104](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile104.png>)

This in turn implies that the number of switches from graphs in Fxz− to graphs in Fxz+ is at least (1 − 2√ν)dˆ(x)dˆ(z)|Fˆxz− |

(27) ≥ (1 − 24√ν)dˆ(x)dˆ(z)|Fxz− |.

![image 105](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile105.png>)

![image 106](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile106.png>)

Furthermore, since the edges of F are not involved in such switches, there are at most dˆ(x)dˆ(z) switches transforming a graph in Fxz− into a graph in Fxz+ .

Consider now a graph in Fxz+ . Any switch that transforms it into a graph in Fxz− must use the edge xz. It suﬃces to bound the number of choices for the other edge. On the one hand, it is easy to see that there are at most M switches leading to a graph in Fxz− . On the other hand, since d(x),d(z) ≤ n1/4, there are at least M − νn − 2n1/2 edges in distance at least 2 from xz which belong to G[V \ Z]. Thus there are at least M − 2νn switches leading to a graph in Fxz−.

Combining all four bounds, leads to the desired statement.

- 8.2. The exploration process. In order to bound the order of the largest component in GDp


we will perform an exploration process on GD that reveals the components of GDp . An input is a pair (G,S) with the following properties. For a given degree sequence D on the vertex set V , we let G be a graph on V with degree sequence D and for every vertex v, we arbitrarily assign the labels 1,... ,d(v) to its incident edges. In this way, each edge obtains two labels. Since each label is associated with one of the endpoints of the corresponding edge, it is convenient to understand this labelling as a labelling of the semi-edges of the graph in such a way that the semi-edges incident to v are given the labels 1,... ,d(v). Thus, during the exploration process,

- G is equipped with an arbitrary labelling of the semi-edges incident to each vertex. The semiedge labelling ﬁts well with the switching method: if G′ is obtained from G by switching two edges, then the semi-edges of G′ naturally inherit the labelling on the semi-edges of G. The set


S = {σv : v ∈ V } is a collection of permutations, one for each vertex v ∈ V , where σv is a permutation of length d(v). For technical reasons that will become apparent soon, we will need to consider the exploration process on an input. The labelling on the semi-edges together with S, will determine the order in which the vertices are explored during the process.

Given an input (G,S) and a subset of vertices S0 ⊆ V , we proceed to describe the exploration of G from S0. First, for every vertex in v ∈ V , we permute the labels of its incident semi-edges according to σv. Observe that a uniformly selected set of permutations S leads to a uniformly selected labelling of the semi-edges incident to each vertex of G. First, we expose the graph G[S0]. For every t ≥ 0, let St be the set of vertices that have been explored up to time t, let Ht := G[St] and let Ft be the bipartite subgraph with vertex partition (St,V \ St) that contains those edges of E(G) that have been exposed but have not survived the random deletion – we will be referring to these edges as the edges that have failed to percolate. For a vertex u ∈ V , we deﬁne its free degree at time t as

dˆt(u) := d(u) − dHt(u) − dFt(u) . We may assume that V has some ﬁxed ordering. If at time t there exists at least one vertex

- v ∈ St with dˆt(v) ≥ 1, we select1 the smallest vertex vt+1 ∈ St such that dˆt(vt+1) ≥ 1. Let wt+1 be the vertex w ∈ V \St with vt+1w ∈ E(G)\E(Ft) that minimizes σvt+1(ℓ(w)), where ℓ(w) is the


![image 107](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile107.png>)

1To be precise, the selection of a new vertex and the updates of the considered parameters happen between time t and t + 1.

label of the semi-edge incident to vt+1 that corresponds to vt+1w. After that, with probability p, we retain the edge vt+1wt+1 in Gp. If the edge survives percolation, we proceed as follows:

- 1. we set St+1 := St ∪ {wt+1};
- 2. we expose all the edges (back edges) from wt+1 to St \{vt+1} that are not in Ft; we deﬁne the backward degree2 of wt+1 as

d′t(wt+1) := d(wt+1,St \ {vt+1}) − dFt(wt+1) ;

- 3. we retain each of the back edges in Gp independently with probability p; and
- 4. we deﬁne Ht+1 := G[St+1] and let Ft+1 be the bipartite subgraph with vertex partition (St+1,V \ St+1) that contains all the edges between St+1 and V \ St+1 that have failed to percolate so far.


If vt+1wt+1 fails to percolate, we set St+1 := St, Ht+1 := Ht, V (Ft+1) := V (Ft) ∪ {wt+1}, and E(Ft+1) := E(Ft) ∪ {vt+1wt+1}.

Finally, if there is no v ∈ St with dˆt(v) ≥ 1, we let wt+1 = u, where u ∈ V \ St is chosen with probability proportional to dˆt(u), and we set St+1 := St ∪ {wt+1}, Ht+1 := G[St+1] and Ft+1 := Ft. This marks the beginning of a new component.

Note that at time t we have explored at most t new vertices and that G[St] is fully exposed (as well as Gp[St]). Moreover, there is a set of edges E(Ft) joining St and V \ St that have also been exposed but failed to percolate.

Let Ht denote the history of the exploration process after t rounds (at time t). More precisely, this is the random object composed of the collection of all the choices that have been made in the exploration process up to time t, and include the choice of St, Ht = G[St] and Ft. Observe that for a ﬁxed input (G,S), the only randomness in this exploration process stems from the percolation process and the random selection of a new vertex if Ht is a union of components in the percolated graph.

The next two variables will be crucial to control our exploration process at time t:

- - Mt := u∈V \S

t

dˆt(u), which equals the number of ordered edges uv with u ∈ V \ St and uv ∈/ E(Ft).

- - Xt := u∈S


dˆt(u), which equals the number of edges uv with u ∈ St, v ∈ V \ St and uv ∈/ E(Ft).

t

The variable Xt counts the number of edges that are suitable to be used in the step t + 1 to continue the exploration process. If Xt = 0, then we have completed the exploration of a component of Gp.

In order to deduce Proposition 9, we will analyse the exploration procedure on the input (GD,S), where each permutation in S is chosen uniformly at random among all permutations of the appropriate length. In order to show that the largest component in GDp is large or small, we will consider the evolution of the random process {Xt}t≥0 conditional on its history Ht, that is, the set of all decisions taken up to step t. More formally, Ht is the σ-algebra generated by all random decision taken up to step t. Note that now Ht does not only depend on the indicator random variables associated with whether the edges survive percolation, but also on the random graph GD. Using the method of the deferred decisions, we can generate each random permutation while we perform the exploration process. This ensures that, at step t, any choice of wt+1 satisfying the desired properties is equally possible (see Section 2.2 in [15] for a more details).

- 8.3. The expected increase of Xt. For every uv ∈ E(G), let I(uv) be the indicator random variable that the edge uv percolates. If Xt > 0, then the increase of Xt can be written as


- (29) Xt+1 − Xt = −(1 − I(vt+1wt+1)) + I(vt+1wt+1)((dˆt(wt+1) − 2) − 2d′t(wt+1)) ,


![image 108](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile108.png>)

2Note that the backward degree does not include the contribution of vt+1.

and if Xt = 0, as

- (30) Xt+1 − Xt = dˆt(wt+1) .

The next three lemmas use Lemmas 12 and 13, (29), (30), and E(I(vt+1wt+1)) = p to provide bounds on E[Xt+1 − Xt | Ht] assuming that t is small, Mt is large, and Xt is small and for the ﬁrst lemma also positive.

- Lemma 14. Suppose n ∈ N and 1/n ≪ β,ρ,η ≪ λ ≪ µ,1/d,p¯ ≤ 1. Let S0 ⊆ V and let D be a


degree sequence on V such that ΣD ≤ dn¯ and u∈V \S

0

d(u)(p(d(u) − 1) − 1) ≤ −µn. Consider the exploration process described above on (GD,S) with initial set S0 and suppose

- t ≤ ρn. Conditional on Ht satisfying dHt(w) = d(w) for every w ∈ V with d(w) > n1/4, Mt ≥ (1 − η)ΣD, and 0 < Xt ≤ βn, we have

E[Xt+1 − Xt | Ht] ≤ −λ.

Proof. At time t, there are at most t vertices u ∈ V \ St such that dˆt(u) = 0. This is the case since d(u) = dˆt(u) + dFt(u) for all u ∈ V \ St and at each step s ≤ t there is at most one edge added to Fs. Observe also that the function h(x) = x(x − 2) is monotone increasing for x ≥ 1 and h(0) = h(2) = 0, h(1) = −1. This implies that dˆt(u)(dˆt(u) − 2) > d(u)(d(u) − 2) only if d(u) = 1 and dˆt(u) = 0. It follows that

u∈V \St

dˆt(u)(dˆt(u) − 2) ≤ t +

u∈V \S0

(31) d(u)(d(u) − 2) .

The fact that S0 contains all the neighbours in GD of vertices of degree larger than n1/4 and that S0 ⊆ St, ensures that for every v ∈ St such that dˆt(v) ≥ 1, we have d(v) ≤ n1/4. Choose

- u ∈ V \ St. Since Mt ≥ (1 − η)ΣD ≥ n/10 (recall that degrees are positive) and Xt ≤ βn, and provided vt+1u ∈/ E(Ft), we can apply Lemma 13 with ν = β, Z = St, H = Ht, F = Ft, z = vt+1, and x = u to conclude that




dˆt(vt+1)dˆt(u) Mt

P[vt+1u ∈ E(GD) | Ht] =

![image 109](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile109.png>)

(1 ± 25 β) .

![image 110](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile110.png>)

Observe that every edge incident to vt+1 that is not contained in E(Ft) ∪ E(Ht) is chosen with the same probability to continue the exploration process. Thus the probability that u is the

vertex w that minimizes σvt+1(ℓ(w)), where ℓ(w) is the label of the semi-edge incident to vt+1 and corresponding to vt+1w, among all w ∈ V \ St with vt+1w ∈ E(GD) \ E(Ft), is precisely 1/dˆt(vt+1). Therefore,

dˆt(u) Mt

![image 111](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile111.png>)

(1 ± 25 β) .

P[u = wt+1 | Ht] =

![image 112](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile112.png>)

Note that if vt+1u ∈ E(Ft), then P[u = wt+1 | Ht] = 0.

Let n1 denote the number of vertices v ∈ V \ St with dˆt(v) = 1 and let At ⊆ V \ St denote the set of vertices u such that vt+1u ∈ E(Ft). Since d(vt+1) ≤ n1/4, we have |At| ≤ n1/4. Also dˆt(u) < d(u) ≤ n1/4 for all u ∈ At. Therefore, | u∈At dˆt(u)(dˆt(u) − 2)| ≤ n3/4.

Using (29) and the fact that an edge percolates independently from the underlying graph, we conclude that

P[u = wt+1](dˆt(u) − 2)

E[Xt+1 − Xt | Ht] ≤ −(1 − p) + p

u∈V \St

dˆt(u)(dˆt(u) − 2) − n1(1 − 25 β) + 2n3/4

 (1 + 25 β)

p Mt

![image 113](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile113.png>)

![image 114](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile114.png>)

≤ −(1 − p) +

![image 115](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile115.png>)



u∈V \St:dˆt(u)≥2

dˆt(u)(dˆt(u) − 2)

 

2pn3/4 Mt

p Mt

![image 116](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile116.png>)

![image 117](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile117.png>)

≤ −(1 − p) + (1 + 25 β)

 + 100 β +

![image 118](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile118.png>)

![image 119](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile119.png>)

u∈V \St

- (31),β,η≪1 ≤ −(1 − p) + (1 + 25 β)

![image 120](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile120.png>)

p Mt

![image 121](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile121.png>)

 

u∈V \S0

d(u)(d(u) − 2)

 + 2ρ + 101 β.

![image 122](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile122.png>)

Now, we write

p Mt

![image 123](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile123.png>)

 

u∈V \S0

d(u)(d(u) − 2)

 =

p Mt

![image 124](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile124.png>)

 

u∈V \S0

d(u)(d(u) − 1) −

u∈V \S0

d(u)



=

p Mt

![image 125](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile125.png>)

 

u∈V \S0

d(u)(d(u) − 1) −

u∈V \S0

d(u)

 −

1 Mt

![image 126](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile126.png>)

u∈V \S0

d(u) +

1 Mt

![image 127](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile127.png>)

u∈V \S0

d(u)

=

1 − p Mt

![image 128](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile128.png>)

u∈V \S0

d(u) +

1 Mt

![image 129](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile129.png>)

 

u∈V \S0

d(u)(p(d(u) − 1) − 1)

- (32) .


Hence,

 −Mt + (1 + 25 β)

d(u)

1 − p Mt

![image 130](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile130.png>)

E[Xt+1 − Xt | Ht] ≤

![image 131](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile131.png>)



u∈V \S0

1 + 25√β Mt

 

d(u)(p(d(u) − 1) − 1)

![image 132](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile132.png>)

![image 133](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile133.png>)

 + 2ρ + 101 β.

+

![image 134](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile134.png>)

u∈V \S0

But since Mt ≥ (1 − η)ΣD ≥ (1 − η) v∈V \S

d(v), we have

0

d(u)

 −Mt + (1 + 25 β)

1 − p 1 − η −(1 − η) + 1 + 25 β ≤ η + β1/3,

1 − p Mt

![image 135](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile135.png>)

![image 136](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile136.png>)

 ≤

![image 137](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile137.png>)

![image 138](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile138.png>)

u∈V \S0

where the previous inequality follows as η ≤ p and β ≪ 1. Thereby, taking β,ρ,η ≪ λ ≪ µ,1/d¯,

1 + 25√β Mt

d(u)(p(d(u) − 1) − 1)

 

![image 139](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile139.png>)

 + 2ρ + 101 β + η + β1/3

![image 140](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile140.png>)

E[Xt+1 − Xt | Ht] ≤

![image 141](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile141.png>)

u∈V \S0

µ d¯

+ 2ρ + 101 β + η + β1/3 ≤ −λ ,

![image 142](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile142.png>)

≤ −

![image 143](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile143.png>)

which completes the proof. For the following two lemmas we do not require the condition Xt > 0.

- Lemma 15. Suppose n ∈ N and 1/n ≪ β,ρ,η ≪ λ ≪ µ,1/d,p¯ ≤ 1. Let S0 ⊆ V and let D be a degree sequence on V such that ΣD ≤ dn¯ and RpD ≥ µn.


Consider the exploration process described above on (GD,S) with initial set S0 and suppose t ≤ ρn. Conditional on Ht satisfying dHt(w) = d(w) for every w ∈ V with d(w) > n1/4, Mt ≥ (1 − η)ΣD and Xt ≤ βn, we have

2λ + 1 − p p

E[dˆt(wt+1) − 2 | Ht] ≥

.

![image 144](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile144.png>)

dˆt(u)(p(dˆt(u) − 1) − 1). Consider a realisation of the degree sequence of GD[V \ St] which satisﬁes the conditions on Ht, which we denote by Dt′ = (d′1,... ,d′n′) with d′1 ≤ ··· ≤ dn′ and n′ = |Dt′|. Since Mt ≥ (1 − η)ΣD, we have that v∈S

Proof. We will ﬁrst provide a lower bound on u∈V \S

t

d(v) ≤ ηdn¯ . By Proposition 8, with S = St and ν = ηd¯, and since RpD ≥ µn (observe that we choose ν ≪ µ), we have RD

t

′

p t ≥ µn50 . (At this point we want to stress that the previous bound is not a with-high-probability statement; it holds for every possible realisation of Dt′.) Recall that for j ≥ jDp ′

![image 145](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile145.png>)

, we have p(d′j − 1) − 1 > 0. It follows that

t

dˆt(u)(p(dˆt(u) − 1) − 1)

u∈V \St

dGD[V\St](u)(p(dGD[V \St](u) − 1) − 1) − Xt

≥

u∈V \St

jDp ′ t

n′

d′j(p(d′j − 1) − 1) +

d′j(p(d′j − 1) − 1) − djp

≥

(p(djp

D′ t

j=jDp ′ t

j=1

n′

d′j(p(d′j − 1) − 1) − 2βn

≥

j=jDp ′ t

n

(p(d′j − 1) − 1) − 2βn

≥

j=jDp ′ t

β≪µ

µn 60

′

= RD

p t − 2βn

≥

- (33) .


![image 146](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile146.png>)

− 1) − 1) − βn

D′ t

Let n1 denote the number of vertices v ∈ V \St with dˆt(v) = 1 and let At ⊆ V \St denote the set of vertices u such that vt+1u ∈ E(Ft). As in Lemma 14, we have | u∈At dˆt(u)(dˆt(u)−2)| ≤ n3/4.

If Xt > 0 holds3, we can use Lemma 13 to show that

P[wt+1 = u | Ht](dˆt(u) − 2)

pE[dˆt(wt+1) − 2 | Ht] = p

u∈V \St

dˆt(u)(dˆt(u) − 2) − n1(1 + 25 β) − n3/4

 (1 − 25 β)

p Mt

![image 147](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile147.png>)

![image 148](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile148.png>)

≥

![image 149](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile149.png>)



u∈V \St:dˆ(u)≥2

dˆt(u)(dˆt(u) − 2)

 

p Mt

![image 150](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile150.png>)

![image 151](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile151.png>)

≥ (1 − 25 β)

 − 101 β .

![image 152](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile152.png>)

u∈V \St

![image 153](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile153.png>)

3Observe that this calculation is also correct if Xt = 0.

Therefore, using a similar calculation as in (32), we conclude

dˆt(u)

 −Mt + (1 − 25 β)

1 − p Mt

−(1 − p) + pE[dˆt(wt+1) − 2 | Ht] ≥

![image 154](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile154.png>)

![image 155](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile155.png>)



u∈V \St

1 − 25√β Mt

dˆt(u)(p(dˆt(u) − 1) − 1)

 

![image 156](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile156.png>)

- (34)  − 101 β.

![image 157](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile157.png>)

Note that u∈V\S

t

dˆt(u) ≥ Mt − t ≥ (1 − ρ)Mt. Similarly as before,

1 − p Mt

![image 158](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile158.png>)

 −Mt + (1 − 25 β)

![image 159](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile159.png>)

u∈V \St

dˆt(u)

 ≥ (1 − p) −1 + (1 − 25 β)(1 − ρ)

![image 160](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile160.png>)

- (35) ≥ −(ρ + 25 β). Using (33), (34), (35), and taking β,ρ ≪ λ ≪ µ,1/d¯, we conclude the proof of the lemma as

![image 161](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile161.png>)

−(1 − p)+pE[dˆt(wt+1) − 2 | Ht] ≥

(1 − 25√β)µ 60d¯ − ρ − 126 β ≥ 2λ .

![image 162](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile162.png>)

![image 163](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile163.png>)

![image 164](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile164.png>)

Lemma 16. Suppose n ∈ N and 1/n ≪ β,ρ,η ≪ λ ≪ µ,1/d,p¯ ≤ 1. Suppose S0 ⊆ V and let D be a degree sequence on V such that ΣD ≤ dn¯ and RpD ≥ µn.

Consider the exploration process described above on (GD,S) with initial set S0 and suppose t ≤ ρn. Conditional on Ht satisfying dHt(w) = d(w) for every w ∈ V with d(w) > n1/4, Mt ≥ (1 − η)ΣD and Xt ≤ βn, we have

E[d′t(wt+1) | Ht] ≤

1 10

![image 165](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile165.png>)

E[dˆt(wt+1) − 2 | Ht], and

E[Xt+1 − Xt | Ht] ≥ λ .

Proof. Suppose ﬁrst that Xt = 0. Recall that in this case, we start the exploration of a new component and we select a vertex in V \St with probability proportional to its free degree. As this is at least 1, we deduce E[Xt+1−Xt | Ht] ≥ p ≥ λ. By Lemma 15, we have E[dˆt(wt+1)−2 | Ht] > 0.

- As d′t(wt+1) = 0, the ﬁrst bound also follows. Suppose now that Xt > 0. In order to bound the expectation of d′(wt+1) it is clear from


Lemma 12 with ν = β, Z = St, H = Ht, F′ = Ft, x = wt+1, z = vt+1 and E = {xz ∈ E(GD)} that

E[d′t(wt+1) | Ht] ≤ 2 βE[dˆt(wt+1) | Ht]

![image 166](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile166.png>)

- (36) = 2 βE[dˆt(wt+1) − 2 | Ht] + 4 β


+

![image 167](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile167.png>)

u∈V \St

![image 168](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile168.png>)

![image 169](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile169.png>)

1 10

E[dˆt(wt+1) − 2 | Ht] ,

≤

![image 170](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile170.png>)

where the previous inequality follows from the fact that E[dˆ(wt+1) − 2 | Ht] ≥ 2λ by Lemma 15 and β ≪ λ.

Using (29), (36), Lemma 15 and taking β ≪ λ, we obtain

E[Xt+1 − Xt | Ht] = −(1 − p) + p(E[dˆt(wt+1) − 2 | Ht] − 2E[d′t(wt+1) | Ht]) ≥ −(1 − p) + p · (1 − 4 β)E[dˆt(wt+1) − 2 | Ht] − 8p β ≥ 2(1 − 4 β)λ − (1 − p)4 β − 8p β ≥ λ ,

![image 171](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile171.png>)

![image 172](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile172.png>)

![image 173](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile173.png>)

![image 174](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile174.png>)

![image 175](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile175.png>)

which completes the proof.

- 8.4. Another concentration inequality. The following lemma will be used to show that several parameters of our process do not deviate much from their expected value.


- Lemma 17. Suppose a < 0,b > 0, m ∈ {0,1}, t ∈ N, and y ∈ [a,0). Suppose τ is a stopping


time with respect to a ﬁltration (Fs)ts=0. Suppose Y0,Y1,... ,Yt are random variables such that Ys is measurable at time s and Ys − Ys−1 ∈ [a,b]. Suppose that for any s ∈ [t], we have

E[1{s≤τ}(−1)m(Ys − Ys−1) | Fs−1] ≤ y1{s≤τ}. Then

y2

yt 2

12(b−a)2 ·t.

< e−

P (−1)m(Yτ∧t − Y0) + 1{t>τ}(t − τ)y >

![image 176](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile176.png>)

![image 177](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile177.png>)

To this end, we shall use the following lemma which was proved in [25] and is a corollary of a martingale concentration theorem (Theorem 3.12) from [17]. Proposition 18. Let W1,... ,Wt be random variables taking values in [0,1] such that

E[Ws | W1,... ,Ws−1] ≤ ws for each s ∈ [t]. Let λt := ts=1 ws. Then for any 0 < δ ≤ 1, we have P

t

δ2λt

Ws ≥ (1 + δ)λt ≤ e−

3 .

![image 178](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile178.png>)

s=1

Proof of Lemma 17. The assumption of the lemma implies that for every s ∈ [t] E[1{s≤τ}(−1)m(Ys − Ys−1) + y1{s>τ} | Fs−1] ≤ y.

We set Zs := 1{s≤τ}(−1)m(Ys − Ys−1) + y1{s>τ}. The history Fs−1 completely determines Z1,... ,Zs−1, whereby

- (37) E[Zs | Z1,... ,Zs−1] ≤ y. We now rescale the variables Zs to obtain random variables in [0,1]. To this end, we set
- (38) Ws :=


Zs − a b − a

. It follows directly from (37) that

![image 179](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile179.png>)

y − a b − a

E[Ws | W1,... ,Ws−1] ≤

=: w . By Proposition 18 with ws := w for each s ∈ [t] and λt := wt, for any δ ∈ (0,1], it follows that P

![image 180](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile180.png>)

t

Ws ≥ (1 + δ)tw < e−δ2wt/3 .

s=1

Using the deﬁnition of Ws in (38), we obtain P

t

δ2t(y−a)

Zs ≥ (1 + δ)(y − a)t + at ≤ e−

3(b−a) .

![image 181](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile181.png>)

s=1

Recall that a < y < 0. Choosing δ = −2(yy−a) ∈ (0,1], we have (1+δ)(y−a)t+at = yt+δ(y−a)t = yt 2 . Using that b − a ≥ y − a, we obtain

![image 182](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile182.png>)

![image 183](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile183.png>)

t

y2

ty 2

< e−

12(b−a)2 ·t .

![image 184](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile184.png>)

Zs ≥

P

![image 185](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile185.png>)

s=1

Finally, note that

t

Zs = 1{t>τ}((−1)m(Yτ − Y0) + (t − τ)y) + 1{t≤τ}(−1)m(Yt − Y0)

s=1

= (−1)m(Yτ∧t − Y0) + 1{t>τ}(t − τ)y and the lemma follows.

- 8.5. Proof of Proposition 9. In this subsection we will prove the Proposition 9. We ﬁrst need three more technical statements.


- Lemma 19. Suppose n ∈ N and 1/n ≪ α,β ≪ ξ ≪ η,ρ ≪ µ,1/d,p¯ ≤ 1. Suppose S0 ⊆ V and let D be a degree sequence on V such that ΣD ≤ dn¯ and w ∈ S0 for every w ∈ V with d(w) > n1/4


d(v) ≤ αn. Let τ be the smallest t ≤ n such that either Xt > βn or Mt < (1 − η)ΣD - if this does not exist, we set τ = n + 1. Conditional on the event that dH0(w) = d(w) for every

and v∈S

0

- w ∈ V with d(w) > n1/4, then P[τ ≤ ξn,Xτ ≤ βn] = o(n−2).


Proof. Observe that P[τ ≤ ξn,Xτ ≤ βn,Mτ ≥ (1 − η)ΣD] = 0. Thus

- (39) P[τ ≤ ξn,Xτ ≤ βn] = P[τ ≤ ξn,Xτ ≤ βn,Mτ < (1 − η)ΣD] .

Note ﬁrst that if Mτ < (1 − η)ΣD, then v∈S

τ

d(v) ≥ ηΣD ≥ ηn. Let Rt be the set of times s ∈ {0,... ,t} where the edge vs+1ws+1 has percolated and let Rt′ be the set of times where s ∈ {0,... ,t} where Xs = 0. Therefore, we have

t∈Rτ

(dˆt(wt+1) + dFt(wt+1)) +

t∈R′τ

dˆt(wt+1) ≥

v∈Sτ

d(v) −

v∈S0

- (40) d(v) ≥ (η − α)n .

- At each step s ∈ {0,... ,t} of the process at most one edge is added to Fs. For every 1 ≤ t ≤ τ, it follows that


s∈Rt

dFs(ws+1) ≤ t + 1 ≤ ξn + 1 . Taking α ≪ ξ ≪ η and using (40) one concludes

t∈Rτ∪R′τ

dˆt(wt+1) ≥

t∈Rτ

dˆt(wt+1) + dFt(wt+1) − ξn − 1 +

t∈R′τ

dˆt(wt+1) ≥

ηn 2

![image 186](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile186.png>)

- (41) .

From (29) and (30), and with ξ ≪ η,p, it follows that Xτ = X0 − (τ − |Rτ|) +

t∈Rτ

(dˆt(wt+1) − 2 − 2d′t(wt+1)) +

t∈R′τ

dˆt(wt+1)

≥ −3τ +

- 1

![image 187](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile187.png>)

- 2 t∈R


τ∪R′τ

dˆt(wt+1) +

- 1

![image 188](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile188.png>)

- 2 t∈R


τ

dˆt(wt+1) − 4d′t(wt+1)

(41) ≥

ηn 4 − 3ξn +

![image 189](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile189.png>)

- 1

![image 190](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile190.png>)

- 2 t∈R


τ

dˆt(wt+1) − 4d′t(wt+1)

≥

ηn 8

![image 191](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile191.png>)

+

1 2 t∈R

![image 192](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile192.png>)

τ

- (42) dˆt(wt+1) − 4d′t(wt+1) .

Therefore, we deduce that P[τ ≤ ξn,Xτ ≤ βn,Mτ < (1 − η)ΣD] ≤ P τ ≤ ξn,Xτ ≤ βn,Xτ ≥

ηn 8

![image 193](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile193.png>)

+

- 1

![image 194](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile194.png>)

- 2 t∈R


τ

- (43) dˆt(wt+1) − 4d′t(wt+1) .


We take β ≪ η. So in order that Xτ ≤ βn, it suﬃces to prove that − t∈Rτ(dˆt(wt+1) − 4d′t(wt+1)) is not too large.

We deﬁne the following sequence Y1,... ,Yξn of random variables. Let Y0 := 0. Suppose t is the s-th smallest entry in Rτ. We set

Ys := Ys−1 − (dˆt(wt+1) − 4d′t(wt+1)); in the case where |Rτ| < s and s ≤ ξn, we set

Ys := Ys−1 − 1.

Observe that |Ys−Ys−1| ≤ 4n1/4. Let {Fs}ξns=0 be the ﬁltration induced by the sequence {Ys}ξns=0.

Suppose again that t is the s-th smallest entry in Rτ. We apply Lemma 12 with ν = β, Z′ = St, H′ = GD[St], F′ = Ft, x = wt+1, z = vt+1 and E = {xz ∈ E(GD)}. The ﬁrst three conditions of the lemma are satisﬁed: the ﬁrst one is immediate from our hypothesis, the second one follows

from Xt ≤ βn and the third one from the fact that Mt− w∈V\St dFt(w) ≥ (1−η)ΣD −t ≥ n/20. Moreover, xz ∈/ E(F′) holds. Similarly as in (36), we obtain,

1 10

E[dˆ(wt+1) | Ht] .

E[d′(wt+1) | Ht] ≤

![image 195](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile195.png>)

Let t−1 be deﬁned such that t−1 −1 is the (s−1)-th smallest entry in Rτ or −1 if s = 1. Observe that given Ht−1 we still can apply Lemma 12 to any possible input with history Ht. This implies that

1 10

E[dˆ(wt+1) | Ht−1] . Clearly E[dˆt(wt+1)|Ht−1] ≥ 1, so

E[d′(wt+1) | Ht−1] ≤

![image 196](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile196.png>)

- 1

![image 197](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile197.png>)

- 2


E[Ys+1 − Ys|Fs] ≤ −

.

We can apply Lemma 17 to the collection Y0,... Yξn with −a = b = 4n1/4,y = −1/2,m = 0 and t = ξn, where τ is the stopping time τ = ξn, to conclude that

ξn 4

P −Yξn <

![image 198](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile198.png>)

= o(n−2).

d ˆt(wt+1) − 4d′t(wt+1) ≥ −Yξn − ξn. Hence

Observe that by construction of Ys we have t∈R

τ∧ξn

- (44) P


d ˆt(wt+1) − 4d′t(wt+1) < −



t∈Rτ∧ξn

So by (43) we can further bound P[τ ≤ ξn,Xτ ≤ βn,Mτ < (1 − η)ΣD] ≤ P τ ≤ ξn,Xτ ≤ βn,Xτ ≥

+ P 

ηn 8 −

3ξn 8

![image 199](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile199.png>)

![image 200](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile200.png>)



t∈Rτ∧ξn

(44)

3ξn 8

ηn 8 −

+ o(n−2). We will show that the ﬁrst term is 0. Indeed,

≤ P τ ≤ ξn,Xτ ≤ βn,Xτ ≥

![image 201](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile201.png>)

![image 202](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile202.png>)

  = o(n−2) .

- 3ξn

![image 203](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile203.png>)

- 4


 

- 3ξn

![image 204](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile204.png>)

- 4


d ˆt(wt+1) − 4d′t(wt+1) < −

Xτ >

η 8 −

3ξ 8

![image 205](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile205.png>)

![image 206](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile206.png>)

η 16 · n > βn ;

n ≥

![image 207](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile207.png>)

so this cannot hold simultaneously with Xτ ≤ βn. Finally by (39), we conclude that the probability that τ ≤ ξ and Xτ ≤ βn is o(n−2).

- Lemma 20. Suppose n ∈ N and 1/n ≪ α ≪ β ≪ η,ρ ≪ µ,1/d,p¯ ≤ 1. Let S0 ⊆ V and let D be a degree sequence on V such that ΣD ≤ dn¯ and w ∈ S0 for every w ∈ V with d(w) > n1/4, and


- v∈S0 d(v) ≤ αn. Let τ be the smallest t ≤ n such that either Xt > βn or Mt < (1 − η)ΣD -

if this does not exist, we set τ = n + 1. Conditional on the event that dH0(w) = d(w) for every

- w ∈ V with d(w) > n1/4, the following holds:


- (i) If u∈V \S

0

d(u)(p(d(u) − 1) − 1) ≤ −µn and τ1 is the smallest t such that Xt = 0, then the probability that τ1 > ρn is o(1/n).

- (ii) If RpD ≥ µn, then the probability that τ > ρn or that Xτ ≤ βn is o(1/n).


Proof. Recall that I(uv) is the indicator random variable that is equal to 1 if and only if uv ∈ E(GD) survives percolation when it is exposed. Also, recall (29): if Xt > 0, then

Xt+1 − Xt = −(1 − I(vt+1wt+1)) + I(vt+1wt+1)((dˆt(wt+1) − 2) − 2d′t(wt+1)) .

We ﬁrst prove (i). Consider the sequence Y0,Y1,... of random variables such that Y0 := X0 and

Ys := Ys−1 + 1{s≤τ∧τ1} (Xs − Xs−1) .

Thus |Ys − Ys−1| ≤ 2n1/4. Let us take λ satisfying η,ρ ≪ λ ≪ µ,1/d,p¯ . Since Xs−1 > 0 if s ≤ τ ∧ τ1, by Lemma 14, we have

E[Ys − Ys−1|Hs−1] ≤ −λ1{s≤τ∧τ1} =: y1{s≤τ∧τ1} .

Let ν and ξ be such that α ≪ ν ≪ β ≪ ξ ≪ η,ρ. We now apply Lemma 17 to Ys with −a = b = 2n1/4, m = 0 and t = cn, for some c such that 1/n ≪ c < 1, to conclude that

λ 2 · cn ≥ 1 − e−λ

2

48 ·cn1/2

P (Xτ∧τ1∧cn − X0) − 1{cn>τ∧τ1}(cn − τ ∧ τ1)λ ≤ −

![image 208](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile208.png>)

![image 209](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile209.png>)

- (45) ≥ 1 − n−2.


Let E1(t) denote the event (Xτ∧τ1∧t − X0) − 1{t>τ∧τ1}(t − τ ∧ τ1)λ ≤ −λ2 · t. We use Lemma 19 (for the second inequality below) and we write

![image 210](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile210.png>)

P[τ1 > ρn] = P[τ1 > ρn,τ ≤ ξn] + P[τ1 > ρn,τ > ξn] ≤ P[τ1 > ρn,τ ≤ ξn,Xτ > βn] + n−2 + P[τ1 > ρn,τ > ξn] ≤ P[τ1 > ρn,τ ≤ ξn,Xτ > βn,E1(νn)] + P[E1(νn)] + n−2 + P[τ1 > ρn,τ > ξn]

![image 211](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile211.png>)

(45=) P[τ1 > ρn,τ ≤ ξn,Xτ > βn,E1(νn)] + 2n−2 + P[τ1 > ρn,τ > ξn].

Suppose that the events τ1 > ρn, 34νn ≤ τ ≤ ξn,Xτ > βn and E1(νn) are realised simultaneously. Recall that α ≪ ν ≪ β ≪ ξ ≪ ρ ≪ λ. Since τ1 > ρn, we have Xτ∧τ1∧νn > 0. Then, we reach a contradiction in the following way

![image 212](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile212.png>)

λν 8

λ 2

νn + X0 + 1{νn>τ∧τ1}(νn − τ ∧ τ1)λ ≤ −

0 < Xτ∧τ1∧νn ≤ −

n < 0 .

![image 213](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile213.png>)

![image 214](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile214.png>)

Suppose that the events τ1 > ρn, τ ≤ 34νn,Xτ > βn and E1(νn) are realised simultaneously. Again, we reach a contradiction as follows

![image 215](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile215.png>)

λ 2

νn + X0 + (νn − τ)λ ≤ 2λνn < βn . Hence, P[τ1 > ρn,τ ≤ ξn,Xτ > βn,E1(νn)] = 0.

βn < Xτ∧τ1∧νn = Xτ ≤ −

![image 216](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile216.png>)

Thereby,

P[τ1 > ρn] ≤ P[τ1 > ρn,τ > ξn] + 2n−2

≤ P[τ1 > ρn,τ > ξn,E1(ξn)] + P[E1(ξn)] + 2n−2 (45=) P[τ1 > ρn,τ > ξn,E1(ξn)] + 3n−2.

![image 217](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile217.png>)

But again the event τ1 > ρn,τ > ξn cannot occur simultaneously with E1(ξn), since otherwise, Xξn = Xτ∧τ1∧ξn ≤ −

λ 2

ξn + X0 < 0 .

![image 218](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile218.png>)

We conclude that P[τ1 > ρn] ≤ 3n−2. We proceed to prove (ii). Let Y0 := 0. For s ≥ 1, consider the random variable

Ys := Ys−1 − 1{s≤τ} (Xs − Xs−1) . By the second part of Lemma 16,

E[Ys|Hs−1] ≤ −λ1{s≤τ} =: y1{s≤τ} .

Let us take ξ and λ such that β ≪ ξ ≪ η,ρ ≪ λ ≪ µ,1/d,p¯ . Similarly as before, we can apply Lemma 17 to the random variables Ys with −a = b = 2n1/4, m = 1 and t = ξn to conclude that

λ 2 · ξn ≥ 1 − e−λ

2

48 ·ξn1/2 = 1 − o(n−2).

- (46) P (Xτ∧ξn − X0) + 1{ξn>τ}(ξn − τ)λ >


![image 219](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile219.png>)

![image 220](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile220.png>)

Now, let E2(ξn) denote the event Xτ∧ξn − X0 + 1{ξn>τ}(ξn − τ)λ > λ2 · ξn. Letting ξ ≪ ρ, we then have

![image 221](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile221.png>)

![image 222](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile222.png>)

P[τ > ρn] ≤ P[τ > ξn] ≤ P[τ > ξn,E2(ξn)] + P[E2(ξn)]

(46) ≤ P[τ > ξn,E2(ξn)] + n−2 .

But if τ > ξn holds simultaneously with E2(ξn), then we have Xξn = Xτ∧ξn > X0 + λξ2 · n ≥ βn which contradicts that τ > ξn. So, this event has probability 0.

![image 223](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile223.png>)

Similarly, using Lemma 19 (for the ﬁrst inequality) we obtain

P[Xτ < βn] = P[Xτ < βn,τ ≤ ξn] + P[Xτ < βn,τ > ξn] ≤ n−2 + P[Xτ < βn,τ > ξn] ≤ n−2 + P[Xτ < βn,τ > ξn,E2(ξn)] + P[E2(ξn)]

![image 224](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile224.png>)

(46=) n−2 + P[Xτ < βn,τ > ξn,E2(ξn)].

As above, τ > ξn and E2(ξn) are incompatible. Therefore, the second event has probability 0, whereby we deduce that P[Xτ < βn] = o(1/n).

- Lemma 21. Let 1/n ≪ ν,ρ ≪ 1/d,p¯ ≤ 1. Suppose that S ⊆ V with |S| ≤ ρn + 1 and U ⊆ S. Suppose H is a graph with vertex set S and F is a bipartite graph with vertex partition (S,V \ S) and |E(F)| ≤ ρn. Let D be a degree sequence on V such that ΣD ≤ dn¯ and, moreover,


d(w) = dH(w) for every w ∈ V with d(w) ≥ n1/4 and u∈U(d(u) − dH(u) − dF(u)) ≥ νn. Conditional on GD[S] = H and on F ⊆ GD being the set of edges between S and V \ S that

have failed to percolate in GDp , the probability that the union of components of GDp that intersect U contains at most (νp/(20d¯))n vertices is o(1).

Proof. We may assume that |U| < (νp/(20d¯))n. Let GˆD := GD − E(F). Our aim is to show that NGˆD(U) ⊆ NGD(U) is typically large. Note that for every vertex w ∈ NGˆD(U), there is at least one edge uw ∈ E(GˆD) with u ∈ U that has not been exposed to percolation. In the second part of the proof, we will show that many of these edges are preserved in GDp , implying that the union of components of GDp that intersect U contains many vertices.

Let K := ⌊(ν/5d¯)n⌋. For every k < K, let Fk be the set of graphs G with degree sequence D

such that G[S] = H, F ⊆ G and |NGˆ(U)| = k, where Gˆ := G − E(F). In order to estimate the probability of each Fk we only use edges not contained in E(H) ∪ E(F) for a switch.

Consider a graph in Fk. There are at least νn − k ≥ 4νn/5 choices for an edge uv ∈ E(Gˆ) with u ∈ U, v ∈ NGˆ(U) and such that there exists u′ = u with u′ ∈ U and u′v ∈ E(Gˆ). Since δ(G) ≥ 1 and d(w) ≤ n1/4 for every w ∈ {u} ∪ NGˆ(U), there are at least (n − |S ∪ NGˆ(U)|)/2 − |E(F)| − 2n1/2 ≥ n/3 edges xy ∈ E(Gˆ) with x ∈/ S ∪ NGˆ(U) and which are in distance at least 2 from uv. Thus, the total number of such switches into a graph in Fk+1 is at least νn2/4.

Given a graph in Fk+1, then there are at most (k + 1)dn¯ switches that transform it into a graph in Fk.

Thus, for every k < K, we have

(k + 1)dn¯

- 4

![image 225](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile225.png>)

- 5 · P[Fk+1] ,


νn2/4 · P[Fk+1] ≤ which implies

P[Fk] ≤

![image 226](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile226.png>)

P[∪k≤K/2Fk] ≤ P[FK/2]

(4/5)−i ≤ (4/5)−K/2+1P[FK] = o(1) .

i≥0

That is, with probability 1 − o(1), there are at least (ν/10d¯)n vertices that are connected to U by at least one edge in GˆD. These edges have still not been exposed for percolation. Chernoﬀ’s inequality (Lemma 6) now implies that with probability 1 − o(1) a proportion of at least p/2 of

(U)| ≤ (νp/(20d¯))n. The conclusion follows.

- them will be retained in GDp . Therefore, with probability o(1), we have |NGD


p

Proof of Propostion 9. We start with the ﬁrst statement. Suppose there exists a set S ⊆ V such that d(v) ≤ n1/4 for every v ∈/ S, and for every possible choice of G with degree sequence D, we have u∈N

G[S] d(u) ≤ αn and u∈V\N

G[S] d(u)(p(d(u) − 1) − 1) ≤ −µn.

We show that every vertex u ∈ V is in a component of size at least γn with probability o(1/n). A union bound over all vertices completes the proof.

Suppose u ∈ V . We prove the desired statement conditional on every possible neighbourhood of S. Thus let S0 := N[S] ∪ {u} for some choice of N[S]. Hence u∈S

d(u) ≤ 2αn and

0

u∈V \S0 d(u)(p(d(u) − 1) − 1) ≤ −µn/2. Moreover, for every vertex v ∈ V with d(v) > n1/4, all its neighbours belong to S0. We apply the ﬁrst part of Lemma 20 with ρ = γ/2. Since γ ≪ µ, there exists a t ≤ γn/2 such that Xt = 0 with probability 1 − o(1/n). Since |St| ≤ t + |S0| ≤ (γ/2 + 2α)n < γn, the union of all components that intersect {u} ∪ N[S] contain less than γn vertices with probability 1 − o(1/n).

Now we prove the second statement. Recall that now ∆(D) ≤ n1/4. Let S0 := {u0} for an arbitrary vertex u0 ∈ V . Clearly, v∈S

d(v) ≤ αn. Recall that Xt counts the number of edges between St and V \ St in the graph GD that have not yet been exposed for percolation. Observe that all the edges counted by Xt will belong to the same component of GDp if they survive percolation. Note that this component may not contain u0.

0

We choose β and ρ such that γ ≪ β ≪ ρ ≪ µ. By the second part of Lemma 20, with probability 1 − o(1), there exists a τ ≤ ρn with Xτ ≥ βn. Recall that Hτ denotes the history of the exploration process, with the corresponding choice of Sτ, Hτ and Fτ at time τ. Let U be the set of vertices from the component of GDp under exploration at time τ that have been already explored; that is, the ones in Sτ. Then u∈U(d(u) − dHτ(u) − dFτ(u)) = Xτ ≥ βn. Moreover, |Sτ| ≤ τ + 1 ≤ ρn + 1 and |E(Fτ)| ≤ τ ≤ ρn. By Lemma 21 with ν = β, S = Sτ, H = Hτ and F = Fτ, with probability 1 − o(1), there exists a component in GDp with at least (βp/(20d¯))n ≥ γn vertices.

9. Degree sequences with many vertices of high degree

In this section we prove Proposition 10. As in the proof of Theorem 3, we adapt our argumentation according to the structure of the degree sequence. If not stated otherwise, we always consider a degree sequence D on V with average degree at most d¯, where V is a set of size n. Recall that d¯ is assumed to be ﬁxed. In addition, we assume 1/n ≪ 1/d¯ ≤ 1. We start with some notation, which we use throughout this section. Let

T := {u ∈ V : d(u) ≤ 3d¯},

- S1 := {u ∈ V : d(u) ≥ log2 n},
- S2 := {u ∈ V : d(u) ≥ n1/3}, and
- S3 := {u ∈ V : d(u) ≥ n4/5}.


We say D satisﬁes (Dǫ1) if

(Dǫ1) d(u) ≥ ǫn ,

u∈S1

and we say it satisﬁes (Dǫ3) if

ǫn 10

(Dǫ3) .

d(u) ≥

![image 227](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile227.png>)

u∈S3

- 9.1. Degree sequences with vertices of very high degree. In this subsection we consider


degree sequences D that satisfy (Dǫ3). We collect several results about such degree sequences, which we will use in the proof of Proposition 10.

The ﬁrst lemma shows that GD[S3] is typically a clique.

- Lemma 22. Suppose n ∈ N and 1/n ≪ 1/d¯≤ 1. Let V be a set of size n and let D be a degree sequence on V with ΣD ≤ dn¯ . Then the probability that GD[S3] is a clique is at least 1 − n−1/11.


Proof. Since ΣD ≤ dn¯ , it follows that |S3| ≤ dn¯ 1/5. If P[uv ∈/ E(GD)] ≤ n−1/2 for every u,v ∈ S3, a union bound over all pairs u,v ∈ S3 proves the lemma.

It remains to prove that for each pair u,v ∈ S3, we have P[uv ∈/ E(GD)] ≤ n−1/2. Let F− be the set of graphs G on V with degree sequence D and uv ∈/ E(G) and let F+ be the set of graphs G on V with degree sequence D and uv ∈ E(G).

Suppose G ∈ F−. Since d(u),d(v) ≥ n4/5 and ΣD ≤ dn¯ , there exist at least n8/5/2 ordered pairs (x,y) with x ∈ N(u), y ∈ N(v) and xy ∈/ E(G). Switching ux and vy transforms G into a graph in F+.

Suppose G ∈ F+, then there are at most dn¯ switches that transform G into a graph in F−. Therefore, by (11), we obtain

2dn¯ n8/5 · P[F+] ≤ n−1/2.

P[F−] ≤

![image 228](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile228.png>)

Conditional on GD[S3] being a clique, GDp [S3] is a binomial random graph on |S3| vertices and edge probability p. Since p ∈ (0,1), it is an exercise to check that S3 induces a connected graph in GDp with probability at least 1 − c|1S3|, for some c1 = c1(p) < 1. Together with Lemma 22 we obtain the following corollary.

Corollary 23. Suppose n ∈ N and 1/n ≪ 1 − c ≪ p,1/d¯≤ 1. Let V be a set of size n and let D be a degree sequence on V with ΣD ≤ dn¯ . Then

P[GDp [S3] is disconnected] ≤ c|S3|.

The next lemma shows that, typically, the vertices in S2 \ S3 are connected to a vertex in S3 in GD if |S3| ≥ 100.

- Lemma 24. Suppose n ∈ N and 1/n ≪ 1/d¯≤ 1. Let V be a set of size n and let D be a degree sequence on V with ΣD ≤ dn¯ . Assume that |S3| ≥ 100. Then, with probability at most 1/n, there is a vertex u ∈ S2 \ S3 which is not adjacent to a vertex in S3.


Proof. It suﬃces to show that every vertex u ∈ S2 is adjacent to a vertex in S3 with probability at least 1−n−2. Let u ∈ S2 and let 0 ≤ k ≤ 50. Let Fk be the event that u is adjacent to exactly k vertices in S3.

Consider a graph G ∈ Fk+1. Clearly, there are at most (k +1)dn¯ switches transforming G into a graph in Fk.

Consider a graph G ∈ Fk. Let x be any vertex in S3 which is not adjacent to u (since |S3| ≥ 100 but k ≤ 50 there is such a vertex). Thus there are at least n1/3+4/5 = n17/15 pairs (v,y) such that v ∈ N(u) and y ∈ N(x). For at most n pairs v = y and for at most 2dn¯ pairs, we have vy ∈ E(G). Thus at least n17/15/2 pairs lead to a {uv,xy}-switch transforming G into a graph in Fk+1. Hence

P[Fk] ≤ n−1/15 · P[Fk+1]. Moreover, this implies

P[F0] ≤ n−50/15 · P[F50] ≤ n−2, which completes the proof.

Recall that T is the set of vertices of degree at most 3d¯. As D has average degree at most d¯, many vertices belong to T. More precisely, as every vertex in V \ T has degree at least 3d¯ and the average degree at most d¯, we conclude |V \ T| ≤ n/3. Thus

- 2n

![image 229](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile229.png>)

- 3


|T| ≥

- (47) . The next lemma shows that many vertices in T are adjacent to a vertex in S2 if (Dǫ3) holds.


- Lemma 25. Suppose n ∈ N and 1/n ≪ 1000ǫ ≤ 1/d¯≤ 1. Suppose V is a set of size n and D is a degree sequence on V with ΣD ≤ dn¯ that satisﬁes (Dǫ3). Then,

P[|N(S2) ∩ T| ≤ ǫ2n] ≤ n−1 .

Proof. For every 0 ≤ k ≤ 2ǫ2n, let Fk be the set of graphs with degree sequence D such that |T ∩ N(S2)| = k.

Suppose 0 ≤ k ≤ 2ǫ2n. Consider at graph G ∈ Fk+1. In order to transform G into a graph in Fk, we need to select a vertex u ∈ T ∩ N(S2) which has at exactly one neighbour v in S2. Then there are at most dn¯ switches involving uv. Thus in total, there are at most 2ǫ2dn¯ 2 switches from Fk+1 to Fk.

Suppose G ∈ Fk. Recall that k ≤ 2ǫ2n. Since ΣD ≤ dn¯ , we have |S2| ≤ dn¯ 2/3 and |S3| ≤ dn¯ 1/5. As (Dǫ3) holds and as there at most (d¯)2n2/3+1/5 ≤ ǫn/40 edges between the vertices of S3 and S2, it turns out that there are at least ǫn/15 edges xy such that x ∈ S3 ⊆ S2 and y ∈ N(S2). More speciﬁcally, since k ≤ 2ǫ2n, there are least ǫn/20 edges xy with x ∈ S3 and such that y satisﬁes one of the following: either y ∈ N(S2) \ T or if y ∈ N(S2) ∩ T, then it has at least two neighbours in S2. Fix such a choice of an edge xy. Note that if we switch xy with another edge uv such that u ∈ T \ N(S2), we can only increase the neighbourhood of S2. Observe that there are at most n2/3 edges uv such that u ∈ T \ N(S2) and v ∈ N(y). Furthermore, |T \ N(S2)| ≥ n/2. Let u ∈ T \ N(S2) and v ∈ N(u) such that v ∈/ N(y). Then there are at least n/2 − n2/3 ≥ n/3 choices for the edge uv. Observe that the {uv,xy}-switch yields a graph in Fk+1 and there are at least ǫn2/60 switches from Fk to Fk+1. Hence

P[Fk] ≤

120ǫ2dn¯ 2 ǫn2 · P[Fk+1] ≤

![image 230](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile230.png>)

- 1

![image 231](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile231.png>)

- 2


P[Fk+1]. In particular,

ǫ2n

k=0

P[Fk] ≤ 2P[Fǫ2n] ≤ 2−ǫ2n+1 ,

which completes the proof.

9.2. Lighter degree sequences. In this subsection we consider degree sequences that satisfy (Dǫ1) but not (Dǫ3). The ﬁrst lemma shows that in this case, typically, the minimum degree of GD[S1] is large.

- Lemma 26. Suppose n ∈ N and 1/n ≪ ǫ ≪ 1/d¯ ≤ 1. Let V be a set of size n and let D be a degree sequence on V with ΣD ≤ dn¯ . Assume also D that satisﬁes (Dǫ1), but not (Dǫ3). Then, with probability o(1), there exists a vertex u ∈ S1 such that dGD[S1](u) ≤ min{d(u),n1/6}·ǫ/(16d¯).


Proof. Let u ∈ S1 and let K := ⌊min{d(u),n1/6} · ǫ/(16d¯)⌋. For every 0 ≤ k ≤ 2K, let Fk be the set of graphs G with degree sequence D such that dG[S1](u) = k.

Suppose G ∈ Fk. There are at least d(u) − k ≥ d(u)/2 choices for an edge uv with v ∈ N(u) \ S1. The degree of v is less than log2 n and each one of its neighbours has either degree less than n4/5 (outside S3) or it belongs to S3. The former have total degree less than n4/5 log2 n, whereas the latter have total degree at most ǫn/10 (since (Dǫ3) does not hold). Hence, there are at most n4/5 log2 n + ǫn/10 ≤ ǫn/5 edges at distance 2 from v. Similarly, there are at most n4/5k +ǫn/10 ≤ ǫn/5 edges with one endpoint in N(u) ∩ S1. Since (Dǫ1) holds, there are at least ǫn− 2ǫn/5 ≥ ǫn/2 edges xy with x ∈ S1 \ N(u) and y ∈/ N(v). Performing a {xy,uv}-switch, we

obtain a graph in Fk+1. We conclude that there are at least ǫd(u)n/4 switches that transform G into a graph in Fk+1.

If G is in Fk+1, there are at most (k + 1) · dn¯ switches that transform it into a graph in Fk. Therefore, for every 0 ≤ k < 2K, we obtain

4(k + 1)dn¯

- 1

![image 232](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile232.png>)

- 2 · P[Fk+1] .


ǫd(u)n · P[Fk+1] ≤ Since u ∈ S1, we have d(u) ≥ log2 n and we obtain

P[Fk] ≤

![image 233](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile233.png>)

K−1

P[Fk] ≤ 2−KP[F2K] ≤ n−2 .

k=0

A union bound over all vertices u ∈ S1 completes the proof.

- Lemma 27. Suppose n ∈ N and 1/n ≪ p,1/d¯ ≤ 1. Let V be a set of size n and let D be a degree sequence on V with ΣD ≤ dn¯ . For R ⊆ V the following holds. Conditional on δ(GD[R]) ≥ 200log n/p, the probability that GDp [R] is connected is 1 − o(1). Proof. Let N := |R|. Our proof strategy is to show that with high probability for every possible


partition (A,B) of R, there are edges between A and B in GDp . Let (A,B) be a partition of R such that α := |A|/N and α ≤ 1/2. Let K := ⌊2αN log n/p⌋.

For every 0 ≤ k ≤ 2K, let Fk be the set of graphs G with degree sequence D such that δ(G[R]) ≥ 200log n/p and there are exactly k edges between A and B. In order to give an upper bound on

P[Fk], we will consider switches between Fk and Fk+2.

Let G ∈ Fk. We claim that there exist two subsets A′ ⊆ A and B′ ⊆ B with |A′| ≥ |A|/2 and |B′| ≥ |B|/2 such that for every u ∈ A′ (and every y ∈ B′), there are at least 100log n/p edges from u to A (and from y to B). We prove this claim for A, because the latter case is similar. Our assumption is that 0 ≤ k ≤ 2K ≤ 4αN log n/p and δ(G[R]) ≥ 200log n/p. Let A′′ ⊆ A be the subset that consists of all those vertices u such that dG[A](u) < 100log n/p. If |A′′| ≥ |A|/2 = αN/2, then

100log n p

4αN log n p ≥ 2K ≥ k,

αN 2 ·

>

e(A,B) >

![image 234](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile234.png>)

![image 235](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile235.png>)

![image 236](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile236.png>)

which is a contradiction. Therefore |A′′| < |A|/2, and setting A′ = A \ A′′ we have |A′| = |A \ A′′| ≥ |A|/2. Similarly, we set B′ = B \ B′′.

Next we claim that the edges of G[A] can be oriented in such a way so that every vertex in A′ has out-degree at least 48log n/p in A. To obtain such an orientation, start consistently orienting the edges of undirected cycles in G[A] until the undirected graph induces a forest. Afterwards iteratively and consistently orient maximal undirected paths in this forest. If so, the out-degree of a vertex in A is at least the in-degree minus 1. Since dG[A](u) ≥ 100log n/p for every vertex

- u ∈ A′, the vertex u has at least 50log n/p − 1 ≥ 48log n/p out-neighbours. Similarly, one can also orient the edges of G[B] in such a way that every vertex in B′ has out-degree at least 48log n/p in B.


For each vertex in u ∈ A′, select a set E(u) of exactly 48log n/p directed edges from u to a vertex in A, and analogously select E(y), for each y ∈ B′. We will only count the (possible) {uv,xy}-switches with u ∈ A′, y ∈ B′, uv ∈ E(u) and yx ∈ E(y). For the switch to be valid, we insist on ux,vy ∈/ E(G). Each edge ab with a ∈ A,b ∈ B can only invalidate switches of the form {av,by} with (a,v) ∈ E(a) and of the form {ua,xb} with (b,x) ∈ E(b); that is, one edge ab invalidates at most

48N log n p

|E(a)| · (1 − α)N + |E(b)| · αN =

![image 237](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile237.png>)

switches. Hence in total the edges between A and B block at most

192αN2 log2 n p2

48N log n p ≤

2K ·

![image 238](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile238.png>)

![image 239](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile239.png>)

possible switches. Recall that |A′| ≥ |A|/2, |B′| ≥ |B|/2. Thus, by using 1 − α ≥ 1/2, there are at least

192αN2 log2 n p2 ≥

96αN2 log2 n p2

(1 − α)N 2 ·

αN 2 ·

48log n p ·

48log n p −

,

![image 240](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile240.png>)

![image 241](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile241.png>)

![image 242](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile242.png>)

![image 243](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile243.png>)

![image 244](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile244.png>)

![image 245](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile245.png>)

switches that transform the graph G into a graph in Fk+2. Since we only switch edges with both endpoints in R, the minimum degree in the graph induced by R stays the same.

Consider a graph in Fk+2. Clearly, there are at most (k + 2)2 switches that transform G into a graph in Fk. Therefore, for every 0 ≤ k ≤ 2K − 2, we conclude

p2(k + 2)2 96αN2 log2 n · P[Fk+2] ≤

1 4 · P[Fk+2] .

P[Fk] ≤

![image 246](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile246.png>)

![image 247](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile247.png>)

We conclude that the probability there are less than K edges in GD between A and B is small, namely

K−1

- (48) P[Fk] ≤ 2 · 4−K/2(P[F2K] + P[F2K−1]) ≤ 2−K+1 .

If k ≥ K, then P[e(Gp[A,B]) = 0 | Fk] ≤ (1 − p)K. Therefore, provided δ(G[R]) ≥ 200log n/p, the probability that e(GDp [A,B]) = 0 is at most (1 − p)K + 2−K+1 ≤ e−32αN logn, where we used (48) and that 1 − p ≤ e−p.

![image 248](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile248.png>)

To conclude the proof of the lemma, we use a union bound over all partitions (A,B) of R.

Since for every 1 ≤ a ≤ N/2, there are Na ≤ ealogN partitions with |A| = a. Conditional on δ(G[R]) ≥ 200log n/p, the probability that GDp [R] is disconnected is at most

N/2

a=1 R=A∪B

|A|=a

P[e(GDp [A,B]) = 0] ≤

N/2

a=1

ealogNe−32alogn ≤

![image 249](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile249.png>)

N/2

a=1

e−21alogn = o(1) .

![image 250](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile250.png>)

- 9.3. Proof of Proposition 10. In this section we use the results from the two previous subsections to conclude the proof of Proposition 10. Let p,δ,ǫ and d¯ be as in the statement. Let n be large enough in terms of these parameters. Let V be a set of size n. Let D be a degree sequence on V with ΣD ≤ dn¯ . Recall that S1 = {u ∈ V : d(u) ≥ log2 n}, S2 = {u ∈ V : d(u) ≥ n1/3} and S3 = {u ∈ V : d(u) ≥ n4/5}. Proposition 10 assumes that D satisﬁes (Dǫ1).


- Case 1: Suppose D also satisﬁes (Dǫ3), that is, u∈S


3

d(u) ≥ ǫn/10. Let s ≥ 100 be the smallest integer such that δ > 2cs, where c is the constant given by Corollary 23 for our choice of p and d¯. Set γ1 := ǫp/(20s). If |S3| < s, then there exists a vertex u ∈ S3 with d(u) ≥ 2γ1n/p, because D satisﬁes (Dǫ3). This implies, by a simple application of Chernoﬀ’s inequality, that GDp contains a star of order γ1n with centre u, in particular, GDp contains a component of order at least γ1n.

Suppose now that |S3| ≥ s. Let A1 be the event that GDp [S3] is connected. Then, by deﬁnition of s and by Corollary 23,

P[A1] ≤

![image 251](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile251.png>)

δ 2

![image 252](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile252.png>)

- (49) .


k=0

Let A2 be the event that every vertex in S2 \ S3 has a neighbour in S3 and let A3 be the event that |N(S2) ∩ T| ≤ ǫ2n. Then by Lemmas 24 and 25,

P[A2 ∪ A3] ≤ 2n−1.

![image 253](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile253.png>)

![image 254](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile254.png>)

- Let γ2 := p2ǫ2n/3. We will show that P[L1(GDp ) > γ2n | A2,A3] ≥ 1 − δ. If |N(S3) ∩ T| ≥ ǫ2n/2, then a straightforward application of Chernoﬀ’s inequality combined


with (49) shows that there is a component of order at least pǫ2n/3 ≥ γ2n in GDp with probability at least 1 − δ.

If |N(S3) ∩ T| ≤ ǫ2n/2, then |N(S2 \ S3) ∩ T| ≥ ǫ2n/2. Let F be a forest in GD such that F contains N(S2 \ S3) ∩ T, for every vertex x1 ∈ N(S2 \ S3) ∩ T, there is a path x1x2x3 in F such that x2 ∈ S2 \ S3 and x3 ∈ S3, and among all such forests, F contains as few as edges as

possible. To complete the case when D satisﬁes (Dǫ3), we will show that GDp [S3] ∪ Fp contains a component of order at least γ2n with probability at least 1 − δ. Consider a realisation of GD that satisﬁes A2 ∩ A3. Observe ﬁrst that whether a certain edge in F is present in Fp changes the number of vertices in N(S2 \ S3) ∩ T that are connected via Fp to S3 by at most n4/5. Thus assuming A1 holds, a straightforward application of McDiarmid’s inequality (Lemma 7) shows that there is a component of order at least p2 · ǫ2n/3 = γ2n in GDp [S3] ∪ Fp with probability at least 1 − n−1. This together with (49), completes the case when D satisﬁes (Dǫ3).

- Case 2: Now, suppose that D does not satisfy Condition (Dǫ3). Since it satisﬁes (Dǫ1), by Lemma 26, we obtain


ǫ 16d¯

P δ(GD[S1]) ≥

log2 n = 1 − o(1). Together with Lemma 27 where S1 plays the role of R, we conclude that

![image 255](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile255.png>)

- (50) P[GDp [S1] is connected] = 1 − o(1).


In order to show that GDp contains a giant component, we will show that |N(S1) ∩ T| is large. Let K := ⌊ǫn/(128d¯)⌋. For every 0 ≤ k ≤ 2K, let Fk be the set of graphs with degree sequence D such that |N(S1) ∩ T| = k.

Let G ∈ Fk. Using (47) and δ(G) ≥ 1, there are at least |T| − k ≥ 2n/3 − k ≥ n/2 choices for an edge xy with x ∈ T \ N(S1). Observe that d(y) ≤ log2 n, since x ∈/ N(S1). Also, since x,y ∈/ S1 and D does not satisfy (Dǫ3), we claim that there are at most

ǫn 5

3d¯log2 n + n4/5 log2 n + ǫn/10 ≤

![image 256](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile256.png>)

edges incident to a neighbour of either x or y. Indeed, the number of edges incident to a neighbour of x is bounded by 3d¯log2 n, as x has no neighbours inside S1. Now, the neighbours of y are classiﬁed either as the neighbours that belong to S3 or those that do not. Since property (Dǫ3) does not hold, and there are at most ǫn/10 edges incident to any vertex in S3, there are at most ǫn/10 edges incident to the ﬁrst class of neighbours. Regarding the latter class of neighbours, there are at most log2 n of them (as y  ∈ S1) and each has degree at most n4/5. Thereby, there at most n4/5 · log2 n such edges. Hence our claim holds.

Let uv be an edge such that u ∈ S1, v ∈/ N(y), and either v ∈/ T or if v ∈ T, then there exists a u′ ∈ S1 with u′v ∈ E(G). Since u∈S

d(u) ≥ ǫn, there are at least ǫn − k − ǫn/5 ≥ ǫn/2 such edges. Hence, the total number of {xy,uv}-switches that transform G into a graph in Fk+1∪Fk+2 is at least ǫn2/4 (we transform G into a graph satisfying Fk+2 if v ∈ S1 and y ∈ T \ N(S1)).

1

If G ∈ Fk+1 ∪ Fk+2, then there are at most (k + 2)dn¯ switches that transform G into a graph in Fk. As before, for every 0 ≤ k ≤ 2K − 2, this implies

4(k + 2)dn¯ ǫn2 · (P[Fk+1] + P[Fk+2]) ≤

1 4 · max{P[Fk+1],P[Fk+2]} .

P[Fk] ≤

![image 257](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile257.png>)

![image 258](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile258.png>)

Therefore,

K−1

P[Fk] ≤ 2−KP[F2K] ≤ 2−K = o(1) . Hence

k=0

P[|N(S1) ∩ T| ≥ ⌊ǫn/(128d¯)⌋] = 1 − o(1) .

- Let γ3 := ǫp/(130d¯). The Chernoﬀ bound (Lemma 6) implies that


(S1) ∩ T| ≥ pǫn/(130d¯)] = 1 − o(1) .

P[|NGD

p

Together with (50), this implies P[L1(GDp ) ≥ γ3n] ≥ 1 − δ. Setting γ := min{γ1,γ2,γ3}, we obtain

P[L1(GDp ) ≥ γn] ≥ 1 − δ .

10. Sequences of degree sequences: proof of Theorem 1

Let D = (Dn)n≥1 be a sequence of degree sequences with Dn = (d(1n),... ,d(nn)). For the sake of simplicity, we write Dn = (d1,... ,dn) and W(c) := W(c,Dn). Set

di(di − 1) i∈V \W(c) di

dc,n := max i∈V\W(c)

,1 .

![image 259](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile259.png>)

We assume that dc := limn→∞ dc,n exists for every c ≥ 1 and that d is such that d = sup

dc,n ∈ [1,∞) . We deﬁne the critical probability as in (6) by

dc = sup c≥1

lim

n→∞

c≥1

di i∈V \W(c) di(di − 1)

1 dc,n

pcrit(c,Dn) = min i∈V \W(c)

,1 =

.

![image 260](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile260.png>)

![image 261](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile261.png>)

We start with the proof of part (i) and begin with a claim which states that for every large c we can replace 1/d by pcrit(c,Dn) provided n is large enough in terms of c.

Claim 1. For every ǫ ∈ (0,1/2), there exists cǫ such that for every c ≥ cǫ, there exists nǫ,c such that for every n ≥ nǫ,c, we have

- - if p < (1 − ǫ)d1, then p < 1 − 4ǫ pcrit(c,Dn).

![image 262](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile262.png>)

![image 263](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile263.png>)

- - if p > (1 + ǫ)d1, then p > 1 + 4ǫ pcrit(c,Dn).


![image 264](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile264.png>)

![image 265](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile265.png>)

Proof. Note ﬁrst that dc,n is non-decreasing with respect to c; that is, dc2,n ≥ dc1,n for c2 ≥ c1. This implies that dc2 = limn→∞ dc2,n ≥ limn→∞ dc1,n = dc1. Hence (dc)c≥1 is a monotone nondecreasing sequence and it converges to d. Furthermore, d < ∞ by assumption. Thus, for any ǫ > 0, there exists cǫ such that for any c > cǫ, we have

(1 − ǫ2/2)d < dc ≤ d. In turn, given c, there exists nǫ,c such that for any n > nǫ,c, we have

(1 − ǫ2/2)dc < dc,n < (1 + ǫ2)dc. Therefore, for every c ≥ cǫ and every n ≥ nǫ,c we directly obtain

- (51) (1 − ǫ2)d < dc,n < (1 + ǫ2)d. Moreover, if ǫ < 1/2 and p < (1 − ǫ)1d, then

![image 266](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile266.png>)

p < (1 − ǫ)(1 + ǫ2)

1 dc,n

![image 267](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile267.png>)

< (1 − ǫ/4)

1 dc,n

![image 268](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile268.png>)

.

Similarly, if ǫ < 1/2 and p > (1 + ǫ)d1, then p > (1 + ǫ)(1 − ǫ2)

![image 269](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile269.png>)

1 dc,n

![image 270](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile270.png>)

> (1 + ǫ/4)

1 dc,n

![image 271](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile271.png>)

.

In what follows we will select c1, c2 and η such that the hypotheses of Theorem 2 are satisﬁed. By the strong uniform integrability assumption, for any ǫ > 0, there exists a c′ǫ ∈ N such that for every c ≥ c′ǫ, there exists n′ǫ,c such that for n ≥ n′ǫ,c we have

- (52) j∈W(c)


ǫ2 c · n .

dj ≤

![image 272](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile272.png>)

We may assume that for ﬁxed ǫ and all c1 ≤ c2, we have nǫ,c1 ≤ nǫ,c2 and n′ǫ,c2 ≤ nǫ,c2 as we simply can replace nǫ,c2 by maxc′≤c2{nǫ,c′,n′ǫ,c′}. We may also assume that ǫ < (64dd¯)−1. We choose c1 := max{cǫ,c′ǫ}. Suppose c > c1 and n ≥ nǫ,c. Next we prove that A2(ǫ/4,c1,c) holds

for a suitable c. Note that this condition is only needed in Theorem 2 (ii). If dc1,n ≤ (1 + ǫ/5),

- then p > (1 + ǫ)/d implies (by Claim 1 and c1 ≥ cǫ) that


ǫ 4

1 dc1,n

p > 1 +

> 1,

![image 273](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile273.png>)

![image 274](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile274.png>)

and there is nothing to prove. Thus, we may assume that dc1,n > (1 + ǫ/5). Hence, dc,n =

i∈V \W(c) di(di−1)

i∈V\W(c) di ≤ c for any c ≥ c1 and n suﬃciently large in terms of c. It follows that

![image 275](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile275.png>)

dj(dj − 1) =

j∈W(c1)\W(c)

dj(dj − 1) −

dj(dj − 1)

j∈V \W(c)

j∈V \W(c1)

dj − dc1,n

dj

= dc,n

j∈V \W(c1)

j∈V \W(c)

= (dc,n − dc1,n)

dj + dc,n

j∈V \W(c1)

(52)

≤ (dc,n − dc1,n)dn¯ + ǫ2dn

(51)

≤ 3ǫ2ddn¯ . This in turn implies that

dj

j∈W(c1)\W(c)

d2j =

j∈W(c1)\W(c)

dj(dj − 1) +

dj

j∈W(c1)\W(c)

j∈W(c1)\W(c)

≤ 3ǫ2ddn¯ +

dj

j∈W(c1)

(52) < 4ǫ2ddn¯ ≤

ǫ/4 4 · n . Thus A2(ǫ/4,c1,c) holds for all c ≥ c1 and n ≥ nǫ,c. Note that c1 only depends on ǫ. Let η = η(γ,ǫ/4,d¯) be as in Theorem 2. Using again Condition (b), for n ≥ nη,c2 we have

![image 276](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile276.png>)

η c2 · n ,

dj ≤

![image 277](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile277.png>)

j∈W(c2)

and thus A1(η,c2) is satisﬁed (even if dc1,n ≤ (1 + ǫ/5)).

Also let ρ = ρ(ǫ/4,c1) be the constant provided by Theorem 2, which in this case only depends on ǫ; that is, we can choose γ ≤ ρ. Let n be larger than max{nη,c2,nǫ,c2} and the n0 given by Theorem 2 for the parameters ǫ/4,γ,c1,c2,d¯. By Claim 1, we can apply Theorem 2 with ǫ/4 to Dn to conclude that

if p < (1 − ǫ)1d, then P[L1(GDp n) > γn] = o(1), if p > (1 + ǫ)1d, then P[L1(GDp n) > ρn] = 1 − o(1).

![image 278](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile278.png>)

![image 279](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile279.png>)

We proceed to the proof of Theorem 1 (ii). Our aim is to apply Theorem 3. Let us check that the hypotheses are satisﬁed. Given δ,p and d¯, let K be the constant provided by Theorem 3.

Suppose ﬁrst that d = ∞. Since supc≥1 dc = limc→∞ dc = d = ∞, there exists cK such that for every c ≥ cK, we have

lim

dc,n = dc > 2K .

n→∞

Similarly, there exists nK,c such that dc,n ≥ K for every n ≥ nK,c. For c ≥ max{cK,2d¯} and n ≥ nK,c, we obtain

K 2 · n ,

d2j ≥

dj(dj − 1) ≥ K

dj ≥

![image 280](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile280.png>)

j∈V \W(c)

j∈V \W(c)

j∈V \W(c)

and so A2(K,0,c) does not hold. Thus Theorem 3 leads to the desired conclusion.

Suppose now that d < ∞ but the sequence robustly fails the strong uniform integrability assumption. Let c0 be such that f(c) ≥ K for every c ≥ c0. As f(c) → ∞ as c → ∞ such a c0 exists. This in turn immediately implies that A1(K,c) does not hold provided n is large enough. Again, Theorem 3 leads to the desired conclusion and this completes the proof.

We close this section with the following remark. Suppose that limn→∞ ni/n =: λi < ∞ for all i ≥ 1, that i≥1 λi = 1, and that i≥1 iλi < ∞. Then

i(i − 1)λi i≥1 iλi

d = i≥1

.

![image 281](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile281.png>)

This recovers the results obtained by the ﬁrst author [10], Janson [13], and Bollob´s and Riordan [8].

11. Application: power-law degree distributions

Power law degree distributions have attracted considerable interest as they are one of the usual characteristics of complex networks [2]. Roughly speaking, in such degree sequences the fraction of vertices that have degree equal to k (when k is large) scales like k−γ, for some γ > 0.

A variety of random graph models which exhibit a power law degree distribution have been introduced in the last 15 years, mainly, in search for a sound model for complex networks. Among other properties, robustness is a central property that has been considered in this context; that is, how robust a random network is if several of its edges or its vertices fail.

In several random graph models with a power law degree distribution, it has been observed that if γ > 3, then there exists a critical value pcrit (which is bounded away from 0) for the appearance of a giant component in the bond percolation process. However, if γ ≤ 3, for any ﬁxed p > 0 (that is, independent of the order of the random graph), a giant component survives the random deletions with high probability. This behaviour has been observed in diverse random graph models that give rise to power-law degree distributions such as the conﬁguration model ([3], Corollary 2.5), the preferential attachment model [7] and random graphs on the hyperbolic plane [9].

We now apply Theorem 1 in this context. This recovers a known result for power law sequences but also exempliﬁes how our results can be used for particular degree sequences. Consider a sequence of degree sequences (Dn)n∈N, where Dn is a feasible degree sequence on [n] and assume that it satisﬁes the following: for k ≥ 1, let nk denote the number of vertices of degree k in Dn, then there exist positive constants γ,λ1,λ2,k0 > 0 such that for every k ≥ k0, we have

λ2 kγ

nk n ≤

λ1 kγ ≤

. If so, we say that Dn follows a power law distribution with exponent γ.

![image 282](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile282.png>)

![image 283](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile283.png>)

![image 284](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile284.png>)

In this section we show that power law distributions, as deﬁned here, show the same behaviour around γ = 3. As before, we write Dn = (d1,... ,dn) and W(c) := W(c,Dn) = {i : di ≥ c} for every c ≥ 1.

Let Dn follow a power law distribution with γ > 3. Then, there exists λ′2 > 0 such that for every c2 ≥ k0, we have

λ′2 cγ2−2

n c2

· n = λ′2c32−γ ·

k1−γ ≤

knk ≤ λ2n

di =

,

![image 285](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile285.png>)

![image 286](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile286.png>)

k≥c2

k≥c2

i∈W(c2)

and thus, Dn satisﬁes A1(λ′2c23−γ,c2). Moreover, there exists λ′′2 > 0 such that for all c2 ≥ c1 ≥ k0, we have

c2−1

c2−1

k2−γ ≤ λ′′2c31−γ · n ,

k2nk ≤ λ2n

d2i =

k=c1

k=c1

i∈W(c1)\W(c2)

that is, Dn satisﬁes A2(4λ′′2c13−γ,c1,c2).

Provided that c1 and c2 are large enough and γ > 3 (so the ﬁrst parameters in conditions A1 and A2 are arbitrarily small), we can apply Theorem 2 to determine a quantity pcrit > 0 that is bounded away from 0, such that bond percolation in GDn has a threshold at pcrit.

Now, let Dn follow a power law distribution with 2 < γ < 3. Then, there exists λ′1 > 0 such that for every c ≥ k0, we have

n c

k1−γ ≥ λ′1c2−γ · n = λ′1c3−γ ·

knk ≥ λ1n

,

di =

![image 287](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile287.png>)

k≥c

k≥c

i∈W(c)

that is, Dn does not satisfy A1(λ′1c3−γ,c). Provided that c1 is large enough (so the ﬁrst parameter in condition A1 is arbitrarily large), we

can apply Theorem 3 to show that bond percolation in GDn does not have a positive threshold. Note that if γ ≤ 2, then the average degree of GDn is unbounded and our results do not apply. We ﬁnally state the “limit” version of the result for Dn that follows a power law distribution.

Suppose that there exists c > 0 such that for all k ≥ 1, we have lim

nk n

= ck−γ .

![image 288](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile288.png>)

n→∞

If γ > 3, then d < ∞, while if γ < 3, then d = ∞. So, Theorem 1 implies that in the former case we have pcrit = 1/d > 0, whereas in the latter case pcrit = 0.

It is worth to stress that our results do not provide any meaningful information at γ = 3.

12. Concluding remarks We ﬁnish the paper with some remarks on our results.

- 1) Theorem 3 provides a statement that holds only with probability at least 1−δ. The only part of its proof that does not hold with high probability is Corollary 23. This makes it easy to construct degree sequences that show that this cannot be improved. For a given ρ > 0, let us consider the following degree sequence on n vertices (large enough in terms of ρ). Let a := ⌊2/ρ⌋ and suppose a divides n − a. Consider the degree sequence with a vertices of degree (n − a)/a + a − 1, and n − a vertices of degree 1. This degree sequence is feasible and the only graph (up to isomorphism) with this degree sequence consists of a clique of size a where each of its vertices is adjacent to n/a − 1 vertices of degree 1.

With positive probability independently of n all a2 edges inside the clique of size a fail to percolate in GDp . If so, L1(GDp ) ≤ ρn/2. Thus for every p ∈ [0,1), we have

P[L1(GDp ) < ρn] > δ(ρ,p) . Observe that these degree sequences also do not satisfy A1(K,c) for all c ≥ 2K.

- 2) In [15], a special role is given to vertices of degree 2. However, by considering bond percolation this special situation never appears. If most of the edges are incident to vertices of degree 2 after the bond percolation, then p ≈ 1 and almost all vertices have degree 2 already before the percolation. In this case set pcrit := 1. Let W be the set of

vertices with degree diﬀerent from 2. If i∈W di = o(n), then |N[W]| = o(n). For every ǫ > 0 and every p < 1 − ǫ, it follows that,

i∈V \N[W]

di(p(di − 1) − 1) = (n − |N[W]|)2(p − 1) < −ǫn .

Using the ﬁrst part of Proposition 9 we obtain that GDp has no giant component with high probability, and thus pcrit = 1.

- 3) The previous remark is a particular case of the case ΣD/n → ∞. While it might seem


natural that pcrit(D) → 0, here we provide an example for which ΣD/n → ∞ and pcrit is bounded away from 0.

Consider the degree sequence D formed by n2/3 vertices of degree n2/3 and n − n2/3 vertices of degree 1. The critical condition in [15] shows that GD has a giant component with high probability. However, it is easy to see that, with high probability, GDp has at least (1 − 2p)n isolated vertices and thus we cannot expect to have a component of order

larger than 2pn. If p → 0 (as n → ∞), then GDp does not have a giant component with high probability.

References

- 1. W. Aiello, F. Chung, and L. Lu, A random graph model for massive graphs, Proceedings of the thirty-second annual ACM symposium on Theory of computing, ACM, 2000, pp. 171–180.
- 2. R. Albert and A.-L. Barab´asi, Statistical mechanics of complex networks, Reviews of modern physics 74 (2002), 47.
- 3. E. Baroni, R. van der Hofstad, and J. Komj´thy, Nonuniversality of weighted random graphs with inﬁnite variance degree, Journal of Applied Probability 54 (2017), no. 1, 146—164.
- 4. E.A. Bender and E.R. Canﬁeld, The asymptotic number of labeled graphs with given degree sequences, J. Combinatorial Theory Ser. A 24 (1978), 296–307.
- 5. S. Boccaletti, V. Latora, Y. Moreno, M. Chavez, and D.-U. Hwang, Complex networks: Structure and dynamics, Physics reports 424 (2006), 175–308.
- 6. B. Bollob´s, A probabilistic proof of an asymptotic formula for the number of labelled regular graphs, European J. Combin. 1 (1980), 311–316.
- 7. B. Bollob´s and O. Riordan, Robustness and vulnerability of scale-free random graphs, Internet Math. 1 (2003), 1–35.
- 8. , An old approach to the giant component problem, J. Combin. Theory Ser. B 113 (2015), 236–260.

![image 289](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile289.png>)

- 9. E. Candellero and N. Fountoulakis, Bootstrap percolation and the geometry of complex networks, Stochastic Process. Appl. 126 (2016), 234–264.
- 10. N. Fountoulakis, Percolation on sparse random graphs with given degree sequence, Internet Mathematics 4

(2007), 329–356.

- 11. A. Goerdt, The giant component threshold for random regular graphs with edge faults, Theoret. Comput. Sci. 259 (2001), 307–321.
- 12. H. Hatami and M. Molloy, The scaling window for a random graph with a given degree sequence, Random Structures Algorithms 41 (2012), 99–123.
- 13. S. Janson, On percolation in random graphs with given vertex degrees, Electron. J. Probab. 14 (2009), 87–118.
- 14. S. Janson and M.J. Luczak, A new approach to the giant component problem, Random Structures Algorithms 34 (2009), 197–216.
- 15. F. Joos, G. Perarnau, D. Rautenbach, and B. Reed, How to determine if a random graph with a ﬁxed degree sequence has a giant component, Probab. Theory Related Fields 170 (2018), 263–310.
- 16. M. Kang and T. G. Seierstad, The critical phase for random graphs with a given degree sequence, Comb. Probab. Comput. 17 (2008), 67–86.
- 17. C. McDiarmid, Concentration, Probabilistic methods for algorithmic discrete mathematics, vol. 16, Springer, 1998, pp. 195–248.
- 18. M. Molloy and B. Reed, A critical point for random graphs with a given degree sequence, Random Structures Algorithms 6 (1995), 161–180.
- 19. , The size of the giant component of a random graph with a given degree sequence, Comb. Probab. Comput. 7 (1998), 295–305.

![image 290](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile290.png>)

- 20. , Graph colouring and the probabilistic method, vol. 23, Springer Science & Business Media, 2013.

![image 291](<2016-fountoulakis-percolation-random-graphs-fixed_images/imageFile291.png>)

- 21. A. Nachmias and Y. Peres, Critical percolation on random regular graphs, Random Structures Algorithms 36

(2010), 111–148.

- 22. M. E. J. Newman, The structure and function of complex networks, SIAM review 45 (2003), 167–256.
- 23. B. Pittel, Edge percolation on a random regular graph of low degree, The Annals of Probability 36 (2008), 1359–1389.
- 24. O. Riordan, The phase transition in the conﬁguration model, Comb. Probab. Comput. 21 (2012), 265–299.
- 25. B. Sudakov and J. Vondrak, A randomized embedding algorithms for trees, Combinatorica 30 (2010), 445–470.
- 26. N. Wormald, Some problems in the enumeration of labelled graphs, University of Newcastle, 1979, PhD thesis.
- 27. N. C. Wormald, Models of random regular graphs, Surveys in combinatorics, 1999 (Canterbury), London Math. Soc. Lecture Note Ser., vol. 267, Cambridge Univ. Press, Cambridge, 1999, pp. 239–298.


Version January 12, 2022

Nikolaos Fountoulakis <n.fountoulakis@bham.ac.uk> School of Mathematics, University of Birmingham, Birmingham United Kingdom

Felix Joos <joos@informatik.uni-heidelberg.de> Institute for Computer Science, Heidelberg University, Heidelberg Germany

Guillem Perarnau <guillem.perarnau@upc.edu> IMTech, Universitat Polit`ecnica de Catalunya, and Centre de Recerca Matema`tica, Barcelona Spain

