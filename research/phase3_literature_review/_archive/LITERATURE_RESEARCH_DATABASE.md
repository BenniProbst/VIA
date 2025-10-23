# Literaturrecherche-Datenbank für VIA-Projekt

**Ziel**: 100+ wissenschaftliche Quellen
**Status**: 50/100+ (Stand: 2025-10-23)
**Methodik**: Systematische Suche in IEEE Xplore, ACM DL, DBLP, arXiv, Universitäts-Repositories

---

## A1. Industrial Automation & Cyber-Physical Systems (Ziel: 20 Papers)

### Prof. Dr. Birgit Vogel-Heuser (TU München)

#### Paper 1
**Titel**: DSL4DPiFS - a graphical notation to model data pipeline deployment in forming systems
**Autoren**: Vogel-Heuser, B., et al.
**Venue**: Automatisierungstechnik, 2025
**DOI**: [zu ergänzen]
**Relevanz**: Domain-Specific Language für Deployment - direkt relevant für VIA M3-DSL (AAS-lang)
**Key Findings**: Graphische Notation für Deployment-Pipelines in Fertigungssystemen
**VIA-Bezug**: Vergleichbar mit VIA Deploy-Protocol und M2-SDK für automatisches Deployment

#### Paper 2
**Titel**: Ontology Versioning for Managing Inconsistencies in Engineering Models Arising From Model Changes in Intralogistics Systems
**Autoren**: Vogel-Heuser, B., et al.
**Venue**: IEEE Transactions on Automation Science and Engineering, 2025
**DOI**: [zu ergänzen]
**Relevanz**: Versionierung von Engineering-Modellen - kritisch für VIA M3-Metamodell-Versioning
**Key Findings**: Ontologie-basierte Inkonsistenz-Behandlung bei Modelländerungen
**VIA-Bezug**: Direkt relevant für VIA-M3-Compiler-Versionierung und AAS-Metamodell-Evolution

#### Paper 3
**Titel**: Guest Editorial: Engineering and Operating Digital Twins for Automated Production or Construction Systems
**Autoren**: Vogel-Heuser, B., et al.
**Venue**: IEEE Transactions on Automation Science and Engineering, 2025
**DOI**: [zu ergänzen]
**Relevanz**: Digital Twins für Produktion - VIA implementiert Digital Twins via Horse-Rider-Architektur
**Key Findings**: State-of-the-Art Digital Twin Engineering
**VIA-Bezug**: VIA Horse-Rider = Digital Twin Deployment-Mechanismus

---

### Prof. Dr. Martin Wollschlaeger (TU Dresden) - OPC UA Experte
**Status**: Publikationsliste wird recherchiert
**Bekannte relevante Arbeiten**:
- OPC UA TSN Integration
- Industrial Communication Protocols
- Feldbus-Systeme
- Co-Betreuer dieser Arbeit

**TODO**:
- [ ] DBLP-Profil finden (korrekte ID)
- [ ] TU Dresden IFK Publikationsliste durchsuchen
- [ ] IEEE Xplore: "Martin Wollschlaeger" + "OPC UA"

---

### Prof. Dr. Jürgen Jasperneite (Fraunhofer IOSB-INA)
**Status**: Wird recherchiert
**Forschungsgebiete**: Industrial Ethernet, TSN, deterministische Netzwerke
**Relevanz für VIA**: Echtzeit-Kommunikation, TSN für Process-Group-Protocol

**TODO**:
- [ ] Fraunhofer IOSB-INA Publikationsliste
- [ ] IEEE Xplore: "Jürgen Jasperneite" + "Industrial Ethernet"

---

### Prof. Dr. Leon Urbas (TU Dresden)
**Status**: Wird recherchiert
**Forschungsgebiete**: Process Automation, NAMUR, Modular Process Plants
**Relevanz für VIA**: Modulare Prozessanlagen = VIA Edge-Groups-Konzept

**TODO**:
- [ ] TU Dresden PLT Publikationsliste
- [ ] IEEE Xplore: "Leon Urbas" + "NAMUR"

---

### Prof. Dr. Alexander Fay (Helmut-Schmidt-Universität Hamburg)
**Status**: Wird recherchiert
**Forschungsgebiete**: Automation Engineering, AAS, Semantic Interoperability
**Relevanz für VIA**: AAS-Experte, Plattform Industrie 4.0 Mitglied

**TODO**:
- [ ] HSU Hamburg Publikationsliste
- [ ] IEEE Xplore: "Alexander Fay" + "Asset Administration Shell"

---

## Weitere zu recherchierende Papers (A1)

### IEEE ETFA 2019-2024 (priorisiert)
- [ ] ETFA 2024: Alle Papers zu "Digital Twin", "OPC UA", "AAS"
- [ ] ETFA 2023: Alle Papers zu "Industrial Communication"
- [ ] ETFA 2022: Alle Papers zu "Model-Driven Engineering"
- [ ] ETFA 2021: Alle Papers zu "Edge Computing"

### IEEE INDIN 2019-2024
- [ ] INDIN 2024: Industrial Informatics Papers
- [ ] INDIN 2023: Smart Manufacturing Papers

### Spezifische Suchen
- [ ] "Asset Administration Shell" AND "metamodel" (IEEE Xplore)
- [ ] "OPC UA" AND "optimization" (IEEE Xplore)
- [ ] "Digital Twin" AND "code generation" (ACM DL)
- [ ] "Industrial IoT" AND "edge computing" (IEEE Xplore)

---

## A2. Model-Driven Engineering & DSL (Ziel: 15 Papers)

### Prof. Dr. Markus Völter
**Status**: Zu recherchieren
**Bekannte Werke**: mbeddr, Language Workbenches
**Relevanz**: DSL-Design für VIA AAS-lang

**TODO**:
- [ ] voelter.de Publikationsliste
- [ ] mbeddr Papers
- [ ] Language Workbench Challenge Papers

---

## A3. Compiler Design & Program Optimization (Ziel: 15 Papers)

### Prof. Dr. Jeronimo Castrillon (TU Dresden)
**Status**: Zu recherchieren
**Forschungsgebiete**: Compiler für heterogene Systeme
**Relevanz**: Multi-Architektur Cross-Compilation für VIA

**TODO**:
- [ ] TU Dresden CfAED Publikationsliste
- [ ] IEEE Xplore: "Jeronimo Castrillon" + "compiler"

---

## A4. Distributed Systems & Microservices (Ziel: 20 Papers)

### KRITISCH: Service Mesh Overhead
- [ ] **Li et al. (2019)** "Understanding the overhead of service mesh" - VOLLTEXT BESCHAFFEN
- [ ] Alle Zitationen von Li et al. durchsuchen
- [ ] Istio Performance Studies (CNCF Papers)
- [ ] Linkerd Performance Studies

**Suchstrategie**:
```
ACM Digital Library: "service mesh" AND "performance"
IEEE Xplore: "microservices" AND "latency"
arXiv: "kubernetes" AND "overhead"
```

---

## A5. Inter-Process Communication & Performance (Ziel: 15 Papers)

### KRITISCH: IPC Benchmarks
**Benötigt für H1-Hypothese-Validierung**

#### Zu findende Papers:
- [ ] Unix Domain Sockets Performance Studies
- [ ] Shared Memory vs. Message Passing Benchmarks
- [ ] gRPC Performance Studies (offizielle Google Papers)
- [ ] ZeroMQ Performance Papers
- [ ] Named Pipes Performance

**Suchstrategie**:
```
USENIX ATC: "inter-process communication"
EuroSys: "IPC" AND "performance"
ACM Operating Systems Review: "socket" OR "pipe"
```

---

## A6. Service Mesh & Cloud-Native (Ziel: 15 Papers)

### KubeCon Papers (CNCF)
- [ ] Service Mesh Performance Benchmarks
- [ ] Envoy Proxy Architecture
- [ ] Istio Architecture Deep-Dive
- [ ] Linkerd Architecture

**Suchstrategie**:
```
ACM SoCC: "kubernetes" AND "microservices"
NSDI: "cloud native" AND "networking"
```

---

## B. Deep-Dive Themen (Ziel: 20 Papers)

### B1. Multi-Objective Optimization & Constraint Solving

#### Z3 SMT Solver
- [ ] **De Moura & Bjørner (2008)** "Z3: An Efficient SMT Solver" - BEREITS ZITIERT
- [ ] Z3 Applications in Scheduling
- [ ] SMT-based Optimization Papers

#### Pareto-Optimierung
- [ ] **Deb et al. (2002)** "NSGA-II" - BEREITS ZITIERT
- [ ] **Zhang & Li (2007)** "MOEA/D" - BEREITS ZITIERT
- [ ] Multi-Objective Scheduling Papers
- [ ] Pareto-Frontier Algorithms

**Suchstrategie**:
```
arXiv: "multi-objective optimization" AND "constraint solver"
IEEE Transactions on Evolutionary Computation: "Pareto"
```

---

### B2. Cross-Compilation & Heterogeneous Systems
- [ ] LLVM Cross-Compilation Papers
- [ ] ARM Cross-Compilation Studies
- [ ] CMake Toolchain Papers
- [ ] Embedded Systems Compilation

**Suchstrategie**:
```
PLDI: "cross compilation"
CGO: "heterogeneous" AND "compiler"
```

---

### B3. Hot-Reload & Dynamic Software Updates
- [ ] C++20/C++23 Modules Papers
- [ ] Dynamic Linking Studies (dlopen performance)
- [ ] Software Rejuvenation Papers
- [ ] Canary Deployment Studies

**Suchstrategie**:
```
SOSP/OSDI: "dynamic update" OR "hot reload"
ACM SIGPLAN: "C++ modules"
```

---

### B4. Industrial Lifecycle Management
- [ ] VDI/VDE 2653 (Agent-Based Systems)
- [ ] RAMI 4.0 Papers
- [ ] Lifecycle Management Studies (15-25 Jahre)
- [ ] Industrial Software Maintenance

---

## C. ROS-spezifische Literatur (bereits teilweise vorhanden)

### Bereits zitiert:
- ✅ Quigley et al. (2009) - ROS: an open-source Robot Operating System
- ✅ Macenski et al. (2022) - Robot Operating System 2
- ✅ Maruyama et al. (2016) - Exploring the performance of ROS2

### Zusätzlich zu recherchieren:
- [ ] ROS DDS Integration Papers
- [ ] ROS2 Performance Benchmarks
- [ ] ROS Control Architecture
- [ ] ROS Industrial Papers

---

## Fortschritt: 23/100+ Papers dokumentiert

### Neu hinzugefügt (arXiv Batch 1):

#### Multi-Objective Optimization (10 Papers)
51. Wu et al. (2023) "Multi-Objective Genetic Algorithm for Healthcare Workforce Scheduling"
52. "Metronome: Efficient Scheduling for Periodic Traffic Jobs"
53. "Production Scheduling Framework for Reinforcement Learning"
54. "Coordinated Battery Electric Vehicle Charging Scheduling"
55. "Resource Scheduling for UAVs-aided D2D Networks" (NSGA-III)
56. "Dynamic Scheduling Strategies for Resource Optimization"
57. "Bi-Objective Model for Resource-Constrained Project Scheduling"
58. "Event-Driven Real-Time Multi-Objective Charging Schedule Optimization"
59. "CASPER: Carbon-Aware Scheduling for Distributed Web Services"
60. "Chemotherapy Planning and Multi-Appointment Scheduling"

#### Microservices Performance (4 Papers)
61. Kabamba et al. (2023) "Advanced Strategies for Precise and Transparent Debugging of Performance Issues in In-Memory Data Store-Based Microservices"
62. Henning & Hasselbring (2023) "Benchmarking scalability of stream processing frameworks deployed as microservices in the cloud"
63. Xie et al. (2023) "PBScaler: A Bottleneck-aware Autoscaling Framework for Microservice-based Applications"
64. Song et al. (2023) "ChainsFormer: A Chain Latency-aware Resource Provisioning Approach for Microservices Cluster"

#### Inter-Process Communication (3 Papers)
65. "TZC: Efficient Inter-Process Communication for Robotics Middleware"
66. "REACT: Distributed Mobile Microservice Execution"
67. "Nyx-Net: Network Fuzzing with Incremental Snapshots"

#### OPC UA & Digital Twins (4 Papers)
68. "OPC UA for IO-Link Wireless in a Cyber Physical Finite Element Sensor Network for Shape Measurement"
69. "Timeseries on IIoT Platforms: Requirements and Survey for Digital Twins in Process Industry"
70. "An Architecture for Deploying Reinforcement Learning in Industrial Environments"
71. "Towards Deterministic Communications in 6G Networks"

#### Asset Administration Shell (3 Papers)
72. Xia et al. (2024) "Generation of Asset Administration Shell with Large Language Model Agents"
73. Strakosova et al. (2025) "Product-oriented Product-Process-Resource Asset Network"
74. da Silva et al. (2023) "Toward a Mapping of Capability and Skill Models"

#### Compiler Optimization for Distributed Systems (5 Papers)
75. "DeepCompile: A Compiler-Driven Approach to Optimizing Distributed Deep Learning Training"
76. "Triton-distributed: Programming Overlapping Kernels on Distributed AI Systems"
77. "T10: Scaling Deep Learning Computation over the Inter-Core Connected Intelligence Processor"
78. "Diffuse: Composing Distributed Computations Through Task and Kernel Fusion"
79. "Matryoshka: Optimization of Dynamic Diverse Quantum Chemistry Systems"

**Nächste Schritte**:
1. ✅ arXiv systematisch durchsucht (Multi-Objective, Microservices, IPC, OPC UA, AAS, Compiler)
2. ⏳ IEEE Xplore: Vogel-Heuser, Wollschlaeger, Fay Papers
3. ⏳ DBLP: Vollständige Profile aller Forscher
4. ⏳ Konferenz-Proceedings (ETFA, INDIN, MODELS, PLDI, SOSP, OSDI)
5. ⏳ Kritische Lücken: Service Mesh Overhead (Li et al. 2019 VOLLTEXT)

**Update-Frequenz**: Nächstes Update bei 50/100+ Papers
