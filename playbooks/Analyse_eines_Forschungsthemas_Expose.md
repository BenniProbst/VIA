# Exposé: Analyse eines Forschungsthemas - Prozesskommunikation

**Titel**: VIA - Virtual Integration Architecture: Self-Modeling and Building Systems for Industry 4.0

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
**VIA (Virtual Integration Automation)** ist eine mehrstufige Compiler-Kette (M3→M2→M1) für heterogene Industriesysteme mit automatischer Orchestrierung von >50.000 Edge-Devices. Das Gesamtsystem umfasst:
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

### 3.5 Forschungslücken
- Keine mehrstufige Compiler-Kette M3→M2→M1
- Keine automatische Orchestrierung >50.000 Geräte
- Keine Sub-Protokolle unter OPC UA standardisiert
- Keine Horse-Rider-Deployment mit C++23 erforscht

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
- **Phase 1**: Research & Analyse ✅ ABGESCHLOSSEN
- **Phase 2**: Playbook-Erstellung ⏳ IN PROGRESS
- **Phase 3**: Prototypische Implementierung (VIA-M3-Compiler)
- **Phase 4**: Evaluation (Benchmark, Skalierbarkeit, Use-Case)
- **Phase 5**: Dokumentation & Publikation

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

### 7.1 Wissenschaftliche Beiträge
- **B1**: Mehrstufige Compiler-Architektur (M3→M2→M1), Production-Grade
- **B2**: Sub-Protokoll-Design, Standardisierungsvorschlag OPC Foundation
- **B3**: Horse-Rider-Deployment mit C++23 Modules, Hot-Reload
- **B4**: Automatische Network Discovery & Orchestrierung >50.000 Geräte
- **B5**: KI-Integration Industrie 5.0 (NLP → M3 → System)

### 7.2 Praktische Ergebnisse
- **E1**: VIA-Toolchain (Open-Source): M3-Compiler, M2-SDK, M1-Deployer
- **E2**: VIA Companion Specification für OPC UA
- **E3**: Benchmark-Ergebnisse (Code-Gen Speed, Runtime, Skalierbarkeit)
- **E4**: Industrieller Use-Case (Partner-Firma, Real-World Deployment)

### 7.3 Limitationen
- **L1**: Komplexität Testabdeckung → Constraint-basierte Test-Generierung
- **L2**: C++23 Module ABI-Stabilität → Konservatives ABI-Subset
- **L3**: Skalierbarkeit >50K → Hierarchische Orchestrierung
- **L4**: Sicherheit Hot-Reload → Signierte Modules, Secure Boot

---

## 8. Zeitplan

- **Phase 1** (4 Wochen): Research & Playbooks ✅ ABGESCHLOSSEN
- **Phase 2** (2 Wochen): Implementation Playbooks
- **Phase 3** (6 Wochen): VIA-M3-Compiler Prototyp
- **Phase 4** (6 Wochen): VIA-M2-SDK-Compiler Prototyp
- **Phase 5** (6 Wochen): VIA-M1-System-Deployer Prototyp
- **Phase 6** (4 Wochen): Evaluation & Benchmarking
- **Phase 7** (4 Wochen): Dokumentation & Publikation

**Gesamtdauer**: 32 Wochen (~8 Monate)

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

### 9.4 Weitere Quellen (geplant: +15 nach weiterem Research)
13-27. [Placeholder: Compiler-Theorie, C++23 Modules, Kubernetes Edge, gRPC Benchmarks, Industrial Protocols, Canary Deployment, Cross-Compilation, Digital Twins, NLP System Config, Software-in-the-Loop, Distributed Builds, IPC Performance, Metamodeling, Code Generation, Industrial Cybersecurity]

---

**Status**: ✅ Strukturiert mit Stichpunkten aus README.md & TODO.md
**Basis**: Phase 1 + Phase 2 Research-Erkenntnisse
**Nächste Schritte**: Literaturrecherche Quellen 13-27, Detaillierung nach Implementation, Transformation zu .docx
