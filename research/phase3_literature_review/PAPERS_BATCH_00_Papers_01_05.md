# Paper Batch 00: Papers 1-5 (Foundation Papers)

**Titel**: ROS Foundation, Service Mesh Overhead, IPC Performance Baselines
**Zeitraum**: 2009-2022
**Hauptthemen**:
- ROS/ROS2 Architecture (Quigley 2009, Macenski 2022, Maruyama 2016)
- Service Mesh Overhead (Li et al. 2019 - KRITISCH für H1)
- Unix IPC Performance (Stevens & Rago 2013 - KRITISCH für H1)

**Status**: 5/5 Papers vollständig analysiert ✅
**Kritische Papers (⭐⭐⭐⭐⭐)**: 5/5 Papers (alle KRITISCH)

**Mapping**:
- Paper 83 = Paper 1: Quigley et al. (2009) - ROS
- Paper 84 = Paper 2: Macenski et al. (2022) - ROS2
- Paper 85 = Paper 3: Maruyama et al. (2016) - ROS2 Performance
- Paper 38 = Paper 4: Li et al. (2019) - Service Mesh Overhead
- Paper 43 = Paper 5: Stevens & Rago (2013) - Unix IPC

---

## Kategorie 1: ROS-spezifische Literatur (KRITISCH für Abschnitt 3.0)

### Paper 83 (=Paper 1): Quigley et al. (2009) - ROS: an open-source Robot Operating System

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

Abschnitt 3.0.7, Zeile 345:
"Die ROS-Architektur demonstriert die **Machbarkeit metamodell-basierter Abstraktion** für komplexe
verteilte Systeme und validiert zentrale VIA-Design-Entscheidungen:
- **Mehrschichtige Abstraktion** ist in der Praxis bewährt (ROS: >10 Jahre Produktionseinsatz, Quigley et al. 2009)"
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Grundlegende ROS-Paper, bereits im Exposé zitiert

---

### Paper 84 (=Paper 2): Macenski et al. (2022) - Robot Operating System 2

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

Abschnitt 3.0.7, Zeile 346:
"- **Middleware-Abstraktion** (RMW) zeigt, dass heterogene Implementierungen unter einheitlicher
API integrierbar sind (Macenski et al. 2022)"
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Aktuelles ROS2-Paper, validiert VIA-Unterschiede

---

### Paper 85 (=Paper 3): Maruyama et al. (2016) - ROS2 Performance

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
Abschnitt 7.3.2, Baseline Table (NEU):
| ROS2 (DDS)[^4] | ~2ms (lokal) | DDS-Overhead | +0.15 vCPU | Runtime-Config |

[^4]: Maruyama et al. (2016). ROS2 Performance mit FastRTPS DDS-Implementierung.
```

**Priorität**: ⭐⭐⭐⭐ HOCH - Performance-Daten direkt relevant für H1-Hypothese

---

## Kategorie 2: Service Mesh Overhead (KRITISCH für H1-Hypothese)

### Paper 38 (=Paper 4): Li et al. (2019) - Service Mesh Overhead

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
- ⏳ **Abschnitt 2.2** "Forschungshypothesen" - H1 Begründung ERWEITERN
- ⏳ **Abschnitt 3.6** "IPC-Optimizer" - Service Mesh als Motivation
- ⏳ **Abschnitt 6 "Verwandte Arbeiten"** - Service Mesh als Vergleichs-Baseline

**Zitations-Kontext**:
```markdown
Abschnitt 2.2, Zeile 57-61 (ERWEITERN):
"- **H1 (Latenz)**: Compiler-basierte IPC-Optimierung hat das Potenzial, Latenz gegenüber
Runtime-Service-Mesh-Lösungen signifikant zu reduzieren (zu messen in Phase 5). Li et al. (2019)
zeigen, dass Istio Service Mesh 5-10ms Latenz-Overhead pro Request verursacht. VIA eliminiert
diesen Overhead durch Compile-Time IPC-Entscheidungen ohne Sidecar Proxies."

Abschnitt 3.6, Zeile 410-415:
"Der IPC-Optimizer in VIA adressiert das Service-Mesh-Overhead-Problem (Li et al. 2019):
Während Istio/Linkerd 5-10ms Latenz-Overhead durch Sidecar Proxies verursachen, berechnet
VIA IPC-Mechanismen zur Compile-Zeit ohne Runtime-Proxy-Hops."

Abschnitt 7.3.2, Zeile 605 (BEREITS VORHANDEN):
[^2]: Istio Performance Docs (2024). Sidecar Proxy: 0.20 vCPU, 60 MB Memory.
      Li et al. (2019): 5-10ms Latenz-Overhead, 20-40% Throughput-Reduktion.
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Zentral für H1-Hypothese, MUSS ausführlich zitiert werden

---

## Kategorie 3: IPC Performance (KRITISCH für H1-Hypothese)

### Paper 43 (=Paper 5): Stevens & Rago (2013) - Unix IPC

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
- ⏳ **Abschnitt 3.6** "IPC-Optimizer" - IPC-Mechanismen Performance-Charakteristik
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

Abschnitt 3.6, Zeile 410:
"Der M2-Compiler wählt zur Compile-Zeit optimale IPC-Mechanismen basierend auf
Performance-Charakteristiken (Stevens & Rago 2013): Unix Domain Sockets (20-50μs)
für lokale Prozesse, TCP für remote Kommunikation, Shared Memory für Bulk Data Transfer."

Abschnitt 7.3.2, Zeile 606 (BEREITS VORHANDEN):
[^3]: Stevens & Rago (2013), Unix Domain Sockets. Kernel-level IPC,
      20-50μs Latenz für lokale Kommunikation.
```

**Priorität**: ⭐⭐⭐⭐⭐ KRITISCH - Standard-Referenz für IPC Performance

---

**Zusammenfassung Batch 00**:
- Alle 5 Papers sind **KRITISCH** für VIA-Exposé
- Papers 83-85 (ROS) validieren VIA-Design-Entscheidungen
- Paper 38 (Li et al.) ist **zentral** für H1-Hypothese (Service Mesh Overhead)
- Paper 43 (Stevens & Rago) ist **zentral** für H1-Hypothese (IPC Performance Baseline)
