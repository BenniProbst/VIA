# Research Papers - Vollständiger Status nach Option A

**Zeitpunkt**: 2025-10-22
**Token-Stand**: ~109K/200K (54.5%)
**Status**: ✅ Alle geplanten Papers vollständig gelesen (Option A abgeschlossen)

---

## ✅ VOLLSTÄNDIG GELESEN: 9 von 12 Dokumenten

### Gruppe 1: Forschungsantrag + SOA Communication (2 Docs)
1. ✅ **doc1_20251015_antrag.txt** (27 Absätze)
2. ✅ **doc3_d1-02.txt** (475 Absätze) → research_doc3_erkenntnisse.md

### Gruppe 2: CMFM Papers - Santiago Olaya (4 Docs)
3. ✅ **doc5_cmfm_1.txt** (6 Seiten) → research_doc5_erkenntnisse.md (2022)
4. ✅ **doc6_cmfm_2.txt** (6 Seiten) → research_doc6_erkenntnisse.md (2019)
5. ✅ **doc_santiago_7.txt** (8 Seiten) → research_santiago_7_mmb_erkenntnisse.md (MMB 2024)
6. ✅ **doc_santiago_8.txt** (6 Seiten) → research_santiago_8_soa_erkenntnisse.md (SOA 2024)
7. ✅ **doc_santiago_9.txt** (4 Seiten) → research_santiago_9_cmfm_role_erkenntnisse.md (2019 früh)

### Gruppe 3: OPC UA + SCADA/MES (2 Docs)
8. ✅ **doc_chatgpt_1.txt** (7 Seiten) → research_doc_opcua_1_erkenntnisse.md
9. ✅ **doc_chatgpt_2.txt** (6 Seiten) → research_doc_scada_mes_erkenntnisse.md

---

## ⏭️ ÜBERSPRUNGEN: 2 SNMP Dokumente (Redundanz)

10. ⏭️ **doc_chatgpt_3.txt** (508 Zeilen) - SNMP Industrie 4.0
11. ⏭️ **doc_chatgpt_4.txt** (315 Zeilen) - SNMP MIB Objekte
**Grund**: SNMP bereits umfassend in doc_chatgpt_2 behandelt

---

## 📊 NICHT GELESEN: 1 Dokument (5G - niedrige Priorität)

12. ❌ 5G Papers im Uni-Ordner (2 Docs)
- Management_of_Industrial_5G_Networks_over_Asset_Administration_Shell.pdf
- Flexible_Reconfiguration_of_Industrial_5G_Networks_over_Asset_Administration_Shell.pdf
**Grund**: Benjamin sagte "vielleicht nicht ganz so wichtig"

---

## Erkenntnisse-Dateien erstellt: 9 Dateien

### CMFM-Linie (4 Dateien)
1. research_doc5_erkenntnisse.md - CMFM Generality & Workflow (2022)
2. research_doc6_erkenntnisse.md - CMFM Applied to HetIndNets (2019)
3. research_santiago_7_mmb_erkenntnisse.md - Multi-Message Broker (2024)
4. research_santiago_9_cmfm_role_erkenntnisse.md - Role of CMFM (2019 früh)

### SOA/OPC UA-Linie (3 Dateien)
5. research_doc3_erkenntnisse.md - SOA Communication Management (Automotive)
6. research_doc_opcua_1_erkenntnisse.md - OPC UA Funktionsweise
7. research_doc_scada_mes_erkenntnisse.md - SCADA/MES/OPC UA/SNMP
8. research_santiago_8_soa_erkenntnisse.md - SOA for I4.0 Digital Twins (gRPC/Protobuf)

### Meta-Dokumentation (1 Datei)
9. research_step1_zusammenfassung.md - Gesamtübersicht (erste 4 Docs)

---

## Kernerkenntnisse nach Option A

### 1. VIA = Multi-Message Broker (MMB)
**Quelle**: doc_santiago_7 (2024)
- **Northbound**: I4.0 Interface (OPC UA HTTP API)
- **Southbound**: Legacy Assets (Multi-Protocol: Pipe, Socket, TCP, FileQueue)
- **Internal Layers**: Consistency, Mapping, AAS Storage
- **AID/AIMC Submodels**: Asset Interface Description + Mapping Configuration
- **Sync/Async Translation**: Buffer OR block strategies

**VIA Mapping**:
- VIA Processes = Legacy Assets (Brownfield)
- VIA Registry = AAS Storage
- VIA IPC = Southbound Protocols
- VIA OPC UA API = Northbound Interface

### 2. VIA = Microservice Network (gRPC + Protobuf)
**Quelle**: doc_santiago_8 (2024)
- **gRPC**: High-performance, low-latency, HTTP/2 multiplexing
- **Protobuf**: Binary serialization, contract-first, code generation
- **One Microservice per Submodel** → **One Microservice per VIA Process**
- **Code Generation Pipeline**: OpenAPI → Protobuf → C++/Python/Java
- **Container Deployment**: Docker + Kubernetes, transparent relocation
- **AAS Core SDK**: Metamodel types, (de-)serialization → **via-core-cpp analog**

**VIA Mapping**:
- VIA Services = Microservices
- gRPC Communication = VIA Internal Network
- HTTP Northbound = OPC UA API
- Protobuf Definitions = VIA Interface Definitions

### 3. VIA = CMFM Domain
**Quellen**: doc5 (2022), doc6 (2019), doc9 (2019)

**Generality Hierarchy** (doc5):
- **M3**: CMFM Meta-Model (Implementation → User → Domain)
- **M2**: VIA-spezifische CMFs (SDK)
- **M1**: System-spezifische Representations

**Human-Centered** (doc9):
- **Manager knows abstract goal** (z.B. "Send message to Service X")
- **CMFM translates** zu konkrete Implementation (Pipe vs Socket vs TCP)
- **Equivalences** between different management systems

**VIA CMFs**:
- `registerProcess`, `discoverService`, `routeMessage`, `scheduleTask`, `healthMonitor`

**VIA Vocabulary**:
- Elements: Process, Service, Registry, Scheduler, Router
- Verbs: register, discover, route, schedule, monitor
- IPC Types: Pipe, Socket, TCP, FileQueue, Thread

### 4. Control Plane Architecture
**Quelle**: doc3 (SOA Communication in Automotive)
- **Data Plane**: IPC Mechanisms (actual message payloads)
- **Control Plane**: Registry, Orchestration, Scheduling
- **Management Plane**: CMFM-based Operations

**VIA Separation** (besser als Legacy Industrial):
- Legacy: Keine Trennung Data/Control/Management
- VIA: Klare Separation → bessere Flexibility

### 5. ISA-95 Levels Integration
**Quelle**: doc_chatgpt_2 (SCADA/MES)
- **Level 2 (SCADA)**: VIA Core (Prozessebene)
- **Level 3 (MES)**: VIA Orchestrator (Produktionsleitebene)
- **OPC UA als Vermittler**: Zwischen Levels

**VIA Telemetrie**:
- **OPC UA Subscriptions**: Echtzeitdaten
- **SNMP v3**: Monitoring/Alarme (lightweight)
- **Hybrid Approach**: Best of both worlds

### 6. OPC UA M3/M2/M1 Architecture
**Quelle**: doc_chatgpt_1 (OPC UA Funktionsweise)
- **M3**: OPC UA Basisebene (Objekte, Variablen, Methoden)
- **M2**: VIA-spezifische Typen (Domain Model)
- **M1**: Laufende VIA-Instanzen

**Address Space**:
```
VIA Root
├── ProcessRegistry (Object)
│   ├── RegisteredProcesses[] (List)
│   ├── RegisterProcess() (Method)
│   └── DiscoverProcess() (Method)
├── Scheduler (Object)
│   ├── TaskQueue[] (List)
│   └── ScheduleTask() (Method)
└── Router (Object)
    ├── RouteTable[] (List)
    └── RouteMessage() (Method)
```

**VIA Companion Specification**: Eigene OPC UA Spec für VIA

---

## Timeline: CMFM Evolution verstanden

### 2019 (doc9 - frühe Version)
- **Foundation**: Human-Centered Abstraction
- **Minimum**: Goal, Input, Output
- **Problem**: Heterogeneity in Management Plane
- **Concept**: Network of Networks

### 2019 (doc6 - HetIndNets)
- **Elaboration**: Meta-Model Details
- **Taxonomy**: Hierarchical Composition
- **Constraints**: Time, Order, Existence, Mutual Exclusiveness
- **Use-Case**: PROFIBUS + IIoT + TCP/IP

### 2022 (doc5 - Generality & Workflow)
- **Formalization**: Generality Hierarchy
- **Catalog vs Core**: Promotion Mechanism
- **Vocabulary Management**: Repository (wie GitHub)
- **AAS Integration**: CMFs als Operations

### 2024 (doc7 - MMB)
- **Implementation**: Multi-Message Broker als Gateway
- **AID/AIMC**: Submodels für Integration
- **Prototype**: TypeScript, aas-core3.0-typescript
- **Real Deployment**: Brownfield Integration

### 2024 (doc8 - SOA)
- **Microservices**: gRPC + Protobuf Network
- **Code Generation**: Automated Pipeline
- **Container Deployment**: Docker + Kubernetes
- **Evaluation**: C# .NET Implementation

---

## Noch ausstehend (für Repository-Analyse)

### Repositories zu analysieren:
1. ⏳ **open62541** (GitHub) - C99 OPC UA Implementation
2. ⏳ **UA-Nodeset** (GitHub) - Standard NodeSets, Companion Specs
3. ⏳ **aas-core-works** (GitHub) - AAS Metamodel, Python SDK, C++ SDK

### Zu erarbeiten:
4. ⏳ **VIA ↔ OPC UA M3 Mapping** - Konkrete Typdefinitionen
5. ⏳ **OPC UA Research Playbook** - Synthese aller Erkenntnisse

---

## Token-Budget nach Option A

**Verbraucht**: ~109K/200K (54.5%)
**Verbleibend**: ~91K Tokens

**Reicht für**:
- Repository-Analyse: **NICHT** genug (geschätzt 50-80K pro Repo)
- SNMP Docs nachträglich: Ja (~30K)
- Finaler Status-Report: Ja (~10K)

**Empfehlung**:
- ✅ Papers vollständig gelesen (Option A erfüllt)
- ❌ NICHT weiter mit Repositories (Token-Reset nötig)
- ✅ Finalen Status schreiben, dann STOPPEN

---

## Nächste Schritte (nach Token-Reset)

1. **Mit frischen Tokens**: Repository-Analyse (open62541, UA-Nodeset, aas-core-works)
2. **VIA M3 Mapping erarbeiten** (OPC UA + AAS)
3. **OPC UA Research Playbook erstellen** (Synthese)
4. **AAS Research Playbook erstellen**
5. **CMFM Research Playbook erstellen** (alle Santiago Papers synthetisiert)
6. **Main System Playbooks** (M3/M2/M1)
7. **Exposé nach CELM-Vorlage**
