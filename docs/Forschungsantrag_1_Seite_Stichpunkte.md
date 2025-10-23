# Forschungsantrag: VIA - Virtual Industry Automation

**Promotionsvorhaben an der TU Dresden, Fakultät Informatik**

---

## Basisdaten

**Titel**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0
**Fokus**: Compile-Time-Optimierung von Prozesskommunikation in Industrie 4.0-Systemen

**Doktorand**: Benjamin-Elias Probst
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger (TU Dresden, Lehrstuhl für Industrielle Kommunikationstechnik)
**Co-Betreuer**: Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Datum**: Oktober 2025

---

## Forschungsfrage

> **Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?**

**Kernproblem**: Service-Mesh-Lösungen (Istio, Linkerd) wählen IPC-Mechanismen zur Laufzeit → 5-10ms Overhead durch Sidecar Proxies. VIA untersucht Compile-Time-Optimierung zur Latenzreduktion bei gleichzeitiger industrieller Skalierbarkeit (>50.000 Edge-Devices).

---

## Forschungslücke

**Bisherige Ansätze**:
- aas-core-works (AAS IEC 63278): Python-Skripte für Code-Generierung, keine Production-Grade Compiler
- ROS2: Runtime-IPC-Optimierung via DDS QoS, keine Compile-Time-Analyse
- Service Mesh (Istio): Dynamische Runtime-Orchestrierung, 5-10ms Latenz-Overhead

**Lücke**:
1. Keine wissenschaftliche Untersuchung: **Compile-Time IPC-Optimierung** für Mikroservice-Kommunikation
2. Kein metamodell-basiertes Framework für **statische Positionierungsentscheidungen**
3. Keine **Pareto-Optimierung** (Latenz, Durchsatz, Ressourcenverbrauch) zur Compile-Zeit
4. Keine **standardisierten OPC UA Sub-Protokolle** für Prozessgruppierung und Deployment-Management

---

## Hypothesen (zu testen in Phase 5)

- **H1 (Latenz)**: Compile-Time IPC-Optimierung → potenziell 100-500x niedrigere Latenz vs. Istio (Unix Sockets: ~20-50μs vs. Istio: 5-10ms)
- **H2 (Effizienz)**: Statische Positionierung approximiert dynamische Runtime-Orchestrierung unter definierten Constraints
- **H3 (Skalierbarkeit)**: Process-Group-Protocol mit hierarchischer Gruppierung skaliert auf ≥100.000 Services
- **H4 (Entwicklungszeit)**: Metamodell-basierte Abstraktion reduziert manuelle Entwicklungszeit messbar (Ziel: >75%)

---

## Wissenschaftliche Beiträge

### Theoretische Beiträge:
1. **Metamodell-Extension für Prozesskommunikation**: AAS M3-Erweiterung mit IPC-Typen (Pipe, Socket, TCP, FileQueue, Thread) als formale Modellelemente
2. **Compiler-Optimierungsalgorithmus**: Graph-basierter Ansatz mit Constraint-Solver (Z3) für IPC-Mechanismus-Auswahl
3. **Process-Group-Protocol**: OPC UA Sub-Protokoll-Spezifikation für industrielle Mikroservice-Orchestrierung
4. **Pareto-Optimierung**: Multi-Objective-Optimization (Latenz, Durchsatz, Ressourcen) zur Compile-Zeit

### Praktische Beiträge:
5. **M2-SDK-Compiler Prototyp**: Open-Source-Implementierung in C++20/23 mit IPC-Optimizer
6. **Benchmark-Suite**: Systematischer Vergleich Compiler-Optimierung vs. Service Mesh vs. manuelle Konfiguration
7. **Use-Case**: SCADA+MES+PLC-Edge-Integration (100 PLC-Devices, 10 MES-Server, Automobilproduktion)
8. **Standardisierungsvorschlag**: VIA Custom OPC UA Companion Specification für OPC Foundation

### Interdisziplinärer Mehrwert:
- **Compiler-Design ↔ Industrieautomatisierung**: Anwendung von Compiler-Optimierungstechniken (M3/M2/M1 Metamodell-Kette, Constraint-Solving) auf Industrie 4.0-Probleme
- **Autonome Systeme**: In-the-Loop Selbstoptimierung mit Telemetrie-Feedback (CPU, RAM, Latenz) → automatische Kubernetes-Lastverteilung

---

## Methodik

**Forschungsansatz**: Ingenieurwissenschaftlich (Requirements → Design → Prototyp → Evaluation)

### Phase 1 (4 Wochen) ✅ ABGESCHLOSSEN:
- Research & Analyse: AAS, OPC UA, IPC-Mechanismen, Service Mesh
- Literaturreview: 133 Papers (IEEE/ACM/Springer, arXiv)

### Phase 2 (2 Wochen) ✅ ABGESCHLOSSEN:
- Playbook-Erstellung: 8 Teilprobleme dokumentiert (`playbooks/`)
- Exposé-Fertigstellung: 1202 Zeilen, vollständige Konsistenzprüfung

### Phase 3 (6 Wochen) → NÄCHSTE PHASE:
- **M2-SDK-Compiler Prototyp**: C++20/23 mit IPC-Optimizer
  - Woche 1-2: Graph-basierter Optimierungsalgorithmus
  - Woche 3-4: IPC-Mechanismus-Implementierung (5 Typen)
  - Woche 5-6: Process-Group-Protocol-Spezifikation (OPC UA)

### Phase 4 (4 Wochen):
- **Benchmark-Suite**: Latenz, Throughput, CPU, Memory
- **Use-Case**: Automobilproduktion (100 PLC + 10 MES + 3 SCADA)

### Phase 5 (4 Wochen):
- **Evaluation**: Vergleichsmessungen gegen Baselines (gRPC, Istio, UNIX Sockets)
- **Hypothesen-Validierung**: H1-H4 empirisch testen
- **Skalierungstest**: Mininet-Simulation (1.000 Nodes)

### Phase 6 (4 Wochen):
- **Publikation**: Paper für IEEE INDIN/ETFA
- **Standardisierung**: OPC Foundation Companion Spec Proposal

**Gesamtdauer**: 22 Wochen (circa 5 Monate) ab Start Phase 3

---

## Evaluationsumgebung

**Labor-Setup**:
- 3-Node Kubernetes Cluster (64 Core, 256 GB RAM, 10 Gbit/s Netzwerk)
- Mininet für virtuelle Netzwerktopologien (bis 1.000 Nodes)

**Benchmark-Szenarien**:
- **S1**: Lokale Prozesskette (5 Services, gleicher Host)
- **S2**: Verteilte Prozesskette (20 Services, 3 Hosts)
- **S3**: Skalierungstest (100.000 Services, hierarchische Gruppierung)
- **S4**: Real-World Use-Case (Industrieller SCADA+MES+PLC)

**Vergleichsbaselines**:
- Baseline 1: Manuell konfiguriertes gRPC (statisch)
- Baseline 2: Istio Service Mesh (dynamisch, Runtime-Overhead)
- Baseline 3: UNIX Sockets (optimal lokal, keine verteilte Orchestrierung)
- **VIA**: Compiler-optimiert (Pareto-Frontier)

**Metriken**:
- Latenz: End-to-End (P50, P95, P99 Perzentile)
- Throughput: Messages/s
- CPU-Last: % pro Service
- Memory Footprint: MB pro Service
- Entwicklungszeit: Manual vs. Metamodell-generiert (Stunden)

---

## Verwandte Arbeiten & Abgrenzung

**ROS (Robot Operating System)**:
- Ähnlichkeit: Mehrschichtige Abstraktion (Filesystem/Computation Graph/Community Level)
- **Unterschied**: ROS = Runtime-Optimierung (DDS QoS), VIA = **Compile-Time-Optimierung**
- Domäne: ROS für Robotik (dynamisch, 10-1.000 Nodes), VIA für Fabriken (statisch, 50.000+ Devices)

**Service Mesh (Istio/Linkerd)**:
- Ähnlichkeit: Mikroservice-Orchestrierung, Service Discovery
- **Unterschied**: Service Mesh = Runtime-Routing (5-10ms Overhead), VIA = **statische IPC-Entscheidung**

**aas-core-works (TU Dresden, Santiago Soler Perez Olaya)**:
- Ähnlichkeit: M3/M2/M1 Metamodell-Architektur, AAS IEC 63278
- **Unterschied**: aas-core = Python-Skripte, VIA = **produktionsreifer C++ Compiler**

**Multi-Message Broker (MMB, Santiago Soler Perez Olaya et al., IEEE ETFA 2024)**:
- Integration: MMB als **M3-Bibliothek** für VIA Sub-Protokolle (Edge-Group, Deploy, Process-Group)
- Brownfield-Integration: AID/AIMC-Mapping für Legacy-Geräte (Modbus, PROFIBUS)

---

## Standardkonformität

**Basis-Standards**:
- **IEC 63278-1:2024**: Asset Administration Shell (AAS) Metamodel
- **IEC 62541-1:2020**: OPC Unified Architecture (OPC UA)
- **ISA-95** (2010): Enterprise-Control System Integration

**Geplante Standardisierung**:
- **VIA Custom OPC UA Companion Specification**: Einreichung bei OPC Foundation
  - VIAProcessType, VIARouterType, VIASchedulerType, VIARegistryType
  - Process-Group-Protocol, Edge-Group-Protocol, Deploy-Protocol

---

## Limitationen

**L1**: Compile-Time-Optimierung erfordert statische Topologie (dynamische Änderungen → Neu-Compilation)
**L2**: M3-Modellelemente noch nicht in offizieller AAS-Spezifikation standardisiert
**L3**: Cross-Architektur-Performance variiert (MIPS vs. x86)
**L4**: Laborumgebung (3 Nodes) extrapoliert auf >50.000 Geräte (Simulation erforderlich)
**L5**: Hypothesen H1-H4 sind **zu testende Annahmen** (empirische Validierung in Phase 5)

---

## Publikationsstrategie

**Ziel-Konferenzen**:
- IEEE International Conference on Industrial Informatics (INDIN)
- IEEE Conference on Emerging Technologies and Factory Automation (ETFA)
- IEEE Industrial Cyber-Physical Systems (ICPS)

**Ziel-Journals** (optional):
- IEEE Transactions on Automation Science and Engineering
- Automatisierungstechnik (at - Automation Technology)

**Meilenstein**: Paper-Submission nach Phase 5 (Evaluation abgeschlossen)

---

## Erwartete Ergebnisse

### Minimales Erfolgskriterium:
- ✅ Metamodell-Extension für Prozesskommunikation (M3-Modellelemente spezifiziert)
- ✅ Process-Group-Protocol-Spezifikation (OPC UA Sub-Protokoll dokumentiert)
- ✅ Compiler-Optimierungsalgorithmus (Pareto-Optimierung formal beschrieben)
- ✅ Prototyp-Implementierung (M2-SDK-Compiler lauffähig)

### Optimales Erfolgskriterium:
- ✅ Alle H1-H4 bestätigt (Latenz, Effizienz, Skalierbarkeit, Entwicklungszeit)
- ✅ Benchmark-Suite zeigt signifikante Verbesserung vs. Istio Service Mesh
- ✅ Real-World Use-Case deployed (SCADA+MES+PLC-Edge-Integration)
- ✅ OPC Foundation akzeptiert VIA Companion Specification

**Wissenschaftlicher Wert unabhängig von H1-H4**: Selbst bei Fehlschlagen einzelner Hypothesen liefert die Arbeit fundamentale Beiträge zu Compile-Time-Optimierung für Industrie 4.0-Systeme.

---

## Kontakt & Repository

**GitHub Repository**: https://github.com/BEP-Venture-UG/VIA (geplant, derzeit privat)
**Projekt-Dokumentation**: `playbooks/` (8 Teilprobleme, 133 Papers)
**Exposé**: `playbooks/Analyse_eines_Forschungsthemas_Expose.md` (1202 Zeilen)

**E-Mail**: [Kontaktdaten einfügen]
**Institution**: TU Dresden, Fakultät Informatik, Lehrstuhl für Industrielle Kommunikationstechnik

---

**Status**: Bereit für Projektanmeldung | Phase 1+2 abgeschlossen | Phase 3 startet
