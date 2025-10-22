# Exposé: Analyse eines Forschungsthemas - Prozesskommunikation

**Titel**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Autor**: Benjamin Probst
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Fakultät Informatik
**Datum**: Oktober 2025

---

## 1. Einleitung und Motivation

### 1.1 Ausgangssituation
- AAS (Asset Administration Shell) Repository von Dr. Santiago Soler Perez Olaya offenbart vollständige Compiler-Architektur
- M3/M2/M1 Metamodell-Struktur analog zu Prof. Castrillon (TU Dresden)
- Derzeitige Implementierung: Python-Skripte simulieren Compiler-Funktionalität
- Problem: Keine vollständige Compiler-Implementierung als externes Übersetzerprogramm

### 1.2 Vision: Industrie 5.0
- KI-gesteuerte Systembeschreibung: Kunde beschreibt System natürlichsprachlich
- Automatische Compilation und Deployment
- Software-in-the-Loop: Iterative Fehlerkorrektur gegen Kundenspezifikation
- Ziel: "Der Kunde beschreibt sein System der KI, die KI definiert Compiler-Beschreibung, Compiler generiert System"

### 1.3 Forschungslücke
- Fehlende Verbindung: Metamodell → Production-Grade Compiler → Deployment
- Keine wartbare, versionierte SDK-Generierung für industrielle Langzeitnutzung
- Manuelle Orchestrierung von >50.000 Edge-Geräten unzumutbar
- Heterogene Architekturen (MIPS, RISC-V, POWER9, x86, ARM, Sparc) erfordern Multi-Target-Compilation

---

## 2. Problemstellung und Forschungsfrage

### 2.1 Kontext: VIA-Gesamtsystem
**VIA (Virtual Industry Automation)** ist eine mehrstufige Compiler-Kette (M3→M2→M1) für heterogene Industriesysteme mit automatischer Orchestrierung von >50.000 Edge-Devices. Das Gesamtsystem umfasst:
- **M3-Compiler**: AAS Metamodell → C++ SDK
- **M2-SDK-Compiler**: Kundenprojekt → Systemprojekt mit Network Discovery
- **M1-System-Deployer**: Cross-Compilation, Horse-Rider-Deployment, Kubernetes-Orchestrierung

### 2.2 Fokus dieser Forschungsarbeit: Prozesskommunikations-Protokoll

**Forschungsfrage:**
> **Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?**

**Teilfragen:**
1. Welche M3-Modellelemente sind notwendig, um Prozesskommunikation zu beschreiben?
2. Wie kann der M2-SDK-Compiler aus Prozessabhängigkeiten optimale IPC-Mechanismen ableiten?
3. Welche Metriken bestimmen die Positionierung (gleicher Container, gleicher Host, Remote)?
4. Wie verhält sich das Process-Group-Protocol unter OPC UA bei >50.000 Geräten?

**Hypothesen:**
- **H1**: Compiler-basierte IPC-Optimierung reduziert Latenz um >30% gegenüber Runtime-Service-Mesh
- **H2**: Statische Positionierungsentscheidung (Compile-Time) erreicht 90% der Effizienz dynamischer Orchestrierung
- **H3**: Process-Group-Protocol skaliert linear bis 100.000 Services bei hierarchischer Gruppierung
- **H4**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um 60%

**Abgrenzung:** Diese Arbeit konzentriert sich auf das **Process-Group-Protocol-Subsystem** als Teil des VIA-Gesamtsystems. Die M3/M2/M1-Architektur dient als Kontext und theoretischer Rahmen.

### 2.3 Teilprobleme des Gesamtsystems (Kontext)

#### 2.3.0 Hauptprogramm (Orchestrierung M3→M2→M1)
- **Zentrale Koordination**: Hauptsystem orchestriert Verlauf der 3 Compiler-Phasen
- **Pipeline-Management**: Ergebnisse jeder Phase in nächste Phase überführen
- **Anwenderaufgaben**: Teil der Benutzerinteraktion übernehmen
- Input: Benutzerbeschreibung (natürlichsprachlich oder strukturiert)
- Output: Vollständig deployed System (Ende-zu-Ende)
- **Selbstreferenz**: "M3 mit sich selbst definieren" - Meilenstein der Forschung
- Problem: Zustandsverwaltung über 3 Phasen, Fehlerbehandlung bei jeder Stufe, Transaktionalität

#### 2.3.1 M3-Ebene (Metamodell-Compiler)
- Definition zweckgebundener Programmiersprache aus AAS-Elementen
- Vollständiger Compiler als statisches C++ Programm
- Input: AAS M3 Definitionen + Benutzerbeschreibung
- Output: M2 SDK (C++, Python, Java etc.)
- Problem: Spaghetti-Code bei aktueller Code-Generierung vermeiden

#### 2.3.2 M2-Ebene (SDK-Compiler)
- SDK als erneuter Compiler: Syntax-Prüfung, Tests, Projektvalidierung
- Automatische Network Discovery (SNMP, OPC UA, Modbus, MQTT, RPC)
- Vorschläge für Implementierung durch Netzwerkkartografie
- Output: Vollständiges C++ Kundensystemprojekt
- Kubernetes-Beschreibungen, Netzwerkprotokollimplementierungen
- Problem: Deterministische Testabdeckung für industrielle Kombinatorik

#### 2.3.3 M1-Ebene (System-Deployment)
- VIA-M1-System-Deployer: Kubernetes Cluster + Edge-Module ("Horses")
- Generierte Systemtests aus grober Kundenvordefinition
- Distributed Compilation via GitHub Runners
- Output: Deployable System für >50.000 Geräte
- Problem: Hot-Reload, Canary-Deployment, Versionskonsistenz bei C++23 Modules

#### 2.3.4 Deployment-System (Horse-Rider-Architektur)
- **Horse-Service**: Deployment-Service trägt Rider-Service (Fachlogik) als Prozess
- **Hot-Reload**: C++23 Modules mit stabilen ABIs für Canary Deployment
- **Redundanz**: Mindestens 2 parallele Mikroservices pro Edge-Gerät (Digital Twin)
- **Rollback**: Sekundenbruchteile bei Fehler, alte Version vorgehalten
- **Distributed Compilation**: GitHub Runners für parallele Module-Builds
- Problem: ABI-Stabilität, Zustandssynchronisation bei Hot-Reload, Rollback-Transaktionalität

#### 2.3.5 Sub-Protokolle unter OPC UA
- **Edge-Group-Protocol**: Virtuelle Netzwerkgruppen für Edgegeräte
- **Deploy-Protocol**: Versionierung, Logging, Systemupdates, Rejuvenation
- **Process-Group-Protocol**: IPC zwischen Services (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) → **FORSCHUNGSFOKUS**
- **MMB-Integration**: Many-to-Many Broadcast nach Dr. Soler Perez Olaya
- Problem: Protokoll-Komposition, Effizienz bei >50k Geräten, Sicherheitsschichten

#### 2.3.6 Network Discovery System
- **Auto-Discovery**: SNMP, OPC UA, Modbus, MQTT, RPC Scanner
- **Netzwerkkartografie**: Topologie-Erkennung, Geräte-Eigenschaften auslesen
- **Asset-Mapping**: Vorschläge für M2-Projektkonfiguration
- **Edge-Devices**: Messwertwandler, PLCs, SCADA-Systeme
- Problem: Protokoll-Heterogenität, Zugriffskontrolle, Offline-Geräte

#### 2.3.7 Master Active Management (Deployment-Orchestrierung)
- **Active/Active Redundanz**: Analog zu Active Directory Domäne
- **Zugriffskontrolle**: Rollen, Benutzer, Administratoren (Samba/AD-Integration)
- **Deployment-Master**: Konfiguration von Redundanz-Levels, Service-Verteilung
- **Koordination**: Kubernetes + VIA-eigene Edge-Service-Orchestrierung
- Problem: Split-Brain-Szenarien, Konsistenz über Cluster, Failover-Zeiten

#### 2.3.8 Multi-Architektur Cross-Compilation
- **Target-Architekturen**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc
- **Betriebssysteme**: Linux, Windows, Mac
- **Heterogenität**: Billigste Minicomputer (Edge) bis Verarbeitungs-Monster (Server)
- **CMake-Konfiguration**: M2-Ebene definiert Zielarchitekturen
- **Legacy-Support**: Industrie 4.0 + Industrie der Vergangenheit
- Problem: Toolchain-Management, Treiber-Verfügbarkeit, Memory-Modelle

---

## 3. Stand der Forschung

### 3.1 Asset Administration Shell (AAS)
- IEC 63278 Standard, aas-core-works: Python DSL für M3
- Code-Generator für 6 Sprachen, Limitation: Python-Skripte, keine Production-Compiler

### 3.2 OPC UA (IEC 62541)
- open62541: C99, ~250KB Footprint, Nodeset Compiler: XML → C
- 76+ Companion Specifications (DI, I4AAS, PLCopen)
- Limitation: Statische NodeSets, keine dynamische Orchestrierung

### 3.3 Multi-Message Broker (Dr. Santiago Soler Perez Olaya)
- Northbound: I4.0 OPC UA, Southbound: Legacy Assets
- AID/AIMC Submodels für Asset Mapping
- Limitation: Kein vollautomatisches Deployment

### 3.4 CMFM & SOA
- CMFM: Generality Hierarchy, VIA als Domain
- SOA: gRPC + Protobuf, Kubernetes Container
- Limitation: Keine Compiler-Kette, manuelle Orchestrierung

### 3.5 IPC & Service Mesh (Related Work)
- **gRPC**: HTTP/2, Protobuf, ~0.5ms Latenz (Single-Host), Service Discovery fehlt
- **ZeroMQ**: Message Queues, 5 Patterns (REQ/REP, PUB/SUB), keine Compiler-Integration
- **DDS (OMG Data Distribution Service)**: Real-Time, QoS-Policies, Overhead ~2ms, keine Metamodell-Abstraktion
- **Istio/Linkerd (Service Mesh)**: Runtime-Routing, Dynamic Discovery, Sidecar-Overhead 5-10ms
- **UNIX Domain Sockets**: ~20μs Latenz, nur lokale Prozesse, keine verteilte Orchestrierung
- **Limitation**: Alle Ansätze erfordern manuelle Konfiguration, keine Compile-Time-Optimierung

### 3.6 Forschungslücken
- Keine mehrstufige Compiler-Kette M3→M2→M1 für Prozesskommunikation
- Keine automatische IPC-Mechanismus-Auswahl bei Compilation
- Keine Sub-Protokolle unter OPC UA standardisiert
- Keine Compile-Time-Optimierung von Microservice-Positionierung
- Service Mesh Overhead (5-10ms) vs. potenzielle Compiler-Optimierung unerforscht

---

## 4. Zielsetzung und Forschungsmethodik

### 4.1 Hauptziel
**Entwicklung einer vollautomatischen Compiler-Kette (VIA) für Industrie 4.0-Systeme**

### 4.2 Teilziele
- **T1**: VIA-M3-Compiler (C++, AAS M3 → C++ SDK)
- **T2**: VIA-M2-SDK-Compiler (SDK → Kundensystem, Network Discovery)
- **T3**: VIA-M1-System-Deployer (Distributed Compilation, Horse-Rider)
- **T4**: Sub-Protokoll-Design (Edge/Deploy/Process-Group)
- **T5**: KI-Integration Industrie 5.0 (NLP → M3 → System)

### 4.3 Forschungsmethodik

#### 4.3.1 Methodisches Vorgehen
1. **Requirements Engineering**: M3-Modellelemente für Prozesskommunikation definieren (AAS-Extension)
2. **Design**: Compiler-Optimierungsalgorithmus (Graph-basiert, Constraint Solver)
3. **Prototypische Implementierung**: M2-SDK-Compiler mit IPC-Optimizer (C++20/23)
4. **Evaluation**: Benchmark-Suite, Use-Case-Implementierung, Vergleichsmessungen

#### 4.3.2 Evaluationsumgebung
- **Labor-Setup**: 3-Node Kubernetes Cluster (64 Core, 256 GB RAM, 10 Gbit/s Netzwerk)
- **Simulationstools**: Mininet für virtuelle Netzwerktopologien (bis 1.000 Nodes)
- **Benchmark-Szenarien**:
  - **S1**: Lokale Prozesskette (5 Services, gleicher Host)
  - **S2**: Verteilte Prozesskette (20 Services, 3 Hosts)
  - **S3**: Skalierungstest (100.000 Services, hierarchische Gruppierung)
  - **S4**: Real-World Use-Case (Industrieller SCADA + MES + PLC-Edge-Integration)

#### 4.3.3 Metriken & Erfolgskriterien
- **Latenz**: End-to-End Prozesskette (P50, P95, P99 Perzentile)
- **Throughput**: Nachrichten/Sekunde (Messages/s)
- **CPU-Last**: Prozessor-Auslastung bei Last (%)
- **Memory Footprint**: RAM-Verbrauch pro Service (MB)
- **Entwicklungszeit**: Manual vs. Metamodell-generiert (Stunden)
- **Erfolgskriterium**: H1-H4 bestätigt (siehe Hypothesen Kapitel 2.2)

#### 4.3.4 Vergleichsbaseline
- **Baseline 1**: Manuell konfiguriertes gRPC (statisch)
- **Baseline 2**: Istio Service Mesh (dynamisch)
- **Baseline 3**: UNIX Sockets (optimal, nur lokal)
- **VIA Process-Group-Protocol**: Compiler-optimiert

#### 4.3.5 Phasenplan
- **Phase 1**: Research & Analyse ✅ ABGESCHLOSSEN
- **Phase 2**: Playbook-Erstellung & Metamodell-Design ⏳ IN PROGRESS
- **Phase 3**: M2-SDK-Compiler Prototyp mit IPC-Optimizer (6 Wochen)
- **Phase 4**: Benchmark-Suite & Use-Case-Implementierung (4 Wochen)
- **Phase 5**: Evaluation & Vergleichsmessungen (4 Wochen)
- **Phase 6**: Dokumentation & Publikation (4 Wochen)

---

## 5. Theoretischer Hintergrund

### 5.1 Compiler-Theorie
- Multi-Stage Compilation: M3 → M2 → M1
- Code-Generation: Template-basiert, Type-Safe
- Metaprogramming: C++20 Concepts, Constexpr

### 5.2 Metamodell-Architekturen (M3/M2/M1)
- M3: Metamodell (Objects, Variables, Methods existieren)
- M2: Modell (VIA-spezifische Typen)
- M1: Instanz (Laufende Systeme)

### 5.3 Asset Administration Shell
- IEC 63278: Standardisiertes Metamodell
- Submodels: Modulare Datenbeschreibung
- AID/AIMC: Asset Interface Description + Mapping

### 5.4 OPC UA Information Model
- M3-basierte Typdefinitionen
- Companion Specifications: Domain-Erweiterungen
- Address Space: Hierarchische Nodes

### 5.5 Prozesskommunikation
- IPC Mechanisms: Pipe, Socket, TCP, File-Queue, Thread
- Data vs. Control vs. Management Plane
- gRPC + Protobuf: Contract-First, Binary Serialization

### 5.6 CMFM
- Generality Hierarchy: Domain > User > Implementation
- VIA as Domain: Gesamte Prozesskommunikations-Domain
- Promotion: Tacit vs. Explicit

---

## 6. Konzeptioneller Ansatz: VIA-Architektur

### 6.0 VIA-Hauptprogramm (Orchestrierung M3→M2→M1)

#### Input
- Benutzerbeschreibung des gewünschten Systems (natürlichsprachlich oder strukturiert)
- Konfiguration: Target-Architekturen, Deployment-Ziele, Netzwerk-Topologie

#### Verarbeitung
- **Phase-Coordination**: Sequenzieller Aufruf M3-Compiler → M2-SDK-Compiler → M1-Deployer
- **Pipeline-Management**: Output jeder Phase wird Input der nächsten
- **Zustandsverwaltung**: Persistierung Zwischenergebnisse (M2-SDK, M1-Systemprojekt)
- **Fehlerbehandlung**: Rollback bei Fehler, Logging jeder Phase
- **Anwenderinteraktion**: GUI/CLI für Fortschrittsanzeige, Zwischenentscheidungen

#### Output
- **Ende-zu-Ende**: Von Benutzerbeschreibung bis deployed System
- **Traceability**: Kompletter Audit-Trail (Beschreibung → M3 → M2 → M1 → Produktion)
- **Logs**: Jede Phase dokumentiert (für Debugging, Reproduzierbarkeit)

#### Besonderheit
- **Selbstreferenz**: Hauptprogramm nutzt VIA-M2-SDK (Bootstrap-Problem gelöst)
- **Transaktionalität**: Atomare Phasen, Rollback bei Fehler
- **Parallelisierung**: Mehrere Kundenprojekte gleichzeitig orchestrieren

### 6.1 VIA-M3-Compiler (Metamodell → SDK)
- **Input**: AAS M3 + VIA-Extensions + Benutzerdefinierte Typen
- **Verarbeitung**: C++20 Metaprogramming, Template-Engine, Constraint-Validation
- **Output**: VIA-M2-SDK-C++, OPC UA NodeSet XML, Protobuf, Dokumentation
- **Besonderheit**: Wartbar, versioniert, Testframework

### 6.2 VIA-M2-SDK-Compiler (SDK → Kundensystem)
- **Input**: Kundenprojekt (M3-Syntax), Netzwerk-Topologie, Deployment-Ziele
- **Verarbeitung**: Syntax-Prüfung, Network Discovery, Auto-Vorschläge, IPC-Optimierung
- **Output**: C++ Systemprojekt, Kubernetes Manifests, Edge-Modules, Tests
- **Besonderheit**: Release (RAM→g++), Debug (Projektdateien)

### 6.3 VIA-M1-System-Deployer (System → Produktion)
- **Input**: M2 Systemprojekt, Deployment-Targets, Architecture Map
- **Verarbeitung**: Distributed Compilation, Cross-Compilation, Horse-Rider, Master Orchestrierung
- **Output**: Deployed System >50.000 Geräte, Digital Twin, Monitoring, Logs
- **Besonderheit**: Hot-Reload, Canary Deployment, Sekundenbruchteile-Rollback

### 6.4 Sub-Protokolle unter OPC UA
- **Edge-Group-Protocol**: Virtuelle Netzwerkgruppen, Hardcoded Messages
- **Deploy-Protocol**: Versionierung, Metadaten, Horse-Rider
- **Process-Group-Protocol**: IPC zwischen Services (Pipe/Socket/TCP/File-Queue/Thread)

---

## 7. Erwartete Ergebnisse

### 7.1 Wissenschaftliche Beiträge (Fokus Prozesskommunikation)
- **B1**: Metamodell-Extension für Prozesskommunikation in AAS M3
- **B2**: Compiler-Optimierungsalgorithmus für IPC-Mechanismus-Auswahl
- **B3**: Process-Group-Protocol als OPC UA Sub-Protokoll
- **B4**: Benchmark-Vergleich: Compiler-Optimierung vs. Service Mesh vs. Manuelle Konfiguration
- **B5**: Skalierbarkeitsnachweis >100.000 Services mit hierarchischer Gruppierung

### 7.2 Praktische Ergebnisse
- **E1**: M2-SDK-Compiler Prototyp mit IPC-Optimizer (Open-Source)
- **E2**: Benchmark-Suite für IPC-Performance (Latenz, Throughput, CPU, Memory)
- **E3**: Use-Case-Implementierung: SCADA + MES + PLC-Edge-Integration
- **E4**: Standardisierungsvorschlag: VIA Process-Group-Protocol für OPC Foundation

### 7.3 Konkrete Evaluation-Kriterien

#### 7.3.1 Use-Case-Szenario: Automobilproduktion (Exemplarisch)
**System-Architektur:**
- **100 PLC-Edge-Devices**: Roboterarme, Förderbänder, Prüfstationen (MIPS/ARM, Linux)
- **10 MES-Server**: Manufacturing Execution System (x86, Windows Server)
- **3 SCADA-Server**: Supervisory Control, Visualisierung (x86, Linux)
- **5 Analytics-Services**: Predictive Maintenance, Quality Control (Kubernetes Pods)

**Prozesskette (Beispiel):**
1. PLC-Edge → MES: Produktionsdaten (1 Hz, 1 KB)
2. MES → Analytics: Aggregierte Daten (0.1 Hz, 10 KB)
3. Analytics → SCADA: Alarme + Prognosen (Event-based, 100 Bytes)
4. SCADA → PLC-Edge: Steuerkommandos (0.5 Hz, 50 Bytes)

**Erfolgsmetriken (quantitativ):**
- **Latenz P95 < 5ms** (End-to-End Prozesskette)
- **Throughput > 10.000 Msg/s** (Gesamtsystem)
- **CPU-Last < 20%** (pro Service)
- **Memory Footprint < 50 MB** (pro Service)
- **Entwicklungszeit: 8h manuell → 2h metamodell-generiert** (75% Reduktion)

#### 7.3.2 Vergleich mit Baselines
| Metrik | gRPC (manuell) | Istio Service Mesh | UNIX Sockets | VIA (Ziel) |
|--------|---------------|-------------------|--------------|------------|
| Latenz P95 | 2-5ms | 10-15ms | 0.05ms (lokal) | 1-3ms |
| Throughput | 50k Msg/s | 30k Msg/s | 200k Msg/s (lokal) | 80k Msg/s |
| CPU-Last | 15% | 25% | 5% (lokal) | 12% |
| Config-Zeit | 8h | 4h (Runtime-Auto) | N/A (lokal only) | 2h (Compile-Auto) |

### 7.4 Limitationen
- **L1**: Compile-Time-Optimierung erfordert statische Topologie (dynamische Änderungen → Neu-Compilation)
- **L2**: M3-Modellelemente noch nicht in offizieller AAS-Spezifikation
- **L3**: Cross-Architektur-Performance variiert (MIPS vs. x86)
- **L4**: Laborumgebung (3 Nodes) → Extrapolation auf >50k Geräte

---

## 8. Zeitplan (Fokus Prozesskommunikation)

- **Phase 1** (4 Wochen): Research & Analyse (AAS, OPC UA, IPC) ✅ ABGESCHLOSSEN
- **Phase 2** (2 Wochen): Playbook & M3-Metamodell-Design ⏳ IN PROGRESS
- **Phase 3** (6 Wochen): M2-SDK-Compiler Prototyp mit IPC-Optimizer
  - Woche 1-2: Graph-basierter Optimierungsalgorithmus
  - Woche 3-4: IPC-Mechanismus-Implementierung (Pipe, Socket, TCP, File-Queue, Thread)
  - Woche 5-6: Process-Group-Protocol unter OPC UA
- **Phase 4** (4 Wochen): Benchmark-Suite & Use-Case
  - Woche 1-2: Benchmark-Implementierung (Latenz, Throughput, CPU, Memory)
  - Woche 3-4: Automobilproduktion Use-Case (SCADA+MES+PLC)
- **Phase 5** (4 Wochen): Evaluation & Vergleichsmessungen
  - Woche 1: Baseline-Messungen (gRPC, Istio, UNIX Sockets)
  - Woche 2-3: VIA-Messungen & Skalierungstests
  - Woche 4: Auswertung & Hypothesen-Validierung
- **Phase 6** (4 Wochen): Dokumentation & Publikation
  - Woche 1-2: Forschungsbericht verfassen
  - Woche 3: Paper für INDIN/ETFA-Konferenz vorbereiten
  - Woche 4: OPC Foundation Standardisierungsvorschlag

**Gesamtdauer**: 24 Wochen (~6 Monate)

---

## 9. Literaturverzeichnis

### 9.1 Standards
1. IEC 63278 (2024). Asset Administration Shell
2. IEC 62541 (2020). OPC Unified Architecture
3. ISO/IEC 20922 (2016). MQTT Protocol
4. ISA-95 (2010). Enterprise-Control System Integration

### 9.2 Forschungsarbeiten (Dr. Santiago Soler Perez Olaya)
5. Soler Perez Olaya, S. et al. (2024). Dynamic Multi-Message Broker for I4.0 AAS
6. Soler Perez Olaya, S. et al. (2024). SOA for Digital Twins with gRPC and Protobuf
7. Soler Perez Olaya, S. & Wollschlaeger, M. (2022). CMFM Generality Hierarchy
8. Soler Perez Olaya, S. et al. (2019). CMFM for Heterogeneous Industrial Networks
9. Soler Perez Olaya, S. (2019). Role of CMFM in Network Management. PhD Thesis, TU Dresden

### 9.3 Open-Source Projekte
10. aas-core-works (2024). AAS SDKs and Tools. https://github.com/aas-core-works
11. open62541 (2024). OPC UA C99 Implementation. https://github.com/open62541/open62541
12. OPC Foundation (2024). UA-Nodeset Repository. https://github.com/OPCFoundation/UA-Nodeset

### 9.4 IPC & Service Mesh (Related Work)
13. Vinoski, S. (2006). Advanced Message Queuing Protocol. IEEE Internet Computing.
14. Hintjens, P. (2013). ZeroMQ: Messaging for Many Applications. O'Reilly Media.
15. OMG (2015). Data Distribution Service (DDS) v1.4. Object Management Group.
16. Li, H. et al. (2019). Understanding the overhead of service mesh. SoCC'19.
17. Istio Project (2024). Performance Benchmarks. https://istio.io/latest/docs/ops/deployment/performance-and-scalability/

### 9.5 Compiler-Optimierung & Metamodelle
18. Parr, T. (2010). Language Implementation Patterns. Pragmatic Bookshelf.
19. Lattner, C. & Adve, V. (2004). LLVM: A Compilation Framework. CGO'04.
20. Czarnecki, K. & Eisenecker, U. (2000). Generative Programming. Addison-Wesley.
21. Völter, M. et al. (2013). Model-Driven Software Development. Wiley.

### 9.6 IPC Performance Studies
22. Sridharan, A. et al. (2003). UNIX Domain Sockets vs. Internet Sockets. Linux Journal.
23. Google (2024). gRPC Performance Benchmarks. https://grpc.io/docs/guides/benchmarking/
24. Redis Labs (2019). Inter-Process Communication Performance Analysis.

### 9.7 Industrial Automation & Edge Computing
25. Plattform Industrie 4.0 (2023). Asset Administration Shell Reading Guide.
26. Sauter, T. (2010). The Three Generations of Field-Level Networks. IEEE Industrial Electronics Magazine.
27. Shi, W. et al. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal.

---

**Status**: ✅ Strukturiert mit Stichpunkten aus README.md & TODO.md
**Basis**: Phase 1 + Phase 2 Research-Erkenntnisse
**Nächste Schritte**: Literaturrecherche Quellen 13-27, Detaillierung nach Implementation, Transformation zu .docx
