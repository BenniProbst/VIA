# Research Exposé: Analysis of a Research Topic - Process Communication

**Title**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Author**: Benjamin-Elias Probst
**Supervisors**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Faculty of Computer Science
**Date**: October 2025

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

---

## 3. State of Research

The research builds on several established standards and research results, systematically presented below. The analysis covers AAS code generation (Section 3.1), OPC UA as communication protocol (Section 3.2), Multi-Message Broker for brownfield integration (Section 3.3), management frameworks (Section 3.4), service-oriented architectures (Section 3.5), monitoring approaches (Section 3.6), and theoretical foundations like ISA-95 and CMFM (Section 3.7).

### 3.1 Asset Administration Shell (AAS) - aas-core-works

The aas-core-works framework forms the conceptual starting point for metamodel-based code generation in VIA. It implements the IEC 63278 standard as M3/M2/M1 Metamodel Architecture for digital twins and demonstrates how production-ready code for six target languages can be generated from an abstract metamodel (aas-core-meta in simplified Python). The architecture follows the Single-Source-of-Truth principle: The M3 metamodel is canonically defined once, the aas-core-codegen compiler automatically transforms it into language-specific SDKs with identical semantics.

### 3.2 OPC UA (IEC 62541) & open62541 C99 Stack

OPC UA (Open Platform Communications Unified Architecture) according to IEC 62541 forms the communication backbone for VIA. As an established standard in industrial automation, OPC UA offers M3/M2/M1-based information modeling structurally compatible with the VIA architecture. The open62541 implementation – originally a TU Dresden research project – delivers a production-ready C99 stack with minimal memory footprint (~250KB) suitable for edge devices. Particularly relevant for VIA is the Dynamic Address Space API, which enables creating and deleting OPC UA nodes at runtime – a prerequisite for mapping dynamically registering VIA processes.

### 3.3 Multi-Message Broker (Santiago Soler Perez Olaya et al., IEEE ETFA 2024)

The Multi-Message Broker (MMB) addresses the challenge of brownfield integration: Legacy devices with proprietary, inflexible protocols (Modbus, PROFIBUS, EtherCAT) must be integrated into modern AAS-based Industry 4.0 systems. The MMB acts as gateway between northbound interfaces (I4.0 HTTP API, future Type 3 Proactive AAS) and southbound protocols (Modbus, HTTP, MQTT, future PROFIBUS/EtherCAT/PROFINET). The architecture demonstrates how heterogeneous protocols can be systematically transferred into a unified AAS data model through mapping submodels (AID/AIMC) – an approach VIA uses for automatic generation of protocol adapters.

### 3.4 CMFM & Management Paradigms

The Comprehensive Management Function Model (CMFM) offers a theoretical framework for Human-Centered Management in heterogeneous industrial networks ("Network of Networks"). Unlike System-Centric approaches (SNMP Value-based, SDN Requirements-based), CMFM focuses on Intent-based Management: Users describe goals and desired outputs, the system automatically derives necessary configurations. VIA adapts the CMFM philosophy for process communication: The M3 metamodel defines a VIA Vocabulary (Elements: Process, Service, Registry; Verbs: register, discover, route; IPC Types: Pipe, Socket, TCP, FileQueue, Thread), from which the M2 compiler automatically generates orchestration logic.

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
