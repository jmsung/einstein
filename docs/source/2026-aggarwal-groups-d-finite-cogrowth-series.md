---
type: source
kind: paper
title: On groups with D-finite cogrowth series
authors: Mudit Aggarwal, Murray Elder, Andrew Rechnitzer
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2605.12793v1
source_local: ../raw/2026-aggarwal-groups-d-finite-cogrowth-series.pdf
topic: general-knowledge
cites:
---

# arXiv:2605.12793v1[math.CO]12May2026

## On groups with D-finite cogrowth series

Mudit Aggarwal, Murray Elder, and Andrew Rechnitzer

May 14, 2026

Abstract

The cogrowth series of a group with respect to a finite generating set is an important combinatorial quantity that seems very difficult to compute exactly, as evidenced by the scarcity of known examples. In this paper, we give a particular infinite family of presentations for which the cogrowth series can be determined as the constant term of an algebraic function, which shows that it is D-finite and, with more work, not algebraic.

Our proof exploits the fact that for a particular choice of subgroup, the corresponding Schreier graph has finite tree width, and by considering paths in the cosets and the Schreier graph separately, we are able to construct a system of generating functions which count paths. We find the asymptotics of this system to conclude that the groups have D-finite but non-algebraic cogrowth series.

We also apply our method to some additional examples which have some similarities with the infinite family above, and again show they have D-finite but non-algebraic cogrowth series.

These examples lend some support to the conjecture that if a group has an algebraic cogrowth series, then it must be virtually-free, and adds to the small collection of known examples of groups having D-finite cogrowth series for at least one finite generating set.

### Contents

###### 1 Introduction 2

- 1.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
- 1.2 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


###### 2 Groups with presentation ⟨a1,...,ak | a21 = a22 = ··· = a2k⟩ 6

- 2.1 Walks in the k-regular tree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
- 2.2 Back to cogrowth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


###### 3 Groups with presentation ⟨a1,...,ak | ap11 = ap22 = ··· = apkk⟩ 12

- 3.1 Winding number . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 3.2 Generating functions for walks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 3.3 The system of equations for G(p1,...,pk) . . . . . . . . . . . . . . . . . . . . . . . . 17


###### 4 Part 1: Asymptotics of L0 18

- 4.1 General results on asymptotics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
- 4.2 Partial asymptotics for G(p1,...,pk) . . . . . . . . . . . . . . . . . . . . . . . . . . . 22


###### 5 Decompositions, patterns, and variance 23

- 5.1 Decomposing the walk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
- 5.2 Pattern theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
- 5.3 Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27


###### 6 Transformations and proof of Theorem 4.6 28

- 6.1 Even case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
- 6.2 Odd case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
- 6.3 Mixed case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32


###### 7 Part 2: Asymptotics of Fk 33

- 7.1 Popularity argument . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
- 7.2 Geometric group theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
- 7.3 Expected number of returns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
- 7.4 Return to the singularity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39


###### 8 Applying the techniques to other presentations 41

- 8.1 The standard presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
- 8.2 Second presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
- 8.3 Third presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


Acknowledgements 43 References 43

- A Explicit asymptotics for some examples 46

- A.1 B3 with trefoil knot presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
- A.2 B3 with standard presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49


- B B3 with presentation ⟨a,x | axa = x2⟩ 50


- B.1 Counting returns on the Schreier graph (no q’s) . . . . . . . . . . . . . . . . . . . . . 51
- B.2 Return to the Schreier graph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56


### 1 Introduction

Let Γ be a group with finite generating set S, and let S−1 be a distinct alphabet in bijection with S, where the bijection is given by the map s  → s−1 ∈ Γ. Let W be the set of words in (S ∪ S−1)∗ that evaluate to the identity in Γ. The cogrowth function ψ: N −→ N is defined as ψ(n) = ψn = |{w ∈ W | |w| = n}|. The formal power series

∞

z|w| (1.1)

ψnzn =

ΨΓ,S(z) =

n=0

w∈W

is called the cogrowth series of Γ with the set S. It is well known [9, 22] that the cogrowth, the exponential growth rate of ΨΓ,S(z), satisfies

ψn1/n = 2|S| (1.2)

limsup

n−→∞

if and only if Γ is amenable.

In this work, we do not consider only freely reduced words; rather, we define the cogrowth series in terms of words that are equivalent to the identity, whether they are freely reduced or not. This is done to simplify much of the combinatorial analysis that follows. There are simple substitutions to move between the cogrowth series defined on all words and on freely reduced words [27].

The following well-known theorem by Kouksov [27] classifies group presentations that have rational cogrowth series.

- Theorem 1.1 (Kouksov [27]). The cogrowth series for a group with presentation ⟨S | R⟩, |S| finite, is rational if and only if the group is finite.


An analogous result for algebraic cogrowth series is open, although a longstanding conjecture exists in the literature.

Conjecture 1.2 (Folklore, mentioned in [5, page 1], [6, page 1]). The cogrowth series for a group with presentation ⟨S | R⟩, |S| finite, is algebraic if and only if the group is virtually-free.

A group is said to be virtually-free if it has a finite-index subgroup that is free. More generally, a group is virtually-P (for some property P) if it has a finite-index subgroup that has property P.

This conjecture has been around in different guises for some time (see, for example, [19]), usually phrased in terms of Green’s functions. Recall that the Green’s function is the probability generating function G(x,y;z) = n≥0 P(n)(x,y)zn, where P(n)(x,y) is the probability that a simple random walk starting at x ends at y after n steps in the Cayley graph of the associated group (see [40]). Hence, G(e,e;z) can be obtained from the cogrowth series via the substitution z  → z/(2|S|).

The backwards direction of Conjecture 1.2 follows from the combination of two notable theorems: Muller and Schupp (relying on a result of Dunwoody) show that a finitely generated group is virtually-free if and only if the set W is a context-free language [14, 32], and in particular the context-free grammar describing the word problem is unambiguous; and Chomsky and Schu¨tzenberger’s result that unambiguous context-free languages have algebraic generating functions [8].

A standard superset of algebraic generating functions are D-finite generating functions. A generating function is said to be D-finite (or holonomic) if it satisfies a linear differential equation (of finite order) with polynomial coefficients (see [37] for a proof of the inclusion). A sequence is said to be P-recursive if it satisfies a linear recurrence relation with polynomial coefficients. A standard result (see [38]) states that an integer sequence ψn is P-recursive if and only if its generating function

∞ n=0 ψnzn is D-finite.

The cogrowth series for Baumslag-Solitar groups, BS(M,N) = ⟨a,t | taMt−1 = aN⟩, was studied in [15]. It was shown that when M = N, the cogrowth series is D-finite (and not algebraic for N ≤ 10) with respect to the generating set {a±1,t±1}. It was also conjectured that for M ̸= N the series should be non-D-finite.

Garrabrant and Pak [18] proved that any amenable linear group of exponential growth has nonD-finite cogrowth series with respect to any generating set. This includes for example the solvable Baumslag-Solitar groups BS(1,N) = ⟨a,x | xax−1 = aN⟩. They also show that F11 × F3 (where

Fk denotes the free group of rank k) has D-finite cogrowth series for one finite generating set but not for another.

Later, Bell and Mishna [3] extended this to any amenable group of super-polynomial (intermediate and exponential) growth by finding necessary conditions on the generating function to be D-finite. They also claimed that any virtually abelian group will have D-finite cogrowth series for any finite generating set, which was proved by Bishop [5] who showed more generally that if a group contains Zd ×Fk as a finite index subgroup (where Zd is the free abelian group of rank d), then its cogrowth series is the diagonal of a rational function for all presentations, answering a question in [18] and extending some results from [15].

However, the exact cogrowth series is not known for many group presentations. Kuksov [28] computed the cogrowth series for certain free products of free and finite groups using combinatorial and series arguments. Bell, Liu and Mishna [2] construct a grammar via which they can compute the cogrowth series for free products of finite groups. Darbinyan, Grigorchuk and Shaikh [10] compute the cogrowth series of finitely generated subgroups of free groups via ergodic automata. Some more work in a similar vein includes generalisations of the cogrowth series [21, 24], and computational work to estimate the cogrowth of Thompson’s group [16, 34].

Additionally, not a lot is known about the groups that are not virtually-free. In the few known results, it is seen that the cogrowth series are either non-D-finite, as in [18], or D-finite but not algebraic, as in [15]. Pak and Sokup [33] show that even for virtually-nilpotent groups, the problem of writing the cogrowth series as a diagonal of a rational function is not computable. More recently, Bodart [6] gave an explicit virtually-nilpotent group presentation with a generating multiset where the cogrowth series is not D-finite.

The goal of the present article is to expand the list of group presentations for which the cogrowth series can be computed exactly, and in particular those whose cogrowth series is D-finite and not algebraic. Specifically, in this article, we first study the cogrowth series in the following family of presentations

⟨a1,...,ak | ap11 = ··· = apkk⟩, (1.3) where k ≥ 2,pi ≥ 2 are positive integers. In Section 8 and the Appendix, we apply our techniques with mild generalisations to the following presentations of the 3-strand braid group B3:

⟨a,b | aba = bab⟩ ⟨a,x | axa = x2⟩ (1.4)

(see Section 8 to see how these present the same group). In each case, we prove the cogrowth series is again D-finite and non-algebraic. Another presentation of B3, ⟨x,c | x3 = c2⟩, is covered by our main results, and we also give explicit asymptotics of the cogrowth series in the Appendix.

###### 1.1 Notation

We use the standard notations for groups and presentations as in [31]. We write u ≡ v, where u,v are words in (S ∪ S−1)∗, to mean that the products u and v are equal in the group Γ, and u = g if the product u is equal to the group element g ∈ Γ. The length of the word u is denoted |u|.

The (right-)Schreier graph of a group Γ with respect to a finite generating set S and subgroup H is the graph whose vertices are the right-cosets of H, {Hg | g ∈ Γ}, with directed edges (Hg,Hgs) labeled s for each coset Hg and each s ∈ S ∪ S−1. In the case the H is a normal subgroup, the Schreier graph of Γ identical to the Cayley graph of the quotient group H\Γ.

Much of the paper focuses on the following family of groups.

- Definition 1.3. Let p1,...,pk be integers at least 2 and k ≥ 2. Let G(p1,...,pk) be the group


presented by ⟨a1,...,ak | ap11 = ap22 = ··· = apkk⟩. For simplicity of notation, we will often write Gk in place of G(p1,...pk) when the values pi are understood.

###### 1.2 Overview

The main work of this paper is concerned with showing that the group Gk with respect to the generating set in Definition 1.3 has a D-finite but non-algebraic cogrowth series. We will also show

that the cogrowth is an algebraic number. We will often work with fixed p1,...,pk and simply denote the group by Gk.

Our method is roughly as follows. We find a central element ∆ (that is, commutes with every element of the group), together with a normal form ∆mw. When multiplication by generators on the right does not change the normal form too dramatically, we come up with a finite system of two-variable generating functions counting various sets of words. We start with the set of words W which evaluate to an element in ⟨∆⟩, so have normal form ∆m for some integer m. We let

z|w|qm =

fn,mznqm (1.5)

Fk(z;q) =

m∈Z w∈W

m∈Z n∈N

be the generating function for the function fn,k counting words in W of length n and having normal form ∆m.

By defining several related series, we are able to prove that Fk(z;q) is algebraic. We can then obtain the cogrowth series by computing the diagonal [q0]Fk(z;q), which is then D-finite since the diagonal of a D-finite series is again D-finite [29].

We then show that the series is not algebraic by showing that it has asymptotic form fn,0 ∼ Cµnn−j where j is a positive integer. The key here is to essentially decompose our generating function into a product of two “easier” ones.

- • The first one counts paths in a tree or tree-like graph and usually has an µnn−3/2 term in its asymptotic formula, typical of algebraic generating functions. This will be our Schreier graph with finite tree-width.
- • The second one is essentially a one-dimensional random walk on Z, which counts the exponent ∆m. This gives us Gaussian behaviour, with its asymptotics of the form n−1/2 exp(−Cm2/n).


So, together, we get n−2 (or n−1 in edge cases); this proves the series cannot be algebraic. This is in contrast with [15], where non-algebraicity could only be proved for a finite number of cases.

In Section 2, we compute the asymptotics explicitly for the special case with the presentation ⟨a1,...,ak | a21 = a22 = ··· = a2k⟩ by first counting walks on a k-regular tree, and then keeping track of the exponent ∆m. This yields Theorem 2.8.

For the general case, with presentation ⟨a1,...,ak | ap11 = ap22 = ··· = apkk⟩, we need more work. Section 3 begins by discussing the notion of “winding number”, which we use to keep track of ∆m.

We then discuss how to build a system of generating functions for walks on this group.

Unfortunately, computing the asymptotics in the general case explicitly is not feasible (though we do have numerical results for special cases in Appendix A). Hence, we rely on general theorems in the literature [1, 12, 13]. We get the required asymptotics in two main parts.

• In part 1 (Section 4), we get an asymptotic expansion for certain parts of our system. We do this by using the standard results, which we also state. This yields Theorem 4.6, and we will use it later.

In order to prove Theorem 4.6, we need to deal with two technical issues. Firstly, we need to find bounds on the variance of the winding number in a random walk. We do that in Section 5. In particular, we find a decomposition of the walk (for an upper bound) in Section 5.1, and prove a pattern theorem in Section 5.2. Secondly, we need to deal with contributions from multiple singularities and saddle points depending on the parity of our system. We do that via generating function transformations in Section 6.

• In part 2 (Section 7), we prove an asymptotic expansion for the entire system using tools from geometric group theory and probability on groups. In particular, we show that a closed random walk on our Schreier graph spends very little time at the root, which implies that the asymptotics of the entire system are similar to the asymptotics of the partial system proved earlier.

We then exploit the fact that our Schreier graph has finite tree-width to apply the results of Gou¨ezel [20] to determine the asymptotics.

### 2 Groups with presentation ⟨a1,...,ak | a21 = a22 = ··· = a2k⟩

In this section, we consider the special case of Definition 1.3 where p1 = ··· = pk = 2 with k ≥ 2, which will introduce many of the ideas needed for the general case. Thus we have

G(2,...,2) = Gk = ⟨a1,...,ak | a21 = a22 = ··· = a2k⟩. (2.1)

Let ∆ = a21 ≡ a22 ≡ ··· ≡ a2k.

- Lemma 2.1. Each element of Gk can be written in normal form w = ∆mv (2.2)


where m ∈ Z and the suffix v ∈ {a1,...,ak}∗ that does not contain a2i.

Proof. Let u be a word in the generators and inverses. Replace a−i 1 by ∆−1ai and a2i by ∆ everywhere in u starting from left to right. Since ∆ is central, commute all powers of ∆ to the left.

If this produces more positive powers, repeat.

| |
|---|


From this, we can construct the Schreier graph of Gk with respect to the generating set {a1,...,ak} and subgroup ⟨∆⟩, which is a k-valent tree. Figure 1 shows an example for k = 3. The vertices of

this graph are in bijection with the suffixes in the above lemma, and so we simply label them by the suffix. So, two vertices labeled by suffixes v1,v2 are connected by an edge labeled s ∈ S ∪ S−1 when v2 = v1s.

We note that at times it will be convenient to think of there being two directed edges between these vertices, one labelled by s and the other by its inverse.

bcb

bca

bc

acb

- bab

- cab

bac

- cac




- b
- c


ac

aca

ba

e a

ca

ab

aba

abc

cb

cba

cbc

Figure 1: The Schreier graph of G3 = ⟨a,b,c | a2 = b2 = c2⟩; vertex v corresponds to the coset ⟨∆⟩v with the edges drawn by two arcs. To avoid overuse of subscripts, we have chosen generators a,b,c rather than a1,a2,a3.

###### 2.1 Walks in the k-regular tree

The problem of counting words in Gk which are equivalent to the identity will be closely related to the problem of counting walks in the k-tree that start and end at the origin. Before we proceed with the cogrowth series, let’s recall one way in which to count such walks.

- Definition 2.2. Let Fk(z) be the generating function that counts all walks that start and end at the root vertex of the k-valent tree. Similarly, define Ai(z) to be the generating function that counts all walks that start and end at the vertex ai, without ever visiting the root (one can look at the tree depicted in Figure 1).


We remark that the generating functions Ai(z) defined here are slightly different from the ones in the general case defined in Section 3. In the special case we are in, these ones are easier to work with explicitly; however, the general argument will also give us the same final Fk.

We establish a system of algebraic equations satisfied by these generating functions via a decomposition of the walks that they count. The key idea is to decompose a walk counted by (say) Fk(z) by cutting it when it last leaves the root vertex. This shows that any such walk is either trivial or is comprised of two shorter walks, one counted by Fk and the other by one of the Ais. This sort of factorisation is quite standard.

- Lemma 2.3. The above generating functions satisfy the following system of equations:


A1(z) = A2(z) = ··· = Ak(z), (2.3a) A1(z) = 1 + (k − 1)z2A1(z)2, (2.3b) Fk(z) = 1 + kz2Fk(z)A1(z) (2.3c)

and hence

2(k − 1) k − 2 + k 1 − 4(k − 1)z2

Fk(z) =

. (2.4)

Proof. The equality of the Ais follows from symmetry. Now, consider a walk counted by Fk. Such a walk

- • has length 0, or
- • can be decomposed by cutting it at the last time it leaves the root vertex.


In this second case, the walk decomposes into another walk counted by Fk(z), a step away from the root, a walk counted by one of the Ais, and finally a step back to the root vertex. Translating this into operations on the corresponding generating functions, we have.

Fk(z) = 1 + Fk(z) · z ·

i

Ai(k) · z. (2.5)

Now take a walk counted by A1 and decompose it in a similar way. It either

- • has length 0, or
- • can be decomposed by cutting it at the last time it leaves the vertex a1.


In the second case, the walk decomposes into a walk counted by A1(z), a step away from a1 to the vertex corresponding to a1ai for i ̸= 1, a walk counted by Ai(z) for i ̸= 1 (respectively), and a final step back to a1. Hence we obtain

A1(z) = 1 + A1(z) · z ·

which gives us the required system of equations. The equation for A1(z) has two possible solutions

Ai(z) · z, (2.6)

i̸=1

1 ± 1 − 4(k − 1)z2 2(k − 1)z2

A1(z) =

. (2.7)

The positive branch is O(z−2) and so is not a valid generating function, while the negative branch is valid and its first few terms are 1 + (k − 1)z2 + O(z4). Substituting the negative branch into the equation for Fk(z) gives the result.

| |
|---|


We demonstrate that one can actually write out the coefficients of this generating function quite explicitly.

- Lemma 2.4. For the above system, the generating function Fk(z) is


z2n

Fk(z) = 1 + k

n≥1

n−1

n − m n

m=0

2n m

(k − 1)m. (2.8)

Proof. To obtain the explicit expansion of Fk(z), start by rewriting Fk(z) =

1 1 − kz2A1(z)

kjz2jA1(z)j, (2.9)

=

j≥0

n

n

kj[z2n−2j]A(z)j =

kn−ℓ[z2ℓ]A(z)n−ℓ (2.10)

[z2n]Fk(z) =

j=0

ℓ=0

where we have used the fact that A(z) contains only even powers of z. Notice that A(z) is very nearly the Catalan generating function and its expansion is well understood:

2n + ℓ − 1 n

ℓ n + ℓ

[z2n]A(z)ℓ =

(k − 1)n. (2.11) Hence, some standard manipulations give

n

[z2n]Fk(z) =

ℓ=0

k n

=

n − ℓ n

kn−ℓ ·

n + ℓ − 1 ℓ

n−1

(k − 1)m(n − m)

m=0

2n m

(k − 1)ℓ (2.12)

. (2.13)

Along the way, one uses the equality

2n m

which is fairly standard.

m

=

ℓ=0

n + ℓ − 1 ℓ

n − ℓ m − ℓ

, (2.14)

| |
|---|


###### 2.2 Back to cogrowth

In order to compute the cogrowth series, we will use a very similar decomposition. Indeed, the main difference is that as we move around the Schreier graph, we must also keep track of powers of ∆. Let us start by forming a generating function analogous to Fk above.

- Definition 2.5. For m ∈ Z let Wm be the set of words in {ai,a−i 1}i≤k that are equivalent to group


elements whose normal form is exactly ∆m, and then let W = m Wm. Hence, a word is in W if and only if it corresponds to a group element lying in the subgroup generated by ∆. Then define

z|w|qm (2.15)

Fk(z;q) =

m w∈Wm

where |w| denotes the length of w. This counts all words equivalent to elements in the coset ⟨∆⟩ according to their length and also the exponent of ∆. The cogrowth series is then the constant term of F(z,q) with respect to q.

Hence, we note that [znqm]Fk = # of words of length n equivalent to ∆m.

To obtain this generating function, we first need to define some auxiliary functions (analogous to the Ais above).

- Definition 2.6. Let Wi,m be the subset of Wm so that if w = uv then u ̸≡ ∆jai for any j. Further,


let Wi = m Wi,m. These words describe walks in the Schreier graph that start at the origin and never visit ⟨∆⟩ai. Let their generating function be

z|w|qm. (2.16)

Ai(z;q) =

m w∈Wi,m

We find a set of equations satisfied by these generating functions using a similar decomposition.

- Lemma 2.7. The generating functions Ai(z;q) and Fk(z;q) satisfy the following set of equations: A1(z;q) = A2(z;q) = ··· = Ak(z;q), (2.17a) A1(z;q) = 1 + (k − 1)z2(q + 2 + q−1)A1(z;q), (2.17b) Fk(z;q) = 1 + kz2(q + 2 + q−1)Fk(z;q) · A1(z;q). (2.17c)


Proof. The first equation follows from symmetry. For the remaining ones, we proceed as we did above. We decompose any walk counted by Fk by cutting it when it last leaves the coset ⟨∆k⟩. Any walk counted by Fk

- • has length 0, or
- • can be decomposed by cutting it at the last time it leaves the coset ⟨∆⟩.


In this second case, the walk, w, decomposes into a shorter walk counted by Fk, a step away from ⟨∆⟩ to one of the cosets ⟨∆⟩ai, then another walk, wˆ, and finally a step back to ⟨∆⟩.

Say our walk has stepped to ⟨∆⟩aj, then the intermediate walk wˆ must start and end at ⟨∆⟩aj, while never visiting ⟨∆⟩. These are precisely the walks counted by Aj(z;q).

Now, in order to step from ⟨∆⟩ to ⟨∆⟩aj, we must either append an aj or a−j 1.

- • Appending aj does not change the power of ∆.
- • Appending a−j 1 decreases the power of ∆ since ∆ma−j 1 = ∆m−1aj. Similarly, when we step back, we must also append an aj or a−j 1.
- • Appending aj increases the power of ∆, since ∆ma2j = ∆m+1.
- • Appending a−j 1 does not change the power of ∆ since ∆maja−j 1 = ∆m.


This gives us

F(z;q) = 1 + F(z;q) · z(1 + q−1) ·

j

Aj(z;q) · z(1 + q). (2.18)

A very similar argument for decomposing A1 gives us A1(z;q) = 1 + A1(z;q) · z(1 + q−1) ·

Aj(z;q) · z(1 + q). (2.19)

j̸=1

These equations can now be simplified to get the result. Solving this system of equations then gives us

| |
|---|


- Theorem 2.8 (Cogrowth series for G(2,2,...,2) = Gk with k ≥ 2). The generating function Fk(z;q) for k ≥ 2 is given by


2(k − 1) k − 2 + k 1 − 4(k − 1)(q + 2 + q−1)z2

Fk(z;q) =

. (2.20)

Hence, the cogrowth series of the group Gk is given by

2

2n n

z2n

[q0]F2(z;q) = 1 +

, (2.21)

n≥1

n−1

n − m n

2n n

2n m

[q0]Fk(z;q) = 1 + k

z2n

(k − 1)m. (k ≥ 3) (2.22)

n≥1

m=0

Hence,

1

πn · 42n 1 + O(n−1) , (2.23) [z2nq0]Fk(z;q) =

[z2nq0]F2(z;q) =

42n(k − 1)n πn2

k(k − 1) (k − 2)2 ·

1 + O(n−1) . (k ≥ 3) (2.24)

Consequently, the cogrowth is 4√k − 1, and the cogrowth series is D-finite but not algebraic for any integer k ≥ 2.

Proof. Solving the system in Lemma 2.7 gives the required expression. We obtain the explicit expression for the coefficients by noting that Fk(z;q) can be obtained from the generating function for walks on k-regular trees by substituting z2  → z2(q + 2 + q−1). More precisely, let Tk(z) be the generating function for walks on k-regular trees, which we called Fk(z) in Equation (2.4). Then

Fk(z;q) = Tk(z q + 2 + q−1), (2.25) [z2nq0]Fk(z;q) = [z2n]Tk(z) · [q0](q + 2 + q−1)n, (2.26)

n−1

n − m n

2n m

[z2nq0]Fk(z;q) = [q0](q + 2 + q−1)n · k

(k − 1)m, (2.27)

m=0

and [q0](q + 2 + q−1)n = 2nn .

We first consider k ≥ 3 and then turn to k = 2, which simplifies considerably. So for k ≥ 3, to obtain the asymptotics of the cogrowth series, we use standard tools from analytic combinatorics [17] to construct an uniform expansion of Tk(z):

4n(k − 1)n √

k(k − 1) (k − 2)2 ·

[z2n]Tk(z) =

πn3

1 + O(n−1) (2.28)

and similarly find a uniform expansion of 2nn :

2n n

4n √nπ

=

1 + O(n−1) . (2.29)

The product of these expansions gives the asymptotics of the cogrowth series.

Finally, the function Fk(z;q) is algebraic and hence D-finite (see [36], for example). D-finite series are closed under extraction of constant terms [29], and hence the cogrowth series is D-finite. Finally, we know that the cogrowth series is not algebraic because of the dominant asymptotics. The n−2 correction to the dominant exponential term is incompatible with an algebraic generating function ([17, Section VII.7] and [25]).

For k = 2, note that the generating function simplifies to

1 1 − 4z2(q + 2 + q−1)

F2(z;q) =

(2.30)

which can be explicitly expanded to get the required form of [q0]F2(z;q). The uniform expansion of 2nn then gives us the result.

| |
|---|


This gives an infinite family of groups for which we can determine the cogrowth series explicitly and, further, demonstrate that the series is not an algebraic function.

### 3 Groups with presentation ⟨a1,...,ak | ap

#### 1 = ap

#### 2 = ··· = ap

#### k ⟩

1

2

k

Let Gk = G(p1,...,pk) where k,pi ≥ 2, and define ∆ = ap11 ≡ ap22 ≡ ap33 ≡ ···. From here onwards, we assume at least one of the pis is at least 3 unless stated otherwise. Hence, max{p1,...,pk} ≥ 3. We do this since the case with all pi = 2 has been handled in Section 2.

- Lemma 3.1. The element ∆ is central. Consequently, ⟨∆⟩ is a normal subgroup of Gk.


Proof. Since ap11 ≡ apii for all i, it is enough to show that ap11 commutes with every element of Gk. Consider a generator aj of Gk. Then,

aj · ap11 = aj · apjj = ajpj+1 = apjj · aj = ap11 · aj. (3.1) Apply this to any word in the generators and their inverses to get the result.

| |
|---|


Corollary 3.2. Every element w ∈ Gk can be written in the normal form

w = ∆mv (m ∈ Z) (3.2)

where the suffix v ∈ Gk is a word in strictly positive powers of the generators {a1,...,ak} such that it doesn’t contain any subword from {ap11,...,apkk}.

ba2 ba

a2b3 a2b2

b a2 b2

b2a

a2b

e

b2a2

ab3

a

b3

ab ab2

b3a b3a2

- Figure 2: The Schreier graph of G2 = ⟨a,b | a3 = b4⟩; vertex p corresponds to the coset ⟨∆⟩p.


Consider the Schreier graph of Gk with respect to the generating set {a1,...,ak and subgroup ⟨∆⟩. As before, since cosets are in bijection with suffixes as in the previous corollary, we may assume vertices are labelled by suffixes.

An example of G2 = ⟨a,b | a3 = b4⟩ is shown in Figure 2. Note again that we use a,b for generators instead of a1,a2 to avoid overuse of subscripts.

- Definition 3.3. For m ∈ Z, define Wm to be the set of words in {a1,...,ak,a−1 1,...a−k 1} such that their normal form is exactly ∆m. Then define the generating function Fk is:


z|w|qm. (3.3)

Fk(z;q) =

m w∈Wm

Hence, the coefficient [znqm]Fk(z;q) is the number of words in Gk with length n and normal form ∆m. Hence, the cogrowth series is given by [q0]Fk.

We now describe a system of equations for Fk(z;q) based on walks on the Schreier graph.

###### 3.1 Winding number

To keep track of the power of q in our generating functions, we define a notion of a winding number for a closed walk on our graphs. The winding number will track the power of ∆ in the normal forms of group elements visited by the walk as it moves around the group.

First consider the case in which pi ≥ 3, such as in the square and triangle adjacent to e depicted in

- Figure 2. We will consider the pi = 2 case shortly. A walk starting at e and moving anticlockwise around the triangle constructs words with normal forms e  → a  → a2  → ∆1. Similarly, a walk moving clockwise around the triangle constructs e  → a−1  → a−2  → ∆−1. We can use q) to keep track of that change in the exponent of ∆ by accumulating a weight of q when we step from a2 to e and q−1 when we make the reverse step. We do similarly when between b3 and e.


More generally, we will consider the graph to be embedded into the plane so that each facet is oriented in this way; positive powers of ai will move anticlockwise around the face, while negative powers move clockwise.

Note that whenever a walk enters a facet moving away from the root, we must exit from the same vertex going back to the root since our graph is a “tree of polygons”. This step can either use the same edge we took after entering the vertex, or a different edge. If we use the same edge in both the directions then this gives weight 1 · 1 or q−1 · q and so does not result in a net change in the exponent of q. On the other hand, if the walk enters and leaves by different edges, then it gains 1 · q if it moves anticlockwise about the facet, or q−1 · 1 if it moves clockwise about the facet. See

- Figure 3. By keeping track of these facet traversals, as the winding number, we keep track of the exponent of q and so of ∆ in the normal form.


Now turn the case of pi = 2. Starting at ∆mw, multiplying by ai gives ∆mwai, while multiplying by a−i 1 gives ∆m−1wai. Similarly, starting at ∆mwai multiplying by ai gives ∆m+1w while multiplying by a−i 1 gives ∆mw. Consequently, we draw a bigon to denote these possibilities and pick one of the edges and give it a weight q when traversed towards the root, and q−1 when traversed away from the root. Just as above, we can use this factor of q to denote the change in winding number, and so the power of ∆ in the normal form.

- Definition 3.4. The winding number for a closed walk is the signed number of loops we make across the facets of the graph. We use the convention that any clockwise loop contributes −1, and any anticlockwise loop contributes +1. Note that if a walk enters and leaves a facet by the same edge, then it contributes 0 to the winding number.


In particular, if we go across a facet such that we end up at the same vertex we started with, using a different edge than our starting edge, we add a +1 or −1 to the winding number (depending on the orientation). This doesn’t have to be immediate; we can enter a facet, leave from a different vertex, and come back. This keeps the winding number preserved. Figure 3 shows some examples of winding number contributions.

- Figure 3: (Left to right): Walks starting and ending at the highlighted vertex giving winding number contributions of −1,0,+1 respectively.


We root the Schreier graph at the vertex corresponding to the identity. If we take closed walks on the graph, we see that the winding number of the walk is the same as the exponent of ∆ picked up

for the corresponding word. This is similar to the argument we did earlier for the special case of the k-tree in Section 2. Hence, the Fk(z;q) defined above for words in the group can be written as

Fk(z;q) =

z|w|qm =

m w∈Wm

n m

fn,mznqm, (3.4)

where fn,m is the number of closed walks of length n with winding number m. To be precise, this shows that fn,m is also the number of words of length n in the subgroup with normal form ∆m. This is due to every closed walk being in direct bijection with such a word.

###### 3.2 Generating functions for walks

We now describe how to write a system of equations for Fk. Rather than doing this in full generality, we demonstrate it for G(3,4) = ⟨a1,a2 | a31 = a42⟩ first. The other cases follow similarly.

##### M1

##### M2

M0

q

Fk

##### M3

##### L2

q

L0

L1

- Figure 4: Building our system from two different facets. The dashed line represents where we “cut” our graph to make two one-sided graphs. We have highlighted the edges that accumulate a weight of q when traversed anticlockwise and q−1 when traversed clockwise.


- Definition 3.5. Let Fk(z;q) be the generating function that counts all closed walks that start and end at the root vertex of the graph.

Note that it lies on the intersection of a triangle and a square. Consider the one-sided graph corresponding to the triangle. That is, choose the subgraph in the direction of the triangle: these are vertices that are labelled by suffix words that do not start with b. This is the graph on the right side of the dashed line in Figure 4.

- Definition 3.6. Consider the triangle and square that contain the root vertex in Figure 4; these are separated by a dashed line which splits the graph into two subgraphs joined at the root.


Define L0(z;q) to be the generating function that counts all walks that start and end at the root vertex, without ever visiting a vertex that is labelled by a suffix that starts with b. These are the

walks that do not cross the dashed line indicated in Figure 4 and stay in the subgraph originating from the triangle away from the root.

Moving anticlockwise around the triangle from the origin, label the vertices L0 (being the root), L1 ,and L2. Then define L1(z;q) and L2(z;q) to be the generating functions that counts all walks that start at the root vertex, and end at L1 and L2 (respectively) while staying in the subgraph originating from the triangle away from the root.

Now consider the other subgraph; we can similarly define vertices M0,M1,M2,M3. These in turn allow us to define generating functions Mi(z;q) for walks in the subgraph on the left of the dashed line in Figure 4 ending at Mi. These walks never visit any vertex that is labelled with a suffix starting with a.

- Lemma 3.7. The above generating functions satisfy the system of equations:


L0 = 1 + z[L1 + q · L2], (3.5a) L1 = z[L0 + L2] · M0, (3.5b) L2 = z[q−1 · L0 + L1] · M0. (3.5c)

1 1 − PL

1 1 − PM

L0 =

, M0 =

M0 = 1 + z[M1 + q · M3], (3.6a) M1 = z[M0 + M2] · L0, (3.6b) M2 = z[M1 + M3] · L0, (3.6c) M3 = z[q−1 · M0 + M2] · L0. (3.6d)

1 1 − (PL + PM)

, Fk =

. (3.7)

Proof. Consider a walk counted by L0. Such a walk:

- • has length 0, or
- • had its last step taken from either L1 or L2 to L0.


In the second case, we get a walk from L0 to L1 or L2, followed by a step back to L0. Translating this into generating functions, we get

L0(z;q) = 1 + (L1(z;q) + q · L2(z;q)) · z. (3.8)

The factor of z comes simply from adding an extra step. Any walk ending at L1 has normal form ∆ma, and so stepping to L0 requires us to multiply by a−1. This results in an element with normal form ∆m (hence no change in the power of q). Stepping from L2 to L0 requires us to multiply by a, giving an element equivalent to ∆ma2a ≡ ∆m+1. Hence, the power of q increases by 1.

Now, consider a walk counted by L1(z;q). Such a walk can be decomposed by cutting it at the last time a step was taken to L1 from either L0 or L2. Note that the normal forms of the corresponding words do not change the power of ∆, so there is no factor of q, but the power of z increases by 1 corresponding to the increase in length. This subwalk is counted by (L0(z;q) + L2(z;q)) · z. The remainder of the walk stays in the subgraph at or below the vertex L1. That subwalk is counted by M0(z;q) due to vertex transitivity. This gives the equation for L1(z;q).

We make a similar decomposition for a walk counted by L2(z;q) by cutting it at the last time a step was taken to L2 from either L1 or L0. Notice that when stepping from L0 to L2 the corresponding word changes ∆m  → ∆ma−1 ≡ ∆m−1a2 and so decreases the power of q by 1. Hence we obtain

a subwalk counted by (L1(z;q) + q−1L0(z;q))z. As per above the other subwalk is counted by M0(z;q).

Similar arguments give the equations for Mi(z;q). A little care is required for L2(z;q) and M3(z;q) to take into account the winding number as the walk traverses facets of the graph.

For the remaining equations, we break these walks into primitive subwalks, which is a standard technique in enumeration (see [17, Theorem I.1]). Any walk counted by L0(z;q) (or M0(z;q)) can be decomposed into a sequence of primitive walks, where a primitive walk is a walk starting and ending at L0 (or M0), but not returning to the root anytime except the start and the end. Let the primitives be counted by PL(z;q) (or PM(z;q)). Hence,

1 1 − PL

L0 = 1 + PL + PL2 + ··· =

, (3.9)

1 1 − PM

M0 = 1 + PM + PM2 + ··· =

. (3.10)

We can do the same thing with walks counted by Fk(z;q). Every time the walk returns to the root, the walk has arrived from either an L-vertex or an M-vertex and so is adding a primitive PL or PM. This gives

1 1 − (PL + PM)

Fk = 1 + (PL + PM) + (PL + PM)2 + ··· =

. (3.11)

which gives us the system.

| |
|---|


###### 3.3 The system of equations for G(p1,...,pk)

For the general case, we consider the group presentation ⟨a1,...,ak | ap11 = ··· = apkk⟩. This gives us a Schreier graph consisting of facets which are polygons with pi sides. For each such facet, we get a one-sided graph originating from the root.

- Definition 3.8. Let L(ji) denote the generating function corresponding to the j-th vertex on the i-th facet. It counts the walks (weighted by the winding number) on the one-sided graph of the i-th facet starting at the root and ending at the j-th vertex.


As an example, for the earlier system with L0,L1,L2,M0,M1,M2,M3 we have L(1)0 = L0, L(2)0 = M0, L(1)1 = L1, and so on. With this, we can write our system in the general case:

L(0i) = 1 + z[L(1i) + qL(pi)

- i−1], (3.12) L(ri) = z[L(ri−)1 + L(ri+1) ]
- j̸=i


L(0j) (1 ≤ r ≤ pi − 2), (3.13)

L(0j), (3.14)

L(pi)

i−1 = z[L(pi)

i−2 + q−1L(0i)]

j̸=i

for all 1 ≤ i ≤ k. These govern the walks on one-sided graphs. For walks on the entire graph, we also require the following.

1 1 − Pi

L(0i) =

1 1 − i≤k Pi

(1 ≤ i ≤ k), Fk =

. (3.15)

In Figure 5 we show the centre of the Schreier graph for the case G(3,4,5).

L(3)2 L(3)3

L(1)2 L(2)1 L(2)0

L(1)0

q

L(3)1

q

F3 q

L(3)4

L(2)2 L(2)3

L(1)1

L(3)0

- Figure 5: Building blocks for this Schreier coset graph and system of walks for G(3,4,5). Again, the dashed lines on the left side represent the “cuts” we make to get our one-sided graphs.


We note here that even though we are using low values of pi’s in the above discussion, we see that the system is already fairly unwieldy. In particular, the number of equations in the system

is i≤k pi + k + 1, of which i≤k(pi − 1) have 2(k − 1) quadratic terms each. When we explored these systems at even quite modest values of the pi, we found that computer algebra systems were not able to reduce the set of equations down by eliminating variables or compute a discriminant; the required memory and time appeared to grow extremely quickly with increasing pi’s. We didn’t explore this behaviour in detail.

However, for small values of the parameters, one can use computer algebra systems to compute the exact asymptotics. In particular, Appendix A.1 shows the numeric computations for the torus knot group (k = 2, p1 = 2, p2 = 3).

We note that we could generalise the above to keep track of winding number contributions from different facet types. The resulting system is very similar, and the asymptotics can be computed similarly with a little more bookkeeping. We do not need that level of granularity for the results of this paper.

### 4 Part 1: Asymptotics of L0

We are now ready to proceed to the asymptotics of the solutions of these systems. For technical reasons we break this into two parts. Here, in the first part, we deal with the asymptotics of generating functions of walks on one-sided subgraphs. Since the generating function of all walks depends on that of the walks on the one-sided subgraphs, but not vice versa, we cannot jump straight to the asymptotics of walks on the full graph. Those asymptotics are discussed in the next part, Section 7.

###### 4.1 General results on asymptotics

In this section, we talk about some well-known results about the asymptotics of algebraic functions. We state the relevant results from [1, 12, 13] here without proof. The proofs and more general analysis of the “typical behaviour” of algebraic generating functions can be found in these references, as well as in [17, Section VII.7].

The following theorem is a part of [1, Theorem A.6]. Similar to the treatment in [1] and [13], we suppress the dependence on q for now since it plays no role in this result.

- Theorem 4.1 (Bassino et al. [1]). Consider a system of equations denoted as Y (z) = Φ(z,Y (z)), where Φ(z,y) is a vector of polynomials in z and y over Z. Let M be the Jacobian of Φ(z,y) wrt y. Also, assume the following:

- 1. Φ is strongly connected.
- 2. Φ(0,0) = 0.
- 3. M(0,0) = 0 as a matrix.
- 4. Φ(z,0) ̸= 0.
- 5. Φ is not linear in the second argument.


Then there is a unique solution Y (z) of the equation Y (z) = Φ(z,Y (z)) in the ring of formal power series with no constant coefficient. All entries have non-negative coefficients and the same radius of convergence ρ < ∞.

Additionally, there exists (z,y) in the region of convergence of Φ such that y = Φ(z,y), and M(z,y) has dominant eigenvalue 1.

Using this theorem, one gets the existence of a point at which the dominant eigenvalue is 1. One can use this to apply the following result (originally [13, Theorem 2.33]) to find a local representation of our generating functions around the dominant singularity. The singularity is of the square-root type, giving us the generic behaviour of algebraic generating functions.

Let the number of equations in our system be N. Though the general theorems and definitions that follow work for any finite set of qis, we only consider one q-variable.

- Theorem 4.2 (Drmota [13]). Consider a non-linear system of functions Φ(z,Y ,q) that are analytic around (0,0,0). Let M be the Jacobian of Φ(z,y,q) wrt y. Assume that:


- 1. All Taylor coefficients are non-negative.
- 2. Φ is strongly connected.
- 3. Φ(0,Y ,q) = 0.
- 4. Φ(z,0,q) ̸= 0.
- 5. ∂zΦ(z,Y ,q) ̸= 0.


Y = Φ(z,Y ,1), (4.1) 0 = det(I − M(z,Y ,1)), (4.2)

have a common non-negative solution inside it. Let the solutions be z = zc(q), Y = Yc(q) in a complex neighbourhood U of q = 1 that are real, positive, and minimal for positive real q ∈ U.

Let Y = Y (z,q) = Y1(z,q) Y2(z,q) ... YN(z,q) T denote the analytic solutions of Y = Φ(z,Y ,q) where Y (0,q) = 0.

Then there exists an ϵ > 0 such that Yj(z,q) admit a representation of the form

z zc(q)

Yj(z,q) = gj(z,q) − hj(z,q) 1 −

(4.3)

for q ∈ U, |z − zc(q)| < ϵ, |arg(z − zc(q))| ̸= 0, where gj,hj are analytic functions with

gj(z,q) ̸= 0, (4.4) hj(z,q) ̸= 0, (4.5)

gj(zc(q),q) j = Yj(zc(q),q) j = Yc(q). (4.6)

With this, one can apply a version of the Drmota-Lalley-Woods theorem ([12, Theorem 1]), which we state after the following definition.

- Definition 4.3. We say our system Φ is of simple type if there exist 2-D cones Cj ⊆ R2 for 1 ≤ j ≤ N such that they are centered at 0 and have the following property: For sufficiently large (n,m) ∈ Cj we have yj,n,m > 0, where yj,n,m are the Taylor coefficients of Yj,


Yj(z,q) =

yj,n,mznqm for 1 ≤ j ≤ N. (4.7)

n,m

We note that a system being of simple type is a sufficient condition for there being only one dominant singularity that contributes to the asymptotics.

- Theorem 4.4 (Drmota [12]). Consider a non-linear system of functions Φ(z,Y ,q) that are analytic around (0,0,0). Let M be the Jacobian of Φ(z,y,q) wrt y. Assume that:


- 1. All Taylor coefficients are non-negative.
- 2. Φ is strongly connected.
- 3. Φ(0,Y ,q) = 0.
- 4. Φ(z,0,q) ̸= 0.
- 5. ∂zΦ(z,Y ,q) ̸= 0.


Y = Φ(z,Y ,1), (4.8) 0 = det(I − M(z,Y ,1)), (4.9)

have a common non-negative solution inside it. Let the solutions be z = zc(q), Y = Yc(q) in a complex neighbourhood U of q = 1. Define λ and σ2 as:

1 zc(1)

∂zc ∂qk q=1

λ = −

∂2zc ∂q2 q=1

1 zc(1)

σ2 = −

+ λ2 + λ. (4.10)

If the system is of simple type and σ2 > 0, then the Taylor coefficients of Yj(z,q) =

yj,n,mznqm 1 ≤ j ≤ N (4.11)

n,m

are asymptotically given, for m close to λn, by

aj(zc(1))−n 2√2πn2

yj,n,m =

(m − λn)2 2nσ2

exp −

+ O(√n) , (4.12)

uniformly for all n,m, where yj,n,m ̸= 0, and aj ≥ 0, 1 ≤ j ≤ N. In fact, [12] and [13] also give implicit expressions for aj, but we don’t need them in our case.

We see that the asymptotics results require bounds on the variance of the statistic. For bivariate algebraic generating functions, one can sometimes find expressions for their moments. We will require the following lemma for that.

- Lemma 4.5. Consider a generating function f(z,q) which is locally, around z = r(q), of the form


z r(q)

f(z,q) = a(z,q) + b(z,q) 1 −

(4.13)

where a(z,q) and b(z,q) each have radii of convergence > r(q). Let X denote the statistic counted by q. Then:

r′(1) r(1)

E[X] n

= −

lim

, (4.14)

n→∞

2

r′′(1) r(1)

r′(1) r(1)

r′(1) r(1)

V[X] n

= −

−

lim

+

. (4.15)

n→∞

Proof. Differentiating f, we get

b · r′ · z r2

−1/2

∂f ∂q

z r

- 1

- 2


z r

= a′ + b′ 1 −

1 −

+

, (4.16)

−3/2 b · (r′)2 4r4

∂2f ∂q2

z r − z2 1 −

z r

= a′′ + b′′ 1 −

−1/2 b′ · r′ r2 −

b · (r′)2 r3

b · r′′ 2r2

z r

+ z 1 −

+

. (4.17)

Let R = r(1),R′ = r′(1),R′′ = r′′(1). Then, on applying [17, Theorem VI.1] (considering only the dominant term) and [17, Proposition III.2] we get

R′ R

E[X] ∼ −n

+ c1, (4.18)

2

2

R′ R

R′ R

2R′ · b′(R,1) R · b(R,1) −

R′′ R

E[X(X − 1)] ∼ n2

−

+ n

+ c2 (4.19)

where c1,c2 are O(1) terms. These can be calculated explicitly by iterating the asymptotic method to get subdominant terms. Rearranging these, we get the required expressions.

| |
|---|


###### 4.2 Partial asymptotics for G(p1,...,pk)

Here, we discuss the asymptotics of the system consisting of walks on the one-sided graphs. Recall the system from Section 3.3. The equations for walks on one-sided graphs are:

L(0i) = 1 + z[L(1i) + qL(pi)

- i−1], (4.20) L(ri) = z[L(ri−)1 + L(ri+1) ]
- j̸=i


L(0j) (1 ≤ r ≤ pi − 2), (4.21)

L(pi)

i−1 = z[L(pi)

i−2 + q−1L(0i)]

L(0j), (4.22)

j̸=i

for all 1 ≤ i ≤ k.

In this first part of asymptotics, we consider the system consisting of only these equations. Equation (3.15), which relates these to walks on the entire graph, will only be considered Section 7 onwards.

In order to apply the asymptotics results, we see one minor and two major technical hurdles. First, the minor technicality; the winding number is not non-negative as required by the theorems. This can be easily fixed by the substitution z  → zq. Hence, we pick up an additional q with every step, which is equivalent to the invertible transformation W  → W + n. This shifts the mean of the statistic to n and makes it non-negative while keeping the variance the same. Hence, we can apply this transformation, use the theorems, and then shift the mean back to 0.

The two major technical hurdles we face are:

- • Bounding the variance of winding number.
- • Proving the system is of simple type.


We deal with the former in Section 5, and with the latter in Section 6.

Using those, one can get the following local limit law for our system of L(ji), specialised to even lengths and even winding numbers. We note here that for this particular law, we do not consider

the Pis and Fk in the system as discussed above.

- Theorem 4.6. For any finite system of facets, let L(0i) = n,m ci,n,mznqm. Then, asymptotically


aiβ−2n n2

ci,2n,2m =

exp −m2 γn

+ O(√n) , (4.23)

when m is close to 0, for some positive constants ai,β,γ.

The proof is described in Section 6, and follows by combining Lemma 6.2, Lemma 6.4, and Lemma 6.6.

This gives us the asymptotics of the system with walks on the one-sided graphs. We will use this to find a local limit law for Fk in Section 7.

### 5 Decompositions, patterns, and variance

The first substantial issue we face for asymptotics is that the variance should be bounded on both sides. Hence, we show here that the variance of the winding number is Θ(n).

The tools for proving the upper bound are built in Section 5.1, and for the lower bound in Section 5.2. Then Section 5.3 puts them together for our bound.

###### 5.1 Decomposing the walk

In this section, we see how to decompose our walk into constituent subwalks, each with its own winding number contribution. This allows us to represent the generating function Fk(z;q) in a different way, using which we can find a linear upper bound on the variance (Theorem 5.10).

- Lemma 5.1 (Decomposition). Fk(z;q) = m,n fm,nqmzn. We can represent it in the form


Fk(z;q) =

n

n

1 q

dn,ℓzn q +

ℓ=0

ℓ

, (5.1)

where dn,ℓ ≥ 0 is the number of walks of length n with ℓ non-trivial loops. Proof. In any closed walk on our graph, we get a non-zero contribution for the winding number any time all the following things happen:

- 1. The walk enters a new facet, going farther away from the root.
- 2. The walk subsequently stays in the facet, or goes farther away from the root.
- 3. The walk returns to the facet, and moves back closer to the root from a different edge than it entered the facet with.


Hence, every facet can independently contribute a 0,1, or −1 to the winding number. We note that if the walk enters a facet multiple times, each instance is treated independently. When a walk leaves a facet, it must re-enter the facet using exactly the same vertex due to the Schreier graph having a tree-of-polygons structure. This happens since every vertex is a cut vertex in our graph.

So, in a closed walk, all the non-zero contributions to the winding number can be independently switched in sign by reversing the walk in the corresponding facet. Therefore, if we have ℓ nontrivial contributions to the winding number in a walk, we can switch any subset of them around independently. Therefore q and q−1 are equiprobable, and the result follows.

| |
|---|


- Figure 6: Walk decomposition and switching the winding number contribution of a particular loop. Notice that one can reverse the direction of the walk on the main facet without changing the orientation on any of the other facets.


This tells us that every individual contributing loop can be flipped. Hence, we do not have very heavy tails since the contributing loops can be flipped in the opposite direction to get a value closer to the mean.

###### 5.2 Pattern theorem

In this section, we prove a pattern theorem for closed walks on our graphs. In general, a pattern theorem shows that a small pattern or a motif occurring in a combinatorial class implies that most large objects in that class contain a positive density of that pattern. Pattern theorems are ubiquitous in combinatorics literature, and the first pattern theorem is attributed to Kesten [26] in the setting of self-avoiding walks.

In particular, our pattern would be a cycle across the facet of the largest length in our configuration. Our case is somewhat simpler due to the vertex-transitivity of our Schreier graphs. However, even without that, one can make this argument along the lines of [7, Section 3] and [4]. This leads to the lower bound on variance in Theorem 5.10.

Fix a given group Gk, and let the largest pi be p. We assume that p > 2, since we have explicitly computed the case that all pi = 2 in Section 2. We fix our pattern to be a directed closed cycle on p vertices.

- Definition 5.2. Let M be the set of closed walks on the Schreier graph of Gk. Also, let M(z) = y∈M z|y| = n mnzn.

Clearly, the pattern naturally occurs in these walks. We now try to show that it must occur a linear number of times, in most of the walks.

- Definition 5.3. Let c > 0 be fixed and small. Let H be the class of all walks y with at most c|y| patterns. This is the class of walks with density of patterns at most c. Also let H(z) be the corresponding generating function.


The main technical step of this section is to show that the exponential growth rate of H is strictly smaller than that of M. We do this by showing that the radius of convergence of the generating function H(z + zp) is strictly larger than that of M(z). To do this, we need to have a solid combinatorial interpretation of the substitution z  → z +zp; we should understand this as a process in which at each vertex, independently, we either leave it alone (z  → z) or insert a length p walk (z  → zp). There are some technical conditions require to ensure that this substitution is consistent, and we summarise those as an attachment scheme (see [4] for other examples of this idea).

- Definition 5.4. An attachment scheme is a procedure to attach patterns to elements in H that has the following properties:


- 1. The pattern addition preserves the vertex where we break the walk to add it.
- 2. The pattern attachment is not an iterative process. Once a pattern is attached, any new places it creates for viable attachments can not be used. In this way, the pattern addition can be parallelised, and so nested patterns cannot be added. We might have nested patterns when the base walk already has some patterns, but no nesting is permitted in the newly added patterns (this is because we are making a single substitution).
- 3. We can add a pattern at every vertex of the walk.
- 4. All patterns and walks lie in M that is closed under any number of attachments of the pattern. Hence, the result of this substitution process must stay within M.


We note here that we count labelled vertices here, with the starting vertex being numbered 0. So a walk of length 4 that just bounces between 2 vertices would still be counted as being on 4 vertices. (This convention gives us the convenience that our generating function for walks on n vertices is the same as the generating function for walks of length n).

We define our addition scheme as follows. Consider a walk of length n. At each of those vertices, either do nothing, or break the walk, attach a p-cycle (our pattern), and continue the walk again from the same vertex.

We note that due to the structure of the Schreier graph, every vertex can potentially have a p-cycle attached to it. Hence, this is a valid attachment process.

Figure 7: Example of attachment with our walks.

- Definition 5.5. Let K be the (multi-)set of walks obtained by using the attachment procedure on H. While some caution is needed to deal with the multiplicities, we can (thankfully) manage to bound the multiplicities to get our pattern theorem. Then, one can write this attachment as a generating function substitution.


z|y| =

hnzn, (5.2)

H(z) =

n

y∈H

z|y| =

knzn (Has multiplicity) (5.3)

K(z) =

n

y∈K

= H(z + zp). (Attachment process) (5.4)

From this, one gets an expression for the growth rate of K. This is the restatement of [4, Lemma 2] with our parameters.

- Lemma 5.6 (Bender et al. [4]). For H(z) and K(z) described above, we get that


1 µ(H)

1 µ(K)

1 µ(K)p

=

+

. (5.5)

- Theorem 5.7 (Pattern Theorem). Under the setting described above, where we have a valid attachment procedure, we get µ(M) > µ(H). Consequently, the set of walks without a density of patterns is exponentially small in the set of all walks.


We remind the reader that the definition of the set H implicitly depends on a constant c > 0. So the above statement implicitly asserts the existence of some c > 0 that defines an H that makes the above true; see Corollary 5.8 that follows the proof. The proof below follows [7, Section 3].

Proof. Consider y ∈ M with length n. So, y is either in K or not. Let sn count the number of walks on n vertices not in K. Let kn,ℓ be the number of walks in K with length n and having ℓ patterns.

For any x ∈ K with length n, let #n(x) be its multiplicity. Also, let x˜n ∈ G be the walk with the highest multiplicity with length n. So

1 #n(y) ≥

1 #n(y) ≥

mn = sn +

y∈K |y|=n

y∈K |y|=n

1 #n(x˜n)

y∈K |y|=n

kn #n(x˜n)

=

. (5.6)

Since #n(x˜n) is the maximum multiplicity of any walk, we have #n(x˜n) = max{#n(y) : y ∈ K} (5.7)

 

 

ℓ j

: ℓ ≤ n, kn,ℓ ̸= 0

(each pattern is replaced or not) (5.8)

= max





j≥ℓ−cn

ℓ i

: ℓ ≤ n, kn,ℓ ̸= 0 (symmetry of the binomial) (5.9)

= max

i<cn

≤ max

=

i<cn

n i

i<cn

n i ≤ cn

: ℓ ≤ n, kn,ℓ ̸= 0 (since ℓ ≤ n) (5.10)

n cn ≤ cn

e c

cn

= tn. (5.11)

Hence, we get mn ≥ kn/tn, where tn implicitly depends on c. Now, µ(M) = limsup

(m1n/n) (5.12)

n

1/n

1/n

1 cn

c e

c e

kn tn

c

c

≥ limsup

lim

= µ(K)

. (5.13)

= µ(K)

n

n

Now, we can use Lemma 5.6 on the above expression. µ(M) µ(H) ≥

c e

c µ(K) µ(H)

c e

1 µ(K)

1 µ(K)p

c

=

µ(K)

+

(5.14)

c e

c

1 + µ(K)−p−1 > 1. (5.15)

=

The last line follows since (c/e)c −→ 1. Additionally, notice that µ(H) is bounded below by the growth rate of returns on trees, and bounded above by twice the number of generators of the group. Hence 0 < µ(H) ≤ 2k < ∞. Then, Lemma 5.6 implies 0 < µ(K) < ∞.

| |
|---|


Corollary 5.8. For our case of closed walks on graphs, there exist constants c,d > 0 such that for a random walk of length n, say y ∈ M,

P[y has ≤ cn patterns] ≤ e−dn. (5.16)

###### 5.3 Variance

Now, we can use Corollary 5.8 and Lemma 5.1 to prove that the variance of the winding number of a closed random walk of length n is Θ(n).

We will need this technical but standard probability lemma. There are many proofs of this available. For one using moment generating functions, see [35, Example 1.5(A)].

- Lemma 5.9. Let {Xi}i be a sequence of iid RVs with mean λ and variance σ2. Let Sn = ni=0 Xi be the sum of the first n RVs. Let N be a (bounded) random variable taking values in {0,1,2,...} that is independent of the Xis. Then


E[SN] = λE[N], (5.17) V[SN] = λ2V[N] + σ2E[N]. (5.18)

The lower bound comes from the pattern theorem we proved. Heuristically, since we have a lot of small patterns, we can flip each of those independently to give the walk different values of winding number. Hence, the variance cannot be too small. The upper bound directly follows from the decomposition of the walk in Lemma 5.1.

- Theorem 5.10. Let W be the winding number of a closed random walk. Then V[W] = Θ(n).


Proof. For the lower bound, consider any walk of length n. Here, we can separate the winding number contribution from the patterns, and from the “base” walk after removing the patterns. This idea is inspired by [39].

Let W be the winding number of a random walk, and Wb,Wp denote the contributions from the base walk and patterns, respectively. Then W = Wb + Wp. Also we note Wb and Wp are independent. So, we have V[W] = V[Wb] + V[Wp].

To proceed further, let the winding number contribution of the i-th pattern be given by Xi. Let N be the number of patterns. For a walk of length n, the random variable N is bounded above by n. Then, by the notation in Lemma 5.9, Wp ≡ SN.

We also note that Xis are iid Rademacher, that is, they are discrete random variables with distribution P[Xi = 1] = P[Xi = −1] = 1/2. Hence:

V[W] = V[Wb] + V[Wp] (5.19) = V[Wb] + V[SN] (5.20) = V[Wb] + V[Xi]E[N] (Since E[Xi] = 0) (5.21) ≥ E[N] (Since V[Xi] = 1) (5.22) ≥ cn(1 − e−dn) (From Corollary 5.8) (5.23) = Ω(n). (5.24)

For the upper bound, consider the expression of Fk in Lemma 5.1:

n

ℓ

1 q

dn,ℓzn q +

Fk(z;q) =

. (5.25)

n

ℓ=0

Now, one can use [17, Proposition III.2] to get

n nℓ=0 dn,ℓ2ℓ n ℓ=0 dn,ℓ2ℓ

n ℓ=0 dn,ℓ2ℓℓ

V[W] =

n ℓ=0 dn,ℓ2ℓ ≤

= n. (5.26)

Hence, putting these together, V[W] = Θ(n). We also note that the variance via patterns and decomposition here has used the final generating function Fk. However, the same arguments work for the generating functions L(0i).

| |
|---|


### 6 Transformations and proof of Theorem 4.6

The second substantial issue we face is that our system is not of simple type due to parity effects in the coefficients, which stem from the parities of the facets. To deal with this, we consider three different cases:

- 1. all facets even [even case]
- 2. all facets odd [odd case]
- 3. at least one odd and one even facet [mixed case].


As a result, we cannot immediately apply the results of Section 4 to our system of equations. Thankfully, there are some simple transformations of our system that make it amenable to these results, which we describe in this section.

###### 6.1 Even case

Here, all pi are even, and hence all the facets have even length. We note that the coefficients of odd powers of z in L(0j) are all zero. So, the system has a symmetry L(0i)(z;q) = L(0i)(−z;q). Hence, near q = 1, we get two singularities zc(1) and −zc(1) with equal and opposite contributions. To deal with this, we restrict our system to give us the asymptotics along the even-length walks. This removes the additional singularity.

We describe the transformations required by an example which can be generalised in a straightforward manner. Consider the case with a square and a hexagon (p1 = 4,p2 = 6):

- L(1)0 = 1 + z[L(1)1 + qL(1)3 ], (6.1a)
- L(1)1 = z[L(1)0 + L(1)2 ]L(2)0 , (6.1b)
- L(1)2 = z[L(1)1 + L(1)3 ]L(2)0 , (6.1c)
- L(1)3 = z[L(1)2 + q−1L(1)0 ]L(2)0 , (6.1d)


- L(2)1 = z[L(2)0 + L(2)2 ]L(1)0 , (6.1f)
- L(2)2 = z[L(2)1 + L(2)3 ]L(1)0 , (6.1g)
- L(2)3 = z[L(2)2 + L(2)4 ]L(1)0 , (6.1h)
- L(2)4 = z[L(2)3 + L(2)5 ]L(1)0 , (6.1i)
- L(2)5 = z[L(2)4 + q−1L(2)0 ]L(1)0 . (6.1j)


L(2)0 = 1 + z[L(2)1 + qL(2)5 ], (6.1e) We note that the expressions arising in the even-length walks can further be written in terms of even-length walks:

- L(1)1 + qL(1)3 = z[2L(1)0 + L(1)2 + qL(1)2 ]L(2)0 , (6.2a)

- L(1)1 + L(1)3 = z[L(1)0 + q−1L(1)0 + 2L(1)2 ]L(2)0 , (6.2b)
- L(2)1 + qL(2)5 = z[2L(2)0 + L(2)2 + qL(4)2 ]L(1)0 , (6.2c)


- L(2)1 + L(2)3 = z[L(2)0 + L(2)4 + 2L(2)2 ]L(1)0 , (6.2d)


- L(2)3 + L(2)5 = z[L(2)2 + q−1L(2)0 + 2L(2)4 ]L(1)0 , (6.2e)


Substituting these back into the system, we get

- L(1)0 = 1 + z2L(2)0 [2L(1)0 + L(1)2 + qL(1)2 ], (6.3a)

- L(1)2 = z2(L(2)0 )2[L(1)0 + q−1L(1)0 + 2L(1)2 ], (6.3b)
- L(2)0 = 1 + z2L(1)0 [2L(2)0 + L(2)2 + qL(2)4 ], (6.3c)


- L(2)2 = z2(L(1)0 )2[L(2)0 + 2L(2)2 + L(2)4 ], (6.3d)


- L(2)4 = z2(L(1)0 )2[L(2)2 + 2L(2)4 + q−1L(2)0 ]. (6.3e)


Now, we can substitute z2 = t in this new set of equations and get the system we need. This tells us that all even-length walks have only one singularity, so we can apply the results above.

- Lemma 6.1. In the setting above with all even lengths, the system is of simple type.


Proof. We show this for an arbitrary L(0i). Similar arguments work for other L(ji) generating functions. With some abuse of notation, let the L(0i) post-transformation be L(0i)(t;q) = n,m di,n,mtnqm. The transformation gives us the mapping di,n,m = ci,2n,m. Indeed, one can think of n being the “half-length” of a walk.

First, note that di,0,0 = 1, and then by stepping out and back along any incident edge, we have di,n+1,0 ≥ di,n,0. Then, by walking around the smallest facet in either direction, we have that di,n+p/2,m±1 ≥ di,n,m, where p is the length of the shortest facet.

By iterating these relations, we have that di,n,m > 0 for any |m| ≤ ⌊2n/p⌋, giving us the required cone of positive coefficients.

| |
|---|


- Lemma 6.2. For the setting above with all even lengths, the non-zero Taylor coefficients of L(0i)(t;q) = n,m di,n,mtnqm (when m is close to 0) are asymptotically given by


aiβ−n 23/2πn2

di,n,m =

exp −m2 2γn

+ O(√n) , (6.4)

for positive constants ai,β,γ.

Proof. We begin by substituting L˜(i) = L(0i) − 1 in our system. The new system now is in the variable Y = L ˜(1) L(1)1 ··· L˜(2) L(2)1 ··· L˜(k) L(1k) ···

T

. Let the equations by denoted by Φ(t,Y ,q). This is the system we discussed earlier with all the even-length walks. We can check that this system does indeed satisfy the conditions in Theorem 4.1. Hence, there is a solution to Y (t,1) = Φ(t,Y ,1) where M(t,Y ,1) has dominant eigenvalue 1. This gives us that

Yc(tc(1),1) = Φ(tc(1),Yc(1),1), (6.5) det(I − M(t,Y ,1)) = 0 (6.6)

are satisfied. We define λ and σ2 by

1 tc(1)

∂tc ∂q q=1

λ = −

1 tc(1)

σ2 = −

∂2tc ∂q2 q=1

+ λ2 + λ. (6.7)

We can apply Theorem 4.2 here to get a local representation of Yj(t,q) of the form

t tc(q)

Yj(t,q) = gj(t,q) − hj(t,q) 1 −

, (6.8)

where gj,hj are analytic functions. Define X to be the random variable that counts the winding number. Now, from Lemma 4.5, we see that

V[X] n

E[X] n

= σ2. (6.9)

= λ and lim

lim

n→∞

n→∞

Now, from our earlier discussion on shifting the mean, we can take λ = 0. Then, using Theorem 5.10 and Lemma 4.5 we get that σ2 = γ for some constant γ > 0. In fact, for explicit cases, we can calculate it using the same procedure.

Now, applying Theorem 4.4, we get that asymptotically

ai(tc(1))−n 23/2πn2

di,n,m =

exp −m2 2γn

+ O(√n) , (6.10)

when m is close to 0, and for some positive constants ai (depending on the solution to the system). We only look at the expansion of L˜(i) here, but a similar expansion holds for the entire system.

| |
|---|


- 6.2 Odd case Here, we note that nonzero coefficients can only occur when powers of q and z have the same parity.


Hence, our system has the symmetry L(0i)(z;q) = L(0i)(−z;−q). Since a local limit law depends on the behaviour of the function on the entire unit circle (|q| = 1), this gives us contributions from

both zc(1) and −zc(−1). Here, we can remove the parity effects by substituting q2  → u. In order to keep the system polynomial, we also substitute z  → tq. This is the same substitution as shifting the mean. As an example, we consider the case with a triangle and a pentagon (p1 = 3,p2 = 5):

- L(1)0 = 1 + t√u[L(1)1 + √uL(1)2 ], (6.11a)

- L(1)1 = t√u[L(1)0 + L(1)2 ]L(2)0 , (6.11b)

- L(1)2 = t√u[L(1)1 +


√

u−1L(1)0 ]L(2)0 , (6.11c) L(2)0 = 1 + t√u[L(2)1 + √uL(2)4 ], (6.11d)

- L(2)1 = t√u[L(2)0 + L(2)2 ]L(1)0 , (6.11e)

- L(2)2 = t√u[L(2)1 + L(2)3 ]L(1)0 , (6.11f)

- L(2)3 = t√u[L(2)2 + L(2)4 ]L(1)0 , (6.11g)

- L(2)4 = t√u[L(2)3 +


√

u−1L(2)0 ]L(1)0 . (6.11h)

Substituting the odd-length walks (L(1)1 ,L(2)1 ,L(2)3 ) back into the system we get

- L(1)0 = 1 + t[uL(1)2 + tu(L(1)0 + L(1)2 )L(2)0 ], (6.12a) L(1)2 = tL(2)0 [tuL(2)0 (L(1)0 + L(1)2 ) + L(1)0 ], (6.12b)
- L(2)0 = 1 + tu[L(2)4 + t(L(2)0 + L(2)2 )L(1)0 ], (6.12c) L(2)2 = t2u(L(2)0 )2[L(2)0 + 2L(2)2 + L(2)4 ], (6.12d) L(2)4 = tL(1)0 [tuL(1)0 (L(2)4 + L(1)2 ) + L(2)0 ]. (6.12e)


This gives us the system we can use.

- Lemma 6.3. In the setting above with all odd lengths, the system is of simple type.


Proof. We show this for an arbitrary L(0i). Similar arguments work for the other L(ji) generating functions. With some abuse of notation, let the generating functions L(0i) post-transformation be L(0i)(t;u) = n,m di,n,mtnum.

The sequence of transformations is (z,q)  → (z,√u)  → (t√u,√u). Hence, the transformations give us the relations

di,n,m = ci,n,2m−n ci,n,m = di,n,m+n

. (6.13)

2

This works because the only nonzero coefficients initially were the ones with m and n having the same parity.

First, note that di,n,n/2 = ci,n,0 > 0 for even n by stepping out and back along any incident edge. Also, for sufficiently large odd n, di,n,(n±1)/2 = ci,n,n±1 > 0.

Then, by walking around the smallest facet in either direction, we have that di,n+p,(n+p+m±1)/2 = ci,n+p,m±1 ≥ ci,n,m = di,n,(n+m)/2, where p is the length of the shortest facet, and p odd.

By iterating these relations, we get the required cone with axis m = n/2.

| |
|---|


- Lemma 6.4. For the setting above with all odd lengths, the non-zero Taylor coefficients of L(0i)(t;u) = n,m di,n,mtnum (when m is close to n) are asymptotically given by


aiβ−n 23/2πn2

di,n,m =

exp −(m − n)2 2γn

+ O(√n) , (6.14)

for positive constants ai,β,γ. The proof follows from the same argument as in Lemma 6.2.

###### 6.3 Mixed case

In case we have both even and odd length facets, neither of the issues occurs. We can have loops of both even and odd length contributing to the winding number. The system is actually of simple type. Hence, we do not have any unwanted symmetries in the system and require no transformations. So, we only have one singularity and saddle point corresponding to zc(1).

- Lemma 6.5. In the setting with at least one even and one odd length, the system is of simple type.

Proof. We show this for an arbitrary L(0i). Similar arguments work for other L(ji) generating functions. First, note that ci,n,0 > 0 for all even n by stepping out and back along any edge. Now, let the smallest even pi in the group presentation of Gk be p1, and the smallest odd pi be p2.

Now, by walking along the smallest odd or even facet in either direction, we get ci,n+p1,m±1 ≥ ci,n,m and ci,n+p2,m±1 ≥ ci,n,m. Since p1 and p2 have different parities, iterating these relations gives us the required cone.

| |
|---|


- Lemma 6.6. For a mixed system, the non-zero Taylor coefficients of L(0i)(z;q) = n,m ci,n,mznqm (when m is close to 0) are asymptotically given by

ci,n,m =

aiβ−n 23/2πn2

exp −m2 2γn

+ O(√n) , (6.15)

for positive constants ai,β,γ. The proof, again, follows from the same argument as in Lemma 6.2.

- 7 Part 2: Asymptotics of Fk


We now move the asymptotics of L0 proven in Section 4 to the asymptotics of Fk. This is done by showing that a walk on the entire Schreier graph spends very little time at the root, and hence the asymptotics are governed by the asymptotics of the walks in the one-sided graphs. This will prove the main result of the paper.

We first note that Theorem 4.1 implies that all the L(ji) in our system have the same growth rate. Additionally,

1 1 − P1

L(1)0 =

1 1 − kj=1 Pk

. (7.1)

Fk =

Definition 7.1. We choose any arbitrary L(0i)(z;q) (say L(1)0 (z;q)) and call it L(z;q). We will use this for our asymptotics.

This is okay to do since L(ji) all have the same growth rate, and all L(0i) have the same asymptotics. The asymptotics of L are not those of a simple pole, and hence the dominant singularity does not arise from the zero of the denominator. Instead, it must come from P, and so L and P1 have the same radius of convergence. Since all the Lj have the same radius of convergence, we know that all the Pj have the same radius of convergence.

The dominant singularity of Fk comes either from the zero of the denominator or from the Pjs, which is also that of the Lj. If we can show that Fk has the same radius of convergence as the Lj, then the dominant singularity of Fk must come from the Pjs and so not be a pole. As a consequence, the asymptotics will have a similar form to that of the Lj.

Firstly, using the popularity argument [23] from statistical mechanics, we can show that the growth rates are the same for q > 0. We sketch it out here for completeness. Unfortunately, it does not work for other q and hence we will need more specialised results.

###### 7.1 Popularity argument

We will need the following lemma, which is a generalisation of the well-known Fekete’s lemma by Erd˝s and de Bruijn [11, Theorem 23].

- Lemma 7.2 (Fekete, Erd˝s, de Bruijn). Consider a sequence {an}n, and a function ψ(t) that is positive and increasing for t > 0. Assume that


∞

ψ(t) t2

an+m ≤ an + am + ψ(n + m) and

dt < ∞. (7.2) Then the following limit exists for some −∞ ≤ ℓ < ∞:

1

an n

lim

= ℓ. (7.3)

n−→∞

Consider our original system Y (z,q) = Φ(Y ,z,q). Since all the Yi have the same radius of convergence, we choose any L(0i) and call it L. We will argue that it has the same growth rate as Fk. So, we have

Fk(z;q) =

n,m

fn = fn(q) =

fn,mznqm, L(z;q) =

n,m

m

fn,mqm, cn = cn(q) =

cn,mznqm, (7.4)

m

cn,mqm. (7.5)

- Lemma 7.3. Let q > 0. Then, as functions of q, the following limits exist:


fn1/n and lim

lim

n−→∞

n−→∞

c1n/n. (7.6)

Proof. We show this for fn, and the same argument works for cn as well.

We see that fn1+n2,m1+m2 ≥ fn1,m1fn2,m2 since we can concatenate closed walks. The resulting walk is still closed. Now, for any n1,n2,

fn1,m1qm1 ·

fn2,m2qm2 (7.7)

fn1fn2 =

m1

m2

fn1,m1fn2,m2qm1+m2 (7.8)

=

m1 m2

fn1+n2,m1+m2qm1+m2 (7.9)

≤

m1 m2

fn1+n2,mqm. (7.10)

≤ 2(n1 + n2)

m

Here, the last inequality follows from the fact that we can sum over all possible values of m = m1 + m2, and there are at most 2(n1 + n2) ways of writing m as a sum of m1 and m2, each having the same contribution to the sum.

This gives us fn1fn2 ≤ 2(n1 + n2)fn1+n2. So, we get that

(−log fn1+n2) ≤ (−log fn1) + (−log fn2) + log(2(n1 + n2)). (7.11) We also note that

∞

log(2t) t2

dt = 1 + log 2 < ∞. (7.12)

1

Hence, by Lemma 7.2, log(fn)/n −→ ℓ ∈ (−∞,∞]. However, ℓ is not ∞ since log(fn)/n is bounded above (in this case by 2k, since at every vertex we have 2k choices of the next step). So the limit exists and is finite.

| |
|---|


Theorem 7.4. As a function of q, the growth rate of L is the same as that of Fk. That is, µq(L) = µq(Fk), when q > 0.

Proof. Since Fk counts all walks counted by L, we see that for any n cn =

cn,mqm ≤

fn,mqm ≤ n = fn. (7.13)

m

m

Hence, limsup|cn|1/n ≤ limsup|fn|1/n. So, µq(L) ≤ µq(Fk) when q > 0.

For the other direction, consider the walks counted by fn. We characterise them by the maximum distance the walk reaches from the root. Say fn(h) = # of closed walks of length n that reach a maximum of h distance away from the root.

Every walk is weighted by the winding number contribution, in the form of qm. Now, fn(h) = 0 when h > n/2, since the walks are closed. So, fn = n/h=02 fn(h). We choose an h∗ such that fn(h∗) ≥ fn(h) for all h. This is called the most popular choice. Hence, fn(h∗) ≤ fn ≤ n · fn(h∗).

We now relate fn(h∗) to L. Let y be an open walk of length h∗ that starts from the root, and walks to a vertex v that is h∗ distance away. Since the vertex v is h∗ distance away, a walk between the root and v of length h∗ is necessarily the shortest. Let the reversal of this walk be yˆ.

For any closed walk w (counted by Fk) that reaches a max distance of h∗ from the root, we can make a new walk y · wM · yˆ, where wM signifies repeating the walk M times. This is well defined since w is a closed walk (see Figure 8). This walk remains on one side of the graph by construction, and is hence counted by L. So, it follows that

fnM ≤ nM · cnM+2h∗, (7.14) f

1 nM+2h∗

M nM+2h∗

M

nM+2h∗ · c

n ≤ n

nM+2h∗, (7.15) fn1/n ≤ n1/n · µq(L) (Taking M −→ ∞), (7.16)

µq(Fk) ≤ µq(L) (Taking n −→ ∞). (7.17) Here, the limits exist due to Lemma 7.3.

| |
|---|


We note that the same argument also works between [q0]Fk(z;q) and Fk(z;1) to show that they have the same growth rate (sketched below), which we will use in Corollary 7.13.

yˆ

M

w

w

h∗

y

Figure 8: Construction of new walks in the popularity argument.

- Lemma 7.5. [q0]Fk(z;q) and Fk(z;1) have the same exponential growth rate.


Proof. Let the growth rate of [q0]Fk(z;q) be µ0 and that of Fk(z;1) be µ1. Then, clearly 0 ≤ µ0 ≤ µ1 ≤ 2k. In order to complete the proof, we show that µ0 ≥ µ.

Again, fn,m = 0 when |m| > n/2, and fn,m = fn,−m. So, we write

⌈n/2⌉

fn =

fn,m. (7.18)

m=⌊−n/2⌋

For a given n, there must be there is a value of m which gives the largest summand. That is, define m∗ so that fn,m∗ ≥ fn,m for all m. It follows that

fn,m∗ ≤ fn ≤ (n + 1)fn,m∗. (7.19) Taking the n-th root and then the limit as n −→ ∞ gives

fn,m1/n∗ = limsup

fn1/n = lim

fn1/n = µ. (7.20)

limsup

n→∞

n−→∞

n−→∞

Now fix n and consider a walk counted by fn,m∗ and another counted by fn,−m∗. Concatenating them gives a walk counted by f2n,0. Then considering all possible ways of concatenating M walks counted by fn,m∗ with M walks counted by fn,−m∗ gives the inequality

fn,mM ∗fn,M−m∗ ≤ fn,m2M∗ ≤ f2nM,0. (7.21)

Now take the (2nM)-th root of both sides and let M −→ ∞ to obtain fn,k1/n∗ ≤ µ0. Letting n −→ ∞ then shows that µ1 ≤ µ0. Thus, we must have that µ1 = µ0.

| |
|---|


###### 7.2 Geometric group theory

In order to proceed with showing that the growth rate of L and Fk is the same for all q, we use tools from geometric group theory and probability. We proceed by arguing that Fk is not dominated by a pole.

We first recall that the subgroup ⟨∆⟩ of Gk is normal (Lemma 3.1), so the Schreier graph of Gk with respect to the subgroup ⟨∆⟩ is the same as the Cayley graph of the quotient group ⟨∆⟩\Gk, which has the presentation

⟨a1,...,ak | ap11 = ap22 = ··· = apkk = e⟩. (7.22) We denote the quotient group as G˜k.

In light of this identification, we work with walks on the Cayley graph of G˜k from now on. Note that G˜k is a free product of finite groups, so it is virtually free (see, for example, [30, Theorem 2]) and hence hyperbolic.

Recall that the case in which p1 = p2 = ··· = pk = 2 has been handled explicitly in Section 2. Consequently we assume here that max{p1,...,pk} ≥ 3.

A hyperbolic group is said to be non-elementary if it is not virtually cyclic (that is, not virtually Z or finite). Notice that since we can assume that there exists pℓ ≥ 3, for any i ̸= ℓ the subgroup ⟨aℓai,a−ℓ 1ai⟩ is free of rank 2, so the group G˜k is non-elementary hyperbolic.

It follows that we may use the following result ([20, Theorem 1.1]) on asymptotics of random walks on Cayley graphs of hyperbolic groups.

Theorem 7.6 (Gou¨ezel [20]). Let Γ be a hyperbolic and non-elementary group. Consider the simple random walk on Γ starting at the root. Let P(n) denote the probability that the walk is at the root after n steps. Then

P(n) ∼ Cρ−nn−3/2,

where C > 0 is some constant and ρ > 1 is the inverse of the spectral radius. This holds for all n if the walk is not periodic. If the walk is periodic, the same still holds when restricted to even n.

Note that [20, Theorem 1.1] is stated for any admissible finitely supported symmetric probability measure on G, which for us corresponds to the simplest case of having uniform probability on each element of S ∪ S−1, which is a symmetric generating set for Γ.

###### 7.3 Expected number of returns

In this section, we drop the dependence on q, since we only talk about the structure and returns of the walk, without keeping track of the winding number. This, henceforth, is agnostic of the value of q. This is precisely the reason we are using this argument; arguments depending on the value of q seem not to work well (see Section 7.1).

- Definition 7.7. Let (Xn)n be a simple random walk on the Cayley graph of G˜k starting at the root (denoted by 0).

As noted above, this is the same as the walk on the Schreier graph of Gk. The walk is, unlike the walks considered above, not constrained to end at the root yet.

- Definition 7.8. Let P(n) be the probability that after n steps, the walk is at the root. Hence, P(n) = P[Xn = 0 | X0 = 0]. (7.23)


We note here that in the notation of our sequences of walks, we have

P(n) =

fn (2k)n

1 limsupn(P(n))1/n

=

, ρ =

2k µ(Fk)

. (7.24)

Since fn+m ≥ fnfm, we have P(n+m) ≥ P(n)P(m).

- Definition 7.9. Let Vn be the number of visits to the origin in a random walk of length n, and let vn = E[Vn | Xn = 0].


Consider such a visit in a walk; by cutting the walk at that point, one obtains two shorter walks that start and end at the root. Hence,

n−1 i=0 P(i)P(n−i)

vn = E[Vn | Xn = 0] =

, (7.25)

P(n)

when P(n) ̸= 0. If it is 0, we set the expectation to be 0 as well. The denominator here follows since we are conditioning on a bridge, so we divide by that probability.

- Theorem 7.10. Restricted to the subsequence where P(n) ̸= 0, vn is uniformly bounded.


Proof. From Theorem 7.6, we get that P(n) ∼ Cρ−nn−3/2 for some constant C. Let N ∈ N such that for any n > N

P(n) Cρ−nn−3/2 − 1 ≤

- 1

- 2


. (7.26)

Then we have for n > N:

n/2 i=0 P(i)P(n−i)

n−1 i=0 P(i)P(n−i)

P(n) ≤ 2

vn =

(7.27)

P(n)

 

  (7.28)

n/2

N

2 P(n)

P(i)P(n−i) +

P(i)P(n−i)

=

i=0

i=N+1

n/2

2 P(n)

P(i)P(n−i) since P(n) ≥ P(i)P(n−i) (7.29)

≤ 2(N + 1) +

i=N+1

9C n−3/2

≤ 2(N + 1) +

n/2

i−3/2(n − i)−3/2 (7.30)

i=N+1

9C n−3/2

≤ 2(N + 1) +

√

≤ 2(N + 1) + 18

2C

n/2

−3/2

n 2

i−3/2

i=N+1

∞

√

i−3/2 = 2(N + 1) + 18

i=1

(7.31)

2C · ζ(3/2), (7.32)

where ζ(3/2) ≈ 2.61237.... Hence, vn is bounded independent of n.

| |
|---|


###### 7.4 Return to the singularity

We use the expected number of returns to demonstrate that the dominant singularity is not a simple pole. The following lemma shows how to link the expected number of returns in a walk and the associated generating functions. It follows from fairly standard arguments.

Lemma 7.11. Consider combinatorial classes A,B with associated generating fucntions A(z) =

n αizn and B(z) = n βizn respectively. Let A be obtained by concatenating elements from B together in sequences. That is, their generating functions are related as

1 1 − B(z)

A(z) = 1 + B(z) + B(z)2 + ··· =

. (7.33)

In a random element of A of size n, let the number of elements of B be counted by a random variable T. Then

n i=1 αiαn−i

E[T] =

. (7.34)

αn

Proof. We construct an auxiliary generating function

1 1 − tB(z)

Aˆ(z;t) = 1 + tB(z) + t2B(z)2 + ··· =

. (7.35)

Hence, the variable t counts the occurrences of elements of B. We can compute the number of occurrences of B’s by differentiating with respect to t. This gives

∂Aˆ ∂t t=1

= Aˆ(z;1)2 − Aˆ(z;1). (7.36)

Then, applying [17, Proposition III.2] and setting t = 1 we get

[zn](A(z)2 − A(z)) [zn]A(z)

E[T] =

n i=0 αiαn−i

n i=1 αiαn−i

αn − 1 =

=

αn

(7.37)

since Aˆ(z;1) = A(z).

| |
|---|


We now prove the main technical result of the paper, which gives us a local limit law for Fk.

- Theorem 7.12. For the group Gk with at least one pi > 2, the dominant asymptotics of Fk(z;q) come from the dominant asymptotics of L(z;q). Consequently,


[z2nq2m]Fk(z;q) = f2n,2m = Cρ−nn−2 exp −m2 γn

+ O(√n) , (7.38)

when m is close to 0, and C,ρ,γ are positive constants. Proof. We begin by noting again that

1 1 − i Pi(z;q)

Fk(z;q) =

. (7.39)

As discussed at the start of Section 7, the dominant singularity of Fk comes either from the zero of the denominator or from the Pi’s, which is also that of the L. We now argue that the dominant singularity of Fk does not come from a pole. As a consequence, the asymptotics will have a similar form to that of the Lj.

Suppose the dominant singularity (say z = r) does come from a pole at the zero of the denominator. Then, locally around z = r, one can express

Q2(z) (1 − z/r)ℓ

Fk(z) = Q1(z) +

where ℓ ∈ {1,2,3,...} is the order of the pole, and Q1,Q2 are analytic functions. Then, standard analytic combinatorics results [17] show that fn ∼ Cr−nnℓ−1. By Lemma 7.11, one gets the expected number of returns:

(7.40)

n i=1 fifn−i

n i=1 iℓ−1

fn − 1 ≥ Cˆ

E[T] =

nℓ−1 = Ω(n), (7.41) for some positive constant Cˆ. This can be made precise, similar to the proof of Theorem 7.10. Similarly, if the dominant singularity comes from confluent singularities from the pole and the singularity of P at the same radius, we get

Q2(z) (1 − z/r)ℓ−1/2

Fk(z) = Q1(z) +

, (7.42)

where ℓ ∈ {1,2,3,...} is the order of the pole, and Q1,Q2 are analytic functions. This happens since Pis and L have a square-root singularity.

The same argument as above shows that the expected number of returns is Ω(√n). Both these cases contradict Theorem 7.10.

As a consequence, we see that the dominant singularity of Fk is the same as that of L, and the result follows.

| |
|---|


We can now put everything together to prove that the cogrowth series of groups in our infinite family are D-finite and not algebraic.

Corollary 7.13 (Cogrowth series for G(p1,...,pk) = Gk). For the group Gk, the cogrowth series is D-finite but not algebraic. Additionally, the cogrowth series is an algebraic number.

Proof. When p1 = p2 = ··· = pk = 2, the result follows from Theorem 2.8. So now assume that at max{p1,··· ,pk} ≥ 3, so that we can use the asymptotic results from Theorem 7.12.

Note Fk(z;q) is algebraic (solution to a system of algebraic equations), and hence D-finite. As a result, [q0]Fk(z;q) is D-finite [29], and hence the cogrowth series is D-finite. This is not algebraic since the n−2 factor in the asymptotics is incompatible with an algebraic generating function ([17, Section VII.7] and [25]).

In order to see that the cogrowth is an algebraic number, one uses Lemma 7.5. Then, since Fk(z;1) is an algebraic generating function, the cogrowth is an algebraic number.

| |
|---|


### 8 Applying the techniques to other presentations

In this section, we consider three presentations for the 3-strand braid group as shown in Equation (1.4).

Starting with ⟨a,b | aba = bab⟩ and applying the Tietze transformation (see [31, Proposition 2.1]) that adds a new generator x we obtain

⟨a,b,x | aba = bab,x = ba⟩ = ⟨a,b,x | abaa = baba,x = ba⟩ = ⟨a,b,x | axa = x2,xa−1 = b⟩. (8.1) Then removing the generator b yields ⟨a,x | axa = x2⟩. Now adding a new generator c we obtain

⟨a,x,c | axa = x2,c = ax⟩ = ⟨a,x,c | axax = x3,c = ax⟩ = ⟨a,x,c | c2 = x3,cx−1 = a⟩. (8.2)

Then removing a yields ⟨x,c | c2 = x3⟩. Note that this presentation is also referred to as the (torus or) trefoil knot presentation, since it is a standard presentation for the fundamental group of the trefoil knot complement.

###### 8.1 The standard presentation Here, we work with the presentation

⟨a,b | aba = bab⟩ (8.3)

and apply our results above to this case. As before, we start by choosing a special element ∆. Previously, we chose a central element for ∆, but in this case, we set ∆ = aba ≡ bab; this does not commute with the generators but does interact with them in a simple way as follows.

∆a ≡ b∆, ∆b ≡ a∆, (8.4) ∆a−1 ≡ ba, ∆b−1 ≡ ab. (8.5)

Thus ∆2 is central; we could replace ∆ by ∆2. However, it makes the subsequent work more cumbersome. Some fairly standard work shows that every element of the group can be represented by a word with normal form

w ≡ ∆mp, (8.6)

where p is a word in non-negative powers of the generators {a,b}∗. Again, we form the Schreier graph of the cosets of the subgroup generated by ∆. The graph forms a tree (see Figure 9) similar to the group ⟨a,b | a3 = b3⟩ discussed in Section 3. Due to this similarity in the Schreier graphs, similar and quite explicit generating function arguments work here. We give the details in Appendix A.2. It turns out that the cogrowth series of this group with respect to this generating set is the same

- as that of G(3,3).


- Theorem 8.1. The cogrowth series for B3 with respect to the generating set {a,b} is D-finite but not algebraic.


b2 ab2a

b ab

b2a

ab2

e

ba2

a2b

a

ba

ba2b

a2

- Figure 9: The Schreier graphs of the cosets of the subgroup ⟨∆⟩ of B3 with respect to the generating set {a,b}. The vertex labelled p corresponds to the coset ⟨∆⟩p.


We note that our methods can be extended to generalisations of the group presented by

⟨a,b | (a,b)p = (b,a)p⟩, (8.7) where p ≥ 3 and ∆ = (a,b)p = abab...

.

p symbols

The Schreier graph consists of polygons with side lengths p, which means this group will have the same cogrowth series as G(p,p) and so be D-finite and not algebraic.

This extends in a reasonably straightforward way to any number of generators. For example, with 3 generators, the group with presentation

⟨a,b,c | (a,b,c)p = (b,c,a)p = (c,a,b)p⟩, (8.8) where ∆ = (a,b,c)p = abcabc...

, has the same cogrowth series as G(p,p,p).

p symbols

###### 8.2 Second presentation

Next, we consider the presentation ⟨x,c | c2 = x3⟩ for B3. This is G(2,3), and so we know that its cogrowth series is D-finite but not algebraic. In Appendix A.1 we compute the explicit asymptotic behaviour of the cogrowth series with respect to this generating set.

###### 8.3 Third presentation

Now consider the presentation ⟨a,x | axa = x2⟩ for B3. Setting ∆ = x3, the Schreier graph with respect to ⟨∆⟩ and {a,x} is shown in Figure 10. This still gives us a tree-like graph of triangles and squares, but now these meet along edges rather than vertices.

The absence of cut-vertices renders the combinatorial analysis substantially more difficult. See Appendix B. In spite of this, we can still show that the cogrowth series is D-finite but not algebraic.

- Figure 10: The Schreier graph of B3 with respect to the presentation ⟨a,x | axa = x2⟩ and ∆ = x3. The coset ⟨∆⟩ is indicated by the black vertex.


- Theorem 8.2. The cogrowth series for B3 with respect to the generating set {a,x} is D-finite but not algebraic.


The proof is quite similar to the results above, but requires us to keep track of more tedious details. In particular, we show that the cogrowth series is D-finite by (as done above) finding a system of algebraic equations with the cogrowth series as its diagonal. As a consequence, we reserve the details of proving D-finiteness to Appendix B (Theorem B.7).

The proof for non-algebraicity follows from similar arguments on asymptotics as described in the main body of the paper. The steps are similar but more tedious. In particular, more care is required to bound the number of returns and hence show that the singularities are the same. However, one can work this out to show that this group presentation also has non-algebraic cogrowth series.

### Acknowledgements

The authors thank Omer Angel, Tony Guttmann, Kasia Jankiewicz, Manuel Kauers, Jens Malmquist, and Stephan Wagner for helpful conversations. Elder acknowledges funding in the form of an ARC Discovery Project. Rechnitzer acknowledges funding in the form of an NSERC Discovery Project.

### References

- [1] Fr´ed´erique Bassino, Mathilde Bouvel, Valentin Fe´ray, Lucas Gerin, Micka¨el Maazoun, and Adeline Pierrot. Scaling limits of permutation classes with a finite specification: A dichotomy. Adv. Math., 405:108513, 2022.
- [2] Jason Bell, Haggai Liu, and Marni Mishna. Cogrowth series for free products of finite groups. Internat. J. Algebra Comput., 33(02):237–260, 2023.


- [3] Jason Bell and Marni Mishna. On the complexity of the cogrowth sequence. J. Comb. Algebra, 4(1):73–85, 2020.
- [4] Edward A Bender, Zhi-Cheng Gao, and L Bruce Richmond. Submaps of maps. I. General 0–1 laws. J. Combin. Theory Ser. B, 55(1):104–117, 1992.
- [5] Alex Bishop. On groups whose cogrowth series is the diagonal of a rational series. Internat. J. Algebra Comput., 34(8):1209–1224, 2024.
- [6] Corentin Bodart. A virtually nilpotent group whose green series is not D-finite. Internat. J. Algebra Comput., 0(0):1–11, 0.
- [7] Harrison Chapman. Asymptotic laws for random knot diagrams. J. Phys. A, 50(22):225001, May 2017.
- [8] N. Chomsky and M. P. Sch¨utzenberger. The algebraic theory of context-free languages. In Computer programming and formal systems, pages 118–161. North-Holland, Amsterdam, 1963.
- [9] Joel M. Cohen. Cogrowth and amenability of discrete groups. J. Funct. Anal., 48(3):301–309, 1982.
- [10] Arman Darbinyan, Rostislav Grigorchuk, and Asif Shaikh. Finitely generated subgroups of free groups as formal languages and their cogrowth. J. Groups Complex. Cryptol., 13(2):Paper No. 1, 30, 2021.
- [11] N.G. de Bruijn and P. Erd¨s. Some linear and some quadratic recursion formulas II. Indag. Math., 55:152–163, 1952.
- [12] Michael Drmota. Systems of functional equations. Random Structures Algorithms, 10(1-2):103– 124, 1997.
- [13] Michael Drmota. Random Trees: An Interplay between Combinatorics and Probability. Mathematics and Statistics. Springer Vienna, 2009.
- [14] Martin J. Dunwoody. The accessibility of finitely presented groups. Invent. Math., 81(3):449– 457, 1985.
- [15] Murray Elder, Andrew Rechnitzer, Esaias J. Janse van Rensburg, and Thomas Wong. The cogrowth series for BS(N,N) is D-finite. Internat. J. Algebra Comput., 24(2):171–187, 2014.
- [16] Murray Elder, Andrew Rechnitzer, and Thomas Wong. On the cogrowth of Thompson’s group F. Groups Complex. Cryptol., 4(2):301–320, 2012.
- [17] P. Flajolet and R. Sedgewick. Analytic combinatorics. Cambridge Univ. Press, 2009.
- [18] Scott Garrabrant and Igor Pak. Words in linear groups, random walks, automata and Precursiveness. J. Comb. Algebra, 1(2):127–144, 2017.
- [19] S´ebastien Gou¨ezel and Steven P. Lalley. Random walks on co-compact Fuchsian groups. Ann. Sci. Ec.´ Norm. Supe´r. (4), 46(1):129–173 (2013), 2013.
- [20] S´ebastien Gou¨ezel. Local limit theorem for symmetric random walks in Gromov-hyperbolic groups. J. Amer. Math. Soc., 27(3):893–928, 2014.


- [21] R. Grigorchuk, J.-F. Quint, and A. Shaikh. Multivariate growth and cogrowth. Carpathian Math. Publ., 17(1):82–109, 2025.
- [22] R. I. Grigorchuk. Symmetrical random walks on discrete groups. In Multicomponent random systems, volume 6 of Adv. Probab. Related Topics, pages 285–325. Dekker, New York, 1980.
- [23] J.M. Hammersley, G.M. Torrie, and S.G. Whittington. Self-avoiding walks interacting with a surface. J. Phys. A, 15(2):539, 1982.
- [24] Stephen P. Humphries. Generalised cogrowth series, random walks, and the group determinant. Math. Proc. Cambridge Philos. Soc., 165(3):445–465, 2018.
- [25] R. Jungen. Sur les s´eries de taylor n’ayant que des singularit´es alg´ebrico-logarithmiques sur leur cercle der convergence. Comment. Math. Helv., 3:266–306, 1931.
- [26] Harry Kesten. On the number of self-avoiding walks. J. Math. Physics, 4(7):960–969, 07 1963.
- [27] Dmitri Kouksov. On rationality of the cogrowth series. Proc. Amer. Math. Soc., 126(10):2845– 2847, 1998.
- [28] Dmitri Kuksov. Cogrowth series of free products of finite and free groups. Glasg. Math. J., 41(1):19–31, 1999.
- [29] L. Lipshitz. The diagonal of a D-finite power series is D-finite. J. Algebra, 113(2):373–378, 1988.
- [30] Roger Lyndon. Two notes on Rankin’s book on the modular group. J. Aust. Math. Soc., 16(4):454–457, 1973.
- [31] Roger C. Lyndon and Paul E. Schupp. Combinatorial group theory. Springer-Verlag, Berlin,

1977. Ergebnisse der Mathematik und ihrer Grenzgebiete, Band 89.

- [32] David E. Muller and Paul E. Schupp. Groups, the theory of ends, and context-free languages. J. Comput. System Sci., 26:295–310, 1983.
- [33] Igor Pak and David Soukup. Algebraic and arithmetic properties of the cogrowth sequence of nilpotent groups, 2022.
- [34] Andrew Elvey Price and Anthony J. Guttmann. Numerical studies of Thompson’s group F and related groups. Internat. J. Algebra Comput., 29(2):179–243, 2019.
- [35] S.M. Ross. Stochastic Processes. Wiley series in probability and mathematical statistics. Wiley, 1995.
- [36] R. P. Stanley. Differentiably finite power series. European J. Combin, 1(2):175–188, 1980.
- [37] R. P. Stanley. Enumerative combinatorics. Volume 2, volume 62 of Cambridge Stud. Adv. Math. Cambridge Univ. Press, Cambridge, 1999.
- [38] R. P. Stanley. Enumerative combinatorics. Volume 1, volume 49 of Cambridge Stud. Adv. Math. Cambridge Univ. Press, Cambridge, second edition, 2012.
- [39] E J Jance van Rensburg, E Orlandini, D W Sumners, M C Tesi, and S G Whittington. The writhe of a self-avoiding polygon. J. Phys. A, 26(19):L981, Oct 1993.


- [40] Wolfgang Woess. Random Walks on Infinite Graphs and Groups. Cambridge Tracts in Math. Cambridge Univ. Press, 2000.


### A Explicit asymptotics for some examples

In this appendix, we discuss some explicit asymptotic results for small values of our parameters.

- A.1 B3 with trefoil knot presentation Consider the following presentation of the trefoil group


⟨c,d | c3 = d2⟩. (A.1)

Then, using computer algebra systems, we obtain the following.

- Theorem A.1. The generating function F2(z;q) satisfies 0 = z2 − 1 + j1 · F2(z;q) + j2 · F2(z;q)2 + j3 · F2(z;q)3, (A.2)


where

- j1 = 1 − (Q + 3)z2 + Qz3 − Qz4, (A.3a)
- j2 = −1 + (2Q + 8)z2 + Qz3 − (Q2 + 4Q + 7)z4 + (Q + 1)Qz5, (A.3b)
- j3 = −1 + (3Q + 12)z2 + 2Qz3 − (3Q2 + 12Q + 21)z4 + 6(Q + 1)Qz5, (A.3c) Q = q + q−1. (A.3d)


Corollary A.2. The cogrowth of the group ⟨c,d | c3 = d2⟩ is the largest positive zero of the polynomial m4 − 2m3 − 11m2 + 12m + 4. That is

1 + 25 + 16√2

(#trivial words of length n)1/n =

2 ≈ 3.950630994... (A.4) Proof. By Lemma 7.5 we know that the coefficients of the cogrowth series and those of F2(z;1) grow

lim

n−→∞

- at the same exponential rate. So it suffices to examine the asymptotics of F2(z;1). Substituting q = 1 into the equation in Theorem A.1 gives:


(−12z3 + 11z2 + 2z − 1)F2(z;1)2 + (−2z3 + z2 − z)F2(z;1) + 1 − z

× (1 + 2z − 3z2)F2(z;1) + z + 1 = 0. (A.5)

Since we know that F2(z;1) is a power series with non-negative coefficients, we can discard the solution to the linear term and one of the solutions to the quadratic term, leaving

√

F2(z;1) = −2z3 + z2 − z + (2 − z)

1 − 2z − 11z2 + 12z3 + 4z4 2(1 − z)(1 + 3z)(1 − 4z)

. (A.6)

Thus, one expects singularities at 1,−1/3,1/4 and the zeros of 1 − 2z − 11z2 + 12z3 + 4z4. The apparent singularity at z = 1/4 does not occur since the numerator is also zero at z = 1/4. A little computer algebra then shows that the dominant singularity comes from the smallest positive zero of 1 − 2z − 11z2 + 12z3 + 4z4.

| |
|---|


We note here that we were able to find a 7th-order linear differential equation satisfied by the cogrowth series, which is equivalent to a 13th-order recurrence satisfied by its coefficients.

We can go further and use the methods of [12] to compute more detailed asymptotics of the coefficients. In particular, we can establish the asymptotics of [znqαn]F(z;q) for a given constant α; these are sufficient to demonstrate that the cogrowth series is D-finite but not algebraic.

- Theorem A.3. Let x be a real number, then


√n]F2(z;q) =

γ πσn2

[znqα

µne−α2/2σ2 · (1 + o(1)), (A.7)

where µ is the cogrowth, being the largest positive solution of

1 + 25 + 16√2 2

m4 − 2m3 − 11m2 + 12m + 4 = 0 and so µ =

. (A.8)

σ2 is the smallest positive solution of

452s4 − 904s3 + 512s2 − 60s − 1 = 0, (A.9) and the constant γ2 is the largest positive solution of

65536g4 − 41566208g3 + 5469075424g2 + 914873312g + 1442897 = 0. (A.10) Numerically these are

µ ≈ 3.950630994... σ2 ≈ 0.1801879352... γ ≈ 21.16215950.... (A.11)

Hence, the coefficients of the cogrowth series [znq0]F(z;q) scale with an exponent of −2. Consequently, the cogrowth series is not algebraic.

Proof. We follow the arguments used in [12]. First, write the polynomial equation satisfied by F2 as P(F2,z;q) = 0. We can use this to find the dominant singularity, zc, of F2(z;1) and the value of the generating function at that point Fc = F2(zc;1). We can do this from the explicit expression for F2(z;1) (which is given in the proof of Corollary A.2) or as follows.

Let (z,F) = (zc,Fc) be the unique positive solution of the equations P(F,z;1) = 0, PF(F,z;1) = 0, (A.12)

where we have used PF to denote the partial derivative of P with respect to F. We can readily compute these using computer algebra, and find that zc is the smallest positive solution of

4z4 + 12z3 − 11z2 − 2z + 1 = 0, (A.13)

while Fc is the largest zero of

2F4 − 4F3 − 67F2 + 20F + 2 = 0. (A.14) Numerically, these are

zc ≈ 0.2531241216... Fc ≈ 6.744148958... (A.15)

Since Pz(Fc,zc,1) ̸= 0 and PFF(Fc,zc,1) ̸= 0 we can then expand F2(z;q) around (z,q) = (zc,1) as

z ρ(q)

F2(z;q) = α(q) − β(q) 1 −

+ O(z − ρ(q)), (A.16)

where α(q),β(q) are analytic functions around q = 1 and ρ(q) is the radius of convergence. We refer the reader to [12] for the details of this argument. Further, α(q) = F2(ρ(q),q) and

β(q) =

2ρ(q)Pz F2(ρ(q);q)),ρ(q);q PFF F2(ρ(q);q)),ρ(q);q

. (A.17)

- A little computer algebra shows that ρ(q) satisfies a degree 8 polynomial equation (which can be found by computing the discriminant of P(F2;z,q) with respect to F2). Singularity analysis (see [17] Theorem IX.12) then tells us that


β(q) 2√π · ρ(q)−nn−3/2(1 + o(1)). (A.18)

[zn]F2(z;q) =

Saddle point methods then allow us to extract the coefficients of q:

√n]F2(z;q) =

β(1)

σπ√8 · ρ(1)−n · n−2e−α2/2σ2(1 + o(1)), (A.19) where

[znqα

σ2 =

ρ′(1) ρ(1)

2

ρ′′(1) ρ(1) −

−

ρ′(1) ρ(1)

. (A.20)

This can be computed from the polynomial satisfied by ρ(q), and shows that σ2 is the largest positive solution of

452s4 − 904s3 + 512s2 − 60s − 1 = 0. (A.21) Numerically, this gives σ ≈ 0.1801879352.... The constant γ = β(q)/√8 can be computed from zc and Fc. The largest positive solution of

65536g4 − 41566208g3 + 5469075424g2 + 914873312g + 1442897 = 0 (A.22) gives γ2, and numerically γ ≈ 21.16215950.... This scaling form indicates that the coefficients of the cogrowth series scale with a correction of n−2, which is incompatible with the series being algebraic.

| |
|---|


- A.2 B3 with standard presentation Consider the following presentation of the 3-strand braid group B3:


⟨a,b | aba = bab⟩. (A.23)

Then, one has, using computer algebra systems:

- Theorem A.4. The generating function F(z;q) satisfies (8(q + q−1)z3 + 12z2 − 1)F3 + (2z − 1)(2z + 1)F2 + F + 1 = 0. (A.24)


Corollary A.5. The cogrowth of B3 with respect to the generating set {a,a−1,b,b−1} is the largest positive zero of the polynomial m2 − 2m − 7. That is

√

(#trivial words of length n)1/n = 1 + 2

2 ≈ 3.828427124... (A.25)

lim

n−→∞

Proof. We again appeal to Lemma 7.5, which also holds for this group, and the proof is identical. So it is sufficient to study F(z;1). Setting q = 1 into the equation for F in Theorem A.4 gives

(2Fz + F + 1)(8F2z2 + 2F2z − F2 − 2Fz + 1) = 0. (A.26) Of the 3 possible solutions, only one is a positive generating function:

√

1 − 2z − 7z2 (1 − 4z)(1 + 2z)

F(z,1) = −z +

. (A.27)

Standard singularity analysis then shows that the exponential growth rate is determined by the reciprocal of the smallest positive zero of 1 − 2z − 7z2; the apparent singularity at z = 1/4 is not present.

| |
|---|


We note that we were able to find a 6th-order linear differential equation satisfied by the cogrowth series, which is equivalent to a 9th-order recurrence satisfied by its (even) coefficients.

Again, as done earlier, we can also obtain finer details of the asymptotics of the coefficients of F(z;q). This is somewhat complicated by the fact that the coefficients of F display strong oddeven behaviour; in particular, [znqm]F(z;q) is only non-zero when n + m is even.

- Theorem A.6. Let α be a real number, so that m = α√n is an integer, then


√n]F(z;q) =

γ

πσn2 · (1 + (−1)n+m) · µn · e−α2/2σ2 · (1 + o(1)), (A.28) where

[znqα

5 − 3√2 7

√

√

√

2) 10 −

2. (A.29) Numerically these are

µ = 1 + 2

2, σ =

, γ = (6 + 5

µ ≈ 3.828427127... σ ≈ 0.3289288492... γ ≈ 38.30020588.... (A.30)

Hence, the coefficients of the cogrowth series [znq0]F(z;q) scale with an exponent of −2 and consequently the cogrowth series is not algebraic.

The odd-even behaviour of F(z;q) (as reflected in the statement of the theorem) makes the proof a little more complicated than that of Theorem A.3. In particular, we must take into account the contributions of two saddle points.

Proof. We follow the proof of Theorem A.3. Following [12], let P(F,z,q) be the polynomial equation satisfied by F(z;q).Then its discriminant is

DF(z,q) = 27q4 + 58q2 + 27 z4 + 72q q2 + 1 z3 + 44z2q2 − 4q q2 + 1 z − 4q2. (A.31)

Examining the derivative of z with respect to q, we see that there are two relevant saddles, which gives the main complication in this proof. When q = 1 we have an exponential growth of µn, while at q = −1 the growth is (−µ)n. The combination of these terms gives the required odd-even behaviour.

From the saddles at q = ±1 we obtain (recalling that α√n = m ∈ Z)

√n] =

β(1)

σπ√8 · µn · n−2e−α2/2σ2(1 + o(1)), (A.32) [znqα

[znqα

√n] =

β(±1) σπ√8 · (−1)n+mµn · n−2e−α2/2σ2(1 + o(1)), (A.33)

where

√

2 and σ2 =

β(±1) = 4 44 + 25

Adding these contributions gives the stated result.

5 − 3√2 7

. (A.34)

| |
|---|


### B B3 with presentation ⟨a,x | axa = x2⟩

Let ∆ = x3, then the Schreier graph of the group with respect to the presentation ⟨a,x | axa = x2⟩ has the structure shown in Figure 11.

- Figure 11: The Schreier graph of the group ⟨a,x | axa = x2⟩; The coset ⟨∆⟩ is indicated by the black vertex.


###### B.1 Counting returns on the Schreier graph (no q’s)

We start by first counting returns on the Schreier graph without considering the exponent of ∆. Consider the central triangle shown in Figure 12. The vertex corresponding to the coset ⟨∆⟩ is

Figure 12: The central triangle of the Schreier graph.

indicated by the black vertex. We label this vertex 0 and then proceeding clockwise around the face, label the other vertices 1 and 2. Now let

- • F00(z) be the generating function of paths in the graph that start and end at the vertex 0,
- • F01(z) be the generating function of paths in the graph that start at 0 and end at 1, and
- • F02(z) be the generating function of paths in the graph that start at 0 and end at 2.


In order to establish equations satisfied by these generating functions, we consider similar paths, but confined to two of the three main “branches” of the graph. In particular, consider the graph depicted in Figure 13, which shows the central triangular face and two of the three “branches” attached to it.

Let

- • G00(z) be the generating function of paths in this graph that start and end at the vertex 0,


- Figure 13: The graph with one “branch” removed.
- • G01(z) be the generating function of paths in this graph that start at 0 and end at 1, and
- • G02(z) be the generating function of paths in this graph that start at 0 and end at 2.


The generating functions G10 and G20 are defined analogously. We also need to define some “primitive loops”. Let

- • L00(z) be the generating function of walks of positive length that start at 0, never visit 1 or 2 and only return to 0 at their last step. Similarly, define
- • L01(z) be the generating function of walks that start at 0, never return to 0, never visit 2 and only return to 1 at their last step, and
- • L10(z) be the generating function of walks that start at 1, never return to 1, never visit 2 and only return to 0 at their last step.


- Lemma B.1. The Gij generating functions satisfy


and, further,

- G00(z) = 1 + G00(z)L00(z) + G01(z)L10(z) + zG02(z), (B.1)
- G01(z) = G00(z)L01(z) + G01(z) · 2L00(z) + G02(z)L10(z), (B.2)
- G02(z) = zG00(z) + G01(z)L01(z) + G02(z)L00(z), (B.3)


G10(z) = 2L00(z)G10(z) + L10(z)G00(z) + L01(z)G20(z), (B.4) G20(z) = L00(z)G20(z) + L10(z)G10(z) + zG00(z). (B.5)

Proof. The first three equations are obtained by decomposing the corresponding paths at the last time they leave any of the vertices 0,1 or 2. We consider each equation in order.

- • Take any path counted by G00. If it has length 0, then it contributes 1 to the generating function. Otherwise, we can decompose the path by the last time it leaves any of the vertices 0, 1 and 2.

- – If it leaves 0 last, then cutting the path at that point breaks it into a path counted by G00 and another counted by L00. Thus it contributes G00L00.
- – If it leaves 1 last, then it cannot step to the vertex 2. So, so cutting the path at that point breaks the path into one counted by G01 and a primitive loop counted by L10. Hence it contributes G01L10.
- – If it leaves 2 last, then it cannot step to the vertex 1 and so must simply take one step back to the vertex 1. Hence it contributes zG02.


- • Consider a path counted by G01 and cut it at the last time it leaves 0,1 or 2.

- – If it leaves 0 last then the path separates into one counted by G00 and a primitive loop counted by L01.
- – If it leaves 1 last then the path separates into one couned by G01 and a loop counted by L00. However, this loop can either reside in the “branch” attached to the vertices 0,1 or the vertices 1,2. Hence this contributes G01 · 2L00.
- – If it leaves 2 last then the path decomposes into one counted by G02 and a loop counted by L10, giving the G02L10 term.


- • Take any path counted by G02 and decompose it by the last time it leaves 0,1 or 2.


- – If it leaves 0 last, then, since it cannot visit 1, it must simply take a single step to 2. Thus, it contributes zG00.
- – If it leaves 1 last then decomposing it at the last time it leaves 1 we obtain a path counted by G01 and one counted by L01, and so it contributes G01L01.
- – If it leaves 2 last, then cutting the path at that point breaks it into a path counted by G02 and (by symmetry) another counted by L00. Thus, it contributes G02L00.


This gives us the relations that we require.

| |
|---|


We can now express the L generating functions in terms of the Gij generating functions.

- Lemma B.2. The L generating functions satisfy L00(z) = z2G00(z), L01(z) = z + z2G02(z), L10(z) = z + z2G20(z). (B.6)


The last two equations are obtained by considering the first time the corresponding paths return to any of 0,1, or 2. The arguments are then very similar.

Proof. Consider the graph in Figure 14. We consider each equation in turn.

Figure 14: Graph with labelled vertices used to prove the recursive decomposition of paths for the proof of Lemma B.2

.

- • Any path counted by L00 must take at least 2 steps. The first step must go from 0 to 0′ and the last from 0′ to 0. Deleting these steps, one has a walk that starts and ends at 0′ and never visits the vertex 1. These are precisely the walks counted by the generating function G00. This gives L00(z) = z2G00(z) as required.
- • Any path counted by L01 either has length 1 (contributing z) or takes at least 3 steps. The first of these steps must be from 0 to 0′, while the last is from 2′ to 1. Deleting these two steps gives a walk that is counted by G02. Hence L01(z) = z + z2G02(z).


A similar argument gives the equation for L10. We can now express the F generating functions in terms of the L generating functions.

| |
|---|


- Lemma B.3. The F generating functions satisfy


- F00(z) = 1 + F00(z) · 2L00(z) + F01(z)L10(z) + F02(z)L01(z), (B.7)
- F01(z) = F00(z)L01(z) + F01(z) · 2L00(z) + F02(z)L10(z), (B.8)
- F02(z) = F00(z)L10(z) + F01(z)L01(z) + F02(z) · 2L00(z). (B.9)


Proof. As was the case for the Gij-equations, all three equations are obtained by decomposing the corresponding paths at the last time they leave any of the vertices 0,1, or 2. Let us start with the first equation.

Consider a path counted by F00. It either has length 0 or we cut it at the last time it leaves any of the vertices 0,1 or 2.

- • If it leaves 0 last then it separates into a path counted by F00 and a primitive loop. Since this loop cannot visit either 1 or 2, it must be counted by L00. However, the loop can either reside in the “branch” attached to 0 and 1 or the “branch” attached to 0 and 2. Hence, this contributes F00 · 2L00.
- • If the path leaves 1 last then it separates into a path counted by F01, and a primitive loop starting at 1, ending at 0, and never visiting any of 0,1,2 in between. This is precisely a path counted by L10. Hence, these paths contributes F01L10.
- • If the path leaves 2 last, then it decomposes into a path counted by F02 and a loop. The loop starts at 2 and ends at 0 never visiting 0,1,2 in between. These loops are (by symmetry) counted by the generating function L01. Hence, these paths give the term F02L01.


The equations for F01 and F02 follow by very similar arguments.

| |
|---|


These three lemmas define a system of 11 algebraic equations. However, we wish to focus on F00(z). We can use computer algebra to eliminate the other generating functions to obtain a single polynomial equation satisfied by F00(z):

- Theorem B.4. The generating function F00(z) satisfies the following quintic equation


0 = (2z + 1)(z − 1)(3z + 1)(−1 + 4z)2(4z + 1)F00(z)5

+ (−1 + 4z)(16z5 − 28z4 − 50z3 − 5z2 + 6z + 1)F00(z)4

+ (52z4 + 20z3 − 18z2 − 2z + 1)F00(z)3 + (12z4 − 12z3 − 18z2 + 2z + 1)F00(z)2 + z(z − 2)(4z2 + 2z − 1)F00(z)

− z2(2z + 3). (B.10)

Hence, the asymptotics of the number of paths of length n that start and end at the origin are given by

[zn]F00(z) = A · µnn−3/2 (1 + o(1)). (B.11) where µ ≈ 3.9076667... is the largest positive real solution of

0 = 4z11 + 24z10 − 88z9 − 763z8 − 130z7 + 6598z6 + 9136z5

− 8940z4 − 12888z3 + 7788z2 + 1192z − 108. (B.12) Proof. By symmetry:

G10 = G01, G20 = G02, L10 = L01, F02 = F01. (B.13)

So our original system is reduced to a system of 7 equations in 7 unknown functions. One can then use computer algebra to eliminate G00,G01,G02,L00,L01 and F01, leaving the above single equation in F00(z). Standard methods of analytic combinatorics then yield the asymptotic form given.

| |
|---|


###### B.2 Return to the Schreier graph

We proceed in much the same manner as for the groups above. We now consider the graph as a Schreier graph and must keep track of the exponent of ∆ in the normal forms of the associated group elements. Notice that since ∆ commutes with both generators, we are free to move the power of ∆ to the extreme right of any normal form. We do that here.

Consider the central triangle again as shown in Figure 15.

Figure 15: The central triangle of the Schreier graph with the cosets ⟨∆⟩, x⟨∆⟩, and x2⟨∆⟩.

The vertices labelled e,x,x2 correspond to the cosets ⟨∆⟩, x⟨∆⟩, and x2⟨∆⟩. Now we extend the generating functions used above to include information about ∆. As before, z counts the length and q counts the exponent of ∆ in the corresponding normal form. Let

- • F00(z,q) be the generating function of paths that start at the identity and end at ⟨∆⟩,
- • F01(z,q) be the generating function of paths that start at the identity and end at x⟨∆⟩, and
- • F02(z,q) be the generating function of paths that start at the identity and end at x2⟨∆⟩.


We define the extended Gij and L generating functions in a similar manner. A little care is needed for L10(z,q), G10(z,q), and G20(z,q). Let

- • L10(z) be the generating function of walks of positive length that start at x, never visit 1 or 2, and only return to the coset ⟨∆⟩ at their last step. Then let
- • G10(z) be the generating function of walks on the Schreier graph, corresponding to the graph in Figure 13, that start at x and end at the coset ⟨∆⟩. Finally, let
- • G20(z) be the generating function of walks on the Schreier graph, corresponding to the graph in Figure 13, that start at x2 and end at the coset ⟨∆⟩.


The extended generating functions satisfy very similar equations, which are obtained by very similar arguments.

- Lemma B.5. The extended Gij generating functions satisfy


- G00(z,q) = 1 + G00(z,q)L00(z,q) + G01(z,q)L10(z,q) + zqG02(z,q), (B.14)
- G01(z,q) = G00(z,q)L01(z,q) + G01(z,q) · 2L00(z,q) + G02(z,q)L10(z,q), (B.15)
- G02(z,q) = zq−1G00(z,q) + G01(z,q)L01(z,q) + G02(z,q)L00(z,q), (B.16)


and further,

G10(z,q) = 2L00(z,q)G10(z,q) + L10(z,q)G00(z,q) + L01(z,q)G20(z,q), (B.17) G20(z,q) = L00(z,q)G20(z,q) + L10(z,q)G10(z,q) + zqG00(z,q). (B.18)

Proof. We use the same constructions as previously. The equations for G01(z,q) and G10(z,q) follow by very similar arguments. Those for the other three G’s also follow very similarly. However, more care is needed to account for changes in the exponent of ∆.

Consider any path counted by G00 and the last time that path leaves any of the cosets ⟨∆⟩, x⟨∆⟩, or x2⟨∆⟩.

- • If it last leaves from ⟨∆⟩, then the path decomposes into a path from the identity to ⟨∆⟩, and then a primitive loop starting and ending at ⟨∆⟩. This gives G00L00.
- • If it last leaves from x⟨∆⟩, then the path decomposes into a path from the identity to x⟨∆⟩, and then a primitive loop starting at x⟨∆⟩ and ending at ⟨∆⟩. This gives G01L10.
- • If it last leaves from x2⟨∆⟩, then the path decomposes into a path from the identity to x2⟨∆⟩, and then it must take a single step from x2⟨∆⟩ to ⟨∆⟩. This single step must be an x and hence increases the exponent of ∆ by 1.


Now consider any path counted by G02 and the last time that path leaves any of the cosets ⟨∆⟩, x⟨∆⟩, or x2⟨∆⟩.

- • If it last leaves from ⟨∆⟩, then the path decomposes into a path from x2 to ⟨∆⟩, and then it must take a single step from ⟨∆⟩ to x2⟨∆⟩. This single step must be an x−1 and hence decreases the exponent of ∆ by 1, since ∆kx−1 = x2∆k−1.
- • If it last leaves from x⟨∆⟩ then the path decomposes into a path from the identity to x⟨∆⟩, and then a primitive loop starting at x⟨∆⟩ and ending at x2⟨∆⟩. This gives G01L01.
- • If it last leaves from x2⟨∆⟩, then the path decomposes into a path from the identity to ⟨∆⟩, and then a primitive loop starting and ending at x2⟨∆⟩. This gives G02L00.


Finally, take any path counted by G20 and examine the first time that path returns to any of the cosets ⟨∆⟩, x⟨∆⟩, or x2⟨∆⟩.

- • If it first returns to x2⟨∆⟩, then the path decomposes into a primitive loop from x2 to x2⟨∆⟩, and a path that starts at x2⟨∆⟩ and ends at ⟨∆⟩. Hence, this contributes L00G20.
- • If it first returns to x⟨∆⟩, then it decomposes into a primitive loop from x2 to x⟨∆⟩, and a path from x⟨∆⟩ to ⟨∆⟩. The first of these is counted by L10, while the second is counted by G10; hence, they contribute L10G10.
- • Finally, if it first returns to ⟨∆⟩, then it must consist of a single step from x2 to ⟨∆⟩. This step must be an x, and so the exponent of ∆ increases by 1. This gives the term zqG00.


These give us the required generating function relations. Similar arguments allow us to find relations and symmetries within all of these generating functions, which we summarise in the following lemma. We state it without proof.

| |
|---|


- Lemma B.6. The extended L generating functions satisfy L00(z,q) = z2G00(z,q), L01(z,q) = z + z2G02(z,q), L10(z,q) = z + z2G20(z,q). (B.19)


while the extended F generating functions satisfy

F00(z,q) = 1 + F00(z,q) · 2L00(z,q) + F01(z,q)L10(z,q) + qF02(z,q)L01(z,q), (B.20) F01(z,q) = F00(z,q)L01(z,q) + F01(z,q) · 2L00(z,q) + F02(z,q)L10(z,q), (B.21) F02(z,q) = q−1F00(z,q)L10(z,q) + F01(z,q)L01(z,q) + F02(z,q) · 2L00(z,q). (B.22)

Further, the following symmetries hold

G10(z,q) = G01(z,q−1), G20(z,q) = G02(z,q−1), (B.23) L10(z,q) = L01(z,q−1), F02(z,q) = qF01(z,q−1). (B.24)

Unfortunately, we have not been able to reduce the above system of equations down to a single equation for F00(z,q). We are able to find degree 11 polynomial equations for L00(z;q),L01(z,q), and L10(z,q) and can express F00(z;q) as a simple rational function of these L’s. The computer algebra systems we tried were unable to reduce those equations to a polynomial for F00(z,q); the computation did not terminate after any reasonable time.

Note that by fixing the value of q at small integers n = −1,1,2,3,... we were able to guess algebraic equations for F00(z,n). When n = 1, we recover Equation (B.10) and when n = −1, we find a cubic(!). For other integer values of n we find polynomials of degree 11 whose coefficients are polynomials in z of degree up to 28. In principle, it would be possible to determine the q-dependence of these coefficients by guessing at many values of n, but we have not done this.

- Theorem B.7. The generating function F00(z,q) satisfies an algebraic equation. Hence, the cogrowth series for B3 with respect to the generating set {a,x}, being [q0]F00(z,q), is a D-finite generating function.


Proof. Though we have been unable to find an explicit algebraic equation for F00(z,q), we know that one must exist from the system of equations above. Hence, F00(z,q) is also D-finite and so its constant term with respect to q is also D-finite [29].

| |
|---|


