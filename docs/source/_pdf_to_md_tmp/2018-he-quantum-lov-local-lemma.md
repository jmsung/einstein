arXiv:1804.07055v5[cs.CC]27Sep2024

QUANTUM LOVASZ´ LOCAL LEMMA: SHEARER’S BOUND IS TIGHT

KUN HE∗, QIAN LI †, XIAOMING SUN† AND JIAPENG ZHANG ‡

A       .  e Lovasz´ Local Lemma (LLL) is a very powerful tool in combinatorics and probability theory to show the possibility of avoiding all bad events under some weakly dependent conditions. In a seminal paper, Ambainis, Kempe, and Sa ath (JACM 2012) introduced a quantum version LLL (QLLL) which shows the possibility of avoiding all “bad” Hamiltonians under some weakly dependent condition, and applied QLLL to the random k-QSAT problem. Sa ath, Morampudi, Laumann, and Moessner (PNAS 2015) extended Ambainis, Kempe, and Sa ath’s result and showed that Shearer’s bound is a suﬃcient condition for QLLL, and conjectured that Shearer’s bound is indeed the tight condition for QLLL.

In this paper, we aﬃrm this conjecture. Precisely, we prove that Shearer’s bound is tight for QLLL, i.e., the relative dimension of the smallest satisfying subspace is completely characterized by the independent set polynomial. Our result implies the tightness of Gilyen´ and Sa ath’s algorithm (FOCS 2017), and also implies that the la ice gas partition function fully characterizes quantum satisﬁability for almost all Hamiltonians with large enough qudits (Sa ath, Morampudi, Laumann and Moessner, PNAS 2015).

 e commuting LLL (CLLL), which focuses on commuting local Hamiltonians, is also investigated here. We prove that the tight regions of CLLL and QLLL are diﬀerent in general.  is result indicates that it is possible to design an algorithm for CLLL which is still eﬃcient beyond Shearer’s bound.

![image 1](<2018-he-quantum-lov-local-lemma_images/imageFile1.png>)

∗ e Key Lab of Data Engineering and Knowledge Engineering, MOE, Renmin University of China, Beijing, China. Email:hekun.threebody@foxmail.com

†Institute of Computing Technology, Chinese Academy of Sciences. University of Chinese Academy of Sciences. Beijing, China. Email:liqian,sunxiaoming@ict.ac.cn

‡University of Southern California. Email:jiapengz@usc.edu

1. I            Classical Lovasz´ Local Lemma  e Lovasz´ Local Lemma (or LLL) is a very powerful tool in combinatorics and probability theory to show the possibility of avoiding all “bad” events under some “weakly dependent” condition. Formally, given a set = { 1, · · · ,  } of bad events in a probability space, the LLL is a condition on the probabilities of and the dependency among under which P(∩ ∈ ) > 0.  e dependency among events is characterized by an undirected graph, called dependency graph. Precisely, a dependency graph is an undirected graph = ([ ],   ) such that for any vertex , is independent of { : ∉ Γ ∪ { }}, where Γ stands for the set of neighbors of in . In this se ing, ﬁnding the conditions under which P(∩ ∈ ) > 0 is reduced to the following problem: given a graph

![image 2](<2018-he-quantum-lov-local-lemma_images/imageFile2.png>)

![image 3](<2018-he-quantum-lov-local-lemma_images/imageFile3.png>)

![image 4](<2018-he-quantum-lov-local-lemma_images/imageFile4.png>)

, determine its abstract interior I( ) which is the set of vectors such that P ∩ ∈ > 0 for any event set with dependency graph and probability vector . Local solutions to this problem, including the ﬁrst LLL proved in 1975 by Erdos˝ and Lovasz´ [9], are referred as abstract LLLs.

 e most frequently used abstract LLL is as follows:

-  eorem 1.1 ([33]). Given a dependency graph = ([ ],   ) and a probability vector ∈ [0, 1] ,

if there exist real numbers 1, ...,  ∈ (0, 1) such that ≤ ∈Γ (1 − ) for any ∈ [ ], then ∈ I( ). Shearer [32] provided the exact characterization of I( ) with the independence polynomial de-

ﬁned as follows.

- Deﬁnition 1.1 (Multivariate independence polynomial). Let = ([ ],   ), = ( : ∈ [ ]), and Ind( ) be the set of all independent sets of . For each vertex set ⊆ [ ], deﬁne

( , , )

⊆ : ∈Ind( )

(−1)| |

∈

.

We call ( , ) ( , , [ ]) the multivariate independence polynomial of .

- Deﬁnition 1.2 (Shearer’s bound). Given a dependency graph = ([ ],   ), a probability vector


= ( 1, · · · ,  ) ∈ [0, 1] is called beyond the Shearer’s bound of if there exists a vertex set ⊆ [ ] such that ( , , ) ≤ 0. Otherwise we say is in the Shearer’s bound of .

 e tight criterion under which the abstract LLL holds provided by Shearer is as follows. Given any set of events = { 1, · · · ,  }, we use ∼ ( , ( 1, · · · ,  )) to denote that has as dependency graph and satisﬁes P( ) = for any ∈ [ ].

-  eorem 1.2([32]). Foradependency graph = ([ ],   ) and aprobability vector = ( 1, · · · ,  ) ∈ [0, 1] , the following conditions are equivalent:


- (1) is in the Shearer’s bound of .
- (2) for any probability space Ω, and any event set = { ⊆ Ω : ∈ [ ]} where ∼ ( , ), we have P(∩ ∈ ) ≥ ( , ) > 0.


![image 5](<2018-he-quantum-lov-local-lemma_images/imageFile5.png>)

In addition, let = ( , ) if ∈ I( ) and be = 0 otherwise.  en there exists a set of events ∼ ( , ) such that P(∩ ∈ ) = . In other words, ∈ I( ) if and only if is in the Shearer’s bound of .

![image 6](<2018-he-quantum-lov-local-lemma_images/imageFile6.png>)

Variable version Lovasz´ Local Lemma (or VLLL), which focuses on variable-generated events, is another important version of LLL. In this version, there is a set of mutually independent random variables X = { 1, · · · ,  }, and each event can be fully determined by some subset X ⊆ X of variables. An event-variable graph is a bipartite graph = ([ ], [ ],   ) such that for any ∈ X , there is an edge ( , ) ∈ [ ] × [ ]. Similar to the abstract-LLL, the VLLL is for solving the following problem: given a bipartite graph , determine its variable interior VI( ) which is the set of vectors such that P ∩ ∈ > 0 for any variable-generated event system with event-variable graph and probability vector .

![image 7](<2018-he-quantum-lov-local-lemma_images/imageFile7.png>)

 e VLLL is important because many problems in which LLL has applications naturally conform with the variable se ing, including hypergraph coloring [22], satisﬁability [11, 10], counting solutions

to CNF formulas [23], acyclic edge coloring [13]. Moreover, a major line of research on constructive LLLs is based on the variable model [25, 27, 19, 16].

A key problem around the VLLL is whether Shearer’s bound is tight for VLLL [19]. Precisely, given a bipartite graph = ( , , ), its base graph is deﬁned as the graph ( ) = ( , ′) such that for any two nodes ,  ∈ , there is an edge ( ,  ) ∈ ′ if and only if and share some common neighbor in . Observe that ( ) is a dependency graph of the variable-generated event system with event-variable graph .  us we have I( ( )) ⊆ VI( ). If I( ( )) ≠ VI( ), we say that Shearer’s bound is not tight for , or has a gap.  e ﬁrst example of gap existence is a bipartite graph whose base graph is a cycle of length 4 [19].  en, He et al. [15] showed that Shearer’s bound is generally not tight for VLLL. More precisely, Shearer’s bound is tight if the base graph ( ) is a tree, while not tight if ( ) has an induced cycle of length at least 4.  e remaining case when

( ) has only 3-cliques is partially solved.

 antum Satisﬁability and  antum Lovasz Local Lemma Most systems of physical interest can be described by local Hamiltonians = where each -local term acts nontrivially on at most qudits. We say is frustration free if the ground state of is also the ground state of every . Let Π be the projection operator on the excited states of and Π = Π , then it is easy to see that the frustration freeness of and Π are the same. Henceforth, we only care about the Hamiltonians that are projectors. Determining whether a given Π is frustration free (or satisﬁable, in computer science language), known as the quantum satisﬁability problem, is a central pillar in quantum complexity theory, and has many applications in quantum many-body physics.

Unfortunately, the quantum satisﬁability problem has been shown to be QMA1-complete [4], which is widely believed to be intractable in general even for quantum computing.  is makes it highly desirable to search for eﬃcient heuristics and algorithms in order to, at least, partially answer this question.

In a seminal paper, by generalizing the notations of probability and independence as described in the following table, Ambainis, Kempe, and Sa ath [3] introduced a quantum version LLL (or QLLL), which is a suﬃcient condition on the relative dimensions and the dependency graph under which the Hamiltonian is guaranteed to be frustration free. Here, the relative dimension of a Hamiltonian is deﬁned as that of the subspace it projects. Utilizing the QLLL, they [3] greatly improved the known critical density for random -QSAT from Ω(1) [20] to Ω(2 / 2), almost meeting the best known upper bound of (2 ) [20].

Probability space Ω → Vector space Event → Subspace ⊆ Complement = Ω\ → Orthogonal completementary subspace ⊥ Probability P( ) → Relative dimension R( ) := dimdim(( ) ) Disjunction ∨ → + = { + | ∈  ,  ∈ } Conjunction ∧ → ∩ Independence P( ∧ ) = ( ) · ( ) → R( ∩ ) = R( ) · R( ) Conditioning P( | ) = P(P( ∧ ) ) → R( | ) := RR( ( ∩ ) )

![image 8](<2018-he-quantum-lov-local-lemma_images/imageFile8.png>)

![image 9](<2018-he-quantum-lov-local-lemma_images/imageFile9.png>)

![image 10](<2018-he-quantum-lov-local-lemma_images/imageFile10.png>)

![image 11](<2018-he-quantum-lov-local-lemma_images/imageFile11.png>)

 en, Sa ath et al. [29] leveraged Shearer’s technique to the QLLL and showed that Shearer’s bound is still a suﬃcient condition for QLLL. Here, the interaction bipartite graph, which is the quantum analog of the classical event-variable graph, is used to characterize the dependency between Hamiltonians and qudits. In an interaction bipartite graph, the le  vertices represent Hamiltonians, the right vertices represent qudits, and an edge between a le  vertex and a right vertex means the corresponding Hamiltonian acts on the corresponding qudit. Remarkably, the probability threshold of Shearer’s bound turns out to be the ﬁrst negative fugacity of the hardcore la ice gas partition function, which has been extensively studied in classical statistical mechanics. Utilizing tools in classical statistical mechanics, they concretely apply QLLL to evaluate the critical threshold for various regular la ices. In contrast to

the classical VLLL [15] which generally goes beyond Shearer’s bound, Sa ath et al. [29] conjectured that Shearer’s bound is tight for QLLL, which, if true, would have important physical signiﬁcance and several striking consequences [29].

In the past few years, as a special case of the quantum satisﬁability problem, the commuting local Hamiltonian problem (CLH), where [Π , Π ] = 0 for all and , has a racted considerable a ention [6, 1, 30, 14, 2]. Commuting Hamiltonians are somewhat “halfway” between classical and quantum, and are capable of exhibiting intriguing multi-particle entanglement phenomena, such as the well-known toric code [18]. CLH interests people not only because the commutation restriction is natural and o en made in physics, but also because it may help us to understand the centrality of non-commutation in quantum mechanics. CLH can be viewed as a generalization of the classical SAT, thus CLH is at least NP-hard, and as a suﬃcient condition, the commuting version LLL (or CLLL) is desirable and would have various applications.

 e QLLL and CLLL provide suﬃcient conditions for frustration freeness. A natural question is whether there is an eﬃcient way to prepare a frustration-free state under the condition of QLLL or CLLL. A series of results showed that the answer is aﬃrmative if all local Hamiltonians commute [31, 8, 28]. Recently, Gilyen´ and Sa ath [12] improved the previous constructive results by designing an algorithm that works eﬃciently under Shearer’s bound for non-commuting terms as well under the condition that the Hamiltonian has a uniform inverse polynomial gap. Here, a uniform gap is the minimum energy gap among the system and all its subsystems [12].

 erefore, the following two closely related problems beg answers:

- (1) Tight region for QLLL: complete characterization of the interior of QLLL, QI( ), for a given interaction bipartite graph . Here the interior QI( ) is the set of vectors such that any local Hamiltonians with relative dimensions and interaction bipartite graph are frustration free. As Shearer’s bound has been shown to be a suﬃcient condition for QLLL [29], a fundamental open question here is whether Shearer’s bound is tight. If it is tight, there are several striking consequences. First, the tightness implies that Gilyen´ and Sa ath’s algorithm [12] converges up to the tight region assuming a uniform inverse-polynomial spectral gap of the Hamiltonian. Second, the geometrization theorem [21] says that given the interaction bipartite graph, dimensions of qudits, and dimensions of local Hamiltonians, either all such Hamiltonian are frustration free, or almost all such Hamiltonians are not. If Shearer’s bound turns out to be tight for the QLLL, by geometrization theorem we know that the quantum satisﬁability for almost all Hamiltonians with large enough qudits can be completely characterized by the la ice gas partition function.  e la ice gas critical exponents can be directly applied to count of the ground state entropy of almost all quantum Hamiltonians in the frustration free regime.  us, the tightness means a lot for transferring insights from classical statistical mechanics into the quantum complexity domain [29].
- (2) Tight region for CLLL: complete characterization of the interior of CLLL, CI( ), for a given interaction bipartite graph . Here the interior CI( ) is the set of vectors such that any commuting Hamiltonians with relative dimensions and interaction bipartite graph are frustration free. Obviously, the interior of the CLLL is a superset of that of the QLLL for any . An interesting question that remains is whether the containment is proper.  ere are a series of results on the algorithms for preparing a frustration-free state for commuting Hamiltonians under the conditions of QLLL [31, 8, 28].  us if the containment turns out to be proper, it might be possible to design a more specialized algorithm for commuting Hamiltonians that is still eﬃcient beyond the conditions of QLLL, e.g., Shearer’s bound.  e tight region for CLLL requires characterization not only due to the various applications in CLH, but also because it may help us to understand the role of non-commutation in the quantum world.


1.1. Results and Discussion. We provide a complete answer to the ﬁrst problem. Speciﬁcally, we show that Shearer’s bound is tight for QLLL. We also study CLLL and partially answer the second problem. Precisely, we show that in contrast to QLLL, the interior of CLLL goes beyond Shearer’s bound generally.  e main results are listed and discussed as follows.

In this work, the interaction bipartite graph of Hamiltonians and the classical event-variable graph are both denoted by the bipartite graph = ([ ], [ ],   ). We call the vertices in [ ] the le  vertices and those in [ ] the right vertices. Usually, we will index the le  vertices with “ ” and the right vertices with “ ”. In , there may be two vertices with the same index : one is a le  vertex and the other is a right vertex. In this paper, there will never be ambiguity in identifying which vertex is which from the context.

- 1.1.1. Tight Region for QLLL. In this paper, we ﬁrst prove the tightness of Shearer’s bound for QLLL, which aﬃrms the conjecture in [29, 24]. Precisely,

 eorem 1.3 (Informal). Given an interaction bipartite graph = ([ ], [ ],   ) and a rational vector

∈ [0, 1] , consider the Hamiltonians Π = Π with relative dimensions and interaction bipartite graph .

- • If ∈ I( ( )), then R(ker Π) ≥ ( ( ), ) > 0 [29] for all such Hamiltonians. For qudits of proper dimensions, this lower bound can be achieved by almost all such Hamiltonians acting on

these qudits. Moreover, there exists a 0 such that for all qudits with dimensions ≥ 0, we have R(ker Π) ≤ ( ( ), ) + for almost all such Hamiltonians, where > 0 can be arbitrarily small as 0 goes to inﬁnity.

- • Otherwise, for qudits of proper dimensions, almost all such Hamiltonians acting on these qudits are not frustration free. Furthermore, there exists a 0 such that for all qudits with dimensions


≥ 0, we have R(ker Π) ≤ for almost all such Hamiltonians, where > 0 can be arbitrarily small as 0 goes to inﬁnity.

In contrast to the classical VLLL which goes beyond Shearer’s bound generally, QLLL is another example of the diﬀerence between the classical world and the quantum world. As mentioned above,  eorem 1.3 means that the position of the ﬁrst negative fugacity zero of the la ice gas partition function is exactlythe criticalthreshold of quantum satisﬁabilityfor almost all Hamiltonians with large enough qudits, and the relative dimension of the smallest satisfying subspace is exactly characterized by the independent set polynomial. Additionally,  eorem 1.3 also implies the tightness of Gilyen´ and Sa ath’s algorithm [12], which eﬃciently prepares a frustration free state in the Shearer’s bound assuming a uniform inverse polynomial spectral gap.

Independently, Siddhardh Morampudi and Chris Laumann showed that Shearer’s bound is tight for a large class of graphs [24]. Our result shows that Shearer’s bound is tight for any graph.

Finally, the 0 that we obtain is tremendously large (see the formal statement of  eorem 1.3 in Section 3). We are curious about how small 0 can be, and particularly whether 0 can be polynomially bounded by the vector .  is open problem is important especially for the computational aspects of QLLL.

It seems [5, 20, 3, 29] that QLLL has three ranges: for suﬃciently small relative dimensions, there is a classical (unentangled) satisfying state, and when the relative dimensions of Hamiltonians increase the states need to become entangled in order to satisfy all Hamiltonians, just before the system becomes unsatisﬁable. As only two ranges are studied in  eorem 1.3, namely the satisﬁable region and the unsatisﬁable region, it is another important open problem to investigate when the satisfying state must be entangled.

- 1.1.2. Tight Region for CLLL. We partially depict the interior of CLLL. Precisely, we obtain the following results.


Solitary qudits are classical. Given , we call a right vertex ∈ [ ] solitary if for any 1, 2 ∈ N ( ) we have N ( 1) ∩ N ( 2) = { }. Here, N ( ) stands for the set of neighbors of in . We prove that all qudits H where is solitary can be restricted to be classical variables without changing the interior ( eorem 4.2). As a corollary, if all right vertices in are solitary, then the interior of CLLL equals to that of VLLL. In particular, when is a cycle of length at least 6, we have the tight region of CLLL goes beyond Shearer’s bound, as that of VLLL does [15].

![image 12](<2018-he-quantum-lov-local-lemma_images/imageFile12.png>)

Leveraging tools for VLLL to CLLL. We leverage two tools developed in [15] for deciding whether Shearer’s bound is tight for VLLL on a given to CLLL.  e ﬁrst tool, namely  eorem 4.6, enables

![image 13](<2018-he-quantum-lov-local-lemma_images/imageFile13.png>)

us to prove Shearer’s bound is tight for CLLL on a given just by constructing a commuting local Hamiltonians and without computing the interior of CLLL or the Shearer’s bound.  e second tool is a set of reduction rules with which we can infer whether Shearer’s bound is tight for CLLL on a given interaction bipartite graph from known graphs.

An almost complete characterization of graphs on which Shearer’s bound is tight for CLLL. Based on the above results, we prove that Shearer’s bound is not tight for CLLL on many interaction bipartite graphs. Precisely, given an interaction bipartite graph , we show that Shearer’s bound is tight for CLLL if its base graph is a tree, and not tight if its base graph has an induced cycle of length at least 4.  is gives an almost complete characterization of bipartite graphs on which Shearer’s bound is tight for CLLL except when the base graph has only 3-cliques.

![image 14](<2018-he-quantum-lov-local-lemma_images/imageFile14.png>)

Organization. Section 2 provides some basic notations. In Section 3, we prove that Shearer’s bound is tight for QLLL. In Section 4, we investigate the tight region of CLLL.

2. N         H           ,

Let H1, H2, · · · , H be qudits.  en the Hilbert space of the quantum system is an th-order tensor product H1⊗H2⊗· · ·⊗H over C. For any ⊆ [ ], let H ∈ H denote the Hilbert space of the qudits in . For example, H{1,2} = H1 ⊗ H2. For simplicity, we assume that H∅ satisﬁes H∅ ⊗ H = H for each Hilbert Space H. For any ∈ [ ], let dim(H ) be the dimension of H and dim(H1, · · · , H ) be (dim(H1), dim(H2), · · · , dim(H )).

In this paper, the terms “subspaces”, “Hamiltonians”, and “projectors” will be used interchangeably. We will use  , ,  to denote subspaces. A vector space is said to be direct sum of its subspaces

1, . . .,  , denoted as = 1 ⊕ 2 ⊕ · · · ⊕ , if = 1 + 2 + · · · + and ∩ ℓ≠ ℓ = {0} for any 1 ≤ ≤ . Given a Hilbert space H and a subspace ⊆ H, let Π be the projector onto .  e relative dimension of to H is deﬁned as

dim( ) dim(H)

tr(Π ) dim(H)

R( , H)

.

=

![image 15](<2018-he-quantum-lov-local-lemma_images/imageFile15.png>)

![image 16](<2018-he-quantum-lov-local-lemma_images/imageFile16.png>)

For simplicity, we will omit “to H” and denote R( , H) as use R( ) if H is clear from the context.  roughout this paper, we are only interested in ﬁnite-dimensional quantum systems and restrict our a ention to rational relative dimensions.

Given a bipartite graph = ([ ], [ ],   ), let N ( , ) (or N ( ) if is implicit) denote the neighbors of vertex in if which side this vertex belongs to is clear from the context. We say two le  vertices 1, 2 ∈ [ ] are neighboring or adjacent if N ( 1) ∩ N ( 2) ≠ ∅. We say a le  vertex

∈ [ ] and a right vertex ∈ [ ] are neighboring or adjacent if ∈ N ( ). Given a set , let N ( ) denote ∈ N ( ). We say a set of local Hamiltonians = { 1, · · · ,  } conforms with , denoted by ∼ , if for any ∈ [ ], Π acts trivially on the qudits H[ ]\N( ).  us, we can write as

∗ ⊗ H[ ]\N( ) where ∗ is some subspace of HN( ). Similarly, we can also deﬁne a set of events conforms with , denoted by ∼ . In this paper, we usually call the interaction graph.

GivenH1, H2, · · · , H andasetofsubspaces = { 1, · · · ,  } inH[ ], wewilluse R( ) torepresent the vector (R( 1), · · · , R( )) and use dim( ) to represent the vector (dim( 1), · · · , dim( )). We say a set of subspaces is frustration free if 1, · · · ,  do not span H[ ]. We will use boldface type for vectors. For example, stands for a set of subspaces, stands for a relative dimension vector, stands for a probability vector and stands for a dimension vector. For any two vectors of numbers

= ( 1, 2, · · · ,  ) and ′ = ( ′1, ′2, · · · , ′ ) of the same length, we say ≥ ′ if ≥ ′ holds for each ∈ [ ]. We say > ′ if ≥ ′ and > ′ holds for some ∈ [ ].

Now we can deﬁne the instances and the random instance of some given , and .

- Deﬁnition 2.1 (Instance and random instance). Given an interaction graph = ([ ], [ ],   ), a rational vector = ( 1, · · · ,  ) ∈ [0, 1] and an integer vector = ( 1, · · · ,  ), we say a subspace set of H[ ] is an instance of the se ing ( , , ), denoted as ∼ ( , , ), if ∼ , R( , H[ ]) = and dim(H1, · · · , H ) = . When we talk about the instances of the se ing ( , , ), we always assume that the Hilbert space H[ ] with the dimension vector can admit an instance with the interaction


graph = ([ ], [ ],   ) and the relative dimension vector , i.e., each where ∈ [ ] satisﬁes that dim(HN( )) is an integer.

We say a subspace set = ( 1, · · · ,  ) of H[ ] is a random instance of the se ing ( , , ) if ∼ ( , , ) and = ∗ ⊗ H[ ]\N( ) for each le  vertex , where ∗ is a random subspace of HN( )

according to the Haar measure with R( ∗ , HN( )) = (in particular, ∗ = HN( ) if = 1). Given a random instance ∼ ( , , ) in H[ ], we say spans the whole space if P[R( ∈  , H[ ]) = 1] = 1.

3. QLLL: S      ’  B     I  T    

 is section aims at proving Theorem 1.3. Section 3.1 presents our main results,  eorems 3.2 and 1.3, and illustrate the main idea of our proof. We prove Theorem 3.2 by induction on the number of le  vertices in the interaction graph.  e induced interaction graph, the induced relative dimensions, the induced dimensions of qudits and the induced subspaces are deﬁned in Sections 3.2, 3.3 and 3.4, respectively. In Section 3.5, we construct the subspaces in Theorem 3.2 from the induced subspaces. Finally,  eorems 3.2 and 1.3 are proved in sections 3.6 and 3.7, respectively.

- 3.1. Shearer’s Bound Is Tight for QLLL. In this subsection we show that Shearer’s bound is tight for QLLL. Given an interaction graph , the base graph of is deﬁned as ( ) = ([ ],   ),


where ( 1, 2) ∈ if and only if the le  vertices 1, 2 are neighbors in . For simplicity, we will use to denote ( ) if there is no ambiguity. For example, we let I( ) = I( ( )), and Ind( ( )) = Ind( ). In addition, for any interaction graph = ([ ], [ ],   ) and ∈ (0, 1]

and ⊆ [ ], we let ( , , ) = ( ( ), , ) and ( , ) = ( ( ), ). If and are clear from the context, we will simply denote ( , , ) as ( ). It has been proved that Shearer’s bound is a lower bound on the relative dimension of the satisfying subspace [29], more precisely,

 eorem 3.1(Restateof  eorem1in [29]). Given an interaction graph = ([ ], [ ],   ) and rational

= ( 1, · · · ,  ) ∈ (0, 1] , if ∈ I( ), then for any subspaces ( 1, · · · ,  ) of relative dimension , 1 − R( =1 ) ≥ ([ ]).

In addition to Theorem 3.1, we further show that Shearer’s bound can be achieved on the qudits with proper dimensions.

-  eorem 3.2. Given = ([ ], [ ],   ) and rational = ( 1, · · · ,  ) ∈ (0, 1] , assume that for each le  vertex ∈ [ ], we have = where ,  are mutually prime and if N ( ) = ∅ then = 1. Let


![image 17](<2018-he-quantum-lov-local-lemma_images/imageFile17.png>)

= ∈[ ] .  en

- (a) if ∉ I( ), then there exists some = ( 1, · · · ,  ) such that ≤ 4 for each ∈ [ ] and P[R( ∈ ) = 1] = 1 for the random instance of the se ing ( , , ).
- (b) otherwise, ∈ I( ), then there exists some = ( 1, · · · ,  ) such that ≤ 8+4 for each ∈ [ ] and P[R( ∈ ) = 1 − ([ ])] = 1 for the random instance of the se ing ( , , ).


Remark.  e interaction graph = ([ ], [ ],   ) in above theorem can be disconnected. Furthermore, for any le  or right vertex in , N ( ) can be ∅.  is is for the sake of convenience of the induction argument.  e dimensions of qudits in  eorem 3.2 is not optimised, but we do not expect to be able to use the current techniques to improve it substantially. Our main point is that Shearer’s bound can be achieved on some qudits.

 e following theorem further extends Theorem 3.2 to all large enough qudits.

 eorem 1.3 (Restated). Given an interaction graph = ([ ], [ ],   ) and a rational ∈ (0, 1] , for any ∈ (0, 1] and any integers ≥ · 1+8 4 , · · · ,  · 1+8 4 where = 2 +1 , the random instance of the se ing ( , , ) satisﬁes that

![image 18](<2018-he-quantum-lov-local-lemma_images/imageFile18.png>)

- (a) if ∉ I( ), then


P R

∈

∈ [1 −  , 1] = 1;

- (b) otherwise,


P R

∈

∈ [1 − ([ ]) −  , 1 − ([ ])] = 1.

 e core in the above two theorems is Theorem 3.2 (a). In the following, we illustrate the main idea of its proof. A key tool in our proof is the geometrization theorem established by Laumann et al. [21], which shows that “almost all” is equivalent to “existence”.

-  eorem 3.3 ( e geometrization theorem, adapted from [21]). Given any interaction graph = ([ ], [ ],   ), any dimension vector , and any relative dimension vector ∈ [0, 1] , if there exists an instance of the se ing ( , , ) satisfying R( ∈ ) = 1, then for the random instance of the se ing ( , , ), we have P[R( ∈ ) = 1] = 1.


 e following lemma is used in the proof of Theorem 3.2. Given positive integers 1, · · · ,  and an instance of the se ing ( , , ) spanning the whole space, one can construct an instance of the se ing ( , , ( 1 1, · · · ,  )) spanning the whole space by combining ∈[ ] instances of the se ing ( , , ).

- Lemma 3.1. Given any , , = ( 1, · · · ,  ) and any positive integers 1, · · · ,  ,

- (a) if there exists an instance of the se ing ( , , ) spanning the whole space, then there exists some instance of the se ing ( , , ( 1 1, · · · ,  )) spanning the whole space as well;
- (b) if the random instance the se ing ( , , ) spans the whole space, then the random instance of the se ing ( , , ( 1 1, · · · ,  )) spans the whole space as well.


Now we prove Lemma 3.1.

Proof. We only prove (a) here, then (b) is immmediate by Theorem 3.3. Let H[ ] = ∈[ ] H be a Hilbert space where dim(H ) = for each ∈ [ ]. We decompose the qudit H to orthogonal

subspaces H = ℓ∈[ ] Hℓ where dim(Hℓ ) = for each ∈ [ ], ℓ ∈ [ ].  us for each ℓ = (ℓ1, ℓ2, · · · , ℓ ) where ℓ ∈ [ ] for all ∈ [ ], we have (H1ℓ1, · · · , Hℓ ) are of dimensions , and then can be spanned by some subspace set ℓ ∼ with relative dimensions with respect with (H1ℓ1, · · · , Hℓ ). Let

=

ℓ∈[ 1]×···×[ ]

ℓ.

It is easy to verify that is an instance of the se ing ( , , ( 1 1, · · · ,  ))) and spans H[ ]. Combining Deﬁnition 1.2 with Theorem 1.2, we have the following lemma.

- Lemma 3.2. For each = ([ ], [ ],   ) and = ( 1, · · · ,  ) ∈ (0, 1] , the following are equivalent:


(1) is in Shearer’s bound for ( ); (2) ( , , ) > 0 for each ⊆ [ ]; (3) ∈ I( ).

With Lemmas 3.1, 3.2 and Theorem 3.3, our main idea can be illustrated with following example. Example. Let = ([4], [4],  ) where = {( , ), ( ,  + 1 (mod 4)),  ∈ [4]} as in Figure 1 (A). Let

( 1, 2, 3, 4) = (13, 31, 41, 14). Notethat ( ) is a cycle of length 4, henceby Deﬁnition1.1 we have

![image 19](<2018-he-quantum-lov-local-lemma_images/imageFile19.png>)

![image 20](<2018-he-quantum-lov-local-lemma_images/imageFile20.png>)

![image 21](<2018-he-quantum-lov-local-lemma_images/imageFile21.png>)

![image 22](<2018-he-quantum-lov-local-lemma_images/imageFile22.png>)

( , ) = 1− 4 =1 + 1 · 3 + 2 · 4 = 0.  en one can verify that ∉ I( ) by Lemma 3.2. Moreover, one can verify that for the given and , the parameter in Theorem 3.2 is 3 × 3 × 4 × 4 = 144.

 e proof of Theorem 3.2 (a) is by induction on the number of le  vertices in the interaction graph. To illustrate the proof, we will verify Theorem 3.2 (a) on the given and based on the induction hypothesis that it has already been proved for each interaction graph where the number of le  vertices is no more than 3. By Theorem 3.3, it is suﬃcient to construct an instance spanning the whole space where ∼ ( , , ) for some ≤ 14444, 14444, 14444, 14444 . Our construction is as follows.

Let H1, H3, H4 be three qudits where ( 1, 3, 4) = (dim(H1), dim(H3), dim(H4)) will be determined later. Let H2 1⊕ 2 ≃ C2 where 1 and 2 are two orthogonal subspaces of C2 with dimension

1. Deﬁne random 1 ′, 2′, 3′, 4′ as follows.

- (1) 1 ′ = 1 ∗ ⊗ H{3,4} where 1 ∗ is a random subspace of H1 with R( 1 ∗, H1) = 32.


![image 23](<2018-he-quantum-lov-local-lemma_images/imageFile23.png>)

| |H1|
|---|---|
| | |


- 1

- 2

- 3

- 4 ( )


| |H2|
|---|---|
| | |


| |H3|
|---|---|
| | |


| |H4|
|---|---|
| | |


| |H1|
|---|---|
| | |


′ 1

| |H4|
|---|---|
| | |


′ 4

| |H3|
|---|---|
| | |


′ 3

( ) 1

| |H3|
|---|---|
| | |


′

- 2

′

- 3

′

- 4 ( ) 2


| |H4|
|---|---|
| | |


| |H1|
|---|---|
| | |


F      1.  e interaction graphs in the example

- (2) 2 ′ = 2 ∗ ⊗ H{1,4} where 2 ∗ is a random subspace of H3 with R( 2 ∗, H3) = 32.

![image 24](<2018-he-quantum-lov-local-lemma_images/imageFile24.png>)

- (3) 3 ′ = 3 ∗ ⊗ H1 where 3 ∗ is a random subspace of H3 ⊗ H4 with R( 3 ∗, H3 ⊗ H4) = 41.

![image 25](<2018-he-quantum-lov-local-lemma_images/imageFile25.png>)

- (4) 4 ′ = 4 ∗ ⊗ H3 where 4 ∗ is a random subspace of H4 ⊗ H1 with R( 4 ∗, H4 ⊗ H1) = 41.


![image 26](<2018-he-quantum-lov-local-lemma_images/imageFile26.png>)

Obviously, 1 ′, 2′, 3′, 4′ are subspaces in H1,3,4. Let ′ = 3 2, 41, 14 . One can verify that the interaction graph of 1 ′, 3′, 4′ is 1 as in Figure 1 (B), and R 1 ′, 3′, 4′ , H1,3,4 = ′.  us, 1 ′, 3′, 4′ is a random instance of ( 1, ′, ( 1, 3, 4)). Similarly, the interaction graph of 2 ′, 3′, 4′ is 2 as in Figure 1 (C), and R 2 ′, 3′, 4′ , H1,3,4 = ′. We also have 2 ′, 3′, 4′ is a random instance of ( 2, ′, ( 1, 3, 4)).

![image 27](<2018-he-quantum-lov-local-lemma_images/imageFile27.png>)

![image 28](<2018-he-quantum-lov-local-lemma_images/imageFile28.png>)

![image 29](<2018-he-quantum-lov-local-lemma_images/imageFile29.png>)

In addition, by Deﬁnition 1.1 we have ( 1, ′) = 1 −

- 2

![image 30](<2018-he-quantum-lov-local-lemma_images/imageFile30.png>)

- 3


1 4

1 4

- 2

![image 31](<2018-he-quantum-lov-local-lemma_images/imageFile31.png>)

- 3


1 4

−

−

+

·

= 0.

![image 32](<2018-he-quantum-lov-local-lemma_images/imageFile32.png>)

![image 33](<2018-he-quantum-lov-local-lemma_images/imageFile33.png>)

![image 34](<2018-he-quantum-lov-local-lemma_images/imageFile34.png>)

- Combining with Lemma 3.2, we have ′ ∉ I( 1).  us by the induction hypothesis, there is some ′ 1, 3′ and 4 ′ where ′ ≤ (3×4×4)43 for each ∈ {1, 3, 4} such that the random instance of the se ing

( 1, ′, ( 1 ′, 3′, 4′)) spans H1,3,4. Similarly, by Deﬁnition 1.1 we also have ( 2, ′) = 1 −

- 2

![image 35](<2018-he-quantum-lov-local-lemma_images/imageFile35.png>)

- 3


−

1 4

![image 36](<2018-he-quantum-lov-local-lemma_images/imageFile36.png>)

−

1 4

![image 37](<2018-he-quantum-lov-local-lemma_images/imageFile37.png>)

+

- 2

![image 38](<2018-he-quantum-lov-local-lemma_images/imageFile38.png>)

- 3


·

1 4

![image 39](<2018-he-quantum-lov-local-lemma_images/imageFile39.png>)

= 0.

- Combining with Lemma 3.2, we have ′ ∉ I( 2).  us by the induction hypothesis, there is some ′′ 2 , 3′′ and 4 ′′ where ′ ≤ (3 × 4 × 4)43 for each ∈ {2, 3, 4} such that the random instance of the


se ing ( 2, ′′, ( 1 ′′, 3′′, 4′′)) spans H1,3,4.

Let = ′ ′′ for each ∈ {1, 3, 4}. By ′ , ′′ ≤ (3×4×4)43 for each ∈ {1, 3, 4}, we have ≤ 14444. Recall that 1 ′, 3′, 4′ is a random instance of ( 1, ′, ( 1, 3, 4)) and the random instance of the se ing ( 1, ′, ( 1 ′, 3′, 4′)) spans H1,3,4.  us, by Lemma 3.1 (b) and = ′ ′′ for each ∈ {1, 3, 4}, we have 1 ′, 3′, 4′ spans the whole space H1,3,4 with probability 1. Similarly, one can also verify that

′ 2, 3′, 4′ spans the whole space H1,3,4 with probability 1. By the union bound and the deﬁnition of

′ 1, 2′, 3′, 4′, we have there must be some 1 ★, 2★, 3★, 4★ such that the following conditions hold:

- (1) 1 ★ is some subspace of H{1,3,4} with R( 1 ★, H{1,3,4}) = 23 which acts trivially on H{3,4}.

![image 40](<2018-he-quantum-lov-local-lemma_images/imageFile40.png>)

- (2) 2 ★ is some subspace of H{1,3,4} with R( 2 ★, H{1,3,4}) = 32 which acts trivially on H{1,4}.

![image 41](<2018-he-quantum-lov-local-lemma_images/imageFile41.png>)

- (3) 3 ★ is some subspace of H{1,3,4} with R( 3 ★, H{1,3,4}) = 41 which acts trivially on H1.

![image 42](<2018-he-quantum-lov-local-lemma_images/imageFile42.png>)

- (4) 4 ★ is some subspace of H{1,3,4} with R( 4 ★, H{1,3,4}) = 41 which acts trivially on H3.

![image 43](<2018-he-quantum-lov-local-lemma_images/imageFile43.png>)

- (5) Both 1 ★, 3★, 4★ and 2 ★, 3★, 4★ span the whole space H{1,3,4}.


Let 1 = 1 ★ ⊗ 1, 2 = 2 ★ ⊗ 2, 3 = 3 ★ ⊗ H2 and 4 = 4 ★ ⊗ H2. Let = ( 1, 2, 3, 4). One can verify that the interaction graph of is as in Figure 1 (A), and R , H[4] = 3 1, 13, 41, 41 = . In addition, we also have dim(H1, H2, H3, H4) = ( 1, 2, 3, 4) ≤ (14444, 14444, 14444, 14444). Moreover, by 1 ★, 3★, 4★ span the space H{1,3,4}, we have 1, 3, 4 span the space H{1,3,4} ⊗ 1. Similarly, by

![image 44](<2018-he-quantum-lov-local-lemma_images/imageFile44.png>)

![image 45](<2018-he-quantum-lov-local-lemma_images/imageFile45.png>)

![image 46](<2018-he-quantum-lov-local-lemma_images/imageFile46.png>)

![image 47](<2018-he-quantum-lov-local-lemma_images/imageFile47.png>)

2 , 3★, 4★ span the space H{1,3,4}, we have 2, 3, 4 span the space H{1,3,4} ⊗ 2.  us, 1, 2, 3, 4 span the whole space H[4] = H{1,3,4} ⊗ 1 ⊕ H{1,3,4} ⊗ 2. In summary, we have ∼ ( , , ) for some ≤ 14444, 14444, 14444, 14444 and spans the whole space H[4].  us, Theorem 3.2 (a) holds on the given and .

★

- 3.2. Induced interaction graph and induced relative dimensions. Our proof of Theorem 3.2 (a) is by induction on the number of le  vertices in the interaction graphs. We ﬁrst deﬁne the induced interaction graph and induced relative dimensions.


For any two sets of le  vertices  ,  ⊆ [ ] in , deﬁne | in as \ ({le  vertex : ∈ or N ( , ) ∩ N ( , ) ≠ ∅ for some ∈ }).

Intuitively, | is the set of le  vertices in which share no neighbor with the le  vertices in . For simplicity, we will omit “in ” if is clear from the context. For each ∈ [ ] and ⊆ [ ], we will also simply denote the set | { } with | .

- Deﬁnition 3.1(Inducedinteractiongraphandinducedrelativedimensions). Given = ([ ], [ ],   )


and rational = ( 1, · · · ,  ) ∈ (0, 1] where ( , , ) > 0 for each [ ] and |N ( )| ≥ 2 for the right vertex , assume w.l.o.g. N ( ) = [ ] where 2 ≤ ≤ . Also assume that for each le  vertex

∈ [ ], N ( ) ≠ ∅ and = < 1 where ,  are mutually prime. Let = ∈[ ] .

![image 48](<2018-he-quantum-lov-local-lemma_images/imageFile48.png>)

Given a le  vertex ∈ [ ], let = { } ∪ ([ ] \ [ ]). Let be the induced graph on the le  vertices in and the right vertices in [ − 1]. For each vertex , we will use N ( ) to denote the neighbor of

in and use N ( , ) to denote the neighbor of in where we specify for clarity. Similarly, we will also use ( ) to denote ( , , ) for each subset ⊆ [ ] and use ( , , ) to denote the independence polynomial of , and ⊆ where we specify and for clarity. When we use the notation | for some sets  , , we always means | in .

Let = ( ) ∈ where = for each ≠ and

· ([ ] | ℓ) ([ ] | )

= ℓ∈[ ] ℓ

- (1) , = min { , 1} . Assume = where ,  are mutually prime for each ∈ .


![image 49](<2018-he-quantum-lov-local-lemma_images/imageFile49.png>)

![image 50](<2018-he-quantum-lov-local-lemma_images/imageFile50.png>)

Remark. In above deﬁnition, by ( , , ) > 0 for each [ ], we have ,  are properly deﬁned and 0 < ≤ 1. In addition, by = for each ≠ and ∈ (0, 1], we have 0 < ≤ 1 for each ≠ .  us, = ( ) ∈ is a properly deﬁned relative dimension vector. We emphasize that if N ( ) = { } for the le  vertex , then has no neighbor in .

 e following lemma is used in the induction proof of Theorem 3.2 (a). It shows that if ([ ]) ≤ 0, then the induced interaction graph and the induced relative dimension vector also satisfy the condition in Theorem 3.2 (a).

- Lemma 3.3. Given , , , and as in Deﬁnition 3.1, assume ([ ]) ≤ 0.  en ∉ I( ). Moreover, if N ( , ) = ∅ for some le  vertex ∈ in , then = 1.

 e following lemma is used in the proof of Lemma 3.3, which is immediate by Deﬁnition 3.1 and Deﬁnition 1.1.

- Lemma 3.4. Given , , , , and as in Deﬁnition 3.1 and a le  vertex ∈ [ ], we have ( , , [ ] \ [ ]) = ([ ] \ [ ]), ( , , [ ] | ) = ([ ] | ).


 us, we also have

( ℓ ( , , [ ] | ℓ)) ( , , [ ] | )

= min ℓ∈[ ]

, 1 .

![image 51](<2018-he-quantum-lov-local-lemma_images/imageFile51.png>)

By the deﬁnition of independence polynomial, we have the following properties. Proposition 3.4. Given = ([ ], [ ],   ) and ∈ (0, 1] , we have

- (a) for each ∉ [ ], ( ∪ { }) = ( ) − · ( | ).
- (b) if N ( ) = [ ] for the right vertex , then ([ ]) = ([ ] \ [ ]) − ℓ=1 ℓ · ([ ] | ℓ).
- (c) if ( ) > 0 for each [ ], then we have ( ) ≤ 1 for each ⊆ [ ].
- (d) if ( ) > 0 for each [ ] and ([ ]) ≤ 0, then ( ) is connected.


Proof. By Deﬁnition 1.1, (a) and (b) are immediate. In the following, we prove (c) and (d).

(c). For each and where ∉ [ ], by ( ) > 0 for each [ ], we have ( | ) > 0. Combining with > 0, we have ( | ) > 0. In addition, by (a) of this proposition, we have

( ∪ { }) = ( ) − ( | ). Combining with ( | ) > 0, we have ( ∪ { }) < ( ). In other words, ( ) decreases as grows.  us, for any ⊆ [ ], we have ( ) ≤ (∅) = 1.

(d). Assume that ( ) is notconnectedfor contradiction.  en thereexists ∅ [ ] such that

and [ ]\ areseparatein ( ). Inaddition,byDeﬁnition1.1 wehave ([ ]) = ( ) ([ ]\ ) ≤ 0.  us, either ( ) ≤ 0 or ([ ] \ ) ≤ 0, a contradiction with ( ) > 0 for each [ ].

Now we can prove Lemma 3.3.

Proof of Lemma 3.3. At ﬁrst, we prove that ∉ I( ). By ∈ [ ] = N ( ) for the right vertex , we have ([ ] \ [ ]) | = [ ] | .  us,

( , ,  ) (by = { } ∪ ([ ] \ [ ])) = ( , , { } ∪ ([ ] \ [ ])) (by Proposition 3.4 (a)) = ( , , [ ]\[ ]) − ( , , ([ ] \ [ ]) | )

( ℓ ( , , [ ] | ℓ)) ( , , [ ] | )

(by (1)) = ( , , [ ]\[ ]) − ℓ∈[ ]

· ( , , ([ ] \ [ ]) | )

![image 52](<2018-he-quantum-lov-local-lemma_images/imageFile52.png>)

( ℓ ([ ] | ℓ)) ([ ] | )

(by Lemma 3.4) = ([ ]\[ ]) − ℓ∈[ ]

· (([ ] \ [ ]) | )

![image 53](<2018-he-quantum-lov-local-lemma_images/imageFile53.png>)

( ℓ ([ ] | ℓ)) ([ ] | )

(by ([ ] \ [ ]) | = [ ] | ) = ([ ]\[ ]) − ℓ∈[ ]

· ([ ] | )

![image 54](<2018-he-quantum-lov-local-lemma_images/imageFile54.png>)

( ℓ ([ ] | ℓ)) (by Proposition 3.4 (b)) = ([ ])

= ([ ]\[ ]) −

ℓ∈[ ]

≤0. Combining with Lemma 3.2, we have ∉ I( ).

In the following, we show that if N ( , ) = ∅ for some le  vertex ∈ in , then = 1. It is lossless to assume that ∈ [ ]. Because if ∈ [ ] \ [ ], we have N ( , ) = N ( , ). Combining with the assumption N ( , ) ≠ ∅ in Deﬁnition 3.1, we also have N ( , ) ≠ ∅. In the following, we assume ∈ [ ]. Combining with ∈ , we have = . In addition, if N ( , ) = ∅ for the le  vertex , we have N ( , ) = { }.  erefore, we have [ ] | = [ ] \ [ ] in .  us, we have

([ ] | ) −

ℓ∈[ ]

( ℓ ([ ] | ℓ)) = ([ ]\[ ]) −

ℓ∈[ ]

( ℓ ([ ] | ℓ)) = ([ ]) ≤ 0,

where the last equality is by Proposition 3.4 (b). Combining with (1) and  ,  > 0, we have  ,  = 1. In summary, for each le  vertex ∈ , if N ( , ) = ∅, then = 1.  e lemma is proved.

3.3. Induced dimensions of qudits. In this subsection, we deﬁne the induced dimensions of qudits. Roughly speaking, for the induced interaction graph and the induced relative dimension vector

, we pick some induced dimension vector ( ) ∈ such that the random instance of the se ing ( , , ( ) ∈ ) spans the whole space.  e existence of such ( ) ∈ is ensured by applying  eorem 3.2 (a) to and .  e dimension of qudit for and is deﬁned as the product of the induced dimension of corresponding qudit if ∈ [ − 1], and deﬁned by the independence polynomial of

, if = .

- Deﬁnition 3.2 (Dimensions and induced dimensions of qudits). Given , , , , , and as in Deﬁnition 3.1, let ( ) ∈ be some dimension vector such that given any H1, · · · , H −1 with dim(H1, · · · , H −1) = ( ) ∈ , the random subspaces in H[ −1] of the se ing ( , , ( ) ∈ ) span the whole space H[ −1]. Deﬁne ( ) ∈ as follows. If ≥ 1, let = for each ∈ . Otherwise, let ( ) ∈ be ( ) ∈ .


Deﬁne

if ∈ [ − 1]

= ∈[ ]

- (2)

Remark. We will specify ( ) ∈ for each ∈ [ ] concretely in Section 3.6.

 e following lemma shows that ( 1, · · · ,  ) is a properly deﬁned dimension vector of qudits and provides an upper bound for the dimension of . Lemma 3.5. Given 1, · · · ,  as in Deﬁnition 3.2, we have 1, · · · ,  are positive integers. In addition, we have ≤ 2 2.

 e following lemma is used in the proof of Lemma 3.5. Lemma 3.6. Given , and as in Deﬁnition 3.1, for each [ ] and ℓ ∈ [ ] we have

- (a) ℓ and ( ) are positive integers;
- (b) ℓ ([ ] | ℓ), ℓ 2 ([ ] | ℓ),  ∈ ([ ] | ) , 2 ∈ ([ ] | ) are positive integers;
- (c) for each ∈ , there exists some integer 0 < ≤ such that


( ([ ] | ))−1

∈

- (3) ([ ] | )


2

ℓ=1 ( ℓ ([ ] | ℓ)) if =  .

is a positive integer. Proof. (a). By > 0 and ℓ > 0, we have ℓ is positive. In addition, by = ∈[ ] and ℓ = ℓ

, we have

![image 55](<2018-he-quantum-lov-local-lemma_images/imageFile55.png>)

ℓ

ℓ = ℓ

∈[ ]\{ℓ}

.

 us we have ℓ is an integer by ℓ and for all ∈ [ ] are integers. In summary, ℓ is a positive integer.

For each [ ], by Deﬁnition 1.1 we have ( ) = ( )

(−1)| |

=

ℓ

∈ ℓ∈ \ ∈[ ]\

∈ ∈[ ]\

∈Ind( )∧ ⊆

is an integer. In addition, recall that ( ) > 0,  > 0 as in Deﬁnition 3.1, we have ( ) is positive.  us, ( ) is a positive integer.

(b). We only show that ℓ ([ ] | ℓ) is a positive integer for each ℓ ∈ [ ].  en it is immediate that ℓ 2 ([ ] | ℓ),  ∈ ([ ] | ) and 2 ∈ ([ ] | ) are also positive integers. Recall that ( ) > 0 for each [ ] as in Deﬁnition 3.1, we have ([ ] | ℓ) > 0. Combining with ℓ > 0 and > 0, we have ℓ ([ ] | ℓ) is positive. In addition, we also have ℓ ([ ] | ℓ) is an integer. Let

{ | ( ∈ Ind( )) ∧ ( ⊆ ([ ] | ℓ))}. By Deﬁnition 1.1, we have

ℓ ([ ] | ℓ) = ℓ

= ℓ

∈

∈

(−1)| |

∈

=

∈[ ]

· ℓ ℓ

·

![image 56](<2018-he-quantum-lov-local-lemma_images/imageFile56.png>)

(−1)| |

∈ ∈[ ]\( ∪{ℓ})

,

∈

(−1)| |

∈

![image 57](<2018-he-quantum-lov-local-lemma_images/imageFile57.png>)

where the last equality is by ℓ ∉ ([ ] | ℓ). Combining with ,  are integers for each ∈ [ ], we have ℓ ([ ] | ℓ) is an integer. In summary, we have ℓ ([ ] | ℓ) is a positive integer.

(c). Let = ([ ] | ). Combining with ( ) is a positive integer for each [ ] as shown in

- (a) of this lemma, we have is a positive integer. In addition, by (3) we have

( ([ ] | ))−1

∈

([ ] | ) =

∈

([ ] | ) .

Combining with that ([ ] | ) is a positive integer for each ∈ [ ] as shown in (b) of this lemma, we have (3) is a positive integer.

By Lemma 3.6, we have the following corollary immediately. Corollary 3.5. ∈ ≤ 2 for each ∈ [ ].

Proof. By = for each ≠ , we also have = for each ≠ . In addition, by combining (1) with Lemma 3.6 (c), we have there exists some integer 0 < ≤ ∈[ ] such that is a positive integer.  us, we have ≤ ≤ ∈[ ] = . Combining with = for each ≠ , we have

∈

≤ ·

≠

≤ ·

≠

≤ 2.

Now we can prove Lemma 3.5.

Proof of Lemma 3.5. At ﬁrst, we prove that 1, · · · ,  are positive integers. For each ∈ [ − 1], is a positive integer is immediate by ≥ 2,  ,  is a positive integer for each ∈ [ ] and (2).

In the next, we prove that is a positive integer no more than 2 . Combining (2) with Lemma 3.6

- (b), we have is a positive integer. Moreover, we have


ℓ · ([ ] | ℓ)

ℓ=1

(by Proposition 3.4 (b)) = ([ ] \ [ ]) − ([ ]) (by Proposition 3.4 (a)) = ([ ] \ [ ]) − ( ([ ]\{1}) − 1 · ([ ] | {1}))

(by ([ ]\{1}) > 0 and 1 ≤ 1) < ([ ] \ [ ]) + ([ ] | {1})

(by Proposition 3.4 (c)) ≤2.  us by (2) we have ≤ 2 2.

Given , as in Deﬁnition 3.1, for each ∈ [ ], we have 2 ([ ] | ) is a positive integer by

- Lemma 3.6 (b).  us, one can decompose a qudit with dimension into orthogonal subspaces as follows.

Deﬁnition 3.3 (Induced qudits). Given 1, · · · ,  as in Deﬁnition 3.2, Let H1, H2, · · · , H be qudits where dim(H ) = for each ∈ [ ]. Decompose H into orthogonal subspaces H1 , · · · , H arbitrarily where

(4) ∀ ∈ [ ], dim(H ) = 2 ([ ] | ). Deﬁne

- 1 {le  vertex | ( ∈ [ ]) ∧ dim(H ) < dim(H ) ∧ (N ( ) ≠ { })},
- 2 {le  vertex | ( ∈ [ ]) ∧ dim(H ) ≥ dim(H ) }.


By (2) and (4) we have dim(H ) = = ℓ=1 dim(Hℓ ).  us the decomposition in Deﬁnition 3.3 is properly deﬁned. In addition, the following lemma shows that 1, 2 form a partition of the set of le  vertices [ ].

- Lemma 3.7. 1 ∩ 2 = ∅ and 1 ∪ 2 = [ ].


Proof. 1 ∩ 2 = ∅ is immediate by their deﬁnitions. In the following, we show that 1 ∪ 2 = [ ].  en the lemma is immediate. By Proposition 3.4 (b) we have

([ ]) = ([ ] \ [ ]) −

ℓ=1

ℓ · ([ ] | ℓ).

If ([ ]) ≤ 0, we have

([ ] \ [ ]) ≤

ℓ · ([ ] | ℓ). For each le  vertex where N ( ) = { }, we have

ℓ=1

ℓ · ([ ] | ℓ).  us we have

([ ] | ) = ([ ] \ [ ]) ≤

ℓ=1

2 ([ ] | ) ≤ 2

( ℓ ([ ] | ℓ)) . Combining with (4) and (2), we have

ℓ=1

dim(H ) = 2 ([ ] | ) ≤ 2

( ℓ ([ ] | ℓ)) = = dim(H ). In summary, if N ( ) = { }, we have dim(H ) ≤ dim(H ).  us we have { ∈ [ ] | N ( ) = { }} ⊆

ℓ=1

- 2.  us, we have 2 = {le  vertex | ( ∈ [ ]) ∧ dim(H ) ≥ dim(H ) }

= {le  vertex | ( ∈ [ ]) ∧ dim(H ) ≥ dim(H ) ∨ (N ( ) = { }) }. Combining the deﬁnition of 1, we have 1 ∪ 2 = [ ].

- 3.4. Induced subspaces. In this subsection, we deﬁne the induced subspaces. Given H1, H2, · · · , H and H1 , · · · , H as in Deﬁnition 3.3, we deﬁne the induced random subspaces 1 ′, · · · , ′ and the induced subspaces 1 ★, · · · , ★ as follows.  e intuition is to let 1 ′, · · · , ′ and 1 ★, · · · , ★ be some random instance and instance of the se ing ( , , ( 1, · · · ,  −1)), respectively.


- Deﬁnition 3.4 (Induced subspaces). Given H1, H2, · · · , H and H1 , · · · , H as in Deﬁnition 3.3, we choose subspaces 1 ′, · · · , ′ of H[ −1] randomly for each ∈ [ ] as follows.


- • For each ∈ 1, let ′ be ∗ ⊗ H[ −1]\N( ) where ∗ is a random subspace of HN( )\{ } with

R ∗ , HN( )\{ } =

dim(H ) dim(H )

![image 58](<2018-he-quantum-lov-local-lemma_images/imageFile58.png>)

.

- • For each ∈ 2, let ′ be H[ −1].
- • For each ∈ [ ] \ [ ], let ′ be ∗ ⊗H[ −1]\N( ) where ∗ is a random subspace of HN( ) with R( ∗ , HN( )) = .


Similarly, let 1 ★, · · · , ★ be some subspaces of H[ −1] such that R( ★ , H[ −1]) = R( ′ , H[ −1]) for each ∈ [ ] and

- • For each ∈ 1, ★ acts trivially on H[ −1]\N( ).
- • For each ∈ 2, ★ = H[ −1].
- • For each ∈ [ ] \ [ ], ★ acts trivially on H[ −1]\N( ).


Remark. We will specify 1 ★, · · · , ★ concretely in Section 3.6.  e following lemmas show that 1 ′, · · · , ′ are properly deﬁned. Similarly, one can also verify that

★ 1 , · · · , ★ are also properly deﬁned.

- Lemma 3.8. For each ∈ 1 ∪ ([ ] \ [ ]), we have dim( ∗ ) is a positive integer.  us, dim( ′ ) is also a positive integer for each ∈ [ ].

 e following two lemmas are used in the proof of Lemma 3.8. Lemma 3.9 is a simple fact by (1), (2) and (4), and Lemma 3.10 is an easy observation by Deﬁnition 2.1.

- Lemma 3.9. For each ∈ [ ], we have dim(H )


= .

![image 59](<2018-he-quantum-lov-local-lemma_images/imageFile59.png>)

dim(H )

- Lemma 3.10. Given ∈ [ ], if P[R( ∈ ) = 1] = 1 for random subspaces ( ) ∈ of the se ing ( , , ( ) ∈ ), then for each ∈ , ∈N( , ) is a positive integer.

Proof of Lemma 3.8. We only prove that dim( ∗ ) is a positive integer for each ∈ 1∪([ ] \ [ ]).  en it is immediate that dim( ′ ) is also a positive integer for each ∈ [ ] by its deﬁnition. For each ∈ 1, by the deﬁnition of 1 in Deﬁnition 3.3, we have dim(H ) < dim(H ). Combining with Lemma 3.9, we have

=

dim(H ) dim(H )

![image 60](<2018-he-quantum-lov-local-lemma_images/imageFile60.png>)

(5) < 1.

Combining with Deﬁnition 3.2, we have P[R( ∈ ) = 1] = 1 for random subspaces ( ) ∈ of the se ing ( , , ( ) ∈ ). Combining with Lemma 3.10, we have ∈N( , ) is a positive integer. In addition, by ∈ N ( , ) and the deﬁnition of , we have ∈ [ −1]. Combining with Deﬁnition 3.2 and ∈N( , ) is a positive integer, we have ∈N( , ) is also a positive integer. Moreover, by (5) and (1), we have

= =

dim(H ) dim(H )

![image 61](<2018-he-quantum-lov-local-lemma_images/imageFile61.png>)

(6) .

Combining with Deﬁnition 3.4, we have = R ∗ , HN( )\{ } . By ∈ 1 and the deﬁnition of in Deﬁnition 3.1, we have N ( , ) = N ( ) \ { }.  us, we have

∈N ( , )

= R ∗ , HN( )\{ }

∈N ( )\{ }

= R ∗ , HN( )\{ } dim HN( )\{ } = dim ∗ ,

where the second equality is by Deﬁnition 3.3. Combining with that ∈N( , ) is a positive integer, we have dim ∗ is also a positive integer.  e lemma is proved.

 efollowing twolemmasshow that 1 ′, · · · , ′ areaninstanceof these ing ( , , ( 1, · · · ,  −1)).

- Lemma 3.11. For each le  vertex ∈ [ ], is an interaction graph of ( ′ ) ∈ .

Proof. Given a le  vertex ∈ [ ], by Lemma 3.7, we have either ∈ 1 or ∈ 2. If ∈ 1, we have N ( , ) = N ( ) \ { } and

′ = ∗ ⊗ H[ ]\N( ) = ∗ ⊗ H[ −1]\N( , ). If ∈ 2, we have N ( , ) = N ( ) \ { } and ′ = H[ −1]. Moreover, for each le  vertex ∈ [ ] and

∈ \{ }, we have ∈ [ ]\[ ]. Combining with [ ] = N ( ) for the right vertex , we have ∉ N ( ).  us, ∉ N ( ). Combining with Deﬁnition 3.1, we have N ( , ) = N ( ) \ { } = N ( ). Combining with Deﬁnition 3.4, we have

′ = ∗ ⊗ H[ −1]\N( ) = ∗ ⊗ H[ −1]\N( , ). In summary, we always have that Π ′ acts trivially on the qudits H[ −1]\N( , ) for each ∈ [ ] and ∈ .  en is an interaction graph of ( ′ ) ∈ .

- Lemma 3.12. For each le  vertex ∈ [ ] and ∈ , we have


- (a) 0 < ≤ 1;
- (b) ′ = H[ −1] if = 1;
- (c) ′ = ∗ ⊗H[ −1]\N( , ) where ∗ is a random subspace of HN( , ) according to the Haar measure with R( ∗ , HN( , )) = if < 1.


Proof. By (1), we have 0 < ≤ 1 immediately. Recall that = { } ∪ ([ ] \ [ ]). Combining with

∈ , we have either ∈ [ ] \ [ ] or = . In the following, we prove (b) and (c) of this lemma for the two cases ∈ [ ] \ [ ] and = separately.  en the lemma is immediate.

At ﬁrst, we assume ∈ [ ]\[ ]. We have ∉ N ( ) and then N ( ) = N ( , ).  us, by ∈ [ ]\[ ] and Deﬁnition 3.4, we have

′ = ∗ ⊗ H[ −1]\N( ) = ∗ ⊗ H[ −1]\N( , )

where ∗ is a random subspace of HN( ) = HN( , ) according to the Haar measure with

- (7) R( ∗ , HN( , )) = R( ∗ , HN( )) = . Moreover, by ∈ [ ] \ [ ] and ∈ [ ], we have ≠ . Combining with Deﬁnition 3.1, we have = .

- Combining with (7), we have R( ∗ , HN( , )) = .  en (c) of this lemma is proved. Meanwhile, if

= 1, by (7) we have R( ∗ , HN( )) = 1 and then ∗ = HN( ). Combining with Deﬁnition 3.4, we have ′ = ∗ ⊗ H[ −1]\N( ) = H[ −1].  en (b) of this lemma is proved.  us the case ∈ [ ] \ [ ] is proved.

In the following, we assume = . We have ∈ N ( ) = N ( ) and then

(8) N ( , ) = N ( ) \ { }.

If = 1, we have = 1. Moreover, we claim that = 1 if and only if ∈ 2.  us by = 1, we have ∈ 2. Combining with Deﬁnition 3.4, we have ′ = H[ −1]. Combining with = , we have

′ = H[ −1].  en (b) of this lemma is proved. If < 1, we have = < 1. Combining with the claim that = 1 if and only if ∈ 2, we have ∉ 2. Combining with ∈ [ ] and Lemma 3.7, we have

∈ 1. Combining with Deﬁnition 3.4 and = , we have ′ = ∗ ⊗ H[ −1]\N( ) where ∗ is a random subspace of HN( )\{ } with

R ∗ , HN( )\{ } =

dim(H ) dim(H )

![image 62](<2018-he-quantum-lov-local-lemma_images/imageFile62.png>)

.

- Combining with (8), we have ′ = ∗ ⊗ H[ −1]\N( ) = ∗ ⊗ H[ −1]\N( , )

where ∗ is a random subspace of HN( , ) with R ∗ , HN( , ) = R ∗ , HN( )\{ } =

dim(H ) dim(H )

![image 63](<2018-he-quantum-lov-local-lemma_images/imageFile63.png>)

(9) . In addition, by (2) and dim(H ) = , we have

dim(H ) = = 2

ℓ=1

(10) ( ℓ ([ ] | ℓ)) .

- Combining with (9), (4) and (10), we have


- (11) ( ℓ ([ ] | ℓ)) . Combining with (4) and (10), we have
- (12)


2

ℓ∈[ ] ( ℓ ([ ] | ℓ)) 2 ([ ] | )

( ℓ ([ ] | ℓ)) ([ ] | )

dim(H ) dim(H )

= ℓ∈[ ]

R ∗ , HN( , ) =

. Combining with = < 1 and (1), we have

=

![image 64](<2018-he-quantum-lov-local-lemma_images/imageFile64.png>)

![image 65](<2018-he-quantum-lov-local-lemma_images/imageFile65.png>)

![image 66](<2018-he-quantum-lov-local-lemma_images/imageFile66.png>)

( ℓ ([ ] | ℓ)) ([ ] | )

R ∗ , HN( , ) = ℓ∈[ ]

= = .  en (c) of this lemma is proved.

![image 67](<2018-he-quantum-lov-local-lemma_images/imageFile67.png>)

At last, we prove the claim that = 1 if and only if ∈ 2.  en the case = is proved and the lemma is immediate. If = 1, by (1) we have

([ ] | ) ≤

ℓ=1

dim(H ) − dim(H ) = 2 ([ ] | ) − 2

( ℓ ([ ] | ℓ))

ℓ=1

= 2 ([ ] | ) −

( ℓ ([ ] | ℓ)) .

ℓ=1

Combining with (11), we have dim(H ) ≤ dim(H ). Combining with Deﬁnition 3.3 and ∈ , we have ∈ 2. Conversely, we also have = 1 if ∈ 2.  e claim is proved.

By Lemmas 3.11, 3.12, and Deﬁnition 2.1, we have the following corollary. Corollary3.6. Foreach le vertex ∈ [ ], ( ′ ) ∈ isarandom instance ofthe se ing ( , , ( 1, · · · ,  −1)). Similarly, one can also prove the following corollary.

- Corollary 3.7. For each le  vertex ∈ [ ], ( ★ ) ∈ is an instance of the se ing ( , , ( 1, · · · ,  −1)).


- 3.5. Subspaces. In this subsection, we deﬁne the subspaces. Given H1, H2, · · · , H , H1 , · · · , H as in


Deﬁnition 3.3 and 1 ★, · · · , ★ as in Deﬁnition 3.4, we deﬁne the subspaces 1, · · · ,  as follows. For each ∈ [ ], is deﬁned based on the tenser product of ★ and the induced qudit H or the qudit

H . If the relative dimension of the tenser product is less than , an orthogonal subspace is added to make up the deﬁcit.  e goal is to let ( 1, · · · ,  ) be an instance of the se ing ( , , ).

- Deﬁnition 3.5 (Subspaces). For each ∈ [ ], deﬁne 1, · · · ,  as follows.


- • If ∈ 1, let = ★ ⊗ H .
- • If ∈ 2, let = ★ ⊗ H ⊕ ⊗ H[ ]\N( ) where isanarbitrarilysubspace ofHN( )\{ }⊗ ℓ∈[ ]\{ } Hℓ with

dim( ) = dim(H ) − dim(H ) · dim(HN( )\{ }).

- • If ∈ [ ] \ [ ], let = ★ ⊗ H .


 e following two lemmas show that 1, · · · ,  are properly deﬁned.

- Lemma 3.13. For each ∈ 2, dim( ) is a nonnegative integer. In addition, dim( ) is also a positive integer for each ∈ [ ].

Proof. We only prove that dim( ) is a nonnegative integer for each ∈ 2. Combining with Deﬁnition 3.4 and that dim( ★ ) is a positive integer, it is immediate that dim( ) is also a positive integer

for each ∈ [ ]. Given ∈ 2, we have dim(H ) ≥ dim(H ).  us dim( ) = dim(H ) − dim(H ) · dim(HN( )\{ }) ≥ 0.

In addition, recall that , ℓ=1 ℓ ([ ] | ℓ) and ([ ] | ) are postive integers by Lemma 3.6.  us, by (2) and (4) we have

dim( ) = dim(H ) − dim(H ) · dim(HN( )\{ })

= − 2 ([ ] | )) · dim(HN( )\{ })

= 2 · dim(HN( )\{ }) · − ([ ] | ) +

ℓ=1

( ℓ ([ ] | ℓ))

= ( ) · dim(HN( )\{ }) · − ([ ] | ) +

ℓ=1

( ℓ ([ ] | ℓ)) is also an integer. In summary, we have dim( ) is a nonnegative integer.  e lemma is proved.

- Lemma 3.14. For each ∈ 2,


dim( ) ≤ HN( )\{ } ⊗

Hℓ .

ℓ∈[ ]\{ }

Proof. Given ∈ 2, we have dim( ) = dim(H ) − dim(H ) · dim HN( )\{ } ≤ dim HN( )\{ } · dim(H ) − dim(H )

= dim HN( )\{ } · dim

Hℓ = dim HN( )\{ } ⊗

ℓ∈[ ]\{ }

Hℓ .

ℓ∈[ ]\{ }

 e following two lemmas show that ( 1, · · · ,  ) is an instance of the se ing ( , , ).

- Lemma 3.15. is an interaction graph of 1, · · · ,  . Proof. If ∈ 1, we have

= ′ ⊗ H = ∗ ⊗ H[ ]\N( ) ⊗ H . If ∈ 2, we have

= ′ ⊗ H ⊕ ⊗ H[ ]\N( ) = H[ −1] ⊗ H ⊕ ⊗ H[ ]\N( )

= H[ ]\N( ) ⊗ HN( )\{ } ⊗ H ⊕ .

If ∈ [ ] \ [ ], we have = ∗ ⊗ H[ ]\N( ). In summary, we always have that Π acts trivially on the qudits H[ ]\N( ) for each ∈ [ ].  us we have is one interaction graph of 1, · · · ,  .

- Lemma 3.16. For each le  vertex ∈ [ ], we have R( , H[ ]) = . Proof. If ∈ 1, we have ∈ [ ].  en ∈ N ( ) and [ − 1] \ ([ ] \ N ( )) = N ( ) \ { }.  erefore,

R , H[ ] = R ′ ⊗ H , H[ ] = R ′ , H[ −1] × R H , H

= R ∗ ⊗ H[ ]\N( ), H[ −1] × R H , H

= R ∗ , HN( )\{ } × R H , H =

dim(H ) dim(H )

![image 68](<2018-he-quantum-lov-local-lemma_images/imageFile68.png>)

·

dim(H ) dim(H )

![image 69](<2018-he-quantum-lov-local-lemma_images/imageFile69.png>)

= .

If ∈ 2, by that is a subspace of HN( )\{ } ⊗ ℓ∈[ ]\{ } Hℓ , we have H[ −1] ⊗ H and ⊗ H[ ]\N( ) are orthogonal.  us, we have

R , H[ ] = R ′ ⊗ H ⊕ ⊗ H[ ]\N( ), H[ ] = R H[ −1] ⊗ H ⊕ ⊗ H[ ]\N( ), H[ ]

=

dim H[ −1] ⊗ H ⊕ ⊗ H[ ]\N( ) dim H[ ]

![image 70](<2018-he-quantum-lov-local-lemma_images/imageFile70.png>)

=

dim H[ −1] ⊗ H + dim ⊗ H[ ]\N( ) dim H[ ]

![image 71](<2018-he-quantum-lov-local-lemma_images/imageFile71.png>)

=

dim H[ −1] ⊗ H dim H[ −1] ⊗ H

![image 72](<2018-he-quantum-lov-local-lemma_images/imageFile72.png>)

+

dim ⊗ H[ ]\N( ) dim HN( ) ⊗ H[ ]\N( )

![image 73](<2018-he-quantum-lov-local-lemma_images/imageFile73.png>)

=

dim H dim (H )

![image 74](<2018-he-quantum-lov-local-lemma_images/imageFile74.png>)

+

dim ( ) dim HN( )

![image 75](<2018-he-quantum-lov-local-lemma_images/imageFile75.png>)

=

dim H dim (H )

![image 76](<2018-he-quantum-lov-local-lemma_images/imageFile76.png>)

+

dim(H ) − dim(H ) · dim(HN( )\{ }) dim HN( )

![image 77](<2018-he-quantum-lov-local-lemma_images/imageFile77.png>)

=

dim H dim (H )

![image 78](<2018-he-quantum-lov-local-lemma_images/imageFile78.png>)

+

dim(H ) − dim(H ) dim (H )

![image 79](<2018-he-quantum-lov-local-lemma_images/imageFile79.png>)

= . If ∈ [ ] \ [ ], we also have

R( , H[ ]) =

dim ′ ⊗ H dim(H[ ])

![image 80](<2018-he-quantum-lov-local-lemma_images/imageFile80.png>)

=

dim ∗ ⊗ H[ −1]\N( ) ⊗ H dim(H[ ])

![image 81](<2018-he-quantum-lov-local-lemma_images/imageFile81.png>)

=

dim ∗ dim(HN( ))

![image 82](<2018-he-quantum-lov-local-lemma_images/imageFile82.png>)

= R( ∗ , HN( )) = .

By Lemmas 3.15 and 3.16, we have the following corollary.

- Corollary 3.8.  e instance ( 1, · · · ,  ) is of the se ing ( , , ).  e following is an easy property of 1, · · · ,  by Deﬁnition 3.5.


- Lemma 3.17. If for each le  vertex ∈ [ ], ( ★ ) ∈ span the whole space H[ −1], then 1, · · · ,  span the whole space H[ ].


Proof. By ( ★ ) ∈ span the whole space H[ −1] for each le  vertex ∈ [ ], we have ( ★ ⊗ H ) ∈ span the whole space H[ −1] ⊗ H . In addition, by Deﬁnition 3.5 we have ★ ⊗ H = and

★ ⊗ H ⊆ ★ ⊗ H = for each ∈ \ { } = [ ] \ [ ].  us, we have 1, · · · ,  span the whole space H[ ].

- 3.6. Proof of  eorem 3.2. In this subsection, we ﬁnish the proof of Theorem 3.2.  e following lemma will be used in the proof of Theorem 3.2. Given = ([ ], [ ],   ) and


= ( 1, · · · ,  ) where ∈ I( ), let ′ be the resulted graph by adding a le  vertex + 1 where N ( +1) = [ ] to and let ′ be ( 1, · · · ,  , ( , )). With this lemma, one can verify Theorem 3.2 (b) on and by applying Theorem 3.2 (a) to ′ and ′.

- Lemma 3.18. Given any = ([ ], [ ],   ), and any rational = ( 1, · · · ,  ) ∈ [0, 1] , let ′ = ([ + 1], [ ],  ′ ) where ′ = ∪ {( + 1, 1), ( + 1, 2), · · · , ( + 1, )}, i.e., the le  vertex + 1 has neighbors N ( + 1) = [ ]. If ∈ I( ), let = ( , ); otherwise, let = 0.  en for any +1 ≥ ,


′ ( 1, · · · ,  ,  +1) ∉ I( ′ ). In addition, given = ( 1, · · · ,  ), if P [R ( ∈ ) = 1] = 1 for the random instance of the se ing ( ′ , ′, ), then P[R( ∈ ) ∈ [1 − +1, 1 − ]] = 1 for the random instance of the se ing ( , , ).

Proof. At ﬁrst, we prove ′ ∉ I( ′ ). If ∉ I( ), we have +1 ≥ = 0.  en by ∉ I( ) and the deﬁnition of ′ , ′ = ( 1, · · · ,  ,  +1) ∉ I( ′ ) is immediate. If ∈ I( ), we have +1 ≥ =

( , ). By Deﬁnition 1.1 we have ( ′ , ′, [ + 1]) =

(−1)| |

(−1)| |

= − +1 +

∈Ind( ′ )

∈

∈

∈Ind( )

= − +1 + ( , ) ≤ 0. Combining with Lemma 3.2, we have ′ ∉ I( ′ ).

In the next, we show that if P [R ( ∈ ) = 1] = 1 for the random instance of the se ing ( ′ , ′, ), then P[R( ∈ ) ∈ [1 − +1, 1 − ]] = 1 for the random instance of the se ing ( , , ).  en the lemma is immediate. Given the random instance 1, · · · ,  ,  +1 of the se ing ( ′ , ′, ) where

= 1

P 

- (13) = 1,

we have

R

∈[ ]

≥ R

∈[ +1]

− R ( +1) = R

∈[ +1]

− +1.

Combining with (13), we have

P 

 

R

∈[ ]

≥ 1 − +1  

- (14) = 1.


R

 

 

∈[ +1]

In addition, if ∈ I( ), by Theorem 3.1 we have R ∈[ ] ≤ 1 − ( , ) = 1 − . If ∉ I( ), we also have R ∈[ ] ≤ 1 = 1 − .  erefore, we always have R ∈[ ] ≤ 1 − . Combining with (14), we have P[R( ∈ ) ∈ [1 − +1, 1 − ]] = 1. Moreover, by ( 1, · · · ,  ,  +1) is the random instance of the se ing ( ′ , ′, ), one can verify that ( 1, 2, · · · ,  ) is the random instance of the se ing ( , , ),  e lemma is proved.

Now we can prove  eorem 3.2, the main idea of which has been illustrated in Section 3.1.

- Proof of  eorem 3.2. (a).  e proof is by induction on the number of le  vertices in . For the base case that the number of le  vertices in is no more than 1, the theorem holds trivially.


For the induction step, given any integer ≥ 2, we assume that (a) of this theorem holds for any interaction graph where the number of le  vertices is no more than − 1. In the following, we prove that the theorem also holds for any graph where the number of le  vertices is .

If ∉ I( ), by Lemma 3.2 we have there is some ⊆ [ ] such that ( ) ≤ 0. Let ⊆ be a set such that ( ) ≤ 0 and ( ) > 0 for each . In the following, we consider the two possible cases

[ ] and = [ ] separately.

At ﬁrst we assume [ ]. Let ′ be the interaction graph obtained from by deleting the le  vertices [ ] \ and the edges connected to these vertices. Let be ( ) ∈ . By ( ′, , ) = ( ) ≤ 0 and Lemma 3.2, we have ∉ I( ′). Let = ∈ and = ∉ . Let N ( ) denote N ( , ) for simpliﬁcation. For each le  vertex ∈ , we have N ( ′, ) = N ( ). Combining with the assumption

= 1 if N ( ) = ∅, we have = 1 if N ( ′, ) = ∅. Combining with ∉ I( ′) and the induction hypothesis, we have there exists some = ( 1, 2, · · · ,  ) where ≤ 4 for each ∈ [ ] such that random subspaces of the se ing ( ′, , ) span the whole space.  us, there exists a subspace set of the se ing ( ′, , ) spanning the whole space. Combining with Lemma 3.1 (a), we have for any set of qudits H1, H2, · · · , H where dim(H1, · · · , H ) = , there exists a subspace set ( ′ ) ∈ of H[ ] such that ( ′ ) ∈ ∼ ( ′, ,   ) and ( ′ ) ∈ spans the whole space H[ ]. Moreover, by = ∈ ,

= ∉ and ≤ 4 for each ∈ [ ], we have ≤ 4 · ≤

- (15) 4 = 4 .


∈[ ]

We deﬁne a subspace set ( 1 ★, 2★, · · · , ★ ) of H[ ] as follows. For each ∈ , let ★ = ′ . For each

∈ [ ]\ , let ★ = ∗ ⊗H[ ]\N( ) where ∗ is an arbitrary subspace of HN( ) with R ∗ , HN( ) = . First of all, we show that dim( ∗ ) is an integer for each ∈ [ ] \ .  us ( 1 ★, 2★, · · · , ★ ) is well deﬁned. Given ∈ [ ] \ , if = 1, then by R ∗ , HN( ) = , we have dim( ∗ ) = dim(HN( )) is an integer. In the following, we assume ∈ [ ] \ and < 1. Combining with the assumption if N ( ) = ∅ then = 1, we have N ( ) ≠ ∅. Assume w.l.o.g. ∈ N ( ) for some right vertex ∈ [ ]. By the deﬁnitions of , and H1, H2, · · · , H , we have

dim ∗ = · dim HN( ) = ·

dim (H ) = ·

∈N ( )

( ) = ·

![image 83](<2018-he-quantum-lov-local-lemma_images/imageFile83.png>)

∈N ( )

∈N ( )

=

![image 84](<2018-he-quantum-lov-local-lemma_images/imageFile84.png>)

( ) =

![image 85](<2018-he-quantum-lov-local-lemma_images/imageFile85.png>)

∈N ( )\{ }

ℓ∉

ℓ

( ) =

∈N ( )\{ }

ℓ∉ ∪{ }

ℓ

( ) ,

∈N ( )\{ }

where the last equality is by that ∈ [ ] \ .  erefore, by  , ℓ,  , ℓ are integers for each ℓ ∈ [ ] and ∈ [ ], we have dim( ∗ ) is also an integer.

In the next, we show that ( 1 ★, 2★, · · · , ★ ) is an instance of the se ing ( , ,   ) spanning the whole space H[ ].  us, (a) of this theorem is immediate by Theorem 3.3 and (15). At ﬁrst, we have dim(H1, · · · , H ) = . Meanwhile, given a le  vertex ∈ [ ], we have either ∈ or ∈ [ ] \ . If

∈ , we have ★ = ′ . Combining with ( ′ ) ∈ ∼ ( ′, ,   ), we have

★ = ′ = ⊗ H[ ]\N( ′, ) = ⊗ H[ ]\N( ),

where is some subspace of HN( ) with R , HN( ) = .  us R ★ , H[ ] = R ′ , H[ ] = . Otherwise, ∈ [ ]\ . We also have ★ = ∗ ⊗H[ ]\N( ) and R ★ , H[ ] = R ∗ , HN( ) = .  us,

is an interaction graph of ( 1 ★, 2★, · · · , ★ ) and R , H[ ] = . In addition, by that ( ′ ) ∈ spans the whole space H[ ] and that ★ = ′ for each ∈ , we have ( 1 ★, 2★, · · · , ★ ) spans the whole space H[ ] immediately.  e case [ ] is proved.

In the following we assume = [ ]. Recall that satisﬁes ( ) ≤ 0 and ( ) > 0 for each . Combining with = [ ] and Proposition 3.4 (d), we have ( ) is connected. Also recall that ≥ 2, we have there must be a right vertex in with at least two neighbors in the le  vertices. Without loss of generality, we assume the right vertex is such a vertex and N ( ) = [ ] where ≥ 2. In addition, by ≥ 2 and ( ) > 0 for each = [ ], we have < 1 for each le  vertex of . Otherwise,

≥ 1. We have ({ }) = 1 − ≤ 0 by Deﬁnition 1.1, a contradiction with that ( ) > 0 for each

[ ]. For each le  vertex ∈ [ ], combining < 1 with the assumption that = 1 if N ( ) = ∅ in the theorem, we have N ( ) ≠ ∅.  us, all the assumptions in Deﬁnition 3.1 are satisﬁed. One can deﬁne the induced interaction graphs, the induced qudits with induced dimensions, and the induced subspaces with the induced relative dimensions as in Deﬁnitions 3.1, 3.2, 3.3 and 3.4, and deﬁne the dimensions of qudits = ( 1, · · · ,  ) and the subspaces ( 1, · · · ,  ) as in Deﬁnitions 3.2 and 3.5. By Corollary 3.8, we have ( 1, · · · ,  ) is of the se ing ( , , ). Moreover, we claim that ≤ 4

for each ∈ [ ] and 1, · · · ,  spans the whole space.  en (a) of this theorem is immediate by Theorem 3.3. In the following, we prove the claim.

At ﬁrst, we prove that ≤ 4 for each ∈ [ ]. Recall the deﬁnitions of and in Deﬁnition 3.1. By ([ ]) = ( ) ≤ 0 and Lemma 3.3, for each ∈ [ ] we have ∉ I( ) and if N ( , ) = ∅ for some le  vertex ∈ in , then = 1. Combining with the induction hypothesis, we have there exists some ( ) ∈ such that ≤ 4 − +1 for each ∈ and the random instance of the se ing ( , , ( ) ∈ ) spans the whole space. Combining withthe deﬁnitionof ( ) ∈ in Deﬁnition3.2, we have if < 1, then = ≤ 4 − +1 for each ∈ ; otherwise ≥ 1, we also have = ≤ 4 − +1 Combining with (2), we have for each ∈ [ − 1],

- (16) ≤ ·4 − +1 ≤ 4 ,

where the last inequality is by ≥ 2. Combining with Lemma 3.5, we have ≤ 4 for each ∈ [ ].

In the following, we show that 1, · · · ,  spans the whole space.  en (a) of this theorem is proved. Recall that for each ∈ [ ], the random instance of the se ing ( , , ( ) ∈ ) spans the whole space. If < 1, we have = by Deﬁnition 3.2, then the random instance of the se ing ( , , ( ) ∈ ) spans the whole space. If ≥ 1, we have = 1 by (1).  us we also have the random instance of the se ing ( , , ( ) ∈ ) spans the whole space. Combining with (2) and Lemma 3.1 (b), we have the random subspaces of the se ing ( , , ( ) ∈ ) spans the whole space. Combining with Corollary 3.6, we have ( ′ ) ∈ as in Deﬁnition 3.4, is a random instance of the se ing ( , , ( ) ∈ ) and spans the whole space. In other words, P[R( ∈ ′ , H[ −1]) = 1] = 1. By the union bound, we have

P

∈[ ]

R

∈

′ , H[ −1] = 1 ≥ 1 −

∈[ ]

1 − P R

∈

′ , H[ −1] = 1 = 1.

 us, wehavetherearesomespaces ( ★ ) ∈[ ], asinDeﬁnition3.4, satisﬁesthatR( ∈ ★ , H[ −1]) = 1. Combining with Lemma 3.17, we have that the subspaces 1, · · · ,  span the whole space H[ ], which ﬁnishes the proof of (a).

(b). Given = ([ ], [ ],   ) and = ( 1, · · · ,  ) where ∈ I( ), by Lemma 3.2, we have ( , , [ ]) > 0. Let ′ = ([ + 1], [ ],  ′ ) where ′ = ∪ {( + 1, 1), ( + 1, 2), · · · , ( + 1, )}

and ′ be ( 1, · · · ,  ,  +1) where +1 = ( , , [ ]) > 0. By Lemma 3.18, we have ′ ∉ I( ′ ). Let

+1 be the minimum positive integer such that +1 is an integer.  us, we have +1 ≤ if +1 is an integer. In addition, by Deﬁnition 1.1 we have

+1 = +1

∈[ ]

= ( , , [ ])

∈[ ]

=

∈Ind( )

(−1)| |

∈ ∈[ ]\

.

Combining with ,  are integers for each ∈ [ ], we have +1 is also an integer.  us we have

+1 ≤ .  erefore, we have

∈[ +1]

≤ 2.

Recall that ′ ∉ I( ′ ). Applying (a) of this theorem to ′ and ′, we have there is some = ( 1, · · · ,  ) such that

≤

∈[ +1]

4 +1 ≤ 8+4

for each ∈ [ ] and P [R ( ∈ ) = 1] = 1 for the random instance of the se ing ( ′ , ′, ). Combining with Lemma 3.18, we have

P 

 

R

∈[ ]

∈ [1 − +1, 1 − ( , , [ ])]

 

- (17) = 1,


=

∈

for the random instance ( 1, 2, · · · ,  ) of the se ing ( , , ). Combining with +1 = ( , , [ ]), we have

= 1 − ( , , [ ])

P 

= 1,

R

 

 

∈[ ]

Recall that ≤ 8+4 for each ∈ [ ].  e conclusion is immediate.

- 3.7. Proof of  eorem 1.3. In this subsection, we prove  eorem 1.3.  eorem 1.3 provides an in-


terval of R ( ∈ ) for the random instance of some given se ing. By Lemma 3.18, it is suﬃcient to show that the random instance ′ of another se ing spans the whole space. Given any ,

= ( 1, · · · ,  ), = ( 1, · · · ,  ) and any positive integer , to prove that the random instance of the se ing ( , , ) spans the whole space, Lemma 3.19 shows that it is suﬃcient to prove that the random instance of the se ing ( , ′, ′) spans the whole space for some ′ = ( 1 ′, · · · , ′ ) and ′, where ′ is tailored from such that ′ is a multiple of 1/ for each ∈ [ ], and ′ ≤ . Because ′ is tailored to multiples of 1/ , by  eorem 3.2 (a) we have there exists some ′ which is upper bounded by a function of and such that the random instance of the se ing ( , ′, ′) spans the whole space.  us  eorem 1.3 is proved.

 e following lemma is the core of the proof of  eorem 1.3.

- Lemma 3.19. For any interaction graph = ([ ], [ ],   ), any positive integer , any rational


= ( 1, · · · ,  ) ∈ [0, 1] , let ′ = ( 1 ′, · · · , ′ ) where ′ = max

⌊ − 1⌋

- (18) , 0


![image 86](<2018-he-quantum-lov-local-lemma_images/imageFile86.png>)

for each ∈ [ ]. If there exists some ′ such that the random instance of the se ing ( , ′, ′) spans the whole space, then for any ≥ ′, the random instance of the se ing ( , , ) spans the whole space.

Proof. By Theorem 3.3, to prove this lemma, it is suﬃcient to construct an instance ( 1, 2, · · · ,  ) ∼ ( , , ) spanning the whole space H[ ] where dim (H1, · · · , H ) = . Suppose ′ = ( 1 ′, · · · , ′ ) and

= ( 1, · · · ,  ).  e construction of ( 1, 2, · · · ,  ) is as follows.

- • For each ∈ [ ], decompose H into two orthogonal subspaces H = H ⊕ H with

dim(H ) = ′ · ′ , dim(H ) = − dim(H ).

![image 87](<2018-he-quantum-lov-local-lemma_images/imageFile87.png>)

We emphasize that dim(H ) = 0 if is a multiple of ′ . Note that dim(H ) is a multiple of ′ .  us, by Lemma 3.1 (a) and that the random instance of the se ing ( , ′, ′) spans

the whole space, we have there is an instance 1 ∗ ⊗ H [ ]\N(1), · · · , ∗ ⊗ H [ ]\N( ) ∼ spanning H [ ] with relative dimension ′ to H [ ].

- • For any ∈ [ ] where ′ > 0, let

=

∈N ( )

H ⊗ HN( )\{ } , = ∗ ⊕ ⊕ ★ ⊗ H[ ]\N( )

where ★ is an arbitrary subspace of HN( ) which is orthogonal with ∗ ⊕ and of dimension

dim( ★ ) = dim HN( ) − dim ∗ ⊕ . We remark that it is possible that dim( ★ ) = 0.

- • For any ∈ [ ] where ′ = 0, let = ★ ⊗ H[ ]\N( ) where ★ is an arbitrary subspace of HN( ) of dimension dim HN( ) .


At ﬁrst, we show that dim( ★ ) is a nonnegative integer for each ∈ [ ].  us, ( 1, 2, · · · ,  ) is properly deﬁned. Recall that when we talk about the instance of the se ing ( , , ), we always

assume that the Hilbert space H[ ] with the dimension vector can admit an instance with the interaction graph and the relative dimension vector as in Deﬁnition 2.1.  us, we have ∈N( ) is an integer for each ∈ [ ], otherwise, some subspace in the instance must has a fractional dimension, which is a contradiction. By ∈N( ) is an integer for each ∈ [ ], we have dim( ★ ) is also an integer. In the next, we show that dim( ★ ) is nonnegative for each ∈ [ ]. If ′ = 0, this conclusion is immediate. In the following, we assume ′ > 0. Recall that ( 1 ∗⊗H [ ]\N(1), · · · , ∗ ⊗H [ ]\N( )) ∼ has relative dimension ′ to H [ ].  us, we have ∗ is a subspace of H N( ) with relative dimension ′ to H N( ).  erefore, we have

- (19) dim( ∗ ) = ′ · dim(H N( )) ≤ ′ · dim(HN( )). Meanwhile, for each ∈ [ ], by the deﬁnition of H we have dim(H ) ≤ ′ . Combining with dim(H ) = ≥ · ′ , we have R H , H ≤ 1 .  us, by the deﬁnition of we have

![image 88](<2018-he-quantum-lov-local-lemma_images/imageFile88.png>)

R , HN( ) =

∈N ( )

R H ⊗ HN( )\{ }, HN( ) =

∈N ( )

R H , H ≤ =

![image 89](<2018-he-quantum-lov-local-lemma_images/imageFile89.png>)

1

![image 90](<2018-he-quantum-lov-local-lemma_images/imageFile90.png>)

.

 erefore,

dim ( ) = R , HN( ) · dim HN( ) ≤

dim HN( )

![image 91](<2018-he-quantum-lov-local-lemma_images/imageFile91.png>)

- (20) . In addition, by (18) we have ≥ ′ + 1 . Combining with (19) and (20), we have


![image 92](<2018-he-quantum-lov-local-lemma_images/imageFile92.png>)

1

dim ∗ ⊕ = dim( ∗ ) + dim ( ) = ′ +

![image 93](<2018-he-quantum-lov-local-lemma_images/imageFile93.png>)

dim HN( ) ≤ dim HN( ) .

Combining with dim( ★ ) = dim HN( ) − dim ∗ ⊕ , we have dim( ★ ) ≥ 0. In summary, dim( ★ ) is a nonnegative integer for each ∈ [ ].

In the next, we show that ( 1, 2, · · · ,  ) ∼ ( , , ). By the deﬁnition of ( 1, 2, · · · ,  ), we have is an interaction graph of ( 1, 2, · · · ,  ) immediately. In addition, if ′ = 0, we have

R( , H[ ]) = R ★ ⊗ H[ ]\N( ), H[ ] = R ★ , N ( ) = .

If ′ > 0, by the deﬁnitions of ∗ ,  and ★ , we have ∗ ,  , ★ are orthogonal each other.  us, we have

dim ∗ ⊕ ⊕ ★ = dim ∗ + dim ( ) + dim ★

= dim HN( ) − dim ∗ ⊕ + dim ( ) + dim ★

= dim HN( ) .  erefore,

R( , H[ ]) = R ∗ ⊕ ⊕ ★ ⊗ H[ ]\N( ), H[ ] = R ∗ ⊕ ⊕ ★ , HN( )

dim ∗ ⊕ ⊕ ★ dim HN( )

dim HN( ) dim HN( )

= .

=

=

![image 94](<2018-he-quantum-lov-local-lemma_images/imageFile94.png>)

![image 95](<2018-he-quantum-lov-local-lemma_images/imageFile95.png>)

 us we have R(( 1, 2, · · · ,  ), H[ ]) = . Moreover, one can verify that dim(H1, · · · , H ) = . In summary, we have ( 1, 2, · · · ,  ) ∼ ( , , ).

At last, we verify that ( 1, 2, · · · ,  ) spans the whole space H[ ].  en this lemma is proved. Deﬁne

= { ∈ [ ] | ′ > 0}, =

N ( ).

∈

Recall that the instance 1 ∗ ⊗ H [ ]\N(1), · · · , ∗ ⊗ H [ ]\N( ) ∼ has relativedimension ′ to H [ ] and spans H [ ].  us, we have dim( ∗ ) = ′ = 0 for each ∉ and

H [ ] ⊆

∈[ ]

∗ ⊗ H [ ]\N( ) .

 erefore we have H [ ] ⊆

∈[ ]

∗ ⊗ H [ ]\N( ) =

∈

∗ ⊗ H [ ]\N( ) ⊆

∈

∗ ⊗ H[ ]\N( ) .

Moreover, by the deﬁnitions of and , we have for each ∈ , ∗ ⊗ H[ ]\N( ) acts trivially on the qudits H[ ]\ .  us, we have

- (21) ∗ ⊗ H[ ]\N( ) . In addition, by the deﬁnitions of , and , we have
- (22)


H ⊗ H[ ]\ ⊆

∈

H ⊗ H[ ]\{ } =

H ⊗ H[ ]\{ } =

∈ ∈N ( )

∈ ∈ N ( )

∈

H[ ]\N( ) ⊗

H ⊗ HN( )\{ } ⊗ H[ ]\N( ) =

=

∈ ∈N ( )

∈

H ⊗ H[ ]\{ }

∈N ( )

H ⊗ HN( )\{ }

H[ ]\N( ) ⊗ . Combining with (21) and (22), we have H[ ] =

=

∈

H = H[ ]\ ⊗

∈[ ]

∈

H ⊕ H

⊆ H[ ]\ ⊗ H + H[ ]\ ⊗

∈

H ⊗

= H[ ]\ ⊗ H +

∈

H ⊗ H[ ]\{ }

∈ \{ }

H ⊕ H

⊆

∈

=

∈

∗ ⊗ H[ ]\N( ) +

∈

# ( ∗ ⊕ ) ⊗ H[ ]\N( ) ⊆

H[ ]\N( ) ⊗

∈[ ]

.

In other words, ( 1, 2, · · · ,  ) spans the whole space H[ ], which ﬁnishes the proof. Now we can prove Theorem 1.3.

Proof of  eorem 1.3. Suppose = ( 1, · · · ,  ). Let ′ = ([ + 1], [ ],  ′ ) where ′ = ∪ {( + 1, 1), ( + 1, 2), · · · , ( + 1, )}. Deﬁne ′ = ( 1 ′, · · · , ′ , ′ +1) as follows. Let ′ be deﬁned as (18) for each ∈ [ ]. Deﬁne

′

+1

( , ( 1 ′, · · · , ′ )), if ( 1 ′, · · · , ′ ) ∈ I( ), 0, otherwise.

By Lemma 3.2, we have ( , ( 1 ′, · · · , ′ )) ≥ 0 if ( 1 ′, · · · , ′ ) ∈ I( ).  us, we always have ′ +1 ≥ 0. Deﬁne

( , ), if ∈ I( ), 0, otherwise.

=

Similarly to ′ +1, we also have ≥ 0. Let +1 = ′ +1 + 1/ .

We claim that ≤ +1 ≤ + and that there is some ′ = ( 1 ′, · · · , ′ ) where ′ ≤ 8 ·4 for each ∈ [ ] such that the random instance of the se ing ( ′ , ′, ′) spans the whole space.  us, by

- Lemma 3.19 we have for any ≥ · 1+8 4 , · · · ,  · 1+8 4 ≥ ′,


the random instance of the se ing ( ′ , ( 1, · · · ,  +1), ) spans the whole space. By Lemma 3.18 and

≤ +1, we have P [R ( ∈ ) ∈ [1 − +1, 1 − ]] = 1 for the random instance of the se ing ( , , ). Combining with +1 ≤ + , we have

- (23) ∈ [1 − +1, 1 − ] = 1.

If ∉ I( ), we have = 0.  en (a) of this theorem is immediate by (23). If ∈ I( ), we have

= ( , ).  en (b) of this theorem is also immediate by (23). In the following, we prove the claims.  en the theorem is proved.

At ﬁrst, we show the claim ≤ +1 ≤ + . Firstly, if ∉ I( ), we have = 0.  en +1 = ′

+1 + 1/ ≥ 0 = . If ∈ I( ), we have = ( , ). By (18) we have ′ ≤ for each ∈ [ ].  en ( 1 ′, · · · , ′ ) ≤ . We have

( , ( 1 ′, · · · , ′ )) ≥ ( , ) =  ,

because ( , 1) ≤ ( , 2) for any and any 2 ≤ 1 where 1 ∈ I( ). In addition, by ( 1 ′, · · · , ′ ) ≤ and ∈ I( ), wealso have ( 1 ′, · · · , ′ ) ∈ I( ) andthen ′ +1 = ( , ( 1 ′, · · · , ′ )).  us, we have

+1 = ′ +1 + 1/ = ( , ( 1 ′, · · · , ′ )) + 1/ ≥ + 1/ ≥  .

In summary, we always have +1 ≥ . In the following, we prove +1 ≤ + . By +1 = ′ +1 +1/ , it is suﬃcient to show ′ +1 ≤ + − 1/ . If ( 1 ′, · · · , ′ ) ∉ I( ), we have ′ +1 = 0 ≤ + − 1/ . In the following, weassume ( 1 ′, · · · , ′ ) ∈ I( ).  en ′ +1 = ( , ( 1 ′, · · · , ′ )). Suppose ′ +1 > + −1/ for contradiction. We have

′

- (24) +1 = ( , ( 1 ′, · · · , ′ )) > + − 1/ .

In addition, let ( 1, · · · ,  ) ∼ ( , ( 1, · · · ,  )) be a set of events such that P ∩ ∈[ ] = . By Theorem 1.2, such events ( 1, · · · ,  ) exist. Let 1, · · · ,  be independent random variables drawn from [0,1] uniformly where { 1, · · · ,  } are independent of { 1, · · · ,  }. For each ∈ [ ], let ′ be the event that happens and ≤ ′ / .  us, for each ∈ [ ] we have

![image 96](<2018-he-quantum-lov-local-lemma_images/imageFile96.png>)

- (25) P( ′ ) = P( ) ·

′

![image 97](<2018-he-quantum-lov-local-lemma_images/imageFile97.png>)

= ′ , P( \ ′ ) = P( ) − P( ′ ) = − ′ .

In addition, one can verify that ( ′1, · · · , ′ ) ∼ ( , ( 1, · · · ,  )). Combining with ( 1 ′, · · · , ′ ) ∈ I( ) and Theorem 1.2, we have

- (26) P


# ∈ [1 − −  , 1 − ] ≥ P R

P R

∈

∈

′ ≥ , 1 ′, · · · , ′ .

![image 98](<2018-he-quantum-lov-local-lemma_images/imageFile98.png>)

∈[ ]

 us, we have

P

![image 99](<2018-he-quantum-lov-local-lemma_images/imageFile99.png>)

∈[ ]

(by the inclusion–exclusion principle ) ≥ P

![image 100](<2018-he-quantum-lov-local-lemma_images/imageFile100.png>)

# ′ − P

∈[ ]

∈[ ]

\ ′

(by the union bound ) ≥ P

![image 101](<2018-he-quantum-lov-local-lemma_images/imageFile101.png>)

′ −

∈[ ]

P \ ′

∈[ ]

(by (26) and (25)) ≥ , 1 ′, · · · , ′ −

2

1

(by (24) and (18)) > + −

−

![image 102](<2018-he-quantum-lov-local-lemma_images/imageFile102.png>)

![image 103](<2018-he-quantum-lov-local-lemma_images/imageFile103.png>)

∈[ ]

− ′

by =

2 + 1

![image 104](<2018-he-quantum-lov-local-lemma_images/imageFile104.png>)

≥

![image 105](<2018-he-quantum-lov-local-lemma_images/imageFile105.png>)

![image 106](<2018-he-quantum-lov-local-lemma_images/imageFile106.png>)

 at is, P ∩ ∈[ ] > , which is contradictory with P ∩ ∈[ ] = . In summary, we always have ≤ +1 ≤ + .

In the next, we show the claim that there is some ′ = ( 1 ′, · · · , ′ ) where ′ ≤ 8 ·4 for each ∈ [ ] such that the random instance of the se ing ( ′ , ′, ′) spans the whole space. At ﬁrst, we

prove ′ ∉ I( ′ ). If ( 1 ′, · · · , ′ ) ∈ I( ), we have ′ +1 = ( , ( 1 ′, · · · , ′ )).  us, by Deﬁnition 1.1 we have

(−1)| |

(−1)| |

′ = − ′ +1 +

( ′ , ′) =

∈Ind( ′ )

∈

∈Ind( )

= − ( , ( 1 ′, · · · , ′ )) + ( , ( 1 ′, · · · , ′ )) = 0.

∈

′

Combining with Lemma 3.2, we have ′ ∉ I( ′ ). If ( 1 ′, · · · , ′ ) ∉ I( ), we have ′ +1 = 0 and then ′ = ( 1 ′, · · · , ′ , 0). Combining with ( 1 ′, · · · , ′ ) ∉ I( ) and the deﬁnition of ′ , we also have

′ = ( 1 ′, · · · , ′ , 0) ∉ I( ′ ).

Let be the minimum positive integer such that ′ is an integer for each ∈ [ + 1]. We show that

- (27) ∈[ +1]


≤ 2

By (18), we have ≤ for each ∈ [ ]. In the next, we show +1 ≤ .  en (27) is immediate. If ( 1 ′, · · · , ′ ) ∈ I( ), we have ′ +1 = ( , ( 1 ′, · · · , ′ )). Combining with Deﬁnition 1.1 we have

′

+1 = ( , ( 1 ′, · · · , ′ )) =

(−1)| |

∈Ind( )

∈

max {⌊ − 1⌋ , 0}

∈[ ]\

 .

Combining with is an integer, we have ′ +1 is also an integer. If ( 1 ′, · · · , ′ ) ∉ I( ), we have

′

+1 = 0, then ′ +1 is also an integer.  us, we always have +1 ≤ . Combining with ≤ for each ∈ [ ], (27) is proved.

If ( 1 ′, · · · , ′ +1) ∈ (0, 1] +1, combining ′ ∉ I( ′ ), (27) with Theorem 3.2 (a), we have the there is some ′ = ( 1 ′, · · · , ′ ) where

′ ≤

∈[ +1]

4 +1 ≤ 2 ·4( +1) = 8 ·4

for each ∈ [ ] such that the random instance of the se ing ( ′ , ′, ′) spans the whole space. If

′ = 0 for some ∈ [ + 1], by applying Theorem 3.2 (a) to the subgraph of ′ induced by the le  vertices { ∈ [ + 1] | ′ > 0} and the right vertices [ ], one can also verify that such ′ exists.  en the claims are proved and the theorem is immediate.

4. CLLL: B      S      ’  B     In this section, we study the interior of commuting LLL.

- Deﬁnition 4.1 (Commuting Interior).  e commuting interior of an interaction bipartite graph =

([ ], [ ],   ), denoted by I ( ), is the set {rational ∈ [0, 1) : R ∈ < 1 for any commuting subspace set ∼ with R( ) = }.

 e following is a basic property of the commuting interior. Proposition 4.1. If ∈ I ( ), then ′ ∈ I ( ) for any rational ′ ≤ . Proof. Without loss of generality, we assume that ′ = ( 1 −  , 2, · · · ,  ). By contradiction, suppose that there exists a commuting subspace set ′ ∼ with R( ′) = ′ such that R ′∈ ′

′ = 1. In the following, we will construct another commuting subspace set ∼ with R( ) = such that R ∈ = 1, which is contradicted to the condition ∈ I ( ).

W.l.o.g., we assume the edge (1, 1) exists in . Since and ′ are both rational vectors, 1− ′

![image 107](<2018-he-quantum-lov-local-lemma_images/imageFile107.png>)

1

is a rational number. Suppose 1− ′

![image 108](<2018-he-quantum-lov-local-lemma_images/imageFile108.png>)

1

= where and are integers. Let H1′, · · · , H′ denote the qudits that

![image 109](<2018-he-quantum-lov-local-lemma_images/imageFile109.png>)

′ = { 1 ′, · · · , ′ } acts on. Deﬁne H1 = H1′ ⊗H 1 where dim (H 1) = , and H = H′ for any 2 ≤ ≤ . We construct a subspace set = { 1, · · · ,  } acting on the qudits H1, · · · , H as follows. Deﬁne

1 = 1 ′ ⊗ H 1 + H′[ ] ⊗ where is an arbitrary -dimensional subspace of H 1. For each 2 ≤ ≤ , let = ′ ⊗ H 1. We can easily check that is commuting, R( ) = , and R ∈ = 1.

As shorthand, we write I( ) for I( ( )). According to  eorem 1 in [29] (see also  eorem

- 3.1), I contains all rational vectors in the Shearer’s bound.  at is, for any rational , if ∈ I( ), then ∈ I ( ). Here, we particularly care about whether I ( ) ⊆ I( ), i.e., whether Shearer’s bound is tight for CLLL.

Deﬁnition 4.2 (Gap). An interaction bipartite graph is called gapless for CLLL if I ( ) ⊆ I( ), otherwise it is called gapful. Similarly, we can also deﬁne gapless/gapful for VLLL. We do not mention “for CLLL” or “for VLLL” if it is clear from context.

 e rest of Section 4 is organized as follows. Section 4.1 shows that CLLL equals VLLL on a large class of bipartite graphs. Section 4.2 provides a suﬃcient and necessary condition for gap existence. Section 4.3 develops a set of reduction rules for inferring gap existence of a bipartitegraph from known ones. Finally, based on these results, Section 4.4 provides an almost complete characterization of gapless/gapful bipartite graphs.

- 4.1. Solitary  dits Are Classical.  e main result of this subsection is  eorem 4.2, which says that solitary qudits can be restricted to be classical without changing the interior. As a corollary, for


- Deﬁnition 4.3 (Solitary  dits). Given an interaction bipartite graph = ([ ], [ ],   ), we say a right vertex ∈ [ ] is solitary if for any 1, 2 ∈ N ( ) we have N ( 1) ∩ N ( 2) = { }.
- Deﬁnition 4.4 (Classical  dits). Let H be a qudit and {|ℓ : ℓ ∈ [ ]} be its computational basis. H is said to be classical if every Hamiltonian commutes with |ℓ ℓ| for any ℓ ∈ [ ].


where all right vertices are solitary, the interior of CLLL equals that of VLLL ( eorem 4.5).

 eorem 4.2. Given an interaction bipartite graph = ([ ], [ ],   ), if there exists a commuting subspace set ∼ spanning the whole space, then there exists another commuting subspace set ′ ∼ with R( ′) = R( ) spanning the whole space and satisfying that for each solitary ∈ [ ], H is classical.

 e idea of  eorem 4.2 is to dissect the structure of commuting local Hamiltonians by using Bravyi and Vyalyi’s Structure Lemma [6].

- Lemma 4.3 (Structure Lemma, adapted from [6]). Suppose X, Y, Z are complex Euclidean spaces, Π and Π are projection operators acting on X ⊗ Y and Y ⊗ Z respectively. If Π and Π commute, then Y can be decomposed to some orthogonal subspaces Y = ℓ Yℓ = ℓ Yℓ1 ⊗ Yℓ2 such that for any ℓ:


- (1) Π and Π preserve Yℓ;


- (2) Restricted to Yℓ, Π and Π act non-trivially only on Yℓ1 and Yℓ2 respectively.


In other words, can be decomposed as = ℓ ℓ ⊗Yℓ2 where ℓ ⊆ X ⊗Yℓ1, and can be decomposed as = ℓ ℓ ⊗ Yℓ1 where ℓ ⊆ Yℓ2 ⊗ Z.

 e following lemma will be also used in the proof of  eorem 4.2.

Lemma 4.4. Suppose X1, Y1, X2, and Y2 are complex Euclidean spaces. 1 is a subspace of X1 ⊗ Y1 satisfying that 1 1 ⊗ Y1 for any nonempty subspace 1 ⊆ X1. 2 is a subspace of X2 ⊗Y2 satisfying that 2 2 ⊗Y2 for any nonempty subspace 2 ⊆ X2.  en 1 ⊗X2 ⊗Y2+ 2 ⊗X1⊗Y1 ⊗Y1 ⊗Y2 for any nonempty subspace ⊆ X1 ⊗ X2.

Proof. We ﬁrst introduce some notations. For a vector | ∈ X ⊗ Y, we deﬁne X (|  ) as the span of its Schmidt bases for X. In other words, if | = | ⊗ | is the Schmidt decomposition, then

X (|  ) = Span(|1 , |2 , · · · ). For asubspace ⊆ X ⊗Y, wedeﬁne X ( ) := Span( X (|  ) : | ∈ ) as the span of X (|  ) over all | ∈ . Claim. ⊗ Y for any nonempty subspace ⊆ X if and only if X ( ⊥) = X. Proof. ⇐=: Suppose that ⊇ ⊗ Y for some nonempty ⊆ X.  en ⊥ ⊆ ⊥ ⊗ Y and X (|  ) ⊆

⊥ for any | ∈ ⊥. So X ( ⊥) ⊆ ⊥ X.

=⇒: Suppose X ( ⊥) ⊆ ⊥ for some nonempty ⊆ X.  en X (|  ) ⊆ ⊥ for any | ∈ ⊥. Obviously, we have ⊥ ⊆ ⊥ ⊗ Y, which implies that ⊇ ⊗ Y.

Note that ( 1⊗X2⊗Y2+ 2 ⊗X1⊗Y1)⊥ = 1 ⊥⊗ 2 ⊥.  en it is easy to check that X1⊗X2( 1 ⊥⊗ 2 ⊥) =

X1( 1 ⊥) ⊗ X2( 2 ⊥), which is X1 ⊗X2 according to the above claim. Finally, we can conclude the proof by applying the above claim again.

- Proof of  eorem 4.2. Fix an arbitrary solitary ∈ [ ] and w.l.o.g. assume N ( ) = [ ]. Let H1, · · · , H denote the qudits that = { 1, · · · ,  } acts on. By applying Lemma 4.3 iteratively, we decompose


H to some orthogonal subspaces H = ℓ H ℓ = ℓ H ℓ1 ⊗ H ℓ2 ⊗ · · · ⊗ H ℓ  such that: for each ∈ [ ], can be decomposed as

=

ℓ

 ℓ =

ℓ

∗

 ℓ ⊗

′≠

H ℓ ′ ⊗ H[ ]\N( )

where  ℓ ∗ ⊆ HN( )\{ } ⊗H ℓ . Furthermore, we can always decompose  ℓ ∗ to two orthogonal subspaces

 ℓ =  ℓ, ∗ 1 ⊕  ℓ, ∗ 2 such that

∗

- (i)  ℓ, ∗ 1 = ⊗ H ℓ  for some nonempty subspace ⊆ HN( )\{ }, and
- (ii)  ℓ, ∗ 2 ⊗ H ℓ  for any nonempty subspace ⊆ HN( )\{ }.


We deﬁne

 ℓ,1 :=  ℓ, ∗ 1 ⊗

′≠

H ℓ ′ ⊗ H[ ]\N( ) and  ℓ,2 :=  ℓ, ∗ 2 ⊗

′≠

H ℓ ′ ⊗ H[ ]\N( ).

Weconstruct asubspace set ′ = { 1 ′, · · · , ′ } ∼ asfollows. Foreach ∈ [ ], deﬁne ′ = ℓ  ℓ,1. For each ∉ [ ], deﬁne ′ = . Note that restricted to H ℓ,  ℓ,1 acts non-trivially only on the qudit HN( )\{ }.  us ′ uses H as a classical variable (rotate the computational basis if needed).

and ′

Claim. ′

commute for any 1, 2 ∈ [ ]. Proof. We only need to prove the claim in the following two cases.

2

1

Case I: 1 ≠ 2 ∈ [ ]. It suﬃces to show that 1ℓ1,1 and 2ℓ2,1 commute for any ℓ1 and ℓ2. If ℓ1 ≠ ℓ2, then 1ℓ1,1 ⊆ H ℓ1 ⊗ H[ ]\{ } and 2ℓ2,1 ⊆ H ℓ2 ⊗ H[ ]\{ } are orthogonal and thus commute. If ℓ1 = ℓ2 = ℓ, then restricted to H ℓ, 1ℓ,1 and 2ℓ,1 act non-trivially on HN( 1)\{ } and HN( 2)\{ } respectively. Noticing that (N ( 1) \ { }) ∩ (N ( 1) \ { }) = ∅ since is solitary, we have that 1ℓ,1 and

2ℓ,1 commute.

Case II: 1 ∈ [ ] and 2 ∉ [ ]. Let Πℓ, Π 1ℓ, and Π 1ℓ,1 denote the projectors on H ℓ ⊗ H[ ]\{ }, 1ℓ, and 1ℓ,1 respectively. Noting that Π 1ℓ = Π

· Πℓ and Πℓ acts non-trivially only on the qudit H , we have

1

Π 1ℓ · Π

· Πℓ · Π

· Π

· Πℓ = Π

· Π

· Πℓ = Π

· Π 1ℓ, i.e., Π 1ℓ and Π

# = Π

# = Π

2

1

2

1

2

2

1

2

commute. Let {|  } denote the computational basis of H ℓ 1. A key observation is that Π 1ℓ,1 is the product of |Π 1ℓ|  ⊗id over all | ’s, where id denotes the identity operator on H ℓ 1. Since Π 1ℓ and Π

2

.  en Π 1ℓ,1 also commutes with Π

commute, every |Π 1ℓ| ⊗ id commutes with Π

2

2

.  us Π ′

= ℓ Π 1ℓ,1 and Π ′

commute.

# = Π

2

2

1

2

Claim. ′ spans the whole space. Proof. Let  ℓ be the subspace of HN( )\{ } such that  ℓ, ∗ 1 =  ℓ ⊗H ℓ . For simplicity of notations, we let

∗ ⊗ H[ ]\(N( )∪{ }),

 ℓ ⊗ H[ ]\N( ) +

ℓ =

∉[ ]

∈[ ]

Note that =1 ′ = ℓ ℓ ⊗ H ℓ and =1 = ℓ ℓ ⊗ H ℓ + =1  ℓ,2 .

By contradiction, we assume that ′ does not span the whole space, i.e., there exists some ℓ such that ℓ H[ ]\{ }. In the nextparagraph, we willshow that ℓ⊗H ℓ and =1  ℓ,2 commute.  en, because ℓ ⊗ H ℓ + =1  ℓ,2 = H[ ]\{ } ⊗ H ℓ, we have =1  ℓ,2 ⊇ ℓ ⊥ ⊗ H[ ]\{ }. However, as {  ℓ,2} =1 act

non-trivially on disjoint qudits, by applying Lemma 4.4 iteratively, we have that =1  ℓ,2 ⊗ H ℓ for any nonempty subspace ⊆ H[ ]\{ }. A contradiction.

To show that ℓ ⊗ H ℓ and =1  ℓ,2 commute, it suﬃces to show that for any ∈ [ ] and ′ ∈ [ ],

- (a) ′ℓ ⊗ H[ ]\N( ′) commute with  ℓ,2 if ′ ∈ [ ]; and
- (b) ∗ ′ ⊗ H[ ]\(N( ′)∪{ }) commute with  ℓ,2 if + 1 ≤ ′ ≤ .


Case (a) is obvious because restricted to H ℓ, ′ℓ ⊗ H[ ]\N( ′) and  ℓ,2 act non-trivially on disjoint set of qudits, namely HN( ′)\{ } ⊗ H ℓ ′ and HN( )\{ } ⊗ H ℓ  respectively. For Case (b), the proof of the previous claim presents that both  ℓ and  ℓ,1 commute with ′ for any ≤ ′ ≤ . So  ℓ,2 also commutes with ′, as  ℓ,2 is the orthogonal complement of  ℓ,1 in  ℓ. Let Πℓ denote the projector on H ℓ ⊗ H[ ]\{ }, then the projector projecting on ∗ ′ ⊗ H[ ]\(N( ′)∪{ }) is Π ′Πℓ. Now it is obvious that

∗ ′ ⊗ H[ ]\(N( ′)∪{ }) and  ℓ,2 commute by noting that Πℓ and  ℓ,2 commute.

Note that R( ′) may be smaller than R( ). We can easily address this problem while keeping H

still classical by playing the trick used in the proof of Proposition 4.1. Finally, we apply the above procedure to each solitary qudits one by one in an arbitrary order. It is straightforward to verify that a classical qudit keeps classical when applying the above procedure to other solitary qudits. Finally, all solitary qudits will be classical.

 e following theorem is an immediate corollary of  eorem 4.2.

-  eorem 4.5. For any interaction bipartite graph where all the right vertices are solitary, I ( ) is the set consisting of all rational vectors in I ( ).


In particular, if is a cycle of length at least 6, i.e., is isomorphic to a bipartitegraph ([ℓ], [ℓ],  ℓ) where ℓ = {( , ), ( ,  + 1) : ∈ [ℓ − 1]} ∪ {(ℓ, ℓ), (ℓ, 1)} and ℓ ≥ 3, then is gapful for VLLL [15]. By  eorem 4.5, is also gapful for CLLL.

- 4.2. A Suﬃcient and Necessary Condition for Gap Decision.  e main result of this subsection is  eorem 4.6, a suﬃcient and necessary condition for deciding whether Shearer’s bound is tight for CLLL on a given interaction bipartite graph.  eorem 4.6 enables to decide whether a gap existence withoutcomputing the Shearer’s bound. In particular,  eorem 4.6 will be used in the proof of  eorem 4.10, which is about reduction rules.


- Deﬁnition 4.5 ( antum Exclusiveness). A subspace set = { 1, · · · ,  } is called exclusive with respect to an interaction bipartite graph , if ∼ and ⊥ ′ for any edge ( , ′) in the base graph. We will omit “with respect to ” if it is clear from the context. Note that an exclusive subspace set must be commuting.


-  eorem 4.6. Given a connected interaction bipartite graph , the following two conditions are equivalent:


- (a) For any rational ∈ I ( ), there is an exclusive subspace set with interaction bipartite graph and relative dimension vector .
- (b) is gapless for CLLL.


 eorem 4.6 is in fact a leveraging of  eorem 5 in [15], which is for VLLL, to CLLL.  e following two lemmas, Lemma 4.7 and 4.8, about exclusive classical event sets will be used.

- Deﬁnition 4.6 (Classical exclusiveness). A classical event set is said to be exclusive with respect to a graph , if is a dependency graph of and P( ∩ ′) = 0 for any edge ( , ′) in . We do not mention “with respect to ” if it is clear from context.


 e abstract boundary of a graph , denoted by ( ), is the set { : (1 − ) ∈ I( ) and (1 + ) ∉ I( ) for any ∈ (0, 1)}.

- Lemma 4.7 ( eorem 1 in [32]). Given a graph and ∈ I( ) ∪ ( ). Among all event sets ∼ with P( ) = , there is an exclusive one such that P(∪ ∈ ) is maximized.
- Lemma 4.8 (Lemma 29 in [15]). Suppose that is a dependency graph of event sets and , P( ) =

P( ), and is exclusive.  en P(∪ ∈ ) ≥ P(∪ ∈ ). Moreover, when is connected, the equality holds if and only if is exclusive.

 e following basic fact about quantum exclusiveness will also be used.

- Lemma 4.9. Given an interaction bipartite graph = ([ ], [ ],   ) and a rational vector ∈ [0, 1) , if there is an exclusive subspace set ∼ with R( ) = , then for any rational ′ ≤ , there is an exclusive subspace set ′ ∼ with R( ′) = ′.


Proof. Without loss of generality, we assume that ′ = ( 1 −  , 2, · · · ,  ) and the edge (1, 1) exists in

. Since ′ and are both rational, so is / 1. Suppose / 1 = / where and are integers. Let H1, · · · , H be the qudits that = { 1, · · · ,  } acts on. Deﬁne H1′ = H1 ⊗ H 1 where dim (H 1) = , and H′ = H for any ≥ 2. We construct a subspace set ′ = { 1 ′, · · · , ′ } acting on the qudits H1′, · · · , H′ as follows. Let 1 ′ = 1 ⊗ where is an arbitrary ( − )-dimensional subspace of H 1. For each ≥ 2, let ′ = ⊗H 1. One can easily check that ′ ∼ , R( ′) = ′, and ′ is exclusive.

Now, we are ready to prove  eorem 4.6. Proof of  eorem 4.6. Let denote the base graph of . ( ) ⇒ ( ): Given any rational ∈ I ( ), suppose there is an exclusive subspace set ∼

![image 110](<2018-he-quantum-lov-local-lemma_images/imageFile110.png>)

with R( ) = . Because ∈ I ( ), we have R( ∈ ) < 1. In the following, we will construct an exclusive classical event set with dependency graph and P( ) = such that P(∪ ∈ ) = R( ∈ ) < 1. By Lemma 4.8, we have P(∪ ∈ ) < 1 for every event set ∼ with P( ) = .  us ∈ I( ), which concludes the proof of this direction.

 e event set = ( 1, · · · ,  ) is constructed as follows. Because is commuting, 1, · · · ,  can be diagonalized with respect to the same orthonormal basis, denoted by {| ℓ : ℓ ∈ [ ]}. Let (Ω, F, P) be a probability space where Ω = {| ℓ : ℓ ∈ [ ]}, F = 2Ω, and P(|  ) = 1/ for each . Deﬁne

= {| ℓ : | ℓ ∈ }. Obviously, P( ) = R( ) and P(∪ ∈ ) = R( ∈ ) < 1. Moreover, for any ∈ [ ] and ⊆ [ ] \ (N ( , ) ∪ { }), we have P( ∩ (∪ ′∈ ′)) = R( ∩ ( ′∈ ′)) = R( ) · R( ′∈ ′) = P( ) · P(∪ ′∈ ′), thus is independent with { ′ : ′ ∉ N ( , ) ∪ { }}. So

( ) is a dependency graph of . Finally, for any edge ( , ′) in , P( ∩ ′) = R( ∩ ′) = 0, thus is exclusive.

( ) ⇒ ( ): We assume that is gapless, i.e., I ( ) ⊂ I( ). Given a rational ∈ I ( ), choose an arbitrary rational vector ∈ ( ) satisfying that ≥ . As ( ) ∩I( ) = ∅ and I ( ) ⊂ I( ), it has that ∉ I ( ). By Deﬁnition 4.1, there exists a commuting subspace set ∼ with R( ) =

![image 111](<2018-he-quantum-lov-local-lemma_images/imageFile111.png>)

such that R ( ∈ ) = 1. In the following, we will show that is exclusive, which then concludes the proof by  eorem 4.9.

We deﬁne a classical event set = { 1, · · · ,  } corresponding to as in the proof of the direction ( ) ⇒ ( ). By Lemma 4.7, there is an exclusive event set ∼ with P( ) = . Because is connected and P(∪ ∈ ) = R( ∈ ) = 1 ≥ P(∪ ∈ ), we have that is exclusive by Lemma 4.8. Finally, noticing that ⊥ ′ if and only if P( ∩ ′) = 0, we conclude that is exclusive.

- 4.3. Reduction Rules. To infer gap existence of a bipartitegraph from known ones, a set of reduction rules are established for VLLL [15]. With these reduction rules, various bipartite graphs are shown to be gapful/gapless for VLLL. In this subsection, we leverage these reduction rules to CLLL.


Weconsiderthefollowingsixtypesofoperationsonaninteractionbipartitegraph = ([ ], [ ],   ).

- • Delete- -Leaf: Delete a vertex ∈ [ ] on the right side with |N ( )| ≤ 1, and remove the incident edge if any.
- • Duplicate- -Vertex: Given a vertex ∈ [ ] on the le  side, add a vertex ′ to the le  side, and add edges incident to ′ so that N ( ′) = N ( ).
- • Duplicate- -Vertex: Given a vertex ∈ [ ] on the right side, add a vertex ′ to the right side, and add some edges incident to ′ so that N ( ′) ⊆ N ( ).
- • Delete-Edge: Delete an edge from provided that the base graph remains unchanged.
- • Delete- -Vertex: Delete a vertex ∈ [ ] on the le  side, and remove all the incident edges.
- • Delete- -Leaf: Delete a vertex ∈ [ ] on the le  side with |N ( )| ≤ 1, and remove the incident edge if any.


 e following theorem summarizes how these operations inﬂuence the existence of gaps.

-  eorem 4.10. Given an interaction bipartite graph = ([ ], [ ],   ), we have


- (a) if is gapful for CLLL, then it remains gapful a er applying Delete-Edge;
- (b) if is gapless for CLLL, then it remains gapless a er applying Delete- -Vertex;
- (c) is gapful if and only it is gapful a er applying Delete- -Leaf, Duplicate- -Vertex, Duplicate-


-Vertex, or Delete- -Leaf;

Proof.  roughout this proof, we only consider bipartite graphs which are connected.  is restriction does not lose generality for the following reason.  e abstract interior (and commuting interior respectively) of a disconnected bipartite graph is exactly the direct product of the abstract interiors (and commuting interior respectively) of its connected components, which are also bipartite graphs. So a bipartite graph is gapless if and only if each of its connected component is gapless.

- Part (a). Let ′ be the bipartite graph obtained from a er applying Delete-Edge. Because the base graph is unchanged, I( ) = I( ′ ). Moreover, it is obvious that I ( ′ ) ⊆ I ( ). So Part (a) is immediate by Deﬁnition 4.2.

![image 112](<2018-he-quantum-lov-local-lemma_images/imageFile112.png>)

- Part (b). W.l.o.g., we delete the le  vertex from and obtain a bipartite graph ′ . Let and ′


![image 113](<2018-he-quantum-lov-local-lemma_images/imageFile113.png>)

denote the base graphs of and ′ respectively. A key observation is that ( ′ , ) ≡ , ( , 0) . So I( ′ ) = { ∈ I( ) : = 0}. Moreover, it is easy to see that I ( ′ ) = { ∈ I ( ) : = 0} by Deﬁnition 4.1. Now, Part (b) is obvious.

Part (c). Duplicate-R-Vertex: Trivial, because both the abstract interior and commuting interior remain unchanged a er applying Duplicate-R-Vertex.

![image 114](<2018-he-quantum-lov-local-lemma_images/imageFile114.png>)

Duplicate-L-Vertex: W.l.o.g., we duplicate the le  vertex and obtain a bipartite graph ′ .  at is,

′ = ([ +1], [ ],  ′ ) where ′ = ∪{( +1, ) : ∈ N ( )}. Let and ′ denote the base graphs of and ′ respectively. Itis straightforwardtoverifythat ( ′ , ) ≡ ( , ( 1, · · · ,  −1,  + +1)). So I( ′ ) = { : ( 1, · · · ,  −1,  + +1) ∈ I( )}. Moreover, it is easy to see that I ( ′ ) = { : ( 1, · · · ,  −1,  + +1) ∈ I ( )} by Deﬁnition 4.1.  en this case is obvious.

Delete- -Leaf: W.l.o.g., suppose that the vertex on the right side satisﬁes that |N ( )| ≤ 1.  e nontrivial case is when |N ( )| = 1. W.l.o.g., we assume N ( ) = { }. Furthermore, as is connected, the le  vertex has at least two incident edges, and we assume the edge ( ,  − 1) exists in without loss of generality. Let ′ = ([ ], [ − 1],  ′ }) denote the bipartite graph obtained from by deleting the vertex and its incident edge ( , ). On one hand, since ′ can be obtained from by applying Delete-Edge and then deleting the isolated right vertex , so according to Part (a), if is gapful, then so is ′ . On the other hand, let ′′ = ([ ], [ ],  ′′ ) be another bipartite graph where

′′ = ∪ {( , ) : ∈ N ( − 1)}. Because can be obtained from ′′ by applying Delete-Edge

operations, so according to Part (a), if is gapless, then so is ′′ . Moreover, ′′ can be obtained from ′ by applying Duplicate- -Vertex, so if ′′ is gapless, then so is ′ .

Delete- -Leaf: W.l.o.g., suppose that the vertex on the le  side satisﬁes that |N ( )| ≤ 1.  e nontrivial case is when |N ( )| = 1. W.l.o.g., we assume N ( ) = { } and let ′ = ([ − 1], [ ],  ′ }) denote the resulted bipartite graph a er removing the vertex and its incident edge ( , ). Besides, we assume N ( , ) = {1, 2, · · · , , }. As is connected, we have ≥ 1.

′ is gapless ⇒ is gapless: Given any rational = ( 1, · · · ,  ) ∈ I ( ), we will construct an exclusive ∼ , which implies is gapless by  eorem 4.6. Deﬁne

′ = 1 1 −

, 2 1 −

,  +1, · · · ,  −1 . We claim that ′ ∈ I ( ′ ). By contradiction, suppose that ′ ∉ I ( ′ ). As ′ is rational, there is a

, · · · ,

![image 115](<2018-he-quantum-lov-local-lemma_images/imageFile115.png>)

![image 116](<2018-he-quantum-lov-local-lemma_images/imageFile116.png>)

![image 117](<2018-he-quantum-lov-local-lemma_images/imageFile117.png>)

1 −

commuting subspace set ′ ∼ ′ with R( ′) = ′ satisfying R ∈[ −1] ′ = 1. Let H1′ ⊗ · · · ⊗ H′ denote the qudits that ′ acts on. We construct a commuting subspace set ∼ as follows. Suppose

1 − = / where and are integers. Let H = H′ ⊗ H where dim (H ) = , and H′ = H for any ∈ [ − 1]. Pick an arbitrary -dimensional subspace of H and let

- • = ′ ⊗ for each ∈ [ ],
- • = ′ ⊗ H for each < ≤ − 1, and
- • = ⊥ ⊗ =1 H′ .


It is easy to verify that is commuting, ∼ , R ∈[ ] = 1, and R( ) = . So ∉ I ( ). A contradiction.

Because ′ ∈ I ( ′ ) and ′ is gapless, according to  eorem 4.6, there is an exclusive subspace set

′ ∼ ′ where R( ′) = ′. We construct from ′ as above. It is easy to verify that ∼ , R( ) = , and is exclusive.

is gapless ⇒ ′ is gapless: Notethat ′ can beobtainedfrom by applying the Delete-L-Vertex (deleting the le  vertex ). So ′ is gapless according to Part (b).

With these reductionrules, it is easy to see all trees are gapless, including 1-D chains [26] and regular trees [32, 17, 7, 29].

-  eorem 4.11. An interaction bipartite graph is gapless for CLLL if it is a tree.

Proof. Suppose = ([ ], [ ],   ) is a tree. We can obtain the bipartite graph ([1], [1], {(1, 1)}) from

by applying Delete- -Leaf or Delete- -Leaf repeatedly. Obviously, ′ is gapless. So is also gapless according to  eorem 4.10.

4.4. An Almost Complete Characterization of Gap Existence. In this subsection, we prove  eorem 4.12, which gives an almost complete characterization of gap existence except when the base graph has only 3-cliques.

-  eorem 4.12. Given an interaction bipartite graph , is gapless for CLLL if its base graph is a tree, and gapful for CLLL if its base graph has an induced cycle of length at least 4.


Proof. Let denote the base graph of . If is a tree, then is gapless for VLLL by  eorem 6 in [15], so it is also gapless for CLLL.

Suppose has an induced cycle of length at least 4. W.l.o.g., we assume the induced subgraph of

on [ℓ], where ℓ ≥ 4, is a cycle ([ℓ],   ) where = {( ,  + 1) : ∈ [ℓ − 1]} ∪ {(ℓ, 1)}. We apply Delete- -Vertex on to delete all le  vertices not in [ℓ] and then apply Delete- -Leaf to delete all right vertices whose degree are at most 1, then we obtain a bipartite graph ′ = ([ℓ], , ′ ) such that for any ∈ , either N ( ′ , ) = { ,  + 1} for some ∈ [ℓ − 1] or N ( ′ , ) = {ℓ, 1}. So all ∈ are solitary. Moreover, by  eorem 7 in [15], such ′ is gapful for VLLL, so ′ is also gapful for CLLL according to  eorem 4.5. Finally, we can conclude is gapful for CLLL according to  eorem 4.10 (b) and (c).

A              

We are grateful to Andras Gily´ en for his manuscript´ about VLLL and telling us the problem whether Shearer’s bound is tight for QLLL. We also thank the anonymous referees for their valuable comments.

R         

- [1] Dorit Aharonov and Lior Eldar. On the complexity of commuting local hamiltonians, and tight conditions for topological order in such systems. In Foundations of Computer Science (FOCS), 2011 IEEE 52nd Annual Symposium on, pages 334–343. IEEE, 2011.
- [2] Dorit Aharonov, Oded Kenneth, and Itamar Vigdorovich. On the complexity of two dimensional commuting local hamiltonians. In 13th Conference on the  eory of  antum Computation, Communication and Cryptography, TQC 2018, July 16-18, 2018, Sydney, Australia, volume 111, pages 2:1–2:21, 2018.
- [3] Andris Ambainis, Julia Kempe, and Or Sa ath. A quantum Lovasz´ local lemma. Journal of the ACM (JACM), 59(5):24, 2012.
- [4] Sergey Bravyi. Eﬃcient algorithm for a quantum analogue of 2-sat. Contemporary Mathematics, 536:33–48, 2011.
- [5] Sergey Bravyi, Cristopher Moore, and Alexander Russell. Bounds on the quantum satisﬁability threshold. In Innovations of Computer Science, pages 482–489, 2010.
- [6] Sergey Bravyi and Mikhail Vyalyi. Commutative version of the local hamiltonian problem and common eigenspace problem.  antum Information & Computation, 5(3):187–215, 2005.
- [7] Ma hew Coudron and Ramis Movassagh. Unfrustration condition and degeneracy of qudits on trees. arXiv preprint arXiv:1209.4395, 2012.
- [8] Toby S. Cubi  and Martin Schwarz. A constructive commutative quantum Lovasz´ local lemma, and beyond. Eprint Arxiv, 2012.
- [9] Paul Erdos and L˝ aszl´ o Lov´ asz.´ Problems and results on 3-chromatichypergraphs and some related questions. Inﬁnite and ﬁnite sets, 10(2):609–627, 1975.
- [10] Heidi Gebauer, Robin A Moser, Dominik Scheder, and Emo Welzl.  e Lovasz´ local lemma and satisﬁability. In Eﬃcient Algorithms, pages 30–54. Springer, 2009.
- [11] Heidi Gebauer, Tibor Szabo,´ and Gabor´ Tardos.  e local lemma is asymptotically tight for SAT. Journal of the ACM (JACM), 63(5):43, 2016.
- [12] Andras´ Gilyen´ and Or Sa ath. On preparing ground states of gapped hamiltonians: An eﬃcient quantum lovasz´ local lemma. In 2017 IEEE 58th Annual Symposium on Foundations of Computer Science (FOCS), pages 439–450, 2017.
- [13] Ioannis Giotis, Le eris Kirousis, Kostas I Psaromiligkos, and Dimitrios M  ilikos. Acyclic edge coloring through the Lovasz´ local lemma.  eoretical Computer Science, 665:40–50, 2017.
- [14] Daniel Go esman and Sandy Irani.  e quantum and classical complexity of translationally invariant tiling and hamiltonian problems. In Foundations of Computer Science, 2009. FOCS’09. 50th Annual IEEE Symposium on, pages 95–104. IEEE, 2009.
- [15] Kun He, Liang Li, Xingwu Liu, Yuyi Wang, and Mingji Xia. Variable-version Lovasz´ local lemma: Beyond shearer’s bound. In 58th IEEE Annual Symposium on Foundations of Computer Science, FOCS 2017, Berkeley, CA, USA, October 15-17, 2017, pages 451–462, 2017.
- [16] Kun He, Qian Li, and Xiaoming Sun. Moser-tardos algorithm: Beyond shearer’s bound. CoRR, abs/2111.06527, 2021.
- [17] Ole J. Heilmann and Ellio  H. Lieb.  eory of monomer-dimer systems. Communications in Mathematical Physics, 25(3):190–232, 1972.
- [18] A Yu Kitaev. Fault-tolerant quantum computation by anyons. Annals of Physics, 303(1):2–30, 2003.
- [19] Kashyap Babu Rao Kolipaka and Mario Szegedy. Moser and tardos meet lovasz.´ In Proceedings of the forty-third annual ACM symposium on  eory of computing, pages 235–244. ACM, 2011.
- [20] C. R. Laumann, A. M. Lauchli,¨ R. Moessner, A. Scardicchio, and S. L. Sondhi. On product, generic and random generic quantum satisﬁability. Physical Review A, 81(6):359–366, 2010.
- [21] Chris Laumann, Roderich Moessner, Antonello Scardicchio, and Shivaji Sondhi. Phase transitions in random quantum satisﬁability. Bulletin of the American Physical Society, 54, 2009.


- [22] Colin McDiarmid. Hypergraph colouring and the Lovasz´ local lemma. Discrete Mathematics, 167:481–486, 1997.
- [23] Ankur Moitra. Approximate counting, the Lovasz local lemma, and inference in graphical models.´ In Proceedings ofthe 49th Annual ACM SIGACT Symposium on  eory of Computing, pages 356–369. ACM, 2017.
- [24] Siddhardh C. Morampudi and Chris R. Laumann. Many-body systems with random spatially local interactions. Physical Review B, 2019.
- [25] Robin A Moser and Gabor Tardos.´ A constructive proof of the general Lovasz local lemma.´ Journal of the ACM (JACM), 57(2):11, 2010.
- [26] Ramis Movassagh, Edward Farhi, Jeﬀrey Goldstone, Daniel Nagaj, Tobias J. Osborne, and Peter W. Shor. Unfrustrated qudit chains and their ground states. Physical Review A, 82(1):16279–16288, 2010.
- [27] Wesley Pegden. An extension of the moser–tardos algorithmic local lemma. SIAM Journal on Discrete Mathematics, 28(2):911–917, 2014.
- [28] Or Sa ath and Itai Arad. A constructive quantum Lovasz´ local lemma for commuting projectors.  antum Information & Computation, 15(11-12):987–996, 2015.
- [29] Or Sa ath, Siddhardh C. Morampudi, Chris R. Laumann, and Roderich Moessner. When a local hamiltonian must be frustration-free. Proceedings of the National Academy of Sciences, 113(23):6433–6437, 2016.
- [30] Norbert Schuch. Complexity of commuting hamiltonians on a square la ice of qubits.  antum Information & Computation, 11(11-12):901–912, 2011.
- [31] Martin Schwarz, Toby S Cubi , and Frank Verstraete. An information-theoretic proof of the constructive commutative quantum Lovasz´ local lemma. arXiv preprint arXiv:1311.6474, 2013.
- [32] James B Shearer. On a problem of spencer. Combinatorica, 5(3):241–245, 1985.
- [33] Joel Spencer. Asymptotic lower bounds for Ramsey functions. Discrete Mathematics, 20:69–76, 1977.


