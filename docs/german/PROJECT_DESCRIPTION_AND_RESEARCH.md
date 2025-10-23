# Exposé: Analyse eines Forschungsthemas - Prozesskommunikation

**Titel**: VIA - Virtual Industry Automation: Self-Modeling and Building Systems for Industry 4.0

**Autor**: Benjamin-Elias Probst
**Betreuer**: Prof. Dr.-Ing. habil. Martin Wollschlaeger, Dr.-Ing. Frank Hilbert, Santiago Soler Perez Olaya
**Institution**: Technische Universität Dresden, Fakultät Informatik
**Datum**: Oktober 2025

---

_Hinweis: Dies ist eine Kopie des vollständigen Forschungsexposés aus `playbooks/Analyse_eines_Forschungsthemas_Expose.md` für die Projektdokumentation. Das Original in playbooks/ dient weiterhin als Arbeitsdokument._

---

Für die vollständige deutsche Fassung (675 Zeilen) des Forschungsexposés siehe bitte:
**`playbooks/Analyse_eines_Forschungsthemas_Expose.md`**

Das Exposé umfasst:
- Kapitel 1: Einleitung und Motivation (Ausgangssituation, Vision Industrie 5.0, Forschungslücke)
- Kapitel 2: Problemstellung und Forschungsfrage (VIA-Gesamtsystem, Process-Group-Protocol, 8 Teilprobleme)
- Kapitel 3: Stand der Forschung (AAS, OPC UA, MMB, CMFM, SOA, IPC & Service Mesh)
- Kapitel 4: Zielsetzung und Forschungsmethodik (Hauptziel, Teilziele, 6-Phasen-Plan)
- Kapitel 5: Theoretischer Hintergrund (Compiler-Theorie, Metamodelle, AAS, OPC UA, CMFM)
- Kapitel 6: Konzeptioneller Ansatz (VIA-Hauptprogramm, M3-Compiler, M2-SDK-Compiler, M1-Deployer, Sub-Protokolle)
- Kapitel 7: Erwartete Ergebnisse (Wissenschaftliche Beiträge, Praktische Ergebnisse, Use-Case Automobilproduktion)
- Kapitel 8: Zeitplan (6 Phasen, 24 Wochen)
- Kapitel 9: Literaturverzeichnis (27 Quellen)

## Zusammenfassung

VIA (Virtual Industry Automation) ist ein Forschungsprojekt an der TU Dresden, das einen **selbst-kompilierenden Bootstrap-Mechanismus** für Industrie 4.0 Automatisierung entwickelt. Das System transformiert Metamodell-Definitionen durch eine Compiler-Kette (M3→M2→M1) in deployed Industriesysteme für 50.000+ Edge-Geräte.

### Zentrale Forschungsfrage

> Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?

### Kernkomponenten

#### 1. VIA-M3-Compiler (Metamodell → SDK)
- **Input**: AAS IEC 63278 Textspezifikation, OPC UA IEC 62541, VIA-Extensions
- **Verarbeitung**: C++20/23 Metaprogramming, Custom Template-Engine in AAS-lang, Protobuf als M3-Interpreter
- **Output**: C++ SDK, OPC UA NodeSet XML, Protobuf `.proto` Files

#### 2. VIA-M2-SDK-Compiler (SDK → Kundensystem) → **Forschungskern**
- **Input**: Kundenprojekt `.via` Dateien, Optional: Netzwerk-Topologie
- **Verarbeitung**:
  - Network Discovery (SNMP/OPC UA/Modbus Scanner)
  - **IPC Optimizer**: Graph-basierte Compile-Time-Optimierung (Pareto-Frontier)
  - Test Generator: Automatische Tests aus M3 Constraints
- **Output**: C++ Gesamtprojekt, Kubernetes Manifests, Edge-Modules

#### 3. VIA-M1-System-Deployer (System → Produktion)
- **Input**: M1 Systemprojekt, Deployment-Targets (MIPS, RISC-V, ARM, x86, etc.)
- **Verarbeitung**:
  - Cross-Compilation (Multi-Architektur Toolchain Management)
  - Horse-Rider-Deployment (C++23 Modules, Hot-Reload, Canary)
  - Distributed Build (parallele Builds über GitHub Runners)
- **Output**: Deployed System für >50.000 Edge-Geräte, Digital Twin

#### 4. Sub-Protokolle unter OPC UA
- **Edge-Group-Protocol**: Virtuelle Netzwerkgruppen, hierarchische Edgegeräte-Gruppierung
- **Deploy-Protocol**: Versionierung, Systemupdates, Telemetrie, In-the-Loop Selbstoptimierung
- **Process-Group-Protocol** (Forschungsfokus): IPC-Optimierung, Pareto-Optimierung (Latenz/Durchsatz/Ressourcen)

### Hypothesen

- **H1**: Compiler-basierte IPC-Optimierung reduziert Latenz um >30% gegenüber Runtime-Service-Mesh
- **H2**: Statische Positionierung erreicht 90% der Effizienz dynamischer Orchestrierung
- **H3**: Process-Group-Protocol skaliert linear bis 100.000 Services
- **H4**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um 60%

### Wissenschaftlicher Mehrwert

1. **M3-Bibliotheks-Architektur**: MMB als wiederverwendbare M3-Bibliothek, Protokoll-Komposition
2. **Pareto-Optimierung**: Formal lösbares Optimierungsproblem mit Z3 Constraint-Solver
3. **Autonome Systeme**: In-the-Loop Selbstoptimierung via Telemetrie-Feedback
4. **Geschachtelte Sicherheit**: Rekursive Sicherheitsstufen pro Protokoll-Ebene
5. **Interdisziplinär**: Brückenschlag Compiler-Design ↔ Industrieautomatisierung

### Technologie-Stack

- **Sprachen**: C++20/23, AAS-lang (custom DSL), Protobuf
- **Protokolle**: OPC UA (IEC 62541), gRPC, IPC-Mechanismen
- **Deployment**: Kubernetes, C++23 Modules (Horse-Rider pattern)
- **Optimierung**: Z3 Constraint Solver, Pareto-Optimierung
- **Architekturen**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc

### Zeitplan (24 Wochen)

- **Phase 1**: Research & Analyse ✅ ABGESCHLOSSEN (4 Wochen)
- **Phase 2**: Playbook & M3-Metamodell-Design ⏳ IN PROGRESS (2 Wochen)
- **Phase 3**: M2-SDK-Compiler Prototyp mit IPC-Optimizer (6 Wochen)
- **Phase 4**: Benchmark-Suite & Use-Case (4 Wochen)
- **Phase 5**: Evaluation & Vergleichsmessungen (4 Wochen)
- **Phase 6**: Dokumentation & Publikation (4 Wochen)

---

**Für vollständige Details, alle Kapitel und Literaturverzeichnis siehe**:
`playbooks/Analyse_eines_Forschungsthemas_Expose.md` (675 Zeilen)
