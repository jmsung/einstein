Bounds on entanglement dimensions and quantum graph parameters via noncommutative polynomial optimization

Sander Gribling∗ David de Laat† Monique Laurent‡

arXiv:1708.09696v2[math.OC]9Jan2018

Abstract

In this paper we study optimization problems related to bipartite quantum correlations using techniques from tracial noncommutative polynomial optimization. First we consider the problem of ﬁnding the minimal entanglement dimension of such correlations. We construct a hierarchy of semideﬁnite programming lower bounds and show convergence to a new parameter: the minimal average entanglement dimension, which measures the amount of entanglement needed to reproduce a quantum correlation when access to shared randomness is free. Then we study optimization problems over synchronous quantum correlations arising from quantum graph parameters. We introduce semideﬁnite programming hierarchies and unify existing bounds on quantum chromatic and quantum stability numbers by placing them in the framework of tracial optimization.

# 1 Introduction

- 1.1 Bipartite quantum correlations


One of the distinguishing features of quantum mechanics is quantum entanglement, which allows for nonclassical correlations between spatially separated parties. In this paper we consider the problems of quantifying the advantage entanglement can bring (ﬁrst investigated through Bell inequalities in the seminal work [3]) and quantifying the minimal amount of entanglement necessary for generating a given correlation (initiated in [5] and continued, e.g., in [38, 54, 47]).

Quantum entanglement has been widely studied in the bipartite correlation setting (for a survey, see, e.g., [39]). Here we have two parties, Alice and Bob, where Alice receives a question s taken from a ﬁnite set S and Bob receives a question t taken from a ﬁnite set T. The parties do not know each other’s questions, and after receiving the questions they do not communicate. Then, according to some predetermined protocol, Alice returns an answer a from a ﬁnite set A and Bob returns an answer b from a ﬁnite set B. The probability that the parties answer (a,b) to questions (s,t) is given by a bipartite correlation P(a,b|s,t), which satisﬁes P(a,b|s,t) ≥ 0 for all (a,b,s,t) ∈ Γ and a,b P(a,b|s,t) = 1 for all (s,t) ∈ S × T. Throughout we set Γ = A × B × S × T. Which bipartite correlations P = (P(a,b|s,t)) ∈ RΓ are possible depends on the additional resources available to the two parties Alice and Bob.

If the parties do not have access to additional resources, then the correlation is deterministic, which means it is of the form P(a,b|s,t) = PA(a|s)PB(b|t), with PA(a|s) and PB(b|t) taking values in {0,1} and a PA(a|s) = b PB(b|t) = 1 for all s,t. If the parties have access to local randomness, then PA and PB take values in [0,1]. If the parties have access to shared randomness, then the resulting correlation is a convex combination of deterministic correlations

![image 1](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile1.png>)

∗CWI and QuSoft, Amsterdam, the Netherlands. Supported by the Netherlands Organization for Scientiﬁc Research, grant number 617.001.351. gribling@cwi.nl

†CWI and QuSoft, Amsterdam, the Netherlands. Supported by the Netherlands Organization for Scientiﬁc Research, grant number 617.001.351, and by the ERC Consolidator Grant QPROGRESS 615307. mail@daviddelaat.nl

‡CWI and QuSoft, Amsterdam, and Tilburg University, Tilburg, the Netherlands. laurent@cwi.nl

and is said to be a classical correlation. The classical correlations form a polytope, denoted Cloc(Γ), whose valid inequalities are known as Bell inequalities [3].

We are interested in the quantum setting, where the parties have access to a shared quantum state on which they can perform measurements. The quantum setting can be modeled in diﬀerent ways, leading to the so-called tensor and commuting models; see the discussion, e.g., in [52, 31, 11].

In the tensor model, Alice and Bob each have access to “one half” of a ﬁnite dimensional quantum state, which is modeled by a unit vector ψ ∈ Cd ⊗ Cd. Alice and Bob determine their answers by performing a measurement on their part of the state. Such a measurement is modeled by a positive operator valued measure (POVM), which consists of a set of d × d Hermitian positive semideﬁnite matrices labeled by the possible answers and summing to the identity matrix. If Alice uses the POVM {Esa}a∈A when she gets question s ∈ S and Bob uses the POVM {Ftb}b∈B when he gets question t ∈ T, then the probability of obtaining the answers (a,b) is given by

P(a,b|s,t) = Tr((Esa ⊗ Ftb)ψψ∗) = ψ∗(Esa ⊗ Ftb)ψ. (1)

If the state ψ cannot be written as a single tensor product ψA ⊗ ψB, then ψ is entangled, which means it can be used to produce a nonclassical correlation P.

A correlation of the above form (1) is a quantum correlation, realizable in the tensor model in local dimension d (or in dimension d2). Let Cqd(Γ) be the set of such correlations and deﬁne

Cqd(Γ).

Cq(Γ) =

d∈N

Denote the smallest dimension needed to realize P ∈ Cq(Γ) in the tensor model by Dq(P) = min d2 : d ∈ N, P ∈ Cqd(Γ) . (2)

The set Cq1(Γ) contains the deterministic correlations. Hence, by Carathe´odory’s theorem, Cloc(Γ) ⊆ Cqc(Γ) holds for c = |Γ| + 1 − |S||T|; that is, quantum entanglement can be used as an alternative to shared randomness. If A, B, S, and T all contain at least two elements, then

Bell [3] shows the inclusion Cloc(Γ) ⊆ Cq(Γ) is strict; that is, quantum entanglement can be used to obtain nonclassical correlations.

The second commonly used model to deﬁne quantum correlations is the commuting model (or relativistic ﬁeld theory model). Here a correlation P ∈ RΓ is called a commuting quantum correlation if it is of the form

P(a,b|s,t) = Tr(XsaYtbψψ∗) = ψ∗(XsaYtb)ψ, (3)

where {Xsa}a and {Ytb}b are POVMs consisting of bounded operators on a separable Hilbert space H, satisfying [Xsa,Ytb] = XsaYtb − YtbXsa = 0 for all (a,b,s,t) ∈ Γ, and where ψ is a unit vector in H. Such a correlation is said to be realizable in dimension d = dim(H) in the commuting model. Denote the set of such correlations by Cqcd (Γ) and set Cqc(Γ) = Cqc∞(Γ). The smallest dimension needed to realize a quantum correlation P ∈ Cqc(Γ) is given by

Dqc(P) = min d ∈ N ∪ {∞} : P ∈ Cqcd (Γ) . (4)

We have Cqd(Γ) ⊆ Cqcd2(Γ), which follows by setting Xsa = Esa ⊗ I and Ytb = I ⊗ Ftb. This shows Dqc(P) ≤ Dq(P) for all P ∈ Cq(Γ).

The minimum Hilbert space dimension in which a given quantum correlation P can be realized quantiﬁes the minimal amount of entanglement needed to represent P. Computing Dq(P) is NP-hard [49], so a natural question is to ﬁnd good lower bounds for the parameters Dq(P) and Dqc(P). A main contribution of this paper is proposing a hierarchy of semideﬁnite programming lower bounds for these parameters.

As said above we have Cqd(Γ) ⊆ Cqcd2(Γ). Conversely, each ﬁnite dimensional commuting quantum correlation can be realized in the tensor model, although not necessarily in the same dimension [52] (see, e.g., [11] for a proof). This shows

Cqcd (Γ) ⊆ Cqc(Γ).

Cq(Γ) =

d∈N

Using a direct sum construction one can show ∪d∈NCqcd (Γ) and Cqc(Γ) are convex. Whether the two sets Cq(Γ) and Cqc(Γ) coincide is known as Tsirelson’s problem. In a recent breakthrough Slofstra [48] showed that Cq(Γ) is not closed for |A| ≥ 8, |B| ≥ 2, |S| ≥ 184, |T| ≥ 235. More recently it was shown in [13] that the same holds for |A| ≥ 2, |B| ≥ 2, |S| ≥ 5, |T| ≥ 5. Hence, for such Γ there is a sequence {Pi} ⊆ Cq(Γ) with Dq(Pi) → ∞. Moreover, since Cqc(Γ) is closed [14, Prop. 3.4], the inclusion Cq(Γ) ⊆ Cqc(Γ) is strict, thus settling Tsirelson’s problem. Whether the closure of Cq(Γ) equals Cqc(Γ) for all Γ is equivalent to Connes’ embedding conjecture in operator theory [20, 37].

Further variations on the above deﬁnitions are possible. For instance, we can consider a mixed state ρ (a Hermitian positive semideﬁnite matrix ρ with Tr(ρ) = 1) instead of a pure state ψ, where we replace the rank 1 matrix ψψ∗ by ρ in the above deﬁnitions. By convexity this does not change the sets Cq(Γ) and Cqc(Γ). It is shown in [47] that this also does not change the parameter Dq(P), but it is unclear whether or not Dqc(P) might decrease. Another variation would be to use projection valued measures (PVMs) instead of POVMs, where the operators are projectors instead of positive semideﬁnite matrices. This again does not change the sets Cq(Γ) and Cqc(Γ) [35], but the dimension parameters can be larger when restricting to PVMs.

When the two parties have the same question sets (S = T) and the same answer sets (A = B), a bipartite correlation P ∈ RΓ is called synchronous if P(a,b|s,s) = 0 for all s and a = b. The sets of synchronous (commuting) quantum correlations, denoted Cq,s(Γ) and Cqc,s(Γ), are rich enough, so that Connes’ embedding conjecture still holds if and only if cl(Cq,s(Γ)) = Cqc,s(Γ) for all Γ [12, Thm. 3.7]. The quantum graph parameters discussed in Section 1.3 will be deﬁned through optimization problems over these sets.

A matrix M ∈ Rn×n is completely positive semideﬁnite if there exist d ∈ N and Hermitian positive semideﬁnite matrices X1,... ,Xn ∈ Cd×d with M = (Tr(XiXj)). The minimal such d is its completely positive semideﬁnite rank, denoted cpsd-rank(M). Completely positive semideﬁnite matrices are used in [25] to model quantum graph parameters and the completely positive semideﬁnite rank is investigated in [43, 16, 44, 15]. By combining the proofs from [46] (see also [28]) and [41] one can show the following link between synchronous correlations and completely positive semideﬁnite matrices.1

Proposition A.1. The smallest local dimension in which a synchronous quantum correlation P can be realized is given by the completely positive semideﬁnite rank of the matrix MP indexed by S × A with entries (MP)(s,a),(t,b) = P(a,b|s,t).

In [15] we use techniques from tracial polynomial optimization to deﬁne a semideﬁnite programming hierarchy {ξrcpsd(M)} of lower bounds on cpsd-rank(M). By the above result this hierarchy gives lower bounds on the smallest local dimension in which a synchronous correlation can be realized in the tensor model. However, in [15] we show that the hierarchy typically does not converge to cpsd-rank(M) but instead (under a certain ﬂatness condition) to a parameter ξ∗cpsd(M), which can be seen as a block-diagonal version of the completely positive semideﬁnite rank.

Here we use similar techniques, now exploiting the special structure of quantum correlations, to construct a hierarchy {ξrq(P)} of lower bounds on the minimal dimension Dq(P) of any – not necessarily synchronous – quantum correlation P. The hierarchy converges (under ﬂatness)

![image 2](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile2.png>)

1See Appendix A for a proof.

to a parameter ξ∗q(P), and using the additional structure we can show that ξ∗q(P) is equal to an interesting parameter Aq(P) ≤ Dq(P). This parameter describes the minimal average entanglement dimension of a correlation when the parties have free access to shared randomness; see Section 1.2.

In the rest of the introduction we give a road map through the contents of the paper and state the main results. We will introduce the necessary background along the way.

## 1.2 A hierarchy for the average entanglement dimension

We are interested in the minimal entanglement dimension needed to realize a given correlation P ∈ Cq(Γ). If P is deterministic or only uses local randomness, then Dq(P) = Dqc(P) = 1. But other classical correlations (which use shared randomness) have Dq(P) ≥ Dqc(P) > 1, which means the shared quantum state is used as a shared randomness resource. In [5] the concept of dimension witness is introduced, where a d-dimensional witness is deﬁned as a halfspace containing conv(Cqd(Γ)), but not the full set Cq(Γ). As a measure of entanglement this suggests the parameter

inf maxi∈[I]Dq(Pi) : I ∈ N, λ ∈ RI+,

I

λi = 1, P =

i=1

I

λiPi, Pi ∈ Cq(Γ) . (5)

i=1

Observe that, for a bipartite correlation P, this parameter is equal to 1 if and only if P is classical. Hence, it more closely measures the minimal entanglement dimension when the parties have free access to shared randomness. From an operational point of view, (5) can be interpreted as follows. Before the game starts the parties select a ﬁnite number of pure states ψi (i ∈ I) (instead of a single one), in possibly diﬀerent dimensions di, and POVMs {Esa(i)}a, {Ftb(i)}b for each i ∈ I and (s,t) ∈ S × T. As before, we assume that the parties cannot communicate after receiving their questions (s,t), but now they do have access to shared randomness, which they use to decide on which state ψi to use. The parties proceed to measure state ψi using POVMs {Esa(i)}a, {Ftb(i)}b, so that the probability of answers (a,b) is given by the quantum correlation Pi. Equation (5) then asks for the largest dimension needed in order to generate P when access to shared randomness is free.

It is not clear how to compute (5). Here we propose a variation of (5), and we provide a hierarchy of semideﬁnite programs that converges to it under ﬂatness. Instead of considering the largest dimension needed to generate P, we consider the average dimension. That is, we minimize i∈I λiDq(Pi) over all convex combinations P = i∈I λiPi. Hence, the minimal average entanglement dimension is given by

Aq(P) = inf

I

λiDq(Pi) : I ∈ N, λ ∈ RI+,

i=1

I

λi = 1, P =

i=1

I

λiPi, Pi ∈ Cq(Γ)

i=1

in the tensor model. In the commuting model, Aqc(P) is given by the same expression with Dq(Pi) replaced by Dqc(Pi). Observe that we need not replace Cq(Γ) by Cqc(Γ) since Dqc(P) = ∞ for any P ∈ Cqc(Γ) \ Cq(Γ).

It follows by convexity that for the above deﬁnitions it does not matter whether we use pure or mixed states. We show that for the average minimal entanglement dimension it also does not matter whether we use the tensor or commuting model.

- Proposition 2.1. For any P ∈ Cq(Γ) we have Aq(P) = Aqc(P).


We have Aq(P) ≤ Dq(P) and Aqc(P) ≤ Dqc(P) for P ∈ Cq(Γ), with equality if P is an extreme point of Cq(Γ). Hence, we have Dq(P) = Dqc(P) if P is an extreme point of Cq(Γ). We show that the parameter Aq(P) can be used to distinguish between classical and nonclassical correlations.

- Proposition 2.2. For a correlation P ∈ RΓ we have Aq(P) = 1 if and only if P ∈ Cloc(Γ).

As mentioned before, there exist Γ for which Cq(Γ) is not closed [48, 13], which implies the existence of a sequence {Pi} ⊆ Cq(Γ) such that Dq(P) → ∞. We show this also implies the existence of such a sequence with Aq(Pi) → ∞.

- Proposition 2.3. If Cq(Γ) is not closed, there exists {Pi} ⊆ Cq(Γ) with Aq(Pi) → ∞.


Using tracial polynomial optimization we construct a hierarchy {ξrq(P)} of lower bounds on Aqc(P). For each r ∈ N this is a semideﬁnite program, and for r = ∞ it is an inﬁnite dimensional semideﬁnite program. We further deﬁne a (hyperﬁnite) variation ξ∗q(P) of ξ∞q (P) by adding a ﬁnite rank constraint, so that

ξ1q(P) ≤ ξ2q(P) ≤ ... ≤ ξ∞q (P) ≤ ξ∗q(P) ≤ Aqc(P).

We do not know whether ξ∞q (P) = ξ∗q(P) always holds; this question is related to Connes’ embedding conjecture [22]. First we show that we imposed enough constraints in the bounds ξrq(P) so that ξ∗q(P) = Aqc(P).

- Proposition 2.8. For any P ∈ Cq(Γ) we have ξ∗q(P) = Aqc(P).

Then we show that the inﬁnite dimensional semideﬁnite program ξ∞q (P) is the limit of the ﬁnite dimensional semideﬁnite programs.

- Proposition 2.9. For any P ∈ Cq(Γ) we have ξrq(P) → ξ∞q (P) as r → ∞.

Finally we give a criterion under which ﬁnite convergence ξrq(P) = ξ∗q(P) holds. The deﬁnition of ﬂatness follows later in the paper; here we only note that it is an easy to check criterion given the output of the semideﬁnite programming solver.

- Proposition 2.10. If ξrq(P) admits a (⌈r/3⌉ + 1)-ﬂat optimal solution, ξrq(P) = ξ∗q(P).


## 1.3 Quantum graph parameters

Nonlocal games have been introduced in quantum information theory as abstract models to quantify the power of entanglement, in particular, in how much the sets Cq(Γ) and Cqc(Γ) diﬀer from Cloc(Γ). A nonlocal game is deﬁned by a probability distribution π: S × T → [0,1] and a predicate f : A × B × S × T → {0,1}. Alice and Bob receive a question pair (s,t) ∈ S × T with probability π(s,t). They know the game parameters π and f, but they do not know each other’s questions, and they cannot communicate after they receive their questions. Their answers (a,b) are determined according to some correlation P ∈ RΓ, called their strategy, on which they may agree before the start of the game, and which can be classical or quantum depending on whether P belongs to Cloc(Γ), Cq(Γ), or Cqc(Γ). Then their corresponding winning probability is given by

P(a,b|s,t)f(a,b,s,t). (6)

π(s,t)

(s,t)∈S×T

(a,b)∈A×B

A strategy P is called perfect if the above winning probability is equal to one, that is, if for all (a,b,s,t) ∈ Γ we have

π(s,t) > 0 and f(a,b,s,t) = 0 =⇒ P(a,b|s,t) = 0.

Computing the maximum winning probability of a nonlocal game is an instance of linear optimization over Cloc(Γ) in the classical setting, and over Cq(Γ) or Cqc(Γ) in the quantum setting. Since the inclusion Cloc(Γ) ⊆ Cq(Γ) can be strict, the winning probability can be higher when the parties have access to entanglement. In fact there are nonlocal games that can

be won with probability 1 by using entanglement, but with probability strictly less than 1 in the classical setting.

The quantum graph parameters are analogues of the classical parameters deﬁned through the coloring and stability number games as described below. These nonlocal games use the set [k] (whose elements are denoted as a,b) and the set V of vertices of G (whose elements are denoted as i,j) as question and answer sets.

In the quantum coloring game, introduced in [1, 9], we have a graph G = (V,E) and an integer k. Here we have question sets S = T = V and answer sets A = B = [k], and the distribution π is strictly positive on V × V . The predicate f is such that the players’ answers have to be consistent with having a k-coloring of G; that is, f(a,b,i,j) = 0 precisely when (i = j and a = b) or ({i,j} ∈ E and a = b). This expresses the fact that if Alice and Bob receive the same vertex they should return the same color and if they receive adjacent vertices they should return distinct colors. A perfect classical strategy exists if and only if a perfect deterministic strategy exists, and a perfect deterministic strategy corresponds to a k-coloring of G. Hence the smallest number k of colors for which there exists a perfect classical strategy is equal to the classical chromatic number χ(G). It is therefore natural to deﬁne the quantum chromatic number as the smallest k for which there exists a perfect quantum strategy. Since such a strategy is necessarily synchronous we get the following deﬁnition.

- Deﬁnition 1.1. The (commuting) quantum chromatic number χq(G) (resp., χqc(G)) is the smallest integer k ∈ N for which there exists a synchronous correlation P = (P(a,b|i,j)) in Cq,s([k]2 × V 2) (resp., Cqc,s([k]2 × V 2)) such that

P(a,a|i,j) = 0 for all a ∈ [k],{i,j} ∈ E.

In the quantum stability number game, introduced in [28, 45], we again have a graph G = (V,E) and k ∈ N, but now we use the question set [k] × [k] and the answer set V × V . The distribution π is again strictly positive on the question set and now the predicate f of the game is such that the players’ answers have to be consistent with having a stable set of size k, that is, f(i,j,a,b) = 0 precisely when (a = b and i = j) or (a = b and (i = j or {i,j} ∈ E)). This expresses the fact that if Alice and Bob receive the same index a = b ∈ [k] they should answer with the same vertex i = j of G, and if they receive distinct indices a = b from [k] they should answer with distinct nonadjacent vertices i and j of G. There is a perfect classical strategy precisely when there exists a stable set of size k, so that the largest integer k for which there exists a perfect classical strategy is equal to the stability number α(G). Again, such a strategy is necessarily synchronous, so we get the following deﬁnition.

- Deﬁnition 1.2. The (commuting) stability number αq(G) (resp., αqc(G)) is the largest integer k ∈ N for which there exists a synchronous correlation P = (P(i,j|a,b)) in Cq,s(V 2 × [k]2) (resp., Cqc,s(V 2 × [k]2)) such that


P(i,j|a,b) = 0 whenever (i = j or {i,j} ∈ E) and a = b ∈ [k].

The classical parameters χ(G) and α(G) are NP-hard. The same holds for the quantum coloring number χq(G) [19] and also for the quantum stability number αq(G) in view of the following reduction to coloring shown in [28]:

χq(G) = min{k ∈ N : αq(G Kk) = |V |}. (7)

Here G Kk is the Cartesian product of the graph G = (V,E) and the complete graph Kk. By construction we have χqc(G) ≤ χq(G) ≤ χ(G) and α(G) ≤ αq(G) ≤ αqc(G). The separations between χq(G) and χ(G), and between αq(G) and α(G), can be exponentially large in the number of vertices; this is the case for the graphs with vertex set {±1}n for n a multiple of 4, where two vertices are adjacent if they are orthogonal [1, 28, 29]. While it was recently shown

that the sets Cq,s(Γ) and Cqc,s(Γ) can be diﬀerent, it is not known whether there is a separation between the parameters χq(G) and χqc(G), and between αq(G) and αqc(G).

We now give an overview of the results of Section 3 and refer to that section for formal deﬁnitions. We ﬁrst reformulate the quantum graph parameters in terms of C∗-algebras, which allows us to use techniques from tracial polynomial optimization to formulate bounds on the quantum graph parameters. We deﬁne a hierarchy {γrcol(G)} of lower bounds on the commuting quantum chromatic number and a hierarchy {γrstab(G)} of upper bounds on the commuting quantum stability number. We show the following convergence results for these hierarchies.

Proposition 3.2. There is an r0 ∈ N such that γrcol(G) = χqc(G) and γrstab(G) = αqc(G) for all r ≥ r0. Moreover, if γrcol(G) admits a ﬂat optimal solution, then γrcol(G) = χq(G), and if γrstab(G) admits a ﬂat optimal solution, then γrstab(G) = αq(G).

Then we deﬁne tracial analogues {ξrstab(G)} and {ξrcol(G)} of Lasserre type bounds on α(G) and χ(G) that provide hierarchies of bounds for their quantum analogues. These bounds are more economical than the bounds γrcol(G) and γrstab(G) (since they use less variables) and also permit to recover some known bounds for the quantum parameters. We show that ξ∗stab(G), which is the parameter ξ∞stab(G) with an additional rank constraint on the matrix variable, coincides with the projective packing number αp(G) from [45] and that ξ∞stab(G) upper bounds αqc(G).

Proposition 3.4. We have ξ∗stab(G) = αp(G) ≥ αq(G) and ξ∞stab(G) ≥ αqc(G).

Next, we consider the chromatic number. The tracial hierarchy {ξrcol(G)} uniﬁes two known bounds: the projective rank ξf(G), a lower bound on the quantum chromatic number from [28], and the tracial rank ξtr(G), a lower bound on the commuting quantum chromatic number from [41]. In [12, Cor. 3.10] it is shown that the projective rank and the tracial rank coincide if Connes’ embedding conjecture is true.

Proposition 3.6. We have ξ∗col(G) = ξf(G) ≤ χq(G) and ξ∞col(G) = ξtr(G) ≤ χqc(G).

We compare the hierarchies ξrcol(G) and γrcol(G), and the hierarchies ξrstab(G) and γrstab(G). For the coloring parameters, we show the analogue of reduction (7).

- Proposition 3.10. For r ∈ N ∪ {∞} we have γrcol(G) = min{k : ξrstab(G Kk) = |V |}.

We show an analogous statement for the stability parameters, when using the homomorphic

graph product of Kk with the complement of G, denoted here as Kk ⋆ G, and the following reduction shown in [28]:

αq(G) = max{k ∈ N : αq(Kk ⋆ G) = k}.

- Proposition 3.11. For r ∈ N ∪ {∞} we have γrstab(G) = max{k : ξrstab(Kk ⋆ G) = k}.

Finally, we show that the hierarchies {γrcol(G)} and {γrstab(G)} reﬁne the hierarchies {ξrcol(G)} and {ξrstab(G)}.

- Proposition 3.12. For r ∈ N ∪ {∞,∗}, ξrcol(G) ≤ γrcol(G) and ξrstab(G) ≥ γrstab(G).


## 1.4 Techniques from noncommutative polynomial optimization

To derive our bounds we use techniques from tracial polynomial optimization. This is a noncommutative extension of the widely used moment and sum-of-squares techniques from Lasserre [23] and Parrilo [40] in polynomial optimization, dealing with the problem of minimizing a multivariate polynomial over a feasible region deﬁned by polynomial inequalities. These techniques

have been adapted to the noncommutative setting in [31] and [11] for approximating the set Cqc(Γ) of commuting quantum correlations and the winning probability of nonlocal games over Cqc(Γ) (and, more generally, computing Bell inequality violations). In [42, 32] this approach has been extended to the general eigenvalue optimization problem, of the form

inf ψ∗f(X1,... ,Xn)ψ : d ∈ N, ψ ∈ Cd unit vector, X1,... ,Xn ∈ Cd×d, g(X1,... ,Xn) 0 for g ∈ G .

Here, the matrix variables Xi have free dimension d ∈ N and {f} ∪ G ⊆ R x1,... ,xn is a set of symmetric polynomials in noncommutative variables. In tracial optimization, instead of minimizing the smallest eigenvalue of f(X1,... ,Xn), we minimize its normalized trace Tr(f(X1,... ,Xn))/d (so that the identity matrix has trace one) [7, 6, 8, 21]. The moment approach for these problems relies on minimizing L(f), where L is a linear functional on the space of noncommutative polynomials satisfying some necessary conditions, and L(f) models ψ∗f(X1,... ,Xn)ψ or Tr(f(X1,... ,Xn))/d. By truncating the degrees one gets hierarchies of lower bounds for the original problem. The asymptotic limit of these bounds involves operators Xi on a Hilbert space (possibly of inﬁnite dimension). In tracial optimization this leads to allowing solutions Xi in a C∗-algebra A equipped with a tracial state τ, where τ(f(X1,... ,Xn)) is minimized.

An important feature in noncommutative optimization is the dimension independence: the optimization is over all possible matrix sizes d ∈ N. In some applications one may want to restrict to optimizing over matrices with restricted size d. In [33, 30] techniques are developed that allow to incorporate this dimension restriction by suitably selecting the linear functionals L in a speciﬁed space; this is used to give bounds on the maximum violation of a Bell inequality in a ﬁxed dimension. A related natural problem is to decide what is the minimum dimension d needed to realize a given algebraically deﬁned object, such as a (commuting) quantum correlation P. We propose an approach based on tracial optimization: starting from the observation that the trace of the d × d identity matrix gives its size d, we consider the problem of minimizing L(1) where L is a linear functional modeling the non-normalized matrix trace. This approach has been used in several recent works [51, 34, 15] for lower bounding factorization ranks of matrices and tensors.

# 2 A hierarchy for the minimal entanglement dimension

## 2.1 The minimal average entanglement dimension

We start by showing that it does not matter whether we use the tensor or the commuting model when deﬁning the average entanglement dimension.

- Proposition 2.1. For any P ∈ Cq(Γ) we have Aq(P) = Aqc(P).


Proof. The easy inequality Aqc(P) ≤ Aq(P) follows from Esa ⊗ Ftb = (Esa ⊗ I)(I ⊗ Ftb).

For the other inequality we suppose P = Ii=1λiPi is feasible for Aqc(P). This means we have POVMs {Xsa(i)}a and {Ytb(i)}b in Cdi×di with [Xsa(i),Ytb(i)] = 0 and unit vectors ψi ∈ Cdi such that Pi(a,b|s,t) = ψi∗Xsa(i)Ytb(i)ψi for all (a,b,s,t) ∈ Γ and i ∈ [I]. We will construct a feasible solution to Aq(P) with value at most i λidi.

Fix some index i ∈ [I]. By Artin-Wedderburn theory applied to C {Xsa(i)}a,s , the ∗-algebra generated by the matrices Xsa(i) for (a,s) ∈ A×S, there exists a unitary matrix Ui and integers Ki,mk,nk such that

UiC {Xsa(i)}a,s Ui∗ =

Ki

(Cnk×nk ⊗ Imk) and di =

k=1

Ki

mknk.

k=1

By the commutation relations each matrix Ytb(i) commutes with all the matrices in C {Xsa(i)}a,s , and thus UiYtb(i)Ui∗ lies in the algebra k(Ink ⊗ Cmk×mk). Hence, we may assume

Ki

Ki

Ki

Xsa(i) =

Esa(i,k) ⊗ Imk, Ytb(i) =

Ink ⊗ Ftb(i,k), ψi =

ψi,k,

k=1

k=1

k=1

with Esa(i,k) ∈ Cnk×nk, Ftb(i,k) ∈ Cmk×mk, and ψi,k ∈ Cmknk. Then we have

Ki

ψi,kψi,k∗

ψi,k 2 Tr Esa(i,k) ⊗ Ftb(i,k)

Pi(a,b|s,t) = Tr(Xsa(i)Ytb(i)ψiψi∗) =

,

![image 3](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile3.png>)

ψi,k 2 Qi,k(a,b|s,t)

k=1

![image 4](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile4.png>)

![image 5](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile5.png>)

where Qi,k ∈ Cq(Γ). As k ψi,k 2 = ψi 2 = 1, we have that Pi = k ψi,k 2Qi,k is a convex combination of the Qi,k’s.

We now show that Qi,k ∈ Cqmin{mk,nk}(Γ). Consider the Schmidt decomposition ψi,k/ ψi,k = min{mk,nk}

l=1 λi,k,l vi,k,l ⊗ wi,k,l, where λi,k,l ≥ 0 and {vi,k,l}nl=1k ⊆ Cnk and {wi,k,l}ml=1k ⊆ Cmk are orthonormal bases. Deﬁne unitary matrices Vk ∈ Cnk×nk and Wk ∈ Cmk×mk such that Vkvi,k,l is the lth unit vector in Rnk and Wkwi,k,l is the lth unit vector in Rmk for l ≤ min{mk,nk}. Let Esa(i,k)′ (resp., Ftb(i,k)′) be the leading principal submatrices of VkEsa(i,k)Vk∗ (resp., WkFtb(i,k)Wk∗) of size min{mk,nk}. Moreover, set φi,k = minl=1{mk,nk} λi,k,lel ⊗ el, where el is the lth unit vector in Rmin{mk,nk}. Then we have

ψi,kψi,k∗ ψi,k 2

Qi,k(a,b|s,t) = Tr Esa(i,k) ⊗ Ftb(i,k)

![image 6](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile6.png>)

min{mk,nk}

λi,k,lλi,k,l′vi,k,l∗ Esa(i,k)vi,k,l′wi,k,l∗ Ftb(i,k)wi,k,l′

=

l,l′=1

min{mk,nk}

λi,k,lλi,k,l′e∗l Esa(i,k)′el′e∗l Ftb(i,k)′el′

=

l,l′=1

= Tr((Esa(i,k)′ ⊗ Ftb(i,k)′)φi,kφ∗i,k),

thus showing Qi,k ∈ Cqmin{mk,nk}(Γ). Since P = i,k λi ψi,k 2Qi,k is a convex decomposition, we obtain

Aq(P) ≤

λi ψi,k 2min{mk,nk}2 ≤

i,k

λimin{mk,nk}2 ≤

i,k

λimknk =

i,k

i

λidi.

![image 7](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile7.png>)

![image 8](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile8.png>)

![image 9](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile9.png>)

![image 10](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile10.png>)

We now show the parameter Aq(·) permits to characterize classical correlations.

- Proposition 2.2. For a correlation P ∈ RΓ we have Aq(P) = 1 if and only if P ∈ Cloc(Γ).


Proof. If P ∈ Cloc(Γ), then P can be written as a convex combination of deterministic correlations (which are contained in Cq1(Γ)), hence Aq(P) = 1.

On the other hand, if Aq(P) = 1, then there exist convex decompositions indexed by l ∈ N: P = i∈Il λliPil with {Pil} ⊆ Cq(Γ) and liml→∞ i∈Il λlDq(Pil) = 1. Decompose Il as the disjoint union I−l ∪ I+l so that Dq(Pi) is equal to 1 for i ∈ I−l and strictly greater than 1 for i ∈ I+l . Let ε > 0. For all l suﬃciently large we have

λli ≤

λli +

λli + 2

λliDq(Pil) ≤ 1 + ε,

1 −

i∈I+l

i∈I−l

i∈I+l

i∈I+l

λli ≤ ε. This shows that P is the limit of convex combinations of deterministic correlations, which implies that P ∈ Cloc(Γ).

which shows that i∈Il

+

![image 11](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile11.png>)

![image 12](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile12.png>)

![image 13](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile13.png>)

![image 14](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile14.png>)

- Proposition 2.3. If Cq(Γ) is not closed, there exists {Pi} ⊆ Cq(Γ) with Aq(Pi) → ∞.


Proof. Assume for contradiction there exists an integer K such that Aq(P) ≤ K for all P ∈ Cq(Γ); we show this results in a uniform upper bound K′ on Dqc(P), which implies Cq(Γ) = CqcK′(Γ) is closed. For this, we will ﬁrst show that P ∈ conv(CqcK(Γ)).

In a ﬁrst step observe that any P ∈ Cq(Γ) \ conv(CqcK(Γ)) can be decomposed as P = µ1R1 + (1 − µ1)Q1, (8)

- where R1 ∈ Cq(Γ), Q1 ∈ conv(CqcK(Γ)), and 0 < µ1 ≤ K/(K + 1). Indeed, by assumption and using Proposition 2.1, Aqc(P) = Aq(P) ≤ K, so P can be written as a convex combination P = i∈I λiPi with {Pi} ⊆ Cq(Γ) and i∈I λiDqc(Pi) ≤ K. As P  ∈ conv(CqcK(Γ)), the set J of indices i ∈ I with Dqc(Pi) ≥ K +1 is non empty. Then (K +1) i∈J λi ≤ i∈J λiDqc(Pi) ≤ K,


λi ≤ K/(K + 1). Hence (8) holds after setting R1 = ( i∈J λiPi)/µ1 and Q1 = ( i∈I\J λiPi)/(1 − µ1).

and thus 0 < µ1 := i∈I

+

As R1 ∈ Cq(Γ) \ CqcK(Γ), we may repeat the same argument for R1. By iterating we obtain for each integer k ∈ N a decomposition

P = µ1µ2 ··· µkRk + (1 − µ1)Q1 + µ1(1 − µ2)Q2 + ... + µ1µ2 ··· µk−1(1 − µk)Qk

,

![image 15](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile15.png>)

![image 16](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile16.png>)

=(1−µ1µ2···µk)Qˆk

where Rk ∈ Cq(Γ), Qˆk ∈ conv(CqcK(Γ)) and µ1µ2 ··· µk ≤ (K/(K + 1))k. As the entries of Rk lie in [0,1] we can conclude that µ1µ2 ··· µkRk tends to 0 as k → ∞. Hence the sequence (Qˆk)k has a limit Qˆ and P = Qˆ holds. As all Qˆk lie in the compact set conv(CqcK(Γ)), we also have P ∈ conv(CqcK(Γ)).

The extreme points of the compact convex set conv(CqcK(Γ)) lie in CqcK(Γ), so, by the Carathe´odory theorem, any P ∈ conv(CqcK(Γ)) is a convex combination of c elements from CqcK(Γ), where c = |Γ| + 1 − |S||T|. By using a direct sum construction one can obtain Dqc(P) ≤ cK, which shows K′ := cK is a uniform upper bound on Dqc(P) for all P ∈ Cq(Γ).

![image 17](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile17.png>)

![image 18](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile18.png>)

![image 19](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile19.png>)

![image 20](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile20.png>)

## 2.2 Setup of the hierarchy

We will now construct a hierarchy of lower bounds on the minimal entanglement dimension, using its formulation via Aqc(P). Our approach is based on noncommutative polynomial optimization, thus similar to the approach in [15] for bounding matrix factorization ranks.

We ﬁrst need some notation. Set x = xas : (a,s) ∈ A×S and y = ytb : (b,t) ∈ B×T , and let x,y,z r be the set of all words of length at most r in the n = |S||A| + |T||B| + 1 symbols xas, ytb, and z. Moreover, set x,y,z = x,y,z ∞. We equip x,y,z r with an involution w  → w∗ that reverses the order of the symbols in the words and leaves the symbols xas,ytb,z invariant; e.g., (xasz)∗ = zxas. Let R x,y,z r be the vector space of all real linear combinations of the words of length (aka degree) at most r. The space R x,y,z = R x,y,z ∞ is the ∗algebra with Hermitian generators {xas}, {ytb}, and z, and the elements in this algebra are called noncommutative polynomials in the variables {xas},{ytb},z.

The hierarchy is based on the following idea: For any feasible solution to Aqc(P), its objective value can be modeled as L(1) for a certain tracial linear form L on the space of noncommutative polynomials (truncated to degree 2r).

Indeed, assume {(Pi,λi)i} is a feasible solution to the program Aqc(P) deﬁned in Section 1.2, where Pi(a,b|s,t) = Tr Xsa(i)Ytb(i)ψiψi∗ with Xsa(i),Ytb(i) ∈ Cdi×di, ψi ∈ Cdi, and di = Dqc(Pi). For r ∈ N ∪ {∞}, consider the linear functional L ∈ R x,y,z ∗2r deﬁned by

λi Re(Tr(p(X(i),Y(i),ψiψi∗))) for p ∈ R x,y,z 2r.

L(p) =

i

Here, for each index i, we set X(i) = (Xsa(i) : (a,s) ∈ A × S), Y(i) = (Ytb(i) : (b,t) ∈ B × T), and replace the variables xas, ytb, z by Xsa(i), Ytb(i), and ψiψi∗. Then L(1) = i λidi. That

is, L(1) is the objective value of the feasible solution {(Pi,λi)i} to Aqc(P). We will identify several computationally tractable properties that this L satisﬁes. Then the hierarchy of lower bounds on Aqc(P) consists of optimization problems where we minimize L(1) over the set of linear functionals that satisfy these properties.

First note that L is symmetric, that is, L(w) = L(w∗) for all w ∈ x,y,z 2r, and tracial, that is, L(ww′) = L(w′w) for all w,w′ ∈ x,y,z with deg(ww′) ≤ 2r.

For all p ∈ R x,y,z r−1 we have L(p∗xasp) =

λi Re(Tr(M(i)∗Xsa(i)M(i)) ≥ 0, where M(i) = p(X(i),Y(i),ψiψi∗),

i

as M(i)∗Xsa(i)M(i) is positive semideﬁnite since Xsa(i) is positive semideﬁnite. In the same way we have L(p∗ytbp) ≥ 0 and L(p∗zp) ≥ 0. That is, if we set

G = xas : s ∈ S, a ∈ A ∪ ytb : t ∈ T, b ∈ B ∪ {z}, then L is nonnegative (denoted as L ≥ 0) on the truncated quadratic module

M2r(G) = cone p∗gp : p ∈ R x,y,z , g ∈ G ∪ {1}, deg(p∗gp) ≤ 2r . (9) Similarly, setting

H = z − z2 ∪ 1 −

xas : s ∈ S ∪ 1 −

a∈A

ytb : t ∈ T ∪ [xas,ytb] : (s,t,a,b) ∈ Γ ,

b∈B

we have L = 0 on the truncated ideal I2r(H) = ph : p ∈ R x,y,z , h ∈ H, deg(ph) ≤ 2r . (10)

Moreover, we have L(z) = i λiRe(Tr(ψiψi∗)) = 1. In addition, for any matrices U,V ∈ Cdi×di we have

ψiψi∗Uψiψi∗V ψiψi∗ = ψiψi∗V ψiψi∗Uψiψi∗, and therefore, in particular,

L(wzuzvz) = L(wzvzuz) for all u,v,w ∈ x,y,z with deg(wzuzvz) ≤ 2r. That is, we have L = 0 on I2r(Rr), where

Rr = zuzvz − zvzuz : u,v ∈ u,v ∈ x,y,z with deg(zuzvz) ≤ 2r .

We get the idea of adding these last constraints from [32], where this is used to study the mutually unbiased bases problem.

We call M(G) = M∞(G) the quadratic module generated by G, and we call I(H ∪ R∞) = I∞(H ∪ R∞) the ideal generated by H ∪ R∞.

For r ∈ N ∪ {∞} we can now deﬁne the parameter:

ξrq(P) = min L(1) : L ∈ R x,y,z ∗2r tracial and symmetric, L(z) = 1, L(xasytbz) = P(a,b|s,t) for all (a,b,s,t) ∈ Γ, L ≥ 0 on M2r(G), L = 0 on I2r(H ∪ Rr) .

Additionally, we deﬁne ξ∗q(P) by adding the constraint rank(M(L)) < ∞ to ξ∞q (P). By construction this gives a hierarchy of lower bounds for Aqc(P):

ξ1q(P) ≤ ... ≤ ξrq(P) ≤ ξ∞q (P) ≤ ξ∗q(P) ≤ Aqc(P).

Note that for order r = 1 we get the trivial lower bound ξ1q(P) = 1.

For each ﬁnite r ∈ N the parameter ξrq(P) can be computed by semideﬁnite programming. Indeed, the condition L ≥ 0 on M2r(G) means that L(p∗gp) ≥ 0 for all g ∈ G ∪ {1} and all polynomials p ∈ R x,y,z with degree at most r − ⌈deg(g)/2⌉. This is equivalent to requiring that the matrices (L(w∗gw′)), indexed by all words w,w′ with degree at most r − ⌈deg(g)/2⌉, are positive semideﬁnite. To see this, write p = w pww and let pˆ = (pw) denote the vector of coeﬃcients, then L(p∗gp) ≥ 0 is equivalent to pˆT(L(w∗gw′))ˆp ≥ 0. When g = 1, the matrix (L(w∗w′)) is indexed by the words of degree at most r, it is called the moment matrix of L and denoted by Mr(L) (or M(L) when r = ∞). The entries of the matrices (L(w∗gw′)) are linear combinations of the entries of Mr(L), and the constraint L = 0 on I2r(H ∪ Rr) can be written as a set of linear constraints on the entries of Mr(L). It follows that for ﬁnite r ∈ N, the parameter ξrq(P) is indeed computable by a semideﬁnite program.

## 2.3 Background on positive tracial linear forms

Before we show the convergence results we give some background on positive tracial linear forms, which we use again in Section 3. We state these results using the variables x1,... ,xn, where we use the notation x = x1,... ,xn . The results stated below do not always appear in this way in the sources cited; we follow the presentation of [15], where full proofs for these results are also provided.

First we need a few more deﬁnitions. A polynomial p ∈ R x is called symmetric if p∗ = p, and we denote the set of symmetric polynomials by SymR x . Given G ⊆ SymR x and H ⊆ R x , the set M(G)+I(H) is called Archimedean if it contains the polynomial R− ni=1 x2i for some R > 0. We will use the concept of a C∗-algebra, which for our purposes can be deﬁned as a norm closed ∗-subalgebra of the space B(H) of bounded operators on a complex Hilbert space H. We say that A is unital if it contains the identity operator (denoted 1). An element a ∈ A is called positive if a = b∗b for some b ∈ A. A linear form τ on a unital C∗-algebra A is said to be a state if τ(1) = 1 and τ is positive; that is, τ(a) ≥ 0 for all positive elements a ∈ A. We say that a state τ is tracial if τ(ab) = τ(ba) for all a,b ∈ A. See, for example, [4] for more information on C∗-algebras.

The ﬁrst result relates positive tracial linear forms to C∗-algebras; see [32] for the noncommutative (eigenvalue) setting and [8] for the tracial setting.

- Theorem 2.4. Let G ⊆ SymR x and H ⊆ R x and assume that M(G)+I(H) is Archimedean. For a linear form L ∈ R x ∗, the following are equivalent:

- (1) L is symmetric, tracial, nonnegative on M(G), zero on I(H), and L(1) = 1;
- (2) there is a unital C∗-algebra A with tracial state τ and X ∈ An such that g(X) is positive in A for all g ∈ G, and h(X) = 0 for all h ∈ H, with


L(p) = τ(p(X)) for all p ∈ R x . (11)

The following can be seen as the ﬁnite dimensional analogue of the above result. The proof of the unconstrained case (G = H = ∅) can be found in [7], and for the constrained case in [8]. Given a linear form L ∈ R x ∗, recall that the moment matrix M(L) is given by M(L)u,v = L(u∗v) for u,v ∈ x .

- Theorem 2.5. Let G ⊆ SymR x and H ⊆ R x . For L ∈ R x ∗, the following are equivalent:


- (1) L is a symmetric, tracial, linear form with L(1) = 1 that is nonnegative on M(G), zero on I(H), and has rank(M(L)) < ∞;
- (2) there is a ﬁnite dimensional C∗-algebra A with a tracial state τ and X ∈ An satisfying (11), with g(X) positive in A for all g ∈ G and h(X) = 0 for all h ∈ H;


- (3) L is a convex combination of normalized trace evaluations at tuples X of Hermitian matrices that satisfy g(X) 0 for all g ∈ G and h(X) = 0 for all h ∈ H.


A truncated linear functional L ∈ R x 2r is called δ-ﬂat if the principal submatrix Mr−δ(L) of Mr(L) indexed by monomials up to degree r −δ has the same rank as Mr(L); L is ﬂat if it is δ-ﬂat for some δ ≥ 1. The following result claims that any ﬂat linear functional on a truncated polynomial space can be extended to a linear functional L on the full algebra of polynomials. It is due to Curto and Fialkow [10] in the commutative case and extensions to the noncommutative case can be found in [42] (for eigenvalue optimization) and [7, 21] (for trace optimization).

- Theorem 2.6. Let 1 ≤ δ ≤ t < ∞, G ⊆ SymR x 2r, and H ⊆ R x 2r. If L ∈ R x ∗2r is symmetric, tracial, δ-ﬂat, nonnegative on M2r(G), and zero on I2r(H), then L extends to a symmetric, tracial, linear form on R x that is nonnegative on M(G), zero on I(H), and whose moment matrix has ﬁnite rank.


The following technical lemma, based on the Banach-Alaoglu theorem, is a well-known tool to show asymptotic convergence results in polynomial optimization.

- Lemma 2.7. Let G ⊆ SymR x , H ⊆ R x , and assume that for some d ∈ N and R > 0


we have R − (x21 + ··· + x2n) ∈ M2d(G) + I2d(H). For r ∈ N assume Lr ∈ R x ∗2r is tracial, nonnegative on M2r(G) and zero on I2r(H). Then |Lr(w)| ≤ R|w|/2Lr(1) for all w ∈ x 2r−2d+2. In addition, if supr Lr(1) < ∞, then {Lr}r has a pointwise converging subsequence in R x ∗.

## 2.4 Convergence results

We ﬁrst show equality ξ∗q(P) = Aqc(P), and then we consider convergence properties of the bounds ξrq(P) to the parameters ξ∞q (P) and ξ∗q(P).

- Proposition 2.8. For any P ∈ Cq(Γ) we have ξ∗q(P) = Aqc(P).


Proof. We already know that ξ∗q(P) ≤ Aqc(P). To show ξ∗q(P) ≥ Aqc(P) we let L be feasible for ξ∗q(P), so that L ≥ 0 on M(G) and L = 0 on I(H ∪ R∞). By Theorem 2.5, there exist ﬁnitely many scalars λi ≥ 0, Hermitian matrix tuples X(i) = (Xsa(i))a,s and Y(i) = (Ytb(i))b,t, and Hermitian matrices Zi, so that g(X(i),Y(i),Zi) 0 for all g ∈ G, h(X(i),Y(i),Zi) = 0 for all h ∈ H ∪ R∞, and

λi Tr(p(X(i),Y(i),Zi)) for all p ∈ R x,y,z . (12)

L(p) =

i

By Artin–Wedderburn theory we know that for each i there is a unitary matrix Ui such that UiC X(i),Y(i),Zi Ui∗ = k Cdk×dk ⊗ Imk. Hence, after applying this further block diagonalization we may assume that in the decomposition (12), for each i, C X(i),Y(i),Zi is a full matrix algebra Cdi×di.

Since h(E(i),F(i),Zi) = 0 for all h ∈ R∞ ∪ {z − z2}, the commutator ZiuZi,ZivZi

vanishes for all u,v ∈ E(i),F(i),Zi and hence for all u,v ∈ C E(i),F(i),Zi . This means that [ZiT1Zi,ZiT2Zi] = 0 for all T1,T2 ∈ Cdi×di. Since Zi is a projector, there exists a unitary matrix Ui such that UiZiUi∗ = Diag(1,... ,1,0,... ,0). The above then implies that for all T1 and T2, the leading principal submatrices of size rank(Zi) of UiT1Ui∗ and UiT2Ui∗ commute. This implies rank(Zi) ≤ 1 and thus Tr(Zi) ∈ {0,1}. Let I be the set of indices with Tr(Zi) = 1. Then i∈I λi = i λi Tr(Zi) = L(z) = 1.

For each i ∈ I deﬁne Pi = (Tr(Esa(i)Ftb(i)Zi)), which is a quantum correlation in Cqcdi(Γ) because Tr(Zi) = 1, a Xsa(i) = b Ytb(i) = I, and [Xsa(i),Ytb(i)] = 0 by the ideal conditions. We have P = i∈I λiPi, so that (Pi,λi)i∈I forms a feasible solution to Aqc(P) with objective value i∈I λiDqc(Pi) ≤ i∈I λidi ≤ i λidi = L(1).

![image 21](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile21.png>)

![image 22](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile22.png>)

![image 23](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile23.png>)

![image 24](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile24.png>)

The problem ξrq(P) diﬀers in two ways from a standard tracial optimization problem. It does not have the normalization L(1) = 1 (and instead minimizes L(1)), and it has ideal constraints L = 0 on I2r(Rr) where Rr depends on r. We show asymptotic convergence still holds.

- Proposition 2.9. For any P ∈ Cq(Γ) we have ξrq(P) → ξ∞q (P) as r → ∞.

Proof. First observe that 1 − z2, 1 − (xas)2, 1 − (ytb)2 ∈ M4(G ∪ H0), where H0 contains the symmetric polynomials in H; i.e., omitting the commutators [xas,ytb]. Indeed, we have 1 − z2 = (1−z)2+2(z−z2) and 1−(xas)2 = (1−xas)2+2(1−xas)xas(1−xas)+2xas 1− a′ xas′ + a′ =a xas′ xas, and the same for ytb. Hence R − z2 − a,s(xas)2 − b,t(ytb)2 ∈ M4(G ∪ H0) for some R > 0. Fix ε > 0 and for each r ∈ N let Lr be feasible for ξrq(P) with value Lr(1) ≤ ξrq(P)+ε. As Lr is tracial and zero on I2r(H0), it follows (using the identity p∗gp = pp∗g+[p∗g,p]) that L = 0 on M2r(H0). Hence, Lr ≥ 0 on M2r(G ∪ H0). Since suprLr(1) ≤ Aq(P) + ε, we can apply Lemma 2.7 and conclude that {Lr}r has a converging subsequence; denote its limit by Lε ∈ R x ∗. One can verify that Lε is feasible for ξ∞q (P), and ξ∞q (P) ≤ Lε(1) ≤ limr→∞ ξrq(P) + ε ≤ ξ∞q (P) + ε. Letting ε → 0 we obtain that ξ∞q (P) = limr→∞ ξrq(P).

![image 25](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile25.png>)

![image 26](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile26.png>)

![image 27](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile27.png>)

![image 28](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile28.png>)

Next we show that if ξrq(P) admits a δ-ﬂat optimal solution with δ = ⌈r/3⌉ + 1, then we have ξrq(P) = ξ∗q(P). This result is a variation of the ﬂat extension result from Theorem 2.6, where δ now depends on the order r because the ideal constraints in ξrq(P) depend on r.

- Proposition 2.10. If ξrq(P) admits a (⌈r/3⌉ + 1)-ﬂat optimal solution, ξrq(P) = ξ∗q(P).


Proof. Let δ = ⌈r/3⌉ + 1 and let L be a δ-ﬂat optimal solution to ξrq(P). We have to show ξrq(P) ≥ ξ∗q(P), which we do by constructing a feasible solution to ξ∗q(P) with the same objective value. The main step in the proof of Theorem 2.6 consists of extending the linear form L to a tracial symmetric linear form Lˆ on R x,y,z that is nonnegative on M(G), zero on I(H), and satisﬁes rank(M(Lˆ)) < ∞ (see the proof of [15, Thm. 2.3] for a detailed exposition). To do this a subset W of x,y,z r−δ is found such that we have the vector space direct sum R x,y,z = span(W) ⊕ I(Nr(L)), where Nr(L) is the vector space

Nr(L) = p ∈ R x,y,z r : L(qp) = 0 for all q ∈ R x,y,z r .

It is moreover shown that I(Nr(L)) ⊆ N(Lˆ). For p ∈ R x,y,z we denote by rp the unique element in span(W) such that p − rp ∈ I(Nr(L)). We now show that Lˆ is zero on I(R∞). For this ﬁx u,v,w ∈ R x,y,z . Then we have

Lˆ(w(zuzvz − zvzuz)) = Lˆ(wzuzvz) − Lˆ(wzvzuz). Since Lˆ is tracial and u − ru,v − rv,w − rw ∈ I(Nr(L)) ⊆ N(Lˆ), we have

Lˆ(wzuzvz) = Lˆ(rwzruzrvz) and Lˆ(wzvzuz) = Lˆ(rwzrvzruz). Since deg(ruzrvzrwz) = deg(rvzruzrwz) ≤ 2r we have

Lˆ(rwzruzrvz) = L(rwzruzrvz) and Lˆ(rwzrvzruz) = L(rwzrvzruz). So L = 0 on I2r(Rr) implies Lˆ = 0 on I(R∞).

Since Lˆ extends L we have Lˆ(z) = L(z) = 1 and Lˆ(xasytbz) = L(xasytbz) = P(a,b|s,t) for all a,b,s,t. So, Lˆ is feasible for ξ∗q(P) and has the same objective value Lˆ(1) = L(1).

![image 29](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile29.png>)

![image 30](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile30.png>)

![image 31](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile31.png>)

![image 32](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile32.png>)

# 3 Bounding quantum graph parameters

- 3.1 Hierarchies γrcol(G) and γrstab(G) based on synchronous correlations


In Section 1.3 we introduced quantum chromatic numbers (Deﬁnition 1.1) and quantum stability numbers (Deﬁnition 1.2) in terms of synchronous quantum correlations satisfying certain linear constraints. We ﬁrst give (known) reformulations in terms of C∗-algebras, and then we reformulate those in terms of tracial optimization, which leads to the hierarchies γrcol(G) and γrstab(G).

The following result from [41] allows us to write a synchronous quantum correlation in terms of C∗-algebras admitting a tracial state.

Theorem 3.1 ([41]). Let Γ = A2 ×S2 and P ∈ RΓ. We have P ∈ Cqc,s(Γ) (resp., P ∈ Cq,s(Γ)) if and only if there exists a unital (resp., ﬁnite dimensional) C∗-algebra A with a faithful tracial

state τ and a set of projectors {Xsa : s ∈ S,a ∈ A} ⊆ A satisfying a∈A Xsa = 1 for all s ∈ S and P(a,b|s,t) = τ(XsaXtb) for all s,t ∈ S,a,b ∈ A.

Here we add the condition that τ is faithful, that is, τ(X∗X) = 0 implies X = 0, since it follows from the GNS construction in the proof of [41]. This means that

0 = P(a,b|s,t) = τ(XsaXtb) = τ((Xsa)2(Xtb)2) = τ((XsaXtb)∗XsaXtb)

implies XsaXtb = 0. It follows that χqc(G) is equal to the smallest k ∈ N for which there exists a C∗-algebra A, a tracial state τ on A, and a family of projectors {Xic : i ∈ V,c ∈ [k]} ⊆ A satisfying

Xic − 1 = 0 for all i ∈ V, (13)

c∈[k]

XicXjc′ = 0 if (c = c′ and i = j) or (c = c′ and {i,j} ∈ E). (14)

The quantum chromatic number χq(G) is equal to the smallest k ∈ N for which there exists a ﬁnite dimensional C∗-algebra A with the above properties.

Analogously, αqc(G) is equal to the largest k ∈ N for which there is a C∗-algebra A, a tracial state τ on A, and a set of projectors {Xci : c ∈ [k],i ∈ V } ⊆ A satisfying

Xci − 1 = 0 for all c ∈ [k], (15)

i∈V

XciXcj′ = 0 if (i = j and c = c′) or ((i = j or {i,j} ∈ E) and c = c′), (16) and αq(G) is equal to the largest k ∈ N for which A can be taken ﬁnite dimensional.

These reformulations of χq(G),χqc(G),αq(G) and αqc(G) also follow from [36, Thm. 4.7], where general quantum graph homomorphisms are considered; the formulations of χq(G) and χqc(G) are also made explicit in [36, Thm. 4.12].

By Artin-Wedderburn theory [53, 2], a ﬁnite dimensional C∗-algebra is isomorphic to a matrix algebra. So the above reformulations of χq(G) and αq(G) can be seen as feasibility problems of systems of equations in matrix variables of unspeciﬁed (but ﬁnite) dimension; such formulations are given in [9, 28, 46]. Restricting to scalar solutions (1 × 1 matrices) in these feasibility problems recovers the classical graph parameters χ(G) and α(G).

We now reinterpret the above formulations in terms of tracial optimization. Given a graph

G = (V,E), let i ≃ j denote {i,j} ∈ E or i = j. For k ∈ N, let HG,kcol and HG,kstab denote the sets of polynomials corresponding to equations (13)–(14) and (15)–(16):

HG,kcol = 1 −

xci : i ∈ V ∪ xcixcj′ : (c = c′ and i = j) or (c = c′ and {i,j} ∈ E) ,

c∈[k]

HG,kstab = 1 −

i∈V

xic : c ∈ [k] ∪ xicxjc′ : (i = j and c = c′) or (i ≃ j and c = c′) .

We have 1 − (xci)2 ∈ M2(∅) + I2(HG,kcol ), since 1 − (xci)2 = (1 − xci)2 + 2(xci − (xci)2) and xci − (xci)2 = xci 1 − c′ xci′ + c′:c′ =c xcixci′ ∈ I2(HG,kcol ), and the analogous statements hold for HG,kstab. Hence, both M(∅) + I(Hkcol) and M(∅) + I(Hkstab) are Archimedean and we can apply Theorems 2.4 and 2.5 to express the quantum graph parameters in terms of positive tracial linear functionals. Namely,

χqc(G) = min k ∈ N : L ∈ R {xci : i ∈ V,c ∈ [k]} ∗ symmetric, tracial, positive, L(1) = 1, L = 0 on I(HG,kcol ) , and χq(G) is obtained by adding the constraint rank(M(L)) < ∞. Likewise, αqc(G) = min k ∈ N : L ∈ R {xic : c ∈ [k],i ∈ V } ∗ symmetric, tracial, positive, L(1) = 1, L = 0 on I(HG,kstab) , and αq(G) is given by this program with the additional constraint rank(M(L)) < ∞.

Starting from these formulations it is natural to deﬁne a hierarchy {γrcol(G)} of lower bounds on χqc(G) and a hierarchy {γrstab(G)} of upper bounds on αqc(G), where the bounds of order r ∈ N are obtained by truncating L to polynomials of degree at most 2r and truncating the ideal

to degree 2r. Then, by deﬁning γ∗col(G) and γ∗stab(G) by adding the constraint rank(M(L)) < ∞ to γ∞col(G) and γ∞stab(G), we have

γ∞col(G) = χqc(G), γ∞stab(G) = αqc(G), γ∗col(G) = χq(G), and γ∗stab(G) = αq(G).

The optimization problems γrcol(G), for r ∈ N, can be computed by semideﬁnite programming and binary search on k, since the positivity condition on L can be expressed by requiring that its truncated moment matrix Mr(L) = (L(w∗w′)) (indexed by words with degree at most r) is positive semideﬁnite. If there is an optimal solution (k,L) to γrcol(G) with L ﬂat, then, by Theorem 2.6, we have equality γrcol(G) = χq(G). Since {γrcol(G)}r∈N is a monotone nondecreasing sequence of lower bounds on χq(G), there exists an r0 such that for all r ≥ r0 we have γrcol(G) = γrcol0 (G), which is equal to γ∞col(G) = χqc(G) by Lemma 2.7. The analogous statements hold for the parameters γrstab(G). Hence, we have shown the following result.

Proposition 3.2. There is an r0 ∈ N such that γrcol(G) = χqc(G) and γrstab(G) = αqc(G) for all r ≥ r0. Moreover, if γrcol(G) admits a ﬂat optimal solution, then γrcol(G) = χq(G), and if γrstab(G) admits a ﬂat optimal solution, then γrstab(G) = αq(G).

Remark 3.3. A hierarchy {Qr(Γ)} of outer semideﬁnite approximations for the set Cqc(Γ) of commuting quantum correlations was constructed in [41], revisiting the approach in [31, 42]. This hierarchy is converging, that is,

Cqc(Γ) = Q∞(Γ) =

Qr(Γ).

r∈N

The approximations Qr(Γ) are based on the eigenvalue optimization approach, applied to the formulation (3) of commuting quantum correlations, and thus they use linear functionals on

polynomials involving two sets of variables xas,ytb for (a,b,s,t) ∈ Γ. The authors of [41] use these outer approximations of Cqc(Γ) to deﬁne a converging hierarchy of lower bounds on χqc(G) in terms of feasibility problems over the sets Qr(Γ).

For synchronous correlations we can use the result of Theorem 3.1 and the tracial optimization approach used here to deﬁne directly a converging hierarchy {Qr,s(Γ)} of outer semideﬁnite

approximations for the set Cqc,s(Γ) of synchronous commuting quantum correlations. These approximations now use linear functionals on polynomials involving only one set of variables xas. Namely, deﬁne Qr,s(Γ) as the set of P ∈ RΓ for which there exists a symmetric, tracial, positive linear functional L ∈ R {xas : (a,s) ∈ A × S} ∗2r such that L(1) = 1 and L = 0 on the ideal generated by the polynomials xas − (xas)2 ((a,s) ∈ A × S) and 1 − a∈A xas (s ∈ S), truncated at degree 2r. Then we have

Cqc,s(Γ) = Q∞,s(Γ) =

Qr,s(Γ).

r∈N

The synchronous value of a nonlocal game is deﬁned in [12] as the maximum value of the objective function (6) over the set Cqc,s(Γ). By maximizing the objective (6) over the relaxations Qr,s(Γ) we get a hierarchy of semideﬁnite programming upper bounds that converges to the synchronous value of the game. Finally note that one can also view the parameters γrcol(G) as solving feasibility problems over the sets Qr,s(Γ).

## 3.2 Hierarchies ξrcol(G) and ξrstab(G) based on Lasserre type bounds

Here we revisit some known Lasserre type hierarchies for the classical stability number α(G) and chromatic number χ(G) and we show that their tracial noncommutative analogues can be used to recover known parameters such as the projective packing number αp(G), the projective rank ξf(G), and the tracial rank ξtr(G). Compared to the hierarchies deﬁned in the previous section, these Lasserre type hierarchies use less variables (they only use variables indexed by the vertices of the graph G), but they also do not converge to the (commuting) quantum chromatic or stability number.

Given a graph G = (V,E), deﬁne the set of polynomials

HG = xi − x2i : i ∈ V ∪ xixj : {i,j} ∈ E

in the variables x = (xi : i ∈ V ) (which are commutative or noncommutative depending on the context). Note that 1 − x2i ∈ M2(∅) + I2(HG) for all i ∈ V , so M(∅) + I(HG) is Archimedean.

- 3.2.1 Semideﬁnite programming bounds on the projective packing number


We ﬁrst recall the Lasserre hierarchy of bounds for the classical stability number α(G). Starting from the formulation of α(G) via the optimization problem

α(G) = sup

xi : x ∈ Rn, h(x) = 0 for h ∈ HG ,

i∈V

the r-th level of the Lasserre hierarchy for α(G) (introduced in [23, 24]) is deﬁned by

lasstabr (G) = sup L

xi : L ∈ R[x]∗2r positive, L(1) = 1, L = 0 on I2r(HG) .

i∈V

Then lasstabr+1(G) ≤ lasstabr (G), the ﬁrst bound is Lov´asz’ theta number: lasstab1 (G) = ϑ(G), and ﬁnite convergence to α(G) is shown in [24]: lasstabα(G)(G) = α(G). Roberson [45] introduces the projective packing number

αp(G) = sup

= sup

1 d i∈V

rankXi : d ∈ N, X ∈ (Sd)n projectors, XiXj = 0 for {i,j} ∈ E

![image 33](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile33.png>)

1 d

Xi : d ∈ N, X ∈ (Sd)n, h(X) = 0 for h ∈ HG (17)

Tr

![image 34](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile34.png>)

i∈V

as an upper bound for the quantum stability number αq(G); the inequality αq(G) ≤ αp(G) also follows from Proposition 3.4 below. In view of (17), the parameter αp(G) can be seen as a noncommutative analogue of α(G).

For r ∈ N ∪ {∞} we deﬁne the noncommutative analogue of lasstabr (G) by

ξrstab(G) = sup L

xi : L ∈ R x ∗2r tracial, symmetric, and positive, L(1) = 1, L = 0 on I2r(HG) ,

i∈V

and ξ∗stab(G) by adding the constraint rank(M(L)) < ∞ to the deﬁnition of ξ∞stab(G).

In view of Theorems 2.4 and 2.5, both ξ∞stab(G) and ξ∗stab(G) can be reformulated in terms of C∗-algebras: ξ∞stab(G) (resp., ξ∗stab(G)) is the largest value of τ( i∈V Xi), where A is a (resp., ﬁnite-dimensional) C∗-algebra with tracial state τ and Xi ∈ A (i ∈ [n]) are projectors satisfying XiXj = 0 for all {i,j} ∈ E. Moreover, as we now see, the parameter ξ∗stab(G) coincides with the projective packing number and the parameters ξ∗stab(G) and ξ∞stab(G) upper bound the quantum stability numbers.

- Proposition 3.4. We have ξ∗stab(G) = αp(G) ≥ αq(G) and ξ∞stab(G) ≥ αqc(G).


Proof. By (17), αp(G) is the largest value of L( i∈V xi) over linear functionals L that are normalized trace evaluations at projectors X ∈ (Sd)n (for some d ∈ N) with XiXj = 0 for {i,j} ∈ E. By convexity the optimum remains unchanged when considering a convex combination of such trace evaluations. In view of Theorem 2.5(3), this optimum is precisely the parameter ξ∗stab(G). This shows equality αp(G) = ξ∗stab(G).

Consider a C∗-algebra A with tracial state τ and projectors Xci ∈ A (i ∈ V, c ∈ [k]) satisfying (15)-(16). Then, setting Xi = c∈[k] Xci for i ∈ V , we obtain projectors Xi ∈ A that satisfy XiXj = 0 if {i,j} ∈ E. Moreover, τ( i∈V Xi) = c∈[k] τ( i∈V Xci) = k. This shows ξ∞stab(G) ≥ αqc(G) and, when restricting A to be ﬁnite dimensional, ξ∗stab(G) ≥ αq(G).

![image 35](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile35.png>)

![image 36](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile36.png>)

![image 37](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile37.png>)

![image 38](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile38.png>)

Using Lemma 2.7 one can verify that ξrstab(G) converges to ξ∞stab(G) as r → ∞, and for r ∈ N∪{∞} the inﬁmum in ξrstab(G) is attained. Moreover, by Theorem 2.6, if ξrstab(G) admits a ﬂat optimal solution, then ξrstab = ξ∗stab(G). Also, the ﬁrst bound ξ1stab(G) coincides with the theta number, since ξ1stab(G) = lasstab1 (G) = ϑ(G). Summarizing we have αqc(G) ≤ ξ∞stab(G) and the following chain of inequalities

αq(G) ≤ αp(G) = ξ∗stab(G) ≤ ξ∞stab(G) ≤ ξrstab(G) ≤ ξ1stab(G) = ϑ(G).

- 3.2.2 Semideﬁnite programming bounds on the projective rank and tracial rank


We now turn to the (quantum) chromatic numbers. First recall the deﬁnition of the fractional chromatic number:

χf(G) := min

λS : λ ∈ RS+,

λS = 1 for all i ∈ V ,

S∈S

S∈S:i∈S

- where S is the set of stable sets of G. Clearly, χf(G) ≤ χ(G). The following Lasserre type lower bounds for the classical chromatic number χ(G) are deﬁned in [18]:


lascolr (G) = inf L(1) : L ∈ R[x]∗2r positive, L(xi) = 1 (i ∈ V ), L = 0 on I2r(HG) .

By viewing χf(G) as minimizing L(1) over linear functionals L ∈ R[x]∗ that are conic combinations of evaluations at characteristic vectors of stable sets, we see that lascolr (G) ≤ χf(G) for all r ≥ 1. In [18] it is shown that lascolα(G)(G) = χf(G). Moreover, the order 1 bound coincides with the theta number: lascol1 (G) = ϑ(G).

![image 39](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile39.png>)

The following parameter ξf(G), called the projective rank of G, was introduced in [28] as a lower bound on the quantum chromatic number χq(G):

ξf(G) := inf

d r

: d,r ∈ N, X1,... ,Xn ∈ Sd, Tr(Xi) = r (i ∈ V ), Xi2 = Xi (i ∈ V ), XiXj = 0 ({i,j} ∈ E) .

![image 40](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile40.png>)

- Proposition 3.5 ([28]). For any graph G we have ξf(G) ≤ χq(G).

Proof. Set k = χq(G). It is shown in [9] that in the deﬁnition of χq(G) from (13)–(14), one may assume w.l.o.g. that all matrices Xic have the same rank, say, r. Then, for any given color c ∈ [k], the matrices Xic (i ∈ V ) provide a feasible solution to ξf(G) with value d/r. Finally, d/r = k holds since by (13)–(14) we have d = rank(I) = kc=1 rank(Xic) = kr.

![image 41](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile41.png>)

![image 42](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile42.png>)

![image 43](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile43.png>)

![image 44](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile44.png>)

In [41, Prop. 5.11] it is shown that the projective rank can equivalently be deﬁned as ξf(G) = inf λ : A is a ﬁnite dimensional C∗-algebra with tracial state τ, Xi ∈ A projector with τ(Xi) = 1/λ(i ∈ V ), XiXj = 0 ({i,j} ∈ E) .

They also deﬁne the tracial rank ξtr(G) of G as the parameter obtained by omitting in the above deﬁnition of ξf(G) the restriction that A has to be ﬁnite dimensional. The motivation for the parameter ξtr(G) is that it lower bounds the commuting quantum chromatic number [41, Thm. 5.11]: ξtr(G) ≤ χqc(G).

In view of Theorems 2.4 and 2.5, we obtain the following reformulations: ξf(G) = inf L(1) : L ∈ R x ∗ tracial, symmetric, positive, rank(M(L)) < ∞, L(xi) = 1 (i ∈ V ), L = 0 on I(HG) ,

and ξtr(G) is obtained by the same program without the restriction rank(M(L)) < ∞. In addition, using Theorem 2.5(3), we see that in this formulation of ξf(G) we can equivalently optimize over all L that are conic combinations of trace evaluations at projectors Xi ∈ Sd (for some d ∈ N) satisfying XiXj = 0 for all {i,j} ∈ E. If we restrict the optimization to scalar evaluations (d = 1) we obtain the fractional chromatic number. This shows that the projective rank can be seen as the noncommutative analogue of the fractional chromatic number, as was already observed in [28, 41].

The above formulations of the parameters ξtr(G) and ξf(G) in terms of linear functionals also show that they ﬁt within the following hierarchy {ξrcol(G)}r∈N∪{∞}, deﬁned as the noncommutative tracial analogue of the hierarchy {lascolr (G)}r:

ξrcol(G) = inf L(1) : L ∈ R x ∗2r tracial, symmetric, and positive, L(xi) = 1 (i ∈ V ), L = 0 on I2r(HG) .

Again, ξ∗col(G) is the parameter obtained by adding the constraint rank(M(L)) < ∞ to the program deﬁning ξ∞col(G). By the above discussion the following holds.

- Proposition 3.6. We have ξ∗col(G) = ξf(G) ≤ χq(G) and ξ∞col(G) = ξtr(G) ≤ χqc(G).


Using Lemma 2.7 one can verify that the parameters ξrcol(G) converge to ξ∞col(G). Moreover, by Theorem 2.6, if ξrcol(G) admits a ﬂat optimal solution, then we have ξrcol = ξ∗col(G). Also, the parameter ξ1col(G) coincides with lascol1 (G) = ϑ(G). Summarizing we have ξ∞col(G) = ξtr(G) ≤ χqc(G) and the following chain of inequalities

![image 45](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile45.png>)

ϑ(G) = ξ1col(G) ≤ ξrcol(G) ≤ ξ∞col(G) = ξtr(G) ≤ ξ∗col(G) = ξf(G) ≤ χq(G).

![image 46](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile46.png>)

Observe that the bounds lascolr (G) and ξrcol(G) remain below the fractional chromatic number χf(G), since ξf(G) = ξ∗col(G) ≤ lascol∗ (G) = χf(G). Hence, these bounds are weak if χf(G) is close to ϑ(G) and far from χ(G) or χq(G). In the classical setting this is the case, e.g., for the class of Kneser graphs G = K(n,r), with vertex set the set of all r-subsets of [n] and having an edge between any two disjoint r-subsets. By results of Lov´asz [26, 27], the fractional chromatic number is n/r, which is known to be equal to ϑ(K(n,r)), while the chromatic number is n − 2r + 2. In [18] this was used as a motivation to deﬁne a new hierarchy of lower bounds {Λr(G)} on the chromatic number that can go beyond the fractional chromatic number. In Section 3.3 we recall this approach and show that its extension to the tracial setting recovers the hierarchy {γrcol(G)} introduced in Section 3.1. We also show how a similar technique can be used to recover the hierarchy {γrstab(G)}.

![image 47](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile47.png>)

![image 48](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile48.png>)

- 3.2.3 A link between ξrstab(G) and ξrcol(G)

In [18, Thm. 3.1] it is shown that, for any r ≥ 1, the bounds lasstabr (G) and lascolr (G) satisfy lasstabr (G)lascolr (G) ≥ |V |, with equality if G is vertex-transitive, which extends a well-known property of the theta number (case r = 1). The same holds for the noncommutative analogues ξrstab(G) and ξrcol(G).

Lemma 3.7. For any graph G = (V,E) and r ∈ N ∪ {∞,∗} we have ξrstab(G)ξrcol(G) ≥ |V |, with equality if G is vertex-transitive.

Proof. Let L be feasible for ξrcol(G). Then L˜ = L/L(1) provides a solution to ξrstab(G) with value L˜ i∈V xi = |V |/L(1), implying that ξrstab(G) ≥ |V |/L(1) and therefore ξrstab(G)ξrcol(G) ≥ |V |.

Assume G is vertex-transitive. Let L be a feasible solution for ξrstab(G). As G is vertextransitive we may assume (after symmetrization) that L(xi) is constant, set L(xi) =: 1/λ for all i ∈ V , so that the objective value of L for ξrstab(G) is |V |/λ. Then L˜ = λL provides a feasible solution for ξrcol(G) with value λ, implying ξrcol(G) ≤ λ. This implies ξrcol(G)ξrstab(G) ≤ |V |.

![image 49](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile49.png>)

![image 50](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile50.png>)

![image 51](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile51.png>)

![image 52](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile52.png>)

For vertex-transitive G, the inequality ξf(G)αq(G) ≤ |V | is shown in [28, Lem. 6.5]; it can be recovered from the r = ∗ case of Lemma 3.7 and αq(G) ≤ αp(G).

- 3.2.4 Comparison to existing semideﬁnite programming bounds


By adding the inequalities L(xixj) ≥ 0, for all i,j ∈ V , to ξ1col(G), we obtain the strengthened theta number ϑ+(G) (from [50]). Moreover, if we add the constraints

![image 53](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile53.png>)

L(xixj) ≥ 0 for i = j ∈ V, (18)

L(xixj) ≤ 1 for i ∈ V, (19)

j∈C

L(xixj) ≥ |C| + |C′| for C,C′ distinct cliques in G (20)

L(1) +

i∈C,j∈C′

to the program deﬁning the parameter ξ1col(G), then we obtain the parameter ξSDP(G), which is introduced in [41, Thm. 7.3] as a lower bound on ξtr(G). We will now show that the inequalities (18)–(20) are in fact valid for ξ2col(G), which implies

ξ2col(G) ≥ ξSDP(G) ≥ ϑ+(G).

![image 54](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile54.png>)

For this, given a clique C in G, we deﬁne the polynomial gC := 1 − i∈C xi ∈ R x . Then (19) and (20) can be reformulated as L(xigC) ≥ 0 and L(gCgC′) ≥ 0, respectively, using the fact that L(xi) = L(x2i ) = 1 for all i ∈ V . Hence, to show that any feasible L for ξ2col(G) satisﬁes (18)(20), it suﬃces to show Lemma 3.8 below. Recall that a commutator is a polynomial of the

form [p,q] = pq−qp with p,q ∈ R x . We denote the set of linear combinations of commutators [p,q] with deg(pq) ≤ r by Θr.

- Lemma 3.8. Let C and C′ be cliques in a graph G and let i,j ∈ V . Then we have gC ∈ M2(∅) + I2(HG), and xixj, xigC, gCgC′ ∈ M4(∅) + I4(HG) + Θ4.


Proof. The claim gC ∈ M2(∅) + I2(HG) follows from the identity gC = 1 −

2

(xi − x2i) +

= gC2 + h, (21)

+

xixj

xi

i∈C

i =j∈C

i∈C

![image 55](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile55.png>)

![image 56](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile56.png>)

![image 57](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile57.png>)

![image 58](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile58.png>)

gC

h

where h ∈ I2(HG). We also have xixj = xix2jxi + xj(xi − x2i) + x2i(xj − x2j) + [xi,xix2j] + [xi − x2i,xj], xigC = xigC2 xi + gC2 (xi − x2i) + [xi − x2i ,gC2 ] + [xi,xigC2 ],

and, writing analogously gC′ = gC2 ′ + h′ with h′ ∈ I2(HG), we have gCgC′ = gCgC2 ′gC + [gC,gCgC2 ′] + [h,gC2 ′] + gC2 h′ + hh′ + gC2 ′h.

![image 59](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile59.png>)

![image 60](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile60.png>)

![image 61](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile61.png>)

![image 62](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile62.png>)

Using ξSDP(G), it is shown in [41, Thm. 7.4] that for the odd cycle C2n+1, the tracial rank satisﬁes ξ∞col(C2n+1) = (2n + 1)/n. Combining this with Lemma 3.7 gives n = ξ∞stab(C2n+1) ≥ αqc(C2n+1). Equality holds since αqc(C2n+1) ≥ α(C2n+1) = n.

## 3.3 Links between the bounds γrcol(G), ξrcol(G), γrstab(G), and ξrstab(G)

Here, in this last section, we make the link between the hierarchies {ξrstab(G)} (resp. {ξrcol(G)}) and {γrstab(G)} (resp. {γrcol(G)}). The key fact is the interpretation of the coloring and stability numbers in terms of certain graph products.

We start with the (quantum) coloring number. For an integer k, recall that the Cartesian product G Kk is the graph with vertex set V × [k], where the vertices (i,c) and (j,c′) are adjacent if ({i,j} ∈ E and c = c′) or (i = j and c = c′). The following is a well-known reduction of the chromatic number χ(G) to the stability number of the Cartesian product G Kk: χ(G) = min k ∈ N : α(G Kk) = |V | . It was used in [18] to deﬁne the following lower bounds on the chromatic number:

Λr(G) = min k ∈ N : lasstabr (G Kk) = |V | ,

where it was also shown that lascolr (G) ≤ Λr(G) ≤ χ(G) for all r ≥ 1, with equality Λ|V|(G) = χ(G). Hence the bounds Λr(G) may go beyond the fractional chromatic number. This is the case for the above mentioned Kneser graphs; see [17] for other graph instances.

The above reduction from coloring to stability number has been extended to the quantum setting by [28], where it is shown that χq(G) = min{k ∈ N : αq(G Kk) = |V |}. It is therefore natural to use the upper bounds ξrstab(G Kk) on αq(G Kk) in order to get the following lower bounds on the quantum coloring number:

min{k : ξrstab(G Kk) = |V |}, (22) which are thus the noncommutative analogues of the bounds Λr(G). Observe that, for any integer k ∈ N and r ∈ N ∪ {∞,∗}, we have ξrstab(G Kk) ≤ |V |, which follows from Lemma 3.8 and the fact that the cliques Ci = {(i,c) : c ∈ [k]}, for i ∈ V , cover all vertices in G Kk. Let CG Kk = gCi : i ∈ V , where gCi = 1 − c∈[k] xci, denote the set of polynomials corresponding to these cliques. We now show that the parameters (22) coincide in fact with γrcol(G) for all r ∈ N ∪ {∞}. For this observe ﬁrst that the quadratic polynomials in the set HG,kcol correspond precisely to the edges of G Kk, and the projector constraints are included in I2(HG,kcol ) (see Section 3.1), so that I2r(HG,kcol ) = I2r(HG Kk ∪ CG Kk). We will also use the following result.

- Lemma 3.9. Let r ∈ N ∪ {∞,∗} and assume L is feasible for ξrstab(G Kk). Then, we have L( i∈V,c∈[k] xci) = |V | if and only if L = 0 on I2r(CG Kk).


Proof. First: If L = 0 on I2r(CG Kk), then 0 = i∈V L(gCi) = |V | − L( i,c xci).

Conversely assume that 0 = L i∈V,c∈[k] xci − |V | = i∈V L(gCi). We will show L = 0 on I2r(CG Kk). For this we ﬁrst observe that gCi − (gCi)2 ∈ I2(HG Kk) by (21). Hence L(gCi) = L(gC2

) ≥ 0, which, combined with i L(gCi) = 0, implies L(gCi) = 0 for all i ∈ V . Next we show L(wgCi) = 0 for all words w with degree at most 2r − 1, using induction on deg(w). The base case w = 1 holds by the above. Assume now w = uv, where deg(v) < deg(u) ≤ r. Using

i

v)1/2. Note that it suﬃces to show L(v∗gCiv) = 0 since, using again (21), this implies L(v∗gC2

the positivity of L, the Cauchy-Schwarz inequality gives |L(uvgCi)| ≤ L(u∗u)1/2L(v∗gC2

i

v) = 0 and thus L(uvgCi) = 0. Using the tracial property of L and the induction assumption, we see that L(v∗gCiv) = L(vv∗gCi) = 0 since deg(vv∗) < deg(w).

i

![image 63](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile63.png>)

![image 64](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile64.png>)

![image 65](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile65.png>)

![image 66](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile66.png>)

- Proposition 3.10. For r ∈ N ∪ {∞} we have γrcol(G) = min{k : ξrstab(G Kk) = |V |}.

Proof. Let L be a linear functional certifying γrcol(G) ≤ k. Then L is feasible for ξrstab(G Kk) and, as L = 0 on I2r(CG Kk), Lemma 3.9 shows that L( i,c xci) = |V |. This shows that ξrstab(G Kk) = |V | and thus min{k : ξrstab(G Kk) = |V |} ≤ k.

Conversely, assume ξrstab(G Kk) = |V |. Since the optimum is attained, there exists a linear functional L feasible for ξrstab(G Kk) with L( i,c xci) = |V |. Using Lemma 3.9 we can conclude that L is zero on I2r(CG Kk) and thus also on I2r(HG,kcol ). This shows γrcol(G) ≤ k.

![image 67](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile67.png>)

![image 68](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile68.png>)

![image 69](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile69.png>)

![image 70](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile70.png>)

Note that the proof of Proposition 3.10 also works in the commutative setting; this shows that the sequence Λr(G) corresponds to the usual Lasserre hierarchy for the feasibility problem deﬁned by the equations (13)–(14), which is another way of showing Λ∞(G) = χ(G).

We now turn to the (quantum) stability number. For k ∈ N, consider the graph product Kk ⋆ G, with vertex set [k] × G, and with an edge between (c,i) and (c′,j) when (c = c′,i = j) or (c = c′,i = j) or (c = c′,{i,j} ∈ E). The product Kk ⋆ G coincides with the homomorphic product Kk⋉G used in [28, Sec. 4.2], where it is shown that αq(G) = max k ∈ N : αq(Kk⋆G) = k . This suggests using the upper bounds ξrstab(Kk ⋆ G) on αq(Kk ⋆ G) to deﬁne the following upper bounds on αq(G):

![image 71](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile71.png>)

max k ∈ N : ξrstab(Kk ⋆ G) = k . (23) For each c ∈ [k], the set Cc = {(c,i) : i ∈ V } is a clique in Kk ⋆ G and we let CKk⋆G =

gCc : c ∈ [k] , where gCc = 1 − i∈V xic, denote the set of polynomials corresponding to these cliques. Since these k cliques cover the vertex set of Kk ⋆ G, we can use Lemma 3.8 to conclude ξrstab(Kk ⋆ G) ≤ k for all r ∈ N ∪ {∞,∗}. Again, observe that the quadratic polynomials in the set HG,kstab correspond precisely to the edges of Kk ⋆ G and that we have I2r(HG,kstab) = I2r(HKk⋆G ∪ CKk⋆G). Based on this, one can show the analogue of Lemma 3.9: If L is feasible for the program ξrstab(Kk ⋆ G), then we have L( i,c xic) = k if and only if L = 0 on I2r(CKk⋆G), which implies the following result.

- Proposition 3.11. For r ∈ N ∪ {∞} we have γrstab(G) = max{k : ξrstab(Kk ⋆ G) = k}. We do not know whether the results of Propositions 3.10 and 3.11 hold for r = ∗, since


we do not know whether the supremum is attained in the parameter ξ∗stab(·) = αp(·) (as was already observed in [45, p. 120]). Hence we can only claim the inequalities

γ∗col(G) ≥ min{k : ξ∗stab(G Kk) = |V |} and γ∗stab(G) ≤ max{k : ξ∗stab(Kk ⋆ G) = k}.

As mentioned above, we have lascolr (G) ≤ Λr(G) for any r ∈ N [18, Prop. 3.3]. This result extends to the noncommutative setting and the analogous result holds for the stability parameters. In other words the hierarchies {γrcol(G)} and {γrstab(G)} reﬁne the hierarchies {ξrcol(G)} and ξrstab(G)}.

- Proposition 3.12. For r ∈ N ∪ {∞,∗}, ξrcol(G) ≤ γrcol(G) and ξrstab(G) ≥ γrstab(G).


Proof. We may restrict to r ∈ N since we have seen earlier that the inequalities hold for r ∈ {∞,∗}. The proof for the coloring parameters is similar to the proof of [18, Prop. 3.3] in the classical case and thus omitted. We show the inequality ξrstab(G) ≥ γrstab(G). Set k = γrstab(G) and, using Proposition 3.11, let L ∈ R xic : i ∈ V,c ∈ [k] ∗2r be optimal for ξrstab(Kk⋆G) = k. That is, L is tracial, symmetric, positive, and satisﬁes L(1) = 1, L( i,c xic) = k, and L = 0 on I(HKk⋆G). It suﬃces now to construct a tracial symmetric positive linear form Lˆ ∈ R xi : i ∈ V ∗2r such that Lˆ(1) = 1, Lˆ( i∈V xi) = k, and Lˆ = 0 on I2r(HG), since this will imply ξrstab(G) ≥ k. For this, for any word xi1 ··· xit with degree 1 ≤ t ≤ 2r, we deﬁne Lˆ(xi1 ··· xit) := c∈[k] L(xic1 ··· xict). Also, we set Lˆ(1) = L(1) = 1. Then, we have Lˆ( i∈V xi) = k. Moreover, one can easily check that Lˆ is indeed tracial, symmetric, positive, and vanishes on I2r(HG).

![image 72](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile72.png>)

![image 73](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile73.png>)

![image 74](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile74.png>)

![image 75](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile75.png>)

# References

- [1] D. Avis, J. Hasegawa, Y. Kikuchi, and Y. Sasaki. A quantum protocol to win the graph coloring game on all Hadamard graphs. IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences, E89-A(5):1378–1381, 2006.
- [2] G. P. Barker, L. Q. Eiﬂer, and T. P. Kezlan. A non-commutative spectral theorem. Linear Algebra and its Applications, 20(2):95–100, 1978.
- [3] J. S. Bell. On the Einstein Podolsky Rosen paradox. Physics, 1(3):195–200, 1964.
- [4] B. Blackadar. Operator Algebras: Theory of C∗-Algebras and Von Neumann Algebras. Encyclopaedia of Mathematical Sciences. Springer, 2006.
- [5] N. Brunner, S. Pironio, A. Acin, N. Gisin, A. A. Me´thot, and V. Scarani. Testing the dimension of Hilbert spaces. Physical Review Letters, 100:210503, 2008.
- [6] S. Burgdorf, K. Cafuta, I. Klep, and J. Povh. The tracial moment problem and traceoptimization of polynomials. Mathematical Programming, 137(1):557–578, 2013.
- [7] S. Burgdorf and I. Klep. The truncated tracial moment problem. Journal of Operator Theory, 68(1):141–163, 2012.
- [8] S. Burgdorf, I. Klep, and J. Povh. Optimization of Polynomials in Non-Commutative Variables. Springer Briefs in Mathematics. Springer, 2016.
- [9] P. J. Cameron, A. Montanaro, M. W. Newman, S. Severini, and A. Winter. On the quantum chromatic number of a graph. The Electronic Journal of Combinatorics, 14(1), 2007.
- [10] R. E. Curto and L. A. Fialkow. Solution of the Truncated Complex Moment Problem for Flat Data, volume 568 of Memoirs of the American Mathematical Society. American Mathematical Society, 1996.
- [11] A.C. Doherty, Y.-C. Liang, B. Toner, and S. Wehner. The quantum moment problem and bounds on entangled multiprover games. Proceedings of the 2008 IEEE 23rd Annual Conference on Computational Complexity, pages 199–210, 2008.
- [12] K. J. Dykema and V. I. Paulsen. Synchronous correlation matrices and Connes’ embedding conjecture. Journal of Mathematical Physics, 57:015214, 2016.
- [13] K. J. Dykema, V. I. Paulsen, and J. Prakash. Non-closure of the set of quantum correlations via graphs. arXiv:1709.05032, 2017.
- [14] T. Fritz. Tsirelson’s problem and Kirchberg’s conjecture. Reviews in Mathematical Physics, 24(05), 2012.
- [15] S. Gribling, D. de Laat, and M. Laurent. Lower bounds on matrix factorization ranks via noncommutative polynomial optimization. arXiv:1708.01573, 2017.
- [16] S. Gribling, D. de Laat, and M. Laurent. Matrices with high completely positive semideﬁnite rank. Linear Algebra and its Applications, 513:122–148, 2017.


- [17] N. Gvozdenovic´ and M. Laurent. Computing semideﬁnite programming lower bounds for the (fractional) chromatic number via block-diagonalization. SIAM Journal on Optimization, 19(2):592–615, 2008.
- [18] N. Gvozdenovic´ and M. Laurent. The operator ψ for the chromatic number of a graph. SIAM Journal on Optimization, 19(2):572–591, 2008.
- [19] Z. Ji. Binary constraint system games and locally commutative reductions. arXiv:1310:3794, 2013.
- [20] M. Junge, M. Navascues, C. Palazuelos, D. Perez-Garcia, V.B. Scholtz, and R.F. Werner. Connes’ embedding problem and Tsirelson’s problem. Journal of Mathematical Physics, 52:012102, 2011.
- [21] I. Klep and J. Povh. Constrained trace-optimization of polynomials in freely noncommuting variables. Journal of Global Optimization, 64(2):325–348, 2016.
- [22] I. Klep and M. Schweighofer. Connes’ embedding conjecture and sums of Hermitian squares. Advances in Mathematics, 217(4):1816–1837, 2008.
- [23] J. B. Lasserre. Global optimization with polynomials and the problem of moments. SIAM Journal on Optimization, 11(3):796–817, 2001.
- [24] M. Laurent. A comparison of the Sherali-Adams, Lov´asz-Schrijver, and Lasserre relaxations for 0-1 programming. Mathematics of Operations Research, 28(3):470–496, 2003.
- [25] M. Laurent and T. Piovesan. Conic approach to quantum graph parameters using linear optimization over the completely positive semideﬁnite cone. SIAM Journal on Optimization, 25(4):2461–2493, 2015.
- [26] L. Lov´asz. Kneser’s conjecture, chromatic number, and homotopy. Journal of Combinatorial Theory, Series A, 25(3):319 – 324, 1978.
- [27] L. Lov´asz. On the shannon capacity of a graph. IEEE Transactions on Information Theory, 25(1):1–7, 2006.
- [28] L. Mancˇinska and D. E. Roberson. Quantum homomorphisms. Journal of Combinatorial Theory, Series B, 118:228–267, 2016.
- [29] L. Mancˇinska, G. Scarpa, and S. Severini. New separations in zero-error channel capacity through projective Kochen-Specker sets and quantum coloring. IEEE Transactions on Information Theory, 59(6):4025–4032, 2013.
- [30] M. Navascue´s, A. Feix, M. Araujo, and T. Ve´rtesi. Characterizing ﬁnite-dimensional quantum behavior. Physical Review A, 92, 2015.
- [31] M. Navascue´s, S. Pironio, and A. Acı´n. A convergent hierarchy of semideﬁnite programs characterizing the set of quantum correlations. New Journal of Physics, 10(7):073013, 2008.
- [32] M. Navascue´s, S. Pironio, and A. Acı´n. SDP relaxations for non-commutative polynomial optimization. In M. F. Anjos and J. B. Lasserre, editors, Handbook on Semideﬁnite, Conic and Polynomial Optimization, pages 601–634. Springer, 2012.
- [33] M. Navascue´s and T. Ve´rtesi. Bounding the set of ﬁnite dimensional quantum correlations. Physical Review Letters, 115(2):020501, 2015.
- [34] J. Nie. Symmetric tensor nuclear norms. SIAM Journal on Applied Algebra and Geometry, 1(1):599–625, 2017.
- [35] M. A. Nielsen and I. L. Chuang. Quantum Computation and Quantum Information. Cambridge University Press, 2000.
- [36] C. M. Ortiz and V. I. Paulsen. Quantum graph homomorphisms via operator systems. Linear Algebra and its Applications, 497:23–43, 2016.
- [37] N. Ozawa. About the Connes’ embedding problem–algebraic approaches. Japanese Journal of Mathematics, 8(1):147–183, 2013.
- [38] K F. Pa´l and T. Ve´rtesi. Eﬃciency of higher-dimensional Hilbert spaces for the violation of Bell inequalities. Physical Review A, 77:042105, 2008.
- [39] C. Palazuelos and T. Vidick. Survey on nonlocal games and operator space theory. Journal of Mathematical Physics, 57(1):015220, 2016.


- [40] P. A. Parrilo. Structured Semideﬁnite Programs and Semialgebraic Geometry Methods in Robustness and Optimization. PhD thesis, Caltech, 2000.
- [41] V. I. Paulsen, S. Severini, D. Stahlke, I. G. Todorov, and A. Winter. Estimating quantum chromatic numbers. Journal of Functional Analysis, 270(6):2188–2222, 2016.
- [42] S. Pironio, M. Navascue´s, and A. Acı´n. Convergent relaxations of polynomial optimization problems with noncommuting variables. SIAM Journal on Optimization, 20(5):2157–2180, 2010.
- [43] A. Prakash, J. Sikora, A. Varvitsiotis, and Z. Wei. Completely positive semideﬁnite rank. Mathematical Programming Series A, 2017. To appear.
- [44] A. Prakash and A. Varvitsiotis. Matrix factorizations of correlation matrices and applications. arXiv:1702.06305, 2017.
- [45] D. E. Roberson. Variations on a Theme: Graph Homomorphisms. PhD thesis, University of Waterloo, 2013.
- [46] J. Sikora and A. Varvitsiotis. Linear conic formulations for two-party correlations and values of nonlocal games. Mathematical Programming, 162(1):431–463, 2017.
- [47] J. Sikora, A. Varvitsiotis, and Z. Wei. Minimum dimension of a Hilbert space needed to generate a quantum correlation. Physical Review Letters, 2016.
- [48] W. Slofstra. The set of quantum correlations is not closed. arXiv:1703.08618, 2017.
- [49] C. Stark. Learning optimal quantum models is NP-hard. arXiv:1510.02800, 2015.
- [50] M. Szegedy. A note on the theta number of Lov´asz and the generalized Delsarte bound. In Proceedings of the 35th Annual IEEE Symposium on Foundations of Computer Science, pages 36–39, 1994.
- [51] G. Tang and P. Shah. Guaranteed tensor decomposition: A moment approach. In Proceedings of the 32nd International Conference on Machine Learning, pages 1491–1500, 2015.
- [52] B. Tsirelson. Bell inequalities and operator algebras. Technical report, 2006. http://www.tau.ac.il/~tsirel/download/bellopalg.pdf.
- [53] J. H. M. Wedderburn. Lectures on Matrices. Dover Publications Inc., 1964.
- [54] S. Wehner, M. Christandl, and A. C. Doherty. Lower bound on the dimension of a quantum system given measured data. Physical Review A, 78:062112, 2008.


# A Synchronous quantum correlations

We prove the following result by combining proofs from [46] (see also [28]) and [41].

Proposition A.1. The smallest local dimension in which a synchronous quantum correlation P can be realized is given by the completely positive semideﬁnite rank of the matrix MP indexed by S × A with entries (MP)(s,a),(t,b) = P(a,b|s,t).

Proof. Suppose ﬁrst that (ψ,Esa,Ftb) is a realization of P in local dimension d. That is, ψ is a unit vector in Cd ⊗ Cd, Esa,Ftb are d × d Hermitian positive semideﬁnite matrices such that

a Esa = b Ftb = I for all s,t and P(a,b|s,t) = ψ∗(Esa ⊗ Ftb)ψ for all (a,b,s,t) ∈ Γ. We will show cpsd-rankC(AP) ≤ d.

The Schmidt decomposition of the unit vector ψ gives nonnegative scalars {λi} and or-

thonormal bases {ui} and {vi} of Cd such that ψ = di=1 √λi ui ⊗ vi. If we replace ψ by d i=1

![image 76](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile76.png>)

√λi vi ⊗ vi and Esa by U∗EsaU, where U is the unitary matrix for which ui = Uvi for all i, then we obtain a new realization ( di=1 √λi vi ⊗ vi,U∗EsaU,Ftb) of P still in local dimension d. For the simplicity of notation we rename U∗EsaU as Esa. Then we deﬁne the matrices

![image 77](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile77.png>)

![image 78](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile78.png>)

d

K =

i=1

![image 79](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile79.png>)

λi vivi∗, Xsa = K1/2EsaK1/2, Ytb = K1/2FtbK1/2.

By using the identities vec(K) = ψ and

vec(K)∗(Esa ⊗ Ftb)vec(K) = Tr(KEsaKFtb) = Tr(K1/2EsaK1/2K1/2FtbK1/2), we see that

P(a,b|s,t) = Xsa,Ytb for all a,b,s,t, (24) and

Xsa =

Ytb = K for all s,t. (25)

K,K = 1,

a

b

For each s, by applying twice the Cauchy–Schwarz inequality gives 1 =

Xsa,Ysa ≤

Xsa,Xsa 1/2 Ysa,Ysa 1/2

P(a,a|s,s) =

a

a

a

1/2

1/2

Ysa,Ysa

Xsa,Xsa

≤

a

a

1/2

1/2

Ysa,

Ysa

Xsa,

Xsa

≤

= K,K = 1.

a

a

a

a

Thus all inequalities above are equalities. The ﬁrst inequality being an equality shows that there exist scalars αs,a such that Xsa = αs,aYsa for all a,s. The second inequality being an equality shows that there exist scalars βs such that Xsa = βs Ysa for all a,s. Hence,

βs Ysa = Xsa = αs,aYsa = αs,a Ysa = αs,a Ysa for all s,a,

which shows Xsa = βsYsa for all s. Since a Xsa = K = a Ysa, we have βs = 1 for all s. Thus Xsa = Ysa for all a,s. Therefore,

(AP)(s,a),(t,b) = Xsa,Xtb for all a,b,s,t, which shows cpsd-rankC(AP) ≤ d.

For the other direction we suppose {Xsa} are Hermitian positive semideﬁnite matrices with the smallest possible size such that (AP)(s,a),(t,b) = Xsa,Xtb for all a,s,t,b. Then,

1 =

P(a,b|s,t) =

a,b

a,b

Xsa,Xtb =

a

Xsa,

b

Xtb for all s,t,

which shows the existence of a matrix K such that K = a Xsa for all s. We have K,K = 1 so that vec(K) is a unit vector, and since the factorization is smallest possible, K is invertible.

Set Esa = K−1/2XsaK−1/2 for all s,a, so that a Esa = I for all s. Then,

P(a,b|s,t) = (AP)(s,a),(t,b) = Xsa,Xtb = vec(K)∗(Esa ⊗ Etb)vec(K), which shows P has a realization of local dimension cpsd-rankC(AP).

![image 80](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile80.png>)

![image 81](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile81.png>)

![image 82](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile82.png>)

![image 83](<2017-gribling-bounds-entanglement-dimensions-quantum_images/imageFile83.png>)

