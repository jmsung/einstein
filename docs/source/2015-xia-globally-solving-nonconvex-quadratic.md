---
type: source
kind: paper
title: Globally Solving Nonconvex Quadratic Programs via Linear Integer Programming Techniques
authors: Wei Xia, Juan C. Vera, L. Zuluaga
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1511.02423
source_local: ../raw/2015-xia-globally-solving-nonconvex-quadratic.pdf
topic: general-knowledge
cites:
---

arXiv:1511.02423v3[math.OC]13Jul2018

Globally solving Non-Convex Quadratic Programs via Linear Integer Programming techniques

Wei Xia∗1, Juan Vera†2 and Luis F. Zuluaga‡1

- 1Department of Industrial and Systems Engineering, Lehigh University

H.S. Mohler Laboratory, 200 West Packer Avenue, Bethlehem, PA 18015

- 2Department of Econometrics and Operations Research, Tilburg University 5000 LE, Tilburg, The Netherlands


July 17, 2018

Abstract

Quadratic programming (QP) is a well-studied fundamental NP-hard optimization problem which optimizes a quadratic objective over a set of linear constraints. In this paper, we reformulate QPs as a mixed-integer linear problem (MILP). This is done via the reformulation of QP as a linear complementary problem, and the use of binary variables and big-M constraints, to model the complementary constraints. To obtain such reformulation, we show how to impose bounds on the dual variables without eliminating all the (globally) optimal primal solutions; using some fundamental results on the solution of perturbed linear systems.

Reformulating non-convex QPs as MILPs provides an advantageous way to obtain global solutions as it allows the use of current state-of-the-art MILP solvers. To illustrate this, we compare the performance of our solution approach, labeled quadprogIP, with the current benchmark global QP solver quadprogBB, as well as with BARON, one of the leading non-linear programming (NLP) solvers, and CPLEX’s non-convex QP solver, on a large variety of QP test instances. In practice, quadprogIP is shown to typically outperform by orders of magnitude quadprogBB, BARON, and CPLEX on standard QPs. For general QPs, quadprogIP outperforms quadprogBB, outperforms BARON in most instances, while CPLEX performs the best on these instances. For box-constrained QPs, quadprogIP has a comparable performance to quadprogBB and BARON in small- to medium-scale instances, but is outperformed by these solvers on large-scale instances; while CPLEX performs the best on box-constrained QP instances. Also, unlike quadprogBB, the solution approach proposed here is able to solve QP instances whose dual feasible set is unbounded. The MATLAB code, called quadprogIP, and the instances used to perform these numerical experiments are publicly available at https://github.com/xiawei918/quadprogIP.

# 1 Introduction

Quadratic programmming (QP), is a fundamental optimization problem with a quadratic objective and linear constraints. QP is NP-hard (see, e.g., Pardalos and Vavasis 1991, and the references therein), however, when the objective is convex, QP can be globally solved (within a predetermined precision ǫ > 0) in polynomial time via interior-point methods (see, e.g., Renegar 2001). Here, the focus is on obtaining global solutions for non-convex QP. QP is arguably the most basic instance of a (non-convex), non-linear program (NLP). At a fundamental level, the complexity of globally solving QP lies in the fact that multiple of its local optimal solutions may not necessarily be global optimal solutions (see, e.g. Bertsekas 1999).

QPs commonly arise in applications in engineering, pure and social sciences, ﬁnance, and economics (see, e.g., Horst et al. 2000). As a result, there has been extensive work on studying how to

![image 1](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile1.png>)

∗wex213@lehigh.edu †j.c.veralizcano@uvt.nl ‡luis.zuluaga@lehigh.edu, Corresponding author.

obtain global solutions of QPs using both NLP techniques (see, Gould et al. 2003, Gao 2004, for surveys in this area), and convex optimization techniques (consider, e.g., Nesterov 1998, Kim and Kojima 2001, 2003, Chen and Burer 2012, among many others).

In this paper, we reformulate QPs as a mixed-integer linear problem (MILP). This provides an advantageous way to obtain global solutions as it allows the use of current state-of-the-art MILP solvers. Moreover, the numerical experiments of Section 3 show that a basic implementation of the proposed algorithm, which we refer to as quadprogIP, typically outperform by orders of magnitude quadprogBB, BARON, and CPLEX on standard QPs. For general QPs, quadprogIP outperforms quadprogBB, outperforms BARON in most instances, while CPLEX performs the best on these instances. For box-constrained QPs, quadprogIP has a comparable performance to quadprogBB and BARON in small- to medium-scale instances, but is outperformed by these solvers on large-scale instances; while CPLEX performs the best on boxconstrained QP instances.

Unlike quadprogBB, the solution approach proposed here is able to solve QP instances whose dual feasible set is unbounded. The MATLAB code and the instances used to perform these numerical experiments are available at https://github.com/xiawei918/quadprogIP.

To obtain the proposed MILP-reformulation (see Sec. 2.1), the QP’s KKT conditions are used to reformulate the QP as a linear complementarity problem (LCP). In this reformulation, the complexity of the problem is captured by the complementarity constraints. The KKT-branching approach (Burer and Vandenbussche 2009), which consist on branching on this complementarity constraints, is not useful on this reformulation of the problem, as the underlying linear relaxations at the root node of the KKT-branching tree are (under mild assumptions) unbounded (Burer and Vandenbussche 2009, Cor. 2.3). Another alternative, namely, reformulating the complementarity constraints using binary variables and big M constraints, requires the knowledge of bounds on the problem’s KKT multipliers, which in general are unbounded (cf., Hu et al. 2012, Sec. 6.1 and 6.2). To directly use MILP solvers for the solution of the QP, we overcome this requirement by restricting our attention to a subset of optimal KKT points. We show (Theorem 1) that it is possible to impose bounds on the dual variables without eliminating all the (globally) optimal primal solutions. Our results are based on fundamental results on the approximate solution of systems of linear equations (e.g., Gu¨ler et al. 1995, Mangasarian 1981). One advantage of the proposed methodology is that unlike previous related work, the convergence of the MILP-based approach to the QP’s global optimal solution in ﬁnite time follows in straightforward fashion (see Sec. 3.1.1). Also, the methodology can be applied to QPs without the need for assumptions on the relative interior of its feasible set (see Sec. 2.3 for details).

Before stating the results described above, we end this section with a short review of both NLP and convex optimization techniques for the global solution of QP’s. Using NLP techniques, Vanderbei and Shanno

(1999) proposed an interior-point algorithm for NLPs (thus, applicable for QPs), which is an extension of the interior-point methods for linear and convex optimization problems (cf., Renegar 2001). Floudas and Visweswaran (1990) proposed an algorithm which globally solves certain classes of NLPs by decomposing the problem based on an appropriate partition of its decision variables. The work of Belotti et al. (2009) and Tawarmalani and Sahinidis (2004) on the use of relaxation and linearization techniques (cf., Sherali and Adams 1994), in combination with spatial branching techniques (cf., Tawarmalani and Sahinidis 2004), has lead to the development of the two well-known global solvers Couenne (Belotti 2010) and BARON (Sahinidis 1996) for NLPs. Another solver that combines these type of techniques, together with techniques to exploit the problems structure is GloMIQO, developed by Misener and Floudas (2013) for the solution of more general quadratically constrained quadratic programs with integer variables. More recently, specialized solution approaches have been developed for special classes of QP. In particular, Bonami et al. (2016b) develop a special branch-and-cut algorithm for box constrained QPs based on using cuts derived from the boolean quadric polytope. Also, Bonami et al. (2016a) develop new specialized cuts that are used within a spatial branch and bound algorithm to solve standard QPs. For further review of numerical and theoretical results on the solution of QPs using NLP techniques, we refer the reader to Gould et al. (2003) and Gao (2004).

Besides NLP techniques, convex optimization techniques (cf., Renegar 2001, Ben-Tal and Nemirovski 2001) have also been used to address the solution of QPs. For example, Nesterov (1998) and later Kim and Kojima (2001, 2003), explored the use of semideﬁnite programming (SDP) as well as secondorder cone relaxations to approximately or globally solve a QP.

More recently, Burer and Vandenbussche (2009) proposed a SDP-based branch and bound approach to globally solve box-constrained QPs; they reformulate a QP by adding the QP’s corresponding KarushKuhn-Tucker (KKT) conditions as redundant constraints. Let us refer to this quadratically constrained quadratic program (QCQP) as QPKKT. To solve QPKKT, Burer and Vandenbussche (2009) construct a ﬁnite KKT-branching tree by branching on the resulting problem’s complementarity constraints. SDP

relaxations of QPKKT are used to obtain lower bounds at each node of the KKT-branching tree. On the other hand, to obtain upper bounds a (local) QP-solver based on NLP techniques is used. Chen and Burer (2012) improved the solution methodology of Burer and Vandenbussche (2009) by obtaining tighter lower bounds at each node of the KKT-branching tree. For that purpose, the double non-negative (DNN) relaxation of the completely positive reformulation (Burer 2009) of QPKKT at each node of the KKTbranching tree is used. Chen and Burer (2012) provide a MATLAB implementation of their approach called quadprogBB. In this implementation, the MATLAB (local) QP solver quadprog is used to obtain the upper bounds while the algorithm proposed by Burer (2010) is used to obtain lower bounds, at each node of the KKT-branching tree. Chen and Burer (2012) show that this solution approach typically outperforms the solver Couenne and the approach proposed by Burer and Vandenbussche (2009) on a test bed of publicly available QP instances. This makes the solver quadprogBB a current benchmark for the global solution of QP problems.

The rest of the paper is organized as follows. In Section 2, we formally introduce the QP problem and present the theoretical results that serve as the foundation for the proposed solution approach. In Section 3, we illustrate the eﬀectiveness of this approach by presenting relevant numerical results on test instances of the QP problem. To conclude, in Section 4, we provide conclusions and directions for future work.

# 2 Solution Approach for non-convex QPs

We consider the following quadratic programming problem QP : min 12x⊺Hx + f⊺x s. t. Ax = b x ≥ 0,

![image 2](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile2.png>)

(1)

where f ∈ Rn, A ∈ Rm×n, b ∈ Rm, and H ∈ Rn×n is a symmetric matrix. Note that there is no assumption on the matrix H being positive semideﬁnite; that is, QP is in general a non-convex optimization problem (cf., Bertsekas 1999).

Similar to Burer and Vandenbussche (2009) and Chen and Burer (2012), we assume that the feasible set of QP is nonempty and bounded. However, in what follows, no further assumption is made about the feasible set of QP.

- 2.1 Mixed-integer linear programming reformulation


After introducing the Lagrange multipliers µ ∈ Rm for its equality constraints and λ ∈ Rn for its non-negativity constraints, the KKT conditions for QP are given by

Hx + f + A⊺µ − λ = 0 (2a) x⊺λ = 0

Ax = b (2b) x ≥ 0, λ ≥ 0. (2c)

In what follows, we will refer to the set

ΛKKT = {(x, µ, λ) ∈ R2n+m : (x,µ, λ) satisfy (2a) − (2c)} (3) as the KKT points of QP.

Note that because the feasible set of QP (1) is a polyhedron, the KKT conditions (2) are ﬁrst order necessary conditions for the optimal solutions of QP (see, e.g. Eustaquio et al. 2008, Thm. 3.3). Thus, one can add these KKT conditions as redundant constraints in QP to obtain the following equivalent formulation of QP,

min 12x⊺Hx + f⊺x s. t. Hx + f + A⊺µ − λ = 0

![image 3](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile3.png>)

x⊺λ = 0 Ax = b x ≥ 0, λ ≥ 0.

(4)

As shown by Giannessi and Tomasin (1973, Thm. 2.4), one can use the KKT conditions (2a)–(2b) to linearize the objective of (4). Namely, for any feasible solution x ∈ Rn of (4), we have

- 1

![image 4](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile4.png>)

- 2


x⊺Hx + f⊺x =

- 1

![image 5](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile5.png>)

- 2


(f⊺x − x⊺A⊺µ + x⊺λ) =

- 1

![image 6](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile6.png>)

- 2


(f⊺x − b⊺µ).

As a result, problem (4) is equivalent to the following problem with a linear (instead of quadratic) objective.

- 1

![image 7](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile7.png>)

- 2 min f⊺x − b⊺µ s. t. Hx + f + A⊺µ − λ = 0


(5)

x⊺λ = 0 Ax = b x ≥ 0, λ ≥ 0.

Notice that in (5), the complexity of QP is captured in the complementary constraints x⊺λ = 0. Next, we address the complementary constraints in (5) by using Big-M constraints. For that purpose, in Section 2.2, we derive upper bounds U, V ∈ Rn on the decision variables x, λ ∈ Rn of (5) such that there are (globally) optimal KKT points (x, µ, λ) ∈ R2n+m of QP satisfying x ≤ U, λ ≤ V . Using these upper bounds, one can show (see, Theorem 1) that a global optimal solution of QP can be obtained by solving the following MILP

IQP : 12 min f⊺x − b⊺µ s. t. Hx + f + A⊺µ − λ = 0

![image 8](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile8.png>)

Ax = b

0 ≤ xj ≤ zjUj j = 1, . . . , m 0 ≤ λj ≤ (1 − zj)Vj j = 1, . . . , m zj ∈ {0, 1} j = 1, . . . , m.

(6)

Speciﬁcally, problem IQP is a MILP with the same optimal value as QP whose optimal solutions are optimal solutions of QP.

- 2.2 Bounding the primal and dual variables


As mentioned earlier, the ﬁrst step in obtaining problem IQP is to derive explicit upper bounds U, V ∈ Rn such that there are optimal KKT points (x,µ, λ) ∈ R2n+m of QP satisfying x ≤ U, λ ≤ V .

Similar to Chen and Burer (2012), using the assumption that the feasible set of QP is non-empty and bounded, one can compute the upper bounds U ∈ Rn+ on the primal variables x ∈ Rn by setting:

Uj := max{xj : Ax = b, x ≥ 0}, (7) for every j = 1, . . . , n.

Using assumptions stronger than ours, Chen and Burer (2012) show that ΛKKT , the set of KKT points, is bounded. As the following example illustrates, under our weaker assumptions, the set ΛKKT could be unbounded.

- Example 1. Consider the instance of QP deﬁned by setting


  f =

  A =

 

 

2 0 0 0 −1 0 0 0 1

- 2 4
- 3


1 1

2 1 1 1 1 1

b =

H =

.

Note that in this case the feasible region of QP is {[0, 1 − t,t]⊺ : 0 ≤ t ≤ 1}, which is bounded and non-empty. However, the set of KKT points ΛKKT (3) is unbounded. Speciﬁcally, notice that for any v ≥ 1 the following is a KKT point for QP :

 .

  µ =

 

 

−1 + v 0 0

- 0
- 1 0


v −3 − v

λ =

x =

Thus, to handle the complementarity contrains in (5) using Big-M constraints, we do not try to obtain a bound for the value of the entries of λ ∈ Rm for all KKT points. Instead, in Theorem 1, we prove that there exist a bound that we can impose in the dual variables, without discarding all (globally) optimal KKT points of QP. For this purpose, we make use of fundamental results on the approximate solution of systems of linear equations (e.g., Gu¨ler et al. 1995, Mangasarian 1981).

Let us ﬁrst deﬁne a particular instance of the well-known Hoﬀman bound (Hoﬀman 2003), closely following the notation in Gu¨ler et al. (1995).

- Deﬁnition 1. Fix the norm   ·  α on Rn and the norm   ·  β on Rm. Given A ∈ Rm×n and b ∈ Rm, let F := {x ∈ Rn+ : Ax = b}. Let HA,b ∈ R be the smallest constant satisfying:

For all y ∈ Rn such that Ay = b, there is x ∈ F such that x − y α ≤ HA,b y− β. (8)

Above, for any y ∈ Rn, y− ∈ Rn is the vector diﬁned by yi− = max{0, −yi}, i = 1, . . . , n. That is, Deﬁnition 1 corresponds to the Hoﬀman bound obtained when looking at perturbations of only the non-negative constraints of the polyhedron F := {x ∈ Rn+ : Ax = b}.

In what follows we will use the following notation to denote the dual norm associated to a given norm.

- Deﬁnition 2. Given a norm · on Rn, its associated dual norm on Rn, denoted · ∗ is deﬁned as: x ∗ = sup{x⊺z : z ∈ Rn, z ≤ 1}.


In particular, for any x ∈ Rn, x ∗∞ = x 1. Using Deﬁnition 1, we provide in Theorem 1 below, the desired bound to be used on the dual variables

of QP in the IQP formulation (6).

Theorem 1. Let A ∈ Rm×n and b ∈ Rm be such that the set F := {x ∈ Rn+ : Ax = b} is non-empty and bounded. Let HA,b be deﬁned by (8), and M > (κ + f ∗α)HA,b e β, where κ := max{ Hx ∗α : Ax = b, x ≥ 0}. Then, there exists an optimal KKT point (x∗, µ∗, λ∗) for QP such that e⊺λ∗ ≤ M, and µ∗ ∈ Rm.

Proof. Proof. Consider the following perturbed version of QP:

min 21x⊺Hx + f⊺x + Mt s. t. Ax = b

![image 9](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile9.png>)

x ≥ −te 0 ≤ t ≤ δ,

(9)

where e is the vector of all ones, and δ > 0. Notice that the feasible set of (9) is a closed subset of {x ∈ Rn : Ax = b, x ≥ −δe} × [0, δ] which is non-empty and bounded as F is non-empty, bounded, and the recession cone of {x ∈ Rn : Ax = b, x ≥ −δe} is equal to the recession cone of F. Thus, the optimal value of (9) exists and it is attained.

Let (x∗, t∗) be an optimal solution of (9). Then, there exists (µ∗, λ∗, ρ∗, ω∗) ∈ Rn+m+2 such that (x∗, t∗, µ∗, λ∗, ρ∗, ω∗) satisﬁes the KKT conditions associated with problem (9)

Hx∗ + f + A⊺µ∗ − λ∗ = 0 M − e⊺λ∗ − ρ∗ + ω∗ = 0 (x∗ − t∗e)⊺λ∗ = 0

t∗ρ∗ = 0 (δ − t∗)ω∗ = 0

Ax∗ = b x∗ + t∗e ≥ 0 0 ≤ t∗ ≤ δ

λ∗, ρ∗, ω∗ ≥ 0,

(10)

where µ∗ ∈ Rm, λ∗ ∈ Rn, ρ∗ ∈ R, ω∗ ∈ R, are respectively the Lagrangian multipliers of problem (9) associated with the linear constraints, lower bounds in the decision variables x ∈ Rn, and lower and upper bounds on the decision variable t ∈ R.

Now we claim that t∗ = 0. In that case, notice that the complementarity constraint (δ − t∗)ω∗ = 0 in (10) implies ω∗ = 0 and thus, from the equation M − e⊺λ∗ − ρ∗ + ω∗ = 0 in (10) and the fact that ρ∗ ≥ 0, it follows that (x∗, µ∗, λ∗) satisﬁes the statement of the theorem.

To show that t∗ = 0, note that from Deﬁnition 1, it follows that there exists x′ ∈ F such that x′ − x∗ α ≤ HA,bt∗ e β. (11)

In problem (9), (x′, 0) is a feasible solution and thus the objective value of (x′, 0) is no smaller than the objective value of (x∗, t∗). That is,

- 1

![image 10](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile10.png>)

- 2


x∗⊺Hx∗ + f⊺x∗ + Mt∗ ≤

- 1

![image 11](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile11.png>)

- 2


x′⊺Hx′ + f⊺x′.

Therefore,

1 2

Mt∗ ≤

(x′⊺Hx′ − x∗⊺Hx∗) + f⊺(x′ − x∗)

![image 12](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile12.png>)

- 1

![image 13](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile13.png>)

- 2


(x′ + x∗)⊺H(x′ − x∗) + f⊺(x′ − x∗) ≤

=

- 1

![image 14](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile14.png>)

- 2


H(x′ + x∗) ∗α x′ − x∗ α + f ∗α x′ − x∗ α ≤

- 1

![image 15](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile15.png>)

- 2


( Hx′ ∗α + Hx∗ ∗α) + f ∗α x′ − x∗ α.

Thus, using (11) we have

- 1

![image 16](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile16.png>)

- 2


(κ + κδ) + f ∗α HA,b e βt∗ (12) where κδ := max{ Hx ∗α : Ax = b, x ≥ −δe, x ∈ Rn}.

Mt∗ ≤

As M > (κ + f ∗α) HA,b e β, and κδ ↓ κ when δ ↓ 0, taking δ > 0 small enough we have that M > 12(κ + κδ) + f ∗α HA,b e β. Thus, (12) implies that t∗ = 0.

![image 17](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile17.png>)

![image 18](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile18.png>)

![image 19](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile19.png>)

![image 20](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile20.png>)

![image 21](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile21.png>)

- 2.3 Computation of the dual bounds


Theorem 1 provides the bounds needed for the reformulation of QP as IQP (6) in terms of the Hoﬀman constant HA,b introduced in Deﬁnition 1. Next, we discuss how this constant can be obtained in closedform for important special classes of QP, as well as how it can be computed for general classes of QP.

- 2.3.1 Standard Quadratic Programming. Consider the standard quadratic program (SQP):


SQP : max

x∈∆

- 1

![image 22](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile22.png>)

- 2x⊺Hx + f⊺x (13)


where ∆ = x ∈ Rn : ni=1 xi = 1, x ≥ 0 , is the standard simplex. The SQP problem is fundamental in optimization and arises in many applications (see, e.g., Bomze 1998). Next, we show that in this case,

the Hoﬀman bound HA,b introduced in Deﬁnition 1 can be computed in closed-form for suitable choices of the norm · α on Rn and the norm · β on Rm.

- Proposition 1. Consider the norm  · α =  ·  1 on Rn and the norm  ·  β =  ·  1 on Rm. Let A = e⊺ and b = 1. Then HA,b = 2.


Proof. Proof. Let y ∈ Rn such that e⊺y = 1 be given. Let I = {i ∈ {1, . . . , n} : yi ≥ 0} and Ic = {1, . . . , n} \ I, and consider the case Ic = ∅ (otherwise, the statement follows by letting x = y in

Deﬁnition 1). Note that e⊺y = 1 implies I = ∅ and that i∈I yi = 1 − i∈Ic yi = 1 + y− 1. Let x ∈ Rn be deﬁned by setting xi = 0 for all i ∈ Ic, and xi = 1+ y1−

yi for all i ∈ I. Clearly, x ∈ ∆. Furthermore, for any i ∈ Ic, |xi − yi| = −yi. Also for any i ∈ I, we have |xi − yi| = y

![image 23](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile23.png>)

1

−

1+ y− 1 yi. Thus, x − y 1 = − i∈Ic yi + y

1

![image 24](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile24.png>)

1+ y− 1 i∈I yi = 2 y− 1. That is, HA,b ≤ 2. To show HA,b ≥ 2, consider y = (n, −1, . . . , −1). For any x ∈ ∆, it follows that x − y 1 = |x1 − n| + ni=2 |xi + 1| = 2n − 1 − x1 + ni=2 xi = 2(n − x1) ≥ 2(n − 1) = 2 y− 1.

−

1

![image 25](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile25.png>)

![image 26](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile26.png>)

![image 27](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile27.png>)

![image 28](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile28.png>)

![image 29](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile29.png>)

Thus, (13) can be reformulated as IQP by letting:

U = e and V > Me, (14) with

M = 2n ( H ∞,∞ + f ∞) , (15) where we have used that

κ = max{ Hx ∞ : e⊺x = 1, x ∈ Rn+} ≤ max

|Hij| =: H ∞,∞.

i,j∈{1,...,n}

- Remark 1. It is worth mentioning that a proof similar to the one given in Proposition 1 shows that


if · 1 is replaced with · ∞ in Proposition 1, the corresponding Hoﬀman constant would be equal to n − 1. However, this leads to a weaker bound V than the one given in (14).

- 2.3.2 Quadratic Programming with Box Constraints. Now, consider the box-constrained QP (BoxQP)

BoxQP : max 21x⊺Hx + f⊺x s. t. l ≤ x ≤ u,

![image 30](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile30.png>)

(16)

where l, u ∈ Rn are given bounds on the primal variables of BoxQP satisfying (w.l.o.g.) l < u (componentwise). Problem BoxQP is equivalent to the following QP problem:

max 12x⊺Hx + (Hl + f)⊺x s. t. x + s = u − l

![image 31](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile31.png>)

x ≥ 0, s ≥ 0.

(17)

Next, we show that in this case, the Hoﬀman bound HA,b introduced in Deﬁnition 1 can be computed in closed-form for a suitable choice of the norm · α on Rn and the norm · β on Rm.

- Proposition 2. Consider the norm · α = · ∞ on Rn and the norm · β = · ∞ on Rm. Let I denote the identity matrix in Rn×n, b ∈ Rn+, and A = [I, I]. Then HA,b = 1.

Proof. Proof. Let (y, z) ∈ R2n such that y + z = b be given. Deﬁne x = y+ − z− and s = z+ − y−. We claim (x, s) ∈ F = {(x, s) ∈ R2+n : x + s = b}. To show this notice ﬁrst that x + s = y+ − z− + z+ − y− = y + z = b. Now let i ∈ {1, . . . , n}. If zi− = 0 then xi = yi+ ≥ 0. Thus assume zi− > 0. Then zi+ = 0 and xi = bi − si = bi + yi− ≥ 0. Thus x ≥ 0. Similarly s ≥ 0. To ﬁnish, notice that (y, z) − (x, s) ∞ = (−y− + z−, −z− + y−) ∞ = (y−, z−) ∞ = (y, z)− ∞. This shows that HA,b ≤ 1. To show HA,b ≥ 1, let y = −e and z = b + e. For any (x, s) ∈ F, it follows that

(x,s) − (y,z) ∞ ≥ |x1 + 1| ≥ 1 = (y, z)− ∞. Using Proposition 2, we obtain that (17) can be reformulated as IQP by letting:

![image 32](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile32.png>)

![image 33](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile33.png>)

![image 34](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile34.png>)

![image 35](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile35.png>)

U =

u − l u − l

and V > Me, (18)

with

M = min(n H ∞,∞ u − l 1, H 1,1 u − l ∞) + f + Hl 1, (19) where we have used that

κ = max{ Hx 1 : x + s = u − l, x,s ∈ Rn+} ≤ min(n H ∞,∞ u − l 1, H 1,1 u − l ∞), where H 1,1 := i =j∈{1,...,n} |Hij|.

2.3.3 General Quadratic Programming.

Note that to compute an appropriate M value in Theorem 1, it is enough to let M > (κ + f ∗α)HA e β for some constant HA ≥ HA,b. As shown bellow, HA can be computed in general using Gu¨ler et al. (1995, Theorem 3.2).

![image 36](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile36.png>)

![image 37](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile37.png>)

![image 38](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile38.png>)

- Proposition 3. Fix the norm · α on Rn and the norm · β on Rm. Let A ∈ Rm×n and b ∈ Rm be such that the set F := {x ∈ Rn+ : Ax = b} = ∅. Also, let




σ¯(A) = (µ+, µ−, λ) ∈ Rm+n : A⊺(µ+ − µ−) − λ ∗α ≤ 1, µ+, µ− ∈ Rm+, λ ∈ Rn+ , and

HA = max{ (µ+, µ−, λ) ∗β : (µ+, µ−, λ) is an extreme point of σ¯(A)}. (20) Then, HA ≥ HA,b. Proof. Proof. First notice that for all y ∈ Rn,

![image 39](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile39.png>)

![image 40](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile40.png>)

x − y α = min{ x − y α : A′x ≤ b′, x ∈ Rn} where

min

x∈F

  .

  , b′ =

 

 

b −b 0

A −A −I

A′ =

Thus, it follows from Gu¨ler et al. (1995, Theorem 3.2) that

(Ay − b)+ (Ay − b)− y−

 

 

![image 41](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile41.png>)

x − y α ≤ HA

min

, (21)

x∈F

β

after identifying HA = Kαβ(A′), σ¯α(A) = σα(A′) (see, Gu¨ler et al. 1995, Theorem 3.2). From (21), it follows that for any y ∈ Rn such that Ay = b, then

![image 42](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile42.png>)

 

 

0 0 y−

= HA y− β . (22)

![image 43](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile43.png>)

![image 44](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile44.png>)

x − y α ≤ HA

min

x∈F

β

![image 45](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile45.png>)

Also, from (22), HA ≥ HA,b follows from Deﬁnition 1, as HA,b is the smallest constant satisfying (22). In order to use Proposition 3 to reformulate QP (1) as IQP (6), one can ﬁrst, similar to Chen and Burer

![image 46](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile46.png>)

![image 47](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile47.png>)

![image 48](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile48.png>)

![image 49](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile49.png>)

(2012), normalize the primal variables of QP to be between 0 and 1. Namely, under the boundedness assumption considered here, on has that QP is equivalent to:

min 12x⊺Hx˜ + f˜⊺x s. t. Ax˜ = b

![image 50](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile50.png>)

x ≥ 0,

where A˜ij := AijUiUj, f˜i := fiUi, and A˜ij := AijUj for all i, j ∈ {1, . . . , n}, and U ∈ Rn+ is given by (7). Now, using Proposition 3, and choosing the norm · α = · ∞ on Rn and the norm · β = · ∞ on Rm, we obtain that QP (1) can be reformulated as IQP (6) by letting H = H˜, f = f˜, A = A˜,

U = e, and V > Me, with

M = H ˜ 1,1 + f ˜ 1 HA, (23) where we have used that κ = max{ Hx˜ 1 : x ≤ e, x ∈ Rn+} ≤ H ˜ 1,1.

![image 51](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile51.png>)

In the case that one chooses the norm · α = · 1 on Rn and the norm · β = · 1 on Rm, then M = n(n H ˜ ∞,∞ + f ˜ ∞)HA. However, empirical results on test instances shows that this latter M is weaker than the bound obtained using (23).

![image 52](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile52.png>)

![image 53](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile53.png>)

Obtaining an eﬃcient way to compute the constant HA in (20) is however still an open question (see, e.g., Zheng and Ng 2004, Gu¨ler et al. 1995, Pen˜a et al. 2017). For illustrative purposes, in Section 2.3.4, we show the results of using an algorithm recently proposed in Pen˜a et al. (2017) to compute HA, and the corresponding bound M in (23).

![image 54](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile54.png>)

An alternative and eﬃcient way to compute bounds on the dual variables of a general instance of QP, is to use the bounds on the dual variables proposed by Chen and Burer (2012, Proposition 3.1) which are valid for QP instances having a strictly non-negative feasible solution (i.e., a feasible solution satisfying x > 0), and can be computed by solving a LP (cf., Chen and Burer 2012, eq. (19)). Speciﬁcally, notice that after obtaining the primal bounds U ∈ Rn using (7), problem QP is equivalent to

min 12x⊺Hx + f⊺x s. t. Ax = b

![image 55](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile55.png>)

0 ≤ x ≤ U.

(24)

Following the notation used thus far and letting ρ ∈ Rn be the dual variables associated with the upper bound constraints on the variables x ∈ Rn in (24), it follows from the KKT conditions of (24) that any of its optimal solutions must satisfy:

Hx + f + A⊺µ − λ + ρ = 0 (25a) x⊺λ = 0, (U − x)⊺ρ = 0 (25b)

Ax = b (25c) x ≥ 0, λ ≥ 0, ρ ≥ 0.

Also, after multiplying (25a) by a feasible solution x ∈ Rn of (24) and using (25b), (25c), it follows that any optimal solution of (24) also satisﬁes:

x⊺Hx + f⊺x + b⊺µ + U⊺ρ = 0.

Then, if QP has a feasible solution x ∈ Rn satisfying xi > 0, i = 1, . . . , m, it follows from Chen and Burer (2012, Proposition 3.1) that bounds on the dual variables V ∈ Rn required for the MILP reformulation IQP of QP can be computed by solving the following LP:

 

 

Hx + f + A⊺µ − λ + ρ = 0 H • X + f⊺x + b⊺µ + U⊺ρ = 0 0 ≤ Xij ≤ UiUj, i, j = 1, . . . , n 0 ≤ x ≤ U, λ ≥ 0, ρ ≥ 0, X ∈ Sn

, (26)

λj :

Vj = max





where H • X indicates the trace of the matrix HX, the matrix X ∈ Sn represents the linearization of the matrix xx⊺ ∈ Sn, and Sn is the set of n × n real symmetric matrices.

- Remark 2. In Chen and Burer (2012), eq. (18) is used to reﬁne the dual variable bounds after scaling the problem so that its variables are between zero and one. However, this reﬁnement of the bounds is not necessary to obtain their result in Proposition 3.1. The reﬁned version of these bounds is however the one implemented in quadprogIP, the implementation of our solution approach for general instances of QP.
- Remark 3. From Theorem 1, the constraint e⊺λ ≤ M could be added in the IQP formulation of QP (6). Adding this constraint however has not led to improved solution times of IQP. Thus, this constraint is not used in the implementation of our proposed solution approach for QP.


- 2.3.4 Bound comparison


In light of the bounds on the dual variables discussed here and the dual bounds proposed by Chen and Burer (2012, eq. (19)), it is natural to compare their values and computing times for diﬀerent instances of QP. Before doing so, however, it is important to emphasize that the dual bounds proposed here can be imposed on QP, even if the dual feasible set of QP is unbounded.

- Example 2 (Example 1 revisited). Recall the problem discussed in Example 1, and consider the norm · α = · ∞ on Rn and the norm · β = · ∞ on Rm. It is not diﬃcult to see that in this case


HA,b ≤ 1, and κ = 1. Since f 1 = 9, and e ∞ = 1, it follows that M = (κ + f 1)HA,b ≤ 10. Thus, for this problem we can bound the dual variables with the constraint

[λ1, λ2, λ3]⊺ ≤ 11[1, 1, 1]⊺. (27) In fact, notice that the following optimal solution of the problem

  µ∗ =

 

 ,

 

- 0
- 1 0


0 0 0

0 −3

x∗ =

λ∗ =

satisﬁes the dual bounds (27). On the other hand, from Example 1, it follows that max{λ1 : (x, µ, λ) ∈ ΛKKT } = ∞. Thus, dual bounds for this problem cannot be computed using Chen and Burer (2012, eq. (19)). In Table 1, we compare the bounds obtained in Section 2.3.1 with the bounds obtained using Chen and Burer

(2012, eq. (19)) for a number of randomly selected SQP instances. From Table 1, it is clear that the bounds obtained using Theorem 1, and speciﬁcally, eq. (15) are tighter than the ones obtained using Chen and Burer (2012, eq. (19)) (and labeled “RLT bounds” in Table 1 for the reformulation linearization techniques (RLT) used to derive them) on a random sample of SPQ instances. In fact, this is the case for all the SQP instances considered in Section 3.

Similarly, in Table 2, we compare the bounds obtained in Section 2.3.2 with the bounds obtained using Chen and Burer (2012, eq. (19)) for a number of randomly selected SQP instances. From Table 2, it is clear that the bounds obtained using Theorem 1, and speciﬁcally, eq. (19) are tighter than the ones obtained using Chen and Burer (2012, eq. (19)) on a random sample of BoxPQ instances. In fact, this is the case for all the BoxQP instances considered in Section 3. Both in Table 1 and Table 2 the time diﬀerences are a result of the bounds resulting from Theorem 1 being computed from the closed-form formulas (15), (19), while the RLP bounds are obtained by solving a linear program (Chen and Burer 2012, eq. (19)).

![image 56](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile56.png>)

Thm. 1 bound RLT bound SQP Instance Value Time (s) Value Time (s)

![image 57](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile57.png>)

![image 58](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile58.png>)

![image 59](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile59.png>)

spar030-060-1.mat: 5,520 0.0000 10,628 0.4952 spar030-070-3.mat: 5,880 0.0000 16,448 0.4694 spar050-040-1.mat: 9,200 0.0000 18,925 1.4016 spar050-050-3.mat: 9,800 0.0000 29,719 1.8674 spar060-020-1.mat: 11,040 0.0000 13,255 1.8344 spar070-075-1.mat: 13,440 0.0000 90,316 17.0129

- spar080-025-2.mat: 15,680 0.0001 31,792 13.8083
- spar080-025-3.mat: 15,040 0.0001 38,115 13.8468


- spar090-025-2.mat: 17,640 0.0001 44,646 22.8278
- spar090-025-3.mat: 16,920 0.0001 49,459 23.3063 spar090-050-3.mat: 17,460 0.0001 95,726 37.7146 spar090-075-1.mat: 17,280 0.0001 148,416 49.4807


- spar100-050-2.mat: 19,600 0.0001 115,192 67.8767
- spar100-050-3.mat: 19,400 0.0001 119,634 67.6607


![image 60](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile60.png>)

- Table 1: Comparison of bounds on e⊺λ obtained using (15) ( “Thm. 1 bound” columns) vs. using Chen and Burer (2012, eq. (19)) (“RLT bound” columns), together with corresponding computation times for a random sample of SQP instances.

![image 61](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile61.png>)

Thm. 1 bound RLT bound BoxQP Instance Value Time (s) Value Time (s)

![image 62](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile62.png>)

![image 63](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile63.png>)

![image 64](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile64.png>)

spar020-100-3.mat: 9,708 0.0001 73,497 0.2955 spar030-060-1.mat: 13,097 0.0001 152,505 0.5289

- spar030-070-1.mat: 14,887 0.0002 172,151 0.5001
- spar030-070-2.mat: 15,909 0.0001 176,093 0.5362
- spar030-070-3.mat: 16,827 0.0001 184,397 0.4815


- spar030-080-1.mat: 18,259 0.0001 219,338 0.4578
- spar030-080-2.mat: 18,532 0.0001 205,091 0.4539
- spar030-080-3.mat: 18,585 0.0001 202,502 0.5233 spar040-060-3.mat: 25,889 0.0001 388,914 0.7893 spar040-080-1.mat: 31,929 0.0001 524,796 0.9596 spar040-090-2.mat: 37,109 0.0001 589,155 1.1884 spar070-025-1.mat: 30,162 0.0182 819,461 7.1339


![image 65](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile65.png>)

- Table 2: Comparison of bounds on e⊺λ obtained using (19) (“Thm. 1 bound” columns) vs. using Chen and Burer (2012, eq. (19)) (“RLT bound” columns), together with corresponding computation times for a random sample of BoxQP instances.


In Table 3, we compare the bounds obtained in Section 2.3.3 with the bounds obtained using Chen and Burer

(2012, eq. (19)) for a number of randomly selected general QP instances. From Table 3, it is clear that the bounds obtained using Theorem 1, and speciﬁcally, eq. (23) are weaker than the ones obtained using Chen and Burer (2012, eq. (19)) on a random sample of general QP instances. In fact, this is the case for all the general QP instances considered in Section 3. In Table 3 the time diﬀerences are a result of the bounds resulting from Theorem 1 being computed using an algorithm whose complexity is exponential on the size of the constraint matrix of the problem (Pen˜a et al. 2017), while the RLP bounds are obtained by solving a linear program (Chen and Burer 2012, eq. (19)).

From the results in Table 1, Table 2, and Table 3, it is clear that using the bound of Theorem 1 can lead to tighter bounds on the QP dual variables λ ∈ Rn+ than the ones obtained using Chen and Burer (2012, eq. (19)) when a tight bound on the Hoﬀman constant HA,b used in Theorem 1 can be computed eﬃciently.

As illustrated in Example 2, the dual QP bounds obtained from Theorem 1 can be used even if the dual feasible set of QP is unbounded. In such case, it is not possible to use the quadprogBB solution

![image 66](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile66.png>)

Thm. 1 bound RLT bound

![image 67](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile67.png>)

![image 68](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile68.png>)

General QP Instance Value Time (s) Value Time (s) st e26.mat 49,200 0.0575 8,828 0.0742

![image 69](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile69.png>)

![image 70](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile70.png>)

- st fp4.mat 830,297 1.6961 594 0.1380

![image 71](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile71.png>)

- st fp5.mat 47,263,557 125.8385 792 0.2807 st glmp kky.mat 83,410 22.4100 339 0.1013 st glmp ss1.mat 33,757 6.5787 429 0.1067 st m1.mat 556,912,094 0.0655 19,060,333 0.3594 st pan2.mat 6,017 0.0544 1,494 0.0939 st jcbpaf2.mat: - - 96,969 0.2757 st ph10.mat 1,320 0.5757 27 0.0679 st ph2.mat 69,951 0.0601 8,043 0.1132 st qpc m0.mat 372 0.0573 35 0.0501 qp20 10 2 1.mat 69,846 0.0671 2,500 0.5206


![image 72](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile72.png>)

![image 73](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile73.png>)

![image 74](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile74.png>)

![image 75](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile75.png>)

![image 76](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile76.png>)

![image 77](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile77.png>)

![image 78](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile78.png>)

![image 79](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile79.png>)

![image 80](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile80.png>)

![image 81](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile81.png>)

![image 82](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile82.png>)

![image 83](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile83.png>)

![image 84](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile84.png>)

![image 85](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile85.png>)

![image 86](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile86.png>)

- qp30 15 1 4.mat 44,451 0.0621 1,661 0.7943

![image 87](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile87.png>)

![image 88](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile88.png>)

![image 89](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile89.png>)

- qp30 15 2 4.mat 41,625 0.0602 1,122 0.9512 qp40 20 1 4.mat 85,008 0.0548 8,700 1.3852 qp40 20 4 1.mat 523,052 0.0606 16,371 3.3573 qp50 25 1 2.mat 149,684 0.0668 12,476 2.4781 qp50 25 1 4.mat 169,868 0.0676 17,623 2.1617


![image 90](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile90.png>)

![image 91](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile91.png>)

![image 92](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile92.png>)

![image 93](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile93.png>)

![image 94](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile94.png>)

![image 95](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile95.png>)

![image 96](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile96.png>)

![image 97](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile97.png>)

![image 98](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile98.png>)

![image 99](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile99.png>)

![image 100](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile100.png>)

![image 101](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile101.png>)

![image 102](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile102.png>)

![image 103](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile103.png>)

![image 104](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile104.png>)

![image 105](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile105.png>)

- Table 3: Comparison of bounds on e⊺λ obtained using (23) (“Thm. 1 bound” columns) vs. using Chen and Burer (2012, eq. (19)) (“RLT bound” columns), together with corresponding computation times for a random sample of (general) QP instances. Dash “-” indicates that the time limit of 1800 sec has been reached without computing the bound.


methodology proposed by Chen and Burer (2012) to solve the problem, as the methodology requires (through a condition on the primal QP problem) the dual feasible set of QP to be bounded. To illustrate this (see Table 4), we modify some general QP test instances in a simple way to make their dual feasible set unbounded. The modiﬁcation we use is to pick the ﬁrst variable x1 of the instance and add the constraint x1 = x∗1, where x∗1 is the value of x1 in an optimal solution of the problem (i.e., this results in a problem that likely violates the interior condition required by Chen and Burer (see, 2012, preceding Prop. 3.1)). As shown in Table 4, these modiﬁed instances can be correctly solved using the approach proposed here with the bounds (23), while quadprogBB of Chen and Burer (2012) is unable to solve them due to the unboundedness of some of the dual variables of the modiﬁed version of the problem. Speciﬁcally, Table 4 provides the name of the original instance (1st column), its optimal value (2nd column), the constraint that is added to the problem to make its dual feasible set unbounded while leaving its optimal value unchanged (3rd column), the value of the M bound (23) computed as a bound for the dual variables while still retaining at least an optimal solution (4th column), the optimal solution for the modiﬁed version of the instance obtained with quadprogIP (5th column), and the number of the dual variable of the modiﬁed version of the instance that quadprogBB detects to be unbounded which results in quadprogBB not being able to solve the modiﬁed version of the problem.

# 3 Computational results

In this section, we provide a detailed description of the implementation of the solution approach for QP problems described in the previous sections. Also, we illustrate the performance of the solution approach by presenting the results of numerical experiments on a diverse set of QP test problems.

3.1 Problem instances

To test the performance of the proposed solution approach for QP, we use the set of BoxQP (16), Globallib (http://www.gamsworld.org/global/Globallib.htm), CUTEr (Gould et al. 2003), and RandQP test problems used in (Chen and Burer 2012, Section 4.2 and Table 1). In addition to these test problems, we consider the following QP test instances:

![image 106](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile106.png>)

quadprogIP quadprogBB Original Fixed M bound Modiﬁed instance detected

QP instance Optimal Value Variable (23) Optimal Value unbounded dual

![image 107](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile107.png>)

- qp20 10 1 1.mat -13.189 x1=0.4660 2.07E+04 -13.189 43-th

![image 108](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile108.png>)

![image 109](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile109.png>)

![image 110](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile110.png>)

- qp20 10 1 2.mat 11.6662 x1=1.0000 1.89E+04 11.6662 66-th


![image 111](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile111.png>)

![image 112](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile112.png>)

![image 113](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile113.png>)

- qp20 10 1 4.mat -18.3137 x1=0.0000 1.29E+04 -18.3137 45-th

![image 114](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile114.png>)

![image 115](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile115.png>)

![image 116](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile116.png>)

- qp20 10 2 1.mat -3.2442 x1=0.0000 6.98E+04 -3.2442 45-th

![image 117](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile117.png>)

![image 118](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile118.png>)

![image 119](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile119.png>)

- qp20 10 2 2.mat 8.5919 x1=0.0000 1.27E+04 8.5919 45-th

![image 120](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile120.png>)

![image 121](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile121.png>)

![image 122](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile122.png>)

- qp20 10 2 4.mat 6.5794 x1=0.0000 9.54E+03 6.5794 45-th

![image 123](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile123.png>)

![image 124](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile124.png>)

![image 125](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile125.png>)

- qp20 10 3 1.mat -30.179 x1=0.0000 7.10E+04 -30.179 45-th


![image 126](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile126.png>)

![image 127](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile127.png>)

![image 128](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile128.png>)

- qp20 10 3 2.mat -15.0508 x1=0.0000 4.70E+04 -15.0508 45-th


![image 129](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile129.png>)

![image 130](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile130.png>)

![image 131](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile131.png>)

- qp20 10 3 4.mat -12.665 x1=0.0000 1.49E+04 -12.665 45-th


![image 132](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile132.png>)

![image 133](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile133.png>)

![image 134](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile134.png>)

- qp30 15 1 1.mat 32.9577 x1=0.0000 1.96E+05 32.9577 67-th

![image 135](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile135.png>)

![image 136](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile136.png>)

![image 137](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile137.png>)

- qp30 15 1 3.mat 0.525 x1=0.0000 3.91E+04 0.525 67-th

![image 138](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile138.png>)

![image 139](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile139.png>)

![image 140](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile140.png>)

- qp30 15 1 4.mat 9.2296 x1=0.0000 4.45E+04 9.2296 67-th


![image 141](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile141.png>)

![image 142](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile142.png>)

![image 143](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile143.png>)

- qp30 15 2 3.mat -2.0693 x1=1.0000 3.18E+04 -2.0693 98-th qp30 15 2 4.mat 1.2862 x1=0.0000 4.16E+04 1.2862 67-th qp40 20 1 3.mat -2.7293 x1=0.0000 8.30E+04 -2.7293 89-th


![image 144](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile144.png>)

![image 145](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile145.png>)

![image 146](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile146.png>)

![image 147](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile147.png>)

![image 148](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile148.png>)

![image 149](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile149.png>)

![image 150](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile150.png>)

![image 151](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile151.png>)

![image 152](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile152.png>)

- qp50 25 1 4.mat 13.8442 x1=0.0000 1.70E+05 13.8442 111-th

![image 153](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile153.png>)

![image 154](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile154.png>)

![image 155](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile155.png>)

- qp50 25 2 4.mat -6.8577 x1=0.0000 2.80E+05 -6.8577 111-th

![image 156](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile156.png>)

![image 157](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile157.png>)

![image 158](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile158.png>)

- qp50 25 3 2.mat 35.9871 x1=0.0000 2.15E+05 35.9871 111-th


![image 159](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile159.png>)

![image 160](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile160.png>)

![image 161](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile161.png>)

![image 162](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile162.png>)

- Table 4: Solution of QP test instances modiﬁed to have an unbounded dual feasible set using quadprogIP.


- • SQP. Standard quadratic programming instances (13) are created by replacing the constraints of each of the BoxQPs considered in (Chen and Burer 2012, Section 4.2 and Table 1) by the constraint that the decision variables belong to the standard simplex of appropriate dimension.
- • SQP30, SQP50 (see, http://or.dei.unibo.it/library/msc). A set of 300 SQP instances used for test purposes in Bonami et al. (2016b).
- • StableQP. These instances are particular SQPs resulting from the problem of computing the stability number of a graph (see, e.g., Motzkin and Straus 1965). We use instances of this type arising from a class of graphs that have been used for testing purposes in the literature (see, e.g., Dobre and Vera 2015, Section 4.2.2). A more detailed description of these instances is presented in Section 3.1.1.
- • Scozzari/Tardella (see, http://or.dei.unibo.it/library/msc). A set of 14 SQP instances used for test purposes in Scozzari and Tardella (2008), Bonami et al. (2016b).
- • QPLIB2014 (see, http://www.lamsade.dauphine.fr/QPlib2014/doku.php). Nine nonconvex quadratic instances are selected from this test set. Four of the instances which are SQP instances are added to the SQP test set, and the other ﬁve instances are BoxQP instances, which are added to the BoxQP test set.


Similar to Chen and Burer (2012), Table 5 provides a summary of the basic information of all the test instances. In Table 5, n denotes the range of the number of decision variables required to formulate the corresponding problem instance using mineq inequality constraints, and meq equality constraints. Also, density denotes the corresponding density range for the matrix deﬁning the quadratic problem’s objective.

3.1.1 StableQP instances

For any graph G, the inverse of α(G), the stability number of G, can be computed by solving the following SQP (see, e.g., Motzkin and Straus 1965).

1 α(G)

x⊺(A + I)x, (28)

= min

![image 163](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile163.png>)

x∈∆

where A ∈ Sn is the adjacency matrix of the undirected graph G(V, E) with number of vertices V = n, and set of edges E ∈ V × V . Also I is the identity matrix of appropriate dimensions.

![image 164](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile164.png>)

Type # Instances n mineq + meq density StableQP 8 [5, 26] [0,1] [0.30, 0.60] SQP 90 [20, 100] [0, 90] [0.19, 0.99] BoxQP 90 [20, 100] [0, 0] [0.19, 0.99] Globallib 83 [2, 100] [1,52] [0.01, 1] CUTEr 6 [4, 12] [0, 13] [0.08, 1] RandQP 64 [20, 50] [14, 35] [0.23, 1] SQP30 150 [30, 30] [0,1] [1, 1] SQP50 150 [50, 50] [0,1] [1, 1] Scozzari/Tardella 14 [30, 1000] [0,1] [0.25, 1]

![image 165](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile165.png>)

![image 166](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile166.png>)

- Table 5: Statistics of the test QP instances.


The StableQP instances are obtained by solving (28) for a class of graphs Gk, k = 1, . . . introduced in Dobre and Vera (2015) that have proven to be hard instances for approximation methods for α(G) proposed in Bomze et al. (2010), Bundfuss and Du¨r (2009), Dong and Anstreicher (2013), Dobre and Vera (2015).

- 3.2 Implementation details

The solution approach for QP proposed here is implemented as follows. First, explicit upper and lower bounds for the instance’s decision variables are obtained. Then, the problem instance is reformulated as QP by linearly shifting its decision variables, and adding slack variables to the problem as necessary (e.g., (17)). The upper bounds on the added slack variables are computed using (7) to obtain the primal variable upper bounds U ∈ Rn. Upper bounds V ∈ Rn on the dual variable are calculated using the methods described in Section 2.3 (see (14), (18) and (26)). Finally, CPLEX 12.5.1 (cf., http://www-eio.upc.edu/lceio/manuals/CPLEX-11/html/) is used to solve IQP. The following parameter settings are used for CPLEX MILP solver:

- • Max time: This is the user speciﬁed maximum running time of the algorithm and is set to 104 seconds. Any problem taking longer than this value to be solved will be deemed as “out of time”.

![image 167](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile167.png>)

- • Tol: The solver will stop when |bestnode − bestinteger|

![image 168](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile168.png>)

1−10 + |bestinteger|

≤ 10−6.

For the interested reader, the deﬁnition of the parameters bestnode and bestinteger can be found in CPLEX (2010). Here, it suﬃces to say that this criteria is consistent with quadprogBB stopping criteria (cf., Chen and Burer 2012), which is

Greatest upper bound − current lower bound max{1, |Greatest upper bound|}

![image 169](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile169.png>)

≤ 10−6.

- • Other parameters of the CPLEX MILP solver such as TolXInteger, Max iter, BranchStrategy, Nodeselect, are set to their default values.


![image 170](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile170.png>)

We refer to the procedure described in this section to solve QP as quadprogIP, which is coded using Matlab R2014a, and is publicly available at https://github.com/xiawei918/quadprogIP.

- 3.3 Numerical performance


In order to test the performance of the quadprogIP methodology proposed in Section 3.2, the QP test instances discussed in Section 3.1 are solved using quadprogIP, the quadprogBB solver introduced by Chen and Burer (2012), the NLP solver BARON 17.8.9 of Sahinidis (1996), and the CPLEX 12.7.0.0 QP solver. All tests are done using Matlab R2014b (8.4.0.150421), together with CPLEX 12.7.0.0., on a AMD Opteron 2.0 GHz machine with 32GB memory and 16 cores (each core is a 2.0 GHz. 64 bit architecture), from the COR@L laboratory (cf., http://coral.ise.lehigh.edu/).

Similar to Chen and Burer (2012), to compare the performance between quadprogIP and quadprogBB, quadprogIP and BARON, and quadprogIP and CPLEX, we plot the solution time it takes to solve a particular QP instance with two of the solvers as a square in a 2D plane, where the y-axis denotes either quadprogBB’s, BARON’s, or CPLEX’s solution time and the x-axis denotes quadprogIP ’s solution time. The dashed line in the plots indicates the y = x line in the plane, that represents equal colution solution times. Thus, a square that is above the diagonal line indicates an instance for which it takes the solver represented on y-axis more solution time to solve than quadprogIP. Furthermore, the size of the square illustrates the size (number of decision variables) of the instance. That is, smaller squares represent “smaller” size instances while bigger squares represent “bigger” size instances. In the ﬁgures below, only instances in which at least one of the methodologies solves the problem within the maximum time allowed are displayed.

3.3.1 Results on SQP instances.

The results for the SQP test instances are shown in Figure 1. Note that a diﬀerent scale is used in the axes of Figures 1a, 1b, and 1c.

- 100
- 101
- 102
- 103
- 104


- 100
- 101
- 102
- 103
- 104


| | | |
|---|---|---|
| | | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |
| | |


quadprogBB

BARON

| | | | |
|---|---|---|---|
| | | | |


| | | |
|---|---|---|
| | | |
| | | |


| |
|---|
| |


10−1 100 101 102 103 104 quadprogIP

10−1 100 101 102 103 104 quadprogIP

(a) quadprogIP vs quadprogBB.

(b) quadprogIP vs BARON.

- 100
- 101
- 102
- 103
- 104


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


| | |
|---|---|
| | |


- 0.8
- 1


ProblemsSolved

CPLEX

0.6

| |
|---|
| |
| |


quadprogIP quadprogBB CPLEX BARON

| | | |
|---|---|---|
| | | |
| | | |


| | | |
|---|---|---|
| | | |
| | | |
| | | |


0.4

0.2

10−1

0

10−1 100 101 102 103 104

100 101 102 103

quadprogIP

Performance Ratio

(c) quadprogIP vs CPLEX.

(d) Performance proﬁle for SQP instances.

- Figure 1: Solution time in seconds of SQP instances. Size of squares illustrates size of the instance. A square at the maximum value of an axis represents an instances for which the solver in that axis reached maximum running time without solving it.


Figure 1a shows that quadprogIP clearly outperforms quadprogBB by solving all SQP instances in a time that is one to two orders of magnitude faster than quadprogBB and specially in the larger instances.

Similarly, Figure 1b shows that quadprogIP clearly outperforms BARON by solving all SQP instances in a time that is one to two orders of magnitude faster than BARON, and specially in the larger instances. Although CPLEX solves two small-scale instances faster than quadprogIP, again, in general quadprogIP outperforms CPLEX by orders of magnitude in terms of solution time (see, Figure 1c). As Figures 1a, 1b, and 1c illustrate, the performance of quadprogIP against the other solvers improves as the SQP instance becomes larger. The performance proﬁle in Figure 1d summarizes the clear advantages of solving the very important class of SQP instances with the proposed quadprogIP solution approach.

3.3.2 Results on SQP30 and SQP50 instances.

As Figure 2 shows, the results on the SQP instances SQP30 and SQP50 from Bonami et al. (2016b) is very similar to the ones presented in Section 3.3.1. As with the set of SQP instances, only CPLEX is able to solve a few instances faster than quadprogIP; however, in general quadprogIP outperforms the other solvers by orders of magnitude in terms of solution time.

- 100
- 101
- 102
- 103
- 104


- 101
- 102
- 103
- 104


| |
|---|
| |
| |
| |
| |
| |
| |
| |


| | |
|---|---|
| | |
| | |
| | |
| | |


quadprogBB

BARON

| |
|---|
| |
| |


| | |
|---|---|


| |
|---|
| |


| | |
|---|---|
| | |
| | |


| |
|---|
| |
| |


| | | |
|---|---|---|
| | | |


| | | |
|---|---|---|
| | | |


| | | |
|---|---|---|


| | |
|---|---|


10−1

10−1 100 101 102 103 104 quadprogIP

10−1 100 101 102 103 104

quadprogIP

(a) quadprogIP vs quadprogBB.

(b) quadprogIP vs BARON.

- 100
- 101
- 102
- 103
- 104


| | | | | | | | |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |


- 0.8
- 1


| | | |
|---|---|---|
| | | |
| | | |
| | | |


| | |
|---|---|
| | |


ProblemsSolved

CPLEX

0.6

0.4

quadprogIP quadprogBB CPLEX BARON

10−1

0.2

10−2

0

10−1 100 101 102 103 104

100 101 102 103

quadprogIP

Performance Ratio

(c) quadprogIP vs CPLEX.

(d) Performance proﬁle for SQP30 and SQP50 instances.

- Figure 2: Solution time in seconds of SQP30 and SQP50 instances. Size of squares illustrates size of the instance. A square at the maximum value of an axis represents an instances for which the solver in that axis reached maximum running time without solving it.


3.3.3 Results on StableQP instances.

In line with the performance of quadprogIP on SQP, SQP30, and SQP50 instances, it is interesting to see in Table 6 that quadprogIP clearly outperforms quadprogBB, BARON, and CPLEX in the StableQP instances (see, Section 3.1). In fact, while quadprogIP solves each of the instances in less than a second, quadprogBB, and CPLEX are unable to solve the instances beyond k ≥ 4 within the maximum allowed solution time of 104 seconds, while BARON is unable to solve the instances beyond k ≥ 3 within the maximum allowed solution time.

![image 171](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile171.png>)

Solution Time (s.) k quadprogIP quadprogBB ⁀BARON ⁀CPLEX

![image 172](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile172.png>)

![image 173](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile173.png>)

- 1 0.34 3.67 8.93 0.39
- 2 0.25 6.28 2573.77 8.75
- 3 0.34 12.56 - 685.70
- 4 0.43 - - -
- 5 0.49 - - -
- 6 0.51 - - -
- 7 0.46 - - -
- 8 0.49 - - -


![image 174](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile174.png>)

- Table 6: Solution time in seconds for StableQP instances. Dash “-” indicates that the solver was unable to solve the instance within the maximum allowed time.

3.3.4 Results on Scozzari/Tardella instances.

The Scozzari/Tardella from Scozzari and Tardella (2008) are composed of much larger-scale instances of SQP than the ones considered so far. Table 7, as with the previously discussed groups of standard QP instances, clearly shows that quadprogIP is able to solve these instances faster than the other solvers, and is able to solve more large-scale instances than the other solvers.

![image 175](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile175.png>)

Solution Time (s.) Scozzari/Tardella instance quadprogIP quadprogBB ⁀BARON ⁀CPLEX

![image 176](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile176.png>)

![image 177](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile177.png>)

Problem 30x30 0.75.mps.mat: 0.51 5.27 39.32 5.56 Problem 50x50 0.75.mps.mat: 11.78 48.29 - 2,162.13 Problem 100x100 0-1.mps.mat: 1.54 1,412.16 223.54 154.71 Problem 100x100 0.5.mps.mat: 6.71 319.82 - Problem 100x100 0.75.mps.mat: 36.76 1,519.61 - Problem 200x200 0-1.mps.mat: 36.86 - - 9,995.67 Problem 200x200 0.5.mps.mat: 175.15 - - Problem 500x500 0-1.mps.mat: 240.09 - - Problem 500x500 0.25.mps.mat: 2,092.48 - - Problem 1000x1000 0.25.mps.mat: - - - Problem Q30.mps.mat: 0.54 4.27 - Problem Q50.mps.bar.mat: 2.45 8,476.70 - Problem Q100.mps.bar.mat: 4.71 - - Problem Q150.mps.mat: 20.89 - - -

![image 178](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile178.png>)

![image 179](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile179.png>)

![image 180](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile180.png>)

![image 181](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile181.png>)

![image 182](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile182.png>)

![image 183](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile183.png>)

![image 184](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile184.png>)

![image 185](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile185.png>)

![image 186](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile186.png>)

![image 187](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile187.png>)

![image 188](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile188.png>)

![image 189](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile189.png>)

![image 190](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile190.png>)

![image 191](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile191.png>)

![image 192](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile192.png>)

![image 193](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile193.png>)

![image 194](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile194.png>)

![image 195](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile195.png>)

![image 196](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile196.png>)

![image 197](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile197.png>)

![image 198](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile198.png>)

![image 199](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile199.png>)

![image 200](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile200.png>)

![image 201](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile201.png>)

![image 202](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile202.png>)

- Table 7: Solution time in seconds for Scozzari/Tardella instances. Dash “-” indicates that the solver was unable to solve the instance within the maximum allowed time.


3.3.5 Results on BoxQP instances.

In Figure 3, we compare the performance of quadprogIP on the BoxQP instances against the other three selected solvers. It is clear from Figure 3a that while quadprogIP outperforms quadprogBB in the smaller

BoxQP instances (ranging between 20–60 decision variables), quadprogBB outperforms quadprogIP for larger BoxQP instances (ranging between 60–100 decision variables), where quadprogIP is typically unable to solve the instance within the 104 maximum solution time.

- 100
- 101
- 102
- 103
- 104


- 100
- 101
- 102
- 103
- 104


quadprogBB

BARON

| | |
|---|---|
| | |


| |
|---|
| |
| |
| |


| | |
|---|---|
| | |
| | |


| | | |
|---|---|---|
| | | |
| | | |
| | | |


| |
|---|
| |


| |
|---|
| |
| |


| | | |
|---|---|---|
| | | |
| | | |
| | | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|


| |
|---|
| |


| | | |
|---|---|---|
| | | |


10−1

100 101 102 103 104 quadprogIP

100 101 102 103 104

quadprogIP

(a) quadprogIP vs quadprogBB.

(b) quadprogIP vs BARON.

- 100
- 101
- 102
- 103
- 104


| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


- 0.8
- 1


ProblemsSolved

CPLEX

0.6

| | |
|---|---|
| | |
| | |


| |
|---|
| |
| |


| | | |
|---|---|---|


| |
|---|
| |
| |
| |


0.4

| |
|---|
| |
| |


| | | |
|---|---|---|
| | | |
| | | |


| | |
|---|---|
| | |
| | |


quadprogIP quadprogBB CPLEX BARON

0.2

10−1

0

100 101 102 103 104

100 101 102 103

quadprogIP

Performance Ratio

(c) quadprogIP vs CPLEX.

(d) Performance proﬁle for BoxQP instances.

- Figure 3: Solution time in seconds of BoxQP instances. Size of squares illustrates size of the instance. A square at the maximum value of an axis represents an instances for which the solver in that axis reached maximum running time without solving it.


Figure 3b shows the performance of quadprogIP and BARON on the BoxQP test set. It is clear that BARON outperforms quadprogIP in most BoxQP instances. Although for instances with less than 40 decision variables the solution time of quadprogIP is not signiﬁcantly longer than that of BARON. Figure 3c shows that CPLEX performs much better than quadprogIP on all BoxQP instances. Figure 3d summarizes these results, where it is clear that CPLEX and BARON are the best solvers for these BoxQP instances.

It is worth mentioning that the performance of quadprogIP on BoxQP instances can be improved by adding appropriate valid constraints to the IQP (6) formulation of the BoxQP. This valid constraints can be derived from Hansen et al. (1993, Prop. 1). Speciﬁcally, notice that the IQP (6) corresponding to (17) can be written as:

- 1

![image 203](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile203.png>)

- 2 min (Hl + f)⊺x − (u − l)⊺µ


λx λs

H 0 0 0

f + Hl 0

x s

I I

µ −

s. t.

+

+

= 0 x + s = u − l

0 ≤ xi ≤ zix(ui − li) i = 1, . . . , n 0 ≤ si ≤ zis(ui − li) i = 1, . . . , n 0 ≤ λxi ≤ (1 − zix)Vi i = 1, . . . , n 0 ≤ λsi ≤ (1 − zis)Vi i = 1, . . . , n zix, zis ∈ {0, 1} i = 1, . . . , n.

(29)

Then, from Hansen et al. (1993, Prop. 1), and Proposition 4 below, it follows that the constraints zix + zis = 1, for all i ∈ {1, . . . , n} such that Hii < 0, (30)

are valid constraints for the optimal solutions of (29). When added to (29), the valid constraints (30) improve the solution time of the approach proposed here to globally solve BoxQP problems.

Proposition 4. Let (x, s, µ, λx, λs) ∈ Rn+ × Rn+ × R2n × Rn+ × Rn+ be a KKT point of (17). Then e⊺λx + e⊺λs ≤ M, where M is given by (18). That is, every KKT point of (17) satisﬁes the bounds given by (18).

Proof. Proof. Let (x,s, µ, λx, λs) satisfy the KKT conditions of (17). Then

H 0 0 0

x s

λx λs

f + Hl 0

I I

µ −

= 0 (31) x⊺λx = 0, s⊺λs = 0, x + s = U (32)

+

+

x ≥ 0, λx ≥ 0, λs ≥ 0.

where µ ∈ Rn, λx ∈ Rn+, λx ∈ Rn+ are respectively the dual multipliers for the x + s = u − l, x ≥ 0, and s ≥ 0 constraints in (17). Equation (31) implies that

λx − λs = Hx + f + Hl. (33) Thus, using (32), (33), and the results in Section 2.3.2

e⊺λx + e⊺λs = e⊺|λx − λs| = Hx + f + Hl 1 ≤ Hx 1 + f + Hl 1 ≤ M

![image 204](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile204.png>)

![image 205](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile205.png>)

![image 206](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile206.png>)

![image 207](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile207.png>)

Although the quadprogIP code does not include the strengthening constraints (30) for BoxQPs, the results illustrated on Figure 4 show how adding the valid constraints (30) improves the solution time on a set of spar BoxQP instances ranging on size between 20-40 variables with density between 30100. In particular, with the addition of these constraints, quadprogIP outperforms quadprogBB on these instances.

Results on CUTEr, Globallib, and RandQP instances.

In Figures 5, we compare the performance of quadprogIP on the CUTEr, Globallib, and RandQP instances against the other solvers. As Figure 5a illustrates, except for a few instances, quadprogIP has shorter solution times than quadprogBB on the more general CUTEr, Globallib, and RandQP instances of QP. Moreover, quadprogIP typically solves these problems about 10 times faster than quadprogBB. For these CUTEr, Globallib, and RandQP we ﬁnd nine (9) instances that are successfully solved by quadprogIP but not by quadprogBB within the maximum allowed solution time of 104 seconds.

As for BARON, it can be seen from Figures 5b that quadprogIP is faster on most of the CUTEr, Globallib, and RandQP instances, with quadprogIP being able to solve a fair number of instances that BARON is not able to solve within the maximum allowed time of 104 seconds. On the other hand, CPLEX is able to solve most of the CUTEr, Globallib, and RandQP instances faster than quadprogIP; however, still a number of instances are solved faster than CPLEX, and most instances are solved by quadprogIP in a time no larger than 10 times the solution time of CPLEX. Figure 5d summarizes these results.

| | | | | | | |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |
| | | | | | | |


- 0.8
- 1


ProblemsSolved

0.6

0.4

0.2

quadprogIP quadprogIP with extra constraint quadprogBB

0

100 101 102 103

Performance Ratio

- Figure 4: Performance proﬁle for spar BoxQP instances anging on size between 20-40 variables with density between 30-100. Extra constraints refer to adding constraints (30) in the quadprogIP solver.


# 4 Conclusion

In this paper, we present a new simple and eﬀective approach for the global solution of (non-convex) linearly constrained quadratic problems (QP) by combining the use of the problem’s necessary KKT conditions together with state-of-the-art integer programming solvers. This is done via a reformulation of the QP as a mixed-integer linear program (MILP). We show that in general, this MILP reformulation can be obtained for QPs with a bounded primal feasible set via fundamental results related to the solution of perturbed linear systems of equations (see, e.g., Gu¨ler et al. 1995). In practice, quadprogIP is shown to typically outperform by orders of magnitude quadprogBB, BARON, and CPLEX on standard QPs. For general QPs, quadprogIP outperforms quadprogBB, outperforms BARON in most instances, while CPLEX performs the best on these instances. For box-constrained QPs, quadprogIP has a comparable performance to quadprogBB and BARON in small- to medium-scale instances, but is outperformed by these solvers on large-scale instances, while CPLEX performs the best on box-constrained QP instances. Also, unlike quadprogBB, the solution approach proposed here is able to solve QP instances whose dual feasible set is unbounded. The performance of this methodology on standard QP problems allows for the potential use of this solution approach as a basis for the solution of copositive programs (cf., Du¨r 2010). Which is an interesting direction of future research work.

The proposed IP formulation of general QPs requires the computation of certain type of Hoﬀman bound (see, e.g., Hoﬀman 2003) on the system of linear equations deﬁning the problem’s feasible set. Thus, obtaining general and eﬀectively computable bounds of this type is an interesting open question.

We ﬁnish by mentioning that a basic implementation of the proposed solution approach referred as quadprogIP is publicly available at https://github.com/xiawei918/quadprogIP, together with pointers to the test instances used in the article for the numerical experiments, and the raw data of all the solution times used to construct the ﬁgures throughout the article in the PDF ﬁle raw data.pdf.

# Acknowledgments

The authors would like to thank two anonymous referees for the very thoughtful and thorough comments provided on an earlier version of this manuscript. The work of the ﬁrst and third author is supported by the NSF CMMI grant 1300193.

# References

Belotti, P. 2010. Couenne: a user’s manual. Tech. rep., Clemson University. Available at http://projects.coin-or.org/Couenne/browser/trunk/Couenne/doc/couenne-user-manual.pdf.

- 100
- 101
- 102
- 103
- 104


- 100
- 101
- 102
- 103
- 104


| | |
|---|---|


| |
|---|
| |
| |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


| | |
|---|---|
| | |


quadprogBB

| |
|---|
| |


| | |
|---|---|
| | |


| |
|---|
| |


BARON

| | |
|---|---|


| | |
|---|---|
| | |


| | |
|---|---|
| | |
| | |


| | | |
|---|---|---|


| | | |
|---|---|---|


| | |
|---|---|


| |
|---|
| |


| |
|---|
| |
| |


| |
|---|
| |
| |


| | | |
|---|---|---|


| |
|---|
| |


| | | | | |
|---|---|---|---|---|
| | | | | |


| |
|---|
| |
| |


| | |
|---|---|
| | |


| |
|---|
| |
| |


| | | |
|---|---|---|
| | | |


| | |
|---|---|
| | |


10−1

| |
|---|
| |
| |
| |
| |


| | |
|---|---|


| | |
|---|---|


| |
|---|
| |


10−2

10−1 100 101 102 103 104 quadprogIP

10−1 100 101 102 103 104

quadprogIP

(a) quadprogIP vs quadprogBB.

(b) quadprogIP vs BARON.

- 100
- 101
- 102
- 103
- 104


- 0.8
- 1


ProblemsSolved

0.6

CPLEX

| |
|---|
| |
| |


| | | | |
|---|---|---|---|
| | | | |
| | | | |


| | |
|---|---|
| | |
| | |


| | | | |
|---|---|---|---|
| | | | |


0.4

10−1

| |
|---|
| |


quadprogIP

| | | |
|---|---|---|


0.2

10−2

quadprogBB

cplexqp BARON

10−3

0

100 101 102 103

10−1 100 101 102 103 104

Performance Ratio

quadprogIP

(d) Performance proﬁle for CUTEr, Globallib, and RandQP instances.

(c) quadprogIP vs CPLEX.

- Figure 5: Solution time in seconds of CUTEr, Globallib, and RandQP instances. Size of squares illustrates size of the instance. A square at the maximum value of an axis represents an instances for which the solver in that axis reached maximum running time without solving it.


Belotti, P., J. Lee, L. Liberti, F. Margot, A. Wachter. 2009. Branching and bounds tightening techiques for non-convex MINLP. Optimization Methods and Software 24 597–634. Ben-Tal, A., A. Nemirovski. 2001. Lectures on Modern Convex Optimization: Analysis, Algorithms, and

Engineering Applications. MPS-SIAM Series on Optimization, SIAM, Philadelphia, PA. Bertsekas, D. 1999. Nonlinear Programming. Athena Scientiﬁc, Belmont, MA. Bomze, I. M. 1998. On standard quadratic optimization problems. Journal of Global Optimization 13

369–387. Bomze, I. M., F. Frommlet, M. Locatelli. 2010. Copositivity cuts for improving SDP bounds on the clique number. Mathematical Programming 124 13–32.

Bonami, P., A. Lodi, J. Schweiger, A. Tramontani. 2016a. Solving standard quadratic programming by cutting planes. Tech. Rep. DS4DM-2016-001, hola. Available at http://cerc-datascience.polymtl.ca/wp-content/uploads/2016/06/Technical-Report_DS4DM-2016-001-1.pdf.

Bonami, Pierre, Oktay Gu¨nlu¨k, Jeﬀ Linderoth. 2016b. Solving box-constrained nonconvex quadratic programs. Optimization Online .

Bundfuss, S., Du¨r. 2009. An adaptive linear approximation algorithm for copositive programs. SIAM Journal on Optimization 20 30–53. Burer, S. 2009. On the copositive representation of binary and continuous nonconvex quadratic programs. Mathematical Programming 120 479–495. Burer, S. 2010. Optimizing a polyhedral-semideﬁnite relaxation of completely positive programs. Mathematical Programming Computation 2 1–19.

Burer, S., D. Vandenbussche. 2009. Globally solving box-constrained non-convex quadratic programs with semideﬁnite-based ﬁnite branch-and-bound. Computational Optimization and Applications 43 181–195.

Chen, J., S. Burer. 2012. Globally solving nonconvex quadratic programming problems via completely positive programming. Mathematical Programming Computation 4 33–52. CPLEX, IBM ILOG. 2010. 12.2 user?s manual. ILOG. See ftp://ftp. software. ibm. com/software/websphere/ilog/docs/optimization/cplex/ps usrmancplex. pdf . Dobre, C., J. C. Vera. 2015. Exploiting symmetry in copositive programs via semideﬁnite hierarchies. Mathematical Programming 151 659–680. Dong, H. B., K. Anstreicher. 2013. Separating doubly nonnegative and completely positive matrices. Mathematical Programming 137 131–153.

![image 208](<2015-xia-globally-solving-nonconvex-quadratic_images/imageFile208.png>)

Du¨r, M. 2010. Copositive programming – a survey. M. Diehl, F. Glineur, E. Jarlebring, W. Michiels, eds., Recent Advances in Optimization and its Applications in Engineering. Springer, 3–20. Eustaquio, RODRIGO G, ELIZABETH W Karas, ADEMIR A Ribeiro. 2008. Constraint qualiﬁcations

for nonlinear programming. Federal University of Parana . Floudas, C. A., V. Visweswaran. 1990. A global optimization algorithm (GOP) for certain classes of nonconvex NLPs–I. Theory. Computers and Chemical Engineering 14 1397–1417. Gao, D. Y. 2004. Canonical duality theory and solutions to constrained nonconvex quadratic programming. Journal of Global Optimization 29 377–399.

Giannessi, F., E. Tomasin. 1973. Nonconvex quadratic programs, linear complementarity problems, and integer linear programs. Lecture Notes in Computer Science, vol. 3. Fifth Conference on Optimization Techniques, Springer, Berlin Heidelberg New York, 437–449.

Gould, N. I. M., D. Orban, P.L. Toint. 2003. CUTEr and SifDec: A constrained and unconstrained testing environment, revisited. ACM Transactions on Mathematical Software 29 373–394. Gu¨ler, O., A. J. Hoﬀman, U. G. Rothblum. 1995. Approximations to solutions to systems of linear inequalities. SIAM Journal on Matrix Analysis and Applications 16 688–696.

Hansen, Pierre, Brigitte Jaumard, Miche`le Ruiz, Junjie Xiong. 1993. Global minimization of indeﬁnite quadratic functions subject to box constraints. Naval Research Logistics (NRL) 40 373–392. Hoﬀman, Alan J. 2003. On approximate solutions of systems of linear inequalities. Selected Papers Of

Alan J Hoﬀman: With Commentary 174–176. Horst, R., P. M. Pardalos, N.V. Thoai. 2000. Introduction to Global Optimization. 2nd ed. Dortrecht: Kluwer. Hu, J., J. E. Mitchell, J. S. Pang, B. Yu. 2012. On linear programs with linear complementarity constraints. Journal of Global Optimization 53 29–51. Kim, S., M. Kojima. 2001. Second order cone programming relaxation of nonconvex quadratic optimization problems. Optimization Methods and Software 15 201–224. Kim, S., M. Kojima. 2003. Exact solutions of some nonconvex quadratic optimization problems via SDP and SOCP relaxations. Computational Optimization and Applications 26 143–154. Mangasarian, O. L. 1981. A condition number for linear inequalities and linear programs. Tech. Rep. 2231, MRC Technical Summary Report. Misener, Ruth, Christodoulos A Floudas. 2013. Glomiqo: Global mixed-integer quadratic optimizer. Journal of Global Optimization 57 3–50. Motzkin, T. S., E. G. Straus. 1965. Maxima for graphs and a new proof of a theorem of Tur´an. Canadian Journal of Mathematics 17 533–540. Nesterov, Y. 1998. Semideﬁnite relaxation and nonconvex quadratic optimization. Optimization Methods and Software 9 141–160.

Pardalos, P. M., S. A. Vavasis. 1991. Quadratic programming with one negative eigenvalue is NP-hard. Journal of Global Optimization 1 15–22. Pen˜a, Javier, Juan C. Vera, Luis F. Zuluaga. 2017. Hoﬀman bounds and norms of set-valued mappings. Tech. rep., Carnegie Mellon University. Renegar, J. 2001. A Mathematical View of Interior-Point Methods in Convex Optimization, MPS/SIAM Series on Optimization, vol. 3. SIAM. Sahinidis, N. V. 1996. BARON: a general purpose global optimization software package. Journal of Global Optimization 8 201–205. Scozzari, Andrea, Fabio Tardella. 2008. A clique algorithm for standard quadratic programming. Discrete Applied Mathematics 156 2439–2448. Sherali, H., W. Adams. 1994. A hierarchy of relaxations for mixed-integer zero-one programming problems. Discrete Applied Mathematics 52 83–106. Tawarmalani, M., N. V. Sahinidis. 2004. Global optimization of mixed-integer nonlinear programs: A theoretical and computational study. Mathematical Programming 99 563–591. Vanderbei, R. J., D. F. Shanno. 1999. An interior-point algorithm for nonconvex nonlinear programming. Computational Optimization and Applications 13 231–252. Zheng, X. Y., K. F. Ng. 2004. Hoﬀman’s least error bounds for systems of linear inequalities. Journal of Global Optimization 30 391–403.

