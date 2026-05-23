---
type: source
kind: paper
title: Comparison of two convergence criteria for the variable-assignment Lopsided Lovasz Local Lemma
authors: David G. Harris
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1610.01926v9
source_local: ../raw/2016-harris-comparison-two-convergence-criteria.pdf
ingested_for_concept: probabilistic-method.md
cites:
  - ../wiki/concepts/probabilistic-method.md
  - ../wiki/problems/12-*.md
  - ../wiki/problems/19-*.md
---

# arXiv:1610.01926v9[math.PR]26Aug2022

## Comparison of two convergence criteria for the variable-assignment Lopsided Lova´sz Local Lemma

##### David G. Harris∗

###### Abstract

The Lopsided Lov´sz Local Lemma (LLLL) is a cornerstone probabilistic tool for showing that it is possible to avoid a collection of “bad” events as long as their probabilities and interdependencies are suﬃciently small. The strongest possible criterion in these terms is due to Shearer (1985), although it is technically diﬃcult to apply to constructions in combinatorics.

The original formulation of the LLLL was non-constructive; a seminal algorithm of Moser & Tardos (2010) gave an eﬃcient algorithm for nearly all its applications, including to k-SAT instances where each variable appears in a bounded number of clauses. Harris (2015) later gave an alternate criterion for this algorithm to converge; unlike the LLL criterion or its variants, this criterion depends in a fundamental way on the decomposition of bad-events into variables.

In this note, we show that the criterion given by Harris can be stronger in some cases even than Shearer’s criterion. We construct k-SAT formulas with bounded variable occurrence, and show that the criterion of Harris is satisﬁed while the criterion of Shearer is violated. In fact, there is an exponentially growing gap between the bounds provable from any form of the LLLL and from the bound shown by Harris.

### 1 Introduction

The Lov´sz Local Lemma (LLL) is a general probabilistic principle for showing that, in a probability space Ω with a ﬁnite set B of “bad” events which are not too interdependent and are not too likely, then there is a positive probability no events in B occur. Since its introduction in [3], it has become a cornerstone of the probabilistic method of combinatorics.

There have been numerous extensions of the LLL since its original formulation. One important generalization known as the Lopsided Lov´asz Local Lemma (LLLL) [4] observes that it is not necessary for bad-events to be fully independent. If the bad-events are positively correlated in a certain sense, then for the purposes of the LLL this is just as good as independence. This type of correlation, which we discuss shortly, is known as lopsidependency.

In order to explain the LLL formally, we need to introduce a number of deﬁnitions. For any collection of events S ⊆ B, we deﬁne S = B∈S B; we refer to this event as avoiding

S. A dependency graph is a graph G on vertex set B such that for any B ∈ B and any set S ⊆ B − {B} − NG(B) (where NG(B) denotes the neighborhood of B in G), we have

Pr(B | S) = Pr(B). (1)

That is, each bad-event B ∈ B is independent of all other events in B, except possibly those which are neighbors of B in the dependency graph. A lopsidependency graph is a graph G on vertex set

∗Department of Computer Science, University of Maryland, College Park, MD 20742. Research supported in part by NSF Awards CNS 1010789 and CCF 1422569. Email: davidgharris29@gmail.com

B, satisfying the relaxed condition that for any B ∈ B and set S ⊆ B − {B} − NG(B), Pr(B | S) ≤ Pr(B). (2)

A probability space Ω and collection of bad-events B does not have a unique dependency graph or lopsidependency graph. Rather, we suppose that we are given Ω,B and some chosen graph G which is a (lopsi-)dependency graph for them.

For such a graph G with vertex set V = B, we say a set S ⊆ V is stable if no elements of S are adjacent in G. For real numbers pv, indexed by the vertices v ∈ V , we deﬁne the stable set polynomial of G with respect to base set S ⊆ V , denoted Q(G,S,p ), by

(−1)|T|−|S|

Q(G,S,p ) =

pv

v∈T

stable sets T S⊆T⊆V

With these deﬁnitions, we state a few formulations of the LLLL.

- Theorem 1.1. Suppose G is a lopsidependency graph for Ω,B. If any of the following conditions are satisﬁed, then Pr(B) > 0.

- 1. (Symmetric LLLL) If G has maximum degree d and every B ∈ B has Pr(B) ≤ p and ep(d + 1) ≤ 1
- 2. (Asymmetric LLLL) If there is a function x : B → (0,1) satisfying

∀B ∈ B Pr(B) ≤ x(B)

A∈NG(B)

(1 − x(A))

- 3. (Cluster-expansion criterion [2]) If there is a function µ : B → [0,∞) satisfying


∀B ∈ B µ(B) ≥ Pr(B) µ(B) +

Y ⊆NG(B) Y stable

A∈Y

µ(A)

The symmetric LLLL uses only a few crude parameters of the problem instance — namely, the maximum probability of a bad-event and the maximum degree of the lopsidependency graph. The other variants use progressively more information and take advantage of reﬁned dependency structure. See also [14] for another criterion in this vein. In [20], Shearer derived the most powerful possible criterion in these terms.

- Theorem 1.2 (Shearer’s criterion [20]). Let G be a graph on vertex set V = {1,...,n} and let p1,...,pn ∈ [0,1].


- 1. Suppose that Q(G,∅,p ) > 0 and Q(G,S,p ) ≥ 0 for all S ⊆ V . Then for any probability space Ω, and any events B1,...,Bn ⊆ Ω in that space such that Pr(Bi) = pi for i = 1,...,n and such that G is a lopsidependency graph for B = {B1,...,Bn}, we have Pr(B) ≥ Q(G,∅,p ) > 0. In this case, we say that Shearer’s criterion is satisﬁed by G,p .

- 2. Suppose that either Q(G,∅,p ) ≤ 0 or there is some stable set S ⊆ V with Q(G,S,p ) < 0. Then there is some probability space Ω and events B1,...,Bn ⊆ Ω such that PrΩ(Bi) = pi for i = 1,...,n and such that G is a dependency graph for B = {B1,...,Bn} and Pr(B) = 0. In this case, we say that Shearer’s criterion is violated by G,p .


Having bad-events with probability 0 or 1 is not so interesting, and Theorem 1.2 can be simpliﬁed when we disallow these cases.

- Theorem 1.3 ([8], Lemma 5.27). Suppose that p1,...,pn ∈ (0,1). Shearer’s criterion is satisﬁed by G,p if and only if Q(G,S,p ) > 0 for all stable sets S.


Thus, Shearer’s criterion exactly characterizes which probability and lopsidependency structure of the bad-events guarantees a positive probability of avoiding B. From a theoretical point of view, alternate bounds such as Theorem 1.1 are all weaker than, and are implied by, Shearer’s criterion. However, Shearer’s criterion is technically diﬃcult to apply to constructions in combinatorics.

#### 1.1 The variable-assignment LLLL

The LLLL has been applied to diverse probability spaces such as random permutations [16], Hamiltonian cycles [1], and perfect matchings [17]. However, by far the most common form of the LLL and LLLL concerns what we refer to as the variable-assignment setting. Here, the probability space Ω has m independent discrete random variables X1,...,Xm, and the bad-events can be taken to be “monomial events”; that is, each B ∈ B can be written in the form

(Xi1 = j1) ∧ (Xi2 = j2) ∧ ··· ∧ (Xik = jk)

For such a monomial event, we deﬁne var(B) = {i1,...,ik}. We say that two events B,B disagree on variable i if B demands Xi = j and B demands Xi = j for j = j .

- Deﬁnition 1.4. The canonical dependency graph G has an edge (B,B ) iﬀ var(B) ∩ var(B ) = ∅. The canonical lopsidependency graph G has edge (B,B ) iﬀ B disagrees with B on any variable i ∈ var(B) ∩ var(B ).


It is immediate that the canonical dependency graph is, indeed, a dependency graph for Ω,B. The fact that the canonical lopsidependency graph is a lopsidependency graph follows from the FKG inequality. Most applications of the LLL use only the canonical dependency graph; some noteworthy applications of the canonical lopsidependency graph include monochromatic hypergraph coloring [18] and boolean satisﬁability [6]. We will discuss the latter in much more detail later.

In [13], Kolipaka & Szegedy noted that the Shearer criterion is not tight for the variableassignment LLL setting. Namely, they found an explicit dependency graph and vector of probabilities where the Shearer criterion is violated yet any variable-assignment realization must have a satisfying assignment. Later work [11] provided a more systematic description of which dependency graphs were satisﬁable in the variable-assignment setting.

#### 1.2 The Moser-Tardos algorithm

The LLLL ensures that Pr(B) > 0, and this is usually suﬃcient for combinatorics where the main goal is to show existence results. However, typically Pr(B) is exponentially small, and hence the LLLL does not give eﬃcient algorithms for constructing such a conﬁguration. In [19], Moser & Tardos introduced a remarkably simple algorithm for the variable-assignment LLLL setting:

Algorithm 1 The Moser-Tardos (MT) algorithm

- 1: Draw each variable independently from the distribution Ω.
- 2: while there is a true bad-event on X do
- 3: Choose a true bad-event B arbitrarily.
- 4: Resample var(B) according to the distribution Ω.


They showed that when the asymmetric LLLL criterion is satisﬁed with respect to the canonical lopsidependency graph, then this algorithm terminates in expected polynomial time with a conﬁguration avoiding B. Later work [13] showed that this algorithm terminates quickly whenever the Shearer criterion is satisﬁed. Thus, at least for the variable-assignment LLLL setting, this gives an eﬃcient algorithm for nearly every construction based on the LLLL.

In [7], Harris gave a diﬀerent type of criterion for the Moser-Tardos algorithm. Unlike the symmetric LLLL or other similar criteria, this cannot be stated solely in terms of the dependency graph and the probabilities of the bad-events. We summarize it here (in a slightly simpliﬁed form).

- Deﬁnition 1.5 (Orderability). Given B ∈ B, we say that a set of bad-events Y ⊆ B is orderable to B, if there is an ordering Y = {B1,...,Bs}, such that, for each i = 1,...,s, there is a variable zi ∈ var(B) ∩ var(Bi) where B disagrees with Bi on zi but B does not disagree with B1,...,Bi−1 on zi.


- Theorem 1.6 ([7]). Suppose there is µ : B → [0,∞) satisfying the condition


∀B ∈ B µ(B) ≥ Pr(B) µ(B) +

µ(A)

A∈Y

Y orderable to B

Then the Moser-Tardos algorithm terminates with probability 1.

Theorem 1.6 is superﬁcially similar to the cluster-expansion criterion. It is strictly stronger than the asymmeric LLLL and certain simpliﬁed forms of the cluster-expansion criterion. However, its relation to the Shearer criterion is not clear. It is quite plausible, along the lines of [13, 9], that it truly takes advantage of extra information in the variable assignment LLLL. On the other hand it is quite plausible that Theorem 1.6 is more along the lines of [14], namely, it provides a more accurate and computationally eﬃcient approximation to Shearer’s criterion.

In this paper, we will construct a problem instance for which Theorem 1.6 is satisﬁed, yet Shearer’s criterion is violated. Thus, it is impossible to deduce the fact that Pr(B) > 0 based only on the probabilities and interdependency structure of the bad-events; it is necessary to take into account the decomposition of the bad-events into variables (as is provided by Theorem 1.6). In other words, Theorem 1.6 can be stronger than Shearer’s criterion.

We emphasize that Shearer’s criterion concerns arbitrary probability spaces; one cannot hope to provide a stronger criterion than Shearer’s for the level of generality to which the latter applies. The strength of Theorem 1.6 comes from its less general setting (the variable assignment LLLL), which is nevertheless encompasses many applications in combinatorics.

We also remark on other related criteria for the variable-assignment LLL setting. For instance, [9, 10] derive certain convergence conditions in terms of the bipartite graph H on vertex sets {1,...,m} and B and an edge on (i,B) when i ∈ var(B), and [11] derives conditions in terms of the probabilities that certain neighboring bad-events hold simultaneously.

### 2 Satisﬁability with bounded variable occurrence

Consider boolean k-satisﬁability instances, where we have m boolean variables X1,...,Xm and n clauses C1,...,Cn of width k, each of the form

Ci ≡ li1 ∨ li2 ∨ ··· ∨ lik

for distinct literals li1,...,lik (i.e. expressions of the form Xj or ¬Xj). The goal is to produce a value for the boolean variables X1,...,Xm ∈ {T,F}m such that all the clauses Ci are simultaneously

true. Equivalently, we want to ﬁnd a satisfying assignment of the conjuctive-normal form (CNF) formula

n

li1 ∨ li2 ∨ ··· ∨ lik

Φ =

i=1

We are interested speciﬁcally in instances where each variable appears in a bounded number of clauses. For each i = 1,...,m, deﬁne R0(Φ,i) and R1(Φ,i) to be the number of clauses which contain the literal Xi (respectively ¬Xi), and let R(Φ,i) = R0(Φ,i) + R1(Φ,i). In [15], Kratochvı´l, Savicky´, and Tuza deﬁned the function f(k) as the largest integer L such that whenever R(Φ,i) ≤ L

for all i, then Φ is satisﬁable; they showed f(k) ≥ 2ekk. A series of later works [21, 12, 5, 6] showed a variety of upper and lower bounds of f(k). In particular, [6] showed

2k+1 e(k + 1) ≤ f(k) ≤ (1 + O(k−1/2))

2k+1 ek

,

The lower bound comes from the variable-assignment LLLL. Here, the probability space Ω is deﬁned by setting each variable Xi = T with a certain probability pi given by

R1(Φ,i) − R0(Φ,i) R(Φ,i)

pi = 1/2 + x

for some carefully chosen parameter x ≥ 0. Then, for each clause Ci, there is a corresponding bad-event Bi that Ci is false, namely Bi has the form

(Xi1 = ji1) ∧ ··· ∧ (Xik = jik)

where ji1,...,jik ∈ {T,F}. Using Theorem 1.6 in place of the LLLL, and using a slightly diﬀerent value for the probabilities pi, Harris [7] showed a stronger bound

2k+1(1 − 1/k)k k − 1 −

2 k

f(k) ≥

With these constructions, we thus know the asymptotic bound

(3)

2k+1 ek

f(k) ∼

;

nevertheless, there are two main reasons to determine f(k) as precisely as possible. First, since f(k) grows exponentially in k, the asymptotic value is not as relevant for practical applications. Second, [15] showed a sudden gap in the computational complexity of k-SAT: for problem instances where variables may appear in f(k) + 1 clauses, it is NP-complete to determine satisﬁability. On the other hand, problems instances where they appear in at most f(k) clauses are always satisﬁable and the problem is computationally vacuous. Thus, tiny gaps in the value of f(k) can lead to huge gaps in computational hardness.

#### 2.1 Restricting the number of occurrences of each literal

Our goal is to demonstrate that the bound in Eq. (3) cannot be shown from the Shearer criterion. If the probability space Ω is allowed to vary in a problem-speciﬁc way, then any satisﬁable formula can trivially satisfy the LLL: namely, Ω puts probability mass 1 on some satisfying assignment. Thus, in order to separate the LLL and Theorem 1.6, we must restrict Ω to be problem-independent.

In both the constructions of [6] and [7], the probabilities pi depend solely on the imbalance between R0(Φ,i) and R1(Φ,i). They use slightly diﬀerent formulas; however, in both constructions, the extremal case is when R0(Φ,i) = R1(Φ,i), in which case pi is set to 1/2.

Accordingly, let us deﬁne f (k) to be the largest integer L such that whenever R0(Φ,i) ≤ L and R1(Φ,i) ≤ L for all i, then the formula Φ is satisﬁable. Clearly f (k) ≥ f(k)/2. This function is also studied in [5], with slightly diﬀerent terminology, in terms of a combinatorial object called a (k,d)-tree.

Deﬁnition 2.1 ([6]).1 A (k,d)-tree is a binary tree T where every leaf has depth at least k, and every node u of T has at most d descendant leaves within distance k of u.

We quote the following two results from [5] and [6]:

- Theorem 2.2. • [5, Lemma 2] If there exists a (k − 1,d)-tree, then there is an unsatisﬁable k-CNF formula where every literal occurs in at most d clauses.

• [6, Theorem 1.3] For any k ≥ 1, there exists a (k,d) tree with d = (2/e + O(k−1/2))2k/k This immediately gives the following result:

- Theorem 2.3. f (k) ≤ (1 + O(k−1/2))2ekk

Let us use the LLL and Theorem 1.6 to show more precise lower bounds on f (k). We will ﬁx a problem-independent probability space Ω to set each Xi to be T with probability pi = 1/2. For each clause Ci, we have a bad-event Bi with probability Pr(Bi) = p = 2−k.

- Theorem 2.4 (Follows easily from the symmetric LLLL). f (k) ≥ 2ekk − 1/k Proof. Consider some bad-event, without loss of generality

B ≡ (X1 = T) ∧ ··· ∧ (Xk = T)

The neighbors of B in the canonical lopsidependency graph G are bad-events involving Xi = F for some i = 1,...,k; as each literal occurs at most L times, there are at most d = kL such bad-events. The symmetric LLLL criterion ep(d + 1) ≤ 1 then holds if L ≤ 2ekk − 1/k.

| |
|---|


- Theorem 2.5 (From Theorem 1.6). Suppose that


(2k − 1)(1 − 1/k)k−1 k

R0(Φ,i),R1(Φ,i) ≤

for all i. Then the Moser-Tardos algorithm ﬁnds a satisfying assignment of Φ in expected polynomial time. In particular,

(2k − 1)(1 − 1/k)k−1 k

f (k) ≥

Proof. We will set µ(B) = α for all B ∈ B, where α ≥ 0 is some parameter to be determined. Consider some bad-event, without loss of generality

B ≡ (X1 = T) ∧ ··· ∧ (Xk = T)

1The deﬁnitions of (k, d)-trees are slightly shifted in the two papers; the object referred to as a (k, d)-tree in [6] is referred to as a (k − 1, d)-tree in [5]. To put things on a consistent footing, we have adopted the terminology of [6].

It is diﬃcult to list all orderable sets of neighbors of B according to Deﬁnition 1.5. However, to apply Theorem 1.6, we only need to provide an upper bound on the sum over such orderable sets (possibly including some additional neighbor-sets Y as well). Any such orderable set will have, for each j = 1,...,k, a choice of zero or one bad-events Aj which ﬁrst disagree with B on variable Xj. (That is, in Deﬁnition 1.5, we have Bi = Aj where zi = Xj). Thus, we have an upper bound:

A∈Y

Y orderable to B

µ(A) ≤

k

(1 + R1(Φ,j)α) ≤ (1 + Lα)k

j=1

So a suﬃcient criterion to satisfy Theorem 1.6 is α ≥ 2−k(α + (1 + Lα)k) (4)

1

2k−1 kL

k−1 −1

We choose α to maximize α−2−k(α+(1+Lα)k); simple calculus gives α =

L , which is non-negative for L ≤ 2kk−1. With this choice of α, the condition (4) is satisﬁed for

(2k − 1)(1 − 1/k)k−1 k Thus, if L ≤ (2

L ≤

k−1)(1−1/k)k−1

k and L ≤ 2kk−1, then Theorem 1.6 is satisﬁed. The second condition L ≤ 2kk−1 can be easily seen to be redundant, leading to the given bounds.

| |
|---|


In either case, we have f (k) ∼ 2k/(ek) ∼ f(k)/2. Let us deﬁne FLLL(k) = 2ekk − 1/k and FMT(k) = (2

k−1)(1−1/k)k−1

k to be the bounds on f (k) which are provable respectively from the symmetric LLLL (Theorem 2.4) and from the criterion of Theorem 2.5. We observe that

2k 2ek2 − 1

FMT(k) − FLLL(k) ≥

So the gap between the LLL and Theorem 1.6 appears to be growing exponentially in k. (The relative diﬀerence between the formulas approaches zero, however).

### 3 Constructing the extremal formula Φ

Let us ﬁx integers L,k. We will construct a k-SAT instance Φ with R0(Φ,i),R1(Φ,i) ≤ L, in which the Shearer criterion is violated for the canonical lopsidependency graph corresponding to the natural space Ω where Pr(Xi = T) = 1/2, and all variables Xi are independent, and with the natural collection of bad-events corresponding to the clauses. However, L ≤ FMT(k); thus Theorem 1.6 ensures that Φ is satisﬁable.

To begin the construction, start with Φ0 containing no clauses (i.e. Φ0 is the tautology). At stage i of the process, we modify Φi−1 to produce a new formula Φi by adding L − 1 clauses in which i appears positively and L − 1 clauses in which i appears negatively. All other variables in these clauses are completely new, not appearing in any clause of Φi−1; they all appear positively in the 2L − 2 new clauses, and each of the new variables (other than variable i) appears in exactly one new clause.

Note that Pr(B) = p = 2−k for all bad-events. Furthermore, since each variable i has exactly one positive occurence added in some iteration Φi for i = i, we have

R0(Φj,i) ≤ L R1(Φj,i) ≤ L − 1

for all i,j.

Deﬁne G be the canonical lopsidependency graph corresponding to the bad-events for the formula Φ . Although these graphs are complex, they contain a relatively simple and regular family of subgraphs Hj. We will show that Shearer’s criterion is violated for these subgraphs; as shown in [20], this implies that Shearer’s criterion is violated for the overall graph G .

The graph family Hj will consist of many copies of KL−1,L−1, the complete bipartite graph with L − 1 vertices on each side. Each graph Hj has a special copy of KL−1,L−1, called the root of Hj. We deﬁne these graphs recursively. First, H0 is the empty graph. To form Hj+1, we start by taking a new copy of KL−1,L−1 designated as the root of Hj+1. For each vertex v in this root, we add k − 1 separate new copies of Hj, along with an edge connecting v to all the vertices in the right-half of the root of the corresponding Hj.

For example, H1 consists of a single copy of KL−1,L−1. See Figure 1.

Root of H_{j+1}

v

… (k-1) copies of H_j

Figure 1: Construction of Hj+1 from Hj. We have only shown here two copies of Hj corresponding to a single vertex v in the root of Hj+1. There are k − 1 copies of Hj for each vertex in the root of Hj+1 (a total of 2(L − 1)(k − 1) copies of Hj).

- Proposition 3.1. Any graph Hj appears as a subgraph of G for some suﬃciently large.


Proof. Deﬁne Ai to be the collection of clauses in Φi but not Φi−1. We can also deﬁne a tree structure T on the variables of Φ: variable i is a parent of variable j if variable j appears in Φi but not Φi−1. For any variable i, let Ti denote the subtree of T rooted at i.

For any set of variables S, deﬁne G [S] to be the subgraph of G induced on the clauses φ of Φ such that all variables in φ come from S. Observe that if S,S are disjoint sets of variables then G [S],G [S ] are also vertex-disjoint graphs.

We will prove by induction on j a stronger claim: for any variable i, there is some integer D(i,j) suﬃciently large such that the induced subgraph GD(i,j)[Ti] contains a copy of Hj, and the root of this copy of Hj corresponds to the clauses of Ai.

When j = 0 this is vacuously true. For the induction step, consider some variable i. Let C denote the (2L−2)(k −1) variables which are children of i in T . By inductive hypothesis, for each i ∈ C, the graph GD(i ,j−1)[Ti ] contains a copy of Hj−1 whose root corresponds to Ai .

Let = i + maxi ∈C D(i ,j − 1); we claim that the choice D(i,j) = satisﬁes the induction claim. For, in the graph G [Ti], the clauses of Ai in which i appears positively are lopsidependent with those clauses in which i appears negatively. Thus, it has a copy of KL−1,L−1 corresponding to Ai; we denote this copy by J. The graph G [Ti] also contains the disjoint graphs G [Ti ] for each i ∈ C. For each such i ∈ C, let Ji denote the corresponding copy of Hj−1 in G [Ti ].

Consider some clause φ ∈ Ai, corresponding to a vertex of J, and some variable i = i in this clause. The root of Ji corresponds to the clauses Ai . Note that φ is the only clause of Ai in which i appears, and it appears positively in φ. Variable i also appears negatively in exactly L−1

clauses of Ai , which correspond to the right-half of Ji . Thus, there are edges from φ in J to all the right-vertices in k − 1 copies of Hj−1. As this is true for every φ ∈ J, the resulting graph is precisely Hj. This completes the induction.

| |
|---|


### 4 Computing the Shearer criterion for Hj

We now compute the Shearer criterion for the family of graphs Hj. For our intermediate calculations, we also need to work with another closely-related family of graphs. For each j ≥ 0, deﬁne a

graph H j by taking a single vertex v along with k − 1 new copies of Hj. We include an edge from v to all the vertices in the right-half of the roots of Hj. See Figure 2.

Root of H'_{j}

v

(k-1) copies of H_{j} …

Copies of H_{j-1}

Figure 2: The construction of H j from Hj.

We will make use of two computational tricks for stable set polynomials; the proofs of these are elementary and are omitted here.

- Proposition 4.1. If vertex set V is partitioned into connected-components as V = V1 V2, then Q(G,∅,p ) = Q(G[V1],∅,p )Q(G[V2],∅,p )
- Proposition 4.2. Suppose X ⊆ V . Then

Q(G,∅,p ) =

stable set U⊆X

Q(G[V − X − N(U)],∅,p )

i∈U

(−pi)

We now begin the calculation.

- Proposition 4.3. Let us deﬁne rj = Q(H j,∅,p ) sj = Q(Hj,∅,p )


Then r0 = 1 − p,s0 = 1, and r,s satisfy the mutual recurrence relations for j ≥ 1: rj = s(jk−1) − prj(k−−11)(L−1)s(k−1)

2(L−1) j−1

sj = 2rj(L−−11)sj(k−−11)(L−1) − s(jk−−11)(2L−2)

Proof. The base cases are clear, since H0 is empty and H 0 is a single node. We ﬁrst show the bound on sj for j ≥ 1. In any stable set U of Hj, either U contains zero vertices from the left half of the root of Hj, or zero vertices from the right-half of the root of Hj, or both. In the ﬁrst two cases, when we remove the vertices in the left (respectively right) half of Hj, then we are left with L − 1 copies of H j−1 and (k − 1)(L − 1) copies of Hj−1. In the third case, we are left with (k − 1)(2L − 2) copies of Hj−1. We can sum the ﬁrst two contributions and subtract the third, as it is double-counted: this gives

sj = 2rj(L−−11)s(jk−−11)(L−1) − s(jk−−11)(2L−2)

Next consider the bound for rj. Let v denote the root node of H j and let J1,...,Jk−1 be the copies of Hj to which it is connected, and let Pi denote the root of each Ji. We apply Proposition 4.2 with X = {v}, and so either U = ∅ or U = {v}. For U = ∅, the graph H j[V − X − N(U)] consists of k−1 independent copies of Hj. For U = {v}, consider the graph H j[V −X −N(U)]: the vertices in the left half of Pi now yield L−1 disconnected copies of H j−1 and each vertex u in the right half of Pi now yields k −1 disconnected copies of Hj−1. Over all k −1 choices of i and all (k −1)(L−1) choices for u in each Pi, we see that H j[V −v −N(v)] consists of (k −1)(L−1) copies of H j−1 and (k − 1)2(L − 1) copies of Hj−1. See Figure 3.

Root of H'_{j}

(k-1) copies of H_{j}

…

Copies of H_{j-1}

Figure 3: Removing the root node from H j Summing the contributions of these two terms according to Proposition 4.2 gives

2(L−1)

rj = Q(H j,∅,p ) = sj(k−1) − prj(k−−11)(L−1)s(k−1)

j−1 .

| |
|---|


- Proposition 4.4. Suppose that G satisﬁes the Shearer condition for all ≥ 0. Then, if we deﬁne the function g : [0,1] → R by


p (2 − a−(L−1))k−1, there is some a ∈ (2

g(a) = 1 −

−2

2L−2,1] satisfying g(a) = a. Proof. For j ≥ 0 deﬁne

rj s(jk−1)

aj =

.

We will show a recurrence relation for aj. Using Proposition 4.3, we calculate for j ≥ 1:

2(L−1) j−1

2(2L−2) j−1

s(jk−1) − prj(k−−11)(L−1)s(k−1)

prj(k−−11)(L−1) s(jk−−11)2(L−1)

s(k−1)

paj(k−−11)(L−1)

= 1 −

= 1 −

·

aj =

k−1

s(jk−1)

sj(k−1)

sj s(jk−−11)(2L−2)

###### Here again using Proposition 4.3, we get

sj s(jk−−11)(L−2)

2rj(L−−11)s(jk−−11)(L−1) − s(jk−−11)(2L−2) s(jk−−11)(2L−2)

=

2rj(L−−11) s(jk−−11)(L−1)

− 1 = 2a(jL−−11) − 1 (5)

=

and, substituting this into the equation for aj, this implies:

pa(jk−−11)(L−1) (2a(jL−−11) − 1)k−1

aj = 1 −

= g(aj−1). (6)

−2

2L−2 for all j ≥ 1. For, if not, then Eq. (5) would otherwise imply that sj

We must have aj > 2

≤ 0; thus, either sj ≤ 0 or sj−1 ≤ 0. Thus, either Hj or Hj−1 violates the Shearer condition, and so would some G ; this contradicts our hypothesis.

s(jk−−11)(2L−2)

−2

Now suppose g(a) < a for all a ∈ (2−

2L−2,1], so from Eq. (6) the sequence a1,a2,... decreases monotonically. Because of the lower bound aj ≥ 2

−2

−2

2L−2, it converges to some limit point a ≥ 2

2L−2. By continuity, this must be a ﬁxed point, i.e. g(a) = a, as desired. Furthermore, since g(a) diverges to inﬁnity at a = 2

−2

2

2L−2, we must indeed have a > 2−

2L−2 strictly. Otherwise, suppose that g(a) ≥ a for some a ∈ (2−

−2

2L−2,1]. Observe that g(1) = 1 − p < 1. Hence, the function g(a) − a changes sign on the interval (2−

−2

2L−2,1]. This implies there must be a ﬁxed point g(a) = a on this interval.

| |
|---|


###### Proposition 4.5. Suppose

ln(2 − t) ln(1 − 2−kt1−k) for all t ∈ (2k/(k−1),2). Then the Shearer condition is violated on G , for suﬃciently large. Proof. Suppose not; by Proposition 4.4, the function g then has a ﬁxed point a ∈ (2−

L > 1 −

−2

2L−2,1]. So

2−k (2 − a−(L−1))k−1 Solving for L, we thus obtain:

a = 1 −

k

1 1−k

ln 2 − 2

1−k(1 − a)

L = 1 −

lna

for t = 2k/(1−k)(1 − a)1/(1−k) (7)

where here t ∈ (2k/(k−1),2). This contradicts our hypothesis. For any k ≥ 1, let us deﬁne the quantity F˜Shearer(k) by: F˜Shearer(k) = max

ln(2 − t) ln(1 − 2−kt1−k)

1 −

t∈(2k/(k−1),2)

| |
|---|


In light of Proposition 4.5, this is an upper bound on the value of f (k) that can be shown using the LLL or any variant of it. We observe that F˜Shearer(k) ≥ FLLL(k) for all values of k — this must be the case, since the bound FLLL was indeed derived using the LLL and this is always weaker than Shearer’s criterion. To illustrate, we list FLLL,F˜Shearer, and FMT for a few small values of k.

|k| |FLLL|F˜Shearer|FMT|
|---|---|---|---|---|
|9| |20|21|22|
|10| |37|38|39|
|11| |68|69|71|
|12| |125|126|131|
|13| |231|233|241|
|14| |430|432|446|
|15| |803|806|831|
|16| |1506|1510|1555|
|17| |2836|2842|2922|
|18| |5357|5366|5511|
|19| |10151|10165|10426|
|20| |19287|19311|19784|


The gap between F˜Shearer and FLLL is very small, suggesting that there is little to no improvement possible in the bound for f (k) from a more advanced more of the LLL.

We next derive an asymptotic approximation to F˜Shearer.

- Proposition 4.6. F˜Shearer = 2ekk + Θ(2kk3) Proof. We can show the lower bound by taking t = 1 − 1/k, i.e.


2k ek

2k k3

ln(2 − t) ln(1 − 2−kt1−k) ≥ −

ln(2 − t) ln(1 − 2−kt1−k)

F˜Shearer ≥ 1 −

=

+ Ω(

).

For the lower bound, let L = F˜Shearer(k), so that L ≤ 1 −

ln(2 − t) ln(1 − 2−kt1−k)

for some t ∈ (2k/(k−1),2). Using the bound −ln(1 − x) ≥ x for x ≥ 0, we have:

L ≤ 1 + tk−12k ln(2 − t) (8) Since ln(2 − t) is a concave-down function of t, we have the bound

t0 − t 2 − t0

ln(2 − t) ≤ ln(2 − t0) +

for any chosen value t0 ∈ (0,2). Substituting this bound into (8), and diﬀerentiating with respect to t to maximize the resulting value, we get

k

2(1 − 1/k)(t0 + (2 − t0)ln(2 − t0))

L ≤ 1 +

(9)

(2 − t0)(k − 1)

If we set t0 = 1 − 1/k in Eq. (9), then straightforward analysis gives: L ≤

2k ek

2k k3

+ O(

)

| |
|---|


On the other hand, one can easily verify that FMT(k) ≥ 2ekk + Ω(2kk2); thus, there is a large and growing gap between FMT and F˜Shearer.

### 5 Acknowledgments

Thanks to Aravind Srinivasan and anonymous journal referees for many helpful comments and suggestions.

### References

- [1] Albert, M., Frieze, A., Reed, B.: Multicoloured Hamilton Cycles. The Electronic Journal of Combinatorics 2-1, R10. (1995)
- [2] Bissacot, R., Fernandez, R., Procacci, A., Scoppola, B.: An improvement of the Lov´sz Local Lemma via cluster expansion. Combinatorics, Probability and Computing 20-5, pp. 709-719

(2011)

- [3] Erd˝s, P., Lov´sz, L.: Problems and results on 3-chromatic hypergraphs and some related questions. In A. Hajnal, R. Rado, and V. T. Sos, eds. Inﬁnite and Finite Sets II, pp. 607-726

(1975)

- [4] Erd˝s, P., Spencer, J.: Lopsided Lov´sz Local Lemma and Latin transversals. Discrete Applied Math 30, pp. 151-154 (1990)
- [5] Gebauer, H.: Disproof of the neighborhood conjecture with implications to SAT. Combinatorica 32-5, pp. 573-587 (2012)
- [6] Gebauer, H., Szab´, T., Tardos, G.: The local lemma is asymptotically tight for SAT. Journal of the ACM 63-5, Article #43 (2016)
- [7] Harris, D.: Lopsidependency in the Moser-Tardos framework: beyond the Lopsided Lov´sz Local Lemma. ACM Transactions on Algorithms 13-1, Article #17 (2016)
- [8] Harvey, N., Vondr´k, J.: An algorithmic proof of the Lov´sz local lemma via resampling oracles. Proc. 56th annual IEEE Sympsium on Foundations of Computer Science (FOCS), pp. 1327-1346

(2015).

- [9] He, K., Li, L., Liu, X., Wang, Y., Xia, M.: Variable version Lov´sz local lemma: beyond Shearer’s bound. Proc. 58th annual IEEE Symposium on Foundations of Computer Science (FOCS), pp. 451-462 (2017)
- [10] He., K., Li, Q., Sun, X., Zhang, J.: Quantum Lov´sz local lemma: Shearer’s bound is tight. Proc. 51st annual ACM SIGACT Symposium on Theory of Computing (STOC), pp. 461-472

(2019)

- [11] He, K., Li, Q., Sun, X.: Moser-Tardos algorithm: beyond Shearer’s bound. arXiv:2111.06527

(2021)

- [12] Hoory, S., Szeider, S. Computing unsatisﬁability k-SAT instances with few occurrences per variable. Theoretical Computer Science 337 (1-3), pp. 347-359 (2005)
- [13] Kolipaka, K., Szegedy, M.: Moser and Tardos meet Lov´sz. Proc. 43rd annual ACM Symposium on Theory of Computing (STOC), pp. 235-244 (2011)


- [14] Kolipaka, K., Szegedy, M., Xu, Y.: A sharper local lemma with improved applications. In “Approximation, Randomization, and Combinatorial Optimization. Algorithms and Techniques” LNCS 7408, pp. 603-614 (2012)
- [15] Kratochvı´l, J., Savicky´, P., Tuza, Z.: One more occurrence of variables makes satisﬁability jump from trivial to NP-complete. SIAM Journal of computing 22-1, pp. 203-210 (1993)
- [16] Lu, L., Sz´ek´ely, L.: Using Lov´sz Local Lemma in the space of random injections. The Electronic Journal of Combinatorics 13-R63 (2007)
- [17] Lu, L., Sz´ek´ely, L.: A new asymptotic enumeration technique: the Lov´sz local lemma. arXiv:0905.3983v3 (2011)
- [18] McDiarmid, C.: Hypergraph coloring and the Lov´sz Local Lemma. Journal of Discrete Mathematics 167/168, pp. 481-486 (1995)
- [19] Moser, R., Tardos, G.: A constructive proof of the general Lov´sz Local Lemma. Journal of the ACM 57-2, pp. 11:1-11:15 (2010)
- [20] Shearer, J. B.: On a problem of Spencer. Combinatorica 5, pp. 241-245 (1985)
- [21] Savicky´, P., Sgall, J.: DNF tautologies with a limited number of occurrences of every variable. Theoretical Computer Science 238 (1-2), pp. 495-498 (2000)


