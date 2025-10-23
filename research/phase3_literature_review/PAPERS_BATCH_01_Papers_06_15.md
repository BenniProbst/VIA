# Paper Batch 01: Papers 6-15

**Titel**: Micro-ROS, OPC UA, DDS, AAS Standards, Pareto-Optimization, Z3, LLVM
**Zeitraum**: 2002-2024
**Hauptthemen**:
- Embedded Systems (micro-ROS)
- Industrial Standards (IEC 63278 AAS, IEC 62541 OPC UA)
- Middleware (DDS, ROS2 Composition)
- Multi-Objective Optimization (NSGA-II, MOEA/D)
- Constraint Solving (Z3 SMT Solver)
- Compiler Architecture (LLVM)

**Status**: 10/10 Papers vollständig analysiert ✅
**Kritische Papers (⭐⭐⭐⭐⭐)**: 6 Papers (IEC 63278, IEC 62541, NSGA-II, Z3, LLVM, ROS2 Composition)

---

## Papers 6-15: Micro-ROS, OPC UA, DDS, AAS, Pareto-Optimization, Z3, LLVM

### Paper 6: micro-ROS Documentation (2024)
**Typ**: Offizielle Projekt-Dokumentation
**URL**: https://micro.ros.org/
**Schlüsselkonzepte**:
- Client-Agent-Architektur für Mikrocontroller (STM32, ESP32, Renesas RA)
- Micro XRCE-DDS (optimiert für low memory usage)
- rclc Executor mit bounded end-to-end latencies (Real-Time)
- Memory Footprint: "Extremely resource-constrained devices" (<1MB RAM)

**Zitations-Kontext**:
Abschnitt 3.0.4, Zeile 260-278 (VIA Hybrid Deployment):
> "**Edge-Devices mit begrenzten Ressourcen**: <1GB RAM, keine Container-Runtime. Micro-ROS demonstriert, dass Embedded-Systeme mit <1MB RAM (micro-ROS auf STM32, ESP32) Middleware-Abstraktion realisieren können. VIA folgt ähnlichem Prinzip mit ~250KB Footprint (open62541 C99 Stack), erweitert jedoch um native Cross-Compilation für Legacy-Architekturen (MIPS, RISC-V), die micro-ROS nicht adressiert."

**Relevanz für VIA**: ⭐⭐⭐⭐ (Embedded Deployment Strategies)

---

### Paper 7: ROS2 Composition Documentation (2024)
**Typ**: Offizielle technische Dokumentation
**URL**: https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Composition.html
**Schlüsselkonzepte**:
- Intra-Process Communication (Zero-Copy Message Passing)
- Component Container (Single-Threaded, Multi-Threaded, Isolated Executors)
- Deploy-Time-Flexibilität: Separate Prozesse vs. Single Process

**Zitations-Kontext**:
Abschnitt 3.0.2, Zeile 197-212 (ROS-Prozesskommunikation vs. VIA):
> "**ROS Composition**: Deploy-Time-Entscheidung zwischen separate processes (fault isolation) und single process (lower overhead). **VIA Process-Group-Protocol**: Compile-Time-Entscheidung für IPC-Mechanismus (Pipe, Unix Socket, TCP) mit optionalem Runtime-Remapping über MMB."

**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (IPC-Optimierung Konzeptvergleich)

---

### Paper 8: Pardo-Castellote (2003) - OMG DDS Architectural Overview
**Bibliographie**: Pardo-Castellote, G. (2003). DOI: 10.1109/ICDCSW.2003.1203555
**Zitations-Kontext**: Abschnitt 3.0.2 (DDS QoS), Abschnitt 5.4 (OPC UA vs. DDS)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Middleware QoS Design Patterns)

---

### Paper 9: OMG (2015) - DDS Version 1.4
**Bibliographie**: OMG. (2015). Data Distribution Service (DDS) Version 1.4. formal/2015-04-10
**Zitations-Kontext**: Abschnitt 3.0.3 (RMW-Abstraktion), Abschnitt 3.5 (SOA DDS Integration)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Standards-Referenz)

---

### Paper 10: IEC 63278-1:2024 - AAS Metamodel
**Bibliographie**: IEC 63278-1:2024. Asset Administration Shell for Industrial Applications – Part 1: Metamodel
**Zitations-Kontext**: Abschnitt 1.1 (Ausgangssituation), Abschnitt 3.1 (AAS-core-works), Abschnitt 5.3 (Theoretischer Hintergrund)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Zentrale Standards-Grundlage)

---

### Paper 11: IEC 62541-1:2020 - OPC UA
**Bibliographie**: IEC 62541-1:2020. OPC Unified Architecture – Part 1: Overview and Concepts
**Zitations-Kontext**: Abschnitt 1.1 (M3-Bibliothek), Abschnitt 3.2 (OPC UA Stack), Abschnitt 5.4 (Information Model)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Kommunikations-Grundlage)

---

### Paper 12: Deb et al. (2002) - NSGA-II
**Bibliographie**: Deb, K., et al. (2002). A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II. *IEEE TEVC*, 6(2), 182-197. DOI: 10.1109/4235.996017
**Zitations-Kontext**: Abschnitt 2.2 (H1-Hypothese Pareto-Optimierung), Abschnitt 3.6 (IPC-Optimizer), Abschnitt 3.8.2 (Mathematische Rigorosität)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Kernalgorithmus für IPC-Optimizer)

---

### Paper 13: Zhang & Li (2007) - MOEA/D
**Bibliographie**: Zhang, Q., & Li, H. (2007). MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition. *IEEE TEVC*, 11(6), 712-731. DOI: 10.1109/TEVC.2007.892759
**Zitations-Kontext**: Abschnitt 3.6 (Alternative zu NSGA-II für >3 Objectives), Abschnitt 4.3.1 (Algorithmus-Design)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Alternative für komplexe Szenarien)

---

### Paper 14: De Moura & Bjørner (2008) - Z3 SMT Solver
**Bibliographie**: De Moura, L., & Bjørner, N. (2008). Z3: An Efficient SMT Solver. *TACAS 2008*, 337-340. DOI: 10.1007/978-3-540-78800-3_24
**Zitations-Kontext**: Abschnitt 2.2 (Constraint-Solver), Abschnitt 3.6 (IPC-Optimizer Integration), Abschnitt 3.8.2 (Beweisbar optimale Lösungen)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Constraint-Solver für IPC-Optimierung)

---

### Paper 15: Lattner & Adve (2004) - LLVM
**Bibliographie**: Lattner, C., & Adve, V. (2004). LLVM: A Compilation Framework. *CGO'04*, 75-86. DOI: 10.1109/CGO.2004.1281665
**Zitations-Kontext**: Abschnitt 2.3.1 (M3-Compiler Architektur), Abschnitt 5.1 (Compiler-Theorie), Abschnitt 6.1 (Template-Engine)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Compiler-Architektur Blueprint)

---

**Status**: 15/133 Papers analyzed (11.3%)
**Nächster Batch**: Papers 16-30 (Industrial Automation - Wollschlaeger, Vogel-Heuser, Fay)
# Papers 16-30: Industrial Automation (Wollschlaeger, Vogel-Heuser, Fay)

### Paper 16: Vogel-Heuser et al. (2025) - DSL4DPiFS
**Bibliographie**: Vogel-Heuser, B., et al. (2025). DSL4DPiFS - a graphical notation to model data pipeline deployment in forming systems. *Automatisierungstechnik*, 2025.
**Schlüsselkonzepte**: Graphische Notation für Deployment-Pipelines
**Zitations-Kontext**: Abschnitt 2.3.1 (M3-DSL), Abschnitt 6.2 (M2-SDK Deployment)
**Relevanz für VIA**: ⭐⭐⭐⭐ (DSL Design Patterns)

---

### Paper 17: Vogel-Heuser et al. (2025) - Ontology Versioning
**Bibliographie**: Vogel-Heuser, B., et al. (2025). Ontology Versioning for Managing Inconsistencies. *IEEE TASE*, 2025.
**Zitations-Kontext**: Abschnitt 3.1 (AAS-Versioning), Abschnitt 6.1 (M3-Compiler SemVer)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Versionierungs-Strategie)

---

### Paper 18: Vogel-Heuser et al. (2025) - Digital Twins Editorial
**Bibliographie**: Vogel-Heuser, B., et al. (2025). Guest Editorial: Engineering and Operating Digital Twins. *IEEE TASE*, 2025.
**Zitations-Kontext**: Abschnitt 2.3.4 (Horse-Rider Hot-Reload), Abschnitt 5.3 (Digital Twin Requirements)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Digital Twin Design Principles)

---

### Paper 19: Vogel-Heuser et al. (2024) - Model-driven Latency Analysis
**Bibliographie**: Vogel-Heuser, B., et al. (2024). Model-driven latency analysis of distributed skills.
**Zitations-Kontext**: Abschnitt 2.2 (H1 Latenz-Hypothese), Abschnitt 7.3.2 (Compile-Time Latenz-Garantien)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (H1-Hypothese Validierung)

---

### Paper 20: Wollschlaeger et al. (2025) - AAS Meets OPC UA
**Bibliographie**: Wollschlaeger, M., et al. (2025). AAS Meets OPC UA: A Unified Approach. *IEEE ICPS 2025*.
**Zitations-Kontext**: Abschnitt 1.1 (AAS-OPC UA Integration), Abschnitt 3.2 (Bidirektionales Mapping), Abschnitt 5.4 (Transformation-Rules)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Co-Advisor Paper, direkte VIA-Validierung)

---

### Paper 21: Santiago Soler Perez Olaya et al. (2024) - Multi-Message Broker
**Bibliographie**: Soler Perez Olaya, S., Wollschlaeger, M., et al. (2024). Dynamic Multi-Message Broker. *IEEE ETFA 2024*.
**Zitations-Kontext**: Abschnitt 3.4 (MMB Northbound/Southbound), Abschnitt 6.4.1 (Protokoll-Orchestrierung)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (MMB-Konzept Grundlage)

---

### Paper 22: Santiago Soler Perez Olaya et al. (2024) - SOA for I4.0
**Bibliographie**: Soler Perez Olaya, S., Wollschlaeger, M., et al. (2024). SOA for I4.0 Digital Twins. *IEEE IECON 2024*.
**Zitations-Kontext**: Abschnitt 3.5 (Microservice-Architektur), Abschnitt 6.4.3 (Service Contracts)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (SOA-Architektur Grundlage)

---

### Paper 23: Wollschlaeger et al. (2024) - Broker-Less OPC UA PubSub
**Bibliographie**: Wollschlaeger, M., et al. (2024). Broker-Less OPC UA PubSub Performance. *IEEE ICT 2024*.
**Zitations-Kontext**: Abschnitt 7.3.2 (H1 Baseline 2-5ms), Abschnitt 3.2 (Brokered vs Broker-Less)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Performance-Benchmarks)

---

### Paper 24: Wollschlaeger et al. (2024) - Capability/Requirement Processing
**Bibliographie**: Wollschlaeger, M., et al. (2024). Capability and Requirement Processing for AAS. *IEEE IECON 2024*.
**Zitations-Kontext**: Abschnitt 6.5 (Master Active Management Matching), Abschnitt 2.2 (Edge-Group-Protocol)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Edge-Group-Protocol Design)

---

### Paper 25: Wollschlaeger et al. (2024) - Test Framework for Reactive AAS
**Bibliographie**: Wollschlaeger, M., et al. (2024). Test Framework for Reactive AAS. *IEEE ETFA 2024*.
**Zitations-Kontext**: Abschnitt 4.4 (Testing-Phase), Abschnitt 6.1 (Reactive Systems Testing)
**Relevanz für VIA**: ⭐⭐⭐ (Test-Strategie)

---

### Paper 26: Fay et al. (2025) - AAS Integrated Toolchains
**Bibliographie**: Fay, A., et al. (2025). AAS for Integrated Toolchains and Collaborative Engineering.
**Zitations-Kontext**: Abschnitt 3.1 (Engineering-Toolchain), Abschnitt 1.1 (SITL Collaborative Engineering)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Toolchain-Integration)

---

### Paper 27: Fay et al. (2024) - AI-Assisted Engineering
**Bibliographie**: Fay, A., et al. (2024). AI-Assisted Engineering for Industry 4.0.
**Zitations-Kontext**: Abschnitt 6.1 (LLM Code-Generation - Future Work)
**Relevanz für VIA**: ⭐⭐ (Zukünftige Erweiterung)

---

### Paper 28: Jasperneite et al. (2023) - TSN Industrial Ethernet
**Bibliographie**: Jasperneite, J., et al. (2023). Time-Sensitive Networking for Industrial Ethernet.
**Zitations-Kontext**: Abschnitt 3.2 (OPC UA PubSub TSN), Abschnitt 2.2 (H1 TSN-Scheduling)
**Relevanz für VIA**: ⭐⭐⭐ (Echtzeit-Netzwerk)

---

### Paper 29: Urbas et al. (2023) - NAMUR MTP
**Bibliographie**: Urbas, L., et al. (2023). NAMUR Open Architecture for Modular Process Plants.
**Zitations-Kontext**: Abschnitt 6.4.2 (Edge-Group-Hierarchie analog NAMUR)
**Relevanz für VIA**: ⭐⭐⭐ (Hierarchische Orchestrierung)

---

### Paper 30: Urbas et al. (2024) - Process Automation Digitalization
**Bibliographie**: Urbas, L., et al. (2024). Digital Transformation of Process Automation.
**Zitations-Kontext**: Abschnitt 1.1 (Brownfield-Integration, Native Cross-Compilation)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Brownfield-Szenarien)

---

**Status**: 30/133 Papers analyzed (22.6%)
# Papers 31-79: Multi-Objective Optimization, Microservices, IPC, OPC UA, AAS

