# VIA — Virtual Industry Automation

**Multi-Stage Compiler System for Metamodel-Based Industrial Microservice Architecture**

VIA is a M3→M2→M1 compiler chain that generates optimized microservice deployments for heterogeneous industrial systems using Asset Administration Shell (AAS) and OPC UA standards from Industrie 4.0 and the third digital industry phase, where AI models automate human will into results and self defining and constructing systems.

> **Research Project**: TU Dresden, Chair of Industrial Communications
> **Supervisors**: Prof. Dr.-Ing. Martin Wollschlaeger, Dr.-Ing. Hilbert, Santiago Soler Perez Olaya

---

## 🎯 Project Status

| Phase | Status | Description |
|-------|--------|-------------|
| **Phase 1** | ✅ **Complete** | Research analysis (11 university papers) |
| **Phase 2** | ✅ **Complete** | GitHub repository analysis (AAS, OPC UA) |
| **Phase 3** | 🔄 **In Progress** | Implementation playbooks |
| **Phase 4** | ⏳ **Pending** | Research exposé & proposal |

**📖 Research Documentation**: [playbooks/](playbooks/)
**🔬 Research Exposé**: [playbooks/Analyse_eines_Forschungsthemas_Expose.md](playbooks/Analyse_eines_Forschungsthemas_Expose.md)
**📋 Detailed Playbook**: [playbooks/README.md](playbooks/README.md)

---

## Research Focus

**Research Question**:
> Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?

**Key Innovations**:
- ✅ **M3→M2→M1 Compiler Chain**: Automated code generation from metamodel to deployment
- ✅ **Process-Group-Protocol**: Compile-time IPC optimization (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging)
- ✅ **Horse-Rider Deployment**: C++23 Modules with hot-reload for edge devices
- ✅ **Dynamic OPC UA Address Space**: VIA Registry ↔ OPC UA nodes (open62541 C99 stack)
- ✅ **AAS Integration**: Asset Administration Shell submodel exposure
- ✅ **Multi-Architecture Support**: Cross-compilation (MIPS, RISC-V, POWER9, x86, ARM, Sparc)

**Target Performance**:
- H1: 30% latency reduction vs. runtime service mesh
- H2: 90% efficiency of dynamic orchestration
- H3: Linear scaling to 100K services
- H4: 60% development time reduction

---

## Core Components

### VIA-M3-Compiler
Metamodel-to-Code Generator (M3 → M2 SDK + OPC UA NodeSet XML)

### VIA-M2-SDK
C++ SDK for microservice development with IPC abstraction

### VIA-M1-System-Deploy
Kubernetes + Edge deployment system with Horse-Rider architecture

### Sub-Protocols under OPC UA
- **Edge-Group-Protocol**: Virtual network groups
- **Deploy-Protocol**: Version control, logging, rejuvenation
- **Process-Group-Protocol**: IPC optimization (Research Focus)

---

## Documentation

### 🔬 Research Documentation

**Phase 1: University Papers (11 Documents)**
- [Phase 1 Summary](playbooks/phase1_research/PHASE1_SUMMARY.md)
- CMFM (Comprehensive Management Function Model)
- Multi-Message Broker (MMB)
- SOA for Digital Twins
- SNMP + OPC UA + MQTT Monitoring
- SCADA/MES Integration

**Phase 2: GitHub Repository Analysis (3 Repositories)**
- [Phase 2 Summary](playbooks/phase2_research/PHASE2_SUMMARY.md)
- [AAS Research](playbooks/phase2_research/Research_AAS_MERGED.md) - aas-core-works code generator
- [open62541 Research](playbooks/phase2_research/Research_open62541.md) - C99 OPC UA stack
- [UA-Nodeset Research](playbooks/phase2_research/Research_UA_Nodeset.md) - 76+ Companion Specifications

**Research Exposé**:
- [Forschungsthema Exposé](playbooks/Analyse_eines_Forschungsthemas_Expose.md) - Complete research proposal

**Implementation Playbooks** (Phase 3):
- [Main Playbook](playbooks/README.md) - VIA system overview
- [TODO & Progress](playbooks/TODO.md) - Development tracking

### 🛠️ Technical Documentation

**Architecture**:
- [docs/ARCHITECTURE.md](docs/english/ARCHITECTURE.md) - System architecture
- [playbooks/README.md](playbooks/README.md) - Detailed implementation plan

**Development**:
- [Contributing Guide](docs/english/CONTRIBUTING.md)
- [Implementation Verification](docs/IMPLEMENTATION_VERIFICATION.md)

---

## Current Status

⚠️ **Pre-Alpha Research Phase** - Implementation in progress

**Completed**:
- ✅ Research Phase 1 & 2 (14 documents analyzed)
- ✅ Research Exposé (31KB, comprehensive)
- ✅ Architecture Design (M3/M2/M1 compiler chain)

**In Progress**:
- 🔄 Implementation Playbooks (Phase 3)
- 🔄 VIA-M3-Compiler prototype
- 🔄 VIA-M2-SDK C++ library

**Planned**:
- ⏳ VIA-M1-System-Deploy (Kubernetes integration)
- ⏳ Test system & benchmarks
- ⏳ Research paper submission

---

## Project Structure

```
VIA/
├── playbooks/                      # Research & Implementation Playbooks
│   ├── Analyse_eines_Forschungsthemas_Expose.md  # Research Exposé (31KB)
│   ├── README.md                   # Main system playbook
│   ├── TODO.md                     # Development tracking
│   ├── phase1_research/            # ✅ University papers (11 docs)
│   │   ├── PHASE1_SUMMARY.md
│   │   ├── research_*.md           # Analysis documents
│   │   └── doc_*.md                # Extracted papers
│   ├── phase2_research/            # ✅ GitHub analysis (3 repos)
│   │   ├── PHASE2_SUMMARY.md
│   │   ├── Research_AAS_MERGED.md  # aas-core-works
│   │   ├── Research_open62541.md   # C99 OPC UA stack
│   │   └── Research_UA_Nodeset.md  # OPC UA NodeSets
│   ├── VIA-M3-Compiler/            # 🔄 M3 Metamodel Compiler
│   │   ├── implementation/
│   │   └── tests/
│   ├── VIA-M2-SDK/                 # 🔄 M2 SDK (C++ Library)
│   │   ├── implementation/
│   │   └── tests/
│   └── VIA-M1-System-Deploy/       # ⏳ M1 Deployment System
│       ├── implementation/
│       └── tests/
├── docs/                           # Legacy documentation
│   ├── english/
│   └── german/
├── include/                        # C++ headers (future)
├── src/                            # C++ source (future)
├── tests/                          # Unit tests (future)
├── third_party/                    # Third-party dependencies
├── CMakeLists.txt
└── README.md                       # This file
```

---

## Technology Stack

**Core Technologies**:
- **C++23**: Modern C++ with Modules support
- **Protobuf**: M3 metamodel definition & serialization
- **gRPC**: High-performance RPC framework
- **open62541**: C99 OPC UA stack (250KB footprint)
- **CMake**: Cross-platform build system

**Standards Integration**:
- **IEC 63278**: Asset Administration Shell (AAS)
- **IEC 62541**: OPC UA (OPC Unified Architecture)
- **ISA-95**: SCADA/MES integration

**Deployment Targets**:
- **Architectures**: MIPS, RISC-V, POWER9, x86, ARM, Sparc
- **OS**: Linux, Windows, macOS
- **Orchestration**: Kubernetes + Edge Modules

---

## License

This project is subject to a proprietary End User License Agreement (EULA).

**Important:** This software is provided for internal use only. Redistribution, reverse engineering, or commercial use without explicit permission is prohibited.

For licensing inquiries: bep.venture.ug@gmail.com

---

## Academic Collaboration

**TU Dresden Partnership**:
- Chair of Industrial Communications
- Prof. Dr.-Ing. Martin Wollschlaeger
- Dr.-Ing. Hilbert
- Santiago Soler Perez Olaya

**Research Integration**:
- CMFM (Comprehensive Management Function Model)
- Multi-Message Broker (MMB)
- open62541 (TU Dresden origin)

---

## Support & Contact

- **Email**: bep.venture.ug@gmail.com
- **Address**: BEP Venture UG, Chemnitzer Straße 69, 01187 Dresden, Germany
- **Issues**: [GitHub Issues](https://github.com/BenniProbst/VIA/issues)
- **Research Docs**: [playbooks/](playbooks/)

---

## Version

**Current Version**: 0.1.0-alpha (Research Phase)
**Last Updated**: 22.10.2025

---

**Copyright © 2025 BEP Venture UG (haftungsbeschränkt)**
**Research Collaboration with TU Dresden**
