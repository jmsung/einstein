arXiv:1311.5240v1[math.OC]20Nov2013

![image 1](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile1.png>)

![image 2](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile2.png>)

![image 3](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile3.png>)

## Mathematical Programming manuscript No. (will be inserted by the editor)

![image 4](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile4.png>)

Jan Fiala · Michal Kocˇvara · Michael Stingl

# PENLAB: A MATLAB solver for nonlinear semideﬁnite optimization⋆

Received: date / Revised version: date

Abstract. PENLAB is an open source software package for nonlinear optimization, linear and nonlinear semideﬁnite optimization and any combination of these. It is written entirely in MATLAB. PENLAB is a young brother of our code PENNON [23] and of a new implementation from NAG [1]: it can solve the same classes of problems and uses the same algorithm. Unlike PENNON, PENLAB is open source and allows the user not only to solve problems but to modify various parts of the algorithm. As such, PENLAB is particularly suitable for teaching and research purposes and for testing new algorithmic ideas.

In this article, after a brief presentation of the underlying algorithm, we focus on practical use of the solver, both for general problem classes and for speciﬁc practical problems.

![image 5](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile5.png>)

## 1. Introduction

Many problems in various scientiﬁc disciplines, as well as many industrial problems lead to (or can be advantageously formulated) as nonlinear optimization problems with semideﬁnite constraints. These problems were, until recently, considered numerically unsolvable, and researchers were looking for other formulations of their problem that often lead only to approximation (good or bad) of the true solution. This was our main motivation for the development of PENNON [23], a code for nonlinear optimization problems with matrix variables and matrix inequality constraints.

Apart from PENNON, other concepts for the solution of nonlinear semideﬁnite programs are suggested in literature; see [32] for a discussion on the classic augmented Lagrangian method applied to nonlinear semideﬁnite programs, [6,10,12] for sequential semideﬁnite programming algorithms and [19] for a smoothing type algorithm. However, to our best knowledge, none of these algorithmic concepts lead to a publicly available code yet.

In this article, we present PENLAB, a younger brother of PENNON and a new implementation from NAG. PENLAB can solve the same classes of problems, uses the same algorithm and its behaviour is very similar. However, its performance is relatively

![image 6](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile6.png>)

Jan Fiala: The Numerical Algorithms Group Ltd, Wilkinson House, Jordan Hill Road, Oxford, OX2 8DR, UK, e-mail: jan@nag.co.uk

Michal Kocˇvara: School of Mathematics, University of Birmingham, Birmingham B15 2TT, UK and Institute of Information Theory and Automation, Academy of Sciences of the Czech Republic, Pod voda´renskou veˇzˇ´ı 4, 18208 Praha 8, Czech Republic, e-mail: m.kocvara@bham.ac.uk

Michael Stingl: Applied Mathematics II, University of Erlangen-Nuremberg, Na¨gelsbachstr. 49b, 91052 Erlangen, Germany, e-mail: stingl@am.uni-erlangen.de

⋆ The research of MK was partly supported by the Grant Agency of the Czech Republic through project GAP201-12-0671.

limited in comparison to [23] and [1], due to MATLAB implementation. On the other hand, PENLAB is open source and allows the user not only to solve problems but to modify various parts of the algorithm. As such, PENLAB is particularly suitable for teaching and research purposes and for testing new algorithmic ideas.

After a brief presentation of the underlying algorithm, we focus on practical use of the solver, both for general problem classes and for speciﬁc practical problems, namely, the nearest correlation matrix problem with constraints on condition number, the truss topology problem with global stability constraint and the static output feedback problem. More applications of nonlinear semideﬁnite programming problems can be found, for instance, in [2,18,26].

PENLAB is distributed under GNU GPL license and can be downloaded from http://web.mat.bham.ac.uk/kocvara/penlab.

We use standard notation: Matrices are denoted by capital letters (A,B,X,...) and their elements by the corresponding small-case letters (aij,bij,xij,...). For vectors x,y ∈ Rn, x,y := ni=1 xiyi denotes the inner product. Sm is the space of real symmetric matrices of dimension m × m. The inner product on Sm is deﬁned by

A,B Sm := Tr (AB). When the dimensions of A and B are known, we will often use notation A,B , same as for the vector inner product. Notation A B for A,B ∈ Sm means that the matrix B − A is positive semideﬁnite. If A is an m × n matrix and aj its j-th column, then vecA is the mn × 1 vector

vecA = aT1 aT2 ··· aTn T .

Finally, for Φ : Sm → Sm and X,Y ∈ Sm, DΦ(X;Y ) denotes the directional derivative of Φ with respect to X in direction Y .

## 2. The problem

We intend to solve optimization problems with a nonlinear objective subject to nonlinear inequality and equality constraints and nonlinear matrix inequalities (NLP-SDP):

f(x,Y ) (1)

min

x∈Rn,Y1∈Sp1,...,Yk∈Spk

subject to gi(x,Y ) ≤ 0, i = 1,...,mg hi(x,Y ) = 0, i = 1,...,mh Ai(x,Y ) 0, i = 1,...,mA λiI Yi λiI, i = 1,...,k .

![image 9](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile9.png>)

![image 10](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile10.png>)

Here

- – x ∈ Rn is the vector variable;
- – Y1 ∈ Sp1

,...,Yk ∈ Spk are the matrix variables, k symmetric matrices of dimensions p1 × p1,...,pk × pk;

- – we denote Y = (Y1,...,Yk);
- – f, gi and hi are C2 functions from Rn × Sp1

× ... × Spk to R;

- – λi and λi are the lower and upper bounds, respectively, on the eigenvalues of Yi, i = 1,...,k;

![image 11](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile11.png>)

![image 12](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile12.png>)

- – Ai(x,Y ) are twice continuously differentiable nonlinear matrix operators from


× ... × Spk to SpAi where pA

, i = 1,...,mA, are positive integers.

Rn × Sp1

i

## 3. The algorithm

The basic algorithm used in this article is based on the nonlinear rescaling method of Roman Polyak [30] and was described in detail in [23] and [31]. Here we brieﬂy recall it and stress points that will be needed in the rest of the paper.

The algorithm is based on a choice of penalty/barrier functions ϕ : R → R that penalize the inequality constraints and Φ : Sp → Sp penalizing the matrix inequalities. These functions satisfy a number of properties (see [23,31]) that guarantee that for any π > 0 and Π > 0, we have

z(x) ≤ 0 ⇐⇒ πϕ(z(x)/π) ≤ 0, z ∈ C2(Rn → R) and

Z 0 ⇐⇒ ΠΦ(Z/Π) 0, Z ∈ Sp . This means that, for any π > 0, Π > 0, problem (1) has the same solution as the following “augmented” problem

f(x,Y ) (2)

min

x∈Rn,Y1∈Sp1,...,Yk∈Spk

subject to ϕπ(gi(x,Y )) ≤ 0, i = 1,...,mg ΦΠ(Ai(x,Y )) 0, i = 1,...,mA ΦΠ(λiI − Yi) 0, i = 1,...,k ΦΠ(Yi − λiI) 0, i = 1,...,k hi(x,Y ) = 0, i = 1,...,mh ,

![image 13](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile13.png>)

![image 14](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile14.png>)

where we have used the abbreviations ϕπ = πϕ(·/π) and ΦΠ = ΠΦ(·/Π). The Lagrangian of (2) can be viewed as a (generalized) augmented Lagrangian of

(1): F(x,Y,u,Ξ,U,U,v,π,Π)

![image 16](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile16.png>)

![image 17](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile17.png>)

mg

mA

Ξi,ΦΠ(Ai(x,Y ))

uiϕπ(gi(x,Y )) +

= f(x,Y ) +

i=1

i=1

k

k

Ui,ΦΠ(Yi − λiI) + v⊤h(x,Y ); (3)

![image 18](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile18.png>)

![image 19](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile19.png>)

Ui,ΦΠ(λiI − Yi) +

+

![image 20](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile20.png>)

![image 21](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile21.png>)

i=1

i=1

here u ∈ Rmg, Ξ = (Ξ1,...,Ξm

),Ξi ∈ SpAi, and U = (U1,...,Uk),U = (U1,...,Uk), Ui,Ui ∈ Spi, are Lagrange multipliers associated with the standard and the matrix inequality constraints, respectively, and v ∈ Rmh is the vector of Lagrangian multipliers associated with the equality constraints.

![image 22](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile22.png>)

A

![image 23](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile23.png>)

![image 24](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile24.png>)

![image 25](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile25.png>)

![image 26](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile26.png>)

![image 27](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile27.png>)

![image 28](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile28.png>)

![image 29](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile29.png>)

The algorithm combines ideas of the (exterior) penalty and (interior) barrier methods with the augmented Lagrangian method.

- Algorithm 1 Let x1,Y 1 and u1,Ξ1,U1,U1,v1 be given. Let π1 > 0, Π1 > 0 and α1 > 0. For ℓ = 1,2,... repeat till a stopping criterium is reached:


![image 30](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile30.png>)

![image 31](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile31.png>)

- (i) Find xℓ+1, Y ℓ+1 and vℓ+1 such that  ∇x,Y F(xℓ+1,Y ℓ+1,uℓ,Ξℓ,Uℓ,Uℓ,vℓ+1,πℓ,Πℓ) ≤ αℓ

![image 32](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile32.png>)

![image 33](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile33.png>)

h(xℓ+1,Y ℓ+1) ≤ αℓ

- (ii) uℓi+1 = uℓiϕ′πℓ(gi(xℓ+1,Y ℓ+1)), i = 1, ...,mg Ξiℓ+1 = DAΦΠℓ(Ai(xℓ+1,Y ℓ+1);Ξiℓ), i = 1, ...,mA Uℓi+1 = DAΦΠℓ((λiI − Yiℓ+1);Uℓi), i = 1, ...,k Uℓi+1 = DAΦΠℓ((Yiℓ+1 − λiI);Uℓi), i = 1, ...,k

![image 34](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile34.png>)

![image 35](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile35.png>)

![image 36](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile36.png>)

![image 37](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile37.png>)

![image 38](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile38.png>)

![image 39](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile39.png>)

- (iii) πℓ+1 < πℓ, Πℓ+1 < Πℓ, αℓ+1 < αℓ .


In Step (i) we attempt to ﬁnd an approximate solution of the following system (in x,Y and v):

![image 40](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile40.png>)

∇x,Y F(x,Y,u,Ξ,U,U,v,π,Π) = 0 h(x,Y ) = 0 ,

(4)

![image 41](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile41.png>)

where the penalty parameters π,Π, as well as the multipliers u,Ξ,U,U are ﬁxed. In order to solve it, we apply the damped Newton method. Descent directions are calculated utilizing the MATLAB command ldl that is based on the factorization routine MA57, in combination with an inertia correction strategy described in [31]. In the forthcoming release of PENLAB, we will also apply iterative methods, as described in [24]. The step length is derived using an augmented Lagrangian merit function deﬁned as

![image 42](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile42.png>)

![image 43](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile43.png>)

- 1

![image 44](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile44.png>)

- 2µ


![image 45](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile45.png>)

F(x,Y,u,Ξ,U,U,v,π,Π) +

![image 46](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile46.png>)

h(x,Y ) 22

along with an Armijo rule.

If there are no equality constraints in the problems, the unconstrained minimization in Step (i) is performed by the modiﬁed Newton method with line-search (for details, see [23]).

The multipliers calculated in Step (ii) are restricted in order to satisfy:

uℓi+1 uℓi

1 µ

<

µ <

![image 48](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile48.png>)

![image 49](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile49.png>)

with some positive µ ≤ 1; by default, µ = 0.3. A similar restriction procedure can be applied to the matrix multipliers Uℓ+1,Uℓ+1 and Ξ; see again [23] for details.

![image 50](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile50.png>)

![image 51](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile51.png>)

The penalty parameters π,Π in Step (iii) are updated by some constant factor dependent on the initial penalty parameters π1,Π1. The update process is stopped when πeps (by default 10−6) is reached.

Algorithm 1 is stopped when a criterion based on the KKT error is satisﬁed and both of the inequalities holds:

|f(xℓ,Y ℓ) − F(xℓ,Y ℓ,uℓ,Ξℓ,Uℓ,Uℓ,vℓ,πℓ,Πℓ)| 1 + |f(xℓ,Y ℓ)|

![image 52](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile52.png>)

< ǫ |f(xℓ,Y ℓ) − f(xℓ−1,Y ℓ−1)| 1 + |f(xℓ,Y ℓ)|

![image 53](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile53.png>)

![image 54](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile54.png>)

< ǫ ,

![image 55](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile55.png>)

where ǫ is by default 10−6.

- 3.1. Choice of ϕ and Φ


To treat the standard NLP constraints, we use the penalty/barrier function proposed by Ben-Tal and Zibulevsky [3]:

 

- 1

![image 56](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile56.png>)

- 2


τ2 if τ ≥ τ¯

τ +

(5)

ϕτ¯(τ) =

- 1

![image 57](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile57.png>)

- 2


1 + 2¯τ − τ 1 + τ¯



− (1 + τ¯)2 log

τ¯2 if τ < τ¯;

+ τ¯ +

![image 58](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile58.png>)

by default, τ¯ = −21.

![image 59](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile59.png>)

The penalty function ΦΠ of our choice is deﬁned as follows (here, for simplicity, we omit the variable Y ):

ΦΠ(A(x)) = −Π2(A(x) − ΠI)−1 − ΠI . (6)

The advantage of this choice is that it gives closed formulas for the ﬁrst and second derivatives of ΦΠ. Deﬁning

Z(x) = −(A(x) − ΠI)−1 (7)

we have (see [23]):

∂A(x) ∂xi

∂ ∂xi

ΦΠ(A(x)) = Π2Z(x)

Z(x) ∂2 ∂xi∂xj

![image 61](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile61.png>)

![image 62](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile62.png>)

∂A(x) ∂xj

∂A(x) ∂xi

ΦΠ(A(x)) = Π2Z(x)

Z(x)

![image 63](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile63.png>)

![image 64](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile64.png>)

![image 65](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile65.png>)

∂A(x) ∂xj

+

Z(x)

![image 66](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile66.png>)

∂2A(x) ∂xi∂xj

+

![image 67](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile67.png>)

∂A(x) ∂xi

Z(x).

![image 68](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile68.png>)

- 3.2. Strictly feasible constraints


In certain applications, some of the bound constraints must remain strictly feasible for all iterations because, for instance, the objective function may be undeﬁned at infeasible points (see examples in Section 7.2). To be able to solve such problems, we treat these inequalities by a classic barrier function. In case of matrix variable inequalities, we split Y in non-strictly feasible matrix variables Y1 and strictly feasible matrix variables Y2, respectively, and deﬁne the augmented Lagrangian

![image 69](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile69.png>)

![image 70](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile70.png>)

F(x,Y1,Y2,u,Ξ,U,U,v,π,Π,κ) = F(x,Y1,u,Ξ,U,U,v,π,Π) + κΦbar(Y2),

![image 71](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile71.png>)

![image 72](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile72.png>)

(8) where Φbar can be deﬁned, for example for the constraint Y2 0, by

Φbar(Y2) = − log det(Y2).

Strictly feasible variables x are treated in a similar manner. Note that, while the penalty parameter π may be constant from a certain index ℓ¯ (see again [31] for details), the barrier parameter κ is required to tend to zero with increasing ℓ.

## 4. The code

PENLAB is a free open-source MATLAB implementation of the algorithm described above. The main attention was given to clarity of the code rather than tweaks to improve its performance. This should allow users to better understand the code and encourage them to edit and develop the algorithm further. The code is written entirely in MATLAB with an exception of two mex-functions that handles the computationally most intense task of evaluating the second derivative of the Augmented Lagrangian and a sum of multiple sparse matrices (a slower non-mex alternative is provided as well). The solver is implemented as a MATLAB handle class and thus it should be supported on all MATLAB versions starting from R2008a.

PENLAB is distributed under GNU GPL license and can be downloaded from http://web.mat.bham.ac.uk/kocvara/penlab. The distribution package includes the full source code and precompiled mex-functions, PENLAB User’s Guide and also an internal (programmer’s) documentation which can be generated from the source code. Many examples provided in the package show various ways of calling PENLAB and handling NLP-SDP problems.

- 4.1. Usage

The source code is divided between a class penlab which implements Algorithm 1 and handles generic NLP-SDP problems similar to formulation (1) and interface routines providing various specialized inputs to the solver. Some of these are described in Section 6.

The user needs to prepare a MATLAB structure (here called penm) which describes the problem parameters, such as number of variables, number of constraints, lower and upper bounds, etc. Some of the ﬁelds are shown in Table 1, for a complete list see the PENLAB User’s Guide. The structure is passed to penlab which returns the initialized problem instance:

>> problem = penlab(penm); The solver might be invoked and results retrieved, for example, by calling

>> problem.solve() >> problem.x

The point x or option settings might be changed and the solver invoked again. The whole object can be cleared from the memory using >> clear problem;

Table 1. Selection of ﬁelds of the MATLAB structure penm used to initialize PENLAB object. Full list is available in PENLAB User’s Guide. ﬁeld name meaning Nx dimension of vector x NY number of matrix variables Y Y cell array of length NY with a nonzero pattern of each of the matrix variables lbY NY lower bounds on matrix variables (in spectral sense) ubY NY upper bounds on matrix variables (in spectral sense) NANLN number of nonlinear matrix constraints NALIN number of linear matrix constraints lbA lower bounds on all matrix constraints ubA upper bounds on all matrix constraints

![image 74](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile74.png>)

![image 75](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile75.png>)

![image 76](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile76.png>)

- 4.2. Callback functions


The principal philosophy of the code is similar to many other optimization codes—we use callback functions (providedby the user) to compute function values and derivatives of all involved functions.

For a generic problem, the user must deﬁne nine MATLAB callback functions: objfun, objgrad, objhess, confun, congrad, conhess, mconfun, mcongrad, mconhess for function value, gradient, and Hessian of the objective function, (standard) constraints and matrix constraint. If one constraint type is not present, the corresponding callbacks need not be deﬁned. Let us just show the parameters of the most complex callbacks for the matrix constraints:

function [Ak, userdata] = mconfun(x,Y,k,userdata) function [dAki,userdata] = mcongrad(x,Y,k,i,userdata) function [ddAkij, userdata] = mconhess(x,Y,k,i,j,userdata) Here x,Y are the current values of the (vector and matrix) variables. Parameter k stands for the constraint number. Because every element of the gradient and the Hessian of a matrix function is a matrix, we compute them (the gradient and the Hessian) elementwise (parameters i,j). The outputs Ak,dAki,ddAkij are symmetric matrices saved in sparse MATLAB format.

Finally, userdata is a MATLAB structure passed through all callbacks for user’s convenience and may contain any additional data needed for the evaluations. It is unchanged by the algorithm itself but it can be modiﬁed in the callbacks by user. For instance, some time-consuming computation that depends on x,Y,k but is independent of i can be performed only for i = 1, the result stored in userdata and recalled for any i > 1 (see, e.g., Section 7.2, example Truss Design with Buckling Constraint).

- 4.3. Mex ﬁles


Despite our intentions to use only pure Matlab code, two routines were identiﬁed to cause a signiﬁcant slow-down and therefore their m-ﬁles were substituted with equivalent mex-ﬁles. The ﬁrst one computes linear combination of a set of sparse matrices, e.g., when evaluating Ai(x) for polynomial matrix inequalities, and is based on ideas from [7]. The second one evaluates matrix inequality contributions to the Hessian of the augmented Lagrangian (3) when using penalty function (6).

The latter case reduces to computing zℓ = TAkU, Aℓ for ℓ = k,...,n where T,U ∈ Sm are dense and Aℓ ∈ Sm are sparse with potentially highly varying densities. Such expressions soon become challenging for nontrivial m and can easily dominate the whole Algorithm 1. Note that the problem is common even in primal-dual interior point methods for SDPs and have been studied in [13]. We developed a relatively simple strategy which can be viewed as an evolution of the three computational formulae presented in [13] and offers a minimal number of multiplications while keeping very modest memory requirements. We refer to it as a look-ahead strategy with caching. It can be described as follows:

- Algorithm 2 Precompute a set J of all nonempty columns across all Aℓ,ℓ = k,...,n and a set I of nonempty rows of Ak (look-ahead). Reset ﬂag vector c ← 0, set z = 0 and v = w = 0. For each j ∈ J perform:


- 1. compute selected elements of the j-th column of AkU, i.e., vi = mα=1(Ak)iαUαj for i ∈ I,
- 2. for each Aℓ with nonempty j-th column go through its nonzero elements (Aℓ)ij and


- (a) if ci < j compute wi = α∈I Tiαvα and set ci ← j (caching),
- (b) update trace, i.e., zℓ = zℓ + wi(Aℓ)ij.


## 5. Gradients and Hessians of matrix valued functions

There are several concepts of derivatives of matrix functions; they, however, only differ in the ordering of the elements of the resulting “differential”. In PENLAB, we use the following deﬁnitions of the gradient and Hessian of matrix valued functions.

- Deﬁnition 1. Let F be a differentiable m×n real matrix function of an p×q matrix of real variables X. The (i,j)-th element of the gradient of F at X is the m × n matrix

[∇F(X)]ij :=

∂F(X) ∂xij

![image 79](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile79.png>)

, i = 1,...,p, j = 1,...,q . (9)

- Deﬁnition 2. Let F be a twice differentiable m × n real matrix function of an p × q matrix of real variables X. The (ij,kℓ)-th element of the Hessian of F at X is the m×n matrix


∂2F(X) ∂xij∂xkl

∇2F(X) ij,kℓ :=

, i,k = 1,...,p, j,ℓ = 1,...,q . (10)

![image 80](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile80.png>)

In other words, for every pair of variables xij, xkℓ, elements of X, the second partial derivative of F(X) with respect to these variables is the m × n matrix ∂

2F(X) ∂xij∂xkℓ.

![image 81](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile81.png>)

How to compute these derivatives, i.e., how to deﬁne the callback functions? In Appendix A, we summarize basic formulas for the computation of derivatives of scalar and matrix valued functions of matrices.

For low-dimensional problems, the user can utilize MATLAB’s Symbolic Toolbox. For instance, for F(X) = XX, the commands

>> A=sym(’X’,[2,2]); >> J=jacobian(X*X,X(:)); >> H=jacobian(J,X(:));

generate arrays J and H such that the i-th column of J is the vectorized i-th element of the gradient of F(X); similarly, the k-th column of H, k = (i − 1)n2 + j for i,j = 1,...,n2 is the vectorized (i,j)-th element of the Hessian of F(X). Clearly, the dimension of the matrix variable is ﬁxed and for a different dimension we have to generate new formulas. Unfortunately, this approach is useless for higher dimensional matrices (the user is invited to use the above commands for F(X) = X−1 with X ∈ S5 to see the difﬁculties). However, one can always use symbolic computation to check validity of general dimension independent formulas on small dimensional problems.

## 6. Pre-programmed interfaces

PENLAB distribution contains several pre-programmed interfaces for standard optimization problems with standard inputs. For these problems, the user does not have to create the penm object, nor the callback functions.

- 6.1. Nonlinear optimization with AMPL input

PENLAB can read optimization problems that are deﬁned in and processed by AMPL [11]. AMPL contains routines for automatic differentiation, hence the gradients and Hessians in the callbacks reduce to calls to appropriate AMPL routines.

Assume that nonlinear optimization problem is processed by AMPL, so that we have the corresponding.nl ﬁle, for instance chain.nl, stored in directorydatafiles. All the user has to do to solve the problem is to call the following three commands:

>> penm = nlp_define(’datafiles/chain100.nl’); >> problem = penlab(penm); >> problem.solve();

- 6.2. Linear semideﬁnite programming

Assume that the data of a linear SDP problem is stored in a MATLAB structure sdpdata. Alternatively, such a structure can be created by the user from SDPA input ﬁle [14]. For instance, to read problem arch0.dat-s stored in directory datafiles, call

>> sdpdata = readsdpa(’datafiles/control1.dat-s’);

To solve the problem by PENLAB, the user just has to call the following sequence of commands:

>> penm = sdp_define(sdpdata); >> problem = penlab(penm); >> problem.solve();

- 6.3. Bilinear matrix inequalities


We want to solve an optimization problem with quadratic objective and constraints in the form of bilinear matrix inequalities:

- 1

![image 83](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile83.png>)

- 2


xTHx + cTx (11) subject to blow ≤ Bx ≤ bup Qi0 +

min

x∈Rn

n

n

n

xkQik +

xkxℓQikℓ 0, i = 1,...,m.

k=1

k=1

ℓ=1

The problem data should be stored in a simple format explained in PENLAB User’s Guide. All the user has to do to solve the problem is to call the following sequence of commands:

>> load datafiles/bmi_example; >> penm = bmi_define(bmidata); >> problem = penlab(penm); >> problem.solve();

- 6.4. Polynomial matrix inequalities


We want to solve an optimization problem with constraints in the form of polynomial matrix inequalities:

- 1

![image 85](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile85.png>)

- 2


xTHx + cTx (12) subject to blow ≤ Bx ≤ bup

min

x∈Rn

Ai(x) 0, i = 1,...,m with

i(j))Qij

x(κ

Ai(x) =

j

where κi(j) is a multi-index of the i-th constraint with possibly repeated entries and x(κ

i(j)) is a product of elements with indices in κi(j). For example, for

A(x) = Q1 + x1x3Q2 + x2x34Q3

the multi-indices are κ(1) = {0} (Q1 is an absolute term), κ(2) = {1,3} and κ(3) = {2,4,4,4}.

Assuming now that the problem is stored in a structure pmidata (as explained in PENLAB User’s Guide), the user just has to call the following sequence of commands:

>> load datafiles/pmi_example; >> penm = pmi_define(pmidata); >> problem = penlab(penm); >> problem.solve();

## 7. Examples

All MATLAB programs and data related to the examples in this section can be found in directories examples and applications of the PENLAB distribution.

- 7.1. Correlation matrix with the constrained condition number We consider the problem of ﬁnding the nearest correlation matrix ([17]):


n

(Xij − Hij)2 (13)

min

X

i,j=1

subject to Xii = 1, i = 1,...,n X 0 .

In addition to this standard setting of the problem, let us bound the condition number of the nearest correlation matrix by adding the constraint

cond(X) = κ . We can formulate this constraint as

I X κI (14) the variable transformation

X = ζX . After the change of variables, and with the new constraint, the problem of ﬁnding the nearest correlation matrix with a given condition number reads as follows:

n

1 ζ

Xij − Hij)2 (15)

(

min

![image 87](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile87.png>)

ζ, X

i,j=1

subject to Xii − ζ = 0, i = 1,...,n I X κI

The new problem now has the NLP-SDP structure of (1).

We will consider an example based on a practical application from ﬁnances; see [33]. Assume that we are given a 5 × 5 correlation matrix. We now add a new asset class, that means, we add one row and column to this matrix. The new data is based on a different frequency than the original part of the matrix, which means that the new matrix is no longer positive deﬁnite:





1 −0.44 −0.20 0.81 −0.46 −0.05 −0.44 1 0.87 −0.38 0.81 −0.58 −0.20 .87 1 −0.17 0.65 −0.56

Hext =

.

0.81 −0.38 −0.17 1 −0.37 −0.15 −0.46 0.81 0.65 −0.37 1 −0.08 −0.05 −0.58 −0.56 −0.15 0.08 1

 

 

When solving problem (15) by PENLAB with κ = 10, we get the solution after 11 outer and 37 inner iterations. The optimal value of ζ is 3.4886 and, after the back substitution X = ζ1 X, we get the nearest correlation matrix X =

![image 88](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile88.png>)

1.0000 -0.3775 -0.2230 0.7098 -0.4272 -0.0704

- -0.3775 1.0000 0.6930 -0.3155 0.5998 -0.4218
- -0.2230 0.6930 1.0000 -0.1546 0.5523 -0.4914 0.7098 -0.3155 -0.1546 1.0000 -0.3857 -0.1294
- -0.4272 0.5998 0.5523 -0.3857 1.0000 -0.0576
- -0.0704 -0.4218 -0.4914 -0.1294 -0.0576 1.0000


with eigenvalues eigenvals =

0.2866 0.2866 0.2867 0.6717 1.6019 2.8664 and the condition number equal to 10, indeed.

Gradients and Hessians What are the ﬁrst and second partial derivatives of functions involved in problem (15)? The constraint is linear, so the answer is trivial here, and we can only concentrate on the objective function

f(z, X) :=

n

(z Xij − Hij)2 = z X − H,z X − H , (16)

i,j=1

where, for convenience, we introduced a variable z = ζ1.

![image 90](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile90.png>)

- Theorem 1. Let xij and hij, i,j = 1,...,n be elements of X and H, respectively. For the function f deﬁned in (16) we have the following partial derivatives:


- (i) ∇z f(z, X) = 2 X,z X − H
- (ii) ∇ Xf(z, X) ij

= 2z(zxij − hij), i,j = 1,...,n

- (iii) ∇z,z2 f(z, X) = 2 X, X
- (iv) ∇z,2 X f(z, X)

ij

= ∇ X,z2 f(z, X)

ij

= 4zxij − 2hij, i,j = 1,...,n

- (v) ∇ X,2 X f(z, X)


= 2z2 for i = k, j = ℓ and zero otherwise (i,j,k,ℓ = 1,...,n).

ij,kℓ

The proof follows directly from formulas in Appendix A.

PENLAB distribution This problemis stored in directory applications/CorrMat of the PENLAB distribution. To solve the above example and to see the resulting eigenvalues of X, run in its directory

>> penm = corr_define; >> problem = penlab(penm); >> problem.solve(); >> eig(problem.Y{1}*problem.x)

- 7.2. Truss topology optimization with stability constraints


In truss optimization we want to design a pin-jointed framework consisting of m slender bars of constant mechanical properties characterized by their Young’s modulus E. We will consider trusses in a d-dimensional space, where d = 2 or d = 3. The bars are jointed at n˜ nodes. The system is under load, i.e., forces fj ∈ Rd are acting at some nodes j. They are aggregated in a vector f, where we put fj = 0 for nodes that are not under load. This external load is transmitted along the bars causing displacements of the nodes that make up the displacement vector u. Let p be the number of ﬁxed nodal coordinates, i.e., the number of components with prescribed discrete homogeneous Dirichlet boundary condition. We omit these ﬁxed components from the problem formulation reducing thus the dimension of u to

n = d · n˜ − p.

Analogously, the external load f is considered as a vector in Rn.

The design variables in the system are the bar volumes x1,...,xm. Typically, we want to minimize the weight of the truss. We assume to have a unique material (and thus density) for all bars, so this is equivalent to minimizing the volume of the truss, i.e., mi=1 xi. The optimal truss should satisfy mechanical equilibrium conditions:

K(x)u = f ; (17) here

m

Ei ℓ2i

γiγi⊤ (18)

xiKi, Ki =

K(x) :=

![image 92](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile92.png>)

i=1

is the so-called stiffness matrix, Ei the Young modulus of the ith bar, ℓi its length and γi the n−vector of direction cosines.

We further introduce the compliance of the truss f⊤u that indirectly measures the stiffness of the structure under the force f and impose the constraints

f⊤u ≤ γ .

This constraint, together with the equilibrium conditions, can be formulated as a single linear matrix inequality ([21])

K(x) f fT γ

0 .

The minimum volume single-load truss topology optimization problem can then be formulated as a linear semideﬁnite program:

m

xi (19) subject to

min

x∈Rm

i=1

K(x) f fT γ

0 xi ≥ 0, i = 1,...,m.

We further consider the constraint on the global stability of the truss. The meaning of the constraint is to avoid global buckling of the optimal structure. We consider the simplest formulation of the buckling constraint based on the so-called linear buckling assumption [21]. As in the case of free vibrations, we need to constrain eigenvalues of the generalized eigenvalue problem

K(x)w = λG(x)w , (20)

in particular, we require that all eigenvalues of (20) lie outside the interval [0,1]. The so-called geometry stiffness matrix G(x) depends, this time, nonlinearly on the design variable x:

G(x) =

m

Gi(x), Gi(x) =

i=1

Exi ℓdi

(γi⊤K(x)−1f)(δiδi⊤ + ηiηi⊤). (21)

![image 93](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile93.png>)

Vectors δ,η are chosen so that γ,δ,η are mutually orthogonal. (The presented formula is for d = 3. In the two-dimensional setting the vector η is not present.) To simplify the notation, we denote

∆i = δiδiT + ηiηiT .

It was shown in [21] that the eigenvalue constraint can be equivalently written as a nonlinear matrix inequality

K(x) + G(x) 0 (22) that is now to be added to (19) to get the following nonlinear semideﬁnite programming problem. Note that xi are requested to be strictly feasible.

m

xi (23) subject to

min

x∈Rm

i=1

K(x) f fT γ

0

K(x) + G(x) 0 xi > 0, i = 1,...,m

Gradients and Hessians Let M : Rm → Rn×n be a matrix valued function assigning each vector ξ a matrix M(ξ). We denote by ∇kM the partial derivative of M(ξ) with respect to the k-th component of vector ξ.

Lemma 1 (based on [27]). Let M : Rm → Rn×n be a symmetric matrix valued function assigning each ξ ∈ Rm a nonsingular (n×n) matrix M(ξ). Then (for convenience we omit the variable ξ)

∇kM−1 = −M−1(∇kM)M−1 .

If M is a linear function of ξ, i.e., M(ξ) = mi=1 ξiMi with symmetric positive semidefinite Mi,i = 1,...,m, then the above formula simpliﬁes to

∇kM−1 = −M−1MkM−1 .

- Theorem 2 ([21]). Let G(x) be given as in (21). Then


and

[∇G]k =

m

E ℓ3k

γkTK−1f∆k −

![image 95](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile95.png>)

j=1

Etj ℓ3j

γjTK−1KkK−1f∆j

![image 96](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile96.png>)

E ℓ3k

[∇2G]kℓ = −

E ℓ3ℓ

γkTK−1KℓK−1f∆k −

γℓTK−1KkK−1f∆ℓ

![image 97](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile97.png>)

![image 98](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile98.png>)

m

Etj ℓ3j

γjTK−1KℓK−1KkK−1f∆j

−

![image 99](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile99.png>)

j=1

m

Etj ℓ3j

γjTK−1KkK−1KℓK−1f∆j.

−

![image 100](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile100.png>)

j=1

Example Consider the standard example of a laced column under axial loading (example tim in the PENLAB collection). Due to symmetry, we only consider one half of the column, as shown in Figure 1(top-peft); it has 19 nodes and 42 potential bars, so n = 34 and m = 42. The column dimensions are 8.5 × 1, the two nodes on the left-hand side are ﬁxed and the “axial” load applied at the column tip is (0,−10). The upper bound on the compliance is chosen as γ = 1.

Assume ﬁrst that xi = 0.425,i = 1,...,m, i.e., the volumes of all bars are equal and the total volume is 17.85. The values of xi were chosen such that the truss satisﬁes the compliance constraint: f⊤u = 0.9923 ≤ γ. For this truss, the smallest nonnegative eigenvalue of (20) is equal to 0.7079 and the buckling constraint (22) is not satisﬁed. Figure 1(top-right) shows the corresponding the buckling mode (eigenvector associated with this eigenvalue). Let us now solve the truss optimization problem without the sta-

Fig. 1. Truss optimization with stability problem: initial truss (top-left); its buckling mode (top-right); optimal truss without stability constraint (bottom-left); and optimal stable truss (bottom-right)

bility constraint (23). We obtain the design shown in Figure 1(bottom-left). This truss is much lighter than the original one (

m

xi = 9.388), it is, however, extremely unstable under the given load, as (20) has a zero eigenvalue.

i=1

When solving the truss optimization problem with the stability constraint (23) by PENLAB, we obtain the design shown in Figure 1(bottom-right). This truss is still signiﬁcantly lighter than the original one (

m

xi = 12.087), but it is now stable under

i=1

the given load. To solve the nonlinear SDP problem, PENLAB needed 18 global and 245 Newton iterations and 212 seconds of CPU time, 185 of which were spent in the Hessian evaluation routines.

PENLAB distribution Directories applications/TTOand applications/TTObuckling of the PENLAB distribution contain the problem formulation and many examples of trusses. To solve the above example with the buckling constraint, run

>> solve_ttob(’GEO/tim.geo’)

in directory TTObuckling.

- 7.3. Static output feedback Given a linear system with A ∈ Rn×n,B ∈ Rn×m,C ∈ Rp×n


- x˙ = Ax + Bu
- y = Cx


we want to stabilize it by static output feedback u = Ky . That is, we want to ﬁnd a matrix K ∈ Rm×p such that the eigenvalues of the closed-loop system A + BKC belong to the left half-plane.

The standard way how to treat this problem is based on the Lyapunov stability theory. It says that A + BKC has all its eigenvalues in the open left half-plane if and only if there exists a symmetric positive deﬁnite matrix P such that

(A + BKC)TP + P(A + BKC) ≻ 0 . (24)

Hence, by introducing the new variable, the Lyapunov matrix P, we can formulate the SOF problem as a feasibility problem for the bilinear matrix inequality (24) in variables K and P. As typically n > p,m (often n ≫ p,m), the Lyapunov variable dominates here, although it is just an auxiliary variable and we do not need to know its value at the feasible point. Hence a natural question arises whether we can avoid the Lyapunov variable in the formulation of the problem. The answer was given in [15] and lies in the formulation of the problem using polynomial matrix inequalities.

Let k = vecK. Deﬁne the characteristic polynomial of A + BKC:

q(s,k) = det(sI − A − BKC) =

n

qi(k)si ,

i=0

where qi(k) = α qiαkα and α ∈ Nmp are all monomialpowers. The Hermite stability criterion says that the roots of q(s,k) belong to the stability region D (in our case the

left half-plane) if and only if

n

H(q) =

i=0

n

qi(k)qj(k)Hij ≻ 0 .

j=0

Here the coefﬁcients Hij depend on the stability region only (see, e.g., [16]). For instance, for n = 3, we have

 

  .

2q0q1 0 2q0q3 0 2q1q2 − 2q0q3 0 2q0q3 0 2q2q3

H(q) =

The Hermite matrix H(q) = H(k) depends polynomially on k: H(k) =

Hαkα ≻ 0 (25)

α

where Hα = HαT ∈ Rn×n and α ∈ Nmp describes all monomial powers.

- Theorem 3 ([15]). Matrix K solves the static output feedback problem if and only if k = vecK satisﬁes the polynomial matrix inequality (25).


In order to solve the strict feasibility problem (25), we can solve the following optimization problem with a polynomial matrix inequality

λ − µ k 2 (26) subject to H(k) λI .

max

k∈Rmp, λ∈R

Here µ > 0 is a parameter that allows us to trade off between feasibility of the PMI and a moderate norm of the matrix K, which is generally desired in practice.

COMPlib examples In order to use PENLAB for the solution of SOF problems (26), we have developed an interface to the problem library COMPlib [25]1. Table 2 presents the results of our numericaltests. We have only solved COMPlib problemsof small size, with n < 10 and mp < 20. The reason for this is that our MATLAB implementation of the interface (building the matrix H(k) from COMPlib data) is very time-consuming. For each COMPlib problem, the table shows the degree of the matrix polynomial, problem dimensions n and mp, the optimal λ (the negative largest eigenvalue of the matrix K), the CPU time and number of Newton iterations/linesearch steps of PENLAB. The ﬁnal column contains information about the solution quality. “F” means failure of PENLAB to converge to an optimal solution. The plus sign “+” means that PENLAB converged to a solution which does not stabilize the system and ”0” is used when PENLAB converged to a solution that is on the boundary of the feasible domain and thus not useful for stabilization. The reader can see that PENLAB can solve all problems apart from AC7, NN10, NN13 and NN14; these problems are, however, known to be very ill-conditioned and could not be solved via the Lyapunov matrix approach either (see [22]). Notice that the largest problems with polynomials of degree up to 8 did not cause any major difﬁculties to the algorithm.

PENLAB distribution The related MATLAB programsare stored in directory applications/SOF of the PENLAB distribution. To solve, for instance, example AC1, run

>> sof(’AC1’); COMPlib program and library must be installed on user’s computer.

## 8. PENLAB versus PENNON (MATLAB versus C)

The obvious concern of any user will be, how fast (or better, how slow) is the MATLAB implementation and if it can solve any problems of non-trivial size. The purpose of this section is to give a very rough comparison of PENLAB and PENNON, i.e., the MATLAB and C implementation of the same algorithm. The reader should, however, not make any serious conclusion from the tables below, for the following reasons:

![image 104](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile104.png>)

1 The authors would like to thank Didier Henrion, LAAS-CNRS Toulouse, for developing a substantial part of this interface.

### Table 2. mmm

Problem degree n mp λopt CPU (sec) iter remark AC1 5 5 9 −0.871 · 100 2.2 27/30 AC2 5 5 9 −0.871 · 100 2.3 27/30 AC3 4 5 8 −0.586 · 100 1.8 37/48 AC4 2 4 2 0.245 · 10−2 1.9 160/209 + AC6 4 7 8 −0.114 · 104 1.2 22/68 AC7 2 9 2 −0.102 · 103 0.9 26/91 AC8 2 9 5 0.116 · 100 3.9 346/1276 F

![image 106](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile106.png>)

![image 107](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile107.png>)

- AC11 4 5 8 −0.171 · 105 2.3 65/66
- AC12 6 4 12 0.479 · 100 12.3 62/73 +


- AC15 4 4 6 −0.248 · 10−1 1.2 25/28
- AC16 4 4 8 −0.248 · 10−1 1.2 23/26
- AC17 2 4 2 −0.115 · 102 1.0 19/38


- HE1 2 4 2 −0.686 · 102 1.0 22/22
- HE2 4 4 4 −0.268 · 100 1.6 84/109 HE5 4 8 8 0.131 · 102 1.9 32/37 +


- REA1 4 4 6 −0.726 · 102 1.4 33/35
- REA2 4 4 4 −0.603 · 102 1.3 34/58


- DIS1 8 8 16 −0.117 · 102 137.6 30/55
- DIS2 4 3 4 −0.640 · 101 1.6 59/84
- DIS3 8 6 16 −0.168 · 102 642.3 66/102 MFP 3 4 6 −0.370 · 10−1 1.0 20/21


- TF1 4 7 8 −0.847 · 10−8 1.7 27/31 0
- TF2 4 7 6 −0.949 · 10−7 1.3 19/23 0
- TF3 4 7 6 −0.847 · 10−8 1.6 28/38 0 PSM 4 7 6 −0.731 · 102 1.1 17/39 NN1 2 3 2 −0.131 · 100 1.2 32/34 0


- NN3 2 4 1 0.263 · 102 1.0 31/36 +
- NN4 4 4 6 −0.187 · 102 1.2 33/47
- NN5 2 7 2 0.137 · 102 1.5 108/118 +


- NN8 3 3 4 −0.103 · 101 1.0 19/29
- NN9 4 5 6 0.312 · 101 1.6 64/97 +
- NN10 6 8 9 0.409 · 104 18.3 300/543 F


- NN12 4 6 4 0.473 · 101 1.4 47/58 +
- NN13 4 6 4 0.279 · 1012 2.2 200/382 F
- NN14 4 6 4 0.277 · 1012 2.3 200/382 F
- NN15 3 3 4 −0.226 · 100 1.0 15/14
- NN16 7 8 16 −0.623 · 103 613.3 111/191
- NN17 2 3 2 0.931 · 10−1 1.0 25/26 +


![image 108](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile108.png>)

- – Both implementations slightly differ. This can be seen on the different numbers of iterations needed to solve single examples.
- – The difference in CPU timing very much depends on the type of the problem. For instance, some problems require multiplications of sparse matrices with dense onesin this case, the C implementation will be much faster. On the other hand, for some problems most of the CPU time is spent in the dense Cholesky factorization which, in both implementations, relies on LAPACK routines and thus the running time may be comparable.
- – The problems were solved using an Intel i7 processor with two cores. The MATLAB implementation used both cores to perform some commands, while the C implementation only used one core. This is clearly seen, e.g., example lame emd10 in Table 3.


![image 109](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile109.png>)

- – For certain problems (such as mater2 in Table 5), most of the CPU time of PENLAB is spent in the user deﬁned routine for gradient evaluation. For linear SDP, this only amounts to reading the data matrices, in our implementation elements of a twodimensional cell array, from memory. Clearly, a more sophisticated implementation would improve the timing.


For all calculations, we have used a notebook running Windows 7 (32 bit) on Intel Core i7 CPU M620@2.67GHz with 4GB memory and MATLAB 7.7.0.

- 8.1. Nonlinear programming problems

We ﬁrst solved selected examples from the COPS collection [8] using AMPL interface. These are medium size examples mostly coming from ﬁnite element discretization of optimization problems with PDE constraints. Table 3 presents the results.

- Table 3. Selected COPS examples. CPU time is given in seconds. Iteration count gives the number of the global iterations in Algorithm 1 and the total number of steps of the Newton method.


![image 111](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile111.png>)

problem vars constr. constraint PENNON PENLAB type CPU iter. CPU iter.

![image 112](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile112.png>)

elec200 600 200 = 40 81/224 31 43/135 chain800 3199 2400 = 1 14/23 6 24/56

pinene400 8000 7995 = 1 7/7 11 17/17 channel800 6398 6398 = 3 3/3 1 3/3 torsion100 5000 10000 ≤ 1 17/17 17 26/26 bearing100 5000 5000 ≤ 1 17/17 13 36/36 lane emd10 4811 21 ≤ 217 30/86 64 25/49

![image 113](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile113.png>)

dirichlet10 4491 21 ≤ 151 33/71 73 32/68

henon10 2701 21 ≤ 57 49/128 63 76/158 minsurf100 5000 5000 box 1 20/20 97 203/203

gasoil400 4001 3998 = & box 3 34/34 13 59/71 duct15 2895 8601 = & ≤ 6 19/19 9 11/11

tri turtle 3578 3968 ≤ & box 3 49/49 4 17/17 marine400 6415 6392 ≤ & box 2 39/39 22 35/35 steering800 3999 3200 ≤ & box 1 9/9 7 19/40

![image 114](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile114.png>)

methanol400 4802 4797 ≤ & box 2 24/24 16 47/67 catmix400 4398 3198 ≤ & box 2 59/61 15 44/44

![image 115](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile115.png>)

- 8.2. Linear semideﬁnite programming problems


We solved selected problems from the SDPLIB collection (Table 4) and Topology Optimization collection (Table 5); see [5,20]. The data of all problems were stored in SDPA input ﬁles [14]. Instead of PENNON, we have used its clone PENSDP that directly reads the SDPA ﬁles and thus avoid repeated calls of the call back functions. The difference between PENNON and PENSDP (in favour of PENSDP) would only be signiﬁcant in the mater2 example with many small matrix constraints.

- Table 4. Selected SDPLIB examples. CPU time is given in seconds. Iteration count gives the number of the global iterations in Algorithm 1 and the total number of steps of the Newton method.

![image 117](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile117.png>)

problem vars constr. constr. PENSDP PENLAB

size CPU iter. CPU iter. control3 136 2 30 1 19/103 20 22/315 maxG11 800 1 1600 18 22/41 186 18/61

![image 118](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile118.png>)

qpG11 800 1 1600 43 22/43 602 18/64 ss30 132 1 294 20 23/112 17 12/63 theta3 1106 1 150 11 15/52 61 14/48

![image 119](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile119.png>)

- Table 5. Selected TOPO examples. CPU time is given in seconds. Iteration count gives the number of the global iterations in Algorithm 1 and the total number of steps of the Newton method.


problem vars constr. constr. PENSDP PENLAB

![image 120](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile120.png>)

size CPU iter. CPU iter. buck2 144 2 97 2 23/74 22 18/184 vibra2 144 2 97 2 34/132 35 20/304

![image 121](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile121.png>)

shmup2 200 2 441 65 24/99 172 26/179 mater2 423 94 11 2 20/89 70 12/179

![image 122](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile122.png>)

## A. Appendix: Differential calculus for functions of symmetric matrices

Matrix differentialcalculus—derivativesof functionsdependingon matrices—is a topic covered in several papers; see, e.g., [4,9,28,29] and the book [27]. The notation and the very deﬁnition of the derivative differ in these papers. Hence, for reader’s convenience, we will give a basic overview of the calculus for some typical (in semideﬁnite optimization) functions of matrices.

For a matrix X (whether symmetric or not), let xij denote its (i,j)-th element. Let further Eij denote a matrix with all elements zero except for a unit element in the i-the row and j-th column (the dimension of Eij will be always clear from the context). Our differential formulas are based on Deﬁnitions 1 and 2, hence we only need to ﬁnd the partial derivative of a function F(X), whether matrix or scalar valued, with respect to a single element xij of X.

- A.1. Matrix valued functions


Let F be a differentiable m×n real matrix function of an p×q matrix of real variables X. Table 6 gives partial derivatives of F(X) with respect to xij, i = 1,...,p, j = 1,...,q for some most common functions. In this table, Eij is always of the same dimension as X. To compute other derivatives, we may use the following result on the chain rule.

- Theorem 4. Let F be a differentiable m × n real matrix function of an p × q matrix Y that itself is a differentiable function G of an s × t matrix of real variables X, that is F(Y ) = F(G(X)). Then


p

∂F(G(X)) ∂xij

=

![image 123](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile123.png>)

k=1

q

∂[G(X)]kℓ ∂xij

∂F(Y ) ∂ykℓ

. (27)

![image 124](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile124.png>)

![image 125](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile125.png>)

ℓ=1

### Table 6.

![image 127](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile127.png>)

F(X) ∂F∂x(X)

Conditions

![image 128](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile128.png>)

ij

![image 129](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile129.png>)

X Eij XT Eji AX AEij A ∈ Rm×p XA EijA A ∈ Rm×p XX EijX + XEij XT X EjiX + XT Eij XXT EijXT + XEji

s−2

XkEijXs−k−1 + Xs−1Eij X square, p = 1, 2, . . . X−1 −X−1EijX−1 X nonsingular

Xs EijXs−1 +

k=1

![image 130](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile130.png>)

In particular, we have

∂(G(X)H(X)) ∂xij

∂G(X) ∂xij

∂H(X) ∂xij

(28) ∂(G(X))−1 ∂xij

=

H(X) + G(X)

![image 131](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile131.png>)

![image 132](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile132.png>)

![image 133](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile133.png>)

∂G(X) ∂xij

= −(G(X))−1

(G(X))−1 . (29)

![image 134](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile134.png>)

![image 135](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile135.png>)

We ﬁnish this section with the all important theorem on derivatives of functions of symmetric matrices.

- Theorem 5. Let F be a differentiable n×n real matrix function of a symmetric m×m


matrix of real variables X. Denote Zij be the (i,j)-th element of the gradient of F(X) computed by the general formulas in Table 6 and Theorem 4. Then

[∇F(X)]i,i = Zii and

[∇F(X)]i,j = Zij + Zji for i = j .

x211 + x12x21 x11x12 + x12x22 x11x21 + x21x22 x12x21 + x222

x11 x12 x21 x22

and F(X) = X2 =

. Then

Example Let X =

  

  

2x11 x12 x21 0

x21 x11 + x22

0 x21 x12 0

∇F(X) =

0 x12 x21 2x22

x11 + x22 x12

(a 2×2 array of 2×2 matrices). If we now assume that X is symmetric, i.e. x12 = x21, we get

   .

  

2x11 x21 x21 0

2x21 x11 + x22 x11 + x22 2x21

∇F(X) =

0 x21 x21 2x22

2x21 x11 + x22 x11 + x22 2x21

We can see that we could obtain the gradient for the symmetric matrix using the general formula in Table 6 together with Theorem 5.

Notice that if we simply replaced each x12 in ∇F(X) by x21 (assuming symmetry of X), we would get an incorrect result

  

∇F(X) =

2x11 x21 x21 0

x21 x11 + x22

0 x21 x21 0

0 x21 x21 2x22

x11 + x22 x21

   .

- A.2. Scalar valued functions


Table 7 shows derivatives of some most common scalar valued functions of an m × n matrix X.

Table 7.

![image 137](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile137.png>)

F(X) equivalently ∂F∂x(X)

Conditions

![image 138](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile138.png>)

ij

![image 139](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile139.png>)

TrX I, X δij TrAXT A, X Ai,j A ∈ Rm×n aT Xa aaT , X aiaj a ∈ Rn, m = n TrX2 X, X 2Xj,i m = n

![image 140](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile140.png>)

Let Φ and Ψ be functions of a square matrix variable X. The following derivatives of composite functions allow us to treat many practical problems (Table 8). We can use

Table 8.

![image 141](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile141.png>)

F(X) equivalently ∂F∂x(X)

Conditions

![image 142](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile142.png>)

ij

![image 143](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile143.png>)

TrAΦ(X) A, Φ(X) A, ∂Φ∂x(X)

![image 144](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile144.png>)

ij

TrΦ(X)2 Φ(X), Φ(X) 2 Φ(X), ∂Φ∂x(X)

![image 145](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile145.png>)

ij

+ ∂Φ∂x(X)

Tr(Φ(X)Ψ(X)) Φ(X), Ψ(X) Φ(X), ∂Ψ∂x(X)

, Ψ(X)

![image 146](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile146.png>)

![image 147](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile147.png>)

ij

ij

![image 148](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile148.png>)

it, for instance, to get the following two results for a n × n matrix X and a ∈ Rn:

∂ ∂xij

∂ ∂xij

(aTX−1a) =

aaT,X−1

![image 149](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile149.png>)

![image 150](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile150.png>)

= − aaT,X−1EijX−1

= −aTX−1EijX−1a ,

in particular, ∂ ∂xij

∂ ∂xij

I,X−1 = − I,X−1EijX−1 = −Tr(X−1EijX−1). Recall that for a symmetric n × n matrix X, the above two formulas would change to

Tr X−1 =

![image 152](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile152.png>)

![image 153](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile153.png>)

∂ ∂xij

(aTX−1a) = −aT(Zij + ZijT − diagZij)a and

![image 154](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile154.png>)

∂ ∂xij

Tr X−1 = −Tr(Zij + ZijT − diagZij) with

![image 155](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile155.png>)

Zij = X−1EijX−1 .

- A.3. Second-order derivatives


To compute the second-order derivatives of functions of matrices, we can simply apply the formulas derived in the previous sections to the elements of the gradients. Thus we get, for instance,

∂2X2 ∂xij∂xkℓ

∂ ∂xkℓ

(EijX + XEij) = EijEkℓ + EkℓEij or

=

![image 156](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile156.png>)

![image 157](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile157.png>)

∂2X−1 ∂xij∂xkℓ

∂ ∂xkℓ

(−X−1EijX−1) = X−1EijX−1EklX−1+X−1EklX−1EijX−1 for the matrix valued functions, and

=

![image 158](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile158.png>)

![image 159](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile159.png>)

∂2 ∂xij∂xkℓ

∂2Φ(X)

∂Φ(X) ∂xij

∂Φ(X) ∂xkl

+ 2 Φ(X),

Φ(X),Φ(X) = 2

,

![image 160](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile160.png>)

![image 161](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile161.png>)

![image 162](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile162.png>)

![image 163](<2013-fiala-penlab-matlab-solver-nonlinear_images/imageFile163.png>)

∂xij∂xkℓ for scalar valued matrix functions. Other formulas easily follow.

## References

- 1. NAG Numerical Libraries. http://www.nag.co.uk/, 2013.
- 2. Ch. Anand, R. Sotirov, T. Terlaky, and Z. Zheng. Magnetic resonance tissue quantiﬁcation using optimal bssfp pulse-sequence design. Optimization and Engineering, 8(2):215–238, 2007.
- 3. A. Ben-Tal and M. Zibulevsky. Penalty/barrier multiplier methods for convex programming problems. SIAM Journal on Optimization, 7:347–366, 1997.
- 4. R. J. Boik. Lecture notes: Statistics 550. Technical report, Montana State University, Bozeman, Spring

2006. online.

- 5. B. Borchers. SDPLIB 1.2, a library of semideﬁnite programming test problems. Optimization Methods and Software, 11 & 12:683–690, 1999. Available at http://www.nmt.edu/˜borchers/.
- 6. R. Correa and H. Ramirez. A global algorithm for nonlinear semideﬁnite programming. SIAM Journal on Optimization, 15(1):303–318, 2004.
- 7. T. A. Davis. Direct Methods for Sparse Linear Systems (Fundamentals of Algorithms 2). Society for Industrial and Applied Mathematics, Philadelphia, PA, USA, 2006.


- 8. E. D. Dolan, J. J. More´, and T. S. Munson. Benchmarking optimization software with COPS 3.0. Argonne National Laboratory Technical Report ANL/MCS-TM-273, 2004.
- 9. P. S. Dwyer and M. S. MacPhail. Symbolic matrix derivatives. The Annals of Mathematical Statistics, 19(4):517–534, 1948.
- 10. B. Fares, D. Noll, and P. Apkarian. Robust control via sequential semideﬁnite programming. SIAM Journal on Control and Optimization, 40(6):1791–1820, 2002.
- 11. R. Fourer, D. M. Gay, and B. W. Kerningham. AMPL: A Modeling Language for Mathematical Programming. The Scientiﬁc Press, 1993.
- 12. R. W. Freund, F. Jarre, and C. Vogelbusch. Nonlinear semideﬁnite programming: sensitivity, convergence, and an application in passive reduced order modelling. Math. Program., 109(2-3):581–611, 2007.
- 13. K. Fujisawa, M. Kojima, and K. Nakata. Exploiting sparsity in primal-dual interior-point method for semideﬁnite programming. Mathematical Programming, 79:235–253, 1997.
- 14. K. Fujisawa, M. Kojima, K. Nakata, and M. Yamashita. SDPA User’s Manual—Version 6.00. Technical report, Department of Mathematical and Computing Science, Tokyo University of Technology, 2002.
- 15. D. Henrion, J. Lo¨fberg, M. Kocˇvara, and M. Stingl. Solving polynomial static output feedback problems with PENBMI. In Decision and Control, 2005 and 2005 European Control Conference. CDC-ECC’05. 44th IEEE Conference on, pages 7581–7586. IEEE, 2005.
- 16. D. Henrion, D. Peaucelle, D. Arzelier, and M. Sebek.ˇ Ellipsoidal approximation of the stability domain of a polynomial. In Proceedings of the European Control Conference, Porto, Portugal, 2001.
- 17. N. J. Higham. Computing the nearest correlation matrix—a problem from ﬁnance. IMA Journal of Numerical Analysis, 22(3):329–343, 2002.
- 18. Y. Kanno and I. Takewaki. Sequential semideﬁnite program for maximum robustness design under load uncertainty. Journal of Optimization Theory and Applications, 130(2):265–287, 2006.
- 19. C. Kanzow and C. Nagel. Some structural properties of a Newton-type method for semideﬁnite programs. J. of Opt. Theory and Applications, 122:219–226, 2004.
- 20. M. Kocˇvara. A collection of sparse linear SDP problems arising in structural optimization. Available at http://web.mat.bham.ac.uk/kocvara/pennon/problems.html.
- 21. M. Kocˇvara. On the modelling and solving of the truss design problem with global stability constraints. Struct. Multidisc. Optimization, 23(3):189–203, 2002.
- 22. M. Kocˇvara, F. Leibfritz, M. Stingl, and D. Henrion. A nonlinear SDP algorithm for static output feedback problems in COMPlib. LAAS-CNRS research report no. 04508, LAAS, Toulouse, 2004.
- 23. M. Kocˇvara and M. Stingl. PENNON—a code for convex nonlinear and semideﬁnite programming. Optimization Methods and Software, 18(3):317–333, 2003.
- 24. M. Kocˇvara and M. Stingl. On the solution of large-scale SDP problems by the modiﬁed barrier method using iterative solvers. Mathematical Programming (Series B), 109(2-3):413–444, 2007.
- 25. F. Leibfritz. COMPleib: COnstraint Matrix-optimization Problem library—a collection of test examples for nonlinear semideﬁnite programs, control system design and related problems. Technical report, Universita¨t Trier, 2004.
- 26. F. Leibfritz and S. Volkwein. Reduced order output feedback control design for pde systems using proper orthogonal decomposition and nonlinear semideﬁnite programming. Linear Algebra and Its Applications, 415(2-3):542–575, 2006.
- 27. J. Magnus and H. Neudecker. Matrix differential calculus. Cambridge Univ Press, 1988.
- 28. K. B. Petersen and M. S. Pedersen. The Matrix Cookbook, version 20121115. Technical report, Technical University of Denmark, 2012.
- 29. D. S. G. Pollock. Tensor products and matrix differential calculus. Linear Algebra and its Applications, 67:169–193, 1985.
- 30. R. Polyak. Modiﬁed barrier functions: Theory and methods. Mathematical Programming, 54:177–222, 1992.
- 31. M. Stingl. On the Solution of Nonlinear Semideﬁnite Programs by Augmented Lagrangian Methods. PhD thesis, Institute of Applied Mathematics II, Friedrich-Alexander University of Erlangen-Nuremberg, 2006.
- 32. D. Sun, J. Sun, and L. Zhang. The rate of convergence of the augmented lagrangian method for nonlinear semideﬁnite programming. Math. Pogram., 114(2):349–391, 2008.
- 33. R. Werner and K. Scho¨ttle. Calibration of correlation matrices—SDP or not SDP. Technical report,


2007. Available at http://gloria-mundi.com.

