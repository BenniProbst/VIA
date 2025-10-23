# VIA - Architektur-Dokumentation

## Übersicht

VIA (Virtual Industry Automation) ist ein mehrstufiges Compiler-System für Industrie 4.0 Automatisierung, das Metamodell-Definitionen durch eine Compiler-Kette (M3’M2’M1) in deployed Industriesysteme für 50.000+ Edge-Geräte transformiert.

## Kernarchitektur

### Multi-Stage Compiler Chain

```
M3 Metamodel (AAS IEC 63278, OPC UA IEC 62541)
    “ VIA-M3-Compiler
M2 SDK (C++ SDK mit generierten Types & Services)
    “ VIA-M2-SDK-Compiler (IPC Optimizer)
M1 System Project (Kundenprojekt als C++ Gesamtprojekt)
    “ VIA-M1-System-Deployer
M0 Deployed System (Binaries auf >50.000 Edge-Devices)
```

### Komponenten

#### 1. VIA-M3-Compiler (Metamodel ’ SDK)
- **Input**: AAS IEC 63278 Textspezifikation (via SITL transformiert), OPC UA IEC 62541 als M3-Bibliothek, VIA-Extensions
- **Verarbeitung**: C++20/23 Metaprogramming, Custom Template-Engine in AAS-lang, Protobuf als M3-Interpreter
- **Output**: C++ SDK (`playbooks/VIA-M2-SDK/`), OPC UA NodeSet XML, Protobuf `.proto` Files

#### 2. VIA-M2-SDK-Compiler (SDK ’ Kundensystem)
- **Input**: Kundenprojekt `.via` Dateien, Optional: Netzwerk-Topologie via Network Discovery
- **Verarbeitung**:
  - **Network Discovery**: SNMP/OPC UA/Modbus Scanner
  - **IPC Optimizer** (Forschungsfokus): Graph-basierte Compile-Time-Optimierung
  - **Test Generator**: Automatische Test-Generierung aus M3 Constraints
- **Output**: C++ Gesamtprojekt (`playbooks/VIA-M1-System/`), Kubernetes Manifests, Edge-Modules

#### 3. VIA-M1-System-Deployer (System ’ Produktion)
- **Input**: M1 Systemprojekt, Deployment-Targets (MIPS, RISC-V, ARM, x86, etc.)
- **Verarbeitung**:
  - **Cross-Compilation**: Multi-Architektur Toolchain Management
  - **Horse-Rider-Deployment**: C++23 Modules, Hot-Reload, Canary Deployment
  - **Distributed Build**: Parallele Builds über GitHub Runners
- **Output**: Deployed System für >50.000 Edge-Geräte, Binaries, Digital Twin

## Sub-Protokolle unter OPC UA

VIA definiert drei custom OPC UA Sub-Protokolle:

### 1. Edge-Group-Protocol (Außenwelt-Ebene)
- **Funktion**: Virtuelle Netzwerkgruppen für hierarchische Edgegeräte-Gruppierung
- **Performance**: Hardcoded Messages, kein virtueller Router ’ Zeitkritikalität gewahrt
- **Sicherheit**: Geschachtelte Sicherheitsstufen (Device-Groups ’ Edge-Groups ’ Cluster-Groups ’ Global)

### 2. Deploy-Protocol (Verwaltungs-Ebene)
- **Funktion**: Versionierung, Systemupdates, Rejuvenation
- **Separation**: Metadaten getrennt von Anlagendaten
- **Telemetrie**: CPU-Last, RAM-Auslastung, Disk I/O
- **In-the-Loop Selbstoptimierung**: Kontinuierliche Feedback-Schleife

### 3. Process-Group-Protocol (Datenebene) ’ **Forschungskern**
- **Funktion**: Transparente IPC-Optimierung zwischen Services
- **IPC-Mechanismen**: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging
- **Optimierung**: Pareto-Optimierung (Latenz, Durchsatz, Ressourcenverbrauch) via Z3 Constraint-Solver
- **Compile-Time-Entscheidung**: Statisches Ranking mit optionaler Runtime-Anpassung

## Projektfortschritt und Entwicklungsplan

Siehe `playbooks/TODO.md` für detaillierte Aufgaben und Fortschritt.

### Phase 1: Research & Analyse  ABGESCHLOSSEN
- Alle Uni-Dokumente vollständig gelesen
- AAS, OPC UA, CMFM, SOA analysiert
- Santiago Papers (MMB, CMFM, SOA) vollständig verarbeitet

### Phase 2: GitHub Repository-Analyse  ABGESCHLOSSEN
- aas-core-works (M3 Metamodel, Code-Generator)
- open62541 (C99 OPC UA Stack)
- UA-Nodeset (76+ Companion Specifications)

### Phase 3: Implementation Playbooks ó NÄCHSTE PHASE
1. `Main_System_playbook_DAY01.md` (orchestriert M3’M2’M1)
2. `VIA-M3-Compiler/implementation/M3_compiler_playbook.md`
3. `VIA-M3-Compiler/tests/M3_tests_playbook.md`
4. `VIA-M2-SDK/implementation/M2_sdk_playbook.md`
5. `VIA-M2-SDK/tests/M2_tests_playbook.md`
6. `VIA-M1-System-Deploy/implementation/M1_deploy_playbook.md`
7. `VIA-M1-System-Deploy/tests/M1_tests_playbook.md`

### Phase 4: Exposé & Forschungsantrag =Ë GEPLANT
- Exposé nach CELM-Vorlage
- Forschungsantrag 1-Seite Summary

## Forschungsfokus

### Zentrale Forschungsfrage
> Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC) bei der Kompilation optimiert wird?

### Hypothesen
- **H1**: Compiler-basierte IPC-Optimierung reduziert Latenz um >30% gegenüber Runtime-Service-Mesh
- **H2**: Statische Positionierung erreicht 90% der Effizienz dynamischer Orchestrierung
- **H3**: Process-Group-Protocol skaliert linear bis 100.000 Services
- **H4**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um 60%

## Technologie-Stack

- **Sprachen**: C++20/23, AAS-lang (custom DSL), Protobuf
- **Protokolle**: OPC UA (IEC 62541), gRPC, IPC-Mechanismen
- **Deployment**: Kubernetes, C++23 Modules (Horse-Rider pattern)
- **Optimierung**: Z3 Constraint Solver, Pareto-Optimierung
- **Architekturen**: MIPS, RISC-V, POWER9+, x86, ARM1+, Sparc
- **Betriebssysteme**: Linux, Windows, macOS

## Multi-Level-Debugging

VIA implementiert durchgängige Fehlerrückverfolgung über alle Compiler-Stufen:

```
M0 Binary (deployed) ’ Fehler
    “ Trace
M1 Systemprojekt (C++ Code) ’ Fehlerquelle
    “ Trace
M2 SDK (generierter Code) ’ Generierungsregel
    “ Trace
M3 Metamodell (AAS-lang Definition) ’ Ursprüngliche Spezifikation
```

Analogie: Wie gdb über g++-Compiler-Schichten hinweg debuggen kann (Frontend ’ Middle-End ’ Backend ’ Assembly ’ Binary), kann VIA-Debugger über mehrere Metamodell-Ebenen zurückverfolgen.

## Skalierbarkeit

**Zielsystem**: >50.000 Edge-Geräte

**Performance-Optimierungen**:
- Hardcoded Messages (effizienter als dynamisches Routing)
- Compile-Time-Entscheidungen (statisches IPC-Ranking)
- Binary ABI-Stabilität (C++23 Modules)
- Distributed Compilation (parallele Builds)
- Keine virtuellen Router bei Zeitkritikalität

## Sicherheit

**Geschachtelte Sicherheitsarchitektur**:
- Jede Protokoll-Ebene (Edge-Group, Deploy, Process-Group) hat eigene Sicherheitsstufen
- Rekursive Gruppierung ermöglicht hierarchische Policies
- Hardcoded Messages verhindern Runtime-Code-Change
- Quellcode kann zur Laufzeit nicht verändert werden (Fokus auf Deployment-Server-Sicherheit)

## Vision: Industrie 5.0

**Zukünftige KI-Integration**:
1. Kunde beschreibt System per Sprache/Text
2. KI-Modell übersetzt in M3-Compiler-Anforderungen
3. Compiler-Kette (M3 ’ M2 ’ M1) generiert System
4. Software-in-the-Loop: Iterative Fehlerkorrektur
5. Vollautomatisches Deployment

**Meilensteine**:
- **M3 mit sich selbst definieren**: VIA schließt den Kreis durch automatische M3-Definition über M3
- **Systeme, die sich selbst definieren**: Autonome Systemgenerierung und Konstruktion

## Literatur

Siehe `docs/english/PROJECT_DESCRIPTION_AND_RESEARCH.md` für vollständiges Literaturverzeichnis.

### Kernquellen
- IEC 63278 (2024): Asset Administration Shell
- IEC 62541 (2020): OPC Unified Architecture
- Soler Perez Olaya, S. et al. (2024): Dynamic Multi-Message Broker, SOA for Digital Twins
- Soler Perez Olaya, S. & Wollschlaeger, M. (2022): CMFM Generality Hierarchy
- aas-core-works: https://github.com/aas-core-works
- open62541: https://github.com/open62541/open62541

---

**Letzte Aktualisierung**: Oktober 2025
**Status**: Phase 2 abgeschlossen, Phase 3 in Vorbereitung
