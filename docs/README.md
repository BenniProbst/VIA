# VIA - Virtual Industry Automation

**Documentation Overview**

This directory contains comprehensive project documentation in both German and English.

## Quick Links

- **German Documentation**: [german/](german/)
- **English Documentation**: [english/](english/)
- **Project Description & Research**:
  - German: [german/PROJECT_DESCRIPTION_AND_RESEARCH.md](german/PROJECT_DESCRIPTION_AND_RESEARCH.md)
  - English: [english/PROJECT_DESCRIPTION_AND_RESEARCH.md](english/PROJECT_DESCRIPTION_AND_RESEARCH.md)

## What is VIA?

VIA (Virtual Industry Automation) is a research project developing a **self-compiling bootstrap compiler system** for Industry 4.0 automation. It transforms metamodel definitions through a multi-stage compiler chain (M3→M2→M1) into deployed industrial systems for 50,000+ edge devices.

### Core Innovation

- **M3-Compiler**: Metamodel → SDK (transforms AAS IEC 63278 into C++ SDK)
- **M2-SDK-Compiler**: SDK → Customer System (with automatic IPC optimization)
- **M1-System-Deployer**: System → Production (Horse-Rider deployment, Kubernetes orchestration)

### Research Focus

This research investigates **compile-time optimization of Inter-Process Communication (IPC)** in microservice architectures:

> Can process chains of microservices be automatically created via metamodels, with their positioning and communication mechanism (Pipe/Socket/TCP/FileQueue/Thread) optimized during compilation?

## Documentation Structure

### German Documentation (german/)
- **ARCHITECTURE.md**: System architecture and component design
- **BENUTZERHANDBUCH.md**: User manual (German)
- **CODE_OF_CONDUCT.md**: Community guidelines
- **CONTRIBUTING.md**: Contribution guide
- **SECURITY.md**: Security policy
- **CHANGELOG.md**: Version history

### English Documentation (english/)
- **ARCHITECTURE.md**: System architecture and component design
- **USER_MANUAL.md**: User manual (English)
- **CODE_OF_CONDUCT.md**: Community guidelines
- **CONTRIBUTING.md**: Contribution guide
- **SECURITY.md**: Security policy
- **CHANGELOG.md**: Version history

## For Researchers

The project addresses several research gaps:
1. **Metamodel-based IPC Optimization**: First systematic approach to compile-time IPC selection
2. **OPC UA Sub-Protocols**: Edge-Group, Deploy, and Process-Group protocols
3. **Multi-Level Debugging**: Trace errors from deployed binary through M1/M2/M3 back to model definition
4. **In-the-Loop Self-Optimization**: Autonomous cluster optimization via telemetry feedback

## Project Structure

```
VIA/
├── docs/                  # This documentation
│   ├── german/           # German documentation
│   ├── english/          # English documentation
│   └── architecture/     # Architecture diagrams
├── playbooks/            # Development playbooks & research notes
│   ├── phase1_research/ # AAS, OPC UA, CMFM research
│   ├── phase2_research/ # GitHub repository analysis
│   ├── VIA-M3-Compiler/ # M3 compiler implementation playbooks
│   ├── VIA-M2-SDK/      # M2 SDK compiler playbooks
│   └── VIA-M1-System-Deploy/ # Deployment playbooks
├── src/                  # Source code
└── tests/                # Test suites
```

## Getting Started

1. **Understand the Vision**: Read [PROJECT_DESCRIPTION_AND_RESEARCH.md](english/PROJECT_DESCRIPTION_AND_RESEARCH.md)
2. **Explore Architecture**: Check [ARCHITECTURE.md](english/ARCHITECTURE.md)
3. **Read Playbooks**: See detailed development plans in `playbooks/`

## Key Technologies

- **Standards**: IEC 63278 (AAS), IEC 62541 (OPC UA)
- **Languages**: C++20/23, AAS-lang (custom DSL), Protobuf
- **Protocols**: OPC UA, gRPC, IPC mechanisms
- **Deployment**: Kubernetes, C++23 Modules (Horse-Rider pattern)
- **Optimization**: Z3 Constraint Solver, Pareto optimization

## Supervisors

- **Prof. Dr.-Ing. habil. Martin Wollschlaeger** (TU Dresden)
- **Dr.-Ing. Frank Hilbert** (TU Dresden)
- **Santiago Soler Perez Olaya** (TU Dresden)

## Author

**Benjamin-Elias Probst**
Technische Universität Dresden, Faculty of Computer Science

---

For detailed project history and development status, see `playbooks/TODO.md`.
