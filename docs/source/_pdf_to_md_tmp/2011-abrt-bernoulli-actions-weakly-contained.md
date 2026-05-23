arXiv:1103.1063v2[math.DS]27Sep2011

Bernoulli actions are weakly contained in any free action

Mikl´os Ab´ert and Benjamin Weiss November 26, 2024

Abstract

Let Γ be a countable group and let f be a free probability measure preserving action of Γ. We show that all Bernoulli actions of Γ are weakly contained in f.

It follows that for a ﬁnitely generated group Γ, the cost is maximal on Bernoulli actions for Γ and that all free factors of i.i.d. of Γ have the same cost.

We also show that if f is ergodic, but not strongly ergodic, then f is weakly equivalent to f × I where I denotes the trivial action of Γ on the unit interval. This leads to a relative version of the Glasner-Weiss dichotomy.

# 1 Introduction

Let Γ be a countable group. By a probability measure preserving (p.m.p.) action f of Γ we mean a representation of γ ∈ Γ by fγ in the group of measure preserving transformations of (X,B,µ). Here (X,B,µ) is a standard Borel probability space. The action f is free, if for µ-almost every x ∈ X and γ = γ′ ∈ Γ we have fγ(x) = fγ′(x).

Let f and g be p.m.p. actions of Γ on (X,B,µ) and (Y,C,ν), respectively. Following the deﬁnition of Kechris [7], we say that f weakly contains g (f g) if for all Borel subsets Y1,...,Yn ∈ C, ﬁnite sets S ⊆ Γ and ε > 0 there exist Borel subsets X1,...,Xn ∈ B such that

|µ(fγXi ∩ Xj) − ν(gγYi ∩ Yj)| < ε (1 ≤ i,j ≤ n,γ ∈ S).

In particular, the way g acts on ﬁnite partitions of the underlying space can be simulated by f with arbitrarily small error. A special case of weak containment is when g is a factor of f, that is, there exists a surjective measure preserving Γ-equivariant map from (X,B,µ) to (Y,C,ν). We call f and g weakly equivalent if f g and g f.

Let κ be a probability space. The Bernoulli action κΓ is deﬁned as the set of maps from Γ to κ, endowed with the product measure and the shift action by Γ. These actions are also called i.i.d. processes on Γ.

The main result of this paper is the following:

Theorem 1 Let Γ be a countable inﬁnite group and let f be a free p.m.p. action of Γ. Then f weakly contains every Bernoulli action of Γ. In particular, all free factors of i.i.d.-s of Γ are weakly equivalent.

Note that one can obtain the original Rokhlin lemma for Z as a quick corollary of Theorem 1. In this language, the lemma says that every free action of Z weakly contains the cyclic action of Z on n points for all n > 0. Since weak containment is transitive, by Theorem 1, it is enough to prove this for {0,1}Z with p(0) = p(1) = 1/2. For a natural number k, 0 ≤ l ≤ n − 1 and ω ∈ {0,1}Z let

k−1

ω(in + l)

ω k,l =

i=0

and let

Ak = ω ∈ {0,1}Z | ω k,0 > ω k,l + n for all 1 ≤ l ≤ n − 1 .

Let T denote the shift operator on {0,1}Z. Then the sets Ak,TAk,...,Tn−1Ak are disjoint, while the measure of Ak converges to 1/n as k tends to inﬁnity, since for a ﬁxed k, the ω k,l are independent binomial variables.

As a corollary of Theorem 1, one gets a new result on cost. The cost is a numeric invariant of a p.m.p. action of a countable group. Its study was initiated by G. Levitt [8] and has been investigated in depth by D. Gaboriau [3]. One of the major open problems here is the Fixed Price problem, that is, whether every free action of a countable group has the same cost. A. Kechris showed that for ﬁnitely generated groups and free actions, the cost is monotonic with respect to weak containment [7, Corollary 10.14], so Theorem 1 leads to the following.

Corollary 2 Let Γ be a ﬁnitely generated group. Then, among free p.m.p. actions of Γ, the cost is maximal on free factors of i.i.d.-s. In particular, all free factors of i.i.d.-s have the same cost.

Since the cost of any free action of an inﬁnite group is at least 1, we get that an inﬁnite group Γ has ﬁxed price 1 if and only if one of its Bernoulli actions have cost 1. We will generalize the monotonicity result of A. Kechris to actions that are not necessarily free, but for that we need to use an extension of the notion of cost called the groupoid cost. For details see Section 3.

In the language of weak containment, one can express the well-known notion of strong ergodicity as follows. An action of Γ is strongly ergodic, if it is ergodic and it does not weakly contain the identity action of Γ on two points with equal mass.

In the presence of ergodicity, the absence of strong ergodicity forces various structural restrictions on the action. An example of this is the theorem of V. Jones and K. Schmidt [6] that says that the equivalence relation deﬁned by such

an action factors onto a nontrivial hyperﬁnite equivalence relation. We will give another kind of restriction in the language of weak containment.

For a measure preserving action f on (X,B,µ) let f ×I denote the diagonal action of Γ on (X,B,µ) × [0,1] where Γ acts on the second coordinate trivially.

- Theorem 3 Let f be an ergodic p.m.p. action of a countable group. Then the following are equivalent:

- 1) f is not strongly ergodic;
- 2) f is weakly equivalent to f × I.


This leads to the following convexity result, that can be viewed as a ‘relative Glasner-Weiss theorem’.

For a compact topological space K let KΓ denote the shift of Γ with base set K. This is a continuous action on a compact space. Let M(Γ,K) denote the set of Γ-invariant Borel measures on KΓ, endowed with the weak* topology and let E(Γ,K) ⊆ M(Γ,K) denote the set of ergodic measures. It is a standard fact that M(Γ,K) is a simplex where the set of extreme points equals E(Γ,K).

For an ergodic p.m.p. action f on (X,B,µ) any Borel map φ : X → K deﬁnes a Γ-equivariant map Φ : X → KΓ by setting, for x ∈ X and γ ∈ Γ

Φ(x)(γ) = φ(fγ(x)). (1) The measure Φ ◦ µ is an invariant measure on KΓ.

Let

E(f,K) = {Φ ◦ µ | φ a Borel map from X to K}.

One can also describe E(f,K) as the set of invariant measures on KΓ that are factors of f. We have the following dichotomy, that can be viewed as a ‘relative Glasner-Weiss theorem’.

- Theorem 4 Let f be an ergodic p.m.p. action of the countable group Γ. If f is strongly ergodic, then E(f,K) ⊆ E(Γ,K). If f is not strongly ergodic, then E(f,K) is convex.


![image 1](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile1.png>)

![image 2](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile2.png>)

The Glasner-Weiss theorem [5] says that when Γ has property (T), then E(Γ,K) is closed, and when it does not have property (T), then E(Γ,K) = M(Γ,K). We can deduce this result from Theorem 4 as follows. By the GlasnerThouvenot-Weiss theorem [4], for every countable group Γ there exists an ergodic p.m.p. action f of Γ that weakly contains all ergodic actions of Γ. This means that E(Γ,K) ⊆ E(f,K).

![image 3](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile3.png>)

![image 4](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile4.png>)

If Γ has property (T), then by K. Schmidt [10], every ergodic action of Γ is strongly ergodic, in particular, f is strongly ergodic. So by Theorem 4 E(f,K) = E(Γ,K) and hence E(Γ,K) is closed.

![image 5](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile5.png>)

If Γ does not have property (T), then by the Connes-Weiss theorem, Γ has an ergodic action that is not strongly ergodic. But that action is weakly contained in f, so f is also not strongly ergodic. So by Theorem 4, E(f,K) is convex and since it contains all of E(Γ,K), it must equal M(Γ,K), the convex hull of E(Γ,K).

![image 6](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile6.png>)

The paper is organized as follows. In Section 2 we prove Theorem 1. In Section 3 we deﬁne the groupoid cost and show that for ﬁnitely generated groups, it is monotonic with respect to weak containment. Finally, in Section 4 we prove Theorem 3 and Theorem 4.

Acknowledgement. The authors thank the Glasner family (Eli and Yair) for establishing a link between them, that led to this paper.

# 2 Weak containment of i.i.d. actions

In this section we prove Theorem 1. Throughout the paper, when it is convenient, we will assume that the p.m.p. action is continuous on a compact metric space. This can be easily seen by taking a Borel bijection φ between X and the Cantor set K and then considering the shift action on KΓ with the invariant measure Φ ◦ µ.

For positive numbers p1,...,pd with

d

pi = 1

i=1

let κ(p1,...,pd) denote the probability space on {1,...,d} where P(i) = pi. For any T ⊆ Γ there is a natural projection πT from {1,...,d}Γ to {1,...,d}T.

The sets of the form πT−1(D) with D ⊆ {1,...,d}T are called the cylinder sets with respect to T.

- Lemma 5 Let f be a p.m.p. action of the countable group Γ on (X,B,µ). Then f weakly contains κ(p1,...,pd)Γ if for all ﬁnite subsets F of Γ and δ > 0 there exists a Borel map φ : X → {1,...,d} such that for all α ∈ {1,...,d}F


µ({x ∈ X | φ(fγx) = α(γ) for all γ ∈ F}) −

pα(γ) < δ.

γ∈F

Proof. Assume that the condition holds. Let g denote the shift action of Γ on κ(p1,...,pd)Γ and let λ denote the measure on κ(p1,...,pd)Γ.

Let Y1,...,Yn ⊆ {1,...,d}Γ be Borel subsets, let S ⊆ Γ be a ﬁnite symmetric set containing the identity and let ε > 0.

Then for any r > 0, there exists a ﬁnite subset T of Γ, and subsets Di ⊆ {1,...,d}T such that for all 1 ≤ i ≤ n we have

λ(Yi △ πT−1(Di)) < r.

Here △ denotes symmetric diﬀerence. We now apply the condition of the lemma for F = TS and a δ > 0 to be chosen later.

For 1 ≤ i ≤ n let

Xi = Φ−1(πT−1(Di))

where Φ is the map deﬁned by 1) in the Introduction. Then for suﬃciently small r and δ it follows that

|µ(fγXi ∩ Xj) − λ(gγYi ∩ Yj)| < ε (1 ≤ i,j ≤ n,γ ∈ S). The lemma is proved.

- Lemma 6 Let f be a free p.m.p. action of the countable group Γ on the compact metric space (X,d,µ). Then for any ﬁnite symmetric subset F of Γ and any ε > 0 there exists s > 0 such that


µ({x ∈ X | d(fγx,fγ′x) > s for all γ = γ′ ∈ F}) > 1 − ε (*) and

µ × µ({(x,x′) ∈ X × X | d(fγx,fγ′x′) > s for all γ,γ′ ∈ F}) > 1 − ε (**)

In other terms, for this s, most of the F-neighbourhoods of pairs of points in X are s-apart. We leave the details to the reader.

We are ready to prove Theorem 1.

Proof of Theorem 1. We will verify that the conditions of Lemma 5 hold. Let F be a ﬁnite subset of Γ and let δ > 0. Let ε > 0 be determined later. Use Lemma 6 with this ε to ﬁnd s that satisﬁes the conclusions of the lemma. Let {Bj | 1 ≤ j ≤ J} be a Borel partition of X into sets of diameter less than s. Let U1,...,UJ be independent random variables with distribution κ(p1,...,pd). Deﬁne a random map φ : X → {1,...,d} by setting

φ(x) = Uj when x ∈ Bj.

We shall show that with high probability, this map will satisfy the conditions of Lemma 5. In particular, this will imply the existence of such a map.

We shall use the so-called second moment method. For α ∈ {1,...,d}F let

Gα = {x ∈ X | φ(fγx) = α(γ) for all γ ∈ F} . Now µ(Gα) is a random variable with expected value given by

Eµ(Gα) = E

X

1G

α

(x)dµ(x) =

X

E1G

α

(x)dµ(x).

For x ∈ X such that the F-neighbourhood of x is s-apart (that is, the set deﬁned in (*) of Lemma 6) the expected value E1G

(x) =

pα(γ) because the φ-values at the neighbours are independent. It follows that

α

γ∈F

Eµ(Gα) −

pα(γ) < 2ε.

γ∈F

We shall now estimate the variance of µ(Gα). We have

Eµ2(Gα) = E

X

= E

X X

1G

α

(x)dµ(x)

X

1G

α

(x′)dµ(x′) =

1G

α

(x)1G

α

(x′)d(µ × µ)(x,x′) =

=

E(1G

α

(x)1G

α

(x′))d(µ × µ)(x,x′)

X X

For x,x′ ∈ X such that the F-neighbourhoods of x and x′ are s-apart (that is, when both x, x′ satisfy (*) and (x,x′) satisﬁes (**) of Lemma 6) then

 

 

2

(x′) =

(x)1G

E1G

pα(γ)

α

α

γ∈F

because the φ-values at the neighbours are independent. The µ × µ-measure of these pairs of points is at least 1 − 3ε. It follows that

Var(µ(Gα)) = Eµ2(Gα) − (Eµ(Gα))2 < 12ε. Now Chebyshev’s inequality says that the probability

Var(µ(Gα)) c2 Setting c = ε1/3 we get

P(|µ(Gα) − Eµ(Gα)| > c) ≤

![image 7](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile7.png>)

P(|µ(Gα) − Eµ(Gα)| > ε1/3) ≤ 12ε1/3

Setting ε small enough, we get that |µ(Gα) − Eµ(Gα)| is arbitrarily small for all α ∈ {1,...,d}F simultaneously. Hence the conditions of Lemma 5 hold and f weakly contains κ(p1,...,pd)Γ for any ﬁnite distribution κ(p1,...,pd).

Since any probability distribution can be approximated by ﬁnite distributions, we get that f weakly contains all Bernoulli actions and the theorem has been established.

# 3 Groupoid cost and weak containment

In this section we will introduce the groupoid cost of a p.m.p. action and show that for ﬁnitely generated groups, it is monotonic with respect to weak containment. Groupoid cost has been introduced in [1] as an extension of cost for non-free p.m.p. actions. The monotonicity result was proved by A. Kechris [7, Corollary 10.14] for the original cost and free actions.

Let f be a p.m.p. action of the countable group Γ on (X,B,µ). Without loss of generality, we can assume that the space X is compact. Endow Γ with

the discrete topology and the counting measure. Consider X × Γ, endowed with the product Borel structure and the product measure µ. We deﬁne a partial product on X ×Γ as follows. The product of (x1,γ1) and (x2,γ2) is only deﬁned, when fγ

x1 = x2; in this case let (x1,γ1) · (x2,γ2) = (x1,γ1γ2). The inverse of (x,γ) is deﬁned as (fγx,γ−1) and is denoted by (x,γ)−1, so we have (x,γ) · (x,γ)−1 = (x,e). Then X × Γ forms a groupoid with respect to this partial product.

1

Now we deﬁne the subset groupoid Gf as follows. Elements of Gf are Borel subsets of X × Γ. For A,B ∈ Gf let

A · B = {a · b | a ∈ A, b ∈ B when a · b is deﬁned}.

Let E = X × {e} where e is the identity element of Γ. Then for all A ∈ Gf we have AE = EA = A. When f is a continuous action on a compact space, the partial product is continuous as well, which in particular implies that the product of open elements of Gf is open and the product of compact elements is compact.

We say that A ∈ Gf generates the action f, if ∞

A ∪ A−1 ∪ E n = X × Γ.

n=1

In particular, for any generating set S of Γ, XS = X ×S generates f. Note that this is a topological condition and is independent of the measure.

The groupoid cost of f is deﬁned as gcost(f) = inf

µ(A).

A generates f

When f is a free action, X × Γ can be identiﬁed with the equivalence relation generated by f on X, elements of Gf are graphings in this relation and A ∈ Gf generates f if and only if the correspoding graphing generates the equivalence relation. Hence, for free actions, gcost(f) = cost(f) and so the groupoid cost is indeed an extension of cost to non-free actions. Note that the original notion of cost required that the graphing generates the relation only up to a nullset, but it is easy to see that without loss of generality, one can assume full generation.

Trivially, for every generator A ∈ Gf and ε > 0 there exists an open generator B ∈ Gf such that A ⊆ B and µ(B) ≤ µ(A) + ε. So, in the deﬁnition of gcost, it is enough to consider open generators. The following lemma is essentially contained in [1].

- Lemma 7 Assume that X is compact, totally disconnected and Γ is ﬁnitely generated. Then


gcost(f) = inf µ(A) where A varies over compact, clopen generators for f.

Proof. Let Γ be generated by the ﬁnite set S. Let C be a countable clopen basis for the topology of X. List the elements of C as C1,C2,... For an open set O ∈ B and n > 0 let

Ci.

On =

1≤i≤n Ci⊆O

Let A ∈ Gf be an open generating element for Gf with µ(A) < ∞. Then A = ∪γ∈ΓA(γ) × {γ} where A(γ)× {γ} = A ∩(X × {γ}) and A(γ) is open. For n > 0 let An = ∪γ∈ΓA(γ)n × {γ}. Then An is compact (since µ(A) < ∞) and clopen. Let Bn = An ∪ A−n1 ∪ E. Then

∞

Bnn = X × Γ

n=1

since every possible ﬁnite product in A ∪ A−1 ∪ E is realized in Bn for large enough n. In particular,

∞

(Bnn ∩ XS) = XS

n=1

but since Bnn ∩ XS is open and XS is compact, there exists an n > 0 with XS ⊆ Bnn. Since XS generates f, we get that already An generates f.

It follows that any open generator for f with ﬁnite measure contains a compact, clopen generator. The lemma is proved.

For the convenience of the reader, we now recall some deﬁnitions from the Introduction. For a compact topological space K let KΓ denote the shift of Γ with base set K. This is a continuous action on a compact space. Let M(Γ,K) denote the set of Γ-invariant Borel measures on KΓ, endowed with the weak* topology and let E(Γ,K) ⊆ M(Γ,K) denote the set of ergodic measures.

For an ergodic p.m.p. action f on (X,B,µ) any Borel map φ : X → K deﬁnes a Γ-equivariant map Φ : X → KΓ by setting, for x ∈ X and γ ∈ Γ

Φ(x)(γ) = φ(fγ(x)). The measure Φ ◦ µ is an invariant measure on KΓ. Let

E(f,K) = {Φ ◦ µ | φ a Borel map from X to K}.

One can also describe E(f,K) as the set of invariant measures on KΓ that are factors of f.

- Lemma 8 Let f and g be p.m.p. actions of the countable group Γ on (X,B,µ) and (Y,C,ν), respectively. Then f weakly contains g if and only if


![image 8](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile8.png>)

E(f,K) ⊇ E(g,K) (*)

for any compact topological space K. The same result holds if we only consider the class of ﬁnite spaces.

Proof. The (*) condition for all ﬁnite spaces K is easily seen to be equivalent with the original deﬁnition of weak containment.

If L is a ﬁnite subset of K, then LΓ is contained in KΓ. The invariant measures concentrated on LΓ as L varies over the ﬁnite subsets of K, are dense in M(Γ,K).

Moreover, it follows that

![image 9](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile9.png>)

E(g,L) ⊇ E(g,K).

L⊆K ﬁnite

This is because

E(g,K) = {Φ ◦ ν | φ a Borel map from Y to K}.

and the Borel map φ can be well approximated by maps φn with ﬁnite range Ln in such a way that Φn ◦ ν converges to Φ ◦ ν. This yields

![image 10](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile10.png>)

![image 11](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile11.png>)

![image 12](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile12.png>)

E(g,K) ⊆

E(f,L) ⊆ E(f,K).

E(g,L) ⊆

L⊆K ﬁnite

L⊆K ﬁnite

The lemma is proved.

Theorem 9 Let f and g be p.m.p. actions of the ﬁnitely generated group Γ on (X,B,µ) and (Y,C,ν), respectively, such that f weakly contains g. Then gcost(f) ≤ gcost(g).

Proof. Let K be the standard Cantor set. Let φ be a Borel isomorphism from Y to K. Then the shift action on KΓ with the invariant measure ν′ = Φ ◦ ν is isomorphic to g. Let h be the shift action of Γ on KΓ with the invariant measure ν′. Clearly, gcost(h) = gcost(g). Using Lemma 7, for any ε > 0 there exists a clopen, compact A ∈ Gh that generates h and ν′(A) < gcost(h) + ε. Since weak convergence of probability measures ρn on KΓ implies convergence of ρn on clopen compact subsets of KΓ × Γ, using Lemma 8 there exists a map ψ : X → K such that

Ψ ◦ µ(A) ≤ ν′(A) + ε.

The condition of generating is independent of the invariant measure, so A generates the shift action on KΓ with the invariant measure Ψ ◦ µ as well. This action is a factor of f, and hence its gcost is an upper bound for the gcost of f. This implies

gcost(f) ≤ Ψ ◦ µ(A) ≤ ν′(A) + ε < gcost(g) + 2ε. The theorem holds.

Proof of Corollary 2. Let Γ be a ﬁnitely generated group and let f be a free p.m.p. action of Γ. Then, using Theorem 1, f weakly contains all Bernoulli actions, so by Theorem 9 the gcost of f is at most the gcost of any Bernoulli

action of Γ, in particular, the cost of f is at most the cost of any free Bernoulli action of Γ.

Note that any nontrivial Bernoulli action of an inﬁnite group is free. Also, it is easy to see that when Γ is torsion free, then every nontrivial factor of i.i.d. is free. However, in the presence of torsion, this last statement fails to hold.

# 4 Ergodic actions and convexity

Let f be a p.m.p. action of the countable group Γ on (X,B,µ). A sequence of subsets An ∈ B is almost invariant, if

lim

µ(fγAn △ An) = 0 for all γ ∈ Γ.

n→∞

The sequence is trivial, if limn→∞ µ(An)(1−µ(An)) = 0. We say that the action f is strongly ergodic, if every almost invariant sequence is trivial.

The following lemma is due to K. Schmidt [9].

- Lemma 10 (Schmidt) Let f be a p.m.p. action of the countable group Γ on (X,B,µ), such that f is ergodic, but not strongly ergodic. Then for all 0 < λ < 1 there exists an almost invariant sequence An such that µ(An) = λ (n ≥ 0).

In particular, the action is strongly ergodic if and only if it is ergodic and does not weakly contain the identity action of Γ on two points with equal mass.

The following lemma forms a part of the proof of Schmidt’s lemma. For completeness, we provide a short proof.

- Lemma 11 Let f be an ergodic p.m.p. action of the countable group Γ on


the compact space (X,B,µ), let 0 < λ < 1 and let An be an almost invariant sequence such that

µ(An) = λ. Let µn be the measure on X deﬁned by

lim

n→∞

µn(Y ) = µ(An ∩ Y ) (Y ∈ B). Then µn weak* converges to λµ. Proof. Let nk be a sequence such that µn

is weakly convergent and let ν be the limit measure. Then ν is invariant under Γ and is bounded by µ/λ, so by ergodicity, ν is a scalar multiple of µ. But ν(X) = limµ(An) = λ which proves the lemma.

k

- Proof of Theorem 3. Let f be an ergodic p.m.p. action of the countable group Γ on (X,B,µ).


Assume that f is weakly equivalent to f × I. Since f × I factors on the identity action b of Γ on two points with equal mass, this means that f weakly

contains b. Hence f can not be strongly ergodic.

Now assume f is not strongly ergodic. We claim that f weakly contains f×b. We can assume that the space (X,B,µ) is totally disconnected and compact and Γ acts by continuous maps. Let C denote the set of clopen sets in B. Then C is a ﬁnitely additive algebra and for any B ∈ B and ε > 0 there exists C ∈ C with µ(B △ C) < ε.

Hence, it is enough to check the weak containment condition for clopen subsets. In addition, by Schmidt’s lemma, there exists an almost invariant sequence An ∈ C with

µ(An) = 1/2. Lemma 11 implies that for every clopen set C ∈ C, we have lim

lim

n→∞

µ(C ∩ An) = µ(C)/2. Indeed, weak* convergence of measures implies convergence on clopen sets.

n→∞

Let Y1′,...,Yk′,Y1′′,...,Yk′′ ∈ C, let S ⊆ Γ be a ﬁnite subset and let ε > 0. Then by the almost invariance of An, for all γ ∈ S we have

µ(fγAn △ An) = 0 Also for all 1 ≤ i,j ≤ k and γ ∈ S we have

lim

n→∞

µ(An ∩ fγYi′ ∩ Yj′) − µ(fγYi′ ∩ Yj′)/2 = 0 and

lim

n→∞

µ(An ∩ fγYi′′ ∩ Yj′′) − µ(fγYi′′ ∩ Yj′′)/2 = 0

lim

n→∞

Let n be large enough such that all the above quantities (listed in the above three displays) are less than ε. Now for 1 ≤ i ≤ k let

Xi = (An ∩ Yi′) ∪ (Acn ∩ Yi′′) where Acn denotes the complement of An.

Now let Y1,...,Yk be Borel subsets of X × {0,1}. Let

Yi′ × {0} = Yi ∩ (X × {0}) and let

Yi′′ × {1} = Yi ∩ (X × {1}).

Applying the above argument for Yi′ and Yi′′ we obtain the desired measurable subsets X1,...,Xn. The claim holds and f weakly contains f × b.

Iterating the argument, we get that f weakly contains f×b2n where b2n is the trivial action of Γ on {1,...,2n} with uniform measure. An easy approximation argument yields that f weakly contains f × I. Since f is a factor of f × I, we get that f is weakly equivalent to f × I.

The theorem is proved.

- Proof of Theorem 4. Let f be an ergodic p.m.p. action of the countable group Γ.


Assume that f is strongly ergodic. Assume by contradiction that there exists a sequence of Borel maps φn : X → K such that Φn◦µ weak* converges to a nonergodic measure λ on KΓ. Let A be a Γ-invariant Borel set with 0 < λ(A) < 1. Let us approximate A with a clopen sequence An with respect to λ. It is easy to see that An is almost invariant with respect to λ. Then there exists k(n) such that Φ−k(1n)(An) gives us a nontrivial almost invariant sequence for f, a contradiction. Hence E(f,K) ⊆ E(Γ,K).

![image 13](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile13.png>)

Assume that f is not strongly ergodic. Let µ′ be the product measure µ × {1/2,1/2}. Let φ0,φ1 : X → K be Borel maps and let φ : X × {0,1} → K be deﬁned by

φ((x,i)) = φi(x) for i = 0,1. Then by Theorem 3, f weakly contains f × b, so by Lemma 4, Φ ◦ µ′ is in E(f,K). But

![image 14](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile14.png>)

- 1

![image 15](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile15.png>)

- 2


- 1

![image 16](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile16.png>)

- 2


Φ ◦ µ′ =

Φ0 ◦ µ +

Φ1 ◦ µ.

![image 17](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile17.png>)

![image 18](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile18.png>)

This gives that for λ,λ′ ∈ E(f,K), 21λ + 21λ′ ∈ E(f,K). Hence E(f,K) is convex.

![image 19](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile19.png>)

![image 20](<2011-abrt-bernoulli-actions-weakly-contained_images/imageFile20.png>)

The theorem holds.

# References

- [1] M. Ab´ert and N. Nikolov, Rank gradient, cost of groups and the rank versus Heegard genus problem, to appear in J. of the EMS
- [2] A. Connes and B. Weiss, Property T and asymptotically invariant sequences, Israel Journal of Math. 37 1980 209–210.
- [3] D. Gaboriau, Coˆut des relations d’´equivalence et des groupes. (French) [Cost of equivalence relations and of groups] Invent. Math. 139 (2000), no. 1, 41–98.
- [4] E. Glasner, J.-P. Thouvenot and B. Weiss, Every countable group has the weak Rohlin property, Bull. London Math. Soc. 38, 2006, 932–936.
- [5] E. Glasner and B. Weiss, Kazhdan’s property T and the geometry of the collection of invariant measures, Geom. Funct. Anal. 7 (1997), no. 5, 917–935.
- [6] V. Jones and K. Schmidt, Asymptotically invariant sequences and approximate ﬁniteness, Am. J. of Math. 109 (1987) 91-114.
- [7] A. Kechris, Global aspects of ergodic group actions, to appear in the series ”Mathematical Surveys and Monographs” of the AMS


- [8] G. Levitt, On the cost of generating an equivalence relation, Ergodic Theory Dynam. Systems 15 (1995), no. 6, 1173–1181.
- [9] K. Schmidt, Amenability, Kazhdan’s property T, strong ergodicity and invariant means for ergodic group-actions, Ergodic Theory Dynamical Systems 1 (1981), no. 2, 223–236.
- [10] K. Schmidt, Asymptotically invariant sequences and an action of SL(2,Z) on the 2-sphere, Israel J. of Math. 37 (1980), 193-208.


