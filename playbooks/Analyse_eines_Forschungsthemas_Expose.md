# Exposé: Analyse eines Forschungsthemas - Prozesskommunikation

**Titel**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Autor**: Benjamin Probst
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Fakultät Informatik
**Datum**: Oktober 2025

---

## 1. Einleitung und Motivation

### 1.1 Ausgangssituation

Die industrielle Automatisierung steht vor der Herausforderung, heterogene Systeme mit unterschiedlichen Protokollen, Architekturen und Kommunikationsmustern zu integrieren. Im Rahmen der Forschungsarbeiten am Lehrstuhl für Industrielle Kommunikationstechnik der TU Dresden unter Prof. Dr.-Ing. habil. Martin Wollschlaeger wurde das Asset Administration Shell (AAS) Framework nach IEC 63278 als standardisierter Ansatz für digitale Zwillinge in der Industrie 4.0 entwickelt. Die von Dr. Santiago Soler Perez Olaya betreute aas-core-works Implementierung offenbart dabei eine vollständige Compiler-Architektur, die auf einer M3/M2/M1 Metamodell-Struktur basiert – analog zu den Ansätzen von Prof. Castrillon im Bereich Compiler-Design an der TU Dresden.

Die derzeitige Implementierung des AAS-Frameworks nutzt Python-Skripte, die Compiler-Funktionalität simulieren: Das aas-core-meta Repository definiert das M3-Metamodell in vereinfachtem Python, während aas-core-codegen daraus Zielsprachen-SDKs generiert (C++, C#, Python, TypeScript, Java, Golang). Trotz dieser funktionalen Code-Generierung fehlt eine vollständige Compiler-Implementierung als externes Übersetzerprogramm, das als eigenständiges, wartbares Tool in industriellen Produktionsumgebungen eingesetzt werden kann.

### 1.2 Vision: Industrie 5.0

Die nächste Generation industrieller Automatisierung – Industrie 5.0 – erfordert eine fundamentale Paradigmenverschiebung: Statt manueller Systemkonfiguration und -programmierung soll eine KI-gesteuerte Systembeschreibung ermöglicht werden, bei der Anwender ihr System natürlichsprachlich beschreiben. Das Zielsystem führt automatische Compilation und Deployment durch, wobei Software-in-the-Loop Verfahren iterative Fehlerkorrektur gegen die Kundenspezifikation ermöglichen. Das langfristige Ziel dieser Forschungsvision lautet: "Der Kunde beschreibt sein System der KI, die KI definiert eine Compiler-Beschreibung, der Compiler generiert das funktionsfähige System."

Diese Vision erfordert eine durchgängige Automatisierung vom abstrakten Metamodell bis zum deployed System auf heterogenen Edge-Geräten. VIA (Virtual Industry Automation) verfolgt diesen Ansatz durch eine mehrstufige Compiler-Kette (M3→M2→M1), die aus einem Metamodell zunächst ein SDK generiert (M3→M2), aus Kundenprojekten Systemprojekte erstellt (M2→M1) und diese schließlich auf über 50.000 Edge-Geräte verteilt deployed (M1-Deployment).

### 1.3 Forschungslücke

Trotz der vorhandenen Metamodell-Frameworks und Code-Generatoren existiert eine fundamentale Forschungslücke zwischen Metamodell-Definition und Production-Grade Compiler-Implementierung. Bisherige Ansätze wie aas-core-codegen erzeugen zwar lauffähigen Code, jedoch fehlt die Verbindung zum automatisierten Deployment: Es gibt keine wartbare, versionierte SDK-Generierung für industrielle Langzeitnutzung (typischerweise 15-25 Jahre in der Fertigungsindustrie), keine automatische Orchestrierung der generierten Systeme und keine Optimierung der Prozesskommunikation zur Compile-Zeit.

Die manuelle Orchestrierung von mehr als 50.000 Edge-Geräten in einer typischen Automobilfabrik ist praktisch unzumutbar und fehleranfällig. Zudem erfordern heterogene Zielarchitekturen (MIPS, RISC-V, POWER9, x86, ARM, Sparc) eine Multi-Target-Compilation, die in bisherigen AAS-Implementierungen nicht vorgesehen ist. Insbesondere fehlt eine wissenschaftliche Untersuchung, ob und wie Mikroservice-Kommunikation (IPC: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) zur Compile-Zeit optimiert werden kann, um Latenz und Ressourcenverbrauch gegenüber Runtime-Orchestrierung zu reduzieren.

---

## 2. Problemstellung und Forschungsfrage

### 2.1 Kontext: VIA-Gesamtsystem

VIA (Virtual Industry Automation) bildet den übergeordneten Kontext dieser Forschungsarbeit. Es handelt sich um eine mehrstufige Compiler-Kette (M3→M2→M1) für heterogene Industriesysteme mit automatischer Orchestrierung von mehr als 50.000 Edge-Devices. Das Gesamtsystem gliedert sich in drei Hauptkomponenten: Der **M3-Compiler** transformiert das AAS-Metamodell in ein sprachspezifisches SDK (C++, Python, Java), der **M2-SDK-Compiler** konvertiert Kundenprojekte unter Einbeziehung von Network Discovery in vollständige Systemprojekte, und der **M1-System-Deployer** führt Cross-Compilation, Horse-Rider-Deployment und Kubernetes-Orchestrierung durch.

Diese Architektur ermöglicht eine durchgängige Automatisierung von der abstrakten Systembeschreibung bis zum deployed System auf heterogenen Hardwareplattformen. Während das VIA-Gesamtsystem alle Aspekte von Metamodellierung bis Deployment abdeckt, fokussiert sich die vorliegende Forschungsarbeit auf einen spezifischen, kritischen Teilaspekt: die Optimierung der Prozesskommunikation zur Compile-Zeit.

### 2.2 Fokus dieser Forschungsarbeit: Process-Group-Protocol

Die zentrale Forschungsfrage dieser Arbeit lautet:

> **Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?**

Diese Frage adressiert eine fundamentale Herausforderung moderner Mikroservice-Architekturen: Die Wahl des Inter-Process Communication (IPC) Mechanismus erfolgt üblicherweise zur Laufzeit durch Service-Mesh-Lösungen wie Istio oder Linkerd. Diese Runtime-Entscheidungen verursachen jedoch Overhead durch dynamisches Routing, Service Discovery und Load Balancing. Die vorliegende Arbeit untersucht, ob durch Compile-Time-Analyse des Metamodells eine statische Optimierung möglich ist, die Latenz reduziert ohne Flexibilität signifikant einzuschränken.

Zur systematischen Bearbeitung dieser Forschungsfrage werden vier Teilfragen formuliert:

1. **Metamodell-Elemente**: Welche M3-Modellelemente sind notwendig, um Prozesskommunikation (Abhängigkeiten, Datenflüsse, Latenzanforderungen) zu beschreiben?

2. **IPC-Ableitung**: Wie kann der M2-SDK-Compiler aus Prozessabhängigkeiten optimale IPC-Mechanismen ableiten? Welche Heuristiken bestimmen, ob Pipe (gleicher Host, geringer Overhead), Unix Socket (gleicher Host, höhere Flexibilität), TCP (Remote, höchste Flexibilität), File-Queue (asynchron, persistent) oder Thread-Messaging (gleicher Prozess, geringste Latenz) gewählt wird?

3. **Positionierungsmetriken**: Welche Metriken bestimmen die Positionierung von Mikroservices (gleicher Container, gleicher Host, gleicher Cluster-Node, Remote)? Wie werden Latenzanforderungen, Ressourcenverfügbarkeit und Ausfallsicherheit gewichtet?

4. **Skalierbarkeit**: Wie verhält sich das Process-Group-Protocol unter OPC UA bei mehr als 50.000 Geräten? Kann hierarchische Gruppierung (Edge-Groups → Cluster-Groups → Global) lineares Skalierungsverhalten erreichen?

Zur Validierung der Forschungshypothese werden vier messbare Hypothesen aufgestellt:

- **H1 (Latenz)**: Compiler-basierte IPC-Optimierung reduziert Latenz um mindestens 30% gegenüber Runtime-Service-Mesh-Lösungen
- **H2 (Effizienz)**: Statische Positionierungsentscheidung zur Compile-Zeit erreicht mindestens 90% der Effizienz dynamischer Runtime-Orchestrierung
- **H3 (Skalierbarkeit)**: Das Process-Group-Protocol skaliert linear bis 100.000 Services bei hierarchischer Gruppierung
- **H4 (Entwicklungszeit)**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um mindestens 60%

**Abgrenzung**: Diese Arbeit konzentriert sich auf das **Process-Group-Protocol-Subsystem** als Teil des VIA-Gesamtsystems. Die M3/M2/M1-Architektur dient als Kontext und theoretischer Rahmen, wird jedoch nicht in allen Details implementiert. Insbesondere werden M3-Compiler-Optimierungen, Multi-Architektur-Cross-Compilation und das vollständige Horse-Rider-Deployment als gegeben vorausgesetzt und nicht eigenständig erforscht.

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

Die Forschungsarbeit baut auf mehreren etablierten Standards und Forschungsergebnissen auf, die im Folgenden systematisch dargestellt werden. Die Analyse umfasst AAS-Code-Generierung (Abschnitt 3.1), OPC UA als Kommunikationsprotokoll (Abschnitt 3.2), Multi-Message Broker für Brownfield-Integration (Abschnitt 3.3), Management-Frameworks (Abschnitt 3.4), Service-orientierte Architekturen (Abschnitt 3.5), Monitoring-Ansätze (Abschnitt 3.6) sowie theoretische Grundlagen wie ISA-95 und CMFM (Abschnitt 3.7).

### 3.1 Asset Administration Shell (AAS) - aas-core-works

Das aas-core-works Framework bildet den Ausgangspunkt für die metamodell-basierte Code-Generierung in VIA. Es implementiert den IEC 63278 Standard als M3/M2/M1 Metamodel Architecture für digitale Zwillinge und demonstriert, wie aus einem abstrakten Metamodell (aas-core-meta in simplified Python) produktionsreifer Code für sechs Zielsprachen generiert werden kann. Die Architektur folgt dem Single-Source-of-Truth Prinzip: Das M3-Metamodell wird einmal kanonisch definiert, der aas-core-codegen Compiler transformiert es automatisch in sprachspezifische SDKs mit identischer Semantik. Zentrale technische Eigenschaften:

- **IEC 63278 Standard**: M3/M2/M1 Metamodel Architecture für Digital Twins
- **aas-core-meta**: M3 Metamodel in simplified Python (canonical definition), versioned releases (YYYY.MM.DD)
- **aas-core-codegen**: Multi-Target Compiler, Single Source of Truth, automated generation, scalability
- **6 Language SDKs**: C++, C#, Python, TypeScript, Java, Golang (identical semantics)
- **5 Schema Exports**: JSON Schema, XSD, RDF SHACL, JSON-LD Context, Protobuf
- **Code Generation Pipeline**: Python M3 → Parser & Analyzer → Language SDKs + Schema Exports
- **Transformation Rules**: Python classes → Target language classes, Properties → Getters/setters, Constraints → Validation functions, Documentation → API docs
- **Constraint System**: Python `@invariant` decorators → Runtime Validation (Uniqueness, Multiplicity, Type Safety, Semantic Consistency)
- **Code Injection Points**: Custom constructors, Serialization/deserialization, Performance optimizations
- **Community**: 2.9K Stars, 307 Contributors, MPL 2.0 License
- Limitation: Python-Skripte (nicht C++ Production-Compiler), statisches Modell (keine Runtime Reconfiguration), AAS-spezifisch (keine Industrial Real-Time Constraints)

### 3.2 OPC UA (IEC 62541) & open62541 C99 Stack

OPC UA (Open Platform Communications Unified Architecture) nach IEC 62541 bildet das Kommunikations-Rückgrat für VIA. Als etablierter Standard in der industriellen Automatisierung bietet OPC UA eine M3/M2/M1-basierte Informationsmodellierung, die strukturell mit der VIA-Architektur kompatibel ist. Die open62541 Implementierung – ursprünglich ein TU Dresden Forschungsprojekt – liefert einen produktionsreifen C99-Stack mit minimalem Memory-Footprint (~250KB), der für Edge-Geräte geeignet ist. Besonders relevant für VIA ist die Dynamic Address Space API, die es ermöglicht, OPC UA Nodes zur Laufzeit zu erzeugen und zu löschen – eine Voraussetzung für die Abbildung dynamisch registrierender VIA-Prozesse. Zentrale Eigenschaften:

- **Client-Server Many-to-Many**: Mehrere Clients ↔ Mehrere Server, Discovery Mechanismen, Subscriptions
- **Informationsmodellierung (Herzstück)**: Beliebig komplexe Strukturen, eigene Objekttypen/Variablentypen, objektorientiert, dynamisch erweiterbar
- **M3/M2/M1 Architektur**: M3 (Metamodell: Objekte/Variablen/Methoden existieren), M2 (Modell: Domain-spezifische Typen), M1 (Instanz: Laufende Systeme)
- **ModelCompiler**: XML-Modellbeschreibung → C#/C Code, UA Modeler für grafisches Design
- **C++ SDKs**: OPC Foundation (ANSI C/C++), Unified Automation (kommerziell), open62541 (C99, ~250KB, Open Source)
- **open62541**: C99 Implementation, MPL 2.0, 2.9K Stars, 307 Contributors, ursprünglich TU Dresden Forschungsprojekt
  - **Embedded-Friendly**: ~250KB minimal config (Core + Namespace 0 MINIMAL), ~500KB full config, zertifiziert "Micro Embedded Device Server"
  - **Plugin-Architektur**: Logging, Crypto (OpenSSL/mbedTLS), Access Control (RBAC), NodeStore (HashMap/ZipTree)
  - **Platform Abstraction**: POSIX, Windows, Zephyr RTOS (freeRTOS legacy), portierbar auf neue Plattformen (clock, networking)
  - **Nodeset Compiler**: Python Tool (nodeset_compiler.py), XML NodeSet → C Code, Integration mit VIA-M3-Compiler
  - **Dynamic Address Space**: Nodes zur Laufzeit hinzufügen/löschen (VIA Registry ↔ OPC UA Nodes), `UA_Server_addObjectNode()` API
  - **Performance**: 10K ops/sec (single-thread), 50K ops/sec (multi-thread 4 cores), 100K nodes tested, 1K notifications/sec
  - **Security**: Basic256Sha256 (AES-256 + SHA256), X.509 Zertifikate, Encryption Policies
- **76+ Companion Specifications** (UA-Nodeset Repository): DI, I4AAS, PLCopen, Robotics, CNC, MTConnect, ISA-95, PackML, EUROMAP, BACnet
  - **DI (Device Integration)**: Generic device modeling, Base für VIA Custom Companion Spec (DeviceType, BlockType, ConfigurableObjectType)
  - **I4AAS Companion Spec**: Maps AAS to OPC UA (AssetAdministrationShell → UA Object, Submodel → UA Object, Property → UA Variable)
  - **VIA Custom Companion Spec** (Vision): VIAProcessType (extends DeviceType), VIARouterType, VIASchedulerType, VIARegistryType
- **NodeSet XML Format**: Standardisierte Information Models, `<UANodeSet>` root, `<UAObject>`, `<UAVariable>`, `<UAMethod>`, `<UAObjectType>`, `<UADataType>`
- **Hybrid Model für VIA**: Static NodeSet (VIA types) + Dynamic Instances (created at runtime when VIA processes register)
- **Aggregationsserver**: Sammelt Daten von vielen Servern in einheitlichem Adressraum
- **Multi-Language-Interoperabilität**: python-opcua, Java, .NET, gRPC-Bindings möglich
- **Code Generation Pipeline (VIA Integration)**:
  ```
  VIA M3 Metamodel → VIA-M3-Compiler → OPC UA NodeSet XML
                                        ↓
                               open62541 nodeset_compiler.py
                                        ↓
                                   C Code (via_nodeset.c/.h)
                                        ↓
                               Link mit VIA Process (C++23 Module)
  ```
- Limitation: Statische NodeSets (behoben durch Dynamic Address Space API), keine dynamische Orchestrierung, keine Compile-Time-Optimierung

### 3.3 Multi-Message Broker (Dr. Santiago Soler Perez Olaya et al., IEEE ETFA 2024)

Der Multi-Message Broker (MMB) adressiert die Herausforderung der Brownfield-Integration: Legacy-Geräte mit proprietären, inflexiblen Protokollen (Modbus, PROFIBUS, EtherCAT) müssen in moderne AAS-basierte Industrie 4.0-Systeme integriert werden. Der MMB fungiert als Gateway zwischen Northbound-Schnittstellen (I4.0 HTTP API, zukünftig Type 3 Proactive AAS) und Southbound-Protokollen (Modbus, HTTP, MQTT, zukünftig PROFIBUS/EtherCAT/PROFINET). Die Architektur demonstriert, wie heterogene Protokolle durch Mapping-Submodelle (AID/AIMC) systematisch in ein einheitliches AAS-Datenmodell überführt werden können – ein Ansatz, den VIA für die automatische Generierung von Protocol-Adaptern nutzt. Zentrale Eigenschaften:

- **Problem**: Brownfield Integration (Legacy Devices mit inflexiblen Protokollen)
- **MMB als Gateway**: Northbound (I4.0 HTTP API, zukünftig Type 3 Proactive AAS) ↔ Southbound (Modbus, HTTP, MQTT, zukünftig PROFIBUS/EtherCAT/PROFINET)
- **Internal Layers**: Consistency Layer (identische Requests → gleiche Info), Mapping Layer (Connector-Auswahl + Data Transformation), AAS Storage (ein AAS pro Legacy Asset)
- **AID/AIMC Submodels**:
  - **AID (Asset Interfaces Description)**: Von Vendor, Available Endpoints, basiert auf W3C WoT TD
  - **AIMC (Asset Interfaces Mapping Configuration)**: Von User, bidirectional Mapping Asset ↔ AAS SubmodelElements
- **Sync/Async Translation**: Buffer latest status ODER block until response available
- **AAS Interaction Types**: Type 1 (Passive: XML/JSON/RDF), Type 2 (Reactive: HTTP API), Type 3 (Proactive: autonomous inter-AAS, Zukunft)
- **Real-time vs Non-real-time**: Gateway zwischen Hard/Soft Real-time (Fieldbus) und Non-real-time (HTTP)
- **Protokoll-Translation**: Controller/Peripheral ↔ Client/Server ↔ Pub/Sub
- Limitation: AIMC erlaubt keine Data Transformations, Type 3 noch nicht standardisiert, kein vollautomatisches Deployment

### 3.4 CMFM & Management Paradigmen

Das Comprehensive Management Function Model (CMFM) bietet einen theoretischen Rahmen für Human-Centered Management in heterogenen industriellen Netzwerken ("Network of Networks"). Anders als System-Centric Ansätze (SNMP Value-based, SDN Requirements-based) fokussiert CMFM auf Intent-basiertes Management: Anwender beschreiben Ziele (Goals) und gewünschte Ausgaben (Outputs), das System leitet automatisch notwendige Konfigurationen ab. VIA adaptiert die CMFM-Philosophie für die Prozesskommunikation: Das M3-Metamodell definiert ein VIA-Vocabulary (Elements: Process, Service, Registry; Verbs: register, discover, route; IPC Types: Pipe, Socket, TCP, FileQueue, Thread), aus dem der M2-Compiler automatisch Orchestrierungslogik generiert. Zentrale Konzepte:

- **CMFM**: Human-Centered vs. System-Centric Management
- **Management Paradigmen**: Value-based (SNMP), Policy-based (Intent), Requirements-based (SDN/TSN), Ontology-based (Semantic)
- **CMFM Stärken**: Heterogeneity Management, Intent-based, Knowledge Transfer
- **CMFM Meta-Model**: Goal (mandatory), Output (mandatory), Input (optional), Constraints (optional), Representation (optional)
- **Constraints-Typen**: Time, Order, Existence, Mutual Exclusiveness, Execution Success
- **Taxonomy**: Hierarchische Composition, Multiple Super-CMFMs möglich
- **VIA Vocabulary**: Elements (Process, Service, Registry, Scheduler, Router), Verbs (register, discover, route, schedule), IPC Types (Pipe, Socket, TCP, FileQueue, Thread)
- **Data/Control/Management Plane**: IPC (Data), Orchestration (Control), CMFM (Management) - Separation besser als Legacy Industrial Systems
- **Network of Networks**: VIA als holistic Management für heterogene IPC-Mechanismen (Pipe, Socket, TCP, FileQueue, Thread)
- **Seamless Integration**: Access to different management systems, orchestration throughout
- **Legacy Problem**: Keine Trennung Data/Control/Management in Industrial Systems, proprietary Interfaces, statische Configuration
- Limitation: Keine Compiler-Kette, manuelle CMFM-Erstellung, Vocabulary Management yet-to-standardize

### 3.5 SOA & Microservice Architecture (Dr. Santiago Soler Perez Olaya et al., IECON 2024)

Service-orientierte Architekturen (SOA) und Microservices bilden die strukturelle Grundlage für VIA-Prozesse. Die Forschungsarbeit von Dr. Soler Perez Olaya demonstriert, wie AAS-Submodels als eigenständige Microservices implementiert werden können, die über gRPC+Protobuf kommunizieren. Besonders relevant ist die beschriebene Code-Generation-Pipeline: OpenAPI-Spezifikationen (AAS Spec) werden in Protobuf-Definitionen transformiert, aus denen der protoc-Compiler sprachspezifischen Code generiert. VIA erweitert diesen Ansatz um eine zusätzliche Abstraktionsebene (M3-Metamodell) und automatische IPC-Optimierung. Zentrale Erkenntnisse:

- **SOA Prinzipien**: Modularity, Abstraction, Loose Coupling, Service Composition, Reusability
- **Automotive SOA**: SOME/IP (Autosar), DDS (Publish/Subscribe), OPC UA (Interoperabilität)
- **Microservice Network für AAS**: One microservice per Submodel, Northbound (HTTP API) ↔ Internal (gRPC) ↔ Southbound (Asset Protocol)
- **gRPC + Protobuf Vorteile**: High-performance, low-latency, HTTP/2 multiplexing, language interoperability (C++, C#, Python, Java, Go), binary serialization (compact, efficient), backward/forward compatibility, contract-first paradigm
- **Code Generation Pipeline**: OpenAPI (AAS Spec) → Protobuf (.proto files) → protoc → Language-specific Code (messages, service stubs)
- **AAS SDK Integration**: aas-core-csharp für (de-)serialization, metamodel types
- **Container Deployment**: Docker + Kubernetes, transparent relocation (services near workload/gateway)
- **Limitation**: Protobuf kein Inheritance (resort to composition), duality Protobuf-generated vs AAS Core SDK classes, heterogene Protokolle nicht unified, manuelle Orchestrierung

### 3.6 IPC, Monitoring & Service Mesh (Related Work)

Die Wahl des IPC-Mechanismus hat fundamentalen Einfluss auf Latenz und Skalierbarkeit verteilter Systeme. Bestehende Lösungen wie gRPC (~0.5ms Latenz, aber keine Service Discovery), UNIX Domain Sockets (~20μs, nur lokal), DDS (Real-Time QoS, ~2ms Overhead) und Service-Mesh-Lösungen wie Istio/Linkerd (Runtime-Routing, 5-10ms Sidecar-Overhead) erfordern manuelle Konfiguration und bieten keine Compile-Time-Optimierung. Für Monitoring existieren etablierte Standards (SNMP für Infrastruktur, OPC UA für Prozessdaten, MQTT für Cloud-Anbindung), jedoch fehlt eine integrierte Sicht. VIA adressiert diese Fragmentierung durch eine Compiler-gestützte Vereinheitlichung: Der M2-Compiler wählt automatisch den optimalen IPC-Mechanismus basierend auf Prozess-Lokalisierung (gleicher Host → Pipe/Socket, Remote → TCP/gRPC) und Latenzanforderungen. Übersicht bestehender Ansätze:

- **gRPC**: HTTP/2, Protobuf, ~0.5ms Latenz (Single-Host), Service Discovery fehlt
- **ZeroMQ**: Message Queues, 5 Patterns (REQ/REP, PUB/SUB), keine Compiler-Integration
- **DDS (OMG Data Distribution Service)**: Real-Time, QoS-Policies, Overhead ~2ms, keine Metamodell-Abstraktion
- **Istio/Linkerd (Service Mesh)**: Runtime-Routing, Dynamic Discovery, Sidecar-Overhead 5-10ms
- **UNIX Domain Sockets**: ~20μs Latenz, nur lokale Prozesse, keine verteilte Orchestrierung
- **SNMP (Simple Network Management Protocol)**: Manager-Agent-Model, Polling (GET-Anfragen alle 60s) + Traps (Push bei Ereignissen), MIB-OID-Struktur (hierarchisch), Standard-MIBs (IF-MIB, HOST-RESOURCES-MIB, ENTITY-SENSOR-MIB), Grenzen: flache OID-Liste (keine Objekthierarchien), Polling-Paradigma (keine Pub/Sub), primär Monitoring (nicht Steuerung), Skalierungslimit bei 1000en Geräten
- **MQTT (Message Queuing Telemetry Transport)**: Pub/Sub, Broker-basiert, IoT-Sensorik, Cloud-Anbindung, extrem schlank (bandbreite-kritisch)
- **Hybrid-Ansatz (Empfohlen)**: SNMP (Infrastruktur-Monitoring), OPC UA (detaillierte Prozessdaten), MQTT (Cloud Analytics)
- **Limitation**: Alle Ansätze erfordern manuelle Konfiguration, keine Compile-Time-Optimierung, keine unified heterogene Protokolle

### 3.7 Forschungslücken

Die Analyse des Stands der Forschung offenbart mehrere fundamentale Lücken, die diese Arbeit adressiert:

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

### 5.4 OPC UA Information Model & ISA-95 Integration
- **M3-basierte Typdefinitionen**: Metamodell für Objekte, Variablen, Methoden
- **Companion Specifications**: Domain-Erweiterungen (DI, I4AAS, PLCopen)
- **Address Space**: Hierarchische Nodes, objektorientiert
- **ISA-95 Levels**: Level 2 (SCADA: Prozessebene, Echtzeit), Level 3 (MES: Produktionsleitebene), Level 4 (ERP: Unternehmensebene)
- **SCADA**: Prozessdaten erfassen, Steuerbefehle senden, Alarmierung, Historisierung, Visualisierung (HMI)
- **MES**: Produktionsaufträge, Feinplanung, Qualitätssicherung, OEE/KPI, Rückverfolgung, bidirektional mit SCADA
- **OPC UA als Vermittler**: Standardisierter Zugriff für SCADA, MES, ERP, Cloud

### 5.5 Prozesskommunikation
- IPC Mechanisms: Pipe, Socket, TCP, File-Queue, Thread
- Data vs. Control vs. Management Plane
- gRPC + Protobuf: Contract-First, Binary Serialization

### 5.6 CMFM (Comprehensive Management Function Model)
- **Manager-Centric Paradigm**: Fokus auf Ziele statt System-Details (vs. System-Centric)
- **CMF Komponenten**: Goal (mandatory), Output (mandatory), Input (optional), Constraints (optional), Representations (optional)
- **Generality Hierarchy**: Implementation → User → Domain → Parent Domain
- **VIA as Domain**: Gesamte Prozesskommunikations-Domain
- **Catalog vs. Core**: Liste aller CMFs vs. allgemein anwendbare CMFs nach Promotion
- **Promotion**: Tacit (automatisch durch häufige Nutzung) vs. Explicit (durch Standardization Bodies)
- **CMF Interrelations**: Equivalence (Merge gleicher Goals), Composition (Upwards/Downwards)
- **AAS Integration**: CMFs als Operations im AAS Meta-Model, Input/Output als Attributes
- **VIA CMFs**: process-register, process-discover, route-message, schedule-task
- **Vocabulary Management**: Öffentliches Repository, Verknüpfung mit e-Class, CDD, I4.0 SemanticID

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
