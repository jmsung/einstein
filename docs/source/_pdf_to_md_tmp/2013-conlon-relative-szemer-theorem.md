arXiv:1305.5440v2[math.NT]25Nov2014

A RELATIVE SZEMEREDI´ THEOREM

DAVID CONLON, JACOB FOX, AND YUFEI ZHAO

Abstract. The celebrated Green-Tao theorem states that there are arbitrarily long arithmetic progressions in the primes. One of the main ingredients in their proof is a relative Szemere´di theorem which says that any subset of a pseudorandom set of integers of positive relative density contains long arithmetic progressions.

In this paper, we give a simple proof of a strengthening of the relative Szemere´di theorem, showing that a much weaker pseudorandomness condition is suﬃcient. Our strengthened version can be applied to give the ﬁrst relative Szemere´di theorem for k-term arithmetic progressions in pseudorandom subsets of ZN of density N−ck.

The key component in our proof is an extension of the regularity method to sparse pseudorandom hypergraphs, which we believe to be interesting in its own right. From this we derive a relative extension of the hypergraph removal lemma. This is a strengthening of an earlier theorem used by Tao in his proof that the Gaussian primes contain arbitrarily shaped constellations and, by standard arguments, allows us to deduce the relative Szemere´di theorem.

1. Introduction

The Green-Tao theorem [24] states that the primes contain arbitrarily long arithmetic progressions. This result, along with their subsequent work [25] on determining the asymptotics for the number of prime k-tuples in arithmetic progression, constitutes one of the great breakthroughs in 21st century mathematics.

The proof of the Green-Tao theorem has two key steps. The ﬁrst step, which Green and Tao refer to as the “main new ingredient” of their proof, is to establish a relative Szemere´di theorem. Szemere´di’s theorem [45] states that any dense subset of the integers contains arbitrarily long arithmetic progressions. More formally, we have the following theorem, which is stated for ZN := Z/NZ but easily implies an equivalent statement in the set [N] := {1,2,... ,N}.

- Theorem 1.1 (Szemere´di’s theorem). For every natural number k ≥ 3 and every δ > 0, as long


- as N is suﬃciently large, any subset of ZN of density at least δ contains an arithmetic progression of length k.


A relative Szemere´di theorem is a similar statement where the ground set is no longer the set ZN but rather a sparse pseudorandom subset of ZN.

The second step in their proof is to show that the primes are a dense subset of a pseudorandom set of “almost primes”, suﬃciently pseudorandom that the relative Szemere´di theorem holds. Then, since the primes are a dense subset of this pseudorandom set, an application of the relative Szemere´di theorem implies that the primes contain arbitrarily long arithmetic progressions. This part of the proof use some ideas from the work of Goldston and Yıldırım [18] (and was subsequently simpliﬁed in [46]).

In the work of Green and Tao, the pseudorandomness conditions on the ground set are known as the linear forms condition and the correlation condition. Roughly speaking, both of these conditions say that, in terms of the number of solutions to certain linear systems of equations, the set behaves

![image 1](<2013-conlon-relative-szemer-theorem_images/imageFile1.png>)

The ﬁrst author was supported by a Royal Society University Research Fellowship, the second author was supported by a Simons Fellowship, NSF grant DMS-1069197, by an Alfred P. Sloan Fellowship, and by an MIT NEC Corporation Fund Award, and the third author was supported by a Microsoft Research PhD Fellowship.

1

like a random set of the same density. A natural question is whether these pseudorandomness conditions can be weakened. We address this question by giving a simple proof for a strengthening of the relative Szemere´di theorem, showing that a weak linear forms condition is suﬃcient for the theorem to hold.

This improvement has two aspects. We remove the correlation condition entirely but we also reduce the set of linear forms for which the correct count is needed. In particular, we remove those corresponding to the dual function condition, a pointwise boundedness condition stated explicitly by Tao [47] in his work on constellations in the Gaussian primes but also used implicitly in [24].

To state the main theorem, we will assume the deﬁnition of the k-linear forms condition. The formal deﬁnition, which may be found in Section 2 below, is stated for measures rather than sets but we will ignore this relatively minor distinction here, reserving a more complete discussion of our terminology for there.

- Theorem 1.2 (Relative Szemere´di theorem). For every natural number k ≥ 3 and every δ > 0, if


S ⊂ ZN satisﬁes the k-linear forms condition and N is suﬃciently large, then any subset of S of relative density at least δ contains an arithmetic progression of length k.

One of the immediate advantages of this theorem is that it simpliﬁes the proof of the Green-Tao theorem. In addition to giving a simple proof of the relative Szemere´di theorem, it removes the need for the number-theoretic estimates involved in establishing the correlation condition for the almost primes. A further advantage is that, by removing the correlation condition, the relative Szemere´di theorem now applies to pseudorandom subsets of ZN of density N−ck. With the correlation condition, one could only hope for such a theorem down to densities of the form N−o(1).

While the relative Szemere´di theorem is the main result of this paper, the main advance is an approach to regularity in sparse pseudorandom hypergraphs. This allows us to prove analogues of several well-known combinatorial theorems relative to sparse pseudorandom hypergraphs. In particular, we prove a sparse analogue of the hypergraph removal lemma. It is from this that we derive our relative Szemere´di theorem. As always, applying the regularity method has two steps, a regularity lemma and a counting lemma. We provide novel approaches to both.

A counting lemma for subgraphs of sparse pseudorandom graphs was already proved by the authors in [7]. In this paper, we simplify and streamline the approach taken there in order to prove a counting lemma for subgraphs of sparse pseudorandom hypergraphs. This result is the key technical step in our proof and, perhaps, the main contribution of this paper. Apart from the obvious diﬃculties in passing from graphs to hypergraphs, the crucial diﬀerence between this paper and [7] is in the type of pseudorandomness considered. For graphs, we have a long-established notion of pseudorandomness known as jumbledness. The greater part of [7] is then concerned with optimizing the jumbledness condition which is necessary for counting a particular graph H. For hypergraphs, we use an analogue of the linear forms condition ﬁrst considered by Tao [47]. It says that our hypergraph is pseudorandom enough for counting H within subgraphs if it contains asymptotically the correct count for the 2-blow-up of H and all its subgraphs.

We also use an alternative approach to regularity in sparse hypergraphs. While it would be natural to use a sparse hypergraph regularity lemma (and, following our approach in [7], this was how we initially proceeded), it suﬃces to use a weak sparse hypergraph regularity lemma which is an extension of the weak regularity lemma of Frieze and Kannan [16]. This is also closely related to the transference theorem used by Green and Tao (see, for example, [21] or [35, 52], where it is also referred to as the dense model theorem).

With both a regularity lemma and a counting lemma in place, it is then a straightforward matter to prove a relative extension of the famous hypergraph removal lemma [20, 34, 36, 37, 48]. Such a theorem was ﬁrst derived by Tao [47] in his work on constellations in the Gaussian primes but, like the Green-Tao relative Szemere´di theorem, needs both a correlation condition and a dual

function condition.1 Our approach removes these conditions. The ﬁnal step in the proof of the relative Szemere´di theorem is then a standard reduction used to derive Szemere´di’s theorem from the hypergraph removal lemma. The details of this reduction already appear in [47] but we include

- them here for completeness. In fact, the paper is self-contained apart from assuming the hypergraph removal lemma.


In Section 2, we state our results including the relative Szemere´di theorem and the removal, regularity, and counting lemmas. In Section 3, we deduce the relative multidimensional Szemere´di theorem from our relative hypergraph removal lemma. In Section 4, we prove the removal lemma from the regularity and counting lemmas. We will prove our weak sparse hypergraph regularity lemma in Section 5 and the associated counting lemma in Section 6. We conclude, in Section 7, with some remarks.

2. Definitions and results

Notation. Dependence on N. We consider functions ν = ν(N), where N (usually suppressed) is assumed to be some large integer. We write o(1) for a quantity that tends to zero as N → ∞. Expectation. We write E[f(x1,x2,... )|x1 ∈ A1,x2 ∈ A2,... ] for the expectation of f(x1,x2,... ) when each xi is chosen uniformly and independently at random from Ai.

- 2.1. A relative Szemere´di theorem. Here is an equivalent weighted version of Szemere´di’s theorem as formulated, for example, in [24, Prop. 2.3].


- Theorem 2.1 (Szemere´di’s theorem, weighted version). For every k ≥ 3 and δ > 0, there exists


c > 0 such that for N suﬃciently large and any nonnegative function f : ZN → [0,1] satisfying E[f] ≥ δ,

E[f(x)f(x + d)f(x + 2d)··· f(x + (k − 1)d)|x,d ∈ ZN] ≥ c. (1)

A relative Szemere´di theorem would instead ask for the nonnegative function f to be bounded above by a measure ν instead of the constant function f. For us, a measure will be any nonnegative function on ZN. We do not explicitly assume the additional condition that

E[ν(x)|x ∈ ZN] = 1 + o(1), but this property follows from the linear forms condition that we will now assume. Such measures are more general than subsets, as any subset S ⊆ ZN (e.g., in Theorem 1.2) can be thought of as a measure on ZN taking value N/|S| on S and 0 elsewhere. The dense case, as in Theorem 2.1, corresponds to taking ν = 1. Our notion of pseudorandomness for measures ν on ZN is now as follows.

Deﬁnition 2.2 (Linear forms condition). A nonnegative function ν = ν(N) : ZN → R≥0 is said to obey the k-linear forms condition if one has

E

k

ν

j=1 ω∈{0,1}[k]\{j}

k

(i − j)xi(ωi)

i=1

nj,ω

x(0)1 ,x(1)1 ,... ,x(0)k ,x(1)k ∈ ZN = 1 + o(1) (2)

for any choices of exponents nj,ω ∈ {0,1}. Example 2.3. For k = 3, condition (2) says that

E[ν(y + 2z)ν(y′ + 2z)ν(y + 2z′)ν(y′ + 2z′)ν(−x + z)ν(−x′ + z)ν(−x + z′)ν(−x′ + z′)

· ν(−2x − y)ν(−2x′ − y)ν(−2x − y′)ν(−2x′ − y′)|x,x′,y,y′,z,z′ ∈ ZN] = 1 + o(1) and similar conditions hold if one or more of the twelve ν factors in the expectation are erased.

![image 2](<2013-conlon-relative-szemer-theorem_images/imageFile2.png>)

1The problem of relative hypergraph removal was also recently considered by Towsner [51].

Our linear forms condition is much weaker that that used in Green and Tao [24]. In particular, Green and Tao need to assume that pointwise estimates such as

E[ν(a + x)ν(a + y)ν(a + x + y)|x,y ∈ ZN] = 1 + o(1)

hold uniformly over all a ∈ ZN. Such linear forms do not arise in our proof. Moreover, to prove their relative Szemere´di theorem, Green and Tao need to assume a further pseudorandomness condition, which they call the correlation condition. This condition also does not arise in our proofs. Indeed, we prove that a relative Szemere´di theorem holds given only the linear forms condition deﬁned above.

- Theorem 2.4 (Relative Szemere´di theorem). For every k ≥ 3 and δ > 0, there exists c > 0 such that if ν : ZN → R≥0 satisﬁes the k-linear forms condition, N is suﬃciently large, and f : ZN → R≥0 satisﬁes 0 ≤ f(x) ≤ ν(x) for all x ∈ ZN and E[f] ≥ δ, then


E[f(x)f(x + d)f(x + 2d)··· f(x + (k − 1)d)|x,d ∈ ZN] ≥ c. (3)

We note that both here and in Theorem 1.2, the phrase “N is suﬃciently large” indicates not only a dependency on δ and k as in the usual version of Szemere´di’s theorem but also a dependency on the o(1) term in the linear forms condition. We will make a similar assumption in many of the theorems stated below.

We prove Theorem 2.4 using a new relative hypergraph removal lemma.2 In the next subsection we set up the notation for hypergraphs and state the corresponding pseudorandomness hypothesis.

- 2.2. Hypergraphs. We borrow most of our notation and deﬁnitions from Tao [47, 48].


- Deﬁnition 2.5 (Hypergraphs). Let J be a ﬁnite set and r > 0. Deﬁne Jr = {e ⊆ J : |e| = r} to be the set of all r-element subsets of J. An r-uniform hypergraph on J is deﬁned to be any subset H ⊆ Jr .
- Deﬁnition 2.6 (Hypergraph system). A hypergraph system is a quadruple V = (J,(Vj)j∈J,r,H), where J is a ﬁnite set, (Vj)j∈J is a collection of ﬁnite non-empty sets indexed by J, r ≥ 1 is a

positive integer, and H ⊆ Jr is an r-uniform hypergraph. For any e ⊆ J, we set Ve := j∈e Vj. For any x = (xj)j∈J ∈ VJ and any subset J′ ⊆ J, we write xJ′ = (xj)j∈J′ ∈ VJ′ to mean the natural projection of x onto the coordinates J′. Finally, for any e ⊆ J, we write ∂e for the set {f e : |f| = |e| − 1}, the skeleton of e.

- Deﬁnition 2.7 (Weighted hypergraphs). Let V = (J,(Vj)j∈J,r,H) be a hypergraph system. A weighted hypergraph on V is a collection g = (ge)e∈H of functions ge: Ve → R≥0 indexed by H. We write 0 and 1 to denote the constant-valued weighted hypergraphs of uniform weight 0 and 1, respectively. Given two weighted hypergraphs g and ν on the same hypergraph system, we write g ≤ ν to mean that ge ≤ νe for all e, which in turn means that ge(xe) ≤ νe(xe) for all xe ∈ Ve.


The weighted hypergraph ν plays an analogous role to the ν in Theorem 2.4, with ν = 1 again corresponding to the dense case. We have an analogous linear forms condition for ν as a weighted hypergraph. We use the following indexing notation. For a ﬁnite set e and ω ∈ {0,1}e, we write

xe(ω) to mean the tuple (xj(ωj))j∈e. We also write x(0)e := (x(0)j )j∈e and similarly with x(1)e .

![image 3](<2013-conlon-relative-szemer-theorem_images/imageFile3.png>)

2Green and Tao [24] prove a transference result that allows them to apply the dense version of Szemere´di’s theorem

- as a black box. This allows them to show that the optimal c in (3) can be taken to be the same as the optimal c in (1). The proof in this paper goes through the hypergraph removal lemma and thus does not obtain the same c. Nevertheless, one can obtain our result with the same c by modifying the argument to an arithmetic setting, as done by the third author in a follow-up paper [53].


V1

H:

V2 V3

(a)

V1

V1

H-linear forms condition: & subgraphs, e.g.,

V2 V3

V2 V3

(b)

(c)

Figure 1. Linear forms conditions for H = K3. See Example 2.9.

- Deﬁnition 2.8 (Linear forms condition). A weighted hypergraph ν = ν(N) on the hypergraph


system V = V (N) = (J,(Vj(N))j∈J,r,H) is said to obey the H-linear forms condition (or simply the linear forms condition if there is no confusion) if one has

E

νe(xe(ω))ne,ω x(0)J ,x(1)J ∈ VJ = 1 + o(1) (4)

e∈H ω∈{0,1}e

for any choices of exponents ne,ω ∈ {0,1}.

- Example 2.9. Let H be the set of all pairs in J = {1,2,3}. The linear forms condition says that


E

νij(xi,xj)νij(x′i,xj)νij(xi,x′j)νij(x′i,x′j) x1,x′1 ∈ V1, x2,x′2 ∈ V2, x3,x′3 ∈ V3 = 1+o(1)

ij=12,13,23

and similarly if one or more of the twelve ν factors are deleted. This expression represents the weighted homomorphism density of K2,2,2 in the weighted tripartite graph given by ν, as illustrated in Figure 1(b) (the vertices of K2,2,2 must map into the corresponding parts). Deleting some ν factors corresponds to considering various subgraphs of K2,2,2, e.g., Figure 1(c).

In general, the H-linear forms condition says that ν has roughly the expected density for the 2-blow-up3 of H as well as any subgraph of the 2-blow-up. Our linear forms condition for hypergraphs coincides with the one used by Tao [47, Def. 2.8], although in [47] one assumes additional pseudorandomness hypotheses on ν known as the dual function condition and the correlation condition.

- 2.3. Hypergraph removal lemma. The hypergraph removal lemma was ﬁrst proved by Gowers [20] and by Nagle, Ro¨dl, Schacht, and Skokan [34, 36, 37]. It states that for every r-uniform hypergraph H on h vertices, every r-uniform hypergraph on n vertices with o(nh) copies of H can be made H-free by removing o(nr) edges. As ﬁrst explicitly stated and proved by Tao [48], the proof of the hypergraph removal lemma further gives that the edges can be removed in a low complexity way (this idea will soon be made formal). We will use a slightly stronger version, where edges are given weights in the interval [0,1]. This readily follows from the usual version by a simple rounding argument, as done in [47, Thm. 3.7]. We state this result as Theorem 2.11 below.


Deﬁnition 2.10. For any set e of size r and any Ee ⊆ Ve = j∈e Vj, we deﬁne the complexity of Ee to be the minimum integer T such that there is a partition of Ee into T sets Ee,1,... ,Ee,T, so that each Ee,i is the set of r-cliques of some (r − 1)-uniform hypergraph, meaning that there exists some Bf,i ⊆ Vf for each f ∈ ∂e so that 1Ee,i(xe) = f∈∂e 1Bf,i(xf) for all xe ∈ Ve.

![image 4](<2013-conlon-relative-szemer-theorem_images/imageFile4.png>)

3By the 2-blow-up of H we mean the hypergraph consisting of vertices j(0), j(1) for each j ∈ J, and edges e(ω) := {j(ωj) : j ∈ e} for any e ∈ H and ω ∈ {0, 1}e. We actually do not need the full strength of this assumption. It suﬃces to assume that ν has roughly the expected density for any subgraph of a weak 2-blow-up of H, where by a weak 2-blow-up we mean the following. Fix some edge e1 ∈ H (we will need to assume the condition for all e1). The weak 2-blow-up of H with respect to e1 is the subgraph of the usual 2-blow-up consisting of all edges e(ω) where ωi = ωj for any i, j ∈ e \ e1. This weaker version of the H-linear forms condition is all we shall use for the proof, although everything to follow will be stated as in Deﬁnition 2.8 for clarity.

- Theorem 2.11 (Weighted hypergraph removal lemma). For every ǫ > 0 and ﬁnite set J, there

exists δ > 0 and T > 0 such that the following holds. Let V = (J,(Vj)j∈J,r,H) be a hypergraph system. Let g be a weighted hypergraph on V satisfying 0 ≤ g ≤ 1 and

E

e∈H

ge(xe) x ∈ VJ ≤ δ.

Then for each e ∈ H there exists a set Ee′ ⊆ Ve for which Ve \ Ee′ has complexity at most T and such that

e∈H

1E′

e(xe) = 0 for all x ∈ VJ and for all e ∈ H one has

E[ge(xe)1Ve\E′

e

(xe)|xe ∈ Ve] ≤ ǫ.

We prove a relativized extension of the hypergraph removal lemma. A relative hypergraph removal lemma was already established by Tao in [47], where he assumed the majorizing measure satisﬁes three conditions: the linear forms condition, the correlation condition, and the dual function condition. We again show that a linear forms condition is suﬃcient.

- Theorem 2.12 (Relative hypergraph removal lemma). For every ǫ > 0 and ﬁnite set J, there


exists δ > 0 and T > 0 such that the following holds. Let V = (J,(Vj)j∈J,r,H) be a hypergraph system. Let ν and g be weighted hypergraphs on V . Suppose 0 ≤ g ≤ ν, ν satisﬁes the H-linear forms condition, and N is suﬃciently large. If

E

ge(xe) x ∈ VJ ≤ δ,

e∈H

- then for each e ∈ H there exists a set Ee′ ⊆ Ve for which Ve \Ee′ has complexity at most T and such that

e∈H

1E′

e(xe) = 0 for all x ∈ VJ and for all e ∈ H one has

E[ge(xe)1Ve\E′

e

(xe)|xe ∈ Ve] ≤ ǫ.

In Section 4 we will deduce Theorem 2.12 from Theorem 2.11 by applying the weak regularity lemma and the counting lemma which are stated in the next two subsections.

- 2.4. Weak hypergraph regularity. The Frieze-Kannan weak regularity lemma [16] allows one


- to approximate in cut-norm a matrix (or graph) with entries in the interval [0,1] by another matrix of low complexity. A major advantage over simply applying Szemere´di’s regularity lemma is that the complexity has only an exponential dependence on the approximation parameter, as opposed to the tower-type bound that is incurred by Szemere´di’s regularity lemma. Unfortunately, these regularity lemmas are not meaningful for sparse graphs as the error term is too large in this setting. Following sparse extensions of Szemere´di’s regularity lemma by Kohayakawa [26] and Ro¨dl, a sparse extension of the weak regularity lemma was proved by Bollob´s and Riordan [3] and by Coja-Oghlan, Cooper, and Frieze [6]. In [6], they further generalize this to r-dimensional tensors (or r-uniform hypergraphs), but it only gives an approximation which is close in density on all hypergraphs induced by large vertex subsets. In order to prove a relative hypergraph removal lemma, we will need a stronger approximation, which is close in density on all dense r-uniform hypergraphs formed by the clique set of some (r − 1)-uniform hypergraph. In Section 5, we will prove a more general sparse regularity lemma. For now, we state the result in the form that we need.


The weak regularity lemma approximates a weighted hypergraph g on V by another weighted hypergraph g˜ of bounded complexity which satisﬁes 0 ≤ g˜ ≤ 1. One can think of g˜ as a dense approximation of g. The following deﬁnition makes precise in what sense g˜ approximates g.

- Deﬁnition 2.13 (Discrepancy pair). Let e be a ﬁnite set and ge,g˜e: j∈e Vj → R≥0 be two nonnegative functions. We say that (ge,g˜e) is an ǫ-discrepancy pair if for all subsets Bf ⊆ Vf,

- f ∈ ∂e, one has


E (ge(xe) − g˜e(xe))

f∈∂e

1Bf(xf) xe ∈ Ve ≤ ǫ. (5)

For two weighted hypergraphs g and g˜ on (J,(Vj)j∈J,r,H), we say that (g,g˜) is an ǫ-discrepancy pair if (ge,g˜e) is an ǫ-discrepancy pair for all e ∈ H.

One needs an additional hypothesis on g in order to prove a weak regularity lemma. The condition roughly says that g contains “no dense spots.”

- Deﬁnition 2.14 (Upper regular). Let e be a ﬁnite set, ge: j∈e Vj → R≥0 a nonnegative function, and η > 0. We say that ge is upper η-regular if for all subsets Bf ⊆ Vf, f ∈ ∂e, one has


E (ge(xe) − 1)

f∈∂e

1Bf(xf) xe ∈ Ve ≤ η. (6)

A hypergraph g on on (J,(Vj)j∈J,r,H) is upper η-regular if ge is upper η-regular for all e ∈ H.

Note that unlike (5), there is no absolute value on the left-hand side of (6). The upper regularity hypothesis is needed for establishing the sparse regularity lemma. Fortunately, this mild hypothesis is automatically satisﬁed in our setting. We will say more about this in Section 6.2.

Lemma 2.15. Let V = (J,(Vj)j∈J,r,H) be a hypergraph system. Let ν and g be weighted hypergraphs on V . Suppose 0 ≤ g ≤ ν and ν satisﬁes the H-linear forms condition. Then g is upper o(1)-regular.

Deﬁne the complexity of a function g: Ve → [0,1] to be the minimum T such that there is a partition of Ve into T subgraphs S1,... ST, each of which is the set of r-cliques of some (r − 1)uniform hypergraph (see Deﬁnition 2.10), and such that g is constant on each Si. We state the regularity lemma below with a complexity bound on g˜, although the complexity bound will not actually be needed for our application.

- Theorem 2.16 (Sparse weak regularity lemma). For any ǫ > 0 and function g: V1×···×Vr → R≥0 which is upper η-regular with η ≤ 2−40r/ǫ2, there exists g˜: V1 × ··· × Vr → [0,1] with complexity at most 220r/ǫ2 such that (g,g˜) is an ǫ-discrepancy pair. The special case r = 2 is the sparse extension of the Frieze-Kannan weak regularity lemma.

2.5. Counting lemma. Informally, the counting lemma says that if (g,g˜) is an ǫ-discrepancy pair, with the additional assumption that g ≤ ν and g˜ ≤ 1, then the density of H in g˜ is close to the density of H in g. This sparse counting lemma is perhaps the most novel ingredient in this paper.

- Theorem 2.17 (Counting lemma). For every γ > 0 and ﬁnite set J, there exists an ǫ > 0 so


that the following holds. Let V = (J,(Vj)j∈J,r,H) be a hypergraph system and ν, g, g˜ be weighted hypergraphs on V . Suppose that ν satisﬁes the H-linear forms condition and N is suﬃciently large. Suppose also that 0 ≤ g ≤ ν, 0 ≤ g˜ ≤ 1, and (g,g˜) is an ǫ-discrepancy pair. Then

E

ge(xe) x ∈ VJ − E

e∈H

g˜e(xe) x ∈ VJ ≤ γ. (7)

e∈H

As a corollary, Theorem 2.17 also holds if the hypothesis 0 ≤ g˜ ≤ 1 is replaced by 0 ≤ g˜ ≤ ν. Indeed, we can use the weak regularity lemma, Theorem 2.16, to ﬁnd a common 1-bounded approximation to g and g˜. The result then follows from Theorem 2.17 and the triangle inequality.

To summarize, to get a counting lemma for a ﬁxed hypergraph H in a subgraph of a pseudorandom host hypergraph, it suﬃces to know that the host hypergraph has approximately the expected count for a somewhat larger family of hypergraphs (namely, subgraphs of the 2-blow-up of H).

3. The relative Szemer´edi theorem

In this section, we deduce the relative Szemere´di theorem, Theorem 2.4, from the relative hypergraph removal lemma, Theorem 2.12. We use the relative hypergraph removal lemma to prove a relative arithmetic removal lemma, Theorem 3.3. This result then easily implies a relative version of the multidimensional Szemere´di theorem of Furstenberg and Katznelson [17]. This is Theorem 3.1 below. The relative Szemere´di theorem, Theorem 2.4, follows as a special case of Theorem 3.1 by setting Z = Z′ = ZN and φj(d) = (j − 1)d. One may easily check that the linear forms condition for the resulting hypergraph is satisﬁed if ν : ZN → R≥0 satisﬁes the k-linear forms condition.

The statement and proof of Theorem 3.1 closely follows the write-up in Tao [47, Thm 2.18], adapted in a straightforward way to our new pseudorandomness conditions as well as to the slightly more general setting of functions instead of subsets. Earlier versions of this type of argument for deducing Szemere´di-type results (in the dense setting) from graph and hypergraph removal lemmas were given by Ruzsa and Szemere´di [38], Frankl and Ro¨dl [15], and Solymosi [44, 43].

- Theorem 3.1 (Relative multidimensional Szemere´di theorem). For a ﬁnite set J and δ > 0, there exists c > 0 so that the following holds. Let Z,Z′ be two ﬁnite additive groups and let (φj)j∈J be a ﬁnite collection of group homomorphisms φj : Z → Z′ from Z to Z′. Assume that the elements {φi(d)−φj(d) : i,j ∈ J,d ∈ Z} generate Z′ as an abelian group. Let ν : Z′ → R≥0 be a nonnegative function with the property that in the hypergraph system V = (J,(Vj)j∈J,r,H), with Vj := Z, r := |J| − 1, and H := Jr , the weighted hypergraph (νe)e∈H deﬁned by


νJ\{j}((xi)i∈J\{j}) := ν

(φi(xi) − φj(xi))

i∈J\{j}

satisﬁes the H-linear forms condition. Assume that N is suﬃciently large. Then, for any f : Z′ → R≥0 satisfying 0 ≤ f(x) ≤ ν(x) for all x ∈ Z′ and E[f] ≥ δ,

E

f(a + φj(d)) a ∈ Z′,d ∈ Z ≥ c. (8)

j∈J

- Example 3.2. Let S ⊂ ZN × ZN. Suppose the associated measure ν = |NS|1S satisﬁes E[ν(x,y)ν(x′,y)ν(x,y′)ν(x′,y′)ν(x,z − x)ν(x′,z − x′)ν(x,z′ − x)ν(x′,z′ − x′)


![image 5](<2013-conlon-relative-szemer-theorem_images/imageFile5.png>)

· ν(z − y,y)ν(z − y′,y′)ν(z′ − y,y)ν(z′ − y′,y′)|x,x′,y,y′,z,z′ ∈ ZN] = 1 + o(1)

and similar conditions hold if any subset of the twelve ν factors in the expectation are erased. Then any corner-free subset of S has size o(|S|). Here a corner in Z2N is a set of the form {(x,y),(x + d,y),(x,y +d)} for some d = 0. This claim follows from Theorem 3.1 by setting Z = ZN, Z′ = Z2N, φ0(d) = (0,0), φ1(d) = (d,0), φ2(d) = (0,d).

As in [47, Remark 2.19], we note that the hypothesis that {φi(d) − φj(d) : i,j ∈ J,d ∈ Z} generate Z′ can be dropped by foliating Z′ into cosets. However, this results in a change to the linear forms hypothesis on ν, namely, that it must be assumed on every coset.

We shall prove Theorem 3.1 by proving a somewhat more general removal-type result for arithmetic patterns.

- Theorem 3.3 (Relative arithmetic removal lemma). For every ﬁnite set J and ǫ > 0, there exists c > 0 so that the following holds. Let Z,Z′,(φj)j∈J,ν be the same as in Theorem 3.1. For any collection of functions {fj : Z′ → R≥0}j∈J satisfying 0 ≤ fj(x) ≤ ν(x) for all x ∈ Z′ and j ∈ J, and such that


fj(a + φj(d)) a ∈ Z′,d ∈ Z ≤ c (9)

E

j∈J

one can ﬁnd Aj ⊆ Z′ for each j ∈ J so that

1Aj(a + φj(d)) = 0 for all a ∈ Z′,d ∈ Z (10) and

j∈J

E[fj(x)1Z′\Aj(x)|x ∈ Z′] ≤ ǫ for all j ∈ J. (11)

Theorem 3.1 follows from Theorem 3.3 by setting fj = f for all j ∈ J and ǫ < δ/(r+1). Indeed, if the conclusion (8) fails, then Theorem 3.3 implies that there exists Aj ⊆ Z′ for each j ∈ J satisfying (10) and (11). The Aj’s cannot have a common intersection, or else (10) fails for d = 0. It follows that {Z′ \ Aj : j ∈ J} covers Z′, and hence (11) implies that E[f] ≤ j E[fj1Z′\Aj] ≤ (r + 1)ǫ < δ, which contradicts the hypothesis E[f] ≥ δ.

Proof of Theorem 3.3. Let V = (J,(Vj),r,H) be as in the statement of Theorem 3.1. Write ej := J \ {j} ∈ H. Deﬁne the weighted hypergraph g on V by setting

gej(xej) := fj(ψj(xej)) for all j ∈ J where ψj : Vej → Z′ is deﬁned by

ψj(xej) =

(φi(xi) − φj(xi)) = a + φj(d) (12)

i∈ej

where

φi(xi) and d = −

xi. (13) Then, for all x ∈ V and a,d deﬁned in (13), we have

a =

i∈J

i∈J

gej(xej) =

j∈J

fj(a + φj(d)). (14)

j∈J

The homomorphism x  → (a,d): V → Z′ × Z given by (13) is surjective: the image contains {(φi(d) − φj(d),0) : i,j ∈ J,d ∈ Z} and hence all of Z′ × {0}. Moreover, the image also contains {(−φi(d),d) : i ∈ J,d ∈ Z}. Together, these sets generate all of Z′ × Z. It follows that (a,d) varies uniformly over Z′ × Z as x varies uniformly over VJ, and so (14) implies that

E

gej(xej) x ∈ VJ = E

j∈J

fj(a + φj(d)) a ∈ Z′,d ∈ Z ≤ c.

j∈J

By the relative hypergraph removal lemma, for c small enough (depending on J and ǫ), we can ﬁnd a subset Ej′ ⊂ Vej for each j ∈ J such that

(xej) = 0 for all x ∈ VJ (15) and

1E′

j

j∈J

E[gej(xej)1Ve

j\Ej′(xej)|xej ∈ Vej] ≤ ǫ/(r + 1) for all j ∈ J. For each j ∈ J, deﬁne Aj ⊆ Z′ by

Aj := {z′ ∈ Z′ : |ψj−1(z′) ∩ Ej′| > r+1r |ψj−1(z′)|}. (16) In other words, Aj contains z′ ∈ Z′ if the hypergraph removal lemma removes less than a 1/(r +1) fraction of the edges in Vej representing z′ via ψj.

![image 6](<2013-conlon-relative-szemer-theorem_images/imageFile6.png>)

For any z′ ∈ Z′ \ Aj, on the ﬁber ψ−1(z′) the function gej takes the common value fj(z′). Furthermore, by (16), on this ﬁber, the expectation of 1Ve

j\Ej′ is at least 1/(r + 1). Hence E[fj(x)1Z′\Aj(x)|x ∈ Z′] ≤ (r + 1)E[gej(xej)1Ve

j\Ej′(xej)|xej ∈ Vej] ≤ ǫ.

This proves (11). To prove (10), suppose for some a ∈ Z′,d ∈ Z we have a + φj(d) ∈ Aj for all j ∈ J. Let VJa,d ⊂ VJ consist of all x ∈ VJ satisfying (13). Then ψj(xej) = a+φj(d) for all x ∈ VJa,d by (12), and in fact ψj−1(a + φj(d)) is the projection of VJa,d onto Vej. By (16), more than an r+1r fraction of this projection is in Ej′. It follows by the pigeonhole principle (or a union bound on the complement) that there exists some x ∈ VJa,d such that xej ∈ Ej′ for every j ∈ J. But this contradicts (15). Thus (10) holds.

![image 7](<2013-conlon-relative-szemer-theorem_images/imageFile7.png>)

4. The relative hypergraph removal lemma

Proof of Theorem 2.12. By Lemma 2.15, ν is upper o(1)-regular, so we can apply the weak sparse hypergraph regularity lemma (Theorem 2.16) to ﬁnd functions g˜e : Ve → [0,1] for every e ∈ H so that (g,g˜) is an o(1)-discrepancy pair. By the counting lemma (Theorem 2.17), we have

E

g˜e(xe) x ∈ VJ = E

e∈H

ge(xe) x ∈ VJ + o(1) ≤ δ + o(1).

e∈H

The dense weighted hypergraph removal lemma (Theorem 2.11) tells us that for each e ∈ H we can choose Ee′ ⊂ Ve for which Ve \ Ee′ has complexity Oδ(1) (i.e., at most some constant depending on δ) and such that

e(xe) = 0 for all x ∈ VJ and, as long as δ is small enough and N is large enough, we have E[˜ge(xe)1Ve\E′

1E′

e∈H

(xe)|xe ∈ Ve] ≤ ǫ/2 for all e ∈ H. (17)

e

As Ve \ Ee′ has complexity Oδ(1), there is a partition of Ve \ Ee′ into Oδ(1) hypergraphs Fei each of which is the set of r-cliques of some (r − 1)-uniform hypergraph. We have

|E[(˜ge − ge)(xe)1Ve\E′

(xe)|xe ∈ Ve]| ≤

e

i

|E[(˜ge − ge)(xe)1Fei(xe)|xe ∈ Ve]|

≤

i

o(1) = Oδ(1)o(1) ≤ ǫ/2 for all e ∈ H. (18)

We used that (ge,g˜e) is an o(1)-discrepancy pair on each of the terms of the sum, and the ﬁnal inequality is true as long as N is large enough. Combining (17) and (18) we obtain

E[ge(xe)1Ve\E′

(x)|xe ∈ Ve] ≤ ǫ for all e ∈ H. This proves the claim.

e

5. The weak regularity lemma

Let X be a ﬁnite set and g : X → R≥0. Let F be a family of subsets of X which is closed under intersection, X ∈ F, all subsets of X of size one are in F, and such that, for every S ∈ F, there is a partition of X which contains S and consists of members of F. For t ≥ 2, the family F is t-splittable if for every S ∈ F there is a partition P of X into members of F such that S ∈ P and |P| ≤ t. The complexity p = p(f) of a function f : X → R≥0 is the minimum p for which there is a partition X = S1 ∪ ··· ∪ Sp into p subsets each in F such that f is constant on each Si. We call (g,g˜) an ǫ-discrepancy pair if for all A ∈ F,

E[(g − g˜)1A] ≤ ǫ. All expectations are done with the uniform measure on X. For P a partition of X, let gP be the function on X given by gP(x) = EE[[1g1A]

A] when x ∈ A ∈ P. That is, gP(x) is the conditional expectation of g(x) given the partition P and is constant on any part A of the partition.

![image 8](<2013-conlon-relative-szemer-theorem_images/imageFile8.png>)

The function g we call upper η-regular if for every A ∈ F, we have E[g1A] ≤ E[1A] + η. If g is upper η-regular, A,B ∈ F, and F is t-splittable, then E[g1B\A] ≤ E[1B\A] + (t − 1)η. (19)

Indeed, in this case B \ A can be partitioned into t − 1 sets in F (we ﬁrst split with respect to A and then consider the intersections of the parts of the partition with B). Applying the upper η-regularity condition to each of these sets and summing up the inequalities, we arrive at (19).

Following Scott [41], let φ : R≥0 → R≥0 be the convex function given by

φ(u) =

u2 if u ≤ 2, 4u − 4 otherwise.

For a partition P of X, let φ(P) = E[φ(gP)], which is the mean φ-density of g with respect to the partition P. As φ takes only nonnegative values and φ(u) ≤ 4u, we have

0 ≤ φ(P) ≤ 4E[gP] = 4E[g]. Also, by the convexity of φ, it follows that if P′ is a reﬁnement of P, then φ(P′) ≥ φ(P).

- Lemma 5.1. Let X and F as above be such that F is t-splittable. Let 0 < ǫ,η < 1 and T = t20/ǫ2.


For any g : X → R≥0 which is upper η-regular with η ≤ 8tTǫ , there is g˜ : X → [0,1] with complexity

![image 9](<2013-conlon-relative-szemer-theorem_images/imageFile9.png>)

- at most T such that (g,g˜) is an ǫ-discrepancy pair.


Proof. Let α = ǫ42. We ﬁrst ﬁnd a partition P of X into members of F with |P| ≤ t5/α = T such that for any reﬁnement P′ of P into members of F with |P′| ≤ t|P|, we have φ(P′) − φ(P) < α.

![image 10](<2013-conlon-relative-szemer-theorem_images/imageFile10.png>)

In order to construct P, we ﬁrst recursively construct a sequence P0,P1,... of ﬁner partitions of X into members of F so that |Pj| ≤ tj and φ(Pj) ≥ jα. We begin by considering the trivial partition P0 = {X}, which satisﬁes φ(P0) ≥ 0. At the beginning of step j + 1, we have a partition Pj of X into members of F with |Pj| ≤ tj and φ(Pj) ≥ jα. If there exists a reﬁnement Pj+1 of X into members of F with |Pj+1| ≤ t|Pj| and φ(Pj+1) ≥ φ(Pj) + α, then we continue to step j + 2. Otherwise, we may pick P = Pj to be the desired partition. Note that this process must stop after

- at most 5/α steps since 5 > 4(1 + η) ≥ 4E[g] ≥ φ(Pj) ≥ jα, where the second inequality follows from g being upper η-regular. We therefore arrive at the desired partition P.


Let P : X = S1 ∪ ··· ∪ Sp. Let g˜ : X → [0,1], where g˜ = gP ∧ 1 is the minimum of gP and

the constant function 1. We will show that (gP,g˜) is an 4ǫ-discrepancy pair and (gP,g) is a 34ǫdiscrepancy pair, which implies by the triangle inequality that (g,g˜) is an ǫ-discrepancy pair. As g˜

![image 11](<2013-conlon-relative-szemer-theorem_images/imageFile11.png>)

![image 12](<2013-conlon-relative-szemer-theorem_images/imageFile12.png>)

has complexity at most |P| ≤ T, this will complete the proof.

We ﬁrst show (gP,g˜) is an 4ǫ-discrepancy pair. Note that gP − g˜ is nonnegative and constant on each part of P. If Si ∈ P and gP − g˜ > 0 on Si, then also gP > 1 and g˜ = 1 on Si. As g is upper η-regular, we have E[g1Si] ≤ E[1Si] + η and hence E[(g − g˜)1Si] ≤ η. Therefore, by summing over all parts in the partition P, we see that if A ∈ F,

![image 13](<2013-conlon-relative-szemer-theorem_images/imageFile13.png>)

ǫ 4

0 ≤ E[(gP − g˜)1A] ≤ E[(gP − g˜)] ≤ η|P| ≤ ηT ≤

,

![image 14](<2013-conlon-relative-szemer-theorem_images/imageFile14.png>)

and (gP,g˜) is an 4ǫ-discrepancy pair.

![image 15](<2013-conlon-relative-szemer-theorem_images/imageFile15.png>)

We next show that (gP,g) is a 34ǫ-discrepancy pair, which completes the proof. Suppose for contradiction that there is A ∈ F such that

![image 16](<2013-conlon-relative-szemer-theorem_images/imageFile16.png>)

- 3ǫ

![image 17](<2013-conlon-relative-szemer-theorem_images/imageFile17.png>)

- 4


|E[(gP − g)1A]| >

. Let B be the union of all Si ∩ A, where Si ∈ P, for which both E[1Si∩A] ≥ tη and E[1Si\A] ≥ tη.

We claim that for each Si ∈ P, we have |E[(gP − g)(1A∩Si − 1B∩Si)]| ≤ 2tη. (20)

Indeed, if B ∩ Si = A ∩ Si, then the left hand side of (20) is 0. Otherwise, E[1A∩Si] ≤ tη or E[1Si\A] ≤ tη. In the ﬁrst case, when E[1A∩Si] ≤ tη, we have 1B∩Si is identically 0, as well as

E[g1A∩Si] ≤ E[1A∩Si] + η ≤ (t + 1)η and

E[g1Si] E[1Si]

(E[1Si] + η) E[1Si]

E[gP1A∩Si] =

E[1A∩Si] ≤

E[1A∩Si] ≤ E[1A∩Si] + η ≤ (t + 1)η,

![image 18](<2013-conlon-relative-szemer-theorem_images/imageFile18.png>)

![image 19](<2013-conlon-relative-szemer-theorem_images/imageFile19.png>)

from which (20) follows. In the second case, when E[1Si\A] ≤ tη, we again have 1B∩Si is identically 0, so that

E[(g − gP)(1A∩Si − 1B∩Si)] = E[(g − gP)1A∩Si] = E[(g − gP)(1Si − 1Si\A)]

= E[(g − gP)1Si] − E[(g − gP)1Si\A] = −E[(g − gP)1Si\A], and similar to the ﬁrst case, using (19) to estimate E[g1Si\A] and E[gP1Si\A], we get (20).

Notice that

ǫ 4

|E[(gP − g)1A] − E[(gP − g)1B]| = |E[(gP − g)(1A − 1B)]| ≤ |P|2tη ≤

,

![image 20](<2013-conlon-relative-szemer-theorem_images/imageFile20.png>)

where the ﬁrst inequality follows by using (20) for each part Si and the triangle inequality. Hence,

ǫ 4

ǫ 2

- 3ǫ

![image 21](<2013-conlon-relative-szemer-theorem_images/imageFile21.png>)

- 4


|E[(gP − g)1B]| ≥ |E[(gP − g)1A]| − |E[(gP − g)1A] − E[(gP − g)1B]| >

−

=

.

![image 22](<2013-conlon-relative-szemer-theorem_images/imageFile22.png>)

![image 23](<2013-conlon-relative-szemer-theorem_images/imageFile23.png>)

Let Pˆ be the reﬁnement of P where Si is also in Pˆ if B ∩Si = ∅ and otherwise Si ∩B and Si \B are parts of Pˆ, and let P′ be a reﬁnement of Pˆ into at most t|P| members of F. The reﬁnement P′ exists as F is t-splittable and is closed under intersections, P consists of members of F, A ∈ F, and Si ∩ B = Si ∩ A ∈ F if Si ∩ B ∈ Pˆ. As P′ is a reﬁnement of Pˆ which is a reﬁnement of P, we have φ(P′) ≥ φ(Pˆ) ≥ φ(P). Let R ∈ {Si,Si ∩ B,Si \ B}, where Si is a part of P that is reﬁned into two parts in Pˆ, so that E[1R] ≥ tη. Letting u = EE[[1g1R]

R] , we see, since g is upper η-regular and using (19), that u ≤ 1 + tη(tη)−1 = 2 and hence φ(u) = u2. It follows, by considering the functions pointwise, that φ(gPˆ) − φ(gP) = gP2ˆ − gP2 . Hence,

![image 24](<2013-conlon-relative-szemer-theorem_images/imageFile24.png>)

φ(P′) − φ(P) ≥ φ(Pˆ) − φ(P) = E[gP2ˆ] − E[gP2 ] = E[gP2ˆ − gP2 ] = E[ gPˆ − gP 2] ≥ E[(gPˆ − gP)1B]2 = E[(g − gP)1B]2 >

ǫ2 4

= α.

![image 25](<2013-conlon-relative-szemer-theorem_images/imageFile25.png>)

The third equality above is the Pythagorean identity, which uses that Pˆ is a reﬁnement of P, and the second inequality is an application of the Cauchy-Schwarz inequality. However, since P′ is a reﬁnement of P consisting of members of F with |P′| ≤ t|P|, this contradicts φ(P′) − φ(P) < α from the deﬁnition of P and completes the proof.

To establish the weak hypergraph regularity lemma, Theorem 2.16, we use Lemma 5.1 with X = V1×···×Vr and F being the family of subsets of X which form the r-cliques of some r-partite (r − 1)-uniform hypergraph with parts V1,... ,Vr. Noting that F is 2r-splittable in this case, we obtain Theorem 2.16.

6. The counting lemma The three main ingredients in our proof of the counting lemma (Theorem 2.17) are as follows.

- (1) A standard telescoping argument [4] in the dense case, i.e., when ν = 1.
- (2) Repeated applications of the Cauchy-Schwarz inequality. This is a standard technique in this area, e.g., [19, 20, 24, 47].
- (3) Densiﬁcation. This is the main new ingredient in our proof. At each step, we reduce the problem of counting H in a particular weighted hypergraph to that of counting H in a modiﬁed weighted hypergraph. For an edge e ∈ H, we replace the triple (νe,ge,g˜e) by a new triple (1,ge′ ,g˜e′) with 0 ≤ ge′,g˜e′ ≤ 1 and such that (ge′ ,g˜e′) is an ǫ′-discrepancy pair for some ǫ′ = oǫ→0(1). By repeatedly applying this reduction to all e ∈ H (we use induction), we reduce the counting lemma to the dense case.


We developed the densiﬁcation technique in our earlier paper [7], where we proved a sparse counting lemma in graphs. We have signiﬁcantly simpliﬁed a number of technical steps from [7] in order to extend the densiﬁcation technique to hypergraphs here.

- 6.1. Telescoping argument. The following argument allows us to prove the counting lemma in the dense case, i.e., when 0 ≤ g ≤ 1.


- Lemma 6.1 (Telescoping discrepancy argument for dense hypergraphs). Theorem 2.17 holds if we assume that there is some e1 ∈ H so that νe = 1 for all e ∈ H \ {e1}. In fact, in this case,


E

ge(xe) x ∈ VJ − E

e∈H

g˜e(xe) x ∈ VJ ≤ |H|ǫ. (21)

e∈H

- Lemma 6.1 uses only the assumption that (ge,g˜e) is an ǫ-discrepancy pair for every e ∈ H and


nothing about the linear forms condition on ν. Recall that for each ﬁxed e ∈ H, the condition that (ge,g˜e) is an ǫ-discrepancy pair means that for all subsets Bf ⊆ Vf, f ∈ ∂e, we have

E (ge(xe) − g˜e(xe))

f∈∂e

1Bf(xf) xe ∈ Ve ≤ ǫ. (22)

This is equivalent to the condition that for all functions uf : Vf → [0,1], f ∈ ∂e, we have E (ge(xe) − g˜e(xe))

uf(xf) xe ∈ Ve ≤ ǫ. (23)

f∈∂e

Indeed, the expectation is linear in each uf and hence the extrema occur when the uf’s are {0,1}valued, thereby reducing to (22).

Proof. Let h = |H| and order the edges of H \ {e1} arbitrarily as e2,... ,eh. We can write the left-hand side of (21), without the absolute values, as a telescoping sum

h

E

t=1

t−1

g˜es(xes) (get(xet) − g˜et(xet))

s=1

h

ges(xes) x ∈ VJ . (24)

s=t+1

For the t-th term in the sum, when we ﬁx the value of xJ\et ∈ VJ\et, the expectation has the form E (get(xet) − g˜et(xet))

uf(xf) xet ∈ Vet (25)

f∈∂et

for some functions uf : Vf → [0,1] (here we used the key fact that ges ≤ 1 for all s > 1 and g˜es ≤ 1 for all s). Since (get,g˜et) is an ǫ-discrepancy pair, (23) implies that (25) is bounded in absolute value by ǫ. The same bound holds after we vary xJ\et ∈ VJ\et. So every term in (24) is bounded by ǫ in absolute value, and hence (24) is at most hǫ in absolute value.

- 6.2. Strong linear forms. The main result of this subsection tells us that ν can be replaced by the constant function 1 in counting expressions. Though somewhat technical in detail, the main idea of the proof is quite simple and may be summarized as follows: we use the Cauchy-Schwarz inequality to double each vertex j of a certain edge in turn, at each step majorizing those edges which do not contain j. This method is quite standard in the ﬁeld. In the work of Green and Tao, it is used to prove generalized von Neumann theorems [24, Prop. 5.3], [47, Thm. 3.8], although the statement of our lemma is perhaps more similar to the uniform distribution property [24, Prop. 6.2], [47, Prop. 5.1].


We begin by using a similar method to prove a somewhat easier result. It shows that if ν satisﬁes the H-linear forms condition then (ν,1) is an o(1)-discrepancy pair, which implies Lemma 2.15.

- Lemma 6.2. Let e be a ﬁnite set, Vj a ﬁnite set for each j ∈ e, and Ve = j∈e Vj. Then, for any function ν : Ve → R and any collection of Bf ⊆ Vf for f ∈ ∂e,


E (νe(xe) − 1)

f∈∂e

1Bf(xf) xe ∈ Ve ≤ E

(νe(xe(ω)) − 1) x(0)e ,x(1)e ∈ Ve

ω∈{0,1}e

1/2|e|

. (26)

- Lemma 6.2 follows from a direct application of the Gowers-Cauchy-Schwarz [19] inequality for

hypergraphs (see [8]). We include the proof here for completeness.

Proof. For ∅ ⊆ d ⊆ e, let

Xd :=

ω∈{0,1}d

(ve(xe\d,xd(ω)) − 1), Yd :=

f∈∂e f⊇d

ω∈{0,1}d

1Bf(xf\d,xd(ω)),

and

Qd := E[XdYd|xe\d ∈ Ve\d, x(0)d ,x(1)d ∈ Vd]. Then (26) can be written as |Q∅| ≤ Q1/2

|e|

e . By induction, it suﬃces to show that Q2d ≤ Qd∪{j} whenever j ∈ e \ d. Let Yd = Yd∋jYd ∋j where Yd∋j consists of all the factors in Yd that contain xj in the argument, and Yd ∋j consists of all other factors. By the Cauchy-Schwarz inequality, we have

Q2d = E[E[XdYd∋j|xj ∈ Vj]Yd ∋j]2 ≤ E[E[XdYd∋j|xj ∈ Vj]2]E[(Yd ∋j)2] ≤ Qd∪{j},

since Qd∪{j} = E[E[XdYd∋j|xj ∈ Vj]2] and 0 ≤ Yd ∋j ≤ 1, where the outer expectations are taken over all free variables. This shows that Q2d ≤ Qd∪{j}. Hence, |Q∅| ≤ Q1/2

|e|

e , as desired. The next lemma is very similar, except that now we need to invoke the linear forms condition.

- Lemma 6.3 (Strong linear forms). Let V = (J,(Vj)j∈J,r,H) be a hypergraph system and let ν be a weighted hypergraph on V satisfying the linear forms condition. Let e1 ∈ H. For each ι ∈ {0,1} and e ∈ H \ {e1}, let ge(ι): Ve → R≥0 be a function so that either ge(ι) ≤ 1 or ge(ι) ≤ νe holds. Then


ge(ι)(x(eι)) x(0)J ,x(1)J ∈ VJ;x(0)e1 = x(1)e1 = xe1 = o(1). (27)

E (νe1(xe1) − 1)

ι∈{0,1} e∈H\{e1}

In (27) the notation x(0)e1 = x(1)e1 = xe1 means that x(0)j ,x(1)j ,xj are taken to be the same for all j ∈ e1. Recall that we write o(1) for a quantity that tends to zero as N → ∞.

Proof. For each ι ∈ {0,1} and e ∈ H \ {e1}, let g¯e(ι) be either 1 or νe so that ge(ι) ≤ g¯e(ι) holds. For ∅ ⊆ d ⊆ e1, deﬁne

(νe1(xe1\d,xd(ω)) − 1),

Xd :=

ω∈{0,1}d

Yd :=

ι∈{0,1} e∈H\{e1} ω∈{0,1}e∩d

,xd(ω),xe∩e1\d) if e ⊇ d g¯e(ι)(x(eι\)e

ge(ι)(x(eι\)e

1

,xe(ω∩)d,xe∩e1\d) if e d

1

,

and

1)∪d,x(1)(J\e

Qd := E XdYd x(0)(J\e

1)∪d ∈ V(J\e1)∪d, xe1\d ∈ Ve1\d . We observe that Q∅ is equal to the left-hand side of (27) and

Qe1 = E

(νe1(xe(ω1)) − 1)

ω∈{0,1}e1

,xe(ω∩)e1) x(0)J ,x(1)J ∈ VJ = o(1)

g¯e(ι)(x(eι\)e

1

ι∈{0,1} e∈H\{e1} ω∈{0,1}e∩e1

by the linear forms condition (4).4 Indeed, after we expand ω∈{0,1}e1(νe1(xe(ω1)) − 1), every term in Qe1 has the form of (4) (since g¯e(ι) is 1 or νe). Thus Qe1 is the sum of 2|e1| terms, each of which is ±(1 + o(1)) by the linear forms condition, and they cancel accordingly to o(1).

We claim that if j ∈ e1 \ d then

|Qd| ≤ (1 + o(1))Q1d/∪{2j}, (28) from which it would follow by induction that

|LHS of (27)| = |Q∅| ≤ (1 + o(1))Qe11/2r = o(1).

Now we prove (28). Let Yd = Yd∋jYd ∋j where Yd∋j consists of all the factors in Yd that contain xj in the argument, and Yd ∋j consists of all other factors. Using the Cauchy-Schwarz inequality and Yd ∋j ≤ Y  ∋dj one has

![image 26](<2013-conlon-relative-szemer-theorem_images/imageFile26.png>)

Q2d = E[E[XdYd∋j|xj ∈ Vj]Yd ∋j]2 ≤ E[E[XdYd∋j|xj ∈ Vj]2Yd ∋j] E[Yd ∋j]

≤ E[E[XdYd∋j|xj ∈ Vj]2Y  ∋dj] E[Y  ∋dj] = Qd∪{j} E[Y  ∋dj] (29) where the outer expectations are taken over all free variables. The second factor in (29) is 1 + o(1) by the linear forms condition (4) as Y  ∋dj consists only of ν factors. This proves (28).

![image 27](<2013-conlon-relative-szemer-theorem_images/imageFile27.png>)

![image 28](<2013-conlon-relative-szemer-theorem_images/imageFile28.png>)

![image 29](<2013-conlon-relative-szemer-theorem_images/imageFile29.png>)

![image 30](<2013-conlon-relative-szemer-theorem_images/imageFile30.png>)

- 6.3. Counting lemma proof. As already mentioned, the main idea of the following proof is a process called densiﬁcation, where we reduce the problem of counting H in a sparse hypergraph to that of counting H in a dense hypergraph by replacing sparse edges with dense edges one at a time. Several steps are needed to densify a given edge e1. The ﬁrst step is to double all vertices outside of e1 and to majorize ge1 by νe1. We then use the strong linear forms condition to remove the edge corresponding to e1 entirely. This leaves us with the seemingly harder problem of counting the graph H′ consisting of two copies of H\{e1} joined along the vertices of e1. However, an inductive hypothesis tells us that we can count copies of H\{e1}. The core of the proof is in showing that this allows us to replace one of the copies of H\{e1} in H′ by a dense edge, thus reducing our problem to that of counting H with one edge replaced by a dense edge.


![image 31](<2013-conlon-relative-szemer-theorem_images/imageFile31.png>)

4This is where the weak 2-blow-up of H arises, since the estimate Qe1 = o(1) only relies upon knowing that ν has roughly the expected density for certain subgraphs of the weak 2-blow-up.

Proof of Theorem 2.17. We use induction on |{e ∈ H : νe = 1}|. When |{e ∈ H : νe = 1}| = 0 or 1, the result follows from Lemma 6.1. Now take e1 ∈ H so that νe1 = 1.

We assume that |J| is a ﬁxed constant. We write o(1) for a quantity that tends to zero as N → ∞ and oǫ→0(1) for a quantity that tends to zero as N → ∞ and ǫ → 0. We need to show that the following quantity is oǫ→0(1):

E

ge(xe) x ∈ VJ − E

e∈H

g˜e(xe) x ∈ VJ

e∈H

g˜e(xe) x ∈ VJ +E (ge1(xe1)−g˜e1(xe1))

= E ge1(xe1)

ge(xe)−

g˜e(xe) x ∈ VJ .

e∈H\{e1}

e∈H\{e1}

e∈H\{e1}

(30) The second term in (30) is at most ǫ in absolute value since (ge1,g˜e1) is an ǫ-discrepancy pair and

- g˜ ≤ 1 (e.g., see proof of Lemma 6.1). It remains to show that the ﬁrst term in (30) is oǫ→0(1). Deﬁne functions νe′1,ge′1,g˜e′1 : Ve1 → R≥0 by


νe′1(xe1) := E

νe(xe) xJ\e1 ∈ VJ\e1 , (31)

e∈H\{e1}

ge′1(xe1) := E

ge(xe) xJ\e1 ∈ VJ\e1 , (32)

e∈H\{e1}

g˜e′1(xe1) := E

g˜e(xe) xJ\e1 ∈ VJ\e1 . (33)

e∈H\{e1}

We have ge′1 ≤ νe′1 and g˜e1 ≤ 1 (pointwise). In the rest of this proof, unless otherwise speciﬁed, expectations are for functions on Ve1 with arguments varying uniformly over Ve1. The linear forms condition (4) implies that E[νe′1] = 1 + o(1) and E[(νe′1)2] = 1 + o(1), so that5

E[(νe′1 − 1)2] = o(1). (34) The square of the ﬁrst term in (30) equals

E[ge1(ge′1 − g˜e′1)]2 ≤ E[ge1(ge′1 − g˜e′1)2] E[ge1] ≤ E[νe1(ge′1 − g˜e′1)2] E[νe1]

= (E[(ge′1 − g˜e′1)2] + o(1))(1 + o(1)). (35) The ﬁrst inequality above is due to the Cauchy-Schwarz inequality. In the ﬁnal step, both factors are estimated using Lemma 6.3 (for the ﬁrst factor, expand the square (ge′1−g˜e′1)2 and apply Lemma 6.3 term by term). Continuing (35) it suﬃces to show that the following quantity is oǫ→0(1):

E[(ge′1 − g˜e′1)2] = E[(ge′1 − g˜e′1)(ge′1 − ge′1 ∧ 1)] + E[(ge′1 − g˜e′1)(ge′1 ∧ 1 − g˜e′1)] (36)

(here a ∧ b := min{a,b}). That is, we are capping the weighted hypergraph ge′1 by 1. Since νe′1 is very close to 1 by (34), this should not result in a large loss. Indeed, since 0 ≤ ge′1 ≤ νe′1, we have

0 ≤ ge′1 − ge′1 ∧ 1 = max{ge′1 − 1,0} ≤ max{νe′1 − 1,0} ≤ |νe′1 − 1|. (37)

Using (37), ge′1 ≤ νe′1, and g˜e′1 ≤ 1, we bound the magnitude of the ﬁrst term on the right-hand side of (36) by

E[(νe′1 +1) νe′1 − 1 ] = E[(νe′1 −1) νe′1 − 1 ]+2E[ νe′1 − 1 ] ≤ E[(νe′1 −1)2]+2E[(νe′1 −1)2]1/2 = o(1) by the triangle inequality, the Cauchy-Schwarz inequality, and (34). To estimate the second term on the right-hand side of (36), we need the following claim.

![image 32](<2013-conlon-relative-szemer-theorem_images/imageFile32.png>)

5In fact, the only assumptions on ν needed for the proof of Theorem 2.17 are (34) and the strong linear forms condition, Lemma 6.3, as well as analogous conditions for other choices of e1 ∈ H and allowing some subset of the functions νe to be replaced by 1.

Claim. (ge′1 ∧ 1,g˜e′1) is an ǫ′-discrepancy pair with ǫ′ = oǫ→0(1). Proof of Claim. We need to show that, whenever Bf ⊆ Vf for all f ∈ ∂e1, we have

E (ge′1(xe1) ∧ 1 − g˜e′1(xe1))

1Bf(xf) xe1 ∈ Ve1 = oǫ→0(1). (38)

f∈∂e1

Deﬁne ge′′1 : Ve1 → R≥0 by ge′′1(xe1) = f∈∂e

1Bf(xf). So the left-hand side of (38) is equal to E[(ge′1 ∧ 1 − ge′1)ge′′1] + E[(ge′1 − g˜e′1)ge′′1]. (39)

1

Using 0 ≤ ge′′1 ≤ 1, (37), the Cauchy-Schwarz inequality, and (34), we can bound the magnitude of the ﬁrst term in (39) by

E[ νe′1 − 1 ] ≤ E[(νe′1 − 1)2]1/2 = o(1). The second term on the right-hand side of (39) is equal to

E

g˜e(xe) ge′′1(xe1) x ∈ VJ .

ge(xe) −

e∈H\{e1}

e∈H\{e1}

This is oǫ→0(1) by the induction hypothesis applied to new weighted hypergraphs where the old (νe1,ge1,g˜e1) gets replaced by (1,ge′′1,ge′′1), thereby decreasing |{e ∈ H : νe = 1}|. Note that the linear forms condition continues to hold. Thus (38) holds, so (ge′1 ∧ 1,g˜e′1) is an ǫ′-discrepancy pair with ǫ′ = oǫ→0(1).

We expand the second term of (36) as

E[(ge′1 − g˜e′1)(ge′1 ∧ 1 − g˜e′1)] = E[ge′1(ge′1 ∧ 1)] − E[ge′1g˜e′1] − E[˜ge′1(ge′1 ∧ 1)] + E[(˜ge′1)2]. (40) We claim that each expectation on the right-hand side of (40) is E[(˜ge′1)2] + oǫ→0(1). Indeed, by

(32) and (33) we have E[ge′1(ge′1 ∧ 1)] − E[(˜ge′1)2] = E (ge′1(xe1) ∧ 1)

ge(xe) − g˜e′1(xe1)

g˜e(xe) x ∈ VJ ,

e∈H\{e1}

e∈H\{e1}

which is oǫ→0(1) by the induction hypothesis applied to new weighted hypergraphs where the old (νe1,ge1,g˜e1) is replaced by (1,ge′1 ∧1,g˜e′1). This is allowed as (ge′1 ∧1,g˜e′1) is an ǫ′-discrepancy pair with ǫ′ = oǫ→0(1), the new ν still satisﬁes the linear forms condition, and |{e ∈ H : νe = 1}| has decreased. The claims that the other terms on the right-hand side of (40) are each E[(˜ge′1)2]+oǫ→0(1) are similar (in fact, easier). It follows that (40) is oǫ→0(1), so (36) is oǫ→0(1) and we are done.

7. Concluding remarks

Conditions for counting lemmas. In this paper, we determined suﬃcient conditions for establishing a relative Szemere´di theorem and, more generally, a counting lemma for sparse hypergraphs. We have assumed that the hypergraph we want to count within is a subgraph of a pseudorandom hypergraph. The main question then is to determine a good notion of pseudorandomness which is suﬀﬁcient to establish a counting lemma.

There is a marked diﬀerence between this paper and our previous paper on graphs [7] in terms of the type of pseudorandom condition assumed for the majorizing hypergraph. In this paper, we prove a counting lemma for a given hypergraph H by assuming that the underlying pseudorandom hypergraph contains approximately the correct count for each hypergraph in a certain collection of hypergraphs H derived from H. That is, for each H′ ∈ H, we assume that our pseudorandom hypergraph contains (1 + o(1))pe(H′)nv(H′) labeled copies of H′, where p is the edge density of the pseudorandom hypergraph.

The approach used in [7] is equivalent, up to some polynomial loss in ǫ, to assuming that the number of labeled cycles of length 4 in our pseudorandom graph is (1 + ǫ)p4n4, where ǫ is now a carefully controlled term and the question of whether H can be embedded in our pseudorandom

graph depends on whether ǫ is suﬃciently small with respect to H and p. It is possible to adapt the methods of this paper so that the notion of pseudorandomness used for hypergraphs is more closely related to this latter notion. However, for the purposes of applying the results to a relative Szemere´di theorem, the current formulation seemed more appropriate.

Gowers uniformity norms. For a function f : ZN → R, the Gowers Ur-norm of f is deﬁned to be

1/2r

f(x0 + ω · x) x0,x1,... ,xr ∈ ZN

f Ur = E

,

ω∈{0,1}r

where x = (x1,... ,xr). The following inequality, referred to as a generalized von Neumann theorem, bounds the weighted count of (r+1)-term arithmetic progressions from functions f0,... ,fr in terms of the Gowers uniformity norm:

E f0(x)f1(x + d)f2(x + 2d)··· fr(x + rd) x,d ∈ ZN ≤ fj Ur

i =j

fi ∞ .

This fundamental fact is an important starting point for Gowers’ celebrated proof [19] of Szemere´di’s theorem as well as many later developments in additive combinatorics. For a sparse set S ⊆ ZN of density p, this inequality implies the correct count of (r + 1)-term arithmetic progressions in S as long as ν − 1 Ur = o(pr), where ν = p−11S (a more careful analysis shows that it suﬃces to assume ν − 1 Ur = o(pr/2)).

Gowers [21]6 and Green [22] asked if ν − 1 Us = o(1) for some large s = s(r) is suﬃcient for ν to satisfy a relative Szemere´di theorem for (r + 1)-term arithmetic progressions. Note that this is precisely a linear forms condition and we proved in this paper that a diﬀerent linear forms condition is suﬃcient. However, we do not even know if such a condition implies the existence of (r+1)-term arithmetic progressions in ν. Clearly s(r) cannot be too small and indeed we know from the recent work of Bennett and Bohman [2] on the random AP-free process that one can ﬁnd a 3-AP-free S ⊂ ZN such that ν = (N/|S|)1S satisﬁes ν − 1 U2 = o(1). Therefore, if s(2) exists, it must be greater than 2. More generally, they show that s(r) > 1+log2 r. In a companion note [8], we show that if a measure ν satisﬁes the stronger condition ν − 1 Ur = o(pr), where p = ν −∞1, then the relative Szemere´di theorem holds with respect to ν for (r + 1)-term arithmetic progressions. This strengthens the consequence of the generalized von Neumann theorem discussed above.

Corners in products of pseudorandom sets. Example 3.2 illustrates the relative multidimensional Szemere´di theorem applied to a pseudorandom set S ⊂ Z2N. However, the situation is quite diﬀerent for S×S ⊂ Z2N with some pseudorandom set S ⊂ ZN. Indeed, S×S ⊂ Z2N does not satisfy the linear forms condition in Example 3.2. Intuitively, this is because the events (x,y) ∈ S ×S and

- (x,y′) ∈ S × S are correlated as both involve x ∈ S. However, we may still deduce the following result using our relative triangle removal lemma.


Recall that a corner in Z2N is a set of the form {(x,y),(x + d,y),(x,y + d)}, where d = 0. Proposition 7.1. If S ⊂ ZN is such that ν = |NS|1S satisﬁes

![image 33](<2013-conlon-relative-szemer-theorem_images/imageFile33.png>)

E[ν(x)ν(x′)ν(z − x)ν(z − x′)ν(z′ − x)ν(z′ − x′)

· ν(y)ν(y′)ν(z − y)ν(z − y′)ν(z′ − y)ν(z′ − y′)|x,x′,y,y′,z,z′ ∈ ZN] = 1 + o(1) (41) and similar conditions hold if any subset of the ν factors are erased, then any corner-free subset of S × S has size o(|S|2).

Proof (sketch). Let A be a corner-free subset of S × S. We build two tripartite graph Γ and G on the same vertex set X ∪ Y ∪ Z with X = Y = S and Z = ZN (note that unlike the proof of Theorem 3.1 we do not take X and Y to be the whole of ZN here). In Γ, we place a complete

![image 34](<2013-conlon-relative-szemer-theorem_images/imageFile34.png>)

- 6This question can be found in the penultimate paragraph in §4 of the arXiv version of [21].


bipartite graph between X and Y ; between Y and Z the edge (y,z) ∈ Y × Z is present if and only if z − y ∈ S; and between X and Z the edge (x,z) ∈ X × Z is present if and only if z − x ∈ S. In G, between X and Y the edge (x,y) ∈ (X,Y ) is present if and only if (x,y) ∈ A; between Y and Z the edge (y,z) ∈ Y × Z is present if and only if (z − y,y) ∈ A; and between X and Z the edge

- (x,z) ∈ X × Z is present if and only if (x,z − x) ∈ A. The vertices (x,y,z) ∈ X × Y × Z form a triangle if and only if (x,y),(z − y,y),(x,z − x) ∈ A.


These three points form a corner, which is degenerate only when x + y = z. Since A is corner-free, every edge of G is contained in exactly one triangle (namely the one that completes the equation x + y = z). In particular, G contains exactly |A| triangles. After checking some hypotheses, we can apply our relative triangle removal lemma (as a special case of Theorem 2.12) to conclude that it is possible to remove all triangles from G by deleting o(|S|2) edges. Since every edge of G is contained in exactly one triangle, and |G| has 3|A| edges, we have |A| = o(|S|2), as desired.

One can easily generalize the above Proposition to Sm ⊂ ZmN (as before, S ⊂ ZN). Here a corner is a set of the form {x,x + de1,... ,x + dem}, where x ∈ ZN, 0 = d ∈ ZN, and ei is the i-th coordinate vector. Then, for any ﬁxed m, any corner-free subset of Sm must have size o(|S|m),

provided that ν = |NS|1S satisﬁes the linear forms condition

![image 35](<2013-conlon-relative-szemer-theorem_images/imageFile35.png>)

E

m

i=1

xj(ωj))ni,ω

ν(x(0)i )ni,0ν(x(1)i )ni,1

(x(0ω0) −

j∈[m]\{i}

ω∈{0,1}{0}∪[m]\{i}

x(0)0 ,x(1)0 ,... ,x(0)m ,x(1)m ∈ ZN = 1 + o(1) for any choices of exponents ni,0,ni,1,ni,ω ∈ {0,1}.

A more general result concerning the existence of arbitrarily shaped constellations in Sm is known, provided that S satisﬁes certain stronger linear forms hypotheses. We refer the readers to [13, 14, 50] for further details. In particular, the multidimensional relative Szemere´di theorem holds in Pm, where P is the primes.

Sparse graph limits. The regularity method played a fundamental role in the development of the theory of dense graph limits [4, 30]. However, no satisfactory theory of graph limits is known for graphs with edge density o(1). Bollob´s and Riordan [3] asked a number of questions and made explicit conjectures on suitable conditions for sparse graph limits and counting lemmas. Our work gives some natural suﬃcient conditions for obtaining a counting lemma in a sequence of sparse graphs GN. The new counting lemma allows us to transfer the results of Lov´asz and Szegedy [30, 31] on the existence of the limit graphon, as well as the results of Borgs, Chayes, Lov´asz, So´s, and Vesztergombi [4] on the equivalence of left-convergence (i.e., convergence in homomorphism densities) and convergence in cut distance. The famous quasirandomness results of Chung, Graham, and Wilson [5] also transfer, namely, that an appropriate relationship between edge density and C4-density (of homomorphisms) determines the asymptotic F-density for every graph F. We will explain these connections in more detail in an upcoming survey article [9].

Existing applications of the Green-Tao method. Though our discussion has focused on the relative Szemere´di theorem, we have proved a relative version of the stronger multidimensional Szemere´di theorem. Following Tao [47], this may be used to prove that the Gaussian primes contain arbitrarily shaped constellations, though without the need to verify either the correlation condition or the dual function condition. It seems likely that our method could also be useful for simplifying several other papers where the machinery of Green and Tao is used [12, 25, 29, 32, 33, 49]. In some cases it should be possible to use our results verbatim but in others, such as the paper of Tao and Ziegler [49] proving that there are arbitrarily long polynomial progressions in the primes, it will probably require substantial additional work.

Sparse hypergraph regularity. In proving a hypergraph removal lemma for subgraphs of pseudorandom hypergraphs, we have developed a general approach to regularity and counting in sparse pseudorandom hypergraphs which has the potential for much broader application. It is, for example, quite easy to use our results to prove analogues of well-known combinatorial theorems such as Ramsey’s theorem and Tura´n’s theorem relative to sparse pseudorandom hypergraphs of density N−cH. We omit the details. In the graph case, a number of further applications were discussed in [7]. We expect that hypergraph versions of many of these applications should be an easy corollary of our results.

Counting in random hypergraphs. There has been much recent work on counting lemmas and relative versions of combinatorial theorems within random graphs and hypergraphs [1, 10, 11, 39, 40]. Surprisingly, there are a number of disparate approaches to these problems, each having its own strengths and weaknesses. We believe that our results can be used to give an alternative framework for one of these approaches, due to Conlon and Gowers [10].7 Their proof relies heavily upon an application of the Green-Tao transference theorem, which we believe can be replaced with an application of the sparse Frieze-Kannan regularity lemma and our densiﬁcation technique. However, the key technical step in [10], which in our language is to verify that the strong linear forms condition, Lemma 6.3, holds when ν is a random measure, would remain unchanged.

Sparse arithmetic removal. In Theorem 3.3, we proved an arithmetic removal lemma for linear patterns such as arithmetic progressions. More generally, an arithmetic removal lemma claims that if a system of linear equations Ma = b over the integers has a small number of solutions a = (a1,a2,... ,an) with ai ∈ Ai for all i = 1,2,... ,n then one may remove a small number of elements from each Ai to ﬁnd subsets A′i such that there are no solutions a′ = (a′1,a′2,... ,a′n) to Ma′ = b with a′i ∈ A′i for all i = 1,2,... ,n. Such a result was conjectured by Green [23] and proved by Kra´l’, Serra, and Vena [28] and, independently, Shapira [42]. Both of these proofs are based upon representing a system of linear equations by a hypergraph and deducing the arithmetic removal lemma from a hypergraph removal lemma. Such an idea was ﬁrst used by Kra´l’, Serra, and Vena [27] with graphs (instead of hypergraphs). In [7], we adapted the arguments of [27] to sparse pseudorandom subsets of the integers using the removal lemma in sparse pseudorandom graphs. Likewise, our results on hypergraph removal in this paper may be used to prove a sparse pseudorandom generalization of the arithmetic removal lemma [28, 42] for all systems of linear equations.

Acknowledgements. We would like to thank Tom Bohman and Ben Green for helpful discussions. References

- [1] J. Balogh, R. Morris, and W. Samotij, Independent sets in hypergraphs, J. Amer. Math. Soc., to appear.
- [2] P. Bennett and T. Bohman, A note on the random greedy independent set algorithm, arXiv:1308.3732.
- [3] B. Bollob´s and O. Riordan, Metrics for sparse graphs, Surveys in combinatorics 2009, London Math. Soc. Lecture Note Ser., vol. 365, Cambridge Univ. Press, Cambridge, 2009, pp. 211–287.
- [4] C. Borgs, J. T. Chayes, L. Lova´sz, V. T. S´os, and K. Vesztergombi, Convergent sequences of dense graphs. I. Subgraph frequencies, metric properties and testing, Adv. Math. 219 (2008), 1801–1851.
- [5] F. R. K. Chung, R. L. Graham, and R. M. Wilson, Quasi-random graphs, Combinatorica 9 (1989), 345–362.
- [6] A. Coja-Oghlan, C. Cooper, and A. Frieze, An eﬃcient sparse regularity concept, SIAM J. Discrete Math. 23 (2009/10), 2000–2034.
- [7] D. Conlon, J. Fox, and Y. Zhao, Extremal results in sparse pseudorandom graphs, Adv. Math. 256 (2014), 206–290.
- [8] , Linear forms from the Gowers uniformity norm, unpublished companion note.

![image 36](<2013-conlon-relative-szemer-theorem_images/imageFile36.png>)

- [9] , The sparse regularity method, in preparation.

![image 37](<2013-conlon-relative-szemer-theorem_images/imageFile37.png>)

- [10] D. Conlon and W. T. Gowers, Combinatorial theorems in sparse random sets, arXiv:1011.4310.


![image 38](<2013-conlon-relative-szemer-theorem_images/imageFile38.png>)

- 7This should at least be true for theorems regarding graphs and hypergraphs, though we feel that a similar approach should also be possible for subsets of the integers.


- [11] D. Conlon, W. T. Gowers, W. Samotij, and M. Schacht, On the K LR conjecture in random graphs, Israel J. Math., to appear.
- [12] B. Cook and A. Magyar, Constellations in Pd, Int. Math. Res. Not. 2012 (2012), 2794–2816.
- [13] B. Cook, A. Magyar, and T. Titichetrakun, A multidimensional Szemer´edi theorem in the primes, arXiv:1306.3025.
- [14] J. Fox and Y. Zhao, A short proof of the multidimensional Szemer´edi theorem in the primes, Amer. J. Math., to appear.
- [15] P. Frankl and V. Ro¨dl, Extremal problems on set systems, Random Structures Algorithms 20 (2002), 131–164.
- [16] A. Frieze and R. Kannan, Quick approximation to matrices and applications, Combinatorica 19 (1999), 175–220.
- [17] H. Furstenberg and Y. Katznelson, An ergodic Szemer´edi theorem for commuting transformations, J. Analyse Math. 34 (1978), 275–291.
- [18] D. A. Goldston and C. Y. Yıldırım, Higher correlations of divisor sums related to primes. I. Triple correlations, Integers 3 (2003), A5, 66.
- [19] W. T. Gowers, A new proof of Szemer´edi’s theorem, Geom. Funct. Anal. 11 (2001), 465–588.
- [20] , Hypergraph regularity and the multidimensional Szemer´edi theorem, Ann. of Math. 166 (2007), 897–946.

![image 39](<2013-conlon-relative-szemer-theorem_images/imageFile39.png>)

- [21] , Decompositions, approximate structure, transference, and the Hahn-Banach theorem, Bull. Lond. Math. Soc. 42 (2010), 573–606, arXiv:0811.3103.

![image 40](<2013-conlon-relative-szemer-theorem_images/imageFile40.png>)

- [22] B. Green, Personal communication.
- [23] , A Szemer´edi-type regularity lemma in abelian groups, with applications, Geom. Funct. Anal. 15 (2005), 340–376.

![image 41](<2013-conlon-relative-szemer-theorem_images/imageFile41.png>)

- [24] B. Green and T. Tao, The primes contain arbitrarily long arithmetic progressions, Ann. of Math. 167 (2008), 481–547.
- [25] , Linear equations in primes, Ann. of Math. 171 (2010), 1753–1850.

![image 42](<2013-conlon-relative-szemer-theorem_images/imageFile42.png>)

- [26] Y. Kohayakawa, Szemer´edi’s regularity lemma for sparse graphs, Foundations of computational mathematics (Rio de Janeiro, 1997), Springer, Berlin, 1997, pp. 216–230.
- [27] D. Kr´l’, O. Serra, and L. Vena, A combinatorial proof of the removal lemma for groups, J. Combin. Theory Ser. A 116 (2009), 971–978.
- [28] , A removal lemma for systems of linear equations over ﬁnite ﬁelds, Israel J. Math. 187 (2012), 193–207.

![image 43](<2013-conlon-relative-szemer-theorem_images/imageFile43.png>)

- [29] T. H. Leˆ, Green-Tao theorem in function ﬁelds, Acta Arith. 147 (2011), 129–152.
- [30] L. Lova´sz and B. Szegedy, Limits of dense graph sequences, J. Combin. Theory Ser. B 96 (2006), 933–957.
- [31] , Szemer´edi’s lemma for the analyst, Geom. Funct. Anal. 17 (2007), 252–270.

![image 44](<2013-conlon-relative-szemer-theorem_images/imageFile44.png>)

- [32] L. Matthiesen, Correlations of the divisor function, Proc. Lond. Math. Soc. 104 (2012), 827–858.
- [33] , Linear correlations amongst numbers represented by positive deﬁnite binary quadratic forms, Acta Arith. 154 (2012), 235–306.

![image 45](<2013-conlon-relative-szemer-theorem_images/imageFile45.png>)

- [34] B. Nagle, V. Ro¨dl, and M. Schacht, The counting lemma for regular k-uniform hypergraphs, Random Structures Algorithms 28 (2006), 113–179.
- [35] O. Reingold, L. Trevisan, M. Tulsiani, and S. Vadhan, Dense subsets of pseudorandom sets, 49th Annual IEEE Symposium on Foundations of Computer Science, IEEE Computer Society, 2008, pp. 76–85.
- [36] V. Ro¨dl and J. Skokan, Regularity lemma for k-uniform hypergraphs, Random Structures Algorithms 25 (2004), 1–42.
- [37] , Applications of the regularity lemma for uniform hypergraphs, Random Structures Algorithms 28 (2006), 180–194.

![image 46](<2013-conlon-relative-szemer-theorem_images/imageFile46.png>)

- [38] I. Z. Ruzsa and E. Szemere´di, Triple systems with no six points carrying three triangles, Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II, Colloq. Math. Soc. J´anos Bolyai, vol. 18, North-Holland, Amsterdam, 1978, pp. 939–945.
- [39] D. Saxton and A. Thomason, Hypergraph containers, arXiv:1204.6595.
- [40] M. Schacht, Extremal results for random discrete structures, submitted.
- [41] A. Scott, Szemer´edi’s regularity lemma for matrices and sparse graphs, Combin. Probab. Comput. 20 (2011), 455–466.
- [42] A. Shapira, A proof of Green’s conjecture regarding the removal properties of sets of linear equations, J. Lond. Math. Soc. 81 (2010), 355–373.
- [43] J. Solymosi, Note on a generalization of Roth’s theorem, Discrete and computational geometry, Algorithms Combin., vol. 25, Springer, Berlin, 2003, pp. 825–827.
- [44] , A note on a question of Erd˝os and Graham, Combin. Probab. Comput. 13 (2004), 263–267.

![image 47](<2013-conlon-relative-szemer-theorem_images/imageFile47.png>)

- [45] E. Szemere´di, On sets of integers containing no k elements in arithmetic progression, Acta Arith. 27 (1975), 199–245.
- [46] T. Tao, A remark on Goldston-Yıldırım correlation estimates, unpublished.
- [47] , The Gaussian primes contain arbitrarily shaped constellations, J. Anal. Math. 99 (2006), 109–176.

![image 48](<2013-conlon-relative-szemer-theorem_images/imageFile48.png>)

- [48] , A variant of the hypergraph removal lemma, J. Combin. Theory Ser. A 113 (2006), 1257–1280.


![image 49](<2013-conlon-relative-szemer-theorem_images/imageFile49.png>)

- [49] T. Tao and T. Ziegler, The primes contain arbitrarily long polynomial progressions, Acta Math. 201 (2008), 213–305.
- [50] , A multi-dimensional Szemer´edi theorem for the primes via a correspondence principle, Israel J. Math., to appear.

![image 50](<2013-conlon-relative-szemer-theorem_images/imageFile50.png>)

- [51] H. Towsner, An analytic approach to sparse hypergraphs: hypergraph removal, arXiv:1204.1884.
- [52] L. Trevisan, M. Tulsiani, and S. Vadhan, Regularity, boosting, and eﬃciently simulating every high-entropy distribution, 24th Annual IEEE Conference on Computational Complexity, IEEE Computer Society, 2009, pp. 126–136.
- [53] Y. Zhao, An arithmetic transference proof of a relative Szemer´edi theorem, Math. Proc. Cambridge Philos. Soc. 156 (2014), 255–261.


Mathematical Institute, Oxford OX1 3LB, United Kingdom E-mail address: david.conlon@maths.ox.ac.uk

Department of Mathematics, MIT, Cambridge, MA 02139-4307 E-mail address: fox@math.mit.edu

Department of Mathematics, MIT, Cambridge, MA 02139-4307 E-mail address: yufeiz@math.mit.edu

