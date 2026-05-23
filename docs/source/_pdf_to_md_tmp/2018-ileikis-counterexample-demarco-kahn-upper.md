arXiv:1809.09595v2[math.PR]3Jun2019

A Counterexample to the DeMarco-Kahn Upper Tail Conjecture

Matas Sileikisˇ ∗ and Lutz Warnke† 9 October 2018; revised February 8, 2019

Abstract

Given a ﬁxed graph H, what is the (exponentially small) probability that the number XH of copies of H in the binomial random graph Gn,p is at least twice its mean? Studied intensively since the mid 1990s, this so-called infamous upper tail problem remains a challenging testbed for concentration inequalities. In 2011 DeMarco and Kahn formulated an intriguing conjecture about the exponential rate of decay of P(XH (1 + ε)EXH) for ﬁxed ε > 0. We show that this upper tail conjecture is false, by exhibiting an inﬁnite family of graphs violating the conjectured bound.

# 1 Introduction

Understanding the distribution of subgraph counts is one of the central topics in random graph theory. Ever since the seminal paper of Erdo˝s and R´enyi [11] from 1960 it has served as a rich source of intriguing probabilistic challenges and conjectures — repeatedly stimulating the development of new insights and tools in combinatorial probability theory (in particular concentration inequalities).

In this note we focus on the tails of the number XH = XH(n,p) of copies of a ﬁxed graph H in the binomial random graph Gn,p, which have been intensively studied for decades. Indeed, in the 1980s the need for exponentially small tail probabilities emerged in applications, and the behaviour of the lower tail P(XH (1−ε)EXH) was eventually resolved by the celebrated Janson’s inequality [16, 15, 24, 22]. In the early 1990s the need for also understanding the exponential decay of the upper tail P(XH (1+ε)EXH) became evident, and since then the following ‘infamous’ upper tail problem has proven to be much more challenging than its lower tail counterpart (see [20] and [15, 25] as well as [33, Section 4.8] and [21, Problem 6.1]).

Problem 1 (Upper tail problem for subgraph counts). Given a ﬁxed graph H with eH 1 edges, determine for ﬁxed ε > 0 and arbitrary p = p(n) ∈ (0,1) the order of magnitude of

− log P(XH (1 + ε)EXH). (1)

In 2002 Janson, Oleszkiewicz and Ruci´nski [18] ﬁnally determined the exponential rate of decay (1) up to a factor of O(log(1/p)). This breakthrough solved Problem 1 for constant edge-probabilities p ∈ (0,1), but closing the logarithmic gap for p = o(1) remained an elusive technical challenge.

Shortly after the upper tail problem was settled for triangles H = K3 [5, 8], in 2011 DeMarco and Kahn solved the more general case of ﬁxed-size cliques H = Kr with r 3 [9], and also formulated a plausible conjecture on the general solution of Problem 1; see Conjecture 1 below. This ‘upper tail conjecture’ has been veriﬁed for large p = p(n) of form p n−δ

via large deviation machinery [6, 23, 2, 10], and for small p = p(n) of form p n−v/e(log n)C

H

for so-called strictly balanced graphs H [31, 28, 34] (where eF/vF < eH/vH for any non-empty F H); see also [1, 27, 28, 30] for further supporting results. In fact, this conjecture was also described as ‘likely to be true’ in the recent random graphs book by Frieze and Karo´nski [12, Section 5.4].

H

![image 1](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile1.png>)

∗Department of Theoretical Computer Science, Institute of Computer Science of the Czech Academy of Sciences, 182 07 Prague, Czech Republic. E-mail: matas.sileikis@gmail.com. With institutional support RVO:67985807. Research supported by the Czech Science Foundation, grant number GJ16-07822Y.

†School of Mathematics, Georgia Institute of Technology, Atlanta GA 30332, USA. E-mail: warnke@math.gatech.edu. Research partially supported by NSF Grant DMS-1703516 and a Sloan Research Fellowship.

In this note we show that the 7-year-old DeMarco–Kahn upper tail conjecture for subgraph counts is false, by exhibiting an inﬁnite family of graphs which violate the conjectured behavior of the upper tail (1); see Theorem 1 below. On a conceptual level, our results shed new light on the upper tail behaviour for small edge-probabilities p = p(n), indicating that close to the threshold of appearance the reason for having ‘too many’ copies of H can be more complicated than previously anticipated (see Sections 1.2 and 4). In retrospect this might perhaps not seem so surprising, taking into account that at the appearance threshold the limiting distribution of XH can be quite complicated, as discovered in the 1980s [3, 14, 4, 26].

- 1.1 Main result


Turning to the details, we now formally state1 the upper tail conjecture from [9], which proposes a compelling solution to Problem 1. Let µH := EXH, σH2 := VarXH, and mH := maxF⊆H:v

F 1 eF/vF, as usual. As pointed out in [18, 9, 27, 12], to avoid degenerate behaviour of the upper tail it is natural and convenient to assume (i) that p = p(n) is above the appearance threshold n−1/m

of H, and (ii) that (1 + ε)EXH is at most the number of copies of H in the complete graph Kn, which is equivalent to (1 + ε)pe

H

1.

H

Conjecture 1 (DeMarco and Kahn, 2011). Let H be a graph with eH 1 edges. For ﬁxed ε > 0 and any p = p(n) with n−1/m

< p (1 + ε)−1/e

we have

H

H

− log P (XH (1 + ε)EXH) = Θ min ΦH, MH log(1/p) , (2) where the implicit constants in (2) may depend on ε and H, with

ΦH = ΦH(n,p) := min

µG, (3)

G⊆H:eG 1

 

∗ G

µ1/α

G if p < n−1/∆

, n2p∆

min

H

G⊆H:eG 1

(4)

MH = MH(n,p) :=

if p n−1/∆

,

H

H



where ∆G is the maximum degree of G, and α∗G is the fractional independence number2 of G.

One conceptual contribution of the above conjecture was to enhance the exponent (2) by the ΦH term, whose inclusion only matters for p n−1/m

(log n)O(1) unless ∆H = 1 holds (cf. [18, Remark 8.3] and Section 1.2). Our main result shows that Conjecture 1 is false, by proving that there are inﬁnitely many graphs H

H

which violate the conjectured exponential rate of decay (2) close to the appearance threshold n−1/m

.

H

Theorem 1 (Counterexamples to Conjecture 1). There is an inﬁnite family H of graphs such that the following holds for any H ∈ H. There exists a constant cH > 0 such that for ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with n−1/m

(log n)c

≪ p ≪ n−1/m

we have

H

H

H

− log P (XH (1 + ε)EXH) = o min ΦH, MH log(1/p) . (5) Remark 2. Given H ∈ H, for ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with n−1/m

≪ p ≪ 1 we also have

H

− log P (XH (1 + ε)EXH) = o(ΦH). (6) The proof of Theorem 1 and Remark 2 is given in Section 2. As we shall see, it uses the family of graphs H illustrated in Figure 1, which are all connected and balanced (i.e., satisfy eH/vH = mH). Remark 2 demonstrates that their upper tail probabilities are signiﬁcantly larger than the lower tail probabilities for virtually all edge-probabilities p of interest, since [15, 22] gives under analogous assumptions that

− logP (XH (1 − ε)EXH) = Θ(ΦH).

We ﬁnd this complete separation of the decay of the two tails conceptually interesting (it was previously only known a bit above the appearance threshold, i.e., for n−1/m

log n ≪ p ≪ 1; see [18, Remark 8.3]).

H

![image 2](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile2.png>)

- 1In the spirit of earlier questions and examples in the area (see, e.g., [32, Section 4] and [21, Section 6]), DeMarco and Kahn formally stated [9, Conjecture 10.1] for ε = 1 only, tacitly assuming the necessary condition p (1 + ε)−1/eH . The natural variant (2) for arbitrary ﬁxed ε > 0 is of course also attributed to them; cf. [12, Section 5.4] and [8, Section 4]. In (4) we also use a simpliﬁed (but up to constant factors equivalent) deﬁnition of MH; cf. [9, (46)] and [18, Theorem 1.5 and Remark 1.6].
- 2The fractional independence number is deﬁned as α∗G := max v∈V (G) f(v), where maximum is taken over all functions f : V (G) → [0, 1] satisfying f(u) + f(v) 1 for every edge {u, v} ∈ E(G); see, e.g., [18, Appendix A].


- Figure 1: Examples of the graph Cℓ+r with (ℓ,r) = (3,2) and (ℓ,r) = (6,3), obtained by attaching r pendant


edges to some vertex of an ℓ-vertex cycle. Theorem 1 shows that any graph in H := {Cℓ+r : ℓ 3,r 2} is a counterexample to the DeMarco–Kahn upper tail conjecture (see Section 2 for the full details).

- 1.2 Discussion


- Conjecture 1 can be interpreted as an educated guess to a variant of the following question: what is the most likely way to get at least (1 + ε)EXH copies of H in Gn,p? Indeed, as we shall see, it is based on two diﬀerent mechanisms that each enforce XH (1 + ε)EXH in Gn,p, giving two lower bounds with exponents MH log(1/p) and ΦH. Hence (2) intuitively predicts that the dominating (more likely) mechanism determines the exponential decay of the upper tail, ignoring constant factors in the exponent.


The ﬁrst clustered mechanism is based on the idea that suitable ‘local’ clustering of the edges can enforce

many copies of H (e.g., a clique Kz contains z3 > 2 n3 p3 triangles for suitable z ≍ np). In particular, if F ⊆ Kn contains at least (1 + ε)EXH copies of H, then by simply enforcing F ⊆ Gn,p we obtain

P(XH (1 + ε)EXH) P(F ⊆ Gn,p) = pe

.

F

Janson, Oleszkiewicz and Ruci´nski [18] noted that one does not need to directly enforce copies of H: it is enough if F ⊆ Kn contains unusually many copies of some subgraph J ⊆ H (say at least 2(1+ε)EXJ many), since after planting F ⊆ Gn,p the rare upper tail event {XH (1+ε)EXH} becomes ‘typical’. By minimizing the number eF of edges over all such special graphs F ⊆ Kn, this eventually gives a lower bound of form

pΘ(M

H), (7)

P(XH (1 + ε)EXH | F ⊆ Gn,p)pe

P(XH (1 + ε)EXH) max

F

F⊆Kn

see [18, Theorems 1.5 and 3.1] for the full details. This explains the exponent MH log(1/p) in (2).

The second disjoint mechanism is based on many mutually exclusive ‘global’ conﬁgurations of the edges, which each contain many disjoint copies of H. Let DH,ε denote the event that Gn,p contains exactly k := ⌈(1 + ε)EXH⌉ disjoint copies of H (either vertex-disjoint or edge-disjoint), and write N = N(n,H) for the number of H-copies in Kn. Summing over distinct k-sets of disjoint H-copies, for strictly-balanced graphs this eventually gives a binomial-like lower bound in some range, which turns out to be roughly of form

P(XH (1 + ε)EXH) P(DH,ε) ≈

N k · pke

H

· (1 − pe

H

)N−k = exp −Θ(µH) ,

see [9, 27, 28] for the full details. As in the clustered mechanism, it turns out that we can again optimize the resulting bound over all relevant subgraphs J ⊆ H, eventually leading to a lower bound of form

P(XH (1 + ε)EXH) exp −Θ(ΦH) , (8)

see [27, Theorem 4.4] for the full details (note that, due to subgraphs consisting of a single edge, the optimization leading to (8) includes the mechanism which is based on enforcing Gn,p to have ‘too many edges’). This explains the exponent ΦH in (2). Alternatively, by combining the intuition that XH should have subgaussian tails (in some range) with the standard variance estimate

σH2 ≍ µ2H/ΦH (9) from [17, Lemma 3.5], for ﬁxed ε > 0 we again (heuristically) arrive at an exponent of order (εµH)2/σH2 ≍ ΦH.

A key message of Theorem 1 and our counterexamples from Sections 2–3 is that for some graphs H there is a yet another mechanism (which we tentatively call locally-disjoint mechanism), whose lower bound can beat both aforementioned mechanisms close to the appearance threshold n−1/m

. Remark 2 also shows that for certain graphs the disjoint mechanism (with exponent ΦH) never wins, complementing the known fact that the clustered mechanism (with exponent MH log(1/p)) never wins for matchings [18, 9].

H

- 1.3 Organization


The remainder of this note is organized as follows. In Section 2 we prove Theorem 1 and Remark 2, i.e., present a simple set of counterexamples and describe how they contradict the upper tail conjecture. In Section 3 we elaborate the basic idea: we describe a larger set of counterexamples, and also give a new lower bound for the upper tail. The ﬁnal Section 4 contains some concluding remarks and conjectures.

# 2 Simple counterexamples: Proof of Theorem 1 and Remark 2

In this section we prove Theorem 1 and Remark 2 by considering the graphs H = Cℓ+r illustrated in Figure 1, which are constructed from an ℓ-vertex cycle Cℓ by connecting r additional vertices to the same vertex of the cycle (so vH = eH = ℓ + r). These graphs have a history of exemplifying non-trivial behaviour of subgraph counts: (i) in 1987 Janson used Cℓ+2 to demonstrate that at the threshold XH can converge to complicated distributions [14, Section 10], and (ii) in 2000 Janson and Ruci´nski used C3+3 to demonstrate that near the threshold XH need not always have subgaussian tails [19, Example 6.14]. As we shall see, the following auxiliary result demonstrates yet another non-trivial behaviour of the graphs H = Cℓ+r, since the lower bound (10) will contradict Conjecture 1 (and establish Theorem 1). Note that mH = 1 and µH ≍ (np)ℓ+r.

Lemma 3. Given integers ℓ 3 and r 1, let H := Cℓ+r be the graph deﬁned above. For ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with 1 ≪ np ≪ n1/(1+ℓ/r) we have

P (XH (1 + ε)EXH) exp −O µ1H/r log(np) , (10) where the implicit constant in (10) may depend on ε and H.

One basic strategy for proving lower bounds is to enforce F ⊆ Gn,p for some graph F which itself contains at least (1 + ε)µH copies of H. For example, F := Cℓ+z contains zr (1 + ε)µH copies of H = Cℓ+r for suitable z ≍ (µH)1/r. Following [32, 18], by enforcing F on the ﬁrst vF vertices of Gn,p we would obtain

P(XH (1 + ε)µH) P(F ⊆ Gn,p) pe

F

exp −O µ1H/r log(1/p) .

Here we shall improve the log(1/p) ≍ log n in the exponent to log(np) by enforcing F somewhere in Gn,p. To this end, much in the spirit of a sequential embedding idea from [3], we will below use a two-round exposure

of the edges of Gn,p to ﬁrst ﬁnd a ‘random’ copy of Cℓ, which we then extend to a copy of F = Cℓ+z. We believe that, for r 2 and ε = Θ(1), the resulting rate of decay (10) is best possible when np → ∞ slowly.

Proof of Lemma 3. Set p2 := p/2, and pick p1 ∈ [p/2,p] such that (1 − p1)(1 − p2) = 1 − p. We expose the edges in two rounds: for i ∈ [2] we insert each of the n2 possible edges into Ei independently with probability pi; their union E1 ∪ E2 then gives Gn,p. To establish the lower bound (10), the strategy is to (i) ﬁrst use the E1–edges to ﬁnd one copy G′ of G := Cℓ, and (ii) then use the E2–edges to extend G′ to at least zr (1 + ε)µH copies of H, by enforcing that (in E2) one vertex of G′ has z neighbours outside of V (G′), where

z := r (1 + ε)µH 1/r ≍ (np)1+ℓ/r = o(n).

Turning to the details, for step (i) let XG∗ be the number of copies of G = Cℓ in E1. Since mG = 1 and p1 p/2 ≫ n−1, it is well-known (see, e.g., [17, Theorem 3.4]) that

P(XG∗ 1) = 1 − o(1). (11)

For step (ii), we henceforth condition on the edge-set E1, and assume that XG∗ 1; we also ﬁx a copy G′ of Cℓ in E1, and one vertex v ∈ V (G′). Deﬁning Z as the number of vertices in [n]\V (G′) that are neighbours of v in E2, note that Z = z implies XH Zr (Z/r)r (1 + ε)µH. Hence

n − ℓ z

z

np 4z

e−np (np)−O(z). (12)

(p2)z(1 − p2)n−ℓ−z

P(XH (1 + ε)µH | E1) P(Z = z | E1) =

![image 3](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile3.png>)

It follows that P(XH (1+ε)µH | XG∗ 1) (np)−O(z), which together with (11) implies inequality (10).

![image 4](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile4.png>)

![image 5](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile5.png>)

![image 6](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile6.png>)

![image 7](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile7.png>)

It is easy to check that the exponent of (10) is of order [(1 + ε)µH]1/r log (1 + ε)1/ℓnp . In Section 3 we will give a variant of the above argument which not only gives a better dependence on ε (when ε → 0), but also applies to a signiﬁcantly larger family of graphs H. We are now ready to prove Theorem 1 and Remark 2.

Proof of Theorem 1. Deﬁne H := {Cℓ+r : ℓ 3,r 2}. We henceforth ﬁx H = Cℓ+r ∈ H. Since every subgraph of H with fewer than ℓ vertices is acyclic, for 1 ≪ np ≪ n1/(ℓ−1) we have

µG ≍ min min

ΦH = min

G⊆H:eG 1

2 k ℓ−1

nkpk−1 , min

ℓ k ℓ+r

nkpk ≍ (np)ℓ ≫ 1. (13)

. Since α∗G vG ℓ + r holds by deﬁnition (cf. Footnote 2 on page 2 or [18, Appendix A]), using (13) it follows that

n for p n−1/∆

Turning to the parameter MH deﬁned in (4), note that n2p∆

H

H

MH log(1/p) = Ω min ΦH1/(ℓ+r), n · log(1/p) ≫ log n. (14) Using ℓ 3 and r 2, it now is routine to check that there is a constant cH > 0 such that

µ1H/r log(np) ≍ (np)1+ℓ/r log(np) ≪ min (np)ℓ, log n (15) for 1 ≪ np ≪ (log n)c

, which in view of (13)–(14), Lemma 3 and mH = 1 implies inequality (5).

![image 8](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile8.png>)

![image 9](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile9.png>)

![image 10](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile10.png>)

H

![image 11](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile11.png>)

Proof of Remark 2. Note that the above proof shows µ1H/r log(np) ≪ ΦH for 1 ≪ np ≪ n1/(ℓ−1), so Lemma 3 implies (6) for n−1/m

H+1/ℓ, say (recall that mH = 1 and r 2). In the remaining range of p then [18, Remark 8.3] already states that inequality (6) holds (even for n−1/m

≪ p ≪ n−1/m

H

log n ≪ p ≪ 1).

![image 12](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile12.png>)

![image 13](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile13.png>)

![image 14](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile14.png>)

H

![image 15](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile15.png>)

# 3 Extensions and generalizations

In this section we generalize the lower bound construction from Section 2. First, in Section 3.1 we show that many graphs H are not only counterexamples to Conjecture 1, but also fail to have subgaussian upper tails in some range. Next, in Section 3.2 we state a new lower bound for the upper tail, which complements the two clustered/disjoint mechanism based lower bounds from Section 1.2 used in Conjecture 1. We believe that our new lower bounds will not only serve as a testbed for future reﬁnements of the upper tail conjecture (cf. Section 4), but also stimulate the development of new upper bounds (here the importance of having non-trivial lower bounds was already highlighted by Vu [33, Section 4.8] more than 15 years ago).

To state our results, we now introduce some terminology on the structure of the graph H. We say that a subgraph G ⊆ H is primal (for H) if eG/vG = mH. Clearly all primal subgraphs are induced, and thus we can treat them as a family LH of subsets of V (H); see Claim 7 below for further properties. We say that G2 covers a primal G1 if G1 G2 and there is no further primal F with G1 F G2.

- 3.1 Further counterexamples and a general lower bound construction


The ﬁrst inequality (16) of the following result generalizes Theorem 1, by showing that many graphs H violate Conjecture 1. The second inequality (17) conceptually generalizes Remark 2, by showing that the upper tail of these graphs is also not of a subgaussian type, no matter how close p = p(n) is to the appearance threshold n−1/m

(even if we allow ε → 0 reasonably slowly; for H = C3+3 this was already shown in [19, Example 6.14]). The assumption λσH t = O(µH) below means that we are considering large deviations, i.e., deviations that are of higher order than the standard deviation σH = √VarXH.

H

![image 16](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile16.png>)

Theorem 4. Suppose that there is G ∈ LH and distinct J1,...,Jr ∈ LH covering G, such that K := J1 ∪ ··· ∪ Jr satisﬁes vK/r < minF∈L

vF. Then there are constants cH,βH > 0 such that the following holds. For ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with 1 ≪ npm

H

≪ (log n)c

we have

H

H

− log P (XH (1 + ε)EXH) = o min ΦH, MH log(1/p) . (16) Furthermore, there is λ = λ(n,p,H) ≫ 1 with λσH ≪ µH such that, whenever 1 ≪ npm

≪ nβ

and λσH t = O(µH) holds, we have

H

H

− log P (XH EXH + t) = o t2/σH2 . (17)

x5

- x6

- x7

- x8


- x9

- x10


- x1

- x2 x3


x4

G

K

H

- Figure 2: Example of a graph with r = 3, G = H[{x1,...,x5}]), Ji = H[V (G)∪{x5+i}]), and K = J1∪J2∪J3,


= eK/vK = 2 and eH/vH = 19/10 < 2. Theorem 4 shows that this graph is another counterexample to the DeMarco–Kahn upper tail conjecture (and also fails to have subgaussian upper tails in some range).

/vJ

where m(H) = eG/vG = eJ

i

i

Before giving the proof, we ﬁrst use Theorem 4 to argue that counterexamples to Conjecture 1 are abundant, by describing an abstract way of generating them. Suppose that we have a balanced graph J and a primal subgraph G with the property that J covers G (using as illustration Figure 2, consider G ∼= K5 and construct J by connecting two vertices of G to a common outside neighbour). Then we construct K by ‘gluing’ r distinct copies J1,...,Jr of J in a consistent way3 onto G = i∈[r] Jr (see Figure 2 for an example with r = 3). Let P be a primal of J with the minimum number of vertices (in Figure 2 we have P = G). The resulting graph K is easily seen4 to (i) be balanced with density mJ, and (ii) have no primal with fewer vertices than P. If vJ − vG < vP holds, then vK/r = vJ − vG + vG/r < vP for suﬃciently large r, in which case Theorem 4 implies that H := K is a counterexample to Conjecture 1 (in fact, this is true for any graph H ⊇ K for which P remains a vertex-minimal primal, as in Figure 2).

We shall prove Theorem 4 as a corollary of the following more general result, which qualitatively extends Lemma 3 to any graph H that is not strictly balanced (and also allows for ε → 0). Here we are again considering large deviations, since by (9) the assumption ε2ΦH ≫ 1 is equivalent to εEXH ≫

√VarXH.

![image 17](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile17.png>)

Lemma 5. For any graph H with eH 1 there is a constant βH > 0 such that the following holds for all ε = ε(n) > 0 and p = p(n) ∈ [0,1] with ε2ΦH ≫ 1, ε = O(1), and 1 ≪ npm

nβ

. If G ∈ LH and distinct J1,...,Jr ∈ LH cover G, then we have, writing K := J1 ∪ ··· ∪ Jr,

H

H

P (XH (1 + ε)EXH) exp −O (εµK)1/r log npm

H

, (18)

where the implicit constant in (18) may depend on H. Remark 6. The proof shows that for ε = Θ(1) the condition ε2ΦH ≫ 1 is redundant (as in Lemma 3, where mH = 1), and that ΦH ≍ (npm

)min

F∈LH vF holds for 1 ≪ npm

nβ

(cf. inequalities (36)–(38)).

H

H

H

Reﬁning the proof strategy of Lemma 3, inspired by [32, 18, 22, 35] the idea is to ﬁrst enforce y = Θ(εµK) copies of K via some some special F ⊆ Gn,p, which we again ﬁnd via two exposure rounds. Then we simultaneously (a) extend these y copies of K to 2εµH copies of H, and (b) also ﬁnd additional (1 − ε)µH ‘random’ copies of H. The routine proof of the following auxiliary claim is deferred to Appendix B.

![image 18](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile18.png>)

- 3To make the gluing precise, writing V (G) = {u1, . . . , uvG} and V (J)\V (G) = {w1, . . . , wvJ−vG}, the vertex-set of K consists of V (G) and r new vertices {wj,1, . . . , wj,r} for each wj ∈ V (J) \ V (G). The edge-set of K consists of E(G) and {ui, wj,k} : k ∈ [r] for every {ui, wj} ∈ E(J) \ E(G) as well {wi,k, wj,k} : k ∈ [r] for every {wi, wj} ∈ E(J) \ E(G).
- 4For a formal proof of claims (i)–(ii) note that, for any Q ⊆ K with vQ 1, using mJi = mJ = mG = eG/vG we have


eQ = eQ∩G + i∈[r] eG∪(Q∩Ji) − eG mG vQ∩G + i∈[r] vG∪(Q∩Ji) − vG = mJvQ, which holds with equality for Q = K and thus establishes (i). For any primal Q ⊆ K the above inequality must also hold with equality, and in view of (Q ∩ Ji) ∩ G = Q ∩ G it follows that eQ∩Ji = eG∪(Q∩Ji) + eQ∩G − eG = mJvQ∩Ji for all i ∈ [r]. Hence any Q ∩ Ji = ∅ (at least one such subgraph must exist) is a primal of Ji ∼= J, so vQ vQ∩Ji vP establishes (ii).

Claim 7. The following holds:

- (i) For distinct G1,G2 ∈ LH we have G1 ∪ G2 ∈ LH.
- (ii) If G ∈ LH and J ∈ LH covers G, then the graph J \ G := J[V (J) \ V (G)] is connected.
- (iii) If G ∈ LH and distinct J1,...,Jr ∈ LH cover G, then the Ji \ G are pairwise vertex-disjoint.


Proof-Sketch of Lemma 5. Deferring the choices of the constants CH 1 cH > 0, let

z := CHεµK 1/r , (19) δ := cH min{ε,1}. (20)

Similarly as in the proof of Lemma 3, we expose the edges of Gn,p in three rounds: for i ∈ [3] we insert each of the n2 possible edges into Ei independently with probability pi, where

1 − p (1 − p1)(1 − p2)

p1 := p2 := δp and p3 := 1 −

= (1 − O(δ)) p. (21)

![image 19](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile19.png>)

To establish the lower bound (18), the strategy is to (i) ﬁrst use the E1–edges to ﬁnd one copy G′ of G. Next, we (ii) partition the remaining vertex-set [n]\V (G′) into r sets V1,...,Vr of approximately equal sizes, and use the E2–edges to simultaneously extend G′ to z copies of each Ji which (a) embed V (Ji \ G) into Vi, and (b) are pairwise vertex-disjoint outside of V (G′). This clearly enforces y := zr copies of K = J1 ∪···∪Jr extending G′ (by Claim 7(iii) all subgraphs Ji \ G are pairwise vertex-disjoint). Finally, we (iii) use the E3–edges to show that we can simultaneously (a) extend y = Θ(CHεµK) of the aforementioned special copies of K via the E3–edges to at least 2εµH copies of H, and (b) also ﬁnd at least (1 − ε)µH additional copies of H in E3 itself, so that we overall obtain XH 2εµH + (1 − ε)µH (1 + ε)µH copies of H.

While some care is needed, the technical details of the outlined steps are mostly elementary, and thus deferred to Appendix B. Here we just mention that, analogously to Lemma 3, the probability of the ‘disjoint construction’ from step (ii) again gives the main contribution to our lower bound. In particular, by a more involved variant of the ‘enforcing z neighbours’ argument from (12), the aforementioned probability of step (ii) that G′ has z ‘non-overlapping extensions’ to each Ji will turn out to be (noting that i∈[r] nv

Ji−vGpe

Ji−eG ≍ i∈[r](µJ

/µG) ≍ µK/µG by Claim 7(iii), and that zr ≍ εµK) roughly of form

i

z Θ i∈[r] δe

Ji−eG εµG

z

|Vi| vJi−vG

Θ nv

Ji−vG(δp)e

Ji−eG

p2(e

Ji−eG)z

. (22)

![image 20](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile20.png>)

![image 21](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile21.png>)

z

z

i∈[r]

i∈[r]

)v

Using δ ≍ ε, ε2 ≫ 1/ΦH 1/µG and µG ≍ (npm

≫ 1 (by primality of G), this in turn is at least Θ ε i(eJi−eG)−1

G

H

z

z 1 µΘ(1)G

H −O(z), (23)

npm

![image 22](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile22.png>)

![image 23](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile23.png>)

µG

making the right-hand side of inequality (18) plausible (see Appendix B for the full details). Proof of Theorem 4. Let ω := npm

![image 24](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile24.png>)

![image 25](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile25.png>)

![image 26](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile26.png>)

![image 27](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile27.png>)

vF. Note that ΦH ≍ ωv

≫ 1 by Remark 6. Since the graph K = J1 ∪ ··· ∪ Jr is primal by Claim 7(i), it follows easily that µK ≍ ωv

and v0 := minF∈L

0

H

H

(see, e.g., (36)). We are now ready to prove (16). Since ΦH = O((log n)v

K

0cH) holds by assumption, we have ΦH ≪ log n ≪ MH log(1/p) for cH > 0 small enough. Since vK/r < v0 holds by assumption, we also have µ1K/r log(npm

) ≍ ωv

H

≍ ΦH, so that inequality (16) follows from Lemma 5 (as ε2ΦH ≍ ΦH ≫ 1).

K/r log ω ≪ ωv

0

We next turn to (17). Pick positive c ∈ v0/2− (rv0 − vK)/(2r − 1),v0/2 , and deﬁne λ := ωc. Using the variance estimate (9) we infer λσH/µH ≍ λ/Φ1H/2 ≍ ωc−v

0/2 ≪ 1 and thus λσH ≪ µH. Deﬁning ε := t/µH = O(1), using (9) we also infer ε2ΦH ≍ t2/σH2 λ2 ≫ 1, so Lemma 5 applies. Combining t2/σH2 ≍ ε2ΦH and ε λσH/µH ≍ ωc−v

and µK ≍ ωv

0/2 with ΦH ≍ ωv

, it follows by choice of c that, say,

K

0

t2/σH2 r ≍ ε · ε2r−1 ΦH r ε · Ω ω(c−v

(log ω)r ≍ εµK(log ω)r.

0/2)(2r−1)+rv0 ≫ ε · ωv

K

This readily implies (εµK)1/r log ω ≪ t2/σH2 , which in view of (18) establishes inequality (17).

![image 28](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile28.png>)

![image 29](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile29.png>)

![image 30](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile30.png>)

![image 31](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile31.png>)

3

- 4

- 5


6 7

2 1

- Figure 3: The snail graph H, which is balanced and satisﬁes mH = 1. Example 9 demonstrates that no graph in the Bollob´s–Wierman grading decomposition H[123] ⊂ H[12347] ⊂ H minimizes ζH(G) in (24).


- 3.2 Optimizing the lower bound for the upper tail


In this subsection we optimize the lower bound (18) for the upper tail over all possible choices of G and K = J1 ∪···∪Jr, restricting to the important case where ε > 0 is ﬁxed (as in Problem 1); see Lemma 8 below. To state our result, given G ∈ LH, let J1,...,Js(G) be all primals of H which cover G, ordered by the increasing number of vertices (how the ties are broken is irrelevant for our purposes). Then, for graphs H which are not strictly balanced (which implies that there is G ∈ LH with s(G) 1), we deﬁne

vG + ri=1(vJ

i − vG) r

ζH(G) := min

ζH(G) : s(G) 1 . (24)

and ζH := min

![image 32](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile32.png>)

G∈LH

r∈[s(G)]

Lemma 8. For every graph H that is not strictly balanced there is a constant βH > 0 such that the following holds. For ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with 1 ≪ npm

nβ

we have

H

H

)ζ

P (XH (1 + ε)EXH) exp −O (npm

H

H

log(npm

H

) , (25)

where the implicit constant in (25) may depend on ε and H. Proof. Fix arbitrary G ∈ LH with s(G) 1. Combining Lemma 5 with µ1K/r ≍ (npm

K/r ≫ 1 (cf. the proof of Theorem 4), it suﬃces to show that the minimum of vK

)v

H

/|S| over all S ⊆ [s(G)] with S = ∅ equals ζH(G), where KS := ∪i∈SJi. By Claim 7(iii) the graphs Ji share no vertices except for those in V (G), so

S

i − vG). (26)

= vG +

vK

(vJ

S

i∈S

, a moment’s thought reveals that the minimum is always attained by one of the sets S ∈ {[1],[2],...,[s(G)]}, which establishes minS vK

... vJ

Recalling vJ

1

s(G)

/|S| = ζH(G) and thus completes the proof.

![image 33](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile33.png>)

![image 34](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile34.png>)

![image 35](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile35.png>)

S

![image 36](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile36.png>)

It seems diﬃcult to give a simple combinatorial description of the G ∈ LH which minimize ζH(G) in (24). For balanced graphs H it is natural to ﬁrst focus on the so-called ‘grading decomposition’ {G0,...,Gs} ⊆ LH of Bollob´s and Wierman [4], which determines the limit distribution of XH at the appearance threshold (i.e., when p ∼ cn−1/m

for some c ∈ (0,∞)). Turning to the inductive deﬁnition of their decomposition, let G0 be the union of minimal primal subgraphs of H. Then, given Gi = H, let Gi+1 be the union of all primal subgraphs covering Gi. For balanced graphs H the resulting grading G0 ⊂ ··· ⊂ Gs always terminates with Gs = H (and Claim 7(i) implies Gj ∈ LH). In [4] the distribution of XH at the threshold is then determined inductively: ﬁrst counting G0-subgraphs, then G1-subgraphs that contain the G0 subgraphs, etc, continuing until all H-subgraphs are counted. Moving a tiny bit above the appearance threshold (as in Lemma 8), it thus sounds plausible that the exponential decay of P (XH (1 + ε)EXH) could potentially be determined by one of the ‘transitions’ from Gi to Gi+1, which in turn suggests that the minimum in ζH might perhaps be attained by some Gj. The following example shows that this speculation is false.

H

Example 9. Consider the graph H in Figure 3 with vH = 7. Its primals (as vertex sets) are 123, 1234, 1237, 12347, 12345, 12346, 123456, 123457, 123467, and 1234567. Straightforward case checking reveals that ζH is attained by 1234, which is covered by the three primals 12345, 12346, and 12347, so that ζH(H[1234]) = min{5/1,6/2,7/3} = 7/3. However, the Bollob´s-Wierman grading decomposition is G0 := H[123] ⊂ G1 := H[12347] ⊂ G2 := H, and both ζH(G0) = 5/2 and ζH(G1) = 7/2 are suboptimal.

2

1

- 3

- 4


... r − 1 times

6

5

= 4/3. Theorem 10 illustrates that the upper tail behaviour of Hr is extremely complicated for r 7 (see also Appendix A).

- Figure 4: The graph Hr, which is balanced and satisﬁes mH


r

# 4 Concluding remarks

In this note we showed that the DeMarco–Kahn upper tail conjecture is false. Nevertheless we believe that its prediction is true when H is strictly balanced or p = p(n) is suﬃciently above the appearance threshold.

- Conjecture 2. Conjecture 1 is true for any strictly balanced graph H. Furthermore, for any ﬁxed γ > 0,


Conjecture 1 is true under the additional assumption p n−1/m

H+γ.

We leave it as an intriguing open problem to formulate an upper tail conjecture for graphs which are not strictly balanced (this would already be interesting for balanced graphs). Combining the new ‘locally-disjoint mechanism’ based lower bound (25) from Lemma 8 with the previously known clustered/disjoint mechanism based lower bounds (7)–(8) from Section 1.2, it is tempting to speculate that we might perhaps have

)ζ

− log P (XH (1 + ε)µH) = Θ min ΦH, MH log(1/p), (npm

H

H

log(npm

H

) , (27)

which we believe to be correct for many graphs (e.g, for the graphs Cℓ+r from Section 2). However, the following result shows that the natural guess (27) is false for the balanced graphs Hr illustrated in Figure 4, indicating that for subgraph counts a general upper tail conjecture is most likely quite complicated.

Theorem 10. Let H := {Hr : r 7}. For any H ∈ H there are constants 1 > dH > cH > 0 such that the following holds. For ﬁxed ε > 0 and any p = p(n) ∈ [0,1] with (log n)c

≪ (log n)d

≪ npm

we have

H

H

H

)ζ

− log P (XH (1 + ε)EXH) = o min ΦH, MH log(1/p), (npm

H

H

log(npm

H

) . (28)

The proof of inequality (28) is based on the observation that diﬀerent kinds of extensions (for Hr from Figure 4 the dangling triangle and the rooted path) can have diﬀerent ranges of p = p(n) where the disjoint mechanism beats the clustered one, which means that in some transitional range of p = p(n) a mixture of both mechanisms can potentially give better bounds (which turns out to be the case for Hr). More precisely, adapting the framework of Lemma 5 for H = Hr with G := H[123456] and K := H, after planting one copy of G here the idea is to (a) enforce z vertex-disjoint triangles which are each connected to vertex 1 of G, and (b) enforce at least z∗ clustered copies of 5-vertex paths with endvertices 3,4 of G (by planting a complete bipartite graph which connects a ﬁxed vertex-set U of size 2√z∗ with the vertex-set {w,3,4}, where the extra vertex w  ∈ V (G)∪U is also ﬁxed). Analyzing these two mechanisms, it turns out that this way we obtain at least r− z1 ·z∗ copies of Hr with probability at least (npm

![image 37](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile37.png>)

√z∗), which for suitable z ≪ µ1H/r ≪ z∗ and p = p(n) eventually gives inequality (28); see Appendix A for the details.

![image 38](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile38.png>)

)−O(z) ·pΘ(

H

Of course, one could augment (27) by the above-discussed new mix of the disjoint/clustered mechanisms (by adapting Lemmas 5 and 8), but we are not sure if the resulting bound would be optimal (in general).

Finally, it would also be interesting to explore if Stein’s method, large deviation theory (possibly after altering the variational problem from [7, 6, 10]), or some other probabilistic approach could yield an educated guess for the solution to the upper tail problem (Problem 1) close to the appearance threshold n−1/m

. Acknowledgements. We thank the referees for helpful suggestions.

H

# References

- [1] R. Adamczak and P. Wolﬀ. Concentration inequalities for non-Lipschitz functions with bounded derivatives of higher order. Probab. Theory Related Fields 162 (2015), 531–586.
- [2] B. Bhattacharya, S. Ganguly, E. Lubetzky, and Y. Zhao. Upper tails and independence polynomials in random graphs. Adv. Math. 319 (2017), 313–347.
- [3] B. Bollob´s. Threshold functions for small subgraphs. Math. Proc. Cambridge Philos. Soc. 90 (1981), 197–206.
- [4] B. Bollob´s and J.C. Wierman. Subgraph counts and containment probabilities of balanced and unbalanced subgraphs in a large random graph. In Graph theory and its applications: East and West (Jinan, 1986), Annals of the New York Academy Vol. 141. pp. 763–70, New York Acad. Sci., New York (1989).
- [5] S. Chatterjee. The missing log in large deviations for triangle counts. Random Struct. Alg. 40 (2012), 437–451.
- [6] S. Chatterjee and A. Dembo. Nonlinear large deviations. Adv. Math. 299 (2016), 396–450.
- [7] S. Chatterjee and S.R.S. Varadhan. The large deviation principle for the Erd˝s-Re´nyi random graph. European J. Combin. 32 (2011), 1000–1017.
- [8] B. DeMarco and J. Kahn. Upper tails for triangles. Random Struct. Alg. 40 (2012), 452–459.
- [9] B. DeMarco and J. Kahn. Tight upper tail bounds for cliques. Random Struct. Alg. 41 (2012), 469–487.
- [10] R. Eldan. Gaussian-width gradient complexity, reverse log-Sobolev inequalities and nonlinear large deviations. Geom. Funct. Anal. 28 (2018) 1548–1596.
- [11] P. Erd˝s and A. Re´nyi. On the evolution of random graphs. Magyar Tud. Akad. Mat. Kutat´o Int. K¨ozl 5 (1960), 17–61.
- [12] A. Frieze and M. Karon´ski. Introduction to random graphs. Cambridge University Press, Cambridge (2016).
- [13] T.E. Harris. A lower bound for the critical probability in a certain percolation process. Math. Proc. Cambridge Philos. Soc. 56 (1960), 13–20.
- [14] S. Janson. Poisson convergence and Poisson processes with applications to random graphs. Stochastic Process. Appl. 26 (1987), 1–30.
- [15] S. Janson. Poisson approximation for large deviations. Random Struct. Alg. 1 (1990), 221–229.
- [16] S. Janson, T.  Luczak, and A. Rucin´ski. An exponential bound for the probability of nonexistence of a speciﬁed subgraph in a random graph. In Random graphs ’87 (Poznan´, 1987), pp. 73–87, Wiley, Chichester (1990).
- [17] S. Janson, T.  Luczak, and A. Rucin´ski. Random graphs. Wiley-Interscience Series in Discrete Mathematics and Optimization. Wiley-Interscience, New York (2000).
- [18] S. Janson, K. Oleszkiewicz, and A. Rucin´ski. Upper tails for subgraph counts in random graphs. Israel J. Math. 142 (2004), 61–92.
- [19] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Preprint (2000). http://www2.math.uu.se/~svante/papers/sj135_ppt.pdf
- [20] S. Janson and A. Rucin´ski. The infamous upper tail. Random Struct. Alg. 20 (2002), 317–342.
- [21] S. Janson and A. Rucin´ski. The deletion method for upper tail estimates. Combinatorica 24 (2004), 615–640.
- [22] S. Janson and L. Warnke. The lower tail: Poisson approximation revisited. Random Struct. Alg. 48 (2016), 219–246.
- [23] E. Lubetzky and Y. Zhao. On the variational problem for upper tails in sparse random graphs. Random Struct. Alg. 50 (2017), 420–436.
- [24] O. Riordan and L. Warnke. The Janson inequalities for general up-sets. Random Struct. Alg. 46 (2015), 391–395.
- [25] V. Ro¨dl and A. Rucin´ski. Random graphs with monochromatic triangles in every edge coloring. Random Struct. Alg. 5 (1994), 253–270.
- [26] A. Rucin´ski. Small subgraphs of random graphs—a survey. In Random graphs ’87 (Poznan´, 1987), pp. 283–303, Wiley, Chichester (1990).
- [27] M. Sileikis.ˇ Inequalities for Sums of Random Variables: a combinatorial perspective. PhD thesis, AMU Poznan´

(2012). Available from https://sites.google.com/site/matassileikis/

- [28] M. Sileikis.ˇ On the upper tail of counts of strictly balanced subgraphs. Electron. J. Combin. 19 (1) Paper 4

(2012), 14 pages.

- [29] M. Sileikisˇ and L. Warnke. Counting extensions revisited. Manuscript (2019).
- [30] M. Sileikisˇ and L. Warnke. Upper tail bounds for Stars. Preprint (2019). arXiv:1901.10637.
- [31] V.H. Vu. On the concentration of multivariate polynomials with small expectation. Random Struct. Alg. 16

(2000), 344–363.

- [32] V.H. Vu. A large deviation result on the number of small subgraphs of a random graph. Combin. Probab. Comput. 10 (2001), 79–94.
- [33] V.H. Vu. Concentration of non-Lipschitz functions and applications. Random Struct. Alg. 20 (2002), 262–316.
- [34] L. Warnke. On the missing log in upper tail estimates. J. Combin. Theory Ser. B, to appear. arXiv:1612.08561.
- [35] L. Warnke. Upper tails for arithmetic progressions in random subsets. Israel J. Math. 221 (2017), 317–365.


# A Appendix: Proof of Theorem 10

and γ := 1/r3. Deﬁne

Proof of Theorem 10. Fix H = Hr ∈ H, with vH = 3r + 6. Let ω := npm

H

2 vH/r − (r − 1)γ

1 vH/r − 2 + γ/2

cH :=

and dH :=

,

![image 39](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile39.png>)

![image 40](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile40.png>)

noting that cH < dH as γ < (4 − vH/r)/r = (1 − 6/r)/r. Since G has the smallest number of vertices among primals, we obtain ΦH ≍ ω6 by Remark 6. Using 1 ≪ ω no(1) and mH ∆H/2, it is not diﬃcult to verify that MH = minG⊆H:e

∗ G

G 1 µvG/α

F∈LH vF/α∗F holds (e.g., by combining (36)– (37) with 1/α∗F ∈ [1/vF,1]). Since every F ∈ LH is a union of G and some (possibly empty) subset of the Ji, using [18, Proposition A.4] it turns out that α∗F = vF/2, so MH ≍ ω2. It is routine to check that ζH = vH/r = 3+6/r. It follows that ΦH ≫ ωζ

G and thus MH ≍ ωmin

H/r−2 ≫ log ω, so the minimum in (28) satisﬁes

≍ (log n)/ωv

log ω and MH log(1/p)/ωζ

H

H

)ζ

min ΦH, MH log(1/p), (npm

H

log(npm

H

) = ωv

H/r log ω. (29)

H

We are now ready to establish (28) by adapting the proof of Lemma 3, exposing the edges of Gn,p via E1∪E2 in two independent rounds with edge-probabilities p2 := p/2 and p1 ∈ [p/2,p]. For the desired lower bound, the strategy is to (i) ﬁrst use the E1–edges to ﬁnd one copy G′ of G := H[123456], where the vertices vj of G′ correspond to vertices j of G (see Figure 4). Next we (ii) partition the vertex-set [n] \ V (G′) = V1 ∪ V2 into two sets with |Vi| ≈ n/2, and then use the E2–edges to simultaneously (a) create z vertex-disjoint triangles in V1, which are each connected to vertex v1 of G′, and (b) create z∗ ‘clustered’ copies of a 5vertex-path whose internal vertices are in V2 and whose endpoints are v3,v4 of G′. This together enforces at least r− z1 · z∗ > (1 + ε)µH copies of H = Hr extending G′ (see Figure 4), where

H/r−γ and z∗ := ((1 + ε)µH)1/rω(r−1)γ ≍ ωv

H/r+(r−1)γ.

z := r((1 + ε)µH)1/rω−γ ≍ ωv

Turning to the details, in step (i) we ﬁnd with probability 1 − o(1) at least one copy of G := H[123456] in E1, since mG = 4/3 = mH and p1 p/2 ≫ n−1/m

is above the appearance threshold. For step (ii), we henceforth condition on the edge-set E1 and ﬁx one copy G′ of G in E1. Mimicking the calculations leading to (43)–(45) in Appendix B, it turns out that the probability of step (ii).(a) is at least

H

z Θ(ω3−o(1)) ωvH/r−γ

z

Θ(n3p4ω−o(1)) z

|V1| − 3j 3

1 z! 0 j<z

vH/r), (30)

p42 · ω−o(z)

ω−o(ω

![image 41](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile41.png>)

![image 42](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile42.png>)

![image 43](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile43.png>)

where we used vH/r = 3+6/r. Turning to step (ii).(b), after ﬁxing a vertex-set U ⊆ V2 of size |U| = ⌈2√z∗⌉ and a vertex w ∈ V2 \ U, we deﬁne F as the complete bipartite graph between U and {v3,v4,w}. Note that the union of G′ and F contains at least |U2| z∗ diﬀerent 5-vertex-paths with endpoints v3,v4 and internal vertices from V2. Recalling p2 = n−1/m

![image 44](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile44.png>)

H+o(1), the probability of step (ii).(b) is thus at least

√z∗) ω−o(ω

vH/r), (31) where we used ωv

P (F ⊆ E2) = p23|U| n−Θ(

![image 45](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile45.png>)

H/r/√z∗ ≍ ω(v

H/r−(r−1)γ)/2 log n. Noting that the step (ii) events lower bounded by (30)–(31) are independent (as they depend on disjoint edge-sets), it follows that P (XH (1 + ε)EXH) ω−o(ω

![image 46](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile46.png>)

vH/r), which together with (29) implies inequality (28).

![image 47](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile47.png>)

![image 48](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile48.png>)

![image 49](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile49.png>)

![image 50](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile50.png>)

# B Appendix: Proof of Lemma 5 and Claim 7

1∩G2 it routinely follows that eG

1∩G2/vG

= mH eG

/vG

Proof of Claim 7. For property (i), using eG

i

i

2 − eG

+ eG

eG

1∪G2 vG

1∩G2 vG

1

mH, (32)

=

![image 51](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile51.png>)

![image 52](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile52.png>)

2 − vG

+ vG

1∩G2

1∪G2

1

which implies that G1 ∪ G2 ⊆ H is primal.

For property (iii), suppose that Ji \G and Jj \G with i = j are not vertex-disjoint. Clearly G Ji ∩Jj Ji. Since Jk covers G, this implies eJ

= mH, analogously to (32) we infer eJ

i∩Jj < mH. Since eJ

/vJ

i∩Jj/vJ

k

k

i∪Jj > mH, reaching the desired contradiction (since Ji ∪ Jj ⊆ H).

i∪Jj/vJ

For property (ii), suppose that J \G is not connected. Then we can partition V (J \G) = V (J)\V (G) into two non-empty vertex-sets Vj such that there are no edges between V1 and V2 in J. Since the graphs Fj := J[V (G) ∪ Vj] are not primal (as G Fj J), we have eF

< mH = eG/vG. It follows that

/vF

j

j

2 − eG vF

eJ vJ

+ eF

eF

1

< mH,

=

![image 53](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile53.png>)

![image 54](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile54.png>)

2 − vG

+ vF

1

reaching the desired contradiction (since J ⊆ H is primal).

![image 55](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile55.png>)

![image 56](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile56.png>)

![image 57](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile57.png>)

![image 58](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile58.png>)

Proof of Lemma 5. We keep the setup from the sketch in Section 3.1: in particular, we shall expose the edges of Gn,p via E1∪E2∪E3 in three independent rounds with edge-probabilities p1 = p2 = δp and p3 = (1−O(δ))p, where δ = cH min{ε,1} and cH 1. Adding an extra initial reduction step, we claim that it suﬃces to prove Lemma 5 for graphs K = J1 ∪ ··· ∪ Jr which satisfy, for all i ∈ [r],

/µG (εµK)1/r. (33)

µJ

i

To see that this implies Lemma 5 for arbitrary K = J1∪···∪Jr, we use induction on the number of J1,...,Jr (formally allowing the implicit constant in inequality (18) to depend on 1 r vH). The base case r = 1 is immediate, since (33) always holds due to (εµK)1/r = εµG · (µJ

/µG) and εµG εΦH ≫ ε−1 =

1

Ω(1). For r 2 it suﬃces to consider the case where (33) fails for some i ∈ [r]. Set K′ := j =i Jj. Applying induction (with K replaced by K′, and thus r replaced by r − 1), the lower bound (18) holds

with (εµK′)1/(r−1) log(npm

) in the exponent. It thus remains to check that

H

(εµK′)1/(r−1) = O (εµK)1/r . (34) Using Claim 7(iii) we obtain µK ≍ µK′·µJ

/µG > (εµK)1/r holds) we infer εµK′ ≍ εµK · µG/µJ

/µG. Since we assumed that (33) fails (i.e., that µJ

i

i

= O((εµK)1−1/r) and thus establish (34), completing the proof of the claimed reduction.

i

To facilitate our three-step proof strategy, we henceforth assume that (33) holds for all i ∈ [r]. Furthermore, we ﬁx an ordering u1,...,uv

of the vertices of H such that the ﬁrst vG vertices are vertices of G, the following vJ

H

1 −vG vertices are vertices of J1\G, followed by the vertices of J2\G, and so on up to Jr \G (this is possible since the subgraphs Ji \ G are pairwise vertex-disjoint, see Claim 7(iii)), while the ﬁnal vH − vK vertices are the remaining vertices of H \ K. We also introduce the shorthand notation

with 1 ≪ ω nβ

ω := npm

. (35) We assume βH < 1/vH, so that every primal subgraph F ⊆ H satisﬁes

H

H

H vF = ωv

F/vF vF = npm

FβH ≪ n. (36) Furthermore, for any non-primal subgraph F ⊆ H we have BF,H := mH − eF/vF > 0, so that, say,

nv

µF ≍ npe

F

H−eF/vF) vF ω · nB

F,H(1−βH)/mH vF ≫ n2v

2

2

HβH ω2v

· p−(m

µF ≍ npm

H (37) for βH > 0 small enough (the ad hoc 2vH2 -term is convenient later on). From (35)–(37) we easily deduce

H

ΦG ΦH ≫ 1. (38) Using ε2ΦH ≫ 1 and (36) we obtain

δ ≍ min{ε,1} ≫ (ΦH)−1/2 (µG)−1/2 = Ω(ω−v

G/2). (39)

Finally, recalling the deﬁnition (19) of z, note that ε2ΦH ≫ 1 and ε = O(1) imply zr ≍ εµK εΦH ≫ ε−1 = Ω(1) and zr = O(µK). Since K ⊆ H is primal (by Claim 7(i)), using (36) it follows that

1 ≪ z = O(ωv

K/r) ≪ n1/r. (40)

Turning to the technical details of step (i), let XG∗ be the number of copies of G in E1. We claim that P(XG∗ 1) ≫ ω−v

GeG. (41)

For the proof we use a version of the Paley–Zygmund inequality (see, e.g., [17, (3.3)–(3.4)]) and the standard estimate VarXG∗ /(EXG∗ )2 ≍ 1/ΦG(n,p1) (see, e.g., [17, Lemma 3.5]), so that p1 = δp and δ 1 imply

(EXG∗ )2 (EX∗

≍ min 1, ΦG(n,p1) min 1, δe

P(XG∗ 1)

ΦG .

G

![image 59](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile59.png>)

G)2 + VarX∗

G

Now inequality (41) follows, since δ ≫ ω−v

G/2 by (39) and ΦG ≫ 1 by (38).

For step (ii), we henceforth condition on the edge-set E1, and assume that XG∗ 1. We also ﬁx an ordered copy G′ of G in E1, i.e., a copy of G with E(G′) ⊆ E1 and an ordering u′1,...,u′v

of V (G′) that is consistent with the above-ﬁxed ordering u1,...,uv

G

of G (i.e., the injection uj  → u′j maps edges of E(G) into edges of E1). We partition [n] \ V (G′) into r vertex-sets V1,...,Vr of approximately equal sizes ni := |Vi| ≈ n/r. We say that an (eJ

G

i∪V (G′)

′)

i −eG)-element edge-set S ⊆ V

2 \ V(G

2 is an (G′,Ji)-edge-extension if there is an injection from V (Ji) to W(S) := V (G′)∪ f∈S f with uj  → u′j for j ∈ [vG] that maps every edge E(Ji)\E(G) to an edge in S (this deﬁnition makes sense since Ji \ G = Ji[V (Ji) \ V (G)] contains no isolated vertices, see Claim 7(ii)). Note that |W(S) \ V (G′)| = vJ

i − vG, and that S ∪ E(G′) corresponds to (the edge-set of) a copy of Ji which contains G′. Let ZG′,Ji be the number of (G′,Ji)-edge-extensions S ⊆ E2. Noting that the random variables ZG′,Ji,i ∈ [r] depend on disjoint sets of independent E2-edges, we infer

P(ZG′,Ji = z | E1). (42)

P(ZG′,Ji = z for all i ∈ [r] | E1) =

i∈[r]

Fix i ∈ [r]. We claim that

P(ZG′,Ji = z | E1) ω−O(z). (43) The following proof of (43) is fairly standard (similar to, e.g., [9, Proposition 9.1], [28, Theorem 1] or [35, Lemma 23]), and we shall omit the conditioning on E1 from our notation to avoid clutter. Let Si denote the set of all (G′,Ji)-edge-extensions S. Since S ⊆ V

i∪V (G′)

′)

2 \ V (G

2 and z ≪ n by (40), the number of

z-element collections C ⊆ Si of edge-extensions with pairwise disjoint vertex-sets W(S) \ V (G′) is at least 1 z! 0 j<z

z

vJi−vG z Θ(nv

Ji−vG) z

i − vG) vJ

ni − z(vJ

i − vG) vJ

ni − j(vJ

1 z!

. (44)

![image 60](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile60.png>)

![image 61](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile61.png>)

![image 62](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile62.png>)

![image 63](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile63.png>)

i − vG

i − vG

For any such collection C, for brevity we introduce the events

IC := {E2 contains all S ∈ C} and DC := {E2 contains no S ∈ Si \ C}. We trivially have P(IC) p(eJ

i−eG)z

2 (in fact, this holds with equality), and defer the proof of

P(DC | IC) ω−o(z). (45) Since there are at least (44) many such collections C, using disjointness of the events IC ∩ DC we obtain

Ji−vGpeJ

i−eG

z

nv

2 ω−o(1) z

P(IC)P(DC | IC)

.

P(ZG′,Ji = z)

![image 64](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile64.png>)

C

/µG ≍ ωv

Ji−vG. Since δ ≫ ω−v

K/r) by (40), we infer nv

G/2 by (39) and z = O(ωv

Note that (36) gives µJ

i

Ji−vGpeJ

i−eG 2

δe

Ji−eG

µJ

ω−Θ(1),

i

µG ·

z ≍

![image 65](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile65.png>)

![image 66](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile66.png>)

![image 67](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile67.png>)

z

and (recalling that we omitted the conditioning on E1 from our notation) inequality (43) follows. It remains to give the deferred proof of estimate (45). To this end observe that

{S  ⊆ E2} and IC = {EC ⊆ E2} with EC :=

S.

DC =

S∈C

S∈Si\C

Noting that the {S \ EC  ⊆ E2} are all decreasing events with respect to the independent E2-edge indicators, using Harris’ inequality [13] (a special case of the FKG-inequality) it follows that

P(DC | IC) = P

{S \ EC  ⊆ E2}

S∈Si\C

P(S \ EC  ⊆ E2) =

S∈Si\C

S∈Si\C

1 − p|S\2 EC| . (46)

Recall that each edge-extension S ∈ Si is isomorphic to E(Ji) \ E(G). Combining that Ji \ G = Ji[V (Ji) \ V (G)] is connected (see Claim 7(ii)) with the fact that all vertex-sets W(S) \ V (G′) with S ∈ C are pairwise disjoint, it follows that EC contains no further edge-extension S ∈ Si \ C. Therefore in every factor in (46) we have |S \ EC| 1 and thus S \ EC is isomorphic to E(Ji) \ E(F) for some G ⊆ F Ji. As p2 p ≪ 1, ni n and |C| = z, it follows that

F−vG µJ

p|S\2 EC| 2

F−vGnv

Ji−vF pe

i|C|)v

Ji−eF = O

zv

i

− logP(DC | IC) 2

(vJ

.

![image 68](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile68.png>)

µF

G⊆F Ji

G⊆F Ji

S∈Si\C

K/r) and (36) gives µG ≍ ωv

/µG ≪ z log ω, see (33) and (19). Furthermore, (40) gives z = O(ωv

Our initial reduction step ensures µJ

i

. As no G F Ji is primal (since Ji covers G), using (37) it follows that

G

FvK/r ωv

µJ

G

ωv

i

≪ z log ω,

− logP(DC | IC) = O

1 +

![image 69](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile69.png>)

![image 70](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile70.png>)

ω2vH2

µG

G F Ji

which completes the proof of (45) and thus inequality (43).

For the ﬁnal step (iii), we further (in addition to the conditioning on E1 from step (ii) above) condition on the edge-set E2, assuming that ZG′,Ji = z for all i ∈ [r]. Recalling that the subgraphs Ji \ G are vertexdisjoint (see Claim 7(iii)), note that if we pick any r copies of J1,...,Jr counted by ZG′,J1,...,ZG′,Jr (which are all vertex-disjoint outside of G′), then their union gives a copy of K = J1 ∪ ··· ∪ Jr (here it matters that the shared copy G′ is ordered). For each such copy of K we henceforth ﬁx one ordered copy K′ with vertex-ordering u′1,...,u′v

, say. Let K denote the collection of all such ordered K′ (each of which satisﬁes E(K′) ⊆ E1 ∪ E2), and deﬁne V (K) as the union of all their vertex-sets. Note that

,u′v

G+1,...,u′v

K

G

pe

|K| = zr ≍ CHεµK ≍ CHεnv

. (47)

K

K

Given K′ ∈ K, we say that a copy H′ of H in E1 ∪ E2 ∪ E3 is an (K′,H)-extension if H′ contains the ordered copy K′ with V (K′) = {u′1,...,u′v

}, satisﬁes V (H′)\ V (K′) ⊆ [n]\ V (K), and there is an injection from V (H) to V (H′) with uj  → u′j for j ∈ [vK] that maps every edge E(H)\E(K) to an edge in E3. Let XH′ denote the number of copies of H which are (K′,H)-extensions for some K′ ∈ K. Let XH′′ denote the number of copies of H with vertices in [n]\V (G′) and all edges in E3. As the sets of H-copies counted by XH′ and XH′′ are disjoint (the former contain G′, and the latter share no vertices with G′), we have XH XH′ + XH′′ . Noting that XH′ and XH′′ are both increasing functions of the independent E3-edge indicators, using Harris’ inequality it follows that

K

P(XH (1 + ε)µH | E1,E2) P(XH′ 2εµH | E1,E2) · P(XH′′ (1 − ε)µH | E1,E2). (48) To establish inequality (18) it thus suﬃces to prove

P(XH′ 2εµH | E1,E2) ≫ ω−v

, (49) P(XH′′ (1 − ε)µH | E1,E2) = 1 − o(1). (50)

K

Indeed, since we conditioned on E1 satisfying XG∗ 1 and E2 satisfying ZG′,Ji = z for all i ∈ [r], by combining (48)–(50) with estimates (41) and (42)–(43), then inequality (18) follows readily.

In the remaining proofs of (49)–(50) we shall again omit the conditioning (on E1,E2) from our notation. Turning to the crude estimate (49), we deﬁne YK′,H as the number of (K′,H)-extensions, so that

XH′ =

YK′,H.

K′∈K

Note that (47) and (40) imply the rough bound |V (K)| vK|K| ≍ zr ≪ n, so that |[n] \ V (K)| ≍ n, say. Combining (47) with p3 = (1 − O(δ))p ≍ p (which due to δ = cH min{ε,1} holds for cH > 0 suﬃciently small) and µH = Θ(nv

pe

), it follows for CH > 0 suﬃciently large that

H

H

H−vKpe

H−eK

EXH′ =

EYK′,H = |K| · Θ(nv

3 ) = CH · Θ(εµH) 4εµH.

K′∈K

Similarly, for all K1′,K2′ ∈ K we also have the routine upper bound

µK µF

H−vKpe

H−eK 3

H−vF pe

H−eF

2,H) nv

nv

i,H · O

EYK′

E(YK′

1,HYK′

3 =

![image 71](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile71.png>)

K⊆F⊆H

K⊆F⊆H

i∈[2]

.

Since K is primal (see Claim 7(i)), by combining µF ΦH with estimates (36) and (38) it follows that

E(XH′ )2 =

E(YK′

K1′,K2′∈K

2,H) (EXH′ )2 · O(µK/ΦH) ≪ (EXH′ )2 · ωv

.

1,HYK′

K

Using a version of the Paley–Zygmund inequality (see, e.g., [18, Lemma 3.2]) we infer

P(XH′ 2εµH) P(XH′ 12EXH′ )

![image 72](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile72.png>)

(EXH′ )2 E(X′

1 4 ·

H)2 ≫ ω−v

,

K

![image 73](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile73.png>)

![image 74](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile74.png>)

which (recalling that we omitted the conditioning on E1,E2 from our notation) implies inequality (49).

Turning to the ﬁnal estimate (50), for any F ⊆ H with eF 1 we deﬁne YF as the number of copies of F with vertex-set in [n]\V (G′) and edge-set in E3, so that XH′′ = YH. Note that YF has the same distribution as the number of copies of F in the (unconditional) binomial random graph Gn−v(G),p

. Furthermore, δ ≫ n−1 follows from (39) and (36), with room to spare (since G is primal). Recalling the deﬁnitions of p3 = (1−O(δ))p and δ = cH min{ε,1}, for cH > 0 suﬃciently small it thus is routine to see that

3

n−v(G) vF

eF

EYF µF

p3 p

= 1 − O(n−1) · 1 − O(δ) 1 − ε/2.

=

![image 75](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile75.png>)

![image 76](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile76.png>)

![image 77](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile77.png>)

n vF

Since also EYF ≍ µF, standard variance estimates for random graphs (see, e.g., (9) or [17, Lemma 3.5]) imply

(EYH)2 minF⊆H:e

(µH)2 ΦH

VarYH ≍

F 1 EYF ≍

.

![image 78](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile78.png>)

![image 79](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile79.png>)

Using XH′′ = YH, Chebychev’s inequality, and the assumption ε2ΦH ≫ 1 it follows that

VarYH (21εµH)2 ≍

1 ε2ΦH

P(XH′′ (1 − ε)µH) P(YH EYH − 21εµH)

= o(1),

![image 80](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile80.png>)

![image 81](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile81.png>)

![image 82](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile82.png>)

![image 83](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile83.png>)

which (as we omitted the conditioning on E1,E2) completes the proof of (49)–(50) and thus Lemma 5.

![image 84](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile84.png>)

![image 85](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile85.png>)

![image 86](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile86.png>)

![image 87](<2018-ileikis-counterexample-demarco-kahn-upper_images/imageFile87.png>)

