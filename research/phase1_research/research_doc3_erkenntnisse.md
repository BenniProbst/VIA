# Erkenntnisse: d1-02 (SOA Communication Management in Automotive)

## Quelle
IEEE SA Ethernet & IP @ Automotive Technology Day 2021
Trista Lin, David Fernandez Blanco, Juleixis Guariguata

## Hauptthemen

### 1. SOA Architektur im Automotive
- **Ziel**: Software-definierte Fahrzeuge statt Hardware-definierte
- **Treiber**: Elektrifizierung, Autonomes Fahren, Konnektivität, Shared Mobility
- **Konzept**: Service-Oriented Architecture mit Virtualisierung

### 2. Kommunikationsprotokolle Vergleich
**SOME/IP**:
- Automotive-spezifisch
- Service discovery
- Legacy ECU Kommunikation
- Adaptive/Classic Autosar kompatibel

**DDS (Data Distribution Service)**:
- Data-centric
- Publish/Subscribe
- N-N Topologie
- QoS-aware

**OPC UA**:
- Interoperabilität
- Data modeling
- Server discovery
- Session authentication
- Data confidentiality

### 3. SOA Prinzipien
- Modularity, Abstraction, Loose coupling
- Fault Tolerance, Open Standards
- Service Composition, Reusability
- Orchestration, Load balancing

### 4. Control Plane vs Data Plane
**Control Plane Services**:
- Orchestration, Task Assignment
- Network Supervision, Error Handling
- Dynamic Reconfiguration
- SOTA/FOTA/AOTA update
- Lifecycle management

**Data Plane**:
- Eigentliche Service-Kommunikation
- Transparent durch Control Plane

### 5. Herausforderungen
- **Heterogenität**: Classic Autosar, Adaptive Autosar, Linux, Android
- **Dynamik**: Stateful/Stateless Services, Fine-grained services
- **Latenz**: Real-time Anforderungen
- **RAMS & Security**: Failover, unauthorized access prevention

### 6. Trend: Data-Centric
- Von Signal zu Service
- Data addressing via Topics/Named Data
- Apps kurzlebig, ständig updated
- Scalable Software Architecture

## Relevanz für VIA
1. **Control Plane Konzept** passt zu VIA Service Registry/Orchestrierung
2. **Multi-Protokoll Support** notwendig (SOME/IP, DDS, OPC UA)
3. **Data Modeling** zentral für M3 Metamodell
4. **Virtualisierung** wichtig für M2/M1 Deployment
5. **IPC Mechanisms**: Shared Memory, Socket, D-Bus → VIA C++ Interface
