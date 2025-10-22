# Erkenntnisse: CMFM Applied to HetIndNets (Santiago Olaya 2019)

## Quelle
Santiago Soler Perez Olaya, Robert Lehmann, Martin Wollschlaeger
TU Dresden, Chair of Industrial Communications
IEEE 2019 INDIN Conference

## Kern: CMFM für Heterogeneous Industrial Networks (HetIndNet)

### 1. Management Paradigmen Klassifikation

**Value-based Management**:
- Fokus: Managed Network (Information Models/Objects)
- Operations: get/set von Werten
- Besser für Monitoring als Configuration
- Beispiel: SNMP

**Policy-based Management**:
- Intent-oriented approach
- Network rekonfiguriert sich selbst via Policies
- Problem: Limitiertes Spektrum in der Praxis
- Behavior delegation an Network Devices

**Requirements-based Management**:
- Service Level Agreements (SLA)
- Top-Down Approach
- Erwartet homogene Communication Stratum
- Beispiele: SDN, NFV, TSN Stream Reservation

**Ontology-based Management**:
- Semantic Technologies
- Use Cases: Model Integration, Information Representation, Semantic Reasoners
- Problem: Akademisch reif, praktisch kaum implementiert

### 2. CMFM = Human-Centered vs System-Centric

**Problem**: Network Manager schreibt Scripts nur für eine spezifische Network Instance

**Lösung CMFM**:
- Abstraction Layer zwischen heterogenem Netzwerk und Manager
- Formalisierung von Manager-Wissen und Expertise
- Wissenstransfer zwischen Generationen/Teams/Integratoren/Endusern

### 3. CMFM Meta-Model Details

**Mandatory Components**:
- **Goal**: Semantic-validated expression (Intent des Managers)
- **Output**: Erwartete Information (Erfolg/Fehler)

**Optional Components**:
- **Input**: Benötigte Information
- **Constraints**: Einschränkungen (Time, Order, Existence, Mutual Exclusiveness, Execution Success)
- **Representation**: CLI Scripts für spezifisches Management System

**Taxonomy Structure**:
- Hierarchische Struktur (Composition)
- Incomplete Composition möglich
- Ein CMFM kann mehrere Super-CMFMs haben
- Beispiel: `resetLogs` unter `restartNetwork` UND `freeUpMemory`

### 4. Constraints-Typen
1. **Time**: z.B. Updates nur nachts
2. **Order**: z.B. erst `readConfig`, dann `enforceConfig`
3. **Existence**: z.B. Network Devices eines Typs vorhanden
4. **Mutual Exclusiveness**: z.B. während `readConfig` ist `enforceConfig` nicht erlaubt
5. **Execution Success**: Abhängigkeiten zwischen CMFMs

### 5. Vocabulary & Semantic Validation
- **Expression**: Helper Abstract Class für Input/Output/Constraint/Goal
- **Vocabulary Terms**: Müssen aus Katalog valider Konzepte kommen
- **Balance**: Exactitude vs Complexity
- **Iteratives Wachstum**: Vocabulary kann schrittweise erweitert werden

### 6. Use-Case: PROFIBUS + IIoT + TCP/IP

**Szenario**:
- PROFIBUS (Feldebene)
- IIoT Sensor Network (Predictive Maintenance)
- TCP/IP Ethernet (Office Network)
- Central Operations Office

**Management Systems**:
- SNMP für TCP/IP
- OMA-DM für IIoT
- Fieldbus Management für PROFIBUS

**Beispiel CMF**: `enforceConfig`
- **Goal**: "use input configuration information from OO and engineering station to configure gateway PROFIBUS-IIoT, gateway TCP/IP-IIoT, IIoT nodes, and building router, and program the PLC. Check for errors and output result"
- **Input**: "list of pairs configuration file and target element"
- **Output**: "result of the error check"
- **Representations**: 5 (4 für Configuration + 1 für PLC Programming)

**Vocabulary für Use-Case**:
- **Elements**: IIoT node, gateway PROFIBUS-IIoT, gateway TCP/IP-IIoT, PLC, Field Device, PC, engineering station, building router, operation office
- **Verbs**: enforce, check, send, program, use
- **General**: input, output, goal, health, configuration, information, representation, constraint

### 7. Evaluation: CMFM vs SNMP vs NETCONF vs WBEM

| Criteria | SNMP | NETCONF | WBEM | CMFM |
|----------|------|---------|------|------|
| Monitoring | 4 | 3 | 4 | 3 |
| Configuration | 1 | 4 | 3 | 3 |
| Heterogeneity | 1 | 1 | 2 | **4** |
| Intent | 1 | 2 | 3 | **4** |
| Human-centric | 1 | 1 | 2 | **4** |

**CMFM Stärken**:
- Heterogeneity Management (einzigartig)
- Intent-based (stark)
- Human-centric (stark)

**CMFM Schwächen**:
- Monitoring nicht so gut wie SNMP
- Configuration nicht so gut wie NETCONF

### 8. Roadmap & Feasibility

**Problem Ontology-only Approach**:
- "Manage yourself!" Button unrealistisch
- Reasoner für optimales Management in Real-Time nicht machbar

**CMFM Roadmap**:
1. **Step 1**: Vocabulary definieren (Balance exactitude/complexity)
2. **Step 2**: CMFM Taxonomy mit Manager-Wissen füllen
3. **Step 3**: Schrittweise Automatisierung
4. **Step 4**: Reasoner über gesammelte Knowledge (offline)

**Vorteile Smooth Transition**:
- Sofortiger Nutzen: Overview, Knowledge Transfer
- Schrittweise Automatisierung möglich
- Foundation für Full Automation

### 9. Industry 4.0 Integration

**Asset Administration Shell (AAS)**:
- Jedes Asset hat AAS für Lebenszyklus
- AAS managed Interaktion mit Environment
- Yet-to-standardize Communication Service
- CMFM können Teil des AAS sein

**Problem aktuelle Industrial Systems**:
- Keine Trennung Data/Control/Management Plane
- Proprietary Management Interfaces
- Nur für Manufacturer Tools

## Relevanz für VIA

### 1. Direkte Anwendung
- **VIA als HetIndNet**: Heterogene Prozesse über Pipe/Socket/TCP/File-Queue/Thread
- **CMFM für VIA Services**: Service Registry, Orchestration, Scheduling
- **Human-Centered**: VIA Playbooks = CMFM Taxonomy für VIA Domain

### 2. VIA-spezifische CMFMs
- `registerProcess`: Process im VIA Registry registrieren
- `discoverService`: Verfügbare Services finden
- `routeMessage`: Message zum korrekten Process routen
- `scheduleTask`: Task im VIA Scheduler einplanen
- `healthMonitor`: Health Status aller Processes monitoren

### 3. VIA Vocabulary
**Elements**: Process, Service, Registry, Scheduler, Router, Message, Task, Session, Cluster
**Verbs**: register, discover, route, schedule, monitor, connect, disconnect, send, receive
**IPC Types**: Pipe, UnixSocket, TCP, FileQueue, ThreadMessaging, RoundRobinMemoryStream

### 4. VIA Constraints
- **Time**: Scheduling nur in bestimmten Slots
- **Order**: Erst Registry, dann Discovery, dann Route
- **Existence**: Service muss registered sein
- **Mutual Exclusiveness**: Während Migration kein neuer Traffic
- **Execution Success**: Bei Registry-Failure alle Services benachrichtigen

### 5. VIA als Abstraction Layer
- **Data Plane**: IPC Mechanisms (Pipe, Socket, TCP, etc.)
- **Control Plane**: VIA Orchestration, Scheduling, Registry
- **Management Plane**: VIA CMFM für holistic Management

### 6. Integration mit M3/M2/M1
- **M3**: CMFM Meta-Model Definition
- **M2**: VIA-spezifische CMFMs (SDK)
- **M1**: System-spezifische Representations

## Offene Fragen für VIA
1. Wie CMFM Taxonomy für VIA Domain strukturieren?
2. CLI Scripts vs C++ API als Representations?
3. Reasoner für automatische VIA Configuration?
4. Integration mit Kubernetes Service Registry?
5. Telemetry als CMFM Output?
