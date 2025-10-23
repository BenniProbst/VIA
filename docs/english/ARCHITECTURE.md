# VIA - Architecture Documentation

## Overview

VIA (Virtual Industry Automation) is a multi-stage compiler system for Industry 4.0 automation that transforms metamodel definitions through a compiler chain (M3’M2’M1) into deployed industrial systems for 50,000+ edge devices.

## Core Architecture

### Multi-Stage Compiler Chain

```
M3 Metamodel (AAS IEC 63278, OPC UA IEC 62541)
    “ VIA-M3-Compiler
M2 SDK (C++ SDK with generated types & services)
    “ VIA-M2-SDK-Compiler (IPC Optimizer)
M1 System Project (Customer project as C++ overall project)
    “ VIA-M1-System-Deployer
M0 Deployed System (Binaries on >50,000 Edge Devices)
```

### Components

#### 1. VIA-M3-Compiler (Metamodel ’ SDK)
- **Input**: AAS IEC 63278 text specification (transformed via SITL), OPC UA IEC 62541 as M3 library, VIA extensions
- **Processing**: C++20/23 metaprogramming, custom template engine in AAS-lang, Protobuf as M3 interpreter
- **Output**: C++ SDK (`playbooks/VIA-M2-SDK/`), OPC UA NodeSet XML, Protobuf `.proto` files

#### 2. VIA-M2-SDK-Compiler (SDK ’ Customer System)
- **Input**: Customer project `.via` files, Optional: Network topology via Network Discovery
- **Processing**:
  - **Network Discovery**: SNMP/OPC UA/Modbus scanner
  - **IPC Optimizer** (research focus): Graph-based compile-time optimization
  - **Test Generator**: Automatic test generation from M3 constraints
- **Output**: C++ overall project (`playbooks/VIA-M1-System/`), Kubernetes manifests, edge modules

#### 3. VIA-M1-System-Deployer (System ’ Production)
- **Input**: M1 system project, deployment targets (MIPS, RISC-V, ARM, x86, etc.)
- **Processing**:
  - **Cross-Compilation**: Multi-architecture toolchain management
  - **Horse-Rider-Deployment**: C++23 modules, hot-reload, canary deployment
  - **Distributed Build**: Parallel builds via GitHub runners
- **Output**: Deployed system for >50,000 edge devices, binaries, digital twin

## Sub-Protocols under OPC UA

VIA defines three custom OPC UA sub-protocols:

### 1. Edge-Group-Protocol (External Layer)
- **Function**: Virtual network groups for hierarchical edge device grouping
- **Performance**: Hardcoded messages, no virtual router ’ time-criticality preserved
- **Security**: Nested security levels (Device-Groups ’ Edge-Groups ’ Cluster-Groups ’ Global)

### 2. Deploy-Protocol (Management Layer)
- **Function**: Versioning, system updates, rejuvenation
- **Separation**: Metadata separated from plant data
- **Telemetry**: CPU load, RAM usage, disk I/O
- **In-the-Loop Self-Optimization**: Continuous feedback loop

### 3. Process-Group-Protocol (Data Layer) ’ **Research Core**
- **Function**: Transparent IPC optimization between services
- **IPC Mechanisms**: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging
- **Optimization**: Pareto optimization (latency, throughput, resource consumption) via Z3 constraint solver
- **Compile-Time Decision**: Static ranking with optional runtime adaptation

## Project Progress and Development Plan

See `playbooks/TODO.md` for detailed tasks and progress.

### Phase 1: Research & Analysis  COMPLETED
- All university documents fully read
- AAS, OPC UA, CMFM, SOA analyzed
- Santiago papers (MMB, CMFM, SOA) fully processed

### Phase 2: GitHub Repository Analysis  COMPLETED
- aas-core-works (M3 Metamodel, Code Generator)
- open62541 (C99 OPC UA Stack)
- UA-Nodeset (76+ Companion Specifications)

### Phase 3: Implementation Playbooks ó NEXT PHASE
1. `Main_System_playbook_DAY01.md` (orchestrates M3’M2’M1)
2. `VIA-M3-Compiler/implementation/M3_compiler_playbook.md`
3. `VIA-M3-Compiler/tests/M3_tests_playbook.md`
4. `VIA-M2-SDK/implementation/M2_sdk_playbook.md`
5. `VIA-M2-SDK/tests/M2_tests_playbook.md`
6. `VIA-M1-System-Deploy/implementation/M1_deploy_playbook.md`
7. `VIA-M1-System-Deploy/tests/M1_tests_playbook.md`

### Phase 4: Exposé & Research Proposal =Ë PLANNED
- Exposé based on CELM template
- Research proposal 1-page summary

## Research Focus

### Central Research Question
> Can process chains of microservices be automatically created via metamodels (M3/M2), with their positioning in the system and communication mechanism (IPC) optimized during compilation?

### Hypotheses
- **H1**: Compiler-based IPC optimization reduces latency by >30% compared to runtime service mesh
- **H2**: Static positioning achieves 90% of the efficiency of dynamic orchestration
- **H3**: Process-Group-Protocol scales linearly to 100,000 services
- **H4**: Metamodel-based abstraction reduces manual development time by 60%

## Technology Stack

- **Languages**: C++20/23, AAS-lang (custom DSL), Protobuf
- **Protocols**: OPC UA (IEC 62541), gRPC, IPC mechanisms
- **Deployment**: Kubernetes, C++23 modules (Horse-Rider pattern)
- **Optimization**: Z3 Constraint Solver, Pareto optimization
- **Architectures**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc
- **Operating Systems**: Linux, Windows, macOS

## Multi-Level Debugging

VIA implements continuous error traceability across all compiler stages:

```
M0 Binary (deployed) ’ Error
    “ Trace
M1 System Project (C++ code) ’ Error source
    “ Trace
M2 SDK (generated code) ’ Generation rule
    “ Trace
M3 Metamodel (AAS-lang definition) ’ Original specification
```

Analogy: Just as gdb can debug across g++ compiler layers (Frontend ’ Middle-End ’ Backend ’ Assembly ’ Binary), VIA debugger can trace back across multiple metamodel levels.

## Scalability

**Target System**: >50,000 edge devices

**Performance Optimizations**:
- Hardcoded messages (more efficient than dynamic routing)
- Compile-time decisions (static IPC ranking)
- Binary ABI stability (C++23 modules)
- Distributed compilation (parallel builds)
- No virtual routers for time-critical operations

## Security

**Nested Security Architecture**:
- Each protocol layer (Edge-Group, Deploy, Process-Group) has its own security levels
- Recursive grouping enables hierarchical policies
- Hardcoded messages prevent runtime code changes
- Source code cannot be modified at runtime (focus on deployment server security)

## Vision: Industry 5.0

**Future AI Integration**:
1. Customer describes system via speech/text
2. AI model translates to M3 compiler requirements
3. Compiler chain (M3 ’ M2 ’ M1) generates system
4. Software-in-the-Loop: Iterative error correction
5. Fully automatic deployment

**Milestones**:
- **M3 defining itself**: VIA closes the loop through automatic M3 definition via M3
- **Self-defining systems**: Autonomous system generation and construction

## References

See `docs/english/PROJECT_DESCRIPTION_AND_RESEARCH.md` for complete bibliography.

### Core Sources
- IEC 63278 (2024): Asset Administration Shell
- IEC 62541 (2020): OPC Unified Architecture
- Soler Perez Olaya, S. et al. (2024): Dynamic Multi-Message Broker, SOA for Digital Twins
- Soler Perez Olaya, S. & Wollschlaeger, M. (2022): CMFM Generality Hierarchy
- aas-core-works: https://github.com/aas-core-works
- open62541: https://github.com/open62541/open62541

---

**Last Updated**: October 2025
**Status**: Phase 2 completed, Phase 3 in preparation
