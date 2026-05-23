---
type: source
kind: paper
title: The Power of Two Choices in Graphical Allocation
authors: Nikhil Bansal, Ohad Feldheim
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2106.06051v2
source_local: ../raw/2021-bansal-power-two-choices-graphical.pdf
topic: general-knowledge
cites:
---

# arXiv:2106.06051v2[cs.DM]20Nov2021

## The Power of Two Choices in Graphical Allocation

Nikhil Bansal∗ Ohad Feldheim†

Abstract

The graphical balls-into-bins process is a generalization of the classical 2-choice balls-into-bins process, where the bins correspond to vertices of an arbitrary underlying graph G. At each time step an edge of G is chosen uniformly at random, and a ball must be assigned to either of the two endpoints of this edge. The standard 2-choice process corresponds to the case of G = Kn.

For any k(n)-edge-connected, d(n)-regular graph on n vertices, and any number of balls, we give an allocation strategy that, with high probability, ensures a gap of O((d/k) log4n log log n), between the load of any two bins. In particular, this implies polylogarithmic bounds for natural graphs such as cycles and tori, for which the classical greedy allocation strategy is conjectured to have a polynomial gap between the bins’ loads. For every graph G, we also show an Ω((d/k) + log n) lower bound on the gap achievable by any allocation strategy. This implies that our strategy achieves the optimal gap, up to polylogarithmic factors, for every graph G.

Our allocation algorithm is simple to implement and requires only O(log(n)) time per allocation. It can be viewed as a more global version of the greedy strategy that compares average load on certain ﬁxed sets of vertices, rather than on individual vertices. A key idea is to relate the problem of designing a good allocation strategy to that of ﬁnding suitable multi-commodity ﬂows. To this end, we consider Räcke’s cut-based decomposition tree and deﬁne certain orthogonal ﬂows on it.

Keywords. Load-balancing, Balls-into-bins processes, graphical two-choice, Rácke decomposition.

∗CWI Amsterdam and TU Eindhoven, N.Bansal@cwi.nl. Supported by the NWO VICI grant 639.023.812. †Hebrew University of Jerusalem Israel, ohad.feldheim@mail.huji.ac.il. Supported by ISF grant 1327/19.

### 1 Introduction

Randomized balls-into-bins models serve as useful abstractions for various problems arising in hashing, load balancing and resource allocation in parallel and distributed systems and have been extensively studied in the areas of probability, economics and algorithms (see e.g., [RS98, DR96, AK14]). The balls typically represent tasks or items, that need to be allocated to resources that are modeled by the bins. The goal is to balance the loads across bins as much as possible.

These models usually diﬀer by the kind of control available to the algorithm over the allocation process. In the classical single-choice model, the algorithm has no control and each ball is placed in a bin chosen uniformly at random. For n balls and n bins, it is well known that the heaviest bin has load (1 + o(1))lnn/lnlnn with high probability (w.h.p.). In the heavily loaded case, where the number of balls T can be much larger than n, the bin loads are in the range T/n ± Θ( (T log n)/n) (provided that T ≥ nlog n). In particular, the deviation from the average load of T/n increases with T as Θ( (T log n)/n).

2-choice model. Perhaps the simplest and most well-studied controlled variant of this model is the 2-choice model. Here at each step the algorithm is given two uniformly chosen bins into one of which it must allocate the ball. This seemingly minor modiﬁcation, leads to substantial improvements. In a seminal result, Azar, Broder, Karlin and Upfal [ABKU94] showed that if a ball is placed in the least loaded of d ≥ 2 uniformly sampled bins, then for T = O(n), the maximum load reduces to lnlnn/lnd + Θ(1). They also establish that this greedy allocation strategy is asymptotically optimal for this model.

These results were extended by Berenbrink, Czumaj, Steger and Vöcking [BCSV06] to the harder setting of arbitrary T. They showed that the maximum load is T/n + lnlnn/lnd + O(1) with probability

- 1 − 1/poly(n). Remarkably this implies that already for d = 2 choices, the excess load over the average does not increase with T at all (unlike for the case of d = 1). A simpler proof of this result, albeit with worse tail bounds, was given by Talwar and Wieder [TW14]).


Graphical process. In many natural settings, there are restrictions on which pairs of bins can be queried or where the ball can be placed. An elegant generalization of the 2-choice process, called the graphical process, was introduced by Kenthapadi and Panigrahy [KP06]. Here there is an underlying graph G = (V,E) on n = |V | vertices, and at each step, a uniformly random edge e = (u,v) is chosen and the ball must be placed on one of the two endpoints of e. Notice that the standard 2-choice process corresponds to the special case of G = Kn. This motivates the following natural question:

Given a graph G what is the best load balance obtainable by a graphical two-choice allocation strategy? Extending the results for the classical 2-choice process (G = Kn), [KP06] showed that if G is n -regular,

then for T = n balls, the greedy strategy, has maximum load is lnlnn + O(log 1/ ). An extension to hypergraphs was considered in [God08].

The harder setting of arbitrary T, which is also the focus of our work, was considered by Peres, Talwar, Weider [PTW15]. They investigated the greedy strategy, and using an elegant majorization and potential function technique showed that the gap between the maximum and minimum bin load is Θ(log n) for complete graphs and more generally, O((log n)/β) for d-regular graphs with edge-expansion1 β.

Upper gap versus gap. Notice that the objective studied by [PTW15] is slightly diﬀerent from the one in [ABKU94, BCSV06, KP06]. Let us use the term upper gap for the diﬀerence between the maximum load and the average load, and gap for the diﬀerence between the maximum and minimum load. These objectives can diﬀer sometimes, e.g., for G = Kn, the gap2 is Θ(log n) while the upper gap is Θ(log log n). However, this diﬀerence seems less relevant for general graphs, e.g., for a constant degree expander G, the gap is Θ(log n) while the upper gap is Ω(log n/log log n). We discuss this issue further in Sections 1.3 and 4.

Limitations of the greedy strategy. While almost all previous results on the 2-choice model consider the greedy strategy, it turns out that greedy can be quite sub-optimal for general graphs. For example,

1For any subset S ⊂ V with |S| ≤ n/2, E(S, S) ≥ βd|S|. 2The lower bound of Ω(log n) on the gap follows (in fact for any graph G) because by a standard coupon collector argument,

in any consecutive sequence of Ω(n log n) steps, with constant probability some bin will not be considered at all.

for a n-vertex cycle G the conjectured gap and upper gap under greedy are Θ(√n) [ANS20]3. See also our simulation results in Figure 1 below. The best known upper bound for a cycle is O(nlog n) by the result of [PTW15] (as the expansion β = O(1/n)).

Analyzing the gap for greedy, even on simple graphs like cycles, seems surprisingly hard and its study has led to several intriguing conjectures in asymmetric stochastic dynamics that seem beyond current techniques. On the cycle, the loads are conjectured to converge after proper scaling to a Brownian motion. For more general graphs the load ﬂuctuations under greedy are conjectured to be similar to the ﬂuctuations in classical statistical mechanics models.4

|0<br><br>10<br><br>20<br><br>30<br><br>40<br><br>50<br><br>60<br><br>70<br><br>10 40 70 100 130 160 190 220 250 280 310 340 370 400 430 460 490 520 550 580 610 640 670 700 730 760 790 820 850 880 910 940 970<br><br>Gap<br><br>Bins<br><br>Greedy Algorithm Gap Distribu on<br><br>Sampled Gap Average Square root es mate<br><br>|
|---|


Gap

Figure 1: The gap for greedy algorithm on cycles of sizes 10 to 1000, averaged over 84 runs of 109 balls. The dotted line is the function f(x) = 1.85√x − 1, error margins for 95% conﬁdence are provided. The graph clearly shows the polynomial growth of the gap.

Beyond greedy strategy. An advantage of the greedy strategy is that it is only uses local information: all we need to know in order to allocate is the load of the two suggested bins. However, in many applications the algorithm may be able to gather more global information to make better decisions, even though the task (ball) itself has only a few available options (bins). For example, in some situations transferring the task may require heavy overhead, complicated real world shipment, or overcoming physical restrictions, while the information could propagate in the network at much lower cost. Hence, a natural question is whether there are other allocation strategies which are superior and achieve substantially better gaps than greedy on more general graphs. Ideally we would also like that these strategies be simple to implement and be realizable in a distributed setting with low communication overhead.

#### 1.1 Results

Our main result is an allocation strategy that achieves the best possible gap, up to polylogarithmic factors, for the graphical process on any graph G. More formally, we show the following.

- Theorem 1.1. Let G = (V,E) be any k edge-connected, d-regular5 graph on n vertices. There is an allocation strategy for the graphical process on G, that guarantees for any time t ∈ N,


gapG(t) = O((d/k)log4 nlog log n) with probability at least 1 − 1/poly(n). Here gapG(t) is the maximum diﬀerence in vertex loads at time t.

- 3The authors consider a model where after allocating the ball to a vertices of the requested edge, the load on the two vertices is averaged. In this model, which intuitively should have a lower gap than greedy, they show that the typical gap is Ω(√n).

- 4In particular Peres (in private communication) suggested that, up to a log n factor the gap should be the same as that of a Gaussian free ﬁeld on G. This suggests that even for certain non-expander graphs, such as high-dimensional balanced grids, the greedy algorithm should have polylogarithmic gaps.
- 5The regularity assumption on G is standard and ensures uniform expected load on all bins under a random strategy. The results extend to irregular graphs in a natural way where one measures the gap with loads normalized suitably by the degree.


This is also the best possible gap for every graph G up to polylog(n) factors.

- Theorem 1.2. For any d-regular graph G and for any allocation strategy for G, for any time t, with constant probability, gapG(t) = Ω(d/k + log n), where k is the edge-connectivity of G.


In particular Theorem 1.1 gives an allocation strategy with gap polylog(n) for cycles and grids and any arbitrary connected bounded degree graph. More generally, it implies polylogarithmic gap for any graph G with connectivity k = Ω(d/polylog(n)), without any requirements on the expansion of G.

For a graph G the bound the gap in Theorem 1.1 is actually O(αG (d/k)log2 n) where αG is the congestion ratio for oblivious routing on G based on a Räcke decomposition tree [Räc02]6. It is known that αG = O(log2 nlog log n) for general graphs G [HHR03] and better bounds are also known for speciﬁc graphs, e.g., αG = O(log n) for a cycle.

The Algorithm. The algorithm consists of two parts: a preprocessing stage and an online allocation stage. The allocation strategy stays ﬁxed throughout, is quite simple to implement and incurs only O(log n) worst case running time per allocation. It can be viewed as a more global version of the greedy strategy, where given an edge e = (u,v), instead of comparing the loads on u and v, it compares the average load on two sets selected at random from a ﬁxed small collection and allocates the ball to u or v according to the result.

The preprocessing stage computes (i) a binary hierarchical decomposition of the vertices of G and (ii) for each edge e a distribution Pe over pairs of sibling sets (S,S ) in the decomposition. For each e, the support of Pe is only O(log n). The sets S and the distributions Pe are then ﬁxed and do not change over time.

In the allocation stage, upon the request for random edge e = (u,v), a pair of sets (S,S ) is sampled according to Pe and the ball is assigned to u or v depending on whether S or S has larger average load.

Complexity. The allocation strategy is very eﬃcient to implement and requires only O(log n) time per allocation step. In fact, this can be further reduced to O(1) amortized updates per allocation step. The total space used is O(mlog n).

The allocation strategy is also quite robust and does not require the exact knowledge of load on the sets S in the decomposition. We use this to give a distributed implementation the allocation strategy that requires only O(1) amortized messages per allocation, with O(log n) bits per message.

These implementation details are discussed in Section 3.5.

Remark 1.1. Finally we remark that our results do not require the full power of two choices. In the 1 + β graphical choice model (see also Section 1.3 below), at each step an edge is given only with probability β, and with probability 1 − β there is no choice and the ball is allocated to a random bin. Our bound on the gap extends directly to this model with factor O(1/β) loss.

- 1.2 Preliminaries, overview and techniques We now give a detailed overview of the ideas and the algorithm. We begin by describing the relevant notation.


Notation. A graphical process is speciﬁed by some ﬁxed d-regular graph G = (V,E). Henceforth we denote n = |V | and m = |E|.7 Let N(u) denote the neighborhood of the vertex u. At each time t = 1,2,..., an edge e = et = (u,v) ∈ E is chosen (requested) uniformly at random, and a ball must be assigned to one of its endpoints: u or v. We refer to the vertices of G as bins, and say that vertex u has load at time t, if

balls have been assigned to it after t steps. Let Lt : V → N denote the load vector at time t. We assume L0(u) = 0 for all u ∈ V so that the total load Lt 1 = t for each t ∈ N and the average vertex load is t/n.

An allocation strategy, upon the request e = (u,v), decides whether to assign the ball to u or v based on the current loads (and possibly on the entire history so far). The goal of the strategy is to regulate the

- 6While better bounds are known for congestion in oblivious routing [ACF+04, Räc08, AF09] based on a convex combination of trees, our method requires a single Räcke tree as the demands for our ﬂows depend on the tree itself.
- 7typically in balls-into-bins literature, m is used for the number of balls, but we will think of the allocation process as indeﬁnite, using t for the index of the allocated ball.


process in order to keep the load gap small, where the gap at time t is deﬁned as gap(t) = gapG(t) = max

Lt(u) − min

Lt(u).

u

u

- As maxu |Lt(u) − t/n| ≤ gapG(t) ≤ 2maxu |Lt(u) − t/n|, we sometimes work with maxu |Lt(u) − t/n|, the maximum deviation from the average load. For a subset S ⊂ V , We use Lt(S) := u∈S Lt(u) and Lt(S) := Lt(S)/|S| to the total and average load on vertices in S at time t, respectively.


Edge biases, induced drift and ﬂows. Upon the arrival of an edge e = (u,v), by choosing whether to allocate the ball to u or v, an allocation strategy can bias the load toward u or v. Let bt(u,v) denote the bias towards v for an edge e = (u,v) at time t. So bt(u,v) = 2p−1 ∈ [−1,1] if the ball is allocated to v with probability p upon arrival of e. Thus, bt(u,v) = −bt(v,u).

At any time t, the behavior of an allocation strategy deﬁnes the biases bt(u,v) ∈ [−1,1] for each edge (u,v) ∈ E, and, conversely, any valid biases at time t deﬁne an allocation strategy. Now let us consider the eﬀect of the biases at a vertex. At each time step, the average load over all bins increases by 1/n. Let

qt(v) =

(1 + bt(u,v)) 2

1 m

=

u∈N(v)

1 n

bt(u,v) 2m

+

u∈N(v)

denote the probability of assigning a ball to v at time t. Let us call dt(v) = 2m(qt(v)−1/n) = u∈N(v) bt(u,v) the drift induced by the strategy at v at time t. Observe that dt(v) ∈ [−d,d] and qt(v) ∈ [0,2/n].

A simple but useful observation is that if we view the biases bt(u,v) as a ﬂow of bt(u,v) from u to v, then the drifts correspond to the total ﬂow entering a vertex. Conversely, for any desired vertex drifts if there is a corresponding feasible ﬂow with capacity at most 1 per edge, viewing the ﬂow as edge biases gives an allocation strategy achieving this drift vector.

A ﬁrst attempt. To control the load gap, we would like to set the edge biases at each time t, such that the underloaded vertices are more likely to receive a ball (say qt(v) ≥ (1+δ)/n) while the overloaded vertices are less likely (qt(v) ≤ (1 − δ)/n) to receive a ball. By a simple Markov chain argument, this ensures an O(δ−1 log n) gap w.h.p. at any time. This is the same as assigning drift ≥ δd (resp. ≤ −δd) to underloaded (resp. overloaded) vertices.

However, such a drift is impossible to realize as a feasible ﬂow, unless G has large expansion. In particular, consider a cycle where the the vertices of the left half of are overloaded and those of the right half are underloaded. As the total ﬂow that can cross the cut separating the two halves is at most 2, the drifts can only have absolute value O(1/n) on average, resulting in an Ω(nlog n) load deviation. Roughly, this is the reason why the expansion condition on G is required in [PTW15].

Additionally, we would also like the allocation strategy to be simple to implement, and avoid solving a ﬂow problem at each time step, depending on which vertices are overloaded or underloaded.

We now describe our method for geting around both of these issues. Roughly speaking, we will create drifts for sets of vertices instead of drifts for individual vertices.

Hierarchical decomposition and orthogonal drifts. Let G = (V,E) be the graph underlying the process. Consider some binary hierarchical decomposition of G, represented by a binary tree T = (VT,ET), with internal nodes i ∈ VT corresponding to subsets Si ⊂ V and leaves in VT to singleton sets, one for each vertex of G. We will identify the leaves of T with the vertices of G. We use node to refer to the internal vertices of T and vertex to refer to the vertices of G.

Let r be the root of T. For a leaf u, consider the unique path u = i0,i1,...,ih = r from u to r in T, so that {u} = Si

= V . As Lt(Sr) = Lt(V ) = t/n and Lt(Su) = Lt(u), the load deviation for u at time t can be upper bounded by

0 ⊂ Si

1 ⊂ ... ⊂ Si

h

|Lt(u) − t/n| =

h

j=1

h

Lt(Si

###### ) − Lt(Si

) ≤

j−1

j

j=1

Lt(Si

###### ) − Lt(Si

###### ) ,

j−1

j

and hence to control the load deviation for each u ∈ V , up to an h = O(log n) factor, it suﬃces to control the gap |Lt(Si

) − Lt(Si

)| for each parent-child node pair.

j−1

j

Fix a non-leaf node i ∈ VT, and let (i),r(i) denote its left and right children. A simple computation shows that the parent-child gap can be bounded in terms of the sibling gap |L(S (i)) − L(Sr(i))|. To control this sibling gap for each pair of siblings (i) and r(i) in the tree, we would like to create a (dynamic) balancing drift between S (i) and Sr(i), that at any time is directed towards the sibling with lower load.

To avoid these diﬀerent drifts from interfering, a key idea is to construct the drifts to be orthogonal,

which ensures that the drift associated with S (i) and Sr(i) yields zero net drift on every other set Sj ∈ T. To do so we set the balancing drift to be the Haar measure associated with node i in the hierarchical Haar

decomposition basis corresponding to T. Simply put, we divide the drift on each of S (i),Sr(i) evenly among all vertices of the corresponding set. An illustration of a system of orthogonal drifts is provided in Figure 2.

Small relative bias suﬃces. The balancing drifts associated with S (i) and Sr(i) should also be suﬃciently strong in order to get good bounds on |L(S (i)) − L(Sr(i))|, but on the other hand, the resulting ﬂow (edge biases) should be feasible. Suppose k = Ω(d) for this discussion. A second key observation is that to achieve the polylogarithmic gap in Theorem 1.1, it suﬃces to have the total drift between every two siblings S (i) and Sr(i) be Ω(d/polylog(n)), i.e., the drifts for vertices in S (i),Sr(i) need only be Ω(d/|S (i)|polylog(n)) and Ω(d/|Sr(i)|polylog(n)) on average. It may seem counter-intuitive at ﬁrst, that the total drift does not need to scale with the sizes of S (i) and Sr(i). The reason for this is that what matters is the concentration of |L(S (i)) − L(Sr(i))| which is also normalized by the sizes of the two sets.

Using Räcke Trees to realize the drift. To realize the above system of drifts by feasible ﬂows, the ﬁnal piece is Räcke trees and the multicommodity ﬂow templates associated with them.

A Räcke tree R of a graph G = (V,E) corresponds to a hierarchical decomposition R together with a collection of ﬂow templates {fuv}u,v∈V for each pair of vertices u,v. Each internal vertex i ∈ R corresponds to a set Si ⊂ V , where the leaves of correspond to the singleton vertices of G. The capacity of a parentchild edge (i,j) ∈ R is the capacity of the corresponding cut (Sj,Sjc) in G. The ﬂow templates {fuv}u,v∈V specify how to route one unit of ﬂow from u to v in G and have the following remarkable property: let D = {κ(u,v)}u,v∈V be any multicommodity demand vector where κ(u,v) units of commodity ku,v to be routed from u to v. If D can be routed feasibly on R (along the unique u to v path on the tree) subject to the edge capacities in R, then the corresponding ﬂow in G produced using the ﬂow templates has load at most αGce on any edge e ∈ E, where ce is the capacity of e. We call αG the congestion ratio of G with respect to R.

The best bound on αG is O(log2 nlog log n) [HHR03] for general graphs, and the corresponding R and ﬂow templates fuv can be constructed in polynomial time. Almost linear time constructions with slightly worse αG are also known [RST14]. The tree R is also well-balanced so that |Rj|/|Ri| ≤ 34 for each child Rj of Ri, and thus it has depth O(log n).

In the preprocessing stage, given G we ﬁrst construct the Räcke tree R and modify it into a binary tree T. For each internal node i of T, we deﬁne the orthogonal drift between the corresponding sets S (i) and Sr(i) as described above. Together with the ﬂow templates, which are ﬁxed, this deﬁnes ﬁxed probabilities pe(i) that each edge e will use to bias according to the sign of L(S (i))−L(Sr(i)). As the drifts are orthogonal and the sets Si and the ﬂow templates are ﬁxed, this allows us to decouple the drifts for diﬀerent i.

The resulting allocation strategy after preprocessing is extremely simple to describe and eﬃcient to implement and requires only O(log n) running time per allocation request.

#### 1.3 Related work and models

The literature on ball-into-bins processes is extensive and it is impossible to cover even a small portion of the developments and applications. The ﬁrst appearance of a 2-choice type result was in [KLadH96] in the context of online hashing. Following the result of Azar et al., [ABKU94] several variations of the model have been studied. Variations include models in which balls are eliminated over time [Mit91, CFM+98] – either by age or at random and parallel allocation of the balls with limited communication [Ste96, ACMR98].

a

S1

- 10

- 11


- S11
- S12


c b

3ε 3ε

6ε

- 4

- 5


7 5

S1 S2

d

3ε 3ε

e

3ε

3 3

- 1

- 2


6 3

- 1

- 2


S11 S12

ε ε ε

- 2ε ε
- 3ε


ε 2ε

f g

a b c

f g h

3 2

3 2

-ε -2ε

0 0 0

0

h

i

d e

i k

k

2ε ε

S2

0 0

a

S1

0.6ε

- 10

- 11


- S11
- S12


c b

3ε 3ε

6ε

- 4

- 5


7 5

1.2ε

S1 S2

0.6ε

d

1.2ε 1.8ε

1.2ε 1.8ε

e

0

3 3

- 1

- 2


6 3

- 1

- 2


S11 S12

ε ε ε

0.6ε 0.6ε 0.6ε 1.2ε

0.6ε 0.6ε 0.6ε

1.2ε

f g

a b c

f g h

3 2

3 2

0.6 ε 1.2ε

0.6 ε 0.6 ε 0.6 ε -0.6 ε -0.6 ε -0.6 ε

0.6ε 0.6ε

h

0.6ε 0.6ε

i

0.6ε

d e

i k

k

0.6 ε

0.6 ε

-0.6 ε -0.6 ε

S2

Figure 2: The ﬁgure shows a 10 vertex graph G with vertices depicted by bins and the dots in a bin indicating the current load. The weights on the edges specify the edge biases (illustrated by red). The graphs and the vertex loads on the top and the bottom left are identical, but the edge biases (illustrated by red arrows) are diﬀerent. As S2 has higher average load than S1 (LS

= 4/5), on both top and bottom, we create 3 units of balancing drift from S2 into S1 (to balance the gap between S2 and S1). The drift on bottom is orthogonal, while the one on top is not. On the right side, we see the resulting drifts on the sets in G’s decomposition tree (both trees are identical). Inside a node we depict the average load (as balls divided by bins) for the corresponding set. The drifts on top create an undesired relative drift from the underloaded set S11 to the overloaded set S12 (the horizontal dashed line). On the other hand, on bottom right, there is only a drift from S2 to S1 and the relative drift between any other pair of siblings is 0. E.g., the drift entering S11 and S12 is exactly in proportion to their sizes 2 and 3. So the drift does not interfere with balancing |LS

###### = 7/5 and LS

1

2

12|. The same holds for all other pairs of siblings except S1 and S2.

11 − LS

Many of the earlier results are surveyed in Mitzenmacher’s Thesis [Mit91] and in his survey with Richa and Sitaraman [MRS01]. A more recent survey is due to Wieder [Wie17].

In his thesis Mitzenmacher suggested the model of 1 + β choice for β < 1, where the algorithm is given two choices with probability β and only one choice with probability 1 − β. His motivation for introducing this model stems from a problem in queuing theory. Vöcking [Vöc03] show that for d-choice, non-uniform choices can improve over the greedy algorithm of [ABKU94], resulting in maximum load of Θ(log log(n)/d) (cf., Θ(log log(n)/log d)).

The heavily loaded case of the two-choice problem was ﬁrst analyzed in [BCSV06] (see a neat and short proof by Talwar and Wieder [TW14]). In [PTW15], Peres, Talwar and Wieder considered the 1 + β choice model for complete graphs and showed that there both gap and upper gap are Θ((log n)/β). The drift and potential methods introduced in this work allowed the authors to relate this result to the graphical case for expanders in [PTW15] and inspired methods used here as well.

### 2 Algorithm

Let G = (V,E) be the underlying graph for the graphical process and let k = k(G) denote the edgeconnectivity (the size of the minimum cut) of G. The algorithm consists of two parts: a preprocessing stage and an online allocation stage. The preprocessing stage takes G as input and computes a binary decomposition tree T of G, together with some information on how an edge should bias its allocation based on the imbalance in average load on certain siblings in T. This information is used to realize a simple online allocation strategy.

Let IT denote the set of internal nodes of T. For an internal node i ∈ iT, let S (i) and Sr(i) denote the subsets of V corresponding to the left (resp. right) child (i) (resp. r(i)) of i. The goal of each node i ∈ IT is to control |Lt(S (i)) − Lt(Sr(i))|, the diﬀerence in average load on S (i) and Sr(i) at the end of time t.

The preprocessing stage also outputs the following (ﬁxed) vectors for each edge e = (x,y) ∈ E.

- 1. A probability vector pe : IT ∪{∅} → [0,1] specifying the probability that e will determine the allocation based on comparing L(S (i)) and L(Sr(i)).

- 2. A direction vector σe : IT → ±1 indicating to which endpoint of e the ball should be assigned if L(S (i)) − L(Sr(i)) is positive.


Before we discuss the preprocessing steps, we ﬁrst describe the allocation strategy.

#### 2.1 An online allocation strategy

- At each time t + 1 for t = 0,1,2,..., the allocation strategy does the following. Allocation. Given a request for an edge e = (x,y):


- 1. Select an i ∈ IT ∪ {∅}, according to the precomputed distribution pe.
- 2. If i = ∅ allocate the ball randomly to either endpoint of e with probability 1/2.
- 3. Otherwise, consider the quantity σe(i)(Lt(S (i)) − Lt(Sr(i)).


- (a) If this is positive, allocate the ball to y.8
- (b) If this is negative, allocate the ball to x.
- (c) Otherwise if it is exactly zero, allocate the ball to an endpoint of e uniformly at random.


Update. Update Lt(S) for the sets S containing the vertex to which the ball was assigned.

8The vectors σ will satisfy σ(x,y)(i) = −σ(y,x)(i), so the allocation in independent of whether we write e = (x, y) or e = (y, x).

#### 2.2 Preprocessing

The preprocessing consists of four stages. In the ﬁrst stage we compute a Räcke cut-based decomposition R = (VR,ER,cR) tree for G, together with the ﬂow templates fuv for each ordered pair u,v ∈ V . In the second stage we use R to construct a binary decomposition tree T. In the third stage we compute a balancing drift and associated ﬂows corresponding to each node i ∈ IT. Finally we use these ﬂows to construct the vectors pe and σe required to run the allocation strategy.

###### 2.2.1 Step 1: Construct a Räcke decomposition.

Given G, compute a Räcke cut-based decomposition R = (VR,ER,cR) tree for G, together with the ﬂow templates fuv for each ordered pair u,v ∈ V , as deﬁned in Section 1.2. This is done using the algorithm of [HHR03] so that congestion ratio of G with respect to R is αG = O(log2 nlog log n).

###### 2.2.2 Step 2: From general tree to a binary one.

In this step, we convert R into a binary hierarchical decomposition tree T = (VT,ET) of G. The nodes of T will deﬁne the sets whose average load we will balance in the allocation strategy.

- 1. Apply the following step repeatedly to R until all non-leaf nodes have degree 2.
- 2. Choose a node i with p > 2 children j1,...,jp. Let w(h) = |Sj


h|/|Si| for h ∈ [p], so that ph=1 w(h) = 1.

- (a) If w(h) > 1/4 for some h, make jh the left child of i. Create a new right child b with the remaining

p − 1 children other than jh. The node b corresponds to the set Si \ Sj

h

.

- (b) Otherwise, arbitrarily partition {j1,...,jh} into two sets A and B so that w(A),w(B) ∈ [1/4,3/4]. Create two children a and b of i, where the children of a (resp. b) are the nodes in A (resp. B). The nodes a and b corresponds to sets ∪j∈ASj and ∪j∈BSj.


Clearly, T is binary. Also T and R have the same set of leaves as R is a contraction of T.

###### 2.2.3 Step 3: Deﬁning drifts and computing ﬂows.

Let IT denote the set of internal (non-leaf) vertices of T. For i ∈ IT, let (i) and r(i) denote its left and right children in T. Let β = 1/(8αG) and recall that k is the edge connectivity of G. For each i ∈ IT, we create a commodity i, and send

βk |S (i)||Sr(i)|

1(u ∈ S (i),v ∈ Sr(i)) (1)

κi(u,v) =

units of ﬂow in T from each leaf u ∈ S (i) to each leaf v ∈ Sr(i). Let di(z) denote the amount of commodity i entering vertex z, so that for each u ∈ S (i), v ∈ Sr(i) and w ∈ V \ Si, we have

di(u) = −βk/|S (i)|, di(v) = βk/|Sr(i)| and di(w) = 0. (2)

As we shall see, the allocation strategy on G will precisely produce the drift vector di or −di for balancing L(S (i)) and L(Sr(i)), where the sign depends on which one of these loads is higher.

Consider the ﬂow templates fuv for each pair u,v ∈ V in G, given by the oblivious routing associated with the tree R. Let gi be the ﬂow of commodity i produced in G by routing the ﬂows κi(u,v) using the ﬂow templates fuv. That is, for an edge e = (x,y) of G, let

gi(x,y) =

u,v∈V

fuv(x,y)κi(u,v). (3)

Note that the ﬂow gi only depends on the graph G (via R,T,{fuv}u,v∈V ). In particular, it does not depend on the current load vector Lt and hence is ﬁxed over time. We use these gi(x,y) to deﬁne pe and σe.

- 2.2.4 Step 4: Deﬁning pe and σe. For each edge e, and for each i ∈ IT, we set


σe(i) = sgngi(e) and pe(i) = |gi(e)|. (4)

Finally, set pe(∅) = 1 − i∈IT pe(i). This concludes the preprocessing9.

### 3 Analysis

In this section we show that the preprocessing stage produces pe,σe and an allocation strategy with the desired properties and use these to establish Theorem 1.1. To do so, we ﬁrst study the drifts realized by the algorithm and then establish congestion and concentration bounds.

- 3.1 Verifying the preprocessing We begin by showing that T is well-balanced.


Claim 3.1. Let a,b be two nodes in T such that a is an ancestor of b, and let q be the distance from a to b. Then |Sb| ≤ (3/4) q/2 |Sa|. In particular, T has depth O(log n).

Proof. Consider some path f,g,h of length 2 in T, where f is the ancestor of h. It suﬃces to show that either |Sh| ≤ (3/4)|Sg| or |Sg| ≤ (3/4)|Sf|. If g was a node in R, this follows by the well-balancedness of a Räcke tree for the edge (g,h). Otherwise g ∈/ R, and no matter whether (f,g) was produced according to rule (2a) or (2b) in Section 2.2.2, we have |Sg| ≤ (3/4)|Sf|.

| |
|---|


The demand vectors di satisfy a useful orthogonality property, as illustrated in Figure 2. For W ⊂ V , let di(W) = w∈W di(w) denote the total ﬂow of commodity i entering the set W.

- Lemma 3.2. For any i,j ∈ IT, with i = j we have that


di(Sr(j)) |Sr(j)|

di(S (j)) |S (j)|

= 0. (5)

−

For j = i we have

di(Sr(i)) |Sr(i)|

di(S (i)) |S (i)|

1 |S (i)|

1 |Sr(i)|

. (6)

−

= −βk

+

Proof. Fix i ∈ IT and let Ti denote the subtree of IT rooted at i. We ﬁrst consider j = i. Recall that the ﬂow of commodity i, satisfying (1) and (2), is only between nodes of Si and that di(w) = 0 for w ∈/ Si. So if j ∈/ Ti and i ∈/ Tj, then (5) holds trivially as Sj ∩ Si = ∅ and di(S (j)) = di(Sr(j)) = 0.

Next, if i ∈ Tj (and i = j) then Si is contained entirely in either S (j) or S (i). As the total commodity i ﬂow leaving Si is 0, this gives that di(S (j)) = di(Sr(j)) = 0.

Next, suppose j ∈ Ti (and j = i) and assume without loss of generality that j lies in the right subtree of

- i. Then positive ﬂow enters each vertex of Sj and the ﬂow entering S (j) is exactly


di(S (j)) =

di(u) = βk|S (j)| |Sr(i)|

. (7)

u∈S (j)

Similarly di(Sr(j)) = βk|Sr(j)|/|Sr(i)|, and the lemma follows. Likewise, if j lies in the left subtree of i (so that the ﬂow leaves S (j) and Sr(j)), the same argument holds, up to a change of sign.

Finally for j = i, we have di(S (j)) = −βk and di(Sr(j)) = βk, and the lemma follows.

9Note that σ(x, y) = −σ(y, x) as gi(x, y) = −gi(y, x) (being a ﬂow). This does not aﬀect the allocation strategy as writing e = (x, y) or e = (y, x) ﬂips both σe(i) and the x and y in steps 3(a)-3(c).

- Lemma 3.3. For any node j ∈ IT we have i∈I

T

|di(Sj)| ≤ 8βk = k/αG.

Proof. Fix a node j ∈ IT. For any i that lies in the subtree Tj rooted at j, we have that di(Sj) = 0 as di(u) = 0 for all u ∈/ Si, di(Si) = 0 and Si ⊆ Sj.

Next, consider any i such that j ∈/ Ti (and also i ∈/ Tj by the case above), then Sj ∩ Si = ∅ and we have that di(Sj) = 0 as di(w) = 0 for w ∈/ Si.

Thus it suﬃces to consider nodes i which are ancestors of j. Suppose, without loss of generality, that j is in the left subtree of i. Then, by Claim 3.1 and (7),

|di(Sj)| =

u∈Sj

di(u) ≤ βk|Sj|/|S (i)| ≤ βk(3/4) (dist(i,j)−1)/2 ,

where dist(i,j) is the distance between i and j. The result follows by summing up over all the ancestors i of

- j and using that (3/4)1/2 ≤ 7/8. We now show that pe is a valid probability vector.


| |
|---|


- Lemma 3.4. For every e ∈ E of the graph G, we have that i∈I


pe(i) ≤ 1.

T

Proof. Fix an edge e = (x,y) of G. Recall that for each node i ∈ IT, we deﬁned pi(e) = |gi(x,y)| in (4) where the ﬂow gi is obtained by mapping the commodity i ﬂow in R to G using the ﬂow templates as deﬁned in (3). So i∈I

pi(e) is exactly the total multi-commodity ﬂow through the edge e.

T

By the property of Räcke trees, it suﬃces to show that the total multi-commodity ﬂow through any edge (j,j ) of R is at most 1/αG times its capacity. Moreover as G is k edge-connected, each edge in R has capacity at least k, and it suﬃces to show that this is at most k/αG.

Let j be the child of j in R. Then the edge (j,j ) corresponds to path in T with j an ancestor of j . The ﬂow across (j,j ) in R of commodity i is due to demands κi(u,v) for all pairs (u,v) with exactly one of u or v is contained in Sj, i.e., |{u,v} ∩ Sj| = 1. For each i ∈ IT, the total commodity i ﬂow that leaves or enters the set Sj is exactly |di(Sj)| and hence by Lemma 3.3, the total ﬂow across (j,j ) is at most k/αG.

| |
|---|


#### 3.2 Realized ﬂows and drifts

The vectors pe, σe(i) are constructed so that the allocation strategy at each time achieves a certain drift vector. Fix a time t. Given a load vector Lt, for each i ∈ iT deﬁne

 

+1 if Lt(S (i)) > Lt(Sr(i)), −1 if Lt(S (i)) < Lt(Sr(i)), 0 otherwise.

QLt(i) =



Notice that using these QLt(i) our allocation strategy at time t + 1 as described in Section 2.1 can be expressed more compactly as follows. When edge e = (x,y) is requested, with probability pe(i), assign the ball to y with probability (1+σe(i)QLt(i))/2 and to x otherwise. In other words, the strategy creates a bias of σe(i)QLt(i) with probability pe(i), towards y upon request to (x,y) at time t + 1.

Summing up over i, the overall bias towards y upon the request to edge e = (x,y) is

gi(x,y)QLt(i), (8)

sgn gi(x,y) |gi(x,y)|QLt(i) =

bt(x,y) =

QLt(i)σe(i)pe(i) =

i∈IT

i∈IT

i∈IT

where the second equality uses the deﬁnition of σe(i) and pe(i) in (4).

In other words, the edge biases bt(x,y) are exactly realized by the sum of ﬂows gi(x,y) weighted by the signs QLt(i) which are based on the current loads.

Using this we can now describe the probability qt(y) that a vertex y ∈ V is assigned a ball at step t + 1.

Henceforth, we will focus on a ﬁxed time and drop the dependence on t in Lt,Lt,QLt,bt(x,y) and qt(y) for ease of notation. These quantities should always be viewed as functions of t.

- Lemma 3.5. At every time t, writing L = Lt, for each vertex y of G the allocation strategy assigns a ball to y at time t + 1 with probability

q(y) =

1 n

+

- 1

- 2m i∈I


T

di(y)QL(i).

Equivalently, the drift dt(y) = 2m(q(y) − 1/n) at time t at each node y is exactly i∈I

T

di(y)QL(i).

Proof. As each edge e is requested uniformly at random, by (8) the probability of allocating the ball to y is exactly

q(y) =

1 m

x∈N(y)

1 + b(x,y) 2

=

d 2m

+

- 1

- 2m x∈N(y) i∈IT


gi(x,y)QL(i).

As 2m = nd and x∈N(y) gi(x,y) is the commodity i ﬂow entering y, which by deﬁnition is exactly di(y), we obtain that

q(y) =

1 n

+

- 1

- 2m i∈I


T

di(y)QL(i).

| |
|---|


For a subset of vertices W ⊂ V , let qt(W) = w∈W qt(w) (denoted q(W) henceforth) denote the probability of allocating a ball at time t + 1 to some vertex in W.

We can now compute the relative drift between any two sibling sets S (i) and Sr(i).

- Lemma 3.6. For a node i ∈ IT and its children (i) and r(i), q(S (i))

|S (i)|

−

q(Sr(i)) |Sr(i)|

= −βkQL(i) 2m

1 |S (i)|

+

1 |Sr(i)|

.

Observe that this only depends on QL(i), i.e. on how they average loads on S (i) and Sr(i) compare, and not on anything else (this is exactly where the orthogonality property is useful). This will allow us to establish concentration bounds on the diﬀerence |L(S (i)) − L(Sr(i))|. Proof. By Lemma 3.5, we have that

q(S (i)) =

y∈S (i)

q(y) = |S (i)|/n +

j∈iT

dj(S (i))QL(j)/2m,

and an analogous expression for q(Sr(i)) with S (i) replaced by Sr(i). Together this gives,

q(S (i)) |S (i)|

−

q(Sr(i)) |Sr(i)|

=

- 1

- 2m j∈i


T

QL(j)

dj(S (i)) |S (i)|

−

dj(Sr(i)) |Sr(i)|

.

By the orthogonality property in Lemma 3.2, the only non-zero contribution in the sum above is due to the term j = i. Using (6) the result follows.

| |
|---|


- 3.3 Controlling the gap through concentration


With the results above, we are now ready to prove Theorem 1.1. To this end, we ﬁrst state a bound on the gap between the average load on sets corresponding to any two siblings in T. Recall that d and k are the degree and edge-connectivity of G.

- Lemma 3.7. Writing L = Lt, for any time t and any non-leaf node i ∈ IT, for every constant c > 0, Pr |L(S (i)) − L(Sr(i))| > 8(d/k)αG clog n = O(n−c).


Let us ﬁrst see how this directly implies Theorem 1.1.

Proof of Theorem 1.1. Fix any non-leaf node i ∈ IT and consider some child j ∈ { (i),r(i)} of i. Let j be the sibling of j. We ﬁrst observe that the diﬀerence between average load of siblings is no less than the diﬀerence for a parent-child pair. This follows as

L(Si) − L(Sj) |Sj |

= |Si| |Sj |

L(Sj) |Sj|

L(Sj) − L(Si) ≥ L(Sj) − L(Si) , (9)

L(Sj) − L(Sj ) =

−

where we use the fact that L(Si) = L(Sj) + L(Sj ), |Si| = |Sj| + |Sj | and |Si| ≥ |Sj |.

Fix some vertex u of G, and consider the path u = i0,i1,...,ih = r in T from the leaf u to the root r. As L(u) = L(u) for a leaf u and L(r) is the average load over V , the deviation of the load u from the global average is

h

h

) ≤

L(u) − L(r) =

###### ) − L(Si

###### ) − L(Si

L(Si

L(Si

) .

g−1

g−1

g

g

g=1

g=1

Applying Lemma 3.7 with c > 1, taking a union bound over the O(n) edges (i,j) ∈ ET and using (9), we get that w.h.p. |L(Si) − L(Sj)| ≤ (d/k)αG c log n for all edges (i,j) ∈ ET. As the height of T is hT = O(log n) by Claim 3.1, this gives that, w.h.p., for every vertex u,

L(u) − L(r) = O((d/k)αG log2 n). Recalling that αG = O(log2 nlog log n) gives the claimed result.

| |
|---|


- 3.4 Proof of the concentration estimate We now prove Lemma 3.7. We ﬁrst develop a concentration lemma to be used in our analysis.


2-point concentration. Consider the following set up. There are two bins, 1 and 2, associated with steady state probabilities π1,π2 which satisfy π1 + π2 = 1. At each time step a ball arrives and let t1, t2 denote the loads of the bins at the end of time t. In addition, there is ﬁxed parameter ε ≤ min(π1,π2)/2.

Suppose the allocation process at t + 1 is as follows: choose a parameter εt > ε (independent of future allocations, but possibly depending on the history of the process and external randomness) which almost surely satisﬁes εt ≤ max(π1,π2)/2. If t1/π1 > t2/π2, then allocate the ball to bin 1 with probability π1 − εt or to bin 2 otherwise. If t1/π1 > t2/π2, allocate the ball to bin 1 with probability π1 + εt or to bin 2 otherwise. Finally, if t1/π1 = t2/π2 allocate the ball to bin 1 with probability π1 or to bin 2 otherwise.

For any time t, let δ(t) = t1/π1 − t2/π2 denote the normalized diﬀerence in the loads of the bin. Then we have the following concentration bound for this 2-point process.

- Lemma 3.8. For any time t and any x ≥ 0 it holds that Pr[|δ(t)| ≥ x/ε] = O exp(−x/8) .


Proof. We deﬁne the potential function Φ(t) = cosh(αδ(t)), where α = ε/8. So Φ(0) = 1 initially at t = 0.

Fix a time t and let ∆Φ = Φ(t+1)−Φ(t) and denote δ = δ(t) and ∆δ = δ(t+1)−δ(t). Then, by Taylor expansion, and using (d/dx)cosh(x) = sinh(x) and (d/dx)sinhx = coshx,

∆Φ = sinh(αδ) α∆δ + (α∆δ)3/3! + ... + cosh(αδ) α(∆δ)2/2! + (α∆δ)4/4! + ... .

Let γ = 1/π1 + 1/π2. As ε ≤ max(π1,π2)/2 we have that γε ≤ 1. As either t1 or t2 rises by 1, we have |∆δ| ≤ γ, and hence |α∆δ| ≤ 1/2. Bounding |(α∆δ)i| ≤ (α∆δ)22−i+2 for i ≥ 2, and using that coshx − 1 ≤ |sinh(x)| ≤ coshx for all x,

∆Φ ≤ sinh(αδ)(α∆δ) + cosh(αδ)(α∆δ)2. We now bound E[∆δ] and E[(∆δ)2]. For δ > 0,

1 π1 − (π2 + εt)

1 π2

E(∆δ) = (π1 − εt)

= −εt

1 π2

1 π1

+

= −εtγ ≤ −εγ,

while for δ < 0, we have E[∆δ] = εtγ ≥ εγ. For δ = 0 we have E[∆δ] = 0. For δ > 0, we have

E[(∆δ)2] = (π1 − εt)

1 π1

2

+ (π2 + εt)

1 π2

2

= γ + εt(−1/π12 + 1/π22) ≤ γ + εtγ2 ≤ 2γ,

where the last step uses the fact that εtγ ≤ 1. The same bound also holds for δ < 0 and for δ = 0. This gives

E[∆Φ(t) | Φ(t)] ≤ α sinh(αδ)E[∆δ] + 2α2 cosh(αδ)E[(∆δ)2] ≤ −α|sinh(αδ)|εγ + 4α2γ cosh(αδ) ≤ −αεγ(Φ(t) − 1) + αεγΦ(t)/2 = −αεγ(Φ(t) − 2)/2.

Thus, taking expectation and using ∆(Φ(t)) = Φ(t + 1) − Φ(t) we obtain

E[Φ(t + 1)] ≤ αεγ + (1 − αεγ/2)E[Φ(t)]. Taking induction over t and recalling that Φ(0) = 1 we obtain

E[Φ(t)] ≤ 2 1 − (1 − αεγ2 )t + (1 − αεγ2 )t ≤ 2. The result now follows by applying Markov’s inequality to Φ(t).

| |
|---|


Proof of Lemma 3.7. We apply the set up above to bound L(S (i)) − L(Sr(i)) . Letting bin 1 correspond to S (i) and bin 2 to Sr(i), we restrict ourselves to the time steps when the ball is allocated to some vertex in Si. Let π1 = |S (i)|/|Si| and π2 = |Sr(i)|/|Si| so that π1 + π2 = 1.

By deﬁnition of q = qt, the probability of allocating the ball to S (i) conditioned on it being allocated to Si is q(S (i))/q(Si), and similarly q(Sr(i))/q(Si) for Sr(i).

Let us write π1 −εt = q(S (i))/q(Si) and π2 +εt = q(Sr(i))/q(Si). Dividing the ﬁrst and second equations by π1 and π2 and subtracting the ﬁrst from the second give that

εt

1 π1

1 π2

+

which by Lemma 3.6 equals

q(S (i)) π1q(Si)

q(Sr(i)) π2q(Si) −

= |Si| q(Si)

=

q(Sr(i)) |Sr(i)|

−

q(S (i)) |S (i)|

,

|Si| q(Si)

βkQL(i) 2m

1 |S (i)|

1 |Sr(i)|

1 q(Si)

βkQL(i) 2m

1 π1

1 π2

+

=

+

.

This yields εt = βkQL(i)/q(Si).

Since QL(i) ∈ {−1,1} and q(Si) ≤ 2|Si|/n (as q(v) ≤ d/m = 2/n for any vertex v), we deduce that |εt| ≥ βkn/(2m|Si|). We thus deﬁne

k 8dαG|Si|

βkn 2m|Si|

, (10)

=

ε :=

so that ε ≤ |εt|. Applying Lemma 3.8, we obtain

L(Sr(i)) π2 ≥ x/ε = O exp(−x/8) .

L(S (i)) π1 −

Pr

As π1 = |S (i)|/|Si|,π2 = |Sr(i)|/|Si|, and using the value of ε in (10), this becomes

Pr L(S (i)) − L(Sr(i)) ≥ 8x(d/k)αG = O exp(−x/8) , which implies the lemma.

| |
|---|


#### 3.5 Implementation

To implement the allocation strategy, the algorithm can maintain a dynamic table of size O(n) containing the load on each set S in the decomposition. At any time, upon an edge request e = (u,v), the algorithm samples i ∈ IT ∪ {∅} with the probability pe(i) and looks up the two table entries containing loads on S (i) and Sr(i). When a ball is assigned to some vertex v only the O(log n) entries for S with v ∈ S are updated.

Remark 3.9. In fact, the number of updates to the table per time step can be reduced to O(1). In the distributed implementation part below we show that the bound in Theorem 1.1 holds even if at any time the entry for the total load of any set S is not very accurate and can diﬀer from the actual load on S by O(|S|log n). We can use this slack to let each vertex v make a batch update to the entry for each S with v ∈ S only every O(nlog n) steps. As each vertex lies in O(log n) sets, the total number of batch updates is O(nlog n) per O(nlog n) steps, implying O(1) amortized update time per allocation step.

Finally, storing the vectors pe and σe does not require much memory either, as for each edge e, the vectors pe and σ(e) have support O(log n). This follows by the property of Räcke trees and the ﬂow templates that an edge e is used in fuv only if both endpoints of e lie in Sa(u,v) and Sa(u,v) where a(u,v) is the least common ancestor of u and v in T. As T has depth O(log n), for each edge e, there are only O(log n) relevant sets Si with pe(i) = 0. So the total memory used to store these (static) vectors is O(mlog n).

Distributed implementation. The implementation above assumed that each vertex had read/write access to a centralized table containing the loads L(S). We now consider a distributed setting where vertex maintains its own local table with possibly stale entries L(S) and give a distributed implementation that requires only O(1) amortized messages per allocation, with O(log n) bits per message. The key underlying observation is that allocation strategy is quite robust and does not require exact knowledge of the load L(S) on the sets S in the decomposition. In particular, the bound in Theorem 1.1 also holds when L(S) is inaccurate up to O(|S|log n) for each set S.

More precisely, suppose for any set Si, the allocation strategy is guaranteed to produces the balancing drift in the correct direction only when |L(S (i)) − L(Sr(i)| ≥ clog n and otherwise the direction can be arbitrary, i.e., if |L(S (i)) − L(Sr(i)| ≤ log n, then the sign QL(i) can be arbitrary. This aﬀects the gap |L(S (i)) − L(Sr(i)| in the 2-point concentration argument by only an additive clog n so that we now have

Pr |L(S (i)) − L(Sr(i))| ≥ 8x(d/k)αG + clog n = O exp(−x/8) . As (d/k)αG ≥ 1 this gives a similar tail bound as the original allocation strategy whenever x = Ω(log n).

So each vertex can maintain its own stale estimate of L(S) with error up to O(|S|log n). Moreover, as any set S has at most 2|S|/n probability of being assigned a ball at ant time, w.h.p., it suﬃces for a vertex needs to update its load entry for S in only O(nlog n) steps. Let us focus on a ﬁxed set S in the decomposition. The Räcke decomposition ensures that the induced graph G[S] on each such set S is connected. So after every interval of O(nlog n) time steps, the vertices in S can aggregate the information on how many balls in total were assigned to S during that interval. As S is connected, this can be implemented directly using O(|S|) messages of length O(log n) in total.

As the sum of the sizes of all the sets at a given level in the decomposition tree T is at most n and as T has depth O(log n), the total number of messages sent during an interval of size O(nlog n) is O(nlog n). This implies an amortized communication overhead of O(1) message per time step.

### 4 Lower Bounds

We describe various simple but instructive lower bounds. First we prove Theorem 1.2 in Section 4.1. Then, in Section 4.2 we show an Ω(log(n)/log log n) lower bound on the upper gap for bounded degree graphs. In particular this implies that on bounded degree expanders, the upper gap is roughly of the same order as the gap, in contrast with the complete graph where the upper gap is O(log log n) and the gap is Ω(log n).

We also remark that [PTW15] showed that for complete graphs, under the 1+β choice model for a ﬁxed β < 1, the upper gap is Ω(log n) and hence similar to the gap. Again this is in contrast to β = 1 (the 2-choice model) where the upper gap O(log log n) and gap is Ω(log n).

#### 4.1 Proof of Theorem 1.2

We show for any d-regular k edge-connected graph G, under any allocation strategy, the gap is Ω(d/k+log n) with at least constant probability.

The Ω(log n) bound follows from the following folklore argument. Fix any time t and consider any interval I of O(nlog n) steps just before t. For a ﬁxed vertex, at any time step, the probability that some edge incident to it is chosen is d/m = 2/n. Hence, by standard coupon-collector argument, with Ω(1) probability, there is some vertex v for which no incident edge is chosen during I. So during I, the load of v cannot change under any strategy, while the average load increases by log n.

Hence, to prove Theorem 1.2, it suﬃces to show the following.

- Lemma 4.1. Let G be any d-regular, k edge-connected graph. Then for any allocation strategy, and at any time t the gap is Ω(d/k) with constant probability. Proof. Let C = (S,S) be some minimum cut in G, and let S be the larger side with |S| ≥ n/2. Fix a time t and consider some time interval I of length T just before t. We specify T later. Let Y be the number of edges requested with both endpoints in S. As an edge is requested uniformly at random at each time, and

- as there are (d|S| − k)/2 such edges, we obtain E[Y ] = (d|S| − k)/2 · T/m = (|S| − k/d)T/n.

As k ≤ d and |S| ≥ n/2, this at least T/3, provided that n ≥ 6. By standard estimates, with at least constant positive probability, we have Y ≥ E[Y ]+

√

T. Conditioned on this event, the average load on vertices in S during I exceeds the stationary load of T/n by at least

Y |S|

−

T n ≥

E[Y ] +

√

T |S|

−

T n

=

(|S|d − k)T |S|dn

+

√

T |S|

−

T n

=

√

T |S|

−

kT nd|S|

.

Choosing T = cn2d2/k2 for small enough c and as |S| ≥ n/2, this is Ω(d/k).

| |
|---|


4.2 Upper gap for bounded degree graphs

Next we show that even for bounded degree expanders, under the greedy strategy the maximum load at time t is typically t/n + Ω(log˜ n). This is unlike for complete graphs where the upper gap is O(log log n).

Lemma 4.2. For any d-regular graph G = (V,E) with d = O(1), at any time t and for any allocation strategy, with constant probability the maximum vertex load is t/n + Ω(log n/log log n).

Proof. Fix a time t, and consider the interval I of length |E| = dn/2 just before t. Let t = t−|I| be time at the beginning of I, and let a = t /n denote the average load at t . Let s = log n/(4log log n). We will show that with constant probability, either t or t has upper gap Ω(log˜ n).

If some vertex has load a+s/4 at time t , then we are already done. Otherwise, by an averaging argument, there can be at most n/4 vertices with load at most a−s at time t . Call an edge bad if it is incident to such a vertex, and let B be the set of bad edges. As G is d-regular, |B| ≤ d(n/4) ≤ |E|/2.

As |I| = |E|, and each edge is requested uniformly and independently during I, with constant probability, some edge e ∈ E \B will be requested at least 4s times. If this event occurs, then for any allocation strategy, the load on some endpoint of e increases by at least 2s during I, and hence becomes at least a−s+2s = a+s

- at time t. On the other hand, the average load only increases by |I|/n = d/2 = O(1), to become a + d/2 at time t. This implies the result.




| |
|---|


#### Concluding Remarks

###### Our result gives, in particular, an allocation strategy with asymptotically polylogarithmic gap for any dregular d-connected graph. One may wonder whether this strategy gives any improvement in practical settings where the number of bins is not too large. To show that it indeed does, we conclude the paper with with a simulation result of our strategy for cycles, compared against the asymptotic behavior of the greedy strategy (Figure 3).

##### Maximum Gap of the Flow Strategy

180

| | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |


160

140

120

100

Gap

80

60

40

20

0

0 1000 2000 3000 4000 5000 6000 7000 8000 9000

Cycle Size (Bins)

Flow Strategy Gap Greedy Gap Asymp.

Figure 3: The gap for our ﬂow algorithm on cycles for the best possible Räcke tree, averaged over 32 runs of n2.5 balls for cycles of sizes n = 10 to 8400.

### Acknowledgments

We thank Guy Bensky and Shlomo Ron for their coding assistance in making our simulations.

### References

[ABKU94] Yossi Azar, Andrei Z. Broder, Anna R. Karlin, and Eli Upfal. Balanced allocations. In Symposium on theory of computing, pages 593–602, 1994.

[ACF+04] Yossi Azar, Edith Cohen, Amos Fiat, Haim Kaplan, and Harald Räcke. Optimal oblivious routing in polynomial time. J. Comput. Syst. Sci., 69(3):383–394, 2004.

[ACMR98] Micah Adler, Soumen Chakrabarti, Michael Mitzenmacher, and Lars Rasmussen. Parallel randomized load balancing. Random Structures & Algorithms, 13(2):159–188, 1998.

[AF09] Reid Andersen and Uriel Feige. Interchanging distance and capacity in probabilistic mappings. CoRR, abs/0907.3631, 2009.

[AK14] Roc Armenter and Miklós Koren. A balls-and-bins model of trade. American Economic Review, 104(7):2127–51, 2014.

[ANS20] Dan Alistarh, Giorgi Nadiradze, and Amirmojtaba Sabour. Dynamic averaging load balancing on cycles. In ICALP, volume 168 of LIPIcs, pages 7:1–7:16, 2020.

[BCSV06] Petra Berenbrink, Artur Czumaj, Angelika Steger, and Berthold Vöcking. Balanced allocations: The heavily loaded case. SIAM Journal on Computing, 35(6):1350–1385, 2006.

[CFM+98] Richard Cole, Alan Frieze, Bruce M. Maggs, Michael Mitzenmacher, Andréa W Richa, Ramesh Sitaraman, and Eli Upfal. On balls and bins with deletions. In International Workshop on Randomization and Approximation Techniques in Computer Science, pages 145–158. Springer, 1998.

[DR96] Devdatt P. Dubhashi and Desh Ranjan. Balls and bins: A study in negative dependence. BRICS Report Series, 3(25), 1996.

[God08] P. Brighten Godfrey. Balls and bins with structure: balanced allocations on hypergraphs. In Symposium on Discrete algorithms, pages 511–517, 2008.

[HHR03] Chris Harrelson, Kirsten Hildrum, and Satish Rao. A polynomial-time tree decomposition to minimize congestion. In Symposium on Parallel algorithms and architectures, pages 34–43, 2003.

[KLadH96] Richard M. Karp, Michael Luby, and F. Meyer auf der Heide. Eﬃcient pram simulation on a distributed memory machine. Algorithmica, 16(4):517–542, 1996.

[KP06] Krishnaram Kenthapadi and Rina Panigrahy. Balanced allocation on graphs. In SODA, volume 6, pages 434–443, 2006.

[Mit91] Michael Mitzenmacher. The Power of Two Choices in Randomized Load Balancing. PhD thesis, Harvard University, 1991.

[MRS01] Michael Mitzenmacher, Andrea W. Richa, and Ramesh Sitaraman. The power of two random choices: A survey of techniques and results. Combinatorial Optimization, 9:255–304, 2001.

[PTW15] Yuval Peres, Kunal Talwar, and Udi Wieder. Graphical balanced allocations and the (1 + β)-choice process. Random Struct. Algorithms, 47(4):760–775, 2015.

[Räc02] Harald Räcke. Minimizing congestion in general networks. In Foundations of Computer Science, FOCS, pages 43–52, 2002.

[Räc08] Harald Räcke. Optimal hierarchical decompositions for congestion minimization in networks. In Symposium on Theory of Computing, pages 255–264, 2008.

[RS98] Martin Raab and Angelika Steger. “balls into bins” — a simple and tight analysis. In International Workshop on Randomization and Approximation Techniques in Computer Science, pages 159–170. Springer, 1998.

[RST14] Harald Räcke, Chintan Shah, and Hanjo Täubig. Computing cut-based hierarchical decompositions in almost linear time. In Symposium on Discrete Algorithms, SODA, pages 227–238, 2014.

[Ste96] Volker Stemann. Parallel balanced allocations. In Proceedings of the eighth annual ACM symposium on Parallel algorithms and architectures, pages 261–269, 1996.

[TW14] Kunal Talwar and Udi Wieder. Balanced allocations: A simple proof for the heavily loaded case. In International Colloquium on Automata, Languages, and Programming, pages 979–990. Springer, 2014.

[Vöc03] Berthold Vöcking. How asymmetry helps load balancing. Journal of the ACM (JACM), 50(4):568–589, 2003.

[Wie17] Udi Wieder. Hashing, load balancing and multiple choice. Foundations and Trends in Theoretical Computer Science, 12:275–379, 2017.

