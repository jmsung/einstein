---
type: source
kind: paper
title: "SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks"
authors: Yuchen Zeng, Shupeng Li, Daxiang Dong, R. Xu, Zimo Chen, Liwei Zheng, Yuxuan Li, Zhe Zhou, Hao-Dong Zhao, Lun Tian, Hengjia Xiao, Tianshun Zhu, Longkun Hao, Jianmin Wu
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2603.00575
source_local: ../raw/2026-zeng-swe-hub-unified-production-system.pdf
topic: general-knowledge
cites:
---

## SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks

Qianfan Team, Baidu Inc.

# arXiv:2603.00575v1[cs.AI]28Feb2026

Abstract

Progress in software-engineering agents is increasingly constrained by the scarcity of executable, scalable, and realistic data for training and evaluation. This scarcity stems from three fundamental challenges in existing pipelines: environments are brittle and difficult to reproduce across languages; synthesizing realistic, system-level bugs at scale is computationally expensive; and existing data predominantly consists of short-horizon repairs, failing to capture long-horizon competencies like architectural consistency. We introduce SWE-Hub, an end-to-end system that operationalizes the data factory abstraction by unifying environment automation, scalable synthesis, and diverse task generation into a coherent production stack. At its foundation, the Env Agent establishes a shared execution substrate by automatically converting raw repository snapshots into reproducible, multi-language container environments with standardized interfaces. Built upon this substrate, SWE-Scale engine addresses the need for high-throughput generation, combining cross-language code analysis with cluster-scale validation to synthesize massive volumes of localized bug-fix instances. Bug Agent generates high-fidelity repair tasks by synthesizing systemlevel regressions involving cross-module dependencies, paired with user-like issue reports that describe observable symptoms rather than root causes. Finally, SWE-Architect expands the task scope from repair to creation by translating natural-language requirements into repository-scale build-a-repo tasks. By integrating these components, SWE-Hub establishes a unified production pipeline capable of continuously delivering executable tasks across the entire software engineering lifecycle.

### 1 Introduction

Large language model (LLM) agents have become increasingly capable at writing code and repairing bugs, yet their progress on repository-level software engineering remains constrained by the scarcity of high-quality data (Jimenez et al., 2024; OpenAI, 2024; Wang et al., 2025b; Deng et al., 2025; Zeng et al., 2025; Song et al., 2025; Tao et al., 2026; Chen et al., 2026). This scarcity arises because software engineering correctness is execution-grounded: determining whether a change is correct depends on the complex interplay of build systems, dependency graphs, runtime behavior, and test harnesses, rather than textual similarity or static diffs. Consequently, the prohibitive cost and inherent complexity of generating such execution-grounded data constitute a fundamental bottleneck, hindering the scalability of agent training and evaluation. Therefore, effective datasets must not only be large but also executable by construction, ensuring each instance is paired with a reproducible environment and a verifiable oracle. Crucially, effective data must also excel across three dimensions: cross-language reproducibility, system-level fault realism, and long-horizon task complexity.

Generating such comprehensive data is difficult because these three dimensions are misaligned in current pipelines: First, ensuring reproducibility across languages is a structural challenge (Zan et al., 2025; Qwen Team; Chen et al., 2026). Real-world repositories are heterogeneous in their languages, toolchains, and test ecosystems; indeed, reproducing a single project often requires expert, manual environment debugging. Second, even within reproducible environments, current pipelines lack scalable, cross-language bug synthesis methods (Yang et al., 2025; Pham et al., 2025; Zhang et al., 2025). Consequently, much of today’s synthetic bug data remains local: perturbations are typically confined to a single function or file, which under-represents failures that arise from cross-module contracts, configuration interactions, or subtle regressions whose symptoms surface far from the root cause. Third, beyond fault complexity, the

task scope remains limited. The dominant benchmark format focuses on short-horizon repair—given a failing signal, produce a patch—while under-measuring long-horizon competencies such as planning, dependency management, multi-file coherence, and repository-scale consistency (Thai et al., 2026; Xu et al., 2026; He et al., 2025).

This paper argues that the right abstraction is not the manual data curation typical of existing benchmarks, but a data factory: a reproducible production system that continuously converts raw repositories into diverse, executable tasks. A practical data factory must satisfy three core requirements simultaneously: (i) environment reliability, which ensures the automated provisioning of deterministic, execution-ready environments for heterogeneous repositories (Chen et al., 2026; Shum et al., 2025); (ii) scalable data synthesis, which enables the massive-scale generation of data candidates by integrating automated synthesis algorithms with cluster-scale computing for parallel validation (Pham et al., 2025; Zhang et al., 2025; Tao et al., 2026); and (iii) task versatility, which allows the factory to generate a wide spectrum of task types that range from localized repairs to repository construction (Ding et al., 2026; Zhan et al., 2025).

To operationalize the data factory abstraction, we introduce SWE-Hub, an end-to-end system that unifies the three core requirements through a shared execution substrate. At its foundation, the Env Agent automatically converts raw repository snapshots into reproducible, execution-ready environments. By standardizing container images and verification interfaces, this Agent transforms environment construction from a manual, ad-hoc prerequisite into a reusable asset.

Founded on this substrate, SWE-Hub implements three product lines that collectively fulfill the remaining requirements:

- 1. SWE-Scale: scalable synthesis for repair. Building on SWE-Smith (Yang et al., 2025), SWE-Scale engine addresses the need for high-throughput generation by producing large volumes of localized bug-fix instances. It combines cross-language code analysis with automated bug injection and cluster-scale validation to efficiently synthesize and filter candidates based on execution signals.
- 2. Bug Agent: realistic repair task synthesis. Bug Agent generates high-fidelity repair tasks by synthesizing system-level regressions that reflect cross-module dependencies. Unlike localized bug injection, it produces user-like issue reports focusing on observable symptoms rather than root causes, ensuring the repair tasks mirror real-world debugging scenarios.
- 3. SWE-Architect: versatile long-horizon tasks. Extending the NL2Repo benchmark (Ding et al., 2026), SWE-Architect translates natural-language requirements into repository-scale construction tasks. This enables the factory to generate diverse training data that covers a wide spectrum of competencies—from localized fixes to global architectural planning—within a unified production pipeline.


SWE-Hub consolidates previously fragmented efforts, which include environment automation, scalable synthesis, realism-driven bug generation, and long-horizon task design, into a coherent production stack with standardized interfaces, unified verification, and shared extensibility mechanisms. Rather than releasing a static dataset, we provide a production system capable of continuously generating executable tasks, scaling with compute, and adapting to new languages and task families.

We make the following contributions:

- • A unified data factory architecture. We propose a system that standardizes the production of execution-grounded software engineering tasks. By integrating environment setup, candidate generation, and verification, this architecture enables compute-scalable data creation that is reproducible by construction.
- • An automated reproducibility substrate. We develop the Env Agent to act as a universal adapter for raw repositories. It autonomously provisions and verifies containerized environments, decoupling task generation from the complexities of language-specific toolchains and build systems.


- • Scalable and realistic task synthesis mechanisms. We introduce SWE-Scale engine to achieve high-throughput generation via parallelized validation, and Bug Agent to ensure high fidelity by creating system-level faults with decoupled symptoms and root causes.
- • Expansion of task horizons. We introduce SWE-Architect to generate "build-from-scratch" tasks at scale, producing training data that targets long-context competencies—such as architectural planning and global consistency—which are underrepresented in repair-centric datasets.


### 2 Related Work

SWE-Hub is positioned at the intersection of (i) execution-grounded software engineering (SWE) benchmarks that rely on containerized evaluation, and (ii) scalable task generation methods that synthesize verifiable bug-fix instances over real repositories. In contrast to one-off benchmark releases, our work presents a production system designed to continuously transform raw repositories into executable task records through a shared execution substrate and multiple, specialized task product lines.

#### 2.1 Execution Substrates and Reproducible Evaluation Harnesses

A significant body of recent literature evaluates repository-level agents using containerized harnesses that standardize dependency installation, test invocation, and outcome collection. SWE-bench (Jimenez et al., 2024) pioneered the issue-resolution setting over real GitHub repositories, providing a Dockerbased harness for reproducible evaluation. Subsequent efforts have further emphasized robustness and expanded coverage, including SWE-bench Verified (OpenAI, 2024) and SWE-bench++ (Wang et al., 2025b). Concurrently, other research initiatives have elevated “repository operationalization” to a firstclass capability: Multi-Docker-Eval(Fu et al., 2025) benchmarks agents on the automatic construction of runnable Docker environments across heterogeneous projects.

Limitations. While these efforts substantially improve evaluation reproducibility, they predominantly frame containerization as an evaluation harness or a specific benchmark task. Consequently, environment setup remains tightly coupled to particular benchmark specifications, and the environment layer is rarely abstracted as a reusable, versioned asset capable of supporting diverse downstream task families at scale. Furthermore, failure handling in large-scale automation is frequently under-specified; distinguishing between environment failures, test harness incompatibilities, and invalid task instances remains a persistent challenge.

Our improvement. SWE-Hub generalizes containerized evaluation into a shared execution substrate for data production. By converting repositories into versioned, pinned container images with standardized verifier entrypoints, we decouple the environment logic from task logic. Downstream generators consume only this uniform interface, enabling systematic gating, replay, and the reliable support of multiple task families over the same substrate.

#### 2.2 Scalable Synthesis and Task Generation

Complementing static benchmarks, several lines of work aim to scale training and evaluation data by synthesizing verifiable tasks from repositories. SWE-Smith (Yang et al., 2025) generates large volumes of bug-fix instances by manipulating real codebases and validating candidates via execution. Similarly, R2E-Gym (Jain et al., 2025) and SWE-Gym (Pan et al., 2025) provide executable training environments and procedural task generation with verifiers to support agent learning under rigorous correctness checks. Other efforts explore alternative scaling axes. For instance, SWE-Synth (Pham et al., 2025) synthesizes verifiable data with agent-generated trajectories, while SWE-Mirror expands datasets by reusing existing environments and “mirroring” issues across repositories (Wang et al., 2025a). Additionally, Self-Play SWE-RL (Wei et al., 2025) automates problem creation via iterative self-play. Finally, SWE-Lego (Tao et al., 2026) demonstrates that carefully constructed mixtures of real and synthetic data can substantially improve supervised fine-tuning.

Limitations. Most existing synthesis pipelines prioritize a single task format—often short-horizon repairs—and embed implicit assumptions about environment setup, repository structure, or verification interfaces. This coupling limits portability across ecosystems and hinders the composition of diverse

task families. Additionally, while high-throughput synthesis requires treating verification as a systems problem (encompassing isolation, retry semantics, stateless execution, and scalable scheduling), many prior pipelines validate tasks without explicitly surfacing the infrastructure contract as a reusable layer.

Our improvement. SWE-Hub provides a unified factory architecture where (i) environment provisioning is decoupled from task logic via a standardized execution substrate, and (ii) task generation is organized into modular product lines sharing a common verification contract. This design supports highthroughput synthesis and filtering through scalable, stateless sandboxed verification, while simultaneously enabling task diversity that extends beyond local bug-fixing.

#### 2.3 Long-Horizon Competencies and Repository Creation

Recognizing that issue-fixing alone is insufficient to measure comprehensive agent capabilities, recent benchmarks increasingly emphasize long-horizon competencies such as planning, dependency management, and multi-step repository evolution. For instance, SWE-EVO evaluates coding agents in long-horizon software evolution scenarios (Thai et al., 2026), and SWE-Bench Pro introduces more complex tasks extending beyond standard issue fixing (Deng et al., 2025). The NL-to-repository setting further pushes the boundary by requiring agents to construct or substantially extend repositories from natural language requirements under executable tests, with NL2Repo-Bench serving as a prominent example (Ding et al., 2026).

Limitations. While these benchmarks successfully motivate long-horizon evaluation, they are typically introduced as standalone datasets or isolated tasks. They lack integration into a shared production pipeline capable of continuously generating and validating instances under a uniform execution interface.

Our improvement. SWE-Hub integrates long-horizon repository construction as a first-class product line built upon the same execution substrate used for repair and regression tasks. This integration ensures consistent verification, comparable task records, and scalable instance generation across different task horizons.

#### 2.4 Summary

In summary, existing work has advanced (i) containerized reproducible evaluation and (ii) scalable synthesis of executable SWE tasks, yet these capabilities are often delivered as benchmark-specific harnesses or single-format generation pipelines. SWE-Hub contributes a production-oriented unification: a reusable execution substrate with standardized verifier interfaces, coupled with multiple task product lines that span the spectrum from short-horizon repairs and system-level regressions to long-horizon repository construction.

### 3 SWE-Hub System Overview

SWE-Hub is an end-to-end data production system designed to generate diverse, executable software engineering (SWE) tasks at scale. Given raw source repositories, SWE-Hub produces task instances that are verifiable by construction: each instance is packaged with a pinned execution environment and a standardized verification entrypoint. Crucially, SWE-Hub represents not a static benchmark release, but a factory abstraction that decouples (i) a shared execution substrate—responsible for making repositories runnable and testable—from (ii) multiple task product lines that synthesize distinct families of tasks on top of this substrate. Built upon a foundational Kubernetes execution environment, this architecture ensures the scalability and isolation necessary for high-throughput data production. This section details the design goals, system architecture, unified task schema, and the Kubernetes-native execution module.

#### 3.1 Design Goals

We design SWE-Hub around five verifiable goals, each directly manifested in the system’s artifacts and operational guarantees.

• G1: Executable by construction. Every task is bound to (a) an immutable container image reference (pinned by digest) and (b) a standardized verification entrypoint (test command + result collector).

###### SWE-Hub System

SWE-Scale Bug Agent SWE-Architect

- Build from Spec
- • Structured spec
- • Integration & wiring
- • Multi-file implementation
- • Planning-heavy tasks


Large-Scale Repair

- Realistic Regressions
- • Repo-level change
- • User-like symptoms
- • No root-cause hints
- • Closer to realistic


- • Local edits
- • High throughput
- • Cross-language
- • Low-cost


Unified Task Schema

- • 𝑓 (Family)
- • ℛ (Repository Spec)
- • 𝒫𝑏𝑢𝑔 (Problem Patch)
- • 𝒫 (Problem Statement)
- • 𝒪 (Oracle)
- • 𝒱 (Validation Criteria)
- • ℳ (Metadata)


ENV Agent

Pinned Container Image Standard Verification

Deterministic Artifacts

Raw Source Repositories

Unified Entrypoint

Makes Code Runnable & Testable

Kubernetes-native Execution Module

Kubernetes-Native Execution Model

- • Cache amortization
- • Parallel verification


- • Ephemeral isolated pods
- • No state contamination


- Figure 1: SWE-Hub architecture. Starting from raw source repositories, the Env Agent provisions a deterministic execution substrate—pinned container images, a unified verification entrypoint, and deterministic artifacts—to make code runnable and testable. On top of this substrate, three task generators produce complementary SWE workloads: SWE-Scale for high-throughput local repair edits, Bug Agent for realism-oriented repo-level regressions with user-like symptoms and no root-cause hints, and SWE-Architect for building multi-file implementations from structured specifications.


This eliminates implicit environment assumptions and ensures that correctness is determined strictly through execution signals.

- • G2: Cross-language extensibility with bounded engineering effort. SWE-Hub is languageagnostic at the system level. Language- and ecosystem-specific details (parsing rules, build conventions, dependency tooling, test runners) are externalized into declarative configurations. A shared analysis backbone (e.g., tree-sitter-based parsing and queries) provides a uniform interface for code inspection and transformation. This design does not claim a “universal solution” for all languages but significantly reduces the marginal cost of adding new ecosystems to implement the required configuration and adapters.
- • G3: Verification as a first-class scalability target. Since execution dominates the computational cost, verification is treated as a distributed systems problem. SWE-Hub employs stateless, containerized workers scheduled on a Kubernetes cluster (Kubernetes, 2014) to support high parallelism, strict isolation, and fault recovery. The system aims for throughput that scales linearly with available compute while remaining robust to long-tail test runtimes and I/O overheads.
- • G4: Realism with leakage-resistant task presentation. Beyond simple local perturbations, SWEHub supports tasks that mirror real-world incidents: system-level regressions accompanied by userlike issue reports. Issue prompts are generated under explicit constraints that preserve observable symptom and reproduction evidence (logs, steps, expected/observed behavior) while withholding root-cause hints (e.g., causal identifiers and explanations), thereby mitigating answer leakage.
- • G5: Multi-horizon task coverage under a unified verifier interface. The system supports both short-horizon repair tasks and long-horizon repository construction tasks. All task families are evaluated through the same execution substrate and verification entrypoint; task-specific oracles


dictate only how success is interpreted (e.g., fail-to-pass sets vs. hidden tests), enabling comparable evaluation across different complexity horizons.

#### 3.2 Architecture

Overview. SWE-Hub is composed of an execution substrate layer and multiple task product lines (Figure 1). The substrate layer guarantees that a repository is runnable and testable in a deterministic way, while the product lines generate task instances by transforming repositories and validating outcomes through execution.

Execution substrate: Env Agent. Given a repository snapshot, the Env Agent automatically constructs: (i) a versioned container image capturing toolchains and dependencies, and (ii) standardized verification entrypoints (e.g., a test runner command coupled with a result parser). The target state is defined as environment readiness: the repository’s verification harness can be invoked deterministically inside the container and produces machine-parseable outcomes (including failures), with logs and exit status captured. Notably, readiness does not require tests to pass; rather, it establishes a stable boundary that ensures downstream synthesis and evaluation are reproducible.

- Product line A: SWE-Scale for scalable repair-task synthesis. Building on the SWE-Smith methodology, SWE-Scale engine produces high volumes of short-horizon repair instances by injecting candidate fault patches and validating them through execution. It leverages cross-language code analysis (via the shared parsing backbone) to locate transformation sites and apply either procedural mutations or LLM-assisted rewrites. Candidates are accepted only if execution validates the intended signal (e.g., pass-to-fail transitions under the repository test suite), yielding verifiable repair tasks with precise failure signatures.
- Product line B: Bug Agent for realism-oriented regressions and issue prompts. Bug Agent targets failures that are non-local in either origin or manifestation. It synthesizes system-level regressions involving cross-file or cross-module interactions (e.g., contract violations across components, configurationdriven behavior changes, or regressions whose symptoms surface far from the modified code). For each validated regression, Bug Agent generates a user-like issue report that includes symptoms and reproduction evidence while explicitly avoiding root-cause disclosure. While Bug Agent shares the substrate and verifier interface, it operates independently to generate high-fidelity debugging scenarios.
- Product line C: SWE-Architect for long-horizon repository construction. Building on the NL2Repo methodology, SWE-Architect expands the task space from repair to creation. Starting from a pristine repository version, it derives structured natural-language requirements and generates tasks that require agents to implement substantial repository functionality (modules, APIs, integration glue) from specifications. Evaluation remains execution-grounded under the same substrate and entrypoint, typically utilizing hidden tests to assess repository-scale correctness, architectural planning quality, dependency management, and global consistency.


Shared services. All product lines rely on common infrastructure: (i) the execution substrate (image + entrypoints), (ii) a unified task schema, (iii) cluster-scale orchestration and isolation, and (iv) standardized logging and artifact retention. This modular design allows new task families to be added as additional product lines without re-engineering environment provisioning or verification logic.

#### 3.3 Unified Task Schema

SWE-Hub records every task as a self-contained, language-agnostic task record optimized for consumption by downstream training and evaluation pipelines. Formally, each task instance T is defined as:

T = (f,R,Pbug,P,O,V,M), where:

- • Family f ∈ {SWE-Scale,Bug Agent,SWE-Architect}: the task family produced by a specific product line.


- • Repository Spec R: repository identifier and pinned base commit representing the clean, original state.
- • Problem Patch Pbug: the patch applied to R to generate the initial (buggy or incomplete) repository state presented to the agent.

- – For repair tasks (f ∈ {SWE-Scale,Bug Agent}), this is the injected bug patch.
- – For creation tasks (f = SWE-Architect), this is the hollowing patch that removes implementations to define the starting point.


- • Problem Statement P: a structured natural-language prompt (e.g., issue-style description) describing the task.
- • Oracle O: the Ground Truth Solution patch.

- – For repair tasks, this is the reference fix patch that resolves the issue.
- – For creation tasks, this is the gold implementation patch containing the correct modules and functions.


- • Validation Criteria V: the specific test execution signals or partitions used to judge success, independent of the oracle.

- – For repair tasks, V consists of the test partition derived from the baseline run, specifically

identifying the pass-to-fail (TP2F) and pass-to-pass (TP2P) test sets that define the required behavior change.

- – For creation tasks, V consists of the target test suite (hidden tests) that must be satisfied by the completed repository.


- • Metadata M: execution-grounded diagnostics and performance statistics, including exit codes, runtime/resource usage, and full logs (stdout/stderr).


This schema is intentionally execution-centered: it separates the initial state construction (R + Pbug) from the solution verification. The oracle O strictly represents the correct code, while V defines the behavioral contract the solution must satisfy. In practice, all families reduce to invoking the same verification entrypoint inside the pinned image. Here, the field V governs the automated evaluation by determining success based solely on execution signals (e.g., unit test pass/fail status), whereas O serves as the ground-truth reference code for offline analysis and training, distinct from the execution-based verification process.

#### 3.4 Kubernetes-native Execution Module

SWE-Hub is implemented as a container-native distributed system to maximize throughput, ensure isolation, and guarantee operational robustness.

Job orchestration. A central controller schedules environment provisioning, task generation, and verification as Kubernetes Jobs. Each unit of work executes in a short-lived pod with explicit CPU/memory limits, preventing state contamination across tasks and enforcing strict resource boundaries.

Stateless verification workers. Verification runs are designed to be stateless: inputs are task records and pinned image references, while outputs are structured validation artifacts. This statelessness supports deterministic reruns, robust retry-on-transient-failure policies, and simplified debugging.

Caching and warm start. To mitigate overhead, cluster nodes cache commonly used images and dependencies. For repositories with expensive setup costs (e.g., complex builds), SWE-Hub can maintain a warm container pool to amortize initialization time while strictly preserving isolation guarantees.

Observability and artifact retention. For every execution, SWE-Hub logs comprehensive stdout/stderr, exit codes, parsed test outcomes, and resource usage. Failures are retained with full diagnostic context to enable offline analysis and to prevent silent dataset corruption.

Environment Layer: ENV Agent and Test Agent

Phase 2:Test Agent – Verifier

Phase 1:ENV Agent – Provisioning & Build Readiness

Phase 3:Solidification & Verification Gate

Discovery & Standardization

Environment-Ready Container

Repo Code Base Image

Repo Code Base Image

Image with Code

pom.xml,package.json, CMakeLists.txt …

Find Test Commands

(pytest,npm test …)

run

install_script

Identify Toolchains

Observe Outputs, Generate Adapters

(pip,npm,maven)

ENV Ready Image

Compile/Build

(Tests Skipped)

run

Enforce Standard Schema (JUnit XML/JSON)

test_entrypoint

𝑓𝑎𝑖𝑙𝑒𝑑

Install Missing Libs/Packages

𝑠𝑢𝑐𝑐𝑒𝑠𝑠 Verified Image

test_entrypoint & Adapter

install_script (Goal Achieved) Environment Readiness

Standardized Verifier Interface

Reusable Execution Substrate

- Figure 2: SWE-Hub Environment Layer pipeline. Phase 1 (Env Agent) performs environment provisioning and build readiness, identifying toolchains and installing dependencies to achieve environment readiness without requiring tests to pass. Phase 2 (Test Agent) establishes a unified verification interface via entrypoint discovery and result standardization, employing dynamic adapters to handle heterogeneous ecosystems where native reporting is non-standard. Phase 3 (Solidification and Verification Gate) encapsulates the environment state and verification logic into a pinned container image, applying a strict execution check to ensure the substrate is deterministic and reusable for downstream task generation.


### 4 Environment Layer: The Execution Substrate

Repository-level software engineering is fundamentally execution-grounded: the success of an agent is ultimately determined by build correctness, dependency resolution, runtime behavior, and executable test suites. In practice, the primary source of brittleness when scaling training data synthesis and evaluation is not the code transformation logic itself, but the environment problem: heterogeneous toolchains, drifting dependencies, project-specific test entrypoints, and non-standard result formats. SWE-Hub addresses this bottleneck by elevating environment provisioning to a first-class component of the factory. Our Environment Layer deploys two specialized agents—Env Agent and Test Agent—to transform an arbitrary repository snapshot into a reusable execution substrate that downstream task product lines can invoke deterministically(Figure 2).

Outputs. For each repository snapshot, the Environment Layer produces three core artifacts: (i) an idempotent install_script that provisions toolchains and dependencies; (ii) a standardized test_entrypoint that executes the repository’s verification harness and emits machine-parseable results; and (iii) a versioned container image that encapsulates the above into a durable, reusable asset. Downstream components (SWE-Scale, Bug Agent, SWE-Architect) consume this substrate via a uniform interface: invoke the test_entrypoint inside the pinned image and parse the standardized artifacts.

Section contributions. This section makes the following contributions: (i) Formalization of environment readiness. We define a strict termination condition separating infrastructure setup (invocability) from test passing, resolving the ambiguity between environment failures and test failures. (ii) Dualagent framework. We introduce a decoupled Env Agent and Test Agent design to automate complex dependency resolution and test harness discovery across diverse ecosystems. (iii) Dynamic adapters. We provide runtime adapters to normalize heterogeneous test outputs into a unified schema, ensuring consistent downstream verification.

#### 4.1 Challenges and Design Principles

A single “run tests” command is insufficient as a robust objective across diverse ecosystems. In many repositories, failures occurring during environment setup (e.g., missing system libraries, incompatible runtime versions, broken dependency resolution, or absent build tools) are indistinguishable from legitimate test failures (e.g., assertion failures signaling real bugs) if conflated into a single execution stage. This ambiguity is fatal for automation: it prevents the system from determining whether it should continue remedying the environment or proceed to downstream task generation.

SWE-Hub therefore adopts two core principles:

- • P1: Decouple environment readiness from test correctness. The Environment Layer is responsible solely for making the verification harness invocable and its outputs collectible; it is explicitly not responsible for ensuring that tests pass.
- • P2: Standardize the verifier interface and artifacts. To support large-scale distributed execution, verification must rely on a stable entrypoint and a canonical output schema, regardless of the underlying language, framework, or project-specific conventions.


These principles motivate a two-agent design: the Env Agent establishes readiness by provisioning a buildable, runnable environment, while the Test Agent identifies test entrypoints and produces machineparseable results—often implementing adapters when native structured reports are unavailable.

#### 4.2 Environment Readiness as a Termination Criterion

A central requirement for autonomous environment provisioning is a clear, verifiable termination condition. We define environment readiness as a repository-specific boundary state at which:

the repository’s verification harness can be invoked deterministically inside the container, and the run produces machine-parseable outcome artifacts (including failures), with logs and exit status captured.

Readiness explicitly does not imply that “tests pass.” Rather, it signifies that the system can repeatedly execute the verifier and collect structured outcomes. Concretely, readiness is instantiated per ecosystem by verifying the presence of a valid test invocation capability coupled with structured artifact generation:

- • Python: a pytest-based harness is invocable and emits a structured report (e.g., JUnit XML or JSON), regardless of individual test pass/fail status.
- • Java: mvn test or gradlew test executes the test harness to completion and produces JUnitcompatible XML reports.
- • JS/TS: a project-defined test script executes without environment-level errors (e.g., missing modules or toolchains), and its results are captured in a standardized schema (either native or adapted).
- • C# / .NET: dotnet test executes against the solution or project targets and emits structured results (e.g., TRX format via built-in loggers) regardless of test pass/fail status.
- • C/C++: the project builds and runs test targets (via CMake, Make, or Autotools), and the verifier (e.g., ctest or test executables) is invocable with logs and exit codes captured. Execution outputs are normalized into a unified schema, utilizing native reports or generated adapters where necessary.
- • Go: go test executes across relevant packages (e.g., ./...), building dependencies and test binaries, and emits structured JSON output (via the -json flag) capturing individual test status.
- • PHP: dependencies are resolved via Composer, and the test harness (e.g., PHPUnit via vendor/bin/phpunit) runs to completion, generating structured logs (e.g., JUnit XML) regardless of pass/fail status.


- • Ruby: the environment is prepared using Bundler, and the test suite (e.g., RSpec or Minitest via bundle exec) executes. Results are captured in a standardized schema, using native JSON formatters or adapters to normalize output streams.
- • Rust: the project builds and tests via cargo test, which implicitly compiles the workspace. The test harness runs to completion, and results are captured—typically via an adapter that parses the standard output or through specific logging configurations—to produce machine-parseable artifacts.


This definition establishes a uniform, checkable success state while strictly respecting ecosystemspecific conventions.

The implementation of the Environment Layer follows the three-phase pipeline illustrated in Figure 2: Phase 1 (ENV Agent) establishes the build environment; Phase 2 (Test Agent) standardizes the verification interface; and Phase 3 solidifies these into a reusable image asset.

#### 4.3 Phase I: The Env Agent: Provisioning and Build Readiness

Goal. The Env Agent generates an idempotent install_script that transitions the container from a clean base image to an environment-ready state, without requiring tests to pass. Its output is a deterministic sequence of commands sufficient to reproduce the exact toolchain setup and dependency installation.

Workflow. Given a repository snapshot, the Env Agent executes the following steps:

- 1. Repository Scouting. Identifies language and toolchain signals, locates build descriptors (e.g., pyproject.toml, requirements.txt, package.json, pom.xml, build.gradle), and infers likely runtime constraints (e.g., specific Node, Python, or Java versions).
- 2. Toolchain Provisioning. Installs and pins the required runtimes and system dependencies (compilers, build tools, OS libraries) using non-invasive, environment-level operations.
- 3. Dependency Installation. Executes ecosystem-appropriate installation commands (e.g., pip, npm, maven, gradle) while capturing detailed logs and exit codes.
- 4. Build Readiness Verification. Executes build steps designed to avoid conflating test failures with environment failures (e.g., performing build/compile/package steps with tests skipped where supported). Failures trigger targeted remediation strategies (e.g., installing missing libraries, adjusting runtime versions, or installing build tools) until the readiness conditions are satisfied.


Scope and Boundary. The Env Agent does not modify project semantics to “fix tests”, nor does it attempt to interpret assertion-level failures. Its responsibility terminates once the repository can invoke the verifier deterministically.

#### 4.4 Phase II: The Test Agent: EntryPoint Discovery and Standardization

Goal. Operating in an environment-ready container, the Test Agent produces a standardized test_entrypoint (and any necessary adapters) such that a verification run yields machine-parseable artifacts under a uniform schema. This is critical because repository test commands and output formats are often project-specific and designed for human consumption.

Workflow. The Test Agent performs the following:

- 1. EntryPoint Discovery. Identifies candidate test commands from project configuration files (e.g., package.json scripts, build tool defaults, CI configurations).
- 2. Trial Execution. Executes candidate commands to observe failure modes and output structure, carefully distinguishing environment-level failures (missing tools, missing modules, misconfigured paths) from legitimate test failures (e.g., assertion errors) by parsing error signatures and exit codes.


- 3. Structured Reporting. Prioritizes native structured reports where available (e.g., JUnit XML from Java toolchains, pytest JUnit/JSON plugins). When outputs are unstructured, it synthesizes an adapter that wraps the original test command and converts raw stdout/stderr streams into a unified standard_result.json format.
- 4. Acceptance Validation. The verifier is accepted if it can be invoked deterministically and produces valid structured artifacts, even if the tests themselves fail.

Dynamic adapters for heterogeneous outputs. Adapters are particularly vital for ecosystems where testing conventions are highly heterogeneous or lack standardized reporting, such as JavaScript/TypeScript (characterized by a fragmented landscape of competing frameworks like Jest, Mocha, and AVA) and C/C++ (which often rely on custom build scripts and unstructured console output). In such cases, the Test Agent generates a lightweight runtime-specific wrapper (e.g., a Node.js runner for JS projects or a shell script adapter for C/C++ makefiles) that executes the project’s test script, captures output streams, and emits a normalized result object (containing test counts, failing test identifiers, exit codes, and logs). This ensures downstream verification remains uniform and machine-checkable across diverse repository ecosystems.

- 4.5 Phase III: Substrate Solidification: From Scripts to Images


While the Env Agent and Test Agent initially operate in an exploratory mode to generate per-repository scripts and adapters, SWE-Hub solidifies these ephemeral artifacts into durable, reusable assets:

- • A versioned container image produced by applying the install_script to a clean base image and freezing the resulting filesystem state.
- • A metadata record that binds the image reference to the specific verifier interface (test entrypoint + result schema) utilized throughout the factory.


Verification gate. Before an image enters the asset pool, SWE-Hub enforces a strict validation gate: it instantiates a fresh container from the candidate image and executes the standardized test_entrypoint. The environment is accepted only if the run completes deterministically and emits valid machine-parseable artifacts conforming to the expected schema (with logs archived). This gate prevents silent corruption of downstream datasets and ensures that all subsequent synthesis and evaluation steps inherit strong reproducibility guarantees.

### 5 SWE-Scale: A Scalable Synthesis Engine for Repair

SWE-Hub’s primary source of data volume is SWE-Scale, a high-throughput synthesis-and-verification engine that transforms a single environment-ready repository substrate into vast numbers of executable bug-fix instances. The critical bottleneck in prior synthesis workflows is shared mutable state: when generation and validation operate on a single working directory (or a shared Git checkout), each candidate mutation forces a serial loop of apply → test → reset. SWE-Scale eliminates this bottleneck by enforcing three system-level invariants: (i) stateless sandboxes for all mutations and tests, (ii) cluster-scale verification as the default execution mode, and (iii) polyglot synthesis via a shared parsing backbone and configuration-driven language support.

Section contributions. This section makes three contributions aligned with these invariants: (i) a container-native redesign that enables massively parallel verification, (ii) a polyglot analysis-and-mutation substrate grounded in a unified parser and configuration-as-code, enabling cross-language bug injection without core engine rewrites, and (iii) a restructured bug-injection engine that emits robust, byte-offset edits and hosts both procedural and model-assisted transformations. Figure 3 illustrates the overall architecture of SWE-Scale, integrating these components into a unified pipeline.

##### SWE-Scale: A Scalable Synthesis Engine for Repair

K8S Verification Cluster

Shared Parsing Backbone

Issue Generator

###### Repos

Tree-sitter AST Entity Report

- • Execution Logs
- • Candidate Patches
- • Pass-to-Fail Tests (P2F)
- • Few-shot Examples


Warm Container Pool

![image 1](<2026-zeng-swe-hub-unified-production-system_images/imageFile1.png>)

Python

- • Location(file:line)
- • Signature and Snippet
- • Complexity Score
- • Structural Tags


JS/TS

Sandbox Pods

LLM Generate

C/C++

Problem Statement

…

- 1. Materialize Patch:

• Apply Patch to Source

- 2. Run test:

• Run Test Suite for Verification

- 3. Capture Signals:


Candidate Patch Generator

Modifier

Target

Candidate

Operational

• Capture P2F & Execution Data

Data Package

Entity Target

Patch

Control Flow

Candidate

- • Portable Patch
- • P2P & P2F Tests
- • Pinned Environment
- • Problem Statement


Procedural

Entity

Patch

Structural

Candidate Entity Report Patch

Target Entity

Class-Orient

Validity Check

Modify

(|𝑇P2F| > 0)

…

…

LLM-Assisted

Rewrite

- Figure 3: SWE-Scale architecture. The system transforms an Environment-Ready Substrate into executable bug-fix instances. The pipeline follows a structured flow: the Shared Parsing Backbone performs polyglot entity analysis using Tree-sitter ASTs to identify targets; the Candidate Generator synthesizes fault specifications via procedural or LLM-assisted strategies; and the Kubernetes-Scale Verification Cluster materializes patches in isolated sandbox pods, executing tests and performing behavioral validity checks to produce verified task records.


#### 5.1 Stateless Execution Module and Container Isolation

SWE-Scale is architected around a strict “sandbox-per-candidate” execution model. Leveraging the pinned container image and verifier entrypoint produced by the Environment Layer (Section 4), each atomic operation (e.g., materializing a candidate edit, extracting a patch, or executing a verification job) is run inside a fresh, short-lived container instance. No candidate mutates the global checkout; instead, each receives an isolated filesystem snapshot and is discarded immediately after artifact generation.

This design yields two critical benefits. First, it eliminates cross-candidate contamination (e.g., lingering build products, modified lockfiles, cached dependencies) that can silently corrupt validation results. Second, it ensures failures are local and recoverable: a crashed container is equivalent to a failed candidate and can be retried or dropped without affecting concurrent jobs. In practice, this statelessness is the prerequisite for scalable verification (Section 5.2) and for producing reproducible task artifacts that downstream pipelines can deterministically replay.

Warm-start optimization via a container pool. While stateless sandboxes guarantee correctness and isolation, naive container instantiation can impose significant startup overhead. SWE-Scale therefore maintains a warm container pool that leases pre-initialized sandboxes (with the repository snapshot and common tooling pre-loaded), applies candidate edits, and returns sandboxes after cleanup. This mechanism amortizes cold-start costs without compromising the stateless execution contract.

#### 5.2 Distributed Verification and Behavioral Validity Criteria

Verification is the dominant computational cost in synthesis pipelines. SWE-Scale therefore treats test execution as a distributed systems workload: candidate patches are dispatched as Kubernetes jobs, each executing within an isolated pod subject to explicit resource limits and standardized logging. This architecture enables high concurrency while preserving reproducibility through pinned images and uniform verifier entrypoints.

Behavioral validity criteria. Let Tsuite denote the repository’s test suite, and let R(P,E) be the vector of test outcomes obtained by applying patch P in environment E and invoking the standardized verifier entrypoint. For a candidate injected patch Pbug to be accepted as a valid regression instance, it must flip at least one previously passing test to failing (a non-empty pass-to-fail set):

TP2F = {t ∈ Tsuite | R(∅,E)[t] = pass ∧ R(Pbug,E)[t] = fail}, |TP2F| > 0. We also record the pass-to-pass set TP2P for regression analysis and stability checks:

TP2P = {t ∈ Tsuite | R(∅,E)[t] = pass ∧ R(Pbug,E)[t] = pass}.

These execution-grounded signals, combined with logs, exit codes, runtime metrics, and resource usage, are stored in the task Validation field V and Metadata field M (Section 3.3), enabling comprehensive auditing, deterministic reruns, and the extraction of rich downstream training signals beyond a single binary label.

#### 5.3 Polyglot Analysis and Targeting Backbone

Earlier synthesis systems are often tightly coupled to specific language ecosystems (e.g., Python AST tooling), making extensibility expensive. SWE-Scale adopts a polyglot design centered on tree-sitter as a shared parsing and querying backbone, which provides a uniform interface for analyzing and transforming syntactic structures across languages.

Universal entity extraction. The first phase of the synthesis pipeline transforms raw source code into a structured, language-agnostic representation. By utilizing the shared tree-sitter backbone (Treesitter, 2015), the system identifies and extracts code entities—such as functions, methods, and classes—irrespective of the programming language. This analysis generates an entity analysis report that captures essential structural features (e.g., signatures, nesting depth) and complexity signals (e.g., presence of loops or binary operations). This report serves as the foundational inventory for the engine, enabling precise targeting and filtering of candidates based on their structural properties.

Enabling procedural modification. Beyond analysis, the shared tree-sitter backbone also serves as the enabler for cross-language bug injection. It allows the engine to precisely locate modification targets in any supported ecosystem without relying on language-specific AST libraries. By leveraging the same querying mechanism used for extraction, the engine can identify specific syntactic patterns (e.g., binary operators, conditional blocks) that serve as injection points. This capability ensures that the logic for target localization is decoupled from the specific syntax of the source language.

Configuration-as-code for language support. To achieve true polyglot extensibility without rewriting the core engine, SWE-Scale externalizes all language-specific knowledge into declarative Language Templates (YAML). These templates define the rules governing both analysis and modification:

- • Metadata: File extensions, indentation size, and test file patterns.
- • Analysis Rules: Patterns used to identify entities and compute complexity.
- • Injection Rules: Queries that map bug types to syntactic structures (e.g., locating binary expressions for operand swaps).


This design ensures that supporting a new language (e.g., Java, JavaScript, or Go) requires only authoring a new YAML configuration, allowing the system to seamlessly scale its synthesis capabilities across diverse codebases.

#### 5.4 Modification Strategies: Procedural and LLM-Based

Built upon the shared parsing interface, SWE-Scale implements bug injection as a set of pluggable transformation policies. The engine supports two distinct modes of fault generation: Procedural Modification (rule-based structural edits) and LLM-Based Modification (semantic-level rewrites).

- 5.4.1 Procedural Modification: Rule-Based Structural Edits Building upon the targeting capabilities of the polyglot backbone, procedural modification implements a standardized, three-step workflow for injecting syntax-level faults. First, the engine localizes target nodes within the code using the tree-sitter queries defined in the Language Templates. Second, it validates preconditions against the entity analysis report to ensure the code is a suitable candidate (e.g., verifying that a function actually contains a loop before attempting a loop-modifying injection). Finally, it generates atomic edits based on the precise byte offsets of the located nodes. This approach guarantees that modifications are syntactically correct and structurally precise, avoiding the brittleness of naive string replacement.

We categorize these rule-based modifiers into four primary families, covering a wide spectrum of common programming errors:

Operational Modifications. These inject subtle arithmetic or logic errors by mutating operators or operands. Examples include swapping operators within the same functional group (e.g., changing + to −), flipping logical operators (e.g., == to ! =), or swapping the order of operands in non-commutative operations (e.g., a − b to b − a).

Control Flow Modifications. These disrupt the execution order or causal dependencies within functions. Techniques include inverting the bodies of if-else blocks, swapping if-elif conditions, or shuffling the order of statements within a function body to break temporal coupling.

Structural Modifications. These remove or unwrap code structures to simulate missing features or broken error handling. Examples include deleting loop bodies, removing conditional branches, stripping class inheritance to break polymorphism, or unwrapping try-except blocks to eliminate error handling.

Table 1 provides a comprehensive taxonomy of the implemented modifiers, detailing their target syntax, transformation logic, and the simulated bug types.

- 5.4.2 LLM-Based Modification: Semantic Rewrites While procedural bugs are syntactically precise, they often lack the semantic nuance of real-world errors. SWE-Scale uses LLMs to generate two types of semantic bugs:


LLM Rewrite (Implementation Reconstruction). This mode simulates errors common in initial implementations.. The engine provides the LLM with the full file context but obscures the implementation of a target function (replacing it with a stub). The prompt instructs the model to implement the function from scratch without external libraries. This forces the model to rely on “common sense” patterns, often missing edge cases (e.g., null inputs, empty lists) or choosing inefficient algorithms, resulting in fragile code.

LLM Modify (Blind Implementation). This mode simulates “maintenance-introduced” errors. The engine provides the LLM with the correct, working code and instructs it to introduce a subtle logical bug that will break existing unit tests. The prompt provides a dynamic menu of bug types (e.g., “introduce off-by-one error”, “alter operator precedence”) and enforces strict constraints: no syntax errors, no comments revealing the bug, and high subtlety. This creates adversarial bugs that are harder to detect than simple syntactic flips.

#### 5.5 Issue Generation: Synthesizing User-Like Problem Statements

A complete task instance requires not only a patch but also a problem statement that guides the agent. After a valid bug is verified, SWE-Scale synthesizes an Issue Description that mimics real-world user reports.

Symptom-centric generation. The generation process is designed to translate technical failure artifacts into natural-language narratives that reflect a user’s perspective, rather than a developer’s debugging summary. This transformation is driven by three key inputs:

- • The Bug Patch: The specific code changes that introduced the regression.


- • Execution Artifacts: The failure traces (stack traces, error messages, and stdout) which provide the observable symptoms of the bug.
- • Failing Test Source: The source code of the test cases that failed (TP2F), which defines the expected behavior and context.


The LLM constructs a symptom-focused narrative by analyzing the test source code to understand expected behavior and contrasting it with the observed symptoms in execution logs. Prompted to act as a user, it describes the error and provides a reproduction script. To ensure the output captures the informal style of real community reports, the generation utilizes few-shot demonstrations from actual GitHub issues.

#### 5.6 End-to-End Workflow and Produced Artifacts

Given an environment-ready repository substrate (E), SWE-Scale executes a four-stage, fully parallelizable workflow:

- 1. Candidate enumeration and proposal. The engine enumerates candidate entities using the shared parsing backbone and entity analysis report. It then generates candidate bug specifications using a hybrid of procedural transformations (Section 5.4) and LLM-based modifications.
- 2. Patch materialization in sandboxes. Each candidate specification is dispatched to a disposable container (typically leased from the warm pool). Inside the sandbox, the candidate edit (whether byte-offset or LLM-generated code) is applied to the source, and a portable patch artifact (e.g., git diff) is extracted.
- 3. Distributed verification and filtering. The candidate patch is verified in an isolated Kubernetes pod: apply patch → run standardized verifier → parse results. Only candidates satisfying the behavioral validity criterion (non-empty TP2F) are retained.
- 4. Task packaging and Issue synthesis. The final output of SWE-Scale is a verified Data Package, instantiating the task family f = SWE-Scale within the unified task schema (Section 3.3). For each retained candidate, the engine synthesizes a user-like problem statement P and aggregates it with the repository spec R, the injected bug patch Pbug, the oracle O (the reference fix patch), the validation criteria V (the TP2F and TP2P partitions), and execution metadata M. This package is bound to the pinned execution environment E, finalizing a self-contained, executable artifact ready for downstream consumption.
- 5.7 Discussion: Quality, Triviality, and System-Level Limitations


Execution-based filtering ensures instances are active, but activeness is insufficient for high-quality data: trivial mutations (e.g., flipping a comparison) satisfy validity criteria yet offer limited learning signal. Moreover, entity-local transformations are inherently biased toward localized failures, failing to capture system-level regressions where symptoms are separated from their root causes by architectural layers.

These limitations drive two key implications. First, scaling synthesis throughput requires robust environment automation (Section 4). Second, achieving system-level realism necessitates reasoning beyond local edits. To address this, SWE-Hub introduces Bug Agent (Section 6), an independent product line that targets complex, cross-module regressions and generates realistic, symptom-centric issue reports on the shared execution substrate.

### 6 Realism-Oriented Synthesis: Bug Agent and Issue Agent

While high-throughput synthesis (Section 5) is necessary for scale, it is insufficient for realism. Entitylocal mutations tend to produce failures with a local footprint: the injected edit is in close proximity to the failing assertion, and the task description often inherits implementation details that leak the root cause. Real-world incidents exhibit distinct characteristics: regressions frequently stem from crossmodule interactions, configuration-sensitive behavior, or violated assumptions at API boundaries, while issue reports typically emphasize observable symptoms and reproduction evidence rather than causal

Table 1: Taxonomy of Procedural Modifiers in SWE-Scale.

Category Modifier Action Bug Type Operational Op. Change Replace operator with group sibling (e.g.,

Operator Misuse

+ → −).

Op. Flip Invert boolean/comparison logic (e.g., >

Logic Inversion

→ ≤).

Operand Swap Swap L/R operands (a,b → b,a). Order Error Chain Break Replace full expression with sub-operand

Data Loss

(a + b → a).

Const. Mod Apply ±1 to integer literals. Off-by-one

Control Flow Branch Swap Swap if body with else/elif body. Logic Reversal

Stmt Shuffle Reorder statements within function scope. Temporal Coupling Structural Block Drop Remove entire Loop, Conditional, or As-

Missing Logic

signment.

Wrap. Drop Remove try/with block and its content. Missing Feature Wrap. Unwrap Remove try/with keyword, keep content. Unsafe Execution

Class-Oriented Base Drop Remove inherited base classes. Broken Polymorphism Mem. Shuffle Reorder methods/fields within a class. Declaration Order Method Drop Remove method definition. Missing Interface

explanations. To bridge this realism gap (Figure 4), SWE-Hub introduces a dedicated Realism Layer comprising two specialized agents: the Bug Agent, which synthesizes system-level regressions, and the Issue Agent, which converts verified regressions into user-like issue reports under strict anti-leakage constraints.

Section contributions. This section makes two primary contributions: (i) the Bug Agent, a regression synthesis engine that targets system-level, non-local failures via contract-violating edits to mimic realworld debugging complexity; and (ii) the Issue Agent, a symptom-centric reporting module that enforces strict symptom-cause separation to generate leakage-resistant, user-like problem statements.

#### 6.1 Bug Agent: System-Level Regression Synthesis

Operational definition. We define a system-level regression as a verified behavioral failure where the cause, symptom, or both are non-local. The injected change affects an interface, invariant, or cross-module contract such that failing tests manifest in components that are not co-located with the edit—often separated by file boundaries, module calls, or architectural layers. Unlike local mutation strategies, Bug Agent explicitly targets such regressions to maximize diagnostic depth.

Design principle: contract violations with ripple effects. Bug Agent is guided by a “ripple effect” principle: realistic regressions often originate from changes that appear plausible from an engineering standpoint (e.g., refactors, performance optimizations, or API cleanups) but subtly violate an implicit contract relied upon by downstream components. This creates failures that manifest remotely, thereby increasing diagnostic difficulty and better mimicking real-world debugging scenarios. Concretely, Bug Agent prioritizes edits that (i) preserve local syntactic validity and compilation, (ii) resemble coherent block-level modifications, and (iii) are likely to perturb cross-component behavior (e.g., altering boundary checks, default values, ordering guarantees, serialization formats, or configuration-sensitive branches).

#### 6.1.1 Workflow: Context–Edit–Verify Loop

- Figure 4 illustrates the end-to-end pipeline of this layer. Bug Agent follows a structured reasoningverification loop grounded in execution:


1. Context audit and target selection. The agent identifies candidate hotspots that are (a) exercised by the test suite and (b) structurally connected to other components (via callers, callees, shared data

Realism-Oriented Synthesis: Bug Agent and Issue Agent

Issue Agent

Repo Analyze Bug Agent

Logic Layer

Logic Layer

Call Graph

Bug Patch P2F Error Logs

User Tone

Explore Repo

Bug Injection

Report Quality

Professional

Data Package

Real Repository

Log Dump

Confused Frustrated Minimalist

Snippet

- • Bug Patch
- • Issue Report
- • P2F Tests
- • F2P Tests
- • Pinned Env


Verification

Reproduction

Test Baseline

Static Analysis

Test Execution

Bug Patch P2F Error Logs

Final Issue Report

Example Layer

Example Layer

inject bug here

use view() instead of reshape() in torch/nn/functional.py

`RuntimeError` when passing transposed tensor to `nn.Linear` (view size mismatch?) Hi, I‘m running into a weird crash with a standard `Linear` layer. I have a tensor of shape `(Batch, Seq, Feature)`... Minimal Code to Reproduce: import torch … Stack Trace: Traceback (most recent call last): File "reproduce_issue.py", line 14, in <module> out = layer(x) …

Call Graph Test Baseline

user calls nn.Linear in user’s net

Key Outputs for Verification: Call Graph: Identifies callers,

callees, and shared data structures

RuntimeError: view size is not

compatible with input tensor's size…

RuntimeError: view size is not compatible with input tensor's size and stride

Test Baseline: Establishes a passto-fail (P2F) signal ground truth.

errors occur here

- Figure 4: Workflow of the Realism Layer in SWE-Hub. The pipeline initiates with Repo Analysis to extract call graphs and test baselines. The Bug Agent (center) then iteratively synthesizes system-level regressions that trigger non-local failures, validated by a Pass-to-Fail (P2F) signal. Finally, the Issue Agent (right) generates a user-like report from the verified regression, enforcing strict symptom-cause separation to prevent information leakage while adopting diverse personas.


structures, or configuration paths). It then retrieves extended context, including relevant call sites and associated tests.

- 2. Motivation sampling (plausible rationale). To steer edits toward realistic-looking patches rather than arbitrary corruption, the agent samples a refactoring “motivation” (e.g., performance optimization, code simplification, syntax modernization, or style consistency).
- 3. Block-level rewrite and injection. The agent performs coherent block-level changes (targeting loops, conditionals, boundary handling, or API glue) to introduce a subtle semantic fault while maintaining plausible code structure.
- 4. Execution-based verification. The injected patch is accepted only if it induces a pass-to-fail signal

under the repository verifier (Section 5.2). Verification yields structured traces (TP2F, logs) used both for filtering and for downstream issue generation.

- 5. Artifact materialization. The final output is a replayable regression instance: the bug injection patch, the pinned execution substrate reference, and verification metadata.

This loop ensures that realism-oriented synthesis remains fully compatible with SWE-Hub’s reproducibility guarantees: all accepted regressions are executable and auditable.

- 6.1.2 Regression Families Bug Agent supports two complementary regression families that cover common real-world failure modes:


Single-change ripple regressions. A localized but contract-breaking edit triggers failures in downstream components (e.g., callers relying on a specific boundary condition, ordering, or default behavior). The symptom is separated from the edit site by call chains or module boundaries, modeling non-local debugging scenarios.

Co-modification (multi-module) regressions. Coordinated changes are applied across coupled modules (e.g., partial migrations, API reshaping, or cross-file refactors). Individually reasonable edits interact negatively to produce a regression, reflecting failures introduced during large-scale maintenance and architectural cleanup.

These families complement the local mutation synthesis of SWE-Scale: they increase both the causal depth and the surface diversity of failures without abandoning execution-grounded verification.

#### 6.2 Issue Agent: Symptom-Centric Reporting with Anti-Leakage

A realistic SWE task requires not only a buggy state but also a natural problem statement that mirrors how failures are reported in the wild. Issue Agent translates a verified regression (comprising a bug patch and failing evidence) into an issue-style prompt that emphasizes symptoms and reproduction steps while rigorously avoiding causal hints.

#### 6.2.1 Persona and Evidence Diversity

Real issue reports exhibit wide variance in tone and evidence. Issue Agent samples from a set of report personas and evidence styles to mitigate template artifacts, including: concise user reports, maintainer-style reports with structured steps, and log-centric reports dominated by stack traces or error messages. This diversity improves the robustness of downstream agent training and better aligns with the heterogeneous distribution of real-world reports.

#### 6.2.2 Symptom–Cause Separation as Constrained Generation

Issue Agent enforces symptom–root cause separation through explicit constraints. Generated reports must:

- • describe observable behavior changes (expected vs. observed).
- • include reproduction steps and minimal evidence (logs, failing test names where appropriate).
- • avoid repair-oriented cues, such as naming the modified function/file as the cause, proposing specific fixes, or revealing implementation-level causal explanations.


We implement this as a post-generation validation step (a lightweight anti-leakage filter) that rejects reports violating the constraint set.

Minimal reproducible examples. When feasible, Issue Agent additionally synthesizes a minimal reproducible example (MRE) that isolates the symptom while remaining self-contained (e.g., using in-memory inputs). MRE generation is grounded in the same execution substrate and validated through the verifier interface, enhancing both realism and task usability.

#### 6.3 Produced Artifacts

The Realism Layer synthesizes a complete Data Package that instantiates the task family f = Bug Agent within the unified task schema (Section 3.3). The Bug Agent provides the core regression artifacts: the problem patch Pbug (the injected system-level regression), the validation criteria V (derived from the P2F signal), and implicitly defines the oracle O as the original repository baseline (the clean state before injection). The Issue Agent contributes the natural-language problem statement P, ensuring the prompt is symptom-centric and leakage-resistant. Combined with the repository spec R and pinned environment E, this forms a self-contained, high-fidelity task ready for evaluating agent capabilities in realistic debugging scenarios.

#### 6.4 Limitations: The Verification Coverage Paradox and Future Directions

As illustrated in Figure 4, the Realism Layer inherits a fundamental limitation of execution-grounded datasets: verification relies on an existing test oracle. This introduces survivorship bias—only regressions covered by available tests can be validated and retained—while real-world failures sometimes escape CI due to inadequate coverage.

###### SWE-Architect: Long-Horizon Repository Construction

DOC Agent

Structured Requirement

Scope Mining

(Macro View)

Doc(𝒫)

| | |
|---|---|
| | |


Readme

Project Description

Config

Summarize

Context

- 1. Project Description:

• High-Level Purpose & User

Behavior

- 2. Supports: Dependencies & Directory Layout
- 3. API Usage Guide: Signatures & Functional Contracts
- 4. Implementation Nodes: Disambiguating Input/Output Pairs


Directory

Real Repository

Supports

Tree

(Constraints)

Data Package

API Agent

- • Requirement Doc
- • Hollowing Patch
- • Hidden Tests
- • Pinned Env


(Micro View)

Coverage-Based Filtering

| | |
|---|---|
| | |


Source Code

API Usage

Guide

Extract Contracts & Examples

Implementation Nodes

Test Cases

Code Hollowing

Target Entities

Related

Strip Function Bodies

Tests

Hollowing Patch

Executable

Functions/Class es to implement

verification scope

ImplementationComplete Skeleton(ℛ Golden Patch

0)

- Figure 5: SWE-Architect pipeline. (1) Mine a cohesive task scope from a real repository using coverage structure.


(2) Create an initial repository state via code hollowing, and retain a golden reference patch. (3) Generate a structured requirement document via a two-agent reverse-engineering process (DOC Agent + API Agent). (4) Package the task with the pinned execution substrate and hidden tests in the unified task schema.

We refer to this tension as the Verification Coverage Paradox: the most severe and subtle regressions may be precisely those that are hardest to certify under existing tests. A promising direction is reverse test generation: when a plausibly injected regression does not trigger any failing tests, the system generates a targeted reproduction test that fails on the buggy version but passes on the clean baseline. This closes the loop by producing both a certified bug and a regression test artifact, improving coverage and task fidelity.

### 7 SWE-Architect: Long-Horizon Repository Construction

While repair-centric benchmarks provide strong signals for localized debugging, they systematically underevaluate an agent’s capacity to create: translating high-level requirements into coherent, repository-scale software. In many existing settings, edit scopes are heavily constrained (e.g., single-file patches, fixed signatures), allowing agents to succeed without making architectural decisions, managing dependencies, or maintaining global invariants. SWE-Architect expands the task space from repair to repository construction. Each task presents a structured requirement document and an incomplete repository state; the agent must produce a functional repository implementation that satisfies an executable test oracle. SWE-Architect is designed to impose long-horizon pressure while remaining objectively verifiable and scalable to diverse real-world repositories.

SWE-Architect explicitly targets four recurring challenges in complex development workflows:

- 1. Planning & termination (deciding what to build and defining completion criteria),
- 2. Global coherence (ensuring cross-file consistency and interface alignment),
- 3. Dependency management (handling libraries, build/test tooling, and runtime constraints), and
- 4. Long-range reasoning (linking high-level requirements to implementation details across architectural modules).


Section contributions. This section makes three primary contributions: (i) the SWE-Architect framework, which extends the SWE-Hub’s scope from repair to repository-scale construction, targeting longhorizon competencies like planning and dependency management; (ii) the task mining pipeline, utilizing code hollowing and coverage-based scope mining to generate executable, skeleton-based tasks from real repositories; and (iii) the agentic document generation process, employing DOC and API agents to reverse-engineer structured requirement documents that balance specificity with implementation leakage resistance.

#### 7.1 Task Definition and Execution Oracle

A SWE-Architect instance provides a structured natural-language specification P and an initial repository state R0 (typically a realistic skeleton with missing implementations). An agent produces a completed repository R′ = π(P,R0). Evaluation is strictly execution-grounded via a hidden test oracle:

V (R′) = I RunTests(R′,E,Thidden) = PASS ,

where E is the pinned execution substrate (container image + standardized verifier entrypoint provided by the Environment Layer), and Thidden is a private test suite. This definition ensures that success reflects repository-level functional correctness under a real verification harness, rather than surface-form similarity to a reference implementation.

#### 7.2 The Structured Requirement Document

A central design choice is to encapsulate the task specification into a single structured document that is (i) sufficiently detailed to guide implementation, yet (ii) abstract enough to prevent trivial copying and root-cause leakage. Each document comprises four sections:

- • Project Description: The purpose, goals, and user-facing behavior of the system.
- • System Constraints: Non-functional requirements including allowed dependencies, directory layout conventions, and runtime assumptions.
- • API Usage Guide: The functional contract—defining public interfaces, expected behaviors, semantic constraints, and cross-API invariants.
- • Implementation Examples: Concrete input/output examples for key APIs to disambiguate natural language requirements and clarify edge cases.


The document is written from an external, black-box perspective: it specifies interfaces and behaviors but deliberately excludes implementation code or internal causal explanations. This design encourages genuine planning and system design rather than simple template completion.

#### 7.3 From Real Repositories to SWE-Architect Instances

SWE-Architect is produced by a scalable task factory that converts real repositories into construction tasks while preserving executable evaluation guarantees. Figure 5 summarizes the pipeline.

#### 7.3.1 Mining Cohesive Scope via Coverage Structure

Directly requiring agents to rebuild entire repositories is neither scalable nor well-controlled. SWEArchitect instead derives a cohesive task scope from each repository by analyzing the coverage structure (e.g., a test-to-code coverage graph) to identify clusters of functionality that are internally cohesive and relatively isolated. The output is a candidate module package: a precise list of target entities (functions/classes with file paths) to be implemented, mapped to the corresponding evaluation tests. To maintain a clean boundary between implementation and verification, entities originating from test files are strictly excluded from the target set.

#### 7.3.2 Initial State and Golden Patch via Code Hollowing

To create a realistic construction setting, we generate the initial repository state R0 through code hollowing: we remove the bodies of target entities while strictly preserving the surrounding architecture (file hierarchy, imports, type/interface declarations, and non-target code). This yields a repository that retains the structural complexity of a real codebase, requiring the agent to implement missing functionality within an existing context rather than starting from an empty directory.

We also retain a golden patch (a git diff computed from the original repository) that restores all hollowed code. The golden patch serves two purposes: (i) it certifies solvability by construction (guaranteeing a correct solution exists), and (ii) it provides a precise scope definition used for quality control and debugging of the task generation process.

#### 7.4 Agentic Document Generation: DOC Agent and API Agent

Synthesizing a high-quality requirement document is itself a reverse-engineering task: it requires both highlevel project understanding and low-level API accuracy. SWE-Architect therefore employs a collaborative two-agent design.

DOC Agent (macro-level specification). DOC Agent extracts repository context (e.g., README, configuration, package metadata) to produce a PRD-like narrative covering the project purpose, functional goals, and infrastructure constraints (dependencies, directory conventions). It also organizes target entities into coherent functional groups, forming the structural backbone of the requirement document.

API Agent (micro-level contracts and examples). API Agent focuses on the target entities. For each entity, it derives: (i) a static interface contract (signatures, type annotations where available, exceptions/edge cases), and (ii) behavioral examples mined from tests or usage sites, reformatted as specification-level input/output nodes. These artifacts populate the API Usage Guide and Implementation Examples sections, ensuring technical rigor while keeping the document implementation-agnostic.

This division of labor mirrors the abstraction gap in software engineering: repository context is broad and unstructured, while API behavior is local but demands precise technical detail.

#### 7.5 Packaging into SWE-Hub

The final output of SWE-Architect is a complete Data Package that instantiates the task family f = SWE-Architect within the unified task schema (Section 3.3). The package aggregates the structured requirement document P, the initial state defined by the hollowing patch Pbug (which removes implementations), and the golden patch O (the reference solution). It also binds the validation criteria V—the hidden test suite Thidden—to the pinned execution environment E. This configuration ensures that the construction task is fully executable and allows for direct comparison with repair-oriented tasks under the SWE-Hub’s unified evaluation protocol.

### 8 Conclusion

We introduced SWE-Hub, a unified data factory for software engineering agents that produces tasks that are executable by construction. The core abstraction is a shared execution substrate—pinned container images plus a standardized verifier entrypoint—provisioned automatically by the Environment Layer (Env Agent + Test Agent) to ensure reproducibility across heterogeneous repositories. Built upon this substrate, SWE-Hub orchestrates three specialized product lines: (i) SWE-Scale, a stateless synthesisand-verification engine that enables Kubernetes-scale parallel validation and polyglot bug injection via a shared parsing backbone and configuration-as-code; (ii) the Realism Layer (Bug Agent + Issue Agent), which targets system-level regressions and generates user-like issue reports with explicit symptom–root cause separation to mitigate leakage; and (iii) SWE-Architect, which extends the evaluation horizon to repository construction, requiring agents to translate structured natural-language specifications into code validated against executable (often hidden) test oracles.

By treating SWE data generation as a modular production system rather than a one-off benchmark, SWE-Hub enables the continuous creation of diverse task families—spanning from short-horizon repair

to long-horizon construction—under a consistent verification contract. We posit that this factory paradigm establishes a robust foundation for more reliable training, more representative evaluation, and faster iteration of agentic SWE methods. Future directions include expanding to broader ecosystem coverage, incorporating richer regression modes (e.g., performance, security, concurrency), and closing the loop with automated test generation and adaptive curricula driven by agent feedback.

### References

Mouxiang Chen, Lei Zhang, Yunlong Feng, Xuwu Wang, Wenting Zhao, Ruisheng Cao, Jiaxi Yang, Jiawei Chen, Mingze Li, Zeyao Ma, Hao Ge, Zongmeng Zhang, Zeyu Cui, Dayiheng Liu, Jingren Zhou, Jianling Sun, Junyang Lin, and Binyuan Hui. 2026. Swe-universe: Scale real-world verifiable environments to millions. Preprint, arXiv:2602.02361.

Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Vijay Bharadwaj, Jeff Holm, Raja Aluri, Chen Bo Calvin Zhang, and 3 others. 2025. Swe-bench pro: Can ai agents solve long-horizon software engineering tasks? Preprint, arXiv:2509.16941.

Jingzhe Ding, Shengda Long, Changxin Pu, Huan Zhou, Hongwan Gao, Xiang Gao, Chao He, Yue Hou, Fei Hu, Zhaojian Li, Weiran Shi, Zaiyuan Wang, Daoguang Zan, Chenchen Zhang, Xiaoxu Zhang, Qizhi Chen, Xianfu Cheng, Bo Deng, Qingshui Gu, and 30 others. 2026. Nl2repo-bench: Towards long-horizon repository generation evaluation of coding agents. Preprint, arXiv:2512.12730.

Kelin Fu, Tianyu Liu, Zeyu Shang, Yingwei Ma, Jian Yang, Jiaheng Liu, and Kaigui Bian. 2025. Multi-docker-eval: A ‘shovel of the gold rush’ benchmark on automatic environment building for software engineering. Preprint, arXiv:2512.06915.

Xinyi He, Qian Liu, Mingzhe Du, Lin Yan, Zhijie Fan, Yiming Huang, Zejian Yuan, and Zejun Ma. 2025. Swe-perf: Can language models optimize code performance on real-world repositories? Preprint, arXiv:2507.12415.

Naman Jain, Jaskirat Singh, Manish Shetty, Liang Zheng, Koushik Sen, and Ion Stoica. 2025. R2e-gym: Procedural environments and hybrid verifiers for scaling open-weights swe agents. Preprint, arXiv:2504.07164.

Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.

2024. Swe-bench: Can language models resolve real-world github issues? Preprint, arXiv:2310.06770. Kubernetes. 2014. Kubernetes: Production-grade container scheduling and management. Accessed 2026-02-05. OpenAI. 2024. Introducing swe-bench verified. Accessed 2026-02-05. Jiayi Pan, Xingyao Wang, Graham Neubig, Navdeep Jaitly, Heng Ji, Alane Suhr, and Yizhe Zhang. 2025. Training

software engineering agents and verifiers with swe-gym. Preprint, arXiv:2412.21139.

Minh V. T. Pham, Huy N. Phan, Hoang N. Phan, Cuong Le Chi, Tien N. Nguyen, and Nghi D. Q. Bui. 2025. Swe-synth: Synthesizing verifiable bug-fix data to enable large language models in resolving real-world bugs. Preprint, arXiv:2504.14757.

Qwen Team. Qwen3-coder-next technical report. Technical report. Accessed: 2026-02-03. KaShun Shum, Binyuan Hui, Jiawei Chen, Lei Zhang, X. W., Jiaxi Yang, Yuzhen Huang, Junyang Lin, and Junxian

He. 2025. Swe-rm: Execution-free feedback for software engineering agents. Preprint, arXiv:2512.21919.

Yueqi Song, Ketan Ramaneti, Zaid Sheikh, Ziru Chen, Boyu Gou, Tianbao Xie, Yiheng Xu, Danyang Zhang, Apurva Gandhi, Fan Yang, Joseph Liu, Tianyue Ou, Zhihao Yuan, Frank Xu, Shuyan Zhou, Xingyao Wang, Xiang Yue, Tao Yu, Huan Sun, and 2 others. 2025. Agent data protocol: Unifying datasets for diverse, effective fine-tuning of llm agents. Preprint, arXiv:2510.24702.

Chaofan Tao, Jierun Chen, Yuxin Jiang, Kaiqi Kou, Shaowei Wang, Ruoyu Wang, Xiaohui Li, Sidi Yang, Yiming Du, Jianbo Dai, Zhiming Mao, Xinyu Wang, Lifeng Shang, and Haoli Bai. 2026. Swe-lego: Pushing the limits of supervised fine-tuning for software issue resolving. Preprint, arXiv:2601.01426.

Minh V. T. Thai, Tue Le, Dung Nguyen Manh, Huy Phan Nhat, and Nghi D. Q. Bui. 2026. Swe-evo: Benchmarking coding agents in long-horizon software evolution scenarios. Preprint, arXiv:2512.18470.

Tree-sitter. 2015. Tree-sitter: An incremental parsing system for programming tools. Accessed 2026-02-05.

Junhao Wang, Daoguang Zan, Shulin Xin, Siyao Liu, Yurong Wu, and Kai Shen. 2025a. Swe-mirror: Scaling issue-resolving datasets by mirroring issues across repositories. Preprint, arXiv:2509.08724.

Lilin Wang, Lucas Ramalho, Alan Celestino, Phuc Anthony Pham, Yu Liu, Umang Kumar Sinha, Andres Portillo, Onassis Osunwa, and Gabriel Maduekwe. 2025b. Swe-bench++: A framework for the scalable generation of software engineering benchmarks from open-source repositories. Preprint, arXiv:2512.17419.

Yuxiang Wei, Zhiqing Sun, Emily McMilin, Jonas Gehring, David Zhang, Gabriel Synnaeve, Daniel Fried, Lingming Zhang, and Sida Wang. 2025. Toward training superintelligent software agents through self-play swe-rl. Preprint, arXiv:2512.18552.

Yisen Xu, Jinqiu Yang, Tse-Hsun, and Chen. 2026. Swe-refactor: A repository-level benchmark for real-world llm-based code refactoring. Preprint, arXiv:2602.03712.

John Yang, Kilian Lieret, Carlos E. Jimenez, Alexander Wettig, Kabir Khandpur, Yanzhe Zhang, Binyuan Hui, Ofir Press, Ludwig Schmidt, and Diyi Yang. 2025. Swe-smith: Scaling data for software engineering agents. Preprint, arXiv:2504.21798.

Daoguang Zan, Zhirong Huang, Wei Liu, Hanwu Chen, Linhao Zhang, Shulin Xin, Lu Chen, Qi Liu, Xiaojian Zhong, Aoyan Li, Siyao Liu, Yongsheng Xiao, Liangqiang Chen, Yuyu Zhang, Jing Su, Tianyu Liu, Rui Long, Kai Shen, and Liang Xiang. 2025. Multi-swe-bench: A multilingual benchmark for issue resolving. Preprint, arXiv:2504.02605.

Liang Zeng, Yongcong Li, Yuzhen Xiao, Changshi Li, Chris Yuhao Liu, Rui Yan, Tianwen Wei, Jujie He, Xuchen Song, Yang Liu, and Yahui Zhou. 2025. Skywork-swe: Unveiling data scaling laws for software engineering in llms. Preprint, arXiv:2506.19290.

Zizheng Zhan, Ken Deng, Huaixi Tang, Wen Xiang, Kun Wu, Weihao Li, Wenqiang Zhu, Jingxuan Xu, Lecheng Huang, Zongxian Feng, Shaojie Wang, Shangpeng Yan, Xuxing Chen, Jiaheng Liu, Zhongyuan Peng, Zuchen Gao, Haoyang Huang, Xiaojiang Zhang, Jinghui Wang, and 11 others. 2025. Kat-v1: Kwai-autothink technical report. Preprint, arXiv:2507.08297.

Lei Zhang, Jiaxi Yang, Min Yang, Jian Yang, Mouxiang Chen, Jiajun Zhang, Zeyu Cui, Binyuan Hui, and Junyang Lin. 2025. Swe-flow: Synthesizing software engineering data in a test-driven manner. Preprint, arXiv:2506.09003.

### Core Contributors

- • Yucheng Zeng‡
- • Shupeng Li‡
- • Daxiang Dong‡
- • Ruijie Xu
- • Zimo Chen
- • Liwei Zheng
- • Yuxuan Li


- • Zhe Zhou
- • Haotian Zhao
- • Lun Tian
- • Heng Xiao
- • Tianshu Zhu
- • Longkun Hao
- • Jianmin Wu†


‡ Project Leader. † Project Sponsor.

