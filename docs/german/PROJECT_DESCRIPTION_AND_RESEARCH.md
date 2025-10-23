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

## 1. Einleitung und Motivation

### 1.1 Ausgangssituation

Die industrielle Automatisierung steht vor der Herausforderung, heterogene Systeme mit unterschiedlichen Protokollen, Architekturen und Kommunikationsmustern zu integrieren. Im Rahmen der Forschungsarbeiten am Lehrstuhl für Industrielle Kommunikationstechnik der TU Dresden unter Prof. Dr.-Ing. habil. Martin Wollschlaeger wurde das Asset Administration Shell (AAS) Framework nach IEC 63278 als standardisierter Ansatz für digitale Zwillinge in der Industrie 4.0, oder aus digitaler Sicht Industrie 3.2, entwickelt. Die von Santiago Soler Perez Olaya betreute aas-core-works Implementierung offenbart dabei eine vollständige Compiler-Architektur, die auf einer M3/M2/M1 Metamodell-Struktur basiert – analog zu den Ansätzen von Prof. Castrillon im Bereich Compiler-Design an der TU Dresden.

Die derzeitige Implementierung des AAS-Frameworks nutzt Python-Skripte, die Compiler-Funktionalität simulieren: Das aas-core-meta Repository definiert das M3-Metamodell in vereinfachtem Python, während aas-core-codegen daraus Zielsprachen-SDKs generiert (C++, C#, Python, TypeScript, Java, Golang). Trotz dieser funktionalen Code-Generierung fehlt eine vollständige Compiler-Implementierung als externes Übersetzerprogramm, das als eigenständiges, wartbares Tool in industriellen Produktionsumgebungen eingesetzt werden kann.

VIA (Virtual Industry Automation) adressiert diese Lücke durch einen **selbst-kompilierenden Bootstrap-Mechanismus**: Das VIA-Hauptprogramm kompiliert zunächst den M3-Compiler aus AAS-Metamodell-Definitionen, testet diesen, und verwendet ihn zur Generierung der M2-SDK. Diese SDK wird wiederum kompiliert, getestet und zur Übersetzung von Kundenprojekten (M2→M1) eingesetzt. Ein Software-in-the-Loop (SITL) System automatisiert dabei Ki-gestützt die Transformation textueller Spezifikationen (AAS IEC 63278, OPC UA IEC 62541) in ausführbaren M3-Modellcode, sowie die voll autonome Anpassung, Implementierung und Tests des Programmcodes (System on call / SOC). Während aas-core-works statische SDKs generiert, ermöglicht VIA durch diesen Bootstrap-Ansatz eine durchgängige Automatisierung von der Textspezifikation bis zum deployed Industriesystem – inklusive der Fähigkeit zur Selbstmodifikation und Hot-Reload des Hauptprogramms im laufenden Betrieb.

### 1.2 Vision: Industrie 5.0 (Oder besser: Industrie 3.3)

Die nächste Generation industrieller Automatisierung – Industrie 5.0 – erfordert eine fundamentale Paradigmenverschiebung: Statt manueller Systemkonfiguration und -programmierung soll eine KI-gesteuerte Systembeschreibung ermöglicht werden, bei der Anwender ihr System natürlichsprachlich beschreiben. Das Zielsystem führt automatische Compilation und Deployment durch, wobei Software-in-the-Loop Verfahren iterative Fehlerkorrektur gegen die Kundenspezifikation ermöglichen. Das langfristige Ziel dieser Forschungsvision lautet: "Der Kunde beschreibt sein System der KI, die KI definiert eine Compiler-Beschreibung, der Compiler generiert das funktionsfähige System."

Denkt man diesen Schritt weiter, so kann der Kunde Systeme definieren, die sich selbst definieren oder Systeme konstruieren, die den Architektur- und Definitionsteil selbstständig übernehmen und durchführen, woraus sich eine M3 Selbstdefinition und Konstruktion ergibt.

Diese Vision erfordert eine durchgängige Automatisierung vom abstrakten Metamodell bis zum deployed System auf heterogenen Edge-Geräten. VIA (Virtual Industry Automation) verfolgt diesen Ansatz durch eine mehrstufige Compiler-Kette (M3→M2→M1), die aus einem Metamodell zunächst ein SDK generiert (M3→M2), aus Kundenprojekten Systemprojekte erstellt (M2→M1) und diese schließlich auf über 50.000 Edge-Geräte verteilt deployed (M1-Deployment).

### 1.3 Forschungslücke

Trotz der vorhandenen Metamodell-Frameworks und Code-Generatoren existiert eine fundamentale Forschungslücke zwischen Metamodell-Definition und Production-Grade Compiler-Implementierung. Bisherige Ansätze wie aas-core-codegen erzeugen zwar lauffähigen Code, jedoch fehlt die Verbindung zum automatisierten Deployment: Es gibt keine wartbare, versionierte SDK-Generierung für industrielle Langzeitnutzung (typischerweise 15-25 Jahre in der Fertigungsindustrie), keine automatische Orchestrierung der generierten Systeme und keine Optimierung der Prozesskommunikation zur Compile-Zeit.

Die manuelle Orchestrierung von mehr als 50.000 Edge-Geräten in einer typischen Automobilfabrik ist praktisch unzumutbar und fehleranfällig. Zudem erfordern heterogene Zielarchitekturen (MIPS, RISC-V, POWER9, x86, ARM, Sparc) eine Multi-Target-Compilation, die in bisherigen AAS-Implementierungen nicht vorgesehen ist. Insbesondere fehlt eine wissenschaftliche Untersuchung, ob und wie Mikroservice-Kommunikation (IPC: Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) zur Compile-Zeit optimiert werden kann, um Latenz und Ressourcenverbrauch gegenüber Runtime-Orchestrierung zu reduzieren.

---

## 2. Problemstellung und Forschungsfrage

### 2.1 Kontext: VIA-Gesamtsystem

VIA (Virtual Industry Automation) bildet den übergeordneten Kontext dieser Forschungsarbeit. Es handelt sich um eine mehrstufige Compiler-Kette (M3→M2→M1) für heterogene Industriesysteme mit automatischer Orchestrierung von mehr als 50.000 Edge-Devices. Das Gesamtsystem gliedert sich in drei Hauptkomponenten: Der **M3-Compiler** transformiert das AAS-Metamodell in ein sprachspezifisches SDK (C++, Python, Java), der **M2-SDK-Compiler** konvertiert Kundenprojekte unter Einbeziehung von Network Discovery in vollständige Systemprojekte, und der **M1-System-Deployer** führt Cross-Compilation, Horse-Rider-Deployment und Kubernetes-Orchestrierung durch.

Diese Architektur ermöglicht eine durchgängige Automatisierung von der abstrakten Systembeschreibung bis zum deployed System auf heterogenen Hardwareplattformen. Während das VIA-Gesamtsystem alle Aspekte von Metamodellierung bis Deployment abdeckt, fokussiert sich die vorliegende Forschungsarbeit auf einen spezifischen, kritischen Teilaspekt: die Optimierung der Prozesskommunikation zur Compile-Zeit.

### 2.2 Fokus dieser Forschungsarbeit: Process-Group-Protocol

Die zentrale Forschungsfrage dieser Arbeit lautet:

> **Können über Metamodelle (M3/M2) automatisch Prozessketten von Mikroservices erstellt werden, deren Positionierung im System und Kommunikationsmechanismus (IPC: Pipe, Socket, TCP, File-Queue, Thread) bei der Kompilation optimiert wird?**

Diese Frage adressiert eine fundamentale Herausforderung moderner Mikroservice-Architekturen: Die Wahl des Inter-Process Communication (IPC) Mechanismus erfolgt üblicherweise zur Laufzeit durch Service-Mesh-Lösungen wie Istio oder Linkerd. Diese Runtime-Entscheidungen verursachen jedoch Overhead durch dynamisches Routing, Service Discovery und Load Balancing. Die vorliegende Arbeit untersucht, ob durch Compile-Time-Analyse des Metamodells eine statische Optimierung möglich ist, die Latenz reduziert ohne Flexibilität signifikant einzuschränken.

Zur systematischen Bearbeitung dieser Forschungsfrage werden vier Teilfragen formuliert:

1. **Metamodell-Elemente**: Welche M3-Modellelemente sind notwendig, um Prozesskommunikation (Abhängigkeiten, Datenflüsse, Latenzanforderungen) zu beschreiben?

2. **IPC-Ableitung**: Wie kann der M2-SDK-Compiler aus Prozessabhängigkeiten optimale IPC-Mechanismen ableiten? Welche Heuristiken bestimmen, ob Pipe (gleicher Host, geringer Overhead), Unix Socket (gleicher Host, höhere Flexibilität), TCP (Remote, höchste Flexibilität), File-Queue (asynchron, persistent) oder Thread-Messaging (gleicher Prozess, geringste Latenz) gewählt wird?

3. **Positionierungsmetriken**: Welche Metriken bestimmen die Positionierung von Mikroservices (gleicher Container, gleicher Host, gleicher Cluster-Node, Remote)? Wie werden Latenzanforderungen, Ressourcenverfügbarkeit und Ausfallsicherheit gewichtet?

4. **Skalierbarkeit**: Wie verhält sich das Process-Group-Protocol unter OPC UA bei mehr als 50.000 Geräten? Kann hierarchische Gruppierung (Edge-Groups → Cluster-Groups → Global) lineares Skalierungsverhalten erreichen?

Zur Validierung der Forschungshypothese werden vier messbare Hypothesen aufgestellt:

- **H1 (Latenz)**: Compiler-basierte IPC-Optimierung reduziert Latenz um mindestens 30% gegenüber Runtime-Service-Mesh-Lösungen
- **H2 (Effizienz)**: Statische Positionierungsentscheidung zur Compile-Zeit erreicht mindestens 90% der Effizienz dynamischer Runtime-Orchestrierung
- **H3 (Skalierbarkeit)**: Das Process-Group-Protocol skaliert linear bis 100.000 Services bei hierarchischer Gruppierung
- **H4 (Entwicklungszeit)**: Metamodell-basierte Abstraktion senkt manuelle Entwicklungszeit um mindestens 60%

**Abgrenzung**: Diese Arbeit konzentriert sich auf das **Process-Group-Protocol-Subsystem** als Teil des VIA-Gesamtsystems. Die M3/M2/M1-Architektur dient als Kontext und theoretischer Rahmen, wird jedoch nicht in allen Details implementiert. Insbesondere werden M3-Compiler-Optimierungen, Multi-Architektur-Cross-Compilation und das vollständige Horse-Rider-Deployment als gegeben vorausgesetzt und nicht eigenständig erforscht.

### 2.3 Teilprobleme des Gesamtsystems (Kontext)

Das VIA-Gesamtsystem gliedert sich in acht Teilprobleme, die in der Projektstruktur unter `playbooks/` als separate Implementierungs-Playbooks dokumentiert sind. Während diese Arbeit sich auf das Process-Group-Protocol (2.3.5) konzentriert, ist das Verständnis aller Komponenten notwendig, da sie die Ausführungsumgebung für die Prozesskommunikation bilden.

#### 2.3.0 Hauptprogramm (Orchestrierung M3→M2→M1)

**Projektlokation**: `src/main.cpp` (versioniert, nicht in gitignore)

Das VIA-Hauptprogramm orchestriert den gesamten Bootstrap-Zyklus durch sequenzielle Compilation und Testing der Compiler-Stufen:

1. **M3-Compiler-Build**: Kompiliert `playbooks/VIA-M3-Compiler/` via CMake → `build/via-m3-compiler` Binary
2. **M3-Compiler-Test**: Führt M3-Testframework aus, validiert AAS-lang Parsing
3. **M2-SDK-Generation**: Führt `via-m3-compiler` aus → generiert `playbooks/VIA-M2-SDK/` (gitignored)
4. **M2-SDK-Build**: Kompiliert generierte SDK → `build/via-m2-sdk-compiler` Binary
5. **Kundenprojekt-Compilation**: Lädt Kundenprojekt-Dateien (`.via` Format), kompiliert mit M2-SDK → `playbooks/VIA-M1-System/` (gitignored, C++ Gesamtprojekt)
6. **M1-System-Build**: Kompiliert M1-Projekt für alle Zielarchitekturen → `build/binaries/{arch}/` Ordner
7. **Deployment**: Verteilt Binaries über Horse-Rider-Architektur an Edge-Geräte
8. **Servermodus**: Wechselt in OPC UA Servermodus, akzeptiert Neukompilations-Requests von Administratoren

**Selbstreferenz-Mechanismus**: Bei Neukompilations-Request kompiliert das Hauptprogramm sich selbst neu (M3→M2→M1→M0), startet neue VIA-Instanz über Prozesskommunikation und beendet sich selbst nach erfolgreichem Handover.

**Multi-Level-Debugging und Fehlerrückverfolgung**: Wenn in einer Prozesskette des M0-kompilierten Systems ein Fehler auftritt, verwaltet das Hauptprogramm ein durchgängiges Tracing-Modell über alle Kompilationsstufen hinweg. Dieses ermöglicht die lückenlose Rückverfolgung eines Fehlers vom deployed Binary (M0) über das Systemprojekt (M1), die generierte SDK (M2) bis zur ursprünglichen M3-Modelldefinition und Kundenprojektdefinition. Da jede niedere Meta-Stufe eine Implementierung einer höheren Meta-Stufe ist, ergibt sich eine vollständige konzeptionelle Repräsentation über alle Schichten hinweg. Der VIA-Debugger kann rückwärts über mehrere Schichten durchdringen und verfügt über mehrere Programmzeiger gleichzeitig, die sich über verschiedene Modell-Dateien (`.aas`, `.via`) und generierte C++-Quelldateien erstrecken – analog zum gdb-Debugger, der ebenfalls über mehrere Schichten der g++-Compiler-Architektur hinweg debuggen kann (Frontend → Middle-End → Backend → Assembly → Binary). Diese Multi-Level-Debugging-Fähigkeit ist essentiell für die Wartbarkeit industrieller Systeme, da Fehler direkt auf ihre konzeptionelle Ursache in der Metamodell-Spezifikation zurückgeführt werden können, anstatt nur Symptome im generierten Code zu analysieren.

**Problem**: Zustandsverwaltung über 3 Phasen, Fehlerbehandlung bei jeder Stufe, Transaktionalität bei Selbst-Neukompilation, Overhead des Multi-Level-Tracing in Produktivsystemen

#### 2.3.1 M3-Ebene (Metamodell-Compiler)

Der M3-Compiler, lokalisiert in `playbooks/VIA-M3-Compiler/` als versionierter Bestandteil des Repositories, definiert die AAS-lang (Asset Administration Shell Language) als domänenspezifische Programmiersprache für industrielle Systeme. Diese Compiler-Komponente bildet die erste Stufe der VIA-Compiler-Kette und ist für die Transformation von abstrakten Metamodell-Definitionen (M3) in eine typ-sichere C++ SDK (M2) verantwortlich.

Der M3-Compiler empfängt als Eingabe die AAS IEC 63278 Textspezifikation, die über das SITL-System (Software-in-the-Loop) automatisch in ausführbaren M3-Modellcode transformiert wird. Zusätzlich verarbeitet er OPC UA IEC 62541 als M3-Bibliothek, ebenfalls über SITL eingelesen falls noch nicht vorhanden, sowie VIA-Extensions für Prozesskommunikation als custom M3-Definitionen. Diese Eingaben bilden die formale Grundlage für die anschließende SDK-Generierung.

Die Verarbeitung erfolgt durch einen custom Template-Engine, der in AAS-lang selbst definiert ist und auf C++20/23 Metaprogramming aufsetzt. Als M3-Interpreter fungiert Protobuf aus dem `third_party/` Verzeichnis, das zum Einlesen von Modell und Kundendaten verwendet wird. Ein integriertes Constraint-System validiert Typensicherheit und verhindert die Entstehung von Spaghetti-Code durch rigorose Modularisierung der generierten SDK.

Als Output generiert der M3-Compiler das Verzeichnis `playbooks/VIA-M2-SDK/` mit dem vollständigen C++ SDK-Code (gitignored, da generiert), OPC UA NodeSet XML-Dateien für die VIA Custom Companion Specification, Protobuf `.proto` Dateien für die Microservice-Kommunikation zwischen Services, sowie umfassende Dokumentation mit durchgereichten M3-Kommentaren, die bis in die Binary-Headers propagieren.

Die zentrale Herausforderung dieser Komponente liegt in der Vermeidung von Spaghetti-Code bei der automatischen Code-Generierung. Dies wird durch ein mehrschichtiges Constraint-System adressiert, das Typensicherheit, Modularität und Wartbarkeit der generierten SDK garantiert.

#### 2.3.2 M2-Ebene (SDK-Compiler)

**Projektlokation**: `playbooks/VIA-M2-SDK/` (generiert, gitignored)

Die M2-SDK fungiert als Compiler für Kundenprojekte. Sie liest `.via` Projektdateien (in AAS-lang geschrieben), validiert Syntax, und kompiliert in ein C++ Gesamtprojekt (M1).

Die geplante Playbook-Struktur umfasst vier Sub-Komponenten, die verschiedene Aspekte der SDK-Funktionalität adressieren. Das `network_discovery.md` Playbook beschreibt einen SNMP/OPC UA/Modbus Scanner zur automatischen Topologie-Erkennung im Kundennetzwerk. Der `ipc_optimizer.md` Playbook implementiert einen graph-basierten Algorithmus zur IPC-Mechanismus-Auswahl und bildet den Forschungsfokus dieser Arbeit. Das `auto_suggestions.md` Playbook ermöglicht KI-gestützte Vorschläge für Systemkonfiguration basierend auf erkannter Netzwerktopologie. Schließlich definiert `test_generator.md` die automatische Generierung deterministischer Tests aus M3-Constraints, um vollständige Testabdeckung zu gewährleisten.

Als Input empfängt die M2-SDK Kundenprojekt-Dateien im `.via` Format unter `customer_project/*.via` sowie optional eine Netzwerk-Topologie, die über das Network Discovery System ermittelt wurde. Die Verarbeitung dieser Eingaben resultiert in drei Hauptausgaben: Das Verzeichnis `playbooks/VIA-M1-System/` enthält das vollständige C++ Gesamtprojekt (gitignored, da generiert), Kubernetes Manifests werden als `deployment.yaml` bereitgestellt, und automatisch generierte Tests enthalten durchgereichte Kundenkommentare für vollständige Traceability.

Die zentrale Herausforderung dieser Komponente liegt in der deterministischen Testabdeckung für industrielle Kombinatorik sowie der IPC-Optimierung bei mehr als 50.000 Services, wobei skalierbare Algorithmen und effiziente Heuristiken notwendig sind.

#### 2.3.3 M1-Ebene (System-Deployment)

**Projektlokation**: `playbooks/VIA-M1-System-Deploy/` (Playbooks für Deployment-Logik)

Der M1-Deployer kompiliert das M1-Systemprojekt (C++ Code) in Binaries für alle Zielarchitekturen und verteilt diese über das Horse-Rider-Deployment-System.

Die Architektur umfasst drei Sub-Komponenten, die verschiedene Deployment-Aspekte abdecken. Das `cross_compilation.md` Playbook beschreibt das Multi-Architektur Toolchain Management für MIPS, RISC-V, ARM, x86 und weitere Plattformen, wodurch heterogene Industrieumgebungen mit Legacy-Systemen adressiert werden. Das `horse_rider_deployment.md` Playbook implementiert C++23 Modules mit stabilen ABIs, Hot-Reload-Mechanismen und Canary Deployment für ausfallsichere Updates. Das `distributed_build.md` Playbook orchestriert parallele Builds über GitHub Runners, um die Compilationszeit für große Systeme signifikant zu reduzieren.

Der M1-Deployer generiert drei Kategorien von Ausgaben. Die kompilierten Binaries werden in der Ordnerstruktur `build/binaries/{arch}/{device_id}/` architekturspezifisch abgelegt, wobei jedes Edge-Gerät sein dediziertes Binary erhält. Deployment-Manifests für Kubernetes und Edge-Geräte ermöglichen automatisierte Rollouts über Container-Orchestrierung. Versionierte Binaries mit Header-Dokumentation erlauben externe Edge-Programmierung durch Drittanbieter-Systeme, die gegen stabile VIA-ABIs linken können.

Die zentralen Herausforderungen dieser Komponente liegen im Hot-Reload ohne Systemausfall, im Canary-Deployment mit automatischem Rollback bei Fehlern, in der Versionskonsistenz bei C++23 Modules über mehrere Compiler-Generationen hinweg sowie in der ABI-Stabilität für langfristige Industriekompatibilität (typischerweise 15-25 Jahre).

#### 2.3.4 Deployment-System (Horse-Rider-Architektur)

**Projektlokation**: Teil von `playbooks/VIA-M1-System-Deploy/horse_rider_deployment.md`

Die Horse-Rider-Architektur entkoppelt Deployment-Logik (Horse) von Fachlogik (Rider) durch eine modulare Trennung der Verantwortlichkeiten. Der Horse-Service fungiert als stabiler Container, der Rider-Services als C++23 Modules dynamisch zur Laufzeit lädt und entlädt, wodurch Hot-Reload ohne Systemausfall ermöglicht wird. Bei einem Rider-Update prüft der Horse zunächst die ABI-Kompatibilität des neuen Moduls gegen die definierten Schnittstellen. Anschließend lädt er das neue Modul parallel zum alten (Canary-Deployment) und routet zunächst nur einen kleinen Prozentsatz des Traffics zum neuen Service. Bei erfolgreichem Canary-Test erfolgt der vollständige Traffic-Switch zum neuen Rider, während bei Fehlern ein automatisches Rollback zum alten Modul durchgeführt wird. Die Architektur sieht mindestens zwei parallele Horses pro Edge-Gerät vor, die als Digital Twin fungieren und gegenseitige Redundanz gewährleisten.

Die zentralen technischen Herausforderungen dieser Architektur liegen in der ABI-Stabilität bei C++23 Modules über mehrere Compiler-Versionen und Aktualisierungszyklen hinweg, in der Zustandssynchronisation bei Hot-Reload zwischen altem und neuem Rider-Service sowie in der Rollback-Transaktionalität, die sicherstellt, dass bei Fehlern ein konsistenter Systemzustand innerhalb von Sekundenbruchteilen wiederhergestellt werden kann.

#### 2.3.5 Sub-Protokolle unter OPC UA → **FORSCHUNGSFOKUS**

**Projektlokation**: `playbooks/VIA-M3-Compiler/via_protocols/` (zukünftig, Spezifikation noch offen)

VIA definiert drei custom OPC UA Sub-Protokolle als systematische Erweiterung des Standards, die verschiedene Aspekte der Systemorchestrierung adressieren. Das Edge-Group-Protocol ermöglicht virtuelle Netzwerkgruppen für hierarchische Edgegeräte-Gruppierung, wodurch die Skalierbarkeit auf mehr als 50.000 Geräte erreicht wird. Das Deploy-Protocol verwaltet Versionierung, Logging und Rejuvenation für das Horse-Rider-System, um ausfallsichere Updates zu gewährleisten. Das Process-Group-Protocol bildet den Kern dieser Forschungsarbeit und optimiert die IPC-Mechanismen zwischen Services durch automatische Auswahl zwischen Pipe, Unix Socket, TCP, File-Queue und Thread-Messaging basierend auf Prozessabhängigkeiten und Latenzanforderungen.

Die Implementierung dieser Protokolle erfolgt als M3-Bibliothek (`via_protocols` lib) innerhalb der AAS-lang, wodurch sie vom VIA-M3-Compiler verarbeitet und in die M2-SDK integriert werden können. Die geplante MMB-Integration (Multi-Message Broker nach Santiago Soler Perez Olaya) ermöglicht Many-to-Many Broadcast-Kommunikation für flexible Nachrichtenverteilung zwischen heterogenen Prozessgruppen.

Der aktuelle Status dieser Komponente ist die Spezifikationsphase; die konkreten Protokoll-Definitionen werden im weiteren Projektverlauf als M3-Modelle ausgearbeitet. Die zentralen Herausforderungen liegen in der Protokoll-Komposition verschiedener Sub-Protokolle ohne semantische Konflikte, in der Effizienz bei mehr als 50.000 Geräten durch hierarchische Gruppierung, in der Definition geschachtelter Sicherheitsschichten sowie in der zukünftigen Standardisierung durch die OPC Foundation als offizielle Companion Specification.

#### 2.3.6 Network Discovery System

**Projektlokation**: Teil von `playbooks/VIA-M2-SDK/network_discovery.md`

Das Network Discovery System führt automatisches Scanning des Kundennetzwerks durch, indem es verschiedene industrielle Protokolle wie SNMP, OPC UA, Modbus, MQTT und RPC systematisch zur Topologie-Erkennung einsetzt. Das System liest Geräteeigenschaften von PLCs, SCADA-Systemen, MES-Servern und Sensoren aus, klassifiziert diese automatisch und erstellt eine strukturierte Netzwerktopologie. Basierend auf dieser Analyse generiert das System Asset-Mapping-Vorschläge für die M2-Projektkonfiguration, die dem Anwender als Startpunkt für die weitere Systemdefinition dienen.

Die wesentlichen Herausforderungen dieser Komponente liegen in der Protokoll-Heterogenität verschiedener Industriestandards mit unterschiedlichen Datenmodellen und Kommunikationsmustern, in der Zugriffskontrolle auf sicherheitskritische Produktionssysteme ohne bestehende Credentials sowie im Umgang mit Offline-Geräten, die zum Scan-Zeitpunkt nicht erreichbar sind, aber dennoch in die Topologie integriert werden müssen.

#### 2.3.7 Master Active Management (Deployment-Orchestrierung)

**Projektlokation**: Teil von `playbooks/VIA-M1-System-Deploy/master_active_management.md`

Das Master Active Management implementiert Active/Active Redundanz analog zu Microsoft Active Directory, wobei mehrere Deployment-Master gleichzeitig aktiv sind und sich gegenseitig replizieren. Der Deployment-Master koordiniert sowohl Kubernetes-Container-Orchestrierung als auch Edge-Service-Orchestrierung für nicht-containerisierte Geräte und bildet damit die zentrale Steuerungsinstanz des VIA-Systems. Die Zugriffskontrolle wird über ein rollenbasiertes Berechtigungssystem verwaltet, das Benutzer und Rollen definiert und optional mit bestehenden Samba- oder Active-Directory-Infrastrukturen integriert werden kann. Die Konfiguration von Redundanz-Levels und Service-Verteilung erfolgt durch Policies, die festlegen, wie viele Replikate jedes Services auf welchen Hosts deployed werden.

Die kritischen Herausforderungen dieser Komponente liegen in der Vermeidung von Split-Brain-Szenarien, bei denen getrennte Master-Instanzen inkonsistente Entscheidungen treffen, in der Gewährleistung von Konsistenz über geografisch verteilte Cluster hinweg sowie in der Minimierung von Failover-Zeiten beim Ausfall eines Masters, um kontinuierliche Orchestrierung zu garantieren.

#### 2.3.8 Multi-Architektur Cross-Compilation

**Projektlokation**: Teil von `playbooks/VIA-M1-System-Deploy/cross_compilation.md`

Das Multi-Architektur Cross-Compilation System ermöglicht die Unterstützung heterogener Hardwareplattformen, darunter MIPS, RISC-V, POWER9+, x86, ARM1+ und Sparc, jeweils auf Betriebssystemen wie Linux, Windows und macOS. Der M2-SDK-Kunde definiert die gewünschten Zielarchitekturen deklarativ in `.via` Projektdateien, woraufhin der M1-Deployer automatisch CMake-Toolchains für alle Targets konfiguriert und parallele Cross-Compilation durchführt. Diese Architektur-Vielfalt ermöglicht Legacy-Support für alte Industriesysteme, die teilweise seit Jahrzehnten in Produktion sind, sowie gleichzeitige Integration moderner Architekturen für neue Komponenten.

Die wesentlichen Herausforderungen dieser Komponente liegen im Toolchain-Management für eine Vielzahl von Compiler-Versionen und Zielplattformen, in der Treiber-Verfügbarkeit für spezifische Hardware-Komponenten auf Legacy-Systemen sowie in den unterschiedlichen Memory-Modellen verschiedener Architekturen (z.B. Big-Endian vs. Little-Endian, unterschiedliche Pointer-Größen), die konsistente Datenserialisierung und IPC-Kommunikation über Architekturgrenzen hinweg erfordern.

---

## 3. Stand der Forschung

Die Forschungsarbeit baut auf mehreren etablierten Standards und Forschungsergebnissen auf, die im Folgenden systematisch dargestellt werden. Die Analyse umfasst AAS-Code-Generierung (Abschnitt 3.1), OPC UA als Kommunikationsprotokoll (Abschnitt 3.2), Multi-Message Broker für Brownfield-Integration (Abschnitt 3.3), Management-Frameworks (Abschnitt 3.4), Service-orientierte Architekturen (Abschnitt 3.5), Monitoring-Ansätze (Abschnitt 3.6) sowie theoretische Grundlagen wie ISA-95 und CMFM (Abschnitt 3.7).

### 3.1 Asset Administration Shell (AAS) - aas-core-works

Das aas-core-works Framework bildet den konzeptionellen Ausgangspunkt für die metamodell-basierte Code-Generierung in VIA. Es implementiert den IEC 63278 Standard als M3/M2/M1 Metamodel Architecture für digitale Zwillinge und demonstriert, wie aus einem abstrakten Metamodell (aas-core-meta in simplified Python) produktionsreifer Code für sechs Zielsprachen generiert werden kann. Die Architektur folgt dem Single-Source-of-Truth Prinzip: Das M3-Metamodell wird einmal kanonisch definiert, der aas-core-codegen Compiler transformiert es automatisch in sprachspezifische SDKs mit identischer Semantik.

**VIA-Projektintegration**: VIA übernimmt die M3/M2/M1-Architektur-Idee, implementiert jedoch einen eigenständigen M3-Compiler in `playbooks/VIA-M3-Compiler/`, der AAS IEC 63278 als M3-Modellcode interpretiert. Die textuelle Spezifikation (PDF/HTML der IEC 63278) wird über SITL (Software-in-the-Loop) automatisch in ausführbaren M3-Code transformiert, der vom VIA-M3-Compiler verarbeitet wird. Die 6 Language SDKs von aas-core-codegen dienen als Referenz-Implementierung, VIA fokussiert initial jedoch auf C++-SDK-Generierung mit eigenem Template-Engine (definiert in AAS-lang selbst, nicht in Python). Anders als aas-core-works, das Python-Skripte zur Code-Generierung nutzt, ist VIA-M3-Compiler ein produktionsreifer C++20/23-Compiler mit vollständigem Testframework und stabiler Binary-Distribution.

Das aas-core-works Framework implementiert den IEC 63278 Standard, der eine M3/M2/M1 Metamodel Architecture für Digital Twins definiert. Das aas-core-meta Repository enthält das M3 Metamodell in simplified Python als kanonische Definition, wobei Releases nach dem Schema YYYY.MM.DD versioniert werden. Der aas-core-codegen Multi-Target Compiler folgt dem Single Source of Truth Prinzip und ermöglicht automatisierte Generierung mit Fokus auf Skalierbarkeit.

Das Framework generiert sechs Language SDKs (C++, C#, Python, TypeScript, Java, Golang) mit identischer Semantik sowie fünf Schema Exports (JSON Schema, XSD, RDF SHACL, JSON-LD Context, Protobuf). Die Code Generation Pipeline transformiert das Python M3 Metamodell über Parser und Analyzer in sprachspezifische SDKs und Schema Exports. Die Transformation Rules bilden Python-Klassen auf Zielsprachen-Klassen ab, Properties werden zu Getters/Setters transformiert, Constraints werden in Validierungsfunktionen übersetzt, und Dokumentation wird automatisch in API-Dokumentation propagiert.

Das Constraint System nutzt Python `@invariant` Decorators für Runtime Validation, wobei Uniqueness, Multiplicity, Type Safety und Semantic Consistency validiert werden. Code Injection Points ermöglichen Custom Constructors, Serialization/Deserialization und Performance-Optimierungen an definierten Stellen im generierten Code. Die Community umfasst 2.9K Stars und 307 Contributors, das Projekt steht unter MPL 2.0 Lizenz.

Die Limitationen des Frameworks liegen darin, dass Python-Skripte statt eines C++ Production-Compilers verwendet werden, das Modell statisch ist ohne Runtime Reconfiguration, und die Implementierung AAS-spezifisch ist ohne Berücksichtigung Industrial Real-Time Constraints.

### 3.2 OPC UA (IEC 62541) & open62541 C99 Stack

OPC UA (Open Platform Communications Unified Architecture) nach IEC 62541 bildet das Kommunikations-Rückgrat für VIA. Als etablierter Standard in der industriellen Automatisierung bietet OPC UA eine M3/M2/M1-basierte Informationsmodellierung, die strukturell mit der VIA-Architektur kompatibel ist. Die open62541 Implementierung – ursprünglich ein TU Dresden Forschungsprojekt – liefert einen produktionsreifen C99-Stack mit minimalem Memory-Footprint (~250KB), der für Edge-Geräte geeignet ist. Besonders relevant für VIA ist die Dynamic Address Space API, die es ermöglicht, OPC UA Nodes zur Laufzeit zu erzeugen und zu löschen – eine Voraussetzung für die Abbildung dynamisch registrierender VIA-Prozesse.

**VIA-Projektintegration**: OPC UA wird in VIA ausschließlich auf M3-Ebene als Bibliothek definiert. Die textuelle Spezifikation von OPC UA IEC 62541 wird über SITL in M3-Modellcode transformiert und in `playbooks/VIA-M3-Compiler/third_party/opcua_m3/` als M3-Bibliothek integriert. Der VIA-M3-Compiler generiert aus diesen M3-Modellen sowohl OPC UA NodeSet XML-Dateien (VIA Custom Companion Spec) in `playbooks/VIA-M3-Compiler/output/via_companion_spec.xml` als auch die vollständige OPC UA Implementierung für die M2-SDK. VIA verwendet keine externen M2-Bibliotheken wie open62541 direkt, sondern generiert die gesamte OPC UA Funktionalität aus dem M3-Metamodell heraus. Die open62541 C99-Implementierung dient lediglich als Referenz und Beweis, dass die OPC UA Spezifikation korrekt in embedded Systemen implementierbar ist. Die von VIA generierte SDK implementiert die Dynamic Address Space API analog zu `UA_Server_addObjectNode()` für die dynamische Registrierung von Prozessen zur Laufzeit – ein Hybrid-Modell aus statischen Typdefinitionen (VIAProcessType, VIARouterType) und dynamischen Instanzen.

OPC UA implementiert ein Client-Server Many-to-Many Modell, bei dem mehrere Clients mit mehreren Servern kommunizieren können, unterstützt durch Discovery Mechanismen und Subscriptions für ereignisbasierte Datenübertragung. Die Informationsmodellierung bildet das Herzstück von OPC UA und ermöglicht beliebig komplexe Strukturen mit eigenen Objekttypen und Variablentypen, wobei das Modell objektorientiert und dynamisch erweiterbar ist.

Die M3/M2/M1 Architektur definiert drei Abstraktionsebenen: M3 als Metamodell, in dem Objekte, Variablen und Methoden als Konzepte existieren, M2 als Modell mit domain-spezifischen Typen, und M1 als Instanz-Ebene mit laufenden Systemen. Der ModelCompiler transformiert XML-Modellbeschreibungen in C# oder C Code, wobei der UA Modeler grafisches Design ermöglicht. Verschiedene C++ SDKs stehen zur Verfügung: Die OPC Foundation bietet eine ANSI C/C++ Implementierung, Unified Automation eine kommerzielle Lösung, und open62541 eine C99-basierte Open Source Variante mit circa 250KB Footprint.

Die open62541 Implementierung ist eine C99 Implementation unter MPL 2.0 Lizenz mit 2.9K Stars und 307 Contributors, die ursprünglich als TU Dresden Forschungsprojekt entstand. Sie ist embedded-friendly mit circa 250KB minimaler Konfiguration (Core + Namespace 0 MINIMAL) und circa 500KB voller Konfiguration, zertifiziert als "Micro Embedded Device Server". Die Plugin-Architektur umfasst austauschbare Module für Logging, Crypto (OpenSSL oder mbedTLS), Access Control (RBAC) und NodeStore (HashMap oder ZipTree). Die Platform Abstraction unterstützt POSIX, Windows und Zephyr RTOS (freeRTOS legacy) und ist portierbar auf neue Plattformen durch abstrahierte Clock- und Networking-Interfaces.

Der Nodeset Compiler ist ein Python Tool (nodeset_compiler.py), das XML NodeSets in C Code transformiert und für die Integration mit dem VIA-M3-Compiler vorgesehen ist. Die Dynamic Address Space API ermöglicht das Hinzufügen und Löschen von Nodes zur Laufzeit, was die Abbildung der VIA Registry auf OPC UA Nodes über die `UA_Server_addObjectNode()` API ermöglicht. Die Performance liegt bei 10.000 Operationen pro Sekunde im Single-Thread-Betrieb, 50.000 Operationen pro Sekunde mit vier Cores, wobei 100.000 Nodes getestet wurden und 1.000 Notifications pro Sekunde unterstützt werden. Die Sicherheitsimplementierung umfasst Basic256Sha256 (AES-256 + SHA256), X.509 Zertifikate und konfigurierbare Encryption Policies.

Das UA-Nodeset Repository bietet über 76 Companion Specifications, darunter DI, I4AAS, PLCopen, Robotics, CNC, MTConnect, ISA-95, PackML, EUROMAP und BACnet. Die DI (Device Integration) Companion Specification definiert generic device modeling und bildet die Basis für die VIA Custom Companion Spec mit Typen wie DeviceType, BlockType und ConfigurableObjectType. Die I4AAS Companion Spec mappt AAS auf OPC UA, wobei AssetAdministrationShell zu UA Object, Submodel zu UA Object und Property zu UA Variable transformiert wird. Die VIA Custom Companion Spec (Vision) definiert VIAProcessType (extends DeviceType), VIARouterType, VIASchedulerType und VIARegistryType.

Das NodeSet XML Format standardisiert Information Models mit `<UANodeSet>` als root-Element und enthält `<UAObject>`, `<UAVariable>`, `<UAMethod>`, `<UAObjectType>` und `<UADataType>` Definitionen. VIA nutzt ein Hybrid Model aus Static NodeSet (VIA types) und Dynamic Instances, die zur Laufzeit erstellt werden, wenn VIA-Prozesse sich registrieren. Aggregationsserver sammeln Daten von vielen Servern in einem einheitlichen Adressraum. Multi-Language-Interoperabilität wird durch python-opcua, Java, .NET und gRPC-Bindings ermöglicht.

Die Code Generation Pipeline für VIA Integration verläuft wie folgt: Das VIA M3 Metamodell wird vom VIA-M3-Compiler in OPC UA NodeSet XML transformiert, das vom open62541 nodeset_compiler.py in C Code (via_nodeset.c/.h) übersetzt wird, der schließlich mit VIA Prozessen (C++23 Modules) gelinkt wird.

Die Limitationen von OPC UA liegen in statischen NodeSets, wobei die Dynamic Address Space API diese Einschränkung für VIA behebt, sowie im Fehlen dynamischer Orchestrierung und Compile-Time-Optimierung in bisherigen Implementierungen.

### 3.3 Multi-Message Broker (Santiago Soler Perez Olaya et al., IEEE ETFA 2024)

Der Multi-Message Broker (MMB) adressiert die Herausforderung der Brownfield-Integration: Legacy-Geräte mit proprietären, inflexiblen Protokollen (Modbus, PROFIBUS, EtherCAT) müssen in moderne AAS-basierte Industrie 4.0-Systeme integriert werden. Der MMB fungiert als Gateway zwischen Northbound-Schnittstellen (I4.0 HTTP API, zukünftig Type 3 Proactive AAS) und Southbound-Protokollen (Modbus, HTTP, MQTT, zukünftig PROFIBUS/EtherCAT/PROFINET). Die Architektur demonstriert, wie heterogene Protokolle durch Mapping-Submodelle (AID/AIMC) systematisch in ein einheitliches AAS-Datenmodell überführt werden können – ein Ansatz, den VIA für die automatische Generierung von Protocol-Adaptern nutzt.

**VIA-Projektintegration**: Der MMB bildet die **M3-Modellgrundlage und Bibliothek** (`playbooks/VIA-M3-Compiler/third_party/mmb/`) für die drei VIA-Sub-Protokolle unter OPC UA. Die MMB-Architektur wird auf M3-Ebene als Basis-Bibliothek implementiert, auf der Edge-Group-Protocol, Deploy-Protocol und Process-Group-Protocol aufbauen. Diese Protokolle werden **virtuell und dynamisch als MMB zwischen Verarbeitungsgruppen auf OPC UA gemappt** – nicht statisch zur Compile-Zeit, sondern dynamisch zur Laufzeit anpassbar.

Die MMB-Konzepte (AID/AIMC Mapping, Consistency Layer, Sync/Async Translation, Many-to-Many Broadcast) werden zweifach genutzt:
1. **Network Discovery** (`playbooks/VIA-M2-SDK/network_discovery.md`): Automatische Erkennung von Brownfield-Geräten, AID-Extraktion, AIMC-Mapping-Generierung als `.via`-Projektdatei-Vorschläge
2. **Dynamische Protokoll-Orchestrierung**: Die 3 Sub-Protokolle organisieren sich **getrennt voneinander** im Gesamtnetz, bilden **geschachtelte und rekursive Sicherheitsstufen** in jeder Protokoll-Ebene, und ermöglichen virtuelle Netzwerkströme mit unterschiedlichen QoS-Garantien (Latenz, Paket-Ankunftssicherheit, Sicherheitsstufen).

Der MMB adressiert das Problem der Brownfield Integration, bei dem Legacy Devices mit inflexiblen Protokollen in moderne Systeme eingebunden werden müssen. Der MMB fungiert als Gateway mit Northbound-Schnittstellen (I4.0 HTTP API, zukünftig Type 3 Proactive AAS) und Southbound-Protokollen (Modbus, HTTP, MQTT, zukünftig PROFIBUS/EtherCAT/PROFINET).

Die interne Architektur umfasst drei Schichten: Der Consistency Layer garantiert, dass identische Requests die gleiche Information zurückgeben, der Mapping Layer wählt den passenden Connector aus und führt Data Transformation durch, und der AAS Storage speichert ein AAS pro Legacy Asset. Das AID/AIMC Submodel-Konzept trennt Vendor-bereitgestellte Informationen (AID - Asset Interfaces Description mit Available Endpoints basierend auf W3C WoT TD) von User-Konfiguration (AIMC - Asset Interfaces Mapping Configuration mit bidirectionalem Mapping zwischen Asset und AAS SubmodelElements).

Die Sync/Async Translation ermöglicht zwei Modi: Entweder wird der latest status gebuffert, oder die Anfrage blockiert, bis eine Response verfügbar ist. AAS Interaction Types werden in drei Stufen klassifiziert: Type 1 (Passive: XML/JSON/RDF Dateiaustausch), Type 2 (Reactive: HTTP API für Request-Response), Type 3 (Proactive: autonomous inter-AAS Kommunikation, derzeit in Standardisierung). Der MMB bildet ein Gateway zwischen Real-time (Hard/Soft Real-time Fieldbus-Systeme) und Non-real-time (HTTP-basierte Cloud-Anbindung). Die Protokoll-Translation überbrückt verschiedene Kommunikationsmuster: Controller/Peripheral, Client/Server und Pub/Sub.

Die Limitationen des MMB liegen darin, dass AIMC keine Data Transformations erlaubt (nur 1:1 Mapping), Type 3 Interaction noch nicht standardisiert ist, und kein vollautomatisches Deployment vorgesehen ist.

### 3.4 CMFM & Management Paradigmen

Das Comprehensive Management Function Model (CMFM) bietet einen theoretischen Rahmen für Human-Centered Management in heterogenen industriellen Netzwerken ("Network of Networks"). Anders als System-Centric Ansätze (SNMP Value-based, SDN Requirements-based) fokussiert CMFM auf Intent-basiertes Management: Anwender beschreiben Ziele (Goals) und gewünschte Ausgaben (Outputs), das System leitet automatisch notwendige Konfigurationen ab. VIA adaptiert die CMFM-Philosophie für die Prozesskommunikation: Das M3-Metamodell definiert ein VIA-Vocabulary (Elements: Process, Service, Registry; Verbs: register, discover, route; IPC Types: Pipe, Socket, TCP, FileQueue, Thread), aus dem der M2-Compiler automatisch Orchestrierungslogik generiert.

**VIA-Projektintegration**: Das VIA Vocabulary ist **noch zu definieren** und wird in `playbooks/VIA-M3-Compiler/via_vocabulary.md` dokumentiert, sobald es aus dem AAS-Kontext extrahiert wurde. Die CMFM-Struktur (Goal, Output, Input, Constraints, Representation) wird auf M3-Ebene als AAS-lang Konstrukte implementiert: Kundenprojekte (`.via` Dateien) beschreiben ihre Ziele intent-basiert (z.B. "Verbinde Sensor A mit Prozess B, maximiere Durchsatz, minimiere Latenz"), der VIA-M2-Compiler leitet daraus automatisch IPC-Mechanismus (Pipe/Socket/TCP/FileQueue/Thread) und Service-Positionierung (gleicher Container/Host/Remote) ab. Die drei Management-Ebenen (Data/Control/Management) werden in VIA sauber getrennt: IPC (Data Plane), Process-Group-Protocol (Control Plane), Deploy-Protocol (Management Plane). Diese Trennung ist in `playbooks/VIA-M3-Compiler/via_protocols/` als M3-Modelle zu spezifizieren.

Das CMFM (Comprehensive Management Function Model) kontrastiert Human-Centered Management mit System-Centric Management und ermöglicht verschiedene Management Paradigmen: Value-based (SNMP mit Polling von Werten), Policy-based (Intent-basierte Zielvorgaben), Requirements-based (SDN/TSN mit QoS-Anforderungen) und Ontology-based (Semantic-basierte Reasoning-Systeme).

Die Stärken von CMFM liegen in Heterogeneity Management für "Network of Networks", Intent-based Abstraktion statt Low-Level-Konfiguration, und Knowledge Transfer durch standardisierte CMF-Definitionen. Das CMFM Meta-Model definiert fünf Komponenten: Goal (mandatory, beschreibt das Ziel), Output (mandatory, beschreibt die erwartete Ausgabe), Input (optional, beschreibt notwendige Eingaben), Constraints (optional, definiert Einschränkungen) und Representation (optional, verschiedene Darstellungsformen).

Constraints werden in fünf Typen klassifiziert: Time (zeitliche Beschränkungen), Order (Reihenfolge-Abhängigkeiten), Existence (Existenz-Bedingungen), Mutual Exclusiveness (gegenseitiger Ausschluss) und Execution Success (Erfolgs-Kriterien). Die Taxonomy ermöglicht hierarchische Composition, wobei Multiple Super-CMFMs möglich sind.

Das VIA Vocabulary definiert Elements (Process, Service, Registry, Scheduler, Router), Verbs (register, discover, route, schedule) und IPC Types (Pipe, Socket, TCP, FileQueue, Thread) als domänenspezifisches Vokabular. Die Separation von Data/Control/Management Plane erfolgt durch IPC (Data Plane), Orchestration (Control Plane) und CMFM (Management Plane), was eine Verbesserung gegenüber Legacy Industrial Systems darstellt.

VIA fungiert als "Network of Networks" mit holistic Management für heterogene IPC-Mechanismen (Pipe, Socket, TCP, FileQueue, Thread) und ermöglicht seamless Integration mit Access to different management systems und orchestration throughout. Das Legacy Problem industrieller Systeme liegt in fehlender Trennung von Data/Control/Management Planes, proprietary Interfaces und statischer Configuration.

Die Limitationen von CMFM liegen darin, dass keine Compiler-Kette vorgesehen ist, CMFM-Erstellung manuell erfolgt, und Vocabulary Management yet-to-standardize ist.

### 3.5 SOA & Microservice Architecture (Santiago Soler Perez Olaya et al., IECON 2024)

Service-orientierte Architekturen (SOA) und Microservices bilden die strukturelle Grundlage für VIA-Prozesse. Die Forschungsarbeit von Santiago Soler Perez Olaya demonstriert, wie AAS-Submodels als eigenständige Microservices implementiert werden können, die über gRPC+Protobuf kommunizieren. Besonders relevant ist die beschriebene Code-Generation-Pipeline: OpenAPI-Spezifikationen (AAS Spec) werden in Protobuf-Definitionen transformiert, aus denen der protoc-Compiler sprachspezifischen Code generiert. VIA erweitert diesen Ansatz um eine zusätzliche Abstraktionsebene (M3-Metamodell) und automatische IPC-Optimierung.

**VIA-Projektintegration**: VIA nutzt **Protobuf auf M3-Ebene** als Interpreter für Metamodell-Definitionen und Kundenprojektdaten (`playbooks/VIA-M3-Compiler/` verwendet Protobuf aus `third_party/`). Der VIA-M3-Compiler generiert `.proto`-Dateien für die Microservice-Kommunikation, die in `playbooks/VIA-M2-SDK/proto/` abgelegt werden. Anders als Santiago Soler Perez Olayas Ansatz (OpenAPI → Protobuf → protoc), folgt VIA dem Pfad: **M3-Metamodell (in AAS-lang) → VIA-M3-Compiler → Protobuf-Definitionen + C++-SDK**. Die "One microservice per Submodel"-Idee wird in VIA umgesetzt: Jedes AAS-Submodel wird als eigenständiger VIA-Prozess (C++23 Module) deployed, wobei der M2-Compiler automatisch gRPC-Service-Stubs generiert. Die IPC-Optimierung wählt dann zur Compile-Zeit: gRPC (Remote), UNIX Socket (lokal, high-performance) oder Thread-Messaging (gleicher Prozess).

Service-orientierte Architekturen (SOA) basieren auf fundamentalen Prinzipien: Modularity für unabhängige Services, Abstraction zur Kapselung von Implementierungsdetails, Loose Coupling für minimale Abhängigkeiten, Service Composition für flexible Kombination, und Reusability für Wiederverwendung über Systemgrenzen hinweg.

Automotive SOA nutzt SOME/IP (Autosar) für Fahrzeug-interne Kommunikation, DDS (Publish/Subscribe) für Echtzeit-Datenverteilung, und OPC UA für Interoperabilität mit Backend-Systemen. Das Microservice Network für AAS implementiert "One microservice per Submodel", wobei Northbound HTTP API für Clients, Internal gRPC für Service-zu-Service-Kommunikation, und Southbound Asset Protocol für Hardware-Anbindung verwendet wird.

Die Kombination von gRPC und Protobuf bietet zahlreiche Vorteile: High-performance mit low-latency durch HTTP/2 multiplexing, language interoperability für C++, C#, Python, Java und Go, binary serialization für compact und efficient Datenübertragung, backward/forward compatibility für versionssichere Evolution, und contract-first paradigm für klare API-Definition.

Die Code Generation Pipeline transformiert OpenAPI (AAS Spec) in Protobuf (.proto files), die vom protoc Compiler in Language-specific Code (messages, service stubs) übersetzt werden. Die AAS SDK Integration nutzt aas-core-csharp für (de-)serialization und metamodel types. Container Deployment erfolgt über Docker und Kubernetes mit transparent relocation, wobei services near workload oder gateway positioniert werden.

Die Limitationen dieses Ansatzes liegen darin, dass Protobuf kein Inheritance unterstützt (resort to composition), eine duality zwischen Protobuf-generated und AAS Core SDK classes besteht, heterogene Protokolle nicht unified sind, und manuelle Orchestrierung erforderlich ist.

### 3.6 IPC, Monitoring & Service Mesh (Related Work)

Die Wahl des IPC-Mechanismus hat fundamentalen Einfluss auf Latenz und Skalierbarkeit verteilter Systeme. Bestehende Lösungen wie gRPC (~0.5ms Latenz, aber keine Service Discovery), UNIX Domain Sockets (~20μs, nur lokal), DDS (Real-Time QoS, ~2ms Overhead) und Service-Mesh-Lösungen wie Istio/Linkerd (Runtime-Routing, 5-10ms Sidecar-Overhead) erfordern manuelle Konfiguration und bieten keine Compile-Time-Optimierung. Für Monitoring existieren etablierte Standards (SNMP für Infrastruktur, OPC UA für Prozessdaten, MQTT für Cloud-Anbindung), jedoch fehlt eine integrierte Sicht. VIA adressiert diese Fragmentierung durch eine Compiler-gestützte Vereinheitlichung: Der M2-Compiler wählt automatisch den optimalen IPC-Mechanismus basierend auf Prozess-Lokalisierung (gleicher Host → Pipe/Socket, Remote → TCP/gRPC) und Latenzanforderungen.

**VIA-Projektintegration**: Der **IPC-Optimizer** in `playbooks/VIA-M2-SDK/ipc_optimizer.md` implementiert einen graph-basierten Algorithmus zur Compile-Time-Auswahl des optimalen IPC-Mechanismus (**Kern dieser Forschungsarbeit**). Die Entscheidungslogik wird im M3-Metamodell als Template-Regeln definiert (`playbooks/VIA-M3-Compiler/templates/ipc_decision_logic.aas`), die der Kunde in seinem M2-Projekt (`.via` Dateien) mit konkreten Constraints instanziiert (z.B. "max_latency: 5ms", "same_host: true").

**Multi-Objective Optimization (Pareto-Optimierung)**: Der M2-Compiler führt zur Compile-Zeit einen Constraint-Solver (Z3) aus, der **Pareto-optimale Lösungen** für konfligierende Ziele findet:
- **Latenz minimieren** (μs-Bereich für Unix Socket, ms-Bereich für TCP)
- **Durchsatz maximieren** (Messages/s, MB/s)
- **Ressourcenverbrauch minimieren** (CPU%, RAM MB, Netzwerkbandbreite)

Eine Lösung ist **Pareto-optimal**, wenn keine Zielgröße verbessert werden kann, ohne eine andere zu verschlechtern. Der Constraint-Solver berechnet die **Pareto-Frontier** (Menge aller nicht-dominierten Lösungen) und wählt basierend auf Kunden-Constraints die beste Trade-off-Lösung. Die 5 IPC-Mechanismen (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) werden als AAS-lang Enumerations im M3 definiert.

**In-the-Loop Selbstoptimierung**: VIA implementiert eine **autonome Cluster-Optimierung** durch kontinuierliche Telemetrie-Auswertung:
- **Telemetrie-Metriken**: CPU-Last (%), RAM-Auslastung (MB), Festplatten-I/O (MB/s), Netzwerk-Latenz (ms), Message-Throughput (Messages/s)
- **Evaluationsschleife**: Deploy-Protocol sammelt Telemetrie von allen Services → M2-Compiler analysiert Bottlenecks → Kubernetes-Lastverteilung wird dynamisch angepasst
- **Scope**: Verarbeitende Services für Messdaten (Edge-Devices → Aggregation → Analytics) + OPC UA Protokollebene (Sub-Protokolle werden virtuell über MMB zwischen Verarbeitungsgruppen umgemappt)
- **Feedback-Loop**: Neue Service-Positionierung wird als Canary-Deployment getestet, bei Verbesserung der Pareto-Metriken permanent übernommen, bei Verschlechterung Rollback in Sekundenbruchteilen

Monitoring-Integration erfolgt über das Deploy-Protocol (Logging, Telemetrie) und OPC UA (Prozessdaten-Exposition).

Die Übersicht bestehender Ansätze zeigt verschiedene Stärken und Schwächen: gRPC nutzt HTTP/2 und Protobuf mit circa 0.5ms Latenz im Single-Host-Betrieb, bietet jedoch keine integrierte Service Discovery. ZeroMQ implementiert Message Queues mit fünf Patterns (REQ/REP, PUB/SUB), verfügt jedoch über keine Compiler-Integration. DDS (OMG Data Distribution Service) ist für Real-Time optimiert mit QoS-Policies, verursacht aber circa 2ms Overhead und bietet keine Metamodell-Abstraktion.

Service Mesh Lösungen wie Istio und Linkerd ermöglichen Runtime-Routing mit Dynamic Discovery, verursachen jedoch 5-10ms Sidecar-Overhead pro Request. UNIX Domain Sockets bieten circa 20μs Latenz für lokale Prozesse, unterstützen jedoch keine verteilte Orchestrierung über Host-Grenzen hinweg.

SNMP (Simple Network Management Protocol) implementiert ein Manager-Agent-Model mit Polling (GET-Anfragen alle 60 Sekunden) und Traps (Push bei Ereignissen), nutzt eine hierarchische MIB-OID-Struktur und definiert Standard-MIBs wie IF-MIB, HOST-RESOURCES-MIB und ENTITY-SENSOR-MIB. Die Grenzen von SNMP liegen in der flachen OID-Liste ohne Objekthierarchien, im Polling-Paradigma ohne Pub/Sub-Unterstützung, in der primären Fokussierung auf Monitoring statt Steuerung, und im Skalierungslimit bei tausenden Geräten.

MQTT (Message Queuing Telemetry Transport) ist Pub/Sub-basiert und Broker-zentriert, optimiert für IoT-Sensorik und Cloud-Anbindung, und extrem schlank für bandbreite-kritische Anwendungen. Ein empfohlener Hybrid-Ansatz kombiniert SNMP für Infrastruktur-Monitoring, OPC UA für detaillierte Prozessdaten, und MQTT für Cloud Analytics.

Die fundamentale Limitation aller genannten Ansätze liegt darin, dass sie manuelle Konfiguration erfordern, keine Compile-Time-Optimierung bieten, und heterogene Protokolle nicht unified verwalten können.

### 3.7 Forschungslücken

Die Analyse des Stands der Forschung offenbart mehrere fundamentale Lücken, die diese Arbeit adressiert. Es existiert keine mehrstufige Compiler-Kette M3→M2→M1 speziell für Prozesskommunikation, die Metamodell-Definitionen automatisch in optimierte IPC-Implementierungen übersetzt. Die automatische IPC-Mechanismus-Auswahl bei Compilation ist in bisherigen Frameworks nicht vorgesehen; stattdessen erfolgt die Wahl zur Laufzeit oder durch manuelle Konfiguration.

Unter OPC UA sind keine standardisierten Sub-Protokolle für Prozessgruppierung, Deployment-Management und IPC-Optimierung definiert, obwohl diese Funktionalität in industriellen Systemen dringend benötigt wird. Die Compile-Time-Optimierung von Microservice-Positionierung basierend auf Prozessabhängigkeiten und Latenzanforderungen ist ein unerforschtes Gebiet.

Der Trade-off zwischen Service Mesh Overhead (5-10ms Sidecar-Latenz) und potenzieller Compiler-Optimierung wurde wissenschaftlich nicht systematisch untersucht. In-the-Loop Selbstoptimierung mit Pareto-Metriken (Latenz, Durchsatz, Ressourcenverbrauch) als autonome Feedback-Schleife existiert in keinem bekannten industriellen Framework. Schließlich fehlt das Konzept der M3-Bibliotheks-Komposition für Protokoll-Erweiterbarkeit, bei dem neue Protokolle auf bestehenden M3-Bibliotheken aufbauen können.

### 3.8 Wissenschaftlicher Mehrwert dieser Arbeit

Die vorliegende Forschungsarbeit leistet mehrere fundamentale Beiträge, die über inkrementelle Verbesserungen bestehender Systeme hinausgehen:

#### 3.8.1 Theoretische Fundierung durch M3-Bibliotheks-Architektur

**MMB als M3-Bibliothek**: Die Einbettung des Multi-Message Broker (MMB) als wiederverwendbare M3-Bibliothek demonstriert, wie Forschungsergebnisse aus der Brownfield-Integration (Santiago Soler Perez Olaya et al.) als formale Metamodell-Komponenten operationalisiert werden können. Die drei VIA-Sub-Protokolle (Edge-Group, Deploy, Process-Group) sind **selbst als M3-Bibliotheken in AAS-lang definiert** – analog zu Protobuf als M3-Interpreter – und laden Modelle von MMB. Diese Modell-Komposition auf M3-Ebene schafft eine **wissenschaftliche Grundlage für erweiterbare Protokoll-Architekturen** in der industriellen Automatisierung.

**Wiederverwendbarkeit und Erweiterbarkeit**: Durch die Trennung von Basis-Bibliothek (MMB) und spezialisierten Protokollen (Edge-Group/Deploy/Process-Group) entsteht eine modulare Architektur, die zukünftige Erweiterungen ermöglicht. Andere Forschungsprojekte können MMB-Modelle importieren und eigene Protokoll-Semantik definieren – ein Paradigma, das in bisherigen OPC UA Companion Specifications fehlt.

#### 3.8.2 Mathematische Rigorosität durch Pareto-Optimierung

**Multi-Objective Optimization**: Die Anwendung von Pareto-Optimierung auf IPC-Mechanismus-Auswahl überführt eine bisher heuristische Entscheidung in ein **formal lösbares Optimierungsproblem**. Die konfligierenden Ziele (Latenz minimieren, Durchsatz maximieren, Ressourcenverbrauch minimieren) werden nicht durch Ad-hoc-Gewichtung gelöst, sondern durch Berechnung der **Pareto-Frontier** – der Menge aller nicht-dominierten Lösungen. Dies ermöglicht eine **wissenschaftlich nachvollziehbare Begründung** für jede IPC-Entscheidung und schafft Vergleichbarkeit zwischen Systemen.

**Z3 Constraint-Solver**: Die Integration eines formalen Constraint-Solvers zur Compile-Zeit hebt die Arbeit über empirische Benchmarks hinaus. Die Lösungen sind nicht nur "gut gemessen", sondern **beweisbar optimal** innerhalb der definierten Constraints.

#### 3.8.3 Autonome Systeme durch In-the-Loop Selbstoptimierung

**Feedback-Loop-Architektur**: Die kontinuierliche Telemetrie-Auswertung (CPU%, RAM, Disk I/O, Netzwerk-Latenz, Message-Throughput) mit automatischer Kubernetes-Lastverteilung realisiert **autonome Cluster-Optimierung** – eine Kernvision von Industrie 5.0. Die Evaluationsschleife (Deploy-Protocol sammelt → M2-Compiler analysiert → Lastverteilung anpassen → Canary-Test → Übernahme/Rollback) demonstriert **selbstadaptierende Systeme** ohne menschliche Intervention.

**Wissenschaftlicher Beitrag**: Diese Arbeit zeigt erstmals, wie Compile-Time-Optimierung (Pareto-Frontier) und Runtime-Adaptation (Telemetrie-Feedback) **komplementär kombiniert** werden können. Bestehende Ansätze sind entweder rein statisch (manuelle Konfiguration) oder rein dynamisch (Service Mesh) – VIA vereint beide Paradigmen.

#### 3.8.4 Geschachtelte Sicherheitsarchitekturen

**Rekursive Sicherheitsstufen**: Die Fähigkeit jeder Protokoll-Ebene, **getrennt voneinander** hierarchische Sicherheitsregeln zu bilden (z.B. Device-Groups → Edge-Groups → Cluster-Groups → Global), adressiert Enterprise-Anforderungen in heterogenen Netzwerken. Diese Architektur ist wissenschaftlich relevant, da sie **Separation of Concerns** auf Protokoll-Ebene realisiert – ein bisher ungelöstes Problem in OPC UA Companion Specifications.

**Dynamisches MMB-Mapping**: Die Fähigkeit, Sub-Protokolle **virtuell zwischen Verarbeitungsgruppen umzumappen** (z.B. bei Bottleneck: neue Services instanziieren, Datenströme umleiten), demonstriert **Runtime-Adaptivität** trotz Compile-Time-Optimierung – ein fundamentaler Widerspruch, den VIA durch die Trennung von Protokoll-Definition (M3, statisch) und Protokoll-Instanziierung (MMB, dynamisch) auflöst.

#### 3.8.5 Brückenschlag zwischen Compiler-Design und Industrieautomatisierung

**Interdisziplinäre Innovation**: Die Anwendung von Compiler-Optimierungstechniken (M3/M2/M1 Metamodell-Kette, Constraint-Solving, Code-Generierung) auf industrielle Prozesskommunikation (OPC UA, IPC, Service-Orchestrierung) schafft eine **neue Forschungsrichtung** an der Schnittstelle von Informatik und Automatisierungstechnik. Die Arbeit zeigt, dass Industrie 4.0-Probleme von Compiler-Perspektive aus lösbar sind – eine Perspektive, die in bisherigen AAS-Implementierungen (Python-Skripte, manuelle Orchestrierung) fehlt.

---

## 4. Zielsetzung und Forschungsmethodik

### 4.1 Hauptziel

Das übergeordnete Ziel dieser Forschungsarbeit ist die Entwicklung und Evaluierung eines vollautomatischen Compiler-Systems für Industrie 4.0-Systeme mit Fokus auf das **Process-Group-Protocol-Subsystem**. Im Gegensatz zu bestehenden Ansätzen, die IPC-Mechanismen manuell oder zur Laufzeit wählen, soll VIA diese Entscheidung zur Compile-Zeit treffen und dabei Latenz, Durchsatz und Ressourcenverbrauch optimieren.

### 4.2 Teilziele

Die Forschungsarbeit gliedert sich in fünf Teilziele, wobei sich die vorliegende Arbeit primär auf T2 (IPC-Optimierung) und T4 (Process-Group-Protocol) konzentriert:

- **T1 (Kontext)**: VIA-M3-Compiler – Transformation AAS M3 Metamodell → C++ SDK
- **T2 (Forschungsfokus)**: VIA-M2-SDK-Compiler – Automatische IPC-Mechanismus-Auswahl basierend auf Prozessabhängigkeiten
- **T3 (Kontext)**: VIA-M1-System-Deployer – Distributed Compilation, Horse-Rider-Deployment, Kubernetes-Orchestrierung
- **T4 (Forschungsfokus)**: Sub-Protokoll-Design – Spezifikation und Implementierung des Process-Group-Protocol unter OPC UA
- **T5 (Ausblick)**: KI-Integration Industrie 5.0 – Natürlichsprachliche Systembeschreibung → Automatische Compilation

### 4.3 Forschungsmethodik

Die Forschungsmethodik folgt einem ingenieurwissenschaftlichen Ansatz mit vier Hauptphasen: Requirements Engineering, Design, prototypische Implementierung und experimentelle Evaluation.

#### 4.3.1 Methodisches Vorgehen

**Phase 1 – Requirements Engineering**: Definition der M3-Modellelemente zur Beschreibung von Prozesskommunikation als AAS-Extension. Dies umfasst die Spezifikation von Abhängigkeitstypen (datengetrieben, steuergetrieben, zeitgetrieben), Latenzanforderungen (Soft-Realtime, Best-Effort) und Ressourcenbeschränkungen (Memory, CPU, Bandbreite).

**Phase 2 – Design**: Entwicklung eines Compiler-Optimierungsalgorithmus zur IPC-Mechanismus-Auswahl. Der Algorithmus modelliert Prozessabhängigkeiten als gerichteten Graphen, auf dem ein Constraint Solver (z.B. Z3) eine Pareto-optimale Lösung für Latenz, Durchsatz und Ressourcenverbrauch berechnet.

**Phase 3 – Prototypische Implementierung**: Implementierung des M2-SDK-Compilers mit IPC-Optimizer in C++20/23. Der Prototyp generiert aus M2-Projektkonfigurationen vollständige Systemprojekte mit optimiertem IPC-Setup (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging).

**Phase 4 – Evaluation**: Experimentelle Validierung mittels Benchmark-Suite und Real-World Use-Case. Vergleichsmessungen gegen etablierte Baselines (gRPC, Istio Service Mesh, UNIX Sockets) zur Validierung der Hypothesen H1-H4.

#### 4.3.2 Evaluationsumgebung
- **Labor-Setup**: 3-Node Kubernetes Cluster (64 Core, 256 GB RAM, 10 Gbit/s Netzwerk)
- **Simulationstools**: Mininet für virtuelle Netzwerktopologien (bis 1.000 Nodes)
- **Benchmark-Szenarien**:
  - **S1**: Lokale Prozesskette (5 Services, gleicher Host)
  - **S2**: Verteilte Prozesskette (20 Services, 3 Hosts)
  - **S3**: Skalierungstest (100.000 Services, hierarchische Gruppierung)
  - **S4**: Real-World Use-Case (Industrieller SCADA + MES + PLC-Edge-Integration)

#### 4.3.3 Metriken & Erfolgskriterien
- **Latenz**: End-to-End Prozesskette (P50, P95, P99 Perzentile)
- **Throughput**: Nachrichten/Sekunde (Messages/s)
- **CPU-Last**: Prozessor-Auslastung bei Last (%)
- **Memory Footprint**: RAM-Verbrauch pro Service (MB)
- **Entwicklungszeit**: Manual vs. Metamodell-generiert (Stunden)
- **Erfolgskriterium**: H1-H4 bestätigt (siehe Hypothesen Kapitel 2.2)

#### 4.3.4 Vergleichsbaseline
- **Baseline 1**: Manuell konfiguriertes gRPC (statisch)
- **Baseline 2**: Istio Service Mesh (dynamisch)
- **Baseline 3**: UNIX Sockets (optimal, nur lokal)
- **VIA Process-Group-Protocol**: Compiler-optimiert

#### 4.3.5 Phasenplan
- **Phase 1**: Research & Analyse ✅ ABGESCHLOSSEN
- **Phase 2**: Playbook-Erstellung & Metamodell-Design ⏳ IN PROGRESS
- **Phase 3**: M2-SDK-Compiler Prototyp mit IPC-Optimizer (6 Wochen)
- **Phase 4**: Benchmark-Suite & Use-Case-Implementierung (4 Wochen)
- **Phase 5**: Evaluation & Vergleichsmessungen (4 Wochen)
- **Phase 6**: Dokumentation & Publikation (4 Wochen)

---

## 5. Theoretischer Hintergrund

Die Forschungsarbeit vereint Konzepte aus Compiler-Theorie (Abschnitt 5.1), Metamodell-Architekturen (Abschnitt 5.2), AAS-Standards (Abschnitt 5.3), OPC UA und ISA-95 Integration (Abschnitt 5.4), Prozesskommunikation (Abschnitt 5.5) sowie Management-Frameworks (Abschnitt 5.6). Dieses interdisziplinäre Fundament ist notwendig, um die Herausforderungen metamodell-basierter IPC-Optimierung zu adressieren.

### 5.1 Compiler-Theorie

Die Compiler-Theorie bildet die technische Grundlage für VIA mit Multi-Stage Compilation über drei Ebenen (M3 → M2 → M1), wobei jede Stufe spezifische Transformationen durchführt. Die Code-Generation erfolgt Template-basiert und Type-Safe, um Typsicherheit bereits zur Compile-Zeit zu garantieren. Metaprogramming nutzt C++20 Concepts für Constraint-basierte Template-Spezialisierung und Constexpr für Compile-Time-Berechnung komplexer Ausdrücke.

### 5.2 Metamodell-Architekturen (M3/M2/M1)

Die Metamodell-Architektur gliedert sich in drei Abstraktionsebenen: M3 definiert das Metamodell, in dem Objects, Variables und Methods als abstrakte Konzepte existieren; M2 repräsentiert das Modell mit VIA-spezifischen Typen wie VIAProcessType und VIARouterType; M1 bildet die Instanz-Ebene mit laufenden Systemen und konkreten Prozess-Instanzen.

### 5.3 Asset Administration Shell

Die Asset Administration Shell nach IEC 63278 definiert ein standardisiertes Metamodell für digitale Zwillinge in der Industrie 4.0. Submodels ermöglichen modulare Datenbeschreibung durch unabhängige, wiederverwendbare Komponenten. Das AID/AIMC-Konzept trennt Asset Interface Description (Vendor-bereitgestellte Schnittstellendefinition) von Asset Interfaces Mapping Configuration (User-konfiguriertes Mapping zwischen Asset und AAS).

### 5.4 OPC UA Information Model & ISA-95 Integration

Das OPC UA Information Model basiert auf M3-basierten Typdefinitionen, die ein Metamodell für Objekte, Variablen und Methoden bereitstellen. Companion Specifications erweitern OPC UA um Domain-spezifische Funktionalität, darunter DI (Device Integration), I4AAS (Industrie 4.0 AAS), und PLCopen. Der Address Space organisiert Nodes hierarchisch und objektorientiert.

Die ISA-95 Levels definieren funktionale Ebenen: Level 2 (SCADA: Prozessebene mit Echtzeit-Anforderungen), Level 3 (MES: Produktionsleitebene), und Level 4 (ERP: Unternehmensebene). SCADA-Systeme erfassen Prozessdaten, senden Steuerbefehle, verwalten Alarmierung und Historisierung, und bieten Visualisierung über HMI. MES-Systeme verwalten Produktionsaufträge, führen Feinplanung durch, implementieren Qualitätssicherung, berechnen OEE und KPIs, ermöglichen Rückverfolgung, und kommunizieren bidirektional mit SCADA. OPC UA fungiert als Vermittler und bietet standardisierten Zugriff für SCADA, MES, ERP und Cloud-Systeme.

### 5.5 Prozesskommunikation

Die Prozesskommunikation nutzt verschiedene IPC Mechanisms: Pipe für sequenzielle Prozessketten, Socket für lokale bidirektionale Kommunikation, TCP für Remote-Kommunikation, File-Queue für asynchrone persistente Nachrichten, und Thread-Messaging für intra-prozessuale Kommunikation. Die Architektur trennt Data Plane (eigentliche Datenübertragung), Control Plane (Routing und Orchestrierung) und Management Plane (Konfiguration und Monitoring). gRPC und Protobuf implementieren Contract-First Development mit Binary Serialization für kompakte und effiziente Datenübertragung.

### 5.6 CMFM (Comprehensive Management Function Model)

Das CMFM implementiert ein Manager-Centric Paradigm, das auf Ziele statt System-Details fokussiert im Gegensatz zu System-Centric Ansätzen. CMF Komponenten umfassen Goal (mandatory, beschreibt Managementziel), Output (mandatory, erwartete Ausgabe), Input (optional, benötigte Eingaben), Constraints (optional, Einschränkungen) und Representations (optional, verschiedene Darstellungsformen).

Die Generality Hierarchy definiert Abstraktionsebenen: Implementation (konkrete Implementierung), User (benutzerspezifisch), Domain (domänenspezifisch), Parent Domain (übergeordnete Domäne). VIA as Domain repräsentiert die gesamte Prozesskommunikations-Domain als einheitliches Konzept. Catalog vs. Core unterscheidet zwischen der Liste aller CMFs und allgemein anwendbaren CMFs nach Promotion.

Promotion erfolgt tacit (automatisch durch häufige Nutzung) oder explicit (durch Standardization Bodies). CMF Interrelations umfassen Equivalence (Merge gleicher Goals zu einem CMF) und Composition (Upwards: Zusammenfassung mehrerer CMFs, Downwards: Zerlegung in Sub-CMFs). Die AAS Integration bildet CMFs als Operations im AAS Meta-Model ab, wobei Input und Output als Attributes repräsentiert werden.

VIA CMFs definieren process-register (Prozess-Registrierung), process-discover (Service Discovery), route-message (Nachrichten-Routing) und schedule-task (Task-Scheduling). Vocabulary Management erfolgt über ein öffentliches Repository mit Verknüpfung zu e-Class, CDD (Common Data Dictionary) und I4.0 SemanticID.

---

## 6. Konzeptioneller Ansatz: VIA-Architektur

### 6.0 VIA-Hauptprogramm (Orchestrierung M3→M2→M1)

**Projektlokation**: `src/main.cpp` (versioniert)

#### Input
- Benutzerbeschreibung des gewünschten Systems (Code-Kommentare in `.via` Dateien oder natürlichsprachliche Textdatei für zukünftige KI-Integration)
- Konfiguration: Target-Architekturen (MIPS, RISC-V, x86, ARM, etc.), Deployment-Ziele (Kubernetes Cluster, Edge-Devices), Netzwerk-Topologie (optional via Network Discovery)

#### Verarbeitung
- **Phase-Coordination**: Sequenzieller Aufruf des 8-stufigen Bootstrap-Zyklus (siehe Abschnitt 2.3.0): M3-Compiler-Build → M3-Test → M2-SDK-Generation → M2-SDK-Build → Kundenprojekt-Compilation → M1-System-Build → Deployment → Servermodus
- **Pipeline-Management**: Output jeder Phase wird Input der nächsten, gespeichert in versionierten (`build/via-m3-compiler`, `src/main.cpp`) oder gitignored Ordnern (`playbooks/VIA-M2-SDK/`, `playbooks/VIA-M1-System/`, `build/binaries/`)
- **Zustandsverwaltung**: Persistierung Zwischenergebnisse als CMake-Build-Artefakte und generierte Projektordner
- **Fehlerbehandlung**: Rollback bei Fehler durch Versionskontrolle (git) für versionierte Teile, Transaktionale Neuausführung für gitignored Teile
- **Anwenderinteraktion**: CLI mit strukturiertem Output (Fortschrittsbalken, Testresultate), OPC UA Server für Remote-Monitoring

#### Output
- **Ende-zu-Ende**: Von `.via` Kundenprojektdateien bis deployed System auf >50.000 Edge-Geräten
- **Traceability**: Kompletter Audit-Trail (Kommentare propagieren durch M3→M2→M1→M0, landen in Binary-Headers)
- **Logs**: Jede Phase dokumentiert in `build/logs/` (für Debugging, Reproduzierbarkeit), Deploy-Protocol für Remote-Logs
- **Deployed Binaries**: `build/binaries/{arch}/{device_id}/` mit Header-Dokumentation

#### Besonderheit
- **Selbstreferenz**: Hauptprogramm kann sich selbst neu kompilieren (M3→M2→M1→M0), startet neue Instanz über Prozesskommunikation und beendet sich nach erfolgreichem Handover
- **Transaktionalität**: Atomare Phasen mit Rollback-Mechanismus (alte Binaries vorgehalten für sekundenschnelles Rollback)
- **Parallelisierung**: Mehrere Kundenprojekte gleichzeitig orchestrieren (GitHub Runners für Distributed Compilation, siehe Abschnitt 2.3.3)

### 6.1 VIA-M3-Compiler (Metamodell → SDK)

**Projektlokation**: `playbooks/VIA-M3-Compiler/` (versioniert)

Der VIA-M3-Compiler empfängt als Input die AAS IEC 63278 Textspezifikation, die über SITL (Software-in-the-Loop) automatisch in M3-Code transformiert wird, OPC UA IEC 62541 als M3-Bibliothek (ebenfalls über SITL eingelesen, falls nicht vorhanden), sowie VIA-Extensions für Prozesskommunikation als custom M3-Definitionen in AAS-lang.

Die Verarbeitung erfolgt durch C++20/23 Metaprogramming mit einem custom Template-Engine, der in AAS-lang selbst definiert ist (nicht in Python wie bei aas-core-works). Constraint-Validation wird über das M3-Testframework durchgeführt, wobei Protobuf als M3-Interpreter aus `third_party/protobuf` zum Einlesen von Modell und Kundendaten verwendet wird.

Als Output generiert der Compiler das Verzeichnis `playbooks/VIA-M2-SDK/` mit gitignored, generiertem C++ Code, OPC UA NodeSet XML in `output/via_companion_spec.xml`, Protobuf `.proto` Dateien für Microservice-Kommunikation in `proto/`, sowie umfassende Dokumentation mit durchgereichten M3-Kommentaren, die bis in die Binary-Headers propagieren.

Die Besonderheit liegt darin, dass der Compiler wartbar und versioniert ist im Gegensatz zu aas-core-works Python-Skripten, als produktionsreifer Compiler mit vollständigem Testframework konzipiert ist, und Spaghetti-Code durch ein mehrschichtiges Constraint-System vermeidet.

### 6.2 VIA-M2-SDK-Compiler (SDK → Kundensystem)

**Projektlokation**: `playbooks/VIA-M2-SDK/` (generiert, gitignored)

Der VIA-M2-SDK-Compiler empfängt als Input Kundenprojekt-Dateien (`customer_project/*.via` in AAS-lang geschrieben), optional eine Netzwerk-Topologie via Network Discovery (`network_discovery.md`), sowie Deployment-Ziele mit Zielarchitekturen und Betriebssystemen.

Die Verarbeitung umfasst mehrere Phasen: Zunächst erfolgt Syntax-Prüfung der `.via` Dateien, gefolgt vom Network Discovery Scanner für SNMP, OPC UA und Modbus. Auto-Vorschläge für Systemkonfiguration werden über `auto_suggestions.md` generiert. Die IPC-Optimierung in `ipc_optimizer.md` bildet den Forschungsfokus und implementiert einen graph-basierten Algorithmus mit Constraint-Solver für Compile-Time-Entscheidungen. Der Test-Generator in `test_generator.md` erstellt automatisch deterministische Tests aus M3-Constraints.

Als Output generiert der Compiler das Verzeichnis `playbooks/VIA-M1-System/` (gitignored, vollständiges C++ Gesamtprojekt), Kubernetes Manifests als `deployment.yaml`, Edge-Modules als C++23 Modules für Horse-Rider-Deployment, sowie generierte Tests mit durchgereichten Kundenkommentaren für vollständige Traceability.

Die Besonderheit liegt im Release-Modus, bei dem der C++-Output-Stream über Memory-Filesystem/RAM direkt mit Pipe in g++ kompiliert wird für maximale Performance, sowie im Debug-Modus, der Projektdateien mit umfassender Dokumentation für Entwickler-Einsicht bereitstellt.

### 6.3 VIA-M1-System-Deployer (System → Produktion)

**Projektlokation**: `playbooks/VIA-M1-System-Deploy/` (Playbooks für Deployment-Logik)

Der VIA-M1-System-Deployer empfängt als Input das M1-Systemprojekt aus `playbooks/VIA-M1-System/`, Deployment-Targets als Architecture Map für MIPS, RISC-V, ARM, x86 und weitere Architekturen, sowie kundendefinierte Systemtests als grobe Vordefinition.

Die Verarbeitung erfolgt in mehreren spezialisierten Phasen: Distributed Compilation über GitHub Runners ermöglicht parallele Builds aller Module (siehe `distributed_build.md`). Cross-Compilation mit Multi-Architektur Toolchain Management wird in `cross_compilation.md` durchgeführt. Horse-Rider-Deployment mit C++23 Modules, stabilen ABIs, Hot-Reload und Canary Deployment erfolgt nach `horse_rider_deployment.md`. Master Active Management orchestriert das gesamte Deployment gemäß `master_active_management.md`.

Als Output entsteht ein deployed System für mehr als 50.000 Edge-Geräte mit Binaries in `build/binaries/{arch}/{device_id}/`, Deployment-Manifests für Kubernetes und Edge-Geräte, versionierte Binaries mit Header-Dokumentation für externe Edge-Programmierung, sowie ein Digital Twin mit Monitoring und Logging.

Die Besonderheit liegt im Hot-Reload-Mechanismus, bei dem der Horse-Service ein neues Rider-Service parallel zum alten lädt, einen Canary-Test durchführt, und bei Erfolg den Traffic switched. Rollback erfolgt in Sekundenbruchteilen bei Fehlern durch Vorhalten der alten Version. Redundanz wird durch mindestens zwei parallele Horses pro Edge-Gerät als Digital Twin gewährleistet.

### 6.4 Sub-Protokolle unter OPC UA

**Projektlokation**: `playbooks/VIA-M3-Compiler/via_protocols/` (zukünftig, **Spezifikation in Planung**)

**M3-Bibliotheks-Architektur**: Die drei VIA-Sub-Protokolle sind **selbst als M3-Bibliotheken in AAS-lang definiert** (analog zu Protobuf als M3-Interpreter). Sie werden in `playbooks/VIA-M3-Compiler/via_protocols/` als Modelle implementiert und **laden Modelle von der MMB-Bibliothek** (`playbooks/VIA-M3-Compiler/third_party/mmb/`) als Basis.

Die MMB-Architektur (Consistency Layer, Mapping Layer, Many-to-Many Broadcast) wird auf M3-Ebene als wiederverwendbare Bibliothek implementiert. Die drei Sub-Protokolle importieren MMB-Modelle und erweitern diese um VIA-spezifische Semantik:
- **Edge-Group-Protocol**: Importiert MMB-Broadcast-Modelle → erweitert um hierarchische Gruppierung
- **Deploy-Protocol**: Importiert MMB-Mapping-Modelle → erweitert um Versionierung/Telemetrie
- **Process-Group-Protocol**: Importiert MMB-Consistency-Modelle → erweitert um IPC-Optimierung

Diese Modell-Komposition auf M3-Ebene ermöglicht **Wiederverwendbarkeit** und **Erweiterbarkeit** – analog zu Protobuf, das ebenfalls Modelle lädt und transformiert.

#### 6.4.1 Edge-Group-Protocol (Außenwelt-Ebene)

Das Edge-Group-Protocol implementiert virtuelle Netzwerkgruppen für hierarchische Edgegeräte-Gruppierung und vermeidet einzelne Koordination durch intelligente Gruppierung von Zielen.

Die Architektur basiert auf hardcoded Messages, wobei Gruppeneigenschaften zur Compile-Zeit in Binaries kompiliert werden, um Runtime-Code-Changes aus Sicherheitsgründen zu verhindern. Binary ABI-Stabilität wird durch C++23 Modules mit stabilen Schnittstellen gewährleistet, sodass jedes Edge-Gerät selbst weiß, wohin es gehört. Geschachtelte Sicherheitsstufen ermöglichen hierarchische Gruppierung (Device-Groups → Edge-Groups → Cluster-Groups → Global) mit rekursiven Sicherheitsregeln pro Ebene. Virtuelle Netzwerkströme unterteilen die Außenwelt in getrennte Verarbeitungsgruppen mit unterschiedlichen QoS-Garantien für Latenz, Durchsatz und Paket-Ankunftssicherheit.

Die Performance profitiert davon, dass kein virtueller Router notwendig ist, wodurch Zeitkritikalität gewahrt bleibt, da Routing-Entscheidungen bereits zur Compile-Zeit getroffen werden. Dynamisches MMB-Mapping ermöglicht, dass Edge-Groups zur Laufzeit virtuell über MMB zwischen Verarbeitungsgruppen umgemappt werden können, beispielsweise bei Netzwerk-Rekonfiguration, Ausfall oder Lastverschiebung.

#### 6.4.2 Deploy-Protocol (Verwaltungs-Ebene)

Das Deploy-Protocol verwaltet Versionierung, Systemupdates und Rejuvenation für das Horse-Rider-System und bildet damit die Verwaltungs-Ebene der VIA-Architektur.

Die Architektur implementiert strikte Separation, wobei Metadaten und Messdaten der Computer getrennt von Anlagendaten verwaltet werden zur Kapselung verschiedener Verantwortlichkeiten. Logging umfasst Netzwerk-Logs für Fehleranalyse sowie Telemetrie-Sammlung von CPU-Last in Prozent, RAM-Auslastung in Megabyte und Disk I/O. Die Horse-Rider-Integration ermöglicht Protokollverwaltung durch den Deployment-Service mit Canary-Deployment, Hot-Reload und Rollback-Mechanismen. Geschachtelte Sicherheitsstufen definieren Versionierungs-Policies pro Cluster oder Gruppe, beispielsweise "Production: nur Stable" oder "Staging: Canary erlaubt".

In-the-Loop Selbstoptimierung wird durch eine kontinuierliche Feedback-Schleife realisiert: Das Deploy-Protocol sammelt Telemetrie von allen Services, der M2-Compiler analysiert Bottlenecks, Kubernetes-Lastverteilung wird dynamisch angepasst, neue Positionierung wird als Canary getestet, und bei Verbesserung der Pareto-Metriken (Latenz, Durchsatz, Ressourcenverbrauch) wird die neue Konfiguration permanent übernommen.

Dynamisches MMB-Mapping ermöglicht, dass Deployment-Gruppen zur Laufzeit neu organisiert werden können, beispielsweise indem alle Analytics-Services auf dedizierte High-RAM-Nodes verschoben werden.

#### 6.4.3 Process-Group-Protocol (Datenebene) → **Kern dieser Forschungsarbeit**

Das Process-Group-Protocol bildet den Kern dieser Forschungsarbeit und implementiert transparente IPC-Optimierung zwischen Services, wobei Programm-Steuerung von Daten getrennt wird.

Die Architektur definiert fünf IPC-Mechanismen (Pipe, Unix Socket, TCP, File-Queue, Thread-Messaging) als AAS-lang Enumerations im M3-Metamodell. Die Automatisierung erfolgt durch den M2-SDK-Compiler, der automatisch Prozessketten von Mikroservices basierend auf Prozessabhängigkeiten erstellt. Compile-Time-Optimierung nutzt einen Constraint-Solver (Z3), der die Pareto-Frontier für konfligierende Ziele (Latenz minimieren, Durchsatz maximieren, Ressourcenverbrauch minimieren) berechnet. Cluster-Verteilung ermöglicht virtuelle Weiterverarbeitung oder Gliederung in Unteraufgaben auf anderen Containern oder Maschinen. Geschachtelte Sicherheitsstufen erlauben, dass IPC-Kommunikation pro Prozess-Gruppe unterschiedliche Verschlüsselungs- und Authentifizierungs-Level haben kann.

Dynamisches MMB-Mapping ermöglicht, dass die Prozesskommunikations-Topologie zur Laufzeit über MMB umgemappt werden kann. Eine typische Pipeline verläuft von Edge-Devices über Aggregation-Services zu Analytics-Services. Bei Bottlenecks können neue Aggregation-Services instanziiert und Datenströme über virtuelles Mapping umgeleitet werden. Das Sub-Protokoll organisiert sich getrennt von Edge-Group-Protocol und Deploy-Protocol im Gesamtnetz, wodurch unabhängige Optimierung jeder Ebene möglich wird.

Eine Windows-Limitation besteht darin, dass auf Windows-Systemen die IPC-Möglichkeiten begrenzter sind, insbesondere fehlen Unix Sockets als hochperformante lokale Kommunikationsoption.

---

**Protokoll-Interaktion**: Die drei Sub-Protokolle können sich **getrennt voneinander** im Gesamtnetz organisieren und gruppieren, jedes mit eigenen **geschachtelten und rekursiven Sicherheitsstufen**. Die dynamische Orchestrierung über MMB ermöglicht virtuelle Netzwerkströme mit unterschiedlichen Eigenschaften (Latenz-kritisch, Durchsatz-optimiert, Sicherheits-gehärtet).

**Status**: Spezifikation der 3 Protokolle wird im Projektverlauf als M3-Modelle definiert, basierend auf MMB-M3-Bibliothek

---

## 7. Erwartete Ergebnisse

Die Forschungsarbeit strebt sowohl wissenschaftliche Beiträge (Abschnitt 7.1) als auch praktische Ergebnisse (Abschnitt 7.2) an. Die Evaluation erfolgt anhand eines konkreten Use-Case-Szenarios aus der Automobilproduktion (Abschnitt 7.3), das die industrielle Relevanz demonstriert. Die erwarteten Ergebnisse adressieren direkt die formulierten Hypothesen H1-H4 und tragen zur Schließung der identifizierten Forschungslücken bei.

### 7.1 Wissenschaftliche Beiträge (Fokus Prozesskommunikation)

Die wissenschaftlichen Beiträge dieser Arbeit umfassen fünf Kernelemente. Beitrag B1 liefert eine Metamodell-Extension für Prozesskommunikation in AAS M3, implementiert als VIA-Extensions in `playbooks/VIA-M3-Compiler/`, die IPC-Typen (Pipe, Socket, TCP, FileQueue, Thread) als AAS-lang Enumerations definiert und ein Constraint-System für Latenzanforderungen und Ressourcenbeschränkungen bereitstellt.

Beitrag B2 entwickelt einen Compiler-Optimierungsalgorithmus für IPC-Mechanismus-Auswahl, implementiert in `playbooks/VIA-M2-SDK/ipc_optimizer.md`, der einen graph-basierten Ansatz mit Constraint-Solver (Z3) nutzt, Pareto-Optimierung für Latenz, Durchsatz und Ressourcenverbrauch durchführt, und Compile-Time-Entscheidungen mit optionaler Runtime-Anpassung ermöglicht.

Beitrag B3 spezifiziert das Process-Group-Protocol als OPC UA Sub-Protokoll in `playbooks/VIA-M3-Compiler/via_protocols/process_group_protocol.md` mit Integration der open62541 Dynamic Address Space API und einem Hybrid-Modell aus statischen Typen und dynamischen Instanzen.

Beitrag B4 führt einen Benchmark-Vergleich zwischen Compiler-Optimierung, Service Mesh und manueller Konfiguration durch, wobei die Evaluationsumgebung einen 3-Node Kubernetes Cluster (64 Core, 256 GB RAM) und Mininet für Skalierungstests bis 1.000 Nodes umfasst, mit vier Szenarien S1-S4 gemäß Abschnitt 4.3.2.

Beitrag B5 liefert einen Skalierbarkeitsnachweis für mehr als 100.000 Services mit hierarchischer Gruppierung, wobei das Edge-Group-Protocol hierarchische Gruppierung (Edge-Groups → Cluster-Groups → Global) ermöglicht mit dem Ziel linearen Skalierungsverhaltens (Hypothese H3).

### 7.2 Praktische Ergebnisse

Die praktischen Ergebnisse gliedern sich in vier Deliverables. Ergebnis E1 umfasst einen M2-SDK-Compiler Prototyp mit IPC-Optimizer als Open-Source-Implementierung, realisiert in C++20/23 unter `playbooks/VIA-M2-SDK/` mit vollständigem Testframework, der lauffähige M1-Systemprojekte in `playbooks/VIA-M1-System/` generiert.

Ergebnis E2 liefert eine Benchmark-Suite für IPC-Performance mit Metriken für Latenz (P50/P95/P99 Perzentile), Throughput (Messages/s), CPU-Last (%), und Memory Footprint (MB), wobei automatische Testausführung über das generierte Deploy-Protocol erfolgt.

Ergebnis E3 implementiert einen Use-Case für SCADA, MES und PLC-Edge-Integration als exemplarisches Szenario mit 100 PLC-Edge-Devices (MIPS/ARM), 10 MES-Servern (x86), 3 SCADA-Servern (x86) und 5 Analytics-Services (Kubernetes Pods), wobei die Prozesskette 1Hz Produktionsdaten über 0.1Hz Aggregation zu Event-based Alarmen transformiert.

Ergebnis E4 erstellt einen Standardisierungsvorschlag für das VIA Process-Group-Protocol zur Einreichung bei der OPC Foundation, umfassend die VIA Custom Companion Specification (VIAProcessType, VIARouterType, VIASchedulerType, VIARegistryType), dokumentiert als OPC UA NodeSet XML zur Prüfung als offizielle Companion Spec.

### 7.3 Konkrete Evaluation-Kriterien

#### 7.3.1 Use-Case-Szenario: Automobilproduktion (Exemplarisch)

Das exemplarische Use-Case-Szenario aus der Automobilproduktion dient zur Validierung der VIA-Architektur in einem realistischen industriellen Kontext. Die System-Architektur umfasst 100 PLC-Edge-Devices für Roboterarme, Förderbänder und Prüfstationen auf MIPS oder ARM mit Linux, 10 MES-Server als Manufacturing Execution System auf x86 mit Windows Server, 3 SCADA-Server für Supervisory Control und Visualisierung auf x86 mit Linux, sowie 5 Analytics-Services für Predictive Maintenance und Quality Control als Kubernetes Pods.

Die exemplarische Prozesskette verläuft wie folgt: PLC-Edge sendet Produktionsdaten an MES mit 1 Hz Frequenz und 1 KB Nachrichtengröße, MES aggregiert und sendet Daten an Analytics mit 0.1 Hz und 10 KB, Analytics generiert Alarme und Prognosen für SCADA Event-based mit 100 Bytes, und SCADA sendet Steuerkommandos zurück an PLC-Edge mit 0.5 Hz und 50 Bytes.

Die quantitativen Erfolgsmetriken definieren messbare Zielwerte: Latenz P95 unter 5ms für die End-to-End Prozesskette, Throughput über 10.000 Messages pro Sekunde für das Gesamtsystem, CPU-Last unter 20% pro Service, Memory Footprint unter 50 MB pro Service, sowie Entwicklungszeit-Reduktion von 8 Stunden manuell auf 2 Stunden metamodell-generiert, was einer 75% Reduktion entspricht.

#### 7.3.2 Vergleich mit Baselines
| Metrik | gRPC (manuell) | Istio Service Mesh | UNIX Sockets | VIA (Ziel) |
|--------|---------------|-------------------|--------------|------------|
| Latenz P95 | 2-5ms | 10-15ms | 0.05ms (lokal) | 1-3ms |
| Throughput | 50k Msg/s | 30k Msg/s | 200k Msg/s (lokal) | 80k Msg/s |
| CPU-Last | 15% | 25% | 5% (lokal) | 12% |
| Config-Zeit | 8h | 4h (Runtime-Auto) | N/A (lokal only) | 2h (Compile-Auto) |

### 7.4 Limitationen

Die Forschungsarbeit unterliegt vier wesentlichen Limitationen. Limitation L1 besteht darin, dass Compile-Time-Optimierung eine statische Topologie erfordert, wobei dynamische Änderungen eine Neu-Compilation notwendig machen, was die Flexibilität zur Laufzeit einschränkt.

Limitation L2 liegt darin, dass die entwickelten M3-Modellelemente noch nicht in der offiziellen AAS-Spezifikation standardisiert sind, wodurch Interoperabilität mit anderen AAS-Implementierungen zunächst begrenzt ist.

Limitation L3 betrifft die Cross-Architektur-Performance, die zwischen verschiedenen Plattformen variiert (MIPS vs. x86), was unterschiedliche Optimierungsergebnisse für heterogene Systeme zur Folge hat.

Limitation L4 besteht darin, dass die Laborumgebung mit drei Nodes Extrapolation auf mehr als 50.000 Geräte erfordert, wobei Skalierungsverhalten in Produktionsumgebungen von simulierten Ergebnissen abweichen kann.

---

## 8. Zeitplan (Fokus Prozesskommunikation)

Der Zeitplan gliedert sich in sechs Phasen mit einer Gesamtdauer von 24 Wochen (circa 6 Monate). Phase 1 umfasste Research und Analyse zu AAS, OPC UA und IPC über vier Wochen und ist abgeschlossen. Phase 2 fokussiert auf Playbook und M3-Metamodell-Design über zwei Wochen und befindet sich derzeit in Bearbeitung.

Phase 3 erstreckt sich über sechs Wochen zur Entwicklung des M2-SDK-Compiler Prototyps mit IPC-Optimizer. Woche 1-2 implementieren den graph-basierten Optimierungsalgorithmus, Woche 3-4 realisieren die IPC-Mechanismus-Implementierung für Pipe, Socket, TCP, File-Queue und Thread, und Woche 5-6 spezifizieren das Process-Group-Protocol unter OPC UA.

Phase 4 umfasst vier Wochen für Benchmark-Suite und Use-Case. Woche 1-2 implementieren die Benchmark-Suite für Latenz, Throughput, CPU und Memory, während Woche 3-4 den Automobilproduktion Use-Case mit SCADA, MES und PLC realisieren.

Phase 5 widmet sich über vier Wochen der Evaluation und Vergleichsmessungen. Woche 1 führt Baseline-Messungen für gRPC, Istio und UNIX Sockets durch, Woche 2-3 erheben VIA-Messungen und Skalierungstests, und Woche 4 wertet die Ergebnisse aus und validiert die Hypothesen H1-H4.

Phase 6 erstreckt sich über vier Wochen für Dokumentation und Publikation. Woche 1-2 verfassen den Forschungsbericht, Woche 3 bereitet ein Paper für INDIN oder ETFA-Konferenz vor, und Woche 4 erstellt den OPC Foundation Standardisierungsvorschlag.

---

## 9. Literaturverzeichnis

### 9.1 Standards
1. IEC 63278 (2024). Asset Administration Shell
2. IEC 62541 (2020). OPC Unified Architecture
3. ISO/IEC 20922 (2016). MQTT Protocol
4. ISA-95 (2010). Enterprise-Control System Integration

### 9.2 Forschungsarbeiten (Santiago Soler Perez Olaya)
5. Soler Perez Olaya, S. et al. (2024). Dynamic Multi-Message Broker for I4.0 AAS
6. Soler Perez Olaya, S. et al. (2024). SOA for Digital Twins with gRPC and Protobuf
7. Soler Perez Olaya, S. & Wollschlaeger, M. (2022). CMFM Generality Hierarchy
8. Soler Perez Olaya, S. et al. (2019). CMFM for Heterogeneous Industrial Networks
9. Soler Perez Olaya, S. (2019). Role of CMFM in Network Management. PhD Thesis, TU Dresden

### 9.3 Open-Source Projekte
10. aas-core-works (2024). AAS SDKs and Tools. https://github.com/aas-core-works
11. open62541 (2024). OPC UA C99 Implementation. https://github.com/open62541/open62541
12. OPC Foundation (2024). UA-Nodeset Repository. https://github.com/OPCFoundation/UA-Nodeset

### 9.4 IPC & Service Mesh (Related Work)
13. Vinoski, S. (2006). Advanced Message Queuing Protocol. IEEE Internet Computing.
14. Hintjens, P. (2013). ZeroMQ: Messaging for Many Applications. O'Reilly Media.
15. OMG (2015). Data Distribution Service (DDS) v1.4. Object Management Group.
16. Li, H. et al. (2019). Understanding the overhead of service mesh. SoCC'19.
17. Istio Project (2024). Performance Benchmarks. https://istio.io/latest/docs/ops/deployment/performance-and-scalability/

### 9.5 Compiler-Optimierung & Metamodelle
18. Parr, T. (2010). Language Implementation Patterns. Pragmatic Bookshelf.
19. Lattner, C. & Adve, V. (2004). LLVM: A Compilation Framework. CGO'04.
20. Czarnecki, K. & Eisenecker, U. (2000). Generative Programming. Addison-Wesley.
21. Völter, M. et al. (2013). Model-Driven Software Development. Wiley.

### 9.6 IPC Performance Studies
22. Sridharan, A. et al. (2003). UNIX Domain Sockets vs. Internet Sockets. Linux Journal.
23. Google (2024). gRPC Performance Benchmarks. https://grpc.io/docs/guides/benchmarking/
24. Redis Labs (2019). Inter-Process Communication Performance Analysis.

### 9.7 Industrial Automation & Edge Computing
25. Plattform Industrie 4.0 (2023). Asset Administration Shell Reading Guide.
26. Sauter, T. (2010). The Three Generations of Field-Level Networks. IEEE Industrial Electronics Magazine.
27. Shi, W. et al. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal.

---

**Status**: ✅ Strukturiert mit Stichpunkten aus README.md & TODO.md
**Basis**: Phase 1 + Phase 2 Research-Erkenntnisse
**Nächste Schritte**: Literaturrecherche Quellen 13-27, Detaillierung nach Implementation, Transformation zu .docx
