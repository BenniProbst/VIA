# Research Step 1 - Zusammenfassung: Uni-Dokumente

## Status: ✅ ABGESCHLOSSEN
Datum: 2025-10-22

## Gelesene Dokumente

### 1. Forschungsantrag Prozesskommunikation (doc1)
**Quelle**: 20251015 Antrag_Aufgabenstellung_AnalyseForschungsthema_Probst.docx
**Bearbeiter**: Benjamin-Elias Probst, TU Dresden
**Betreuung**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert

**Thema**: Entwicklung eines Interfacekommunizierenden prozesskommunikationsgestützten Messagesystems

**Kernziele**:
- Einheitliches C++ Kommunikations-Interface für: Pipe, Unix Domain Socket, TCP, File-Queue, Thread-Messaging über Round Robin Memory Streams
- Service-Registry + Orchestrierung für Kubernetes
- Aufgabenverwaltung + Scheduling mit Session Management Traffic Router
- Telemetrie mit Witness/Arbiter
- Benchmarks: Latenz, Jitter, Payload, Response Time, Job Complexity Hops
- 90% Projektcoverage mit Unit-Tests und Chaos Tests

**Vergleich**: Small-Messages, Burst, Crash-Recovery Orchestration, Tracing

---

### 2. SOA Communication Management in Automotive (doc3)
**Quelle**: d1-02.docx (IEEE SA Ethernet & IP @ Automotive Technology Day 2021)
**Autoren**: Trista Lin, David Fernandez Blanco, Juleixis Guariguata

**Hauptthemen**:
- **SOA Evolution**: Von Signal zu Service, Hardware-defined → Software-defined
- **Treiber**: Elektrifizierung, Autonomous Driving, Connectivity, Shared Mobility
- **Protokolle**: SOME/IP (Automotive), DDS (Data-centric), OPC UA (Interoperabilität)

**Control Plane Services**:
- Orchestration, Task Assignment, Network Supervision, Error Handling
- Dynamic Reconfiguration, SOTA/FOTA/AOTA, Lifecycle Management

**Herausforderungen**:
- Heterogenität (Classic/Adaptive Autosar, Linux, Android)
- Dynamik (Stateful/Stateless Services)
- Latenz (Real-time)
- RAMS & Security

**Trend**: Data-Centric (Topic-based, Named Data, Apps kurzlebig)

---

### 3. CMFM Generality & Workflow (doc5)
**Quelle**: Santiago Soler Perez Olaya, Martin Wollschlaeger (TU Dresden, IEEE 2022 INDIN)

**Kernkonzept**: Comprehensive Management Function Model (CMFM)

**Manager-Centric Paradigm**:
- Problem: System-centric Management spiegelt Komplexität
- Lösung: Manager-centric fokussiert auf Ziele

**CMF Komponenten**:
- **Mandatory**: Goal, Output
- **Optional**: Input, Constraints, Representations

**Generality-Konzept** (NEU):
1. **Implementation**: Spezifisch für eine Implementierung
2. **User**: Für einen User über mehrere Implementierungen
3. **Domain**: Für eine ganze Wissensdomäne

**Workflow**:
- **Catalog**: Liste aller CMFs
- **Core**: Allgemein anwendbare CMFs nach Promotion
- **Vocabulary**: Öffentliches Repository (wie GitHub)
- **Tacit Promotion**: Automatisch durch häufige Nutzung
- **Explicit Promotion**: Durch Standardization Bodies

**Evaluation**: CMFM = Compromise zwischen Open Source (Flexibilität, schnell) und Standardization (Reliability, Coverage)

**AAS Integration**: CMFs als Operations im Asset Administration Shell

---

### 4. CMFM Applied to HetIndNets (doc6)
**Quelle**: Santiago Soler Perez Olaya, Robert Lehmann, Martin Wollschlaeger (TU Dresden, IEEE 2019 INDIN)

**Management Paradigmen**:
1. **Value-based**: get/set (z.B. SNMP) → Monitoring
2. **Policy-based**: Intent-oriented, Policies enforcement
3. **Requirements-based**: SLA, Top-Down (SDN, NFV, TSN)
4. **Ontology-based**: Semantic Technologies (akademisch, praktisch selten)

**CMFM = Human-Centered**:
- Formalisierung von Manager-Wissen
- Wissenstransfer zwischen Generationen/Teams
- Abstraction Layer zwischen heterogenem Netzwerk und Manager

**Meta-Model Details**:
- **Taxonomy**: Hierarchische Struktur (Composition)
- **Constraints**: Time, Order, Existence, Mutual Exclusiveness, Execution Success
- **Vocabulary**: Semantic-validated expressions (Iteratives Wachstum)

**Use-Case**: PROFIBUS + IIoT + TCP/IP
- 3 Management Systems: SNMP (TCP/IP), OMA-DM (IIoT), Fieldbus Management (PROFIBUS)
- Beispiel CMF: `enforceConfig` mit 5 Representations

**Evaluation**: CMFM übertrifft SNMP/NETCONF/WBEM in Heterogeneity, Intent, Human-centric

**Roadmap**: Smooth Transition von aktuellen Scripts zu vollautomatischer Management

---

## Relevanz für VIA-Projekt

### 1. Direkte Verbindungen
| VIA Komponente | Uni-Forschung Quelle |
|----------------|----------------------|
| C++ IPC Interface | Forschungsantrag: Pipe/Socket/TCP/FileQueue/Thread |
| Service Registry | Forschungsantrag + doc3 Control Plane |
| Orchestration | doc3 Control Plane Services |
| Scheduling | Forschungsantrag Task Assignment |
| Telemetrie | Forschungsantrag + doc3 Network Monitoring |
| CMFM Integration | doc5+6: VIA als Domain, Services als CMFs |

### 2. VIA als CMFM Domain
- **M3**: CMFM Meta-Model (Generality Hierarchy)
- **M2**: VIA-spezifische CMFs (SDK)
- **M1**: System-spezifische Representations

### 3. VIA-spezifische CMFs
- `registerProcess`, `discoverService`, `routeMessage`, `scheduleTask`, `healthMonitor`

### 4. VIA Vocabulary
- **Elements**: Process, Service, Registry, Scheduler, Router, Message, Task, Session, Cluster
- **Verbs**: register, discover, route, schedule, monitor, connect, disconnect
- **IPC Types**: Pipe, UnixSocket, TCP, FileQueue, ThreadMessaging, RoundRobinMemoryStream

### 5. Control Plane Architektur
VIA übernimmt Control Plane Konzept:
- **Data Plane**: IPC Mechanisms
- **Control Plane**: Registry, Orchestration, Scheduling
- **Management Plane**: CMFM für holistic Management

### 6. Industry 4.0 / AAS Anbindung
- VIA Processes als AAS Assets
- VIA CMFs als AAS Operations
- VIA Semantic Model als AAS Submodel

---

## Nächste Schritte (Research Step 2)

Jetzt vollständig lesen:
1. AAS Repository (aas-core-works): M3 Metamodell, Python SDK, C++ SDK, Code-Generator
2. OPC UA Repositories: UA-Nodeset + open62541
3. Weitere Santiago Papers falls vorhanden im Uni-Ordner

Dann:
4. Research Playbooks erstellen (strukturierte Zusammenfassung)
5. Output Playbooks für VIA-Implementation

---

## Dateien angelegt
- `doc1_20251015_antrag.txt` (27 Absätze)
- `doc3_d1-02.txt` (475 Absätze)
- `doc5_cmfm_1.txt` (563 Zeilen, 6 Seiten)
- `doc6_cmfm_2.txt` (360 Zeilen, 6 Seiten)
- `research_doc3_erkenntnisse.md`
- `research_doc5_erkenntnisse.md`
- `research_doc6_erkenntnisse.md`
- `research_step1_progress.md`
- `research_step1_zusammenfassung.md` (diese Datei)
