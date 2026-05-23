arXiv:1610.02420v4[cs.DS]1Dec2016

Lopsidependency in the Moser-Tardos framework: Beyond the Lopsided Lov´sz Local Lemma

David G. Harris∗

Abstract

The Lopsided Lova´sz Local Lemma (LLLL) is a powerful probabilistic principle which has been used in a variety of combinatorial constructions. While this principle began as a general statement about probability spaces, it has recently been transformed into a variety of polynomial-time algorithms. The resampling algorithm of Moser & Tardos (2010) is the most well-known example of this. A variety of criteria have been shown for the LLLL; the strongest possible criterion was shown by Shearer, and other criteria which are easier to use computationally have been shown by Bissacot et al (2011), Pegden (2014), Kolipaka & Szegedy (2011), and Kolipaka, Szegedy, Xu (2012).

We show a new criterion for the Moser-Tardos algorithm to converge. This criterion is stronger than the LLLL criterion, and in fact can yield better results even than the full Shearer criterion. This is possible because it does not apply in the same generality as the original LLLL; yet, it is strong enough to cover many applications of the LLLL in combinatorics. We show a variety of new bounds and algorithms. A noteworthy application is for k-SAT, with bounded occurrences of variables. As shown in

Gebauer, Sza´bo, and Tardos (2011), a k-SAT instance in which every variable appears L ≤ e2(kk+1+1) times, is satisﬁable. Although this bound is asymptotically tight (in k), we improve it to L ≤ 2

![image 1](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile1.png>)

k+1(1−1/k)k

k−1 − k2 which can be signiﬁcantly stronger when k is small.

![image 2](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile2.png>)

![image 3](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile3.png>)

We introduce a new parallel algorithm for the LLLL. While Moser & Tardos described a simple parallel algorithm for the Lova´sz Local Lemma, and described a simple sequential algorithm for a form of the Lopsided Lemma, they were not able to combine the two. Our new algorithm applies in nearly all settings in which the sequential algorithm works — this includes settings covered by our new stronger LLLL criterion.

# 1 Introduction

We begin by reviewing background material on the Lov´asz Local Lemma (LLL), the Resampling Algorithm of Moser & Tardos to implement it [22], and its generalization the Lopsided Lov´asz Local Lemma (LLLL). We discuss some strengthened forms of the LLL, such as Shearer’s criterion [24]. This will set notation which we will use throughout the paper. In Section 1.4, we will describe the main contribution of this paper, which is a strengthened form of the LLLL.

This is an extended version of a paper which appeared in the Proceedings of the Twenty-sixth annual ACM-SIAM Symposium on Discrete Algorithms.

- 1.1 The Lov´asz Local Lemma and the Moser-Tardos algorithm


The Lov´asz Local Lemma (LLL) is a very general probabilistic principle, ﬁrst introduced in [6], for showing that it is possible to avoid a potentially large set B of “bad-events”, as long as the bad-events are not interdependent and are not too likely. We write m = |B|. One formulation of this principle is the following: Suppose we have a probability space Ω, and we deﬁne a dependency graph among all the bad-events, such that any bad-event B ∈ B is independent of all the other bad-events except its neighbors in the dependency graph. We use the notation B ∼ B′ to denote that B and B′ are connected in the dependency graph. (The notion of dependency is intuitively clear, although the formal deﬁnition is somewhat technical.)

Now suppose there is some weighting function µ : B → [0,∞), with the property ∀B ∈ B µ(B) ≥ PΩ(B)

(1 + µ(B′)) (1)

B′∼B

![image 4](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile4.png>)

∗Department of Computer Science, University of Maryland, College Park, MD 20742. Research supported in part by NSF Awards CNS 1010789 and CCF 1422569. Email: davidgharris29@gmail.com

then, in the probability space Ω, there is a positive probability that none of the bad-events B ∈ B are true.1

The LLL is often seen in the simpler “symmetric” form: suppose each bad-event B has probability at most p; and suppose each bad-event depends on at most d other bad-events. Then (1) can be simpliﬁed to the criterion ep(d + 1) ≤ 1.

This principle has had many applications in combinatorics, for showing the existence of a wide variety of conﬁgurations. Unfortunately, typically the probability of avoiding B is exponentially small, so this does not yield eﬃcient algorithms. In [22], Moser & Tardos developed an amazingly simple eﬃcient algorithm for the LLL, as follows: suppose we have a series of variables X1,...,Xn; we wish to assign values to these variables. The probability space Ω assigns each variable independently, with PΩ(Xi = j) = pij. We also have a set B of forbidden conﬁgurations of these variables, which we refer to as bad-events. For our purposes, it will suﬃce to consider bad-events which are atomic; that is, any bad-event B can be written B ≡ (Xi

= jr). We abuse notation, so that B is identiﬁed with the set {(i1,j1),...,(ir,jr)}. Thus, for instance, when we write (i,j) ∈ B, we mean that B demands Xi = j.

= j1)∧···∧(Xi

1

r

The Moser-Tardos algorithm (henceforth referred to as MT) can now be described as follows:

- 1. Draw each variable independently from the distribution Ω.
- 2. While there is some true bad-event:


- 2a. Choose a true bad-event B arbitrarily.
- 2b. Resample all the variables involved in B according to the distribution Ω.


Under the same conditions as (1), the criterion for the probabilistic LLL, [22] showed that this algorithm terminates quickly.

- 1.2 The Lopsided Lov´asz Local Lemma


In [7], the LLL was generalized by observing that it is not necessary for bad-events to be fully independent. If the bad-events are positively correlated in a certain sense, then for the purposes of the LLL this is just as good as independence. (The precise form of the positive correlation is somewhat involved, but we will not need it in this paper so this intuitive deﬁnition will suﬃce.)

If bad-events B,B′ are not positively correlated in this sense, we say that B,B′ are lopsidependent. One can likewise build a lopsidependency graph (also known as a negative dependency graph) on the set of bad-events B. In this case, the LLL criterion (only slightly modiﬁed) still applies: we must have

∀B ∈ B µ(B) ≥ PΩ(B) µ(B) +

(1 + µ(B′))

B′∼B

This generalized form of LLL, referred to as the Lopsided Lov´sz Local Lemma (LLLL), has been used in a variety of contexts. A variety of probability spaces ﬁt into this framework, for example random permutations [18], Hamiltonian cycles [2], and matchings on the complete graph [19]. Only a few applications of the LLLL have corresponding eﬃcient algorithms; for example, [12] gives an MT variant for random permutations and [1] gives algorithms for other spaces such as Hamiltonian cycles.

One important and simple setting for the LLLL is covered by the original MT algorithm, and this was already described in the original paper of Moser & Tardos: suppose as above that Ω chooses each variable independently and the bad-events are atomic. Given two such bad-events B,B′, we say that B,B′ agree on variable i if there is some j with (i,j) ∈ B,(i,j) ∈ B′. We say that B,B′ disagree on variable i if there are j = j′ with (i,j) ∈ B,(i,j′) ∈ B′. Now the relation of disagreeing on some variable deﬁnes a lopsidependency graph:

B ∼ B′ if ∃(i,j) ∈ B,(i,j′) ∈ B′,j = j′

We use the notation (i,j) ∼ (i′,j′) iﬀ i = i′,j = j′. Some related notations will be to write (i,j) ∼ B iﬀ there is some j′ = j with (i,j′) ∈ B, and to write i ∼ B iﬀ there is some (i,j) ∈ B. We note that if B ∼ B′, then B and B′ are mutually exclusive events.

![image 5](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile5.png>)

1Note that the standard presentation of the LLL uses the parametrization x(B) = µ(µB(B)+1) , but this alternate parametrization will be necessary for later results.

![image 6](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile6.png>)

We refer to this setting as the “variable-assignment LLLL,” since we are independently assigning values to each variable. The k-SAT problem is a canonical example; we discuss how the LLLL applies in Section 4.1. In this problem, we are given a collection of clauses in n variables, each involving k distinct literals. Each variables appears in at most L clauses (either positively or negatively). Our goal is to ﬁnd a solution which makes all the clauses true. It turns out the worst case is when each variable appears L/2 times positively and L/2 times negatively (see Section 4.1 for more details). In this case, we assign each variable to be true or false with probability 1/2. For each clause, we have a bad-event that the clause is falsiﬁed. Now consider a bad-event B; it has probability 2−k. In the LLLL setting, B depends only on clauses which disagree with the variables in that clause; as each clause appears L/2 times with each polarity, there are kL/2 other bad-events which are lopsidependent with B. Thus the symmetric LLLL gives the bound L ≤ 2

k+1−2e

ek to guarantee that a solution exists (and MT ﬁnds it). As we will see in Section 4.1, more careful calculations and more precise forms of the LLL can give slightly better bounds.

![image 7](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile7.png>)

- 1.3 Shearer’s criterion and stronger formulations of the LLL and LLLL

The LLL and LLLL criteria depend solely on two factors: the probabilities of the bad-events, and the shape of the dependency (or lopsidependency) graph between them. The precise nature of the dependency does not enter into them; for example, we have the same formula whether we are dealing with the variable-assignment setting, or permutations, or matchings, and so on.

One can ask what is the strongest possible criterion that can be given in terms of these two quantities. Thus, given a dependency graph G and probabilities PΩ(B), is there guaranteed to be a non-zero probability of avoiding all bad-events? In fact, the exactly tight criterion was shown by Shearer [24], and it is stronger than (1). Furthermore, [15] showed that, if the MT algorithm has a small slack compared to this optimal criterion, then it too will converge.

Unfortunately, the criterion of [24] is not easy to compute. A variety of other criteria, which are slightly weaker than [24] but easier to apply, have been shown, e.g. [3], [23], [16]. These criteria apply both to the probabilistic form of the LLLL as well as to the MT algorithm. We emphasize that these alternate criteria are all weaker than and are implied by Shearer’s criterion. We will discuss them in greater detail in Section 2.2.

As noted by [15], the MT algorithm applies to a more restrictive model than the LLL, so Shearer’s LLL criterion is not necessarily tight in this restrictive class. [15] gave some toy examples of this situation. Notwithstanding this, most researchers have considered Shearer’s criterion to be the ultimate form of the LLL. Other forms of the LLL and algorithms such as MT are attempts to match this bound.

- 1.4 Our contributions: a new LLLL criterion


In this paper, we do not change the MT algorithm in any way. However, we give a alternate criterion for it to converge. In our opinion, the surprising fact is that this new criterion can go beyond the Shearer criterion. In the LLLL framework, lopsidependency is as good as pure independence; we show that if bad-events agree on a variable, this gives better bounds than if they were independent!

We reiterate that the Shearer criterion is the strongest possible criterion that can be given for the level of generality to which it applies. Our new criterion depends in a fundamental way on the decomposition of bad-events into variables; it cannot be stated in the language of probability and dependency graphs.

We state our new criterion as follows.

- Deﬁnition 1.1 (Orderability). Given an event E, we say that a set of bad-events Y ⊆ B is orderable to E, if either of the conditions hold:


- (O1) Y = {E}, or
- (O2) there is some ordering Y = {B1,...,Bs}, with the following property. For each i = 1,...,s, there is some zi ∈ E such that zi ∼ Bi,zi  ∼ B1,...,zi  ∼ Bi−1.


Note that ∅ is orderable to E, as indeed it satisﬁes condition (O2). Recall that when we write z ∼ B, we mean that there exists z′ ∈ B with z ∼ z′.

- Theorem 1.2. In the variable-assignment setting, suppose there is µ : B → [0,∞) satisfying the following condition:


µ(B′)

∀B ∈ B,µ(B) ≥ PΩ(B)

B′∈Y

Y orderable to B

then the MT terminates with probability 1. The expected number of resamplings of a bad-event is at most µ(B).

The LLLL cannot guarantee under these conditions that a satisfactory conﬁguration even exists; for this reason, we view this criterion as going beyond the LLLL. This criterion is about as easy to work with as the original MT criterion — in some cases, in fact, it can yield signiﬁcantly simpler calculations. In Section 2.2, we compare this to other LLLL criteria.

In Section 4, we give some applications of this new criterion. We summarize the most important ones here:

- 1. SAT with bounded variable occurrences Consider the following problem: we have a SAT instance, in which each clause contains k distinct variables. We are also guaranteed that each variable occurs in at most L clauses, either positively or negatively. How can large can L be so as to guarantee the existence of a solution to the SAT instance?

As shown in [8], the LLLL gives an asymptotically tight bound for this problem, namely L ≤ 2

k+1

![image 8](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile8.png>)

e(k+1). However, there still is room for improvement, especially when k is small. As L is growing exponentially, it is arguably the case that large k is not algorithmically relevant anyway. We are able to improve on [8] to show that when

L ≤

2k+1(1 − 1/k)k k − 1

![image 9](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile9.png>)

−

2 k

![image 10](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile10.png>)

then the SAT instance is satisﬁable, and the MT algorithm ﬁnds a satisfying occurrence in polynomial time. This is always better than the bound of [8], and when k is small the improvement can be substantial.

- 2. Hypergraph coloring. Suppose we are given a k-uniform hypergraph, in which each vertex participates in at most L edges. We wish to c-color the vertices, so that no edge is monochromatic (all vertices receiving the same color). This problem was in fact the inspiration for the original LLL [6]. There are many types of graphs and parameters for which better bounds are known, but the LLL gives very simple constructions and also provides the strongest bounds in some cases (particularly when c,k are ﬁxed small integers). Strangely, depending on whether c or k is large, one can obtain better bounds using the standard LLL or the LLLL. Thus one can show the bounds:


L ≤

(1 − 1/k)k−1 c

ck k

max(

,

![image 11](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile11.png>)

![image 12](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile12.png>)

1 (c − 1)e

) (2)

![image 13](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile13.png>)

Our approach gives the simpler and stronger criterion:

ck(1 − 1/k)k−1 k(c − 1)

L ≤

.

![image 14](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile14.png>)

Our new criterion is always better than (2), interpolating smoothly between the regimes when c or k is large. This illustrates an advantage of our technique — despite the daunting form of our new LLLL criterion, in practice it typically gives formulas which are more computationally tractable.

Comparison of Shearer criterion to Moser-Tardos. It is challenging to directly compare the Shearer criterion with the Moser-Tardos algorithm, because they apply to such diﬀerent contexts: generic probability spaces in the former case and variable conﬁgurations in the latter. We defer this discussion to a forthcoming paper [11] which shows that the analysis of [8] (based on the asymmetric LLL) cannot be much improved by using a stronger form of the LLL. In particular, our proof directly based on our new MT criterion is stronger than would be possible from Shearer’s criterion, let alone the LLL.

- 1.5 Our contribution: a new parallel algorithm


The original MT framework had a simple parallel RNC algorithm for the Lov´asz Local Lemma. Frustratingly, although the sequential MT algorithm applied to the variable-assignment LLLL setting, the parallel algorithm did not.

We remedy this situation in Section 3 by introducing a new parallel randomized algorithm for the variableassignment LLLL, which requires only a multiplicative slack compared to our new criterion for the sequential algorithm. (Showing that this algorithm is compatible with the new LLLL criterion requires non-trivial arguments).

- Theorem 1.3. Suppose there is µ : B → [0,∞) satisfying the following condition:


∀B ∈ B,µ(B) ≥ (1 + ǫ)PΩ(B)

Y orderable to B

B′∈Y

µ(B′)

then our new parallel algorithm algorithm terminates with probability 1. Suppose that the size of each badevent is at most M. Then our parallel algorithm terminates in time ǫ−1M(log B∈B µ(B))(logO(1) n)(M + logO(1) m) and (nm)O(1) processors with high probability. (Typically B∈B µ(B) ≤ O(m)).

We list a few applications of these new parallel algorithms:

- 1. SAT with bounded variable occurrences We have a SAT instance, in which each clause contains at least k variables. We are also guaranteed that each variable occurs in at most L clauses. Then,

under the condition L ≤ 2

k+1(1−1/k)k (k−1)(1+ǫ) − k2 the parallel MT algorithms ﬁnd a satisfying assignment in

![image 15](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile15.png>)

![image 16](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile16.png>)

time k

O(1) logO(1) n

![image 17](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile17.png>)

ǫ .

- 2. Hypergraph coloring. Suppose we are given a k-uniform hypergraph, in which each vertex participates in at most L edges. We wish to c-color the vertices, so that no edge is monochromatic.


k(1−1/k)k−1 (1+ǫ)(c−1)k the parallel MT algorithm ﬁnds a good coloring in time

Then, under the condition L ≤ c

![image 18](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile18.png>)

kO(1) logO(1) n

ǫ .

![image 19](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile19.png>)

# 2 The variable-assignment LLLL

As we have said, we do not change the MT algorithm in any way. The only change is to the analysis. The analysis of [22] is based on two main idea: a resampling table, and building witness trees for each resampling that occurs during a run of the algorithm. A witness tree lists the full history of the variables involved in a resampling — “why” a given resampling occurred. [22] describes this in much greater detail, and we recommend that the reader should read that paper for a careful and thorough explanation of the witness tree analysis.

The idea of the resampling table is that, at the very beginning of the algorithm, you draw an inﬁnite list of all the future values for each variables. Then resampling table entry R(i,j) gives the jth value for each variable Xi. Initially, you set Xi = R(i,1); when you need to resample i, you set Xi = R(i,2), and so forth. After drawing R, the remainder of the MT algorithm becomes deterministic. One can determine, for each witness tree, necessary conditions to hold on R.

In the MT algorithm, the choice of which bad-event to resample can be arbitrary, and can even be under the control of an adversary. In fact, MT shows something even stronger than this: even if the choice of which bad-event to resample depends on R, then the MT algorithm must still converge with high probability. Thus, the LLLL criterion is strong enough to show convergence even if the resampling is determined by a clairvoyant adversary.

Our analysis is also based on witness trees, but it dispenses with the resampling table. Instead, variables are assumed to be resampled in an on-line fashion. The choice of which bad-event to resample can be arbitrary, but must depend solely on the prior state (not the future state) of the system.

Because we impose this restriction on the resampling rule, we can use stochasticity to analyze our witness trees, in a way which is not possible with the MT framework. The basic idea is that, whenever we resample

some bad-event B, the distribution for the new values for its variables is the same as the law of Ω, even conditional on all prior state. This is simply not true in the MT framework: the choice of resampling rule could produce a dependency on the future.

We will eventually take a union-bound over witness trees, so it is critical to prune the space of witness trees as much as possible. In other words, we will need the most succinct possible explanation of each resampling. Let us consider a simple example of how we can use our stronger stochasticity assumption to analyze more succinct witness trees. Suppose that we have some bad-event B ∋ (i,j), and we want to explain why we eventually resampled Xi = j. Suppose there were two earlier events B1,B2 which included (i,j′). These events would be placed as children of B in the standard MT witness tree. This means that we encounter B1,B2 (in an unspeciﬁed order), and when we encounter the second one we select Xi = j.

We can view the witness tree for B as making a prediction: namely, that at the appropriate time, when we choose to resample variable Xi, then we set Xi = j. If we can ﬁx a speciﬁc time at which this prediction should hold, then we can bound its probability. For this purpose, it suﬃces to only record information about the later of the two events B1,B2. We can discard the information about the earlier resampling. By only retaining the latest occurrence of each variable, we still have all the information we need to deduce the resamplings. The stochasticity now tells us that whenever the resample the latter of B1,B2, the new values for the variables in it must have the same distribution as in Ω. The reason that this is true is that the choice of whether to resample B1 or B2 ﬁrst cannot depend on the new values of the variables.

We see that we have “compressed” the information relevant of B. This signiﬁcantly prunes the space of witness trees, but we will have to work much harder to show that it is suﬃcient.

2.1 Forming witness trees

When building witness trees, we will maintain the following key invariant: for any node v in the tree labeled by B, the children of v receive distinct labels B1,...,Bs such that {B1,...,Bs} is an orderable set for B. This is the key principle behind our new criterion.

We now describe how to form a witness tree for an event of interest E. Suppose we have listed, in order, all the bad-events that were ever resampled during MT, listed as B1,...,BT. This is referred to as the execution log. Suppose E = Bt. We start with the resampled event E at the root. Starting at time t − 1, we proceed backward through the execution log. For each bad-event B encountered, we see if there is some node v ∈ τ for which B is eligible. If so, we add B to the deepest such position (breaking ties arbitrarily). We give the following more precise deﬁnition of eligibility:

- Deﬁnition 2.1 (Eligibility). Suppose we have formed a (partial) witness tree τ, and we have a node v ∈ τ labeled by B. Suppose the children of v receive distinct labels B1,...,Bs. Then we say a bad-event B′ is eligible for v if B′ = B1,...,Bs and if {B1,...,Bs,B′} is orderable for B.


We distinguish between two related notions of the witness tree. Let τˆt denote the witness tree corresponding to the resampling at time t during an execution of the algorithm; this is a random variable. We also denote by τˆt

t0 the witness tree produced in this way, in which we only keep track of events after time t0 (that is, this witness tree only records events between times t0 and t1 inclusive). If t0 > t1, then τˆt

1

t0 is deﬁned to be the null tree. We will sometimes omit the superscript to simplify the notation. By deﬁnition τˆ1t = τˆt.

1

We also sometimes may wish to discuss a certain labeled tree, and under what conditions it could have been produced. We use then the notation τ to denote a witness tree in this sense.

One simple deﬁnition we will use often:

Deﬁnition 2.2. Consider any variable i, and consider a tree τ with a node v. We say that v involves i, if v is labeled by some bad-event B, and (i,j) ∈ B for some j.

We list some easy properties of the witness trees produced in this manner:

- Proposition 2.3. 1. Consider any bad-event B. Consider the leaf nodes of τˆ labeled by B; all such nodes must have distinct depths in the tree.


2. Consider any variable i, and, among all the nodes v ∈ τˆ involving i, consider the set of such nodes which are greatest depth in the tree. While it is possible that there are multiple such nodes v1,...,vr, all such nodes must be labeled by B1,...,Br which agree on variable i.

Proof. The earlier bad-event would have been eligible to be a child of the later bad-event, and hence would have been placed either there or deeper in the tree.

![image 20](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile20.png>)

![image 21](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile21.png>)

![image 22](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile22.png>)

![image 23](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile23.png>)

In light of Proposition 2.3, we may deﬁne the active value for each variable:

Deﬁnition 2.4 (The active value of a variable). Consider any variable i, and, among the set of nodes v ∈ τ involving i, consider the nodes at greatest depth in the tree. All such nodes contain (i,j) for some common value j. We denote by Ai(τ), the active value of variable i, by this common value j.

If variable i does not appear in τ, we deﬁne Ai(τ) = ⊤, the sure value. By convention, we use Xi = ⊤

- as a shorthand for the sure event (the entire probability space). For example, PΩ(Xi = ⊤) = 1.


We note that these types of witness trees look very diﬀerent from the standard MT construction. For example, the layers in the tree (and even the children of a common parent) do not necessarily form an independent set; there can be multiple copies of a single bad-event in a given layer.

Suppose we are given a tree τ and a time t1; we want to estimate the probability that τˆt

= τ. This is the key to the MT proof strategy. We can imagine running the MT algorithm and see whether, so far, it appears that it is still possible for τˆt

1

= τ. This is a kind of dynamic process, in which we see what conditions are still imposed in order to achieve this tree. One key point in our rule for forming witness trees is that, as we run the MT algorithm, we will be able to deduce not just τˆt

1

but also τˆt

t0 for all t0 ≥ 1. We will often omit the superscript t1 in the following; it should be understood.

1

1

- Proposition 2.5. Suppose we are given the partial witness tree τˆt, and we encounter a bad-event B at time t. Then τˆt+1 is uniquely determined, according to the following rule: if there is a leaf node labeled by B, select the deepest such leaf node v (by Proposition 2.3 it is unique) and we have τˆt+1 = τˆt − v. Otherwise we have τˆt+1 = τˆt.

Proof. First, suppose that τˆt did contain such a node v. It must be that v  ∈ τˆt+1. For, if so, then when forming τˆt from τˆt+1, we would have placed B as a child of v; that is, τˆt would include an additional copy of B. So τˆt+1 is missing the node v from τˆt. As each time step can only aﬀect a single node in the witness tree, it must be that τˆt+1 = τˆt − v.

Second, suppose that τˆt contained no such node v. When forming τˆt from τˆt+1, we either make no changes or add a single node labeled by B. In the latter case, τˆt would contain a leaf node labeled by B, which has not occurred. Hence it must be that τˆt = τˆt+1 as claimed.

![image 24](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile24.png>)

![image 25](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile25.png>)

![image 26](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile26.png>)

![image 27](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile27.png>)

The other key point is that, from the partial tree τˆt, we can deduce some information about the variables:

- Proposition 2.6. Consider any variable i. At time t of the MT algorithm, we must have Xi = Ai(ˆτt).


Proof. Suppose B is a node of greatest depth containing variable i, and we have (i,j) ∈ B, where j = Ai(ˆτt). Suppose Xi = j′ = j at time t.

In order to include B in the witness tree τˆ, we must eventually resample B, which implies that eventually we must have Xi = j. As Xi = j′ at time t, this implies that we must ﬁrst encounter some bad-event B′ ∋ (i,j′). But then B′ would be eligible to be placed as a child of B, and so would be placed there or lower. This contradicts that B is the greatest-depth occurrence of variable i.

![image 28](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile28.png>)

![image 29](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile29.png>)

![image 30](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile30.png>)

![image 31](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile31.png>)

These propositions together allow us to prove the Witness Tree Lemma:

Lemma 2.7 (Witness Tree Lemma). Let τ be a witness tree with nodes labeled B1,...,Bs. Then the probability of ever observing this witness tree is bounded by

P(ˆτt = τ for some t ∈ Z) ≤ PΩ(B1)···PΩ(Bs) We sometimes refer to the RHS as the weight of τ,

w(τ) = PΩ(B1)···PΩ(Bs)

Proof. The ﬁrst step of the MT algorithm is to draw all the variables independently from Ω. We may consider ﬁxing the variables to some arbitrary (not random) values, and allowing the MT algorithm to run from that point onward. We refer to this as starting at an arbitrary state of the MT algorithm. We prove by induction on τ the following: for any witness tree τ, and starting at any state of the MT algorithm, then we have

PΩ(B) i PΩ(Xi = Ai(τ))

τˆt = τ) ≤ B∈τ

P(

(3)

![image 32](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile32.png>)

t>0

First, the base case when τ = ∅. Then this is vacuously true, as the RHS of (3) is equal to 1. Next, for the induction. Suppose that τˆt = τ for some t > 0. Then, a necessary condition of this is that,

- at some time t′ < t, we must resample some B ∈ B such that a leaf node of τ is labeled by B. (If not, then τˆt could never acquire such a leaf node.) Suppose that t′ is the earliest such time and that v is a leaf node labeled by B. We condition now on a speciﬁc value for t′ and B.


For each i ∼ B, we must resample variable i to take on value Ai(τ − v) (recall our convention that if A(τ − v) = ⊤, then this is automatically true.) This has probability PΩ(Xi = Ai(τ − v)). Next, starting at the state of the system at time t′ +1, we must satisfy τˆt−1 = τ −v. We need to estimate the probability that this occurs, conditional on a ﬁxed choice of t′,B. Crucially, the inductive hypothesis gives an upper bound on this probability conditional on any state of the MT algorithm. In particular, this upper bound applies even when we condition on t′,B. Thus, we may multiply the two probabilities to obtain:

′∈τ−v PΩ(B′) i PΩ(Xi = Ai(τ − v))

PΩ(Xi = Ai(τ − v)) B

τˆt = τ) ≤

P(

![image 33](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile33.png>)

t>0

i∼B

′∈τ PΩ(B′) PΩ(B) i ∼B PΩ(Xi = Ai(τ − v))

= B

![image 34](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile34.png>)

If i  ∼ B then Ai(τ − v) = Ai(τ), while for each i ∼ B we have (i,Ai(τ)) ∈ B. Hence the denominator is equal to i PΩ(Xi = Ai(τ)) and the induction holds.

Next, we claim that the probability that there is some t > 0 such τˆt = τ is at most w(τ). (Note that this diﬀers subtly from the induction; in the induction, we are showing a bound which applies to any starting state of the system; here, we are claiming that this bound holds when the MT algorithm begins with a random initialization.) To see this, note that a necessary condition to have τˆt = τ is that in the initial sampling of all relevant variables, each variable i must take on value Ai(τ). Conditional on this event, the probability of τˆt = τ for some t is still given by the inductive hypothesis, so we have

τˆt = τ) ≤

P(

t>0

i

PΩ(B) i PΩ(Xi = Ai(τ))

PΩ(Xi = Ai(τ)) × B∈τ

= w(τ)

![image 35](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile35.png>)

![image 36](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile36.png>)

![image 37](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile37.png>)

![image 38](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile38.png>)

![image 39](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile39.png>)

Finally, we show that each event in the execution log of the MT algorithm has a distinct witness tree. This is almost a triviality in the standard analysis of the MT algorithm, but here it is surprisingly subtle. For instance, there may be multiple resamplings of a bad-event B, and the later occurrences may have smaller witness trees. Nevertheless, all such trees are unique:

= τˆt

- Proposition 2.8. Let t1 < t2; then τˆt


. Proof. Suppose τˆt

2

1

= τˆt

. Proposition 2.5 shows that the sequence of trees τˆt is uniquely determined by the original value τˆ and by the sequence of resamplings encountered the execution of the MT algorithm. As τˆt

2

1

initially, we must have that τˆt

t = τˆt

t for all t ≥ 1. But now substitute t = t2; in this case, τˆt

= τˆt

t is the null tree and τˆt

1

2

1

2

- 1


t consists of a single node. So this is a contradiction.

2

![image 40](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile40.png>)

![image 41](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile41.png>)

![image 42](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile42.png>)

![image 43](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile43.png>)

- Theorem 2.9. Suppose there is µ : B → [0,∞) satisfying the following condition:


∀B ∈ B,µ(B) ≥ PΩ(B)

B′∈Y

Y orderable to B

µ(B′)

then the MT terminates with probability 1. The expected number of resamplings of a bad-event B is at most µ(B).

Proof. First, by induction on tree-height, one can show that the total weight of all witness trees rooted in a bad-event B, is at most µ(B). This follows since the children of the root node form an orderable set for B.

Next, by Proposition 2.8, each resampling of B corresponds to a distinct witness tree. Hence, by the Lemma 2.7, the expected number of witness trees rooted in B is at most the sum of the weights of all such trees. Hence the expected number of resamplings of B is at most µ(B).

![image 44](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile44.png>)

![image 45](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile45.png>)

![image 46](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile46.png>)

![image 47](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile47.png>)

- 2.2 Comparison to other LLL criteria


The original form of the LLL simply counted the number of neighbors of each bad-event. As noted by [3], the criterion can be strengthened by further analysis of the dependency graph; namely, for any bad-event B, one only needs to examine independent sets of neighbors of B. Later, Pegden showed that this improved criterion applies also to the MT algorithm [23]. Alternatively, following [15], one can derive this strengthened criterion as a corollary of [24]. This can be stated as follows:

- Theorem 2.10 (Pegden’s Criterion). Suppose there is µ : B → [0,∞) satisfying the following condition:


µ(B′)

∀B ∈ B µ(B) ≥ PΩ(B) µ(B) +

B′∈Y

Y an independent set of neighbors to B

then the MT terminates with probability 1. The expected number of resamplings of a bad-event B is at most µ(B).

This criterion applies for any dependency graph. In particular, it applies if ∼ is deﬁned in terms of lopsidependency (B ∼ B′ if they disagree) or in terms of simple dependency (B ∼ B′ if they agree or disagree). One counter-intuitive aspect to Theorem 2.10 is that sometimes a denser dependency graph gives a stronger criterion. (For the Shearer criterion, this can never occur). In particular, ignoring lopsidependency can give better bounds.

Strictly speaking, Pegden’s criterion is incomparable to ours. However, in practice, the usual method of accounting for independent sets of neighbors comes from analyzing, for each variable i, the total set of all bad-events in which i could participate. An independent set of neighbors of B can contain one or zero bad-events involving each variable. Any higher-order interaction — such as ﬁnding groups of variables participating jointly in bad-events — is usually too complicated to analyze and is disregarded.

When we account for the dependency graph solely in terms of variable intersection, then we can replace the somewhat confusing concept of “orderable set” with a simpler (albeit slightly weaker) notion.

- Deﬁnition 2.11. Given an event E, we say that a set of bad-events Y ⊆ B is assignable to E, if either Y = {E}, or there is an injective function f : Y → E, such that for all B ∈ Y , we have some B ∋ z ∼ f(B) ∈ E


- Proposition 2.12. If Y is orderable to B, then it is assignable to B (but not necessarily vice-versa) Proof. Let Y = {B1,...,Bs}, so that for each i = 1,...,s there is some zi ∈ E with

zi ∼ Bi zi  ∼ B1,...,Bi−1

Now deﬁne f(Bi) = zi. We claim that f is injective. For, suppose zi = zj and i < j. Then zi ∼ Bi, so zj ∼ Bi, which is a contradiction.

![image 48](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile48.png>)

![image 49](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile49.png>)

![image 50](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile50.png>)

![image 51](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile51.png>)

When we sort bad-events by their variables, we obtain the following criteria; these are respectively the LLLL criterion and Pegden’s LLL criterion:

- Proposition 2.13. 1. If for all bad-events B we have


(1 + µ(B′))

µ(B) ≥ PΩ(B) µ(B) +

(i,j)∈B j′ =j B′∋(i,j′)

then the MT algorithm converges.

- 2. If for all bad-events B we have

µ(B) ≥ PΩ(B)

(i,j)∈B

1 +

j′ B′∋(i,j′)

µ(B′)

then the MT algorithm converges. Our criterion blends these two conditions and is stronger than either of them:

Proposition 2.14. If for all bad-events B we have

µ(B) ≥ PΩ(B) µ(B) +

(i,j)∈B

(1 +

j′ =j B′∋(i,j′)

µ(B′))

then the MT algorithm terminates with probability 1; the expected number of resamplings of B is at most µ(B).

Proof. For the bad-event B, we have the criterion

µ(B) ≥ PΩ(B)

Y assignable to B

B′∈Y

µ(B′)

We enumerate the assignable sets Y as follows. First, we may take Y = {B}; this accounts for the term µ(B) in the RHS of Proposition 2.14. Next, for each variable (i,j) ∈ B, we may select either zero or one bad-event B′ ∋ (i,j′) for some j′ = j. These account for respectively the terms 1 and j′ =j B′∋(i,j′) µ(B′) in Proposition 2.14.

![image 52](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile52.png>)

![image 53](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile53.png>)

![image 54](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile54.png>)

![image 55](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile55.png>)

It is in this sense that we view our criterion as being stronger than the original MT lopsidependency criterion and stronger than Pegden’s criterion.

- 3 Parallel algorithm for MT


In [22], a simple parallel algorithm was introduced which is based on the MT algorithm:

- 1. Draw all variables from Ω
- 2. While there is some true bad-event, repeat the following:


- 2a. Select a maximal independent set I of true bad-events
- 2b. Resample, in parallel, all bad-events in I.


This algorithm depends on the fact that, in the standard MT framework, bad-events which are unconnected do not share any variables. Hence they do not interact in any way and can be resampled in parallel. This is no longer the case for the lopsidependent MT algorithm; so in that case, frustratingly, we do not have any corresponding parallel algorithms.2

In this section, we introduce a new parallel algorithm corresponding to the lopsidependent MT setting, which achieves our new criterion up to a multiplicative slack. We assume that each bad-event uses at most M ≤ polylog(n) terms. We also suppose that the number of bad-events is polynomially bounded, although this can be relaxed quite a bit. Finally, we require a multiplicative slack in the LLLL criterion.

Here is the basic idea. Suppose we have a large number of bad-events which are currently true. Due to the LLLL criterion, there may be many “unconnected” bad-events which are simultaneously true, yet they intersect in variables and cannot be resampled in parallel. However, suppose we resample a given variable; with good probability, it will change its value, thereby falsifying all of the bad-events which contain it, even those we did not explicitly resample.

![image 56](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile56.png>)

2In [4], there is a brief discussion about a parallel deterministic algorithm for the variable-assignment LLLL. However, no algorithm is provided, nor are there any deﬁnite claims made for its performance.

This argument can break down if we have pij ≈ 1 for any variable i and value j (this situation is rare; see Section 4.5 for an example). In that case, resampling the variable i a single time is not likely to ﬂip its value; we must resample it multiple times. Much of the complication of our parallel algorithm comes from dealing with this somewhat pathological case. We will begin by stating a simple parallel algorithm which assumes pij < 1 − Ω(1) for all i,j; we then modify it to remove this condition.

- 3.1 The parallel algorithm: warm-up exercise We present the following Parallel Moser-Tardos Algorithm (Simpliﬁed):


- 1. Draw all variables independently from the distribution Ω.
- 2. While there is some true bad-event, repeat the following for rounds t = 1,2,...,:


- 3. Let Vt,1 be the set of bad-events which are true at the beginning of round t.
- 4. Repeat the following for a series of sub-rounds s = 1,2,..., until Vt,s = ∅.
- 5. Select a maximal disjoint set It,s ⊆ Vt,s. (This can be done using a parallel MIS algorithm).
- 6. Resample all B ∈ It,s.
- 7. Update Vt,s+1 as: Vt,s+1 = Vt,s − It,s − All bad events which are no longer true.


Theorem 3.1. Suppose that we satisfy the condition

∀B ∈ B,µ(B) ≥ PΩ(B)(1 + ǫ)

B′∈Y

Y orderable to B

µ(B′)

Suppose further that we satisfy the condition

∀i,j,PΩ(Xi = j) < 1 − ψ Let us deﬁne

W =

µ(B)

B∈B

Then whp the Parallel Moser Tardos (Simpliﬁed) terminates in time ψ−1ǫ−1 log W logO(1)(nm) using (nm)O(1) processors.

Proof. We provide only a sketch, as we will later introduce a more advanced algorithm. In each round t,s, note that every bad-event B ∈ Vt,s contains some resampled variable. Such a variable switches to a new value with probability ≥ ψ, in which case B is removed from Vt,s+1. Hence the expected size of Vt,s is decreasing as (1 − ψ)s. So, for s = Ω(ψ−1 log n), we have Vt,s = ∅ and the round t is done.

Next, suppose that a bad-event is resampled in round t. One can show that the witness tree for this resampling must have height t exactly. One can also compute the total weight of all such trees, and show that this is decreasing as (1 + ǫ)−t. Taking a union-bound over such trees, this implies that the probability of having ≥ t rounds is at most (1 + ǫ)−tW.

This implies that, whp, our algorithm requires ψ−1ǫ−1 logO(1) n logW rounds. In each round, one must select an MIS of the currently-true bad-events, which takes at most logO(1) m time and mO(1) processors.

![image 57](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile57.png>)

![image 58](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile58.png>)

![image 59](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile59.png>)

![image 60](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile60.png>)

It will take a lot more work to drop the dependency of the running time on ψ. To do this, we will need to resample a variable multiple times in the round. Thus, we must replace the step of selecting a maximal disjoint set of bad-events with a maximal set in which no variable occurs too many times (which depends on its probabilities pi). We must also deal with the possibility that we get inconsistent results when we resample a variable multiple times in a round.

Before we move on to the general case, we will need a subroutine to solve a problem we refer to as the vertex-capacitated maximal edge packing problem (VCMEP). We believe this may be a useful building block for other parallel algorithms.

- 3.2 Vertex-capacitated maximal edge packing


- Deﬁnition 3.2. Suppose we are given a hypergraph G, with m edges of size ≤ k, on a vertex set V . For each v ∈ V , we are given a capacity Cv in the range {0,...,m}. We wish to select a subset L ⊆ E of the edges, with the property that each vertex appears in at most Cv edges of L, and such that L is a maximal subset of E with that property. Such a set L is referred to as a vertex-capacitated maximal edge packing (VCMEP).


Such a set can be found easily by a sequential algorithm. Note that if Cv = 1 for all v, this is equivalent to ﬁnding a maximal independent set of the line graph of G.

- Theorem 3.3. There is parallel algorithm to ﬁnd a VCMEP in time k × logO(1)(mn).


Proof. We will repeatedly add edges until we have reached such a maximal set. At round i, suppose we have selected so far edges Li, and we begin with L0 = ∅.

Now form the residual graph and residual capacities; we abuse notation so that these are also denoted G,C. One can form an integer program corresponding to the vertex-capacitated maximum edge packing (i.e. packing of highest cardinality) for the residual. We let Mi denote the size of the maximum packing which can be obtained by extending Li. This integer program has variables xf corresponding to each edge f ∈ G, along with constraints that v∈f xf ≤ Cv for each vertex v. Now relax the integer program to a positive linear program. As shown by [20], there is a parallel algorithm running in time logO(1)(n + m) which can ﬁnd a solution x′ which is at least (1 − ǫ) times the optimum solution, where ǫ > 0 is some suﬃciently small constant. In turn, this solution is at least (1 − ǫ)(Mi − |Li|).

We now round this fractional solution x′ as follows: each edge is selected with probability x′f/(2k); if any vertex constraint v is violated, then all edges containing v are de-selected. We deﬁne Li+1 to be Li plus any selected edges.

Deﬁne the potential function Φi = Mi−|Li|. Note that if Φi = 0, then Li must be a maximal set of edges. We claim that, conditional on the state at the beginning of round i, we have E[Φi+1] ≤ (1 − Ω(1/k))Φi.

For, consider some edge f; it is selected with probability x′f/(2k); suppose we condition on that event. Consider any vertex v ∈ f. The expected number of times that other edges incident to v are selected is f′∋v,f′ =f x′f/(2k) ≤ (Cv − x′f)/(2k). By Markov’s inequality, the probability that the actual number exceeds Cv, in which case f is de-selected, is at most Cv−x

′ f

2kCv . Hence the total probability that f is selected is at least

![image 61](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile61.png>)

x′f 2k

P(f selected) ≥

(1 −

![image 62](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile62.png>)

Cv − x′f 2kCv

) ≥

![image 63](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile63.png>)

v∈f

x′f 2k

x′f 4k

- 1

![image 64](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile64.png>)

- 2k


(1 − k ×

) ≥

![image 65](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile65.png>)

![image 66](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile66.png>)

Summing over all such edges, we have that E[Φi+1] = E[Mi+1] − E[Li+1] ≤ Mi − |Li| −

x′f 4k

![image 67](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile67.png>)

f

(1 − ǫ)(|Mi| − Li) 4k

≤ Mi − |Li| − (

) ≤ Φi(1 − Ω(1/k))

![image 68](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile68.png>)

Hence, for i ≥ Ω(k log(mn)), we have E[Φi] ≤ n−Ω(1). This implies that Φi = 0 with high probability, which in turn implies that Li is a maximal packing with high probability.

![image 69](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile69.png>)

![image 70](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile70.png>)

![image 71](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile71.png>)

![image 72](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile72.png>)

- 3.3 The parallel algorithm


We now present our full parallel algorithm. We will suppose that each bad-event uses at most M terms. We also suppose that the number of bad-events is polynomially bounded, although this can be relaxed quite a

bit. Finally, we suppose there is a slack in the LLL condition, ∀B ∈ B,µ(B) ≥ PΩ(B)(1 + ǫ)

µ(B′)

B′∈Y

Y orderable to B

- 1. Draw all variables independently from the distribution Ω.
- 2. While there is some true bad-event, repeat the following for rounds t = 1,2,...,:

- 3. Let Vt,1 be the set of bad-events which are true at the beginning of round t. Let ai be the value of variable Xi at the beginning round t. Note that each bad-event in Vt,1 is a conjunction of terms Xi = ai. For notation throughout the rest of this algorithm, for each variable i let qi = PΩ(Xi = ai).
- 4. Repeat the following for a series of sub-rounds s = 1,2,..., until Vt,s = ∅.
- 5. View Vt,s as a hypergraph, whose vertices correspond to variables and whose hyper-edges correspond to bad-events. For each variable i, deﬁne the capacity Ci = ⌈Mq1

![image 73](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile73.png>)

i

⌉. Find a VCMEP It,s ⊆ Vt,s.

- 6. For each B ∈ It,s and each variable i ∼ B, draw a resampling value xB,i from its distribution in Ω. This represents that if we decide to resample B, then we will choose to set variable Xi equal to xB,i.
- 7. For each B ∈ It,s choose a random ρ(B) independently from the real interval [0,1]. We think of ρ(B) as the priority of B; we will resample the bad-events in the order of increasing ρ. Construct the undirected graph Gt,s whose vertices correspond to elements of It,s, and where there is an edge from B1 to B2 if ρ(B1) < ρ(B2) and B1,B2 both share a variable i and we

have xB

1,i = ai.

- 8. Find the lexicographically-ﬁrst MIS (LFMIS) It,s′ ⊆ It,s of the graph Gt,s, with respect to the order ρ. (We will say more about this step later)
- 9. For each variable Xi, if there is some B ∈ It,s′ with xB,i = ai, set Xi = xB,i (by the way that Gt,s is constructed, there can be at most one such B for each variable i); we say such that variable i is switched; otherwise leave Xi = ai.
- 10. Update Vt,s+1 as Vt,s+1 = Vt,s − It,s − All bad events containing a switched variable.


This algorithm is quite intricate to analyze. There are two main parts to the proof: showing that the number of rounds is small, and showing that each round can be executed quickly.

- 3.4 Bounding the number of rounds


The key to showing that the number of rounds is small, is to show that this parallel algorithm is simulating a version of the sequential MT algorithm.

- Proposition 3.4. Consider the following sequential algorithm, which is a variant of the MT algorithm with an unusual rule for selecting which bad-event to resample:


- 1. Draw all variables independently from the distribution Ω.
- 2. While there is some true bad-event, repeat the following for rounds t = 1,2,...,:
- 3. Let Vt,1 be the set of bad-events which are true at the beginning of round t. Let ai be the value of variable Xi at the beginning round t.
- 4. Repeat the following for a series of sub-rounds s = 1,2,..., until Vt,s = ∅.
- 5. View Vt,s as a hypergraph, whose vertices correspond to variables and whose hyper-edges correspond to bad-events. For each variable i, deﬁne the capacity Ci = ⌈Mq1

![image 74](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile74.png>)

i

⌉. Find a VCMEP It,s ⊆ Vt,s.

- 6. Select a random ordering πt,s of It,s. For i = 1,...,|It,s| let πt,s(i) denote the ith element of It,s in this ordering.


- 7. For k = 1,...,|It,s| do the following:


8. If πt,s(k) is currently true, resample it.

9. Update Vt,s+1 as Vt,s+1 = Vt,s − It,s − All bad events containing a switched variable. Let Xi,t,s denote the value of variable i after round t and sub-round s. Then the random variables Xi,t,s have the same distribution for the parallel algorithm and for this sequential resampling algorithm. Proof. We will show this by coupling the sequential and parallel algorithms. We consider the following hybrid algorithm which we denote H.

- 1. Draw all variables independently from the distribution Ω.
- 2. While there is some true bad-event, repeat the following for rounds t = 1,2,...,:


- 3. Let Vt,1 be the set of bad-events which are true at the beginning of round t.
- 4. Repeat the following for a series of sub-rounds s = 1,2,..., until Vt,s = ∅.
- 5. View Vt,s as a hypergraph, whose vertices correspond to variables and whose hyper-edges correspond to bad-events. For each variable i, deﬁne the capacity Ci = ⌈Mq1

![image 75](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile75.png>)

i

⌉. Find a VCMEP It,s ⊆ Vt,s.

- 6. For each B ∈ It,s and each variable i ∼ B, draw a random variable xB,i independently from Ω and draw a random variable ρ(B) independently from [0,1].
- 7. Form a permutation π of It,s by sorting in increasing order of ρ.
- 8. For k = 1,...,|It,s| do the following:


9. If π(k) is currently true, then for each variable i ∼ π(k), set Xi = xπ(k),i.

10. Update Vt,s+1 as Vt,s+1 = Vt,s − It,s − All bad events containing a switched variable.

We ﬁrst claim that H induces the same distribution on the random variables as the sequential algorithm. For, the permutation π in H is clearly drawn uniformly from the set of permutations of It,s. Also, the algorithm H does not examine the variable xπ(k),i in any way before step (9), and so by the principle of deferred decisions it is equivalent to draw Xi independently from Ω instead of setting Xi = xπ(k),i.

We next claim that H induces the same distribution on the random variables as the parallel algorithm. This follows from the following stronger claim: suppose that we ﬁx the random variables xB,i and ρ. Then the value of the variables X is identical in H and the parallel algorithm. To see this, consider some B ∈ It,s with π(k) = B. Then a simple induction on k shows that B ∈ It,s′ if and only if B is true at stage k of the loop (9) of H.

![image 76](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile76.png>)

![image 77](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile77.png>)

![image 78](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile78.png>)

![image 79](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile79.png>)

One may build witness trees for the resamplings of this sequential algorithm, as it is merely a variant of the usual MT algorithm.

- Proposition 3.5. Suppose that B is resampled in round t. Then the witness tree corresponding to this resampling has height t.


Proof. For each t′ ≤ t, let τˆ(t′) denote the tree formed for the resampling of B from round t′ onward (that is, we only add events in rounds t′,...,t inclusive to the witness tree).

We will prove by induction the stronger claim: Suppose that B is resampled in round t. Then for each

t′ ≤ t, the tree τˆ(t′) has height exactly t − t′ + 1; furthermore, all the nodes at depth t − t′ + 1 correspond to bad-events resampled at round t′. (Depth 1 corresponds to the root of the tree).

The base case of this induction is t′ = t. In this case, note that all events resampled in round t agree

on all variables, and each bad-event B ∈ B is resampled at most once. Hence τˆ(t) consists consists of just a singleton node labeled by B.

We move on to the induction step. We begin with τˆ(t′) and wish to extend it backward in time to round t′ −1. By induction hypothesis, τˆ(t′) has height exactly t−t′ +1 and the nodes at depth t−t′ +1 correspond to bad-events resampled at round t′.

Note ﬁrst that all bad-events encountered in round t′ − 1 are true at the beginning of that round. So they agree on all variables, which implies that they cannot be children of each other. This implies that the

only possible nodes at depth t′ − t + 2 in τˆ(t′−1) correspond to bad-events resampled in round t′ − 1 which have as their parent a node of depth t′ − t + 1. Thus, the height of τˆ(t′−1) is either t − t′ + 2 (as we want to show), or is t − t′ + 1.

By induction hypothesis, the tree τ(t′) contains some node v labeled by B′ at height t′ − t + 1 resampled in round t′.

First suppose B′ is true at the beginning of round t′ − 1, so B′ ∈ Vt′−1,1. Then either B′ is resampled in round t′ −1, or B′ becomes false during round t′ −1. In the ﬁrst case, B′ would be eligible to be placed as a child of v, so it is either placed there or at some other position at the same depth; either way, τˆ(t′−1) would have height t − t′ + 2. In the second case, it must be that B′ contains a variable which switched in round t′ − 1. This implies that B′ remains false at the end of round t′ − 1, so B′  ∈ Vt′,1; but B′ was resampled in round t′ so this is a contradiction.

Second suppose B′ is false at the beginning of round t′ − 1. It must have become true due to some variable Xi switching in round t′ −1 due to resampling some B′′. But then B′′ disagrees with B′ on variable Xi, so B′′ ∼ B′. As v is a leaf node in τˆ(t′), this implies that B′′ would be eligible to placed as a child of v. Again, such B′′ will be placed either as a child of v or at some position at the same depth, so that τˆ(t′−1) would have height t − t′ + 2.

![image 80](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile80.png>)

![image 81](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile81.png>)

![image 82](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile82.png>)

![image 83](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile83.png>)

- Proposition 3.6. The parallel algorithm terminates after O(logǫW ) rounds whp. Proof. By Proposition 3.4, it suﬃces to show that the sequential algorithm terminates after O(logǫW ) rounds whp. In each round t, there is at least one resampling, which must correspond to some tree of height t. As shown in [22], due to the slack condition the total weight of all such trees rooted in a bad-event B is

![image 84](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile84.png>)

![image 85](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile85.png>)

- O(µ(B)(1 + ǫ)−t). Summing over all such B, this implies that for t = Ω(log(nW)) this weight is n−Ω(1). Hence whp no such trees appear.


![image 86](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile86.png>)

![image 87](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile87.png>)

![image 88](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile88.png>)

![image 89](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile89.png>)

3.5 Analyzing the run-time of individual rounds

We next consider the individual steps that make up a round of the parallel algorithm.

- Proposition 3.7. The LFMIS It,s′ can be found whp in time O(log loglognn). Proof. In general, the problem of ﬁnding the LFMIS is P-complete [5], hence we do not expect a generic parallel algorithm for this. However, what saves us it that the ordering ρ and the graph Gt,s are constructed in a highly random fashion. This allows us to use a greedy algorithm to construct It,s′ :


![image 90](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile90.png>)

1. Let H1 be the directed graph obtained by orienting all edges of Gt,s in the direction of ρt,s. Repeat the following for l = 1,2,...,:

- 2. If Hl = ∅ terminate.
- 3. Find all source nodes of Hl. Add these to It,s′ .
- 4. Construct Hl+1 by removing all source nodes and all successors of source nodes from Hl.


The output of this algorithm is the LFMIS It,s′ . Each step can be implemented in parallel time O(1). The number of iterations of this algorithm is the length of the longest directed path in Gt,s. So it suﬃces it show that, whp, all directed paths in Gt,s have small length.

Suppose we select B1,...,Bl ∈ B uniformly at random. Let us analyze how these could form a directed path in G.

First, note that B2 is a neighbor of B1. Each variable i ∼ B1 appears in at most Ci −1 other bad-events. If B1 and B2 intersect in variable i, then that variable i creates an edge between B1,B2 only if xB

1,i = ai, which occurs with probability qi. Thus, for each B1, the expected number of B2 which are connected to that B1 is at most

(Ci − 1)qi ≤

1/(Mqi) × qi ≤ 1

i∼B1

i∼B1

Continuing this way, we see that the expected number of B1,...,Bl which are connected is at most 1.

Next, it must be the case that ρ(B1) < ρ(B2) < ··· < ρ(Bl). So far, none of the probabilistic statements have referred to ρ, so the probability this occurs conditional on all previous events is 1/l!. Thus, for l ≥ Ω(logloglognn), this is n−Ω(1) as desired.

![image 91](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile91.png>)

![image 92](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile92.png>)

![image 93](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile93.png>)

![image 94](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile94.png>)

![image 95](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile95.png>)

- Proposition 3.8. For s = Ω(M log n), we have Vt,s = ∅ whp.


Proof. We will show that Vt,s has an expected size which is decreasing exponentially in s.

First, we show the following fact: given any B ∈ It,s, we have B ∈ It,s′ with probability ≥ 1/2. For, a suﬃcient condition for B ∈ It,s′ is that there is no variable i ∼ B with B′ ∈ It,s,ρ(B′) < ρ(B) and xB′,i = ai. For each variable i, there are at most Ci − 1 candidate B′ ∈ It,s, and each of them has probability qi of setting xB′,i = ai, so the expected number of such B′ is at most qi × Mq1

× 1/2 ≤ 2M1 . Over all variables i ∼ B, this gives a total probability of ≤ 1/2.

![image 96](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile96.png>)

![image 97](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile97.png>)

i

Now consider any B ∈ Vt,s. By maximality of It,s, either B ∈ It,s, or B contains some variable which occurs Ci times in It,s. In the former case, B is necessarily removed from Vt,s+1.

Now, suppose variable i ∼ B occurs exactly Ci times in It,s. For each such occurrence B′, there is a probability of ≥ 1/2 that B′ ∈ It,s′ . The event that B′ ∈ It,s′ is independent of xB′,i, so each such B′ has a probability of qi/2 that B′ is selected and xB′,i = ai. Hence the total expected number of B′ ∈ It,s′ with xB′,i = ai, is at least Ci × qi/2 ≥ 2M1 . Note that there are either zero or one elements B′ ∈ It,s′ with this property, hence the probability that Xi switches is at least 2M1 . If this occurs, then we have B ∈/ Vt,s+1.

![image 98](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile98.png>)

![image 99](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile99.png>)

In either case, we have shown that a given B ∈ Vt,s is removed with probability at least 1 − 2M1 . Hence we have

![image 100](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile100.png>)

- 1

![image 101](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile101.png>)

- 2M


)|Vt,s| which implies that for s ≥ Ω(M log n) we have Vt,s = ∅ with high probability.

E[|Vt,s+1| | stage before stage t,s] ≤ (1 −

![image 102](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile102.png>)

![image 103](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile103.png>)

![image 104](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile104.png>)

![image 105](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile105.png>)

Putting this all together, we have the following:

- Theorem 3.9. Suppose that each B ∈ B has size at most M. Suppose that we satisfy the condition

∀B ∈ B,µ(B) ≥ PΩ(B)(1 + ǫ)

Y orderable to B

B′∈Y

µ(B′)

Then whp the Parallel MT algorithm terminates in time ǫ−1M(log W)(logO(1) n)(M + logO(1) m) using (nm)O(1) processors.

Note that the running time of the Simpliﬁed Parallel Moser-Tardos algorithm does not depend on M. In practice, when M is large, then other parallel aspects of the Moser-Tardos algorithm can become problematic; for example, we need non-trivial parallel algorithms to enumerate and check the events of B. It remains an interesting open problem to ﬁnd a parallel algorithm which works in the regime in which M is large and the probabilities of the bad-events become close to 1.

4 Applications

4.1 SAT with bounded variable occurrences

Consider the following problem: we have a SAT instance, in which each clause contains at least k variables. We are also guaranteed that each variable occurs in at most L clauses, either positively or negatively. How can large can L be so as to guarantee the existence of a solution to the SAT instance? This problem was ﬁrst introduced by [17], which showed some bounds on L. Most recently, it was addressed by [8]; they showed that the criterion L ≤ 2

k+1

![image 106](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile106.png>)

e(k+1) suﬃces to guarantee that a solution exists (and can be found eﬃciently). This criterion is also shown to be asymptotically optimal (up to ﬁrst-order terms). The main proof for this is to use the LLLL; they show that the worst-case behavior comes when each variable appears in a balanced way (half positive and half negative).

Although the criterion of [8] is asymptotically optimal, we can still improve its second-order terms. We show the following bound:

- Theorem 4.1. If each variable appears at most


2k+1(1 − 1/k)k k − 1

2 k

−

L ≤

![image 107](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile107.png>)

![image 108](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile108.png>)

times then the SAT instance is satisﬁable, and the MT algorithm ﬁnds a satisfying occurrence in polynomial time.

k+1(1−1/k)k (k−1)(1+ǫ) −k2. then whp the Parallel Resampling Algorithm ﬁnds a satisfying

Furthermore, suppose L ≤ 2

![image 109](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile109.png>)

![image 110](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile110.png>)

O(1)

occurrence in time (klogn)

ǫ . Proof. We will only prove the sequential result; the parallel result is almost identical.

![image 111](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile111.png>)

For each SAT clause, we have a bad-event B that it is violated. We deﬁne µ(B) = α for each bad-event, where α > 0 is a constant to be chosen.

As described by [8], the key problem is to choose a good probability distribution for each variable. Suppose a variable i occurs in li clauses, of which it occurs δili positively. In this case, we set variable i to be T with probability 1/2 − x(δi − 1/2), where x ∈ [0,1] is a parameter to be chosen. This is quite counter-intuitive. One would think that if a variable occurs positively in many clauses, then one should set the variable to be T with high probability; in fact we do the opposite.

We now wish to show that our MT criterion is satisﬁed. Let C be a clause and suppose without loss of generality each variable appears in it negatively. Then the corresponding bad-event is that all such variables are true. This has probability i∈C(1/2 − x(δi − 1/2)). Now, consider the assignable sets for the clause. We may either select the singleton C itself, or for each of the k variables we may select one or zero other clauses in which the corresponding variable appears positively. For each such variable i, the total number of such clauses is at most δiL. Hence we have the criterion:

α ≥

i∈C

1/2 − x(δi − 1/2) α +

(1 + δiLα)

i∈C

We bound the RHS as follows:

i∈C

1/2 − x(δi − 1/2) α +

(1 + δiLα) ≤

i∈C

i∈C

1/2 − x(δi − 1/2) 1 + δiLα + α/k (4)

Now set x = 2α+2αkLk+αkL; clearly x ∈ [0,1]. With this choice, verify that that the RHS of (4), viewed as a function of δi, achieves its maximum value at δi = 1/2. Thus we have

![image 112](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile112.png>)

i∈C

1/2 − x(δi − 1/2) α +

(1 + δiLα) ≤

i∈C

i∈C

- 1

![image 113](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile113.png>)

- 2


(1 + α/k + αL/2) = 2−k(1 + α/k + αL/2)k

We thus need to ﬁnd α ≥ 0 such that α − 2−k(1 + α/k + αL/2)k ≥ 0 (5)

Diﬀerentiate with respect to α to make the LHS of (5) as large as possible. This yields our optimal choice of α namely:

1

k+1

2k ( 2

k−1 − 1 2 + kL

2+kL)

![image 114](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile114.png>)

![image 115](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile115.png>)

α =

![image 116](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile116.png>)

k+1(1−1/k)k

1

k+1

When L ≤ 2

k−1 − k2, note that ( 2

k−1 ≥ k−k1 and so α ≥ 0 as desired. Also, (5) is satisﬁed.

2+kL)

![image 117](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile117.png>)

![image 118](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile118.png>)

![image 119](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile119.png>)

![image 120](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile120.png>)

![image 121](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile121.png>)

![image 122](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile122.png>)

![image 123](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile123.png>)

![image 124](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile124.png>)

![image 125](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile125.png>)

- 4.2 Hypergraph coloring


Suppose we have a k-uniform hypergraph, in which each vertex appears in at most L edges. We wish to c-color this hypergraph, while avoiding any monochromatic edges. There are many types of graphs and parameters for which better bounds are known, but the LLL gives very simple constructions and also provides the strongest bounds in some cases (particularly when c,k are ﬁxed small integers)[21].

Let us ﬁrst examine how the conventional LLL analysis would work. Counter-intuitively, when c is large it is better to use the standard LLL (deﬁning ∼ in terms of simple dependency) and when k is large it is better to use the LLLL (deﬁning ∼ in terms of lopsidependency.) In the ﬁrst case, a bad-event is that an edge is monochromatic (of an unspeciﬁed color). Consider an edge f. The neighbors of f would be other edges that intersect f. An independent set of neighbors of f consists of either f itself, or for each vertex

v ∈ f we may select one or zero edges (other than f). Setting µ(B) = α for all bad-events, this gives us the criterion

α ≥ c1−k(α + (1 + (L − 1)α)k) Routine calculations show that this can be satisﬁed if L ≤ c

k−1(1−1/k)k−1

k .

![image 126](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile126.png>)

Alternatively, in the LLLL, a bad-event would be that an edge f receives some color j. The neighbors of this event would be other edges receiving colors other than j; there are k(L − 1)(c − 1) + c such neighbors. Using the symmetric LLL and some simpliﬁcations, one obtains the bound L ≤ c

k

(c−1)ek. Pegden’s criterion could improve this somewhat, although there would no longer be a simple closed form.

![image 127](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile127.png>)

k−1

There seems to be a “basic” form of the bound L ≤ c

ek ; the standard LLL framework can improve on this using either Pegden’s criterion (replacing 1/e by (1 − 1/k)k−1) or by lopsidependency (replacing one factor of c by (c − 1)), but cannot do both simultaneously.

![image 128](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile128.png>)

Our new LLLL criterion. For each edge f ∈ G, we have c bad-events, namely that f is monochromatic of any given color. We assign µ(B) = α to all bad-events, where α > 0 is a parameter to be determined. We color each vertex independently and uniformly.

Now consider a bad-event B, say without loss of generality that edge f receives color 1. It has probability c−k. Consider the orderable sets for B; we want to sum B′∈Y µ(B′) over all such sets Y .

First, Y may consist of B itself; this contributes α. Second, Y may consist of, for each vertex v ∈ f, zero edges or one edge other than f receiving one color 2,...,c. Finally, we may have one vertex select f and some color for it; some set of other vertices selects other edges and other colors. Summing all these cases, we have the criterion for B:

α ≥ c−k (1 + α(c − 1)(L − 1))k + α(c − 1)((1 + α(c − 1)(L − 1))k − (α(c − 1)(L − 1))k) + α (6)

This has no closed-form solution for general L,k. But, for ﬁxed values of L,k it is easily solvable. For example, when c = 2, we list the largest values of L which are obtained by either our improved MT criterion or the original MT criterion (listed under L′):

![image 129](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile129.png>)

k L L′ k L L′

![image 130](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile130.png>)

![image 131](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile131.png>)

![image 132](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile132.png>)

![image 133](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile133.png>)

![image 134](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile134.png>)

![image 135](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile135.png>)

![image 136](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile136.png>)

![image 137](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile137.png>)

![image 138](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile138.png>)

![image 139](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile139.png>)

- 4 2 2 8 13 12

![image 140](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile140.png>)

![image 141](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile141.png>)

![image 142](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile142.png>)

![image 143](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile143.png>)

![image 144](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile144.png>)

![image 145](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile145.png>)

![image 146](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile146.png>)

![image 147](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile147.png>)

- 5 3 3 9 23 21

![image 148](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile148.png>)

![image 149](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile149.png>)

![image 150](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile150.png>)

![image 151](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile151.png>)

![image 152](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile152.png>)

![image 153](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile153.png>)

![image 154](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile154.png>)

![image 155](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile155.png>)

- 6 5 4 10 40 38

![image 156](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile156.png>)

![image 157](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile157.png>)

![image 158](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile158.png>)

![image 159](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile159.png>)

![image 160](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile160.png>)

![image 161](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile161.png>)

![image 162](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile162.png>)

![image 163](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile163.png>)

- 7 8 7 11 72 69


![image 164](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile164.png>)

![image 165](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile165.png>)

![image 166](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile166.png>)

![image 167](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile167.png>)

![image 168](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile168.png>)

![image 169](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile169.png>)

![image 170](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile170.png>)

![image 171](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile171.png>)

We see that our new criterion indeed gives (slightly) stronger bounds. For the asymptotic case when L is large, note that the RHS of (6) can be approximated:

RHS ≤ c−k(α + (1 + α(c − 1)(L − 1))k(1 + (c − 1)α)) ≤ c−k(1 + α(c − 1)L)k

1

ck (c−1)kL

![image 172](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile172.png>)

k−1 −1

![image 173](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile173.png>)

Thus, setting α =

(c−1)L , we satisfy the LLLL criterion if

![image 174](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile174.png>)

ck(1 − 1/k)k−1 (c − 1)k

L ≤

.

![image 175](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile175.png>)

which is slightly better than the bounds from the conventional LLLL.

- 4.3 Second Hamiltonian cycle


Consider a k-regular graph G, with a Hamiltonian cycle C. Under what conditions is there a second Hamiltonian cycle C′ (that is, the cycle C is not unique)? In [26], Thomassen showed that a suﬃcient condition for the existence of the second cycle is a set of vertices S ⊆ V which is simultaneously a dominating set for G − C and an independent set for C. Speciﬁcally, S must satisfy the following two conditions:

- 1. If v and w are adjacent on the cycle C, then v and w are not both in S.
- 2. For any vertex v ∈ G, either v is in S, or it is connected to a vertex w ∈ S via some edge e ∈/ C.


Using the LLL, Thomassen then showed that this can always be satisﬁed as long as k ≥ 73. This was based on a simple random process, in which each vertex was put into S independently with probability p. Using the LLL with a much more sophisticated random process, Haxell showed that this condition can be satisﬁed as long as k ≥ 23 [14]. It was conjectured that this condition could be satisﬁed as long as k ≥ 5.

Haxell’s proof is quite involved, and our LLLL criterion would oﬀer little beneﬁt for it (as all the badevents involve many vertices). In [9], there was a simple proof using the LLLL that this condition can be satisﬁed as long as k ≥ 48. Our LLLL criterion can be used to give another very simple proof under the condition k ≥ 43. While not as good as Haxell’s construction, the proof is far simpler.

- Theorem 4.2. If G is a k-regular graph for k ≥ 43 and C is a Hamiltonian cycle of G, then there is a G − C-dominating, C-independent set S ⊆ V .


Proof. Each vertex enters into S independently with probability p. There are two types of bad-events: for each edge of C, there is an event of type A, that the endpoints are both in S; for each vertex of G − C, there is an event of type B, that v nor its k − 2 neighbors outside of C are in S. We assign µ(B) = a for all events of the ﬁrst type, and µ(B) = b for all events of the second type. Note that events of type A are lopsidependent only with events of type B, and vice versa.

Now consider an event of type A. It has probability p2. There are two vertices in this edge, each of which participates in k − 2 events of type B. Similarly, an event of type B has probability (1 − p)k−1, and each of the k − 1 vertices participates in two events of type A. Hence our LLLL criteria can be stated as

a ≥ p2(1 + (k − 2)b)2, b ≥ (1 − p)k−1(1 + 2a)k−1 Routine calculations show that this is solvable for k ≥ 43.

![image 176](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile176.png>)

![image 177](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile177.png>)

![image 178](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile178.png>)

![image 179](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile179.png>)

- 4.4 Independent transversals


Suppose we are given a graph G, along with a partition of the vertices V = V1 ⊔ ··· ⊔ Vk in which each class has size exactly b. We would like to select one vertex from each class; this is known as a transversal. If we select a transversal which is also an independent set, this is known as an independent transversal. Typically, bounds for the existence of an independent transversal are given in terms of the maximum degree ∆.

Haxell showed that when b ≥ 2∆, an independent transversal exists, and this is the optimal constant [13]. However, this result is non-constructive. The best algorithms for ﬁnding independent transversals come from the MT algorithm. A simple application of LLL shows that b ≥ 2e∆ suﬃces to guarantee an independent transversal. Pegden’s criterion shows that b ≥ 4∆ suﬃces. We slightly can improve this, obtaining the best constructive bound known so far:

Proposition 4.3. Suppose b ≥ 4∆ − 1. Then the MT algorithm ﬁnds an independent transversal in polynomial expected time. Furthermore, under these conditions, the Parallel MT algorithm runs in time

4(b − 1)∆ b2 − 4(b − 1)∆

logO(1) n × min(1,

)

![image 180](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile180.png>)

Proof. We prove the ﬁrst statement only; the second is similar.

Each edge corresponds to a bad-event; it has probability 1/b2. For an assignable set of neighbors to an edge f = u,v , we may choose f, or we may choose u′,x where u′ = u is in the class of u, or we may choose v′,x where v′ = v is in the class of v; or we may choose both. This gives us the criterion

α ≥ b−2(α + (1 + (b − 1)∆α)2) which is satisﬁed by some α ≥ 0 whenever b ≥ 4∆ − 1.

![image 181](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile181.png>)

![image 182](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile182.png>)

![image 183](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile183.png>)

![image 184](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile184.png>)

Note that the second condition gives an RNC algorithm either if b ≥ 4∆(1 + ǫ) for some constant ǫ > 0, or if b ≥ 4∆ − 1 and ∆ = logO(1) n.

- 4.5 Oﬀ-diagonal Ramsey numbers


In this section, we consider the classical oﬀ-diagonal Ramsey problem on graphs. Suppose we wish to twocolor – with colors red and blue – the edges of Kn, the complete graph on n vertices. We wish to avoid any red s-cliques or blue t-cliques in the resulting graph. The largest value n for which it is possible to avoid such cliques is known as the oﬀ-diagonal Ramsey number R(s,t). There are many aspects and generalizations studied for Ramsey numbers. One frequently studied scenario is when s is held constant while t → ∞.

s+1

It was shown in [25], using the LLL, that when n ≤ c(t/ logt)

2 and c is a constant (depending on s) that such a coloring is possible. In other words, R(s,t) ≥ Ωs (t/ logt)

![image 185](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile185.png>)

s+1

2 . For speciﬁc values of s, better bounds are known (e.g., R(3,t) = Θ(t2/ logt)), but this is the best bound known for general s. The algorithmic challenge is to eﬃciently ﬁnd colorings of the edges of Kn that avoid red Ks and blue Kt. Such algorithms should operate when n is as large as possible, ideally up to R(s,t). Unfortunately, the LLL construction of [25] does not lead to eﬃcient serial or parallel algorithms. The main roadblock is that there is a bad-event for each t-clique, so that ﬁnding a bad event requires exponential time. For speciﬁc values of s, again, there are known polynomial-time algorithms for ﬁnding good colorings. But in general there is no algorithm that corresponds to the best bounds.

![image 186](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile186.png>)

In [10], an algorithm based on MT was proposed for ﬁnding such colorings. The basic idea of [10] is to ﬁnd and resample red Ks, while ignoring blue Kt. One then shows that, high probability, none of the Kt became blue, even though we did not explicitly check or resample them. The serial running time of this would be Ωs(ns), to search for the red Ks; no parallel algorithm was given.

These results depend on the “MT-distribution”; that is, the distribution on the variables when the MT algorithm terminates. We will show that in the MT distribution there is only a small probability of a blue Kt. Though we did not show this explicitly in Section 2, it is not hard to use Lemma 2.7 to derive a bound on the MT distribution, similar to [10]:

- Theorem 4.4. Suppose we have a set of bad-events B which satisﬁes our LLLL criterion which weights µ. Suppose E is any atomic event (which is not itself in B). Then the probability that E is true at the end of the MT algorithm is given by

P(E is true at end of MT) ≤ PΩ(E)

Y orderable to E B′∈Y

µ(B′)

Proof. One can construct a witness tree for the ﬁrst time that E becomes true. Such a witness tree is rooted in E, and its children correspond to a set of bad-events which is orderable to E. Thus, the result follows by taking a union-bound over all such witness trees. See [10] for more details.

![image 187](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile187.png>)

![image 188](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile188.png>)

![image 189](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile189.png>)

![image 190](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile190.png>)

Using this result,we will give a serial algorithm for oﬀ-diagonal Ramsey coloring with a much better run-time, and we will also give a parallel algorithm based on our Parallel Resampling Algorithm.

- Theorem 4.5. Consider the problem of ﬁnding a red-blue coloring of the edges of Kn avoiding red Ks and blue Kt. Deﬁne


1 s−2

s+1 2

![image 191](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile191.png>)

2(s − 2)! s(s − 1)(

2 s

2 s − 1

![image 192](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile192.png>)

−

.

cs =

+ 1

![image 193](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile193.png>)

![image 194](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile194.png>)

![image 195](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile195.png>)

)

s 2

- 1. Suppose n ≤ (logt t)

![image 196](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile196.png>)

s+1

![image 197](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile197.png>)

2 (cs −o(1)). There is a serial randomized algorithm which runs in time ns/4+O(1) and produces a correct solution when it halts, except with a failure probability of n−Ω(1).

- 2. Suppose s is constant and n ≤ (logt t)


s+1

2 (cs − o(1)). There is a parallel randomized algorithm which runs in time sO(1) logO(1) n time using ns/4+O(1) processors, and produces a correct solution when it halts, except with a failure probability of n−Ω(1).

![image 198](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile198.png>)

![image 199](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile199.png>)

Proof. The proofs of both parts are very similar; to simplify the discussion, we will focus mostly on the serial algorithm, noting any diﬀerence between that and the parallel algorithm.

The probability space Ω is deﬁned by coloring each edge red with probability

p =

2(s − 2)! (s − 1)s

![image 200](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile200.png>)

2 s2−s−2

![image 201](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile201.png>)

−2 s+1

n

![image 202](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile202.png>)

and blue otherwise. We ignore the blue Kt and so our only bad-events are the red Ks. Each bad-event has probability q = p(s

). Observe that each bad-event is lopsidependent with only a single bad-event, namely itself. So the LLLL criterion is satisﬁed, setting µ(B) = 1−qq for all bad-events B.

2

![image 203](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile203.png>)

Now consider an arbitrary Kt, and let E be the event that it is red at the end of the MT. We have

t 2

). The orderable sets for this event can be found as follows: for each of the 2 t edges, we may select zero or one blue Ks. Thus, by Theorem 4.4, the probability that E holds at the end of MT is given by

- PΩ(E) = (1 − p)(


(t

)

n − 2 s − 2

2

P(Kt is blue) ≤ (1 − p)(1 +

µ)

2 −s2+s+2

s(s − 1) 2(s − 2)!

2 s − s2

![image 204](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile204.png>)

≤ 1 −

1 +

![image 205](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile205.png>)

![image 206](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile206.png>)

t 2

−2

s+1 where c′s =

c′sn

≤ exp −

![image 207](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile207.png>)

−2 s+1

n

![image 208](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile208.png>)

(t

)

2

2(s − 2)! s(s − 1)

![image 209](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile209.png>)

2

2 s − s2

![image 210](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile210.png>)

s2−s−2 1 +

![image 211](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile211.png>)

Hence, the expected number of blue Kt is at most

E[Blue Kt] ≤

nt t!

−2

exp(−t2c′sn

s+1/2)

![image 212](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile212.png>)

![image 213](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile213.png>)

In order to avoid all blue Kt with high probability, say with probability n−φ for φ > 0 some arbitrary constant, we must take

s+1 2

  

  

![image 214](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile214.png>)

c′st2 (s + 1)(φ + t)log c

s+1 2

![image 215](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile215.png>)

(cs − os(1))

n ≤

= t/ logt

![image 216](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile216.png>)

2 (s+1)(φ+t)

′ st2(t!)−

![image 217](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile217.png>)

![image 218](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile218.png>)

(s+1)(φ+t)

So far, we have shown that when we run the MT algorithm with the given parameters, then indeed we avoid Kt with high probability. The next thing we must examine is how to run the MT algorithm. In this problem, in which the bad-events are deﬁned to be red Ks, the MT algorithm is somewhat degenerate. The critical thing to note is that when we resample a bad-event, we can never create new bad-events. Thus, the most potentially time-consuming step of MT — repeatedly searching for any bad-events which are currently true — can be much simpliﬁed. At the beginning of the process, after we make the initial random color assignment but before we do any resamplings, we can enumerate all red Ks. For each such red Ks, we repeatedly sample the edges until the Ks is no longer red. The process of ﬁnding the red Ks can be aided by the fact that we are searching for them in a random graph — namely, the edges are red independently with probability p.

The simplest way to search for such red Ks seems to be through a branching process: we gradually build up red Kl, for l ≤ s. In this branching process, the expected number of red Kl is p(l

) n

l . Thus, the total time complexity of this branching process will be

2

s

n l

p(l

)

Time to ﬁnd red Ks ≤ nO(1)

2

l=0

(l − 1)2 2

≤ nO(1) exp( max l∈[0,s]

log p − l log l + l) ≤ ns/4+O(1) (by routine calculus)

l log n +

![image 219](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile219.png>)

This concludes part (1) of the theorem. As the Parallel Moser-Tardos algorithm simulates the serial algorithm, all the results about the MT distribution still remain true in the parallel setting; in particular we avoid the blue Kt with high probability. Also, one can enumerate the red Ks in parallel, using ns/4+O(1) processors and s stages, via the same type of branching process.

One can see easily that we satisfy the parallel LLLL criterion for n suﬃciently large, setting µ(B) = 1 for all B and ǫ = 1/2. All the bad events then use 2 s elements, and the total number of bad-events is nO

s(1),

and we have log B∈B µ(B) = Os(log n). Hence by Theorem 3.9, the Parallel Moser-Tardos terminates in time sO(1) logO(1) n whp.

![image 220](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile220.png>)

![image 221](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile221.png>)

![image 222](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile222.png>)

![image 223](<2015-harris-lopsidependency-moser-tardos-framework_images/imageFile223.png>)

# 5 Acknowledgments

Thanks to Aravind Srinivasan for many helpful comments and suggestions, as well as suggesting the algorithm for vertex-capacitated maximal edge covering. Thanks to the anonymous referees for their suggestions.

# References

- [1] Achlioptas, D., Iliopoulos, F.: Random walks that ﬁnd perfect objects and the Lovasz Local Lemma. Foundations of Computer Science (2014).
- [2] Albert, M., Frieze, A., Reed, B.: Multicoloured Hamilton Cycles. The Electronic Journal of Combinatorics 2-1, R10. (1995)
- [3] Bissacot, R., Fernandez, R., Procacci, A., Scoppola, B.: An improvement of the Lov´asz Local Lemma via cluster expansion. Combinatorics, Probability and Computing 20-5, pp. 709-719 (2011).
- [4] Chandrasekaran, K., Goyal, N., Haeupler, B.: Deterministic algorithms for the Lov´asz local lemma. SIAM Journal on Computing 42-6 , pp. 2132-2155 (2013)
- [5] Cook, S.: A Taxonomy of problems with fast parallel algorithms. Information and Control 64, pp. 2-22

(1985).

- [6] Erdo˝s, P., Lov´asz, L.: Problems and results on 3-chromatic hypergraphs and some related questions. In A. Hajnal, R. Rado, and V. T. Sos, eds. Inﬁnite and Finite Sets II, pp. 607-726 (1975).
- [7] Erdo˝s, P., Spencer, J.: Lopsided Lov´asz Local Lemma and Latin transversals. Discrete Applied Math 30, pp. 151-154 (1990).
- [8] Gebauer, H., Szabo´, T., Tardos, G.: The local lemma is tight for SAT. Symposium on Discrete Algorithms (SODA) (2011).
- [9] Ghandehari, M., Hatami, H.: A note on independent dominating sets and second Hamiltonian cycles. Submitted for publication.
- [10] Haeupler, B., Saha, B., Srinivasan, A.: New constructive aspects of the Lov´asz Local Lemma. Journal of the ACM, 58-6, 2011.
- [11] Harris, D.: The Moser-Tardos lopsidependency criterion can be stronger than Shearer’s criterion. arxiv
- [12] Harris, D., Srinivasan, A.: A constructive algorithm for the Lov´asz Local Lemma on permutations. Symposium on Discrete Algorithms (SODA) (2014).
- [13] Haxell, P.: A note on vertex list coloring. Combinatorics, Probability and Computing 10, pp. 345-348

(2001).

- [14] Haxell, P., Seamonez, B., Verstraete, J.: Independent dominating sets and hamiltonian cycles. Journal of Graph Theory 54-3, pp. 233-244 (2007)
- [15] Kolipaka, K., Szegedy, M.: Moser and Tardos meet Lov´asz. Symposium on Theory of Computing, pp. 235-244 (2011).
- [16] Kolipaka, K., Szegedy, M., Xu, Y.: A sharper local lemma with improved applications. In “Approximation, Randomization, and Combinatorial Optimizationn. Algorithms and Techniques” LNCS 7408, pp. 603-614 (2012).


- [17] Kratochv´ıl, J., Savick´y, P., Tuza, Z.: One more occurrence of variables makes satisﬁability jump from trivial to NP-complete. SIAM Journal of computing 22-1, pp. 203-210 (1993).
- [18] Lu, L., Sz´ek´ely, L.: Using Lov´asz Local Lemma in the space of random injections. The Electronic Journal of Combinatorics 13-R63 (2007).
- [19] Lu, L., Sz´ek´ely, L.: A new asymptotic enumeration technique: the Lov´asz local lemma. arXiv:0905.3983v3 (2011).
- [20] Luby, M., Nisan, N.: A parallel approximation algorithm for positive linear programming. Symposium on Theory of Computing, pp. 448-457 (1993).
- [21] McDiarmid, C.: Hypergraph coloring and the Lov´asz Local Lemma. Journal of Discrete Mathematics 167/168, pp. 481-486 (1995).
- [22] Moser, R., Tardos, G.: A constructive proof of the general Lov´asz Local Lemma. Journal of the ACM 57-2, pp. 11:1-11:15 (2010).
- [23] Pegden, W.: An extension of the Moser-Tardos algorithmic local lemma. SIAM Journal of Discrete Math 28-2, pp. 911-917 (2014).
- [24] Shearer, J. B.: On a problem of Spencer. Combinatorica 5, pp. 241-245 (1985).
- [25] Spencer, J.: Asymptotic lower bounds for Ramsey functions. Discrete Mathematics 20, pp. 69-76 (1977)
- [26] Thomassen, C. Independent dominating sets and a second Hamiltonian cycle in regular graphs. Journal of Combinatorial Theory B-72, pp. 104-109 (1998)


