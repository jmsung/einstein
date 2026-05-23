---
type: source
kind: paper
title: Optimization-friendly generic mechanisms without money
authors: Mark Braverman
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2106.07752v1
source_local: ../raw/2021-braverman-optimization-friendly-generic-mechanisms-with.pdf
topic: general-knowledge
cites:
---

arXiv:2106.07752v1[cs.GT]14Jun2021

# Optimization-friendly generic mechanisms without money

### Mark Braverman*

Abstract

The goal of this paper is to develop a generic framework for converting modern optimization algorithms into mechanisms where inputs come from self-interested agents.

We focus on aggregating preferences from n players in a context without money. Special cases of this setting include voting, allocation of items by lottery, and matching. Our key technical contribution is a new meta-algorithm we call APEX (Adaptive Pricing Equalizing Externalities). The framework is sufﬁciently general to be combined with any optimization algorithm that is based on local search. We outline an agenda for studying the algorithm’s properties and its applications.

As a special case of applying the framework to the problem of one-sided assignment with lotteries, we obtain a strengthening of the 1979 result by Hylland and Zeckhauser on allocation via a competitive equilibrium from equal incomes (CEEI). The [HZ79] result posits that there is a (fractional) allocation and a set of item prices such that the allocation is a competitive equilibrium given prices. We further show that there is always a reweighing of the players’ utility values such that running unit-demand VCG with reweighed utilities leads to a HZequilibrium prices. Interestingly, not all HZ competitive equilibria come from VCG prices. As part of our proof, we re-prove the [HZ79] result using only Brouwer’s ﬁxed point theorem (and not the more general Kakutani’s theorem). This may be of independent interest.

![image 1](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile1.png>)

*Department of Computer Science, Princeton University. Research supported in part by the NSF Alan T. Waterman Award, Grant No. 1933331, a Packard Fellowship in Science and Engineering, and the Simons Collaboration on Algorithms and Geometry. Any opinions, ﬁndings, and conclusions or recommendations expressed in this publication are those of the author and do not necessarily reﬂect the views of the National Science Foundation.

Acknowledgments. I gratefully acknowledge the many comments that helped shape this paper from Itai Ashlagi, Antonio Molina Lovett, Aviad Rubinshtein, Matt Weinberg, and the detailed comments from Sahil Singla. This paper was inﬂuenced by discussions with Georgy Noarov, Sahil Singla, Matt Weinberg, Leeat Yariv, and Yufei Zheng.

### Overview and summary of results

Motivation. Our main goal is to develop a generic reduction for converting algorithms based on iterated local optimization into mechanisms. We focus on mechanisms without money (which are generally more difﬁcult to design). We would like our reduction to work for heuristics that have good empirical performance even in lieu of formal guarantees. Therefore, our reduction aims to change the algorithm as little as possible, while attaining good incentive properties.

Speciﬁcally, we start with n players who have preference functions fi over an outcome space X. There is an optimization heuristic H for maximizing functions over X. The heuristic H is local — giving a recipe for constructing a sequence x0, x1, . . . ∈ X that (hopefully) converges to a highvalue outcome. Our goal is to use H to produce a mechanism that (1) matches the performance of H as much as possible; (2) leads to a correlated equilibrium where for each player i, reporting fi truthfully is an approximately dominant strategy.

Main ingredients. We connect three main ingredients: (1) online learning and its connection to correlated equilibria in games; (2) the VCG mechanism — a mechanism with money, where truthful reporting by participants is a dominant strategy; and (3) bandits with knapsacks (BwK) — a special type of online learning where players obtain a reward and experience a capacity cost every time they pull an arm, and where the aim is to maximize total reward subject to a capacity budget. We will elaborate on these ingredients in Sections 1.1–1.4.

The APEX algorithm and framework. Our main APEX (adaptive pricing equalizing externalities) framework is given by Algorithm 1 in Section 2.1. It is most closely related to CEEI (competitive equilibria from equal incomes) in the mechanism design literature, with a major distinction being that the equilibrium gets discovered together with the participants via an iterated optimization procedure using heuristic H by the principal.

The principal receives utility functions f1, . . ., fn from the players1, and a sequence of coefﬁcients λi,t ≥ 0 representing the weight the i-th player’s preferences should be given at round t. Each player receives a ﬁxed token endowment B at the beginning of the execution.

At round t, the principal uses heuristic H to (locally) optimize the objective i λi,tfi(x) possibly with a regularizer added to it. The principal then uses H to perform local optimization in order to calculate VCG prices (in tokens) that the players will get charged. The players, from their end, will run bandits with knapsacks algorithms to produce λi,t’s in order to maximize their utility subject to the token budget of B.

The output of the mechanism is the long-term trajectory of this iterated game. Assuming players have negligible regrets, all players are either maximally happy or exhaust their token budgets

— which mean that their averaged VCG payments (and thus their externalities) are equalized.

![image 2](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile2.png>)

1The principal may not need to actually collect the fi’s. In fact, the players may not even need to know their own fi’s. The algorithm can be implemented purely using gradient queries, where players are asked to give their local preference ∇fi(x) at a given point x.

General results. The APEX algorithm converges if after some number of iterations: (1) a goodvalue solution to the optimization problem is reached; (2) players have negligible regret with respect to their actions in the bandits-with-knapsacks game. The framework is very general, and it is unlikely that a full-generality convergence result can be proved (especially since we do not wish to make assumptions on the heuristic H). However, assuming the algorithm converges, we can show that it leads to an approximate correlated equilibrium where truthful reporting of fi is dominant:

Lemma 4. [restated] Suppose that fi(x) ∈ [0, 1] for all x ∈ X, and that during the execution of Algorithm 1 with budget Bi and a truthfully reported fi, Player i has strong regret ≤ ε. Suppose further that heuristic H is locally correct. Then reporting fi truthfully is an (2ε)-dominant strategy for the menu of options available to Player i that is induced by the mechanism.

The conditions of Lemma 4 can be veriﬁed given an execution of the mechanism. Even if we can’t be sure that the mechanism will converge, we can be assured of good incentive properties given a convergent execution. Therefore, the framework allows us to convert heuristic algorithms into heuristic mechanisms.

Application: new results for the one-sided matching problem. In Section 3, we discuss applications of the framework to three classical areas of mechanisms without money: voting, one-sided assignment, and two-sided matching. Voting with cardinal preferences (Section 3.1) is subject of an ongoing work and is mostly beyond the scope of this paper. Efﬁcient two-sided matching (Section 3.3) — the Gale-Shapley setting but with cardinal preferences — is perhaps the most interesting immediate application of our framework. Plugging the two-sided matching setup into the APEX framework gives interesting initial results, but a key deﬁnition of “externality” in this setting appears to be non-canonical. We discuss this issue in detail in Section 3.3.

One area where we are able to immediately use the APEX framework to obtain new results is one-sided assignment. A classical result of Hylland and Zeckhauser [HZ79] states that in a setting without money n items can be allocated to n unit-demand players via lotteries using an equilibrium from equal incomes (CEEI). Given utilities uij ≥ 0 — the utility of player i for item j — there are prices Pj ≥ 0 assigned to items, and a bi-stochastic n × n allocation matrix X, such that Xi is the best distribution on items Player i can afford with a unit budget and prices {Pj}.

By plugging the one-sided allocation into the APEX framework, where one iteration is unitdemand VCG with utilities {λi,t · uij}, we obtain a strengthening of the HZ result. We show that there is always a scaling of utilities such that resulting VCG prices support a HZ equilibrium.

Theorem 5. [restated] Let U = {uij}i,j=1..n be a matrix utilities with uij ≥ 0. Then there exist numbers λi ≥ 0, prices C = {Cj} and an allocation X = {xij} with the following properties.

- 1. X is a valid allocation: ∀j : i xij = 1 and ∀i : j xij = 1;
- 2. Cj are the VCG prices for utilities given by u′ij = λiuij;
- 3. X is a combination of optimal allocations under u′: for every π : [n] → [n] with ∀i xiπ(i) > 0 we have


u′iπ(i) = max

u′iσ(i).

σ

i

i

- 4. The players can purchase their allocations with budget not exceeding 1. For each player i,

j

Cjxij ≤ 1.

- 5. Prices Cj and allocation X form a HZ equilibrium. That is, for every player i


j

u′ijxij = max y : j

Cjyj ≤ 1 j yj = 1

j

u′ijyj.

Theorem 5 was discovered via the APEX framework, but we prove it directly using Brouwer’s ﬁxed-point theorem. Our proof is arguably simpler than the original proof of [HZ79], although it relies on the fact that properties of unit-demand VCG auctions are very well-understood at this point.

Interestingly, we show that not all HZ CEEI prices are VCG prices, and thus equilibria supported by VCG prices on scaled utilities form a proper subset of all HZ equilibria.

Even though Theorem 5 is proved directly without using the APEX algorithm, we do show that any low-regret execution execution of the APEX algorithm on a regularized objective

Ft(x) :=

i,j

λi,t · uijxij + F0(x)

will lead to an approximate HZ competitive equilibrium. Theorem 13. [informal, restated] In the unit-demand allocation setting without money with n players and n items, let {uij} ≥ 0 be utilities.

For each δ > 0, there is an ε > 0 and a concave regularizer F0(x) such that an execution of the APEX algorithm with regret < ε · T, leads to an allocation X and VCG prices C, such that X is supported by a δ-approximate competitive equilibrium from equal income with prices C.

## 1 Introduction

Algorithms play an increasingly important role in coordinating a broad range of human activity. Algorithm design addresses the problem of attaining a desired outcome on a given input. For example, ﬁnding a good allocation of tasks to machines, ﬁnding and maintaining a communication route between a client and a host, or optimizing an online advertisement campaign for maximum impact. More open-ended (in terms of objective function) important algorithmic tasks include internet search and matching consumers to goods and services. Another very important special class of algorithms has to do with building models for predicting the future — for example in the context of planning and control. Any process affecting the well-being of participants it does not directly control invites manipulation by those participants for their own beneﬁt, and algorithmdriven processes are not exempt from this rule. Examples range from strategic voting to the search

engine optimization industry. This motivates the ﬁeld of algorithmic mechanism design, whose goal is to design algorithms that work “well” even when the inputs come from self-interested players.

Algorithmic mechanism design and the price of anarchy. In mathematical terms, an algorithm induces a mechanism which can be analyzed using game-theoretic tools. Typically, the design goal is to attain a good performance in some kind of game-theoretic equilibrium: a situation where the output of the algorithm is good according to the prescribed performance metric, while participants cannot change their behavior (such as their input to the algorithm) to drastically improve their own well-being.

Almost any optimization problem can be cast into one (or more) mechanism design problem based on which participants are allowed to behave strategically, and the space of allowed strategic behaviors. Needless to say, the mechanism design problem is signiﬁcantly more difﬁcult both mathematically (having to deal with game-theoretic equilibria instead of simple objective function values), and in terms of the performance one can guarantee. In the algorithmic game theory literature the gap between the performance of the best optimization algorithm and the best (equilibrium) performance of a mechanism for the same problem is called the price of anarchy, and it can be signiﬁcant in many cases.

Online algorithms. An algorithmic setting which plays an important role both in practice and in the theory of machine learning is that of online algorithms. In the online setting, at time t the algorithm receives an input Xt, and needs to produce an action At(X1..t, Y1..t−1). It then learns the state of nature Yt at time t, and experiences loss L(Xt, At, Yt, Rt) (where Rt is random and is not observed directly). Consider the example of, say, learning to label objects. In this setting the algorithm receives object Xt, produces a label At. The reference label Yt is then revealed and the loss function measures some kind of distance between At and Yt. A low-loss algorithm would translate into a function that correctly predicts the mapping Xt  → Yt.

There exist multiple connections between optimization algorithms, online algorithms and game theory. Fueled by machine learning applications, there has been signiﬁcant progress in both theoretical and empirical understanding of online algorithms (and optimization algorithms that are tightly connected to them). Our goal is to investigate generic ways to extend this progress to algorithmic mechanism design. We start by exploring the three-way connection between optimization algorithms, online algorithms, and game theory.

### 1.1 Bandits and regret minimization

In this section we will brieﬂy survey the simplest setup for online algorithms, namely expert and bandit games. These games serve as an instructive (but tractable) model for more general machine learning scenarios, and have important connections to game theory and equilibria.

Setup. The game is played repeatedly for T time steps. At each step, the player is allowed to pull one of K available arms from set A2. The player incurs loss ℓit for pulling arm i at time t. The player’s goal is to minimize total loss of the sequence of pulls i = {it}Tt=1:

L(i) :=

T

ℓi

t,t.

t=1

One standard benchmark for the player to meet is to attain small weak regret, or regret against ﬁxed strategies:

T

T

R(i) :=

ℓi

t,t − min

ℓj,t . (1) That is, the goal is to perform better (or at least not much worse) than the best arm in hindsight.

j∈A

t=1

t=1

An important distinction in this context needs to be made between the bandits and the experts setting. In the bandits setting, the player only learns the loss resulting from her own action, while in the experts setting she also learns the (counterfactual) loss of actions not taken. The bandits setting is more appropriate in game-theoretic scenarios, where a player does not typically know the hypothetical outcome of actions not taken. The experts setting is a good ﬁt for machine learning problems, where it is possible to evaluate the performance of any model on past examples.

Generally speaking, minimizing regret as in (1) is a well-understood problem, in both the bandits and the experts setting [LS20]. Assume losses are bounded in [0, 1], and inputs are adversarial (that is, the player is allowed to randomize her strategy, and wishes to attain a low regret in expectation for any possible loss function). Then the best regret on can attain in the bandit setting is ∼

√T · K, and in the expert setting is ∼

√T · log K. In particular, in the bandits setting, regret becomes o(T) whenever K ≪ T holds3. In the expert setting regret becomes o(T) whenever K = 2o(T).

![image 3](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile3.png>)

![image 4](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile4.png>)

The best (or at least conceptually simplest) algorithms for online regret minimization come in the form of multiplicative weight updates: maintain vector of “weights” on arms (corresponding to the next arm the player will pull); upon learning the outcome of a pull, update this vector, penalizing the weight more if the loss was high.

There are two interesting variants of the bandit problem, which we would like to mention before exploring the connections between bandits and online algorithms further. The ﬁrst one has a direct connection to game theory equilibria, while the second will be important for our reductions from algorithms to VCG-based mechanisms.

Swap regret minimization. It is clear that the regret notion in (1) is just one of many possible regret notions, and that it can be strengthened by considering a richer class of strategies with which the player must compete. For example, one may not merely consider strategies taking a

![image 5](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile5.png>)

- 2The size K of A varies depending on the application domain. Generally, in the context of machine learning, A corresponds to the hypothesis class and is exponentially large in T, while in game-theoretic applications A may correspond to available strategies and is often smaller.
- 3When K > T we can’t expect low regret without additional assumptions, since the player won’t even get a chance to try all arms.


single action for all T periods of time, but “two-action” strategies that are allowed to e.g. take one action j1 during steps 1..T1 and then a different action j2 during steps T1 + 1..T. In many cases, such enhanced classes can be just thought of as enlarging the set A: in the example with two intervals, one can just think of regret with respect to all “two-action” strategies as competing with all strategies from A′ = [T] × A × A.

Other notions of regret are internal — in the sense that they depend on actions taken by the player. One such notion is swap regret (also known as internal regret). It is important due to its connections to correlated equilibria in game theory, as we will see later. In weak regret, the player contemplates having played the same action j at each round, and compares resulting loss with her realized loss. In swap regret, the player contemplates replacing each of her actions i ∈ A with a different action σ(i), where σ : A → A is an arbitrary function. Swap regret is thus deﬁned as:

Rswap(i) :=

T

t=1

ℓi

t,t − min

σ:A→A

T

ℓσ(i

t),t =

ℓi,t − min

j∈A

t=1

i∈A t:it=i

ℓj,t . (2)

t:it=i

Note that swap regret is larger than weak regret, since weak regret is captured by constant functions of the form σ(i) ≡ j. Even though it does not follow from general low-regret theorems that it is possible to attain low swap regret, there exists a black-box reduction from regret minimization to swap regret minimization [BM07]. A regret bound of O(K√T log K) can be attained [Sto05]. Note that regret again becomes o(T) for T polynomially large in K.

![image 6](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile6.png>)

Bandits with knapsacks. So far we have been dealing with scenarios where (for a sufﬁciently large T) regret per-step vanishes: total regret is o(T) (and also o(OPT) — even though we have not considered this dependence explicitly). Unfortunately, in some cases it is impossible to make decisions online in a way that would lead to vanishing regrets. Speciﬁcally, when decisions between rounds are linked.

One such generic setup is the bandits with knapsacks (BwK) model [BKS13b]. It represents a setting where the player is given limited amounts of some resources, which are consumed by arms. For our purposes it will sufﬁce to consider the scenario with one resource being consumed. Let us say that the player has a budget B. Since the game has to stop once the budget is exhausted, it is more natural to think of the arms as providing rewards ri,t instead of losses. At each step, after pulling an arm it, the player learns the attained reward ri

t,t, and the incurred cost ci

t,t. The game stops (and no further rewards are obtained) when either t = T or tτ=1 ci

τ,τ ≥ B — that is, the budget has been exhausted.

It is not hard to see why we can’t hope to get an o(OPT) regret bound against the best ﬁxed strategy in the bandits with knapsacks setting. Assuming that the budget (and not time) is the main constraint, we would like to maximize the reward-to-cost ratio ri

t,t/ci

t,t over time, weighed by ci

t,t. This is not a decision that can be made in an online fashion. Suppose that for t ∈ [1..T/2] arm 1 gives the player 1 unit of reward per unit of cost; then for t ∈ [T/2 + 1..T] arm 2 gives player R units of reward per unit of cost, where R = 0 with probability 1/2 and R = 2 with probability 1/2. No matter which mixed strategy player uses, her regret will be at least OPT/3 at least half of the time.

A related setting is the online knapsack problem where the costs are seen by the player before the arm is chosen, and where the player competes with the best sequence in hindsight [DJSW19, DH09, AD14]. Our setting is a hybrid of the online knapsack problem and the bandits with knapsacks problem: we only learn the cost after pulling an arm and are hoping to compete with the best sequence in hindsight. Throughout the paper, we will refer to our setting as the BwK setting, since the setup is the BwK setup, with the only difference being the more ambitious regret goal. While this goal appears hopeless in general, it is plausibly attainable in our application.

An important feature making our setting easier is that not knowing the target ratio between reward and cost is the only obstacle to attaining low-regret online algorithms for bandits with knapsacks. Moreover, while it may not be possible to prevent having regret, in hindsight the player is able to tell whether o(OPT) regret has been attained or not. This means that bandits with knapsacks have the potential to be used heuristically, where a good solution may not be guaranteed, but is self-certiﬁed once attained.

Summary and connections to learning and to games. Although the study of multi-arm bandit problems is still subject to very active research, it is fair to say that the problem is very well understood. Absent a simple information-theoretic obstacle (such as having to pull each arm at least once, or not having knowledge of future reward-to-cost ratios) there are algorithms attaining optimal or close-to-optimal regret bounds. In addition, these algorithms are efﬁcient in the number of arms K.

Most machine learning tasks can be cast as bandit problems, where “loss” is the gap between predicted label and ground truth. In fact, much progress on bandit problems originated from the machine learning theory literature. This link is not without limitations, however. When trying to learn a predictive model, the space of arms is typically exponential in the number of parameters. Thus algorithms with running time polynomial in the number of arms cannot be used without modiﬁcations. In addition, in many cases, such as neural-net models, practically attainable regret values are signiﬁcantly better than the ones guaranteed by generalization bounds.

The typical way in which machine learning algorithms convert a search problem with exponentially many model candidates into a tractable one is by turning it into an optimization problem. Typical bandit (and expert) algorithms have to maintain a vector of dimension K tracking the performance of each arm over time. When K is exponential, one cannot hope to do that, and has to settle for maintaining the “best arm so far”. Here, “best” is a combination of retrospective loss and simplicity (to avoid overﬁtting), and deﬁning what “best” means is an important art within machine learning practice. We will dive deeper into these questions in the next section.

### 1.2 Online algorithms and learning based on empirical regret minimization

In this section we will explore the connection between online algorithms and optimization. We frame the discussion in machine learning terms, but the same applies to any online algorithmic task.

Suppose we are trying to learn a model A ∈ A mapping inputs Xt to labels Yt. A na¨ıve “follow the leader” approach would be to always propose the best strategy in hindsight (known as “follow

the leader”):

t−1

At := arg min

A∈A

L(Xi, A(Xi), Yi). (3)

i=1

It turns out that this approach underperforms both in theory and in practice. Most importantly, (both in theory and in practice) is that using (3) will lead to overﬁtting: the model At will perform better than expected on the training samples {X1, . . ., Xt−1}, and worse than expected on the test sample Xt. A second problem is a computational one: assuming the model A is non-convex in its parameters, the function in the RHS of (3) is non-convex in the parameters of A. This makes At both computationally difﬁcult to ﬁnd, and potentially unstable in the inputs.

A generic solution to the overﬁtting problem is using a regularizer4 function Ψ(A), and choosing the strategy (known as “follow the regularized leader”):

At := arg min

A∈A

Ψ(A) +

t−1

L(Xi, A(Xi), Yi) . (4)

i=1

Using a regularizer leads to better performance guarantees. Intuitively, Ψ induces a metric on which models A are more likely to occur — typically “simpler” models according to some notion of simplicity5 — and prevents over-ﬁtting by penalizing large deviations to accommodate a small number of examples. In terms of optimization, if Ψ(A) is a nice (e.g. strongly convex) function, then one can hope that, at least locally around the previous optimum At−1 the function

Ft(A) := Ψ(A) +

t−1

L(Xi, A(Xi), Yi) = Ft−1(A) + L(Xt−1, A(Xt−1), Yt−1)

i=1

will appear convex. Then local gradient descent will allow us to get from At−1 to At. Note that the gradient of Ft at At−1 is given by

∇Ft(At−1) = ∇Ft−1(At−1)+∇L(Xt−1, At−1(Xt−1), Yt−1) = ∇L(Xt−1, At−1(Xt−1), Yt−1), (5)

since At−1 minimizes Ft−1(A), and thus its gradient is zero. Therefore, after seeing the pair (Xt−1, Yt−1), At−1 will need to move only in the direction reducing the loss of At−1 on Xt−1 — leading to signiﬁcant computational savings. This step is known as back-propagation in the neural networks training literature.

There are additional improvements that can be made to (5) to speed up convergence and improve generalization. The local geometry around At−1 may be transformed — to make the function Ft more isotropic (using adaptive learning rates) — so that gradient descent converges faster. In

![image 7](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile7.png>)

- 4Another solution — in line with expert algorithms discussed in the previous section — would be to maintain a number of models weighed according to their past performance, and to aggregate them together. This is generally computationally too cumbersome — instead of using d models of size S one can train a single model of size d · S, which will perform better. The regularizer in some sense serves as a proxy for maintaining many “good” models, and combining them to make the prediction.
- 5If one does Bayesian maximum likelihood estimation then Ψ(A) literally comes from a prior distribution of models.


addition, in the context of model training, where labeled data is usually scarce, multiple passes over the samples are used (so t pairs (Xi, Yi) may be sampled T ≫ t times with repetition). Given the practical importance (and the signiﬁcant investment) in developing and training machine learning models, there is a signiﬁcant body of applied and theoretical knowledge about each of the steps described here. It is not our goal to survey this knowledge. Rather, let us summarize some higherlevel points, which will guide us in suggesting meta-mechanisms based on online optimization algorithms of the form (4).

Upper bounds: proof-to-applications pipeline. In the context of optimization (linked to online algorithms or otherwise), there is a stark divide between the convex and the non-convex case. Generally speaking, convex optimization (where the loss function and the regularizer are convex functions and the domain of possible models A is an efﬁciently-speciﬁed convex set) is tractable. Oversimplifying decades of research, versions of gradient descent can be used to solve these problems efﬁciently. Many purely “combinatorial” problems such as maximum bipartite matching are in fact tractable because they are instances of linear programming (an important special case of convex programming).

In the context of learning and online algorithms, a promising approach has been to use the convex case to derive rigorous performance bounds, and then port them as heuristics into the more general non-convex model classes that one wants to train in practice. Thus the pipeline is (1) prove rigorous performance results about the convex case (e.g. in terms of accumulated loss, running time etc.); (2) use the same algorithms (or their natural extensions) in the more general setting. While (1) is a mathematically robust exercise, (2) is a matter of accumulated wisdom about what kind of things are likely to port into the non-convex domain. A necessary (but not sufﬁcient) condition for (2) to work is that the optimization procedures suggested in (1) tend to be local and continuous: local updates based on local quantities such as gradients and Hessians.

Lower bounds are overly pessimistic. In many cases, a procedure suggested by (2) will at least lead to some kind of a local optimum — one cannot hope to do much better provably, because global optimization of non-convex functions is almost always NP-hard — a fact that does not appear to be the main bottleneck in achieving performance (as will be discussed later, approximation and generalization errors seem to play a more dominant role).

More importantly, in many cases, the resulting models signiﬁcantly outperform generalization bounds. While the exact theoretical mechanisms explaining this are subject of active research, this is a phenomenon that mechanisms built on top of such algorithms should be prepared to take into account.

Approximation and generalization error: bound to be an art. In general, an online algorithm (or equivalently a learning algorithm) that takes actions based on a model it trains suffers from three sources of loss: (A) approximation error: how close is the best model A in the class A is to the truly best model? (B) optimization error: in the language of (4), how close is A˜t obtained by the algorithm to minimizing the expression in (4)? (C) generalization error: how close is the optimizer of (4) to producing the smallest possible regret?

Except when A is the set of all possible functions, designing the class A to attain a small approximation error is an important application-speciﬁc task, an in many cases it is more of an art than an exact science. This is especially true since the choice of A affects other sources of loss.

Classical learning theory, such as PAC-learning and multi-arm bandit theory, allow one to give rigorous bounds on the generalization error based on optimization error. Roughly speaking, if a model performs well on a randomly selected training set, and it does not have enough parameters to be able to overﬁt to the training data, then its performance on Xt must be in line with its performance on X1..t−1. Observed performance in training neural nets often signiﬁcantly exceeds these guarantees — generalization error is typically estimated empirically by examining the model’s performance on a holdout set. Being in a regime where a low generalization error is an empirical fact and not mathematically guaranteed means that the optimization heuristic may affect generalization performance — an optimization heuristic attaining the lowest optimization error may underperform a heuristic attaining a higher optimization error, but a lower generalization error.

Summary. The main upshot of the discussion so far is that some of the more important modern algorithms are a result of domain-speciﬁc experience and are not easily replaced with a functionally equivalent algorithm based on the problem the algorithm is trying to solve. This is in contrast to classical discrete algorithms for problems such as maximum matching or network ﬂow, where all correct algorithms will output the same (correct) answer.

Our goal is to develop new reductions from algorithms to mechanisms, and in this context this means that the reduction should happen at the level of the algorithm and not at the level of the problem that the algorithm is trying to solve. In other words, given a heuristic H for a problem P, the mechanism should assume that it won’t be able to attain a comparable performance on P without using H (or a version of it) as a sub-routine. This is a departure from most existing algorithmic mechanism design literature, which we feel is necessary in order to keep up with advances in applied algorithms.

A very important special case is when H is just a local optimization (such as stochastic gradient descent) aimed at minimizing an expression of the form (4). In this case, the algorithmically difﬁcult part is devising the class of models A and the regularizing function Ψ, and we would like to develop generic mechanisms that make use of these while having good game-theoretic properties.

### 1.3 Games, online algorithms, and equilibria

So far, we have seen that even “one shot” optimization, such as ﬁnding the best classiﬁcation model given labeled data can be naturally cast as an online algorithms problem. Next we will see that the same is true about game theory, making online optimization a natural language to connect the two.

When an algorithm is turned into a mechanism (by allowing inputs to come from self-interested participants), it induces a strategic game among the participants (in which the mechanism — or the “principal” is sometimes a party as well). The basic question facing the mechanism designer is “what outcome will this game lead to?”. One notion of a plausible strategic outcome is that of an equilibrium: a steady state in which no player beneﬁts from deviating from their current

strategy. Of particular importance for mechanism design are mechanisms that ask participants for their inputs (“direct revelation mechanisms”), and where in the induced game reporting inputs truthfully is an equilibrium6.

Unlike being “optimal” in the combinatorial sense (a solution’s objective value is close to the best objective value attainable), a “good” or “optimal” equilibrium is very much a function of the mechanism implementation details. This leads to signiﬁcant complications, both in theory and in practice, since whether a good equilibrium can be sustained is a function of participants’ behaviors in practice (or modeling assumptions in theory). A signiﬁcant portion of games, both in theory and in practice, have multiple equilibria, and it is often impossible to rule out “bad” equilibria. Moreover, in some cases there are lower bounds known as “the price of anarchy” showing that all equilibria attain a substantially lower objective function value than the combinatorially optimal outcome.

Despite these challenges, equilibria become signiﬁcantly nicer objects to deal with once they are presented in the language of online regret minimization (corresponding to correlated equilibria). In addition, at least when money can be used arbitrarily, the Vickrey–Clarke–Groves (VCG) mechanism attains combinatorially optimal performance, while incentivizing participants to report their types truthfully. As we will see, VCG is not a “cure-all” mechanism since suffers from several important shortcomings that make it more appealing in theory than in practice. One of our goals is to mitigate some of the shortcomings while preserving its desirable properties in a generic way.

Nash equilibria. To keep the exposition simple, consider a basic two-player strategic game, where row player Row and column player Col each pick actions i and j, respectively, from a set of n available actions. On actions (i, j) the payoff or Row is given by the matrix Rij, and the payoff of Col is given by Cij. A Nash equilibrium (p, q) is a distribution of actions by the two players such that no player beneﬁts from deviating. For Row, it means that no action in the support of p is strictly dominated by another action Row may take. Let Ui := j qjRij be Row’s expected payoff under action i. Then the equilibrium condition can be written as:

whenever pi > 0 ⇒ for any alternative action i′ Ui′ ≤ Ui (6)

It should be noted that while Nash equilibria are perhaps the best-known notions of equilibria, they are arguably not the best-suited in the context of algorithmic mechanism design. To argue that action distributions (p, q) are a plausible answer to the question “What will Row and Col do?”, one needs to assume that e.g. Row is perfectly informed about the distribution q so that the nonzero-probability actions i with pi > 0 make sense under (6). If Row is misinformed about q, the equilibrium may fail to materialize. This is especially true in a game induced by a mechanism with

![image 8](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile8.png>)

6The reason for focusing on direct-revelation mechanisms is something called the “revelation principle”. The revelation principle asserts that any mechanism can be converted into a truthful direct revelation mechanism by appointing a perfectly informed advocate for each player as part of the mechanism. A player then reveals her type (truthfully) to the advocate, who uses this knowledge to interact with the mechanism in a way that maximizes player’s happiness. The extent to which this reduction is realistic or practical is a very important question whose answer depends on the setting. Regardless, it is clear that truthful direct revelation mechanisms are the most natural extension of algorithms to which one should aspire.

many participants. A more robust notion of an equilibrium would be based on participants making decisions regardless of their beliefs about others’ actions.

Dominant strategy equilibria. In a dominant strategy equilibrium, no player takes an action that is dominated by another action for some realization by the other players. In the two-player example, Row would not take an action that is dominated by another action for some action j of Col:

whenever pi > 0 ⇒ for any alternative action i′ and for any j Ri′j ≤ Rij (7) Condition (7) is clearly much stronger than (6). In particular, whenever it holds, it is easier to believe that the outcome (p, q) will be realized. This is especially true when p and q are just single actions, i.e. pi = 1, qj = 1 for some (i, j).

Unfortunately, it is easy to see that dominant strategy equilibria do not always exist — for example there is no “best” strategy in the Rock-Paper-Scissors game (or any zero-sum game for that matter). On the other hand, Nash’s celebrated theorem guarantees the existence of a Nash equilibrium in any game. In mechanism design we typically have some degree of control over the game, and can aspire for an equilibrium where truthful reporting of one’s type is, in fact, a dominant strategy. This is often impossible to attain, a slightly less ambitious goal is for truthful reporting to be an approximately dominant strategy.

Approximate equilibria. For any notion of an equilibrium such as above, there is an associated notion of an approximate or an ε-equilibrium. The approximation here refers to the beneﬁt a player can derive by deviating from her current action proﬁle. Assuming a player’s utilities for outcomes are in a bounded interval [0, C], a set of actions is an ε-equilibrium if no player can improve her utility by more than ε · C by deviating. Thus, assuming Rij ∈ [0, 1], (6) becomes the condition

whenever pi > 0 ⇒ for any alternative action i′ Ui′ ≤ Ui + ε (8) for being an ε-Nash equilibrium, and (7) becomes the condition

whenever pi > 0 ⇒ for any alternative action i′ and for any j Ri′j ≤ Rij + ε (9) for being ε-dominant strategy equilibrium.

We note that while ε-approximate equilibria are easier to ﬁnd and attain7, a ε-dominant-strategy equilibrium may still not exist. An important advantage of ε-approximate equilibria is that they can be tied into online learning and regret bounds.

Learning, regret minimization, and correlated equilibria. Suppose a strategic game or mechanism were presented to someone with no prior knowledge of game theory, with the question of ‘what will happen?’. A reasonable approach would be to run simulations with participants trying to “learn to play” the game to the best of their ability, and to see what happens.

![image 9](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile9.png>)

7For example, while ﬁnding a Nash equilibrium, even for a two-player game, is PPAD-complete [DGP09, CD06], and ﬁnding a good-value Nash equilibrium is NP-complete [CS08], both problems can be solved in quasi-polynomial time nO(logn) in the ε-approximate setting [LMM03].

As deﬁned, the game is played only once, and “learning” as such doesn’t make sense. A reasonable solution is to let the players play the game T ≫ 1 times in a row, and observe the distribution to which their actions converge. If a player ignores the effect her play may have one future plays by other players8, then the problem she is facing is exactly the online learning problem we discussed earlier.

Considering the two-player setting for simplicity, and taking Row’s viewpoint, at each round t = 1..T, if Col plays jt, Row faces payoff Rij

for action i at step t. Row will be solving the online learning problem with the goal of maximizing payoff Tt=1 Ri

t

tjt. Col will be solving a similar problem. At a minimum, Row and Col should be running a low-regret learning algorithm, although we should note that any family of online learning algorithms would lead to an outcome with potentially interesting properties.

Running two online learning algorithms will unfortunately not lead to a Nash equilibrium. Still, the outcome of such a process has an important interpretation: it leads to something called a coarse correlated equilibrium. Moreover, if the players run a low swap regret online learning algorithm (of the kind discussed in Section 1.1), then the resulting outcome is an ε-correlated equilibrium. Here ε → 0 as T grows. When T → ∞ we obtain a correlated equilibrium.

A correlated equilibrium is an equilibrium where a suggested action is presented to each player. The players are free to not follow the suggested action, and instead choose a different action (which may depend on the suggested action). The suggested actions form a correlated equilibrium if no player gains by deviating from the proposed actions. Formally, in the two-player case, the correlated equilibrium is a distribution µ on pairs of strategies (i, j), such that no player beneﬁts from not following the suggested play. For Row, this condition becomes:

for all i and potential substitutes i′,

j

(µ(i, j) · Rij) ≥

j

(µ(i, j) · Ri′j) (10)

A canonical example of a correlated equilibrium is one induced by a trafﬁc light, where it is a dominant strategy for each driver to stop on red, expecting crossing trafﬁc to not stop on green.

Competitive equilibria and markets. More pertinently for mechanism design, a market that sets prices is also a form of a correlated equilibrium. Market-based solution concepts for reallocation of goods, such as Fisher and Arrow-Debreu markets, are based on a concept of a competitive equilibrium, which is a natural type of a correlated equilibrium.

For example, in the case of a Fisher market, each player is given an endowment, and wishes to spend it on a bundle of (divisible) goods. A solution to the Fisher market problem produces a vector of prices p  for the goods. Each player then spends her endowment to buy her favorite bundle at the given prices. The prices “clear” the market if all players spend their budget, and all goods are sold. Given the prices p , each player gets her favorite bundle at these prices, and therefore truthful reporting of valuations over goods is a dominant strategy, and we obtain a correlated equilibrium where truthful reporting is a dominant strategy.

![image 10](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile10.png>)

8This is a very important simplifying assumption — repeated games where stages are linked are often much more complicated than the base game.

Note that this sidesteps the question of how prices p  are obtained, and indeed, solutions to Fisher markets do not yield a truthful mechanism if one considers the effect players’ reports have on prices. This parallels a broader points about market-based mechanisms: if one treats market prices as ﬁxed, then interaction with the market is typically truthful. However, when a player considers her impact on market prices, most market mechanisms are not truthful (for example, one can try to feign reduced interest in an item to get its price to drop). This concern is very real (and leads to reduced overall welfare) when there are few players in the market. When the market is large — and the impact of each individual player on the market is small, one can hope that the resulting mechanism will be approximately truthful even when one accounts for a player’s impact on prices: the impact on the prices (and thus the potential beneﬁt) of misreporting preferences is small, and the effect of misreporting on the bundle one gets is always non-positive.

The upshot of the discussion above is that in market-based solution concepts, a competitive equilibrium is a type of a correlated equilibrium where reporting preferences truthfully is a dominant strategy — as long as we manage to sidestep the issues of how prices are arrived yet. Taking a cue from the Nash equilibria → correlated equilibria simpliﬁcation, a natural source of these prices is through repeated play. Note that this is how prices in ‘real’ large markets are discovered: participants repeatedly interact with the market, with supply and demand serving as signals that update market prices. This process has similarities to taˆtonnement in equilibria theory, except we will consider the time-average of the outcomes at all steps, and not just a “limit” outcome — giving our model more ﬂexibility.

Prices and outcomes through repeated play. The discussion above gives us a blueprint for producing an equilibrium outcome using individual preferences and an aggregation heuristic. We will formalize parts of it as the APEX algorithm in Section 2.1 below. It consists of the following components:

- 1. A repeated game where at step t each player i submits its preferences function fti to a central principal;
- 2. at each step t the principal runs a heuristic to produce an outcome ot;
- 3. at each step t the principal calculates prices to be charged to participants (since we’re dealing with a mechanism without money, prices are charged in tokens);
- 4. participants are not allowed to exceed their token budget;
- 5. in each step t the principal also outputs prices which allow each player i to estimate the price and outcome oit(f˜ti) under reported preferences f˜ti instead of fti;
- 6. the outcome of the mechanism is the time-average o¯ := T1 Tt=1 ot;

![image 11](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile11.png>)

- 7. each player runs an online learning strategy with the goal of maximizing its utility; here we make a distinction between an “equilibrium” and a “competitive equilibrium” notion of


maximizing utility9.

Players in the mechanism above will run a bandits with knapsacks online algorithm. If incentives are correctly aligned, in each step, players will report their types truthfully up to a constant scaling factor10. Thus if the normalized preferences function of player i at time t is fˆti, the player will report fti = λit · fˆti, where λit ≥ 0 are chosen to that the reward per marginal token spent is equalized across rounds.

There are important details to be ﬁlled in the above blueprint, primarily around the principal’s heuristic and the prices it would induce. In the spirit of the discussion about algorithms and optimization, we will not want to limit the scope of possible heuristics, except we would expect the outcome ot to try and maximize i fti(ot), possibly with a regularization term. In practice this might mean either computing ot from scratch or computing it from ot−1 via some kind of gradient update.

The previous part of the description is necessarily vague, since it needs to accommodate various

types of optimization algorithms and heuristics. Assuming the algorithm for converting the fti’s into an outcome ot is a good one, we still need to take care of incentivizing players to report their preferences fti truthfully.

There is a generic tool in mechanism design, called the Vickrey–Clarke–Groves (VCG) mechanism under which truthful reporting is a dominant strategy. While theoretically the VCG mechanism is very appealing, it has some signiﬁcant practical drawbacks that stand in the way of it being adopted. We will argue that in our case most of these drawbacks either don’t occur11, or would occur to the same extent under other mechanisms.

The ﬁnal piece of our mechanism will be using a local version of VCG to set prices accruing to the players. Before putting all the pieces together more formally, let us brieﬂy discuss the VCG mechanism, and some challenges in using it in practice.

### 1.4 Mechanism design: the VCG mechanism and its shortcomings

The VCG mechanism is a mechanism with money — meaning that there is a way for participants to store residual utility after the mechanism completes. In this paper we are dealing with mechanisms without money, but since the mechanism is multi-round, tokens serve the role of money, allowing us to use VCG locally.

The mechanism. Suppose there is an outcome space O, and n players. Player i has utility ui(o) ≥ 0 for an outcome o ∈ O. Since we are dealing with a mechanism with money, we can assume that ui is in currency units. The mechanism will choose an outcome maximizing total

![image 12](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile12.png>)

- 9In the competitive equilibrium approach, each player ignores her effect on future plays by other participants of the mechanism, treating the other players and a principal as “nature” in the sense of online algorithms.
- 10Such factors are unavoidable in mechanisms without money: a player with utility function ui should be treated the same a player with utility function 2 · ui, since there is no functional means of distinguishing the two.
- 11For example, because we are consideringmechanisms withoutmoney, and thus do not need to be “budget-neutral”.


utility:

oVCG := arg max

o∈O

ui(o). (11)

i∈[n]

Each player is then charged pi — the calculated externality she imposes on other players: pi(oVCG) := max

uj(o) −

uj(oVCG). (12)

o∈O

j∈[n]; j =i

j∈[n]; j =i

In other words, pi is the extra utility other players could have attained if they didn’t need to take i’s preferences into account. Note that the realized utility for player i from outcome o′ is given by

ui(o′) − pi(o′) = ui(o′) +

uj(o′) − max

o∈O

j∈[n]; j =i

j∈[n]; j =i

uj(o) =

uj(o′) − max

uj(o).

o∈O

j∈[n]

j∈[n]; j =i

The second term does not depend on ui, and the ﬁrst term is maximized when o′ = oVCG, which is obtained when player i reports her type truthfully. Therefore VCG is dominant-strategy truthful. An example of a problem VCG “solves” in principle is that of combinatorial auctions: optimally selling goods to players who may have arbitrary preferences over bundles of goods. It should be noted that in the case where the goal of the mechanism is to sell a single item (that is, O = [n] determines which player gets the item, and ui(o) := 1o=i · ui), VCG turns into the second-price auction.

There is a number of important practical reasons why VCG in its pure form has remained primarily a theoretical tool. An analysis of some of the more important issues can be found in [AM+06, Rot07]. We will have to keep these issues in mind when we integrate a version of the VCG mechanism into our reduction. For our purposes, the issues can be broken down into several categories. We present these in order of relevance, from the least to the most relevant.

Revenue sub-optimality; budget non-neutrality. One of the main reasons VCG is not used in actual auctions is that while it maximizes participants’ welfare, it does not generally maximize the principal’s revenue. In fact, in some cases, such as unit-demand auctions, it is the mechanism minimizing the amount of revenue raised. In part, the fact that VCG is maximally efﬁcient already suggests that it won’t be revenue-maximizing: in practice, the way to fetch a higher price for a good is to be willing to set a reservation price, and not sell it for a lower price even if withholding it is inefﬁcient. A related problem is that VCG is not “budget neutral” — even when the goal of the mechanism is to facilitate a transaction between two players, the mechanism might prescribe payments to/from players that do not add up to 0, requiring an outside subsidy for the mechanism to run.

Neither of these are a problem for us, since we will be using VCG in the context of a mechanism without money, with players endowed with tokens. The objective is to maximize aggregate utility subject to some notion of fairness (such as players starting with an equal token endowment).

Computational difﬁculty of bidding; optimization and numerical instability of payments and utility. The second set of problems for using VCG in practice is computational. For an individual

player, ﬁguring out the function ui and communicating it to the mechanism may be prohibitively expensive. In addition, solving the optimization problem (11) precisely is often NP-hard.

More importantly, even if (11) can be solved heuristically to a high degree of precision, the effect of the approximation error on price calculations in (12) may be prohibitive, since it involves a difference between two approximate quantities. To illustrate, if there are n = 1,000 participants in an auction involving $5,000,000 worth of goods, then getting the optimal allocation of goods to within 1% (or $50,000) is acceptable, but calculating prices charged to individual players to within an additive $50,000 (where the average purchase is only worth $5,000) is unacceptable.

In our setting, even when the space O is quite complicated, we will only need gradient access to the function ui, so the bidding complexity will not be a problem. The optimization gap is a real concern. Depending on the setting, the optimization problem may be solvable exactly, in which case it is not an issue. If the optimization is being done by a heuristic, we will rely on the fact that at each step of the optimization ot is only adjusted locally, and even very complicated functions can be simpliﬁed locally (e.g. by taking a quadratic approximation), allowing us to compute local prices with an acceptable precision. One tool at our disposal is regularization, which at every step will turn the optimization problem into a locally convex one.

Issues with chaining several VCGs one after another. A signiﬁcant issue for the truthfulness of the VCG mechanism, happens if multiple instances of the mechanism are chained one after another with players given a ﬁxed total budget for all rounds. It might be beneﬁcial for a player to withhold bids in one round, and use tokens saved to bid in later rounds. Generally speaking, in situations where utilities are concave, and player i is bidding λifˆi, increasing λi will result in a lower marginal utility per token. Therefore, assuming the algorithm converges, we can expect that in a typical round the marginal utility of player i per token is about the same. However, the exact conditions for convergence will likely require further investigation and analysis.

Susceptibility to various forms of cheating and collusion. While VCG is immune to manipulation via misreported preferences, it is extremely susceptible to other forms of manipulation. Considering the simple second-price auction scenario, the mechanism is susceptible to shill bidding (a player colludes with the principal to extract more than the second price from the winner) and non-winning players being bribed to drop out (to reduce the price the winner has to pay). More sophisticated scenarios are also susceptible to a single player bidding under multiple identities.

Some of these problems disappear in a mechanism without money. For example, in voting it is clear that a single player can beneﬁt by “voting under multiple identities”, and preventing this from happening falls outside of the voting mechanism. In other cases, collusion between players is inevitable, and cannot be prevented by the mechanism. In case of voting, even an approximately truthful voting mechanism will be susceptible to voters forming a party and then voting as a block in favor of issues they all agree on, while avoiding canceling each other on issues they disagree on.

In summary, unlike computational issues which we can hope to do away with, some of the issues around collusion are real, and will not disappear. We do not expect that using VCG will exacerbate these issues compared to other mechanisms, but this will need to be investigated further.

### 1.5 New results on one-sided allocation

One area where we have obtained new theoretical results using the APEX framework is one-sided allocation. The results are presented in detail in Section 3.2, we summarize them brieﬂy here. We should emphasize that we didn’t set out to obtain these results, and that they followed naturally by applying the framework to the one-sided matching setting.

In the simplest one-sided allocation setting there are n players and n items. Player i has utility uij ∈ [0, 1] for item j. A general solution is a bi-stochastic matrix {Xij}, where player i gets item j with probability Xij. The utility of player i under such allocation is just her expected utility

ui(X) =

j

uij · Xij.

A classical result of Hylland and Zeckhauser [HZ79] says that there is always a competitive equilibrium from equal endowments (CEEI) solution to the one-sided allocation problem. Informally, it means that if we give each player one unit of tokens, there is an allocation Xij and prices Pj ≥ 0 (in tokens) on items such X is a competitive equilibrium supported by prices Pj: the bundle Xi costs at most one token, and is utility-maximizing for player i among all cost-≤ 1 bundles of total probability 1.

Note that the HZ competitive equilibrium has nice properties such as Pareto-efﬁciency and envy-freeness. On the other hand, there could be multiple HZ-equilibria (existence proof uses Kakutani’s ﬁxed-point theorem). We obtain the following reﬁnement of the HZ-equilibrium existence:

Theorem 5. [restated] For any uij, there exist scaling factors λi ≥ 0 and an allocation X such that X is a result of running VCG on utilities λiuij. The resulting VCG prices Cj support X as a HZ-equilibrium. In the resulting VCG payments supporting X, all players either get their favorite item or pay exactly 1 unit for their bundle.

Thus, there is always a HZ equilibrium supported by VCG prices applied to players’ scaled utilities. It turns out that equilibria from Theorem 5 form a proper subset of all HZ equilibria there exist HZ equilibria that are not supported by VCG prices.

In addition to the existence result, in Theorem 13 we show that there is a natural online optimization dynamics on our general mechanism, such that whenever that dynamics converges it leads to a HZ equilibrium of the form guaranteed by Theorem 5. This gives a new attack route for both provable and heuristic approaches to calculating HZ equilibria.

### 1.6 Related works Note. This section will be updated as I collect more relevant works across the different domains.

The main thrust of the paper is to build a new three-way connection between optimization, online learning, and mechanism design without money — particularly the VCG mechanism. Each of these topics forms a subject of a major discipline in Applied Mathematics and Economics. Each pair of these topics is also the subject of a signiﬁcant body of work (at a level where textbooks or

whole conferences dedicated to the subject exist). We will very brieﬂy survey those here, before mentioning some more directly relevant works.

Online learning and optimization. The connection between online learning and optimization is well-established. In the convex setting, the textbook [Haz19] provides a recent treatment of the subject.

Optimization and mechanism design is the subject of much of modern Algorithmic Game Theory (AGT) [NRTV07, Rou16]. The effort to convert good algorithms (typically optimizing an objective) into a good mechanism is at the core of AGT. Our work is also part of this effort, with the added twist of viewing the optimization component of the algorithm as an iterative process similar to online optimization.

Online learning and mechanism design is perhaps the least developed of the three connections. Within classical game theory, it has been known that correlated equilibria correspond to online learning dynamics. More recently, the subject of learning in repeated games has received renewed interest due to its practical importance in areas such as online ad auctions. Recent references include Chapter 11 in [Sli19], as well as articles such as [BMSW19, FPX20, DSS19].

Speciﬁc related recent works. Below we brieﬂy discuss recent papers that are most closely related to the present one.

In [KGJS20] a framework for online learning with incentives is developed in the context of mechanism design with money. Participants learn their value for the different options as the algorithm progresses. The construction uses a combination of online learning techniques and the VCG mechanism to achieve both low regret and good incentive properties.

[IPW19] develops a framework for joint decision making in a metric space with quadratic utilities. The primary goal of the work is actually to obtain a decision-making algorithm that complies with the normative requirement of “equalizing inﬂuence among participants”. The resulting outcome notion is in fact very similar to the notion of a competitive equilibrium from equal budgets in the present paper.

## 2 Pseudo-market mechanisms

With the components in place we are ready to start putting together generic mechanisms based on online optimization and other algorithmic heuristics.

### 2.1 Setup and the generic APEX mechanism

- 2.1.1 The mechanism


We begin by stating a very general reduction from optimization heuristics to algorithms. We will then instantiate it in ways that seem to be most immediately useful.

Our starting point is an online learning heuristic H. The heuristic takes a sequence of objective functions {Fs(x)}ts=1, and starting point xt. It then generates a function Ψt+1 = Ψt+1(F1, . . ., Ft, xt), and outputs a value xt+1 that maximizes the function Ψt+1(x). Typically, Ψt+1 will either be a concave function, or contain a regularization term that drops off sharply away from xt, thus making computing xt+1 from xt easy.

We will particularly focus on the effect Ft has on xt+1. Regularization, along with the fact that Ft is only one of the functions feeding into Ψt+1 means that we may expect the dependence of xt+1 on Ft to be smooth even if the overall landscape of Ψt+1 is very complicated. For an alternative objective function F˜t we can deﬁne

Ψ˜t+1 := Ψt+1(F1, . . ., F˜t, xt),

and let be x˜t+1 the outcome of maximizing Ψ˜t+1(x) over x. For illustration purposes, one property we expect H to satisfy is monotonicity, which can be viewed as a local relaxation of ﬁnding an actual maximizer:

Deﬁnition 1. Heuristic H is said to have the monotonicity property if for all F1, . . ., Ft, F˜t, and xt, the following holds:

Ft(xt+1) − Ft(˜xt+1) ≥ F˜t(xt+1) − F˜t(˜xt+1). (13) In other words, moving from F˜t to Ft results in a shift more beneﬁcial to Ft than to F˜t.

Example. Suppose that in a heuristic H, Ψt+1 takes the form Ψt+1(x) = G(x) + Ft(x), where G(x) is a function that depends on previous F’s and potentially on a regularizer12. Then by optimality of xt+1 we have Ψt+1(xt+1) ≥ Ψt+1(˜xt+1), and thus Ft(xt+1) + G(xt+1) ≥ Ft(˜xt+1) + G(˜xt+1). Similarly, F˜t(xt+1) + G(xt+1) ≤ F˜t(˜xt+1) + G(˜xt+1). Thus, in this case, we get

Ft(xt+1) − Ft(˜xt+1) ≥ G(˜xt+1) − G(xt+1) ≥ F˜t(xt+1) − F˜t(˜xt+1), and the monotonicity property holds.

The APEX algorithm will use heuristic H iteratively to ﬁnd a solution sequence X0, . . ., XT. The algorithm lets participants specify their objective fi (which remains ﬁxed throughout the execution), and the intensity λi,t of their preferences (which gets adjusted throughout the execution). The players get charged in tokens. Prices are calculated to be VCG prices. We will see in Lemma 4 that the dominant-strategy truthfulness of VCG implies that a low-regret execution of the APEX algorithm leads to a competitive equilibrium where truthful reporting of fi is an approximately dominant strategy for Player i.

Players’ actions. For now, we do not specify the algorithm the players will use to solve the Bandits with Knapsacks (BwK) set up by the main mechanism. BwK is a much more difﬁcult problem than the “usual” Bandits. Unlike the Bandits setting, a general o(1) regret algorithm does not exist.

![image 13](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile13.png>)

12Follow the leader, and follow the regularized leader algorithms have this format.

![image 14](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile14.png>)

Algorithm 1 APEX (f0, f1, . . ., fn, H) algorithm given utilities fi : X → R by the participants, principal’s utility f0 : X → R, local optimization heuristic H Main mechanism:

![image 15](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile15.png>)

- 1: Fix starting point X0 ∈ X;
- 2: for t = 0..T − 1 do
- 3: Collect bids λi,t ≥ 0 from Player i;
- 4: Selects a regularizer Rt(x) that may depend on t, X0, . . ., Xt;
- 5: Set Ft(x) := f0(x) + j=1..n λj,tfj(x) + Rt(x);
- 6: Let Xt+1 be obtained by H by maximizing Ft(x) starting at Xt;
- 7: for each Player i = 1..n do
- 8: Set Ft−i(x) := f0(x) + j=1..n,j =i λj,tfj(x) + Rt(x)
- 9: Let Xt−+1i be obtained by H by maximizing Ft−i(x) starting at Xt;
- 10: Charge Player i, Ci,t := Ft−i(Xt−+1i ) − Ft−i(Xt+1) tokens;
- 11: end for
- 12: end for Suggested algorithm for Player i:


- 1: Report utility fi : X → R to the mechanism;
- 2: Run a Bandit with Knapsacks online algorithm with initial budget Bi to determine the {λi,t}Tt=1;


![image 16](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile16.png>)

At the same time, it is not difﬁcult to come up with a reasonable heuristic for the BwK problem. The algorithm will try to learn the best marginal “bang-per-buck” ratio it can expect, and play accordingly. Fix a round t and the bids of all other players. Then each value of the bid λi induces a utility ui,t(λi) and a cost Ci,t(λi). Under very mild local optimality conditions, ui,t and Ci,t are monotonically non-decreasing in λi.

A ratio r can be thought of as the exchange rate Player i is willing to pay in tokens per additional

unit of utility13. Let Λ be a distribution of strategy sequences {λ′i,t} that is feasible in expectation, that is:

T

Ci,t(λ′i,t) ≤ Bi, (14)

E

{λ′i,t}∼Λ

t=1

T

t=1 ui,t(λ′i,t) .

maximizing the payoff E{λ′i,t}∼Λ

If the inequality in (14) is strict, that is, Λ does not spend its entire budget, then the budget constraint is irrelevant, and player i can attain maximal utility by bidding the same high value of λi at every round. Otherwise, the budget Bi is a real constraint on player i’s attainable utility. For simplicity, let us assume that Ci,t(λi) is a continuous function14. Since Ci,t are monotonically

![image 17](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile17.png>)

13The discussion that follows can be easily restated in the language of constrained optimization. Given the objective

of maximizing t ui,t(λi) subject to t Ci,t(λi) ≤ Bi. We can take a Lagrangian of the budget constraint with coefﬁcient r to get an upper bound on the possible utility. Under strong duality, we can attain the value OPT using this

r. To keep the presentation more broadly accessible, we do the relevant calculations directly in this section. 14Otherwise, the same analysis still works, but we need to replace λi with a distribution on a small interval (λi −

non-decreasing in λi, there is a value λimax such that

T

Ci,t(λimax) = Bi.

t=1

Deﬁne

1 λimax

rmin :=

.

![image 18](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile18.png>)

Claim 2. Assuming local optimality of heuristic H, for each t and for each λ′i, we have ui,t(λ′i) − rmin · Ci,t(λ′i) ≤ ui,t(λimax) − rmin · Ci,t(λimax).

Proof. Let Xmax be the solution H gives when we optimize Ft−i(x) + λimax · fi(x), and X′ be the solution H gives when we optimize Ft−i(x) + λ′i · fi(x), and X′. We have

Ci,t(λ′i) − Ci,t(λimax) = −Ft−i(X′) + Ft−i(Xmax), since the Ft−i(Xt−+1i ) term cancels out. Therefore,

ui,t(λimax) − rmin · Ci,t(λimax) = rmin · (λimax · ui,t(λimax) − Ci,t(λimax))

= rmin · (λimax · fi(Xmax) − Ci,t(λ′i) + Ft−i(Xmax) − Ft−i(X′)) ≥ rmin · (λimax · fi(X′) − Ci,t(λ′i) + Ft−i(X′) − Ft−i(X′))

= ui,t(λ′i) − rmin · Ci,t(λ′i), where the inequality follows from Xmax being a local optimizer for Ft−i(x) + λimax · fi(x).

![image 19](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile19.png>)

![image 20](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile20.png>)

![image 21](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile21.png>)

![image 22](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile22.png>)

Claim 2 implies that the simple strategy of playing λimax in every round matches or exceeds the performance of the optimal distributional strategy Λ:

E

{λ′i,t}∼Λ

T

T

ui,t(λ′i,t) = E

ui,t(λ′i,t) − rmin · Ci,t(λ′i,t) + rmin ·

{λ′i,t}∼Λ

t=1

t=1

T

T

ui,t(λimax) − rmin · Ci,t(λimax) + rmin · Bi =

t=1

t=1

T

Ci,t(λ′i,t) ≤

t=1

ui,t(λimax). (15)

Here, the ﬁrst part of the inequality is by Claim 2, and the second half is by the feasibility of λ′i,t.

Observe that the guarantee of (15) is a very powerful one: it doesn’t just compete with the performance of the best ﬁxed λi in hindsight, but with respect to the best sequence of λi,t’s. One catch here (as in any discussion of competitive equilibria) is that we assume that the actions of other players are ﬁxed and are not affected by the λi,t’s. This is acceptable given that our goal is indeed to obtain a competitive equilibrium.

![image 23](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile23.png>)

δ,λi + δ) to make the expected Ci,t continuous in λi. This is essentially what happens in the proof of Theorem 5 later in the paper.

- 2.1.2 Reading the output of the APEX mechanism

Given an execution trace of Algorithm 1, there is a natural way to “read off” the outcome and prices of the algorithm.

Outcome. The (distributional) outcome is obtained by taking the time-average of the Xt’s:

X¯ := U({X1, . . ., XT}). (16) Note that here X¯ is a uniform random variable15, taking each of the T values with probability T1 .

![image 24](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile24.png>)

Prices. To obtain a competitive equilibrium, we expose Player i to a menu of possibilities. The menu will be based on the execution of Algorithm 1, and will be separable by round. In other words, the player will essentially be exposed to T independent menus — linked by a common budget, and by a common utility function f˜i. At round t, given a utility function f˜i and a bid λ˜i,t the algorithm deﬁnes

F˜t(x) := Ft−i + λ˜i,tf˜i(x)., which leads to the outcome X˜t+1 is obtained by maximizing F˜t starting at Xt using H. We use the values of Ft−i and Xt−+1i from the original execution of the algorithm. Player i is then charged

C˜i,t(f˜i, λ˜i,t) := Ft−i(Xt−+1i ) − Ft−i(X˜t+1).

Player i bids a utility function f˜i and {λ˜i,t}t=0..T−1. The sequence is required to be feasible, that is,

T−1

t=0

C˜i,t(f˜i, λ˜i,t) ≤ Bi. If the sequence is feasible, then the outcome is just the uniform distribution X¯ i := U({X˜1, . . ., X˜T}).

Note that the sequence of bids with the truthful fi, f˜i = fi and {λi,t}t=0..T−1 is feasible and leads to outcome X¯ .

- 2.1.3 From low-regret to an approximate correlated equilibrium.


As expected, our aim will be to link low-regret properties of the players’ interaction with the algorithm to show that the outcome of the algorithm is a competitive equilibrium.

Deﬁnition 3. Consider a bandits-with-knapsacks game with a budget B, where the payoff of actions is in [0, M]. At each step an action at leads to utility ut(at) and to cost ct(at). Let a =

![image 25](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile25.png>)

15When the Xt’s are probability distributions themselves, this amounts to averaging them. In more general cases there might not be a generic way of mixing different Xt beyond taking one of them at random.

(a1, . . ., aT) be a sequence of actions satisfying the feasibility constraint c(a) := Tt=1 ct(at) ≤ B, that leads to utility U(a) := Tt=1 ut(at).

We say that a sequence of actions has strong regret ε, if for all possible distributions A on sequences of actions a′ = (a′1, . . ., a′T) satisfying Ea′∼A

T

t=1 ct(a′t) ≤ B, the resulting utility

[U(a′)] := E

E

a′∼A

a′∼A

T

ut(a′t) ≤ U + ε · M. (17)

t=1

On the face of it, Deﬁnition 3 appears to be impossibly strong: we are considering regret with respect to any feasible strategy in hindsight. We even consider distributions over infeasible strategies as long as their average is feasible. However, in light of the discussion leading up to (15), it is something that is potentially attainable in our context. We claim that strong regret bounds translate into approximate equilibria in the game induced by the APEX mechanism. This is a consequence of the truthfulness of the VCG mechanism.

Lemma 4. Suppose that fi(x) ∈ [0, 1] for all x ∈ X, and that during the execution of Algorithm 1 with budget Bi and a truthfully reported fi, Player i has strong regret ≤ ε. Suppose further that heuristic H is locally correct. Then reporting fi truthfully and playing {λi,t}t=0..T−1 is an (2ε)dominant strategy for the menu of options available to Player i that is induced by the mechanism.

The proof requires a few careful steps, but the basic intuition is that local correctness + the fact that the prices are VCG prices implies that there is no beneﬁt (in tokens) in misrepresenting fi using some f˜i. Some extra effort is needed to see that the advantage of fi over f˜i in tokens+utility can be converted into a pure advantage in utility. After we establish that bidding fi is near-dominant, the low regret property concludes the argument.

Proof. Consider an alternative outcome based on the menu of options induced by the execution of Algorithm 1. In the alternative outcome, player i reports type f˜i and {λ˜i,t}t=0..T−1 leading to outcome X¯ i = U({X˜1, . . ., X˜T}).

We ﬁrst claim that there is no need for using f˜i = fi. Fix a round t, let C := C˜i,t(f˜i, λ˜i,t); U := fi(X˜t+1) − fi(Xt−+1i ).

That is, C is the cost Player i pays in round t, and U is the utility she derives compared to bidding 0. We will show that, at least in expectation, up to an additive ε, it is possible to attain the same (or better) cost/utility combination by bidding f instead of f˜.

Let

C(λ) := C˜i,t(fi, λ); U(λ) := fi(Xtλ+1) − fi(Xt−+1i ),

where Xtλ+1 is the outcome on bid (fi, λ). That is, the cost and utility due to Player i when bidding the true fi and λi,t = λ. Clearly C(0) = 0 and U(0) = 0.

t+1 and X2 := Xλ

C(λ) and U(λ) are non-decreasing. Suppose 0 ≤ λ1 < λ2. Let X1 := Xλ

2

1

t+1. Then we have, by the local correctness of H, and thus by local optimality of X1 and X2,

- Ft−i(X1) + λ1fi(X1) ≥ Ft−i(X2) + λ1fi(X2), (18) and
- Ft−i(X2) + λ2fi(X2) ≥ Ft−i(X1) + λ2fi(X1). (19) Adding (18) + (19) and simplifying, we get


(λ2 − λ1)fi(X2) ≥ (λ2 − λ1)fi(X1), which implies U(λ2) ≥ U(λ1).

Adding λ2 · (18) + λ1 · (19) and simplifying, we get

(λ2 − λ1)Ft−i(X1) ≥ (λ2 − λ1)Ft−i(X2), which implies that the VCG prices

C(λ2) = Ft−i(Xt−+1i ) − Ft−i(X2) ≥ Ft−i(Xt−+1i ) − Ft−i(X1) = C(λ1).

Utility U −ε can be attained using fi at some cost. Next, let δ := ε/T and λ := C/δ. We have Ft−i(Xtλ+1) + λfi(Xtλ+1) ≥ Ft−i(X˜t+1) + λfi(X˜t+1); thus

−C(λ) + U(λ) · C/δ ≥ −C + U · C/δ, and

U(λ) ≥ U − δ.

Utility ≥ U −ε can be attained using fi at cost ≤ C. Thus U is a non-decreasing function with U(0) = 0 and U(λ) ≥ U − δ for some λ16. Therefore, there must exist a value λ where the U − δ threshold is crossed. Unfortunately, a point with U(λ) = U − ε may not exist. However, there is a value λ such that

U(λ−) := lim

η→λ−

U(η) ≤ U − δ; and U(λ+) := lim

η→λ+

U(η) ≥ U − δ

Let µ ∈ [0, 1] be a parameter such that µ · U(λ−) + (1 − µ) · U(λ+) = U − δ.

Consider a mixed strategy that bids λ− (i.e. a value of λ arbitrarily close to λ from below) with probability µ and λ+ with probability (1 − µ). The expected utility of such a strategy is U − δ. It remains to calculate the expected cost, and to show that it is at most C.

![image 26](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile26.png>)

16In many cases, there is in fact a U such that U(λ) ≥ U. In these cases we in fact lose no utility from reporting the true fi.

Let X− and X+ be the outcomes of the bids (fi, λ−) and (fi, λ+), respectively. Then by optimality of X+ and X− we have

Ft−i(X−) + λfi(X−) ≥ Ft−i(X˜t+1) + λfi(X˜t+1), (20) and

Ft−i(X+) + λfi(X+) ≥ Ft−i(X˜t+1) + λfi(X˜t+1). (21) Taking the combination µ · (20) + (1 − µ) · (21), we get

µ · Ft−i(X−) + (1 − µ) · Ft−i(X+) + µ · λfi(X−) + (1 − µ) · λfi(X+) ≥

Ft−i(X˜t+1) + λfi(X˜t+1), which implies

−µ · C(λ−) − (1 − µ) · C(λ+) + U − δ ≥ −C + U, and thus the expected cost satisﬁes

µ · C(λ−) + (1 − µ) · C(λ+) ≤ C − δ.

Using strong regret to ﬁnish the argument. We have seen that it is possible to attain a total utility of at least

T−1

T−1

fi(X˜t+1) − T · δ =

fi(X˜t+1) − ε

t=0

t=0

using a mixed strategy over λi,t that only uses the true utility function fi. By the strong regret property, this mixed strategy attains utility within an additive ε of what Player i attains in the execution of Algorithm 1, leading to a total beneﬁt of at most 2ε from deviating.

![image 27](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile27.png>)

![image 28](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile28.png>)

![image 29](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile29.png>)

![image 30](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile30.png>)

### 2.2 An inﬁnitesimal version of the APEX algorithm

- Algorithm 1 is written in the full generality of the VCG mechanism. As a result, individual prices need to be calculated by making n calls to heuristic H at every time step. In addition, while as we have seen in the analysis of the algorithm, it does induce a menu of (token) prices for each player at each step, these prices are difﬁcult to interpret.


In the special case where X has a nice differentiable structure (for example, when X is Rk or the k-dimensional simplex ∆k as in the voting example below), and n is large, it is possible to use a quadratic approximation for the cost function to get a simpliﬁed version of Algorithm 1, with the added property that it produces a universal set of prices for effecting marginal change in the value of Xt+1.

For simplicity, let us assume that X is an open set. Alternatively, if X has a boundary, we assume that the regularizer goes to −∞ on the boundary ∂X, and thus Xt is a point in the interior of X for all t. In this case, assuming the objective functions and the regularizer are twice differentiable, we can write Ft(x) around Xt+1 as

Ft(Xt+1 + x) = Ft(Xt+1) − xTHtx + o( x 2). (22)

Note that since Xt+1 is a local maximum of Ft, the linear term vanishes, and we may assume that Ht 0 is non-negative semi-deﬁnite. Assuming Ht ≻ 0, and assuming the market is large17, using approximation (22) we can calculate approximate prices to charge Player i as follows.

Write

fi(Xt+1 + x) ≈ fi(Xt+1) + ∇fi(Xt+1)T · x. Then

Ft−i(Xt+1 + x) ≈ Ft(Xt+1) − xTHtx − λi,t∇fi(Xt+1)T · x. Maximizing over x gives

Xt−+1i ≈ Xt+1 − λi,tHt−1∇fi(Xt+1)/2, and

λ2i,t

Ci,t = Ft−i(Xt−+1i ) − Ft−i(Xt+1) ≈

4 · ∇fi(Xt+1)THt−1∇fi(Xt+1). (23) This leads to the specialized Algorithm 2 below. Note that a very attractive feature of Algorithm 2 is that we only need gradient access to fi in order to compute prices. Assuming H is a heuristic based on gradient descent, one can expect to be able to run the entire algorithm with only gradient oracle access to the players’ utilities. This is important both due to communication/privacy constraints and the fact that the players themselves may only have limited access to the fi’s through a gradient (or even just a stochastic gradient) oracle.

![image 31](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile31.png>)

![image 32](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile32.png>)

- Algorithm 2 Inﬁnitesimal-APEX (f0, f1, . . ., fn, H) algorithm given utilities fi : X → R, principal’s utility f0 : X → R, local optimization heuristic H Main mechanism:


![image 33](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile33.png>)

- 1: Fix starting point X0 ∈ X;
- 2: for t = 0..T − 1 do
- 3: Collect bids λi,t ≥ 0 from Player i;
- 4: Selects a regularizer Rt(x) that may depend on t, X0, . . ., Xt;
- 5: Set Ft(x) := f0(x) + j=1..n λj,tfj(x) + Rt(x);
- 6: Let Xt+1 be obtained by H by maximizing Ft(x) starting at Xt;
- 7: Write Ft(Xt+1 + x) = Ft(Xt+1) − xTHtx + o( x 2);
- 8: for each Player i = 1..n do
- 9: Charge Player i, Ci,t := λ

2 i,t

![image 34](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile34.png>)

4 · ∇fi(Xt+1)THt−1∇fi(Xt+1) tokens;

- 10: end for
- 11: end for Suggested algorithm for Player i:


- 1: Report utility fi : X → R to the mechanism;
- 2: Run a Bandit with Knapsacks online algorithm with initial budget Bi to determine the {λi,t}Tt=1;


![image 35](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile35.png>)

![image 36](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile36.png>)

17We don’t need this assumption if fi is linear on X

Relation to quadratic pricing. We note that the competitive equilibrium induced by Algorithm 2 exposes each player to quadratic prices over the space of outcomes. Quadratic pricing (and quadratic voting) has a rich history within the area of social choice — suggesting another way in which such prices may occur “naturally” as a result of repeated VCG-mediated interactions. We expect quadratic prices to occur whenever (22) is an adequate approximation. Generally speaking, this should hold when dim(X) ≪ n. Therefore, quadratic pricing are natural to expect in voting and participatory budgeting, while we should expect other (potentially linear) prices to occur when dim(X) is high, such as in allocation of items or in bipartite matching.

### 2.3 General analysis and open problems

As we have seen in Lemma 4, if the players attain low regret, the APEX Algorithm leads to a competitive equilibrium in which reporting fi truthfully is an ε-dominant strategy. Assuming approximation (22) holds, a similar statement can be made about Algorithm 2. The main question therefore is ﬁnding out whether/when players under the APEX Algorithm attain strong low regret, and — if possible — how one can compute the outcome of such convergence efﬁciently. We should note that unlike some scenarios in algorithmic mechanism design, the algorithm’s incentive properties hold assuming it has converged. Therefore, even without theoretical guarantees, a heuristic that almost always converges in practice will have the desired incentive properties. As we have seen in Lemma 4, and will see in Section 3.2 (Theorem 13) again, results can be typically phrased as “if the algorithm converges to a low-regret solution, then...”.

Beyond convergence of the algorithm — or, rather, assuming it converges (either provably or in practice) — we need to consider whether the outcome of the algorithm is “good”. In the setting without money it is impossible to deﬁne a common utility function and thus it is an interesting problem to even deﬁne efﬁciency (beyond Pareto efﬁciency) in these settings. Some of the questions that come up here are philosophical in nature (e.g. deﬁning “fairness” of a decision procedure — most deﬁnitions are necessarily under-speciﬁed).

Additional interesting questions arise when one tries to adapt the mechanisms to the setting with money. Generally speaking, mechanism design with money is easier than without money, since it is easier to state common objectives such as utility using the common currency. However, the introduction of money takes away one degree of freedom from the mechanism — the exchange ratio between a player’s utility and tokens, potentially making the problem more difﬁcult. In addition, the direct link between payments within the mechanism and money opens the opportunity for collusion through outside transfers18.

In the direction opposite to mechanisms with money, the bandits with knapsacks setup actually allows one to use multiple non-exchangeable token currencies with which participants are endowed. Bandits with knapsacks with multiple currencies (multiple knapsack constraints in the BwK terminology) are considerably more complex to analyze. Therefore, it may be more difﬁcult to get algorithms with multiple currencies to converge. At the same time, having multiple token currencies would allow to express more complex normative requirements from the resulting mech-

![image 37](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile37.png>)

18Collusion is possible — an indeed is sometimes unavoidable — even in mechanisms without money, but the ability to measure collusion in money simpliﬁes collusion between untrusting parties.

anism (e.g. “equal treatment with respect to multiple non-substitutable categories of outcomes”).

At the core of our reductions from algorithms (or heuristics) to mechanisms is the bandits with knapsacks setting. While it has receive substantial attention in the past decade (both directly, and indirectly – e.g. in the context of online advertisement campaigns with budgets), it is still not nearly as well-understood as the general bandits setting. Further development of the theory of BwK — particularly in terms of sufﬁcient conditions for the existence of low-regret strategies would further our ability to develop new generic mechanisms.

Finally, throughout the reduction we have treated the participants’ utilities fi as ﬁxed and known to the participants at the start of the algorithm. In practice, often these utilities themselves are being learned by the participants in a multi-round process. While the time t in Algorithm 1 is entirely ﬁctitious — representing epochs of an optimization procedure. However, it is not hard to adapt the algorithm into an online version where participants adjust their function fi over time,

- as new information arrives. As there is a tight link between optimization and online optimization, one can expect this link to extend to the reduction given by Algorithm 1.


Below we will address these points in greater detail, formulating speciﬁc problems and directions.

- 2.3.1 Convergence analysis


The APEX Algorithm provides a generic procedure for turning optimization heuristics into mechanisms. Unfortunately, at this level of generality, there is no hope of proving that the procedure “works”. Even deﬁning what “works” means is potentially challenging.

We say that an execution of the APEX Algorithm is valid if at the end of the execution all players have low regret with respect to the resulting outcome and prices. One actually has to be careful about deﬁning what low regret here means. In Lemma 4 we took strong ε-regret to mean that the absolute difference between the realized moves and the best moves in hindsight are small, one can also imagine scenarios where a relative measure of regret is more appropriate. Whichever notion is chosen, it makes sense to ask whether a valid execution exists, whether it is attained by a typical execution of the algorithm, and how robust it is.

- Problem 1. Let an execution be valid if players experience low strong regret. Provide sufﬁcient


conditions on X, the fi’s Rt’s, H, and the regret notion so that there exists a valid execution of the APEX Algorithm.

We expect a valid execution to exist under reasonably mild conditions — ones that follow from generic ﬁxed point theorems. For example, as we shall see in Section 3.2, Brouwer’s Fixed Point Theorem is sufﬁcient to prove that there always exists a competitive allocation of items under the Hylland-Zeckhauser scheme are supported by a valid execution of the APEX Algorithm. A more ambitious question is to ﬁnd sufﬁcient conditions for all executions to be valid. Note that for all executions to be valid we will need the players’ BwK algorithms to be “good” — ones attaining low strong regret under reasonable conditions on the game the player is facing. We will leave questions of designing such “good” BwK algorithms to Section 2.3.3.

- Problem 2. Let an execution be valid if players experience low strong regret. Provide an algorithm

for the players and sufﬁcient conditions on X, the fi’s Rt’s, H and the regret notion so that the execution of the APEX Algorithm is valid with high probability.

Note that the APEX Algorithm has a parameter T representing the number of rounds or epochs in the optimization. Therefore, in both Problems 1 and 2 (as in later problems concerning the quality of the resulting solution), the answer may depend on T. Just as in optimization for empirical loss minimization of machine learning models, one can expect the quality of the solution to improve as T → ∞19. It is therefore important to understand the dependence of the set of outcomes of valid executions on T.

- Problem 3. Let VT = VT({fi}, Rt, H) ⊂ ∆(X) be the set of possible outcomes X¯ of a valid execution of the APEX Algorithm. Under what conditions does the sequence {VT} converge to a set V (in the earth-mover metric W1(X))?

Building on the above, one can ask whether the resulting solution is essentially unique.

- Problem 4. Under what conditions is the resulting set V in Problem 3 a singleton V = {ν}? How fast do {VT} converge to {ν} in this case?

2.3.2 Computational issues in reaching equilibrium

Since our end-goal is to be able to efﬁciently ﬁnd the solution X¯ , questions from Section 2.3.1 may and should be asked in the context of computational efﬁciency. One advantage of the approach based on an algorithm (as opposed to one based on an equilibrium deﬁnition) is that the APEX Algorithm is itself a procedure for producing a solution X¯ . As long as it converges to an ε-equilibrium reasonably fast, say in s(n, ε) steps, we get an algorithm whose running time is dominated by O(n · s(n, ε)) applications of heuristic H.

Part of the setup’s goal is to be able to treat H as a black-box. This would allow us, for example, to deal with cases where the functions fi are not convex. When we treat H as a black-box, our only recourse in terms of accelerating computation is to speed up convergence — the number of steps s(n, ε) it takes to converge to an ε-equilibrium.

- Problem 5. What is the smallest number of iterations s(n, ε) does the APEX Algorithm need to converge to an ε-equilibrium? Can the algorithm be tweaked to make this number instanceoptimal?


One can hope that this number of steps can be reduced by changing the weights in the output X¯ to speed up convergence. As in many cases involving iterated minimization, it is likely that there are heuristics that converge much faster than the worst-case guaranteed convergence speed.

The special case where the underlying problem is convex (and thus heuristic H is not strictly necessary) is important in a number of potential applications, including the ones we’ll see in Section 3. In this case, it is entirely plausible that Algorithm 1 can be rewritten as a (larger) convex

![image 38](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile38.png>)

19One can also envision a version of Algorithm 1 where the learning rate is lowered over time.

program, featuring variables λi, and potentially other auxiliary variables. This is indeed the case with correlated Nash equilibria, which can be attained via play among appropriate low-regret players, but can also be computed directly via a linear program20.

- Problem 6. Suppose f0 and the fj’s are concave, and that X is a convex set. Further suppose that Rt = 0, and that H is just the algorithm that ﬁnds the maximum of a function on X. When can an outcome X be computed by a convex program, and what is the convex program computing it?


A likely prerequisite for an afﬁrmative answer to Problem 6 is that the set of possible ε-regret outcomes is convex.

- 2.3.3 Bandits with knapsacks


The technically least speciﬁed part of the APEX Algorithm has to do with the low-regret algorithm the players are supposed to run. While quite a bit of work has been done on bandits with knapsacks, there are many outstanding questions remaining.

In its full generality, in the bandits with knapsacks setting, at time t the agent can pull one of k arms. After pulling arm it at time t, in addition to the reward ri

t,t, the player experiences a d-dimensional cost vector ci

t,t ∈ Rd≥0, corresponding to the cost of pulling the arm in terms of d constrained resources21. The player is constrained by a budget vector B ∈ Rd≥0 Once the sum of the costs in one of the constraints ℓ ∈ [d] is exceeded, that is:

T0

ci

τ,τ,ℓ ≥ Bℓ,

τ=1

the player has to stop and can’t collect further rewards. For all preceding discussions, we are only interested in the special case of d = 1. The case d > 1 is potentially interesting for some generalizations discussed is Section 2.3.5, but for all standard applications d = 1 is the case to consider.

As we noted earlier, unlike the standard multi-arm bandits setting, in the BwK setting we cannot guarantee vanishing regret in hindsight. In standard bandit settings with bounded rewards, over T rounds, one can hope to attain O(T1/2) regret. In the case with knapsacks, there is no way to attain a o(T) regret, and, in fact, there may be a multiplicative regret of as much as ×log T [ISSS19].

The big reason for BwK being more difﬁcult, which we alluded to earlier, is that the optimal “bang-per-buck” may change drastically over time. Consider a simple scenario where at each round there is a zero-arm with cost and reward zero22. The second arm costs ct = 1 to pull. The total budget is B = T/2. In rounds t = 1..T/2 the reward rt = 1. There are two scenarios with respect to rewards in the second half: either the reward is rt = 2 for all for t = T/2 + 1..T, or the reward is rt = 0 for all for t = T/2 + 1..T. The player needs to decide whether to exhaust

![image 39](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile39.png>)

20Which method is faster or better depends on the application domain. From the theoretic perspective what’s

important is that this equivalence exists. 21These are the capacity-constrained “knapsacks”. 22It is often assumed by default that such an arm — the option of “not playing” is available.

its budget in the ﬁrst half of the game, before learning whether this was the right decision. It is not hard to see that the best additive regret the player can attain is T/2, and the best multiplicative ratio attainable is 32. Thus, even in this toy example, vanishing regret is impossible. Interestingly, this effect seems to persist even in the experts with knapsacks model, where the payoffs and costs of all arms is revealed.

![image 40](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile40.png>)

One can specialize the general BwK scenario to the following concave-reward game. At every round, the player is presented with a concave, non-decreasing cost-reward-function Rt : c  → rt, satisfying Rt(0) = 0. The player chooses a cost ct, subject to the global constraint Tt=1 ct ≤ B. The reward is calculated as

T

R(c) =

Rt(ct). Models of this kind have been considered in [AD19].

t=1

On the face of it, the concave-reward game is easier than the general BwK game. However, we believe that, in fact, it captures the difﬁcult part of the BwK, and the gap between these two games in fact vanishes in the same way as the regret of bandits without knapsacks is vanishing. It would be interesting to formulate the exact sufﬁcient conditions for this.

- Problem 7. Under what conditions are the regrets of the following games with budgets the same up to an additive o(T)? How small is the gap between regrets? The scenarios are:


- 1. general BwK, with a menu of cost/rewards (ci,t, ri,t), where cost/reward information is only revealed about the arm pulled;
- 2. BwK in the experts setting, where the cost/reward information is revealed about all arms;
- 3. BwK with stochastic closure of the arms: we are allowed to pull an arm i with probability p ∈ [0, 1], and experience cost p · ci,t and reward p · ri,t;
- 4. the setting above in the experts regime: where the cost/reward information is revealed about all arms;
- 5. the setting with stochastic closure, where the cost/reward information is revealed before the decision about it is made. Note that the cost-reward function in this case is given by


Rt(c) := max

min(ri,t · c/ci,t, ri,t). (24)

i

Rt is concave and non-decreasing — corresponding to the cost-reward game scenario.

In particular, while nominally scenario 1 is much harder than scenario 5, we believe that they are in fact equivalent under reasonable assumptions.

- 2.3.4 Efﬁciency and fairness of the outcome


The overall goal of the framework we present is to attain “good” solutions X¯ using a mechanism that leads players to reveal their utility functions fi truthfully. Since we chose to focus on mechanisms without money, actually deﬁning efﬁciency appears to be non-trivial23.

Pareto efﬁciency. One relatively weak benchmark is Pareto efﬁciency — the resulting outcome X¯ cannot be replaced with an outcome X¯ ′ under which all players are at least as well-off as under X¯ , and at least one player is strictly better off.

We should note that unlike mechanisms with money, in the world without money Pareto optimality is a fairly weak condition. To illustrate, in the context of voting, all Pareto efﬁciency requires is that if all voters prefer option A over option B, then option B is never selected.

There are two main obstacles to our mechanism being Pareto efﬁcient: (1) the heuristic H may fail to optimize correctly (an algorithmic failure to locate a solution that is “better for everyone” will necessarily map to a mechanism failure); and (2) whenever a regularizer is used, a (small) fraction of utility is sacriﬁced by adding a regularizer. Given these obstacles, it is possible for the outcome to not be entirely Pareto efﬁcient. In the voting example, even if all voters prefer

- A over B, it is possible that the regularizer will allow for B to be selected with some (vanishing) probability.


A natural approach would be relax the Pareto optimality condition, to allow for deviations that lead to vanishing improvements. One natural deﬁnition of approximate Pareto efﬁciency is given in [ILWM17], saying that an outcome X¯ is (1+ε) Pareto efﬁcient, if there is no alternative solution X¯ ′ where the utility of each player is increased by a factor (1 + ε). A weaker deﬁnition would say that there is no X¯ ′ where no player is worse-off, and at least one player is better off by a factor > (1 + ε). We believe that in most cases X¯ will satisfy at least approximate Pareto efﬁciency.

- Problem 8.


- 1. Under what conditions do all solutions X¯ given by the APEX Algorithm satisfy Pareto efﬁciency?
- 2. What is the correct notion of approximate Pareto efﬁciency in this setting? Under what conditions do all solutions X¯ given by the APEX Algorithm satisfy approximate Pareto efﬁciency with approximation ratio 1 + on(1)?


Efﬁciency beyond Pareto. As noted above, Pareto efﬁciency appears to be a fairly weak efﬁciency guarantee. While one would be suspicious of a mechanism that fails to be Pareto efﬁcient, there are Pareto efﬁcient schemes that are clearly “inefﬁcient”.

Consider the example of n voters choosing between two alternatives A and B. A mechanism

that picks A and B with probability 12 each unless there is unanimous support for one of the alternatives (in which case that alternative is picked), is Pareto efﬁcient, even though intuitively it is

![image 41](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile41.png>)

![image 42](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile42.png>)

23In mechanisms with money, one can deﬁne the utility of the outcome in units of the common currency, and compare this utility to the maximum attainable total utility.

inefﬁcient to select B with probability 12 if n−1 participants prefer A and only 1 participant prefers B.

![image 43](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile43.png>)

On the other hand, this simple example already illustrates the difﬁculty in deﬁning efﬁciency without money — it fails to take into account intensities of preferences. If there are n − 1 participants having a very weak preference for A and 1 participant with a very strong preference for B, then perhaps choosing B with probability 12 (or even with probability 1) is the efﬁcient outcome. It is hard to imagine a practically “efﬁcient” mechanism in which A will not be selected with an overwhelming probability. Thus the question is not just how to attain efﬁciency by a truthful mechanism, but how to deﬁne it properly.

![image 44](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile44.png>)

- Problem 9. Is there a generic deﬁnition of efﬁciency in mechanisms without money that extends beyond Pareto efﬁciency and that is consistent with truthful mechanisms?


Fairness. Once one moves beyond Pareto efﬁciency, a tension arises between fairness and efﬁciency. It is very challenging to deﬁne fairness in mechanisms without money. A minimum requirement akin to Pareto efﬁciency is equal treatment of equals: identical players should (at least ex-ante in the case of lotteries) experience identical outcomes. In allocation problems, this can be attained by a pseudomarket based on equal endowments such as the Hylland-Zeckhauser scheme [Bud11, HMPY18]24. In social choice context, this can be attained by a symmetric social choice function.

It would be appealing to have a deﬁnition of fairness that moves beyond ‘equal treatment of equals’. A natural deﬁnition of efﬁciency that is not attached to prior beliefs about values is ‘maximize sum-total welfare of participants’25. What should a similar deﬁnition of fairness? Without any additional context, fairness will translate into equal treatment of participants — of course, it is unclear what that would actually mean.

A compelling extension of equal treatment of equals is equalizing the externalities participants exert on other participants: the amount of utility reduction they inﬂict on other players by participating. A recent detailed discussion of this extension in the context of algorithmic mechanisms without money (and additional references) can be found in [IPW19].

To illustrate equalizing externalities, consider an example with two players Alice and Bob with utility functions UA : X → R+ and UB : X → R+. Let oA := maxx UA(x) and oB := maxx UB(x) be the maximum utilities attainable by the individual players. A solution yopt will be efﬁcient if

UA(yopt) + UB(yopt) = max

(UA(x) + UB(x)).

x

The externality Bob causes in solution y is ExtB(y) := oA − UA(y) ≥ 0. The externality Alice causes os ExtA(y) = oB − UB(y) ≥ 0. If we are lucky, we will have

ExtB(yopt) = ExtA(yopt),

![image 45](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile45.png>)

- 24In the context of allocations using pseudomarkets, we also wish to have the property of envy-freeness: no player wishes the bundle of another player. Note, however, that the concept of envy-freeness does not make sense in scenarios such as voting or even two-sided matching.
- 25As seen above, there are signiﬁcant implementation barriers to realizing efﬁciency without money.


or, more broadly

ExtA(y), (25) where the distribution µ of outcomes is supported on points maximizing UA(y) + UB(y):

ExtB(y) = E

E

y∼µ

y∼µ

∀y ∈ supp(µ) UA(y) + UB(y) = max

(UA(x) + UB(x)). (26)

x

Note that there is no reason to believe that (25) and (26) can be satisﬁed simultaneously — most likely they cannot. One solution is to assign weights to players so as to make both conditions hold — the weights correspond to a competitive equilibrium. In terms of good fairness properties for a mechanism to have, one can ask that it ﬁnds an externality equalizing distribution over optimal outcomes whenever one exists.

- Problem 10. Is there a generic deﬁnition of fairness in mechanisms without money that is consistent with truthful mechanisms?

It is quite possible that there is no generic answer to Problem 10, and that the answer will depend on the precise setting. For example, in the case of voting, it makes sense to extend equaltreatment-of-equals to require that two “diametrically opposite” voters (approximately) cancel out. On the other hand, in the case of allocation mechanisms ex-ante envy freeness is a natural condition.

Towards axiomatization? The discussion of both efﬁciency beyond Pareto and fairness thus far focused on deﬁnitions as they pertain to the underlying optimization problem. The additional truthfulness constraints in the context of mechanism design will make attaining these properties even more difﬁcult. On the other hand, the need for a truthful implementation might actually simplify the problem of reaching the “right” deﬁnitions, by limiting the scope of what is possible.

- Problem 11. Are there natural axiomatic properties pertaining to efﬁciency, fairness, and truthfulness, that together yield a set of mechanisms without money that can be presented in a general form, along the lines of the APEX Algorithm?


- 2.3.5 Extensions to mechanisms with money and with multiple token currencies


Many mechanisms without money over continuous domains use some kind of token pseudocurrency within their calculations. These tokens can be interpreted as representing a view on the relative importance of participants’ preferences. For example, under most schemes, participants that are given equal token endowments will have an equal opportunity to affect the outcome of the mechanism. The APEX Algorithm, along with applications we will discuss in Section 3 fall into the single-token category.

Mechanisms with money. It is natural to ask whether these mechanisms apply in settings with money. At a high level, money makes attaining efﬁciency easier, since it provides an absolute efﬁciency scale. At the same time, it may make truthfulness more difﬁcult to attain, since one needs to not only consider deviations leading to a better outcome for player pi, but also deviations leading to an identical outcome where pi has more money in the end. In addition, participation constraints which are not an issue in mechanisms without money may become an issue26. A closely related issue — which for example limits the utility of the VCG mechanism in the context of public projects — is that the amount of revenue raised by VCG is highly unstable in the inputs.

An important example of a successful mechanism with money which combines elements of online learning and repeated auctions is the sponsored search ad placement mechanism [LPSV07]. In this setting a search engine such as Google needs to decide which ads to display along with its search results. The resulting mechanisms often feature an advertisement budget, which makes

- them share some features with the no-money setting (the problem becomes in part “get the best set of ads displayed in exchange for budget B”).


- Problem 12.

- 1. To what extent can the framework of the APEX Algorithm be adapted to a setting with money, in particular with budget constraints? Can results such as the Fisher market be recovered?
- 2. Can the framework be extended to a hybrid setting with both tokens and money, to attain higher level of efﬁciency while maintaining a degree of fairness?


Another question altogether is the best way of attaining truthfulness and efﬁciency with money, where the underlying preferences are very complex, and possibly implicit — given only via a gradient oracle, or evolving over time. In practical terms, it might be best to keep the internal workings of the APEX Algorithm denominated in token units (and not in money), and wrap a money-for-token exchange around it.

Multiple token currencies. The bandits with knapsacks framework extends naturally to a setting with d different types of constrained resources. This should allow our framework to extend seamlessly to a setting with multiple currencies. It remains to be seen whether there are natural scenarios where using multiple token currencies is preferred to using a single one. On the one hand, having multiple currencies might allow the designer to state multiple normative constraints of the form “players are treated equally along multiple axes”. On the other hand, an effective “exchange rate” may emerge between the currencies, nullifying its beneﬁt.

- Problem 13.


- 1. Can the APEX Algorithm be adapted to a setting with multiple token currencies? What properties hold in this case?
- 2. Are there settings where multiple token currencies attain an objective not attainable using a single token currency?


![image 46](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile46.png>)

26Participation constraints assert that a player is not worse-off participating in a mechanism than not participating.

An potential setting to investigate in this context is bipartite matching, with two different currencies used by the two sides of the match, as a way to ensure that both sides’ preferences are given equal consideration.

- 2.3.6 Combining with online learning


Much of algorithmic mechanism design presupposes that utility functions fi are known to the participants themselves, and that the main challenge is to elicit information about these fi to arrive

- at a socially desirable outcome. On the other hand, the key challenge in online learning (even with a single participant), is that the payoff function is unknown and needs to be discovered/maintained over time. In many practical scenarios with multiple participants features from both mechanism design and online learning are present. For example, advertisers buying impressions online are simultaneously (1) learning the value of these impressions (for example by observing the fraction of impressions that result in a sale); and (2) learning to interact with the mechanism selling ad impressions.


Citing online advertising as an explicit motivation, [KGJS20] formalizes the problem of mechanism design where rewards need to be learned27. For the setting with money, it gives a VCG-based mechanism that has both good asymptotic regret properties and is asymptotically truthful — at least when deviations by a single player are considered. This immediately raises the question of whether one can produce a good mechanism without money for agents that are learning over time.

- Problem 14. Design mechanisms without money for a setting where players learn their type over time.

For best results, the mechanism would interpret “learn” broadly in the following sense. Traditionally, regret bounds are frames in max-min terms, against the worst possible environment, while in practice learning algorithms may perform much better than these guarantees. Ideally, the performance of the mechanism should be comparable to the heuristic performance of the best learning algorithm in hindsight, and not to the max-min regret performance.

A natural candidate to address Problem 14 is an adaptation of Algorithm 1, where instead of fi the players submit function fi,t based on what they’ve learned about the environment up to that point. In the non-strategic settings, algorithms such as “follow the regularized leader” are already framed in terms of optimizing an objective function that evolves based on past feedback.

- Problem 15. Analyze the extension of Algorithm 1 based on utility functions fi,t that evolve over time.


Note that as stated, “time” in Algorithm 1 corresponds to optimization epochs, therefore it is likely that the correct blending of the algorithm with online learning would involve updating the functions fi,t only every T rounds — interlacing T rounds of optimization with a single round of performing an action, observing the outcome, and updating utility functions based on these observations.

![image 47](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile47.png>)

27See also earlier works, e.g. [NSV08, BKS13a].

## 3 Applications

In this section we present a preliminary discussion on applications to main domains where mechanisms without money are used.

As we will discuss, in many cases there are inherent incentive issues, such as collusion, that are beyond the reach of any mechanism. On the other hand, our framework is sufﬁciently ﬂexible to ﬁt most optimization algorithms, and in many cases it is ﬁrst-order approximately individually truthful, which means that we can hope to have ﬁrst-order approximate efﬁciency and (competitiveequilibrium) truthfulness even in cases where known negative results rule out efﬁcient truthful mechanisms.

In other words, one can decompose the problem of coordination via a mechanism into the following three components: (1) algorithmic: ﬁguring out individual utility functions, and solving the aggregate optimization problem; (2) individual incentives: incentivizing participants to reveal their preferences truthfully; (3) policy: preventing mechanism failure through actions outside the mechanism (such as collusion). Algorithmic mechanism design deals primarily with (2). The best one can hope for is to attain (2) without putting constraints on (1), and without making (3) worse than necessary.

We will discuss three main applications: voting, one-sided allocation, and two-sided allocation. In the case of one-sided allocation, we will show a new connection to existing pseudo-market mechanisms. In the other two cases, we will give a general high-level discussion, leaving results to subsequent works.

### 3.1 Voting with cardinal preferences

We consider the problem of aggregating cardinal preferences of n over a discrete set of possibilities [k] with k ≥ 2. “Cardinal” (as opposed to ordinal) means that each player i ∈ [n] has a utility vector

- ui ∈ Rk, where uij represents how happy player i would be with outcome j. Since the aggregation mechanism doesn’t use money, the output should be the same whether player i reports ui or 2ui, which means that ui should be treated as normalized direction vectors.


Impossibility: strategy-proofness and efﬁciency Generally speaking, the only case in which truthful, symmetric (or even just non-dictatorial), and Pareto efﬁcient voting is possible is when k = 2. Whenever there are more than two possibilities to choose from, there will be some opportunity for strategic voting. This is true in the ordinal case [Gib73, Sat75], and in the case with cardinal voting [Gib78, Hyl80].

A dictatorial scheme is truthful and Pareto efﬁcient; it can be made symmetric by turning it into a randomized dictatorship scheme, where an index i ∈ [n] is selected at random, and then player i picks her favorite alternative. Note that even in the case with two alternatives, randomized dictatorship is not very efﬁcient — if 90% of the voters prefer alternative A, and 10% prefer alternative B, the disfavored alternative will be chosen 10% of the time. In addition, randomized dictatorship discards all quantitative information about the preferences. For example, suppose are three alternatives A,B, and C. Half the voters have preference A C ≫ B (that is, slightly prefer

- A over C, and strongly disfavor B), and half the voters have preference B C ≫ A. In such a scenario, the clearly best alternative is C, but a randomized dictatorship will select A and B with equal probability, never selecting C.


As noted in Section 2.3.4, even in the case of two alternatives, efﬁciency is somewhat elusive due to normalization. For k = 2, and the standard majority rule, the voting rule does not pick an alternative j maximizing

U(j) :=

uij.

i∈[n]

Rather, if we denote λi := |u 1

i1−ui2|, the majority rule maximized U˜(j) :=

![image 48](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile48.png>)

λiuij. (27)

i∈[n]

In other words, each voter is scaled so that the difference between their more preferred alternative and less preferred alternative is 1. In such a scheme, voters who have stronger preferences are scaled down, and voters who have weaker preferences are scaled up. Absent money (or some other persistent value-tracking mechanism), such scaling is unavoidable, since there is no cost for player i to report 2ui instead of ui, and thus such report shouldn’t increase the player’s inﬂuence.

One could hope to deﬁne efﬁciency in terms of the sum of universally normalized utilities,

maximizing i∈[n] uˆij, where uˆ is the unit vector in the direction of u according to some norm. This is indeed the form of (27) for the two-alternative majority rule. With more than two al-

ternatives, truthfulness implies that the norm in the scaling will have to depend on the outcome being considered. Consider an example where there are k = 3 alternatives (A, B, C) and there is an approximately equal number of voters with utility vectors given by u1 = (12, 11, −23),

- u2 = (11, 12, −23), u3 = (2, 1, −3), u4 = (1, 2, −3). The preferences u1 and u3 are identical with respect to alternatives A and B, but u1 has a much stronger preferences against C28. Note that all players dislike alternative C, and thus the choice will be between alternatives A and B. In


this example, we then should expect uˆ1 ≈ uˆ3, but this means that the norm with respect to which normalization will happen will have to give very little weight to the C component. Otherwise, players with type u1 will be incentivized to misreport their type as u3 — this is how strategic voting typically happens in practice: if an alternative is “not realistic” voters will try to reallocate their inﬂuence to alternatives among which actual choice is happening.

Therefore, in deﬁning efﬁciency, the normalization factors in (27) will not only need to depend on the uij’s, but also on the alternatives being considered. The key challenge, of course, is the circularity of such scaling: the outcomes considered depend on the scaling factors, while the scaling factors depend on the outcomes being considered.

Collusion-proofness. Typically, truthfulness, or strategy-proofness is concerned with deviations by a single player. Even the strongest notion of truthfulness — dominant strategy truthfulness — only requires that a single player cannot improve her outcome by misreporting her type. A

![image 49](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile49.png>)

28Note that the utilities are given up to scaling and shifting. If we add 10 to all values in u3, we will get (12,11,7), demonstrating that u1 indeed dislikes C much more than u3.

truthful mechanism may still be susceptible to collusion, where a number of players misreport their types to improve their outcomes. In some settings (such as one-sided allocation) it is possible to resist collusion, at least when transfers between players are not allowed. Unfortunately, it appears that in the context of voting, it is impossible to avoid collusion. Continuing the three-alternative example, two players with types u1 = (1, 1, −2) and u2 = (1, −2, 1) are in perfect agreement about preferring alternative A, but work against each other regarding alternatives B and C. They can form a coalition around promoting alternative A, for example by reporting their type as u˜ = (2, −1, −1). Under most voting schemes (including schemes based on normalizing votes), this will increase the collective impact of the two players. In the context of politics, such collusion corresponds to forming a political party.

Quadratic voting. A natural concept for cardinal voting that has gained some popularity in recent years is quadratic voting. Under quadratic voting, a voter is given a budget of 1 token, which she can allocate among the alternatives [LW18]. Giving vj votes to alternative j costs vj2 tokens. Suppose the voter has utility uj · vj for giving vj tokens to alternative j, and suppose further that

- uj ≥ 0. Then the unit-cost allocation maximizing total utility is given by


uj

vj =

.

![image 50](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile50.png>)

![image 51](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile51.png>)

i u2i

Thus, the optimal vote is indeed the true type uˆ normalized to unit euclidean length. This scheme can work in the context of participatory budgeting, but is not portable “as-is” to the social choice context. Even if the output is a lottery where alternative j ∈ [k] is selected with probability pj, the constraints pj ≥ 0, j∈[k] pj = 1 would make an non-distorted quadratic voting scheme impossible. On the other hand, the equilibria that naturally occur in Algorithm 1 (and more explicitly in Algorithm 2), lead to essentially a “quadratic-form” voting scheme, where the cost of the vote in direction v is vTAv for some PSD A 0, rather than just vTv = vi2.

Speciﬁc problems. The speciﬁc problems can be broken down into two parts corresponding to “theory building” and “algorithm design”. On the algorithm design side, the main problem is to design new voting mechanisms with cardinal utilities based on Algorithm 1. These are essentially Problems 1–6 specialized to the voting scenario.

- Problem 16. 1. Adapt Algorithms 1 and 2 to the setting where X = ∆k is the set of probability distributions over [k], and utilities fi(p) := j uijpj are linear.


- 2. Under what conditions is the output of such an algorithm unique? How hard is it to compute both in theory and in practice?
- 3. What kind of competitive equilibrium does it induce?
- 4. What are the competitive-equilibrium truthfulness guarantees, and what is the efﬁciencytruthfulness trade-off?


Giving satisfactory answers to Problem 16 will yield a new practical family of preference aggregation algorithms. There are some secondary beneﬁts to being approximately strategy-proof, such as allowing for asynchronous voting (since knowing how other participants voted does not have much impact on one’s best response).

In terms of theory-building, there are two main outstanding questions.

Efﬁciency-truthfulness trade-offs. The ﬁrst theory-building question is about mapping out the efﬁciency-truthfulness frontier.

- Problem 17. For the n-voter, k-alternative voting problem with (normalized) cardinal utilities, what is the fundamental trade-off between approximate truthfulness and approximate efﬁciency?

Known negative results show that (exact) truthfulness is incompatible even with fairly weak notion of efﬁciency. Note that one needs to be careful with the deﬁnition of “approximate truthfulness”: it is not hard to create a voting scheme that is efﬁcient and ε-truthful with ε = on(1), in the sense that the expected beneﬁt from misreporting one’s preferences is bounded by ε. The problem is that in such mechanisms the beneﬁt of voting would also be O(ε). A proper deﬁnition of approximate truthfulness would say that the beneﬁt from misrepresenting one’s vote should either be small relative to the beneﬁt of voting at all, or tiny in absolute terms.

A possible deﬁnition of an (ε, δ)-truthful voting scheme M is that for all u−i, ui, u′i, uTi · (M(u−i, u′i) − M(u−i, ui))

![image 52](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile52.png>)

![image 53](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile53.png>)

beneﬁt from misreporting

≤ δ · ui + ε · uTi · (M(u−i, ui) − M(u−i, 0))

![image 54](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile54.png>)

![image 55](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile55.png>)

beneﬁt from voting

. (28)

Here δ should be very small (o(n−1/2), and ideally O(n−1) or even 0), and ε should be O(1), and ideally o(1).

- Problem 18. For what values of (ε, δ) is it possible to attain an (ε, δ)-truthful voting mechanism with vanishing efﬁciency loss?


Good properties beyond symmetry? The second theory-building question is deﬁning “good” properties one should require of a quantitative voting scheme, and obtaining relationships between these properties. The biggest question is how to deﬁne fairness beyond requiring that M is symmetric in the votes. One possible extension is that if two players have diametrically opposing views — that is ui + uj = 0, then removing them should only change the outcome distribution by a negligible amount. This can be extended to a small set S of voters with i∈S ui = 0. We should not expect such a property to hold exactly, since one would expect that adding a pair of voters that is indifferent in aggregate would slightly move the outcome towards the uniform distribution29.

### 3.2 One-sided allocation

In the one-sided allocation setting there are n players and n goods. We will focus on the simplest case, in which each player wishes to obtain exactly one good, and the goal of the mechanism is to

![image 56](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile56.png>)

29Note that a (1 000 100,1 000 000) vote is much closer than a (100,0) vote.

produce a matching π : [n] → [n]. Each player has a vector of utilities ui, where uij ∈ [0, 1] is the utility experienced by player i from obtaining item j. Applications of this setting include allocation of scarce resources where money cannot be used, such as school choice and course assignment. Since transfers cannot be used, the solution concept typically involves a lottery, where the outcome is given by a bi-stochastic matrix X = (xij)i,j=1..n, with xij representing the probability that player i receives item j. By Birkhoff–von Neumann theorem, X can be implemented as a lottery over assignments.

An important solution concept in this setting was given by Hylland and Zeckhauser [HZ79]. The solution ﬁts within the broader competitive equilibrium from equal incomes (CEEI) framework. In the HZ scheme, each player is given 1 unit of token endowment. Each item is given a price Cj, and each player i is given a bundle xij with j xij = 1, xij ≥ 0. The outcome is a competitive equilibrium if

- 1. all items get allocated: i xij = 1 for all j;
- 2. each player i stays within her budget: j Cj · xij ≤ 1; and
- 3. each player receives her favorite bundle among the ones she can afford: for each i, and for each yij ≥ 0 with j yij = 1 and j Cj · yij ≤ 1,


j

uij · yij ≤

j

uij · xij. (29)

Existence of a price vector C inducing a CE follows from general ﬁxed-point results. The price vector needs not be unique. It is still unknown whether such prices can be computed efﬁciently in general30. The mechanism induced by a HZ scheme needs not be truthful, although in large markets truthfulness does emerge [Bud11].

The output of Algorithm 1 when players have vanishing strong regret is a competitive equilibrium allocating items using a token system. It is therefore natural to ask whether there is a correspondence between CEs induced by Algorithm 1 and HZ equilibria. To be speciﬁc, we will distinguish two versions of Algorithm 1. The non-regularized version just runs a unit-demand VCG at every step. The regularized version adds a concave regularizer to the process.

- 3.2.1 Not all HZ equilibria correspond to VCG-competitive equilibria


A non-regularized version of Algorithm 1 is just a repeated run of unit-demand VCG auction using tokens, where the bid of player i at time t takes the form λi,t · ui. In a competitive equilibrium, the sum of these runs would exhaust the token endowment of all players, except those who always get their favorite item. We start mapping out the relationship between these equilibria and HZ equilibria by showing that there exist HZ equilibria that do not correspond to a combination of VCGs.

Consider the following setting with 4 players and 4 items.

![image 57](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile57.png>)

30Moreover, an approximate competitive equilibrium may be easier to attain than an exact one. See [VY20] for a recent discussion on computational complexity questions.

![image 58](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile58.png>)

A B C D

![image 59](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile59.png>)

- u1 11 9 14 0

![image 60](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile60.png>)

- u2 11 9 14 0

![image 61](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile61.png>)

- u3 0 0 10 0

![image 62](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile62.png>)

- u4 0 0 10 0


![image 63](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile63.png>)

The following prices P1 and allocation x form a HZ equilibrium:

![image 64](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile64.png>)

A B C D P1 1.1 0.9 2 0 x1 0.5 0.5 0 0 x2 0.5 0.5 0 0 x3 0 0 0.5 0.5 x4 0 0 0.5 0.5

![image 65](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile65.png>)

![image 66](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile66.png>)

![image 67](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile67.png>)

![image 68](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile68.png>)

![image 69](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile69.png>)

![image 70](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile70.png>)

![image 71](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile71.png>)

We claim that there is no distribution on tuples of the form (λ1, λ2, λ3, λ4), such that the allocation x is the result of running VCG on utilities (λ1u1, λ2u2, λ3u3, λ4u4), and the payments due from each player average out to 1. To see this, let (λ1, λ2, λ3, λ4) be a tuple in the support. Without loss of generality, suppose the resulting allocation is (A → 1; B → 2; C → 3; D → 4) (the argument in symmetric for the other three possible allocations). The following conditions hold for the λ’s by the optimality of the allocation:

 

λ1 ≥ λ2 λ3 ≥ λ4



11λ1 + 9λ2 + 10λ3 ≥ 14λ1 + 11λ2

Next, let us compute the externalities. The price accruing to player 1 is C1 = 2λ2. The price accruing to players 2 and 4 is C2 = C4 = 0. The price accruing to player 3 is C3(14λ1 + 11λ2) − (11λ1 + 9λ2) = 3λ1 + 2λ2.

We see that C3 + C4 ≥ C1 + C2, with equality only when C1 = C2 = 0. Therefore, there cannot be a distribution over λ’s where C1 + C2 and C3 + C4 both average out to 2.

There is a different HZ competitive equilibrium allocation y, given below, supported by prices P2 that do come from a distribution of VCG allocations.

![image 72](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile72.png>)

A B C D P2 8/7 0 20/7 0

![image 73](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile73.png>)

![image 74](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile74.png>)

![image 75](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile75.png>)

- y1 1/2 7/20 3/20 0

![image 76](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile76.png>)

- y2 1/2 7/20 3/20 0

![image 77](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile77.png>)

- y3 0 3/20 7/20 1/2

![image 78](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile78.png>)

- y4 0 3/20 7/20 1/2


![image 79](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile79.png>)

Consider the weights λ1 = λ2 = 4/7, λ3 = λ4 = 2/7, resulting in scaled utilities:

![image 80](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile80.png>)

A B C D λ1u1 44/7 36/7 56/7 0 λ2u2 44/7 36/7 56/7 0 λ3u3 0 0 20/7 0 λ4u4 0 0 20/7 0

![image 81](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile81.png>)

![image 82](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile82.png>)

![image 83](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile83.png>)

![image 84](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile84.png>)

![image 85](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile85.png>)

Allocation y can be represented as a combination of 4 permutations, each with total utility 100/7, and VCG payments given by the following table:

![image 86](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile86.png>)

weight\player 1 2 3 4

![image 87](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile87.png>)

- 7/20 A B C D

![image 88](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile88.png>)

VCG payment 8/7 0 20/7 0

![image 89](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile89.png>)

- 7/20 B A D C


![image 90](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile90.png>)

![image 91](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile91.png>)

VCG payment 0 8/7 0 20/7

![image 92](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile92.png>)

3/20 C A B D VCG payment 20/7 8/7 0 0

![image 93](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile93.png>)

![image 94](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile94.png>)

3/20 A C D B VCG payment 8/7 20/7 0 0

![image 95](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile95.png>)

- 3.2.2 All preference proﬁles admit a VCG competitive equilibrium


Let U = {uij}i,j=1..n be a matrix utilities with uij ≥ 0. Our goal will be to prove the following theorem, which asserts that it is possible to obtain a competitive HZ equilibrium for the allocation problem with utilities U, where the prices are VCG prices supported by utilities of the form λiui for λi ≥ 0. This gives a more reﬁned version of the main result in [HZ79]. To make extensions and generalizations easier we only use Brouwer’s ﬁxed-point theorem (and not the more general Kakutani’s theorem as in the original proof).

Note that while Theorem 5 was found using the APEX framework, it is proven directly without relying on any convergence assumptions. Later, in Theorem 13 we will show that a convergent low-regret execution of APEX on a (regularized) allocation optimizer gives a constructive way of ﬁnding approximate HZ prices31.

Theorem 5. Let U = {uij}i,j=1..n be a matrix utilities with uij ≥ 0. Then there exist numbers λi ≥ 0, prices C = {Cj} and an allocation X = {xij} with the following properties.

- 1. X is a valid allocation: ∀j : i xij = 1 and ∀i : j xij = 1;
- 2. Cj are the VCG prices for utilities given by u′ij = λiuij;32


![image 96](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile96.png>)

- 31This does not quite resolve the problem of computing a HZ competitive equilibrium efﬁciently, because there are no general low-regret algorithms for BwK. It remains to be seen whether low-regret algorithms with good convergence properties can be found for the speciﬁc setting corresponding to one-sided allocation.
- 32Recall that for VCG for unit-demand allocation, the payment accruing to player i depends only on the item j she receives, and that if there are multiple optimal solutions, in all of them, the same item j will be sold for the same price Cj.


- 3. X is a combination of optimal allocations under u′: for every π : [n] → [n] with ∀i xiπ(i) > 0 we have

i

u′iπ(i) = max

σ

i

u′iσ(i).

- 4. The players can purchase their allocations with budget not exceeding 1. For each player i,

j

Cjxij ≤ 1.

- 5. Prices Cj and allocation X form a HZ equilibrium. That is, for every player i


j

u′ijxij = max y : j

Cjyj ≤ 1 j yj = 1

j

u′ijyj.

Proof. Without loss of generality we can scale the problem so that uij ∈ [0, 1]. Fix a parameter ε > 0 (we will later take ε → 0). For a vector of λ with λi ≥ 0, deﬁne the following function Φε(λ):

Φε(λ)i :=

[Payment due from player i in V CG(λ′1u1, . . ., λ′nun)].

E

(λ′1,...,λ′n)∼U[λ1,λ1+ε]×[λ2,λ2+ε]×...×[λn,λn+ε]

Here V CG(v1, . . ., vn) denotes the unit-demand VCG mechanism with given valuations. Denote the following adjustment mapping Ψε from the space of λ’s to itself:

Ψε(λ)i := min max(0, λi + (1 − Φε(λ)i)), λ¯ , where

n mini,j

λ¯ := 1 +

.

![image 97](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile97.png>)

1,j1:uij1 =uij2 |uij

1 − uij

2|

In other words, we adjust λi by adding (1 − Φε(λ)i) to it, so that if player i pays more than 1, λi gets decreased, and if she pays less than 1, λi gets increased. We then snap it to the interval [0, λ¯] if the adjustment causes λi to escape this interval, where λ¯ is chosen to be sufﬁciently large.

Consider a λ in the closed, convex set M := [0, λ¯]n. On this set Ψε(λ)i is bounded by λ¯. When we vary λi by δ ≪ ε, the distribution under the expectation in Φε(λ)j only varies by δε in statistical distance, and thus Φε(λ)j changes by at most δε·λ¯, and Ψε(λ) also changes by at most δ·λ¯

![image 98](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile98.png>)

![image 99](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile99.png>)

ε in each coordinate. Therefore, Ψε(λ) is a continuous mapping from M to itself, and by the Brouwer ﬁxed-point theorem it admits a ﬁxed point λε such that

![image 100](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile100.png>)

Ψε(λε) = λε.

Each λε induces an allocation Xε and prices Cε on items given by considering the expected allocation and expected VCG prices for λ sampled uniformly from [λε1, λε1 + ε] × [λε2, λε2 + ε] ×

. . . × [λεn, λεn + ε]. The allocations Xε belong to the compact region of bi-stochastic matrices in [0, 1]n×n by deﬁnition.

The prices Cjε are non-negative. We claim that they are also uniformly bounded. Note that

j

Cjε =

i

Φε(λε)i,

therefore, it sufﬁces to show that Φε(λε)i are uniformly bounded for each i. Note that whenever Φε(λε)i > 1, our assumption that

Ψε(λε)i = λεi implies λεi = 0, which in turn implies that Φε(λε)i ≤ ε. For ε < 1 this implies

Φε(λε)i ≤ 1 (30) for all i, and Cjε ≤ n for all j.

Thus the points Xε, λε and Cε belong to compact sets. Thus the sequence {(X1/k, C1/k, λ1/k)}k=1..∞ contains a converging subsequence.

More precisely, we get a sequence εk → 0 such that lim

Xε

=: X;

k

k→∞

Cε

=: C; and

lim

k

k→∞

λε

=: λ, We claim that X, C, and λ satisfy the conditions of the theorem. The ﬁrst condition in the theorem holds because Xεk

lim

k

k→∞

is a valid allocation for each k, and thus the limit is also a valid allocation.

When (λ′1, . . ., λ′n) varies within [λ1, λ1 +ε]×[λ2, λ2 +ε]×. . .×[λn, λn+ε], item prices vary by at most εn. Therefore, whenever Xijε > 0, the amount player i pays per unit of j on average differs from Cjε by at most εn. Hence

Φε(λε)i −

j

Xijε · Cjε ≤ εn. (31)

By (30) this implies

Xijε · Cjε ≤ 1 + εn. By taking the limit over Xε

j

and Cε

, we get

k

k

j

Xij · Cj ≤ 1,

for all i, implying the fourth condition of the theorem.

The second and third conditions follow from the fact that the optimal value attainable by an allocation is uniformly continuous in the vector λ. One characterization of the VCG prices Cj is the difference between the optimal utility attainable when two copies of item j are available, vs. the utility when only a single copy is available. By this characterization, whenever λεk

→ λ, the VCG prices corresponding to any λ′ ∈ [λε

1 , λε

1 + εk] × [λε

2 , λε

2 + εk] × . . . × [λε

nk, λε

nk + εk] will uniformly (in εk) converge to VCG prices corresponding to λ. Thus, Cεk

k

k

k

k

converge to VCG prices corresponding to λ — implying that C gives us the prices corresponding to VCG on (λiui).

Similarly, if π is a permutation such that Xiπ(i) > δ for all i and some δ > 0, then for all sufﬁciently large k

Xε

iπ(i) > 0, which implies

k

λε

λε

i uiπ(i) > max

i uiσ(i) − 2nεk.

k

k

σ

i

Taking k → ∞, this implies i λiuiπ(i) ≥ maxσ i λiuiσ(i).

Taken together, the ﬁrst four properties imply that X is a viable VCG outcome for utilities u′i = λiui, supported by prices Cj.

To establish the ﬁfth property, we consider players i who exhaust their budgets ( j CjXij = 1), and those who don’t exhaust ( j CjXij < 1) separately.

By the envy-freeness of VCG, players who pay 1 unit cannot obtain a better bundle for one unit, which is exactly what the ﬁfth property asserts. If a player i pays strictly less than 1 unit,

(λεk)i < 1. By the ﬁxed point property, this means that λε

- then by (31) for all sufﬁciently large k, Φε


k

i = λ¯, and thus λi = λ¯. We ﬁnish the proof by claiming that whenever λi = λ¯, the VCG unit-demand mechanism corresponding to (u′t)nt=1 = (λtut)nt=1 will always allocate player i her favorite items only, making the ﬁfth property hold automatically.

k

- Claim 6. Suppose λi = λ¯, then for all j with Xij > 0,


uiℓ =: u∗i.

uij = max

ℓ

In other words, a player i with λi = λ¯ only gets allocated her favorite item(s).

Proof of Claim 6. Suppose Xij > 0 for some j with uij < uiℓ = u∗i. Every allocation under VCG is envy-free. Therefore, whenever player i is allocated item j under X, whoever is allocated item

ℓ pays at least λi ·(u∗i −uij) for the item, and thus the cost of item ℓ is at least Cℓ ≥ λi ·(u∗i −uij). Therefore, by (30),

n ≥

q

Cq ≥ Cℓ ≥ λi · (u∗i − uij) = λ¯ · (u∗i − uij) > n,

contradiction.

![image 101](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile101.png>)

![image 102](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile102.png>)

![image 103](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile103.png>)

![image 104](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile104.png>)

![image 105](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile105.png>)

![image 106](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile106.png>)

![image 107](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile107.png>)

![image 108](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile108.png>)

- 3.2.3 Not all no-regret repeated VCG executions correspond to a HZ equilibrium


One way to interpret Theorem 5 is that in the setting of allocation with cardinal preferences, there is always a competitive equilibrium in the sense of Hylland and Zeckhauser that is supported by weights λ and a (combination of) VCG executions on utilities u′i = λiui. If we initialized Algorithm 1 to weights λi, and ran it without a regularizer, using time to alternate between the permutations that make up X, we would obtain a valid execution of the algorithm corresponding

- to outcome X. The strong no-regret property in this case follows directly from the truthfulness of VCG.


It is reasonable to ask whether all valid (i.e. low strong-regret) executions of repeated VCG — corresponding to running Algorithm 1 without a regularizer — lead to an (approximate) HZ competitive equilibrium. The following examples shows that the answer is ‘no’. The example is somewhat pathological, but is illuminating nonetheless.

Consider the following simple setting with just two players and two items. A B

![image 109](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile109.png>)

![image 110](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile110.png>)

- u1 1 0

![image 111](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile111.png>)

- u2 1 0


![image 112](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile112.png>)

Both players (equally) prefer item A to item B. Any allocation coming from a HZ competitive equilibrium33 would divide the items equally among the two players.

Consider the following submissions of λ1,t and λ2,t to Algorithm 1: t 1 2 3 4 5 6 7 8 9 . . .

![image 113](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile113.png>)

![image 114](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile114.png>)

- λ1,t 3 3 3 3 3 3 3 3 3 . . .

![image 115](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile115.png>)

- λ2,t 4 1.5 1.5 4 1.5 1.5 4 1.5 1.5 . . .


(32)

![image 116](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile116.png>)

During the execution, player 1 receives item A during times t = 3i + 2 and t = 3i + 3 for i ≥ 0. Whenever this happens, player 1 pays 1.5 units, which averages to 1 unit per time step. Player 2 receives item B during times t = 3i + 1 for i ≥ 0. Whenever this happens, player 2 pays 3 units, which also averages to 1 unit per time step. Thus, the allocation we end up with is:

![image 117](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile117.png>)

A B

X1 23 13 X2 13 23

![image 118](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile118.png>)

![image 119](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile119.png>)

![image 120](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile120.png>)

![image 121](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile121.png>)

![image 122](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile122.png>)

![image 123](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile123.png>)

![image 124](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile124.png>)

Such an allocation cannot be supported by a HZ equilibrium. To see that the execution (32) has the strong low-regret property, observe that player 1 has no useful deviation from playing λ1,t = 3 at every round. Suppose she deviated in a way that gives her item A during αT ≤ T/3 of the rounds in which player 2 plays 4, and βT ≤ 2T/3 of the rounds in which player 2 plays 1.5. The payment in the ﬁrst case is 4 and in the second is 1.5 for a total of (4α+1.5β)T ≤ T by the budget constraint. The utility of player 1 is at most

- 2

![image 125](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile125.png>)

- 3 · (1.5α + 1.5β) ≤


- 2

![image 126](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile126.png>)

- 3 · (4α + 1.5β) ≤


- 2

![image 127](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile127.png>)

- 3


α + β =

.

![image 128](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile128.png>)

33And, indeed, any reasonable allocation.

Player 2 has no useful deviations either. At any round where she gets item A, she has to pay 3 units, which means that she can at most get item A during T/3 rounds.

The example is quite different from the setup in the proof of Theorem 5. In the proof of Theorem 5, in all the approximate solutions, the players’ λi’s are conﬁned to a small region of size εk. In the example above, player 2’s λ2 oscillates between two very distant values. Note that while player 1 strongly prefers to not deviate from her current play, player 2 only has a weak incentive. In fact, if instead of playing (4, 1.5) the second player played (4, 2.5), her payoff would have been the same, but the game would no longer be feasible for player 1.

Even a very modest incentive to keep λ2,t’s close to each other would have ruled out this kind of example. A concave regularizer provides this kind of incentive.

- 3.2.4 Regularized VCG corresponds to an approximate HZ equilibrium


In this section we will show that a regularized execution of Algorithm 1 avoids the pathological example from previous section, and does lead to an approximate HZ equilibrium. As in other ﬁelds, such as learning and optimization, regularization sacriﬁces a small amount of efﬁciency to attain stability.

Before considering executions of “regularized VCG” in Algorithm 1, let us see what property we hope would lead to the outcome being an approximate HZ competitive equilibrium. The property we need is that for each player i the values of λi,t do not vary greatly throughout the execution. We can then deﬁne the “typical” value of λi,t to be λi, and use the VCG prices induced by the λi’s to deﬁne an approximate HZ equilibrium.

After that, we will see under what conditions low strong regret implies “λi,t do not vary greatly throughout the execution”. As we will see, this happens whenever the function mapping payment Ci,t to the utility experienced by player i at round t is smooth and strictly concave — having second derivative bounded away from 0. This is a property that fails to hold for standard VCG. In the example from Section 3.2.3 the cost/utility function for player 2 (deﬁned as “how much utility can one derive by spending an average of c units of cost) is given by

U2(c) =

c/3 when c ≤ 3 1 when c > 3

The function U2 is neither smooth — its derivative drops from 1/3 to 0, nor strictly concave — it is linear on the interval [0, 3]. This causes player 2 to be indifferent among all the λ2’s in (0, 3) and among all λ2’s in (3, ∞), and makes a solution where player 2 alternates between {1.5, 4}, as opposed to alternating between {3 − ε, 3 + ε} a low-regret solution for player 2.

The role of regularization. Next, we will see how regularization yields an approximate HZequilibrium.

Rather than try to give a general implication, we will work out an example of one speciﬁc regularizer, to show that low strong-regret executions with this regularizer correspond to approximate HZ equilibria. It should be noted that regularizers in general reduce the efﬁciency of the mechanism, since adding a “utility function” for the principal necessarily reduces the utility of players.

The main theorem of the section states that a valid execution of Algorithm 1 with regularization indeed leads to an approximate HZ-equilibrium supported by VCG prices. The proof is not technically deep but requires careful calculations which we defer to Appendix B.

Theorem 13. [restated] In the unit-demand allocation setting without money with n players and n items, let {uij} be utilities such that uij ∈ [0, 1], and for each i, minj uij = 0 and maxj uij = 1.

For each δ > 0, there are β = (δ/n)O(1), ε = (δ/n)O(1), and λ¯ = O(1/δ), such that if we use the concave regularizer

F0(x) :=

−β/xij ≤ 0,

ij

the following holds.

Consider an execution of Algorithm 1, with λi,t ∈ [0, λ¯]. Suppose that each player has strong regret < ε · T. Let x be the resulting allocation.

Let λi be the best response for each player i to the observed sequence of actions. Let Cj be VCG prices corresponding to utilities {λiuij}.

Then x is a δ-competitive equilibrium at budgets 1 supported by prices Cj′ = (1 − δ) · Cj.

### 3.3 Two-sided matching

The third important application of mechanisms without money is that of two-sided matching. The most famous algorithm is this area is the Gale-Shapley deferred acceptance algorithm for stable matching. A pair of players form a blocking pair for a matching M if they are not matched to each other under M, but prefer each other to their current partners. A match M is stable if there it has no blocking pairs. Stability is a desirable property since it makes enforcing that the players follow M easy — there are no useful deviations from M that would beneﬁt all deviating players.

Stability is a notion that only depends on ordinal preferences. As with voting and one-sided matching, it is often desirable to incorporate cardinal utilities into the preference model, with the goal of attaining cardinally efﬁcient outcomes. Unfortunately, stability is generally completely incompatible with efﬁciency.

Consider the following example with n = 2. There are two hospitals h1 and h2 and two doctors d1 and d2.

Hospitals’ utilities d1 d2

![image 129](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile129.png>)

![image 130](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile130.png>)

- h1 9 10

![image 131](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile131.png>)

- h2 0 9


![image 132](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile132.png>)

Doctors’ utilities

![image 133](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile133.png>)

h1 h2 d1 9 0 d2 10 9

![image 134](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile134.png>)

![image 135](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile135.png>)

![image 136](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile136.png>)

(33)

The only stable matching in (33) is M1 := {(h1, d2), (h2, d1)}, since otherwise (h1, d2) would form a blocking pair. The total utility of such a matching is 20, while the utility of matching M2 := {(h1, d1), (h2, d2)} is 36. This is because even though (h1, d2) form a blocking pair for M2, they are almost indifferent between the two matchings, while the other two participants strongly prefer M2 to M1.

Introducing money transfers can help address the efﬁciency problem34. Without money, it is generally unknown how to achieve efﬁciency and truthfulness. As in other settings without money, the solution concept has to be invariant to scaling players’ utilities, which means that only a sum of scaled utilities can be maximized — the outcome should be invariant to scaling and shifting of individuals’ entire utility vectors. Thus (33) becomes

Hospitals’ utilities d1 d2

![image 137](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile137.png>)

![image 138](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile138.png>)

- h1 0 1

![image 139](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile139.png>)

- h2 0 1


![image 140](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile140.png>)

Doctors’ utilities

![image 141](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile141.png>)

h1 h2 d1 1 0 d2 1 0

![image 142](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile142.png>)

![image 143](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile143.png>)

![image 144](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile144.png>)

(34)

We see that h1 and d2 are the desirable participants. Under a stable match, they will be matched to each other, even though M1 and M2 have the same total utility.

Applying Algorithm 1 to (34) would lead to assigning the same weight λi = 1 to all participants, and to an outcome µ := 12 · M1 + 12 · M2.

![image 145](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile145.png>)

![image 146](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile146.png>)

To see that the externalities are indeed equalized, note that h1 and d2 prefer M1 and h2 and d1

prefer M2. Under µ the total utility of players h1, h2, d1 is 23. If we ignored the preferences of (say) d2, then µ would be replaced with M2 with probability 1. The total utility of players h1, h2, d1

![image 147](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile147.png>)

under M2 is 2. Thus d2 causes 12 unit of externality on other players. This calculation can be repeated to see that each player’s externality is 12, showing that µ indeed equalizes externalities across players.

![image 148](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile148.png>)

![image 149](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile149.png>)

Is desirability treated as an endowment? In the example above there is a signiﬁcant difference between the uniform distribution that Algorithm 1 outputs and the single stable matching M1 in which the more desirable hospital matches to the more desirable doctor. This example can be expanded to a setting with n > 2, where the contrast is even more stark. Consider the most straightforward setting where each doctor derives utility i from hospital hi and each hospital derives utility i from doctor di. Thus all participants agree on the ranking h1 ≺ h2 ≺ . . . ≺ hn and d1 ≺ d2 ≺ . . . ≺ dn.

The only stable matching in this case is the assortative a := {(hi, di)}ni=1 matching. This is easy to see by induction: in a stable match (hn, dn) must be together, otherwise they will form a blocking pair. Assuming (hn, dn) are matched to each other, (hn−1, dn−1) will form a blocking pair unless they are matched to each other, and so on.

Under Algorithm 1, all preferences are the same, and by symmetry, in the resulting distribution35, each pair (hi, dj) will appear with equal probability n1.

![image 150](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile150.png>)

We believe that both outcomes give meaningful solutions under very different solution concepts. A deeper investigation of the solution concept given by Algorithm 1 will need to be deferred to future work, but we can offer some preliminary comments here.

The stark difference between the two outcomes can be traced to how the desirability is treated by the mechanism. Under Algorithm 1 the desirability of hn is just part of the input landscape.

![image 151](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile151.png>)

34For example, under preferences (33) h2 could pay d2 a little bit to make her prefer M2 over M1. 35There are many ways to implement such distribution — the algorithm only speciﬁes the ex-ante marginal proba-

bilities of pairs (hi,dj).

The “beneﬁt” from hn being so desirable doesn’t accrue to hn, and thus hn gets the same outcome as the least desirable hospital h1. Put differently, Algorithm 1 measures the (negative) externality caused by hn having preferences, but not the (positive) externality caused by hn being present.

On the other hand, when we say that (hn, dn) are a blocking pair, it is implied that hn’s and dn’s desirability accrue to them, and they can internalize them by matching with each other.

There are variants with Hylland-Zeckhauser with endowments [EMZ19a, EMZ19b, GTV20], and it is possible to adapt Algorithm 1 to treat desirability as an endowment and to give match participants credit for being desirable. It is also possible to create a hybrid approach, where the match is partially redistributive, for example ﬁnding a solution with lowest level of inequality among externalities subject to (inequality-promoting) stability constraints. We leave investigating these adaptations to future works.

## References

[AD14] Shipra Agrawal and Nikhil R Devanur. Fast algorithms for online stochastic convex programming. In Proceedings of the twenty-sixth annual ACM-SIAM symposium on Discrete algorithms, pages 1405–1424. SIAM, 2014.

[AD19] Shipra Agrawal and Nikhil R Devanur. Bandits with global convex constraints and objective. Operations Research, 67(5):1486–1502, 2019.

[AM+06] Lawrence M Ausubel, Paul Milgrom, et al. The lovely but lonely vickrey auction. Combinatorial auctions, 17:22–26, 2006.

- [BKS13a] Moshe Babaioff, Robert Kleinberg, and Aleksandrs Slivkins. Multi-parameter mechanisms with implicit payment computation. In Proceedings of the fourteenth ACM conference on Electronic commerce, pages 35–52, 2013.
- [BKS13b] Ashwinkumar Badanidiyuru, Robert Kleinberg, and Aleksandrs Slivkins. Bandits with knapsacks. In 2013 IEEE 54th Annual Symposium on Foundations of Computer Science, pages 207–216. IEEE, 2013.


[BM07] Avrim Blum and Yishay Mansour. From external to internal regret. Journal of Machine Learning Research, 8(Jun):1307–1324, 2007.

[BMSW19] Mark Braverman, Jieming Mao, Jon Schneider, and S Matthew Weinberg. Multiarmed bandit problems with strategic arms. In Conference on Learning Theory, pages 383–416. PMLR, 2019.

[Bud11] Eric Budish. The combinatorial assignment problem: Approximate competitive equilibrium from equal incomes. Journal of Political Economy, 119(6):1061–1103, 2011.

[CD06] Xi Chen and Xiaotie Deng. Settling the complexity of two-player nash equilibrium. In 2006 47th Annual IEEE Symposium on Foundations of Computer Science (FOCS’06), pages 261–272. IEEE, 2006.

[CS08] Vincent Conitzer and Tuomas Sandholm. New complexity results about nash equilibria. Games and Economic Behavior, 63(2):621–641, 2008.

[DGP09] Constantinos Daskalakis, Paul W Goldberg, and Christos H Papadimitriou. The complexity of computing a nash equilibrium. SIAM Journal on Computing, 39(1):195– 259, 2009.

[DH09] Nikhil R Devanur and Thomas P Hayes. The adwords problem: online keyword matching with budgeted bidders under random permutations. In Proceedings of the 10th ACM conference on Electronic commerce, pages 71–78, 2009.

[DJSW19] Nikhil R Devanur, Kamal Jain, Balasubramanian Sivan, and Christopher A Wilkens. Near optimal online algorithms and fast approximation algorithms for resource allocation problems. Journal of the ACM (JACM), 66(1):1–41, 2019.

[DSS19] Yuan Deng, Jon Schneider, and Balusubramanian Sivan. Strategizing against noregret learners. arXiv preprint arXiv:1909.13861, 2019.

- [EMZ19a] Federico Echenique, Antonio Miralles, and Jun Zhang. Constrained pseudo-market equilibrium. arXiv preprint arXiv:1909.05986, 2019.
- [EMZ19b] Federico Echenique, Antonio Miralles, and Jun Zhang. Fairness and efﬁciency for probabilistic allocations with endowments. arXiv preprint arXiv:1908.04336, 2019.


[FPX20] Zhe Feng, David Parkes, and Haifeng Xu. The intrinsic robustness of stochastic bandits to strategic manipulation. In International Conference on Machine Learning, pages 3092–3101. PMLR, 2020.

[Gib73] Allan Gibbard. Manipulation of voting schemes: a general result. Econometrica: journal of the Econometric Society, pages 587–601, 1973.

[Gib78] Allan Gibbard. Straightforwardness of game forms with lotteries as outcomes. Econometrica: Journal of the Econometric Society, pages 595–614, 1978.

[GTV20] Jugal Garg, Thorben Tr¨obst, and Vijay V Vazirani. An Arrow-Debreu extension of the Hylland-Zeckhauser scheme: Equilibrium existence and algorithms. arXiv preprint arXiv:2009.10320, 2020.

[Haz19] Elad Hazan. Introduction to online convex optimization. arXiv preprint arXiv:1909.05207, 2019.

[HMPY18] Yinghua He, Antonio Miralles, Marek Pycia, and Jianye Yan. A pseudo-market approach to allocation with priorities. American Economic Journal: Microeconomics, 10(3):272–314, 2018.

[Hyl80] Aanund Hylland. Strategy proofness of voting procedures with lotteries as outcomes and inﬁnite sets of strategies. Unpublished paper, University of Oslo.[341, 349], 1980.

[HZ79] Aanund Hylland and Richard Zeckhauser. The efﬁcient allocation of individuals to positions. Journal of Political economy, 87(2):293–314, 1979.

[ILWM17] Nicole Immorlica, Brendan Lucier, Glen Weyl, and Joshua Mollner. Approximate efﬁciency in matching markets. In International Conference on Web and Internet Economics, pages 252–265. Springer, 2017.

[IPW19] Nicole Immorlica, Ben Plaut, and E Glen Weyl. Equality of power and fair public decision-making. Available at SSRN 3420450, 2019.

[ISSS19] Nicole Immorlica, Karthik Abinav Sankararaman, Robert Schapire, and Aleksandrs Slivkins. Adversarial bandits with knapsacks. In 2019 IEEE 60th Annual Symposium on Foundations of Computer Science (FOCS), pages 202–219. IEEE, 2019.

[KGJS20] Kirthevasan Kandasamy, Joseph E Gonzalez, Michael I Jordan, and Ion Stoica. Mechanism design with bandit feedback. arXiv preprint arXiv:2004.08924, 2020.

[Leo83] Herman B Leonard. Elicitation of honest preferences for the assignment of individuals to positions. Journal of political Economy, 91(3):461–479, 1983.

[LMM03] Richard J Lipton, Evangelos Markakis, and Aranyak Mehta. Playing large games using simple strategies. In Proceedings of the 4th ACM Conference on Electronic Commerce, pages 36–41, 2003.

[LPSV07] Se´bastien Lahaie, David M Pennock, Amin Saberi, and Rakesh V Vohra. Sponsored search auctions. Algorithmic game theory, 1:699–716, 2007.

[LS20] Tor Lattimore and Csaba Szepesva´ri. Bandit algorithms. Cambridge University Press, 2020.

[LW18] Steven P Lalley and E Glen Weyl. Quadratic voting: How mechanism design can radicalize democracy. In AEA Papers and Proceedings, volume 108, pages 33–37, 2018.

[NRTV07] Noam Nisan, Tim Roughgarden, Eva´ Tardos, and Vijay V. Vazirani. Algorithmic Game Theory. Cambridge University Press, New York, NY, USA, 2007.

[NSV08] Hamid Nazerzadeh, Amin Saberi, and Rakesh Vohra. Dynamic cost-per-action mechanisms and applications to online advertising. In Proceedings of the 17th international conference on World Wide Web, pages 179–188, 2008.

[Rot07] Michael H Rothkopf. Thirteen reasons why the Vickrey-Clarke-Groves process is not practical. Operations Research, 55(2):191–197, 2007.

[Rou16] Tim Roughgarden. Twenty lectures on algorithmic game theory. Cambridge University Press, 2016.

[Sat75] Mark Allen Satterthwaite. Strategy-proofness and Arrow’s conditions: Existence and correspondence theorems for voting procedures and social welfare functions. Journal of economic theory, 10(2):187–217, 1975.

[Sli19] Aleksandrs Slivkins. Introduction to multi-armed bandits. arXiv preprint arXiv:1904.07272, 2019.

[Sto05] Gilles Stoltz. Incomplete information and internal regret in prediction of individual sequences. PhD thesis, Universite´ Paris Sud-Paris XI, 2005.

[VY20] Vijay V Vazirani and Mihalis Yannakakis. Computational complexity of the Hylland-Zeckhauser scheme for one-sided matching markets. arXiv preprint arXiv:2004.01348, 2020.

## A Properties of unit-demand VCG

In this section we summarize some useful properties of unit-demand VCG. A detailed discussion on the properties of unit-demand VCG can be found e.g. in [Leo83].

Notation. Suppose there are n players and n items. Player i has utility uij ∈ [0, 1] for item j. Let OPT denote the maximum utility attainable by a permutation.

OPT := max

π:[n]֒→[n]

i

uiπ(i).

Let

OPT+j := max

π:[n]֒→[n]∪{j′}

i

uiπ(i),

where uij′ := uij, be the maximum attainable utility if a second copy of item j becomes available.

The optimization problem can be made convex by replacing the permutation with bi-stochastic matrices. Bi-stochastic matrices correspond to distributions over permutations. Thus, one gets a linear program:   

maximize ij uijxij subject to:

- ∀i j xij ≤ 1
- ∀j i xij ≤ 1


(35)

The dual to (35) ﬁnds variables ai and bj such that

∀i, j uij ≤ ai + bj, (36) where equality holds whenever the in the optimal solution x∗, x∗ij > 0. Thus

OPT =

i

ai +

j

bj.

VCG prices. We state some properties of VCG prices.

- Claim 7. 1. Item price independent of receiver. Whenever there are multiple optimal solutions, the same item j is sold for the same price Cj — the VCG price of j.


- 2. Item price is beneﬁt from a second copy. This price is equal to OPT+j − OPT — the extra welfare from having another copy of j.
- 3. Prices as dual variables. Let π be an optimal allocation. Deﬁne bj := Cj, ai := uiπ(i) − Ci.

Then π with prices Cj results in an envy-free allocation — equivalently, {ai}, {bj} form a valid solution for the dual program (36).

- 4. Fractional augmentation. Let y be an allocation vector with yj ≥ 0, j yj ≤ 1. Let OPT+y be the value of an optimal allocation where the amount of each item j available is 1 + yj rather than 1. Then

OPT+y = OPT +

j

yjCj. (37)

- 5. Continuity of prices in utilities. Let uij ≥ 0 and u˜ij be two sets of utilities. Let Cj and C˜j be the corresponding V CG prices. Then for all j,


|Cj − C˜j| ≤ 2 ·

i

ui − u˜i ∞ = 2 ·

i

max

|uij − u˜ij|. (38)

j

Proof. The ﬁrst three statements are standard properties of unit-demand VCG.

For the fractional augmentation property, we will prove an inequality in both directions to obtain equality. Let x be an optimal allocation realizing OPT. Let x+j be an allocation realizing OPT+j, thus

x+iℓjuiℓ = OPT+j.

x+iℓj ≤ 1 + 1ℓ=j and

∀ℓ

i

iℓ

Consider x˜ := (1 − j yj) · x + j(yj · x+j). Then each player is allocated a total of one unit under x˜. We have

yj · 1j=ℓ = 1 + yj,

x˜iℓ ≤ 1 +

∀ℓ

j

i

making x˜ a feasible solution for OPT+y. We have

ij

x˜ijuij = (1 −

j

yj) · OPT +

j

yjOPT+j = OPT +

j

yjCj.

Thus OPT+y ≥ OPT + j yjCj.

For the converse inequality, we have that for each i, j, uij ≤ ai + Cj, where OPT = i ai + j Cj. Let z be a solution for realizing OPT+y. We have

OPT+y =

ij

uijzij ≤

ij

(ai + Cj)zij ≤

i

ai +

j

(1 + yj)Cj = OPT +

j

yjCj.

We note that the ≤ direction of this claim continues to hold even when j yj > 1, but the inequality may no longer be tight.

For the continuity of prices in utilities property, we will prove that C˜j ≤ Cj+2· i ui−u˜i ∞. Together with the same inequality with C˜j and Cj swapped, (38) follows. Let x be a utilitymaximizing allocation under u, and let x+j be a utility-maximizing allocation under u when a second copy of item j is available. Similarly, let y and y+j be the corresponding optimal allocations under u˜. We have

C˜j =

iℓ

yiℓ+ju˜iℓ −

iℓ

yiℓu˜iℓ

≤

≤

i

i

≤ 2 ·

ui − u˜i ∞ +

ui − u˜i ∞ +

iℓ

iℓ

i

ui − u˜i ∞ +

yiℓ+juiℓ −

iℓ

x+iℓjuiℓ −

iℓ

x+iℓjuiℓ −

iℓ

= 2 ·

i

ui − u˜i ∞ + Cj,

yiℓu˜iℓ

xiℓu˜iℓ

iℓ

xiℓuiℓ

where the second inequality is by optimality of x+j and of y.

![image 152](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile152.png>)

![image 153](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile153.png>)

![image 154](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile154.png>)

![image 155](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile155.png>)

## B Proof of Theorem 13

In this section we continue the discussion from Section 3.2.4 to give a proof of Theorem 13.

Fix the setting where there are n players and n items, and utilities {uij} ∈ [0, 1]n×n. Further, by scaling and shifting, we may assume without loss of generality that for each i, maxj uij = 1 and minj uij = 0. Consider the regularizer

F0(x) :=

ij

f0(xij) ≤ 0,

where x is a (fractional) allocation, and f0 : (0, 1] → R≤0 is a real-valued function such that

- • f0(z) ≤ 0;
- • f0(z) is increasing, with limz→0+ f0(z) = −∞; and
- • f0(z) is strictly concave with f0′′(z) ≤ −γ for a parameter γ > 0


- Claim 8. Let uij ∈ [0, 1] be utilities as above. Let λi ≥ 0 be multipliers. Let xij and Cj be the allocation and prices resulting from running the VCG mechanism on utilities λiui with regularizer f0. Let M > 1 be a parameter. Denote


λi M − n2 · f0

η = η(λ) := i

![image 156](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile156.png>)

Then the following properties hold:

1 n · M

![image 157](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile157.png>)

.

- 1. Small efﬁciency loss due to regularization. Let OPT := maxπ i λiuiπ(i). Then

ij

xijλiuij ≥ OPT − η. (39)

- 2. Prices close to VCG prices. Under the regularized mechanism the payment Pi from player i satisﬁes:

Pi −

j

xijCj ≤ η. (40)

- 3. Allocation close to a competitive equilibrium at prices Cj. For any alternative bundle yij player i receives with j yij = 1,


j

yijλiuij ≤

j

xijλiuij +

j

yijCj − Pi + η. (41)

Proof. Small efﬁciency loss due to regularization: Let y be a solution realizing OPT = OPT(λ). Let e be the all-uniform allocation with eij = n1. Let y′ := (1 − 1/M)y + e/M. Then

![image 158](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile158.png>)

λi M

F0(y′) +

λiuijyij′ ≥ n2 · f0(1/(n · M)) + OPT − i

.

![image 159](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile159.png>)

ij

By the optimality of x, we have

ij

xijλiuij ≥ F0(x) +

ij

xijλiuij

λiuijyij′

≥ F0(y′) +

ij

λi M

≥ n2 · f0(1/(n · M)) + OPT − i

![image 160](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile160.png>)

= OPT − η. Denote by

OPT0(λ) = max

x

F0(x) +

ij

xijλiuij .

Then we have just shown that

OPT(λ) − η(λ) ≤ OPT0(λ) ≤ OPT(λ). (42) To show that prices are close to VCG prices, we will prove two inequalities. It is ﬁrst useful to remember some general facts about the unit-demand VCG, summarized in Claim 7. Speciﬁcally, there exist dual parameters ai (corresponding to the “welfare” of player i), such that

∀k, ℓ λk · ukℓ ≤ ak + Cℓ, with equality at an optimal allocation, and

OPT(λ) =

k

ak +

ℓ

Cℓ.

Denote by λ−i the setting where λ−k i = λk for k = i, and λ−i i = 0. We have, by deﬁnition, Pi = OPT0(λ−i) − OPT0(λ) −

xijλiuij . (43)

j

Let π be an allocation attaining OPT(λ). Then OPT(λ−i) = OPT(λ) − λiuiπ(i) + Cπ(i) =

ak +

k =i

j

Cj.

We prove (40) by proving two inequalities on Pi. Using (43), Pi ≥ OPT(λ−i) − η(λ−i) −

xkjλkukj +

k,j

j

xijλiuij

=

ak +

k =i

j

Cj − η(λ−i) −

xkjλkukj

k =i;j∈[n]

≥

ak +

k =i

j

Cj − η(λ) −

xkj(ak + Cj)

k =i;j∈[n]

Again using (43),

=

j

xijCj − η(λ).

Pi ≤ OPT(λ−i) − OPT(λ) + η(λ) +

j

=

ak +

k =i

j

Cj + η(λ) −

k

ak −

= η(λ) − ai +

≤ η(λ) − ai +

j

j

xijλiuij

xij(ai + Cj)

= η(λ) +

j

xijCj.

xijλiuij

j

Cj +

j

xijλiuij

The allocation close to a competitive equilibrium at prices Cj follows similarly. Let yij be any alternative allocation to player i with j yij = 1. Then

j

yijλiuij ≤

j

yij(ai + Cj) = ai +

j

yijCj

=

≤

j

yijCj − Pi + Pi + ai

j

yijCj − Pi + OPT(λ−i) − OPT(λ) + η(λ) +

j

xijλiuij + ai

=

j

yijCj − Pi +

j

xijλiuij + η.

![image 161](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile161.png>)

![image 162](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile162.png>)

![image 163](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile163.png>)

![image 164](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile164.png>)

Informally, the next claim shows that strict concavity of the regularizer implies strict truthfulness.

- Claim 9. Consider an execution of the regularized VCG mechanism with λi = λ, resulting in an allocation xkj and payment Pi from player i. Consider an alternative execution where λi is changed to λ′, resulting in an allocation x′kj and payment Pi′ from player i. Then


j

λiuijxij − Pi −

j

γ 2 ·

λiuijx′ij − Pi′ ≥

![image 165](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile165.png>)

k,j

|xkj − x′kj|2. (44)

Proof. Denote

We have

Ψ(x) := F0(x) +

λkukjxkj.

k,j∈[n]

j

λiuijxij − Pi −

The function Ψ is strongly concave36, with

j

λiuijx′ij − Pi′ = Ψ(x) − Ψ(x′).

∇2Ψ(x) = ∇2F0 −γ · In2. Further, since x maximizes Ψ, and thus ∇Ψ(x) = 0, we have

γ 2 ·

|xkj − x′kj|2.

Ψ(x) − Ψ(x′) ≥

![image 166](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile166.png>)

k,j

![image 167](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile167.png>)

![image 168](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile168.png>)

![image 169](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile169.png>)

![image 170](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile170.png>)

![image 171](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile171.png>)

36This is where we use the regularizer — without it the function is merely concave, potentially with regions where the gradient is constant 0.

Consider an execution {λi,t}Tt=1 of the algorithm with low strong regret. Regularization on its own is not enough to force λi,t’s to not grow to ∞ — pathological examples can be constructed with arbitrarily large λi,t’s. Instead we limit the game space to λi,t ∈ [0, λ¯]. Here λ¯ is a parameter (on which the function f0 may depend). As in the proof of Theorem 5, for large enough λ¯, if the limitation of λi,t ≤ λ¯ becomes relevant, then player i gets allocated (close to) her favorite bundle, and the competitive equilibrium condition will hold automatically.

We will show that for a reasonably chosen f0, and for a large enough T = nO(1), a low strong regret solution translates into an approximate HZ equilibrium based on VCG prices. Our goal will be to streamline the proof — almost certainly the upper bound we get on T can be tightened to a lower power of n.

There is a unique best-response λi.

- Claim 10. Fix {λi,t}Tt=1. Fix a t and an i, and consider the payment Pi,t(λt) and utility Ui,t(λt) experienced in round t by player i if she reports λi instead of λi,t. Let λ˜t be a best response maximizing t Ui,t(λt) subject to t Pi,t(λt) ≤ T. Then


- 1. Pi,t(λt) is strictly increasing for λt ≥ 0;
- 2. Pi,t(λt) is continuous in λt;
- 3. Pi,t(0) = 0 and limλ

t→∞ Pi,t = ∞;

- 4. there is a utility maximizer for player i of the form λ˜t = λi for all t;
- 5. λi > 1; and
- 6. it is the unique maximizer.


Proof. Fix a round t ∈ [T]. Let

Ψλ(x) :=

k =i j

λk,tukjxkj +

j

λuijxij + F0(x).

Ψλ(x) is strictly concave, and tends to −∞ on the boundary where xkj = 0 for some k, j. Thus it has a unique maximizer in the interior. Denote it by X(λ). Further, note that if λ′ = λ, then

∇Ψλ′(X(λ)) = ∇Ψλ(X(λ)) + (λ′ − λ)ui = (λ′ − λ)ui = 0. Therefore X(λ′) = X(λ).

We have

Ui,t(λ) =

uijX(λ)ij.

j

Let X(0) be the point maximizing Ψ0(x). By deﬁnition, we have Pi,t(λ) = Ψ0(X(0)) − Ψλ(X(λ)) + λ · Ui,t(λ).

We immediately see that Pi,t(0) = 0. Moreover, if j is such that uij = 0 while uik = 1 for some other k, as λ → ∞ we will have X(λ)ij → 0, and thus F0(X(λ)) → −∞, and Pi,t(λ) → ∞.

Next, let us see that Pi,t(λ) is strictly increasing. Suppose λ′ > λ ≥ 0. We have

λ · Ui,t(λ) − Pi,t(λ) = Ψλ(X(λ)) − Ψ0(X(0))

> Ψλ(X(λ′)) − Ψ0(X(0)) = λ · Ui,t(λ′) − Pi,t(λ′). (45) Similarly,

λ′ · Ui,t(λ′) − Pi,t(λ′) = Ψλ′(X(λ′)) − Ψ0(X(0))

> Ψλ′(X(λ)) − Ψ0(X(0)) = λ′ · Ui,t(λ) − Pi,t(λ). (46) By taking λ′ · (45) + λ · (46), and noting that since λ′ > 0 the inequality remains strict, we obtain

−λ′ · Pi,t(λ) − λ · Pi,t(λ′) > −λ′ · Pi,t(λ′) − λ · Pi,t(λ), thus

(λ′ − λ) · Pi,t(λ′) > (λ′ − λ) · Pi,t(λ),

implying Pi,t(λ′) > Pi,t(λ). Similarly, taking (45) + (46) yields Ui,t(λ′) > Ui,t(λ). By strong concavity of Ψλ, the value of X(λ) varies continuously in λ. Therefore, Ui,t(λ) and

Pi,t(λ) also change continuously in λ.

We have Pi,t(λ) a continuous, non-decreasing function that starts at Pi,t(0) = 0 and tends to ∞ as λ → ∞. Therefore the function

T

Pi(λ) :=

Pi,t(λ)

t=1

also has those properties. In particular, there exists a unique λi such that

Pi(λi) = T. By plugging in λ = 0 and λ′ = 1 into (46), we get

Pi,t(1) < Ui,t(1) − Ui,t(0) ≤ 1, and thus Pi(1) < T and hence λi > 1.

The strategy λ˜t = λi is a feasible strategy. It remains to be seen that it is a utility-maximizing one — in fact, the only utility-maximizing strategy. Consider any alternative strategy λ˜t such that

t

Pi,t(λ˜t) ≤ T.

By (45) we have

λi ·

t

Ui,t(λ˜t) ≤ λi ·

≤ λi ·

= λi ·

t

t

t

Ui,t(λi) +

t

Pi,t(λ˜t) −

Ui,t(λi) + T − T =

Ui,t(λi),

t

Pi,t(λi)

where the ﬁrst inequality is strict unless λ˜t = λi for all t. We deﬁne

![image 172](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile172.png>)

![image 173](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile173.png>)

![image 174](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile174.png>)

![image 175](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile175.png>)

λi := min player i’s best response from Claim 10, λ¯ (47)

The remainder of the proof is conceptually straightforward, despite some calculations that need to be performed. Informally, any execution that has low strong regret must consist of each player i repeatedly playing λi,t that is close to its best-response value λi — the extent to which this fails to hold corresponds to the extent player i experiences strong regret. Assuming this holds the outcome is close to a repeated execution of each player playing λi. The resulting prices, by Claim 8 are close to VCG prices under preferences (λiuij), completing the picture.

From now on, we ﬁx

β xij

, as in the statement of Theorem 13, where β ≪ 1 is a parameter to be selected later.

f0(xij) := −

![image 176](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile176.png>)

- Claim 11. Fix a player i. Let λi be the best-response λ’s deﬁned in (47). Consider a round t in which all λ′k := λk,t ≤ λ¯. Let x′ and Pi′ be the resulting allocation and price charged from player


i, and let x and Pi be the resulting allocation and price when player i reports λi instead of λ′i. Then

j

λiuijxij − Pi −

j

λiuijx′ij − Pi′ ≥ (λi − λ′i)2 · Ω β2 · n−12 · λ¯−3 . (48)

Proof. Denote

Φ(x) := F0(x) +

ij

λiuijxij.

Let x be the maximizer of Φ(x). Note that x is the resulting allocation on input λ.

The fact that x maximizes Φ(x) implies that there exist am, bj, ck, and dℓ such that for all m and j,

β (xmj)2

λmumj +

= am + bj, (49) where without loss of generality (by adding a constant to all a’s and subtracting from all b’s)

![image 177](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile177.png>)

bj = 0. This implies am > 0 for all m.

Recall that λk ≤ λ¯ for all k. There exists37 a matching π such that for all k, xkπ(k) ≥ 1/n2, and thus

|ak + bπ(k)| ≤ β · n4 + λ.¯ Therefore, for all j,

bj < β · n4 + λ.¯ (50) and for some m,

am ≤ β · n4 + λ.¯ (51) We claim that for all m, j,

1/2

1 3 ·

β n4λ¯

xmj >

. (52)

![image 178](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile178.png>)

![image 179](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile179.png>)

If this is not the case, then am+bj > 8λn¯ 4, and thus by (50) am > 6λn¯ 4. Therefore bπ(m) < −4λn¯ 4. For all k we have ak + bπ(m) > 0, and thus ak > 4λn¯ 4, contradicting (51).

Let r and s be such that uir = 1 and uis = 0, and let k be arbitrary. By adding equation (49) with (i, r) and (k, s) and subtracting it with (i, s) and (k, r), we get

β x2ir

β x2is

λi − λkukr + λkuks = λiuir − λiuis − λkukr + λkuks = −

+

+

![image 180](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile180.png>)

![image 181](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile181.png>)

Repeating this process for x′ instead of x we get:

β x2kr −

β x2ks

. (53)

![image 182](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile182.png>)

![image 183](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile183.png>)

β x′2is

β x′2kr −

β x′2ks

β x′2ir

λ′i − λkukr + λkuks = λ′iuir − λ′iuis − λkukr + λkuks = −

+

+

, (54)

![image 184](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile184.png>)

![image 185](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile185.png>)

![image 186](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile186.png>)

![image 187](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile187.png>)

and thus for some m, j,

Together with (52) this implies

|λi − λ′i| 4

β x2mj −

β x′2mj ≥

. (55)

![image 188](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile188.png>)

![image 189](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile189.png>)

![image 190](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile190.png>)

|xmj − x′mj| > Ω β1/2 · n−6 · λ¯−3/2 · |λi − λ′i|. (56) By Claim 9, with γ = β, this implies (48).

![image 191](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile191.png>)

![image 192](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile192.png>)

![image 193](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile193.png>)

![image 194](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile194.png>)

- Claim 12. Let {λi,t} be a feasible execution of the regularized algorithm with λi,t ∈ [0, λ¯], such that player i experiences total strong regret < εT. Let λi be the best-response strategy for player i as described in (47). Then


|λi,t − λi| < O ε1/2 · T · λ¯2 · n6 · β−1 . (57)

t

![image 195](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile195.png>)

37By the Birkhoff-von Neumann theorem, x can be written as a convex combination of matchings. Moreover, by Caratheodory’s theorem about convex hulls, x can be written as a convex combination of at most (n − 1)2 + 1 < n2 matchings. The highest-weight matching π will appear with weight > 1/n2.

Proof. Let xt be the result obtained in round t when player i deviates to λi, and let x˜t be the original result of playing λi,t. Let Pit and P˜it be the corresponding prices.

Note that if λi = λ¯, then t Pit ≥ t

P˜it since Pit is increasing in λi and in this case λi = λ¯ ≥ λi,t. On the other hand, if λi < λ¯, then t Pit = T ≥ t

P˜it by the budget constraint.

Using Claim 11 we get the following chain of inequalities involving the regret player i experiences:

ε · T >

t j

(uijxtij − uijx˜tij)

Thus

≥ λ¯−1 ·

t j

λiuijxtij − Pit −

j

λiuijx˜tij − P˜it

≥ Ω(1) · λ¯−1 ·

(λi − λi,t)2 · β2 · n−12 · λ¯−3

t

2

≥ Ω(1) · λ¯−4 · β2 · n−12 ·

· T−1.

|λi − λi,t|

t

t

|λi − λi,t| < O ε1/2 · T · λ¯2 · n6 · β−1 .

![image 196](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile196.png>)

![image 197](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile197.png>)

![image 198](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile198.png>)

![image 199](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile199.png>)

Theorem 13. In the unit-demand allocation setting without money, let {uij} be utilities such that uij ∈ [0, 1], and for each i, minj uij = 0 and maxj uij = 1.

Consider an execution of the algorithm with regularizer f0(xij) = −λ¯−3 · n−4/xij, that is with β = λ¯−3 · n−4 and with λi,t ∈ [0, λ¯], where λ¯ > 10. Suppose that each player has strong regret < ε · T with38 ε = o λ ¯−12 · n−22 .

Let x be the resulting allocation, and Pi be the price charged to player i during the execution of the algorithm.

Let λi be the best response for each player i as in (47). Let Cj be VCG prices corresponding to utilities λiuij. Then for

δ = 10 · λ¯−1 < 1 the allocation x is a δ-competitive equilibrium at budgets 1 supported by prices Cj′ = (1−δ/3)·Cj.

![image 200](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile200.png>)

38Importantly, the bound we need on ε does not depend on T.

Proof. Applying Claim 12 to each player i and taking the sum we get

t i

|λi,t − λi| =: s · T = O ε1/2 · T · λ¯2 · n7 · β−1 = o(T · λ¯−1). (58)

We apply Claim 8 to {λi,t} for each t. Since λi,t ≤ λ¯, we can choose M = λ¯1/2 · β−1/2 · n−1 to obtain the statement with

η ≤ 2 · λ¯1/2 · n2 · β1/2 = 2 · λ¯−1. Denote

st :=

|λi,t − λi|,

i

the contribution of round t to s. Note that s = T1 t st. Let Cj,t be the VCG price of item j with utilities λi,tuij. By Claim 7 we have

![image 201](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile201.png>)

|Cj − Cj,t| ≤ 2 · st. (59) Applying (40) we get

t j

Cj′xtij ≤ (1 − δ/3) ·

t

2st +

j

Cj,t · xtij

≤ (1 − δ/3) ·

(2st + Pi,t + η)

t

= (1 − δ/3) · (2s · T + η · T + Pi) ≤ T.

Consider an alternative allocation yij such that

j

Cj′yij ≤ 1,

and thus

j

Cjyij < 1 + δ/2.

We need to bound j uijyij − j uijxij. Consider the execution of the algorithm where λi,t is replaced with λi with all other bids re-

maining λk,t. Let C˜j,t be the resulting VCG prices, x˜tkj be the resulting allocation and P˜i,t the resulting payment due from player i. We know that

t

P˜i,t ≤ T,

and that by the low strong regret condition, T−1 ·

uijx˜tij ≤

t j

j

uijxij + ε.

Moreover t P˜i,t = T unless λi = λ¯.

By condition (41) we get T ·

yijλiuij =

yijλiuij

j

t j

≤

t j

x˜tijλiuij +

t j

yijC˜j,t −

t

P˜i,t + T · η

≤ T · λi ·

j

uijxij + ελiT + T · yijCj +

t j

yij|C˜j,t − Cj| −

≤ T · λi ·

= T · λi ·

j

j

uijxij + ελiT + T · (1 + δ/2) + 2s · T −

t

P˜i,t + Tη

uijxij −

t

P˜i,t + T · (1 + δ/2 + η + ελi + 2s)

t

P˜i,t + T · η

Recall that λi ≥ 1. If λi < λ¯, then we get

1 λi · (δ/2 + η + ελi + 2s) < δ.

uijyij −

uijxij ≤

![image 202](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile202.png>)

j

j

If λi = λ¯, we can just drop the − t

P˜i,t term and divide by λi · T = λ¯ · T to get

j

uijyij −

j

uijxij ≤ ε + (1 + δ/2 + η + 2s) · λ¯−1 < ε + 2 · λ¯−1 < δ.

![image 203](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile203.png>)

![image 204](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile204.png>)

![image 205](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile205.png>)

![image 206](<2021-braverman-optimization-friendly-generic-mechanisms-with_images/imageFile206.png>)

