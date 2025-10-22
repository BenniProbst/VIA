# Erkenntnisse: SOA for I4.0 Digital Twins (Santiago et al., IECON 2024)

## Autoren
Nico Braunisch, Tom Gneuß, Uwe Schmidt (TU Dresden)
Marko Ristin, Hans Wernher van de Venn (ZHAW)
Martin Wollschlaeger (TU Dresden)

## Kernkonzept: Microservice Architecture für AAS

**Problem**: Kein Roadmap für large + distributed I4.0 System
**Lösung**: SOA mit gRPC + Protobuf, Partitionierung in Microservice Network

---

## Architecture: Northbound/Southbound + Internal

### Northbound (NB)
- **HTTP-Northbound Service**: Sole representative of AAS
- **Provides**: AAS Interface + Submodel Interface (Part 2 Spec)
- **To**: I4.0 Environment (external)
- **Swagger UI**: API Documentation

### Internal (gRPC Network)
- **AssetAdministrationShellService**: AAS Runtime
- **SubmodelService**: One per Submodel (narrow scope)
  - Implements Submodel Interface API
  - Custom endpoints optional
- **Submodel Repository** (optional): Represents all SubmodelServices
- **Mapping**: HTTP Request → identical gRPC function call

### Southbound (SB)
- **Part of SubmodelService** (yellow in diagram)
- **Establishes connection** to physical asset
- **Native Protocol**: Asset's own protocol
- **Adapter-based**: Choose appropriate adapter per asset

---

## gRPC + Protobuf Vorteile

### gRPC (Google Remote Procedure Call)
- **High-performance, low-latency**
- **HTTP/2**: Multiplexing requests over single TCP
- **Language Interoperability**: C++, C#, Python, Java, Go, etc.
- **Request-Response**: Remote Procedure Calls
- **Publish-Subscribe**: Channels

### Protocol Buffers (Protobuf)
- **Binary serialization**: Compact, efficient (vs JSON/XML)
- **Backward/Forward Compatibility**: Easy evolution
- **Contract-first**: Interface + message definitions in advance
- **Code Generation**: Boilerplate for multiple languages
- **Type Safety**: Well-structured classes/objects

### Advantages over HTTP REST
- **No dynamic payload construction**: Invoke as local functions
- **Efficient parsing**: Automatic, no overhead
- **Convenient data exchange**: Type-safe
- **Language-agnostic**: Evolve independently

---

## Code Generation Pipeline

### 1. OpenAPI → Protobuf
- **Input**: AAS API JSON/YAML from OpenAPI-Hub
- **Tool**: OpenAPI Generator
- **Output**: Protobuf definitions (.proto files)
- **Manual tailoring**: Remove redundant parameters, unprovided endpoints

### 2. Protobuf → Language-specific Code
- **Protobuf Compiler** (protoc)
- **Generates**:
  - **Messages**: Classes with getters/setters
  - **AAS Metamodel Types**: Submodel, SubmodelElement
  - **Service Stubs**: Interfaces/abstract classes per service

### 3. HTTP API Code
- **OpenAPI Code Generator**
- **Target**: ASP.NET Core (C#), Node.js (TypeScript), etc.
- **Swagger-based Documentation**

### 4. Implementation
- **Northbound**: Determines SubmodelService address, opens gRPC channel
- **SubmodelService**: Returns cached OR fetches from asset
- **Southbound**: Protocol-specific packages

---

## AAS Interaction Types

### Type 1 (Passive)
- **File-based**: XML, JSON, RDF, AASX serialization
- **Simple**, low complexity

### Type 2 (Active/Reactive)
- **HTTP API**: Dynamic, real-time
- **Currently specified**: Part 2 Spec
- **This paper's focus**

### Type 3 (Proactive)
- **Autonomous AAS-to-AAS communication**
- **Dedicated I4.0 language** (future)
- **High automation, intelligent systems**

---

## SOA vs Microservices

### SOA (Service-Oriented Architecture)
- **Service = Business Process**: Persistence, User Management
- **ESB (Enterprise Service Bus)**: SOAP Messages
- **Homogenous Tech Stack**: Maintainability
- **Deployed together**, thoroughly orchestrated

### MSA (Microservice Architecture)
- **Microservice = Single Task**: Narrowly scoped
- **Independent**: Develop, deploy, scale independently
- **Decentralized Data**: Each has own database
- **Tech Stack Agnostic**: Interface compliance only

### MSA Advantages
- **Independence**: Speed up development
- **Parallelism**: Instantiate in parallel → scalability
- **Fault Isolation**: Errors don't affect others (expected to fail)

### MSA Disadvantages
- **Complexity**: Many services to manage
- **Data Integrity**: Challenging across parallel services

---

## Deployment Strategy

### Container-based (Docker)
- **Services packaged as containers**: Implementation-independent from machine
- **Mobile**: Don't need same machine
- **Transparent Relocation**: SubmodelService near asset, gRPC for long distance
- **Loose Coupling**: Different programming languages possible

### Orchestration (Kubernetes)
- **Infrastructure Services**: AAS Registry (off-the-shelf)
- **Combined**: Northbound + SubmodelServices + Registry

---

## Evaluation: C# .NET Implementation

### Technology Stack
- **Language**: C# .NET
- **HTTP**: ASP.NET Core
- **gRPC**: ASP.NET Core gRPC package
- **AAS SDK**: aas-core-csharp [16] (metamodel types, (de-)serialization)
- **Protobuf**: Generated from OpenAPI Entire-API-Collection

### Problems Encountered
- **OpenAPI → Protobuf**: Some data types differ, inheritance detection fails
- **Protobuf Restrictions**: No inheritance (resort to composition)
- **Manual Fixes**: Invalid structures, ill-defined types
- **Duality**: Protobuf-generated classes vs AAS Core SDK classes (future work)

### Prototype Limitations
- **Static XML AAS**: Loaded at startup (no dynamic southbound)
- **No dynamic submodel addition**: Runtime addition not yet conceptualized

---

## Related Work

### Kuhn et al. (BaSyx)
- **Timing Restrictions**: Conflict SOA ↔ Legacy control (soft vs hard real-time)
- **Solution**: SOA for higher levels (data aggregation, planning), PLC for time-critical

### Kanaan et al.
- **VDI/VDE 2193-1 Bidding Protocol**: Self-organizing assets
- **SOA provides stage** for collaborating assets

### Dietrich et al.
- **Open-source AAS System Architecture**
- **Tech**: Docker, Kubernetes, Apache Kafka, InfluxDB
- **Microservices**: Data management, communication

---

## Relevanz für VIA

### 1. VIA = Microservice Network
**VIA Services als Microservices**:
- **One microservice per VIA Process**
- **gRPC Communication**: VIA Core ↔ Processes
- **HTTP Northbound**: OPC UA API für I4.0 Environment

### 2. VIA Code Generation
**Model-Driven Approach**:
- **M3 → Protobuf**: VIA Metamodel als .proto
- **Protobuf Compiler**: Generate C++/Python/Java code
- **VIA SDK**: aas-core analog für VIA
- **Boilerplate Elimination**: Process stubs auto-generated

### 3. VIA Northbound/Southbound
**Analog zu Paper**:
- **NB**: OPC UA HTTP API (Standard I4.0)
- **Internal**: gRPC Network (VIA Services)
- **SB**: IPC Mechanisms (Pipe, Socket, TCP, FileQueue, Thread)

### 4. Contract-First Paradigm
**VIA Interface Definitions**:
- **Protobuf files**: Define VIA Service Interfaces
- **Messages**: VIA Data Structures (Process, Task, Message, etc.)
- **Language-agnostic**: C++ Core + Python Scripts + Java Clients

### 5. Transparent Relocation
**VIA Deployment**:
- **VIA Scheduler**: Can be near workload
- **VIA Router**: Can be near network gateway
- **VIA Registry**: Centralized OR distributed
- **gRPC**: Efficient over network

### 6. Container Deployment
**VIA Containerization**:
- **Docker**: Each VIA Service as container
- **Kubernetes**: Orchestration, scaling
- **Dynamic Instantiation**: New Process → new container (like dynamic submodel)

### 7. AAS Core SDK Equivalent
**VIA Core SDK**:
- **Via-core-cpp**: Metamodel types, (de-)serialization
- **Protobuf Duality**: Resolve wie Santiago
- **Single Source**: Unified VIA SDK

### 8. Dynamic Submodel Problem
**VIA Equivalent**:
- **Runtime Process Addition**: Start container, parameterize, register
- **Open Question für VIA**: Conceptualize + implement

---

## Offene Fragen für VIA

1. **VIA Protobuf**: Eigene .proto für VIA Metamodel?
2. **OpenAPI Spec für VIA**: JSON/YAML für VIA API?
3. **Protobuf ↔ via-core-cpp**: Duality harmonization?
4. **Dynamic Process Addition**: Container orchestration strategy?
5. **gRPC vs OPC UA**: Hybrid oder exklusiv?
6. **Real-time über gRPC**: Soft real-time guarantees?
7. **Submodel Repository analog**: VIA Process Repository Service?
