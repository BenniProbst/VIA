# PHASE 1: Research & Dokumentenanalyse - ABGESCHLOSSEN

**Zeitraum**: 2025-10-22
**Status**: ✅ VOLLSTÄNDIG ABGESCHLOSSEN
**Token-Verbrauch**: 114K/200K (57%)

---

## Überblick

Phase 1 umfasste die vollständige Analyse aller relevanten Forschungsdokumente aus dem Uni-Ordner und ChatGPT-Ordner. Ziel war es, ein umfassendes Verständnis der theoretischen Grundlagen für das VIA-Projekt zu entwickeln.

---

## Was wurde erreicht

### 📚 Dokumente vollständig gelesen: 11/12 (91.7%)

**Gruppe 1: Forschungsantrag + SOA (2 Docs)**
- ✅ doc1_20251015_antrag.txt (27 Absätze)
- ✅ doc3_d1-02.txt (475 Absätze)

**Gruppe 2: CMFM Santiago Papers (5 Docs)**
- ✅ doc5_cmfm_1.txt - CMFM Generality & Workflow (2022, 6 Seiten)
- ✅ doc6_cmfm_2.txt - CMFM Applied to HetIndNets (2019, 6 Seiten)
- ✅ doc_santiago_7.txt - Multi-Message Broker (2024, 8 Seiten)
- ✅ doc_santiago_8.txt - SOA for I4.0 Digital Twins (2024, 6 Seiten)
- ✅ doc_santiago_9.txt - Role of CMFM (2019, 4 Seiten)

**Gruppe 3: OPC UA + SCADA/MES + SNMP (4 Docs)**
- ✅ doc_chatgpt_1.txt - OPC UA Funktionsweise (7 Seiten)
- ✅ doc_chatgpt_2.txt - SCADA/MES/OPC UA/SNMP Basics (6 Seiten)
- ✅ doc_chatgpt_3.txt - SNMP in Industrie 4.0 (10 Seiten)
- ✅ doc_chatgpt_4.txt - SNMP MIB Objekte (7 Seiten)

**Nicht gelesen (explizit niedrige Priorität)**
- ❌ 5G Papers (2 Docs) - Benjamin: "vielleicht nicht ganz so wichtig"

### 📝 Erkenntnisse-Dateien erstellt: 10

1. **research_doc3_erkenntnisse.md** - SOA Communication Management
2. **research_doc5_erkenntnisse.md** - CMFM Generality & Workflow
3. **research_doc6_erkenntnisse.md** - CMFM Applied to HetIndNets
4. **research_doc_opcua_1_erkenntnisse.md** - OPC UA Funktionsweise
5. **research_doc_scada_mes_erkenntnisse.md** - SCADA/MES/OPC UA/SNMP
6. **research_santiago_7_mmb_erkenntnisse.md** - Multi-Message Broker
7. **research_santiago_8_soa_erkenntnisse.md** - SOA for I4.0 Digital Twins
8. **research_santiago_9_cmfm_role_erkenntnisse.md** - Role of CMFM
9. **research_snmp_complete_erkenntnisse.md** - SNMP vollständig
10. **research_step1_zusammenfassung.md** - Erste 4 Docs Überblick

### 📊 Meta-Dokumentation: 6 Dateien

1. **research_step1_progress.md** - Fortschrittstracking während Arbeit
2. **research_memory_reconstruction.md** - Benjamins Anfragen rekonstruiert
3. **research_step1_remaining_docs.md** - Liste fehlender Dokumente
4. **research_step1_final_status.md** - Status nach erstem Durchlauf
5. **research_current_memory_state.md** - Live Snapshot
6. **research_papers_complete_status.md** - Status nach Option A
7. **research_FINAL_status.md** - Finaler Abschlussstatus
8. **PHASE1_SUMMARY.md** - Diese Zusammenfassung

---

## Kernerkenntnisse

### 1. VIA = Multi-Message Broker (MMB)
**Quelle**: Santiago et al. 2024

**Architektur**:
- **Northbound**: I4.0 Interface (OPC UA HTTP API)
- **Southbound**: Legacy Assets (Multi-Protocol: Pipe, Socket, TCP, FileQueue, Thread)
- **Internal Layers**: Consistency Layer, Mapping Layer, AAS Storage

**AID/AIMC Submodels**:
- **AID**: Asset Interfaces Description (von Vendor)
- **AIMC**: Asset Interfaces Mapping Configuration (von User)
- Bidirectional Mapping zwischen Asset und AAS

**Sync/Async Translation**:
- Buffer latest asset status ODER
- Block until response available

**VIA Mapping**:
- VIA Processes = Legacy Assets (Brownfield)
- VIA Registry = AAS Storage
- VIA IPC Mechanisms = Southbound Protocols
- VIA OPC UA API = Northbound Interface

### 2. VIA = Microservice Network (gRPC + Protobuf)
**Quelle**: Santiago et al. 2024

**Technologie-Stack**:
- **gRPC**: High-performance RPC, HTTP/2 multiplexing
- **Protobuf**: Binary serialization, contract-first, backward-compatible
- **Code Generation**: OpenAPI → Protobuf → C++/Python/Java/C#
- **Container**: Docker + Kubernetes deployment

**Architektur**:
- **One Microservice per Submodel** → **One per VIA Process**
- **Transparent Relocation**: Services können near asset deployed werden
- **Loose Coupling**: gRPC channels, language-agnostic

**AAS Core SDK**:
- Metamodel types, (de-)serialization
- C# Implementation: aas-core-csharp
- **VIA Analog**: via-core-cpp (zu entwickeln)

**VIA Mapping**:
- VIA Services = Microservices
- gRPC Communication = VIA Internal Network
- HTTP Northbound = OPC UA API für external
- Protobuf Definitions = VIA Interface Definitions

### 3. VIA = CMFM Domain
**Quellen**: Santiago Olaya 2019-2022

**CMFM Evolution Timeline**:
- **2019 (früh)**: Human-Centered Abstraction, Network of Networks
- **2019 (HetIndNets)**: Meta-Model, Taxonomy, Constraints, Use-Case
- **2022 (Generality)**: Generality Hierarchy, Catalog vs Core, Vocabulary Management
- **2024 (MMB)**: Implementation mit AID/AIMC Submodels

**Generality Hierarchy**:
- **Implementation**: Spezifisch für eine Implementation
- **User**: Für einen User über mehrere Implementations
- **Domain**: Für eine ganze Wissensdomäne
→ **VIA = Domain** im CMFM Sinne

**Promotion Mechanism**:
- **Catalog**: Liste aller CMFs
- **Core**: Allgemein anwendbare CMFs nach Promotion
- **Tacit**: Automatisch durch häufige Nutzung
- **Explicit**: Durch Standardization Bodies

**VIA CMFs**:
- `registerProcess`, `discoverService`, `routeMessage`, `scheduleTask`, `healthMonitor`

**VIA Vocabulary**:
- **Elements**: Process, Service, Registry, Scheduler, Router, Message, Task, Session
- **Verbs**: register, discover, route, schedule, monitor, connect, disconnect
- **IPC Types**: Pipe, Socket, TCP, FileQueue, Thread, RoundRobinMemoryStream

### 4. Control Plane Architecture
**Quelle**: SOA Communication Management (Automotive)

**Drei Ebenen** (besser als Legacy Industrial):
- **Data Plane**: IPC Mechanisms (actual message payloads)
- **Control Plane**: Registry, Orchestration, Scheduling, Router
- **Management Plane**: CMFM-based holistic Management

**Legacy Problem**: Keine Trennung Data/Control/Management
**VIA Lösung**: Klare Separation → bessere Flexibility

### 5. ISA-95 Levels Integration
**Quelle**: SCADA/MES Dokument

**VIA Mapping zu ISA-95**:
- **Level 2 (SCADA)**: VIA Core - Prozessebene, Echtzeit-Prozessführung
- **Level 3 (MES)**: VIA Orchestrator - Produktionsleitebene
- **OPC UA**: Vermittler zwischen Levels

**SCADA vs MES**:
- SCADA: Prozessnah, laufender Betrieb, Messwerte, Aggregate steuern
- MES: Produktionsnah, Auftrags-/Qualitätsaspekte, Optimierung

### 6. OPC UA M3/M2/M1 Architecture
**Quelle**: OPC UA Funktionsweise

**Drei Ebenen**:
- **M3 (Metamodell)**: OPC UA Basisebene (Objects, Variables, Methods existieren)
- **M2 (Modell)**: VIA-spezifische Typen, Companion Specification
- **M1 (Instanz)**: Laufende VIA-Instanzen, Live-Daten

**VIA Address Space Design**:
```
VIA Root
├── ProcessRegistry (Object)
│   ├── RegisteredProcesses[] (List)
│   ├── RegisterProcess() (Method)
│   └── DiscoverProcess() (Method)
├── Scheduler (Object)
│   ├── TaskQueue[] (List)
│   ├── ScheduleTask() (Method)
│   └── GetTaskStatus() (Method)
└── Router (Object)
    ├── RouteTable[] (List)
    ├── RouteMessage() (Method)
    └── UpdateRoute() (Method)
```

**VIA Companion Specification**: Eigene OPC UA Spec für VIA Domain

### 7. Hybrid Monitoring Strategy (SNMP + OPC UA + MQTT)
**Quellen**: SNMP + SCADA/MES Dokumente

**SNMP** (Lightweight, Infrastructure):
- VIA Processes als SNMP Agents
- Custom VIA-MIB: viaProcessStatus, viaTaskQueueLength, viaMessageRate, viaIPCLatency
- Traps: viaProcessCrashTrap, viaSchedulerOverloadTrap, viaRouterCongestionTrap
- SNMPv3 authPriv für Security (SHA-256 + AES-128)
- Manager-Agent Model: VIA Registry als SNMP Manager

**OPC UA** (Rich, Semantisch):
- Detaillierte Process Data mit Kontext
- Address Space mit VIA Services
- Subscriptions für Echtzeit-Updates
- Methodenaufrufe (RegisterProcess, ScheduleTask, etc.)

**MQTT** (Cloud, Skalierbar):
- Aggregierte Telemetrie an Cloud
- Pub/Sub für Big Data Analytics
- Prometheus SNMP Exporter + Grafana Integration

**Empfehlung**: Alle 3 parallel nutzen (Hybrid-Ansatz)

---

## Statistik

**Gesamtseiten gelesen**: ~67 Seiten
**Gesamtzeilen verarbeitet**: ~3800 Zeilen
**Token verbraucht**: 114K/200K (57%)
**Arbeitszeit**: ~1 Session
**Durchsatz**: ~0.6 Seiten pro 1K Tokens (effizient durch Kompaktheit)

---

## Nächste Phase: Repository-Analyse

### PHASE 2: GitHub Repositories analysieren

**Zu analysierende Repositories**:
1. **open62541** (https://github.com/open62541/open62541)
   - C99 OPC UA Implementation
   - Architektur, API, Beispiele, Integration

2. **UA-Nodeset** (https://github.com/OPCFoundation/UA-Nodeset)
   - Standard NodeSets
   - Companion Specifications
   - AAS NodeSet

3. **aas-core-works** (https://github.com/aas-core-works)
   - AAS Metamodell M3
   - Python SDK Implementation
   - C++ SDK Specifications
   - Code-Generator

**Geschätzter Token-Bedarf**: 150-240K (50-80K pro Repo)
**Empfehlung**: Frischer Token-Reset vor Start

### PHASE 3: Research Playbooks erstellen

Nach Repository-Analyse:
1. **OPC UA Research Playbook** - Synthese aller OPC UA Erkenntnisse
2. **AAS Research Playbook** - AAS Metamodell, Integration
3. **CMFM Research Playbook** - Alle Santiago Papers synthetisiert
4. **Prozesskommunikation Research Playbook** - Forschungsantrag

### PHASE 4: VIA M3 Mapping

1. **VIA ↔ OPC UA M3 Mapping** - Konkrete Typdefinitionen
2. **VIA Address Space vollständig** - Alle Nodes definiert
3. **VIA Companion Specification Draft**

### PHASE 5: Output Playbooks

1. **Main_System_playbook_DAY01.md**
2. **VIA-M3-Compiler/implementation/M3_implementation_playbook_DAY01.md**
3. **VIA-M2-SDK/implementation/M2_implementation_playbook_DAY01.md**
4. **VIA-M1-System-Deploy/implementation/M1_implementation_playbook_DAY01.md**
5. Entsprechende Tests-Playbooks

### PHASE 6: Dokumentation

1. **Exposé nach CELM-Vorlage** (unter docs/)
2. **Antrag auf 1 Seite aktualisieren** (Stichpunkte für Projektanmeldung)

---

## Ordnerstruktur Phase 1

```
playbooks/
├── phase1_research/
│   ├── PHASE1_SUMMARY.md (diese Datei)
│   ├── research_FINAL_status.md
│   ├── research_papers_complete_status.md
│   ├── research_current_memory_state.md
│   ├── research_memory_reconstruction.md
│   ├── research_step1_progress.md
│   ├── research_step1_remaining_docs.md
│   ├── research_step1_final_status.md
│   ├── research_step1_zusammenfassung.md
│   ├── research_doc3_erkenntnisse.md
│   ├── research_doc5_erkenntnisse.md
│   ├── research_doc6_erkenntnisse.md
│   ├── research_doc_opcua_1_erkenntnisse.md
│   ├── research_doc_scada_mes_erkenntnisse.md
│   ├── research_santiago_7_mmb_erkenntnisse.md
│   ├── research_santiago_8_soa_erkenntnisse.md
│   ├── research_santiago_9_cmfm_role_erkenntnisse.md
│   ├── research_snmp_complete_erkenntnisse.md
│   ├── doc1_20251015_antrag.txt
│   ├── doc3_d1-02.txt
│   ├── doc5_cmfm_1.txt
│   ├── doc6_cmfm_2.txt
│   ├── doc_santiago_7.txt
│   ├── doc_santiago_8.txt
│   ├── doc_santiago_9.txt
│   ├── doc_chatgpt_1.txt
│   ├── doc_chatgpt_2.txt
│   ├── doc_chatgpt_3.txt
│   └── doc_chatgpt_4.txt
└── TODO.md (aktualisiert)
```

---

## Lessons Learned

1. **Vollständigkeit zahlt sich aus**: Keine head-Limits, alle Dokumente komplett gelesen
2. **CMFM Evolution verstehen**: Timeline 2019→2024 gibt klares Bild
3. **Externe Dateien für Speicher**: Memory State in Dateien auslagern spart Tokens
4. **Kompakte Erkenntnisse**: Fokus auf VIA-Relevanz, nicht redundante Volltext-Wiederholung
5. **Hybrid-Ansatz erkennen**: SNMP + OPC UA + MQTT Kombination optimal
6. **Santiago Papers zentral**: 5 Papers bilden theoretisches Fundament für VIA

---

## Erfolgs-Metriken ✅

✅ **ALLE relevanten Dokumente vollständig gelesen** (keine Abstriche!)
✅ **CMFM Evolution vollständig verstanden** (2019→2024 Timeline)
✅ **3 Haupterkenntnisse klar synthetisiert** (MMB, gRPC/Protobuf, CMFM)
✅ **Hybrid Monitoring-Strategie erarbeitet** (3-Protokoll-Ansatz)
✅ **VIA Mappings zu allen Frameworks dokumentiert**
✅ **Token-Management erfolgreich** (57% für 67 Seiten = effizient)
✅ **Speicher sauber ausgelagert** (10 Erkenntnisse + 8 Meta-Docs)

---

## Status: PHASE 1 ABGESCHLOSSEN ✅

**Bereit für**: PHASE 2 (Repository-Analyse mit frischen Tokens)
