## MOSER-TARDOS ALGORITHM: BEYOND SHEARER’S BOUND

KUN HE, QIAN LI, AND XIAOMING SUN

# arXiv:2111.06527v1[cs.DS]12Nov2021

A       . In a seminal paper (Moser and Tardos, JACM’10), Moser and Tardos developed a simple and powerful algorithm to nd solutions to combinatorial problems in the variable Lov´asz Local Lemma (LLL) seing. Kolipaka and Szegedy (Kolipaka and Szegedy, STOC’11) proved that the Moser-Tardos algorithm is ecient up to the tight condition of the abstract Lov´asz Local Lemma, known as Shearer’s bound. A fundamental problem around LLL is whether the ecient region of the Moser-Tardos algorithm can be further extended.

In this paper, we give a positive answer to this problem. We show that the ecient region of the

Moser-Tardos algorithm goes beyond the Shearer’s bound of the underlying dependency graph, if the graph is not chordal. Otherwise, the dependency graph is chordal, and it has been shown that Shearer’s bound exactly characterizes the ecient region for such graphs (Kolipaka and Szegedy, STOC’11; He, Li, Liu, Wang and Xia, FOCS’17).

Moreover, we demonstrate that the ecient region can exceed Shearer’s bound by a constant by explicitly calculating the gaps on several innite laices.

e core of our proof is a new criterion on the eciency of the Moser-Tardos algorithm which takes the intersection between dependent events into consideration. Our criterion is strictly beer than Shearer’s bound whenever the intersection exists between dependent events. Meanwhile, if any two dependent events are mutually exclusive, our criterion becomes the Shearer’s bound, which is known to be tight in this situation for the Moser-Tardos algorithm (Kolipaka and Szegedy, STOC’11; Guo, Jerrum and Liu, JACM’19).

1. I           

Suppose A = {𝐴1, · · · ,𝐴𝑚} is a set of bad events. If the events are mutually independent, then we can avoid all of these events simultaneously whenever no event has probability 1. Lov´asz Local Lemma (LLL) [EL75], one of the most important probabilistic methods, allows for limited dependency among the events, but still concludes that all the events can be avoided simultaneously if each individual event has a bounded probability. In the most general seing (a.k.a. abstract LLL), the dependency among A is characterized by an undirected graph 𝐺𝐷 = ([𝑚],𝐸𝐷), called a dependency graph of A, which satises that for any vertex 𝑖, 𝐴𝑖 is independent of {𝐴𝑗 : 𝑗 ∉ N𝐺𝐷 (𝑖) ∪ {𝑖}}. Here N𝐺(𝑖) stands for the set of neighbors of vertex 𝑖 in a given graph 𝐺.

We use A ∼ (𝐺𝐷,𝒑) to denote that (i) 𝐺𝐷 is a dependency graph of A and (ii) the probability vector of A is 𝒑. Given a graph 𝐺𝐷, dene the abstract interior I𝑎(𝐺𝐷) to be the set consisting of all vectors 𝒑 such that P ∩𝐴∈A𝐴 > 0 for any A ∼ (𝐺𝐷,𝒑). In this context, the most frequently used abstract LLL can be stated as follows:

eorem 1.1 ([Spe77]). Given any graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and any probability vector 𝒑 ∈ (0, 1]𝑚, if there exist real numbers 𝑥1, ...,𝑥𝑚 ∈ (0, 1) such that 𝑝𝑖 ≤ 𝑥𝑖 𝑗∈N𝐺

𝐷 (𝑖)(1 − 𝑥𝑗) for any 𝑖 ∈ [𝑚], then 𝒑 ∈ I𝑎(𝐺𝐷).

Shearer [She85] obtained the strongest possible condition for abstract LLL. Let Ind(𝐺𝐷) be the set of all independent sets of an undirected graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and 𝒑 = (𝑝1, · · · ,𝑝𝑚) ∈ (0, 1]𝑚. For each 𝐼 ∈ Ind(𝐺𝐷), dene the quantity

𝑞𝐼 (𝐺𝐷,𝒑) = ∑︁

### (−1)|𝐽 |−|𝐼|

𝑝𝑖.

𝐽 ∈Ind(𝐺𝐷),𝐼 ⊆𝐽

𝑖∈𝐽

(Kun He, Qian Li, and Xiaoming Sun) I         C         T         , C       A       S       , B      , C    . U             C       A          S       . B      , C    . E-mail: hekun.threebody@foxmail.com, liqian@ ict.ac.cn, and sunxiaoming@ict.ac.cn.

𝒑 is called in Shearer’s bound of 𝐺𝐷 if 𝑞𝐼 (𝐺𝐷,𝒑) > 0 for any 𝐼 ∈ Ind(𝐺𝐷). Otherwise we say 𝒑 is beyond Shearer’s bound of 𝐺𝐷. Shearer’s result can be stated as follows.

eorem 1.2 ([She85]). For any graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and any probability vector 𝒑 ∈ (0, 1]𝑚, 𝒑 ∈ I𝑎(𝐺𝐷) if and only if 𝒑 is in Shearer’s bound of 𝐺𝐷.

Variable Lov´asz Local Lemma. Variable Lov´asz Local Lemma (VLLL) is another quite general and common seing of LLL, which applies to variable-generated event systems. In this seing, there is a set of underlying mutually independent random variables {𝑋1, · · · ,𝑋𝑛}, and each event 𝐴𝑖 can be fully determined by some variables vbl(𝐴𝑖) of them. e dependency between events and variables can be naturally characterized by a bipartite graph 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵), known as the event-variable graph, such that edge (𝑖, 𝑗) ∈ [𝑚] × [𝑛] exists if and only if 𝑋𝑗 ∈ vbl(𝐴𝑖).

e variable seing is important, mainly because most applications of LLL have natural underlying independent variables, such as the satisability of CNF formulas[ GMSW09, GST16, Moi19a, FGYZ20], hypergraph coloring [McD97, GLLZ19], and Ramsey numbers[Spe75, Spe77, Har16]. In particular, the groundbreaking result by Moser and Tardos [MT10] on constructive LLL applies in the variable seing.

ere is a natural choice for the dependency graph of variable-generated systems, called the canonical dependency graph: two events are adjacent if they share some common variables. Formally, given a bipartite graph 𝐺𝐵 = (𝑈,𝑉,𝐸𝐵), its base graph is dened as the graph 𝐺𝐷(𝐺𝐵) = (𝑈,𝐸𝐷) such that for any two vertices 𝑢𝑖,𝑢𝑗 ∈ 𝑈, (𝑢𝑖,𝑢𝑗) ∈ 𝐸𝐷 if and only if 𝑢𝑖 and 𝑢𝑗 share common neighbors in 𝐺𝐵. If 𝐺𝐵 is the event-variable graph of a variable-generated system A, then 𝐺𝐷(𝐺𝐵) is the canonical dependency graph of A.

Given a graph𝐺𝐷, dene the variable interior I𝑣(𝐺𝐷) to be the set consisting of all vectors 𝒑 such that P ∩𝐴∈A𝐴 > 0 for any variable-generated event system A ∼ (𝐺𝐷,𝒑). Obviously, I𝑣(𝐺𝐷) ⊇ I𝑎(𝐺𝐷) for any 𝐺𝐷. In contrast with the abstract LLL, the Shearer’s bound (of the canonical dependency graph) turns out to be not tight for variable-generated systems [HLL+17]: the containment is proper if and only if 𝐺𝐷 is not chordal1.

Constructive (variable) Lov´asz Local Lemma and Moser-Tardos algorithm. e abstract LLL and the variable LLL mentioned above are not constructive in that they do not indicate how to eciently nd an object avoiding all the bad events. In a seminal paper [ MT10], Moser and Tardos developed an amazingly simple ecient algorithm for variable-generated systems, depicted in Algorithm 12, and showed that this algorithm terminates quickly under the condition in eorem 1.1. Following the Moser-Tardos algorithm (or MT algorithm for short), a large amount of eort devoted to constructive LLL, including the remarkable works which extend the MT techniques beyond the variable seing [ HS14, AIV17, AIK19, AIS19, IS20, HV20]. e MT algorithm has been applied to many important problems, including 𝑘-SAT [GST16], hypergraph coloring [Har16], Hamiltonian cycle [Har16], and their counting and sampling [GJL19, Moi19a, FGYZ20, FHY21, JPV21, HSW21].

Algorithm 1: Moser-Tardos Algorithm

- 1 Assign random values to 𝑋1, · · · ,𝑋𝑛;
- 2 while ∃𝑖 ∈ [𝑚] such that 𝐴𝑖 holds do

- 3 Arbitrarily select one such 𝑖 and resample all variables 𝑋𝑗 in vbl(𝐴𝑖);

- 4 Return the current assignment;


Mainly because such a simple algorithm is so powerful and general-purpose, it is one of the most intriguing and fundamental problems on constructive LLL how powerful the MT algorithm is. Given a graph 𝐺𝐷, dene the Moser-Tardos interior I𝑀𝑇 (𝐺𝐷) to be the set consisting of all vectors 𝒑 such that the MT algorithm is ecient for any variable-generated event system A ∼ (𝐺𝐷,𝒑). Clearly, I𝑀𝑇 (𝐺𝐷) ⊆ I𝑣(𝐺𝐷) for any 𝐺𝐷. A major line of follow-up works explores I𝑀𝑇 (𝐺𝐷) [KSX12, Peg14, KS11, CCS+17].

- 1A graph is chordal if it has no induced cycle of length at least four. 2roughout the paper, the Moser-Tardos algorithm is allowed to follow arbitrary selection rules.


e best known criterion is obtained by Kolipaka and Szegedy [ KS11]. ey extended the MT interior

to the Shearer’s bound. at is, they showed that I𝑀𝑇 (𝐺𝐷) ⊇ I𝑎(𝐺𝐷). As mentioned above, if 𝐺𝐷 is not chordal, I𝑎(𝐺𝐷) is properly contained in I𝑣(𝐺𝐷), so it is possible to further push I𝑀𝑇 (𝐺𝐷) beyond Shearer’s bound.

In this paper, we concentrate on the following open problem:

Problem 1: does I𝑀𝑇 (𝐺𝐷) properly contain I𝑎(𝐺𝐷) for some 𝐺𝐷? If so, for what kind of graph 𝐺𝐷?

Rather than potential applications, our main motivations are the following fundamental problems around LLL itself:

- • e limitation of the constructive LLL in the variable seing. In the most fascinating problems around LLL, a mysterious conjecture says that there is an algorithm which is ecient for all variable-

generated systems A if A ∼ (𝐺𝐷,𝒑) for some 𝐺𝐷 and 𝒑 ∈ I𝑣(𝐺𝐷) [Sze13]. It would be a small miracle if the conjecture is true, since if so, one can always construct a solution eciently in the

variable seing if solutions are guaranteed to exist by the LLL condition. Towards this conjecture, a good start is to show that I𝑀𝑇 (𝐺𝐷) I𝑎(𝐺𝐷) for some 𝐺𝐷, as I𝑣(𝐺𝐷) I𝑎(𝐺𝐷) for 𝐺𝐷 which is not chordal.

- • e limitation of the MT algorithm. e MT algorithm is one of the most intriguing topics in modern algorithm researches, not only because it is very simple and with magic power, but also because it is closely related to the famous Walksat algorithm for random 𝑘-SAT. A mysterious problem about the MT algorithm is where is its true limitation [Sze13, CCS+17]. It is conjectured that


I𝑀𝑇 (𝐺𝐷) = I𝑣(𝐺𝐷) for any 𝐺𝐷 [Sze13]. To prove this conjecture, the rst step is to give a positive

answer to Problem 1. Moreover, due to the connection between Shearer’s bound and the Repulsive Laice Gas model, it is conjectured that essential connection exists between statistical mechanics and the MT algorithm [Sze13]. Whether I𝑀𝑇 (𝐺𝐷) = I𝑎(𝐺𝐷) for each 𝐺𝐷 is critical to this conjecture.

Remark 1.3. To explore the power of the MT algorithm in specic applications, one may employ special structures of the applications, such as the way the variables interact, to obtain sharp bounds rather than in terms of the canonical dependency graph only. Nevertheless, characterizing the power of the MT algorithm in terms of the canonical dependency graph is a very fundamental problem and also the focus of the major line of researches [MT10, Peg14, BFPS11, KS11]. Moreover, a major diculty to strengthen the guarantees of the MT algorithm is that the analysis should be valid for all possible variable-generated event systems. It is not quite surprising to obtain beer bounds if the event system has further restrictions. To substantially improve the guarantees of the MT algorithm and provide deep insight about its dynamics, we would rather focus on the general variable LLL seing than employ the special structures in the applications.

We should emphasize that Problem 1 is still quite open! As mentioned before, it has been proved that the Shearer’s bound is not tight for variable-generated systems [HLL+17]. However, this only says that there is some probability vector 𝒑 beyond the Shearer’s bound such that all variable-generated event systems A ∼ (𝐺𝐷,𝒑) must have a satisfying assignment. It is unclear whether the MT algorithm can construct such an assignment eciently.

It also has been proved that the MT algorithm can still be ecient even beyond the Shearer’s bound for some specic applications [Har16]. Despite its novel contribution, this result does not provide an answer to Problem 1. e result in [ Har16] focuses on the event systems with special structures. us, it only implies that there is a probability vector 𝒑 beyond the Shearer’s bound such that the MT algorithm is ecient for some restricted variable-generated event systems A ∼ (𝐺𝐷,𝒑). However, to show I𝑀𝑇 (𝐺𝐷) I𝑎(𝐺𝐷), one must prove that the MT algorithm is ecient for all possible event systems, and this is one major diculty to resolve Problem 1.

- 1.1. Results and contributions. We provide a complete answer to Problem 1 (eorem 1.5): if 𝐺𝐷 is not chordal, then I𝑀𝑇 (𝐺𝐷) I𝑎(𝐺𝐷), i.e., the ecient region of the MT algorithm goes beyond Shearer’s bound. Otherwise, I𝑀𝑇 (𝐺𝐷) = I𝑎(𝐺𝐷), because I𝑎(𝐺𝐷) ⊆ I𝑀𝑇 (𝐺𝐷) ⊆ I𝑣(𝐺𝐷) and I𝑣(𝐺𝐷) = I𝑎(𝐺𝐷) for chordal graphs 𝐺𝐷 [HLL+17].


e core of the proof of eorem 1.5 is a new convergence criterion for the MT algorithm (eorem

- 1.6), which may be of independent interest. is new criterion takes the intersection between dependent


events into consideration, and is strictly beer than Shearer’s bound when there exists a pair of dependent events which are not mutually exclusive.

- 1.1.1. Moser-Tardos algorithm: beyond Shearer’s bound. Given a dependency graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and a probability vector 𝒑 = (𝑝1,𝑝2, · · · ,𝑝𝑚) ∈ (0, 1)𝑚, we say that 𝒑 is on the Shearer’s boundary of 𝐺𝐷 if (1 − 𝜀)𝒑 is in Shearer’s bound and (1 + 𝜀)𝒑 is not for any 𝜀 > 0. A chordless cycle in a graph 𝐺𝐷 is an induced cycle of length at least 4. A chordal graph is a graph without chordless cycles.

Given two vectors 𝒑 and 𝒒, we say 𝒑 ≤ 𝒒 if the inequality holds entry-wise. Additionally, if the inequality is strict on at least one entry, we say that 𝒑 < 𝒒.

- Denition 1.4 (Maximum 𝐿1-gap to the Shearer’s bound). Given a dependency graph 𝐺𝐷 and a probability vector 𝒑 beyond the Shearer’s bound of 𝐺𝐷, dene the maximum 𝐿1-gap from 𝒑 to the Shearer’s bound of 𝐺𝐷 as


𝑑(𝒑,𝐺𝐷) arg sup ||𝒒||1

{𝒑 − 𝒒 ∉ I𝑎(𝐺𝐷) : 𝒒 ≤ 𝒑}.

For convenience, we let 𝑑(𝒑,𝐺𝐷) = −1 if 𝒑 is in the Shearer’s bound of 𝐺𝐷.

Intuitively, 𝑑(𝒑,𝐺𝐷) measures how far 𝒑 is from the Shearer’s bound of 𝐺𝐷. One can verify that 𝑑(𝒑,𝐺𝐷) < 0 if 𝒑 is in the Shearer’s bound, 𝑑(𝒑,𝐺𝐷) = 0 if 𝒑 is on the Shearer’s boundary, and 𝑑(𝒑,𝐺𝐷) > 0 if 𝒑 is beyond Shearer’s bound but not on the Shearer’s boundary. Now, we are ready to state our main result.

- eorem 1.5. For any chordal graph 𝐺𝐷, I𝑀𝑇 (𝐺𝐷) = I𝑎(𝐺𝐷), i.e., 𝒑 ∈ I𝑀𝑇 (𝐺𝐷) i 𝑑(𝒑,𝐺𝐷) < 0. For any graph 𝐺𝐷 which is not chordal, 𝒑 ∈ I𝑀𝑇 (𝐺𝐷) if


𝑑(𝒑,𝐺𝐷) <

1 545 · ∑︁

𝑖≤ℓ

|𝐶𝑖| min 𝑗 ∈𝐶𝑖

𝑝𝑗 4 · max

2 𝑗∈𝐶𝑖 √𝑝𝑗 |𝐶𝑖|

− 1, 0

2

for some disjoint chordless cycles 𝐶1,𝐶2, · · · ,𝐶ℓ in 𝐺𝐷. In particular, there is a probability vector 𝒑 with 𝑑(𝒑,𝐺𝐷) ≥ 2−20𝐾−3 satisfying the above condition, where 𝐾 is the length the shortest chordless cycle. is implies that I𝑀𝑇 (𝐺𝐷) contains a probability vector 𝒑 with 𝑑(𝒑,𝐺𝐷) ≥ 2−20𝐾−3.

e intuition of eorem 1.5 is as follows. e theorem characterizes the ecient region of the MT algorithm with 𝑑(𝒑,𝐺𝐷). It shows that if 𝑑(𝒑,𝐺𝐷) is upper bounded by a non-negative quantity related to the chordless cycles in 𝐺𝐷, then the MT algorithm is ecient. Since I𝑎(𝐺𝐷) is the set of 𝒑 where 𝑑(𝒑,𝐺𝐷) < 0, our criterion is at least as good as Shearer’s bound. Moreover, for each 𝐺𝐷 which is not chordal, our criterion is strictly beer: there exists some 𝒑 with 𝑑(𝒑,𝐺𝐷) ≥ 2−20𝐾−3 satisfying our criterion. Intuitively, eorem 1.5 implies that chordless cycles in 𝐺𝐷 enhance the power of the MT algorithm.

We emphasize that eorem 1.5 provides a complete answer to Problem 1: I𝑀𝑇 (𝐺𝐷) properly contains I𝑎(𝐺𝐷) if and only if 𝐺𝐷 is not chordal.

- 1.1.2. A new constructive LLL for non-extremal instances. Given a set A of events with dependency


graph 𝐺𝐷, A is called extremal if all pairs of dependent events are mutually exclusive, and nonextremal otherwise. Kolipaka and Szegedy [KS11] showed that the MT algorithm is ecient up to

the Shearer’s bound. In particular, Shearer’s bound is the tight convergence criterion for extremal instances [KS11, GJL19]. Here, we provide a new convergence criterion (eorem 1.6) which is a strict improvement of Kolipaka and Szegedy’s result: this criterion is strictly beer than Shearer’s bound when the instance is non-extremal, and becomes Shearer’s bound when the instance is extremal. is criterion, named intersection LLL, is the core of our proof of eorem 1.5.

Let𝐺𝐷 = ([𝑚],𝐸𝐷) be a canonical dependency graph and 𝒑 = (𝑝1, · · · ,𝑝𝑚) ∈ (0, 1)𝑚 be a probability vector. Let M = {(𝑖1,𝑖 1), (𝑖2,𝑖 2), · · · } ⊆ 𝐸𝐷 be a matching of 𝐺𝐷, and 𝜹 = (𝛿𝑖1,𝑖

, · · · ) ∈ (0, 1)|M| be another probability vector. We say that an event set A is of the seing (𝐺𝐷,𝒑, M, 𝜹), and write A ∼ (𝐺𝐷,𝒑, M, 𝜹), if A ∼ (𝐺𝐷,𝒑) and P(𝐴𝑖 ∩𝐴𝑖 ) ≥ 𝛿𝑖,𝑖 for each pair (𝑖,𝑖 ) ∈ M. Given (𝐺𝐷,𝒑, M, 𝜹),

,𝛿𝑖2,𝑖

1

2

dene 𝒑− ∈ (0, 1)𝑚 as follows:

∀𝑖 ∈ [𝑚] : 𝑝𝑖− =

𝑝𝑖 − 171 · 𝛿𝑖,𝑖2 , if (𝑖,𝑖 ) ∈ M for some 𝑖 ; 𝑝𝑖, otherwise.

- eorem 1.6 (intersection LLL (informal)). For any A ∼ (𝐺𝐷,𝒑, M, 𝜹), MT algorithm terminates quickly if 𝒑− is in the Shearer’s bound of 𝐺𝐷.


e intuition of eorem 1.6 is as follows. For any matching M in 𝐺𝐷, if the intersection of events

on each edge (𝑖,𝑖 ) in M has a lower bound 𝛿𝑖,𝑖 , then one can subtract 171 ·𝛿𝑖,𝑖2 from the probabilities of endpoints 𝑖 and 𝑖 , and the MT algorithm is guaranteed to be ecient whenever the reduced probability

vector is in the Shearer’s bound.

Remark 1.7. In many applications of LLL [McD97, GST16, GMSW09, Moi19a, GKPT17], the dependent bad events naturally intersect with each other. For instance, in a CNF formula, if the common variables in two clauses are both either positive or negative, then the bad events corresponding to these two clauses are dependent and intersect with each other. us our intersection LLL may be capable of improving bounds for these applications. However, currently the improvement is weak because only the intersections between the matched events are considered in eorem 1.6.

Nevertheless, the primary motivation of this work is to explore the power of the MT algorithm in the general variable LLL seing. is basic problem is very important in itself, besides its potential applications.

- 1.1.3. Application to laices. To illustrate the application of eorem 1.5, we estimate the ecient region of the MT algorithm on some laices explicitly. For simplicity, we focus on symmetric probabilities, i.e., 𝒑 = (𝑝,𝑝, · · · ,𝑝). Our lower bounds on the gaps between the ecient region of the MT algorithm and the Shearer’s bound are summarized in Table 1. For example, when the canonical dependency graph is the square laice, the vector (0.1193, 0.1193, · · · ) is on the Shearer’s boundary, and the MT algorithm is provably ecient whenever the probability of each event is at most 0.1193 + 1.858 × 10−22.


T     1. Summary of lower bounds on the gaps Laice Shearer’s bound lower bound on the gaps Square 0.1193 [GF65, Tod99] 1.858 × 10−22

Hexagonal 0.1547 [Tod99] 2.597 × 10−25 Simple Cubic 0.0744 [Gau67] 7.445 × 10−23

- 1.2. Technique overview. As mentioned before, the Shearer’s bound is the tight criterion for MT algorithm on extremal instances. us in order to show that MT algorithm goes beyond Shearer’s bound, we need to take advantage of the intersection between dependent events. Specically, eorem


- 1.5 immediately follows from two results about non-extremal instances. One is the intersection LLL criterion (eorem 1.6), which goes beyond Shearer’s bound whenever there are intersections between dependent events. e other result is a lower bound on the amount of intersection between dependent events for general instances (eorem 4.1).


- 1.2.1. Proof overview of eorem 1.6. Let us rst remember Kolipaka and Szegedy’s argument [ KS11],


which shows that the MT algorithm is ecient up to the Shearer’s bound. We assume that {𝐴𝑖}𝑚𝑖=1 is a xed set of events with dependency graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and probabilities 𝒑 = (𝑝1, · · · ,𝑝𝑚). e notion of a witness DAG3 (abbreviated wdag) is central to their argument. A wdag is a DAG whose each node 𝑣 has a label 𝐿(𝑣) from [𝑚] and in which two nodes 𝑣 and 𝑣 are connected by an arc if and only if 𝐿(𝑣) = 𝐿(𝑣 ) or (𝐿(𝑣),𝐿(𝑣 )) ∈ 𝐸𝐷. With a resampling sequence 𝒔 = 𝑠1,𝑠2, · · · ,𝑠𝑇 (i.e., MT algorithm picks the events 𝐴𝑠1,𝐴𝑠2, · · · ,𝐴𝑠𝑇 for resampling in this order), we associate a wdag 𝐷𝒔 on node set {𝑣1, · · · ,𝑣𝑇 } as follows: (a) 𝐿(𝑣𝑘) = 𝑠𝑘 and (b) there is an arc from 𝑣𝑘 to 𝑣ℓ with 𝑘 < ℓ if and only if either 𝑠𝑘 = 𝑠ℓ or (𝑠𝑘,𝑠ℓ) ∈ 𝐸𝐷 (see an example in Figure 1). We say that a wdag 𝐷 occurs in the resampling

3In the paper [KS11], the role of witness DAGs was played by “stable set sequences”, but the concepts are essentially the same: there is a natural bijection between stable set sequences and wdags.

![image 1](<2021-he-moser-tardos-algorithm-beyond-shearer_images/imageFile1.png>)

F      1. (a) a dependency graph 𝐺𝐷; (b) a resample sequence; (c) the 𝐷𝑠; (d) a wdag occurring in 𝒔.

sequence 𝒔 if there is subset 𝑈 of nodes in 𝐷𝒔 such that 𝐷 is a subgraph of 𝐷𝒔 induced by the nodes that have a directed path to 𝑈 (Figure 1 (d) is an example, where 𝑈 = {𝑣4}). An useful observation is that E[𝑇] = 𝐷∈D P𝒔[𝐷 occurs in 𝒔]. Here, D denotes the set of all single-sink wdags (a.k.a. proper wdags) of 𝐺𝐷.

We dene the weight of a wdag 𝐷 to be Π𝑣∈𝐷𝑝𝐿(𝑣). e crucial lemma in Kolipaka and Szegedy’s argument (the idea is from Moser-Tardos analysis) is that the probability of occurrence of a certain wdag 𝐷 is upper bounded by its weight. e idea is that we can assume (only for the analysis) that the MT algorithm has a preprocessing step where it prepares an innite number of independent samples for each variable. ese independent samples create a table 𝑿, called the resampling table (see Figure

- 2 in Section 3.1 for an example). When the MT algorithm decides to resample variable 𝑋𝑗, it picks a new sample of 𝑋𝑗 from the resampling table. Suppose a certain wdag 𝐷 occurs, then for each of its events we can determine a particular set of samples in the resampling table that must satisfy the event, where we say that 𝐷 is consistent with the resampling table 𝑿 and denote it by 𝐷 ∼ 𝑿. Hence, P𝒔[𝐷 occurs in 𝒔] ≤ P𝑿 [𝐷 ∼ 𝑿] = Π𝑣∈𝐷𝑝𝐿(𝑣).


Finally, they solved beautifully the summation of weights of proper wdags, i.e., 𝐷∈D Π𝑣∈𝐷𝑝𝐿(𝑣), which turns out to converge if and only if 𝒑 is in the Shearer’s bound of 𝐺𝐷.

Viewing eorem 1.6 as an improvement of Kolipaka and Szegedy’s result, we begin by providing a tighter upper bound on 𝐷∈D P𝒔[𝐷 occurs in 𝒔] when the instance is non-extremal (eorem 3.7). First, note that for each wdag 𝐷, there exist selection rules to make P𝒔[𝐷 occurs in 𝒔] = Π𝑣∈𝐷𝑝𝐿(𝑣), so it is impossible to give a beer upper bound on P𝒔[𝐷 occurs in 𝒔] which holds for all selection rules. Our idea is to group proper wdags, and consider the sum of P𝒔[𝐷 occurs in 𝒔] over a group. For example, suppose that 𝐴1 and 𝐴2 are dependent and P[𝐴1 ∩ 𝐴2] ≥ 𝛿1,2. Let 𝐷1 denote the proper wdag which consists of only one arc 𝐴1 → 𝐴2, and 𝐷2 denote the proper wdag consisting of only 𝐴2 → 𝐴1. 𝐷1 and 𝐷2 cannot both occur, but they may be both consistent with a given resampling table. So the total weights of 𝐷1 and 𝐷2 is an overestimate of the probability that 𝐷1 or 𝐷2 occurs. Formally,

P𝒔[𝐷1 occurs in 𝒔] + P𝒔[𝐷2 occurs in 𝒔] =P𝒔[(𝐷1 occurs in 𝒔) ∨ (𝐷2 occurs in 𝒔)] ≤P𝑿 [(𝐷1 ∼ 𝑿) ∨ (𝐷2 ∼ 𝑿)]

### =P𝑿 [𝐷1 ∼ 𝑿] + P𝑿 [(𝐷2 ∼ 𝑿) ∧ (𝐷1 𝑿)] ≤𝑝1𝑝2 + 𝑝1𝑝2 − 𝛿12,2,

where the last inequality is according to the Cauchy–Schwarz inequality (see Proposition 3.3). Importantly, the upper bound holds for all selection rules.

It is crucial as well as the diculty that our improvement over the weight of wdags should be

“exponential”: since the quantity 𝐷∈D Π𝑣∈𝐷𝑝𝐿−(𝑣) converges if and only if 𝒑− is in the Shearer’s bound, constant factor or even sub-exponential improvements over 𝐷∈D Π𝑣∈𝐷𝑝𝐿(𝑣) do not help to show the desired convergence criterion. Our exponential improvement relies on a delicate grouping and a tricky random partition of the union of 𝐷 ∼ 𝑿 across wdags.

We rst state how we group proper wdags: dene D(𝑖,𝑟) to be the set of proper wdags whose unique sink node is labelled with 𝑖 and in which there are exactly 𝑟 nodes labelled with 𝑖. Noticing that at most one wdag in D(𝑖,𝑟) can occur, we have that

P𝒔[𝐷 occurs in 𝒔] =P𝑿 

  

≤ P𝑿 

  

∑︁

(𝐷 occurs)

(𝐷 ∼ 𝑿)

.

  𝐷∈D(𝑖,𝑟)

  𝐷∈D(𝑖,𝑟)

𝐷∈D(𝑖,𝑟)

Now, we partition the space 𝐷∈D(𝑖,𝑟)(𝐷 ∼ 𝑿) across wdags in D(𝑖,𝑟). e notions of reversible arcs (see Denition 2.4) and a auxiliary table (see Section 3.1) are two central concepts here. Specically, an arc𝑢 → 𝑣 in a wdag 𝐷 is said reversible, if the directed graph obtained from 𝐷 by reversing the direction of 𝑢 → 𝑣 is also a wdag. e auxiliary table is a table 𝒀 of independent fair coins corresponding to directions of reversible arcs. We say a wdag 𝐷 is consistent with (𝑿, 𝒀), denoted by 𝐷 ∼ (𝑿, 𝒀) if (i) 𝐷 ∼ 𝑿; and (ii) for each reversible arc whose direction is not consistent with 𝒀, the wdag obtained by reversing the arc is not consistent with 𝑿. e crucial lemma (Lemma 3.1) shows that for any certain assignment 𝒚 of the auxiliary table 𝒀, 𝐷∈D(𝑖,𝑟)(𝐷 ∼ 𝑿) = 𝐷∈D(𝑖,𝑟)(𝐷 ∼ (𝑿,𝒚)). e point is that (𝐷 ∼ (𝑿,𝒚))’s have much less overlap with each other so that they can be viewed as a “approximate” partition of the space. By applying union bound, we get

P𝑿 

  

=E𝒀P𝑿 

  

= E𝒀P𝑿 

  

(𝐷 ∼ 𝑿)

(𝐷 ∼ 𝑿)

(𝐷 ∼ (𝑿, 𝒀)

  𝐷∈D(𝑖,𝑟)

  𝐷∈D(𝑖,𝑟)

  𝐷∈D(𝑖,𝑟)

≤E𝒀 ∑︁

P𝑿 [𝐷 ∼ (𝑿, 𝒀)]

= ∑︁

𝐷∈D(𝑖,𝑟)

E𝒀P𝑿 [𝐷 ∼ (𝑿, 𝒀)] .

𝐷∈D(𝑖,𝑟)

en we are able to provide an upper bound on E𝒀P𝑿 [𝐷 ∼ (𝑿, 𝒀)] which is “exponentially” smaller than Π𝑣∈𝐷𝑝𝐿(𝑣) (Lemma 3.4), and then complete the proof of eorem 3.7.

e next step is to show that the tighter upper bound converges when 𝒑− is in the Shearer’s bound. For each vertex 𝑖 in the matching M, we “split” vertex 𝑖 into two new connected vertices 𝑖↑ and 𝑖↓. Let 𝐺M be the resulted dependency graph (see an example in Figure 3). Dene 𝑝𝑖M↑ = 𝑝 𝑖 and 𝑝𝑖M↓ = 𝑝𝑖− − 𝑝 𝑖 (see the denition of 𝑝 𝑖 in Section 2.3). One can see that (𝐺𝐷,𝒑−) and (𝐺M,𝒑M) are essentially the same: suppose A ∼ (𝐺𝐷,𝒑−), then for each 𝑖 ∈ M, we view 𝐴𝑖 as the union of two mutually exclusive events 𝐴𝑖↑ and 𝐴𝑖↓ whose probabilities are 𝑝 𝑖 and 𝑝− − 𝑝 𝑖 respectively. Such a representation of A is of the seing (𝐺M,𝒑M). us, the sum of weights of proper wdags in the seing (𝐺𝐷,𝒑−) is equal to that in the seing (𝐺M,𝒑M) (Proposition 3.9). So it suces to show that our tighter upper bound is upper bounded by the sum of weights of proper wdags in the seing (𝐺M,𝒑M) (eorem 3.13). Our idea is to construct a mapping which maps each 𝐷 ∈ D(𝐺𝐷) to a subset of D(𝐺M) and satises that:

- (a) distinct proper wdags of 𝐺𝐷 are mapped to disjoint subsets of D(𝐺M); and
- (b) for each 𝐷 ∈ D(𝐺𝐷), the bound in Lemma 3.4 is upper bounded by the sum of weights of proper wdags over the subset that 𝐷 is mapped to.


We present such a mapping in Denition 3.11. Conditions (a) and (b) are veried in eorem 3.12 and eorem 3.13 respectively.

e idea of constructing a mapping between wdags of two dependency graphs may be of independent interest, and may be applied elsewhere when we wish to show some properties about Shearer’s bound.

- 1.2.2. Proof overview of eorem 4.1. e proof of eorem 4.1 mainly consists of two parts. First, we show that there is an elementary event set which approximately achieves the minimum amount of the intersection between dependent events (Lemma 4.2). Here, we call an event 𝐴𝑖 ∈ A elementary, if there is a subset 𝑆𝑖𝑗 of the domain of variable 𝑋𝑗 for each variable in vbl(𝐴) such that 𝐴 happens if


and only if 𝑋𝑗 ∈ 𝑆𝑖𝑗 for all variables in vbl(𝐴). We call a set A of events elementary if every 𝐴𝑖 ∈ A is elementary. en, for elementary event sets, by applying AM-GM inequality, we obtain a lower

bound on the total amount of overlap on common variables, which further implies a lower bound on the amount of intersection between dependent events (Lemma 4.5).

- 1.3. Related works. Beck proposed the rst constructive LLL, which provides ecient algorithms for nding the perfect object avoiding all “bad” events [ Bec91]. His methods were rened and improved by a long line of research [Alo91, MR98, CS00, HSS11]. In a groundbreaking work, Moser and Tardos proposed a new algorithm, i.e., Algorithm 1, and proved that it nds such a perfect object under the condition in eorem 1.1 in the variable seing [ MT10]. Pegden [Peg14] proved that the MT algorithm eciently converges even under the condition of the cluster expansion local lemma [ BFPS11]. Kolipaka and Szegedy [KS11] pushed the ecient region to Shearer’s bound. e phenomenon that the MT algorithm can still be ecient beyond Shearer’s bound was known to exist for sporadic and toy examples [Har16]. However, such result employs the special structures in the examples and only applies to some

restricted variable-generated event systems A ∼ (𝐺𝐷,𝒑). By contrast, the results in this work applies to all variable-generated event systems.

Besides the line of research exploring the ecient region of the MT algorithm, there is a large amount of eort devoted to derandomizing or parallelizing the MT algorithm [ MT10, CGH13, Har19, BFH+16, Gha16, CPS17, HH17, Har18] and to extending the Moser-Tardos techniques beyond the variable seing [HS14, AI16, HV20, AIV17, AIK19, Mol19, IS20, AIS19].

ere is a line of works studying the gap between non-constructive VLLL and Shearer’s bound [KS11, HLL+17, Gil19, HLSZ19]. Kolipaka and Szegedy [KS11] obtained the rst example of gap existence where the canonical dependency graph is a cycle of length 4. e paper [ HLL+17] showed that Shearer’s bound is not tight for VLLL. More precisely, Shearer’s bound is tight for non-constructive VLLL if and only if the canonical dependency graph is chordal. e rst paper to study quantitatively the gaps systematically is [HLSZ19], which provides lower bounds on the gap when the canonical dependency graph containing many chordless cycles.

Erd¨os and Spencer [ES91] introduced the lopsided-LLL, which extends the results in [EL75] to lopsidependency graphs. Lopsided LLL has many interesting applications in combinatorics and theoretical computer science, such as the𝑘-SAT [GST16], random permutations [LS07], Hamiltonian cycles [AFR95], and matchings on the complete graph [LS09]. Shearer’s bound is also the tight condition for the lopsided LLL [She85].

LLL has a strong connection to sampling. Guo, Jerrum and Liu [GJL19] proved that the MT algorithm indeed uniformly samples a perfect object if the instance is extremal. For extremal instances, they developed an algorithm called “partial rejection sampling” which resamples in a parallel fashion, since the occurring bad events form an independent set in the dependency graph. Actually, a series of sampling algorithms for specic problems are the parallel resampling algorithm running in the extremal case [GJL19, GJ19, GH20, GJ18]. In a celebrated work, Moitra [Moi19b] introduced a novel approach that utilizes LLL to sample 𝑘-CNF solutions. is approach was then extended by several works [GLLZ19, GGGY20, FGYZ20, FHY20, JPV20, JPV21].

- 1.4. Organization of the paper. In Section 2, we recall and introduce some denitions and notations. In Section 3, we prove eorem 1.6. Section 4 is about the proof of eorem 4.1, which gives a lower bound on the amount of the intersection between dependent events. In Section 5, we prove eorem
- 1.5. In Section 6, we provide a explicit lower bound for the gaps between the ecient region of MT algorithm and Shearer’s bound on periodic Euclidean graphs.


2. P            

Let N = {0, 1, 2, · · · } denote the set of non-negative integers. Let N+ = {1, 2, · · · } denote the set positive integers. For 𝑚 ∈ N+, we dene [𝑚] = {1, · · · ,𝑚}. roughout this section, we x a canonical dependency graph 𝐺𝐷 = ([𝑚],𝐸𝐷).

- 2.1. Witness DAG. If for a given run, MT algorithm picks the events 𝐴𝑠1,𝐴𝑠2, ...,𝐴𝑠𝑇 for resampling in this order, we say that 𝒔 = 𝑠1,𝑠2...,𝑠𝑇 is a resample sequence. If the algorithm never nishes, the resample sequence is innite, and in this case we set 𝑇 = ∞.


- Denition 2.1 (Witness DAG). We dene a witness DAG (abbreviated wdag) of 𝐺𝐷 to be a DAG 𝐷, in which each node 𝑣 has a label 𝐿(𝑣) from [𝑚], and which satises the additional condition that for all distinct nodes 𝑣,𝑣 ∈ 𝐷 there is an arc between 𝑣 and 𝑣 (in either direction) if and only if 𝐿(𝑣) = 𝐿(𝑣 ) or


𝐿(𝑣),𝐿(𝑣 ) ∈ 𝐸𝐷.

We say 𝐷 is a proper wdag (abbreviated pwdag) if 𝐷 has only one sink node. Let D(𝐺𝐷) denote the set of pwdags of 𝐺𝐷.

Given a resampling sequence 𝒔 = 𝑠1,𝑠2, ...,𝑠𝑇, we associate a wdag 𝐷𝒔 on the node set {𝑣1, ...,𝑣𝑇 } such that (i) 𝐿(𝑣𝑘) = 𝑠𝑘 and (ii) 𝑣𝑘 → 𝑣ℓ with 𝑘 < ℓ is as an arc of 𝐷𝒔 if and only if either 𝑠𝑘 = 𝑠ℓ or (𝑠𝑘,𝑠ℓ) ∈ 𝐸𝐷. See Figure 1 for an example of 𝐷𝒔.

Given a wdag 𝐷 and a set 𝑈 of nodes of 𝐷, we dene 𝐷(𝑈) to be the induced subgraph on all nodes which has a directed path to some 𝑢 ∈ 𝑈. Note that 𝐷(𝑈) is also a wdag. We say that 𝐻 is a prex of 𝐷, denoted by 𝐻 𝐷, if 𝐻 = 𝐷(𝑈) for some node set 𝑈.

- Denition 2.2. We say a wdag 𝐷 occurs in a resampling sequence 𝒔 if 𝐷 𝐷𝒔. Let 𝜒𝐷 be the indicator variable of the event that 𝐷 occurs in 𝒔.


Similar to Lemma 12 in [KS11], we have that 𝑇 = 𝐷∈D(𝐺𝐷) 𝜒𝐷. For 𝑖 ∈ [𝑚] and 𝑟 ∈ N+, dene

D(𝑖,𝑟) to be the set of pwdags whose unique sink node is labelled with 𝑖 and in which there are exactly 𝑟 nodes labelled with 𝑖. Let 𝜒D(𝑖,𝑟) be the indicator variable of the event that there is a 𝐷 ∈ D(𝑖,𝑟) occurring in 𝒔. It is easy to see that only one pwdag in D(𝑖,𝑟) can occur in 𝒔. us 𝜒D(𝑖,𝑟) = 𝐷∈D(𝑖,𝑟) 𝜒𝐷, which further implies that

### Fact 2.3. 𝑇 = 𝑖∈[𝑚] 𝑟∈N+ 𝜒D(𝑖,𝑟).

- 2.2. Reversible arc. In the rest of this section, we x a matching M ⊆ 𝐸𝐷 of 𝐺𝐷. Given 𝑖 ∈ [𝑚], with a slight abuse of notation, we sometimes say 𝑖 ∈ M if there is some 𝑖 ∈ [𝑚] such that (𝑖,𝑖 ) ∈ M.

- Denition 2.4 (Reversibility). We say that an arc 𝑢 → 𝑣 is reversible in a wdag 𝐷 if the directed graph obtained from 𝐷 by reversing the direction of the arc is still a DAG.


Furthermore, we say that 𝑢 → 𝑣 is M-reversible in 𝐷 if 𝑢 → 𝑣 is reversible in 𝐷 and (𝐿(𝑢),𝐿(𝑣)) ∈ M. By denition, we have the following two observations.

- Fact 2.5. 𝑢 → 𝑣 is reversible in 𝐷 if and only if it is the unique path from 𝑢 to 𝑣 in 𝐷.
- Fact 2.6. If 𝑢 → 𝑣 is reversible in a wdag 𝐷 of 𝐺𝐷, then the directed graph obtained from 𝐷 by reversing the direction of 𝑢 → 𝑣 is also a wdag of 𝐺𝐷.

Given a pwdag 𝐷 = (𝑉,𝐸,𝐿), dene

V(𝐷) {𝑣 : ∃𝑢 ∈ 𝑉 such that 𝑢 → 𝑣 or 𝑣 → 𝑢 is M-reversible in 𝐷}

to be the set of nodes participating in reversible arcs, and V(𝐷) 𝑉 \ V(𝐷). For 𝑖 ∈ [𝑚], dene V(𝐷,𝑖) V(𝐷) ∩ {𝑣 : 𝐿(𝑣) = 𝑖}.

2.3. Other notations. Let 𝒑 = (𝑝1, · · · ,𝑝𝑚) ∈ (0, 1]𝑚 and 𝜹 ∈ (0, 1)M be two probability vectors. Recall that 𝒑− = (𝑝1−, · · · ,𝑝𝑚−) is dened as

∀𝑖 ∈ [𝑚] : 𝑝𝑖− = 𝑝𝑖 − 𝛿

2

𝑖,𝑖

17 if (𝑖,𝑖 ) ∈ M for some 𝑖 , 𝑝𝑖 otherwise.

- (1)


For each 𝑖 ∈ [𝑚] where (𝑖,𝑖 ) ∈ M for some 𝑖 ∈ [𝑚], dene

𝑐𝑖

𝛿𝑖,𝑖2 8𝑝𝑖𝑝𝑖

and 𝑝 𝑖 𝑝𝑖(1 − 𝑐𝑖) = 𝑝𝑖 −

𝛿𝑖,𝑖2 8𝑝𝑖

.

- Fact 2.7. 𝑝𝑖− + 𝑝𝑖− (𝑝𝑖− − 𝑝 𝑖) ≥ 𝑝𝑖 for each (𝑖,𝑖 ) ∈ M.




3. P     T       1.6

e proof of eorem 1.6 consists of two parts. First, we provide a tighter upper bound on the complexity of MT algorithm (Section 3.1). en, we show that the tighter upper bound converges if 𝒑− is in the Shearer’s bound of 𝐺𝐷 (Section 3.2).

- 3.1. A tighter upper bound on the complexity of MT algorithm. In this subsection, we prove eorem 3.7, which follows from Lemma 3.1 and Lemma 3.4 immediately. We rst recall and introduce some concepts and notations.


Resampling Table. One key analytical technique of Moser and Tardos [MT10] is to precompute the randomness in a resampling table 𝑿. Specically, we can assume (only for the analysis) that MT algorithm has a preprocessing step where it draws an innite number of independent samples 𝑋𝑗1,𝑋𝑗2, · · · for each variable𝑋𝑗. ese independent samples create a table 𝑿 = (𝑋𝑗𝑘)𝑗∈[𝑚],𝑘∈N+, called the resampling table (see Figure 2). MT algorithm takes that rst column as the initial assignments of 𝑋1, · · · ,𝑋𝑛. en, when 𝑋𝑗 is to be resampled, MT algorithm goes right in the row corresponding to 𝑋𝑗 and picks the sample. Consistency with the resampling table. For a wdag 𝐷, a node 𝑣, and a variable 𝑋𝑗 ∈ vbl(𝐴𝐿(𝑣)), we dene

L(𝐷,𝑣, 𝑗) |{𝑢 : there is a directed path from 𝑢 to 𝑣 in 𝐷 and 𝑋𝑗 ∈ vbl(𝐴𝐿(𝑢))}| + 1.

Moreover, let 𝑿𝐷,𝑣 {𝑋𝑗L(𝐷,𝑣,𝑗) : 𝑋𝑗 ∈ 𝐴𝐿(𝑣)}. We say that 𝐷 is consistent with 𝑿, denoted by 𝐷 ∼ 𝑿, if for each node 𝑣 in 𝐷, the event 𝐴𝐿(𝑣) holds on 𝑿𝐷,𝑣. Intuitively, suppose 𝐷 occurs, then 𝑿𝐷,𝑣 are the assignments of vbl(𝐴𝐿(𝑣)) just before the time that the MT algorithm picks the event corresponding to 𝑣 to resample, hence 𝐴𝐿(𝑣) must hold on 𝑿𝐷,𝑣. We sometimes use L(𝑣, 𝑗) and 𝑿𝑣 instead of L(𝐷,𝑣, 𝑗) and 𝑿𝐷,𝑣 respectively if 𝐷 is clear from the context. Besides, we use D(𝑖,𝑟) ∼ 𝑿 to denote that there is some 𝐷 ∈ D(𝑖,𝑟) such that 𝐷 ∼ 𝑿.

![image 2](<2021-he-moser-tardos-algorithm-beyond-shearer_images/imageFile2.png>)

![image 3](<2021-he-moser-tardos-algorithm-beyond-shearer_images/imageFile3.png>)

F      2. e le is a resampling table where there are four variables 𝑋1, · · · ,𝑋4. e right is an auxiliary table where M = {(1, 2), (3, 4), (5, 6), (7, 8)}.

Auxiliary Table. We introduce another central concept in the proof of eorem 3.7, called the auxiliary table, which is a table of independent fair coins. Specically, for each pair (𝑖,𝑖 ) ∈ M, we draw an innite number of independent fair coins 𝑌𝑖,𝑖1 ,𝑌𝑖,𝑖2 , · · · , where P(𝑌𝑖,𝑖𝑘 = 𝑖) = P(𝑌𝑖,𝑖𝑘 = 𝑖 ) = 1/2. ese independent coins form the auxiliary table 𝒀 = (𝑌𝑖,𝑖𝑘 )(𝑖,𝑖 )∈M,𝑘∈N+ (see Figure 2). e auxiliary table is used to encode directions of M-reversible arcs, according to which we partition the space

### 𝐷∈D(𝑖,𝑟)(𝐷 ∼ 𝑿).

Consistency with the resampling table and the auxiliary table. We need some notations about reversible arcs. Suppose 𝐷 has a unique sink node 𝑤 and 𝑢 → 𝑣 is reversible in 𝐷. Let 𝐷 be the DAG obtained from 𝐷 by reversing the direction of 𝑢 → 𝑣. We dene 𝜑(𝐷,𝑢,𝑣) 𝐷 ({𝑤}). In other words, 𝜑(𝐷,𝑢,𝑣) is the prex of 𝐷 with a unique sink node 𝑤. Given (𝑖,𝑖 ) ∈ M and a pwdag 𝐷, let List(𝐷,𝑖,𝑖 ) denote the sequence listing all nodes in 𝐷 with labels 𝑖 or 𝑖 in a topological order of 𝐺𝐷4. Given a node 𝑣 in 𝐷, if (𝐿(𝑣),𝑖) ∈ M5, we dene

### 𝜆(𝑣,𝐷) |{𝑢 : (𝑢 → 𝑣 is in 𝐷) ∧ (𝐿(𝑢) ∈ {𝑖,𝐿(𝑣)})}| + 1

4It is easy to see that List(𝐷,𝑖,𝑖 ) is well dened. at is, all topological orderings of 𝐷 induce the same List(𝐷,𝑖,𝑖 ). 5Because M is a matching, there is at most one such 𝑖.

to be the order of 𝑣 in List(𝐷,𝐿(𝑣),𝑖). For simplicity of notations, we will use 𝜆(𝑣) instead of 𝜆(𝑣,𝐷) if 𝐷 is clear from the context.

Given a wdag 𝐷, we say an M-reversible arc 𝑢 → 𝑣 is inconsistent with the auxiliary table 𝒀 if

𝑦𝐿𝜆((𝑢𝑢)),𝐿(𝑣) = 𝐿(𝑣). We say 𝐷 is consistent with (𝑿, 𝒀), denoted by 𝐷 ∼ (𝑿, 𝒀), if (i) 𝐷 ∼ 𝑿 and (ii) for any M-reversible arc 𝑢 → 𝑣 inconsistent with 𝒚, 𝜑(𝐷,𝑢,𝑣) 𝑿. We say D(𝑖,𝑟) ∼ (𝑿, 𝒀) if there is some 𝐷 ∈ D(𝑖,𝑟) such that 𝐷 ∼ (𝑿, 𝒀).

e intuition of the notion “consistency” is as follows. Suppose 𝑢 → 𝑣 in a M-reversible arc in 𝐷, and both 𝐷 and𝜑(𝐷,𝑢,𝑣) are consistent with the resampling table. But 𝐷 and𝜑(𝐷,𝑢,𝑣) cannot both occur. It is according to the auxiliary table to which one of 𝐷 and𝜑(𝐷,𝑢,𝑣) we assign (𝐷 ∼ 𝑿)∧(𝜑(𝐷,𝑢,𝑣) ∼ 𝑿).

Lemma 3.1. For each 𝑖 ∈ [𝑚] and 𝑟 ∈ N+, P𝑿 [D(𝑖,𝑟) ∼ 𝑿] = P𝑿,𝒀 [D(𝑖,𝑟) ∼ (𝑿, 𝒀)].

Proof. Fix an arbitrary assignment 𝒙 of 𝑿 and an arbitrary assignment 𝒚 of 𝒀. Suppose D(𝑖,𝑟) ∼ 𝒙, i.e, ∃𝐷0 ∈ D(𝑖,𝑟) such that 𝐷 ∼ 𝒙. We will show that there must exist some 𝐷 ∈ D(𝑖,𝑟) such that 𝐷 ∼ (𝒙,𝒚). is will imply the conclusion immediately.

We apply the following procedure to nd such a pwdag 𝐷 ∈ D(𝑖,𝑟).

- 1 Initially, 𝑘 = 0;
- 2 while ∃ an M-reversible arc 𝑢𝑘 → 𝑣𝑘 in 𝐷𝑘 inconsistent with 𝒚 such that 𝜑(𝐷𝑘,𝑢𝑘,𝑣𝑘) ∼ 𝒙 do

- 3 let 𝐷𝑘+1 := 𝜑(𝐷𝑘,𝑢𝑘,𝑣𝑘) and 𝑘 := 𝑘 + 1;

- 4 Return 𝐷𝑘;


By induction on 𝑘, it is easy to check that 𝐷𝑘 ∼ 𝒙 and 𝐷𝑘 ∈ D(𝑖,𝑟) for each 𝑘. Furthermore, if the procedure terminates, then in the nal wdag 𝐷, for every M-reversible arc 𝑢 → 𝑣 inconsistent with 𝒚, we have that 𝜑(𝐷,𝑢,𝑣) 𝒙. So 𝐷 ∼ (𝒙,𝒚). In the following, we will show that the procedure always terminates, which nishes the proof.

Note that each 𝐷𝑘 has no more nodes than 𝐷0 and that there are nite number of wdags in D(𝑖,𝑟) with no more nodes than 𝐷0, so it suces to prove that each wdag appears at most once in the procedure.

By contradiction, assume 𝐷𝑗 = 𝐷𝑘 for some 𝑗 ≤ 𝑘. Recall that 𝑢𝑗 → 𝑣𝑗 is reversible in 𝐷𝑗 and inconsistent with 𝒚. So 𝑦𝐿𝜆((𝑢𝑣𝑗,𝐷𝑗)−1

𝑗),𝐿(𝑣𝑗) = 𝑦𝐿𝜆((𝑢𝑢𝑗,𝐷𝑗)

𝑗),𝐿(𝑣𝑗) = 𝐿(𝑣𝑗).

Let 𝐷ℓ be the last wdag in 𝐷𝑗+1, · · · ,𝐷𝑘 such that 𝜆(𝑣𝑗,𝐷ℓ) < 𝜆(𝑣𝑗,𝐷𝑗). Observing that 𝜆(𝑣𝑗,𝐷𝑗+1) = 𝜆(𝑣𝑗,𝐷𝑗) − 1, we have such 𝐷ℓ must exist. By 𝜆(𝑣𝑗,𝐷𝑘) = 𝜆(𝑣𝑗,𝐷𝑗), we have 𝜆(𝑣𝑗,𝐷ℓ) = 𝜆(𝑣𝑗,𝐷𝑗) − 1, 𝜆(𝑣𝑗,𝐷ℓ+1) = 𝜆(𝑣𝑗,𝐷𝑗). erefore, 𝜆(𝑣𝑗,𝐷ℓ+1) = 𝜆(𝑣𝑗,𝐷ℓ) + 1. Combining with that 𝑢ℓ → 𝑣ℓ is the inconsistent arc in 𝐷ℓ which is reversed in 𝐷ℓ+1, we have 𝑢ℓ = 𝑣𝑗, (𝐿(𝑢𝑗),𝐿(𝑣𝑗)) = (𝐿(𝑢ℓ),𝐿(𝑣ℓ)) ∈ M

ℓ),𝐿(𝑣ℓ) = 𝐿(𝑢𝑗). Note that 𝜆(𝑣ℓ,𝐷ℓ) = 1 + 𝜆(𝑢ℓ,𝐷ℓ) = 1 + 𝜆(𝑣𝑗,𝐷ℓ). Combining with 𝜆(𝑢𝑗,𝐷𝑗) = 𝜆(𝑣𝑗,𝐷𝑗) − 1, we have 𝜆(𝑢ℓ,𝐷ℓ) = 𝜆(𝑢𝑗,𝐷𝑗). Combining with𝑦𝐿𝜆((𝑢𝑢ℓ,𝐷ℓ)

and 𝑦𝐿𝜆((𝑢𝑢ℓ,𝐷ℓ)

ℓ),𝐿(𝑣ℓ) = 𝐿(𝑣ℓ). us we have 𝐿(𝑣ℓ) = 𝐿(𝑢𝑗) and 𝑦𝐿𝜆((𝑢𝑢ℓ,𝐷ℓ)

ℓ),𝐿(𝑣ℓ) = 𝐿(𝑢𝑗), we have𝑦𝐿𝜆((𝑢𝑢𝑗,𝐷𝑗)

ℓ),𝐿(𝑣ℓ) = 𝐿(𝑢𝑗). is is contradicted with 𝑦𝐿𝜆((𝑢𝑢𝑗,𝐷𝑗)

𝑗),𝐿(𝑣𝑗) = 𝐿(𝑣𝑗).

e following two propositions will be used in the proof of Lemma 3.4. e rst proposition is an easy observation, and the second one is a direct application of the Cauchy-Schwarz inequality. For the sake of completeness, we present their proof in the appendix.

- Proposition 3.2. Given any wdag 𝐷, there exists a set P of disjoint M-reversible arcs6 such that: for each 𝑖 ∈ M,


- 1

- 2 · V(𝐷,𝑖).


|{𝑣 : ∃𝑢 such that 𝑢 → 𝑣 or 𝑣 → 𝑢 is in P} ∩ {𝑣 : 𝐿(𝑣) = 𝑖}| ≥

6We say two arc 𝑢 → 𝑣 and 𝑢 → 𝑣 are disjoint if their node sets are disjoint, i.e. {𝑢,𝑣} ∩ {𝑢 ,𝑣 } = ∅.

- Proposition 3.3. Suppose 𝑋,𝑌 and 𝑍 are three independent random variables, 𝐴 is an event determined


by {𝑋,𝑌}, and 𝐴 is an event determined by {𝑌,𝑍}. Let 𝑋1,𝑌1,𝑌2,𝑍1 be four independent samples of 𝑋,𝑌,𝑌,𝑍, respectively. en the following holds with probability at most P(𝐴)P(𝐴 ) − P(𝐴 ∩ 𝐴 )2:

- • 𝐴 is true on (𝑋1,𝑌1), 𝐴 is true on (𝑌2,𝑍1), and
- • either 𝐴 is false on (𝑋1,𝑌2) or 𝐴 is false on (𝑌1,𝑍1).


Now, we are ready to show Lemma 3.4. Lemma 3.4. For each pwdag 𝐷,

### P[𝐷 ∼ (𝑿, 𝒀)] ≤

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣) .

𝑣∈V(𝐷)

𝑣∈V(𝐷)

Proof. Let P be the set of disjoint M-reversible arcs dened in Proposition 3.2. Let 𝑉 (P) denote the set of nodes which appears in P, and 𝑉 (P) consists of the other nodes. Proposition 3.2 says that for each 𝑖 ∈ M,

- 1

- 2 · V(𝐷,𝑖).


𝑉 (P) ∩ {𝑣 : 𝐿(𝑣) = 𝑖}| ≥

For each 𝑣 ∈ 𝑉 (P), let 𝐵𝑣 denote the event that 𝐴𝐿(𝑣) holds on 𝑿𝑣. It is easy to see that P[𝐵𝑣] = 𝑝𝐿(𝑣). Besides,

- Claim 3.5. If 𝐷 ∼ (𝑿, 𝒀), then 𝐵𝑣 holds for each 𝑣 ∈ 𝑉 (P).

Proof. Note that 𝑿𝑣 are the assignments of vbl(𝐴𝐿(𝑣)) just before the time that the MT algorithm picks the event corresponding to 𝑣 to resample. MT algorithm decides to pick 𝐴𝐿(𝑣) only if 𝐴𝐿(𝑣) holds. Hence 𝐴𝐿(𝑣) must hold on 𝑿𝑣.

Let 𝑢 → 𝑣 be an arc in P, where 𝐿(𝑢) = 𝑖 and 𝐿(𝑣) = 𝑖 . en by the denition of P, we have 𝑢 → 𝑣 is reversible in 𝐷. Let 𝐷 be the wdag obtained by reversing the direction of 𝑢 → 𝑣 in 𝐷. Recalling the denition of 𝑿𝐷 ,𝑣, one can verify that

𝑿𝐷 ,𝑢 := 𝑋𝑗,L(𝑣,𝑗) : 𝑋𝑗 ∈ vbl 𝐴𝑖 ∩ vbl 𝐴𝑖 ∪ 𝑋𝑗,L(𝑢,𝑗) : 𝑋𝑗 ∈ vbl 𝐴𝑖 \ vbl 𝐴𝑖 and

𝑿𝐷 ,𝑣 := 𝑋𝑗,L(𝑢,𝑗) : 𝑋𝑗 ∈ vbl 𝐴𝑖 ∩ vbl 𝐴𝑖 ∪ 𝑋𝑗,L(𝑣,𝑗) : 𝑋𝑗 ∈ vbl 𝐴𝑖 \ vbl 𝐴𝑖 . For simplicity, let 𝜆 := 𝜆(𝑢,𝐷). We dene 𝐵𝑢,𝑣 to be the event that the following hold:

- (a) 𝐴𝑖 holds on 𝑋𝑢, and 𝐴𝑖 holds on 𝑋𝑣;
- (b) If 𝑌𝑖,𝑖𝜆 = 𝑖 , then either 𝐴𝑖 is false on 𝑿𝐷 ,𝑢 or 𝐴 𝑖 is false on 𝑿𝐷 ,𝑣.


Conditioned on that 𝑌𝑖,𝑖𝜆 = 𝑖, 𝐵𝑢,𝑣 happens with probability 𝑝𝑖𝑝𝑖 . Condition on that 𝑌𝑖,𝑖𝜆 = 𝑖 , by using Proposition 3.3, 𝐵𝑢,𝑣 happens with probability at most 𝑝𝑖𝑝𝑖 − 𝛿𝑖,𝑖2 . us,

P[𝐵𝑢,𝑣] ≤ P[𝑌𝑖,𝑖𝜆 = 𝑖]𝑝𝑖𝑝𝑖 + P[𝑌𝑖,𝑖𝜆 = 𝑖 ] 𝑝𝑖𝑝𝑖 − 𝛿𝑖,𝑖2 ≤ ≤ 𝑝𝑖𝑝𝑖 (1 − 2𝑐𝑖)(1 − 2𝑐𝑖 ).

- 1

- 2 · 𝑝𝑖𝑝𝑖 +


- 1

- 2 · 𝑝𝑖𝑝𝑖 − 𝛿𝑖,𝑖2


- Claim 3.6. If 𝐷 ∼ (𝑿, 𝒀), then 𝐵𝑢,𝑣 holds for each 𝑢 → 𝑣 in P.


Proof. Suppose 𝐷 ∼ (𝑿, 𝒀). Similar to the argument in Claim 3.5, we can see that Item (a) holds. In the following, we show Item (b) holds.

By contradiction, assume 𝑌𝑖,𝑖𝜆 = 𝑖 , 𝐴𝑖 holds on 𝑿𝐷 ,𝑢, and 𝐴𝑖 holds on 𝑿𝐷 ,𝑣. en, we have 𝑢 → 𝑣 in 𝐷 is inconsistent with 𝒀 and 𝐷 ∼ 𝑿. us, 𝜑(𝐷,𝑢,𝑣) ∼ 𝑿 since 𝜑(𝐷,𝑢,𝑣) is a prex of 𝐷 . By denition, we have 𝐷 (𝑿, 𝒀), a contradiction.

Since the events {𝐵𝑣 : 𝑣 ∈ 𝑉 (P)} and {𝐵𝑢,𝑣 : 𝑢 → 𝑣 is in P} depend on distinct entries of 𝑿 and 𝒀, they are mutually independent. erefore,

### P [𝐷 ∼ (𝑿, 𝒀)] ≤ P 

𝐵𝑢,𝑣 

=

### P(𝐵𝑤)

P(𝐵𝑢,𝑣)

𝐵𝑤

  𝑤∈𝑉 (P)

 

𝑢→𝑣 is in P

𝑢→𝑣 is in P

𝑤∈𝑉 (P)

𝑝𝐿(𝑢)𝑝𝐿(𝑣) 1 − 2𝑐𝐿(𝑢) 1 − 2𝑐𝐿(𝑢)

≤

𝑝𝐿(𝑤)

𝑢→𝑣 is in P

𝑤∈𝑉 (P)

### =

𝑝𝐿(𝑣) ·

𝑣 in 𝐷

(1 − 2𝑐𝑖)|P∩{𝑣:𝐿(𝑣)=𝑖}|

𝑖∈[𝑚]

### ≤

𝑝𝐿(𝑣) ·

𝑣 in 𝐷

### (1 − 2𝑐𝑖)|V(𝑖) |/2 ≤

𝑖∈[𝑚]

𝑝𝐿(𝑣) ·

𝑣 in 𝐷

(1 − 𝑐𝑖)|V(𝑖) |

𝑖∈[𝑚]

=

𝑝𝐿(𝑣)

𝑣∈V(𝐷)

𝑝 𝐿(𝑣) .

𝑣∈V(𝐷)

Now we are ready to prove the main theorem of this subsection.

- eorem 3.7. E[𝑇] ≤ 𝐷∈D(𝐺𝐷) 𝑣∈V(𝐷) 𝑝𝐿(𝑣) 𝑣∈V(𝐷) 𝑝 𝐿(𝑣) . Proof. First, according to Lemmas 3.1 and 3.4,


### P[𝜒D(𝑖,𝑟)] ≤ P[D(𝑖,𝑟) ∼ 𝑿] = P[D(𝑖,𝑟) ∼ (𝑿, 𝒀)] ≤ ∑︁

𝐷∈D(𝑖,𝑟)

≤ ∑︁

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣) .

𝐷∈D(𝑖,𝑟) 𝑣∈V(𝐷)

𝑣∈V(𝐷)

en, by Fact 2.3 and the above inequality, we have

### P[𝜒D(𝑖,𝑟)] ≤ ∑︁

∑︁

∑︁

### E[𝑇] = ∑︁

∑︁

𝑝𝐿(𝑣)

𝑟 ∈N+

𝑟 ∈N+

𝑖∈[𝑚]

𝐷∈D(𝑖,𝑟) 𝑣∈V(𝐷)

𝑖∈[𝑚]

≤ ∑︁

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣) .

𝐷∈D(𝐺𝐷) 𝑣∈V(𝐷)

𝑣∈V(𝐷)

P[𝐷 ∼ (𝑿, 𝒀)]

𝑝 𝐿(𝑣)

𝑣∈V(𝐷)

- 3.2. Mapping between wdags. In this section, we will prove eorem 3.13, which provides a upper bound of E[𝑇] in terms of 𝒑−.


- Denition 3.8 (Homomorphic dependency graph). Given a dependency graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and a matching M of 𝐺𝐷, we dene a graph 𝐺M = (𝑉 M,𝐸M) homomorphic to 𝐺𝐷 respected to M as follows.


- • 𝑉 M = [𝑚] \ {𝑖0,𝑖1 : (𝑖0,𝑖1) ∈ M} ∪ {𝑖0↑,𝑖0↓,𝑖1↑,𝑖1↓ : (𝑖0,𝑖1) ∈ M};
- • ∀(𝑖0,𝑖1) ∈ 𝐸𝐷, each pair of vertices in {𝑖0,𝑖1,𝑖0↑,𝑖0↓,𝑖1↑,𝑖1↓} ∩𝑉 M are connected in 𝐺M.


Besides, we associate a probability vector 𝒑M with 𝐺M as follows:

 

𝑝 𝑖 if 𝑣 = 𝑖↑ for some 𝑖 ∈ [𝑚], 𝑝𝑖− − 𝑝 𝑖 if 𝑣 = 𝑖↓ for some 𝑖 ∈ [𝑚], 𝑝𝑖− otherwise, 𝑣 = 𝑖 for some 𝑖 ∈ [𝑚].

∀𝑣 ∈ 𝑉 M : 𝑝𝑣M =

 

![image 4](<2021-he-moser-tardos-algorithm-beyond-shearer_images/imageFile4.png>)

F      3. (a) a dependency graph 𝐺𝐷; (b) the 𝐺M when M = {(2, 3)}.

In fact, (𝐺𝐷,𝒑−) and (𝐺M,𝒑M) are essentially the same: suppose A ∼ (𝐺𝐷,𝒑−), then for each 𝑖 ∈ M, we view 𝐴𝑖 as the union of two mutually exclusive events 𝐴𝑖↑ ∪ 𝐴𝑖↓ whose probabilities are 𝑝 𝑖 and 𝑝− − 𝑝 𝑖 respectively. Such a representation of A is of the seing (𝐺M,𝒑M).

We have the following proposition, whose proof can be found in the appendix. Proposition 3.9. 𝐷 ∈D(𝐺M) 𝑣 in 𝐷 𝑝𝐿M (𝑣 ) = 𝐷∈D(𝐺𝐷) 𝑣 in 𝐷 𝑝𝐿−(𝑣).

Given a pwdag 𝐷 = (𝑉,𝐸,𝐿), recall that V(𝐷) is the set of nodes of M-reversible arcs in 𝐷. Dene

ℳ(𝐷) {𝑣 : 𝐿(𝑣) ∈ M} to be the set of nodes 𝑣 in 𝐷 where 𝐿(𝑣) is contained in an edge in M. Obviously, V(𝐷) ⊆ ℳ(𝐷). For simplicity of notations, we will omit 𝐷 from the notations if 𝐷 is clear from the context.

Given a pwdag 𝐷 = (𝑉,𝐸,𝐿), we use 𝒮 = {𝒮1,𝒮2,𝒮3,𝒮4} to represent a partition of ℳ(𝐷) where V ⊆ 𝒮1 (some of these four sets are possibly empty). Let 𝜓(𝐷) denote the set consisting of all such partitions. e formal denition is as follows.

- Denition 3.10 (Partition). Given a pwdag 𝐷 = (𝑉,𝐸,𝐿) of 𝐺𝐷, dene 𝜓(𝐷) {{𝒮1,𝒮2,𝒮3,𝒮4} : V ⊆ 𝒮1 and ℳ = 𝒮1 𝒮2 𝒮3 𝒮4}.


Given a wdag 𝐷, there may be two or more topological ordering of 𝐷. We x an arbitrary topological ordering, and denote it by 𝜋𝐷. In the following, we dene an injection ℎ from {(𝐷,𝒮) : 𝐷 ∈ D(𝐺𝐷),𝒮 ∈ 𝜓(𝐷)} to D(𝐺M).

Denition 3.11. Given a pwdag 𝐷 and 𝒮 ∈ 𝜓(𝐷), dene ℎ(𝐷,𝒮) to be a directed graph 𝐷 = (𝑉 ,𝐸 ,𝐿 ) constructed as follows.

Constructing 𝑉 . 𝑉 = 𝑉 1 𝑉 2 where |𝑉 1| = |𝑉 | and |𝑉 2| = |𝒮3 ∪ 𝒮4|. For convenience of presentation, we x two bijections 𝑓 : 𝑉 → 𝑉 1 and 𝑓 ∗ : 𝒮3 ∪ 𝒮4 → 𝑉 2 to name nodes in 𝑉 . In order to distinguish between nodes in 𝐷 and those in 𝐷 , we will always use 𝑢,𝑣,𝑤 to represent the nodes of 𝐷 and 𝑢 ,𝑣 ,𝑤 to present the nodes of 𝐷 . Given 𝑣 ∈ 𝑉 , we use 𝑔(𝑣 ) to denote the unique node 𝑣 ∈ 𝑉 such that 𝑓 (𝑣) = 𝑣

(if 𝑣 ∈ 𝑉 1) or 𝑓 ∗(𝑣) = 𝑣 (if 𝑣 ∈ 𝑉 2). Description of 𝐿 . For each node 𝑣 ∈ 𝑉 1, where 𝑣 = 𝑓 (𝑣),

- (2) 𝐿 (𝑣 ) =

 

 

(𝐿(𝑣))↑, if 𝑣 ∈ 𝒮1, (𝐿(𝑣))↓, if 𝑣 ∈ 𝒮2 ∪ 𝒮3 ∪ 𝒮4, 𝐿(𝑣), otherwise, 𝑣 ∉ ℳ.

For each node 𝑣 ∈ 𝑉 2, assuming 𝑣 ∈ 𝒮3 ∪ 𝒮4 is the node such that 𝑣 = 𝑓 ∗(𝑣) and 𝑖 ∈ [𝑚] is the node such that ((𝐿(𝑣),𝑖) ∈ M,

- (3) 𝐿 (𝑣 ) =


𝑖↑, if 𝑣 ∈ 𝒮3, 𝑖↓, otherwise, 𝑣 ∈ 𝒮4.

Constructing 𝐸 . 𝐸 = 𝐸 1 𝐸 2 where 𝐸 1 = {𝑓 ∗(𝑣) → 𝑓 (𝑣) : 𝑣 ∈ 𝒮3 ∪ 𝒮4} and 𝐸 2 = {𝑢 → 𝑣 : (𝐿 (𝑢 ) = 𝐿 (𝑣 ) ∨ (𝐿 (𝑢 ),𝐿 (𝑣 )) ∈ 𝐸M) ∧ (𝑔(𝑢 ) ≺ 𝑔(𝑣 ) in 𝜋𝐷)}.

- eorem 3.12. ℎ(·, ·) is an injection from {(𝐷,𝒮) : 𝐷 ∈ D(𝐺𝐷),𝒮 ∈ 𝜓(𝐷)} to D(𝐺M).


e proof of eorem 3.12 is in the appendix. Now we can prove the main theorem of this subsection.

- eorem 3.13. 𝐷∈D(𝐺𝐷) 𝑣∈V(𝐷) 𝑝𝐿(𝑣) 𝑣∈V(𝐷) 𝑝 𝐿(𝑣) ≤ 𝐷∈D(𝐺𝐷) 𝑣 in 𝐷 𝑝𝐿−(𝑣). Proof. For each 𝑖 ∈ [𝑚] where (𝑖, 𝑗) ∈ M, let


𝑞𝑖1 𝑝 𝑖, 𝑞𝑖2 𝑝𝑖− − 𝑝 𝑖, 𝑞𝑖3 (𝑝𝑖− − 𝑝 𝑖)𝑝 𝑗, and 𝑞𝑖4 (𝑝𝑖− − 𝑝 𝑖)(𝑝−𝑗 − 𝑝 𝑗). According to Fact 2.7, 𝑞𝑖1 + 𝑞𝑖2 + 𝑞𝑖3 + 𝑞𝑖4 = 𝑝𝑖− + 𝑝−𝑗 (𝑝𝑖− − 𝑝 𝑖) ≥ 𝑝𝑖.

Given 𝐷 = (𝑉,𝐸,𝐿) ∈ D(𝐺𝐷) and 𝒮 ∈ 𝜓(𝐷), let 𝐷 = ℎ(𝐷,𝒮). For each 𝑣 in 𝐷 where (𝐿(𝑣), 𝑗) ∈ M for some 𝑗 ∈ [𝑚], according to the denition of 𝒑M, (2), and (3), we have that

- • if 𝑣 ∈ 𝒮1, then 𝑝𝐿M (𝑓 (𝑣)) = 𝑝 𝐿(𝑣) = 𝑞𝐿1(𝑣);
- • if 𝑣 ∈ 𝒮2, then 𝑝𝐿M (𝑓 (𝑣)) = 𝑝𝐿−(𝑣) − 𝑝 𝐿(𝑣) = 𝑞𝐿2(𝑣);
- • if 𝑣 ∈ 𝒮3, then 𝑝𝐿M (𝑓 (𝑣)) · 𝑝𝐿M (𝑓∗(𝑣)) = (𝑝𝐿−(𝑣) − 𝑝 𝐿(𝑣))𝑝 𝑗 = 𝑞𝐿3(𝑣);
- • if 𝑣 ∈ 𝒮4, then 𝑝𝐿M (𝑓 (𝑣)) · 𝑝𝐿M (𝑓∗(𝑣)) = (𝑝𝐿−(𝑣) − 𝑝 𝐿(𝑣))(𝑝−𝑗 − 𝑝 𝑗) = 𝑞𝐿4(𝑣).


Moreover, for each𝑢 ∈ 𝑉 \ℳ(𝐷) = V(𝐷) \ℳ(𝐷), we have 𝑝𝐿M (𝑓 (𝑣)) = 𝑝𝐿(𝑣). us, for each 𝒮 ∈ 𝜓(𝐷),

𝑝𝐿M (𝑣 ) =

𝑞𝐿1(𝑣)

𝑞𝐿2(𝑣)

𝑞𝐿3(𝑣)

𝑞𝐿4(𝑣)

𝑝𝐿(𝑣)

𝑣 in ℎ(𝐷,𝒮)

𝑣∈𝒮1

𝑣∈𝒮2

𝑣∈𝒮3

𝑣∈𝒮4

𝑣∈V\ℳ

𝑞𝐿1(𝑣)

𝑞𝐿2(𝑣)

𝑞𝐿3(𝑣)

𝑞𝐿4(𝑣).

=

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣)

𝑣∈V

𝑣∈𝒮2

𝑣∈𝒮3

𝑣∈𝒮4

𝑣∈𝒮1\V

𝑣∈V\ℳ

So

### ∑︁

### 𝑝𝐿M (𝑣 ) = ∑︁

𝑞𝐿1(𝑣)

𝑞𝐿2(𝑣)

𝑞𝐿3(𝑣)

𝑞𝐿4(𝑣)

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣)

𝒮∈𝜓 (𝐷) 𝑣 in ℎ(𝐷,𝒮)

𝑣∈V

𝑣∈𝒮2

𝑣∈𝒮3

𝑣∈𝒮4

𝑝 𝐿(𝑣) ∑︁

𝒮∈𝜓 (𝐷) 𝑣∈V\ℳ

𝑣∈𝒮1\V

𝑞𝐿1(𝑣)

𝑞𝐿2(𝑣)

𝑞𝐿4(𝑣)

𝑞𝐿3(𝑣)

=

𝑝𝐿(𝑣)

𝑣∈V

𝑣∈𝒮4

𝑣∈𝒮2

𝑣∈𝒮3

𝒮∈𝜓 (𝐷) 𝑣∈𝒮1\V

𝑣∈V\ℳ

𝑞𝐿1(𝑣) + 𝑞𝐿2(𝑣) + 𝑞𝐿3(𝑣) + 𝑞𝐿4(𝑣)

=

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣)

𝑣∈V

𝑣∈ℳ\V

𝑣∈V\ℳ

≥

𝑝𝐿(𝑣)

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣)

𝑣∈V

𝑣∈ℳ\V

𝑣∈V\ℳ

=

𝑝𝐿(𝑣)

𝑝 𝐿(𝑣),

𝑣∈V

𝑣∈V

where the third equality is according to the denition of 𝜓(𝐷). Finally,

∑︁

𝑝 𝐿(𝑣) ≤ ∑︁

∑︁

### 𝑝𝐿M (𝑣 ) ≤ ∑︁

𝑝𝐿M (𝑣 )

𝑝𝐿(𝑣)

𝐷 ∈D(𝐺M) 𝑣 in 𝐷

𝒮∈𝜓 (𝐷) 𝑣 in ℎ(𝐷,𝒮)

= ∑︁

𝐷∈D(𝐺𝐷) 𝑣∈V(𝐷)

𝑣∈V(𝐷)

𝐷∈D(𝐺𝐷)

𝑝𝐿−(𝑣), where the second inequality is due to eorem 3.12 and the equality is by Proposition 3.9. 3.3. Putting all things together. e following lemma is implicitly proved in [ KS11].

𝐷∈D(𝐺𝐷) 𝑣 in 𝐷

- Lemma 3.14 ([KS11]). For any undirected graph𝐺𝐷 = ([𝑚],𝐸𝐷) and probability vector 𝒑 ∈ I𝑎(𝐺𝐷)/(1+


𝜀), 𝑖∈[𝑚] 𝑞𝑞{𝑖}(𝐺𝐷,𝒑)

∅(𝐺𝐷,𝒑) ≤ 𝑚/𝜀.

eorem 1.6 (restated). For any A ∼ (𝐺𝐷,𝒑, M, 𝜹), if (1 +𝜀) · 𝒑− ∈ I𝑎(𝐺𝐷), then the expected number of resampling steps performed by MT algorithm is most 𝑚/𝜀, where 𝑚 is the number of events in A.

Proof. Fix any such A. We have that E[𝑇] ≤ ∑︁

𝑞{𝑖}(𝐺𝐷,𝒑−) 𝑞∅(𝐺𝐷,𝒑−)

𝑚 𝜀

𝑝𝐿−(𝑣) ≤ 𝑖∈[𝑚]

≤

,

𝐷∈D(𝐺𝐷) 𝑣 in 𝐷

where the rst inequality is by eorems 3.7 and 3.13, the second inequality is due to eorem 4 in [KS11], and the last inequality is according to Lemma 3.14.

4. L    

In order to explore how far beyond Shearer’s bound MT algorithm is still ecient in general, we provide a lower bound on the amount of intersection between dependent events for general instances (eorem 4.1).

We rst introduce some notations. Given a bipartite graph 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵), we call the vertex 𝑖 ∈ [𝑚] le vertex and the vertex 𝑗 ∈ [𝑛] right vertex. We call 𝐺𝐵 linear7 if any two le vertices in [𝑚] share at most one common neighbor in [𝑛]. Let Δ𝐷(𝐺𝐵) denote the maximum degree of 𝐺𝐷(𝐺𝐵), and Δ𝐵(𝐺𝐵) denote the maximum degree of the le vertices in 𝐺𝐵. If 𝐺𝐵 is clear from the context, we may omit 𝐺𝐵 from these notations. In addition, for a bipartite graph 𝐺 = (𝐿 ⊂ [𝑚],𝑅,𝐸) and a probability vector 𝒑 ∈ (0, 1)𝑚, we dene 8

min𝑖∈𝐿 𝑝𝑖 2 · −| ∪𝑖∈𝐿 N𝐺(𝑖)| + 𝑖∈𝐿 |N𝐺(𝑖)| · 𝑝𝑖1/|N𝐺(𝑖) | √︁|𝐿| · Δ𝐷(𝐺) · Δ𝐵(𝐺)2

(𝐺,𝒑)

.

and +(𝐺,𝒑) max{ (𝐺,𝒑), 0}.

We use A ∼ (𝐺𝐵,𝒑) to denote that (i)𝐺𝐵 is an event-variable graph of A and (ii) the probability vector of A is 𝒑. Let M = {(𝑖1,𝑖 1), (𝑖2,𝑖 2), · · · } be a matching of𝐺𝐷(𝐺𝐵), and 𝜹 = (𝛿𝑖1,𝑖

, · · · ) ∈ (0, 1)|M| be another probability vector. We say that an event set A is of the seing (𝐺𝐵,𝒑, M, 𝜹), and write A ∼ (𝐺𝐵,𝒑, M, 𝜹), if A ∼ (𝐺𝐵,𝒑) and P(𝐴𝑖 ∩ 𝐴𝑖 ) ≥ 𝛿𝑖,𝑖 for each pair (𝑖,𝑖 ) ∈ M.

,𝛿𝑖2,𝑖

1

2

We call an event 𝐴 elementary, if 𝐴 can be wrien as (𝑋𝑖1 ∈ 𝑆𝑖1) ∧ (𝑋𝑖2 ∈ 𝑆𝑖2) ∧ · · · ∧ (𝑋𝑖𝑘 ∈ 𝑆𝑖𝑘)

where 𝑆𝑖1, · · · ,𝑆𝑖𝑘 are subsets of the domains of variables. We call an event set A elementary if all events in A are elementary.

- eorem 4.1. Let 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵) be a bipartite graph, 𝒑 ∈ (0, 1]𝑚 be a probability vector, and 𝐿1,𝐿2, · · · ,𝐿𝑡 be a collection of disjoint subsets of [𝑚]. For each 𝑘 ∈ [𝑡], let𝐺𝑘 denote the induced subgraph


on 𝐿𝑘 ∪ ∪𝑖∈𝐿𝑘N𝐺𝐵(𝑖) and 𝐸𝑘 denote the edge set of 𝐺𝐷(𝐺𝑘). If all 𝐺𝑘’s are linear, then the following holds.

If A ∼ (𝐺𝐵,𝒑), then there is a matching M of 𝐺𝐷(𝐺𝐵) satisfying that (𝑖,𝑖 )∈M∩𝐸𝑘 P(𝐴𝑖 ∩ 𝐴𝑖 )2 ≥ ( +(𝐺𝑘,𝒑))2 for any 𝑘.

e proof of eorem 4.1 mainly consists of two parts. First, we show that there is an elementary event set which approximately achieves the minimum amount of intersection between dependent events (Lemma 4.2). en, for elementary event sets, by applying AM-GM inequality, we obtain a lower bound on the total amount of overlap on common variables, which further implies a lower bound on the amount of intersection between dependent events (Lemma 4.5).

- Lemma 4.2. Let 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵) be a linear bipartite graph, 𝐸𝐷 be the edge set of 𝐺𝐷(𝐺𝐵), and 𝒑 ∈ (0, 1]𝑚 is a probability vector. Let𝛾 denote the minimum (𝑖0,𝑖1)∈𝐸𝐷 P[𝐴𝑖0 ∩𝐴𝑖1] among all event sets


A = (𝐴1, · · · ,𝐴𝑚) ∼ (𝐺𝐵,𝒑). en there is an elementary event set A such that (𝑖0,𝑖1)∈𝐸𝐷 P[𝐴 𝑖

### ] ≤ (Δ𝐵(𝐺𝐵))2 ·𝛾.

∩𝐴 𝑖

0

1

Proof. For simplicity, we let Δ Δ𝐵(𝐺𝐵). Without loss of generality, we assume that each random variable𝑋𝑖 is uniformly distributed over [0, 1]. Let A ∼ (𝐺𝐵,𝒑) be an event set where (𝑖0,𝑖1)∈𝐸𝐷 P[𝐴𝑖 ∩

- 7e notion is not arbitrary. e bipartite graph 𝐺𝐵 can be represented by a hypergraph in a natural way: each right vertex 𝑗 is represented by a node 𝑣𝑗 in the hypergraph, each le vertex 𝑖 is represented by a hyperedge 𝑒𝑖, and 𝑣𝑗 is in 𝑒𝑖 if and only if (𝑖, 𝑗) ∈ 𝐸𝐵. A hypergraph is called linear if any two hyperedges share at most one node.
- 8It is possible that (𝐺,𝒑) < 0.


𝐴𝑗] = 𝛾. We will replace 𝐴𝑖 with an elementary 𝐴 𝑖 one by one for each 𝑖 = 1, 2, · · · ,𝑚, so that the resulted event set A satises (𝑖0,𝑖1)∈𝐸𝐷 P[𝐴 𝑖

### ] ≤ Δ2 · (𝑖0,𝑖1)∈𝐸𝐷 P[𝐴𝑖0 ∩ 𝐴𝑖1] = Δ2 ·𝛾.

∩ 𝐴 𝑖

0

1

More precisely, x 𝑖 ∈ [𝑚] and suppose 𝐴1, · · · ,𝐴𝑖−1 have been replaced with elementary events 𝐴 1, · · · ,𝐴 𝑖−1 respectively. For simplicity of notations, for any pair 𝑖0 < 𝑖1, we abbreviate P[𝐴𝑖0 ∩ 𝐴𝑖1], P[𝐴 𝑖

0,𝑖1 respectively. Without loss of generality, we assume 𝐴𝑖 depends on variables 𝑋1,𝑋2, · · · ,𝑋𝑘. For every 𝑗 ∈ [𝑘], we dene

∩𝐴𝑖1] and P[𝐴 𝑖

] to 𝑝𝑖0,𝑖1, 𝑝 𝑖

0,𝑖1 and 𝑝 𝑖

∩𝐴 𝑖

0

0

1

### 𝑃𝑗(𝑥𝑗) := ∑︁

### 1 Δ · P[𝐴 𝑖0 | 𝑋𝑗 = 𝑥𝑗] + ∑︁

P[𝐴𝑖0 | 𝑋𝑗 = 𝑥𝑗].

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

for 𝑥𝑗 ∈ [0, 1]. Without loss of generality, we assume 𝑃𝑗(·) is non-decreasing. Let 𝜇 : [0, 1]𝑘 → {0, 1} be the indicator of 𝐴𝑖, then

### ∫

𝜇(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘 = P[𝐴𝑖], For each 𝑗 ∈ [𝑘], let

𝑥1,···,𝑥𝑘

### 𝜇𝑗(𝑥𝑗) := P[𝐴𝑖 | 𝑋𝑗 = 𝑥𝑗] = ∫

### 𝜇(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑗−1d𝑥𝑗+1 · · · d𝑥𝑘.

𝑥1,···,𝑥𝑗−1,𝑥𝑗+1,···,𝑥𝑘

Noticing that 𝐺𝐵 is linear (i.e., any two events share at most one common variable), we have

### ∫

### Δ + ∑︁

### 𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗 = ∑︁

𝑝 𝑖

0,𝑖

- (4) 𝑝𝑖0,𝑖.


𝑥𝑗

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

Let 𝐴 𝑖 be an elementary event such that it happens if and only if (𝑥1, · · · ,𝑥𝑘) ∈ [0,𝑞1] × · · · × [0,𝑞𝑘]. Here 𝑞1, · · · ,𝑞𝑘 is a set of positive real numbers satisfying that

- (i) Π𝑘𝑗=1𝑞𝑗 = P[𝐴𝑖]. at is, P[𝐴 𝑖] = P[𝐴𝑖];
- (ii) ∫


𝑥2≥𝑞2 𝜇2(𝑥2)d𝑥2 · · · = ∫

𝑥1≥𝑞1 𝜇1(𝑥1)d𝑥1 = ∫

𝑥𝑘≥𝑞𝑘 𝜇𝑘(𝑥𝑘)d𝑥𝑘.

- Claim 4.3. Such {𝑞1, · · · ,𝑞𝑘} exists. us so does 𝐴 𝑖.

Proof. We prove a generalized statement in which Π𝑘𝑗=1𝑞𝑗 can be required to be an arbitrary number in [0, 1]. Our proof is by induction on 𝑘. e base case when 𝑘 = 1 is trivial. Now we assume that for any

preset 𝑞 ∈ (0, 1], there exist {𝑞1, · · · ,𝑞𝑘−1} satisfying that

- (i) Π𝑘𝑗=−11𝑞𝑗 = 𝑞 and
- (ii) ∫


𝑥1≥𝑞1 𝜇1(𝑥1)d𝑥1 = · · · = ∫

𝑥𝑘−1≥𝑞𝑘−1 𝜇𝑘−1(𝑥𝑘−1)d𝑥𝑘−1. Let 𝑓 (𝑞 ) denote the minimum ∫

𝑥1≥𝑞1 𝜇1(𝑥1)d𝑥1 among all such {𝑞1, · · · ,𝑞𝑘−1}’s. It is easy to see that 𝑓 (1) = 0 and 𝑓 is continuous and non-increasing.

Fix an arbitrary𝑞 ∈ [0, 1]. We dene 𝑔(𝑞 ) := ∫

𝑥𝑘≥𝑞/𝑞 𝜇𝑘(𝑥𝑘)d𝑥𝑘 for𝑞 ∈ [𝑞, 1]. Obviously,𝑔(𝑞) = 0 and 𝑔 is continuous and non-decreasing. So there must exist a 𝑞∗ ∈ [𝑞, 1] such that 𝑔(𝑞∗) = 𝑓 (𝑞∗). en let {𝑞1∗, · · · ,𝑞𝑘∗−1} be a set of positive real numbers where

- (i) Π𝑘𝑗=−11𝑞∗𝑗 = 𝑞∗ and
- (ii) 𝑓 (𝑞∗) = ∫


𝑥1≥𝑞1∗ 𝜇1(𝑥1)d𝑥1 = · · · = ∫

𝑥𝑘−1≥𝑞𝑘∗−1 𝜇𝑘−1(𝑥𝑘−1)d𝑥𝑘−1. Let 𝑞𝑘∗ = 𝑞/𝑞∗. It is obvious that Π𝑘𝑗=1𝑞∗𝑗 = 𝑞 and 𝑓 (𝑞∗) = 𝑔(𝑞∗) = ∫

𝑥𝑘≥𝑞𝑘∗ 𝜇𝑘(𝑥𝑘)d𝑥𝑘. is completes the induction step.

- Claim 4.4. For every 𝑗 ∈ [𝑘], we have ∑︁


### 𝑝 𝑖0,𝑖 + Δ · ∑︁

### Δ + ∑︁

### 𝑝 𝑖0,𝑖 ≤ ∑︁

𝑝 𝑖

0,𝑖

𝑝𝑖0,𝑖.

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

Proof. Let 𝜇𝑖 , 𝜇𝑖∩𝑖 , and 𝜇𝑖 \𝑖 denote the indicator functions of the events 𝐴 𝑖, 𝐴 𝑖 ∩ 𝐴𝑖, and 𝐴 𝑖 \ 𝐴𝑖 respectively. Since P[𝐴 𝑖] = P[𝐴𝑖], ∫

∫

### 𝜇𝑘(𝑥𝑘)d𝑥𝑘 ≥ P[𝐴𝑖\𝐴 𝑖] = P[𝐴 𝑖\𝐴𝑖] = ∫

𝜇𝑖 \𝑖(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘. Fix 𝑗 ∈ [𝑘], then

𝜇1(𝑥1)d𝑥1+· · ·+

𝑥1≥𝑞1

𝑥𝑘 ≥𝑞𝑘

𝑥1,···,𝑥𝑘

### ∫

∫

1 𝑘 ·

𝜇𝑖 \𝑖(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘. Since 𝑃𝑗(𝑥𝑗) is non-decreasing and 𝑘 ≤ Δ, we have

𝜇𝑗(𝑥𝑗)d𝑥𝑗 ≥

𝑥𝑗 ≥𝑞𝑗

𝑥1,𝑥2,···,𝑥𝑘

∫

### ∫

1 Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑖 \𝑖(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘. According to Equation 4,

𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗 ≥

𝑥1,𝑥2,···,𝑥𝑘

𝑥𝑗 ≥𝑞𝑗

∫

### ∑︁

### 𝑝 𝑖0,𝑖 + Δ · ∑︁

𝑝𝑖0,𝑖 = Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗

𝑥𝑗

∫

### ∫

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

=Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗 + Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗

∫

### ∫

𝑥𝑗 ≥𝑞𝑗

𝑥𝑗<𝑞𝑗

≥Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑗(𝑥𝑗)d𝑥𝑗 + Δ ·

𝑃𝑗(𝑥𝑗)𝜇𝑖∩𝑖 (𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘

∫

∫

𝑥𝑗 ≥𝑞𝑗

𝑥1,···,𝑥𝑘

≥

𝑃𝑗(𝑥𝑗)𝜇𝑖 \𝑖(𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘 +

𝑃𝑗(𝑥𝑗)𝜇𝑖∩𝑖 (𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘

=∫

𝑥1,···,𝑥𝑘

𝑥1,···,𝑥𝑘

𝑃𝑗(𝑥𝑗)𝜇𝑖 (𝑥1, · · · ,𝑥𝑘)d𝑥1 · · · d𝑥𝑘

𝑥1,···,𝑥𝑘

Δ + ∑︁

= ∑︁

P[𝐴 𝑖

∩ 𝐴 𝑖]

0

### P[𝐴𝑖0 ∩ 𝐴 𝑖].

𝑖0>𝑖,𝑖0∈N𝐺𝐵 (𝑗)

𝑖0<𝑖,𝑖0∈N𝐺𝐵 (𝑗)

is completes the proof. From Claim 4.4, we have

### 𝑝 𝑖0,𝑖 + Δ · ∑︁

### 𝑝 𝑖0,𝑖 ≤ ∑︁

### Δ + ∑︁

### ∑︁

𝑝 𝑖

0,𝑖

- (5) 𝑝𝑖0,𝑖,

By summation over all 𝑖 ∈ [𝑚], we nish the proof:

∑︁

(𝑖0,𝑖)∈𝐸𝐷

𝑝 𝑖

0,𝑖

Δ ≤ Δ · ∑︁

(𝑖0,𝑖)∈𝐸𝐷

𝑝𝑖0,𝑖.

- Lemma 4.5. Let 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵) be a linear bipartite graph and 𝒑 be a probability vector. en for


any elementary A = (𝐴1, · · · ,𝐴𝑚) ∼ (𝐺𝐵,𝒑),

∑︁

(𝑖0,𝑖1)∈𝐸𝐷

P 𝐴𝑖0 ∩ 𝐴𝑖1 ≥

√𝑚 · Δ𝐷(𝐺𝐵) · Δ𝐵(𝐺𝐵)2 · (𝐺𝐵,𝒑),

where 𝐸𝐷 is the edge set of 𝐺𝐷(𝐺𝐵) Proof. For simplicity of notation, we let N stand for N𝐺𝐵. Without loss of generality, we assume that each variable 𝑋𝑖 is uniformly distributed over [0, 1]. As A is elementary, each 𝐴𝑖 can be wrien as

𝑗∈N(𝑖)[𝑋𝑗 ∈ 𝑆𝑖𝑗] where 𝑆𝑖𝑗 ⊂ [0, 1]. Let 𝜇 be the Lebesgue measure. On one hand, according to the AM–GM inequality,

∑︁

𝑖∈[𝑚]

∑︁

𝑗 ∈N(𝑖)

𝜇(𝑆𝑖𝑗) ≥ ∑︁

𝑖∈[𝑚]

|N(𝑖)| · Π𝑗∈N(𝑖)𝜇(𝑆𝑖𝑗) 1/|N(𝑖) | = ∑︁

𝑖∈[𝑚]

- (6) |N(𝑖)| · 𝑝𝑖1/|N(𝑖) |.


𝑖0>𝑖,𝑖0∈N𝐺𝐷 (𝑖)

𝑖0<𝑖,𝑖0∈N𝐺𝐷 (𝑖)

𝑖0>𝑖,𝑖0∈N𝐺𝐷 (𝑖)

𝑖0<𝑖,𝑖0∈N𝐺𝐷 (𝑖)

On the other hand,

∑︁

∑︁

𝜇(𝑆𝑖𝑗) = ∑︁

∑︁

𝜇(𝑆𝑖𝑗) ≤ 𝑛 + ∑︁

∑︁

- (7)

By Inequalities 6 and 7 and noticing 𝐺𝐵 is linear, we have that

∑︁

(𝑖0,𝑖1)∈𝐸𝐷

∑︁

𝑗 ∈N(𝑖0)∩N(𝑖1)

𝜇 𝑆𝑖𝑗

0

∩ 𝑆𝑖𝑗

1

= ∑︁

𝑗 ∈[𝑛]

∑︁

𝑖0≠𝑖1∈N(𝑗)

𝜇 𝑆𝑖𝑗

0

∩ 𝑆𝑖𝑗

1

≥ ∑︁

𝑖∈[𝑚]

- (8) |N(𝑖)| · 𝑝𝑖1/|N(𝑖) | − 𝑛.

Moreover, given any (𝑖0,𝑖1) ∈ 𝐸𝐷, where {𝑗} = N(𝑖) ∩ N(𝑖 ), we have that

- (9)

P(𝐴𝑖0 ∩ 𝐴𝑖1) ≥ 𝜇 𝑆𝑖𝑗

0

∩ 𝑆𝑖𝑗

1

·

𝑘∈N(𝑖0)\{𝑗 }

𝜇(𝑆𝑖𝑘

0

) ·

𝑘 ∈N(𝑖1)\{𝑗 }

𝜇(𝑆 𝑖𝑘

1

)

≥ 𝜇 𝑆𝑖𝑗

0

∩ 𝑆𝑖𝑗

1

· 𝑝𝑖0 · 𝑝𝑖1. Finally, combining (8) with (9), we concludes that

∑︁

(𝑖0,𝑖1)∈𝐸𝐷

P(𝐴𝑖0 ∩ 𝐴𝑖1) ≥ ∑︁

(𝑖0,𝑖1)∈𝐸𝐷

∑︁

𝑗 ∈N(𝑖0)∩N(𝑖1)

𝜇 𝑆𝑖𝑗

0

∩ 𝑆𝑖𝑗

1

· 𝑝𝑖0 · 𝑝𝑖1

≥ min

𝑖∈[𝑚]

𝑝𝑖

2 ∑︁

𝑖

|N(𝑖)| · 𝑝𝑖1/|N(𝑖) | − 𝑛

= √𝑚 · Δ𝐷(𝐺𝐵) · Δ𝐵(𝐺𝐵)2 · (𝐺𝐵,𝒑).

e following lemma is a special case of eorem 4.1 where 𝑡 = 1 and 𝐿1 = [𝑚]. In fact, eorem 4.1 is proved by applying Lemma 4.6 to each 𝐺𝑘 separately.

- Lemma 4.6. Let 𝐺𝐵 = ([𝑚], [𝑛],𝐸𝐵) be a linear bipartite graph and 𝒑 be a probability vector. If A ∼ (𝐺𝐵,𝒑), then A ∼ (𝐺𝐵,𝒑, M, 𝜹) for some matching M of 𝐺𝐷(𝐺𝐵) and some 𝜹 ∈ (0, 1)|M| satisfying that (𝑖,𝑖 )∈M 𝛿𝑖,𝑖2 ≥ +(𝐺𝐵,𝒑) 2.


Proof. Given an instance A ∼ (𝐺𝐵,𝒑), we construct such a M greedily as follows.

We maintain two sets 𝐸 and M, which are initialized as 𝐸𝐷 and ∅ respectively. We do the following iteratively until 𝐸 becomes empty: select a edge (𝑖0,𝑖1) with maximum P(𝐴𝑖0 ∩ 𝐴𝑖1) from 𝐸, add (𝑖0,𝑖1) to M, and delete all edges connecting 𝑖0 or 𝑖1 from 𝐸 (including (𝑖0,𝑖1)).

Let Δ𝐷 and Δ𝐵 denote Δ𝐷(𝐺𝐵) and Δ𝐵(𝐺𝐵) respectively. In each iteration, at most 2Δ𝐷 edges are

deleted from 𝐸 and for each deleted edge (𝑖,𝑖 ), P(𝐴𝑖 ∩𝐴𝑖 )2 ≤ P(𝐴𝑖0 ∩𝐴𝑖1)2. Based on this observation, it is easy to see that

∑︁

(𝑖0,𝑖1)∈M

P(𝐴𝑖0 ∩ 𝐴𝑖1)2 ≥

- 1

- 2Δ𝐷


∑︁

(𝑖,𝑖 )∈𝐸𝐷

- (10) P(𝐴𝑖 ∩ 𝐴𝑖 )2.

Moreover, according to Lemma 4.2 and 4.5, it has that

∑︁

(𝑖,𝑖 )∈𝐸𝐷

P(𝐴𝑖 ∩ 𝐴𝑖 )2 ≥

1 |𝐸𝐷|

· ∑︁

(𝑖,𝑖 )∈𝐸𝐷

P(𝐴𝑖 ∩ 𝐴𝑖 )

2

≥

𝑚 · Δ𝐷2 · ( +(𝐺𝐵,𝒑))2 |𝐸𝐷|

- (11) ,


𝜇 𝑆𝑖𝑗

∩ 𝑆𝑖𝑗

0

1

𝑖0≠𝑖1∈N(𝑗)

𝑖∈[𝑚]

𝑗 ∈N(𝑖)

𝑗 ∈[𝑛]

𝑖∈N(𝑖)

𝑗 ∈[𝑛]

By combining Inequality 10 and 11, seing 𝛿𝑖,𝑖 = P(𝐴𝑖 ∩ 𝐴𝑖 ), and noting 2|𝐸𝐷| ≤ 𝑚Δ𝐷, we nish the proof.

Proof of eorem 4.1. For each 𝑘 ∈ [𝑡], by applying Lemma 4.6 to 𝐺𝑘, we have that A ∼ (𝐺𝐵,𝒑, M𝑘, 𝜹𝑘) for some matching M𝑘 ⊆ 𝐸𝑘 and some 𝜹𝑘 where (𝑖,𝑖 )∈M𝑘 𝛿𝑖,𝑖2 ≥ +(𝐺𝑘,𝒑) 2. Note that 𝐸𝑘’s are disjoint with each other, so M1∪M2∪· · ·∪M𝑡 is still a matching. By leing M = M1∪M2∪· · ·∪M𝑡 and 𝜹 = (𝜹1, · · · , 𝜹𝑡), we conclude the theorem.

Remark 4.7. Given a bipartite graph 𝐺, its simplied graph is dened to be obtained from 𝐺 by deleting all the right nodes which only have one neighbor and combining all the right nodes with the same neighbor set. Notice that if 𝐺 is linear, so is its simplied graph.

eorem 4.1 can be slightly generalized: it is sucient that the simplied graph of 𝐺𝑘 instead of 𝐺𝑘 itself is linear.

5. T   M     T      S      ’ 

In this section, we prove eorem 1.5. Given a dependency graph 𝐺𝐷, a vector 𝒑 and a chordless cycle 𝐶 in 𝐺𝐷, dene

2 𝑗∈𝐶 √𝑝𝑗 |𝐶|

2

𝑝𝑗 4 ·

− 1

𝑟(𝐺𝐷,𝒑,𝐶) |𝐶| · min

. and

𝑗 ∈𝐶

2 𝑗∈𝐶 √𝑝𝑗 |𝐶|

2

𝑝𝑗 4 · max

𝑟+(𝐺𝐷,𝒑,𝐶) |𝐶| · min

− 1, 0

. en eorem 1.5 is obvious by Lemmas 5.1 and 5.2.

𝑗 ∈𝐶

- Lemma 5.1. Given 𝐺𝐷, 𝒑 and 𝜀 > 0, let 𝐶1,𝐶2, · · · ,𝐶ℓ be any disjoint chordless cycles in 𝐺𝐷. If

𝑑((1 + 𝜀)𝒑,𝐺𝐷) <

1 544

∑︁

𝑖≤ℓ

𝑟+(𝐺𝐷,𝒑,𝐶𝑖),

then for any variable-generated event system A ∼ (𝐺𝐷,𝒑), the expected number of resampling steps performed by MT algorithm is most 𝑚/𝜀.

Proof. Fix such an instance A. Dene 𝛿𝑖,𝑖 := P(𝐴𝑖 ∩ 𝐴𝑖 ). Let 𝐺𝐵 denote the event-variable graph of A. Let 𝐺𝑘 denote the induced subgraph of 𝐺𝐵 on 𝐶𝑘 ∪ ∪𝑖∈𝐶𝑘N𝐺𝐵(𝑖) . According to Remark 4.7, it is lossless to assume 𝐺𝑘 is a cycle of length 2|𝐶𝑘|. us we have

(12) +(𝐺𝑘,𝒑) ≥

min𝑖∈𝐶𝑘 𝑝𝑖 2 · −|𝐶𝑘| + 𝑖∈𝐿 2√𝑝𝑖 8√︁|𝐶𝑘|

.

According to eorem 4.1, there is a matching M of 𝐺𝐷 such that (𝑖,𝑖 )∈M 𝛿𝑖,𝑖2 ≥ 𝑘≤ℓ ( +(𝐺𝑘,𝒑))2. Dene 𝒑− as (1). We have (1 + 𝜀)𝒑− ≤ (1 + 𝜀)𝒑 and

||(1 + 𝜀)𝒑 − (1 + 𝜀)𝒑−||1 ≥ ||𝒑 − 𝒑−||1 ≥

2 17

∑︁

(𝑖,𝑖 )∈M

𝛿𝑖,𝑖2 ≥

2 17

∑︁

𝑘≤ℓ

+(𝐺𝑘,𝒑) 2 .

Combining with (12), we have

||(1 + 𝜀)𝒑 − (1 + 𝜀)𝒑−||1 ≥

1 544

∑︁

𝑖≤ℓ

𝑟+(𝐺𝐷,𝒑,𝐶𝑖) > 𝑑((1 + 𝜀)𝒑,𝐺𝐷),

where the last inequality is by the condition of the lemma. us by Denition 1.4, we have (1+𝜀)𝒑− is in the Shearer’s bound of 𝐺𝐷. Combining with eorem 1.6, we have the expected number of resampling steps performed by the Moser-Tardos algorithm is most 𝑚/𝜀.

- Lemma 5.2. Given 𝐺𝐷 and any chordless cycle 𝐶 in 𝐺𝐷, there is some probability vector 𝒑 beyond the Shearer’s bound of 𝐺𝐷 and with

𝑑(𝒑,𝐺𝐷) ≥

1 545 · 𝑟(𝐺𝐷,𝒑,𝐶) > 2−20ℓ−3

such that for any variable-generated event system A ∼ (𝐺𝐷,𝒑), the expected number of resampling steps performed by MT algorithm is most 229 ·𝑚2 · |𝐶|3.

e following two lemmas will be used in the proof of Lemma 5.2.

- Lemma 5.3. [She85] 𝑞∅(𝐺𝐷,𝒑) = 1 − P( 𝐴∈A 𝐴) holds for any extremal instance A ∼ (𝐺𝐷,𝒑).


- Lemma 5.4. [She85] Suppose 𝒑 is the Shearer’s bound of 𝐺𝐷 = ([𝑚],𝐸𝐷). en for 𝑖 ∈ [𝑚],


𝜕𝑞∅(𝐺𝐷,𝒑) 𝜕𝑝𝑖

### = −P

𝐴𝑗

𝑗∉N𝐺𝐷 (𝑖)∪{𝑖}

holds for any A ∼ (𝐺𝐷,𝒑) satisfying that 𝐴𝑖 ∩ 𝐴𝑖 = ∅ for any (𝑖 ,𝑖 ) ∈ 𝐸𝐷 where 𝑖 ,𝑖 ≠ 𝑖. Proof of Lemma 5.2. Let ℓ = |𝐶| and 𝝀 = 14, · · · , 41, 14 . Let A ∼ (𝐶,𝝀) be an extremal instance dened

as follows: A = (𝐴1, · · · ,𝐴ℓ) is a variable-generated event system fully determined a set of underlying mutually independent random variables {𝑋1, · · · ,𝑋ℓ}. Moreover, 𝐴𝑖 = [𝑋𝑖 < 1/2] ∧ [𝑋𝑖+1 ≥ 1/2] for each 𝑖 ∈ [ℓ − 1], and 𝐴ℓ = [𝑋ℓ < 1/2] ∧ [𝑋1 ≥ 1/2]. According to Lemma 5.3,

- 1

- 2ℓ−1 .


### 𝑞∅(𝐶,𝝀) = P

𝐴𝑖 =

𝑖∈[ℓ]

Besides, according to Lemma 5.4, for any 𝝀 = (41, · · · , 14, 14 + 𝜀) in the Shearer’s bound of 𝐶,

𝜕𝑞∅(𝐶,𝝀 ) 𝜕𝜆 ℓ

ℓ − 2 2ℓ−3 .

### = −P

𝐴𝑖 = −

𝑖∈[2,ℓ−2]

us, for any 𝝀 ≤ 𝝀 ≤ 𝝀 := 4 1, · · · , 14, 14 + 4(ℓ1−1) , we have that

### ∫ 𝜆

𝜕𝑞∅(𝐶,𝝀 ) 𝜕𝜆 ℓ

ℓ − 2 ℓ − 1 ·

1

1 2ℓ−1 −

- 1

- 2ℓ−1 =


- 1

- 2ℓ−1 .


ℓ

𝑞∅(𝐶,𝝀 ) = 𝑞∅(𝐶,𝝀) +

ℓ − 1 ·

𝑑𝜆 ℓ >

1 4

Hence 𝝀 is in the Shearer’s bound of 𝐶. us, there exists 𝑞 > 0 such that 𝒒 dened as follows is on the Shearer’s boundary of 𝐺𝐷:

 

1 4 if 𝑖 ∈ [ℓ − 1], 1 4 + 4(ℓ1−1) if 𝑖 = ℓ,

∀𝑖 ∈ [𝑚] : 𝑞𝑖 =

 

𝑞 otherwise. One can verify that

- (13) 𝑟+(𝐺𝐷, 𝒒,𝐶) = 𝑟(𝐺𝐷, 𝒒,𝐶) > ℓ ·

1 44 ·

- 1

- 2ℓ2


2

>

1 210 · ℓ3

.

Dene

𝑓 (𝛿) = 545 · 𝑑((1 + 𝛿)𝒒,𝐺𝐷) − 𝑟+(𝐺𝐷, (1 + 𝛿)𝒒,𝐶).

One can verify that 𝑓 (0) < 0 because 𝑑(𝒒,𝐺𝐷) = 0 and 𝑟+(𝐺𝐷, 𝒒,𝐶) > 0. Moreover, let 𝛿 be large enough such that (1 + 𝛿 )𝒒 ∉ I𝑣(𝐺𝐷). One can verify that such 𝛿 must exist. We have 𝑓 (𝛿 ) ≥ 0. is is because otherwise 𝑓 (𝛿 ) < 0 and then

𝑑((1 + 𝛿 )𝒒,𝐺𝐷) <

1

545 · 𝑟+(𝐺𝐷, (1 + 𝛿 )𝒒,𝐶). By following the proof of Lemma 5.1, we have the MT algorithm terminates at (1 + 𝛿 )𝒒, which is contradictory with (1 + 𝛿 )𝒒 ∉ I𝑣(𝐺𝐷).

Moreover, 𝑓 (𝛿) is a continuous function of 𝛿, because 𝑑((1 + 𝛿)𝒒,𝐺𝐷) and 𝑟+(𝐺𝐷, (1 + 𝛿)𝒒,𝐶) are both continuous functions of 𝛿. Combining with 𝑓 (0) < 0 and 𝑓 (𝛿 ) > 0, we have there must be a

- 0 ≤ 𝛿 ≤ 𝛿 such that 𝑓 (𝛿) = 0. Let 𝒑 = (1 + 𝛿)𝒒. By 𝑓 (𝛿) = 0, we have


- (14) 𝑑(𝒑,𝐺𝐷) =


1 545 · 𝑟+(𝐺𝐷,𝒑,𝐶).

Combining with 𝑟+(𝐺𝐷,𝒑,𝐶) = 𝑟(𝐺𝐷,𝒑,𝐶) > 𝑟(𝐺𝐷, 𝒒,𝐶) and (13), we have 𝑑(𝒑,𝐺𝐷) > 2−20ℓ−3.

Fix a variable-generated event system A ∼ (𝐺𝐷,𝒑). Dene 𝛿𝑖,𝑖 := P(𝐴𝑖 ∩ 𝐴𝑖 ). Let 𝐺𝐵 denote the

event-variable graph of A. Let 𝐺 denote the induced subgraph of 𝐺𝐵 on 𝐶 ∪ ∪𝑖∈𝐶N𝐺𝐵(𝑖) . According to Remark 4.7, it is lossless to assume that 𝐺 is a cycle of length 2|𝐶|. us we have

min𝑖∈𝐶 𝑝𝑖 2 · −|𝐶| + 𝑖∈𝐿 2√𝑝𝑖 8√︁|𝐶|

- (15) +(𝐺,𝒑) ≥


.

According to eorem 4.1, there is a matching M of 𝐺𝐷 such that (𝑖,𝑖 )∈M 𝛿𝑖,𝑖2 ≥ ( +(𝐺,𝒑))2. Dene 𝒑− as (1). We have

∑︁

∑︁

2 17

2 17

+(𝐺𝑘,𝒑) 2 . Combining with (15), we have

||𝒑 − 𝒑−||1 ≥

𝛿𝑖,𝑖2 ≥

𝑘≤ℓ

(𝑖,𝑖 )∈M

1

544 · 𝑟+(𝐺𝐷,𝒑,𝐶). Let

||𝒑 − 𝒑−||1 ≥

1 229 · ℓ3 ·𝑚

𝜀

. By (13) we have

1 545 · 544 · 210 · ℓ3 ≤

1 544 −

1 545

1 544 −

1 545

𝑟+(𝐺𝐷,𝒑,𝐶). us we have

𝑟+(𝐺𝐷, 𝒒,𝐶) ≤

𝑚𝜀 ≤

𝑟+(𝐺𝐷,𝒑,𝐶)

𝑟+(𝐺𝐷,𝒑,𝐶)

||𝒑 − (1 + 𝜀)𝒑−||1 > ||𝒑 − 𝒑−||1 −𝑚𝜀 ≥

544 −𝑚𝜀 ≥

545 ≥ 𝑑(𝒑,𝐺𝐷),

where the last inequality is by (14). us by Denition 1.4, we have (1 + 𝜀)𝒑− is in the Shearer’s bound of 𝐺𝐷. Combining with eorem 1.6, we have the expected number of resampling steps performed by the MT algorithm is most 𝑚/𝜀.

6. A           E        

In this section, we explicitly calculate the gaps between our new criterion and Shearer’s bound on periodic Euclidean graphs, including several laices that have been studied extensively in physics. It turns out the ecient region of MT algorithm can exceed signicantly beyond Shearer’s bound.

A periodic Euclidean graph 𝐺𝐷 is a graph that is embedded into a Euclidean space naturally and has a translational unit 𝐺𝑈 in the sense that 𝐺𝐷 can be viewed as the union of periodic translations of 𝐺𝑈. For example, a cycle of length 4 is a translational unit of the square laice.

Given a dependency graph 𝐺𝐷, it naturally denes a bipartite graph 𝐺𝐵(𝐺𝐷) as follows. Regard each edge of 𝐺𝐷 as a variable and each vertex as an event. An event 𝐴 depends on a variable 𝑋 if and only if the vertex corresponding to 𝐴 is an endpoint of the edge corresponding to 𝑋.

For simplicity, we only focus on symmetric probabilities, where𝒑 = (𝑝,𝑝, · · · ,𝑝). Given a dependency graph 𝐺𝐵 and a vector 𝒑, remember that 𝒑 is on Shearer’s boundary of 𝐺𝐷 if (1 − 𝜀)𝒑 is in Shearer’s bound and (1 + 𝜀)𝒑 is not for any 𝜀 > 0.

Given a dependency graph 𝐺𝐷 = ([𝑚],𝐸𝐷) and two vertices 𝑖,𝑖 ∈ [𝑚], we use dist(𝑖,𝑖 ) to denote the distance between 𝑖 and 𝑖 in 𝐺𝐷. e following Lemma will be used.

Lemma 6.1. Suppose 𝒑𝑎 = (𝑝𝑎,𝑝𝑎, · · · ,𝑝𝑎) is on Shearer’s boundary of 𝐺𝐷 = ([𝑚],𝐸𝐷). For any probability vector 𝒑 other than 𝒑𝑎, it is in the Shearer’s bound if there exist 𝐾,𝑑 ∈ N+, S ⊆ 2[𝑚] where ∪𝑆∈S = [𝑚], and 𝑓 : S → 2[𝑚] such that the following conditions hold:

- (a) for each 𝑖 ∈ [𝑚], there are at most 𝐾 subsets 𝑆 ∈ S such that 𝑓 (𝑆) 𝑖;
- (b) if 𝑓 (𝑆) = 𝑇, then dist(𝑖,𝑖 ) ≤ 𝑑 for each 𝑖 ∈ 𝑆 and 𝑖 ∈ 𝑇;
- (c) if 𝑓 (𝑆) = 𝑇, then


𝐾 𝑝𝑎 · ∑︁

max{𝑝𝑖 − 𝑝𝑎, 0} ≤ ∑︁ 𝑖∈𝑇

𝑑−1

1 − 𝑝𝑎 𝑝𝑎

·

max{𝑝𝑎 − 𝑝𝑖, 0}.

𝑖∈𝑆

While Lemma 6.1 looks involved, the basic idea is simple: by contradiction, suppose there is such a vector 𝒑 beyond Shearer’s bound; then we apply Lemma D.1 repeatedly to transfer probability from one event to another while keeping the probability vector still beyond Shearer’s bound; nally, the vector 𝒑 will be changed to a vector strictly below 𝒑, which makes a contradiction to the assumption that 𝒑 is on the Shearer’s boundary. e involved part is a transferring scheme which changes 𝒑 to another probability vector strictly below 𝒑. We leave the proof to the appendix.

e main result of this section is as follows.

eorem 6.2. Let 𝐺𝐷 = (𝑉𝐷,𝐸𝐷) be a periodic Euclidean graph with maximum degree Δ, and 𝒑𝑎 = (𝑝𝑎, · · · ,𝑝𝑎) be the probability vector on Shearer’s boundary of 𝐺𝐷. Suppose 𝐺𝑈 = (𝑉𝑈,𝐸𝑈) is a translational unit of 𝐺𝐷 with diameter 𝐷. Let

### 𝑝𝑎𝐷+2 +(𝐺𝐵(𝐺𝑈),𝒑𝑎) 2 17 · (Δ + 1) · |𝑉 |2 · (1 − 𝑝𝑎)𝐷+1

.

𝑞

en for any A ∼ (𝐺𝐵(𝐺𝐷),𝒑) where (1 +𝜀)𝒑 ≤ (𝑝𝑎 +𝑞, · · · ,𝑝𝑎 +𝑞), the expected number of resampling steps performed by the MT algorithm is most |𝑉𝐷|/𝜀.

Proof. Fix any A ∼ (𝐺𝐵(𝐺𝐷),𝒑) where (1 + 𝜀)𝒑 ≤ (𝑝𝑎 + 𝑞, · · · ,𝑝𝑎 + 𝑞). Let 𝛿𝑣0,𝑣1 denote P(𝐴𝑣0 ∩ 𝐴𝑣1) for (𝑣0,𝑣1) ∈ 𝐸𝐷. We construct a matching M ⊂ 𝐸𝐷 greedily as follows: we maintain two sets 𝐸 and M, which are initialized as 𝐸𝐷 and ∅ respectively. We do the following iteratively until 𝐸 becomes empty: select a edge (𝑣0,𝑣1) with maximum 𝛿𝑣0,𝑣1 from 𝐸, add (𝑣0,𝑣1) to M, and delete all edges connecting 𝑣0 or 𝑣1 from 𝐸 (including (𝑣0,𝑣1)). Let 𝜹 = 𝛿𝑣0,𝑣1 : (𝑣0,𝑣1) ∈ M . en A ∼ (𝐺𝐵(𝐺𝐷),𝒑, M, 𝜹).

Dene 𝒑− as (1). In the remaining part of the proof, we will show that (1 + 𝜀)𝒑− is in the Shearer’s bound. is implies the conclusion immediately by eorem 1.6.

In fact, it is a direct application of Lemma 6.1 to show that (1 + 𝜀)𝒑− is in the Shearer’s bound. To provide more detail, we need some notations. We use 𝑣,𝑣 ,𝑣1,𝑣2, · · · to represent vertices in 𝐺𝐷, and use 𝑢,𝑢 ,𝑢1,𝑢2, · · · to represent vertices in 𝐺𝑈. Let 𝐺𝑈1,𝐺𝑈2, · · · be the periodic translations of 𝐺𝑈 in 𝐺𝐷. And we use a surjection9 ℎ : N+ × 𝑉𝑈 → 𝑉𝐷 to represent how these periodic translations constitute 𝐺𝐷: ℎ(𝑘,𝑢) = 𝑣 if the copy of 𝑢 ∈ 𝑉𝑈 in 𝑘-th translation (i.e., 𝐺𝑈𝑘 ) is 𝑣 ∈ 𝑉𝐷. In particular, the vertex set of 𝐺𝑈𝑘 , denoted by 𝑉𝑈𝑘, is {ℎ(𝑘,𝑢) : 𝑢 ∈ 𝑉 }, and the edge set of 𝐺𝑈𝑘 , denoted by 𝐸𝑈𝑘 , is {(ℎ(𝑘,𝑢),ℎ(𝑘,𝑢 )) : (𝑢,𝑢 ) ∈ 𝐸𝑈 }. Besides, let N+(𝑣) := N𝐺𝐷 (𝑣) ∪ {𝑣} for 𝑣 ∈ 𝑉𝐷. For 𝑉 ⊂ 𝑉𝐷, let N+(𝑉) := ∪𝑣∈𝑉N+(𝑣). Let𝑇𝑘 := {(𝑣0,𝑣1) ∈ M : 𝑣0,𝑣1 ∈ N+(𝐺𝑈𝑘 )} stand for the pairs in M adjacent to 𝐺𝑈𝑘 . With some abuse of notation, we sometimes use 𝑣 ∈ 𝑇𝑘 to denote that (𝑣,𝑣 ) ∈ 𝑇𝑘 for some 𝑣 ∈ 𝑉𝐷.

e following claim says that 𝒑− is much smaller than 𝒑 even projected on a single translation. Its proof uses a similar idea to eorem 4.6 and can be found in the appendix.

Claim 6.3. (𝑣0,𝑣1)∈𝑇𝑘 𝛿𝑣20,𝑣1 ≥ +(𝐺𝐵(𝐺𝑈),𝒑) 2 holds for any 𝑘.

To apply Lemma 6.1, let 𝐾 := (Δ + 1)|𝑉𝑈 |, 𝑑 := 𝐷 + 2, S := {𝑉𝑈1,𝑉𝑈2, · · · }, and 𝑓 (𝑉𝑈𝑘) := 𝑇𝑘. Based on Claim 6.3, one can check that all the three conditions in Lemma 6.1 hold (see the appendix for details). us, according to Lemma 6.1, (1 + 𝜀)𝒑− is in Shearer’s bound.

We apply eorem 6.2 to three laices: square laice, Hexagonal laice, and simple cubic laice. For square laice, we take the 5 × 5 square with 25 vertices as the translational unit. For Hexagonal laice, we take a graph consisting of 19 hexagons as the translational unit, in which there are 3,4,5,4,3 hexagons in the ve columns, respectively. For simple cubic laice, we take the 3 × 3 × 3 cube with 27 vertices as the translational unit. e explicit gaps are summarized in Table 1. Finally, the lower bounds for these three laices in Table 1 hold for all bipartite graphs with the given canonical dependency graph, because all such bipartite graphs are essentially the same under the reduction rules dened in [HLL+17].

9ℎ is possibly not a injection, as these translations are possibly overlapped with each other.

R          [AFR95] Michael Albert, Alan Frieze, and Bruce Reed. Multicoloured hamilton cycles. the electronic journal of combinatorics, 2(1):R10, 1995. [AI16] Dimitris Achlioptas and Fotis Iliopoulos. Random walks that nd perfect objects and the lov´asz local lemma. Journal of ACM, 63(3):22:1–22:29, 2016. [AIK19] Dimitris Achlioptas, Fotis Iliopoulos, and Vladimir Kolmogorov. A local lemma for focused stochastic algorithms. SIAM Journal on Computing, 48(5):1583–1602, 2019.

[AIS19] Dimitris Achlioptas, Fotis Iliopoulos, and Alistair Sinclair. Beyond the lov´asz local lemma: Point to set correlations and their algorithmic applications. In Proceedings of Symposium on Foundations of Computer Science (FOCS), pages 725–744, 2019.

[AIV17] Dimitris Achlioptas, Fotis Iliopoulos, and Nikos Vlassis. Stochastic control via entropy compression. In Proceedings of International Colloquium on Automata, Languages, and Programming (ICALP), volume 80, pages 83:1–83:13, 2017.

[Alo91] Noga Alon. A parallel algorithmic version of the local lemma. Random Structures and Algorithms, 2(4):367–378, 1991. [Bec91] J´ozsef Beck. An algorithmic approach to the Lov´asz local lemma. Random Structures and Algorithms, 2(4):343–365, 1991.

[BFH+16] Sebastian Brandt, Orr Fischer, Juho Hirvonen, Barbara Keller, Tuomo Lempi¨ainen, Joel Rybicki, Jukka Suomela, and Jara Uio. A lower bound for the distributed lov´asz local lemma. In Proceedings of Symposium on eory of Computing (STOC) , pages 479–488, 2016.

[BFPS11] Rodrigo Bissacot, Roberto Fern´andez, Aldo Procacci, and Benedeo Scoppola. An improvement of the Lov´asz local lemma via cluster expansion. Combinatorics, Probability and Computing, 20(05):709–719, 2011.

[CCS+17] Jan Dean Catarata, Sco Corbe, Harry Stern, Mario Szegedy, Tomas Vyskocil, and Zheng

Zhang. e Moser-Tardos resample algorithm: Where is the limit?(an experimental inquiry). In 2017 Proceedings of the Ninteenth Workshop on Algorithm Engineering and Experiments (ALENEX), pages 159–171, 2017.

[CGH13] Karthekeyan Chandrasekaran, Navin Goyal, and Bernhard Haeupler. Deterministic algorithms for the lov´asz local lemma. SIAM Journal on Computing, 42(6):2132–2155, 2013. [CPS17] Kai-Min Chung, Seth Peie, and Hsin-Hao Su. Distributed algorithms for the lov´asz local lemma and graph coloring. Distributed Computing, 30(4):261–280, 2017.

[CS00] Artur Czumaj and Christian Scheideler. Coloring nonuniform hypergraphs: A new algorithmic approach to the general Lov´asz local lemma. Random Structures and Algorithms, 17(3-4):213–237, 2000.

[EL75] Paul Erd˝os and L´aszl´o Lov´asz. Problems and results on 3-chromatic hypergraphs and some related questions. Innite and nite sets , 10(2):609–627, 1975. [ES91] Paul Erd¨os and Joel Spencer. Lopsided lov´asz local lemma and latin transversals. Discrete Applied Mathematics, 30(2-3):151–154, 1991.

[FGYZ20] Weiming Feng, Heng Guo, Yitong Yin, and Chihao Zhang. Fast sampling and counting𝑘-sat solutions in the local lemma regime. In Proceedings of Symposium on eory of Computing (STOC), pages 854–867, 2020.

- [FHY20] Weiming Feng, Kun He, and Yitong Yin. Sampling constraint satisfaction solutions in the local lemma regime. arXiv preprint arXiv:2011.03915, 2020.
- [FHY21] Weiming Feng, Kun He, and Yitong Yin. Sampling constraint satisfaction solutions in the local lemma regime. In Proceedings of the 53rd Annual ACM SIGACT Symposium on eory of Computing, pages 1565–1578, 2021.


[Gau67] David S Gaunt. Hard-sphere laice gases. ii. plane-triangular and three-dimensional laices. e Journal of Chemical Physics , 46(8):3237–3259, 1967. [GF65] David S Gaunt and Michael E Fisher. Hard-sphere laice gases. i. plane-square laice. e Journal of Chemical Physics, 43(8):2840–2863, 1965. [GGGY20] Andreas Galanis, Leslie Ann Goldberg, Heng Guo, and Kuan Yang. Counting solutions to random CNF formulas. In ICALP, volume 168 of LIPIcs, pages 53:1–53:14, 2020.

[GH20] Heng Guo and Kun He. Tight bounds for popping algorithms. Random Structures & Algorithms, 2020.

[Gha16] Mohsen Ghaari. An improved distributed algorithm for maximal independent set. In Robert Krauthgamer, editor, Proceedings of ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 270–277, 2016.

[Gil19] Andr´as Gily´en. antum singular value transformation & its algorithmic applications . PhD thesis, University of Amsterdam, 2019.

- [GJ18] Heng Guo and Mark Jerrum. Approximately counting bases of bicircular matroids. arXiv preprint arXiv:1808.09548, 2018.
- [GJ19] Heng Guo and Mark Jerrum. A polynomial-time approximation algorithm for all-terminal network reliability. SIAM Journal on Computing, 48(3):964–978, 2019.


[GJL19] Heng Guo, Mark Jerrum, and Jingcheng Liu. Uniform sampling through the lov´asz local lemma. Journal of the ACM (JACM), 66(3):18, 2019.

[GKPT17] Ioannis Giotis, Leeris Kirousis, Kostas I Psaromiligkos, and Dimitrios M ilikos. Acyclic edge coloring through the Lov´asz local lemma. eoretical Computer Science , 665:40–50, 2017.

[GLLZ19] Heng Guo, Chao Liao, Pinyan Lu, and Chihao Zhang. Counting hypergraph colorings in

the local lemma regime. SIAM Journal on Computing, 48(4):1397–1424, 2019. [GMSW09] Heidi Gebauer, Robin A Moser, Dominik Scheder, and Emo Welzl. e lov´asz local lemma

and satisability. In Ecient Algorithms , pages 30–54. Springer, 2009. [GST16] Heidi Gebauer, Tibor Szab´o, and G´abor Tardos. e local lemma is asymptotically tight for SAT. Journal of ACM, 63(5):43, 2016. [Har16] David G Harris. Lopsidependency in the moser-tardos framework: beyond the lopsided Lov´asz local lemma. ACM Transactions on Algorithms (TALG), 13(1):17, 2016.

- [Har18] David G. Harris. Deterministic parallel algorithms for fooling polylogarithmic juntas and the lov´asz local lemma. ACM Transaction on Algorithms, 14(4):47:1–47:24, 2018.
- [Har19] David G. Harris. Deterministic algorithms for the lovasz local lemma: simpler, more general, and more parallel. CoRR, abs/1909.08065, 2019.


[HH17] Bernhard Haeupler and David G. Harris. Parallel algorithms and concentration bounds for the lov´asz local lemma via witness dags. ACM Transaction on Algorithms, 13(4):53:1–53:25, 2017.

[HLL+17] Kun He, Liang Li, Xingwu Liu, Yuyi Wang, and Mingji Xia. Variable-version Lov´asz local lemma: Beyond shearer’s bound. In Proceedings of Symposium on Foundations of Computer Science (FOCS), pages 451–462, 2017.

[HLSZ19] Kun He, Qian Li, Xiaoming Sun, and Jiapeng Zhang. antum lov´asz local lemma: Shearer’s bound is tight. In Proceedings of Symposium on eory of Computing (STOC) , pages 461–472, 2019.

[HS14] David G. Harris and Aravind Srinivasan. A constructive algorithm for the lov´asz local lemma on permutations. In Proceedings of ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 907–925, 2014.

[HSS11] Bernhard Haeupler, Barna Saha, and Aravind Srinivasan. New constructive aspects of the lov´asz local lemma. Journal of ACM, 58(6):1–28, 2011. [HSW21] Kun He, Xiaoming Sun, and Kewen Wu. Perfect sampling for (atomic) lov\’asz local lemma. arXiv preprint arXiv:2107.03932, 2021. [HV20] Nicholas J. A. Harvey and Jan Vondr´ak. An algorithmic proof of the lov´asz local lemma via resampling oracles. SIAM Journal on Computing, 49(2):394–428, 2020.

[IS20] Fotis Iliopoulos and Alistair Sinclair. Eciently list-edge coloring multigraphs asymptotically optimally. In Proceedings of ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 2319–2336, 2020.

- [JPV20] Vishesh Jain, Huy Tuan Pham, and uy Duong Vuong. Towards the sampling lov´asz local lemma. CoRR, abs/2011.12196, 2020.
- [JPV21] Vishesh Jain, Huy Tuan Pham, and uy Duong Vuong. On the sampling lov´asz local lemma for atomic constraint satisfaction problems. CoRR, abs/2102.08342, 2021.


[KS11] Kashyap Babu Rao Kolipaka and Mario Szegedy. Moser and tardos meet lov´asz. In

Proceedings of Symposium on eory of Computing (STOC) , pages 235–244, 2011. [KSX12] Kashyap Babu Rao Kolipaka, Mario Szegedy, and Yixin Xu. A sharper local lemma with improved applications. In Proceedings of APPROX/RANDOM, volume 7408 of Lecture Notes in Computer Science, pages 603–614, 2012.

[LS07] Linyuan Lu and L´aszl´o Sz´ekely. Using lov´asz local lemma in the space of random injections. the electronic journal of combinatorics, 14(1):R63, 2007. [LS09] Linyuan Lu and Laszlo A Szekely. A new asymptotic enumeration technique: the lov´asz local lemma. arXiv preprint arXiv:0905.3983, 2009. [McD97] Colin McDiarmid. Hypergraph colouring and the Lov´asz local lemma. Discrete Mathematics, 167:481–486, 1997.

- [Moi19a] Ankur Moitra. Approximate counting, the lovasz local lemma, and inference in graphical models. Journal of ACM, 66(2):10, 2019.
- [Moi19b] Ankur Moitra. Approximate counting, the Lov´asz local lemma, and inference in graphical models. J. ACM, 66(2):10:1–10:25, 2019.


[Mol19] Michael Molloy. e list chromatic number of graphs with small clique number. Journal of Combinatorial eory, Series B , 134:264–284, 2019.

[MR98] Michael Molloy and Bruce Reed. Further algorithmic aspects of the local lemma. In Proceedings of Symposium on eory of Computing (STOC) , pages 524–529, 1998.

[MT10] Robin A Moser and G´abor Tardos. A constructive proof of the general Lov´asz local lemma. Journal of ACM, 57(2):11, 2010. [Peg14] Wesley Pegden. An extension of the moser–tardos algorithmic local lemma. SIAM Journal

on Discrete Mathematics, 28(2):911–917, 2014. [She85] James B. Shearer. On a problem of spencer. Combinatorica, 5(3):241–245, 1985. [Spe75] Joel Spencer. Ramsey’s theorem—a new lower bound. Journal of Combinatorial eory,

Series A, 18(1):108–115, 1975. [Spe77] Joel Spencer. Asymptotic lower bounds for Ramsey functions. Discrete Mathematics, 20:69–76, 1977. [Sze13] Mario Szegedy. e lov´asz local lemma–a survey. In International Computer Science Symposium in Russia, pages 1–11. Springer, 2013. [Tod99] Synge Todo. Transfer-matrix study of negative-fugacity singularity of hard-core laice gas. International Journal of Modern Physics C, 10(04):517–529, 1999.

A        A. M       P      S       2 Proof of Proposition 3.2. e following simple greedy procedure will nd such a P.

- 1 Initially, P = ∅;
- 2 for each (𝑖,𝑖 ) ∈ M do

- 3 for each 𝑘 from 1 to |List(𝐷,𝑖,𝑖 )| − 1 do

- 4 if the 𝑘-th node and (𝑘 + 1)-th node in List(𝐷,𝑖,𝑖 ) form a reversible arc then

- 5 add this arc to P, and 𝑘 := 𝑘 + 2;

- 6 else

- 7 𝑘 := 𝑘 + 1;

- 8 Return P;


Obviously, for each (𝑖,𝑖 ) ∈ M, the procedure contains at least half of all reversible arcs𝑢 → 𝑣 where {𝐿(𝑢),𝐿(𝑣)} = {𝑖,𝑖 }, hence at least half of nodes in V(𝐷,𝑖).

A        B. P     P           3.9

Given a pwdag 𝐷 = (𝑉,𝐸,𝐿) of 𝐺𝐷 and a Boolean string 𝑹 ∈ {0, 1}ℳ(𝐷), dene ℎ(𝐷, 𝑹) to be a directed graph 𝐷 := (𝑉 ,𝐸 ,𝐿 ) where 𝑉 = 𝑉, 𝐸 = 𝐸, and

 

(𝐿(𝑣))↑, if 𝑣 ∈ ℳ and 𝑅𝑣 = 0; (𝐿(𝑣))↓, if 𝑣 ∈ ℳ and 𝑅𝑣 = 1; 𝐿(𝑣), otherwise, 𝑣 ∉ ℳ.

∀𝑣 ∈ 𝑉 : 𝐿 (𝑣) =

 

It is easy to verify that ℎ(𝐷, 𝑹) is a pwdag of 𝐺M. Moreover, given any 𝐷 ∈ D(𝐺M), there is one and only one 𝐷 ∈ D(𝐺𝐷) and 𝑹 ∈ {0, 1}ℳ(𝐷) such that ℎ(𝐷, 𝑹) = 𝐷 . In other words, ℎ is a bijection between {(𝐷, 𝑹) : 𝐷 ∈ D(𝐺𝐷), 𝑹 ∈ {0, 1}ℳ(𝐷)} and D(𝐺M). So

### ∑︁

𝑝𝐿M (𝑣 ) = ∑︁

∑︁

𝑝𝐿M (𝑣 )

𝐷 ∈D(𝐺M) 𝑣 in 𝐷

𝑹∈{0,1}ℳ(𝐷) 𝑣 in ℎ(𝐷,𝑹)

= ∑︁

∑︁

𝐷∈D(𝐺𝐷)

𝑝𝐿M (𝑣)

𝑹∈{0,1}ℳ(𝐷) 𝑣 in 𝐷

𝐷∈D(𝐺𝐷)

= ∑︁

### 𝑝𝐿M (𝑣) ∑︁

𝑝𝐿M (𝑣)

𝐷∈D(𝐺𝐷) 𝑣∉ℳ(𝐷)

𝑹∈{0,1}ℳ(𝐷) 𝑣∈ℳ(𝐷)

= ∑︁

𝑝𝐿M(𝑣)↑ + 𝑝𝐿M(𝑣)↓

### 𝑝𝐿M(𝑣)

= ∑︁

𝐷∈D(𝐺𝐷) 𝑣∉ℳ(𝐷)

𝑣∈ℳ(𝐷)

𝑝𝐿−(𝑣)

𝑝 𝐿(𝑣) + 𝑝𝐿−(𝑣) − 𝑝 𝐿(𝑣)

### = ∑︁

𝐷∈D(𝐺𝐷) 𝑣∉ℳ(𝐷)

𝑣∈ℳ(𝐷)

𝑝𝐿−(𝑣),

𝐷∈D(𝐺𝐷) 𝑣 in 𝐷

where the second equality is by that 𝑉 = 𝑉 , the forth equality is by the denition of 𝐿 , and the h equality is by the denition of 𝒑M.

A        C. P     T       3.12

We rst verify that the image of ℎ is a subset of D(𝐺M). Lemma C.1. For any 𝐷 ∈ D(𝐺𝐷) and 𝒮 ∈ 𝜓(𝐷), ℎ(𝐷,𝒮) ∈ D(𝐺M). Proof. First, we prove that ℎ(𝐷,𝒮) = (𝑉 ,𝐸 ,𝐿 ) is a DAG. Dene a total order 𝜋 over the set 𝑉 as follows: for any two distinct nodes 𝑢 ,𝑣 ∈ 𝑉 ,

- • if 𝑔(𝑢 ) ≠ 𝑔(𝑣 ), then 𝑢 ≺ 𝑣 in 𝜋 if and only if 𝑔(𝑢 ) ≺ 𝑔(𝑣 ) in 𝜋𝐷;
- • if 𝑔(𝑢 ) = 𝑔(𝑣 ), then 𝑢 ≺ 𝑣 in 𝜋 if and only if 𝑢 = 𝑓 ∗(𝑔(𝑢 )) (and then 𝑣 = 𝑓 (𝑔(𝑢 ))).


One can verify that 𝜋 is a topological order of ℎ(𝐷,𝒮), which means that ℎ(𝐷,𝒮) is a DAG.

Secondly, we prove that ℎ(𝐷,𝒮) is a wdag of 𝐺M. As ℎ(𝐷,𝒮) has been shown to be a DAG, we only need to verify that: for any two distinct nodes 𝑢 ,𝑣 in 𝐷 , there is a arc between 𝑢 and 𝑣 (in either direction) if and only if either 𝐿 (𝑢 ) = 𝐿 (𝑣 ) or (𝐿 (𝑣 ),𝐿 (𝑢 )) ∈ 𝐸M.

=⇒: By symmetry, suppose (𝑢 → 𝑣 ) ∈ 𝐸 . If (𝑢 → 𝑣 ) ∈ 𝐸 1, then 𝑢 = 𝑓 ∗(𝑤) and 𝑣 = 𝑓 (𝑤) for some vertex 𝑤 ∈ 𝒮3 ∪ 𝒮4. us, by ( 2) and (3) we have 𝐿 (𝑢 ) ∈ {𝑖↑,𝑖↓} and 𝐿 (𝑣 ) = 𝐿(𝑤)↓ where (𝐿(𝑤),𝑖) ∈ M. By (𝐿(𝑤),𝑖) ∈ M, any two vertices in {(𝐿(𝑤))↑, (𝐿(𝑤))↓,𝑖↑,𝑖↓} are connected in 𝐺M.

In particular, (𝐿 (𝑣 ),𝐿 (𝑢 )) ∈ 𝐸M. If (𝑢 → 𝑣 ) ∈ 𝐸 2, we have 𝐿 (𝑢 ) = 𝐿 (𝑣 ) or (𝐿 (𝑢 ),𝐿 (𝑣 )) ∈ 𝐸M immediately.

⇐=: Suppose 𝑢 ,𝑣 ∈ 𝑉 are two distinct nodes where 𝐿 (𝑢 ) = 𝐿 (𝑣 ) or (𝐿 (𝑢 ),𝐿 (𝑣 )) ∈ 𝐸M. If 𝑔(𝑢 ) ≠ 𝑔(𝑣 ), then either𝑔(𝑢 ) ≺ 𝑔(𝑣 ) or𝑔(𝑣 ) ≺ 𝑔(𝑢 ) in 𝜋𝐷, which implies that either (𝑢 → 𝑣 ) ∈ 𝐸 2 or (𝑣 → 𝑢 ) ∈ 𝐸 2. Otherwise, 𝑔(𝑢 ) = 𝑔(𝑣 ). Let 𝑣 := 𝑔(𝑢 ) = 𝑔(𝑣 ). By (2) and (3), we have 𝑣 ∈ 𝒮3 ∪ 𝒮4 and {𝑢 ,𝑣 } = {𝑓 (𝑣), 𝑓 ∗(𝑣)}. erefore either 𝑢 → 𝑣 or 𝑣 → 𝑢 is in 𝐸 1.

Finally, one can check that 𝑓 (𝑣) where 𝑣 is the unique sink of 𝐷 is the unique sink of 𝐷 . is completes the proof.

In the rest of this section, we show that ℎ is injective. Given 𝐷 ∈ D(𝐺𝐷) and (𝑖, 𝑗) ∈ M, recall that List(𝐷,𝑖, 𝑗) is the sequence listing all nodes in 𝐷 labelled with 𝑖 or 𝑗 in the topological order. Similarly, Denition C.2. Given 𝐷 = (𝑉 ,𝐸 ,𝐿 ) ∈ D(𝐺M) and (𝑖, 𝑗) ∈ M, we use List (𝐷 ,𝑖, 𝑗) to denote the unique sequence listing all nodes in 𝐷 with label in {𝑖↑,𝑖↓, 𝑗↑, 𝑗↓} in the topological order.

Claims C.3 and C.5 are two properties about List (𝐷 ,𝑖, 𝑗), which will be used to show the injectiveness of ℎ. Claim C.3. Suppose 𝐷 = ℎ(𝐷,𝒮) for some 𝐷 ∈ D(𝐺𝐷) and 𝒮 ∈ 𝜓(𝐷). Let (𝑖, 𝑗) ∈ M. en for any node 𝑣 in 𝐷 ,

- (a) 𝑣 ∈ List (𝐷 ,𝑖, 𝑗) if and only if 𝑔(𝑣 ) ∈ List(𝐷,𝑖, 𝑗);
- (b) forany othernode𝑢 in𝐷 , if𝑔(𝑢 ) precedes𝑔(𝑣 ) inList(𝐷,𝑖, 𝑗), then𝑢 precedes𝑣 inList (𝐷 ,𝑖, 𝑗);
- (c) if 𝑣 ∈ 𝒮3 ∪ 𝒮4, then 𝑓 (𝑣) is next to 𝑓 ∗(𝑣) in List (𝐷 ,𝑖, 𝑗).


Proof. Part (a) is immediate by Denition 3.11.

Now, we show Part (b). Suppose 𝑔(𝑢 ) precedes 𝑔(𝑣 ) in List(𝐷,𝑖, 𝑗). en 𝑔(𝑢 ) ≺ 𝑔(𝑣 ) in 𝜋𝐷. us one can check that all the four arcs 𝑓 (𝑔(𝑢 )) → 𝑓 (𝑔(𝑣 )), 𝑓 ∗(𝑔(𝑢 )) → 𝑓 (𝑔(𝑣 )), 𝑓 (𝑔(𝑢 )) → 𝑓 ∗(𝑔(𝑣 )), and 𝑓 ∗(𝑔(𝑢 )) → 𝑓 ∗(𝑔(𝑣 )) are contained in 𝐸 2. In particular, (𝑢 → 𝑣 ) ∈ 𝐸 as 𝑢 ∈ {𝑓 (𝑔(𝑢 )), 𝑓 ∗(𝑔(𝑢 ))} and 𝑣 ∈ {𝑓 (𝑔(𝑣 )), 𝑓 ∗(𝑔(𝑣 ))}. is implies that 𝑢 precedes 𝑣 in List (𝐷 ,𝑖, 𝑗).

Finally, we prove Part (c). According to Part (b), 𝑓 (𝑣) and 𝑓 ∗(𝑣) are adjacent in List (𝐷 ,𝑖, 𝑗). Besides, as there is an arc 𝑓 ∗(𝑣) → 𝑓 (𝑣) in 𝐸 1, we conclude that 𝑓 (𝑣) is next to 𝑓 ∗(𝑣) in List (𝐷 ,𝑖, 𝑗).

Denition C.4. For a reversible arc 𝑢 → 𝑣 in 𝐷 , we call it (∗,↓)-reversible in 𝐷 if 𝐿 (𝑢 ) ∈ {𝑖↑,𝑖↓} and 𝐿 (𝑣 ) = 𝑗↓ for some (𝑖, 𝑗) ∈ 𝐸𝐷.

Claim C.5. Suppose 𝐷 = ℎ(𝐷,𝒮) for some 𝐷 ∈ D(𝐺𝐷) and 𝒮 ∈ 𝜓(𝐷). Let (𝑖, 𝑗) ∈ M. Let 𝑢 ,𝑣 be two nodes in List (𝐷 ,𝑖, 𝑗) where 𝑣 is next to 𝑢 . en 𝑢 ∈ 𝑉 2 if and only if 𝑢 → 𝑣 is (∗,↓)-reversible in 𝐷 and 𝑣 ∈ 𝑉 1.

Proof. =⇒: Let 𝑢 := 𝑔(𝑢 ). Assume 𝑢 ∈ 𝑉 2, i.e., 𝑢 = 𝑓 ∗(𝑢). By Denition 3.11, 𝑢 ∈ 𝒮3 ∪ 𝒮4. According to Part (c) of Claim C.3, as 𝑣 is next to 𝑢 , we have 𝑣 = 𝑓 (𝑢) and then 𝑣 ∈ 𝑉 1.

Now we show that 𝑢 → 𝑣 is (∗,↓)-reversible. First, by Denition 3.11, either 𝐿 (𝑢 ) ∈ {𝑖↑,𝑖↓} and 𝐿 (𝑣 ) = 𝑗↓, or 𝐿 (𝑢 ) ∈ {𝑗↑, 𝑗↓} and 𝐿 (𝑣 ) = 𝑖↓. What remains is to show 𝑢 → 𝑣 is reversible, by Fact 2.5 which is equivalent to show that 𝑓 ∗(𝑢) → 𝑓 (𝑢) is the unique path from 𝑢 to 𝑣 in 𝐷 . By

contradiction, assume that there is a path 𝑓 ∗(𝑢) → 𝑤 1 → · · · → 𝑤 𝑘 → 𝑓 (𝑢) in 𝐷 where 𝑤 1 ≠ 𝑓 (𝑢) and 𝑤 𝑘 ≠ 𝑓 ∗(𝑢). As 𝑤 1 ≠ 𝑓 (𝑢), we have (𝑓 ∗(𝑢) → 𝑤 1) is not in 𝐸 1 and then should be in 𝐸 2, which further implies that 𝑢 ≺ 𝑔(𝑤 1) in 𝜋𝐷. Similarly, we have 𝑔(𝑤 𝑘) ≺ 𝑢 in 𝜋𝐷. So 𝑔(𝑤 𝑘) ≺ 𝑢 ≺ 𝑔(𝑤 1). Meanwhile, for each ℓ < 𝑘, if (𝑤 ℓ → 𝑤 ℓ+1) ∈ 𝐸 1, then 𝑔(𝑤 ℓ) = 𝑔(𝑤 ℓ+1); if (𝑤 ℓ → 𝑤 ℓ+1) ∈ 𝐸 2, then 𝑔(𝑤 ℓ) ≺ 𝑔(𝑤 ℓ+1) in 𝜋𝐷. So, it always holds that 𝑔(𝑤 ℓ) 𝑔(𝑤 ℓ+1) in 𝜋𝐷 for each ℓ < 𝑘. In particular, 𝑔(𝑤 1) 𝑔(𝑤 𝑘). A contradiction.

⇐=: Let 𝑢 := 𝑔(𝑢 ) and 𝑣 := 𝑔(𝑣 ). Assume 𝑢 ∉ 𝑉 2 and 𝑣 ∈ 𝑉 1, i.e., 𝑢 = 𝑓 (𝑢) and 𝑣 = 𝑓 (𝑣). Furthermore, assume 𝐿 (𝑣 ) = 𝑗↓, then 𝑣 ∉ 𝒮1 and 𝐿(𝑣) = 𝑗. We will show that (𝑓 (𝑢) → 𝑓 (𝑣)) is not reversible.

Note that (𝑓 (𝑢) → 𝑓 (𝑣)) should be in 𝐸 2 and then 𝑢 ≺ 𝑣 in 𝜋𝐷. By 𝐿 (𝑢 ) ∈ {𝑖↑,𝑖↓}, 𝑢 = 𝑓 (𝑢), and (2), we have 𝐿(𝑢) = 𝑖. us, (𝐿(𝑢),𝐿(𝑣)) = (𝑖, 𝑗) ∈ M ⊆ 𝐸𝐷. As 𝐷 is a wdag and 𝑢 ≺ 𝑣 in 𝜋𝐷, the arc (𝑢 → 𝑣) exists in 𝐷. Since 𝑣 ∉ 𝒮1, 𝑣 ∉ V, which means that 𝑢 → 𝑣 is not reversible in 𝐷. According to Fact 2.5, there is a path 𝑢 = 𝑤1 → 𝑤2 → · · · → 𝑤𝑘 → 𝑤𝑘+1 = 𝑣 from 𝑢 to 𝑣 in 𝐷 other than the arc 𝑢 → 𝑣, where 𝑤ℓ ≺ 𝑤ℓ+1 in 𝜋𝐷 and (𝐿(𝑤ℓ) = 𝐿(𝑤ℓ+1)) ∨ ((𝐿(𝑤ℓ),𝐿(𝑤ℓ+1)) ∈ 𝐸𝐷) for each ℓ ∈ [𝑘].

According to the denition of 𝐺M and (2), one can check that (𝑓 (𝑤𝑖) → 𝑓 (𝑤𝑖+1)) ∈ 𝐸 2. erefore 𝑢 = 𝑓 (𝑤1) → 𝑓 (𝑤2) → · · · → 𝑓 (𝑤𝑘) → 𝑓 (𝑤𝑘+1) = 𝑣 is a path from 𝑢 to 𝑣 in 𝐷 , which implies that 𝑢 → 𝑓 (𝑣) is not reversible in 𝐷 by Fact 2.5.

Having Claims C.3 and C.5, we are ready to show that ℎ is injective. Lemma C.6. ℎ is injective. Proof. Fix a 𝐷 = (𝑉,𝐸,𝐿) ∈ D(𝐺𝐷) and a 𝒮 ∈ 𝜓(𝐷). Let 𝐷 = (𝑉 ,𝐸 ,𝐿 ) denote ℎ(𝐷,𝒮). We show (𝐷,𝒮) can be recovered from 𝐷 , which implies the injectiveness of ℎ.

First, we recover the partition (𝑉 1,𝑉 2). at is, given a node 𝑢 ∈ 𝑉 , we distinguish whether 𝑢 ∈ 𝑉 1 or 𝑢 ∈ 𝑉 2. If 𝐿 (𝑢 ) ∈ [𝑚] \ M, then 𝑢 ∈ 𝑉 1 according to (2). Otherwise, we have 𝐿 (𝑢 ) ∈ {𝑖↑,𝑖↓} for some (𝑖, 𝑗) ∈ M, hence 𝑢 is in List (𝐷 ,𝑖, 𝑗). Assume the nodes in List (𝐷,𝑖, 𝑗) are 𝑣 1𝑣 2𝑣 3 · · ·𝑣 𝑘. According to Claim C.5, we can see that the following procedure distinguishes whether 𝑣 ℓ ∈ 𝑉 1 or 𝑣 𝑘 ∈ 𝑉 2 for all 𝑣 ℓ ∈ List (𝐷 ,𝑖, 𝑗), including 𝑢 .

- 1 Initially, mark that 𝑣 𝑘 ∈ 𝑉 1, and let ℓ := 𝑘 − 1;
- 2 while ℓ ≥ 1 do

- 3 if the arc (𝑣 ℓ → 𝑣 ℓ+1) is (∗,↓)-reversible and 𝑣 ℓ+1 ∈ 𝑉 1 then

- 4 Mark that 𝑣 ℓ ∈ 𝑉 2;
- 5 else

- 6 Mark that 𝑣 ℓ ∈ 𝑉 1;

- 7 ℓ := ℓ − 1;


Secondly, we can easily recover 𝐷 = (𝑉,𝐸,𝐿) from 𝐷 and (𝑉 1,𝑉 2). Ignoring labels, it is easy to see that 𝐷 is exactly the induced subgraph of 𝐷 on 𝑉 1. By the way, we also get the function 𝑓 : 𝑉 → 𝑉 1. For labels, we simply replace each label 𝑖↑ or 𝑖↓ with 𝑖.

Finally, we recover 𝒮 from 𝐷 , 𝐷 and (𝑉 1,𝑉2). at is, we distinguish which one of {𝒮1,𝒮2,𝒮3,𝒮3} contains a given node 𝑣 ∈ ℳ(𝐷). Assume 𝐿(𝑣) = 𝑖 and (𝑖, 𝑗) ∈ M. Let 𝑢 be the node previous to 𝑓 (𝑣) in List (𝐷,𝑖, 𝑗). According to Part (c) of Claim C.3,𝑢 ∈ 𝑉 2 if and only if 𝑣 ∈ 𝒮3 ∪𝒮4. When 𝑣 ∈ 𝒮3 ∪𝒮4, 𝑣 ∈ 𝒮3 if 𝐿 (𝑢 ) = 𝑗↑, and 𝑣 ∈ 𝒮4 if 𝐿 (𝑢 ) = 𝑗↓. When 𝑣 ∉ 𝒮3 ∪ 𝒮4, 𝑣 ∈ 𝒮1 if 𝐿 (𝑣 ) = 𝑖↑, and 𝑣 ∈ 𝒮2 if 𝐿 (𝑣 ) = 𝑖↓.

A        D. P     L     6.1

Let 𝒆𝒊 denote the vector whose coordinates are all 0 except the 𝑖-th that equals 1. e following lemmas will be used in the proof. Lemma D.1. [HLSZ19] Let 𝐺𝐷 = ([𝑚],𝐸𝐷) be a dependency graph and 𝒑 be a probability vector beyond the Shearer’s bound. Suppose 𝑖,𝑖1,𝑖2, · · · ,𝑖𝑘−1,𝑖 form a shortest path from 𝑖 to 𝑖 in 𝐺𝐷. en for any 𝑞 ≤ 𝑝𝑖 , 𝒑 − 𝑞𝒆𝒊 + ℓ∈[𝑘−1]

1−𝑝𝑖ℓ

𝑝𝑖ℓ · 1𝑝−𝑝𝑖

· 𝑞𝒆𝒊 is also beyond the Shearer’s bound.

𝑖

Without loss of generality, we assume that 𝑝𝑖 − 𝑝𝑎 is rational for each 𝑖 ∈ [𝑚]. By contradiction, let 𝒑 be such a vector which is beyond Shearer’s bound. Let 𝑆+ := {𝑖 ∈ [𝑚] : 𝑝𝑖 > 𝑝} and 𝑆− := {𝑖 ∈ [𝑚] : 𝑝𝑖 < 𝑝}. Let Δ𝑝 be a real number such that the following hold:

- • For each 𝑖 ∈ 𝑆+, 𝑝𝑖 − 𝑝𝑎 = 𝛾𝑖 · Δ𝑝 for some 𝛾𝑖 ∈ N+. Intuitively, we cut 𝑝𝑖 − 𝑝𝑎 into 𝛾𝑖 pieces each of size Δ𝑝. Besides, we call such pieces positive pieces.
- • For each 𝑖 ∈ 𝑆−,


𝑑−1

Δ𝑝 𝑝𝑎

1 − 𝑝𝑎 𝑝𝑎

𝑝𝑎 − 𝑝𝑖 = 𝜏𝑖 · 𝐾 ·

·

𝑑−1

· Δ𝑝𝑝

for some 𝜏𝑖 ∈ N+. Intuitively, we cut 𝑝𝑎 − 𝑝𝑖 into 𝜏𝑖 · 𝐾 pieces each of size 1−𝑝𝑎

. We call such pieces negative pieces.

𝑝𝑎

𝑎

We use R := {(𝑖,𝑟) : 𝑖 ∈ 𝑆+,𝑟 ∈ [𝛾𝑖]} and T {(𝑖 ,𝑡,𝑘) : 𝑖 ∈ 𝑆−,𝑡 ∈ [𝜏𝑖 ],𝑘 ∈ [𝐾]} to denote the set of positive pieces and negative pieces respectively.

For convenience, let 𝛾𝑖 = 0 if 𝑖 ∉ 𝑆+, and 𝜏𝑖 = 0 if 𝑖 ∉ 𝑆−. en Condition (c) can be restated as: for 𝑓 (𝑆) = 𝑇, the positive pieces in 𝑆 are no more than the negative pieces in 𝑇, i.e.,

### ∑︁

𝛾𝑖 ≤ ∑︁ 𝑖 ∈𝑇

- (16) 𝜏𝑖 .


𝑖∈𝑆

e basic idea of Lemma 6.1 is relatively simple: for each 𝑆 ∈ S, we move positive pieces in 𝑆 to 𝑓 (𝑆) such that (i) all the positive pieces in 𝑆 are absorbed by the negative pieces in 𝑓 (𝑆) and (ii) the resulted probability vector is still beyond Shearer’s bound. Finally, all positive pieces will be absorbed, and we will get a vector strictly smaller than 𝒑. By Lemma D.1, this vector is beyond Shearer’s bound, which makes a contradiction.

For 𝑖 ∈ [𝑚], remember Condition (a) which says that there are at most 𝐾 subsets 𝑆 ⊂ S such that 𝑖 ∈ 𝑓 (𝑆), and we use 𝑆𝑖1 ,𝑆𝑖2 , · · · to represent these subsets. Let 𝑔 : R → T be a injection mapping each (𝑖,𝑟) ∈ R to some (𝑖 ,𝑡,𝑘) ∈ T satisfying that (i) 𝑖 ∈ 𝑆𝑖𝑘 and (ii)

### ∑︁

### 𝛾𝑖0 + 𝑟 = ∑︁

𝜏𝑖1 + 𝑡.

𝑖0∈𝑆𝑖𝑘 ,𝑖0<𝑖

𝑖1∈𝑓 (𝑆𝑖𝑘 ),𝑖1<𝑖

By (16), one can verify that such mapping 𝑔 exists. In addition, according to Condition (b), if 𝑔(𝑖,𝑟) = (𝑖 ,𝑡,𝑘), then dist(𝑖,𝑖 ) ≤ 𝑑.

In the following, we will apply Lemma D.1 repeatedly. Let 𝑔0 be 𝑔, 𝑆0 be 𝑆− and R0 be R. Given an injection 𝑔𝜅 : R → T, 𝑆𝜅 and R𝜅 where dis(𝑖, 𝑗) ≤ 𝑑 if

𝑔𝜅(𝑖,𝑟) = (𝑗,𝑡,𝑘), we construct another injection 𝑔𝜅+1 : R → T, 𝑆𝜅+1 and R𝜅+1 as follows. ere are two possible cases for 𝑔𝜅, 𝑆𝜅 and R𝜅.

- (1) there exists𝑖,𝑟, 𝑗,𝑡,𝑘 such that (𝑖,𝑟) ∈ R𝜅,𝑔𝜅(𝑖,𝑟) = (𝑗,𝑡,𝑘) and there is a shortest path between 𝑖 and 𝑗 such that no vertex in 𝑆𝜅 is on the path;
- (2) For each 𝑔𝜅(𝑖,𝑟) = (𝑗,𝑡,𝑘) where (𝑖,𝑟) ∈ R𝜅 and each shortest path between 𝑖 and 𝑗, there is a vertex in 𝑆𝜅 on the path.


- For case (1), we let 𝑔𝜅+1 = 𝑔𝜅, R𝜅+1 = R𝜅 \ {(𝑖,𝑟)}, and 𝑆𝜅+1 = {𝑗 ∈ 𝑆− : there exists 𝑖,𝑟,𝑡,𝑘 where (𝑖,𝑟) ∈ R𝜅+1 such that 𝑔𝜅+1(𝑖,𝑟) = (𝑗,𝑡,𝑘)}.
- For case (2), there must be (𝑖1,𝑟1, 𝑗1,𝑡1,𝑘1), · · · , (𝑖𝑛,𝑟𝑛, 𝑗𝑛,𝑡𝑛,𝑘𝑛) for some 𝑛 ∈ N+ such that


- - (𝑖ℓ,𝑟ℓ) ∈ R𝜅, 𝑗ℓ ∈ 𝑆𝜅, 𝑔𝜅(𝑖ℓ,𝑟ℓ) = (𝑗ℓ,𝑡ℓ,𝑘ℓ) for each ℓ ∈ [𝑛],
- - 𝑗ℓ+1 is on a shortest path between 𝑖ℓ and 𝑗ℓ for each ℓ ∈ [𝑛 − 1],
- - 𝑗1 is on a shortest path between 𝑖𝑛 and 𝑗𝑛.


We dene the injection 𝐹(𝑔𝜅) as follows.

 

𝐹(𝑔𝜅)(𝑖𝑛,𝑟𝑛) = (𝑗1,𝑡1,𝑘1), 𝐹(𝑔𝜅)(𝑖ℓ,𝑟ℓ) = (𝑗ℓ+1,𝑡ℓ+1,𝑘ℓ+1) for each ℓ ∈ [𝑛 − 1], 𝐹(𝑔𝜅)(𝑖,𝑟) = 𝑔𝜅(𝑖,𝑟) for other (𝑖,𝑟).

 

One can verify that dis(𝑖, 𝑗) ≤ 𝑑 if 𝐹(𝑔𝜅)(𝑖,𝑟) = (𝑗,𝑡,𝑘) and 𝑁 ∑︁

### dis(𝑖, 𝑗) ≥ 1 + ∑︁

dis(𝑖, 𝑗).

(𝑖,𝑟,𝑗,𝑡,𝑘): 𝑔𝜅 (𝑖,𝑟)=(𝑗,𝑡,𝑘)

(𝑖,𝑟,𝑗,𝑡,𝑘): 𝐹 (𝑔𝜅)(𝑖,𝑟)=(𝑗,𝑡,𝑘)

Since 𝑁 is bounded, there must be a constant ℓ ≤ 𝑁 and 𝑖,𝑟, 𝑗,𝑡,𝑘 such that (𝑖,𝑟) ∈ R𝜅, 𝐹ℓ(𝑔𝜅)(𝑖,𝑟) = (𝑗,𝑡,𝑘) and there is a shortest path between 𝑖 and 𝑗 such that no vertex in 𝑆𝜅 is on the path. Let 𝑔𝜅+1 = 𝐹ℓ(𝑔𝜅), R𝜅+1 = R𝜅 \ {(𝑖,𝑟)} and

𝑆𝜅+1 = {𝑗 ∈ 𝑆− : there exists 𝑖,𝑟,𝑡,𝑘 where (𝑖,𝑟) ∈ R𝜅+1 such that 𝑔𝜅+1(𝑖,𝑟) = (𝑗,𝑡,𝑘)}. One can verify that in both cases,𝑔𝜅+1 is an injection from R to T and dis(𝑖, 𝑗) ≤ 𝑑 if𝑔𝜅+1(𝑖,𝑟) = (𝑗,𝑡,𝑘).

Let 𝑔 be 𝑔|R|. For each ℓ ∈ [|R|], let (𝑖ℓ,𝑟ℓ) be the unique element in Rℓ−1 \ Rℓ. Let (𝑗ℓ,𝑡ℓ,𝑘ℓ) denote 𝑔 (𝑖ℓ,𝑟ℓ). us, we have

- - 𝑔 is an injection from R to T,
- - dis(𝑖ℓ, 𝑗ℓ) ≤ 𝑑 for each ℓ ∈ [|R|],


- - there is a shortest path between 𝑖ℓ and 𝑗ℓ such that 𝑗ℓ+1, 𝑗ℓ+2, · · · , 𝑗|R| ∈ 𝑆ℓ are not on the path.


For each 𝑗 ∈ 𝑆−, dene

𝜂𝑗 = |{(𝑖,𝑟) : 𝑔 (𝑖,𝑟) = (𝑗,𝑡,𝑘) for some 𝑡 ∈ [𝜏𝑗],𝑘 ∈ [𝐾]}|. Because 𝑔 is an injection, we have 𝜂𝑗 ≤ 𝜏𝑗 · 𝐾. Let

𝒑 𝒑 + ∑︁

𝑑−1

Δ𝑝 𝑝 · 𝒆𝑗.

1 − 𝑝 𝑝

·

(𝐾 · 𝜏𝑗 − 𝜂𝑗) ·

𝑗 ∈𝑆−

By 𝒑 is beyond Shearer’s bound and 𝜂𝑗 ≤ 𝐾 · 𝜏𝑗 for each 𝑗 ∈ 𝑆−, we have 𝒑 is also beyond Shearer’s bound. For each ℓ ∈ [0, |R|], let

𝒑ℓ 𝒑 − Δ𝑝 · ∑︁

𝑑−1

𝑑−1

1 − 𝑝 𝑝

1 − 𝑝 𝑝

1 𝑝 · 𝒆𝑗𝜅 + 𝒆𝑖ℓ −

1

𝒆𝑖𝜅 −

·

·

𝑝 + Δ𝑝 · 𝒆𝑗ℓ .

𝜅≤ℓ−1

en we have the following claim. Claim D.2. For ℓ ∈ [0, |R|], 𝒑ℓ is beyond Shearer’s bound. Proof. We prove this claim by induction. Obviously, 𝒑0 is beyond Shearer’s bound. In the following, we prove that if 𝒑ℓ−1 is beyond Shearer’s bound, then 𝒑ℓ is also beyond Shearer’s bound.

Let

### 𝒒 𝒑 − Δ𝑝 · ∑︁

𝑑−1

1 − 𝑝 𝑝

1 𝑝 · 𝒆𝑗𝜅 .

·

𝒆𝑖𝜅 −

𝜅≤ℓ−1

Obviously, 𝒒 ≥ 𝒑ℓ−1. By 𝒑ℓ−1 is beyond Shearer’s bound, we have 𝒒 is also beyond Shearer’s bound. Note that there is a shortest path 𝑖ℓ,𝑘1,𝑘2, · · · ,𝑘𝑛, 𝑗ℓ between 𝑖ℓ and 𝑗ℓ such that 𝑗ℓ+1, 𝑗ℓ+2, · · · , 𝑗|R| are not on the path. Because 𝒒 is beyond Shearer’s bound, by Lemma D.1, we have

### 1 − 𝑞𝑘𝑡

1 𝑞𝑖 · 𝒆𝑗ℓ

𝒒 𝒒 − Δ𝑝 · 𝒆𝑖ℓ −

𝑞𝑘𝑡 ·

𝑡 ∈[𝑛]

is also beyond Shearer’s bound. Meanwhile, by (𝑖ℓ,𝑟ℓ) ∈ R, we have 𝑞𝑖ℓ = 𝑝 𝑖 − Δ𝑝 ∑︁

(𝑖𝜅 = 𝑖ℓ) ≥ 𝑝 𝑖 − (𝛾𝑖 − 1)Δ𝑝 ≥ 𝑝𝑖 + Δ𝑝.

𝜅∈ℓ−1

For each 𝑡 ∈ [𝑛], if 𝑘𝑡 ∉ 𝑆−, we have 𝑞𝑘𝑡 ≥ 𝑝. Otherwise, 𝑘𝑡 ∈ 𝑆−, and 𝑘𝑡 ≠ 𝑗𝜅 for each 𝜅 ≥ ℓ. us, we have 𝜅∈ℓ−1 (𝑗𝜅 = 𝑘𝑡) = 𝜂𝑘𝑡. erefore,

Δ𝑝 𝑝 + ∑︁

𝑑−1

𝑑−1

Δ𝑝 𝑝

1 − 𝑝 𝑝

1 − 𝑝 𝑝

𝑞𝑘𝑡 = 𝑝 𝑘

(𝑗𝜅 = 𝑘𝑡) ·

·

·

+ (𝐾 · 𝜏𝑘𝑡 − 𝜂𝑘𝑡) ·

𝑡

𝜅∈ℓ−1

𝑑−1

𝑑−1

Δ𝑝 𝑝 + 𝜂𝑘𝑡 ·

Δ𝑝 𝑝

1 − 𝑝 𝑝

1 − 𝑝 𝑝

= 𝑝 𝑘

= 𝑝.

+ (𝐾 · 𝜏𝑘𝑡 − 𝜂𝑘𝑡) ·

·

·

𝑡

By dis(𝑖, 𝑗) ≥ 𝑑,𝑞𝑖ℓ ≥ 𝑝 + Δ𝑝 and 𝑞𝑘𝑡 ≥ 𝑝 for each 𝑡 ∈ [𝑛], we have

𝑑−1

### 1 − 𝑞𝑘𝑡

1 − 𝑝 𝑝

1 𝑞𝑖

1 𝑝 + Δ𝑝

𝑞𝑘𝑡 ·

·

<

.

𝑡 ∈[𝑛]

us, by 𝒒 is beyond Shearer’s bound, we have

𝑑−1

1 − 𝑝 𝑝

1

𝒑ℓ = 𝒒 − Δ𝑝 · 𝒆𝑖ℓ −

𝑝 + Δ𝑝 · 𝒆𝑗ℓ is also beyond Shearer’s bound.

·

us, we have 𝒑|R| is beyond Shearer’s bound. It is easy to verify that𝒑|R| < 𝒑, which is contradictory with that 𝒑 is on Shearer’s boundary.

A        E. M       T       6.2

Proof of Claim 6.3. Observe that for each (𝑣,𝑣 ) ∈ 𝐸𝑈𝑘 , if (𝑣,𝑣 ) ∉ M, then one of its neighboring edge (𝑣0,𝑣1) is in 𝑇𝑘 and satises that 𝛿𝑣,𝑣 ≤ 𝛿𝑣0,𝑣1. Here, we say two edges neighboring if they share a common vertex. Besides, note that each edge has at most 2Δ neighboring edges. So

∑︁

∑︁

1 2Δ

- (17) 𝛿𝑣,𝑣2 .

Moreover, according to Lemma 4.2 and 4.5, it has that

∑︁

(𝑣,𝑣 )∈𝐸𝑈𝑘

𝛿𝑣,𝑣2 ≥

1 |𝐸𝑈𝑘 |

· ∑︁

(𝑣,𝑣 )∈𝐸𝑈𝑘

𝛿𝑣,𝑣

2

≥

|𝑉𝑈𝑘| · Δ2 |𝐸𝑈𝑘 |

- (18) · +(𝐺𝐵(𝐺𝐷),𝒑) 2 ,

By combining Inequality 17, 18 and the fact that 2|𝐸𝑈𝑘 | ≤ |𝑉𝑈𝑘|Δ, we nish the proof.

Let 𝐾 := (Δ + 1)|𝑉𝑈 |, 𝑑 := 𝐷 + 2, S := {𝑉𝑈1,𝑉𝑈2, · · · }, and 𝑓 (𝑉𝑈𝑘) := 𝑇𝑘. In the following, we check that all the three conditions in Lemma 6.1 hold.

- Condition (a). at is, we want to show |{𝑘 : 𝑇𝑘 𝑣}| ≤ (Δ + 1)|𝑉𝑈 | for each 𝑣 ∈ 𝑉𝐷. Observe that if 𝑣 ∈ 𝑇𝑘, then 𝑣 ∈ N+(𝑉𝑈𝑘). So

|{𝑘 : 𝑇𝑘 𝑣}| ≤ |{𝑘 : N+(𝑉𝑈𝑘) 𝑣}| ≤ |{𝑘 : N+(𝑣)∩𝑉𝑈𝑘 ≠ ∅}| ≤ ∑︁

𝑣 ∈N+(𝑣)

|{𝑘 : 𝑉𝑈𝑘 𝑣 }| ≤ (Δ+1)·|𝑉𝐷|. e last inequality uses the fact that ℎ(𝑘 ,𝑢) ≠ ℎ(𝑘,𝑢) if 𝑘 ≠ 𝑘 .

- Condition (b). at is, we want to show dist(𝑣,𝑣 ) ≤ 𝐷 + 2 for any 𝑣 ∈ 𝑉𝑈𝑘 and 𝑣 ∈ 𝑇𝑘. is is obvious, because if 𝑣 ∈ 𝑇𝑘, then 𝑣 ∈ N+(𝑉𝑈𝑘).

- Condition (c). We verify that


1 − 𝑝𝑎 𝑝𝑎

𝐷+1

·

𝐾 𝑝𝑎 · ∑︁

𝑖∈𝑆

max{𝑝𝑖 − 𝑝𝑎, 0} ≤ ∑︁ 𝑖∈𝑇

- (19) max{𝑝𝑎 − 𝑝𝑖, 0}.

On one hand, noting that max{(1 + 𝜀)𝑝𝑣− − 𝑝𝑎, 0} ≤ max{(1 + 𝜀)𝑝𝑣 − 𝑝𝑎, 0} ≤ 𝑞, we have L.H.S of (19) ≤

1 − 𝑝𝑎 𝑝𝑎

𝐷+1

·

(Δ + 1)|𝑉𝑈 |2

- (20) 𝑝𝑎 · 𝑞. On the other hand, observe that

max{𝑝𝑎 − (1 + 𝜀)𝑝𝑣−, 0} ≥ 𝑝𝑎 − (1 + 𝜀)𝑝𝑣− = (𝑝𝑎 + 𝑞 − (1 + 𝜀)𝑝𝑣−) − 𝑞 ≥ (1 + 𝜀)(𝑝𝑣 − 𝑝𝑣−) − 𝑞 ≥ (𝑝𝑣 − 𝑝𝑣−) − 𝑞,

where the last inequality is due to the assumption that (1 + 𝜀)𝒑 ≤ (𝑝𝑎 + 𝑞, · · · ,𝑝𝑎 + 𝑞). en

R.H.S of (19) ≥ ∑︁

𝑣∈𝑉𝑈𝑘

(𝑝𝑣 − 𝑝𝑣−) − |N+(𝑉𝑈𝑘)|𝑞 ≥

2 17

∑︁

(𝑣0,𝑣1)∈𝑇𝑘

𝛿𝑣20,𝑣1 − Δ|𝑉𝑈 |𝑞

≥

2 17

- (21) +(𝐺𝐵(𝐺𝐷),𝒑) 2 − Δ|𝑉𝑈 |𝑞.


𝛿𝑣20,𝑣1 ≥

(𝑣0,𝑣1)∈𝑇𝑘

(𝑣,𝑣 )∈𝐸𝑈𝑘

Puing Inequality 20 and 21 together and noting that 1−𝑝𝑎 𝑝𝑎 ≥ 1.

