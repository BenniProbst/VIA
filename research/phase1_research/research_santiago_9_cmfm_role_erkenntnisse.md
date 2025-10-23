# Erkenntnisse: Role of CMFM in HetIndNets (Santiago Olaya 2019 - Frühe Version)

## Autoren
Santiago Soler Perez Olaya, Martin Wollschlaeger (TU Dresden, 2019)

## Kontext: Industrie 4.0 + IIoT Herausforderungen

**Trends**:
- Factories of the Future (FoF) - EU Horizon 2020
- Industrie 4.0 (I40) - Germany
- Industrial Internet of Things (IIoT) - Parallel sensor networks

**Problem**: **Heterogeneity** in Management Plane wächst dramatisch

---

## CMFM Kernkonzept (Human-Centered)

### Grundidee
- **Network Manager kennt abstrakt**, was zu tun ist
- **Manager-centric**, nicht System-centric
- **Domain-specific Abstraction** der Management Tasks

### CMFM Komponenten (Minimum)
1. **Goal**: Was soll erreicht werden
2. **Required Information**: Input
3. **Expected Output**: Was wird zurückgegeben

**Beispiel**: "Set network address of device"
- **PROFIBUS**: Set variable via set command
- **WBEM**: Set property of object in object tree
- **SNMP**: Read-only in standard MIB, nur über enterprise MIB

→ **Gleicher Goal**, verschiedene Implementations

---

## Management Plane Heterogeneity

### Legacy Industrial Systems
- **Keine Trennung**: Data, Control, Management Plane (anders als IT)
- **Proprietary Interfaces**: Nur für Hersteller-Tools
- **PLC = Master**: Führt preprogrammed configuration aus
- **Engineering Phase**: Config designed, bleibt statisch
- **Runtime Flexibility**: Unthinkable ohne huge prior efforts

### IIoT Approach
- **Parallel Sensor Networks**: Nicht interfere mit Fieldbus
- **Real-time Measurements**: Predictive Maintenance, Optimization
- **Circumvents Interoperability**: Aber **erhöht Heterogeneity**
- **Does NOT solve Management Problem**

---

## Management System Functions

### Table 1: Common Functions across Systems

| System | Functions/Operations |
|--------|----------------------|
| **OSI Management** | M-Create, M-Delete, M-Action, M-Set, M-Get, M-Event_Report |
| **WBEM** | GetInstance, ModifyInstance, InvokeMethod, EnumerateClasses, etc. |
| **SNMP** | GetRequest, SetRequest, SNMPv2-Trap, InformRequest, etc. |
| **PROFIBUS** | Reset, Set-Value, Read-Value, Event, Live-List, Upload/Download |

**Equivalences**:
- **WBEM InvokeMethod** = **PROFIBUS stateless/state-oriented functions**
- **SNMP** hat kein direktes equivalent, aber kann auch trigger function

---

## Network of Networks Concept

### Typical Industrial Facility
- **Office**: Standard IT Networks (TCP/IP Ethernet)
- **Shop Floor**: Different legacy industrial communication systems
- **IIoT**: Parallel sensor networks

→ **Network of Networks**

### Handicap
- Legacy systems **not designed to interoperate**
- Robust, aber **far from flexibility**
- **Network Management** bisher zu sehr relegated to engineering tools

### CMFM Solution
- **Seamless Integration**: Access different management systems
- **Holistic Management**: Manage network of networks **as single network**
- **Sufficient Abstraction Level**: Enable orchestration throughout
- **Aligns with Interpreter Concept** [Derhamy 2017], but **focus on Management Plane**

---

## Asset Administration Shell (AAS) Context

### I40 AAS Goal
- **Harmonize access** to management and engineering data/functions
- **Asset** = anything valuable for value chain
- **AAS accompanies Asset** through lifecycle

### AAS Management (2019 Status)
- **Yet-to-standardize** communication service
- **Still-not-listed** partial models
- **Management functions/services** yet to define

→ CMFM kann hier Lücke füllen!

---

## Use-Case: PROFIBUS + IIoT + TCP/IP

### Scenario
- **Legacy**: PROFIBUS (shop floor)
- **New**: IIoT sensor network (predictive maintenance)
- **Office**: TCP/IP Ethernet
- **Connection**: PLC Ethernet port (programming/debugging)

### Many Facilities, Central Operations Office
- **3 Management Systems**:
  1. WBEM/SNMP (IT network)
  2. NETCONF (IIoT, angenommen)
  3. Fieldbus Management (PROFIBUS)

### CMFM Encapsulates Expertise
- **Network/System Engineers' Knowledge** for specific domain
- **Reduced Effort**: Integration of future communication systems

### Example: Monitor E2E Delay
**Goal**: Monitor IIoT sensor → PLC delay (crossing both networks)
**Challenge**: Requires info from **both management systems**
**CMFM Solution**:
- **monitor E2E delay** CMFM
- Gathers knowledge to monitor delay in both systems
- **Automatically** gather required info + perform operations

---

## Time-Sensitive Networking (TSN) Outlook

### Promise
- **Seamless coexistence** all communication requirements same network
- Ethernet with TSN Task Force

### Challenge
- **Very complex** implementation in industrial facilities
- **Brownfield Integration**: Still-running legacy systems
- **Roadmap needed**: Ensure viability, success

### Interoperability
- **Data Plane**: Seamless communication (vertical + horizontal)
- **Management Plane**: Challenge remains → **CMFM Solution**

---

## Future Work (2019)

1. **Listing** domain-specific required/optional CMFMs
2. **Semantics + Ontologies** in combination with interoperability
3. **Holistic Management Systems** where CMFMs play central role

---

## Vergleich zu späteren CMFM Papers

### Diese Version (2019) - Grundkonzept
- **Human-Centered** Abstraction
- **Minimum Components**: Goal, Input, Output
- **Equivalences** zwischen Management Systems
- **Network of Networks** Motivation

### Spätere Versionen (2022)
- **Generality Hierarchy**: Implementation → User → Domain
- **Catalog vs Core** (Promotion)
- **Vocabulary Management** (Repository)
- **AAS Integration** (Companion Spec)
- **Workflow** für CMF-Erstellung

→ **2019 = Foundation**, 2022 = Elaboration + Formalization

---

## Relevanz für VIA

### 1. VIA = Network of Networks
- **VIA Processes** = Network Nodes
- **IPC Mechanisms** = Heterogeneous Protocols (Pipe, Socket, TCP, FileQueue, Thread)
- **VIA Registry** = Holistic Management

### 2. VIA CMFMs
**Analog zu Use-Case**:
- `registerProcess`: Register Process in VIA Registry
- `discoverService`: Find available services
- `routeMessage`: Route to correct process
- `monitorE2ELatency`: Monitor across different IPC mechanisms

### 3. Abstraction über IPC Heterogeneity
**Same Goal, different implementations**:
- `sendMessage` via Pipe (sync)
- `sendMessage` via Socket (async)
- `sendMessage` via TCP (async, remote)
- `sendMessage` via FileQueue (async, persistent)

### 4. Human-Centered VIA Management
- **Developer kennt abstraktes Ziel** (z.B. "Send data to Service X")
- **VIA translates** zu konkrete IPC Mechanism
- **VIA CMFM encapsulates** Expertise über IPC mechanisms

### 5. VIA als "Operations Office"
- **Central VIA Registry** manages many distributed Processes
- **3 Management Contexts**:
  1. **Local**: Pipe/Unix Socket (fast, low-latency)
  2. **Remote**: TCP (network, higher latency)
  3. **Persistent**: FileQueue (store-and-forward)

### 6. Data vs Control vs Management Plane
**VIA Separation** (besser als Legacy Industrial):
- **Data Plane**: Actual message payloads via IPC
- **Control Plane**: VIA Scheduler, Router
- **Management Plane**: VIA Registry, CMFM-based Operations

### 7. Engineering vs Runtime Flexibility
**VIA Improvement**:
- **Legacy**: Config designed in engineering, bleibt statisch
- **VIA**: Dynamic Process registration, runtime reconfiguration

---

## Offene Fragen für VIA

1. **VIA CMFM Listing**: Welche CMFMs für VIA Domain?
2. **VIA Vocabulary**: Semantics für VIA Elements/Verbs?
3. **VIA Ontology**: Formal model für VIA Management?
4. **Equivalence Detection**: Auto-detect gleiche Goals über IPC mechanisms?
5. **Interoperability Approaches**: VIA CMFM + existing standards (OPC UA, DDS)?
6. **Brownfield Integration**: VIA Wrapper für legacy C++ apps?
