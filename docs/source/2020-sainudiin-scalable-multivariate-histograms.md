---
type: source
kind: paper
title: Scalable Multivariate Histograms
authors: Raazesh Sainudiin, Warwick Tucker, Tilo Wiklund
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2012.14847v1
source_local: ../raw/2020-sainudiin-scalable-multivariate-histograms.pdf
topic: author-sweep
cites:
---

# arXiv:2012.14847v1[stat.CO]29Dec2020

## Scalable Multivariate Histograms

##### Raazesh Sainudiin1,2, Warwick Tucker1,3, and Tilo Wiklund1,2

1 Department of Mathematics, Uppsala University, Uppsala, Sweden 2 Combient Competence Centre for Data Engineering Sciences, Uppsala University, Uppsala, Sweden 3 School of Mathematics, Monash University, Melbourne, Australia raazesh.sainudiin@math.uu.se warwick.tucker@monash.edu tilo.wiklund@math.uu.se

Abstract. We give a distributed variant of an adaptive histogram estimation procedure previously developed by the ﬁrst author. The procedure is based on regular pavings and is known to have numerous appealing statistical and arithmetical properties. The distributed version makes it possible to process data sets signiﬁcantly bigger than previously. We provide prototype implementation under a permissive license.

Keywords: density estimation · penalized likelihood · statistical regular paving · multivariate histogram trees · Apache Spark · MapReduce

### 1 Introduction

Suppose our random variable X has an unknown density f on Rd, then for all Borel sets A ⊆ Rd,

µ(A) := Pr{X ∈ A} =

f(x)dx .

A

Any density estimate fn(x) := fn(x;X1,X2,...,Xn) : Rd × Rd n → R is a map from Rd n+1 to R. The objective in density estimation is to estimate the unknown f from an independent and identically distributed (IID) sample X1,X2,...,Xn drawn from f. Density estimation is often the ﬁrst step in many learning tasks, including, anomaly detection, classiﬁcation, regression and clustering. Current density estimators do not computationally cope with large datasets. We use a MapReduce implementation of an optimally smoothed multivariate density estimator over a dense class of tree-based data-adaptive partitions.

#### 1.1 Plan of the paper

The rest of the paper is laid out as follows. Section 2 introduces the algebra for regular pavings (RPs), the arithmetic and algebra of real-mapped regular

pavings (R-MRPs) and statistical regular pavings (SRPs), and explains how various multivariate data-adaptive histogram estimates can be built using these structures. Section 2.2 illustrates the use of a novel partitioning strategy using a complementary pair of Priority-queued Markov chains (PQMCs) on the state space of SRPs with a reference to a proof of its asymptotic L1-consistency and a strategy for smoothing using penalized likelihoods. In Section 3, the main focus of this paper, we show how the algorithm can be distributed to scale to arbitrarily large datasets. In Section 4 we share references to the implementation in C++ and Apache Spark and evaluate the performance on simulated data.

### 2 Statistical regular pavings and histograms

This section introduces the notions of regular pavings (RPs), statistical regular pavings (SRPs) and real mapped regular pavings (R-MRPs), and explains how a histogram density estimate can be built using these tree based and arithmetically amenable data structures.

#### 2.1 Regular pavings (RPs)

Let x := [x,x] be a compact real interval with lower bound x and upper bound x, where x ≤ x. Let the space of such intervals be IR. The width of an interval x is wid(x) := x − x. The midpoint is mid(x) := (x + x)/2. A box of dimension d with coordinates in ∆ := {1,2,...,d} is an interval vector with ι as the ﬁrst coordinate of maximum width:

x := [x1,x1] × ... × [xd,xd] =: ⊗

[xj,xj], ι := min argmax

(wid(xi)) .

j∈∆

i

The set of all such boxes is IRd, i.e., the set of all interval real vectors in dimension d. A bisection or split of x perpendicularly at the mid-point along this ﬁrst widest coordinate ι gives the left and right child boxes of x

xL := [x1,x1] × ... × [xι,mid(xι)) × [xι+1,xι+1] × ... × [xd,xd] , xR := [x1,x1] × ... × [mid(xι),xι] × [xι+1,xι+1] × ... × [xd,xd] .

Such a bisection is said to be regular. Note that this bisection gives the left child box a half-open interval [xι,mid(xι)) on coordinate ι so that the intersection of the left and right child boxes is empty. A recursive sequence of selective regular bisections of boxes, with possibly open boundaries, along the ﬁrst widest coordinate, starting from the root box xρ in IRd is known as a regular paving [5] or n-tree [12] of xρ. A regular paving of xρ can also be seen as a binary tree formed by recursively bisecting the box xρ at the root node. Each node in the binary tree has either no children or two children. These trees are known as plane binary trees in enumerative combinatorics [13, Ex. 6.19(d), p. 220] and as ﬁnite, rooted binary trees (frb-trees) in geometric group theory [9, Chap. 10].

ρ

ρ

ρL ρR

|xρ|
|---|


|xρL|xρR|
|---|---|


ρ

ρ

ρ

ρR

ρLL ρLR

|xρLR|xρR|
|---|---|
|xρLL| |


ρLL ρRL ρRR

ρLL ρLR ρRL ρRR

ρLRL ρLRR

|xρLR|xρRR|
|---|---|
|xρLL|xρRL|


|xLRLρ|xLRRρ|xρRR|
|---|---|---|
|xρLL| |xρRL|


xLRRρ

xLRLρ

Fig. 1. A sequence of selective bisections of boxes (nodes) along the ﬁrst widest coordinate, starting from the root box (root node) in two dimensions, produces an RP.

The relationship of trees, labels and partitions is illustrated in Figure 1 via a sequence of bisections of a square (2-dimensional) root box by always bisecting on the ﬁrst widest coordinate.

Let N := {1,2,...} be the set of natural numbers. Let the j-th interval of a box xρv be [xρv,j,xρv,j], the volume of a d-dimensional box xρv be vol(xρv) = N}, the set of all leaf nodes be L and the set of internal nodes or splits be V˘(s) := V(s) \ L(s). The set of leaf boxes of a regular paving s with root box xρ is denoted by xL(s) and it speciﬁes a partition of the root box xρ. Let Sk be the set of all regular pavings with root box xρ made of k splits. Note that the number of leaf nodes m = |L(s)| = k + 1 if s ∈ Sk. The number of distinct binary trees with k splits is equal to the Catalan number Ck. For i,j ∈ Z+, where Z+ := {0,1,2,...} and i ≤ j, let Si:j := ∪jk=iSk be the set of regular pavings with k splits where k ∈ {i,i+1,...,j}. Let the set of all regular pavings be S0:∞ := limj→∞ S0:j.

- d j=1(xρv,j − xρv,j), the set of all nodes of an RP be V := ρ ∪ {ρ{L,R}j : j ∈


Statistical regular pavings (SRPs) A statistical regular paving (SRP) denoted by s is an extension of the RP structure that is able to act as a partitioned ‘container’ and responsive summarizer for multivariate data. An SRP can be used to create a histogram of a data set. A recursively computable statistic [1,3] that an SRP node ρv caches is #xρv, the count of the number of data points that fell into xρv. A leaf node ρv with #xρv > 0 is a non-empty leaf node. The set of non-empty leaves of an SRP s is L+(s) := {ρv ∈ L(s) : #xρv > 0} ⊆ L(s).

Figure 2 depicts a small SRP s with root box xρ ∈ IR2. The number of sample data points in the root box xρ is 10. Figure 2(a) shows the tree, including the count associated with each node in the tree and the partition of the root box represented by the leaf boxes of this tree, with the sample data points superimposed on the boxes. Figure 2(b) shows how the density estimate is computed

##### from the count and the volume of leaf boxes to obtain the density estimate fn,s as an SRP histogram.

ρ

#xρ = 10

#xρL = 5 #xρR = 5

ρR

ρL

#xρLL = 2 #xρLR = 3

ρLL ρLR

xρLR

xρR

xρLL

(a) An SRP tree and its constituents.

ρ

5

10 × 1/12 = 1

ρL ρR

10 × 1/14 = 0.8 103 × 1/14 = 1.2

2

ρLL ρLR

![image 1](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile1.png>)

![image 2](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile2.png>)

![image 3](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile3.png>)

![image 4](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile4.png>)

![image 5](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile5.png>)

![image 6](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile6.png>)

![image 7](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile7.png>)

(b) An SRP histogram fn,s.

Fig. 2. An SRP and its corresponding histogram.

An SRP histogram is obtained from n data points that fell into xρ of SRP s

- as follows:

fn,s(x) = fn(x) =

ρv∈L(s)

11xρv

(x) n

#xρv vol(xρv)

. (1)

It is the maximum likelihood estimator over the class of simple (piecewiseconstant) functions given the partition xL(s) of the root box of s. We suppress subscripting the histogram by the SRP s for notational convenience. SRP histograms have some similarities to dyadic histograms (for eg. [6, chap. 18], [7]). Both are binary tree-based and partition so that a box may only be bisected

- at the mid-point of one of its coordinates, but the RP structure restricts partitioning further by only bisecting a box on its ﬁrst widest coordinate in order to


make S0:∞ closed under addition and scalar multiplication and thereby allowing for computationally eﬃcient computer arithmetic over a dense set of simple functions. See [4] for statistical applications of this computer tree arithmetic, including conditional density regression, 1 − α conﬁdence sets and associated tail probabilities, and model averaging across multivariate histograms with diﬀerent partitions.

The set of regularly paved real-valued simple functions on xρ ∈ IRd satisﬁes the conditions of a Stone-Weierstrass theorem and is therefore dense in C(xρ,R), the algebra of real-valued continuous functions over xρ [4, Theorem 4.1]. This ensures that histograms obtained from statistical regular pavings subject to an

asymptotically L1-consistent partitioning strategy can uniformly approximate any continuous density f : xρ → R. Note that S0:∞, the set of RP tree partitions, contains the set of dyadic partitions of xρ represented by complete dyadic binary trees: {S0,S2,S4,S8,...} ⊂ S0:∞. Thus S0:∞ can be used in principle to obtain any σ-additive measure using standard measure-theoretic constructions (but such constructions without eﬃciency considerations may be limited in practice due to ﬁnite machine memory and computing time).

#### 2.2 Priority-queued Markov chains

The pseudo-code to generate sample paths from a generic priority-queued Markov chain (PQMC) over the state space of statistical regular pavings is given in Algorithm 1. A leaf node of a statistical regular paving (SRP) is splittable if it contains data and the child nodes from the split can be represented in the computer (as described in the next paragraph). A PQMC is a Markov chain on SRPs whose transition probabilities are given by ordering the elements of L (s), the splittable leaf nodes of the current SRP state s, by a randomized queue that is prioritized according to a given priority function ψ : L (s) → R. This priorityqueued collection of splittable leaf nodes is used to select the next node to be split from argmaxρv∈L (s) ψ(ρv), the set of splittable leaf nodes of s which are equally ‘large’ when measured using ψ. If there is more than one such ‘largest’ node the choice is made uniformly at random from this set; this is the ‘randomized’ aspect of the process. Three criteria can be speciﬁed to stop the PQMC. A straightforward stopping condition is to stop partitioning when the number of leaves in the SRP reaches a speciﬁed maximum m. The other stopping condition relates to the priority function so that partitioning stops when the value of the largest node under the priority function ψ is less than or equal to a speciﬁed value ψ. A PQMC will also stop partitioning if there are no splittable leaf nodes in the SRP.

The output of PQMC(s,ψ,ψ,m) algorithm is [s(0),s(1),...,s(T)], a sequence of SRP states giving a sample path from the PQMC {S(t)}t∈Z+

on S0:m−1, such that L (s(T)) = ∅ or ψ(ρv) ≤ ψ ∀ρv ∈ L (s(T)) or |L(s(T))| ≤ m and T is a corresponding random stopping time. Care must be taken in deﬁning splittable nodes as well as the values of the stopping parameters ψ and m, to ensure that ψ(ρv) ≤ ψ ∀ρv ∈ L (s(T)) and |L(s(T))| ≤ m. If the initial state S(t = 0) is the root s ∈ S0 then PQMC {S(t)}t∈Z+

on S0:m−1 satisﬁes S(t) ∈ St for each t ∈ Z+, i.e., the state at time t has t + 1 leaves or t splits. Note that the initial state can be speciﬁed by a sample from any distribution on S0:m−1. In fact, we will use a distribution deﬁned from sample paths of one PQMC with a speciﬁc priority function to initialize several independent PQMCs with a diﬀerent and complementary priority function to ﬁnd our density estimate as described next.

Statistically Equivalent Blocks PQMC or SEB-PQMC A statistically equivalent block (SEB) partition of a sample space is some partitioning scheme that results in equal numbers of data points in each element (block) of the

###### ALGORITHM 1: PQMC(s, ψ, ψ, m)

input : s, initial SRP with root box xρ, x = (x1, x2, . . . , xn), a data burst of size n, ψ : L (s) → R, a priority function, ψ, maximum value of ψ(ρv) ∈ L (s) for any splittable leaf node in the

ﬁnal SRP,

m, maximum number of leaves in the ﬁnal SRP.

output : a sequence of SRP states [s(0), s(1), . . . , s(T)] such that L (s(T)) = ∅

or ψ(ρv) ≤ ψ ∀ρv ∈ L (s(T)) or |L(s(T))| ≤ m .

initialize: xρ x, make xρ such that ∪ni xi ⊂ xρ if domain knowledge or historical data, s xρ, specify the root box of s, s ← [s]

while L (s) = ∅ & |L(s)| < m & ψ argmaxρv∈L (s) ψ(ρv) > ψ do

ρv ← random_sample argmax

ψ(ρv) // sample uniformly from nodes with largest ψ

ρv∈L (s)

s ← s with node ρv split // split the sampled node and update s s.append(s) // append the new SRP state with an additional split

end

partition [14] (except possibly in blocks on the boundary of the partitioned space). A statistically equivalent blocks (SEB)-based SRP partitioning scheme speciﬁed by the PQMC with (i) priority function ψ(ρv) = #xρv, i.e., the number of sample points associated with a node ρv, (ii) ψ-related stopping condition ψ = # and (iii) m, is denoted by SEB-PQMC. Thus, at stopping time T, the SRP s realized by the SEB-PQMC will be such that either L (s) = ∅ or |L(s)| ≤ m or #xρv ≤ # ∀ρv ∈ L (s). The operation may only be considered to be successful if |L(s)| ≤ m and #xρv ≤ # ∀ρv ∈ L (s). Care must be taken to ensure that the operation is successful. Therefore, an SEB-PQMC can be used to create a ﬁnal SRP at stopping time T such that each leaf node has at most # of the sample data points associated with it and the total number of leaves is at most m. Intuitively, SEB-PQMC prioritizes the splitting of leaf nodes with the largest numbers of data points associated with them.

Unfortunately, under an SEB-PQMC partitioning strategy over SRPs, the nodes with least data associated with them will remain unsplit for longer (and will possibly never be split). This tends to result in relatively large regions of very low density in the tails of the density estimate fn formed from the SRP. Figure 3 shows two partitions of an SRP associated with a highly correlated dataset super-imposed on it. As the number of leaves in the partition increases from 20 (Figure 3(a)) to 40 (Figure 3(b)), large sub-boxes containing very little sample data remain unsplit. The eﬀect can be especially distorting to the resulting histogram when the axis-aligned root box required by the SRP is a poor ﬁt to the data (when large areas of the root box contain no data points). Thus, we

![image 8](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile8.png>)

![image 9](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile9.png>)

![image 10](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile10.png>)

![image 11](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile11.png>)

(a) 20 leaves. (b) 40 leaves. (c) 20 leaves. (d) 40 leaves.

Fig. 3. Partition using an SEB-PQMC and SPC-PQMC.

would like to carve out empty space within the root box while remaining in S0:∞. The next PQMC ameliorates this undesirable feature of SEB-PQMC and can be used collaboratively with SEB-PQMC to still ensure asymptotic L1 consistency of the joint partitioning strategy.

Support Carving PQMC or SPC-PQMC A support-carving (SPC) SRP partitioning scheme speciﬁed by the PQMC with (i) ψ(ρv) = Ξ(ρv) = (1 − #xρv/n)vol(ρv), the SPC priority function which prioritizes node ρv according to the relative lack of its empirical measure when further scaled by its volume, (ii) ψ-related stopping condition Ξ and (iii) maximum number of leaves mΞ, is denoted by SPC-PQMC. Using SPC-PQMC to carve out “empty space” in the complement of the empirical support can be thought of as an ‘inversion’ of the SEB-PQMC: instead of prioritizing splitting of nodes with the largest number of data points associated with them as done by SEB-PQMC, the SPC-PQMC prioritizes splitting of non-empty leaf nodes with large boxes but few data points and thus is likely to result in one of the child nodes being devoid of any sample data. Hence, the two PQMCs are thought to be complementary. The carving

- eﬀect is illustrated in Figure 3. The partitions are created for the same set of correlated data shown in Figure 3 using SPC-PQMC. Figures 3(c) and 3(d) show the partition when the SRP has 20 and 40 leaves, respectively. Partitioning is concentrated in the regions of sparse sample data and the eﬀect is to reduce the size of the sub-boxes of the partition into which these sparse data points fall, in eﬀect more tightly enclosing the support of the data as desired while still


remaining in S0:∞.

Algorithm 1 with the SPC priority function Ξ can be used to obtain a core support-carved path in S0:mΞ by initializing from the root SRP s ∈ S0 through the procedure PQMC(s,Ξ,Ξ,mΞ) with Ξ = 0.0. Thus, the partitioning process of this core SPC-PQMC only stops when the SRP has mΞ leaves or aborts if there a no splittable nodes. More general support-carved paths can be generated by specifying Ξ > 0.0 or imposing constraints on the minimum volume of splittable nodes if deemed appropriate for the underlying data generation process.

Joint exploration An SPC-PQMC of Section 2.2 alone will not give an eﬀective data-driven partitioning strategy, but used in conjunction with an SEB-PQMC it can improve the SRP histogram. An initial SPC-PQMC can be run for a short

![image 12](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile12.png>)

![image 13](<2020-sainudiin-scalable-multivariate-histograms_images/imageFile13.png>)

- Fig. 4. Two histogram density estimates for the standard bivariate Gaussian density. The left ﬁgure shows a histogram with 1485 leaf nodes where # = 50 and the histogram on the right has # = 1500 resulting in 104 leaf nodes.


time (specifying Ξ = 0.0 and a relatively low value of mΞ, say a small fraction of the total number of leaves m), followed by an SEB-PQMC. The empty elements of the partition ‘carved out’ will be ignored by the SEB-PQMC, under which partitioning will be concentrated on the areas where most of the sample data has fallen. The core support-carved path from SPC-PQMC over S0:mΞ through PQMC(s,Ξ,Ξ,mΞ) with Ξ = 0.0 will be used to determine cΞ many spread-out initial conditions for launching multiple independent SEB-PQMCs. It is along these cΞ many joint SPC/SEB-PQMC paths, which may be viewed as a system of cΞ many SEB-PQMC tributaries spread along the core support-carved path of the SPC-PQMC, that we conduct MAP estimation for a given τ-speciﬁc prior by simply identifying the SRP state s with the highest log-posterior value. The search for the density estimate is conducted sequentially along each of the SPC/SEB-PQMC paths. The cΞ many initial conditions from the core supportcarved path for launching the SEB-PQMCs, should be well spread out in order to facilitate a better search strategy over S0:m, and in particular, contain the SEB-PQMC launched from the root node as one of its joint SPC/SEB-PQMC paths. In essence, we can view the joint exploration as one that will necessarily improve upon the estimate found by the SEB-PQMC initialized from the root node (which satisﬁes the three conditions of [8] and thus asymptotically L1consistent as shown in [10]).

Smoothing Figure 4 shows two diﬀerent SRP histograms constructed using two diﬀerent values of # for the same dataset of n = 105 points simulated under the standard bivariate Gaussian density. A small # produces a histogram that is under-smoothed with unnecessary spikes (Fig. 4 left) while the other histogram with a larger # used as the SEB stopping criterion is over-smoothed (Fig. 4 right). We will use the leave-one-out cross-validation to choose an optimally smoothed density.

Let x1,...,xn be the sample data, L(fn) be the likelihood of the data given SRP s, m = m(s) = |L(s)| be the number of cells or leaf boxes in the partition given by the SRP s, i.e., m = k + 1 if s ∈ Sk. For a given τ, ﬁnding the regularized (penalized) maximum likelihood estimate, amounts to solving the following maximization problem over S0:∞:

m(s) τ

log L(fn) −

.

fn,τ := argmax

log(π(s;τ)) = argmax

s∈S0:∞

s∈S0:∞

We will solve this smoothing problem by minimizing Stone’s leave-one-out cross-validation score J(τ), a nearly unbiased estimator of the expected L2 loss

(fn,τ(x) − f(x))2dx (eg. [15]), given by:

n

2 n

J(τ) = (fn,τ(x))2 dx −

fn,τ(−i)(xi) ,

i=1

where fn,τ(−i) is the estimate obtained from the data set by leaving out xi.

### 3 Going distributed

Simply computing multiple histograms in parallel has a number of limitations. First of all the number of histograms to compute will typically be relatively small. More importantly one is still limited by the memory capacity of each individual machine, since each histogram would be based on all data points.

For simplicity we will consider only axis parallel splits through cell centres, with respect to a priority depending on volume and count (this covers support carving and SEB PQMCs). The idea generalizes to priority functions that depend on any recursively computable statistic and splitting hyper-planes that may depend on some appropriate function of both the cell and the data points it contains.

Recall that Algorithm 1 proceeded roughly as follows: given a sequence x = (x1,...,xN) of (data) points in Rd produce s(0),s(1),... the sequence of partitions given by splitting according to some priority ψ: N×R≥0 → R≥0 starting at any s(0). Thus s(n + 1) equals s(n) with one cell split, according to the highest priority assigned by ψ. Schematically it thus proceeds as in Algorithm 2.

This is inherently sequential; modulo special properties of the priority functions one needs to split the current most high priority cell before being able to determine which cell to split next. One can make the procedure parallel by using two basic observations. Firstly, from s(n) one can (again sequentially) reconstruct the path s(n),s(n − 1),...,s(0) without knowing x. Following the path backward entails a sequence of mergers of sibling leafs as opposed to a sequence of splits. To get the ﬁnal path one merges in order of least priority of the parent.

Both count and volume, and thus the priority ψ, for any internal node can be computed by adding the counts and volumes of its children. Knowing only leaf counts and volumes one can therefore determine the last node to have been split. This is summarized in Algorithm 3 and illustrated in Figure 5.

- ALGORITHM 2: High level sketch of sequential splitting procedures

input : ψ: Count × Volume → R≥0, a priority function, x1, . . . , xN, (data) points in Rd, s(0), initial SRP, ψ, maximum priority for any cell node in ﬁnal output

output : Increasing (reﬁning) s(0), . . . , s(K), cells of s(K) have priority below ψ initialize: r ← s(0) while r has any cell of priority above ψ do

output r r ← r with the cell of highest priority split

end output r

- ALGORITHM 3: Backtracking from an intermediate SRP


input : ψ: Count × Volume → R≥0, a priority function,

s(0), “intermediate” SRP output : Decreasing (coarsening) s(0), s(1), . . . , s(K), with s(K) trivial initialize: r ← s(0) while r has more than one cell do

output r p ← parents of leaf nodes in r w ← priority (ψ) of all p based on volume/count of children r ← r with children of the least priority node according W merged

end output r

The second observation is that given a threshold c > 0 the tree S given by starting at s(0) and splitting leafs in an arbitrary order until all have a priority less than c will satisfy S = s(k) for some k. This is most easily seen by letting S = s(l) where l = min{k | all cells in s(k) priority below c} and noting that S = S . The last statement holds since any cell split to get S will sooner or later have to be split when constructing S , and vice versa. Formally this follows by induction on the depth, within the tree, of the cell.

9 5

3 2 2

4 2 1

2

9 5

- 3

9 5

- 4 2


3

4 2 1

2

9 5 3

9

- Fig. 5. Illustration of Algorithm 3, each tree is an SRP with nodes labelled with its priority and priorities of inner nodes computed recursively


This gives us the freedom to pick the order in which cells are split. In particular we can split multiple cells at once. Using the ﬁrst observation the sequence of intermediary trees can be reconstructed. While this reconstruction is again sequential, performing mergers will generally be faster than splitting, since the latter involves traversals of all data points in the cell.

Once we can split cells simultaneously one may as well split all nodes with a priority over the threshold c. Note that any intermediate SRP computed this way need not lie along the path output by the original procedure; a node may well split into two where at least one has a higher priority than something split simultaneously (see Figure 6).

The path produced by Algorithm 2 can now be found using Algorithm 4 followed by Algorithm 3. This should yield a gain in performance when the number of data points is large, so that a merge is signiﬁcantly faster than a split, assuming one can perform all splits in each iteration in parallel.

- ALGORITHM 4: High level sketch of parallel splitting procedures input/output: As in Algorithm 2


initialize : r ← s(0) while r has any cell of priority above ψ do

r ← r with all cells of priority above ψ split

end output r

9

9 5 3

9 5

9 5 4 2

3

3

4 2 1

2

9

9 5 3

9 5 4 2

3 2 2

9 5

3 2 2

4 2 1

2

9 5

3 2 2

4 2 1

2

- Fig. 6. Illustration of sequential (upper) and parallel (lower) splitting procedures, each tree represents an SRP with each node labeled by the priority of that node

In order for the procedure outlined above to translate into a distributed algorithm one needs a distributed representation that allows for eﬃcient distributed and parallel computation of how a given set of cells split.

The way we achieve this is by storing the current tree implicitly by tagging each data point by the cell in which it lies. That is to say, the points (x1,...,x6) and partition {A,B,C} in Figure 7 would be represented by the sequence (A,x1),(A,x2),(B,x3),(C,x4),(B,x5),(A,x6).

|A x1<br><br>x2<br><br>x6|B<br><br>x3 x5<br><br>|
|---|---|
| |C<br><br>x4|


- Fig. 7. Partitioned points represented by (A, x1), (A, x2), (B, x3), (C, x4), (B, x5), (A, x6)


Counting the current number of points in each cell is now a simple reduce operation available in, for example, Apache Spark under the name countByKey. The resulting map (counting the number of points for each cell) can either be collected to a single machine or itself remain distributed. It involves communication proportional to the current number of non-empty cells; in the worst case scenario every machine has to send its counts for each non-empty cell.

As volume is a function only of the cell this gives enough information for determining which cells needs to be split. Simply compute the priority (a function

of count and volume) and ﬁlter to get only those cells with a priority exceeding the predetermined threshold c.

Once one has determined which cells to be split getting the new partition is a point-wise operation. For each pair (A,x) (point x in cell A) one checks if A is to be split and if so on which side of the splitting hyper plane x lies. If x lies below produce the pair (A ,x) where A is the lower part (relative to the hyper plane) of A and otherwise produce (A ,x) where A is the upper part of A.

Most of this computation ﬁts directly into the MapReduce framework since it simply applies a function point-wise (thus a map operation). How to communicate of cells to be split depends on how the resulting map was stored; either one broadcasts it from a single machine or performs a distributed join operation.

- ALGORITHM 5: MapReduce-friendly parallel splitting procedure


input : ψ: Count × Volume → R≥0, a priority function, x1, . . . , xN, (data) points in Rd, ψ, maximum priority for any cell node in ﬁnal output

output : SRP with cells of priority below ψ and cell count corresponding to the

number of points in x1, . . . , xN in the cell

initialize: ρ ← root cell y ← [(ρ, x1), . . . , (ρ, xN)] // distributed array c ← [(ρ, N)]

while c has any cell/count pair with priority above ψ do // Implemented as a distributed map operation foreach (a, x) ∈ y do

if ψ(count of a in c, volume of a) > ψ then if x is below splitting hyperplane of a then

a ← subcell of a below splitting hyperplane

end else

a ← subcell of a above splitting hyperplane

end replace (a, x) by (a , x)

###### end

end // Implemented as a distributed reduce operation c ← [ ] foreach (a, x) ∈ y do

increment count in c at a by 1 (adding key a if needed) end

end output SRP with leaves/counts corresponding to cells/counts in c

The procedure can be improved by pruning pairs corresponding to cells with a priority below the threshold. The relevant computations are already performed when determining, for each tuple, whether or not the cell is one to be split (see

Algorithm 5). Filtering these points avoids repeating this check in subsequent iterations; the threshold remains ﬁxed so these cells will not be split in a future iteration either.

- ALGORITHM 6: Optimization of Algorithm 4


while c has any cell/count pair with priority above ψ do // Now becomes a map and filter operation foreach (a, x) ∈ y do

if ψ(count of a in c, volume of a) > ψ then

compute new cell a as before replace (a, x) by (a , x)

end else

delete (a, x) end

end update c as before, keeping counts for cells that have passed threshold

end output SRP with leaves/counts corresponding to cells/counts in c

For good performance one needs also a good representation for the cells in the distributed sequence of cell/point tuples. For our purposes a convenient representation is given by identifying cells with nodes in the (inﬁnite) plane binary tree as described in Section 2 and illustrated in Figure 1.

For practical purposes such a node can be identiﬁed with a positive natural number as follows: the root node is assigned number 1, the left sub-child of the node with number n is assigned the number 2n, and the right child of the node with number n is assigned number 2n+1. This is simply a binary encoding given by an initial 1 followed by the unique path from the root node; left steps are encoded by 0 and right steps are encoded by 1.

Using multiple precision integer types (as provided by for example gmp[2]) this is yields a fairly compact representation (bits proportional to tree depth) where many operations can be implemented in terms of bit-level operations. For example, passing to ancestors corresponds to taking right shifts and the depth (distance to the root node) is the index of the most signiﬁcant bit.

### 4 Implementation and Results

A complete, though non-parallel, C++ implementation of regular paving trees is available in the open source library mrs2 [11]. Our reference Scala implementation of the parallel density estimation procedure on top of Apache Spark is also publicly available [16].

Motivated by an industrial problem in fraud detection, we simulated n = 13 × 107 points in 2 and 10 dimensions from a multivariate density. A typical

computation on an Apache Spark cluster with 5 Workers (totaling 30.0 GB Memory and 4.4 Cores) in 2 and 10 dimensions took about 1.79 and 5.8 hours with estimated L1 errors of 0.03 and 1.13, respectively. Density estimates for such large datasets cannot be obtained in a single commodity machine.

### Acknowledgements

This work was initiated with support from project CORCON: Correctness by Construction, Seventh Framework Programme of the European Union, Marie Curie Actions-People, International Research Staﬀ Exchange Scheme (IRSES) with counter-part funding from the Royal Society of New Zealand. It is completed with support from Combient Competence Centre for Data Engineering Sciences. RS thanks Nina Nowak and Guillermo Padres for inspiring discussions on the industrial needs for distributed multivariate density estimators.

### References

- 1. Fisher, R.A.: Theory of statistical estimation. Mathematical Proceedings of the Cambridge Philosophical Society 22, 700–725 (1925)
- 2. Granlund, T., the GMP development team: GNU MP: The GNU Multiple Precision Arithmetic Library, http://gmplib.org/
- 3. Gray, A.G., Moore, A.W.: Nonparametric Density Estimation: Towards Computational Tractability. In: SIAM International Conference on Data Mining. pp. 203–

211. SIAM, San Francisco, California, USA (2003)

- 4. Harlow, J., Sainudiin, R., Tucker, W.: Mapped regular pavings. Reliable Computing 16, 252–282 (2012)
- 5. Kieﬀer, M., Jaulin, L., Braems, I., Walter, E.: Guaranteed set computation with subpavings. In: Kraemer, W., Gudenberg, J. (eds.) Scientiﬁc Computing, Validated Numerics, Interval Methods, Proceedings of SCAN 2000, pp. 167–178. Kluwer Academic Publishers, New York (2001)
- 6. Klemelä, J.: Smoothing of Multivariate Data: Density Estimation and Visualization. Wiley, Chichester, United Kingdom (2009)
- 7. Lu, L., Jiang, H., Wong, W.H.: Multivariate density estimation by bayesian sequential partitioning. Journal of the American Statistical Association 108(504), 1402–1410 (2013)
- 8. Lugosi, G., Nobel, A.: Consistency of Data-Driven Histogram Methods for Density Estimation and Classiﬁcation. The Annals of Statistics 24(2), 687–706 (1996)
- 9. Meier, J.: Groups, Graphs and Trees: An Introduction to the Geometry of Inﬁnite Groups. Cambridge University Press, Cambridge, United Kingdom (2008)
- 10. Sainudiin, R., Teng, G.: Minimum distance histograms with universal performance guarantees. Japanese Journal of Statistics and Data Science 2(2), 507–527 (2019), https://doi.org/10.1007/s42081-019-00054-y
- 11. Sainudiin, R., York, T., Harlow, J., Teng, G., Tucker, W., George, D.: MRS 2.0, a C++ class library for statistical set processing and computer-aided proofs in statistics. https://github.com/raazesh-sainudiin/mrs2 (2008–2018)
- 12. Samet, H.: The Design and Analysis of Spatial Data Structures. Addison-Wesley Longman, Boston (1990)


- 13. Stanley, R.P.: Enumerative combinatorics. Vol. 2, Cambridge Studies in Advanced Mathematics, vol. 62. Cambridge University Press, Cambridge (1999)
- 14. Tukey, J.W.: Non-Parametric Estimation II. Statistically Equivalent Blocks and Tolerance Regions — The Continuous Case. The Annals of Mathematical Statistics 18(4), 529–539 (1947)
- 15. Wasserman, L.: All of Statistics: A Concise Course in Statistical Inference. Springer, New York (2003)
- 16. Wiklund, T.: SparkDensityTree. https://github.com/TiloWiklund/ SparkDensityTree (2018)


