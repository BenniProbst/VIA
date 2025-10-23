# Research Exposé: Analysis of a Research Topic - Process Communication

**Title**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Author**: Benjamin-Elias Probst
**Supervisors**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Faculty of Computer Science
**Date**: October 2025

---

_Note: This is a copy of the complete research exposé from `playbooks/Analyse_eines_Forschungsthemas_Expose.md` for project documentation. The original in playbooks/ continues to serve as a working document._

---

For the complete English version (763 lines) of the research exposé, please see this document.

The exposé comprises:
- Chapter 1: Introduction and Motivation (Initial Situation, Vision Industry 5.0, Research Gap)
- Chapter 2: Problem Statement and Research Question (VIA Overall System, Process-Group-Protocol, 8 Sub-problems)
- Chapter 3: State of Research (AAS, OPC UA, MMB, CMFM, SOA, IPC & Service Mesh)
- Chapter 4: Objectives and Research Methodology (Main Objective, Sub-Objectives, 6-Phase Plan)
- Chapter 5: Theoretical Background (Compiler Theory, Metamodels, AAS, OPC UA, CMFM)
- Chapter 6: Conceptual Approach (VIA Main Program, M3-Compiler, M2-SDK-Compiler, M1-Deployer, Sub-Protocols)
- Chapter 7: Expected Results (Scientific Contributions, Practical Results, Automotive Production Use-Case)
- Chapter 8: Timeline (6 Phases, 24 Weeks)
- Chapter 9: Bibliography (27 Sources)

## Summary

VIA (Virtual Industry Automation) is a research project at TU Dresden that develops a **self-compiling bootstrap mechanism** for Industry 4.0 automation. The system transforms metamodel definitions through a compiler chain (M3→M2→M1) into deployed industrial systems for 50,000+ edge devices.

### Central Research Question

> Can process chains of microservices be automatically created via metamodels (M3/M2), whose positioning in the system and communication mechanism (IPC: Pipe, Socket, TCP, File-Queue, Thread) are optimized during compilation?

### Core Components

#### 1. VIA-M3-Compiler (Metamodel → SDK)
- **Input**: AAS IEC 63278 Text Specification, OPC UA IEC 62541, VIA-Extensions
- **Processing**: C++20/23 Metaprogramming, Custom Template-Engine in AAS-lang, Protobuf as M3-Interpreter
- **Output**: C++ SDK, OPC UA NodeSet XML, Protobuf `.proto` Files

#### 2. VIA-M2-SDK-Compiler (SDK → Customer System) → **Research Core**
- **Input**: Customer Project `.via` Files, Optional: Network Topology
- **Processing**:
  - Network Discovery (SNMP/OPC UA/Modbus Scanner)
  - **IPC Optimizer**: Graph-based Compile-Time-Optimization (Pareto-Frontier)
  - Test Generator: Automatic Tests from M3 Constraints
- **Output**: C++ Complete Project, Kubernetes Manifests, Edge-Modules

#### 3. VIA-M1-System-Deployer (System → Production)
- **Input**: M1 System Project, Deployment-Targets (MIPS, RISC-V, ARM, x86, etc.)
- **Processing**:
  - Cross-Compilation (Multi-Architecture Toolchain Management)
  - Horse-Rider-Deployment (C++23 Modules, Hot-Reload, Canary)
  - Distributed Build (parallel builds via GitHub Runners)
- **Output**: Deployed System for >50,000 Edge Devices, Digital Twin

#### 4. Sub-Protocols under OPC UA
- **Edge-Group-Protocol**: Virtual Network Groups, hierarchical edge device grouping
- **Deploy-Protocol**: Versioning, System Updates, Telemetry, In-the-Loop Self-Optimization
- **Process-Group-Protocol** (Research Focus): IPC-Optimization, Pareto-Optimization (Latency/Throughput/Resources)

### Hypotheses

- **H1**: Compiler-based IPC optimization reduces latency by >30% compared to runtime service mesh
- **H2**: Static positioning achieves 90% of the efficiency of dynamic orchestration
- **H3**: Process-Group-Protocol scales linearly to 100,000 services
- **H4**: Metamodel-based abstraction reduces manual development time by 60%

### Scientific Value

1. **M3-Library-Architecture**: MMB as reusable M3-Library, Protocol Composition
2. **Pareto-Optimization**: Formally solvable optimization problem with Z3 Constraint-Solver
3. **Autonomous Systems**: In-the-Loop Self-Optimization via Telemetry-Feedback
4. **Nested Security**: Recursive security levels per protocol layer
5. **Interdisciplinary**: Bridge between Compiler-Design ↔ Industrial Automation

### Technology Stack

- **Languages**: C++20/23, AAS-lang (custom DSL), Protobuf
- **Protocols**: OPC UA (IEC 62541), gRPC, IPC-Mechanisms
- **Deployment**: Kubernetes, C++23 Modules (Horse-Rider pattern)
- **Optimization**: Z3 Constraint Solver, Pareto-Optimization
- **Architectures**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc

### Timeline (24 Weeks)

- **Phase 1**: Research & Analysis ✅ COMPLETED (4 Weeks)
- **Phase 2**: Playbook & M3-Metamodel-Design ⏳ IN PROGRESS (2 Weeks)
- **Phase 3**: M2-SDK-Compiler Prototype with IPC-Optimizer (6 Weeks)
- **Phase 4**: Benchmark-Suite & Use-Case (4 Weeks)
- **Phase 5**: Evaluation & Comparative Measurements (4 Weeks)
- **Phase 6**: Documentation & Publication (4 Weeks)

---

## 1. Introduction and Motivation

### 1.1 Initial Situation

Industrial automation faces the challenge of integrating heterogeneous systems with different protocols, architectures, and communication patterns. As part of research at the Chair of Industrial Communication Technology at TU Dresden under Prof. Dr.-Ing. habil. Martin Wollschlaeger, the Asset Administration Shell (AAS) framework according to IEC 63278 was developed as a standardized approach for digital twins in Industry 4.0, or from a digital perspective Industry 3.2. The aas-core-works implementation supervised by Santiago Soler Perez Olaya reveals a complete compiler architecture based on an M3/M2/M1 metamodel structure – analogous to approaches by Prof. Castrillon in compiler design at TU Dresden.

The current implementation of the AAS framework uses Python scripts that simulate compiler functionality: The aas-core-meta repository defines the M3 metamodel in simplified Python, while aas-core-codegen generates target language SDKs (C++, C#, Python, TypeScript, Java, Golang). Despite this functional code generation, a complete compiler implementation as an external translation program that can be used as a standalone, maintainable tool in industrial production environments is missing.

VIA (Virtual Industry Automation) addresses this gap through a **self-compiling bootstrap mechanism**: The VIA main program first compiles the M3 compiler from AAS metamodel definitions, tests it, and uses it to generate the M2 SDK. This SDK is then compiled, tested, and used to translate customer projects (M2→M1). A Software-in-the-Loop (SITL) system automates the AI-assisted transformation of textual specifications (AAS IEC 63278, OPC UA IEC 62541) into executable M3 model code, as well as fully autonomous adaptation, implementation, and testing of program code (System on call / SOC). While aas-core-works generates static SDKs, VIA enables through this bootstrap approach a continuous automation from textual specification to deployed industrial system – including the capability for self-modification and hot-reload of the main program during operation.

### 1.2 Vision: Industry 5.0 (Or Better: Industry 3.3)

The next generation of industrial automation – Industry 5.0 – requires a fundamental paradigm shift: Instead of manual system configuration and programming, AI-driven system description should be enabled, where users describe their system in natural language. The target system performs automatic compilation and deployment, with Software-in-the-Loop procedures enabling iterative error correction against customer specifications. The long-term goal of this research vision is: "The customer describes their system to the AI, the AI defines a compiler description, the compiler generates the functional system."

Thinking this step further, the customer can define systems that define themselves or construct systems that independently handle the architecture and definition part, resulting in M3 self-definition and construction.

This vision requires continuous automation from abstract metamodel to deployed system on heterogeneous edge devices. VIA (Virtual Industry Automation) pursues this approach through a multi-stage compiler chain (M3→M2→M1), which first generates an SDK from a metamodel (M3→M2), creates system projects from customer projects (M2→M1), and finally deploys these to over 50,000 edge devices (M1 deployment).

### 1.3 Research Gap

Despite existing metamodel frameworks and code generators, a fundamental research gap exists between metamodel definition and production-grade compiler implementation. Previous approaches like aas-core-codegen generate executable code, but the connection to automated deployment is missing: There is no maintainable, versioned SDK generation for long-term industrial use (typically 15-25 years in manufacturing), no automatic orchestration of generated systems, and no optimization of process communication at compile time.

Manual orchestration of more than 50,000 edge devices in a typical automotive factory is practically unreasonable and error-prone. Additionally, heterogeneous target architectures (MIPS, RISC-V, POWER9, x86, ARM, Sparc) require multi-target compilation not provided in previous AAS implementations. In particular, a scientific investigation is missing on whether and how microservice communication (IPC: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) can be optimized at compile time to reduce latency and resource consumption compared to runtime orchestration.

---

## 2. Problem Statement and Research Question

### 2.1 Context: VIA Overall System

VIA (Virtual Industry Automation) forms the overarching context of this research. It is a multi-stage compiler chain (M3→M2→M1) for heterogeneous industrial systems with automatic orchestration of more than 50,000 edge devices. The overall system consists of three main components: The **M3 Compiler** transforms the AAS metamodel into a language-specific SDK (C++, Python, Java), the **M2 SDK Compiler** converts customer projects including network discovery into complete system projects, and the **M1 System Deployer** performs cross-compilation, Horse-Rider deployment, and Kubernetes orchestration.

This architecture enables continuous automation from abstract system description to deployed system on heterogeneous hardware platforms. While the VIA overall system covers all aspects from metamodeling to deployment, this research focuses on a specific, critical sub-aspect: optimization of process communication at compile time.

### 2.2 Focus of This Research: Process-Group-Protocol

The central research question of this work is:

> **Can process chains of microservices be automatically created via metamodels (M3/M2), whose positioning in the system and communication mechanism (IPC: Pipe, Socket, TCP, File-Queue, Thread) are optimized during compilation?**

This question addresses a fundamental challenge of modern microservice architectures: The choice of Inter-Process Communication (IPC) mechanism is typically made at runtime by service mesh solutions like Istio or Linkerd. However, these runtime decisions cause overhead through dynamic routing, service discovery, and load balancing. This work investigates whether static optimization through compile-time analysis of the metamodel is possible, reducing latency without significantly limiting flexibility.

For systematic treatment of this research question, four sub-questions are formulated:

1. **Metamodel Elements**: Which M3 model elements are necessary to describe process communication (dependencies, data flows, latency requirements)?

2. **IPC Derivation**: How can the M2 SDK compiler derive optimal IPC mechanisms from process dependencies? Which heuristics determine whether Pipe (same host, low overhead), Unix Socket (same host, higher flexibility), TCP (remote, highest flexibility), File-Queue (asynchronous, persistent), or Thread-Messaging (same process, lowest latency) is chosen?

3. **Positioning Metrics**: Which metrics determine the positioning of microservices (same container, same host, same cluster node, remote)? How are latency requirements, resource availability, and fault tolerance weighted?

4. **Scalability**: How does the Process-Group-Protocol behave under OPC UA with more than 50,000 devices? Can hierarchical grouping (Edge-Groups → Cluster-Groups → Global) achieve linear scaling behavior?

For validation of the research hypothesis, four measurable hypotheses are established:

- **H1 (Latency)**: Compiler-based IPC optimization reduces latency by at least 30% compared to runtime service mesh solutions
- **H2 (Efficiency)**: Static positioning decision at compile time achieves at least 90% of the efficiency of dynamic runtime orchestration
- **H3 (Scalability)**: The Process-Group-Protocol scales linearly to 100,000 services with hierarchical grouping
- **H4 (Development Time)**: Metamodel-based abstraction reduces manual development time by at least 60%

**Delimitation**: This work focuses on the **Process-Group-Protocol subsystem** as part of the VIA overall system. The M3/M2/M1 architecture serves as context and theoretical framework but is not implemented in all details. In particular, M3 compiler optimizations, multi-architecture cross-compilation, and complete Horse-Rider deployment are assumed as given and not independently researched.

### 2.3 Sub-problems of the Overall System (Context)

The VIA overall system is structured into eight sub-problems, documented in the project structure under `playbooks/` as separate implementation playbooks. While this work focuses on the Process-Group-Protocol (2.3.5), understanding all components is necessary as they form the execution environment for process communication.

#### 2.3.0 Main Program (Orchestration M3→M2→M1)

**Project Location**: `src/main.cpp` (versioned, not in gitignore)

The VIA main program orchestrates the entire bootstrap cycle through sequential compilation and testing of the compiler stages:

1. **M3-Compiler-Build**: Compiles `playbooks/VIA-M3-Compiler/` via CMake → `build/via-m3-compiler` binary
2. **M3-Compiler-Test**: Executes M3 test framework, validates AAS-lang parsing
3. **M2-SDK-Generation**: Executes `via-m3-compiler` → generates `playbooks/VIA-M2-SDK/` (gitignored)
4. **M2-SDK-Build**: Compiles generated SDK → `build/via-m2-sdk-compiler` binary
5. **Customer-Project-Compilation**: Loads customer project files (`.via` format), compiles with M2-SDK → `playbooks/VIA-M1-System/` (gitignored, C++ complete project)
6. **M1-System-Build**: Compiles M1 project for all target architectures → `build/binaries/{arch}/` directories
7. **Deployment**: Distributes binaries via Horse-Rider architecture to edge devices
8. **Server Mode**: Switches to OPC UA server mode, accepts recompilation requests from administrators

**Self-Reference Mechanism**: Upon recompilation request, the main program compiles itself anew (M3→M2→M1→M0), starts a new VIA instance via process communication, and terminates itself after successful handover.

**Multi-Level Debugging and Error Traceability**: When an error occurs in a process chain of the M0-compiled system, the main program maintains a comprehensive tracing model across all compilation stages. This enables seamless error tracking from the deployed binary (M0) through the system project (M1), the generated SDK (M2), back to the original M3 model definition and customer project definition. Since each lower meta-level is an implementation of a higher meta-level, a complete conceptual representation emerges across all layers. The VIA debugger can penetrate backwards through multiple layers and maintains multiple program counters simultaneously, spanning different model files (`.aas`, `.via`) and generated C++ source files – analogous to the gdb debugger, which can also debug across multiple layers of the g++ compiler architecture (Frontend → Middle-End → Backend → Assembly → Binary). This multi-level debugging capability is essential for the maintainability of industrial systems, as errors can be traced directly to their conceptual cause in the metamodel specification, rather than merely analyzing symptoms in generated code.

**Problem**: State management across 3 phases, error handling at each stage, transactionality during self-recompilation, overhead of multi-level tracing in production systems

#### 2.3.1 M3-Level (Metamodel-Compiler)

The M3-Compiler, located in `playbooks/VIA-M3-Compiler/` as a versioned component of the repository, defines the AAS-lang (Asset Administration Shell Language) as a domain-specific programming language for industrial systems. This compiler component forms the first stage of the VIA compiler chain and is responsible for transforming abstract metamodel definitions (M3) into a type-safe C++ SDK (M2).

The M3-Compiler receives as input the AAS IEC 63278 text specification, which is automatically transformed into executable M3 model code via the SITL system (Software-in-the-Loop). Additionally, it processes OPC UA IEC 62541 as an M3 library, also read via SITL if not yet available, as well as VIA extensions for process communication as custom M3 definitions. These inputs form the formal foundation for subsequent SDK generation.

Processing is performed by a custom template engine, defined in AAS-lang itself and building on C++20/23 metaprogramming. As the M3 interpreter, Protobuf from the `third_party/` directory is used to read model and customer data. An integrated constraint system validates type safety and prevents the emergence of spaghetti code through rigorous modularization of the generated SDK.

As output, the M3-Compiler generates the directory `playbooks/VIA-M2-SDK/` with complete C++ SDK code (gitignored, as generated), OPC UA NodeSet XML files for the VIA Custom Companion Specification, Protobuf `.proto` files for microservice communication between services, and comprehensive documentation with propagated M3 comments that reach into the binary headers.

The central challenge of this component lies in avoiding spaghetti code during automatic code generation. This is addressed through a multi-layered constraint system that guarantees type safety, modularity, and maintainability of the generated SDK.

#### 2.3.2 M2-Level (SDK-Compiler)

**Project Location**: `playbooks/VIA-M2-SDK/` (generated, gitignored)

The M2-SDK functions as a compiler for customer projects. It reads `.via` project files (written in AAS-lang), validates syntax, and compiles into a C++ complete project (M1).

The planned playbook structure comprises four sub-components addressing various aspects of SDK functionality. The `network_discovery.md` playbook describes an SNMP/OPC UA/Modbus scanner for automatic topology recognition in the customer network. The `ipc_optimizer.md` playbook implements a graph-based algorithm for IPC mechanism selection and forms the research focus of this work. The `auto_suggestions.md` playbook enables AI-assisted suggestions for system configuration based on recognized network topology. Finally, `test_generator.md` defines automatic generation of deterministic tests from M3 constraints to ensure complete test coverage.

As input, the M2-SDK receives customer project files in `.via` format under `customer_project/*.via` and optionally a network topology determined via the Network Discovery System. Processing of these inputs results in three main outputs: The directory `playbooks/VIA-M1-System/` contains the complete C++ project (gitignored, as generated), Kubernetes manifests are provided as `deployment.yaml`, and automatically generated tests contain propagated customer comments for complete traceability.

The central challenge of this component lies in deterministic test coverage for industrial combinatorics as well as IPC optimization for more than 50,000 services, requiring scalable algorithms and efficient heuristics.

#### 2.3.3 M1-Level (System-Deployment)

**Project Location**: `playbooks/VIA-M1-System-Deploy/` (Playbooks for deployment logic)

The M1-Deployer compiles the M1 system project (C++ code) into binaries for all target architectures and distributes them via the Horse-Rider deployment system.

The architecture comprises three sub-components covering different deployment aspects. The `cross_compilation.md` playbook describes multi-architecture toolchain management for MIPS, RISC-V, ARM, x86, and other platforms, addressing heterogeneous industrial environments with legacy systems. The `horse_rider_deployment.md` playbook implements C++23 Modules with stable ABIs, hot-reload mechanisms, and canary deployment for fault-tolerant updates. The `distributed_build.md` playbook orchestrates parallel builds across GitHub Runners to significantly reduce compilation time for large systems.

The M1-Deployer generates three categories of outputs. Compiled binaries are stored architecture-specifically in the directory structure `build/binaries/{arch}/{device_id}/`, with each edge device receiving its dedicated binary. Deployment manifests for Kubernetes and edge devices enable automated rollouts via container orchestration. Versioned binaries with header documentation allow external edge programming by third-party systems that can link against stable VIA ABIs.

The central challenges of this component lie in hot-reload without system downtime, canary deployment with automatic rollback on errors, version consistency for C++23 Modules across multiple compiler generations, and ABI stability for long-term industrial compatibility (typically 15-25 years).

#### 2.3.4 Deployment System (Horse-Rider Architecture)

**Project Location**: Part of `playbooks/VIA-M1-System-Deploy/horse_rider_deployment.md`

The Horse-Rider architecture decouples deployment logic (Horse) from business logic (Rider) through modular separation of responsibilities. The Horse service functions as a stable container that dynamically loads and unloads Rider services as C++23 Modules at runtime, enabling hot-reload without system downtime. During a Rider update, the Horse first checks ABI compatibility of the new module against defined interfaces. It then loads the new module parallel to the old one (canary deployment) and initially routes only a small percentage of traffic to the new service. Upon successful canary test, complete traffic switch to the new Rider occurs, while errors trigger automatic rollback to the old module. The architecture provides for at least two parallel Horses per edge device, functioning as a digital twin and ensuring mutual redundancy.

The central technical challenges of this architecture lie in ABI stability for C++23 Modules across multiple compiler versions and update cycles, state synchronization during hot-reload between old and new Rider service, and rollback transactionality ensuring that a consistent system state can be restored within fractions of seconds upon errors.

#### 2.3.5 Sub-Protocols under OPC UA → **RESEARCH FOCUS**

**Project Location**: `playbooks/VIA-M3-Compiler/via_protocols/` (future, specification still open)

VIA defines three custom OPC UA sub-protocols as systematic extensions of the standard, addressing various aspects of system orchestration. The Edge-Group-Protocol enables virtual network groups for hierarchical edge device grouping, achieving scalability to more than 50,000 devices. The Deploy-Protocol manages versioning, logging, and rejuvenation for the Horse-Rider system to ensure fault-tolerant updates. The Process-Group-Protocol forms the core of this research work and optimizes IPC mechanisms between services through automatic selection between Pipe, Unix Socket, TCP, File-Queue, and Thread-Messaging based on process dependencies and latency requirements.

Implementation of these protocols occurs as an M3 library (`via_protocols` lib) within AAS-lang, allowing them to be processed by the VIA-M3-Compiler and integrated into the M2-SDK. Planned MMB integration (Multi-Message Broker according to Santiago Soler Perez Olaya) enables many-to-many broadcast communication for flexible message distribution between heterogeneous process groups.

The current status of this component is the specification phase; concrete protocol definitions will be elaborated in the further project course as M3 models. Central challenges lie in protocol composition of different sub-protocols without semantic conflicts, efficiency for more than 50,000 devices through hierarchical grouping, definition of nested security layers, and future standardization by the OPC Foundation as an official Companion Specification.

#### 2.3.6 Network Discovery System

**Project Location**: Part of `playbooks/VIA-M2-SDK/network_discovery.md`

The Network Discovery System performs automatic scanning of the customer network by systematically employing various industrial protocols such as SNMP, OPC UA, Modbus, MQTT, and RPC for topology recognition. The system reads device properties from PLCs, SCADA systems, MES servers, and sensors, automatically classifies them, and creates a structured network topology. Based on this analysis, the system generates asset mapping suggestions for M2 project configuration, serving users as a starting point for further system definition.

Essential challenges of this component lie in protocol heterogeneity of various industry standards with different data models and communication patterns, access control to security-critical production systems without existing credentials, and handling offline devices that are not reachable at scan time but must still be integrated into the topology.

#### 2.3.7 Master Active Management (Deployment Orchestration)

**Project Location**: Part of `playbooks/VIA-M1-System-Deploy/master_active_management.md`

Master Active Management implements Active/Active redundancy analogous to Microsoft Active Directory, where multiple deployment masters are simultaneously active and replicate each other. The Deployment Master coordinates both Kubernetes container orchestration and edge service orchestration for non-containerized devices, thus forming the central control instance of the VIA system. Access control is managed via a role-based permission system that defines users and roles and can optionally be integrated with existing Samba or Active Directory infrastructures. Configuration of redundancy levels and service distribution occurs through policies that determine how many replicas of each service are deployed on which hosts.

Critical challenges of this component lie in avoiding split-brain scenarios where separate master instances make inconsistent decisions, ensuring consistency across geographically distributed clusters, and minimizing failover times upon master failure to guarantee continuous orchestration.

#### 2.3.8 Multi-Architecture Cross-Compilation

**Project Location**: Part of `playbooks/VIA-M1-System-Deploy/cross_compilation.md`

The Multi-Architecture Cross-Compilation System enables support for heterogeneous hardware platforms, including MIPS, RISC-V, POWER9+, x86, ARM1+, and Sparc, each on operating systems like Linux, Windows, and macOS. The M2-SDK customer declaratively defines desired target architectures in `.via` project files, whereupon the M1-Deployer automatically configures CMake toolchains for all targets and performs parallel cross-compilation. This architectural diversity enables legacy support for old industrial systems that have sometimes been in production for decades, while simultaneously integrating modern architectures for new components.

Essential challenges of this component lie in toolchain management for a multitude of compiler versions and target platforms, driver availability for specific hardware components on legacy systems, and differing memory models of various architectures (e.g., big-endian vs. little-endian, different pointer sizes), requiring consistent data serialization and IPC communication across architectural boundaries.

---

## 3. State of Research

The research builds on several established standards and research results, systematically presented below. The analysis covers AAS code generation (Section 3.1), OPC UA as communication protocol (Section 3.2), Multi-Message Broker for brownfield integration (Section 3.3), management frameworks (Section 3.4), service-oriented architectures (Section 3.5), monitoring approaches (Section 3.6), and theoretical foundations like ISA-95 and CMFM (Section 3.7).

### 3.1 Asset Administration Shell (AAS) - aas-core-works

The aas-core-works framework forms the conceptual starting point for metamodel-based code generation in VIA. It implements the IEC 63278 standard as M3/M2/M1 Metamodel Architecture for digital twins and demonstrates how production-ready code for six target languages can be generated from an abstract metamodel (aas-core-meta in simplified Python). The architecture follows the Single-Source-of-Truth principle: The M3 metamodel is canonically defined once, the aas-core-codegen compiler automatically transforms it into language-specific SDKs with identical semantics.

### 3.2 OPC UA (IEC 62541) & open62541 C99 Stack

OPC UA (Open Platform Communications Unified Architecture) according to IEC 62541 forms the communication backbone for VIA. As an established standard in industrial automation, OPC UA offers M3/M2/M1-based information modeling structurally compatible with the VIA architecture. The open62541 implementation – originally a TU Dresden research project – delivers a production-ready C99 stack with minimal memory footprint (~250KB) suitable for edge devices. Particularly relevant for VIA is the Dynamic Address Space API, which enables creating and deleting OPC UA nodes at runtime – a prerequisite for mapping dynamically registering VIA processes.

### 3.3 Multi-Message Broker (Santiago Soler Perez Olaya et al., IEEE ETFA 2024)

The Multi-Message Broker (MMB) addresses the challenge of brownfield integration: Legacy devices with proprietary, inflexible protocols (Modbus, PROFIBUS, EtherCAT) must be integrated into modern AAS-based Industry 4.0 systems. The MMB acts as gateway between northbound interfaces (I4.0 HTTP API, future Type 3 Proactive AAS) and southbound protocols (Modbus, HTTP, MQTT, future PROFIBUS/EtherCAT/PROFINET). The architecture demonstrates how heterogeneous protocols can be systematically transferred into a unified AAS data model through mapping submodels (AID/AIMC) – an approach VIA uses for automatic generation of protocol adapters.

**VIA Project Integration**: The MMB forms the **M3 model foundation and library** (`playbooks/VIA-M3-Compiler/third_party/mmb/`) for the three VIA sub-protocols under OPC UA. The MMB architecture is implemented at the M3 level as a base library upon which Edge-Group-Protocol, Deploy-Protocol, and Process-Group-Protocol build. These protocols are **virtually and dynamically mapped as MMB between processing groups on OPC UA** – not statically at compile time, but dynamically adaptable at runtime.

The MMB concepts (AID/AIMC Mapping, Consistency Layer, Sync/Async Translation, Many-to-Many Broadcast) are used in two ways:
1. **Network Discovery** (`playbooks/VIA-M2-SDK/network_discovery.md`): Automatic recognition of brownfield devices, AID extraction, AIMC mapping generation as `.via` project file suggestions
2. **Dynamic Protocol Orchestration**: The 3 sub-protocols organize themselves **separately from each other** in the overall network, form **nested and recursive security levels** at each protocol layer, and enable virtual network streams with different QoS guarantees (latency, packet arrival certainty, security levels).

The MMB addresses the problem of brownfield integration, where legacy devices with inflexible protocols must be integrated into modern systems. The MMB functions as a gateway with northbound interfaces (I4.0 HTTP API, future Type 3 Proactive AAS) and southbound protocols (Modbus, HTTP, MQTT, future PROFIBUS/EtherCAT/PROFINET).

The internal architecture comprises three layers: The Consistency Layer guarantees that identical requests return the same information, the Mapping Layer selects the appropriate connector and performs data transformation, and the AAS Storage stores one AAS per legacy asset. The AID/AIMC Submodel concept separates vendor-provided information (AID - Asset Interfaces Description with available endpoints based on W3C WoT TD) from user configuration (AIMC - Asset Interfaces Mapping Configuration with bidirectional mapping between Asset and AAS SubmodelElements).

Sync/Async Translation enables two modes: Either the latest status is buffered, or the request blocks until a response is available. AAS Interaction Types are classified in three stages: Type 1 (Passive: XML/JSON/RDF file exchange), Type 2 (Reactive: HTTP API for request-response), Type 3 (Proactive: autonomous inter-AAS communication, currently in standardization). The MMB forms a gateway between real-time (hard/soft real-time fieldbus systems) and non-real-time (HTTP-based cloud connection). Protocol translation bridges different communication patterns: Controller/Peripheral, Client/Server, and Pub/Sub.

The limitations of the MMB lie in the fact that AIMC does not allow data transformations (only 1:1 mapping), Type 3 Interaction is not yet standardized, and no fully automatic deployment is provided.

### 3.4 CMFM & Management Paradigms

The Comprehensive Management Function Model (CMFM) offers a theoretical framework for Human-Centered Management in heterogeneous industrial networks ("Network of Networks"). Unlike System-Centric approaches (SNMP Value-based, SDN Requirements-based), CMFM focuses on Intent-based Management: Users describe goals and desired outputs, the system automatically derives necessary configurations. VIA adapts the CMFM philosophy for process communication: The M3 metamodel defines a VIA Vocabulary (Elements: Process, Service, Registry; Verbs: register, discover, route; IPC Types: Pipe, Socket, TCP, FileQueue, Thread), from which the M2 compiler automatically generates orchestration logic.

**VIA Project Integration**: The VIA Vocabulary is **yet to be defined** and will be documented in `playbooks/VIA-M3-Compiler/via_vocabulary.md` once extracted from the AAS context. The CMFM structure (Goal, Output, Input, Constraints, Representation) is implemented at the M3 level as AAS-lang constructs: Customer projects (`.via` files) describe their goals intent-based (e.g., "Connect Sensor A with Process B, maximize throughput, minimize latency"), the VIA-M2-Compiler automatically derives IPC mechanism (Pipe/Socket/TCP/FileQueue/Thread) and service positioning (same container/host/remote). The three management levels (Data/Control/Management) are cleanly separated in VIA: IPC (Data Plane), Process-Group-Protocol (Control Plane), Deploy-Protocol (Management Plane). This separation is to be specified in `playbooks/VIA-M3-Compiler/via_protocols/` as M3 models.

The CMFM (Comprehensive Management Function Model) contrasts Human-Centered Management with System-Centric Management and enables various management paradigms: Value-based (SNMP with polling of values), Policy-based (intent-based goal specifications), Requirements-based (SDN/TSN with QoS requirements), and Ontology-based (semantic-based reasoning systems).

The strengths of CMFM lie in heterogeneity management for "Network of Networks", intent-based abstraction instead of low-level configuration, and knowledge transfer through standardized CMF definitions. The CMFM Meta-Model defines five components: Goal (mandatory, describes the objective), Output (mandatory, describes the expected output), Input (optional, describes necessary inputs), Constraints (optional, defines restrictions), and Representation (optional, various representation forms).

Constraints are classified into five types: Time (temporal restrictions), Order (sequence dependencies), Existence (existence conditions), Mutual Exclusiveness (mutual exclusion), and Execution Success (success criteria). The taxonomy enables hierarchical composition, with multiple super-CMFMs possible.

The VIA Vocabulary defines Elements (Process, Service, Registry, Scheduler, Router), Verbs (register, discover, route, schedule), and IPC Types (Pipe, Socket, TCP, FileQueue, Thread) as domain-specific vocabulary. Separation of Data/Control/Management Plane occurs through IPC (Data Plane), Orchestration (Control Plane), and CMFM (Management Plane), representing an improvement over legacy industrial systems.

VIA functions as a "Network of Networks" with holistic management for heterogeneous IPC mechanisms (Pipe, Socket, TCP, FileQueue, Thread) and enables seamless integration with access to different management systems and orchestration throughout. The legacy problem of industrial systems lies in missing separation of Data/Control/Management Planes, proprietary interfaces, and static configuration.

The limitations of CMFM lie in the fact that no compiler chain is provided, CMFM creation is manual, and vocabulary management is yet-to-standardize.

### 3.5 SOA & Microservice Architecture (Santiago Soler Perez Olaya et al., IECON 2024)

Service-oriented architectures (SOA) and microservices form the structural foundation for VIA processes. The research work by Santiago Soler Perez Olaya demonstrates how AAS submodels can be implemented as independent microservices communicating via gRPC+Protobuf. Particularly relevant is the described code generation pipeline: OpenAPI specifications (AAS Spec) are transformed into Protobuf definitions, from which the protoc compiler generates language-specific code. VIA extends this approach with an additional abstraction layer (M3 metamodel) and automatic IPC optimization.

**VIA Project Integration**: VIA uses **Protobuf at the M3 level** as an interpreter for metamodel definitions and customer project data (`playbooks/VIA-M3-Compiler/` uses Protobuf from `third_party/`). The VIA-M3-Compiler generates `.proto` files for microservice communication, which are stored in `playbooks/VIA-M2-SDK/proto/`. Unlike Santiago Soler Perez Olaya's approach (OpenAPI → Protobuf → protoc), VIA follows the path: **M3-Metamodel (in AAS-lang) → VIA-M3-Compiler → Protobuf definitions + C++ SDK**. The "One microservice per Submodel" idea is implemented in VIA: Each AAS Submodel is deployed as an independent VIA process (C++23 Module), with the M2-Compiler automatically generating gRPC service stubs. IPC optimization then selects at compile time: gRPC (Remote), UNIX Socket (local, high-performance), or Thread-Messaging (same process).

Service-oriented architectures (SOA) are based on fundamental principles: Modularity for independent services, Abstraction for encapsulation of implementation details, Loose Coupling for minimal dependencies, Service Composition for flexible combination, and Reusability for reuse across system boundaries.

Automotive SOA uses SOME/IP (Autosar) for in-vehicle communication, DDS (Publish/Subscribe) for real-time data distribution, and OPC UA for interoperability with backend systems. The Microservice Network for AAS implements "One microservice per Submodel", with Northbound HTTP API for clients, Internal gRPC for service-to-service communication, and Southbound Asset Protocol for hardware connection.

The combination of gRPC and Protobuf offers numerous advantages: High-performance with low-latency through HTTP/2 multiplexing, language interoperability for C++, C#, Python, Java, and Go, binary serialization for compact and efficient data transfer, backward/forward compatibility for version-safe evolution, and contract-first paradigm for clear API definition.

The Code Generation Pipeline transforms OpenAPI (AAS Spec) into Protobuf (.proto files), which are translated by the protoc Compiler into language-specific code (messages, service stubs). AAS SDK Integration uses aas-core-csharp for (de-)serialization and metamodel types. Container Deployment occurs via Docker and Kubernetes with transparent relocation, with services positioned near workload or gateway.

The limitations of this approach lie in the fact that Protobuf does not support inheritance (resort to composition), a duality exists between Protobuf-generated and AAS Core SDK classes, heterogeneous protocols are not unified, and manual orchestration is required.

### 3.6 IPC, Monitoring & Service Mesh (Related Work)

The choice of IPC mechanism has fundamental influence on latency and scalability of distributed systems. Existing solutions like gRPC (~0.5ms latency, but no service discovery), UNIX Domain Sockets (~20μs, only local), DDS (Real-Time QoS, ~2ms overhead), and service mesh solutions like Istio/Linkerd (runtime routing, 5-10ms sidecar overhead) require manual configuration and offer no compile-time optimization. For monitoring, established standards exist (SNMP for infrastructure, OPC UA for process data, MQTT for cloud connection), but an integrated view is missing. VIA addresses this fragmentation through compiler-assisted unification: The M2-Compiler automatically selects the optimal IPC mechanism based on process localization (same host → Pipe/Socket, Remote → TCP/gRPC) and latency requirements.

**VIA Project Integration**: The **IPC-Optimizer** in `playbooks/VIA-M2-SDK/ipc_optimizer.md` implements a graph-based algorithm for compile-time selection of the optimal IPC mechanism (**core of this research work**). The decision logic is defined in the M3 metamodel as template rules (`playbooks/VIA-M3-Compiler/templates/ipc_decision_logic.aas`), which the customer instantiates in their M2 project (`.via` files) with concrete constraints (e.g., "max_latency: 5ms", "same_host: true").

**Multi-Objective Optimization (Pareto-Optimization)**: The M2-Compiler executes a constraint solver (Z3) at compile time, which finds **Pareto-optimal solutions** for conflicting goals:
- **Minimize latency** (μs range for Unix Socket, ms range for TCP)
- **Maximize throughput** (Messages/s, MB/s)
- **Minimize resource consumption** (CPU%, RAM MB, network bandwidth)

A solution is **Pareto-optimal** if no objective can be improved without worsening another. The constraint solver calculates the **Pareto-Frontier** (set of all non-dominated solutions) and selects the best trade-off solution based on customer constraints. The 5 IPC mechanisms (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) are defined as AAS-lang Enumerations in the M3.

**In-the-Loop Self-Optimization**: VIA implements **autonomous cluster optimization** through continuous telemetry evaluation:
- **Telemetry Metrics**: CPU load (%), RAM usage (MB), Disk I/O (MB/s), Network latency (ms), Message throughput (Messages/s)
- **Evaluation Loop**: Deploy-Protocol collects telemetry from all services → M2-Compiler analyzes bottlenecks → Kubernetes load distribution is dynamically adjusted
- **Scope**: Processing services for measurement data (Edge-Devices → Aggregation → Analytics) + OPC UA protocol level (Sub-protocols are virtually remapped between processing groups via MMB)
- **Feedback-Loop**: New service positioning is tested as canary deployment, permanently adopted upon improvement of Pareto metrics, rollback in fractions of seconds upon deterioration

Monitoring integration occurs via the Deploy-Protocol (Logging, Telemetry) and OPC UA (process data exposition).

The overview of existing approaches shows various strengths and weaknesses: gRPC uses HTTP/2 and Protobuf with circa 0.5ms latency in single-host operation, but offers no integrated service discovery. ZeroMQ implements message queues with five patterns (REQ/REP, PUB/SUB), but has no compiler integration. DDS (OMG Data Distribution Service) is optimized for real-time with QoS policies, but causes circa 2ms overhead and offers no metamodel abstraction.

Service Mesh solutions like Istio and Linkerd enable runtime routing with dynamic discovery, but cause 5-10ms sidecar overhead per request. UNIX Domain Sockets offer circa 20μs latency for local processes, but support no distributed orchestration across host boundaries.

SNMP (Simple Network Management Protocol) implements a Manager-Agent model with Polling (GET requests every 60 seconds) and Traps (Push upon events), uses a hierarchical MIB-OID structure, and defines standard MIBs like IF-MIB, HOST-RESOURCES-MIB, and ENTITY-SENSOR-MIB. The limitations of SNMP lie in the flat OID list without object hierarchies, the polling paradigm without Pub/Sub support, the primary focus on monitoring rather than control, and the scaling limit at thousands of devices.

MQTT (Message Queuing Telemetry Transport) is Pub/Sub-based and broker-centric, optimized for IoT sensors and cloud connection, and extremely lean for bandwidth-critical applications. A recommended hybrid approach combines SNMP for infrastructure monitoring, OPC UA for detailed process data, and MQTT for cloud analytics.

The fundamental limitation of all mentioned approaches is that they require manual configuration, offer no compile-time optimization, and cannot manage heterogeneous protocols in a unified manner.

### 3.7 Research Gaps

The analysis of the state of research reveals several fundamental gaps that this work addresses. There exists no multi-stage compiler chain M3→M2→M1 specifically for process communication that automatically translates metamodel definitions into optimized IPC implementations. Automatic IPC mechanism selection at compilation is not provided in existing frameworks; instead, the choice occurs at runtime or through manual configuration.

Under OPC UA, no standardized sub-protocols for process grouping, deployment management, and IPC optimization are defined, although this functionality is urgently needed in industrial systems. Compile-time optimization of microservice positioning based on process dependencies and latency requirements is an unexplored area.

The trade-off between Service Mesh overhead (5-10ms sidecar latency) and potential compiler optimization has not been systematically investigated scientifically. In-the-Loop self-optimization with Pareto metrics (latency, throughput, resource consumption) as an autonomous feedback loop exists in no known industrial framework. Finally, the concept of M3-library composition for protocol extensibility, where new protocols can build on existing M3 libraries, is missing.

### 3.8 Scientific Value of This Work

This research work makes several fundamental contributions that go beyond incremental improvements of existing systems:

#### 3.8.1 Theoretical Foundation through M3-Library-Architecture

**MMB as M3-Library**: The embedding of the Multi-Message Broker (MMB) as a reusable M3 library demonstrates how research results from brownfield integration (Santiago Soler Perez Olaya et al.) can be operationalized as formal metamodel components. The three VIA sub-protocols (Edge-Group, Deploy, Process-Group) are **themselves defined as M3 libraries in AAS-lang** – analogous to Protobuf as M3 interpreter – and load models from MMB. This model composition at the M3 level creates a **scientific foundation for extensible protocol architectures** in industrial automation.

**Reusability and Extensibility**: Through the separation of base library (MMB) and specialized protocols (Edge-Group/Deploy/Process-Group), a modular architecture emerges that enables future extensions. Other research projects can import MMB models and define their own protocol semantics – a paradigm missing in previous OPC UA Companion Specifications.

#### 3.8.2 Mathematical Rigor through Pareto-Optimization

**Multi-Objective Optimization**: The application of Pareto optimization to IPC mechanism selection transforms a previously heuristic decision into a **formally solvable optimization problem**. The conflicting goals (minimize latency, maximize throughput, minimize resource consumption) are not solved through ad-hoc weighting, but through calculation of the **Pareto-Frontier** – the set of all non-dominated solutions. This enables **scientifically traceable justification** for each IPC decision and creates comparability between systems.

**Z3 Constraint-Solver**: The integration of a formal constraint solver at compile time elevates the work beyond empirical benchmarks. The solutions are not just "well measured" but **provably optimal** within the defined constraints.

#### 3.8.3 Autonomous Systems through In-the-Loop Self-Optimization

**Feedback-Loop Architecture**: Continuous telemetry evaluation (CPU%, RAM, Disk I/O, network latency, message throughput) with automatic Kubernetes load distribution realizes **autonomous cluster optimization** – a core vision of Industry 5.0. The evaluation loop (Deploy-Protocol collects → M2-Compiler analyzes → adjust load distribution → Canary test → Adoption/Rollback) demonstrates **self-adaptive systems** without human intervention.

**Scientific Contribution**: This work shows for the first time how compile-time optimization (Pareto-Frontier) and runtime adaptation (telemetry feedback) can be **complementarily combined**. Existing approaches are either purely static (manual configuration) or purely dynamic (Service Mesh) – VIA unifies both paradigms.

#### 3.8.4 Nested Security Architectures

**Recursive Security Levels**: The ability of each protocol layer to form **separately from each other** hierarchical security rules (e.g., Device-Groups → Edge-Groups → Cluster-Groups → Global) addresses enterprise requirements in heterogeneous networks. This architecture is scientifically relevant as it realizes **Separation of Concerns** at the protocol level – a previously unsolved problem in OPC UA Companion Specifications.

**Dynamic MMB-Mapping**: The ability to **virtually remap sub-protocols between processing groups** (e.g., at bottleneck: instantiate new services, redirect data streams) demonstrates **runtime adaptivity** despite compile-time optimization – a fundamental contradiction that VIA resolves through the separation of protocol definition (M3, static) and protocol instantiation (MMB, dynamic).

#### 3.8.5 Bridge between Compiler Design and Industrial Automation

**Interdisciplinary Innovation**: The application of compiler optimization techniques (M3/M2/M1 metamodel chain, constraint solving, code generation) to industrial process communication (OPC UA, IPC, service orchestration) creates a **new research direction** at the interface of computer science and automation engineering. The work shows that Industry 4.0 problems are solvable from a compiler perspective – a perspective missing in previous AAS implementations (Python scripts, manual orchestration).

---

## 4. Objectives and Research Methodology

### 4.1 Main Objective

The overarching goal of this research is the development and evaluation of a fully automatic compiler system for Industry 4.0 systems with focus on the **Process-Group-Protocol subsystem**. Unlike existing approaches that choose IPC mechanisms manually or at runtime, VIA should make this decision at compile time while optimizing latency, throughput, and resource consumption.

### 4.2 Sub-Objectives

The research is divided into five sub-objectives, with this work primarily focusing on T2 (IPC optimization) and T4 (Process-Group-Protocol):

- **T1 (Context)**: VIA-M3-Compiler – Transformation AAS M3 Metamodel → C++ SDK
- **T2 (Research Focus)**: VIA-M2-SDK-Compiler – Automatic IPC mechanism selection based on process dependencies
- **T3 (Context)**: VIA-M1-System-Deployer – Distributed Compilation, Horse-Rider-Deployment, Kubernetes orchestration
- **T4 (Research Focus)**: Sub-Protocol Design – Specification and implementation of Process-Group-Protocol under OPC UA
- **T5 (Outlook)**: AI Integration Industry 5.0 – Natural language system description → Automatic Compilation

### 4.3 Research Methodology

The research methodology follows an engineering science approach with four main phases: Requirements Engineering, Design, prototypical implementation, and experimental evaluation.

---

## 5. Expected Results

### 5.1 Scientific Contributions (Focus Process Communication)

The scientific contributions include five core elements:

- **B1**: Metamodel extension for process communication in AAS M3
- **B2**: Compiler optimization algorithm for IPC mechanism selection
- **B3**: Process-Group-Protocol specification as OPC UA sub-protocol
- **B4**: Benchmark comparison between compiler optimization, service mesh, and manual configuration
- **B5**: Scalability proof for more than 100,000 services with hierarchical grouping

### 5.2 Practical Results

- **E1**: M2 SDK Compiler prototype with IPC optimizer
- **E2**: Benchmark suite for IPC performance
- **E3**: Use case for SCADA, MES, and PLC edge integration
- **E4**: Standardization proposal for VIA Process-Group-Protocol for submission to OPC Foundation

---

## 6. Timeline

The timeline is divided into six phases with total duration of 24 weeks (approx. 6 months):

- **Phase 1**: Research & Analysis (4 weeks) ✅ COMPLETED
- **Phase 2**: Playbook & M3 Metamodel Design (2 weeks) ⏳ IN PROGRESS
- **Phase 3**: M2 SDK Compiler Prototype with IPC Optimizer (6 weeks)
- **Phase 4**: Benchmark Suite & Use Case (4 weeks)
- **Phase 5**: Evaluation & Comparative Measurements (4 weeks)
- **Phase 6**: Documentation & Publication (4 weeks)

---

## References

### Standards
1. IEC 63278 (2024). Asset Administration Shell
2. IEC 62541 (2020). OPC Unified Architecture
3. ISO/IEC 20922 (2016). MQTT Protocol
4. ISA-95 (2010). Enterprise-Control System Integration

### Research Papers (Santiago Soler Perez Olaya)
5. Soler Perez Olaya, S. et al. (2024). Dynamic Multi-Message Broker for I4.0 AAS
6. Soler Perez Olaya, S. et al. (2024). SOA for Digital Twins with gRPC and Protobuf
7. Soler Perez Olaya, S. & Wollschlaeger, M. (2022). CMFM Generality Hierarchy
8. Soler Perez Olaya, S. et al. (2019). CMFM for Heterogeneous Industrial Networks

### Open Source Projects
10. aas-core-works (2024). https://github.com/aas-core-works
11. open62541 (2024). https://github.com/open62541/open62541
12. OPC Foundation (2024). https://github.com/OPCFoundation/UA-Nodeset

---

**Status**: ✅ Structured with key points from README.md & TODO.md
**Basis**: Phase 1 + Phase 2 Research Findings
**Next Steps**: Literature research sources 13-27, Detailed implementation, Transform to .docx
