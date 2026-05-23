## arXiv:1508.04874v2[cs.DS]5Nov2015

### A Faster Cutting Plane Method and its Implications for Combinatorial and Convex Optimization

Yin Tat Lee MIT yintat@mit.edu

Aaron Sidford MIT sidford@mit.edu

Sam Chiu-wai Wong UC Berkeley samcwong@berkeley.edu

Abstract

In this paper we improve upon the running time for ﬁnding a point in a convex set given a separation oracle. In particular, given a separation oracle for a convex set K ⊂ Rn that is contained in a box of radius R we show how to either compute a point in K or prove that K does not contain a ball of radius using an expected O(nlog(nR/ )) evaluations of the oracle and additional time O(n3 logO(1)(nR/ )). This matches the oracle complexity and improves upon the O(nω+1 log(nR/ )) additional time of the previous fastest algorithm achieved over 25 years ago by Vaidya [103] for the current value of the matrix multiplication constant ω < 2.373 [110, 41] when R/  = O(poly(n)).

Using a mix of standard reductions and new techniques we show how our algorithm can be used to improve the running time for solving classic problems in continuous and combinatorial optimization. In particular we provide the following running time improvements:

- • Submodular Function Minimization: let n be the size of the ground set, M be the maximum absolute value of function values, and EO be the time for function evaluation. Our weakly and strongly polynomial time algorithms have a running time of O(n2 log nM · EO + n3 logO(1) nM) and O(n3 log2 n · EO + n4 logO(1) n), improving upon the previous best of O((n4 · EO + n5)log M) and O(n5 · EO + n6) respectively.
- • Matroid Intersection: let n be the size of the ground set, r be the maximum size of independent sets, M be the maximum absolute value of element weight, and Trank and Tind be the time for each rank and independence oracle query. We obtain a running time of O(nrTrank log nlog(nM)+n3 logO(1) nM) and O(n2Tind log(nM)+ n3 logO(1) nM), achieving the ﬁrst quadratic bound on the query complexity for the independence and rank oracles. In the unweighted case, this is the ﬁrst improvement since 1986 for independence oracle.
- • Submodular Flow: let n and m be the number of vertices and edges, C be the maximum edge cost in absolute value, and U be the maximum edge capacity in absolute value. We obtain a faster weakly polynomial running time of O(n2 log nCU·EO+n3 logO(1) nCU), improving upon the previous best of O(mn5 log nU · EO) and O n4hmin{log C,log U} from 15 years ago by a factor of O˜(n4). We also achieve faster strongly polynomial time algorithms as a consequence of our result on submodular minimization.
- • Semideﬁnite Programming: let n be the number of constraints, m be the number of dimensions and S be the total number of non-zeros in the constraint matrix. We obtain a running time of O˜(n(n2 + mω + S)), improving upon the previous best of O˜(n(nω + mω + S)) for the regime S is small.


#### Contents

###### Overview 4

###### 1 Introduction 4

- 1.1 Paper Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2 Overview of Our Results 5

- 2.1 Cutting Plane Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5


- 2.2 Convex Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
- 2.3 Submodular Function Minimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8


###### 3 Preliminaries 8

- 3.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
- 3.2 Separation Oracles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9


- I A Faster Cutting Plane Method 10

- 4 Introduction 10

- 4.1 Previous Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
- 4.2 Challenges in Improving Previous Work . . . . . . . . . . . . . . . . . . . . . . . . . 12
- 4.3 Our Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
- 4.4 Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14


- 5 Preliminaries 14

- 5.1 Leverage Scores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
- 5.2 Hybrid Barrier Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15


- 6 Our Cutting Plane Method 15

- 6.1 Centering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
- 6.2 Changing Constraints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
- 6.3 Hybrid Center Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
- 6.4 The Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
- 6.5 Guarantees of the Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33


- 7 Technical Tools 38


- 7.1 Estimating Changes in Leverage Scores . . . . . . . . . . . . . . . . . . . . . . . . . 38
- 7.2 The Stochastic Chasing 0 Game . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42


- II A User’s Guide to Cutting Plane Methods 45


###### 8 Introduction 45

- 8.1 Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
- 8.2 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
- 8.3 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50


###### 9 Preliminaries 50

- 10 Convex Optimization 53

- 10.1 From Feasibility to Optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
- 10.2 Duality and Semideﬁnite Programming . . . . . . . . . . . . . . . . . . . . . . . . . . 55


- 11 Intersection of Convex Sets 60

- 11.1 The Technique . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
- 11.2 Matroid Intersection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
- 11.3 Submodular Flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
- 11.4 Aﬃne Subspace of Convex Set . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69


- III Submodular Function Minimization 71


- 12 Introduction 71

- 12.1 Previous Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
- 12.2 Our Results and Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
- 12.3 Organization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74


- 13 Preliminaries 74

- 13.1 Submodular Function Minimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
- 13.2 Lov´sz Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
- 13.3 Polyhedral Aspects of SFM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76


- 14 Improved Weakly Polynomial Algorithms for SFM 77
- 15 Improved Strongly Polynomial Algorithms for SFM 80

- 15.1 Improved Oracle Complexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
- 15.2 Technical Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

- 15.2.1 SFM over Ring Family . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
- 15.2.2 Identifying New Valid Arcs . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83


- 15.3 O(n4 · EO + n5) Time Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87

- 15.3.1 Consolidating A and f . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
- 15.3.2 Deducing New Constraints xi = 0, xj = 1, xi = xj or xi ≤ xj . . . . . . . . . 89
- 15.3.3 Running Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95


- 15.4 O(n3 · EO + n4) Time Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95


- 15.4.1 Partitioning Ground Set into Buckets . . . . . . . . . . . . . . . . . . . . . . 96
- 15.4.2 Separating Hyperplane: Project and Lift . . . . . . . . . . . . . . . . . . . . . 97
- 15.4.3 Deducing New Constraints xi = 0, xj = 1, xi = xj or xi ≤ xj . . . . . . . . . 99
- 15.4.4 Running Time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102


- 16 Discussion and Comparison with Previous Algorithms 103 16.1 Open Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104


Part

# Overview

#### 1 Introduction

The ellipsoid method and more generally, cutting plane methods,1 that is optimization algorithms which iteratively call a separation oracle, have long been central to theoretical computer science. In combinatorial optimization, since Khachiyan’s seminal result in 1980 [65] proving that the ellipsoid method solves linear programs in polynomial time, the ellipsoid method has been crucial to solving discrete problems in polynomial time [49]. In continuous optimization, cutting plane methods have long played a critical role in convex optimization, where they are fundamental to the theory of non-smooth optimization [45].

Despite the key role that cutting plane methods have played historically in both combinatorial and convex optimization, over the past two decades progress on improving both the theoretical running time of cutting plane methods as well as the complexity of using cutting plane methods for combinatorial optimization has stagnated.2 The theoretical running time of cutting plane methods for convex optimization has not been improved since the breakthrough result by Vaidya in 1989 [103, 105]. Moreover, for many of the key combinatorial applications of ellipsoid method, such as submodular minimization, matroid intersection and submodular ﬂow, the running time improvements over the past two decades have been primarily combinatorial; that is they have been achieved by discrete algorithms that do not use numerical machinery such as cutting plane methods.

In this paper we make progress on these classic optimization problems on two fronts. First we show how to improve on the running time of cutting plane methods for a broad range of parameters that arise frequently in both combinatorial applications and convex programming (Part I). Second, we provide several frameworks for applying the cutting plane method and illustrate the eﬃcacy of these frameworks by obtaining faster running times for semideﬁnite programming, matroid intersection, and submodular ﬂow (Part II). Finally, we show how to couple our approach with the problem speciﬁc structure and obtain faster weakly and strongly polynomial running times for submodular function minimization, a problem of tremendous importance in combinatorial optimization (Part III). In both cases our algorithms are faster than previous best by a factor of roughly Ω(n2).

We remark that many of our running time improvements come both from our faster cutting method and from new careful analysis of how to apply these cutting plane methods. In fact, simply using our reductions to cutting plane methods and a seminal result of Vaidya [103, 105] on cutting plane methods we provide running times for solving many of these problems that improves upon the previous best stated. As such, we organized our presentation to hopefully make it easy to apply cutting plane methods to optimization problems and obtain provable guarantees in the future.

Our results demonstrate the power of cutting plane methods in theory and possibly pave the way for new cutting plane methods in practice. We show how cutting plane methods can continue to improve running times for classic optimization problems and we hope that these methods may ﬁnd further use. As cutting plane methods such as analytic cutting plane method [43, 10, 44, 87, 111, 45] are frequently used in practice [48, 42], these techniques may have further implications.

- 1Throughout this paper our focus is on algorithms for polynomial time solvable convex optimization problems

given access to a linear separation oracle. Our usage of the term cutting plane methods, should not be confused with work on integer programming, an NP-hard problem.

- 2There are exceptions to this trend. For example, [70] showed how to apply cutting plane methods to yield running


time improvements for semideﬁnite programming, and recently [15] showed how to use cutting plane methods to obtain an optimal result for smooth optimization problems.

###### 1.1 Paper Organization

After providing an overview of our results (Section 2) and preliminary information and notation used throughout the paper (Section 3), we split the remainder of the paper into three parts:

- • In Part I we provide our new cutting plane method.
- • In Part II we provide several general frameworks for using this cutting plane method and illustrate these frameworks with applications in combinatorial and convex optimization.
- • In Part III we then consider the more speciﬁc problem of submodular function minimization and show how our methods can be used to improve the running time for both strongly and weakly polynomial time algorithms.


We aim to make each part relatively self contained. While each part builds upon the previous and the problems considered in each part are increasingly speciﬁc, we present the key results in each section in a modular way so that they may be read in any order. The dependencies between the diﬀerent parts of our paper are characterized by the following:

- • Part I presents our faster cutting plane method as Theorem 31.
- • Part II depends only on Theorem 31 of Part I and presents a general running time guarantee for convex optimization problems as Theorem 42.
- • The faster weakly polynomial time algorithm in Part III depends only on Theorem 42, Part II.
- • The faster strongly polynomial time algorithm in Part III depends only on Theorem 31, Part I.


2 Overview of Our Results

Here we brieﬂy summarize the contributions of our paper. For each of Part I, Part II, and Part III we describe the key technical contributions and present the running time improvements achieved.

###### 2.1 Cutting Plane Methods

The central problem we consider in Part I is as follows. We are promised that a set K is contained a box of radius R and a separation oracle that given a point  x in time SO either outputs that  x is in K or outputs a separating hyperplane. We wish to either ﬁnd a point in K or prove that K does not contain an ball of radius . The running times for this problem are given in Table 1.

|Year|Algorithm<br><br>|Complexity|
|---|---|---|


|1979|Ellipsoid Method [97, 112, 65]<br><br>|O(n2SOlog κ + n4 log κ)|
|---|---|---|
|1988<br><br>|Inscribed Ellipsoid [66, 88]|O(nSOlog κ + (nlog κ)4.5)|
|1989<br><br>|Volumetric Center [103]|O(nSOlog κ + n1+ω log κ)|
|1995|Analytic Center [10]<br><br>|O(nSOlog2 κ + nω+1 log2 κ + (nlog κ)2+ω/2)|
|2004<br><br>|Random Walk [13]<br><br>|→ O(nSOlog κ + n7 log κ)|
|2013|This paper<br><br>|O(nSOlog κ + n3 logO(1) κ)|


Table 1: Algorithms for the Feasibility Problem. κ indicates nR/ . The arrow, →, indicates that it solves a more general problem where only a membership oracle is given.

In Part I we show how to solve this problem in O(nSOlog(nR/ ) + n3 logO(1)(nR/ )) time. This is an improvement over the previous best running time of O(nSOlog(nR/ )+nω+1 log(nR/ )) for the current best known bound of ω < 2.37 [41] assuming that R/  = O(poly(n)), a common assumption for many problems in combinatorial optimization and numerical analysis as we ﬁnd in Part II and Part III. (See Table 1 for a summary of previous running times.)

Our key idea for achieving this running time improvement is a new straightforward technique for providing low variance unbiased estimates for changes in leverage scores that we hope will be of independent interest (See Section 7.1). We show how to use this technique along with ideas from [10, 104, 76] to decrease the O(nω+1 log(D/ )) overhead in the previous fastest algorithm [103].

###### 2.2 Convex Optimization

- In Part II we provide two techniques for applying our cutting plane method (and cutting plane methods in general) to optimization problems and provide several applications of these techniques.


The ﬁrst technique concerns reducing the number of dimensions through duality. For many problems, their dual is signiﬁcantly simpler than itself (primal). We use semideﬁnite programming as a concrete example to show how to improve upon the running time for ﬁnding both primal and dual solution by using the cutting planes maintained by our cutting plane method. (See Table 2.)

The second technique concerns how to minimize a linear function over the intersection of convex sets using optimization oracle. We analyze a simple potential function which allows us to bypass the typical reduction between separation and optimization to achieve faster running times. This reduction provides an improvement over the reductions used previously in [49]. Moroever, we show how this technique allows us to achieve improved running times for matroid intersection and minimum cost submodular ﬂow. (See Tables 2, 3, 4, and 5 for running time summaries.)

|Authors|Years<br><br>|Running times|
|---|---|---|


|Nesterov, Nemirovsky[89]|1992|O˜(√m(nmω + nω−1m2))<br><br>|
|---|---|---|
|Anstreicher [7]|2000|O˜((mn)1/4(nmω + nω−1m2))|
|Krishnan, Mitchell [70]|2003<br><br>|O˜(n(nω + mω + S)) (dual SDP)|
|This paper|2015|O˜(n(n2 + mω + S))|


Table 2: Algorithms for solving a m × m SDP with n constraints and S non-zero entries

|Authors|Years<br><br>|Complexity|
|---|---|---|


|Edmonds [26]|1968<br><br>|not stated|
|---|---|---|
|Aigner, Dowling [2]<br><br>|1971<br><br>|O(nr2Tind)|
|Tomizawa, Iri [102]|1974|not stated|
|Lawler [72]<br><br>|1975|O(nr2Tind)|
|Edmonds [28]<br><br>|1979<br><br>|not stated|
|Cunningham [21]<br><br>|1986|O(nr1.5Tind)|
|This paper<br><br>|2015|O(n2 log nTind + n3 logO(1) n) O(nr log2 nTrank + n3 logO(1) n)|


- Table 3: Algorithms for (unweighted) matroid intersection. n is the size of the ground set, r is the maximum rank of the two matroids, Tind is the time to check if a set is independent (membership oracle), and Trank is the time to compute the rank of a given set (rank oracle).


|Authors<br><br>|Years<br><br>|Running times|
|---|---|---|


|Edmonds [26]|1968<br><br>|not stated|
|---|---|---|
|Tomizawa, Iri [102]|1974|not stated|
|Lawler [72]<br><br>|1975|O(nr2Tind + nr3)|
|Edmonds [28]|1979|not stated|
|Frank [33]|1981<br><br>|O(n2r(Tcircuit + n))|
|Orlin, Ahuja [91]<br><br>|1983|not stated|
|Brezovec, Cornu´ejols, Glover[14]<br><br>|1986|O(nr(Tcircuit + r + log n))|
|Fujishige, Zhang [39]<br><br>|1995|O(n2r0.5 log rM · Tind)|
|Shigeno, Iwata [96]|1995|O((n + Tcircuit)nr0.5 log rM)|
|This paper<br><br>|2015|O(n2 log nMTind + n3 logO(1) nM) O(nr log nlog nMTrank + n3 logO(1) nM)|


###### Table 4: Algorithms for weighted matroid intersection. In addition to the notation in Table 3 Tcircuit is the time needed to ﬁnd a fundamental circuit and M is the bit complexity of the weights.

|Authors<br><br>|Years|Running times|
|---|---|---|


|Fujishige [35]|1978<br><br>|not stated|
|---|---|---|
|Grotschel, Lovasz, Schrijver[49]<br><br>|1981|weakly polynomial|
|Zimmermann [113]<br><br>|1982|not stated|
|Barahona, Cunningham [12]<br><br>|1984|not stated|
|Cunningham, Frank [22]<br><br>|1985|→ O(n4hlog C)|
|Fujishige [36]|1987|not stated|
|Frank, Tardos [34]|1987<br><br>|strongly polynomial|
|Cui, Fujishige [108]|1988|not stated|
|Fujishige, R¨ck, Zimmermann[38]<br><br>|1989|→ O(n6hlog n)|
|Chung, Tcha [18]<br><br>|1991|not stated|
|Zimmermann [114]|1992<br><br>|not stated|
|McCormick, Ervolina [82]<br><br>|1993|O(n7h∗ log nCU)|
|Wallacher, Zimmermann [109]|1994<br><br>|O(n8hlog nCU)|
|Iwata [52]|1997<br><br>|O(n7hlog U)|
|Iwata, McCormick, Shigeno [57]<br><br>|1998|O n4hmin log nC,n2 log n|
|Iwata, McCormick, Shigeno [58]<br><br>|1999<br><br>|O n6hmin log nU,n2 log n|
|Fleischer, Iwata, McCormick[32]|1999<br><br>|O n4hmin log U,n2 log n|
|Iwata, McCormick, Shigeno [59]<br><br>|1999<br><br>|O n4hmin log C,n2 log n|
|Fleischer, Iwata [30]|2000<br><br>|O(mn5 log nU · EO)|
|This paper<br><br>|2015|O(n2 log nCU · EO + n3 logO(1) nCU)|


###### Table 5: Algorithms for minimum cost submodular ﬂow with n vertices, maximum cost C and maximum capacity U. The factor h is the time for an exchange capacity oracle, h∗ is the time for a “more complicated exchange capacity oracle,” and EO is the time for evaluation oracle of the submodular function. The arrow, →, indicates that it uses the current best submodular ﬂow algorithm as subroutine which was non-existent at the time of the publication.

###### 2.3 Submodular Function Minimization

- In Part III we consider the problem of submodular minimization, a fundamental problem in combinatorial optimization with many diverse applications in theoretical computer science, operations research, machine learning and economics. We show that by considering the interplay between the guarantees of our cutting plane algorithm and the primal-dual structure of submodular minimization we can achieve improved running times in various settings.


First, we show that a direct application of our method yields an improved weakly polynomial time algorithm for submodular minimization. Then, we present a simple geometric argument that submodular function can be solved with O(n3 log n · EO) oracle calls but with exponential running time. Finally, we show that by further studying the combinatorial structure of submodular minimization and a modiﬁcation to our cutting plane algorithm we can obtained a fully improved strongly polynomial time algorithm for submodular minimization. We summarize the improvements in Table 6.

|Authors<br><br>|Years|Running times<br><br>|Remarks|
|---|---|---|---|


|Gr¨tschel, Lov´sz, Schrijver [49, 50]|1981,1988|O(n5 · EO + n7) [81]<br><br>|ﬁrst weakly and strongly<br><br>|
|---|---|---|---|
|Cunningham [20]|1985<br><br>|O(Mn6 log nM · EO)|ﬁrst combin. pseudopoly|
|Schrijver [93]|2000|O(n8 · EO + n9)<br><br>|ﬁrst combin. strongly|
|Iwata, Fleischer, Fujishige[56]<br><br>|2000|O(n5 · EOlog M) O(n7 log n · EO)<br><br>|ﬁrst combin. strongly|
|Iwata, Fleischer [31]<br><br>|2000|O(n7 · EO + n8)| |
|Iwata [54]|2003<br><br>|O((n4 · EO + n5)log M) O((n6 · EO + n7)log n)|current best weakly|
|Vygen [107]<br><br>|2003|O(n7 · EO + n8)| |
|Orlin [90]|2007<br><br>|O(n5 · EO + n6)|current best strongly|
|Iwata, Orlin [60]<br><br>|2009|O((n4 · EO + n5)log nM)<br>O((n5 · EO + n6)log n)<br>| |
|Our algorithms<br><br>|2015|O(n2 log nM · EO + n3 logO(1) nM)<br>O(n3 log2 n · EO + n4 logO(1) n)<br>| |


Table 6: Algorithms for submodular function minimization.

- 3 Preliminaries Here we introduce notation and concepts we use throughout the paper.


###### 3.1 Notation

Basics: Throughout this paper, we use vector notation, e.g  x = (x1,...,xn), to denote a vector and bold, e.g. A, to denote a matrix. We use nnz( x) or nnz(A) to denote the number of nonzero entries in a vector or a matrix respectively. Frequently, for  x ∈ Rd we let X ∈ Rd×d denote diag( x), the diagonal matrix such that Xii = xi. For a symmetric matrix, M, we let diag(M) denote the vector corresponding to the diagonal entries of M, and for a vector,  x, we let  x M def=

√

 xTM x.

Running Times: We typically use XO to denote the running time for invoking the oracle, where X depends on the type of oracle, e.g., SO typically denotes the running time of a separation oracle, EO denotes the running time of an evaluation oracle, etc. Furthermore, we use O(f) def= O(f logO(1) f).

Spectral Approximations: For symmetric matrices N,M ∈ Rn×n, we write N M to denote that  xTN x ≤  xTM x for all  x ∈ Rn and we deﬁne N M, N ≺ M and N M analogously.

Standard Convex Sets: We let Bp(r) def= { x :  x p ≤ r} denote a ball of radius r in the p norm. For brevity we refer to B2(r) as a a ball of radius r and B∞(r) as a box of radius r.

Misc: We let ω < 2.373 [110] denote the matrix multiplication constant.

###### 3.2 Separation Oracles

Throughout this paper we frequently make assumptions about the existence of separation oracles for sets and functions. Here we formally deﬁne these objects as we use them throughout the paper. Our deﬁnitions are possibly non-standard and chosen to handle the diﬀerent settings that occur in this paper.

- Deﬁnition 1 (Separation Oracle for a Set). Given a set K ⊂ Rn and δ ≥ 0, a δ-separation oracle for K is a function on Rn such that for any input  x ∈ Rn, it either outputs “successful” or a half

space of the form H = {z  :  cTz  ≤  cT x + b} ⊇ K with b ≤ δ  c 2 and  c = 0. We let SOδ(K) be the time complexity of this oracle.

For brevity we refer to a 0-separation oracle for a set as just a separation oracle. We refer to the hyperplanes deﬁning the halfspaces returned by a δ-separation oracle as oracle hyperplanes.

Note that in Deﬁnition 1 we do not assume that K is convex. However, we remark that it is well known that there is a separation oracle for a set if and only if it is convex and that there is a δ separation oracle if and only if the set is close to convex in some sense.

- Deﬁnition 2 (Separation Oracle for a Function). For any convex function f, η ≥ 0 and δ ≥ 0, a (η,δ)-separation oracle on a convex set Γ for f is a function on Rn such that for any input  x ∈ Γ, it either asserts f( x) ≤ min y∈Γ f( y) + η or outputs a half space H such that


{z  ∈ Γ : f(z ) ≤ f( x)} ⊂ H def= {z  :  cTz  ≤  cT x + b} (3.1) with b ≤ δ  c and  c = 0. We let SOη,δ(f) be the time complexity of this oracle.

Part I

# A Faster Cutting Plane Method

- 4 Introduction Throughout Part I we study the following feasibility problem:


- Deﬁnition 3 (Feasibility Problem). Given a separation oracle for a set K ⊆ Rn contained in a box of radius R either ﬁnd a point  x ∈ K or prove that K does not contain a ball of radius .


This feasibility problem is one of the most fundamental and classic problems in optimization. Since the celebrated result of Yudin and Nemirovski [112] in 1976 and Khachiyan [65] in 1979 essentially proving that it can be solved in time O(poly(n) · SO · log(R/ )), this problem has served as one of the key primitives for solving numerous problems in both combinatorial and convex optimization.

Despite the prevalence of this feasibility problem, the best known running time for solving this problem has not been improved in over 25 years. In a seminal paper of Vaidya in 1989 [103], he showed how to solve the problem in O(n·SO·log(nR/ )+nω+1 log(nR/ )) time. Despite interesting generalizations and practical improvements [5, 92, 43, 10, 44, 87, 111, 45, 15], the best theoretical guarantees for solving this problem have not been improved since.

In Part I we show how to improve upon Vaidya’s running time in certain regimes. We provide a cutting plane algorithm which achieves an expected running time of O(n · SO · log(nR/ ) + n3 logO(1)(nR/ )), improving upon the previous best known running time for the current known value of ω < 2.373 [110, 41] when R/  = O(poly(n)).

We achieve our results by the combination of multiple techniques. First we show how to use techniques from the work of Vaidya and Atkinson to modify Vaidya’s scheme so that it is able to tolerate random noise in the computation in each iteration. We then show how to use known numerical machinery [104, 99, 76] in combination with some new techniques (Section 7.1 and Section 7.2) to implement each of these relaxed iterations eﬃciently. We hope that both these numerical techniques as well as our scheme for approximating complicated methods, such as Vaidya’s, may ﬁnd further applications.

While our paper focuses on theoretical aspects of cutting plane methods, we achieve our results via the careful application of practical techniques such as dimension reduction and sampling. As such we hope that ideas in this paper may lead to improved practical3 algorithms for non-smooth optimization.

###### 4.1 Previous Work

Throughout this paper, we restrict our attention to algorithms for the feasibility problem that have a polynomial dependence on SO, n, and log(R/ ). Such “eﬃcient” algorithms typically follow the following iterative framework. First, they compute some trivial region Ω that contains K. Then, they call the separation oracle at some point  x ∈ Ω. If  x ∈ K the algorithm terminates having successfully solved the problem. If  x ∈/ K then the separation oracle must return a half-space

3Although cutting plane methods are often criticized for their empirical performance, recently, Bubeck, Lee and Singh [15] provided a variant of the ellipsoid method that achieves the same convergence rate as Nesterov’s accelerated gradient descent. Moreover, they provided numerical evidence that this method can be superior to Nesterov’s accelerated gradient descent, thereby suggesting that cutting plane methods can be as aggressive as ﬁrst order methods if designed properly.

|Year<br><br>|Algorithm|Complexity|
|---|---|---|


|1979|Ellipsoid Method [97, 112, 65]|O(n2SOlog κ + n4 log κ)|
|---|---|---|
|1988|Inscribed Ellipsoid [66, 88]<br><br>|O(nSOlog κ + (nlog κ)4.5)|
|1989<br><br>|Volumetric Center [103]|O(nSOlog κ + n1+ω log κ)|
|1995|Analytic Center [10]<br><br>|O<br><br>nSOlog2 κ + nω+1 log2 κ +(nlog κ)2+ω/2|
|2004|Random Walk [13]<br><br>|→ O(nSOlog κ + n7 log κ)|
|2013<br><br>|This paper|O(nSOlog κ + n3 logO(1) κ)|


Table 7: Algorithms for the Feasibility Problem. κ indicates nR/ . The arrow, →, indicates that it solves a more general problem where only a membership oracle is given.

containing K. The algorithm then uses this half-space to shrink the region Ω while maintaining the invariant that K ⊆ Ω. The algorithm then repeats this process until it ﬁnds a point  x ∈ K or the region Ω becomes too small to contain a ball with radius .

Previous works on eﬃcient algorithms for the feasibility problem all follow this iterative framework. They vary in terms of what set Ω they maintain, how they compute the center to query the separation oracle, and how they update the set. In Table 7, we list the previous running times for solving the feasibility problem. As usual SO indicates the cost of the separation oracle. To simplify the running times we let κ def= nR/ . The running times of some algorithms in the table depend on R/  instead of nR/ . However, for many situations, we have log(R/ ) = Θ(log(nR/ )) and hence we believe this is still a fair comparison.

The ﬁrst eﬃcient algorithm for the feasibility problem is the ellipsoid method, due to Shor [97], Nemirovksii and Yudin [112], and Khachiyan [65]. The ellipsoid method maintains an ellipsoid as Ω and uses the center of the ellipsoid as the next query point. It takes Θ(n2 log κ) calls of oracle which is far from the lower bound Ω(nlog κ) calls [86].

To alleviate the problem, the algorithm could maintain all the information from the oracle, i.e., the polytope created from the intersection of all half-spaces obtained. The center of gravity method [77] achieves the optimal oracle complexity using this polytope and the center of gravity of this polytope as the next point. However, computing center of gravity is computationally expensive and hence we do not list its running time in Table 7. The Inscribed Ellipsoid Method [66] also achieved an optimal oracle complexity using this polytope as Ω but instead using the center of the maximal inscribed ellipsoid in the polytope to query the separation oracle. We listed it as occurring in year 1988 in Table 7 because it was [88] that yielded the ﬁrst polynomial time algorithm to actually compute this maximal inscribed ellipsoid for polytope.

Vaidya [103] obtained a faster algorithm by maintaining an approximation of this polytope and using a diﬀerent center, namely the volumetric center. Although the oracle complexity of this volumetric center method is very good, the algorithm is not extremely eﬃcient as each iteration involves matrix inversion. Atkinson and Vaidya [10] showed how to avoid this computation in certain settings. However, they were unable to achieve the desired convergence rate from their method.

Bertsimas and Vempala [13] also gives an algorithm that avoids these expensive linear algebra operations while maintaining the optimal convergence rate by using techniques in sampling convex sets. Even better, this result works for a much weaker oracle, the membership oracle. However, the additional cost of this algorithm is relatively high in theory. We remark that while there are considerable improvemenst on the sampling techniques [79, 63, 76], the additional cost is still quite high compared to standard linear algebra.

###### 4.2 Challenges in Improving Previous Work

Our algorithm builds upon the previous fastest algorithm of Vaidya [105]. Ignoring implementation details and analysis, Vaidya’s algorithm is quite simple. This algorithm simply maintains a polytope P(k) = {x ∈ Rn : A x − b ≥ 0} as the current Ω and uses the volumetric center, the minimizer of the following volumetric barrier function

- 1

- 2


log det ATS x−2A where S x def= diag(A x − b) (4.1)

arg min

 x

as the point at which to query the separation oracle. The polytope is then updated by adding shifts of the half-spaces returned by the separation oracle and dropping unimportant constraints. By choosing the appropriate shift, picking the right rule for dropping constraints, and using Newton’s method to compute the volumetric center he achieved a running time of O(n·SO·log κ+n1+ω log κ).

While Vaidya’s algorithm’s dependence on SO is essentially optimal, the additional per-iteration costs of his algorithm could possibly be improved. The computational bottleneck in each iteration of Vaidya’s algorithm is computing the gradient of log det which in turn involves computing the leverage scores  σ( x) def= diag(S−x1A ATS−x2A −1 ATS−x1), a commonly occurring quantity in numerical analysis and convex optimization [99, 19, 78, 76, 75]. As the best known algorithms for computing leverage scores exactly in this setting take time O(nω), directly improving the running time of Vaidya’s algorithm seems challenging.

However, since an intriguing result of Spielman and Srivastava in 2008 [99], it has been well known that using Johnson-Lindenstrauss transform these leverage scores can be computed up to a multiplicative (1 ± ) error by solving O( −2 log n) linear systems involving ATS−x2A. While in general this still takes time O( −2nω), there are known techniques for eﬃciently maintaining the inverse of a matrix so that solving linear systems take amortized O(n2) time [104, 75, 76]. Consequently if it could be shown that computing approximate leverage scores suﬃced, this would potentially decrease the amortized cost per iteration of Vaidya’s method.

Unfortunately, Vaidya’s method does not seem to tolerate this type of multiplicative error. If leverage scores were computed this crudely then in using them to compute approximate gradients for (4.1), it seems that any point computed would be far from the true center. Moreover, without being fairly close to the true volumetric center, it is diﬃcult to argue that such a cutting plane method would make suﬃcient progress.

To overcome this issue, it is tempting to directly use recent work on improving the running time of linear program [75]. In this work, the authors faced a similar issue where a volumetric, i.e. log det, potential function had the right analytic and geometric properties, however was computational expensive to minimize. To overcome this issue the authors instead computed a weighted analytic center:

wi log si( x) where  s( x) def= A x − b .

−

arg min

 x

i∈[m]

For carefully chosen weights this center provides the same convergence guarantees as the volumetric potential function, while each step can be computed by solving few linear systems (rather than forming the matrix inverse).

Unfortunately, it is unclear how to directly extend the work in [75] on solving an explicit linear program to the feasibility problem speciﬁed by a separation oracle. While it is possible to approximate the volumetric barrier by a weighted analytic center in many respects, proving that this approximation suﬃces for fast convergence remains open. In fact, the volumetric barrier

function as used in Vaidya’s algorithm is well approximated simply by the standard analytic center arg min

log si( x) where  s( x) def= A x − b .

−

 x

i∈[m]

- as all the unimportant constraints are dropped during the algorithm. However, despite decades of research, the best running times known for solving the feasibility problem using the analytic center are Vaidya and Atkinson algorithm from 1995 [10]. While the running time of this algorithm could possibly be improved using approximate leverage score computations and amortized eﬃcient linear system solvers, unfortunately at best, without further insight this would yield an algorithm which requires a suboptimal O(nlogO(1) κ) queries to the separation oracle.


As pointed out in [10], the primary diﬃculty in using any sort of analytic center is quantifying the amount of progress made in each step. We still believe providing direct near-optimal analysis of weighted analytic center is a tantalizing open question warranting further investigation. However, rather than directly address the question of the performance of weighted analytic centers for the feasibility problem, we take a slightly diﬀerent approach that side-steps this issue. We provide a partial answer that still sheds some light on the performance of the weighted analytic center while still providing our desired running time improvements.

###### 4.3 Our Approach

To overcome the shortcoming of the volumetric and analytic centers we instead consider a hybrid barrier function

wi log si( x) + log det(ATS−x1A) where  s( x) def= A x − b .

−

arg min

 x

i∈[m]

for careful chosen weights. Our key observation is that for correct choice of weights, we can compute the gradient of this potential function. In particular if we let w  = τ  −  σ( x) then the gradient of this potential function is the same as the gradients of i∈[m] τi log si( x), which we can compute eﬃciently. Moreover, since we are using log det, we can use analysis similar to Vaidya’s algorithm [103] to analyze the convergence rate of this algorithm.

Unfortunately, this is a simple observation and does not immediately change the problem substantially. It simply pushes the problem of computing gradients of log det to computing w . Therefore, for this scheme to work, we would need to ensure that the weights do not change too much and that when they change, they do not signiﬁcantly hurt the progress of our algorithm. In other words, for this scheme to work, we would still need very precise estimates of leverage scores.

However, we note that the leverage scores  σ( x) do not change too much between iterations. Moreover, we provide what we believe is an interesting technical result that an unbiased estimates to the changes in leverage scores can be computed using linear system solvers such that the total error of the estimate is bounded by the total change of the leverage scores (See Section 7.1). Using this result our scheme simply follows Vaidya’s basic scheme in [103], however instead of minimizing the hybrid barrier function directly we alternate between taking Newton steps we can compute, changing the weights so that we can still compute Newton steps, and computing accurate unbiased estimates of the changes in the leverage scores so that the weights do not change adversarially by too much.

To make this scheme work, there are two additional details that need to be dealt with. First, we cannot let the weights vary too much as this might ultimately hurt the rate of progress of our algorithm. Therefore, in every iteration we compute a single leverage score to high precision to

control the value of wi and we show that by careful choice of the index we can ensure that no weight gets too large (See Section 7.2).

Second, we need to show that changing weights does not aﬀect our progress by much more than the progress we make with respect to log det. To do this, we need to show the slacks are bounded above and below. We enforce this by adding regularization terms and instead consider the potential function

- 1

- 2


λ 2

x 22

log det ATS−x2A + λI +

p e( x) = −

wi log si( x) +

i∈[m]

This allows us to ensure that the entries of  s( x) do not get too large or too small and therefore changing the weighting of the analytic center cannot aﬀect the function value too much.

Third, we need to make sure our potential function is convex. If we simply take w  = τ  −  σ( x) with τ  as an estimator of  σ( x), w  can be negative and the potential function could be non-convex. To circumvent this issue, we use w  = ce + τ  −  σ( x) and make sure τ  −  σ( x) ∞ < ce.

Combining these insights, using eﬃcient algorithms for solving a sequence of slowly changing linear systems [104, 75, 76], and providing careful analysis ultimately allows us to achieve a running time of O(nSOlog κ+n3 logO(1) κ) for the feasibility problem. Furthermore, in the case that K does not contain a ball of radius , our algorithm provides a proof that the polytope does not contain a ball of radius . This proof ultimately allows us to achieve running time improvements for strongly polynomial submodular minimization in Part III.

###### 4.4 Organization

The rest of Part I is organized as follows. In Section 5 we provide some preliminary information and notation we use throughout Part I. In Section 6 we then provide and analyze our cutting plane method. In Section 7 we provide key technical tools which may be of independent interest.

##### 5 Preliminaries Here we introduce some notation and concepts we use throughout Part I.

###### 5.1 Leverage Scores

Our algorithms in this section make extensive use of leverage scores, a common measure of the importance of rows of a matrix. We denote the leverage scores of a matrix A ∈ Rn×d by  σ ∈ Rn and say the leverage score of row i ∈ [n] is σi def= [A ATA −1 AT]ii. For A ∈ Rn×d, d ∈ Rn>0, and D def= diag( d) we use the shorthand  σA( d) to denote the leverage scores of the matrix D1/2A. We frequently use well known facts regarding leverage scores, such as σi ∈ [0,1] and  σ 1 ≤ d. (See [99, 80, 78, 19] for a more in-depth discussion of leverage scores, their properties, and their many applications.) In addition, we make use of the fact that given an eﬃcient linear system solver of ATA we can eﬃciently compute multiplicative approximations to leverage scores (See Deﬁnition 4 and Lemma 5 below).

- Deﬁnition 4 (Linear System Solver). An algorithm S is a LO-time solver of a PD matrix M ∈ Rn×n if for all b ∈ Rn and ∈ (0,1/2], the algorithm outputs a vector S( b, ) ∈ Rn in time O(LO·log( −1)) such that with high probability in n, S( b, ) − M−1 b 2M ≤ M−1 b 2M.


- Lemma 5 (Computing Leverage Scores [99]). Let A ∈ Rn×d, let  σ denote the leverage scores of A, and let > 0. If we have a LO-time solver for ATA then in time O((nnz(A) + LO) −2 log( −1)) we can compute τ  ∈ Rn such that with high probability in d, (1− )σi ≤ τi ≤ (1+ )σi for all i ∈ [n].


###### 5.2 Hybrid Barrier Function

As explained in Section 4.3 our cutting plane method maintains a polytope P = { x ∈ Rn : A x ≥ b} for A ∈ Rm×n and b ∈ Rn that contains some target set K. We then maintain a minimizer of the following hybrid barrier function:

1 2

λ 2

x 22

log det ATS−x2A + λI +

p e( x) def= −

(ce + ei)log si( x) +

i∈[m]

where  e ∈ Rm is a variable we maintain, ce ≥ 0 and λ ≥ 0 are constants we ﬁx later,  s( x) def= A x− b, and Sx = diag( s( x)). When the meaning is clear from context we often use the shorthand Ax def= S−x1A.

Rather than maintaining  e explicitly, we instead maintain a vector τ  ∈ Rm that approximates the leverage score

ψ( x) def= diag Ax ATxAx + λI −1 ATx . Note that ψ( x) is simply the leverage scores of certain rows of the matrix √ Ax λI

.

and therefore the usual properties of leverage scores hold, i.e. ψi( x) ∈ (0,1) and ψi( x) 1 ≤ n. We write ψ( x) equivalently as ψAx or ψP when we want the matrix to be clear. Furthermore, we let Ψx def= diag( ψ( x)) and µ( x) def= mini ψi( x). Finally, we typically pick  e using the function  eP(τ , x) def= τ  − ψ( x). Again, we use the subscripts of Ax and P interchangeably and often drop them when the meaning is clear from context.

We remark that the last term λ2 x 22 ensures that our point is always within a certain region (Lemma 23) and hence the term (ce + ei)log si( x)i never gets too large. However, this 2 term changes the Hessian of the potential function and hence we need to put a λI term inside both the log det and the leverage score to reﬂect this. This is the reason why we use ψ instead of the standard leverage score.

- 6 Our Cutting Plane Method


In this section we develop and prove the correctness of our cutting plane method. We use the notation introduced in Section 3 and Section 5 as well as the technical tools we introduce in Section 7.

We break the presentation and proof of correctness of our cutting plane methods into multiple parts. First in Section 6.1 we describe how we maintain a center of the hybrid barrier function p e and analyze this procedure. Then, in Section 6.2 we carefully analyze the eﬀect of changing constraints on the hybrid barrier function and in Section 6.3 we prove properties of an approximate center of hybrid barrier function, which we call a hybrid center. In Section 6.4 we then provide our cutting plane method and in Section 6.5 we prove that the cutting plane method solves the feasibility problem as desired.

###### 6.1 Centering

In this section we show how to compute approximate centers or minimizers of the hybrid barrier function for the current polytope P = { x : A x ≥ b}. We split this proof up into multiple parts. First we simply bound the gradient and Hessian of the hybrid barrier function, p e, as follows.

- Lemma 6. For f( x) def= 12 log det ATS−x2A + λI , we have that

∇f( x) = −ATx ψ( x) and ATxΨ( x)Ax ∇2f( x) 3ATxΨ( x)Ax . Proof. Our proof is similar to [4, Appendix] which proved the statement when λ = 0. This case does not change the derivation signiﬁcantly, however for completeness we include the proof below.

We take derivatives on  s ﬁrst and then apply chain rule. Let f( s) = 12 log det ATS−2A + λI . We use the notation Df( x)[ h] to denote the directional derivative of f along the direction h at the point  x. Using the standard formula for the derivative of log det, i.e. dtd log detBt = Tr((Bt)−1(ddtBt)), we have

Df( s)[ h] =

- 1

- 2


Tr((ATS−2A + λI)−1(AT(−2)S−3HA)) (6.1)

= −

i

hi si

1Ti S−1A ATS−2A + λI −1 AS−1 1i = −

i

ψihi si

.

Applying chain rules, we have ∇f( x) = −ATx ψ. Now let P def= S−1A ATS−2A + λI −1 ATS−1. Taking the derivative of (6.1) again and using the cyclic property of trace, we have

D2f( s)[ h1, h2] = Tr ATS−2A + λI −1 AT(−2)S−3H2A ATS−2A + λI −1 ATS−3H1A −Tr ATS−2A + λI −1 AT(−3)S−4H2H1A

= 3Tr PS−2H2H1 − 2Tr PS−1H2PS−1H1

= 3

i

Pii

h1(i) h2(i) s2i − 2

ij

Pij

h2(j) sj

Pji

h2(i) si

= 3

i

ψi

h1(i) h2(i) s2i − 2

ij

Pij2

h2(j) sj

h2(i) si

.

Consequently, D2f( x)[ 1i, 1j] = [S−1 3Ψ − 2P(2) S−1]ij where P(2) is the Schur product of P with itself.

Now note that

i

Pij2 = 1jS−1A ATS−2A + λI −1 ATS−2A ATS−2A + λI −1 ATS−1 1j

≤ 1jS−1A ATS−2A + λI −1 ATS−1 1j = Pjj = Ψjj .

Hence, the Gershgorin circle theorem shows that the eigenvalues of Ψ − P(2) are lies in union of the interval [0,2ψj] over all j. Hence, Ψ − P(2) 0. On the other hand, Schur product theorem shows that P(2) 0 as P 0. Hence, the result follows by chain rule.

| |
|---|


Lemma 6 immediately shows that under our choice of  e =  eP( x,τ ) we can compute the gradient of the hybrid barrier function, p e( x) eﬃciently. Formally, Lemma 6 immediately implies the following:

- Lemma 7 (Gradient). For  x ∈ P = { y ∈ Rn : A y ≥ b} and  e ∈ Rm we have


∇p e( x) = −ATx(ce 1 +  e + ψP( x)) + λ x and therefore for all τ  ∈ Rm, we have

∇p e(τ , x)( x) = −ATx ce 1 + τ  + λ x.

Remark 8. To be clear, the vector ∇p e(τ , x)( x) is deﬁned as the vector such that

1 t

[∇p e(τ , x)( x)]i = lim t→0

p e(τ , x)( x + t 1i) − p e(τ , x)( x) .

In other words, we treat the parameter  e(τ , x) as ﬁxed. This is the reason we denote it by subscript to emphasize that p e( x) is a family of functions, p e(τ , x) is one particular function, and ∇p e(τ , x) means taking gradient on that particular function.

Consequently, we can always compute ∇p e(τ , x)( x) eﬃciently. Now, we measure centrality or how close we are to the hybrid center as follows. Deﬁnition 9 (Centrality). For  x ∈ P =  y ∈ Rn : A y ≥ b and  e ∈ Rm, we deﬁne the centrality of  x by

δ e( x) def= ∇p e( x)

H( x)−1

where H( x) def= ATx (ceI + Ψ( x))Ax + λI. Often, we use weights w  ∈ Rm>0 to approximate this Hessian and consider Q( x,w ) def= ATx (ceI + W)Ax + λI.

Next, we bound how much slacks can change in a region close to a nearly central point.

- Lemma 10. Let  x ∈ P =  y ∈ Rn : A y ≥ b and  y ∈ Rn such that  x −  y H( x) ≤ ce + µ( x) for < 1. Then  y ∈ P and (1 − )Sx Sy (1 + )Sx . Proof. Direct calculation reveals the following:

S−x1( s y −  sx) ∞ ≤ Ax( y −  x) 2 ≤

1 ce + µ( x)

Ax( y −  x) c

eI+Ψ( x)

≤

1 ce + µ( x)

 y −  x H( x) ≤ .

Consequently, (1 − )Sx Sy (1 + )Sx. Since y ∈ P if and only if Sy 0 the result follows. Combining the previous lemmas we obtain the following.

| |
|---|


- Lemma 11. Let  x ∈ P = { y ∈ Rn : A y ≥ b} and  e,w  ∈ Rm such that  e ∞ ≤ 12ce ≤ 1 and Ψ( x) W 3 4Ψ( x). If  y ∈ Rn satisﬁes  x −  y Q( x,w ) ≤ 101 ce + µ( x), then


- 1

- 2


1 4

Q( x,w ) ∇2p e( y) 8Q( x,w ) and

H( x) H( y) 2H( x) . Proof. Lemma 6 shows that

ATy (ceI + E + Ψ( y))Ay + λI ∇2p e( y) ATy (ceI + E + 3Ψ( y))Ay + λI . (6.2)

Since W Ψ, we have that Q( x,w ) H( x) and therefore  x− y H( x) ≤ ce + µ( x) with = 0.1. Consequently, by Lemma 10 we have (1 − )Sx Sy (1 + )Sx and therefore

(1 − )2 (1 + )2

(1 + )2 (1 − )2

Ψ( x) Ψ( y)

Ψ( x)

and

(1 − )2 (1 + )4

(1 + )2 (1 − )4

- 1

- 2


H( x)

H( x) H( y)

H( x) 2H( x)

Furthermore, (6.2) shows that ∇2p e( y) ATy (ceI + E + 3Ψ( y))Ay + λI

(1 + )2 (1 − )4

ATx (ceI + E + 3Ψ( x))Ax + λI

(1 + )2 (1 − )4

3 2

ATx

ceI + 3W Ax + λI

(1 + )2 (1 − )4

3

Q( x,w ) 8Q( x,w )

and

∇2p e( y) ATy (ceI + E + Ψ( y))Ay + λI

(1 − )4 (1 + )2

ATx (ceI + E + Ψ( x))Ax + λI

(1 − )4 (1 + )2

- 1

- 2


- 3

- 4


ATx

ceI +

###### W Ax + λI

(1 − )4 (1 + )2

- 1

- 2


1 4

Q( x,w )

Q( x,w ).

| |
|---|


To analyze our centering scheme we use standard facts about gradient descent we prove in

- Lemma 12.


- Lemma 12 (Gradient Descent). Let f : Rn → R be twice diﬀerentiable and Q ∈ Rn×n be positive


deﬁnite. Let  x0 ∈ Rn and  x1 def=  x0 − L1 Q−1∇f( x0). Furthermore, let  xα =  x0 + α( x1 −  x) and suppose that µQ ∇2f( xα) LQ for all α ∈ [0,1]. Then,

- 1. ∇f( x1) Q−1 ≤ 1 − Lµ ∇f( x0) Q−1

- 2. f( x1) ≥ f( x0) − L1 ∇f( x0) 2Q−1


Proof. Integrating we have that

∇f( x1) = ∇f( x0) + ˆ 1

∇2f( xα)( x1 −  x0)dα = ˆ 1

0

0

Consequently, by applying Jensen’s inequality we have

1 L∇2f( xα) Q−1∇f( x0)dα

Q −

∇f( x1) Q−1 = ˆ 1

1 L∇2f( xα) Q−1∇f( x0)dα

Q −

Q−1 ≤ ˆ 1

0

1 L∇2f( xα) Q−1∇f( x0)

Q −

dα

Q−1

0

≤ Q−1/2∇f( x0)

[Q−1/2(Q−L1 ∇2f( xα))Q−1/2]2 Now we know that by assumption that

µ L

1 L∇2f( xα) Q−1/2 1 −

0 Q−1/2 Q −

###### I

and therefore combining these (1) holds. Using the convexity of f, we have

f( x1) ≥ f( x0) +  ∇f( x0), x1 −  x0 ≥ f( x0) − ∇f( x0) Q−1  x1 −  x0 Q

and since  x1 −  x0 Q = L1 ∇f( x0) Q−1, (2) holds as well. Next we bound the eﬀect of changing  e on the hybrid barrier function p e( x).

- Lemma 13. For  x ∈ P = { y ∈ Rn : A y ≥ b},  e, f ∈ Rm, and w  ∈ Rm>0 such that W Ψx


1 ce + µ( x)

∇p f( x) Q( x,w )−1 ≤ ∇p e( x) Q( x,w )−1 +

f −  e 2

Proof. Direct calculation shows the following

| |
|---|


∇p f( x) Q( x,w )−1 = − ATx(ce 1 + f + ψP( x)) + λ x Q( x,w )−1 (Formula for ∇p f( x)) ≤ ∇p e( x) Q( x,w )−1 + ATx( f −  e) Q( x,w )−1 (Triangle inequality) ≤ ∇p e( x) Q( x,w )−1 +

1 ce + µ( x)

ATx( f −  e) (AT

xAx)−1 (Bound on Q( x,w ))

1 ce + µ( x)

≤ ∇p e( x) Q( x,w )−1 +

f −  e 2 (Property of projection matrix)

where in the second to third line we used Q( x,w ) H( x) (ce + µ( x))ATxAx. We now have everything we need to analyze our centering algorithm.

| |
|---|


Algorithm 1: ( x(r),τ (r)) = Centering( x(0),τ (0),r,c∆) Input: Initial point  x(0) ∈ P = { y ∈ Rn : A y ≥ b}, Estimator of leverage scores τ (0) ∈ Rn Input: Number of iterations r > 0, Accuracy of the estimator 0 ≤ c∆ ≤ 0.01ce. Given:  e(0) ∞ ≤ 13ce ≤ 13 where  e(0) =  e(τ (0), x(0)). Given: δ e(0)( x(0)) = ∇p e(0)( x(0)) H( x(0))−1 ≤ 1001 ce + µ( x(0)).

Compute w  such that Ψ( x(0)) W 43Ψ( x(0)) (See Lemma 5) Let Q def= Q( x(0),w ). for k = 1 to r do

 x(k) :=  x(k−1) − 18Q−1∇p e(k−1)( x(k−1)). Sample ∆(k) ∈ Rn s.t.

E[ ∆(k)] = ψ( x(k)) − ψ( x(k−1)) and with high probability in n,

∆(k) − ( ψ( x(k)) − ψ( x(k−1))) 2 ≤ c∆ S x−(1k−1)( s x(k) −  s x(k−1)) 2 (See Section 7.1) τ (k) := τ (k−1) + ∆(k).  e(k) :=  e(τ (k), x(k)).

end Output: ( x(r),τ (r))

- Lemma 14. Let  x(0) ∈ P = { y ∈ Rn : A y ≥ b} and let τ (0) ∈ Rm such that  e(τ (0), x(0)) ∞ ≤ 1 3ce ≤ 13. Assume that r is a positive integer, 0 ≤ c∆ ≤ 0.01ce and δ e(0)( x(0)) ≤ 1001 ce + µ( x(0)). With high probability in n, the algorithm Centering( x(0),τ (0),r,c∆) outputs ( x(r),τ (r)) such that


- 1. δ e(r)( x(r)) ≤ 2 1 − 641 r δ e(0)( x(0)).

- 2. E[p e(k)( x(r))] ≥ p e(0)( x(0)) − 8 δ e(0)( x(0)) 2 .
- 3. E e(r) =  e(0) and  e(r) −  e(0) 2 ≤ 101 c∆.

- 4. S x−(0)1 ( s( x(r)) −  s( x(0)))


≤ 101 .

2

where  e(r) =  e(τ (r), x(r)). Proof. Let η = ∇p e(0)( x(0)) Q−1. First, we use induction to prove that  x(r) −  x(0) Q ≤ 8η,

∇p e(r)( x(r)) Q−1 ≤ 1 − 641 r η and  e(r) −  e(0) 2 ≤ 101 c∆ for all r.

Clearly the claims hold for r = 0. We now suppose they hold for all r ≤ t and show that they hold for r = t + 1. Now, since  x(t) −  x(0) Q ≤ 8η,  x(t+1) =  x(t) − 18Q−1∇p e(t)( x(t)), and

∇p e(t)( x(t)) Q−1 ≤ 1 − 641 t η ≤ η, we have

1 8 ∇p e(t)( x(t)) Q−1 ≤ 9η.

 x(t+1) −  x(0) Q ≤  x(t) −  x(0) Q +

We will improve this estimate later in the proof to ﬁnish the induction on  x(t+1) −  x(0) Q, but using this, η ≤ 0.01 ce + µ( x(0)), and  e(t) ∞ ≤  e(t) −  e(0) ∞ +  e(0) ∞ ≤ c2e, we can invoke Lemma 11 and Lemma 12 and therefore

1

32 ∇p e(t)( x(t)) Q−1 . By Lemma 13 we have

∇p e(t)( x(t+1)) Q−1 ≤ 1 −

1 32 ∇p e(t)( x(t)) Q−1 +

1 ce + µ( x(0))

∇p e(t+1)( x(t+1)) Q−1 ≤ 1 −

 e(t+1) −  e(t) 2. (6.3)

To bound  e(t+1)− e(t) 2, we note that Lemma 10 and the induction hypothesis  x(t)− x(0) H( x(0)) ≤  x(t) −  x(0) Q ≤ 8η shows that (1 − 0.1)Sx(0) Sx(t) (1 + 0.1)Sx(0) and therefore

1 1 − 0.1

S−x(1t)( sx(t) −  sx(t+1)) 2 ≤

S−x(0)1 A  x(t) −  x(t+1) 2

1 8

1 1 − 0.1

Q−1∇p e(t)( x(t))

=

AT S−2

x(0)A

1 8(1 − 0.1) ce + µ( x(0))

∇p e(t)( x(t)) Q−1 (6.4) Now since

≤

 e(t+1) −  e(t) = τ (t+1) − ψ( x(t+1)) − τ (t) − ψ( x(t))

= ∆(t+1) − ψ( x(t+1)) − ψ( x(t))

Consequently, with high probability in n,

 e(t+1) −  e(t) 2 = ∆(t+1) − ψ( x(t+1)) − ψ( x(t))

2 ≤ c∆ S−x(1t)( sx(t+1) −  sx(t))

2

c∆ 8(1 − 0.1) ce + µ( x(0))

∇p e(t)( x(t)) Q−1 .

≤

where in the last line we used mini∈[m] wi ≥ µ( x(0)). Since c∆ < 0.01ce, by (6.3), we have

0.01ce

1 32 ∇p e(t)( x(t)) Q−1 +

8(1 − 0.1)(ce + µ( x(0))) ∇p e(t)( x(t)) Q−1 ≤ 1 −

∇p e(t+1)( x(t+1)) Q−1 ≤ 1 −

1

64 ∇p e(t)( x(t)) Q−1 . Furthermore, this implies that

 x(t+1) −  x(0) Q ≤

Similarly, we have that

t

k=0

1 8

Q−1∇p e(k)( x(k))

≤

Q−1

∞

1 8

i=0

1 64

1 −

k

64 8

η ≤

η = 8η .

t

k

1 64

c∆ 8(1 − 0.1) ce + µ( x(0))

∇p e(0)( x(0)) Q−1

 e(t+1) −  e(0) 2 ≤

1 −

k=0

8c∆η (1 − 0.1) ce + µ( x(0))

8c∆ (1 − 0.1) ce + µ( x(0))

1 10

δ e(0)( x(0)) ≤

≤

≤

c∆

where we used η = ∇p e(0)( x(0)) Q−1 ≤ ∇p e(0)( x(0)) H−1 = δ e(0)( x(0)) and this ﬁnishes the induction on ∇p e(t)( x(t)) Q−1,  x(t) −  x(0) Q and  e(t) −  e(0) 2.

Hence, for all r, Lemma 11 shows that

√

δ e(r)( x(r)) = ∇p e(r)( x(r)) H( x(r))−1 ≤

2 ∇p e(r)( x(r)) H( x(0))−1 ≤

r

8 3 ∇p e(r)( x(r)) Q−1 ≤

8 3

1 64

∇p e(0)( x(0)) Q−1 ≤ 2 1 −

1 −

r

1 64

δ e(0)( x(0)).

Using that E e(t+1) =  e(t), we see that the expected change in function value is only due to the change while taking centering steps and therefore Lemma 12 shows that

∞

1 8

E[p e(r)( x(r))] ≥ p e(0)( x(0)) −

k=0

1 64

1 −

2k

∇p e(0)( x(0)) 2Q−1 ≥ p e(0)( x(0)) − 8 δ e(0)( x(0))

2

.

Finally, for (4), we note that

s( x(r)) − s( x(0)) s( x(0))

=  x(r) −  x(0)

2

≤

AT S−2

x(0)A

1 µ( x(0)) + ce

 x(r) −  x(0)

1 10

≤

.

Q−1

| |
|---|


###### 6.2 Changing Constraints

Here we bound the eﬀect that adding or a removing a constraint has on the hybrid barrier function. Much of the analysis in this section follows from the following lemma which follows easily from the Sherman Morrison Formula.

- Lemma 15 (Sherman Morrison Formula Implications). Let B ∈ Rn×n be an invertible symmetric matrix and let  a ∈ Rn be arbitrary vector satisfying  aTB−1 a < 1. The following hold:

- 1. B ± a aT −1 = B−1 ∓ B1−±1 a a aTBT−B1− a1.

- 2. 0 B1−±1 a a aTBT−B1− a1 1±  aT aTBB−−1 a1 aB−1.

- 3. log det B ± a aT = lndetB + ln 1 ± aTB−1 a .


Proof. (1) follows immediately from Sherman Morrison [95]. (2) follows since  a aT is PSD,

B−1 a aTB−1 1 ± aTB−1 a

= B−1/2

B−1/2 a aTB−1/2 1 ± aTB−1 a

B−1/2 ,

and  y yT  y 22I for any vector  y. (3) follows immediately from the Matrix Determinant Lemma.

| |
|---|


We also make use of the following technical helper lemma.

- Lemma 16. For A ∈ Rn×m and all  a ∈ Rn we have


1 ψA[i]

4 i

2

A ATA + λI −1 a

≤  aT ATA + λI −1 a

i∈[m]

Proof. We have by Cauchy Schwarz that

2

≤ ψA[i] · aT ATA + λI −1 a and consequently

1Ti A ATA + λI −1 a

4

1Ti A ATA + λI −1 a

ψA[i] ≤  aT ATA + λI −1 a

i∈[m]

Since

i∈[m]

1iA ATA + λI −1 a

2

.

2

=  aT ATA + λI −1 ATA ATA + λI −1 a

1Ti A ATA + λI −1 a

i∈[m]

≤  aT ATA + λI −1 a, we have the desired result.

| |
|---|


We now bound the eﬀect of adding a constraint.

- Lemma 17. Let A ∈ Rm×n, b ∈ Rm, τ  ∈ Rm, and  x ∈ P def=  y ∈ Rn : A y ≥ b . Let A ∈ R(m+1)×n be A with a row  am+1 added, let b ∈ Rm+1 be the vector b with an entry bm+1 added, and let


T m+1(ATx Ax+λI)−1 am+1

P def=  y ∈ Rn : A y ≥ b . Let sm+1 =  aTm+1 x − bm+1 > 0, ψa =  a

###### s2m+1 . Now, let  υ ∈ Rm+1 be deﬁned so that υm+1 = 1+ψψa

and for all i ∈ [m]

a

1 1 + ψa

υi = τi −

 am+1 sm+1

Ax ATxAx + λI −1

2

.

i

Then, the following hold

- • [Leverage Score Estimation] eP( υ, x)m+1 = 0 and eP( υ, x)i = eP(τ , x)i for all i ∈ [m].

- • [Function Value Increase] p e

P( υ, x)( x) = p eP(τ , x)( x) − ce lns( x)m+1 + ln(1 + ψa).

- • [Centrality Increase] δ e


P( υ, x)( x) ≤ δ eP( υ, x)( x) + (ce + ψa) µψ( xa) + ψa. Proof. By (1) in Lemma 15, we have that for all i ∈ [m]

2

1 1 + ψa

 am+1 sm+1

Ax ATxAx + λI −1

ψP( x)i = ψP( x)i −

i

and that

ψa2 1 + ψa

ψP( x)m+1 = ψa −

ψa 1 + ψa

=

.

Consequently [Leverage Score Estimation] holds. Furthermore, by (3) in Lemma 15 this then implies that [Function Value Change] holds.

To bound the change in centrality note that by (2) in Lemma 15 we have that H−1 H−1.

Therefore if let  υ ∈ Rm be deﬁned so that  υ i =  υi for all i ∈ [m] then by triangle inequality we have

δ ep( υ, x)( x) = ATx(ce 1 +  υ) H−1 ≤ ATx(ce 1 +  υ) H−1 ≤ ATx(ce 1 + τ ) H−1 +

 am+1 sm+1

+ ATx( υ − τ ) H−1

(ce + υm+1)

H−1

ψa 1 + ψa

 am+1 sm+1 H−1

+ ATx( υ − τ ) H−1

= δ eP(τ , x)( x) + ce +

Now, since H−1 µ( 1 x) ATxAx + λI −1, we have that

 am+1 sm+1 H−1 ≤

1 µ( x)

 am+1 sm+1 (AT

=

x Ax+λI)−1

ψa µ( x)

.

Since Ψ1/2Ax ATxΨAx −1 ATxΨ1/2 is a projection matrix, we have Ψ−1 Ax ATxΨAx −1 ATx

AxH−1ATx. By Lemma 16, we have ATx τ  −  υ 2H−1 ≤ τ  −  υ 2Ψ−1

2 2

1 1 + ψa

 am+1 sm+1

1 ψ( x)i

1iAx ATxAx + λI −1

=

i∈[m]

2

2  aTm+1 ATxAx + λI −1 am+1 s2m+1

1 1 + ψa

ψa 1 + ψa

≤

=

2

Combining, we have that

ψa 1 + ψa

P( υ, x)( x) ≤ δ eP(τ , x)( x) + ce +

δ e

≤ δ eP(τ , x)( x) + (ce + ψa)

ψa µ( x)

ψa µ( x)

ψa 1 + ψa

+

+ ψa.

| |
|---|


We now bound the eﬀect of removing a constraint.

- Lemma 18 (Removing a Constraint). Let A ∈ Rm×n, b ∈ Rm, τ  ∈ Rm, and  x ∈ P def= { y ∈ Rn : A y ≥ b}. Let A ∈ R(m−1)×n be A with row m removed, let b ∈ Rm−1 denote the ﬁrst m − 1


coordinates of b, and let P def= { y ∈ Rn : A y ≥ b}. Let ψd = ψP( x)m. Now, let  υ ∈ Rm−1 be deﬁned so that for all i ∈ [m − 1]

1 1 − ψd

2 i

Ax ATxAx + λI −1 ATx 1m

υi = τi +

.

Assume ψd ≤ 1.1µ( x) ≤ 101 and  eP(τ , x) ∞ ≤ ce ≤ 12, we have the following:

- • [Leverage Score Estimation] eP( υ, x)i = eP(τ , x)i for all i ∈ [m − 1].

- • [Function Value Decrease] p ep( υ, x)( x) = p eP(τ , x)( x) + [ce + eP(τ , x)m]lns( x)m + ln(1 − ψd)

- • [Centrality Increase] δ ep( υ, x)( x) ≤ √ 1


δ eP(τ , x)( x) + 3(ce + µ( x)). Proof. By (1) in Lemma 15, we have that for all i ∈ [m − 1]

1−2µ( x)

1 1 − ψd

2

1Ti Ax ATxAx + λI −1 ATx 1m

.

ψP( x)i = ψP( x)i +

Consequently, [Leverage Score Estimation] holds. Furthermore, by (3) in Lemma 15, this then implies that [Function Value Change] holds.

To bound the change in centrality we ﬁrst note that by (1) and (2) in Lemma 15, we have that the approximate Hessian for P, denoted H( x), is bounded by

H( x)−1 = H( x) − ATx (ceI + Ψx)1/2 1m 1Tm (ceI + Ψx)1/2 Ax

α 1 − α

1 1 − α

H( x)−1 =

H( x)−1

1 +

−1

where α def= 1Tm (ceI + Ψx)1/2 AxH( x)−1ATx (ceI + Ψx)1/2 1m. Using ce + µ( x) ≤ 21 + 101 ≤ 1, we have

H( x)−1 ATx(ce + µ( x))Ax + λI −1 (ce + µ( x))−1 ATxAx + λI −1 . (6.5) Using this, we have

α ≤

ce + ψd ce + µ( x)

1TmAx ATxAx + λI −1 ATx 1m =

ce + ψd ce + µ( x)

ψd . (6.6)

Now let τ  ∈ Rm−1 be deﬁned so that τ i = τi for all i ∈ [m − 1]. We have by above that

1 √1 − α

ATx(ce 1 +  υ) H−1 and therefore, by triangle inequality

δ ep( υ, x)( x) = ATx(ce 1 +  υ) H−1 ≤

ATx(ce 1 +  υ) H−1 ≤ ATx(ce 1 + τ ) H−1 + ATx 1m(ce + τm) H−1 + ATx(τ  −  υ) H−1

= δ eP(τ , x)( x) + (ce + τm) ATx 1m H−1 + ATx(τ  −  υ) H−1 . Now, (6.5) shows that

1 ce + µ( x)

ATx 1m H−1 ≤

ATx 1m (AT

xAx+λI)−1 ≤

ψd ce + µ( x)

Furthermore, since Ψ−1 Ax ATxΨAx −1 ATx AxH−1ATx, by Lemma 16 we have

ATx τ  −  υ 2H−1 ≤ τ  −  υ 2Ψ−1

2 2

1 1 − ψd

1 ψ( x)i

1Ti Ax ATxAx + λI −1 ATx 1m

=

i∈[m]

2

ψd 1 − ψd

1 1 − ψd

2

1TmAx ATxAx + λI −1 ATx 1m

≤

=

Combining, we have that

2

1 √1 − α

δ ep( υ, x)( x) ≤

δ eP(τ , x)( x) + (ce + τm)

ψd ce + µ( x)

+

ψd 1 − ψd

.

Using the assumption ψd ≤ 1.1µ( x) ≤ 101 ,  eP(τ , x) ∞ ≤ ce and (6.6), we have α ≤ 1.1ψd ≤ 1.21µ( x) and τm ≤ ψd + ce, and

√

1 1 − 1.3µ( x)

δ ep( υ, x)( x) ≤

δ eP(τ , x)( x) + (ce + τm)

1.1 + 1.2ψd

√

√

1 1 − 2µ( x)

1 1 − 110.3

≤

1.1 · 2ce + (

1.1 + 1.2 · 1.1)µ( x)

δ eP(τ , x)( x) +

| |
|---|


###### 6.3 Hybrid Center Properties

Here we prove properties of points near the hybrid center. First we bound the distance between points in the H( x) norm in terms of the 2 norm of the points.

- Lemma 19. For A ∈ Rm×n and b ∈ Rm suppose that  x ∈ P = { y : A y ≥ b} and  e ∈ Rm such that  e ∞ ≤ 21ce < 201 and δ e ≤ 0.1 ce + µ( x). Then for all  y ∈ P we have


12mce + 6n + 2λ  y 22 ce + µ( x)

 x −  y H( x) ≤

(6.7)

and

 x 22 ≤ 4λ−1(mce + n) + 2  y 22 .

Proof. For notational simplicity let t def= ce 1 +  e + ψx, T def= diag( t), and Q def= ATx(ceI + Ψx)Ax. We have

and

and

 x −  y 2AT

xTAx =

i∈[m]

[ sx −  sy]2i [ sx]2i

ti

=

i∈[m]

[ sy]2i [ sx]2i ≤

ti

i∈[m]

 

i∈[m]

  max

[ sy]i [ sx]i ≤

[ sy]i [ sx]i

ti

i∈[m]

 

i∈[m]

[ sy]i [ sx]i

ti 1 − 2

+

[ sy]2i [ sx]2i

(6.8)

  1 + S−x1( sy −  sx) ∞ (6.9)

[ sy]i [ sx]i

ti

S−x1AH( x)−1ATS−x1 ii

S−x1 ( sx −  sy) ∞ ≤ max

1iS−x1A( x −  y) ≤  x −  y H( x) max

i∈[m]

i∈[m]

≤ (ce + µ( x))−1/2  x −  y H( x) . (6.10)

Now, clearly i∈[m] ti[ sy]i/[ sx]i is positive and since  e ∞ ≤ 21ce we know that 12Q ATxTAx. Therefore, by combining, (6.8), (6.9), and (6.10) we have

 

 

 x −  y H( x) ce + µ( x)

[ sy]i [ sx]i

[ sy]i [ sx]i

- 1

- 2


 x −  y 2Q ≤ t 1 −

ti

+

ti

i∈[m]

i∈[m]

 

 

 x −  y H( x) ce + µ( x)

[ sy]i [ sx]i

≤ t 1 +

ti

(6.11)

i∈[m]

Now since ∇p e( x) = −ATS−x1T 1 + λ x we have  x −  y,∇p e( x) = −

[ sx −  sy]i [ sx]i

+ λ xT( x −  y)

ti

i∈[m]

and therefore by Cauchy Schwarz and  xT y ≤  x 22 + 14  y 22,

[ sy]i [ sx]i

= t 1 − λ  x 22 + λ xT y +  x −  y,∇p e( x) (6.12)

ti

i∈[m]

λ 4

 y 22 +  x −  y H( x)δ e( x) . (6.13)

≤ t 1 +

Now, using (6.11), (6.13) and the deﬁnition of H( x), we have

- 1

- 2


- 1

- 2


λ 2

 x −  y 2H( x) =

 x −  y 2Q +

 x −  y 22

 

 

 x −  y H( x) ce + µ( x)

[ sy]i [ sx]i

λ 2

 x −  y 22

≤ t 1 +

ti

+

i∈[m]

 x −  y 2H( x) ce + µ( x)

t 1 + λ4  y 22 ce + µ( x)

λ 2

≤ t 1 +

 x −  y H( x) + δe( x)

+

 x −  y 22.

Using the fact that δe( x) ≤ 0.1 ce + µ( x), we have

t 1 + λ4  y 22 ce + µ( x)

1 4

λ 2

 x −  y 2H( x) ≤ t 1 +

 x −  y 22 +

 x −  y H( x). (6.14)

Furthermore, since i∈[m] ti[ sy]i/[ sx]i is positive, (6.12) shows that

λ xT( x −  y) = λ  x 22 − λ xT y ≤ t 1 +  x −  y,∇p e( x) ≤ t 1 +  x −  y H( x)δe( x) and hence

λ 2

λ 2

λ 2

λ 2

 x −  y 22 ≤

 y 22 ≤ t 1 +

 x −  y 22 +

 x 22 = λ xT( x −  y) +

λ 2

 y 22 +  x −  y H( x)δe( x) . (6.15) Putting (6.15) into (6.14) and using the fact that δe( x) ≤ 0.1 ce + µ( x), we have

t 1 + λ4  y 22 ce + µ( x)

λ 2

1 4

 x −  y 2H( x) ≤ 2 t 1 +

 y 22 + 0.1 +

 x −  y H( x).

Now, using t 1 ≤ 2mce + n, we have

2mce + n + λ4  y 22 ce + µ( x)

1 4

 x −  y 2H( x) ≤ 2α + (0.1 + α)  x −  y H( x) for α =

Since ce + µ( x) ≤ 1.05, we have α ≥ 0.9 and hence

0.1 + α + (α + 0.1)2 + 2α 2 · 14

 x −  y H( x) ≤

≤ 6α

yielding (6.7). We also have by (6.12) and the fact that δe( x) ≤ 0.1 ce + µ( x),

[ sy]i [ sx]i

λ  x 22 = t 1 + λ xT y +  x −  y,∇p e( x) −

ti

i∈[m]

λ 2

λ 2

 y 22 +  x −  y H( x)δe( x) ≤ t 1 +

 x 22 +

≤ t 1 +

λ 2

λ 2

 x 22 +

 y 22 + 0.1 ce + µ( x)  x −  y H( x)

.

Hence, using t 1 ≤ 2mce + n and  x −  y H( x) ≤ 6α, we have

λ 2

λ 2

λ 4

 x 22 ≤ t 1 +

 y 22 ≤ λ  y 22 + 2(mce + n).

 y 22 + 0.6 2mce + n +

| |
|---|


In the following lemma we show how we can write one hyperplane in terms of the others provided that we are nearly centered and show there is a constraint that the central point is close to.

- Lemma 20. Let A ∈ Rm×n and b ∈ Rm such that ai 2 = 1 for all i. Suppose that  x ∈ P = { y :


A y ≥ b} and  e ∈ Rm such that  e ∞ ≤ 12ce ≤ 12. Furthermore, let = minj∈[m] sj( x) and suppose that i = arg minj∈[m] sj( x) then

 ai +

j =i

- s(x)i

- s(x)j


Proof. We know that

ce + ej + ψj( x) ce + ei + ψi( x)

 aj

2 (ce + µ( x))

≤

2

λ  x 2 + δe( x)

∇pe( x) = −ATS−x1(ce 1 +  e + ψx) + λ x

(ce + ei + ψi) s( x)i

= λ x −

 ai

i∈[m]

Consequently, by  e ∞ ≤ 21ce, and ψi( x) ≥ µ( x)

mce + n 2 + λ .

 ai +

j =i

- s(x)i

- s(x)j


ce + ej + ψj( x) ce + ei + ψi( x)

 aj

si( x) (ce + ei + ψi( x))

ATS−x1(ce 1 +  e + ψx)

=

2

2 (ce + µ( x))

λ  x 2 + ∇pe( x) 2 .

≤

2

Using  ai = 1, i ψi ≤ n, and si( x) ≥ , we have

Tr(ATx(ceI + Ψx)Ax) = Tr(AxATx(ceI + Ψx)) =

ai 22 s2i( x) ≤

mce + n 2 . (6.16)

(ce + ψi)

i

Hence, we have H( x) mce 2+n + λ I and ∇pe( x) 2 ≤ δe( x) mce 2+n + λ yielding the result.

| |
|---|


###### 6.4 The Algorithm

Here, we put all the results in the previous sections to get our ellipsoid algorithm. Below is a sketch of the pseudocode; we use ca,cd,ce,c∆ to denote parameters we decide later.

In the algorithm, there are two main invariants we maintain. First, we maintain that the centrality δP, e( x), which indicates how close  x is to the minimum point of p e, is small. Second, we maintain that  e(τ , x) ∞, which indicates how accurate the leverage score estimate τ  is, is small. In the following lemma we show that we maintain both invariants throughout the algorithm.

Algorithm 2: Our Cutting Plane Method Input: A(0) ∈ Rm×n, b(0) ∈ Rm, > 0, and radius R > 0. Input: A separation oracle for a non-empty set K ⊂ B∞(R). Check: Throughout the algorithm, if si( x(k)) < output P(k). Check: Throughout the algorithm, if  x(k) ∈ K, output  x(k). Set P(0) = B∞(R). Set  x(0) := 0 and compute τi(0) = ψP(0)( x(0))i for all i ∈ [m] exactly. for k = 0 to ∞ do

Let m(k) be the number of constraints in P(k). Compute w (k) such that ΨP(k)( x(k)) W(k) (1 + c∆)ΨP(k)( x(k)). Let i(k) ∈ arg maxi∈[m(k)] wi(k) − τi(k) . Set τ(k+

1 3)

1 3)

i(k) = ψP(k)( x(k))i(k) and τ(k+

j = τj(k) for all j = i(k). if mini∈[m(k)] wi(k) ≤ cd then

Remove constraint with minimum wi(k) yielding polytope P(k+1). Update τ  according to Lemma 18 to get τ(k+

- 2

- 3)


j . else

Use separation oracle at  x(k) to get a constraint { x :  aT x ≥  aT x(k)} with  a 2 = 1. Add constraint { x :  aT x ≥  aT x(k) − ca−1/2  aT(ATS x−(2k)A + λI)−1 a} yielding polytope P(k+1). Update τ  according to Lemma 17 to get τ(k+

- 2

- 3)


j .

( x(k+1),τ (k+1)) = Centering( x(k),τ (k+23),200,c∆). end

- Lemma 21. Assume that ce ≤ cd ≤ 1016, ca√ca ≤ 10cd3, cd ≤ ca, and c∆ ≤ Cce/log(n) for some small enough universal constant C. During our cutting plane method, for all k, with high probability in n, we have


- 1.  e(τ (k+31), x(k)) ∞ ≤ 10001 ce,  e(τ (k+23), x(k)) ∞ ≤ 10001 ce,  e(τ (k+1), x(k+1)) ∞ ≤ 4001 ce.

- 2. δP(k), e(τ (k+2

3), x(k))( x(k)) ≤ 1001 ce + min µ( x(k)),cd .

- 3. δP(k+1), e(τ (k+1), x(k+1))( x(k+1)) ≤ 4001 ce + min µ( x(k+1)),cd .


Proof. Some statements of the proof hold only with high probability in n; we omit mentioning this for simplicity.

We prove by induction on k. Note that the claims are written in order consistent with the algorithm and proving the statement for k involves bounding centrality at the point  x(k+1). Trivially we deﬁne, τ (−1) = τ (−32) = τ (−31) = τ (0) and note that the claims then hold for k = −1 as we compute the initial leverage scores, τ (0), exactly and since the polytope is symmetric we have δ e(τ (0), x(0))( 0) = 0. We now suppose they hold for all r < t and show that they hold for r = t.

We ﬁrst bound δ. For notational simplicity, let ηt def= ce + min{µ( x(t)),cd}. By the induction hypothesis we know that δP(t), e(τ (t), x(t))( x(t)) ≤ 4001 ηt. Now, when we update τ(t) to τ(t+13), we set

 ei(t) to 0. Consequently, Lemma 13 and the induction hypothesis  e(τ (t), x(t)) ∞ ≤ 4001 ce show that

1 ce + µ( x(t))

ei(t)(τ (t), x(t))

3), x(t))( x(t)) ≤ δP(t), e(τ (t), x(t))( x(t)) +

δP(t), e(τ (t+1

√ce 400 ≤

1 400

ηt 200

≤

ηt +

(6.17)

Next, we estimate the δ changes when we remove or add a constraint. For the case of removal, we note that it happens only if µ( x(t)) ≤ mini wi ≤ cd ≤ 1016. Also,

the row we remove has leverage score at most 1.1µ( x(t)) because we pick the row with minimum w. Hence, Lemma 18 and ce ≤ 1016 show that

1 1 − 2µ( x(t))

3), x(t))( x(t)) ≤

3), x(t))( x(t)) + 2.7(ce + µ( x(t))) ≤

δP(t+1), e(τ (t+2

δP(t), e(τ (t+1

1 √

ηt 200

ηt 100

+ 3(ce + µ( x(t))) ≤

1 − 2 · 10−6

√2

√ce + cdηt ≤

where we used the fact µ( x(t)) ≤ cd and hence ce + µ( x(t)) ≤

1000ηt.

For the case of addition, we note that it happens only if 2µ( x(t)) ≥ mini wi ≥ cd. Furthermore, in this case the hyperplane we add is chosen precisely so that ψa = ca. Furthermore, since ce ≤ cd ≤ ca by Lemma 17 we have that

3), x(t))( x(t)) ≤ δP(t), e(τ (t+1

3), x(t)) + (ce + ψa)

δP(t+1), e(τ (t+2

ψa µ( x(t))

ηt 200

+ ψa ≤

+ 4ca

ca cd

.

Furthermore, since ca√ca ≤ 1000cd , µ( x(t)) ≥ cd/2, and cd ≤ 10−6 we know that 4ca ca/cd ≤ 2001 ηt and consequently in both cases we have δP(t+1), e(τ (t+2

3), x(t))( x(t)) ≤ 1001 ηt.

Now, note that Lemmas 17 and 18 show that  e does not change during the addition or removal of an constraint. Hence, we have  e(τ (t+23), x(t)) ∞ ≤  e(τ (t+13), x(t)) ∞. Furthermore, we know the step “τ (k+

1 3)

i(k) = ψP(k)( x(k))i(k)” only decreases  e ∞ and hence we have  e(τ (t+23), x(t)) ∞ ≤  e(τ (t), x(t)) ∞ ≤ 400ce . Thus, we have all the conditions needed for Lemma 14 and consequently

200

1 64

1 1000

3), x(t))( x(t)) ≤

δP(t+1), e(τ (t+1), x(t+1))( x(t+1)) ≤ 2 1 −

δP(t+1), e(τ (t+2

ηt .

(t+1))−s( x(t)) s( x(t)) 2

Lemma 14 also shows that that s( x

≤ 101 and hence ψi( x(t)) ≤ 2ψi( x(t+1)) for all i. Therefore, ηt ≤ 2ηt+1 and thus

ce + min cd,µ( x(t+1)) 400

δP(t+1), e(τ (t+1), x(t+1))( x(t+1)) ≤

.

completing the induction case for δ.

Now, we bound  e ∞. Lemma 17 and 18 show that  e does not change during the addition or removal of an constraint. Hence,  e is aﬀected by only the update step “τ(k+

- 1

- 2)


i(k) = ψP(k)( x(k))i(k)” and the centering step. Using the induction hypothesis δP(r), e(τ (r+2

3), x(r))( x(r)) ≤ 1001 ηr and Lemma 14 shows that E e(τ (r+1), x(r+1)) =  e(τ (r+32), x(r)) and  e(τ (r+1), x(r+1)) −  e(τ (r+23), x(r)) 2 ≤ 101 c∆ for

all r ≤ t. The goal for the update step is to decrease  e by updating τ . In Section 7.2, we give a self-contained analysis of the eﬀect of this step as a game. In each round, the vector  e is corrupted

by some mean 0 and bounded variance noise and the problem is how to update  e such that  e ∞ is bounded. Theorem 34 shows that we can do this by setting the  ei = 0 for the almost maximum coordinate in each iteration. This is exactly what the update step is doing. Hence, Theorem 34 shows that this strategy guarantees that after the update step, we have

 e(τ(r+13), x(r))

= O (c∆ log (n))

∞

for all r ≤ t. Now, by our choice of c∆, we have  e(τ (t+13), x(t)) ∞ ≤ 10001 ce. Lemma 17 and 18 show that  e does not change during the addition or removal of an constraint. Hence, we

have  e(τ (t+32), x(t)) ∞ ≤ 10001 ce. Now, we note that again Lemma 14 shows  e(τ (t+1), x(t+1)) −  e(τ (t+32), x(t)) 2 ≤ 101 c∆ ≤ 10001 ce, and we have  e(τ (t+1), x(t+1)) ∞ ≤ 400ce . This ﬁnishes the induction case for  e ∞ and proves this lemma.

| |
|---|


Next, we show the number of constraints is always linear to n.

- Lemma 22. Throughout our cutting plane method, there are at most 1 + 2cn

d

constraints. Proof. We only add a constraint if mini wi ≥ cd. Since 2ψi ≥ wi, we have ψi ≥ c2d for all i. Letting

- m denote the number of constraints after we add that row, we have n ≥ i ψi ≥ (m−1)(cd/2). Using K = ∅ and K ⊂ B∞(R), here we show that the points are bounded.


| |
|---|


- Lemma 23. During our Cutting Plane Method, for all k, we have  x(k) 2 ≤ 6 n/λ + 2√nR.

Proof. By Lemma 21 and Lemma 19 we know that  x(k) 22 ≤ 4λ−1(mce + n) + 2  y 22 for any  y ∈ P(k). Since our method never cuts out any point in K and since K is nonempty, there is some

 y ∈ K ⊂ P(k). Since K ⊂ B∞(R), we have  y 22 ≤ nR. Furthermore, by Lemma 22 we have that mce ≤ ce + 2n ≤ 3n yielding the result.

| |
|---|


- Lemma 24. si  x(k) ≤ 12 n/λ + 4√nR + c1


aλ for all i and k in the our cutting plane method.

Proof. Let  x(j) be the current point at the time that the constraint corresponding to si, denoted { x :  aTi  x ≥ aTi  x(j) − si( x(j))}, was added. Clearly

si( x(k)) =  aTi  x(k) − aTi  x(j) + si( x(j)) ≤  ai ·  x(k) +  aTi  x(j) − si( x(j)) .

On the one hand, if the constraint for si comes from the initial symmetric polytope P(0) = B∞(R), we know  aT x(j) −  si( x(j)) ≤ R . On the other hand, if the constraint was added later then we know that

si( x(j)) = c−a 1/2  aT(ATS x−(2j)A + λI)−1 a ≤ (caλ)−1/2 and  aT x(j) − si( x(j)) ≤  ai ·  x(j) + si( x(j)) . Since  ai 2 = 1 by design and  x(j) 2 and

 x(k) 2 are upper bounded by 6 n/λ + 2√nR by Lemma 23, in either case the result follows.

| |
|---|


Now, we have everything we need to prove that the potential function is increasing in expectation.

aR2, ce = 6 ln(17cdnR/ ), and 24cd ≤ ca ≤ 13 then for all k we have

- Lemma 25. Under the assumptions of Lemma 21 if λ = c 1


Ep e(τ (k+1), x(k+1))( x(k+1)) ≥ p e(τ (k), x(k))( x(k)) − cd + ln(1 + β) where β = ca for the case of adding a constraint β = −cd for the case of removal.

Proof. Note that there are three places which aﬀect the function value, namely the update step for τ(k+13), the addition/removal of constraints, and the centering step. We bound the eﬀect of each separately.

First, for the update step, we have

3), x(k))( x(k)) = −ei(k) log(si(k)( x(k))) + p e(τ (k), x(k))( x(k)). Lemma 24, the termination condition and λ = c 1

p e(τ (k+1

aR2 ensure that

caλ ≤ 17√nR (6.18) and Lemma 21 shows that |ei(k)| ≤ ce. Hence, we have

≤ si(k)( x(k)) ≤ 12 n/λ + 4√nR +

1

3), x(k))( x(k)) ≥ p e(τ (k), x(k))( x(k)) − ce log(17nR/ ). For the addition step, Lemma 17 shows that

p e(τ (k+1

3), x(k))( x(k)) = p e(τ (k+1

3), x(k))( x(k)) − ce lns( x)m+1 + ln(1 + ca) ≥ p e(τ (k+1

p e(τ (k+2

3), x(k))( x(k)) − ce log(17nR/ ) + ln(1 + ca) and for the removal step, Lemma 18 and |ei| ≤ ce shows that

3), x(k))( x(k)) ≥ p e(τ (k+1

3), x(k))( x(k)) − [ce + eP(τ , x)m]lns( x)m + ln(1 − cd) ≥ p e(τ (k+1

p e(τ (k+2

3), x(k))( x(k)) − 2ce log(17nR/ ) + ln(1 − cd) After the addition or removal of a constraint, Lemma 21 shows that

1 100

3), x(k))( x(k)) ≤

ce + min µ( x(k)),cd and therefore Lemma 14 and ce ≤ cd show that

δP(k), e(τ (k+2

 

 

2

ce + min µ( x(k)),cd 100

Ep e(τ (k+1), x(k+1))( x(k+1)) ≥ p e(τ (k+2

3), x(k))( x(k)) − 8

cd 625

3), x(k))( x(k)) −

≥ p e(τ (k+2

.

Combining them with ce = 6 ln(17cdnR/ ), we have Ep e(τ (k+1), x(k+1))( x(k+1)) ≥ p e(τ (k), x(k))( x(k)) − 3ce log(17nR/ ) −

cd 625

+ ln(1 + β) ≥ p e(τ (k), x(k))( x(k)) − cd + ln(1 + β)

where β = ca for the case of addition and β = −cd for the case of removal.

| |
|---|


Theorem 26. For ca = 10110, cd = 10112, ce = 6 ln(17cdnR/ ), c∆ = log(Ccne) and λ = c 1

aR2 for some small enough universal constant C, then we have

1 1011

9β 1011

Ep e(τ (k+1), x(k+1))( x(k+1)) ≥ p e(τ (k), x(k))( x(k)) −

+

where β = 1 for the case of addition and β = 0 for the case of removal. Proof. It is easy to see that these parameters satisfy the requirements of Lemma 25.

| |
|---|


###### 6.5 Guarantees of the Algorithm

In this section we put everything together to prove Theorem 31, the main result of this section, providing the guarantees of our cutting plane method.

For the remainder of this section we assume that ca = 10110, cd = 10112, ce = 6 ln(17cdnR/ ), c∆ = log(Ccne) and λ = c 1

aR2. Consequently, throughout the algorithm we have

 x 2 ≤ 6 n/λ + 2√nR = 6 canR2 + 2√nR ≤ 3√nR. (6.19)

- Lemma 27. If si( x(k)) < for some i and k during our Cutting Plane Method then

max

 y∈P(k)∩B∞(R)

 ai, y − min

 y∈P(k)∩B∞(R)

 ai, y ≤

8n  cace

.

Proof. Let  y ∈ P(k) ∩ B∞(R) be arbitrary. Since  y ∈ B∞(R) clearly  y 22 ≤ nR2. Furthermore, by Lemma 22 and the choice of parameters mce + n ≤ 3n. Consequently, by Lemma 19 and the fact

that λ = c 1

aR2 and ca < 1 we have

 x −  y H( x) ≤

12mce + 6n + 2λ  y 22 ce + µ( x) ≤

30n + 2cn

a

ce + µ( x) ≤

4n ca√ce and therefore

S−x(1k)(s( x(k)) − s( y))

∞

≤

1 √ce

S−x(1k)(s( x(k)) − s( y))

ceI+Ψ

≤

4n cace

.

Consequently, we have (1 − c4n

ace)si( x(k)) ≤ si( y) ≤ (1 + c4n

ace)si( x(k)) for all  y ∈ P(k) ∩ B∞(R).

| |
|---|


Now let us show how to compute a proof (or certiﬁcate) that the feasible region has small width on the direction  ai.

- Lemma 28. Suppose that during some iteration k for i = arg minj sj( x(k)) we have si( x(k)) ≤ . Let ( x∗,τ ∗) = Centering( x(k),τ (k),64log(2R/ ),c∆) where τ (k) is the τ at that point in the algorithm and let


ce + ej( x∗,τ ∗) + ψj( x∗) ce + ei( x∗,τ ∗) + ψi( x∗)

- s( x∗)i

- s( x∗)j


 a∗ =

tj aj where tj =

.

j =i

√n 

Then, we have that  ai + a∗ 2 ≤ 8

caceR and tj ≥ 0 for all j. Furthermore, we have

 

 

T

O(n)

O(n)

3n ce

 x∗ −

tjbj ≤

s( x∗)i .

tjaj

j =i

j =i

Proof. By Lemma 14 and Lemma 21 we know that  e( x∗,τ ∗) ≤ 21ce and δ e( x∗,τ ∗) ≤ R ce + µ( x∗). Since  e( x∗,τ ∗) ≤ 12ce, we have tj ≥ 0 for all j. Furthermore, by Lemma 20 and (6.19), we then have that with high probability in n

2 (ce + µ( x∗))

mce + n 2 + λ

 ai + a∗ 2 ≤

λ  x∗ 2 + δe( x∗)

(3√nR) +

n caR2 ≤

2 ce

1 caR2

3n 2 +

≤

R

√3n 4

3√n caR

2√n √caR

2 ce

+

+

.

Hence, we have

8√n  caceR

 ai + a∗ 2 ≤

.

By Lemma 21 we know that  e( x∗,τ ∗) ≤ 12ce and hence

 

 

T

- O(n)


O(n)

O(n)

O(n)

ce + ej( x∗,τ ∗) + ψj( x∗) ce + ei( x∗,τ ∗) + ψi( x∗)

 x∗ −

tjaj

tjbj =

tjs( x∗)j = si( x∗)

j =i

j =i

j =i

j =i

O(n)

O(n)

3 2ce + ψj( x∗)

3mce + 2n ce ≤

3n ce

- 1

- 2ce + ψi( x∗) ≤ si( x∗)


≤ si( x∗)

si( x∗)

j =i

j =i

| |
|---|


- Lemma 29. During our Cutting Plane Method, if p e( x(k)) ≥ nlog(cn


)+6cn

, then we have si( x(k)) ≤ for some i.

a

a

Proof. Recall that

- 1

- 2


λ 2

 x(k) 22.

log det ATS−x(2k)A + λI +

p e( x(k)) = −

(ce + ei)log si( x(k))i +

i∈[m]

Using  x(k) ≤ 3√nR (6.19) and λ = c 1

aR2, we have p e( x(k)) ≤ −

5n ca

1 2

log det ATS−x(2k)A + λI +

(ce + ei)log(s( x(k))i) +

.

i∈[m]

Next, we note that ei ∞ ≤ ce ≤ 12 ln(171nR/ ) and si  x(k) ≤ 12 n/λ + 4√nR + c1

aλ ≤ 6√nR (Lemma 24). Hence, we have

p e( x(k)) ≤

- 1

- 2


6n ca

log det ATS−x(2k)A + λI +

.

###### , we have 12 log det ATS−x(2k)A + λI ≥ nlog(cn

Since p e( x(k)) ≥ nlog(cn

###### ) + 6cn

###### ). Using < R, we have that cn22

a

a

a

###### 2 ≥ n 22 + λ and hence

a

n

log λi ATS−x2A + λI ≥ nlog

2 + λ .

i

###### Therefore, we have log λmax ATS−x2A + λI ≥ log n 2 + λ . Hence, we have some unit vector  v such that  vATS−x2A v + λ vT v ≥ n 2 + λ. Thus,

(A v)2i s( x(k))2i ≥

n

2.

i

2 i

Therefore there is some i such that (A v)

s( x(k))2i ≥ 1 2. Since  ai and  v are unit vectors, we have 1 ≥  ai, v 2 ≥ s( x(k))2i/ 2 and hence s( x(k))i ≤ .

| |
|---|


- Lemma 30. With constant probability, the algorithm ends in 1024nlog(nR ) iterations. 4 Proof. Theorem 26 shows that for all k


1 1011

9β 1011

Ep e(τ (k+1), x(k+1))( x(k+1)) ≥ p e(τ (k), x(k))( x(k)) −

+

(6.20)

where β = 1 for the case of adding a constraint and β = 0 for the case of removing a constraint. Now, for all t consider the random variable

4.5m(t) 1011 −

3.5t 1011

Xt = p e(τ (t), x(t))( x(t)) −

where m(t) is the number of constraints in iteration t of the algorithm. Then, since m(t+1) = m(t) − 1 + 2β, (6.20) shows that

4.5m(t+1) 1011 −

1 1011

9β 1011 −

3.5(t + 1) 1011

EXt+1 ≥ p e(τ (t), x(t))( x(t)) −

+

4.5(−1 + 2β) 1011 −

1 1011

9β 1011 −

3.5 1011

= Xt −

= Xt. Hence, it is a sub-martingale. Let τ be the iteration the algorithm throws out error or outputs

+

- P(k). Optional stopping theorem shows that EXmin(τ,t) ≥ EX0. (6.21)


Using the diameter of P(0) is √nR, we have

- 1

- 2


λ 2

log det ATS−0 2A + λI +

p 0( 0) = −

ce log si( 0) +

i∈[m(0)]

≥ −cem(0) log(√nR) +

1 caR2 ≥ − n + cem(0) log(√nR).

n 2

log

Using ce = 6 ln(17cdnR/ ), cd = 10112 and m(0) = 2n, we have

0 22

4.5m(0) 1011 ≥ −nlog(√nR) − 100n.

X0 ≥ − n + cem(0) log(√nR) −

4We have made no eﬀort on improving this constant and we believe it can be improved to less than 300 using techniques in [5, 6].

- Therefore, (6.21) shows that for all t we have

− n(log(nR) + 100) ≤ EXmin(τ,t)

= pE Xmin(τ,t)|τ < t + (1 − p)E Xmin(τ,t)|τ ≥ t (6.22) where p def= P(τ < t).

Note that

E Xmin(τ,t)|τ ≥ t ≤ E p e(τ (t), x(t))( x(t))|τ ≥ t −

4.5m(t) 1011 −

3.5t 1011

.

≤ E p e(τ (t), x(t))( x(t))|τ ≥ t −

3.5t 1011

.

Furthermore, by Lemma 29 we know that when p e(τ (t), x(t))( x(t)) ≥ nlog(cn

a

) + 6cn

a

, there is a slack that is too small and the algorithm terminates. Hence, we have

E Xmin(τ,t)|τ ≥ t ≤ nlog(

n ca

) +

6n ca −

3.5t 1011

.

The proof of Lemma 21 shows that the function value does not change by more than 1 in one iteration by changing  x and can change by at most mce log(3nR ) by changing τ. Since by Lemma 22 we know that m ≤ 1 + 2cn

a

and ce = 6 ln(17cdnR/ ), we have that p e( x) ≤ nlog(cn

a

) + 7cn

a

throughout the execution of the algorithm. Therefore, we have

E Xmin(τ,t)|τ ≤ t ≤ Eτ<tp e(τ (t), x(t))( x(t)) ≤ nlog(

n ca

) +

7n ca

.

- Therefore, (6.22) shows that


Hence, we have

Thus, we have

−n(log(nR) + 100) ≤ nlog

n ca

7n ca − (1 − p)

3.5t 1011

+

.

3.5t 1011 ≤ nlog

(1 − p)

≤ nlog

= nlog

n ca

Rn2 ca

Rn2 ca

7n ca

+

+ n(log(nR) + 100)

7n ca

+ 100n

+

+ 8 · 1010n.

1 t

P(τ < t) = p ≥ 1 −

1011nlog

n2R

+ 1022n .

| |
|---|


Now, we gather all the result as follows:

Theorem 31 (Our Cutting Plane Method). Let K ⊆ Rn be a non-empty set contained in a box of radius R, i.e. K ⊆ B∞(R). For any ∈ (0,R) in expected time O(nSOΩ( /√n)(K)log(nR/ ) +

- n3 logO(1)(nR/ )) our cutting plane method either outputs  x ∈ K or ﬁnds a polytope P = { x : A x ≥ b} ⊇ K such that


- 1. P has O(n) many constraints (i.e. A ∈ RO(n)×n and b ∈ RO(n)).
- 2. Each constraint of P is either an initial constraint from B∞(R) or of the form  a, x ≥ b − δ where  a, x ≥ b is a normalized hyperplane (i.e.  a 2 = 1) returned by the separation oracle and δ = Ω √n .

- 3. The polytope P has small width with respect to some direction  a1 given by one of the constraints, i.e.

max

 y∈P∩B∞(R)

 a1, y − min

 y∈P∩B∞(R)

 a1, y ≤ O (n ln(R/ ))

- 4. Furthermore, the algorithm produces a proof of the fact above involving convex combination of the constraints, namely, non-negatives t2,...,tO(n) and  x ∈ P such that


- (a)  x 2 ≤ 3√nR,

- (b)  a1 + Oi=2(n) ti ai 2

= O R√nlog(R/ ) ,

- (c)  aT1  x − b1 ≤ ,
- (d) Oi=2(n) tiai


T

 x − Oi=2(n) tibi ≤ O(n log(R/ )) .

Proof. Our algorithm either ﬁnds  x ∈ K or we have si( x(k)) < . When si( x(k)) < , we apply Lemma 28 to construct the polytope P and the linear combination Oi=2(n) ti ai.

Notice that each iteration of our algorithm needs to solve constant number of linear systems and implements the sampling step to ﬁnd ∆(k) ∈ Rn s.t. E[ ∆(k)] = ψ( x(k))− ψ( x(k−1)). Theorem 33 shows how to do the sampling in O˜(1) many linear systems. Hence, in total, each iterations needs to solve O˜(1) many linear systems plus nearly linear work. To output the proof for (4), we use Lemma 28.

Note that the linear systems the whole algorithm need to solve is of the form (ATS−x2A + λI)−1 x =  y.

where the matrix ATS−x2A + λI can be written as ATDA for the matrix A = [A I] and diagonal matrix

S−2 0 0 λI

D =

.

Note that Lemma 14 shows that S(k) −1 ( s(k+1) −  s(k)) 2 ≤ 101 for the kth and (k + 1)th linear systems we solved in the algorithm. Hence, we have D(k) −1 ( d(k+1) − d(k)) 2 ≤ 101 . In [76], they showed how to solve such sequence of systems in O˜(n2) amortized cost. Moreover, since our algorithm always changes the constraints by δ amount where δ = Ω(√n) an inexact separation oracle SOΩ( /√n) suﬃces. (see Def 1). Consequently, the total work O(nSOΩ( /√n)(K)log(nR/ ) + n3 logO(1)(nR/ )). Note that as the running time holds with only constant probability, we can restart the algorithm whenever the running time is too large.

To prove (2), we note that from the algorithm description, we know the constraints are either from B∞(R) or of the form  aT x ≥  aT x(k) − δ where

 aT(ATS x−(2k)A + λI)−1 a ca

δ =

.

From the proof of Lemma 29, we know that if λmax(ATS−x2A + λI) ≥ n 2, then there is si < . Hence, we have λmin((ATS−x2A + λI)−1) ≤ n 2. Since  a is a unit vector, we have

 aT(ATS x−(2k)A + λI)−1 a ca ≥

2

.

nca

| |
|---|


#### 7 Technical Tools

In this section we provide stand-alone technical tools we use in our cutting plane method in Section 6. In Section 7.1 we show how to eﬃciently compute accurate estimates of changes in leverage scores using access to a linear system solver. In Section 7.2 we study what we call the “Stochastic Chasing 0 Game” and show how to maintain that a vector is small in ∞ norm by making small coordinate updates while the vector changes randomly in 2.

###### 7.1 Estimating Changes in Leverage Scores

In previous sections, we needed to compute leverage scores accurately and eﬃciently for use in our cutting plane method. Note that the leverage score deﬁnition we used was

√

√

WA ATWA + λI −1 AT

ψ(w )i = 1Ti

W 1i for some λ > 0 which is diﬀerent from the standard deﬁnition

√

√

WA ATWA −1 AT

σ(w )i = 1Ti

###### W 1i.

However, note that the matrix ATWA + λI can be written as ATDA for the matrix A = [A I] and diagonal matrix

W 0 0 λI

D =

.

and therefore computing ψ is essentially strictly easier than computing typical leverage scores. Consequently, we use the standard deﬁnition σ to simplify notation.

In [99], Spielman and Srivastava observed that leverage scores can be written as the norm of certain vectors

√

√

2 2

WA ATWA −1 AT

W 1i

σ(w )i =

and therefore leverage scores can be approximated eﬃciently using dimension reduction. Unfortunately, the error incurred by this approximation is too large to use inside the cutting point method. In this section, we show how to eﬃciently approximate the change of leverage score more accurately.

In particular, we show how to approximate σ(w ) − σ( v) for any given w , v with log(w ) −

log( v) 2 1. Our algorithm breaks σ(w )i − σ( v)i into the sum of the norm of small vectors and then uses the Johnson-Lindenstrauss dimension reduction to approximate the norm of each vector

separately. Our algorithm makes use of the following version of Johnson-Lindenstrauss.

Lemma 32 ([1]). Let 0 ≤ ≤ 12 and let  x1,..., xm ∈ Rn be arbitrary m points. For k = O( −2 log(m)) let Q be a k × n random matrix with each entry sampled from {−√1k, √1k} uniformly and independently. Then, E Q xi 2 =  xi 2 for all i ∈ [m] and with high probability in m we have that for all i ∈ [m]

(1 − )  xi 2 ≤ Q xi 2 ≤ (1 + )  xi 2 .

Algorithm 3: h = LeverageChange(A, v,w , ,α) Input: A ∈ Rm×n,  v,w  ∈ Rm>0, ∈ (0,0.5). Given: V−1( v − w ) 2 ≤ 101 and ATVA and ATWA are invertible. Sample Qd ∈ RO( −2 log(m))×n as in Lemma 32. Let dˆi = Qd

√

WA ATWA −1 AT 1i 22 for all i ∈ [n]. Let t = O log( −1) . Sample Qf ∈ RO( −2 log(mt))×n as in Lemma 32. Pick positive integer u randomly such that Pr[u = i] = (12)i. for j ∈ {1,2,··· ,t} ∪ {t + u} do

if j is even then Let fˆi(j) = Qf

√

j

VA ATVA −1 AT (V − W)A ATVA −1

2 AT 1i 22. else

Let ∆+ def= (V − W)+, i.e. the matrix V − W with negative entries set to 0. Let ∆− def= (W − V)+, i.e. the matrix W − V with negative entries set to 0. Let αˆi(j) = Qf

√

∆+A(ATVA)−1(AT (V − W)A ATVA −1)j−21AT 1i 22. Let βˆi(j) = Qf

√

∆−A(ATVA)−1(AT(V − W)A(ATVA)−1)j−21AT 1i 22. Let fˆi(j) = αˆi(j) − βˆi(j).

###### end

end Let fˆi = 2ufˆi(t+u) + tj=1 fˆi(j). Output: hˆi = (wi − vi)dˆi + vifˆi. for all i ∈ [m]

- Theorem 33. Let A ∈ Rm×n and  v,w  ∈ Rm>0 be such that α def= V−1( v − w ) 2 ≤ 101 and both ATVA and ATWA are invertible. For any ∈ (0,0.5), Algorithm 3 generates a random variable h


such that Ehˆ = σ(w )−σ( v) and with high probability in m, we have h−(σ(w ) − σ( v)) 2 ≤ O (α ). Furthermore, the expected running time is O((nnz(A) + LO)/ 2) where LO is the amount of time needed to apply ATVA −1 and ATWA −1 to a vector.

Proof. First we bound the running time. To compute dˆi,fˆi(j),αˆi(j),βˆi(j), we simply perform matrix multiplications from the left and then consider the dot products with each of the rows of A. Naively

this would take time O((t + u)2 log(mt)(nnz(A) + LO)). However, we can reuse the computation in computing high powers of j to only take time O((t + u)log(mt)(nnz(A) + LO)). Now since E[u] is constant we see that the total running time is as desired. It only remains to prove the desired properties of hˆ.

First we note that we can re-write leverage score diﬀerences using σ(w )i − σ( v)i = (wi − vi) A ATWA −1 AT

###### + vi A ATWA −1 − ATVA −1 AT

. Consequently, for all i ∈ [m], if we let

ii

ii

di def= 1Ti A ATWA −1 AT 1i, fi def= 1Ti A ATWA −1 − ATVA −1 AT 1i.

then

σ(w )i − σ( v)i = (wi − vi)di + (vi)fi . (7.1)

We show that dˆi approximates d and fˆi approximate fˆ well enough to satisfy the statements in the Theorem.

√

WA ATWA −1 AT 1i 22. Consequently, Lemma 32 shows that E[dˆi] = di and that with high probability in m we have (1− )di ≤ dˆi ≤ (1+ )di for all i ∈ [m]. Therefore, with high probability in m, we have

First we bound the quality of dˆi. Note that di =

2

(w  −  v) d − (w  −  v) d 22 =

(wi − vi)2d2i

≤ 2

(wi − vi)2 di − di

i∈[m]

i∈[m]

2

2

wi − vi vi

σ(w )i w i

(wi − vi)2

= 2

≤ 2 2

.

i∈[m]

i∈[m]

Next we show how to estimate f. Let X def= ATVA −1/2 AT (V − W)A ATVA −1/2. By the

assumption on α we know −12V ≺ V − W ≺ 12V and therefore −12I ≺ X ≺ 12I. Consequently we have that

ATWA −1 = ATVA −1/2 (I − X)−1 ATVA −1/2

∞

###### ATVA −1/2 Xj ATVA −1/2 .

=

j=0

and therefore

 

 AT 1i

∞

ATVA −1/2 Xj ATVA −1/2 − ATVA −1

fi = 1Ti A

j=0

∞

fi(j) where fi(j) def= 1Ti A ATVA −1/2 Xj ATVA −1/2 AT 1i .

=

j=1

Furthermore, using the deﬁnition of X we have that for even j

2 2

2 ATVA −1/2 AT 1i

j

fi(j) = X

2

j

= ATVA −1/2 AT (V − W)A ATVA −1

2 AT 1i

2

2

√

j

VA ATVA −1 AT (V − W)A ATVA −1

2 AT 1i

=

2 For odd j, using our deﬁnition of ∆+ and ∆− we have that

fi(j) = 1Ti A ATVA −1/2 Xj ATVA −1/2 AT 1i

j−1

= 1Ti A ATVA −1 AT (V − W)A

2 ATVA −1 AT (V − W)

j−1

×A ATVA −1 AT (V − W)A ATVA −1

2 AT 1i

= αi(j) − βi(j)

where

αi(j) def=

βi(j) def=

√

∆+A ATVA −1 AT (W − V)A ATVA −1

√

∆−A ATVA −1 AT (W − V)A ATVA −1

j−1

2 AT 1i

j−1

2 AT 1i

2

2

2

2

,

.

Consequently, by Lemma 32 and the construction, we see that

 

  =

∞

∞

t

2u 2u

fˆi(t+u)

fˆi(j) +

fi(j) = fi

Efˆi = E

u=1

j=1

j=1

and therefore Ehˆ = σ(w ) − σ( v) as desired. All that remains is to bound the variance of fˆi.

To bound the variance of fˆ, let |X| = ATVA −1/2 AT |W − V|A ATVA −1/2. Note that −41I −|X| X |X| 14I and consequently for all j

gi(j) def= 1Ti A ATVA −1/2 |X|j ATVA −1/2 AT 1i ≤

1

4j−1 1Ti A ATVA −1/2 |X| ATVA −1/2 AT 1i def=

1

vi4j−1 1Ti Pv∆Pv 1i where Pv =

√

√

VA ATVA −1/2 AT

V and ∆ is a diagonal matrix with ∆ii = wiv−vi

. Using that 0 Pv I, we have that for all j

i

m

(4j−1)2

i=1

vigi(j)

2

m

2

1Ti Pv∆Pv 1i

=

= Tr(Pv∆PvPv∆Pv) ≤ Tr(Pv∆∆Pv) = Tr(∆PvPv∆) ≤ Tr ∆2 =

i=1

m

2

wi − vi vi

≤ α2

i=1

and thus V g(j) 2 ≤ 44αj . Furthermore, since ∆+ |W − V| and ∆− |W − V| we have that αi(j) ≤ gi(j) and βi(j) ≤ gi(j). Consequently, by Lemma 32 again, we have

2

Vfˆ(j) − V f(j) 22 =

vi2 f ˆi(j) − fi(j)

i

2

vi2 α ˆi(j) − αi(j)

≤ 2

+ 2

i

i

2

vi2 αi(j)

+ βi(j)

≤ 2 2

i

2α2 2 (4j−1)2

2

vigi(j)

≤ 2 2

≤

.

i

vi2 β ˆi(j) − βi(j)

2

2

Putting this all together we have that

∞

t

Vfˆ− V f 2 ≤ 2uVfˆ(t+u) +

Vfˆ(j) −

V f(j) 2

j=1

j=1

∞

t

Vfˆ(j) − V f(j) 2 +

≤ 2u Vfˆ(t+u) 2 +

j=t+1

j=1

√2α  4j−1 +

∞

t

4α 4t+u

4α 4j

≤ 2u

+

j=1

j=t+1

α 4t

= O α  +

.

V f(j) 2

Consequently, since t = O(log( −1)) we have the desired result.

| |
|---|


###### 7.2 The Stochastic Chasing 0 Game

To avoid computing leverage scores exactly, in Section 7.1 we showed how to estimate the diﬀerence of leverage scores and use these to update the leverage scores. However, if we only applied this technique the error of leverage scores would accumulate in the algorithm and we need to ﬁx it. Naturally, one may wish to use dimension reduction to compute a multiplicative approximation to the leverage scores and update our computed value if the error is too large. However, this strategy would fail if there are too many rows with inaccurate leverage scores in the same iteration. In this case, we would change the central point too much that we are not able to recover. In this section, we present this update problem in a general form that we call Stochastic Chasing 0 game and provide an eﬀective strategy for playing this game.

The Stochastic chasing 0 game is as follows. There is a player, a stochastic adversary, and a point  x ∈ Rm. The goal of the player is to keep the point close to 0 ∈ Rm in ∞ norm and the goal of the stochastic adversary is to move  x away from 0. The game proceeds for an inﬁnite number of iterations where in each iteration the stochastic adversary moves the current point  x(k) ∈ Rm to some new point  x(k)+ ∆(k) ∈ Rm and the player needs to respond. The stochastic adversary cannot move the ∆(k) arbitrarily, instead he is only allowed to choose a probability distribution D(k) and

sample ∆(k) from it. Furthermore, it is required that ED(k) ∆ = 0 and ∆ 22 ≤ c for some ﬁxed c and all ∆ ∈ D(k). The player does not know  x(k) or the distribution D(k) or the move ∆(k) of the

stochastic adversary. All the player knows is some  y(k) ∈ Rn that is close to  x(k) in ∞ norm. With this information, the player is allowed to choose one coordinate i and set x(ik+1) to be zero and for other j, we have x(jk+1) = x(jk) + ∆(jk).

The question we would like to address is, what strategy the player should choose to keep  x(k) close to 0 in ∞ norm? We show that there is a trivial strategy that performs well: simply pick the

largest coordinate and set it to 0.

Algorithm 4: Stochastic chasing 0 game Constant: c > 0,R > 0. Let  x(1) = 0 ∈ Rm. for k = 1 to ∞ do

Stochastic Adversary: Pick D(k) such that ED(k) ∆ = 0 and ∆ 2 ≤ c all ∆ ∈ D(k). Stochastic Adversary: Pick  y(k) ∈ Rm such that  y(k) −  x(k) ∞ ≤ R. Player: Pick a coordinate i(k) using only  y(k). Sample ∆(k) from D(k). Set x(i(kk+1)) = 0 and x(jk+1) = x(jk) + ∆j(k) for all j = i.

###### end

- Theorem 34. Using the strategy i(k) = arg maxi yi(k) , with probability at least 1 − p, we have


 x(k) ∞ ≤ 2(c + R)log 4mk2/p for all k in the Stochastic Chasing 0 Game. Proof. Consider the potential function Φ( x) = i eαxi + i e−αxi where α is to be determined. Now for all x we know that ex ≤ 1 + x + x22e|x| and therefore for all |δ| ≤ c, x and α, we have

- 1

- 2


α2δ2eαx+|α|c . Consequently,

eαx+αδ ≤ eαx + αδeαx +

 

 

(k)

(k)

e−αx

E ∆∈D(k)Φ( x(k) + ∆) ≤ Φ( x(k)) + αE ∆∈D(k)

eαx

i ∆i −

i ∆i

i∈[m]

i∈[m]

 

  .

α2 2

(k)

(k)

eα ∆ ∞E ∆∈D(k)

e−αx

eαx

i ∆2i +

i ∆2i

+

i∈[m]

i∈[m]

(k)

(k)

i ∆i − i e−αx

Since ED(k) ∆ = 0 and ∆ 2 ≤ c, we have E ∆∈D(k) i eαx

i ∆i = 0 and

E ∆∈D(k)

i

(k)

eαx

i ∆2i +

i

(k)

e−αx

i ∆2i ≤ E ∆∈D(k)

≤ c2 max

i

i

∆2i max

i

(k)

e−αx

eαx

i + max

i

(k)

(k)

i ,maxi e−αx

Letting η(k) = max maxi eαx

i , we then have

(k)

(k) i

e−αx

eαx

i + max

i

(k)

i .

E ∆∈D(k)Φ( x(k) + ∆) ≤ Φ( x(k)) + α2eαcc2η(k).

Since i(k) = arg maxi yi(k) and  y(k) −  x(k) ∞ ≤ R, the player setting x(i(kk+1)) = 0 decreases Φ by at least e−α(R+c)η(k). Hence, we have

E ∆∈D(k)Φ( x(k+1)) ≤ Φ( x(k)) + α2eαcc2η(k) − e−αRη(k).

Picking α = 2(c+1 R), we have e2α(c+R)(α(c + R))2 ≤ 1 and hence α2eαcc2 ≤ e−α(R+c). Therefore, we have that

E ∆∈D(k)Φ( x(k+1)) ≤ EΦ( x(k)) ≤ ... ≤ Φ( x(1)) = 2m. Consequently, by Markov’s inequality we have that Pr[Φ( x(k)) ≥ λk] ≤ 2λm

###### for any λk. Furthermore, since clearly Φ( x) ≥ eα  x ∞ we have that Pr[  x(k) ∞ ≥ log(λk)/α] ≤ 2λm

k

for all k. Choosing λk = 4mkp 2 and taking a union bound over all k, we have that

k

 x(k) ∞ ≤ 2(c + R)log 4mk2/p for all k with probability at least

∞

∞

2m λk

1 −

= 1 −

i=1

k=1

p 2k2 ≥ 1 − p .

| |
|---|


Part II

# A User’s Guide to Cutting Plane Methods

#### 8 Introduction

Cutting plane methods have long been employed to obtain polynomial time algorithms for solving optimization problems. However, for many problems cutting plane methods are often regarded as ineﬃcient both in theory and in practice. Here, in Part II we provide several techniques for applying cutting plane methods eﬃciently. Moreover, we illustrate the eﬃcacy and versatility of these techniques by applying them to achieve improved running times for solving multiple problems including semideﬁnite programming, matroid intersection, and submodular ﬂow.

We hope these results revive interest in ellipsoid and cutting plane methods. We believe these results demonstrate how cutting plan methods are often useful not just for showing that a problem is solvable in polynomial time, but in many yield substantial running time improvements. We stress that while some results in Part II are problem-speciﬁc, the techniques introduced here are quite general and are applicable to a wide range of problems.

In the remainder of this introduction we survey the key techniques we use to apply our cutting plane method (Section 8.1) and the key results we obtain on improving the running time for solving various optimization problems (Section 8.2). We conclude in Section 8.3 by providing an overview of where to ﬁnd additional technical result in Part II.

###### 8.1 Techniques

Although cutting plane methods are typically introduced as algorithms for ﬁnding a point in a convex set (as we did with the feasibility problem in Part I), this is often not the easiest way to apply the methods. Moreover, improperly applying results on the feasibility problem to solve convex optimization problems can lead to vastly sub-optimal running times. Our central goal, here, in Part II is to provide tools that allow cutting plane methods to be eﬃciently applied to solve complex optimization problems. Some of these tools are new and some are extensions of previously known techniques. Here we brieﬂy survey the techniques we cover in Section 10 and Section 11.

###### Technique 0: From Feasibility to Optimization

- In Section 10.1, we explain how to use our cutting plane method to solve convex optimization problems using an approximate subgradient oracle. Our result is based on a result of Nemirovski [85] in which he showed how to use a cutting plane method to solve convex optimization problems without smoothness assumptions on the function and with minimal assumptions on the size of the function’s domain. We generalize his proof to accommodate for an approximate separation oracle, an extension which is essential for our applications. We use this result as the starting point for two new techniques we discuss below.

Technique 1: Dimension Reduction through Duality

- In Section 10.2, we discuss how cutting plane methods can be applied to obtain both primal and dual solutions to convex optimization problems. Moreover, we show how this can be achieved while only applying the cutting plane method in the space, primal or dual, which has a fewer number of variables. Thus we show how to use duality to improve the convergence of cutting plane methods while still solving the original problem.


To illustrate this idea consider the following very simple linear program (LP)

n

min

wixi

xi≥0, xi=1

i=1

where  x ∈ Rn and w  ∈ Rn. Although this LP has n variables, it should to be easy to solve purely on the grounds that it only has one equality constraint and thus dual linear program is simply

max

y ,

y≤wi∀i

i.e. a LP with only one variable. Consequently, we can apply our cutting plane method to solve it eﬃciently.

However, while this simple example demonstrates how we can use duality to decrease dimensions, it is not always obvious how to recover the optimal primal solution x variable given the optimal dual solution y. Indeed, for many problems their dual is signiﬁcantly simpler than itself (primal), so some work is required to show that working in the space suﬃces to require a primal solution.

One such recent example of this approach proving successful is a recent linear programming result [75]. In this result, the authors show how to take advantage of this observation and get a faster LP solver and maximum ﬂow algorithm. It is interesting to study how far this technique can extend, that is, in what settings can one recover the solution to a more diﬃcult dual problem from the solution to its easier primal problem?

There is in fact another precedent for such an approach. Gr¨tschel, Lov´sz and Schrijver[50] showed how to obtain the primal solution for linear program by using a cutting plane method to solve the linear program exactly. This is based on the observation that cutting plane methods are able to ﬁnd the active constraints of the optimal solution and hence one can take dual of the linear program to get the dual solution. This idea was further extended in [69] which also observed that cutting plane methods are incrementally building up a LP relaxation of the optimization problem. Hence, one can ﬁnd a dual solution by taking the dual of that relaxation.

In Section 10.2, we provide a fairly general technique to recover a dual optimal solution from an approximately optimal primal solution. Unfortunately, the performance of this technique seems quite problem-dependent. We therefore only analyze this technique for semideﬁnite programming (SDP), a classic and popular convex optimization problem. As a result, we obtain a faster SDP solver in both the primal and dual formulations of the problem.

###### Technique 2: Using Optimization Oracles Directly

In the seminal works of Gr¨tschel, Lov´sz, Schrijver and independently Karp and Papadimitriou [49, 64], they showed the equivalence between optimization oracles and separation oracles, and gave a general method to construct a separation oracle for a convex set given an optimization oracle for that set, that is an oracle for minimizing linear functionals over the set. This seminal result led to the ﬁrst weakly polynomial time algorithm for many algorithms such as submodular function minimization. Since then, this idea has been used extensively in various settings [62, 16, 17, 23].

Unfortunately, while this equivalence of separation and optimization is a beautiful and powerful tool for polynomial time solvability of problems, in many case it may lead to ineﬃcient algorithms. In order to use this reduction to get a separation oracle, the optimization oracle may need to be called multiple times – essentially the number of times needed to run a cutting plane method and hence may be detrimental to obtaining small asymptotic running times. Therefore, it is an interesting question of whether there is a way of using an optimization oracle more directly.

In Section 11 we provide a partial answer to this question for the case of a broad class of problems, that we call the intersection problem. For these problems we demonstrate how to achieve running time improvements by using optimization oracles directly. The problem we consider is as follows. We wish to solve the problem for some cost vector  c ∈ Rn and convex set K. We assume that the convex set K can be decomposed as K = K1 ∩ K2 such that max x∈K1  c, x and max x∈K2  c, x can each be solved eﬃciently. Our goal is to obtain a running time for this problem comparable to that of minimizing K given only a separation oracle for it.

We show that by considering a carefully regularized variant, we obtain a problem such that optimization oracles for K1 and K2 immediately yield a separation oracle for this regularized problem. By analyzing the regularizer and bounding the domains of the problem we are able to show that this allows us to eﬃciently compute highly accurate solutions to the intersection problem by applying our cutting plane method once. In other words, we do not need to use a complicated iterative scheme or directly invoke the equivalence between separation and optimization and thereby save O(poly(n)) factors in our running times.

We note that this intersection problem can be viewed as a generalization of the matroid intersection problem and in Section 11.2, we show our reduction gives a faster algorithm in certain parameter regimes. As another example, in Section 11.3 we show our reduction gives a substantial polynomial improvement for the submodular ﬂow problem. Furthermore, in Section 11.4 we show how our techniques allow us to minimize a linear function over the intersection of a convex set and an aﬃne subspace in a number of iterations that depends only on the co-dimension of the aﬃne space.

###### 8.2 Applications

Our main goal in Part II is to provide general techniques for eﬃciently using cutting plane methods for various problems. Hence, in Part II we use minimally problem-speciﬁc techniques to achieve the best possible running time. However, we also demonstrate the eﬃcacy of our approach by showing how techniques improve upon the previous best known running times for solve several classic problems in combinatorial and continuous optimization. Here we provide a brief overview of these applications, previous work on these problems, and our results.

In order to avoid deviating from our main discussion, our coverage of previous methods and techniques is brief. Given the large body of prior works on SDP, matroid intersection and submodular ﬂow, it would be impossible to have an in-depth discussion on all of them. Therefore, this section focuses on running time comparisons and explanations of relevant preivous techniques.

###### Semideﬁnite Programming

- In Section 10.2 we consider the classic semideﬁnite programming (SDP) problem:


bT y s.t.

C • X s.t. Ai • X = bi (primal) min

max

X 0

 y

n

yiAi C (dual)

i=1

where X, C, Ai are m × m symmetric matrices, b, y ∈ Rn, and A • B def= Tr(ATB). For many problems, n m2 and hence the dual problem has fewer variables than the primal. There are many results and applications of SDP; see [106, 101, 83] for a survey on this topic. Since our focus is on polynomial time algorithms, we do not discuss pseudo-polynomial algorithms such as the spectral bundle method [51], multiplicative weight update methods [8, 9, 61, 3], etc.

|Authors|Years<br><br>|Running times|
|---|---|---|


|Nesterov, Nemirovsky[89]|1992|O˜(√n(nmω + nω−1m2))<br><br>|
|---|---|---|
|Anstreicher [7]<br><br>|2000|O˜((mn)1/4(nmω + nω−1m2))|
|Krishnan, Mitchell [70]|2003|O˜(m(nω + mω + S)) (dual SDP)|
|This paper|2015<br><br>|O˜(m(n2 + mω + S))|


- Table 8: Previous algorithms for solving a n × n SDP with m constraints and S non-zeros entries


Currently, there are two competing approaches for solving SDP problems, namely interior point methods (IPM) and cutting plane methods. Typically, IPMs require fewer iterations than the cutting plane methods, however each iteration of these methods is more complicated and possibly more computationally expensive. For SDP problems, interior point methods require the computations of the Hessian of the function −log det(C − ni=1 yiAi) whereas cutting plane methods usually only need to compute minimum eigenvectors of the slack matrix C − ni=1 yiAi.

In [7], Anstreicher provided the current fastest IPM for solving the dual SDP problem using a method based on the volumetric barrier function. This method takes O((mn)1/4) iterations and each iteration is as cheap as usual IPMs. For general matrices C,X,Ai, each iteration takes O(nmω + nω−1m2) time where ω is the fast matrix multiplication exponent. If the constraint matrices Ai are rank one matrices, the iteration cost can be improved to O(mω + nm2 + n2m) [71]. If the matrices are sparse, then [40, 84] show how to use matrix completion inside the IPM. However, the running time depends on the extended sparsity patterns which can be much larger than the total number of non-zeros.

In [70], Krishnan and Mitchell observed that the separation oracle for dual SDP takes only

- O(mω + S) time, where S = ni=1 nnz(Ai) be the total number of non-zeros in the constant matrix. Hence, the cutting plane method by [105] gives a faster algorithm for SDP for many regimes. For ω = 2.38, the cutting plane method is faster when Ai is not rank 1 and the problem is


not too dense, i.e. ni=1 nnz(Ai) < n0.63m2.25. While there are previous methods for using cutting plane methods to obtain primal solutions[69] , to the best of our knowledge, there are no worst

case running time analysis for these techniques.

In Section 10.2, show how to alleviate this issue. We provide an improved algorithm for ﬁnding the dual solution and prove carefully how to obtain a comparable primal solution as well. See Figure 9.1 for a summary of the algorithms for SDP and their running times.

###### Matroid Intersection

- In Section 11.2 we show how our optimization oracle technique can be used to improve upon the previous best known running times for matroid intersection. Matroid intersection is one of the most fundamental problems in combinatorial optimization. The ﬁrst algorithm for matroid intersection is due to the seminal paper by Edmonds [26]. In Figures 9.2 and 9.3 we provide a summary of the previous algorithms for unweighted and weighted matroid intersection as well as the new running times we obtain in this paper. While there is no total ordering on the running times of these algorithms due to the diﬀerent dependence on various parameters, we would like to point out that our algorithms outperform the previous ones in regimes where r is close to n and/or the oracle query costs are relatively expensive. In particular, in terms of oracle query complexity our algorithms are the ﬁrst to achieve the quadratic bounds of O˜(n2) and O˜(nr) for independence and rank oracles. We hope our work will revive the interest in the problem of which progress has been mostly stagnated for the past 20-30 years.


|Authors|Years<br><br>|Running times|
|---|---|---|


|Edmonds [26]<br><br>|1968<br><br>|not stated|
|---|---|---|
|Aigner, Dowling [2]<br><br>|1971<br><br>|O(nr2Tind)|
|Tomizawa, Iri [102]<br><br>|1974|not stated|
|Lawler [72]<br><br>|1975<br><br>|O(nr2Tind)|
|Edmonds [28]|1979|not stated|
|Cunningham [21]|1986<br><br>|O(nr1.5Tind)|
|This paper|2015|O(n2 log nTind + n3 logO(1) n) O(nr log2 nTrank + n3 logO(1) n)|


- Table 9: Previous algorithms for (unweighted) matroid intersection. Here n is the size of the ground set, r = max{r1,r2} is the maximum rank of the two matroids, Tind is the time needed to check if a set is independent (independence oracle), and Trank is the time needed to compute the rank of a given set (rank oracle).

|Authors<br><br>|Years|Running times|
|---|---|---|


|Edmonds [26]|1968<br><br>|not stated|
|---|---|---|
|Tomizawa, Iri [102]<br><br>|1974|not stated|
|Lawler [72]|1975|O(nr2Tind + nr3)|
|Edmonds [28]|1979<br><br>|not stated|
|Frank [33]|1981<br><br>|O(n2r(Tcircuit + n))|
|Orlin, Ahuja [91]<br><br>|1983<br><br>|not stated|
|Brezovec, Cornu´ejols, Glover[14]<br><br>|1986<br><br>|O(nr(Tcircuit + r + log n))|
|Fujishige, Zhang [39]|1995<br><br>|O(n2r0.5 log rM · Tind)|
|Shigeno, Iwata [96]<br><br>|1995<br><br>|O((n + Tcircuit)nr0.5 log rM)|
|This paper<br><br>|2015<br><br>|O((n2 log nTind + n3 logO(1) n)log nM) O((nr log2 nTrank + n3 logO(1) n)log nM)|


- Table 10: Previous algorithms for weighted matroid intersection. In additions to the notations used


in the unweighted table, Tcircuit is the time needed to ﬁnd a fundamental circuit and M is the bit complexity of the weights.

###### Minimum-Cost Submodular Flow

In Section 11.3 we show how our optimization oracle technique can be used to improve upon the previous best known running times for (Minimum-cost) Submodular Flow. Submodular ﬂow is a very general problem in combinatorial optimization which generalizes many problems such as minimum cost ﬂow, the graph orientation, polymatroid intersection, directed cut covering [37]. In Figure 9.4 we provide an overview of the previous algorithms for submodular ﬂow as well as the new running times we obtain in this paper.

Many of the running times are in terms of a parameter h, which is the time required for computing an “exchange capacity”. To the best of our knowledge, the most eﬃcient way of computing an exchange capacity is to solve an instance of submodular minimization which previously took time O˜(n4EO + n5) (and now takes O˜(n2EO + n3) time using our result in Part III). Readers may wish to substitute h = O˜(n2EO + n3) when reading the table.

The previous fastest weakly polynomial algorithms for submodular ﬂow are by [59, 30, 32], which take time O˜(n6EO + n7) and O(mn5 log nU · EO), assuming h = O˜(n2EO + n3). Our algorithm for submodular ﬂow has a running time of O˜(n2EO + n3), which is signiﬁcantly faster by roughly a factor of O˜(n4).

For strongly polynomial algorithms, our results do not yield a speedup but we remark that our faster strongly polynomial algorithm for submodular minimization in Part III improves the previous algorithms by a factor of O˜(n2) as a corollary (because h requires solving an instance of submodular minimization).

###### 8.3 Overview

After providing covering some preliminaries on convex analysis in Section 9 we split the remainder of Part II into Section 10 and Section 11. In Section 10 we cover our algorithm for convex optimization using an approximate subgradient oracle (Section 10.1) as well as our technique on using duality to decrease dimensions and improve the running time of semideﬁnite programming (Section 10.2). In Section 11 we provide our technique for using minimization oracles to minimize functions over the intersection of convex sets and provide several applications including matroid intersection (Section 11.2), submodular ﬂow (Section 11.3), and minimizing a linear function over the intersection of an aﬃne subspace and a convex set (Section 11.4).

#### 9 Preliminaries

In this section we review basic facts about convex functions that we use throughout Part II. We also introduce two oracles that we use throughout Part II, i.e. subgradient and optimization oracles, and provide some basic reductions between them. Note that we have slightly extended some deﬁnitions and facts to accommodate for the noisy separation oracles used in this paper.

First we recall the deﬁnition of strong convexity

- Deﬁnition 35 (Strong Convexity ). A real valued function f on a convex set Ω is α-strongly convex if for any  x, y ∈ Ω and t ∈ [0,1], we have


1 2

αt(1 − t)  x −  y 2 ≤ tf( x) + (1 − t)f( y).

f(t x + (1 − t) y) +

Next we deﬁne an approximate subgradient.

|Authors<br><br>|Years|Running times|
|---|---|---|


|Fujishige [35]|1978<br><br>|not stated|
|---|---|---|
|Gr¨tschel, Lov´sz, Schrijver[49]|1981|weakly polynomial|
|Zimmermann [113]|1982<br><br>|not stated|
|Barahona, Cunningham [12]<br><br>|1984|not stated|
|Cunningham, Frank [22]|1985<br><br>|→ O(n4hlog C)|
|Fujishige [36]|1987<br><br>|not stated|
|Frank, Tardos [34]|1987|strongly polynomial|
|Cui, Fujishige [108]<br><br>|1988|not stated|
|Fujishige, R¨ck, Zimmermann[38]<br><br>|1989|→ O(n6hlog n)|
|Chung, Tcha [18]|1991<br><br>|not stated|
|Zimmermann [114]|1992<br><br>|not stated|
|McCormick, Ervolina [82]<br><br>|1993|O(n7h∗ log nCU)|
|Wallacher, Zimmermann [109]|1994<br><br>|O(n8hlog nCU)|
|Iwata [52]|1997<br><br>|O(n7hlog U)|
|Iwata, McCormick, Shigeno [57]|1998|O n4hmin log nC,n2 log n|
|Iwata, McCormick, Shigeno [58]|1999<br><br>|O n6hmin log nU,n2 log n|
|Fleischer, Iwata, McCormick[32]|1999<br><br>|O n4hmin log U,n2 log n|
|Iwata, McCormick, Shigeno [59]|1999<br><br>|O n4hmin log C,n2 log n|
|Fleischer, Iwata [30]<br><br>|2000|O(mn5 log nU · EO)|
|This paper<br><br>|2015|O(n2 log nCU · EO + n3 logO(1) nCU)|


###### Figure 8.1: Previous algorithms for Submodular Flow with n vertices, maximum cost C and maximum capacity U. The factor h is the time for an exchange capacity oracle, h∗ is the time for a “more complicated exchange capacity oracle” and EO is the time for evaluation oracle of the submodular function. The arrow,→, indicates that it used currently best maximum submodular ﬂow algorithm as subroutine which was non-existent at the time of the publication.

- Deﬁnition 36 (Subgradient). For any convex function f on a convex set Ω, the δ-subgradients of f at x are deﬁned to be


∂δf( x) def= { g ∈ Ω : f( y) + δ ≥ f( x) +  g, y −  x for all  y ∈ Ω}.

Here we provide some basic facts regarding convexity and subgradients. These statements are natural extensions of well known facts regarding convex functions and their proof can be found in any standard textbook on convex optimization.

Fact 37. For any convex set Ω and  x be a point in the interior of Ω, we have the following:

- 1. If f is convex on Ω, then ∂0f( x) = ∅ and ∂sf( x) ⊆ ∂tf( x) for all 0 ≤ s ≤ t.Otherwise, we have  g 2 > 12 Dδ . For any f( y) ≤ f( x), we have δ ≥  g, y −  x and hence

- 2. If f is a diﬀerential convex function on Ω, then ∇f( x) ∈ ∂0f( x).
- 3. If f1 and f2 are convex function on Ω,  g1 ∈ ∂δ1f1( x) and  g2 ∈ ∂δ2f1( x), then α g1 + β g2 ∈ ∂αδ1+βδ2( g1 +  g2)( x).
- 4. If f is α-strongly convex on Ω with minimizer x∗, then for any  y with f( y) ≤ f( x∗) + , we have 12α  x∗ −  y 2 ≤ .


Next we provide a reduction from subgradients to separation oracles. We will use this reduction several times in Part II to simplify our construction of separation oracles. Lemma 38. Let f be a convex function. Suppose we have  x and  g ∈ ∂δf( x) with  x 2 ≤ 1 ≤ D and δ ≤ 1. If  g 2 ≤ 12 Dδ , then f( x) ≤ min  y2 2≤D f( y) + 2

√

δD and if  g 2 ≤ 12 Dδ then

√

{  y 2 ≤ D : f( y) ≤ f( x)} ⊂ { y : dT y ≤ dT x + 2

δD}

√

√

δD)-separation oracle on the set {  x 2 ≤ D}. Proof. Let  y such that  y 2 ≤ D. By the deﬁnition of δ-subgradient, we have

with d =  g/  g 2. Hence, this gives a (2

δD,2

f( y) + δ ≥ f( x) +  g, y −  x .

√

If  g ≤ 21 Dδ , then, we have |  g, y −  x | ≤

δD because  x ≤ D and  y 2 ≤ D. Therefore, min

√

δD ≥ f( x).

f( y) + 2

 y 2≤D

Otherwise, we have  g 2 > 12 Dδ . For any f( y) ≤ f( x), we have δ ≥  g, y −  x and hence

√

δD ≥

2

 g  g

, y −  x .

| |
|---|


At several times in Part II we will wish to construct subgradient oracles or separation oracles given only the ability to approximately maximize a linear function over a convex set. In the remainder of this section we formally deﬁne such a optimization oracle and prove this equivalence.

Deﬁnition 39 (Optimization Oracle). Given a convex set K and δ > 0 a δ-optimization oracle for K is a function on Rn such that for any input  c ∈ Rn, it outputs  y such that

 c, x ≤  c, y + δ.

max

 x∈K

We denote by OOδ(K) the time complexity of this oracle. Lemma 40. Given a convex set K, any -optimization oracle for K is a -subgradient oracle for f( c) def= max x∈K  c, x . Proof. Let  xc be the output of -optimization oracle on the cost vector  c. We have

max

 x∈K

 c, x ≤  c, xc +  .

Hence, for all d, we have and therefore

 xc, d − c + f( c) ≤ f( d) +  . Hence,  xc ∈ ∂δf( c).

| |
|---|


Combining these lemmas shows that having an -optimization oracle for a convex set K contained in a ball of radius D yields a O(

√

√

D ) separation oracle for maxx∈K  c, x . We use these ideas to construction separation oracles throughout Part II.

D ,

#### 10 Convex Optimization

In this section we show how to apply our cutting plane method to eﬃciently solve problems in convex optimization. First, in Section 10.1 we show how to use our result to minimize a convex function given an approximate subgradient oracle. Then, in Section 10.2 we illustrate how this result can be used to obtain both primal and dual solutions for a standard convex optimization problems. In particular, we show how our result can be used to obtain improved running times for semideﬁnite programming across a range of parameters.

###### 10.1 From Feasibility to Optimization

In this section we consider the following standard optimization problem. We are given a convex function f : Rn → R ∪ {+∞} and we want to ﬁnd a point  x that approximately solves the minimization problem

f( x) given only a subgradient oracle for f.

min

 x∈Rn

Here we show how to apply the cutting plane method from Part I turning the small width guarantee of the output of that algorithm into a tool to ﬁnd an approximate minimizer of f. Our result is applicable to any convex optimization problem armed with a separation or subgradient oracle. This result will serve as the foundation for many of our applications in Part II.

Our approach is an adaptation of Nemiroski’s method [85] which applies the cutting plane method to solve convex optimiziation problems, with only minimal assumption on the cutting plane method. The proof here is a generalization that accommodates for the noisy separation oracle used in this paper. In the remainder of this subsection we provide a key deﬁnition we will use in our algorithm (Deﬁntion 41), provide our main result (Theorem 42), and conclude with a brief discussion of this result.

Deﬁnition 41. For any compact set K, we deﬁne the minimum width by MinWidth(K) def= min  a 2=1 max x,y ∈K  a, x −  y .

Theorem 42. Let f be a convex function on Rn and Ω be a convex set that contains a minimizer of f. Suppose we have a (η,δ)-separation oracle for f and Ω is contained inside B∞(R). Using B∞(R) as the initial polytope for our Cutting Plane Method, for any 0 < α < 1, we can compute

-  x ∈ Rn such that

f( x) − min

 y∈Ω

f( y) ≤ η + α max

 y∈Ω

f( y) − min

 y∈Ω

f( y) . (10.1) with an expected running time of

O nSOη,δ(f)log

nκ α

+ n3 logO(1)

nκ α

,

where δ = Θ αMinWidth(Ω)n3/2 ln(κ) and κ = MinWidth(Ω)R . Furthermore, we only need the oracle deﬁned on the set B∞(R).

Proof. Let  x∗ ∈ arg min x∈Ω f( x). Since B∞(R) ⊃ Ω contains a minimizer of f, by the deﬁnition of (η,δ)-separation oracles, our Cutting Plane Method (Theorem 31) either returns a point  x that is almost optimal or returns a polytope P of small width. In the former case we have a point  x such that f( x) ≤ min y f( y) + η. Hence, the error is clearly at most η + α (maxz ∈Ω f(z ) − min x∈Ω f( x)) as desired. Consequently, we assume the latter case.

Theorem 31 shows MinWidth(P) < Cn ln(R/ ) for some universal constant C. Picking

= C

αMinWidth(Ω) nln nκα

(10.2)

for small enough constant C , we have MinWidth(P(i)) < αMinWidth(Ω). Let Ωα =  x∗+α(Ω− x∗), namely, Ωα = { x∗ + α(z  −  x∗) : z  ∈ Ω}. Then, we have

MinWidth(Ωα) = αMinWidth(Ω) > MinWidth(P).

Therefore, Ωα is not a subset of P(i) and hence there is some point  y ∈ Ωα\P. Since Ωα ⊆ Ω ⊆ B∞(R), we know that  y does not violate any of the constraints of P(0) and therefore must violate one of the constraints added by querying the separation oracle. Therefore, for some j ≤ i, we have

 c(j−1), y >  c(j−1), x(j−1) + cs /√n . By the deﬁnition of (η,cs /√n)-separation oracle (Deﬁnition 2), we have f( y) > f( x(j−1)). Since

-  y ∈ Ωα, we have  y = (1 − α) x∗ + αz  for some z  ∈ Ω. Thus, the convexity of f implies that f( y) ≤ (1 − α)f( x∗) + αf(z ).


Therefore, we have min

f( x) < f( y) − f( x∗) ≤ α max z ∈Ω

f( x(k)) − min  x∈Ω

f(z ) − min

f( x) .

1≤k≤i

 x∈Ω

Hence, we can simply output the best  x among all  x(j) and in either case  x satisﬁes (10.1).

Note that we need to call (η,δ)-separation oracle with δ = Ω( /√n) to ensure we do not cut out  x∗. Theorem 31 shows that the algorithm takes O(nSOη,δ(f)log(nR/ ) + n3 logO(1)(nR/ )) expected time, as promised. Furthermore, the oracle needs only be deﬁned on B∞(R) as our cutting plane method guarantees  x(k) ∈ B∞(R) for all k (although if needed, an obvious separating hyperplane can be returned for a query point outside B∞(R) ).

| |
|---|


Observe that this algorithm requires no information about Ω (other than that Ω ⊆ B∞(R)) and does not guarantee that the output is in Ω. Hence, even though Ω can be complicated to describe, the algorithm still gives a guarantee related to the gap max x∈Ω f( x) − min x∈Ω f( x). For speciﬁc applications, it is therefore advantageous to pick a Ω as large as possible while the bound on function value is as small as possible.

Before indulging into speciﬁc applications, we remark on the dependence on κ. Using John’s ellipsoid, it can be shown that any convex set Ω can be transformed linearly such that (1) B∞(1) contains Ω and, (2) MinWidth(Ω) = Ω(n−3/2). In other words, κ can be eﬀectively chosen as O(n3/2). Therefore if we are able to ﬁnd such a linear transformation, the running time is simply O nSO(f)log (n/α) + n3 logO(1) (n/α) . Often this can be done easily using the structure of the particular problem and the running time does not depend on the size of domain at all.

###### 10.2 Duality and Semideﬁnite Programming

In this section we illustrate how our result in Section 10.1 can be used to obtain both primal and dual solutions for standard problems in convex optimization. In particular we show how to obtain improved running times for semideﬁnite programming.

To explain our approach, consider the following minimax problem min

max

A x, y +  c, x + d, y (10.3)

 y∈Y

 x∈X

where  x ∈ Rm and  y ∈ Rn. When m n, solving this problem by directly using Part I could lead to an ineﬃcient algorithm with running time at least m3. In many situations, for any ﬁxed  y, the problem max x∈X A x, y is very easy and hence one can use it as a separation oracle and apply Part I and this would gives a running time almost independent of m. However, this would only give us the  y variable and it is not clear how to recover  x variable from it.

In this section we show how to alleviate this issue and give semideﬁnite programming (SDP)

- as a concrete example of how to apply this general technique. We do not write down the general version as the running time of the technique seems to be problem speciﬁc and faster SDP is already an interesting application.


For the remainder of this section we focus on the semideﬁnite programming (SDP) problem: max

C • X s.t. Ai • X = bi (10.4) and its dual

X 0

n

bT y s.t.

min

yiAi C (10.5)

 y

i=1

where X, C, Ai are m × m symmetric matrices and b, y ∈ Rn. Our approach is partially inspired by one of the key ideas of [51, 70]. These results write down the dual SDP in the form

n

bT y − K min(λmin(

min

y

i=1

yiAi − C),0) (10.6)

for some large number K and use non-smooth optimization techniques to solve the dual SDP problem. Here, we follow the same approach but instead write it as a max-min problem min y fK( y) where

n

bT y + X,C −

fK( y) = max

yiAi . (10.7)

TrX≤K,X 0

i=1

Thus the SDP problem in fact assumes the form (10.3) and many ideas in this section can be generalized to the minimax problem (10.3).

To get a dual solution, we notice that the cutting plane method maintains a subset of the primal feasible solution conv(Xi) such that

bT y + max

min

TrX≤K,X 0

 y

X,C −

n

bT y + max

yiAi ∼ min

 y

X∈conv(Xi)

i=1

n

X,C −

yiAi .

i=1

Applying minimax theorem, this shows that there exists an approximation solution X in conv(Xi) for the primal problem. Hence, we can restrict the primal SDP on the polytope conv(Xi), this reduces the primal SDP into a linear program which can be solved very eﬃciently. This idea of getting primal/dual solution from the cutting plane method is quite general and is the main purpose of this example. As a by-product, we have a faster SDP solver in both primal and dual! We remark that this idea has been used as a heuristic to obtain [69] for getting the primal SDP solution and our contribution here is mainly the asymptotic time analysis.

We ﬁrst show how to construct the separation oracle for SDP. For that we need to compute smallest eigenvector of a matrix. Below, for completeness we provide a folklore result showing we can do this using fast matrix multiplication.

- Lemma 43. Given a n × n symmetric matrix Y such that −RI Y RI, for any > 0, with high probability in n in time O(nω+o(1) logO(1)(R/ )) we can ﬁnd a unit vector  u such that  uTY u ≥ λmax(Y) − .


Proof. Let B def= R1 Y + I. Note that B 0. Now, we consider the repeated squaring B0 = B and Bk+1 = B

2 k

TrB2k. Let 0 ≤ λ1 ≤ λ2 ≤ ··· ≤ λn be the eigenvalues of B and  vi be the corresponding eigenvectors. Then, it is easy to see the the eigenvalues of Bk are λ

2k i

.

n i=1 λ2ik

Let q  be a random unit vector and  r def= Bkq . Now q  = αi vi for some αi such that αi2 = 1. Letting

αiλ2ik vi

p  = λi>(1−δ)λn

n i=1 λ2ik

we have

αiλ2ik vi

λ2ik

 r − p  2 = λi≤(1−δ)λn

n i=1 λ2ik 2 ≤ λi≤(1−δ)λn

n i=1 λ2ik ≤ (1 − δ)2kn.

3/2/δ) δ , we have  r − p  2 ≤ δ/√n. Since 0 B 2I, we have

Letting k = log2 log(n

√

 rTB r ≥ p TBp  − ( r − p )TB( r − p ) ≥ p TBp  − 2δ/√n. Note that p  involves only eigenvectors between (1 − δ)λn to λn. Hence, we have √

 rTB r ≥ (1 − δ)λn p  2 − 2δ/√n.

With constant probability, we have αn = Ω(1/√n). Hence, we have p  2 = Ω(1/√n). Using B 2I and p  2 ≥  r 2 − δ/√n we have that so long as δ is a small enough universal constant

√

(1 − δ)λn p  2 − 2δ/√n p  2 + δ/√n

 rTB r  r 2 ≥

= (1 − O(δ)) λn − O(δ)

√

= λn − O(δ

R). Therefore, we have  rTY r

2 ≥ λmax(Y) − O(Rδ). Hence, we can ﬁnd vector  r by computing k matrix multiplications. [24] showed that fast matrix multiplication is stable under Frobenius norm, i.e., for any η > 0, using O(log(n/b)) bits, we can ﬁnd C such that C − AB F ≤ 1b A B in time O(nω+η) where ω is the matrix multiplicative constant. Hence, this algorithm takes only

 r

- O(nω+o(1) logO(1)(δ−1)) time. The result follows from renormalizing the vector  r, repeating the algorithm O(log n) times to boost the probability and taking δ = Ω( /R).


| |
|---|


The following lemma shows how to compute a separation for fK deﬁned in (10.7).

- Lemma 44. Suppose that Ai F ≤ M and C F ≤ M. For any 0 < < 1 and  y with  y 2 =


O(L), with high probability in m, we can compute a ( , )-separation of fK on {  x 2 ≤ L} at  y in time O(S + mω+o(1) logO(1)(nKML/ )) where where S is the sparsity of the problem deﬁned as

nnz(C) + ni=1 nnz(Ai). Proof. Note that −O(nML)I C− ni=1 yiAi O(nML)I. Using Lemma 43, we can ﬁnd a vector  v with  v 2 = K in time O(mω+o(1) logO(1)(nKML/δ)) such that

 vT C −

n

yiAi  v ≥ max

TrX≤K,X 0

i=1

X,C −

n

yiAi − δ. (10.8)

i=1

In other words, we have a δ-optimization oracle for the function fK. Lemma 40 shows this yields a δ-subgradient oracle and Lemma 38 then shows this yields a O(

√

√

δL) -separation oracle on the set {  x 2 ≤ L}. By picking δ = 2/L, we have the promised oracle.

δL),O(

| |
|---|


With the separation oracle in hand, we are ready to give the algorithm for SDP:

Theorem 45. Given a primal-dual semideﬁnite programming problem in the form (10.4) and (10.5), suppose that for some M ≥ 1 we have

- 1. b 2 ≤ M, C F ≤ M and Ai F ≤ M for all i.
- 2. The primal feasible set lies inside the region TrX ≤ M.
- 3. The dual feasible set lies inside the region  y ∞ ≤ M.


Let OPT be the optimum solution of (10.4) and (10.5). Then, with high probability, we can ﬁnd X and  y such that

- 1. X 0, TrX = O(M), i |bi − X,Ai | ≤ for all i and C • X ≥ OPT −  .
- 2.  y ∞ = O(M), ni=1 yiAi C − I and bT y ≤ OPT +  .


in expected time O nS + n3 + nmω+o(1) logO(1) nM where S is the sparsity of the problem deﬁned as nnz(C) + ni=1 nnz(Ai) and ω is the fast matrix multiplication constant. Proof. Let K ≥ M be some parameter to be determined. Since the primal feasible set is lies inside the region TrX ≤ M ≤ K, we have

bT y = max

###### C • X

min

n i=1 yiAi C

X 0,TrX≤K,Ai•X=bi

###### C • X −

yi (Ai • X − bi)

= max

min

X 0,TrX≤K

 y

i

= min

max

X 0,TrX≤K

 y

= min

fK( y).

 y

bT y + (C −

i

yiAi) • X

Lemma 44 shows that it takes SOδ,δ(fK) = O(S + mω+o(1) log(nKML/δ)) time to compute a (δ,δ)-separation oracle of fK for any point  y with  y ∞ = O(L) where L is some parameter with L ≥ M. Taking the radius R = L, Theorem 42 shows that it takes O nSOδ,δ(fK)log α n + n3 logO(1) α n expected time with δ = Θ αn−3/2L to ﬁnd  y such that

  ≤ δ + 2α (nML + 2nKML).

  max

fK( y) − min

fK( y) ≤ δ + α

fK( y) − min

fK( y)

 y ∞≤L

 y ∞≤L

 y ∞≤L

Picking α = 7nMKL, we have fK( y) ≤ min y fK( y) +  . Therefore,

n

bT y + K max(λmax(C −

yiAi),0) ≤ OPT +  .

i=1

Let β = max(λmax(C − ni=1 yiAi),0). Then, we have that ni=1 yiAi C − βI and

bT y

bT y ≥ min n i=1 yiAi C−βI

(C − βI) • X ≥ OPT − βM

= max

X 0Ai•X=bi

because TrX ≤ M. Hence, we have

OPT − βM + βK ≤ bT y + K max(λmax(C −

n

yiAi),0) ≤ OPT +

i=1

Putting K = M + 1, we have β ≤ . Thus,

n

###### yiAi C − I.

i=1

This gives the result for the dual with the running time O nS + n3 + nmω+o(1) logO(1) nML .

Our Cutting Plane Method accesses the sub-problem max

###### (C −

yiAi) • X

X 0,TrX≤K

i

only through the separation oracle. Let z  be the output of our Cutting Plane Method and { vi viT}Oi=1(n) be the matrices used to construct the separation for the O(n) hyperplanes the algorithm maintains

- at the end. Let  u be the maximum eigenvector of C − ni=1 ziAi. Now, we consider a realization of fK


n

f˜K( y) = bT y + max

X,C −

yiAi .

X∈conv(K u uT , vi viT )

i=1

Since applying our Cutting Plane Method to either fK or f˜K gives the same result, the correctness of the our Cutting Plane Method shows that

f˜K(z ) ≤ min

f˜K( y) +  .

 y ∞≤L

Note that the function f˜K is deﬁned such that f˜K(z ) = fK(z ). Hence, we have min

f˜K( y) +  .

fK( y) ≤ fK(z ) ≤ f˜K(z ) ≤ min

 y ∞≤L

 y ∞≤L

Also, note that f˜K( x) ≤ fK( x) for all  x. Hence, we have min

f˜( y) ≤ min

fK( y) − ≤ min

fK( y).

 y ∞≤L

 y ∞≤L

 y ∞≤L

Now, we consider the primal version of f˜, namely

g(X) def= min

bT y + X,C −

 y ∞≤L

n

yiAi .

i=1

Sion’s minimax theorem [98] shows that OPT ≥ max

f˜( y) ≥ OPT −  .

g(X) = min

X∈conv(K u uT , vi viT )

 y ∞≤L

Therefore, to get the primal solution, we only need to ﬁnd  u by Lemma 43 and solve the maximization problem on g. Note that

n

yi (bi − X,Ai ) + X,C

g(X) = min

 y ∞≤L

i=1

= −L

|bi − X,Ai | + X,C .

i

For notation simplicity, we write K u uT =  v0 v0T. Then, X = Oj=0(n) αj vj vjT for some αj = 1 and αj ≥ 0. Substituting this into the function g, we have

g( α) = −L

j

bi −

j

αj vjTAi vj +

j

αj vjTC vj.

Hence, this can be easily written as a linear program with O(n) variables and O(n) constraints in time O(nS). Now, we can apply interior point method to ﬁnd  α such that

g( α) ≥ max

g(X) − ≥ OPT − 2 .

X∈conv(K u uT , vi viT )

Let the corresponding approximate solution be X = αj vj vjT. Then, we have

X,C − L

i

|bi − X,Ai | ≥ OPT − 2 .

Now, we let ˜bi = X,Ai . Then, we note that

X,C ≤ max

###### C • X

X 0Ai•X=˜bi

˜bTi  y ≤ OPT + M

= min

n i=1 yiAi C

bi − X,Ai

i

because  y ∞ ≤ M. Hence, we have OPT + (M − L)

bi − X,Ai ≥ X,C − L

i

i

Now, we put L = M + 2, we have

bi − X,Ai ≥ OPT − 2 .

i

bi − X,Ai ≤  .

This gives the result for the primal. Note that it only takes O(n5/2 logO(1)(nM/ )) to solve a linear program with O(n) variables and O(n) constraints because we have an explicit interior point deep inside the feasible set, i.e. αi = m1 for some parameter m [76].5 Hence, the running time is dominated by the cost of cutting plane method which is O nS + n3 + nmω+o(1) logO(1) nM by putting L = M + 2.

| |
|---|


We leave it as an open problem if it is possible to improve this result by reusing the computation in the separation oracle and achieve a running time of O nS + n3 + nm2 logO(1) nM .

#### 11 Intersection of Convex Sets

In this section we introduce a general technique to optimize a linear function over the intersection of two convex sets, whenever the linear optimization problem on each of them can be done eﬃciently. At the very high level, this is accomplished by applying cutting plane to a suitably regularized version of the problem. In Section 11.1 we present the technique and in the remaining sections we provide several applications including, matroid intersection (Section 11.2), submodular ﬂow (Section 11.3), and minimizing over the intersection of an aﬃne subspace and a convex set (Section 11.4).

5Without this, the running time of interior point method depends on the bit complexity of the linear programs.

- 11.1 The Technique Throughout this section we consider variants of the following general optimization problem


max

 c, x (11.1)

 x∈K1∩K2

where  x, c ∈ Rn, K1 and K2 are convex subsets of Rn. We assume that max

 x 2 < M,  c 2 ≤ M (11.2) for some constant M ≥ 1 and we assume that

 x 2 < M, max  x∈K2

 x∈K1

K1 ∩ K2 = ∅. (11.3)

Instead of a separation oracle, we assume that K1 and K2 each have optimization oracles (see Section 9).

To solve this problem we ﬁrst introduce a relaxation for the problem (11.1) that we can optimize eﬃciently. Because we have only the optimization oracles for K1 and K2, we simply have variables  x and  y for each of them in the objective. Since the output should (approximately) be in the

intersection of K1 and K2, a regularization term −λ2  x −  y 22 is added to force  x ≈  y where λ is a large number to be determined later. Furthermore, we add terms to make the problem strong

concave.

- Lemma 46. Assume (11.2) and (11.3). For λ ≥ 1, let


- 1

- 2


λ 2

1 2

- 1

- 2λ


- 1

- 2λ


 x −  y 22 −

 x 22 −

 y 22 . (11.4)

fλ( x, y) def=

 c, y −

 c, x +

There is an unique maximizer ( xλ, yλ) for the problem max x∈K1, y∈K2 fλ( x, y). The maximizer ( xλ, yλ) is a good approximation of the solution of (11.1), i.e.  xλ −  yλ 22 ≤ 6Mλ 2 and

M2 λ

 c, x ≤ fλ( xλ, yλ) +

max

. (11.5)

 x∈K1∩K2

Proof. Let  x∗ be a maximizer of max x∈K1∩K2  c, x . By assumption (11.2),  x∗ 2 ≤ M, and therefore

 x∗ 22 λ ≥ max

M2 λ

fλ( x∗, x∗) =  c, x∗ −

 c, x −

. (11.6)

 x∈K1∩K2

This shows (11.5). Since fλ is strongly concave in  x and  y, there is a unique maximizer ( xλ, yλ). Let OPTλ = fλ( xλ, yλ). Then, we have

- 1

- 2


λ 2

- 1

- 2


 xλ −  yλ 22 ≤

 c 2  yλ 2 −

OPTλ ≤

 c 2  xλ 2 +

M2 2

M2 2 −

λ 2

 xλ −  yλ 22. On the other hand, using λ ≥ 1, (11.6) shows that

+

M2

OPTλ ≥ fλ( x∗, x∗) ≥ max

λ ≥ −2M2. Hence, we have

 c, x −

 x∈K1∩K2

 xλ −  yλ 22 ≤

2 M2 − OPTλ λ ≤

6M2 λ

. (11.7)

Now we write maxfλ( x, y) as a max-min problem. The reason for doing this is that the dual approximate solution is much easier to obtain and there is a way to read oﬀ a primal approximate solution from a dual approximate solution. This is analogous to the idea in [73] which showed how to convert a cut solution to a ﬂow solution by adding regularization terms into the problem.

- Lemma 47. Assume (11.2) and (11.3). Let λ ≥ 2. For any  x ∈ K1 and  y ∈ K2, the function fλ can be represented as


fλ( x, y) = min

gλ( x, y, θ1, θ2, θ3) (11.8)

( θ1, θ2, θ3)∈Ω

where Ω = {( θ1, θ2, θ3) : θ1 2 ≤ 2M, θ2 2 ≤ M, θ3 2 ≤ M} and

 c 2

θ2 λ

 c 2 − λ θ1 +

θ3 λ

λ 2

- 1

- 2λ


- 1

- 2λ


θ1 22 +

θ2 22 +

θ3 22. (11.9)

gλ( x, y, θ1, θ2, θ3) =

+ λ θ1 +

, x +

, y +

Let hλ( θ1, θ2, θ3) = max x∈K1, y∈K2 gλ( x, y, θ1, θ2, θ3). For any ( θ 1, θ 2, θ 3) such that hλ( θ 1, θ 2, θ 3) ≤ min( θ

1, θ2, θ3)∈Ω hλ( θ1, θ2, θ3) +  , we know z  = 21( θ 2 + θ 3) satisﬁes

20M2 λ

+ 20λ3 .

 c, x ≤  c,z  +

max

 x∈K1∩K2

√

2λ + 6Mλ 2 where ( xλ, yλ) is the unique maximizer for the problem

and z − xλ 2+ z − yλ 2 ≤ 4

max x∈K1, y∈K2 fλ( x, y). Proof. Note that for any ξ 2 ≤ α, we have

- 1

- 2


- 1

- 2


ξ 22 = min

θ 22

−

θ, ξ +

θ 2≤α

Using this and (11.2), we have (11.8) for all  x ∈ K1 and  y ∈ K2 as desired. Since Ω is closed and bounded set and the function gλ is concave in ( x, y) and convex in ( θ1, θ2, θ3), Sion’s minimax theorem [98] shows that

max

fλ( x, y) = min

 x∈K1, y∈K2

( θ1, θ2, θ3)∈Ω

hλ( θ1, θ2, θ3) (11.10)

Since fλ is strongly concave, there is an unique maximizer ( xλ, yλ) of fλ. Since hλ is strongly convex, there is a unique minimizer ( θ1∗, θ2∗, θ3∗). By the deﬁnition of fλ and hλ, we have

hλ( θ1∗, θ2∗, θ3∗) ≥ gλ( xλ, yλ, θ1∗, θ2∗, θ3∗) ≥ fλ( xλ, yλ) .

Using (11.10), the equality above holds and hence ( θ1∗, θ2∗, θ3∗) is the minimizer of gλ( xλ, yλ, θ1, θ2, θ3) over ( θ1, θ2, θ3). Since the domain Ω is large enough that ( θ1∗, θ2∗, θ3∗) is an interior point in Ω, the optimality condition of gλ shows that we have θ2∗ =  xλ and θ3∗ =  yλ.

Since hλ is λ1 strongly convex, we have θ 1 − θ1∗ 22 + θ 2 − θ2∗ 22 + θ 3 − θ3∗ 22 ≤ 2λ  (Fact 37). Since θ2∗ =  xλ and θ3∗ =  yλ, we have

θ 2 −  xλ 22 + θ 3 −  yλ 22 ≤ 2λ . (11.11)

√

√

Therefore, we have  xλ −  yλ 2 ≥ θ 2 − θ 3 2 − 2

2λ  and  yλ 2 ≥ θ 3 2 −

2λ ,  xλ 2 ≥ θ 2 2 −

√

2λ . Using these,  xλ 2 ≤ M and  yλ 2 ≤ M, we have

1 2λ

1 2λ

- 1

- 2


λ 2

- 1

- 2


θ 2 − θ 3 22 −

θ 3 22 ≥

θ 2 22 −

 c, θ 3 −

 c, θ 2 +

fλ( θ 2, θ 3) =

√

1 2

1 2

 c, yλ − M

2λ  −

 c, xλ +

√

λ 2

2

 xλ −  yλ 2 + 2

2λ 

√

√

- 1

- 2λ


- 1

- 2λ


2

2

−

−

 xλ 2 +

2λ 

 yλ 2 +

2λ 

- 1

- 2


1 2

λ 2

- 1

- 2λ


- 1

- 2λ


 yλ 22 −M

 xλ −  yλ 22 −

 xλ 22 −

 c, yλ −

=

 c, xλ +

√

√

2λ   xλ −  yλ 2 − 4λ2 −

2λ  − 2λ

√

√

1 λ

1 λ

2λ  − −

2λ  −  .

 xλ 2

 yλ 2

Using  xλ −  yλ 2 ≤ 6Mλ 2 (Lemma 46),  xλ 2 < M and  yλ 2 < M, we have fλ( θ 2, θ 3) ≥ fλ( xλ, yλ) −M

√

√

2λ   xλ −  yλ 2 − 4λ2 −

2λ  − 2λ

√

√

1 λ

1 λ

2λ  −  . ≥ fλ( xλ, yλ)

2λ  − −

 xλ 2

 yλ 2

√

√

12 M − 4λ2 −2M 2

−M

2λ  − 2λ

λ − 2 . Since λ ≥ 2, we have

fλ( θ 2, θ 3) ≥ fλ( xλ, yλ) − 20Mλ√

− 10λ2 .

Let z  = θ 2+2 θ 3. Lemma 46 shows that

M2 λ ≤ fλ( θ 2, θ 3) +

 c, x ≤ max

max

fλ( x, y) +

 x∈K1∩K2

 x∈K1, y∈K2

M2 λ

+ 20Mλ√ + 10λ2

20M2 λ

+ 20λ3

≤  c,z  +

because 20Mλ√

≤ 10Mλ2 + 10λ3 . Furthermore, we have z  −  xλ 2 + z  −  yλ 2 ≤ θ 2 −  xλ 2 + θ 3 −  yλ 2 + θ 2 − θ 3 2 ≤ 4

√

6M2 λ

2λ  +

.

We now apply our cutting plane method to solve the optimization problem (11.1). First we

show how to transform the optimization oracles for K1 and K2 to get a separation oracle for hλ, with the appropriate parameters.

- Lemma 48. Suppose we have a -optimization oracle for K1 and K2 for some 0 < < 1. Then on the set { θ 2 ≤ D}, we have a (O(


√

√

 λD),O(

 λD))-separation oracle for hλ with time complexity

OO (K1) + OO (K2). Proof. Recall that the function hλ is deﬁned by

hλ( θ1, θ2, θ3)

= max

 x∈K1, y∈K2

 c 2

###### = max

 x∈K1

 c 2

+ λ θ1 +

θ2 λ

+ λ θ1 +

, x +

θ2 λ

, x + max

 y∈K2

 c 2 − λ θ1 +

θ3 λ

λ 2

, y +

θ1 22 +

 c 2 − λ θ1 +

θ3 λ

λ 2

, y +

1 2λ

θ1 22 +

- 1

- 2λ


- 1

- 2λ


θ2 22 +

θ3 22

1 2λ

θ2 22 +

θ3 22.

Lemma 40 shows how to compute the subgradient of functions of the form f( c) = max x∈K  c, x

using the optimization oracle for K. The rest of the term are diﬀerentiable so its subgradient is just the gradient. Hence, by addition rule for subgradients (Fact 37), we have a O( λ)-subgradient oracle for fλ using a O( )-optimization oracle for K1 and K2. The result then follows from Lemma 38.

| |
|---|


Theorem 49. Assume (11.2) and (11.3). Suppose that we have -optimization oracle for every

> 0. For 0 < δ < 1, we can ﬁnd z  ∈ Rn such that max

 c, x ≤ δ +  c,z 

 x∈K1∩K2

and z  −  x 2 + z  −  y 2 ≤ δ for some  x ∈ K1 and  y ∈ K2 in time

O n(OOη(K1) + OOη(K2))log

nM δ

+ n3 logO(1)

nM δ

where η = Ω nM δ O(1) .

Proof. Setting λ = 40δM2 2 and = 107δM7 6 in Lemma 47 we see that so long as we obtain any approximate solution ( θ 1, θ 2, θ 3) such that

hλ( θ 1, θ 2, θ 3) ≤ min

hλ( θ1, θ2, θ3) +  ,

( θ1, θ2, θ3)∈Ω

then we obtain the point we want. To apply Theorem 42, we use

h˜( θ1, θ2, θ3) =

hλ( θ1, θ2, θ3) if ( θ1, θ2, θ3) ∈ Ω

.

+∞ else

Lemma 48 shows that for any γ > 0 we can obtain a (γ,γ)-separation oracle of hλ( θ) by using suﬃciently accurate optimization oracles. Since Ω is just a product of 2 balls, we can produce a separating hyperplane easily when ( θ1, θ2, θ3) ∈/ Ω. Hence, we can obtain a (γ,γ)-separation oracle

of h˜( θ). For simplicity, we use θ to represent ( θ1, θ2, θ3). Note that B∞(2M) ⊇ Ω and therefore we can apply Theorem 42 with R = 2M to compute θ such

h˜( θ ) − min

h˜( θ) ≤ γ + α max

h˜( θ) − min

h˜( θ)

θ∈Ω

θ∈Ω

θ∈Ω

in time O nSOγ,γ log nκα + n3 logO(1) nκα where γ = Ω αMinWidth(Ω)/nO(1) = Ω αM/nO(1) and κ = MinWidth(Ω)2M = O(1). Using λ ≥ 1 and M ≥ 1, we have

M4 δ2

h˜( θ) − min

h˜( θ) ≤ O λM2 ≤ O

.

max

θ∈Ω

θ∈Ω

Setting α = Θ M δ910 with some small enough constant, we have that we can ﬁnd θ such that

M4 δ2

hλ( θ ) ≤ min θ∈P

hλ( θ) + γ + αO

δ7 M6

hλ( θ) + O

= min

θ∈P

= min

hλ( θ) +

θ∈P

in time O nSOγ,γ log nMδ + n3 logO(1) nMδ where γ = Ω nM δ O(1) . Lemma 48 shows that the cost of (γ,γ)-separation oracle is just O(OOη(K1) + OOη(K2)) where η = Ω nM δ O(1) .

| |
|---|


Remark 50. Note that the algorithm does not promise that we obtain a point close to K1 ∩ K2. It only promises to give a point that is close to both some point in K1 and some point in K2. It appears to the authors that a further assumption is needed to get a point close to K1 ∩ K2. For example, if K1 and K2 are two almost parallel lines, it would be diﬃcult to get an algorithm that does not depend on the angle. However, as far as we know, most algorithms tackling this problem are pseudo-polynomial and have polynomial dependence on the angle. Our algorithm depends on the logarithmic of the angle which is useful for combinatorial problems.

This reduction is very useful for problems in many areas including linear programming, semideﬁnite programming and algorithmic game theory. In the remainder of this section we demonstrate its power by applying it to classical combinatorial problems.

There is however one issue with applying our cutting plane algorithm to these problems. As with other convex optimization methods, only an approximately optimal solution is found. On the other hand, typically an exact solution is insisted in combinatorial optimization. To overcome this gap, we introduce the following lemma which (1) transforms the objective function so that there is only one optimal solution and (2) shows that an approximate solution is close to the optimal solution whenever it is unique. As we shall see in the next two subsections, this allows us to round an approximate solution to an optimal one.

Lemma 51. Given a linear program minA x≥ b cT x where  x, c ∈ Zn, b ∈ Zm and A ∈ Zm×n. Suppose {A x ≥ b} is an integral polytope (i.e. all extreme points are integral) contained in the

set {  x ∞ ≤ M}. Then we can ﬁnd a random cost vector z  ∈ Zn with z  ∞ ≤ O(n2M2  c ∞) such that with constant probability, minA x≥ b z T x has an unique minimizer  x∗ and this minimizer is one of the minimizer(s) of minA x≥ b cT x. Furthermore, if there is an interior point  y such that z T y < minA x≥ b z T x + δ, then  y −  x∗ ∞ ≤ 2nMδ.

Proof. The ﬁrst part of the lemma follows by randomly perturbing the cost vector  c. We consider a new cost vector z  = 100n2M2 c +  r where each coordinate of  r is sampled randomly from {0,1,··· ,10nM}. [67, Lem 4] shows that the linear program minA x≥ b z T x has a unique minimizer with constant probability. Furthermore, it is clear that the minimizer of minA x≥ b z T x is a minimizer of minA x≥ b cT x (as  ri 100n2M2| ci|).

Now we show the second part of the lemma. Given an interior point  y of the polytope {A x ≥ b}, we can write  y as a convex combination of the vertices of {A x ≥ b}, i.e.  y = ti vi. Note that z T y = tiz T vi. If all  vi are not the minimizer, then z T vi ≥ OPT + 1 and hence z T y ≥ OPT + 1 which is impossible. Hence, we can assume that  v1 is the minimizer. Hence, z T vi = OPT if i = 1 and z T vi ≥ OPT+1 otherwise. We then have z T y ≥ OPT+(1−t1) which gives 1−t1 < δ. Finally, the claim follows from  y −  v1 ∞ ≤ i =1 ti  vi −  v1 ∞ ≤ 2nMδ.

| |
|---|


###### 11.2 Matroid Intersection

Let M1 = (E,I1) and M2 = (E,I2) be two matroids sharing the same ground set. In this section we consider the weighted matroid intersection problem

min

w (S).

S∈I1∩I2

where w  ∈ RE and w(S) def= e∈S we.

For any matroid M = (E,I), it is well known that the polytope of all independent sets has the following description [28]:

conv(I1) = { x ∈ RE s.t. 0 ≤ x(S) ≤ r(S) for all S ⊆ E} (11.12)

where r is the rank function for M, i.e. r(S) is the size of the largest independent set that is a subset of S. Furthermore, the polytope of the matroid intersection satisﬁes conv(I1 ∩ I2) = conv(I1) ∩ conv(I2).

It is well known that the optimization problem min

w(S) and min

w(S)

S∈I1

S∈I2

can be solved eﬃciently by the greedy method. Given a matroid (polytope), the greedy method ﬁnds a maximum weight independent subset by maintaining a candidate independent subset S and iteratively attempts to add new element to S in descending weight. A element i is added to S if S ∪ {i} is still independent. A proof of this algorithm is well-known and can be found in any standard textbook on combinatorial optimization.

Clearly, the greedy method can be implemented by O(n) calls to the independence oracle (also called membership oracle). For rank oracle, it requires O(r log n) calls by ﬁnding the next element to add via binary search. Therefore, we can apply Theorem 49 to get the following result (note that this algorithm is the fastest if r is close to n for the independence oracle).

Theorem 52. Suppose that the weights w  are integer with w ∞ ≤ M. Then, we can ﬁnd

S ∈ arg min

w(S)

S∈I1∩I2

in time O nGOlog (nM) + n3 logO(1) (nM) where GO is the cost of greedy method for I1 and I2.

Proof. Applying Lemma 51, we can ﬁnd a new cost z  such that min

z T x

 x∈conv(I1)∩conv(I2)

has an unique solution. Note that for any  x ∈ conv(I1), we have  x ∞ ≤ 1. Hence, applying theorem 49, we can ﬁnd q  such that q Tz  ≤ OPT + and q  −  x 2 + q  −  y 2 ≤ for some  x ∈ conv(I1) and  y ∈ conv(I2). Using (11.12), we have the coordinate wise minimum of  x, y, i.e. min{ x, y}, is in conv(I1) ∩ conv(I2). Since q  − min{ x, y} 2 ≤ q  −  x 2 + q  −  y 2 ≤ , we have

(min{ x, y})T z  ≤ OPT + nM . Hence, we have a feasible point min{ x, y} which has value close to optimal and Lemma 51 shows that

min( x, y)− s ∞ ≤ 2n2M2 where  s is the optimal solution. Hence, we have q − s ∞ ≤ 2n2M2 + .

Picking = 6n21M2, we have q  − s ∞ < 21 and hence, we can get the optimal solution by rounding to the nearest integer.

Since optimization over I1 and I2 involves applying greedy method on certain vectors, it takes only O(GO) time. Theorem 49 shows it only takes O nGOlog (nM) + n3 logO(1) (nM) in ﬁnding such q .

| |
|---|


This gives the following corollary.

Corollary 53. We have O(n2Tind log(nM)+n3 logO(1) nM) and O(nrTrank log nlog(nM)+n3 logO(1) nM) time algorithms for weighted matroid intersection. Here Tind is the time needed to check if a subset is independent, and Trank is the time needed to compute the rank of a given subset.

Proof. By Theorem 52, it suﬃces to show that the optimization oracle for the matroid polytope can be implemented in O(nTind) and O(rTrank log n) time. This is simply attained by the well-known greedy algorithm which iterates through all the positively-weighted elements in decreasing order, and adds an element to our candidate independent set whenever possible.

For the independence oracle, this involves one oracle call for each element. On the other hand, for the rank oracle, we can ﬁnd the next element to add by binary search which takes time O(Trank log n). Since there are at most r elements to add, we have the desired running time.

| |
|---|


###### 11.3 Submodular Flow

Let G = (V,E) be a directed graphwith |E| = m, let f be a submodular function on RV with |V | = n, f(∅) = 0 and f(V ) = 0, and let A be the incidence matrix of G. In this section we consider the submodular ﬂow problem

Minimize c,ϕ (11.13) subject to l(e) ≤ ϕ(e) ≤ u(e) ∀e ∈ E

x(v) = (Aϕ)(v) ∀v ∈ V

x(v) ≤ f(S) ∀S ⊆ V

v∈S

where c ∈ ZE, l ∈ ZE, u ∈ ZE where C =  c ∞ and U = max u ∞, l ∞,maxS⊂V |f(S)| . Here c is the cost on edges, ϕ is the ﬂow on edges, l and u are lower and upper bounds on the amount

of ﬂow on the edges, and x(v) is the net ﬂow out of vertex v. The submodular function f upper bounds the total net ﬂow out of any subset S of vertices by f(S).

Theorem 54. Suppose that the cost vector  c is integer weight with  c ∞ ≤ C and the capacity vector and the submodular function satisfy U = max u ∞, l ∞,maxS⊂V |f(S)| . Then, we can solve the submodular ﬂow problem (11.13) in time O n2EOlog(mCU) + n3 logO(1)(mCU) where EO is the cost of function evaluation.

Proof. First, we can assume l(e) ≤ u(e) for every edge e, otherwise, the problem is infeasible. Now, we apply a similar transformation in [49] to modify the graph. We create a new vertex v0. For every vertex v in V , we create a edge from v0 to v with capacity lower bounded by 0, upper bounded by 4nU, and with cost 2mCU. Edmonds and Giles showed that the submodular ﬂow polytope is integral [29]. Hence, there is an integral optimal ﬂow on this new graph. If the optimal ﬂow passes through the newly created edge, then it has cost at least 2mCU − mCU because the cost of all other edges in total has at least −mCU. That means the optimal ﬂow has the cost larger than mCU which is impossible. So the optimal ﬂow does not use the newly created edges and vertex and hence the optimal ﬂow in the new problem gives the optimal solution of the original problem. Next, we note that for any ϕ on the original graph such that l(e) ≤ ϕ(e) ≤ u(e), we can send suitable amount of ﬂow from v0 to v to make ϕ feasible. Hence, this modiﬁcation makes the feasibility problem trivial.

Lemma 51 shows that we can assume the new problem has an unique solution and it only blows up C by a (mU)O(1) factors.

Note that the optimal value is an integer and its absolute value at most mCU. By binary search, we can assume we know the optimal value OPT. Now, we reduce the problem to ﬁnding a feasible ϕ with { d,ϕ ≤ OPT + } with determined later. Let P be the set of such ϕ. Note that P = K1,  ∩ K2,  where

- K1,  =

 



x ∈ RV such that

l(e) ≤ ϕ(e) ≤ u(e) ∀e ∈ E x(v) = (Aϕ)(v) ∀v ∈ V d,ϕ ≤ OPT +

for some ϕ

 



,

- K2,  = y ∈ RV such that v∈S


y(v) ≤ f(S) ∀S ⊆ V,

y(v) = f(V ) .

v∈V

Note that the extra condition v y(v) = f(V ) is valid because v y(v) = v(Aϕ)(v) = 0 and f(V ) = 0, and K1,  has radius bounded by O((mCU)O(1)) and K2,  has radius bounded by O(nU). Furthermore, for any vector  c ∈ RV , we note that

max

c,x = max

c,x

x∈K1, 

l≤ϕ≤u, d,ϕ ≤OPT+ ,x=Aϕ

= max

c,Aϕ

l≤ϕ≤u, d,ϕ ≤OPT+

ATc,ϕ .

= max

l≤ϕ≤u, d,ϕ ≤OPT+

To solve this problem, again we can do a binary search on d,ϕ and reduce the problem to max

ATc,ϕ

l≤ϕ≤u, d,ϕ =K

for some value of K. Since ATc is ﬁxed, this is a linear program with only the box constraints and an extra equality constraint. Hence, it can be solved in nearly linear time [76, Thm 17, ArXiv v1]. As the optimization oracle for K1,  involves only computing ATc and solving this simple linear program, it takes only O(n2 logO(1)(mCU/ )) time. On the other hand, since K2,  is just a base

polyhedron, the optimization oracle for K2,  can be done by greedy method and only takes O(nEO) time.

Applying Theorem 49, we can ﬁnd q such that q − x 2 + q − y 2 ≤ δ for some x ∈ K1, , y ∈ K2,  and δ to be chosen later. According to the deﬁnition of K1, , there is ϕ such that l(e) ≤ ϕ(e) ≤ u(e) and x(v) = (Aϕ)(v) for all v and d,ϕ ≤ OPT + . Since y − x 2 ≤ 2δ, that means |y(v) − (Aϕ)(v)| ≤ 2δ for all v.

- • Case 1) If y(v) ≥ (Aϕ)(v), then we can replace y(v) by (Aϕ)(v), note that y is still in K2,  because of the submodular constraints.
- • Case 2) If y(v) ≤ (Aϕ)(v), then we can send a suitable amount of ﬂow from v0 to v to make ϕ feasible y(v) ≤ (Aϕ)(v).


Note that under this modiﬁcation, we increased the objective value by (δn)(2mCU) because the new edge cost 2mCU per unit of ﬂow. Hence, we ﬁnd a ﬂow ϕ which is feasible in new graph with objective value +(δn)(2mCU) far from optimum value. By picking δ = 2mnCU1 , we have the value 2 far from OPT. Now, we use Lemma 51 to shows that when is small enough, i.e, (mCU1 )c for some constant c, then we can guarantee that y − x∗ ∞ ≤ 14 where x∗ is the optimal demand. Now, we note that q − y 2 ≤ δ and we note that we only modify y by a small amount, we in fact have q − x∗ ∞ < 21. Hence, we can read oﬀ the solution x∗ by rounding q to the nearest integer. Note that we only need to solve the problem K1, ∩K2,  to (mCU1)Θ(1) accuracy and the optimization oracle for K1,  and K2,  takes time O(n2 logO(1)(mCU)) and O(nEO) respectively. Hence, Theorem

- 49 shows that it takes O n2EOlog(mCU) + n3 logO(1)(mCU) time to ﬁnd x∗ exactly. After getting x∗, one can ﬁnd ϕ∗ by solving a min cost ﬂow problem using interior point method


[74], which takes O(m√nlogO(1)(mCU)) time.

| |
|---|


###### 11.4 Aﬃne Subspace of Convex Set

In this section, we give another example about using optimization oracle directly via regularization. We consider the following optimization problem

max

 x∈K and A x= b

 c, x (11.14)

where  x, c ∈ Rn, K is a convex subset of Rn, A ∈ Rr×n and b ∈ Rm. We suppose that r n and thus, the goal of this subsection is to show how to obtain an algorithm takes only O˜(r) many iterations. To do this, we assume a slightly stronger optimization oracle for K:

Deﬁnition 55. Given a convex set K and δ > 0. A δ-2nd-order-optimization oracle for K is a function on Rn such that for any input  c ∈ Rn and λ > 0, it outputs  y such that

 c, x − λ  x 2 ≤ δ +  c, y − λ  y 2.

max

 x∈K

We denote by OO(2)δ,λ(K) the time complexity of this oracle.

The strategy for solving this problem is very similar to the intersection problem and hence some details are omitted.

Theorem 56. Assume that max x∈K  x 2 < M, b 2 < M,  c 2 < M, A 2 < M and λmin(A) > 1/M. Assume that K ∩{A x = b} = ∅ and we have -2nd-order-optimization oracle for every > 0. For 0 < δ < 1, we can ﬁnd z  ∈ K such that

 c, x ≤ δ +  c,z 

max

 x∈K and A x= b

and Az  − b 2 ≤ δ. This algorithm takes time

nM δ

O rOO(2)η,λ(K)log

+ r3 logO(1)

nM δ

where r is the number of rows in A, η = nM δ Θ(1) and λ = nM δ Θ(1). Proof. The proof is based on the minimax problem

OPTλ def= min

max

 x∈K

 η 2≤λ

1 λ

 c, x +  η,A x − b −

where λ = nM δ c for some large constant c. We note that

 x 22

1 λ

 x 22

 c, x +  η,A x − b −

OPTλ = max  x∈K

min

 η 2≤λ

1 λ

 x 22.

 c, x − λ A x − b 2 −

###### = max

 x∈K

Since λmin(A) > 1/M and the set K is bounded by M, one can show that the saddle point ( x∗, η∗) of the minimax problem gives a good enough solution  x for the original problem for large enough constant c.

For any  η, we deﬁne

1 λ

 x 22. Since the problem is strongly concave in  x, one can prove that

 c, x +  η,A x − b −

 x η = arg max

 x∈K

 x η −  x∗ 2 ≤

nM δ

O(c)

 η −  η∗ 2.

Hence, we can ﬁrst ﬁnd an approximate minimizer of the function f( η) = max x∈K  c, x +  η,A x − b − 1 λ  x 22 and use the oracle to ﬁnd  x η.

To ﬁnd an approximate minimizer of f, we note that the subgradient of f can be found using the optimization oracle similar to Theorem 49. Hence, the result follows from our cutting plane method and the fact that  η ∈ Rr.

| |
|---|


Remark 57. In [74], they considered the special case K = { x : 0 ≤ xi ≤ 1} and showed that it can be solved in O˜(√r) iterations using interior point methods. This gives the current fastest algorithm for the maximum ﬂow problem on directed weighted graphs. Our result generalizes their result to any convex set K but with O˜(r) iterations. This suggests the following open problem: under what condition on K can one optimize linear functions over aﬃne subspaces of K with r constraints in O˜(√r) iterations?

Part III

# Submodular Function Minimization

#### 12 Introduction

Submodular functions and submodular function minimization (SFM) are fundamental to the ﬁeld of combinatorial optimization. Examples of submodular functions include graph cut functions, set coverage function, and utility functions from economics. Since the seminal work by Edmonds in 1970 [27], submodular functions and the problem of minimizing such functions (i.e. submodular function minimization) have served as a popular modeling and optimization tool in various ﬁelds such as theoretical computer science, operations research, game theory, and most recently, machine learning. Given its prevalence, fast algorithms for SFM are of immense interest both in theory and in practice.

Throughout Part III, we consider the standard formulation of SFM: we are given a submodular function f deﬁned over the subsets of a n-element ground set. The values of f are integers, have absolute value at most M, and are evaluated by querying an oracle that takes time EO. Our goal is to produce an algorithm that solves this SFM problem, i.e. ﬁnds a minimizer of f, while minimizing both the number of oracle calls made and the total running time.

We provide new O(n2 log nM · EO + n3 logO(1) nM) and O(n3 log2 n · EO + n4 logO(1) n) time algorithms for SFM. These algorithms improve upon the previous fastest weakly and strongly polynomial time algorithms for SFM which had a a running time of O((n4 · EO + n5)log M) [54] and O(n5 ·EO+n6) [90] respectively. Consequently, we improve the running times in both regimes by roughly a factor of O(n2).

Both of our algorithms bear resemblance to the classic approach of Gr¨tschel, Lov´sz and Schrijver [49, 50] using the Lov´sz extension. In fact our weakly polynomial time algorithm directly uses the Lov´asz extension as well as the results of Part II to achieve these results. Our strongly polynomial time algorithm also uses the Lov´sz extension, along with more modern tools from the past 15 years.

At a high level, our strongly polynomial algorithms apply our cutting plane method in conjunction with techniques originally developed by Iwata, Fleischer, and Fujishige (IFF) [56]. Our cutting plane method is performed for enough iterations to sandwich the feasible region in a narrow strip from which useful structural information about the minimizers can be deduced. Our ability to derive the new information hinges on a signiﬁcant extension of IFF techniques.

Over the past few decades, SFM has drawn considerable attention from various research communities, most recently in machine learning [11, 68]. Given this abundant interest in SFM, we hope that our ideas will be of value in various practical applications. Indeed, one of the critiques against existing theoretical algorithms is that their running time is too slow to be practical. Our contribution, on the contrary, shows that this school of algorithms can actually be made fast theoretically and we hope it may potentially be competitive against heuristics which are more commonly used.

###### 12.1 Previous Work

Here we provide a brief survey of the history of algorithms for SFM. For a more comprehensive account of the rich history of SFM, we refer the readers to recent surveys [81, 55].

The ﬁrst weakly and strongly polynomial time algorithms for SFM were based on the ellipsoid method [65] and were established in the foundational work of Gr¨tschel, Lov´sz and Schrijver in 1980’s [49, 50]. Their work was complemented by a landmark paper by Cunningham in 1985 which provided a pseudopolynomial algorithm that followed a ﬂow-style algorithmic framework [20]. His tools foreshadowed much of the development in SFM that would take place 15 years later. Indeed, modern algorithms synthesize his framework with inspirations from various max ﬂow algorithms.

The ﬁrst such “ﬂow style” strongly polynomial algorithms for SFM were discovered independently in the breakthrough papers by Schrijver [93] and Iwata, Fleischer, and Fujishige (IFF) [56]. Schrijver’s algorithm has a running of O(n8 · EO + n9) and borrows ideas from the push-relabel algorithms [46, 25] for the maximum ﬂow problem. On the other hand, IFF’s algorithm runs in time O(n7 log n·EO) and O(n5·EOlog M), and applies a ﬂow-scaling scheme with the aid of certain proximity-type lemmas as in the work of Tardos [100]. Their method has roots in ﬂow algorithms such as [52, 47].

Subsequent work on SFM provided algorithms with considerably faster running time by extending the ideas in these two “genesis” papers [93, 56] in various novel directions [107, 31, 54, 90, 60]. Currently, the fastest weakly and strongly polynomial time algorithms for SFM have a running time of O((n4 · EO + n5)log M) [54] and O(n5 · EO + n6) [90] respectively. Despite this impressive track record, the running time has not been improved in the last eight years.

We remark that all of the previous algorithms for SFM proceed by maintaining a convex combination of O(n) BFS’s of the base polyhedron, and incrementally improving it in a relatively local manner. As we shall discuss in Section 12.2, our algorithms do not explicitly maintain a convex combination. This may be one of the fundamental reasons why our algorithms achieve a faster running time.

Finally, beyond the distinction between weakly and strongly polynomial time algorithms for SFM, there has been interest in another type of SFM algorithm, known as fully combinatorial algorithms in which only additions and subtractions are permitted. Previous such algorithms include [60, 54, 53]. We do not consider such algorithms in the remainder of the paper and leave it as an open question if it is possible to turn our algorithms into fully combinatorial ones.

###### 12.2 Our Results and Techniques

In Part III we show how to improve upon the previous best known running times for SFM by a factor of O(n2) in both the strongly and weakly polynomial regimes. In Table 11 summarizes the running time of the previous algorithms as well as the running times of the fastest algorithms presented in this paper.

Both our weakly and strongly polynomial algorithms for SFM utilize a convex relaxation of the submodular function, called the Lov´asz extension. Our algorithms apply our cutting plane method from Part I using a separation oracle given by the subgradient of the Lov´asz extension. To the best of the author’s knowledge, Gr¨tschel, Lov´sz and Schrijver were the ﬁrst to formulate this convex optimization framework for SFM [49, 50].

For weakly polynomial algorithms, our contribution is two-fold. First, we show that cutting plane methods such as Vaidya’s [105] can be applied to SFM to yield faster algorithms. Second, as our cutting plane method, Theorem 42, improves upon previous cutting plane algorithms and consequently the running time for SFM as well. This gives a running time of O(n2 log nM · EO +

|Authors<br><br>|Years|Running times|Remarks|
|---|---|---|---|


|Gr¨tschel, Lov´sz, Schrijver [49, 50]<br><br>|1981,1988<br><br>|O(n5 · EO + n7)[81]|ﬁrst weakly and strongly|
|---|---|---|---|
|Cunningham [20]<br><br>|1985<br><br>|O(Mn6 log nM · EO)<br><br>|ﬁrst pseudopoly|
|Schrijver [93]<br><br>|2000|O(n8 · EO + n9)|ﬁrst combin. strongly|
|Iwata, Fleischer, Fujishige[56]<br><br>|2000<br><br>|O(n5 · EOlog M) O(n7 log n · EO)|ﬁrst combin. strongly|
|Iwata, Fleischer [31]|2000|O(n7 · EO + n8)| |
|Iwata [54]<br><br>|2003|O((n4 · EO + n5)log M) O((n6 · EO + n7)log n)<br><br>|current best weakly|
|Vygen [107]<br><br>|2003|O(n7 · EO + n8)| |
|Orlin [90]|2007<br><br>|O(n5 · EO + n6)|current best strongly|
|Iwata, Orlin [60]|2009|O((n4 · EO + n5)log nM)<br>O((n5 · EO + n6)log n)<br>| |
|Our algorithms|2015|O(n2 log nM · EO + n3 logO(1) nM)<br>O(n3 log2 n · EO + n4 logO(1) n)<br>| |


Table 11: Algorithms for submodular function minimization. Note that some of these algorithms were published in both conferences and journals, in which case the year we provided is the earlier one.

n3 logO(1) nM), an improvement over the previous best algorithm by Iwata [54] by a factor of almost O(n2).

Our strongly polynomial algorithms, on the other hand, require substantially more innovation. We ﬁrst begin with a very simple geometric argument that SFM can be solved in O(n3 log n · EO) oracle calls (but in exponential time). This proof only uses Grunbaum’s Theorem from convex geometry and is completely independent from the rest of the paper. It was the starting point of our method and suggests that a running time of O(n3 · EO + nO(1)) for submodular minimization is in principle achievable.

To make this existence result algorithmic, we ﬁrst run cutting plane, Theorem 31, for enough iterations such that we compute either a minimizer or a set P containing the minimizers that ﬁts within in a narrow strip. This narrow strip consists of the intersection of two approximately parallel hyperplanes. If our narrow strip separates P from one of the faces xi = 0, xi = 1, we can eﬀectively eliminate the element i from our consideration and reduce the dimension of our problem by 1. Otherwise a pair of elements p,q can be identiﬁed for which q is guaranteed to be in any minimizer containing p (but p may not be contained in a minimizer). Our ﬁrst algorithm deduces only one such pair at a time. This technique immediately suﬃces to achieve a O(n4 ·EO+n5) time algorithm for SFM (See Section 15.3). We then improve the running time to O(n3 · EO + n4) by showing how to deduce many such pairs simultaneously. Similar to past algorithms, this structural information is deduced from a point in the so-called base polyhedron (See Section 13).

Readers well-versed in SFM literature may recognize that our strongly polynomial algorithms are reminiscent of the scaling-based approach ﬁrst used by IFF [56] and later in [54, 60]. While both approaches share the same skeleton, there are diﬀerences as to how structural information about minimizers is deduced. A comparison of our algorithms and previous ones are presented in Section 16.

Finally, there is one more crucial diﬀerence between these algorithms which we believe is responsible for much of our speedup. One common feature shared by all the previous algorithms is

that they maintain a convex combination of O(n) BFS’s of the base polyhedron, and incrementally improve on it by introducing new BFS’s by making local changes to existing ones. Our algorithms, on the other hand, choose new BFS’s by the cutting plane method. Because of this, our algorithm considers the geometry of the existing BFS’s where each of them has inﬂuences over the choice of the next BFS. In some sense, our next BFS is chosen in a more “global” manner.

###### 12.3 Organization

The rest of Part III is organized as follows. We ﬁrst begin with a gentle introduction to submodular functions in Section 13. In Section 14, we apply our cutting plane method to SFM to obtain a faster weakly polynomial algorithms. In Section 15 we then present our results for achieving better strongly polynomial algorithms, where a warm-up O(n4 · EO + n5) algorithm is given before the full-ﬂedged O(n3 · EO + n4) algorithm. Finally, we end the part with a discussion and comparison between our algorithms and previous ones in Section 16.

We note that there are a few results in Part III that can be read fairly independently of the rest of the paper. In Theorem 67 we show how Vaidya’s algorithm can be applied to SFM to obtain a faster weakly polynomial running time. Also in Theorem 71 we present a simple geometric argument that SFM can be solved with O(n3 log n · EO) oracle calls but with exponential time. These results can be read with only a working knowledge of the Lov´sz extension of submodular functions.

#### 13 Preliminaries

Here we introduce background on submodular function minimization (SFM) and notation that we use throughout Part III. Our exposition is kept to a minimal amount suﬃcient for our purposes. We refer interested readers to the extensive survey by McCormick [81] for further intuition.

###### 13.1 Submodular Function Minimization

Throughout the rest of the paper, let V = {1,...,n} = [n] denote a ground set and let f : 2V −→ Z denote a submodular function deﬁned on subsets of this ground set. We use V and [n] interchangeably and let [0] def= ∅. We abuse notation by letting S + i def= S ∪ {i} and S − i def= S\{i} for an element i ∈ V and a set S ⊆ 2V . Formally, we call a function submodular if it obeys the following property of diminishing marginal diﬀerences:

Deﬁnition 58 (Submodularity). A function f : 2V −→ Z is submodular if f(T + i) − f(T) ≤ f(S + i) − f(S) for any S ⊆ T and i ∈ V \T.

For convenience we assume without loss of generality that f(∅) = 0 by replacing f(S) by f(S) − f(∅) for all S. We also let M def= maxS∈2V |f(S)|.

The central goal of Part III is to design algorithms for SFM, i.e. computing the minimizer of f. We call such an algorithm strongly polynomial if its running time depends only polynomially on n and EO, the time needed to compute f(S) for a set S, and we call such an algorithm weakly polynomial if it also depends polylogarithmically on M.

###### 13.2 Lova´sz Extension

Our new algorithms for SFM all consider a convex relaxation of a submodular function, known as the Lov´sz extension, and then carefully apply our cutting plane methods to it. Here we formally introduce the Lov´sz extension and present basic facts that we use throughout Part III.

The Lov´sz extension of fˆ: [0,1]n −→ R of our submodular function f is deﬁned for all  x by

fˆ( x) def= Et∼[0,1][f({i : xi ≥ t})],

where t ∼ [0,1] is drawn uniformly at random from [0,1]. The Lov´sz extension allows us to reduce SFM to minimizing a convex function deﬁned over the interior of the hypercube. Below we state that the Lov´sz extension is a convex relaxation of f and that it can be evaluated eﬃciently.

Theorem 59. The Lov´asz extension fˆ satisﬁes the following properties:

- 1. fˆ is convex and min x∈[0,1]n fˆ( x) = minS⊂[n] f(S);
- 2. f(S) = fˆ(IS), where IS is the characteristic vector for S, i.e. IS(i) =

1 if i ∈ S 0 if i ∈/ S

;

- 3. If S is a minimizer of f, then IS is a minimizer of fˆ;
- 4. Suppose x1 ≥ ··· ≥ xn ≥ xn+1 def= 0, then


n

n

fˆ( x) =

f([i])(xi − xi+1) =

(f([i]) − f([i − 1]))xi .

i=1

i=1

Proof. See [50] or any standard textbook on combinatorial optimization, e.g. [94].

| |
|---|


Next we show that we can eﬃciently compute a subgradient of the Lov´sz or alternatively, a separating hyperplane for the set of minimizers of our submdoular function f. First we remind the reader of the deﬁnition of a separation oracle, and then we prove the necessary properties of the hyperplane, Theorem 61.

Deﬁnition 60 (separation oracle, Deﬁntion 1 restated for Lov´sz extension). Given a point x¯ and a convex function fˆ over a convex set P,  aT x ≤ b is a separating hyperplane if  aTx¯ ≥ b and any minimizer x∗ of fˆ over P satisﬁes  aTx∗ ≤ b.

- Theorem 61. Given a point x¯ ∈ [0,1]n assume without loss of generality (by re-indexing the coordinates) that x¯1 ≥ ··· ≥ x¯n. Then the following inequality is a valid separating hyperplane for


-  x and f: n


(f([i]) − f([i − 1]))xi ≤ fˆ(¯x)

i=1

i.e., it satisﬁes the following:

- 1. (separating) x¯ lies on ni=1(f([i]) − f([i − 1]))xi ≤ fˆ(¯x).
- 2. (valid) For any  x, we have ni=1(f([i]) − f([i − 1]))xi ≤ fˆ( x). In particular, ni=1(f([i]) −


f([i − 1]))x∗i ≤ fˆ(¯x) for any minimizer  x∗, i.e. the separating hyperplane does not cut out any minimizer.

Moreover, such a hyperplane can be computed with n oracle calls to f and in time O(n · EO + n2).

Proof. Note that by Theorem 59 we have that i∈[n](f([i]) − f([i − 1]))xi = fˆ(¯x) and thus the hyperplane satisﬁes the separating condition. Moreover, clearly computing it only takes time O(n·

EO + n2) as we simply need to sort the coordinates and evaluate f at n points, i.e. each of the [i]. All that remains is to show that the hyperplane satisﬁes the valid condition.

Let L(t) def= {i : xi ≥ t}. Recall that fˆ( x) = Et∼[0,1][f(Lt)]. Thus fˆ( x) can be written as a

convex combination fˆ( x) = t αtf(L(t)), where αt ≥ 0 and t αt = 1. However, by diminishing marginal diﬀerences we see that for all t

(f([i]) − f([i − 1]))(IL(t))i =

(f([i]) − f([i − 1]))

i∈[n]

i∈L(t)

f([i] ∩ L(t)) − f([i − 1] ∩ L(t))

≤

i∈L(t)

= f(L(t)) − f(∅) = f(L(t)) and therefore since t αtIL(t) =  x we have

(f[i] − f([i − 1])xi =

i∈[n]

t

n

(f([i]) − f([i − 1]))(IL(t))i ≤

αt

i=1

t

αtf(L(t)) = fˆ( x).

| |
|---|


###### 13.3 Polyhedral Aspects of SFM

Here we provide a natural primal dual view of SFM that we use throughout the analysis. We provide a dual convex optimization program to minimizing the Lov´sz extension and provide several properties of these programs. We believe the material in this section helps crystallize some of the intuition behind our algorithm and we make heavy use of the notation presented in this section. However, we will not need to appeal to the strong duality of these programs in our proofs.

Consider the following primal and dual programs, where we use the shorthands y(S) = i∈S yi

and yi− = min{0,yi}. Here the primal constraints are often called the base polyhedron B(f) def= { y ∈ Rn : y(S) ≤ f(S)∀S  ⊆ V,y(V ) = f(V )} and the dual program directly corresponds to minimizing

the Lov´asz extension and thus f.

|Primal|Dual|
|---|---|


|maxy−(V ) y(S) ≤ f(S)∀S  ⊆ V y(V ) = f(V )|minfˆ( x) 0 ≤  x ≤ 1|
|---|---|


- Theorem 62. h is a basic feasible solution (BFS) of the base polyhedron B(f) if and only if hi = f({v1,...,vi}) − f({v1,...,vi−1})


for some permutation v1,...,vn of the ground set V . We call v1,...,vn the deﬁning permutation of

- h. We call vi precedes vj for i < j.


This theorem gives a nice characterization of the BFS’s of B(f). It also gives the key observation underpinning our approach: the coeﬃcients of each separating hyperplane in Theorem 61 precisely corresponds to a primal BFS (Theorem 62). Our analysis relies heavily on this connection. We re-state Theorem 61 in the language of BFS.

Lemma 63. We have hT x ≤ fˆ( x) for any  x ∈ [0,1]n and BFS h. Proof. Any BFS is given by some permutation. Thus this is just Theorem 61 in disguise.

| |
|---|


We also note that since the objective function of the primal program is non-linear, we cannot say that the optimal solution to the primal program is a BFS. Instead we only know that it is a convex combination of the BFS’s that satisfy the following property. A proof can be found in any standard textbook on combinatorial optimization.

Theorem 64. The above primal and dual programs have no duality gap. Moreover, there always exists a primal optimal solution  y = k λ(k) h(k) with k λ(k) = 1 (a convex combination of BFS h(k)) s.t. any i with yi < 0 precedes any j with yj > 0 in the deﬁning permutation for each BFS h(k).

Our algorithms will maintain collections of BFS and use properties of h ∈ B(f), i.e. convex combination of BFS. To simplify our analysis at several points we will want to assume that such a vector h ∈ B(f) is non-degenerate, meaning it has both positive and negative entries. Below, we prove that such degenerate points in the base polytope immediately allow us to trivially solve the SFM problem.

Lemma 65 (Degenerate Hyperplanes). If h ∈ B(f) is non-negative then ∅ is a minimizer of f and if h is non-positive then V is a minimizer of f. Proof. While this follows immediately from Theorem 64, for completeness we prove this directly. Let S ∈ 2V be arbitrary. If h ∈ B(f) is non-negative then by the we have

f(S) ≥ h(S) =

hi ≥ 0 = f(∅).

i∈S

On the other hand if h is non-positive then by deﬁnition we have f(S) ≥ h(S) =

hi ≥

hi = h(V ) = f(V ).

i∈S

i∈V

| |
|---|


#### 14 Improved Weakly Polynomial Algorithms for SFM

- In this section we show how our cutting plane method can be used to obtain a O(n2 log nM · EO + n3 logO(1) nM) time algorithm for SFM. Our main result in this section is the following theorem, which shows how directly applying our results from earlier parts to minimize the Lov´sz extension yields the desired running time.


- Theorem 66. We have an O(n2 log nM · EO + n3 logO(1) nM) time algorithm for submodular function minimization.


Proof. We apply Theorem 42 to the Lov´sz extension fˆ : [0,1]n −→ R with the separation oracle given by Theorem 61. fˆfulﬁlls the requirement on the domain as its domain Ω = [0,1]n is symmetric about the point (1/2,...,1/2) and has exactly 2n constraints.

In the language of Theorem 42, our separation oracle is a (0,0)-separation oracle with η = 0 and δ = 0.

###### We ﬁrst show that δ = 0. Firstly, our separating hyperplane can be written as

n

(f([i]) − f([i − 1]))xi ≤ fˆ(¯x) =

i=1

n

(f([i]) − f([i − 1]))¯xi,

i=1

where the equality follows from Theorem 59. Secondly, for any  x with fˆ( x) ≤ fˆ(¯x) we have by Theorem 61 that n

(f([i]) − f([i − 1]))xi ≤ fˆ( x) ≤ fˆ(¯x)

i=1

which implies that  x is not cut away by the hyperplane.

Next we show that η = 0. Our separating hyperplane induces a valid halfspace whenever it is not nonzero, i.e. f([i]) = f([i − 1]) for some i. In the case that it is zero f([i]) = f([i − 1])∀i, by the same argument above, we have fˆ(¯x) = ni=1(f([i]) − f([i − 1]))¯xi = 0 and

n

fˆ( x) ≥

(f([i]) − f([i − 1]))xi = 0 = fˆ(¯x).

i=1

In other words, x¯ is an exact minimizer, i.e. η = 0. Note that f ˆ( x) = Et∼[0,1][f({i : xi ≥ t})] ≤ M as M = maxS |f(S)|. Now plugging in α = 4M1

in the guarantee of Theorem 31, we can ﬁnd a point x∗ such that

1 4M

fˆ(x∗) − min

fˆ( x) ≤

fˆ( x) − min

fˆ( x)

max

 x∈[0,1]n

 x∈[0,1]n

 x∈[0,1]n

1 4M

≤

(2M) < 1

We claim that mint∈[0,1] f({i : x∗i ≥ t}) is minimum. To see this, recall from 59 that fˆ has an integer minimizer and hence min x∈[0,1]n fˆ( x) = minS f(S). Moreover, fˆ(x∗) is a convex combination of f({i : x∗i ≥ t}) which gives

fˆ( x) = fˆ(x∗) − min

1 > fˆ(x∗) − min

f({i : x∗i ≥ t}) − min

f(S) ≥ min

f(S).

 x∈[0,1]n

S

S

t∈[0,1]

Since f is integer-valued, we must then have mint∈[0,1] f({i : x∗i ≥ t}) = minS f(S) as desired. Since our separation oracle can be computed by n oracle calls and runs in time O(n · EO + n2), by Theorem 42 the overall running time is then O(n2 log nM · EO + n3 logO(1) nM) as claimed.

| |
|---|


Needless to say the proof above completely depends on Theorem 42. We remark that one can use the Vaidya’s cutting plane instead of ours to get a time complexity O(n2 log nM · EO + nω+1 logO(1) n · log M). There is actually an alternate argument that gives a time complexity of O(n2 log M · EO + nO(1) · log M). Thus it requires slightly fewer oracle calls at the expense of slower running time. A proof is oﬀered in this section, which can be skipped without any risk of discontinuation. This proof relies the following cutting plane method.

- Theorem 67 ([13] ). Given any convex set K ⊂ [0,1]n with a separation oracle of cost SO, in time O(kSO+knO(1)) one can ﬁnd either ﬁnd a point  x ∈ K or ﬁnd a polytope P such that K ⊂ P and the volume of K is at most 3 2 k.


The Theorem allows us to decrease the volume of the feasible region by a factor of 3 2 k after k iterations. Similar to above, we apply cutting plane to minimize fˆ over the hypercube [0,1]n for O(nlog M) iterations, and outputs any integral point in the remaining feasible region P.

Lemma 68. Let x∗ achieve the minimum function value fˆ(x∗) among the points used to query the separation oracle. Then

- 1. x∗ ∈ P(k), the current feasible region.
- 2. Any  x with fˆ( x) ≤ fˆ(x∗) belongs to P(k).
- 3. suppose x∗i


###### ≥ ··· ≥ x∗i

and let Sj = {i1,...,ij}. Then Sl ∈ arg minSj f(Sj) also belongs to P(k).

n

1

Proof. For any separating hyperplane hTx ≤ fˆ(¯x) given by x¯, we have by Lemma 63 that hTx∗ ≤ fˆ(x∗). Since fˆ(x∗) is the minimum among all fˆ(¯x), hTx∗ ≤ fˆ(¯x) and hence x∗ is not removed by any new separating hyperplane. In other words, x∗ ∈ P(k) . The argument for (2) is analogous.

For (3), recall that by the deﬁnition of Lov´sz extension fˆ(x∗) is a convex combination of f(Sj) and thus the indicator variable ISl for Sl satisﬁes f(ISl) ≤ fˆ(x∗). By Lemma 63 again, this implies hTISl ≤ f(ISl) ≤ fˆ(x∗) ≤ fˆ(¯x) for any separating hyperplane hTx ≤ fˆ(¯x).

| |
|---|


Theorem 69. Suppose that we run Cutting Plane in Theorem 67 for O(nlog M) iterations. Then Sl from the last lemma also minimizes f.

Proof. We use the notations from the last lemma. After k = Knlog2/3 M iterations, the volume of the feasible region P(k) is at most 1/MKn. By the last lemma, ISl ∈ P(k).

Suppose for the sake of contradiction that S minimizes f but f(S) < f(Sl). Since f is integervalued, f(S) + 1 ≤ f(Sl). Let r def= 1/6M. Consider the set B def= { x : 0 ≤ xi ≤ r ∀i ∈/ S, 1 − r ≤ xi ≤ 1 ∀i ∈ S}. We claim that for  x ∈ B,

fˆ( x) ≤ f(S) + 1.

To show this, note that f({i : xi ≥ t}) = f(S) for r < t ≤ 1 − r as xi ≤ r for i ∈/ S and xi ≥ 1 − r for i ∈ S. Now using conditional probability and |f(T)| ≤ M for any T,

fˆ( x) = Et∼[0,1][f({i : xi ≥ t})]

= (1 − 2r)E[f({i : xi ≥ t})|r < t ≤ 1 − r] + r (E[f({i : xi ≥ t})|0 ≤ t ≤ r] + E[f({i : xi ≥ t})|1 − r ≤ t ≤ 1]])

= (1 − r)f(S) + r (E[f({i : xi ≥ t})|0 ≤ t ≤ r + E[f({i : xi ≥ t})|1 − r ≤ t ≤ 1]]) ≤ (1 − 2r)f(S) + 2rM ≤ f(S) + 4rM ≤ f(S) + 1

But now B ⊆ P(k) as fˆ( x) ≤ f(S) + 1 ≤ f(Sl) and by (2) of the last lemma. This would lead to a contradiction since

1 (6M)n

1

MKn ≥ vol(P(k)) for suﬃciently large K.

vol(B) =

>

| |
|---|


Corollary 70. There is an O(n2 log M ·EO+nO(1) log M) time algorithm for submodular function minimization. Proof. This simply follows from the last lemma, Theorem 67, and the fact that our separation oracle runs in time O(n · EO + n2).

| |
|---|


Curiously, we obtained O(log M) rather than O(log nM) as in our algorithm. We leave it as an open problem whether one can slightly improve our running time to O(n2 log M ·EO+n3 logO(1) n· log M). The rest of this paper is devoted to obtaining better strongly polynomial running time.

#### 15 Improved Strongly Polynomial Algorithms for SFM

- In this section we show how our cutting plane method can be used to obtain a O(n3 · EO + n4) time algorithm for SFM, which improves over the currently fastest O(n5 · EO + n6) time algorithm by Orlin.


###### 15.1 Improved Oracle Complexity

We ﬁrst present a simple geometric argument that f can be minimized with just O(n3 log n · EO) oracle calls. While this is our desired query complexity (and it improves upon the previous best known bounds by a factor of O(n2) unfortunately the algorithm runs in exponential time. Nevertheless, it does provide some insight into how our more eﬃcient algorithms should proceed and it alone, does suggests that information theoretically, O(n3 log n·EO) calls suﬃce to solve SFM. In the rest of the paper, we combine this insight with some of the existing SFM tools developed over the last decade to get improved polynomial time algorithms.

Theorem 71. Submodular functions can be minimized with O(n3 log n · EO) oracle calls.

Proof. We use the cutting plane method in Theorem 67 with the separation oracle given by Theorem 61. This method reduce the volume of the feasible region by a factor of (32)k after k iterations if the optimal has not found yet.

Now, we argue that after O(nlog n) iterations of this procedure we have either found a minimizer of f or we have enough information to reduce the dimension of the problem by 1. To see this, ﬁrst note that if the separation oracle ever returns a degenerate hyperplane, then by Lemma 65 then either ∅ or V is the minimizer, which we can determine in time O(EO + n). Otherwise, after 100nlog n iterations, our feasible region P must have a volume of at most 1/n10n . In this case, we claim that the remaining integer points in P all lie on a hyperplane. This holds, as if this was not the case, then there is a simplex , with integral vertices v0,v1,...,vn, contained in P. But then

1 n! |det(v1 − v0 v2 − v0 ... vn − v0)| ≥

1 n!

vol(P) ≥ vol( ) =

where the last inequality holds since the determinant of an integral matrix is integral, yielding a contradiction.

In other words after O(nlog n) iterations, we have reduced the dimension of all viable solutions by at least 1. Thus, we can recurse by applying the cutting plane method to the lower dimensional feasible region, i.e. P is (replaced by) the convex combination of all the remaining integer points. There is a minor technical issue we need to address as our space is now lower dimensional and the starting region is not necessarily the hypercube anymore and the starting volume is not necessarily equal to 1.

We argue that the starting volume is bounded by nO(n). If this is indeed the case, then our previous argument still works as the volume goes down by a factor of 1/nO(n) in O(nlog n) iterations.

Let v ∈ P be an integer point. Now the dim(P)-dimensional ball of radius √n centered at v must contain all the other integer points in P as any two points of {0,1}n are at most √n apart. Thus the volume of P is bounded by the volume of the ball which is nO(n). Now to get the volume down to 1/n10n, the number of iterations is still O(nlog n).

In summary, we have reduced our dimension by 1 using O(nlog n) iterations which requires O(n2 log n · EO) oracle calls (as each separating hyperplane is computed with n · EO oracle calls). This can happen at most n times. The overall query complexity is then O(n3 log n · EO).

Note that the minimizer  x obtained may not be integral. This is not a problem as the deﬁnition of Lov´sz extension implies that if fˆ( x) is minimal, then f({i : xi ≥ t}) is minimal for any t ∈ [0,1].

We remark that this algorithm does not have a polynomial runtime. Even though all the integral vertices of P lie on a hyperplane, the best way we know of that identiﬁes it takes exponential time by checking for all the integer points {0,1}n.

| |
|---|


Remark 72. Note that this algorithm works for minimizing any convex function over the hypercube that obtains its optimal value at a vertex of the hypercube. Formally, our proof of Theorem 71 holds whenever a function f : 2V −→ Rn admits a convex relaxation fˆwith the following properties:

- 1. For every S ⊆ V , fˆ(IS) = f(S).
- 2. Every fˆ( x) can be written as a convex combination S∈S αSf(S), where αS = 1, |S| = O(n), and S can be computed without any oracle call.
- 3. A subgradient ∂fˆ( x) of fˆ at any point  x ∈ [0,1]n can be computed with O(n · EO) oracle calls.


In this case, the proof of Theorem 71, implies that fˆ and f can be minimized with O(n3 log n·EO) oracle calls by using the separating hyperplane ∂fˆ(¯x)T( x − x¯) ≤ 0.

###### 15.2 Technical Tools

To improve upon the running time of the algorithm in the previous section, we use more structure of our submodular function f. Rather than merely showing that we can decrease the dimension of our SFM problem by 1 we show how we can reduce the degrees of freedom of our problem in a more principled way. In Section 15.2.1 we formally deﬁne the abstraction we use for this and discuss how to change our separation oracle to accommodate this abstraction, and in Section 15.2.2 we show how we can deduce these constraints. These tools serve as the foundation for the faster strongly polynomial time SFM algorithms we present in Section 15.3 and Section 15.4.

###### 15.2.1 SFM over Ring Family

For the remainder of the paper we consider a more general problem than SFM in which we wish to compute a minimizer of our submodular function f over a ring family of the ground set V = [n]. A ring family F is a collection of subsets of V such that for any S1,S2 ∈ F, we have S1∪S2,S1∩S2 ∈ F. Thus SFM corresponds to the special case where F consists of every subset of V . This generalization has been considered before in the literature and was essential to the IFF algorithm.

It is well known that any ring family F over V can be represented by a directed graph D = (V,A) where S ∈ F iﬀ S contains all of the descendants of any i ∈ S. An equivalent deﬁnition is that for

any arc (i,j) ∈ A, i ∈ S implies j ∈ S. It is customary to assume that A is acyclic as any (directed) cycle of A can be contracted (see section 15.3.1).

We denote by R(i) the set of descendants of i (including i itself) and Q(i) the set of ancestors of i (including i itself). Polyhedrally, an arc (i,j) ∈ A can be encoded as the constraint xi ≤ xj as shown by the next lemma.

Lemma 73. Let F be a ring family over V and D = (V,A) be its directed acyclic graph representation. Suppose f : V −→ R is submodular with Lov´asz extension fˆ. Then the characteristic vector IS of any minimizer S = arg minS∈F f(S) over F is also the solution to

minfˆ( x) xi ≤ xj ∀(i,j) ∈ A 0 ≤  x ≤ 1

(15.1)

Proof. Let x∗ be a minimizer, and L(t) = {i : x∗i ≥ t}. It is easy to check that the indicator variable IL(t) satisﬁes (15.1) since x∗ does. Moreover, recall that fˆ(x∗) = Et∼[0,1][f(Lt)]. Thus fˆ(x∗) can be written as a convex combination fˆ(x∗) = t αtf(L(t)) = t αtfˆ(IL(t)), where αt > 0 and t αt = 1. Thus all such fˆ(IL(t)) are minimal, i.e. (15.1) has no “integrality gap”.

| |
|---|


We also modify our separation oracle to accommodate for this generalization as follows. Before doing so we need a deﬁnition which relates our BFS to the ring family formalism.

Deﬁnition 74. A permutation (v1,...,vn) of V is said to be consistent with an arc (i,j) if j precedes i in (v1,...,vn). Similarly, a BFS of the base polyhedron is consistent with (i,j) if j precedes i in its deﬁning permutation. (v1,...,vn) (or a BFS) is consistent with A if it is consistent with every (i,j) ∈ A.

Readers may ﬁnd it helpful to keep in mind the following picture which depicts the relative positions between R(i),i,Q(i) in the deﬁning permutation of h that is consistent with A:

##### ······ R(i)\{i} ······ i ······ Q(i)\{i} ······

In Theorem 61, given x¯ ∈ [0,1]n our separating hyperplane is constructed by sorting the entries of x¯. This hyperplane is associated with some BFS h of the base polyhedron. As we shall see towards the end of the section, we would like h to be consistent with every arc (i,j) ∈ A.

This task is easy initially as x¯ satisﬁes xi ≤ xj for (i,j) ∈ A for the starting polytope of (15.1). If xi < xj, nothing special has to be done as j must precede i in the ordering. On the other hand, whenever xi = xj, we can always break ties by ranking j ahead of i.

However, a technical issue arises due to the fact that our cutting plane algorithm may drop constraints from the current feasible region P. In other words, x¯ may violate xi ≥ 0, xj ≤ 1 or xi ≤ xj if it is ever dropped. Fortunately this can be ﬁxed by reintroducing the constraint. We summarize the modiﬁcation needed in the pseudocode below and formally show that it fulﬁlls our requirement.

- Lemma 75. Our modiﬁed separation oracle returns either some BFS h = 0 or a valid separating hyperplane, i.e.


- 1. x¯ either lies on the separating hyperplane or is cut away by it.
- 2. Any minimizer of (15.1) is not cut away by the separating hyperplane.


Algorithm 5: Modiﬁed Separation Oracle Input: x¯ ∈ Rn and the set of arcs A if x¯i < 0 for some i then

- Output: xi ≥ 0 else if x¯j > 1 for some j then

- Output: xj ≤ 1 else if x¯i > x¯j for some (i,j) ∈ A then


###### Output: xi ≤ xj else

Let i1,...,in be a permutation of V such that x¯i1 ≥ ... ≥ x¯inand for all (i,j) ∈ A, j precedes i in i1,...,in. Output: hT x ≤ fˆ(¯x), where h is the BFS deﬁned by the permutation i1,...,in.

Such a hyperplane can be computed with n oracle calls to f and in time O(n · EO + n2).

Proof. If we get xi ≥ 0, xj ≤ 1 or xi ≤ xj (if loop or the ﬁrst two else loops), then clearly x¯ is cut away by it and any minimizer must of course satisfy xi ≥ 0, xj ≤ 1 and xi ≤ xj as they are the constraints in (15.1). This proves (1) and (2) for the case of getting xi ≥ 0, xj ≤ 1 or xi ≤ xj.

Thus it remains to consider the case hT x ≤ fˆ(¯x) (last else loop). First of all, x¯ lies on it as fˆ(¯x) = hTx¯. This proves (1). For (2), we have from Lemma 63 that hT x ≤ fˆ( x). If x∗ is a minimizer of (15.1), we must then have hTx∗ ≤ fˆ(x∗) ≤ fˆ(¯x) as x¯ is also feasible for (15.1).

Finally we note that the running time is self-evident. We stress again that the main purpose of modifying our separation oracle is to ensure that any

| |
|---|


BFS h used to deﬁne a new separating hyperplane must be consistent with every (i,j) ∈ A.

###### 15.2.2 Identifying New Valid Arcs

The reason for considering the ring family generalization of SFM is that our algorithms (and some previous algorithms too) work by adding new arcs to our digraph D. This operation yields a strongly polynomial algorithm since there are only 2· n2 possible arcs to add. Of course, a new arc (i,j) is valid only if i ∈ Smin =⇒ j ∈ Smin for some minimizer Smin. Here we show how to identify such valid arcs by extracting information from certain nice elements of the base polyhedron.

This is guaranteed by the next four lemmas, which are stated in a way diﬀerent from previous works e.g. our version is extended to the ring family setting. This is necessary as our algorithms require a more general formulation. We also give a new polyhedral proof, which is mildly simpler than the previous combinatorial proof. On the other hand, Lemma 80 is new and unique to our work. It is an important ingredient of our O(n3 · EO + n4) time algorithm.

Recall that each BFS of the base polyhedron is deﬁned by some permutation of the ground set elements.

First, we prove the following two lemmas which show that should we ever encounter a nondegenerate point in the base polytope with a coordinate of very large value, then we can immediately conclude that that coordinate must be or must not be in solution to SFM over the ring family.

- Lemma 76. If  y ∈ B(f) is non-degenerate and satisﬁes yi > −(n−1)minj yj, then i is not in any minimizer of f (over the ring family A).


Proof. We proceed by contradiction and suppose that S is a minimizer of f that contains i. Now since  y is non-degenerate we know that minj yj ≤ 0 and by the deﬁnition of  y we have the following contradiction

0 < yi + (n − 1)min

yj ≤

yj =  y(S) ≤ f(S) ≤ f(∅) = 0.

j

j∈S

| |
|---|


- Lemma 77. If  y ∈ B(f) is non-degenerate and satisﬁes yi < −(n − 1)maxj yj, then i is in every minimizer of f (over the ring family A).

Proof. We proceed by contradiction and suppose that S is a minimizer of f that does not contain i. Now since  y is non-degenerate we know that maxj yj ≥ 0 and therefore

j∈[n]

yj = yi +

j∈S

yj +

j∈V −(S+i)

yj < −(n − 1)max

j

yj +

j∈S

yj + (|V | − |S| − 1)max

j

yj ≤

j∈S

yj .

However by the deﬁnition of  y we have

j∈S

yj =  y(S) ≤ f(S) ≤ f(V ) =

j∈[n]

yj .

Thus we have a contradiction and the result follows.

| |
|---|


Now we are ready to present conditions under which a new valid arc can be added. We begin with a simple observation. Let upper(i) def= f(R(i)) − f(R(i) − i) and lower(i) def= f(V \Q(i) + i) − f(V \Q(i)). As the names suggest, they bound the value of hi for any BFS used.

- Lemma 78. For any BFS h used to construct a separating hyperplane given by our modiﬁed separation oracle, we have lower(i) ≤ hi ≤ upper(i).

Proof. Note that by Lemma 75, h is consistent with every (j1,j2) ∈ A and hence i must precede Q(i) and be preceded by R(i). Let S be the set of elements preceding i in the deﬁning permutation of h. Then hi = f(S + i) − f(S) ≤ f(R(i)) − f(R(i) − i) because of diminishing return and R(i) − i ⊆ S. The lower bound follows from the same argument as Q(i) − i comes after i, and so Q(i) ⊆ V \S.

| |
|---|


In the following two lemmas, we show that if upper(i) is ever suﬃciently positive or lower(i) is suﬃciently negative, then we ﬁnd a new arc.

While these lemmas may appear somewhat technical but actually has an intuitive interpretation. Suppose an element p is in a minimizer Smin of f over the ring family D. Then R(p) must also be part of Smin. Now if f(R(p)) is very large relative to f(R(p) − p), there should be some element q ∈ Smin\R(p) compensating for the discrepancy. The lemma says that such an element q can in fact be found eﬃciently.

- Lemma 79 (new arc). Let  y = k λ(k) y(k) be a non-degenerate convex combination of O(n) base polyhedron BFS’s  y(k) which are consistent with every arc (i,j) ∈ A. If some element p satisﬁes


upper(p) > n4 maxyj, then we can ﬁnd, using O(n·EO) oracle calls and O(n2) time, some q ∈/ R(p) such that the arc (p,q) is valid, i.e. if p is in a minimizer, then so is q.

Proof. If maxyj < 0 then we are immediately done by Lemma 65. We assume maxyj ≥ 0 in the proof. For all k let  y (k) be the BFS obtained by taking the deﬁning permutation of  y(k) and moving R(p) to the front while preserving the relative ordering of R(p) within each permutation).

Furthermore, let  y def= k λ(k) y (k). Then since y (pk) = f(R(p)) − f(R(p) − p) = upper(p) we have upper(p) = y p = f(R(p)) − f(R(p) − p). Moreover,

y j ≥ yj ∀j ∈ R(p) and y j ≤ yj ∀j ∈/ R(p) (15.2) by diminishing marginal return.

Now, suppose p is in a minimizer Smin. Then R(p) ⊆ Smin by deﬁnition. We then deﬁne f (S) = f(S ∪ R(p)) for S ⊆ V \R(p). It can be checked readily that f is submodular and Smin\R(p) is a minimizer of f (over the corresponding ring family). Note that now  y V \R(p) (the restriction of  y to V \R(p)) is a convex combination of the BFS’s of the base polyhedron B(f ) of f . We shall show that  y V \R(p) has the desired property in Lemma 77.

Note that y (V \R(p) + p) ≤ y(V \R(p) + p) since y (V \R(p)+p) = y (V )−y (R(p)−p) = y(V )−y (R(p)−p) ≤ y(V )−y(R(p)−p) = y(V \R(p)+p). But now since  y is non-degenerate maxj yj ≥ 0 and therefore

y (V \R(p)) ≤ y(V \R(p) + p) − y p

= y(V \R(p) + p) − (f(R(p)) − f(R(p) − p)) (15.3) ≤ nmaxyj − (f(R(p)) − f(R(p) − p)) < (n − n4)maxyj

Therefore by the Pigeonhole Principle some q ∈/ R(p) must satisfy

y q < (n − n4)maxyj /(n − 1) = −(n3 + n2 + n)maxyj ≤ −(n3 + n2 + n) max

yj ≤ −(n3 + n2 + n) max

j /∈R(p)

y j by (15.2)

j /∈R(p)

By Lemma 77, this q must be in any minimizer of f . In other words, whenever p is in a minimizer of f, then so is q.

Note however that computing all  y would take O(n2) oracle calls in the worst case as there are

O(n)  y (k)’s. We use the following trick to identify some q with y q < −(n − 1)maxyj using just O(n) calls. The idea is that we actually only want to have suﬃcient decreases in y (V \R(p)) which can be accomplished by having a large corresponding decrease in some  y (k).

For each k, by the same argument above (see (15.3))

y (k)(V \R(p)) − y(k)(V \R(p)) ≤ y(pk) − (f(R(p)) − f(R(p) − p)) (15.4) The “weighted decrease” λ(k) y(pk) − (f(R(p)) − f(R(p) − p)) for  y (k) sum up to

λ(k) y(pk) − (f(R(p)) − f(R(p) − p)) = yp − (f(R(p)) − f(R(p) − p)) < (1 − n4)maxyj Thus by the Pigeonhole Principle, some l will have

λ(l) y(pl) − (f(R(p)) − f(R(p) − p)) < (1 − n4)maxyj /O(n) < −n2 maxyj.

For this  y(l) we compute  y (l). We show that  y = λ(l) y (l) + k =l λ(k) y(k) has the same property as  y above.

y (V \R(p)) = λ(l)y (l)(V \R(p)) +

λ(k)y(k)(V \R(p))

k =l

= y(V \R(p)) + λ(l) y (l)(V \R(p)) − y(l)(V \R(p)) ≤ y(V \R(p)) + λ(l) y(pl) − (f(R(p)) − f(R(p) − p)) by (15.4)

< (n − 1)maxyj − n2 maxyj < (n − n2)maxyj

Then some q ∈ V \R(p) must satisfy

n − n2 n − 1

maxyj = −nmaxyj

y q <

That is, the arc (p,q) is valid. This takes O(n) oracle calls as given  y = k λ(k) y(k) , computing

-  y requires knowing only f(R(p)), f(R(p) − p), and  y (l) which can be computed from  y(l) with n oracle calls. The runtime is O(n2) which is needed for computing  y .


| |
|---|


- Lemma 80. Let  y = k λ(k) y(k)be a non-degenerate convex combination of base polyhedron BFS  y(k) which is consistent with every arc (i,j) ∈ A. If lower(p) < n4 minyj, then we can ﬁnd, using O(n · EO) oracle calls and O(n2) time, some q ∈/ Q(p) such that the arc (q,p) is valid, i.e. if p is not in a minimizer, then q is not either.


Proof. It is possible to follow the same recipe in the proof of Lemma 79 but using Lemma 76 instead of Lemma 77. Here we oﬀer a proof which directly invokes Lemma 77 on a diﬀerent submodular function.

Let g be deﬁned by g(S) def= f(V \S) for any S, and Ag be the set of arcs obtained by reversing the directions of the arcs of A. Consider the problem of minimizing g over the ring family Ag. Using subscripts to avoid confusion with f and g, e.g. Rg(i) is the set of descendants of i w.r.t. Ag, it is not hard to verify the following:

- • g is submodular
- • Rg(i) = Qf(i)
- • g(Rg(p)) − g(Rg(p) − p) = −(f(V \Qf(p) + p) − f(V \Qf(p)))
- • − y(k) is a BFS of B(g) if and only if  y(k) is a BFS of B(f)
- • max(−yj) = −minyj


By using the above correspondence and applying Lemma 79 to g and Ag, we can ﬁnd, using O(n) oracle calls and O(n2) time, some q ∈/ Rg(p) = Q(p) such that the arc (p,q) is valid for g and Ag. In other words, the reverse (q,p) will be valid for f and A.

| |
|---|


These lemmas lay the foundation of our algorithm. They suggests that if the positive entries of a point in the base polyhedron are small relative to some upper(p) = f(R(p)) − f(R(p) − p), a new arc (p,q) can be added to A. This can be seen as a robust version of Lemma 65.

Finally, we end the section with a technical lemma that will be used crucially for both of our algorithms. The importance of it would become obvious when it is invoked in our analyses.

- Lemma 81. Let h denote a convex combination of two vectors h and h in the base polyhedron, i.e. h = λ h + (1 − λ) h for some λ ∈ [0,1]. Further suppose that


h 2 ≤ α min λ h 2,(1 − λ) h 2

for some α ≤ 2√1n. Then for p = arg maxj(max{λ|hj|,(1 − λ)|h j|}) we have

- 1

- 2α√n · h ∞ .


1 2α√n · h ∞ and upper(p) ≥

lower(p) ≤ −

Proof. Suppose without loss of generality that λ|hp| ≥ (1 − λ)|h p|. Then by assumptions we have

h ∞ ≤ h 2 ≤ α · min λ h 2,(1 − λ) h 2 ≤ α√n|λhp| .

However, since α ≤ 2√1n we see that

λhp + (1 − λ)h p ≤ h ∞ ≤ α√n|λhp| ≤

- 1

- 2 |λhp| .


Consequently, λhp and (1 − λ)h p have opposite signs and (1 − λ)h p ≥ 12 λh p . We then have,

1 2 |λhp| ≤ −

- 1

- 2α√n


lower(p) ≤ min hp,h p ≤ min λhp,(1 − λ)h p ≤ −

h ∞ and

1 2 |λhp| ≥

- 1

- 2α√n


upper(p) ≥ max hp,h p ≥ max λhp,(1 − λ)h p ≥

h ∞ .

| |
|---|


###### 15.3 O(n4 · EO + n5) Time Algorithm

Here we present a O(n4 · EO + n5) time, i.e. strongly polynomial time algorithm, for SFM. We build upon the algorithm achieved in the section to achieve a faster running time in Section 15.4.

Our new algorithm combines the existing tools for SFM developed over the last decade with our cutting plane method. While there are certain similarities with previous algorithms (especially [54, 60, 56]), our approach signiﬁcantly departs from all the old approaches in one important aspect.

All of the previous algorithms actively maintain a point in the base polyhedron and represent it as a convex combination of BFS’s. At each step, a new BFS may enter the convex combination and an old BFS may exit. Our algorithm, on the other hand, maintains only a collection of BFS’s (corresponding to our separating hyperplanes), rather than an explicit convex combination. A “good” convex combination is computed from the collection of BFS’s only after running Cutting Plane for enough iterations. We believe that this crucial diﬀerence is the fundamental reason which oﬀers the speedup. This is achieved by the Cutting Plane method which considers the geometry of the collection of BFS’s. On the other hand, considering only a convex combination of BFS’s eﬀectively narrows our sight to only one point in the base polyhedron.

###### Overview

Now we are ready to describe our strongly polynomial time algorithm. Similar to the weakly polynomial algorithm, we ﬁrst run our cutting plane for enough iterations on the initial feasible region { x ∈ [0,1]n : xi ≤ xj ∀(i,j) ∈ A}, after which a pair of approximately parallel supporting hyperplanes F1,F2 of width 1/nΘ(1) can be found. Our strategy is to write F1 and F2 as a nonnegative combination of the facets of remaining feasible region P. This combination is made up of newly added separating hyperplanes as well as the inequalities xi ≥ 0, xj ≤ 1 and xi ≤ xj. We then argue that one of the following updates can be done:

- • Collapsing: xi = 0, xj = 1 or xi = xj
- • Adding a new arc (i,j): xi ≤ xj for some (i,j) ∈/ A


The former case is easy to handle by elimination or contraction. If xi = 0, we simply eliminate i from the ground set V ; and if xi = 1, we redeﬁne f so that f(S) = f(S + i) for any S ⊆ V − i. xi = xj can be handled in a similar fashion. In the latter case, we simply add the arc (i,j) to A. We then repeat the same procedure on the new problem.

Roughly speaking, our strongly polynomial time guarantee follows as eliminations and contrac-

tions can happen at most n times and at most 2 · n2 new arcs can be added. While the whole picture is simple, numerous technical details come into play in the execution. We advise readers to

keep this overview in mind when reading the subsequent sections. Algorithm

Our algorithm is summarized below. Again, we remark that our algorithm simply uses Theorem 82 regarding our cutting plane and is agnostic as to how the cutting plane works, thus it could be replaced with other methods, albeit at the expense of slower runtime.

- 1. Run cutting plane on (15.1) (Theorem 82 with τ = Θ(1)) using our modiﬁed separation oracle (Section 15.2.1).
- 2. Identify a pair of “narrow” approximately parallel supporting hyperplanes or get some BFS h = 0 (in which case both ∅ and V are minimizers).
- 3. Deduce from the hyperplanes some new constraint of the forms xi = 0,xj = 1,xi = xj or xi ≤ xj (Section 15.3.2).
- 4. Consolidate A and f (Section 15.3.1).
- 5. Repeat by running our cutting plane method on (15.1) with updated A and f. (Note that Any previously found separating hyperplanes are discarded.)


We call step (1) a phase of cutting plane. The minimizer can be constructed by unraveling the recursion.

###### 15.3.1 Consolidating A and f

Here we detail how the set of valid arcs A and submodular function f should be updated once we deduce new information xi = 0,xi = 1,xi = xj or xi ≤ xj. Recall that R(i) and Q(i) are the sets of descendants and ancestors of i respectively (including i itself). The changes below are somewhat self-evident, and are actually used in some of the previous algorithms so we only sketch how they are done without a detailed justiﬁcation.

Changes to the digraph representation D of our ring family include:

- • xi = 0: remove Q(i) from the ground set and all the arcs incident to Q(i)
- • xi = 1: remove R(i) from the ground set and all the arcs incident to R(i)
- • xi = xj: contract i and j in D and remove any duplicate arcs
- • xi ≤ xj: insert the arc (i,j) to A
- • For the last two cases, we also contract the vertices on a directed cycle of A until there is no more. Remove any duplicate arcs.


Here we can contract any cycle (i1,...,ik) because the inequalities xi1 ≤ xi2,...,xik−1 ≤ xik,xik ≤ xi1 imply xi1 = ... = xik.

Changes to f:

- • xi = 0: replace f by f : 2V \Q(i) −→ R, f (S) = f(S) for S ⊆ V \Q(i)
- • xi = 1: replace f by f : 2V \R(i) −→ R, f (S) = f(S ∪ R(i)) for S ⊆ V \R(i)
- • xi = xj: see below
- • xi ≤ xj: no changes to f needed if it does not create a cycle in A; otherwise see below
- • Contraction of C = {i1,...,ik}: replace f by f : 2V \C+l −→ R, f (S) = f(S) for S ⊆ V \C and f (S) = f((S − l) ∪ C) for S l


Strictly speaking, these changes are in fact not needed as they will automatically be taken care of by our cutting plane method. Nevertheless, performing them lends a more natural formulation of the algorithm and simpliﬁes its description.

###### 15.3.2 Deducing New Constraints xi = 0, xj = 1, xi = xj or xi ≤ xj

Here we show how to deduce new constraints through the result of our cutting plane method. This is the most important ingredient of our algorithm. As mentioned before, similar arguments were used ﬁrst by IFF [56] and later in [54, 60]. There are however two important diﬀerences for our method:

- • We maintain a collection of BFS’s rather a convex combination; a convex combination is computed and needed only after each phase of cutting plane.
- • As a result, our results are proved mostly geometrically whereas the previous ones were proved mostly combinatorially.


Our ability to deduce such information hinges on the power of the cutting plane method in Part I. We re-state our main result Theorem 31 in the language of SFM. Note that Theorem 82 is formulated in a fairly general manner in order to accommodate for the next section. Readers may wish to think τ = Θ(1) for now.

Theorem 82 (Theorem 31 restated for SFM). For any τ ≥ 100, applying our cutting plane method, Theorem 82, to (15.1) with our modiﬁed separation oracle (or its variant in Section 15.4) with high probability in n either

- 1. Finds a degenerate BFS h ≥ 0 or h ≤ 0.


- 2. Finds a polytope P consisting of O(n) constraints which are our separating hyperplanes or the constraints in (15.1). Moreover, P satisﬁes the following inequalities


 cT x ≤ M and  c T x ≤ M ,

both of which are nonnegative combinations of the constraints of P, where || c +  c ||2 ≤ min{|| c||2,|| c ||2}/nΘ(τ) and |M + M | ≤ min{|| c||2,|| c ||2}/nΘ(τ).

Furthermore, the algorithm runs in expected time O(n2τ log n · EO + n3τO(1) logO(1) n).

Proof. In applying Theorem 82 we let K be the set of minimizers of f over the ring family and the box is the hypercube with R = 1. We run cutting plane with our modiﬁed separation oracle (Lemma 75). The initial polytope P(0) can be chosen to be, say, the hypercube. If some separating hyperplane is degenerate, then we have the desired result (and know that either ∅ or V is optimal). Otherwise let P be the current feasible region. Note that P = ∅, because our minimizers of fˆ are all in P(0) and P(k) as they are never cut away by the separating hyperplanes.

Let S be the collection of inequalities (15.1) as well as the separating hyperplanes hT x ≤ fˆ(¯xh) = hTx¯h used. By Theorem 31, all of our minimizers will be contained in P, consisting of O(n) constraints A x ≥ b. Each such constraint  aTi  x ≥ bi is a scaling and shifting of some inequality p Ti  x ≥ qi in S, i.e.  ai = p i/||p i||2 and bi ≤ qi/||p i||2.

By taking = 1/nΘ(τ) with suﬃciently large constant in Θ, our theorem certiﬁes that P

has a narrow width by  a1, some nonnegative combination Oi=2(n) ti ai and point  xo ∈ P with || xo||∞ ≤ 3√nR = 3√n satisying the following:

O(n)

 a1 +

ti ai

i=2

≤ 1/nΘ(τ)

2

0 ≤  aT1  xo − b1 ≤ 1/nΘ(τ)

 

 

T

O(n)

O(n)

tibi ≤ 1/nΘ(τ)

0 ≤

 xo −

tiai

i=2

i=2

We convert these inequalities to p  and q. Let t i def= ti · ||p 1||2/||p i||2 ≥ 0.

O(n)

p 1 +

t ip i

i=2

≤ ||p 1||2/nΘ(τ)

2

0 ≤ p T1  xo − q1 ≤ ||p 1||2/nΘ(τ)

 

 

T

O(n)

O(n)

t iqi ≤ ||p 1||2/nΘ(τ)

0 ≤

 xo −

t ip i

i=2

i=2

We claim that6  c = −p 1, M = −q1,  c = − Oi=2(n) t ip i, M = − Oi=2(n) t iqi satisfy our requirement.

6Minus signs is needed because we express our inequalities as e.g. hT x ≤ hTx¯h whereas in Theorem 31,  aTi  x ≥ bi is used. We apologize for the inconvenience.

We ﬁrst show that || c +  c ||2 ≤ min{|| c||2,|| c ||2}/nΘ(τ). We have || c +  c ||2 ≤ || c||2/nΘ(τ) from the ﬁrst inequality. If || c||2 ≤ || c ||2 we are done. Otherwise, by triangle inequality

|| c ||2 − || c||2 ≤ || c + c ||2 ≤ || c||2/nΘ(τ) =⇒ 2|| c||2 ≥ || c ||2 and hence || c + c ||2 ≤ || c||2/nΘ(τ) ≤ || c ||2/2nΘ(τ) = || c ||2/nΘ(τ).

We also need to prove |M + M | ≤ min{|| c||2,|| c ||2}/nΘ(τ). Summing the second and third inequalities,

−|| c||2/nΘ(τ) ≤ ( c + c )T xo − (M + M ) ≤ 0 Recall that we have || xo||∞ ≤ 3√n. Then

|M + M | ≤ |( c + c )T xo − (M + M )| + |( c + c )T xo| ≤ || c||2/nΘ(τ) + 3√n|| c + c ||2 ≤ || c||2/nΘ(τ) + 3√n|| c||2/nΘ(τ)

= || c||2/nΘ(τ) as desired. Our result then follows as we proved 2|| c ||2 ≥ || c||2.

Finally, we have the desired runtime as our modiﬁed separation oracle runs in time O(n · EO + n2 logO(1) n).

| |
|---|


Informally, the theorem above simply states that after O(nτ log n) iterations of cutting plane, the remaining feasible region P can be sandwiched between two approximately parallel supporting hyperplanes of width 1/nO(τ). A good intuition to keep in mind is that every O(n) iterations of cutting plane reduces the minimum width by a constant factor.

Remark 83. As shown in the proof of Theorem 82, one of the two approximately parallel hyperplanes can actually be chosen to be a constraint of our feasible region P. However we do not exploit this property as it does not seem to help us and would break the notational symmetry in  c and  c .

###### Setup

In each phase, we run cutting plane using Theorem 82 with τ = Θ(1). If some separating hyperplane used is degenerate, we have found the minimizer by Lemma 65.

Now assume none of the separating hyperplanes is degenerate. By Theorem 82, P is sandwiched by a pair of approximately parallel supporting hyperplanes F,F which are of width 1/10n10 apart. The width here can actually be 1/nc for any constant c by taking a suﬃciently large constant in Theta.

Here, we show how to deduce from F and F some xi = 0,,xj = 1,xi = xj, or xi ≤ xj constraint on the minimizers of f over the ring family. Let

 cT x = cixi ≤ M and  c T x = c ixi ≤ M be the inequality for F and F such that

|M + M |, || c + c ||2 ≤ gap, where gap def=

1 10n10

min{|| c||2,|| c ||2}.

By the same theorem we can write  cT x ≤ M as a nonnegative combination of the constraints for P. Recall that the constraints for P take on four diﬀerent forms: (1) −xi ≤ 0; (2) xj ≤ 1; (3) −(xj − xi) ≤ 0; (4) hT x = hixi ≤ fˆ(¯xh). Here the ﬁrst three types are present initially whereas

the last type is the separating hyperplane added. As alleged previously, the coeﬃcient vector h corresponds to a BFS of the base polyhedron for f. Our analysis crucially exploits this property.

Thus suppose  cT x = i cixi ≤ M is a nonnegative combination of our constraints with weights αi,βj,γij,λh ≥ 0. The number of (positive) αi,βj,γij,λh is at most O(n). Here we denote separating hyperplanes by hT x ≤ fˆ(¯xh). Let H be the set of BFS’s used to construct separating hyperplanes.

λhfˆ(¯xh).

 cT x = −

λh hT x and M =

γij(xi − xj) +

αixi +

βjxj +

βj +

i

j

j

h∈H

h∈H

(i,j)∈A

(15.5) Similarly, we write the inequality for F as a nonnegative combination of the constraints for P

and the number of (positive) α i,β j,γ ij,λ h is O(n):

λ hfˆ(¯xh).

 c T x = − α ixi + β jxj +

λ h hT x and M = β j +

γ ij(xi −xj)+

h∈H

h∈H

(i,j)∈A

(15.6) We also scale  c, c ,α,α ,β,β ,γ,γ ,λ,λ so that

(λh + λ h) = 1

h∈H

as this does not change any of our preceding inequalities regarding F and F .

Now that F,F have been written as combinations of our constraints, we have gathered the necessary ingredients to derive our new arc. We ﬁrst give a geometric intuition why we would expect to be able to derive a new constraint. Consider the nonnegative combination making up F. We think of the coeﬃcient βj as the contribution of xj ≤ 1 to F. Now if βj is very large, F is “very parallel” to xj ≤ 1 and consequently F would miss xj = 0 as the gap between F and F is small. P would then miss xj = 0 too as it is sandwiched between F and F . Similarly, a large αi and a large γij would respectively imply that xi = 1 and (xi = 0,xj = 1) would be missed. The same argument works for F as well.

But on the other hand, if the contributions from xi ≥ 0,xj ≤ 1,xi ≤ xj to both F and F

are small, then the supporting hyperplanes  cT x ≤ ... and  c T x ≤ ... would be mostly made up of separating hyperplanes hT x ≤ fˆ(¯xh). By summing up these separating hyperplanes (whose coeﬃcients form BFS’s), we would then get a point in the base polyhedron which is very close to the origin 0. Moreover, by Lemma 81 and Lemma 79 we should then be able to deduce some interesting information about the minimizer of f over D.

The rest of this section is devoted to realizing the vision sketched above. We stress that while the algebraic manipulations may be long, they are simply the execution of this elegant geometric picture.

Now, consider the following weighted sum of hT x ≤ fˆ(¯xh):

λ h hT  x =

λh hT +

h∈H

h∈H

λ h hT x ≤

λh hT x +

h∈H

h∈H

λ hfˆ(¯xh).

λhfˆ(¯xh) +

h∈H

h∈H

###### Observe that h∈H λh hT+ h∈H λ h hT is in the base polyhedron since it is a convex combination of BFS h. Furthermore, using (15.5) and (15.6) this can also be written as

 

  cT x + αixi − βjxj +

λh hT +

λ h hT  x =

γij(xj − xi)

h∈H

h∈H

(i,j)∈A

 

  c T x + α ixi − β jxj +

(15.7)

γ ij(xj − xi)

+

(i,j)∈A

and

λhfˆ(¯xh) +

λ hfˆ(¯xh) = M − βj + M − β j

h∈H

h∈H

= (M + M ) − βj − β j Furthermore, we can bound  cT x+ c T x by  cT x+ c T x ≥ −|| c+ c ||1 ≥ −

√ngap

√n|| c+ c ||2 ≥ −

- as  x ≤ 1. Since M + M ≤ gap, we obtain


LHS def= αixi + α ixi − βjxj − β jxj +

γij(xj − xi) +

γ ij(xj − xi)

(i,j)∈A

(i,j)∈A

≤ 2√ngap − βj − β j

Geometrically, the next lemma states that if the contribution from, say xi ≥ 0, to F is too large, then F would be forced to miss xi = 1 because they are close to one another.

- Lemma 84. Suppose  x satisﬁes (15.1) and LHS ≤ 2√ngap− βj− β j with αi,βj,γij,α i,β j,γ ij ≥


- 0.
- 1. If αi > 2√ngap or α i > 2√ngap, then xi < 1.

- 2. If βj > 2√ngap or β j > 2√ngap, then xj > 0.

- 3. If γij > 2√ngap or γ ij > 2√ngap, then 0 ≤ xj − xi < 1.


Proof. We only prove it for αi,βj,γij as the other case follows by symmetry.

Using 0 ≤ x ≤ 1 and xi ≤ xj for (i,j) ∈ A, we have LHS ≥ αixi − βj − β j. Hence αixi ≤ 2√ngap and we get xi < 1 if αi > 2√ngap.

Similarly, LHS ≥ −βkxk − j =k βj − β j which gives −βkxk ≤ 2√ngap − βk. Then xk > 0 if βk > 2√ngap.

Finally, LHS ≥ γij(xj −xi)− βj − β j which gives γij(xj −xi) ≤ 2√ngap. Then xj −xi < 1 if γij > 2√ngap. We have xi ≤ xj since (i,j) ∈ A.

| |
|---|


So if either condition of Lemma 84 holds, we can set xi = 0 or xj = 1 or xi = xj since our problem (15.1) has an integral minimizer and any minimizer of fˆ is never cut away by Lemma 75. Consequently, in this case we can reduce the dimension by at least 1. From now on we may assume that

max{αi,α i,βj,β j,γij,γ ij} ≤ 2√ngap. (15.8)

Geometrically, (15.8) says that if the supporting hyperplanes are both mostly made up of the separating hyperplanes, then their aggregate contributions to F and F should be small in absolute value.

The next lemma identiﬁes some p ∈ V for which f(R(p)) − f(R(p) − p) is “big”. This prepares for the ﬁnal step of our approach which invokes Lemma 79.

- Lemma 85. Let  y def= h∈H λh h and  y def= h∈H λ h h and let p ∈ arg maxl{max{|yl|,|y l|}} then upper(p) ≥ n7  y +  y ∞


- assuming (15.8). Proof. Recall that  c + c 2 ≤ gap where gap = 10n110 min{|| c||2,|| c ||2},


 c =  y −

i

αi 1i +

j

βj 1j +

γij( 1i − 1j) and  c =  y −

(i,j)

i

α i 1i +

j

γ ij( 1i − 1j).

β j 1j +

(i,j)

- By (15.8) we know that  c −  y 2 ≤ 4n2gap ≤ 104n8  c 2 and  c −  y 2 ≤ 4n2gap ≤ 104n8  c 2. Consequently, by the triangle inequality we have that


 y +  y 2 ≤  c + c 2 +  c −  y 2 +  c −  y 2 ≤ 9n2gap and

4 10n8

 c 2 +  y 2 ⇒  c 2 ≤ 2  y 2

 c 2 ≤  c −  y 2 +  y 2 ≤

Similarly, we have that  c 2 ≤ 2  y 2. Consequently since gap ≤ 10n110 min{|| c||2,|| c ||2}, we have that

2 n8

 y +  y 2 ≤

min  y 2,  y 2 and thus, invoking Lemma 81 yields the result.

| |
|---|


We summarize the results in the lemma below.

Corollary 86. Let P be the feasible region after running cutting plane on (15.1). Then one of the following holds:

- 1. We found a degenerate BFS and hence either ∅ or V is a minimizer.
- 2. The integral points of P all lie on some hyperplane xi = 0, xj = 1 or xi = xj which we can ﬁnd.
- 3. Let H be the collection of BFS’s h used to construct our separating hyperplanes for P. Then there is a convex combination  y of H such that n4|yi| < maxp upper(p) for all i.


Proof. As mentioned before, (1) happens if some separating hyperplane is degenerate. We have (2) if one of the conditions in Lemma 84 holds. Otherwise, y = h∈H λh h + h∈H λ h h is a candidate for Case 3 by Lemma 85.

| |
|---|


Let us revisit the conditions of Lemma 79 and explain that they are satisﬁed by Case 3 of the last lemma.

- •  y is a convex combination of at most O(n) BFS’s. This holds in Case 3 since our current feasible region consists of only O(n) constraints thanks to the Cutting Plane method.
- • Those BFS’s must be consistent with every arc of A. This holds because Case 3 uses the BFS’s for constructing our separating hyperplane. Our modiﬁed separation oracle guarantees that they are consistent with A.


Thus in Case 3 of the last corollary, Lemma 79 allows us to deduce a new constraint xp ≤ xq for some q ∈/ R(p).

- 15.3.3 Running Time Here we bound the total running time of our algorithm and prove the following. Theorem 87. Our algorithm runs in time O(n4 log n · EO + n5 logO(1) n).

Proof. To avoid being repetitive, we appeal to Corollary 86. Each phase of cutting plane takes time O(n2 log n · EO + n3 logO(1) n) (Theorem 82 with τ being a big constant. Given F and F represented as a nonnegative combination of facets, we can check for the conditions in Lemma 84 in O(n) time as there are only this many facets of P. This settles Case 2 of Corollary 86. Finally, Lemma 79 tells us that we can ﬁnd a new arc in O(n · EO + n2) time for Case 3 of Corollary 86. Our conclusion follows from the fact that we can get xi = 0, xi = 1, xi = xj at most n times and xi ≤ xj at most O(n2) times.

| |
|---|


- 15.4 O(n3 · EO + n4) Time Algorithm


Here we show how to improve our running time for strongly polynomial SFM to O(n3·EO+n4). Our algorithm can be viewed as an extension of the algorithm we presented in the previous Section 15.3. The main bottleneck of our previous algorithm was the time needed to identify a new arc, which cost us O(n2 · EO + n3). Here we show how to reduce our amortized cost for identifying a valid arc down to O(n · EO + n2) and thereby achieve our result.

The key observation we make to improve this running time is that our choice of p for adding an arc in the previous lemma can be relaxed. p actually need not be arg maxi upper(i); instead it is enough to have upper(p) > n4 max{αi,α i,βj,β j,γij,γ ij}. For each such p a new constraint xp ≤ xq can be identiﬁed via Lemma 79. So if there are many p’s satisfying this we will be able to obtain many new constraints and hence new valid arcs (p,q).

On the other hand, the bound in Lemma 85 says that our point in the base polyhedron is small in absolute value. This is actually stronger than what we need in Lemma 79 which requires only its positive entries to be “small”. However as we saw in Lemma 80 we can generate a constraint of the form xq ≤ xp whenever lower(p) is suﬃciently negative.

Using this idea, we divide V into diﬀerent buckets according to upper(p) and lower(p). This will allow us to get a speedup for two reasons.

First, bucketing allows us to disregard unimportant elements of V during certain executions of our cutting plane method. If both upper(i) and lower(i) are small in absolute value, then i is essentially negligible because for a separating hyperplane hT x ≤ fˆ(¯x), any hi ∈ [lower(i),upper(i)] small in absolute value would not really make a diﬀerence. We can then run our cutting plane algorithm only on those non-negligible i’s, thereby reducing our time complexity. Of course, whether hi is small is something relative. This suggests that partitioning the ground set by the relative size of upper(i) and lower(i) is a good idea.

Second, bucketing allows us to ensure that we can always add an arc for many edges simultaneously. Recall that we remarked that all we want is nO(1)|yi| ≤ upper(p) for some  y in the base polyhedron. This would be suﬃcient to identify a new valid arc (p,q). Now if the marginal differences upper(p) and upper(p ) are close in value, knowing nO(1)|yi| ≤ upper(p) would eﬀectively give us the same for p for free. This suggests that elements with similar marginal diﬀerences should be grouped together.

The remainder of this section simply formalizes these ideas. In Section 15.4.1 we discuss how we partition the ground set V . In Section 15.4.2, we present our cutting plane method on a subset of the coordinates. Then in Section 15.4.3 we show how we ﬁnd new arcs. Finally, in Section 15.4.4 we put all of this together to achieve our desired running time.

###### 15.4.1 Partitioning Ground Set into Buckets

We partition the ground set V into diﬀerent buckets according to the values of upper(i) and lower(i). This is reminiscent to Iwata-Orlin’s algorithm [60] which considers elements with big upper(i). However they did not need to do bucketing by size or to consider lower(i), whereas these seem necessary for our algorithm.

Let N = maxi{max{upper(i),−lower(i)}} be the largest marginal diﬀerence in absolute value. By Lemma (78), N ≥ 0. We partition our ground set V as follows:

B1 = {i : upper(i) ≥ N/n10 or lower(i) ≤ −N/n10} Bk = {i ∈/ B1 ∪ ... ∪ Bk−1 : N/n10k ≤ upper(i) < N/n10(k−1)

or − N/n10(k−1) < lower(i) ≤ −N/n10k}, k ≥ 2

We call Bk buckets. Our buckets group elements by the values of upper(i) and lower(i) at 1/n10 “precision”. There are two cases.

- • Case 1: the number of buckets is at most log n7, in which case upper(i) > N/nO(logn) or lower(i) < −N/nO(logn) for all i.
- • Case 2: there is some k for which |B1 ∪ ... ∪ Bk| ≥ |Bk+1|.


This is because if there is no such k in Case 2, then by induction each bucket Bk+1 has at least 2k|B1| ≥ 2k elements and hence k ≤ log n.

Case 1 is easier to handle, and is in fact a special case of Case 2. We ﬁrst informally sketch the treatment for Case 1 which should shed some light into how we deal with Case 2.

We run Cutting Plane for O(nlog2 n) iterations (i.e. τ = Θ(log n)). By Theorem 82, our feasible region P would be sandwiched by a pair of approximately parallel supporting hyperplanes of width

- at most 1/nΘ(logn). Now proceeding as in the last section, we would be able to ﬁnd some  y in the base polyhedron and some element p such that nΘ(logn)|yi| ≤ upper(p). This gives


upper(p) nΘ(logn) ≤

N nΘ(logn)

nΘ(logn)|yi| ≤

.

Since upper(i) > N/nΘ(logn) or lower(i) < −N/nΘ(logn) for all i in Case 1, we can then conclude that some valid arc (i,q) or (q,i) can be added for every i. Thus we add n/2 arcs simultaneously in one phase of the algorithm at the expense of blowing up the runtime by O(log n). This saves a factor of n/log n from our runtime in the last section, and the amortized cost for an arc would then be O(n · EO + n2).

On the other hand, in Case 2 we have a “trough” at Bk+1. Roughly speaking, this trough is useful for acting as a soft boundary between B1 ∪ ... ∪ Bk and l≥k+2 Bl. Recall that we are able to “ignore” l≥k+2 Bl because their hi is relatively small in absolute value. In particular, we know that for any p ∈ B1 ∪ ... ∪ Bk and i ∈ Bl, where l ≥ k + 2,

max{upper(p),−lower(p)} ≥ n10 max{upper(i),−lower(i)}.

This is possible because Bk+1, which is sandwiched in between, acts like a shield preventing Bl to “mess with” B1 ∪ ... ∪ Bk. This property comes at the expense of sacriﬁcing Bk+1 which must confront Bl.

Furthermore, we require that |B1 ∪ ... ∪ Bk| ≥ |Bk+1|, and run Cutting Plane on B = (B1 ∪

... ∪ Bk) ∪ Bk+1. If |Bk+1| |B1 ∪ ... ∪ Bk|, our eﬀort would mostly be wasted on Bk+1 which is sacriﬁced, and the amortized time complexity for B1 ∪ ... ∪ Bk would then be large.

Before discussing the algorithm for Case 2, we need some preparatory work.

7More precisely, Bk = ∅ for k > log n .

###### 15.4.2 Separating Hyperplane: Project and Lift

Our speedup is achieved by running our cutting plane method on the projection of our feasible region onto B := (B1 ∪ ··· ∪ Bk) ∪ Bk+1. More precisely, we start by running our cutting plane on PB = { x ∈ RB : ∃ x ∈ RB¯ s.t. ( x, x ) satisﬁes (15.1)}, which has a lower dimension. However, to do this, we need to specify a separation oracle for PB. Here we make one of the most natural choices.

We begin by making an apparently immaterial change to our set of arcs A. Let us take the transitive closure of A by adding the arc (i,j) whenever there is a path from i to j. Clearly this would not change our ring family as a path from i to j implies j ∈ R(i). Roughly speaking, we do this to handle pathological cases such as (i,k),(k,j) ∈ A,(i,j) ∈/ A and i,j ∈ B,k ∈/ B. Without introducing the arc (i,j), we risk confusing a solution containing i but not j as feasible since we are restricting our attention to B and ignoring k ∈/ B.

- Deﬁnition 88. Given a digraph D = (V,A), the transitive closure of A is the set of arcs (i,j) for which there is a directed path from i to j. We say that A is complete if it is equal to its transitive closure.

Given x¯ ∈ [0,1]B, we deﬁne the completion of x¯ with respect to A as follows.

- Deﬁnition 89. Given x¯ ∈ [0,1]B and a set of arcs A, xC ∈ [0,1]n is a completion of x¯ if xCB = x¯ and xCi ≤ xCj for every (i,j) ∈ A. Here xCB denotes the restriction of xC to B.


- Lemma 90. Given x¯ ∈ [0,1]B and a complete set of arcs A, there is a completion of x¯ if x¯i ≤ x¯j for every (i,j) ∈ A ∩ (B × B). Moreover, it can be computed in O(n2) time. Proof. We set xCB = x¯. For i ∈/ B, we set


1 if j ∈ B s.t. (i,j) ∈ A min(i,j)∈A,j∈B xCj otherwise

xCi =

One may verify that xC satisﬁes our requirement as A is complete. Computing each xCi takes O(n) time. Since |V \B| = |B¯| ≤ n, computing the whole xC takes O(n2) time.

| |
|---|


This notion of completion is needed since our original separation oracle requires a full dimensional input x¯. Now that x¯ ∈ RB, we need a way of extending it to Rn while retaining the crucial property that h is consistent with every arc in A.

Note that the runtime is still O(n · EO + n2 logO(1) n) as xC can be computed in O(n2) time by the last lemma.

We reckon that the hyperplane hTB xB ≤ i∈B hix¯i returned by the oracle is not a valid separating hyperplane (i.e. it may cut out the minimizers). Nevertheless, we will show that it is a decent “proxy” to the true separating hyperplane hT x ≤ fˆ(xC) = i∈V hixCi and is good enough to serve our purpose of sandwiching the remaining feasible region in a small strip. To get a glimpse, note that the terms missing hTB xB ≤ i∈B hix¯i all involve hi for i ∈/ B, which is “negligible” compared to B1 ∪ ··· ∪ Bk.

One may try to make hTB xB ≤ i∈B hix¯i valid, say, by hTB xB ≤ i∈B hix¯i + i/∈B |hi|. The problem is that such hyperplanes would not be separating for x¯ anymore as hTBx¯ = i∈B hix¯i <

i∈B hix¯i + i/∈B |hi|. Consequently, we lose the width (or volume) guarantee of our cutting plane algorithm. Although this seems problematic, it is actually still possible to show a guarantee suﬃcient for our purpose as i/∈B |hi| is relatively small. We leave it as a nontrivial exercise to interested readers.

Algorithm 6: Projected Separation Oracle Input: x¯ ∈ RB and a complete set of arcs A if x¯i < 0 for some i ∈ B then

- Output: xi ≥ 0 else if x¯j > 1 for some j ∈ B then

- Output: xj ≤ 1 else if x¯i > x¯j for some (i,j) ∈ A ∩ B2 then


###### Output: xi ≤ xj else

Let xC ∈ Rn be a completion of x¯ Let i1,...,in be a permutation of V such that xCi

≥ ... ≥ xCi

and for all (i,j) ∈ A, j

n

1

precedes i in i1,...,in. Output: hTB xB = i∈B hixi ≤ i∈B hix¯i, where h is the BFS deﬁned by the permutation i1,...,in.

In conclusion, it seems that one cannot have the best of both worlds: the hyperplane returned by the oracle cannot be simultaneously valid and separating. Algorithm

We take k to be the ﬁrst for which |B1∪...∪Bk| ≥ |Bk+1|, i.e. |B1∪...∪Bl| < |Bl+1| for l ≤ k−1. Thus k ≤ log n. Let b = |B|, and so |B1 ∪···∪Bk| ≥ b/2. Case 1 is a special case by taking B = V .

Our algorithm is summarized below. Here A is always complete as A is replaced its transitive closure whenever a new valid arc is added.

- 1. Run Cutting Plane on PB = {x ∈ RB : ∃x ∈ RB¯ s.t. (x,x ) satisﬁes (15.1)} with the new projected separation oracle.
- 2. Identify a pair of “narrow” approximately parallel supporting hyperplanes.
- 3. Deduce from the hyperplanes certain new constraints of the forms xi = 0,xj = 1,xi = xj or xi ≤ xj by lifting separating hyperplanes back to Rn
- 4. Consolidate A and f. If some xi ≤ xj added, replace A by its transitive closure.
- 5. Repeat Step 1 with updated A and f. (Any previously found separating hyperplanes are discarded.)


The minimizer can be constructed by unraveling the recursion.

First of all, to be able to run Cutting Plane on PB we must come up with a polyhedral description of PB which consists of just the constraints involving B. This is shown in the next lemma.

- Lemma 91. Let PB = { x ∈ RB : ∃ x ∈ RB¯ s.t. ( x, x ) satisﬁes (15.1)}. Then PB = { x ∈ RB : 0 ≤  x ≤ 1,xi ≤ xj∀(i,j) ∈ A ∩ (B × B)}


Proof. It is clear that PB ⊆ { x ∈ RB : 0 ≤  x ≤ 1,xi ≤ xj∀(i,j) ∈ A ∩ (B × B)} as the constraints 0 ≤ x ≤ 1,xi ≤ xj∀(i,j) ∈ A ∩ (B × B) all appear in (15.1).

Conversely, for any  x ∈ RB satisfying 0 ≤  x ≤ 1,xi ≤ xj∀(i,j) ∈ A ∩ (B × B), we know there is some completion xC of  x by Lemma 90 as A is complete. Now xC satisﬁes (15.1) by deﬁnition, and hence  x ∈ PB.

| |
|---|


The only place where we have really changed the algorithm is Step (3).

- 15.4.3 Deducing New Constraints xi = 0, xj = 1, xi = xj or xi ≤ xj Our method will deduce one of the following:


- • xi = 0, xj = 1 or xi = xj
- • for each p ∈ B1 ∪ ··· ∪ Bk, xp ≤ xq for some q ∈/ R(p) or xp ≥ xq for some q ∈/ Q(p)


Our argument is very similar to the last section’s. Roughly speaking, it is the same argument but with “noise” introduced by i ∈/ B. We use extensively the notations from the last section.

Our main tool is again Theorem 82. Note that n should be replaced by b in the Theorem statement. We invoke it with τ = k logb n = O(log2 n) (using k ≤ log n) to get a width of

- 1/bΘ(τ) = 1/nΘ(k). This takes time at most O(bnlog2 n·EO+bn2 logO(1) n). Again, this is intuitively clear as we run it for O(kblog n) iterations, each of which takes time O(n · EO + n2 logO(1) n).


After each phase of (roughly O(kblog n) iterations) of Cutting Plane, PB is sandwiched between a pair of approximately parallel supporting hyperplanes F and F which have width 1/n20k. Let F and F be

 cT xB =

cixi ≤ M,  c T xB =

c ixi ≤ M ,

i∈B

i∈B

such that

1 n20k

|M + M |, || c + c ||2 ≤ gap, where gap =

min{|| c||2,|| c ||2}.

The rest of this section presents an execution of the ideas discussed above. All of our work is basically geared towards bringing the amortized cost for identifying a valid arc down to O(n · EO + n2). Again, we can write these two constraints as a nonnegative combination. Here x¯Ch is the completion of the point x¯h used to construct hTB xB ≤ hTB x ¯Ch B. (Recall that x ¯Ch B is the restriction of x¯Ch to B.)

 cT xB = −

αixi+

i∈B

γij(xi−xj)+

βjxj+

j∈B

h∈H

(i,j)∈A∩B2

λh hTB xB and M =

j∈B

λh hTB x ¯Ch B .

βj+

h∈H

 c T xB = −

α ixi+

i∈B

j∈B

γ ij(xi−xj)+

β jxj+

h∈H

(i,j)∈A∩B2

λ h hTB xB and M =

j∈B

λ h hTB x ¯Ch B .

β j+

h∈H

As we have discussed, the problem is that the separating hyperplanes hTB xB ≤ hTB x ¯Ch B are not actually valid. We can, however, recover their valid counterpart by lifting them back to hT x ≤ hTx¯Ch. The hope is that hTB xB ≤ hTB x ¯Ch B and hT x ≤ hTx¯Ch are not too diﬀerent so that the arguments will still go through. We show that this is indeed the case.

Again, we scale c,c ,α,α ,β,β ,γ,γ ,λ,λ so that

(λh + λ h) = 1.

h∈H

By adding all the constituent separating hyperplane inequalities, we get

λ h hTx¯Ch Let

λh hTx¯Ch +

λh hT x +

λ h hT x ≤

h∈H

h∈H

h∈H

h∈H

LHS def= αixi + α ixi − βjxj − β jxj + γij(xj − xi) + γ ij(xj − xi). Here we know that

λh hT x +

λ h hT x = LHS + ( c + c )T xB +

λh hTB¯ xB¯ +

λ h hTB¯ xB¯

h∈H

h∈H

h∈H

h∈H

λ h hTB¯ x ¯Ch B ¯ − βj − β j Combining all yields

λh hTx¯Ch +

λ h hTx¯Ch = (M + M ) +

λh hTB¯ x ¯Ch B ¯ +

h∈H

h∈H

h∈H

h∈H

λh hTB¯ x ¯Ch B ¯+

λ h hTB¯ x ¯Ch B ¯− βj− β j

LHS+( c+ c )T xB+

λh hTB¯ xB¯+

λ h hTB¯ xB¯ ≤ (M+M )+

h∈H

h∈H

h∈H

h∈H

√n|| c +  c ||2 ≥ −

√ngap. Since

Here ( c +  c )T xB can be bounded as before: ( c +  c )T xB ≥ −

M + M ≤ gap, We then obtain LHS+

λ h hTB¯ xB¯ ≤ 2√ngap+

λh hTB¯ x ¯Ch B ¯ +

λ h hTB¯ x ¯Ch B ¯ − βj − β j

λh hTB¯ xB¯ +

h∈H

h∈H

h∈H

h∈H

We should expect the contribution from hB¯ to be small as hi for i ∈/ B is small compared to B1 ∪ ... ∪ Bk. We formalize our argument in the next two lemmas.

- Lemma 92. We have h∈H λh hTB¯ x ¯Ch B ¯ + h∈H λ h hTB¯ x ¯Ch B ¯ ≤ N/n10(k+1)−1.

Proof. We bound each component of h∈H λh hTB¯ x ¯Ch B ¯ + h∈H λ h hTB¯ x ¯Ch B ¯. For i ∈ B¯, we have upper(i) ≤ N/n10(k+1). By Lemma 78 hi ≤ upper(i). Therefore,

h∈H

λh hTi x ¯Ch i +

h∈H

λ h hTi x ¯Ch i ≤

h∈H

λh +

h∈H

λ h N/n10(k+1) = N/n10(k+1).

Our result then follows since

h∈H

λh hTB¯ x ¯Ch B ¯ +

h∈H

λ h hTB¯ x ¯Ch B ¯ =

i∈B¯ h∈H

λh hTi x ¯Ch i +

h∈H

λ h hTi x ¯Ch i .

| |
|---|


- Lemma 93. We have h∈H λh hTB¯ xB¯ + h∈H λ h hTB¯ xB¯ ≥ −N/n10(k+1)−1.


Proof. The proof is almost identical to the last lemma except that we use hi ≥ lower(i) instead of hi ≤ upper(i), and lower(i) ≥ −N/n10(k+1).

| |
|---|


The two lemmas above imply that

LHS ≤ 2√ngap − βj − βj + 2N/n10(k+1)−1 = gap − βj − βj where gap = 2√ngap + 2N/n10(k+1)−1.

###### Lemma 94. Suppose x satisﬁes (15.1) and LHS ≤ gap − βj − β j with αi,βj,γij,α i,β j,γ ij ≥

- 0.
- 1. If αi > gap or α i > gap , then xi < 1.
- 2. If βj > gap or β j > gap , then xj > 0.
- 3. If γij > gap or γ ij > gap , then 0 ≤ xj − xi < 1.


Proof. The proof is exactly the same as Lemma 84 with 2√ngap replaced by gap . From now on we may assume that max{αi,α i,βj,β j,γij,γ ij} ≤ gap . (15.9)

| |
|---|


###### Lemma 95. Let  y def= h∈H λh h and  y def= h∈H λ h h and let p ∈ arg maxl∈B{max{|yl|,|y l|} then

N ≥ n10k+6  yB +  y B ∞

- assuming (15.9). Proof. Recall that  c+ c 2 ≤ gap < gap where gap = n201k min{|| c||2,|| c ||2} and gap = 2√ngap+


- 2N/n10(k+1)−1. Now there are two cases. Case 1: 2√ngap ≥ 2N/n10(k+1)−1. Then gap ≤ 4√ngap and we follow the same proof of


Lemma 85. We have

 c =  yB −

i

αi 1i +

j

βj 1j +

(i,j)

γij( 1i − 1j) and  c =  y B −

i

α i 1i +

j

γ ij( 1i − 1j).

β j 1j +

(i,j)

- By (15.9) we know that  c −  yB 2 ≤ 4n2gap ≤ n171k  c 2 and  c −  y B 2 ≤ 4n2gap ≤ n171k  c 2. Consequently, by the triangle inequality we have that


 yB +  y B 2 ≤  c + c 2 +  c −  yB 2 +  c −  y B 2 ≤ 9n2gap and

1 n17k

 c 2 ≤  c −  yB 2 +  yB 2 ≤

 c 2 +  yB 2 ⇒  c 2 ≤ 2  yB 2

Similarly, we have that  c 2 ≤ 2  y B 2. Consequently since gap ≤ n191k min{|| c||2,|| c ||2}, we have that

18 n17k

 yB +  y B 2 ≤

min  yB 2,  y B 2 and thus, invoking Lemma 81 yields N ≥ upper(p) ≥ n16k  yB +  y B ∞, as desired.

Case 2: 2√ngap < 2N/n10(k+1)−1. Then for any i ∈ B, |ci + c i| ≤ || c +  c ||2 ≤ gap < 2N/n10(k+1)−1. Since

 yB +  y B = ( c + c ) +

i

αi 1i −

j

βj 1j −

γij( 1i − 1j) +

(i,j)

i

α i 1i −

j

β j 1j −

γ ij( 1i − 1j)

(i,j)

we have

 yB +  y B ∞ ≤ 2N/n10(k+1)−1 + 2n1.5gap ≤ N/n10k+7.

| |
|---|


Corollary 96. Let P be the feasible region after running Cutting Plane on (15.1) with the projected separation oracle. Then one of the following holds:

- 1. We found a BFS h with hB = 0.
- 2. The integral points of P all lie on some hyperplane xi = 0,xj = 1 or xi = xj.
- 3. Let H be the collection of BFS’s h used to construct our separating hyperplanes for P. Then there is a convex combination  y of H such that for p ∈ B1∪···∪Bk, we have n4|yi| < upper(p) or lower(p) < −n4|yi| for all i.


Proof. As mentioned before, (1) happens if some separating hyperplane satisﬁes hB = 0 when running cutting plane on the non-negligible coordinates. We have (2) if some condition in Lemma

94 holds. Otherwise, we claim y = h λhh + h λ hh is a candidate for Case 3. y is a convex combination of BFS and by Lemma 95, for the big elements i ∈ B we have

1 n4

|yi| ≤ N/n10k+6 ≤

max{upper(p),−lower(p)}.

where the last inequality holds since for p ∈ B1 ∪ ··· ∪ Bk, max{upper(p),−lower(p)} ≥ N/n10k. On the other hand, for the small elements i ∈/ B, |yi| ≤ N/n10(k+1) ≤ n14 max{upper(p),−lower(p)}

- as desired.


| |
|---|


The gap is then smaller enough to add an arc for each p ∈ B1 ∪ ··· ∪ Bk by Lemmas 79 and 80. Therefore we can add a total of |B1 ∪ ··· ∪ Bk|/2 ≥ b/4 arcs with roughly O(kblog n) = O(b) iterations of Cutting Plane, each of which takes O(n · EO + n2). That is, the amortized cost for each arc is O(n·EO+n2). We give a more formal time analysis in below but it should be somewhat clear why we have the desired time complexity.

Lemma 97. Suppose there is a convex combination  y of H such that for p ∈ B1 ∪ ··· ∪ Bk, we have n4|yi| < upper(p) or lower(p) < −n4|yi| for all i. Then we can identify at least b/4 new valid arcs.

Proof. We have |H| = O(n) since H is the set of BFS’s used for the constraints of P which has O(n) constraints. By Lemmas 79 and 80, for p ∈ B1 ∪ ··· ∪ Bk we can add a new valid arc (p,q) or (q,p). However note that a new arc (p1,p2) may added twice by both p1 and p2. Therefore the total number of new arcs is only at least |B1 ∪ ··· ∪ Bk|/2 ≥ b/4.

| |
|---|


###### 15.4.4 Running Time

Not much changes to the previous runtime analysis are needed. To avoid repetition, various details already present in the corresponding part of the last section are omitted. Recall k ≤ log n, and of course, b ≤ n.

For each (roughly) O(kblog n) iterations of Cutting Plane we either get xi = 0,xi = 1,xi = xj or b/4 xi ≤ xj’s. The former can happen at most n times while in the latter case, the amortized cost of each arc is O(k log n) iterations of Cutting Plane. In the worst case the overall number of iterations required is O(n2). Thus our algorithm has a runtime of O(n3 · EO + n4) since each iteration is O(n · EO + n2) as shown below.

Theorem 98. Our algorithm runs in time O(n3 log2 n · EO + n4 logO(1) n).

Proof. We use Corollary 96. First we note that Case 1 can actually be integrated into Case 3 since max{upper(p),−lower(p)} ≥ N/n10k = n10N/n10(k+1) ≥ hi for i ∈/ B.

As we have argued in the beginning of the last section, Theorem 82 with τ = k logb n implies that the runtime for each phase is O(bnlog2 n · EO + bn2 logO(1) n). In each phase we either get xi = 0, xi = 1, xi = xj (Case 2) or b/4 xi ≤ xj’s (Case 3), the latter of which follows from Corollary

- 96 and Lemma 97. Case 2 can only happen n times. Thus the total cost is at most O(n3 log2 n·EO+n4 logO(1) n).


The overhead cost is also small. Similar to before, given F and F represented as a nonnegative combination of facets, we can check for the conditions in Lemma 94 in O(n) time as there are only this many facets of P. This settles Case 2.

For case 3 the amortized cost for each arc is O(nlog2 n·EO+n2 logO(1) n). Our desired runtime follows since there are only O(n2) arcs to add. Unlike Case 2 some extra care is needed to handle the overhead cost. The time needed to deduce a new arc (applying Lemmas 79 and 80 to  y and p ∈ B1 ∪ ··· ∪ Bk) is still O(n · EO + n2). But as soon as we get a new arc, we must update A to be its transitive closure so that it is still complete. Given A complete and a new arc (p,q) ∈/ A, we can simply add the arcs from the ancestors of p to q and from p to the descendants of q. There are

- at most O(n) arcs to add so this takes time O(n2) per arc, which is okay.


| |
|---|


#### 16 Discussion and Comparison with Previous Algorithms

We compare and contrast our algorithms with the previous ones. We focus primarily on strongly polynomial time algorithms.

###### Convex combination of BFS’s

All of the previous algorithms maintain a convex combination of BFS’s and iteratively improve over it to get a better primal solution. In particular, the new BFS’s used are typically obtained by making local changes to existing ones. Our algorithms, on the other hand, considers the geometry of the existing BFS’s. The weighted “inﬂuences”8 then aggregately govern the choice of the next BFS. We believe that this is the main driving force for the speedup of our algorithms.

###### Scaling schemes

Many algorithms for combinatorial problems are explicitly or implicitly scaling a potential function or a parameter. In this paper, our algorithms in some sense aim to minimize the volume of the feasible region. Scaling schemes for diﬀerent potential functions and parameters were also designed in previous works [56, 54, 60, 53]. All of these functions and parameters have an explict form. On the contrary, our potential function is somewhat unusual in the sense that it has no closed form.

###### Deducing new constraints

As mentioned in the main text, our algorithms share the same skeleton and tools for deducing new constraints with [56, 54, 60, 53]. Nevertheless, there are diﬀerences in the way these tools are employed. Our algorithms proceed by invoking them in a geometric manner, whereas previous algorithms were mostly combinatorial.

###### Big elements and bucketing

Our bucketing idea has roots in Iwata-Orlin’s algorithm [60] but is much more sophisticated. For instance, it is suﬃcient for their algorithm to consider only big elements, i.e. upper(i) ≥ N/nO(1). Our algorithm, on the other hand, must carefully group elements by the size of both upper(i) and

8In the terminology of Part I, these weighted inﬂuences are the leverage scores.

lower(i). The speedup appears impossible without these new ideas. We do however note that it is unfair to expect such a sophisticated scheme in Iwata-Orlin’s algorithm as it would not lead to a speedup. In other words, their method is fully suﬃcient for their purposes, and the simplicity in their case is a virtue rather than a shortcoming.

###### 16.1 Open Problems

One natural open problem is improving our weakly polynomial algorithm to O(n2 log M · EO + n3 logO(1) n · log M) time. Our application of center of mass to SFM demonstrates that it should be possible.

For strongly polynomial algorithms, the existential result of Theorem 71 shows that SFM can be solved with O(n3 log n · EO) oracle calls. Unfortunately, our algorithm incurs an overhead of log n as there can be as many as log n buckets each time. One may try to remove this log n overhead by designing a better bucketing scheme or arguing that more arcs can be added.

The other log n overhead seem much trickier to remove. Our method currently makes crucial use of the tools developed by [56], where the log n factors in the runtime seem inevitable. We suspect that our algorithm may have an analogue similar to [93, 90], which do not carry any log n overhead in the running time.

Perhaps an even more interesting open problem is whether our algorithm is optimal (up to polylogarithmic factors). There are grounds for optimism. So far the best way of certifying the optimality of a given solution S ⊆ V is to employ duality and express some optimal solution to the base polyhedron as a convex combination of n+1 BFS’s. This already takes n2 oracle calls as each BFS requires n. Thus one would expect the optimal number of oracle calls needed for SFM to be at least n2. Our bound is not too far oﬀ from it, and anything strictly between n2 and n3 seems instinctively unnatural.

#### Acknowledgments

We thank Matt Weinberg for insightful comments about submodular minimization and minimizing the intersection of convex sets that were deeply inﬂuential to our work. We thank Yan Kit Chim, Stefanie Jegelka, Jonathan A. Kelner, Robert Kleinberg, Pak-Hin Lee, Christos Papadimitriou, and Chit Yu Ng for many helpful conversations. We thank Chien-Chung Huang for pointing out a typo in an earlier draft of this paper. This work was partially supported by NSF awards 0843915 and 1111109, NSF grants CCF0964033 and CCF1408635, Templeton Foundation grant 3966, NSF Graduate Research Fellowship (grant no. 1122374). Part of this work was done while the ﬁrst two authors were visiting the Simons Institute for the Theory of Computing, UC Berkeley. Lastly, we would like to thank Vaidya for his beautiful work on his cutting plane method.

#### References

- [1] Dimitris Achlioptas. Database-friendly random projections: Johnson-lindenstrauss with binary coins. Journal of computer and System Sciences, 66(4):671–687, 2003.
- [2] Martin Aigner and Thomas A Dowling. Matching theory for combinatorial geometries. Transactions of the American Mathematical Society, 158(1):231–245, 1971.


- [3] Zeyuan Allen-Zhu, Yin Tat Lee, and Lorenzo Orecchia. Using optimization to obtain a width-independent, parallel, simpler, and faster positive sdp solver. arXiv preprint arXiv:1507.02259, 2015.
- [4] Kurt M Anstreicher. Large step volumetric potential reduction algorithms for linear programming. Annals of Operations Research, 62(1):521–538, 1996.
- [5] Kurt M Anstreicher. On vaidya’s volumetric cutting plane method for convex programming. Mathematics of Operations Research, 22(1):63–89, 1997.
- [6] Kurt M Anstreicher. Towards a practical volumetric cutting plane method for convex programming. SIAM Journal on Optimization, 9(1):190–206, 1998.
- [7] Kurt M Anstreicher. The volumetric barrier for semideﬁnite programming. Mathematics of Operations Research, 25(3):365–380, 2000.
- [8] Sanjeev Arora, Elad Hazan, and Satyen Kale. Fast algorithms for approximate semideﬁnite programming using the multiplicative weights update method. In Foundations of Computer Science, 2005. FOCS 2005. 46th Annual IEEE Symposium on, pages 339–348. IEEE, 2005.
- [9] Sanjeev Arora and Satyen Kale. A combinatorial, primal-dual approach to semideﬁnite programs. In Proceedings of the thirty-ninth annual ACM symposium on Theory of computing, pages 227–236. ACM, 2007.
- [10] David S Atkinson and Pravin M Vaidya. A cutting plane algorithm for convex programming that uses analytic centers. Mathematical Programming, 69(1-3):1–43, 1995.
- [11] Francis Bach. Learning with submodular functions: A convex optimization perspective. Foundations and Trends in Machine Learning, 2013.
- [12] Francisco Barahona and William H Cunningham. A submodular network simplex method. In Mathematical Programming at Oberwolfach II, pages 9–31. Springer, 1984.
- [13] Dimitris Bertsimas and Santosh Vempala. Solving convex programs by random walks. Journal of the ACM (JACM), 51(4):540–556, 2004.
- [14] Carl Brezovec, Gerard Cornu´ejols, and Fred Glover. Two algorithms for weighted matroid intersection. Mathematical Programming, 36(1):39–53, 1986.
- [15] S´ebastien Bubeck, Yin Tat Lee, and Mohit Singh. A geometric alternative to nesterov’s accelerated gradient descent. arXiv preprint arXiv:1506.08187, 2015.
- [16] Yang Cai, Constantinos Daskalakis, and S Matthew Weinberg. Optimal multi-dimensional mechanism design: Reducing revenue to welfare maximization. In Foundations of Computer Science (FOCS), 2012 IEEE 53rd Annual Symposium on, pages 130–139. IEEE, 2012.
- [17] Yang Cai, Constantinos Daskalakis, and S Matthew Weinberg. Reducing revenue to welfare maximization: Approximation algorithms and other generalizations. In Proceedings of the Twenty-Fourth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 578–595. SIAM, 2013.
- [18] Nam-Kee Chung and Dong-Wan Tcha. A dual algorithm for submodular ﬂow problems. Operations research letters, 10(8):489–495, 1991.


- [19] Michael B. Cohen, Yin Tat Lee, Cameron Musco, Christopher Musco, Richard Peng, and Aaron Sidford. Uniform sampling for matrix approximation. CoRR, abs/1408.5099, 2014.
- [20] William H Cunningham. On submodular function minimization. Combinatorica, 5(3):185– 192, 1985.
- [21] William H Cunningham. Improved bounds for matroid partition and intersection algorithms. SIAM Journal on Computing, 15(4):948–957, 1986.
- [22] William H Cunningham and Andr´s Frank. A primal-dual algorithm for submodular ﬂows. Mathematics of Operations Research, 10(2):251–262, 1985.
- [23] Constantinos Daskalakis and S Matthew Weinberg. Bayesian truthful mechanisms for job scheduling from bi-criterion approximation algorithms. In Proceedings of the Twenty-Sixth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 1934–1952. SIAM, 2015.
- [24] James Demmel, Ioana Dumitriu, Olga Holtz, and Robert Kleinberg. Fast matrix multiplication is stable. Numerische Mathematik, 106(2):199–224, 2007.
- [25] EA Dinic. An algorithm for the solution of the max-ﬂow problem with the polynomial estimation. Doklady Akademii Nauk SSSR, 194(4):1277–1280, 1970.
- [26] Jack Edmonds. Matroid partition. Mathematics of the Decision Sciences, 11:335–345, 1968.
- [27] Jack Edmonds. Submodular functions, matroids, and certain polyhedra. Edited by G. Goos, J. Hartmanis, and J. van Leeuwen, page 11, 1970.
- [28] Jack Edmonds. Matroid intersection. Annals of discrete Mathematics, 4:39–49, 1979.
- [29] Jack Edmonds and Rick Giles. A min-max relation for submodular functions on graphs. Studies in Integer Programming (PL Hammer, EL Johnson and BH Korte, eds.), Ann. Discrete Math, 1:185–204, 1977.
- [30] Lisa Fleischer and Satoru Iwata. Improved algorithms for submodular function minimization and submodular ﬂow. In Proceedings of the thirty-second annual ACM symposium on Theory of computing, pages 107–116. ACM, 2000.
- [31] Lisa Fleischer and Satoru Iwata. A push-relabel framework for submodular function minimization and applications to parametric optimization. Discrete Applied Mathematics, 131(2):311– 322, 2003.
- [32] Lisa Fleischer, Satoru Iwata, and S Thomas McCormick. A faster capacity scaling algorithm for minimum cost submodular ﬂow. Mathematical Programming, 92(1):119–139, 2002.
- [33] Andr´s Frank. A weighted matroid intersection algorithm. Journal of Algorithms, 2(4):328– 336, 1981.
- [34] Andr´s Frank and Eva´ Tardos. An application of simultaneous diophantine approximation in combinatorial optimization. Combinatorica, 7(1):49–65, 1987.
- [35] S. Fujishige. Algorithms for solving the independent-ﬂow problems. Journal of the Operations Research Society of Japan, 1978.


- [36] Satoru Fujishige. An out-of-kilter method for submodular ﬂows. Discrete applied mathematics, 17(1):3–16, 1987.
- [37] Satoru Fujishige and Satoru Iwata. Algorithms for submodular ﬂows. IEICE TRANSACTIONS on Information and Systems, 83(3):322–329, 2000.
- [38] Satoru Fujishige, Hans R¨ock, and Uwe Zimmermann. A strongly polynomial algorithm for minimum cost submodular ﬂow problems. Mathematics of Operations Research, 14(1):60–69, 1989.
- [39] Satoru Fujishige and Zhang Xiaodong. An eﬃcient cost scaling algorithm for the independent assignment problem. Journal of the Operations Research Society of Japan, 38(1):124–136, 1995.
- [40] Mituhiro Fukuda, Masakazu Kojima, Kazuo Murota, and Kazuhide Nakata. Exploiting sparsity in semideﬁnite programming via matrix completion i: General framework. SIAM Journal on Optimization, 11(3):647–674, 2001.
- [41] Fran¸cois Le Gall. Powers of tensors and fast matrix multiplication. arXiv preprint arXiv:1401.7714, 2014.
- [42] J-L Goﬃn, Jacek Gondzio, Robert Sarkissian, and J-P Vial. Solving nonlinear multicommodity ﬂow problems by the analytic center cutting plane method. Mathematical Programming, 76(1):131–154, 1997.
- [43] Jean-Louis Goﬃn, Zhi-Quan Luo, and Yinyu Ye. Complexity analysis of an interior cutting plane method for convex feasibility problems. SIAM Journal on Optimization, 6(3):638–652, 1996.
- [44] Jean-Louis Goﬃn and Jean-Philippe Vial. Shallow, deep and very deep cuts in the analytic center cutting plane method. Mathematical Programming, 84(1):89–103, 1999.
- [45] Jean-Louis Goﬃn and Jean-Philippe Vial. Convex nondiﬀerentiable optimization: A survey focused on the analytic center cutting plane method. Optimization Methods and Software, 17(5):805–867, 2002.
- [46] Andrew V Goldberg and Robert E Tarjan. A new approach to the maximum-ﬂow problem. Journal of the ACM (JACM), 35(4):921–940, 1988.
- [47] Andrew V Goldberg and Robert E Tarjan. Finding minimum-cost circulations by successive approximation. Mathematics of Operations Research, 15(3):430–466, 1990.
- [48] Jacek Gondzio, O Du Merle, Robert Sarkissian, and J-P Vial. Accpmı¨¿œxa library for convex optimization based on an analytic center cutting plane method. European Journal of Operational Research, 94(1):206–211, 1996.
- [49] Martin Gr¨tschel, L´szl´ Lov´sz, and Alexander Schrijver. The ellipsoid method and its consequences in combinatorial optimization. Combinatorica, 1(2):169–197, 1981.
- [50] Martin Gr¨tschel, L´szl´ Lov´sz, and Alexander Schrijver. Geometric algorithms and combinatorial optimization. Springer, 1988.
- [51] Christoph Helmberg and Franz Rendl. A spectral bundle method for semideﬁnite programming. SIAM Journal on Optimization, 10(3):673–696, 2000.


- [52] Satoru Iwata. A capacity scaling algorithm for convex cost submodular ﬂows. Mathematical programming, 76(2):299–308, 1997.
- [53] Satoru Iwata. A fully combinatorial algorithm for submodular function minimization. Journal of Combinatorial Theory, Series B, 84(2):203–212, 2002.
- [54] Satoru Iwata. A faster scaling algorithm for minimizing submodular functions. SIAM Journal on Computing, 32(4):833–840, 2003.
- [55] Satoru Iwata. Submodular function minimization. Mathematical Programming, 112(1):45–64, 2008.
- [56] Satoru Iwata, Lisa Fleischer, and Satoru Fujishige. A combinatorial strongly polynomial algorithm for minimizing submodular functions. Journal of the ACM (JACM), 48(4):761– 777, 2001.
- [57] Satoru Iwata, S Thomas McCormick, and Maiko Shigeno. A faster algorithm for minimum cost submodular ﬂows. In SODA, pages 167–174, 1998.
- [58] Satoru Iwata, S Thomas McCormick, and Maiko Shigeno. A strongly polynomial cut canceling algorithm for the submodular ﬂow problem. In Integer Programming and Combinatorial Optimization, pages 259–272. Springer, 1999.
- [59] Satoru Iwata, S Thomas McCormick, and Maiko Shigeno. A fast cost scaling algorithm for submodular ﬂow. Information Processing Letters, 74(3):123–128, 2000.
- [60] Satoru Iwata and James B Orlin. A simple combinatorial algorithm for submodular function minimization. In Proceedings of the twentieth Annual ACM-SIAM Symposium on Discrete Algorithms, pages 1230–1237. Society for Industrial and Applied Mathematics, 2009.
- [61] Rahul Jain and Penghui Yao. A parallel approximation algorithm for positive semideﬁnite programming. In Foundations of Computer Science (FOCS), 2011 IEEE 52nd Annual Symposium on, pages 463–471. IEEE, 2011.
- [62] Klaus Jansen. Approximate strong separation with application in fractional graph coloring and preemptive scheduling. Theoretical Computer Science, 302(1):239–256, 2003.
- [63] Ravindran Kannan and Hariharan Narayanan. Random walks on polytopes and an aﬃne interior point method for linear programming. Mathematics of Operations Research, 37(1):1– 20, 2012.
- [64] Richard M Karp and Christos H Papadimitriou. On linear characterizations of combinatorial optimization problems. SIAM Journal on Computing, 11(4):620–632, 1982.
- [65] Leonid G Khachiyan. Polynomial algorithms in linear programming. USSR Computational Mathematics and Mathematical Physics, 20(1):53–72, 1980.
- [66] LG Khachiyan, SP Tarasov, and II Erlikh. The method of inscribed ellipsoids. In Soviet Math. Dokl, volume 37, pages 226–230, 1988.
- [67] Adam R Klivans and Daniel Spielman. Randomness eﬃcient identity testing of multivariate polynomials. In Proceedings of the thirty-third annual ACM symposium on Theory of computing, pages 216–223. ACM, 2001.


- [68] Andreas Krause. http://submodularity.org/.
- [69] Kartik Krishnan and John E Mitchell. A unifying framework for several cutting plane methods for semideﬁnite programming. Optimization methods and software, 21(1):57–74, 2006.
- [70] Kartik Krishnan and John E Mitchell. Properties of a cutting plane method for semideﬁnite programming. Paciﬁc Journal of Optimization, 8(4):779–802, 2012.
- [71] Kartik Krishnan and Tam´s Terlaky. Interior point and semideﬁnite approaches in combinatorial optimization. In Graph theory and combinatorial optimization, pages 101–157. Springer, 2005.
- [72] Eugene L Lawler. Matroid intersection algorithms. Mathematical programming, 9(1):31–56, 1975.
- [73] Yin Tat Lee, Satish Rao, and Nikhil Srivastava. A new approach to computing maximum ﬂows using electrical ﬂows. In The 45th ACM Symposium on Theory of Computing (STOC), pages 755–764, 2013.
- [74] Yin Tat Lee and Aaron Sidford. Path ﬁnding ii: An\˜ o (m sqrt (n)) algorithm for the minimum cost ﬂow problem. arXiv preprint arXiv:1312.6713, 2013.
- [75] Yin Tat Lee and Aaron Sidford. Path-ﬁnding methods for linear programming : Solving linear programs in ˜(sqrt(rank)) iterations and faster algorithms for maximum ﬂow. In 55th Annual IEEE Symposium on Foundations of Computer Science, FOCS 2014, 18-21 October, 2014, Philadelphia, PA, USA, pages 424–433, 2014.
- [76] Yin Tat Lee and Aaron Sidford. Eﬃcient inverse maintenance and faster algorithms for linear programming. arXiv preprint arXiv:1503.01752, 2015.
- [77] A. Yu Levin. On an algorithm for the minimization of convex functions. Soviet Math. Doklady, 1965.
- [78] Mu Li, Gary L Miller, and Richard Peng. Iterative row sampling. 2012.
- [79] La´szl´ Lov´sz and Santosh Vempala. Simulated annealing in convex bodies and an o*(n4) volume algorithm. J. Comput. Syst. Sci., 72(2):392–417, 2006.
- [80] Michael W. Mahoney. Randomized algorithms for matrices and data. Foundations and Trends in Machine Learning, 3(2):123–224, 2011.
- [81] S McCormick. Submodular Function Minimization. 2013.
- [82] S Thomas and McCormick. Canceling most helpful total submodular cuts for submodular ﬂow. In IPCO, pages 343–353, 1993.
- [83] Renato DC Monteiro. First-and second-order methods for semideﬁnite programming. Mathematical Programming, 97(1-2):209–244, 2003.
- [84] Kazuhide Nakata, Katsuki Fujisawa, Mituhiro Fukuda, Masakazu Kojima, and Kazuo Murota. Exploiting sparsity in semideﬁnite programming via matrix completion ii: Implementation and numerical results. Mathematical Programming, 95(2):303–327, 2003.
- [85] Arkadi Nemirovski. Eﬃcient methods in convex programming. 1994.


- [86] D. B. Nemirovsky, A. S., & Yudin. Problem complexity and method eﬃciency in optimization. 1983.
- [87] Yu Nesterov. Complexity estimates of some cutting plane methods based on the analytic barrier. Mathematical Programming, 69(1-3):149–176, 1995.
- [88] Yu Nesterov and Arkadi Nemirovskiy. Self-concordant functions and polynomial-time methods in convex programming. USSR Academy of Sciences, Central Economic & Mathematic Institute, 1989.
- [89] Yu Nesterov and A Nemirovsky. Conic formulation of a convex programming problem and duality. Optimization Methods and Software, 1(2):95–115, 1992.
- [90] James B Orlin. A faster strongly polynomial time algorithm for submodular function minimization. Mathematical Programming, 118(2):237–251, 2009.
- [91] James B Orlin, John VandeVate, et al. On a” primal” matroid intersection algorithm. 1983.
- [92] Srinivasan Ramaswamy and John E Mitchell. A long step cutting plane algorithm that uses the volumetric barrier. Department of Mathematical Science, RPI, Troy, NY, 1995.
- [93] Alexander Schrijver. A combinatorial algorithm minimizing submodular functions in strongly polynomial time. Journal of Combinatorial Theory, Series B, 80(2):346–355, 2000.
- [94] Alexander Schrijver. Combinatorial optimization: polyhedra and eﬃciency, volume 24. Springer, 2003.
- [95] Jack Sherman and Winifred J Morrison. Adjustment of an inverse matrix corresponding to a change in one element of a given matrix. The Annals of Mathematical Statistics, pages 124–127, 1950.
- [96] Maiko Shigeno and Satoru Iwata. A dual approximation approach to weighted matroid intersection. Operations research letters, 18(3):153–156, 1995.
- [97] Naum Z Shor. Cut-oﬀ method with space extension in convex programming problems. Cybernetics and systems analysis, 13(1):94–96, 1977.
- [98] Maurice Sion. On general minimax theorems. Paciﬁc J. Math, 8(1):171–176, 1958.
- [99] Daniel A Spielman and Nikhil Srivastava. Graph sparsiﬁcation by eﬀective resistances. SIAM Journal on Computing, 40(6):1913–1926, 2011.
- [100] Eva´ Tardos. A strongly polynomial minimum cost circulation algorithm. Combinatorica, 5(3):247–255, 1985.
- [101] Michael J Todd. Semideﬁnite optimization. Acta Numerica 2001, 10:515–560, 2001.
- [102] Nobuaki Tomizawa and Masao Iri. Algorithm for determining rank of a triple matrix product axb with application to problem of discerning existence of unique solution in a network. ELECTRONICS & COMMUNICATIONS IN JAPAN, 57(11):50–57, 1974.
- [103] Pravin M. Vaidya. A new algorithm for minimizing convex functions over convex sets (extended abstract). In FOCS, pages 338–343, 1989.


- [104] Pravin M Vaidya. Speeding-up linear programming using fast matrix multiplication. In Foundations of Computer Science, 1989., 30th Annual Symposium on, pages 332–337. IEEE, 1989.
- [105] Pravin M Vaidya. A new algorithm for minimizing convex functions over convex sets. Mathematical Programming, 73(3):291–341, 1996.
- [106] Lieven Vandenberghe and Stephen Boyd. Semideﬁnite programming. SIAM review, 38(1):49– 95, 1996.
- [107] Jens Vygen. A note on schrijver’s submodular function minimization algorithm. Journal of Combinatorial Theory, Series B, 88(2):399–402, 2003.
- [108] S. Fujishige W. Cui. A primal algorithm for the submodular ﬂow problem with minimum mean cycle selection. Journal of the Operations Research Society of Japan, 1988.
- [109] C Wallacher and Uwe T Zimmermann. A polynomial cycle canceling algorithm for submodular ﬂows. Mathematical programming, 86(1):1–15, 1999.
- [110] Virginia Vassilevska Williams. Multiplying matrices faster than coppersmith-winograd. In Proceedings of the forty-fourth annual ACM symposium on Theory of computing, pages 887–

898. ACM, 2012.

- [111] Yinyu Ye. Complexity analysis of the analytic center cutting plane method that uses multiple cuts. Mathematical Programming, 78(1):85–104, 1996.
- [112] David B Yudin and Arkadii S Nemirovski. Evaluation of the information complexity of mathematical programming problems. Ekonomika i Matematicheskie Metody, 12:128–142, 1976.
- [113] U Zimmermann. Minimization on submodular ﬂows. Discrete Applied Mathematics, 4(4):303– 323, 1982.
- [114] Uwe Zimmermann. Negative circuits for ﬂows and submodular ﬂows. Discrete applied mathematics, 36(2):179–189, 1992.


