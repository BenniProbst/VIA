# Forschungszusammenfassung und Arbeitsplan

**Datum**: 2025-10-23
**Status**: Phase 2 - Literaturrecherche und Exposé-Überarbeitung

---

## ✅ Abgeschlossene Aufgaben

### 1. Performance-Claims entfernt/umformuliert
- Hypothesen H1-H4 als "zu testende" markiert statt feste Behauptungen
- Vergleichstabelle (Abschnitt 7.3.2) mit Hinweis versehen: "Projektziele, keine gemessenen Ergebnisse"
- Footnotes mit Literaturquellen hinzugefügt
- Zeile 66-69: Umformuliert zu "hat das Potenzial", "soll", "zu messen in Phase 5"

### 2. ROS-VIA-Integration konzipiert
- Umfassender neuer Abschnitt 3.0 "Robot Operating System (ROS) - Verwandte Architektur und potenzielle VIA-Integration"
- ROS als potentielles VIA-Subsystem beschrieben (nicht nur Vergleich)
- 3 Integrationsszenarien ausgearbeitet:
  1. ROS-Nodes als VIA-Prozesse
  2. ROS-Roboter als Edge-Gruppen
  3. ROS-Messages als M3-Datatypes
- Wissenschaftlicher Mehrwert der Integration dargestellt
- Abgrenzung: ROS-Integration als Post-Dissertation Extension

### 3. Fachbereiche und Forschungsgruppen identifiziert

#### Fachbereich 1: Industrial Automation & Cyber-Physical Systems
**Führende Forscher:**
- Prof. Dr. Martin Wollschlaeger (TU Dresden) - OPC UA, Industrial Communication
- Prof. Dr. Birgit Vogel-Heuser (TU München) - Industrial Automation, Model-Driven Engineering
- Prof. Dr. Jürgen Jasperneite (Fraunhofer IOSB-INA) - Industrial Ethernet, TSN
- Prof. Dr. Leon Urbas (TU Dresden) - Process Automation, NAMUR
- Prof. Dr. Alexander Fay (Helmut-Schmidt-Universität Hamburg) - Automation Engineering, AAS

**Relevante Konferenzen:**
- IEEE ETFA (Emerging Technologies and Factory Automation)
- IEEE INDIN (Industrial Informatics)
- IEEE WFCS (Workshop on Factory Communication Systems)

#### Fachbereich 2: Model-Driven Engineering & DSL
**Führende Forscher:**
- Prof. Dr. Markus Völter (Independent) - Language Workbenches, mbeddr
- Prof. Dr. Bernhard Rumpe (RWTH Aachen) - Model-Based Software Engineering
- Prof. Dr. Steffen Becker (Universität Stuttgart) - Component-Based Software Engineering
- Prof. Dr. Jean Bézivin (†) (Université de Nantes) - Model-Driven Engineering Pioneer
- Prof. Dr. Jordi Cabot (ICREA, UOC) - Model-Driven Software Development

**Relevante Konferenzen:**
- MODELS (ACM/IEEE International Conference on Model Driven Engineering Languages and Systems)
- SLE (Software Language Engineering)
- ECMFA (European Conference on Modelling Foundations and Applications)

#### Fachbereich 3: Compiler Design & Program Optimization
**Führende Forscher:**
- Prof. Dr. Chris Lattner (Modular AI, ex-Apple/Tesla) - LLVM, MLIR
- Prof. Dr. Vikram Adve (University of Illinois) - LLVM Co-Creator
- Prof. Dr. Jeronimo Castrillon (TU Dresden) - Compiler for Heterogeneous Systems
- Prof. Dr. Mary Hall (University of Utah) - Auto-Tuning, Loop Optimization
- Prof. Dr. Keshav Pingali (University of Texas at Austin) - Parallelizing Compilers

**Relevante Konferenzen:**
- PLDI (Programming Language Design and Implementation)
- CGO (Code Generation and Optimization)
- OOPSLA (Object-Oriented Programming, Systems, Languages & Applications)

#### Fachbereich 4: Distributed Systems & Microservices
**Führende Forscher:**
- Prof. Dr. Leslie Lamport (Microsoft Research) - Distributed Systems Theory
- Prof. Dr. Barbara Liskov (MIT) - Distributed Objects
- Prof. Dr. Ken Birman (Cornell University) - Cloud Computing, Reliable Multicast
- Prof. Dr. Indranil Gupta (UIUC) - Distributed Systems, Cloud Computing
- Prof. Dr. Ion Stoica (UC Berkeley) - Cloud Computing, Apache Spark

**Relevante Konferenzen:**
- SOSP (Symposium on Operating Systems Principles)
- OSDI (Operating Systems Design and Implementation)
- NSDI (Networked Systems Design and Implementation)

#### Fachbereich 5: Inter-Process Communication & Performance
**Führende Forscher:**
- W. Richard Stevens (†) - UNIX Programming (posthum relevant)
- Prof. Dr. Remzi Arpaci-Dusseau (University of Wisconsin-Madison) - Operating Systems
- Prof. Dr. Robert Morris (MIT) - Distributed Systems
- Prof. Dr. Michael Stumm (University of Toronto) - OS, Distributed Shared Memory
- Prof. Dr. Hakim Weatherspoon (Cornell University) - Distributed Systems

**Relevante Konferenzen:**
- USENIX ATC (Annual Technical Conference)
- EuroSys (European Conference on Computer Systems)
- ASPLOS (Architectural Support for Programming Languages and Operating Systems)

#### Fachbereich 6: Service Mesh & Cloud-Native
**Führende Forscher/Experten:**
- Brendan Burns (Microsoft, Kubernetes Co-Creator)
- Kelsey Hightower (Google Cloud)
- William Morgan (Buoyant, Linkerd Creator)
- Prof. Dr. Adrian Mouat (Container Solutions)
- Matt Klein (Lyft, Envoy Creator)

**Relevante Konferenzen:**
- KubeCon + CloudNativeCon
- SREcon
- ACM SoCC (Symposium on Cloud Computing)

### 4. Literaturliste von 27 auf 50 Einträge erweitert
Siehe Exposé Abschnitt 9 - Literaturverzeichnis

---

## 📋 Arbeitsplan für weitere Literaturrecherche (100+ Quellen)

### Phase A: Systematische Datenbanksuche pro Fachbereich (Ziel: 100+ Papers)

#### A1. Industrial Automation & Cyber-Physical Systems (Ziel: 20 Papers)
**Suchstrategie:**
- IEEE Xplore: "Asset Administration Shell" OR "OPC UA" AND "Industry 4.0"
- IEEE Xplore: "digital twin" AND "industrial automation"
- ACM Digital Library: "cyber-physical systems" AND "metamodel"
- Zeitraum: 2018-2025 (letzte 7 Jahre)

**Zu recherchierende Autoren:**
- Martin Wollschlaeger (TU Dresden) - alle Papers zu OPC UA
- Birgit Vogel-Heuser (TU München) - alle Papers zu MDE in Automation
- Jürgen Jasperneite (Fraunhofer) - alle Papers zu Industrial Ethernet
- Leon Urbas (TU Dresden) - NAMUR-Papers
- Alexander Fay (HSU Hamburg) - AAS-Papers

#### A2. Model-Driven Engineering & DSL (Ziel: 15 Papers)
**Suchstrategie:**
- ACM Digital Library: "model-driven engineering" AND "code generation"
- IEEE Xplore: "domain-specific language" AND "metamodel"
- MODELS Conference Proceedings: 2020-2024
- SLE Conference Proceedings: 2020-2024

**Zu recherchierende Autoren:**
- Markus Völter - mbeddr, Language Workbenches
- Bernhard Rumpe - MontiCore, UML/P
- Jordi Cabot - Model-Driven Web Engineering
- Steffen Becker - Palladio Component Model

#### A3. Compiler Design & Program Optimization (Ziel: 15 Papers)
**Suchstrategie:**
- ACM Digital Library: "compiler optimization" AND "distributed systems"
- PLDI Proceedings: 2020-2024
- CGO Proceedings: 2020-2024
- arXiv: "heterogeneous systems" AND "compiler"

**Zu recherchierende Autoren:**
- Chris Lattner - LLVM, MLIR
- Jeronimo Castrillon - TU Dresden, Compiler for Heterogeneous Systems
- Mary Hall - Auto-Tuning, Polyhedral Compilation
- Keshav Pingali - Graph Compilers

#### A4. Distributed Systems & Microservices (Ziel: 20 Papers)
**Suchstrategie:**
- ACM Digital Library: "microservices" AND "performance" AND "IPC"
- SOSP Proceedings: 2019-2024
- OSDI Proceedings: 2019-2024
- NSDI Proceedings: 2019-2024

**Spezifische Suchen:**
- "service mesh" AND "overhead" (für H1-Hypothese)
- "inter-process communication" AND "optimization"
- "distributed systems" AND "compile-time optimization"

#### A5. Inter-Process Communication & Performance (Ziel: 15 Papers)
**Suchstrategie:**
- USENIX ATC Proceedings: 2019-2024
- EuroSys Proceedings: 2019-2024
- ACM Operating Systems Review
- Search: "IPC performance", "UNIX domain sockets", "shared memory"

**Spezifische Benchmarks suchen:**
- Unix Domain Sockets vs. TCP Sockets (Performance-Vergleiche)
- gRPC Performance Studies
- ZeroMQ, MQTT, AMQP Performance Comparisons

#### A6. Service Mesh & Cloud-Native (Ziel: 15 Papers)
**Suchstrategie:**
- ACM SoCC Proceedings: 2019-2024
- KubeCon Proceedings (soweit verfügbar)
- Cloud-Native Computing Foundation (CNCF) Technical Papers

**Spezifische Suchen:**
- Istio Performance (kritisch für H1)
- Linkerd Performance
- Envoy Proxy Benchmarks
- Service Mesh Overhead Studies (Li et al. 2019 als Basis)

---

### Phase B: Spezifische Themen-Deep-Dives (Ziel: zusätzliche 20+ Papers)

#### B1. Multi-Objective Optimization & Constraint Solving
- Z3 SMT Solver Papers (Microsoft Research)
- Pareto-Optimierung für Scheduling/Resource Allocation
- Multi-Objective Evolutionary Algorithms (NSGA-II, MOEA/D)

#### B2. Cross-Compilation & Heterogeneous Systems
- ARM Cross-Compilation Studies
- Embedded Systems Compilation
- LLVM Cross-Compilation
- CMake Toolchain Papers

#### B3. Hot-Reload & Dynamic Software Updates
- C++ Modules (C++20/23)
- Dynamic Linking, dlopen() Performance
- Software Rejuvenation
- Canary Deployment Studies

#### B4. Industrial Lifecycle Management
- VDI/VDE Standards (2653, 2206, 3695)
- RAMI 4.0 (Reference Architecture Model Industrie 4.0)
- Lifecycle Management für industrielle Software (15-25 Jahre)

---

### Phase C: Historische und Grundlagenwerke (bereits teilweise vorhanden)

#### C1. Compiler-Klassiker
- ✅ Lattner & Adve (2004) - LLVM
- ✅ Czarnecki & Eisenecker (2000) - Generative Programming
- ✅ Parr (2010) - Language Implementation Patterns

#### C2. Distributed Systems Klassiker
- ✅ Lamport Papers (Byzantine Generals, Paxos, TLA+)
- ✅ Liskov Papers (Distributed Object Systems)

#### C3. Operating Systems & IPC Klassiker
- ✅ Stevens & Rago (2013) - Advanced Programming in the UNIX Environment

---

## 🎯 Unmittelbare nächste Schritte (priorisiert)

### 1. Kritische Lücken schließen (HÖCHSTE PRIORITÄT)
- [ ] **Li et al. (2019)** "Understanding the overhead of service mesh" - VOLLSTÄNDIGE Zitation mit Messwerten
- [ ] **gRPC Benchmarks** - Offizielle Performance-Daten
- [ ] **Istio Performance** - Dokumentierte Overhead-Werte
- [ ] **Unix Domain Sockets** - Performance-Studien mit Latenz-Messungen
- [ ] **DDS Performance** - RTI/eProsima Benchmarks

### 2. Santiago Soler Perez Olaya Papers vervollständigen
- [ ] ETFA 2024 Paper - DOI ergänzen (sobald veröffentlicht)
- [ ] IECON 2024 Paper - DOI ergänzen (sobald veröffentlicht)
- [ ] Alle älteren Papers: DOIs validieren

### 3. Forscherlisten pro Fachbereich erweitern
- [ ] Google Scholar Profile für jeden identifizierten Forscher
- [ ] Top 10 Papers pro Forscher identifizieren
- [ ] H-Index und Zitationszahlen dokumentieren

### 4. Konferenz-Proceedings systematisch durchsuchen
- [ ] IEEE ETFA 2019-2024 - alle relevanten Papers
- [ ] IEEE INDIN 2019-2024 - alle relevanten Papers
- [ ] MODELS 2020-2024 - MDE-Papers
- [ ] PLDI 2020-2024 - Compiler-Papers
- [ ] SOSP/OSDI 2019-2024 - Distributed Systems Papers

---

## 📊 Fortschrittstracking

### Literatureinträge: 50/100+
- ✅ Standards: 7
- ✅ ROS-Literatur: 3
- ✅ Santiago Soler Perez Olaya: 5
- ✅ Open-Source Projekte: 3
- ✅ IPC & Service Mesh: 7
- ✅ DDS: 4
- ✅ Compiler-Optimierung: 4
- ✅ Multi-Objective Optimization: 3
- ✅ Industrial Automation: 4
- ✅ ZeroMQ & MQ: 2
- ✅ Distributed Systems: 2
- ✅ C++ Template Metaprogramming: 2
- ✅ Industrial Lifecycle: 4

### Noch zu recherchieren: 50+
- ⏳ Fachbereich 1 (Industrial Automation): 20 Papers
- ⏳ Fachbereich 2 (MDE): 15 Papers
- ⏳ Fachbereich 3 (Compiler): 15 Papers
- ⏳ Fachbereich 4 (Distributed): 20 Papers
- ⏳ Fachbereich 5 (IPC): 15 Papers
- ⏳ Fachbereich 6 (Service Mesh): 15 Papers
- ⏳ Deep-Dives: 20 Papers

---

## 🔍 Suchstrategie-Template

Für jedes Paper:
1. **Identifikation**: Titel, Autoren, Jahr, Venue
2. **Relevanzprüfung**: Abstract lesen, passt es zu VIA-Themen?
3. **Kategorisierung**: Welcher Fachbereich? Welche Forschungsfrage adressiert?
4. **Zitation**: DOI, URL, vollständige Bibliographie
5. **Key Findings**: 2-3 Sätze zu Haupterkenntnissen
6. **VIA-Relevanz**: Wie unterstützt dies die VIA-Forschung?

---

## 📝 Notizen

### OPC Foundation Technical Advisory Council (kontaktieren)
- Stefan Hoppe (Beckhoff) - President
- Thomas Hahn (Siemens) - Vice President
- Karl Deiretsbacher - Technical Director
- Jim Luth - Chief Technology Officer
- Randy Armstrong - Lead Security Architect

**Ziel**: Feedback zu VIA Custom Companion Specification einholen

### IDTA (Industrial Digital Twin Association)
- aas-core-works Maintainer kontaktieren
- Mögliche Standardisierung von VIA-Extensions diskutieren

---

**Nächstes Update**: Nach Abschluss von Phase A1 (20 Industrial Automation Papers)
