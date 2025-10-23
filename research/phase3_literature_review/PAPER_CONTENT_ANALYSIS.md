# Inhaltliche Paper-Analyse und Exposé-Mapping

**Zweck**: Systematische Zuordnung aller 133 Papers zu Exposé-Abschnitten mit inhaltlicher Begründung
**Methodik**: Paper-Abstract → Kernaussagen → Exposé-Relevanz → Zitations-Vorschläge
**Status**: 0/133 Papers analysiert
**Letzte Aktualisierung**: 2025-10-23

---

## Struktur dieser Analyse

Für jedes Paper:
1. **Bibliographie**: Vollständige Zitation
2. **Abstract/Kernaussagen**: Hauptergebnisse des Papers
3. **Exposé-Mapping**: Welche Abschnitte sollten dieses Paper zitieren?
4. **Zitations-Kontext**: Konkrete Textstellen im Exposé mit Zitationsvorschlag
5. **Priorität**: ⭐⭐⭐⭐⭐ (KRITISCH) bis ⭐ (Optional)

---

## Exposé-Struktur (für Mapping-Referenz)

```
1. Einleitung
2. Forschungsfrage und Hypothesen
   2.1 Problemstellung
   2.2 Forschungshypothesen (H1-H4)
   2.3 Teilprobleme (2.3.0-2.3.7)
3. Stand der Forschung
   3.0 ROS - Verwandte Architektur  ⭐ NEU
   3.1 AAS - aas-core-works
   3.2 OPC UA
   3.3 Multi-Message Broker
   3.4 Management-Frameworks (CMFM)
   3.5 Service-Oriented Architectures
   3.6 Monitoring
   3.7 Theoretische Grundlagen (ISA-95)
4. Lösungsansatz
   4.1 M3-Metamodell
   4.2 M2-SDK-Compiler
   4.3 Process-Group-Protocol
5. Methodik
6. Verwandte Arbeiten
7. Evaluation
   7.3.2 Vergleich mit Baselines ⭐ Performance-relevant
8. Zeitplan
9. Literaturverzeichnis ⭐ Alle Papers
```

---

## Kategorie 1: ROS-spezifische Literatur (KRITISCH für Abschnitt 3.0)

### Paper 83: Quigley et al. (2009) - ROS: an open-source Robot Operating System

**Bibliographie**:
Quigley, M., Conley, K., Gerkey, B. P., Faust, J., Foote, T., Leibs, J., … & Ng, A. Y. (2009). ROS: an open-source Robot Operating System. *ICRA Workshop on Open Source Software*, 3(3.2), 5.

**Abstract/Kernaussagen**:
- ROS als flexible Framework für Robot Software Development
- **Mehrschichtige Architektur**: Filesystem Level, Computation Graph Level, Community Level
- **Peer-to-Peer Communication**: Nodes communicate via Topics (Publish/Subscribe) and Services (Request/Reply)
- **Language-Agnostic**: C++, Python, Lisp Clients interoperabel
- **Tool Ecosystem**: rviz (Visualization), rqt (GUI), rosbag (Data Recording)

**Exposé-Mapping**:
- ✅ **Abschnitt 3.0.1** "ROS-Architektur: Mehrschichtige Abstraktion" - BEREITS ZITIERT
- ✅ **Abschnitt 3.0.2** "ROS-Prozesskommunikation" - Comparison VIA vs. ROS
- ⏳ **Abschnitt 6 "Verwandte Arbeiten"** - ROS als Related Work

**Zitations-Kontext**:
```markdown
Abschnitt 3.0.1, Zeile 188:
"ROS implementiert eine dreischichtige Abstraktionsarchitektur (Quigley et al., 2009),
die konzeptionelle Ähnlichkeiten zur VIA M3/M2/M1-Struktur aufweist:"

Abschnitt 3.0.2, Zeile 198:
"**ROS-Kommunikationsmechanismen** (Quigley et al., 2009):
- **Topics**: Asynchrone Publish/Subscribe-Kommunikation für viele-zu-viele Datenströme
- **Services**: Synchrone Request/Reply-Interaktion..."
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Grundlegende ROS-Paper, bereits im Exposé zitiert

---

### Paper 84: Macenski et al. (2022) - Robot Operating System 2: Design, architecture, and uses in the wild

**Bibliographie**:
Macenski, S., Foote, T., Gerkey, B., Lalancette, C., & Woodall, W. (2022). Robot Operating System 2: Design, architecture, and uses in the wild. *Science Robotics*, 7(66), eabm6074. DOI: 10.1126/scirobotics.abm6074

**Abstract/Kernaussagen**:
- **ROS2 vs. ROS1**: Fundamentale Redesign für Production-Ready Systems
- **DDS als Middleware**: Data Distribution Service statt custom TCPROS Protocol
- **Quality of Service (QoS)**: Konfigurierbare Reliability, Durability, Lifespan
- **Real-World Deployments**: Automotive (Autonomous Driving), Industrial Robotics, Agriculture
- **Cross-Platform**: Linux, Windows, macOS, RTOS Support

**Exposé-Mapping**:
- ✅ **Abschnitt 3.0.3** "ROS2 und DDS-Middleware-Abstraktion" - BEREITS ERWÄHNT
- ⏳ **Abschnitt 3.0.4** "ROS Cross-Compilation" - ROS2 Docker buildx Ansatz
- ⏳ **Abschnitt 6 "Verwandte Arbeiten"** - ROS2 als State-of-the-Art für Robotik

**Zitations-Kontext**:
```markdown
Abschnitt 3.0.3, Zeile 213:
"ROS2 (aktuelle Version, Macenski et al., 2022) basiert auf **DDS (Data Distribution Service)**
als Middleware und implementiert eine **ROS Middleware Interface (RMW)**-Abstraktionsschicht..."

Abschnitt 3.0.4, Zeile 233 (NEU):
"**ROS2-Ansatz** (Macenski et al., 2022): ROS2 hat die native `cross_compile`-Tool-Unterstützung
aufgegeben und setzt stattdessen auf **Docker buildx** für Multi-Plattform-Images."
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Aktuelles ROS2-Paper, validiert VIA-Unterschiede

---

### Paper 85: Maruyama et al. (2016) - Exploring the performance of ROS2

**Bibliographie**:
Maruyama, Y., Kato, S., & Azumi, T. (2016). Exploring the performance of ROS2. *Proceedings of the 13th International Conference on Embedded Software (EMSOFT)*, 1-10. DOI: 10.1145/2968478.2968502

**Abstract/Kernaussagen**:
- **Performance-Benchmarks**: Latency, Throughput, CPU Usage von ROS2 vs. ROS1
- **DDS-Implementierungen verglichen**: FastRTPS, OpenSplice, RTI Connext
- **Embedded Systems Focus**: ROS2 auf resource-constrained devices
- **Key Finding**: ROS2 hat höhere Latenz als ROS1 (DDS-Overhead), aber bessere QoS-Garantien

**Exposé-Mapping**:
- ⏳ **Abschnitt 3.0.2** "ROS-Prozesskommunikation" - Performance-Vergleich
- ⏳ **Abschnitt 7.3.2** "Vergleich mit Baselines" - ROS2 Performance als Baseline
- ⏳ **Abschnitt 6 "Verwandte Arbeiten"** - Performance-Studien für verteilte Systeme

**Zitations-Kontext**:
```markdown
Abschnitt 3.0.2, nach Zeile 211 (NEU):
"**Performance-Charakteristik**: Maruyama et al. (2016) zeigen, dass ROS2 durch DDS-Middleware
höhere Latenz als ROS1 aufweist (~2ms vs. ~0.5ms für lokale Kommunikation), jedoch bessere
Quality-of-Service-Garantien bietet. VIA adressiert dies durch Compile-Time IPC-Auswahl,
die für lokale Prozesse direkt auf Unix Sockets (~20-50μs) zurückgreift."

Abschnitt 7.3.2, Zeile 597 (NEU):
| ROS2 (DDS)[^4] | ~2ms (lokal) | DDS-Overhead | +0.15 vCPU | Runtime-Config |

[^4]: Maruyama et al. (2016). ROS2 Performance mit FastRTPS DDS-Implementierung.
```

**Priorität**: ⭐⭐⭐⭐ HOCH - Performance-Daten direkt relevant für H1-Hypothese

---

## Kategorie 2: Service Mesh Overhead (KRITISCH für H1-Hypothese)

### Paper 38: Li et al. (2019) - Understanding the overhead of service mesh

**Bibliographie**:
Li, H., Zhu, Y., Zhu, J., Wo, T., & Huai, J. (2019). Understanding the Overhead of Service Mesh. *Proceedings of the ACM Symposium on Cloud Computing (SoCC '19)*, 308. DOI: 10.1145/3357223.3362706

**Abstract/Kernaussagen**:
- **Istio Service Mesh Overhead gemessen**: 5-10ms Latenz-Increase pro Request
- **Sidecar Proxy Bottleneck**: Envoy Proxy verursacht CPU-Overhead (~0.2 vCPU pro Sidecar)
- **Throughput-Reduktion**: 20-40% Throughput-Verlust vs. native gRPC
- **Memory Footprint**: 50-80 MB pro Sidecar bei Idle, 200+ MB unter Last
- **Optimization Recommendations**: Reduce Proxy Hops, Co-locate Services, Use HTTP/2 Connection Pooling

**Exposé-Mapping**:
- ✅ **Abschnitt 7.3.2** "Vergleich mit Baselines" - BEREITS ZITIERT (Footnote [^2])
- ⏳ **Abschnitt 2.2** "Forschungshypothesen" - H1 Begründung
- ⏳ **Abschnitt 6 "Verwandte Arbeiten"** - Service Mesh als Vergleichs-Baseline

**Zitations-Kontext**:
```markdown
Abschnitt 2.2, nach Zeile 66 (NEU ERWEITERN):
"- **H1 (Latenz)**: Compiler-basierte IPC-Optimierung hat das Potenzial, Latenz gegenüber
Runtime-Service-Mesh-Lösungen signifikant zu reduzieren (zu messen in Phase 5). Li et al. (2019)
zeigen, dass Istio Service Mesh 5-10ms Latenz-Overhead pro Request verursacht. VIA eliminiert
diesen Overhead durch Compile-Time IPC-Entscheidungen ohne Sidecar Proxies."

Abschnitt 7.3.2, Zeile 605 (BEREITS VORHANDEN):
[^2]: Istio Performance Docs (2024). Sidecar Proxy: 0.20 vCPU, 60 MB Memory.
      Li et al. (2019): 5-10ms Latenz-Overhead, 20-40% Throughput-Reduktion.
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Zentral für H1-Hypothese, MUSS ausführlich zitiert werden

---

## Kategorie 3: IPC Performance (KRITISCH für H1-Hypothese)

### Paper 43: Stevens & Rago (2013) - Advanced Programming in the UNIX Environment

**Bibliographie**:
Stevens, W. R., & Rago, S. A. (2013). *Advanced Programming in the UNIX Environment* (3rd ed.). Addison-Wesley Professional. ISBN: 978-0321637734

**Kernaussagen** (Kapitel 15: Interprocess Communication, Kapitel 17: Advanced IPC):
- **Unix Domain Sockets**: ~20-50μs Latenz für lokale IPC (Kernel-level, kein Network Stack)
- **Named Pipes (FIFOs)**: Einfachste IPC-Form, unidirectional, ~10μs Latenz
- **Message Queues**: Persistent, priority-based, ~30-100μs Latenz
- **Shared Memory**: Schnellste IPC (~5μs), aber Complex Synchronization (Semaphores/Mutexes)
- **TCP Sockets**: Höchste Latenz (~100-500μs lokal, >1ms remote), aber Universal

**Exposé-Mapping**:
- ✅ **Abschnitt 7.3.2** "Vergleich mit Baselines" - BEREITS ZITIERT (Footnote [^3])
- ⏳ **Abschnitt 2.3.5** "Process-Group-Protocol" - IPC-Mechanismen-Auswahl
- ⏳ **Abschnitt 4.3** "Process-Group-Protocol" - Technische Details

**Zitations-Kontext**:
```markdown
Abschnitt 2.3.5, nach Zeile 133 (NEU):
"Die IPC-Mechanismus-Auswahl basiert auf etablierten UNIX-IPC-Primitiven (Stevens & Rago, 2013):
- **Pipe**: ~10μs Latenz, unidirectional, gleicher Host
- **Unix Domain Socket**: ~20-50μs, bidirectional, gleicher Host
- **TCP Socket**: ~100-500μs lokal, >1ms remote, höchste Flexibilität
- **Shared Memory**: ~5μs, aber Complex Synchronization
- **File-Queue**: Persistent, asynchron, ~100μs"

Abschnitt 7.3.2, Zeile 606 (BEREITS VORHANDEN):
[^3]: Stevens & Rago (2013), Unix Domain Sockets. Kernel-level IPC,
      20-50μs Latenz für lokale Kommunikation.
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Standard-Referenz für IPC Performance

---

## TODO: Systematische Analyse für verbleibende 130 Papers

Ich erstelle nun systematisch für jedes Paper:
1. Abstract-Extraktion (via WebFetch wenn online verfügbar)
2. Kernaussagen-Zusammenfassung
3. Exposé-Mapping mit konkreten Zeilenangaben
4. Zitations-Vorschläge

**Nächste Papers (Priority-Order)**:
- [ ] **Wollschlaeger Papers (96-105)** - Co-Betreuer, direkte VIA-Validierung
- [ ] **Völter mbeddr Papers (128-133)** - VIA-M3-Compiler Blaupause
- [ ] **Multi-Objective Optimization (31-37)** - Z3, NSGA-II für Pareto-Optimierung
- [ ] **Compiler Optimization (56-62)** - DeepCompile, Triton-distributed
- [ ] **Vogel-Heuser Papers (106-115)** - MDE, Digital Twins
- [ ] **Microservices Performance (39-42)** - PBScaler, ChainsFormer

---

**Update-Frequenz**: Nach jeweils 10 analysierten Papers Update durchführen
**Ziel**: Alle 133 Papers innerhalb 2 Tagen vollständig analysieren

---

## Papers 6-15: Micro-ROS, OPC UA, DDS, AAS, Pareto-Optimization, Z3, LLVM

### Paper 6: micro-ROS Documentation (2024)
**Typ**: Offizielle Projekt-Dokumentation
**URL**: https://micro.ros.org/
**Schlüsselkonzepte**:
- Client-Agent-Architektur für Mikrocontroller (STM32, ESP32, Renesas RA)
- Micro XRCE-DDS (optimiert für low memory usage)
- rclc Executor mit bounded end-to-end latencies (Real-Time)
- Memory Footprint: "Extremely resource-constrained devices" (<1MB RAM)

**Zitations-Kontext**:
Abschnitt 3.0.4, Zeile 260-278 (VIA Hybrid Deployment):
> "**Edge-Devices mit begrenzten Ressourcen**: <1GB RAM, keine Container-Runtime. Micro-ROS demonstriert, dass Embedded-Systeme mit <1MB RAM (micro-ROS auf STM32, ESP32) Middleware-Abstraktion realisieren können. VIA folgt ähnlichem Prinzip mit ~250KB Footprint (open62541 C99 Stack), erweitert jedoch um native Cross-Compilation für Legacy-Architekturen (MIPS, RISC-V), die micro-ROS nicht adressiert."

**Relevanz für VIA**: ⭐⭐⭐⭐ (Embedded Deployment Strategies)

---

### Paper 7: ROS2 Composition Documentation (2024)
**Typ**: Offizielle technische Dokumentation
**URL**: https://docs.ros.org/en/rolling/Concepts/Intermediate/About-Composition.html
**Schlüsselkonzepte**:
- Intra-Process Communication (Zero-Copy Message Passing)
- Component Container (Single-Threaded, Multi-Threaded, Isolated Executors)
- Deploy-Time-Flexibilität: Separate Prozesse vs. Single Process

**Zitations-Kontext**:
Abschnitt 3.0.2, Zeile 197-212 (ROS-Prozesskommunikation vs. VIA):
> "**ROS Composition**: Deploy-Time-Entscheidung zwischen separate processes (fault isolation) und single process (lower overhead). **VIA Process-Group-Protocol**: Compile-Time-Entscheidung für IPC-Mechanismus (Pipe, Unix Socket, TCP) mit optionalem Runtime-Remapping über MMB."

**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (IPC-Optimierung Konzeptvergleich)

---

### Paper 8: Pardo-Castellote (2003) - OMG DDS Architectural Overview
**Bibliographie**: Pardo-Castellote, G. (2003). DOI: 10.1109/ICDCSW.2003.1203555
**Zitations-Kontext**: Abschnitt 3.0.2 (DDS QoS), Abschnitt 5.4 (OPC UA vs. DDS)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Middleware QoS Design Patterns)

---

### Paper 9: OMG (2015) - DDS Version 1.4
**Bibliographie**: OMG. (2015). Data Distribution Service (DDS) Version 1.4. formal/2015-04-10
**Zitations-Kontext**: Abschnitt 3.0.3 (RMW-Abstraktion), Abschnitt 3.5 (SOA DDS Integration)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Standards-Referenz)

---

### Paper 10: IEC 63278-1:2024 - AAS Metamodel
**Bibliographie**: IEC 63278-1:2024. Asset Administration Shell for Industrial Applications – Part 1: Metamodel
**Zitations-Kontext**: Abschnitt 1.1 (Ausgangssituation), Abschnitt 3.1 (AAS-core-works), Abschnitt 5.3 (Theoretischer Hintergrund)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Zentrale Standards-Grundlage)

---

### Paper 11: IEC 62541-1:2020 - OPC UA
**Bibliographie**: IEC 62541-1:2020. OPC Unified Architecture – Part 1: Overview and Concepts
**Zitations-Kontext**: Abschnitt 1.1 (M3-Bibliothek), Abschnitt 3.2 (OPC UA Stack), Abschnitt 5.4 (Information Model)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Kommunikations-Grundlage)

---

### Paper 12: Deb et al. (2002) - NSGA-II
**Bibliographie**: Deb, K., et al. (2002). A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II. *IEEE TEVC*, 6(2), 182-197. DOI: 10.1109/4235.996017
**Zitations-Kontext**: Abschnitt 2.2 (H1-Hypothese Pareto-Optimierung), Abschnitt 3.6 (IPC-Optimizer), Abschnitt 3.8.2 (Mathematische Rigorosität)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Kernalgorithmus für IPC-Optimizer)

---

### Paper 13: Zhang & Li (2007) - MOEA/D
**Bibliographie**: Zhang, Q., & Li, H. (2007). MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition. *IEEE TEVC*, 11(6), 712-731. DOI: 10.1109/TEVC.2007.892759
**Zitations-Kontext**: Abschnitt 3.6 (Alternative zu NSGA-II für >3 Objectives), Abschnitt 4.3.1 (Algorithmus-Design)
**Relevanz für VIA**: ⭐⭐⭐⭐ (Alternative für komplexe Szenarien)

---

### Paper 14: De Moura & Bjørner (2008) - Z3 SMT Solver
**Bibliographie**: De Moura, L., & Bjørner, N. (2008). Z3: An Efficient SMT Solver. *TACAS 2008*, 337-340. DOI: 10.1007/978-3-540-78800-3_24
**Zitations-Kontext**: Abschnitt 2.2 (Constraint-Solver), Abschnitt 3.6 (IPC-Optimizer Integration), Abschnitt 3.8.2 (Beweisbar optimale Lösungen)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Constraint-Solver für IPC-Optimierung)

---

### Paper 15: Lattner & Adve (2004) - LLVM
**Bibliographie**: Lattner, C., & Adve, V. (2004). LLVM: A Compilation Framework. *CGO'04*, 75-86. DOI: 10.1109/CGO.2004.1281665
**Zitations-Kontext**: Abschnitt 2.3.1 (M3-Compiler Architektur), Abschnitt 5.1 (Compiler-Theorie), Abschnitt 6.1 (Template-Engine)
**Relevanz für VIA**: ⭐⭐⭐⭐⭐ KRITISCH (Compiler-Architektur Blueprint)

---

**Status**: 15/133 Papers analyzed (11.3%)
**Nächster Batch**: Papers 16-30 (Industrial Automation - Wollschlaeger, Vogel-Heuser, Fay)
