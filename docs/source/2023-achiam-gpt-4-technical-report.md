---
type: source
kind: paper
title: GPT-4 Technical Report
authors: OpenAI Josh Achiam, Steven Adler, S. Agarwal, L. Ahmad, Ilge Akkaya, Florencia Leoni Aleman, D. Almeida, Janko Altenschmidt, S. Altman, Shyamal Anadkat, Red Avila, Igor Babuschkin, S. Balaji, Valerie Balcom, Paul Baltescu, Haim-ing Bao, Mo Bavarian, Jeff Belgum, Irwan Bello, Jake Berdine, Gabriel Bernadett-Shapiro, Christopher Berner, Lenny Bogdonoff, O. Boiko, Made-laine Boyd, Anna-Luisa Brakman, Greg Brockman, Tim Brooks, Miles Brundage, Kevin Button, Trevor Cai, Rosie Campbell, Andrew Cann, Brittany Carey, Chelsea Carlson, Rory Carmichael, Brooke Chan, Che Chang, Fotis Chantzis, Derek Chen, Sully Chen, Ruby Chen, Jason Chen, Mark Chen, Benjamin Chess, Chester Cho, Casey Chu, Hyung Won Chung, Dave Cummings, Jeremiah Currier, Yunxing Dai, Cory Decareaux, Thomas Degry, Noah Deutsch, Damien Deville, Arka Dhar, David Dohan, Steve Dowling, Sheila Dunning, Adrien Ecoffet, Atty Eleti, Tyna Eloundou, David Farhi, L. Fedus, Niko Felix, S. Fishman, Juston Forte, Is-abella Fulford, Leo Gao, Elie Georges, C. Gibson, Vik Goel, Tarun Gogineni, Gabriel Goh, Raphael Gontijo-Lopes, J. Gordon, Morgan Grafstein, Scott Gray, Ryan Greene, Joshua Gross, S. Gu, Yufei Guo, Chris Hallacy, Jesse Han, J. Harris, Yuchen He, Mike Heaton, Johannes Heidecke, Chris Hesse, Alan Hickey, W. Hickey, P. Hoeschele, Brandon Houghton, Kenny Hsu, Shengli Hu, Xin Hu, Joost Huizinga, Shantanu Jain, Shawn Jain, Joanne Jang, Angela Jiang, R. Jiang, Haozhun Jin, Denny Jin, Shino Jomoto, Billie Jonn, Heewoo Jun, Tomer Kaftan, Lukasz Kaiser, Ali Kamali, I. Kanitscheider, N. Keskar, Tabarak Khan, Logan Kilpatrick, Jong Wook Kim, Christina Kim, Yongjik Kim, Hendrik Kirchner, J. Kiros, Matthew Knight, Daniel Kokotajlo, Lukasz Kondraciuk, Andrew Kondrich, Aris Konstantinidis, Kyle Kosic, Gretchen Krueger, Vishal Kuo, Michael Lampe, Ikai Lan, Teddy Lee, Jan Leike, Jade Leung, Daniel Levy, Chak Li, Rachel Lim, Molly Lin, Stephanie L. Lin, Ma-teusz Litwin, Theresa Lopez, Ryan Lowe, Patricia Lue, A. Makanju, Kim Malfacini, Sam Manning, Todor Markov, Yaniv Markovski, Bianca Martin, Katie Mayer, Andrew Mayne, Bob McGrew, S. McKinney, Christine McLeavey, Paul McMillan, Jake McNeil, David Medina, Aalok Mehta, Jacob Menick, Luke Metz, Andrey Mishchenko, Pamela Mishkin, Vinnie Monaco, Evan Morikawa, Daniel P. Mossing, Tong Mu, M. Murati, O. Murk, David M'ely, Ashvin Nair, Reiichiro Nakano, Rajeev Nayak, Arvind Neelakantan, R. Ngo, Hyeonwoo Noh, Ouyang Long, Cullen O'Keefe, J. Pachocki, A. Paino, Joe Palermo, Ashley Pantuliano, Giambattista Parascandolo, J. Parish, Emy Parparita, Alexandre Passos, Mikhail Pavlov, Andrew Peng, Adam Perelman, Filipe de Avila Belbute Peres, Michael Petrov, Henrique Pondé de Oliveira Pinto, Michael Pokorny, Michelle Pokrass, Vitchyr H. Pong, Tolly Powell, Alethea Power, Boris Power, Elizabeth Proehl, Raul Puri, Alec Radford, Jack W. Rae, Aditya Ramesh, Cameron Raymond, F. Real, Kendra Rimbach, Carl Ross, Bob Rotsted, Henri Roussez, N. Ryder, M. Saltarelli, Ted Sanders, Shibani Santurkar, G. Sastry, Heather Schmidt, David Schnurr, John Schulman, Daniel Selsam, Kyla Sheppard, T. Sherbakov, Jessica Shieh, S. Shoker, Pranav Shyam, Szymon Sidor, Eric Sigler, M. Simens, Jordan Sitkin, Katarina Slama, Ian Sohl, Benjamin Sokolowsky, Yang Song, N. Staudacher, F. Such, Natalie Summers, I. Sutskever, Jie Tang, N. Tezak, Madeleine Thompson, P. Tillet, Amin Tootoonchian, Elizabeth Tseng, Preston Tuggle, Nick Turley, Jerry Tworek, Juan Felipe Cer'on Uribe, Andrea Vallone, Arun Vijayvergiya, Chelsea Voss, Carroll L. Wainwright, Justin Wang, Alvin Wang, Ben Wang, Jonathan Ward, Jason Wei, CJ Weinmann, Akila Welihinda, Peter Welinder, Jiayi Weng, Lilian Weng, Matt Wiethoff, Dave Willner, Clemens Winter, Samuel Wolrich, Hannah Wong, Lauren Workman, Sherwin Wu, Jeff Wu, Michael Wu, Kai Xiao, Tao Xu, Sarah Yoo, Kevin Yu, Qim-ing Yuan, Wojciech Zaremba, Rowan Zellers, Chong Zhang, Marvin Zhang, Shengjia Zhao, Tianhao Zheng, Juntang Zhuang, William Zhuk, Barret Zoph
year: 2023
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/2303.08774
source_local: ../raw/2023-achiam-gpt-4-technical-report.pdf
topic: general-knowledge
cites:
---

# GPT-4 Technical Report

**Authors:** OpenAI Josh Achiam, Steven Adler, S. Agarwal, L. Ahmad, Ilge Akkaya, et al.  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2303.08774

## One-line
Technical report on GPT-4, a large multimodal Transformer-based language model with predictable scaling, human-level exam performance, and RLHF-based safety alignment.

## Key claim
GPT-4 achieves human-level performance on a wide range of professional/academic exams (e.g., top 10% on a simulated Uniform Bar Exam, 86.4% on MMLU 5-shot), and its final pre-training loss + HumanEval pass rate can be accurately predicted from models trained with $1{,}000\times$–$10{,}000\times$ less compute via a power-law fit $L(C) = a C^b + c$.

## Method
Standard Transformer decoder pre-trained for next-token prediction on internet + licensed text, followed by RLHF post-training for alignment. Capability prediction uses scaling laws of the form $L(C) = a C^b + c$ (irreducible loss) for cross-entropy and $-\mathbb{E}_P[\log(\text{pass\_rate}(C))] = \alpha\, C^{-k}$ for HumanEval. Safety mitigation combines domain-expert red-teaming with a model-assisted safety pipeline.

## Result
Pre-training loss on internal code corpus and HumanEval mean log pass rate (on 23 problems, 3rd-easiest bucket) extrapolate from sub-compute runs to GPT-4 with high accuracy. GPT-4 beats GPT-3.5 and prior LM SOTA on MMLU, HellaSwag, ARC, WinoGrande, HumanEval (67.0%), DROP, and GSM-8K (92.0%); reverses inverse-scaling on Hindsight Neglect; reduces hallucinations by ~19 percentage points on internal factuality evals; pre-train model is well-calibrated (ECE 0.007) but RLHF degrades calibration (ECE 0.074).

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructural context for the agent itself (capability scaling, calibration loss after RLHF, hallucination/reasoning-failure modes) — not a math-content paper for sphere-packing, autocorrelation, or any of the 23 Einstein Arena problems.

## Open questions / connections
- Predictability of *individual* benchmark problems (per-problem pass rate can worsen with scale) remains hard — what governs reverse-scaling pockets?
- Post-RLHF calibration loss (ECE 0.007 → 0.074) is unexplained; can alignment preserve calibration?
- Architecture/data/compute withheld — independent replication of the scaling-law prediction methodology is blocked.

## Key terms
GPT-4, Transformer, scaling laws, power law, RLHF, HumanEval, MMLU, calibration, ECE, hallucination, inverse scaling, multimodal, next-token prediction
