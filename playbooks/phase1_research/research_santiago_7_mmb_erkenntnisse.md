# Erkenntnisse: Dynamic Multi-Message Broker (Santiago et al., IEEE 2024)

## Autoren
Nico Braunisch, Robert Lehmann, Uwe Schmidt, Tom Gneuß (TU Dresden)
Daniel Kluge (Infineon), Martin Wollschlaeger (TU Dresden)
IEEE ETFA 2024

## Problem: Brownfield Integration in Industry 4.0

**Legacy Devices**:
- Purpose-built hardware
- Inflexibly bound to certain communication protocols
- Do not integrate with I4.0 interaction methods
- Replacing not economical

**Solution**: Multi-Message Broker (MMB) as Gateway

---

## Multi-Message Broker (MMB) Konzept

### Architektur (Northbound/Southbound)

**Northbound (NB)**: I4.0 Ecosystem
- HTTP API (Type 2 AAS)
- Future: Proactive AAS (Type 3) für peer-to-peer

**Southbound (SB)**: Legacy Assets
- Modbus, HTTP, MQTT
- Future: PROFIBUS, EtherCAT, PROFINET

**Internal Layers**:
- **Consistency Layer**: Identische Requests → gleiche Info
- **Mapping Layer**: Wählt geeigneten Connector, optional Data Transformation
- **AAS Storage**: Ein AAS pro Legacy Asset

### Kernfunktionen

1. **Provision of I4.0 Interface**: AAS für Brownfield Devices
2. **Data Mapping**: Transformation Source ↔ Destination Format
3. **Sync/Async Handling**: Buffer latest status ODER block until response
4. **Multi-Protocol Support**: Viele Protokolle gleichzeitig

---

## AAS Submodels für Integration

### Asset Interfaces Description (AID)
- **Von Vendor**: Available Endpoints
- **Protocols**: Modbus, HTTP, MQTT (v1.0), zukünftig mehr
- **Basiert auf**: W3C Web of Things Thing Description (WoT TD)
- **Externe Descriptors**: GSD, GSDML, IO Device Description

### Asset Interfaces Mapping Configuration (AIMC)
- **Von User**: Bidirectional Mapping Asset ↔ AAS
- **Links**: AID Endpoints → AAS SubmodelElements
- **Problem**: AIMC erlaubt KEINE Data Transformations (derzeit)

### Runtime Environment
- **Nicht in Submodels**: Actual Interaction Execution
- Liest AID → interacts with Asset
- Populates AAS gemäß AIMC
- Delivers via I4.0 Interface

---

## AAS Interaction Typen

**Type 1 (Passive AAS)**:
- Static exchange (XML, JSON, RDF, AASX serialization)

**Type 2 (Reactive AAS)**:
- HTTP API (implementation-agnostic)
- Aktuell einzig offiziell spezifiziert

**Type 3 (Proactive AAS)**:
- Autonomous inter-AAS communication
- Dedicated I4.0 language (Zukunft)
- Self-orchestrated I4.0 components

---

## Synchronous vs Asynchronous

### Problem
- **NB**: HTTP API synchronous
- **SB**: Asset kann async sein (MQTT)

### MMB Lösungen
1. **Buffer**: Latest asset status → deliver on request
2. **Block**: Wait for latest data from asset before HTTP response

### Protokoll-Translation
**Sync → Async**:
- Delay response until async response available ODER
- Acknowledgement + separate polling later

**Async → Sync**:
- Block until sync response ODER
- Buffer result until polled

---

## Real-time vs Non-real-time

### Hard Real-time
- Reaction MUSS in exact time (not exceed, not fall short)
- No retransmission (unforeseeable delays)

### Soft Real-time
- Statistical compliance
- Occasional deviations ok

### MMB
- Gateway zwischen Real-time (Fieldbus) und Non-real-time (HTTP)
- Careful attention bei inter-protocol communication

---

## Controller/Peripheral vs Client/Server vs Pub/Sub

### Controller/Peripheral (Master/Slave)
- One/few controllers steer devices
- Regular bus cycle times
- Controller sends instructions
- Devices write back process data

### Client/Server
- Every participant can initiate
- Direct communication with partner
- Server can be client to another server

### Publish/Subscribe (Observer)
- Decouple communication partners
- Subscribe to topics
- Publish updates on channels
- Intervals not constant
- Central broker manages forwarding

---

## Prototype Implementation

### Technology Stack
- **Language**: TypeScript with Node.js
- **Framework**: aas-core3.0-typescript
- **NB**: HTTP Interface Server
- **SB**: MQTT Connector

### Components
- **MultiMessageBroker**: Heart, AAS Registration
- **FileImporter**: Load AAS description files
- **AIMCMapper**: Evaluate AIMC + AID, dedicated parsers
- **AbstractInterfaceServer**: Generalized NB API (subclass for new protocols)
- **AbstractConnectionObject**: Generalized SB API (subclass for new protocols)

### Extensibility
- Abstract classes → minimal dependencies
- Separate project for concrete implementations
- Callbacks: onRequestCallback (NB), onConnectorEvent (SB)

---

## Relevanz für VIA

### 1. VIA als MMB
**VIA = Multi-Message Broker**:
- **NB**: OPC UA Server (I4.0 compliant)
- **SB**: VIA IPC Mechanisms (Pipe, Socket, TCP, FileQueue, Thread)
- **Internal**: VIA Registry, Scheduler, Router

### 2. VIA Process = Asset
- **Each Process**: Legacy "Asset" im VIA Kontext
- **VIA Registry**: AAS für jeden Process
- **AID**: VIA Process Interfaces (Pipe, Socket, etc.)
- **AIMC**: Mapping Process Data → VIA Address Space

### 3. Sync/Async Handling
- **VIA Router**: Buffer latest Process status
- **VIA Scheduler**: Block until Process response
- **Telemetry**: Async Subscriptions

### 4. Multi-Protocol Support
**VIA Southbound**:
- Pipe (sync)
- Unix Socket (sync/async)
- TCP (async)
- File-Queue (async)
- Thread-Messaging (sync)
- Round Robin Memory Streams (async)

**VIA Northbound**:
- OPC UA HTTP API
- OPC UA PubSub (MQTT)
- Future: Proactive AAS (Type 3)

### 5. Consistency Layer
- **VIA Registry**: Ensure identical requests → same result
- **Lock-free**: Round Robin Memory Streams
- **Concurrent Access**: Chaos Tests

### 6. Mapping Layer
**VIA Mapping**:
- Process IPC Interface → OPC UA Methods
- Process Data Types → OPC UA Variables
- Process Events → OPC UA Events

### 7. Retrofit Concept
**VIA Retrofitting**:
- Existing C++ Applications = Brownfield
- VIA Process Wrapper = Retrofit Adapter
- VIA AAS = Digital Twin für Legacy App

### 8. TypeScript Prototype Lessons
- **Model-driven**: aas-core3.0-typescript
- **Abstract Classes**: Extensibility
- **Callbacks**: Event-driven Architecture
- **Separate Modules**: Minimize dependencies

---

## Offene Fragen für VIA

1. **VIA AID Submodel**: Eigene Spec für VIA IPC Interfaces?
2. **VIA AIMC**: Data Transformations spezifizieren?
3. **WoT TD Integration**: Web of Things für VIA Processes?
4. **Real-time Guarantees**: Wie VIA Gateway Real-time bewahren?
5. **Proactive VIA**: Type 3 AAS für autonome Process-Orchestration?
6. **Chaos Testing**: MMB-style Testing für VIA Consistency?
